"""
Type annotations for marketplace-catalog service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_marketplace_catalog/type_defs.html)

Usage::

    ```python
    from mypy_boto3_marketplace_catalog.type_defs import CancelChangeSetResponseTypeDef

    data: CancelChangeSetResponseTypeDef = {...}
    ```
"""
import sys
from typing import List

from mypy_boto3_marketplace_catalog.literals import ChangeStatus, FailureCode, SortOrder

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelChangeSetResponseTypeDef",
    "ChangeSetSummaryListItemTypeDef",
    "ChangeSummaryTypeDef",
    "ChangeTypeDef",
    "DescribeChangeSetResponseTypeDef",
    "DescribeEntityResponseTypeDef",
    "EntitySummaryTypeDef",
    "EntityTypeDef",
    "ErrorDetailTypeDef",
    "FilterTypeDef",
    "ListChangeSetsResponseTypeDef",
    "ListEntitiesResponseTypeDef",
    "SortTypeDef",
    "StartChangeSetResponseTypeDef",
)


class CancelChangeSetResponseTypeDef(TypedDict, total=False):
    ChangeSetId: str
    ChangeSetArn: str


class ChangeSetSummaryListItemTypeDef(TypedDict, total=False):
    ChangeSetId: str
    ChangeSetArn: str
    ChangeSetName: str
    StartTime: str
    EndTime: str
    Status: ChangeStatus
    EntityIdList: List[str]
    FailureCode: FailureCode


class ChangeSummaryTypeDef(TypedDict, total=False):
    ChangeType: str
    Entity: "EntityTypeDef"
    Details: str
    ErrorDetailList: List["ErrorDetailTypeDef"]
    ChangeName: str


class _RequiredChangeTypeDef(TypedDict):
    ChangeType: str
    Entity: "EntityTypeDef"
    Details: str


class ChangeTypeDef(_RequiredChangeTypeDef, total=False):
    ChangeName: str


class DescribeChangeSetResponseTypeDef(TypedDict, total=False):
    ChangeSetId: str
    ChangeSetArn: str
    ChangeSetName: str
    StartTime: str
    EndTime: str
    Status: ChangeStatus
    FailureCode: FailureCode
    FailureDescription: str
    ChangeSet: List["ChangeSummaryTypeDef"]


class DescribeEntityResponseTypeDef(TypedDict, total=False):
    EntityType: str
    EntityIdentifier: str
    EntityArn: str
    LastModifiedDate: str
    Details: str


class EntitySummaryTypeDef(TypedDict, total=False):
    Name: str
    EntityType: str
    EntityId: str
    EntityArn: str
    LastModifiedDate: str
    Visibility: str


_RequiredEntityTypeDef = TypedDict("_RequiredEntityTypeDef", {"Type": str})
_OptionalEntityTypeDef = TypedDict("_OptionalEntityTypeDef", {"Identifier": str}, total=False)


class EntityTypeDef(_RequiredEntityTypeDef, _OptionalEntityTypeDef):
    pass


class ErrorDetailTypeDef(TypedDict, total=False):
    ErrorCode: str
    ErrorMessage: str


class FilterTypeDef(TypedDict, total=False):
    Name: str
    ValueList: List[str]


class ListChangeSetsResponseTypeDef(TypedDict, total=False):
    ChangeSetSummaryList: List["ChangeSetSummaryListItemTypeDef"]
    NextToken: str


class ListEntitiesResponseTypeDef(TypedDict, total=False):
    EntitySummaryList: List["EntitySummaryTypeDef"]
    NextToken: str


class SortTypeDef(TypedDict, total=False):
    SortBy: str
    SortOrder: SortOrder


class StartChangeSetResponseTypeDef(TypedDict, total=False):
    ChangeSetId: str
    ChangeSetArn: str
