"""
Type annotations for lookoutvision service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutvision/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lookoutvision.type_defs import CreateDatasetResponseTypeDef

    data: CreateDatasetResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_lookoutvision.literals import DatasetStatus, ModelHostingStatus, ModelStatus

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateDatasetResponseTypeDef",
    "CreateModelResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "DatasetDescriptionTypeDef",
    "DatasetGroundTruthManifestTypeDef",
    "DatasetImageStatsTypeDef",
    "DatasetMetadataTypeDef",
    "DatasetSourceTypeDef",
    "DeleteModelResponseTypeDef",
    "DeleteProjectResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeModelResponseTypeDef",
    "DescribeProjectResponseTypeDef",
    "DetectAnomaliesResponseTypeDef",
    "DetectAnomalyResultTypeDef",
    "ImageSourceTypeDef",
    "InputS3ObjectTypeDef",
    "ListDatasetEntriesResponseTypeDef",
    "ListModelsResponseTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModelDescriptionTypeDef",
    "ModelMetadataTypeDef",
    "ModelPerformanceTypeDef",
    "OutputConfigTypeDef",
    "OutputS3ObjectTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectMetadataTypeDef",
    "S3LocationTypeDef",
    "StartModelResponseTypeDef",
    "StopModelResponseTypeDef",
    "TagTypeDef",
    "UpdateDatasetEntriesResponseTypeDef",
)


class CreateDatasetResponseTypeDef(TypedDict, total=False):
    DatasetMetadata: "DatasetMetadataTypeDef"


class CreateModelResponseTypeDef(TypedDict, total=False):
    ModelMetadata: "ModelMetadataTypeDef"


class CreateProjectResponseTypeDef(TypedDict, total=False):
    ProjectMetadata: "ProjectMetadataTypeDef"


class DatasetDescriptionTypeDef(TypedDict, total=False):
    ProjectName: str
    DatasetType: str
    CreationTimestamp: datetime
    LastUpdatedTimestamp: datetime
    Status: DatasetStatus
    StatusMessage: str
    ImageStats: "DatasetImageStatsTypeDef"


class DatasetGroundTruthManifestTypeDef(TypedDict, total=False):
    S3Object: "InputS3ObjectTypeDef"


class DatasetImageStatsTypeDef(TypedDict, total=False):
    Total: int
    Labeled: int
    Normal: int
    Anomaly: int


class DatasetMetadataTypeDef(TypedDict, total=False):
    DatasetType: str
    CreationTimestamp: datetime
    Status: DatasetStatus
    StatusMessage: str


class DatasetSourceTypeDef(TypedDict, total=False):
    GroundTruthManifest: "DatasetGroundTruthManifestTypeDef"


class DeleteModelResponseTypeDef(TypedDict, total=False):
    ModelArn: str


class DeleteProjectResponseTypeDef(TypedDict, total=False):
    ProjectArn: str


class DescribeDatasetResponseTypeDef(TypedDict, total=False):
    DatasetDescription: "DatasetDescriptionTypeDef"


class DescribeModelResponseTypeDef(TypedDict, total=False):
    ModelDescription: "ModelDescriptionTypeDef"


class DescribeProjectResponseTypeDef(TypedDict, total=False):
    ProjectDescription: "ProjectDescriptionTypeDef"


class DetectAnomaliesResponseTypeDef(TypedDict, total=False):
    DetectAnomalyResult: "DetectAnomalyResultTypeDef"


class DetectAnomalyResultTypeDef(TypedDict, total=False):
    Source: "ImageSourceTypeDef"
    IsAnomalous: bool
    Confidence: float


ImageSourceTypeDef = TypedDict("ImageSourceTypeDef", {"Type": str}, total=False)


class _RequiredInputS3ObjectTypeDef(TypedDict):
    Bucket: str
    Key: str


class InputS3ObjectTypeDef(_RequiredInputS3ObjectTypeDef, total=False):
    VersionId: str


class ListDatasetEntriesResponseTypeDef(TypedDict, total=False):
    DatasetEntries: List[str]
    NextToken: str


class ListModelsResponseTypeDef(TypedDict, total=False):
    Models: List["ModelMetadataTypeDef"]
    NextToken: str


class ListProjectsResponseTypeDef(TypedDict, total=False):
    Projects: List["ProjectMetadataTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class ModelDescriptionTypeDef(TypedDict, total=False):
    ModelVersion: str
    ModelArn: str
    CreationTimestamp: datetime
    Description: str
    Status: ModelStatus
    StatusMessage: str
    Performance: "ModelPerformanceTypeDef"
    OutputConfig: "OutputConfigTypeDef"
    EvaluationManifest: "OutputS3ObjectTypeDef"
    EvaluationResult: "OutputS3ObjectTypeDef"
    EvaluationEndTimestamp: datetime
    KmsKeyId: str


class ModelMetadataTypeDef(TypedDict, total=False):
    CreationTimestamp: datetime
    ModelVersion: str
    ModelArn: str
    Description: str
    Status: ModelStatus
    StatusMessage: str
    Performance: "ModelPerformanceTypeDef"


class ModelPerformanceTypeDef(TypedDict, total=False):
    F1Score: float
    Recall: float
    Precision: float


class OutputConfigTypeDef(TypedDict):
    S3Location: "S3LocationTypeDef"


class OutputS3ObjectTypeDef(TypedDict):
    Bucket: str
    Key: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ProjectDescriptionTypeDef(TypedDict, total=False):
    ProjectArn: str
    ProjectName: str
    CreationTimestamp: datetime
    Datasets: List["DatasetMetadataTypeDef"]


class ProjectMetadataTypeDef(TypedDict, total=False):
    ProjectArn: str
    ProjectName: str
    CreationTimestamp: datetime


class _RequiredS3LocationTypeDef(TypedDict):
    Bucket: str


class S3LocationTypeDef(_RequiredS3LocationTypeDef, total=False):
    Prefix: str


class StartModelResponseTypeDef(TypedDict, total=False):
    Status: ModelHostingStatus


class StopModelResponseTypeDef(TypedDict, total=False):
    Status: ModelHostingStatus


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class UpdateDatasetEntriesResponseTypeDef(TypedDict, total=False):
    Status: DatasetStatus
