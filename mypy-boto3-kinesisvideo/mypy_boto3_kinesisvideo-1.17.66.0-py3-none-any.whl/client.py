"""
Type annotations for kinesisvideo service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesisvideo import KinesisVideoClient

    client: KinesisVideoClient = boto3.client("kinesisvideo")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_kinesisvideo.literals import APIName, UpdateDataRetentionOperation
from mypy_boto3_kinesisvideo.paginator import ListSignalingChannelsPaginator, ListStreamsPaginator
from mypy_boto3_kinesisvideo.type_defs import (
    ChannelNameConditionTypeDef,
    CreateSignalingChannelOutputTypeDef,
    CreateStreamOutputTypeDef,
    DescribeSignalingChannelOutputTypeDef,
    DescribeStreamOutputTypeDef,
    GetDataEndpointOutputTypeDef,
    GetSignalingChannelEndpointOutputTypeDef,
    ListSignalingChannelsOutputTypeDef,
    ListStreamsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTagsForStreamOutputTypeDef,
    SingleMasterChannelEndpointConfigurationTypeDef,
    SingleMasterConfigurationTypeDef,
    StreamNameConditionTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("KinesisVideoClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AccountChannelLimitExceededException: Type[BotocoreClientError]
    AccountStreamLimitExceededException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientLimitExceededException: Type[BotocoreClientError]
    DeviceStreamLimitExceededException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidDeviceException: Type[BotocoreClientError]
    InvalidResourceFormatException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TagsPerResourceExceededLimitException: Type[BotocoreClientError]
    VersionMismatchException: Type[BotocoreClientError]


class KinesisVideoClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#can-paginate)
        """

    def create_signaling_channel(
        self,
        ChannelName: str,
        ChannelType: Literal["SINGLE_MASTER"] = None,
        SingleMasterConfiguration: "SingleMasterConfigurationTypeDef" = None,
        Tags: List[TagTypeDef] = None,
    ) -> CreateSignalingChannelOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.create_signaling_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#create-signaling-channel)
        """

    def create_stream(
        self,
        StreamName: str,
        DeviceName: str = None,
        MediaType: str = None,
        KmsKeyId: str = None,
        DataRetentionInHours: int = None,
        Tags: Dict[str, str] = None,
    ) -> CreateStreamOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.create_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#create-stream)
        """

    def delete_signaling_channel(
        self, ChannelARN: str, CurrentVersion: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.delete_signaling_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#delete-signaling-channel)
        """

    def delete_stream(self, StreamARN: str, CurrentVersion: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.delete_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#delete-stream)
        """

    def describe_signaling_channel(
        self, ChannelName: str = None, ChannelARN: str = None
    ) -> DescribeSignalingChannelOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_signaling_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#describe-signaling-channel)
        """

    def describe_stream(
        self, StreamName: str = None, StreamARN: str = None
    ) -> DescribeStreamOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.describe_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#describe-stream)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#generate-presigned-url)
        """

    def get_data_endpoint(
        self, APIName: APIName, StreamName: str = None, StreamARN: str = None
    ) -> GetDataEndpointOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.get_data_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#get-data-endpoint)
        """

    def get_signaling_channel_endpoint(
        self,
        ChannelARN: str,
        SingleMasterChannelEndpointConfiguration: SingleMasterChannelEndpointConfigurationTypeDef = None,
    ) -> GetSignalingChannelEndpointOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.get_signaling_channel_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#get-signaling-channel-endpoint)
        """

    def list_signaling_channels(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        ChannelNameCondition: ChannelNameConditionTypeDef = None,
    ) -> ListSignalingChannelsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.list_signaling_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#list-signaling-channels)
        """

    def list_streams(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        StreamNameCondition: StreamNameConditionTypeDef = None,
    ) -> ListStreamsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.list_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#list-streams)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, NextToken: str = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#list-tags-for-resource)
        """

    def list_tags_for_stream(
        self, NextToken: str = None, StreamARN: str = None, StreamName: str = None
    ) -> ListTagsForStreamOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.list_tags_for_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#list-tags-for-stream)
        """

    def tag_resource(self, ResourceARN: str, Tags: List[TagTypeDef]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#tag-resource)
        """

    def tag_stream(
        self, Tags: Dict[str, str], StreamARN: str = None, StreamName: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.tag_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#tag-stream)
        """

    def untag_resource(self, ResourceARN: str, TagKeyList: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#untag-resource)
        """

    def untag_stream(
        self, TagKeyList: List[str], StreamARN: str = None, StreamName: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.untag_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#untag-stream)
        """

    def update_data_retention(
        self,
        CurrentVersion: str,
        Operation: UpdateDataRetentionOperation,
        DataRetentionChangeInHours: int,
        StreamName: str = None,
        StreamARN: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.update_data_retention)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#update-data-retention)
        """

    def update_signaling_channel(
        self,
        ChannelARN: str,
        CurrentVersion: str,
        SingleMasterConfiguration: "SingleMasterConfigurationTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.update_signaling_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#update-signaling-channel)
        """

    def update_stream(
        self,
        CurrentVersion: str,
        StreamName: str = None,
        StreamARN: str = None,
        DeviceName: str = None,
        MediaType: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Client.update_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/client.html#update-stream)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_signaling_channels"]
    ) -> ListSignalingChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListSignalingChannels)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators.html#listsignalingchannelspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_streams"]) -> ListStreamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/kinesisvideo.html#KinesisVideo.Paginator.ListStreams)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/paginators.html#liststreamspaginator)
        """
