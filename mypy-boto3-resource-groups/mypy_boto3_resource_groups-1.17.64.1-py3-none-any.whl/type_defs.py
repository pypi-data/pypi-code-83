"""
Type annotations for resource-groups service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resource_groups/type_defs.html)

Usage::

    ```python
    from mypy_boto3_resource_groups.type_defs import CreateGroupOutputTypeDef

    data: CreateGroupOutputTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from mypy_boto3_resource_groups.literals import (
    GroupConfigurationStatus,
    GroupFilterName,
    QueryErrorCode,
    QueryType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateGroupOutputTypeDef",
    "DeleteGroupOutputTypeDef",
    "FailedResourceTypeDef",
    "GetGroupConfigurationOutputTypeDef",
    "GetGroupOutputTypeDef",
    "GetGroupQueryOutputTypeDef",
    "GetTagsOutputTypeDef",
    "GroupConfigurationItemTypeDef",
    "GroupConfigurationParameterTypeDef",
    "GroupConfigurationTypeDef",
    "GroupFilterTypeDef",
    "GroupIdentifierTypeDef",
    "GroupQueryTypeDef",
    "GroupResourcesOutputTypeDef",
    "GroupTypeDef",
    "ListGroupResourcesItemTypeDef",
    "ListGroupResourcesOutputTypeDef",
    "ListGroupsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PendingResourceTypeDef",
    "QueryErrorTypeDef",
    "ResourceFilterTypeDef",
    "ResourceIdentifierTypeDef",
    "ResourceQueryTypeDef",
    "ResourceStatusTypeDef",
    "ResponseMetadata",
    "SearchResourcesOutputTypeDef",
    "TagOutputTypeDef",
    "UngroupResourcesOutputTypeDef",
    "UntagOutputTypeDef",
    "UpdateGroupOutputTypeDef",
    "UpdateGroupQueryOutputTypeDef",
)


class CreateGroupOutputTypeDef(TypedDict):
    Group: "GroupTypeDef"
    ResourceQuery: "ResourceQueryTypeDef"
    Tags: Dict[str, str]
    GroupConfiguration: "GroupConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeleteGroupOutputTypeDef(TypedDict):
    Group: "GroupTypeDef"
    ResponseMetadata: "ResponseMetadata"


class FailedResourceTypeDef(TypedDict, total=False):
    ResourceArn: str
    ErrorMessage: str
    ErrorCode: str


class GetGroupConfigurationOutputTypeDef(TypedDict):
    GroupConfiguration: "GroupConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetGroupOutputTypeDef(TypedDict):
    Group: "GroupTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetGroupQueryOutputTypeDef(TypedDict):
    GroupQuery: "GroupQueryTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetTagsOutputTypeDef(TypedDict):
    Arn: str
    Tags: Dict[str, str]
    ResponseMetadata: "ResponseMetadata"


_RequiredGroupConfigurationItemTypeDef = TypedDict(
    "_RequiredGroupConfigurationItemTypeDef", {"Type": str}
)
_OptionalGroupConfigurationItemTypeDef = TypedDict(
    "_OptionalGroupConfigurationItemTypeDef",
    {"Parameters": List["GroupConfigurationParameterTypeDef"]},
    total=False,
)


class GroupConfigurationItemTypeDef(
    _RequiredGroupConfigurationItemTypeDef, _OptionalGroupConfigurationItemTypeDef
):
    pass


class _RequiredGroupConfigurationParameterTypeDef(TypedDict):
    Name: str


class GroupConfigurationParameterTypeDef(_RequiredGroupConfigurationParameterTypeDef, total=False):
    Values: List[str]


class GroupConfigurationTypeDef(TypedDict, total=False):
    Configuration: List["GroupConfigurationItemTypeDef"]
    ProposedConfiguration: List["GroupConfigurationItemTypeDef"]
    Status: GroupConfigurationStatus
    FailureReason: str


class GroupFilterTypeDef(TypedDict):
    Name: GroupFilterName
    Values: List[str]


class GroupIdentifierTypeDef(TypedDict, total=False):
    GroupName: str
    GroupArn: str


class GroupQueryTypeDef(TypedDict):
    GroupName: str
    ResourceQuery: "ResourceQueryTypeDef"


class GroupResourcesOutputTypeDef(TypedDict):
    Succeeded: List[str]
    Failed: List["FailedResourceTypeDef"]
    Pending: List["PendingResourceTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class _RequiredGroupTypeDef(TypedDict):
    GroupArn: str
    Name: str


class GroupTypeDef(_RequiredGroupTypeDef, total=False):
    Description: str


class ListGroupResourcesItemTypeDef(TypedDict, total=False):
    Identifier: "ResourceIdentifierTypeDef"
    Status: "ResourceStatusTypeDef"


class ListGroupResourcesOutputTypeDef(TypedDict):
    Resources: List["ListGroupResourcesItemTypeDef"]
    ResourceIdentifiers: List["ResourceIdentifierTypeDef"]
    NextToken: str
    QueryErrors: List["QueryErrorTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListGroupsOutputTypeDef(TypedDict):
    GroupIdentifiers: List["GroupIdentifierTypeDef"]
    Groups: List["GroupTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PendingResourceTypeDef(TypedDict, total=False):
    ResourceArn: str


class QueryErrorTypeDef(TypedDict, total=False):
    ErrorCode: QueryErrorCode
    Message: str


class ResourceFilterTypeDef(TypedDict):
    Name: Literal["resource-type"]
    Values: List[str]


class ResourceIdentifierTypeDef(TypedDict, total=False):
    ResourceArn: str
    ResourceType: str


ResourceQueryTypeDef = TypedDict("ResourceQueryTypeDef", {"Type": QueryType, "Query": str})


class ResourceStatusTypeDef(TypedDict, total=False):
    Name: Literal["PENDING"]


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class SearchResourcesOutputTypeDef(TypedDict):
    ResourceIdentifiers: List["ResourceIdentifierTypeDef"]
    NextToken: str
    QueryErrors: List["QueryErrorTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class TagOutputTypeDef(TypedDict):
    Arn: str
    Tags: Dict[str, str]
    ResponseMetadata: "ResponseMetadata"


class UngroupResourcesOutputTypeDef(TypedDict):
    Succeeded: List[str]
    Failed: List["FailedResourceTypeDef"]
    Pending: List["PendingResourceTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class UntagOutputTypeDef(TypedDict):
    Arn: str
    Keys: List[str]
    ResponseMetadata: "ResponseMetadata"


class UpdateGroupOutputTypeDef(TypedDict):
    Group: "GroupTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateGroupQueryOutputTypeDef(TypedDict):
    GroupQuery: "GroupQueryTypeDef"
    ResponseMetadata: "ResponseMetadata"
