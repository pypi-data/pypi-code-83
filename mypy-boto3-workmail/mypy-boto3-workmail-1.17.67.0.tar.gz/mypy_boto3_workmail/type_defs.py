"""
Type annotations for workmail service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workmail/type_defs.html)

Usage::

    ```python
    from mypy_boto3_workmail.type_defs import AccessControlRuleTypeDef

    data: AccessControlRuleTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_workmail.literals import (
    AccessControlRuleEffect,
    EntityState,
    FolderName,
    MailboxExportJobState,
    MemberType,
    MobileDeviceAccessRuleEffect,
    PermissionType,
    ResourceType,
    RetentionAction,
    UserRole,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessControlRuleTypeDef",
    "BookingOptionsTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateMobileDeviceAccessRuleResponseTypeDef",
    "CreateOrganizationResponseTypeDef",
    "CreateResourceResponseTypeDef",
    "CreateUserResponseTypeDef",
    "DelegateTypeDef",
    "DeleteOrganizationResponseTypeDef",
    "DescribeGroupResponseTypeDef",
    "DescribeMailboxExportJobResponseTypeDef",
    "DescribeOrganizationResponseTypeDef",
    "DescribeResourceResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "DomainTypeDef",
    "FolderConfigurationTypeDef",
    "GetAccessControlEffectResponseTypeDef",
    "GetDefaultRetentionPolicyResponseTypeDef",
    "GetMailboxDetailsResponseTypeDef",
    "GetMobileDeviceAccessEffectResponseTypeDef",
    "GroupTypeDef",
    "ListAccessControlRulesResponseTypeDef",
    "ListAliasesResponseTypeDef",
    "ListGroupMembersResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListMailboxExportJobsResponseTypeDef",
    "ListMailboxPermissionsResponseTypeDef",
    "ListMobileDeviceAccessRulesResponseTypeDef",
    "ListOrganizationsResponseTypeDef",
    "ListResourceDelegatesResponseTypeDef",
    "ListResourcesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersResponseTypeDef",
    "MailboxExportJobTypeDef",
    "MemberTypeDef",
    "MobileDeviceAccessMatchedRuleTypeDef",
    "MobileDeviceAccessRuleTypeDef",
    "OrganizationSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "ResourceTypeDef",
    "StartMailboxExportJobResponseTypeDef",
    "TagTypeDef",
    "UserTypeDef",
)


class AccessControlRuleTypeDef(TypedDict, total=False):
    Name: str
    Effect: AccessControlRuleEffect
    Description: str
    IpRanges: List[str]
    NotIpRanges: List[str]
    Actions: List[str]
    NotActions: List[str]
    UserIds: List[str]
    NotUserIds: List[str]
    DateCreated: datetime
    DateModified: datetime


class BookingOptionsTypeDef(TypedDict, total=False):
    AutoAcceptRequests: bool
    AutoDeclineRecurringRequests: bool
    AutoDeclineConflictingRequests: bool


class CreateGroupResponseTypeDef(TypedDict, total=False):
    GroupId: str


class CreateMobileDeviceAccessRuleResponseTypeDef(TypedDict, total=False):
    MobileDeviceAccessRuleId: str


class CreateOrganizationResponseTypeDef(TypedDict, total=False):
    OrganizationId: str


class CreateResourceResponseTypeDef(TypedDict, total=False):
    ResourceId: str


class CreateUserResponseTypeDef(TypedDict, total=False):
    UserId: str


DelegateTypeDef = TypedDict("DelegateTypeDef", {"Id": str, "Type": MemberType})


class DeleteOrganizationResponseTypeDef(TypedDict, total=False):
    OrganizationId: str
    State: str


class DescribeGroupResponseTypeDef(TypedDict, total=False):
    GroupId: str
    Name: str
    Email: str
    State: EntityState
    EnabledDate: datetime
    DisabledDate: datetime


class DescribeMailboxExportJobResponseTypeDef(TypedDict, total=False):
    EntityId: str
    Description: str
    RoleArn: str
    KmsKeyArn: str
    S3BucketName: str
    S3Prefix: str
    S3Path: str
    EstimatedProgress: int
    State: MailboxExportJobState
    ErrorInfo: str
    StartTime: datetime
    EndTime: datetime


class DescribeOrganizationResponseTypeDef(TypedDict, total=False):
    OrganizationId: str
    Alias: str
    State: str
    DirectoryId: str
    DirectoryType: str
    DefaultMailDomain: str
    CompletedDate: datetime
    ErrorMessage: str
    ARN: str


DescribeResourceResponseTypeDef = TypedDict(
    "DescribeResourceResponseTypeDef",
    {
        "ResourceId": str,
        "Email": str,
        "Name": str,
        "Type": ResourceType,
        "BookingOptions": "BookingOptionsTypeDef",
        "State": EntityState,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class DescribeUserResponseTypeDef(TypedDict, total=False):
    UserId: str
    Name: str
    Email: str
    DisplayName: str
    State: EntityState
    UserRole: UserRole
    EnabledDate: datetime
    DisabledDate: datetime


class DomainTypeDef(TypedDict, total=False):
    DomainName: str
    HostedZoneId: str


class _RequiredFolderConfigurationTypeDef(TypedDict):
    Name: FolderName
    Action: RetentionAction


class FolderConfigurationTypeDef(_RequiredFolderConfigurationTypeDef, total=False):
    Period: int


class GetAccessControlEffectResponseTypeDef(TypedDict, total=False):
    Effect: AccessControlRuleEffect
    MatchedRules: List[str]


class GetDefaultRetentionPolicyResponseTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Description: str
    FolderConfigurations: List["FolderConfigurationTypeDef"]


class GetMailboxDetailsResponseTypeDef(TypedDict, total=False):
    MailboxQuota: int
    MailboxSize: float


class GetMobileDeviceAccessEffectResponseTypeDef(TypedDict, total=False):
    Effect: MobileDeviceAccessRuleEffect
    MatchedRules: List["MobileDeviceAccessMatchedRuleTypeDef"]


class GroupTypeDef(TypedDict, total=False):
    Id: str
    Email: str
    Name: str
    State: EntityState
    EnabledDate: datetime
    DisabledDate: datetime


class ListAccessControlRulesResponseTypeDef(TypedDict, total=False):
    Rules: List["AccessControlRuleTypeDef"]


class ListAliasesResponseTypeDef(TypedDict, total=False):
    Aliases: List[str]
    NextToken: str


class ListGroupMembersResponseTypeDef(TypedDict, total=False):
    Members: List["MemberTypeDef"]
    NextToken: str


class ListGroupsResponseTypeDef(TypedDict, total=False):
    Groups: List["GroupTypeDef"]
    NextToken: str


class ListMailboxExportJobsResponseTypeDef(TypedDict, total=False):
    Jobs: List["MailboxExportJobTypeDef"]
    NextToken: str


class ListMailboxPermissionsResponseTypeDef(TypedDict, total=False):
    Permissions: List["PermissionTypeDef"]
    NextToken: str


class ListMobileDeviceAccessRulesResponseTypeDef(TypedDict, total=False):
    Rules: List["MobileDeviceAccessRuleTypeDef"]


class ListOrganizationsResponseTypeDef(TypedDict, total=False):
    OrganizationSummaries: List["OrganizationSummaryTypeDef"]
    NextToken: str


class ListResourceDelegatesResponseTypeDef(TypedDict, total=False):
    Delegates: List["DelegateTypeDef"]
    NextToken: str


class ListResourcesResponseTypeDef(TypedDict, total=False):
    Resources: List["ResourceTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class ListUsersResponseTypeDef(TypedDict, total=False):
    Users: List["UserTypeDef"]
    NextToken: str


class MailboxExportJobTypeDef(TypedDict, total=False):
    JobId: str
    EntityId: str
    Description: str
    S3BucketName: str
    S3Path: str
    EstimatedProgress: int
    State: MailboxExportJobState
    StartTime: datetime
    EndTime: datetime


MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "Id": str,
        "Name": str,
        "Type": MemberType,
        "State": EntityState,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class MobileDeviceAccessMatchedRuleTypeDef(TypedDict, total=False):
    MobileDeviceAccessRuleId: str
    Name: str


class MobileDeviceAccessRuleTypeDef(TypedDict, total=False):
    MobileDeviceAccessRuleId: str
    Name: str
    Description: str
    Effect: MobileDeviceAccessRuleEffect
    DeviceTypes: List[str]
    NotDeviceTypes: List[str]
    DeviceModels: List[str]
    NotDeviceModels: List[str]
    DeviceOperatingSystems: List[str]
    NotDeviceOperatingSystems: List[str]
    DeviceUserAgents: List[str]
    NotDeviceUserAgents: List[str]
    DateCreated: datetime
    DateModified: datetime


class OrganizationSummaryTypeDef(TypedDict, total=False):
    OrganizationId: str
    Alias: str
    DefaultMailDomain: str
    ErrorMessage: str
    State: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PermissionTypeDef(TypedDict):
    GranteeId: str
    GranteeType: MemberType
    PermissionValues: List[PermissionType]


ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "Id": str,
        "Email": str,
        "Name": str,
        "Type": ResourceType,
        "State": EntityState,
        "EnabledDate": datetime,
        "DisabledDate": datetime,
    },
    total=False,
)


class StartMailboxExportJobResponseTypeDef(TypedDict, total=False):
    JobId: str


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class UserTypeDef(TypedDict, total=False):
    Id: str
    Email: str
    Name: str
    DisplayName: str
    State: EntityState
    UserRole: UserRole
    EnabledDate: datetime
    DisabledDate: datetime
