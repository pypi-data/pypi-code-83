"""
Type annotations for forecast service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/type_defs.html)

Usage::

    ```python
    from mypy_boto3_forecast.type_defs import CategoricalParameterRangeTypeDef

    data: CategoricalParameterRangeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_forecast.literals import (
    AttributeType,
    DatasetType,
    Domain,
    EvaluationType,
    FilterConditionString,
    ScalingType,
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
    "CategoricalParameterRangeTypeDef",
    "ContinuousParameterRangeTypeDef",
    "CreateDatasetGroupResponseTypeDef",
    "CreateDatasetImportJobResponseTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateForecastExportJobResponseTypeDef",
    "CreateForecastResponseTypeDef",
    "CreatePredictorBacktestExportJobResponseTypeDef",
    "CreatePredictorResponseTypeDef",
    "DataDestinationTypeDef",
    "DataSourceTypeDef",
    "DatasetGroupSummaryTypeDef",
    "DatasetImportJobSummaryTypeDef",
    "DatasetSummaryTypeDef",
    "DescribeDatasetGroupResponseTypeDef",
    "DescribeDatasetImportJobResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeForecastExportJobResponseTypeDef",
    "DescribeForecastResponseTypeDef",
    "DescribePredictorBacktestExportJobResponseTypeDef",
    "DescribePredictorResponseTypeDef",
    "EncryptionConfigTypeDef",
    "ErrorMetricTypeDef",
    "EvaluationParametersTypeDef",
    "EvaluationResultTypeDef",
    "FeaturizationConfigTypeDef",
    "FeaturizationMethodTypeDef",
    "FeaturizationTypeDef",
    "FilterTypeDef",
    "ForecastExportJobSummaryTypeDef",
    "ForecastSummaryTypeDef",
    "GetAccuracyMetricsResponseTypeDef",
    "HyperParameterTuningJobConfigTypeDef",
    "InputDataConfigTypeDef",
    "IntegerParameterRangeTypeDef",
    "ListDatasetGroupsResponseTypeDef",
    "ListDatasetImportJobsResponseTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListForecastExportJobsResponseTypeDef",
    "ListForecastsResponseTypeDef",
    "ListPredictorBacktestExportJobsResponseTypeDef",
    "ListPredictorsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricsTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterRangesTypeDef",
    "PredictorBacktestExportJobSummaryTypeDef",
    "PredictorExecutionDetailsTypeDef",
    "PredictorExecutionTypeDef",
    "PredictorSummaryTypeDef",
    "S3ConfigTypeDef",
    "SchemaAttributeTypeDef",
    "SchemaTypeDef",
    "StatisticsTypeDef",
    "SupplementaryFeatureTypeDef",
    "TagTypeDef",
    "TestWindowSummaryTypeDef",
    "WeightedQuantileLossTypeDef",
    "WindowSummaryTypeDef",
)


class CategoricalParameterRangeTypeDef(TypedDict):
    Name: str
    Values: List[str]


class _RequiredContinuousParameterRangeTypeDef(TypedDict):
    Name: str
    MaxValue: float
    MinValue: float


class ContinuousParameterRangeTypeDef(_RequiredContinuousParameterRangeTypeDef, total=False):
    ScalingType: ScalingType


class CreateDatasetGroupResponseTypeDef(TypedDict, total=False):
    DatasetGroupArn: str


class CreateDatasetImportJobResponseTypeDef(TypedDict, total=False):
    DatasetImportJobArn: str


class CreateDatasetResponseTypeDef(TypedDict, total=False):
    DatasetArn: str


class CreateForecastExportJobResponseTypeDef(TypedDict, total=False):
    ForecastExportJobArn: str


class CreateForecastResponseTypeDef(TypedDict, total=False):
    ForecastArn: str


class CreatePredictorBacktestExportJobResponseTypeDef(TypedDict, total=False):
    PredictorBacktestExportJobArn: str


class CreatePredictorResponseTypeDef(TypedDict, total=False):
    PredictorArn: str


class DataDestinationTypeDef(TypedDict):
    S3Config: "S3ConfigTypeDef"


class DataSourceTypeDef(TypedDict):
    S3Config: "S3ConfigTypeDef"


class DatasetGroupSummaryTypeDef(TypedDict, total=False):
    DatasetGroupArn: str
    DatasetGroupName: str
    CreationTime: datetime
    LastModificationTime: datetime


class DatasetImportJobSummaryTypeDef(TypedDict, total=False):
    DatasetImportJobArn: str
    DatasetImportJobName: str
    DataSource: "DataSourceTypeDef"
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime


class DatasetSummaryTypeDef(TypedDict, total=False):
    DatasetArn: str
    DatasetName: str
    DatasetType: DatasetType
    Domain: Domain
    CreationTime: datetime
    LastModificationTime: datetime


class DescribeDatasetGroupResponseTypeDef(TypedDict, total=False):
    DatasetGroupName: str
    DatasetGroupArn: str
    DatasetArns: List[str]
    Domain: Domain
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime


class DescribeDatasetImportJobResponseTypeDef(TypedDict, total=False):
    DatasetImportJobName: str
    DatasetImportJobArn: str
    DatasetArn: str
    TimestampFormat: str
    TimeZone: str
    UseGeolocationForTimeZone: bool
    GeolocationFormat: str
    DataSource: "DataSourceTypeDef"
    EstimatedTimeRemainingInMinutes: int
    FieldStatistics: Dict[str, "StatisticsTypeDef"]
    DataSize: float
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime


class DescribeDatasetResponseTypeDef(TypedDict, total=False):
    DatasetArn: str
    DatasetName: str
    Domain: Domain
    DatasetType: DatasetType
    DataFrequency: str
    Schema: "SchemaTypeDef"
    EncryptionConfig: "EncryptionConfigTypeDef"
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime


class DescribeForecastExportJobResponseTypeDef(TypedDict, total=False):
    ForecastExportJobArn: str
    ForecastExportJobName: str
    ForecastArn: str
    Destination: "DataDestinationTypeDef"
    Message: str
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime


class DescribeForecastResponseTypeDef(TypedDict, total=False):
    ForecastArn: str
    ForecastName: str
    ForecastTypes: List[str]
    PredictorArn: str
    DatasetGroupArn: str
    EstimatedTimeRemainingInMinutes: int
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime


class DescribePredictorBacktestExportJobResponseTypeDef(TypedDict, total=False):
    PredictorBacktestExportJobArn: str
    PredictorBacktestExportJobName: str
    PredictorArn: str
    Destination: "DataDestinationTypeDef"
    Message: str
    Status: str
    CreationTime: datetime
    LastModificationTime: datetime


class DescribePredictorResponseTypeDef(TypedDict, total=False):
    PredictorArn: str
    PredictorName: str
    AlgorithmArn: str
    ForecastHorizon: int
    ForecastTypes: List[str]
    PerformAutoML: bool
    PerformHPO: bool
    TrainingParameters: Dict[str, str]
    EvaluationParameters: "EvaluationParametersTypeDef"
    HPOConfig: "HyperParameterTuningJobConfigTypeDef"
    InputDataConfig: "InputDataConfigTypeDef"
    FeaturizationConfig: "FeaturizationConfigTypeDef"
    EncryptionConfig: "EncryptionConfigTypeDef"
    PredictorExecutionDetails: "PredictorExecutionDetailsTypeDef"
    EstimatedTimeRemainingInMinutes: int
    DatasetImportJobArns: List[str]
    AutoMLAlgorithmArns: List[str]
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime


class EncryptionConfigTypeDef(TypedDict):
    RoleArn: str
    KMSKeyArn: str


class ErrorMetricTypeDef(TypedDict, total=False):
    ForecastType: str
    WAPE: float
    RMSE: float


class EvaluationParametersTypeDef(TypedDict, total=False):
    NumberOfBacktestWindows: int
    BackTestWindowOffset: int


class EvaluationResultTypeDef(TypedDict, total=False):
    AlgorithmArn: str
    TestWindows: List["WindowSummaryTypeDef"]


class _RequiredFeaturizationConfigTypeDef(TypedDict):
    ForecastFrequency: str


class FeaturizationConfigTypeDef(_RequiredFeaturizationConfigTypeDef, total=False):
    ForecastDimensions: List[str]
    Featurizations: List["FeaturizationTypeDef"]


class _RequiredFeaturizationMethodTypeDef(TypedDict):
    FeaturizationMethodName: Literal["filling"]


class FeaturizationMethodTypeDef(_RequiredFeaturizationMethodTypeDef, total=False):
    FeaturizationMethodParameters: Dict[str, str]


class _RequiredFeaturizationTypeDef(TypedDict):
    AttributeName: str


class FeaturizationTypeDef(_RequiredFeaturizationTypeDef, total=False):
    FeaturizationPipeline: List["FeaturizationMethodTypeDef"]


class FilterTypeDef(TypedDict):
    Key: str
    Value: str
    Condition: FilterConditionString


class ForecastExportJobSummaryTypeDef(TypedDict, total=False):
    ForecastExportJobArn: str
    ForecastExportJobName: str
    Destination: "DataDestinationTypeDef"
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime


class ForecastSummaryTypeDef(TypedDict, total=False):
    ForecastArn: str
    ForecastName: str
    PredictorArn: str
    DatasetGroupArn: str
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime


class GetAccuracyMetricsResponseTypeDef(TypedDict, total=False):
    PredictorEvaluationResults: List["EvaluationResultTypeDef"]


class HyperParameterTuningJobConfigTypeDef(TypedDict, total=False):
    ParameterRanges: "ParameterRangesTypeDef"


class _RequiredInputDataConfigTypeDef(TypedDict):
    DatasetGroupArn: str


class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, total=False):
    SupplementaryFeatures: List["SupplementaryFeatureTypeDef"]


class _RequiredIntegerParameterRangeTypeDef(TypedDict):
    Name: str
    MaxValue: int
    MinValue: int


class IntegerParameterRangeTypeDef(_RequiredIntegerParameterRangeTypeDef, total=False):
    ScalingType: ScalingType


class ListDatasetGroupsResponseTypeDef(TypedDict, total=False):
    DatasetGroups: List["DatasetGroupSummaryTypeDef"]
    NextToken: str


class ListDatasetImportJobsResponseTypeDef(TypedDict, total=False):
    DatasetImportJobs: List["DatasetImportJobSummaryTypeDef"]
    NextToken: str


class ListDatasetsResponseTypeDef(TypedDict, total=False):
    Datasets: List["DatasetSummaryTypeDef"]
    NextToken: str


class ListForecastExportJobsResponseTypeDef(TypedDict, total=False):
    ForecastExportJobs: List["ForecastExportJobSummaryTypeDef"]
    NextToken: str


class ListForecastsResponseTypeDef(TypedDict, total=False):
    Forecasts: List["ForecastSummaryTypeDef"]
    NextToken: str


class ListPredictorBacktestExportJobsResponseTypeDef(TypedDict, total=False):
    PredictorBacktestExportJobs: List["PredictorBacktestExportJobSummaryTypeDef"]
    NextToken: str


class ListPredictorsResponseTypeDef(TypedDict, total=False):
    Predictors: List["PredictorSummaryTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class MetricsTypeDef(TypedDict, total=False):
    RMSE: float
    WeightedQuantileLosses: List["WeightedQuantileLossTypeDef"]
    ErrorMetrics: List["ErrorMetricTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParameterRangesTypeDef(TypedDict, total=False):
    CategoricalParameterRanges: List["CategoricalParameterRangeTypeDef"]
    ContinuousParameterRanges: List["ContinuousParameterRangeTypeDef"]
    IntegerParameterRanges: List["IntegerParameterRangeTypeDef"]


class PredictorBacktestExportJobSummaryTypeDef(TypedDict, total=False):
    PredictorBacktestExportJobArn: str
    PredictorBacktestExportJobName: str
    Destination: "DataDestinationTypeDef"
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime


class PredictorExecutionDetailsTypeDef(TypedDict, total=False):
    PredictorExecutions: List["PredictorExecutionTypeDef"]


class PredictorExecutionTypeDef(TypedDict, total=False):
    AlgorithmArn: str
    TestWindows: List["TestWindowSummaryTypeDef"]


class PredictorSummaryTypeDef(TypedDict, total=False):
    PredictorArn: str
    PredictorName: str
    DatasetGroupArn: str
    Status: str
    Message: str
    CreationTime: datetime
    LastModificationTime: datetime


class _RequiredS3ConfigTypeDef(TypedDict):
    Path: str
    RoleArn: str


class S3ConfigTypeDef(_RequiredS3ConfigTypeDef, total=False):
    KMSKeyArn: str


class SchemaAttributeTypeDef(TypedDict, total=False):
    AttributeName: str
    AttributeType: AttributeType


class SchemaTypeDef(TypedDict, total=False):
    Attributes: List["SchemaAttributeTypeDef"]


class StatisticsTypeDef(TypedDict, total=False):
    Count: int
    CountDistinct: int
    CountNull: int
    CountNan: int
    Min: str
    Max: str
    Avg: float
    Stddev: float


class SupplementaryFeatureTypeDef(TypedDict):
    Name: str
    Value: str


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TestWindowSummaryTypeDef(TypedDict, total=False):
    TestWindowStart: datetime
    TestWindowEnd: datetime
    Status: str
    Message: str


class WeightedQuantileLossTypeDef(TypedDict, total=False):
    Quantile: float
    LossValue: float


class WindowSummaryTypeDef(TypedDict, total=False):
    TestWindowStart: datetime
    TestWindowEnd: datetime
    ItemCount: int
    EvaluationType: EvaluationType
    Metrics: "MetricsTypeDef"
