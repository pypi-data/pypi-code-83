"""
Type annotations for connect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_connect.type_defs import AssociateInstanceStorageConfigResponseTypeDef

    data: AssociateInstanceStorageConfigResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_connect.literals import (
    Channel,
    ContactFlowType,
    CurrentMetricName,
    DirectoryType,
    HistoricalMetricName,
    HoursOfOperationDays,
    InstanceAttributeType,
    InstanceStatus,
    PhoneNumberCountryCode,
    PhoneNumberType,
    PhoneType,
    QueueStatus,
    QueueType,
    QuickConnectType,
    SourceType,
    Statistic,
    StorageType,
    Unit,
    VoiceRecordingTrack,
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
    "AssociateInstanceStorageConfigResponseTypeDef",
    "AssociateSecurityKeyResponseTypeDef",
    "AttributeTypeDef",
    "ChatMessageTypeDef",
    "ContactFlowSummaryTypeDef",
    "ContactFlowTypeDef",
    "CreateContactFlowResponseTypeDef",
    "CreateInstanceResponseTypeDef",
    "CreateIntegrationAssociationResponseTypeDef",
    "CreateQueueResponseTypeDef",
    "CreateQuickConnectResponseTypeDef",
    "CreateRoutingProfileResponseTypeDef",
    "CreateUseCaseResponseTypeDef",
    "CreateUserHierarchyGroupResponseTypeDef",
    "CreateUserResponseTypeDef",
    "CredentialsTypeDef",
    "CurrentMetricDataTypeDef",
    "CurrentMetricResultTypeDef",
    "CurrentMetricTypeDef",
    "DescribeContactFlowResponseTypeDef",
    "DescribeHoursOfOperationResponseTypeDef",
    "DescribeInstanceAttributeResponseTypeDef",
    "DescribeInstanceResponseTypeDef",
    "DescribeInstanceStorageConfigResponseTypeDef",
    "DescribeQueueResponseTypeDef",
    "DescribeQuickConnectResponseTypeDef",
    "DescribeRoutingProfileResponseTypeDef",
    "DescribeUserHierarchyGroupResponseTypeDef",
    "DescribeUserHierarchyStructureResponseTypeDef",
    "DescribeUserResponseTypeDef",
    "DimensionsTypeDef",
    "EncryptionConfigTypeDef",
    "FiltersTypeDef",
    "GetContactAttributesResponseTypeDef",
    "GetCurrentMetricDataResponseTypeDef",
    "GetFederationTokenResponseTypeDef",
    "GetMetricDataResponseTypeDef",
    "HierarchyGroupSummaryTypeDef",
    "HierarchyGroupTypeDef",
    "HierarchyLevelTypeDef",
    "HierarchyLevelUpdateTypeDef",
    "HierarchyPathTypeDef",
    "HierarchyStructureTypeDef",
    "HierarchyStructureUpdateTypeDef",
    "HistoricalMetricDataTypeDef",
    "HistoricalMetricResultTypeDef",
    "HistoricalMetricTypeDef",
    "HoursOfOperationConfigTypeDef",
    "HoursOfOperationSummaryTypeDef",
    "HoursOfOperationTimeSliceTypeDef",
    "HoursOfOperationTypeDef",
    "InstanceStatusReasonTypeDef",
    "InstanceStorageConfigTypeDef",
    "InstanceSummaryTypeDef",
    "InstanceTypeDef",
    "IntegrationAssociationSummaryTypeDef",
    "KinesisFirehoseConfigTypeDef",
    "KinesisStreamConfigTypeDef",
    "KinesisVideoStreamConfigTypeDef",
    "LexBotTypeDef",
    "ListApprovedOriginsResponseTypeDef",
    "ListContactFlowsResponseTypeDef",
    "ListHoursOfOperationsResponseTypeDef",
    "ListInstanceAttributesResponseTypeDef",
    "ListInstanceStorageConfigsResponseTypeDef",
    "ListInstancesResponseTypeDef",
    "ListIntegrationAssociationsResponseTypeDef",
    "ListLambdaFunctionsResponseTypeDef",
    "ListLexBotsResponseTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "ListPromptsResponseTypeDef",
    "ListQueueQuickConnectsResponseTypeDef",
    "ListQueuesResponseTypeDef",
    "ListQuickConnectsResponseTypeDef",
    "ListRoutingProfileQueuesResponseTypeDef",
    "ListRoutingProfilesResponseTypeDef",
    "ListSecurityKeysResponseTypeDef",
    "ListSecurityProfilesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUseCasesResponseTypeDef",
    "ListUserHierarchyGroupsResponseTypeDef",
    "ListUsersResponseTypeDef",
    "MediaConcurrencyTypeDef",
    "OutboundCallerConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantDetailsTypeDef",
    "PhoneNumberQuickConnectConfigTypeDef",
    "PhoneNumberSummaryTypeDef",
    "PromptSummaryTypeDef",
    "QueueQuickConnectConfigTypeDef",
    "QueueReferenceTypeDef",
    "QueueSummaryTypeDef",
    "QueueTypeDef",
    "QuickConnectConfigTypeDef",
    "QuickConnectSummaryTypeDef",
    "QuickConnectTypeDef",
    "ReferenceTypeDef",
    "RoutingProfileQueueConfigSummaryTypeDef",
    "RoutingProfileQueueConfigTypeDef",
    "RoutingProfileQueueReferenceTypeDef",
    "RoutingProfileSummaryTypeDef",
    "RoutingProfileTypeDef",
    "S3ConfigTypeDef",
    "SecurityKeyTypeDef",
    "SecurityProfileSummaryTypeDef",
    "StartChatContactResponseTypeDef",
    "StartOutboundVoiceContactResponseTypeDef",
    "StartTaskContactResponseTypeDef",
    "ThresholdTypeDef",
    "UseCaseTypeDef",
    "UserIdentityInfoTypeDef",
    "UserPhoneConfigTypeDef",
    "UserQuickConnectConfigTypeDef",
    "UserSummaryTypeDef",
    "UserTypeDef",
    "VoiceRecordingConfigurationTypeDef",
)


class AssociateInstanceStorageConfigResponseTypeDef(TypedDict, total=False):
    AssociationId: str


class AssociateSecurityKeyResponseTypeDef(TypedDict, total=False):
    AssociationId: str


class AttributeTypeDef(TypedDict, total=False):
    AttributeType: InstanceAttributeType
    Value: str


class ChatMessageTypeDef(TypedDict):
    ContentType: str
    Content: str


class ContactFlowSummaryTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str
    ContactFlowType: ContactFlowType


ContactFlowTypeDef = TypedDict(
    "ContactFlowTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Name": str,
        "Type": ContactFlowType,
        "Description": str,
        "Content": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class CreateContactFlowResponseTypeDef(TypedDict, total=False):
    ContactFlowId: str
    ContactFlowArn: str


class CreateInstanceResponseTypeDef(TypedDict, total=False):
    Id: str
    Arn: str


class CreateIntegrationAssociationResponseTypeDef(TypedDict, total=False):
    IntegrationAssociationId: str
    IntegrationAssociationArn: str


class CreateQueueResponseTypeDef(TypedDict, total=False):
    QueueArn: str
    QueueId: str


class CreateQuickConnectResponseTypeDef(TypedDict, total=False):
    QuickConnectARN: str
    QuickConnectId: str


class CreateRoutingProfileResponseTypeDef(TypedDict, total=False):
    RoutingProfileArn: str
    RoutingProfileId: str


class CreateUseCaseResponseTypeDef(TypedDict, total=False):
    UseCaseId: str
    UseCaseArn: str


class CreateUserHierarchyGroupResponseTypeDef(TypedDict, total=False):
    HierarchyGroupId: str
    HierarchyGroupArn: str


class CreateUserResponseTypeDef(TypedDict, total=False):
    UserId: str
    UserArn: str


class CredentialsTypeDef(TypedDict, total=False):
    AccessToken: str
    AccessTokenExpiration: datetime
    RefreshToken: str
    RefreshTokenExpiration: datetime


class CurrentMetricDataTypeDef(TypedDict, total=False):
    Metric: "CurrentMetricTypeDef"
    Value: float


class CurrentMetricResultTypeDef(TypedDict, total=False):
    Dimensions: "DimensionsTypeDef"
    Collections: List["CurrentMetricDataTypeDef"]


class CurrentMetricTypeDef(TypedDict, total=False):
    Name: CurrentMetricName
    Unit: Unit


class DescribeContactFlowResponseTypeDef(TypedDict, total=False):
    ContactFlow: "ContactFlowTypeDef"


class DescribeHoursOfOperationResponseTypeDef(TypedDict, total=False):
    HoursOfOperation: "HoursOfOperationTypeDef"


class DescribeInstanceAttributeResponseTypeDef(TypedDict, total=False):
    Attribute: "AttributeTypeDef"


class DescribeInstanceResponseTypeDef(TypedDict, total=False):
    Instance: "InstanceTypeDef"


class DescribeInstanceStorageConfigResponseTypeDef(TypedDict, total=False):
    StorageConfig: "InstanceStorageConfigTypeDef"


class DescribeQueueResponseTypeDef(TypedDict, total=False):
    Queue: "QueueTypeDef"


class DescribeQuickConnectResponseTypeDef(TypedDict, total=False):
    QuickConnect: "QuickConnectTypeDef"


class DescribeRoutingProfileResponseTypeDef(TypedDict, total=False):
    RoutingProfile: "RoutingProfileTypeDef"


class DescribeUserHierarchyGroupResponseTypeDef(TypedDict, total=False):
    HierarchyGroup: "HierarchyGroupTypeDef"


class DescribeUserHierarchyStructureResponseTypeDef(TypedDict, total=False):
    HierarchyStructure: "HierarchyStructureTypeDef"


class DescribeUserResponseTypeDef(TypedDict, total=False):
    User: "UserTypeDef"


class DimensionsTypeDef(TypedDict, total=False):
    Queue: "QueueReferenceTypeDef"
    Channel: Channel


class EncryptionConfigTypeDef(TypedDict):
    EncryptionType: Literal["KMS"]
    KeyId: str


class FiltersTypeDef(TypedDict, total=False):
    Queues: List[str]
    Channels: List[Channel]


class GetContactAttributesResponseTypeDef(TypedDict, total=False):
    Attributes: Dict[str, str]


class GetCurrentMetricDataResponseTypeDef(TypedDict, total=False):
    NextToken: str
    MetricResults: List["CurrentMetricResultTypeDef"]
    DataSnapshotTime: datetime


class GetFederationTokenResponseTypeDef(TypedDict, total=False):
    Credentials: "CredentialsTypeDef"


class GetMetricDataResponseTypeDef(TypedDict, total=False):
    NextToken: str
    MetricResults: List["HistoricalMetricResultTypeDef"]


class HierarchyGroupSummaryTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str


class HierarchyGroupTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str
    LevelId: str
    HierarchyPath: "HierarchyPathTypeDef"


class HierarchyLevelTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str


class HierarchyLevelUpdateTypeDef(TypedDict):
    Name: str


class HierarchyPathTypeDef(TypedDict, total=False):
    LevelOne: "HierarchyGroupSummaryTypeDef"
    LevelTwo: "HierarchyGroupSummaryTypeDef"
    LevelThree: "HierarchyGroupSummaryTypeDef"
    LevelFour: "HierarchyGroupSummaryTypeDef"
    LevelFive: "HierarchyGroupSummaryTypeDef"


class HierarchyStructureTypeDef(TypedDict, total=False):
    LevelOne: "HierarchyLevelTypeDef"
    LevelTwo: "HierarchyLevelTypeDef"
    LevelThree: "HierarchyLevelTypeDef"
    LevelFour: "HierarchyLevelTypeDef"
    LevelFive: "HierarchyLevelTypeDef"


class HierarchyStructureUpdateTypeDef(TypedDict, total=False):
    LevelOne: "HierarchyLevelUpdateTypeDef"
    LevelTwo: "HierarchyLevelUpdateTypeDef"
    LevelThree: "HierarchyLevelUpdateTypeDef"
    LevelFour: "HierarchyLevelUpdateTypeDef"
    LevelFive: "HierarchyLevelUpdateTypeDef"


class HistoricalMetricDataTypeDef(TypedDict, total=False):
    Metric: "HistoricalMetricTypeDef"
    Value: float


class HistoricalMetricResultTypeDef(TypedDict, total=False):
    Dimensions: "DimensionsTypeDef"
    Collections: List["HistoricalMetricDataTypeDef"]


class HistoricalMetricTypeDef(TypedDict, total=False):
    Name: HistoricalMetricName
    Threshold: "ThresholdTypeDef"
    Statistic: Statistic
    Unit: Unit


class HoursOfOperationConfigTypeDef(TypedDict, total=False):
    Day: HoursOfOperationDays
    StartTime: "HoursOfOperationTimeSliceTypeDef"
    EndTime: "HoursOfOperationTimeSliceTypeDef"


class HoursOfOperationSummaryTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str


class HoursOfOperationTimeSliceTypeDef(TypedDict, total=False):
    Hours: int
    Minutes: int


class HoursOfOperationTypeDef(TypedDict, total=False):
    HoursOfOperationId: str
    HoursOfOperationArn: str
    Name: str
    Description: str
    TimeZone: str
    Config: List["HoursOfOperationConfigTypeDef"]
    Tags: Dict[str, str]


class InstanceStatusReasonTypeDef(TypedDict, total=False):
    Message: str


class _RequiredInstanceStorageConfigTypeDef(TypedDict):
    StorageType: StorageType


class InstanceStorageConfigTypeDef(_RequiredInstanceStorageConfigTypeDef, total=False):
    AssociationId: str
    S3Config: "S3ConfigTypeDef"
    KinesisVideoStreamConfig: "KinesisVideoStreamConfigTypeDef"
    KinesisStreamConfig: "KinesisStreamConfigTypeDef"
    KinesisFirehoseConfig: "KinesisFirehoseConfigTypeDef"


class InstanceSummaryTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    IdentityManagementType: DirectoryType
    InstanceAlias: str
    CreatedTime: datetime
    ServiceRole: str
    InstanceStatus: InstanceStatus
    InboundCallsEnabled: bool
    OutboundCallsEnabled: bool


class InstanceTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    IdentityManagementType: DirectoryType
    InstanceAlias: str
    CreatedTime: datetime
    ServiceRole: str
    InstanceStatus: InstanceStatus
    StatusReason: "InstanceStatusReasonTypeDef"
    InboundCallsEnabled: bool
    OutboundCallsEnabled: bool


class IntegrationAssociationSummaryTypeDef(TypedDict, total=False):
    IntegrationAssociationId: str
    IntegrationAssociationArn: str
    InstanceId: str
    IntegrationType: Literal["EVENT"]
    IntegrationArn: str
    SourceApplicationUrl: str
    SourceApplicationName: str
    SourceType: SourceType


class KinesisFirehoseConfigTypeDef(TypedDict):
    FirehoseArn: str


class KinesisStreamConfigTypeDef(TypedDict):
    StreamArn: str


class KinesisVideoStreamConfigTypeDef(TypedDict):
    Prefix: str
    RetentionPeriodHours: int
    EncryptionConfig: "EncryptionConfigTypeDef"


class LexBotTypeDef(TypedDict, total=False):
    Name: str
    LexRegion: str


class ListApprovedOriginsResponseTypeDef(TypedDict, total=False):
    Origins: List[str]
    NextToken: str


class ListContactFlowsResponseTypeDef(TypedDict, total=False):
    ContactFlowSummaryList: List["ContactFlowSummaryTypeDef"]
    NextToken: str


class ListHoursOfOperationsResponseTypeDef(TypedDict, total=False):
    HoursOfOperationSummaryList: List["HoursOfOperationSummaryTypeDef"]
    NextToken: str


class ListInstanceAttributesResponseTypeDef(TypedDict, total=False):
    Attributes: List["AttributeTypeDef"]
    NextToken: str


class ListInstanceStorageConfigsResponseTypeDef(TypedDict, total=False):
    StorageConfigs: List["InstanceStorageConfigTypeDef"]
    NextToken: str


class ListInstancesResponseTypeDef(TypedDict, total=False):
    InstanceSummaryList: List["InstanceSummaryTypeDef"]
    NextToken: str


class ListIntegrationAssociationsResponseTypeDef(TypedDict, total=False):
    IntegrationAssociationSummaryList: List["IntegrationAssociationSummaryTypeDef"]
    NextToken: str


class ListLambdaFunctionsResponseTypeDef(TypedDict, total=False):
    LambdaFunctions: List[str]
    NextToken: str


class ListLexBotsResponseTypeDef(TypedDict, total=False):
    LexBots: List["LexBotTypeDef"]
    NextToken: str


class ListPhoneNumbersResponseTypeDef(TypedDict, total=False):
    PhoneNumberSummaryList: List["PhoneNumberSummaryTypeDef"]
    NextToken: str


class ListPromptsResponseTypeDef(TypedDict, total=False):
    PromptSummaryList: List["PromptSummaryTypeDef"]
    NextToken: str


class ListQueueQuickConnectsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    QuickConnectSummaryList: List["QuickConnectSummaryTypeDef"]


class ListQueuesResponseTypeDef(TypedDict, total=False):
    QueueSummaryList: List["QueueSummaryTypeDef"]
    NextToken: str


class ListQuickConnectsResponseTypeDef(TypedDict, total=False):
    QuickConnectSummaryList: List["QuickConnectSummaryTypeDef"]
    NextToken: str


class ListRoutingProfileQueuesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    RoutingProfileQueueConfigSummaryList: List["RoutingProfileQueueConfigSummaryTypeDef"]


class ListRoutingProfilesResponseTypeDef(TypedDict, total=False):
    RoutingProfileSummaryList: List["RoutingProfileSummaryTypeDef"]
    NextToken: str


class ListSecurityKeysResponseTypeDef(TypedDict, total=False):
    SecurityKeys: List["SecurityKeyTypeDef"]
    NextToken: str


class ListSecurityProfilesResponseTypeDef(TypedDict, total=False):
    SecurityProfileSummaryList: List["SecurityProfileSummaryTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class ListUseCasesResponseTypeDef(TypedDict, total=False):
    UseCaseSummaryList: List["UseCaseTypeDef"]
    NextToken: str


class ListUserHierarchyGroupsResponseTypeDef(TypedDict, total=False):
    UserHierarchyGroupSummaryList: List["HierarchyGroupSummaryTypeDef"]
    NextToken: str


class ListUsersResponseTypeDef(TypedDict, total=False):
    UserSummaryList: List["UserSummaryTypeDef"]
    NextToken: str


class MediaConcurrencyTypeDef(TypedDict):
    Channel: Channel
    Concurrency: int


class OutboundCallerConfigTypeDef(TypedDict, total=False):
    OutboundCallerIdName: str
    OutboundCallerIdNumberId: str
    OutboundFlowId: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParticipantDetailsTypeDef(TypedDict):
    DisplayName: str


class PhoneNumberQuickConnectConfigTypeDef(TypedDict):
    PhoneNumber: str


class PhoneNumberSummaryTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    PhoneNumber: str
    PhoneNumberType: PhoneNumberType
    PhoneNumberCountryCode: PhoneNumberCountryCode


class PromptSummaryTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str


class QueueQuickConnectConfigTypeDef(TypedDict):
    QueueId: str
    ContactFlowId: str


class QueueReferenceTypeDef(TypedDict, total=False):
    Id: str
    Arn: str


class QueueSummaryTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str
    QueueType: QueueType


class QueueTypeDef(TypedDict, total=False):
    Name: str
    QueueArn: str
    QueueId: str
    Description: str
    OutboundCallerConfig: "OutboundCallerConfigTypeDef"
    HoursOfOperationId: str
    MaxContacts: int
    Status: QueueStatus
    Tags: Dict[str, str]


class _RequiredQuickConnectConfigTypeDef(TypedDict):
    QuickConnectType: QuickConnectType


class QuickConnectConfigTypeDef(_RequiredQuickConnectConfigTypeDef, total=False):
    UserConfig: "UserQuickConnectConfigTypeDef"
    QueueConfig: "QueueQuickConnectConfigTypeDef"
    PhoneConfig: "PhoneNumberQuickConnectConfigTypeDef"


class QuickConnectSummaryTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str
    QuickConnectType: QuickConnectType


class QuickConnectTypeDef(TypedDict, total=False):
    QuickConnectARN: str
    QuickConnectId: str
    Name: str
    Description: str
    QuickConnectConfig: "QuickConnectConfigTypeDef"
    Tags: Dict[str, str]


ReferenceTypeDef = TypedDict("ReferenceTypeDef", {"Value": str, "Type": Literal["URL"]})


class RoutingProfileQueueConfigSummaryTypeDef(TypedDict):
    QueueId: str
    QueueArn: str
    QueueName: str
    Priority: int
    Delay: int
    Channel: Channel


class RoutingProfileQueueConfigTypeDef(TypedDict):
    QueueReference: "RoutingProfileQueueReferenceTypeDef"
    Priority: int
    Delay: int


class RoutingProfileQueueReferenceTypeDef(TypedDict):
    QueueId: str
    Channel: Channel


class RoutingProfileSummaryTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str


class RoutingProfileTypeDef(TypedDict, total=False):
    InstanceId: str
    Name: str
    RoutingProfileArn: str
    RoutingProfileId: str
    Description: str
    MediaConcurrencies: List["MediaConcurrencyTypeDef"]
    DefaultOutboundQueueId: str
    Tags: Dict[str, str]


class _RequiredS3ConfigTypeDef(TypedDict):
    BucketName: str
    BucketPrefix: str


class S3ConfigTypeDef(_RequiredS3ConfigTypeDef, total=False):
    EncryptionConfig: "EncryptionConfigTypeDef"


class SecurityKeyTypeDef(TypedDict, total=False):
    AssociationId: str
    Key: str
    CreationTime: datetime


class SecurityProfileSummaryTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str


class StartChatContactResponseTypeDef(TypedDict, total=False):
    ContactId: str
    ParticipantId: str
    ParticipantToken: str


class StartOutboundVoiceContactResponseTypeDef(TypedDict, total=False):
    ContactId: str


class StartTaskContactResponseTypeDef(TypedDict, total=False):
    ContactId: str


class ThresholdTypeDef(TypedDict, total=False):
    Comparison: Literal["LT"]
    ThresholdValue: float


class UseCaseTypeDef(TypedDict, total=False):
    UseCaseId: str
    UseCaseArn: str
    UseCaseType: Literal["RULES_EVALUATION"]


class UserIdentityInfoTypeDef(TypedDict, total=False):
    FirstName: str
    LastName: str
    Email: str


class _RequiredUserPhoneConfigTypeDef(TypedDict):
    PhoneType: PhoneType


class UserPhoneConfigTypeDef(_RequiredUserPhoneConfigTypeDef, total=False):
    AutoAccept: bool
    AfterContactWorkTimeLimit: int
    DeskPhoneNumber: str


class UserQuickConnectConfigTypeDef(TypedDict):
    UserId: str
    ContactFlowId: str


class UserSummaryTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Username: str


class UserTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Username: str
    IdentityInfo: "UserIdentityInfoTypeDef"
    PhoneConfig: "UserPhoneConfigTypeDef"
    DirectoryUserId: str
    SecurityProfileIds: List[str]
    RoutingProfileId: str
    HierarchyGroupId: str
    Tags: Dict[str, str]


class VoiceRecordingConfigurationTypeDef(TypedDict, total=False):
    VoiceRecordingTrack: VoiceRecordingTrack
