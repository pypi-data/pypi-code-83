import hashlib
import hmac
import time

from requests.auth import AuthBase


class CoinbaseAuth(AuthBase):
    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key

    def __call__(self, request):
        timestamp = str(int(time.time()))
        message = timestamp + request.method + \
            request.path_url + (request.body or '')
        signature = hmac.new(self.secret_key.encode('utf-8'), message.encode('utf-8'),
                             hashlib.sha256).hexdigest()

        request.headers.update({
            'CB-ACCESS-SIGN': signature,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.api_key,
        })
        return request
