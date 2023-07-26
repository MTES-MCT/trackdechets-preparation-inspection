from datetime import datetime
from typing import Dict, List, Tuple

import pandas as pd

from .constants import BSDA, BSDASRI, BSDD, BSDD_NON_DANGEROUS, BSFF, BSVHU
from .data_extract import (
    load_and_preprocess_regions_geographical_data,
    load_departements_regions_data,
    load_mapping_rubrique_processing_operation_code,
    load_waste_code_data,
)
from .database import (
    build_bsda_query,
    build_bsdasri_query,
    build_bsdd_non_dangerous_query,
    build_bsdd_query,
    build_bsff_packagings_query,
    build_bsff_query,
    build_bsvhu_query,
    build_query_company,
    build_revised_bsda_query,
    build_revised_bsdd_query,
    get_agreement_data,
    get_icpe_data,
)
from .graph_processors.html_components_processors import (
    AdditionalInfoProcessor,
    BsdCanceledTableProcessor,
    BsdStatsProcessor,
    ICPEItemsProcessor,
    InputOutputWasteTableProcessor,
    PrivateIndividualsCollectionsTableProcessor,
    QuantityOutliersTableProcessor,
    ReceiptAgrementsProcessor,
    SameEmitterRecipientTableProcessor,
    StorageStatsProcessor,
    TraceabilityInterruptionsProcessor,
    WasteIsDangerousStatementsProcessor,
)
from .graph_processors.plotly_components_processors import (
    BsdQuantitiesGraph,
    BsdTrackedAndRevisedProcessor,
    WasteOriginProcessor,
    WasteOriginsMapProcessor,
)
from .models import ComputedInspectionData
from .utils import to_verbose_company_types

WASTE_CODES_DATA = load_waste_code_data()
DEPARTEMENTS_REGION_DATA = load_departements_regions_data()
REGIONS_GEODATA = load_and_preprocess_regions_geographical_data()
PROCESSING_OPERATION_CODE_RUBRIQUE_MAPPING = (
    load_mapping_rubrique_processing_operation_code()
)


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
        "bsd_type": BSDD_NON_DANGEROUS,
        "bs_data": build_bsdd_non_dangerous_query,
        "bs_revised_data": build_revised_bsdd_query,
    },
    {
        "bsd_type": BSDA,
        "bs_data": build_bsda_query,
        "bs_revised_data": build_revised_bsda_query,
    },
    {"bsd_type": BSDASRI, "bs_data": build_bsdasri_query},
    {
        "bsd_type": BSFF,
        "bs_data": build_bsff_query,
        "packagings_data": build_bsff_packagings_query,
    },
    {"bsd_type": BSVHU, "bs_data": build_bsvhu_query},
]


class SheetProcessor:
    def __init__(self, computed_pk, force_recompute=False):
        self.computed = ComputedInspectionData.objects.get(pk=computed_pk)
        self.force_recompute = force_recompute
        self.siret = self.computed.org_id
        self.data_start_date = datetime(2022, 1, 1)
        self.data_end_date = datetime.utcnow()
        self.company_id = None
        self.bsds_dfs = {}
        self.revised_bsds_dfs = {}
        self.bsff_packagings_df = None

    def _process_company_data(self):
        company_data_df = build_query_company(
            siret=self.siret, date_params=["created_at"]
        )
        self.company_id = company_data_df.iloc[0].id
        company_values = company_data_df.iloc[0]
        self.computed.company_name = company_values.get("name")
        self.computed.company_address = company_values.get("address")
        self.computed.company_profiles = to_verbose_company_types(
            company_values.get("company_types")
        )
        agreement_data = ReceiptAgrementsProcessor(get_agreement_data(company_data_df))
        self.computed.agreement_data = agreement_data.build()

        self.computed.save()

    def _prepare_plotly_graph(self):
        all_bsd_data_empty = True

        data_date_interval = (self.data_start_date, self.data_end_date)

        for bsd_type, df in self.bsds_dfs.items():
            if not len(df):
                continue
            created_rectified_graph = BsdTrackedAndRevisedProcessor(
                self.siret,
                df,
                data_date_interval,
                self.revised_bsds_dfs.get(bsd_type, None),
            )
            created_rectified_graph_data = created_rectified_graph.build()
            if created_rectified_graph_data:
                all_bsd_data_empty = False
            setattr(
                self.computed,
                f"{bsd_type}_created_rectified_data",
                created_rectified_graph_data,
            )

            quantity_variables = ["quantity_received"]
            packaging_data = None
            if bsd_type == BSDASRI:
                quantity_variables = ["quantity_received", "volume"]
            if bsd_type == BSFF:
                quantity_variables = ["acceptation_weight"]
                packaging_data = self.bsff_packagings_df

            stock_graph = BsdQuantitiesGraph(
                self.siret,
                df,
                data_date_interval,
                quantity_variables_names=quantity_variables,
                packagings_data=packaging_data,
            )
            stock_graph_data = stock_graph.build()
            if stock_graph_data:
                all_bsd_data_empty = False
            setattr(self.computed, f"{bsd_type}_stock_data", stock_graph_data)

            stock_graph = BsdQuantitiesGraph(
                self.siret,
                df,
                data_date_interval,
                quantity_variables_names=quantity_variables,
                packagings_data=packaging_data,
            )
            stock_graph_data = stock_graph.build()
            if stock_graph_data:
                all_bsd_data_empty = False
            setattr(self.computed, f"{bsd_type}_stock_data", stock_graph_data)

            stats_graph = BsdStatsProcessor(
                self.siret,
                df,
                data_date_interval,
                quantity_variables_names=quantity_variables,
                bs_revised_data=self.revised_bsds_dfs.get(bsd_type, None),
                packagings_data=packaging_data,
            )
            stats_graph_data = stats_graph.build()
            if stats_graph_data:
                all_bsd_data_empty = False
            setattr(self.computed, f"{bsd_type}_stats_data", stats_graph_data)

        self.computed.all_bsd_data_empty = all_bsd_data_empty

    def _process_bsds(self):
        additional_data = {"date_outliers": {}, "quantity_outliers": {}}

        data_date_interval = (self.data_start_date, self.data_end_date)

        for bsd_config in bsds_config:
            bsd_type = bsd_config["bsd_type"]
            # compute and store df in a dict
            df = bsd_config["bs_data"](
                siret=self.computed.org_id,
                data_start_date=self.data_start_date,
                data_end_date=self.data_end_date,
            )
            self.bsds_dfs[bsd_type] = df

            bs_data_df, date_outliers = get_outliers_datetimes_df(
                df, date_columns=["sent_at", "received_at", "processed_at"]
            )
            if len(date_outliers) > 0:
                additional_data["date_outliers"][bsd_type] = date_outliers

            bs_revised_data = bsd_config.get("bs_revised_data", None)
            if bs_revised_data:
                revised_df = bs_revised_data(
                    company_id=self.company_id,
                    data_start_date=self.data_start_date,
                    data_end_date=self.data_end_date,
                )
                if len(revised_df) > 0:
                    self.revised_bsds_dfs[bsd_type] = revised_df

            if bsd_type == BSFF:
                bsff_packagings_data = bsd_config.get("packagings_data")(
                    siret=self.computed.org_id,
                    data_start_date=self.data_start_date,
                    data_end_date=self.data_end_date,
                )
                if len(bsff_packagings_data) > 0:
                    self.bsff_packagings_df = bsff_packagings_data

        # prepare plotly graph as json from each precompute dataframes
        self._prepare_plotly_graph()

        icpe_data = get_icpe_data(self.computed.org_id)

        icpe_processor = ICPEItemsProcessor(
            self.computed.org_id,
            icpe_data,
            self.bsds_dfs,
            PROCESSING_OPERATION_CODE_RUBRIQUE_MAPPING,
        )
        self.computed.icpe_data = icpe_processor.build()

        table = InputOutputWasteTableProcessor(
            self.siret, self.bsds_dfs, data_date_interval, WASTE_CODES_DATA
        )
        self.computed.input_output_waste_data = table.build()

        storage_stats = StorageStatsProcessor(
            self.siret,
            self.bsds_dfs,
            WASTE_CODES_DATA,
            data_date_interval,
        )
        self.computed.storage_data = storage_stats.build()

        waste_origin = WasteOriginProcessor(
            self.siret,
            self.bsds_dfs,
            DEPARTEMENTS_REGION_DATA,
            data_date_interval,
        )
        self.computed.waste_origin_data = waste_origin.build()

        waste_origin_map = WasteOriginsMapProcessor(
            self.siret,
            self.bsds_dfs,
            DEPARTEMENTS_REGION_DATA,
            REGIONS_GEODATA,
            data_date_interval,
        )
        self.computed.waste_origin_map_data = waste_origin_map.build()

        outliers_data = AdditionalInfoProcessor(self.siret, additional_data)

        self.computed.outliers_data = outliers_data.build()

        traceability_interruptions = TraceabilityInterruptionsProcessor(
            self.siret,
            self.bsds_dfs[BSDD],
            WASTE_CODES_DATA,
            data_date_interval,
        )
        self.computed.traceability_interruptions_data = (
            traceability_interruptions.build()
        )

        waste_is_dangerous_statements = WasteIsDangerousStatementsProcessor(
            self.siret,
            self.bsds_dfs[BSDD],
            WASTE_CODES_DATA,
            data_date_interval,
        )
        self.computed.waste_is_dangerous_statements_data = (
            waste_is_dangerous_statements.build()
        )

        bsd_canceled_table = BsdCanceledTableProcessor(
            self.siret,
            self.bsds_dfs,
            self.revised_bsds_dfs,
            data_date_interval,
        )
        self.computed.bsd_canceled_data = bsd_canceled_table.build()

        same_emitter_recipient_table = SameEmitterRecipientTableProcessor(
            self.bsds_dfs,
            data_date_interval,
        )
        self.computed.same_emitter_recipient_data = same_emitter_recipient_table.build()

        private_individuals_collections_table = (
            PrivateIndividualsCollectionsTableProcessor(
                self.siret,
                self.bsds_dfs[BSDA],
                data_date_interval,
            )
        )
        self.computed.private_individuals_collections_data = (
            private_individuals_collections_table.build()
        )
        quantity_outliers_table = QuantityOutliersTableProcessor(self.bsds_dfs)
        self.computed.quantity_outliers_data = quantity_outliers_table.build()

        self.computed.state = ComputedInspectionData.StateChoice.COMPUTED
        self.computed.save()

    def process(self):
        self._process_company_data()
        self._process_bsds()
