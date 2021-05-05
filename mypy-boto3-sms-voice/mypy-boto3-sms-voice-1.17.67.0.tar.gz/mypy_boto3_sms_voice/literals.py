"""
Type annotations for sms-voice service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms_voice/literals.html)

Usage::

    ```python
    from mypy_boto3_sms_voice.literals import EventType

    data: EventType = "ANSWERED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EventType",)


EventType = Literal[
    "ANSWERED", "BUSY", "COMPLETED_CALL", "FAILED", "INITIATED_CALL", "NO_ANSWER", "RINGING"
]
