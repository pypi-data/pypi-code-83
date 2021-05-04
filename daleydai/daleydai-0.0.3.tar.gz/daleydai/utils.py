import os
import sys
import json
import pandas as pd

from daleydai import console

from daleydai.constants import CONFIG_DIR, CONFIG_FILE, STOCKS_LIST_FILE


def create_required_files():
    console.print("[blue]Creating config files")
    if not os.path.exists(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)

    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w+"):
            pass

    if not os.path.exists(STOCKS_LIST_FILE):
        with open(STOCKS_LIST_FILE, "w+"):
            pass


def add_mero_shares(stock: str):
    with open(CONFIG_FILE, "r+") as file:
        data = file.readline()

        if not data:
            listData = [stock]
            json.dump(listData, file)
            sys.exit()

        shareList = json.loads(data)

        if stock not in shareList:
            shareList.append(stock)

        file.seek(0)
        json.dump(shareList, file)


def remove_mero_shares(stock: str):
    with open(CONFIG_FILE, "r+") as file:
        data = file.readline()

        if not data:
            sys.exit()

        data_dict = json.loads(data)
        if stock not in data_dict:
            sys.exit()

        data_dict.remove(stock)

        file.seek(0)
        json.dump(data_dict, file)
        file.truncate()
