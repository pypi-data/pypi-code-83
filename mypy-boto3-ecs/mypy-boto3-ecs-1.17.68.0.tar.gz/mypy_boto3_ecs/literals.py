"""
Type annotations for ecs service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/literals.html)

Usage::

    ```python
    from mypy_boto3_ecs.literals import AgentUpdateStatus

    data: AgentUpdateStatus = "FAILED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AgentUpdateStatus",
    "AssignPublicIp",
    "CapacityProviderField",
    "CapacityProviderStatus",
    "CapacityProviderUpdateStatus",
    "ClusterField",
    "ClusterSettingName",
    "Compatibility",
    "Connectivity",
    "ContainerCondition",
    "ContainerInstanceField",
    "ContainerInstanceStatus",
    "DeploymentControllerType",
    "DeploymentRolloutState",
    "DesiredStatus",
    "DeviceCgroupPermission",
    "EFSAuthorizationConfigIAM",
    "EFSTransitEncryption",
    "EnvironmentFileType",
    "ExecuteCommandLogging",
    "FirelensConfigurationType",
    "HealthStatus",
    "IpcMode",
    "LaunchType",
    "ListAccountSettingsPaginatorName",
    "ListAttributesPaginatorName",
    "ListClustersPaginatorName",
    "ListContainerInstancesPaginatorName",
    "ListServicesPaginatorName",
    "ListTaskDefinitionFamiliesPaginatorName",
    "ListTaskDefinitionsPaginatorName",
    "ListTasksPaginatorName",
    "LogDriver",
    "ManagedAgentName",
    "ManagedScalingStatus",
    "ManagedTerminationProtection",
    "NetworkMode",
    "PidMode",
    "PlacementConstraintType",
    "PlacementStrategyType",
    "PlatformDeviceType",
    "PropagateTags",
    "ProxyConfigurationType",
    "ResourceType",
    "ScaleUnit",
    "SchedulingStrategy",
    "Scope",
    "ServiceField",
    "ServicesInactiveWaiterName",
    "ServicesStableWaiterName",
    "SettingName",
    "SortOrder",
    "StabilityStatus",
    "TargetType",
    "TaskDefinitionFamilyStatus",
    "TaskDefinitionField",
    "TaskDefinitionPlacementConstraintType",
    "TaskDefinitionStatus",
    "TaskField",
    "TaskSetField",
    "TaskStopCode",
    "TasksRunningWaiterName",
    "TasksStoppedWaiterName",
    "TransportProtocol",
    "UlimitName",
)


AgentUpdateStatus = Literal["FAILED", "PENDING", "STAGED", "STAGING", "UPDATED", "UPDATING"]
AssignPublicIp = Literal["DISABLED", "ENABLED"]
CapacityProviderField = Literal["TAGS"]
CapacityProviderStatus = Literal["ACTIVE", "INACTIVE"]
CapacityProviderUpdateStatus = Literal[
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "UPDATE_COMPLETE",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
ClusterField = Literal["ATTACHMENTS", "CONFIGURATIONS", "SETTINGS", "STATISTICS", "TAGS"]
ClusterSettingName = Literal["containerInsights"]
Compatibility = Literal["EC2", "FARGATE"]
Connectivity = Literal["CONNECTED", "DISCONNECTED"]
ContainerCondition = Literal["COMPLETE", "HEALTHY", "START", "SUCCESS"]
ContainerInstanceField = Literal["TAGS"]
ContainerInstanceStatus = Literal[
    "ACTIVE", "DEREGISTERING", "DRAINING", "REGISTERING", "REGISTRATION_FAILED"
]
DeploymentControllerType = Literal["CODE_DEPLOY", "ECS", "EXTERNAL"]
DeploymentRolloutState = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
DesiredStatus = Literal["PENDING", "RUNNING", "STOPPED"]
DeviceCgroupPermission = Literal["mknod", "read", "write"]
EFSAuthorizationConfigIAM = Literal["DISABLED", "ENABLED"]
EFSTransitEncryption = Literal["DISABLED", "ENABLED"]
EnvironmentFileType = Literal["s3"]
ExecuteCommandLogging = Literal["DEFAULT", "NONE", "OVERRIDE"]
FirelensConfigurationType = Literal["fluentbit", "fluentd"]
HealthStatus = Literal["HEALTHY", "UNHEALTHY", "UNKNOWN"]
IpcMode = Literal["host", "none", "task"]
LaunchType = Literal["EC2", "FARGATE"]
ListAccountSettingsPaginatorName = Literal["list_account_settings"]
ListAttributesPaginatorName = Literal["list_attributes"]
ListClustersPaginatorName = Literal["list_clusters"]
ListContainerInstancesPaginatorName = Literal["list_container_instances"]
ListServicesPaginatorName = Literal["list_services"]
ListTaskDefinitionFamiliesPaginatorName = Literal["list_task_definition_families"]
ListTaskDefinitionsPaginatorName = Literal["list_task_definitions"]
ListTasksPaginatorName = Literal["list_tasks"]
LogDriver = Literal[
    "awsfirelens", "awslogs", "fluentd", "gelf", "journald", "json-file", "splunk", "syslog"
]
ManagedAgentName = Literal["ExecuteCommandAgent"]
ManagedScalingStatus = Literal["DISABLED", "ENABLED"]
ManagedTerminationProtection = Literal["DISABLED", "ENABLED"]
NetworkMode = Literal["awsvpc", "bridge", "host", "none"]
PidMode = Literal["host", "task"]
PlacementConstraintType = Literal["distinctInstance", "memberOf"]
PlacementStrategyType = Literal["binpack", "random", "spread"]
PlatformDeviceType = Literal["GPU"]
PropagateTags = Literal["SERVICE", "TASK_DEFINITION"]
ProxyConfigurationType = Literal["APPMESH"]
ResourceType = Literal["GPU", "InferenceAccelerator"]
ScaleUnit = Literal["PERCENT"]
SchedulingStrategy = Literal["DAEMON", "REPLICA"]
Scope = Literal["shared", "task"]
ServiceField = Literal["TAGS"]
ServicesInactiveWaiterName = Literal["services_inactive"]
ServicesStableWaiterName = Literal["services_stable"]
SettingName = Literal[
    "awsvpcTrunking",
    "containerInsights",
    "containerInstanceLongArnFormat",
    "serviceLongArnFormat",
    "taskLongArnFormat",
]
SortOrder = Literal["ASC", "DESC"]
StabilityStatus = Literal["STABILIZING", "STEADY_STATE"]
TargetType = Literal["container-instance"]
TaskDefinitionFamilyStatus = Literal["ACTIVE", "ALL", "INACTIVE"]
TaskDefinitionField = Literal["TAGS"]
TaskDefinitionPlacementConstraintType = Literal["memberOf"]
TaskDefinitionStatus = Literal["ACTIVE", "INACTIVE"]
TaskField = Literal["TAGS"]
TaskSetField = Literal["TAGS"]
TaskStopCode = Literal["EssentialContainerExited", "TaskFailedToStart", "UserInitiated"]
TasksRunningWaiterName = Literal["tasks_running"]
TasksStoppedWaiterName = Literal["tasks_stopped"]
TransportProtocol = Literal["tcp", "udp"]
UlimitName = Literal[
    "core",
    "cpu",
    "data",
    "fsize",
    "locks",
    "memlock",
    "msgqueue",
    "nice",
    "nofile",
    "nproc",
    "rss",
    "rtprio",
    "rttime",
    "sigpending",
    "stack",
]
