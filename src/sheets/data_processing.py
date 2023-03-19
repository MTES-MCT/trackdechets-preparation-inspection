from typing import Dict, List, Tuple

import pandas as pd

from .constants import BSDA, BSDASRI, BSDD, BSFF, BSVHU
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
    build_revised_bsda_query,
    build_revised_bsdd_query,
    get_agreement_data,
    get_icpe_data,
)
from .graph_components.data_components import (
    AdditionalInfoComponent,
    BSStatsComponent,
    ICPEItemsComponent,
    InputOutputWasteTableComponent,
    ReceiptAgrementsComponent,
    StorageStatsComponent,
    TraceabilityInterruptionsComponent,
)
from .graph_components.viz_components import (
    BSCreatedAndRevisedComponent,
    BsddGraph,
    WasteOriginsComponent,
    WasteOriginsMapComponent,
)
from .models import ComputedInspectionData
from .utils import to_verbose_company_types

WASTE_CODES_DATA = load_waste_code_data()
DEPARTEMENTS_REGION_DATA = load_departements_regions_data()
REGIONS_GEODATA = load_and_preprocess_regions_geographical_data()
PROCESSING_OPERATION_CODE_RUBRIQUE_MAPPING = (
    load_mapping_rubrique_processing_operation_code()
)


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
    if bs_type in [BSDD, BSDA]:
        df_quantity_outliers = df[
            (df["quantity_received"] > 40)
            & (df["transporter_transport_mode"] == "ROAD")
        ]
    elif bs_type == BSDASRI:
        df_quantity_outliers = df[
            (df["quantity_received"] > 20)
            & (df["transporter_transport_mode"] == "ROAD")
        ]
    elif bs_type == BSVHU:
        df_quantity_outliers = df[(df["quantity_received"] > 40)]
    elif bs_type == BSFF:
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


bsds_config = [
    {
        "bsd_type": BSDD,
        "bs_data": build_bsdd_query,
        "bs_revised_data": build_revised_bsdd_query,
    },
    {
        "bsd_type": BSDA,
        "bs_data": build_bsda_query,
        "bs_revised_data": build_revised_bsda_query,
    },
    {"bsd_type": BSDASRI, "bs_data": build_bsdasri_query},
    {"bsd_type": BSFF, "bs_data": build_bsff_query},
    {"bsd_type": BSVHU, "bs_data": build_bsvhu_query},
]


def prepare_sheet_fn(computed_pk, force_recompute=False):
    computed = ComputedInspectionData.objects.get(pk=computed_pk)

    if not computed.is_initial and not force_recompute:
        return
    siret = computed.org_id
    company_data_df = build_query_company(siret=siret, date_params=["created_at"])
    company_id = company_data_df.iloc[0].id
    company_values = company_data_df.iloc[0]
    computed.company_name = company_values.get("name")
    computed.company_address = company_values.get("address")
    computed.company_profiles = to_verbose_company_types(
        company_values.get("company_types")
    )

    computed.save()
    bsds_dfs = {}
    revised_bsds_dfs = {}
    additional_data = {"date_outliers": {}, "quantity_outliers": {}}

    agreement_data = ReceiptAgrementsComponent(get_agreement_data(company_data_df))
    computed.agreement_data = agreement_data.build()

    # prepare df from sql queries for each bsd type
    for bsd_config in bsds_config:
        bsd_type = bsd_config["bsd_type"]
        # compute and store df in a dict
        df = bsd_config["bs_data"](siret=computed.org_id, date_params=["processed_at"])
        bsds_dfs[bsd_type] = df
        quantity_outliers = get_quantity_outliers(df, bsd_type)
        if len(quantity_outliers) > 0:
            additional_data["quantity_outliers"][bsd_type.upper()] = quantity_outliers
        bs_data_df, date_outliers = get_outliers_datetimes_df(
            df, date_columns=["sent_at", "received_at", "processed_at"]
        )
        if len(date_outliers) > 0:
            additional_data["date_outliers"][bsd_type] = date_outliers

        bs_revised_data = bsd_config.get("bs_revised_data", None)
        if bs_revised_data:
            revised_df = bs_revised_data(
                company_id=company_id,
                date_params=["created_at"],
            )
            if len(revised_df) > 0:
                revised_bsds_dfs[bsd_type] = revised_df

    icpe_data = get_icpe_data(computed.org_id)

    comp = ICPEItemsComponent(
        computed.org_id, icpe_data, bsds_dfs, PROCESSING_OPERATION_CODE_RUBRIQUE_MAPPING
    )
    computed.icpe_data = comp.build()

    # prepare plotly graph as json from each precompute dataframes
    for bsd_type, df in bsds_dfs.items():
        if not len(df):
            continue
        created_rectified_graph = BSCreatedAndRevisedComponent(
            siret, df, revised_bsds_dfs.get(bsd_type, None)
        )
        setattr(
            computed,
            f"{bsd_type}_created_rectified_data",
            created_rectified_graph.build(),
        )
        stock_graph = BsddGraph(siret, df)
        setattr(computed, f"{bsd_type}_stock_data", stock_graph.build())

        stats_graph = BSStatsComponent(siret, df)
        setattr(computed, f"{bsd_type}_stats_data", stats_graph.build())

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

    traceability_interruptions = TraceabilityInterruptionsComponent(
        siret, bsds_dfs[BSDD], WASTE_CODES_DATA
    )
    computed.traceability_interruptions_data = traceability_interruptions.build()

    computed.state = ComputedInspectionData.StateChoice.COMPUTED
    computed.save()
