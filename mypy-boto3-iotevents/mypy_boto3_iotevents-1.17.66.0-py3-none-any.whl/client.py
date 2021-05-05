"""
Type annotations for iotevents service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_iotevents import IoTEventsClient

    client: IoTEventsClient = boto3.client("iotevents")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_iotevents.literals import EvaluationMethod
from mypy_boto3_iotevents.type_defs import (
    CreateDetectorModelResponseTypeDef,
    CreateInputResponseTypeDef,
    DescribeDetectorModelAnalysisResponseTypeDef,
    DescribeDetectorModelResponseTypeDef,
    DescribeInputResponseTypeDef,
    DescribeLoggingOptionsResponseTypeDef,
    DetectorModelDefinitionTypeDef,
    GetDetectorModelAnalysisResultsResponseTypeDef,
    InputDefinitionTypeDef,
    ListDetectorModelsResponseTypeDef,
    ListDetectorModelVersionsResponseTypeDef,
    ListInputsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    LoggingOptionsTypeDef,
    StartDetectorModelAnalysisResponseTypeDef,
    TagTypeDef,
    UpdateDetectorModelResponseTypeDef,
    UpdateInputResponseTypeDef,
)

__all__ = ("IoTEventsClient",)


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
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]


class IoTEventsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#can-paginate)
        """

    def create_detector_model(
        self,
        detectorModelName: str,
        detectorModelDefinition: "DetectorModelDefinitionTypeDef",
        roleArn: str,
        detectorModelDescription: str = None,
        key: str = None,
        tags: List["TagTypeDef"] = None,
        evaluationMethod: EvaluationMethod = None,
    ) -> CreateDetectorModelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.create_detector_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#create-detector-model)
        """

    def create_input(
        self,
        inputName: str,
        inputDefinition: "InputDefinitionTypeDef",
        inputDescription: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateInputResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.create_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#create-input)
        """

    def delete_detector_model(self, detectorModelName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.delete_detector_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#delete-detector-model)
        """

    def delete_input(self, inputName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.delete_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#delete-input)
        """

    def describe_detector_model(
        self, detectorModelName: str, detectorModelVersion: str = None
    ) -> DescribeDetectorModelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.describe_detector_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#describe-detector-model)
        """

    def describe_detector_model_analysis(
        self, analysisId: str
    ) -> DescribeDetectorModelAnalysisResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.describe_detector_model_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#describe-detector-model-analysis)
        """

    def describe_input(self, inputName: str) -> DescribeInputResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.describe_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#describe-input)
        """

    def describe_logging_options(self) -> DescribeLoggingOptionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.describe_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#describe-logging-options)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#generate-presigned-url)
        """

    def get_detector_model_analysis_results(
        self, analysisId: str, nextToken: str = None, maxResults: int = None
    ) -> GetDetectorModelAnalysisResultsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.get_detector_model_analysis_results)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#get-detector-model-analysis-results)
        """

    def list_detector_model_versions(
        self, detectorModelName: str, nextToken: str = None, maxResults: int = None
    ) -> ListDetectorModelVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.list_detector_model_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#list-detector-model-versions)
        """

    def list_detector_models(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListDetectorModelsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.list_detector_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#list-detector-models)
        """

    def list_inputs(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListInputsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.list_inputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#list-inputs)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#list-tags-for-resource)
        """

    def put_logging_options(self, loggingOptions: "LoggingOptionsTypeDef") -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.put_logging_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#put-logging-options)
        """

    def start_detector_model_analysis(
        self, detectorModelDefinition: "DetectorModelDefinitionTypeDef"
    ) -> StartDetectorModelAnalysisResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.start_detector_model_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#start-detector-model-analysis)
        """

    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#tag-resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#untag-resource)
        """

    def update_detector_model(
        self,
        detectorModelName: str,
        detectorModelDefinition: "DetectorModelDefinitionTypeDef",
        roleArn: str,
        detectorModelDescription: str = None,
        evaluationMethod: EvaluationMethod = None,
    ) -> UpdateDetectorModelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.update_detector_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#update-detector-model)
        """

    def update_input(
        self,
        inputName: str,
        inputDefinition: "InputDefinitionTypeDef",
        inputDescription: str = None,
    ) -> UpdateInputResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/iotevents.html#IoTEvents.Client.update_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/client.html#update-input)
        """
