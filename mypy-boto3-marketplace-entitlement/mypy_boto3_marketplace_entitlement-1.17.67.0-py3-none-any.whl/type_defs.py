"""
Type annotations for marketplace-entitlement service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_entitlement/type_defs.html)

Usage::

    ```python
    from mypy_boto3_marketplace_entitlement.type_defs import EntitlementTypeDef

    data: EntitlementTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "EntitlementTypeDef",
    "EntitlementValueTypeDef",
    "GetEntitlementsResultTypeDef",
    "PaginatorConfigTypeDef",
)


class EntitlementTypeDef(TypedDict, total=False):
    ProductCode: str
    Dimension: str
    CustomerIdentifier: str
    Value: "EntitlementValueTypeDef"
    ExpirationDate: datetime


class EntitlementValueTypeDef(TypedDict, total=False):
    IntegerValue: int
    DoubleValue: float
    BooleanValue: bool
    StringValue: str


class GetEntitlementsResultTypeDef(TypedDict, total=False):
    Entitlements: List["EntitlementTypeDef"]
    NextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str
