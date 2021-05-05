"""
Type annotations for workspaces service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/type_defs.html)

Usage::

    ```python
    from mypy_boto3_workspaces.type_defs import AccountModificationTypeDef

    data: AccountModificationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_workspaces.literals import (
    AccessPropertyValue,
    AssociationStatus,
    Compute,
    ConnectionAliasState,
    ConnectionState,
    DedicatedTenancyModificationStateEnum,
    DedicatedTenancySupportResultEnum,
    ModificationResourceEnum,
    ModificationStateEnum,
    OperatingSystemType,
    ReconnectEnum,
    RunningMode,
    Tenancy,
    WorkspaceDirectoryState,
    WorkspaceDirectoryType,
    WorkspaceImageRequiredTenancy,
    WorkspaceImageState,
    WorkspaceState,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountModificationTypeDef",
    "AssociateConnectionAliasResultTypeDef",
    "ClientPropertiesResultTypeDef",
    "ClientPropertiesTypeDef",
    "ComputeTypeTypeDef",
    "ConnectionAliasAssociationTypeDef",
    "ConnectionAliasPermissionTypeDef",
    "ConnectionAliasTypeDef",
    "CopyWorkspaceImageResultTypeDef",
    "CreateConnectionAliasResultTypeDef",
    "CreateIpGroupResultTypeDef",
    "CreateWorkspaceBundleResultTypeDef",
    "CreateWorkspacesResultTypeDef",
    "DefaultWorkspaceCreationPropertiesTypeDef",
    "DescribeAccountModificationsResultTypeDef",
    "DescribeAccountResultTypeDef",
    "DescribeClientPropertiesResultTypeDef",
    "DescribeConnectionAliasPermissionsResultTypeDef",
    "DescribeConnectionAliasesResultTypeDef",
    "DescribeIpGroupsResultTypeDef",
    "DescribeTagsResultTypeDef",
    "DescribeWorkspaceBundlesResultTypeDef",
    "DescribeWorkspaceDirectoriesResultTypeDef",
    "DescribeWorkspaceImagePermissionsResultTypeDef",
    "DescribeWorkspaceImagesResultTypeDef",
    "DescribeWorkspaceSnapshotsResultTypeDef",
    "DescribeWorkspacesConnectionStatusResultTypeDef",
    "DescribeWorkspacesResultTypeDef",
    "FailedCreateWorkspaceRequestTypeDef",
    "FailedWorkspaceChangeRequestTypeDef",
    "ImagePermissionTypeDef",
    "ImportWorkspaceImageResultTypeDef",
    "IpRuleItemTypeDef",
    "ListAvailableManagementCidrRangesResultTypeDef",
    "MigrateWorkspaceResultTypeDef",
    "ModificationStateTypeDef",
    "OperatingSystemTypeDef",
    "PaginatorConfigTypeDef",
    "RebootRequestTypeDef",
    "RebootWorkspacesResultTypeDef",
    "RebuildRequestTypeDef",
    "RebuildWorkspacesResultTypeDef",
    "RootStorageTypeDef",
    "SelfservicePermissionsTypeDef",
    "SnapshotTypeDef",
    "StartRequestTypeDef",
    "StartWorkspacesResultTypeDef",
    "StopRequestTypeDef",
    "StopWorkspacesResultTypeDef",
    "TagTypeDef",
    "TerminateRequestTypeDef",
    "TerminateWorkspacesResultTypeDef",
    "UserStorageTypeDef",
    "WorkspaceAccessPropertiesTypeDef",
    "WorkspaceBundleTypeDef",
    "WorkspaceConnectionStatusTypeDef",
    "WorkspaceCreationPropertiesTypeDef",
    "WorkspaceDirectoryTypeDef",
    "WorkspaceImageTypeDef",
    "WorkspacePropertiesTypeDef",
    "WorkspaceRequestTypeDef",
    "WorkspaceTypeDef",
    "WorkspacesIpGroupTypeDef",
)


class AccountModificationTypeDef(TypedDict, total=False):
    ModificationState: DedicatedTenancyModificationStateEnum
    DedicatedTenancySupport: DedicatedTenancySupportResultEnum
    DedicatedTenancyManagementCidrRange: str
    StartTime: datetime
    ErrorCode: str
    ErrorMessage: str


class AssociateConnectionAliasResultTypeDef(TypedDict, total=False):
    ConnectionIdentifier: str


class ClientPropertiesResultTypeDef(TypedDict, total=False):
    ResourceId: str
    ClientProperties: "ClientPropertiesTypeDef"


class ClientPropertiesTypeDef(TypedDict, total=False):
    ReconnectEnabled: ReconnectEnum


class ComputeTypeTypeDef(TypedDict, total=False):
    Name: Compute


class ConnectionAliasAssociationTypeDef(TypedDict, total=False):
    AssociationStatus: AssociationStatus
    AssociatedAccountId: str
    ResourceId: str
    ConnectionIdentifier: str


class ConnectionAliasPermissionTypeDef(TypedDict):
    SharedAccountId: str
    AllowAssociation: bool


class ConnectionAliasTypeDef(TypedDict, total=False):
    ConnectionString: str
    AliasId: str
    State: ConnectionAliasState
    OwnerAccountId: str
    Associations: List["ConnectionAliasAssociationTypeDef"]


class CopyWorkspaceImageResultTypeDef(TypedDict, total=False):
    ImageId: str


class CreateConnectionAliasResultTypeDef(TypedDict, total=False):
    AliasId: str


class CreateIpGroupResultTypeDef(TypedDict, total=False):
    GroupId: str


class CreateWorkspaceBundleResultTypeDef(TypedDict, total=False):
    WorkspaceBundle: "WorkspaceBundleTypeDef"


class CreateWorkspacesResultTypeDef(TypedDict, total=False):
    FailedRequests: List["FailedCreateWorkspaceRequestTypeDef"]
    PendingRequests: List["WorkspaceTypeDef"]


class DefaultWorkspaceCreationPropertiesTypeDef(TypedDict, total=False):
    EnableWorkDocs: bool
    EnableInternetAccess: bool
    DefaultOu: str
    CustomSecurityGroupId: str
    UserEnabledAsLocalAdministrator: bool
    EnableMaintenanceMode: bool


class DescribeAccountModificationsResultTypeDef(TypedDict, total=False):
    AccountModifications: List["AccountModificationTypeDef"]
    NextToken: str


class DescribeAccountResultTypeDef(TypedDict, total=False):
    DedicatedTenancySupport: DedicatedTenancySupportResultEnum
    DedicatedTenancyManagementCidrRange: str


class DescribeClientPropertiesResultTypeDef(TypedDict, total=False):
    ClientPropertiesList: List["ClientPropertiesResultTypeDef"]


class DescribeConnectionAliasPermissionsResultTypeDef(TypedDict, total=False):
    AliasId: str
    ConnectionAliasPermissions: List["ConnectionAliasPermissionTypeDef"]
    NextToken: str


class DescribeConnectionAliasesResultTypeDef(TypedDict, total=False):
    ConnectionAliases: List["ConnectionAliasTypeDef"]
    NextToken: str


class DescribeIpGroupsResultTypeDef(TypedDict, total=False):
    Result: List["WorkspacesIpGroupTypeDef"]
    NextToken: str


class DescribeTagsResultTypeDef(TypedDict, total=False):
    TagList: List["TagTypeDef"]


class DescribeWorkspaceBundlesResultTypeDef(TypedDict, total=False):
    Bundles: List["WorkspaceBundleTypeDef"]
    NextToken: str


class DescribeWorkspaceDirectoriesResultTypeDef(TypedDict, total=False):
    Directories: List["WorkspaceDirectoryTypeDef"]
    NextToken: str


class DescribeWorkspaceImagePermissionsResultTypeDef(TypedDict, total=False):
    ImageId: str
    ImagePermissions: List["ImagePermissionTypeDef"]
    NextToken: str


class DescribeWorkspaceImagesResultTypeDef(TypedDict, total=False):
    Images: List["WorkspaceImageTypeDef"]
    NextToken: str


class DescribeWorkspaceSnapshotsResultTypeDef(TypedDict, total=False):
    RebuildSnapshots: List["SnapshotTypeDef"]
    RestoreSnapshots: List["SnapshotTypeDef"]


class DescribeWorkspacesConnectionStatusResultTypeDef(TypedDict, total=False):
    WorkspacesConnectionStatus: List["WorkspaceConnectionStatusTypeDef"]
    NextToken: str


class DescribeWorkspacesResultTypeDef(TypedDict, total=False):
    Workspaces: List["WorkspaceTypeDef"]
    NextToken: str


class FailedCreateWorkspaceRequestTypeDef(TypedDict, total=False):
    WorkspaceRequest: "WorkspaceRequestTypeDef"
    ErrorCode: str
    ErrorMessage: str


class FailedWorkspaceChangeRequestTypeDef(TypedDict, total=False):
    WorkspaceId: str
    ErrorCode: str
    ErrorMessage: str


class ImagePermissionTypeDef(TypedDict, total=False):
    SharedAccountId: str


class ImportWorkspaceImageResultTypeDef(TypedDict, total=False):
    ImageId: str


class IpRuleItemTypeDef(TypedDict, total=False):
    ipRule: str
    ruleDesc: str


class ListAvailableManagementCidrRangesResultTypeDef(TypedDict, total=False):
    ManagementCidrRanges: List[str]
    NextToken: str


class MigrateWorkspaceResultTypeDef(TypedDict, total=False):
    SourceWorkspaceId: str
    TargetWorkspaceId: str


class ModificationStateTypeDef(TypedDict, total=False):
    Resource: ModificationResourceEnum
    State: ModificationStateEnum


OperatingSystemTypeDef = TypedDict(
    "OperatingSystemTypeDef", {"Type": OperatingSystemType}, total=False
)


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RebootRequestTypeDef(TypedDict):
    WorkspaceId: str


class RebootWorkspacesResultTypeDef(TypedDict, total=False):
    FailedRequests: List["FailedWorkspaceChangeRequestTypeDef"]


class RebuildRequestTypeDef(TypedDict):
    WorkspaceId: str


class RebuildWorkspacesResultTypeDef(TypedDict, total=False):
    FailedRequests: List["FailedWorkspaceChangeRequestTypeDef"]


class RootStorageTypeDef(TypedDict, total=False):
    Capacity: str


class SelfservicePermissionsTypeDef(TypedDict, total=False):
    RestartWorkspace: ReconnectEnum
    IncreaseVolumeSize: ReconnectEnum
    ChangeComputeType: ReconnectEnum
    SwitchRunningMode: ReconnectEnum
    RebuildWorkspace: ReconnectEnum


class SnapshotTypeDef(TypedDict, total=False):
    SnapshotTime: datetime


class StartRequestTypeDef(TypedDict, total=False):
    WorkspaceId: str


class StartWorkspacesResultTypeDef(TypedDict, total=False):
    FailedRequests: List["FailedWorkspaceChangeRequestTypeDef"]


class StopRequestTypeDef(TypedDict, total=False):
    WorkspaceId: str


class StopWorkspacesResultTypeDef(TypedDict, total=False):
    FailedRequests: List["FailedWorkspaceChangeRequestTypeDef"]


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    Value: str


class TerminateRequestTypeDef(TypedDict):
    WorkspaceId: str


class TerminateWorkspacesResultTypeDef(TypedDict, total=False):
    FailedRequests: List["FailedWorkspaceChangeRequestTypeDef"]


class UserStorageTypeDef(TypedDict, total=False):
    Capacity: str


class WorkspaceAccessPropertiesTypeDef(TypedDict, total=False):
    DeviceTypeWindows: AccessPropertyValue
    DeviceTypeOsx: AccessPropertyValue
    DeviceTypeWeb: AccessPropertyValue
    DeviceTypeIos: AccessPropertyValue
    DeviceTypeAndroid: AccessPropertyValue
    DeviceTypeChromeOs: AccessPropertyValue
    DeviceTypeZeroClient: AccessPropertyValue


class WorkspaceBundleTypeDef(TypedDict, total=False):
    BundleId: str
    Name: str
    Owner: str
    Description: str
    ImageId: str
    RootStorage: "RootStorageTypeDef"
    UserStorage: "UserStorageTypeDef"
    ComputeType: "ComputeTypeTypeDef"
    LastUpdatedTime: datetime
    CreationTime: datetime


class WorkspaceConnectionStatusTypeDef(TypedDict, total=False):
    WorkspaceId: str
    ConnectionState: ConnectionState
    ConnectionStateCheckTimestamp: datetime
    LastKnownUserConnectionTimestamp: datetime


class WorkspaceCreationPropertiesTypeDef(TypedDict, total=False):
    EnableWorkDocs: bool
    EnableInternetAccess: bool
    DefaultOu: str
    CustomSecurityGroupId: str
    UserEnabledAsLocalAdministrator: bool
    EnableMaintenanceMode: bool


class WorkspaceDirectoryTypeDef(TypedDict, total=False):
    DirectoryId: str
    Alias: str
    DirectoryName: str
    RegistrationCode: str
    SubnetIds: List[str]
    DnsIpAddresses: List[str]
    CustomerUserName: str
    IamRoleId: str
    DirectoryType: WorkspaceDirectoryType
    WorkspaceSecurityGroupId: str
    State: WorkspaceDirectoryState
    WorkspaceCreationProperties: "DefaultWorkspaceCreationPropertiesTypeDef"
    ipGroupIds: List[str]
    WorkspaceAccessProperties: "WorkspaceAccessPropertiesTypeDef"
    Tenancy: Tenancy
    SelfservicePermissions: "SelfservicePermissionsTypeDef"


class WorkspaceImageTypeDef(TypedDict, total=False):
    ImageId: str
    Name: str
    Description: str
    OperatingSystem: "OperatingSystemTypeDef"
    State: WorkspaceImageState
    RequiredTenancy: WorkspaceImageRequiredTenancy
    ErrorCode: str
    ErrorMessage: str
    Created: datetime
    OwnerAccountId: str


class WorkspacePropertiesTypeDef(TypedDict, total=False):
    RunningMode: RunningMode
    RunningModeAutoStopTimeoutInMinutes: int
    RootVolumeSizeGib: int
    UserVolumeSizeGib: int
    ComputeTypeName: Compute


class _RequiredWorkspaceRequestTypeDef(TypedDict):
    DirectoryId: str
    UserName: str
    BundleId: str


class WorkspaceRequestTypeDef(_RequiredWorkspaceRequestTypeDef, total=False):
    VolumeEncryptionKey: str
    UserVolumeEncryptionEnabled: bool
    RootVolumeEncryptionEnabled: bool
    WorkspaceProperties: "WorkspacePropertiesTypeDef"
    Tags: List["TagTypeDef"]


class WorkspaceTypeDef(TypedDict, total=False):
    WorkspaceId: str
    DirectoryId: str
    UserName: str
    IpAddress: str
    State: WorkspaceState
    BundleId: str
    SubnetId: str
    ErrorMessage: str
    ErrorCode: str
    ComputerName: str
    VolumeEncryptionKey: str
    UserVolumeEncryptionEnabled: bool
    RootVolumeEncryptionEnabled: bool
    WorkspaceProperties: "WorkspacePropertiesTypeDef"
    ModificationStates: List["ModificationStateTypeDef"]


class WorkspacesIpGroupTypeDef(TypedDict, total=False):
    groupId: str
    groupName: str
    groupDesc: str
    userRules: List["IpRuleItemTypeDef"]
