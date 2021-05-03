"""
Type annotations for mgn service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mgn.type_defs import CPUTypeDef

    data: CPUTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_mgn.literals import (
    ChangeServerLifeCycleStateSourceServerLifecycleState,
    DataReplicationErrorString,
    DataReplicationInitiationStepName,
    DataReplicationInitiationStepStatus,
    DataReplicationState,
    FirstBoot,
    InitiatedBy,
    JobLogEvent,
    JobStatus,
    JobType,
    LaunchDisposition,
    LaunchStatus,
    LifeCycleState,
    ReplicationConfigurationDataPlaneRouting,
    ReplicationConfigurationDefaultLargeStagingDiskType,
    ReplicationConfigurationEbsEncryption,
    ReplicationConfigurationReplicatedDiskStagingDiskType,
    TargetInstanceTypeRightSizingMethod,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CPUTypeDef",
    "ChangeServerLifeCycleStateSourceServerLifecycleTypeDef",
    "DataReplicationErrorTypeDef",
    "DataReplicationInfoReplicatedDiskTypeDef",
    "DataReplicationInfoTypeDef",
    "DataReplicationInitiationStepTypeDef",
    "DataReplicationInitiationTypeDef",
    "DescribeJobLogItemsResponseTypeDef",
    "DescribeJobsRequestFiltersTypeDef",
    "DescribeJobsResponseTypeDef",
    "DescribeReplicationConfigurationTemplatesResponseTypeDef",
    "DescribeSourceServersRequestFiltersTypeDef",
    "DescribeSourceServersResponseTypeDef",
    "DiskTypeDef",
    "IdentificationHintsTypeDef",
    "JobLogEventDataTypeDef",
    "JobLogTypeDef",
    "JobTypeDef",
    "LaunchConfigurationTypeDef",
    "LaunchedInstanceTypeDef",
    "LicensingTypeDef",
    "LifeCycleLastCutoverFinalizedTypeDef",
    "LifeCycleLastCutoverInitiatedTypeDef",
    "LifeCycleLastCutoverRevertedTypeDef",
    "LifeCycleLastCutoverTypeDef",
    "LifeCycleLastTestFinalizedTypeDef",
    "LifeCycleLastTestInitiatedTypeDef",
    "LifeCycleLastTestRevertedTypeDef",
    "LifeCycleLastTestTypeDef",
    "LifeCycleTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkInterfaceTypeDef",
    "OSTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipatingServerTypeDef",
    "ReplicationConfigurationReplicatedDiskTypeDef",
    "ReplicationConfigurationTemplateTypeDef",
    "ReplicationConfigurationTypeDef",
    "SourcePropertiesTypeDef",
    "SourceServerTypeDef",
    "StartCutoverResponseTypeDef",
    "StartTestResponseTypeDef",
    "TerminateTargetInstancesResponseTypeDef",
)


class CPUTypeDef(TypedDict, total=False):
    cores: int
    modelName: str


class ChangeServerLifeCycleStateSourceServerLifecycleTypeDef(TypedDict):
    state: ChangeServerLifeCycleStateSourceServerLifecycleState


class DataReplicationErrorTypeDef(TypedDict, total=False):
    error: DataReplicationErrorString
    rawError: str


class DataReplicationInfoReplicatedDiskTypeDef(TypedDict, total=False):
    backloggedStorageBytes: int
    deviceName: str
    replicatedStorageBytes: int
    rescannedStorageBytes: int
    totalStorageBytes: int


class DataReplicationInfoTypeDef(TypedDict, total=False):
    dataReplicationError: "DataReplicationErrorTypeDef"
    dataReplicationInitiation: "DataReplicationInitiationTypeDef"
    dataReplicationState: DataReplicationState
    etaDateTime: str
    lagDuration: str
    replicatedDisks: List["DataReplicationInfoReplicatedDiskTypeDef"]


class DataReplicationInitiationStepTypeDef(TypedDict, total=False):
    name: DataReplicationInitiationStepName
    status: DataReplicationInitiationStepStatus


class DataReplicationInitiationTypeDef(TypedDict, total=False):
    nextAttemptDateTime: str
    startDateTime: str
    steps: List["DataReplicationInitiationStepTypeDef"]


class DescribeJobLogItemsResponseTypeDef(TypedDict, total=False):
    items: List["JobLogTypeDef"]
    nextToken: str


class DescribeJobsRequestFiltersTypeDef(TypedDict, total=False):
    fromDate: str
    jobIDs: List[str]
    toDate: str


class DescribeJobsResponseTypeDef(TypedDict, total=False):
    items: List["JobTypeDef"]
    nextToken: str


class DescribeReplicationConfigurationTemplatesResponseTypeDef(TypedDict, total=False):
    items: List["ReplicationConfigurationTemplateTypeDef"]
    nextToken: str


class DescribeSourceServersRequestFiltersTypeDef(TypedDict, total=False):
    isArchived: bool
    sourceServerIDs: List[str]


class DescribeSourceServersResponseTypeDef(TypedDict, total=False):
    items: List["SourceServerTypeDef"]
    nextToken: str


DiskTypeDef = TypedDict("DiskTypeDef", {"bytes": int, "deviceName": str}, total=False)


class IdentificationHintsTypeDef(TypedDict, total=False):
    awsInstanceID: str
    fqdn: str
    hostname: str
    vmWareUuid: str


class JobLogEventDataTypeDef(TypedDict, total=False):
    conversionServerID: str
    rawError: str
    sourceServerID: str
    targetInstanceID: str


class JobLogTypeDef(TypedDict, total=False):
    event: JobLogEvent
    eventData: "JobLogEventDataTypeDef"
    logDateTime: str


_RequiredJobTypeDef = TypedDict("_RequiredJobTypeDef", {"jobID": str})
_OptionalJobTypeDef = TypedDict(
    "_OptionalJobTypeDef",
    {
        "arn": str,
        "creationDateTime": str,
        "endDateTime": str,
        "initiatedBy": InitiatedBy,
        "participatingServers": List["ParticipatingServerTypeDef"],
        "status": JobStatus,
        "tags": Dict[str, str],
        "type": JobType,
    },
    total=False,
)


class JobTypeDef(_RequiredJobTypeDef, _OptionalJobTypeDef):
    pass


class LaunchConfigurationTypeDef(TypedDict, total=False):
    copyPrivateIp: bool
    copyTags: bool
    ec2LaunchTemplateID: str
    launchDisposition: LaunchDisposition
    licensing: "LicensingTypeDef"
    name: str
    sourceServerID: str
    targetInstanceTypeRightSizingMethod: TargetInstanceTypeRightSizingMethod


class LaunchedInstanceTypeDef(TypedDict, total=False):
    ec2InstanceID: str
    firstBoot: FirstBoot
    jobID: str


class LicensingTypeDef(TypedDict, total=False):
    osByol: bool


class LifeCycleLastCutoverFinalizedTypeDef(TypedDict, total=False):
    apiCallDateTime: str


class LifeCycleLastCutoverInitiatedTypeDef(TypedDict, total=False):
    apiCallDateTime: str
    jobID: str


class LifeCycleLastCutoverRevertedTypeDef(TypedDict, total=False):
    apiCallDateTime: str


class LifeCycleLastCutoverTypeDef(TypedDict, total=False):
    finalized: "LifeCycleLastCutoverFinalizedTypeDef"
    initiated: "LifeCycleLastCutoverInitiatedTypeDef"
    reverted: "LifeCycleLastCutoverRevertedTypeDef"


class LifeCycleLastTestFinalizedTypeDef(TypedDict, total=False):
    apiCallDateTime: str


class LifeCycleLastTestInitiatedTypeDef(TypedDict, total=False):
    apiCallDateTime: str
    jobID: str


class LifeCycleLastTestRevertedTypeDef(TypedDict, total=False):
    apiCallDateTime: str


class LifeCycleLastTestTypeDef(TypedDict, total=False):
    finalized: "LifeCycleLastTestFinalizedTypeDef"
    initiated: "LifeCycleLastTestInitiatedTypeDef"
    reverted: "LifeCycleLastTestRevertedTypeDef"


class LifeCycleTypeDef(TypedDict, total=False):
    addedToServiceDateTime: str
    elapsedReplicationDuration: str
    firstByteDateTime: str
    lastCutover: "LifeCycleLastCutoverTypeDef"
    lastSeenByServiceDateTime: str
    lastTest: "LifeCycleLastTestTypeDef"
    state: LifeCycleState


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class NetworkInterfaceTypeDef(TypedDict, total=False):
    ips: List[str]
    isPrimary: bool
    macAddress: str


class OSTypeDef(TypedDict, total=False):
    fullString: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParticipatingServerTypeDef(TypedDict, total=False):
    launchStatus: LaunchStatus
    sourceServerID: str


class ReplicationConfigurationReplicatedDiskTypeDef(TypedDict, total=False):
    deviceName: str
    iops: int
    isBootDisk: bool
    stagingDiskType: ReplicationConfigurationReplicatedDiskStagingDiskType


class _RequiredReplicationConfigurationTemplateTypeDef(TypedDict):
    replicationConfigurationTemplateID: str


class ReplicationConfigurationTemplateTypeDef(
    _RequiredReplicationConfigurationTemplateTypeDef, total=False
):
    arn: str
    associateDefaultSecurityGroup: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRouting
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskType
    ebsEncryption: ReplicationConfigurationEbsEncryption
    ebsEncryptionKeyArn: str
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: List[str]
    stagingAreaSubnetId: str
    stagingAreaTags: Dict[str, str]
    tags: Dict[str, str]
    useDedicatedReplicationServer: bool


class ReplicationConfigurationTypeDef(TypedDict, total=False):
    associateDefaultSecurityGroup: bool
    bandwidthThrottling: int
    createPublicIP: bool
    dataPlaneRouting: ReplicationConfigurationDataPlaneRouting
    defaultLargeStagingDiskType: ReplicationConfigurationDefaultLargeStagingDiskType
    ebsEncryption: ReplicationConfigurationEbsEncryption
    ebsEncryptionKeyArn: str
    name: str
    replicatedDisks: List["ReplicationConfigurationReplicatedDiskTypeDef"]
    replicationServerInstanceType: str
    replicationServersSecurityGroupsIDs: List[str]
    sourceServerID: str
    stagingAreaSubnetId: str
    stagingAreaTags: Dict[str, str]
    useDedicatedReplicationServer: bool


class SourcePropertiesTypeDef(TypedDict, total=False):
    cpus: List["CPUTypeDef"]
    disks: List["DiskTypeDef"]
    identificationHints: "IdentificationHintsTypeDef"
    lastUpdatedDateTime: str
    networkInterfaces: List["NetworkInterfaceTypeDef"]
    os: "OSTypeDef"
    ramBytes: int
    recommendedInstanceType: str


class SourceServerTypeDef(TypedDict, total=False):
    arn: str
    dataReplicationInfo: "DataReplicationInfoTypeDef"
    isArchived: bool
    launchedInstance: "LaunchedInstanceTypeDef"
    lifeCycle: "LifeCycleTypeDef"
    sourceProperties: "SourcePropertiesTypeDef"
    sourceServerID: str
    tags: Dict[str, str]


class StartCutoverResponseTypeDef(TypedDict, total=False):
    job: "JobTypeDef"


class StartTestResponseTypeDef(TypedDict, total=False):
    job: "JobTypeDef"


class TerminateTargetInstancesResponseTypeDef(TypedDict, total=False):
    job: "JobTypeDef"
