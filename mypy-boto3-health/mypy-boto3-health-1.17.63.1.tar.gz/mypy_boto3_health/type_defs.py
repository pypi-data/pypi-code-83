"""
Type annotations for health service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_health/type_defs.html)

Usage::

    ```python
    from mypy_boto3_health.type_defs import AffectedEntityTypeDef

    data: AffectedEntityTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_health.literals import (
    entityStatusCode,
    eventScopeCode,
    eventStatusCode,
    eventTypeCategory,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AffectedEntityTypeDef",
    "DateTimeRangeTypeDef",
    "DescribeAffectedAccountsForOrganizationResponseTypeDef",
    "DescribeAffectedEntitiesForOrganizationResponseTypeDef",
    "DescribeAffectedEntitiesResponseTypeDef",
    "DescribeEntityAggregatesResponseTypeDef",
    "DescribeEventAggregatesResponseTypeDef",
    "DescribeEventDetailsForOrganizationResponseTypeDef",
    "DescribeEventDetailsResponseTypeDef",
    "DescribeEventTypesResponseTypeDef",
    "DescribeEventsForOrganizationResponseTypeDef",
    "DescribeEventsResponseTypeDef",
    "DescribeHealthServiceStatusForOrganizationResponseTypeDef",
    "EntityAggregateTypeDef",
    "EntityFilterTypeDef",
    "EventAccountFilterTypeDef",
    "EventAggregateTypeDef",
    "EventDescriptionTypeDef",
    "EventDetailsErrorItemTypeDef",
    "EventDetailsTypeDef",
    "EventFilterTypeDef",
    "EventTypeDef",
    "EventTypeFilterTypeDef",
    "EventTypeTypeDef",
    "OrganizationAffectedEntitiesErrorItemTypeDef",
    "OrganizationEventDetailsErrorItemTypeDef",
    "OrganizationEventDetailsTypeDef",
    "OrganizationEventFilterTypeDef",
    "OrganizationEventTypeDef",
    "PaginatorConfigTypeDef",
)


class AffectedEntityTypeDef(TypedDict, total=False):
    entityArn: str
    eventArn: str
    entityValue: str
    entityUrl: str
    awsAccountId: str
    lastUpdatedTime: datetime
    statusCode: entityStatusCode
    tags: Dict[str, str]


DateTimeRangeTypeDef = TypedDict(
    "DateTimeRangeTypeDef", {"from": datetime, "to": datetime}, total=False
)


class DescribeAffectedAccountsForOrganizationResponseTypeDef(TypedDict, total=False):
    affectedAccounts: List[str]
    eventScopeCode: eventScopeCode
    nextToken: str


class DescribeAffectedEntitiesForOrganizationResponseTypeDef(TypedDict, total=False):
    entities: List["AffectedEntityTypeDef"]
    failedSet: List["OrganizationAffectedEntitiesErrorItemTypeDef"]
    nextToken: str


class DescribeAffectedEntitiesResponseTypeDef(TypedDict, total=False):
    entities: List["AffectedEntityTypeDef"]
    nextToken: str


class DescribeEntityAggregatesResponseTypeDef(TypedDict, total=False):
    entityAggregates: List["EntityAggregateTypeDef"]


class DescribeEventAggregatesResponseTypeDef(TypedDict, total=False):
    eventAggregates: List["EventAggregateTypeDef"]
    nextToken: str


class DescribeEventDetailsForOrganizationResponseTypeDef(TypedDict, total=False):
    successfulSet: List["OrganizationEventDetailsTypeDef"]
    failedSet: List["OrganizationEventDetailsErrorItemTypeDef"]


class DescribeEventDetailsResponseTypeDef(TypedDict, total=False):
    successfulSet: List["EventDetailsTypeDef"]
    failedSet: List["EventDetailsErrorItemTypeDef"]


class DescribeEventTypesResponseTypeDef(TypedDict, total=False):
    eventTypes: List["EventTypeTypeDef"]
    nextToken: str


class DescribeEventsForOrganizationResponseTypeDef(TypedDict, total=False):
    events: List["OrganizationEventTypeDef"]
    nextToken: str


class DescribeEventsResponseTypeDef(TypedDict, total=False):
    events: List["EventTypeDef"]
    nextToken: str


class DescribeHealthServiceStatusForOrganizationResponseTypeDef(TypedDict, total=False):
    healthServiceAccessStatusForOrganization: str


class EntityAggregateTypeDef(TypedDict, total=False):
    eventArn: str
    count: int


class _RequiredEntityFilterTypeDef(TypedDict):
    eventArns: List[str]


class EntityFilterTypeDef(_RequiredEntityFilterTypeDef, total=False):
    entityArns: List[str]
    entityValues: List[str]
    lastUpdatedTimes: List["DateTimeRangeTypeDef"]
    tags: List[Dict[str, str]]
    statusCodes: List[entityStatusCode]


class _RequiredEventAccountFilterTypeDef(TypedDict):
    eventArn: str


class EventAccountFilterTypeDef(_RequiredEventAccountFilterTypeDef, total=False):
    awsAccountId: str


class EventAggregateTypeDef(TypedDict, total=False):
    aggregateValue: str
    count: int


class EventDescriptionTypeDef(TypedDict, total=False):
    latestDescription: str


class EventDetailsErrorItemTypeDef(TypedDict, total=False):
    eventArn: str
    errorName: str
    errorMessage: str


class EventDetailsTypeDef(TypedDict, total=False):
    event: "EventTypeDef"
    eventDescription: "EventDescriptionTypeDef"
    eventMetadata: Dict[str, str]


class EventFilterTypeDef(TypedDict, total=False):
    eventArns: List[str]
    eventTypeCodes: List[str]
    services: List[str]
    regions: List[str]
    availabilityZones: List[str]
    startTimes: List["DateTimeRangeTypeDef"]
    endTimes: List["DateTimeRangeTypeDef"]
    lastUpdatedTimes: List["DateTimeRangeTypeDef"]
    entityArns: List[str]
    entityValues: List[str]
    eventTypeCategories: List[eventTypeCategory]
    tags: List[Dict[str, str]]
    eventStatusCodes: List[eventStatusCode]


class EventTypeDef(TypedDict, total=False):
    arn: str
    service: str
    eventTypeCode: str
    eventTypeCategory: eventTypeCategory
    region: str
    availabilityZone: str
    startTime: datetime
    endTime: datetime
    lastUpdatedTime: datetime
    statusCode: eventStatusCode
    eventScopeCode: eventScopeCode


class EventTypeFilterTypeDef(TypedDict, total=False):
    eventTypeCodes: List[str]
    services: List[str]
    eventTypeCategories: List[eventTypeCategory]


class EventTypeTypeDef(TypedDict, total=False):
    service: str
    code: str
    category: eventTypeCategory


class OrganizationAffectedEntitiesErrorItemTypeDef(TypedDict, total=False):
    awsAccountId: str
    eventArn: str
    errorName: str
    errorMessage: str


class OrganizationEventDetailsErrorItemTypeDef(TypedDict, total=False):
    awsAccountId: str
    eventArn: str
    errorName: str
    errorMessage: str


class OrganizationEventDetailsTypeDef(TypedDict, total=False):
    awsAccountId: str
    event: "EventTypeDef"
    eventDescription: "EventDescriptionTypeDef"
    eventMetadata: Dict[str, str]


class OrganizationEventFilterTypeDef(TypedDict, total=False):
    eventTypeCodes: List[str]
    awsAccountIds: List[str]
    services: List[str]
    regions: List[str]
    startTime: "DateTimeRangeTypeDef"
    endTime: "DateTimeRangeTypeDef"
    lastUpdatedTime: "DateTimeRangeTypeDef"
    entityArns: List[str]
    entityValues: List[str]
    eventTypeCategories: List[eventTypeCategory]
    eventStatusCodes: List[eventStatusCode]


class OrganizationEventTypeDef(TypedDict, total=False):
    arn: str
    service: str
    eventTypeCode: str
    eventTypeCategory: eventTypeCategory
    eventScopeCode: eventScopeCode
    region: str
    startTime: datetime
    endTime: datetime
    lastUpdatedTime: datetime
    statusCode: eventStatusCode


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str
