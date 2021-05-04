"""
Type annotations for appstream service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appstream/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appstream.type_defs import AccessEndpointTypeDef

    data: AccessEndpointTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_appstream.literals import (
    Action,
    AuthenticationType,
    FleetErrorCode,
    FleetState,
    FleetType,
    ImageBuilderState,
    ImageBuilderStateChangeReasonCode,
    ImageState,
    ImageStateChangeReasonCode,
    Permission,
    PlatformType,
    SessionConnectionState,
    SessionState,
    StackErrorCode,
    StorageConnectorType,
    StreamView,
    UsageReportExecutionErrorCode,
    UserStackAssociationErrorCode,
    VisibilityType,
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
    "AccessEndpointTypeDef",
    "ApplicationSettingsResponseTypeDef",
    "ApplicationSettingsTypeDef",
    "ApplicationTypeDef",
    "BatchAssociateUserStackResultTypeDef",
    "BatchDisassociateUserStackResultTypeDef",
    "ComputeCapacityStatusTypeDef",
    "ComputeCapacityTypeDef",
    "CopyImageResponseTypeDef",
    "CreateDirectoryConfigResultTypeDef",
    "CreateFleetResultTypeDef",
    "CreateImageBuilderResultTypeDef",
    "CreateImageBuilderStreamingURLResultTypeDef",
    "CreateStackResultTypeDef",
    "CreateStreamingURLResultTypeDef",
    "CreateUpdatedImageResultTypeDef",
    "CreateUsageReportSubscriptionResultTypeDef",
    "DeleteImageBuilderResultTypeDef",
    "DeleteImageResultTypeDef",
    "DescribeDirectoryConfigsResultTypeDef",
    "DescribeFleetsResultTypeDef",
    "DescribeImageBuildersResultTypeDef",
    "DescribeImagePermissionsResultTypeDef",
    "DescribeImagesResultTypeDef",
    "DescribeSessionsResultTypeDef",
    "DescribeStacksResultTypeDef",
    "DescribeUsageReportSubscriptionsResultTypeDef",
    "DescribeUserStackAssociationsResultTypeDef",
    "DescribeUsersResultTypeDef",
    "DirectoryConfigTypeDef",
    "DomainJoinInfoTypeDef",
    "FleetErrorTypeDef",
    "FleetTypeDef",
    "ImageBuilderStateChangeReasonTypeDef",
    "ImageBuilderTypeDef",
    "ImagePermissionsTypeDef",
    "ImageStateChangeReasonTypeDef",
    "ImageTypeDef",
    "LastReportGenerationExecutionErrorTypeDef",
    "ListAssociatedFleetsResultTypeDef",
    "ListAssociatedStacksResultTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkAccessConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceErrorTypeDef",
    "ServiceAccountCredentialsTypeDef",
    "SessionTypeDef",
    "SharedImagePermissionsTypeDef",
    "StackErrorTypeDef",
    "StackTypeDef",
    "StartImageBuilderResultTypeDef",
    "StopImageBuilderResultTypeDef",
    "StorageConnectorTypeDef",
    "UpdateDirectoryConfigResultTypeDef",
    "UpdateFleetResultTypeDef",
    "UpdateStackResultTypeDef",
    "UsageReportSubscriptionTypeDef",
    "UserSettingTypeDef",
    "UserStackAssociationErrorTypeDef",
    "UserStackAssociationTypeDef",
    "UserTypeDef",
    "VpcConfigTypeDef",
    "WaiterConfigTypeDef",
)


class _RequiredAccessEndpointTypeDef(TypedDict):
    EndpointType: Literal["STREAMING"]


class AccessEndpointTypeDef(_RequiredAccessEndpointTypeDef, total=False):
    VpceId: str


class ApplicationSettingsResponseTypeDef(TypedDict, total=False):
    Enabled: bool
    SettingsGroup: str
    S3BucketName: str


class _RequiredApplicationSettingsTypeDef(TypedDict):
    Enabled: bool


class ApplicationSettingsTypeDef(_RequiredApplicationSettingsTypeDef, total=False):
    SettingsGroup: str


class ApplicationTypeDef(TypedDict, total=False):
    Name: str
    DisplayName: str
    IconURL: str
    LaunchPath: str
    LaunchParameters: str
    Enabled: bool
    Metadata: Dict[str, str]


class BatchAssociateUserStackResultTypeDef(TypedDict, total=False):
    errors: List["UserStackAssociationErrorTypeDef"]


class BatchDisassociateUserStackResultTypeDef(TypedDict, total=False):
    errors: List["UserStackAssociationErrorTypeDef"]


class _RequiredComputeCapacityStatusTypeDef(TypedDict):
    Desired: int


class ComputeCapacityStatusTypeDef(_RequiredComputeCapacityStatusTypeDef, total=False):
    Running: int
    InUse: int
    Available: int


class ComputeCapacityTypeDef(TypedDict):
    DesiredInstances: int


class CopyImageResponseTypeDef(TypedDict, total=False):
    DestinationImageName: str


class CreateDirectoryConfigResultTypeDef(TypedDict, total=False):
    DirectoryConfig: "DirectoryConfigTypeDef"


class CreateFleetResultTypeDef(TypedDict, total=False):
    Fleet: "FleetTypeDef"


class CreateImageBuilderResultTypeDef(TypedDict, total=False):
    ImageBuilder: "ImageBuilderTypeDef"


class CreateImageBuilderStreamingURLResultTypeDef(TypedDict, total=False):
    StreamingURL: str
    Expires: datetime


class CreateStackResultTypeDef(TypedDict, total=False):
    Stack: "StackTypeDef"


class CreateStreamingURLResultTypeDef(TypedDict, total=False):
    StreamingURL: str
    Expires: datetime


class CreateUpdatedImageResultTypeDef(TypedDict, total=False):
    image: "ImageTypeDef"
    canUpdateImage: bool


class CreateUsageReportSubscriptionResultTypeDef(TypedDict, total=False):
    S3BucketName: str
    Schedule: Literal["DAILY"]


class DeleteImageBuilderResultTypeDef(TypedDict, total=False):
    ImageBuilder: "ImageBuilderTypeDef"


class DeleteImageResultTypeDef(TypedDict, total=False):
    Image: "ImageTypeDef"


class DescribeDirectoryConfigsResultTypeDef(TypedDict, total=False):
    DirectoryConfigs: List["DirectoryConfigTypeDef"]
    NextToken: str


class DescribeFleetsResultTypeDef(TypedDict, total=False):
    Fleets: List["FleetTypeDef"]
    NextToken: str


class DescribeImageBuildersResultTypeDef(TypedDict, total=False):
    ImageBuilders: List["ImageBuilderTypeDef"]
    NextToken: str


class DescribeImagePermissionsResultTypeDef(TypedDict, total=False):
    Name: str
    SharedImagePermissionsList: List["SharedImagePermissionsTypeDef"]
    NextToken: str


class DescribeImagesResultTypeDef(TypedDict, total=False):
    Images: List["ImageTypeDef"]
    NextToken: str


class DescribeSessionsResultTypeDef(TypedDict, total=False):
    Sessions: List["SessionTypeDef"]
    NextToken: str


class DescribeStacksResultTypeDef(TypedDict, total=False):
    Stacks: List["StackTypeDef"]
    NextToken: str


class DescribeUsageReportSubscriptionsResultTypeDef(TypedDict, total=False):
    UsageReportSubscriptions: List["UsageReportSubscriptionTypeDef"]
    NextToken: str


class DescribeUserStackAssociationsResultTypeDef(TypedDict, total=False):
    UserStackAssociations: List["UserStackAssociationTypeDef"]
    NextToken: str


class DescribeUsersResultTypeDef(TypedDict, total=False):
    Users: List["UserTypeDef"]
    NextToken: str


class _RequiredDirectoryConfigTypeDef(TypedDict):
    DirectoryName: str


class DirectoryConfigTypeDef(_RequiredDirectoryConfigTypeDef, total=False):
    OrganizationalUnitDistinguishedNames: List[str]
    ServiceAccountCredentials: "ServiceAccountCredentialsTypeDef"
    CreatedTime: datetime


class DomainJoinInfoTypeDef(TypedDict, total=False):
    DirectoryName: str
    OrganizationalUnitDistinguishedName: str


class FleetErrorTypeDef(TypedDict, total=False):
    ErrorCode: FleetErrorCode
    ErrorMessage: str


class _RequiredFleetTypeDef(TypedDict):
    Arn: str
    Name: str
    InstanceType: str
    ComputeCapacityStatus: "ComputeCapacityStatusTypeDef"
    State: FleetState


class FleetTypeDef(_RequiredFleetTypeDef, total=False):
    DisplayName: str
    Description: str
    ImageName: str
    ImageArn: str
    FleetType: FleetType
    MaxUserDurationInSeconds: int
    DisconnectTimeoutInSeconds: int
    VpcConfig: "VpcConfigTypeDef"
    CreatedTime: datetime
    FleetErrors: List["FleetErrorTypeDef"]
    EnableDefaultInternetAccess: bool
    DomainJoinInfo: "DomainJoinInfoTypeDef"
    IdleDisconnectTimeoutInSeconds: int
    IamRoleArn: str
    StreamView: StreamView


class ImageBuilderStateChangeReasonTypeDef(TypedDict, total=False):
    Code: ImageBuilderStateChangeReasonCode
    Message: str


class _RequiredImageBuilderTypeDef(TypedDict):
    Name: str


class ImageBuilderTypeDef(_RequiredImageBuilderTypeDef, total=False):
    Arn: str
    ImageArn: str
    Description: str
    DisplayName: str
    VpcConfig: "VpcConfigTypeDef"
    InstanceType: str
    Platform: PlatformType
    IamRoleArn: str
    State: ImageBuilderState
    StateChangeReason: "ImageBuilderStateChangeReasonTypeDef"
    CreatedTime: datetime
    EnableDefaultInternetAccess: bool
    DomainJoinInfo: "DomainJoinInfoTypeDef"
    NetworkAccessConfiguration: "NetworkAccessConfigurationTypeDef"
    ImageBuilderErrors: List["ResourceErrorTypeDef"]
    AppstreamAgentVersion: str
    AccessEndpoints: List["AccessEndpointTypeDef"]


class ImagePermissionsTypeDef(TypedDict, total=False):
    allowFleet: bool
    allowImageBuilder: bool


class ImageStateChangeReasonTypeDef(TypedDict, total=False):
    Code: ImageStateChangeReasonCode
    Message: str


class _RequiredImageTypeDef(TypedDict):
    Name: str


class ImageTypeDef(_RequiredImageTypeDef, total=False):
    Arn: str
    BaseImageArn: str
    DisplayName: str
    State: ImageState
    Visibility: VisibilityType
    ImageBuilderSupported: bool
    ImageBuilderName: str
    Platform: PlatformType
    Description: str
    StateChangeReason: "ImageStateChangeReasonTypeDef"
    Applications: List["ApplicationTypeDef"]
    CreatedTime: datetime
    PublicBaseImageReleasedDate: datetime
    AppstreamAgentVersion: str
    ImagePermissions: "ImagePermissionsTypeDef"
    ImageErrors: List["ResourceErrorTypeDef"]


class LastReportGenerationExecutionErrorTypeDef(TypedDict, total=False):
    ErrorCode: UsageReportExecutionErrorCode
    ErrorMessage: str


class ListAssociatedFleetsResultTypeDef(TypedDict, total=False):
    Names: List[str]
    NextToken: str


class ListAssociatedStacksResultTypeDef(TypedDict, total=False):
    Names: List[str]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class NetworkAccessConfigurationTypeDef(TypedDict, total=False):
    EniPrivateIpAddress: str
    EniId: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ResourceErrorTypeDef(TypedDict, total=False):
    ErrorCode: FleetErrorCode
    ErrorMessage: str
    ErrorTimestamp: datetime


class ServiceAccountCredentialsTypeDef(TypedDict):
    AccountName: str
    AccountPassword: str


class _RequiredSessionTypeDef(TypedDict):
    Id: str
    UserId: str
    StackName: str
    FleetName: str
    State: SessionState


class SessionTypeDef(_RequiredSessionTypeDef, total=False):
    ConnectionState: SessionConnectionState
    StartTime: datetime
    MaxExpirationTime: datetime
    AuthenticationType: AuthenticationType
    NetworkAccessConfiguration: "NetworkAccessConfigurationTypeDef"


class SharedImagePermissionsTypeDef(TypedDict):
    sharedAccountId: str
    imagePermissions: "ImagePermissionsTypeDef"


class StackErrorTypeDef(TypedDict, total=False):
    ErrorCode: StackErrorCode
    ErrorMessage: str


class _RequiredStackTypeDef(TypedDict):
    Name: str


class StackTypeDef(_RequiredStackTypeDef, total=False):
    Arn: str
    Description: str
    DisplayName: str
    CreatedTime: datetime
    StorageConnectors: List["StorageConnectorTypeDef"]
    RedirectURL: str
    FeedbackURL: str
    StackErrors: List["StackErrorTypeDef"]
    UserSettings: List["UserSettingTypeDef"]
    ApplicationSettings: "ApplicationSettingsResponseTypeDef"
    AccessEndpoints: List["AccessEndpointTypeDef"]
    EmbedHostDomains: List[str]


class StartImageBuilderResultTypeDef(TypedDict, total=False):
    ImageBuilder: "ImageBuilderTypeDef"


class StopImageBuilderResultTypeDef(TypedDict, total=False):
    ImageBuilder: "ImageBuilderTypeDef"


class _RequiredStorageConnectorTypeDef(TypedDict):
    ConnectorType: StorageConnectorType


class StorageConnectorTypeDef(_RequiredStorageConnectorTypeDef, total=False):
    ResourceIdentifier: str
    Domains: List[str]


class UpdateDirectoryConfigResultTypeDef(TypedDict, total=False):
    DirectoryConfig: "DirectoryConfigTypeDef"


class UpdateFleetResultTypeDef(TypedDict, total=False):
    Fleet: "FleetTypeDef"


class UpdateStackResultTypeDef(TypedDict, total=False):
    Stack: "StackTypeDef"


class UsageReportSubscriptionTypeDef(TypedDict, total=False):
    S3BucketName: str
    Schedule: Literal["DAILY"]
    LastGeneratedReportDate: datetime
    SubscriptionErrors: List["LastReportGenerationExecutionErrorTypeDef"]


class UserSettingTypeDef(TypedDict):
    Action: Action
    Permission: Permission


class UserStackAssociationErrorTypeDef(TypedDict, total=False):
    UserStackAssociation: "UserStackAssociationTypeDef"
    ErrorCode: UserStackAssociationErrorCode
    ErrorMessage: str


class _RequiredUserStackAssociationTypeDef(TypedDict):
    StackName: str
    UserName: str
    AuthenticationType: AuthenticationType


class UserStackAssociationTypeDef(_RequiredUserStackAssociationTypeDef, total=False):
    SendEmailNotification: bool


class _RequiredUserTypeDef(TypedDict):
    AuthenticationType: AuthenticationType


class UserTypeDef(_RequiredUserTypeDef, total=False):
    Arn: str
    UserName: str
    Enabled: bool
    Status: str
    FirstName: str
    LastName: str
    CreatedTime: datetime


class VpcConfigTypeDef(TypedDict, total=False):
    SubnetIds: List[str]
    SecurityGroupIds: List[str]


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
