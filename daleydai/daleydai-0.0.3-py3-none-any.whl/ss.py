import json
import pandas as pd

from daleydai.constants import STOCKS_LIST_FILE, CONFIG_FILE

pd.set_option("display.max.columns", None)
pd.set_option("display.max.rows", None)
pd.set_option("display.precision", 10)


def main():

    # read meroshares file
    meroshareData = json.load(open(CONFIG_FILE))

    # read stocks price file
    data = json.load(open(STOCKS_LIST_FILE))
    df = pd.DataFrame(data["content"])

    filteredDf = df[df.symbol.isin(meroshareData)]
    print(
        filteredDf[
            [
                "symbol",
                "openPrice",
                "highPrice",
                "lowPrice",
                "closePrice",
                "businessDate",
            ]
        ]
    )


main()
