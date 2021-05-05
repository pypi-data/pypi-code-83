"""
Type annotations for ivs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ivs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ivs.type_defs import BatchErrorTypeDef

    data: BatchErrorTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_ivs.literals import (
    ChannelLatencyMode,
    ChannelType,
    RecordingConfigurationState,
    StreamHealth,
    StreamState,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchErrorTypeDef",
    "BatchGetChannelResponseTypeDef",
    "BatchGetStreamKeyResponseTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateRecordingConfigurationResponseTypeDef",
    "CreateStreamKeyResponseTypeDef",
    "DestinationConfigurationTypeDef",
    "GetChannelResponseTypeDef",
    "GetPlaybackKeyPairResponseTypeDef",
    "GetRecordingConfigurationResponseTypeDef",
    "GetStreamKeyResponseTypeDef",
    "GetStreamResponseTypeDef",
    "ImportPlaybackKeyPairResponseTypeDef",
    "ListChannelsResponseTypeDef",
    "ListPlaybackKeyPairsResponseTypeDef",
    "ListRecordingConfigurationsResponseTypeDef",
    "ListStreamKeysResponseTypeDef",
    "ListStreamsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PlaybackKeyPairSummaryTypeDef",
    "PlaybackKeyPairTypeDef",
    "RecordingConfigurationSummaryTypeDef",
    "RecordingConfigurationTypeDef",
    "S3DestinationConfigurationTypeDef",
    "StreamKeySummaryTypeDef",
    "StreamKeyTypeDef",
    "StreamSummaryTypeDef",
    "StreamTypeDef",
    "UpdateChannelResponseTypeDef",
)


class BatchErrorTypeDef(TypedDict, total=False):
    arn: str
    code: str
    message: str


class BatchGetChannelResponseTypeDef(TypedDict, total=False):
    channels: List["ChannelTypeDef"]
    errors: List["BatchErrorTypeDef"]


class BatchGetStreamKeyResponseTypeDef(TypedDict, total=False):
    streamKeys: List["StreamKeyTypeDef"]
    errors: List["BatchErrorTypeDef"]


class ChannelSummaryTypeDef(TypedDict, total=False):
    arn: str
    name: str
    latencyMode: ChannelLatencyMode
    authorized: bool
    recordingConfigurationArn: str
    tags: Dict[str, str]


ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "arn": str,
        "name": str,
        "latencyMode": ChannelLatencyMode,
        "type": ChannelType,
        "recordingConfigurationArn": str,
        "ingestEndpoint": str,
        "playbackUrl": str,
        "authorized": bool,
        "tags": Dict[str, str],
    },
    total=False,
)


class CreateChannelResponseTypeDef(TypedDict, total=False):
    channel: "ChannelTypeDef"
    streamKey: "StreamKeyTypeDef"


class CreateRecordingConfigurationResponseTypeDef(TypedDict, total=False):
    recordingConfiguration: "RecordingConfigurationTypeDef"


class CreateStreamKeyResponseTypeDef(TypedDict, total=False):
    streamKey: "StreamKeyTypeDef"


class DestinationConfigurationTypeDef(TypedDict, total=False):
    s3: "S3DestinationConfigurationTypeDef"


class GetChannelResponseTypeDef(TypedDict, total=False):
    channel: "ChannelTypeDef"


class GetPlaybackKeyPairResponseTypeDef(TypedDict, total=False):
    keyPair: "PlaybackKeyPairTypeDef"


class GetRecordingConfigurationResponseTypeDef(TypedDict, total=False):
    recordingConfiguration: "RecordingConfigurationTypeDef"


class GetStreamKeyResponseTypeDef(TypedDict, total=False):
    streamKey: "StreamKeyTypeDef"


class GetStreamResponseTypeDef(TypedDict, total=False):
    stream: "StreamTypeDef"


class ImportPlaybackKeyPairResponseTypeDef(TypedDict, total=False):
    keyPair: "PlaybackKeyPairTypeDef"


class _RequiredListChannelsResponseTypeDef(TypedDict):
    channels: List["ChannelSummaryTypeDef"]


class ListChannelsResponseTypeDef(_RequiredListChannelsResponseTypeDef, total=False):
    nextToken: str


class _RequiredListPlaybackKeyPairsResponseTypeDef(TypedDict):
    keyPairs: List["PlaybackKeyPairSummaryTypeDef"]


class ListPlaybackKeyPairsResponseTypeDef(
    _RequiredListPlaybackKeyPairsResponseTypeDef, total=False
):
    nextToken: str


class _RequiredListRecordingConfigurationsResponseTypeDef(TypedDict):
    recordingConfigurations: List["RecordingConfigurationSummaryTypeDef"]


class ListRecordingConfigurationsResponseTypeDef(
    _RequiredListRecordingConfigurationsResponseTypeDef, total=False
):
    nextToken: str


class _RequiredListStreamKeysResponseTypeDef(TypedDict):
    streamKeys: List["StreamKeySummaryTypeDef"]


class ListStreamKeysResponseTypeDef(_RequiredListStreamKeysResponseTypeDef, total=False):
    nextToken: str


class _RequiredListStreamsResponseTypeDef(TypedDict):
    streams: List["StreamSummaryTypeDef"]


class ListStreamsResponseTypeDef(_RequiredListStreamsResponseTypeDef, total=False):
    nextToken: str


class _RequiredListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]


class ListTagsForResourceResponseTypeDef(_RequiredListTagsForResourceResponseTypeDef, total=False):
    nextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PlaybackKeyPairSummaryTypeDef(TypedDict, total=False):
    arn: str
    name: str
    tags: Dict[str, str]


class PlaybackKeyPairTypeDef(TypedDict, total=False):
    arn: str
    name: str
    fingerprint: str
    tags: Dict[str, str]


class _RequiredRecordingConfigurationSummaryTypeDef(TypedDict):
    arn: str
    destinationConfiguration: "DestinationConfigurationTypeDef"
    state: RecordingConfigurationState


class RecordingConfigurationSummaryTypeDef(
    _RequiredRecordingConfigurationSummaryTypeDef, total=False
):
    name: str
    tags: Dict[str, str]


class _RequiredRecordingConfigurationTypeDef(TypedDict):
    arn: str
    destinationConfiguration: "DestinationConfigurationTypeDef"
    state: RecordingConfigurationState


class RecordingConfigurationTypeDef(_RequiredRecordingConfigurationTypeDef, total=False):
    name: str
    tags: Dict[str, str]


class S3DestinationConfigurationTypeDef(TypedDict):
    bucketName: str


class StreamKeySummaryTypeDef(TypedDict, total=False):
    arn: str
    channelArn: str
    tags: Dict[str, str]


class StreamKeyTypeDef(TypedDict, total=False):
    arn: str
    value: str
    channelArn: str
    tags: Dict[str, str]


class StreamSummaryTypeDef(TypedDict, total=False):
    channelArn: str
    state: StreamState
    health: StreamHealth
    viewerCount: int
    startTime: datetime


class StreamTypeDef(TypedDict, total=False):
    channelArn: str
    playbackUrl: str
    startTime: datetime
    state: StreamState
    health: StreamHealth
    viewerCount: int


class UpdateChannelResponseTypeDef(TypedDict, total=False):
    channel: "ChannelTypeDef"
