"""
Type annotations for lookoutmetrics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lookoutmetrics.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_lookoutmetrics.literals import (
    AggregationFunction,
    AlertStatus,
    AlertType,
    AnomalyDetectionTaskStatus,
    AnomalyDetectorStatus,
    CSVFileCompression,
    Frequency,
    JsonFileCompression,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionTypeDef",
    "AlertSummaryTypeDef",
    "AlertTypeDef",
    "AnomalyDetectorConfigSummaryTypeDef",
    "AnomalyDetectorConfigTypeDef",
    "AnomalyDetectorSummaryTypeDef",
    "AnomalyGroupStatisticsTypeDef",
    "AnomalyGroupSummaryTypeDef",
    "AnomalyGroupTimeSeriesFeedbackTypeDef",
    "AnomalyGroupTimeSeriesTypeDef",
    "AnomalyGroupTypeDef",
    "AppFlowConfigTypeDef",
    "CloudWatchConfigTypeDef",
    "ContributionMatrixTypeDef",
    "CreateAlertResponseTypeDef",
    "CreateAnomalyDetectorResponseTypeDef",
    "CreateMetricSetResponseTypeDef",
    "CsvFormatDescriptorTypeDef",
    "DescribeAlertResponseTypeDef",
    "DescribeAnomalyDetectionExecutionsResponseTypeDef",
    "DescribeAnomalyDetectorResponseTypeDef",
    "DescribeMetricSetResponseTypeDef",
    "DimensionContributionTypeDef",
    "DimensionNameValueTypeDef",
    "DimensionValueContributionTypeDef",
    "ExecutionStatusTypeDef",
    "FileFormatDescriptorTypeDef",
    "GetAnomalyGroupResponseTypeDef",
    "GetFeedbackResponseTypeDef",
    "GetSampleDataResponseTypeDef",
    "ItemizedMetricStatsTypeDef",
    "JsonFormatDescriptorTypeDef",
    "LambdaConfigurationTypeDef",
    "ListAlertsResponseTypeDef",
    "ListAnomalyDetectorsResponseTypeDef",
    "ListAnomalyGroupSummariesResponseTypeDef",
    "ListAnomalyGroupTimeSeriesResponseTypeDef",
    "ListMetricSetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricLevelImpactTypeDef",
    "MetricSetSummaryTypeDef",
    "MetricSourceTypeDef",
    "MetricTypeDef",
    "RDSSourceConfigTypeDef",
    "RedshiftSourceConfigTypeDef",
    "S3SourceConfigTypeDef",
    "SNSConfigurationTypeDef",
    "SampleDataS3SourceConfigTypeDef",
    "TimeSeriesFeedbackTypeDef",
    "TimeSeriesTypeDef",
    "TimestampColumnTypeDef",
    "UpdateAnomalyDetectorResponseTypeDef",
    "UpdateMetricSetResponseTypeDef",
    "VpcConfigurationTypeDef",
)


class ActionTypeDef(TypedDict, total=False):
    SNSConfiguration: "SNSConfigurationTypeDef"
    LambdaConfiguration: "LambdaConfigurationTypeDef"


class AlertSummaryTypeDef(TypedDict, total=False):
    AlertArn: str
    AnomalyDetectorArn: str
    AlertName: str
    AlertSensitivityThreshold: int
    AlertType: AlertType
    AlertStatus: AlertStatus
    LastModificationTime: datetime
    CreationTime: datetime
    Tags: Dict[str, str]


class AlertTypeDef(TypedDict, total=False):
    Action: "ActionTypeDef"
    AlertDescription: str
    AlertArn: str
    AnomalyDetectorArn: str
    AlertName: str
    AlertSensitivityThreshold: int
    AlertType: AlertType
    AlertStatus: AlertStatus
    LastModificationTime: datetime
    CreationTime: datetime


class AnomalyDetectorConfigSummaryTypeDef(TypedDict, total=False):
    AnomalyDetectorFrequency: Frequency


class AnomalyDetectorConfigTypeDef(TypedDict, total=False):
    AnomalyDetectorFrequency: Frequency


class AnomalyDetectorSummaryTypeDef(TypedDict, total=False):
    AnomalyDetectorArn: str
    AnomalyDetectorName: str
    AnomalyDetectorDescription: str
    CreationTime: datetime
    LastModificationTime: datetime
    Status: AnomalyDetectorStatus
    Tags: Dict[str, str]


class AnomalyGroupStatisticsTypeDef(TypedDict, total=False):
    EvaluationStartDate: str
    TotalCount: int
    ItemizedMetricStatsList: List["ItemizedMetricStatsTypeDef"]


class AnomalyGroupSummaryTypeDef(TypedDict, total=False):
    StartTime: str
    EndTime: str
    AnomalyGroupId: str
    AnomalyGroupScore: float
    PrimaryMetricName: str


class AnomalyGroupTimeSeriesFeedbackTypeDef(TypedDict):
    AnomalyGroupId: str
    TimeSeriesId: str
    IsAnomaly: bool


class _RequiredAnomalyGroupTimeSeriesTypeDef(TypedDict):
    AnomalyGroupId: str


class AnomalyGroupTimeSeriesTypeDef(_RequiredAnomalyGroupTimeSeriesTypeDef, total=False):
    TimeSeriesId: str


class AnomalyGroupTypeDef(TypedDict, total=False):
    StartTime: str
    EndTime: str
    AnomalyGroupId: str
    AnomalyGroupScore: float
    PrimaryMetricName: str
    MetricLevelImpactList: List["MetricLevelImpactTypeDef"]


class AppFlowConfigTypeDef(TypedDict):
    RoleArn: str
    FlowName: str


class CloudWatchConfigTypeDef(TypedDict):
    RoleArn: str


class ContributionMatrixTypeDef(TypedDict, total=False):
    DimensionContributionList: List["DimensionContributionTypeDef"]


class CreateAlertResponseTypeDef(TypedDict, total=False):
    AlertArn: str


class CreateAnomalyDetectorResponseTypeDef(TypedDict, total=False):
    AnomalyDetectorArn: str


class CreateMetricSetResponseTypeDef(TypedDict, total=False):
    MetricSetArn: str


class CsvFormatDescriptorTypeDef(TypedDict, total=False):
    FileCompression: CSVFileCompression
    Charset: str
    ContainsHeader: bool
    Delimiter: str
    HeaderList: List[str]
    QuoteSymbol: str


class DescribeAlertResponseTypeDef(TypedDict, total=False):
    Alert: "AlertTypeDef"


class DescribeAnomalyDetectionExecutionsResponseTypeDef(TypedDict, total=False):
    ExecutionList: List["ExecutionStatusTypeDef"]
    NextToken: str


class DescribeAnomalyDetectorResponseTypeDef(TypedDict, total=False):
    AnomalyDetectorArn: str
    AnomalyDetectorName: str
    AnomalyDetectorDescription: str
    AnomalyDetectorConfig: "AnomalyDetectorConfigSummaryTypeDef"
    CreationTime: datetime
    LastModificationTime: datetime
    Status: AnomalyDetectorStatus
    FailureReason: str
    KmsKeyArn: str


class DescribeMetricSetResponseTypeDef(TypedDict, total=False):
    MetricSetArn: str
    AnomalyDetectorArn: str
    MetricSetName: str
    MetricSetDescription: str
    CreationTime: datetime
    LastModificationTime: datetime
    Offset: int
    MetricList: List["MetricTypeDef"]
    TimestampColumn: "TimestampColumnTypeDef"
    DimensionList: List[str]
    MetricSetFrequency: Frequency
    Timezone: str
    MetricSource: "MetricSourceTypeDef"


class DimensionContributionTypeDef(TypedDict, total=False):
    DimensionName: str
    DimensionValueContributionList: List["DimensionValueContributionTypeDef"]


class DimensionNameValueTypeDef(TypedDict):
    DimensionName: str
    DimensionValue: str


class DimensionValueContributionTypeDef(TypedDict, total=False):
    DimensionValue: str
    ContributionScore: float


class ExecutionStatusTypeDef(TypedDict, total=False):
    Timestamp: str
    Status: AnomalyDetectionTaskStatus
    FailureReason: str


class FileFormatDescriptorTypeDef(TypedDict, total=False):
    CsvFormatDescriptor: "CsvFormatDescriptorTypeDef"
    JsonFormatDescriptor: "JsonFormatDescriptorTypeDef"


class GetAnomalyGroupResponseTypeDef(TypedDict, total=False):
    AnomalyGroup: "AnomalyGroupTypeDef"


class GetFeedbackResponseTypeDef(TypedDict, total=False):
    AnomalyGroupTimeSeriesFeedback: List["TimeSeriesFeedbackTypeDef"]
    NextToken: str


class GetSampleDataResponseTypeDef(TypedDict, total=False):
    HeaderValues: List[str]
    SampleRows: List[List[str]]


class ItemizedMetricStatsTypeDef(TypedDict, total=False):
    MetricName: str
    OccurrenceCount: int


class JsonFormatDescriptorTypeDef(TypedDict, total=False):
    FileCompression: JsonFileCompression
    Charset: str


class LambdaConfigurationTypeDef(TypedDict):
    RoleArn: str
    LambdaArn: str


class ListAlertsResponseTypeDef(TypedDict, total=False):
    AlertSummaryList: List["AlertSummaryTypeDef"]
    NextToken: str


class ListAnomalyDetectorsResponseTypeDef(TypedDict, total=False):
    AnomalyDetectorSummaryList: List["AnomalyDetectorSummaryTypeDef"]
    NextToken: str


class ListAnomalyGroupSummariesResponseTypeDef(TypedDict, total=False):
    AnomalyGroupSummaryList: List["AnomalyGroupSummaryTypeDef"]
    AnomalyGroupStatistics: "AnomalyGroupStatisticsTypeDef"
    NextToken: str


class ListAnomalyGroupTimeSeriesResponseTypeDef(TypedDict, total=False):
    AnomalyGroupId: str
    MetricName: str
    TimestampList: List[str]
    NextToken: str
    TimeSeriesList: List["TimeSeriesTypeDef"]


class ListMetricSetsResponseTypeDef(TypedDict, total=False):
    MetricSetSummaryList: List["MetricSetSummaryTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class MetricLevelImpactTypeDef(TypedDict, total=False):
    MetricName: str
    NumTimeSeries: int
    ContributionMatrix: "ContributionMatrixTypeDef"


class MetricSetSummaryTypeDef(TypedDict, total=False):
    MetricSetArn: str
    AnomalyDetectorArn: str
    MetricSetDescription: str
    MetricSetName: str
    CreationTime: datetime
    LastModificationTime: datetime
    Tags: Dict[str, str]


class MetricSourceTypeDef(TypedDict, total=False):
    S3SourceConfig: "S3SourceConfigTypeDef"
    AppFlowConfig: "AppFlowConfigTypeDef"
    CloudWatchConfig: "CloudWatchConfigTypeDef"
    RDSSourceConfig: "RDSSourceConfigTypeDef"
    RedshiftSourceConfig: "RedshiftSourceConfigTypeDef"


class _RequiredMetricTypeDef(TypedDict):
    MetricName: str
    AggregationFunction: AggregationFunction


class MetricTypeDef(_RequiredMetricTypeDef, total=False):
    Namespace: str


class RDSSourceConfigTypeDef(TypedDict):
    DBInstanceIdentifier: str
    DatabaseHost: str
    DatabasePort: int
    SecretManagerArn: str
    DatabaseName: str
    TableName: str
    RoleArn: str
    VpcConfiguration: "VpcConfigurationTypeDef"


class RedshiftSourceConfigTypeDef(TypedDict):
    ClusterIdentifier: str
    DatabaseHost: str
    DatabasePort: int
    SecretManagerArn: str
    DatabaseName: str
    TableName: str
    RoleArn: str
    VpcConfiguration: "VpcConfigurationTypeDef"


class _RequiredS3SourceConfigTypeDef(TypedDict):
    RoleArn: str


class S3SourceConfigTypeDef(_RequiredS3SourceConfigTypeDef, total=False):
    TemplatedPathList: List[str]
    HistoricalDataPathList: List[str]
    FileFormatDescriptor: "FileFormatDescriptorTypeDef"


class SNSConfigurationTypeDef(TypedDict):
    RoleArn: str
    SnsTopicArn: str


class _RequiredSampleDataS3SourceConfigTypeDef(TypedDict):
    RoleArn: str
    FileFormatDescriptor: "FileFormatDescriptorTypeDef"


class SampleDataS3SourceConfigTypeDef(_RequiredSampleDataS3SourceConfigTypeDef, total=False):
    TemplatedPathList: List[str]
    HistoricalDataPathList: List[str]


class TimeSeriesFeedbackTypeDef(TypedDict, total=False):
    TimeSeriesId: str
    IsAnomaly: bool


class TimeSeriesTypeDef(TypedDict):
    TimeSeriesId: str
    DimensionList: List["DimensionNameValueTypeDef"]
    MetricValueList: List[float]


class TimestampColumnTypeDef(TypedDict, total=False):
    ColumnName: str
    ColumnFormat: str


class UpdateAnomalyDetectorResponseTypeDef(TypedDict, total=False):
    AnomalyDetectorArn: str


class UpdateMetricSetResponseTypeDef(TypedDict, total=False):
    MetricSetArn: str


class VpcConfigurationTypeDef(TypedDict):
    SubnetIdList: List[str]
    SecurityGroupIdList: List[str]
