"""
Main interface for ce service client

Usage::

    ```python
    import boto3
    from mypy_boto3_ce import CostExplorerClient

    client: CostExplorerClient = boto3.client("ce")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_ce.literals import (
    AccountScope,
    AnomalyFeedbackType,
    AnomalySubscriptionFrequency,
    Context,
    CostCategoryRuleVersion,
    Dimension,
    Granularity,
    LookbackPeriodInDays,
    Metric,
    PaymentOption,
    SavingsPlansDataType,
    SupportedSavingsPlansType,
    TermInYears,
)
from mypy_boto3_ce.type_defs import (
    AnomalyDateIntervalTypeDef,
    AnomalyMonitorTypeDef,
    AnomalySubscriptionTypeDef,
    CostCategoryRuleTypeDef,
    CreateAnomalyMonitorResponseTypeDef,
    CreateAnomalySubscriptionResponseTypeDef,
    CreateCostCategoryDefinitionResponseTypeDef,
    DateIntervalTypeDef,
    DeleteCostCategoryDefinitionResponseTypeDef,
    DescribeCostCategoryDefinitionResponseTypeDef,
    GetAnomaliesResponseTypeDef,
    GetAnomalyMonitorsResponseTypeDef,
    GetAnomalySubscriptionsResponseTypeDef,
    GetCostAndUsageResponseTypeDef,
    GetCostAndUsageWithResourcesResponseTypeDef,
    GetCostCategoriesResponseTypeDef,
    GetCostForecastResponseTypeDef,
    GetDimensionValuesResponseTypeDef,
    GetReservationCoverageResponseTypeDef,
    GetReservationPurchaseRecommendationResponseTypeDef,
    GetReservationUtilizationResponseTypeDef,
    GetRightsizingRecommendationResponseTypeDef,
    GetSavingsPlansCoverageResponseTypeDef,
    GetSavingsPlansPurchaseRecommendationResponseTypeDef,
    GetSavingsPlansUtilizationDetailsResponseTypeDef,
    GetSavingsPlansUtilizationResponseTypeDef,
    GetTagsResponseTypeDef,
    GetUsageForecastResponseTypeDef,
    GroupDefinitionTypeDef,
    ListCostCategoryDefinitionsResponseTypeDef,
    ProvideAnomalyFeedbackResponseTypeDef,
    RightsizingRecommendationConfigurationTypeDef,
    ServiceSpecificationTypeDef,
    SortDefinitionTypeDef,
    SubscriberTypeDef,
    TotalImpactFilterTypeDef,
    UpdateAnomalyMonitorResponseTypeDef,
    UpdateAnomalySubscriptionResponseTypeDef,
    UpdateCostCategoryDefinitionResponseTypeDef,
)

__all__ = ("CostExplorerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BillExpirationException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    DataUnavailableException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    RequestChangedException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    UnknownMonitorException: Type[BotocoreClientError]
    UnknownSubscriptionException: Type[BotocoreClientError]
    UnresolvableUsageUnitException: Type[BotocoreClientError]


class CostExplorerClient:
    """
    [CostExplorer.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.can_paginate)
        """

    def create_anomaly_monitor(
        self, AnomalyMonitor: "AnomalyMonitorTypeDef"
    ) -> CreateAnomalyMonitorResponseTypeDef:
        """
        [Client.create_anomaly_monitor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.create_anomaly_monitor)
        """

    def create_anomaly_subscription(
        self, AnomalySubscription: "AnomalySubscriptionTypeDef"
    ) -> CreateAnomalySubscriptionResponseTypeDef:
        """
        [Client.create_anomaly_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.create_anomaly_subscription)
        """

    def create_cost_category_definition(
        self,
        Name: str,
        RuleVersion: CostCategoryRuleVersion,
        Rules: List["CostCategoryRuleTypeDef"],
        DefaultValue: str = None,
    ) -> CreateCostCategoryDefinitionResponseTypeDef:
        """
        [Client.create_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.create_cost_category_definition)
        """

    def delete_anomaly_monitor(self, MonitorArn: str) -> Dict[str, Any]:
        """
        [Client.delete_anomaly_monitor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.delete_anomaly_monitor)
        """

    def delete_anomaly_subscription(self, SubscriptionArn: str) -> Dict[str, Any]:
        """
        [Client.delete_anomaly_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.delete_anomaly_subscription)
        """

    def delete_cost_category_definition(
        self, CostCategoryArn: str
    ) -> DeleteCostCategoryDefinitionResponseTypeDef:
        """
        [Client.delete_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.delete_cost_category_definition)
        """

    def describe_cost_category_definition(
        self, CostCategoryArn: str, EffectiveOn: str = None
    ) -> DescribeCostCategoryDefinitionResponseTypeDef:
        """
        [Client.describe_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.describe_cost_category_definition)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.generate_presigned_url)
        """

    def get_anomalies(
        self,
        DateInterval: AnomalyDateIntervalTypeDef,
        MonitorArn: str = None,
        Feedback: AnomalyFeedbackType = None,
        TotalImpact: TotalImpactFilterTypeDef = None,
        NextPageToken: str = None,
        MaxResults: int = None,
    ) -> GetAnomaliesResponseTypeDef:
        """
        [Client.get_anomalies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_anomalies)
        """

    def get_anomaly_monitors(
        self, MonitorArnList: List[str] = None, NextPageToken: str = None, MaxResults: int = None
    ) -> GetAnomalyMonitorsResponseTypeDef:
        """
        [Client.get_anomaly_monitors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_anomaly_monitors)
        """

    def get_anomaly_subscriptions(
        self,
        SubscriptionArnList: List[str] = None,
        MonitorArn: str = None,
        NextPageToken: str = None,
        MaxResults: int = None,
    ) -> GetAnomalySubscriptionsResponseTypeDef:
        """
        [Client.get_anomaly_subscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_anomaly_subscriptions)
        """

    def get_cost_and_usage(
        self,
        TimePeriod: "DateIntervalTypeDef",
        Granularity: Granularity,
        Metrics: List[str],
        Filter: Dict[str, Any] = None,
        GroupBy: List["GroupDefinitionTypeDef"] = None,
        NextPageToken: str = None,
    ) -> GetCostAndUsageResponseTypeDef:
        """
        [Client.get_cost_and_usage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_cost_and_usage)
        """

    def get_cost_and_usage_with_resources(
        self,
        TimePeriod: "DateIntervalTypeDef",
        Granularity: Granularity,
        Filter: Dict[str, Any],
        Metrics: List[str] = None,
        GroupBy: List["GroupDefinitionTypeDef"] = None,
        NextPageToken: str = None,
    ) -> GetCostAndUsageWithResourcesResponseTypeDef:
        """
        [Client.get_cost_and_usage_with_resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_cost_and_usage_with_resources)
        """

    def get_cost_categories(
        self,
        TimePeriod: "DateIntervalTypeDef",
        SearchString: str = None,
        CostCategoryName: str = None,
        Filter: Dict[str, Any] = None,
        SortBy: List[SortDefinitionTypeDef] = None,
        MaxResults: int = None,
        NextPageToken: str = None,
    ) -> GetCostCategoriesResponseTypeDef:
        """
        [Client.get_cost_categories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_cost_categories)
        """

    def get_cost_forecast(
        self,
        TimePeriod: "DateIntervalTypeDef",
        Metric: Metric,
        Granularity: Granularity,
        Filter: Dict[str, Any] = None,
        PredictionIntervalLevel: int = None,
    ) -> GetCostForecastResponseTypeDef:
        """
        [Client.get_cost_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_cost_forecast)
        """

    def get_dimension_values(
        self,
        TimePeriod: "DateIntervalTypeDef",
        Dimension: Dimension,
        SearchString: str = None,
        Context: Context = None,
        Filter: Dict[str, Any] = None,
        SortBy: List[SortDefinitionTypeDef] = None,
        MaxResults: int = None,
        NextPageToken: str = None,
    ) -> GetDimensionValuesResponseTypeDef:
        """
        [Client.get_dimension_values documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_dimension_values)
        """

    def get_reservation_coverage(
        self,
        TimePeriod: "DateIntervalTypeDef",
        GroupBy: List["GroupDefinitionTypeDef"] = None,
        Granularity: Granularity = None,
        Filter: Dict[str, Any] = None,
        Metrics: List[str] = None,
        NextPageToken: str = None,
        SortBy: SortDefinitionTypeDef = None,
        MaxResults: int = None,
    ) -> GetReservationCoverageResponseTypeDef:
        """
        [Client.get_reservation_coverage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_reservation_coverage)
        """

    def get_reservation_purchase_recommendation(
        self,
        Service: str,
        AccountId: str = None,
        Filter: Dict[str, Any] = None,
        AccountScope: AccountScope = None,
        LookbackPeriodInDays: LookbackPeriodInDays = None,
        TermInYears: TermInYears = None,
        PaymentOption: PaymentOption = None,
        ServiceSpecification: "ServiceSpecificationTypeDef" = None,
        PageSize: int = None,
        NextPageToken: str = None,
    ) -> GetReservationPurchaseRecommendationResponseTypeDef:
        """
        [Client.get_reservation_purchase_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_reservation_purchase_recommendation)
        """

    def get_reservation_utilization(
        self,
        TimePeriod: "DateIntervalTypeDef",
        GroupBy: List["GroupDefinitionTypeDef"] = None,
        Granularity: Granularity = None,
        Filter: Dict[str, Any] = None,
        SortBy: SortDefinitionTypeDef = None,
        NextPageToken: str = None,
        MaxResults: int = None,
    ) -> GetReservationUtilizationResponseTypeDef:
        """
        [Client.get_reservation_utilization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_reservation_utilization)
        """

    def get_rightsizing_recommendation(
        self,
        Service: str,
        Filter: Dict[str, Any] = None,
        Configuration: "RightsizingRecommendationConfigurationTypeDef" = None,
        PageSize: int = None,
        NextPageToken: str = None,
    ) -> GetRightsizingRecommendationResponseTypeDef:
        """
        [Client.get_rightsizing_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_rightsizing_recommendation)
        """

    def get_savings_plans_coverage(
        self,
        TimePeriod: "DateIntervalTypeDef",
        GroupBy: List["GroupDefinitionTypeDef"] = None,
        Granularity: Granularity = None,
        Filter: Dict[str, Any] = None,
        Metrics: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        SortBy: SortDefinitionTypeDef = None,
    ) -> GetSavingsPlansCoverageResponseTypeDef:
        """
        [Client.get_savings_plans_coverage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_savings_plans_coverage)
        """

    def get_savings_plans_purchase_recommendation(
        self,
        SavingsPlansType: SupportedSavingsPlansType,
        TermInYears: TermInYears,
        PaymentOption: PaymentOption,
        LookbackPeriodInDays: LookbackPeriodInDays,
        AccountScope: AccountScope = None,
        NextPageToken: str = None,
        PageSize: int = None,
        Filter: Dict[str, Any] = None,
    ) -> GetSavingsPlansPurchaseRecommendationResponseTypeDef:
        """
        [Client.get_savings_plans_purchase_recommendation documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_savings_plans_purchase_recommendation)
        """

    def get_savings_plans_utilization(
        self,
        TimePeriod: "DateIntervalTypeDef",
        Granularity: Granularity = None,
        Filter: Dict[str, Any] = None,
        SortBy: SortDefinitionTypeDef = None,
    ) -> GetSavingsPlansUtilizationResponseTypeDef:
        """
        [Client.get_savings_plans_utilization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_savings_plans_utilization)
        """

    def get_savings_plans_utilization_details(
        self,
        TimePeriod: "DateIntervalTypeDef",
        Filter: Dict[str, Any] = None,
        DataType: List[SavingsPlansDataType] = None,
        NextToken: str = None,
        MaxResults: int = None,
        SortBy: SortDefinitionTypeDef = None,
    ) -> GetSavingsPlansUtilizationDetailsResponseTypeDef:
        """
        [Client.get_savings_plans_utilization_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_savings_plans_utilization_details)
        """

    def get_tags(
        self,
        TimePeriod: "DateIntervalTypeDef",
        SearchString: str = None,
        TagKey: str = None,
        Filter: Dict[str, Any] = None,
        SortBy: List[SortDefinitionTypeDef] = None,
        MaxResults: int = None,
        NextPageToken: str = None,
    ) -> GetTagsResponseTypeDef:
        """
        [Client.get_tags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_tags)
        """

    def get_usage_forecast(
        self,
        TimePeriod: "DateIntervalTypeDef",
        Metric: Metric,
        Granularity: Granularity,
        Filter: Dict[str, Any] = None,
        PredictionIntervalLevel: int = None,
    ) -> GetUsageForecastResponseTypeDef:
        """
        [Client.get_usage_forecast documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.get_usage_forecast)
        """

    def list_cost_category_definitions(
        self, EffectiveOn: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListCostCategoryDefinitionsResponseTypeDef:
        """
        [Client.list_cost_category_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.list_cost_category_definitions)
        """

    def provide_anomaly_feedback(
        self, AnomalyId: str, Feedback: AnomalyFeedbackType
    ) -> ProvideAnomalyFeedbackResponseTypeDef:
        """
        [Client.provide_anomaly_feedback documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.provide_anomaly_feedback)
        """

    def update_anomaly_monitor(
        self, MonitorArn: str, MonitorName: str = None
    ) -> UpdateAnomalyMonitorResponseTypeDef:
        """
        [Client.update_anomaly_monitor documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.update_anomaly_monitor)
        """

    def update_anomaly_subscription(
        self,
        SubscriptionArn: str,
        Threshold: float = None,
        Frequency: AnomalySubscriptionFrequency = None,
        MonitorArnList: List[str] = None,
        Subscribers: List["SubscriberTypeDef"] = None,
        SubscriptionName: str = None,
    ) -> UpdateAnomalySubscriptionResponseTypeDef:
        """
        [Client.update_anomaly_subscription documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.update_anomaly_subscription)
        """

    def update_cost_category_definition(
        self,
        CostCategoryArn: str,
        RuleVersion: CostCategoryRuleVersion,
        Rules: List["CostCategoryRuleTypeDef"],
        DefaultValue: str = None,
    ) -> UpdateCostCategoryDefinitionResponseTypeDef:
        """
        [Client.update_cost_category_definition documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/ce.html#CostExplorer.Client.update_cost_category_definition)
        """
