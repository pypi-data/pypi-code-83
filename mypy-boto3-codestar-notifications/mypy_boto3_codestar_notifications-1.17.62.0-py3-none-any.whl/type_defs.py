"""
Main interface for codestar-notifications service type definitions.

Usage::

    ```python
    from mypy_boto3_codestar_notifications.type_defs import EventTypeSummaryTypeDef

    data: EventTypeSummaryTypeDef = {...}
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
    "EventTypeSummaryTypeDef",
    "NotificationRuleSummaryTypeDef",
    "TargetSummaryTypeDef",
    "CreateNotificationRuleResultTypeDef",
    "DeleteNotificationRuleResultTypeDef",
    "DescribeNotificationRuleResultTypeDef",
    "ListEventTypesFilterTypeDef",
    "ListEventTypesResultTypeDef",
    "ListNotificationRulesFilterTypeDef",
    "ListNotificationRulesResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "ListTargetsFilterTypeDef",
    "ListTargetsResultTypeDef",
    "PaginatorConfigTypeDef",
    "SubscribeResultTypeDef",
    "TagResourceResultTypeDef",
    "TargetTypeDef",
    "UnsubscribeResultTypeDef",
)

EventTypeSummaryTypeDef = TypedDict(
    "EventTypeSummaryTypeDef",
    {"EventTypeId": str, "ServiceName": str, "EventTypeName": str, "ResourceType": str},
    total=False,
)

NotificationRuleSummaryTypeDef = TypedDict(
    "NotificationRuleSummaryTypeDef", {"Id": str, "Arn": str}, total=False
)

TargetSummaryTypeDef = TypedDict(
    "TargetSummaryTypeDef",
    {"TargetAddress": str, "TargetType": str, "TargetStatus": TargetStatus},
    total=False,
)

CreateNotificationRuleResultTypeDef = TypedDict(
    "CreateNotificationRuleResultTypeDef", {"Arn": str}, total=False
)

DeleteNotificationRuleResultTypeDef = TypedDict(
    "DeleteNotificationRuleResultTypeDef", {"Arn": str}, total=False
)

_RequiredDescribeNotificationRuleResultTypeDef = TypedDict(
    "_RequiredDescribeNotificationRuleResultTypeDef", {"Arn": str}
)
_OptionalDescribeNotificationRuleResultTypeDef = TypedDict(
    "_OptionalDescribeNotificationRuleResultTypeDef",
    {
        "Name": str,
        "EventTypes": List["EventTypeSummaryTypeDef"],
        "Resource": str,
        "Targets": List["TargetSummaryTypeDef"],
        "DetailType": DetailType,
        "CreatedBy": str,
        "Status": NotificationRuleStatus,
        "CreatedTimestamp": datetime,
        "LastModifiedTimestamp": datetime,
        "Tags": Dict[str, str],
    },
    total=False,
)


class DescribeNotificationRuleResultTypeDef(
    _RequiredDescribeNotificationRuleResultTypeDef, _OptionalDescribeNotificationRuleResultTypeDef
):
    pass


ListEventTypesFilterTypeDef = TypedDict(
    "ListEventTypesFilterTypeDef", {"Name": ListEventTypesFilterName, "Value": str}
)

ListEventTypesResultTypeDef = TypedDict(
    "ListEventTypesResultTypeDef",
    {"EventTypes": List["EventTypeSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListNotificationRulesFilterTypeDef = TypedDict(
    "ListNotificationRulesFilterTypeDef", {"Name": ListNotificationRulesFilterName, "Value": str}
)

ListNotificationRulesResultTypeDef = TypedDict(
    "ListNotificationRulesResultTypeDef",
    {"NextToken": str, "NotificationRules": List["NotificationRuleSummaryTypeDef"]},
    total=False,
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef", {"Tags": Dict[str, str]}, total=False
)

ListTargetsFilterTypeDef = TypedDict(
    "ListTargetsFilterTypeDef", {"Name": ListTargetsFilterName, "Value": str}
)

ListTargetsResultTypeDef = TypedDict(
    "ListTargetsResultTypeDef",
    {"Targets": List["TargetSummaryTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SubscribeResultTypeDef = TypedDict("SubscribeResultTypeDef", {"Arn": str}, total=False)

TagResourceResultTypeDef = TypedDict(
    "TagResourceResultTypeDef", {"Tags": Dict[str, str]}, total=False
)

TargetTypeDef = TypedDict("TargetTypeDef", {"TargetType": str, "TargetAddress": str}, total=False)

UnsubscribeResultTypeDef = TypedDict("UnsubscribeResultTypeDef", {"Arn": str})
