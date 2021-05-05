"""
Type annotations for iot1click-projects service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_projects/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot1click_projects.type_defs import DescribePlacementResponseTypeDef

    data: DescribePlacementResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DescribePlacementResponseTypeDef",
    "DescribeProjectResponseTypeDef",
    "DeviceTemplateTypeDef",
    "GetDevicesInPlacementResponseTypeDef",
    "ListPlacementsResponseTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementDescriptionTypeDef",
    "PlacementSummaryTypeDef",
    "PlacementTemplateTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectSummaryTypeDef",
)


class DescribePlacementResponseTypeDef(TypedDict):
    placement: "PlacementDescriptionTypeDef"


class DescribeProjectResponseTypeDef(TypedDict):
    project: "ProjectDescriptionTypeDef"


class DeviceTemplateTypeDef(TypedDict, total=False):
    deviceType: str
    callbackOverrides: Dict[str, str]


class GetDevicesInPlacementResponseTypeDef(TypedDict):
    devices: Dict[str, str]


class _RequiredListPlacementsResponseTypeDef(TypedDict):
    placements: List["PlacementSummaryTypeDef"]


class ListPlacementsResponseTypeDef(_RequiredListPlacementsResponseTypeDef, total=False):
    nextToken: str


class _RequiredListProjectsResponseTypeDef(TypedDict):
    projects: List["ProjectSummaryTypeDef"]


class ListProjectsResponseTypeDef(_RequiredListProjectsResponseTypeDef, total=False):
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PlacementDescriptionTypeDef(TypedDict):
    projectName: str
    placementName: str
    attributes: Dict[str, str]
    createdDate: datetime
    updatedDate: datetime


class PlacementSummaryTypeDef(TypedDict):
    projectName: str
    placementName: str
    createdDate: datetime
    updatedDate: datetime


class PlacementTemplateTypeDef(TypedDict, total=False):
    defaultAttributes: Dict[str, str]
    deviceTemplates: Dict[str, "DeviceTemplateTypeDef"]


class _RequiredProjectDescriptionTypeDef(TypedDict):
    projectName: str
    createdDate: datetime
    updatedDate: datetime


class ProjectDescriptionTypeDef(_RequiredProjectDescriptionTypeDef, total=False):
    arn: str
    description: str
    placementTemplate: "PlacementTemplateTypeDef"
    tags: Dict[str, str]


class _RequiredProjectSummaryTypeDef(TypedDict):
    projectName: str
    createdDate: datetime
    updatedDate: datetime


class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, total=False):
    arn: str
    tags: Dict[str, str]
