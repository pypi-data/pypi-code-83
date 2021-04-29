"""
Main interface for mgn service type definitions.

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
    "DataReplicationErrorTypeDef",
    "DataReplicationInfoReplicatedDiskTypeDef",
    "DataReplicationInfoTypeDef",
    "DataReplicationInitiationStepTypeDef",
    "DataReplicationInitiationTypeDef",
    "DiskTypeDef",
    "IdentificationHintsTypeDef",
    "JobLogEventDataTypeDef",
    "JobLogTypeDef",
    "JobTypeDef",
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
    "NetworkInterfaceTypeDef",
    "OSTypeDef",
    "ParticipatingServerTypeDef",
    "ReplicationConfigurationReplicatedDiskTypeDef",
    "ReplicationConfigurationTemplateTypeDef",
    "SourcePropertiesTypeDef",
    "SourceServerTypeDef",
    "ChangeServerLifeCycleStateSourceServerLifecycleTypeDef",
    "DescribeJobLogItemsResponseTypeDef",
    "DescribeJobsRequestFiltersTypeDef",
    "DescribeJobsResponseTypeDef",
    "DescribeReplicationConfigurationTemplatesResponseTypeDef",
    "DescribeSourceServersRequestFiltersTypeDef",
    "DescribeSourceServersResponseTypeDef",
    "LaunchConfigurationTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ReplicationConfigurationTypeDef",
    "StartCutoverResponseTypeDef",
    "StartTestResponseTypeDef",
    "TerminateTargetInstancesResponseTypeDef",
)

CPUTypeDef = TypedDict("CPUTypeDef", {"cores": int, "modelName": str}, total=False)

DataReplicationErrorTypeDef = TypedDict(
    "DataReplicationErrorTypeDef",
    {"error": DataReplicationErrorString, "rawError": str},
    total=False,
)

DataReplicationInfoReplicatedDiskTypeDef = TypedDict(
    "DataReplicationInfoReplicatedDiskTypeDef",
    {
        "backloggedStorageBytes": int,
        "deviceName": str,
        "replicatedStorageBytes": int,
        "rescannedStorageBytes": int,
        "totalStorageBytes": int,
    },
    total=False,
)

DataReplicationInfoTypeDef = TypedDict(
    "DataReplicationInfoTypeDef",
    {
        "dataReplicationError": "DataReplicationErrorTypeDef",
        "dataReplicationInitiation": "DataReplicationInitiationTypeDef",
        "dataReplicationState": DataReplicationState,
        "etaDateTime": str,
        "lagDuration": str,
        "replicatedDisks": List["DataReplicationInfoReplicatedDiskTypeDef"],
    },
    total=False,
)

DataReplicationInitiationStepTypeDef = TypedDict(
    "DataReplicationInitiationStepTypeDef",
    {"name": DataReplicationInitiationStepName, "status": DataReplicationInitiationStepStatus},
    total=False,
)

DataReplicationInitiationTypeDef = TypedDict(
    "DataReplicationInitiationTypeDef",
    {
        "nextAttemptDateTime": str,
        "startDateTime": str,
        "steps": List["DataReplicationInitiationStepTypeDef"],
    },
    total=False,
)

DiskTypeDef = TypedDict("DiskTypeDef", {"bytes": int, "deviceName": str}, total=False)

IdentificationHintsTypeDef = TypedDict(
    "IdentificationHintsTypeDef",
    {"awsInstanceID": str, "fqdn": str, "hostname": str, "vmWareUuid": str},
    total=False,
)

JobLogEventDataTypeDef = TypedDict(
    "JobLogEventDataTypeDef",
    {"conversionServerID": str, "rawError": str, "sourceServerID": str, "targetInstanceID": str},
    total=False,
)

JobLogTypeDef = TypedDict(
    "JobLogTypeDef",
    {"event": JobLogEvent, "eventData": "JobLogEventDataTypeDef", "logDateTime": str},
    total=False,
)

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


LaunchedInstanceTypeDef = TypedDict(
    "LaunchedInstanceTypeDef",
    {"ec2InstanceID": str, "firstBoot": FirstBoot, "jobID": str},
    total=False,
)

LicensingTypeDef = TypedDict("LicensingTypeDef", {"osByol": bool}, total=False)

LifeCycleLastCutoverFinalizedTypeDef = TypedDict(
    "LifeCycleLastCutoverFinalizedTypeDef", {"apiCallDateTime": str}, total=False
)

LifeCycleLastCutoverInitiatedTypeDef = TypedDict(
    "LifeCycleLastCutoverInitiatedTypeDef", {"apiCallDateTime": str, "jobID": str}, total=False
)

LifeCycleLastCutoverRevertedTypeDef = TypedDict(
    "LifeCycleLastCutoverRevertedTypeDef", {"apiCallDateTime": str}, total=False
)

LifeCycleLastCutoverTypeDef = TypedDict(
    "LifeCycleLastCutoverTypeDef",
    {
        "finalized": "LifeCycleLastCutoverFinalizedTypeDef",
        "initiated": "LifeCycleLastCutoverInitiatedTypeDef",
        "reverted": "LifeCycleLastCutoverRevertedTypeDef",
    },
    total=False,
)

LifeCycleLastTestFinalizedTypeDef = TypedDict(
    "LifeCycleLastTestFinalizedTypeDef", {"apiCallDateTime": str}, total=False
)

LifeCycleLastTestInitiatedTypeDef = TypedDict(
    "LifeCycleLastTestInitiatedTypeDef", {"apiCallDateTime": str, "jobID": str}, total=False
)

LifeCycleLastTestRevertedTypeDef = TypedDict(
    "LifeCycleLastTestRevertedTypeDef", {"apiCallDateTime": str}, total=False
)

LifeCycleLastTestTypeDef = TypedDict(
    "LifeCycleLastTestTypeDef",
    {
        "finalized": "LifeCycleLastTestFinalizedTypeDef",
        "initiated": "LifeCycleLastTestInitiatedTypeDef",
        "reverted": "LifeCycleLastTestRevertedTypeDef",
    },
    total=False,
)

LifeCycleTypeDef = TypedDict(
    "LifeCycleTypeDef",
    {
        "addedToServiceDateTime": str,
        "elapsedReplicationDuration": str,
        "firstByteDateTime": str,
        "lastCutover": "LifeCycleLastCutoverTypeDef",
        "lastSeenByServiceDateTime": str,
        "lastTest": "LifeCycleLastTestTypeDef",
        "state": LifeCycleState,
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef", {"ips": List[str], "isPrimary": bool, "macAddress": str}, total=False
)

OSTypeDef = TypedDict("OSTypeDef", {"fullString": str}, total=False)

ParticipatingServerTypeDef = TypedDict(
    "ParticipatingServerTypeDef", {"launchStatus": LaunchStatus, "sourceServerID": str}, total=False
)

ReplicationConfigurationReplicatedDiskTypeDef = TypedDict(
    "ReplicationConfigurationReplicatedDiskTypeDef",
    {
        "deviceName": str,
        "iops": int,
        "isBootDisk": bool,
        "stagingDiskType": ReplicationConfigurationReplicatedDiskStagingDiskType,
    },
    total=False,
)

_RequiredReplicationConfigurationTemplateTypeDef = TypedDict(
    "_RequiredReplicationConfigurationTemplateTypeDef", {"replicationConfigurationTemplateID": str}
)
_OptionalReplicationConfigurationTemplateTypeDef = TypedDict(
    "_OptionalReplicationConfigurationTemplateTypeDef",
    {
        "arn": str,
        "associateDefaultSecurityGroup": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRouting,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskType,
        "ebsEncryption": ReplicationConfigurationEbsEncryption,
        "ebsEncryptionKeyArn": str,
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": List[str],
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Dict[str, str],
        "tags": Dict[str, str],
        "useDedicatedReplicationServer": bool,
    },
    total=False,
)


class ReplicationConfigurationTemplateTypeDef(
    _RequiredReplicationConfigurationTemplateTypeDef,
    _OptionalReplicationConfigurationTemplateTypeDef,
):
    pass


SourcePropertiesTypeDef = TypedDict(
    "SourcePropertiesTypeDef",
    {
        "cpus": List["CPUTypeDef"],
        "disks": List["DiskTypeDef"],
        "identificationHints": "IdentificationHintsTypeDef",
        "lastUpdatedDateTime": str,
        "networkInterfaces": List["NetworkInterfaceTypeDef"],
        "os": "OSTypeDef",
        "ramBytes": int,
        "recommendedInstanceType": str,
    },
    total=False,
)

SourceServerTypeDef = TypedDict(
    "SourceServerTypeDef",
    {
        "arn": str,
        "dataReplicationInfo": "DataReplicationInfoTypeDef",
        "isArchived": bool,
        "launchedInstance": "LaunchedInstanceTypeDef",
        "lifeCycle": "LifeCycleTypeDef",
        "sourceProperties": "SourcePropertiesTypeDef",
        "sourceServerID": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ChangeServerLifeCycleStateSourceServerLifecycleTypeDef = TypedDict(
    "ChangeServerLifeCycleStateSourceServerLifecycleTypeDef",
    {"state": ChangeServerLifeCycleStateSourceServerLifecycleState},
)

DescribeJobLogItemsResponseTypeDef = TypedDict(
    "DescribeJobLogItemsResponseTypeDef",
    {"items": List["JobLogTypeDef"], "nextToken": str},
    total=False,
)

DescribeJobsRequestFiltersTypeDef = TypedDict(
    "DescribeJobsRequestFiltersTypeDef",
    {"fromDate": str, "jobIDs": List[str], "toDate": str},
    total=False,
)

DescribeJobsResponseTypeDef = TypedDict(
    "DescribeJobsResponseTypeDef", {"items": List["JobTypeDef"], "nextToken": str}, total=False
)

DescribeReplicationConfigurationTemplatesResponseTypeDef = TypedDict(
    "DescribeReplicationConfigurationTemplatesResponseTypeDef",
    {"items": List["ReplicationConfigurationTemplateTypeDef"], "nextToken": str},
    total=False,
)

DescribeSourceServersRequestFiltersTypeDef = TypedDict(
    "DescribeSourceServersRequestFiltersTypeDef",
    {"isArchived": bool, "sourceServerIDs": List[str]},
    total=False,
)

DescribeSourceServersResponseTypeDef = TypedDict(
    "DescribeSourceServersResponseTypeDef",
    {"items": List["SourceServerTypeDef"], "nextToken": str},
    total=False,
)

LaunchConfigurationTypeDef = TypedDict(
    "LaunchConfigurationTypeDef",
    {
        "copyPrivateIp": bool,
        "copyTags": bool,
        "ec2LaunchTemplateID": str,
        "launchDisposition": LaunchDisposition,
        "licensing": "LicensingTypeDef",
        "name": str,
        "sourceServerID": str,
        "targetInstanceTypeRightSizingMethod": TargetInstanceTypeRightSizingMethod,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ReplicationConfigurationTypeDef = TypedDict(
    "ReplicationConfigurationTypeDef",
    {
        "associateDefaultSecurityGroup": bool,
        "bandwidthThrottling": int,
        "createPublicIP": bool,
        "dataPlaneRouting": ReplicationConfigurationDataPlaneRouting,
        "defaultLargeStagingDiskType": ReplicationConfigurationDefaultLargeStagingDiskType,
        "ebsEncryption": ReplicationConfigurationEbsEncryption,
        "ebsEncryptionKeyArn": str,
        "name": str,
        "replicatedDisks": List["ReplicationConfigurationReplicatedDiskTypeDef"],
        "replicationServerInstanceType": str,
        "replicationServersSecurityGroupsIDs": List[str],
        "sourceServerID": str,
        "stagingAreaSubnetId": str,
        "stagingAreaTags": Dict[str, str],
        "useDedicatedReplicationServer": bool,
    },
    total=False,
)

StartCutoverResponseTypeDef = TypedDict(
    "StartCutoverResponseTypeDef", {"job": "JobTypeDef"}, total=False
)

StartTestResponseTypeDef = TypedDict("StartTestResponseTypeDef", {"job": "JobTypeDef"}, total=False)

TerminateTargetInstancesResponseTypeDef = TypedDict(
    "TerminateTargetInstancesResponseTypeDef", {"job": "JobTypeDef"}, total=False
)
