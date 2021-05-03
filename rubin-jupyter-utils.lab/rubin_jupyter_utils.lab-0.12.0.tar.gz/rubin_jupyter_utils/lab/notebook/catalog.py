import requests
import pyvo
import pyvo.auth.authsession
from rubin_jupyter_utils.helpers import get_access_token
from rubin_jupyter_utils.config import RubinConfig


def _get_tap_url():
    rc = RubinConfig()
    tapurl = rc.external_tap_url or (rc.external_instance_url +
                                     rc.tap_route)
    return tapurl


def _get_auth():
    tap_url = _get_tap_url()
    s = requests.Session()
    s.headers["Authorization"] = "Bearer " + get_access_token()
    auth = pyvo.auth.authsession.AuthSession()
    auth.credentials.set("lsst-token", s)
    auth.add_security_method_for_url(tap_url, "lsst-token")
    auth.add_security_method_for_url(tap_url + "/sync", "lsst-token")
    auth.add_security_method_for_url(tap_url + "/async", "lsst-token")
    auth.add_security_method_for_url(tap_url + "/tables", "lsst-token")
    return auth


def get_catalog():
    return pyvo.dal.TAPService(_get_tap_url(), _get_auth())


def retrieve_query(query_url):
    return pyvo.dal.AsyncTAPJob(query_url, _get_auth())
