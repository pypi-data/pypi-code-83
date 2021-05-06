"""
Type annotations for cloudwatch service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/literals.html)

Usage::

    ```python
    from mypy_boto3_cloudwatch.literals import AlarmExistsWaiterName

    data: AlarmExistsWaiterName = "alarm_exists"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AlarmExistsWaiterName",
    "AlarmType",
    "AnomalyDetectorStateValue",
    "ComparisonOperator",
    "CompositeAlarmExistsWaiterName",
    "DescribeAlarmHistoryPaginatorName",
    "DescribeAlarmsPaginatorName",
    "GetMetricDataPaginatorName",
    "HistoryItemType",
    "ListDashboardsPaginatorName",
    "ListMetricsPaginatorName",
    "MetricStreamOutputFormat",
    "RecentlyActive",
    "ScanBy",
    "StandardUnit",
    "StateValue",
    "Statistic",
    "StatusCode",
)


AlarmExistsWaiterName = Literal["alarm_exists"]
AlarmType = Literal["CompositeAlarm", "MetricAlarm"]
AnomalyDetectorStateValue = Literal["PENDING_TRAINING", "TRAINED", "TRAINED_INSUFFICIENT_DATA"]
ComparisonOperator = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "GreaterThanUpperThreshold",
    "LessThanLowerOrGreaterThanUpperThreshold",
    "LessThanLowerThreshold",
    "LessThanOrEqualToThreshold",
    "LessThanThreshold",
]
CompositeAlarmExistsWaiterName = Literal["composite_alarm_exists"]
DescribeAlarmHistoryPaginatorName = Literal["describe_alarm_history"]
DescribeAlarmsPaginatorName = Literal["describe_alarms"]
GetMetricDataPaginatorName = Literal["get_metric_data"]
HistoryItemType = Literal["Action", "ConfigurationUpdate", "StateUpdate"]
ListDashboardsPaginatorName = Literal["list_dashboards"]
ListMetricsPaginatorName = Literal["list_metrics"]
MetricStreamOutputFormat = Literal["json", "opentelemetry0.7"]
RecentlyActive = Literal["PT3H"]
ScanBy = Literal["TimestampAscending", "TimestampDescending"]
StandardUnit = Literal[
    "Bits",
    "Bits/Second",
    "Bytes",
    "Bytes/Second",
    "Count",
    "Count/Second",
    "Gigabits",
    "Gigabits/Second",
    "Gigabytes",
    "Gigabytes/Second",
    "Kilobits",
    "Kilobits/Second",
    "Kilobytes",
    "Kilobytes/Second",
    "Megabits",
    "Megabits/Second",
    "Megabytes",
    "Megabytes/Second",
    "Microseconds",
    "Milliseconds",
    "None",
    "Percent",
    "Seconds",
    "Terabits",
    "Terabits/Second",
    "Terabytes",
    "Terabytes/Second",
]
StateValue = Literal["ALARM", "INSUFFICIENT_DATA", "OK"]
Statistic = Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
StatusCode = Literal["Complete", "InternalError", "PartialData"]
