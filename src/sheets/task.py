import base64

from celery import current_task, group
from django.template.loader import render_to_string
from weasyprint import CSS, HTML

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


# todo: import
the_css = """
/* PDF style sheet - some css properties are not or poorly supported */

/* fonts */

/* Skip most font variants for performance */

html {
  font-family: Marianne, sans-serif;
}

body {
  width: 100%;
  font-size: 11pt;

}

/* print */
@page {
  counter-increment: page;
  @top-right {
    content: "Page " counter(page) " sur " counter(pages);
    font-size: 10pt;
    color: #444;
  }
}

@page vertical {
  size: A4 portrait;
  margin: 5mm;
}

@page horizontal {
  size: A4 landscape;
  margin: 5mm;
}


.vertical {
  page: vertical;
}


.horizontal {
  page: horizontal;
}

.pagebreak { page-break-before: always; }

/*reset*/
ul { padding-left: 2rem;}

/* typo utilities */
.bold {
  font-weight: bold;
}

.pdf-text {
  font-size: 11pt;

}

/*  Margin utilities */

.mb-0 {
  margin-bottom: 0;
}

.mt-0 {
  margin-top: 0;
}

/*header*/
.header__text {
  display: inline-block;

  margin-left: 5mm;

}

.header {
  display: inline-block;
  align-items: center;
  margin-top: 1mm;
  margin-bottom: 3mm;
}

.header img {
  margin-right: 1cm;
}

/*layout*/
.row {
  display: block;
  width: 100%;
  margin-bottom: 3mm;
}


.header__title, .header__company {
  font-size: 20pt;
  margin: 0;
  line-height: 1.2;
}


/* cells */
.cell {
  display: inline-block;
  vertical-align: top;
  border-left: 3px solid #e3e3fd;
  padding: 1mm 2mm;

}

.cell:not(:first-child) {
  margin-left: 3mm;
}

.cell > * {
  margin-top: 0;
}

.cell--third {
  width: 30%;
}

.cell--bordered {
  border: 1px solid #e3e3fd;
  border-left: 5px solid #e3e3fd
}

.cell__img {
  width: 100%;
}

.cell__title {
  font-size: 14pt;
  font-weight: 500;
}


/* Tables*/
.pdf-table {
  border: 1px solid #ccc;
  border-collapse: collapse;
  font-size: 12px;
}

.pdf-table thead th {
  border: 1px solid #ccc;
  padding: 0 6px;
}

.pdf-table tbody tr {
  border: 1px solid #ccc;

}

.pdf-table tbody tr:nth-child(even) {
  background-color: #f2f2f2;
}

.pdf-table tbody td {
  border: 1px solid #ccc;
  padding: 3px 6px;

}

.td--right {
  text-align: right;
}
"""


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
    }

    content = render_to_string("sheets/sheetpdf.html", ctx)

    html = HTML(
        string=content,
    )
    css = CSS(string=the_css)

    html.write_pdf(f"/tmp/{sheet.pk}.pdf", stylesheets=[css])

    with open(f"/tmp/{sheet.pk}.pdf", "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode("ascii")

        sheet.pdf = encoded_string
        sheet.save()


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
