"""Voices integration methods."""

import json
from typing import Any, AnyStr, Dict, NoReturn

import voices.validations as validations

from .logger import build_logger
from .utils import send_request


class Voices:
    """Voices client."""

    BASE_URL = 'https://sms-voices.com.mx:8080'

    def __init__(self, user: AnyStr = None, password: AnyStr = None, **kwargs):
        self.user = user
        self.password = password
        self.logger = build_logger(**kwargs)

    def send_sms(self, phone: AnyStr, message: AnyStr, trace_id: AnyStr = None) -> Dict[AnyStr, Any]:
        """Send SMS to an specific phone.

        :param phone: User phone
        :param message: SMS message text
        :param trace_id: Trace ID for the sms
        :return AnyStr: SMS ID
        """

        validations.phone_number(phone)
        validations.message(message)

        method = 'POST'
        url = f'{self.BASE_URL}/envioSms'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        body = {
            'user': self.user,
            'password': self.password,
            'number': phone,
            'message': message,
        }

        if trace_id is not None:
            body['campo_extra'] = trace_id

        self._log_request(headers=headers, body=body, method=method, path=url)

        response = send_request(method=method, url=url, body=body, headers=headers)
        response = json.loads(response)
        validations.response(response)

        return response

    def _log_request(
        self, headers: Dict[AnyStr, AnyStr], body: Dict[AnyStr, AnyStr], method: AnyStr, path: AnyStr,
    ) -> NoReturn:
        """Log request params for debug purpose.

        :param headers: Request headers.
        :param body: Body params that will be as www-url-form-encoded
        :param method: Request Method
        :param path: Resource Path
        """

        self.logger.debug(
            'method: %s url: %s headers: %s body: %s' % (
                method, f'{self.BASE_URL}{path}', str(headers), str(body),
            ),
        )
