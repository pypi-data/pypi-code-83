"""
Type annotations for batch service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_batch/literals.html)

Usage::

    ```python
    from mypy_boto3_batch.literals import ArrayJobDependency

    data: ArrayJobDependency = "N_TO_N"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ArrayJobDependency",
    "AssignPublicIp",
    "CEState",
    "CEStatus",
    "CEType",
    "CRAllocationStrategy",
    "CRType",
    "DescribeComputeEnvironmentsPaginatorName",
    "DescribeJobDefinitionsPaginatorName",
    "DescribeJobQueuesPaginatorName",
    "DeviceCgroupPermission",
    "EFSAuthorizationConfigIAM",
    "EFSTransitEncryption",
    "JQState",
    "JQStatus",
    "JobDefinitionType",
    "JobStatus",
    "ListJobsPaginatorName",
    "LogDriver",
    "PlatformCapability",
    "ResourceType",
    "RetryAction",
)


ArrayJobDependency = Literal["N_TO_N", "SEQUENTIAL"]
AssignPublicIp = Literal["DISABLED", "ENABLED"]
CEState = Literal["DISABLED", "ENABLED"]
CEStatus = Literal["CREATING", "DELETED", "DELETING", "INVALID", "UPDATING", "VALID"]
CEType = Literal["MANAGED", "UNMANAGED"]
CRAllocationStrategy = Literal["BEST_FIT", "BEST_FIT_PROGRESSIVE", "SPOT_CAPACITY_OPTIMIZED"]
CRType = Literal["EC2", "FARGATE", "FARGATE_SPOT", "SPOT"]
DescribeComputeEnvironmentsPaginatorName = Literal["describe_compute_environments"]
DescribeJobDefinitionsPaginatorName = Literal["describe_job_definitions"]
DescribeJobQueuesPaginatorName = Literal["describe_job_queues"]
DeviceCgroupPermission = Literal["MKNOD", "READ", "WRITE"]
EFSAuthorizationConfigIAM = Literal["DISABLED", "ENABLED"]
EFSTransitEncryption = Literal["DISABLED", "ENABLED"]
JQState = Literal["DISABLED", "ENABLED"]
JQStatus = Literal["CREATING", "DELETED", "DELETING", "INVALID", "UPDATING", "VALID"]
JobDefinitionType = Literal["container", "multinode"]
JobStatus = Literal[
    "FAILED", "PENDING", "RUNNABLE", "RUNNING", "STARTING", "SUBMITTED", "SUCCEEDED"
]
ListJobsPaginatorName = Literal["list_jobs"]
LogDriver = Literal["awslogs", "fluentd", "gelf", "journald", "json-file", "splunk", "syslog"]
PlatformCapability = Literal["EC2", "FARGATE"]
ResourceType = Literal["GPU", "MEMORY", "VCPU"]
RetryAction = Literal["EXIT", "RETRY"]
