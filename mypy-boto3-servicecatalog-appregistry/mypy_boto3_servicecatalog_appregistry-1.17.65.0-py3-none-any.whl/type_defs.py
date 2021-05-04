"""
Type annotations for servicecatalog-appregistry service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog_appregistry/type_defs.html)

Usage::

    ```python
    from mypy_boto3_servicecatalog_appregistry.type_defs import ApplicationSummaryTypeDef

    data: ApplicationSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_servicecatalog_appregistry.literals import SyncAction

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationSummaryTypeDef",
    "ApplicationTypeDef",
    "AssociateAttributeGroupResponseTypeDef",
    "AssociateResourceResponseTypeDef",
    "AttributeGroupSummaryTypeDef",
    "AttributeGroupTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateAttributeGroupResponseTypeDef",
    "DeleteApplicationResponseTypeDef",
    "DeleteAttributeGroupResponseTypeDef",
    "DisassociateAttributeGroupResponseTypeDef",
    "DisassociateResourceResponseTypeDef",
    "GetApplicationResponseTypeDef",
    "GetAttributeGroupResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListAssociatedAttributeGroupsResponseTypeDef",
    "ListAssociatedResourcesResponseTypeDef",
    "ListAttributeGroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceInfoTypeDef",
    "SyncResourceResponseTypeDef",
    "UpdateApplicationResponseTypeDef",
    "UpdateAttributeGroupResponseTypeDef",
)

ApplicationSummaryTypeDef = TypedDict(
    "ApplicationSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

ApplicationTypeDef = TypedDict(
    "ApplicationTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class AssociateAttributeGroupResponseTypeDef(TypedDict, total=False):
    applicationArn: str
    attributeGroupArn: str


class AssociateResourceResponseTypeDef(TypedDict, total=False):
    applicationArn: str
    resourceArn: str


AttributeGroupSummaryTypeDef = TypedDict(
    "AttributeGroupSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
    },
    total=False,
)

AttributeGroupTypeDef = TypedDict(
    "AttributeGroupTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateApplicationResponseTypeDef(TypedDict, total=False):
    application: "ApplicationTypeDef"


class CreateAttributeGroupResponseTypeDef(TypedDict, total=False):
    attributeGroup: "AttributeGroupTypeDef"


class DeleteApplicationResponseTypeDef(TypedDict, total=False):
    application: "ApplicationSummaryTypeDef"


class DeleteAttributeGroupResponseTypeDef(TypedDict, total=False):
    attributeGroup: "AttributeGroupSummaryTypeDef"


class DisassociateAttributeGroupResponseTypeDef(TypedDict, total=False):
    applicationArn: str
    attributeGroupArn: str


class DisassociateResourceResponseTypeDef(TypedDict, total=False):
    applicationArn: str
    resourceArn: str


GetApplicationResponseTypeDef = TypedDict(
    "GetApplicationResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "associatedResourceCount": int,
        "tags": Dict[str, str],
    },
    total=False,
)

GetAttributeGroupResponseTypeDef = TypedDict(
    "GetAttributeGroupResponseTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "attributes": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ListApplicationsResponseTypeDef(TypedDict, total=False):
    applications: List["ApplicationSummaryTypeDef"]
    nextToken: str


class ListAssociatedAttributeGroupsResponseTypeDef(TypedDict, total=False):
    attributeGroups: List[str]
    nextToken: str


class ListAssociatedResourcesResponseTypeDef(TypedDict, total=False):
    resources: List["ResourceInfoTypeDef"]
    nextToken: str


class ListAttributeGroupsResponseTypeDef(TypedDict, total=False):
    attributeGroups: List["AttributeGroupSummaryTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ResourceInfoTypeDef(TypedDict, total=False):
    name: str
    arn: str


class SyncResourceResponseTypeDef(TypedDict, total=False):
    applicationArn: str
    resourceArn: str
    actionTaken: SyncAction


class UpdateApplicationResponseTypeDef(TypedDict, total=False):
    application: "ApplicationTypeDef"


class UpdateAttributeGroupResponseTypeDef(TypedDict, total=False):
    attributeGroup: "AttributeGroupTypeDef"
