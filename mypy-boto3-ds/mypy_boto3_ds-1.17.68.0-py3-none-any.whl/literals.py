"""
Type annotations for ds service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/literals.html)

Usage::

    ```python
    from mypy_boto3_ds.literals import CertificateState

    data: CertificateState = "Deregistered"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CertificateState",
    "CertificateType",
    "ClientAuthenticationType",
    "DescribeDirectoriesPaginatorName",
    "DescribeDomainControllersPaginatorName",
    "DescribeSharedDirectoriesPaginatorName",
    "DescribeSnapshotsPaginatorName",
    "DescribeTrustsPaginatorName",
    "DirectoryEdition",
    "DirectorySize",
    "DirectoryStage",
    "DirectoryType",
    "DomainControllerStatus",
    "IpRouteStatusMsg",
    "LDAPSStatus",
    "LDAPSType",
    "ListIpRoutesPaginatorName",
    "ListLogSubscriptionsPaginatorName",
    "ListSchemaExtensionsPaginatorName",
    "ListTagsForResourcePaginatorName",
    "RadiusAuthenticationProtocol",
    "RadiusStatus",
    "RegionType",
    "ReplicationScope",
    "SchemaExtensionStatus",
    "SelectiveAuth",
    "ShareMethod",
    "ShareStatus",
    "SnapshotStatus",
    "SnapshotType",
    "TargetType",
    "TopicStatus",
    "TrustDirection",
    "TrustState",
    "TrustType",
)


CertificateState = Literal[
    "DeregisterFailed",
    "Deregistered",
    "Deregistering",
    "RegisterFailed",
    "Registered",
    "Registering",
]
CertificateType = Literal["ClientCertAuth", "ClientLDAPS"]
ClientAuthenticationType = Literal["SmartCard"]
DescribeDirectoriesPaginatorName = Literal["describe_directories"]
DescribeDomainControllersPaginatorName = Literal["describe_domain_controllers"]
DescribeSharedDirectoriesPaginatorName = Literal["describe_shared_directories"]
DescribeSnapshotsPaginatorName = Literal["describe_snapshots"]
DescribeTrustsPaginatorName = Literal["describe_trusts"]
DirectoryEdition = Literal["Enterprise", "Standard"]
DirectorySize = Literal["Large", "Small"]
DirectoryStage = Literal[
    "Active",
    "Created",
    "Creating",
    "Deleted",
    "Deleting",
    "Failed",
    "Impaired",
    "Inoperable",
    "Requested",
    "RestoreFailed",
    "Restoring",
]
DirectoryType = Literal["ADConnector", "MicrosoftAD", "SharedMicrosoftAD", "SimpleAD"]
DomainControllerStatus = Literal[
    "Active", "Creating", "Deleted", "Deleting", "Failed", "Impaired", "Restoring"
]
IpRouteStatusMsg = Literal["AddFailed", "Added", "Adding", "RemoveFailed", "Removed", "Removing"]
LDAPSStatus = Literal["Disabled", "EnableFailed", "Enabled", "Enabling"]
LDAPSType = Literal["Client"]
ListIpRoutesPaginatorName = Literal["list_ip_routes"]
ListLogSubscriptionsPaginatorName = Literal["list_log_subscriptions"]
ListSchemaExtensionsPaginatorName = Literal["list_schema_extensions"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
RadiusAuthenticationProtocol = Literal["CHAP", "MS-CHAPv1", "MS-CHAPv2", "PAP"]
RadiusStatus = Literal["Completed", "Creating", "Failed"]
RegionType = Literal["Additional", "Primary"]
ReplicationScope = Literal["Domain"]
SchemaExtensionStatus = Literal[
    "CancelInProgress",
    "Cancelled",
    "Completed",
    "CreatingSnapshot",
    "Failed",
    "Initializing",
    "Replicating",
    "RollbackInProgress",
    "UpdatingSchema",
]
SelectiveAuth = Literal["Disabled", "Enabled"]
ShareMethod = Literal["HANDSHAKE", "ORGANIZATIONS"]
ShareStatus = Literal[
    "Deleted",
    "Deleting",
    "PendingAcceptance",
    "RejectFailed",
    "Rejected",
    "Rejecting",
    "ShareFailed",
    "Shared",
    "Sharing",
]
SnapshotStatus = Literal["Completed", "Creating", "Failed"]
SnapshotType = Literal["Auto", "Manual"]
TargetType = Literal["ACCOUNT"]
TopicStatus = Literal["Deleted", "Failed", "Registered", "Topic not found"]
TrustDirection = Literal["One-Way: Incoming", "One-Way: Outgoing", "Two-Way"]
TrustState = Literal[
    "Created",
    "Creating",
    "Deleted",
    "Deleting",
    "Failed",
    "UpdateFailed",
    "Updated",
    "Updating",
    "Verified",
    "VerifyFailed",
    "Verifying",
]
TrustType = Literal["External", "Forest"]
