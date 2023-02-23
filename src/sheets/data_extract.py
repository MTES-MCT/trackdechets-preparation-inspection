import geopandas as gpd
import pandas as pd
from django.conf import settings

CSV_FILES_DIR = settings.CSV_FILES_DIR


def load_departements_regions_data() -> pd.DataFrame:
    """Load geographical data (départements and regions) and returns it as a DataFrame.

    Columns included are :
    - code région
    - libellé region
    - code département
    - libellé département

    Returns
    -------
    DataFrame
        DataFrame with the regions and départements data.
    """

    df_departements = pd.read_csv(CSV_FILES_DIR / "departement_2022.csv", dtype="str")
    df_regions = pd.read_csv(CSV_FILES_DIR / "region_2022.csv", dtype="str")
    dep_reg = pd.merge(
        df_departements,
        df_regions,
        left_on="REG",
        right_on="REG",
        how="left",
        validate="many_to_one",
        suffixes=("_dep", "_reg"),
    )

    return dep_reg


def load_waste_code_data() -> pd.DataFrame:
    """Load the nomenclature of waste and returns it as a DataFrame.

    Columns included are :
    - code
    - description

    Returns
    -------
    DataFrame
        DataFrame with the the nomenclature of waste.
    """

    df = pd.read_csv(CSV_FILES_DIR / "code_dechets.csv", dtype="str", index_col="code")
    assert df.index.is_unique

    return df


def load_mapping_rubrique_processing_operation_code() -> pd.DataFrame:
    """Load the mapping processing operation code <=> rubrique.

    Columns included are :
    - code
    - description

    Returns
    -------
    DataFrame
        DataFrame with the the nomenclature of waste.
    """

    df = pd.read_csv(
        CSV_FILES_DIR / "mapping_rubrique_code_operation.csv",
        dtype="str",
    )

    return df


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
