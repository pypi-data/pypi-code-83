"""
Main interface for synthetics service literal definitions.

Usage::

    ```python
    from mypy_boto3_synthetics.literals import CanaryRunState

    data: CanaryRunState = "FAILED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CanaryRunState", "CanaryRunStateReasonCode", "CanaryState", "CanaryStateReasonCode")


CanaryRunState = Literal["FAILED", "PASSED", "RUNNING"]
CanaryRunStateReasonCode = Literal["CANARY_FAILURE", "EXECUTION_FAILURE"]
CanaryState = Literal[
    "CREATING",
    "DELETING",
    "ERROR",
    "READY",
    "RUNNING",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "UPDATING",
]
CanaryStateReasonCode = Literal["INVALID_PERMISSIONS"]
