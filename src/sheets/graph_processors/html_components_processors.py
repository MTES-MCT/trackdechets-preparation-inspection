import json
import numbers
import re
from datetime import datetime, timedelta
from itertools import chain
from typing import Any, Dict, List

import numpy as np
import pandas as pd
from django.utils import timezone as django_timezone

from sheets.utils import format_number_str

from ..constants import BSDA, BSDASRI, BSDD, BSDD_NON_DANGEROUS, BSFF, BSVHU

# classes returning a context to be rendered in a non-plotly template


# todo: rename
class BsdStatsProcessor:
    """Component that displays aggregated data about 'bordereaux' and estimations of the onsite waste stock.

    Parameters
    ----------
    company_siret: str
        SIRET number of the establishment for which the data is displayed (used for data preprocessing).
    bs_data: DataFrame
        DataFrame containing data for a given 'bordereau' type.
    quantity_variables_names: list of str
        The names of the variables to use to compute quantity statistics.
        For example : ["quantity_received","volume"] to compute statistics for both variables.
    bs_revised_data: DataFrame
        DataFrame containing list of revised 'bordereaux' for a given 'bordereau' type.
    packagings_data:
        For BSFF data, packagings dataset to be able to compute stats at packaging level.
    """

    def __init__(
        self,
        company_siret: str,
        bs_data: pd.DataFrame,
        quantity_variables_names: list[str] = ["quantity_received"],
        bs_revised_data: pd.DataFrame = None,
        packagings_data: pd.DataFrame = None,
    ) -> None:
        self.company_siret = company_siret

        self.bs_data = bs_data
        self.quantity_variables_names = quantity_variables_names
        self.bs_revised_data = bs_revised_data
        self.packagings_data = packagings_data

        # Initialization of dicts that will hold the different computed statistics
        keys = [
            "total",
            "archived",
            "processed_in_more_than_one_month_count",
            "processed_in_more_than_one_month_avg_processing_time",
        ]
        if self.packagings_data is not None:
            keys.extend(
                [
                    "total_packagings",
                    "processed_in_more_than_one_month_packagings_count",
                    "processed_in_more_than_one_month_packagings_avg_processing_time",
                ]
            )

        self.emitted_bs_stats = {key: None for key in keys}
        self.received_bs_stats = {key: None for key in keys}

        self.revised_bs_count = 0

        # Quantities stats is two level deep as it will store the statistics for each
        # chosen quantity variables
        self.quantities_stats = {
            key: {
                "total_quantity_incoming": None,
                "total_quantity_outgoing": None,
                "bar_size_incoming": None,
                "bar_size_outgoing": None,
            }
            for key in self.quantity_variables_names
        }

        self.weight_volume_ratio = None

    def _check_data_empty(self) -> bool:
        bs_data = self.bs_data
        siret = self.company_siret

        bs_emitted_data = bs_data[bs_data["emitter_company_siret"] == siret]
        bs_received_data = bs_data[bs_data["recipient_company_siret"] == siret]

        bs_revised_data = self.bs_revised_data

        # If all raw dataframes are empty, then output data will be empty
        if (len(bs_emitted_data) == len(bs_received_data) == 0) and (
            (bs_revised_data is None) or (len(bs_revised_data) == 0)
        ):
            return True

        # If all values after preprocessing are empty, then output data will be empty
        if all(
            (e == 0) or (e is None)
            for e in chain(
                self.emitted_bs_stats.values(), self.received_bs_stats.values()
            )
        ):
            return True

        return False

    def _preprocess_data(self) -> None:
        one_year_ago = (django_timezone.now() - timedelta(days=365)).strftime(
            "%Y-%m-01"
        )
        today_date = django_timezone.now().strftime("%Y-%m-%d %H:%M:%S")

        bs_data = self.bs_data
        bs_emitted_data = bs_data[
            (bs_data["emitter_company_siret"] == self.company_siret)
            & bs_data["sent_at"].between(one_year_ago, today_date)
        ]
        bs_received_data = bs_data[
            (bs_data["recipient_company_siret"] == self.company_siret)
            & bs_data["received_at"].between(one_year_ago, today_date)
        ]

        # For incoming and outgoing data, we compute different statistics
        # about the 'bordereaux'.
        # `target` is the destination in each result dictionary
        # were to store the computed value.
        for target, to_process, to_process_packagings in [
            (self.emitted_bs_stats, bs_emitted_data, self.packagings_data),
            (self.received_bs_stats, bs_received_data, self.packagings_data),
        ]:
            # total number of 'bordereaux' emitted/received
            target["total"] = len(to_process)

            # total number of 'bordereaux' that are considered as 'archived' (end of traceability)
            target["archived"] = len(
                to_process[
                    to_process["status"].isin(
                        [
                            "PROCESSED",
                            "REFUSED",
                            "NO_TRACEABILITY",
                            "FOLLOWED_WITH_PNTTD",
                        ]
                    )
                ]
            )

            # DataFrame holding all the 'bordereaux' that have been
            # processed in more than one month.
            bs_emitted_processed_in_more_than_one_month = to_process[
                (
                    (to_process["processed_at"] - to_process["received_at"])
                    > np.timedelta64(1, "M")
                )
            ]

            # Total number of bordereaux processed in more than one month
            processed_in_more_than_one_month_count = len(
                bs_emitted_processed_in_more_than_one_month
            )

            target[
                "processed_in_more_than_one_month_count"
            ] = processed_in_more_than_one_month_count

            # If there is some 'bordereaux' processed in morte than one month,
            # we compute the average processing time.
            if processed_in_more_than_one_month_count:
                res = (
                    (
                        bs_emitted_processed_in_more_than_one_month["processed_at"]
                        - bs_emitted_processed_in_more_than_one_month["received_at"]
                    ).mean()
                ).total_seconds() / (
                    24 * 3600
                )  # Time in seconds is converted in days
                target[
                    "processed_in_more_than_one_month_avg_processing_time"
                ] = f"{res:.1f}j"

            # Handle the case of BSFF specific packagings statistics
            if to_process_packagings is not None:
                # Total number of packagings sent/received
                target["total_packagings"] = len(
                    to_process_packagings[
                        (to_process_packagings["bsff_id"].isin(to_process["id"]))
                        & (~to_process_packagings["operation_date"].isnull())
                    ]
                )

                # Merging of BSFF 'bordereaux' data with associated packagings data
                # as we will need the date of reception that is stored at the 'bordereau' level.
                bs_data_with_packagings = to_process.merge(
                    to_process_packagings,
                    left_on="id",
                    right_on="bsff_id",
                    validate="one_to_many",
                )

                # DataFrame with all BSFF along with packagings data
                # for packagings that have been processed in more than one month
                bs_data_with_packagings_processed_in_more_than_one_month = (
                    bs_data_with_packagings[
                        (
                            bs_data_with_packagings["operation_date"]
                            - bs_data_with_packagings["received_at"]
                        )
                        > np.timedelta64(1, "M")
                    ]
                )

                # Number of packagings processed in more than one month.
                target["processed_in_more_than_one_month_packagings_count"] = len(
                    bs_data_with_packagings_processed_in_more_than_one_month
                )

                # Average processing times for the packagings processed in more than one month
                res = (
                    (
                        bs_data_with_packagings_processed_in_more_than_one_month[
                            "operation_date"
                        ]
                        - bs_data_with_packagings_processed_in_more_than_one_month[
                            "received_at"
                        ]
                    ).mean()
                ).total_seconds() / (
                    24 * 3600
                )  # Conversion between number of seconds and days
                if not pd.isna(res):
                    target[
                        "processed_in_more_than_one_month_packagings_avg_processing_time"
                    ] = f"{res:.1f}j"

        # In case there is any 'bordereaux' revision data, we compute
        # the number of 'bordereaux' that have been revised.
        # NOTE: only revision asked by the current organization are computed.
        bs_revised_data = self.bs_revised_data
        if bs_revised_data is not None:
            bs_revised_data = bs_revised_data[
                bs_revised_data["bs_id"].isin(bs_data["id"])
            ]
            self.revised_bs_count = bs_revised_data["bs_id"].nunique()

        # We iterate over the different variables chosen to compute the statistics
        for key in self.quantities_stats.keys():
            # If there is a packagings_data DataFrame, then it means that we are
            # computing BSFF statistics, in this case we use the packagings data instead of
            # 'bordereaux' data as quantity information is stored at packaging level
            if self.packagings_data is not None:
                total_quantity_incoming = bs_received_data.merge(
                    self.packagings_data, left_on="id", right_on="bsff_id"
                )[key].sum()
                total_quantity_outgoing = bs_emitted_data.merge(
                    self.packagings_data, left_on="id", right_on="bsff_id"
                )[key].sum()
            else:
                total_quantity_incoming = bs_received_data[key].sum()
                total_quantity_outgoing = bs_emitted_data[key].sum()

            self.quantities_stats[key][
                "total_quantity_incoming"
            ] = total_quantity_incoming
            self.quantities_stats[key][
                "total_quantity_outgoing"
            ] = total_quantity_outgoing

            incoming_bar_size = 0
            outgoing_bar_size = 0

            if not (total_quantity_incoming == total_quantity_outgoing == 0):
                # The bar sizes are relative to the largest quantity.
                # Size is expressed as percentage of the component width.
                if total_quantity_incoming > total_quantity_outgoing:
                    incoming_bar_size = 100
                    outgoing_bar_size = int(
                        100 * (total_quantity_outgoing / total_quantity_incoming)
                    )
                else:
                    incoming_bar_size = int(
                        100 * (total_quantity_incoming / total_quantity_outgoing)
                    )
                    outgoing_bar_size = 100
            self.quantities_stats[key]["bar_size_incoming"] = incoming_bar_size
            self.quantities_stats[key]["bar_size_outgoing"] = outgoing_bar_size

        # If both "quantity_received" and "volume" variables have been chosen,
        # then it means that we are computing BSDASRI statistics.
        # In this case we compute the ratio between volume and weight.
        if all(
            key in self.quantity_variables_names
            for key in ["quantity_received", "volume"]
        ):
            if (self.quantities_stats["volume"]["total_quantity_incoming"]) > 0:
                self.weight_volume_ratio = (
                    self.quantities_stats["quantity_received"][
                        "total_quantity_incoming"
                    ]
                    / self.quantities_stats["volume"]["total_quantity_incoming"]
                )

    def build_context(self):
        # We use the format_number_str only on variables that holds
        # quantity values.
        ctx = {
            "emitted_bs_stats": {
                k: (format_number_str(v, 0) if isinstance(v, numbers.Number) else v)
                for k, v in self.emitted_bs_stats.items()
            },
            "received_bs_stats": {
                k: (format_number_str(v, 0) if isinstance(v, numbers.Number) else v)
                for k, v in self.received_bs_stats.items()
            },
            "revised_bs_count": format_number_str(self.revised_bs_count, precision=0),
            # quantities_stats is two level deep so we need to use a nested
            # dict comprehension loop.
            "quantities_stats": {
                ok: {
                    k: (
                        format_number_str(v, 2)
                        if k in ["total_quantity_incoming", "total_quantity_outgoing"]
                        else v
                    )
                    for k, v in ov.items()
                }
                for ok, ov in self.quantities_stats.items()
            },
            # We multiply the weight to get kilograms instead of tons for the weight_volume_ratio
            "weight_volume_ratio": format_number_str(self.weight_volume_ratio * 1000, 2)
            if self.weight_volume_ratio is not None
            else None,
        }

        return ctx

    def build(self):
        self._preprocess_data()

        data = {}
        if not self._check_data_empty():
            data = self.build_context()
        return data


class InputOutputWasteTableProcessor:
    """Component that displays an exhaustive tables with input and output wastes classified by waste codes.

    Parameters
    ----------
    company_siret: str
        SIRET number of the establishment for which the data is displayed (used for data preprocessing).
    bs_data_dfs: dict
        Dict with key being the 'bordereau' type and values the DataFrame containing the bordereau data.
    waste_codes_df: DataFrame
        DataFrame containing list of waste codes with their descriptions. It is the waste nomenclature.
    """

    def __init__(
        self,
        company_siret: str,
        bs_data_dfs: Dict[str, pd.DataFrame],
        waste_codes_df: pd.DataFrame,
    ) -> None:
        self.bs_data_dfs = bs_data_dfs
        self.waste_codes_df = waste_codes_df
        self.company_siret = company_siret
        self.preprocessed_df = None

    def _preprocess_data(self) -> None:
        siret = self.company_siret
        one_year_ago = (django_timezone.now() - timedelta(days=365)).strftime(
            "%Y-%m-01"
        )
        today_date = django_timezone.now().strftime("%Y-%m-%d %H:%M:%S")

        dfs_to_concat = [df for df in self.bs_data_dfs.values()]

        if len(dfs_to_concat) == 0:
            self.preprocessed_df = pd.DataFrame()
            return

        df = pd.concat(dfs_to_concat)

        df = df[
            (df.emitter_company_siret == siret) | (df.recipient_company_siret == siret)
        ]

        # We create a column to differentiate incoming waste from
        # outgoing waste.
        df["incoming_or_outgoing"] = pd.NA
        df.loc[
            (df.emitter_company_siret == siret)
            & df.sent_at.between(one_year_ago, today_date),
            "incoming_or_outgoing",
        ] = "outgoing"
        df.loc[
            (df.recipient_company_siret == siret)
            & df.received_at.between(one_year_ago, today_date),
            "incoming_or_outgoing",
        ] = "incoming"
        df = df.dropna(subset="incoming_or_outgoing")

        if len(df) > 0:
            # We compute the quantity by waste codes and incoming/outgoing categories
            df_grouped = df.groupby(
                ["waste_code", "incoming_or_outgoing"], as_index=False
            )["quantity_received"].sum()

            # We add the waste code description from the waste nomenclature
            final_df = pd.merge(
                df_grouped,
                self.waste_codes_df,
                left_on="waste_code",
                right_index=True,
                how="left",
                validate="many_to_one",
            )

            final_df = final_df[final_df["quantity_received"] > 0]
            final_df["quantity_received"] = final_df["quantity_received"].apply(
                lambda x: format_number_str(x, 2)
            )
            self.preprocessed_df = final_df[
                [
                    "waste_code",
                    "description",
                    "incoming_or_outgoing",
                    "quantity_received",
                ]
            ].sort_values(by=["waste_code", "incoming_or_outgoing"])

    def _check_empty_data(self) -> bool:
        if self.preprocessed_df is None:
            return True

        return False

    def build_context(self):
        return self.preprocessed_df.to_dict("records")

    def build(self):
        self._preprocess_data()

        res = {}

        if not self._check_empty_data():
            res = self.build_context()
        return res


class BsdCanceledTableProcessor:
    """Component that displays an exhaustive tables with the list of 'bordereaux' that have been canceled.

    Parameters
    ----------
    company_siret: str
        SIRET number of the establishment for which the data is displayed (used for data preprocessing).
    bs_data_dfs: dict
        Dict with key being the 'bordereau' type and values the DataFrame containing the bordereau data.
    bs_revised_data: DataFrame
        Dict with key being the 'bordereau' type and values the DataFrame containing the associated revision data.
    """

    def __init__(
        self,
        company_siret: str,
        bs_data_dfs: Dict[str, pd.DataFrame],
        bs_revised_data: Dict[str, pd.DataFrame],
    ) -> None:
        self.bs_data_dfs = bs_data_dfs
        self.bs_revised_data = bs_revised_data
        self.company_siret = company_siret

        self.preprocessed_df = pd.DataFrame()

    def _preprocess_data(self) -> None:
        if not self.bs_revised_data:
            return

        one_year_ago = (django_timezone.now() - timedelta(days=365)).strftime(
            "%Y-%m-01"
        )
        today_date = django_timezone.now().strftime("%Y-%m-%d %H:%M:%S")

        dfs = []
        for bs_type, revised_data_df in self.bs_revised_data.items():
            # Cancellation events are stored in revisions
            cancellations = revised_data_df[
                revised_data_df.is_canceled
                & revised_data_df.updated_at.between(one_year_ago, today_date)
            ]
            if len(cancellations):
                bs_data = self.bs_data_dfs[bs_type]

                # Columns that will be displayed in the output table
                columns_to_take = [
                    "id_y",  # Will correspond to the 'bordereau' id after merge
                    "quantity_received",
                    "emitter_company_siret",
                    "recipient_company_siret",
                    "waste_code",
                    "waste_name",
                    "updated_at",
                    "comment",
                ]

                # Human-friendly id is stored in the readable_id column in the case of BSDDs
                if "readable_id" in bs_data.columns:
                    columns_to_take.append("readable_id")

                temp_df = pd.merge(
                    cancellations,
                    bs_data,
                    left_on="bs_id",
                    right_on="id",
                ).sort_values("updated_at")

                temp_df = temp_df[columns_to_take]
                temp_df.rename(columns={"id_y": "id"})

                dfs.append(temp_df)

        if dfs:
            self.preprocessed_df = pd.concat(dfs)

    def _check_empty_data(self) -> bool:
        if len(self.preprocessed_df) == 0:
            return True

        return False

    def build_context(self):
        data = self.preprocessed_df
        data["updated_at"] = data["updated_at"].dt.strftime("%d/%m/%Y %H:%M")
        return json.loads(data.to_json(orient="records"))

    def build(self):
        self._preprocess_data()

        data = {}
        if not self._check_empty_data():
            data = self.build_context()

        return data


class SameEmitterRecipientTableProcessor:
    """Component that displays an exhaustive tables with the
    list of 'bordereaux' that have the same company
    as emitter and recipient along with a worksite address.

    Parameters
    ----------
    bs_data_dfs: dict
        Dict with key being the 'bordereau' type and values the DataFrame containing the bordereau data.
    """

    def __init__(
        self,
        bs_data_dfs: Dict[str, pd.DataFrame],
    ) -> None:
        self.bs_data_dfs = bs_data_dfs
        self.preprocessed_df = pd.DataFrame()

    def _preprocess_data(self) -> None:
        one_year_ago = (django_timezone.now() - timedelta(days=365)).strftime(
            "%Y-%m-01"
        )
        today_date = django_timezone.now().strftime("%Y-%m-%d %H:%M:%S")

        dfs_to_process = [
            df
            for bs_type, df in self.bs_data_dfs.items()
            if bs_type in ["bsdd", "bsda"]
        ]

        columns_to_take = [
            "id",
            "readable_id",
            "sent_at",
            "received_at",
            "quantity_received",
            "waste_code",
            "waste_name",
            "worksite_name",
            "worksite_address",
        ]
        dfs_processed = []
        for df in dfs_to_process:
            same_emitter_recipient_df = df[
                (df["emitter_company_siret"] == df["recipient_company_siret"])
                & df["worksite_address"].notna()
                & df["sent_at"].between(one_year_ago, today_date)
            ].reindex(columns_to_take, axis=1)
            if len(same_emitter_recipient_df):
                dfs_processed.append(same_emitter_recipient_df)

        if dfs_processed:
            self.preprocessed_df = pd.concat(dfs_processed)

    def _check_empty_data(self) -> bool:
        if len(self.preprocessed_df) == 0:
            return True

        return False

    def build_context(self):
        data = self.preprocessed_df
        data["sent_at"] = pd.to_datetime(data["sent_at"]).dt.strftime("%d/%m/%Y %H:%M")
        data["received_at"] = pd.to_datetime(data["received_at"]).dt.strftime(
            "%d/%m/%Y %H:%M"
        )

        return json.loads(data.to_json(orient="records"))

    def build(self):
        self._preprocess_data()

        data = {}
        if not self._check_empty_data():
            data = self.build_context()

        return data


class StorageStatsProcessor:
    """Component that displays waste stock on site by waste codes (TOP 4) and total stock in tons.

    Parameters
    ----------
    company_siret: str
        SIRET number of the establishment for which the data is displayed (used for data preprocessing).
    bs_data_dfs: dict
        Dict with key being the 'bordereau' type and values the DataFrame containing the bordereau data.
    waste_codes_df: DataFrame
        DataFrame containing list of waste codes with their descriptions.
    """

    def __init__(
        self,
        company_siret: str,
        bs_data_dfs: Dict[str, pd.DataFrame],
        waste_codes_df: pd.DataFrame,
    ) -> None:
        self.company_siret = company_siret

        self.bs_data_dfs = bs_data_dfs
        self.waste_codes_df = waste_codes_df

        self.stock_by_waste_code = None
        self.total_stock = None

    def _preprocess_data(self) -> pd.Series:
        siret = self.company_siret

        one_year_ago = (django_timezone.now() - timedelta(days=365)).strftime(
            "%Y-%m-01"
        )
        today_date = django_timezone.now().strftime("%Y-%m-%d %H:%M:%S")

        dfs_to_concat = [df for df in self.bs_data_dfs.values()]

        if len(dfs_to_concat) == 0:
            self.stock_by_waste_code = pd.Series()
            return

        df = pd.concat(dfs_to_concat)

        emitted_mask = (df.emitter_company_siret == siret) & df.sent_at.between(
            one_year_ago, today_date
        )
        received_mask = (df.recipient_company_siret == siret) & df.received_at.between(
            one_year_ago, today_date
        )

        emitted = df[emitted_mask].groupby("waste_code")["quantity_received"].sum()
        received = df[received_mask].groupby("waste_code")["quantity_received"].sum()

        # Index wise sum (index being the waste codes)
        # to compute the theoretical stock of waste
        # (difference between incoming and outgoing quantities)
        stock_by_waste_code: pd.Series = (
            (-emitted + received).fillna(-emitted).fillna(received)
        )
        stock_by_waste_code.sort_values(ascending=False, inplace=True)

        # Only positive differences are kept
        stock_by_waste_code = stock_by_waste_code[stock_by_waste_code > 0]
        total_stock = format_number_str(stock_by_waste_code.sum(), precision=1)
        stock_by_waste_code = stock_by_waste_code.apply(format_number_str, precision=1)

        # Data is enriched with waste description from the waste nomenclature
        stock_by_waste_code = pd.merge(
            stock_by_waste_code,
            self.waste_codes_df,
            left_index=True,
            right_index=True,
            how="left",
            validate="one_to_one",
        )

        self.stock_by_waste_code = stock_by_waste_code
        self.total_stock = total_stock

    def _check_data_empty(self) -> bool:
        if (len(self.stock_by_waste_code) == 0) or self.stock_by_waste_code[
            "quantity_received"
        ].isna().all():
            return True

        return False

    def _add_stats(self):
        stored_waste = []

        for row in self.stock_by_waste_code.head(4).itertuples():
            stored_waste.append(
                {
                    "quantity_received": row.quantity_received,
                    "code": str(row.Index),
                    "description": row.description,
                }
            )
        return {"stored_waste": stored_waste, "total_stock": self.total_stock}

    def build(self):
        self._preprocess_data()

        data = {}
        if not self._check_data_empty():
            data = self._add_stats()
        return data


class AdditionalInfoProcessor:
    """Component that displays additional informations like outliers quantities or inconsistent dates.

    Parameters
    ----------
    company_siret: str
        SIRET number of the establishment for which the data is displayed (used for data preprocessing).
    additional_data: dict
        dict with additional data. The schema of the dict is like:
        {'date_outliers': {'BSDD': {'processed_at':some_DataFrame, 'sentAt': some_DataFrame}}, 'quantity_outliers': {'BSDD': some_DataFrame, 'BSDA': some_DataFrame, 'BSDASRI': some_DataFrame}}
    """

    def __init__(
        self,
        company_siret: str,
        additional_data: Dict[str, Dict[str, pd.DataFrame]],
    ) -> None:
        self.company_siret = company_siret

        self.additional_data = additional_data

        self.date_outliers_data = None
        self.quantity_outliers_data = None

    def _check_data_empty(self) -> bool:
        if (
            len(self.additional_data["date_outliers"])
            == len(self.additional_data["quantity_outliers"])
            == 0
        ):
            self.is_component_empty = True
            return self.is_component_empty

        self.is_component_empty = False
        return False

    def _preprocess_data(self) -> None:
        date_outliers_data = {}
        for key, value in self.additional_data["date_outliers"].items():
            date_outliers_data[key] = {
                k: v[k] for k, v in value.items() if v is not None
            }

        self.date_outliers_data = date_outliers_data
        self.quantity_outliers_data = self.additional_data["quantity_outliers"]

    def _add_date_outliers_layout(self):
        """Create and add the layout for date outliers."""
        res = []
        for bs_type, outlier_data in self.date_outliers_data.items():
            bs_col_example_li = []
            for col, serie in outlier_data.items():
                bs_col_example_li.append(
                    {
                        "bs_type": bs_type,
                        "col": col,
                        "outliers_count": len(serie),
                        "sample": "serie.sample(1).item()",
                    }
                )
            res.append(bs_col_example_li)
        return res

    def _add_quantity_outliers_layout(self):
        """Create and add the layout for quantity outliers."""

        quantity_outliers_bs_list_layout = []
        for bs_type, outlier_data in self.quantity_outliers_data.items():
            quantity_outliers_bs_list_layout.append(
                {
                    "outliers_count": len(outlier_data),
                    "sample": format_number_str(
                        outlier_data.quantity_received.sort_values(ascending=False)
                        .head(1)
                        .item(),
                        precision=0,
                    ),
                }
            )
        return quantity_outliers_bs_list_layout

    def build(self) -> list:
        self._preprocess_data()
        res = {}
        if not self._check_data_empty():
            if len(self.date_outliers_data):
                res["dates_outliers"] = self._add_date_outliers_layout()
            if len(self.quantity_outliers_data):
                res["quantity_outliers"] = self._add_quantity_outliers_layout()

        return res


class ICPEItemsProcessor:
    """Component that displays list of ICPE authorized items.

    Parameters
    ----------
    company_siret: str
        SIRET number of the establishment for which the data is displayed (used for data preprocessing).
    icpe_data: DataFrame
        DataFrame containing list of ICPE authorized items
    bs_data_dfs: dict
        Dict with key being the 'bordereau' type and values the DataFrame containing the bordereau data.
    mapping_processing_operation_code_rubrique: DataFrame
        Mapping between operation codes and rubriques.

    """

    def __init__(
        self,
        company_siret: str,
        icpe_data: pd.DataFrame,
        bs_data_dfs: Dict[str, pd.DataFrame],
        mapping_processing_operation_code_rubrique: pd.DataFrame,
    ) -> None:
        self.company_siret = company_siret
        self.icpe_data = icpe_data
        self.bs_data_dfs = bs_data_dfs

        self.unit_pattern = re.compile(
            r"""^t$
                |^t\/.*$
                |citerne
                |bouteille
                |cabine
                |tonne
                |aire
                |cartouche
            """,
            re.X,
        )
        self.mapping_processing_operation_code_rubrique = (
            mapping_processing_operation_code_rubrique
        )

        self.on_site_2718_quantity = 0
        self.max_2718_quantity = (0, None)

        self.on_site_2760_quantity = 0

        self.avg_daily_2770_quantity = 0
        self.max_2770_quantity = (0, None)

    def _preprocess_data(self) -> List[Dict[str, Any]]:
        preprocessed_inputs_dfs = []
        preprocessed_output_dfs = []
        actual_year = datetime.now().year
        for df in self.bs_data_dfs.values():
            df = df.dropna(subset=["processing_operation_code"])

            if len(df) == 0:
                continue

            df["processing_operation_code"] = df[
                "processing_operation_code"
            ].str.replace(" ", "", regex=False)

            df = pd.merge(
                df,
                self.mapping_processing_operation_code_rubrique,
                left_on="processing_operation_code",
                right_on="code_operation",
                validate="many_to_many",
                how="left",
            )

            preprocessed_inputs_dfs.append(
                df[(df["recipient_company_siret"] == self.company_siret)]
            )
            preprocessed_output_dfs.append(
                df[(df["emitter_company_siret"] == self.company_siret)]
            )

        if len(preprocessed_inputs_dfs) == 0:
            return

        if all(len(df) == 0 for df in preprocessed_inputs_dfs):
            return

        # 2718 preprocessing
        preprocessed_inputs = pd.concat(preprocessed_inputs_dfs)
        preprocessed_outputs = pd.concat(preprocessed_output_dfs)

        preprocessed_inputs_filtered = preprocessed_inputs[
            (preprocessed_inputs["rubrique"] == "2718")
        ].set_index("received_at")

        preprocessed_outputs_filtered = preprocessed_outputs[
            (preprocessed_outputs["rubrique"] == "2718")
        ].set_index("sent_at")
        preprocessed_outputs_filtered["quantity_received"] *= -1

        preprocessed_inputs_outputs = pd.concat(
            (
                preprocessed_inputs_filtered,
                preprocessed_outputs_filtered,
            ),
        ).sort_index()
        if len(preprocessed_inputs_outputs) > 0:
            preprocessed_inputs_outputs["stock"] = (
                preprocessed_inputs_outputs["quantity_received"].cumsum().sort_index()
            )
            max_stock = preprocessed_inputs_outputs.sort_values(
                "stock", ascending=False
            ).iloc[0]
            actual_quantity = preprocessed_inputs_outputs.iloc[-1]
            if actual_quantity["stock"] > 0:
                self.on_site_2718_quantity = actual_quantity["stock"]

            if max_stock["stock"] > 0:
                self.max_2718_quantity = (
                    max_stock["stock"],
                    max_stock.name.date().strftime("%d-%m-%Y"),
                )

        # 2760 preprocessing
        quantity = preprocessed_inputs.loc[
            (preprocessed_inputs["rubrique"] == "2760-1")
            & (preprocessed_inputs["processed_at"].dt.year == actual_year),
            "quantity_received",
        ].sum()
        if quantity > 0:
            self.on_site_2760_quantity = quantity

        # 2770 preprocessing
        quantity = (
            preprocessed_inputs.loc[preprocessed_inputs["rubrique"] == "2770"]
            .groupby(pd.Grouper(key="processed_at", freq="1D"))["quantity_received"]
            .sum()
        )
        if len(quantity) > 0:
            self.avg_daily_2770_quantity = quantity.mean()
            max_quantity = quantity.sort_values(ascending=False)

            self.max_2770_quantity = (
                max_quantity[0],
                max_quantity.index[0].date().strftime("%d-%m-%Y"),
            )

    def _add_items_list(self) -> List[Dict[str, Any]]:
        icpe_data = pd.concat(
            [
                self.icpe_data.loc[
                    self.icpe_data["rubrique"].isin(["2718", "2760", "2790", "2770"])
                ],
                self.icpe_data.loc[
                    ~self.icpe_data["rubrique"].isin(["2718", "2760", "2790", "2770"])
                ].sort_values("rubrique"),
            ]
        )

        icpe_items = [
            {
                "rubrique": item.rubrique,
                "alinea": item.alinea,
                "libelle": item.libelle_court_activite,
                "date_debut": f"{item.date_debut_exploitation:%d-%m-%Y}"
                if not pd.isnull(item.date_debut_exploitation)
                else None,
            }
            for item in icpe_data.itertuples()
        ]
        return icpe_items

    def _check_data_empty(self) -> bool:
        if self.icpe_data is None or len(self.icpe_data) == 0:
            self.is_component_empty = True
            return self.is_component_empty

        self.is_component_empty = False
        return False

    def build(self) -> list:
        if not self._check_data_empty():
            self._preprocess_data()
            icpe_items = self._add_items_list()
            if icpe_items:
                return icpe_items
            return []

        return []


class TraceabilityInterruptionsProcessor:
    """Component that displays list of declared traceability interruptions.

    Parameters
    ----------
    company_siret: str
        SIRET number of the establishment for which the data is displayed (used for data preprocessing).
    bsdd_data: DataFrame
        DataFrame containing BSDD data.
    """

    def __init__(
        self,
        company_siret: str,
        bsdd_data: pd.DataFrame,
        waste_codes_df: pd.DataFrame,
    ) -> None:
        self.company_siret = company_siret

        self.preprocessed_data = None

        self.bsdd_data = bsdd_data
        self.waste_codes_df = waste_codes_df

    def _preprocess_data(self) -> None:
        if self.bsdd_data is None:
            return

        df_filtered = self.bsdd_data[
            self.bsdd_data["no_traceability"]
            & (self.bsdd_data["recipient_company_siret"] == self.company_siret)
        ]

        if len(df_filtered) == 0:
            return

        # Quantity and count are computed by waste code
        df_grouped = df_filtered.groupby("waste_code", as_index=False).agg(
            quantity=pd.NamedAgg(column="quantity_received", aggfunc="sum"),
            count=pd.NamedAgg(column="id", aggfunc="count"),
        )

        # Data is enriched with waste description from the waste nomenclature
        final_df = pd.merge(
            df_grouped,
            self.waste_codes_df,
            left_on="waste_code",
            right_index=True,
            how="left",
            validate="one_to_one",
        )

        final_df["quantity"] = final_df["quantity"].apply(
            format_number_str, precision=2
        )

        self.preprocessed_data = final_df

    def _check_data_empty(self) -> bool:
        if (self.preprocessed_data is None) or (len(self.preprocessed_data) == 0):
            self.is_component_empty = True
            return True

        return False

    def _add_stats(self) -> list:
        stats = []

        for e in self.preprocessed_data.sort_values(
            "quantity", ascending=False
        ).itertuples():
            row = {
                "waste_code": e.waste_code,
                "count": e.count,
                "quantity": e.quantity,
                "description": e.description,
            }
            stats.append(row)
        return stats

    def build(self) -> list:
        self._preprocess_data()

        if not self._check_data_empty():
            return self._add_stats()
        return []


class WasteIsDangerousStatementsProcessor:
    """Component that displays list of wastes tracked
    without dangerous waste code but with the "waste_is_dangerous" option enabled.

    Parameters
    ----------
    company_siret: str
        SIRET number of the establishment for which the data is displayed (used for data preprocessing).
    bsdd_data: DataFrame
        DataFrame containing bsdd data.
    """

    def __init__(
        self,
        company_siret: str,
        bsdd_data: pd.DataFrame,
        waste_codes_df: pd.DataFrame,
    ) -> None:
        self.company_siret = company_siret

        self.preprocessed_data = None

        self.bsdd_data = bsdd_data
        self.waste_codes_df = waste_codes_df

    def _preprocess_data(self) -> None:
        if self.bsdd_data is None:
            return

        one_year_ago = (django_timezone.now() - timedelta(days=365)).strftime(
            "%Y-%m-01"
        )
        today_date = django_timezone.now().strftime("%Y-%m-%d %H:%M:%S")

        df_filtered = self.bsdd_data[
            self.bsdd_data["is_dangerous"]
            & (self.bsdd_data["emitter_company_siret"] == self.company_siret)
            & (~self.bsdd_data["waste_code"].str.contains(pat=r".*\*$"))
            & (self.bsdd_data["sent_at"].between(one_year_ago, today_date))
        ]

        if len(df_filtered) == 0:
            return

        df_grouped = df_filtered.groupby("waste_code", as_index=False).agg(
            quantity=pd.NamedAgg(column="quantity_received", aggfunc="sum"),
            count=pd.NamedAgg(column="id", aggfunc="count"),
        )

        final_df = pd.merge(
            df_grouped,
            self.waste_codes_df,
            left_on="waste_code",
            right_index=True,
            how="left",
            validate="one_to_one",
        )

        final_df["quantity"] = final_df["quantity"].apply(
            format_number_str, precision=2
        )

        self.preprocessed_data = final_df

    def _check_data_empty(self) -> bool:
        if (self.preprocessed_data is None) or (len(self.preprocessed_data) == 0):
            self.is_component_empty = True
            return True

        return False

    def _add_stats(self) -> list:
        stats = []

        for e in self.preprocessed_data.sort_values(
            "quantity", ascending=False
        ).itertuples():
            row = {
                "waste_code": e.waste_code,
                "count": e.count,
                "quantity": e.quantity,
                "description": e.description,
            }
            stats.append(row)
        return stats

    def build(self) -> list:
        self._preprocess_data()

        if not self._check_data_empty():
            return self._add_stats()
        return []


class ReceiptAgrementsProcessor:
    """Component that displays informations about the company receipts and agreements.

    Parameters
    ----------
    receipts_agreements_data : dict
        Dict with keys being the name of the receipt/agreement and values being DataFrames
        with one line per receipt/agreement (usually there is only one receipt for a receipt type for an establishment but
        there might be more).
    """

    def __init__(self, receipts_agreements_data: Dict[str, str]) -> None:
        self.receipts_agreements_data = receipts_agreements_data

    def _check_data_empty(self) -> bool:
        if len(self.receipts_agreements_data) == 0:
            return True

        return False

    def build(self):
        res = []
        for name, data in self.receipts_agreements_data.items():
            for line in data.itertuples():
                validity_str = ""
                if "validity_limit" in line._fields:
                    # todo: utcnow
                    if line.validity_limit < datetime.now():
                        validity_str = (
                            f"expiré depuis le {line.validity_limit:%d/%m/%Y}"
                        )
                    else:
                        validity_str = f"valide jusqu'au {line.validity_limit:%d/%m/%Y}"
                res.append(
                    {
                        "name": name,
                        "number": line.receipt_number,
                        "validity_str": validity_str,
                    }
                )

        return res


class PrivateIndividualsCollectionsTableProcessor:
    """Component that displays a list of private individuals where waste have been picked up.
    Only for BSDA data.

    Parameters
    ----------
    company_siret: str
        SIRET number of the establishment for which the data is displayed (used for data preprocessing).
    bsda_data_df: DataFrame
        Dict with key being the 'bordereau' type and values the DataFrame containing the bordereau data.


    """

    def __init__(
        self,
        company_siret: str,
        bsda_data_df: pd.DataFrame,
    ) -> None:
        self.company_siret = company_siret

        self.bsda_data_df = bsda_data_df

        self.preprocessed_data = None

    def _preprocess_data(self) -> None:
        if self.bsda_data_df is None:
            return

        filtered_df = self.bsda_data_df[
            (
                (self.bsda_data_df["recipient_company_siret"] == self.company_siret)
                | (self.bsda_data_df["worker_company_siret"] == self.company_siret)
            )
            & self.bsda_data_df["emitter_is_private_individual"]
        ]

        if len(filtered_df) > 0:
            self.preprocessed_data = filtered_df

    def _check_data_empty(self) -> bool:
        if self.preprocessed_data is None:
            return True

        return False

    def _add_stats(self) -> list:
        stats = []

        for e in self.preprocessed_data.sort_values("sent_at").itertuples():
            row = {
                "id": e.id,
                "recipient_company_siret": e.recipient_company_siret,
                "worker_company_siret": e.worker_company_siret,
                "emitter_company_name": e.emitter_company_name,
                "emitter_company_address": e.emitter_company_address,
                "worksite_name": e.worksite_name,
                "worksite_address": e.worksite_address,
                "waste_code": e.waste_code,
                "waste_name": e.waste_name,
                "quantity": e.quantity_received
                if not pd.isna(e.quantity_received)
                else None,
                "sent_at": e.sent_at.strftime("%d/%m/%Y %H:%M")
                if not pd.isna(e.sent_at)
                else None,
                "received_at  ": e.received_at.strftime("%d/%m/%Y %H:%M")
                if not pd.isna(e.received_at)
                else None,
            }
            stats.append(row)
        return stats

    def build(self) -> list:
        self._preprocess_data()

        if not self._check_data_empty():
            return self._add_stats()
        return []


class QuantityOutliersTableProcessor:
    """Component that displays a list of bordereaux with outliers values on quantity.

    Parameters
    ----------
    bs_data_dfs: dict
        Dict with key being the 'bordereau' type and values the DataFrame containing the bordereau data.


    """

    def __init__(
        self,
        bs_data_dfs: Dict[str, pd.DataFrame],
    ) -> None:
        self.bs_data_dfs = bs_data_dfs

        self.preprocessed_data = None

    @staticmethod
    def get_quantity_outliers(df: pd.DataFrame, bs_type: str) -> pd.DataFrame:
        """Get lines from 'bordereau' DataFrame with inconsistent received quantity.
        The rules to identify outliers in received quantity are business rules and may be tweaked in the future.

        Parameters
        ----------
        df : DataFrame
            DataFrame with 'bordereau' data.
        bs_type : str
            Name of the 'bordereau' (BSDD, BSDD_NON_DANGEROUS, BSDA, BSFF, BSVHU or BSDASRI).

        Returns
        -------
        DataFrame
            DataFrame with lines with received quantity outliers removed.
        """

        if bs_type in [BSDD, BSDD_NON_DANGEROUS, BSDA]:
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

        df_quantity_outliers["bs_type"] = (
            bs_type if bs_type != BSDD_NON_DANGEROUS else "bsdd"
        )
        return df_quantity_outliers

    def _preprocess_data(self) -> None:
        outliers_dfs = []
        for bs_type, df in self.bs_data_dfs.items():
            df_outliers = self.get_quantity_outliers(df, bs_type)

            if len(df_outliers) != 0:
                if bs_type in [BSDD, BSDD_NON_DANGEROUS]:
                    df_outliers["id"] = df_outliers["readable_id"]

                outliers_dfs.append(df_outliers)

        if outliers_dfs:
            self.preprocessed_data = pd.concat(outliers_dfs)

    def _check_data_empty(self) -> bool:
        if self.preprocessed_data is None:
            return True

        return False

    def _add_stats(self) -> list:
        stats = []

        for e in self.preprocessed_data.sort_values("sent_at").itertuples():
            row = {
                "id": e.id,
                "bs_type": e.bs_type,
                "emitter_company_siret": e.emitter_company_siret,
                "recipient_company_siret": e.recipient_company_siret,
                "waste_code": e.waste_code,
                "waste_name": e.waste_name,
                "quantity": format_number_str(e.quantity_received, 1)
                if not pd.isna(e.quantity_received)
                else None,
                "sent_at": e.sent_at.strftime("%d/%m/%Y %H:%M")
                if not pd.isna(e.sent_at)
                else None,
                "received_at  ": e.received_at.strftime("%d/%m/%Y %H:%M")
                if not pd.isna(e.received_at)
                else None,
            }
            stats.append(row)
        return stats

    def build(self) -> list:
        self._preprocess_data()

        if not self._check_data_empty():
            return self._add_stats()
        return []
