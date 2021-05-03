"""Testing voices client."""

import logging
import os
import uuid

import pytest

from voices import Voices

VOICES_USER = os.getenv('VOICES_USER')
VOICES_PASS = os.getenv('VOICES_PASS')


@pytest.mark.parametrize(
    'user,password,phone,message,trace_id,code,err',
    [
        (
            VOICES_USER,
            VOICES_PASS,
            '5561463627',
            'Unit testing message',
            str(uuid.uuid4()),
            200,
            None,
        ),
        (
            VOICES_USER,
            VOICES_PASS,
            '5561463627',
            'Unit testing message',
            None,
            200,
            None,
        ),
        (
            VOICES_USER,
            VOICES_PASS,
            '1234567890',
            '',
            str(uuid.uuid4()),
            None,
            'voices: empty message is not allowed',
        ),
        (
            VOICES_USER,
            VOICES_PASS,
            '',
            'Unit testing message',
            str(uuid.uuid4()),
            None,
            "voices: invalid phone number format ''",
        ),
        (
            VOICES_USER,
            VOICES_PASS,
            'asdasd',
            'Unit testing message',
            str(uuid.uuid4()),
            None,
            "voices: invalid phone number format 'asdasd'",
        ),
        (
            VOICES_USER,
            VOICES_PASS,
            '1234567890',
            'Unit testing message',
            str(uuid.uuid4()),
            None,
            'voices: [500] No se pudo identificar el numero , error de sistema',
        ),
        (
            VOICES_USER,
            VOICES_PASS,
            '1234567890',
            ''.join(['a' for _ in range(165)]),
            str(uuid.uuid4()),
            None,
            'voices: message limit exceeded 165/160',
        ),
        (
            'asdasd',
            'asdasd',
            '5561463627',
            'Unit testing message',
            str(uuid.uuid4()),
            None,
            'voices: [401] Credenciales no validas o usuario desactivado, favor de verificar',
        ),
    ],
)
def test_send_sms(user, password, phone, message, trace_id, code, err):
    """Should test send_sms request method from client."""

    client = Voices(user, password, logger_level=logging.DEBUG)

    try:
        response = client.send_sms(phone, message, trace_id)
        assert 'code' in response.keys() and response['code'] == code
    except Exception as error:
        if err is not None:
            assert err == str(error)
            return
