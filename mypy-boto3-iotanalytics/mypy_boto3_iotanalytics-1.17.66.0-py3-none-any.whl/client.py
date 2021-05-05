"""
Type annotations for iotanalytics service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotanalytics import IoTAnalyticsClient

    client: IoTAnalyticsClient = boto3.client("iotanalytics")
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta

from mypy_boto3_iotanalytics.paginator import (
    ListChannelsPaginator,
    ListDatasetContentsPaginator,
    ListDatasetsPaginator,
    ListDatastoresPaginator,
    ListPipelinesPaginator,
)
from mypy_boto3_iotanalytics.type_defs import (
    BatchPutMessageResponseTypeDef,
    ChannelMessagesTypeDef,
    ChannelStorageTypeDef,
    CreateChannelResponseTypeDef,
    CreateDatasetContentResponseTypeDef,
    CreateDatasetResponseTypeDef,
    CreateDatastoreResponseTypeDef,
    CreatePipelineResponseTypeDef,
    DatasetActionTypeDef,
    DatasetContentDeliveryRuleTypeDef,
    DatasetTriggerTypeDef,
    DatastoreStorageTypeDef,
    DescribeChannelResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeDatastoreResponseTypeDef,
    DescribeLoggingOptionsResponseTypeDef,
    DescribePipelineResponseTypeDef,
    FileFormatConfigurationTypeDef,
    GetDatasetContentResponseTypeDef,
    LateDataRuleTypeDef,
    ListChannelsResponseTypeDef,
    ListDatasetContentsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListDatastoresResponseTypeDef,
    ListPipelinesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingOptionsTypeDef,
    MessageTypeDef,
    PipelineActivityTypeDef,
    RetentionPeriodTypeDef,
    RunPipelineActivityResponseTypeDef,
    SampleChannelDataResponseTypeDef,
    StartPipelineReprocessingResponseTypeDef,
    TagTypeDef,
    VersioningConfigurationTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("IoTAnalyticsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class IoTAnalyticsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_put_message(
        self, channelName: str, messages: List[MessageTypeDef]
    ) -> BatchPutMessageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.batch_put_message)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#batch-put-message)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#can-paginate)
        """

    def cancel_pipeline_reprocessing(
        self, pipelineName: str, reprocessingId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.cancel_pipeline_reprocessing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#cancel-pipeline-reprocessing)
        """

    def create_channel(
        self,
        channelName: str,
        channelStorage: "ChannelStorageTypeDef" = None,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.create_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#create-channel)
        """

    def create_dataset(
        self,
        datasetName: str,
        actions: List["DatasetActionTypeDef"],
        triggers: List["DatasetTriggerTypeDef"] = None,
        contentDeliveryRules: List["DatasetContentDeliveryRuleTypeDef"] = None,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
        versioningConfiguration: "VersioningConfigurationTypeDef" = None,
        tags: List["TagTypeDef"] = None,
        lateDataRules: List["LateDataRuleTypeDef"] = None,
    ) -> CreateDatasetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.create_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#create-dataset)
        """

    def create_dataset_content(
        self, datasetName: str, versionId: str = None
    ) -> CreateDatasetContentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.create_dataset_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#create-dataset-content)
        """

    def create_datastore(
        self,
        datastoreName: str,
        datastoreStorage: "DatastoreStorageTypeDef" = None,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
        tags: List["TagTypeDef"] = None,
        fileFormatConfiguration: "FileFormatConfigurationTypeDef" = None,
    ) -> CreateDatastoreResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.create_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#create-datastore)
        """

    def create_pipeline(
        self,
        pipelineName: str,
        pipelineActivities: List["PipelineActivityTypeDef"],
        tags: List["TagTypeDef"] = None,
    ) -> CreatePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.create_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#create-pipeline)
        """

    def delete_channel(self, channelName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#delete-channel)
        """

    def delete_dataset(self, datasetName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#delete-dataset)
        """

    def delete_dataset_content(self, datasetName: str, versionId: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_dataset_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#delete-dataset-content)
        """

    def delete_datastore(self, datastoreName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#delete-datastore)
        """

    def delete_pipeline(self, pipelineName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.delete_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#delete-pipeline)
        """

    def describe_channel(
        self, channelName: str, includeStatistics: bool = None
    ) -> DescribeChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#describe-channel)
        """

    def describe_dataset(self, datasetName: str) -> DescribeDatasetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#describe-dataset)
        """

    def describe_datastore(
        self, datastoreName: str, includeStatistics: bool = None
    ) -> DescribeDatastoreResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#describe-datastore)
        """

    def describe_logging_options(self) -> DescribeLoggingOptionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#describe-logging-options)
        """

    def describe_pipeline(self, pipelineName: str) -> DescribePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.describe_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#describe-pipeline)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#generate-presigned-url)
        """

    def get_dataset_content(
        self, datasetName: str, versionId: str = None
    ) -> GetDatasetContentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.get_dataset_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#get-dataset-content)
        """

    def list_channels(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListChannelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.list_channels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#list-channels)
        """

    def list_dataset_contents(
        self,
        datasetName: str,
        nextToken: str = None,
        maxResults: int = None,
        scheduledOnOrAfter: datetime = None,
        scheduledBefore: datetime = None,
    ) -> ListDatasetContentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.list_dataset_contents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#list-dataset-contents)
        """

    def list_datasets(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListDatasetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.list_datasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#list-datasets)
        """

    def list_datastores(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListDatastoresResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.list_datastores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#list-datastores)
        """

    def list_pipelines(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListPipelinesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.list_pipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#list-pipelines)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#list-tags-for-resource)
        """

    def put_logging_options(self, loggingOptions: "LoggingOptionsTypeDef") -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.put_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#put-logging-options)
        """

    def run_pipeline_activity(
        self, pipelineActivity: "PipelineActivityTypeDef", payloads: List[Union[bytes, IO[bytes]]]
    ) -> RunPipelineActivityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.run_pipeline_activity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#run-pipeline-activity)
        """

    def sample_channel_data(
        self,
        channelName: str,
        maxMessages: int = None,
        startTime: datetime = None,
        endTime: datetime = None,
    ) -> SampleChannelDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.sample_channel_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#sample-channel-data)
        """

    def start_pipeline_reprocessing(
        self,
        pipelineName: str,
        startTime: datetime = None,
        endTime: datetime = None,
        channelMessages: ChannelMessagesTypeDef = None,
    ) -> StartPipelineReprocessingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.start_pipeline_reprocessing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#start-pipeline-reprocessing)
        """

    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#tag-resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#untag-resource)
        """

    def update_channel(
        self,
        channelName: str,
        channelStorage: "ChannelStorageTypeDef" = None,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.update_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#update-channel)
        """

    def update_dataset(
        self,
        datasetName: str,
        actions: List["DatasetActionTypeDef"],
        triggers: List["DatasetTriggerTypeDef"] = None,
        contentDeliveryRules: List["DatasetContentDeliveryRuleTypeDef"] = None,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
        versioningConfiguration: "VersioningConfigurationTypeDef" = None,
        lateDataRules: List["LateDataRuleTypeDef"] = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.update_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#update-dataset)
        """

    def update_datastore(
        self,
        datastoreName: str,
        retentionPeriod: "RetentionPeriodTypeDef" = None,
        datastoreStorage: "DatastoreStorageTypeDef" = None,
        fileFormatConfiguration: "FileFormatConfigurationTypeDef" = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.update_datastore)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#update-datastore)
        """

    def update_pipeline(
        self, pipelineName: str, pipelineActivities: List["PipelineActivityTypeDef"]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Client.update_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/client.html#update-pipeline)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_channels"]) -> ListChannelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListChannels)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators.html#listchannelspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_dataset_contents"]
    ) -> ListDatasetContentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatasetContents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators.html#listdatasetcontentspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_datasets"]) -> ListDatasetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatasets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators.html#listdatasetspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_datastores"]) -> ListDatastoresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListDatastores)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators.html#listdatastorespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_pipelines"]) -> ListPipelinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotanalytics.html#IoTAnalytics.Paginator.ListPipelines)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/paginators.html#listpipelinespaginator)
        """
