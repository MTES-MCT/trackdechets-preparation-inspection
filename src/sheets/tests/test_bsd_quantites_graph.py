from datetime import datetime

import numpy as np
import pandas as pd
import pytest

from sheets.constants import BSDD, BSFF

from ..graph_processors.plotly_components_processors import (
    BsdQuantitiesGraph,
)  # Remplace "your_module" par le bon module


@pytest.fixture
def sample_data_bsdd():
    data = {
        "id": [1, 2, 3, 4],
        "recipient_company_siret": ["12345678900011", "12345678900011", "98765432100022", "12345678900011"],
        "emitter_company_siret": ["98765432100022", "98765432100022", "12345678900011", "98765432100011"],
        "received_at": pd.to_datetime(["2024-01-10", "2024-02-15", "2024-03-20", "2024-04-25"]),
        "sent_at": pd.to_datetime(["2024-01-05", "2024-02-10", "2024-03-15", "2024-04-20"]),
        "quantity_received": [10, 20, 30, 40],
        "quantity_refused": [1, None, 2, 40],
    }
    return pd.DataFrame(data)


@pytest.fixture
def sample_data_bsff():
    data = {
        "id": [1, 2, 3, 4],
        "recipient_company_siret": ["12345678900011", "98765432100022", "98765432100022", "12345678900011"],
        "emitter_company_siret": ["98765432100022", "12345678900011", "12345678900011", "98765432100011"],
        "sent_at": pd.to_datetime(["2024-01-05", "2024-02-10", "2024-03-15", "2024-04-20"]),
        "received_at": pd.to_datetime(["2024-01-10", "2024-02-15", "2024-03-20", "2024-04-25"]),
    }
    return pd.DataFrame(data)


@pytest.fixture
def sample_packagings():
    data = {
        "bsff_id": [1, 2, 2, 4, 4],
        "acceptation_date": pd.to_datetime(["2024-01-12", "2024-02-18", "2024-03-22", "2024-04-28", "2024-04-30"]),
        "acceptation_weight": [5, 10, 15, 20, 3],
    }
    return pd.DataFrame(data)


def test_bsd_quantities_graph_bsdd(sample_data_bsdd):
    company_siret = "12345678900011"
    bs_type = BSDD
    data_date_interval = (datetime(2024, 1, 1), datetime(2024, 12, 31))
    quantity_variables_names = ["quantity_received"]

    processor = BsdQuantitiesGraph(
        company_siret=company_siret,
        bs_type=bs_type,
        bs_data=sample_data_bsdd,
        data_date_interval=data_date_interval,
        quantity_variables_names=quantity_variables_names,
    )

    processor._preprocess_data()

    expected_incoming_data_by_month_series = pd.Series(
        data=[
            9.0,
            20.0,
            np.nan,
            np.nan,
        ],
        index=[
            pd.Timestamp("2024-01-31 00:00:00", freq="M"),
            pd.Timestamp("2024-02-29 00:00:00", freq="M"),
            pd.Timestamp("2024-03-31 00:00:00", freq="M"),
            pd.Timestamp("2024-04-30 00:00:00", freq="M"),
        ],
    )
    expected_outgoing_data_by_month_series = pd.Series(
        data=[28.0], index=[pd.Timestamp("2024-03-31 00:00:00", freq="M")]
    )

    assert processor.incoming_data_by_month_series[0].equals(expected_incoming_data_by_month_series)
    assert processor.outgoing_data_by_month_series[0].equals(expected_outgoing_data_by_month_series)


def test_empty_data(sample_data_bsdd):
    # Case no data matching dates
    company_siret = "12345678900011"
    bs_type = BSDD
    data_date_interval = (datetime(2025, 1, 1), datetime(2025, 12, 31))
    quantity_variables_names = ["quantity_received"]

    processor = BsdQuantitiesGraph(
        company_siret=company_siret,
        bs_type=bs_type,
        bs_data=sample_data_bsdd,
        data_date_interval=data_date_interval,
        quantity_variables_names=quantity_variables_names,
    )

    processor._preprocess_data()

    assert processor._check_data_empty() is True

    sample_data_bsdd["quantity_received"] = [np.nan] * len(sample_data_bsdd)
    sample_data_bsdd["quantity_refused"] = [np.nan] * len(sample_data_bsdd)
    data_date_interval = (datetime(2024, 1, 1), datetime(2024, 12, 31))
    processor = BsdQuantitiesGraph(
        company_siret=company_siret,
        bs_type=bs_type,
        bs_data=sample_data_bsdd,
        data_date_interval=data_date_interval,
        quantity_variables_names=quantity_variables_names,
    )

    processor._preprocess_data()


def test_bsd_quantities_graph_bsff(sample_data_bsff, sample_packagings):
    company_siret = "12345678900011"
    bs_type = BSFF
    data_date_interval = (datetime(2024, 1, 1), datetime(2024, 12, 31))
    quantity_variables_names = [
        "acceptation_weight",
    ]

    processor = BsdQuantitiesGraph(
        company_siret=company_siret,
        bs_type=bs_type,
        bs_data=sample_data_bsff,
        data_date_interval=data_date_interval,
        quantity_variables_names=quantity_variables_names,
        packagings_data=sample_packagings,
    )

    processor._preprocess_data()

    expected_incoming_data_by_month_series = pd.Series(
        data=[
            5.0,
            np.nan,
            np.nan,
            23.0,
        ],
        index=[
            pd.Timestamp("2024-01-31 00:00:00", freq="M"),
            pd.Timestamp("2024-02-29 00:00:00", freq="M"),
            pd.Timestamp("2024-03-31 00:00:00", freq="M"),
            pd.Timestamp("2024-04-30 00:00:00", freq="M"),
        ],
    )
    expected_outgoing_data_by_month_series = pd.Series(
        data=[25], index=[pd.Timestamp("2024-02-29 00:00:00", freq="M")]
    )

    assert processor.incoming_data_by_month_series[0].equals(expected_incoming_data_by_month_series)
    assert processor.outgoing_data_by_month_series[0].equals(expected_outgoing_data_by_month_series)


def test_bsd_quantities_graph_bsff_without_acceptation_date(sample_data_bsff, sample_packagings):
    company_siret = "12345678900011"
    bs_type = BSFF
    data_date_interval = (datetime(2024, 1, 1), datetime(2024, 12, 31))
    quantity_variables_names = [
        "acceptation_weight",
    ]

    sample_packagings["acceptation_date"] = [pd.NaT] * len(sample_packagings)

    processor = BsdQuantitiesGraph(
        company_siret=company_siret,
        bs_type=bs_type,
        bs_data=sample_data_bsff,
        data_date_interval=data_date_interval,
        quantity_variables_names=quantity_variables_names,
        packagings_data=sample_packagings,
    )

    processor._preprocess_data()

    expected_incoming_data_by_month_series = pd.Series([])
    expected_outgoing_data_by_month_series = pd.Series(
        data=[25], index=[pd.Timestamp("2024-02-29 00:00:00", freq="M")]
    )

    assert processor.incoming_data_by_month_series[0].equals(expected_incoming_data_by_month_series)
    assert processor.outgoing_data_by_month_series[0].equals(expected_outgoing_data_by_month_series)
