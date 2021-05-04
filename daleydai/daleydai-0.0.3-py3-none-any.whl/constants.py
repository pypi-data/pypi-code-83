from pathlib import Path

"""
URLs
"""
STOCK_LIST_URL = "https://newweb.nepalstock.com/api/nots/company/list"
TODAY_PRICE_URL = (
    "https://newweb.nepalstock.com/api/nots/nepse-data/today-price?&size=500"
)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
}

CONFIG_DIR = f"{Path.home()}/.daleydai"
CONFIG_FILE = f"{CONFIG_DIR}/meroshares.json"
STOCKS_LIST_FILE = f"{CONFIG_DIR}/stocks.json"
