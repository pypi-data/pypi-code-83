"""
Type annotations for budgets service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/type_defs.html)

Usage::

    ```python
    from mypy_boto3_budgets.type_defs import ActionHistoryDetailsTypeDef

    data: ActionHistoryDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_budgets.literals import (
    ActionStatus,
    ActionSubType,
    ActionType,
    ApprovalModel,
    BudgetType,
    ComparisonOperator,
    EventType,
    ExecutionType,
    NotificationState,
    NotificationType,
    SubscriptionType,
    ThresholdType,
    TimeUnit,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionHistoryDetailsTypeDef",
    "ActionHistoryTypeDef",
    "ActionThresholdTypeDef",
    "ActionTypeDef",
    "BudgetPerformanceHistoryTypeDef",
    "BudgetTypeDef",
    "BudgetedAndActualAmountsTypeDef",
    "CalculatedSpendTypeDef",
    "CostTypesTypeDef",
    "CreateBudgetActionResponseTypeDef",
    "DefinitionTypeDef",
    "DeleteBudgetActionResponseTypeDef",
    "DescribeBudgetActionHistoriesResponseTypeDef",
    "DescribeBudgetActionResponseTypeDef",
    "DescribeBudgetActionsForAccountResponseTypeDef",
    "DescribeBudgetActionsForBudgetResponseTypeDef",
    "DescribeBudgetPerformanceHistoryResponseTypeDef",
    "DescribeBudgetResponseTypeDef",
    "DescribeBudgetsResponseTypeDef",
    "DescribeNotificationsForBudgetResponseTypeDef",
    "DescribeSubscribersForNotificationResponseTypeDef",
    "ExecuteBudgetActionResponseTypeDef",
    "IamActionDefinitionTypeDef",
    "NotificationTypeDef",
    "NotificationWithSubscribersTypeDef",
    "PaginatorConfigTypeDef",
    "ScpActionDefinitionTypeDef",
    "SpendTypeDef",
    "SsmActionDefinitionTypeDef",
    "SubscriberTypeDef",
    "TimePeriodTypeDef",
    "UpdateBudgetActionResponseTypeDef",
)


class ActionHistoryDetailsTypeDef(TypedDict):
    Message: str
    Action: "ActionTypeDef"


class ActionHistoryTypeDef(TypedDict):
    Timestamp: datetime
    Status: ActionStatus
    EventType: EventType
    ActionHistoryDetails: "ActionHistoryDetailsTypeDef"


class ActionThresholdTypeDef(TypedDict):
    ActionThresholdValue: float
    ActionThresholdType: ThresholdType


class ActionTypeDef(TypedDict):
    ActionId: str
    BudgetName: str
    NotificationType: NotificationType
    ActionType: ActionType
    ActionThreshold: "ActionThresholdTypeDef"
    Definition: "DefinitionTypeDef"
    ExecutionRoleArn: str
    ApprovalModel: ApprovalModel
    Status: ActionStatus
    Subscribers: List["SubscriberTypeDef"]


class BudgetPerformanceHistoryTypeDef(TypedDict, total=False):
    BudgetName: str
    BudgetType: BudgetType
    CostFilters: Dict[str, List[str]]
    CostTypes: "CostTypesTypeDef"
    TimeUnit: TimeUnit
    BudgetedAndActualAmountsList: List["BudgetedAndActualAmountsTypeDef"]


class _RequiredBudgetTypeDef(TypedDict):
    BudgetName: str
    TimeUnit: TimeUnit
    BudgetType: BudgetType


class BudgetTypeDef(_RequiredBudgetTypeDef, total=False):
    BudgetLimit: "SpendTypeDef"
    PlannedBudgetLimits: Dict[str, "SpendTypeDef"]
    CostFilters: Dict[str, List[str]]
    CostTypes: "CostTypesTypeDef"
    TimePeriod: "TimePeriodTypeDef"
    CalculatedSpend: "CalculatedSpendTypeDef"
    LastUpdatedTime: datetime


class BudgetedAndActualAmountsTypeDef(TypedDict, total=False):
    BudgetedAmount: "SpendTypeDef"
    ActualAmount: "SpendTypeDef"
    TimePeriod: "TimePeriodTypeDef"


class _RequiredCalculatedSpendTypeDef(TypedDict):
    ActualSpend: "SpendTypeDef"


class CalculatedSpendTypeDef(_RequiredCalculatedSpendTypeDef, total=False):
    ForecastedSpend: "SpendTypeDef"


class CostTypesTypeDef(TypedDict, total=False):
    IncludeTax: bool
    IncludeSubscription: bool
    UseBlended: bool
    IncludeRefund: bool
    IncludeCredit: bool
    IncludeUpfront: bool
    IncludeRecurring: bool
    IncludeOtherSubscription: bool
    IncludeSupport: bool
    IncludeDiscount: bool
    UseAmortized: bool


class CreateBudgetActionResponseTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    ActionId: str


class DefinitionTypeDef(TypedDict, total=False):
    IamActionDefinition: "IamActionDefinitionTypeDef"
    ScpActionDefinition: "ScpActionDefinitionTypeDef"
    SsmActionDefinition: "SsmActionDefinitionTypeDef"


class DeleteBudgetActionResponseTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    Action: "ActionTypeDef"


class _RequiredDescribeBudgetActionHistoriesResponseTypeDef(TypedDict):
    ActionHistories: List["ActionHistoryTypeDef"]


class DescribeBudgetActionHistoriesResponseTypeDef(
    _RequiredDescribeBudgetActionHistoriesResponseTypeDef, total=False
):
    NextToken: str


class DescribeBudgetActionResponseTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    Action: "ActionTypeDef"


class _RequiredDescribeBudgetActionsForAccountResponseTypeDef(TypedDict):
    Actions: List["ActionTypeDef"]


class DescribeBudgetActionsForAccountResponseTypeDef(
    _RequiredDescribeBudgetActionsForAccountResponseTypeDef, total=False
):
    NextToken: str


class _RequiredDescribeBudgetActionsForBudgetResponseTypeDef(TypedDict):
    Actions: List["ActionTypeDef"]


class DescribeBudgetActionsForBudgetResponseTypeDef(
    _RequiredDescribeBudgetActionsForBudgetResponseTypeDef, total=False
):
    NextToken: str


class DescribeBudgetPerformanceHistoryResponseTypeDef(TypedDict, total=False):
    BudgetPerformanceHistory: "BudgetPerformanceHistoryTypeDef"
    NextToken: str


class DescribeBudgetResponseTypeDef(TypedDict, total=False):
    Budget: "BudgetTypeDef"


class DescribeBudgetsResponseTypeDef(TypedDict, total=False):
    Budgets: List["BudgetTypeDef"]
    NextToken: str


class DescribeNotificationsForBudgetResponseTypeDef(TypedDict, total=False):
    Notifications: List["NotificationTypeDef"]
    NextToken: str


class DescribeSubscribersForNotificationResponseTypeDef(TypedDict, total=False):
    Subscribers: List["SubscriberTypeDef"]
    NextToken: str


class ExecuteBudgetActionResponseTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    ActionId: str
    ExecutionType: ExecutionType


class _RequiredIamActionDefinitionTypeDef(TypedDict):
    PolicyArn: str


class IamActionDefinitionTypeDef(_RequiredIamActionDefinitionTypeDef, total=False):
    Roles: List[str]
    Groups: List[str]
    Users: List[str]


class _RequiredNotificationTypeDef(TypedDict):
    NotificationType: NotificationType
    ComparisonOperator: ComparisonOperator
    Threshold: float


class NotificationTypeDef(_RequiredNotificationTypeDef, total=False):
    ThresholdType: ThresholdType
    NotificationState: NotificationState


class NotificationWithSubscribersTypeDef(TypedDict):
    Notification: "NotificationTypeDef"
    Subscribers: List["SubscriberTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ScpActionDefinitionTypeDef(TypedDict):
    PolicyId: str
    TargetIds: List[str]


class SpendTypeDef(TypedDict):
    Amount: str
    Unit: str


class SsmActionDefinitionTypeDef(TypedDict):
    ActionSubType: ActionSubType
    Region: str
    InstanceIds: List[str]


class SubscriberTypeDef(TypedDict):
    SubscriptionType: SubscriptionType
    Address: str


class TimePeriodTypeDef(TypedDict, total=False):
    Start: datetime
    End: datetime


class UpdateBudgetActionResponseTypeDef(TypedDict):
    AccountId: str
    BudgetName: str
    OldAction: "ActionTypeDef"
    NewAction: "ActionTypeDef"
