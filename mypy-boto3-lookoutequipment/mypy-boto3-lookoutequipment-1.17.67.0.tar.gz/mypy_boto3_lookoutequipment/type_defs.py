"""
Type annotations for lookoutequipment service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lookoutequipment.type_defs import CreateDatasetResponseTypeDef

    data: CreateDatasetResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_lookoutequipment.literals import (
    DatasetStatus,
    DataUploadFrequency,
    InferenceExecutionStatus,
    InferenceSchedulerStatus,
    IngestionJobStatus,
    ModelStatus,
    TargetSamplingRate,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateDatasetResponseTypeDef",
    "CreateInferenceSchedulerResponseTypeDef",
    "CreateModelResponseTypeDef",
    "DataIngestionJobSummaryTypeDef",
    "DataPreProcessingConfigurationTypeDef",
    "DatasetSchemaTypeDef",
    "DatasetSummaryTypeDef",
    "DescribeDataIngestionJobResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeInferenceSchedulerResponseTypeDef",
    "DescribeModelResponseTypeDef",
    "InferenceExecutionSummaryTypeDef",
    "InferenceInputConfigurationTypeDef",
    "InferenceInputNameConfigurationTypeDef",
    "InferenceOutputConfigurationTypeDef",
    "InferenceS3InputConfigurationTypeDef",
    "InferenceS3OutputConfigurationTypeDef",
    "InferenceSchedulerSummaryTypeDef",
    "IngestionInputConfigurationTypeDef",
    "IngestionS3InputConfigurationTypeDef",
    "LabelsInputConfigurationTypeDef",
    "LabelsS3InputConfigurationTypeDef",
    "ListDataIngestionJobsResponseTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListInferenceExecutionsResponseTypeDef",
    "ListInferenceSchedulersResponseTypeDef",
    "ListModelsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModelSummaryTypeDef",
    "S3ObjectTypeDef",
    "StartDataIngestionJobResponseTypeDef",
    "StartInferenceSchedulerResponseTypeDef",
    "StopInferenceSchedulerResponseTypeDef",
    "TagTypeDef",
)


class CreateDatasetResponseTypeDef(TypedDict, total=False):
    DatasetName: str
    DatasetArn: str
    Status: DatasetStatus


class CreateInferenceSchedulerResponseTypeDef(TypedDict, total=False):
    InferenceSchedulerArn: str
    InferenceSchedulerName: str
    Status: InferenceSchedulerStatus


class CreateModelResponseTypeDef(TypedDict, total=False):
    ModelArn: str
    Status: ModelStatus


class DataIngestionJobSummaryTypeDef(TypedDict, total=False):
    JobId: str
    DatasetName: str
    DatasetArn: str
    IngestionInputConfiguration: "IngestionInputConfigurationTypeDef"
    Status: IngestionJobStatus


class DataPreProcessingConfigurationTypeDef(TypedDict, total=False):
    TargetSamplingRate: TargetSamplingRate


class DatasetSchemaTypeDef(TypedDict, total=False):
    InlineDataSchema: str


class DatasetSummaryTypeDef(TypedDict, total=False):
    DatasetName: str
    DatasetArn: str
    Status: DatasetStatus
    CreatedAt: datetime


class DescribeDataIngestionJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    DatasetArn: str
    IngestionInputConfiguration: "IngestionInputConfigurationTypeDef"
    RoleArn: str
    CreatedAt: datetime
    Status: IngestionJobStatus
    FailedReason: str


class DescribeDatasetResponseTypeDef(TypedDict, total=False):
    DatasetName: str
    DatasetArn: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Status: DatasetStatus
    Schema: str
    ServerSideKmsKeyId: str
    IngestionInputConfiguration: "IngestionInputConfigurationTypeDef"


class DescribeInferenceSchedulerResponseTypeDef(TypedDict, total=False):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatus
    DataDelayOffsetInMinutes: int
    DataUploadFrequency: DataUploadFrequency
    CreatedAt: datetime
    UpdatedAt: datetime
    DataInputConfiguration: "InferenceInputConfigurationTypeDef"
    DataOutputConfiguration: "InferenceOutputConfigurationTypeDef"
    RoleArn: str
    ServerSideKmsKeyId: str


class DescribeModelResponseTypeDef(TypedDict, total=False):
    ModelName: str
    ModelArn: str
    DatasetName: str
    DatasetArn: str
    Schema: str
    LabelsInputConfiguration: "LabelsInputConfigurationTypeDef"
    TrainingDataStartTime: datetime
    TrainingDataEndTime: datetime
    EvaluationDataStartTime: datetime
    EvaluationDataEndTime: datetime
    RoleArn: str
    DataPreProcessingConfiguration: "DataPreProcessingConfigurationTypeDef"
    Status: ModelStatus
    TrainingExecutionStartTime: datetime
    TrainingExecutionEndTime: datetime
    FailedReason: str
    ModelMetrics: str
    LastUpdatedTime: datetime
    CreatedAt: datetime
    ServerSideKmsKeyId: str


class InferenceExecutionSummaryTypeDef(TypedDict, total=False):
    ModelName: str
    ModelArn: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    ScheduledStartTime: datetime
    DataStartTime: datetime
    DataEndTime: datetime
    DataInputConfiguration: "InferenceInputConfigurationTypeDef"
    DataOutputConfiguration: "InferenceOutputConfigurationTypeDef"
    CustomerResultObject: "S3ObjectTypeDef"
    Status: InferenceExecutionStatus
    FailedReason: str


class InferenceInputConfigurationTypeDef(TypedDict, total=False):
    S3InputConfiguration: "InferenceS3InputConfigurationTypeDef"
    InputTimeZoneOffset: str
    InferenceInputNameConfiguration: "InferenceInputNameConfigurationTypeDef"


class InferenceInputNameConfigurationTypeDef(TypedDict, total=False):
    TimestampFormat: str
    ComponentTimestampDelimiter: str


class _RequiredInferenceOutputConfigurationTypeDef(TypedDict):
    S3OutputConfiguration: "InferenceS3OutputConfigurationTypeDef"


class InferenceOutputConfigurationTypeDef(
    _RequiredInferenceOutputConfigurationTypeDef, total=False
):
    KmsKeyId: str


class _RequiredInferenceS3InputConfigurationTypeDef(TypedDict):
    Bucket: str


class InferenceS3InputConfigurationTypeDef(
    _RequiredInferenceS3InputConfigurationTypeDef, total=False
):
    Prefix: str


class _RequiredInferenceS3OutputConfigurationTypeDef(TypedDict):
    Bucket: str


class InferenceS3OutputConfigurationTypeDef(
    _RequiredInferenceS3OutputConfigurationTypeDef, total=False
):
    Prefix: str


class InferenceSchedulerSummaryTypeDef(TypedDict, total=False):
    ModelName: str
    ModelArn: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatus
    DataDelayOffsetInMinutes: int
    DataUploadFrequency: DataUploadFrequency


class IngestionInputConfigurationTypeDef(TypedDict):
    S3InputConfiguration: "IngestionS3InputConfigurationTypeDef"


class _RequiredIngestionS3InputConfigurationTypeDef(TypedDict):
    Bucket: str


class IngestionS3InputConfigurationTypeDef(
    _RequiredIngestionS3InputConfigurationTypeDef, total=False
):
    Prefix: str


class LabelsInputConfigurationTypeDef(TypedDict):
    S3InputConfiguration: "LabelsS3InputConfigurationTypeDef"


class _RequiredLabelsS3InputConfigurationTypeDef(TypedDict):
    Bucket: str


class LabelsS3InputConfigurationTypeDef(_RequiredLabelsS3InputConfigurationTypeDef, total=False):
    Prefix: str


class ListDataIngestionJobsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    DataIngestionJobSummaries: List["DataIngestionJobSummaryTypeDef"]


class ListDatasetsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    DatasetSummaries: List["DatasetSummaryTypeDef"]


class ListInferenceExecutionsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    InferenceExecutionSummaries: List["InferenceExecutionSummaryTypeDef"]


class ListInferenceSchedulersResponseTypeDef(TypedDict, total=False):
    NextToken: str
    InferenceSchedulerSummaries: List["InferenceSchedulerSummaryTypeDef"]


class ListModelsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    ModelSummaries: List["ModelSummaryTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class ModelSummaryTypeDef(TypedDict, total=False):
    ModelName: str
    ModelArn: str
    DatasetName: str
    DatasetArn: str
    Status: ModelStatus
    CreatedAt: datetime


class S3ObjectTypeDef(TypedDict):
    Bucket: str
    Key: str


class StartDataIngestionJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    Status: IngestionJobStatus


class StartInferenceSchedulerResponseTypeDef(TypedDict, total=False):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatus


class StopInferenceSchedulerResponseTypeDef(TypedDict, total=False):
    ModelArn: str
    ModelName: str
    InferenceSchedulerName: str
    InferenceSchedulerArn: str
    Status: InferenceSchedulerStatus


class TagTypeDef(TypedDict):
    Key: str
    Value: str
