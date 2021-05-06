"""
Type annotations for mobile service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mobile/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mobile.type_defs import BundleDetailsTypeDef

    data: BundleDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_mobile.literals import Platform, ProjectState

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BundleDetailsTypeDef",
    "CreateProjectResultTypeDef",
    "DeleteProjectResultTypeDef",
    "DescribeBundleResultTypeDef",
    "DescribeProjectResultTypeDef",
    "ExportBundleResultTypeDef",
    "ExportProjectResultTypeDef",
    "ListBundlesResultTypeDef",
    "ListProjectsResultTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectDetailsTypeDef",
    "ProjectSummaryTypeDef",
    "ResourceTypeDef",
    "UpdateProjectResultTypeDef",
)


class BundleDetailsTypeDef(TypedDict, total=False):
    bundleId: str
    title: str
    version: str
    description: str
    iconUrl: str
    availablePlatforms: List[Platform]


class CreateProjectResultTypeDef(TypedDict, total=False):
    details: "ProjectDetailsTypeDef"


class DeleteProjectResultTypeDef(TypedDict, total=False):
    deletedResources: List["ResourceTypeDef"]
    orphanedResources: List["ResourceTypeDef"]


class DescribeBundleResultTypeDef(TypedDict, total=False):
    details: "BundleDetailsTypeDef"


class DescribeProjectResultTypeDef(TypedDict, total=False):
    details: "ProjectDetailsTypeDef"


class ExportBundleResultTypeDef(TypedDict, total=False):
    downloadUrl: str


class ExportProjectResultTypeDef(TypedDict, total=False):
    downloadUrl: str
    shareUrl: str
    snapshotId: str


class ListBundlesResultTypeDef(TypedDict, total=False):
    bundleList: List["BundleDetailsTypeDef"]
    nextToken: str


class ListProjectsResultTypeDef(TypedDict, total=False):
    projects: List["ProjectSummaryTypeDef"]
    nextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ProjectDetailsTypeDef(TypedDict, total=False):
    name: str
    projectId: str
    region: str
    state: ProjectState
    createdDate: datetime
    lastUpdatedDate: datetime
    consoleUrl: str
    resources: List["ResourceTypeDef"]


class ProjectSummaryTypeDef(TypedDict, total=False):
    name: str
    projectId: str


ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {"type": str, "name": str, "arn": str, "feature": str, "attributes": Dict[str, str]},
    total=False,
)


class UpdateProjectResultTypeDef(TypedDict, total=False):
    details: "ProjectDetailsTypeDef"
