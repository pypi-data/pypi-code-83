"""Util functions."""

import http.client
import json
import urllib
from typing import Any, AnyStr, Dict

from .errors import RequestError


def send_request(
    method: AnyStr,
    url: AnyStr,
    body: Dict[AnyStr, Any] = None,
    params: Dict[AnyStr, Any] = None,
    headers: Dict[AnyStr, Any] = None,
) -> AnyStr:
    """Send REST request from configuration.

    :param method: Request method (GET, POST, PUT, DELETE)
    :param url: Resource url to execute request
    :param body: Request body
    :param params: Query params for url
    :param headers: Request headers
    :return Dict: Response payload
    """

    parsed_url = urllib.parse.urlparse(url)

    client = _build_client(parsed_url)
    headers = _check_headers(headers)
    payload = _build_payload(headers['Content-Type'], body)
    path = _build_path(parsed_url, params)

    try:
        client.request(method, path, payload, headers)
    except Exception as error:
        raise RequestError(f'voices: error calling service {url}') from error

    response = client.getresponse()
    return response.read().decode('utf-8')


def _build_client(parsed_url):
    """Build http client according scheme.

    :param scheme: URL scheme
    :return: HTTP Client
    """

    if parsed_url.scheme == 'https':
        return http.client.HTTPSConnection(parsed_url.hostname, parsed_url.port)

    return http.client.HTTPConnection(parsed_url.hostname, parsed_url.port)


def _build_payload(content_type: AnyStr, body: Dict[AnyStr, Any]) -> AnyStr:
    """Build payload for the given Content Type.

    :param content_type: Body content type
    :param body: Request payload
    :return str: Build payload
    """

    if content_type == 'application/x-www-form-urlencoded':
        return urllib.parse.urlencode(body)

    return json.dumps(body)


def _check_headers(headers: Any) -> Dict:
    """Check headers format an validate content type.

    :param headers: configured headers
    :return Dict: request headers
    """

    if headers is None:
        headers = {}

    if 'Content-Type' not in headers.keys():
        headers['Content-Type'] = 'application/json'

    return headers


def _build_path(parsed_url, params: Dict[AnyStr, Any]) -> AnyStr:
    """Build final resource path from parsed URL.

    :param parsed_url: Configured URL
    :param params: Query params
    :return str: final url path
    """

    path = parsed_url.path

    if params is not None:
        params = urllib.parse.urlencode(params)
        path = f'{path}?{params}'

    return path
