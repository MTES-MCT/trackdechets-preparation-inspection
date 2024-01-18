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
    build_bsdd_non_dangerous_transporter_query_str,
    build_bsdd_query,
    build_bsdd_transporter_query_str,
    build_bsff_packagings_query,
    build_bsff_query,
    build_bsvhu_query,
    build_query_company,
    build_revised_bsda_query,
    build_revised_bsdd_query,
    get_agreement_data,
    get_icpe_data,
    get_icpe_item_data,
    get_linked_companies_data,
    get_gistrid_data,
)
from .graph_processors.html_components_processors import (
    BsdaWorkerStatsProcessor,
    BsdCanceledTableProcessor,
    BsdStatsProcessor,
    BsdaWorkerStatsProcessor,
    FollowedWithPNTTDTableProcessor,
    ICPEItemsProcessor,
    LinkedCompaniesProcessor,
    PrivateIndividualsCollectionsTableProcessor,
    QuantityOutliersTableProcessor,
    ReceiptAgrementsProcessor,
    SameEmitterRecipientTableProcessor,
    StorageStatsProcessor,
    TraceabilityInterruptionsProcessor,
    TransporterBordereauxStatsProcessor,
    WasteFlowsTableProcessor,
    WasteIsDangerousStatementsProcessor,
    WasteProcessingWithoutICPEProcessor,
    GistridStatsProcessor,
)
from .graph_processors.plotly_components_processors import (
    BsdaWorkerQuantityProcessor,
    BsdQuantitiesGraph,
    BsdTrackedAndRevisedProcessor,
    ICPEAnnualItemProcessor,
    ICPEDailyItemProcessor,
    TransportedQuantitiesGraphProcessor,
    TransporterBordereauxGraphProcessor,
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
        "bs_transporter_data": build_bsdd_transporter_query_str,
    },
    {
        "bsd_type": BSDD_NON_DANGEROUS,
        "bs_data": build_bsdd_non_dangerous_query,
        "bs_revised_data": build_revised_bsdd_query,
        "bs_transporter_data": build_bsdd_non_dangerous_transporter_query_str,
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
        self.data_start_date = self.computed.data_start_date.replace(tzinfo=None)
        self.data_end_date = self.computed.data_end_date.replace(tzinfo=None)
        self.company_id = None
        self.bs_dfs = {}
        self.revised_bs_dfs = {}
        self.transporter_data_dfs = {}
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
        self.computed.company_created_at = company_values.get("created_at")
        agreement_data = ReceiptAgrementsProcessor(get_agreement_data(company_data_df))
        self.computed.agreement_data = agreement_data.build()

        linked_companies_data = LinkedCompaniesProcessor(
            company_siret=self.siret,
            linked_companies_data=get_linked_companies_data(self.siret),
        )
        self.computed.linked_companies_data = linked_companies_data.build()

        self.computed.save()

    def _prepare_plotly_graph(self):
        all_bsd_data_empty = True

        data_date_interval = (self.data_start_date, self.data_end_date)

        for bsd_type, df in self.bs_dfs.items():
            if not len(df):
                continue
            created_rectified_graph = BsdTrackedAndRevisedProcessor(
                self.siret,
                df,
                data_date_interval,
                self.revised_bs_dfs.get(bsd_type, None),
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

            stats_graph = BsdStatsProcessor(
                self.siret,
                df,
                data_date_interval,
                quantity_variables_names=quantity_variables,
                bs_revised_data=self.revised_bs_dfs.get(bsd_type, None),
                packagings_data=packaging_data,
            )
            stats_graph_data = stats_graph.build()
            if stats_graph_data:
                all_bsd_data_empty = False
            setattr(self.computed, f"{bsd_type}_stats_data", stats_graph_data)

        self.computed.all_bsd_data_empty = all_bsd_data_empty

        icpe_2770_data = get_icpe_item_data(siret=self.siret, rubrique="2770")
        icpe_2770_graph = ICPEDailyItemProcessor(
            icpe_2770_data,
        )
        icpe_2770_graph_data = icpe_2770_graph.build()
        setattr(self.computed, "icpe_2770_data", icpe_2770_graph_data)

        icpe_2790_data = get_icpe_item_data(siret=self.siret, rubrique="2790")
        icpe_2790_graph = ICPEDailyItemProcessor(
            icpe_2790_data,
        )
        icpe_2790_graph_data = icpe_2790_graph.build()
        setattr(self.computed, "icpe_2790_data", icpe_2790_graph_data)

        icpe_2760_data = get_icpe_item_data(siret=self.siret, rubrique="2760-1")
        icpe_2760_graph = ICPEAnnualItemProcessor(
            icpe_2760_data,
        )
        icpe_2760_graph_data = icpe_2760_graph.build()
        setattr(self.computed, "icpe_2760_data", icpe_2760_graph_data)

    def _process_bsds(self):
        data_date_interval = (self.data_start_date, self.data_end_date)

        for bsd_config in bsds_config:
            bsd_type = bsd_config["bsd_type"]
            # compute and store df in a dict
            df = bsd_config["bs_data"](
                siret=self.computed.org_id,
                data_start_date=self.data_start_date,
                data_end_date=self.data_end_date,
            )
            self.bs_dfs[bsd_type] = df

            bs_revised_data = bsd_config.get("bs_revised_data", None)
            if bs_revised_data:
                revised_df = bs_revised_data(
                    company_id=self.company_id,
                    data_start_date=self.data_start_date,
                    data_end_date=self.data_end_date,
                )
                if len(revised_df) > 0:
                    self.revised_bs_dfs[bsd_type] = revised_df

            bs_transporter_data = bsd_config.get("bs_transporter_data", None)
            if bs_transporter_data:
                transporter_data_df = bs_transporter_data(
                    siret=self.computed.org_id,
                    data_start_date=self.data_start_date,
                    data_end_date=self.data_end_date,
                )
                if len(transporter_data_df) > 0:
                    self.transporter_data_dfs[bsd_type] = transporter_data_df

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
        )
        self.computed.icpe_data = icpe_processor.build()

        table = WasteFlowsTableProcessor(
            self.siret,
            self.bs_dfs,
            self.transporter_data_dfs,
            data_date_interval,
            WASTE_CODES_DATA,
        )
        self.computed.waste_flows_data = table.build()

        storage_stats = StorageStatsProcessor(
            self.siret,
            self.bs_dfs,
            WASTE_CODES_DATA,
            data_date_interval,
        )
        self.computed.storage_data = storage_stats.build()

        waste_origin = WasteOriginProcessor(
            self.siret,
            self.bs_dfs,
            DEPARTEMENTS_REGION_DATA,
            data_date_interval,
        )
        self.computed.waste_origin_data = waste_origin.build()

        waste_origin_map = WasteOriginsMapProcessor(
            self.siret,
            self.bs_dfs,
            DEPARTEMENTS_REGION_DATA,
            REGIONS_GEODATA,
            data_date_interval,
        )
        self.computed.waste_origin_map_data = waste_origin_map.build()

        traceability_interruptions = TraceabilityInterruptionsProcessor(
            self.siret,
            self.bs_dfs[BSDD],
            WASTE_CODES_DATA,
            data_date_interval,
        )
        self.computed.traceability_interruptions_data = (
            traceability_interruptions.build()
        )

        waste_is_dangerous_statements = WasteIsDangerousStatementsProcessor(
            self.siret,
            self.bs_dfs[BSDD],
            WASTE_CODES_DATA,
            data_date_interval,
        )
        self.computed.waste_is_dangerous_statements_data = (
            waste_is_dangerous_statements.build()
        )

        bsd_canceled_table = BsdCanceledTableProcessor(
            self.siret,
            self.bs_dfs,
            self.revised_bs_dfs,
            data_date_interval,
        )
        self.computed.bsd_canceled_data = bsd_canceled_table.build()

        same_emitter_recipient_table = SameEmitterRecipientTableProcessor(
            self.bs_dfs,
            data_date_interval,
        )
        self.computed.same_emitter_recipient_data = same_emitter_recipient_table.build()

        private_individuals_collections_table = (
            PrivateIndividualsCollectionsTableProcessor(
                self.siret,
                self.bs_dfs[BSDA],
                data_date_interval,
            )
        )
        self.computed.private_individuals_collections_data = (
            private_individuals_collections_table.build()
        )

        quantity_outliers_table = QuantityOutliersTableProcessor(self.bs_dfs, self.transporter_data_dfs)
        self.computed.quantity_outliers_data = quantity_outliers_table.build()

        waste_processing_without_icpe_data = WasteProcessingWithoutICPEProcessor(
            self.siret, self.bs_dfs, icpe_data, data_date_interval
        )
        self.computed.bs_processed_without_icpe_authorization = (
            waste_processing_without_icpe_data.build()
        )

        bsda_worker_stats = BsdaWorkerStatsProcessor(
            company_siret=self.siret,
            bsda_data_df=self.bs_dfs[BSDA],
            data_date_interval=data_date_interval,
        )
        self.computed.bsda_worker_stats_data = bsda_worker_stats.build()

        bsda_worker_quantities = BsdaWorkerQuantityProcessor(
            company_siret=self.siret,
            bsda_data_df=self.bs_dfs[BSDA],
            data_date_interval=data_date_interval,
        )
        self.computed.bsda_worker_quantity_data = bsda_worker_quantities.build()

        transporter_bordereaux_graph = TransporterBordereauxGraphProcessor(
            company_siret=self.siret,
            transporters_data_df=self.transporter_data_dfs,
            bs_data_dfs={
                k: v
                for k, v in self.bs_dfs.items()
                if k not in [BSDD, BSDD_NON_DANGEROUS]
            },
            data_date_interval=data_date_interval,
        )
        self.computed.transporter_bordereaux_stats_graph_data = (
            transporter_bordereaux_graph.build()
        )

        quantities_transported_graph = TransportedQuantitiesGraphProcessor(
            company_siret=self.siret,
            transporters_data_df=self.transporter_data_dfs,
            bs_data_dfs={
                k: v
                for k, v in self.bs_dfs.items()
                if k not in [BSDD, BSDD_NON_DANGEROUS]
            },
            data_date_interval=data_date_interval,
            packagings_data_df=self.bsff_packagings_df,
        )
        self.computed.quantities_transported_stats_graph_data = (
            quantities_transported_graph.build()
        )

        transporter_bordereaux_stats = TransporterBordereauxStatsProcessor(
            company_siret=self.siret,
            transporters_data_df=self.transporter_data_dfs,
            bs_data_dfs={
                k: v
                for k, v in self.bs_dfs.items()
                if k not in [BSDD, BSDD_NON_DANGEROUS]
            },
            data_date_interval=data_date_interval,
        )
        self.computed.transporter_bordereaux_stats_data = (
            transporter_bordereaux_stats.build()
        )

        followed_with_pnttd = FollowedWithPNTTDTableProcessor(
            company_siret=self.siret,
            bs_data_dfs={
                k: v for k, v in self.bs_dfs.items() if k in [BSDD, BSDD_NON_DANGEROUS]
            },
            data_date_interval=data_date_interval,
            waste_codes_df=WASTE_CODES_DATA,
        )
        self.computed.followed_with_pnttd_data = followed_with_pnttd.build()
        gistrid_data = get_gistrid_data(self.siret)

        gistrid_stats = GistridStatsProcessor(
            company_siret=self.siret,
            gistrid_data_df=gistrid_data,
        )
        self.computed.gistrid_stats_data = gistrid_stats.build()

        self.computed.state = ComputedInspectionData.StateChoice.COMPUTED
        self.computed.save()

    def process(self):
        self._process_company_data()
        self._process_bsds()
