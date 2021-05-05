"""
Type annotations for machinelearning service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/type_defs.html)

Usage::

    ```python
    from mypy_boto3_machinelearning.type_defs import AddTagsOutputTypeDef

    data: AddTagsOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_machinelearning.literals import (
    DetailsAttributes,
    EntityStatus,
    MLModelType,
    RealtimeEndpointStatus,
    TaggableResourceType,
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
    "AddTagsOutputTypeDef",
    "BatchPredictionTypeDef",
    "CreateBatchPredictionOutputTypeDef",
    "CreateDataSourceFromRDSOutputTypeDef",
    "CreateDataSourceFromRedshiftOutputTypeDef",
    "CreateDataSourceFromS3OutputTypeDef",
    "CreateEvaluationOutputTypeDef",
    "CreateMLModelOutputTypeDef",
    "CreateRealtimeEndpointOutputTypeDef",
    "DataSourceTypeDef",
    "DeleteBatchPredictionOutputTypeDef",
    "DeleteDataSourceOutputTypeDef",
    "DeleteEvaluationOutputTypeDef",
    "DeleteMLModelOutputTypeDef",
    "DeleteRealtimeEndpointOutputTypeDef",
    "DeleteTagsOutputTypeDef",
    "DescribeBatchPredictionsOutputTypeDef",
    "DescribeDataSourcesOutputTypeDef",
    "DescribeEvaluationsOutputTypeDef",
    "DescribeMLModelsOutputTypeDef",
    "DescribeTagsOutputTypeDef",
    "EvaluationTypeDef",
    "GetBatchPredictionOutputTypeDef",
    "GetDataSourceOutputTypeDef",
    "GetEvaluationOutputTypeDef",
    "GetMLModelOutputTypeDef",
    "MLModelTypeDef",
    "PaginatorConfigTypeDef",
    "PerformanceMetricsTypeDef",
    "PredictOutputTypeDef",
    "PredictionTypeDef",
    "RDSDataSpecTypeDef",
    "RDSDatabaseCredentialsTypeDef",
    "RDSDatabaseTypeDef",
    "RDSMetadataTypeDef",
    "RealtimeEndpointInfoTypeDef",
    "RedshiftDataSpecTypeDef",
    "RedshiftDatabaseCredentialsTypeDef",
    "RedshiftDatabaseTypeDef",
    "RedshiftMetadataTypeDef",
    "ResponseMetadata",
    "S3DataSpecTypeDef",
    "TagTypeDef",
    "UpdateBatchPredictionOutputTypeDef",
    "UpdateDataSourceOutputTypeDef",
    "UpdateEvaluationOutputTypeDef",
    "UpdateMLModelOutputTypeDef",
    "WaiterConfigTypeDef",
)


class AddTagsOutputTypeDef(TypedDict):
    ResourceId: str
    ResourceType: TaggableResourceType
    ResponseMetadata: "ResponseMetadata"


class BatchPredictionTypeDef(TypedDict, total=False):
    BatchPredictionId: str
    MLModelId: str
    BatchPredictionDataSourceId: str
    InputDataLocationS3: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Name: str
    Status: EntityStatus
    OutputUri: str
    Message: str
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime
    TotalRecordCount: int
    InvalidRecordCount: int


class CreateBatchPredictionOutputTypeDef(TypedDict):
    BatchPredictionId: str
    ResponseMetadata: "ResponseMetadata"


class CreateDataSourceFromRDSOutputTypeDef(TypedDict):
    DataSourceId: str
    ResponseMetadata: "ResponseMetadata"


class CreateDataSourceFromRedshiftOutputTypeDef(TypedDict):
    DataSourceId: str
    ResponseMetadata: "ResponseMetadata"


class CreateDataSourceFromS3OutputTypeDef(TypedDict):
    DataSourceId: str
    ResponseMetadata: "ResponseMetadata"


class CreateEvaluationOutputTypeDef(TypedDict):
    EvaluationId: str
    ResponseMetadata: "ResponseMetadata"


class CreateMLModelOutputTypeDef(TypedDict):
    MLModelId: str
    ResponseMetadata: "ResponseMetadata"


class CreateRealtimeEndpointOutputTypeDef(TypedDict):
    MLModelId: str
    RealtimeEndpointInfo: "RealtimeEndpointInfoTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DataSourceTypeDef(TypedDict, total=False):
    DataSourceId: str
    DataLocationS3: str
    DataRearrangement: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    DataSizeInBytes: int
    NumberOfFiles: int
    Name: str
    Status: EntityStatus
    Message: str
    RedshiftMetadata: "RedshiftMetadataTypeDef"
    RDSMetadata: "RDSMetadataTypeDef"
    RoleARN: str
    ComputeStatistics: bool
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime


class DeleteBatchPredictionOutputTypeDef(TypedDict):
    BatchPredictionId: str
    ResponseMetadata: "ResponseMetadata"


class DeleteDataSourceOutputTypeDef(TypedDict):
    DataSourceId: str
    ResponseMetadata: "ResponseMetadata"


class DeleteEvaluationOutputTypeDef(TypedDict):
    EvaluationId: str
    ResponseMetadata: "ResponseMetadata"


class DeleteMLModelOutputTypeDef(TypedDict):
    MLModelId: str
    ResponseMetadata: "ResponseMetadata"


class DeleteRealtimeEndpointOutputTypeDef(TypedDict):
    MLModelId: str
    RealtimeEndpointInfo: "RealtimeEndpointInfoTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeleteTagsOutputTypeDef(TypedDict):
    ResourceId: str
    ResourceType: TaggableResourceType
    ResponseMetadata: "ResponseMetadata"


class DescribeBatchPredictionsOutputTypeDef(TypedDict):
    Results: List["BatchPredictionTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeDataSourcesOutputTypeDef(TypedDict):
    Results: List["DataSourceTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeEvaluationsOutputTypeDef(TypedDict):
    Results: List["EvaluationTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeMLModelsOutputTypeDef(TypedDict):
    Results: List["MLModelTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeTagsOutputTypeDef(TypedDict):
    ResourceId: str
    ResourceType: TaggableResourceType
    Tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class EvaluationTypeDef(TypedDict, total=False):
    EvaluationId: str
    MLModelId: str
    EvaluationDataSourceId: str
    InputDataLocationS3: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Name: str
    Status: EntityStatus
    PerformanceMetrics: "PerformanceMetricsTypeDef"
    Message: str
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime


class GetBatchPredictionOutputTypeDef(TypedDict):
    BatchPredictionId: str
    MLModelId: str
    BatchPredictionDataSourceId: str
    InputDataLocationS3: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Name: str
    Status: EntityStatus
    OutputUri: str
    LogUri: str
    Message: str
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime
    TotalRecordCount: int
    InvalidRecordCount: int
    ResponseMetadata: "ResponseMetadata"


class GetDataSourceOutputTypeDef(TypedDict):
    DataSourceId: str
    DataLocationS3: str
    DataRearrangement: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    DataSizeInBytes: int
    NumberOfFiles: int
    Name: str
    Status: EntityStatus
    LogUri: str
    Message: str
    RedshiftMetadata: "RedshiftMetadataTypeDef"
    RDSMetadata: "RDSMetadataTypeDef"
    RoleARN: str
    ComputeStatistics: bool
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime
    DataSourceSchema: str
    ResponseMetadata: "ResponseMetadata"


class GetEvaluationOutputTypeDef(TypedDict):
    EvaluationId: str
    MLModelId: str
    EvaluationDataSourceId: str
    InputDataLocationS3: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Name: str
    Status: EntityStatus
    PerformanceMetrics: "PerformanceMetricsTypeDef"
    LogUri: str
    Message: str
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime
    ResponseMetadata: "ResponseMetadata"


class GetMLModelOutputTypeDef(TypedDict):
    MLModelId: str
    TrainingDataSourceId: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Name: str
    Status: EntityStatus
    SizeInBytes: int
    EndpointInfo: "RealtimeEndpointInfoTypeDef"
    TrainingParameters: Dict[str, str]
    InputDataLocationS3: str
    MLModelType: MLModelType
    ScoreThreshold: float
    ScoreThresholdLastUpdatedAt: datetime
    LogUri: str
    Message: str
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime
    Recipe: str
    Schema: str
    ResponseMetadata: "ResponseMetadata"


class MLModelTypeDef(TypedDict, total=False):
    MLModelId: str
    TrainingDataSourceId: str
    CreatedByIamUser: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    Name: str
    Status: EntityStatus
    SizeInBytes: int
    EndpointInfo: "RealtimeEndpointInfoTypeDef"
    TrainingParameters: Dict[str, str]
    InputDataLocationS3: str
    Algorithm: Literal["sgd"]
    MLModelType: MLModelType
    ScoreThreshold: float
    ScoreThresholdLastUpdatedAt: datetime
    Message: str
    ComputeTime: int
    FinishedAt: datetime
    StartedAt: datetime


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PerformanceMetricsTypeDef(TypedDict, total=False):
    Properties: Dict[str, str]


class PredictOutputTypeDef(TypedDict):
    Prediction: "PredictionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class PredictionTypeDef(TypedDict, total=False):
    predictedLabel: str
    predictedValue: float
    predictedScores: Dict[str, float]
    details: Dict[DetailsAttributes, str]


class _RequiredRDSDataSpecTypeDef(TypedDict):
    DatabaseInformation: "RDSDatabaseTypeDef"
    SelectSqlQuery: str
    DatabaseCredentials: "RDSDatabaseCredentialsTypeDef"
    S3StagingLocation: str
    ResourceRole: str
    ServiceRole: str
    SubnetId: str
    SecurityGroupIds: List[str]


class RDSDataSpecTypeDef(_RequiredRDSDataSpecTypeDef, total=False):
    DataRearrangement: str
    DataSchema: str
    DataSchemaUri: str


class RDSDatabaseCredentialsTypeDef(TypedDict):
    Username: str
    Password: str


class RDSDatabaseTypeDef(TypedDict):
    InstanceIdentifier: str
    DatabaseName: str


class RDSMetadataTypeDef(TypedDict, total=False):
    Database: "RDSDatabaseTypeDef"
    DatabaseUserName: str
    SelectSqlQuery: str
    ResourceRole: str
    ServiceRole: str
    DataPipelineId: str


class RealtimeEndpointInfoTypeDef(TypedDict, total=False):
    PeakRequestsPerSecond: int
    CreatedAt: datetime
    EndpointUrl: str
    EndpointStatus: RealtimeEndpointStatus


class _RequiredRedshiftDataSpecTypeDef(TypedDict):
    DatabaseInformation: "RedshiftDatabaseTypeDef"
    SelectSqlQuery: str
    DatabaseCredentials: "RedshiftDatabaseCredentialsTypeDef"
    S3StagingLocation: str


class RedshiftDataSpecTypeDef(_RequiredRedshiftDataSpecTypeDef, total=False):
    DataRearrangement: str
    DataSchema: str
    DataSchemaUri: str


class RedshiftDatabaseCredentialsTypeDef(TypedDict):
    Username: str
    Password: str


class RedshiftDatabaseTypeDef(TypedDict):
    DatabaseName: str
    ClusterIdentifier: str


class RedshiftMetadataTypeDef(TypedDict, total=False):
    RedshiftDatabase: "RedshiftDatabaseTypeDef"
    DatabaseUserName: str
    SelectSqlQuery: str


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class _RequiredS3DataSpecTypeDef(TypedDict):
    DataLocationS3: str


class S3DataSpecTypeDef(_RequiredS3DataSpecTypeDef, total=False):
    DataRearrangement: str
    DataSchema: str
    DataSchemaLocationS3: str


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class UpdateBatchPredictionOutputTypeDef(TypedDict):
    BatchPredictionId: str
    ResponseMetadata: "ResponseMetadata"


class UpdateDataSourceOutputTypeDef(TypedDict):
    DataSourceId: str
    ResponseMetadata: "ResponseMetadata"


class UpdateEvaluationOutputTypeDef(TypedDict):
    EvaluationId: str
    ResponseMetadata: "ResponseMetadata"


class UpdateMLModelOutputTypeDef(TypedDict):
    MLModelId: str
    ResponseMetadata: "ResponseMetadata"


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
