"""
Type annotations for ecs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ecs.type_defs import AttachmentStateChangeTypeDef

    data: AttachmentStateChangeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_ecs.literals import (
    AgentUpdateStatus,
    AssignPublicIp,
    CapacityProviderStatus,
    CapacityProviderUpdateStatus,
    Compatibility,
    Connectivity,
    ContainerCondition,
    DeploymentControllerType,
    DeploymentRolloutState,
    DeviceCgroupPermission,
    EFSAuthorizationConfigIAM,
    EFSTransitEncryption,
    ExecuteCommandLogging,
    FirelensConfigurationType,
    HealthStatus,
    IpcMode,
    LaunchType,
    LogDriver,
    ManagedScalingStatus,
    ManagedTerminationProtection,
    NetworkMode,
    PidMode,
    PlacementConstraintType,
    PlacementStrategyType,
    PropagateTags,
    ResourceType,
    SchedulingStrategy,
    Scope,
    SettingName,
    StabilityStatus,
    TaskDefinitionStatus,
    TaskStopCode,
    TransportProtocol,
    UlimitName,
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
    "AttachmentStateChangeTypeDef",
    "AttachmentTypeDef",
    "AttributeTypeDef",
    "AutoScalingGroupProviderTypeDef",
    "AutoScalingGroupProviderUpdateTypeDef",
    "AwsVpcConfigurationTypeDef",
    "CapacityProviderStrategyItemTypeDef",
    "CapacityProviderTypeDef",
    "ClusterConfigurationTypeDef",
    "ClusterSettingTypeDef",
    "ClusterTypeDef",
    "ContainerDefinitionTypeDef",
    "ContainerDependencyTypeDef",
    "ContainerInstanceTypeDef",
    "ContainerOverrideTypeDef",
    "ContainerStateChangeTypeDef",
    "ContainerTypeDef",
    "CreateCapacityProviderResponseTypeDef",
    "CreateClusterResponseTypeDef",
    "CreateServiceResponseTypeDef",
    "CreateTaskSetResponseTypeDef",
    "DeleteAccountSettingResponseTypeDef",
    "DeleteAttributesResponseTypeDef",
    "DeleteCapacityProviderResponseTypeDef",
    "DeleteClusterResponseTypeDef",
    "DeleteServiceResponseTypeDef",
    "DeleteTaskSetResponseTypeDef",
    "DeploymentCircuitBreakerTypeDef",
    "DeploymentConfigurationTypeDef",
    "DeploymentControllerTypeDef",
    "DeploymentTypeDef",
    "DeregisterContainerInstanceResponseTypeDef",
    "DeregisterTaskDefinitionResponseTypeDef",
    "DescribeCapacityProvidersResponseTypeDef",
    "DescribeClustersResponseTypeDef",
    "DescribeContainerInstancesResponseTypeDef",
    "DescribeServicesResponseTypeDef",
    "DescribeTaskDefinitionResponseTypeDef",
    "DescribeTaskSetsResponseTypeDef",
    "DescribeTasksResponseTypeDef",
    "DeviceTypeDef",
    "DiscoverPollEndpointResponseTypeDef",
    "DockerVolumeConfigurationTypeDef",
    "EFSAuthorizationConfigTypeDef",
    "EFSVolumeConfigurationTypeDef",
    "EnvironmentFileTypeDef",
    "EphemeralStorageTypeDef",
    "ExecuteCommandConfigurationTypeDef",
    "ExecuteCommandLogConfigurationTypeDef",
    "ExecuteCommandResponseTypeDef",
    "FSxWindowsFileServerAuthorizationConfigTypeDef",
    "FSxWindowsFileServerVolumeConfigurationTypeDef",
    "FailureTypeDef",
    "FirelensConfigurationTypeDef",
    "HealthCheckTypeDef",
    "HostEntryTypeDef",
    "HostVolumePropertiesTypeDef",
    "InferenceAcceleratorOverrideTypeDef",
    "InferenceAcceleratorTypeDef",
    "KernelCapabilitiesTypeDef",
    "KeyValuePairTypeDef",
    "LinuxParametersTypeDef",
    "ListAccountSettingsResponseTypeDef",
    "ListAttributesResponseTypeDef",
    "ListClustersResponseTypeDef",
    "ListContainerInstancesResponseTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskDefinitionFamiliesResponseTypeDef",
    "ListTaskDefinitionsResponseTypeDef",
    "ListTasksResponseTypeDef",
    "LoadBalancerTypeDef",
    "LogConfigurationTypeDef",
    "ManagedAgentStateChangeTypeDef",
    "ManagedAgentTypeDef",
    "ManagedScalingTypeDef",
    "MountPointTypeDef",
    "NetworkBindingTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "PlatformDeviceTypeDef",
    "PortMappingTypeDef",
    "ProxyConfigurationTypeDef",
    "PutAccountSettingDefaultResponseTypeDef",
    "PutAccountSettingResponseTypeDef",
    "PutAttributesResponseTypeDef",
    "PutClusterCapacityProvidersResponseTypeDef",
    "RegisterContainerInstanceResponseTypeDef",
    "RegisterTaskDefinitionResponseTypeDef",
    "RepositoryCredentialsTypeDef",
    "ResourceRequirementTypeDef",
    "ResourceTypeDef",
    "RunTaskResponseTypeDef",
    "ScaleTypeDef",
    "SecretTypeDef",
    "ServiceEventTypeDef",
    "ServiceRegistryTypeDef",
    "ServiceTypeDef",
    "SessionTypeDef",
    "SettingTypeDef",
    "StartTaskResponseTypeDef",
    "StopTaskResponseTypeDef",
    "SubmitAttachmentStateChangesResponseTypeDef",
    "SubmitContainerStateChangeResponseTypeDef",
    "SubmitTaskStateChangeResponseTypeDef",
    "SystemControlTypeDef",
    "TagTypeDef",
    "TaskDefinitionPlacementConstraintTypeDef",
    "TaskDefinitionTypeDef",
    "TaskOverrideTypeDef",
    "TaskSetTypeDef",
    "TaskTypeDef",
    "TmpfsTypeDef",
    "UlimitTypeDef",
    "UpdateCapacityProviderResponseTypeDef",
    "UpdateClusterResponseTypeDef",
    "UpdateClusterSettingsResponseTypeDef",
    "UpdateContainerAgentResponseTypeDef",
    "UpdateContainerInstancesStateResponseTypeDef",
    "UpdateServicePrimaryTaskSetResponseTypeDef",
    "UpdateServiceResponseTypeDef",
    "UpdateTaskSetResponseTypeDef",
    "VersionInfoTypeDef",
    "VolumeFromTypeDef",
    "VolumeTypeDef",
    "WaiterConfigTypeDef",
)


class AttachmentStateChangeTypeDef(TypedDict):
    attachmentArn: str
    status: str


AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {"id": str, "type": str, "status": str, "details": List["KeyValuePairTypeDef"]},
    total=False,
)


class _RequiredAttributeTypeDef(TypedDict):
    name: str


class AttributeTypeDef(_RequiredAttributeTypeDef, total=False):
    value: str
    targetType: Literal["container-instance"]
    targetId: str


class _RequiredAutoScalingGroupProviderTypeDef(TypedDict):
    autoScalingGroupArn: str


class AutoScalingGroupProviderTypeDef(_RequiredAutoScalingGroupProviderTypeDef, total=False):
    managedScaling: "ManagedScalingTypeDef"
    managedTerminationProtection: ManagedTerminationProtection


class AutoScalingGroupProviderUpdateTypeDef(TypedDict, total=False):
    managedScaling: "ManagedScalingTypeDef"
    managedTerminationProtection: ManagedTerminationProtection


class _RequiredAwsVpcConfigurationTypeDef(TypedDict):
    subnets: List[str]


class AwsVpcConfigurationTypeDef(_RequiredAwsVpcConfigurationTypeDef, total=False):
    securityGroups: List[str]
    assignPublicIp: AssignPublicIp


class _RequiredCapacityProviderStrategyItemTypeDef(TypedDict):
    capacityProvider: str


class CapacityProviderStrategyItemTypeDef(
    _RequiredCapacityProviderStrategyItemTypeDef, total=False
):
    weight: int
    base: int


class CapacityProviderTypeDef(TypedDict, total=False):
    capacityProviderArn: str
    name: str
    status: CapacityProviderStatus
    autoScalingGroupProvider: "AutoScalingGroupProviderTypeDef"
    updateStatus: CapacityProviderUpdateStatus
    updateStatusReason: str
    tags: List["TagTypeDef"]


class ClusterConfigurationTypeDef(TypedDict, total=False):
    executeCommandConfiguration: "ExecuteCommandConfigurationTypeDef"


class ClusterSettingTypeDef(TypedDict, total=False):
    name: Literal["containerInsights"]
    value: str


class ClusterTypeDef(TypedDict, total=False):
    clusterArn: str
    clusterName: str
    configuration: "ClusterConfigurationTypeDef"
    status: str
    registeredContainerInstancesCount: int
    runningTasksCount: int
    pendingTasksCount: int
    activeServicesCount: int
    statistics: List["KeyValuePairTypeDef"]
    tags: List["TagTypeDef"]
    settings: List["ClusterSettingTypeDef"]
    capacityProviders: List[str]
    defaultCapacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"]
    attachments: List["AttachmentTypeDef"]
    attachmentsStatus: str


class ContainerDefinitionTypeDef(TypedDict, total=False):
    name: str
    image: str
    repositoryCredentials: "RepositoryCredentialsTypeDef"
    cpu: int
    memory: int
    memoryReservation: int
    links: List[str]
    portMappings: List["PortMappingTypeDef"]
    essential: bool
    entryPoint: List[str]
    command: List[str]
    environment: List["KeyValuePairTypeDef"]
    environmentFiles: List["EnvironmentFileTypeDef"]
    mountPoints: List["MountPointTypeDef"]
    volumesFrom: List["VolumeFromTypeDef"]
    linuxParameters: "LinuxParametersTypeDef"
    secrets: List["SecretTypeDef"]
    dependsOn: List["ContainerDependencyTypeDef"]
    startTimeout: int
    stopTimeout: int
    hostname: str
    user: str
    workingDirectory: str
    disableNetworking: bool
    privileged: bool
    readonlyRootFilesystem: bool
    dnsServers: List[str]
    dnsSearchDomains: List[str]
    extraHosts: List["HostEntryTypeDef"]
    dockerSecurityOptions: List[str]
    interactive: bool
    pseudoTerminal: bool
    dockerLabels: Dict[str, str]
    ulimits: List["UlimitTypeDef"]
    logConfiguration: "LogConfigurationTypeDef"
    healthCheck: "HealthCheckTypeDef"
    systemControls: List["SystemControlTypeDef"]
    resourceRequirements: List["ResourceRequirementTypeDef"]
    firelensConfiguration: "FirelensConfigurationTypeDef"


class ContainerDependencyTypeDef(TypedDict):
    containerName: str
    condition: ContainerCondition


class ContainerInstanceTypeDef(TypedDict, total=False):
    containerInstanceArn: str
    ec2InstanceId: str
    capacityProviderName: str
    version: int
    versionInfo: "VersionInfoTypeDef"
    remainingResources: List["ResourceTypeDef"]
    registeredResources: List["ResourceTypeDef"]
    status: str
    statusReason: str
    agentConnected: bool
    runningTasksCount: int
    pendingTasksCount: int
    agentUpdateStatus: AgentUpdateStatus
    attributes: List["AttributeTypeDef"]
    registeredAt: datetime
    attachments: List["AttachmentTypeDef"]
    tags: List["TagTypeDef"]


class ContainerOverrideTypeDef(TypedDict, total=False):
    name: str
    command: List[str]
    environment: List["KeyValuePairTypeDef"]
    environmentFiles: List["EnvironmentFileTypeDef"]
    cpu: int
    memory: int
    memoryReservation: int
    resourceRequirements: List["ResourceRequirementTypeDef"]


class ContainerStateChangeTypeDef(TypedDict, total=False):
    containerName: str
    imageDigest: str
    runtimeId: str
    exitCode: int
    networkBindings: List["NetworkBindingTypeDef"]
    reason: str
    status: str


class ContainerTypeDef(TypedDict, total=False):
    containerArn: str
    taskArn: str
    name: str
    image: str
    imageDigest: str
    runtimeId: str
    lastStatus: str
    exitCode: int
    reason: str
    networkBindings: List["NetworkBindingTypeDef"]
    networkInterfaces: List["NetworkInterfaceTypeDef"]
    healthStatus: HealthStatus
    managedAgents: List["ManagedAgentTypeDef"]
    cpu: str
    memory: str
    memoryReservation: str
    gpuIds: List[str]


class CreateCapacityProviderResponseTypeDef(TypedDict, total=False):
    capacityProvider: "CapacityProviderTypeDef"


class CreateClusterResponseTypeDef(TypedDict, total=False):
    cluster: "ClusterTypeDef"


class CreateServiceResponseTypeDef(TypedDict, total=False):
    service: "ServiceTypeDef"


class CreateTaskSetResponseTypeDef(TypedDict, total=False):
    taskSet: "TaskSetTypeDef"


class DeleteAccountSettingResponseTypeDef(TypedDict, total=False):
    setting: "SettingTypeDef"


class DeleteAttributesResponseTypeDef(TypedDict, total=False):
    attributes: List["AttributeTypeDef"]


class DeleteCapacityProviderResponseTypeDef(TypedDict, total=False):
    capacityProvider: "CapacityProviderTypeDef"


class DeleteClusterResponseTypeDef(TypedDict, total=False):
    cluster: "ClusterTypeDef"


class DeleteServiceResponseTypeDef(TypedDict, total=False):
    service: "ServiceTypeDef"


class DeleteTaskSetResponseTypeDef(TypedDict, total=False):
    taskSet: "TaskSetTypeDef"


class DeploymentCircuitBreakerTypeDef(TypedDict):
    enable: bool
    rollback: bool


class DeploymentConfigurationTypeDef(TypedDict, total=False):
    deploymentCircuitBreaker: "DeploymentCircuitBreakerTypeDef"
    maximumPercent: int
    minimumHealthyPercent: int


DeploymentControllerTypeDef = TypedDict(
    "DeploymentControllerTypeDef", {"type": DeploymentControllerType}
)

DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "id": str,
        "status": str,
        "taskDefinition": str,
        "desiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "failedTasks": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "launchType": LaunchType,
        "platformVersion": str,
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "rolloutState": DeploymentRolloutState,
        "rolloutStateReason": str,
    },
    total=False,
)


class DeregisterContainerInstanceResponseTypeDef(TypedDict, total=False):
    containerInstance: "ContainerInstanceTypeDef"


class DeregisterTaskDefinitionResponseTypeDef(TypedDict, total=False):
    taskDefinition: "TaskDefinitionTypeDef"


class DescribeCapacityProvidersResponseTypeDef(TypedDict, total=False):
    capacityProviders: List["CapacityProviderTypeDef"]
    failures: List["FailureTypeDef"]
    nextToken: str


class DescribeClustersResponseTypeDef(TypedDict, total=False):
    clusters: List["ClusterTypeDef"]
    failures: List["FailureTypeDef"]


class DescribeContainerInstancesResponseTypeDef(TypedDict, total=False):
    containerInstances: List["ContainerInstanceTypeDef"]
    failures: List["FailureTypeDef"]


class DescribeServicesResponseTypeDef(TypedDict, total=False):
    services: List["ServiceTypeDef"]
    failures: List["FailureTypeDef"]


class DescribeTaskDefinitionResponseTypeDef(TypedDict, total=False):
    taskDefinition: "TaskDefinitionTypeDef"
    tags: List["TagTypeDef"]


class DescribeTaskSetsResponseTypeDef(TypedDict, total=False):
    taskSets: List["TaskSetTypeDef"]
    failures: List["FailureTypeDef"]


class DescribeTasksResponseTypeDef(TypedDict, total=False):
    tasks: List["TaskTypeDef"]
    failures: List["FailureTypeDef"]


class _RequiredDeviceTypeDef(TypedDict):
    hostPath: str


class DeviceTypeDef(_RequiredDeviceTypeDef, total=False):
    containerPath: str
    permissions: List[DeviceCgroupPermission]


class DiscoverPollEndpointResponseTypeDef(TypedDict, total=False):
    endpoint: str
    telemetryEndpoint: str


class DockerVolumeConfigurationTypeDef(TypedDict, total=False):
    scope: Scope
    autoprovision: bool
    driver: str
    driverOpts: Dict[str, str]
    labels: Dict[str, str]


class EFSAuthorizationConfigTypeDef(TypedDict, total=False):
    accessPointId: str
    iam: EFSAuthorizationConfigIAM


class _RequiredEFSVolumeConfigurationTypeDef(TypedDict):
    fileSystemId: str


class EFSVolumeConfigurationTypeDef(_RequiredEFSVolumeConfigurationTypeDef, total=False):
    rootDirectory: str
    transitEncryption: EFSTransitEncryption
    transitEncryptionPort: int
    authorizationConfig: "EFSAuthorizationConfigTypeDef"


EnvironmentFileTypeDef = TypedDict("EnvironmentFileTypeDef", {"value": str, "type": Literal["s3"]})


class EphemeralStorageTypeDef(TypedDict):
    sizeInGiB: int


class ExecuteCommandConfigurationTypeDef(TypedDict, total=False):
    kmsKeyId: str
    logging: ExecuteCommandLogging
    logConfiguration: "ExecuteCommandLogConfigurationTypeDef"


class ExecuteCommandLogConfigurationTypeDef(TypedDict, total=False):
    cloudWatchLogGroupName: str
    cloudWatchEncryptionEnabled: bool
    s3BucketName: str
    s3EncryptionEnabled: bool
    s3KeyPrefix: str


class ExecuteCommandResponseTypeDef(TypedDict, total=False):
    clusterArn: str
    containerArn: str
    containerName: str
    interactive: bool
    session: "SessionTypeDef"
    taskArn: str


class FSxWindowsFileServerAuthorizationConfigTypeDef(TypedDict):
    credentialsParameter: str
    domain: str


class FSxWindowsFileServerVolumeConfigurationTypeDef(TypedDict):
    fileSystemId: str
    rootDirectory: str
    authorizationConfig: "FSxWindowsFileServerAuthorizationConfigTypeDef"


class FailureTypeDef(TypedDict, total=False):
    arn: str
    reason: str
    detail: str


_RequiredFirelensConfigurationTypeDef = TypedDict(
    "_RequiredFirelensConfigurationTypeDef", {"type": FirelensConfigurationType}
)
_OptionalFirelensConfigurationTypeDef = TypedDict(
    "_OptionalFirelensConfigurationTypeDef", {"options": Dict[str, str]}, total=False
)


class FirelensConfigurationTypeDef(
    _RequiredFirelensConfigurationTypeDef, _OptionalFirelensConfigurationTypeDef
):
    pass


class _RequiredHealthCheckTypeDef(TypedDict):
    command: List[str]


class HealthCheckTypeDef(_RequiredHealthCheckTypeDef, total=False):
    interval: int
    timeout: int
    retries: int
    startPeriod: int


class HostEntryTypeDef(TypedDict):
    hostname: str
    ipAddress: str


class HostVolumePropertiesTypeDef(TypedDict, total=False):
    sourcePath: str


class InferenceAcceleratorOverrideTypeDef(TypedDict, total=False):
    deviceName: str
    deviceType: str


class InferenceAcceleratorTypeDef(TypedDict):
    deviceName: str
    deviceType: str


class KernelCapabilitiesTypeDef(TypedDict, total=False):
    add: List[str]
    drop: List[str]


class KeyValuePairTypeDef(TypedDict, total=False):
    name: str
    value: str


class LinuxParametersTypeDef(TypedDict, total=False):
    capabilities: "KernelCapabilitiesTypeDef"
    devices: List["DeviceTypeDef"]
    initProcessEnabled: bool
    sharedMemorySize: int
    tmpfs: List["TmpfsTypeDef"]
    maxSwap: int
    swappiness: int


class ListAccountSettingsResponseTypeDef(TypedDict, total=False):
    settings: List["SettingTypeDef"]
    nextToken: str


class ListAttributesResponseTypeDef(TypedDict, total=False):
    attributes: List["AttributeTypeDef"]
    nextToken: str


class ListClustersResponseTypeDef(TypedDict, total=False):
    clusterArns: List[str]
    nextToken: str


class ListContainerInstancesResponseTypeDef(TypedDict, total=False):
    containerInstanceArns: List[str]
    nextToken: str


class ListServicesResponseTypeDef(TypedDict, total=False):
    serviceArns: List[str]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: List["TagTypeDef"]


class ListTaskDefinitionFamiliesResponseTypeDef(TypedDict, total=False):
    families: List[str]
    nextToken: str


class ListTaskDefinitionsResponseTypeDef(TypedDict, total=False):
    taskDefinitionArns: List[str]
    nextToken: str


class ListTasksResponseTypeDef(TypedDict, total=False):
    taskArns: List[str]
    nextToken: str


class LoadBalancerTypeDef(TypedDict, total=False):
    targetGroupArn: str
    loadBalancerName: str
    containerName: str
    containerPort: int


class _RequiredLogConfigurationTypeDef(TypedDict):
    logDriver: LogDriver


class LogConfigurationTypeDef(_RequiredLogConfigurationTypeDef, total=False):
    options: Dict[str, str]
    secretOptions: List["SecretTypeDef"]


class _RequiredManagedAgentStateChangeTypeDef(TypedDict):
    containerName: str
    managedAgentName: Literal["ExecuteCommandAgent"]
    status: str


class ManagedAgentStateChangeTypeDef(_RequiredManagedAgentStateChangeTypeDef, total=False):
    reason: str


class ManagedAgentTypeDef(TypedDict, total=False):
    lastStartedAt: datetime
    name: Literal["ExecuteCommandAgent"]
    reason: str
    lastStatus: str


class ManagedScalingTypeDef(TypedDict, total=False):
    status: ManagedScalingStatus
    targetCapacity: int
    minimumScalingStepSize: int
    maximumScalingStepSize: int
    instanceWarmupPeriod: int


class MountPointTypeDef(TypedDict, total=False):
    sourceVolume: str
    containerPath: str
    readOnly: bool


class NetworkBindingTypeDef(TypedDict, total=False):
    bindIP: str
    containerPort: int
    hostPort: int
    protocol: TransportProtocol


class NetworkConfigurationTypeDef(TypedDict, total=False):
    awsvpcConfiguration: "AwsVpcConfigurationTypeDef"


class NetworkInterfaceTypeDef(TypedDict, total=False):
    attachmentId: str
    privateIpv4Address: str
    ipv6Address: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef", {"type": PlacementConstraintType, "expression": str}, total=False
)

PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef", {"type": PlacementStrategyType, "field": str}, total=False
)

PlatformDeviceTypeDef = TypedDict("PlatformDeviceTypeDef", {"id": str, "type": Literal["GPU"]})


class PortMappingTypeDef(TypedDict, total=False):
    containerPort: int
    hostPort: int
    protocol: TransportProtocol


_RequiredProxyConfigurationTypeDef = TypedDict(
    "_RequiredProxyConfigurationTypeDef", {"containerName": str}
)
_OptionalProxyConfigurationTypeDef = TypedDict(
    "_OptionalProxyConfigurationTypeDef",
    {"type": Literal["APPMESH"], "properties": List["KeyValuePairTypeDef"]},
    total=False,
)


class ProxyConfigurationTypeDef(
    _RequiredProxyConfigurationTypeDef, _OptionalProxyConfigurationTypeDef
):
    pass


class PutAccountSettingDefaultResponseTypeDef(TypedDict, total=False):
    setting: "SettingTypeDef"


class PutAccountSettingResponseTypeDef(TypedDict, total=False):
    setting: "SettingTypeDef"


class PutAttributesResponseTypeDef(TypedDict, total=False):
    attributes: List["AttributeTypeDef"]


class PutClusterCapacityProvidersResponseTypeDef(TypedDict, total=False):
    cluster: "ClusterTypeDef"


class RegisterContainerInstanceResponseTypeDef(TypedDict, total=False):
    containerInstance: "ContainerInstanceTypeDef"


class RegisterTaskDefinitionResponseTypeDef(TypedDict, total=False):
    taskDefinition: "TaskDefinitionTypeDef"
    tags: List["TagTypeDef"]


class RepositoryCredentialsTypeDef(TypedDict):
    credentialsParameter: str


ResourceRequirementTypeDef = TypedDict(
    "ResourceRequirementTypeDef", {"value": str, "type": ResourceType}
)

ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "name": str,
        "type": str,
        "doubleValue": float,
        "longValue": int,
        "integerValue": int,
        "stringSetValue": List[str],
    },
    total=False,
)


class RunTaskResponseTypeDef(TypedDict, total=False):
    tasks: List["TaskTypeDef"]
    failures: List["FailureTypeDef"]


class ScaleTypeDef(TypedDict, total=False):
    value: float
    unit: Literal["PERCENT"]


class SecretTypeDef(TypedDict):
    name: str
    valueFrom: str


ServiceEventTypeDef = TypedDict(
    "ServiceEventTypeDef", {"id": str, "createdAt": datetime, "message": str}, total=False
)


class ServiceRegistryTypeDef(TypedDict, total=False):
    registryArn: str
    port: int
    containerName: str
    containerPort: int


class ServiceTypeDef(TypedDict, total=False):
    serviceArn: str
    serviceName: str
    clusterArn: str
    loadBalancers: List["LoadBalancerTypeDef"]
    serviceRegistries: List["ServiceRegistryTypeDef"]
    status: str
    desiredCount: int
    runningCount: int
    pendingCount: int
    launchType: LaunchType
    capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"]
    platformVersion: str
    taskDefinition: str
    deploymentConfiguration: "DeploymentConfigurationTypeDef"
    taskSets: List["TaskSetTypeDef"]
    deployments: List["DeploymentTypeDef"]
    roleArn: str
    events: List["ServiceEventTypeDef"]
    createdAt: datetime
    placementConstraints: List["PlacementConstraintTypeDef"]
    placementStrategy: List["PlacementStrategyTypeDef"]
    networkConfiguration: "NetworkConfigurationTypeDef"
    healthCheckGracePeriodSeconds: int
    schedulingStrategy: SchedulingStrategy
    deploymentController: "DeploymentControllerTypeDef"
    tags: List["TagTypeDef"]
    createdBy: str
    enableECSManagedTags: bool
    propagateTags: PropagateTags
    enableExecuteCommand: bool


class SessionTypeDef(TypedDict, total=False):
    sessionId: str
    streamUrl: str
    tokenValue: str


class SettingTypeDef(TypedDict, total=False):
    name: SettingName
    value: str
    principalArn: str


class StartTaskResponseTypeDef(TypedDict, total=False):
    tasks: List["TaskTypeDef"]
    failures: List["FailureTypeDef"]


class StopTaskResponseTypeDef(TypedDict, total=False):
    task: "TaskTypeDef"


class SubmitAttachmentStateChangesResponseTypeDef(TypedDict, total=False):
    acknowledgment: str


class SubmitContainerStateChangeResponseTypeDef(TypedDict, total=False):
    acknowledgment: str


class SubmitTaskStateChangeResponseTypeDef(TypedDict, total=False):
    acknowledgment: str


class SystemControlTypeDef(TypedDict, total=False):
    namespace: str
    value: str


class TagTypeDef(TypedDict, total=False):
    key: str
    value: str


TaskDefinitionPlacementConstraintTypeDef = TypedDict(
    "TaskDefinitionPlacementConstraintTypeDef",
    {"type": Literal["memberOf"], "expression": str},
    total=False,
)


class TaskDefinitionTypeDef(TypedDict, total=False):
    taskDefinitionArn: str
    containerDefinitions: List["ContainerDefinitionTypeDef"]
    family: str
    taskRoleArn: str
    executionRoleArn: str
    networkMode: NetworkMode
    revision: int
    volumes: List["VolumeTypeDef"]
    status: TaskDefinitionStatus
    requiresAttributes: List["AttributeTypeDef"]
    placementConstraints: List["TaskDefinitionPlacementConstraintTypeDef"]
    compatibilities: List[Compatibility]
    requiresCompatibilities: List[Compatibility]
    cpu: str
    memory: str
    inferenceAccelerators: List["InferenceAcceleratorTypeDef"]
    pidMode: PidMode
    ipcMode: IpcMode
    proxyConfiguration: "ProxyConfigurationTypeDef"
    registeredAt: datetime
    deregisteredAt: datetime
    registeredBy: str
    ephemeralStorage: "EphemeralStorageTypeDef"


class TaskOverrideTypeDef(TypedDict, total=False):
    containerOverrides: List["ContainerOverrideTypeDef"]
    cpu: str
    inferenceAcceleratorOverrides: List["InferenceAcceleratorOverrideTypeDef"]
    executionRoleArn: str
    memory: str
    taskRoleArn: str
    ephemeralStorage: "EphemeralStorageTypeDef"


TaskSetTypeDef = TypedDict(
    "TaskSetTypeDef",
    {
        "id": str,
        "taskSetArn": str,
        "serviceArn": str,
        "clusterArn": str,
        "startedBy": str,
        "externalId": str,
        "status": str,
        "taskDefinition": str,
        "computedDesiredCount": int,
        "pendingCount": int,
        "runningCount": int,
        "createdAt": datetime,
        "updatedAt": datetime,
        "launchType": LaunchType,
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "platformVersion": str,
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "loadBalancers": List["LoadBalancerTypeDef"],
        "serviceRegistries": List["ServiceRegistryTypeDef"],
        "scale": "ScaleTypeDef",
        "stabilityStatus": StabilityStatus,
        "stabilityStatusAt": datetime,
        "tags": List["TagTypeDef"],
    },
    total=False,
)


class TaskTypeDef(TypedDict, total=False):
    attachments: List["AttachmentTypeDef"]
    attributes: List["AttributeTypeDef"]
    availabilityZone: str
    capacityProviderName: str
    clusterArn: str
    connectivity: Connectivity
    connectivityAt: datetime
    containerInstanceArn: str
    containers: List["ContainerTypeDef"]
    cpu: str
    createdAt: datetime
    desiredStatus: str
    enableExecuteCommand: bool
    executionStoppedAt: datetime
    group: str
    healthStatus: HealthStatus
    inferenceAccelerators: List["InferenceAcceleratorTypeDef"]
    lastStatus: str
    launchType: LaunchType
    memory: str
    overrides: "TaskOverrideTypeDef"
    platformVersion: str
    pullStartedAt: datetime
    pullStoppedAt: datetime
    startedAt: datetime
    startedBy: str
    stopCode: TaskStopCode
    stoppedAt: datetime
    stoppedReason: str
    stoppingAt: datetime
    tags: List["TagTypeDef"]
    taskArn: str
    taskDefinitionArn: str
    version: int
    ephemeralStorage: "EphemeralStorageTypeDef"


class _RequiredTmpfsTypeDef(TypedDict):
    containerPath: str
    size: int


class TmpfsTypeDef(_RequiredTmpfsTypeDef, total=False):
    mountOptions: List[str]


class UlimitTypeDef(TypedDict):
    name: UlimitName
    softLimit: int
    hardLimit: int


class UpdateCapacityProviderResponseTypeDef(TypedDict, total=False):
    capacityProvider: "CapacityProviderTypeDef"


class UpdateClusterResponseTypeDef(TypedDict, total=False):
    cluster: "ClusterTypeDef"


class UpdateClusterSettingsResponseTypeDef(TypedDict, total=False):
    cluster: "ClusterTypeDef"


class UpdateContainerAgentResponseTypeDef(TypedDict, total=False):
    containerInstance: "ContainerInstanceTypeDef"


class UpdateContainerInstancesStateResponseTypeDef(TypedDict, total=False):
    containerInstances: List["ContainerInstanceTypeDef"]
    failures: List["FailureTypeDef"]


class UpdateServicePrimaryTaskSetResponseTypeDef(TypedDict, total=False):
    taskSet: "TaskSetTypeDef"


class UpdateServiceResponseTypeDef(TypedDict, total=False):
    service: "ServiceTypeDef"


class UpdateTaskSetResponseTypeDef(TypedDict, total=False):
    taskSet: "TaskSetTypeDef"


class VersionInfoTypeDef(TypedDict, total=False):
    agentVersion: str
    agentHash: str
    dockerVersion: str


class VolumeFromTypeDef(TypedDict, total=False):
    sourceContainer: str
    readOnly: bool


class VolumeTypeDef(TypedDict, total=False):
    name: str
    host: "HostVolumePropertiesTypeDef"
    dockerVolumeConfiguration: "DockerVolumeConfigurationTypeDef"
    efsVolumeConfiguration: "EFSVolumeConfigurationTypeDef"
    fsxWindowsFileServerVolumeConfiguration: "FSxWindowsFileServerVolumeConfigurationTypeDef"


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
