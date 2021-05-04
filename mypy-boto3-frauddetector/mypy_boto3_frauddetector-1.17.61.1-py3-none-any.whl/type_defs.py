"""
Type annotations for frauddetector service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/type_defs.html)

Usage::

    ```python
    from mypy_boto3_frauddetector.type_defs import BatchCreateVariableErrorTypeDef

    data: BatchCreateVariableErrorTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, List, Union

from mypy_boto3_frauddetector.literals import (
    AsyncJobStatus,
    DataSource,
    DataType,
    DetectorVersionStatus,
    ModelEndpointStatus,
    ModelInputDataFormat,
    ModelOutputDataFormat,
    RuleExecutionMode,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchCreateVariableErrorTypeDef",
    "BatchCreateVariableResultTypeDef",
    "BatchGetVariableErrorTypeDef",
    "BatchGetVariableResultTypeDef",
    "BatchPredictionTypeDef",
    "CreateDetectorVersionResultTypeDef",
    "CreateModelVersionResultTypeDef",
    "CreateRuleResultTypeDef",
    "DataValidationMetricsTypeDef",
    "DescribeDetectorResultTypeDef",
    "DescribeModelVersionsResultTypeDef",
    "DetectorTypeDef",
    "DetectorVersionSummaryTypeDef",
    "EntityTypeDef",
    "EntityTypeTypeDef",
    "EventTypeTypeDef",
    "ExternalEventsDetailTypeDef",
    "ExternalModelTypeDef",
    "FieldValidationMessageTypeDef",
    "FileValidationMessageTypeDef",
    "GetBatchPredictionJobsResultTypeDef",
    "GetDetectorVersionResultTypeDef",
    "GetDetectorsResultTypeDef",
    "GetEntityTypesResultTypeDef",
    "GetEventPredictionResultTypeDef",
    "GetEventTypesResultTypeDef",
    "GetExternalModelsResultTypeDef",
    "GetKMSEncryptionKeyResultTypeDef",
    "GetLabelsResultTypeDef",
    "GetModelVersionResultTypeDef",
    "GetModelsResultTypeDef",
    "GetOutcomesResultTypeDef",
    "GetRulesResultTypeDef",
    "GetVariablesResultTypeDef",
    "KMSKeyTypeDef",
    "LabelSchemaTypeDef",
    "LabelTypeDef",
    "ListTagsForResourceResultTypeDef",
    "MetricDataPointTypeDef",
    "ModelEndpointDataBlobTypeDef",
    "ModelInputConfigurationTypeDef",
    "ModelOutputConfigurationTypeDef",
    "ModelScoresTypeDef",
    "ModelTypeDef",
    "ModelVersionDetailTypeDef",
    "ModelVersionTypeDef",
    "OutcomeTypeDef",
    "RuleDetailTypeDef",
    "RuleResultTypeDef",
    "RuleTypeDef",
    "TagTypeDef",
    "TrainingDataSchemaTypeDef",
    "TrainingMetricsTypeDef",
    "TrainingResultTypeDef",
    "UpdateModelVersionResultTypeDef",
    "UpdateRuleVersionResultTypeDef",
    "VariableEntryTypeDef",
    "VariableTypeDef",
)


class BatchCreateVariableErrorTypeDef(TypedDict, total=False):
    name: str
    code: int
    message: str


class BatchCreateVariableResultTypeDef(TypedDict, total=False):
    errors: List["BatchCreateVariableErrorTypeDef"]


class BatchGetVariableErrorTypeDef(TypedDict, total=False):
    name: str
    code: int
    message: str


class BatchGetVariableResultTypeDef(TypedDict, total=False):
    variables: List["VariableTypeDef"]
    errors: List["BatchGetVariableErrorTypeDef"]


class BatchPredictionTypeDef(TypedDict, total=False):
    jobId: str
    status: AsyncJobStatus
    failureReason: str
    startTime: str
    completionTime: str
    lastHeartbeatTime: str
    inputPath: str
    outputPath: str
    eventTypeName: str
    detectorName: str
    detectorVersion: str
    iamRoleArn: str
    arn: str
    processedRecordsCount: int
    totalRecordsCount: int


class CreateDetectorVersionResultTypeDef(TypedDict, total=False):
    detectorId: str
    detectorVersionId: str
    status: DetectorVersionStatus


class CreateModelVersionResultTypeDef(TypedDict, total=False):
    modelId: str
    modelType: Literal["ONLINE_FRAUD_INSIGHTS"]
    modelVersionNumber: str
    status: str


class CreateRuleResultTypeDef(TypedDict, total=False):
    rule: "RuleTypeDef"


class DataValidationMetricsTypeDef(TypedDict, total=False):
    fileLevelMessages: List["FileValidationMessageTypeDef"]
    fieldLevelMessages: List["FieldValidationMessageTypeDef"]


class DescribeDetectorResultTypeDef(TypedDict, total=False):
    detectorId: str
    detectorVersionSummaries: List["DetectorVersionSummaryTypeDef"]
    nextToken: str
    arn: str


class DescribeModelVersionsResultTypeDef(TypedDict, total=False):
    modelVersionDetails: List["ModelVersionDetailTypeDef"]
    nextToken: str


class DetectorTypeDef(TypedDict, total=False):
    detectorId: str
    description: str
    eventTypeName: str
    lastUpdatedTime: str
    createdTime: str
    arn: str


class DetectorVersionSummaryTypeDef(TypedDict, total=False):
    detectorVersionId: str
    status: DetectorVersionStatus
    description: str
    lastUpdatedTime: str


class EntityTypeDef(TypedDict):
    entityType: str
    entityId: str


class EntityTypeTypeDef(TypedDict, total=False):
    name: str
    description: str
    lastUpdatedTime: str
    createdTime: str
    arn: str


class EventTypeTypeDef(TypedDict, total=False):
    name: str
    description: str
    eventVariables: List[str]
    labels: List[str]
    entityTypes: List[str]
    lastUpdatedTime: str
    createdTime: str
    arn: str


class ExternalEventsDetailTypeDef(TypedDict):
    dataLocation: str
    dataAccessRoleArn: str


class ExternalModelTypeDef(TypedDict, total=False):
    modelEndpoint: str
    modelSource: Literal["SAGEMAKER"]
    invokeModelEndpointRoleArn: str
    inputConfiguration: "ModelInputConfigurationTypeDef"
    outputConfiguration: "ModelOutputConfigurationTypeDef"
    modelEndpointStatus: ModelEndpointStatus
    lastUpdatedTime: str
    createdTime: str
    arn: str


FieldValidationMessageTypeDef = TypedDict(
    "FieldValidationMessageTypeDef",
    {"fieldName": str, "identifier": str, "title": str, "content": str, "type": str},
    total=False,
)

FileValidationMessageTypeDef = TypedDict(
    "FileValidationMessageTypeDef", {"title": str, "content": str, "type": str}, total=False
)


class GetBatchPredictionJobsResultTypeDef(TypedDict, total=False):
    batchPredictions: List["BatchPredictionTypeDef"]
    nextToken: str


class GetDetectorVersionResultTypeDef(TypedDict, total=False):
    detectorId: str
    detectorVersionId: str
    description: str
    externalModelEndpoints: List[str]
    modelVersions: List["ModelVersionTypeDef"]
    rules: List["RuleTypeDef"]
    status: DetectorVersionStatus
    lastUpdatedTime: str
    createdTime: str
    ruleExecutionMode: RuleExecutionMode
    arn: str


class GetDetectorsResultTypeDef(TypedDict, total=False):
    detectors: List["DetectorTypeDef"]
    nextToken: str


class GetEntityTypesResultTypeDef(TypedDict, total=False):
    entityTypes: List["EntityTypeTypeDef"]
    nextToken: str


class GetEventPredictionResultTypeDef(TypedDict, total=False):
    modelScores: List["ModelScoresTypeDef"]
    ruleResults: List["RuleResultTypeDef"]


class GetEventTypesResultTypeDef(TypedDict, total=False):
    eventTypes: List["EventTypeTypeDef"]
    nextToken: str


class GetExternalModelsResultTypeDef(TypedDict, total=False):
    externalModels: List["ExternalModelTypeDef"]
    nextToken: str


class GetKMSEncryptionKeyResultTypeDef(TypedDict, total=False):
    kmsKey: "KMSKeyTypeDef"


class GetLabelsResultTypeDef(TypedDict, total=False):
    labels: List["LabelTypeDef"]
    nextToken: str


class GetModelVersionResultTypeDef(TypedDict, total=False):
    modelId: str
    modelType: Literal["ONLINE_FRAUD_INSIGHTS"]
    modelVersionNumber: str
    trainingDataSource: Literal["EXTERNAL_EVENTS"]
    trainingDataSchema: "TrainingDataSchemaTypeDef"
    externalEventsDetail: "ExternalEventsDetailTypeDef"
    status: str
    arn: str


class GetModelsResultTypeDef(TypedDict, total=False):
    nextToken: str
    models: List["ModelTypeDef"]


class GetOutcomesResultTypeDef(TypedDict, total=False):
    outcomes: List["OutcomeTypeDef"]
    nextToken: str


class GetRulesResultTypeDef(TypedDict, total=False):
    ruleDetails: List["RuleDetailTypeDef"]
    nextToken: str


class GetVariablesResultTypeDef(TypedDict, total=False):
    variables: List["VariableTypeDef"]
    nextToken: str


class KMSKeyTypeDef(TypedDict, total=False):
    kmsEncryptionKeyArn: str


class LabelSchemaTypeDef(TypedDict):
    labelMapper: Dict[str, List[str]]


class LabelTypeDef(TypedDict, total=False):
    name: str
    description: str
    lastUpdatedTime: str
    createdTime: str
    arn: str


class ListTagsForResourceResultTypeDef(TypedDict, total=False):
    tags: List["TagTypeDef"]
    nextToken: str


class MetricDataPointTypeDef(TypedDict, total=False):
    fpr: float
    precision: float
    tpr: float
    threshold: float


class ModelEndpointDataBlobTypeDef(TypedDict, total=False):
    byteBuffer: Union[bytes, IO[bytes]]
    contentType: str


_RequiredModelInputConfigurationTypeDef = TypedDict(
    "_RequiredModelInputConfigurationTypeDef", {"useEventVariables": bool}
)
_OptionalModelInputConfigurationTypeDef = TypedDict(
    "_OptionalModelInputConfigurationTypeDef",
    {
        "eventTypeName": str,
        "format": ModelInputDataFormat,
        "jsonInputTemplate": str,
        "csvInputTemplate": str,
    },
    total=False,
)


class ModelInputConfigurationTypeDef(
    _RequiredModelInputConfigurationTypeDef, _OptionalModelInputConfigurationTypeDef
):
    pass


_RequiredModelOutputConfigurationTypeDef = TypedDict(
    "_RequiredModelOutputConfigurationTypeDef", {"format": ModelOutputDataFormat}
)
_OptionalModelOutputConfigurationTypeDef = TypedDict(
    "_OptionalModelOutputConfigurationTypeDef",
    {"jsonKeyToVariableMap": Dict[str, str], "csvIndexToVariableMap": Dict[str, str]},
    total=False,
)


class ModelOutputConfigurationTypeDef(
    _RequiredModelOutputConfigurationTypeDef, _OptionalModelOutputConfigurationTypeDef
):
    pass


class ModelScoresTypeDef(TypedDict, total=False):
    modelVersion: "ModelVersionTypeDef"
    scores: Dict[str, float]


class ModelTypeDef(TypedDict, total=False):
    modelId: str
    modelType: Literal["ONLINE_FRAUD_INSIGHTS"]
    description: str
    eventTypeName: str
    createdTime: str
    lastUpdatedTime: str
    arn: str


class ModelVersionDetailTypeDef(TypedDict, total=False):
    modelId: str
    modelType: Literal["ONLINE_FRAUD_INSIGHTS"]
    modelVersionNumber: str
    status: str
    trainingDataSource: Literal["EXTERNAL_EVENTS"]
    trainingDataSchema: "TrainingDataSchemaTypeDef"
    externalEventsDetail: "ExternalEventsDetailTypeDef"
    trainingResult: "TrainingResultTypeDef"
    lastUpdatedTime: str
    createdTime: str
    arn: str


class _RequiredModelVersionTypeDef(TypedDict):
    modelId: str
    modelType: Literal["ONLINE_FRAUD_INSIGHTS"]
    modelVersionNumber: str


class ModelVersionTypeDef(_RequiredModelVersionTypeDef, total=False):
    arn: str


class OutcomeTypeDef(TypedDict, total=False):
    name: str
    description: str
    lastUpdatedTime: str
    createdTime: str
    arn: str


class RuleDetailTypeDef(TypedDict, total=False):
    ruleId: str
    description: str
    detectorId: str
    ruleVersion: str
    expression: str
    language: Literal["DETECTORPL"]
    outcomes: List[str]
    lastUpdatedTime: str
    createdTime: str
    arn: str


class RuleResultTypeDef(TypedDict, total=False):
    ruleId: str
    outcomes: List[str]


class RuleTypeDef(TypedDict):
    detectorId: str
    ruleId: str
    ruleVersion: str


class TagTypeDef(TypedDict):
    key: str
    value: str


class TrainingDataSchemaTypeDef(TypedDict):
    modelVariables: List[str]
    labelSchema: "LabelSchemaTypeDef"


class TrainingMetricsTypeDef(TypedDict, total=False):
    auc: float
    metricDataPoints: List["MetricDataPointTypeDef"]


class TrainingResultTypeDef(TypedDict, total=False):
    dataValidationMetrics: "DataValidationMetricsTypeDef"
    trainingMetrics: "TrainingMetricsTypeDef"


class UpdateModelVersionResultTypeDef(TypedDict, total=False):
    modelId: str
    modelType: Literal["ONLINE_FRAUD_INSIGHTS"]
    modelVersionNumber: str
    status: str


class UpdateRuleVersionResultTypeDef(TypedDict, total=False):
    rule: "RuleTypeDef"


class VariableEntryTypeDef(TypedDict, total=False):
    name: str
    dataType: str
    dataSource: str
    defaultValue: str
    description: str
    variableType: str


class VariableTypeDef(TypedDict, total=False):
    name: str
    dataType: DataType
    dataSource: DataSource
    defaultValue: str
    description: str
    variableType: str
    lastUpdatedTime: str
    createdTime: str
    arn: str
