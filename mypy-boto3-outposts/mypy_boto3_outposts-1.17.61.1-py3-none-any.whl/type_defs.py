"""
Type annotations for outposts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_outposts.type_defs import CreateOutpostOutputTypeDef

    data: CreateOutpostOutputTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateOutpostOutputTypeDef",
    "GetOutpostInstanceTypesOutputTypeDef",
    "GetOutpostOutputTypeDef",
    "InstanceTypeItemTypeDef",
    "ListOutpostsOutputTypeDef",
    "ListSitesOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OutpostTypeDef",
    "ResponseMetadata",
    "SiteTypeDef",
)


class CreateOutpostOutputTypeDef(TypedDict):
    Outpost: "OutpostTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetOutpostInstanceTypesOutputTypeDef(TypedDict):
    InstanceTypes: List["InstanceTypeItemTypeDef"]
    NextToken: str
    OutpostId: str
    OutpostArn: str
    ResponseMetadata: "ResponseMetadata"


class GetOutpostOutputTypeDef(TypedDict):
    Outpost: "OutpostTypeDef"
    ResponseMetadata: "ResponseMetadata"


class InstanceTypeItemTypeDef(TypedDict, total=False):
    InstanceType: str


class ListOutpostsOutputTypeDef(TypedDict):
    Outposts: List["OutpostTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListSitesOutputTypeDef(TypedDict):
    Sites: List["SiteTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class OutpostTypeDef(TypedDict, total=False):
    OutpostId: str
    OwnerId: str
    OutpostArn: str
    SiteId: str
    Name: str
    Description: str
    LifeCycleStatus: str
    AvailabilityZone: str
    AvailabilityZoneId: str
    Tags: Dict[str, str]


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class SiteTypeDef(TypedDict, total=False):
    SiteId: str
    AccountId: str
    Name: str
    Description: str
    Tags: Dict[str, str]
