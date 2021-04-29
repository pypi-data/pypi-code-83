"""
Main interface for importexport service literal definitions.

Usage::

    ```python
    from mypy_boto3_importexport.literals import JobType

    data: JobType = "Export"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("JobType", "ListJobsPaginatorName")


JobType = Literal["Export", "Import"]
ListJobsPaginatorName = Literal["list_jobs"]
