import os
import shutil
import pandas as pd
import random
import toml
from typing import Optional, List
from pathlib import Path
import zipfile


def path_to_bytes(path: str) -> bytes:
    data = open(path, "rb")
    return data.read()


def dict_to_bytes(config: dict) -> bytes:
    json_string = toml.dumps(config)
    return json_string.encode()


def dataframe_to_zip(df_input: List[pd.DataFrame],
                     df_output: List[pd.DataFrame],
                     path_to_save: str,
                     name: Optional[str] = None
                     ) -> str:
    """
    Create respective directories INPUT, OUTPUT, . csv files, and zip them.

    :param df_input: list of dataframes containing the input data
    :param df_output: list of dataframes containing the output data
    :param path_to_save: path to directory where zip should be created
    :param name: name of the zipped dataset- if none automatically generate name,
                 if name does not end on .zip, the extension is automatically added
    :return: name of the zipped dataset
    :raise ValueError: not the same amount of input and output files
    """
    if len(df_input) != len(df_output):
        raise ValueError("Input and output need to be the same size.")
    if name is None:
        name = f"{random.randint(10000, 1000000)}.zip"
    if name[-4:] != ".zip":
        name += ".zip"

    path_to_save = Path(path_to_save)

    input_path = path_to_save / "INPUT"
    output_path = path_to_save / "OUTPUT"
    input_path.mkdir()
    output_path.mkdir()

    for i, df in enumerate(df_input):
        df.to_csv(input_path / f"INPUT_{i}.csv")
    for i, df in enumerate(df_output):
        df.to_csv(output_path / f"OUTPUT_{i}.csv")

    zip_file = zipfile.ZipFile(path_to_save / name, 'w')
    folders = [input_path, output_path]

    for folder in folders:
        for dirpath, dirnames, filenames in os.walk(folder):
            for filename in filenames:
                zip_file.write(
                    os.path.join(dirpath, filename),
                    os.path.relpath(os.path.join(dirpath, filename), os.path.join(folders[0], '..')))

    zip_file.close()
    shutil.rmtree(input_path)
    shutil.rmtree(output_path)
    return name
