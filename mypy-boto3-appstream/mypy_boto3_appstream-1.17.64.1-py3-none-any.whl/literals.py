"""
Type annotations for appstream service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/literals.html)

Usage::

    ```python
    from mypy_boto3_appstream.literals import AccessEndpointType

    data: AccessEndpointType = "STREAMING"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccessEndpointType",
    "Action",
    "AuthenticationType",
    "DescribeDirectoryConfigsPaginatorName",
    "DescribeFleetsPaginatorName",
    "DescribeImageBuildersPaginatorName",
    "DescribeImagesPaginatorName",
    "DescribeSessionsPaginatorName",
    "DescribeStacksPaginatorName",
    "DescribeUserStackAssociationsPaginatorName",
    "DescribeUsersPaginatorName",
    "FleetAttribute",
    "FleetErrorCode",
    "FleetStartedWaiterName",
    "FleetState",
    "FleetStoppedWaiterName",
    "FleetType",
    "ImageBuilderState",
    "ImageBuilderStateChangeReasonCode",
    "ImageState",
    "ImageStateChangeReasonCode",
    "ListAssociatedFleetsPaginatorName",
    "ListAssociatedStacksPaginatorName",
    "MessageAction",
    "Permission",
    "PlatformType",
    "SessionConnectionState",
    "SessionState",
    "StackAttribute",
    "StackErrorCode",
    "StorageConnectorType",
    "StreamView",
    "UsageReportExecutionErrorCode",
    "UsageReportSchedule",
    "UserStackAssociationErrorCode",
    "VisibilityType",
)


AccessEndpointType = Literal["STREAMING"]
Action = Literal[
    "CLIPBOARD_COPY_FROM_LOCAL_DEVICE",
    "CLIPBOARD_COPY_TO_LOCAL_DEVICE",
    "DOMAIN_PASSWORD_SIGNIN",
    "DOMAIN_SMART_CARD_SIGNIN",
    "FILE_DOWNLOAD",
    "FILE_UPLOAD",
    "PRINTING_TO_LOCAL_DEVICE",
]
AuthenticationType = Literal["API", "SAML", "USERPOOL"]
DescribeDirectoryConfigsPaginatorName = Literal["describe_directory_configs"]
DescribeFleetsPaginatorName = Literal["describe_fleets"]
DescribeImageBuildersPaginatorName = Literal["describe_image_builders"]
DescribeImagesPaginatorName = Literal["describe_images"]
DescribeSessionsPaginatorName = Literal["describe_sessions"]
DescribeStacksPaginatorName = Literal["describe_stacks"]
DescribeUserStackAssociationsPaginatorName = Literal["describe_user_stack_associations"]
DescribeUsersPaginatorName = Literal["describe_users"]
FleetAttribute = Literal[
    "DOMAIN_JOIN_INFO", "IAM_ROLE_ARN", "VPC_CONFIGURATION", "VPC_CONFIGURATION_SECURITY_GROUP_IDS"
]
FleetErrorCode = Literal[
    "DOMAIN_JOIN_ERROR_ACCESS_DENIED",
    "DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED",
    "DOMAIN_JOIN_ERROR_FILE_NOT_FOUND",
    "DOMAIN_JOIN_ERROR_INVALID_PARAMETER",
    "DOMAIN_JOIN_ERROR_LOGON_FAILURE",
    "DOMAIN_JOIN_ERROR_MORE_DATA",
    "DOMAIN_JOIN_ERROR_NOT_SUPPORTED",
    "DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN",
    "DOMAIN_JOIN_INTERNAL_SERVICE_ERROR",
    "DOMAIN_JOIN_NERR_INVALID_WORKGROUP_NAME",
    "DOMAIN_JOIN_NERR_PASSWORD_EXPIRED",
    "DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED",
    "FLEET_INSTANCE_PROVISIONING_FAILURE",
    "FLEET_STOPPED",
    "IAM_SERVICE_ROLE_IS_MISSING",
    "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SECURITY_GROUPS_ACTION",
    "IAM_SERVICE_ROLE_MISSING_DESCRIBE_SUBNET_ACTION",
    "IAM_SERVICE_ROLE_MISSING_ENI_CREATE_ACTION",
    "IAM_SERVICE_ROLE_MISSING_ENI_DELETE_ACTION",
    "IAM_SERVICE_ROLE_MISSING_ENI_DESCRIBE_ACTION",
    "IGW_NOT_ATTACHED",
    "IMAGE_NOT_FOUND",
    "INTERNAL_SERVICE_ERROR",
    "INVALID_SUBNET_CONFIGURATION",
    "MACHINE_ROLE_IS_MISSING",
    "NETWORK_INTERFACE_LIMIT_EXCEEDED",
    "SECURITY_GROUPS_NOT_FOUND",
    "STS_DISABLED_IN_REGION",
    "SUBNET_HAS_INSUFFICIENT_IP_ADDRESSES",
    "SUBNET_NOT_FOUND",
]
FleetStartedWaiterName = Literal["fleet_started"]
FleetState = Literal["RUNNING", "STARTING", "STOPPED", "STOPPING"]
FleetStoppedWaiterName = Literal["fleet_stopped"]
FleetType = Literal["ALWAYS_ON", "ON_DEMAND"]
ImageBuilderState = Literal[
    "DELETING",
    "FAILED",
    "PENDING",
    "PENDING_QUALIFICATION",
    "REBOOTING",
    "RUNNING",
    "SNAPSHOTTING",
    "STOPPED",
    "STOPPING",
    "UPDATING",
    "UPDATING_AGENT",
]
ImageBuilderStateChangeReasonCode = Literal["IMAGE_UNAVAILABLE", "INTERNAL_ERROR"]
ImageState = Literal[
    "AVAILABLE", "COPYING", "CREATING", "DELETING", "FAILED", "IMPORTING", "PENDING"
]
ImageStateChangeReasonCode = Literal[
    "IMAGE_BUILDER_NOT_AVAILABLE", "IMAGE_COPY_FAILURE", "INTERNAL_ERROR"
]
ListAssociatedFleetsPaginatorName = Literal["list_associated_fleets"]
ListAssociatedStacksPaginatorName = Literal["list_associated_stacks"]
MessageAction = Literal["RESEND", "SUPPRESS"]
Permission = Literal["DISABLED", "ENABLED"]
PlatformType = Literal["WINDOWS", "WINDOWS_SERVER_2016", "WINDOWS_SERVER_2019"]
SessionConnectionState = Literal["CONNECTED", "NOT_CONNECTED"]
SessionState = Literal["ACTIVE", "EXPIRED", "PENDING"]
StackAttribute = Literal[
    "ACCESS_ENDPOINTS",
    "EMBED_HOST_DOMAINS",
    "FEEDBACK_URL",
    "IAM_ROLE_ARN",
    "REDIRECT_URL",
    "STORAGE_CONNECTORS",
    "STORAGE_CONNECTOR_GOOGLE_DRIVE",
    "STORAGE_CONNECTOR_HOMEFOLDERS",
    "STORAGE_CONNECTOR_ONE_DRIVE",
    "THEME_NAME",
    "USER_SETTINGS",
]
StackErrorCode = Literal["INTERNAL_SERVICE_ERROR", "STORAGE_CONNECTOR_ERROR"]
StorageConnectorType = Literal["GOOGLE_DRIVE", "HOMEFOLDERS", "ONE_DRIVE"]
StreamView = Literal["APP", "DESKTOP"]
UsageReportExecutionErrorCode = Literal[
    "ACCESS_DENIED", "INTERNAL_SERVICE_ERROR", "RESOURCE_NOT_FOUND"
]
UsageReportSchedule = Literal["DAILY"]
UserStackAssociationErrorCode = Literal[
    "DIRECTORY_NOT_FOUND", "INTERNAL_ERROR", "STACK_NOT_FOUND", "USER_NAME_NOT_FOUND"
]
VisibilityType = Literal["PRIVATE", "PUBLIC", "SHARED"]
