"""
Type annotations for ssm service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ssm/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ssm.type_defs import AccountSharingInfoTypeDef

    data: AccountSharingInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_ssm.literals import (
    AssociationComplianceSeverity,
    AssociationExecutionFilterKey,
    AssociationExecutionTargetsFilterKey,
    AssociationFilterKey,
    AssociationFilterOperatorType,
    AssociationStatusName,
    AssociationSyncCompliance,
    AttachmentsSourceKey,
    AutomationExecutionFilterKey,
    AutomationExecutionStatus,
    AutomationType,
    CalendarState,
    CommandFilterKey,
    CommandInvocationStatus,
    CommandPluginStatus,
    CommandStatus,
    ComplianceQueryOperatorType,
    ComplianceSeverity,
    ComplianceStatus,
    ConnectionStatus,
    DescribeActivationsFilterKeys,
    DocumentFilterKey,
    DocumentFormat,
    DocumentHashType,
    DocumentParameterType,
    DocumentReviewAction,
    DocumentStatus,
    DocumentType,
    ExecutionMode,
    Fault,
    InstanceInformationFilterKey,
    InstancePatchStateOperatorType,
    InventoryAttributeDataType,
    InventoryDeletionStatus,
    InventoryQueryOperatorType,
    LastResourceDataSyncStatus,
    MaintenanceWindowExecutionStatus,
    MaintenanceWindowResourceType,
    MaintenanceWindowTaskType,
    NotificationEvent,
    NotificationType,
    OperatingSystem,
    OpsFilterOperatorType,
    OpsItemDataType,
    OpsItemFilterKey,
    OpsItemFilterOperator,
    OpsItemStatus,
    ParametersFilterKey,
    ParameterTier,
    ParameterType,
    PatchAction,
    PatchComplianceDataState,
    PatchComplianceLevel,
    PatchDeploymentStatus,
    PatchFilterKey,
    PatchOperationType,
    PingStatus,
    PlatformType,
    RebootOption,
    ResourceType,
    ReviewStatus,
    SessionFilterKey,
    SessionStatus,
    StepExecutionFilterKey,
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
    "AccountSharingInfoTypeDef",
    "ActivationTypeDef",
    "AssociationDescriptionTypeDef",
    "AssociationExecutionFilterTypeDef",
    "AssociationExecutionTargetTypeDef",
    "AssociationExecutionTargetsFilterTypeDef",
    "AssociationExecutionTypeDef",
    "AssociationFilterTypeDef",
    "AssociationOverviewTypeDef",
    "AssociationStatusTypeDef",
    "AssociationTypeDef",
    "AssociationVersionInfoTypeDef",
    "AttachmentContentTypeDef",
    "AttachmentInformationTypeDef",
    "AttachmentsSourceTypeDef",
    "AutomationExecutionFilterTypeDef",
    "AutomationExecutionMetadataTypeDef",
    "AutomationExecutionTypeDef",
    "BaselineOverrideTypeDef",
    "CancelMaintenanceWindowExecutionResultTypeDef",
    "CloudWatchOutputConfigTypeDef",
    "CommandFilterTypeDef",
    "CommandInvocationTypeDef",
    "CommandPluginTypeDef",
    "CommandTypeDef",
    "ComplianceExecutionSummaryTypeDef",
    "ComplianceItemEntryTypeDef",
    "ComplianceItemTypeDef",
    "ComplianceStringFilterTypeDef",
    "ComplianceSummaryItemTypeDef",
    "CompliantSummaryTypeDef",
    "CreateActivationResultTypeDef",
    "CreateAssociationBatchRequestEntryTypeDef",
    "CreateAssociationBatchResultTypeDef",
    "CreateAssociationResultTypeDef",
    "CreateDocumentResultTypeDef",
    "CreateMaintenanceWindowResultTypeDef",
    "CreateOpsItemResponseTypeDef",
    "CreateOpsMetadataResultTypeDef",
    "CreatePatchBaselineResultTypeDef",
    "DeleteInventoryResultTypeDef",
    "DeleteMaintenanceWindowResultTypeDef",
    "DeleteParametersResultTypeDef",
    "DeletePatchBaselineResultTypeDef",
    "DeregisterPatchBaselineForPatchGroupResultTypeDef",
    "DeregisterTargetFromMaintenanceWindowResultTypeDef",
    "DeregisterTaskFromMaintenanceWindowResultTypeDef",
    "DescribeActivationsFilterTypeDef",
    "DescribeActivationsResultTypeDef",
    "DescribeAssociationExecutionTargetsResultTypeDef",
    "DescribeAssociationExecutionsResultTypeDef",
    "DescribeAssociationResultTypeDef",
    "DescribeAutomationExecutionsResultTypeDef",
    "DescribeAutomationStepExecutionsResultTypeDef",
    "DescribeAvailablePatchesResultTypeDef",
    "DescribeDocumentPermissionResponseTypeDef",
    "DescribeDocumentResultTypeDef",
    "DescribeEffectiveInstanceAssociationsResultTypeDef",
    "DescribeEffectivePatchesForPatchBaselineResultTypeDef",
    "DescribeInstanceAssociationsStatusResultTypeDef",
    "DescribeInstanceInformationResultTypeDef",
    "DescribeInstancePatchStatesForPatchGroupResultTypeDef",
    "DescribeInstancePatchStatesResultTypeDef",
    "DescribeInstancePatchesResultTypeDef",
    "DescribeInventoryDeletionsResultTypeDef",
    "DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef",
    "DescribeMaintenanceWindowExecutionTasksResultTypeDef",
    "DescribeMaintenanceWindowExecutionsResultTypeDef",
    "DescribeMaintenanceWindowScheduleResultTypeDef",
    "DescribeMaintenanceWindowTargetsResultTypeDef",
    "DescribeMaintenanceWindowTasksResultTypeDef",
    "DescribeMaintenanceWindowsForTargetResultTypeDef",
    "DescribeMaintenanceWindowsResultTypeDef",
    "DescribeOpsItemsResponseTypeDef",
    "DescribeParametersResultTypeDef",
    "DescribePatchBaselinesResultTypeDef",
    "DescribePatchGroupStateResultTypeDef",
    "DescribePatchGroupsResultTypeDef",
    "DescribePatchPropertiesResultTypeDef",
    "DescribeSessionsResponseTypeDef",
    "DocumentDefaultVersionDescriptionTypeDef",
    "DocumentDescriptionTypeDef",
    "DocumentFilterTypeDef",
    "DocumentIdentifierTypeDef",
    "DocumentKeyValuesFilterTypeDef",
    "DocumentMetadataResponseInfoTypeDef",
    "DocumentParameterTypeDef",
    "DocumentRequiresTypeDef",
    "DocumentReviewCommentSourceTypeDef",
    "DocumentReviewerResponseSourceTypeDef",
    "DocumentReviewsTypeDef",
    "DocumentVersionInfoTypeDef",
    "EffectivePatchTypeDef",
    "FailedCreateAssociationTypeDef",
    "FailureDetailsTypeDef",
    "GetAutomationExecutionResultTypeDef",
    "GetCalendarStateResponseTypeDef",
    "GetCommandInvocationResultTypeDef",
    "GetConnectionStatusResponseTypeDef",
    "GetDefaultPatchBaselineResultTypeDef",
    "GetDeployablePatchSnapshotForInstanceResultTypeDef",
    "GetDocumentResultTypeDef",
    "GetInventoryResultTypeDef",
    "GetInventorySchemaResultTypeDef",
    "GetMaintenanceWindowExecutionResultTypeDef",
    "GetMaintenanceWindowExecutionTaskInvocationResultTypeDef",
    "GetMaintenanceWindowExecutionTaskResultTypeDef",
    "GetMaintenanceWindowResultTypeDef",
    "GetMaintenanceWindowTaskResultTypeDef",
    "GetOpsItemResponseTypeDef",
    "GetOpsMetadataResultTypeDef",
    "GetOpsSummaryResultTypeDef",
    "GetParameterHistoryResultTypeDef",
    "GetParameterResultTypeDef",
    "GetParametersByPathResultTypeDef",
    "GetParametersResultTypeDef",
    "GetPatchBaselineForPatchGroupResultTypeDef",
    "GetPatchBaselineResultTypeDef",
    "GetServiceSettingResultTypeDef",
    "InstanceAggregatedAssociationOverviewTypeDef",
    "InstanceAssociationOutputLocationTypeDef",
    "InstanceAssociationOutputUrlTypeDef",
    "InstanceAssociationStatusInfoTypeDef",
    "InstanceAssociationTypeDef",
    "InstanceInformationFilterTypeDef",
    "InstanceInformationStringFilterTypeDef",
    "InstanceInformationTypeDef",
    "InstancePatchStateFilterTypeDef",
    "InstancePatchStateTypeDef",
    "InventoryAggregatorTypeDef",
    "InventoryDeletionStatusItemTypeDef",
    "InventoryDeletionSummaryItemTypeDef",
    "InventoryDeletionSummaryTypeDef",
    "InventoryFilterTypeDef",
    "InventoryGroupTypeDef",
    "InventoryItemAttributeTypeDef",
    "InventoryItemSchemaTypeDef",
    "InventoryItemTypeDef",
    "InventoryResultEntityTypeDef",
    "InventoryResultItemTypeDef",
    "LabelParameterVersionResultTypeDef",
    "ListAssociationVersionsResultTypeDef",
    "ListAssociationsResultTypeDef",
    "ListCommandInvocationsResultTypeDef",
    "ListCommandsResultTypeDef",
    "ListComplianceItemsResultTypeDef",
    "ListComplianceSummariesResultTypeDef",
    "ListDocumentMetadataHistoryResponseTypeDef",
    "ListDocumentVersionsResultTypeDef",
    "ListDocumentsResultTypeDef",
    "ListInventoryEntriesResultTypeDef",
    "ListOpsItemEventsResponseTypeDef",
    "ListOpsMetadataResultTypeDef",
    "ListResourceComplianceSummariesResultTypeDef",
    "ListResourceDataSyncResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "LoggingInfoTypeDef",
    "MaintenanceWindowAutomationParametersTypeDef",
    "MaintenanceWindowExecutionTaskIdentityTypeDef",
    "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef",
    "MaintenanceWindowExecutionTypeDef",
    "MaintenanceWindowFilterTypeDef",
    "MaintenanceWindowIdentityForTargetTypeDef",
    "MaintenanceWindowIdentityTypeDef",
    "MaintenanceWindowLambdaParametersTypeDef",
    "MaintenanceWindowRunCommandParametersTypeDef",
    "MaintenanceWindowStepFunctionsParametersTypeDef",
    "MaintenanceWindowTargetTypeDef",
    "MaintenanceWindowTaskInvocationParametersTypeDef",
    "MaintenanceWindowTaskParameterValueExpressionTypeDef",
    "MaintenanceWindowTaskTypeDef",
    "MetadataValueTypeDef",
    "NonCompliantSummaryTypeDef",
    "NotificationConfigTypeDef",
    "OpsAggregatorTypeDef",
    "OpsEntityItemTypeDef",
    "OpsEntityTypeDef",
    "OpsFilterTypeDef",
    "OpsItemDataValueTypeDef",
    "OpsItemEventFilterTypeDef",
    "OpsItemEventSummaryTypeDef",
    "OpsItemFilterTypeDef",
    "OpsItemIdentityTypeDef",
    "OpsItemNotificationTypeDef",
    "OpsItemSummaryTypeDef",
    "OpsItemTypeDef",
    "OpsMetadataFilterTypeDef",
    "OpsMetadataTypeDef",
    "OpsResultAttributeTypeDef",
    "OutputSourceTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterHistoryTypeDef",
    "ParameterInlinePolicyTypeDef",
    "ParameterMetadataTypeDef",
    "ParameterStringFilterTypeDef",
    "ParameterTypeDef",
    "ParametersFilterTypeDef",
    "PatchBaselineIdentityTypeDef",
    "PatchComplianceDataTypeDef",
    "PatchFilterGroupTypeDef",
    "PatchFilterTypeDef",
    "PatchGroupPatchBaselineMappingTypeDef",
    "PatchOrchestratorFilterTypeDef",
    "PatchRuleGroupTypeDef",
    "PatchRuleTypeDef",
    "PatchSourceTypeDef",
    "PatchStatusTypeDef",
    "PatchTypeDef",
    "ProgressCountersTypeDef",
    "PutInventoryResultTypeDef",
    "PutParameterResultTypeDef",
    "RegisterDefaultPatchBaselineResultTypeDef",
    "RegisterPatchBaselineForPatchGroupResultTypeDef",
    "RegisterTargetWithMaintenanceWindowResultTypeDef",
    "RegisterTaskWithMaintenanceWindowResultTypeDef",
    "RelatedOpsItemTypeDef",
    "ResetServiceSettingResultTypeDef",
    "ResolvedTargetsTypeDef",
    "ResourceComplianceSummaryItemTypeDef",
    "ResourceDataSyncAwsOrganizationsSourceTypeDef",
    "ResourceDataSyncDestinationDataSharingTypeDef",
    "ResourceDataSyncItemTypeDef",
    "ResourceDataSyncOrganizationalUnitTypeDef",
    "ResourceDataSyncS3DestinationTypeDef",
    "ResourceDataSyncSourceTypeDef",
    "ResourceDataSyncSourceWithStateTypeDef",
    "ResultAttributeTypeDef",
    "ResumeSessionResponseTypeDef",
    "ReviewInformationTypeDef",
    "RunbookTypeDef",
    "S3OutputLocationTypeDef",
    "S3OutputUrlTypeDef",
    "ScheduledWindowExecutionTypeDef",
    "SendCommandResultTypeDef",
    "ServiceSettingTypeDef",
    "SessionFilterTypeDef",
    "SessionManagerOutputUrlTypeDef",
    "SessionTypeDef",
    "SeveritySummaryTypeDef",
    "StartAutomationExecutionResultTypeDef",
    "StartChangeRequestExecutionResultTypeDef",
    "StartSessionResponseTypeDef",
    "StepExecutionFilterTypeDef",
    "StepExecutionTypeDef",
    "TagTypeDef",
    "TargetLocationTypeDef",
    "TargetTypeDef",
    "TerminateSessionResponseTypeDef",
    "UnlabelParameterVersionResultTypeDef",
    "UpdateAssociationResultTypeDef",
    "UpdateAssociationStatusResultTypeDef",
    "UpdateDocumentDefaultVersionResultTypeDef",
    "UpdateDocumentResultTypeDef",
    "UpdateMaintenanceWindowResultTypeDef",
    "UpdateMaintenanceWindowTargetResultTypeDef",
    "UpdateMaintenanceWindowTaskResultTypeDef",
    "UpdateOpsMetadataResultTypeDef",
    "UpdatePatchBaselineResultTypeDef",
    "WaiterConfigTypeDef",
)


class AccountSharingInfoTypeDef(TypedDict, total=False):
    AccountId: str
    SharedDocumentVersion: str


class ActivationTypeDef(TypedDict, total=False):
    ActivationId: str
    Description: str
    DefaultInstanceName: str
    IamRole: str
    RegistrationLimit: int
    RegistrationsCount: int
    ExpirationDate: datetime
    Expired: bool
    CreatedDate: datetime
    Tags: List["TagTypeDef"]


class AssociationDescriptionTypeDef(TypedDict, total=False):
    Name: str
    InstanceId: str
    AssociationVersion: str
    Date: datetime
    LastUpdateAssociationDate: datetime
    Status: "AssociationStatusTypeDef"
    Overview: "AssociationOverviewTypeDef"
    DocumentVersion: str
    AutomationTargetParameterName: str
    Parameters: Dict[str, List[str]]
    AssociationId: str
    Targets: List["TargetTypeDef"]
    ScheduleExpression: str
    OutputLocation: "InstanceAssociationOutputLocationTypeDef"
    LastExecutionDate: datetime
    LastSuccessfulExecutionDate: datetime
    AssociationName: str
    MaxErrors: str
    MaxConcurrency: str
    ComplianceSeverity: AssociationComplianceSeverity
    SyncCompliance: AssociationSyncCompliance
    ApplyOnlyAtCronInterval: bool
    CalendarNames: List[str]
    TargetLocations: List["TargetLocationTypeDef"]


AssociationExecutionFilterTypeDef = TypedDict(
    "AssociationExecutionFilterTypeDef",
    {"Key": AssociationExecutionFilterKey, "Value": str, "Type": AssociationFilterOperatorType},
)


class AssociationExecutionTargetTypeDef(TypedDict, total=False):
    AssociationId: str
    AssociationVersion: str
    ExecutionId: str
    ResourceId: str
    ResourceType: str
    Status: str
    DetailedStatus: str
    LastExecutionDate: datetime
    OutputSource: "OutputSourceTypeDef"


class AssociationExecutionTargetsFilterTypeDef(TypedDict):
    Key: AssociationExecutionTargetsFilterKey
    Value: str


class AssociationExecutionTypeDef(TypedDict, total=False):
    AssociationId: str
    AssociationVersion: str
    ExecutionId: str
    Status: str
    DetailedStatus: str
    CreatedTime: datetime
    LastExecutionDate: datetime
    ResourceCountByStatus: str


class AssociationFilterTypeDef(TypedDict):
    key: AssociationFilterKey
    value: str


class AssociationOverviewTypeDef(TypedDict, total=False):
    Status: str
    DetailedStatus: str
    AssociationStatusAggregatedCount: Dict[str, int]


class _RequiredAssociationStatusTypeDef(TypedDict):
    Date: datetime
    Name: AssociationStatusName
    Message: str


class AssociationStatusTypeDef(_RequiredAssociationStatusTypeDef, total=False):
    AdditionalInfo: str


class AssociationTypeDef(TypedDict, total=False):
    Name: str
    InstanceId: str
    AssociationId: str
    AssociationVersion: str
    DocumentVersion: str
    Targets: List["TargetTypeDef"]
    LastExecutionDate: datetime
    Overview: "AssociationOverviewTypeDef"
    ScheduleExpression: str
    AssociationName: str


class AssociationVersionInfoTypeDef(TypedDict, total=False):
    AssociationId: str
    AssociationVersion: str
    CreatedDate: datetime
    Name: str
    DocumentVersion: str
    Parameters: Dict[str, List[str]]
    Targets: List["TargetTypeDef"]
    ScheduleExpression: str
    OutputLocation: "InstanceAssociationOutputLocationTypeDef"
    AssociationName: str
    MaxErrors: str
    MaxConcurrency: str
    ComplianceSeverity: AssociationComplianceSeverity
    SyncCompliance: AssociationSyncCompliance
    ApplyOnlyAtCronInterval: bool
    CalendarNames: List[str]
    TargetLocations: List["TargetLocationTypeDef"]


class AttachmentContentTypeDef(TypedDict, total=False):
    Name: str
    Size: int
    Hash: str
    HashType: Literal["Sha256"]
    Url: str


class AttachmentInformationTypeDef(TypedDict, total=False):
    Name: str


class AttachmentsSourceTypeDef(TypedDict, total=False):
    Key: AttachmentsSourceKey
    Values: List[str]
    Name: str


class AutomationExecutionFilterTypeDef(TypedDict):
    Key: AutomationExecutionFilterKey
    Values: List[str]


class AutomationExecutionMetadataTypeDef(TypedDict, total=False):
    AutomationExecutionId: str
    DocumentName: str
    DocumentVersion: str
    AutomationExecutionStatus: AutomationExecutionStatus
    ExecutionStartTime: datetime
    ExecutionEndTime: datetime
    ExecutedBy: str
    LogFile: str
    Outputs: Dict[str, List[str]]
    Mode: ExecutionMode
    ParentAutomationExecutionId: str
    CurrentStepName: str
    CurrentAction: str
    FailureMessage: str
    TargetParameterName: str
    Targets: List["TargetTypeDef"]
    TargetMaps: List[Dict[str, List[str]]]
    ResolvedTargets: "ResolvedTargetsTypeDef"
    MaxConcurrency: str
    MaxErrors: str
    Target: str
    AutomationType: AutomationType
    AutomationSubtype: Literal["ChangeRequest"]
    ScheduledTime: datetime
    Runbooks: List["RunbookTypeDef"]
    OpsItemId: str
    AssociationId: str
    ChangeRequestName: str


class AutomationExecutionTypeDef(TypedDict, total=False):
    AutomationExecutionId: str
    DocumentName: str
    DocumentVersion: str
    ExecutionStartTime: datetime
    ExecutionEndTime: datetime
    AutomationExecutionStatus: AutomationExecutionStatus
    StepExecutions: List["StepExecutionTypeDef"]
    StepExecutionsTruncated: bool
    Parameters: Dict[str, List[str]]
    Outputs: Dict[str, List[str]]
    FailureMessage: str
    Mode: ExecutionMode
    ParentAutomationExecutionId: str
    ExecutedBy: str
    CurrentStepName: str
    CurrentAction: str
    TargetParameterName: str
    Targets: List["TargetTypeDef"]
    TargetMaps: List[Dict[str, List[str]]]
    ResolvedTargets: "ResolvedTargetsTypeDef"
    MaxConcurrency: str
    MaxErrors: str
    Target: str
    TargetLocations: List["TargetLocationTypeDef"]
    ProgressCounters: "ProgressCountersTypeDef"
    AutomationSubtype: Literal["ChangeRequest"]
    ScheduledTime: datetime
    Runbooks: List["RunbookTypeDef"]
    OpsItemId: str
    AssociationId: str
    ChangeRequestName: str


class BaselineOverrideTypeDef(TypedDict, total=False):
    OperatingSystem: OperatingSystem
    GlobalFilters: "PatchFilterGroupTypeDef"
    ApprovalRules: "PatchRuleGroupTypeDef"
    ApprovedPatches: List[str]
    ApprovedPatchesComplianceLevel: PatchComplianceLevel
    RejectedPatches: List[str]
    RejectedPatchesAction: PatchAction
    ApprovedPatchesEnableNonSecurity: bool
    Sources: List["PatchSourceTypeDef"]


class CancelMaintenanceWindowExecutionResultTypeDef(TypedDict, total=False):
    WindowExecutionId: str


class CloudWatchOutputConfigTypeDef(TypedDict, total=False):
    CloudWatchLogGroupName: str
    CloudWatchOutputEnabled: bool


class CommandFilterTypeDef(TypedDict):
    key: CommandFilterKey
    value: str


class CommandInvocationTypeDef(TypedDict, total=False):
    CommandId: str
    InstanceId: str
    InstanceName: str
    Comment: str
    DocumentName: str
    DocumentVersion: str
    RequestedDateTime: datetime
    Status: CommandInvocationStatus
    StatusDetails: str
    TraceOutput: str
    StandardOutputUrl: str
    StandardErrorUrl: str
    CommandPlugins: List["CommandPluginTypeDef"]
    ServiceRole: str
    NotificationConfig: "NotificationConfigTypeDef"
    CloudWatchOutputConfig: "CloudWatchOutputConfigTypeDef"


class CommandPluginTypeDef(TypedDict, total=False):
    Name: str
    Status: CommandPluginStatus
    StatusDetails: str
    ResponseCode: int
    ResponseStartDateTime: datetime
    ResponseFinishDateTime: datetime
    Output: str
    StandardOutputUrl: str
    StandardErrorUrl: str
    OutputS3Region: str
    OutputS3BucketName: str
    OutputS3KeyPrefix: str


class CommandTypeDef(TypedDict, total=False):
    CommandId: str
    DocumentName: str
    DocumentVersion: str
    Comment: str
    ExpiresAfter: datetime
    Parameters: Dict[str, List[str]]
    InstanceIds: List[str]
    Targets: List["TargetTypeDef"]
    RequestedDateTime: datetime
    Status: CommandStatus
    StatusDetails: str
    OutputS3Region: str
    OutputS3BucketName: str
    OutputS3KeyPrefix: str
    MaxConcurrency: str
    MaxErrors: str
    TargetCount: int
    CompletedCount: int
    ErrorCount: int
    DeliveryTimedOutCount: int
    ServiceRole: str
    NotificationConfig: "NotificationConfigTypeDef"
    CloudWatchOutputConfig: "CloudWatchOutputConfigTypeDef"
    TimeoutSeconds: int


class _RequiredComplianceExecutionSummaryTypeDef(TypedDict):
    ExecutionTime: datetime


class ComplianceExecutionSummaryTypeDef(_RequiredComplianceExecutionSummaryTypeDef, total=False):
    ExecutionId: str
    ExecutionType: str


class _RequiredComplianceItemEntryTypeDef(TypedDict):
    Severity: ComplianceSeverity
    Status: ComplianceStatus


class ComplianceItemEntryTypeDef(_RequiredComplianceItemEntryTypeDef, total=False):
    Id: str
    Title: str
    Details: Dict[str, str]


class ComplianceItemTypeDef(TypedDict, total=False):
    ComplianceType: str
    ResourceType: str
    ResourceId: str
    Id: str
    Title: str
    Status: ComplianceStatus
    Severity: ComplianceSeverity
    ExecutionSummary: "ComplianceExecutionSummaryTypeDef"
    Details: Dict[str, str]


ComplianceStringFilterTypeDef = TypedDict(
    "ComplianceStringFilterTypeDef",
    {"Key": str, "Values": List[str], "Type": ComplianceQueryOperatorType},
    total=False,
)


class ComplianceSummaryItemTypeDef(TypedDict, total=False):
    ComplianceType: str
    CompliantSummary: "CompliantSummaryTypeDef"
    NonCompliantSummary: "NonCompliantSummaryTypeDef"


class CompliantSummaryTypeDef(TypedDict, total=False):
    CompliantCount: int
    SeveritySummary: "SeveritySummaryTypeDef"


class CreateActivationResultTypeDef(TypedDict, total=False):
    ActivationId: str
    ActivationCode: str


class _RequiredCreateAssociationBatchRequestEntryTypeDef(TypedDict):
    Name: str


class CreateAssociationBatchRequestEntryTypeDef(
    _RequiredCreateAssociationBatchRequestEntryTypeDef, total=False
):
    InstanceId: str
    Parameters: Dict[str, List[str]]
    AutomationTargetParameterName: str
    DocumentVersion: str
    Targets: List["TargetTypeDef"]
    ScheduleExpression: str
    OutputLocation: "InstanceAssociationOutputLocationTypeDef"
    AssociationName: str
    MaxErrors: str
    MaxConcurrency: str
    ComplianceSeverity: AssociationComplianceSeverity
    SyncCompliance: AssociationSyncCompliance
    ApplyOnlyAtCronInterval: bool
    CalendarNames: List[str]
    TargetLocations: List["TargetLocationTypeDef"]


class CreateAssociationBatchResultTypeDef(TypedDict, total=False):
    Successful: List["AssociationDescriptionTypeDef"]
    Failed: List["FailedCreateAssociationTypeDef"]


class CreateAssociationResultTypeDef(TypedDict, total=False):
    AssociationDescription: "AssociationDescriptionTypeDef"


class CreateDocumentResultTypeDef(TypedDict, total=False):
    DocumentDescription: "DocumentDescriptionTypeDef"


class CreateMaintenanceWindowResultTypeDef(TypedDict, total=False):
    WindowId: str


class CreateOpsItemResponseTypeDef(TypedDict, total=False):
    OpsItemId: str


class CreateOpsMetadataResultTypeDef(TypedDict, total=False):
    OpsMetadataArn: str


class CreatePatchBaselineResultTypeDef(TypedDict, total=False):
    BaselineId: str


class DeleteInventoryResultTypeDef(TypedDict, total=False):
    DeletionId: str
    TypeName: str
    DeletionSummary: "InventoryDeletionSummaryTypeDef"


class DeleteMaintenanceWindowResultTypeDef(TypedDict, total=False):
    WindowId: str


class DeleteParametersResultTypeDef(TypedDict, total=False):
    DeletedParameters: List[str]
    InvalidParameters: List[str]


class DeletePatchBaselineResultTypeDef(TypedDict, total=False):
    BaselineId: str


class DeregisterPatchBaselineForPatchGroupResultTypeDef(TypedDict, total=False):
    BaselineId: str
    PatchGroup: str


class DeregisterTargetFromMaintenanceWindowResultTypeDef(TypedDict, total=False):
    WindowId: str
    WindowTargetId: str


class DeregisterTaskFromMaintenanceWindowResultTypeDef(TypedDict, total=False):
    WindowId: str
    WindowTaskId: str


class DescribeActivationsFilterTypeDef(TypedDict, total=False):
    FilterKey: DescribeActivationsFilterKeys
    FilterValues: List[str]


class DescribeActivationsResultTypeDef(TypedDict, total=False):
    ActivationList: List["ActivationTypeDef"]
    NextToken: str


class DescribeAssociationExecutionTargetsResultTypeDef(TypedDict, total=False):
    AssociationExecutionTargets: List["AssociationExecutionTargetTypeDef"]
    NextToken: str


class DescribeAssociationExecutionsResultTypeDef(TypedDict, total=False):
    AssociationExecutions: List["AssociationExecutionTypeDef"]
    NextToken: str


class DescribeAssociationResultTypeDef(TypedDict, total=False):
    AssociationDescription: "AssociationDescriptionTypeDef"


class DescribeAutomationExecutionsResultTypeDef(TypedDict, total=False):
    AutomationExecutionMetadataList: List["AutomationExecutionMetadataTypeDef"]
    NextToken: str


class DescribeAutomationStepExecutionsResultTypeDef(TypedDict, total=False):
    StepExecutions: List["StepExecutionTypeDef"]
    NextToken: str


class DescribeAvailablePatchesResultTypeDef(TypedDict, total=False):
    Patches: List["PatchTypeDef"]
    NextToken: str


class DescribeDocumentPermissionResponseTypeDef(TypedDict, total=False):
    AccountIds: List[str]
    AccountSharingInfoList: List["AccountSharingInfoTypeDef"]
    NextToken: str


class DescribeDocumentResultTypeDef(TypedDict, total=False):
    Document: "DocumentDescriptionTypeDef"


class DescribeEffectiveInstanceAssociationsResultTypeDef(TypedDict, total=False):
    Associations: List["InstanceAssociationTypeDef"]
    NextToken: str


class DescribeEffectivePatchesForPatchBaselineResultTypeDef(TypedDict, total=False):
    EffectivePatches: List["EffectivePatchTypeDef"]
    NextToken: str


class DescribeInstanceAssociationsStatusResultTypeDef(TypedDict, total=False):
    InstanceAssociationStatusInfos: List["InstanceAssociationStatusInfoTypeDef"]
    NextToken: str


class DescribeInstanceInformationResultTypeDef(TypedDict, total=False):
    InstanceInformationList: List["InstanceInformationTypeDef"]
    NextToken: str


class DescribeInstancePatchStatesForPatchGroupResultTypeDef(TypedDict, total=False):
    InstancePatchStates: List["InstancePatchStateTypeDef"]
    NextToken: str


class DescribeInstancePatchStatesResultTypeDef(TypedDict, total=False):
    InstancePatchStates: List["InstancePatchStateTypeDef"]
    NextToken: str


class DescribeInstancePatchesResultTypeDef(TypedDict, total=False):
    Patches: List["PatchComplianceDataTypeDef"]
    NextToken: str


class DescribeInventoryDeletionsResultTypeDef(TypedDict, total=False):
    InventoryDeletions: List["InventoryDeletionStatusItemTypeDef"]
    NextToken: str


class DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef(TypedDict, total=False):
    WindowExecutionTaskInvocationIdentities: List[
        "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef"
    ]
    NextToken: str


class DescribeMaintenanceWindowExecutionTasksResultTypeDef(TypedDict, total=False):
    WindowExecutionTaskIdentities: List["MaintenanceWindowExecutionTaskIdentityTypeDef"]
    NextToken: str


class DescribeMaintenanceWindowExecutionsResultTypeDef(TypedDict, total=False):
    WindowExecutions: List["MaintenanceWindowExecutionTypeDef"]
    NextToken: str


class DescribeMaintenanceWindowScheduleResultTypeDef(TypedDict, total=False):
    ScheduledWindowExecutions: List["ScheduledWindowExecutionTypeDef"]
    NextToken: str


class DescribeMaintenanceWindowTargetsResultTypeDef(TypedDict, total=False):
    Targets: List["MaintenanceWindowTargetTypeDef"]
    NextToken: str


class DescribeMaintenanceWindowTasksResultTypeDef(TypedDict, total=False):
    Tasks: List["MaintenanceWindowTaskTypeDef"]
    NextToken: str


class DescribeMaintenanceWindowsForTargetResultTypeDef(TypedDict, total=False):
    WindowIdentities: List["MaintenanceWindowIdentityForTargetTypeDef"]
    NextToken: str


class DescribeMaintenanceWindowsResultTypeDef(TypedDict, total=False):
    WindowIdentities: List["MaintenanceWindowIdentityTypeDef"]
    NextToken: str


class DescribeOpsItemsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    OpsItemSummaries: List["OpsItemSummaryTypeDef"]


class DescribeParametersResultTypeDef(TypedDict, total=False):
    Parameters: List["ParameterMetadataTypeDef"]
    NextToken: str


class DescribePatchBaselinesResultTypeDef(TypedDict, total=False):
    BaselineIdentities: List["PatchBaselineIdentityTypeDef"]
    NextToken: str


class DescribePatchGroupStateResultTypeDef(TypedDict, total=False):
    Instances: int
    InstancesWithInstalledPatches: int
    InstancesWithInstalledOtherPatches: int
    InstancesWithInstalledPendingRebootPatches: int
    InstancesWithInstalledRejectedPatches: int
    InstancesWithMissingPatches: int
    InstancesWithFailedPatches: int
    InstancesWithNotApplicablePatches: int
    InstancesWithUnreportedNotApplicablePatches: int
    InstancesWithCriticalNonCompliantPatches: int
    InstancesWithSecurityNonCompliantPatches: int
    InstancesWithOtherNonCompliantPatches: int


class DescribePatchGroupsResultTypeDef(TypedDict, total=False):
    Mappings: List["PatchGroupPatchBaselineMappingTypeDef"]
    NextToken: str


class DescribePatchPropertiesResultTypeDef(TypedDict, total=False):
    Properties: List[Dict[str, str]]
    NextToken: str


class DescribeSessionsResponseTypeDef(TypedDict, total=False):
    Sessions: List["SessionTypeDef"]
    NextToken: str


class DocumentDefaultVersionDescriptionTypeDef(TypedDict, total=False):
    Name: str
    DefaultVersion: str
    DefaultVersionName: str


class DocumentDescriptionTypeDef(TypedDict, total=False):
    Sha1: str
    Hash: str
    HashType: DocumentHashType
    Name: str
    VersionName: str
    Owner: str
    CreatedDate: datetime
    Status: DocumentStatus
    StatusInformation: str
    DocumentVersion: str
    Description: str
    Parameters: List["DocumentParameterTypeDef"]
    PlatformTypes: List[PlatformType]
    DocumentType: DocumentType
    SchemaVersion: str
    LatestVersion: str
    DefaultVersion: str
    DocumentFormat: DocumentFormat
    TargetType: str
    Tags: List["TagTypeDef"]
    AttachmentsInformation: List["AttachmentInformationTypeDef"]
    Requires: List["DocumentRequiresTypeDef"]
    Author: str
    ReviewInformation: List["ReviewInformationTypeDef"]
    ApprovedVersion: str
    PendingReviewVersion: str
    ReviewStatus: ReviewStatus


class DocumentFilterTypeDef(TypedDict):
    key: DocumentFilterKey
    value: str


class DocumentIdentifierTypeDef(TypedDict, total=False):
    Name: str
    Owner: str
    VersionName: str
    PlatformTypes: List[PlatformType]
    DocumentVersion: str
    DocumentType: DocumentType
    SchemaVersion: str
    DocumentFormat: DocumentFormat
    TargetType: str
    Tags: List["TagTypeDef"]
    Requires: List["DocumentRequiresTypeDef"]
    ReviewStatus: ReviewStatus
    Author: str


class DocumentKeyValuesFilterTypeDef(TypedDict, total=False):
    Key: str
    Values: List[str]


class DocumentMetadataResponseInfoTypeDef(TypedDict, total=False):
    ReviewerResponse: List["DocumentReviewerResponseSourceTypeDef"]


DocumentParameterTypeDef = TypedDict(
    "DocumentParameterTypeDef",
    {"Name": str, "Type": DocumentParameterType, "Description": str, "DefaultValue": str},
    total=False,
)


class _RequiredDocumentRequiresTypeDef(TypedDict):
    Name: str


class DocumentRequiresTypeDef(_RequiredDocumentRequiresTypeDef, total=False):
    Version: str


DocumentReviewCommentSourceTypeDef = TypedDict(
    "DocumentReviewCommentSourceTypeDef", {"Type": Literal["Comment"], "Content": str}, total=False
)


class DocumentReviewerResponseSourceTypeDef(TypedDict, total=False):
    CreateTime: datetime
    UpdatedTime: datetime
    ReviewStatus: ReviewStatus
    Comment: List["DocumentReviewCommentSourceTypeDef"]
    Reviewer: str


class _RequiredDocumentReviewsTypeDef(TypedDict):
    Action: DocumentReviewAction


class DocumentReviewsTypeDef(_RequiredDocumentReviewsTypeDef, total=False):
    Comment: List["DocumentReviewCommentSourceTypeDef"]


class DocumentVersionInfoTypeDef(TypedDict, total=False):
    Name: str
    DocumentVersion: str
    VersionName: str
    CreatedDate: datetime
    IsDefaultVersion: bool
    DocumentFormat: DocumentFormat
    Status: DocumentStatus
    StatusInformation: str
    ReviewStatus: ReviewStatus


class EffectivePatchTypeDef(TypedDict, total=False):
    Patch: "PatchTypeDef"
    PatchStatus: "PatchStatusTypeDef"


class FailedCreateAssociationTypeDef(TypedDict, total=False):
    Entry: "CreateAssociationBatchRequestEntryTypeDef"
    Message: str
    Fault: Fault


class FailureDetailsTypeDef(TypedDict, total=False):
    FailureStage: str
    FailureType: str
    Details: Dict[str, List[str]]


class GetAutomationExecutionResultTypeDef(TypedDict, total=False):
    AutomationExecution: "AutomationExecutionTypeDef"


class GetCalendarStateResponseTypeDef(TypedDict, total=False):
    State: CalendarState
    AtTime: str
    NextTransitionTime: str


class GetCommandInvocationResultTypeDef(TypedDict, total=False):
    CommandId: str
    InstanceId: str
    Comment: str
    DocumentName: str
    DocumentVersion: str
    PluginName: str
    ResponseCode: int
    ExecutionStartDateTime: str
    ExecutionElapsedTime: str
    ExecutionEndDateTime: str
    Status: CommandInvocationStatus
    StatusDetails: str
    StandardOutputContent: str
    StandardOutputUrl: str
    StandardErrorContent: str
    StandardErrorUrl: str
    CloudWatchOutputConfig: "CloudWatchOutputConfigTypeDef"


class GetConnectionStatusResponseTypeDef(TypedDict, total=False):
    Target: str
    Status: ConnectionStatus


class GetDefaultPatchBaselineResultTypeDef(TypedDict, total=False):
    BaselineId: str
    OperatingSystem: OperatingSystem


class GetDeployablePatchSnapshotForInstanceResultTypeDef(TypedDict, total=False):
    InstanceId: str
    SnapshotId: str
    SnapshotDownloadUrl: str
    Product: str


class GetDocumentResultTypeDef(TypedDict, total=False):
    Name: str
    VersionName: str
    DocumentVersion: str
    Status: DocumentStatus
    StatusInformation: str
    Content: str
    DocumentType: DocumentType
    DocumentFormat: DocumentFormat
    Requires: List["DocumentRequiresTypeDef"]
    AttachmentsContent: List["AttachmentContentTypeDef"]
    ReviewStatus: ReviewStatus


class GetInventoryResultTypeDef(TypedDict, total=False):
    Entities: List["InventoryResultEntityTypeDef"]
    NextToken: str


class GetInventorySchemaResultTypeDef(TypedDict, total=False):
    Schemas: List["InventoryItemSchemaTypeDef"]
    NextToken: str


class GetMaintenanceWindowExecutionResultTypeDef(TypedDict, total=False):
    WindowExecutionId: str
    TaskIds: List[str]
    Status: MaintenanceWindowExecutionStatus
    StatusDetails: str
    StartTime: datetime
    EndTime: datetime


class GetMaintenanceWindowExecutionTaskInvocationResultTypeDef(TypedDict, total=False):
    WindowExecutionId: str
    TaskExecutionId: str
    InvocationId: str
    ExecutionId: str
    TaskType: MaintenanceWindowTaskType
    Parameters: str
    Status: MaintenanceWindowExecutionStatus
    StatusDetails: str
    StartTime: datetime
    EndTime: datetime
    OwnerInformation: str
    WindowTargetId: str


GetMaintenanceWindowExecutionTaskResultTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskResultTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "TaskArn": str,
        "ServiceRole": str,
        "Type": MaintenanceWindowTaskType,
        "TaskParameters": List[Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"]],
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Status": MaintenanceWindowExecutionStatus,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)


class GetMaintenanceWindowResultTypeDef(TypedDict, total=False):
    WindowId: str
    Name: str
    Description: str
    StartDate: str
    EndDate: str
    Schedule: str
    ScheduleTimezone: str
    ScheduleOffset: int
    NextExecutionTime: str
    Duration: int
    Cutoff: int
    AllowUnassociatedTargets: bool
    Enabled: bool
    CreatedDate: datetime
    ModifiedDate: datetime


class GetMaintenanceWindowTaskResultTypeDef(TypedDict, total=False):
    WindowId: str
    WindowTaskId: str
    Targets: List["TargetTypeDef"]
    TaskArn: str
    ServiceRoleArn: str
    TaskType: MaintenanceWindowTaskType
    TaskParameters: Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"]
    TaskInvocationParameters: "MaintenanceWindowTaskInvocationParametersTypeDef"
    Priority: int
    MaxConcurrency: str
    MaxErrors: str
    LoggingInfo: "LoggingInfoTypeDef"
    Name: str
    Description: str


class GetOpsItemResponseTypeDef(TypedDict, total=False):
    OpsItem: "OpsItemTypeDef"


class GetOpsMetadataResultTypeDef(TypedDict, total=False):
    ResourceId: str
    Metadata: Dict[str, "MetadataValueTypeDef"]
    NextToken: str


class GetOpsSummaryResultTypeDef(TypedDict, total=False):
    Entities: List["OpsEntityTypeDef"]
    NextToken: str


class GetParameterHistoryResultTypeDef(TypedDict, total=False):
    Parameters: List["ParameterHistoryTypeDef"]
    NextToken: str


class GetParameterResultTypeDef(TypedDict, total=False):
    Parameter: "ParameterTypeDef"


class GetParametersByPathResultTypeDef(TypedDict, total=False):
    Parameters: List["ParameterTypeDef"]
    NextToken: str


class GetParametersResultTypeDef(TypedDict, total=False):
    Parameters: List["ParameterTypeDef"]
    InvalidParameters: List[str]


class GetPatchBaselineForPatchGroupResultTypeDef(TypedDict, total=False):
    BaselineId: str
    PatchGroup: str
    OperatingSystem: OperatingSystem


class GetPatchBaselineResultTypeDef(TypedDict, total=False):
    BaselineId: str
    Name: str
    OperatingSystem: OperatingSystem
    GlobalFilters: "PatchFilterGroupTypeDef"
    ApprovalRules: "PatchRuleGroupTypeDef"
    ApprovedPatches: List[str]
    ApprovedPatchesComplianceLevel: PatchComplianceLevel
    ApprovedPatchesEnableNonSecurity: bool
    RejectedPatches: List[str]
    RejectedPatchesAction: PatchAction
    PatchGroups: List[str]
    CreatedDate: datetime
    ModifiedDate: datetime
    Description: str
    Sources: List["PatchSourceTypeDef"]


class GetServiceSettingResultTypeDef(TypedDict, total=False):
    ServiceSetting: "ServiceSettingTypeDef"


class InstanceAggregatedAssociationOverviewTypeDef(TypedDict, total=False):
    DetailedStatus: str
    InstanceAssociationStatusAggregatedCount: Dict[str, int]


class InstanceAssociationOutputLocationTypeDef(TypedDict, total=False):
    S3Location: "S3OutputLocationTypeDef"


class InstanceAssociationOutputUrlTypeDef(TypedDict, total=False):
    S3OutputUrl: "S3OutputUrlTypeDef"


class InstanceAssociationStatusInfoTypeDef(TypedDict, total=False):
    AssociationId: str
    Name: str
    DocumentVersion: str
    AssociationVersion: str
    InstanceId: str
    ExecutionDate: datetime
    Status: str
    DetailedStatus: str
    ExecutionSummary: str
    ErrorCode: str
    OutputUrl: "InstanceAssociationOutputUrlTypeDef"
    AssociationName: str


class InstanceAssociationTypeDef(TypedDict, total=False):
    AssociationId: str
    InstanceId: str
    Content: str
    AssociationVersion: str


class InstanceInformationFilterTypeDef(TypedDict):
    key: InstanceInformationFilterKey
    valueSet: List[str]


class InstanceInformationStringFilterTypeDef(TypedDict):
    Key: str
    Values: List[str]


class InstanceInformationTypeDef(TypedDict, total=False):
    InstanceId: str
    PingStatus: PingStatus
    LastPingDateTime: datetime
    AgentVersion: str
    IsLatestVersion: bool
    PlatformType: PlatformType
    PlatformName: str
    PlatformVersion: str
    ActivationId: str
    IamRole: str
    RegistrationDate: datetime
    ResourceType: ResourceType
    Name: str
    IPAddress: str
    ComputerName: str
    AssociationStatus: str
    LastAssociationExecutionDate: datetime
    LastSuccessfulAssociationExecutionDate: datetime
    AssociationOverview: "InstanceAggregatedAssociationOverviewTypeDef"


InstancePatchStateFilterTypeDef = TypedDict(
    "InstancePatchStateFilterTypeDef",
    {"Key": str, "Values": List[str], "Type": InstancePatchStateOperatorType},
)


class _RequiredInstancePatchStateTypeDef(TypedDict):
    InstanceId: str
    PatchGroup: str
    BaselineId: str
    OperationStartTime: datetime
    OperationEndTime: datetime
    Operation: PatchOperationType


class InstancePatchStateTypeDef(_RequiredInstancePatchStateTypeDef, total=False):
    SnapshotId: str
    InstallOverrideList: str
    OwnerInformation: str
    InstalledCount: int
    InstalledOtherCount: int
    InstalledPendingRebootCount: int
    InstalledRejectedCount: int
    MissingCount: int
    FailedCount: int
    UnreportedNotApplicableCount: int
    NotApplicableCount: int
    LastNoRebootInstallOperationTime: datetime
    RebootOption: RebootOption
    CriticalNonCompliantCount: int
    SecurityNonCompliantCount: int
    OtherNonCompliantCount: int


class InventoryAggregatorTypeDef(TypedDict, total=False):
    Expression: str
    Aggregators: List[Dict[str, Any]]
    Groups: List["InventoryGroupTypeDef"]


class InventoryDeletionStatusItemTypeDef(TypedDict, total=False):
    DeletionId: str
    TypeName: str
    DeletionStartTime: datetime
    LastStatus: InventoryDeletionStatus
    LastStatusMessage: str
    DeletionSummary: "InventoryDeletionSummaryTypeDef"
    LastStatusUpdateTime: datetime


class InventoryDeletionSummaryItemTypeDef(TypedDict, total=False):
    Version: str
    Count: int
    RemainingCount: int


class InventoryDeletionSummaryTypeDef(TypedDict, total=False):
    TotalCount: int
    RemainingCount: int
    SummaryItems: List["InventoryDeletionSummaryItemTypeDef"]


_RequiredInventoryFilterTypeDef = TypedDict(
    "_RequiredInventoryFilterTypeDef", {"Key": str, "Values": List[str]}
)
_OptionalInventoryFilterTypeDef = TypedDict(
    "_OptionalInventoryFilterTypeDef", {"Type": InventoryQueryOperatorType}, total=False
)


class InventoryFilterTypeDef(_RequiredInventoryFilterTypeDef, _OptionalInventoryFilterTypeDef):
    pass


class InventoryGroupTypeDef(TypedDict):
    Name: str
    Filters: List["InventoryFilterTypeDef"]


class InventoryItemAttributeTypeDef(TypedDict):
    Name: str
    DataType: InventoryAttributeDataType


class _RequiredInventoryItemSchemaTypeDef(TypedDict):
    TypeName: str
    Attributes: List["InventoryItemAttributeTypeDef"]


class InventoryItemSchemaTypeDef(_RequiredInventoryItemSchemaTypeDef, total=False):
    Version: str
    DisplayName: str


class _RequiredInventoryItemTypeDef(TypedDict):
    TypeName: str
    SchemaVersion: str
    CaptureTime: str


class InventoryItemTypeDef(_RequiredInventoryItemTypeDef, total=False):
    ContentHash: str
    Content: List[Dict[str, str]]
    Context: Dict[str, str]


class InventoryResultEntityTypeDef(TypedDict, total=False):
    Id: str
    Data: Dict[str, "InventoryResultItemTypeDef"]


class _RequiredInventoryResultItemTypeDef(TypedDict):
    TypeName: str
    SchemaVersion: str
    Content: List[Dict[str, str]]


class InventoryResultItemTypeDef(_RequiredInventoryResultItemTypeDef, total=False):
    CaptureTime: str
    ContentHash: str


class LabelParameterVersionResultTypeDef(TypedDict, total=False):
    InvalidLabels: List[str]
    ParameterVersion: int


class ListAssociationVersionsResultTypeDef(TypedDict, total=False):
    AssociationVersions: List["AssociationVersionInfoTypeDef"]
    NextToken: str


class ListAssociationsResultTypeDef(TypedDict, total=False):
    Associations: List["AssociationTypeDef"]
    NextToken: str


class ListCommandInvocationsResultTypeDef(TypedDict, total=False):
    CommandInvocations: List["CommandInvocationTypeDef"]
    NextToken: str


class ListCommandsResultTypeDef(TypedDict, total=False):
    Commands: List["CommandTypeDef"]
    NextToken: str


class ListComplianceItemsResultTypeDef(TypedDict, total=False):
    ComplianceItems: List["ComplianceItemTypeDef"]
    NextToken: str


class ListComplianceSummariesResultTypeDef(TypedDict, total=False):
    ComplianceSummaryItems: List["ComplianceSummaryItemTypeDef"]
    NextToken: str


class ListDocumentMetadataHistoryResponseTypeDef(TypedDict, total=False):
    Name: str
    DocumentVersion: str
    Author: str
    Metadata: "DocumentMetadataResponseInfoTypeDef"
    NextToken: str


class ListDocumentVersionsResultTypeDef(TypedDict, total=False):
    DocumentVersions: List["DocumentVersionInfoTypeDef"]
    NextToken: str


class ListDocumentsResultTypeDef(TypedDict, total=False):
    DocumentIdentifiers: List["DocumentIdentifierTypeDef"]
    NextToken: str


class ListInventoryEntriesResultTypeDef(TypedDict, total=False):
    TypeName: str
    InstanceId: str
    SchemaVersion: str
    CaptureTime: str
    Entries: List[Dict[str, str]]
    NextToken: str


class ListOpsItemEventsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Summaries: List["OpsItemEventSummaryTypeDef"]


class ListOpsMetadataResultTypeDef(TypedDict, total=False):
    OpsMetadataList: List["OpsMetadataTypeDef"]
    NextToken: str


class ListResourceComplianceSummariesResultTypeDef(TypedDict, total=False):
    ResourceComplianceSummaryItems: List["ResourceComplianceSummaryItemTypeDef"]
    NextToken: str


class ListResourceDataSyncResultTypeDef(TypedDict, total=False):
    ResourceDataSyncItems: List["ResourceDataSyncItemTypeDef"]
    NextToken: str


class ListTagsForResourceResultTypeDef(TypedDict, total=False):
    TagList: List["TagTypeDef"]


class _RequiredLoggingInfoTypeDef(TypedDict):
    S3BucketName: str
    S3Region: str


class LoggingInfoTypeDef(_RequiredLoggingInfoTypeDef, total=False):
    S3KeyPrefix: str


class MaintenanceWindowAutomationParametersTypeDef(TypedDict, total=False):
    DocumentVersion: str
    Parameters: Dict[str, List[str]]


class MaintenanceWindowExecutionTaskIdentityTypeDef(TypedDict, total=False):
    WindowExecutionId: str
    TaskExecutionId: str
    Status: MaintenanceWindowExecutionStatus
    StatusDetails: str
    StartTime: datetime
    EndTime: datetime
    TaskArn: str
    TaskType: MaintenanceWindowTaskType


class MaintenanceWindowExecutionTaskInvocationIdentityTypeDef(TypedDict, total=False):
    WindowExecutionId: str
    TaskExecutionId: str
    InvocationId: str
    ExecutionId: str
    TaskType: MaintenanceWindowTaskType
    Parameters: str
    Status: MaintenanceWindowExecutionStatus
    StatusDetails: str
    StartTime: datetime
    EndTime: datetime
    OwnerInformation: str
    WindowTargetId: str


class MaintenanceWindowExecutionTypeDef(TypedDict, total=False):
    WindowId: str
    WindowExecutionId: str
    Status: MaintenanceWindowExecutionStatus
    StatusDetails: str
    StartTime: datetime
    EndTime: datetime


class MaintenanceWindowFilterTypeDef(TypedDict, total=False):
    Key: str
    Values: List[str]


class MaintenanceWindowIdentityForTargetTypeDef(TypedDict, total=False):
    WindowId: str
    Name: str


class MaintenanceWindowIdentityTypeDef(TypedDict, total=False):
    WindowId: str
    Name: str
    Description: str
    Enabled: bool
    Duration: int
    Cutoff: int
    Schedule: str
    ScheduleTimezone: str
    ScheduleOffset: int
    EndDate: str
    StartDate: str
    NextExecutionTime: str


class MaintenanceWindowLambdaParametersTypeDef(TypedDict, total=False):
    ClientContext: str
    Qualifier: str
    Payload: Union[bytes, IO[bytes]]


class MaintenanceWindowRunCommandParametersTypeDef(TypedDict, total=False):
    Comment: str
    CloudWatchOutputConfig: "CloudWatchOutputConfigTypeDef"
    DocumentHash: str
    DocumentHashType: DocumentHashType
    DocumentVersion: str
    NotificationConfig: "NotificationConfigTypeDef"
    OutputS3BucketName: str
    OutputS3KeyPrefix: str
    Parameters: Dict[str, List[str]]
    ServiceRoleArn: str
    TimeoutSeconds: int


class MaintenanceWindowStepFunctionsParametersTypeDef(TypedDict, total=False):
    Input: str
    Name: str


class MaintenanceWindowTargetTypeDef(TypedDict, total=False):
    WindowId: str
    WindowTargetId: str
    ResourceType: MaintenanceWindowResourceType
    Targets: List["TargetTypeDef"]
    OwnerInformation: str
    Name: str
    Description: str


class MaintenanceWindowTaskInvocationParametersTypeDef(TypedDict, total=False):
    RunCommand: "MaintenanceWindowRunCommandParametersTypeDef"
    Automation: "MaintenanceWindowAutomationParametersTypeDef"
    StepFunctions: "MaintenanceWindowStepFunctionsParametersTypeDef"
    Lambda: "MaintenanceWindowLambdaParametersTypeDef"


class MaintenanceWindowTaskParameterValueExpressionTypeDef(TypedDict, total=False):
    Values: List[str]


MaintenanceWindowTaskTypeDef = TypedDict(
    "MaintenanceWindowTaskTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "TaskArn": str,
        "Type": MaintenanceWindowTaskType,
        "Targets": List["TargetTypeDef"],
        "TaskParameters": Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"],
        "Priority": int,
        "LoggingInfo": "LoggingInfoTypeDef",
        "ServiceRoleArn": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)


class MetadataValueTypeDef(TypedDict, total=False):
    Value: str


class NonCompliantSummaryTypeDef(TypedDict, total=False):
    NonCompliantCount: int
    SeveritySummary: "SeveritySummaryTypeDef"


class NotificationConfigTypeDef(TypedDict, total=False):
    NotificationArn: str
    NotificationEvents: List[NotificationEvent]
    NotificationType: NotificationType


class OpsAggregatorTypeDef(TypedDict, total=False):
    AggregatorType: str
    TypeName: str
    AttributeName: str
    Values: Dict[str, str]
    Filters: List["OpsFilterTypeDef"]
    Aggregators: List[Dict[str, Any]]


class OpsEntityItemTypeDef(TypedDict, total=False):
    CaptureTime: str
    Content: List[Dict[str, str]]


class OpsEntityTypeDef(TypedDict, total=False):
    Id: str
    Data: Dict[str, "OpsEntityItemTypeDef"]


_RequiredOpsFilterTypeDef = TypedDict(
    "_RequiredOpsFilterTypeDef", {"Key": str, "Values": List[str]}
)
_OptionalOpsFilterTypeDef = TypedDict(
    "_OptionalOpsFilterTypeDef", {"Type": OpsFilterOperatorType}, total=False
)


class OpsFilterTypeDef(_RequiredOpsFilterTypeDef, _OptionalOpsFilterTypeDef):
    pass


OpsItemDataValueTypeDef = TypedDict(
    "OpsItemDataValueTypeDef", {"Value": str, "Type": OpsItemDataType}, total=False
)


class OpsItemEventFilterTypeDef(TypedDict):
    Key: Literal["OpsItemId"]
    Values: List[str]
    Operator: Literal["Equal"]


class OpsItemEventSummaryTypeDef(TypedDict, total=False):
    OpsItemId: str
    EventId: str
    Source: str
    DetailType: str
    Detail: str
    CreatedBy: "OpsItemIdentityTypeDef"
    CreatedTime: datetime


class OpsItemFilterTypeDef(TypedDict):
    Key: OpsItemFilterKey
    Values: List[str]
    Operator: OpsItemFilterOperator


class OpsItemIdentityTypeDef(TypedDict, total=False):
    Arn: str


class OpsItemNotificationTypeDef(TypedDict, total=False):
    Arn: str


class OpsItemSummaryTypeDef(TypedDict, total=False):
    CreatedBy: str
    CreatedTime: datetime
    LastModifiedBy: str
    LastModifiedTime: datetime
    Priority: int
    Source: str
    Status: OpsItemStatus
    OpsItemId: str
    Title: str
    OperationalData: Dict[str, "OpsItemDataValueTypeDef"]
    Category: str
    Severity: str
    OpsItemType: str
    ActualStartTime: datetime
    ActualEndTime: datetime
    PlannedStartTime: datetime
    PlannedEndTime: datetime


class OpsItemTypeDef(TypedDict, total=False):
    CreatedBy: str
    OpsItemType: str
    CreatedTime: datetime
    Description: str
    LastModifiedBy: str
    LastModifiedTime: datetime
    Notifications: List["OpsItemNotificationTypeDef"]
    Priority: int
    RelatedOpsItems: List["RelatedOpsItemTypeDef"]
    Status: OpsItemStatus
    OpsItemId: str
    Version: str
    Title: str
    Source: str
    OperationalData: Dict[str, "OpsItemDataValueTypeDef"]
    Category: str
    Severity: str
    ActualStartTime: datetime
    ActualEndTime: datetime
    PlannedStartTime: datetime
    PlannedEndTime: datetime


class OpsMetadataFilterTypeDef(TypedDict):
    Key: str
    Values: List[str]


class OpsMetadataTypeDef(TypedDict, total=False):
    ResourceId: str
    OpsMetadataArn: str
    LastModifiedDate: datetime
    LastModifiedUser: str
    CreationDate: datetime


class OpsResultAttributeTypeDef(TypedDict):
    TypeName: str


class OutputSourceTypeDef(TypedDict, total=False):
    OutputSourceId: str
    OutputSourceType: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


ParameterHistoryTypeDef = TypedDict(
    "ParameterHistoryTypeDef",
    {
        "Name": str,
        "Type": ParameterType,
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "Value": str,
        "AllowedPattern": str,
        "Version": int,
        "Labels": List[str],
        "Tier": ParameterTier,
        "Policies": List["ParameterInlinePolicyTypeDef"],
        "DataType": str,
    },
    total=False,
)


class ParameterInlinePolicyTypeDef(TypedDict, total=False):
    PolicyText: str
    PolicyType: str
    PolicyStatus: str


ParameterMetadataTypeDef = TypedDict(
    "ParameterMetadataTypeDef",
    {
        "Name": str,
        "Type": ParameterType,
        "KeyId": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "Description": str,
        "AllowedPattern": str,
        "Version": int,
        "Tier": ParameterTier,
        "Policies": List["ParameterInlinePolicyTypeDef"],
        "DataType": str,
    },
    total=False,
)


class _RequiredParameterStringFilterTypeDef(TypedDict):
    Key: str


class ParameterStringFilterTypeDef(_RequiredParameterStringFilterTypeDef, total=False):
    Option: str
    Values: List[str]


ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "Name": str,
        "Type": ParameterType,
        "Value": str,
        "Version": int,
        "Selector": str,
        "SourceResult": str,
        "LastModifiedDate": datetime,
        "ARN": str,
        "DataType": str,
    },
    total=False,
)


class ParametersFilterTypeDef(TypedDict):
    Key: ParametersFilterKey
    Values: List[str]


class PatchBaselineIdentityTypeDef(TypedDict, total=False):
    BaselineId: str
    BaselineName: str
    OperatingSystem: OperatingSystem
    BaselineDescription: str
    DefaultBaseline: bool


class _RequiredPatchComplianceDataTypeDef(TypedDict):
    Title: str
    KBId: str
    Classification: str
    Severity: str
    State: PatchComplianceDataState
    InstalledTime: datetime


class PatchComplianceDataTypeDef(_RequiredPatchComplianceDataTypeDef, total=False):
    CVEIds: str


class PatchFilterGroupTypeDef(TypedDict):
    PatchFilters: List["PatchFilterTypeDef"]


class PatchFilterTypeDef(TypedDict):
    Key: PatchFilterKey
    Values: List[str]


class PatchGroupPatchBaselineMappingTypeDef(TypedDict, total=False):
    PatchGroup: str
    BaselineIdentity: "PatchBaselineIdentityTypeDef"


class PatchOrchestratorFilterTypeDef(TypedDict, total=False):
    Key: str
    Values: List[str]


class PatchRuleGroupTypeDef(TypedDict):
    PatchRules: List["PatchRuleTypeDef"]


class _RequiredPatchRuleTypeDef(TypedDict):
    PatchFilterGroup: "PatchFilterGroupTypeDef"


class PatchRuleTypeDef(_RequiredPatchRuleTypeDef, total=False):
    ComplianceLevel: PatchComplianceLevel
    ApproveAfterDays: int
    ApproveUntilDate: str
    EnableNonSecurity: bool


class PatchSourceTypeDef(TypedDict):
    Name: str
    Products: List[str]
    Configuration: str


class PatchStatusTypeDef(TypedDict, total=False):
    DeploymentStatus: PatchDeploymentStatus
    ComplianceLevel: PatchComplianceLevel
    ApprovalDate: datetime


class PatchTypeDef(TypedDict, total=False):
    Id: str
    ReleaseDate: datetime
    Title: str
    Description: str
    ContentUrl: str
    Vendor: str
    ProductFamily: str
    Product: str
    Classification: str
    MsrcSeverity: str
    KbNumber: str
    MsrcNumber: str
    Language: str
    AdvisoryIds: List[str]
    BugzillaIds: List[str]
    CVEIds: List[str]
    Name: str
    Epoch: int
    Version: str
    Release: str
    Arch: str
    Severity: str
    Repository: str


class ProgressCountersTypeDef(TypedDict, total=False):
    TotalSteps: int
    SuccessSteps: int
    FailedSteps: int
    CancelledSteps: int
    TimedOutSteps: int


class PutInventoryResultTypeDef(TypedDict, total=False):
    Message: str


class PutParameterResultTypeDef(TypedDict, total=False):
    Version: int
    Tier: ParameterTier


class RegisterDefaultPatchBaselineResultTypeDef(TypedDict, total=False):
    BaselineId: str


class RegisterPatchBaselineForPatchGroupResultTypeDef(TypedDict, total=False):
    BaselineId: str
    PatchGroup: str


class RegisterTargetWithMaintenanceWindowResultTypeDef(TypedDict, total=False):
    WindowTargetId: str


class RegisterTaskWithMaintenanceWindowResultTypeDef(TypedDict, total=False):
    WindowTaskId: str


class RelatedOpsItemTypeDef(TypedDict):
    OpsItemId: str


class ResetServiceSettingResultTypeDef(TypedDict, total=False):
    ServiceSetting: "ServiceSettingTypeDef"


class ResolvedTargetsTypeDef(TypedDict, total=False):
    ParameterValues: List[str]
    Truncated: bool


class ResourceComplianceSummaryItemTypeDef(TypedDict, total=False):
    ComplianceType: str
    ResourceType: str
    ResourceId: str
    Status: ComplianceStatus
    OverallSeverity: ComplianceSeverity
    ExecutionSummary: "ComplianceExecutionSummaryTypeDef"
    CompliantSummary: "CompliantSummaryTypeDef"
    NonCompliantSummary: "NonCompliantSummaryTypeDef"


class _RequiredResourceDataSyncAwsOrganizationsSourceTypeDef(TypedDict):
    OrganizationSourceType: str


class ResourceDataSyncAwsOrganizationsSourceTypeDef(
    _RequiredResourceDataSyncAwsOrganizationsSourceTypeDef, total=False
):
    OrganizationalUnits: List["ResourceDataSyncOrganizationalUnitTypeDef"]


class ResourceDataSyncDestinationDataSharingTypeDef(TypedDict, total=False):
    DestinationDataSharingType: str


class ResourceDataSyncItemTypeDef(TypedDict, total=False):
    SyncName: str
    SyncType: str
    SyncSource: "ResourceDataSyncSourceWithStateTypeDef"
    S3Destination: "ResourceDataSyncS3DestinationTypeDef"
    LastSyncTime: datetime
    LastSuccessfulSyncTime: datetime
    SyncLastModifiedTime: datetime
    LastStatus: LastResourceDataSyncStatus
    SyncCreatedTime: datetime
    LastSyncStatusMessage: str


class ResourceDataSyncOrganizationalUnitTypeDef(TypedDict, total=False):
    OrganizationalUnitId: str


class _RequiredResourceDataSyncS3DestinationTypeDef(TypedDict):
    BucketName: str
    SyncFormat: Literal["JsonSerDe"]
    Region: str


class ResourceDataSyncS3DestinationTypeDef(
    _RequiredResourceDataSyncS3DestinationTypeDef, total=False
):
    Prefix: str
    AWSKMSKeyARN: str
    DestinationDataSharing: "ResourceDataSyncDestinationDataSharingTypeDef"


class _RequiredResourceDataSyncSourceTypeDef(TypedDict):
    SourceType: str
    SourceRegions: List[str]


class ResourceDataSyncSourceTypeDef(_RequiredResourceDataSyncSourceTypeDef, total=False):
    AwsOrganizationsSource: "ResourceDataSyncAwsOrganizationsSourceTypeDef"
    IncludeFutureRegions: bool
    EnableAllOpsDataSources: bool


class ResourceDataSyncSourceWithStateTypeDef(TypedDict, total=False):
    SourceType: str
    AwsOrganizationsSource: "ResourceDataSyncAwsOrganizationsSourceTypeDef"
    SourceRegions: List[str]
    IncludeFutureRegions: bool
    State: str
    EnableAllOpsDataSources: bool


class ResultAttributeTypeDef(TypedDict):
    TypeName: str


class ResumeSessionResponseTypeDef(TypedDict, total=False):
    SessionId: str
    TokenValue: str
    StreamUrl: str


class ReviewInformationTypeDef(TypedDict, total=False):
    ReviewedTime: datetime
    Status: ReviewStatus
    Reviewer: str


class _RequiredRunbookTypeDef(TypedDict):
    DocumentName: str


class RunbookTypeDef(_RequiredRunbookTypeDef, total=False):
    DocumentVersion: str
    Parameters: Dict[str, List[str]]
    TargetParameterName: str
    Targets: List["TargetTypeDef"]
    MaxConcurrency: str
    MaxErrors: str
    TargetLocations: List["TargetLocationTypeDef"]


class S3OutputLocationTypeDef(TypedDict, total=False):
    OutputS3Region: str
    OutputS3BucketName: str
    OutputS3KeyPrefix: str


class S3OutputUrlTypeDef(TypedDict, total=False):
    OutputUrl: str


class ScheduledWindowExecutionTypeDef(TypedDict, total=False):
    WindowId: str
    Name: str
    ExecutionTime: str


class SendCommandResultTypeDef(TypedDict, total=False):
    Command: "CommandTypeDef"


class ServiceSettingTypeDef(TypedDict, total=False):
    SettingId: str
    SettingValue: str
    LastModifiedDate: datetime
    LastModifiedUser: str
    ARN: str
    Status: str


class SessionFilterTypeDef(TypedDict):
    key: SessionFilterKey
    value: str


class SessionManagerOutputUrlTypeDef(TypedDict, total=False):
    S3OutputUrl: str
    CloudWatchOutputUrl: str


class SessionTypeDef(TypedDict, total=False):
    SessionId: str
    Target: str
    Status: SessionStatus
    StartDate: datetime
    EndDate: datetime
    DocumentName: str
    Owner: str
    Details: str
    OutputUrl: "SessionManagerOutputUrlTypeDef"


class SeveritySummaryTypeDef(TypedDict, total=False):
    CriticalCount: int
    HighCount: int
    MediumCount: int
    LowCount: int
    InformationalCount: int
    UnspecifiedCount: int


class StartAutomationExecutionResultTypeDef(TypedDict, total=False):
    AutomationExecutionId: str


class StartChangeRequestExecutionResultTypeDef(TypedDict, total=False):
    AutomationExecutionId: str


class StartSessionResponseTypeDef(TypedDict, total=False):
    SessionId: str
    TokenValue: str
    StreamUrl: str


class StepExecutionFilterTypeDef(TypedDict):
    Key: StepExecutionFilterKey
    Values: List[str]


class StepExecutionTypeDef(TypedDict, total=False):
    StepName: str
    Action: str
    TimeoutSeconds: int
    OnFailure: str
    MaxAttempts: int
    ExecutionStartTime: datetime
    ExecutionEndTime: datetime
    StepStatus: AutomationExecutionStatus
    ResponseCode: str
    Inputs: Dict[str, str]
    Outputs: Dict[str, List[str]]
    Response: str
    FailureMessage: str
    FailureDetails: "FailureDetailsTypeDef"
    StepExecutionId: str
    OverriddenParameters: Dict[str, List[str]]
    IsEnd: bool
    NextStep: str
    IsCritical: bool
    ValidNextSteps: List[str]
    Targets: List["TargetTypeDef"]
    TargetLocation: "TargetLocationTypeDef"


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TargetLocationTypeDef(TypedDict, total=False):
    Accounts: List[str]
    Regions: List[str]
    TargetLocationMaxConcurrency: str
    TargetLocationMaxErrors: str
    ExecutionRoleName: str


class TargetTypeDef(TypedDict, total=False):
    Key: str
    Values: List[str]


class TerminateSessionResponseTypeDef(TypedDict, total=False):
    SessionId: str


class UnlabelParameterVersionResultTypeDef(TypedDict, total=False):
    RemovedLabels: List[str]
    InvalidLabels: List[str]


class UpdateAssociationResultTypeDef(TypedDict, total=False):
    AssociationDescription: "AssociationDescriptionTypeDef"


class UpdateAssociationStatusResultTypeDef(TypedDict, total=False):
    AssociationDescription: "AssociationDescriptionTypeDef"


class UpdateDocumentDefaultVersionResultTypeDef(TypedDict, total=False):
    Description: "DocumentDefaultVersionDescriptionTypeDef"


class UpdateDocumentResultTypeDef(TypedDict, total=False):
    DocumentDescription: "DocumentDescriptionTypeDef"


class UpdateMaintenanceWindowResultTypeDef(TypedDict, total=False):
    WindowId: str
    Name: str
    Description: str
    StartDate: str
    EndDate: str
    Schedule: str
    ScheduleTimezone: str
    ScheduleOffset: int
    Duration: int
    Cutoff: int
    AllowUnassociatedTargets: bool
    Enabled: bool


class UpdateMaintenanceWindowTargetResultTypeDef(TypedDict, total=False):
    WindowId: str
    WindowTargetId: str
    Targets: List["TargetTypeDef"]
    OwnerInformation: str
    Name: str
    Description: str


class UpdateMaintenanceWindowTaskResultTypeDef(TypedDict, total=False):
    WindowId: str
    WindowTaskId: str
    Targets: List["TargetTypeDef"]
    TaskArn: str
    ServiceRoleArn: str
    TaskParameters: Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"]
    TaskInvocationParameters: "MaintenanceWindowTaskInvocationParametersTypeDef"
    Priority: int
    MaxConcurrency: str
    MaxErrors: str
    LoggingInfo: "LoggingInfoTypeDef"
    Name: str
    Description: str


class UpdateOpsMetadataResultTypeDef(TypedDict, total=False):
    OpsMetadataArn: str


class UpdatePatchBaselineResultTypeDef(TypedDict, total=False):
    BaselineId: str
    Name: str
    OperatingSystem: OperatingSystem
    GlobalFilters: "PatchFilterGroupTypeDef"
    ApprovalRules: "PatchRuleGroupTypeDef"
    ApprovedPatches: List[str]
    ApprovedPatchesComplianceLevel: PatchComplianceLevel
    ApprovedPatchesEnableNonSecurity: bool
    RejectedPatches: List[str]
    RejectedPatchesAction: PatchAction
    CreatedDate: datetime
    ModifiedDate: datetime
    Description: str
    Sources: List["PatchSourceTypeDef"]


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
