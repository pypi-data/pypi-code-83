"""
Type annotations for cloudwatch service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudwatch.type_defs import AlarmHistoryItemTypeDef

    data: AlarmHistoryItemTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_cloudwatch.literals import (
    AlarmType,
    AnomalyDetectorStateValue,
    ComparisonOperator,
    HistoryItemType,
    MetricStreamOutputFormat,
    StandardUnit,
    StateValue,
    Statistic,
    StatusCode,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AlarmHistoryItemTypeDef",
    "AnomalyDetectorConfigurationTypeDef",
    "AnomalyDetectorTypeDef",
    "CompositeAlarmTypeDef",
    "DashboardEntryTypeDef",
    "DashboardValidationMessageTypeDef",
    "DatapointTypeDef",
    "DeleteInsightRulesOutputTypeDef",
    "DescribeAlarmHistoryOutputTypeDef",
    "DescribeAlarmsForMetricOutputTypeDef",
    "DescribeAlarmsOutputTypeDef",
    "DescribeAnomalyDetectorsOutputTypeDef",
    "DescribeInsightRulesOutputTypeDef",
    "DimensionFilterTypeDef",
    "DimensionTypeDef",
    "DisableInsightRulesOutputTypeDef",
    "EnableInsightRulesOutputTypeDef",
    "GetDashboardOutputTypeDef",
    "GetInsightRuleReportOutputTypeDef",
    "GetMetricDataOutputTypeDef",
    "GetMetricStatisticsOutputTypeDef",
    "GetMetricStreamOutputTypeDef",
    "GetMetricWidgetImageOutputTypeDef",
    "InsightRuleContributorDatapointTypeDef",
    "InsightRuleContributorTypeDef",
    "InsightRuleMetricDatapointTypeDef",
    "InsightRuleTypeDef",
    "LabelOptionsTypeDef",
    "ListDashboardsOutputTypeDef",
    "ListMetricStreamsOutputTypeDef",
    "ListMetricsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MessageDataTypeDef",
    "MetricAlarmTypeDef",
    "MetricDataQueryTypeDef",
    "MetricDataResultTypeDef",
    "MetricDatumTypeDef",
    "MetricStatTypeDef",
    "MetricStreamEntryTypeDef",
    "MetricStreamFilterTypeDef",
    "MetricTypeDef",
    "PaginatorConfigTypeDef",
    "PartialFailureTypeDef",
    "PutDashboardOutputTypeDef",
    "PutMetricStreamOutputTypeDef",
    "RangeTypeDef",
    "ResponseMetadata",
    "StatisticSetTypeDef",
    "TagTypeDef",
    "WaiterConfigTypeDef",
)


class AlarmHistoryItemTypeDef(TypedDict, total=False):
    AlarmName: str
    AlarmType: AlarmType
    Timestamp: datetime
    HistoryItemType: HistoryItemType
    HistorySummary: str
    HistoryData: str


class AnomalyDetectorConfigurationTypeDef(TypedDict, total=False):
    ExcludedTimeRanges: List["RangeTypeDef"]
    MetricTimezone: str


class AnomalyDetectorTypeDef(TypedDict, total=False):
    Namespace: str
    MetricName: str
    Dimensions: List["DimensionTypeDef"]
    Stat: str
    Configuration: "AnomalyDetectorConfigurationTypeDef"
    StateValue: AnomalyDetectorStateValue


class CompositeAlarmTypeDef(TypedDict, total=False):
    ActionsEnabled: bool
    AlarmActions: List[str]
    AlarmArn: str
    AlarmConfigurationUpdatedTimestamp: datetime
    AlarmDescription: str
    AlarmName: str
    AlarmRule: str
    InsufficientDataActions: List[str]
    OKActions: List[str]
    StateReason: str
    StateReasonData: str
    StateUpdatedTimestamp: datetime
    StateValue: StateValue


class DashboardEntryTypeDef(TypedDict, total=False):
    DashboardName: str
    DashboardArn: str
    LastModified: datetime
    Size: int


class DashboardValidationMessageTypeDef(TypedDict, total=False):
    DataPath: str
    Message: str


class DatapointTypeDef(TypedDict, total=False):
    Timestamp: datetime
    SampleCount: float
    Average: float
    Sum: float
    Minimum: float
    Maximum: float
    Unit: StandardUnit
    ExtendedStatistics: Dict[str, float]


class DeleteInsightRulesOutputTypeDef(TypedDict):
    Failures: List["PartialFailureTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeAlarmHistoryOutputTypeDef(TypedDict):
    AlarmHistoryItems: List["AlarmHistoryItemTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeAlarmsForMetricOutputTypeDef(TypedDict):
    MetricAlarms: List["MetricAlarmTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeAlarmsOutputTypeDef(TypedDict):
    CompositeAlarms: List["CompositeAlarmTypeDef"]
    MetricAlarms: List["MetricAlarmTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeAnomalyDetectorsOutputTypeDef(TypedDict):
    AnomalyDetectors: List["AnomalyDetectorTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeInsightRulesOutputTypeDef(TypedDict):
    NextToken: str
    InsightRules: List["InsightRuleTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class _RequiredDimensionFilterTypeDef(TypedDict):
    Name: str


class DimensionFilterTypeDef(_RequiredDimensionFilterTypeDef, total=False):
    Value: str


class DimensionTypeDef(TypedDict):
    Name: str
    Value: str


class DisableInsightRulesOutputTypeDef(TypedDict):
    Failures: List["PartialFailureTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class EnableInsightRulesOutputTypeDef(TypedDict):
    Failures: List["PartialFailureTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetDashboardOutputTypeDef(TypedDict):
    DashboardArn: str
    DashboardBody: str
    DashboardName: str
    ResponseMetadata: "ResponseMetadata"


class GetInsightRuleReportOutputTypeDef(TypedDict):
    KeyLabels: List[str]
    AggregationStatistic: str
    AggregateValue: float
    ApproximateUniqueCount: int
    Contributors: List["InsightRuleContributorTypeDef"]
    MetricDatapoints: List["InsightRuleMetricDatapointTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetMetricDataOutputTypeDef(TypedDict):
    MetricDataResults: List["MetricDataResultTypeDef"]
    NextToken: str
    Messages: List["MessageDataTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetMetricStatisticsOutputTypeDef(TypedDict):
    Label: str
    Datapoints: List["DatapointTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetMetricStreamOutputTypeDef(TypedDict):
    Arn: str
    Name: str
    IncludeFilters: List["MetricStreamFilterTypeDef"]
    ExcludeFilters: List["MetricStreamFilterTypeDef"]
    FirehoseArn: str
    RoleArn: str
    State: str
    CreationDate: datetime
    LastUpdateDate: datetime
    OutputFormat: MetricStreamOutputFormat
    ResponseMetadata: "ResponseMetadata"


class GetMetricWidgetImageOutputTypeDef(TypedDict):
    MetricWidgetImage: Union[bytes, IO[bytes]]
    ResponseMetadata: "ResponseMetadata"


class InsightRuleContributorDatapointTypeDef(TypedDict):
    Timestamp: datetime
    ApproximateValue: float


class InsightRuleContributorTypeDef(TypedDict):
    Keys: List[str]
    ApproximateAggregateValue: float
    Datapoints: List["InsightRuleContributorDatapointTypeDef"]


class _RequiredInsightRuleMetricDatapointTypeDef(TypedDict):
    Timestamp: datetime


class InsightRuleMetricDatapointTypeDef(_RequiredInsightRuleMetricDatapointTypeDef, total=False):
    UniqueContributors: float
    MaxContributorValue: float
    SampleCount: float
    Average: float
    Sum: float
    Minimum: float
    Maximum: float


class InsightRuleTypeDef(TypedDict):
    Name: str
    State: str
    Schema: str
    Definition: str


class LabelOptionsTypeDef(TypedDict, total=False):
    Timezone: str


class ListDashboardsOutputTypeDef(TypedDict):
    DashboardEntries: List["DashboardEntryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListMetricStreamsOutputTypeDef(TypedDict):
    NextToken: str
    Entries: List["MetricStreamEntryTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListMetricsOutputTypeDef(TypedDict):
    Metrics: List["MetricTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class MessageDataTypeDef(TypedDict, total=False):
    Code: str
    Value: str


class MetricAlarmTypeDef(TypedDict, total=False):
    AlarmName: str
    AlarmArn: str
    AlarmDescription: str
    AlarmConfigurationUpdatedTimestamp: datetime
    ActionsEnabled: bool
    OKActions: List[str]
    AlarmActions: List[str]
    InsufficientDataActions: List[str]
    StateValue: StateValue
    StateReason: str
    StateReasonData: str
    StateUpdatedTimestamp: datetime
    MetricName: str
    Namespace: str
    Statistic: Statistic
    ExtendedStatistic: str
    Dimensions: List["DimensionTypeDef"]
    Period: int
    Unit: StandardUnit
    EvaluationPeriods: int
    DatapointsToAlarm: int
    Threshold: float
    ComparisonOperator: ComparisonOperator
    TreatMissingData: str
    EvaluateLowSampleCountPercentile: str
    Metrics: List["MetricDataQueryTypeDef"]
    ThresholdMetricId: str


class _RequiredMetricDataQueryTypeDef(TypedDict):
    Id: str


class MetricDataQueryTypeDef(_RequiredMetricDataQueryTypeDef, total=False):
    MetricStat: "MetricStatTypeDef"
    Expression: str
    Label: str
    ReturnData: bool
    Period: int


class MetricDataResultTypeDef(TypedDict, total=False):
    Id: str
    Label: str
    Timestamps: List[datetime]
    Values: List[float]
    StatusCode: StatusCode
    Messages: List["MessageDataTypeDef"]


class _RequiredMetricDatumTypeDef(TypedDict):
    MetricName: str


class MetricDatumTypeDef(_RequiredMetricDatumTypeDef, total=False):
    Dimensions: List["DimensionTypeDef"]
    Timestamp: datetime
    Value: float
    StatisticValues: "StatisticSetTypeDef"
    Values: List[float]
    Counts: List[float]
    Unit: StandardUnit
    StorageResolution: int


class _RequiredMetricStatTypeDef(TypedDict):
    Metric: "MetricTypeDef"
    Period: int
    Stat: str


class MetricStatTypeDef(_RequiredMetricStatTypeDef, total=False):
    Unit: StandardUnit


class MetricStreamEntryTypeDef(TypedDict, total=False):
    Arn: str
    CreationDate: datetime
    LastUpdateDate: datetime
    Name: str
    FirehoseArn: str
    State: str
    OutputFormat: MetricStreamOutputFormat


class MetricStreamFilterTypeDef(TypedDict, total=False):
    Namespace: str


class MetricTypeDef(TypedDict, total=False):
    Namespace: str
    MetricName: str
    Dimensions: List["DimensionTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PartialFailureTypeDef(TypedDict, total=False):
    FailureResource: str
    ExceptionType: str
    FailureCode: str
    FailureDescription: str


class PutDashboardOutputTypeDef(TypedDict):
    DashboardValidationMessages: List["DashboardValidationMessageTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class PutMetricStreamOutputTypeDef(TypedDict):
    Arn: str
    ResponseMetadata: "ResponseMetadata"


class RangeTypeDef(TypedDict):
    StartTime: datetime
    EndTime: datetime


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class StatisticSetTypeDef(TypedDict):
    SampleCount: float
    Sum: float
    Minimum: float
    Maximum: float


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
