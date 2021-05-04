"""
Type annotations for elasticbeanstalk service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/literals.html)

Usage::

    ```python
    from mypy_boto3_elasticbeanstalk.literals import ActionHistoryStatus

    data: ActionHistoryStatus = "Completed"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActionHistoryStatus",
    "ActionStatus",
    "ActionType",
    "ApplicationVersionStatus",
    "ComputeType",
    "ConfigurationDeploymentStatus",
    "ConfigurationOptionValueType",
    "DescribeApplicationVersionsPaginatorName",
    "DescribeEnvironmentManagedActionHistoryPaginatorName",
    "DescribeEnvironmentsPaginatorName",
    "DescribeEventsPaginatorName",
    "EnvironmentExistsWaiterName",
    "EnvironmentHealth",
    "EnvironmentHealthAttribute",
    "EnvironmentHealthStatus",
    "EnvironmentInfoType",
    "EnvironmentStatus",
    "EnvironmentTerminatedWaiterName",
    "EnvironmentUpdatedWaiterName",
    "EventSeverity",
    "FailureType",
    "InstancesHealthAttribute",
    "ListPlatformVersionsPaginatorName",
    "PlatformStatus",
    "SourceRepository",
    "SourceType",
    "ValidationSeverity",
)


ActionHistoryStatus = Literal["Completed", "Failed", "Unknown"]
ActionStatus = Literal["Pending", "Running", "Scheduled", "Unknown"]
ActionType = Literal["InstanceRefresh", "PlatformUpdate", "Unknown"]
ApplicationVersionStatus = Literal["Building", "Failed", "Processed", "Processing", "Unprocessed"]
ComputeType = Literal["BUILD_GENERAL1_LARGE", "BUILD_GENERAL1_MEDIUM", "BUILD_GENERAL1_SMALL"]
ConfigurationDeploymentStatus = Literal["deployed", "failed", "pending"]
ConfigurationOptionValueType = Literal["List", "Scalar"]
DescribeApplicationVersionsPaginatorName = Literal["describe_application_versions"]
DescribeEnvironmentManagedActionHistoryPaginatorName = Literal[
    "describe_environment_managed_action_history"
]
DescribeEnvironmentsPaginatorName = Literal["describe_environments"]
DescribeEventsPaginatorName = Literal["describe_events"]
EnvironmentExistsWaiterName = Literal["environment_exists"]
EnvironmentHealth = Literal["Green", "Grey", "Red", "Yellow"]
EnvironmentHealthAttribute = Literal[
    "All",
    "ApplicationMetrics",
    "Causes",
    "Color",
    "HealthStatus",
    "InstancesHealth",
    "RefreshedAt",
    "Status",
]
EnvironmentHealthStatus = Literal[
    "Degraded", "Info", "NoData", "Ok", "Pending", "Severe", "Suspended", "Unknown", "Warning"
]
EnvironmentInfoType = Literal["bundle", "tail"]
EnvironmentStatus = Literal[
    "Aborting",
    "Launching",
    "LinkingFrom",
    "LinkingTo",
    "Ready",
    "Terminated",
    "Terminating",
    "Updating",
]
EnvironmentTerminatedWaiterName = Literal["environment_terminated"]
EnvironmentUpdatedWaiterName = Literal["environment_updated"]
EventSeverity = Literal["DEBUG", "ERROR", "FATAL", "INFO", "TRACE", "WARN"]
FailureType = Literal[
    "CancellationFailed",
    "InternalFailure",
    "InvalidEnvironmentState",
    "PermissionsError",
    "RollbackFailed",
    "RollbackSuccessful",
    "UpdateCancelled",
]
InstancesHealthAttribute = Literal[
    "All",
    "ApplicationMetrics",
    "AvailabilityZone",
    "Causes",
    "Color",
    "Deployment",
    "HealthStatus",
    "InstanceType",
    "LaunchedAt",
    "RefreshedAt",
    "System",
]
ListPlatformVersionsPaginatorName = Literal["list_platform_versions"]
PlatformStatus = Literal["Creating", "Deleted", "Deleting", "Failed", "Ready"]
SourceRepository = Literal["CodeCommit", "S3"]
SourceType = Literal["Git", "Zip"]
ValidationSeverity = Literal["error", "warning"]
