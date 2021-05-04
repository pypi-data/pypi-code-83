"""SDC2 scoring service API functions used by both user and admin methods."""
from http import HTTPStatus
import os
import logging
from typing import Optional
import urllib.parse

import keycloak
import requests

LOG = logging.getLogger("ska.sdc")

SDC_SCORE_API_URL = os.getenv("SDC_SCORE_API_URL", "https://sdcss.skatelescope.org/api/")
SDC_SCORE_AUTH_URL = os.getenv("SDC_SCORE_AUTH_URL", "https://sdcss.skatelescope.org/auth/")
SDC_SCORE_AUTH_CLIENT_ID = os.getenv("SDC_SCORE_AUTH_CLIENT_ID", "sdc")
SDC_SCORE_AUTH_REALM_NAME = os.getenv("SDC_SCORE_AUTH_REALM_NAME", "sdc")
SDC_SCORE_VERBOSE = bool(int(os.getenv("SDC2_SCORE_VERBOSE", "0")))


def get_token(username: str, password: str):
    """Get keycloak token."""
    LOG.debug(f"Auth url = {SDC_SCORE_AUTH_URL}")
    LOG.debug(f"Getting auth token... {username} - {password}")
    try:
        keycloak_openid = keycloak.KeycloakOpenID(
            SDC_SCORE_AUTH_URL + "/",
            client_id=SDC_SCORE_AUTH_CLIENT_ID,
            realm_name=SDC_SCORE_AUTH_REALM_NAME,
        )
        token = keycloak_openid.token(username=username, password=password)
        LOG.debug("Successfully obtained auth token.")
    except keycloak.exceptions.KeycloakAuthenticationError as err:
        LOG.error("Unable to get auth token. %s", err)
        raise err
    return token


def sdcss_get(
    endpoint: str,
    params: Optional[dict] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
) -> dict:
    """Send HTTP GET to the specified SDCSS endpoint.

    Args:
        endpoint(str): SDC scoring service endpoint.
        params(dict): Optional; Parameters to pass to the API.
        username(str): Optional; Username if authentication is needed.
        password(str): Optional; Password if authentication is needed.

    Returns:
        JSON object with returned by the SDCSS

    Raises:
        RuntimeError: If it is not possible to retrieve requested data.

    """
    _url = SDC_SCORE_API_URL + endpoint
    headers = {}
    if params:
        params = urllib.parse.urlencode(params)
        _url += "?" + params
    if username and password:
        auth_token = get_token(username, password)
        headers["Authorization"] = "Bearer " + auth_token["access_token"]
    LOG.debug("GET url=%s", _url)
    resp = requests.get(_url, headers=headers)
    data = resp.json()
    if resp.status_code != HTTPStatus.OK:
        raise RuntimeError(
            "GET {} failed with status {}. {}".format(endpoint, resp.status_code, data)
        )
    return data


def sdcss_auth_header(username: str, password: str):
    """."""
    token = get_token(username, password)
    return {
        "Authorization": "Bearer " + token["access_token"],
        "Content-Type": "multipart/form-data",
        "Accept": "application/json",
    }


def sdcss_post(
    endpoint: str,
    params: Optional[dict] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
) -> dict:
    """Send HTTP POST to the specified SDCSS endpoint.

    Args:
        endpoint(str): SDC scoring service endpoint.
        params(dict): Optional; Parameters to pass to the API.
        username(str): Optional; Username if authentication is needed.
        password(str): Optional; Password if authentication is needed.

    Returns:
        JSON object with returned by the SDCSS

    Raises:
        RuntimeError: If it is not successful.

    """
    if username and password:
        headers = sdcss_auth_header(username, password)
    else:
        headers = dict()
    _url = SDC_SCORE_API_URL + endpoint
    if params:
        params = urllib.parse.urlencode(params)
        _url += "?" + params
    LOG.debug("POST url=%s", _url)
    resp = requests.post(_url, headers=headers)
    data = resp.json()
    if resp.status_code != HTTPStatus.OK:
        raise RuntimeError(
            "POST {} failed with status {}. {}".format(endpoint, resp.status_code, data)
        )
    return resp


def sdcss_delete(
    endpoint: str,
    params: Optional[dict] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
) -> dict:
    """Send HTTP DELETE to the specified SDCSS endpoint.

    Args:
        endpoint(str): SDC scoring service endpoint.
        params(dict): Optional; Parameters to pass to the API.
        username(str): Optional; Username if authentication is needed.
        password(str): Optional; Password if authentication is needed.

    Returns:
        JSON object with returned by the SDCSS

    Raises:
        RuntimeError: If it is not successful.

    """
    if username and password:
        headers = sdcss_auth_header(username, password)
    else:
        headers = dict()
    _url = SDC_SCORE_API_URL + endpoint
    if params:
        params = urllib.parse.urlencode(params)
        _url += "?" + params
    LOG.debug("POST url=%s", _url)
    resp = requests.delete(_url, headers=headers)
    data = resp.json()
    if resp.status_code != HTTPStatus.OK:
        raise RuntimeError(
            "DELETE {} failed with status {}. {}".format(
                endpoint, resp.status_code, data
            )
        )
    return resp


def display_table(data, fields, indent=0):
    """Display a table from data stored as a list of dictionaries.

    Args:
        data(list(dict)): Data in the form of a list of dictionaries
        fields(list(tuple)): Field specification
        indent(int): Number of columns to indent the table
    """
    # Headings
    headings = [
        " {}".format(entry[0]) if i > 0 else "{}".format(entry[0])
        for i, entry in enumerate(fields)
    ]

    # Dictionary data keys
    keys = [entry[1] for entry in fields]

    # Row format
    fmt = ["{" + ":{}.{}s".format(entry[2], entry[2]) + "}" for entry in fields]
    fmt = " " * indent + "|".join(fmt)

    # Print the table.
    LOG.info(fmt.format(*headings))
    LOG.info(fmt.format(*(["-" * 60] * len(headings))))
    for row in data:
        LOG.info(
            fmt.format(
                *[
                    " " + str(row[field]) if i > 0 else str(row[field])
                    for i, field in enumerate(keys)
                ]
            )
        )
