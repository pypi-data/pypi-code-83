"""
Main interface for iotevents-data service literal definitions.

Usage::

    ```python
    from mypy_boto3_iotevents_data.literals import ErrorCode

    data: ErrorCode = "InternalFailureException"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ErrorCode",)


ErrorCode = Literal[
    "InternalFailureException",
    "InvalidRequestException",
    "ResourceNotFoundException",
    "ServiceUnavailableException",
    "ThrottlingException",
]
