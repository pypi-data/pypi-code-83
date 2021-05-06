"""
Type annotations for kinesis-video-media service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_media/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesis_video_media.type_defs import GetMediaOutputTypeDef

    data: GetMediaOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict

from botocore.response import StreamingBody

from mypy_boto3_kinesis_video_media.literals import StartSelectorType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("GetMediaOutputTypeDef", "ResponseMetadata", "StartSelectorTypeDef")


class GetMediaOutputTypeDef(TypedDict):
    ContentType: str
    Payload: StreamingBody
    ResponseMetadata: "ResponseMetadata"


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class _RequiredStartSelectorTypeDef(TypedDict):
    StartSelectorType: StartSelectorType


class StartSelectorTypeDef(_RequiredStartSelectorTypeDef, total=False):
    AfterFragmentNumber: str
    StartTimestamp: datetime
    ContinuationToken: str
