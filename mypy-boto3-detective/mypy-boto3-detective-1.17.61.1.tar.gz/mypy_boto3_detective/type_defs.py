"""
Type annotations for detective service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/type_defs.html)

Usage::

    ```python
    from mypy_boto3_detective.type_defs import AccountTypeDef

    data: AccountTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_detective.literals import MemberDisabledReason, MemberStatus

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountTypeDef",
    "CreateGraphResponseTypeDef",
    "CreateMembersResponseTypeDef",
    "DeleteMembersResponseTypeDef",
    "GetMembersResponseTypeDef",
    "GraphTypeDef",
    "ListGraphsResponseTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MemberDetailTypeDef",
    "UnprocessedAccountTypeDef",
)


class AccountTypeDef(TypedDict):
    AccountId: str
    EmailAddress: str


class CreateGraphResponseTypeDef(TypedDict, total=False):
    GraphArn: str


class CreateMembersResponseTypeDef(TypedDict, total=False):
    Members: List["MemberDetailTypeDef"]
    UnprocessedAccounts: List["UnprocessedAccountTypeDef"]


class DeleteMembersResponseTypeDef(TypedDict, total=False):
    AccountIds: List[str]
    UnprocessedAccounts: List["UnprocessedAccountTypeDef"]


class GetMembersResponseTypeDef(TypedDict, total=False):
    MemberDetails: List["MemberDetailTypeDef"]
    UnprocessedAccounts: List["UnprocessedAccountTypeDef"]


class GraphTypeDef(TypedDict, total=False):
    Arn: str
    CreatedTime: datetime


class ListGraphsResponseTypeDef(TypedDict, total=False):
    GraphList: List["GraphTypeDef"]
    NextToken: str


class ListInvitationsResponseTypeDef(TypedDict, total=False):
    Invitations: List["MemberDetailTypeDef"]
    NextToken: str


class ListMembersResponseTypeDef(TypedDict, total=False):
    MemberDetails: List["MemberDetailTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class MemberDetailTypeDef(TypedDict, total=False):
    AccountId: str
    EmailAddress: str
    GraphArn: str
    MasterId: str
    AdministratorId: str
    Status: MemberStatus
    DisabledReason: MemberDisabledReason
    InvitedTime: datetime
    UpdatedTime: datetime
    VolumeUsageInBytes: int
    VolumeUsageUpdatedTime: datetime
    PercentOfGraphUtilization: float
    PercentOfGraphUtilizationUpdatedTime: datetime


class UnprocessedAccountTypeDef(TypedDict, total=False):
    AccountId: str
    Reason: str
