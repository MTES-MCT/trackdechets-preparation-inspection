from typing import Dict, List, Tuple

import pandas as pd
from celery import current_task

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
    computed.waste_origin_map = waste_origin_map.build()

    outliers_data = AdditionalInfoComponent(siret, additional_data)

    computed.outliers_data = outliers_data.build()

    computed.save()


@app.task
def prepare_sheet(computed_pk):
    """
    Pollable task to check siret existence and validity on api.

    :param data: {"siret": row.siret, "row_number": row.index}
    """
    errors = []

    prepare_sheet_fn(computed_pk)

    current_task.update_state(state="DONE", meta={"progress": 100})

    return errors
