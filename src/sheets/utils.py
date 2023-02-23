import re

import numpy as np
import pandas as pd


def get_code_departement(postal_code: str) -> str:
    """Take a postal code and returns the département code."""
    if pd.isna(postal_code):
        return np.nan
    if 20000 <= int(postal_code) < 21000:
        if int(postal_code) <= 20190:
            return "2A"
        else:
            return "2B"
    if int(postal_code) > 97000:
        return postal_code[:3]

    return postal_code[:2]


def format_number_str(input_number: float, precision: int = 2) -> str:
    """Format a float to a string with thousands separated by space and rounding it at the given precision."""
    input_number = round(input_number, precision)
    if not input_number:
        return "0"
    return re.sub(r"\.0$", "", "{:,}".format(input_number).replace(",", " "))
