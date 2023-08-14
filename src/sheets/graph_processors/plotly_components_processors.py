import json
import locale
from datetime import datetime, timedelta
from typing import Dict

import geopandas as gpd
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from sheets.utils import format_number_str, get_code_departement

# classes returning a serialized (json) plotly visualization to be consumed by a plotly script
locale.setlocale(locale.LC_ALL, "fr_FR")


class BsdQuantitiesGraph:
    """Component with a Line Figure showing incoming and outgoing quantities of waste..

    Parameters
    ----------
    company_siret: str
        SIRET number of the establishment for which the data is displayed (used for data preprocessing).
    bs_data: DataFrame
        DataFrame containing data for a given 'bordereau' type.
    quantity_variables_names: list of str
        The names of the variables to use to compute quantity statistics. Several variables can be used.
    packagings_data : DataFrame
        For BSFF data, packagings dataset to be able to compute the quantities.
    """

    def __init__(
        self,
        company_siret: str,
        bs_data: pd.DataFrame,
        data_date_interval: tuple[datetime, datetime],
        quantity_variables_names: list[str] = ["quantity_received"],
        packagings_data: pd.DataFrame = None,
    ):
        self.bs_data = bs_data
        self.packagings_data = packagings_data
        self.company_siret = company_siret
        self.data_date_interval = data_date_interval
        self.quantity_variables_names = quantity_variables_names

        self.incoming_data_by_month_series = []
        self.outgoing_data_by_month_series = []

        self.figure = None

        self.figure = None

    def _preprocess_data(self) -> None:
        bs_data = self.bs_data

        incoming_data = bs_data[
            (bs_data["recipient_company_siret"] == self.company_siret)
            & bs_data["received_at"].between(*self.data_date_interval)
        ]
        outgoing_data = bs_data[
            (bs_data["emitter_company_siret"] == self.company_siret)
            & bs_data["sent_at"].between(*self.data_date_interval)
        ]

        # We iterate over the different variables chosen to compute the statistics
        for variable_name in self.quantity_variables_names:
            # If there is a packagings_data DataFrame, then it means that we are
            # computing BSFF statistics, in this case we use the packagings data instead of
            # 'bordereaux' data as quantity information is stored at packaging level
            if self.packagings_data is not None:
                incoming_data_by_month = (
                    incoming_data.merge(
                        self.packagings_data, left_on="id", right_on="bsff_id"
                    )
                    .groupby(pd.Grouper(key="acceptation_date", freq="1M"))[
                        variable_name
                    ]
                    .sum()
                    .replace(0, np.nan)
                )
                outgoing_data_by_month = (
                    outgoing_data.merge(
                        self.packagings_data, left_on="id", right_on="bsff_id"
                    )
                    .groupby(pd.Grouper(key="sent_at", freq="1M"))[variable_name]
                    .sum()
                    .replace(0, np.nan)
                )
            else:
                incoming_data_by_month = (
                    incoming_data.groupby(pd.Grouper(key="received_at", freq="1M"))[
                        variable_name
                    ]
                    .sum()
                    .replace(0, np.nan)
                )

                outgoing_data_by_month = (
                    outgoing_data.groupby(pd.Grouper(key="sent_at", freq="1M"))[
                        variable_name
                    ]
                    .sum()
                    .replace(0, np.nan)
                )

            self.incoming_data_by_month_series.append(incoming_data_by_month)
            self.outgoing_data_by_month_series.append(outgoing_data_by_month)

    def _check_data_empty(self) -> bool:
        incoming_data_by_month_series = self.incoming_data_by_month_series
        outgoing_data_by_month_series = self.outgoing_data_by_month_series

        # If DataFrames are empty then output is empty
        if all(
            len(s) == len(z) == 0
            for s, z in zip(
                incoming_data_by_month_series, outgoing_data_by_month_series
            )
        ):
            return True

        # If preprocessed series are full of NA then output is empty
        if all(
            s.isna().all() and z.isna().all()
            for s, z in zip(
                incoming_data_by_month_series, outgoing_data_by_month_series
            )
        ):
            return True

        # If preprocessed series are full of 0's then output is empty
        if all(
            (s == 0).all() and (z == 0).all()
            for s, z in zip(
                incoming_data_by_month_series, outgoing_data_by_month_series
            )
        ):
            return True

        return False

    def _create_figure(self) -> None:
        fig = go.Figure()

        lines = []  # Will store the lines graph objects

        # We store the minimum date of each series to be able to configure
        # the tick 0 of the figure
        mins_x = []

        # This is used to configure the dticks in case of low number of data points.
        numbers_of_data_points = []

        # We create two lines (for incoming and outgoing) for each quantity variable chosen
        for variable_name, incoming_data_by_month, outgoing_data_by_month in zip(
            self.quantity_variables_names,
            self.incoming_data_by_month_series,
            self.outgoing_data_by_month_series,
        ):
            incoming_line_name = "Quantité entrante"
            incoming_hover_text = "{} - <b>{}</b> tonnes entrantes"
            outgoing_line_name = "Quantité sortante"
            outgoing_hover_text = "{} - <b>{}</b> tonnes sortantes"
            marker_line_style = "solid"
            marker_symbol = "circle"
            marker_size = 6

            # To handle the case of volume
            if variable_name == "volume":
                incoming_line_name = "Volume entrant"
                incoming_hover_text = "{} - <b>{}</b> m³ entrants"
                outgoing_line_name = "Volume sortant"
                outgoing_hover_text = "{} - <b>{}</b> m³ sortants"
                marker_line_style = "dash"
                marker_symbol = "triangle-up"
                marker_size = 10

            if len(incoming_data_by_month) > 0:
                incoming_line = go.Scatter(
                    x=incoming_data_by_month.index,
                    y=incoming_data_by_month,
                    name=incoming_line_name,
                    mode="lines+markers",
                    hovertext=[
                        incoming_hover_text.format(
                            index.strftime("%B %y").capitalize(), format_number_str(e)
                        )
                        for index, e in incoming_data_by_month.items()
                    ],
                    hoverinfo="text",
                    marker_color="#E1000F",
                    marker_symbol=marker_symbol,
                    marker_size=marker_size,
                    line_dash=marker_line_style,
                )
                mins_x.append(incoming_data_by_month.index.min())
                numbers_of_data_points.append(len(incoming_data_by_month))
                lines.append(incoming_line)

            if len(outgoing_data_by_month) > 0:
                outgoing_line = go.Scatter(
                    x=outgoing_data_by_month.index,
                    y=outgoing_data_by_month,
                    name=outgoing_line_name,
                    mode="lines+markers",
                    hovertext=[
                        outgoing_hover_text.format(
                            index.strftime("%B %y").capitalize(), format_number_str(e)
                        )
                        for index, e in outgoing_data_by_month.items()
                    ],
                    hoverinfo="text",
                    marker_color="#6A6AF4",
                    marker_symbol=marker_symbol,
                    marker_size=marker_size,
                    line_dash=marker_line_style,
                )
                mins_x.append(outgoing_data_by_month.index.min())
                numbers_of_data_points.append(len(outgoing_data_by_month))
                lines.append(outgoing_line)

        fig.add_traces(lines)

        dtick = "M2"
        if not numbers_of_data_points or max(numbers_of_data_points) < 3:
            dtick = "M1"

        tickangle = 0
        y_legend = -0.07
        if numbers_of_data_points and max(numbers_of_data_points) >= 15:
            tickangle = -90
            y_legend = -0.12

        fig.update_layout(
            margin={"t": 20, "l": 35, "r": 5},
            legend={"orientation": "h", "y": y_legend, "x": 0},
            legend_font_size=11,
            legend_bgcolor="rgba(0,0,0,0)",
            showlegend=True,
            paper_bgcolor="#fff",
            plot_bgcolor="rgba(0,0,0,0)",
        )

        fig.update_xaxes(
            tickangle=tickangle,
            tickformat="%b %y",
            tick0=min(mins_x) if mins_x else None,
            dtick=dtick,
            gridcolor="#ccc",
        )
        fig.update_yaxes(exponentformat="B", tickformat=".2s", gridcolor="#ccc")

        self.figure = fig

    def build(self):
        self._preprocess_data()

        figure = {}
        if not self._check_data_empty():
            self._create_figure()
            figure = self.figure.to_json()

        return figure


class BsdTrackedAndRevisedProcessor:
    """Component with a Bar Figure of emitted, received and revised 'bordereaux'.

    Parameters
    ----------
    company_siret: str
        SIRET number of the establishment for which the data is displayed (used for data preprocessing).
    bs_data: DataFrame
        DataFrame containing data for a given 'bordereau' type.
    bs_revised_data: DataFrame
        DataFrame containing list of revised 'bordereaux' for a given 'bordereau' type.
    """

    def __init__(
        self,
        company_siret: str,
        bs_data: pd.DataFrame,
        data_date_interval: tuple[datetime, datetime],
        bs_revised_data: pd.DataFrame = None,
    ) -> None:
        self.company_siret = company_siret
        self.bs_data = bs_data
        self.data_date_interval = data_date_interval
        self.bs_revised_data = bs_revised_data
        self.bs_emitted_by_month = None
        self.bs_received_by_month = None
        self.bs_revised_by_month = None

    def _preprocess_bs_data(self) -> None:
        """Preprocess raw 'bordereaux' data to prepare it for plotting."""
        bs_data = self.bs_data

        bs_emitted = bs_data[
            (bs_data["emitter_company_siret"] == self.company_siret)
            & bs_data["sent_at"].between(*self.data_date_interval)
        ].dropna(subset=["sent_at"])

        bs_emitted_by_month = bs_emitted.groupby(
            pd.Grouper(key="sent_at", freq="1M")
        ).id.count()

        bs_received = bs_data[
            (bs_data["recipient_company_siret"] == self.company_siret)
            & bs_data["received_at"].between(*self.data_date_interval)
        ].dropna(subset=["received_at"])

        bs_received_by_month = bs_received.groupby(
            pd.Grouper(key="received_at", freq="1M")
        ).id.count()

        self.bs_emitted_by_month = bs_emitted_by_month
        self.bs_received_by_month = bs_received_by_month

    def _preprocess_bs_revised_data(self) -> None:
        """Preprocess raw revised 'bordereaux' data to prepare it for plotting."""
        bs_revised_data = self.bs_revised_data

        bs_revised_data = bs_revised_data[
            bs_revised_data["bs_id"].isin(self.bs_data["id"])
        ]
        bs_revised_by_month = bs_revised_data.groupby(
            pd.Grouper(key="created_at", freq="1M")
        ).bs_id.nunique()

        self.bs_revised_by_month = bs_revised_by_month

    def _check_data_empty(self) -> bool:
        bs_emitted_by_month = self.bs_emitted_by_month
        bs_received_by_month = self.bs_received_by_month

        if len(bs_emitted_by_month) == len(bs_received_by_month) == 0:
            return True

        return False

    def _create_figure(self) -> None:
        bs_emitted_by_month = self.bs_emitted_by_month
        bs_received_by_month = self.bs_received_by_month
        bs_revised_by_month = self.bs_revised_by_month

        text_size = 12

        bs_emitted_bars = go.Bar(
            x=bs_emitted_by_month.index,
            y=bs_emitted_by_month,
            name="Bordereaux émis",
            hovertext=[
                "{} - <b>{}</b> bordereau(x) émis".format(
                    index.strftime("%B %y").capitalize(), e
                )
                for index, e in bs_emitted_by_month.items()
            ],
            hoverinfo="text",
            textfont_size=text_size,
            textposition="outside",
            constraintext="none",
            marker_color="#6A6AF4",
        )

        bs_received_bars = go.Bar(
            x=bs_received_by_month.index,
            y=bs_received_by_month,
            name="Bordereaux reçus",
            hovertext=[
                "{} - <b>{}</b> bordereau(x) reçus".format(
                    index.strftime("%B %y").capitalize(), e
                )
                for index, e in bs_received_by_month.items()
            ],
            hoverinfo="text",
            textfont_size=text_size,
            textposition="outside",
            constraintext="none",
            marker_color="#E1000F",
        )

        if pd.isna(bs_emitted_by_month.index.min()):
            tick0_min = bs_received_by_month.index.min()
        elif pd.isna(bs_received_by_month.index.min()):
            tick0_min = bs_emitted_by_month.index.min()
        else:
            tick0_min = min(
                bs_emitted_by_month.index.min(), bs_received_by_month.index.min()
            )

        # Used to store the maximum value of each line
        # to be able to configure the height of the plotting area of the figure.
        max_y = max(bs_emitted_by_month.max(), bs_received_by_month.max())

        fig = go.Figure([bs_emitted_bars, bs_received_bars])

        max_points = max(len(bs_emitted_by_month), len(bs_received_by_month))

        tickangle = 0
        y_legend = -0.07
        if max_points >= 15:
            tickangle = -90
            y_legend = -0.15

        if bs_revised_by_month is not None:
            fig.add_trace(
                go.Bar(
                    x=bs_revised_by_month.index,
                    y=bs_revised_by_month,
                    name="Bordereaux corrigés",
                    hovertext=[
                        "{} - <b>{}</b> bordereau(x) révisés".format(
                            index.strftime("%B %y").capitalize(), e
                        )
                        for index, e in bs_revised_by_month.items()
                    ],
                    hoverinfo="text",
                    textfont_size=text_size,
                    textposition="outside",
                    constraintext="none",
                    marker_color="#B7A73F",
                )
            )
            tick0_min = min(tick0_min, bs_revised_by_month.index.min())
            max_y = max(max_y, bs_revised_by_month.max())
            max_points = max(max_points, len(bs_revised_by_month))

        fig.update_layout(
            margin={"t": 20, "l": 35, "r": 5},
            legend={
                "orientation": "h",
                "y": y_legend,
                "x": -0.1,
            },
            legend_bgcolor="rgba(0,0,0,0)",
            showlegend=True,
            paper_bgcolor="#fff",
            plot_bgcolor="rgba(0,0,0,0)",
        )

        ticklabelstep = 2
        if max_points <= 3:
            ticklabelstep = 1

        fig.update_xaxes(
            dtick=f"M{ticklabelstep}",
            tickangle=tickangle,
            tickformat="%b %y",
            tick0=tick0_min,
            ticks="outside",
            gridcolor="#ccc",
        )

        # Range of the y axis is increased to increase the height of the plotting are of the figure
        fig.update_yaxes(range=[0, max_y * 1.1], gridcolor="#ccc")

        self.figure = fig

    def build(self):
        self._preprocess_bs_data()
        if self.bs_revised_data is not None:
            self._preprocess_bs_revised_data()

        figure = {}
        if not self._check_data_empty():
            self._create_figure()
            figure = self.figure.to_json()

        return figure


class WasteOriginProcessor:
    """Component with a bar figure representing the quantity of waste received by départements (only TOP 6).

    Parameters
    company_siret: str
        SIRET number of the establishment for which the data is displayed (used for data preprocessing).
    bs_data_dfs: dict
        Dict with key being the 'bordereau' type and values the DataFrame containing the bordereau data.
    departements_regions_df: DataFrame
        Static data about regions and départements with their codes.
    """

    def __init__(
        self,
        company_siret: str,
        bs_data_dfs: Dict[str, pd.DataFrame],
        departements_regions_df: pd.DataFrame,
        data_date_interval: tuple[datetime, datetime],
    ) -> None:
        self.company_siret = company_siret
        self.bs_data_dfs = bs_data_dfs
        self.departements_regions_df = departements_regions_df
        self.data_date_interval = data_date_interval

        self.preprocessed_serie = None

    def _preprocess_data(self) -> None:
        if len(self.bs_data_dfs) == 0:
            return

        concat_df = pd.concat(
            [
                df[df["received_at"].between(*self.data_date_interval)]
                for df in self.bs_data_dfs.values()
            ]
        )

        # The postal code is extracted from the address field using a simple regex
        concat_df["cp"] = concat_df["emitter_company_address"].str.extract(
            r"([0-9]{5})", expand=False
        )
        concat_df["code_dep"] = concat_df["cp"].apply(get_code_departement)

        # 'Bordereau' data is merged with INSEE geographical data
        concat_df = pd.merge(
            concat_df,
            self.departements_regions_df,
            left_on="code_dep",
            right_on="DEP",
            how="left",
            validate="many_to_one",
        )

        # We create the column `cp_formatted` that will hold the two first digit
        # (three in the case of DOM/TOM) of the postal code
        concat_df.loc[~concat_df["code_dep"].isna(), "cp_formatted"] = (
            concat_df["LIBELLE_dep"] + " (" + concat_df["code_dep"] + ")"
        )

        # We handle the case of failed postal code extraction
        concat_df.loc[concat_df["code_dep"].isna(), "cp_formatted"] = "Origine inconnue"
        serie = (
            concat_df[concat_df["recipient_company_siret"] == self.company_siret]
            .groupby("cp_formatted")["quantity_received"]
            .sum()
        )

        serie.sort_values(ascending=False, inplace=True)

        # Only TOP 5 'départements' are kept
        final_serie = serie[:5]
        # Remaining 'départements' are summed and displayed as "others"
        final_serie["Autres origines"] = serie[5:].sum()
        final_serie = final_serie.astype(int)
        final_serie = final_serie.round(2)

        final_serie = final_serie[final_serie > 0]

        self.preprocessed_serie = final_serie

    def _check_data_empty(self) -> bool:
        if (
            (self.preprocessed_serie is None)
            or self.preprocessed_serie.isna().all()
            or len(self.preprocessed_serie) == 0
        ):
            return True

        return False

    def _create_figure(self) -> None:
        # Prepare order for horizontal bar chart, preserving "Autre origines" as bottom bar
        serie = pd.concat(
            (self.preprocessed_serie[-1:], self.preprocessed_serie[-2::-1])
        )

        # The bar chart has invisible bar (at *_annot positions) that will hold the labels
        # Invisible bar is the bar with width 0 but with a label.
        y_cats = [tup_e for e in serie.index for tup_e in (e, e + "_annot")]
        values = [tup_e for _, e in serie.items() for tup_e in (e, 0)]
        texts = [
            tup_e
            for index, value in serie.items()
            for tup_e in (
                "",
                f"<b>{format_number_str(value, precision=2)}t</b> - {index}",
            )
        ]
        hovertexts = [
            tup_e
            for index, value in serie.items()
            for tup_e in (
                f"{index} - <b>{format_number_str(value, precision=2)}t</b> reçues",
                "",
            )
        ]
        bar_trace = go.Bar(
            x=values,
            y=y_cats,
            orientation="h",
            text=texts,
            textfont_size=20,
            textposition="outside",
            width=[tup_e for e in values for tup_e in (0.7, 1)],
            hovertext=hovertexts,
            hoverinfo="text",
        )

        fig = go.Figure([bar_trace])
        fig.update_xaxes(visible=False)
        fig.update_yaxes(visible=False, type="category")
        fig.update_layout(
            margin={"t": 20, "b": 0, "l": 0, "r": 0},
            paper_bgcolor="#fff",
            plot_bgcolor="rgba(0,0,0,0)",
        )

        self.figure = fig

    def build(self):
        self._preprocess_data()

        figure = {}
        if not self._check_data_empty():
            self._create_figure()
            figure = self.figure.to_json()

        return figure


class WasteOriginsMapProcessor:
    """Component with a bubble map figure representing the quantity of waste received by regions.

    Parameters
    ----------
    company_siret: str
        SIRET number of the establishment for which the data is displayed (used for data preprocessing).
    bs_data_dfs: dict
        Dict with key being the 'bordereau' type and values the DataFrame containing the bordereau data.
    departements_regions_df: DataFrame
        Static data about regions and départements with their codes.
    regions_geodata: GeoDataFrame
        GeoDataFrame including regions geometries.
    """

    def __init__(
        self,
        company_siret: str,
        bs_data_dfs: Dict[str, pd.DataFrame],
        departements_regions_df: pd.DataFrame,
        regions_geodata: gpd.GeoDataFrame,
        data_date_interval: tuple[datetime, datetime],
    ) -> None:
        self.company_siret = company_siret
        self.bs_data_dfs = bs_data_dfs
        self.departements_regions_df = departements_regions_df
        self.regions_geodata = regions_geodata
        self.data_date_interval = data_date_interval

        self.preprocessed_df = None

    def _preprocess_data(self) -> None:
        if len(self.bs_data_dfs) == 0:
            return

        concat_df = pd.concat(
            [
                df[df["received_at"].between(*self.data_date_interval)]
                for df in self.bs_data_dfs.values()
            ]
        )

        # The postal code is extracted from the address field using a simple regex
        concat_df["cp"] = concat_df["emitter_company_address"].str.extract(
            r"([0-9]{5})", expand=False
        )
        concat_df["code_dep"] = concat_df["cp"].apply(get_code_departement)
        concat_df = pd.merge(
            concat_df,
            self.departements_regions_df,
            left_on="code_dep",
            right_on="DEP",
            how="left",
            validate="many_to_one",
        )

        # The 'Region' label is kept after aggregation
        df_grouped = (
            concat_df[concat_df["recipient_company_siret"] == self.company_siret]
            .groupby("LIBELLE_reg")
            .aggregate({"quantity_received": "sum", "REG": "max"})
        )

        final_df = pd.merge(
            self.regions_geodata, df_grouped, left_on="code", right_on="REG", how="left"
        )

        final_df.fillna(0, inplace=True)

        self.preprocessed_df = final_df

    def _check_data_empty(self) -> bool:
        if (
            (self.preprocessed_df is None)
            or self.preprocessed_df["quantity_received"].isna().all()
            or (len(self.preprocessed_df) == 0)
            or (self.preprocessed_df["quantity_received"] == 0).all()
        ):
            return True

        return False

    def _create_figure(self) -> None:
        gdf = self.preprocessed_df
        geojson = json.loads(gdf.to_json())

        # The figure is built in two part.
        # The first trace holds the 'region' geometries.
        # This trace doesn't hold preprocessed data.
        trace = go.Choropleth(
            geojson=geojson,
            z=[0] * len(gdf["quantity_received"]),
            locations=gdf.index,
            locationmode="geojson-id",
            colorscale=["#F9F8F6", "#F9F8F6"],
            marker_line_color="#979797",
            hoverinfo="skip",
            showscale=False,
        )

        sizeref = 2.0 * max(gdf["quantity_received"]) / (12**2)

        gdf_nonzero = gdf[gdf["quantity_received"] != 0]

        # This second trace will holds the circles that will be drawn on the map.
        # It is build using preprocessed data (size are relative to the quantity received).
        trace_2 = go.Scattergeo(
            geojson=geojson,
            locations=gdf_nonzero.index,
            locationmode="geojson-id",
            lat=gdf_nonzero.geometry.centroid.y,
            lon=gdf_nonzero.geometry.centroid.x,
            marker_sizeref=sizeref,
            marker_size=gdf_nonzero["quantity_received"],
            marker_sizemin=3,
            mode="markers+text",
            hovertext=[
                f"{e.nom} - <b>{format_number_str(e.quantity_received, precision=2)}t</b>"
                for e in gdf_nonzero.itertuples()
            ],
            hoverinfo="text",
            marker_color="#518FFF",
        )

        fig = go.Figure([trace, trace_2])
        fig.update_layout(
            margin={"b": 0, "t": 0, "r": 0, "l": 0},
            showlegend=False,
            legend_bgcolor="rgba(0,0,0,0)",
            xaxis_fixedrange=True,
            yaxis_fixedrange=True,
            dragmode=False,
        )
        fig.update_geos(
            fitbounds="locations",
            visible=False,
            showframe=False,
            projection_type="mercator",
        )

        self.figure = fig

        self._preprocess_data()

    def build(self):
        self._preprocess_data()

        figure = {}
        if not self._check_data_empty():
            self._create_figure()
            figure = self.figure.to_json()

        return figure


class ICPEDailyItemProcessor:
    """Component with a figure representing the quantity of waste processed by day for a particular ICPE "rubrique".


    Parameters:
    -----------
    icpe_item_daily_data: DataFrame
        DataFrame containing the waste processed data for a given ICPE "rubrique".
    """

    def __init__(
        self,
        icpe_item_daily_data: pd.DataFrame,
    ) -> None:
        self.icpe_item_daily_data = icpe_item_daily_data

        self.preprocessed_df = None
        self.authorized_quantity = None
        self.mean_quantity = None

        self.figure = None

    def _preprocess_data(self) -> None:
        if (self.icpe_item_daily_data is None) or (len(self.icpe_item_daily_data) == 0):
            return

        df = self.icpe_item_daily_data[["day_of_processing", "processed_quantity"]]
        df = df.sort_values("day_of_processing")

        self.mean_quantity = df["processed_quantity"].mean()

        series = df.set_index("day_of_processing").squeeze()
        final_df = series.resample("1d").max().fillna(0).reset_index()

        self.preprocessed_df = final_df
        self.authorized_quantity = self.icpe_item_daily_data[
            "authorized_quantity"
        ].max()

    def _check_data_empty(self) -> bool:
        if (self.preprocessed_df is None) or len(self.preprocessed_df) == 0:
            return True

        return False

    def _create_figure(self) -> None:
        df = self.preprocessed_df
        authorized_quantity = self.authorized_quantity
        trace = go.Scatter(
            x=df["day_of_processing"],
            y=df["processed_quantity"],
            hovertemplate="Le %{x|%d-%m-%Y} : <b>%{y:.2f}t</b> traitées<extra></extra>",
            line_width=1.5,
        )

        fig = go.Figure([trace])

        fig.update_layout(
            margin={"t": 40, "l": 35, "r": 70},
            legend_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            paper_bgcolor="#fff",
            plot_bgcolor="rgba(0,0,0,0)",
            title={
                "text": f"Quantité moyenne traitée par jour : <b>{format_number_str(self.mean_quantity,2)}</b> t/j",
                "font_size": 14,
            },
        )

        max_y = df["processed_quantity"].max()
        if not pd.isna(authorized_quantity):
            fig.add_hline(
                y=authorized_quantity,
                line_dash="dot",
                line_color="red",
                line_width=3,
            )
            fig.add_annotation(
                xref="x domain",
                yref="y",
                x=1,
                y=authorized_quantity,
                text=f"Quantité maximale <br>autorisée :<b>{format_number_str(authorized_quantity,2)}</b> t/jour",
                font_color="red",
                xanchor="left",
                showarrow=False,
                textangle=-90,
                font_size=13,
            )
            if authorized_quantity > max_y:
                max_y = authorized_quantity

        fig.update_yaxes(
            range=[0, max_y * 1.3], gridcolor="#ccc", title="Quantité traitée en tonnes"
        )

        fig.update_xaxes(
            gridcolor="#ccc",
            zeroline=True,
            linewidth=1,
            linecolor="black",
            title="Date du traitement",
        )

        self.figure = fig

    def build(self):
        self._preprocess_data()

        figure = {}
        if not self._check_data_empty():
            self._create_figure()
            figure = self.figure.to_json()

        return figure


class ICPEAnnualItemProcessor:
    """Component with a figure representing the cummulative quantity of waste processed by day for a particular ICPE "rubrique".


    Parameters:
    -----------
    icpe_item_daily_data: DataFrame
        DataFrame containing the waste processed data for a given ICPE "rubrique".
    """

    def __init__(
        self,
        icpe_item_daily_data: pd.DataFrame,
    ) -> None:
        self.icpe_item_daily_data = icpe_item_daily_data

        self.preprocessed_df = None
        self.authorized_quantity = None

        self.figure = None

    def _preprocess_data(self) -> None:
        if (self.icpe_item_daily_data is None) or (len(self.icpe_item_daily_data) == 0):
            return

        df = self.icpe_item_daily_data[["day_of_processing", "processed_quantity"]]
        df = df.sort_values("day_of_processing")

        series = df.set_index("day_of_processing").squeeze()
        final_df = series.resample("1d").max().fillna(0).reset_index()
        final_df["quantity_cumsum"] = final_df.groupby(
            final_df["day_of_processing"].dt.year
        ).cumsum()

        self.preprocessed_df = final_df
        self.authorized_quantity = self.icpe_item_daily_data[
            "authorized_quantity"
        ].max()

    def _check_data_empty(self) -> bool:
        if (self.preprocessed_df is None) or len(self.preprocessed_df) == 0:
            return True

        return False

    def _create_figure(self) -> None:
        df = self.preprocessed_df
        authorized_quantity = self.authorized_quantity

        traces = []
        for _, temp_df in df.groupby(df["day_of_processing"].dt.year):
            trace = go.Scatter(
                x=temp_df["day_of_processing"],
                y=temp_df["quantity_cumsum"],
                hovertemplate="Le %{x|%d-%m-%Y} : <b>%{y:.2f}t</b> traitées au total sur l'année<extra></extra>",
                line_width=2,
            )
            traces.append(trace)

        fig = go.Figure(traces)

        for trace in traces[1:]:
            year = trace["x"][0].year
            x = min(trace["x"])
            fig.add_vline(
                line_dash="dot",
                line_color="black",
                line_width=2,
                x=x.timestamp()
                * 1000,  # Due to this bug : https://github.com/plotly/plotly.py/issues/3065, we have to convert to epoch here
                annotation_text=f"{year}",
                annotation_position="top right",
            )

        fig.update_layout(
            margin={"t": 30, "l": 35, "r": 70},
            legend_bgcolor="rgba(0,0,0,0)",
            showlegend=False,
            paper_bgcolor="#fff",
            plot_bgcolor="rgba(0,0,0,0)",
        )

        max_y = df["quantity_cumsum"].max()
        if not pd.isna(authorized_quantity):
            fig.add_hline(
                y=authorized_quantity,
                line_dash="dot",
                line_color="red",
                line_width=3,
            )
            fig.add_annotation(
                xref="x domain",
                yref="y",
                x=1,
                y=authorized_quantity,
                text=f"Quantité maximale <br>autorisée :<b>{format_number_str(authorized_quantity,2)}</b> t/an",
                font_color="red",
                xanchor="left",
                showarrow=False,
                textangle=-90,
                font_size=13,
            )
            if authorized_quantity > max_y:
                max_y = authorized_quantity

        fig.update_yaxes(
            range=[0, max_y * 1.3],
            gridcolor="#ccc",
            title="Quantité traitée en tonnes<br>(somme cummulée annuellement)",
        )

        fig.update_xaxes(
            gridcolor="#ccc",
            zeroline=True,
            linewidth=1,
            linecolor="black",
            title="Date du traitement",
        )

        self.figure = fig

    def build(self):
        self._preprocess_data()

        figure = {}
        if not self._check_data_empty():
            self._create_figure()
            figure = self.figure.to_json()

        return figure
