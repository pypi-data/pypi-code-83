import requests
from urllib.parse import urlencode


class HttpResponse(object):
    def __init__(self,
                 url: str,
                 method: str,
                 headers: dict,
                 timeout=None,
                 body=None):
        self.url = url
        self.method = method
        self.headers = headers
        self.body = body
        self.timeout = 5 if timeout is None else timeout

    def get_response_object(self):
        print('the requests url: {}'.format(self.url))
        print('the requests method: {}'.format(self.method))
        print('the requests body: {}'.format(self.body))
        print('the requests headers: {}'.format(self.headers))
        if self.method == "GET":
            response = requests.get(self.url, headers=self.headers, timeout=self.timeout)

        elif self.method == 'POST':
            if self.headers['Content-Type'] == 'application/x-www-form-urlencoded':
                data =urlencode(self.body)
                response = requests.post(self.url, data=data, headers=self.headers, timeout=self.timeout)

            else:
                response = requests.post(self.url, data=self.body, headers=self.headers, timeout=self.timeout)

        else:
            raise Exception(f'Not support the request method {self.method}')
        return response
