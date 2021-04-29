"""
Main interface for mgh service type definitions.

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
    "DiscoveredResourceTypeDef",
    "MigrationTaskSummaryTypeDef",
    "MigrationTaskTypeDef",
    "ProgressUpdateStreamSummaryTypeDef",
    "ResourceAttributeTypeDef",
    "TaskTypeDef",
    "DescribeApplicationStateResultTypeDef",
    "DescribeMigrationTaskResultTypeDef",
    "ListApplicationStatesResultTypeDef",
    "ListCreatedArtifactsResultTypeDef",
    "ListDiscoveredResourcesResultTypeDef",
    "ListMigrationTasksResultTypeDef",
    "ListProgressUpdateStreamsResultTypeDef",
    "PaginatorConfigTypeDef",
)

ApplicationStateTypeDef = TypedDict(
    "ApplicationStateTypeDef",
    {"ApplicationId": str, "ApplicationStatus": ApplicationStatus, "LastUpdatedTime": datetime},
    total=False,
)

_RequiredCreatedArtifactTypeDef = TypedDict("_RequiredCreatedArtifactTypeDef", {"Name": str})
_OptionalCreatedArtifactTypeDef = TypedDict(
    "_OptionalCreatedArtifactTypeDef", {"Description": str}, total=False
)


class CreatedArtifactTypeDef(_RequiredCreatedArtifactTypeDef, _OptionalCreatedArtifactTypeDef):
    pass


_RequiredDiscoveredResourceTypeDef = TypedDict(
    "_RequiredDiscoveredResourceTypeDef", {"ConfigurationId": str}
)
_OptionalDiscoveredResourceTypeDef = TypedDict(
    "_OptionalDiscoveredResourceTypeDef", {"Description": str}, total=False
)


class DiscoveredResourceTypeDef(
    _RequiredDiscoveredResourceTypeDef, _OptionalDiscoveredResourceTypeDef
):
    pass


MigrationTaskSummaryTypeDef = TypedDict(
    "MigrationTaskSummaryTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Status": Status,
        "ProgressPercent": int,
        "StatusDetail": str,
        "UpdateDateTime": datetime,
    },
    total=False,
)

MigrationTaskTypeDef = TypedDict(
    "MigrationTaskTypeDef",
    {
        "ProgressUpdateStream": str,
        "MigrationTaskName": str,
        "Task": "TaskTypeDef",
        "UpdateDateTime": datetime,
        "ResourceAttributeList": List["ResourceAttributeTypeDef"],
    },
    total=False,
)

ProgressUpdateStreamSummaryTypeDef = TypedDict(
    "ProgressUpdateStreamSummaryTypeDef", {"ProgressUpdateStreamName": str}, total=False
)

ResourceAttributeTypeDef = TypedDict(
    "ResourceAttributeTypeDef", {"Type": ResourceAttributeType, "Value": str}
)

_RequiredTaskTypeDef = TypedDict("_RequiredTaskTypeDef", {"Status": Status})
_OptionalTaskTypeDef = TypedDict(
    "_OptionalTaskTypeDef", {"StatusDetail": str, "ProgressPercent": int}, total=False
)


class TaskTypeDef(_RequiredTaskTypeDef, _OptionalTaskTypeDef):
    pass


DescribeApplicationStateResultTypeDef = TypedDict(
    "DescribeApplicationStateResultTypeDef",
    {"ApplicationStatus": ApplicationStatus, "LastUpdatedTime": datetime},
    total=False,
)

DescribeMigrationTaskResultTypeDef = TypedDict(
    "DescribeMigrationTaskResultTypeDef", {"MigrationTask": "MigrationTaskTypeDef"}, total=False
)

ListApplicationStatesResultTypeDef = TypedDict(
    "ListApplicationStatesResultTypeDef",
    {"ApplicationStateList": List["ApplicationStateTypeDef"], "NextToken": str},
    total=False,
)

ListCreatedArtifactsResultTypeDef = TypedDict(
    "ListCreatedArtifactsResultTypeDef",
    {"NextToken": str, "CreatedArtifactList": List["CreatedArtifactTypeDef"]},
    total=False,
)

ListDiscoveredResourcesResultTypeDef = TypedDict(
    "ListDiscoveredResourcesResultTypeDef",
    {"NextToken": str, "DiscoveredResourceList": List["DiscoveredResourceTypeDef"]},
    total=False,
)

ListMigrationTasksResultTypeDef = TypedDict(
    "ListMigrationTasksResultTypeDef",
    {"NextToken": str, "MigrationTaskSummaryList": List["MigrationTaskSummaryTypeDef"]},
    total=False,
)

ListProgressUpdateStreamsResultTypeDef = TypedDict(
    "ListProgressUpdateStreamsResultTypeDef",
    {
        "ProgressUpdateStreamSummaryList": List["ProgressUpdateStreamSummaryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
