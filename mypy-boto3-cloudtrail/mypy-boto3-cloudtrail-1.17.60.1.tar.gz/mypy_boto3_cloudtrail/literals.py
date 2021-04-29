"""
Main interface for cloudtrail service literal definitions.

Usage::

    ```python
    from mypy_boto3_cloudtrail.literals import EventCategory

    data: EventCategory = "insight"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "EventCategory",
    "InsightType",
    "ListPublicKeysPaginatorName",
    "ListTagsPaginatorName",
    "ListTrailsPaginatorName",
    "LookupAttributeKey",
    "LookupEventsPaginatorName",
    "ReadWriteType",
)


EventCategory = Literal["insight"]
InsightType = Literal["ApiCallRateInsight"]
ListPublicKeysPaginatorName = Literal["list_public_keys"]
ListTagsPaginatorName = Literal["list_tags"]
ListTrailsPaginatorName = Literal["list_trails"]
LookupAttributeKey = Literal[
    "AccessKeyId",
    "EventId",
    "EventName",
    "EventSource",
    "ReadOnly",
    "ResourceName",
    "ResourceType",
    "Username",
]
LookupEventsPaginatorName = Literal["lookup_events"]
ReadWriteType = Literal["All", "ReadOnly", "WriteOnly"]
