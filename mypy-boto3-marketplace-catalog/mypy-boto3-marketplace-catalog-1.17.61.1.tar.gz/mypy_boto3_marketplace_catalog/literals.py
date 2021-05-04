"""
Type annotations for marketplace-catalog service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/literals.html)

Usage::

    ```python
    from mypy_boto3_marketplace_catalog.literals import ChangeStatus

    data: ChangeStatus = "APPLYING"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ChangeStatus", "FailureCode", "SortOrder")


ChangeStatus = Literal["APPLYING", "CANCELLED", "FAILED", "PREPARING", "SUCCEEDED"]
FailureCode = Literal["CLIENT_ERROR", "SERVER_FAULT"]
SortOrder = Literal["ASCENDING", "DESCENDING"]
