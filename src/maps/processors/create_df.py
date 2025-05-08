import os
import shutil

from ..data.datasets import get_data_df


def build_dataframes():
    # store dataframes as parquet in temp files
    root = r"temp_data"  # unversionned dir
    try:
        shutil.rmtree(root)
    except FileNotFoundError:
        pass
    os.mkdir(root)

    data = get_data_df()

    for dataset_name in [
        "icpe_installations_data",
        "icpe_installations_waste_processed_data",
        "icpe_departements_waste_processed_data",
        "icpe_regions_waste_processed_data",
        "icpe_france_waste_processed_data",
    ]:
        getattr(data, dataset_name).write_parquet(f"temp_data/{dataset_name}.parquet")
