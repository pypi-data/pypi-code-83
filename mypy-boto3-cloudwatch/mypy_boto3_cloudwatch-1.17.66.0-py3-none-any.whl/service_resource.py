"""
Type annotations for cloudwatch service ServiceResource

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html)

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
import sys
from datetime import datetime
from typing import Any, Iterator, List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from mypy_boto3_cloudwatch.literals import (
    AlarmType,
    ComparisonOperator,
    HistoryItemType,
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

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.ServiceResource.alarms)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#serviceresourcealarmscollection)
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.ServiceResource.metrics)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#serviceresourcemetricscollection)
    """

    def all(self) -> "ServiceResourceMetricsCollection":
        pass

    def filter(  # type: ignore
        self,
        Namespace: str = None,
        MetricName: str = None,
        Dimensions: List[DimensionFilterTypeDef] = None,
        NextToken: str = None,
        RecentlyActive: Literal["PT3H"] = None,
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.Metric.alarms)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metricalarmscollection)
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
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Alarm)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarm)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.Alarm.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmdeletemethod)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.Alarm.describe_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmdescribe-historymethod)
        """

    def disable_actions(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.Alarm.disable_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmdisable-actionsmethod)
        """

    def enable_actions(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.Alarm.enable_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmenable-actionsmethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.Alarm.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.Alarm.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.Alarm.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmreloadmethod)
        """

    def set_state(
        self, StateValue: StateValue, StateReason: str, StateReasonData: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.Alarm.set_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#alarmset-statemethod)
        """


_Alarm = Alarm


class Metric(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Metric)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metric)
    """

    metric_name: str
    dimensions: List[Any]
    namespace: str
    name: str
    alarms: MetricAlarmsCollection

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.Metric.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metricget-available-subresourcesmethod)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.Metric.get_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metricget-statisticsmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.Metric.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metricloadmethod)
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.Metric.put_alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metricput-alarmmethod)
        """

    def put_data(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.Metric.put_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metricput-datamethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.Metric.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#metricreloadmethod)
        """


_Metric = Metric


class CloudWatchServiceResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.ServiceResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html)
    """

    alarms: ServiceResourceAlarmsCollection
    metrics: ServiceResourceMetricsCollection

    def Alarm(self, name: str) -> _Alarm:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Alarm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#cloudwatchserviceresourcealarmmethod)
        """

    def Metric(self, namespace: str, name: str) -> _Metric:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.ServiceResource.Metric)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#cloudwatchserviceresourcemetricmethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudwatch.html#CloudWatch.ServiceResource.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudwatch/service_resource.html#cloudwatchserviceresourceget-available-subresourcesmethod)
        """
