import pytest
import pandas as pd
from datetime import datetime
from ..graph_processors.plotly_components_processors import RNDTSStatementsGraphProcessor


@pytest.fixture
def sample_data():
    incoming_data = pd.DataFrame(
        {
            "id": [1, 2, 3, 4],
            "date_reception": [
                datetime(2024, 8, 9),
                datetime(2024, 9, 10),
                datetime(2024, 7, 15),  # Not in data interval
                datetime(2024, 8, 15),
            ],
            "numero_identification_declarant": [
                "12345678901234",
                "12345678901234",
                "12345678901234",
                "98765432109876",
            ],
        }
    )

    outgoing_data = pd.DataFrame(
        {
            "id": [4, 5, 6],
            "date_expedition": [
                datetime(2024, 8, 11),
                datetime(2024, 8, 12),
                datetime(2024, 8, 1),
            ],
            "numero_identification_declarant": [
                "12345678901234",
                "12345678901234",
                "98765432109876",
            ],
        }
    )

    date_interval = (datetime(2024, 8, 1), datetime(2024, 9, 30))

    return incoming_data, outgoing_data, date_interval


def test_initialization(sample_data):
    incoming_data, outgoing_data, date_interval = sample_data

    processor = RNDTSStatementsGraphProcessor(
        company_siret="12345678901234",
        rndts_incoming_data=incoming_data,
        rndts_outgoing_data=outgoing_data,
        statement_type="non_dangerous_waste",
        data_date_interval=date_interval,
    )

    assert processor.company_siret == "12345678901234"
    assert processor.rndts_incoming_data is incoming_data
    assert processor.rndts_outgoing_data is outgoing_data
    assert processor.statement_type == "non_dangerous_waste"
    assert processor.data_date_interval == date_interval
    assert processor.statements_emitted_by_month_serie is None
    assert processor.statements_received_by_month_serie is None
    assert processor.figure is None


def test_preprocess_bs_data(sample_data):
    incoming_data, outgoing_data, date_interval = sample_data

    processor = RNDTSStatementsGraphProcessor(
        company_siret="12345678901234",
        rndts_incoming_data=incoming_data,
        rndts_outgoing_data=outgoing_data,
        statement_type="non_dangerous_waste",
        data_date_interval=date_interval,
    )

    processor._preprocess_bs_data()

    # Only two rows for each data set should be included in the series, as the others are either outside the date interval or have a different SIRET
    assert processor.statements_received_by_month_serie is not None
    assert processor.statements_received_by_month_serie.shape == (2,)
    assert processor.statements_received_by_month_serie.sum() == 2
    assert processor.statements_emitted_by_month_serie is not None
    assert processor.statements_emitted_by_month_serie.shape == (1,)
    assert processor.statements_emitted_by_month_serie.sum() == 2


def test_check_data_empty(sample_data):
    incoming_data, outgoing_data, date_interval = sample_data

    processor = RNDTSStatementsGraphProcessor(
        company_siret="12345678901234",
        rndts_incoming_data=incoming_data,
        rndts_outgoing_data=outgoing_data,
        statement_type="non_dangerous_waste",
        data_date_interval=date_interval,
    )

    processor._preprocess_bs_data()

    assert not processor._check_data_empty()

    processor = RNDTSStatementsGraphProcessor(
        company_siret="12345678901234",
        rndts_incoming_data=incoming_data,
        rndts_outgoing_data=outgoing_data,
        statement_type="non_dangerous_waste",
        data_date_interval=(datetime(2023, 8, 1), datetime(2024, 7, 1)),
    )

    processor._preprocess_bs_data()

    assert processor._check_data_empty()


def test_create_figure(sample_data):
    incoming_data, outgoing_data, date_interval = sample_data

    processor = RNDTSStatementsGraphProcessor(
        company_siret="12345678901234",
        rndts_incoming_data=incoming_data,
        rndts_outgoing_data=outgoing_data,
        statement_type="non_dangerous_waste",
        data_date_interval=date_interval,
    )

    processor._preprocess_bs_data()
    processor._create_figure()

    assert processor.figure is not None


def test_build_output(sample_data):
    incoming_data, outgoing_data, date_interval = sample_data

    processor = RNDTSStatementsGraphProcessor(
        company_siret="12345678901234",
        rndts_incoming_data=incoming_data,
        rndts_outgoing_data=outgoing_data,
        statement_type="non_dangerous_waste",
        data_date_interval=date_interval,
    )

    result = processor.build()

    assert isinstance(result, str)  # JSON string
    assert len(result) > 0
