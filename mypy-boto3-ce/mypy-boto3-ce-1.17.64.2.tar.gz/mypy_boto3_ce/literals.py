"""
Type annotations for ce service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ce/literals.html)

Usage::

    ```python
    from mypy_boto3_ce.literals import AccountScope

    data: AccountScope = "LINKED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccountScope",
    "AnomalyFeedbackType",
    "AnomalySubscriptionFrequency",
    "Context",
    "CostCategoryInheritedValueDimensionName",
    "CostCategoryRuleType",
    "CostCategoryRuleVersion",
    "CostCategoryStatus",
    "CostCategoryStatusComponent",
    "Dimension",
    "Granularity",
    "GroupDefinitionType",
    "LookbackPeriodInDays",
    "MatchOption",
    "Metric",
    "MonitorDimension",
    "MonitorType",
    "NumericOperator",
    "OfferingClass",
    "PaymentOption",
    "RecommendationTarget",
    "RightsizingType",
    "SavingsPlansDataType",
    "SortOrder",
    "SubscriberStatus",
    "SubscriberType",
    "SupportedSavingsPlansType",
    "TermInYears",
)


AccountScope = Literal["LINKED", "PAYER"]
AnomalyFeedbackType = Literal["NO", "PLANNED_ACTIVITY", "YES"]
AnomalySubscriptionFrequency = Literal["DAILY", "IMMEDIATE", "WEEKLY"]
Context = Literal["COST_AND_USAGE", "RESERVATIONS", "SAVINGS_PLANS"]
CostCategoryInheritedValueDimensionName = Literal["LINKED_ACCOUNT_NAME", "TAG"]
CostCategoryRuleType = Literal["INHERITED_VALUE", "REGULAR"]
CostCategoryRuleVersion = Literal["CostCategoryExpression.v1"]
CostCategoryStatus = Literal["APPLIED", "PROCESSING"]
CostCategoryStatusComponent = Literal["COST_EXPLORER"]
Dimension = Literal[
    "AGREEMENT_END_DATE_TIME_AFTER",
    "AGREEMENT_END_DATE_TIME_BEFORE",
    "AZ",
    "BILLING_ENTITY",
    "CACHE_ENGINE",
    "DATABASE_ENGINE",
    "DEPLOYMENT_OPTION",
    "INSTANCE_TYPE",
    "INSTANCE_TYPE_FAMILY",
    "LEGAL_ENTITY_NAME",
    "LINKED_ACCOUNT",
    "LINKED_ACCOUNT_NAME",
    "OPERATING_SYSTEM",
    "OPERATION",
    "PAYMENT_OPTION",
    "PLATFORM",
    "PURCHASE_TYPE",
    "RECORD_TYPE",
    "REGION",
    "RESERVATION_ID",
    "RESOURCE_ID",
    "RIGHTSIZING_TYPE",
    "SAVINGS_PLANS_TYPE",
    "SAVINGS_PLAN_ARN",
    "SCOPE",
    "SERVICE",
    "SERVICE_CODE",
    "SUBSCRIPTION_ID",
    "TENANCY",
    "USAGE_TYPE",
    "USAGE_TYPE_GROUP",
]
Granularity = Literal["DAILY", "HOURLY", "MONTHLY"]
GroupDefinitionType = Literal["COST_CATEGORY", "DIMENSION", "TAG"]
LookbackPeriodInDays = Literal["SEVEN_DAYS", "SIXTY_DAYS", "THIRTY_DAYS"]
MatchOption = Literal[
    "ABSENT", "CASE_INSENSITIVE", "CASE_SENSITIVE", "CONTAINS", "ENDS_WITH", "EQUALS", "STARTS_WITH"
]
Metric = Literal[
    "AMORTIZED_COST",
    "BLENDED_COST",
    "NET_AMORTIZED_COST",
    "NET_UNBLENDED_COST",
    "NORMALIZED_USAGE_AMOUNT",
    "UNBLENDED_COST",
    "USAGE_QUANTITY",
]
MonitorDimension = Literal["SERVICE"]
MonitorType = Literal["CUSTOM", "DIMENSIONAL"]
NumericOperator = Literal[
    "BETWEEN", "EQUAL", "GREATER_THAN", "GREATER_THAN_OR_EQUAL", "LESS_THAN", "LESS_THAN_OR_EQUAL"
]
OfferingClass = Literal["CONVERTIBLE", "STANDARD"]
PaymentOption = Literal[
    "ALL_UPFRONT",
    "HEAVY_UTILIZATION",
    "LIGHT_UTILIZATION",
    "MEDIUM_UTILIZATION",
    "NO_UPFRONT",
    "PARTIAL_UPFRONT",
]
RecommendationTarget = Literal["CROSS_INSTANCE_FAMILY", "SAME_INSTANCE_FAMILY"]
RightsizingType = Literal["MODIFY", "TERMINATE"]
SavingsPlansDataType = Literal["AMORTIZED_COMMITMENT", "ATTRIBUTES", "SAVINGS", "UTILIZATION"]
SortOrder = Literal["ASCENDING", "DESCENDING"]
SubscriberStatus = Literal["CONFIRMED", "DECLINED"]
SubscriberType = Literal["EMAIL", "SNS"]
SupportedSavingsPlansType = Literal["COMPUTE_SP", "EC2_INSTANCE_SP", "SAGEMAKER_SP"]
TermInYears = Literal["ONE_YEAR", "THREE_YEARS"]
