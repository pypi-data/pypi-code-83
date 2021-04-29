"""
Main interface for ssm service type definitions.

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
    AttachmentHashType,
    AttachmentsSourceKey,
    AutomationExecutionFilterKey,
    AutomationExecutionStatus,
    AutomationSubtype,
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
    DocumentReviewCommentType,
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
    OpsItemEventFilterKey,
    OpsItemEventFilterOperator,
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
    ResourceDataSyncS3Format,
    ResourceType,
    ReviewStatus,
    SessionFilterKey,
    SessionStatus,
    StepExecutionFilterKey,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountSharingInfoTypeDef",
    "ActivationTypeDef",
    "AssociationDescriptionTypeDef",
    "AssociationExecutionTargetTypeDef",
    "AssociationExecutionTypeDef",
    "AssociationOverviewTypeDef",
    "AssociationStatusTypeDef",
    "AssociationTypeDef",
    "AssociationVersionInfoTypeDef",
    "AttachmentContentTypeDef",
    "AttachmentInformationTypeDef",
    "AutomationExecutionMetadataTypeDef",
    "AutomationExecutionTypeDef",
    "CloudWatchOutputConfigTypeDef",
    "CommandInvocationTypeDef",
    "CommandPluginTypeDef",
    "CommandTypeDef",
    "ComplianceExecutionSummaryTypeDef",
    "ComplianceItemTypeDef",
    "ComplianceSummaryItemTypeDef",
    "CompliantSummaryTypeDef",
    "CreateAssociationBatchRequestEntryTypeDef",
    "DocumentDefaultVersionDescriptionTypeDef",
    "DocumentDescriptionTypeDef",
    "DocumentIdentifierTypeDef",
    "DocumentMetadataResponseInfoTypeDef",
    "DocumentParameterTypeDef",
    "DocumentRequiresTypeDef",
    "DocumentReviewCommentSourceTypeDef",
    "DocumentReviewerResponseSourceTypeDef",
    "DocumentVersionInfoTypeDef",
    "EffectivePatchTypeDef",
    "FailedCreateAssociationTypeDef",
    "FailureDetailsTypeDef",
    "InstanceAggregatedAssociationOverviewTypeDef",
    "InstanceAssociationOutputLocationTypeDef",
    "InstanceAssociationOutputUrlTypeDef",
    "InstanceAssociationStatusInfoTypeDef",
    "InstanceAssociationTypeDef",
    "InstanceInformationTypeDef",
    "InstancePatchStateTypeDef",
    "InventoryDeletionStatusItemTypeDef",
    "InventoryDeletionSummaryItemTypeDef",
    "InventoryDeletionSummaryTypeDef",
    "InventoryFilterTypeDef",
    "InventoryGroupTypeDef",
    "InventoryItemAttributeTypeDef",
    "InventoryItemSchemaTypeDef",
    "InventoryResultEntityTypeDef",
    "InventoryResultItemTypeDef",
    "LoggingInfoTypeDef",
    "MaintenanceWindowAutomationParametersTypeDef",
    "MaintenanceWindowExecutionTaskIdentityTypeDef",
    "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef",
    "MaintenanceWindowExecutionTypeDef",
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
    "OpsEntityItemTypeDef",
    "OpsEntityTypeDef",
    "OpsFilterTypeDef",
    "OpsItemDataValueTypeDef",
    "OpsItemEventSummaryTypeDef",
    "OpsItemIdentityTypeDef",
    "OpsItemNotificationTypeDef",
    "OpsItemSummaryTypeDef",
    "OpsItemTypeDef",
    "OpsMetadataTypeDef",
    "OutputSourceTypeDef",
    "ParameterHistoryTypeDef",
    "ParameterInlinePolicyTypeDef",
    "ParameterMetadataTypeDef",
    "ParameterTypeDef",
    "PatchBaselineIdentityTypeDef",
    "PatchComplianceDataTypeDef",
    "PatchFilterGroupTypeDef",
    "PatchFilterTypeDef",
    "PatchGroupPatchBaselineMappingTypeDef",
    "PatchRuleGroupTypeDef",
    "PatchRuleTypeDef",
    "PatchSourceTypeDef",
    "PatchStatusTypeDef",
    "PatchTypeDef",
    "ProgressCountersTypeDef",
    "RelatedOpsItemTypeDef",
    "ResolvedTargetsTypeDef",
    "ResourceComplianceSummaryItemTypeDef",
    "ResourceDataSyncAwsOrganizationsSourceTypeDef",
    "ResourceDataSyncDestinationDataSharingTypeDef",
    "ResourceDataSyncItemTypeDef",
    "ResourceDataSyncOrganizationalUnitTypeDef",
    "ResourceDataSyncS3DestinationTypeDef",
    "ResourceDataSyncSourceWithStateTypeDef",
    "ReviewInformationTypeDef",
    "RunbookTypeDef",
    "S3OutputLocationTypeDef",
    "S3OutputUrlTypeDef",
    "ScheduledWindowExecutionTypeDef",
    "ServiceSettingTypeDef",
    "SessionManagerOutputUrlTypeDef",
    "SessionTypeDef",
    "SeveritySummaryTypeDef",
    "StepExecutionTypeDef",
    "TagTypeDef",
    "TargetLocationTypeDef",
    "TargetTypeDef",
    "AssociationExecutionFilterTypeDef",
    "AssociationExecutionTargetsFilterTypeDef",
    "AssociationFilterTypeDef",
    "AttachmentsSourceTypeDef",
    "AutomationExecutionFilterTypeDef",
    "BaselineOverrideTypeDef",
    "CancelMaintenanceWindowExecutionResultTypeDef",
    "CommandFilterTypeDef",
    "ComplianceItemEntryTypeDef",
    "ComplianceStringFilterTypeDef",
    "CreateActivationResultTypeDef",
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
    "OpsAggregatorTypeDef",
    "InventoryAggregatorTypeDef",
    "DocumentFilterTypeDef",
    "DocumentKeyValuesFilterTypeDef",
    "DocumentReviewsTypeDef",
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
    "InstanceInformationFilterTypeDef",
    "InstanceInformationStringFilterTypeDef",
    "InstancePatchStateFilterTypeDef",
    "InventoryItemTypeDef",
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
    "MaintenanceWindowFilterTypeDef",
    "OpsItemEventFilterTypeDef",
    "OpsItemFilterTypeDef",
    "OpsMetadataFilterTypeDef",
    "OpsResultAttributeTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterStringFilterTypeDef",
    "ParametersFilterTypeDef",
    "PatchOrchestratorFilterTypeDef",
    "PutInventoryResultTypeDef",
    "PutParameterResultTypeDef",
    "RegisterDefaultPatchBaselineResultTypeDef",
    "RegisterPatchBaselineForPatchGroupResultTypeDef",
    "RegisterTargetWithMaintenanceWindowResultTypeDef",
    "RegisterTaskWithMaintenanceWindowResultTypeDef",
    "ResetServiceSettingResultTypeDef",
    "ResourceDataSyncSourceTypeDef",
    "ResultAttributeTypeDef",
    "ResumeSessionResponseTypeDef",
    "SendCommandResultTypeDef",
    "SessionFilterTypeDef",
    "StartAutomationExecutionResultTypeDef",
    "StartChangeRequestExecutionResultTypeDef",
    "StartSessionResponseTypeDef",
    "StepExecutionFilterTypeDef",
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

AccountSharingInfoTypeDef = TypedDict(
    "AccountSharingInfoTypeDef", {"AccountId": str, "SharedDocumentVersion": str}, total=False
)

ActivationTypeDef = TypedDict(
    "ActivationTypeDef",
    {
        "ActivationId": str,
        "Description": str,
        "DefaultInstanceName": str,
        "IamRole": str,
        "RegistrationLimit": int,
        "RegistrationsCount": int,
        "ExpirationDate": datetime,
        "Expired": bool,
        "CreatedDate": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

AssociationDescriptionTypeDef = TypedDict(
    "AssociationDescriptionTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationVersion": str,
        "Date": datetime,
        "LastUpdateAssociationDate": datetime,
        "Status": "AssociationStatusTypeDef",
        "Overview": "AssociationOverviewTypeDef",
        "DocumentVersion": str,
        "AutomationTargetParameterName": str,
        "Parameters": Dict[str, List[str]],
        "AssociationId": str,
        "Targets": List["TargetTypeDef"],
        "ScheduleExpression": str,
        "OutputLocation": "InstanceAssociationOutputLocationTypeDef",
        "LastExecutionDate": datetime,
        "LastSuccessfulExecutionDate": datetime,
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": AssociationComplianceSeverity,
        "SyncCompliance": AssociationSyncCompliance,
        "ApplyOnlyAtCronInterval": bool,
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)

AssociationExecutionTargetTypeDef = TypedDict(
    "AssociationExecutionTargetTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "ResourceId": str,
        "ResourceType": str,
        "Status": str,
        "DetailedStatus": str,
        "LastExecutionDate": datetime,
        "OutputSource": "OutputSourceTypeDef",
    },
    total=False,
)

AssociationExecutionTypeDef = TypedDict(
    "AssociationExecutionTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "ExecutionId": str,
        "Status": str,
        "DetailedStatus": str,
        "CreatedTime": datetime,
        "LastExecutionDate": datetime,
        "ResourceCountByStatus": str,
    },
    total=False,
)

AssociationOverviewTypeDef = TypedDict(
    "AssociationOverviewTypeDef",
    {"Status": str, "DetailedStatus": str, "AssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

_RequiredAssociationStatusTypeDef = TypedDict(
    "_RequiredAssociationStatusTypeDef",
    {"Date": datetime, "Name": AssociationStatusName, "Message": str},
)
_OptionalAssociationStatusTypeDef = TypedDict(
    "_OptionalAssociationStatusTypeDef", {"AdditionalInfo": str}, total=False
)


class AssociationStatusTypeDef(
    _RequiredAssociationStatusTypeDef, _OptionalAssociationStatusTypeDef
):
    pass


AssociationTypeDef = TypedDict(
    "AssociationTypeDef",
    {
        "Name": str,
        "InstanceId": str,
        "AssociationId": str,
        "AssociationVersion": str,
        "DocumentVersion": str,
        "Targets": List["TargetTypeDef"],
        "LastExecutionDate": datetime,
        "Overview": "AssociationOverviewTypeDef",
        "ScheduleExpression": str,
        "AssociationName": str,
    },
    total=False,
)

AssociationVersionInfoTypeDef = TypedDict(
    "AssociationVersionInfoTypeDef",
    {
        "AssociationId": str,
        "AssociationVersion": str,
        "CreatedDate": datetime,
        "Name": str,
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "Targets": List["TargetTypeDef"],
        "ScheduleExpression": str,
        "OutputLocation": "InstanceAssociationOutputLocationTypeDef",
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": AssociationComplianceSeverity,
        "SyncCompliance": AssociationSyncCompliance,
        "ApplyOnlyAtCronInterval": bool,
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)

AttachmentContentTypeDef = TypedDict(
    "AttachmentContentTypeDef",
    {"Name": str, "Size": int, "Hash": str, "HashType": AttachmentHashType, "Url": str},
    total=False,
)

AttachmentInformationTypeDef = TypedDict("AttachmentInformationTypeDef", {"Name": str}, total=False)

AutomationExecutionMetadataTypeDef = TypedDict(
    "AutomationExecutionMetadataTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "AutomationExecutionStatus": AutomationExecutionStatus,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "ExecutedBy": str,
        "LogFile": str,
        "Outputs": Dict[str, List[str]],
        "Mode": ExecutionMode,
        "ParentAutomationExecutionId": str,
        "CurrentStepName": str,
        "CurrentAction": str,
        "FailureMessage": str,
        "TargetParameterName": str,
        "Targets": List["TargetTypeDef"],
        "TargetMaps": List[Dict[str, List[str]]],
        "ResolvedTargets": "ResolvedTargetsTypeDef",
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Target": str,
        "AutomationType": AutomationType,
        "AutomationSubtype": AutomationSubtype,
        "ScheduledTime": datetime,
        "Runbooks": List["RunbookTypeDef"],
        "OpsItemId": str,
        "AssociationId": str,
        "ChangeRequestName": str,
    },
    total=False,
)

AutomationExecutionTypeDef = TypedDict(
    "AutomationExecutionTypeDef",
    {
        "AutomationExecutionId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "AutomationExecutionStatus": AutomationExecutionStatus,
        "StepExecutions": List["StepExecutionTypeDef"],
        "StepExecutionsTruncated": bool,
        "Parameters": Dict[str, List[str]],
        "Outputs": Dict[str, List[str]],
        "FailureMessage": str,
        "Mode": ExecutionMode,
        "ParentAutomationExecutionId": str,
        "ExecutedBy": str,
        "CurrentStepName": str,
        "CurrentAction": str,
        "TargetParameterName": str,
        "Targets": List["TargetTypeDef"],
        "TargetMaps": List[Dict[str, List[str]]],
        "ResolvedTargets": "ResolvedTargetsTypeDef",
        "MaxConcurrency": str,
        "MaxErrors": str,
        "Target": str,
        "TargetLocations": List["TargetLocationTypeDef"],
        "ProgressCounters": "ProgressCountersTypeDef",
        "AutomationSubtype": AutomationSubtype,
        "ScheduledTime": datetime,
        "Runbooks": List["RunbookTypeDef"],
        "OpsItemId": str,
        "AssociationId": str,
        "ChangeRequestName": str,
    },
    total=False,
)

CloudWatchOutputConfigTypeDef = TypedDict(
    "CloudWatchOutputConfigTypeDef",
    {"CloudWatchLogGroupName": str, "CloudWatchOutputEnabled": bool},
    total=False,
)

CommandInvocationTypeDef = TypedDict(
    "CommandInvocationTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "InstanceName": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "RequestedDateTime": datetime,
        "Status": CommandInvocationStatus,
        "StatusDetails": str,
        "TraceOutput": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "CommandPlugins": List["CommandPluginTypeDef"],
        "ServiceRole": str,
        "NotificationConfig": "NotificationConfigTypeDef",
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
    },
    total=False,
)

CommandPluginTypeDef = TypedDict(
    "CommandPluginTypeDef",
    {
        "Name": str,
        "Status": CommandPluginStatus,
        "StatusDetails": str,
        "ResponseCode": int,
        "ResponseStartDateTime": datetime,
        "ResponseFinishDateTime": datetime,
        "Output": str,
        "StandardOutputUrl": str,
        "StandardErrorUrl": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
    },
    total=False,
)

CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "CommandId": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "Comment": str,
        "ExpiresAfter": datetime,
        "Parameters": Dict[str, List[str]],
        "InstanceIds": List[str],
        "Targets": List["TargetTypeDef"],
        "RequestedDateTime": datetime,
        "Status": CommandStatus,
        "StatusDetails": str,
        "OutputS3Region": str,
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetCount": int,
        "CompletedCount": int,
        "ErrorCount": int,
        "DeliveryTimedOutCount": int,
        "ServiceRole": str,
        "NotificationConfig": "NotificationConfigTypeDef",
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
        "TimeoutSeconds": int,
    },
    total=False,
)

_RequiredComplianceExecutionSummaryTypeDef = TypedDict(
    "_RequiredComplianceExecutionSummaryTypeDef", {"ExecutionTime": datetime}
)
_OptionalComplianceExecutionSummaryTypeDef = TypedDict(
    "_OptionalComplianceExecutionSummaryTypeDef",
    {"ExecutionId": str, "ExecutionType": str},
    total=False,
)


class ComplianceExecutionSummaryTypeDef(
    _RequiredComplianceExecutionSummaryTypeDef, _OptionalComplianceExecutionSummaryTypeDef
):
    pass


ComplianceItemTypeDef = TypedDict(
    "ComplianceItemTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Id": str,
        "Title": str,
        "Status": ComplianceStatus,
        "Severity": ComplianceSeverity,
        "ExecutionSummary": "ComplianceExecutionSummaryTypeDef",
        "Details": Dict[str, str],
    },
    total=False,
)

ComplianceSummaryItemTypeDef = TypedDict(
    "ComplianceSummaryItemTypeDef",
    {
        "ComplianceType": str,
        "CompliantSummary": "CompliantSummaryTypeDef",
        "NonCompliantSummary": "NonCompliantSummaryTypeDef",
    },
    total=False,
)

CompliantSummaryTypeDef = TypedDict(
    "CompliantSummaryTypeDef",
    {"CompliantCount": int, "SeveritySummary": "SeveritySummaryTypeDef"},
    total=False,
)

_RequiredCreateAssociationBatchRequestEntryTypeDef = TypedDict(
    "_RequiredCreateAssociationBatchRequestEntryTypeDef", {"Name": str}
)
_OptionalCreateAssociationBatchRequestEntryTypeDef = TypedDict(
    "_OptionalCreateAssociationBatchRequestEntryTypeDef",
    {
        "InstanceId": str,
        "Parameters": Dict[str, List[str]],
        "AutomationTargetParameterName": str,
        "DocumentVersion": str,
        "Targets": List["TargetTypeDef"],
        "ScheduleExpression": str,
        "OutputLocation": "InstanceAssociationOutputLocationTypeDef",
        "AssociationName": str,
        "MaxErrors": str,
        "MaxConcurrency": str,
        "ComplianceSeverity": AssociationComplianceSeverity,
        "SyncCompliance": AssociationSyncCompliance,
        "ApplyOnlyAtCronInterval": bool,
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)


class CreateAssociationBatchRequestEntryTypeDef(
    _RequiredCreateAssociationBatchRequestEntryTypeDef,
    _OptionalCreateAssociationBatchRequestEntryTypeDef,
):
    pass


DocumentDefaultVersionDescriptionTypeDef = TypedDict(
    "DocumentDefaultVersionDescriptionTypeDef",
    {"Name": str, "DefaultVersion": str, "DefaultVersionName": str},
    total=False,
)

DocumentDescriptionTypeDef = TypedDict(
    "DocumentDescriptionTypeDef",
    {
        "Sha1": str,
        "Hash": str,
        "HashType": DocumentHashType,
        "Name": str,
        "VersionName": str,
        "Owner": str,
        "CreatedDate": datetime,
        "Status": DocumentStatus,
        "StatusInformation": str,
        "DocumentVersion": str,
        "Description": str,
        "Parameters": List["DocumentParameterTypeDef"],
        "PlatformTypes": List[PlatformType],
        "DocumentType": DocumentType,
        "SchemaVersion": str,
        "LatestVersion": str,
        "DefaultVersion": str,
        "DocumentFormat": DocumentFormat,
        "TargetType": str,
        "Tags": List["TagTypeDef"],
        "AttachmentsInformation": List["AttachmentInformationTypeDef"],
        "Requires": List["DocumentRequiresTypeDef"],
        "Author": str,
        "ReviewInformation": List["ReviewInformationTypeDef"],
        "ApprovedVersion": str,
        "PendingReviewVersion": str,
        "ReviewStatus": ReviewStatus,
    },
    total=False,
)

DocumentIdentifierTypeDef = TypedDict(
    "DocumentIdentifierTypeDef",
    {
        "Name": str,
        "Owner": str,
        "VersionName": str,
        "PlatformTypes": List[PlatformType],
        "DocumentVersion": str,
        "DocumentType": DocumentType,
        "SchemaVersion": str,
        "DocumentFormat": DocumentFormat,
        "TargetType": str,
        "Tags": List["TagTypeDef"],
        "Requires": List["DocumentRequiresTypeDef"],
        "ReviewStatus": ReviewStatus,
        "Author": str,
    },
    total=False,
)

DocumentMetadataResponseInfoTypeDef = TypedDict(
    "DocumentMetadataResponseInfoTypeDef",
    {"ReviewerResponse": List["DocumentReviewerResponseSourceTypeDef"]},
    total=False,
)

DocumentParameterTypeDef = TypedDict(
    "DocumentParameterTypeDef",
    {"Name": str, "Type": DocumentParameterType, "Description": str, "DefaultValue": str},
    total=False,
)

_RequiredDocumentRequiresTypeDef = TypedDict("_RequiredDocumentRequiresTypeDef", {"Name": str})
_OptionalDocumentRequiresTypeDef = TypedDict(
    "_OptionalDocumentRequiresTypeDef", {"Version": str}, total=False
)


class DocumentRequiresTypeDef(_RequiredDocumentRequiresTypeDef, _OptionalDocumentRequiresTypeDef):
    pass


DocumentReviewCommentSourceTypeDef = TypedDict(
    "DocumentReviewCommentSourceTypeDef",
    {"Type": DocumentReviewCommentType, "Content": str},
    total=False,
)

DocumentReviewerResponseSourceTypeDef = TypedDict(
    "DocumentReviewerResponseSourceTypeDef",
    {
        "CreateTime": datetime,
        "UpdatedTime": datetime,
        "ReviewStatus": ReviewStatus,
        "Comment": List["DocumentReviewCommentSourceTypeDef"],
        "Reviewer": str,
    },
    total=False,
)

DocumentVersionInfoTypeDef = TypedDict(
    "DocumentVersionInfoTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
        "VersionName": str,
        "CreatedDate": datetime,
        "IsDefaultVersion": bool,
        "DocumentFormat": DocumentFormat,
        "Status": DocumentStatus,
        "StatusInformation": str,
        "ReviewStatus": ReviewStatus,
    },
    total=False,
)

EffectivePatchTypeDef = TypedDict(
    "EffectivePatchTypeDef",
    {"Patch": "PatchTypeDef", "PatchStatus": "PatchStatusTypeDef"},
    total=False,
)

FailedCreateAssociationTypeDef = TypedDict(
    "FailedCreateAssociationTypeDef",
    {"Entry": "CreateAssociationBatchRequestEntryTypeDef", "Message": str, "Fault": Fault},
    total=False,
)

FailureDetailsTypeDef = TypedDict(
    "FailureDetailsTypeDef",
    {"FailureStage": str, "FailureType": str, "Details": Dict[str, List[str]]},
    total=False,
)

InstanceAggregatedAssociationOverviewTypeDef = TypedDict(
    "InstanceAggregatedAssociationOverviewTypeDef",
    {"DetailedStatus": str, "InstanceAssociationStatusAggregatedCount": Dict[str, int]},
    total=False,
)

InstanceAssociationOutputLocationTypeDef = TypedDict(
    "InstanceAssociationOutputLocationTypeDef",
    {"S3Location": "S3OutputLocationTypeDef"},
    total=False,
)

InstanceAssociationOutputUrlTypeDef = TypedDict(
    "InstanceAssociationOutputUrlTypeDef", {"S3OutputUrl": "S3OutputUrlTypeDef"}, total=False
)

InstanceAssociationStatusInfoTypeDef = TypedDict(
    "InstanceAssociationStatusInfoTypeDef",
    {
        "AssociationId": str,
        "Name": str,
        "DocumentVersion": str,
        "AssociationVersion": str,
        "InstanceId": str,
        "ExecutionDate": datetime,
        "Status": str,
        "DetailedStatus": str,
        "ExecutionSummary": str,
        "ErrorCode": str,
        "OutputUrl": "InstanceAssociationOutputUrlTypeDef",
        "AssociationName": str,
    },
    total=False,
)

InstanceAssociationTypeDef = TypedDict(
    "InstanceAssociationTypeDef",
    {"AssociationId": str, "InstanceId": str, "Content": str, "AssociationVersion": str},
    total=False,
)

InstanceInformationTypeDef = TypedDict(
    "InstanceInformationTypeDef",
    {
        "InstanceId": str,
        "PingStatus": PingStatus,
        "LastPingDateTime": datetime,
        "AgentVersion": str,
        "IsLatestVersion": bool,
        "PlatformType": PlatformType,
        "PlatformName": str,
        "PlatformVersion": str,
        "ActivationId": str,
        "IamRole": str,
        "RegistrationDate": datetime,
        "ResourceType": ResourceType,
        "Name": str,
        "IPAddress": str,
        "ComputerName": str,
        "AssociationStatus": str,
        "LastAssociationExecutionDate": datetime,
        "LastSuccessfulAssociationExecutionDate": datetime,
        "AssociationOverview": "InstanceAggregatedAssociationOverviewTypeDef",
    },
    total=False,
)

_RequiredInstancePatchStateTypeDef = TypedDict(
    "_RequiredInstancePatchStateTypeDef",
    {
        "InstanceId": str,
        "PatchGroup": str,
        "BaselineId": str,
        "OperationStartTime": datetime,
        "OperationEndTime": datetime,
        "Operation": PatchOperationType,
    },
)
_OptionalInstancePatchStateTypeDef = TypedDict(
    "_OptionalInstancePatchStateTypeDef",
    {
        "SnapshotId": str,
        "InstallOverrideList": str,
        "OwnerInformation": str,
        "InstalledCount": int,
        "InstalledOtherCount": int,
        "InstalledPendingRebootCount": int,
        "InstalledRejectedCount": int,
        "MissingCount": int,
        "FailedCount": int,
        "UnreportedNotApplicableCount": int,
        "NotApplicableCount": int,
        "LastNoRebootInstallOperationTime": datetime,
        "RebootOption": RebootOption,
        "CriticalNonCompliantCount": int,
        "SecurityNonCompliantCount": int,
        "OtherNonCompliantCount": int,
    },
    total=False,
)


class InstancePatchStateTypeDef(
    _RequiredInstancePatchStateTypeDef, _OptionalInstancePatchStateTypeDef
):
    pass


InventoryDeletionStatusItemTypeDef = TypedDict(
    "InventoryDeletionStatusItemTypeDef",
    {
        "DeletionId": str,
        "TypeName": str,
        "DeletionStartTime": datetime,
        "LastStatus": InventoryDeletionStatus,
        "LastStatusMessage": str,
        "DeletionSummary": "InventoryDeletionSummaryTypeDef",
        "LastStatusUpdateTime": datetime,
    },
    total=False,
)

InventoryDeletionSummaryItemTypeDef = TypedDict(
    "InventoryDeletionSummaryItemTypeDef",
    {"Version": str, "Count": int, "RemainingCount": int},
    total=False,
)

InventoryDeletionSummaryTypeDef = TypedDict(
    "InventoryDeletionSummaryTypeDef",
    {
        "TotalCount": int,
        "RemainingCount": int,
        "SummaryItems": List["InventoryDeletionSummaryItemTypeDef"],
    },
    total=False,
)

_RequiredInventoryFilterTypeDef = TypedDict(
    "_RequiredInventoryFilterTypeDef", {"Key": str, "Values": List[str]}
)
_OptionalInventoryFilterTypeDef = TypedDict(
    "_OptionalInventoryFilterTypeDef", {"Type": InventoryQueryOperatorType}, total=False
)


class InventoryFilterTypeDef(_RequiredInventoryFilterTypeDef, _OptionalInventoryFilterTypeDef):
    pass


InventoryGroupTypeDef = TypedDict(
    "InventoryGroupTypeDef", {"Name": str, "Filters": List["InventoryFilterTypeDef"]}
)

InventoryItemAttributeTypeDef = TypedDict(
    "InventoryItemAttributeTypeDef", {"Name": str, "DataType": InventoryAttributeDataType}
)

_RequiredInventoryItemSchemaTypeDef = TypedDict(
    "_RequiredInventoryItemSchemaTypeDef",
    {"TypeName": str, "Attributes": List["InventoryItemAttributeTypeDef"]},
)
_OptionalInventoryItemSchemaTypeDef = TypedDict(
    "_OptionalInventoryItemSchemaTypeDef", {"Version": str, "DisplayName": str}, total=False
)


class InventoryItemSchemaTypeDef(
    _RequiredInventoryItemSchemaTypeDef, _OptionalInventoryItemSchemaTypeDef
):
    pass


InventoryResultEntityTypeDef = TypedDict(
    "InventoryResultEntityTypeDef",
    {"Id": str, "Data": Dict[str, "InventoryResultItemTypeDef"]},
    total=False,
)

_RequiredInventoryResultItemTypeDef = TypedDict(
    "_RequiredInventoryResultItemTypeDef",
    {"TypeName": str, "SchemaVersion": str, "Content": List[Dict[str, str]]},
)
_OptionalInventoryResultItemTypeDef = TypedDict(
    "_OptionalInventoryResultItemTypeDef", {"CaptureTime": str, "ContentHash": str}, total=False
)


class InventoryResultItemTypeDef(
    _RequiredInventoryResultItemTypeDef, _OptionalInventoryResultItemTypeDef
):
    pass


_RequiredLoggingInfoTypeDef = TypedDict(
    "_RequiredLoggingInfoTypeDef", {"S3BucketName": str, "S3Region": str}
)
_OptionalLoggingInfoTypeDef = TypedDict(
    "_OptionalLoggingInfoTypeDef", {"S3KeyPrefix": str}, total=False
)


class LoggingInfoTypeDef(_RequiredLoggingInfoTypeDef, _OptionalLoggingInfoTypeDef):
    pass


MaintenanceWindowAutomationParametersTypeDef = TypedDict(
    "MaintenanceWindowAutomationParametersTypeDef",
    {"DocumentVersion": str, "Parameters": Dict[str, List[str]]},
    total=False,
)

MaintenanceWindowExecutionTaskIdentityTypeDef = TypedDict(
    "MaintenanceWindowExecutionTaskIdentityTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "Status": MaintenanceWindowExecutionStatus,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "TaskArn": str,
        "TaskType": MaintenanceWindowTaskType,
    },
    total=False,
)

MaintenanceWindowExecutionTaskInvocationIdentityTypeDef = TypedDict(
    "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": MaintenanceWindowTaskType,
        "Parameters": str,
        "Status": MaintenanceWindowExecutionStatus,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
    },
    total=False,
)

MaintenanceWindowExecutionTypeDef = TypedDict(
    "MaintenanceWindowExecutionTypeDef",
    {
        "WindowId": str,
        "WindowExecutionId": str,
        "Status": MaintenanceWindowExecutionStatus,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

MaintenanceWindowIdentityForTargetTypeDef = TypedDict(
    "MaintenanceWindowIdentityForTargetTypeDef", {"WindowId": str, "Name": str}, total=False
)

MaintenanceWindowIdentityTypeDef = TypedDict(
    "MaintenanceWindowIdentityTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "Enabled": bool,
        "Duration": int,
        "Cutoff": int,
        "Schedule": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "EndDate": str,
        "StartDate": str,
        "NextExecutionTime": str,
    },
    total=False,
)

MaintenanceWindowLambdaParametersTypeDef = TypedDict(
    "MaintenanceWindowLambdaParametersTypeDef",
    {"ClientContext": str, "Qualifier": str, "Payload": Union[bytes, IO[bytes]]},
    total=False,
)

MaintenanceWindowRunCommandParametersTypeDef = TypedDict(
    "MaintenanceWindowRunCommandParametersTypeDef",
    {
        "Comment": str,
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
        "DocumentHash": str,
        "DocumentHashType": DocumentHashType,
        "DocumentVersion": str,
        "NotificationConfig": "NotificationConfigTypeDef",
        "OutputS3BucketName": str,
        "OutputS3KeyPrefix": str,
        "Parameters": Dict[str, List[str]],
        "ServiceRoleArn": str,
        "TimeoutSeconds": int,
    },
    total=False,
)

MaintenanceWindowStepFunctionsParametersTypeDef = TypedDict(
    "MaintenanceWindowStepFunctionsParametersTypeDef", {"Input": str, "Name": str}, total=False
)

MaintenanceWindowTargetTypeDef = TypedDict(
    "MaintenanceWindowTargetTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "ResourceType": MaintenanceWindowResourceType,
        "Targets": List["TargetTypeDef"],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

MaintenanceWindowTaskInvocationParametersTypeDef = TypedDict(
    "MaintenanceWindowTaskInvocationParametersTypeDef",
    {
        "RunCommand": "MaintenanceWindowRunCommandParametersTypeDef",
        "Automation": "MaintenanceWindowAutomationParametersTypeDef",
        "StepFunctions": "MaintenanceWindowStepFunctionsParametersTypeDef",
        "Lambda": "MaintenanceWindowLambdaParametersTypeDef",
    },
    total=False,
)

MaintenanceWindowTaskParameterValueExpressionTypeDef = TypedDict(
    "MaintenanceWindowTaskParameterValueExpressionTypeDef", {"Values": List[str]}, total=False
)

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

MetadataValueTypeDef = TypedDict("MetadataValueTypeDef", {"Value": str}, total=False)

NonCompliantSummaryTypeDef = TypedDict(
    "NonCompliantSummaryTypeDef",
    {"NonCompliantCount": int, "SeveritySummary": "SeveritySummaryTypeDef"},
    total=False,
)

NotificationConfigTypeDef = TypedDict(
    "NotificationConfigTypeDef",
    {
        "NotificationArn": str,
        "NotificationEvents": List[NotificationEvent],
        "NotificationType": NotificationType,
    },
    total=False,
)

OpsEntityItemTypeDef = TypedDict(
    "OpsEntityItemTypeDef", {"CaptureTime": str, "Content": List[Dict[str, str]]}, total=False
)

OpsEntityTypeDef = TypedDict(
    "OpsEntityTypeDef", {"Id": str, "Data": Dict[str, "OpsEntityItemTypeDef"]}, total=False
)

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

OpsItemEventSummaryTypeDef = TypedDict(
    "OpsItemEventSummaryTypeDef",
    {
        "OpsItemId": str,
        "EventId": str,
        "Source": str,
        "DetailType": str,
        "Detail": str,
        "CreatedBy": "OpsItemIdentityTypeDef",
        "CreatedTime": datetime,
    },
    total=False,
)

OpsItemIdentityTypeDef = TypedDict("OpsItemIdentityTypeDef", {"Arn": str}, total=False)

OpsItemNotificationTypeDef = TypedDict("OpsItemNotificationTypeDef", {"Arn": str}, total=False)

OpsItemSummaryTypeDef = TypedDict(
    "OpsItemSummaryTypeDef",
    {
        "CreatedBy": str,
        "CreatedTime": datetime,
        "LastModifiedBy": str,
        "LastModifiedTime": datetime,
        "Priority": int,
        "Source": str,
        "Status": OpsItemStatus,
        "OpsItemId": str,
        "Title": str,
        "OperationalData": Dict[str, "OpsItemDataValueTypeDef"],
        "Category": str,
        "Severity": str,
        "OpsItemType": str,
        "ActualStartTime": datetime,
        "ActualEndTime": datetime,
        "PlannedStartTime": datetime,
        "PlannedEndTime": datetime,
    },
    total=False,
)

OpsItemTypeDef = TypedDict(
    "OpsItemTypeDef",
    {
        "CreatedBy": str,
        "OpsItemType": str,
        "CreatedTime": datetime,
        "Description": str,
        "LastModifiedBy": str,
        "LastModifiedTime": datetime,
        "Notifications": List["OpsItemNotificationTypeDef"],
        "Priority": int,
        "RelatedOpsItems": List["RelatedOpsItemTypeDef"],
        "Status": OpsItemStatus,
        "OpsItemId": str,
        "Version": str,
        "Title": str,
        "Source": str,
        "OperationalData": Dict[str, "OpsItemDataValueTypeDef"],
        "Category": str,
        "Severity": str,
        "ActualStartTime": datetime,
        "ActualEndTime": datetime,
        "PlannedStartTime": datetime,
        "PlannedEndTime": datetime,
    },
    total=False,
)

OpsMetadataTypeDef = TypedDict(
    "OpsMetadataTypeDef",
    {
        "ResourceId": str,
        "OpsMetadataArn": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "CreationDate": datetime,
    },
    total=False,
)

OutputSourceTypeDef = TypedDict(
    "OutputSourceTypeDef", {"OutputSourceId": str, "OutputSourceType": str}, total=False
)

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

ParameterInlinePolicyTypeDef = TypedDict(
    "ParameterInlinePolicyTypeDef",
    {"PolicyText": str, "PolicyType": str, "PolicyStatus": str},
    total=False,
)

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

PatchBaselineIdentityTypeDef = TypedDict(
    "PatchBaselineIdentityTypeDef",
    {
        "BaselineId": str,
        "BaselineName": str,
        "OperatingSystem": OperatingSystem,
        "BaselineDescription": str,
        "DefaultBaseline": bool,
    },
    total=False,
)

_RequiredPatchComplianceDataTypeDef = TypedDict(
    "_RequiredPatchComplianceDataTypeDef",
    {
        "Title": str,
        "KBId": str,
        "Classification": str,
        "Severity": str,
        "State": PatchComplianceDataState,
        "InstalledTime": datetime,
    },
)
_OptionalPatchComplianceDataTypeDef = TypedDict(
    "_OptionalPatchComplianceDataTypeDef", {"CVEIds": str}, total=False
)


class PatchComplianceDataTypeDef(
    _RequiredPatchComplianceDataTypeDef, _OptionalPatchComplianceDataTypeDef
):
    pass


PatchFilterGroupTypeDef = TypedDict(
    "PatchFilterGroupTypeDef", {"PatchFilters": List["PatchFilterTypeDef"]}
)

PatchFilterTypeDef = TypedDict("PatchFilterTypeDef", {"Key": PatchFilterKey, "Values": List[str]})

PatchGroupPatchBaselineMappingTypeDef = TypedDict(
    "PatchGroupPatchBaselineMappingTypeDef",
    {"PatchGroup": str, "BaselineIdentity": "PatchBaselineIdentityTypeDef"},
    total=False,
)

PatchRuleGroupTypeDef = TypedDict("PatchRuleGroupTypeDef", {"PatchRules": List["PatchRuleTypeDef"]})

_RequiredPatchRuleTypeDef = TypedDict(
    "_RequiredPatchRuleTypeDef", {"PatchFilterGroup": "PatchFilterGroupTypeDef"}
)
_OptionalPatchRuleTypeDef = TypedDict(
    "_OptionalPatchRuleTypeDef",
    {
        "ComplianceLevel": PatchComplianceLevel,
        "ApproveAfterDays": int,
        "ApproveUntilDate": str,
        "EnableNonSecurity": bool,
    },
    total=False,
)


class PatchRuleTypeDef(_RequiredPatchRuleTypeDef, _OptionalPatchRuleTypeDef):
    pass


PatchSourceTypeDef = TypedDict(
    "PatchSourceTypeDef", {"Name": str, "Products": List[str], "Configuration": str}
)

PatchStatusTypeDef = TypedDict(
    "PatchStatusTypeDef",
    {
        "DeploymentStatus": PatchDeploymentStatus,
        "ComplianceLevel": PatchComplianceLevel,
        "ApprovalDate": datetime,
    },
    total=False,
)

PatchTypeDef = TypedDict(
    "PatchTypeDef",
    {
        "Id": str,
        "ReleaseDate": datetime,
        "Title": str,
        "Description": str,
        "ContentUrl": str,
        "Vendor": str,
        "ProductFamily": str,
        "Product": str,
        "Classification": str,
        "MsrcSeverity": str,
        "KbNumber": str,
        "MsrcNumber": str,
        "Language": str,
        "AdvisoryIds": List[str],
        "BugzillaIds": List[str],
        "CVEIds": List[str],
        "Name": str,
        "Epoch": int,
        "Version": str,
        "Release": str,
        "Arch": str,
        "Severity": str,
        "Repository": str,
    },
    total=False,
)

ProgressCountersTypeDef = TypedDict(
    "ProgressCountersTypeDef",
    {
        "TotalSteps": int,
        "SuccessSteps": int,
        "FailedSteps": int,
        "CancelledSteps": int,
        "TimedOutSteps": int,
    },
    total=False,
)

RelatedOpsItemTypeDef = TypedDict("RelatedOpsItemTypeDef", {"OpsItemId": str})

ResolvedTargetsTypeDef = TypedDict(
    "ResolvedTargetsTypeDef", {"ParameterValues": List[str], "Truncated": bool}, total=False
)

ResourceComplianceSummaryItemTypeDef = TypedDict(
    "ResourceComplianceSummaryItemTypeDef",
    {
        "ComplianceType": str,
        "ResourceType": str,
        "ResourceId": str,
        "Status": ComplianceStatus,
        "OverallSeverity": ComplianceSeverity,
        "ExecutionSummary": "ComplianceExecutionSummaryTypeDef",
        "CompliantSummary": "CompliantSummaryTypeDef",
        "NonCompliantSummary": "NonCompliantSummaryTypeDef",
    },
    total=False,
)

_RequiredResourceDataSyncAwsOrganizationsSourceTypeDef = TypedDict(
    "_RequiredResourceDataSyncAwsOrganizationsSourceTypeDef", {"OrganizationSourceType": str}
)
_OptionalResourceDataSyncAwsOrganizationsSourceTypeDef = TypedDict(
    "_OptionalResourceDataSyncAwsOrganizationsSourceTypeDef",
    {"OrganizationalUnits": List["ResourceDataSyncOrganizationalUnitTypeDef"]},
    total=False,
)


class ResourceDataSyncAwsOrganizationsSourceTypeDef(
    _RequiredResourceDataSyncAwsOrganizationsSourceTypeDef,
    _OptionalResourceDataSyncAwsOrganizationsSourceTypeDef,
):
    pass


ResourceDataSyncDestinationDataSharingTypeDef = TypedDict(
    "ResourceDataSyncDestinationDataSharingTypeDef",
    {"DestinationDataSharingType": str},
    total=False,
)

ResourceDataSyncItemTypeDef = TypedDict(
    "ResourceDataSyncItemTypeDef",
    {
        "SyncName": str,
        "SyncType": str,
        "SyncSource": "ResourceDataSyncSourceWithStateTypeDef",
        "S3Destination": "ResourceDataSyncS3DestinationTypeDef",
        "LastSyncTime": datetime,
        "LastSuccessfulSyncTime": datetime,
        "SyncLastModifiedTime": datetime,
        "LastStatus": LastResourceDataSyncStatus,
        "SyncCreatedTime": datetime,
        "LastSyncStatusMessage": str,
    },
    total=False,
)

ResourceDataSyncOrganizationalUnitTypeDef = TypedDict(
    "ResourceDataSyncOrganizationalUnitTypeDef", {"OrganizationalUnitId": str}, total=False
)

_RequiredResourceDataSyncS3DestinationTypeDef = TypedDict(
    "_RequiredResourceDataSyncS3DestinationTypeDef",
    {"BucketName": str, "SyncFormat": ResourceDataSyncS3Format, "Region": str},
)
_OptionalResourceDataSyncS3DestinationTypeDef = TypedDict(
    "_OptionalResourceDataSyncS3DestinationTypeDef",
    {
        "Prefix": str,
        "AWSKMSKeyARN": str,
        "DestinationDataSharing": "ResourceDataSyncDestinationDataSharingTypeDef",
    },
    total=False,
)


class ResourceDataSyncS3DestinationTypeDef(
    _RequiredResourceDataSyncS3DestinationTypeDef, _OptionalResourceDataSyncS3DestinationTypeDef
):
    pass


ResourceDataSyncSourceWithStateTypeDef = TypedDict(
    "ResourceDataSyncSourceWithStateTypeDef",
    {
        "SourceType": str,
        "AwsOrganizationsSource": "ResourceDataSyncAwsOrganizationsSourceTypeDef",
        "SourceRegions": List[str],
        "IncludeFutureRegions": bool,
        "State": str,
        "EnableAllOpsDataSources": bool,
    },
    total=False,
)

ReviewInformationTypeDef = TypedDict(
    "ReviewInformationTypeDef",
    {"ReviewedTime": datetime, "Status": ReviewStatus, "Reviewer": str},
    total=False,
)

_RequiredRunbookTypeDef = TypedDict("_RequiredRunbookTypeDef", {"DocumentName": str})
_OptionalRunbookTypeDef = TypedDict(
    "_OptionalRunbookTypeDef",
    {
        "DocumentVersion": str,
        "Parameters": Dict[str, List[str]],
        "TargetParameterName": str,
        "Targets": List["TargetTypeDef"],
        "MaxConcurrency": str,
        "MaxErrors": str,
        "TargetLocations": List["TargetLocationTypeDef"],
    },
    total=False,
)


class RunbookTypeDef(_RequiredRunbookTypeDef, _OptionalRunbookTypeDef):
    pass


S3OutputLocationTypeDef = TypedDict(
    "S3OutputLocationTypeDef",
    {"OutputS3Region": str, "OutputS3BucketName": str, "OutputS3KeyPrefix": str},
    total=False,
)

S3OutputUrlTypeDef = TypedDict("S3OutputUrlTypeDef", {"OutputUrl": str}, total=False)

ScheduledWindowExecutionTypeDef = TypedDict(
    "ScheduledWindowExecutionTypeDef",
    {"WindowId": str, "Name": str, "ExecutionTime": str},
    total=False,
)

ServiceSettingTypeDef = TypedDict(
    "ServiceSettingTypeDef",
    {
        "SettingId": str,
        "SettingValue": str,
        "LastModifiedDate": datetime,
        "LastModifiedUser": str,
        "ARN": str,
        "Status": str,
    },
    total=False,
)

SessionManagerOutputUrlTypeDef = TypedDict(
    "SessionManagerOutputUrlTypeDef", {"S3OutputUrl": str, "CloudWatchOutputUrl": str}, total=False
)

SessionTypeDef = TypedDict(
    "SessionTypeDef",
    {
        "SessionId": str,
        "Target": str,
        "Status": SessionStatus,
        "StartDate": datetime,
        "EndDate": datetime,
        "DocumentName": str,
        "Owner": str,
        "Details": str,
        "OutputUrl": "SessionManagerOutputUrlTypeDef",
    },
    total=False,
)

SeveritySummaryTypeDef = TypedDict(
    "SeveritySummaryTypeDef",
    {
        "CriticalCount": int,
        "HighCount": int,
        "MediumCount": int,
        "LowCount": int,
        "InformationalCount": int,
        "UnspecifiedCount": int,
    },
    total=False,
)

StepExecutionTypeDef = TypedDict(
    "StepExecutionTypeDef",
    {
        "StepName": str,
        "Action": str,
        "TimeoutSeconds": int,
        "OnFailure": str,
        "MaxAttempts": int,
        "ExecutionStartTime": datetime,
        "ExecutionEndTime": datetime,
        "StepStatus": AutomationExecutionStatus,
        "ResponseCode": str,
        "Inputs": Dict[str, str],
        "Outputs": Dict[str, List[str]],
        "Response": str,
        "FailureMessage": str,
        "FailureDetails": "FailureDetailsTypeDef",
        "StepExecutionId": str,
        "OverriddenParameters": Dict[str, List[str]],
        "IsEnd": bool,
        "NextStep": str,
        "IsCritical": bool,
        "ValidNextSteps": List[str],
        "Targets": List["TargetTypeDef"],
        "TargetLocation": "TargetLocationTypeDef",
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TargetLocationTypeDef = TypedDict(
    "TargetLocationTypeDef",
    {
        "Accounts": List[str],
        "Regions": List[str],
        "TargetLocationMaxConcurrency": str,
        "TargetLocationMaxErrors": str,
        "ExecutionRoleName": str,
    },
    total=False,
)

TargetTypeDef = TypedDict("TargetTypeDef", {"Key": str, "Values": List[str]}, total=False)

AssociationExecutionFilterTypeDef = TypedDict(
    "AssociationExecutionFilterTypeDef",
    {"Key": AssociationExecutionFilterKey, "Value": str, "Type": AssociationFilterOperatorType},
)

AssociationExecutionTargetsFilterTypeDef = TypedDict(
    "AssociationExecutionTargetsFilterTypeDef",
    {"Key": AssociationExecutionTargetsFilterKey, "Value": str},
)

AssociationFilterTypeDef = TypedDict(
    "AssociationFilterTypeDef", {"key": AssociationFilterKey, "value": str}
)

AttachmentsSourceTypeDef = TypedDict(
    "AttachmentsSourceTypeDef",
    {"Key": AttachmentsSourceKey, "Values": List[str], "Name": str},
    total=False,
)

AutomationExecutionFilterTypeDef = TypedDict(
    "AutomationExecutionFilterTypeDef", {"Key": AutomationExecutionFilterKey, "Values": List[str]}
)

BaselineOverrideTypeDef = TypedDict(
    "BaselineOverrideTypeDef",
    {
        "OperatingSystem": OperatingSystem,
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevel,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchAction,
        "ApprovedPatchesEnableNonSecurity": bool,
        "Sources": List["PatchSourceTypeDef"],
    },
    total=False,
)

CancelMaintenanceWindowExecutionResultTypeDef = TypedDict(
    "CancelMaintenanceWindowExecutionResultTypeDef", {"WindowExecutionId": str}, total=False
)

CommandFilterTypeDef = TypedDict("CommandFilterTypeDef", {"key": CommandFilterKey, "value": str})

_RequiredComplianceItemEntryTypeDef = TypedDict(
    "_RequiredComplianceItemEntryTypeDef",
    {"Severity": ComplianceSeverity, "Status": ComplianceStatus},
)
_OptionalComplianceItemEntryTypeDef = TypedDict(
    "_OptionalComplianceItemEntryTypeDef",
    {"Id": str, "Title": str, "Details": Dict[str, str]},
    total=False,
)


class ComplianceItemEntryTypeDef(
    _RequiredComplianceItemEntryTypeDef, _OptionalComplianceItemEntryTypeDef
):
    pass


ComplianceStringFilterTypeDef = TypedDict(
    "ComplianceStringFilterTypeDef",
    {"Key": str, "Values": List[str], "Type": ComplianceQueryOperatorType},
    total=False,
)

CreateActivationResultTypeDef = TypedDict(
    "CreateActivationResultTypeDef", {"ActivationId": str, "ActivationCode": str}, total=False
)

CreateAssociationBatchResultTypeDef = TypedDict(
    "CreateAssociationBatchResultTypeDef",
    {
        "Successful": List["AssociationDescriptionTypeDef"],
        "Failed": List["FailedCreateAssociationTypeDef"],
    },
    total=False,
)

CreateAssociationResultTypeDef = TypedDict(
    "CreateAssociationResultTypeDef",
    {"AssociationDescription": "AssociationDescriptionTypeDef"},
    total=False,
)

CreateDocumentResultTypeDef = TypedDict(
    "CreateDocumentResultTypeDef",
    {"DocumentDescription": "DocumentDescriptionTypeDef"},
    total=False,
)

CreateMaintenanceWindowResultTypeDef = TypedDict(
    "CreateMaintenanceWindowResultTypeDef", {"WindowId": str}, total=False
)

CreateOpsItemResponseTypeDef = TypedDict(
    "CreateOpsItemResponseTypeDef", {"OpsItemId": str}, total=False
)

CreateOpsMetadataResultTypeDef = TypedDict(
    "CreateOpsMetadataResultTypeDef", {"OpsMetadataArn": str}, total=False
)

CreatePatchBaselineResultTypeDef = TypedDict(
    "CreatePatchBaselineResultTypeDef", {"BaselineId": str}, total=False
)

DeleteInventoryResultTypeDef = TypedDict(
    "DeleteInventoryResultTypeDef",
    {"DeletionId": str, "TypeName": str, "DeletionSummary": "InventoryDeletionSummaryTypeDef"},
    total=False,
)

DeleteMaintenanceWindowResultTypeDef = TypedDict(
    "DeleteMaintenanceWindowResultTypeDef", {"WindowId": str}, total=False
)

DeleteParametersResultTypeDef = TypedDict(
    "DeleteParametersResultTypeDef",
    {"DeletedParameters": List[str], "InvalidParameters": List[str]},
    total=False,
)

DeletePatchBaselineResultTypeDef = TypedDict(
    "DeletePatchBaselineResultTypeDef", {"BaselineId": str}, total=False
)

DeregisterPatchBaselineForPatchGroupResultTypeDef = TypedDict(
    "DeregisterPatchBaselineForPatchGroupResultTypeDef",
    {"BaselineId": str, "PatchGroup": str},
    total=False,
)

DeregisterTargetFromMaintenanceWindowResultTypeDef = TypedDict(
    "DeregisterTargetFromMaintenanceWindowResultTypeDef",
    {"WindowId": str, "WindowTargetId": str},
    total=False,
)

DeregisterTaskFromMaintenanceWindowResultTypeDef = TypedDict(
    "DeregisterTaskFromMaintenanceWindowResultTypeDef",
    {"WindowId": str, "WindowTaskId": str},
    total=False,
)

DescribeActivationsFilterTypeDef = TypedDict(
    "DescribeActivationsFilterTypeDef",
    {"FilterKey": DescribeActivationsFilterKeys, "FilterValues": List[str]},
    total=False,
)

DescribeActivationsResultTypeDef = TypedDict(
    "DescribeActivationsResultTypeDef",
    {"ActivationList": List["ActivationTypeDef"], "NextToken": str},
    total=False,
)

DescribeAssociationExecutionTargetsResultTypeDef = TypedDict(
    "DescribeAssociationExecutionTargetsResultTypeDef",
    {"AssociationExecutionTargets": List["AssociationExecutionTargetTypeDef"], "NextToken": str},
    total=False,
)

DescribeAssociationExecutionsResultTypeDef = TypedDict(
    "DescribeAssociationExecutionsResultTypeDef",
    {"AssociationExecutions": List["AssociationExecutionTypeDef"], "NextToken": str},
    total=False,
)

DescribeAssociationResultTypeDef = TypedDict(
    "DescribeAssociationResultTypeDef",
    {"AssociationDescription": "AssociationDescriptionTypeDef"},
    total=False,
)

DescribeAutomationExecutionsResultTypeDef = TypedDict(
    "DescribeAutomationExecutionsResultTypeDef",
    {
        "AutomationExecutionMetadataList": List["AutomationExecutionMetadataTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeAutomationStepExecutionsResultTypeDef = TypedDict(
    "DescribeAutomationStepExecutionsResultTypeDef",
    {"StepExecutions": List["StepExecutionTypeDef"], "NextToken": str},
    total=False,
)

DescribeAvailablePatchesResultTypeDef = TypedDict(
    "DescribeAvailablePatchesResultTypeDef",
    {"Patches": List["PatchTypeDef"], "NextToken": str},
    total=False,
)

DescribeDocumentPermissionResponseTypeDef = TypedDict(
    "DescribeDocumentPermissionResponseTypeDef",
    {
        "AccountIds": List[str],
        "AccountSharingInfoList": List["AccountSharingInfoTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeDocumentResultTypeDef = TypedDict(
    "DescribeDocumentResultTypeDef", {"Document": "DocumentDescriptionTypeDef"}, total=False
)

DescribeEffectiveInstanceAssociationsResultTypeDef = TypedDict(
    "DescribeEffectiveInstanceAssociationsResultTypeDef",
    {"Associations": List["InstanceAssociationTypeDef"], "NextToken": str},
    total=False,
)

DescribeEffectivePatchesForPatchBaselineResultTypeDef = TypedDict(
    "DescribeEffectivePatchesForPatchBaselineResultTypeDef",
    {"EffectivePatches": List["EffectivePatchTypeDef"], "NextToken": str},
    total=False,
)

DescribeInstanceAssociationsStatusResultTypeDef = TypedDict(
    "DescribeInstanceAssociationsStatusResultTypeDef",
    {
        "InstanceAssociationStatusInfos": List["InstanceAssociationStatusInfoTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeInstanceInformationResultTypeDef = TypedDict(
    "DescribeInstanceInformationResultTypeDef",
    {"InstanceInformationList": List["InstanceInformationTypeDef"], "NextToken": str},
    total=False,
)

DescribeInstancePatchStatesForPatchGroupResultTypeDef = TypedDict(
    "DescribeInstancePatchStatesForPatchGroupResultTypeDef",
    {"InstancePatchStates": List["InstancePatchStateTypeDef"], "NextToken": str},
    total=False,
)

DescribeInstancePatchStatesResultTypeDef = TypedDict(
    "DescribeInstancePatchStatesResultTypeDef",
    {"InstancePatchStates": List["InstancePatchStateTypeDef"], "NextToken": str},
    total=False,
)

DescribeInstancePatchesResultTypeDef = TypedDict(
    "DescribeInstancePatchesResultTypeDef",
    {"Patches": List["PatchComplianceDataTypeDef"], "NextToken": str},
    total=False,
)

DescribeInventoryDeletionsResultTypeDef = TypedDict(
    "DescribeInventoryDeletionsResultTypeDef",
    {"InventoryDeletions": List["InventoryDeletionStatusItemTypeDef"], "NextToken": str},
    total=False,
)

DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTaskInvocationsResultTypeDef",
    {
        "WindowExecutionTaskInvocationIdentities": List[
            "MaintenanceWindowExecutionTaskInvocationIdentityTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

DescribeMaintenanceWindowExecutionTasksResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionTasksResultTypeDef",
    {
        "WindowExecutionTaskIdentities": List["MaintenanceWindowExecutionTaskIdentityTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeMaintenanceWindowExecutionsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowExecutionsResultTypeDef",
    {"WindowExecutions": List["MaintenanceWindowExecutionTypeDef"], "NextToken": str},
    total=False,
)

DescribeMaintenanceWindowScheduleResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowScheduleResultTypeDef",
    {"ScheduledWindowExecutions": List["ScheduledWindowExecutionTypeDef"], "NextToken": str},
    total=False,
)

DescribeMaintenanceWindowTargetsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowTargetsResultTypeDef",
    {"Targets": List["MaintenanceWindowTargetTypeDef"], "NextToken": str},
    total=False,
)

DescribeMaintenanceWindowTasksResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowTasksResultTypeDef",
    {"Tasks": List["MaintenanceWindowTaskTypeDef"], "NextToken": str},
    total=False,
)

DescribeMaintenanceWindowsForTargetResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowsForTargetResultTypeDef",
    {"WindowIdentities": List["MaintenanceWindowIdentityForTargetTypeDef"], "NextToken": str},
    total=False,
)

DescribeMaintenanceWindowsResultTypeDef = TypedDict(
    "DescribeMaintenanceWindowsResultTypeDef",
    {"WindowIdentities": List["MaintenanceWindowIdentityTypeDef"], "NextToken": str},
    total=False,
)

DescribeOpsItemsResponseTypeDef = TypedDict(
    "DescribeOpsItemsResponseTypeDef",
    {"NextToken": str, "OpsItemSummaries": List["OpsItemSummaryTypeDef"]},
    total=False,
)

DescribeParametersResultTypeDef = TypedDict(
    "DescribeParametersResultTypeDef",
    {"Parameters": List["ParameterMetadataTypeDef"], "NextToken": str},
    total=False,
)

DescribePatchBaselinesResultTypeDef = TypedDict(
    "DescribePatchBaselinesResultTypeDef",
    {"BaselineIdentities": List["PatchBaselineIdentityTypeDef"], "NextToken": str},
    total=False,
)

DescribePatchGroupStateResultTypeDef = TypedDict(
    "DescribePatchGroupStateResultTypeDef",
    {
        "Instances": int,
        "InstancesWithInstalledPatches": int,
        "InstancesWithInstalledOtherPatches": int,
        "InstancesWithInstalledPendingRebootPatches": int,
        "InstancesWithInstalledRejectedPatches": int,
        "InstancesWithMissingPatches": int,
        "InstancesWithFailedPatches": int,
        "InstancesWithNotApplicablePatches": int,
        "InstancesWithUnreportedNotApplicablePatches": int,
        "InstancesWithCriticalNonCompliantPatches": int,
        "InstancesWithSecurityNonCompliantPatches": int,
        "InstancesWithOtherNonCompliantPatches": int,
    },
    total=False,
)

DescribePatchGroupsResultTypeDef = TypedDict(
    "DescribePatchGroupsResultTypeDef",
    {"Mappings": List["PatchGroupPatchBaselineMappingTypeDef"], "NextToken": str},
    total=False,
)

DescribePatchPropertiesResultTypeDef = TypedDict(
    "DescribePatchPropertiesResultTypeDef",
    {"Properties": List[Dict[str, str]], "NextToken": str},
    total=False,
)

DescribeSessionsResponseTypeDef = TypedDict(
    "DescribeSessionsResponseTypeDef",
    {"Sessions": List["SessionTypeDef"], "NextToken": str},
    total=False,
)

OpsAggregatorTypeDef = TypedDict(
    "OpsAggregatorTypeDef",
    {
        "AggregatorType": str,
        "TypeName": str,
        "AttributeName": str,
        "Values": Dict[str, str],
        "Filters": List["OpsFilterTypeDef"],
        "Aggregators": List[Dict[str, Any]],
    },
    total=False,
)

InventoryAggregatorTypeDef = TypedDict(
    "InventoryAggregatorTypeDef",
    {
        "Expression": str,
        "Aggregators": List[Dict[str, Any]],
        "Groups": List["InventoryGroupTypeDef"],
    },
    total=False,
)

DocumentFilterTypeDef = TypedDict("DocumentFilterTypeDef", {"key": DocumentFilterKey, "value": str})

DocumentKeyValuesFilterTypeDef = TypedDict(
    "DocumentKeyValuesFilterTypeDef", {"Key": str, "Values": List[str]}, total=False
)

_RequiredDocumentReviewsTypeDef = TypedDict(
    "_RequiredDocumentReviewsTypeDef", {"Action": DocumentReviewAction}
)
_OptionalDocumentReviewsTypeDef = TypedDict(
    "_OptionalDocumentReviewsTypeDef",
    {"Comment": List["DocumentReviewCommentSourceTypeDef"]},
    total=False,
)


class DocumentReviewsTypeDef(_RequiredDocumentReviewsTypeDef, _OptionalDocumentReviewsTypeDef):
    pass


GetAutomationExecutionResultTypeDef = TypedDict(
    "GetAutomationExecutionResultTypeDef",
    {"AutomationExecution": "AutomationExecutionTypeDef"},
    total=False,
)

GetCalendarStateResponseTypeDef = TypedDict(
    "GetCalendarStateResponseTypeDef",
    {"State": CalendarState, "AtTime": str, "NextTransitionTime": str},
    total=False,
)

GetCommandInvocationResultTypeDef = TypedDict(
    "GetCommandInvocationResultTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "Comment": str,
        "DocumentName": str,
        "DocumentVersion": str,
        "PluginName": str,
        "ResponseCode": int,
        "ExecutionStartDateTime": str,
        "ExecutionElapsedTime": str,
        "ExecutionEndDateTime": str,
        "Status": CommandInvocationStatus,
        "StatusDetails": str,
        "StandardOutputContent": str,
        "StandardOutputUrl": str,
        "StandardErrorContent": str,
        "StandardErrorUrl": str,
        "CloudWatchOutputConfig": "CloudWatchOutputConfigTypeDef",
    },
    total=False,
)

GetConnectionStatusResponseTypeDef = TypedDict(
    "GetConnectionStatusResponseTypeDef", {"Target": str, "Status": ConnectionStatus}, total=False
)

GetDefaultPatchBaselineResultTypeDef = TypedDict(
    "GetDefaultPatchBaselineResultTypeDef",
    {"BaselineId": str, "OperatingSystem": OperatingSystem},
    total=False,
)

GetDeployablePatchSnapshotForInstanceResultTypeDef = TypedDict(
    "GetDeployablePatchSnapshotForInstanceResultTypeDef",
    {"InstanceId": str, "SnapshotId": str, "SnapshotDownloadUrl": str, "Product": str},
    total=False,
)

GetDocumentResultTypeDef = TypedDict(
    "GetDocumentResultTypeDef",
    {
        "Name": str,
        "VersionName": str,
        "DocumentVersion": str,
        "Status": DocumentStatus,
        "StatusInformation": str,
        "Content": str,
        "DocumentType": DocumentType,
        "DocumentFormat": DocumentFormat,
        "Requires": List["DocumentRequiresTypeDef"],
        "AttachmentsContent": List["AttachmentContentTypeDef"],
        "ReviewStatus": ReviewStatus,
    },
    total=False,
)

GetInventoryResultTypeDef = TypedDict(
    "GetInventoryResultTypeDef",
    {"Entities": List["InventoryResultEntityTypeDef"], "NextToken": str},
    total=False,
)

GetInventorySchemaResultTypeDef = TypedDict(
    "GetInventorySchemaResultTypeDef",
    {"Schemas": List["InventoryItemSchemaTypeDef"], "NextToken": str},
    total=False,
)

GetMaintenanceWindowExecutionResultTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionResultTypeDef",
    {
        "WindowExecutionId": str,
        "TaskIds": List[str],
        "Status": MaintenanceWindowExecutionStatus,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

GetMaintenanceWindowExecutionTaskInvocationResultTypeDef = TypedDict(
    "GetMaintenanceWindowExecutionTaskInvocationResultTypeDef",
    {
        "WindowExecutionId": str,
        "TaskExecutionId": str,
        "InvocationId": str,
        "ExecutionId": str,
        "TaskType": MaintenanceWindowTaskType,
        "Parameters": str,
        "Status": MaintenanceWindowExecutionStatus,
        "StatusDetails": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "OwnerInformation": str,
        "WindowTargetId": str,
    },
    total=False,
)

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

GetMaintenanceWindowResultTypeDef = TypedDict(
    "GetMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "NextExecutionTime": str,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
    },
    total=False,
)

GetMaintenanceWindowTaskResultTypeDef = TypedDict(
    "GetMaintenanceWindowTaskResultTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List["TargetTypeDef"],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskType": MaintenanceWindowTaskType,
        "TaskParameters": Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"],
        "TaskInvocationParameters": "MaintenanceWindowTaskInvocationParametersTypeDef",
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": "LoggingInfoTypeDef",
        "Name": str,
        "Description": str,
    },
    total=False,
)

GetOpsItemResponseTypeDef = TypedDict(
    "GetOpsItemResponseTypeDef", {"OpsItem": "OpsItemTypeDef"}, total=False
)

GetOpsMetadataResultTypeDef = TypedDict(
    "GetOpsMetadataResultTypeDef",
    {"ResourceId": str, "Metadata": Dict[str, "MetadataValueTypeDef"], "NextToken": str},
    total=False,
)

GetOpsSummaryResultTypeDef = TypedDict(
    "GetOpsSummaryResultTypeDef",
    {"Entities": List["OpsEntityTypeDef"], "NextToken": str},
    total=False,
)

GetParameterHistoryResultTypeDef = TypedDict(
    "GetParameterHistoryResultTypeDef",
    {"Parameters": List["ParameterHistoryTypeDef"], "NextToken": str},
    total=False,
)

GetParameterResultTypeDef = TypedDict(
    "GetParameterResultTypeDef", {"Parameter": "ParameterTypeDef"}, total=False
)

GetParametersByPathResultTypeDef = TypedDict(
    "GetParametersByPathResultTypeDef",
    {"Parameters": List["ParameterTypeDef"], "NextToken": str},
    total=False,
)

GetParametersResultTypeDef = TypedDict(
    "GetParametersResultTypeDef",
    {"Parameters": List["ParameterTypeDef"], "InvalidParameters": List[str]},
    total=False,
)

GetPatchBaselineForPatchGroupResultTypeDef = TypedDict(
    "GetPatchBaselineForPatchGroupResultTypeDef",
    {"BaselineId": str, "PatchGroup": str, "OperatingSystem": OperatingSystem},
    total=False,
)

GetPatchBaselineResultTypeDef = TypedDict(
    "GetPatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": OperatingSystem,
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevel,
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchAction,
        "PatchGroups": List[str],
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List["PatchSourceTypeDef"],
    },
    total=False,
)

GetServiceSettingResultTypeDef = TypedDict(
    "GetServiceSettingResultTypeDef", {"ServiceSetting": "ServiceSettingTypeDef"}, total=False
)

InstanceInformationFilterTypeDef = TypedDict(
    "InstanceInformationFilterTypeDef", {"key": InstanceInformationFilterKey, "valueSet": List[str]}
)

InstanceInformationStringFilterTypeDef = TypedDict(
    "InstanceInformationStringFilterTypeDef", {"Key": str, "Values": List[str]}
)

InstancePatchStateFilterTypeDef = TypedDict(
    "InstancePatchStateFilterTypeDef",
    {"Key": str, "Values": List[str], "Type": InstancePatchStateOperatorType},
)

_RequiredInventoryItemTypeDef = TypedDict(
    "_RequiredInventoryItemTypeDef", {"TypeName": str, "SchemaVersion": str, "CaptureTime": str}
)
_OptionalInventoryItemTypeDef = TypedDict(
    "_OptionalInventoryItemTypeDef",
    {"ContentHash": str, "Content": List[Dict[str, str]], "Context": Dict[str, str]},
    total=False,
)


class InventoryItemTypeDef(_RequiredInventoryItemTypeDef, _OptionalInventoryItemTypeDef):
    pass


LabelParameterVersionResultTypeDef = TypedDict(
    "LabelParameterVersionResultTypeDef",
    {"InvalidLabels": List[str], "ParameterVersion": int},
    total=False,
)

ListAssociationVersionsResultTypeDef = TypedDict(
    "ListAssociationVersionsResultTypeDef",
    {"AssociationVersions": List["AssociationVersionInfoTypeDef"], "NextToken": str},
    total=False,
)

ListAssociationsResultTypeDef = TypedDict(
    "ListAssociationsResultTypeDef",
    {"Associations": List["AssociationTypeDef"], "NextToken": str},
    total=False,
)

ListCommandInvocationsResultTypeDef = TypedDict(
    "ListCommandInvocationsResultTypeDef",
    {"CommandInvocations": List["CommandInvocationTypeDef"], "NextToken": str},
    total=False,
)

ListCommandsResultTypeDef = TypedDict(
    "ListCommandsResultTypeDef", {"Commands": List["CommandTypeDef"], "NextToken": str}, total=False
)

ListComplianceItemsResultTypeDef = TypedDict(
    "ListComplianceItemsResultTypeDef",
    {"ComplianceItems": List["ComplianceItemTypeDef"], "NextToken": str},
    total=False,
)

ListComplianceSummariesResultTypeDef = TypedDict(
    "ListComplianceSummariesResultTypeDef",
    {"ComplianceSummaryItems": List["ComplianceSummaryItemTypeDef"], "NextToken": str},
    total=False,
)

ListDocumentMetadataHistoryResponseTypeDef = TypedDict(
    "ListDocumentMetadataHistoryResponseTypeDef",
    {
        "Name": str,
        "DocumentVersion": str,
        "Author": str,
        "Metadata": "DocumentMetadataResponseInfoTypeDef",
        "NextToken": str,
    },
    total=False,
)

ListDocumentVersionsResultTypeDef = TypedDict(
    "ListDocumentVersionsResultTypeDef",
    {"DocumentVersions": List["DocumentVersionInfoTypeDef"], "NextToken": str},
    total=False,
)

ListDocumentsResultTypeDef = TypedDict(
    "ListDocumentsResultTypeDef",
    {"DocumentIdentifiers": List["DocumentIdentifierTypeDef"], "NextToken": str},
    total=False,
)

ListInventoryEntriesResultTypeDef = TypedDict(
    "ListInventoryEntriesResultTypeDef",
    {
        "TypeName": str,
        "InstanceId": str,
        "SchemaVersion": str,
        "CaptureTime": str,
        "Entries": List[Dict[str, str]],
        "NextToken": str,
    },
    total=False,
)

ListOpsItemEventsResponseTypeDef = TypedDict(
    "ListOpsItemEventsResponseTypeDef",
    {"NextToken": str, "Summaries": List["OpsItemEventSummaryTypeDef"]},
    total=False,
)

ListOpsMetadataResultTypeDef = TypedDict(
    "ListOpsMetadataResultTypeDef",
    {"OpsMetadataList": List["OpsMetadataTypeDef"], "NextToken": str},
    total=False,
)

ListResourceComplianceSummariesResultTypeDef = TypedDict(
    "ListResourceComplianceSummariesResultTypeDef",
    {
        "ResourceComplianceSummaryItems": List["ResourceComplianceSummaryItemTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListResourceDataSyncResultTypeDef = TypedDict(
    "ListResourceDataSyncResultTypeDef",
    {"ResourceDataSyncItems": List["ResourceDataSyncItemTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef", {"TagList": List["TagTypeDef"]}, total=False
)

MaintenanceWindowFilterTypeDef = TypedDict(
    "MaintenanceWindowFilterTypeDef", {"Key": str, "Values": List[str]}, total=False
)

OpsItemEventFilterTypeDef = TypedDict(
    "OpsItemEventFilterTypeDef",
    {"Key": OpsItemEventFilterKey, "Values": List[str], "Operator": OpsItemEventFilterOperator},
)

OpsItemFilterTypeDef = TypedDict(
    "OpsItemFilterTypeDef",
    {"Key": OpsItemFilterKey, "Values": List[str], "Operator": OpsItemFilterOperator},
)

OpsMetadataFilterTypeDef = TypedDict("OpsMetadataFilterTypeDef", {"Key": str, "Values": List[str]})

OpsResultAttributeTypeDef = TypedDict("OpsResultAttributeTypeDef", {"TypeName": str})

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

_RequiredParameterStringFilterTypeDef = TypedDict(
    "_RequiredParameterStringFilterTypeDef", {"Key": str}
)
_OptionalParameterStringFilterTypeDef = TypedDict(
    "_OptionalParameterStringFilterTypeDef", {"Option": str, "Values": List[str]}, total=False
)


class ParameterStringFilterTypeDef(
    _RequiredParameterStringFilterTypeDef, _OptionalParameterStringFilterTypeDef
):
    pass


ParametersFilterTypeDef = TypedDict(
    "ParametersFilterTypeDef", {"Key": ParametersFilterKey, "Values": List[str]}
)

PatchOrchestratorFilterTypeDef = TypedDict(
    "PatchOrchestratorFilterTypeDef", {"Key": str, "Values": List[str]}, total=False
)

PutInventoryResultTypeDef = TypedDict("PutInventoryResultTypeDef", {"Message": str}, total=False)

PutParameterResultTypeDef = TypedDict(
    "PutParameterResultTypeDef", {"Version": int, "Tier": ParameterTier}, total=False
)

RegisterDefaultPatchBaselineResultTypeDef = TypedDict(
    "RegisterDefaultPatchBaselineResultTypeDef", {"BaselineId": str}, total=False
)

RegisterPatchBaselineForPatchGroupResultTypeDef = TypedDict(
    "RegisterPatchBaselineForPatchGroupResultTypeDef",
    {"BaselineId": str, "PatchGroup": str},
    total=False,
)

RegisterTargetWithMaintenanceWindowResultTypeDef = TypedDict(
    "RegisterTargetWithMaintenanceWindowResultTypeDef", {"WindowTargetId": str}, total=False
)

RegisterTaskWithMaintenanceWindowResultTypeDef = TypedDict(
    "RegisterTaskWithMaintenanceWindowResultTypeDef", {"WindowTaskId": str}, total=False
)

ResetServiceSettingResultTypeDef = TypedDict(
    "ResetServiceSettingResultTypeDef", {"ServiceSetting": "ServiceSettingTypeDef"}, total=False
)

_RequiredResourceDataSyncSourceTypeDef = TypedDict(
    "_RequiredResourceDataSyncSourceTypeDef", {"SourceType": str, "SourceRegions": List[str]}
)
_OptionalResourceDataSyncSourceTypeDef = TypedDict(
    "_OptionalResourceDataSyncSourceTypeDef",
    {
        "AwsOrganizationsSource": "ResourceDataSyncAwsOrganizationsSourceTypeDef",
        "IncludeFutureRegions": bool,
        "EnableAllOpsDataSources": bool,
    },
    total=False,
)


class ResourceDataSyncSourceTypeDef(
    _RequiredResourceDataSyncSourceTypeDef, _OptionalResourceDataSyncSourceTypeDef
):
    pass


ResultAttributeTypeDef = TypedDict("ResultAttributeTypeDef", {"TypeName": str})

ResumeSessionResponseTypeDef = TypedDict(
    "ResumeSessionResponseTypeDef",
    {"SessionId": str, "TokenValue": str, "StreamUrl": str},
    total=False,
)

SendCommandResultTypeDef = TypedDict(
    "SendCommandResultTypeDef", {"Command": "CommandTypeDef"}, total=False
)

SessionFilterTypeDef = TypedDict("SessionFilterTypeDef", {"key": SessionFilterKey, "value": str})

StartAutomationExecutionResultTypeDef = TypedDict(
    "StartAutomationExecutionResultTypeDef", {"AutomationExecutionId": str}, total=False
)

StartChangeRequestExecutionResultTypeDef = TypedDict(
    "StartChangeRequestExecutionResultTypeDef", {"AutomationExecutionId": str}, total=False
)

StartSessionResponseTypeDef = TypedDict(
    "StartSessionResponseTypeDef",
    {"SessionId": str, "TokenValue": str, "StreamUrl": str},
    total=False,
)

StepExecutionFilterTypeDef = TypedDict(
    "StepExecutionFilterTypeDef", {"Key": StepExecutionFilterKey, "Values": List[str]}
)

TerminateSessionResponseTypeDef = TypedDict(
    "TerminateSessionResponseTypeDef", {"SessionId": str}, total=False
)

UnlabelParameterVersionResultTypeDef = TypedDict(
    "UnlabelParameterVersionResultTypeDef",
    {"RemovedLabels": List[str], "InvalidLabels": List[str]},
    total=False,
)

UpdateAssociationResultTypeDef = TypedDict(
    "UpdateAssociationResultTypeDef",
    {"AssociationDescription": "AssociationDescriptionTypeDef"},
    total=False,
)

UpdateAssociationStatusResultTypeDef = TypedDict(
    "UpdateAssociationStatusResultTypeDef",
    {"AssociationDescription": "AssociationDescriptionTypeDef"},
    total=False,
)

UpdateDocumentDefaultVersionResultTypeDef = TypedDict(
    "UpdateDocumentDefaultVersionResultTypeDef",
    {"Description": "DocumentDefaultVersionDescriptionTypeDef"},
    total=False,
)

UpdateDocumentResultTypeDef = TypedDict(
    "UpdateDocumentResultTypeDef",
    {"DocumentDescription": "DocumentDescriptionTypeDef"},
    total=False,
)

UpdateMaintenanceWindowResultTypeDef = TypedDict(
    "UpdateMaintenanceWindowResultTypeDef",
    {
        "WindowId": str,
        "Name": str,
        "Description": str,
        "StartDate": str,
        "EndDate": str,
        "Schedule": str,
        "ScheduleTimezone": str,
        "ScheduleOffset": int,
        "Duration": int,
        "Cutoff": int,
        "AllowUnassociatedTargets": bool,
        "Enabled": bool,
    },
    total=False,
)

UpdateMaintenanceWindowTargetResultTypeDef = TypedDict(
    "UpdateMaintenanceWindowTargetResultTypeDef",
    {
        "WindowId": str,
        "WindowTargetId": str,
        "Targets": List["TargetTypeDef"],
        "OwnerInformation": str,
        "Name": str,
        "Description": str,
    },
    total=False,
)

UpdateMaintenanceWindowTaskResultTypeDef = TypedDict(
    "UpdateMaintenanceWindowTaskResultTypeDef",
    {
        "WindowId": str,
        "WindowTaskId": str,
        "Targets": List["TargetTypeDef"],
        "TaskArn": str,
        "ServiceRoleArn": str,
        "TaskParameters": Dict[str, "MaintenanceWindowTaskParameterValueExpressionTypeDef"],
        "TaskInvocationParameters": "MaintenanceWindowTaskInvocationParametersTypeDef",
        "Priority": int,
        "MaxConcurrency": str,
        "MaxErrors": str,
        "LoggingInfo": "LoggingInfoTypeDef",
        "Name": str,
        "Description": str,
    },
    total=False,
)

UpdateOpsMetadataResultTypeDef = TypedDict(
    "UpdateOpsMetadataResultTypeDef", {"OpsMetadataArn": str}, total=False
)

UpdatePatchBaselineResultTypeDef = TypedDict(
    "UpdatePatchBaselineResultTypeDef",
    {
        "BaselineId": str,
        "Name": str,
        "OperatingSystem": OperatingSystem,
        "GlobalFilters": "PatchFilterGroupTypeDef",
        "ApprovalRules": "PatchRuleGroupTypeDef",
        "ApprovedPatches": List[str],
        "ApprovedPatchesComplianceLevel": PatchComplianceLevel,
        "ApprovedPatchesEnableNonSecurity": bool,
        "RejectedPatches": List[str],
        "RejectedPatchesAction": PatchAction,
        "CreatedDate": datetime,
        "ModifiedDate": datetime,
        "Description": str,
        "Sources": List["PatchSourceTypeDef"],
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
