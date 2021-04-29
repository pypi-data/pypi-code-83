"""
Main interface for devops-guru service client

Usage::

    ```python
    import boto3
    from mypy_boto3_devops_guru import DevopsGuruClient

    client: DevopsGuruClient = boto3.client("devops-guru")
    ```
"""
from datetime import datetime
from typing import Any, Dict, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_devops_guru.literals import (
    DescribeResourceCollectionHealthPaginatorName,
    GetResourceCollectionPaginatorName,
    InsightType,
    ListAnomaliesForInsightPaginatorName,
    ListEventsPaginatorName,
    ListInsightsPaginatorName,
    ListNotificationChannelsPaginatorName,
    ListRecommendationsPaginatorName,
    ResourceCollectionType,
    SearchInsightsPaginatorName,
    UpdateResourceCollectionAction,
)
from mypy_boto3_devops_guru.paginator import (
    DescribeResourceCollectionHealthPaginator,
    GetResourceCollectionPaginator,
    ListAnomaliesForInsightPaginator,
    ListEventsPaginator,
    ListInsightsPaginator,
    ListNotificationChannelsPaginator,
    ListRecommendationsPaginator,
    SearchInsightsPaginator,
)
from mypy_boto3_devops_guru.type_defs import (
    AddNotificationChannelResponseTypeDef,
    DescribeAccountHealthResponseTypeDef,
    DescribeAccountOverviewResponseTypeDef,
    DescribeAnomalyResponseTypeDef,
    DescribeFeedbackResponseTypeDef,
    DescribeInsightResponseTypeDef,
    DescribeResourceCollectionHealthResponseTypeDef,
    DescribeServiceIntegrationResponseTypeDef,
    GetResourceCollectionResponseTypeDef,
    InsightFeedbackTypeDef,
    ListAnomaliesForInsightResponseTypeDef,
    ListEventsFiltersTypeDef,
    ListEventsResponseTypeDef,
    ListInsightsResponseTypeDef,
    ListInsightsStatusFilterTypeDef,
    ListNotificationChannelsResponseTypeDef,
    ListRecommendationsResponseTypeDef,
    NotificationChannelConfigTypeDef,
    SearchInsightsFiltersTypeDef,
    SearchInsightsResponseTypeDef,
    StartTimeRangeTypeDef,
    UpdateResourceCollectionFilterTypeDef,
    UpdateServiceIntegrationConfigTypeDef,
)

__all__ = ("DevopsGuruClient",)


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
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class DevopsGuruClient:
    """
    [DevopsGuru.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_notification_channel(
        self, Config: "NotificationChannelConfigTypeDef"
    ) -> AddNotificationChannelResponseTypeDef:
        """
        [Client.add_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.add_notification_channel)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.can_paginate)
        """

    def describe_account_health(self) -> DescribeAccountHealthResponseTypeDef:
        """
        [Client.describe_account_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.describe_account_health)
        """

    def describe_account_overview(
        self, FromTime: datetime, ToTime: datetime = None
    ) -> DescribeAccountOverviewResponseTypeDef:
        """
        [Client.describe_account_overview documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.describe_account_overview)
        """

    def describe_anomaly(self, Id: str) -> DescribeAnomalyResponseTypeDef:
        """
        [Client.describe_anomaly documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.describe_anomaly)
        """

    def describe_feedback(self, InsightId: str = None) -> DescribeFeedbackResponseTypeDef:
        """
        [Client.describe_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.describe_feedback)
        """

    def describe_insight(self, Id: str) -> DescribeInsightResponseTypeDef:
        """
        [Client.describe_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.describe_insight)
        """

    def describe_resource_collection_health(
        self, ResourceCollectionType: ResourceCollectionType, NextToken: str = None
    ) -> DescribeResourceCollectionHealthResponseTypeDef:
        """
        [Client.describe_resource_collection_health documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.describe_resource_collection_health)
        """

    def describe_service_integration(self) -> DescribeServiceIntegrationResponseTypeDef:
        """
        [Client.describe_service_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.describe_service_integration)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.generate_presigned_url)
        """

    def get_resource_collection(
        self, ResourceCollectionType: ResourceCollectionType, NextToken: str = None
    ) -> GetResourceCollectionResponseTypeDef:
        """
        [Client.get_resource_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.get_resource_collection)
        """

    def list_anomalies_for_insight(
        self,
        InsightId: str,
        StartTimeRange: "StartTimeRangeTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListAnomaliesForInsightResponseTypeDef:
        """
        [Client.list_anomalies_for_insight documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.list_anomalies_for_insight)
        """

    def list_events(
        self, Filters: ListEventsFiltersTypeDef, MaxResults: int = None, NextToken: str = None
    ) -> ListEventsResponseTypeDef:
        """
        [Client.list_events documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.list_events)
        """

    def list_insights(
        self,
        StatusFilter: ListInsightsStatusFilterTypeDef,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListInsightsResponseTypeDef:
        """
        [Client.list_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.list_insights)
        """

    def list_notification_channels(
        self, NextToken: str = None
    ) -> ListNotificationChannelsResponseTypeDef:
        """
        [Client.list_notification_channels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.list_notification_channels)
        """

    def list_recommendations(
        self, InsightId: str, NextToken: str = None
    ) -> ListRecommendationsResponseTypeDef:
        """
        [Client.list_recommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.list_recommendations)
        """

    def put_feedback(self, InsightFeedback: "InsightFeedbackTypeDef" = None) -> Dict[str, Any]:
        """
        [Client.put_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.put_feedback)
        """

    def remove_notification_channel(self, Id: str) -> Dict[str, Any]:
        """
        [Client.remove_notification_channel documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.remove_notification_channel)
        """

    def search_insights(
        self,
        StartTimeRange: "StartTimeRangeTypeDef",
        Type: InsightType,
        Filters: SearchInsightsFiltersTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> SearchInsightsResponseTypeDef:
        """
        [Client.search_insights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.search_insights)
        """

    def update_resource_collection(
        self,
        Action: UpdateResourceCollectionAction,
        ResourceCollection: UpdateResourceCollectionFilterTypeDef,
    ) -> Dict[str, Any]:
        """
        [Client.update_resource_collection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.update_resource_collection)
        """

    def update_service_integration(
        self, ServiceIntegration: UpdateServiceIntegrationConfigTypeDef
    ) -> Dict[str, Any]:
        """
        [Client.update_service_integration documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Client.update_service_integration)
        """

    @overload
    def get_paginator(
        self, operation_name: DescribeResourceCollectionHealthPaginatorName
    ) -> DescribeResourceCollectionHealthPaginator:
        """
        [Paginator.DescribeResourceCollectionHealth documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Paginator.DescribeResourceCollectionHealth)
        """

    @overload
    def get_paginator(
        self, operation_name: GetResourceCollectionPaginatorName
    ) -> GetResourceCollectionPaginator:
        """
        [Paginator.GetResourceCollection documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Paginator.GetResourceCollection)
        """

    @overload
    def get_paginator(
        self, operation_name: ListAnomaliesForInsightPaginatorName
    ) -> ListAnomaliesForInsightPaginator:
        """
        [Paginator.ListAnomaliesForInsight documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Paginator.ListAnomaliesForInsight)
        """

    @overload
    def get_paginator(self, operation_name: ListEventsPaginatorName) -> ListEventsPaginator:
        """
        [Paginator.ListEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Paginator.ListEvents)
        """

    @overload
    def get_paginator(self, operation_name: ListInsightsPaginatorName) -> ListInsightsPaginator:
        """
        [Paginator.ListInsights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Paginator.ListInsights)
        """

    @overload
    def get_paginator(
        self, operation_name: ListNotificationChannelsPaginatorName
    ) -> ListNotificationChannelsPaginator:
        """
        [Paginator.ListNotificationChannels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Paginator.ListNotificationChannels)
        """

    @overload
    def get_paginator(
        self, operation_name: ListRecommendationsPaginatorName
    ) -> ListRecommendationsPaginator:
        """
        [Paginator.ListRecommendations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Paginator.ListRecommendations)
        """

    @overload
    def get_paginator(self, operation_name: SearchInsightsPaginatorName) -> SearchInsightsPaginator:
        """
        [Paginator.SearchInsights documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/devops-guru.html#DevopsGuru.Paginator.SearchInsights)
        """
