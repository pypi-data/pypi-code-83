"""
Main interface for kinesisanalytics service literal definitions.

Usage::

    ```python
    from mypy_boto3_kinesisanalytics.literals import ApplicationStatus

    data: ApplicationStatus = "DELETING"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ApplicationStatus", "InputStartingPosition", "RecordFormatType")


ApplicationStatus = Literal["DELETING", "READY", "RUNNING", "STARTING", "STOPPING", "UPDATING"]
InputStartingPosition = Literal["LAST_STOPPED_POINT", "NOW", "TRIM_HORIZON"]
RecordFormatType = Literal["CSV", "JSON"]
