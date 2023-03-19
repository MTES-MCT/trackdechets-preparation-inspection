import json
from datetime import datetime, timedelta, timezone
from typing import Dict

import geopandas as gpd
import numpy as np
import pandas as pd
import plotly.graph_objects as go

from sheets.utils import format_number_str, get_code_departement

# classes returning a serialized (json) plotly vizualization to be consumed by a plotly script


class BsddGraph:
    def __init__(self, company_siret, bs_data):
        self.bs_data = bs_data
        self.incoming_data_by_month = None
        self.outgoing_data_by_month = None
        self.company_siret = company_siret

    def _preprocess_data(self) -> None:
        bs_data = self.bs_data
        one_year_ago = (
            datetime.utcnow().replace(tzinfo=timezone.utc) - timedelta(days=365)
        ).strftime("%Y-%m-01")
        today_date = (
            datetime.utcnow().replace(tzinfo=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        )

        incoming_data = bs_data[
            (bs_data["recipient_company_siret"] == self.company_siret)
            & (bs_data["received_at"] >= one_year_ago)
            & (bs_data["received_at"] <= today_date)
        ]
        outgoing_data = bs_data[
            (bs_data["emitter_company_siret"] == self.company_siret)
            & (bs_data["sent_at"] >= one_year_ago)
        ]

        self.incoming_data_by_month = (
            incoming_data.groupby(pd.Grouper(key="received_at", freq="1M"))[
                "quantity_received"
            ]
            .sum()
            .replace(0, np.nan)
        )

        self.outgoing_data_by_month = (
            outgoing_data.groupby(pd.Grouper(key="sent_at", freq="1M"))[
                "quantity_received"
            ]
            .sum()
            .replace(0, np.nan)
        )

    def _check_data_empty(self) -> bool:
        incoming_data_by_month = self.incoming_data_by_month
        outgoing_data_by_month = self.outgoing_data_by_month

        if len(incoming_data_by_month) == len(outgoing_data_by_month) == 0:
            self.is_component_empty = True
            return True

        if incoming_data_by_month.isna().all() and outgoing_data_by_month.isna().all():
            self.is_component_empty = True
            return True

        if (incoming_data_by_month == 0).all() and (outgoing_data_by_month == 0).all():
            self.is_component_empty = True
            return True

        self.is_component_empty = False
        return False

    def _create_figure(self) -> None:
        incoming_data_by_month = self.incoming_data_by_month
        outgoing_data_by_month = self.outgoing_data_by_month

        incoming_line = go.Scatter(
            x=incoming_data_by_month.index,
            y=incoming_data_by_month,
            name="Quantité entrante",
            mode="lines+markers",
            # todo: localize month names
            hovertext=[
                f"{index.month_name()} - <b>{format_number_str(e)}</b> tonnes entrantes"
                for index, e in incoming_data_by_month.items()
            ],
            hoverinfo="text",
        )
        outgoing_line = go.Scatter(
            x=outgoing_data_by_month.index,
            y=outgoing_data_by_month,
            name="Quantité sortante",
            mode="lines+markers",
            hovertext=[
                f"{index.month_name()} - <b>{format_number_str(e)}</b> tonnes sortantes"
                for index, e in outgoing_data_by_month.items()
            ],
            hoverinfo="text",
        )

        fig = go.Figure(data=[incoming_line, outgoing_line])

        fig.update_layout(
            margin={"t": 20, "l": 35, "r": 5},
            legend={"orientation": "h", "y": -0.1, "x": 0.5},
            legend_font_size=11,
            showlegend=True,
            paper_bgcolor="#fff",
            plot_bgcolor="rgba(0,0,0,0)",
        )
        if pd.isna(incoming_data_by_month.index.min()):
            min_x = outgoing_data_by_month.index.min()
        elif pd.isna(outgoing_data_by_month.index.min()):
            min_x = incoming_data_by_month.index.min()
        else:
            min_x = min(
                incoming_data_by_month.index.min(), outgoing_data_by_month.index.min()
            )

        dtick = "M2"
        if max(len(incoming_data_by_month), len(outgoing_data_by_month)) < 3:
            dtick = "M1"

        fig.update_xaxes(
            tickangle=0, tickformat="%b", tick0=min_x, dtick=dtick, gridcolor="#ccc"
        )
        fig.update_yaxes(exponentformat="B", tickformat=".2s", gridcolor="#ccc")

        self.figure = fig

    def build(self):
        self._preprocess_data()
        self._create_figure()

        return self.figure.to_json()


class BSCreatedAndRevisedComponent:
    "cf BSCreatedAndRevisedComponent"
    """Component with a Bar Figure of created and revised 'bordereaux'.

    Parameters
    ----------
    component_title : str
        Title of the component that will be displayed in the component layout.
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
        bs_revised_data: pd.DataFrame = None,
    ) -> None:
        self.company_siret = company_siret
        self.bs_data = bs_data
        self.bs_revised_data = bs_revised_data
        self.bs_emitted_by_month = None
        self.bs_received_by_month = None
        self.bs_revised_by_month = None

    def _preprocess_bs_data(self) -> None:
        """Preprocess raw 'bordereaux' data to prepare it for plotting."""
        bs_data = self.bs_data

        bs_emitted = bs_data[
            bs_data["emitter_company_siret"] == self.company_siret
        ].dropna(subset=["created_at"])

        bs_emitted_by_month = bs_emitted.groupby(
            pd.Grouper(key="created_at", freq="1M")
        ).id.count()

        bs_received = bs_data[
            bs_data["recipient_company_siret"] == self.company_siret
        ].dropna(subset=["received_at"])

        bs_received_by_month = bs_received.groupby(
            pd.Grouper(key="received_at", freq="1M")
        ).id.count()

        self.bs_emitted_by_month = bs_emitted_by_month
        self.bs_received_by_month = bs_received_by_month

    def _preprocess_bs_revised_data(self) -> None:
        """Preprocess raw revised 'bordereaux' data to prepare it for plotting."""
        bs_revised_data = self.bs_revised_data

        bs_revised_by_month = bs_revised_data.groupby(
            pd.Grouper(key="created_at", freq="1M")
        ).id.count()

        self.bs_revised_by_month = bs_revised_by_month

    def _check_data_empty(self) -> bool:
        bs_emitted_by_month = self.bs_emitted_by_month
        bs_received_by_month = self.bs_received_by_month
        bs_revised_by_month = self.bs_revised_by_month

        if (
            len(bs_emitted_by_month) == len(bs_received_by_month) == 0
            and bs_revised_by_month is None
        ):
            self.is_component_empty = True
            return True

        self.is_component_empty = False
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
            text=bs_emitted_by_month,
            textfont_size=text_size,
            textposition="outside",
            constraintext="none",
        )

        bs_received_bars = go.Bar(
            x=bs_received_by_month.index,
            y=bs_received_by_month,
            name="Bordereaux reçus",
            text=bs_received_by_month,
            textfont_size=text_size,
            textposition="outside",
            constraintext="none",
        )

        tick0_min = min(
            bs_emitted_by_month.index.min(), bs_received_by_month.index.min()
        )

        max_y = max(bs_emitted_by_month.max(), bs_received_by_month.max())

        fig = go.Figure([bs_emitted_bars, bs_received_bars])

        max_points = max(len(bs_emitted_by_month), len(bs_received_by_month))
        if bs_revised_by_month is not None:
            fig.add_trace(
                go.Bar(
                    x=bs_revised_by_month.index,
                    y=bs_revised_by_month,
                    name="BSDD corrigés",
                    text=bs_revised_by_month,
                    textfont_size=text_size,
                    textposition="outside",
                    constraintext="none",
                )
            )
            tick0_min = min(tick0_min, bs_revised_by_month.index.min())
            max_y = max(max_y, bs_revised_by_month.max())
            max_points = max(max_points, len(bs_revised_by_month))

        fig.update_layout(
            margin={"t": 20, "l": 35, "r": 5},
            legend={"orientation": "h", "y": -0.05, "x": 0.5},
            showlegend=True,
            paper_bgcolor="#fff",
            plot_bgcolor="rgba(0,0,0,0)",
        )

        ticklabelstep = 2
        if max_points < 3:
            ticklabelstep = 1

        fig.update_xaxes(
            dtick="M1",
            tickangle=0,
            tickformat="%b",
            tick0=tick0_min,
            ticks="outside",
            ticklabelstep=ticklabelstep,
            gridcolor="#ccc",
        )

        fig.update_yaxes(range=[0, max_y * 1.1], gridcolor="#ccc")

        self.figure = fig

    def build(self):
        self._preprocess_bs_data()
        if self.bs_revised_data is not None:
            self._preprocess_bs_revised_data()
        self._create_figure()

        # return self.figure.to_image(format="png")
        return self.figure.to_json()


class WasteOriginsComponent:
    """Component with a bar figure representing the quantity of waste received by départements (only TOP 6).

    Parameters
    ----------
    component_title : str
        Title of the component that will be displayed in the component layout.
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
    ) -> None:
        self.company_siret = company_siret
        self.bs_data_dfs = bs_data_dfs
        self.departements_regions_df = departements_regions_df

        self.preprocessed_serie = None

    def _preprocess_data(self) -> None:
        if len(self.bs_data_dfs) == 0:
            return

        concat_df = pd.concat(list(self.bs_data_dfs.values()))

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

        concat_df.loc[~concat_df["code_dep"].isna(), "cp_formatted"] = (
            concat_df["LIBELLE_dep"] + " (" + concat_df["code_dep"] + ")"
        )
        concat_df.loc[concat_df["code_dep"].isna(), "cp_formatted"] = "Origine inconnue"
        serie = (
            concat_df[concat_df["recipient_company_siret"] == self.company_siret]
            .groupby("cp_formatted")["quantity_received"]
            .sum()
        )

        serie.sort_values(ascending=False, inplace=True)

        final_serie = serie[:5]
        final_serie["Autres origines"] = serie[5:].sum()
        final_serie = final_serie.round(2)
        final_serie = final_serie[final_serie > 0]

        self.preprocessed_serie = final_serie

    def _check_data_empty(self) -> bool:
        if (
            (self.preprocessed_serie is None)
            or self.preprocessed_serie.isna().all()
            or len(self.preprocessed_serie) == 0
        ):
            self.is_component_empty = True
            return True

        self.is_component_empty = False
        return False

    def _create_figure(self) -> None:
        # Prepare order for horizontal bar chart, preserving "Autre origines" has bottom bar
        serie = pd.concat(
            (self.preprocessed_serie[-1:], self.preprocessed_serie[-2::-1])
        )

        # The bar chart has invisible bar (at *_annot positions) that will hold the labels
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

        self._create_figure()

        return self.figure.to_json()


class WasteOriginsMapComponent:
    """Component with a bubble map figure representing the quantity of waste received by regions.

    Parameters
    ----------
    component_title : str
        Title of the component that will be displayed in the component layout.
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
    ) -> None:
        self.company_siret = company_siret
        self.bs_data_dfs = bs_data_dfs
        self.departements_regions_df = departements_regions_df
        self.regions_geodata = regions_geodata

        self.preprocessed_df = None

    def _preprocess_data(self) -> None:
        if len(self.bs_data_dfs) == 0:
            return

        concat_df = pd.concat(list(self.bs_data_dfs.values()))

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
            self.is_component_empty = True
            return True

        self.is_component_empty = False
        return False

    def _create_figure(self) -> None:
        gdf = self.preprocessed_df
        geojson = json.loads(gdf.to_json())
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
        self._create_figure()

        return self.figure.to_json()
