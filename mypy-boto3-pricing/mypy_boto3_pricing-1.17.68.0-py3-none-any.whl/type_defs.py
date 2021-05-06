"""
Type annotations for pricing service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pricing/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pricing.type_defs import AttributeValueTypeDef

    data: AttributeValueTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttributeValueTypeDef",
    "DescribeServicesResponseTypeDef",
    "FilterTypeDef",
    "GetAttributeValuesResponseTypeDef",
    "GetProductsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ServiceTypeDef",
)


class AttributeValueTypeDef(TypedDict, total=False):
    Value: str


class DescribeServicesResponseTypeDef(TypedDict, total=False):
    Services: List["ServiceTypeDef"]
    FormatVersion: str
    NextToken: str


FilterTypeDef = TypedDict(
    "FilterTypeDef", {"Type": Literal["TERM_MATCH"], "Field": str, "Value": str}
)


class GetAttributeValuesResponseTypeDef(TypedDict, total=False):
    AttributeValues: List["AttributeValueTypeDef"]
    NextToken: str


class GetProductsResponseTypeDef(TypedDict, total=False):
    FormatVersion: str
    PriceList: List[str]
    NextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ServiceTypeDef(TypedDict, total=False):
    ServiceCode: str
    AttributeNames: List[str]
