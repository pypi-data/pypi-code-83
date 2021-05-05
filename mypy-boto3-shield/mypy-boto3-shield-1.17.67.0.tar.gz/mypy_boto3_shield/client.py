"""
Type annotations for shield service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_shield import ShieldClient

    client: ShieldClient = boto3.client("shield")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_shield.literals import (
    AutoRenew,
    ProtectedResourceType,
    ProtectionGroupAggregation,
    ProtectionGroupPattern,
)
from mypy_boto3_shield.paginator import ListAttacksPaginator, ListProtectionsPaginator
from mypy_boto3_shield.type_defs import (
    CreateProtectionResponseTypeDef,
    DescribeAttackResponseTypeDef,
    DescribeAttackStatisticsResponseTypeDef,
    DescribeDRTAccessResponseTypeDef,
    DescribeEmergencyContactSettingsResponseTypeDef,
    DescribeProtectionGroupResponseTypeDef,
    DescribeProtectionResponseTypeDef,
    DescribeSubscriptionResponseTypeDef,
    EmergencyContactTypeDef,
    GetSubscriptionStateResponseTypeDef,
    ListAttacksResponseTypeDef,
    ListProtectionGroupsResponseTypeDef,
    ListProtectionsResponseTypeDef,
    ListResourcesInProtectionGroupResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    TagTypeDef,
    TimeRangeTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ShieldClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AccessDeniedForDependencyException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidPaginationTokenException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidResourceException: Type[BotocoreClientError]
    LimitsExceededException: Type[BotocoreClientError]
    LockedSubscriptionException: Type[BotocoreClientError]
    NoAssociatedRoleException: Type[BotocoreClientError]
    OptimisticLockException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class ShieldClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_drt_log_bucket(self, LogBucket: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.associate_drt_log_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#associate-drt-log-bucket)
        """

    def associate_drt_role(self, RoleArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.associate_drt_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#associate-drt-role)
        """

    def associate_health_check(self, ProtectionId: str, HealthCheckArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.associate_health_check)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#associate-health-check)
        """

    def associate_proactive_engagement_details(
        self, EmergencyContactList: List["EmergencyContactTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.associate_proactive_engagement_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#associate-proactive-engagement-details)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#can-paginate)
        """

    def create_protection(
        self, Name: str, ResourceArn: str, Tags: List["TagTypeDef"] = None
    ) -> CreateProtectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.create_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#create-protection)
        """

    def create_protection_group(
        self,
        ProtectionGroupId: str,
        Aggregation: ProtectionGroupAggregation,
        Pattern: ProtectionGroupPattern,
        ResourceType: ProtectedResourceType = None,
        Members: List[str] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.create_protection_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#create-protection-group)
        """

    def create_subscription(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.create_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#create-subscription)
        """

    def delete_protection(self, ProtectionId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.delete_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#delete-protection)
        """

    def delete_protection_group(self, ProtectionGroupId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.delete_protection_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#delete-protection-group)
        """

    def delete_subscription(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.delete_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#delete-subscription)
        """

    def describe_attack(self, AttackId: str) -> DescribeAttackResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.describe_attack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#describe-attack)
        """

    def describe_attack_statistics(self) -> DescribeAttackStatisticsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.describe_attack_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#describe-attack-statistics)
        """

    def describe_drt_access(self) -> DescribeDRTAccessResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.describe_drt_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#describe-drt-access)
        """

    def describe_emergency_contact_settings(
        self,
    ) -> DescribeEmergencyContactSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.describe_emergency_contact_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#describe-emergency-contact-settings)
        """

    def describe_protection(
        self, ProtectionId: str = None, ResourceArn: str = None
    ) -> DescribeProtectionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.describe_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#describe-protection)
        """

    def describe_protection_group(
        self, ProtectionGroupId: str
    ) -> DescribeProtectionGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.describe_protection_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#describe-protection-group)
        """

    def describe_subscription(self) -> DescribeSubscriptionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.describe_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#describe-subscription)
        """

    def disable_proactive_engagement(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.disable_proactive_engagement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#disable-proactive-engagement)
        """

    def disassociate_drt_log_bucket(self, LogBucket: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.disassociate_drt_log_bucket)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#disassociate-drt-log-bucket)
        """

    def disassociate_drt_role(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.disassociate_drt_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#disassociate-drt-role)
        """

    def disassociate_health_check(self, ProtectionId: str, HealthCheckArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.disassociate_health_check)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#disassociate-health-check)
        """

    def enable_proactive_engagement(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.enable_proactive_engagement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#enable-proactive-engagement)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#generate-presigned-url)
        """

    def get_subscription_state(self) -> GetSubscriptionStateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.get_subscription_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#get-subscription-state)
        """

    def list_attacks(
        self,
        ResourceArns: List[str] = None,
        StartTime: "TimeRangeTypeDef" = None,
        EndTime: "TimeRangeTypeDef" = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListAttacksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.list_attacks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#list-attacks)
        """

    def list_protection_groups(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListProtectionGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.list_protection_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#list-protection-groups)
        """

    def list_protections(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListProtectionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.list_protections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#list-protections)
        """

    def list_resources_in_protection_group(
        self, ProtectionGroupId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListResourcesInProtectionGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.list_resources_in_protection_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#list-resources-in-protection-group)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#list-tags-for-resource)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#tag-resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#untag-resource)
        """

    def update_emergency_contact_settings(
        self, EmergencyContactList: List["EmergencyContactTypeDef"] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.update_emergency_contact_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#update-emergency-contact-settings)
        """

    def update_protection_group(
        self,
        ProtectionGroupId: str,
        Aggregation: ProtectionGroupAggregation,
        Pattern: ProtectionGroupPattern,
        ResourceType: ProtectedResourceType = None,
        Members: List[str] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.update_protection_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#update-protection-group)
        """

    def update_subscription(self, AutoRenew: AutoRenew = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Client.update_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/client.html#update-subscription)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_attacks"]) -> ListAttacksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Paginator.ListAttacks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/paginators.html#listattackspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_protections"]
    ) -> ListProtectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/shield.html#Shield.Paginator.ListProtections)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/paginators.html#listprotectionspaginator)
        """
