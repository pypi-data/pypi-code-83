"""
Type annotations for frauddetector service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_frauddetector import FraudDetectorClient

    client: FraudDetectorClient = boto3.client("frauddetector")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_frauddetector.literals import (
    DataSource,
    DataType,
    DetectorVersionStatus,
    ModelEndpointStatus,
    ModelVersionStatus,
    RuleExecutionMode,
)
from mypy_boto3_frauddetector.type_defs import (
    BatchCreateVariableResultTypeDef,
    BatchGetVariableResultTypeDef,
    CreateDetectorVersionResultTypeDef,
    CreateModelVersionResultTypeDef,
    CreateRuleResultTypeDef,
    DescribeDetectorResultTypeDef,
    DescribeModelVersionsResultTypeDef,
    EntityTypeDef,
    ExternalEventsDetailTypeDef,
    GetBatchPredictionJobsResultTypeDef,
    GetDetectorsResultTypeDef,
    GetDetectorVersionResultTypeDef,
    GetEntityTypesResultTypeDef,
    GetEventPredictionResultTypeDef,
    GetEventTypesResultTypeDef,
    GetExternalModelsResultTypeDef,
    GetKMSEncryptionKeyResultTypeDef,
    GetLabelsResultTypeDef,
    GetModelsResultTypeDef,
    GetModelVersionResultTypeDef,
    GetOutcomesResultTypeDef,
    GetRulesResultTypeDef,
    GetVariablesResultTypeDef,
    ListTagsForResourceResultTypeDef,
    ModelEndpointDataBlobTypeDef,
    ModelInputConfigurationTypeDef,
    ModelOutputConfigurationTypeDef,
    ModelVersionTypeDef,
    RuleTypeDef,
    TagTypeDef,
    TrainingDataSchemaTypeDef,
    UpdateModelVersionResultTypeDef,
    UpdateRuleVersionResultTypeDef,
    VariableEntryTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("FraudDetectorClient",)


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
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class FraudDetectorClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_create_variable(
        self, variableEntries: List[VariableEntryTypeDef], tags: List["TagTypeDef"] = None
    ) -> BatchCreateVariableResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.batch_create_variable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#batch-create-variable)
        """

    def batch_get_variable(self, names: List[str]) -> BatchGetVariableResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.batch_get_variable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#batch-get-variable)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#can-paginate)
        """

    def cancel_batch_prediction_job(self, jobId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.cancel_batch_prediction_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#cancel-batch-prediction-job)
        """

    def create_batch_prediction_job(
        self,
        jobId: str,
        inputPath: str,
        outputPath: str,
        eventTypeName: str,
        detectorName: str,
        iamRoleArn: str,
        detectorVersion: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.create_batch_prediction_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#create-batch-prediction-job)
        """

    def create_detector_version(
        self,
        detectorId: str,
        rules: List["RuleTypeDef"],
        description: str = None,
        externalModelEndpoints: List[str] = None,
        modelVersions: List["ModelVersionTypeDef"] = None,
        ruleExecutionMode: RuleExecutionMode = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateDetectorVersionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.create_detector_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#create-detector-version)
        """

    def create_model(
        self,
        modelId: str,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"],
        eventTypeName: str,
        description: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.create_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#create-model)
        """

    def create_model_version(
        self,
        modelId: str,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"],
        trainingDataSource: Literal["EXTERNAL_EVENTS"],
        trainingDataSchema: "TrainingDataSchemaTypeDef",
        externalEventsDetail: "ExternalEventsDetailTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateModelVersionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.create_model_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#create-model-version)
        """

    def create_rule(
        self,
        ruleId: str,
        detectorId: str,
        expression: str,
        language: Literal["DETECTORPL"],
        outcomes: List[str],
        description: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateRuleResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.create_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#create-rule)
        """

    def create_variable(
        self,
        name: str,
        dataType: DataType,
        dataSource: DataSource,
        defaultValue: str,
        description: str = None,
        variableType: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.create_variable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#create-variable)
        """

    def delete_batch_prediction_job(self, jobId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.delete_batch_prediction_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete-batch-prediction-job)
        """

    def delete_detector(self, detectorId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.delete_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete-detector)
        """

    def delete_detector_version(self, detectorId: str, detectorVersionId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.delete_detector_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete-detector-version)
        """

    def delete_entity_type(self, name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.delete_entity_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete-entity-type)
        """

    def delete_event(self, eventId: str, eventTypeName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.delete_event)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete-event)
        """

    def delete_event_type(self, name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.delete_event_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete-event-type)
        """

    def delete_external_model(self, modelEndpoint: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.delete_external_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete-external-model)
        """

    def delete_label(self, name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.delete_label)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete-label)
        """

    def delete_model(
        self, modelId: str, modelType: Literal["ONLINE_FRAUD_INSIGHTS"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.delete_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete-model)
        """

    def delete_model_version(
        self, modelId: str, modelType: Literal["ONLINE_FRAUD_INSIGHTS"], modelVersionNumber: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.delete_model_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete-model-version)
        """

    def delete_outcome(self, name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.delete_outcome)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete-outcome)
        """

    def delete_rule(self, rule: "RuleTypeDef") -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.delete_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete-rule)
        """

    def delete_variable(self, name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.delete_variable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#delete-variable)
        """

    def describe_detector(
        self, detectorId: str, nextToken: str = None, maxResults: int = None
    ) -> DescribeDetectorResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.describe_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#describe-detector)
        """

    def describe_model_versions(
        self,
        modelId: str = None,
        modelVersionNumber: str = None,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeModelVersionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.describe_model_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#describe-model-versions)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#generate-presigned-url)
        """

    def get_batch_prediction_jobs(
        self, jobId: str = None, maxResults: int = None, nextToken: str = None
    ) -> GetBatchPredictionJobsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.get_batch_prediction_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get-batch-prediction-jobs)
        """

    def get_detector_version(
        self, detectorId: str, detectorVersionId: str
    ) -> GetDetectorVersionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.get_detector_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get-detector-version)
        """

    def get_detectors(
        self, detectorId: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetDetectorsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.get_detectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get-detectors)
        """

    def get_entity_types(
        self, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetEntityTypesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.get_entity_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get-entity-types)
        """

    def get_event_prediction(
        self,
        detectorId: str,
        eventId: str,
        eventTypeName: str,
        entities: List[EntityTypeDef],
        eventTimestamp: str,
        eventVariables: Dict[str, str],
        detectorVersionId: str = None,
        externalModelEndpointDataBlobs: Dict[str, ModelEndpointDataBlobTypeDef] = None,
    ) -> GetEventPredictionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.get_event_prediction)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get-event-prediction)
        """

    def get_event_types(
        self, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetEventTypesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.get_event_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get-event-types)
        """

    def get_external_models(
        self, modelEndpoint: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetExternalModelsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.get_external_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get-external-models)
        """

    def get_kms_encryption_key(self) -> GetKMSEncryptionKeyResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.get_kms_encryption_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get-kms-encryption-key)
        """

    def get_labels(
        self, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetLabelsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.get_labels)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get-labels)
        """

    def get_model_version(
        self, modelId: str, modelType: Literal["ONLINE_FRAUD_INSIGHTS"], modelVersionNumber: str
    ) -> GetModelVersionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.get_model_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get-model-version)
        """

    def get_models(
        self,
        modelId: str = None,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetModelsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.get_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get-models)
        """

    def get_outcomes(
        self, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetOutcomesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.get_outcomes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get-outcomes)
        """

    def get_rules(
        self,
        detectorId: str,
        ruleId: str = None,
        ruleVersion: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> GetRulesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.get_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get-rules)
        """

    def get_variables(
        self, name: str = None, nextToken: str = None, maxResults: int = None
    ) -> GetVariablesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.get_variables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#get-variables)
        """

    def list_tags_for_resource(
        self, resourceARN: str, nextToken: str = None, maxResults: int = None
    ) -> ListTagsForResourceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#list-tags-for-resource)
        """

    def put_detector(
        self,
        detectorId: str,
        eventTypeName: str,
        description: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.put_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#put-detector)
        """

    def put_entity_type(
        self, name: str, description: str = None, tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.put_entity_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#put-entity-type)
        """

    def put_event_type(
        self,
        name: str,
        eventVariables: List[str],
        entityTypes: List[str],
        description: str = None,
        labels: List[str] = None,
        tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.put_event_type)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#put-event-type)
        """

    def put_external_model(
        self,
        modelEndpoint: str,
        modelSource: Literal["SAGEMAKER"],
        invokeModelEndpointRoleArn: str,
        inputConfiguration: "ModelInputConfigurationTypeDef",
        outputConfiguration: "ModelOutputConfigurationTypeDef",
        modelEndpointStatus: ModelEndpointStatus,
        tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.put_external_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#put-external-model)
        """

    def put_kms_encryption_key(self, kmsEncryptionKeyArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.put_kms_encryption_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#put-kms-encryption-key)
        """

    def put_label(
        self, name: str, description: str = None, tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.put_label)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#put-label)
        """

    def put_outcome(
        self, name: str, description: str = None, tags: List["TagTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.put_outcome)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#put-outcome)
        """

    def tag_resource(self, resourceARN: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#tag-resource)
        """

    def untag_resource(self, resourceARN: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#untag-resource)
        """

    def update_detector_version(
        self,
        detectorId: str,
        detectorVersionId: str,
        externalModelEndpoints: List[str],
        rules: List["RuleTypeDef"],
        description: str = None,
        modelVersions: List["ModelVersionTypeDef"] = None,
        ruleExecutionMode: RuleExecutionMode = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.update_detector_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update-detector-version)
        """

    def update_detector_version_metadata(
        self, detectorId: str, detectorVersionId: str, description: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.update_detector_version_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update-detector-version-metadata)
        """

    def update_detector_version_status(
        self, detectorId: str, detectorVersionId: str, status: DetectorVersionStatus
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.update_detector_version_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update-detector-version-status)
        """

    def update_model(
        self, modelId: str, modelType: Literal["ONLINE_FRAUD_INSIGHTS"], description: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.update_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update-model)
        """

    def update_model_version(
        self,
        modelId: str,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"],
        majorVersionNumber: str,
        externalEventsDetail: "ExternalEventsDetailTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> UpdateModelVersionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.update_model_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update-model-version)
        """

    def update_model_version_status(
        self,
        modelId: str,
        modelType: Literal["ONLINE_FRAUD_INSIGHTS"],
        modelVersionNumber: str,
        status: ModelVersionStatus,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.update_model_version_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update-model-version-status)
        """

    def update_rule_metadata(self, rule: "RuleTypeDef", description: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.update_rule_metadata)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update-rule-metadata)
        """

    def update_rule_version(
        self,
        rule: "RuleTypeDef",
        expression: str,
        language: Literal["DETECTORPL"],
        outcomes: List[str],
        description: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> UpdateRuleVersionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.update_rule_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update-rule-version)
        """

    def update_variable(
        self, name: str, defaultValue: str = None, description: str = None, variableType: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/frauddetector.html#FraudDetector.Client.update_variable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/client.html#update-variable)
        """
