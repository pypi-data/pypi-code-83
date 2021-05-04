"""
Type annotations for cloudformation service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/literals.html)

Usage::

    ```python
    from mypy_boto3_cloudformation.literals import AccountGateStatus

    data: AccountGateStatus = "FAILED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccountGateStatus",
    "CallAs",
    "Capability",
    "ChangeAction",
    "ChangeSetCreateCompleteWaiterName",
    "ChangeSetStatus",
    "ChangeSetType",
    "ChangeSource",
    "ChangeType",
    "DeprecatedStatus",
    "DescribeAccountLimitsPaginatorName",
    "DescribeChangeSetPaginatorName",
    "DescribeStackEventsPaginatorName",
    "DescribeStacksPaginatorName",
    "DifferenceType",
    "EvaluationType",
    "ExecutionStatus",
    "HandlerErrorCode",
    "ListChangeSetsPaginatorName",
    "ListExportsPaginatorName",
    "ListImportsPaginatorName",
    "ListStackInstancesPaginatorName",
    "ListStackResourcesPaginatorName",
    "ListStackSetOperationResultsPaginatorName",
    "ListStackSetOperationsPaginatorName",
    "ListStackSetsPaginatorName",
    "ListStacksPaginatorName",
    "OnFailure",
    "OperationStatus",
    "PermissionModels",
    "ProvisioningType",
    "RegionConcurrencyType",
    "RegistrationStatus",
    "RegistryType",
    "Replacement",
    "RequiresRecreation",
    "ResourceAttribute",
    "ResourceSignalStatus",
    "ResourceStatus",
    "StackCreateCompleteWaiterName",
    "StackDeleteCompleteWaiterName",
    "StackDriftDetectionStatus",
    "StackDriftStatus",
    "StackExistsWaiterName",
    "StackImportCompleteWaiterName",
    "StackInstanceDetailedStatus",
    "StackInstanceFilterName",
    "StackInstanceStatus",
    "StackResourceDriftStatus",
    "StackRollbackCompleteWaiterName",
    "StackSetDriftDetectionStatus",
    "StackSetDriftStatus",
    "StackSetOperationAction",
    "StackSetOperationResultStatus",
    "StackSetOperationStatus",
    "StackSetStatus",
    "StackStatus",
    "StackUpdateCompleteWaiterName",
    "TemplateStage",
    "TypeRegistrationCompleteWaiterName",
    "Visibility",
)


AccountGateStatus = Literal["FAILED", "SKIPPED", "SUCCEEDED"]
CallAs = Literal["DELEGATED_ADMIN", "SELF"]
Capability = Literal["CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM"]
ChangeAction = Literal["Add", "Dynamic", "Import", "Modify", "Remove"]
ChangeSetCreateCompleteWaiterName = Literal["change_set_create_complete"]
ChangeSetStatus = Literal[
    "CREATE_COMPLETE",
    "CREATE_IN_PROGRESS",
    "CREATE_PENDING",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_PENDING",
    "FAILED",
]
ChangeSetType = Literal["CREATE", "IMPORT", "UPDATE"]
ChangeSource = Literal[
    "Automatic",
    "DirectModification",
    "ParameterReference",
    "ResourceAttribute",
    "ResourceReference",
]
ChangeType = Literal["Resource"]
DeprecatedStatus = Literal["DEPRECATED", "LIVE"]
DescribeAccountLimitsPaginatorName = Literal["describe_account_limits"]
DescribeChangeSetPaginatorName = Literal["describe_change_set"]
DescribeStackEventsPaginatorName = Literal["describe_stack_events"]
DescribeStacksPaginatorName = Literal["describe_stacks"]
DifferenceType = Literal["ADD", "NOT_EQUAL", "REMOVE"]
EvaluationType = Literal["Dynamic", "Static"]
ExecutionStatus = Literal[
    "AVAILABLE",
    "EXECUTE_COMPLETE",
    "EXECUTE_FAILED",
    "EXECUTE_IN_PROGRESS",
    "OBSOLETE",
    "UNAVAILABLE",
]
HandlerErrorCode = Literal[
    "AccessDenied",
    "AlreadyExists",
    "GeneralServiceException",
    "InternalFailure",
    "InvalidCredentials",
    "InvalidRequest",
    "NetworkFailure",
    "NotFound",
    "NotStabilized",
    "NotUpdatable",
    "ResourceConflict",
    "ServiceInternalError",
    "ServiceLimitExceeded",
    "Throttling",
]
ListChangeSetsPaginatorName = Literal["list_change_sets"]
ListExportsPaginatorName = Literal["list_exports"]
ListImportsPaginatorName = Literal["list_imports"]
ListStackInstancesPaginatorName = Literal["list_stack_instances"]
ListStackResourcesPaginatorName = Literal["list_stack_resources"]
ListStackSetOperationResultsPaginatorName = Literal["list_stack_set_operation_results"]
ListStackSetOperationsPaginatorName = Literal["list_stack_set_operations"]
ListStackSetsPaginatorName = Literal["list_stack_sets"]
ListStacksPaginatorName = Literal["list_stacks"]
OnFailure = Literal["DELETE", "DO_NOTHING", "ROLLBACK"]
OperationStatus = Literal["FAILED", "IN_PROGRESS", "PENDING", "SUCCESS"]
PermissionModels = Literal["SELF_MANAGED", "SERVICE_MANAGED"]
ProvisioningType = Literal["FULLY_MUTABLE", "IMMUTABLE", "NON_PROVISIONABLE"]
RegionConcurrencyType = Literal["PARALLEL", "SEQUENTIAL"]
RegistrationStatus = Literal["COMPLETE", "FAILED", "IN_PROGRESS"]
RegistryType = Literal["MODULE", "RESOURCE"]
Replacement = Literal["Conditional", "False", "True"]
RequiresRecreation = Literal["Always", "Conditionally", "Never"]
ResourceAttribute = Literal[
    "CreationPolicy", "DeletionPolicy", "Metadata", "Properties", "Tags", "UpdatePolicy"
]
ResourceSignalStatus = Literal["FAILURE", "SUCCESS"]
ResourceStatus = Literal[
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_SKIPPED",
    "IMPORT_COMPLETE",
    "IMPORT_FAILED",
    "IMPORT_IN_PROGRESS",
    "IMPORT_ROLLBACK_COMPLETE",
    "IMPORT_ROLLBACK_FAILED",
    "IMPORT_ROLLBACK_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
StackCreateCompleteWaiterName = Literal["stack_create_complete"]
StackDeleteCompleteWaiterName = Literal["stack_delete_complete"]
StackDriftDetectionStatus = Literal[
    "DETECTION_COMPLETE", "DETECTION_FAILED", "DETECTION_IN_PROGRESS"
]
StackDriftStatus = Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED", "UNKNOWN"]
StackExistsWaiterName = Literal["stack_exists"]
StackImportCompleteWaiterName = Literal["stack_import_complete"]
StackInstanceDetailedStatus = Literal[
    "CANCELLED", "FAILED", "INOPERABLE", "PENDING", "RUNNING", "SUCCEEDED"
]
StackInstanceFilterName = Literal["DETAILED_STATUS"]
StackInstanceStatus = Literal["CURRENT", "INOPERABLE", "OUTDATED"]
StackResourceDriftStatus = Literal["DELETED", "IN_SYNC", "MODIFIED", "NOT_CHECKED"]
StackRollbackCompleteWaiterName = Literal["stack_rollback_complete"]
StackSetDriftDetectionStatus = Literal[
    "COMPLETED", "FAILED", "IN_PROGRESS", "PARTIAL_SUCCESS", "STOPPED"
]
StackSetDriftStatus = Literal["DRIFTED", "IN_SYNC", "NOT_CHECKED"]
StackSetOperationAction = Literal["CREATE", "DELETE", "DETECT_DRIFT", "UPDATE"]
StackSetOperationResultStatus = Literal["CANCELLED", "FAILED", "PENDING", "RUNNING", "SUCCEEDED"]
StackSetOperationStatus = Literal["FAILED", "QUEUED", "RUNNING", "STOPPED", "STOPPING", "SUCCEEDED"]
StackSetStatus = Literal["ACTIVE", "DELETED"]
StackStatus = Literal[
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "IMPORT_COMPLETE",
    "IMPORT_IN_PROGRESS",
    "IMPORT_ROLLBACK_COMPLETE",
    "IMPORT_ROLLBACK_FAILED",
    "IMPORT_ROLLBACK_IN_PROGRESS",
    "REVIEW_IN_PROGRESS",
    "ROLLBACK_COMPLETE",
    "ROLLBACK_FAILED",
    "ROLLBACK_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_COMPLETE_CLEANUP_IN_PROGRESS",
    "UPDATE_IN_PROGRESS",
    "UPDATE_ROLLBACK_COMPLETE",
    "UPDATE_ROLLBACK_COMPLETE_CLEANUP_IN_PROGRESS",
    "UPDATE_ROLLBACK_FAILED",
    "UPDATE_ROLLBACK_IN_PROGRESS",
]
StackUpdateCompleteWaiterName = Literal["stack_update_complete"]
TemplateStage = Literal["Original", "Processed"]
TypeRegistrationCompleteWaiterName = Literal["type_registration_complete"]
Visibility = Literal["PRIVATE", "PUBLIC"]
