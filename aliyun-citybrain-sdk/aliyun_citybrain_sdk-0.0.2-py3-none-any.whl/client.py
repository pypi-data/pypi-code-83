from .http_model import http_response


class Client(object):
    def __init__(self,
                 ak: str,
                 sk: str,
                 timeout=None):
        """
        :param ak: 天翼云AccessKey
        :param sk: 天翼云SecretKey
        :param timeout: 每个请求超时时间。
        """
        self._ak = ak
        self._sk = sk

    def do_action(self, _request):
        response = self._implementation_of_do_action(_request)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'request get error,the request code {response.status_code} the response: {repr(response.text)}')

    def _implementation_of_do_action(self, _request):
        _response = self._make_http_response(_request)
        response = _response.get_response_object()
        return response

    def _make_http_response(self, _request):
        headers = _request.handle_headers(ak=self._ak, sk=self._sk)
        timeout = _request.get_timeout()
        protocol = _request.get_protocol()
        domain = _request.get_domain()
        call_url = protocol + "://" + domain + _request.get_url()
        method = _request.get_method()
        body = _request.get_body()
        _response = http_response.HttpResponse(url=call_url, method=method, headers=headers, body=body, timeout=timeout)
        return _response
