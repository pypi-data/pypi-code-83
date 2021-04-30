"""
Main interface for ssm service literal definitions.

Usage::

    ```python
    from mypy_boto3_ssm.literals import AssociationComplianceSeverity

    data: AssociationComplianceSeverity = "CRITICAL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AssociationComplianceSeverity",
    "AssociationExecutionFilterKey",
    "AssociationExecutionTargetsFilterKey",
    "AssociationFilterKey",
    "AssociationFilterOperatorType",
    "AssociationStatusName",
    "AssociationSyncCompliance",
    "AttachmentHashType",
    "AttachmentsSourceKey",
    "AutomationExecutionFilterKey",
    "AutomationExecutionStatus",
    "AutomationSubtype",
    "AutomationType",
    "CalendarState",
    "CommandExecutedWaiterName",
    "CommandFilterKey",
    "CommandInvocationStatus",
    "CommandPluginStatus",
    "CommandStatus",
    "ComplianceQueryOperatorType",
    "ComplianceSeverity",
    "ComplianceStatus",
    "ComplianceUploadType",
    "ConnectionStatus",
    "DescribeActivationsFilterKeys",
    "DescribeActivationsPaginatorName",
    "DescribeAssociationExecutionTargetsPaginatorName",
    "DescribeAssociationExecutionsPaginatorName",
    "DescribeAutomationExecutionsPaginatorName",
    "DescribeAutomationStepExecutionsPaginatorName",
    "DescribeAvailablePatchesPaginatorName",
    "DescribeEffectiveInstanceAssociationsPaginatorName",
    "DescribeEffectivePatchesForPatchBaselinePaginatorName",
    "DescribeInstanceAssociationsStatusPaginatorName",
    "DescribeInstanceInformationPaginatorName",
    "DescribeInstancePatchStatesForPatchGroupPaginatorName",
    "DescribeInstancePatchStatesPaginatorName",
    "DescribeInstancePatchesPaginatorName",
    "DescribeInventoryDeletionsPaginatorName",
    "DescribeMaintenanceWindowExecutionTaskInvocationsPaginatorName",
    "DescribeMaintenanceWindowExecutionTasksPaginatorName",
    "DescribeMaintenanceWindowExecutionsPaginatorName",
    "DescribeMaintenanceWindowSchedulePaginatorName",
    "DescribeMaintenanceWindowTargetsPaginatorName",
    "DescribeMaintenanceWindowTasksPaginatorName",
    "DescribeMaintenanceWindowsForTargetPaginatorName",
    "DescribeMaintenanceWindowsPaginatorName",
    "DescribeOpsItemsPaginatorName",
    "DescribeParametersPaginatorName",
    "DescribePatchBaselinesPaginatorName",
    "DescribePatchGroupsPaginatorName",
    "DescribePatchPropertiesPaginatorName",
    "DescribeSessionsPaginatorName",
    "DocumentFilterKey",
    "DocumentFormat",
    "DocumentHashType",
    "DocumentMetadataEnum",
    "DocumentParameterType",
    "DocumentPermissionType",
    "DocumentReviewAction",
    "DocumentReviewCommentType",
    "DocumentStatus",
    "DocumentType",
    "ExecutionMode",
    "Fault",
    "GetInventoryPaginatorName",
    "GetInventorySchemaPaginatorName",
    "GetOpsSummaryPaginatorName",
    "GetParameterHistoryPaginatorName",
    "GetParametersByPathPaginatorName",
    "InstanceInformationFilterKey",
    "InstancePatchStateOperatorType",
    "InventoryAttributeDataType",
    "InventoryDeletionStatus",
    "InventoryQueryOperatorType",
    "InventorySchemaDeleteOption",
    "LastResourceDataSyncStatus",
    "ListAssociationVersionsPaginatorName",
    "ListAssociationsPaginatorName",
    "ListCommandInvocationsPaginatorName",
    "ListCommandsPaginatorName",
    "ListComplianceItemsPaginatorName",
    "ListComplianceSummariesPaginatorName",
    "ListDocumentVersionsPaginatorName",
    "ListDocumentsPaginatorName",
    "ListOpsItemEventsPaginatorName",
    "ListOpsMetadataPaginatorName",
    "ListResourceComplianceSummariesPaginatorName",
    "ListResourceDataSyncPaginatorName",
    "MaintenanceWindowExecutionStatus",
    "MaintenanceWindowResourceType",
    "MaintenanceWindowTaskType",
    "NotificationEvent",
    "NotificationType",
    "OperatingSystem",
    "OpsFilterOperatorType",
    "OpsItemDataType",
    "OpsItemEventFilterKey",
    "OpsItemEventFilterOperator",
    "OpsItemFilterKey",
    "OpsItemFilterOperator",
    "OpsItemStatus",
    "ParameterTier",
    "ParameterType",
    "ParametersFilterKey",
    "PatchAction",
    "PatchComplianceDataState",
    "PatchComplianceLevel",
    "PatchDeploymentStatus",
    "PatchFilterKey",
    "PatchOperationType",
    "PatchProperty",
    "PatchSet",
    "PingStatus",
    "PlatformType",
    "RebootOption",
    "ResourceDataSyncS3Format",
    "ResourceType",
    "ResourceTypeForTagging",
    "ReviewStatus",
    "SessionFilterKey",
    "SessionState",
    "SessionStatus",
    "SignalType",
    "StepExecutionFilterKey",
    "StopType",
)


AssociationComplianceSeverity = Literal["CRITICAL", "HIGH", "LOW", "MEDIUM", "UNSPECIFIED"]
AssociationExecutionFilterKey = Literal["CreatedTime", "ExecutionId", "Status"]
AssociationExecutionTargetsFilterKey = Literal["ResourceId", "ResourceType", "Status"]
AssociationFilterKey = Literal[
    "AssociationId",
    "AssociationName",
    "AssociationStatusName",
    "InstanceId",
    "LastExecutedAfter",
    "LastExecutedBefore",
    "Name",
    "ResourceGroupName",
]
AssociationFilterOperatorType = Literal["EQUAL", "GREATER_THAN", "LESS_THAN"]
AssociationStatusName = Literal["Failed", "Pending", "Success"]
AssociationSyncCompliance = Literal["AUTO", "MANUAL"]
AttachmentHashType = Literal["Sha256"]
AttachmentsSourceKey = Literal["AttachmentReference", "S3FileUrl", "SourceUrl"]
AutomationExecutionFilterKey = Literal[
    "AutomationSubtype",
    "AutomationType",
    "CurrentAction",
    "DocumentNamePrefix",
    "ExecutionId",
    "ExecutionStatus",
    "OpsItemId",
    "ParentExecutionId",
    "StartTimeAfter",
    "StartTimeBefore",
    "TagKey",
    "TargetResourceGroup",
]
AutomationExecutionStatus = Literal[
    "Approved",
    "Cancelled",
    "Cancelling",
    "ChangeCalendarOverrideApproved",
    "ChangeCalendarOverrideRejected",
    "CompletedWithFailure",
    "CompletedWithSuccess",
    "Failed",
    "InProgress",
    "Pending",
    "PendingApproval",
    "PendingChangeCalendarOverride",
    "Rejected",
    "RunbookInProgress",
    "Scheduled",
    "Success",
    "TimedOut",
    "Waiting",
]
AutomationSubtype = Literal["ChangeRequest"]
AutomationType = Literal["CrossAccount", "Local"]
CalendarState = Literal["CLOSED", "OPEN"]
CommandExecutedWaiterName = Literal["command_executed"]
CommandFilterKey = Literal[
    "DocumentName", "ExecutionStage", "InvokedAfter", "InvokedBefore", "Status"
]
CommandInvocationStatus = Literal[
    "Cancelled", "Cancelling", "Delayed", "Failed", "InProgress", "Pending", "Success", "TimedOut"
]
CommandPluginStatus = Literal["Cancelled", "Failed", "InProgress", "Pending", "Success", "TimedOut"]
CommandStatus = Literal[
    "Cancelled", "Cancelling", "Failed", "InProgress", "Pending", "Success", "TimedOut"
]
ComplianceQueryOperatorType = Literal[
    "BEGIN_WITH", "EQUAL", "GREATER_THAN", "LESS_THAN", "NOT_EQUAL"
]
ComplianceSeverity = Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"]
ComplianceStatus = Literal["COMPLIANT", "NON_COMPLIANT"]
ComplianceUploadType = Literal["COMPLETE", "PARTIAL"]
ConnectionStatus = Literal["Connected", "NotConnected"]
DescribeActivationsFilterKeys = Literal["ActivationIds", "DefaultInstanceName", "IamRole"]
DescribeActivationsPaginatorName = Literal["describe_activations"]
DescribeAssociationExecutionTargetsPaginatorName = Literal["describe_association_execution_targets"]
DescribeAssociationExecutionsPaginatorName = Literal["describe_association_executions"]
DescribeAutomationExecutionsPaginatorName = Literal["describe_automation_executions"]
DescribeAutomationStepExecutionsPaginatorName = Literal["describe_automation_step_executions"]
DescribeAvailablePatchesPaginatorName = Literal["describe_available_patches"]
DescribeEffectiveInstanceAssociationsPaginatorName = Literal[
    "describe_effective_instance_associations"
]
DescribeEffectivePatchesForPatchBaselinePaginatorName = Literal[
    "describe_effective_patches_for_patch_baseline"
]
DescribeInstanceAssociationsStatusPaginatorName = Literal["describe_instance_associations_status"]
DescribeInstanceInformationPaginatorName = Literal["describe_instance_information"]
DescribeInstancePatchStatesForPatchGroupPaginatorName = Literal[
    "describe_instance_patch_states_for_patch_group"
]
DescribeInstancePatchStatesPaginatorName = Literal["describe_instance_patch_states"]
DescribeInstancePatchesPaginatorName = Literal["describe_instance_patches"]
DescribeInventoryDeletionsPaginatorName = Literal["describe_inventory_deletions"]
DescribeMaintenanceWindowExecutionTaskInvocationsPaginatorName = Literal[
    "describe_maintenance_window_execution_task_invocations"
]
DescribeMaintenanceWindowExecutionTasksPaginatorName = Literal[
    "describe_maintenance_window_execution_tasks"
]
DescribeMaintenanceWindowExecutionsPaginatorName = Literal["describe_maintenance_window_executions"]
DescribeMaintenanceWindowSchedulePaginatorName = Literal["describe_maintenance_window_schedule"]
DescribeMaintenanceWindowTargetsPaginatorName = Literal["describe_maintenance_window_targets"]
DescribeMaintenanceWindowTasksPaginatorName = Literal["describe_maintenance_window_tasks"]
DescribeMaintenanceWindowsForTargetPaginatorName = Literal[
    "describe_maintenance_windows_for_target"
]
DescribeMaintenanceWindowsPaginatorName = Literal["describe_maintenance_windows"]
DescribeOpsItemsPaginatorName = Literal["describe_ops_items"]
DescribeParametersPaginatorName = Literal["describe_parameters"]
DescribePatchBaselinesPaginatorName = Literal["describe_patch_baselines"]
DescribePatchGroupsPaginatorName = Literal["describe_patch_groups"]
DescribePatchPropertiesPaginatorName = Literal["describe_patch_properties"]
DescribeSessionsPaginatorName = Literal["describe_sessions"]
DocumentFilterKey = Literal["DocumentType", "Name", "Owner", "PlatformTypes"]
DocumentFormat = Literal["JSON", "TEXT", "YAML"]
DocumentHashType = Literal["Sha1", "Sha256"]
DocumentMetadataEnum = Literal["DocumentReviews"]
DocumentParameterType = Literal["String", "StringList"]
DocumentPermissionType = Literal["Share"]
DocumentReviewAction = Literal["Approve", "Reject", "SendForReview", "UpdateReview"]
DocumentReviewCommentType = Literal["Comment"]
DocumentStatus = Literal["Active", "Creating", "Deleting", "Failed", "Updating"]
DocumentType = Literal[
    "ApplicationConfiguration",
    "ApplicationConfigurationSchema",
    "Automation",
    "Automation.ChangeTemplate",
    "ChangeCalendar",
    "Command",
    "DeploymentStrategy",
    "Package",
    "Policy",
    "Session",
]
ExecutionMode = Literal["Auto", "Interactive"]
Fault = Literal["Client", "Server", "Unknown"]
GetInventoryPaginatorName = Literal["get_inventory"]
GetInventorySchemaPaginatorName = Literal["get_inventory_schema"]
GetOpsSummaryPaginatorName = Literal["get_ops_summary"]
GetParameterHistoryPaginatorName = Literal["get_parameter_history"]
GetParametersByPathPaginatorName = Literal["get_parameters_by_path"]
InstanceInformationFilterKey = Literal[
    "ActivationIds",
    "AgentVersion",
    "AssociationStatus",
    "IamRole",
    "InstanceIds",
    "PingStatus",
    "PlatformTypes",
    "ResourceType",
]
InstancePatchStateOperatorType = Literal["Equal", "GreaterThan", "LessThan", "NotEqual"]
InventoryAttributeDataType = Literal["number", "string"]
InventoryDeletionStatus = Literal["Complete", "InProgress"]
InventoryQueryOperatorType = Literal[
    "BeginWith", "Equal", "Exists", "GreaterThan", "LessThan", "NotEqual"
]
InventorySchemaDeleteOption = Literal["DeleteSchema", "DisableSchema"]
LastResourceDataSyncStatus = Literal["Failed", "InProgress", "Successful"]
ListAssociationVersionsPaginatorName = Literal["list_association_versions"]
ListAssociationsPaginatorName = Literal["list_associations"]
ListCommandInvocationsPaginatorName = Literal["list_command_invocations"]
ListCommandsPaginatorName = Literal["list_commands"]
ListComplianceItemsPaginatorName = Literal["list_compliance_items"]
ListComplianceSummariesPaginatorName = Literal["list_compliance_summaries"]
ListDocumentVersionsPaginatorName = Literal["list_document_versions"]
ListDocumentsPaginatorName = Literal["list_documents"]
ListOpsItemEventsPaginatorName = Literal["list_ops_item_events"]
ListOpsMetadataPaginatorName = Literal["list_ops_metadata"]
ListResourceComplianceSummariesPaginatorName = Literal["list_resource_compliance_summaries"]
ListResourceDataSyncPaginatorName = Literal["list_resource_data_sync"]
MaintenanceWindowExecutionStatus = Literal[
    "CANCELLED",
    "CANCELLING",
    "FAILED",
    "IN_PROGRESS",
    "PENDING",
    "SKIPPED_OVERLAPPING",
    "SUCCESS",
    "TIMED_OUT",
]
MaintenanceWindowResourceType = Literal["INSTANCE", "RESOURCE_GROUP"]
MaintenanceWindowTaskType = Literal["AUTOMATION", "LAMBDA", "RUN_COMMAND", "STEP_FUNCTIONS"]
NotificationEvent = Literal["All", "Cancelled", "Failed", "InProgress", "Success", "TimedOut"]
NotificationType = Literal["Command", "Invocation"]
OperatingSystem = Literal[
    "AMAZON_LINUX",
    "AMAZON_LINUX_2",
    "CENTOS",
    "DEBIAN",
    "MACOS",
    "ORACLE_LINUX",
    "REDHAT_ENTERPRISE_LINUX",
    "SUSE",
    "UBUNTU",
    "WINDOWS",
]
OpsFilterOperatorType = Literal[
    "BeginWith", "Equal", "Exists", "GreaterThan", "LessThan", "NotEqual"
]
OpsItemDataType = Literal["SearchableString", "String"]
OpsItemEventFilterKey = Literal["OpsItemId"]
OpsItemEventFilterOperator = Literal["Equal"]
OpsItemFilterKey = Literal[
    "ActualEndTime",
    "ActualStartTime",
    "AutomationId",
    "Category",
    "ChangeRequestByApproverArn",
    "ChangeRequestByApproverName",
    "ChangeRequestByRequesterArn",
    "ChangeRequestByRequesterName",
    "ChangeRequestByTargetsResourceGroup",
    "ChangeRequestByTemplate",
    "CreatedBy",
    "CreatedTime",
    "LastModifiedTime",
    "OperationalData",
    "OperationalDataKey",
    "OperationalDataValue",
    "OpsItemId",
    "OpsItemType",
    "PlannedEndTime",
    "PlannedStartTime",
    "Priority",
    "ResourceId",
    "Severity",
    "Source",
    "Status",
    "Title",
]
OpsItemFilterOperator = Literal["Contains", "Equal", "GreaterThan", "LessThan"]
OpsItemStatus = Literal[
    "Approved",
    "Cancelled",
    "Cancelling",
    "ChangeCalendarOverrideApproved",
    "ChangeCalendarOverrideRejected",
    "CompletedWithFailure",
    "CompletedWithSuccess",
    "Failed",
    "InProgress",
    "Open",
    "Pending",
    "PendingApproval",
    "PendingChangeCalendarOverride",
    "Rejected",
    "Resolved",
    "RunbookInProgress",
    "Scheduled",
    "TimedOut",
]
ParameterTier = Literal["Advanced", "Intelligent-Tiering", "Standard"]
ParameterType = Literal["SecureString", "String", "StringList"]
ParametersFilterKey = Literal["KeyId", "Name", "Type"]
PatchAction = Literal["ALLOW_AS_DEPENDENCY", "BLOCK"]
PatchComplianceDataState = Literal[
    "FAILED",
    "INSTALLED",
    "INSTALLED_OTHER",
    "INSTALLED_PENDING_REBOOT",
    "INSTALLED_REJECTED",
    "MISSING",
    "NOT_APPLICABLE",
]
PatchComplianceLevel = Literal["CRITICAL", "HIGH", "INFORMATIONAL", "LOW", "MEDIUM", "UNSPECIFIED"]
PatchDeploymentStatus = Literal[
    "APPROVED", "EXPLICIT_APPROVED", "EXPLICIT_REJECTED", "PENDING_APPROVAL"
]
PatchFilterKey = Literal[
    "ADVISORY_ID",
    "ARCH",
    "BUGZILLA_ID",
    "CLASSIFICATION",
    "CVE_ID",
    "EPOCH",
    "MSRC_SEVERITY",
    "NAME",
    "PATCH_ID",
    "PATCH_SET",
    "PRIORITY",
    "PRODUCT",
    "PRODUCT_FAMILY",
    "RELEASE",
    "REPOSITORY",
    "SECTION",
    "SECURITY",
    "SEVERITY",
    "VERSION",
]
PatchOperationType = Literal["Install", "Scan"]
PatchProperty = Literal[
    "CLASSIFICATION", "MSRC_SEVERITY", "PRIORITY", "PRODUCT", "PRODUCT_FAMILY", "SEVERITY"
]
PatchSet = Literal["APPLICATION", "OS"]
PingStatus = Literal["ConnectionLost", "Inactive", "Online"]
PlatformType = Literal["Linux", "Windows"]
RebootOption = Literal["NoReboot", "RebootIfNeeded"]
ResourceDataSyncS3Format = Literal["JsonSerDe"]
ResourceType = Literal["Document", "EC2Instance", "ManagedInstance"]
ResourceTypeForTagging = Literal[
    "Document",
    "MaintenanceWindow",
    "ManagedInstance",
    "OpsItem",
    "OpsMetadata",
    "Parameter",
    "PatchBaseline",
]
ReviewStatus = Literal["APPROVED", "NOT_REVIEWED", "PENDING", "REJECTED"]
SessionFilterKey = Literal[
    "InvokedAfter", "InvokedBefore", "Owner", "SessionId", "Status", "Target"
]
SessionState = Literal["Active", "History"]
SessionStatus = Literal[
    "Connected", "Connecting", "Disconnected", "Failed", "Terminated", "Terminating"
]
SignalType = Literal["Approve", "Reject", "Resume", "StartStep", "StopStep"]
StepExecutionFilterKey = Literal[
    "Action",
    "StartTimeAfter",
    "StartTimeBefore",
    "StepExecutionId",
    "StepExecutionStatus",
    "StepName",
]
StopType = Literal["Cancel", "Complete"]
