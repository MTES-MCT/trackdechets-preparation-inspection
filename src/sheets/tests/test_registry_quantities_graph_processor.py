from datetime import datetime

import pandas as pd
import pytest

from ..graph_processors.plotly_components_processors import RegistryQuantitiesGraphProcessor


@pytest.fixture
def sample_data():
    incoming_data = pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "reception_date": [
                datetime(2024, 8, 9),
                datetime(2024, 8, 10),
                datetime(2024, 7, 15),  # Outside date interval
                datetime(2024, 8, 11),
                datetime(2024, 9, 12),
            ],
            "siret": [
                "12345678901234",
                "12345678901234",
                "98765432109876",  # Different SIRET
                "12345678901234",
                "12345678901234",
            ],
            "weight_value": [10, None, 30, None, 50],
            "volume": [None, 20, None, 40, None],
        }
    )

    outgoing_data = pd.DataFrame(
        {
            "id": [6, 7, 8, 9, 10],
            "dispatch_date": [
                datetime(2024, 8, 13),
                datetime(2024, 8, 14),
                datetime(2024, 10, 1),  # Outside date interval
                datetime(2024, 8, 15),
                datetime(2024, 8, 16),
            ],
            "siret": [
                "12345678901234",
                "12345678901234",
                "98765432109876",  # Different SIRET
                "12345678901234",
                "12345678901234",
            ],
            "unite": ["T", "M3", "T", "M3", "T"],
            "weight_value": [15, None, 35, None, 55],
            "volume": [None, 25, None, 45, None],
        }
    )

    date_interval = (datetime(2024, 8, 1), datetime(2024, 9, 30))

    return incoming_data, outgoing_data, date_interval


def test_initialization(sample_data):
    incoming_data, outgoing_data, date_interval = sample_data

    processor = RegistryQuantitiesGraphProcessor(
        company_siret="12345678901234",
        registry_incoming_data=incoming_data,
        registry_outgoing_data=outgoing_data,
        data_date_interval=date_interval,
    )

    assert processor.company_siret == "12345678901234"
    assert processor.registry_incoming_data is incoming_data
    assert processor.registry_outgoing_data is outgoing_data
    assert processor.data_date_interval == date_interval
    assert processor.incoming_weight_by_month_serie.empty
    assert processor.outgoing_weight_by_month_serie.empty
    assert processor.incoming_volume_by_month_serie.empty
    assert processor.outgoing_volume_by_month_serie.empty
    assert processor.figure is None


def test_preprocess_data(sample_data):
    incoming_data, outgoing_data, date_interval = sample_data

    processor = RegistryQuantitiesGraphProcessor(
        company_siret="12345678901234",
        registry_incoming_data=incoming_data,
        registry_outgoing_data=outgoing_data,
        data_date_interval=date_interval,
    )

    processor._preprocess_data()

    # Assert incoming data processing
    assert not processor.incoming_weight_by_month_serie.empty
    assert processor.incoming_weight_by_month_serie.shape == (2,)
    assert processor.incoming_weight_by_month_serie.sum() == 60  # 10 + 50
    assert not processor.incoming_volume_by_month_serie.empty
    assert processor.incoming_volume_by_month_serie.sum() == 60  # 20 + 40

    # Assert outgoing data processing
    assert not processor.outgoing_weight_by_month_serie.empty
    assert processor.outgoing_weight_by_month_serie.shape == (1,)
    assert processor.outgoing_weight_by_month_serie.sum() == 70  # 15 + 55
    assert not processor.outgoing_volume_by_month_serie.empty
    assert processor.outgoing_volume_by_month_serie.sum() == 70  # 25 + 45


def test_check_data_empty(sample_data):
    incoming_data, outgoing_data, date_interval = sample_data

    processor = RegistryQuantitiesGraphProcessor(
        company_siret="12345678901234",
        registry_incoming_data=incoming_data,
        registry_outgoing_data=outgoing_data,
        data_date_interval=date_interval,
    )

    processor._preprocess_data()

    assert not processor._check_data_empty()

    incoming_data, outgoing_data, date_interval = sample_data

    processor = RegistryQuantitiesGraphProcessor(
        company_siret="12345678901234",
        registry_incoming_data=incoming_data,
        registry_outgoing_data=outgoing_data,
        data_date_interval=(datetime(2023, 8, 1), datetime(2024, 6, 30)),
    )

    processor._preprocess_data()

    assert processor._check_data_empty()


def test_create_figure(sample_data):
    incoming_data, outgoing_data, date_interval = sample_data

    processor = RegistryQuantitiesGraphProcessor(
        company_siret="12345678901234",
        registry_incoming_data=incoming_data,
        registry_outgoing_data=outgoing_data,
        data_date_interval=date_interval,
    )

    processor._preprocess_data()
    processor._create_figure()

    assert processor.figure is not None


def test_build_output(sample_data):
    incoming_data, outgoing_data, date_interval = sample_data

    processor = RegistryQuantitiesGraphProcessor(
        company_siret="12345678901234",
        registry_incoming_data=incoming_data,
        registry_outgoing_data=outgoing_data,
        data_date_interval=date_interval,
    )

    result = processor.build()

    assert isinstance(result, str)  # JSON string
    assert len(result) > 0
