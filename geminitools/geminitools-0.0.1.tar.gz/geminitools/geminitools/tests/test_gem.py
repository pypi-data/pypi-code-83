from geminitools import Gem, utils
import unittest
from unittest.mock import Mock, patch, MagicMock
import requests
import json
from urllib.parse import urljoin
import datetime
import time
import hmac
import base64
import hashlib

responses = {
    'ticker': '''{
                    "ask": "977.59",
                    "bid": "977.35",
                    "last": "977.65",
                    "volume": {
                        "BTC": "2210.505328803",
                        "USD": "2135477.463379586263",
                        "timestamp": 1483018200000
                    }
                }''',
    'symbols': '''[
                "btcusd", "ethbtc", "ethusd", "zecusd", "zecbtc",
                "zeceth", "zecbch", "zecltc", "bchusd", "bchbtc", "bcheth",
                "ltcusd", "ltcbtc", "ltceth", "ltcbch", "batusd", "daiusd",
                "linkusd", "oxtusd", "batbtc", "linkbtc", "oxtbtc", "bateth",
                "linketh", "oxteth", "ampusd", "compusd", "paxgusd", "mkrusd",
                "zrxusd", "kncusd", "manausd", "storjusd", "snxusd", "crvusd",
                "balusd", "uniusd", "renusd", "umausd", "yfiusd", "btcdai",
                "ethdai", "aaveusd", "filusd", "btceur", "btcgbp", "etheur",
                "ethgbp", "btcsgd", "ethsgd", "sklusd", "grtusd", "bntusd",
                "1inchusd", "enjusd", "lrcusd", "sandusd", "cubeusd",
                "lptusd", "bondusd", "maticusd", "injusd", "sushiusd"]''',
    'order': '''{
                "order_id": "106817811",
                "id": "106817811",
                "symbol": "btcusd",
                "exchange": "gemini",
                "avg_execution_price": "3632.8508430064554",
                "side": "buy",
                "type": "exchange limit",
                "timestamp": "1547220404",
                "timestampms": 1547220404836,
                "is_live": true,
                "is_cancelled": false,
                "is_hidden": false,
                "was_forced": false,
                "executed_amount": "3.7567928949",
                "remaining_amount": "1.2432071051",
                "client_order_id": "20190110-4738721",
                "options": [],
                "price": "3633.00",
                "original_amount": "5"
            }'''
}


class FakeResponse:

    def __init__(self, restype=None):
        self.res_type = restype

    def text(self):
        if self.res_type in responses.keys():
            return responses[self.res_type]
        else:
            return '[]'

    def json(self):
        return json.loads(self.text())

    def raise_for_status(self):
        pass


class GemTester(unittest.TestCase):

    base_url = 'http://fakeurl'
    key = 'fake_key'
    secret = 'fake_secret'
    fake_response = None

    def setUp(self):
        self.fake_req = requests.get = requests.post = Mock()

        self.gem = Gem(
            self.base_url,
            self.key,
            self.secret
        )

    def set_response_side_effects(self, *args):
        self.fake_req.side_effect = [FakeResponse(typ) for typ in args]

    def create_fake_headers(self, endpoint, symbol, amount, price, side):
        t = datetime.datetime.now()
        time_tuple = t.timetuple()
        datetime.datetime = MagicMock()
        datetime.datetime.now.side_effect = lambda: t
        datetime.datetime.timetuple.side_effect = lambda: time_tuple

        t = datetime.datetime.now()
        payload_nonce = str(int(time.mktime(t.timetuple())*1000))

        payload = {
            'request': endpoint,
            'nonce': payload_nonce,
            'symbol': symbol,
            'amount': amount,
            'price': price,
            'side': side,
            'type': 'exchange limit',
            'options': ['immediate-or-cancel']
        }

        encoded_payload = json.dumps(payload).encode()
        b64 = base64.b64encode(encoded_payload)
        signature = hmac.new(self.secret.encode(), b64,
                             hashlib.sha384).hexdigest()

        headers = {
            'Content-Type': 'text/plain',
            'Content-Length': '0',
            'X-GEMINI-APIKEY': self.key,
            'X-GEMINI-PAYLOAD': b64,
            'X-GEMINI-SIGNATURE': signature,
            'Cache-Control': 'no-cache'
        }
        return headers

    def test__get_supported_symbols(self):
        self.set_response_side_effects('symbols')

        actual = self.gem.get_supported_symbols()
        self.assertIn('btcusd', actual)

        called_with = urljoin(self.base_url, 'v1/symbols')
        self.fake_req.assert_called_once_with(called_with)

    def test__get_supported_symbols__requested_once(self):
        '''
        Gem should save the symbols response somehow.
        We don't want it spamming the server
        since it needs to check symbols a lot!
        '''
        self.set_response_side_effects('symbols')
        self.gem.get_supported_symbols()
        self.gem.get_supported_symbols()
        # Gem should save the response somehow.
        # We don't want it spamming the server
        # since it needs to check symbols a lot!
        self.fake_req.assert_called_once()

    def test__get_ticker_price(self):
        self.set_response_side_effects('symbols', 'ticker')

        ticker = 'btcusd'
        actual = self.gem.get_ticker_price(ticker)
        expected = 977.59
        self.assertEqual(actual, expected)

        base = urljoin(self.base_url, '/v1/pubticker/')
        called_with = urljoin(base, ticker)
        self.fake_req.assert_called_with(called_with)

    def test__get_ticker_price__uppercase(self):
        self.set_response_side_effects('symbols', 'ticker')

        ticker = 'ETHBTC'
        self.gem.get_ticker_price(ticker)

    def test__get_ticker_price__bad_args(self):
        self.set_response_side_effects('symbols', 'ticker')

        with self.assertRaises(ValueError):
            self.gem.get_ticker_price('btcusd', 'bad')
        with self.assertRaises(ValueError):
            self.gem.get_ticker_price('hello')

        self.fake_req.assert_called_once()

    def test__convert_cost_to_asset_amount(self):
        self.set_response_side_effects('symbols', 'ticker')
        cost = 50
        price = 977.59
        actual = self.gem.convert_cost_to_asset_amount('btcusd', cost)
        expected = round(cost / price, 8)
        self.assertEqual(actual, expected)

    def test__place_amount_buy_order(self):
        endpoint = '/v1/order/new'
        symbol = 'btcusd'
        amount = 1
        price = 1000
        headers = self.create_fake_headers(
            endpoint, symbol, amount, price, 'buy')

        self.set_response_side_effects('symbols', 'order')
        res = self.gem.place_amount_buy_order(symbol, amount, price)
        self.assertEqual(res, json.loads(responses['order']))

        url = urljoin(self.base_url, endpoint)

        self.fake_req.assert_called_with(url, data=None, headers=headers)

    def test__place_amount_buy_order__bad_args(self):
        self.set_response_side_effects('symbols', 'order')
        with self.assertRaises(ValueError):
            self.gem.place_amount_buy_order('bad!', 1, 1000)
        with self.assertRaises(ValueError):
            self.gem.place_amount_buy_order('btcusd', -1, 1000)
        with self.assertRaises(ValueError):
            self.gem.place_amount_buy_order('btcusd', 0.1, -1)

        self.fake_req.assert_called_once()

    def test__place_cost_buy_order(self):
        endpoint = '/v1/order/new'
        symbol = 'btcusd'
        cost = 10
        price = 10000

        amount = round(cost / 977.59, 8)
        headers = self.create_fake_headers(
            endpoint, symbol, amount, price, 'buy')

        self.set_response_side_effects('symbols', 'ticker', 'order')
        res = self.gem.place_cost_buy_order(symbol, cost, price)
        self.assertEqual(res, json.loads(responses['order']))

        url = urljoin(self.base_url, endpoint)

        self.fake_req.assert_called_with(url, data=None, headers=headers)


if __name__ == '__main__':
    unittest.main()
