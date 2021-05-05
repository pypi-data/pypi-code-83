"""
Type annotations for cloud9 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloud9/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloud9.type_defs import CreateEnvironmentEC2ResultTypeDef

    data: CreateEnvironmentEC2ResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_cloud9.literals import (
    ConnectionType,
    EnvironmentLifecycleStatus,
    EnvironmentStatus,
    EnvironmentType,
    ManagedCredentialsStatus,
    Permissions,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateEnvironmentEC2ResultTypeDef",
    "CreateEnvironmentMembershipResultTypeDef",
    "DescribeEnvironmentMembershipsResultTypeDef",
    "DescribeEnvironmentStatusResultTypeDef",
    "DescribeEnvironmentsResultTypeDef",
    "EnvironmentLifecycleTypeDef",
    "EnvironmentMemberTypeDef",
    "EnvironmentTypeDef",
    "ListEnvironmentsResultTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "TagTypeDef",
    "UpdateEnvironmentMembershipResultTypeDef",
)


class CreateEnvironmentEC2ResultTypeDef(TypedDict, total=False):
    environmentId: str


class CreateEnvironmentMembershipResultTypeDef(TypedDict):
    membership: "EnvironmentMemberTypeDef"


class DescribeEnvironmentMembershipsResultTypeDef(TypedDict, total=False):
    memberships: List["EnvironmentMemberTypeDef"]
    nextToken: str


class DescribeEnvironmentStatusResultTypeDef(TypedDict):
    status: EnvironmentStatus
    message: str


class DescribeEnvironmentsResultTypeDef(TypedDict, total=False):
    environments: List["EnvironmentTypeDef"]


class EnvironmentLifecycleTypeDef(TypedDict, total=False):
    status: EnvironmentLifecycleStatus
    reason: str
    failureResource: str


class _RequiredEnvironmentMemberTypeDef(TypedDict):
    permissions: Permissions
    userId: str
    userArn: str
    environmentId: str


class EnvironmentMemberTypeDef(_RequiredEnvironmentMemberTypeDef, total=False):
    lastAccess: datetime


_RequiredEnvironmentTypeDef = TypedDict(
    "_RequiredEnvironmentTypeDef", {"type": EnvironmentType, "arn": str, "ownerArn": str}
)
_OptionalEnvironmentTypeDef = TypedDict(
    "_OptionalEnvironmentTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "connectionType": ConnectionType,
        "lifecycle": "EnvironmentLifecycleTypeDef",
        "managedCredentialsStatus": ManagedCredentialsStatus,
    },
    total=False,
)


class EnvironmentTypeDef(_RequiredEnvironmentTypeDef, _OptionalEnvironmentTypeDef):
    pass


class ListEnvironmentsResultTypeDef(TypedDict, total=False):
    nextToken: str
    environmentIds: List[str]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class UpdateEnvironmentMembershipResultTypeDef(TypedDict, total=False):
    membership: "EnvironmentMemberTypeDef"
