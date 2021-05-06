"""
Type annotations for personalize-events service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize_events/type_defs.html)

Usage::

    ```python
    from mypy_boto3_personalize_events.type_defs import EventTypeDef

    data: EventTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("EventTypeDef", "ItemTypeDef", "UserTypeDef")


class _RequiredEventTypeDef(TypedDict):
    eventType: str
    sentAt: datetime


class EventTypeDef(_RequiredEventTypeDef, total=False):
    eventId: str
    eventValue: float
    itemId: str
    properties: str
    recommendationId: str
    impression: List[str]


class _RequiredItemTypeDef(TypedDict):
    itemId: str


class ItemTypeDef(_RequiredItemTypeDef, total=False):
    properties: str


class _RequiredUserTypeDef(TypedDict):
    userId: str


class UserTypeDef(_RequiredUserTypeDef, total=False):
    properties: str
