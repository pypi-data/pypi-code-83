"""
Type annotations for iotfleethub service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotfleethub/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotfleethub.type_defs import ApplicationSummaryTypeDef

    data: ApplicationSummaryTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_iotfleethub.literals import ApplicationState

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationSummaryTypeDef",
    "CreateApplicationResponseTypeDef",
    "DescribeApplicationResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
)


class _RequiredApplicationSummaryTypeDef(TypedDict):
    applicationId: str
    applicationName: str
    applicationUrl: str


class ApplicationSummaryTypeDef(_RequiredApplicationSummaryTypeDef, total=False):
    applicationDescription: str
    applicationCreationDate: int
    applicationLastUpdateDate: int
    applicationState: ApplicationState


class CreateApplicationResponseTypeDef(TypedDict):
    applicationId: str
    applicationArn: str


class _RequiredDescribeApplicationResponseTypeDef(TypedDict):
    applicationId: str
    applicationArn: str
    applicationName: str
    applicationUrl: str
    applicationState: ApplicationState
    applicationCreationDate: int
    applicationLastUpdateDate: int
    roleArn: str


class DescribeApplicationResponseTypeDef(_RequiredDescribeApplicationResponseTypeDef, total=False):
    applicationDescription: str
    ssoClientId: str
    errorMessage: str
    tags: Dict[str, str]


class ListApplicationsResponseTypeDef(TypedDict, total=False):
    applicationSummaries: List["ApplicationSummaryTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str
