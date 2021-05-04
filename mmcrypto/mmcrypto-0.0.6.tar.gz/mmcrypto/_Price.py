import os
from pathlib import Path
import csv


class Price(float):
    attrs = [
        "time",
        "price",
        "low",
        "high",
        "open_",
        "vol",
        "sell",
        "buy",
    ]

    def __new__(self, value, **kwargs):
        return float.__new__(self, value)

    def __init__(
        self,
        value,
        time=None,
        low=None,
        high=None,
        open_=None,
        vol=None,
        sell=None,
        buy=None,
    ):
        self.low = low
        self.high = high
        self.open_ = open_
        self.vol = vol
        self.sell = sell
        self.buy = buy
        self.time = time
        float.__init__(value)

    def __getitem__(self, name):
        if str(name) == "price":
            return self
        if str(name).strip() == "0":
            raise StopIteration
        return eval(f"self.{name}")

    def __setitem__(self, name, value):
        value = float(value)
        return exec(f"self.{name} = {value}")

    def __setattr__(self, name, value):
        if value is not None:
            try:
                value = int(value)
            except ValueError:
                value = float(value)
        return super().__setattr__(name, value)

    def todict(self):
        d = vars(self)
        d["price"] = self
        return d

    def save(self, filename):
        self._validate()
        dir_ = os.path.join(*os.path.split(filename)[:-1])
        if not os.path.exists(dir_):
            raise NotADirectoryError(f"{dir_} not found")
        Path(filename).touch()
        with open(filename, "a") as file_:
            writer = csv.writer(file_)
            row = [self[attr] for attr in self.attrs]
            writer.writerow(row)

    def _validate(self):
        for attr in self.attrs:
            if self[attr] is None:
                raise AttributeError(f"{attr} not assigned in Price")

    @classmethod
    def from_list(cls, list_):
        price = Price(
            value=list_[1],
        )
        for attr, value in zip(cls.attrs, list_):
            price[attr] = value
        return price
