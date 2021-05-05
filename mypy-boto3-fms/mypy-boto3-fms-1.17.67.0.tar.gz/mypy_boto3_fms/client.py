"""
Type annotations for fms service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_fms import FMSClient

    client: FMSClient = boto3.client("fms")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_fms.paginator import (
    ListComplianceStatusPaginator,
    ListMemberAccountsPaginator,
    ListPoliciesPaginator,
)
from mypy_boto3_fms.type_defs import (
    AppsListDataTypeDef,
    GetAdminAccountResponseTypeDef,
    GetAppsListResponseTypeDef,
    GetComplianceDetailResponseTypeDef,
    GetNotificationChannelResponseTypeDef,
    GetPolicyResponseTypeDef,
    GetProtectionStatusResponseTypeDef,
    GetProtocolsListResponseTypeDef,
    GetViolationDetailsResponseTypeDef,
    ListAppsListsResponseTypeDef,
    ListComplianceStatusResponseTypeDef,
    ListMemberAccountsResponseTypeDef,
    ListPoliciesResponseTypeDef,
    ListProtocolsListsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PolicyTypeDef,
    ProtocolsListDataTypeDef,
    PutAppsListResponseTypeDef,
    PutPolicyResponseTypeDef,
    PutProtocolsListResponseTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("FMSClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    InvalidOperationException: Type[BotocoreClientError]
    InvalidTypeException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class FMSClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_admin_account(self, AdminAccount: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.associate_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#associate-admin-account)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#can-paginate)
        """

    def delete_apps_list(self, ListId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.delete_apps_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#delete-apps-list)
        """

    def delete_notification_channel(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.delete_notification_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#delete-notification-channel)
        """

    def delete_policy(self, PolicyId: str, DeleteAllPolicyResources: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.delete_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#delete-policy)
        """

    def delete_protocols_list(self, ListId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.delete_protocols_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#delete-protocols-list)
        """

    def disassociate_admin_account(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.disassociate_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#disassociate-admin-account)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#generate-presigned-url)
        """

    def get_admin_account(self) -> GetAdminAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.get_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get-admin-account)
        """

    def get_apps_list(self, ListId: str, DefaultList: bool = None) -> GetAppsListResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.get_apps_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get-apps-list)
        """

    def get_compliance_detail(
        self, PolicyId: str, MemberAccount: str
    ) -> GetComplianceDetailResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.get_compliance_detail)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get-compliance-detail)
        """

    def get_notification_channel(self) -> GetNotificationChannelResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.get_notification_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get-notification-channel)
        """

    def get_policy(self, PolicyId: str) -> GetPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.get_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get-policy)
        """

    def get_protection_status(
        self,
        PolicyId: str,
        MemberAccountId: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetProtectionStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.get_protection_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get-protection-status)
        """

    def get_protocols_list(
        self, ListId: str, DefaultList: bool = None
    ) -> GetProtocolsListResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.get_protocols_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get-protocols-list)
        """

    def get_violation_details(
        self, PolicyId: str, MemberAccount: str, ResourceId: str, ResourceType: str
    ) -> GetViolationDetailsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.get_violation_details)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#get-violation-details)
        """

    def list_apps_lists(
        self, MaxResults: int, DefaultLists: bool = None, NextToken: str = None
    ) -> ListAppsListsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.list_apps_lists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list-apps-lists)
        """

    def list_compliance_status(
        self, PolicyId: str, NextToken: str = None, MaxResults: int = None
    ) -> ListComplianceStatusResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.list_compliance_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list-compliance-status)
        """

    def list_member_accounts(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListMemberAccountsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.list_member_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list-member-accounts)
        """

    def list_policies(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.list_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list-policies)
        """

    def list_protocols_lists(
        self, MaxResults: int, DefaultLists: bool = None, NextToken: str = None
    ) -> ListProtocolsListsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.list_protocols_lists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list-protocols-lists)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#list-tags-for-resource)
        """

    def put_apps_list(
        self, AppsList: "AppsListDataTypeDef", TagList: List["TagTypeDef"] = None
    ) -> PutAppsListResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.put_apps_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#put-apps-list)
        """

    def put_notification_channel(self, SnsTopicArn: str, SnsRoleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.put_notification_channel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#put-notification-channel)
        """

    def put_policy(
        self, Policy: "PolicyTypeDef", TagList: List["TagTypeDef"] = None
    ) -> PutPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.put_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#put-policy)
        """

    def put_protocols_list(
        self, ProtocolsList: "ProtocolsListDataTypeDef", TagList: List["TagTypeDef"] = None
    ) -> PutProtocolsListResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.put_protocols_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#put-protocols-list)
        """

    def tag_resource(self, ResourceArn: str, TagList: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/client.html#untag-resource)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compliance_status"]
    ) -> ListComplianceStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Paginator.ListComplianceStatus)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators.html#listcompliancestatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_member_accounts"]
    ) -> ListMemberAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Paginator.ListMemberAccounts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators.html#listmemberaccountspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_policies"]) -> ListPoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/fms.html#FMS.Paginator.ListPolicies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/paginators.html#listpoliciespaginator)
        """
