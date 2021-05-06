"""
Type annotations for cloudtrail service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/literals.html)

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
