"""
Type annotations for healthlake service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/literals.html)

Usage::

    ```python
    from mypy_boto3_healthlake.literals import DatastoreStatus

    data: DatastoreStatus = "ACTIVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DatastoreStatus", "FHIRVersion", "JobStatus", "PreloadDataType")


DatastoreStatus = Literal["ACTIVE", "CREATING", "DELETED", "DELETING"]
FHIRVersion = Literal["R4"]
JobStatus = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "SUBMITTED"]
PreloadDataType = Literal["SYNTHEA"]
