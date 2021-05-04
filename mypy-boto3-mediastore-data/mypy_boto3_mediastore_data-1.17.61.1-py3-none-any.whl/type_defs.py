"""
Type annotations for mediastore-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediastore_data.type_defs import DescribeObjectResponseTypeDef

    data: DescribeObjectResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from botocore.response import StreamingBody

from mypy_boto3_mediastore_data.literals import ItemType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DescribeObjectResponseTypeDef",
    "GetObjectResponseTypeDef",
    "ItemTypeDef",
    "ListItemsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutObjectResponseTypeDef",
)


class DescribeObjectResponseTypeDef(TypedDict, total=False):
    ETag: str
    ContentType: str
    ContentLength: int
    CacheControl: str
    LastModified: datetime


class _RequiredGetObjectResponseTypeDef(TypedDict):
    StatusCode: int


class GetObjectResponseTypeDef(_RequiredGetObjectResponseTypeDef, total=False):
    Body: StreamingBody
    CacheControl: str
    ContentRange: str
    ContentLength: int
    ContentType: str
    ETag: str
    LastModified: datetime


ItemTypeDef = TypedDict(
    "ItemTypeDef",
    {
        "Name": str,
        "Type": ItemType,
        "ETag": str,
        "LastModified": datetime,
        "ContentType": str,
        "ContentLength": int,
    },
    total=False,
)


class ListItemsResponseTypeDef(TypedDict, total=False):
    Items: List["ItemTypeDef"]
    NextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PutObjectResponseTypeDef(TypedDict, total=False):
    ContentSHA256: str
    ETag: str
    StorageClass: Literal["TEMPORAL"]
