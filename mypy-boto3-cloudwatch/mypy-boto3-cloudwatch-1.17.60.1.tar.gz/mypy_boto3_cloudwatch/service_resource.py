"""
Main interface for cloudwatch service ServiceResource

Usage::

    ```python
    import boto3

    from mypy_boto3_cloudwatch import CloudWatchServiceResource
    import mypy_boto3_cloudwatch.service_resource as cloudwatch_resources

    resource: CloudWatchServiceResource = boto3.resource("cloudwatch")

    my_alarm: cloudwatch_resources.Alarm = resource.Alarm(...)
    my_metric: cloudwatch_resources.Metric = resource.Metric(...)
```
"""
from datetime import datetime
from typing import Any, Iterator, List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from mypy_boto3_cloudwatch.literals import (
    AlarmType,
    ComparisonOperator,
    HistoryItemType,
    RecentlyActive,
    ScanBy,
    StandardUnit,
    StateValue,
    Statistic,
)
from mypy_boto3_cloudwatch.type_defs import (
    DescribeAlarmHistoryOutputTypeDef,
    DimensionFilterTypeDef,
    DimensionTypeDef,
    GetMetricStatisticsOutputTypeDef,
    MetricDataQueryTypeDef,
    TagTypeDef,
)

__all__ = (
    "CloudWatchServiceResource",
    "Alarm",
    "Metric",
    "ServiceResourceAlarmsCollection",
    "ServiceResourceMetricsCollection",
    "MetricAlarmsCollection",
)


class ServiceResourceAlarmsCollection(ResourceCollection):
    """
    [ServiceResource.alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.ServiceResource.alarms)
    """

    def all(self) -> "ServiceResourceAlarmsCollection":
        pass

    def filter(  # type: ignore
        self,
        AlarmNames: List[str] = None,
        AlarmNamePrefix: str = None,
        AlarmTypes: List[AlarmType] = None,
        ChildrenOfAlarmName: str = None,
        ParentsOfAlarmName: str = None,
        StateValue: StateValue = None,
        ActionPrefix: str = None,
        MaxRecords: int = None,
        NextToken: str = None,
    ) -> "ServiceResourceAlarmsCollection":
        pass

    def delete(self) -> None:
        pass

    def disable_actions(self) -> None:
        pass

    def enable_actions(self) -> None:
        pass

    def limit(self, count: int) -> "ServiceResourceAlarmsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceAlarmsCollection":
        pass

    def pages(self) -> Iterator[List["Alarm"]]:
        pass

    def __iter__(self) -> Iterator["Alarm"]:
        pass


class ServiceResourceMetricsCollection(ResourceCollection):
    """
    [ServiceResource.metrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.ServiceResource.metrics)
    """

    def all(self) -> "ServiceResourceMetricsCollection":
        pass

    def filter(  # type: ignore
        self,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[DimensionFilterTypeDef] = None,
        NextToken: str = None,
        RecentlyActive: RecentlyActive = None,
    ) -> "ServiceResourceMetricsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceMetricsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceMetricsCollection":
        pass

    def pages(self) -> Iterator[List["Metric"]]:
        pass

    def __iter__(self) -> Iterator["Metric"]:
        pass


class MetricAlarmsCollection(ResourceCollection):
    """
    [Metric.alarms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Metric.alarms)
    """

    def all(self) -> "MetricAlarmsCollection":
        pass

    def filter(  # type: ignore
        self,
        Statistic: Statistic = None,
        ExtendedStatistic: str = None,
        Dimensions: List["DimensionTypeDef"] = None,
        Period: int = None,
        Unit: StandardUnit = None,
    ) -> "MetricAlarmsCollection":
        pass

    def delete(self) -> None:
        pass

    def disable_actions(self) -> None:
        pass

    def enable_actions(self) -> None:
        pass

    def limit(self, count: int) -> "MetricAlarmsCollection":
        pass

    def page_size(self, count: int) -> "MetricAlarmsCollection":
        pass

    def pages(self) -> Iterator[List["Alarm"]]:
        pass

    def __iter__(self) -> Iterator["Alarm"]:
        pass


class Alarm(Boto3ServiceResource):
    """
    [Alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Alarm)
    """

    alarm_name: str
    alarm_arn: str
    alarm_description: str
    alarm_configuration_updated_timestamp: datetime
    actions_enabled: bool
    ok_actions: List[Any]
    alarm_actions: List[Any]
    insufficient_data_actions: List[Any]
    state_value: str
    state_reason: str
    state_reason_data: str
    state_updated_timestamp: datetime
    metric_name: str
    namespace: str
    statistic: str
    extended_statistic: str
    dimensions: List[Any]
    period: int
    unit: str
    evaluation_periods: int
    datapoints_to_alarm: int
    threshold: float
    comparison_operator: str
    treat_missing_data: str
    evaluate_low_sample_count_percentile: str
    metrics: List[Any]
    threshold_metric_id: str
    name: str
    metric: "Metric"

    def delete(self) -> None:
        """
        [Alarm.delete documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Alarm.delete)
        """

    def describe_history(
        self,
        AlarmTypes: List[AlarmType] = None,
        HistoryItemType: HistoryItemType = None,
        StartDate: datetime = None,
        EndDate: datetime = None,
        MaxRecords: int = None,
        NextToken: str = None,
        ScanBy: ScanBy = None,
    ) -> DescribeAlarmHistoryOutputTypeDef:
        """
        [Alarm.describe_history documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Alarm.describe_history)
        """

    def disable_actions(self) -> None:
        """
        [Alarm.disable_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Alarm.disable_actions)
        """

    def enable_actions(self) -> None:
        """
        [Alarm.enable_actions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Alarm.enable_actions)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Alarm.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Alarm.get_available_subresources)
        """

    def load(self) -> None:
        """
        [Alarm.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Alarm.load)
        """

    def reload(self) -> None:
        """
        [Alarm.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Alarm.reload)
        """

    def set_state(
        self, StateValue: StateValue, StateReason: str, StateReasonData: str = None
    ) -> None:
        """
        [Alarm.set_state documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Alarm.set_state)
        """


_Alarm = Alarm


class Metric(Boto3ServiceResource):
    """
    [Metric documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Metric)
    """

    metric_name: str
    dimensions: List[Any]
    namespace: str
    name: str
    alarms: MetricAlarmsCollection

    def get_available_subresources(self) -> List[str]:
        """
        [Metric.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Metric.get_available_subresources)
        """

    def get_statistics(
        self,
        StartTime: datetime,
        EndTime: datetime,
        Period: int,
        Dimensions: List["DimensionTypeDef"] = None,
        Statistics: List[Statistic] = None,
        ExtendedStatistics: List[str] = None,
        Unit: StandardUnit = None,
    ) -> GetMetricStatisticsOutputTypeDef:
        """
        [Metric.get_statistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Metric.get_statistics)
        """

    def load(self) -> None:
        """
        [Metric.load documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Metric.load)
        """

    def put_alarm(
        self,
        AlarmName: str,
        EvaluationPeriods: int,
        ComparisonOperator: ComparisonOperator,
        AlarmDescription: str = None,
        ActionsEnabled: bool = None,
        OKActions: List[str] = None,
        AlarmActions: List[str] = None,
        InsufficientDataActions: List[str] = None,
        Statistic: Statistic = None,
        ExtendedStatistic: str = None,
        Dimensions: List["DimensionTypeDef"] = None,
        Period: int = None,
        Unit: StandardUnit = None,
        DatapointsToAlarm: int = None,
        Threshold: float = None,
        TreatMissingData: str = None,
        EvaluateLowSampleCountPercentile: str = None,
        Metrics: List["MetricDataQueryTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        ThresholdMetricId: str = None,
    ) -> _Alarm:
        """
        [Metric.put_alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Metric.put_alarm)
        """

    def put_data(self) -> None:
        """
        [Metric.put_data documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Metric.put_data)
        """

    def reload(self) -> None:
        """
        [Metric.reload documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.Metric.reload)
        """


_Metric = Metric


class CloudWatchServiceResource(Boto3ServiceResource):
    """
    [CloudWatch.ServiceResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.ServiceResource)
    """

    alarms: ServiceResourceAlarmsCollection
    metrics: ServiceResourceMetricsCollection

    def Alarm(self, name: str) -> _Alarm:
        """
        [ServiceResource.Alarm documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Alarm)
        """

    def Metric(self, namespace: str, name: str) -> _Metric:
        """
        [ServiceResource.Metric documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Metric)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [ServiceResource.get_available_subresources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/cloudwatch.html#CloudWatch.ServiceResource.get_available_subresources)
        """
