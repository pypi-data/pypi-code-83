"""
Main interface for detective service literal definitions.

Usage::

    ```python
    from mypy_boto3_detective.literals import MemberDisabledReason

    data: MemberDisabledReason = "VOLUME_TOO_HIGH"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MemberDisabledReason", "MemberStatus")


MemberDisabledReason = Literal["VOLUME_TOO_HIGH", "VOLUME_UNKNOWN"]
MemberStatus = Literal[
    "ACCEPTED_BUT_DISABLED", "ENABLED", "INVITED", "VERIFICATION_FAILED", "VERIFICATION_IN_PROGRESS"
]
