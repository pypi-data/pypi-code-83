"""
Type annotations for devops-guru service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_devops_guru/type_defs.html)

Usage::

    ```python
    from mypy_boto3_devops_guru.type_defs import AddNotificationChannelResponseTypeDef

    data: AddNotificationChannelResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_devops_guru.literals import (
    AnomalySeverity,
    AnomalyStatus,
    CloudWatchMetricsStat,
    CostEstimationServiceResourceState,
    CostEstimationStatus,
    EventClass,
    EventDataSource,
    InsightFeedbackOption,
    InsightSeverity,
    InsightStatus,
    InsightType,
    OptInStatus,
    ServiceName,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddNotificationChannelResponseTypeDef",
    "AnomalySourceDetailsTypeDef",
    "AnomalyTimeRangeTypeDef",
    "CloudFormationCollectionFilterTypeDef",
    "CloudFormationCollectionTypeDef",
    "CloudFormationCostEstimationResourceCollectionFilterTypeDef",
    "CloudFormationHealthTypeDef",
    "CloudWatchMetricsDetailTypeDef",
    "CloudWatchMetricsDimensionTypeDef",
    "CostEstimationResourceCollectionFilterTypeDef",
    "CostEstimationTimeRangeTypeDef",
    "DescribeAccountHealthResponseTypeDef",
    "DescribeAccountOverviewResponseTypeDef",
    "DescribeAnomalyResponseTypeDef",
    "DescribeFeedbackResponseTypeDef",
    "DescribeInsightResponseTypeDef",
    "DescribeResourceCollectionHealthResponseTypeDef",
    "DescribeServiceIntegrationResponseTypeDef",
    "EndTimeRangeTypeDef",
    "EventResourceTypeDef",
    "EventTimeRangeTypeDef",
    "EventTypeDef",
    "GetCostEstimationResponseTypeDef",
    "GetResourceCollectionResponseTypeDef",
    "InsightFeedbackTypeDef",
    "InsightHealthTypeDef",
    "InsightTimeRangeTypeDef",
    "ListAnomaliesForInsightResponseTypeDef",
    "ListEventsFiltersTypeDef",
    "ListEventsResponseTypeDef",
    "ListInsightsAnyStatusFilterTypeDef",
    "ListInsightsClosedStatusFilterTypeDef",
    "ListInsightsOngoingStatusFilterTypeDef",
    "ListInsightsResponseTypeDef",
    "ListInsightsStatusFilterTypeDef",
    "ListNotificationChannelsResponseTypeDef",
    "ListRecommendationsResponseTypeDef",
    "NotificationChannelConfigTypeDef",
    "NotificationChannelTypeDef",
    "OpsCenterIntegrationConfigTypeDef",
    "OpsCenterIntegrationTypeDef",
    "PaginatorConfigTypeDef",
    "PredictionTimeRangeTypeDef",
    "ProactiveAnomalySummaryTypeDef",
    "ProactiveAnomalyTypeDef",
    "ProactiveInsightSummaryTypeDef",
    "ProactiveInsightTypeDef",
    "ReactiveAnomalySummaryTypeDef",
    "ReactiveAnomalyTypeDef",
    "ReactiveInsightSummaryTypeDef",
    "ReactiveInsightTypeDef",
    "RecommendationRelatedAnomalyResourceTypeDef",
    "RecommendationRelatedAnomalySourceDetailTypeDef",
    "RecommendationRelatedAnomalyTypeDef",
    "RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef",
    "RecommendationRelatedEventResourceTypeDef",
    "RecommendationRelatedEventTypeDef",
    "RecommendationTypeDef",
    "ResourceCollectionFilterTypeDef",
    "ResourceCollectionTypeDef",
    "SearchInsightsFiltersTypeDef",
    "SearchInsightsResponseTypeDef",
    "ServiceCollectionTypeDef",
    "ServiceHealthTypeDef",
    "ServiceInsightHealthTypeDef",
    "ServiceIntegrationConfigTypeDef",
    "ServiceResourceCostTypeDef",
    "SnsChannelConfigTypeDef",
    "StartTimeRangeTypeDef",
    "UpdateCloudFormationCollectionFilterTypeDef",
    "UpdateResourceCollectionFilterTypeDef",
    "UpdateServiceIntegrationConfigTypeDef",
)


class AddNotificationChannelResponseTypeDef(TypedDict):
    Id: str


class AnomalySourceDetailsTypeDef(TypedDict, total=False):
    CloudWatchMetrics: List["CloudWatchMetricsDetailTypeDef"]


class _RequiredAnomalyTimeRangeTypeDef(TypedDict):
    StartTime: datetime


class AnomalyTimeRangeTypeDef(_RequiredAnomalyTimeRangeTypeDef, total=False):
    EndTime: datetime


class CloudFormationCollectionFilterTypeDef(TypedDict, total=False):
    StackNames: List[str]


class CloudFormationCollectionTypeDef(TypedDict, total=False):
    StackNames: List[str]


class CloudFormationCostEstimationResourceCollectionFilterTypeDef(TypedDict, total=False):
    StackNames: List[str]


class CloudFormationHealthTypeDef(TypedDict, total=False):
    StackName: str
    Insight: "InsightHealthTypeDef"


class CloudWatchMetricsDetailTypeDef(TypedDict, total=False):
    MetricName: str
    Namespace: str
    Dimensions: List["CloudWatchMetricsDimensionTypeDef"]
    Stat: CloudWatchMetricsStat
    Unit: str
    Period: int


class CloudWatchMetricsDimensionTypeDef(TypedDict, total=False):
    Name: str
    Value: str


class CostEstimationResourceCollectionFilterTypeDef(TypedDict, total=False):
    CloudFormation: "CloudFormationCostEstimationResourceCollectionFilterTypeDef"


class CostEstimationTimeRangeTypeDef(TypedDict, total=False):
    StartTime: datetime
    EndTime: datetime


class DescribeAccountHealthResponseTypeDef(TypedDict):
    OpenReactiveInsights: int
    OpenProactiveInsights: int
    MetricsAnalyzed: int
    ResourceHours: int


class DescribeAccountOverviewResponseTypeDef(TypedDict):
    ReactiveInsights: int
    ProactiveInsights: int
    MeanTimeToRecoverInMilliseconds: int


class DescribeAnomalyResponseTypeDef(TypedDict, total=False):
    ProactiveAnomaly: "ProactiveAnomalyTypeDef"
    ReactiveAnomaly: "ReactiveAnomalyTypeDef"


class DescribeFeedbackResponseTypeDef(TypedDict, total=False):
    InsightFeedback: "InsightFeedbackTypeDef"


class DescribeInsightResponseTypeDef(TypedDict, total=False):
    ProactiveInsight: "ProactiveInsightTypeDef"
    ReactiveInsight: "ReactiveInsightTypeDef"


class _RequiredDescribeResourceCollectionHealthResponseTypeDef(TypedDict):
    CloudFormation: List["CloudFormationHealthTypeDef"]


class DescribeResourceCollectionHealthResponseTypeDef(
    _RequiredDescribeResourceCollectionHealthResponseTypeDef, total=False
):
    Service: List["ServiceHealthTypeDef"]
    NextToken: str


class DescribeServiceIntegrationResponseTypeDef(TypedDict, total=False):
    ServiceIntegration: "ServiceIntegrationConfigTypeDef"


class EndTimeRangeTypeDef(TypedDict, total=False):
    FromTime: datetime
    ToTime: datetime


EventResourceTypeDef = TypedDict(
    "EventResourceTypeDef", {"Type": str, "Name": str, "Arn": str}, total=False
)


class EventTimeRangeTypeDef(TypedDict):
    FromTime: datetime
    ToTime: datetime


class EventTypeDef(TypedDict, total=False):
    ResourceCollection: "ResourceCollectionTypeDef"
    Id: str
    Time: datetime
    EventSource: str
    Name: str
    DataSource: EventDataSource
    EventClass: EventClass
    Resources: List["EventResourceTypeDef"]


class GetCostEstimationResponseTypeDef(TypedDict, total=False):
    ResourceCollection: "CostEstimationResourceCollectionFilterTypeDef"
    Status: CostEstimationStatus
    Costs: List["ServiceResourceCostTypeDef"]
    TimeRange: "CostEstimationTimeRangeTypeDef"
    TotalCost: float
    NextToken: str


class GetResourceCollectionResponseTypeDef(TypedDict, total=False):
    ResourceCollection: "ResourceCollectionFilterTypeDef"
    NextToken: str


class InsightFeedbackTypeDef(TypedDict, total=False):
    Id: str
    Feedback: InsightFeedbackOption


class InsightHealthTypeDef(TypedDict, total=False):
    OpenProactiveInsights: int
    OpenReactiveInsights: int
    MeanTimeToRecoverInMilliseconds: int


class _RequiredInsightTimeRangeTypeDef(TypedDict):
    StartTime: datetime


class InsightTimeRangeTypeDef(_RequiredInsightTimeRangeTypeDef, total=False):
    EndTime: datetime


class ListAnomaliesForInsightResponseTypeDef(TypedDict, total=False):
    ProactiveAnomalies: List["ProactiveAnomalySummaryTypeDef"]
    ReactiveAnomalies: List["ReactiveAnomalySummaryTypeDef"]
    NextToken: str


class ListEventsFiltersTypeDef(TypedDict, total=False):
    InsightId: str
    EventTimeRange: "EventTimeRangeTypeDef"
    EventClass: EventClass
    EventSource: str
    DataSource: EventDataSource
    ResourceCollection: "ResourceCollectionTypeDef"


class _RequiredListEventsResponseTypeDef(TypedDict):
    Events: List["EventTypeDef"]


class ListEventsResponseTypeDef(_RequiredListEventsResponseTypeDef, total=False):
    NextToken: str


ListInsightsAnyStatusFilterTypeDef = TypedDict(
    "ListInsightsAnyStatusFilterTypeDef",
    {"Type": InsightType, "StartTimeRange": "StartTimeRangeTypeDef"},
)

ListInsightsClosedStatusFilterTypeDef = TypedDict(
    "ListInsightsClosedStatusFilterTypeDef",
    {"Type": InsightType, "EndTimeRange": "EndTimeRangeTypeDef"},
)

ListInsightsOngoingStatusFilterTypeDef = TypedDict(
    "ListInsightsOngoingStatusFilterTypeDef", {"Type": InsightType}
)


class ListInsightsResponseTypeDef(TypedDict, total=False):
    ProactiveInsights: List["ProactiveInsightSummaryTypeDef"]
    ReactiveInsights: List["ReactiveInsightSummaryTypeDef"]
    NextToken: str


ListInsightsStatusFilterTypeDef = TypedDict(
    "ListInsightsStatusFilterTypeDef",
    {
        "Ongoing": "ListInsightsOngoingStatusFilterTypeDef",
        "Closed": "ListInsightsClosedStatusFilterTypeDef",
        "Any": "ListInsightsAnyStatusFilterTypeDef",
    },
    total=False,
)


class ListNotificationChannelsResponseTypeDef(TypedDict, total=False):
    Channels: List["NotificationChannelTypeDef"]
    NextToken: str


class ListRecommendationsResponseTypeDef(TypedDict, total=False):
    Recommendations: List["RecommendationTypeDef"]
    NextToken: str


class NotificationChannelConfigTypeDef(TypedDict):
    Sns: "SnsChannelConfigTypeDef"


class NotificationChannelTypeDef(TypedDict, total=False):
    Id: str
    Config: "NotificationChannelConfigTypeDef"


class OpsCenterIntegrationConfigTypeDef(TypedDict, total=False):
    OptInStatus: OptInStatus


class OpsCenterIntegrationTypeDef(TypedDict, total=False):
    OptInStatus: OptInStatus


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredPredictionTimeRangeTypeDef(TypedDict):
    StartTime: datetime


class PredictionTimeRangeTypeDef(_RequiredPredictionTimeRangeTypeDef, total=False):
    EndTime: datetime


class ProactiveAnomalySummaryTypeDef(TypedDict, total=False):
    Id: str
    Severity: AnomalySeverity
    Status: AnomalyStatus
    UpdateTime: datetime
    AnomalyTimeRange: "AnomalyTimeRangeTypeDef"
    PredictionTimeRange: "PredictionTimeRangeTypeDef"
    SourceDetails: "AnomalySourceDetailsTypeDef"
    AssociatedInsightId: str
    ResourceCollection: "ResourceCollectionTypeDef"
    Limit: float


class ProactiveAnomalyTypeDef(TypedDict, total=False):
    Id: str
    Severity: AnomalySeverity
    Status: AnomalyStatus
    UpdateTime: datetime
    AnomalyTimeRange: "AnomalyTimeRangeTypeDef"
    PredictionTimeRange: "PredictionTimeRangeTypeDef"
    SourceDetails: "AnomalySourceDetailsTypeDef"
    AssociatedInsightId: str
    ResourceCollection: "ResourceCollectionTypeDef"
    Limit: float


class ProactiveInsightSummaryTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Severity: InsightSeverity
    Status: InsightStatus
    InsightTimeRange: "InsightTimeRangeTypeDef"
    PredictionTimeRange: "PredictionTimeRangeTypeDef"
    ResourceCollection: "ResourceCollectionTypeDef"
    ServiceCollection: "ServiceCollectionTypeDef"


class ProactiveInsightTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Severity: InsightSeverity
    Status: InsightStatus
    InsightTimeRange: "InsightTimeRangeTypeDef"
    PredictionTimeRange: "PredictionTimeRangeTypeDef"
    ResourceCollection: "ResourceCollectionTypeDef"
    SsmOpsItemId: str


class ReactiveAnomalySummaryTypeDef(TypedDict, total=False):
    Id: str
    Severity: AnomalySeverity
    Status: AnomalyStatus
    AnomalyTimeRange: "AnomalyTimeRangeTypeDef"
    SourceDetails: "AnomalySourceDetailsTypeDef"
    AssociatedInsightId: str
    ResourceCollection: "ResourceCollectionTypeDef"


class ReactiveAnomalyTypeDef(TypedDict, total=False):
    Id: str
    Severity: AnomalySeverity
    Status: AnomalyStatus
    AnomalyTimeRange: "AnomalyTimeRangeTypeDef"
    SourceDetails: "AnomalySourceDetailsTypeDef"
    AssociatedInsightId: str
    ResourceCollection: "ResourceCollectionTypeDef"


class ReactiveInsightSummaryTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Severity: InsightSeverity
    Status: InsightStatus
    InsightTimeRange: "InsightTimeRangeTypeDef"
    ResourceCollection: "ResourceCollectionTypeDef"
    ServiceCollection: "ServiceCollectionTypeDef"


class ReactiveInsightTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Severity: InsightSeverity
    Status: InsightStatus
    InsightTimeRange: "InsightTimeRangeTypeDef"
    ResourceCollection: "ResourceCollectionTypeDef"
    SsmOpsItemId: str


RecommendationRelatedAnomalyResourceTypeDef = TypedDict(
    "RecommendationRelatedAnomalyResourceTypeDef", {"Name": str, "Type": str}, total=False
)


class RecommendationRelatedAnomalySourceDetailTypeDef(TypedDict, total=False):
    CloudWatchMetrics: List["RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef"]


class RecommendationRelatedAnomalyTypeDef(TypedDict, total=False):
    Resources: List["RecommendationRelatedAnomalyResourceTypeDef"]
    SourceDetails: List["RecommendationRelatedAnomalySourceDetailTypeDef"]


class RecommendationRelatedCloudWatchMetricsSourceDetailTypeDef(TypedDict, total=False):
    MetricName: str
    Namespace: str


RecommendationRelatedEventResourceTypeDef = TypedDict(
    "RecommendationRelatedEventResourceTypeDef", {"Name": str, "Type": str}, total=False
)


class RecommendationRelatedEventTypeDef(TypedDict, total=False):
    Name: str
    Resources: List["RecommendationRelatedEventResourceTypeDef"]


class RecommendationTypeDef(TypedDict, total=False):
    Description: str
    Link: str
    Name: str
    Reason: str
    RelatedEvents: List["RecommendationRelatedEventTypeDef"]
    RelatedAnomalies: List["RecommendationRelatedAnomalyTypeDef"]


class ResourceCollectionFilterTypeDef(TypedDict, total=False):
    CloudFormation: "CloudFormationCollectionFilterTypeDef"


class ResourceCollectionTypeDef(TypedDict, total=False):
    CloudFormation: "CloudFormationCollectionTypeDef"


class SearchInsightsFiltersTypeDef(TypedDict, total=False):
    Severities: List[InsightSeverity]
    Statuses: List[InsightStatus]
    ResourceCollection: "ResourceCollectionTypeDef"
    ServiceCollection: "ServiceCollectionTypeDef"


class SearchInsightsResponseTypeDef(TypedDict, total=False):
    ProactiveInsights: List["ProactiveInsightSummaryTypeDef"]
    ReactiveInsights: List["ReactiveInsightSummaryTypeDef"]
    NextToken: str


class ServiceCollectionTypeDef(TypedDict, total=False):
    ServiceNames: List[ServiceName]


class ServiceHealthTypeDef(TypedDict, total=False):
    ServiceName: ServiceName
    Insight: "ServiceInsightHealthTypeDef"


class ServiceInsightHealthTypeDef(TypedDict, total=False):
    OpenProactiveInsights: int
    OpenReactiveInsights: int


class ServiceIntegrationConfigTypeDef(TypedDict, total=False):
    OpsCenter: "OpsCenterIntegrationTypeDef"


ServiceResourceCostTypeDef = TypedDict(
    "ServiceResourceCostTypeDef",
    {
        "Type": str,
        "State": CostEstimationServiceResourceState,
        "Count": int,
        "UnitCost": float,
        "Cost": float,
    },
    total=False,
)


class SnsChannelConfigTypeDef(TypedDict, total=False):
    TopicArn: str


class StartTimeRangeTypeDef(TypedDict, total=False):
    FromTime: datetime
    ToTime: datetime


class UpdateCloudFormationCollectionFilterTypeDef(TypedDict, total=False):
    StackNames: List[str]


class UpdateResourceCollectionFilterTypeDef(TypedDict, total=False):
    CloudFormation: "UpdateCloudFormationCollectionFilterTypeDef"


class UpdateServiceIntegrationConfigTypeDef(TypedDict, total=False):
    OpsCenter: "OpsCenterIntegrationConfigTypeDef"
