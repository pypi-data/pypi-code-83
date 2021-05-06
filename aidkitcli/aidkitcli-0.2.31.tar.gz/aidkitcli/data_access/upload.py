"""Upload and list stored models and data sets."""
import base64
import hashlib
import pandas as pd
import os

from typing import List, Union

from aidkitcli.data_access.api import RESTApi
from aidkitcli.data_access.utils import path_to_bytes, dataframe_to_zip

NUMBER_OF_CHARS_FOR_HASH = 8


def _get_hash(binary_content: bytes) -> str:
    m = hashlib.md5()
    m.update(binary_content)
    binary_hash = m.digest()
    return base64.b16encode(binary_hash).decode()[:NUMBER_OF_CHARS_FOR_HASH]


def upload_model(model_path: str, only_if_necessary: bool = True):
    """Upload a stored model to the server.

    Checks before whether the server has the model in question already
    stored, using md5 hashes.

    :param model_path: path to the model to be uploaded
    :param only_if_necessary: if true, the method checks whether the model
        already exists on the server and only uploads the model if
        necessary
    """
    file_content = path_to_bytes(model_path)
    hash = _get_hash(file_content)
    if only_if_necessary and hash in list_models():
        return [hash]
    api = RESTApi()
    return api.post_model(
        model_content=file_content,
        model_id=hash
    )


def list_models():
    """List all the uploaded models."""
    api = RESTApi()
    return api.list_models()


def upload_data(data_set: Union[str, List[List[pd.DataFrame]]],
                only_if_necessary: bool = True):
    """Upload a data set to the server. The data set is expected to be either
    a zip file or a pandas DataFrame.

    In both cases this function checks using md5 hashes whether the data set
    is already in the server and uploads it only if necessary.

    **- Upload a zip file**

    The zip file must contain two folders (INPUT and OUTPUT) with the
    corresponding CSV files inside.

    A data set can consist of multiple files but the number of files in the
    INPUT and OUTPUT subfolders must be the same. Moreover, the matching files
    must be named the same but with the word INPUT or OUTPUT at the beginning
    as appropriate (:ref:`example-structure-zip-file`).

    Regarding the structure of the CSV files, every row will represent a data
    point and every column a different variable.

    **- Upload a pandas DataFrame**

    The object you pass to the function must be a list where the first element
    is a list containing the DataFrames corresponding to the input features
    and the second element is a list containing the DataFrames corresponding
    to the output values. The i-th DataFrame in the input-list corresponds to
    the i-th DataFrame in the output-list (:ref:`example-structure-dataframe`).

    As before, every row of a DataFrame will represent a data point and every
    column a different variable.

    :param data_set: path to the zip file to be uploaded OR list of lists of
        dataframes
    :param only_if_necessary: whether to check if the data set already exists
        on the server and only upload it if necessary
    """
    generated_from_df = False
    if isinstance(data_set, list):
        generated_from_df = True
        data_set = dataframe_to_zip(data_set[0], data_set[1], ".")

    file_content = path_to_bytes(data_set)
    hash = _get_hash(file_content)
    if only_if_necessary and hash in list_data():
        return hash
    api = RESTApi()

    if generated_from_df:
        os.remove(data_set)

    return api.post_data(
        zip_content=file_content,
        data_id=hash,
    )


def list_data():
    """List all the uploaded data sets."""
    api = RESTApi()
    return api.list_data()
