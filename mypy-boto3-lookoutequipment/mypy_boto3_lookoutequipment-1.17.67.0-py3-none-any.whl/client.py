"""
Type annotations for lookoutequipment service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lookoutequipment import LookoutEquipmentClient

    client: LookoutEquipmentClient = boto3.client("lookoutequipment")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_lookoutequipment.literals import (
    DataUploadFrequency,
    InferenceExecutionStatus,
    IngestionJobStatus,
    ModelStatus,
)
from mypy_boto3_lookoutequipment.type_defs import (
    CreateDatasetResponseTypeDef,
    CreateInferenceSchedulerResponseTypeDef,
    CreateModelResponseTypeDef,
    DataPreProcessingConfigurationTypeDef,
    DatasetSchemaTypeDef,
    DescribeDataIngestionJobResponseTypeDef,
    DescribeDatasetResponseTypeDef,
    DescribeInferenceSchedulerResponseTypeDef,
    DescribeModelResponseTypeDef,
    InferenceInputConfigurationTypeDef,
    InferenceOutputConfigurationTypeDef,
    IngestionInputConfigurationTypeDef,
    LabelsInputConfigurationTypeDef,
    ListDataIngestionJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListInferenceExecutionsResponseTypeDef,
    ListInferenceSchedulersResponseTypeDef,
    ListModelsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    StartDataIngestionJobResponseTypeDef,
    StartInferenceSchedulerResponseTypeDef,
    StopInferenceSchedulerResponseTypeDef,
    TagTypeDef,
)

__all__ = ("LookoutEquipmentClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class LookoutEquipmentClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#can-paginate)
        """

    def create_dataset(
        self,
        DatasetName: str,
        DatasetSchema: DatasetSchemaTypeDef,
        ClientToken: str,
        ServerSideKmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDatasetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#create-dataset)
        """

    def create_inference_scheduler(
        self,
        ModelName: str,
        InferenceSchedulerName: str,
        DataUploadFrequency: DataUploadFrequency,
        DataInputConfiguration: "InferenceInputConfigurationTypeDef",
        DataOutputConfiguration: "InferenceOutputConfigurationTypeDef",
        RoleArn: str,
        ClientToken: str,
        DataDelayOffsetInMinutes: int = None,
        ServerSideKmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateInferenceSchedulerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_inference_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#create-inference-scheduler)
        """

    def create_model(
        self,
        ModelName: str,
        DatasetName: str,
        ClientToken: str,
        DatasetSchema: DatasetSchemaTypeDef = None,
        LabelsInputConfiguration: "LabelsInputConfigurationTypeDef" = None,
        TrainingDataStartTime: datetime = None,
        TrainingDataEndTime: datetime = None,
        EvaluationDataStartTime: datetime = None,
        EvaluationDataEndTime: datetime = None,
        RoleArn: str = None,
        DataPreProcessingConfiguration: "DataPreProcessingConfigurationTypeDef" = None,
        ServerSideKmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateModelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.create_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#create-model)
        """

    def delete_dataset(self, DatasetName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#delete-dataset)
        """

    def delete_inference_scheduler(self, InferenceSchedulerName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_inference_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#delete-inference-scheduler)
        """

    def delete_model(self, ModelName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.delete_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#delete-model)
        """

    def describe_data_ingestion_job(self, JobId: str) -> DescribeDataIngestionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_data_ingestion_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#describe-data-ingestion-job)
        """

    def describe_dataset(self, DatasetName: str) -> DescribeDatasetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_dataset)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#describe-dataset)
        """

    def describe_inference_scheduler(
        self, InferenceSchedulerName: str
    ) -> DescribeInferenceSchedulerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_inference_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#describe-inference-scheduler)
        """

    def describe_model(self, ModelName: str) -> DescribeModelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.describe_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#describe-model)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#generate-presigned-url)
        """

    def list_data_ingestion_jobs(
        self,
        DatasetName: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        Status: IngestionJobStatus = None,
    ) -> ListDataIngestionJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_data_ingestion_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list-data-ingestion-jobs)
        """

    def list_datasets(
        self, NextToken: str = None, MaxResults: int = None, DatasetNameBeginsWith: str = None
    ) -> ListDatasetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_datasets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list-datasets)
        """

    def list_inference_executions(
        self,
        InferenceSchedulerName: str,
        NextToken: str = None,
        MaxResults: int = None,
        DataStartTimeAfter: datetime = None,
        DataEndTimeBefore: datetime = None,
        Status: InferenceExecutionStatus = None,
    ) -> ListInferenceExecutionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_inference_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list-inference-executions)
        """

    def list_inference_schedulers(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        InferenceSchedulerNameBeginsWith: str = None,
        ModelName: str = None,
    ) -> ListInferenceSchedulersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_inference_schedulers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list-inference-schedulers)
        """

    def list_models(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        Status: ModelStatus = None,
        ModelNameBeginsWith: str = None,
        DatasetNameBeginsWith: str = None,
    ) -> ListModelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list-models)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#list-tags-for-resource)
        """

    def start_data_ingestion_job(
        self,
        DatasetName: str,
        IngestionInputConfiguration: "IngestionInputConfigurationTypeDef",
        RoleArn: str,
        ClientToken: str,
    ) -> StartDataIngestionJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.start_data_ingestion_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#start-data-ingestion-job)
        """

    def start_inference_scheduler(
        self, InferenceSchedulerName: str
    ) -> StartInferenceSchedulerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.start_inference_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#start-inference-scheduler)
        """

    def stop_inference_scheduler(
        self, InferenceSchedulerName: str
    ) -> StopInferenceSchedulerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.stop_inference_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#stop-inference-scheduler)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#untag-resource)
        """

    def update_inference_scheduler(
        self,
        InferenceSchedulerName: str,
        DataDelayOffsetInMinutes: int = None,
        DataUploadFrequency: DataUploadFrequency = None,
        DataInputConfiguration: "InferenceInputConfigurationTypeDef" = None,
        DataOutputConfiguration: "InferenceOutputConfigurationTypeDef" = None,
        RoleArn: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/lookoutequipment.html#LookoutEquipment.Client.update_inference_scheduler)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/client.html#update-inference-scheduler)
        """
