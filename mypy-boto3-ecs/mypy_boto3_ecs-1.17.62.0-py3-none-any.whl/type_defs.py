"""
Main interface for ecs service type definitions.

Usage::

    ```python
    from mypy_boto3_ecs.type_defs import AttachmentTypeDef

    data: AttachmentTypeDef = {...}
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
    ClusterSettingName,
    Compatibility,
    Connectivity,
    ContainerCondition,
    DeploymentControllerType,
    DeploymentRolloutState,
    DeviceCgroupPermission,
    EFSAuthorizationConfigIAM,
    EFSTransitEncryption,
    EnvironmentFileType,
    ExecuteCommandLogging,
    FirelensConfigurationType,
    HealthStatus,
    IpcMode,
    LaunchType,
    LogDriver,
    ManagedAgentName,
    ManagedScalingStatus,
    ManagedTerminationProtection,
    NetworkMode,
    PidMode,
    PlacementConstraintType,
    PlacementStrategyType,
    PlatformDeviceType,
    PropagateTags,
    ProxyConfigurationType,
    ResourceType,
    ScaleUnit,
    SchedulingStrategy,
    Scope,
    SettingName,
    StabilityStatus,
    TargetType,
    TaskDefinitionPlacementConstraintType,
    TaskDefinitionStatus,
    TaskStopCode,
    TransportProtocol,
    UlimitName,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttachmentTypeDef",
    "AttributeTypeDef",
    "AutoScalingGroupProviderTypeDef",
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
    "ContainerTypeDef",
    "DeploymentCircuitBreakerTypeDef",
    "DeploymentConfigurationTypeDef",
    "DeploymentControllerTypeDef",
    "DeploymentTypeDef",
    "DeviceTypeDef",
    "DockerVolumeConfigurationTypeDef",
    "EFSAuthorizationConfigTypeDef",
    "EFSVolumeConfigurationTypeDef",
    "EnvironmentFileTypeDef",
    "EphemeralStorageTypeDef",
    "ExecuteCommandConfigurationTypeDef",
    "ExecuteCommandLogConfigurationTypeDef",
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
    "LoadBalancerTypeDef",
    "LogConfigurationTypeDef",
    "ManagedAgentTypeDef",
    "ManagedScalingTypeDef",
    "MountPointTypeDef",
    "NetworkBindingTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkInterfaceTypeDef",
    "PlacementConstraintTypeDef",
    "PlacementStrategyTypeDef",
    "PortMappingTypeDef",
    "ProxyConfigurationTypeDef",
    "RepositoryCredentialsTypeDef",
    "ResourceRequirementTypeDef",
    "ResourceTypeDef",
    "ScaleTypeDef",
    "SecretTypeDef",
    "ServiceEventTypeDef",
    "ServiceRegistryTypeDef",
    "ServiceTypeDef",
    "SessionTypeDef",
    "SettingTypeDef",
    "SystemControlTypeDef",
    "TagTypeDef",
    "TaskDefinitionPlacementConstraintTypeDef",
    "TaskDefinitionTypeDef",
    "TaskOverrideTypeDef",
    "TaskSetTypeDef",
    "TaskTypeDef",
    "TmpfsTypeDef",
    "UlimitTypeDef",
    "VersionInfoTypeDef",
    "VolumeFromTypeDef",
    "VolumeTypeDef",
    "AttachmentStateChangeTypeDef",
    "AutoScalingGroupProviderUpdateTypeDef",
    "ContainerStateChangeTypeDef",
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
    "DeregisterContainerInstanceResponseTypeDef",
    "DeregisterTaskDefinitionResponseTypeDef",
    "DescribeCapacityProvidersResponseTypeDef",
    "DescribeClustersResponseTypeDef",
    "DescribeContainerInstancesResponseTypeDef",
    "DescribeServicesResponseTypeDef",
    "DescribeTaskDefinitionResponseTypeDef",
    "DescribeTaskSetsResponseTypeDef",
    "DescribeTasksResponseTypeDef",
    "DiscoverPollEndpointResponseTypeDef",
    "ExecuteCommandResponseTypeDef",
    "ListAccountSettingsResponseTypeDef",
    "ListAttributesResponseTypeDef",
    "ListClustersResponseTypeDef",
    "ListContainerInstancesResponseTypeDef",
    "ListServicesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTaskDefinitionFamiliesResponseTypeDef",
    "ListTaskDefinitionsResponseTypeDef",
    "ListTasksResponseTypeDef",
    "ManagedAgentStateChangeTypeDef",
    "PaginatorConfigTypeDef",
    "PlatformDeviceTypeDef",
    "PutAccountSettingDefaultResponseTypeDef",
    "PutAccountSettingResponseTypeDef",
    "PutAttributesResponseTypeDef",
    "PutClusterCapacityProvidersResponseTypeDef",
    "RegisterContainerInstanceResponseTypeDef",
    "RegisterTaskDefinitionResponseTypeDef",
    "RunTaskResponseTypeDef",
    "StartTaskResponseTypeDef",
    "StopTaskResponseTypeDef",
    "SubmitAttachmentStateChangesResponseTypeDef",
    "SubmitContainerStateChangeResponseTypeDef",
    "SubmitTaskStateChangeResponseTypeDef",
    "UpdateCapacityProviderResponseTypeDef",
    "UpdateClusterResponseTypeDef",
    "UpdateClusterSettingsResponseTypeDef",
    "UpdateContainerAgentResponseTypeDef",
    "UpdateContainerInstancesStateResponseTypeDef",
    "UpdateServicePrimaryTaskSetResponseTypeDef",
    "UpdateServiceResponseTypeDef",
    "UpdateTaskSetResponseTypeDef",
    "WaiterConfigTypeDef",
)

AttachmentTypeDef = TypedDict(
    "AttachmentTypeDef",
    {"id": str, "type": str, "status": str, "details": List["KeyValuePairTypeDef"]},
    total=False,
)

_RequiredAttributeTypeDef = TypedDict("_RequiredAttributeTypeDef", {"name": str})
_OptionalAttributeTypeDef = TypedDict(
    "_OptionalAttributeTypeDef",
    {"value": str, "targetType": TargetType, "targetId": str},
    total=False,
)


class AttributeTypeDef(_RequiredAttributeTypeDef, _OptionalAttributeTypeDef):
    pass


_RequiredAutoScalingGroupProviderTypeDef = TypedDict(
    "_RequiredAutoScalingGroupProviderTypeDef", {"autoScalingGroupArn": str}
)
_OptionalAutoScalingGroupProviderTypeDef = TypedDict(
    "_OptionalAutoScalingGroupProviderTypeDef",
    {
        "managedScaling": "ManagedScalingTypeDef",
        "managedTerminationProtection": ManagedTerminationProtection,
    },
    total=False,
)


class AutoScalingGroupProviderTypeDef(
    _RequiredAutoScalingGroupProviderTypeDef, _OptionalAutoScalingGroupProviderTypeDef
):
    pass


_RequiredAwsVpcConfigurationTypeDef = TypedDict(
    "_RequiredAwsVpcConfigurationTypeDef", {"subnets": List[str]}
)
_OptionalAwsVpcConfigurationTypeDef = TypedDict(
    "_OptionalAwsVpcConfigurationTypeDef",
    {"securityGroups": List[str], "assignPublicIp": AssignPublicIp},
    total=False,
)


class AwsVpcConfigurationTypeDef(
    _RequiredAwsVpcConfigurationTypeDef, _OptionalAwsVpcConfigurationTypeDef
):
    pass


_RequiredCapacityProviderStrategyItemTypeDef = TypedDict(
    "_RequiredCapacityProviderStrategyItemTypeDef", {"capacityProvider": str}
)
_OptionalCapacityProviderStrategyItemTypeDef = TypedDict(
    "_OptionalCapacityProviderStrategyItemTypeDef", {"weight": int, "base": int}, total=False
)


class CapacityProviderStrategyItemTypeDef(
    _RequiredCapacityProviderStrategyItemTypeDef, _OptionalCapacityProviderStrategyItemTypeDef
):
    pass


CapacityProviderTypeDef = TypedDict(
    "CapacityProviderTypeDef",
    {
        "capacityProviderArn": str,
        "name": str,
        "status": CapacityProviderStatus,
        "autoScalingGroupProvider": "AutoScalingGroupProviderTypeDef",
        "updateStatus": CapacityProviderUpdateStatus,
        "updateStatusReason": str,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

ClusterConfigurationTypeDef = TypedDict(
    "ClusterConfigurationTypeDef",
    {"executeCommandConfiguration": "ExecuteCommandConfigurationTypeDef"},
    total=False,
)

ClusterSettingTypeDef = TypedDict(
    "ClusterSettingTypeDef", {"name": ClusterSettingName, "value": str}, total=False
)

ClusterTypeDef = TypedDict(
    "ClusterTypeDef",
    {
        "clusterArn": str,
        "clusterName": str,
        "configuration": "ClusterConfigurationTypeDef",
        "status": str,
        "registeredContainerInstancesCount": int,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "activeServicesCount": int,
        "statistics": List["KeyValuePairTypeDef"],
        "tags": List["TagTypeDef"],
        "settings": List["ClusterSettingTypeDef"],
        "capacityProviders": List[str],
        "defaultCapacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "attachments": List["AttachmentTypeDef"],
        "attachmentsStatus": str,
    },
    total=False,
)

ContainerDefinitionTypeDef = TypedDict(
    "ContainerDefinitionTypeDef",
    {
        "name": str,
        "image": str,
        "repositoryCredentials": "RepositoryCredentialsTypeDef",
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "links": List[str],
        "portMappings": List["PortMappingTypeDef"],
        "essential": bool,
        "entryPoint": List[str],
        "command": List[str],
        "environment": List["KeyValuePairTypeDef"],
        "environmentFiles": List["EnvironmentFileTypeDef"],
        "mountPoints": List["MountPointTypeDef"],
        "volumesFrom": List["VolumeFromTypeDef"],
        "linuxParameters": "LinuxParametersTypeDef",
        "secrets": List["SecretTypeDef"],
        "dependsOn": List["ContainerDependencyTypeDef"],
        "startTimeout": int,
        "stopTimeout": int,
        "hostname": str,
        "user": str,
        "workingDirectory": str,
        "disableNetworking": bool,
        "privileged": bool,
        "readonlyRootFilesystem": bool,
        "dnsServers": List[str],
        "dnsSearchDomains": List[str],
        "extraHosts": List["HostEntryTypeDef"],
        "dockerSecurityOptions": List[str],
        "interactive": bool,
        "pseudoTerminal": bool,
        "dockerLabels": Dict[str, str],
        "ulimits": List["UlimitTypeDef"],
        "logConfiguration": "LogConfigurationTypeDef",
        "healthCheck": "HealthCheckTypeDef",
        "systemControls": List["SystemControlTypeDef"],
        "resourceRequirements": List["ResourceRequirementTypeDef"],
        "firelensConfiguration": "FirelensConfigurationTypeDef",
    },
    total=False,
)

ContainerDependencyTypeDef = TypedDict(
    "ContainerDependencyTypeDef", {"containerName": str, "condition": ContainerCondition}
)

ContainerInstanceTypeDef = TypedDict(
    "ContainerInstanceTypeDef",
    {
        "containerInstanceArn": str,
        "ec2InstanceId": str,
        "capacityProviderName": str,
        "version": int,
        "versionInfo": "VersionInfoTypeDef",
        "remainingResources": List["ResourceTypeDef"],
        "registeredResources": List["ResourceTypeDef"],
        "status": str,
        "statusReason": str,
        "agentConnected": bool,
        "runningTasksCount": int,
        "pendingTasksCount": int,
        "agentUpdateStatus": AgentUpdateStatus,
        "attributes": List["AttributeTypeDef"],
        "registeredAt": datetime,
        "attachments": List["AttachmentTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

ContainerOverrideTypeDef = TypedDict(
    "ContainerOverrideTypeDef",
    {
        "name": str,
        "command": List[str],
        "environment": List["KeyValuePairTypeDef"],
        "environmentFiles": List["EnvironmentFileTypeDef"],
        "cpu": int,
        "memory": int,
        "memoryReservation": int,
        "resourceRequirements": List["ResourceRequirementTypeDef"],
    },
    total=False,
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "containerArn": str,
        "taskArn": str,
        "name": str,
        "image": str,
        "imageDigest": str,
        "runtimeId": str,
        "lastStatus": str,
        "exitCode": int,
        "reason": str,
        "networkBindings": List["NetworkBindingTypeDef"],
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
        "healthStatus": HealthStatus,
        "managedAgents": List["ManagedAgentTypeDef"],
        "cpu": str,
        "memory": str,
        "memoryReservation": str,
        "gpuIds": List[str],
    },
    total=False,
)

DeploymentCircuitBreakerTypeDef = TypedDict(
    "DeploymentCircuitBreakerTypeDef", {"enable": bool, "rollback": bool}
)

DeploymentConfigurationTypeDef = TypedDict(
    "DeploymentConfigurationTypeDef",
    {
        "deploymentCircuitBreaker": "DeploymentCircuitBreakerTypeDef",
        "maximumPercent": int,
        "minimumHealthyPercent": int,
    },
    total=False,
)

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

_RequiredDeviceTypeDef = TypedDict("_RequiredDeviceTypeDef", {"hostPath": str})
_OptionalDeviceTypeDef = TypedDict(
    "_OptionalDeviceTypeDef",
    {"containerPath": str, "permissions": List[DeviceCgroupPermission]},
    total=False,
)


class DeviceTypeDef(_RequiredDeviceTypeDef, _OptionalDeviceTypeDef):
    pass


DockerVolumeConfigurationTypeDef = TypedDict(
    "DockerVolumeConfigurationTypeDef",
    {
        "scope": Scope,
        "autoprovision": bool,
        "driver": str,
        "driverOpts": Dict[str, str],
        "labels": Dict[str, str],
    },
    total=False,
)

EFSAuthorizationConfigTypeDef = TypedDict(
    "EFSAuthorizationConfigTypeDef",
    {"accessPointId": str, "iam": EFSAuthorizationConfigIAM},
    total=False,
)

_RequiredEFSVolumeConfigurationTypeDef = TypedDict(
    "_RequiredEFSVolumeConfigurationTypeDef", {"fileSystemId": str}
)
_OptionalEFSVolumeConfigurationTypeDef = TypedDict(
    "_OptionalEFSVolumeConfigurationTypeDef",
    {
        "rootDirectory": str,
        "transitEncryption": EFSTransitEncryption,
        "transitEncryptionPort": int,
        "authorizationConfig": "EFSAuthorizationConfigTypeDef",
    },
    total=False,
)


class EFSVolumeConfigurationTypeDef(
    _RequiredEFSVolumeConfigurationTypeDef, _OptionalEFSVolumeConfigurationTypeDef
):
    pass


EnvironmentFileTypeDef = TypedDict(
    "EnvironmentFileTypeDef", {"value": str, "type": EnvironmentFileType}
)

EphemeralStorageTypeDef = TypedDict("EphemeralStorageTypeDef", {"sizeInGiB": int})

ExecuteCommandConfigurationTypeDef = TypedDict(
    "ExecuteCommandConfigurationTypeDef",
    {
        "kmsKeyId": str,
        "logging": ExecuteCommandLogging,
        "logConfiguration": "ExecuteCommandLogConfigurationTypeDef",
    },
    total=False,
)

ExecuteCommandLogConfigurationTypeDef = TypedDict(
    "ExecuteCommandLogConfigurationTypeDef",
    {
        "cloudWatchLogGroupName": str,
        "cloudWatchEncryptionEnabled": bool,
        "s3BucketName": str,
        "s3EncryptionEnabled": bool,
        "s3KeyPrefix": str,
    },
    total=False,
)

FSxWindowsFileServerAuthorizationConfigTypeDef = TypedDict(
    "FSxWindowsFileServerAuthorizationConfigTypeDef", {"credentialsParameter": str, "domain": str}
)

FSxWindowsFileServerVolumeConfigurationTypeDef = TypedDict(
    "FSxWindowsFileServerVolumeConfigurationTypeDef",
    {
        "fileSystemId": str,
        "rootDirectory": str,
        "authorizationConfig": "FSxWindowsFileServerAuthorizationConfigTypeDef",
    },
)

FailureTypeDef = TypedDict(
    "FailureTypeDef", {"arn": str, "reason": str, "detail": str}, total=False
)

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


_RequiredHealthCheckTypeDef = TypedDict("_RequiredHealthCheckTypeDef", {"command": List[str]})
_OptionalHealthCheckTypeDef = TypedDict(
    "_OptionalHealthCheckTypeDef",
    {"interval": int, "timeout": int, "retries": int, "startPeriod": int},
    total=False,
)


class HealthCheckTypeDef(_RequiredHealthCheckTypeDef, _OptionalHealthCheckTypeDef):
    pass


HostEntryTypeDef = TypedDict("HostEntryTypeDef", {"hostname": str, "ipAddress": str})

HostVolumePropertiesTypeDef = TypedDict(
    "HostVolumePropertiesTypeDef", {"sourcePath": str}, total=False
)

InferenceAcceleratorOverrideTypeDef = TypedDict(
    "InferenceAcceleratorOverrideTypeDef", {"deviceName": str, "deviceType": str}, total=False
)

InferenceAcceleratorTypeDef = TypedDict(
    "InferenceAcceleratorTypeDef", {"deviceName": str, "deviceType": str}
)

KernelCapabilitiesTypeDef = TypedDict(
    "KernelCapabilitiesTypeDef", {"add": List[str], "drop": List[str]}, total=False
)

KeyValuePairTypeDef = TypedDict("KeyValuePairTypeDef", {"name": str, "value": str}, total=False)

LinuxParametersTypeDef = TypedDict(
    "LinuxParametersTypeDef",
    {
        "capabilities": "KernelCapabilitiesTypeDef",
        "devices": List["DeviceTypeDef"],
        "initProcessEnabled": bool,
        "sharedMemorySize": int,
        "tmpfs": List["TmpfsTypeDef"],
        "maxSwap": int,
        "swappiness": int,
    },
    total=False,
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {"targetGroupArn": str, "loadBalancerName": str, "containerName": str, "containerPort": int},
    total=False,
)

_RequiredLogConfigurationTypeDef = TypedDict(
    "_RequiredLogConfigurationTypeDef", {"logDriver": LogDriver}
)
_OptionalLogConfigurationTypeDef = TypedDict(
    "_OptionalLogConfigurationTypeDef",
    {"options": Dict[str, str], "secretOptions": List["SecretTypeDef"]},
    total=False,
)


class LogConfigurationTypeDef(_RequiredLogConfigurationTypeDef, _OptionalLogConfigurationTypeDef):
    pass


ManagedAgentTypeDef = TypedDict(
    "ManagedAgentTypeDef",
    {"lastStartedAt": datetime, "name": ManagedAgentName, "reason": str, "lastStatus": str},
    total=False,
)

ManagedScalingTypeDef = TypedDict(
    "ManagedScalingTypeDef",
    {
        "status": ManagedScalingStatus,
        "targetCapacity": int,
        "minimumScalingStepSize": int,
        "maximumScalingStepSize": int,
        "instanceWarmupPeriod": int,
    },
    total=False,
)

MountPointTypeDef = TypedDict(
    "MountPointTypeDef", {"sourceVolume": str, "containerPath": str, "readOnly": bool}, total=False
)

NetworkBindingTypeDef = TypedDict(
    "NetworkBindingTypeDef",
    {"bindIP": str, "containerPort": int, "hostPort": int, "protocol": TransportProtocol},
    total=False,
)

NetworkConfigurationTypeDef = TypedDict(
    "NetworkConfigurationTypeDef",
    {"awsvpcConfiguration": "AwsVpcConfigurationTypeDef"},
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {"attachmentId": str, "privateIpv4Address": str, "ipv6Address": str},
    total=False,
)

PlacementConstraintTypeDef = TypedDict(
    "PlacementConstraintTypeDef", {"type": PlacementConstraintType, "expression": str}, total=False
)

PlacementStrategyTypeDef = TypedDict(
    "PlacementStrategyTypeDef", {"type": PlacementStrategyType, "field": str}, total=False
)

PortMappingTypeDef = TypedDict(
    "PortMappingTypeDef",
    {"containerPort": int, "hostPort": int, "protocol": TransportProtocol},
    total=False,
)

_RequiredProxyConfigurationTypeDef = TypedDict(
    "_RequiredProxyConfigurationTypeDef", {"containerName": str}
)
_OptionalProxyConfigurationTypeDef = TypedDict(
    "_OptionalProxyConfigurationTypeDef",
    {"type": ProxyConfigurationType, "properties": List["KeyValuePairTypeDef"]},
    total=False,
)


class ProxyConfigurationTypeDef(
    _RequiredProxyConfigurationTypeDef, _OptionalProxyConfigurationTypeDef
):
    pass


RepositoryCredentialsTypeDef = TypedDict(
    "RepositoryCredentialsTypeDef", {"credentialsParameter": str}
)

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

ScaleTypeDef = TypedDict("ScaleTypeDef", {"value": float, "unit": ScaleUnit}, total=False)

SecretTypeDef = TypedDict("SecretTypeDef", {"name": str, "valueFrom": str})

ServiceEventTypeDef = TypedDict(
    "ServiceEventTypeDef", {"id": str, "createdAt": datetime, "message": str}, total=False
)

ServiceRegistryTypeDef = TypedDict(
    "ServiceRegistryTypeDef",
    {"registryArn": str, "port": int, "containerName": str, "containerPort": int},
    total=False,
)

ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "serviceArn": str,
        "serviceName": str,
        "clusterArn": str,
        "loadBalancers": List["LoadBalancerTypeDef"],
        "serviceRegistries": List["ServiceRegistryTypeDef"],
        "status": str,
        "desiredCount": int,
        "runningCount": int,
        "pendingCount": int,
        "launchType": LaunchType,
        "capacityProviderStrategy": List["CapacityProviderStrategyItemTypeDef"],
        "platformVersion": str,
        "taskDefinition": str,
        "deploymentConfiguration": "DeploymentConfigurationTypeDef",
        "taskSets": List["TaskSetTypeDef"],
        "deployments": List["DeploymentTypeDef"],
        "roleArn": str,
        "events": List["ServiceEventTypeDef"],
        "createdAt": datetime,
        "placementConstraints": List["PlacementConstraintTypeDef"],
        "placementStrategy": List["PlacementStrategyTypeDef"],
        "networkConfiguration": "NetworkConfigurationTypeDef",
        "healthCheckGracePeriodSeconds": int,
        "schedulingStrategy": SchedulingStrategy,
        "deploymentController": "DeploymentControllerTypeDef",
        "tags": List["TagTypeDef"],
        "createdBy": str,
        "enableECSManagedTags": bool,
        "propagateTags": PropagateTags,
        "enableExecuteCommand": bool,
    },
    total=False,
)

SessionTypeDef = TypedDict(
    "SessionTypeDef", {"sessionId": str, "streamUrl": str, "tokenValue": str}, total=False
)

SettingTypeDef = TypedDict(
    "SettingTypeDef", {"name": SettingName, "value": str, "principalArn": str}, total=False
)

SystemControlTypeDef = TypedDict(
    "SystemControlTypeDef", {"namespace": str, "value": str}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str}, total=False)

TaskDefinitionPlacementConstraintTypeDef = TypedDict(
    "TaskDefinitionPlacementConstraintTypeDef",
    {"type": TaskDefinitionPlacementConstraintType, "expression": str},
    total=False,
)

TaskDefinitionTypeDef = TypedDict(
    "TaskDefinitionTypeDef",
    {
        "taskDefinitionArn": str,
        "containerDefinitions": List["ContainerDefinitionTypeDef"],
        "family": str,
        "taskRoleArn": str,
        "executionRoleArn": str,
        "networkMode": NetworkMode,
        "revision": int,
        "volumes": List["VolumeTypeDef"],
        "status": TaskDefinitionStatus,
        "requiresAttributes": List["AttributeTypeDef"],
        "placementConstraints": List["TaskDefinitionPlacementConstraintTypeDef"],
        "compatibilities": List[Compatibility],
        "requiresCompatibilities": List[Compatibility],
        "cpu": str,
        "memory": str,
        "inferenceAccelerators": List["InferenceAcceleratorTypeDef"],
        "pidMode": PidMode,
        "ipcMode": IpcMode,
        "proxyConfiguration": "ProxyConfigurationTypeDef",
        "registeredAt": datetime,
        "deregisteredAt": datetime,
        "registeredBy": str,
        "ephemeralStorage": "EphemeralStorageTypeDef",
    },
    total=False,
)

TaskOverrideTypeDef = TypedDict(
    "TaskOverrideTypeDef",
    {
        "containerOverrides": List["ContainerOverrideTypeDef"],
        "cpu": str,
        "inferenceAcceleratorOverrides": List["InferenceAcceleratorOverrideTypeDef"],
        "executionRoleArn": str,
        "memory": str,
        "taskRoleArn": str,
        "ephemeralStorage": "EphemeralStorageTypeDef",
    },
    total=False,
)

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

TaskTypeDef = TypedDict(
    "TaskTypeDef",
    {
        "attachments": List["AttachmentTypeDef"],
        "attributes": List["AttributeTypeDef"],
        "availabilityZone": str,
        "capacityProviderName": str,
        "clusterArn": str,
        "connectivity": Connectivity,
        "connectivityAt": datetime,
        "containerInstanceArn": str,
        "containers": List["ContainerTypeDef"],
        "cpu": str,
        "createdAt": datetime,
        "desiredStatus": str,
        "enableExecuteCommand": bool,
        "executionStoppedAt": datetime,
        "group": str,
        "healthStatus": HealthStatus,
        "inferenceAccelerators": List["InferenceAcceleratorTypeDef"],
        "lastStatus": str,
        "launchType": LaunchType,
        "memory": str,
        "overrides": "TaskOverrideTypeDef",
        "platformVersion": str,
        "pullStartedAt": datetime,
        "pullStoppedAt": datetime,
        "startedAt": datetime,
        "startedBy": str,
        "stopCode": TaskStopCode,
        "stoppedAt": datetime,
        "stoppedReason": str,
        "stoppingAt": datetime,
        "tags": List["TagTypeDef"],
        "taskArn": str,
        "taskDefinitionArn": str,
        "version": int,
        "ephemeralStorage": "EphemeralStorageTypeDef",
    },
    total=False,
)

_RequiredTmpfsTypeDef = TypedDict("_RequiredTmpfsTypeDef", {"containerPath": str, "size": int})
_OptionalTmpfsTypeDef = TypedDict("_OptionalTmpfsTypeDef", {"mountOptions": List[str]}, total=False)


class TmpfsTypeDef(_RequiredTmpfsTypeDef, _OptionalTmpfsTypeDef):
    pass


UlimitTypeDef = TypedDict("UlimitTypeDef", {"name": UlimitName, "softLimit": int, "hardLimit": int})

VersionInfoTypeDef = TypedDict(
    "VersionInfoTypeDef", {"agentVersion": str, "agentHash": str, "dockerVersion": str}, total=False
)

VolumeFromTypeDef = TypedDict(
    "VolumeFromTypeDef", {"sourceContainer": str, "readOnly": bool}, total=False
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "name": str,
        "host": "HostVolumePropertiesTypeDef",
        "dockerVolumeConfiguration": "DockerVolumeConfigurationTypeDef",
        "efsVolumeConfiguration": "EFSVolumeConfigurationTypeDef",
        "fsxWindowsFileServerVolumeConfiguration": "FSxWindowsFileServerVolumeConfigurationTypeDef",
    },
    total=False,
)

AttachmentStateChangeTypeDef = TypedDict(
    "AttachmentStateChangeTypeDef", {"attachmentArn": str, "status": str}
)

AutoScalingGroupProviderUpdateTypeDef = TypedDict(
    "AutoScalingGroupProviderUpdateTypeDef",
    {
        "managedScaling": "ManagedScalingTypeDef",
        "managedTerminationProtection": ManagedTerminationProtection,
    },
    total=False,
)

ContainerStateChangeTypeDef = TypedDict(
    "ContainerStateChangeTypeDef",
    {
        "containerName": str,
        "imageDigest": str,
        "runtimeId": str,
        "exitCode": int,
        "networkBindings": List["NetworkBindingTypeDef"],
        "reason": str,
        "status": str,
    },
    total=False,
)

CreateCapacityProviderResponseTypeDef = TypedDict(
    "CreateCapacityProviderResponseTypeDef",
    {"capacityProvider": "CapacityProviderTypeDef"},
    total=False,
)

CreateClusterResponseTypeDef = TypedDict(
    "CreateClusterResponseTypeDef", {"cluster": "ClusterTypeDef"}, total=False
)

CreateServiceResponseTypeDef = TypedDict(
    "CreateServiceResponseTypeDef", {"service": "ServiceTypeDef"}, total=False
)

CreateTaskSetResponseTypeDef = TypedDict(
    "CreateTaskSetResponseTypeDef", {"taskSet": "TaskSetTypeDef"}, total=False
)

DeleteAccountSettingResponseTypeDef = TypedDict(
    "DeleteAccountSettingResponseTypeDef", {"setting": "SettingTypeDef"}, total=False
)

DeleteAttributesResponseTypeDef = TypedDict(
    "DeleteAttributesResponseTypeDef", {"attributes": List["AttributeTypeDef"]}, total=False
)

DeleteCapacityProviderResponseTypeDef = TypedDict(
    "DeleteCapacityProviderResponseTypeDef",
    {"capacityProvider": "CapacityProviderTypeDef"},
    total=False,
)

DeleteClusterResponseTypeDef = TypedDict(
    "DeleteClusterResponseTypeDef", {"cluster": "ClusterTypeDef"}, total=False
)

DeleteServiceResponseTypeDef = TypedDict(
    "DeleteServiceResponseTypeDef", {"service": "ServiceTypeDef"}, total=False
)

DeleteTaskSetResponseTypeDef = TypedDict(
    "DeleteTaskSetResponseTypeDef", {"taskSet": "TaskSetTypeDef"}, total=False
)

DeregisterContainerInstanceResponseTypeDef = TypedDict(
    "DeregisterContainerInstanceResponseTypeDef",
    {"containerInstance": "ContainerInstanceTypeDef"},
    total=False,
)

DeregisterTaskDefinitionResponseTypeDef = TypedDict(
    "DeregisterTaskDefinitionResponseTypeDef",
    {"taskDefinition": "TaskDefinitionTypeDef"},
    total=False,
)

DescribeCapacityProvidersResponseTypeDef = TypedDict(
    "DescribeCapacityProvidersResponseTypeDef",
    {
        "capacityProviders": List["CapacityProviderTypeDef"],
        "failures": List["FailureTypeDef"],
        "nextToken": str,
    },
    total=False,
)

DescribeClustersResponseTypeDef = TypedDict(
    "DescribeClustersResponseTypeDef",
    {"clusters": List["ClusterTypeDef"], "failures": List["FailureTypeDef"]},
    total=False,
)

DescribeContainerInstancesResponseTypeDef = TypedDict(
    "DescribeContainerInstancesResponseTypeDef",
    {"containerInstances": List["ContainerInstanceTypeDef"], "failures": List["FailureTypeDef"]},
    total=False,
)

DescribeServicesResponseTypeDef = TypedDict(
    "DescribeServicesResponseTypeDef",
    {"services": List["ServiceTypeDef"], "failures": List["FailureTypeDef"]},
    total=False,
)

DescribeTaskDefinitionResponseTypeDef = TypedDict(
    "DescribeTaskDefinitionResponseTypeDef",
    {"taskDefinition": "TaskDefinitionTypeDef", "tags": List["TagTypeDef"]},
    total=False,
)

DescribeTaskSetsResponseTypeDef = TypedDict(
    "DescribeTaskSetsResponseTypeDef",
    {"taskSets": List["TaskSetTypeDef"], "failures": List["FailureTypeDef"]},
    total=False,
)

DescribeTasksResponseTypeDef = TypedDict(
    "DescribeTasksResponseTypeDef",
    {"tasks": List["TaskTypeDef"], "failures": List["FailureTypeDef"]},
    total=False,
)

DiscoverPollEndpointResponseTypeDef = TypedDict(
    "DiscoverPollEndpointResponseTypeDef", {"endpoint": str, "telemetryEndpoint": str}, total=False
)

ExecuteCommandResponseTypeDef = TypedDict(
    "ExecuteCommandResponseTypeDef",
    {
        "clusterArn": str,
        "containerArn": str,
        "containerName": str,
        "interactive": bool,
        "session": "SessionTypeDef",
        "taskArn": str,
    },
    total=False,
)

ListAccountSettingsResponseTypeDef = TypedDict(
    "ListAccountSettingsResponseTypeDef",
    {"settings": List["SettingTypeDef"], "nextToken": str},
    total=False,
)

ListAttributesResponseTypeDef = TypedDict(
    "ListAttributesResponseTypeDef",
    {"attributes": List["AttributeTypeDef"], "nextToken": str},
    total=False,
)

ListClustersResponseTypeDef = TypedDict(
    "ListClustersResponseTypeDef", {"clusterArns": List[str], "nextToken": str}, total=False
)

ListContainerInstancesResponseTypeDef = TypedDict(
    "ListContainerInstancesResponseTypeDef",
    {"containerInstanceArns": List[str], "nextToken": str},
    total=False,
)

ListServicesResponseTypeDef = TypedDict(
    "ListServicesResponseTypeDef", {"serviceArns": List[str], "nextToken": str}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": List["TagTypeDef"]}, total=False
)

ListTaskDefinitionFamiliesResponseTypeDef = TypedDict(
    "ListTaskDefinitionFamiliesResponseTypeDef",
    {"families": List[str], "nextToken": str},
    total=False,
)

ListTaskDefinitionsResponseTypeDef = TypedDict(
    "ListTaskDefinitionsResponseTypeDef",
    {"taskDefinitionArns": List[str], "nextToken": str},
    total=False,
)

ListTasksResponseTypeDef = TypedDict(
    "ListTasksResponseTypeDef", {"taskArns": List[str], "nextToken": str}, total=False
)

_RequiredManagedAgentStateChangeTypeDef = TypedDict(
    "_RequiredManagedAgentStateChangeTypeDef",
    {"containerName": str, "managedAgentName": ManagedAgentName, "status": str},
)
_OptionalManagedAgentStateChangeTypeDef = TypedDict(
    "_OptionalManagedAgentStateChangeTypeDef", {"reason": str}, total=False
)


class ManagedAgentStateChangeTypeDef(
    _RequiredManagedAgentStateChangeTypeDef, _OptionalManagedAgentStateChangeTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PlatformDeviceTypeDef = TypedDict("PlatformDeviceTypeDef", {"id": str, "type": PlatformDeviceType})

PutAccountSettingDefaultResponseTypeDef = TypedDict(
    "PutAccountSettingDefaultResponseTypeDef", {"setting": "SettingTypeDef"}, total=False
)

PutAccountSettingResponseTypeDef = TypedDict(
    "PutAccountSettingResponseTypeDef", {"setting": "SettingTypeDef"}, total=False
)

PutAttributesResponseTypeDef = TypedDict(
    "PutAttributesResponseTypeDef", {"attributes": List["AttributeTypeDef"]}, total=False
)

PutClusterCapacityProvidersResponseTypeDef = TypedDict(
    "PutClusterCapacityProvidersResponseTypeDef", {"cluster": "ClusterTypeDef"}, total=False
)

RegisterContainerInstanceResponseTypeDef = TypedDict(
    "RegisterContainerInstanceResponseTypeDef",
    {"containerInstance": "ContainerInstanceTypeDef"},
    total=False,
)

RegisterTaskDefinitionResponseTypeDef = TypedDict(
    "RegisterTaskDefinitionResponseTypeDef",
    {"taskDefinition": "TaskDefinitionTypeDef", "tags": List["TagTypeDef"]},
    total=False,
)

RunTaskResponseTypeDef = TypedDict(
    "RunTaskResponseTypeDef",
    {"tasks": List["TaskTypeDef"], "failures": List["FailureTypeDef"]},
    total=False,
)

StartTaskResponseTypeDef = TypedDict(
    "StartTaskResponseTypeDef",
    {"tasks": List["TaskTypeDef"], "failures": List["FailureTypeDef"]},
    total=False,
)

StopTaskResponseTypeDef = TypedDict("StopTaskResponseTypeDef", {"task": "TaskTypeDef"}, total=False)

SubmitAttachmentStateChangesResponseTypeDef = TypedDict(
    "SubmitAttachmentStateChangesResponseTypeDef", {"acknowledgment": str}, total=False
)

SubmitContainerStateChangeResponseTypeDef = TypedDict(
    "SubmitContainerStateChangeResponseTypeDef", {"acknowledgment": str}, total=False
)

SubmitTaskStateChangeResponseTypeDef = TypedDict(
    "SubmitTaskStateChangeResponseTypeDef", {"acknowledgment": str}, total=False
)

UpdateCapacityProviderResponseTypeDef = TypedDict(
    "UpdateCapacityProviderResponseTypeDef",
    {"capacityProvider": "CapacityProviderTypeDef"},
    total=False,
)

UpdateClusterResponseTypeDef = TypedDict(
    "UpdateClusterResponseTypeDef", {"cluster": "ClusterTypeDef"}, total=False
)

UpdateClusterSettingsResponseTypeDef = TypedDict(
    "UpdateClusterSettingsResponseTypeDef", {"cluster": "ClusterTypeDef"}, total=False
)

UpdateContainerAgentResponseTypeDef = TypedDict(
    "UpdateContainerAgentResponseTypeDef",
    {"containerInstance": "ContainerInstanceTypeDef"},
    total=False,
)

UpdateContainerInstancesStateResponseTypeDef = TypedDict(
    "UpdateContainerInstancesStateResponseTypeDef",
    {"containerInstances": List["ContainerInstanceTypeDef"], "failures": List["FailureTypeDef"]},
    total=False,
)

UpdateServicePrimaryTaskSetResponseTypeDef = TypedDict(
    "UpdateServicePrimaryTaskSetResponseTypeDef", {"taskSet": "TaskSetTypeDef"}, total=False
)

UpdateServiceResponseTypeDef = TypedDict(
    "UpdateServiceResponseTypeDef", {"service": "ServiceTypeDef"}, total=False
)

UpdateTaskSetResponseTypeDef = TypedDict(
    "UpdateTaskSetResponseTypeDef", {"taskSet": "TaskSetTypeDef"}, total=False
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
