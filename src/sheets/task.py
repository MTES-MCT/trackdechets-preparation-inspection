import base64

from celery import current_task, group
from django.conf import settings
from django.template.loader import render_to_string
from weasyprint import CSS, HTML
from weasyprint.text.fonts import FontConfiguration

from config.celery_app import app
from sheets.models import ComputedInspectionData

from .constants import ALLOWED_NAMES
from .data_processing import prepare_sheet_fn
from .rendering_helpers import render_pdf_graph_fn


@app.task
def render_indiv_graph(computed_pk, name):
    render_pdf_graph_fn(computed_pk, name)
    return True


@app.task
def prepare_sheet(computed_pk):
    """
     Pollable task to prepare html view.

    :param computed_pk: ComputedInspectionData pk
    """
    errors = []

    prepare_sheet_fn(computed_pk)

    current_task.update_state(state="DONE", meta={"progress": 100})

    return {"errors": errors, "redirect": "html"}


@app.task
def render_pdf_sheet(computed_pk: str):
    sheet = ComputedInspectionData.objects.get(pk=computed_pk)
    ctx = {
        "sheet": sheet,
        "bsdd_created_rectified_graph": sheet.bsdd_created_rectified_graph,
        "bsdd_stock_graph": sheet.bsdd_stock_graph,
        "bsda_created_rectified_graph": sheet.bsda_created_rectified_graph,
        "bsda_stock_graph": sheet.bsda_stock_graph,
        "bsdasri_created_rectified_graph": sheet.bsdasri_created_rectified_graph,
        "bsdasri_stock_graph": sheet.bsdasri_stock_graph,
        "bsff_created_rectified_graph": sheet.bsff_created_rectified_graph,
        "bsff_stock_graph": sheet.bsff_stock_graph,
        "bsvhu_created_rectified_graph": sheet.bsvhu_created_rectified_graph,
        "bsvhu_stock_graph": sheet.bsvhu_stock_graph,
        "waste_origin_graph": sheet.waste_origin_graph,
        "waste_origin_map_graph": sheet.waste_origin_map_graph,
        "skip_css": True,
    }

    content = render_to_string("sheets/sheetpdf.html", ctx)
    font_config = FontConfiguration()
    html = HTML(string=content, base_url=settings.BASE_URL)
    with open(settings.STATICFILES_DIR / "css" / "pdf.css") as f:
        css_content = f.read()

    css = CSS(
        string=css_content,
        font_config=font_config,
        base_url=f"{settings.BASE_URL}/static/css/",
    )
    tmp_pdf_path = f"/tmp/{sheet.pk}.pdf"

    html.write_pdf(tmp_pdf_path, stylesheets=[css], font_config=font_config)

    with open(tmp_pdf_path, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode("ascii")
        sheet.pdf = encoded_string
        sheet.save()
    # delete tmp


@app.task
def render_pdf(computed_pk: str):
    """
    Pollable task to prepare pdf rendering by computing each graph in a distinct async task.

    :param computed_pk: ComputedInspectionData pk
    """
    errors = []

    computed = ComputedInspectionData.objects.get(pk=computed_pk)
    if not computed.is_computed:
        return

    graph_rendering = group(
        (render_indiv_graph.s(computed_pk, name) for name in ALLOWED_NAMES)
    )

    result = graph_rendering.delay()

    while not result.ready():
        pass

    computed = ComputedInspectionData.objects.get(pk=computed_pk)
    computed.mark_as_graph_rendered()

    pdf = render_pdf_sheet.delay(computed_pk)
    while not pdf.ready():
        pass

    current_task.update_state(state="DONE", meta={"progress": 100})
    return {"errors": errors, "redirect": "pdf"}
