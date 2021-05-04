"""
Type annotations for config service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_config/type_defs.html)

Usage::

    ```python
    from mypy_boto3_config.type_defs import AccountAggregationSourceTypeDef

    data: AccountAggregationSourceTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_config.literals import (
    AggregatedSourceStatusType,
    AggregatedSourceType,
    ComplianceType,
    ConfigRuleState,
    ConfigurationItemStatus,
    ConformancePackComplianceType,
    ConformancePackState,
    DeliveryStatus,
    MaximumExecutionFrequency,
    MemberAccountRuleStatus,
    MessageType,
    OrganizationConfigRuleTriggerType,
    OrganizationResourceDetailedStatus,
    OrganizationResourceStatus,
    OrganizationRuleStatus,
    Owner,
    RecorderStatus,
    RemediationExecutionState,
    RemediationExecutionStepState,
    ResourceType,
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
    "AccountAggregationSourceTypeDef",
    "AggregateComplianceByConfigRuleTypeDef",
    "AggregateComplianceByConformancePackTypeDef",
    "AggregateComplianceCountTypeDef",
    "AggregateConformancePackComplianceCountTypeDef",
    "AggregateConformancePackComplianceFiltersTypeDef",
    "AggregateConformancePackComplianceSummaryFiltersTypeDef",
    "AggregateConformancePackComplianceSummaryTypeDef",
    "AggregateConformancePackComplianceTypeDef",
    "AggregateEvaluationResultTypeDef",
    "AggregateResourceIdentifierTypeDef",
    "AggregatedSourceStatusTypeDef",
    "AggregationAuthorizationTypeDef",
    "BaseConfigurationItemTypeDef",
    "BatchGetAggregateResourceConfigResponseTypeDef",
    "BatchGetResourceConfigResponseTypeDef",
    "ComplianceByConfigRuleTypeDef",
    "ComplianceByResourceTypeDef",
    "ComplianceContributorCountTypeDef",
    "ComplianceSummaryByResourceTypeTypeDef",
    "ComplianceSummaryTypeDef",
    "ComplianceTypeDef",
    "ConfigExportDeliveryInfoTypeDef",
    "ConfigRuleComplianceFiltersTypeDef",
    "ConfigRuleComplianceSummaryFiltersTypeDef",
    "ConfigRuleEvaluationStatusTypeDef",
    "ConfigRuleTypeDef",
    "ConfigSnapshotDeliveryPropertiesTypeDef",
    "ConfigStreamDeliveryInfoTypeDef",
    "ConfigurationAggregatorTypeDef",
    "ConfigurationItemTypeDef",
    "ConfigurationRecorderStatusTypeDef",
    "ConfigurationRecorderTypeDef",
    "ConformancePackComplianceFiltersTypeDef",
    "ConformancePackComplianceSummaryTypeDef",
    "ConformancePackDetailTypeDef",
    "ConformancePackEvaluationFiltersTypeDef",
    "ConformancePackEvaluationResultTypeDef",
    "ConformancePackInputParameterTypeDef",
    "ConformancePackRuleComplianceTypeDef",
    "ConformancePackStatusDetailTypeDef",
    "DeleteRemediationExceptionsResponseTypeDef",
    "DeliverConfigSnapshotResponseTypeDef",
    "DeliveryChannelStatusTypeDef",
    "DeliveryChannelTypeDef",
    "DescribeAggregateComplianceByConfigRulesResponseTypeDef",
    "DescribeAggregateComplianceByConformancePacksResponseTypeDef",
    "DescribeAggregationAuthorizationsResponseTypeDef",
    "DescribeComplianceByConfigRuleResponseTypeDef",
    "DescribeComplianceByResourceResponseTypeDef",
    "DescribeConfigRuleEvaluationStatusResponseTypeDef",
    "DescribeConfigRulesResponseTypeDef",
    "DescribeConfigurationAggregatorSourcesStatusResponseTypeDef",
    "DescribeConfigurationAggregatorsResponseTypeDef",
    "DescribeConfigurationRecorderStatusResponseTypeDef",
    "DescribeConfigurationRecordersResponseTypeDef",
    "DescribeConformancePackComplianceResponseTypeDef",
    "DescribeConformancePackStatusResponseTypeDef",
    "DescribeConformancePacksResponseTypeDef",
    "DescribeDeliveryChannelStatusResponseTypeDef",
    "DescribeDeliveryChannelsResponseTypeDef",
    "DescribeOrganizationConfigRuleStatusesResponseTypeDef",
    "DescribeOrganizationConfigRulesResponseTypeDef",
    "DescribeOrganizationConformancePackStatusesResponseTypeDef",
    "DescribeOrganizationConformancePacksResponseTypeDef",
    "DescribePendingAggregationRequestsResponseTypeDef",
    "DescribeRemediationConfigurationsResponseTypeDef",
    "DescribeRemediationExceptionsResponseTypeDef",
    "DescribeRemediationExecutionStatusResponseTypeDef",
    "DescribeRetentionConfigurationsResponseTypeDef",
    "EvaluationResultIdentifierTypeDef",
    "EvaluationResultQualifierTypeDef",
    "EvaluationResultTypeDef",
    "EvaluationTypeDef",
    "ExecutionControlsTypeDef",
    "ExternalEvaluationTypeDef",
    "FailedDeleteRemediationExceptionsBatchTypeDef",
    "FailedRemediationBatchTypeDef",
    "FailedRemediationExceptionBatchTypeDef",
    "FieldInfoTypeDef",
    "GetAggregateComplianceDetailsByConfigRuleResponseTypeDef",
    "GetAggregateConfigRuleComplianceSummaryResponseTypeDef",
    "GetAggregateConformancePackComplianceSummaryResponseTypeDef",
    "GetAggregateDiscoveredResourceCountsResponseTypeDef",
    "GetAggregateResourceConfigResponseTypeDef",
    "GetComplianceDetailsByConfigRuleResponseTypeDef",
    "GetComplianceDetailsByResourceResponseTypeDef",
    "GetComplianceSummaryByConfigRuleResponseTypeDef",
    "GetComplianceSummaryByResourceTypeResponseTypeDef",
    "GetConformancePackComplianceDetailsResponseTypeDef",
    "GetConformancePackComplianceSummaryResponseTypeDef",
    "GetDiscoveredResourceCountsResponseTypeDef",
    "GetOrganizationConfigRuleDetailedStatusResponseTypeDef",
    "GetOrganizationConformancePackDetailedStatusResponseTypeDef",
    "GetResourceConfigHistoryResponseTypeDef",
    "GetStoredQueryResponseTypeDef",
    "GroupedResourceCountTypeDef",
    "ListAggregateDiscoveredResourcesResponseTypeDef",
    "ListDiscoveredResourcesResponseTypeDef",
    "ListStoredQueriesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MemberAccountStatusTypeDef",
    "OrganizationAggregationSourceTypeDef",
    "OrganizationConfigRuleStatusTypeDef",
    "OrganizationConfigRuleTypeDef",
    "OrganizationConformancePackDetailedStatusTypeDef",
    "OrganizationConformancePackStatusTypeDef",
    "OrganizationConformancePackTypeDef",
    "OrganizationCustomRuleMetadataTypeDef",
    "OrganizationManagedRuleMetadataTypeDef",
    "OrganizationResourceDetailedStatusFiltersTypeDef",
    "PaginatorConfigTypeDef",
    "PendingAggregationRequestTypeDef",
    "PutAggregationAuthorizationResponseTypeDef",
    "PutConfigurationAggregatorResponseTypeDef",
    "PutConformancePackResponseTypeDef",
    "PutEvaluationsResponseTypeDef",
    "PutOrganizationConfigRuleResponseTypeDef",
    "PutOrganizationConformancePackResponseTypeDef",
    "PutRemediationConfigurationsResponseTypeDef",
    "PutRemediationExceptionsResponseTypeDef",
    "PutRetentionConfigurationResponseTypeDef",
    "PutStoredQueryResponseTypeDef",
    "QueryInfoTypeDef",
    "RecordingGroupTypeDef",
    "RelationshipTypeDef",
    "RemediationConfigurationTypeDef",
    "RemediationExceptionResourceKeyTypeDef",
    "RemediationExceptionTypeDef",
    "RemediationExecutionStatusTypeDef",
    "RemediationExecutionStepTypeDef",
    "RemediationParameterValueTypeDef",
    "ResourceCountFiltersTypeDef",
    "ResourceCountTypeDef",
    "ResourceFiltersTypeDef",
    "ResourceIdentifierTypeDef",
    "ResourceKeyTypeDef",
    "ResourceValueTypeDef",
    "RetentionConfigurationTypeDef",
    "ScopeTypeDef",
    "SelectAggregateResourceConfigResponseTypeDef",
    "SelectResourceConfigResponseTypeDef",
    "SourceDetailTypeDef",
    "SourceTypeDef",
    "SsmControlsTypeDef",
    "StartRemediationExecutionResponseTypeDef",
    "StaticValueTypeDef",
    "StatusDetailFiltersTypeDef",
    "StoredQueryMetadataTypeDef",
    "StoredQueryTypeDef",
    "TagTypeDef",
)


class _RequiredAccountAggregationSourceTypeDef(TypedDict):
    AccountIds: List[str]


class AccountAggregationSourceTypeDef(_RequiredAccountAggregationSourceTypeDef, total=False):
    AllAwsRegions: bool
    AwsRegions: List[str]


class AggregateComplianceByConfigRuleTypeDef(TypedDict, total=False):
    ConfigRuleName: str
    Compliance: "ComplianceTypeDef"
    AccountId: str
    AwsRegion: str


class AggregateComplianceByConformancePackTypeDef(TypedDict, total=False):
    ConformancePackName: str
    Compliance: "AggregateConformancePackComplianceTypeDef"
    AccountId: str
    AwsRegion: str


class AggregateComplianceCountTypeDef(TypedDict, total=False):
    GroupName: str
    ComplianceSummary: "ComplianceSummaryTypeDef"


class AggregateConformancePackComplianceCountTypeDef(TypedDict, total=False):
    CompliantConformancePackCount: int
    NonCompliantConformancePackCount: int


class AggregateConformancePackComplianceFiltersTypeDef(TypedDict, total=False):
    ConformancePackName: str
    ComplianceType: ConformancePackComplianceType
    AccountId: str
    AwsRegion: str


class AggregateConformancePackComplianceSummaryFiltersTypeDef(TypedDict, total=False):
    AccountId: str
    AwsRegion: str


class AggregateConformancePackComplianceSummaryTypeDef(TypedDict, total=False):
    ComplianceSummary: "AggregateConformancePackComplianceCountTypeDef"
    GroupName: str


class AggregateConformancePackComplianceTypeDef(TypedDict, total=False):
    ComplianceType: ConformancePackComplianceType
    CompliantRuleCount: int
    NonCompliantRuleCount: int
    TotalRuleCount: int


class AggregateEvaluationResultTypeDef(TypedDict, total=False):
    EvaluationResultIdentifier: "EvaluationResultIdentifierTypeDef"
    ComplianceType: ComplianceType
    ResultRecordedTime: datetime
    ConfigRuleInvokedTime: datetime
    Annotation: str
    AccountId: str
    AwsRegion: str


class _RequiredAggregateResourceIdentifierTypeDef(TypedDict):
    SourceAccountId: str
    SourceRegion: str
    ResourceId: str
    ResourceType: ResourceType


class AggregateResourceIdentifierTypeDef(_RequiredAggregateResourceIdentifierTypeDef, total=False):
    ResourceName: str


class AggregatedSourceStatusTypeDef(TypedDict, total=False):
    SourceId: str
    SourceType: AggregatedSourceType
    AwsRegion: str
    LastUpdateStatus: AggregatedSourceStatusType
    LastUpdateTime: datetime
    LastErrorCode: str
    LastErrorMessage: str


class AggregationAuthorizationTypeDef(TypedDict, total=False):
    AggregationAuthorizationArn: str
    AuthorizedAccountId: str
    AuthorizedAwsRegion: str
    CreationTime: datetime


class BaseConfigurationItemTypeDef(TypedDict, total=False):
    version: str
    accountId: str
    configurationItemCaptureTime: datetime
    configurationItemStatus: ConfigurationItemStatus
    configurationStateId: str
    arn: str
    resourceType: ResourceType
    resourceId: str
    resourceName: str
    awsRegion: str
    availabilityZone: str
    resourceCreationTime: datetime
    configuration: str
    supplementaryConfiguration: Dict[str, str]


class BatchGetAggregateResourceConfigResponseTypeDef(TypedDict, total=False):
    BaseConfigurationItems: List["BaseConfigurationItemTypeDef"]
    UnprocessedResourceIdentifiers: List["AggregateResourceIdentifierTypeDef"]


class BatchGetResourceConfigResponseTypeDef(TypedDict, total=False):
    baseConfigurationItems: List["BaseConfigurationItemTypeDef"]
    unprocessedResourceKeys: List["ResourceKeyTypeDef"]


class ComplianceByConfigRuleTypeDef(TypedDict, total=False):
    ConfigRuleName: str
    Compliance: "ComplianceTypeDef"


class ComplianceByResourceTypeDef(TypedDict, total=False):
    ResourceType: str
    ResourceId: str
    Compliance: "ComplianceTypeDef"


class ComplianceContributorCountTypeDef(TypedDict, total=False):
    CappedCount: int
    CapExceeded: bool


class ComplianceSummaryByResourceTypeTypeDef(TypedDict, total=False):
    ResourceType: str
    ComplianceSummary: "ComplianceSummaryTypeDef"


class ComplianceSummaryTypeDef(TypedDict, total=False):
    CompliantResourceCount: "ComplianceContributorCountTypeDef"
    NonCompliantResourceCount: "ComplianceContributorCountTypeDef"
    ComplianceSummaryTimestamp: datetime


class ComplianceTypeDef(TypedDict, total=False):
    ComplianceType: ComplianceType
    ComplianceContributorCount: "ComplianceContributorCountTypeDef"


class ConfigExportDeliveryInfoTypeDef(TypedDict, total=False):
    lastStatus: DeliveryStatus
    lastErrorCode: str
    lastErrorMessage: str
    lastAttemptTime: datetime
    lastSuccessfulTime: datetime
    nextDeliveryTime: datetime


class ConfigRuleComplianceFiltersTypeDef(TypedDict, total=False):
    ConfigRuleName: str
    ComplianceType: ComplianceType
    AccountId: str
    AwsRegion: str


class ConfigRuleComplianceSummaryFiltersTypeDef(TypedDict, total=False):
    AccountId: str
    AwsRegion: str


class ConfigRuleEvaluationStatusTypeDef(TypedDict, total=False):
    ConfigRuleName: str
    ConfigRuleArn: str
    ConfigRuleId: str
    LastSuccessfulInvocationTime: datetime
    LastFailedInvocationTime: datetime
    LastSuccessfulEvaluationTime: datetime
    LastFailedEvaluationTime: datetime
    FirstActivatedTime: datetime
    LastDeactivatedTime: datetime
    LastErrorCode: str
    LastErrorMessage: str
    FirstEvaluationStarted: bool


class _RequiredConfigRuleTypeDef(TypedDict):
    Source: "SourceTypeDef"


class ConfigRuleTypeDef(_RequiredConfigRuleTypeDef, total=False):
    ConfigRuleName: str
    ConfigRuleArn: str
    ConfigRuleId: str
    Description: str
    Scope: "ScopeTypeDef"
    InputParameters: str
    MaximumExecutionFrequency: MaximumExecutionFrequency
    ConfigRuleState: ConfigRuleState
    CreatedBy: str


class ConfigSnapshotDeliveryPropertiesTypeDef(TypedDict, total=False):
    deliveryFrequency: MaximumExecutionFrequency


class ConfigStreamDeliveryInfoTypeDef(TypedDict, total=False):
    lastStatus: DeliveryStatus
    lastErrorCode: str
    lastErrorMessage: str
    lastStatusChangeTime: datetime


class ConfigurationAggregatorTypeDef(TypedDict, total=False):
    ConfigurationAggregatorName: str
    ConfigurationAggregatorArn: str
    AccountAggregationSources: List["AccountAggregationSourceTypeDef"]
    OrganizationAggregationSource: "OrganizationAggregationSourceTypeDef"
    CreationTime: datetime
    LastUpdatedTime: datetime
    CreatedBy: str


class ConfigurationItemTypeDef(TypedDict, total=False):
    version: str
    accountId: str
    configurationItemCaptureTime: datetime
    configurationItemStatus: ConfigurationItemStatus
    configurationStateId: str
    configurationItemMD5Hash: str
    arn: str
    resourceType: ResourceType
    resourceId: str
    resourceName: str
    awsRegion: str
    availabilityZone: str
    resourceCreationTime: datetime
    tags: Dict[str, str]
    relatedEvents: List[str]
    relationships: List["RelationshipTypeDef"]
    configuration: str
    supplementaryConfiguration: Dict[str, str]


class ConfigurationRecorderStatusTypeDef(TypedDict, total=False):
    name: str
    lastStartTime: datetime
    lastStopTime: datetime
    recording: bool
    lastStatus: RecorderStatus
    lastErrorCode: str
    lastErrorMessage: str
    lastStatusChangeTime: datetime


class ConfigurationRecorderTypeDef(TypedDict, total=False):
    name: str
    roleARN: str
    recordingGroup: "RecordingGroupTypeDef"


class ConformancePackComplianceFiltersTypeDef(TypedDict, total=False):
    ConfigRuleNames: List[str]
    ComplianceType: ConformancePackComplianceType


class ConformancePackComplianceSummaryTypeDef(TypedDict):
    ConformancePackName: str
    ConformancePackComplianceStatus: ConformancePackComplianceType


class _RequiredConformancePackDetailTypeDef(TypedDict):
    ConformancePackName: str
    ConformancePackArn: str
    ConformancePackId: str


class ConformancePackDetailTypeDef(_RequiredConformancePackDetailTypeDef, total=False):
    DeliveryS3Bucket: str
    DeliveryS3KeyPrefix: str
    ConformancePackInputParameters: List["ConformancePackInputParameterTypeDef"]
    LastUpdateRequestedTime: datetime
    CreatedBy: str


class ConformancePackEvaluationFiltersTypeDef(TypedDict, total=False):
    ConfigRuleNames: List[str]
    ComplianceType: ConformancePackComplianceType
    ResourceType: str
    ResourceIds: List[str]


class _RequiredConformancePackEvaluationResultTypeDef(TypedDict):
    ComplianceType: ConformancePackComplianceType
    EvaluationResultIdentifier: "EvaluationResultIdentifierTypeDef"
    ConfigRuleInvokedTime: datetime
    ResultRecordedTime: datetime


class ConformancePackEvaluationResultTypeDef(
    _RequiredConformancePackEvaluationResultTypeDef, total=False
):
    Annotation: str


class ConformancePackInputParameterTypeDef(TypedDict):
    ParameterName: str
    ParameterValue: str


class ConformancePackRuleComplianceTypeDef(TypedDict, total=False):
    ConfigRuleName: str
    ComplianceType: ConformancePackComplianceType
    Controls: List[str]


class _RequiredConformancePackStatusDetailTypeDef(TypedDict):
    ConformancePackName: str
    ConformancePackId: str
    ConformancePackArn: str
    ConformancePackState: ConformancePackState
    StackArn: str
    LastUpdateRequestedTime: datetime


class ConformancePackStatusDetailTypeDef(_RequiredConformancePackStatusDetailTypeDef, total=False):
    ConformancePackStatusReason: str
    LastUpdateCompletedTime: datetime


class DeleteRemediationExceptionsResponseTypeDef(TypedDict, total=False):
    FailedBatches: List["FailedDeleteRemediationExceptionsBatchTypeDef"]


class DeliverConfigSnapshotResponseTypeDef(TypedDict, total=False):
    configSnapshotId: str


class DeliveryChannelStatusTypeDef(TypedDict, total=False):
    name: str
    configSnapshotDeliveryInfo: "ConfigExportDeliveryInfoTypeDef"
    configHistoryDeliveryInfo: "ConfigExportDeliveryInfoTypeDef"
    configStreamDeliveryInfo: "ConfigStreamDeliveryInfoTypeDef"


class DeliveryChannelTypeDef(TypedDict, total=False):
    name: str
    s3BucketName: str
    s3KeyPrefix: str
    s3KmsKeyArn: str
    snsTopicARN: str
    configSnapshotDeliveryProperties: "ConfigSnapshotDeliveryPropertiesTypeDef"


class DescribeAggregateComplianceByConfigRulesResponseTypeDef(TypedDict, total=False):
    AggregateComplianceByConfigRules: List["AggregateComplianceByConfigRuleTypeDef"]
    NextToken: str


class DescribeAggregateComplianceByConformancePacksResponseTypeDef(TypedDict, total=False):
    AggregateComplianceByConformancePacks: List["AggregateComplianceByConformancePackTypeDef"]
    NextToken: str


class DescribeAggregationAuthorizationsResponseTypeDef(TypedDict, total=False):
    AggregationAuthorizations: List["AggregationAuthorizationTypeDef"]
    NextToken: str


class DescribeComplianceByConfigRuleResponseTypeDef(TypedDict, total=False):
    ComplianceByConfigRules: List["ComplianceByConfigRuleTypeDef"]
    NextToken: str


class DescribeComplianceByResourceResponseTypeDef(TypedDict, total=False):
    ComplianceByResources: List["ComplianceByResourceTypeDef"]
    NextToken: str


class DescribeConfigRuleEvaluationStatusResponseTypeDef(TypedDict, total=False):
    ConfigRulesEvaluationStatus: List["ConfigRuleEvaluationStatusTypeDef"]
    NextToken: str


class DescribeConfigRulesResponseTypeDef(TypedDict, total=False):
    ConfigRules: List["ConfigRuleTypeDef"]
    NextToken: str


class DescribeConfigurationAggregatorSourcesStatusResponseTypeDef(TypedDict, total=False):
    AggregatedSourceStatusList: List["AggregatedSourceStatusTypeDef"]
    NextToken: str


class DescribeConfigurationAggregatorsResponseTypeDef(TypedDict, total=False):
    ConfigurationAggregators: List["ConfigurationAggregatorTypeDef"]
    NextToken: str


class DescribeConfigurationRecorderStatusResponseTypeDef(TypedDict, total=False):
    ConfigurationRecordersStatus: List["ConfigurationRecorderStatusTypeDef"]


class DescribeConfigurationRecordersResponseTypeDef(TypedDict, total=False):
    ConfigurationRecorders: List["ConfigurationRecorderTypeDef"]


class _RequiredDescribeConformancePackComplianceResponseTypeDef(TypedDict):
    ConformancePackName: str
    ConformancePackRuleComplianceList: List["ConformancePackRuleComplianceTypeDef"]


class DescribeConformancePackComplianceResponseTypeDef(
    _RequiredDescribeConformancePackComplianceResponseTypeDef, total=False
):
    NextToken: str


class DescribeConformancePackStatusResponseTypeDef(TypedDict, total=False):
    ConformancePackStatusDetails: List["ConformancePackStatusDetailTypeDef"]
    NextToken: str


class DescribeConformancePacksResponseTypeDef(TypedDict, total=False):
    ConformancePackDetails: List["ConformancePackDetailTypeDef"]
    NextToken: str


class DescribeDeliveryChannelStatusResponseTypeDef(TypedDict, total=False):
    DeliveryChannelsStatus: List["DeliveryChannelStatusTypeDef"]


class DescribeDeliveryChannelsResponseTypeDef(TypedDict, total=False):
    DeliveryChannels: List["DeliveryChannelTypeDef"]


class DescribeOrganizationConfigRuleStatusesResponseTypeDef(TypedDict, total=False):
    OrganizationConfigRuleStatuses: List["OrganizationConfigRuleStatusTypeDef"]
    NextToken: str


class DescribeOrganizationConfigRulesResponseTypeDef(TypedDict, total=False):
    OrganizationConfigRules: List["OrganizationConfigRuleTypeDef"]
    NextToken: str


class DescribeOrganizationConformancePackStatusesResponseTypeDef(TypedDict, total=False):
    OrganizationConformancePackStatuses: List["OrganizationConformancePackStatusTypeDef"]
    NextToken: str


class DescribeOrganizationConformancePacksResponseTypeDef(TypedDict, total=False):
    OrganizationConformancePacks: List["OrganizationConformancePackTypeDef"]
    NextToken: str


class DescribePendingAggregationRequestsResponseTypeDef(TypedDict, total=False):
    PendingAggregationRequests: List["PendingAggregationRequestTypeDef"]
    NextToken: str


class DescribeRemediationConfigurationsResponseTypeDef(TypedDict, total=False):
    RemediationConfigurations: List["RemediationConfigurationTypeDef"]


class DescribeRemediationExceptionsResponseTypeDef(TypedDict, total=False):
    RemediationExceptions: List["RemediationExceptionTypeDef"]
    NextToken: str


class DescribeRemediationExecutionStatusResponseTypeDef(TypedDict, total=False):
    RemediationExecutionStatuses: List["RemediationExecutionStatusTypeDef"]
    NextToken: str


class DescribeRetentionConfigurationsResponseTypeDef(TypedDict, total=False):
    RetentionConfigurations: List["RetentionConfigurationTypeDef"]
    NextToken: str


class EvaluationResultIdentifierTypeDef(TypedDict, total=False):
    EvaluationResultQualifier: "EvaluationResultQualifierTypeDef"
    OrderingTimestamp: datetime


class EvaluationResultQualifierTypeDef(TypedDict, total=False):
    ConfigRuleName: str
    ResourceType: str
    ResourceId: str


class EvaluationResultTypeDef(TypedDict, total=False):
    EvaluationResultIdentifier: "EvaluationResultIdentifierTypeDef"
    ComplianceType: ComplianceType
    ResultRecordedTime: datetime
    ConfigRuleInvokedTime: datetime
    Annotation: str
    ResultToken: str


class _RequiredEvaluationTypeDef(TypedDict):
    ComplianceResourceType: str
    ComplianceResourceId: str
    ComplianceType: ComplianceType
    OrderingTimestamp: datetime


class EvaluationTypeDef(_RequiredEvaluationTypeDef, total=False):
    Annotation: str


class ExecutionControlsTypeDef(TypedDict, total=False):
    SsmControls: "SsmControlsTypeDef"


class _RequiredExternalEvaluationTypeDef(TypedDict):
    ComplianceResourceType: str
    ComplianceResourceId: str
    ComplianceType: ComplianceType
    OrderingTimestamp: datetime


class ExternalEvaluationTypeDef(_RequiredExternalEvaluationTypeDef, total=False):
    Annotation: str


class FailedDeleteRemediationExceptionsBatchTypeDef(TypedDict, total=False):
    FailureMessage: str
    FailedItems: List["RemediationExceptionResourceKeyTypeDef"]


class FailedRemediationBatchTypeDef(TypedDict, total=False):
    FailureMessage: str
    FailedItems: List["RemediationConfigurationTypeDef"]


class FailedRemediationExceptionBatchTypeDef(TypedDict, total=False):
    FailureMessage: str
    FailedItems: List["RemediationExceptionTypeDef"]


class FieldInfoTypeDef(TypedDict, total=False):
    Name: str


class GetAggregateComplianceDetailsByConfigRuleResponseTypeDef(TypedDict, total=False):
    AggregateEvaluationResults: List["AggregateEvaluationResultTypeDef"]
    NextToken: str


class GetAggregateConfigRuleComplianceSummaryResponseTypeDef(TypedDict, total=False):
    GroupByKey: str
    AggregateComplianceCounts: List["AggregateComplianceCountTypeDef"]
    NextToken: str


class GetAggregateConformancePackComplianceSummaryResponseTypeDef(TypedDict, total=False):
    AggregateConformancePackComplianceSummaries: List[
        "AggregateConformancePackComplianceSummaryTypeDef"
    ]
    GroupByKey: str
    NextToken: str


class _RequiredGetAggregateDiscoveredResourceCountsResponseTypeDef(TypedDict):
    TotalDiscoveredResources: int


class GetAggregateDiscoveredResourceCountsResponseTypeDef(
    _RequiredGetAggregateDiscoveredResourceCountsResponseTypeDef, total=False
):
    GroupByKey: str
    GroupedResourceCounts: List["GroupedResourceCountTypeDef"]
    NextToken: str


class GetAggregateResourceConfigResponseTypeDef(TypedDict, total=False):
    ConfigurationItem: "ConfigurationItemTypeDef"


class GetComplianceDetailsByConfigRuleResponseTypeDef(TypedDict, total=False):
    EvaluationResults: List["EvaluationResultTypeDef"]
    NextToken: str


class GetComplianceDetailsByResourceResponseTypeDef(TypedDict, total=False):
    EvaluationResults: List["EvaluationResultTypeDef"]
    NextToken: str


class GetComplianceSummaryByConfigRuleResponseTypeDef(TypedDict, total=False):
    ComplianceSummary: "ComplianceSummaryTypeDef"


class GetComplianceSummaryByResourceTypeResponseTypeDef(TypedDict, total=False):
    ComplianceSummariesByResourceType: List["ComplianceSummaryByResourceTypeTypeDef"]


class _RequiredGetConformancePackComplianceDetailsResponseTypeDef(TypedDict):
    ConformancePackName: str


class GetConformancePackComplianceDetailsResponseTypeDef(
    _RequiredGetConformancePackComplianceDetailsResponseTypeDef, total=False
):
    ConformancePackRuleEvaluationResults: List["ConformancePackEvaluationResultTypeDef"]
    NextToken: str


class GetConformancePackComplianceSummaryResponseTypeDef(TypedDict, total=False):
    ConformancePackComplianceSummaryList: List["ConformancePackComplianceSummaryTypeDef"]
    NextToken: str


class GetDiscoveredResourceCountsResponseTypeDef(TypedDict, total=False):
    totalDiscoveredResources: int
    resourceCounts: List["ResourceCountTypeDef"]
    nextToken: str


class GetOrganizationConfigRuleDetailedStatusResponseTypeDef(TypedDict, total=False):
    OrganizationConfigRuleDetailedStatus: List["MemberAccountStatusTypeDef"]
    NextToken: str


class GetOrganizationConformancePackDetailedStatusResponseTypeDef(TypedDict, total=False):
    OrganizationConformancePackDetailedStatuses: List[
        "OrganizationConformancePackDetailedStatusTypeDef"
    ]
    NextToken: str


class GetResourceConfigHistoryResponseTypeDef(TypedDict, total=False):
    configurationItems: List["ConfigurationItemTypeDef"]
    nextToken: str


class GetStoredQueryResponseTypeDef(TypedDict, total=False):
    StoredQuery: "StoredQueryTypeDef"


class GroupedResourceCountTypeDef(TypedDict):
    GroupName: str
    ResourceCount: int


class ListAggregateDiscoveredResourcesResponseTypeDef(TypedDict, total=False):
    ResourceIdentifiers: List["AggregateResourceIdentifierTypeDef"]
    NextToken: str


class ListDiscoveredResourcesResponseTypeDef(TypedDict, total=False):
    resourceIdentifiers: List["ResourceIdentifierTypeDef"]
    nextToken: str


class ListStoredQueriesResponseTypeDef(TypedDict, total=False):
    StoredQueryMetadata: List["StoredQueryMetadataTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]
    NextToken: str


class _RequiredMemberAccountStatusTypeDef(TypedDict):
    AccountId: str
    ConfigRuleName: str
    MemberAccountRuleStatus: MemberAccountRuleStatus


class MemberAccountStatusTypeDef(_RequiredMemberAccountStatusTypeDef, total=False):
    ErrorCode: str
    ErrorMessage: str
    LastUpdateTime: datetime


class _RequiredOrganizationAggregationSourceTypeDef(TypedDict):
    RoleArn: str


class OrganizationAggregationSourceTypeDef(
    _RequiredOrganizationAggregationSourceTypeDef, total=False
):
    AwsRegions: List[str]
    AllAwsRegions: bool


class _RequiredOrganizationConfigRuleStatusTypeDef(TypedDict):
    OrganizationConfigRuleName: str
    OrganizationRuleStatus: OrganizationRuleStatus


class OrganizationConfigRuleStatusTypeDef(
    _RequiredOrganizationConfigRuleStatusTypeDef, total=False
):
    ErrorCode: str
    ErrorMessage: str
    LastUpdateTime: datetime


class _RequiredOrganizationConfigRuleTypeDef(TypedDict):
    OrganizationConfigRuleName: str
    OrganizationConfigRuleArn: str


class OrganizationConfigRuleTypeDef(_RequiredOrganizationConfigRuleTypeDef, total=False):
    OrganizationManagedRuleMetadata: "OrganizationManagedRuleMetadataTypeDef"
    OrganizationCustomRuleMetadata: "OrganizationCustomRuleMetadataTypeDef"
    ExcludedAccounts: List[str]
    LastUpdateTime: datetime


class _RequiredOrganizationConformancePackDetailedStatusTypeDef(TypedDict):
    AccountId: str
    ConformancePackName: str
    Status: OrganizationResourceDetailedStatus


class OrganizationConformancePackDetailedStatusTypeDef(
    _RequiredOrganizationConformancePackDetailedStatusTypeDef, total=False
):
    ErrorCode: str
    ErrorMessage: str
    LastUpdateTime: datetime


class _RequiredOrganizationConformancePackStatusTypeDef(TypedDict):
    OrganizationConformancePackName: str
    Status: OrganizationResourceStatus


class OrganizationConformancePackStatusTypeDef(
    _RequiredOrganizationConformancePackStatusTypeDef, total=False
):
    ErrorCode: str
    ErrorMessage: str
    LastUpdateTime: datetime


class _RequiredOrganizationConformancePackTypeDef(TypedDict):
    OrganizationConformancePackName: str
    OrganizationConformancePackArn: str
    LastUpdateTime: datetime


class OrganizationConformancePackTypeDef(_RequiredOrganizationConformancePackTypeDef, total=False):
    DeliveryS3Bucket: str
    DeliveryS3KeyPrefix: str
    ConformancePackInputParameters: List["ConformancePackInputParameterTypeDef"]
    ExcludedAccounts: List[str]


class _RequiredOrganizationCustomRuleMetadataTypeDef(TypedDict):
    LambdaFunctionArn: str
    OrganizationConfigRuleTriggerTypes: List[OrganizationConfigRuleTriggerType]


class OrganizationCustomRuleMetadataTypeDef(
    _RequiredOrganizationCustomRuleMetadataTypeDef, total=False
):
    Description: str
    InputParameters: str
    MaximumExecutionFrequency: MaximumExecutionFrequency
    ResourceTypesScope: List[str]
    ResourceIdScope: str
    TagKeyScope: str
    TagValueScope: str


class _RequiredOrganizationManagedRuleMetadataTypeDef(TypedDict):
    RuleIdentifier: str


class OrganizationManagedRuleMetadataTypeDef(
    _RequiredOrganizationManagedRuleMetadataTypeDef, total=False
):
    Description: str
    InputParameters: str
    MaximumExecutionFrequency: MaximumExecutionFrequency
    ResourceTypesScope: List[str]
    ResourceIdScope: str
    TagKeyScope: str
    TagValueScope: str


class OrganizationResourceDetailedStatusFiltersTypeDef(TypedDict, total=False):
    AccountId: str
    Status: OrganizationResourceDetailedStatus


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PendingAggregationRequestTypeDef(TypedDict, total=False):
    RequesterAccountId: str
    RequesterAwsRegion: str


class PutAggregationAuthorizationResponseTypeDef(TypedDict, total=False):
    AggregationAuthorization: "AggregationAuthorizationTypeDef"


class PutConfigurationAggregatorResponseTypeDef(TypedDict, total=False):
    ConfigurationAggregator: "ConfigurationAggregatorTypeDef"


class PutConformancePackResponseTypeDef(TypedDict, total=False):
    ConformancePackArn: str


class PutEvaluationsResponseTypeDef(TypedDict, total=False):
    FailedEvaluations: List["EvaluationTypeDef"]


class PutOrganizationConfigRuleResponseTypeDef(TypedDict, total=False):
    OrganizationConfigRuleArn: str


class PutOrganizationConformancePackResponseTypeDef(TypedDict, total=False):
    OrganizationConformancePackArn: str


class PutRemediationConfigurationsResponseTypeDef(TypedDict, total=False):
    FailedBatches: List["FailedRemediationBatchTypeDef"]


class PutRemediationExceptionsResponseTypeDef(TypedDict, total=False):
    FailedBatches: List["FailedRemediationExceptionBatchTypeDef"]


class PutRetentionConfigurationResponseTypeDef(TypedDict, total=False):
    RetentionConfiguration: "RetentionConfigurationTypeDef"


class PutStoredQueryResponseTypeDef(TypedDict, total=False):
    QueryArn: str


class QueryInfoTypeDef(TypedDict, total=False):
    SelectFields: List["FieldInfoTypeDef"]


class RecordingGroupTypeDef(TypedDict, total=False):
    allSupported: bool
    includeGlobalResourceTypes: bool
    resourceTypes: List[ResourceType]


class RelationshipTypeDef(TypedDict, total=False):
    resourceType: ResourceType
    resourceId: str
    resourceName: str
    relationshipName: str


class _RequiredRemediationConfigurationTypeDef(TypedDict):
    ConfigRuleName: str
    TargetType: Literal["SSM_DOCUMENT"]
    TargetId: str


class RemediationConfigurationTypeDef(_RequiredRemediationConfigurationTypeDef, total=False):
    TargetVersion: str
    Parameters: Dict[str, "RemediationParameterValueTypeDef"]
    ResourceType: str
    Automatic: bool
    ExecutionControls: "ExecutionControlsTypeDef"
    MaximumAutomaticAttempts: int
    RetryAttemptSeconds: int
    Arn: str
    CreatedByService: str


class RemediationExceptionResourceKeyTypeDef(TypedDict, total=False):
    ResourceType: str
    ResourceId: str


class _RequiredRemediationExceptionTypeDef(TypedDict):
    ConfigRuleName: str
    ResourceType: str
    ResourceId: str


class RemediationExceptionTypeDef(_RequiredRemediationExceptionTypeDef, total=False):
    Message: str
    ExpirationTime: datetime


class RemediationExecutionStatusTypeDef(TypedDict, total=False):
    ResourceKey: "ResourceKeyTypeDef"
    State: RemediationExecutionState
    StepDetails: List["RemediationExecutionStepTypeDef"]
    InvocationTime: datetime
    LastUpdatedTime: datetime


class RemediationExecutionStepTypeDef(TypedDict, total=False):
    Name: str
    State: RemediationExecutionStepState
    ErrorMessage: str
    StartTime: datetime
    StopTime: datetime


class RemediationParameterValueTypeDef(TypedDict, total=False):
    ResourceValue: "ResourceValueTypeDef"
    StaticValue: "StaticValueTypeDef"


class ResourceCountFiltersTypeDef(TypedDict, total=False):
    ResourceType: ResourceType
    AccountId: str
    Region: str


class ResourceCountTypeDef(TypedDict, total=False):
    resourceType: ResourceType
    count: int


class ResourceFiltersTypeDef(TypedDict, total=False):
    AccountId: str
    ResourceId: str
    ResourceName: str
    Region: str


class ResourceIdentifierTypeDef(TypedDict, total=False):
    resourceType: ResourceType
    resourceId: str
    resourceName: str
    resourceDeletionTime: datetime


class ResourceKeyTypeDef(TypedDict):
    resourceType: ResourceType
    resourceId: str


class ResourceValueTypeDef(TypedDict):
    Value: Literal["RESOURCE_ID"]


class RetentionConfigurationTypeDef(TypedDict):
    Name: str
    RetentionPeriodInDays: int


class ScopeTypeDef(TypedDict, total=False):
    ComplianceResourceTypes: List[str]
    TagKey: str
    TagValue: str
    ComplianceResourceId: str


class SelectAggregateResourceConfigResponseTypeDef(TypedDict, total=False):
    Results: List[str]
    QueryInfo: "QueryInfoTypeDef"
    NextToken: str


class SelectResourceConfigResponseTypeDef(TypedDict, total=False):
    Results: List[str]
    QueryInfo: "QueryInfoTypeDef"
    NextToken: str


class SourceDetailTypeDef(TypedDict, total=False):
    EventSource: Literal["aws.config"]
    MessageType: MessageType
    MaximumExecutionFrequency: MaximumExecutionFrequency


class _RequiredSourceTypeDef(TypedDict):
    Owner: Owner
    SourceIdentifier: str


class SourceTypeDef(_RequiredSourceTypeDef, total=False):
    SourceDetails: List["SourceDetailTypeDef"]


class SsmControlsTypeDef(TypedDict, total=False):
    ConcurrentExecutionRatePercentage: int
    ErrorPercentage: int


class StartRemediationExecutionResponseTypeDef(TypedDict, total=False):
    FailureMessage: str
    FailedItems: List["ResourceKeyTypeDef"]


class StaticValueTypeDef(TypedDict):
    Values: List[str]


class StatusDetailFiltersTypeDef(TypedDict, total=False):
    AccountId: str
    MemberAccountRuleStatus: MemberAccountRuleStatus


class _RequiredStoredQueryMetadataTypeDef(TypedDict):
    QueryId: str
    QueryArn: str
    QueryName: str


class StoredQueryMetadataTypeDef(_RequiredStoredQueryMetadataTypeDef, total=False):
    Description: str


class _RequiredStoredQueryTypeDef(TypedDict):
    QueryName: str


class StoredQueryTypeDef(_RequiredStoredQueryTypeDef, total=False):
    QueryId: str
    QueryArn: str
    Description: str
    Expression: str


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str
