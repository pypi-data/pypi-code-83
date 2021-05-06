"""
Type annotations for workspaces service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workspaces/literals.html)

Usage::

    ```python
    from mypy_boto3_workspaces.literals import AccessPropertyValue

    data: AccessPropertyValue = "ALLOW"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccessPropertyValue",
    "Application",
    "AssociationStatus",
    "Compute",
    "ConnectionAliasState",
    "ConnectionState",
    "DedicatedTenancyModificationStateEnum",
    "DedicatedTenancySupportEnum",
    "DedicatedTenancySupportResultEnum",
    "DescribeAccountModificationsPaginatorName",
    "DescribeIpGroupsPaginatorName",
    "DescribeWorkspaceBundlesPaginatorName",
    "DescribeWorkspaceDirectoriesPaginatorName",
    "DescribeWorkspaceImagesPaginatorName",
    "DescribeWorkspacesConnectionStatusPaginatorName",
    "DescribeWorkspacesPaginatorName",
    "ImageType",
    "ListAvailableManagementCidrRangesPaginatorName",
    "ModificationResourceEnum",
    "ModificationStateEnum",
    "OperatingSystemType",
    "ReconnectEnum",
    "RunningMode",
    "TargetWorkspaceState",
    "Tenancy",
    "WorkspaceDirectoryState",
    "WorkspaceDirectoryType",
    "WorkspaceImageIngestionProcess",
    "WorkspaceImageRequiredTenancy",
    "WorkspaceImageState",
    "WorkspaceState",
)


AccessPropertyValue = Literal["ALLOW", "DENY"]
Application = Literal["Microsoft_Office_2016", "Microsoft_Office_2019"]
AssociationStatus = Literal[
    "ASSOCIATED_WITH_OWNER_ACCOUNT",
    "ASSOCIATED_WITH_SHARED_ACCOUNT",
    "NOT_ASSOCIATED",
    "PENDING_ASSOCIATION",
    "PENDING_DISASSOCIATION",
]
Compute = Literal[
    "GRAPHICS", "GRAPHICSPRO", "PERFORMANCE", "POWER", "POWERPRO", "STANDARD", "VALUE"
]
ConnectionAliasState = Literal["CREATED", "CREATING", "DELETING"]
ConnectionState = Literal["CONNECTED", "DISCONNECTED", "UNKNOWN"]
DedicatedTenancyModificationStateEnum = Literal["COMPLETED", "FAILED", "PENDING"]
DedicatedTenancySupportEnum = Literal["ENABLED"]
DedicatedTenancySupportResultEnum = Literal["DISABLED", "ENABLED"]
DescribeAccountModificationsPaginatorName = Literal["describe_account_modifications"]
DescribeIpGroupsPaginatorName = Literal["describe_ip_groups"]
DescribeWorkspaceBundlesPaginatorName = Literal["describe_workspace_bundles"]
DescribeWorkspaceDirectoriesPaginatorName = Literal["describe_workspace_directories"]
DescribeWorkspaceImagesPaginatorName = Literal["describe_workspace_images"]
DescribeWorkspacesConnectionStatusPaginatorName = Literal["describe_workspaces_connection_status"]
DescribeWorkspacesPaginatorName = Literal["describe_workspaces"]
ImageType = Literal["OWNED", "SHARED"]
ListAvailableManagementCidrRangesPaginatorName = Literal["list_available_management_cidr_ranges"]
ModificationResourceEnum = Literal["COMPUTE_TYPE", "ROOT_VOLUME", "USER_VOLUME"]
ModificationStateEnum = Literal["UPDATE_INITIATED", "UPDATE_IN_PROGRESS"]
OperatingSystemType = Literal["LINUX", "WINDOWS"]
ReconnectEnum = Literal["DISABLED", "ENABLED"]
RunningMode = Literal["ALWAYS_ON", "AUTO_STOP"]
TargetWorkspaceState = Literal["ADMIN_MAINTENANCE", "AVAILABLE"]
Tenancy = Literal["DEDICATED", "SHARED"]
WorkspaceDirectoryState = Literal[
    "DEREGISTERED", "DEREGISTERING", "ERROR", "REGISTERED", "REGISTERING"
]
WorkspaceDirectoryType = Literal["AD_CONNECTOR", "SIMPLE_AD"]
WorkspaceImageIngestionProcess = Literal[
    "BYOL_GRAPHICS", "BYOL_GRAPHICSPRO", "BYOL_REGULAR", "BYOL_REGULAR_WSP"
]
WorkspaceImageRequiredTenancy = Literal["DEDICATED", "DEFAULT"]
WorkspaceImageState = Literal["AVAILABLE", "ERROR", "PENDING"]
WorkspaceState = Literal[
    "ADMIN_MAINTENANCE",
    "AVAILABLE",
    "ERROR",
    "IMPAIRED",
    "MAINTENANCE",
    "PENDING",
    "REBOOTING",
    "REBUILDING",
    "RESTORING",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "SUSPENDED",
    "TERMINATED",
    "TERMINATING",
    "UNHEALTHY",
    "UPDATING",
]
