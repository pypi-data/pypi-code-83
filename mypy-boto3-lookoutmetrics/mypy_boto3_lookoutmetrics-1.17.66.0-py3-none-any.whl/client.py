"""
Type annotations for lookoutmetrics service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_lookoutmetrics import LookoutMetricsClient

    client: LookoutMetricsClient = boto3.client("lookoutmetrics")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_lookoutmetrics.literals import Frequency
from mypy_boto3_lookoutmetrics.type_defs import (
    ActionTypeDef,
    AnomalyDetectorConfigTypeDef,
    AnomalyGroupTimeSeriesFeedbackTypeDef,
    AnomalyGroupTimeSeriesTypeDef,
    CreateAlertResponseTypeDef,
    CreateAnomalyDetectorResponseTypeDef,
    CreateMetricSetResponseTypeDef,
    DescribeAlertResponseTypeDef,
    DescribeAnomalyDetectionExecutionsResponseTypeDef,
    DescribeAnomalyDetectorResponseTypeDef,
    DescribeMetricSetResponseTypeDef,
    GetAnomalyGroupResponseTypeDef,
    GetFeedbackResponseTypeDef,
    GetSampleDataResponseTypeDef,
    ListAlertsResponseTypeDef,
    ListAnomalyDetectorsResponseTypeDef,
    ListAnomalyGroupSummariesResponseTypeDef,
    ListAnomalyGroupTimeSeriesResponseTypeDef,
    ListMetricSetsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MetricSourceTypeDef,
    MetricTypeDef,
    SampleDataS3SourceConfigTypeDef,
    TimestampColumnTypeDef,
    UpdateAnomalyDetectorResponseTypeDef,
    UpdateMetricSetResponseTypeDef,
)

__all__ = ("LookoutMetricsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class LookoutMetricsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def activate_anomaly_detector(self, AnomalyDetectorArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.activate_anomaly_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#activate-anomaly-detector)
        """

    def back_test_anomaly_detector(self, AnomalyDetectorArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.back_test_anomaly_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#back-test-anomaly-detector)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#can-paginate)
        """

    def create_alert(
        self,
        AlertName: str,
        AlertSensitivityThreshold: int,
        AnomalyDetectorArn: str,
        Action: "ActionTypeDef",
        AlertDescription: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateAlertResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.create_alert)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#create-alert)
        """

    def create_anomaly_detector(
        self,
        AnomalyDetectorName: str,
        AnomalyDetectorConfig: AnomalyDetectorConfigTypeDef,
        AnomalyDetectorDescription: str = None,
        KmsKeyArn: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateAnomalyDetectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.create_anomaly_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#create-anomaly-detector)
        """

    def create_metric_set(
        self,
        AnomalyDetectorArn: str,
        MetricSetName: str,
        MetricList: List["MetricTypeDef"],
        MetricSource: "MetricSourceTypeDef",
        MetricSetDescription: str = None,
        Offset: int = None,
        TimestampColumn: "TimestampColumnTypeDef" = None,
        DimensionList: List[str] = None,
        MetricSetFrequency: Frequency = None,
        Timezone: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateMetricSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.create_metric_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#create-metric-set)
        """

    def delete_alert(self, AlertArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.delete_alert)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#delete-alert)
        """

    def delete_anomaly_detector(self, AnomalyDetectorArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.delete_anomaly_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#delete-anomaly-detector)
        """

    def describe_alert(self, AlertArn: str) -> DescribeAlertResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.describe_alert)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#describe-alert)
        """

    def describe_anomaly_detection_executions(
        self,
        AnomalyDetectorArn: str,
        Timestamp: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeAnomalyDetectionExecutionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.describe_anomaly_detection_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#describe-anomaly-detection-executions)
        """

    def describe_anomaly_detector(
        self, AnomalyDetectorArn: str
    ) -> DescribeAnomalyDetectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.describe_anomaly_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#describe-anomaly-detector)
        """

    def describe_metric_set(self, MetricSetArn: str) -> DescribeMetricSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.describe_metric_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#describe-metric-set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#generate-presigned-url)
        """

    def get_anomaly_group(
        self, AnomalyGroupId: str, AnomalyDetectorArn: str
    ) -> GetAnomalyGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.get_anomaly_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#get-anomaly-group)
        """

    def get_feedback(
        self,
        AnomalyDetectorArn: str,
        AnomalyGroupTimeSeriesFeedback: AnomalyGroupTimeSeriesTypeDef,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetFeedbackResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.get_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#get-feedback)
        """

    def get_sample_data(
        self, S3SourceConfig: SampleDataS3SourceConfigTypeDef = None
    ) -> GetSampleDataResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.get_sample_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#get-sample-data)
        """

    def list_alerts(
        self, AnomalyDetectorArn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListAlertsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.list_alerts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#list-alerts)
        """

    def list_anomaly_detectors(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListAnomalyDetectorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.list_anomaly_detectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#list-anomaly-detectors)
        """

    def list_anomaly_group_summaries(
        self,
        AnomalyDetectorArn: str,
        SensitivityThreshold: int,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListAnomalyGroupSummariesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.list_anomaly_group_summaries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#list-anomaly-group-summaries)
        """

    def list_anomaly_group_time_series(
        self,
        AnomalyDetectorArn: str,
        AnomalyGroupId: str,
        MetricName: str,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListAnomalyGroupTimeSeriesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.list_anomaly_group_time_series)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#list-anomaly-group-time-series)
        """

    def list_metric_sets(
        self, AnomalyDetectorArn: str = None, MaxResults: int = None, NextToken: str = None
    ) -> ListMetricSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.list_metric_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#list-metric-sets)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#list-tags-for-resource)
        """

    def put_feedback(
        self,
        AnomalyDetectorArn: str,
        AnomalyGroupTimeSeriesFeedback: AnomalyGroupTimeSeriesFeedbackTypeDef,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.put_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#put-feedback)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#untag-resource)
        """

    def update_anomaly_detector(
        self,
        AnomalyDetectorArn: str,
        KmsKeyArn: str = None,
        AnomalyDetectorDescription: str = None,
        AnomalyDetectorConfig: AnomalyDetectorConfigTypeDef = None,
    ) -> UpdateAnomalyDetectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.update_anomaly_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#update-anomaly-detector)
        """

    def update_metric_set(
        self,
        MetricSetArn: str,
        MetricSetDescription: str = None,
        MetricList: List["MetricTypeDef"] = None,
        Offset: int = None,
        TimestampColumn: "TimestampColumnTypeDef" = None,
        DimensionList: List[str] = None,
        MetricSetFrequency: Frequency = None,
        MetricSource: "MetricSourceTypeDef" = None,
    ) -> UpdateMetricSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/lookoutmetrics.html#LookoutMetrics.Client.update_metric_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/client.html#update-metric-set)
        """
