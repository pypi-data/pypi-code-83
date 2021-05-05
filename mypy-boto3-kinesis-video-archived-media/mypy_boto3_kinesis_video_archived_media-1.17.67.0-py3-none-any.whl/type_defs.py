"""
Type annotations for kinesis-video-archived-media service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesis_video_archived_media.type_defs import ClipFragmentSelectorTypeDef

    data: ClipFragmentSelectorTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from botocore.response import StreamingBody

from mypy_boto3_kinesis_video_archived_media.literals import (
    ClipFragmentSelectorType,
    DASHFragmentSelectorType,
    FragmentSelectorType,
    HLSFragmentSelectorType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClipFragmentSelectorTypeDef",
    "ClipTimestampRangeTypeDef",
    "DASHFragmentSelectorTypeDef",
    "DASHTimestampRangeTypeDef",
    "FragmentSelectorTypeDef",
    "FragmentTypeDef",
    "GetClipOutputTypeDef",
    "GetDASHStreamingSessionURLOutputTypeDef",
    "GetHLSStreamingSessionURLOutputTypeDef",
    "GetMediaForFragmentListOutputTypeDef",
    "HLSFragmentSelectorTypeDef",
    "HLSTimestampRangeTypeDef",
    "ListFragmentsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadata",
    "TimestampRangeTypeDef",
)


class ClipFragmentSelectorTypeDef(TypedDict):
    FragmentSelectorType: ClipFragmentSelectorType
    TimestampRange: "ClipTimestampRangeTypeDef"


class ClipTimestampRangeTypeDef(TypedDict):
    StartTimestamp: datetime
    EndTimestamp: datetime


class DASHFragmentSelectorTypeDef(TypedDict, total=False):
    FragmentSelectorType: DASHFragmentSelectorType
    TimestampRange: "DASHTimestampRangeTypeDef"


class DASHTimestampRangeTypeDef(TypedDict, total=False):
    StartTimestamp: datetime
    EndTimestamp: datetime


class FragmentSelectorTypeDef(TypedDict):
    FragmentSelectorType: FragmentSelectorType
    TimestampRange: "TimestampRangeTypeDef"


class FragmentTypeDef(TypedDict, total=False):
    FragmentNumber: str
    FragmentSizeInBytes: int
    ProducerTimestamp: datetime
    ServerTimestamp: datetime
    FragmentLengthInMilliseconds: int


class GetClipOutputTypeDef(TypedDict):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: "ResponseMetadata"


class GetDASHStreamingSessionURLOutputTypeDef(TypedDict):
    DASHStreamingSessionURL: str
    ResponseMetadata: "ResponseMetadata"


class GetHLSStreamingSessionURLOutputTypeDef(TypedDict):
    HLSStreamingSessionURL: str
    ResponseMetadata: "ResponseMetadata"


class GetMediaForFragmentListOutputTypeDef(TypedDict):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: "ResponseMetadata"


class HLSFragmentSelectorTypeDef(TypedDict, total=False):
    FragmentSelectorType: HLSFragmentSelectorType
    TimestampRange: "HLSTimestampRangeTypeDef"


class HLSTimestampRangeTypeDef(TypedDict, total=False):
    StartTimestamp: datetime
    EndTimestamp: datetime


class ListFragmentsOutputTypeDef(TypedDict):
    Fragments: List["FragmentTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class TimestampRangeTypeDef(TypedDict):
    StartTimestamp: datetime
    EndTimestamp: datetime
