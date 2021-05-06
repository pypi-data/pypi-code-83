"""
Type annotations for codestar-notifications service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codestar_notifications.type_defs import CreateNotificationRuleResultTypeDef

    data: CreateNotificationRuleResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_codestar_notifications.literals import (
    DetailType,
    ListEventTypesFilterName,
    ListNotificationRulesFilterName,
    ListTargetsFilterName,
    NotificationRuleStatus,
    TargetStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateNotificationRuleResultTypeDef",
    "DeleteNotificationRuleResultTypeDef",
    "DescribeNotificationRuleResultTypeDef",
    "EventTypeSummaryTypeDef",
    "ListEventTypesFilterTypeDef",
    "ListEventTypesResultTypeDef",
    "ListNotificationRulesFilterTypeDef",
    "ListNotificationRulesResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "ListTargetsFilterTypeDef",
    "ListTargetsResultTypeDef",
    "NotificationRuleSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "SubscribeResultTypeDef",
    "TagResourceResultTypeDef",
    "TargetSummaryTypeDef",
    "TargetTypeDef",
    "UnsubscribeResultTypeDef",
)


class CreateNotificationRuleResultTypeDef(TypedDict, total=False):
    Arn: str


class DeleteNotificationRuleResultTypeDef(TypedDict, total=False):
    Arn: str


class _RequiredDescribeNotificationRuleResultTypeDef(TypedDict):
    Arn: str


class DescribeNotificationRuleResultTypeDef(
    _RequiredDescribeNotificationRuleResultTypeDef, total=False
):
    Name: str
    EventTypes: List["EventTypeSummaryTypeDef"]
    Resource: str
    Targets: List["TargetSummaryTypeDef"]
    DetailType: DetailType
    CreatedBy: str
    Status: NotificationRuleStatus
    CreatedTimestamp: datetime
    LastModifiedTimestamp: datetime
    Tags: Dict[str, str]


class EventTypeSummaryTypeDef(TypedDict, total=False):
    EventTypeId: str
    ServiceName: str
    EventTypeName: str
    ResourceType: str


class ListEventTypesFilterTypeDef(TypedDict):
    Name: ListEventTypesFilterName
    Value: str


class ListEventTypesResultTypeDef(TypedDict, total=False):
    EventTypes: List["EventTypeSummaryTypeDef"]
    NextToken: str


class ListNotificationRulesFilterTypeDef(TypedDict):
    Name: ListNotificationRulesFilterName
    Value: str


class ListNotificationRulesResultTypeDef(TypedDict, total=False):
    NextToken: str
    NotificationRules: List["NotificationRuleSummaryTypeDef"]


class ListTagsForResourceResultTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class ListTargetsFilterTypeDef(TypedDict):
    Name: ListTargetsFilterName
    Value: str


class ListTargetsResultTypeDef(TypedDict, total=False):
    Targets: List["TargetSummaryTypeDef"]
    NextToken: str


class NotificationRuleSummaryTypeDef(TypedDict, total=False):
    Id: str
    Arn: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class SubscribeResultTypeDef(TypedDict, total=False):
    Arn: str


class TagResourceResultTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class TargetSummaryTypeDef(TypedDict, total=False):
    TargetAddress: str
    TargetType: str
    TargetStatus: TargetStatus


class TargetTypeDef(TypedDict, total=False):
    TargetType: str
    TargetAddress: str


class UnsubscribeResultTypeDef(TypedDict):
    Arn: str
