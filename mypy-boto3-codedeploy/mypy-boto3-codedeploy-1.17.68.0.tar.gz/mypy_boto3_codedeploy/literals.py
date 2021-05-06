"""
Type annotations for codedeploy service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codedeploy/literals.html)

Usage::

    ```python
    from mypy_boto3_codedeploy.literals import ApplicationRevisionSortBy

    data: ApplicationRevisionSortBy = "firstUsedTime"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ApplicationRevisionSortBy",
    "AutoRollbackEvent",
    "BundleType",
    "ComputePlatform",
    "DeploymentCreator",
    "DeploymentOption",
    "DeploymentReadyAction",
    "DeploymentStatus",
    "DeploymentSuccessfulWaiterName",
    "DeploymentTargetType",
    "DeploymentType",
    "DeploymentWaitType",
    "EC2TagFilterType",
    "ErrorCode",
    "FileExistsBehavior",
    "GreenFleetProvisioningAction",
    "InstanceAction",
    "InstanceStatus",
    "InstanceType",
    "LifecycleErrorCode",
    "LifecycleEventStatus",
    "ListApplicationRevisionsPaginatorName",
    "ListApplicationsPaginatorName",
    "ListDeploymentConfigsPaginatorName",
    "ListDeploymentGroupsPaginatorName",
    "ListDeploymentInstancesPaginatorName",
    "ListDeploymentTargetsPaginatorName",
    "ListDeploymentsPaginatorName",
    "ListGitHubAccountTokenNamesPaginatorName",
    "ListOnPremisesInstancesPaginatorName",
    "ListStateFilterAction",
    "MinimumHealthyHostsType",
    "OutdatedInstancesStrategy",
    "RegistrationStatus",
    "RevisionLocationType",
    "SortOrder",
    "StopStatus",
    "TagFilterType",
    "TargetFilterName",
    "TargetLabel",
    "TargetStatus",
    "TrafficRoutingType",
    "TriggerEventType",
)


ApplicationRevisionSortBy = Literal["firstUsedTime", "lastUsedTime", "registerTime"]
AutoRollbackEvent = Literal[
    "DEPLOYMENT_FAILURE", "DEPLOYMENT_STOP_ON_ALARM", "DEPLOYMENT_STOP_ON_REQUEST"
]
BundleType = Literal["JSON", "YAML", "tar", "tgz", "zip"]
ComputePlatform = Literal["ECS", "Lambda", "Server"]
DeploymentCreator = Literal[
    "CloudFormation",
    "CloudFormationRollback",
    "CodeDeploy",
    "CodeDeployAutoUpdate",
    "autoscaling",
    "codeDeployRollback",
    "user",
]
DeploymentOption = Literal["WITHOUT_TRAFFIC_CONTROL", "WITH_TRAFFIC_CONTROL"]
DeploymentReadyAction = Literal["CONTINUE_DEPLOYMENT", "STOP_DEPLOYMENT"]
DeploymentStatus = Literal[
    "Baking", "Created", "Failed", "InProgress", "Queued", "Ready", "Stopped", "Succeeded"
]
DeploymentSuccessfulWaiterName = Literal["deployment_successful"]
DeploymentTargetType = Literal[
    "CloudFormationTarget", "ECSTarget", "InstanceTarget", "LambdaTarget"
]
DeploymentType = Literal["BLUE_GREEN", "IN_PLACE"]
DeploymentWaitType = Literal["READY_WAIT", "TERMINATION_WAIT"]
EC2TagFilterType = Literal["KEY_AND_VALUE", "KEY_ONLY", "VALUE_ONLY"]
ErrorCode = Literal[
    "AGENT_ISSUE",
    "ALARM_ACTIVE",
    "APPLICATION_MISSING",
    "AUTOSCALING_VALIDATION_ERROR",
    "AUTO_SCALING_CONFIGURATION",
    "AUTO_SCALING_IAM_ROLE_PERMISSIONS",
    "CLOUDFORMATION_STACK_FAILURE",
    "CODEDEPLOY_RESOURCE_CANNOT_BE_FOUND",
    "CUSTOMER_APPLICATION_UNHEALTHY",
    "DEPLOYMENT_GROUP_MISSING",
    "ECS_UPDATE_ERROR",
    "ELASTIC_LOAD_BALANCING_INVALID",
    "ELB_INVALID_INSTANCE",
    "HEALTH_CONSTRAINTS",
    "HEALTH_CONSTRAINTS_INVALID",
    "HOOK_EXECUTION_FAILURE",
    "IAM_ROLE_MISSING",
    "IAM_ROLE_PERMISSIONS",
    "INTERNAL_ERROR",
    "INVALID_ECS_SERVICE",
    "INVALID_LAMBDA_CONFIGURATION",
    "INVALID_LAMBDA_FUNCTION",
    "INVALID_REVISION",
    "MANUAL_STOP",
    "MISSING_BLUE_GREEN_DEPLOYMENT_CONFIGURATION",
    "MISSING_ELB_INFORMATION",
    "MISSING_GITHUB_TOKEN",
    "NO_EC2_SUBSCRIPTION",
    "NO_INSTANCES",
    "OVER_MAX_INSTANCES",
    "RESOURCE_LIMIT_EXCEEDED",
    "REVISION_MISSING",
    "THROTTLED",
    "TIMEOUT",
]
FileExistsBehavior = Literal["DISALLOW", "OVERWRITE", "RETAIN"]
GreenFleetProvisioningAction = Literal["COPY_AUTO_SCALING_GROUP", "DISCOVER_EXISTING"]
InstanceAction = Literal["KEEP_ALIVE", "TERMINATE"]
InstanceStatus = Literal[
    "Failed", "InProgress", "Pending", "Ready", "Skipped", "Succeeded", "Unknown"
]
InstanceType = Literal["Blue", "Green"]
LifecycleErrorCode = Literal[
    "ScriptFailed",
    "ScriptMissing",
    "ScriptNotExecutable",
    "ScriptTimedOut",
    "Success",
    "UnknownError",
]
LifecycleEventStatus = Literal["Failed", "InProgress", "Pending", "Skipped", "Succeeded", "Unknown"]
ListApplicationRevisionsPaginatorName = Literal["list_application_revisions"]
ListApplicationsPaginatorName = Literal["list_applications"]
ListDeploymentConfigsPaginatorName = Literal["list_deployment_configs"]
ListDeploymentGroupsPaginatorName = Literal["list_deployment_groups"]
ListDeploymentInstancesPaginatorName = Literal["list_deployment_instances"]
ListDeploymentTargetsPaginatorName = Literal["list_deployment_targets"]
ListDeploymentsPaginatorName = Literal["list_deployments"]
ListGitHubAccountTokenNamesPaginatorName = Literal["list_git_hub_account_token_names"]
ListOnPremisesInstancesPaginatorName = Literal["list_on_premises_instances"]
ListStateFilterAction = Literal["exclude", "ignore", "include"]
MinimumHealthyHostsType = Literal["FLEET_PERCENT", "HOST_COUNT"]
OutdatedInstancesStrategy = Literal["IGNORE", "UPDATE"]
RegistrationStatus = Literal["Deregistered", "Registered"]
RevisionLocationType = Literal["AppSpecContent", "GitHub", "S3", "String"]
SortOrder = Literal["ascending", "descending"]
StopStatus = Literal["Pending", "Succeeded"]
TagFilterType = Literal["KEY_AND_VALUE", "KEY_ONLY", "VALUE_ONLY"]
TargetFilterName = Literal["ServerInstanceLabel", "TargetStatus"]
TargetLabel = Literal["Blue", "Green"]
TargetStatus = Literal[
    "Failed", "InProgress", "Pending", "Ready", "Skipped", "Succeeded", "Unknown"
]
TrafficRoutingType = Literal["AllAtOnce", "TimeBasedCanary", "TimeBasedLinear"]
TriggerEventType = Literal[
    "DeploymentFailure",
    "DeploymentReady",
    "DeploymentRollback",
    "DeploymentStart",
    "DeploymentStop",
    "DeploymentSuccess",
    "InstanceFailure",
    "InstanceReady",
    "InstanceStart",
    "InstanceSuccess",
]
