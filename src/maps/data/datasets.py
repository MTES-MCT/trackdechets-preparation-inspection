"""This module contains the raw datasets.
The datasets are loaded in memory to be reusable by other functions.
"""

from dataclasses import dataclass

import polars as pl

from .data_extract import extract_dataset
from .queries import (
    icpe_departements_waste_processed_sql,
    icpe_france_waste_processed_sql,
    icpe_installations_sql,
    icpe_installations_waste_processed_sql,
    icpe_regions_waste_processed_sql,
)


@dataclass
class Computed:
    icpe_installations_data: pl.DataFrame
    icpe_installations_waste_processed_data: pl.DataFrame
    icpe_departements_waste_processed_data: pl.DataFrame
    icpe_regions_waste_processed_data: pl.DataFrame
    icpe_france_waste_processed_data: pl.DataFrame


def get_data_df():
    icpe_installations_data = extract_dataset(
        icpe_installations_sql,
        {
            "code_aiot": pl.String,
            "siret": pl.String,
            "raison_sociale": pl.String,
            "rubrique": pl.String,
            "quantite_autorisee": pl.Float64,
            "unite": pl.String,
            "latitude": pl.Float64,
            "longitude": pl.Float64,
            "adresse1": pl.String,
            "adresse2": pl.String,
            "code_postal": pl.String,
            "commune": pl.String,
        },
    )
    icpe_installations_waste_processed_data = extract_dataset(
        icpe_installations_waste_processed_sql,
        {
            "code_aiot": pl.String,
            "siret": pl.String,
            "raison_sociale": pl.String,
            "rubrique": pl.String,
            "quantite_autorisee": pl.Float64,
            "quantite_objectif": pl.Float64,
            "unite": pl.String,
            "latitude": pl.Float64,
            "longitude": pl.Float64,
            "adresse1": pl.String,
            "adresse2": pl.String,
            "code_postal": pl.String,
            "commune": pl.String,
        },
    )
    icpe_departements_waste_processed_data = extract_dataset(icpe_departements_waste_processed_sql)
    icpe_regions_waste_processed_data = extract_dataset(icpe_regions_waste_processed_sql)
    icpe_france_waste_processed_data = extract_dataset(icpe_france_waste_processed_sql)

    data = Computed(
        icpe_installations_data=icpe_installations_data,
        icpe_installations_waste_processed_data=icpe_installations_waste_processed_data,
        icpe_departements_waste_processed_data=icpe_departements_waste_processed_data,
        icpe_regions_waste_processed_data=icpe_regions_waste_processed_data,
        icpe_france_waste_processed_data=icpe_france_waste_processed_data,
    )
    return data
