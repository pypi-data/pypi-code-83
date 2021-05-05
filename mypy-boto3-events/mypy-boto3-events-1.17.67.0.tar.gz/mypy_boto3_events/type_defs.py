"""
Type annotations for events service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_events/type_defs.html)

Usage::

    ```python
    from mypy_boto3_events.type_defs import ApiDestinationTypeDef

    data: ApiDestinationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_events.literals import (
    ApiDestinationHttpMethod,
    ApiDestinationState,
    ArchiveState,
    AssignPublicIp,
    ConnectionAuthorizationType,
    ConnectionOAuthHttpMethod,
    ConnectionState,
    EventSourceState,
    LaunchType,
    ReplayState,
    RuleState,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApiDestinationTypeDef",
    "ArchiveTypeDef",
    "AwsVpcConfigurationTypeDef",
    "BatchArrayPropertiesTypeDef",
    "BatchParametersTypeDef",
    "BatchRetryStrategyTypeDef",
    "CancelReplayResponseTypeDef",
    "ConditionTypeDef",
    "ConnectionApiKeyAuthResponseParametersTypeDef",
    "ConnectionAuthResponseParametersTypeDef",
    "ConnectionBasicAuthResponseParametersTypeDef",
    "ConnectionBodyParameterTypeDef",
    "ConnectionHeaderParameterTypeDef",
    "ConnectionHttpParametersTypeDef",
    "ConnectionOAuthClientResponseParametersTypeDef",
    "ConnectionOAuthResponseParametersTypeDef",
    "ConnectionQueryStringParameterTypeDef",
    "ConnectionTypeDef",
    "CreateApiDestinationResponseTypeDef",
    "CreateArchiveResponseTypeDef",
    "CreateConnectionApiKeyAuthRequestParametersTypeDef",
    "CreateConnectionAuthRequestParametersTypeDef",
    "CreateConnectionBasicAuthRequestParametersTypeDef",
    "CreateConnectionOAuthClientRequestParametersTypeDef",
    "CreateConnectionOAuthRequestParametersTypeDef",
    "CreateConnectionResponseTypeDef",
    "CreateEventBusResponseTypeDef",
    "CreatePartnerEventSourceResponseTypeDef",
    "DeadLetterConfigTypeDef",
    "DeauthorizeConnectionResponseTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DescribeApiDestinationResponseTypeDef",
    "DescribeArchiveResponseTypeDef",
    "DescribeConnectionResponseTypeDef",
    "DescribeEventBusResponseTypeDef",
    "DescribeEventSourceResponseTypeDef",
    "DescribePartnerEventSourceResponseTypeDef",
    "DescribeReplayResponseTypeDef",
    "DescribeRuleResponseTypeDef",
    "EcsParametersTypeDef",
    "EventBusTypeDef",
    "EventSourceTypeDef",
    "HttpParametersTypeDef",
    "InputTransformerTypeDef",
    "KinesisParametersTypeDef",
    "ListApiDestinationsResponseTypeDef",
    "ListArchivesResponseTypeDef",
    "ListConnectionsResponseTypeDef",
    "ListEventBusesResponseTypeDef",
    "ListEventSourcesResponseTypeDef",
    "ListPartnerEventSourceAccountsResponseTypeDef",
    "ListPartnerEventSourcesResponseTypeDef",
    "ListReplaysResponseTypeDef",
    "ListRuleNamesByTargetResponseTypeDef",
    "ListRulesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetsByRuleResponseTypeDef",
    "NetworkConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PartnerEventSourceAccountTypeDef",
    "PartnerEventSourceTypeDef",
    "PutEventsRequestEntryTypeDef",
    "PutEventsResponseTypeDef",
    "PutEventsResultEntryTypeDef",
    "PutPartnerEventsRequestEntryTypeDef",
    "PutPartnerEventsResponseTypeDef",
    "PutPartnerEventsResultEntryTypeDef",
    "PutRuleResponseTypeDef",
    "PutTargetsResponseTypeDef",
    "PutTargetsResultEntryTypeDef",
    "RedshiftDataParametersTypeDef",
    "RemoveTargetsResponseTypeDef",
    "RemoveTargetsResultEntryTypeDef",
    "ReplayDestinationTypeDef",
    "ReplayTypeDef",
    "RetryPolicyTypeDef",
    "RuleTypeDef",
    "RunCommandParametersTypeDef",
    "RunCommandTargetTypeDef",
    "SageMakerPipelineParameterTypeDef",
    "SageMakerPipelineParametersTypeDef",
    "SqsParametersTypeDef",
    "StartReplayResponseTypeDef",
    "TagTypeDef",
    "TargetTypeDef",
    "TestEventPatternResponseTypeDef",
    "UpdateApiDestinationResponseTypeDef",
    "UpdateArchiveResponseTypeDef",
    "UpdateConnectionApiKeyAuthRequestParametersTypeDef",
    "UpdateConnectionAuthRequestParametersTypeDef",
    "UpdateConnectionBasicAuthRequestParametersTypeDef",
    "UpdateConnectionOAuthClientRequestParametersTypeDef",
    "UpdateConnectionOAuthRequestParametersTypeDef",
    "UpdateConnectionResponseTypeDef",
)


class ApiDestinationTypeDef(TypedDict, total=False):
    ApiDestinationArn: str
    Name: str
    ApiDestinationState: ApiDestinationState
    ConnectionArn: str
    InvocationEndpoint: str
    HttpMethod: ApiDestinationHttpMethod
    InvocationRateLimitPerSecond: int
    CreationTime: datetime
    LastModifiedTime: datetime


class ArchiveTypeDef(TypedDict, total=False):
    ArchiveName: str
    EventSourceArn: str
    State: ArchiveState
    StateReason: str
    RetentionDays: int
    SizeBytes: int
    EventCount: int
    CreationTime: datetime


class _RequiredAwsVpcConfigurationTypeDef(TypedDict):
    Subnets: List[str]


class AwsVpcConfigurationTypeDef(_RequiredAwsVpcConfigurationTypeDef, total=False):
    SecurityGroups: List[str]
    AssignPublicIp: AssignPublicIp


class BatchArrayPropertiesTypeDef(TypedDict, total=False):
    Size: int


class _RequiredBatchParametersTypeDef(TypedDict):
    JobDefinition: str
    JobName: str


class BatchParametersTypeDef(_RequiredBatchParametersTypeDef, total=False):
    ArrayProperties: "BatchArrayPropertiesTypeDef"
    RetryStrategy: "BatchRetryStrategyTypeDef"


class BatchRetryStrategyTypeDef(TypedDict, total=False):
    Attempts: int


class CancelReplayResponseTypeDef(TypedDict, total=False):
    ReplayArn: str
    State: ReplayState
    StateReason: str


ConditionTypeDef = TypedDict("ConditionTypeDef", {"Type": str, "Key": str, "Value": str})


class ConnectionApiKeyAuthResponseParametersTypeDef(TypedDict, total=False):
    ApiKeyName: str


class ConnectionAuthResponseParametersTypeDef(TypedDict, total=False):
    BasicAuthParameters: "ConnectionBasicAuthResponseParametersTypeDef"
    OAuthParameters: "ConnectionOAuthResponseParametersTypeDef"
    ApiKeyAuthParameters: "ConnectionApiKeyAuthResponseParametersTypeDef"
    InvocationHttpParameters: "ConnectionHttpParametersTypeDef"


class ConnectionBasicAuthResponseParametersTypeDef(TypedDict, total=False):
    Username: str


class ConnectionBodyParameterTypeDef(TypedDict, total=False):
    Key: str
    Value: str
    IsValueSecret: bool


class ConnectionHeaderParameterTypeDef(TypedDict, total=False):
    Key: str
    Value: str
    IsValueSecret: bool


class ConnectionHttpParametersTypeDef(TypedDict, total=False):
    HeaderParameters: List["ConnectionHeaderParameterTypeDef"]
    QueryStringParameters: List["ConnectionQueryStringParameterTypeDef"]
    BodyParameters: List["ConnectionBodyParameterTypeDef"]


class ConnectionOAuthClientResponseParametersTypeDef(TypedDict, total=False):
    ClientID: str


class ConnectionOAuthResponseParametersTypeDef(TypedDict, total=False):
    ClientParameters: "ConnectionOAuthClientResponseParametersTypeDef"
    AuthorizationEndpoint: str
    HttpMethod: ConnectionOAuthHttpMethod
    OAuthHttpParameters: "ConnectionHttpParametersTypeDef"


class ConnectionQueryStringParameterTypeDef(TypedDict, total=False):
    Key: str
    Value: str
    IsValueSecret: bool


class ConnectionTypeDef(TypedDict, total=False):
    ConnectionArn: str
    Name: str
    ConnectionState: ConnectionState
    StateReason: str
    AuthorizationType: ConnectionAuthorizationType
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime


class CreateApiDestinationResponseTypeDef(TypedDict, total=False):
    ApiDestinationArn: str
    ApiDestinationState: ApiDestinationState
    CreationTime: datetime
    LastModifiedTime: datetime


class CreateArchiveResponseTypeDef(TypedDict, total=False):
    ArchiveArn: str
    State: ArchiveState
    StateReason: str
    CreationTime: datetime


class CreateConnectionApiKeyAuthRequestParametersTypeDef(TypedDict):
    ApiKeyName: str
    ApiKeyValue: str


class CreateConnectionAuthRequestParametersTypeDef(TypedDict, total=False):
    BasicAuthParameters: "CreateConnectionBasicAuthRequestParametersTypeDef"
    OAuthParameters: "CreateConnectionOAuthRequestParametersTypeDef"
    ApiKeyAuthParameters: "CreateConnectionApiKeyAuthRequestParametersTypeDef"
    InvocationHttpParameters: "ConnectionHttpParametersTypeDef"


class CreateConnectionBasicAuthRequestParametersTypeDef(TypedDict):
    Username: str
    Password: str


class CreateConnectionOAuthClientRequestParametersTypeDef(TypedDict):
    ClientID: str
    ClientSecret: str


class _RequiredCreateConnectionOAuthRequestParametersTypeDef(TypedDict):
    ClientParameters: "CreateConnectionOAuthClientRequestParametersTypeDef"
    AuthorizationEndpoint: str
    HttpMethod: ConnectionOAuthHttpMethod


class CreateConnectionOAuthRequestParametersTypeDef(
    _RequiredCreateConnectionOAuthRequestParametersTypeDef, total=False
):
    OAuthHttpParameters: "ConnectionHttpParametersTypeDef"


class CreateConnectionResponseTypeDef(TypedDict, total=False):
    ConnectionArn: str
    ConnectionState: ConnectionState
    CreationTime: datetime
    LastModifiedTime: datetime


class CreateEventBusResponseTypeDef(TypedDict, total=False):
    EventBusArn: str


class CreatePartnerEventSourceResponseTypeDef(TypedDict, total=False):
    EventSourceArn: str


class DeadLetterConfigTypeDef(TypedDict, total=False):
    Arn: str


class DeauthorizeConnectionResponseTypeDef(TypedDict, total=False):
    ConnectionArn: str
    ConnectionState: ConnectionState
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime


class DeleteConnectionResponseTypeDef(TypedDict, total=False):
    ConnectionArn: str
    ConnectionState: ConnectionState
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime


class DescribeApiDestinationResponseTypeDef(TypedDict, total=False):
    ApiDestinationArn: str
    Name: str
    Description: str
    ApiDestinationState: ApiDestinationState
    ConnectionArn: str
    InvocationEndpoint: str
    HttpMethod: ApiDestinationHttpMethod
    InvocationRateLimitPerSecond: int
    CreationTime: datetime
    LastModifiedTime: datetime


class DescribeArchiveResponseTypeDef(TypedDict, total=False):
    ArchiveArn: str
    ArchiveName: str
    EventSourceArn: str
    Description: str
    EventPattern: str
    State: ArchiveState
    StateReason: str
    RetentionDays: int
    SizeBytes: int
    EventCount: int
    CreationTime: datetime


class DescribeConnectionResponseTypeDef(TypedDict, total=False):
    ConnectionArn: str
    Name: str
    Description: str
    ConnectionState: ConnectionState
    StateReason: str
    AuthorizationType: ConnectionAuthorizationType
    SecretArn: str
    AuthParameters: "ConnectionAuthResponseParametersTypeDef"
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime


class DescribeEventBusResponseTypeDef(TypedDict, total=False):
    Name: str
    Arn: str
    Policy: str


class DescribeEventSourceResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreatedBy: str
    CreationTime: datetime
    ExpirationTime: datetime
    Name: str
    State: EventSourceState


class DescribePartnerEventSourceResponseTypeDef(TypedDict, total=False):
    Arn: str
    Name: str


class DescribeReplayResponseTypeDef(TypedDict, total=False):
    ReplayName: str
    ReplayArn: str
    Description: str
    State: ReplayState
    StateReason: str
    EventSourceArn: str
    Destination: "ReplayDestinationTypeDef"
    EventStartTime: datetime
    EventEndTime: datetime
    EventLastReplayedTime: datetime
    ReplayStartTime: datetime
    ReplayEndTime: datetime


class DescribeRuleResponseTypeDef(TypedDict, total=False):
    Name: str
    Arn: str
    EventPattern: str
    ScheduleExpression: str
    State: RuleState
    Description: str
    RoleArn: str
    ManagedBy: str
    EventBusName: str
    CreatedBy: str


class _RequiredEcsParametersTypeDef(TypedDict):
    TaskDefinitionArn: str


class EcsParametersTypeDef(_RequiredEcsParametersTypeDef, total=False):
    TaskCount: int
    LaunchType: LaunchType
    NetworkConfiguration: "NetworkConfigurationTypeDef"
    PlatformVersion: str
    Group: str


class EventBusTypeDef(TypedDict, total=False):
    Name: str
    Arn: str
    Policy: str


class EventSourceTypeDef(TypedDict, total=False):
    Arn: str
    CreatedBy: str
    CreationTime: datetime
    ExpirationTime: datetime
    Name: str
    State: EventSourceState


class HttpParametersTypeDef(TypedDict, total=False):
    PathParameterValues: List[str]
    HeaderParameters: Dict[str, str]
    QueryStringParameters: Dict[str, str]


class _RequiredInputTransformerTypeDef(TypedDict):
    InputTemplate: str


class InputTransformerTypeDef(_RequiredInputTransformerTypeDef, total=False):
    InputPathsMap: Dict[str, str]


class KinesisParametersTypeDef(TypedDict):
    PartitionKeyPath: str


class ListApiDestinationsResponseTypeDef(TypedDict, total=False):
    ApiDestinations: List["ApiDestinationTypeDef"]
    NextToken: str


class ListArchivesResponseTypeDef(TypedDict, total=False):
    Archives: List["ArchiveTypeDef"]
    NextToken: str


class ListConnectionsResponseTypeDef(TypedDict, total=False):
    Connections: List["ConnectionTypeDef"]
    NextToken: str


class ListEventBusesResponseTypeDef(TypedDict, total=False):
    EventBuses: List["EventBusTypeDef"]
    NextToken: str


class ListEventSourcesResponseTypeDef(TypedDict, total=False):
    EventSources: List["EventSourceTypeDef"]
    NextToken: str


class ListPartnerEventSourceAccountsResponseTypeDef(TypedDict, total=False):
    PartnerEventSourceAccounts: List["PartnerEventSourceAccountTypeDef"]
    NextToken: str


class ListPartnerEventSourcesResponseTypeDef(TypedDict, total=False):
    PartnerEventSources: List["PartnerEventSourceTypeDef"]
    NextToken: str


class ListReplaysResponseTypeDef(TypedDict, total=False):
    Replays: List["ReplayTypeDef"]
    NextToken: str


class ListRuleNamesByTargetResponseTypeDef(TypedDict, total=False):
    RuleNames: List[str]
    NextToken: str


class ListRulesResponseTypeDef(TypedDict, total=False):
    Rules: List["RuleTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class ListTargetsByRuleResponseTypeDef(TypedDict, total=False):
    Targets: List["TargetTypeDef"]
    NextToken: str


class NetworkConfigurationTypeDef(TypedDict, total=False):
    awsvpcConfiguration: "AwsVpcConfigurationTypeDef"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PartnerEventSourceAccountTypeDef(TypedDict, total=False):
    Account: str
    CreationTime: datetime
    ExpirationTime: datetime
    State: EventSourceState


class PartnerEventSourceTypeDef(TypedDict, total=False):
    Arn: str
    Name: str


class PutEventsRequestEntryTypeDef(TypedDict, total=False):
    Time: datetime
    Source: str
    Resources: List[str]
    DetailType: str
    Detail: str
    EventBusName: str
    TraceHeader: str


class PutEventsResponseTypeDef(TypedDict, total=False):
    FailedEntryCount: int
    Entries: List["PutEventsResultEntryTypeDef"]


class PutEventsResultEntryTypeDef(TypedDict, total=False):
    EventId: str
    ErrorCode: str
    ErrorMessage: str


class PutPartnerEventsRequestEntryTypeDef(TypedDict, total=False):
    Time: datetime
    Source: str
    Resources: List[str]
    DetailType: str
    Detail: str


class PutPartnerEventsResponseTypeDef(TypedDict, total=False):
    FailedEntryCount: int
    Entries: List["PutPartnerEventsResultEntryTypeDef"]


class PutPartnerEventsResultEntryTypeDef(TypedDict, total=False):
    EventId: str
    ErrorCode: str
    ErrorMessage: str


class PutRuleResponseTypeDef(TypedDict, total=False):
    RuleArn: str


class PutTargetsResponseTypeDef(TypedDict, total=False):
    FailedEntryCount: int
    FailedEntries: List["PutTargetsResultEntryTypeDef"]


class PutTargetsResultEntryTypeDef(TypedDict, total=False):
    TargetId: str
    ErrorCode: str
    ErrorMessage: str


class _RequiredRedshiftDataParametersTypeDef(TypedDict):
    Database: str
    Sql: str


class RedshiftDataParametersTypeDef(_RequiredRedshiftDataParametersTypeDef, total=False):
    SecretManagerArn: str
    DbUser: str
    StatementName: str
    WithEvent: bool


class RemoveTargetsResponseTypeDef(TypedDict, total=False):
    FailedEntryCount: int
    FailedEntries: List["RemoveTargetsResultEntryTypeDef"]


class RemoveTargetsResultEntryTypeDef(TypedDict, total=False):
    TargetId: str
    ErrorCode: str
    ErrorMessage: str


class _RequiredReplayDestinationTypeDef(TypedDict):
    Arn: str


class ReplayDestinationTypeDef(_RequiredReplayDestinationTypeDef, total=False):
    FilterArns: List[str]


class ReplayTypeDef(TypedDict, total=False):
    ReplayName: str
    EventSourceArn: str
    State: ReplayState
    StateReason: str
    EventStartTime: datetime
    EventEndTime: datetime
    EventLastReplayedTime: datetime
    ReplayStartTime: datetime
    ReplayEndTime: datetime


class RetryPolicyTypeDef(TypedDict, total=False):
    MaximumRetryAttempts: int
    MaximumEventAgeInSeconds: int


class RuleTypeDef(TypedDict, total=False):
    Name: str
    Arn: str
    EventPattern: str
    State: RuleState
    Description: str
    ScheduleExpression: str
    RoleArn: str
    ManagedBy: str
    EventBusName: str


class RunCommandParametersTypeDef(TypedDict):
    RunCommandTargets: List["RunCommandTargetTypeDef"]


class RunCommandTargetTypeDef(TypedDict):
    Key: str
    Values: List[str]


class SageMakerPipelineParameterTypeDef(TypedDict):
    Name: str
    Value: str


class SageMakerPipelineParametersTypeDef(TypedDict, total=False):
    PipelineParameterList: List["SageMakerPipelineParameterTypeDef"]


class SqsParametersTypeDef(TypedDict, total=False):
    MessageGroupId: str


class StartReplayResponseTypeDef(TypedDict, total=False):
    ReplayArn: str
    State: ReplayState
    StateReason: str
    ReplayStartTime: datetime


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class _RequiredTargetTypeDef(TypedDict):
    Id: str
    Arn: str


class TargetTypeDef(_RequiredTargetTypeDef, total=False):
    RoleArn: str
    Input: str
    InputPath: str
    InputTransformer: "InputTransformerTypeDef"
    KinesisParameters: "KinesisParametersTypeDef"
    RunCommandParameters: "RunCommandParametersTypeDef"
    EcsParameters: "EcsParametersTypeDef"
    BatchParameters: "BatchParametersTypeDef"
    SqsParameters: "SqsParametersTypeDef"
    HttpParameters: "HttpParametersTypeDef"
    RedshiftDataParameters: "RedshiftDataParametersTypeDef"
    SageMakerPipelineParameters: "SageMakerPipelineParametersTypeDef"
    DeadLetterConfig: "DeadLetterConfigTypeDef"
    RetryPolicy: "RetryPolicyTypeDef"


class TestEventPatternResponseTypeDef(TypedDict, total=False):
    Result: bool


class UpdateApiDestinationResponseTypeDef(TypedDict, total=False):
    ApiDestinationArn: str
    ApiDestinationState: ApiDestinationState
    CreationTime: datetime
    LastModifiedTime: datetime


class UpdateArchiveResponseTypeDef(TypedDict, total=False):
    ArchiveArn: str
    State: ArchiveState
    StateReason: str
    CreationTime: datetime


class UpdateConnectionApiKeyAuthRequestParametersTypeDef(TypedDict, total=False):
    ApiKeyName: str
    ApiKeyValue: str


class UpdateConnectionAuthRequestParametersTypeDef(TypedDict, total=False):
    BasicAuthParameters: "UpdateConnectionBasicAuthRequestParametersTypeDef"
    OAuthParameters: "UpdateConnectionOAuthRequestParametersTypeDef"
    ApiKeyAuthParameters: "UpdateConnectionApiKeyAuthRequestParametersTypeDef"
    InvocationHttpParameters: "ConnectionHttpParametersTypeDef"


class UpdateConnectionBasicAuthRequestParametersTypeDef(TypedDict, total=False):
    Username: str
    Password: str


class UpdateConnectionOAuthClientRequestParametersTypeDef(TypedDict, total=False):
    ClientID: str
    ClientSecret: str


class UpdateConnectionOAuthRequestParametersTypeDef(TypedDict, total=False):
    ClientParameters: "UpdateConnectionOAuthClientRequestParametersTypeDef"
    AuthorizationEndpoint: str
    HttpMethod: ConnectionOAuthHttpMethod
    OAuthHttpParameters: "ConnectionHttpParametersTypeDef"


class UpdateConnectionResponseTypeDef(TypedDict, total=False):
    ConnectionArn: str
    ConnectionState: ConnectionState
    CreationTime: datetime
    LastModifiedTime: datetime
    LastAuthorizedTime: datetime
