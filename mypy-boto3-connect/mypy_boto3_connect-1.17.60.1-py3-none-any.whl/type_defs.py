"""
Main interface for connect service type definitions.

Usage::

    ```python
    from mypy_boto3_connect.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_connect.literals import (
    Channel,
    Comparison,
    ContactFlowType,
    CurrentMetricName,
    DirectoryType,
    EncryptionType,
    HistoricalMetricName,
    HoursOfOperationDays,
    InstanceAttributeType,
    InstanceStatus,
    IntegrationType,
    PhoneNumberCountryCode,
    PhoneNumberType,
    PhoneType,
    QueueStatus,
    QueueType,
    QuickConnectType,
    ReferenceType,
    SourceType,
    Statistic,
    StorageType,
    Unit,
    UseCaseType,
    VoiceRecordingTrack,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttributeTypeDef",
    "ContactFlowSummaryTypeDef",
    "ContactFlowTypeDef",
    "CredentialsTypeDef",
    "CurrentMetricDataTypeDef",
    "CurrentMetricResultTypeDef",
    "CurrentMetricTypeDef",
    "DimensionsTypeDef",
    "EncryptionConfigTypeDef",
    "HierarchyGroupSummaryTypeDef",
    "HierarchyGroupTypeDef",
    "HierarchyLevelTypeDef",
    "HierarchyLevelUpdateTypeDef",
    "HierarchyPathTypeDef",
    "HierarchyStructureTypeDef",
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
    "MediaConcurrencyTypeDef",
    "OutboundCallerConfigTypeDef",
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
    "RoutingProfileQueueConfigSummaryTypeDef",
    "RoutingProfileQueueReferenceTypeDef",
    "RoutingProfileSummaryTypeDef",
    "RoutingProfileTypeDef",
    "S3ConfigTypeDef",
    "SecurityKeyTypeDef",
    "SecurityProfileSummaryTypeDef",
    "ThresholdTypeDef",
    "UseCaseTypeDef",
    "UserIdentityInfoTypeDef",
    "UserPhoneConfigTypeDef",
    "UserQuickConnectConfigTypeDef",
    "UserSummaryTypeDef",
    "UserTypeDef",
    "AssociateInstanceStorageConfigResponseTypeDef",
    "AssociateSecurityKeyResponseTypeDef",
    "ChatMessageTypeDef",
    "CreateContactFlowResponseTypeDef",
    "CreateInstanceResponseTypeDef",
    "CreateIntegrationAssociationResponseTypeDef",
    "CreateQueueResponseTypeDef",
    "CreateQuickConnectResponseTypeDef",
    "CreateRoutingProfileResponseTypeDef",
    "CreateUseCaseResponseTypeDef",
    "CreateUserHierarchyGroupResponseTypeDef",
    "CreateUserResponseTypeDef",
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
    "FiltersTypeDef",
    "GetContactAttributesResponseTypeDef",
    "GetCurrentMetricDataResponseTypeDef",
    "GetFederationTokenResponseTypeDef",
    "GetMetricDataResponseTypeDef",
    "HierarchyStructureUpdateTypeDef",
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
    "PaginatorConfigTypeDef",
    "ParticipantDetailsTypeDef",
    "ReferenceTypeDef",
    "RoutingProfileQueueConfigTypeDef",
    "StartChatContactResponseTypeDef",
    "StartOutboundVoiceContactResponseTypeDef",
    "StartTaskContactResponseTypeDef",
    "VoiceRecordingConfigurationTypeDef",
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef", {"AttributeType": InstanceAttributeType, "Value": str}, total=False
)

ContactFlowSummaryTypeDef = TypedDict(
    "ContactFlowSummaryTypeDef",
    {"Id": str, "Arn": str, "Name": str, "ContactFlowType": ContactFlowType},
    total=False,
)

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

CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessToken": str,
        "AccessTokenExpiration": datetime,
        "RefreshToken": str,
        "RefreshTokenExpiration": datetime,
    },
    total=False,
)

CurrentMetricDataTypeDef = TypedDict(
    "CurrentMetricDataTypeDef", {"Metric": "CurrentMetricTypeDef", "Value": float}, total=False
)

CurrentMetricResultTypeDef = TypedDict(
    "CurrentMetricResultTypeDef",
    {"Dimensions": "DimensionsTypeDef", "Collections": List["CurrentMetricDataTypeDef"]},
    total=False,
)

CurrentMetricTypeDef = TypedDict(
    "CurrentMetricTypeDef", {"Name": CurrentMetricName, "Unit": Unit}, total=False
)

DimensionsTypeDef = TypedDict(
    "DimensionsTypeDef", {"Queue": "QueueReferenceTypeDef", "Channel": Channel}, total=False
)

EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef", {"EncryptionType": EncryptionType, "KeyId": str}
)

HierarchyGroupSummaryTypeDef = TypedDict(
    "HierarchyGroupSummaryTypeDef", {"Id": str, "Arn": str, "Name": str}, total=False
)

HierarchyGroupTypeDef = TypedDict(
    "HierarchyGroupTypeDef",
    {"Id": str, "Arn": str, "Name": str, "LevelId": str, "HierarchyPath": "HierarchyPathTypeDef"},
    total=False,
)

HierarchyLevelTypeDef = TypedDict(
    "HierarchyLevelTypeDef", {"Id": str, "Arn": str, "Name": str}, total=False
)

HierarchyLevelUpdateTypeDef = TypedDict("HierarchyLevelUpdateTypeDef", {"Name": str})

HierarchyPathTypeDef = TypedDict(
    "HierarchyPathTypeDef",
    {
        "LevelOne": "HierarchyGroupSummaryTypeDef",
        "LevelTwo": "HierarchyGroupSummaryTypeDef",
        "LevelThree": "HierarchyGroupSummaryTypeDef",
        "LevelFour": "HierarchyGroupSummaryTypeDef",
        "LevelFive": "HierarchyGroupSummaryTypeDef",
    },
    total=False,
)

HierarchyStructureTypeDef = TypedDict(
    "HierarchyStructureTypeDef",
    {
        "LevelOne": "HierarchyLevelTypeDef",
        "LevelTwo": "HierarchyLevelTypeDef",
        "LevelThree": "HierarchyLevelTypeDef",
        "LevelFour": "HierarchyLevelTypeDef",
        "LevelFive": "HierarchyLevelTypeDef",
    },
    total=False,
)

HistoricalMetricDataTypeDef = TypedDict(
    "HistoricalMetricDataTypeDef",
    {"Metric": "HistoricalMetricTypeDef", "Value": float},
    total=False,
)

HistoricalMetricResultTypeDef = TypedDict(
    "HistoricalMetricResultTypeDef",
    {"Dimensions": "DimensionsTypeDef", "Collections": List["HistoricalMetricDataTypeDef"]},
    total=False,
)

HistoricalMetricTypeDef = TypedDict(
    "HistoricalMetricTypeDef",
    {
        "Name": HistoricalMetricName,
        "Threshold": "ThresholdTypeDef",
        "Statistic": Statistic,
        "Unit": Unit,
    },
    total=False,
)

HoursOfOperationConfigTypeDef = TypedDict(
    "HoursOfOperationConfigTypeDef",
    {
        "Day": HoursOfOperationDays,
        "StartTime": "HoursOfOperationTimeSliceTypeDef",
        "EndTime": "HoursOfOperationTimeSliceTypeDef",
    },
    total=False,
)

HoursOfOperationSummaryTypeDef = TypedDict(
    "HoursOfOperationSummaryTypeDef", {"Id": str, "Arn": str, "Name": str}, total=False
)

HoursOfOperationTimeSliceTypeDef = TypedDict(
    "HoursOfOperationTimeSliceTypeDef", {"Hours": int, "Minutes": int}, total=False
)

HoursOfOperationTypeDef = TypedDict(
    "HoursOfOperationTypeDef",
    {
        "HoursOfOperationId": str,
        "HoursOfOperationArn": str,
        "Name": str,
        "Description": str,
        "TimeZone": str,
        "Config": List["HoursOfOperationConfigTypeDef"],
        "Tags": Dict[str, str],
    },
    total=False,
)

InstanceStatusReasonTypeDef = TypedDict(
    "InstanceStatusReasonTypeDef", {"Message": str}, total=False
)

_RequiredInstanceStorageConfigTypeDef = TypedDict(
    "_RequiredInstanceStorageConfigTypeDef", {"StorageType": StorageType}
)
_OptionalInstanceStorageConfigTypeDef = TypedDict(
    "_OptionalInstanceStorageConfigTypeDef",
    {
        "AssociationId": str,
        "S3Config": "S3ConfigTypeDef",
        "KinesisVideoStreamConfig": "KinesisVideoStreamConfigTypeDef",
        "KinesisStreamConfig": "KinesisStreamConfigTypeDef",
        "KinesisFirehoseConfig": "KinesisFirehoseConfigTypeDef",
    },
    total=False,
)


class InstanceStorageConfigTypeDef(
    _RequiredInstanceStorageConfigTypeDef, _OptionalInstanceStorageConfigTypeDef
):
    pass


InstanceSummaryTypeDef = TypedDict(
    "InstanceSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "IdentityManagementType": DirectoryType,
        "InstanceAlias": str,
        "CreatedTime": datetime,
        "ServiceRole": str,
        "InstanceStatus": InstanceStatus,
        "InboundCallsEnabled": bool,
        "OutboundCallsEnabled": bool,
    },
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "Id": str,
        "Arn": str,
        "IdentityManagementType": DirectoryType,
        "InstanceAlias": str,
        "CreatedTime": datetime,
        "ServiceRole": str,
        "InstanceStatus": InstanceStatus,
        "StatusReason": "InstanceStatusReasonTypeDef",
        "InboundCallsEnabled": bool,
        "OutboundCallsEnabled": bool,
    },
    total=False,
)

IntegrationAssociationSummaryTypeDef = TypedDict(
    "IntegrationAssociationSummaryTypeDef",
    {
        "IntegrationAssociationId": str,
        "IntegrationAssociationArn": str,
        "InstanceId": str,
        "IntegrationType": IntegrationType,
        "IntegrationArn": str,
        "SourceApplicationUrl": str,
        "SourceApplicationName": str,
        "SourceType": SourceType,
    },
    total=False,
)

KinesisFirehoseConfigTypeDef = TypedDict("KinesisFirehoseConfigTypeDef", {"FirehoseArn": str})

KinesisStreamConfigTypeDef = TypedDict("KinesisStreamConfigTypeDef", {"StreamArn": str})

KinesisVideoStreamConfigTypeDef = TypedDict(
    "KinesisVideoStreamConfigTypeDef",
    {"Prefix": str, "RetentionPeriodHours": int, "EncryptionConfig": "EncryptionConfigTypeDef"},
)

LexBotTypeDef = TypedDict("LexBotTypeDef", {"Name": str, "LexRegion": str}, total=False)

MediaConcurrencyTypeDef = TypedDict(
    "MediaConcurrencyTypeDef", {"Channel": Channel, "Concurrency": int}
)

OutboundCallerConfigTypeDef = TypedDict(
    "OutboundCallerConfigTypeDef",
    {"OutboundCallerIdName": str, "OutboundCallerIdNumberId": str, "OutboundFlowId": str},
    total=False,
)

PhoneNumberQuickConnectConfigTypeDef = TypedDict(
    "PhoneNumberQuickConnectConfigTypeDef", {"PhoneNumber": str}
)

PhoneNumberSummaryTypeDef = TypedDict(
    "PhoneNumberSummaryTypeDef",
    {
        "Id": str,
        "Arn": str,
        "PhoneNumber": str,
        "PhoneNumberType": PhoneNumberType,
        "PhoneNumberCountryCode": PhoneNumberCountryCode,
    },
    total=False,
)

PromptSummaryTypeDef = TypedDict(
    "PromptSummaryTypeDef", {"Id": str, "Arn": str, "Name": str}, total=False
)

QueueQuickConnectConfigTypeDef = TypedDict(
    "QueueQuickConnectConfigTypeDef", {"QueueId": str, "ContactFlowId": str}
)

QueueReferenceTypeDef = TypedDict("QueueReferenceTypeDef", {"Id": str, "Arn": str}, total=False)

QueueSummaryTypeDef = TypedDict(
    "QueueSummaryTypeDef", {"Id": str, "Arn": str, "Name": str, "QueueType": QueueType}, total=False
)

QueueTypeDef = TypedDict(
    "QueueTypeDef",
    {
        "Name": str,
        "QueueArn": str,
        "QueueId": str,
        "Description": str,
        "OutboundCallerConfig": "OutboundCallerConfigTypeDef",
        "HoursOfOperationId": str,
        "MaxContacts": int,
        "Status": QueueStatus,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredQuickConnectConfigTypeDef = TypedDict(
    "_RequiredQuickConnectConfigTypeDef", {"QuickConnectType": QuickConnectType}
)
_OptionalQuickConnectConfigTypeDef = TypedDict(
    "_OptionalQuickConnectConfigTypeDef",
    {
        "UserConfig": "UserQuickConnectConfigTypeDef",
        "QueueConfig": "QueueQuickConnectConfigTypeDef",
        "PhoneConfig": "PhoneNumberQuickConnectConfigTypeDef",
    },
    total=False,
)


class QuickConnectConfigTypeDef(
    _RequiredQuickConnectConfigTypeDef, _OptionalQuickConnectConfigTypeDef
):
    pass


QuickConnectSummaryTypeDef = TypedDict(
    "QuickConnectSummaryTypeDef",
    {"Id": str, "Arn": str, "Name": str, "QuickConnectType": QuickConnectType},
    total=False,
)

QuickConnectTypeDef = TypedDict(
    "QuickConnectTypeDef",
    {
        "QuickConnectARN": str,
        "QuickConnectId": str,
        "Name": str,
        "Description": str,
        "QuickConnectConfig": "QuickConnectConfigTypeDef",
        "Tags": Dict[str, str],
    },
    total=False,
)

RoutingProfileQueueConfigSummaryTypeDef = TypedDict(
    "RoutingProfileQueueConfigSummaryTypeDef",
    {
        "QueueId": str,
        "QueueArn": str,
        "QueueName": str,
        "Priority": int,
        "Delay": int,
        "Channel": Channel,
    },
)

RoutingProfileQueueReferenceTypeDef = TypedDict(
    "RoutingProfileQueueReferenceTypeDef", {"QueueId": str, "Channel": Channel}
)

RoutingProfileSummaryTypeDef = TypedDict(
    "RoutingProfileSummaryTypeDef", {"Id": str, "Arn": str, "Name": str}, total=False
)

RoutingProfileTypeDef = TypedDict(
    "RoutingProfileTypeDef",
    {
        "InstanceId": str,
        "Name": str,
        "RoutingProfileArn": str,
        "RoutingProfileId": str,
        "Description": str,
        "MediaConcurrencies": List["MediaConcurrencyTypeDef"],
        "DefaultOutboundQueueId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

_RequiredS3ConfigTypeDef = TypedDict(
    "_RequiredS3ConfigTypeDef", {"BucketName": str, "BucketPrefix": str}
)
_OptionalS3ConfigTypeDef = TypedDict(
    "_OptionalS3ConfigTypeDef", {"EncryptionConfig": "EncryptionConfigTypeDef"}, total=False
)


class S3ConfigTypeDef(_RequiredS3ConfigTypeDef, _OptionalS3ConfigTypeDef):
    pass


SecurityKeyTypeDef = TypedDict(
    "SecurityKeyTypeDef", {"AssociationId": str, "Key": str, "CreationTime": datetime}, total=False
)

SecurityProfileSummaryTypeDef = TypedDict(
    "SecurityProfileSummaryTypeDef", {"Id": str, "Arn": str, "Name": str}, total=False
)

ThresholdTypeDef = TypedDict(
    "ThresholdTypeDef", {"Comparison": Comparison, "ThresholdValue": float}, total=False
)

UseCaseTypeDef = TypedDict(
    "UseCaseTypeDef", {"UseCaseId": str, "UseCaseArn": str, "UseCaseType": UseCaseType}, total=False
)

UserIdentityInfoTypeDef = TypedDict(
    "UserIdentityInfoTypeDef", {"FirstName": str, "LastName": str, "Email": str}, total=False
)

_RequiredUserPhoneConfigTypeDef = TypedDict(
    "_RequiredUserPhoneConfigTypeDef", {"PhoneType": PhoneType}
)
_OptionalUserPhoneConfigTypeDef = TypedDict(
    "_OptionalUserPhoneConfigTypeDef",
    {"AutoAccept": bool, "AfterContactWorkTimeLimit": int, "DeskPhoneNumber": str},
    total=False,
)


class UserPhoneConfigTypeDef(_RequiredUserPhoneConfigTypeDef, _OptionalUserPhoneConfigTypeDef):
    pass


UserQuickConnectConfigTypeDef = TypedDict(
    "UserQuickConnectConfigTypeDef", {"UserId": str, "ContactFlowId": str}
)

UserSummaryTypeDef = TypedDict(
    "UserSummaryTypeDef", {"Id": str, "Arn": str, "Username": str}, total=False
)

UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Username": str,
        "IdentityInfo": "UserIdentityInfoTypeDef",
        "PhoneConfig": "UserPhoneConfigTypeDef",
        "DirectoryUserId": str,
        "SecurityProfileIds": List[str],
        "RoutingProfileId": str,
        "HierarchyGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

AssociateInstanceStorageConfigResponseTypeDef = TypedDict(
    "AssociateInstanceStorageConfigResponseTypeDef", {"AssociationId": str}, total=False
)

AssociateSecurityKeyResponseTypeDef = TypedDict(
    "AssociateSecurityKeyResponseTypeDef", {"AssociationId": str}, total=False
)

ChatMessageTypeDef = TypedDict("ChatMessageTypeDef", {"ContentType": str, "Content": str})

CreateContactFlowResponseTypeDef = TypedDict(
    "CreateContactFlowResponseTypeDef", {"ContactFlowId": str, "ContactFlowArn": str}, total=False
)

CreateInstanceResponseTypeDef = TypedDict(
    "CreateInstanceResponseTypeDef", {"Id": str, "Arn": str}, total=False
)

CreateIntegrationAssociationResponseTypeDef = TypedDict(
    "CreateIntegrationAssociationResponseTypeDef",
    {"IntegrationAssociationId": str, "IntegrationAssociationArn": str},
    total=False,
)

CreateQueueResponseTypeDef = TypedDict(
    "CreateQueueResponseTypeDef", {"QueueArn": str, "QueueId": str}, total=False
)

CreateQuickConnectResponseTypeDef = TypedDict(
    "CreateQuickConnectResponseTypeDef",
    {"QuickConnectARN": str, "QuickConnectId": str},
    total=False,
)

CreateRoutingProfileResponseTypeDef = TypedDict(
    "CreateRoutingProfileResponseTypeDef",
    {"RoutingProfileArn": str, "RoutingProfileId": str},
    total=False,
)

CreateUseCaseResponseTypeDef = TypedDict(
    "CreateUseCaseResponseTypeDef", {"UseCaseId": str, "UseCaseArn": str}, total=False
)

CreateUserHierarchyGroupResponseTypeDef = TypedDict(
    "CreateUserHierarchyGroupResponseTypeDef",
    {"HierarchyGroupId": str, "HierarchyGroupArn": str},
    total=False,
)

CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef", {"UserId": str, "UserArn": str}, total=False
)

DescribeContactFlowResponseTypeDef = TypedDict(
    "DescribeContactFlowResponseTypeDef", {"ContactFlow": "ContactFlowTypeDef"}, total=False
)

DescribeHoursOfOperationResponseTypeDef = TypedDict(
    "DescribeHoursOfOperationResponseTypeDef",
    {"HoursOfOperation": "HoursOfOperationTypeDef"},
    total=False,
)

DescribeInstanceAttributeResponseTypeDef = TypedDict(
    "DescribeInstanceAttributeResponseTypeDef", {"Attribute": "AttributeTypeDef"}, total=False
)

DescribeInstanceResponseTypeDef = TypedDict(
    "DescribeInstanceResponseTypeDef", {"Instance": "InstanceTypeDef"}, total=False
)

DescribeInstanceStorageConfigResponseTypeDef = TypedDict(
    "DescribeInstanceStorageConfigResponseTypeDef",
    {"StorageConfig": "InstanceStorageConfigTypeDef"},
    total=False,
)

DescribeQueueResponseTypeDef = TypedDict(
    "DescribeQueueResponseTypeDef", {"Queue": "QueueTypeDef"}, total=False
)

DescribeQuickConnectResponseTypeDef = TypedDict(
    "DescribeQuickConnectResponseTypeDef", {"QuickConnect": "QuickConnectTypeDef"}, total=False
)

DescribeRoutingProfileResponseTypeDef = TypedDict(
    "DescribeRoutingProfileResponseTypeDef",
    {"RoutingProfile": "RoutingProfileTypeDef"},
    total=False,
)

DescribeUserHierarchyGroupResponseTypeDef = TypedDict(
    "DescribeUserHierarchyGroupResponseTypeDef",
    {"HierarchyGroup": "HierarchyGroupTypeDef"},
    total=False,
)

DescribeUserHierarchyStructureResponseTypeDef = TypedDict(
    "DescribeUserHierarchyStructureResponseTypeDef",
    {"HierarchyStructure": "HierarchyStructureTypeDef"},
    total=False,
)

DescribeUserResponseTypeDef = TypedDict(
    "DescribeUserResponseTypeDef", {"User": "UserTypeDef"}, total=False
)

FiltersTypeDef = TypedDict(
    "FiltersTypeDef", {"Queues": List[str], "Channels": List[Channel]}, total=False
)

GetContactAttributesResponseTypeDef = TypedDict(
    "GetContactAttributesResponseTypeDef", {"Attributes": Dict[str, str]}, total=False
)

GetCurrentMetricDataResponseTypeDef = TypedDict(
    "GetCurrentMetricDataResponseTypeDef",
    {
        "NextToken": str,
        "MetricResults": List["CurrentMetricResultTypeDef"],
        "DataSnapshotTime": datetime,
    },
    total=False,
)

GetFederationTokenResponseTypeDef = TypedDict(
    "GetFederationTokenResponseTypeDef", {"Credentials": "CredentialsTypeDef"}, total=False
)

GetMetricDataResponseTypeDef = TypedDict(
    "GetMetricDataResponseTypeDef",
    {"NextToken": str, "MetricResults": List["HistoricalMetricResultTypeDef"]},
    total=False,
)

HierarchyStructureUpdateTypeDef = TypedDict(
    "HierarchyStructureUpdateTypeDef",
    {
        "LevelOne": "HierarchyLevelUpdateTypeDef",
        "LevelTwo": "HierarchyLevelUpdateTypeDef",
        "LevelThree": "HierarchyLevelUpdateTypeDef",
        "LevelFour": "HierarchyLevelUpdateTypeDef",
        "LevelFive": "HierarchyLevelUpdateTypeDef",
    },
    total=False,
)

ListApprovedOriginsResponseTypeDef = TypedDict(
    "ListApprovedOriginsResponseTypeDef", {"Origins": List[str], "NextToken": str}, total=False
)

ListContactFlowsResponseTypeDef = TypedDict(
    "ListContactFlowsResponseTypeDef",
    {"ContactFlowSummaryList": List["ContactFlowSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListHoursOfOperationsResponseTypeDef = TypedDict(
    "ListHoursOfOperationsResponseTypeDef",
    {"HoursOfOperationSummaryList": List["HoursOfOperationSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListInstanceAttributesResponseTypeDef = TypedDict(
    "ListInstanceAttributesResponseTypeDef",
    {"Attributes": List["AttributeTypeDef"], "NextToken": str},
    total=False,
)

ListInstanceStorageConfigsResponseTypeDef = TypedDict(
    "ListInstanceStorageConfigsResponseTypeDef",
    {"StorageConfigs": List["InstanceStorageConfigTypeDef"], "NextToken": str},
    total=False,
)

ListInstancesResponseTypeDef = TypedDict(
    "ListInstancesResponseTypeDef",
    {"InstanceSummaryList": List["InstanceSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListIntegrationAssociationsResponseTypeDef = TypedDict(
    "ListIntegrationAssociationsResponseTypeDef",
    {
        "IntegrationAssociationSummaryList": List["IntegrationAssociationSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListLambdaFunctionsResponseTypeDef = TypedDict(
    "ListLambdaFunctionsResponseTypeDef",
    {"LambdaFunctions": List[str], "NextToken": str},
    total=False,
)

ListLexBotsResponseTypeDef = TypedDict(
    "ListLexBotsResponseTypeDef", {"LexBots": List["LexBotTypeDef"], "NextToken": str}, total=False
)

ListPhoneNumbersResponseTypeDef = TypedDict(
    "ListPhoneNumbersResponseTypeDef",
    {"PhoneNumberSummaryList": List["PhoneNumberSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListPromptsResponseTypeDef = TypedDict(
    "ListPromptsResponseTypeDef",
    {"PromptSummaryList": List["PromptSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListQueueQuickConnectsResponseTypeDef = TypedDict(
    "ListQueueQuickConnectsResponseTypeDef",
    {"NextToken": str, "QuickConnectSummaryList": List["QuickConnectSummaryTypeDef"]},
    total=False,
)

ListQueuesResponseTypeDef = TypedDict(
    "ListQueuesResponseTypeDef",
    {"QueueSummaryList": List["QueueSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListQuickConnectsResponseTypeDef = TypedDict(
    "ListQuickConnectsResponseTypeDef",
    {"QuickConnectSummaryList": List["QuickConnectSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListRoutingProfileQueuesResponseTypeDef = TypedDict(
    "ListRoutingProfileQueuesResponseTypeDef",
    {
        "NextToken": str,
        "RoutingProfileQueueConfigSummaryList": List["RoutingProfileQueueConfigSummaryTypeDef"],
    },
    total=False,
)

ListRoutingProfilesResponseTypeDef = TypedDict(
    "ListRoutingProfilesResponseTypeDef",
    {"RoutingProfileSummaryList": List["RoutingProfileSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListSecurityKeysResponseTypeDef = TypedDict(
    "ListSecurityKeysResponseTypeDef",
    {"SecurityKeys": List["SecurityKeyTypeDef"], "NextToken": str},
    total=False,
)

ListSecurityProfilesResponseTypeDef = TypedDict(
    "ListSecurityProfilesResponseTypeDef",
    {"SecurityProfileSummaryList": List["SecurityProfileSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

ListUseCasesResponseTypeDef = TypedDict(
    "ListUseCasesResponseTypeDef",
    {"UseCaseSummaryList": List["UseCaseTypeDef"], "NextToken": str},
    total=False,
)

ListUserHierarchyGroupsResponseTypeDef = TypedDict(
    "ListUserHierarchyGroupsResponseTypeDef",
    {"UserHierarchyGroupSummaryList": List["HierarchyGroupSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {"UserSummaryList": List["UserSummaryTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ParticipantDetailsTypeDef = TypedDict("ParticipantDetailsTypeDef", {"DisplayName": str})

ReferenceTypeDef = TypedDict("ReferenceTypeDef", {"Value": str, "Type": ReferenceType})

RoutingProfileQueueConfigTypeDef = TypedDict(
    "RoutingProfileQueueConfigTypeDef",
    {"QueueReference": "RoutingProfileQueueReferenceTypeDef", "Priority": int, "Delay": int},
)

StartChatContactResponseTypeDef = TypedDict(
    "StartChatContactResponseTypeDef",
    {"ContactId": str, "ParticipantId": str, "ParticipantToken": str},
    total=False,
)

StartOutboundVoiceContactResponseTypeDef = TypedDict(
    "StartOutboundVoiceContactResponseTypeDef", {"ContactId": str}, total=False
)

StartTaskContactResponseTypeDef = TypedDict(
    "StartTaskContactResponseTypeDef", {"ContactId": str}, total=False
)

VoiceRecordingConfigurationTypeDef = TypedDict(
    "VoiceRecordingConfigurationTypeDef", {"VoiceRecordingTrack": VoiceRecordingTrack}, total=False
)
