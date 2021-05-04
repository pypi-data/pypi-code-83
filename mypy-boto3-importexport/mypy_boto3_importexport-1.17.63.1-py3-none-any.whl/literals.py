"""
Type annotations for importexport service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_importexport/literals.html)

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
