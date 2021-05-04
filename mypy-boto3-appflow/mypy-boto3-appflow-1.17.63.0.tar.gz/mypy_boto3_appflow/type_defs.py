"""
Type annotations for appflow service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_appflow/type_defs.html)

Usage::

    ```python
    from mypy_boto3_appflow.type_defs import AggregationConfigTypeDef

    data: AggregationConfigTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_appflow.literals import (
    AggregationType,
    ConnectionMode,
    ConnectorType,
    DatadogConnectorOperator,
    DataPullMode,
    DynatraceConnectorOperator,
    ExecutionStatus,
    FileType,
    FlowStatus,
    GoogleAnalyticsConnectorOperator,
    InforNexusConnectorOperator,
    MarketoConnectorOperator,
    Operator,
    OperatorPropertiesKeys,
    PrefixFormat,
    PrefixType,
    S3ConnectorOperator,
    SalesforceConnectorOperator,
    ScheduleFrequencyType,
    ServiceNowConnectorOperator,
    SingularConnectorOperator,
    SlackConnectorOperator,
    TaskType,
    TrendmicroConnectorOperator,
    TriggerType,
    VeevaConnectorOperator,
    WriteOperationType,
    ZendeskConnectorOperator,
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
    "AggregationConfigTypeDef",
    "AmplitudeConnectorProfileCredentialsTypeDef",
    "AmplitudeSourcePropertiesTypeDef",
    "ConnectorConfigurationTypeDef",
    "ConnectorEntityFieldTypeDef",
    "ConnectorEntityTypeDef",
    "ConnectorMetadataTypeDef",
    "ConnectorOAuthRequestTypeDef",
    "ConnectorOperatorTypeDef",
    "ConnectorProfileConfigTypeDef",
    "ConnectorProfileCredentialsTypeDef",
    "ConnectorProfilePropertiesTypeDef",
    "ConnectorProfileTypeDef",
    "CreateConnectorProfileResponseTypeDef",
    "CreateFlowResponseTypeDef",
    "CustomerProfilesDestinationPropertiesTypeDef",
    "DatadogConnectorProfileCredentialsTypeDef",
    "DatadogConnectorProfilePropertiesTypeDef",
    "DatadogSourcePropertiesTypeDef",
    "DescribeConnectorEntityResponseTypeDef",
    "DescribeConnectorProfilesResponseTypeDef",
    "DescribeConnectorsResponseTypeDef",
    "DescribeFlowExecutionRecordsResponseTypeDef",
    "DescribeFlowResponseTypeDef",
    "DestinationConnectorPropertiesTypeDef",
    "DestinationFieldPropertiesTypeDef",
    "DestinationFlowConfigTypeDef",
    "DynatraceConnectorProfileCredentialsTypeDef",
    "DynatraceConnectorProfilePropertiesTypeDef",
    "DynatraceSourcePropertiesTypeDef",
    "ErrorHandlingConfigTypeDef",
    "ErrorInfoTypeDef",
    "EventBridgeDestinationPropertiesTypeDef",
    "ExecutionDetailsTypeDef",
    "ExecutionRecordTypeDef",
    "ExecutionResultTypeDef",
    "FieldTypeDetailsTypeDef",
    "FlowDefinitionTypeDef",
    "GoogleAnalyticsConnectorProfileCredentialsTypeDef",
    "GoogleAnalyticsMetadataTypeDef",
    "GoogleAnalyticsSourcePropertiesTypeDef",
    "HoneycodeConnectorProfileCredentialsTypeDef",
    "HoneycodeDestinationPropertiesTypeDef",
    "HoneycodeMetadataTypeDef",
    "IncrementalPullConfigTypeDef",
    "InforNexusConnectorProfileCredentialsTypeDef",
    "InforNexusConnectorProfilePropertiesTypeDef",
    "InforNexusSourcePropertiesTypeDef",
    "ListConnectorEntitiesResponseTypeDef",
    "ListFlowsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MarketoConnectorProfileCredentialsTypeDef",
    "MarketoConnectorProfilePropertiesTypeDef",
    "MarketoSourcePropertiesTypeDef",
    "PrefixConfigTypeDef",
    "RedshiftConnectorProfileCredentialsTypeDef",
    "RedshiftConnectorProfilePropertiesTypeDef",
    "RedshiftDestinationPropertiesTypeDef",
    "S3DestinationPropertiesTypeDef",
    "S3OutputFormatConfigTypeDef",
    "S3SourcePropertiesTypeDef",
    "SalesforceConnectorProfileCredentialsTypeDef",
    "SalesforceConnectorProfilePropertiesTypeDef",
    "SalesforceDestinationPropertiesTypeDef",
    "SalesforceMetadataTypeDef",
    "SalesforceSourcePropertiesTypeDef",
    "ScheduledTriggerPropertiesTypeDef",
    "ServiceNowConnectorProfileCredentialsTypeDef",
    "ServiceNowConnectorProfilePropertiesTypeDef",
    "ServiceNowSourcePropertiesTypeDef",
    "SingularConnectorProfileCredentialsTypeDef",
    "SingularSourcePropertiesTypeDef",
    "SlackConnectorProfileCredentialsTypeDef",
    "SlackConnectorProfilePropertiesTypeDef",
    "SlackMetadataTypeDef",
    "SlackSourcePropertiesTypeDef",
    "SnowflakeConnectorProfileCredentialsTypeDef",
    "SnowflakeConnectorProfilePropertiesTypeDef",
    "SnowflakeDestinationPropertiesTypeDef",
    "SnowflakeMetadataTypeDef",
    "SourceConnectorPropertiesTypeDef",
    "SourceFieldPropertiesTypeDef",
    "SourceFlowConfigTypeDef",
    "StartFlowResponseTypeDef",
    "StopFlowResponseTypeDef",
    "SupportedFieldTypeDetailsTypeDef",
    "TaskTypeDef",
    "TrendmicroConnectorProfileCredentialsTypeDef",
    "TrendmicroSourcePropertiesTypeDef",
    "TriggerConfigTypeDef",
    "TriggerPropertiesTypeDef",
    "UpdateConnectorProfileResponseTypeDef",
    "UpdateFlowResponseTypeDef",
    "UpsolverDestinationPropertiesTypeDef",
    "UpsolverS3OutputFormatConfigTypeDef",
    "VeevaConnectorProfileCredentialsTypeDef",
    "VeevaConnectorProfilePropertiesTypeDef",
    "VeevaSourcePropertiesTypeDef",
    "ZendeskConnectorProfileCredentialsTypeDef",
    "ZendeskConnectorProfilePropertiesTypeDef",
    "ZendeskDestinationPropertiesTypeDef",
    "ZendeskMetadataTypeDef",
    "ZendeskSourcePropertiesTypeDef",
)


class AggregationConfigTypeDef(TypedDict, total=False):
    aggregationType: AggregationType


class AmplitudeConnectorProfileCredentialsTypeDef(TypedDict):
    apiKey: str
    secretKey: str


AmplitudeSourcePropertiesTypeDef = TypedDict("AmplitudeSourcePropertiesTypeDef", {"object": str})


class ConnectorConfigurationTypeDef(TypedDict, total=False):
    canUseAsSource: bool
    canUseAsDestination: bool
    supportedDestinationConnectors: List[ConnectorType]
    supportedSchedulingFrequencies: List[ScheduleFrequencyType]
    isPrivateLinkEnabled: bool
    isPrivateLinkEndpointUrlRequired: bool
    supportedTriggerTypes: List[TriggerType]
    connectorMetadata: "ConnectorMetadataTypeDef"


class _RequiredConnectorEntityFieldTypeDef(TypedDict):
    identifier: str


class ConnectorEntityFieldTypeDef(_RequiredConnectorEntityFieldTypeDef, total=False):
    label: str
    supportedFieldTypeDetails: "SupportedFieldTypeDetailsTypeDef"
    description: str
    sourceProperties: "SourceFieldPropertiesTypeDef"
    destinationProperties: "DestinationFieldPropertiesTypeDef"


class _RequiredConnectorEntityTypeDef(TypedDict):
    name: str


class ConnectorEntityTypeDef(_RequiredConnectorEntityTypeDef, total=False):
    label: str
    hasNestedEntities: bool


class ConnectorMetadataTypeDef(TypedDict, total=False):
    Amplitude: Dict[str, Any]
    Datadog: Dict[str, Any]
    Dynatrace: Dict[str, Any]
    GoogleAnalytics: "GoogleAnalyticsMetadataTypeDef"
    InforNexus: Dict[str, Any]
    Marketo: Dict[str, Any]
    Redshift: Dict[str, Any]
    S3: Dict[str, Any]
    Salesforce: "SalesforceMetadataTypeDef"
    ServiceNow: Dict[str, Any]
    Singular: Dict[str, Any]
    Slack: "SlackMetadataTypeDef"
    Snowflake: "SnowflakeMetadataTypeDef"
    Trendmicro: Dict[str, Any]
    Veeva: Dict[str, Any]
    Zendesk: "ZendeskMetadataTypeDef"
    EventBridge: Dict[str, Any]
    Upsolver: Dict[str, Any]
    CustomerProfiles: Dict[str, Any]
    Honeycode: "HoneycodeMetadataTypeDef"


class ConnectorOAuthRequestTypeDef(TypedDict, total=False):
    authCode: str
    redirectUri: str


class ConnectorOperatorTypeDef(TypedDict, total=False):
    Amplitude: Literal["BETWEEN"]
    Datadog: DatadogConnectorOperator
    Dynatrace: DynatraceConnectorOperator
    GoogleAnalytics: GoogleAnalyticsConnectorOperator
    InforNexus: InforNexusConnectorOperator
    Marketo: MarketoConnectorOperator
    S3: S3ConnectorOperator
    Salesforce: SalesforceConnectorOperator
    ServiceNow: ServiceNowConnectorOperator
    Singular: SingularConnectorOperator
    Slack: SlackConnectorOperator
    Trendmicro: TrendmicroConnectorOperator
    Veeva: VeevaConnectorOperator
    Zendesk: ZendeskConnectorOperator


class ConnectorProfileConfigTypeDef(TypedDict):
    connectorProfileProperties: "ConnectorProfilePropertiesTypeDef"
    connectorProfileCredentials: "ConnectorProfileCredentialsTypeDef"


class ConnectorProfileCredentialsTypeDef(TypedDict, total=False):
    Amplitude: "AmplitudeConnectorProfileCredentialsTypeDef"
    Datadog: "DatadogConnectorProfileCredentialsTypeDef"
    Dynatrace: "DynatraceConnectorProfileCredentialsTypeDef"
    GoogleAnalytics: "GoogleAnalyticsConnectorProfileCredentialsTypeDef"
    Honeycode: "HoneycodeConnectorProfileCredentialsTypeDef"
    InforNexus: "InforNexusConnectorProfileCredentialsTypeDef"
    Marketo: "MarketoConnectorProfileCredentialsTypeDef"
    Redshift: "RedshiftConnectorProfileCredentialsTypeDef"
    Salesforce: "SalesforceConnectorProfileCredentialsTypeDef"
    ServiceNow: "ServiceNowConnectorProfileCredentialsTypeDef"
    Singular: "SingularConnectorProfileCredentialsTypeDef"
    Slack: "SlackConnectorProfileCredentialsTypeDef"
    Snowflake: "SnowflakeConnectorProfileCredentialsTypeDef"
    Trendmicro: "TrendmicroConnectorProfileCredentialsTypeDef"
    Veeva: "VeevaConnectorProfileCredentialsTypeDef"
    Zendesk: "ZendeskConnectorProfileCredentialsTypeDef"


class ConnectorProfilePropertiesTypeDef(TypedDict, total=False):
    Amplitude: Dict[str, Any]
    Datadog: "DatadogConnectorProfilePropertiesTypeDef"
    Dynatrace: "DynatraceConnectorProfilePropertiesTypeDef"
    GoogleAnalytics: Dict[str, Any]
    Honeycode: Dict[str, Any]
    InforNexus: "InforNexusConnectorProfilePropertiesTypeDef"
    Marketo: "MarketoConnectorProfilePropertiesTypeDef"
    Redshift: "RedshiftConnectorProfilePropertiesTypeDef"
    Salesforce: "SalesforceConnectorProfilePropertiesTypeDef"
    ServiceNow: "ServiceNowConnectorProfilePropertiesTypeDef"
    Singular: Dict[str, Any]
    Slack: "SlackConnectorProfilePropertiesTypeDef"
    Snowflake: "SnowflakeConnectorProfilePropertiesTypeDef"
    Trendmicro: Dict[str, Any]
    Veeva: "VeevaConnectorProfilePropertiesTypeDef"
    Zendesk: "ZendeskConnectorProfilePropertiesTypeDef"


class ConnectorProfileTypeDef(TypedDict, total=False):
    connectorProfileArn: str
    connectorProfileName: str
    connectorType: ConnectorType
    connectionMode: ConnectionMode
    credentialsArn: str
    connectorProfileProperties: "ConnectorProfilePropertiesTypeDef"
    createdAt: datetime
    lastUpdatedAt: datetime


class CreateConnectorProfileResponseTypeDef(TypedDict, total=False):
    connectorProfileArn: str


class CreateFlowResponseTypeDef(TypedDict, total=False):
    flowArn: str
    flowStatus: FlowStatus


class _RequiredCustomerProfilesDestinationPropertiesTypeDef(TypedDict):
    domainName: str


class CustomerProfilesDestinationPropertiesTypeDef(
    _RequiredCustomerProfilesDestinationPropertiesTypeDef, total=False
):
    objectTypeName: str


class DatadogConnectorProfileCredentialsTypeDef(TypedDict):
    apiKey: str
    applicationKey: str


class DatadogConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str


DatadogSourcePropertiesTypeDef = TypedDict("DatadogSourcePropertiesTypeDef", {"object": str})


class DescribeConnectorEntityResponseTypeDef(TypedDict):
    connectorEntityFields: List["ConnectorEntityFieldTypeDef"]


class DescribeConnectorProfilesResponseTypeDef(TypedDict, total=False):
    connectorProfileDetails: List["ConnectorProfileTypeDef"]
    nextToken: str


class DescribeConnectorsResponseTypeDef(TypedDict, total=False):
    connectorConfigurations: Dict[ConnectorType, "ConnectorConfigurationTypeDef"]
    nextToken: str


class DescribeFlowExecutionRecordsResponseTypeDef(TypedDict, total=False):
    flowExecutions: List["ExecutionRecordTypeDef"]
    nextToken: str


class DescribeFlowResponseTypeDef(TypedDict, total=False):
    flowArn: str
    description: str
    flowName: str
    kmsArn: str
    flowStatus: FlowStatus
    flowStatusMessage: str
    sourceFlowConfig: "SourceFlowConfigTypeDef"
    destinationFlowConfigList: List["DestinationFlowConfigTypeDef"]
    lastRunExecutionDetails: "ExecutionDetailsTypeDef"
    triggerConfig: "TriggerConfigTypeDef"
    tasks: List["TaskTypeDef"]
    createdAt: datetime
    lastUpdatedAt: datetime
    createdBy: str
    lastUpdatedBy: str
    tags: Dict[str, str]


class DestinationConnectorPropertiesTypeDef(TypedDict, total=False):
    Redshift: "RedshiftDestinationPropertiesTypeDef"
    S3: "S3DestinationPropertiesTypeDef"
    Salesforce: "SalesforceDestinationPropertiesTypeDef"
    Snowflake: "SnowflakeDestinationPropertiesTypeDef"
    EventBridge: "EventBridgeDestinationPropertiesTypeDef"
    LookoutMetrics: Dict[str, Any]
    Upsolver: "UpsolverDestinationPropertiesTypeDef"
    Honeycode: "HoneycodeDestinationPropertiesTypeDef"
    CustomerProfiles: "CustomerProfilesDestinationPropertiesTypeDef"
    Zendesk: "ZendeskDestinationPropertiesTypeDef"


class DestinationFieldPropertiesTypeDef(TypedDict, total=False):
    isCreatable: bool
    isNullable: bool
    isUpsertable: bool
    isUpdatable: bool
    supportedWriteOperations: List[WriteOperationType]


class _RequiredDestinationFlowConfigTypeDef(TypedDict):
    connectorType: ConnectorType
    destinationConnectorProperties: "DestinationConnectorPropertiesTypeDef"


class DestinationFlowConfigTypeDef(_RequiredDestinationFlowConfigTypeDef, total=False):
    connectorProfileName: str


class DynatraceConnectorProfileCredentialsTypeDef(TypedDict):
    apiToken: str


class DynatraceConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str


DynatraceSourcePropertiesTypeDef = TypedDict("DynatraceSourcePropertiesTypeDef", {"object": str})


class ErrorHandlingConfigTypeDef(TypedDict, total=False):
    failOnFirstDestinationError: bool
    bucketPrefix: str
    bucketName: str


class ErrorInfoTypeDef(TypedDict, total=False):
    putFailuresCount: int
    executionMessage: str


_RequiredEventBridgeDestinationPropertiesTypeDef = TypedDict(
    "_RequiredEventBridgeDestinationPropertiesTypeDef", {"object": str}
)
_OptionalEventBridgeDestinationPropertiesTypeDef = TypedDict(
    "_OptionalEventBridgeDestinationPropertiesTypeDef",
    {"errorHandlingConfig": "ErrorHandlingConfigTypeDef"},
    total=False,
)


class EventBridgeDestinationPropertiesTypeDef(
    _RequiredEventBridgeDestinationPropertiesTypeDef,
    _OptionalEventBridgeDestinationPropertiesTypeDef,
):
    pass


class ExecutionDetailsTypeDef(TypedDict, total=False):
    mostRecentExecutionMessage: str
    mostRecentExecutionTime: datetime
    mostRecentExecutionStatus: ExecutionStatus


class ExecutionRecordTypeDef(TypedDict, total=False):
    executionId: str
    executionStatus: ExecutionStatus
    executionResult: "ExecutionResultTypeDef"
    startedAt: datetime
    lastUpdatedAt: datetime
    dataPullStartTime: datetime
    dataPullEndTime: datetime


class ExecutionResultTypeDef(TypedDict, total=False):
    errorInfo: "ErrorInfoTypeDef"
    bytesProcessed: int
    bytesWritten: int
    recordsProcessed: int


class _RequiredFieldTypeDetailsTypeDef(TypedDict):
    fieldType: str
    filterOperators: List[Operator]


class FieldTypeDetailsTypeDef(_RequiredFieldTypeDetailsTypeDef, total=False):
    supportedValues: List[str]


class FlowDefinitionTypeDef(TypedDict, total=False):
    flowArn: str
    description: str
    flowName: str
    flowStatus: FlowStatus
    sourceConnectorType: ConnectorType
    destinationConnectorType: ConnectorType
    triggerType: TriggerType
    createdAt: datetime
    lastUpdatedAt: datetime
    createdBy: str
    lastUpdatedBy: str
    tags: Dict[str, str]
    lastRunExecutionDetails: "ExecutionDetailsTypeDef"


class _RequiredGoogleAnalyticsConnectorProfileCredentialsTypeDef(TypedDict):
    clientId: str
    clientSecret: str


class GoogleAnalyticsConnectorProfileCredentialsTypeDef(
    _RequiredGoogleAnalyticsConnectorProfileCredentialsTypeDef, total=False
):
    accessToken: str
    refreshToken: str
    oAuthRequest: "ConnectorOAuthRequestTypeDef"


class GoogleAnalyticsMetadataTypeDef(TypedDict, total=False):
    oAuthScopes: List[str]


GoogleAnalyticsSourcePropertiesTypeDef = TypedDict(
    "GoogleAnalyticsSourcePropertiesTypeDef", {"object": str}
)


class HoneycodeConnectorProfileCredentialsTypeDef(TypedDict, total=False):
    accessToken: str
    refreshToken: str
    oAuthRequest: "ConnectorOAuthRequestTypeDef"


_RequiredHoneycodeDestinationPropertiesTypeDef = TypedDict(
    "_RequiredHoneycodeDestinationPropertiesTypeDef", {"object": str}
)
_OptionalHoneycodeDestinationPropertiesTypeDef = TypedDict(
    "_OptionalHoneycodeDestinationPropertiesTypeDef",
    {"errorHandlingConfig": "ErrorHandlingConfigTypeDef"},
    total=False,
)


class HoneycodeDestinationPropertiesTypeDef(
    _RequiredHoneycodeDestinationPropertiesTypeDef, _OptionalHoneycodeDestinationPropertiesTypeDef
):
    pass


class HoneycodeMetadataTypeDef(TypedDict, total=False):
    oAuthScopes: List[str]


class IncrementalPullConfigTypeDef(TypedDict, total=False):
    datetimeTypeFieldName: str


class InforNexusConnectorProfileCredentialsTypeDef(TypedDict):
    accessKeyId: str
    userId: str
    secretAccessKey: str
    datakey: str


class InforNexusConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str


InforNexusSourcePropertiesTypeDef = TypedDict("InforNexusSourcePropertiesTypeDef", {"object": str})


class ListConnectorEntitiesResponseTypeDef(TypedDict):
    connectorEntityMap: Dict[str, List["ConnectorEntityTypeDef"]]


class ListFlowsResponseTypeDef(TypedDict, total=False):
    flows: List["FlowDefinitionTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class _RequiredMarketoConnectorProfileCredentialsTypeDef(TypedDict):
    clientId: str
    clientSecret: str


class MarketoConnectorProfileCredentialsTypeDef(
    _RequiredMarketoConnectorProfileCredentialsTypeDef, total=False
):
    accessToken: str
    oAuthRequest: "ConnectorOAuthRequestTypeDef"


class MarketoConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str


MarketoSourcePropertiesTypeDef = TypedDict("MarketoSourcePropertiesTypeDef", {"object": str})


class PrefixConfigTypeDef(TypedDict, total=False):
    prefixType: PrefixType
    prefixFormat: PrefixFormat


class RedshiftConnectorProfileCredentialsTypeDef(TypedDict):
    username: str
    password: str


class _RequiredRedshiftConnectorProfilePropertiesTypeDef(TypedDict):
    databaseUrl: str
    bucketName: str
    roleArn: str


class RedshiftConnectorProfilePropertiesTypeDef(
    _RequiredRedshiftConnectorProfilePropertiesTypeDef, total=False
):
    bucketPrefix: str


_RequiredRedshiftDestinationPropertiesTypeDef = TypedDict(
    "_RequiredRedshiftDestinationPropertiesTypeDef", {"object": str, "intermediateBucketName": str}
)
_OptionalRedshiftDestinationPropertiesTypeDef = TypedDict(
    "_OptionalRedshiftDestinationPropertiesTypeDef",
    {"bucketPrefix": str, "errorHandlingConfig": "ErrorHandlingConfigTypeDef"},
    total=False,
)


class RedshiftDestinationPropertiesTypeDef(
    _RequiredRedshiftDestinationPropertiesTypeDef, _OptionalRedshiftDestinationPropertiesTypeDef
):
    pass


class _RequiredS3DestinationPropertiesTypeDef(TypedDict):
    bucketName: str


class S3DestinationPropertiesTypeDef(_RequiredS3DestinationPropertiesTypeDef, total=False):
    bucketPrefix: str
    s3OutputFormatConfig: "S3OutputFormatConfigTypeDef"


class S3OutputFormatConfigTypeDef(TypedDict, total=False):
    fileType: FileType
    prefixConfig: "PrefixConfigTypeDef"
    aggregationConfig: "AggregationConfigTypeDef"


class _RequiredS3SourcePropertiesTypeDef(TypedDict):
    bucketName: str


class S3SourcePropertiesTypeDef(_RequiredS3SourcePropertiesTypeDef, total=False):
    bucketPrefix: str


class SalesforceConnectorProfileCredentialsTypeDef(TypedDict, total=False):
    accessToken: str
    refreshToken: str
    oAuthRequest: "ConnectorOAuthRequestTypeDef"
    clientCredentialsArn: str


class SalesforceConnectorProfilePropertiesTypeDef(TypedDict, total=False):
    instanceUrl: str
    isSandboxEnvironment: bool


_RequiredSalesforceDestinationPropertiesTypeDef = TypedDict(
    "_RequiredSalesforceDestinationPropertiesTypeDef", {"object": str}
)
_OptionalSalesforceDestinationPropertiesTypeDef = TypedDict(
    "_OptionalSalesforceDestinationPropertiesTypeDef",
    {
        "idFieldNames": List[str],
        "errorHandlingConfig": "ErrorHandlingConfigTypeDef",
        "writeOperationType": WriteOperationType,
    },
    total=False,
)


class SalesforceDestinationPropertiesTypeDef(
    _RequiredSalesforceDestinationPropertiesTypeDef, _OptionalSalesforceDestinationPropertiesTypeDef
):
    pass


class SalesforceMetadataTypeDef(TypedDict, total=False):
    oAuthScopes: List[str]


_RequiredSalesforceSourcePropertiesTypeDef = TypedDict(
    "_RequiredSalesforceSourcePropertiesTypeDef", {"object": str}
)
_OptionalSalesforceSourcePropertiesTypeDef = TypedDict(
    "_OptionalSalesforceSourcePropertiesTypeDef",
    {"enableDynamicFieldUpdate": bool, "includeDeletedRecords": bool},
    total=False,
)


class SalesforceSourcePropertiesTypeDef(
    _RequiredSalesforceSourcePropertiesTypeDef, _OptionalSalesforceSourcePropertiesTypeDef
):
    pass


class _RequiredScheduledTriggerPropertiesTypeDef(TypedDict):
    scheduleExpression: str


class ScheduledTriggerPropertiesTypeDef(_RequiredScheduledTriggerPropertiesTypeDef, total=False):
    dataPullMode: DataPullMode
    scheduleStartTime: datetime
    scheduleEndTime: datetime
    timezone: str
    scheduleOffset: int
    firstExecutionFrom: datetime


class ServiceNowConnectorProfileCredentialsTypeDef(TypedDict):
    username: str
    password: str


class ServiceNowConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str


ServiceNowSourcePropertiesTypeDef = TypedDict("ServiceNowSourcePropertiesTypeDef", {"object": str})


class SingularConnectorProfileCredentialsTypeDef(TypedDict):
    apiKey: str


SingularSourcePropertiesTypeDef = TypedDict("SingularSourcePropertiesTypeDef", {"object": str})


class _RequiredSlackConnectorProfileCredentialsTypeDef(TypedDict):
    clientId: str
    clientSecret: str


class SlackConnectorProfileCredentialsTypeDef(
    _RequiredSlackConnectorProfileCredentialsTypeDef, total=False
):
    accessToken: str
    oAuthRequest: "ConnectorOAuthRequestTypeDef"


class SlackConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str


class SlackMetadataTypeDef(TypedDict, total=False):
    oAuthScopes: List[str]


SlackSourcePropertiesTypeDef = TypedDict("SlackSourcePropertiesTypeDef", {"object": str})


class SnowflakeConnectorProfileCredentialsTypeDef(TypedDict):
    username: str
    password: str


class _RequiredSnowflakeConnectorProfilePropertiesTypeDef(TypedDict):
    warehouse: str
    stage: str
    bucketName: str


class SnowflakeConnectorProfilePropertiesTypeDef(
    _RequiredSnowflakeConnectorProfilePropertiesTypeDef, total=False
):
    bucketPrefix: str
    privateLinkServiceName: str
    accountName: str
    region: str


_RequiredSnowflakeDestinationPropertiesTypeDef = TypedDict(
    "_RequiredSnowflakeDestinationPropertiesTypeDef", {"object": str, "intermediateBucketName": str}
)
_OptionalSnowflakeDestinationPropertiesTypeDef = TypedDict(
    "_OptionalSnowflakeDestinationPropertiesTypeDef",
    {"bucketPrefix": str, "errorHandlingConfig": "ErrorHandlingConfigTypeDef"},
    total=False,
)


class SnowflakeDestinationPropertiesTypeDef(
    _RequiredSnowflakeDestinationPropertiesTypeDef, _OptionalSnowflakeDestinationPropertiesTypeDef
):
    pass


class SnowflakeMetadataTypeDef(TypedDict, total=False):
    supportedRegions: List[str]


class SourceConnectorPropertiesTypeDef(TypedDict, total=False):
    Amplitude: "AmplitudeSourcePropertiesTypeDef"
    Datadog: "DatadogSourcePropertiesTypeDef"
    Dynatrace: "DynatraceSourcePropertiesTypeDef"
    GoogleAnalytics: "GoogleAnalyticsSourcePropertiesTypeDef"
    InforNexus: "InforNexusSourcePropertiesTypeDef"
    Marketo: "MarketoSourcePropertiesTypeDef"
    S3: "S3SourcePropertiesTypeDef"
    Salesforce: "SalesforceSourcePropertiesTypeDef"
    ServiceNow: "ServiceNowSourcePropertiesTypeDef"
    Singular: "SingularSourcePropertiesTypeDef"
    Slack: "SlackSourcePropertiesTypeDef"
    Trendmicro: "TrendmicroSourcePropertiesTypeDef"
    Veeva: "VeevaSourcePropertiesTypeDef"
    Zendesk: "ZendeskSourcePropertiesTypeDef"


class SourceFieldPropertiesTypeDef(TypedDict, total=False):
    isRetrievable: bool
    isQueryable: bool


class _RequiredSourceFlowConfigTypeDef(TypedDict):
    connectorType: ConnectorType
    sourceConnectorProperties: "SourceConnectorPropertiesTypeDef"


class SourceFlowConfigTypeDef(_RequiredSourceFlowConfigTypeDef, total=False):
    connectorProfileName: str
    incrementalPullConfig: "IncrementalPullConfigTypeDef"


class StartFlowResponseTypeDef(TypedDict, total=False):
    flowArn: str
    flowStatus: FlowStatus
    executionId: str


class StopFlowResponseTypeDef(TypedDict, total=False):
    flowArn: str
    flowStatus: FlowStatus


class SupportedFieldTypeDetailsTypeDef(TypedDict):
    v1: "FieldTypeDetailsTypeDef"


class _RequiredTaskTypeDef(TypedDict):
    sourceFields: List[str]
    taskType: TaskType


class TaskTypeDef(_RequiredTaskTypeDef, total=False):
    connectorOperator: "ConnectorOperatorTypeDef"
    destinationField: str
    taskProperties: Dict[OperatorPropertiesKeys, str]


class TrendmicroConnectorProfileCredentialsTypeDef(TypedDict):
    apiSecretKey: str


TrendmicroSourcePropertiesTypeDef = TypedDict("TrendmicroSourcePropertiesTypeDef", {"object": str})


class _RequiredTriggerConfigTypeDef(TypedDict):
    triggerType: TriggerType


class TriggerConfigTypeDef(_RequiredTriggerConfigTypeDef, total=False):
    triggerProperties: "TriggerPropertiesTypeDef"


class TriggerPropertiesTypeDef(TypedDict, total=False):
    Scheduled: "ScheduledTriggerPropertiesTypeDef"


class UpdateConnectorProfileResponseTypeDef(TypedDict, total=False):
    connectorProfileArn: str


class UpdateFlowResponseTypeDef(TypedDict, total=False):
    flowStatus: FlowStatus


class _RequiredUpsolverDestinationPropertiesTypeDef(TypedDict):
    bucketName: str
    s3OutputFormatConfig: "UpsolverS3OutputFormatConfigTypeDef"


class UpsolverDestinationPropertiesTypeDef(
    _RequiredUpsolverDestinationPropertiesTypeDef, total=False
):
    bucketPrefix: str


class _RequiredUpsolverS3OutputFormatConfigTypeDef(TypedDict):
    prefixConfig: "PrefixConfigTypeDef"


class UpsolverS3OutputFormatConfigTypeDef(
    _RequiredUpsolverS3OutputFormatConfigTypeDef, total=False
):
    fileType: FileType
    aggregationConfig: "AggregationConfigTypeDef"


class VeevaConnectorProfileCredentialsTypeDef(TypedDict):
    username: str
    password: str


class VeevaConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str


VeevaSourcePropertiesTypeDef = TypedDict("VeevaSourcePropertiesTypeDef", {"object": str})


class _RequiredZendeskConnectorProfileCredentialsTypeDef(TypedDict):
    clientId: str
    clientSecret: str


class ZendeskConnectorProfileCredentialsTypeDef(
    _RequiredZendeskConnectorProfileCredentialsTypeDef, total=False
):
    accessToken: str
    oAuthRequest: "ConnectorOAuthRequestTypeDef"


class ZendeskConnectorProfilePropertiesTypeDef(TypedDict):
    instanceUrl: str


_RequiredZendeskDestinationPropertiesTypeDef = TypedDict(
    "_RequiredZendeskDestinationPropertiesTypeDef", {"object": str}
)
_OptionalZendeskDestinationPropertiesTypeDef = TypedDict(
    "_OptionalZendeskDestinationPropertiesTypeDef",
    {
        "idFieldNames": List[str],
        "errorHandlingConfig": "ErrorHandlingConfigTypeDef",
        "writeOperationType": WriteOperationType,
    },
    total=False,
)


class ZendeskDestinationPropertiesTypeDef(
    _RequiredZendeskDestinationPropertiesTypeDef, _OptionalZendeskDestinationPropertiesTypeDef
):
    pass


class ZendeskMetadataTypeDef(TypedDict, total=False):
    oAuthScopes: List[str]


ZendeskSourcePropertiesTypeDef = TypedDict("ZendeskSourcePropertiesTypeDef", {"object": str})
