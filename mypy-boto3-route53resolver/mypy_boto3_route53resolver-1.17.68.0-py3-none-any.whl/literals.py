"""
Type annotations for route53resolver service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/literals.html)

Usage::

    ```python
    from mypy_boto3_route53resolver.literals import Action

    data: Action = "ALERT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "Action",
    "BlockOverrideDnsType",
    "BlockResponse",
    "FirewallDomainImportOperation",
    "FirewallDomainListStatus",
    "FirewallDomainUpdateOperation",
    "FirewallFailOpenStatus",
    "FirewallRuleGroupAssociationStatus",
    "FirewallRuleGroupStatus",
    "IpAddressStatus",
    "ListFirewallConfigsPaginatorName",
    "ListFirewallDomainListsPaginatorName",
    "ListFirewallDomainsPaginatorName",
    "ListFirewallRuleGroupAssociationsPaginatorName",
    "ListFirewallRuleGroupsPaginatorName",
    "ListFirewallRulesPaginatorName",
    "ListResolverDnssecConfigsPaginatorName",
    "ListResolverEndpointIpAddressesPaginatorName",
    "ListResolverEndpointsPaginatorName",
    "ListResolverQueryLogConfigAssociationsPaginatorName",
    "ListResolverQueryLogConfigsPaginatorName",
    "ListResolverRuleAssociationsPaginatorName",
    "ListResolverRulesPaginatorName",
    "ListTagsForResourcePaginatorName",
    "MutationProtectionStatus",
    "ResolverDNSSECValidationStatus",
    "ResolverEndpointDirection",
    "ResolverEndpointStatus",
    "ResolverQueryLogConfigAssociationError",
    "ResolverQueryLogConfigAssociationStatus",
    "ResolverQueryLogConfigStatus",
    "ResolverRuleAssociationStatus",
    "ResolverRuleStatus",
    "RuleTypeOption",
    "ShareStatus",
    "SortOrder",
    "Validation",
)


Action = Literal["ALERT", "ALLOW", "BLOCK"]
BlockOverrideDnsType = Literal["CNAME"]
BlockResponse = Literal["NODATA", "NXDOMAIN", "OVERRIDE"]
FirewallDomainImportOperation = Literal["REPLACE"]
FirewallDomainListStatus = Literal[
    "COMPLETE", "COMPLETE_IMPORT_FAILED", "DELETING", "IMPORTING", "UPDATING"
]
FirewallDomainUpdateOperation = Literal["ADD", "REMOVE", "REPLACE"]
FirewallFailOpenStatus = Literal["DISABLED", "ENABLED"]
FirewallRuleGroupAssociationStatus = Literal["COMPLETE", "DELETING", "UPDATING"]
FirewallRuleGroupStatus = Literal["COMPLETE", "DELETING", "UPDATING"]
IpAddressStatus = Literal[
    "ATTACHED",
    "ATTACHING",
    "CREATING",
    "DELETE_FAILED_FAS_EXPIRED",
    "DELETING",
    "DETACHING",
    "FAILED_CREATION",
    "FAILED_RESOURCE_GONE",
    "REMAP_ATTACHING",
    "REMAP_DETACHING",
]
ListFirewallConfigsPaginatorName = Literal["list_firewall_configs"]
ListFirewallDomainListsPaginatorName = Literal["list_firewall_domain_lists"]
ListFirewallDomainsPaginatorName = Literal["list_firewall_domains"]
ListFirewallRuleGroupAssociationsPaginatorName = Literal["list_firewall_rule_group_associations"]
ListFirewallRuleGroupsPaginatorName = Literal["list_firewall_rule_groups"]
ListFirewallRulesPaginatorName = Literal["list_firewall_rules"]
ListResolverDnssecConfigsPaginatorName = Literal["list_resolver_dnssec_configs"]
ListResolverEndpointIpAddressesPaginatorName = Literal["list_resolver_endpoint_ip_addresses"]
ListResolverEndpointsPaginatorName = Literal["list_resolver_endpoints"]
ListResolverQueryLogConfigAssociationsPaginatorName = Literal[
    "list_resolver_query_log_config_associations"
]
ListResolverQueryLogConfigsPaginatorName = Literal["list_resolver_query_log_configs"]
ListResolverRuleAssociationsPaginatorName = Literal["list_resolver_rule_associations"]
ListResolverRulesPaginatorName = Literal["list_resolver_rules"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
MutationProtectionStatus = Literal["DISABLED", "ENABLED"]
ResolverDNSSECValidationStatus = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
ResolverEndpointDirection = Literal["INBOUND", "OUTBOUND"]
ResolverEndpointStatus = Literal[
    "ACTION_NEEDED", "AUTO_RECOVERING", "CREATING", "DELETING", "OPERATIONAL", "UPDATING"
]
ResolverQueryLogConfigAssociationError = Literal[
    "ACCESS_DENIED", "DESTINATION_NOT_FOUND", "INTERNAL_SERVICE_ERROR", "NONE"
]
ResolverQueryLogConfigAssociationStatus = Literal[
    "ACTION_NEEDED", "ACTIVE", "CREATING", "DELETING", "FAILED"
]
ResolverQueryLogConfigStatus = Literal["CREATED", "CREATING", "DELETING", "FAILED"]
ResolverRuleAssociationStatus = Literal["COMPLETE", "CREATING", "DELETING", "FAILED", "OVERRIDDEN"]
ResolverRuleStatus = Literal["COMPLETE", "DELETING", "FAILED", "UPDATING"]
RuleTypeOption = Literal["FORWARD", "RECURSIVE", "SYSTEM"]
ShareStatus = Literal["NOT_SHARED", "SHARED_BY_ME", "SHARED_WITH_ME"]
SortOrder = Literal["ASCENDING", "DESCENDING"]
Validation = Literal["DISABLE", "ENABLE"]
