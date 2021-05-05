"""
Type annotations for sdb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sdb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sdb.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttributeTypeDef",
    "DeletableItemTypeDef",
    "DomainMetadataResultTypeDef",
    "GetAttributesResultTypeDef",
    "ItemTypeDef",
    "ListDomainsResultTypeDef",
    "PaginatorConfigTypeDef",
    "ReplaceableAttributeTypeDef",
    "ReplaceableItemTypeDef",
    "SelectResultTypeDef",
    "UpdateConditionTypeDef",
)


class _RequiredAttributeTypeDef(TypedDict):
    Name: str
    Value: str


class AttributeTypeDef(_RequiredAttributeTypeDef, total=False):
    AlternateNameEncoding: str
    AlternateValueEncoding: str


class _RequiredDeletableItemTypeDef(TypedDict):
    Name: str


class DeletableItemTypeDef(_RequiredDeletableItemTypeDef, total=False):
    Attributes: List["AttributeTypeDef"]


class DomainMetadataResultTypeDef(TypedDict, total=False):
    ItemCount: int
    ItemNamesSizeBytes: int
    AttributeNameCount: int
    AttributeNamesSizeBytes: int
    AttributeValueCount: int
    AttributeValuesSizeBytes: int
    Timestamp: int


class GetAttributesResultTypeDef(TypedDict, total=False):
    Attributes: List["AttributeTypeDef"]


class _RequiredItemTypeDef(TypedDict):
    Name: str
    Attributes: List["AttributeTypeDef"]


class ItemTypeDef(_RequiredItemTypeDef, total=False):
    AlternateNameEncoding: str


class ListDomainsResultTypeDef(TypedDict, total=False):
    DomainNames: List[str]
    NextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredReplaceableAttributeTypeDef(TypedDict):
    Name: str
    Value: str


class ReplaceableAttributeTypeDef(_RequiredReplaceableAttributeTypeDef, total=False):
    Replace: bool


class ReplaceableItemTypeDef(TypedDict):
    Name: str
    Attributes: List["ReplaceableAttributeTypeDef"]


class SelectResultTypeDef(TypedDict, total=False):
    Items: List["ItemTypeDef"]
    NextToken: str


class UpdateConditionTypeDef(TypedDict, total=False):
    Name: str
    Value: str
    Exists: bool
