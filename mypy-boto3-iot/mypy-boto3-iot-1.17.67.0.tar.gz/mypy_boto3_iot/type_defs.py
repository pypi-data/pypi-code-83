"""
Type annotations for iot service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot.type_defs import AbortConfigTypeDef

    data: AbortConfigTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_iot.literals import (
    ActionType,
    AuditCheckRunStatus,
    AuditFindingSeverity,
    AuditFrequency,
    AuditMitigationActionsExecutionStatus,
    AuditMitigationActionsTaskStatus,
    AuditTaskStatus,
    AuditTaskType,
    AuthDecision,
    AuthorizerStatus,
    AutoRegistrationStatus,
    AwsJobAbortCriteriaFailureType,
    CACertificateStatus,
    CannedAccessControlList,
    CertificateMode,
    CertificateStatus,
    ComparisonOperator,
    ConfidenceLevel,
    CustomMetricType,
    DayOfWeek,
    DetectMitigationActionExecutionStatus,
    DetectMitigationActionsTaskStatus,
    DimensionValueOperator,
    DomainConfigurationStatus,
    DomainType,
    DynamicGroupStatus,
    DynamoKeyType,
    EventType,
    FieldType,
    IndexStatus,
    JobExecutionFailureType,
    JobExecutionStatus,
    JobStatus,
    LogLevel,
    LogTargetType,
    MessageFormat,
    MitigationActionType,
    ModelStatus,
    OTAUpdateStatus,
    ProtocolType,
    ReportType,
    ResourceType,
    ServerCertificateStatus,
    ServiceType,
    Status,
    TargetSelection,
    ThingConnectivityIndexingMode,
    ThingGroupIndexingMode,
    ThingIndexingMode,
    TopicRuleDestinationStatus,
    ViolationEventType,
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
    "AbortConfigTypeDef",
    "AbortCriteriaTypeDef",
    "ActionTypeDef",
    "ActiveViolationTypeDef",
    "AddThingsToThingGroupParamsTypeDef",
    "AlertTargetTypeDef",
    "AllowedTypeDef",
    "AssetPropertyTimestampTypeDef",
    "AssetPropertyValueTypeDef",
    "AssetPropertyVariantTypeDef",
    "AssociateTargetsWithJobResponseTypeDef",
    "AttributePayloadTypeDef",
    "AuditCheckConfigurationTypeDef",
    "AuditCheckDetailsTypeDef",
    "AuditFindingTypeDef",
    "AuditMitigationActionExecutionMetadataTypeDef",
    "AuditMitigationActionsTaskMetadataTypeDef",
    "AuditMitigationActionsTaskTargetTypeDef",
    "AuditNotificationTargetTypeDef",
    "AuditSuppressionTypeDef",
    "AuditTaskMetadataTypeDef",
    "AuthInfoTypeDef",
    "AuthResultTypeDef",
    "AuthorizerConfigTypeDef",
    "AuthorizerDescriptionTypeDef",
    "AuthorizerSummaryTypeDef",
    "AwsJobAbortConfigTypeDef",
    "AwsJobAbortCriteriaTypeDef",
    "AwsJobExecutionsRolloutConfigTypeDef",
    "AwsJobExponentialRolloutRateTypeDef",
    "AwsJobPresignedUrlConfigTypeDef",
    "AwsJobRateIncreaseCriteriaTypeDef",
    "AwsJobTimeoutConfigTypeDef",
    "BehaviorCriteriaTypeDef",
    "BehaviorModelTrainingSummaryTypeDef",
    "BehaviorTypeDef",
    "BillingGroupMetadataTypeDef",
    "BillingGroupPropertiesTypeDef",
    "CACertificateDescriptionTypeDef",
    "CACertificateTypeDef",
    "CancelJobResponseTypeDef",
    "CertificateDescriptionTypeDef",
    "CertificateTypeDef",
    "CertificateValidityTypeDef",
    "CloudwatchAlarmActionTypeDef",
    "CloudwatchLogsActionTypeDef",
    "CloudwatchMetricActionTypeDef",
    "CodeSigningCertificateChainTypeDef",
    "CodeSigningSignatureTypeDef",
    "CodeSigningTypeDef",
    "ConfigurationTypeDef",
    "CreateAuthorizerResponseTypeDef",
    "CreateBillingGroupResponseTypeDef",
    "CreateCertificateFromCsrResponseTypeDef",
    "CreateCustomMetricResponseTypeDef",
    "CreateDimensionResponseTypeDef",
    "CreateDomainConfigurationResponseTypeDef",
    "CreateDynamicThingGroupResponseTypeDef",
    "CreateJobResponseTypeDef",
    "CreateKeysAndCertificateResponseTypeDef",
    "CreateMitigationActionResponseTypeDef",
    "CreateOTAUpdateResponseTypeDef",
    "CreatePolicyResponseTypeDef",
    "CreatePolicyVersionResponseTypeDef",
    "CreateProvisioningClaimResponseTypeDef",
    "CreateProvisioningTemplateResponseTypeDef",
    "CreateProvisioningTemplateVersionResponseTypeDef",
    "CreateRoleAliasResponseTypeDef",
    "CreateScheduledAuditResponseTypeDef",
    "CreateSecurityProfileResponseTypeDef",
    "CreateStreamResponseTypeDef",
    "CreateThingGroupResponseTypeDef",
    "CreateThingResponseTypeDef",
    "CreateThingTypeResponseTypeDef",
    "CreateTopicRuleDestinationResponseTypeDef",
    "CustomCodeSigningTypeDef",
    "DeniedTypeDef",
    "DescribeAccountAuditConfigurationResponseTypeDef",
    "DescribeAuditFindingResponseTypeDef",
    "DescribeAuditMitigationActionsTaskResponseTypeDef",
    "DescribeAuditSuppressionResponseTypeDef",
    "DescribeAuditTaskResponseTypeDef",
    "DescribeAuthorizerResponseTypeDef",
    "DescribeBillingGroupResponseTypeDef",
    "DescribeCACertificateResponseTypeDef",
    "DescribeCertificateResponseTypeDef",
    "DescribeCustomMetricResponseTypeDef",
    "DescribeDefaultAuthorizerResponseTypeDef",
    "DescribeDetectMitigationActionsTaskResponseTypeDef",
    "DescribeDimensionResponseTypeDef",
    "DescribeDomainConfigurationResponseTypeDef",
    "DescribeEndpointResponseTypeDef",
    "DescribeEventConfigurationsResponseTypeDef",
    "DescribeIndexResponseTypeDef",
    "DescribeJobExecutionResponseTypeDef",
    "DescribeJobResponseTypeDef",
    "DescribeMitigationActionResponseTypeDef",
    "DescribeProvisioningTemplateResponseTypeDef",
    "DescribeProvisioningTemplateVersionResponseTypeDef",
    "DescribeRoleAliasResponseTypeDef",
    "DescribeScheduledAuditResponseTypeDef",
    "DescribeSecurityProfileResponseTypeDef",
    "DescribeStreamResponseTypeDef",
    "DescribeThingGroupResponseTypeDef",
    "DescribeThingRegistrationTaskResponseTypeDef",
    "DescribeThingResponseTypeDef",
    "DescribeThingTypeResponseTypeDef",
    "DestinationTypeDef",
    "DetectMitigationActionExecutionTypeDef",
    "DetectMitigationActionsTaskStatisticsTypeDef",
    "DetectMitigationActionsTaskSummaryTypeDef",
    "DetectMitigationActionsTaskTargetTypeDef",
    "DomainConfigurationSummaryTypeDef",
    "DynamoDBActionTypeDef",
    "DynamoDBv2ActionTypeDef",
    "EffectivePolicyTypeDef",
    "ElasticsearchActionTypeDef",
    "EnableIoTLoggingParamsTypeDef",
    "ErrorInfoTypeDef",
    "ExplicitDenyTypeDef",
    "ExponentialRolloutRateTypeDef",
    "FieldTypeDef",
    "FileLocationTypeDef",
    "FirehoseActionTypeDef",
    "GetBehaviorModelTrainingSummariesResponseTypeDef",
    "GetCardinalityResponseTypeDef",
    "GetEffectivePoliciesResponseTypeDef",
    "GetIndexingConfigurationResponseTypeDef",
    "GetJobDocumentResponseTypeDef",
    "GetLoggingOptionsResponseTypeDef",
    "GetOTAUpdateResponseTypeDef",
    "GetPercentilesResponseTypeDef",
    "GetPolicyResponseTypeDef",
    "GetPolicyVersionResponseTypeDef",
    "GetRegistrationCodeResponseTypeDef",
    "GetStatisticsResponseTypeDef",
    "GetTopicRuleDestinationResponseTypeDef",
    "GetTopicRuleResponseTypeDef",
    "GetV2LoggingOptionsResponseTypeDef",
    "GroupNameAndArnTypeDef",
    "HttpActionHeaderTypeDef",
    "HttpActionTypeDef",
    "HttpAuthorizationTypeDef",
    "HttpContextTypeDef",
    "HttpUrlDestinationConfigurationTypeDef",
    "HttpUrlDestinationPropertiesTypeDef",
    "HttpUrlDestinationSummaryTypeDef",
    "ImplicitDenyTypeDef",
    "IotAnalyticsActionTypeDef",
    "IotEventsActionTypeDef",
    "IotSiteWiseActionTypeDef",
    "JobExecutionStatusDetailsTypeDef",
    "JobExecutionSummaryForJobTypeDef",
    "JobExecutionSummaryForThingTypeDef",
    "JobExecutionSummaryTypeDef",
    "JobExecutionTypeDef",
    "JobExecutionsRolloutConfigTypeDef",
    "JobProcessDetailsTypeDef",
    "JobSummaryTypeDef",
    "JobTypeDef",
    "KafkaActionTypeDef",
    "KeyPairTypeDef",
    "KinesisActionTypeDef",
    "LambdaActionTypeDef",
    "ListActiveViolationsResponseTypeDef",
    "ListAttachedPoliciesResponseTypeDef",
    "ListAuditFindingsResponseTypeDef",
    "ListAuditMitigationActionsExecutionsResponseTypeDef",
    "ListAuditMitigationActionsTasksResponseTypeDef",
    "ListAuditSuppressionsResponseTypeDef",
    "ListAuditTasksResponseTypeDef",
    "ListAuthorizersResponseTypeDef",
    "ListBillingGroupsResponseTypeDef",
    "ListCACertificatesResponseTypeDef",
    "ListCertificatesByCAResponseTypeDef",
    "ListCertificatesResponseTypeDef",
    "ListCustomMetricsResponseTypeDef",
    "ListDetectMitigationActionsExecutionsResponseTypeDef",
    "ListDetectMitigationActionsTasksResponseTypeDef",
    "ListDimensionsResponseTypeDef",
    "ListDomainConfigurationsResponseTypeDef",
    "ListIndicesResponseTypeDef",
    "ListJobExecutionsForJobResponseTypeDef",
    "ListJobExecutionsForThingResponseTypeDef",
    "ListJobsResponseTypeDef",
    "ListMitigationActionsResponseTypeDef",
    "ListOTAUpdatesResponseTypeDef",
    "ListOutgoingCertificatesResponseTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListPolicyPrincipalsResponseTypeDef",
    "ListPolicyVersionsResponseTypeDef",
    "ListPrincipalPoliciesResponseTypeDef",
    "ListPrincipalThingsResponseTypeDef",
    "ListProvisioningTemplateVersionsResponseTypeDef",
    "ListProvisioningTemplatesResponseTypeDef",
    "ListRoleAliasesResponseTypeDef",
    "ListScheduledAuditsResponseTypeDef",
    "ListSecurityProfilesForTargetResponseTypeDef",
    "ListSecurityProfilesResponseTypeDef",
    "ListStreamsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTargetsForPolicyResponseTypeDef",
    "ListTargetsForSecurityProfileResponseTypeDef",
    "ListThingGroupsForThingResponseTypeDef",
    "ListThingGroupsResponseTypeDef",
    "ListThingPrincipalsResponseTypeDef",
    "ListThingRegistrationTaskReportsResponseTypeDef",
    "ListThingRegistrationTasksResponseTypeDef",
    "ListThingTypesResponseTypeDef",
    "ListThingsInBillingGroupResponseTypeDef",
    "ListThingsInThingGroupResponseTypeDef",
    "ListThingsResponseTypeDef",
    "ListTopicRuleDestinationsResponseTypeDef",
    "ListTopicRulesResponseTypeDef",
    "ListV2LoggingLevelsResponseTypeDef",
    "ListViolationEventsResponseTypeDef",
    "LogTargetConfigurationTypeDef",
    "LogTargetTypeDef",
    "LoggingOptionsPayloadTypeDef",
    "MachineLearningDetectionConfigTypeDef",
    "MetricDimensionTypeDef",
    "MetricToRetainTypeDef",
    "MetricValueTypeDef",
    "MitigationActionIdentifierTypeDef",
    "MitigationActionParamsTypeDef",
    "MitigationActionTypeDef",
    "MqttContextTypeDef",
    "NonCompliantResourceTypeDef",
    "OTAUpdateFileTypeDef",
    "OTAUpdateInfoTypeDef",
    "OTAUpdateSummaryTypeDef",
    "OutgoingCertificateTypeDef",
    "PaginatorConfigTypeDef",
    "PercentPairTypeDef",
    "PolicyTypeDef",
    "PolicyVersionIdentifierTypeDef",
    "PolicyVersionTypeDef",
    "PresignedUrlConfigTypeDef",
    "ProvisioningHookTypeDef",
    "ProvisioningTemplateSummaryTypeDef",
    "ProvisioningTemplateVersionSummaryTypeDef",
    "PublishFindingToSnsParamsTypeDef",
    "PutAssetPropertyValueEntryTypeDef",
    "PutItemInputTypeDef",
    "RateIncreaseCriteriaTypeDef",
    "RegisterCACertificateResponseTypeDef",
    "RegisterCertificateResponseTypeDef",
    "RegisterCertificateWithoutCAResponseTypeDef",
    "RegisterThingResponseTypeDef",
    "RegistrationConfigTypeDef",
    "RelatedResourceTypeDef",
    "ReplaceDefaultPolicyVersionParamsTypeDef",
    "RepublishActionTypeDef",
    "ResourceIdentifierTypeDef",
    "RoleAliasDescriptionTypeDef",
    "S3ActionTypeDef",
    "S3DestinationTypeDef",
    "S3LocationTypeDef",
    "SalesforceActionTypeDef",
    "ScheduledAuditMetadataTypeDef",
    "SearchIndexResponseTypeDef",
    "SecurityProfileIdentifierTypeDef",
    "SecurityProfileTargetMappingTypeDef",
    "SecurityProfileTargetTypeDef",
    "ServerCertificateSummaryTypeDef",
    "SetDefaultAuthorizerResponseTypeDef",
    "SigV4AuthorizationTypeDef",
    "SigningProfileParameterTypeDef",
    "SnsActionTypeDef",
    "SqsActionTypeDef",
    "StartAuditMitigationActionsTaskResponseTypeDef",
    "StartDetectMitigationActionsTaskResponseTypeDef",
    "StartOnDemandAuditTaskResponseTypeDef",
    "StartSigningJobParameterTypeDef",
    "StartThingRegistrationTaskResponseTypeDef",
    "StatisticalThresholdTypeDef",
    "StatisticsTypeDef",
    "StepFunctionsActionTypeDef",
    "StreamFileTypeDef",
    "StreamInfoTypeDef",
    "StreamSummaryTypeDef",
    "StreamTypeDef",
    "TagTypeDef",
    "TaskStatisticsForAuditCheckTypeDef",
    "TaskStatisticsTypeDef",
    "TestAuthorizationResponseTypeDef",
    "TestInvokeAuthorizerResponseTypeDef",
    "ThingAttributeTypeDef",
    "ThingConnectivityTypeDef",
    "ThingDocumentTypeDef",
    "ThingGroupDocumentTypeDef",
    "ThingGroupIndexingConfigurationTypeDef",
    "ThingGroupMetadataTypeDef",
    "ThingGroupPropertiesTypeDef",
    "ThingIndexingConfigurationTypeDef",
    "ThingTypeDefinitionTypeDef",
    "ThingTypeMetadataTypeDef",
    "ThingTypePropertiesTypeDef",
    "TimeoutConfigTypeDef",
    "TimestreamActionTypeDef",
    "TimestreamDimensionTypeDef",
    "TimestreamTimestampTypeDef",
    "TlsContextTypeDef",
    "TopicRuleDestinationConfigurationTypeDef",
    "TopicRuleDestinationSummaryTypeDef",
    "TopicRuleDestinationTypeDef",
    "TopicRuleListItemTypeDef",
    "TopicRulePayloadTypeDef",
    "TopicRuleTypeDef",
    "TransferCertificateResponseTypeDef",
    "TransferDataTypeDef",
    "UpdateAuthorizerResponseTypeDef",
    "UpdateBillingGroupResponseTypeDef",
    "UpdateCACertificateParamsTypeDef",
    "UpdateCustomMetricResponseTypeDef",
    "UpdateDeviceCertificateParamsTypeDef",
    "UpdateDimensionResponseTypeDef",
    "UpdateDomainConfigurationResponseTypeDef",
    "UpdateDynamicThingGroupResponseTypeDef",
    "UpdateMitigationActionResponseTypeDef",
    "UpdateRoleAliasResponseTypeDef",
    "UpdateScheduledAuditResponseTypeDef",
    "UpdateSecurityProfileResponseTypeDef",
    "UpdateStreamResponseTypeDef",
    "UpdateThingGroupResponseTypeDef",
    "ValidateSecurityProfileBehaviorsResponseTypeDef",
    "ValidationErrorTypeDef",
    "ViolationEventAdditionalInfoTypeDef",
    "ViolationEventOccurrenceRangeTypeDef",
    "ViolationEventTypeDef",
    "VpcDestinationConfigurationTypeDef",
    "VpcDestinationPropertiesTypeDef",
    "VpcDestinationSummaryTypeDef",
)


class AbortConfigTypeDef(TypedDict):
    criteriaList: List["AbortCriteriaTypeDef"]


class AbortCriteriaTypeDef(TypedDict):
    failureType: JobExecutionFailureType
    action: Literal["CANCEL"]
    thresholdPercentage: float
    minNumberOfExecutedThings: int


ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "dynamoDB": "DynamoDBActionTypeDef",
        "dynamoDBv2": "DynamoDBv2ActionTypeDef",
        "lambda": "LambdaActionTypeDef",
        "sns": "SnsActionTypeDef",
        "sqs": "SqsActionTypeDef",
        "kinesis": "KinesisActionTypeDef",
        "republish": "RepublishActionTypeDef",
        "s3": "S3ActionTypeDef",
        "firehose": "FirehoseActionTypeDef",
        "cloudwatchMetric": "CloudwatchMetricActionTypeDef",
        "cloudwatchAlarm": "CloudwatchAlarmActionTypeDef",
        "cloudwatchLogs": "CloudwatchLogsActionTypeDef",
        "elasticsearch": "ElasticsearchActionTypeDef",
        "salesforce": "SalesforceActionTypeDef",
        "iotAnalytics": "IotAnalyticsActionTypeDef",
        "iotEvents": "IotEventsActionTypeDef",
        "iotSiteWise": "IotSiteWiseActionTypeDef",
        "stepFunctions": "StepFunctionsActionTypeDef",
        "timestream": "TimestreamActionTypeDef",
        "http": "HttpActionTypeDef",
        "kafka": "KafkaActionTypeDef",
    },
    total=False,
)


class ActiveViolationTypeDef(TypedDict, total=False):
    violationId: str
    thingName: str
    securityProfileName: str
    behavior: "BehaviorTypeDef"
    lastViolationValue: "MetricValueTypeDef"
    violationEventAdditionalInfo: "ViolationEventAdditionalInfoTypeDef"
    lastViolationTime: datetime
    violationStartTime: datetime


class _RequiredAddThingsToThingGroupParamsTypeDef(TypedDict):
    thingGroupNames: List[str]


class AddThingsToThingGroupParamsTypeDef(_RequiredAddThingsToThingGroupParamsTypeDef, total=False):
    overrideDynamicGroups: bool


class AlertTargetTypeDef(TypedDict):
    alertTargetArn: str
    roleArn: str


class AllowedTypeDef(TypedDict, total=False):
    policies: List["PolicyTypeDef"]


class _RequiredAssetPropertyTimestampTypeDef(TypedDict):
    timeInSeconds: str


class AssetPropertyTimestampTypeDef(_RequiredAssetPropertyTimestampTypeDef, total=False):
    offsetInNanos: str


class _RequiredAssetPropertyValueTypeDef(TypedDict):
    value: "AssetPropertyVariantTypeDef"
    timestamp: "AssetPropertyTimestampTypeDef"


class AssetPropertyValueTypeDef(_RequiredAssetPropertyValueTypeDef, total=False):
    quality: str


class AssetPropertyVariantTypeDef(TypedDict, total=False):
    stringValue: str
    integerValue: str
    doubleValue: str
    booleanValue: str


class AssociateTargetsWithJobResponseTypeDef(TypedDict, total=False):
    jobArn: str
    jobId: str
    description: str


class AttributePayloadTypeDef(TypedDict, total=False):
    attributes: Dict[str, str]
    merge: bool


class AuditCheckConfigurationTypeDef(TypedDict, total=False):
    enabled: bool


class AuditCheckDetailsTypeDef(TypedDict, total=False):
    checkRunStatus: AuditCheckRunStatus
    checkCompliant: bool
    totalResourcesCount: int
    nonCompliantResourcesCount: int
    suppressedNonCompliantResourcesCount: int
    errorCode: str
    message: str


class AuditFindingTypeDef(TypedDict, total=False):
    findingId: str
    taskId: str
    checkName: str
    taskStartTime: datetime
    findingTime: datetime
    severity: AuditFindingSeverity
    nonCompliantResource: "NonCompliantResourceTypeDef"
    relatedResources: List["RelatedResourceTypeDef"]
    reasonForNonCompliance: str
    reasonForNonComplianceCode: str
    isSuppressed: bool


class AuditMitigationActionExecutionMetadataTypeDef(TypedDict, total=False):
    taskId: str
    findingId: str
    actionName: str
    actionId: str
    status: AuditMitigationActionsExecutionStatus
    startTime: datetime
    endTime: datetime
    errorCode: str
    message: str


class AuditMitigationActionsTaskMetadataTypeDef(TypedDict, total=False):
    taskId: str
    startTime: datetime
    taskStatus: AuditMitigationActionsTaskStatus


class AuditMitigationActionsTaskTargetTypeDef(TypedDict, total=False):
    auditTaskId: str
    findingIds: List[str]
    auditCheckToReasonCodeFilter: Dict[str, List[str]]


class AuditNotificationTargetTypeDef(TypedDict, total=False):
    targetArn: str
    roleArn: str
    enabled: bool


class _RequiredAuditSuppressionTypeDef(TypedDict):
    checkName: str
    resourceIdentifier: "ResourceIdentifierTypeDef"


class AuditSuppressionTypeDef(_RequiredAuditSuppressionTypeDef, total=False):
    expirationDate: datetime
    suppressIndefinitely: bool
    description: str


class AuditTaskMetadataTypeDef(TypedDict, total=False):
    taskId: str
    taskStatus: AuditTaskStatus
    taskType: AuditTaskType


class _RequiredAuthInfoTypeDef(TypedDict):
    resources: List[str]


class AuthInfoTypeDef(_RequiredAuthInfoTypeDef, total=False):
    actionType: ActionType


class AuthResultTypeDef(TypedDict, total=False):
    authInfo: "AuthInfoTypeDef"
    allowed: "AllowedTypeDef"
    denied: "DeniedTypeDef"
    authDecision: AuthDecision
    missingContextValues: List[str]


class AuthorizerConfigTypeDef(TypedDict, total=False):
    defaultAuthorizerName: str
    allowAuthorizerOverride: bool


class AuthorizerDescriptionTypeDef(TypedDict, total=False):
    authorizerName: str
    authorizerArn: str
    authorizerFunctionArn: str
    tokenKeyName: str
    tokenSigningPublicKeys: Dict[str, str]
    status: AuthorizerStatus
    creationDate: datetime
    lastModifiedDate: datetime
    signingDisabled: bool


class AuthorizerSummaryTypeDef(TypedDict, total=False):
    authorizerName: str
    authorizerArn: str


class AwsJobAbortConfigTypeDef(TypedDict):
    abortCriteriaList: List["AwsJobAbortCriteriaTypeDef"]


class AwsJobAbortCriteriaTypeDef(TypedDict):
    failureType: AwsJobAbortCriteriaFailureType
    action: Literal["CANCEL"]
    thresholdPercentage: float
    minNumberOfExecutedThings: int


class AwsJobExecutionsRolloutConfigTypeDef(TypedDict, total=False):
    maximumPerMinute: int
    exponentialRate: "AwsJobExponentialRolloutRateTypeDef"


class AwsJobExponentialRolloutRateTypeDef(TypedDict):
    baseRatePerMinute: int
    incrementFactor: float
    rateIncreaseCriteria: "AwsJobRateIncreaseCriteriaTypeDef"


class AwsJobPresignedUrlConfigTypeDef(TypedDict, total=False):
    expiresInSec: int


class AwsJobRateIncreaseCriteriaTypeDef(TypedDict, total=False):
    numberOfNotifiedThings: int
    numberOfSucceededThings: int


class AwsJobTimeoutConfigTypeDef(TypedDict, total=False):
    inProgressTimeoutInMinutes: int


class BehaviorCriteriaTypeDef(TypedDict, total=False):
    comparisonOperator: ComparisonOperator
    value: "MetricValueTypeDef"
    durationSeconds: int
    consecutiveDatapointsToAlarm: int
    consecutiveDatapointsToClear: int
    statisticalThreshold: "StatisticalThresholdTypeDef"
    mlDetectionConfig: "MachineLearningDetectionConfigTypeDef"


class BehaviorModelTrainingSummaryTypeDef(TypedDict, total=False):
    securityProfileName: str
    behaviorName: str
    trainingDataCollectionStartDate: datetime
    modelStatus: ModelStatus
    datapointsCollectionPercentage: float
    lastModelRefreshDate: datetime


class _RequiredBehaviorTypeDef(TypedDict):
    name: str


class BehaviorTypeDef(_RequiredBehaviorTypeDef, total=False):
    metric: str
    metricDimension: "MetricDimensionTypeDef"
    criteria: "BehaviorCriteriaTypeDef"
    suppressAlerts: bool


class BillingGroupMetadataTypeDef(TypedDict, total=False):
    creationDate: datetime


class BillingGroupPropertiesTypeDef(TypedDict, total=False):
    billingGroupDescription: str


class CACertificateDescriptionTypeDef(TypedDict, total=False):
    certificateArn: str
    certificateId: str
    status: CACertificateStatus
    certificatePem: str
    ownedBy: str
    creationDate: datetime
    autoRegistrationStatus: AutoRegistrationStatus
    lastModifiedDate: datetime
    customerVersion: int
    generationId: str
    validity: "CertificateValidityTypeDef"


class CACertificateTypeDef(TypedDict, total=False):
    certificateArn: str
    certificateId: str
    status: CACertificateStatus
    creationDate: datetime


class CancelJobResponseTypeDef(TypedDict, total=False):
    jobArn: str
    jobId: str
    description: str


class CertificateDescriptionTypeDef(TypedDict, total=False):
    certificateArn: str
    certificateId: str
    caCertificateId: str
    status: CertificateStatus
    certificatePem: str
    ownedBy: str
    previousOwnedBy: str
    creationDate: datetime
    lastModifiedDate: datetime
    customerVersion: int
    transferData: "TransferDataTypeDef"
    generationId: str
    validity: "CertificateValidityTypeDef"
    certificateMode: CertificateMode


class CertificateTypeDef(TypedDict, total=False):
    certificateArn: str
    certificateId: str
    status: CertificateStatus
    certificateMode: CertificateMode
    creationDate: datetime


class CertificateValidityTypeDef(TypedDict, total=False):
    notBefore: datetime
    notAfter: datetime


class CloudwatchAlarmActionTypeDef(TypedDict):
    roleArn: str
    alarmName: str
    stateReason: str
    stateValue: str


class CloudwatchLogsActionTypeDef(TypedDict):
    roleArn: str
    logGroupName: str


class _RequiredCloudwatchMetricActionTypeDef(TypedDict):
    roleArn: str
    metricNamespace: str
    metricName: str
    metricValue: str
    metricUnit: str


class CloudwatchMetricActionTypeDef(_RequiredCloudwatchMetricActionTypeDef, total=False):
    metricTimestamp: str


class CodeSigningCertificateChainTypeDef(TypedDict, total=False):
    certificateName: str
    inlineDocument: str


class CodeSigningSignatureTypeDef(TypedDict, total=False):
    inlineDocument: Union[bytes, IO[bytes]]


class CodeSigningTypeDef(TypedDict, total=False):
    awsSignerJobId: str
    startSigningJobParameter: "StartSigningJobParameterTypeDef"
    customCodeSigning: "CustomCodeSigningTypeDef"


class ConfigurationTypeDef(TypedDict, total=False):
    Enabled: bool


class CreateAuthorizerResponseTypeDef(TypedDict, total=False):
    authorizerName: str
    authorizerArn: str


class CreateBillingGroupResponseTypeDef(TypedDict, total=False):
    billingGroupName: str
    billingGroupArn: str
    billingGroupId: str


class CreateCertificateFromCsrResponseTypeDef(TypedDict, total=False):
    certificateArn: str
    certificateId: str
    certificatePem: str


class CreateCustomMetricResponseTypeDef(TypedDict, total=False):
    metricName: str
    metricArn: str


class CreateDimensionResponseTypeDef(TypedDict, total=False):
    name: str
    arn: str


class CreateDomainConfigurationResponseTypeDef(TypedDict, total=False):
    domainConfigurationName: str
    domainConfigurationArn: str


class CreateDynamicThingGroupResponseTypeDef(TypedDict, total=False):
    thingGroupName: str
    thingGroupArn: str
    thingGroupId: str
    indexName: str
    queryString: str
    queryVersion: str


class CreateJobResponseTypeDef(TypedDict, total=False):
    jobArn: str
    jobId: str
    description: str


class CreateKeysAndCertificateResponseTypeDef(TypedDict, total=False):
    certificateArn: str
    certificateId: str
    certificatePem: str
    keyPair: "KeyPairTypeDef"


class CreateMitigationActionResponseTypeDef(TypedDict, total=False):
    actionArn: str
    actionId: str


class CreateOTAUpdateResponseTypeDef(TypedDict, total=False):
    otaUpdateId: str
    awsIotJobId: str
    otaUpdateArn: str
    awsIotJobArn: str
    otaUpdateStatus: OTAUpdateStatus


class CreatePolicyResponseTypeDef(TypedDict, total=False):
    policyName: str
    policyArn: str
    policyDocument: str
    policyVersionId: str


class CreatePolicyVersionResponseTypeDef(TypedDict, total=False):
    policyArn: str
    policyDocument: str
    policyVersionId: str
    isDefaultVersion: bool


class CreateProvisioningClaimResponseTypeDef(TypedDict, total=False):
    certificateId: str
    certificatePem: str
    keyPair: "KeyPairTypeDef"
    expiration: datetime


class CreateProvisioningTemplateResponseTypeDef(TypedDict, total=False):
    templateArn: str
    templateName: str
    defaultVersionId: int


class CreateProvisioningTemplateVersionResponseTypeDef(TypedDict, total=False):
    templateArn: str
    templateName: str
    versionId: int
    isDefaultVersion: bool


class CreateRoleAliasResponseTypeDef(TypedDict, total=False):
    roleAlias: str
    roleAliasArn: str


class CreateScheduledAuditResponseTypeDef(TypedDict, total=False):
    scheduledAuditArn: str


class CreateSecurityProfileResponseTypeDef(TypedDict, total=False):
    securityProfileName: str
    securityProfileArn: str


class CreateStreamResponseTypeDef(TypedDict, total=False):
    streamId: str
    streamArn: str
    description: str
    streamVersion: int


class CreateThingGroupResponseTypeDef(TypedDict, total=False):
    thingGroupName: str
    thingGroupArn: str
    thingGroupId: str


class CreateThingResponseTypeDef(TypedDict, total=False):
    thingName: str
    thingArn: str
    thingId: str


class CreateThingTypeResponseTypeDef(TypedDict, total=False):
    thingTypeName: str
    thingTypeArn: str
    thingTypeId: str


class CreateTopicRuleDestinationResponseTypeDef(TypedDict, total=False):
    topicRuleDestination: "TopicRuleDestinationTypeDef"


class CustomCodeSigningTypeDef(TypedDict, total=False):
    signature: "CodeSigningSignatureTypeDef"
    certificateChain: "CodeSigningCertificateChainTypeDef"
    hashAlgorithm: str
    signatureAlgorithm: str


class DeniedTypeDef(TypedDict, total=False):
    implicitDeny: "ImplicitDenyTypeDef"
    explicitDeny: "ExplicitDenyTypeDef"


class DescribeAccountAuditConfigurationResponseTypeDef(TypedDict, total=False):
    roleArn: str
    auditNotificationTargetConfigurations: Dict[Literal["SNS"], "AuditNotificationTargetTypeDef"]
    auditCheckConfigurations: Dict[str, "AuditCheckConfigurationTypeDef"]


class DescribeAuditFindingResponseTypeDef(TypedDict, total=False):
    finding: "AuditFindingTypeDef"


class DescribeAuditMitigationActionsTaskResponseTypeDef(TypedDict, total=False):
    taskStatus: AuditMitigationActionsTaskStatus
    startTime: datetime
    endTime: datetime
    taskStatistics: Dict[str, "TaskStatisticsForAuditCheckTypeDef"]
    target: "AuditMitigationActionsTaskTargetTypeDef"
    auditCheckToActionsMapping: Dict[str, List[str]]
    actionsDefinition: List["MitigationActionTypeDef"]


class DescribeAuditSuppressionResponseTypeDef(TypedDict, total=False):
    checkName: str
    resourceIdentifier: "ResourceIdentifierTypeDef"
    expirationDate: datetime
    suppressIndefinitely: bool
    description: str


class DescribeAuditTaskResponseTypeDef(TypedDict, total=False):
    taskStatus: AuditTaskStatus
    taskType: AuditTaskType
    taskStartTime: datetime
    taskStatistics: "TaskStatisticsTypeDef"
    scheduledAuditName: str
    auditDetails: Dict[str, "AuditCheckDetailsTypeDef"]


class DescribeAuthorizerResponseTypeDef(TypedDict, total=False):
    authorizerDescription: "AuthorizerDescriptionTypeDef"


class DescribeBillingGroupResponseTypeDef(TypedDict, total=False):
    billingGroupName: str
    billingGroupId: str
    billingGroupArn: str
    version: int
    billingGroupProperties: "BillingGroupPropertiesTypeDef"
    billingGroupMetadata: "BillingGroupMetadataTypeDef"


class DescribeCACertificateResponseTypeDef(TypedDict, total=False):
    certificateDescription: "CACertificateDescriptionTypeDef"
    registrationConfig: "RegistrationConfigTypeDef"


class DescribeCertificateResponseTypeDef(TypedDict, total=False):
    certificateDescription: "CertificateDescriptionTypeDef"


class DescribeCustomMetricResponseTypeDef(TypedDict, total=False):
    metricName: str
    metricArn: str
    metricType: CustomMetricType
    displayName: str
    creationDate: datetime
    lastModifiedDate: datetime


class DescribeDefaultAuthorizerResponseTypeDef(TypedDict, total=False):
    authorizerDescription: "AuthorizerDescriptionTypeDef"


class DescribeDetectMitigationActionsTaskResponseTypeDef(TypedDict, total=False):
    taskSummary: "DetectMitigationActionsTaskSummaryTypeDef"


DescribeDimensionResponseTypeDef = TypedDict(
    "DescribeDimensionResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "type": Literal["TOPIC_FILTER"],
        "stringValues": List[str],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)


class DescribeDomainConfigurationResponseTypeDef(TypedDict, total=False):
    domainConfigurationName: str
    domainConfigurationArn: str
    domainName: str
    serverCertificates: List["ServerCertificateSummaryTypeDef"]
    authorizerConfig: "AuthorizerConfigTypeDef"
    domainConfigurationStatus: DomainConfigurationStatus
    serviceType: ServiceType
    domainType: DomainType
    lastStatusChangeDate: datetime


class DescribeEndpointResponseTypeDef(TypedDict, total=False):
    endpointAddress: str


class DescribeEventConfigurationsResponseTypeDef(TypedDict, total=False):
    eventConfigurations: Dict[EventType, "ConfigurationTypeDef"]
    creationDate: datetime
    lastModifiedDate: datetime


class DescribeIndexResponseTypeDef(TypedDict, total=False):
    indexName: str
    indexStatus: IndexStatus
    schema: str


class DescribeJobExecutionResponseTypeDef(TypedDict, total=False):
    execution: "JobExecutionTypeDef"


class DescribeJobResponseTypeDef(TypedDict, total=False):
    documentSource: str
    job: "JobTypeDef"


class DescribeMitigationActionResponseTypeDef(TypedDict, total=False):
    actionName: str
    actionType: MitigationActionType
    actionArn: str
    actionId: str
    roleArn: str
    actionParams: "MitigationActionParamsTypeDef"
    creationDate: datetime
    lastModifiedDate: datetime


class DescribeProvisioningTemplateResponseTypeDef(TypedDict, total=False):
    templateArn: str
    templateName: str
    description: str
    creationDate: datetime
    lastModifiedDate: datetime
    defaultVersionId: int
    templateBody: str
    enabled: bool
    provisioningRoleArn: str
    preProvisioningHook: "ProvisioningHookTypeDef"


class DescribeProvisioningTemplateVersionResponseTypeDef(TypedDict, total=False):
    versionId: int
    creationDate: datetime
    templateBody: str
    isDefaultVersion: bool


class DescribeRoleAliasResponseTypeDef(TypedDict, total=False):
    roleAliasDescription: "RoleAliasDescriptionTypeDef"


class DescribeScheduledAuditResponseTypeDef(TypedDict, total=False):
    frequency: AuditFrequency
    dayOfMonth: str
    dayOfWeek: DayOfWeek
    targetCheckNames: List[str]
    scheduledAuditName: str
    scheduledAuditArn: str


class DescribeSecurityProfileResponseTypeDef(TypedDict, total=False):
    securityProfileName: str
    securityProfileArn: str
    securityProfileDescription: str
    behaviors: List["BehaviorTypeDef"]
    alertTargets: Dict[Literal["SNS"], "AlertTargetTypeDef"]
    additionalMetricsToRetain: List[str]
    additionalMetricsToRetainV2: List["MetricToRetainTypeDef"]
    version: int
    creationDate: datetime
    lastModifiedDate: datetime


class DescribeStreamResponseTypeDef(TypedDict, total=False):
    streamInfo: "StreamInfoTypeDef"


class DescribeThingGroupResponseTypeDef(TypedDict, total=False):
    thingGroupName: str
    thingGroupId: str
    thingGroupArn: str
    version: int
    thingGroupProperties: "ThingGroupPropertiesTypeDef"
    thingGroupMetadata: "ThingGroupMetadataTypeDef"
    indexName: str
    queryString: str
    queryVersion: str
    status: DynamicGroupStatus


class DescribeThingRegistrationTaskResponseTypeDef(TypedDict, total=False):
    taskId: str
    creationDate: datetime
    lastModifiedDate: datetime
    templateBody: str
    inputFileBucket: str
    inputFileKey: str
    roleArn: str
    status: Status
    message: str
    successCount: int
    failureCount: int
    percentageProgress: int


class DescribeThingResponseTypeDef(TypedDict, total=False):
    defaultClientId: str
    thingName: str
    thingId: str
    thingArn: str
    thingTypeName: str
    attributes: Dict[str, str]
    version: int
    billingGroupName: str


class DescribeThingTypeResponseTypeDef(TypedDict, total=False):
    thingTypeName: str
    thingTypeId: str
    thingTypeArn: str
    thingTypeProperties: "ThingTypePropertiesTypeDef"
    thingTypeMetadata: "ThingTypeMetadataTypeDef"


class DestinationTypeDef(TypedDict, total=False):
    s3Destination: "S3DestinationTypeDef"


class DetectMitigationActionExecutionTypeDef(TypedDict, total=False):
    taskId: str
    violationId: str
    actionName: str
    thingName: str
    executionStartDate: datetime
    executionEndDate: datetime
    status: DetectMitigationActionExecutionStatus
    errorCode: str
    message: str


class DetectMitigationActionsTaskStatisticsTypeDef(TypedDict, total=False):
    actionsExecuted: int
    actionsSkipped: int
    actionsFailed: int


class DetectMitigationActionsTaskSummaryTypeDef(TypedDict, total=False):
    taskId: str
    taskStatus: DetectMitigationActionsTaskStatus
    taskStartTime: datetime
    taskEndTime: datetime
    target: "DetectMitigationActionsTaskTargetTypeDef"
    violationEventOccurrenceRange: "ViolationEventOccurrenceRangeTypeDef"
    onlyActiveViolationsIncluded: bool
    suppressedAlertsIncluded: bool
    actionsDefinition: List["MitigationActionTypeDef"]
    taskStatistics: "DetectMitigationActionsTaskStatisticsTypeDef"


class DetectMitigationActionsTaskTargetTypeDef(TypedDict, total=False):
    violationIds: List[str]
    securityProfileName: str
    behaviorName: str


class DomainConfigurationSummaryTypeDef(TypedDict, total=False):
    domainConfigurationName: str
    domainConfigurationArn: str
    serviceType: ServiceType


class _RequiredDynamoDBActionTypeDef(TypedDict):
    tableName: str
    roleArn: str
    hashKeyField: str
    hashKeyValue: str


class DynamoDBActionTypeDef(_RequiredDynamoDBActionTypeDef, total=False):
    operation: str
    hashKeyType: DynamoKeyType
    rangeKeyField: str
    rangeKeyValue: str
    rangeKeyType: DynamoKeyType
    payloadField: str


class DynamoDBv2ActionTypeDef(TypedDict):
    roleArn: str
    putItem: "PutItemInputTypeDef"


class EffectivePolicyTypeDef(TypedDict, total=False):
    policyName: str
    policyArn: str
    policyDocument: str


ElasticsearchActionTypeDef = TypedDict(
    "ElasticsearchActionTypeDef",
    {"roleArn": str, "endpoint": str, "index": str, "type": str, "id": str},
)


class EnableIoTLoggingParamsTypeDef(TypedDict):
    roleArnForLogging: str
    logLevel: LogLevel


class ErrorInfoTypeDef(TypedDict, total=False):
    code: str
    message: str


class ExplicitDenyTypeDef(TypedDict, total=False):
    policies: List["PolicyTypeDef"]


class ExponentialRolloutRateTypeDef(TypedDict):
    baseRatePerMinute: int
    incrementFactor: float
    rateIncreaseCriteria: "RateIncreaseCriteriaTypeDef"


FieldTypeDef = TypedDict("FieldTypeDef", {"name": str, "type": FieldType}, total=False)


class FileLocationTypeDef(TypedDict, total=False):
    stream: "StreamTypeDef"
    s3Location: "S3LocationTypeDef"


class _RequiredFirehoseActionTypeDef(TypedDict):
    roleArn: str
    deliveryStreamName: str


class FirehoseActionTypeDef(_RequiredFirehoseActionTypeDef, total=False):
    separator: str
    batchMode: bool


class GetBehaviorModelTrainingSummariesResponseTypeDef(TypedDict, total=False):
    summaries: List["BehaviorModelTrainingSummaryTypeDef"]
    nextToken: str


class GetCardinalityResponseTypeDef(TypedDict, total=False):
    cardinality: int


class GetEffectivePoliciesResponseTypeDef(TypedDict, total=False):
    effectivePolicies: List["EffectivePolicyTypeDef"]


class GetIndexingConfigurationResponseTypeDef(TypedDict, total=False):
    thingIndexingConfiguration: "ThingIndexingConfigurationTypeDef"
    thingGroupIndexingConfiguration: "ThingGroupIndexingConfigurationTypeDef"


class GetJobDocumentResponseTypeDef(TypedDict, total=False):
    document: str


class GetLoggingOptionsResponseTypeDef(TypedDict, total=False):
    roleArn: str
    logLevel: LogLevel


class GetOTAUpdateResponseTypeDef(TypedDict, total=False):
    otaUpdateInfo: "OTAUpdateInfoTypeDef"


class GetPercentilesResponseTypeDef(TypedDict, total=False):
    percentiles: List["PercentPairTypeDef"]


class GetPolicyResponseTypeDef(TypedDict, total=False):
    policyName: str
    policyArn: str
    policyDocument: str
    defaultVersionId: str
    creationDate: datetime
    lastModifiedDate: datetime
    generationId: str


class GetPolicyVersionResponseTypeDef(TypedDict, total=False):
    policyArn: str
    policyName: str
    policyDocument: str
    policyVersionId: str
    isDefaultVersion: bool
    creationDate: datetime
    lastModifiedDate: datetime
    generationId: str


class GetRegistrationCodeResponseTypeDef(TypedDict, total=False):
    registrationCode: str


class GetStatisticsResponseTypeDef(TypedDict, total=False):
    statistics: "StatisticsTypeDef"


class GetTopicRuleDestinationResponseTypeDef(TypedDict, total=False):
    topicRuleDestination: "TopicRuleDestinationTypeDef"


class GetTopicRuleResponseTypeDef(TypedDict, total=False):
    ruleArn: str
    rule: "TopicRuleTypeDef"


class GetV2LoggingOptionsResponseTypeDef(TypedDict, total=False):
    roleArn: str
    defaultLogLevel: LogLevel
    disableAllLogs: bool


class GroupNameAndArnTypeDef(TypedDict, total=False):
    groupName: str
    groupArn: str


class HttpActionHeaderTypeDef(TypedDict):
    key: str
    value: str


class _RequiredHttpActionTypeDef(TypedDict):
    url: str


class HttpActionTypeDef(_RequiredHttpActionTypeDef, total=False):
    confirmationUrl: str
    headers: List["HttpActionHeaderTypeDef"]
    auth: "HttpAuthorizationTypeDef"


class HttpAuthorizationTypeDef(TypedDict, total=False):
    sigv4: "SigV4AuthorizationTypeDef"


class HttpContextTypeDef(TypedDict, total=False):
    headers: Dict[str, str]
    queryString: str


class HttpUrlDestinationConfigurationTypeDef(TypedDict):
    confirmationUrl: str


class HttpUrlDestinationPropertiesTypeDef(TypedDict, total=False):
    confirmationUrl: str


class HttpUrlDestinationSummaryTypeDef(TypedDict, total=False):
    confirmationUrl: str


class ImplicitDenyTypeDef(TypedDict, total=False):
    policies: List["PolicyTypeDef"]


class IotAnalyticsActionTypeDef(TypedDict, total=False):
    channelArn: str
    channelName: str
    batchMode: bool
    roleArn: str


class _RequiredIotEventsActionTypeDef(TypedDict):
    inputName: str
    roleArn: str


class IotEventsActionTypeDef(_RequiredIotEventsActionTypeDef, total=False):
    messageId: str
    batchMode: bool


class IotSiteWiseActionTypeDef(TypedDict):
    putAssetPropertyValueEntries: List["PutAssetPropertyValueEntryTypeDef"]
    roleArn: str


class JobExecutionStatusDetailsTypeDef(TypedDict, total=False):
    detailsMap: Dict[str, str]


class JobExecutionSummaryForJobTypeDef(TypedDict, total=False):
    thingArn: str
    jobExecutionSummary: "JobExecutionSummaryTypeDef"


class JobExecutionSummaryForThingTypeDef(TypedDict, total=False):
    jobId: str
    jobExecutionSummary: "JobExecutionSummaryTypeDef"


class JobExecutionSummaryTypeDef(TypedDict, total=False):
    status: JobExecutionStatus
    queuedAt: datetime
    startedAt: datetime
    lastUpdatedAt: datetime
    executionNumber: int


class JobExecutionTypeDef(TypedDict, total=False):
    jobId: str
    status: JobExecutionStatus
    forceCanceled: bool
    statusDetails: "JobExecutionStatusDetailsTypeDef"
    thingArn: str
    queuedAt: datetime
    startedAt: datetime
    lastUpdatedAt: datetime
    executionNumber: int
    versionNumber: int
    approximateSecondsBeforeTimedOut: int


class JobExecutionsRolloutConfigTypeDef(TypedDict, total=False):
    maximumPerMinute: int
    exponentialRate: "ExponentialRolloutRateTypeDef"


class JobProcessDetailsTypeDef(TypedDict, total=False):
    processingTargets: List[str]
    numberOfCanceledThings: int
    numberOfSucceededThings: int
    numberOfFailedThings: int
    numberOfRejectedThings: int
    numberOfQueuedThings: int
    numberOfInProgressThings: int
    numberOfRemovedThings: int
    numberOfTimedOutThings: int


class JobSummaryTypeDef(TypedDict, total=False):
    jobArn: str
    jobId: str
    thingGroupId: str
    targetSelection: TargetSelection
    status: JobStatus
    createdAt: datetime
    lastUpdatedAt: datetime
    completedAt: datetime


class JobTypeDef(TypedDict, total=False):
    jobArn: str
    jobId: str
    targetSelection: TargetSelection
    status: JobStatus
    forceCanceled: bool
    reasonCode: str
    comment: str
    targets: List[str]
    description: str
    presignedUrlConfig: "PresignedUrlConfigTypeDef"
    jobExecutionsRolloutConfig: "JobExecutionsRolloutConfigTypeDef"
    abortConfig: "AbortConfigTypeDef"
    createdAt: datetime
    lastUpdatedAt: datetime
    completedAt: datetime
    jobProcessDetails: "JobProcessDetailsTypeDef"
    timeoutConfig: "TimeoutConfigTypeDef"
    namespaceId: str


class _RequiredKafkaActionTypeDef(TypedDict):
    destinationArn: str
    topic: str
    clientProperties: Dict[str, str]


class KafkaActionTypeDef(_RequiredKafkaActionTypeDef, total=False):
    key: str
    partition: str


class KeyPairTypeDef(TypedDict, total=False):
    PublicKey: str
    PrivateKey: str


class _RequiredKinesisActionTypeDef(TypedDict):
    roleArn: str
    streamName: str


class KinesisActionTypeDef(_RequiredKinesisActionTypeDef, total=False):
    partitionKey: str


class LambdaActionTypeDef(TypedDict):
    functionArn: str


class ListActiveViolationsResponseTypeDef(TypedDict, total=False):
    activeViolations: List["ActiveViolationTypeDef"]
    nextToken: str


class ListAttachedPoliciesResponseTypeDef(TypedDict, total=False):
    policies: List["PolicyTypeDef"]
    nextMarker: str


class ListAuditFindingsResponseTypeDef(TypedDict, total=False):
    findings: List["AuditFindingTypeDef"]
    nextToken: str


class ListAuditMitigationActionsExecutionsResponseTypeDef(TypedDict, total=False):
    actionsExecutions: List["AuditMitigationActionExecutionMetadataTypeDef"]
    nextToken: str


class ListAuditMitigationActionsTasksResponseTypeDef(TypedDict, total=False):
    tasks: List["AuditMitigationActionsTaskMetadataTypeDef"]
    nextToken: str


class ListAuditSuppressionsResponseTypeDef(TypedDict, total=False):
    suppressions: List["AuditSuppressionTypeDef"]
    nextToken: str


class ListAuditTasksResponseTypeDef(TypedDict, total=False):
    tasks: List["AuditTaskMetadataTypeDef"]
    nextToken: str


class ListAuthorizersResponseTypeDef(TypedDict, total=False):
    authorizers: List["AuthorizerSummaryTypeDef"]
    nextMarker: str


class ListBillingGroupsResponseTypeDef(TypedDict, total=False):
    billingGroups: List["GroupNameAndArnTypeDef"]
    nextToken: str


class ListCACertificatesResponseTypeDef(TypedDict, total=False):
    certificates: List["CACertificateTypeDef"]
    nextMarker: str


class ListCertificatesByCAResponseTypeDef(TypedDict, total=False):
    certificates: List["CertificateTypeDef"]
    nextMarker: str


class ListCertificatesResponseTypeDef(TypedDict, total=False):
    certificates: List["CertificateTypeDef"]
    nextMarker: str


class ListCustomMetricsResponseTypeDef(TypedDict, total=False):
    metricNames: List[str]
    nextToken: str


class ListDetectMitigationActionsExecutionsResponseTypeDef(TypedDict, total=False):
    actionsExecutions: List["DetectMitigationActionExecutionTypeDef"]
    nextToken: str


class ListDetectMitigationActionsTasksResponseTypeDef(TypedDict, total=False):
    tasks: List["DetectMitigationActionsTaskSummaryTypeDef"]
    nextToken: str


class ListDimensionsResponseTypeDef(TypedDict, total=False):
    dimensionNames: List[str]
    nextToken: str


class ListDomainConfigurationsResponseTypeDef(TypedDict, total=False):
    domainConfigurations: List["DomainConfigurationSummaryTypeDef"]
    nextMarker: str


class ListIndicesResponseTypeDef(TypedDict, total=False):
    indexNames: List[str]
    nextToken: str


class ListJobExecutionsForJobResponseTypeDef(TypedDict, total=False):
    executionSummaries: List["JobExecutionSummaryForJobTypeDef"]
    nextToken: str


class ListJobExecutionsForThingResponseTypeDef(TypedDict, total=False):
    executionSummaries: List["JobExecutionSummaryForThingTypeDef"]
    nextToken: str


class ListJobsResponseTypeDef(TypedDict, total=False):
    jobs: List["JobSummaryTypeDef"]
    nextToken: str


class ListMitigationActionsResponseTypeDef(TypedDict, total=False):
    actionIdentifiers: List["MitigationActionIdentifierTypeDef"]
    nextToken: str


class ListOTAUpdatesResponseTypeDef(TypedDict, total=False):
    otaUpdates: List["OTAUpdateSummaryTypeDef"]
    nextToken: str


class ListOutgoingCertificatesResponseTypeDef(TypedDict, total=False):
    outgoingCertificates: List["OutgoingCertificateTypeDef"]
    nextMarker: str


class ListPoliciesResponseTypeDef(TypedDict, total=False):
    policies: List["PolicyTypeDef"]
    nextMarker: str


class ListPolicyPrincipalsResponseTypeDef(TypedDict, total=False):
    principals: List[str]
    nextMarker: str


class ListPolicyVersionsResponseTypeDef(TypedDict, total=False):
    policyVersions: List["PolicyVersionTypeDef"]


class ListPrincipalPoliciesResponseTypeDef(TypedDict, total=False):
    policies: List["PolicyTypeDef"]
    nextMarker: str


class ListPrincipalThingsResponseTypeDef(TypedDict, total=False):
    things: List[str]
    nextToken: str


class ListProvisioningTemplateVersionsResponseTypeDef(TypedDict, total=False):
    versions: List["ProvisioningTemplateVersionSummaryTypeDef"]
    nextToken: str


class ListProvisioningTemplatesResponseTypeDef(TypedDict, total=False):
    templates: List["ProvisioningTemplateSummaryTypeDef"]
    nextToken: str


class ListRoleAliasesResponseTypeDef(TypedDict, total=False):
    roleAliases: List[str]
    nextMarker: str


class ListScheduledAuditsResponseTypeDef(TypedDict, total=False):
    scheduledAudits: List["ScheduledAuditMetadataTypeDef"]
    nextToken: str


class ListSecurityProfilesForTargetResponseTypeDef(TypedDict, total=False):
    securityProfileTargetMappings: List["SecurityProfileTargetMappingTypeDef"]
    nextToken: str


class ListSecurityProfilesResponseTypeDef(TypedDict, total=False):
    securityProfileIdentifiers: List["SecurityProfileIdentifierTypeDef"]
    nextToken: str


class ListStreamsResponseTypeDef(TypedDict, total=False):
    streams: List["StreamSummaryTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: List["TagTypeDef"]
    nextToken: str


class ListTargetsForPolicyResponseTypeDef(TypedDict, total=False):
    targets: List[str]
    nextMarker: str


class ListTargetsForSecurityProfileResponseTypeDef(TypedDict, total=False):
    securityProfileTargets: List["SecurityProfileTargetTypeDef"]
    nextToken: str


class ListThingGroupsForThingResponseTypeDef(TypedDict, total=False):
    thingGroups: List["GroupNameAndArnTypeDef"]
    nextToken: str


class ListThingGroupsResponseTypeDef(TypedDict, total=False):
    thingGroups: List["GroupNameAndArnTypeDef"]
    nextToken: str


class ListThingPrincipalsResponseTypeDef(TypedDict, total=False):
    principals: List[str]
    nextToken: str


class ListThingRegistrationTaskReportsResponseTypeDef(TypedDict, total=False):
    resourceLinks: List[str]
    reportType: ReportType
    nextToken: str


class ListThingRegistrationTasksResponseTypeDef(TypedDict, total=False):
    taskIds: List[str]
    nextToken: str


class ListThingTypesResponseTypeDef(TypedDict, total=False):
    thingTypes: List["ThingTypeDefinitionTypeDef"]
    nextToken: str


class ListThingsInBillingGroupResponseTypeDef(TypedDict, total=False):
    things: List[str]
    nextToken: str


class ListThingsInThingGroupResponseTypeDef(TypedDict, total=False):
    things: List[str]
    nextToken: str


class ListThingsResponseTypeDef(TypedDict, total=False):
    things: List["ThingAttributeTypeDef"]
    nextToken: str


class ListTopicRuleDestinationsResponseTypeDef(TypedDict, total=False):
    destinationSummaries: List["TopicRuleDestinationSummaryTypeDef"]
    nextToken: str


class ListTopicRulesResponseTypeDef(TypedDict, total=False):
    rules: List["TopicRuleListItemTypeDef"]
    nextToken: str


class ListV2LoggingLevelsResponseTypeDef(TypedDict, total=False):
    logTargetConfigurations: List["LogTargetConfigurationTypeDef"]
    nextToken: str


class ListViolationEventsResponseTypeDef(TypedDict, total=False):
    violationEvents: List["ViolationEventTypeDef"]
    nextToken: str


class LogTargetConfigurationTypeDef(TypedDict, total=False):
    logTarget: "LogTargetTypeDef"
    logLevel: LogLevel


class _RequiredLogTargetTypeDef(TypedDict):
    targetType: LogTargetType


class LogTargetTypeDef(_RequiredLogTargetTypeDef, total=False):
    targetName: str


class _RequiredLoggingOptionsPayloadTypeDef(TypedDict):
    roleArn: str


class LoggingOptionsPayloadTypeDef(_RequiredLoggingOptionsPayloadTypeDef, total=False):
    logLevel: LogLevel


class MachineLearningDetectionConfigTypeDef(TypedDict):
    confidenceLevel: ConfidenceLevel


_RequiredMetricDimensionTypeDef = TypedDict(
    "_RequiredMetricDimensionTypeDef", {"dimensionName": str}
)
_OptionalMetricDimensionTypeDef = TypedDict(
    "_OptionalMetricDimensionTypeDef", {"operator": DimensionValueOperator}, total=False
)


class MetricDimensionTypeDef(_RequiredMetricDimensionTypeDef, _OptionalMetricDimensionTypeDef):
    pass


class _RequiredMetricToRetainTypeDef(TypedDict):
    metric: str


class MetricToRetainTypeDef(_RequiredMetricToRetainTypeDef, total=False):
    metricDimension: "MetricDimensionTypeDef"


class MetricValueTypeDef(TypedDict, total=False):
    count: int
    cidrs: List[str]
    ports: List[int]
    number: float
    numbers: List[float]
    strings: List[str]


class MitigationActionIdentifierTypeDef(TypedDict, total=False):
    actionName: str
    actionArn: str
    creationDate: datetime


class MitigationActionParamsTypeDef(TypedDict, total=False):
    updateDeviceCertificateParams: "UpdateDeviceCertificateParamsTypeDef"
    updateCACertificateParams: "UpdateCACertificateParamsTypeDef"
    addThingsToThingGroupParams: "AddThingsToThingGroupParamsTypeDef"
    replaceDefaultPolicyVersionParams: "ReplaceDefaultPolicyVersionParamsTypeDef"
    enableIoTLoggingParams: "EnableIoTLoggingParamsTypeDef"
    publishFindingToSnsParams: "PublishFindingToSnsParamsTypeDef"


MitigationActionTypeDef = TypedDict(
    "MitigationActionTypeDef",
    {"name": str, "id": str, "roleArn": str, "actionParams": "MitigationActionParamsTypeDef"},
    total=False,
)


class MqttContextTypeDef(TypedDict, total=False):
    username: str
    password: Union[bytes, IO[bytes]]
    clientId: str


class NonCompliantResourceTypeDef(TypedDict, total=False):
    resourceType: ResourceType
    resourceIdentifier: "ResourceIdentifierTypeDef"
    additionalInfo: Dict[str, str]


class OTAUpdateFileTypeDef(TypedDict, total=False):
    fileName: str
    fileType: int
    fileVersion: str
    fileLocation: "FileLocationTypeDef"
    codeSigning: "CodeSigningTypeDef"
    attributes: Dict[str, str]


class OTAUpdateInfoTypeDef(TypedDict, total=False):
    otaUpdateId: str
    otaUpdateArn: str
    creationDate: datetime
    lastModifiedDate: datetime
    description: str
    targets: List[str]
    protocols: List[ProtocolType]
    awsJobExecutionsRolloutConfig: "AwsJobExecutionsRolloutConfigTypeDef"
    awsJobPresignedUrlConfig: "AwsJobPresignedUrlConfigTypeDef"
    targetSelection: TargetSelection
    otaUpdateFiles: List["OTAUpdateFileTypeDef"]
    otaUpdateStatus: OTAUpdateStatus
    awsIotJobId: str
    awsIotJobArn: str
    errorInfo: "ErrorInfoTypeDef"
    additionalParameters: Dict[str, str]


class OTAUpdateSummaryTypeDef(TypedDict, total=False):
    otaUpdateId: str
    otaUpdateArn: str
    creationDate: datetime


class OutgoingCertificateTypeDef(TypedDict, total=False):
    certificateArn: str
    certificateId: str
    transferredTo: str
    transferDate: datetime
    transferMessage: str
    creationDate: datetime


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PercentPairTypeDef(TypedDict, total=False):
    percent: float
    value: float


class PolicyTypeDef(TypedDict, total=False):
    policyName: str
    policyArn: str


class PolicyVersionIdentifierTypeDef(TypedDict, total=False):
    policyName: str
    policyVersionId: str


class PolicyVersionTypeDef(TypedDict, total=False):
    versionId: str
    isDefaultVersion: bool
    createDate: datetime


class PresignedUrlConfigTypeDef(TypedDict, total=False):
    roleArn: str
    expiresInSec: int


class _RequiredProvisioningHookTypeDef(TypedDict):
    targetArn: str


class ProvisioningHookTypeDef(_RequiredProvisioningHookTypeDef, total=False):
    payloadVersion: str


class ProvisioningTemplateSummaryTypeDef(TypedDict, total=False):
    templateArn: str
    templateName: str
    description: str
    creationDate: datetime
    lastModifiedDate: datetime
    enabled: bool


class ProvisioningTemplateVersionSummaryTypeDef(TypedDict, total=False):
    versionId: int
    creationDate: datetime
    isDefaultVersion: bool


class PublishFindingToSnsParamsTypeDef(TypedDict):
    topicArn: str


class _RequiredPutAssetPropertyValueEntryTypeDef(TypedDict):
    propertyValues: List["AssetPropertyValueTypeDef"]


class PutAssetPropertyValueEntryTypeDef(_RequiredPutAssetPropertyValueEntryTypeDef, total=False):
    entryId: str
    assetId: str
    propertyId: str
    propertyAlias: str


class PutItemInputTypeDef(TypedDict):
    tableName: str


class RateIncreaseCriteriaTypeDef(TypedDict, total=False):
    numberOfNotifiedThings: int
    numberOfSucceededThings: int


class RegisterCACertificateResponseTypeDef(TypedDict, total=False):
    certificateArn: str
    certificateId: str


class RegisterCertificateResponseTypeDef(TypedDict, total=False):
    certificateArn: str
    certificateId: str


class RegisterCertificateWithoutCAResponseTypeDef(TypedDict, total=False):
    certificateArn: str
    certificateId: str


class RegisterThingResponseTypeDef(TypedDict, total=False):
    certificatePem: str
    resourceArns: Dict[str, str]


class RegistrationConfigTypeDef(TypedDict, total=False):
    templateBody: str
    roleArn: str


class RelatedResourceTypeDef(TypedDict, total=False):
    resourceType: ResourceType
    resourceIdentifier: "ResourceIdentifierTypeDef"
    additionalInfo: Dict[str, str]


class ReplaceDefaultPolicyVersionParamsTypeDef(TypedDict):
    templateName: Literal["BLANK_POLICY"]


class _RequiredRepublishActionTypeDef(TypedDict):
    roleArn: str
    topic: str


class RepublishActionTypeDef(_RequiredRepublishActionTypeDef, total=False):
    qos: int


class ResourceIdentifierTypeDef(TypedDict, total=False):
    deviceCertificateId: str
    caCertificateId: str
    cognitoIdentityPoolId: str
    clientId: str
    policyVersionIdentifier: "PolicyVersionIdentifierTypeDef"
    account: str
    iamRoleArn: str
    roleAliasArn: str


class RoleAliasDescriptionTypeDef(TypedDict, total=False):
    roleAlias: str
    roleAliasArn: str
    roleArn: str
    owner: str
    credentialDurationSeconds: int
    creationDate: datetime
    lastModifiedDate: datetime


class _RequiredS3ActionTypeDef(TypedDict):
    roleArn: str
    bucketName: str
    key: str


class S3ActionTypeDef(_RequiredS3ActionTypeDef, total=False):
    cannedAcl: CannedAccessControlList


class S3DestinationTypeDef(TypedDict, total=False):
    bucket: str
    prefix: str


class S3LocationTypeDef(TypedDict, total=False):
    bucket: str
    key: str
    version: str


class SalesforceActionTypeDef(TypedDict):
    token: str
    url: str


class ScheduledAuditMetadataTypeDef(TypedDict, total=False):
    scheduledAuditName: str
    scheduledAuditArn: str
    frequency: AuditFrequency
    dayOfMonth: str
    dayOfWeek: DayOfWeek


class SearchIndexResponseTypeDef(TypedDict, total=False):
    nextToken: str
    things: List["ThingDocumentTypeDef"]
    thingGroups: List["ThingGroupDocumentTypeDef"]


class SecurityProfileIdentifierTypeDef(TypedDict):
    name: str
    arn: str


class SecurityProfileTargetMappingTypeDef(TypedDict, total=False):
    securityProfileIdentifier: "SecurityProfileIdentifierTypeDef"
    target: "SecurityProfileTargetTypeDef"


class SecurityProfileTargetTypeDef(TypedDict):
    arn: str


class ServerCertificateSummaryTypeDef(TypedDict, total=False):
    serverCertificateArn: str
    serverCertificateStatus: ServerCertificateStatus
    serverCertificateStatusDetail: str


class SetDefaultAuthorizerResponseTypeDef(TypedDict, total=False):
    authorizerName: str
    authorizerArn: str


class SigV4AuthorizationTypeDef(TypedDict):
    signingRegion: str
    serviceName: str
    roleArn: str


class SigningProfileParameterTypeDef(TypedDict, total=False):
    certificateArn: str
    platform: str
    certificatePathOnDevice: str


class _RequiredSnsActionTypeDef(TypedDict):
    targetArn: str
    roleArn: str


class SnsActionTypeDef(_RequiredSnsActionTypeDef, total=False):
    messageFormat: MessageFormat


class _RequiredSqsActionTypeDef(TypedDict):
    roleArn: str
    queueUrl: str


class SqsActionTypeDef(_RequiredSqsActionTypeDef, total=False):
    useBase64: bool


class StartAuditMitigationActionsTaskResponseTypeDef(TypedDict, total=False):
    taskId: str


class StartDetectMitigationActionsTaskResponseTypeDef(TypedDict, total=False):
    taskId: str


class StartOnDemandAuditTaskResponseTypeDef(TypedDict, total=False):
    taskId: str


class StartSigningJobParameterTypeDef(TypedDict, total=False):
    signingProfileParameter: "SigningProfileParameterTypeDef"
    signingProfileName: str
    destination: "DestinationTypeDef"


class StartThingRegistrationTaskResponseTypeDef(TypedDict, total=False):
    taskId: str


class StatisticalThresholdTypeDef(TypedDict, total=False):
    statistic: str


StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {
        "count": int,
        "average": float,
        "sum": float,
        "minimum": float,
        "maximum": float,
        "sumOfSquares": float,
        "variance": float,
        "stdDeviation": float,
    },
    total=False,
)


class _RequiredStepFunctionsActionTypeDef(TypedDict):
    stateMachineName: str
    roleArn: str


class StepFunctionsActionTypeDef(_RequiredStepFunctionsActionTypeDef, total=False):
    executionNamePrefix: str


class StreamFileTypeDef(TypedDict, total=False):
    fileId: int
    s3Location: "S3LocationTypeDef"


class StreamInfoTypeDef(TypedDict, total=False):
    streamId: str
    streamArn: str
    streamVersion: int
    description: str
    files: List["StreamFileTypeDef"]
    createdAt: datetime
    lastUpdatedAt: datetime
    roleArn: str


class StreamSummaryTypeDef(TypedDict, total=False):
    streamId: str
    streamArn: str
    streamVersion: int
    description: str


class StreamTypeDef(TypedDict, total=False):
    streamId: str
    fileId: int


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    Value: str


class TaskStatisticsForAuditCheckTypeDef(TypedDict, total=False):
    totalFindingsCount: int
    failedFindingsCount: int
    succeededFindingsCount: int
    skippedFindingsCount: int
    canceledFindingsCount: int


class TaskStatisticsTypeDef(TypedDict, total=False):
    totalChecks: int
    inProgressChecks: int
    waitingForDataCollectionChecks: int
    compliantChecks: int
    nonCompliantChecks: int
    failedChecks: int
    canceledChecks: int


class TestAuthorizationResponseTypeDef(TypedDict, total=False):
    authResults: List["AuthResultTypeDef"]


class TestInvokeAuthorizerResponseTypeDef(TypedDict, total=False):
    isAuthenticated: bool
    principalId: str
    policyDocuments: List[str]
    refreshAfterInSeconds: int
    disconnectAfterInSeconds: int


class ThingAttributeTypeDef(TypedDict, total=False):
    thingName: str
    thingTypeName: str
    thingArn: str
    attributes: Dict[str, str]
    version: int


class ThingConnectivityTypeDef(TypedDict, total=False):
    connected: bool
    timestamp: int


class ThingDocumentTypeDef(TypedDict, total=False):
    thingName: str
    thingId: str
    thingTypeName: str
    thingGroupNames: List[str]
    attributes: Dict[str, str]
    shadow: str
    connectivity: "ThingConnectivityTypeDef"


class ThingGroupDocumentTypeDef(TypedDict, total=False):
    thingGroupName: str
    thingGroupId: str
    thingGroupDescription: str
    attributes: Dict[str, str]
    parentGroupNames: List[str]


class _RequiredThingGroupIndexingConfigurationTypeDef(TypedDict):
    thingGroupIndexingMode: ThingGroupIndexingMode


class ThingGroupIndexingConfigurationTypeDef(
    _RequiredThingGroupIndexingConfigurationTypeDef, total=False
):
    managedFields: List["FieldTypeDef"]
    customFields: List["FieldTypeDef"]


class ThingGroupMetadataTypeDef(TypedDict, total=False):
    parentGroupName: str
    rootToParentThingGroups: List["GroupNameAndArnTypeDef"]
    creationDate: datetime


class ThingGroupPropertiesTypeDef(TypedDict, total=False):
    thingGroupDescription: str
    attributePayload: "AttributePayloadTypeDef"


class _RequiredThingIndexingConfigurationTypeDef(TypedDict):
    thingIndexingMode: ThingIndexingMode


class ThingIndexingConfigurationTypeDef(_RequiredThingIndexingConfigurationTypeDef, total=False):
    thingConnectivityIndexingMode: ThingConnectivityIndexingMode
    managedFields: List["FieldTypeDef"]
    customFields: List["FieldTypeDef"]


class ThingTypeDefinitionTypeDef(TypedDict, total=False):
    thingTypeName: str
    thingTypeArn: str
    thingTypeProperties: "ThingTypePropertiesTypeDef"
    thingTypeMetadata: "ThingTypeMetadataTypeDef"


class ThingTypeMetadataTypeDef(TypedDict, total=False):
    deprecated: bool
    deprecationDate: datetime
    creationDate: datetime


class ThingTypePropertiesTypeDef(TypedDict, total=False):
    thingTypeDescription: str
    searchableAttributes: List[str]


class TimeoutConfigTypeDef(TypedDict, total=False):
    inProgressTimeoutInMinutes: int


class _RequiredTimestreamActionTypeDef(TypedDict):
    roleArn: str
    databaseName: str
    tableName: str
    dimensions: List["TimestreamDimensionTypeDef"]


class TimestreamActionTypeDef(_RequiredTimestreamActionTypeDef, total=False):
    timestamp: "TimestreamTimestampTypeDef"


class TimestreamDimensionTypeDef(TypedDict):
    name: str
    value: str


class TimestreamTimestampTypeDef(TypedDict):
    value: str
    unit: str


class TlsContextTypeDef(TypedDict, total=False):
    serverName: str


class TopicRuleDestinationConfigurationTypeDef(TypedDict, total=False):
    httpUrlConfiguration: "HttpUrlDestinationConfigurationTypeDef"
    vpcConfiguration: "VpcDestinationConfigurationTypeDef"


class TopicRuleDestinationSummaryTypeDef(TypedDict, total=False):
    arn: str
    status: TopicRuleDestinationStatus
    createdAt: datetime
    lastUpdatedAt: datetime
    statusReason: str
    httpUrlSummary: "HttpUrlDestinationSummaryTypeDef"
    vpcDestinationSummary: "VpcDestinationSummaryTypeDef"


class TopicRuleDestinationTypeDef(TypedDict, total=False):
    arn: str
    status: TopicRuleDestinationStatus
    createdAt: datetime
    lastUpdatedAt: datetime
    statusReason: str
    httpUrlProperties: "HttpUrlDestinationPropertiesTypeDef"
    vpcProperties: "VpcDestinationPropertiesTypeDef"


class TopicRuleListItemTypeDef(TypedDict, total=False):
    ruleArn: str
    ruleName: str
    topicPattern: str
    createdAt: datetime
    ruleDisabled: bool


class _RequiredTopicRulePayloadTypeDef(TypedDict):
    sql: str
    actions: List["ActionTypeDef"]


class TopicRulePayloadTypeDef(_RequiredTopicRulePayloadTypeDef, total=False):
    description: str
    ruleDisabled: bool
    awsIotSqlVersion: str
    errorAction: "ActionTypeDef"


class TopicRuleTypeDef(TypedDict, total=False):
    ruleName: str
    sql: str
    description: str
    createdAt: datetime
    actions: List["ActionTypeDef"]
    ruleDisabled: bool
    awsIotSqlVersion: str
    errorAction: "ActionTypeDef"


class TransferCertificateResponseTypeDef(TypedDict, total=False):
    transferredCertificateArn: str


class TransferDataTypeDef(TypedDict, total=False):
    transferMessage: str
    rejectReason: str
    transferDate: datetime
    acceptDate: datetime
    rejectDate: datetime


class UpdateAuthorizerResponseTypeDef(TypedDict, total=False):
    authorizerName: str
    authorizerArn: str


class UpdateBillingGroupResponseTypeDef(TypedDict, total=False):
    version: int


class UpdateCACertificateParamsTypeDef(TypedDict):
    action: Literal["DEACTIVATE"]


class UpdateCustomMetricResponseTypeDef(TypedDict, total=False):
    metricName: str
    metricArn: str
    metricType: CustomMetricType
    displayName: str
    creationDate: datetime
    lastModifiedDate: datetime


class UpdateDeviceCertificateParamsTypeDef(TypedDict):
    action: Literal["DEACTIVATE"]


UpdateDimensionResponseTypeDef = TypedDict(
    "UpdateDimensionResponseTypeDef",
    {
        "name": str,
        "arn": str,
        "type": Literal["TOPIC_FILTER"],
        "stringValues": List[str],
        "creationDate": datetime,
        "lastModifiedDate": datetime,
    },
    total=False,
)


class UpdateDomainConfigurationResponseTypeDef(TypedDict, total=False):
    domainConfigurationName: str
    domainConfigurationArn: str


class UpdateDynamicThingGroupResponseTypeDef(TypedDict, total=False):
    version: int


class UpdateMitigationActionResponseTypeDef(TypedDict, total=False):
    actionArn: str
    actionId: str


class UpdateRoleAliasResponseTypeDef(TypedDict, total=False):
    roleAlias: str
    roleAliasArn: str


class UpdateScheduledAuditResponseTypeDef(TypedDict, total=False):
    scheduledAuditArn: str


class UpdateSecurityProfileResponseTypeDef(TypedDict, total=False):
    securityProfileName: str
    securityProfileArn: str
    securityProfileDescription: str
    behaviors: List["BehaviorTypeDef"]
    alertTargets: Dict[Literal["SNS"], "AlertTargetTypeDef"]
    additionalMetricsToRetain: List[str]
    additionalMetricsToRetainV2: List["MetricToRetainTypeDef"]
    version: int
    creationDate: datetime
    lastModifiedDate: datetime


class UpdateStreamResponseTypeDef(TypedDict, total=False):
    streamId: str
    streamArn: str
    description: str
    streamVersion: int


class UpdateThingGroupResponseTypeDef(TypedDict, total=False):
    version: int


class ValidateSecurityProfileBehaviorsResponseTypeDef(TypedDict, total=False):
    valid: bool
    validationErrors: List["ValidationErrorTypeDef"]


class ValidationErrorTypeDef(TypedDict, total=False):
    errorMessage: str


class ViolationEventAdditionalInfoTypeDef(TypedDict, total=False):
    confidenceLevel: ConfidenceLevel


class ViolationEventOccurrenceRangeTypeDef(TypedDict):
    startTime: datetime
    endTime: datetime


class ViolationEventTypeDef(TypedDict, total=False):
    violationId: str
    thingName: str
    securityProfileName: str
    behavior: "BehaviorTypeDef"
    metricValue: "MetricValueTypeDef"
    violationEventAdditionalInfo: "ViolationEventAdditionalInfoTypeDef"
    violationEventType: ViolationEventType
    violationEventTime: datetime


class _RequiredVpcDestinationConfigurationTypeDef(TypedDict):
    subnetIds: List[str]
    vpcId: str
    roleArn: str


class VpcDestinationConfigurationTypeDef(_RequiredVpcDestinationConfigurationTypeDef, total=False):
    securityGroups: List[str]


class VpcDestinationPropertiesTypeDef(TypedDict, total=False):
    subnetIds: List[str]
    securityGroups: List[str]
    vpcId: str
    roleArn: str


class VpcDestinationSummaryTypeDef(TypedDict, total=False):
    subnetIds: List[str]
    securityGroups: List[str]
    vpcId: str
    roleArn: str
