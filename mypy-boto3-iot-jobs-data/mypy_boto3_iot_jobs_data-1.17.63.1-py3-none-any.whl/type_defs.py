"""
Type annotations for iot-jobs-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_jobs_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot_jobs_data.type_defs import DescribeJobExecutionResponseTypeDef

    data: DescribeJobExecutionResponseTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_iot_jobs_data.literals import JobExecutionStatus

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DescribeJobExecutionResponseTypeDef",
    "GetPendingJobExecutionsResponseTypeDef",
    "JobExecutionStateTypeDef",
    "JobExecutionSummaryTypeDef",
    "JobExecutionTypeDef",
    "StartNextPendingJobExecutionResponseTypeDef",
    "UpdateJobExecutionResponseTypeDef",
)


class DescribeJobExecutionResponseTypeDef(TypedDict, total=False):
    execution: "JobExecutionTypeDef"


class GetPendingJobExecutionsResponseTypeDef(TypedDict, total=False):
    inProgressJobs: List["JobExecutionSummaryTypeDef"]
    queuedJobs: List["JobExecutionSummaryTypeDef"]


class JobExecutionStateTypeDef(TypedDict, total=False):
    status: JobExecutionStatus
    statusDetails: Dict[str, str]
    versionNumber: int


class JobExecutionSummaryTypeDef(TypedDict, total=False):
    jobId: str
    queuedAt: int
    startedAt: int
    lastUpdatedAt: int
    versionNumber: int
    executionNumber: int


class JobExecutionTypeDef(TypedDict, total=False):
    jobId: str
    thingName: str
    status: JobExecutionStatus
    statusDetails: Dict[str, str]
    queuedAt: int
    startedAt: int
    lastUpdatedAt: int
    approximateSecondsBeforeTimedOut: int
    versionNumber: int
    executionNumber: int
    jobDocument: str


class StartNextPendingJobExecutionResponseTypeDef(TypedDict, total=False):
    execution: "JobExecutionTypeDef"


class UpdateJobExecutionResponseTypeDef(TypedDict, total=False):
    executionState: "JobExecutionStateTypeDef"
    jobDocument: str
