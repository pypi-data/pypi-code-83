"""
Type annotations for mwaa service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mwaa/literals.html)

Usage::

    ```python
    from mypy_boto3_mwaa.literals import EnvironmentStatus

    data: EnvironmentStatus = "AVAILABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "EnvironmentStatus",
    "ListEnvironmentsPaginatorName",
    "LoggingLevel",
    "Unit",
    "UpdateStatus",
    "WebserverAccessMode",
)


EnvironmentStatus = Literal[
    "AVAILABLE",
    "CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETING",
    "UNAVAILABLE",
    "UPDATE_FAILED",
    "UPDATING",
]
ListEnvironmentsPaginatorName = Literal["list_environments"]
LoggingLevel = Literal["CRITICAL", "DEBUG", "ERROR", "INFO", "WARNING"]
Unit = Literal[
    "Bits",
    "Bits/Second",
    "Bytes",
    "Bytes/Second",
    "Count",
    "Count/Second",
    "Gigabits",
    "Gigabits/Second",
    "Gigabytes",
    "Gigabytes/Second",
    "Kilobits",
    "Kilobits/Second",
    "Kilobytes",
    "Kilobytes/Second",
    "Megabits",
    "Megabits/Second",
    "Megabytes",
    "Megabytes/Second",
    "Microseconds",
    "Milliseconds",
    "None",
    "Percent",
    "Seconds",
    "Terabits",
    "Terabits/Second",
    "Terabytes",
    "Terabytes/Second",
]
UpdateStatus = Literal["FAILED", "PENDING", "SUCCESS"]
WebserverAccessMode = Literal["PRIVATE_ONLY", "PUBLIC_ONLY"]
