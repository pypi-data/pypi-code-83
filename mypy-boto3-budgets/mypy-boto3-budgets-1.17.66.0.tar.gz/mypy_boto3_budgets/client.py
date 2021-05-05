"""
Type annotations for budgets service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_budgets import BudgetsClient

    client: BudgetsClient = boto3.client("budgets")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_budgets.literals import ActionType, ApprovalModel, ExecutionType, NotificationType
from mypy_boto3_budgets.paginator import (
    DescribeBudgetActionHistoriesPaginator,
    DescribeBudgetActionsForAccountPaginator,
    DescribeBudgetActionsForBudgetPaginator,
    DescribeBudgetPerformanceHistoryPaginator,
    DescribeBudgetsPaginator,
    DescribeNotificationsForBudgetPaginator,
    DescribeSubscribersForNotificationPaginator,
)
from mypy_boto3_budgets.type_defs import (
    ActionThresholdTypeDef,
    BudgetTypeDef,
    CreateBudgetActionResponseTypeDef,
    DefinitionTypeDef,
    DeleteBudgetActionResponseTypeDef,
    DescribeBudgetActionHistoriesResponseTypeDef,
    DescribeBudgetActionResponseTypeDef,
    DescribeBudgetActionsForAccountResponseTypeDef,
    DescribeBudgetActionsForBudgetResponseTypeDef,
    DescribeBudgetPerformanceHistoryResponseTypeDef,
    DescribeBudgetResponseTypeDef,
    DescribeBudgetsResponseTypeDef,
    DescribeNotificationsForBudgetResponseTypeDef,
    DescribeSubscribersForNotificationResponseTypeDef,
    ExecuteBudgetActionResponseTypeDef,
    NotificationTypeDef,
    NotificationWithSubscribersTypeDef,
    SubscriberTypeDef,
    TimePeriodTypeDef,
    UpdateBudgetActionResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("BudgetsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CreationLimitExceededException: Type[BotocoreClientError]
    DuplicateRecordException: Type[BotocoreClientError]
    ExpiredNextTokenException: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ResourceLockedException: Type[BotocoreClientError]


class BudgetsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#can-paginate)
        """

    def create_budget(
        self,
        AccountId: str,
        Budget: "BudgetTypeDef",
        NotificationsWithSubscribers: List[NotificationWithSubscribersTypeDef] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.create_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#create-budget)
        """

    def create_budget_action(
        self,
        AccountId: str,
        BudgetName: str,
        NotificationType: NotificationType,
        ActionType: ActionType,
        ActionThreshold: "ActionThresholdTypeDef",
        Definition: "DefinitionTypeDef",
        ExecutionRoleArn: str,
        ApprovalModel: ApprovalModel,
        Subscribers: List["SubscriberTypeDef"],
    ) -> CreateBudgetActionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.create_budget_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#create-budget-action)
        """

    def create_notification(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        Subscribers: List["SubscriberTypeDef"],
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.create_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#create-notification)
        """

    def create_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        Subscriber: "SubscriberTypeDef",
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.create_subscriber)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#create-subscriber)
        """

    def delete_budget(self, AccountId: str, BudgetName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.delete_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#delete-budget)
        """

    def delete_budget_action(
        self, AccountId: str, BudgetName: str, ActionId: str
    ) -> DeleteBudgetActionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.delete_budget_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#delete-budget-action)
        """

    def delete_notification(
        self, AccountId: str, BudgetName: str, Notification: "NotificationTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.delete_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#delete-notification)
        """

    def delete_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        Subscriber: "SubscriberTypeDef",
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.delete_subscriber)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#delete-subscriber)
        """

    def describe_budget(self, AccountId: str, BudgetName: str) -> DescribeBudgetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.describe_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe-budget)
        """

    def describe_budget_action(
        self, AccountId: str, BudgetName: str, ActionId: str
    ) -> DescribeBudgetActionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.describe_budget_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe-budget-action)
        """

    def describe_budget_action_histories(
        self,
        AccountId: str,
        BudgetName: str,
        ActionId: str,
        TimePeriod: "TimePeriodTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeBudgetActionHistoriesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.describe_budget_action_histories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe-budget-action-histories)
        """

    def describe_budget_actions_for_account(
        self, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeBudgetActionsForAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.describe_budget_actions_for_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe-budget-actions-for-account)
        """

    def describe_budget_actions_for_budget(
        self, AccountId: str, BudgetName: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeBudgetActionsForBudgetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.describe_budget_actions_for_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe-budget-actions-for-budget)
        """

    def describe_budget_performance_history(
        self,
        AccountId: str,
        BudgetName: str,
        TimePeriod: "TimePeriodTypeDef" = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeBudgetPerformanceHistoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.describe_budget_performance_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe-budget-performance-history)
        """

    def describe_budgets(
        self, AccountId: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeBudgetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.describe_budgets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe-budgets)
        """

    def describe_notifications_for_budget(
        self, AccountId: str, BudgetName: str, MaxResults: int = None, NextToken: str = None
    ) -> DescribeNotificationsForBudgetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.describe_notifications_for_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe-notifications-for-budget)
        """

    def describe_subscribers_for_notification(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeSubscribersForNotificationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.describe_subscribers_for_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#describe-subscribers-for-notification)
        """

    def execute_budget_action(
        self, AccountId: str, BudgetName: str, ActionId: str, ExecutionType: ExecutionType
    ) -> ExecuteBudgetActionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.execute_budget_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#execute-budget-action)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#generate-presigned-url)
        """

    def update_budget(self, AccountId: str, NewBudget: "BudgetTypeDef") -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.update_budget)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#update-budget)
        """

    def update_budget_action(
        self,
        AccountId: str,
        BudgetName: str,
        ActionId: str,
        NotificationType: NotificationType = None,
        ActionThreshold: "ActionThresholdTypeDef" = None,
        Definition: "DefinitionTypeDef" = None,
        ExecutionRoleArn: str = None,
        ApprovalModel: ApprovalModel = None,
        Subscribers: List["SubscriberTypeDef"] = None,
    ) -> UpdateBudgetActionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.update_budget_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#update-budget-action)
        """

    def update_notification(
        self,
        AccountId: str,
        BudgetName: str,
        OldNotification: "NotificationTypeDef",
        NewNotification: "NotificationTypeDef",
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.update_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#update-notification)
        """

    def update_subscriber(
        self,
        AccountId: str,
        BudgetName: str,
        Notification: "NotificationTypeDef",
        OldSubscriber: "SubscriberTypeDef",
        NewSubscriber: "SubscriberTypeDef",
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Client.update_subscriber)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/client.html#update-subscriber)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budget_action_histories"]
    ) -> DescribeBudgetActionHistoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionHistories)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators.html#describebudgetactionhistoriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budget_actions_for_account"]
    ) -> DescribeBudgetActionsForAccountPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionsForAccount)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators.html#describebudgetactionsforaccountpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budget_actions_for_budget"]
    ) -> DescribeBudgetActionsForBudgetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetActionsForBudget)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators.html#describebudgetactionsforbudgetpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budget_performance_history"]
    ) -> DescribeBudgetPerformanceHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Paginator.DescribeBudgetPerformanceHistory)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators.html#describebudgetperformancehistorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_budgets"]
    ) -> DescribeBudgetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Paginator.DescribeBudgets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators.html#describebudgetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_notifications_for_budget"]
    ) -> DescribeNotificationsForBudgetPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Paginator.DescribeNotificationsForBudget)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators.html#describenotificationsforbudgetpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subscribers_for_notification"]
    ) -> DescribeSubscribersForNotificationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/budgets.html#Budgets.Paginator.DescribeSubscribersForNotification)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_budgets/paginators.html#describesubscribersfornotificationpaginator)
        """
