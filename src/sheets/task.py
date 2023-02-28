import base64
from typing import Dict, List, Tuple

import pandas as pd
from celery import current_task, group
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from weasyprint import CSS, HTML

from config.celery_app import app
from sheets.graph_components.data_components import (
    AdditionalInfoComponent,
    BSStatsComponent,
    ICPEItemsComponent,
    InputOutputWasteTableComponent,
    StorageStatsComponent,
)
from sheets.graph_components.viz_components import (
    BSCreatedAndRevisedComponent,
    BsddGraph,
    WasteOriginsComponent,
    WasteOriginsMapComponent,
)
from sheets.models import ComputedInspectionData

from .constants import COMPANY_TYPES
from .data_extract import (
    load_and_preprocess_regions_geographical_data,
    load_departements_regions_data,
    load_mapping_rubrique_processing_operation_code,
    load_waste_code_data,
)
from .database import (
    build_bsda_query,
    build_bsdasri_query,
    build_bsdd_query,
    build_bsff_query,
    build_bsvhu_query,
    build_query_company,
    get_agreement_data,
    get_icpe_data,
)
from .utils import data_to_bs64_plot

WASTE_CODES_DATA = load_waste_code_data()
DEPARTEMENTS_REGION_DATA = load_departements_regions_data()
REGIONS_GEODATA = load_and_preprocess_regions_geographical_data()
PROCESSING_OPERATION_CODE_RUBRIQUE_MAPPING = (
    load_mapping_rubrique_processing_operation_code()
)


def to_verbose_company_types(db_company_types):
    return [
        COMPANY_TYPES.get(ct) for ct in db_company_types if ct in COMPANY_TYPES.keys()
    ]


def get_quantity_outliers(df: pd.DataFrame, bs_type: str) -> pd.DataFrame:
    """Filter out lines from 'bordereau' DataFrame with inconsistent received quantity.
    The rules to identify outliers in received quantity are business rules and may be tweaked in the future.

    Parameters
    ----------
    df : DataFrame
        DataFrame with 'bordereau' data.
    bs_type : str
        Name of the 'bordereau' (BSDD, BSDA, BSFF, BSVHU or BSDASRI).

    Returns
    -------
    DataFrame
        DataFrame with lines with received quantity outliers removed.
    """

    df = df.copy()
    if bs_type in ["BSDD", "BSDA"]:
        df_quantity_outliers = df[
            (df["quantity_received"] > 40)
            & (df["transporter_transport_mode"] == "ROAD")
        ]
    elif bs_type == "BSDASRI":
        df_quantity_outliers = df[
            (df["quantity_received"] > 20)
            & (df["transporter_transport_mode"] == "ROAD")
        ]
    elif bs_type == "BSVHU":
        df_quantity_outliers = df[(df["quantity_received"] > 40)]
    elif bs_type == "BSFF":
        df_quantity_outliers = df[df["quantity_received"] > 20]

    return df_quantity_outliers


def get_outliers_datetimes_df(
    df: pd.DataFrame, date_columns: List[str]
) -> Tuple[pd.DataFrame, Dict[str, pd.DataFrame]]:
    """For a given DataFrame, separate lines with date outliers
    from lines with consistent (parsable) dates in provided list of date columns.

    Parameters
    ----------
    df : DataFrame
        DataFrame with raw (str) date data.
    date_columns : list of str
        Names of columns to parse as dates in pandas (time-zone aware dates are casted to UTC).

    Returns
    -------
    Tuple consisting of :
    1. DataFrame with consistent dates.
    2. Dict with keys being date column names and values being the DataFrame's lines with inconsistent date for this column.
    """
    df = df.copy()
    outliers = {}
    idx_with_outliers = set()

    for colname in date_columns:
        time_data = pd.to_datetime(df[colname], errors="coerce")
        outliers_df = df[time_data.isna() & (~df[colname].isin(["None", "NaT"]))]
        if len(outliers_df) > 0:
            idx_with_outliers.update(outliers_df.index.tolist())
            outliers[colname] = outliers_df

    if len(idx_with_outliers) > 0:
        df = df[~df.index.isin(idx_with_outliers)]

    for colname in date_columns:
        df[colname] = pd.to_datetime(
            df[colname].replace(["None", "NaT"], pd.NaT), utc=True
        )

    df["created_at"] = pd.to_datetime(
        df["created_at"].replace(["None", "NaT"], pd.NaT), utc=True
    )
    return df, outliers


class SheetBuilder:
    pass


def prepare_sheet_fn(computed_pk):
    computed = ComputedInspectionData.objects.get(pk=computed_pk)

    if not computed.is_initial:
        return
    siret = computed.org_id
    company_data_df = build_query_company(siret=siret, date_params=["created_at"])
    company_values = company_data_df.iloc[0]
    computed.company_name = company_values.get("name")
    computed.company_address = company_values.get("address")
    computed.company_profiles = to_verbose_company_types(
        company_values.get("company_types")
    )

    computed.save()
    additional_data = {"date_outliers": {}, "quantity_outliers": {}}

    computed.agreement_data = get_agreement_data(company_data_df)
    # todo: loop over a config object
    # bsdd
    bsdd_df = build_bsdd_query(siret=computed.org_id, date_params=["processed_at"])
    quantity_outliers = get_quantity_outliers(bsdd_df, "BSDD")
    if len(quantity_outliers) > 0:
        additional_data["quantity_outliers"]["BSDD"] = quantity_outliers
    bs_data_df, date_outliers = get_outliers_datetimes_df(
        bsdd_df, date_columns=["sent_at", "received_at", "processed_at"]
    )
    if len(date_outliers) > 0:
        additional_data["date_outliers"]["BSDD"] = date_outliers

    # bsda
    bsda_df = build_bsda_query(siret=computed.org_id, date_params=["processed_at"])
    quantity_outliers = get_quantity_outliers(bsda_df, "BSDA")
    if len(quantity_outliers) > 0:
        additional_data["quantity_outliers"]["BSDA"] = quantity_outliers
    bs_data_df, date_outliers = get_outliers_datetimes_df(
        bsda_df, date_columns=["sent_at", "received_at", "processed_at"]
    )
    if len(date_outliers) > 0:
        additional_data["date_outliers"]["BSDA"] = date_outliers

    # dasri
    bsdasri_df = build_bsdasri_query(
        siret=computed.org_id, date_params=["processed_at"]
    )
    quantity_outliers = get_quantity_outliers(bsdasri_df, "BSDASRI")
    if len(quantity_outliers) > 0:
        additional_data["quantity_outliers"]["BSDASRI"] = quantity_outliers
    bs_data_df, date_outliers = get_outliers_datetimes_df(
        bsdasri_df, date_columns=["sent_at", "received_at", "processed_at"]
    )
    if len(date_outliers) > 0:
        additional_data["date_outliers"]["BSDASRI"] = date_outliers

    # bsff
    bsff_df = build_bsff_query(siret=computed.org_id, date_params=["processed_at"])
    quantity_outliers = get_quantity_outliers(bsff_df, "BSFF")
    if len(quantity_outliers) > 0:
        additional_data["quantity_outliers"]["BSFF"] = quantity_outliers
    bs_data_df, date_outliers = get_outliers_datetimes_df(
        bsff_df, date_columns=["sent_at", "received_at", "processed_at"]
    )
    if len(date_outliers) > 0:
        additional_data["date_outliers"]["BSFF"] = date_outliers

    # bsvhu
    bsvhu_df = build_bsvhu_query(siret=computed.org_id, date_params=["processed_at"])
    quantity_outliers = get_quantity_outliers(bsvhu_df, "BSVHU")
    if len(quantity_outliers) > 0:
        additional_data["quantity_outliers"]["BSVHU"] = quantity_outliers
    bs_data_df, date_outliers = get_outliers_datetimes_df(
        bsvhu_df, date_columns=["sent_at", "received_at", "processed_at"]
    )
    if len(date_outliers) > 0:
        additional_data["date_outliers"]["BSVHU"] = date_outliers

    bsds_dfs = {
        "bsdd": bsdd_df,
        "bsda": bsda_df,
        "bsdasri": bsdasri_df,
        "bsff": bsff_df,
        "bsvhu": bsvhu_df,
    }

    icpe_data = get_icpe_data(computed.org_id)

    comp = ICPEItemsComponent(
        computed.org_id, icpe_data, bsds_dfs, PROCESSING_OPERATION_CODE_RUBRIQUE_MAPPING
    )
    computed.icpe_data = comp.build()

    # bsdd
    if len(bsdd_df):
        bsdd_created_rectified_graph = BSCreatedAndRevisedComponent(siret, bsdd_df)
        computed.bsdd_created_rectified_data = bsdd_created_rectified_graph.build()
        bsdd_stock_graph = BsddGraph(siret, bsdd_df)
        computed.bsdd_stock_data = bsdd_stock_graph.build()
        #
        bsdd_stats_graph = BSStatsComponent(siret, bsdd_df)
        computed.bsdd_stats_data = bsdd_stats_graph.build()

    # bsda
    if len(bsda_df):
        bsda_created_rectified_graph = BSCreatedAndRevisedComponent(siret, bsda_df)
        computed.bsda_created_rectified_data = bsda_created_rectified_graph.build()
        bsda_stock_graph = BsddGraph(siret, bsda_df)
        computed.bsda_stock_data = bsda_stock_graph.build()
        bsda_stats_graph = BSStatsComponent(siret, bsda_df)
        computed.bsda_stats_data = bsda_stats_graph.build()

    # bsdasri
    if len(bsdasri_df):
        bsdasri_created_rectified_graph = BSCreatedAndRevisedComponent(
            siret, bsdasri_df
        )
        computed.bsdasri_created_rectified_data = (
            bsdasri_created_rectified_graph.build()
        )
        bsdasri_stock_graph = BsddGraph(siret, bsdasri_df)
        computed.bsdasri_stock_data = bsdasri_stock_graph.build()
        bsdasri_stats_graph = BSStatsComponent(siret, bsdasri_df)
        computed.bsdasri_stats_data = bsdasri_stats_graph.build()

    # bsff
    if len(bsff_df):
        bsff_created_rectified_graph = BSCreatedAndRevisedComponent(siret, bsff_df)
        computed.bsff_created_rectified_data = bsff_created_rectified_graph.build()
        bsff_stock_graph = BsddGraph(siret, bsff_df)
        computed.bsff_stock_data = bsff_stock_graph.build()
        bsff_stats_graph = BSStatsComponent(siret, bsff_df)
        computed.bsff_stats_data = bsff_stats_graph.build()

    # bsvhu
    if len(bsvhu_df):
        bsvhu_created_rectified_graph = BSCreatedAndRevisedComponent(siret, bsvhu_df)
        computed.bsvhu_created_rectified_data = bsvhu_created_rectified_graph.build()
        bsvhu_stock_graph = BsddGraph(siret, bsvhu_df)
        computed.bsvhu_stock_data = bsvhu_stock_graph.build()
        bsvhu_stats_graph = BSStatsComponent(siret, bsvhu_df)
        computed.bsvhu_stats_data = bsvhu_stats_graph.build()

    # table
    table = InputOutputWasteTableComponent(siret, bsds_dfs, WASTE_CODES_DATA)
    computed.input_output_waste_data = table.build()

    storage_stats = StorageStatsComponent(siret, bsds_dfs, WASTE_CODES_DATA)
    computed.storage_data = storage_stats.build()

    waste_origin = WasteOriginsComponent(siret, bsds_dfs, DEPARTEMENTS_REGION_DATA)
    computed.waste_origin_data = waste_origin.build()

    waste_origin_map = WasteOriginsMapComponent(
        siret, bsds_dfs, DEPARTEMENTS_REGION_DATA, REGIONS_GEODATA
    )
    computed.waste_origin_map_data = waste_origin_map.build()

    outliers_data = AdditionalInfoComponent(siret, additional_data)

    computed.outliers_data = outliers_data.build()

    computed.state = ComputedInspectionData.StateChoice.COMPUTED
    computed.save()


def render_pdf_fn(computed_pk):
    computed = ComputedInspectionData.objects.get(pk=computed_pk)
    computed.bsdd_created_rectified_graph = data_to_bs64_plot(
        computed.bsdd_created_rectified_data
    )

    computed.bsdd_stock_graph = data_to_bs64_plot(computed.bsdd_stock_data)

    computed.bsda_created_rectified_graph = data_to_bs64_plot(
        computed.bsda_created_rectified_data
    )
    computed.bsda_stock_graph = data_to_bs64_plot(computed.bsda_stock_data)

    computed.bsdasri_created_rectified_graph = data_to_bs64_plot(
        computed.bsdasri_created_rectified_data
    )
    computed.bsdasri_stock_graph = data_to_bs64_plot(computed.bsdasri_stock_data)
    computed.bsff_created_rectified_graph = data_to_bs64_plot(
        computed.bsff_created_rectified_data
    )
    computed.bsff_stock_graph = data_to_bs64_plot(computed.bsff_stock_data)
    computed.bsvhu_created_rectified_graph = data_to_bs64_plot(
        computed.bsvhu_created_rectified_data
    )
    computed.bsvhu_stock_graph = data_to_bs64_plot(computed.bsvhu_stock_data)
    computed.waste_origin_graph = data_to_bs64_plot(computed.waste_origin_data)

    computed.waste_origin_map_graph = data_to_bs64_plot(computed.waste_origin_map_data)
    computed.save()


allowed_names = [
    "bsdd_created_rectified",
    "bsdd_stock",
    "bsda_created_rectified",
    "bsda_stock",
    "bsdasri_created_rectified",
    "bsdasri_stock",
    "bsff_created_rectified",
    "bsff_stock",
    "bsvhu_created_rectified",
    "bsvhu_stock",
    "waste_origin",
    "waste_origin_map",
]


def render_pdf_graph_fn(computed_pk, name):
    if name not in allowed_names:
        raise Exception("Invalid argument")

    with transaction.atomic():
        computed = get_object_or_404(
            ComputedInspectionData.objects.select_for_update(), pk=computed_pk
        )
        if not computed.is_computed:
            return
        graph = data_to_bs64_plot(getattr(computed, f"{name}_data"))
        setattr(computed, f"{name}_graph", graph)

        computed.save()


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
        (render_indiv_graph.s(computed_pk, name) for name in allowed_names)
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
