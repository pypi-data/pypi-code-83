"""
Type annotations for wafv2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_wafv2 import WAFV2Client

    client: WAFV2Client = boto3.client("wafv2")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_wafv2.literals import IPAddressVersion, ResourceType, Scope
from mypy_boto3_wafv2.type_defs import (
    CheckCapacityResponseTypeDef,
    CreateIPSetResponseTypeDef,
    CreateRegexPatternSetResponseTypeDef,
    CreateRuleGroupResponseTypeDef,
    CreateWebACLResponseTypeDef,
    CustomResponseBodyTypeDef,
    DefaultActionTypeDef,
    DeleteFirewallManagerRuleGroupsResponseTypeDef,
    DescribeManagedRuleGroupResponseTypeDef,
    GetIPSetResponseTypeDef,
    GetLoggingConfigurationResponseTypeDef,
    GetPermissionPolicyResponseTypeDef,
    GetRateBasedStatementManagedKeysResponseTypeDef,
    GetRegexPatternSetResponseTypeDef,
    GetRuleGroupResponseTypeDef,
    GetSampledRequestsResponseTypeDef,
    GetWebACLForResourceResponseTypeDef,
    GetWebACLResponseTypeDef,
    ListAvailableManagedRuleGroupsResponseTypeDef,
    ListIPSetsResponseTypeDef,
    ListLoggingConfigurationsResponseTypeDef,
    ListRegexPatternSetsResponseTypeDef,
    ListResourcesForWebACLResponseTypeDef,
    ListRuleGroupsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListWebACLsResponseTypeDef,
    LoggingConfigurationTypeDef,
    PutLoggingConfigurationResponseTypeDef,
    RegexTypeDef,
    RuleTypeDef,
    TagTypeDef,
    TimeWindowTypeDef,
    UpdateIPSetResponseTypeDef,
    UpdateRegexPatternSetResponseTypeDef,
    UpdateRuleGroupResponseTypeDef,
    UpdateWebACLResponseTypeDef,
    VisibilityConfigTypeDef,
)

__all__ = ("WAFV2Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    WAFAssociatedItemException: Type[BotocoreClientError]
    WAFDuplicateItemException: Type[BotocoreClientError]
    WAFInternalErrorException: Type[BotocoreClientError]
    WAFInvalidOperationException: Type[BotocoreClientError]
    WAFInvalidParameterException: Type[BotocoreClientError]
    WAFInvalidPermissionPolicyException: Type[BotocoreClientError]
    WAFInvalidResourceException: Type[BotocoreClientError]
    WAFLimitsExceededException: Type[BotocoreClientError]
    WAFNonexistentItemException: Type[BotocoreClientError]
    WAFOptimisticLockException: Type[BotocoreClientError]
    WAFServiceLinkedRoleErrorException: Type[BotocoreClientError]
    WAFSubscriptionNotFoundException: Type[BotocoreClientError]
    WAFTagOperationException: Type[BotocoreClientError]
    WAFTagOperationInternalErrorException: Type[BotocoreClientError]
    WAFUnavailableEntityException: Type[BotocoreClientError]


class WAFV2Client:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_web_acl(self, WebACLArn: str, ResourceArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.associate_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#associate-web-acl)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#can-paginate)
        """

    def check_capacity(
        self, Scope: Scope, Rules: List["RuleTypeDef"]
    ) -> CheckCapacityResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.check_capacity)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#check-capacity)
        """

    def create_ip_set(
        self,
        Name: str,
        Scope: Scope,
        IPAddressVersion: IPAddressVersion,
        Addresses: List[str],
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateIPSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.create_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#create-ip-set)
        """

    def create_regex_pattern_set(
        self,
        Name: str,
        Scope: Scope,
        RegularExpressionList: List["RegexTypeDef"],
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateRegexPatternSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.create_regex_pattern_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#create-regex-pattern-set)
        """

    def create_rule_group(
        self,
        Name: str,
        Scope: Scope,
        Capacity: int,
        VisibilityConfig: "VisibilityConfigTypeDef",
        Description: str = None,
        Rules: List["RuleTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        CustomResponseBodies: Dict[str, "CustomResponseBodyTypeDef"] = None,
    ) -> CreateRuleGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.create_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#create-rule-group)
        """

    def create_web_acl(
        self,
        Name: str,
        Scope: Scope,
        DefaultAction: "DefaultActionTypeDef",
        VisibilityConfig: "VisibilityConfigTypeDef",
        Description: str = None,
        Rules: List["RuleTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
        CustomResponseBodies: Dict[str, "CustomResponseBodyTypeDef"] = None,
    ) -> CreateWebACLResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.create_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#create-web-acl)
        """

    def delete_firewall_manager_rule_groups(
        self, WebACLArn: str, WebACLLockToken: str
    ) -> DeleteFirewallManagerRuleGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.delete_firewall_manager_rule_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#delete-firewall-manager-rule-groups)
        """

    def delete_ip_set(self, Name: str, Scope: Scope, Id: str, LockToken: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.delete_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#delete-ip-set)
        """

    def delete_logging_configuration(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.delete_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#delete-logging-configuration)
        """

    def delete_permission_policy(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.delete_permission_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#delete-permission-policy)
        """

    def delete_regex_pattern_set(
        self, Name: str, Scope: Scope, Id: str, LockToken: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.delete_regex_pattern_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#delete-regex-pattern-set)
        """

    def delete_rule_group(self, Name: str, Scope: Scope, Id: str, LockToken: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.delete_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#delete-rule-group)
        """

    def delete_web_acl(self, Name: str, Scope: Scope, Id: str, LockToken: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.delete_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#delete-web-acl)
        """

    def describe_managed_rule_group(
        self, VendorName: str, Name: str, Scope: Scope
    ) -> DescribeManagedRuleGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.describe_managed_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#describe-managed-rule-group)
        """

    def disassociate_web_acl(self, ResourceArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.disassociate_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#disassociate-web-acl)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#generate-presigned-url)
        """

    def get_ip_set(self, Name: str, Scope: Scope, Id: str) -> GetIPSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.get_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get-ip-set)
        """

    def get_logging_configuration(self, ResourceArn: str) -> GetLoggingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.get_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get-logging-configuration)
        """

    def get_permission_policy(self, ResourceArn: str) -> GetPermissionPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.get_permission_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get-permission-policy)
        """

    def get_rate_based_statement_managed_keys(
        self, Scope: Scope, WebACLName: str, WebACLId: str, RuleName: str
    ) -> GetRateBasedStatementManagedKeysResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.get_rate_based_statement_managed_keys)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get-rate-based-statement-managed-keys)
        """

    def get_regex_pattern_set(
        self, Name: str, Scope: Scope, Id: str
    ) -> GetRegexPatternSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.get_regex_pattern_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get-regex-pattern-set)
        """

    def get_rule_group(self, Name: str, Scope: Scope, Id: str) -> GetRuleGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.get_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get-rule-group)
        """

    def get_sampled_requests(
        self,
        WebAclArn: str,
        RuleMetricName: str,
        Scope: Scope,
        TimeWindow: "TimeWindowTypeDef",
        MaxItems: int,
    ) -> GetSampledRequestsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.get_sampled_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get-sampled-requests)
        """

    def get_web_acl(self, Name: str, Scope: Scope, Id: str) -> GetWebACLResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.get_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get-web-acl)
        """

    def get_web_acl_for_resource(self, ResourceArn: str) -> GetWebACLForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.get_web_acl_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#get-web-acl-for-resource)
        """

    def list_available_managed_rule_groups(
        self, Scope: Scope, NextMarker: str = None, Limit: int = None
    ) -> ListAvailableManagedRuleGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.list_available_managed_rule_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list-available-managed-rule-groups)
        """

    def list_ip_sets(
        self, Scope: Scope, NextMarker: str = None, Limit: int = None
    ) -> ListIPSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.list_ip_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list-ip-sets)
        """

    def list_logging_configurations(
        self, Scope: Scope = None, NextMarker: str = None, Limit: int = None
    ) -> ListLoggingConfigurationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.list_logging_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list-logging-configurations)
        """

    def list_regex_pattern_sets(
        self, Scope: Scope, NextMarker: str = None, Limit: int = None
    ) -> ListRegexPatternSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.list_regex_pattern_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list-regex-pattern-sets)
        """

    def list_resources_for_web_acl(
        self, WebACLArn: str, ResourceType: ResourceType = None
    ) -> ListResourcesForWebACLResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.list_resources_for_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list-resources-for-web-acl)
        """

    def list_rule_groups(
        self, Scope: Scope, NextMarker: str = None, Limit: int = None
    ) -> ListRuleGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.list_rule_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list-rule-groups)
        """

    def list_tags_for_resource(
        self, ResourceARN: str, NextMarker: str = None, Limit: int = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list-tags-for-resource)
        """

    def list_web_acls(
        self, Scope: Scope, NextMarker: str = None, Limit: int = None
    ) -> ListWebACLsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.list_web_acls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#list-web-acls)
        """

    def put_logging_configuration(
        self, LoggingConfiguration: "LoggingConfigurationTypeDef"
    ) -> PutLoggingConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.put_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#put-logging-configuration)
        """

    def put_permission_policy(self, ResourceArn: str, Policy: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.put_permission_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#put-permission-policy)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#tag-resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#untag-resource)
        """

    def update_ip_set(
        self,
        Name: str,
        Scope: Scope,
        Id: str,
        Addresses: List[str],
        LockToken: str,
        Description: str = None,
    ) -> UpdateIPSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.update_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#update-ip-set)
        """

    def update_regex_pattern_set(
        self,
        Name: str,
        Scope: Scope,
        Id: str,
        RegularExpressionList: List["RegexTypeDef"],
        LockToken: str,
        Description: str = None,
    ) -> UpdateRegexPatternSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.update_regex_pattern_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#update-regex-pattern-set)
        """

    def update_rule_group(
        self,
        Name: str,
        Scope: Scope,
        Id: str,
        VisibilityConfig: "VisibilityConfigTypeDef",
        LockToken: str,
        Description: str = None,
        Rules: List["RuleTypeDef"] = None,
        CustomResponseBodies: Dict[str, "CustomResponseBodyTypeDef"] = None,
    ) -> UpdateRuleGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.update_rule_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#update-rule-group)
        """

    def update_web_acl(
        self,
        Name: str,
        Scope: Scope,
        Id: str,
        DefaultAction: "DefaultActionTypeDef",
        VisibilityConfig: "VisibilityConfigTypeDef",
        LockToken: str,
        Description: str = None,
        Rules: List["RuleTypeDef"] = None,
        CustomResponseBodies: Dict[str, "CustomResponseBodyTypeDef"] = None,
    ) -> UpdateWebACLResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/wafv2.html#WAFV2.Client.update_web_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/client.html#update-web-acl)
        """
