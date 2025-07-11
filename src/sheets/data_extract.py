import geopandas as gpd
import pandas as pd
import polars as pl
from django.conf import settings

CSV_FILES_DIR = settings.CSV_FILES_DIR


def load_departements_regions_data() -> pl.LazyFrame:
    """Load geographical data (départements and regions) and returns it as a LazyFrame.

    Columns included are :
    - code région
    - libellé region
    - code département
    - libellé département

    Returns
    -------
    LazyFrame
        LazyFrame with the regions and départements data.
    """

    df_departements = pl.read_csv(
        CSV_FILES_DIR / "departement_2022.csv",
        schema_overrides={e: pl.String for e in ["DEP", "REG", "CHEFLIEU", "TNCC", "NCC", "NCCENR", "LIBELLE"]},
    )
    df_regions = pl.read_csv(
        CSV_FILES_DIR / "region_2022.csv",
        schema_overrides={e: pl.String for e in ["REG", "CHEFLIEU", "TNCC", "NCC", "NCCENR", "LIBELLE"]},
    )
    dep_reg = df_departements.join(
        df_regions,
        left_on="REG",
        right_on="REG",
        how="left",
        validate="m:1",
        suffix="_reg",
    )

    return dep_reg.lazy()


def load_waste_code_data() -> pl.LazyFrame:
    """Load the nomenclature of waste and returns it as a LazyFrame.

    Columns included are :
    - code
    - description

    Returns
    -------
    LazyFrame
        LazyFrame with the the nomenclature of waste.
    """

    df = pl.read_csv(
        CSV_FILES_DIR / "code_dechets.csv", schema_overrides={e: pl.String for e in ["code", "description"]}
    )
    assert df["code"].is_unique().all()  # nosec

    return df.lazy()


def load_and_preprocess_regions_geographical_data() -> gpd.GeoDataFrame:
    """Load the geojson of french regions, transform it to group overseas territories near metropolitan territory
    and returns it as a DataFrame.

    Columns included are :
    - code région
    - geometry

    Returns
    -------
    DataFrame
        GeoDataFrame with the the nomenclature of waste.
    """

    gdf = gpd.read_file(CSV_FILES_DIR / "regions.geojson")

    translations = {
        "Guadeloupe": {"x": 55, "y": 30, "scale": 1.5},
        "Martinique": {"x": 56, "y": 31, "scale": 1.5},
        "La Réunion": {"x": -62, "y": 63, "scale": 1.5},
        "Mayotte": {"x": -50.5, "y": 54, "scale": 1.5},
        "Guyane": {"x": 47, "y": 40, "scale": 0.5},
    }
    for region, translation in translations.items():
        gdf.loc[gdf["nom"] == region, "geometry"] = (
            gdf.loc[gdf["nom"] == region, "geometry"]
            .translate(xoff=translation["x"], yoff=translation["y"], zoff=0.0)
            .scale(*(translation["scale"],) * 3)
        )

    return gdf
