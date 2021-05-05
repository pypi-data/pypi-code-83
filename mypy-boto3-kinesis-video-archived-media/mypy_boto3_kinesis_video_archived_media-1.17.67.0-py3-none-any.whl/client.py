"""
Type annotations for kinesis-video-archived-media service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesis_video_archived_media import KinesisVideoArchivedMediaClient

    client: KinesisVideoArchivedMediaClient = boto3.client("kinesis-video-archived-media")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_kinesis_video_archived_media.literals import (
    ContainerFormat,
    DASHDisplayFragmentNumber,
    DASHDisplayFragmentTimestamp,
    DASHPlaybackMode,
    HLSDiscontinuityMode,
    HLSDisplayFragmentTimestamp,
    HLSPlaybackMode,
)
from mypy_boto3_kinesis_video_archived_media.paginator import ListFragmentsPaginator
from mypy_boto3_kinesis_video_archived_media.type_defs import (
    ClipFragmentSelectorTypeDef,
    DASHFragmentSelectorTypeDef,
    FragmentSelectorTypeDef,
    GetClipOutputTypeDef,
    GetDASHStreamingSessionURLOutputTypeDef,
    GetHLSStreamingSessionURLOutputTypeDef,
    GetMediaForFragmentListOutputTypeDef,
    HLSFragmentSelectorTypeDef,
    ListFragmentsOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KinesisVideoArchivedMediaClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ClientLimitExceededException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidCodecPrivateDataException: Type[BotocoreClientError]
    InvalidMediaFrameException: Type[BotocoreClientError]
    MissingCodecPrivateDataException: Type[BotocoreClientError]
    NoDataRetentionException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    UnsupportedStreamMediaTypeException: Type[BotocoreClientError]


class KinesisVideoArchivedMediaClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html#can-paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html#generate-presigned-url)
        """

    def get_clip(
        self,
        ClipFragmentSelector: ClipFragmentSelectorTypeDef,
        StreamName: str = None,
        StreamARN: str = None,
    ) -> GetClipOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_clip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html#get-clip)
        """

    def get_dash_streaming_session_url(
        self,
        StreamName: str = None,
        StreamARN: str = None,
        PlaybackMode: DASHPlaybackMode = None,
        DisplayFragmentTimestamp: DASHDisplayFragmentTimestamp = None,
        DisplayFragmentNumber: DASHDisplayFragmentNumber = None,
        DASHFragmentSelector: DASHFragmentSelectorTypeDef = None,
        Expires: int = None,
        MaxManifestFragmentResults: int = None,
    ) -> GetDASHStreamingSessionURLOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_dash_streaming_session_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html#get-dash-streaming-session-url)
        """

    def get_hls_streaming_session_url(
        self,
        StreamName: str = None,
        StreamARN: str = None,
        PlaybackMode: HLSPlaybackMode = None,
        HLSFragmentSelector: HLSFragmentSelectorTypeDef = None,
        ContainerFormat: ContainerFormat = None,
        DiscontinuityMode: HLSDiscontinuityMode = None,
        DisplayFragmentTimestamp: HLSDisplayFragmentTimestamp = None,
        Expires: int = None,
        MaxMediaPlaylistFragmentResults: int = None,
    ) -> GetHLSStreamingSessionURLOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_hls_streaming_session_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html#get-hls-streaming-session-url)
        """

    def get_media_for_fragment_list(
        self, Fragments: List[str], StreamName: str = None, StreamARN: str = None
    ) -> GetMediaForFragmentListOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.get_media_for_fragment_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html#get-media-for-fragment-list)
        """

    def list_fragments(
        self,
        StreamName: str = None,
        StreamARN: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        FragmentSelector: FragmentSelectorTypeDef = None,
    ) -> ListFragmentsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Client.list_fragments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/client.html#list-fragments)
        """

    def get_paginator(self, operation_name: Literal["list_fragments"]) -> ListFragmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesis-video-archived-media.html#KinesisVideoArchivedMedia.Paginator.ListFragments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/paginators.html#listfragmentspaginator)
        """
