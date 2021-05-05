"""
Type annotations for codestar-notifications service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codestar_notifications import CodeStarNotificationsClient

    client: CodeStarNotificationsClient = boto3.client("codestar-notifications")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_codestar_notifications.literals import DetailType, NotificationRuleStatus
from mypy_boto3_codestar_notifications.paginator import (
    ListEventTypesPaginator,
    ListNotificationRulesPaginator,
    ListTargetsPaginator,
)
from mypy_boto3_codestar_notifications.type_defs import (
    CreateNotificationRuleResultTypeDef,
    DeleteNotificationRuleResultTypeDef,
    DescribeNotificationRuleResultTypeDef,
    ListEventTypesFilterTypeDef,
    ListEventTypesResultTypeDef,
    ListNotificationRulesFilterTypeDef,
    ListNotificationRulesResultTypeDef,
    ListTagsForResourceResultTypeDef,
    ListTargetsFilterTypeDef,
    ListTargetsResultTypeDef,
    SubscribeResultTypeDef,
    TagResourceResultTypeDef,
    TargetTypeDef,
    UnsubscribeResultTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeStarNotificationsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    ConfigurationException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class CodeStarNotificationsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html#can-paginate)
        """

    def create_notification_rule(
        self,
        Name: str,
        EventTypeIds: List[str],
        Resource: str,
        Targets: List[TargetTypeDef],
        DetailType: DetailType,
        ClientRequestToken: str = None,
        Tags: Dict[str, str] = None,
        Status: NotificationRuleStatus = None,
    ) -> CreateNotificationRuleResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client.create_notification_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html#create-notification-rule)
        """

    def delete_notification_rule(self, Arn: str) -> DeleteNotificationRuleResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client.delete_notification_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html#delete-notification-rule)
        """

    def delete_target(self, TargetAddress: str, ForceUnsubscribeAll: bool = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client.delete_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html#delete-target)
        """

    def describe_notification_rule(self, Arn: str) -> DescribeNotificationRuleResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client.describe_notification_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html#describe-notification-rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html#generate-presigned-url)
        """

    def list_event_types(
        self,
        Filters: List[ListEventTypesFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListEventTypesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_event_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html#list-event-types)
        """

    def list_notification_rules(
        self,
        Filters: List[ListNotificationRulesFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListNotificationRulesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_notification_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html#list-notification-rules)
        """

    def list_tags_for_resource(self, Arn: str) -> ListTagsForResourceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html#list-tags-for-resource)
        """

    def list_targets(
        self,
        Filters: List[ListTargetsFilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListTargetsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client.list_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html#list-targets)
        """

    def subscribe(
        self, Arn: str, Target: TargetTypeDef, ClientRequestToken: str = None
    ) -> SubscribeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client.subscribe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html#subscribe)
        """

    def tag_resource(self, Arn: str, Tags: Dict[str, str]) -> TagResourceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html#tag-resource)
        """

    def unsubscribe(self, Arn: str, TargetAddress: str) -> UnsubscribeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client.unsubscribe)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html#unsubscribe)
        """

    def untag_resource(self, Arn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html#untag-resource)
        """

    def update_notification_rule(
        self,
        Arn: str,
        Name: str = None,
        Status: NotificationRuleStatus = None,
        EventTypeIds: List[str] = None,
        Targets: List[TargetTypeDef] = None,
        DetailType: DetailType = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Client.update_notification_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/client.html#update-notification-rule)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_event_types"]) -> ListEventTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListEventTypes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/paginators.html#listeventtypespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notification_rules"]
    ) -> ListNotificationRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListNotificationRules)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/paginators.html#listnotificationrulespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_targets"]) -> ListTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-notifications.html#CodeStarNotifications.Paginator.ListTargets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_notifications/paginators.html#listtargetspaginator)
        """
