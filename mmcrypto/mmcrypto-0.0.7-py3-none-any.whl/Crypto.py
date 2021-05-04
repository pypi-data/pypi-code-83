import os
from pathlib import Path
import requests
import csv
from ._Price import Price


class Crypto:
    SYMBOLS = set()

    def __init__(self, symbol: str, data_directory: str):
        if not isinstance(symbol, str):
            raise TypeError("symbol must be a string")
        if not isinstance(data_directory, str):
            raise TypeError("data_directory must be a string")

        self.symbol = symbol
        self.data_directory = data_directory

    def add_price(self, price):
        price.save(self.filename)

    def get_prices(self):
        with open(self.filename) as file_:
            reader = csv.reader(file_)
            for row in reader:
                yield Price.from_list(row)
        # return [Price(20)]

    @property
    def filename(self):
        return os.path.join(self.data_directory, f"{self.symbol}.csv")

    @classmethod
    def all(cls, data_directory: str):
        return [cls(symbol, data_directory) for symbol in cls.SYMBOLS]

    @classmethod
    def update(cls, data_directory: str):
        if not os.path.exists(data_directory):
            os.makedirs(data_directory)
        data = cls._get_data_from_api()
        prices = cls._parse_data_from_api(data)
        for sym, price in prices.items():
            cls.SYMBOLS.add(sym)
            filename = os.path.join(data_directory, f"{sym}.csv")
            Path(filename).touch()
            price.save(filename)

    @classmethod
    def _get_data_from_api(cls):
        res = requests.get("https://api.wazirx.com/api/v2/tickers")
        return res.json()

    @classmethod
    def _parse_data_from_api(cls, data: dict):
        result = {}
        for key, value in data.items():
            key = str(key)
            if key.endswith("inr"):
                sym = value["base_unit"]
                result[sym] = Price(
                    vol=value["volume"],
                    value=value["last"],
                    buy=value["buy"],
                    low=value["low"],
                    high=value["high"],
                    sell=value["sell"],
                    open_=value["open"],
                    time=value["at"],
                )
        return result

    def __str__(self):
        return {self.symbol}

    def __repr__(self):
        return f"Crypto: {self.symbol}"
