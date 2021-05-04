"""
Type annotations for mgh service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mgh.type_defs import ApplicationStateTypeDef

    data: ApplicationStateTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_mgh.literals import ApplicationStatus, ResourceAttributeType, Status

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationStateTypeDef",
    "CreatedArtifactTypeDef",
    "DescribeApplicationStateResultTypeDef",
    "DescribeMigrationTaskResultTypeDef",
    "DiscoveredResourceTypeDef",
    "ListApplicationStatesResultTypeDef",
    "ListCreatedArtifactsResultTypeDef",
    "ListDiscoveredResourcesResultTypeDef",
    "ListMigrationTasksResultTypeDef",
    "ListProgressUpdateStreamsResultTypeDef",
    "MigrationTaskSummaryTypeDef",
    "MigrationTaskTypeDef",
    "PaginatorConfigTypeDef",
    "ProgressUpdateStreamSummaryTypeDef",
    "ResourceAttributeTypeDef",
    "TaskTypeDef",
)


class ApplicationStateTypeDef(TypedDict, total=False):
    ApplicationId: str
    ApplicationStatus: ApplicationStatus
    LastUpdatedTime: datetime


class _RequiredCreatedArtifactTypeDef(TypedDict):
    Name: str


class CreatedArtifactTypeDef(_RequiredCreatedArtifactTypeDef, total=False):
    Description: str


class DescribeApplicationStateResultTypeDef(TypedDict, total=False):
    ApplicationStatus: ApplicationStatus
    LastUpdatedTime: datetime


class DescribeMigrationTaskResultTypeDef(TypedDict, total=False):
    MigrationTask: "MigrationTaskTypeDef"


class _RequiredDiscoveredResourceTypeDef(TypedDict):
    ConfigurationId: str


class DiscoveredResourceTypeDef(_RequiredDiscoveredResourceTypeDef, total=False):
    Description: str


class ListApplicationStatesResultTypeDef(TypedDict, total=False):
    ApplicationStateList: List["ApplicationStateTypeDef"]
    NextToken: str


class ListCreatedArtifactsResultTypeDef(TypedDict, total=False):
    NextToken: str
    CreatedArtifactList: List["CreatedArtifactTypeDef"]


class ListDiscoveredResourcesResultTypeDef(TypedDict, total=False):
    NextToken: str
    DiscoveredResourceList: List["DiscoveredResourceTypeDef"]


class ListMigrationTasksResultTypeDef(TypedDict, total=False):
    NextToken: str
    MigrationTaskSummaryList: List["MigrationTaskSummaryTypeDef"]


class ListProgressUpdateStreamsResultTypeDef(TypedDict, total=False):
    ProgressUpdateStreamSummaryList: List["ProgressUpdateStreamSummaryTypeDef"]
    NextToken: str


class MigrationTaskSummaryTypeDef(TypedDict, total=False):
    ProgressUpdateStream: str
    MigrationTaskName: str
    Status: Status
    ProgressPercent: int
    StatusDetail: str
    UpdateDateTime: datetime


class MigrationTaskTypeDef(TypedDict, total=False):
    ProgressUpdateStream: str
    MigrationTaskName: str
    Task: "TaskTypeDef"
    UpdateDateTime: datetime
    ResourceAttributeList: List["ResourceAttributeTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ProgressUpdateStreamSummaryTypeDef(TypedDict, total=False):
    ProgressUpdateStreamName: str


ResourceAttributeTypeDef = TypedDict(
    "ResourceAttributeTypeDef", {"Type": ResourceAttributeType, "Value": str}
)


class _RequiredTaskTypeDef(TypedDict):
    Status: Status


class TaskTypeDef(_RequiredTaskTypeDef, total=False):
    StatusDetail: str
    ProgressPercent: int
