"""
Type annotations for firehose service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_firehose import FirehoseClient

    client: FirehoseClient = boto3.client("firehose")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_firehose.literals import DeliveryStreamType
from mypy_boto3_firehose.type_defs import (
    CreateDeliveryStreamOutputTypeDef,
    DeliveryStreamEncryptionConfigurationInputTypeDef,
    DescribeDeliveryStreamOutputTypeDef,
    ElasticsearchDestinationConfigurationTypeDef,
    ElasticsearchDestinationUpdateTypeDef,
    ExtendedS3DestinationConfigurationTypeDef,
    ExtendedS3DestinationUpdateTypeDef,
    HttpEndpointDestinationConfigurationTypeDef,
    HttpEndpointDestinationUpdateTypeDef,
    KinesisStreamSourceConfigurationTypeDef,
    ListDeliveryStreamsOutputTypeDef,
    ListTagsForDeliveryStreamOutputTypeDef,
    PutRecordBatchOutputTypeDef,
    PutRecordOutputTypeDef,
    RecordTypeDef,
    RedshiftDestinationConfigurationTypeDef,
    RedshiftDestinationUpdateTypeDef,
    S3DestinationConfigurationTypeDef,
    S3DestinationUpdateTypeDef,
    SplunkDestinationConfigurationTypeDef,
    SplunkDestinationUpdateTypeDef,
    TagTypeDef,
)

__all__ = ("FirehoseClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    InvalidKMSResourceException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]


class FirehoseClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/firehose.html#Firehose.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/firehose.html#Firehose.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#can-paginate)
        """

    def create_delivery_stream(
        self,
        DeliveryStreamName: str,
        DeliveryStreamType: DeliveryStreamType = None,
        KinesisStreamSourceConfiguration: KinesisStreamSourceConfigurationTypeDef = None,
        DeliveryStreamEncryptionConfigurationInput: DeliveryStreamEncryptionConfigurationInputTypeDef = None,
        S3DestinationConfiguration: "S3DestinationConfigurationTypeDef" = None,
        ExtendedS3DestinationConfiguration: ExtendedS3DestinationConfigurationTypeDef = None,
        RedshiftDestinationConfiguration: RedshiftDestinationConfigurationTypeDef = None,
        ElasticsearchDestinationConfiguration: ElasticsearchDestinationConfigurationTypeDef = None,
        SplunkDestinationConfiguration: SplunkDestinationConfigurationTypeDef = None,
        HttpEndpointDestinationConfiguration: HttpEndpointDestinationConfigurationTypeDef = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDeliveryStreamOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/firehose.html#Firehose.Client.create_delivery_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#create-delivery-stream)
        """

    def delete_delivery_stream(
        self, DeliveryStreamName: str, AllowForceDelete: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/firehose.html#Firehose.Client.delete_delivery_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#delete-delivery-stream)
        """

    def describe_delivery_stream(
        self, DeliveryStreamName: str, Limit: int = None, ExclusiveStartDestinationId: str = None
    ) -> DescribeDeliveryStreamOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/firehose.html#Firehose.Client.describe_delivery_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#describe-delivery-stream)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/firehose.html#Firehose.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#generate-presigned-url)
        """

    def list_delivery_streams(
        self,
        Limit: int = None,
        DeliveryStreamType: DeliveryStreamType = None,
        ExclusiveStartDeliveryStreamName: str = None,
    ) -> ListDeliveryStreamsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/firehose.html#Firehose.Client.list_delivery_streams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#list-delivery-streams)
        """

    def list_tags_for_delivery_stream(
        self, DeliveryStreamName: str, ExclusiveStartTagKey: str = None, Limit: int = None
    ) -> ListTagsForDeliveryStreamOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/firehose.html#Firehose.Client.list_tags_for_delivery_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#list-tags-for-delivery-stream)
        """

    def put_record(self, DeliveryStreamName: str, Record: RecordTypeDef) -> PutRecordOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/firehose.html#Firehose.Client.put_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#put-record)
        """

    def put_record_batch(
        self, DeliveryStreamName: str, Records: List[RecordTypeDef]
    ) -> PutRecordBatchOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/firehose.html#Firehose.Client.put_record_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#put-record-batch)
        """

    def start_delivery_stream_encryption(
        self,
        DeliveryStreamName: str,
        DeliveryStreamEncryptionConfigurationInput: DeliveryStreamEncryptionConfigurationInputTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/firehose.html#Firehose.Client.start_delivery_stream_encryption)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#start-delivery-stream-encryption)
        """

    def stop_delivery_stream_encryption(self, DeliveryStreamName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/firehose.html#Firehose.Client.stop_delivery_stream_encryption)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#stop-delivery-stream-encryption)
        """

    def tag_delivery_stream(
        self, DeliveryStreamName: str, Tags: List["TagTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/firehose.html#Firehose.Client.tag_delivery_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#tag-delivery-stream)
        """

    def untag_delivery_stream(self, DeliveryStreamName: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/firehose.html#Firehose.Client.untag_delivery_stream)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#untag-delivery-stream)
        """

    def update_destination(
        self,
        DeliveryStreamName: str,
        CurrentDeliveryStreamVersionId: str,
        DestinationId: str,
        S3DestinationUpdate: "S3DestinationUpdateTypeDef" = None,
        ExtendedS3DestinationUpdate: ExtendedS3DestinationUpdateTypeDef = None,
        RedshiftDestinationUpdate: RedshiftDestinationUpdateTypeDef = None,
        ElasticsearchDestinationUpdate: ElasticsearchDestinationUpdateTypeDef = None,
        SplunkDestinationUpdate: SplunkDestinationUpdateTypeDef = None,
        HttpEndpointDestinationUpdate: HttpEndpointDestinationUpdateTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/firehose.html#Firehose.Client.update_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/client.html#update-destination)
        """
