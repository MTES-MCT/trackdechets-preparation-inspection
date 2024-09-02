import pytest
import pandas as pd
from pandas import Timestamp
from datetime import datetime
import plotly.graph_objects as go
from ..graph_processors.plotly_components_processors import (
    ICPEAnnualItemProcessor,
)  # Import ICPEAnnualItemProcessor from the module where it is defined


# Sample data fixture
@pytest.fixture
def sample_icpe_data():
    data = {
        "day_of_processing": [
            datetime(2023, 1, 1),
            datetime(2023, 1, 2),
            datetime(2023, 1, 3),
            datetime(2023, 1, 4),
            datetime(2023, 1, 5),
            datetime(2023, 1, 6),
            datetime(2023, 1, 7),
            datetime(2023, 1, 8),
            datetime(2023, 1, 9),
            datetime(2023, 1, 10),
        ],
        "processed_quantity": [10, 20, 15, 0, 5, 0, 25, 30, 0, 5],
        "authorized_quantity": [50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
    }

    return pd.DataFrame(data)


def test_preprocess_data(sample_icpe_data):
    processor = ICPEAnnualItemProcessor(icpe_item_daily_data=sample_icpe_data)

    processor._preprocess_data()

    preprocessed_df = processor.preprocessed_df

    expected_output = pd.DataFrame(
        {
            "day_of_processing": [
                Timestamp("2023-01-01 00:00:00"),
                Timestamp("2023-01-02 00:00:00"),
                Timestamp("2023-01-03 00:00:00"),
                Timestamp("2023-01-04 00:00:00"),
                Timestamp("2023-01-05 00:00:00"),
                Timestamp("2023-01-06 00:00:00"),
                Timestamp("2023-01-07 00:00:00"),
                Timestamp("2023-01-08 00:00:00"),
                Timestamp("2023-01-09 00:00:00"),
                Timestamp("2023-01-10 00:00:00"),
            ],
            "processed_quantity": [10, 20, 15, 0, 5, 0, 25, 30, 0, 5],
            "quantity_cumsum": [10, 30, 45, 45, 50, 50, 75, 105, 105, 110],
        }
    )

    assert preprocessed_df.equals(expected_output)


def test_only_one_data_point(sample_icpe_data):
    data = sample_icpe_data.head(1)

    processor = ICPEAnnualItemProcessor(icpe_item_daily_data=data)
    processor._preprocess_data()

    preprocessed_df = processor.preprocessed_df

    expected_output = pd.DataFrame(
        {
            "day_of_processing": [
                Timestamp("2023-01-01 00:00:00"),
            ],
            "processed_quantity": [
                10,
            ],
            "quantity_cumsum": [
                10,
            ],
        }
    )

    assert preprocessed_df.equals(expected_output)


def test_empty_icpe_data():
    processor = ICPEAnnualItemProcessor(icpe_item_daily_data=pd.DataFrame())

    processor._preprocess_data()

    assert processor._check_data_empty(), "Data should be considered empty when input DataFrame is empty."

    processor = ICPEAnnualItemProcessor(icpe_item_daily_data=None)

    processor._preprocess_data()

    assert processor._check_data_empty(), "Data should be considered empty when input DataFrame is None."


def test_correct_figure_creation(sample_icpe_data):
    processor = ICPEAnnualItemProcessor(icpe_item_daily_data=sample_icpe_data)

    processor._preprocess_data()
    processor._create_figure()

    figure = processor.figure

    assert isinstance(figure, go.Figure), "The generated figure should be a Plotly Figure object."
    assert len(figure.data) > 0, "Figure should contain at least one trace."


def test_process_build(sample_icpe_data):
    processor = ICPEAnnualItemProcessor(icpe_item_daily_data=sample_icpe_data)

    result = processor.build()

    assert isinstance(result, str), "Build method should return a JSON string representation of the figure."
    assert len(result) > 0, "Build result should not be empty."


def test_missing_columns():
    data = {"day_of_processing": [datetime(2023, 1, 1)], "processed_quantity": [10]}

    icpe_data_df = pd.DataFrame(data)

    processor = ICPEAnnualItemProcessor(icpe_item_daily_data=icpe_data_df)

    # Should raise a KeyError
    with pytest.raises(KeyError):
        processor._preprocess_data()


def test_incorrect_data_format():
    data = {
        "day_of_processing": ["Not a datetime"],  # Incorrect date format
        "processed_quantity": [10],
        "authorized_quantity": [50],
    }

    icpe_data_df = pd.DataFrame(data)

    processor = ICPEAnnualItemProcessor(icpe_item_daily_data=icpe_data_df)

    # Should raise a TypeError due to type column not being Timestamp
    with pytest.raises(TypeError):
        processor._preprocess_data()


def test_zero_processed_quantities():
    data = {
        "day_of_processing": [datetime(2023, 1, 1), datetime(2023, 1, 2), datetime(2023, 1, 3)],
        "processed_quantity": [0, 0, 0],
        "authorized_quantity": [50, 50, 50],
    }

    icpe_data_df = pd.DataFrame(data)

    processor = ICPEAnnualItemProcessor(icpe_item_daily_data=icpe_data_df)

    processor._preprocess_data()

    assert (
        processor._check_data_empty()
    ), "Data should be considered empty when all rows have zero processed quantities."


def test_only_nan_processed_quantities():
    data = {
        "day_of_processing": [datetime(2023, 1, 1), datetime(2023, 1, 2), datetime(2023, 1, 3)],
        "processed_quantity": [float("nan"), float("nan"), float("nan")],
        "authorized_quantity": [50, 50, 50],
    }

    icpe_data_df = pd.DataFrame(data)

    processor = ICPEAnnualItemProcessor(icpe_item_daily_data=icpe_data_df)

    processor._preprocess_data()

    assert processor._check_data_empty(), "Data should be considered empty when all processed quantities are NaN."
