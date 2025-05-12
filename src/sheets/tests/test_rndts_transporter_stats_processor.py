from datetime import datetime

import pandas as pd
import pytest

from ..graph_processors.html_components_processors import RegistryTransporterStatsProcessor


@pytest.fixture
def sample_rndts_data():
    # Sample RNDTS data for different cases
    return {
        "ndw_incoming": pd.DataFrame(
            {
                "id": [1, 2, 3],
                "date_reception": [datetime(2024, 8, 9), datetime(2024, 8, 10), datetime(2024, 8, 10)],
                "numeros_indentification_transporteurs": [
                    ["12345678901234"],
                    ["23456789012345"],
                    ["12345678901234", "34567890123456"],
                ],
                "quantite": [25, 12, 9.7],
                "unite": ["T", "T", "M3"],
            }
        ),
        "ndw_outgoing": pd.DataFrame(
            {
                "id": [3],
                "date_expedition": [datetime(2024, 8, 11)],
                "numeros_indentification_transporteurs": [["12345678901234"]],
                "quantite": [30],
                "unite": ["M3"],
            }
        ),
        "excavated_land_incoming": pd.DataFrame(
            {
                "id": [4, 5],
                "date_reception": [datetime(2024, 8, 12), datetime(2024, 8, 13)],
                "numeros_indentification_transporteurs": [["34567890123456"], ["12345678901234"]],
                "quantite": [12.6, 3],
                "unite": ["M3", "T"],
            }
        ),
        "excavated_land_outgoing": pd.DataFrame(
            {
                "id": [6],
                "date_expedition": [datetime(2024, 8, 14)],
                "numeros_indentification_transporteurs": [["12345678901234"]],
                "quantite": [40],
                "unite": ["T"],
            }
        ),
    }


@pytest.fixture
def date_interval():
    return (datetime(2024, 8, 1), datetime(2024, 8, 31))


def test_initialization(sample_rndts_data, date_interval):
    processor = RegistryTransporterStatsProcessor(
        company_siret="12345678901234",
        registry_data=sample_rndts_data,
        data_date_interval=date_interval,
    )

    assert processor.company_siret == "12345678901234"
    assert processor.registry_data == sample_rndts_data
    assert processor.data_date_interval == date_interval
    assert isinstance(processor.transported_statements_stats, dict)
    assert "ndw_incoming" in processor.transported_statements_stats


def test_empty_data(sample_rndts_data, date_interval):
    empty_data = {
        "ndw_incoming": pd.DataFrame(),
        "ndw_outgoing": pd.DataFrame(),
        "excavated_land_incoming": pd.DataFrame(),
        "excavated_land_outgoing": pd.DataFrame(),
    }
    processor = RegistryTransporterStatsProcessor(
        company_siret="12345678901234",
        registry_data=empty_data,
        data_date_interval=date_interval,
    )

    empty_data = {
        "ndw_incoming": None,
        "ndw_outgoing": None,
        "excavated_land_incoming": None,
        "excavated_land_outgoing": None,
    }
    processor = RegistryTransporterStatsProcessor(
        company_siret="12345678901234",
        registry_data=empty_data,
        data_date_interval=date_interval,
    )

    # Test data not in date interval
    processor = RegistryTransporterStatsProcessor(
        company_siret="12345678901234",
        registry_data=sample_rndts_data,
        data_date_interval=(datetime(2023, 8, 1), datetime(2024, 7, 30)),
    )

    assert processor.build() == {}


def test_data_preprocessing(sample_rndts_data, date_interval):
    processor = RegistryTransporterStatsProcessor(
        company_siret="12345678901234",
        registry_data=sample_rndts_data,
        data_date_interval=date_interval,
    )

    processor._preprocess_bs_data()

    assert processor.transported_statements_stats["ndw_incoming"]["count"] == 2
    assert processor.transported_statements_stats["ndw_incoming"]["mass_quantity"] == "25"
    assert processor.transported_statements_stats["ndw_incoming"]["volume_quantity"] == "9.7"

    assert processor.transported_statements_stats["ndw_outgoing"]["count"] == 1
    assert processor.transported_statements_stats["ndw_outgoing"]["mass_quantity"] == "0"
    assert processor.transported_statements_stats["ndw_outgoing"]["volume_quantity"] == "30"

    assert processor.transported_statements_stats["excavated_land_incoming"]["count"] == 1
    assert processor.transported_statements_stats["excavated_land_incoming"]["mass_quantity"] == "3"
    assert processor.transported_statements_stats["excavated_land_incoming"]["volume_quantity"] == "0"

    assert processor.transported_statements_stats["excavated_land_outgoing"]["count"] == 1
    assert processor.transported_statements_stats["excavated_land_outgoing"]["mass_quantity"] == "40"
    assert processor.transported_statements_stats["excavated_land_outgoing"]["volume_quantity"] == "0"


def test_build_output(sample_rndts_data, date_interval):
    processor = RegistryTransporterStatsProcessor(
        company_siret="12345678901234",
        registry_data=sample_rndts_data,
        data_date_interval=date_interval,
    )

    result = processor.build()

    assert isinstance(result, dict)
    assert len(result) > 0

    assert "ndw_incoming" in result
    assert "mass_quantity" in result["ndw_incoming"]
    assert "volume_quantity" in result["ndw_incoming"]
    assert result["ndw_incoming"]["count"] == 2
    assert result["ndw_incoming"]["mass_quantity"] == "25"
    assert result["ndw_incoming"]["volume_quantity"] == "9.7"

    assert "ndw_outgoing" in result
    assert "mass_quantity" in result["ndw_outgoing"]
    assert "volume_quantity" in result["ndw_outgoing"]
    assert result["ndw_outgoing"]["count"] == 1
    assert result["ndw_outgoing"]["mass_quantity"] == "0"
    assert result["ndw_outgoing"]["volume_quantity"] == "30"

    assert "excavated_land_incoming" in result
    assert "mass_quantity" in result["excavated_land_incoming"]
    assert "volume_quantity" in result["excavated_land_incoming"]
    assert result["excavated_land_incoming"]["count"] == 1
    assert result["excavated_land_incoming"]["mass_quantity"] == "3"
    assert result["excavated_land_incoming"]["volume_quantity"] == "0"

    assert "excavated_land_outgoing" in result
    assert "mass_quantity" in result["excavated_land_outgoing"]
    assert "volume_quantity" in result["excavated_land_outgoing"]
    assert result["excavated_land_outgoing"]["count"] == 1
    assert result["excavated_land_outgoing"]["mass_quantity"] == "40"
    assert result["excavated_land_outgoing"]["volume_quantity"] == "0"
