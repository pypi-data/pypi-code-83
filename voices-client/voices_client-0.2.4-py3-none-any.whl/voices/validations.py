"""Validations for Voices requests."""

import re
from typing import Any, AnyStr, Dict, NoReturn

from .errors import DataError, RequestError


def phone_number(phone: AnyStr) -> NoReturn:
    """Validate phone number format.

    :param phone: Destination phone number
    :raise DataError: Invalid phone number
    """

    if not re.match(r'^[0-9]{10}$', phone):
        raise DataError(f"voices: invalid phone number format '{phone}'")


def message(text: AnyStr) -> NoReturn:
    """Validate message structure of the SMS.

    :param text: SMS message text
    """

    if text is None or len(text) < 1:
        raise DataError('voices: empty message is not allowed')

    if len(text) > 160:
        raise DataError(f'voices: message limit exceeded {len(text)}/160')


def response(data: Dict[AnyStr, Any]) -> NoReturn:
    """Validate Voices response codes."""

    if 'code' not in data.keys():
        raise RequestError(
            f"voices: unexpected response payload, missing 'code' field ({str(data)})",
        )

    if data['code'] != 200:
        raise RequestError(f"voices: [{data['code']}] {data['desc']}")
