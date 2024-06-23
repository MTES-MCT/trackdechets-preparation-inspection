import base64
import logging

from celery import current_task, group
from django.conf import settings
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from weasyprint import CSS, HTML
from weasyprint.text.fonts import FontConfiguration

from .constants import PLOTLY_GRAPHS_TO_RENDER_IN_PDF
from .data_processing import SheetProcessor
from .models import ComputedInspectionData
from .plotly_utils import data_to_bs64_plot
from django.utils import timezone
logger = logging.getLogger(__name__)

WEB_QUEUE = "web-queue"
API_QUEUE = "api-queue"


def render_pdf_graph_fn(computed_pk, name):
    """Render a plolty png to base64 from stored precomputed data"""
    if name not in PLOTLY_GRAPHS_TO_RENDER_IN_PDF:
        raise Exception("Invalid argument")

    with transaction.atomic():
        computed = get_object_or_404(ComputedInspectionData.objects.select_for_update(), pk=computed_pk)
        if not computed.is_computed:
            return
        graph_data = getattr(computed, f"{name}_data")
        graph = ""
        if graph_data is not None and graph_data != "{}":
            graph = data_to_bs64_plot(graph_data)
        name = f"{name}_graph" if "_graph" not in name else name
        setattr(computed, name, graph)

        computed.save()


def prepare_sheet_fn(computed_pk):
    """
    Pollable task to prepare html view.

    :param computed_pk: ComputedInspectionData pk
    """
    errors = []
    processor = SheetProcessor(computed_pk)

    try:
        processor.process()
    except Exception as e:  # noqa
        current_task.update_state(state="ERROR", meta={"progress": 100})
        ComputedInspectionData.objects.mark_as_failed(computed_pk)
        logger.error(e)
        return {"errors": "Error"}
    current_task.update_state(state="DONE", meta={"progress": 100})

    return {"errors": errors, "redirect": "html"}


def render_pdf_sheet_fn(computed_pk: str):
    sheet = ComputedInspectionData.objects.get(pk=computed_pk)
    ctx = {
        "sheet": sheet,
        "bsdd_created_rectified_graph": sheet.bsdd_created_rectified_graph,
        "bsdd_stock_graph": sheet.bsdd_stock_graph,
        "bsdd_non_dangerous_created_rectified_graph": sheet.bsdd_non_dangerous_created_rectified_graph,
        "bsdd_non_dangerous_stock_graph": sheet.bsdd_non_dangerous_stock_graph,
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
        "icpe_2770_graph": sheet.icpe_2770_graph,
        "icpe_2790_graph": sheet.icpe_2790_graph,
        "icpe_2760_1_graph": sheet.icpe_2760_1_graph,
        "icpe_2771_graph": sheet.icpe_2770_graph,
        "icpe_2791_graph": sheet.icpe_2790_graph,
        "icpe_2760_2_graph": sheet.icpe_2760_2_graph,
        "bsda_worker_quantity_graph": sheet.bsda_worker_quantity_graph,
        "bs_transported_graph": sheet.transporter_bordereaux_stats_graph,
        "bs_quantities_transported_graph": sheet.quantities_transported_stats_graph,
        "dnd_statements_graph": sheet.non_dangerous_waste_statements_graph,
        "dnd_quantity_graph": sheet.non_dangerous_waste_quantities_graph,
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


def render_pdf_fn(computed_pk: str, render_indiv_graph_api_fn):
    """
    Pollable task to prepare pdf rendering by computing each graph in a distinct async task.

    :param computed_pk: ComputedInspectionData pk
    """
    errors = []

    computed = ComputedInspectionData.objects.get(pk=computed_pk)
    if not computed.is_computed:
        return
    computed.pdf_rendering_start = timezone.now()
    graph_rendering = group(
        (render_indiv_graph_api_fn.s(computed_pk, name) for name in PLOTLY_GRAPHS_TO_RENDER_IN_PDF)
    )

    result = graph_rendering.delay()

    while not result.ready():
        pass

    ComputedInspectionData.objects.mark_as_graph_rendered(pk=computed_pk)
    try:
        render_pdf_sheet_fn(computed_pk)

    except Exception as e:  # noqa
        current_task.update_state(state="ERROR", meta={"progress": 100})
        return {"errors": "Error"}
    computed.pdf_rendering_end = timezone.now()
    current_task.update_state(state="DONE", meta={"progress": 100})
    return {"errors": errors, "redirect": "pdf"}
