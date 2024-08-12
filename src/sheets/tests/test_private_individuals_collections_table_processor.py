import pytest
import pandas as pd
from datetime import datetime
from ..graph_processors.html_components_processors import PrivateIndividualsCollectionsTableProcessor


@pytest.fixture
def sample_data():
    # Provide sample data as DataFrames
    bsda_data = pd.DataFrame(
        {
            "id": [1, 2, 3],
            "emitter_is_private_individual": [True, False, True],
            "recipient_company_siret": ["12345678901234", "12345678901234", "98765432109876"],
            "worker_company_siret": [None, "12345678901234", None],
            "emitter_company_name": ["Company A", "Company B", "Company C"],
            "emitter_company_address": ["Address A", "Address B", "Address C"],
            "worksite_name": ["Site A", "Site B", None],
            "worksite_address": ["Address SA", "Address SB", None],
            "waste_code": ["D123", "D456", "D789"],
            "waste_name": ["Waste A", "Waste B", "Waste C"],
            "received_at": [datetime(2024, 8, 10), datetime(2024, 8, 12), datetime(2024, 8, 15)],
        }
    )

    transport_data = pd.DataFrame(
        {
            "bs_id": [1, 2, 3],
            "sent_at": [datetime(2024, 8, 9), datetime(2024, 8, 11), datetime(2024, 8, 14)],
            "quantity_received": [100, 200, 300],
            "transporter_company_siret": ["23456789012345", "23456789012345", "34567890123456"],
        }
    )

    return bsda_data, transport_data


@pytest.fixture
def date_interval():
    return (datetime(2024, 8, 1), datetime(2024, 8, 31))


def test_initialization(sample_data, date_interval):
    bsda_data, transport_data = sample_data
    processor = PrivateIndividualsCollectionsTableProcessor(
        company_siret="12345678901234",
        bsda_data_df=bsda_data,
        bsda_transporters_data_df=transport_data,
        data_date_interval=date_interval,
    )

    assert processor.company_siret == "12345678901234"
    assert processor.bsda_data_df.equals(bsda_data)
    assert processor.bsda_transporters_data_df.equals(transport_data)
    assert processor.data_date_interval == date_interval


def test_empty_data(date_interval):
    empty_df = pd.DataFrame()
    processor = PrivateIndividualsCollectionsTableProcessor(
        company_siret="12345678901234",
        bsda_data_df=empty_df,
        bsda_transporters_data_df=None,
        data_date_interval=date_interval,
    )

    assert processor.build() == []


def test_data_preprocessing(sample_data, date_interval):
    bsda_data, transport_data = sample_data
    processor = PrivateIndividualsCollectionsTableProcessor(
        company_siret="12345678901234",
        bsda_data_df=bsda_data,
        bsda_transporters_data_df=transport_data,
        data_date_interval=date_interval,
    )

    processor._preprocess_data()

    assert processor.preprocessed_data is not None
    assert len(processor.preprocessed_data) == 1  # Only 1 row should match the company_siret


def test_build_output(sample_data, date_interval):
    bsda_data, transport_data = sample_data
    processor = PrivateIndividualsCollectionsTableProcessor(
        company_siret="12345678901234",
        bsda_data_df=bsda_data,
        bsda_transporters_data_df=transport_data,
        data_date_interval=date_interval,
    )

    result = processor.build()

    assert len(result) == 1  # Only 1 row should match both private individual and company_siret
    assert result[0]["id"] == 1
    assert result[0]["quantity"] == 100
    assert result[0]["sent_at"] == "09/08/2024 00:00"  # Converted to string format
