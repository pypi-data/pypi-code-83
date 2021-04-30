"""
Main interface for fis service literal definitions.

Usage::

    ```python
    from mypy_boto3_fis.literals import ExperimentActionStatus

    data: ExperimentActionStatus = "cancelled"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ExperimentActionStatus", "ExperimentStatus")


ExperimentActionStatus = Literal[
    "cancelled", "completed", "failed", "initiating", "pending", "running", "stopped", "stopping"
]
ExperimentStatus = Literal[
    "completed", "failed", "initiating", "pending", "running", "stopped", "stopping"
]
