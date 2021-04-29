import requests

from .auth import CoinbaseAuth
from .models.user import User
from .models.wallet import Wallet


class PortfolioMgmt:

    def __init__(self, url: str, auth: CoinbaseAuth):
        self.url = url
        self.auth = auth
        self.account_list = self._set_accounts()
        # self.payment_methods = self._set_payment_methods()

    @property
    def current_user(self):
        resp = requests.get(f"{self.url}user", auth=self.auth).json()
        return User(**resp["data"])

    def _set_accounts(self):
        resp = requests.get(f"{self.url}accounts", auth=self.auth).json()
        return [Wallet(**data_row) for data_row in resp['data']]

    def _set_payment_methods(self):
        resp = requests.get(f"{self.url}payment-methods",
                            auth=self.auth).json()
        return [Wallet(**data_row) for data_row in resp['data']]

    def wallet(self, symbol: str):
        for wal in self.account_list:
            if wal.balance.currency == symbol:
                return wal

    def price(self, symbol: str, mode: str = "sell", currency: str = "EUR"):
        resp = requests.get(
            f"{self.url}prices/{symbol}-{currency}/{mode}", auth=self.auth).json()
        return resp["data"]["amount"]

    def sell(self, wallet: Wallet, amountInEuro: float):
        pass

    def buy(self, wallet: Wallet, amountInEuro: float):
        pass

    def sellMaxAmount(self, wallet: Wallet):
        pass

    def swap(self, src: Wallet, dst: Wallet):
        pass

    def txs(self):
        pass
