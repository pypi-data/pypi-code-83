"""
Type annotations for batch service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/type_defs.html)

Usage::

    ```python
    from mypy_boto3_batch.type_defs import ArrayPropertiesDetailTypeDef

    data: ArrayPropertiesDetailTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_batch.literals import (
    ArrayJobDependency,
    AssignPublicIp,
    CEState,
    CEStatus,
    CEType,
    CRAllocationStrategy,
    CRType,
    DeviceCgroupPermission,
    EFSAuthorizationConfigIAM,
    EFSTransitEncryption,
    JobStatus,
    JQState,
    JQStatus,
    LogDriver,
    PlatformCapability,
    ResourceType,
    RetryAction,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArrayPropertiesDetailTypeDef",
    "ArrayPropertiesSummaryTypeDef",
    "ArrayPropertiesTypeDef",
    "AttemptContainerDetailTypeDef",
    "AttemptDetailTypeDef",
    "ComputeEnvironmentDetailTypeDef",
    "ComputeEnvironmentOrderTypeDef",
    "ComputeResourceTypeDef",
    "ComputeResourceUpdateTypeDef",
    "ContainerDetailTypeDef",
    "ContainerOverridesTypeDef",
    "ContainerPropertiesTypeDef",
    "ContainerSummaryTypeDef",
    "CreateComputeEnvironmentResponseTypeDef",
    "CreateJobQueueResponseTypeDef",
    "DescribeComputeEnvironmentsResponseTypeDef",
    "DescribeJobDefinitionsResponseTypeDef",
    "DescribeJobQueuesResponseTypeDef",
    "DescribeJobsResponseTypeDef",
    "DeviceTypeDef",
    "EFSAuthorizationConfigTypeDef",
    "EFSVolumeConfigurationTypeDef",
    "Ec2ConfigurationTypeDef",
    "EvaluateOnExitTypeDef",
    "FargatePlatformConfigurationTypeDef",
    "HostTypeDef",
    "JobDefinitionTypeDef",
    "JobDependencyTypeDef",
    "JobDetailTypeDef",
    "JobQueueDetailTypeDef",
    "JobSummaryTypeDef",
    "JobTimeoutTypeDef",
    "KeyValuePairTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LinuxParametersTypeDef",
    "ListJobsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogConfigurationTypeDef",
    "MountPointTypeDef",
    "NetworkConfigurationTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeDetailsTypeDef",
    "NodeOverridesTypeDef",
    "NodePropertiesSummaryTypeDef",
    "NodePropertiesTypeDef",
    "NodePropertyOverrideTypeDef",
    "NodeRangePropertyTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterJobDefinitionResponseTypeDef",
    "ResourceRequirementTypeDef",
    "RetryStrategyTypeDef",
    "SecretTypeDef",
    "SubmitJobResponseTypeDef",
    "TmpfsTypeDef",
    "UlimitTypeDef",
    "UpdateComputeEnvironmentResponseTypeDef",
    "UpdateJobQueueResponseTypeDef",
    "VolumeTypeDef",
)


class ArrayPropertiesDetailTypeDef(TypedDict, total=False):
    statusSummary: Dict[str, int]
    size: int
    index: int


class ArrayPropertiesSummaryTypeDef(TypedDict, total=False):
    size: int
    index: int


class ArrayPropertiesTypeDef(TypedDict, total=False):
    size: int


class AttemptContainerDetailTypeDef(TypedDict, total=False):
    containerInstanceArn: str
    taskArn: str
    exitCode: int
    reason: str
    logStreamName: str
    networkInterfaces: List["NetworkInterfaceTypeDef"]


class AttemptDetailTypeDef(TypedDict, total=False):
    container: "AttemptContainerDetailTypeDef"
    startedAt: int
    stoppedAt: int
    statusReason: str


_RequiredComputeEnvironmentDetailTypeDef = TypedDict(
    "_RequiredComputeEnvironmentDetailTypeDef",
    {"computeEnvironmentName": str, "computeEnvironmentArn": str, "ecsClusterArn": str},
)
_OptionalComputeEnvironmentDetailTypeDef = TypedDict(
    "_OptionalComputeEnvironmentDetailTypeDef",
    {
        "tags": Dict[str, str],
        "type": CEType,
        "state": CEState,
        "status": CEStatus,
        "statusReason": str,
        "computeResources": "ComputeResourceTypeDef",
        "serviceRole": str,
    },
    total=False,
)


class ComputeEnvironmentDetailTypeDef(
    _RequiredComputeEnvironmentDetailTypeDef, _OptionalComputeEnvironmentDetailTypeDef
):
    pass


class ComputeEnvironmentOrderTypeDef(TypedDict):
    order: int
    computeEnvironment: str


_RequiredComputeResourceTypeDef = TypedDict(
    "_RequiredComputeResourceTypeDef", {"type": CRType, "maxvCpus": int, "subnets": List[str]}
)
_OptionalComputeResourceTypeDef = TypedDict(
    "_OptionalComputeResourceTypeDef",
    {
        "allocationStrategy": CRAllocationStrategy,
        "minvCpus": int,
        "desiredvCpus": int,
        "instanceTypes": List[str],
        "imageId": str,
        "securityGroupIds": List[str],
        "ec2KeyPair": str,
        "instanceRole": str,
        "tags": Dict[str, str],
        "placementGroup": str,
        "bidPercentage": int,
        "spotIamFleetRole": str,
        "launchTemplate": "LaunchTemplateSpecificationTypeDef",
        "ec2Configuration": List["Ec2ConfigurationTypeDef"],
    },
    total=False,
)


class ComputeResourceTypeDef(_RequiredComputeResourceTypeDef, _OptionalComputeResourceTypeDef):
    pass


class ComputeResourceUpdateTypeDef(TypedDict, total=False):
    minvCpus: int
    maxvCpus: int
    desiredvCpus: int
    subnets: List[str]
    securityGroupIds: List[str]


class ContainerDetailTypeDef(TypedDict, total=False):
    image: str
    vcpus: int
    memory: int
    command: List[str]
    jobRoleArn: str
    executionRoleArn: str
    volumes: List["VolumeTypeDef"]
    environment: List["KeyValuePairTypeDef"]
    mountPoints: List["MountPointTypeDef"]
    readonlyRootFilesystem: bool
    ulimits: List["UlimitTypeDef"]
    privileged: bool
    user: str
    exitCode: int
    reason: str
    containerInstanceArn: str
    taskArn: str
    logStreamName: str
    instanceType: str
    networkInterfaces: List["NetworkInterfaceTypeDef"]
    resourceRequirements: List["ResourceRequirementTypeDef"]
    linuxParameters: "LinuxParametersTypeDef"
    logConfiguration: "LogConfigurationTypeDef"
    secrets: List["SecretTypeDef"]
    networkConfiguration: "NetworkConfigurationTypeDef"
    fargatePlatformConfiguration: "FargatePlatformConfigurationTypeDef"


class ContainerOverridesTypeDef(TypedDict, total=False):
    vcpus: int
    memory: int
    command: List[str]
    instanceType: str
    environment: List["KeyValuePairTypeDef"]
    resourceRequirements: List["ResourceRequirementTypeDef"]


class ContainerPropertiesTypeDef(TypedDict, total=False):
    image: str
    vcpus: int
    memory: int
    command: List[str]
    jobRoleArn: str
    executionRoleArn: str
    volumes: List["VolumeTypeDef"]
    environment: List["KeyValuePairTypeDef"]
    mountPoints: List["MountPointTypeDef"]
    readonlyRootFilesystem: bool
    privileged: bool
    ulimits: List["UlimitTypeDef"]
    user: str
    instanceType: str
    resourceRequirements: List["ResourceRequirementTypeDef"]
    linuxParameters: "LinuxParametersTypeDef"
    logConfiguration: "LogConfigurationTypeDef"
    secrets: List["SecretTypeDef"]
    networkConfiguration: "NetworkConfigurationTypeDef"
    fargatePlatformConfiguration: "FargatePlatformConfigurationTypeDef"


class ContainerSummaryTypeDef(TypedDict, total=False):
    exitCode: int
    reason: str


class CreateComputeEnvironmentResponseTypeDef(TypedDict, total=False):
    computeEnvironmentName: str
    computeEnvironmentArn: str


class CreateJobQueueResponseTypeDef(TypedDict):
    jobQueueName: str
    jobQueueArn: str


class DescribeComputeEnvironmentsResponseTypeDef(TypedDict, total=False):
    computeEnvironments: List["ComputeEnvironmentDetailTypeDef"]
    nextToken: str


class DescribeJobDefinitionsResponseTypeDef(TypedDict, total=False):
    jobDefinitions: List["JobDefinitionTypeDef"]
    nextToken: str


class DescribeJobQueuesResponseTypeDef(TypedDict, total=False):
    jobQueues: List["JobQueueDetailTypeDef"]
    nextToken: str


class DescribeJobsResponseTypeDef(TypedDict, total=False):
    jobs: List["JobDetailTypeDef"]


class _RequiredDeviceTypeDef(TypedDict):
    hostPath: str


class DeviceTypeDef(_RequiredDeviceTypeDef, total=False):
    containerPath: str
    permissions: List[DeviceCgroupPermission]


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


class _RequiredEc2ConfigurationTypeDef(TypedDict):
    imageType: str


class Ec2ConfigurationTypeDef(_RequiredEc2ConfigurationTypeDef, total=False):
    imageIdOverride: str


class _RequiredEvaluateOnExitTypeDef(TypedDict):
    action: RetryAction


class EvaluateOnExitTypeDef(_RequiredEvaluateOnExitTypeDef, total=False):
    onStatusReason: str
    onReason: str
    onExitCode: str


class FargatePlatformConfigurationTypeDef(TypedDict, total=False):
    platformVersion: str


class HostTypeDef(TypedDict, total=False):
    sourcePath: str


_RequiredJobDefinitionTypeDef = TypedDict(
    "_RequiredJobDefinitionTypeDef",
    {"jobDefinitionName": str, "jobDefinitionArn": str, "revision": int, "type": str},
)
_OptionalJobDefinitionTypeDef = TypedDict(
    "_OptionalJobDefinitionTypeDef",
    {
        "status": str,
        "parameters": Dict[str, str],
        "retryStrategy": "RetryStrategyTypeDef",
        "containerProperties": "ContainerPropertiesTypeDef",
        "timeout": "JobTimeoutTypeDef",
        "nodeProperties": "NodePropertiesTypeDef",
        "tags": Dict[str, str],
        "propagateTags": bool,
        "platformCapabilities": List[PlatformCapability],
    },
    total=False,
)


class JobDefinitionTypeDef(_RequiredJobDefinitionTypeDef, _OptionalJobDefinitionTypeDef):
    pass


JobDependencyTypeDef = TypedDict(
    "JobDependencyTypeDef", {"jobId": str, "type": ArrayJobDependency}, total=False
)


class _RequiredJobDetailTypeDef(TypedDict):
    jobName: str
    jobId: str
    jobQueue: str
    status: JobStatus
    startedAt: int
    jobDefinition: str


class JobDetailTypeDef(_RequiredJobDetailTypeDef, total=False):
    jobArn: str
    attempts: List["AttemptDetailTypeDef"]
    statusReason: str
    createdAt: int
    retryStrategy: "RetryStrategyTypeDef"
    stoppedAt: int
    dependsOn: List["JobDependencyTypeDef"]
    parameters: Dict[str, str]
    container: "ContainerDetailTypeDef"
    nodeDetails: "NodeDetailsTypeDef"
    nodeProperties: "NodePropertiesTypeDef"
    arrayProperties: "ArrayPropertiesDetailTypeDef"
    timeout: "JobTimeoutTypeDef"
    tags: Dict[str, str]
    propagateTags: bool
    platformCapabilities: List[PlatformCapability]


class _RequiredJobQueueDetailTypeDef(TypedDict):
    jobQueueName: str
    jobQueueArn: str
    state: JQState
    priority: int
    computeEnvironmentOrder: List["ComputeEnvironmentOrderTypeDef"]


class JobQueueDetailTypeDef(_RequiredJobQueueDetailTypeDef, total=False):
    status: JQStatus
    statusReason: str
    tags: Dict[str, str]


class _RequiredJobSummaryTypeDef(TypedDict):
    jobId: str
    jobName: str


class JobSummaryTypeDef(_RequiredJobSummaryTypeDef, total=False):
    jobArn: str
    createdAt: int
    status: JobStatus
    statusReason: str
    startedAt: int
    stoppedAt: int
    container: "ContainerSummaryTypeDef"
    arrayProperties: "ArrayPropertiesSummaryTypeDef"
    nodeProperties: "NodePropertiesSummaryTypeDef"


class JobTimeoutTypeDef(TypedDict, total=False):
    attemptDurationSeconds: int


class KeyValuePairTypeDef(TypedDict, total=False):
    name: str
    value: str


class LaunchTemplateSpecificationTypeDef(TypedDict, total=False):
    launchTemplateId: str
    launchTemplateName: str
    version: str


class LinuxParametersTypeDef(TypedDict, total=False):
    devices: List["DeviceTypeDef"]
    initProcessEnabled: bool
    sharedMemorySize: int
    tmpfs: List["TmpfsTypeDef"]
    maxSwap: int
    swappiness: int


class _RequiredListJobsResponseTypeDef(TypedDict):
    jobSummaryList: List["JobSummaryTypeDef"]


class ListJobsResponseTypeDef(_RequiredListJobsResponseTypeDef, total=False):
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class _RequiredLogConfigurationTypeDef(TypedDict):
    logDriver: LogDriver


class LogConfigurationTypeDef(_RequiredLogConfigurationTypeDef, total=False):
    options: Dict[str, str]
    secretOptions: List["SecretTypeDef"]


class MountPointTypeDef(TypedDict, total=False):
    containerPath: str
    readOnly: bool
    sourceVolume: str


class NetworkConfigurationTypeDef(TypedDict, total=False):
    assignPublicIp: AssignPublicIp


class NetworkInterfaceTypeDef(TypedDict, total=False):
    attachmentId: str
    ipv6Address: str
    privateIpv4Address: str


class NodeDetailsTypeDef(TypedDict, total=False):
    nodeIndex: int
    isMainNode: bool


class NodeOverridesTypeDef(TypedDict, total=False):
    numNodes: int
    nodePropertyOverrides: List["NodePropertyOverrideTypeDef"]


class NodePropertiesSummaryTypeDef(TypedDict, total=False):
    isMainNode: bool
    numNodes: int
    nodeIndex: int


class NodePropertiesTypeDef(TypedDict):
    numNodes: int
    mainNode: int
    nodeRangeProperties: List["NodeRangePropertyTypeDef"]


class _RequiredNodePropertyOverrideTypeDef(TypedDict):
    targetNodes: str


class NodePropertyOverrideTypeDef(_RequiredNodePropertyOverrideTypeDef, total=False):
    containerOverrides: "ContainerOverridesTypeDef"


class _RequiredNodeRangePropertyTypeDef(TypedDict):
    targetNodes: str


class NodeRangePropertyTypeDef(_RequiredNodeRangePropertyTypeDef, total=False):
    container: "ContainerPropertiesTypeDef"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RegisterJobDefinitionResponseTypeDef(TypedDict):
    jobDefinitionName: str
    jobDefinitionArn: str
    revision: int


ResourceRequirementTypeDef = TypedDict(
    "ResourceRequirementTypeDef", {"value": str, "type": ResourceType}
)


class RetryStrategyTypeDef(TypedDict, total=False):
    attempts: int
    evaluateOnExit: List["EvaluateOnExitTypeDef"]


class SecretTypeDef(TypedDict):
    name: str
    valueFrom: str


class _RequiredSubmitJobResponseTypeDef(TypedDict):
    jobName: str
    jobId: str


class SubmitJobResponseTypeDef(_RequiredSubmitJobResponseTypeDef, total=False):
    jobArn: str


class _RequiredTmpfsTypeDef(TypedDict):
    containerPath: str
    size: int


class TmpfsTypeDef(_RequiredTmpfsTypeDef, total=False):
    mountOptions: List[str]


class UlimitTypeDef(TypedDict):
    hardLimit: int
    name: str
    softLimit: int


class UpdateComputeEnvironmentResponseTypeDef(TypedDict, total=False):
    computeEnvironmentName: str
    computeEnvironmentArn: str


class UpdateJobQueueResponseTypeDef(TypedDict, total=False):
    jobQueueName: str
    jobQueueArn: str


class VolumeTypeDef(TypedDict, total=False):
    host: "HostTypeDef"
    name: str
    efsVolumeConfiguration: "EFSVolumeConfigurationTypeDef"
