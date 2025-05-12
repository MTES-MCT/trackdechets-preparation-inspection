"""
Utility functions used by data package.
"""

from datetime import datetime, timedelta


def get_data_date_interval_for_year(year: int = 2022) -> tuple[datetime, datetime]:
    """It returns a tuple of two datetime objects,
    the first one being the first day of the year, and the
    second one being the last day of the year

    Parameters
    ----------
    year : int, optional
        the year for which you want to get the data.

    Returns
    -------
        A tuple of two datetime objects.

    """
    now = datetime.now()

    date_interval = (
        datetime(year, 1, 1),
        datetime(year + 1, 1, 1),
    )
    date_start, date_end = date_interval

    if year == datetime.utcnow().year:
        max_date: datetime = now - timedelta(days=(now.toordinal() % 7) - 1)
        date_end = max_date.replace(hour=0, minute=0, second=0, microsecond=0)

    return date_start, date_end


def format_waste_codes(waste_code_list: list[dict], add_top_level: bool = False):
    """This function takes a list of dictionaries representing waste codes,
    and returns a list of dictionaries correctly formatted to be used in UI Tree selector.

    Parameters
    ----------
    waste_code_list : list[dict]
        list of dictionaries representing waste codes
    add_top_level : bool, optional
        if True, adds a top level option with title "Tous les code déchets"
        to the list of waste codes.

    Returns
    -------
        A list of dictionaries.

    """

    new_dict_list = []
    for waste_code_dict in waste_code_list:
        formatted_dict = {}
        formatted_dict["title"] = waste_code_dict["code"] + " - " + waste_code_dict["description"].capitalize()
        formatted_dict["value"] = waste_code_dict["code"]
        formatted_dict["key"] = waste_code_dict["code"]
        formatted_dict["children"] = format_waste_codes(waste_code_dict["children"])
        new_dict_list.append(formatted_dict)

    if add_top_level:
        new_dict_list = [
            {
                "title": "Tous les codes déchets",
                "value": "all",
                "key": "all",
                "children": new_dict_list,
            }
        ]
    return new_dict_list
