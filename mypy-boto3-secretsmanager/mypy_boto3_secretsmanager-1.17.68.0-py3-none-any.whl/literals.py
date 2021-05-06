"""
Type annotations for secretsmanager service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/literals.html)

Usage::

    ```python
    from mypy_boto3_secretsmanager.literals import FilterNameStringType

    data: FilterNameStringType = "all"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("FilterNameStringType", "ListSecretsPaginatorName", "SortOrderType", "StatusType")


FilterNameStringType = Literal[
    "all", "description", "name", "primary-region", "tag-key", "tag-value"
]
ListSecretsPaginatorName = Literal["list_secrets"]
SortOrderType = Literal["asc", "desc"]
StatusType = Literal["Failed", "InProgress", "InSync"]
