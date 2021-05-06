"""
Type annotations for mgn service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgn/literals.html)

Usage::

    ```python
    from mypy_boto3_mgn.literals import ChangeServerLifeCycleStateSourceServerLifecycleState

    data: ChangeServerLifeCycleStateSourceServerLifecycleState = "CUTOVER"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ChangeServerLifeCycleStateSourceServerLifecycleState",
    "DataReplicationErrorString",
    "DataReplicationInitiationStepName",
    "DataReplicationInitiationStepStatus",
    "DataReplicationState",
    "DescribeJobLogItemsPaginatorName",
    "DescribeJobsPaginatorName",
    "DescribeReplicationConfigurationTemplatesPaginatorName",
    "DescribeSourceServersPaginatorName",
    "FirstBoot",
    "InitiatedBy",
    "JobLogEvent",
    "JobStatus",
    "JobType",
    "LaunchDisposition",
    "LaunchStatus",
    "LifeCycleState",
    "ReplicationConfigurationDataPlaneRouting",
    "ReplicationConfigurationDefaultLargeStagingDiskType",
    "ReplicationConfigurationEbsEncryption",
    "ReplicationConfigurationReplicatedDiskStagingDiskType",
    "TargetInstanceTypeRightSizingMethod",
)


ChangeServerLifeCycleStateSourceServerLifecycleState = Literal[
    "CUTOVER", "READY_FOR_CUTOVER", "READY_FOR_TEST"
]
DataReplicationErrorString = Literal[
    "AGENT_NOT_SEEN",
    "FAILED_TO_ATTACH_STAGING_DISKS",
    "FAILED_TO_AUTHENTICATE_WITH_SERVICE",
    "FAILED_TO_BOOT_REPLICATION_SERVER",
    "FAILED_TO_CONNECT_AGENT_TO_REPLICATION_SERVER",
    "FAILED_TO_CREATE_SECURITY_GROUP",
    "FAILED_TO_CREATE_STAGING_DISKS",
    "FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE",
    "FAILED_TO_LAUNCH_REPLICATION_SERVER",
    "FAILED_TO_PAIR_REPLICATION_SERVER_WITH_AGENT",
    "FAILED_TO_START_DATA_TRANSFER",
    "NOT_CONVERGING",
    "SNAPSHOTS_FAILURE",
    "UNSTABLE_NETWORK",
]
DataReplicationInitiationStepName = Literal[
    "ATTACH_STAGING_DISKS",
    "AUTHENTICATE_WITH_SERVICE",
    "BOOT_REPLICATION_SERVER",
    "CONNECT_AGENT_TO_REPLICATION_SERVER",
    "CREATE_SECURITY_GROUP",
    "CREATE_STAGING_DISKS",
    "DOWNLOAD_REPLICATION_SOFTWARE",
    "LAUNCH_REPLICATION_SERVER",
    "PAIR_REPLICATION_SERVER_WITH_AGENT",
    "START_DATA_TRANSFER",
    "WAIT",
]
DataReplicationInitiationStepStatus = Literal[
    "FAILED", "IN_PROGRESS", "NOT_STARTED", "SKIPPED", "SUCCEEDED"
]
DataReplicationState = Literal[
    "BACKLOG",
    "CONTINUOUS",
    "CREATING_SNAPSHOT",
    "DISCONNECTED",
    "INITIAL_SYNC",
    "INITIATING",
    "PAUSED",
    "RESCAN",
    "STALLED",
    "STOPPED",
]
DescribeJobLogItemsPaginatorName = Literal["describe_job_log_items"]
DescribeJobsPaginatorName = Literal["describe_jobs"]
DescribeReplicationConfigurationTemplatesPaginatorName = Literal[
    "describe_replication_configuration_templates"
]
DescribeSourceServersPaginatorName = Literal["describe_source_servers"]
FirstBoot = Literal["STOPPED", "SUCCEEDED", "UNKNOWN", "WAITING"]
InitiatedBy = Literal["DIAGNOSTIC", "START_CUTOVER", "START_TEST", "TERMINATE"]
JobLogEvent = Literal[
    "CLEANUP_END",
    "CLEANUP_FAIL",
    "CLEANUP_START",
    "CONVERSION_END",
    "CONVERSION_FAIL",
    "CONVERSION_START",
    "JOB_CANCEL",
    "JOB_END",
    "JOB_START",
    "LAUNCH_FAILED",
    "LAUNCH_START",
    "SERVER_SKIPPED",
    "SNAPSHOT_END",
    "SNAPSHOT_FAIL",
    "SNAPSHOT_START",
    "USING_PREVIOUS_SNAPSHOT",
]
JobStatus = Literal["COMPLETED", "PENDING", "STARTED"]
JobType = Literal["LAUNCH", "TERMINATE"]
LaunchDisposition = Literal["STARTED", "STOPPED"]
LaunchStatus = Literal["FAILED", "IN_PROGRESS", "LAUNCHED", "PENDING", "TERMINATED"]
LifeCycleState = Literal[
    "CUTOVER",
    "CUTTING_OVER",
    "DISCONNECTED",
    "NOT_READY",
    "READY_FOR_CUTOVER",
    "READY_FOR_TEST",
    "STOPPED",
    "TESTING",
]
ReplicationConfigurationDataPlaneRouting = Literal["PRIVATE_IP", "PUBLIC_IP"]
ReplicationConfigurationDefaultLargeStagingDiskType = Literal["GP2", "ST1"]
ReplicationConfigurationEbsEncryption = Literal["CUSTOM", "DEFAULT", "NONE"]
ReplicationConfigurationReplicatedDiskStagingDiskType = Literal[
    "AUTO", "GP2", "IO1", "SC1", "ST1", "STANDARD"
]
TargetInstanceTypeRightSizingMethod = Literal["BASIC", "NONE"]
