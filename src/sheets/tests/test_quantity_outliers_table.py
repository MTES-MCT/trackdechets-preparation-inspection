import pytest
import pandas as pd
import numpy as np
from datetime import datetime

from sheets.constants import BSDD, BSFF
from ..graph_processors.html_components_processors import QuantityOutliersTableProcessor


@pytest.fixture
def bs_data_dfs():
    return {
        BSDD: pd.DataFrame(
            {
                "id": [1, 2, 3, 4],
                "readable_id": [1, 2, 3, 4],
                "quantity_received": [50, 10, 45, 5],
                "quantity_refused": [7, None, None, 2],
                "received_at": [
                    datetime(2024, 8, 12),
                    datetime(2024, 8, 13),
                    datetime(2024, 8, 14),
                    datetime(2024, 8, 15),
                ],
                "emitter_company_siret": ["12345678900011", "12345678900011", "98765432100022", "98765432100022"],
                "recipient_company_siret": ["98765432100022", "98765432100022", "100000000000000", "12345678900011"],
                "waste_code": ["01 01 01*"] * 4,
                "waste_name": ["Waste Type A"] * 4,
            }
        ),
        BSFF: pd.DataFrame(
            {
                "id": [5, 6, 7, 8],
                "sent_at": [
                    datetime(2024, 8, 10),
                    datetime(2024, 8, 11),
                    datetime(2024, 8, 12),
                    datetime(2024, 8, 13),
                ],
                "received_at": [
                    datetime(2024, 8, 12),
                    datetime(2024, 8, 13),
                    datetime(2024, 8, 14),
                    datetime(2024, 8, 15),
                ],
                "emitter_company_siret": ["12345678900011", "12345678900011", "98765432100022", "98765432100022"],
                "recipient_company_siret": ["98765432100022", "98765432100022", "100000000000000", "12345678900011"],
                "waste_code": ["01 02 01*"] * 4,
                "waste_name": ["Waste Type A"] * 4,
            }
        ),
    }


@pytest.fixture
def packagings_data_df():
    return pd.DataFrame(
        {
            "bsff_id": [5, 5, 6, 7, 8],
            "acceptation_weight": [3, 40, 1, 2.4, 5],
            "acceptation_date": [
                datetime(2024, 8, 12),
                datetime(2024, 8, 12),
                datetime(2024, 8, 13),
                datetime(2024, 8, 14),
                datetime(2024, 8, 15),
            ],
        }
    )


@pytest.fixture
def transporters_data_df():
    return {
        BSDD: pd.DataFrame(
            {
                "bs_id": [1, 2, 3, 4],
                "transporter_company_siret": [
                    "100000000000000",
                    "100000000000000",
                    "12345678900011",
                    "100000000000000",
                ],
                "transporter_transport_mode": ["ROAD", "ROAD", "ROAD", "ROAD"],
                "sent_at": [
                    datetime(2024, 8, 10),
                    datetime(2024, 8, 11),
                    datetime(2024, 8, 12),
                    datetime(2024, 8, 13),
                ],
            }
        ),
        BSFF: pd.DataFrame(
            {
                "bs_id": [5, 6, 7, 8],
                "transporter_company_siret": [
                    "100000000000000",
                    "100000000000000",
                    "12345678900011",
                    "100000000000000",
                ],
                "transporter_transport_mode": ["ROAD", "ROAD", "ROAD", "ROAD"],
                "sent_at": [
                    datetime(2024, 8, 10),
                    datetime(2024, 8, 11),
                    datetime(2024, 8, 12),
                    datetime(2024, 8, 13),
                ],
            }
        ),
    }


@pytest.fixture
def data_date_interval():
    return datetime(2024, 8, 1), datetime(2024, 9, 30)


def test_preprocess_data(bs_data_dfs, transporters_data_df, packagings_data_df, data_date_interval):
    processor = QuantityOutliersTableProcessor(
        bs_data_dfs, transporters_data_df, data_date_interval, packagings_data_df
    )
    processor._preprocess_data()
    preprocessed_data = processor.preprocessed_data

    expected_data = pd.DataFrame(
        {
            "id": [1, 3, 5],
            "readable_id": [1.0, 3.0, np.nan],
            "quantity_received": [50.0, 45.0, 43.0],
            "quantity_refused": [7.0, np.nan, np.nan],
            "received_at": [
                pd.Timestamp("2024-08-12 00:00:00"),
                pd.Timestamp("2024-08-14 00:00:00"),
                pd.Timestamp("2024-08-12 00:00:00"),
            ],
            "emitter_company_siret": ["12345678900011", "98765432100022", "12345678900011"],
            "recipient_company_siret": ["98765432100022", "100000000000000", "98765432100022"],
            "waste_code": ["01 01 01*", "01 01 01*", "01 02 01*"],
            "waste_name": ["Waste Type A", "Waste Type A", "Waste Type A"],
            "bs_id": [1, 3, 5],
            "transporter_company_siret": ["100000000000000", "12345678900011", "100000000000000"],
            "transporter_transport_mode": ["ROAD", "ROAD", "ROAD"],
            "sent_at": [
                pd.Timestamp("2024-08-10 00:00:00"),
                pd.Timestamp("2024-08-12 00:00:00"),
                pd.Timestamp("2024-08-10 00:00:00"),
            ],
            "bs_type": ["bsdd", "bsdd", "bsff"],
        },
        index=[0, 2, 0],
    )
    assert preprocessed_data.equals(expected_data)


def test_check_data_empty(bs_data_dfs, transporters_data_df, packagings_data_df):
    processor = QuantityOutliersTableProcessor(
        bs_data_dfs, transporters_data_df, (datetime(2024, 9, 10), datetime(2024, 10, 10)), packagings_data_df
    )
    assert processor._check_data_empty() is True


def test_build(bs_data_dfs, transporters_data_df, data_date_interval, packagings_data_df):
    processor = QuantityOutliersTableProcessor(
        bs_data_dfs, transporters_data_df, data_date_interval, packagings_data_df
    )
    results = processor.build()

    expected_data = [
        {
            "id": 1,
            "bs_type": "bsdd",
            "emitter_company_siret": "12345678900011",
            "transporter_company_siret": "100000000000000",
            "recipient_company_siret": "98765432100022",
            "waste_code": "01 01 01*",
            "waste_name": "Waste Type A",
            "quantity": "50",
            "quantity_refused": "7",
            "sent_at": "10/08/2024 00:00",
            "received_at": "12/08/2024 00:00",
        },
        {
            "id": 5,
            "bs_type": "bsff",
            "emitter_company_siret": "12345678900011",
            "transporter_company_siret": "100000000000000",
            "recipient_company_siret": "98765432100022",
            "waste_code": "01 02 01*",
            "waste_name": "Waste Type A",
            "quantity": "43",
            "quantity_refused": None,
            "sent_at": "10/08/2024 00:00",
            "received_at": "12/08/2024 00:00",
        },
        {
            "id": 3,
            "bs_type": "bsdd",
            "emitter_company_siret": "98765432100022",
            "transporter_company_siret": "12345678900011",
            "recipient_company_siret": "100000000000000",
            "waste_code": "01 01 01*",
            "waste_name": "Waste Type A",
            "quantity": "45",
            "quantity_refused": None,
            "sent_at": "12/08/2024 00:00",
            "received_at": "14/08/2024 00:00",
        },
    ]

    assert results == expected_data
