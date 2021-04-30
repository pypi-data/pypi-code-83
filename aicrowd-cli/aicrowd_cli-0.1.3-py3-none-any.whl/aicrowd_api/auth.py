"""
all api calls related to auth
"""

import logging

from aicrowd_api.request import RailsAPI


def verify_api_key(api_key: str) -> bool:
    """
    Verifies if the API Key is valid or not

    Args:
        api_key: AIcrowd API Key

    Returns:
        True if API Key valid, False otherwise
    """
    log = logging.getLogger()

    r = RailsAPI(api_key).get("/api_user")

    if not r.ok:
        log.error(
            "Error in verifying API Key.\nReason: %s, Message: %s", r.reason, r.text
        )

    return r.ok
