import json
import requests
from os import path

class ApiClient:
    headers = None
    api_host = None
    api_base = None
    logger = None

    def __init__(self, logger, host, base):
        self.logger = logger
        self.api_host = host
        self.api_base = base

    def _request(self, method, *endpoints, **kwargs):
        kwargs['headers'] = self.headers
        if not endpoints[0].startswith(self.api_base):
            endpoints = [self.api_base, *endpoints]
        url = path.join(self.api_host, *[str(s).strip("/") for s in endpoints])
        response = requests.request(method, url, **kwargs)
        if (response.status_code > 299):
            self.logger.error(
                f"Status code: {response.status_code}, Content: {response.text}"
            )
            response.raise_for_status()
        if response.status_code == 204:
            return {}
        return json.loads(response.text)
    
    def get(self, *segments, **kwargs):
        return self._request("get", *segments, **kwargs)

    def post(self, *segments, **kwargs):
        return self._request("post", *segments, **kwargs)

    def put(self, *segments, **kwargs):
        return self._request("put", *segments, **kwargs)

    def delete(self, *segments, **kwargs):
        return self._request("delete", *segments, **kwargs)
