import pandas as pd
import pytest
from datetime import datetime, timedelta
from ..graph_processors.html_components_processors import BsdStatsProcessor


@pytest.fixture
def sample_bs_data():
    # Create a sample DataFrame for bs_data
    created_at_datetimes = [
        datetime.now() - timedelta(days=95),
        datetime.now() - timedelta(days=65),
        datetime.now() - timedelta(days=35),
        datetime.now() - timedelta(days=20),
        datetime.now() - timedelta(days=10),
        datetime.now() - timedelta(days=5),
    ]
    sent_at_datetimes = [e + timedelta(days=1) for e in created_at_datetimes]
    received_at_datetimes = [e + timedelta(days=1) for e in sent_at_datetimes]
    time_to_process = [60, 1, 1, 1, 60, 1]
    processed_at_datetimes = [
        e + timedelta(days=t) for e, t in zip(received_at_datetimes, time_to_process)
    ]
    bs_data = pd.DataFrame(
        {
            "id": [i for i in range(1, 7)],
            "emitter_company_siret": [
                "123456789",
                "987654321",
                "123456789",
                "123456789",
                "987654321",
                "987654321",
            ],
            "recipient_company_siret": [
                "987654321",
                "123456789",
                "987654321",
                "987654321",
                "123456789",
                "123456789",
            ],
            "created_at": created_at_datetimes,
            "sent_at": sent_at_datetimes,
            "received_at": received_at_datetimes,
            "processed_at": processed_at_datetimes,
            "status": [
                "PROCESSED",
                "REFUSED",
                "RECEIVED",
                "SENT",
                "PROCESSED",
                "PROCESSED",
            ],
            "quantity_received": [10, 20, 2.5, 5, 8, 6.7],
            "volume": [10, 20, 2.5, 5, 8, 6.7],
        }
    )
    return bs_data


@pytest.fixture
def sample_bs_data_empty():
    # Create a sample DataFrame for bs_data that should generate empty component
    created_at_datetimes = [
        datetime.now()
        - timedelta(days=3000),  # More than one year ago, should be discarded
        datetime.now() - timedelta(days=65),
    ]
    sent_at_datetimes = [
        datetime.now() - timedelta(days=2900),
        datetime.now() - timedelta(days=40),
    ]
    received_at_datetimes = [
        datetime.now() - timedelta(days=2900),
        None,
    ]
    processed_at_datetimes = [
        datetime.now() - timedelta(days=2000),
        None,
    ]
    bs_data = pd.DataFrame(
        {
            "id": [i for i in range(1, 3)],
            "emitter_company_siret": [
                "123456789",
                "987654321",
            ],
            "recipient_company_siret": [
                "987654321",
                "123456789",
            ],
            "created_at": created_at_datetimes,
            "sent_at": sent_at_datetimes,
            "received_at": received_at_datetimes,
            "processed_at": processed_at_datetimes,
            "status": [
                "PROCESSED",
                "SENT",
            ],
            "quantity_received": [10, None],
        }
    )
    return bs_data


def test_bsd_stats_processor(sample_bs_data):
    siret = "123456789"
    bs_processor = BsdStatsProcessor(siret, sample_bs_data)

    # Test initialization
    assert bs_processor.company_siret == siret
    assert isinstance(bs_processor.bs_data, pd.DataFrame)
    assert bs_processor.quantity_variables_names == ["quantity_received"]
    assert bs_processor.bs_revised_data is None
    assert bs_processor.packagings_data is None

    # Test preprocessing
    bs_processor._preprocess_data()
    assert bs_processor._check_data_empty() == False

    # Test statistics computation
    context = bs_processor.build_context()

    assert context["emitted_bs_stats"]["total"] == "3"
    assert context["received_bs_stats"]["total"] == "3"

    assert context["emitted_bs_stats"]["archived"] == "1"
    assert context["received_bs_stats"]["archived"] == "3"

    assert context["emitted_bs_stats"]["processed_in_more_than_one_month_count"] == "1"
    assert context["received_bs_stats"]["processed_in_more_than_one_month_count"] == "1"

    assert (
        context["emitted_bs_stats"][
            "processed_in_more_than_one_month_avg_processing_time"
        ]
        == "60j"
    )
    assert (
        context["received_bs_stats"][
            "processed_in_more_than_one_month_avg_processing_time"
        ]
        == "60j"
    )

    assert (
        context["quantities_stats"]["quantity_received"]["total_quantity_incoming"]
        == "34.7"
    )
    assert (
        context["quantities_stats"]["quantity_received"]["total_quantity_outgoing"]
        == "17.5"
    )


def test_bsd_stats_processor_multiple_quantity_variables(sample_bs_data):
    siret = "123456789"
    bs_processor = BsdStatsProcessor(
        siret, sample_bs_data, quantity_variables_names=["quantity_received", "volume"]
    )

    # Test initialization
    assert bs_processor.company_siret == siret
    assert isinstance(bs_processor.bs_data, pd.DataFrame)
    assert bs_processor.quantity_variables_names == ["quantity_received", "volume"]
    assert bs_processor.bs_revised_data is None
    assert bs_processor.packagings_data is None

    # Test preprocessing
    bs_processor._preprocess_data()
    assert bs_processor._check_data_empty() == False

    # Test statistics computation
    context = bs_processor.build_context()

    assert context["emitted_bs_stats"]["total"] == "3"
    assert context["received_bs_stats"]["total"] == "3"
    assert (
        context["quantities_stats"]["quantity_received"]["total_quantity_incoming"]
        == "34.7"
    )
    assert context["quantities_stats"]["volume"]["total_quantity_incoming"] == "34.7"
    assert (
        context["quantities_stats"]["quantity_received"]["total_quantity_outgoing"]
        == "17.5"
    )
    assert context["quantities_stats"]["volume"]["total_quantity_incoming"] == "34.7"
    assert context["weight_volume_ratio"] == "1 000"


def test_bsd_stats_processor_empty_data(sample_bs_data_empty):
    # Test when the input data is empty
    siret = "123456789"
    empty_bs_data = sample_bs_data_empty
    bs_processor = BsdStatsProcessor(siret, empty_bs_data)
    bs_processor._preprocess_data()
    assert bs_processor._check_data_empty() == True

    data = bs_processor.build()
    assert data == {}
