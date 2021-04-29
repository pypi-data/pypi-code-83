"""
Main interface for devops-guru service literal definitions.

Usage::

    ```python
    from mypy_boto3_devops_guru.literals import AnomalySeverity

    data: AnomalySeverity = "HIGH"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AnomalySeverity",
    "AnomalyStatus",
    "CloudWatchMetricsStat",
    "DescribeResourceCollectionHealthPaginatorName",
    "EventClass",
    "EventDataSource",
    "GetResourceCollectionPaginatorName",
    "InsightFeedbackOption",
    "InsightSeverity",
    "InsightStatus",
    "InsightType",
    "ListAnomaliesForInsightPaginatorName",
    "ListEventsPaginatorName",
    "ListInsightsPaginatorName",
    "ListNotificationChannelsPaginatorName",
    "ListRecommendationsPaginatorName",
    "OptInStatus",
    "ResourceCollectionType",
    "SearchInsightsPaginatorName",
    "UpdateResourceCollectionAction",
)


AnomalySeverity = Literal["HIGH", "LOW", "MEDIUM"]
AnomalyStatus = Literal["CLOSED", "ONGOING"]
CloudWatchMetricsStat = Literal[
    "Average", "Maximum", "Minimum", "SampleCount", "Sum", "p50", "p90", "p99"
]
DescribeResourceCollectionHealthPaginatorName = Literal["describe_resource_collection_health"]
EventClass = Literal[
    "CONFIG_CHANGE", "DEPLOYMENT", "INFRASTRUCTURE", "SCHEMA_CHANGE", "SECURITY_CHANGE"
]
EventDataSource = Literal["AWS_CLOUD_TRAIL", "AWS_CODE_DEPLOY"]
GetResourceCollectionPaginatorName = Literal["get_resource_collection"]
InsightFeedbackOption = Literal[
    "ALERT_TOO_SENSITIVE",
    "DATA_INCORRECT",
    "DATA_NOISY_ANOMALY",
    "RECOMMENDATION_USEFUL",
    "VALID_COLLECTION",
]
InsightSeverity = Literal["HIGH", "LOW", "MEDIUM"]
InsightStatus = Literal["CLOSED", "ONGOING"]
InsightType = Literal["PROACTIVE", "REACTIVE"]
ListAnomaliesForInsightPaginatorName = Literal["list_anomalies_for_insight"]
ListEventsPaginatorName = Literal["list_events"]
ListInsightsPaginatorName = Literal["list_insights"]
ListNotificationChannelsPaginatorName = Literal["list_notification_channels"]
ListRecommendationsPaginatorName = Literal["list_recommendations"]
OptInStatus = Literal["DISABLED", "ENABLED"]
ResourceCollectionType = Literal["AWS_CLOUD_FORMATION"]
SearchInsightsPaginatorName = Literal["search_insights"]
UpdateResourceCollectionAction = Literal["ADD", "REMOVE"]
