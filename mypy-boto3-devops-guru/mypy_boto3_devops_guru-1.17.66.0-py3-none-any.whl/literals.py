"""
Type annotations for devops-guru service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/literals.html)

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
    "CostEstimationServiceResourceState",
    "CostEstimationStatus",
    "DescribeResourceCollectionHealthPaginatorName",
    "EventClass",
    "EventDataSource",
    "GetCostEstimationPaginatorName",
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
    "Locale",
    "OptInStatus",
    "ResourceCollectionType",
    "SearchInsightsPaginatorName",
    "ServiceName",
    "UpdateResourceCollectionAction",
)


AnomalySeverity = Literal["HIGH", "LOW", "MEDIUM"]
AnomalyStatus = Literal["CLOSED", "ONGOING"]
CloudWatchMetricsStat = Literal[
    "Average", "Maximum", "Minimum", "SampleCount", "Sum", "p50", "p90", "p99"
]
CostEstimationServiceResourceState = Literal["ACTIVE", "INACTIVE"]
CostEstimationStatus = Literal["COMPLETED", "ONGOING"]
DescribeResourceCollectionHealthPaginatorName = Literal["describe_resource_collection_health"]
EventClass = Literal[
    "CONFIG_CHANGE", "DEPLOYMENT", "INFRASTRUCTURE", "SCHEMA_CHANGE", "SECURITY_CHANGE"
]
EventDataSource = Literal["AWS_CLOUD_TRAIL", "AWS_CODE_DEPLOY"]
GetCostEstimationPaginatorName = Literal["get_cost_estimation"]
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
Locale = Literal[
    "DE_DE",
    "EN_GB",
    "EN_US",
    "ES_ES",
    "FR_FR",
    "IT_IT",
    "JA_JP",
    "KO_KR",
    "PT_BR",
    "ZH_CN",
    "ZH_TW",
]
OptInStatus = Literal["DISABLED", "ENABLED"]
ResourceCollectionType = Literal["AWS_CLOUD_FORMATION", "AWS_SERVICE"]
SearchInsightsPaginatorName = Literal["search_insights"]
ServiceName = Literal[
    "API_GATEWAY",
    "APPLICATION_ELB",
    "AUTO_SCALING_GROUP",
    "CLOUD_FRONT",
    "DYNAMO_DB",
    "EC2",
    "ECS",
    "EKS",
    "ELASTIC_BEANSTALK",
    "ELASTI_CACHE",
    "ELB",
    "ES",
    "KINESIS",
    "LAMBDA",
    "NAT_GATEWAY",
    "NETWORK_ELB",
    "RDS",
    "REDSHIFT",
    "ROUTE_53",
    "S3",
    "SAGE_MAKER",
    "SNS",
    "SQS",
    "STEP_FUNCTIONS",
    "SWF",
]
UpdateResourceCollectionAction = Literal["ADD", "REMOVE"]
