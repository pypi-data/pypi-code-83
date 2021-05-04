import json
import requests
import pandas as pd

from daleydai.constants import headers, TODAY_PRICE_URL, CONFIG_FILE, STOCKS_LIST_FILE


pd.set_option("display.max.columns", None)
pd.set_option("display.max.rows", None)
pd.set_option("display.precision", 10)


def request_api(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(response)
        raise Exception("Bad Request !!")


def fetch_stocks_and_dump_to_file():
    jsonResponse = request_api(TODAY_PRICE_URL)
    with open(STOCKS_LIST_FILE, "w+") as file:
        file.truncate()
        json.dump(jsonResponse, file)
        pass


def fetch_broker_data(BROKER_ID, isBuy):

    buyOrSell = "buyerBroker" if isBuy else "sellerBroker"
    MAIN_URL = f"https://newweb.nepalstock.com/api/nots/nepse-data/floorsheet?&size=500&{buyOrSell}={BROKER_ID}&sort=contractId,desc"

    dataFrames = pd.DataFrame()
    jsonResponse = request_api(MAIN_URL)
    summaryData = pd.json_normalize(jsonResponse["floorsheets"])
    totalPages = summaryData["totalPages"].values[0]
    nextPage = 0
    while nextPage <= totalPages:
        print(f"Fetching page {nextPage + 1}")
        PAGED_URL = f"https://newweb.nepalstock.com/api/nots/nepse-data/floorsheet?page={nextPage}&size=500&{buyOrSell}={BROKER_ID}&sort=contractId,desc"
        pagedResponse = request_api(PAGED_URL)
        pagedDf = pd.json_normalize(pagedResponse["floorsheets"]["content"])
        dataFrames = pd.concat([pagedDf, dataFrames], sort=False)
        nextPage += 1

    unsortedDf = dataFrames.groupby("stockSymbol").agg(
        totalKittas=pd.NamedAgg(column="contractQuantity", aggfunc="sum"),
        totalAmount=pd.NamedAgg(column="contractAmount", aggfunc="sum"),
        totalTransactions=pd.NamedAgg(column="stockSymbol", aggfunc="count"),
        maxPrice=pd.NamedAgg(column="contractRate", aggfunc="max"),
        minPrice=pd.NamedAgg(column="contractRate", aggfunc="min"),
    )

    sortedDf = unsortedDf.sort_values("totalKittas", ascending=False)
    print(sortedDf)


def read_stocks_from_file():
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
