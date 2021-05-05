import logging
from urllib.parse import urljoin
from . import utils
from . import endpoints
import datetime
import time
import json
import hmac
import base64
import hashlib

logger = logging.getLogger(__name__)


class Order():
    def __init__(self, symbol, side, amount, price):
        self.symbol = symbol
        self.side = side
        self.amount = amount
        self.price = price


class Header():
    def __init__(self, endpoint, order, key, secret):
        self.endpoint = endpoint
        self.order = order
        self.key = key
        self.secret = secret

    def get_headers(self):
        self.payload = self._build_payload()

        self.encoded_payload = self._encode_payload()

        self.signature = self._create_signature()

        self.headers = self._build_headers()

        return self.headers

    def _create_nonce(self):
        t = datetime.datetime.now()
        nonce = str(int(time.mktime(t.timetuple())*1000))
        return nonce

    def _encode_payload(self):
        encoded = json.dumps(self.payload).encode()
        b64 = base64.b64encode(encoded)
        return b64

    def _create_signature(self):
        signature = hmac.new(self.secret, self.encoded_payload,
                             hashlib.sha384).hexdigest()
        return signature

    def _build_payload(self):
        return {
            'request': self.endpoint,
            'nonce': self._create_nonce(),
            'symbol': self.order.symbol,
            'amount': self.order.amount,
            'price': self.order.price,
            'side': self.order.side,
            'type': 'exchange limit',
            'options': ['immediate-or-cancel']
        }

    def _build_headers(self):
        return {
            'Content-Type': 'text/plain',
            'Content-Length': '0',
            'X-GEMINI-APIKEY': self.key,
            'X-GEMINI-PAYLOAD': self.encoded_payload,
            'X-GEMINI-SIGNATURE': self.signature,
            'Cache-Control': 'no-cache'
        }


class Gem():
    symbols = None

    def __init__(self, base_url, key, secret):

        self.base_url = base_url
        self.key = key
        self.secret = secret.encode()

    def get_supported_symbols(self):
        '''
        Make a call to the `/v1/symbols` endpoint and return a list of
        accepted symbols.
        '''
        if self.symbols is None:
            url = urljoin(self.base_url, endpoints.SYMBOLS)
            response = utils.make_get_request(url)
            self.symbols = response.json()

        return self.symbols

    def _sanitise_and_validate_symbol(self, symbol):
        symbol = str(symbol).lower()
        symbols = self.get_supported_symbols()
        if symbol not in symbols:
            raise ValueError(
                'Incorrect value of argument `symbol`. '
                f'Expected one of {symbols}')
        return symbol

    def get_ticker_price(self, symbol, price_type='ask'):
        '''
        Make a call to the `/v1/pubticker/` endpoint and return the value
        defined by `price_type` - defaults to 'ask', the asking price.
        '''

        price_types = ('bid', 'ask', 'last')
        if price_type not in price_types:
            raise ValueError('Incorrect value of argument `price_type`. '
                             f'Expected one of {price_types}')

        symbol = self._sanitise_and_validate_symbol(symbol)

        base_url = urljoin(self.base_url, endpoints.TICKER)
        url = urljoin(base_url, symbol)

        response = utils.make_get_request(url)
        data = response.json()
        return float(data[price_type])

    def convert_cost_to_asset_amount(self, symbol, cost, rounded=8):
        '''
        Divides `cost` by the current ticker price given by `symbol` rounding
        to `rounded` decimal places, and returns the resulting asset amount.
        E.g. if `symbol` is 'btcusd', `cost` is 50 (USD) and the current
        ticker price is 60000 (USD), the result would be
        50 / 60000 = 0.00083333 (BTC)
        '''
        ticker_price = self.get_ticker_price(symbol)
        asset_amount = round(cost / ticker_price, rounded)
        return asset_amount

    def _place_order(self, symbol, side, amount, price):
        symbol = self._sanitise_and_validate_symbol(symbol)

        if(amount <= 0):
            raise ValueError('Incorrect value of argument `amount`. '
                             f'Expected a positive value.')

        if(price <= 0):
            raise ValueError('Incorrect value of argument `price`. '
                             f'Expected a positive value.')

        self.order = Order(symbol, side, amount, price)

        endpoint = endpoints.PLACE_ORDER

        url = urljoin(self.base_url, endpoint)

        self.headers = Header(endpoint, self.order,
                              self.key, self.secret).get_headers()

        self.response = utils.make_post_request(url, self.headers)

        return self.response.json()

    def place_amount_buy_order(self, symbol, amount, price):
        '''
        Make a call to the `/v1/order/new` endpoint, placing a buy order for
        `amount` with a limit of `price`, and returns the API response. If you
        pass `symbol` 'BTCUSD', `amount` would be the quantity of BTC you want
        to buy, while `price` would be the max USD market price you're willing
        to pay.
        E.g. `amount` = 0.1 and `price` = 10000 would cause 0.1 BTC to be
        bought if the price of BTC is less than or equal to 10000 USD.
        '''

        return self._place_order(symbol, 'buy', amount, price)

    def place_cost_buy_order(self, symbol, cost, price):
        '''
        Similar to `place_asset_buy_order` but calculates the amount of the
        asset to buy based on the `cost` passed. Returns the API response.
        E.g. Passing `symbol` 'BTCUSD' and a `cost` value of 10 would cause
        the order of 10 USD worth of BTC to be bought.
        '''

        asset_price = self.convert_cost_to_asset_amount(
            symbol, cost)
        return self.place_amount_buy_order(symbol,
                                           asset_price,
                                           price)
