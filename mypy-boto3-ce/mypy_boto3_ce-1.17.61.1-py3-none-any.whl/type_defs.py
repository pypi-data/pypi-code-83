"""
Type annotations for ce service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ce.type_defs import AnomalyDateIntervalTypeDef

    data: AnomalyDateIntervalTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from mypy_boto3_ce.literals import (
    AccountScope,
    AnomalyFeedbackType,
    AnomalySubscriptionFrequency,
    CostCategoryInheritedValueDimensionName,
    CostCategoryRuleType,
    CostCategoryStatus,
    Dimension,
    GroupDefinitionType,
    LookbackPeriodInDays,
    MatchOption,
    MonitorType,
    NumericOperator,
    OfferingClass,
    PaymentOption,
    RecommendationTarget,
    RightsizingType,
    SortOrder,
    SubscriberStatus,
    SubscriberType,
    SupportedSavingsPlansType,
    TermInYears,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AnomalyDateIntervalTypeDef",
    "AnomalyMonitorTypeDef",
    "AnomalyScoreTypeDef",
    "AnomalySubscriptionTypeDef",
    "AnomalyTypeDef",
    "CostCategoryInheritedValueDimensionTypeDef",
    "CostCategoryProcessingStatusTypeDef",
    "CostCategoryReferenceTypeDef",
    "CostCategoryRuleTypeDef",
    "CostCategoryTypeDef",
    "CostCategoryValuesTypeDef",
    "CoverageByTimeTypeDef",
    "CoverageCostTypeDef",
    "CoverageHoursTypeDef",
    "CoverageNormalizedUnitsTypeDef",
    "CoverageTypeDef",
    "CreateAnomalyMonitorResponseTypeDef",
    "CreateAnomalySubscriptionResponseTypeDef",
    "CreateCostCategoryDefinitionResponseTypeDef",
    "CurrentInstanceTypeDef",
    "DateIntervalTypeDef",
    "DeleteCostCategoryDefinitionResponseTypeDef",
    "DescribeCostCategoryDefinitionResponseTypeDef",
    "DimensionValuesTypeDef",
    "DimensionValuesWithAttributesTypeDef",
    "EBSResourceUtilizationTypeDef",
    "EC2InstanceDetailsTypeDef",
    "EC2ResourceDetailsTypeDef",
    "EC2ResourceUtilizationTypeDef",
    "EC2SpecificationTypeDef",
    "ESInstanceDetailsTypeDef",
    "ElastiCacheInstanceDetailsTypeDef",
    "ExpressionTypeDef",
    "ForecastResultTypeDef",
    "GetAnomaliesResponseTypeDef",
    "GetAnomalyMonitorsResponseTypeDef",
    "GetAnomalySubscriptionsResponseTypeDef",
    "GetCostAndUsageResponseTypeDef",
    "GetCostAndUsageWithResourcesResponseTypeDef",
    "GetCostCategoriesResponseTypeDef",
    "GetCostForecastResponseTypeDef",
    "GetDimensionValuesResponseTypeDef",
    "GetReservationCoverageResponseTypeDef",
    "GetReservationPurchaseRecommendationResponseTypeDef",
    "GetReservationUtilizationResponseTypeDef",
    "GetRightsizingRecommendationResponseTypeDef",
    "GetSavingsPlansCoverageResponseTypeDef",
    "GetSavingsPlansPurchaseRecommendationResponseTypeDef",
    "GetSavingsPlansUtilizationDetailsResponseTypeDef",
    "GetSavingsPlansUtilizationResponseTypeDef",
    "GetTagsResponseTypeDef",
    "GetUsageForecastResponseTypeDef",
    "GroupDefinitionTypeDef",
    "GroupTypeDef",
    "ImpactTypeDef",
    "InstanceDetailsTypeDef",
    "ListCostCategoryDefinitionsResponseTypeDef",
    "MetricValueTypeDef",
    "ModifyRecommendationDetailTypeDef",
    "ProvideAnomalyFeedbackResponseTypeDef",
    "RDSInstanceDetailsTypeDef",
    "RedshiftInstanceDetailsTypeDef",
    "ReservationAggregatesTypeDef",
    "ReservationCoverageGroupTypeDef",
    "ReservationPurchaseRecommendationDetailTypeDef",
    "ReservationPurchaseRecommendationMetadataTypeDef",
    "ReservationPurchaseRecommendationSummaryTypeDef",
    "ReservationPurchaseRecommendationTypeDef",
    "ReservationUtilizationGroupTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceUtilizationTypeDef",
    "ResultByTimeTypeDef",
    "RightsizingRecommendationConfigurationTypeDef",
    "RightsizingRecommendationMetadataTypeDef",
    "RightsizingRecommendationSummaryTypeDef",
    "RightsizingRecommendationTypeDef",
    "RootCauseTypeDef",
    "SavingsPlansAmortizedCommitmentTypeDef",
    "SavingsPlansCoverageDataTypeDef",
    "SavingsPlansCoverageTypeDef",
    "SavingsPlansDetailsTypeDef",
    "SavingsPlansPurchaseRecommendationDetailTypeDef",
    "SavingsPlansPurchaseRecommendationMetadataTypeDef",
    "SavingsPlansPurchaseRecommendationSummaryTypeDef",
    "SavingsPlansPurchaseRecommendationTypeDef",
    "SavingsPlansSavingsTypeDef",
    "SavingsPlansUtilizationAggregatesTypeDef",
    "SavingsPlansUtilizationByTimeTypeDef",
    "SavingsPlansUtilizationDetailTypeDef",
    "SavingsPlansUtilizationTypeDef",
    "ServiceSpecificationTypeDef",
    "SortDefinitionTypeDef",
    "SubscriberTypeDef",
    "TagValuesTypeDef",
    "TargetInstanceTypeDef",
    "TerminateRecommendationDetailTypeDef",
    "TotalImpactFilterTypeDef",
    "UpdateAnomalyMonitorResponseTypeDef",
    "UpdateAnomalySubscriptionResponseTypeDef",
    "UpdateCostCategoryDefinitionResponseTypeDef",
    "UtilizationByTimeTypeDef",
)


class _RequiredAnomalyDateIntervalTypeDef(TypedDict):
    StartDate: str


class AnomalyDateIntervalTypeDef(_RequiredAnomalyDateIntervalTypeDef, total=False):
    EndDate: str


class _RequiredAnomalyMonitorTypeDef(TypedDict):
    MonitorName: str
    MonitorType: MonitorType


class AnomalyMonitorTypeDef(_RequiredAnomalyMonitorTypeDef, total=False):
    MonitorArn: str
    CreationDate: str
    LastUpdatedDate: str
    LastEvaluatedDate: str
    MonitorDimension: Literal["SERVICE"]
    MonitorSpecification: "ExpressionTypeDef"
    DimensionalValueCount: int


class AnomalyScoreTypeDef(TypedDict):
    MaxScore: float
    CurrentScore: float


class _RequiredAnomalySubscriptionTypeDef(TypedDict):
    MonitorArnList: List[str]
    Subscribers: List["SubscriberTypeDef"]
    Threshold: float
    Frequency: AnomalySubscriptionFrequency
    SubscriptionName: str


class AnomalySubscriptionTypeDef(_RequiredAnomalySubscriptionTypeDef, total=False):
    SubscriptionArn: str
    AccountId: str


class _RequiredAnomalyTypeDef(TypedDict):
    AnomalyId: str
    AnomalyScore: "AnomalyScoreTypeDef"
    Impact: "ImpactTypeDef"
    MonitorArn: str


class AnomalyTypeDef(_RequiredAnomalyTypeDef, total=False):
    AnomalyStartDate: str
    AnomalyEndDate: str
    DimensionValue: str
    RootCauses: List["RootCauseTypeDef"]
    Feedback: AnomalyFeedbackType


class CostCategoryInheritedValueDimensionTypeDef(TypedDict, total=False):
    DimensionName: CostCategoryInheritedValueDimensionName
    DimensionKey: str


class CostCategoryProcessingStatusTypeDef(TypedDict, total=False):
    Component: Literal["COST_EXPLORER"]
    Status: CostCategoryStatus


class CostCategoryReferenceTypeDef(TypedDict, total=False):
    CostCategoryArn: str
    Name: str
    EffectiveStart: str
    EffectiveEnd: str
    NumberOfRules: int
    ProcessingStatus: List["CostCategoryProcessingStatusTypeDef"]
    Values: List[str]
    DefaultValue: str


CostCategoryRuleTypeDef = TypedDict(
    "CostCategoryRuleTypeDef",
    {
        "Value": str,
        "Rule": "ExpressionTypeDef",
        "InheritedValue": "CostCategoryInheritedValueDimensionTypeDef",
        "Type": CostCategoryRuleType,
    },
    total=False,
)


class _RequiredCostCategoryTypeDef(TypedDict):
    CostCategoryArn: str
    EffectiveStart: str
    Name: str
    RuleVersion: Literal["CostCategoryExpression.v1"]
    Rules: List["CostCategoryRuleTypeDef"]


class CostCategoryTypeDef(_RequiredCostCategoryTypeDef, total=False):
    EffectiveEnd: str
    ProcessingStatus: List["CostCategoryProcessingStatusTypeDef"]
    DefaultValue: str


class CostCategoryValuesTypeDef(TypedDict, total=False):
    Key: str
    Values: List[str]
    MatchOptions: List[MatchOption]


class CoverageByTimeTypeDef(TypedDict, total=False):
    TimePeriod: "DateIntervalTypeDef"
    Groups: List["ReservationCoverageGroupTypeDef"]
    Total: "CoverageTypeDef"


class CoverageCostTypeDef(TypedDict, total=False):
    OnDemandCost: str


class CoverageHoursTypeDef(TypedDict, total=False):
    OnDemandHours: str
    ReservedHours: str
    TotalRunningHours: str
    CoverageHoursPercentage: str


class CoverageNormalizedUnitsTypeDef(TypedDict, total=False):
    OnDemandNormalizedUnits: str
    ReservedNormalizedUnits: str
    TotalRunningNormalizedUnits: str
    CoverageNormalizedUnitsPercentage: str


class CoverageTypeDef(TypedDict, total=False):
    CoverageHours: "CoverageHoursTypeDef"
    CoverageNormalizedUnits: "CoverageNormalizedUnitsTypeDef"
    CoverageCost: "CoverageCostTypeDef"


class CreateAnomalyMonitorResponseTypeDef(TypedDict):
    MonitorArn: str


class CreateAnomalySubscriptionResponseTypeDef(TypedDict):
    SubscriptionArn: str


class CreateCostCategoryDefinitionResponseTypeDef(TypedDict, total=False):
    CostCategoryArn: str
    EffectiveStart: str


class CurrentInstanceTypeDef(TypedDict, total=False):
    ResourceId: str
    InstanceName: str
    Tags: List["TagValuesTypeDef"]
    ResourceDetails: "ResourceDetailsTypeDef"
    ResourceUtilization: "ResourceUtilizationTypeDef"
    ReservationCoveredHoursInLookbackPeriod: str
    SavingsPlansCoveredHoursInLookbackPeriod: str
    OnDemandHoursInLookbackPeriod: str
    TotalRunningHoursInLookbackPeriod: str
    MonthlyCost: str
    CurrencyCode: str


class DateIntervalTypeDef(TypedDict):
    Start: str
    End: str


class DeleteCostCategoryDefinitionResponseTypeDef(TypedDict, total=False):
    CostCategoryArn: str
    EffectiveEnd: str


class DescribeCostCategoryDefinitionResponseTypeDef(TypedDict, total=False):
    CostCategory: "CostCategoryTypeDef"


class DimensionValuesTypeDef(TypedDict, total=False):
    Key: Dimension
    Values: List[str]
    MatchOptions: List[MatchOption]


class DimensionValuesWithAttributesTypeDef(TypedDict, total=False):
    Value: str
    Attributes: Dict[str, str]


class EBSResourceUtilizationTypeDef(TypedDict, total=False):
    EbsReadOpsPerSecond: str
    EbsWriteOpsPerSecond: str
    EbsReadBytesPerSecond: str
    EbsWriteBytesPerSecond: str


class EC2InstanceDetailsTypeDef(TypedDict, total=False):
    Family: str
    InstanceType: str
    Region: str
    AvailabilityZone: str
    Platform: str
    Tenancy: str
    CurrentGeneration: bool
    SizeFlexEligible: bool


class EC2ResourceDetailsTypeDef(TypedDict, total=False):
    HourlyOnDemandRate: str
    InstanceType: str
    Platform: str
    Region: str
    Sku: str
    Memory: str
    NetworkPerformance: str
    Storage: str
    Vcpu: str


class EC2ResourceUtilizationTypeDef(TypedDict, total=False):
    MaxCpuUtilizationPercentage: str
    MaxMemoryUtilizationPercentage: str
    MaxStorageUtilizationPercentage: str
    EBSResourceUtilization: "EBSResourceUtilizationTypeDef"


class EC2SpecificationTypeDef(TypedDict, total=False):
    OfferingClass: OfferingClass


class ESInstanceDetailsTypeDef(TypedDict, total=False):
    InstanceClass: str
    InstanceSize: str
    Region: str
    CurrentGeneration: bool
    SizeFlexEligible: bool


class ElastiCacheInstanceDetailsTypeDef(TypedDict, total=False):
    Family: str
    NodeType: str
    Region: str
    ProductDescription: str
    CurrentGeneration: bool
    SizeFlexEligible: bool


class ExpressionTypeDef(TypedDict, total=False):
    Or: List[Dict[str, Any]]
    And: List[Dict[str, Any]]
    Not: Dict[str, Any]
    Dimensions: "DimensionValuesTypeDef"
    Tags: "TagValuesTypeDef"
    CostCategories: "CostCategoryValuesTypeDef"


class ForecastResultTypeDef(TypedDict, total=False):
    TimePeriod: "DateIntervalTypeDef"
    MeanValue: str
    PredictionIntervalLowerBound: str
    PredictionIntervalUpperBound: str


class _RequiredGetAnomaliesResponseTypeDef(TypedDict):
    Anomalies: List["AnomalyTypeDef"]


class GetAnomaliesResponseTypeDef(_RequiredGetAnomaliesResponseTypeDef, total=False):
    NextPageToken: str


class _RequiredGetAnomalyMonitorsResponseTypeDef(TypedDict):
    AnomalyMonitors: List["AnomalyMonitorTypeDef"]


class GetAnomalyMonitorsResponseTypeDef(_RequiredGetAnomalyMonitorsResponseTypeDef, total=False):
    NextPageToken: str


class _RequiredGetAnomalySubscriptionsResponseTypeDef(TypedDict):
    AnomalySubscriptions: List["AnomalySubscriptionTypeDef"]


class GetAnomalySubscriptionsResponseTypeDef(
    _RequiredGetAnomalySubscriptionsResponseTypeDef, total=False
):
    NextPageToken: str


class GetCostAndUsageResponseTypeDef(TypedDict, total=False):
    NextPageToken: str
    GroupDefinitions: List["GroupDefinitionTypeDef"]
    ResultsByTime: List["ResultByTimeTypeDef"]
    DimensionValueAttributes: List["DimensionValuesWithAttributesTypeDef"]


class GetCostAndUsageWithResourcesResponseTypeDef(TypedDict, total=False):
    NextPageToken: str
    GroupDefinitions: List["GroupDefinitionTypeDef"]
    ResultsByTime: List["ResultByTimeTypeDef"]
    DimensionValueAttributes: List["DimensionValuesWithAttributesTypeDef"]


class _RequiredGetCostCategoriesResponseTypeDef(TypedDict):
    ReturnSize: int
    TotalSize: int


class GetCostCategoriesResponseTypeDef(_RequiredGetCostCategoriesResponseTypeDef, total=False):
    NextPageToken: str
    CostCategoryNames: List[str]
    CostCategoryValues: List[str]


class GetCostForecastResponseTypeDef(TypedDict, total=False):
    Total: "MetricValueTypeDef"
    ForecastResultsByTime: List["ForecastResultTypeDef"]


class _RequiredGetDimensionValuesResponseTypeDef(TypedDict):
    DimensionValues: List["DimensionValuesWithAttributesTypeDef"]
    ReturnSize: int
    TotalSize: int


class GetDimensionValuesResponseTypeDef(_RequiredGetDimensionValuesResponseTypeDef, total=False):
    NextPageToken: str


class _RequiredGetReservationCoverageResponseTypeDef(TypedDict):
    CoveragesByTime: List["CoverageByTimeTypeDef"]


class GetReservationCoverageResponseTypeDef(
    _RequiredGetReservationCoverageResponseTypeDef, total=False
):
    Total: "CoverageTypeDef"
    NextPageToken: str


class GetReservationPurchaseRecommendationResponseTypeDef(TypedDict, total=False):
    Metadata: "ReservationPurchaseRecommendationMetadataTypeDef"
    Recommendations: List["ReservationPurchaseRecommendationTypeDef"]
    NextPageToken: str


class _RequiredGetReservationUtilizationResponseTypeDef(TypedDict):
    UtilizationsByTime: List["UtilizationByTimeTypeDef"]


class GetReservationUtilizationResponseTypeDef(
    _RequiredGetReservationUtilizationResponseTypeDef, total=False
):
    Total: "ReservationAggregatesTypeDef"
    NextPageToken: str


class GetRightsizingRecommendationResponseTypeDef(TypedDict, total=False):
    Metadata: "RightsizingRecommendationMetadataTypeDef"
    Summary: "RightsizingRecommendationSummaryTypeDef"
    RightsizingRecommendations: List["RightsizingRecommendationTypeDef"]
    NextPageToken: str
    Configuration: "RightsizingRecommendationConfigurationTypeDef"


class _RequiredGetSavingsPlansCoverageResponseTypeDef(TypedDict):
    SavingsPlansCoverages: List["SavingsPlansCoverageTypeDef"]


class GetSavingsPlansCoverageResponseTypeDef(
    _RequiredGetSavingsPlansCoverageResponseTypeDef, total=False
):
    NextToken: str


class GetSavingsPlansPurchaseRecommendationResponseTypeDef(TypedDict, total=False):
    Metadata: "SavingsPlansPurchaseRecommendationMetadataTypeDef"
    SavingsPlansPurchaseRecommendation: "SavingsPlansPurchaseRecommendationTypeDef"
    NextPageToken: str


class _RequiredGetSavingsPlansUtilizationDetailsResponseTypeDef(TypedDict):
    SavingsPlansUtilizationDetails: List["SavingsPlansUtilizationDetailTypeDef"]
    TimePeriod: "DateIntervalTypeDef"


class GetSavingsPlansUtilizationDetailsResponseTypeDef(
    _RequiredGetSavingsPlansUtilizationDetailsResponseTypeDef, total=False
):
    Total: "SavingsPlansUtilizationAggregatesTypeDef"
    NextToken: str


class _RequiredGetSavingsPlansUtilizationResponseTypeDef(TypedDict):
    Total: "SavingsPlansUtilizationAggregatesTypeDef"


class GetSavingsPlansUtilizationResponseTypeDef(
    _RequiredGetSavingsPlansUtilizationResponseTypeDef, total=False
):
    SavingsPlansUtilizationsByTime: List["SavingsPlansUtilizationByTimeTypeDef"]


class _RequiredGetTagsResponseTypeDef(TypedDict):
    Tags: List[str]
    ReturnSize: int
    TotalSize: int


class GetTagsResponseTypeDef(_RequiredGetTagsResponseTypeDef, total=False):
    NextPageToken: str


class GetUsageForecastResponseTypeDef(TypedDict, total=False):
    Total: "MetricValueTypeDef"
    ForecastResultsByTime: List["ForecastResultTypeDef"]


GroupDefinitionTypeDef = TypedDict(
    "GroupDefinitionTypeDef", {"Type": GroupDefinitionType, "Key": str}, total=False
)


class GroupTypeDef(TypedDict, total=False):
    Keys: List[str]
    Metrics: Dict[str, "MetricValueTypeDef"]


class _RequiredImpactTypeDef(TypedDict):
    MaxImpact: float


class ImpactTypeDef(_RequiredImpactTypeDef, total=False):
    TotalImpact: float


class InstanceDetailsTypeDef(TypedDict, total=False):
    EC2InstanceDetails: "EC2InstanceDetailsTypeDef"
    RDSInstanceDetails: "RDSInstanceDetailsTypeDef"
    RedshiftInstanceDetails: "RedshiftInstanceDetailsTypeDef"
    ElastiCacheInstanceDetails: "ElastiCacheInstanceDetailsTypeDef"
    ESInstanceDetails: "ESInstanceDetailsTypeDef"


class ListCostCategoryDefinitionsResponseTypeDef(TypedDict, total=False):
    CostCategoryReferences: List["CostCategoryReferenceTypeDef"]
    NextToken: str


class MetricValueTypeDef(TypedDict, total=False):
    Amount: str
    Unit: str


class ModifyRecommendationDetailTypeDef(TypedDict, total=False):
    TargetInstances: List["TargetInstanceTypeDef"]


class ProvideAnomalyFeedbackResponseTypeDef(TypedDict):
    AnomalyId: str


class RDSInstanceDetailsTypeDef(TypedDict, total=False):
    Family: str
    InstanceType: str
    Region: str
    DatabaseEngine: str
    DatabaseEdition: str
    DeploymentOption: str
    LicenseModel: str
    CurrentGeneration: bool
    SizeFlexEligible: bool


class RedshiftInstanceDetailsTypeDef(TypedDict, total=False):
    Family: str
    NodeType: str
    Region: str
    CurrentGeneration: bool
    SizeFlexEligible: bool


class ReservationAggregatesTypeDef(TypedDict, total=False):
    UtilizationPercentage: str
    UtilizationPercentageInUnits: str
    PurchasedHours: str
    PurchasedUnits: str
    TotalActualHours: str
    TotalActualUnits: str
    UnusedHours: str
    UnusedUnits: str
    OnDemandCostOfRIHoursUsed: str
    NetRISavings: str
    TotalPotentialRISavings: str
    AmortizedUpfrontFee: str
    AmortizedRecurringFee: str
    TotalAmortizedFee: str
    RICostForUnusedHours: str
    RealizedSavings: str
    UnrealizedSavings: str


class ReservationCoverageGroupTypeDef(TypedDict, total=False):
    Attributes: Dict[str, str]
    Coverage: "CoverageTypeDef"


class ReservationPurchaseRecommendationDetailTypeDef(TypedDict, total=False):
    AccountId: str
    InstanceDetails: "InstanceDetailsTypeDef"
    RecommendedNumberOfInstancesToPurchase: str
    RecommendedNormalizedUnitsToPurchase: str
    MinimumNumberOfInstancesUsedPerHour: str
    MinimumNormalizedUnitsUsedPerHour: str
    MaximumNumberOfInstancesUsedPerHour: str
    MaximumNormalizedUnitsUsedPerHour: str
    AverageNumberOfInstancesUsedPerHour: str
    AverageNormalizedUnitsUsedPerHour: str
    AverageUtilization: str
    EstimatedBreakEvenInMonths: str
    CurrencyCode: str
    EstimatedMonthlySavingsAmount: str
    EstimatedMonthlySavingsPercentage: str
    EstimatedMonthlyOnDemandCost: str
    EstimatedReservationCostForLookbackPeriod: str
    UpfrontCost: str
    RecurringStandardMonthlyCost: str


class ReservationPurchaseRecommendationMetadataTypeDef(TypedDict, total=False):
    RecommendationId: str
    GenerationTimestamp: str


class ReservationPurchaseRecommendationSummaryTypeDef(TypedDict, total=False):
    TotalEstimatedMonthlySavingsAmount: str
    TotalEstimatedMonthlySavingsPercentage: str
    CurrencyCode: str


class ReservationPurchaseRecommendationTypeDef(TypedDict, total=False):
    AccountScope: AccountScope
    LookbackPeriodInDays: LookbackPeriodInDays
    TermInYears: TermInYears
    PaymentOption: PaymentOption
    ServiceSpecification: "ServiceSpecificationTypeDef"
    RecommendationDetails: List["ReservationPurchaseRecommendationDetailTypeDef"]
    RecommendationSummary: "ReservationPurchaseRecommendationSummaryTypeDef"


class ReservationUtilizationGroupTypeDef(TypedDict, total=False):
    Key: str
    Value: str
    Attributes: Dict[str, str]
    Utilization: "ReservationAggregatesTypeDef"


class ResourceDetailsTypeDef(TypedDict, total=False):
    EC2ResourceDetails: "EC2ResourceDetailsTypeDef"


class ResourceUtilizationTypeDef(TypedDict, total=False):
    EC2ResourceUtilization: "EC2ResourceUtilizationTypeDef"


class ResultByTimeTypeDef(TypedDict, total=False):
    TimePeriod: "DateIntervalTypeDef"
    Total: Dict[str, "MetricValueTypeDef"]
    Groups: List["GroupTypeDef"]
    Estimated: bool


class RightsizingRecommendationConfigurationTypeDef(TypedDict):
    RecommendationTarget: RecommendationTarget
    BenefitsConsidered: bool


class RightsizingRecommendationMetadataTypeDef(TypedDict, total=False):
    RecommendationId: str
    GenerationTimestamp: str
    LookbackPeriodInDays: LookbackPeriodInDays
    AdditionalMetadata: str


class RightsizingRecommendationSummaryTypeDef(TypedDict, total=False):
    TotalRecommendationCount: str
    EstimatedTotalMonthlySavingsAmount: str
    SavingsCurrencyCode: str
    SavingsPercentage: str


class RightsizingRecommendationTypeDef(TypedDict, total=False):
    AccountId: str
    CurrentInstance: "CurrentInstanceTypeDef"
    RightsizingType: RightsizingType
    ModifyRecommendationDetail: "ModifyRecommendationDetailTypeDef"
    TerminateRecommendationDetail: "TerminateRecommendationDetailTypeDef"


class RootCauseTypeDef(TypedDict, total=False):
    Service: str
    Region: str
    LinkedAccount: str
    UsageType: str


class SavingsPlansAmortizedCommitmentTypeDef(TypedDict, total=False):
    AmortizedRecurringCommitment: str
    AmortizedUpfrontCommitment: str
    TotalAmortizedCommitment: str


class SavingsPlansCoverageDataTypeDef(TypedDict, total=False):
    SpendCoveredBySavingsPlans: str
    OnDemandCost: str
    TotalCost: str
    CoveragePercentage: str


class SavingsPlansCoverageTypeDef(TypedDict, total=False):
    Attributes: Dict[str, str]
    Coverage: "SavingsPlansCoverageDataTypeDef"
    TimePeriod: "DateIntervalTypeDef"


class SavingsPlansDetailsTypeDef(TypedDict, total=False):
    Region: str
    InstanceFamily: str
    OfferingId: str


class SavingsPlansPurchaseRecommendationDetailTypeDef(TypedDict, total=False):
    SavingsPlansDetails: "SavingsPlansDetailsTypeDef"
    AccountId: str
    UpfrontCost: str
    EstimatedROI: str
    CurrencyCode: str
    EstimatedSPCost: str
    EstimatedOnDemandCost: str
    EstimatedOnDemandCostWithCurrentCommitment: str
    EstimatedSavingsAmount: str
    EstimatedSavingsPercentage: str
    HourlyCommitmentToPurchase: str
    EstimatedAverageUtilization: str
    EstimatedMonthlySavingsAmount: str
    CurrentMinimumHourlyOnDemandSpend: str
    CurrentMaximumHourlyOnDemandSpend: str
    CurrentAverageHourlyOnDemandSpend: str


class SavingsPlansPurchaseRecommendationMetadataTypeDef(TypedDict, total=False):
    RecommendationId: str
    GenerationTimestamp: str
    AdditionalMetadata: str


class SavingsPlansPurchaseRecommendationSummaryTypeDef(TypedDict, total=False):
    EstimatedROI: str
    CurrencyCode: str
    EstimatedTotalCost: str
    CurrentOnDemandSpend: str
    EstimatedSavingsAmount: str
    TotalRecommendationCount: str
    DailyCommitmentToPurchase: str
    HourlyCommitmentToPurchase: str
    EstimatedSavingsPercentage: str
    EstimatedMonthlySavingsAmount: str
    EstimatedOnDemandCostWithCurrentCommitment: str


class SavingsPlansPurchaseRecommendationTypeDef(TypedDict, total=False):
    AccountScope: AccountScope
    SavingsPlansType: SupportedSavingsPlansType
    TermInYears: TermInYears
    PaymentOption: PaymentOption
    LookbackPeriodInDays: LookbackPeriodInDays
    SavingsPlansPurchaseRecommendationDetails: List[
        "SavingsPlansPurchaseRecommendationDetailTypeDef"
    ]
    SavingsPlansPurchaseRecommendationSummary: "SavingsPlansPurchaseRecommendationSummaryTypeDef"


class SavingsPlansSavingsTypeDef(TypedDict, total=False):
    NetSavings: str
    OnDemandCostEquivalent: str


class _RequiredSavingsPlansUtilizationAggregatesTypeDef(TypedDict):
    Utilization: "SavingsPlansUtilizationTypeDef"


class SavingsPlansUtilizationAggregatesTypeDef(
    _RequiredSavingsPlansUtilizationAggregatesTypeDef, total=False
):
    Savings: "SavingsPlansSavingsTypeDef"
    AmortizedCommitment: "SavingsPlansAmortizedCommitmentTypeDef"


class _RequiredSavingsPlansUtilizationByTimeTypeDef(TypedDict):
    TimePeriod: "DateIntervalTypeDef"
    Utilization: "SavingsPlansUtilizationTypeDef"


class SavingsPlansUtilizationByTimeTypeDef(
    _RequiredSavingsPlansUtilizationByTimeTypeDef, total=False
):
    Savings: "SavingsPlansSavingsTypeDef"
    AmortizedCommitment: "SavingsPlansAmortizedCommitmentTypeDef"


class SavingsPlansUtilizationDetailTypeDef(TypedDict, total=False):
    SavingsPlanArn: str
    Attributes: Dict[str, str]
    Utilization: "SavingsPlansUtilizationTypeDef"
    Savings: "SavingsPlansSavingsTypeDef"
    AmortizedCommitment: "SavingsPlansAmortizedCommitmentTypeDef"


class SavingsPlansUtilizationTypeDef(TypedDict, total=False):
    TotalCommitment: str
    UsedCommitment: str
    UnusedCommitment: str
    UtilizationPercentage: str


class ServiceSpecificationTypeDef(TypedDict, total=False):
    EC2Specification: "EC2SpecificationTypeDef"


class _RequiredSortDefinitionTypeDef(TypedDict):
    Key: str


class SortDefinitionTypeDef(_RequiredSortDefinitionTypeDef, total=False):
    SortOrder: SortOrder


SubscriberTypeDef = TypedDict(
    "SubscriberTypeDef",
    {"Address": str, "Type": SubscriberType, "Status": SubscriberStatus},
    total=False,
)


class TagValuesTypeDef(TypedDict, total=False):
    Key: str
    Values: List[str]
    MatchOptions: List[MatchOption]


class TargetInstanceTypeDef(TypedDict, total=False):
    EstimatedMonthlyCost: str
    EstimatedMonthlySavings: str
    CurrencyCode: str
    DefaultTargetInstance: bool
    ResourceDetails: "ResourceDetailsTypeDef"
    ExpectedResourceUtilization: "ResourceUtilizationTypeDef"


class TerminateRecommendationDetailTypeDef(TypedDict, total=False):
    EstimatedMonthlySavings: str
    CurrencyCode: str


class _RequiredTotalImpactFilterTypeDef(TypedDict):
    NumericOperator: NumericOperator
    StartValue: float


class TotalImpactFilterTypeDef(_RequiredTotalImpactFilterTypeDef, total=False):
    EndValue: float


class UpdateAnomalyMonitorResponseTypeDef(TypedDict):
    MonitorArn: str


class UpdateAnomalySubscriptionResponseTypeDef(TypedDict):
    SubscriptionArn: str


class UpdateCostCategoryDefinitionResponseTypeDef(TypedDict, total=False):
    CostCategoryArn: str
    EffectiveStart: str


class UtilizationByTimeTypeDef(TypedDict, total=False):
    TimePeriod: "DateIntervalTypeDef"
    Groups: List["ReservationUtilizationGroupTypeDef"]
    Total: "ReservationAggregatesTypeDef"
