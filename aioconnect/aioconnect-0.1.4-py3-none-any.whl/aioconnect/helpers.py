"""Extract nested values from a JSON tree."""
import requests
import json


def get_values(json_data: list, key: str = "_id") -> list:
    """Get the value for a key from a list of JSON objects.

    Parameters
    ----------
    json_data : list
        List of JSON objects.
    key : str, optional
        The key for which the value should be returned, by default "_id".

    Returns
    -------
    list
        List of the values.
    """

    if key == "":
        raise ValueError

    ret_list = []
    count = len(json_data)
    for i in range(0, count):
        x = json_data[i][key]
        ret_list.append(x)
    return ret_list
