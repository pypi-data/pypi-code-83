"""
Type annotations for pinpoint service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pinpoint/literals.html)

Usage::

    ```python
    from mypy_boto3_pinpoint.literals import Action

    data: Action = "DEEP_LINK"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "Action",
    "AttributeType",
    "CampaignStatus",
    "ChannelType",
    "DeliveryStatus",
    "DimensionType",
    "Duration",
    "FilterType",
    "Format",
    "Frequency",
    "Include",
    "JobStatus",
    "MessageType",
    "Mode",
    "Operator",
    "RecencyType",
    "SegmentType",
    "SourceType",
    "State",
    "TemplateType",
    "TypeType",
    "__EndpointTypesElement",
)


Action = Literal["DEEP_LINK", "OPEN_APP", "URL"]
AttributeType = Literal["AFTER", "BEFORE", "BETWEEN", "CONTAINS", "EXCLUSIVE", "INCLUSIVE", "ON"]
CampaignStatus = Literal[
    "COMPLETED", "DELETED", "EXECUTING", "INVALID", "PAUSED", "PENDING_NEXT_RUN", "SCHEDULED"
]
ChannelType = Literal[
    "ADM",
    "APNS",
    "APNS_SANDBOX",
    "APNS_VOIP",
    "APNS_VOIP_SANDBOX",
    "BAIDU",
    "CUSTOM",
    "EMAIL",
    "GCM",
    "PUSH",
    "SMS",
    "VOICE",
]
DeliveryStatus = Literal[
    "DUPLICATE",
    "OPT_OUT",
    "PERMANENT_FAILURE",
    "SUCCESSFUL",
    "TEMPORARY_FAILURE",
    "THROTTLED",
    "UNKNOWN_FAILURE",
]
DimensionType = Literal["EXCLUSIVE", "INCLUSIVE"]
Duration = Literal["DAY_14", "DAY_30", "DAY_7", "HR_24"]
FilterType = Literal["ENDPOINT", "SYSTEM"]
Format = Literal["CSV", "JSON"]
Frequency = Literal["DAILY", "EVENT", "HOURLY", "MONTHLY", "ONCE", "WEEKLY"]
Include = Literal["ALL", "ANY", "NONE"]
JobStatus = Literal[
    "COMPLETED",
    "COMPLETING",
    "CREATED",
    "FAILED",
    "FAILING",
    "INITIALIZING",
    "PENDING_JOB",
    "PREPARING_FOR_INITIALIZATION",
    "PROCESSING",
]
MessageType = Literal["PROMOTIONAL", "TRANSACTIONAL"]
Mode = Literal["DELIVERY", "FILTER"]
Operator = Literal["ALL", "ANY"]
RecencyType = Literal["ACTIVE", "INACTIVE"]
SegmentType = Literal["DIMENSIONAL", "IMPORT"]
SourceType = Literal["ALL", "ANY", "NONE"]
State = Literal["ACTIVE", "CANCELLED", "CLOSED", "COMPLETED", "DRAFT", "PAUSED"]
TemplateType = Literal["EMAIL", "PUSH", "SMS", "VOICE"]
TypeType = Literal["ALL", "ANY", "NONE"]
__EndpointTypesElement = Literal[
    "ADM",
    "APNS",
    "APNS_SANDBOX",
    "APNS_VOIP",
    "APNS_VOIP_SANDBOX",
    "BAIDU",
    "CUSTOM",
    "EMAIL",
    "GCM",
    "PUSH",
    "SMS",
    "VOICE",
]
