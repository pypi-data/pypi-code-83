"""
Type annotations for greengrassv2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrassv2/literals.html)

Usage::

    ```python
    from mypy_boto3_greengrassv2.literals import CloudComponentState

    data: CloudComponentState = "DEPLOYABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CloudComponentState",
    "ComponentDependencyType",
    "ComponentVisibilityScope",
    "CoreDeviceStatus",
    "DeploymentComponentUpdatePolicyAction",
    "DeploymentFailureHandlingPolicy",
    "DeploymentHistoryFilter",
    "DeploymentStatus",
    "EffectiveDeploymentExecutionStatus",
    "InstalledComponentLifecycleState",
    "IoTJobAbortAction",
    "IoTJobExecutionFailureType",
    "LambdaEventSourceType",
    "LambdaFilesystemPermission",
    "LambdaInputPayloadEncodingType",
    "LambdaIsolationMode",
    "ListComponentVersionsPaginatorName",
    "ListComponentsPaginatorName",
    "ListCoreDevicesPaginatorName",
    "ListDeploymentsPaginatorName",
    "ListEffectiveDeploymentsPaginatorName",
    "ListInstalledComponentsPaginatorName",
    "RecipeOutputFormat",
)


CloudComponentState = Literal["DEPLOYABLE", "DEPRECATED", "FAILED", "INITIATED", "REQUESTED"]
ComponentDependencyType = Literal["HARD", "SOFT"]
ComponentVisibilityScope = Literal["PRIVATE", "PUBLIC"]
CoreDeviceStatus = Literal["HEALTHY", "UNHEALTHY"]
DeploymentComponentUpdatePolicyAction = Literal["NOTIFY_COMPONENTS", "SKIP_NOTIFY_COMPONENTS"]
DeploymentFailureHandlingPolicy = Literal["DO_NOTHING", "ROLLBACK"]
DeploymentHistoryFilter = Literal["ALL", "LATEST_ONLY"]
DeploymentStatus = Literal["ACTIVE", "CANCELED", "COMPLETED", "FAILED", "INACTIVE"]
EffectiveDeploymentExecutionStatus = Literal[
    "CANCELED", "COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED", "REJECTED", "TIMED_OUT"
]
InstalledComponentLifecycleState = Literal[
    "BROKEN", "ERRORED", "FINISHED", "INSTALLED", "NEW", "RUNNING", "STARTING", "STOPPING"
]
IoTJobAbortAction = Literal["CANCEL"]
IoTJobExecutionFailureType = Literal["ALL", "FAILED", "REJECTED", "TIMED_OUT"]
LambdaEventSourceType = Literal["IOT_CORE", "PUB_SUB"]
LambdaFilesystemPermission = Literal["ro", "rw"]
LambdaInputPayloadEncodingType = Literal["binary", "json"]
LambdaIsolationMode = Literal["GreengrassContainer", "NoContainer"]
ListComponentVersionsPaginatorName = Literal["list_component_versions"]
ListComponentsPaginatorName = Literal["list_components"]
ListCoreDevicesPaginatorName = Literal["list_core_devices"]
ListDeploymentsPaginatorName = Literal["list_deployments"]
ListEffectiveDeploymentsPaginatorName = Literal["list_effective_deployments"]
ListInstalledComponentsPaginatorName = Literal["list_installed_components"]
RecipeOutputFormat = Literal["JSON", "YAML"]
