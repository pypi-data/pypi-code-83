"""
Type annotations for route53resolver service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53resolver/type_defs.html)

Usage::

    ```python
    from mypy_boto3_route53resolver.type_defs import AssociateFirewallRuleGroupResponseTypeDef

    data: AssociateFirewallRuleGroupResponseTypeDef = {...}
    ```
"""
import sys
from typing import List

from mypy_boto3_route53resolver.literals import (
    Action,
    BlockResponse,
    FirewallDomainListStatus,
    FirewallFailOpenStatus,
    FirewallRuleGroupAssociationStatus,
    FirewallRuleGroupStatus,
    IpAddressStatus,
    MutationProtectionStatus,
    ResolverDNSSECValidationStatus,
    ResolverEndpointDirection,
    ResolverEndpointStatus,
    ResolverQueryLogConfigAssociationError,
    ResolverQueryLogConfigAssociationStatus,
    ResolverQueryLogConfigStatus,
    ResolverRuleAssociationStatus,
    ResolverRuleStatus,
    RuleTypeOption,
    ShareStatus,
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
    "AssociateFirewallRuleGroupResponseTypeDef",
    "AssociateResolverEndpointIpAddressResponseTypeDef",
    "AssociateResolverQueryLogConfigResponseTypeDef",
    "AssociateResolverRuleResponseTypeDef",
    "CreateFirewallDomainListResponseTypeDef",
    "CreateFirewallRuleGroupResponseTypeDef",
    "CreateFirewallRuleResponseTypeDef",
    "CreateResolverEndpointResponseTypeDef",
    "CreateResolverQueryLogConfigResponseTypeDef",
    "CreateResolverRuleResponseTypeDef",
    "DeleteFirewallDomainListResponseTypeDef",
    "DeleteFirewallRuleGroupResponseTypeDef",
    "DeleteFirewallRuleResponseTypeDef",
    "DeleteResolverEndpointResponseTypeDef",
    "DeleteResolverQueryLogConfigResponseTypeDef",
    "DeleteResolverRuleResponseTypeDef",
    "DisassociateFirewallRuleGroupResponseTypeDef",
    "DisassociateResolverEndpointIpAddressResponseTypeDef",
    "DisassociateResolverQueryLogConfigResponseTypeDef",
    "DisassociateResolverRuleResponseTypeDef",
    "FilterTypeDef",
    "FirewallConfigTypeDef",
    "FirewallDomainListMetadataTypeDef",
    "FirewallDomainListTypeDef",
    "FirewallRuleGroupAssociationTypeDef",
    "FirewallRuleGroupMetadataTypeDef",
    "FirewallRuleGroupTypeDef",
    "FirewallRuleTypeDef",
    "GetFirewallConfigResponseTypeDef",
    "GetFirewallDomainListResponseTypeDef",
    "GetFirewallRuleGroupAssociationResponseTypeDef",
    "GetFirewallRuleGroupPolicyResponseTypeDef",
    "GetFirewallRuleGroupResponseTypeDef",
    "GetResolverDnssecConfigResponseTypeDef",
    "GetResolverEndpointResponseTypeDef",
    "GetResolverQueryLogConfigAssociationResponseTypeDef",
    "GetResolverQueryLogConfigPolicyResponseTypeDef",
    "GetResolverQueryLogConfigResponseTypeDef",
    "GetResolverRuleAssociationResponseTypeDef",
    "GetResolverRulePolicyResponseTypeDef",
    "GetResolverRuleResponseTypeDef",
    "ImportFirewallDomainsResponseTypeDef",
    "IpAddressRequestTypeDef",
    "IpAddressResponseTypeDef",
    "IpAddressUpdateTypeDef",
    "ListFirewallConfigsResponseTypeDef",
    "ListFirewallDomainListsResponseTypeDef",
    "ListFirewallDomainsResponseTypeDef",
    "ListFirewallRuleGroupAssociationsResponseTypeDef",
    "ListFirewallRuleGroupsResponseTypeDef",
    "ListFirewallRulesResponseTypeDef",
    "ListResolverDnssecConfigsResponseTypeDef",
    "ListResolverEndpointIpAddressesResponseTypeDef",
    "ListResolverEndpointsResponseTypeDef",
    "ListResolverQueryLogConfigAssociationsResponseTypeDef",
    "ListResolverQueryLogConfigsResponseTypeDef",
    "ListResolverRuleAssociationsResponseTypeDef",
    "ListResolverRulesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutFirewallRuleGroupPolicyResponseTypeDef",
    "PutResolverQueryLogConfigPolicyResponseTypeDef",
    "PutResolverRulePolicyResponseTypeDef",
    "ResolverDnssecConfigTypeDef",
    "ResolverEndpointTypeDef",
    "ResolverQueryLogConfigAssociationTypeDef",
    "ResolverQueryLogConfigTypeDef",
    "ResolverRuleAssociationTypeDef",
    "ResolverRuleConfigTypeDef",
    "ResolverRuleTypeDef",
    "TagTypeDef",
    "TargetAddressTypeDef",
    "UpdateFirewallConfigResponseTypeDef",
    "UpdateFirewallDomainsResponseTypeDef",
    "UpdateFirewallRuleGroupAssociationResponseTypeDef",
    "UpdateFirewallRuleResponseTypeDef",
    "UpdateResolverDnssecConfigResponseTypeDef",
    "UpdateResolverEndpointResponseTypeDef",
    "UpdateResolverRuleResponseTypeDef",
)


class AssociateFirewallRuleGroupResponseTypeDef(TypedDict, total=False):
    FirewallRuleGroupAssociation: "FirewallRuleGroupAssociationTypeDef"


class AssociateResolverEndpointIpAddressResponseTypeDef(TypedDict, total=False):
    ResolverEndpoint: "ResolverEndpointTypeDef"


class AssociateResolverQueryLogConfigResponseTypeDef(TypedDict, total=False):
    ResolverQueryLogConfigAssociation: "ResolverQueryLogConfigAssociationTypeDef"


class AssociateResolverRuleResponseTypeDef(TypedDict, total=False):
    ResolverRuleAssociation: "ResolverRuleAssociationTypeDef"


class CreateFirewallDomainListResponseTypeDef(TypedDict, total=False):
    FirewallDomainList: "FirewallDomainListTypeDef"


class CreateFirewallRuleGroupResponseTypeDef(TypedDict, total=False):
    FirewallRuleGroup: "FirewallRuleGroupTypeDef"


class CreateFirewallRuleResponseTypeDef(TypedDict, total=False):
    FirewallRule: "FirewallRuleTypeDef"


class CreateResolverEndpointResponseTypeDef(TypedDict, total=False):
    ResolverEndpoint: "ResolverEndpointTypeDef"


class CreateResolverQueryLogConfigResponseTypeDef(TypedDict, total=False):
    ResolverQueryLogConfig: "ResolverQueryLogConfigTypeDef"


class CreateResolverRuleResponseTypeDef(TypedDict, total=False):
    ResolverRule: "ResolverRuleTypeDef"


class DeleteFirewallDomainListResponseTypeDef(TypedDict, total=False):
    FirewallDomainList: "FirewallDomainListTypeDef"


class DeleteFirewallRuleGroupResponseTypeDef(TypedDict, total=False):
    FirewallRuleGroup: "FirewallRuleGroupTypeDef"


class DeleteFirewallRuleResponseTypeDef(TypedDict, total=False):
    FirewallRule: "FirewallRuleTypeDef"


class DeleteResolverEndpointResponseTypeDef(TypedDict, total=False):
    ResolverEndpoint: "ResolverEndpointTypeDef"


class DeleteResolverQueryLogConfigResponseTypeDef(TypedDict, total=False):
    ResolverQueryLogConfig: "ResolverQueryLogConfigTypeDef"


class DeleteResolverRuleResponseTypeDef(TypedDict, total=False):
    ResolverRule: "ResolverRuleTypeDef"


class DisassociateFirewallRuleGroupResponseTypeDef(TypedDict, total=False):
    FirewallRuleGroupAssociation: "FirewallRuleGroupAssociationTypeDef"


class DisassociateResolverEndpointIpAddressResponseTypeDef(TypedDict, total=False):
    ResolverEndpoint: "ResolverEndpointTypeDef"


class DisassociateResolverQueryLogConfigResponseTypeDef(TypedDict, total=False):
    ResolverQueryLogConfigAssociation: "ResolverQueryLogConfigAssociationTypeDef"


class DisassociateResolverRuleResponseTypeDef(TypedDict, total=False):
    ResolverRuleAssociation: "ResolverRuleAssociationTypeDef"


class FilterTypeDef(TypedDict, total=False):
    Name: str
    Values: List[str]


class FirewallConfigTypeDef(TypedDict, total=False):
    Id: str
    ResourceId: str
    OwnerId: str
    FirewallFailOpen: FirewallFailOpenStatus


class FirewallDomainListMetadataTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str
    CreatorRequestId: str
    ManagedOwnerName: str


class FirewallDomainListTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str
    DomainCount: int
    Status: FirewallDomainListStatus
    StatusMessage: str
    ManagedOwnerName: str
    CreatorRequestId: str
    CreationTime: str
    ModificationTime: str


class FirewallRuleGroupAssociationTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    FirewallRuleGroupId: str
    VpcId: str
    Name: str
    Priority: int
    MutationProtection: MutationProtectionStatus
    ManagedOwnerName: str
    Status: FirewallRuleGroupAssociationStatus
    StatusMessage: str
    CreatorRequestId: str
    CreationTime: str
    ModificationTime: str


class FirewallRuleGroupMetadataTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str
    OwnerId: str
    CreatorRequestId: str
    ShareStatus: ShareStatus


class FirewallRuleGroupTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str
    RuleCount: int
    Status: FirewallRuleGroupStatus
    StatusMessage: str
    OwnerId: str
    CreatorRequestId: str
    ShareStatus: ShareStatus
    CreationTime: str
    ModificationTime: str


class FirewallRuleTypeDef(TypedDict, total=False):
    FirewallRuleGroupId: str
    FirewallDomainListId: str
    Name: str
    Priority: int
    Action: Action
    BlockResponse: BlockResponse
    BlockOverrideDomain: str
    BlockOverrideDnsType: Literal["CNAME"]
    BlockOverrideTtl: int
    CreatorRequestId: str
    CreationTime: str
    ModificationTime: str


class GetFirewallConfigResponseTypeDef(TypedDict, total=False):
    FirewallConfig: "FirewallConfigTypeDef"


class GetFirewallDomainListResponseTypeDef(TypedDict, total=False):
    FirewallDomainList: "FirewallDomainListTypeDef"


class GetFirewallRuleGroupAssociationResponseTypeDef(TypedDict, total=False):
    FirewallRuleGroupAssociation: "FirewallRuleGroupAssociationTypeDef"


class GetFirewallRuleGroupPolicyResponseTypeDef(TypedDict, total=False):
    FirewallRuleGroupPolicy: str


class GetFirewallRuleGroupResponseTypeDef(TypedDict, total=False):
    FirewallRuleGroup: "FirewallRuleGroupTypeDef"


class GetResolverDnssecConfigResponseTypeDef(TypedDict, total=False):
    ResolverDNSSECConfig: "ResolverDnssecConfigTypeDef"


class GetResolverEndpointResponseTypeDef(TypedDict, total=False):
    ResolverEndpoint: "ResolverEndpointTypeDef"


class GetResolverQueryLogConfigAssociationResponseTypeDef(TypedDict, total=False):
    ResolverQueryLogConfigAssociation: "ResolverQueryLogConfigAssociationTypeDef"


class GetResolverQueryLogConfigPolicyResponseTypeDef(TypedDict, total=False):
    ResolverQueryLogConfigPolicy: str


class GetResolverQueryLogConfigResponseTypeDef(TypedDict, total=False):
    ResolverQueryLogConfig: "ResolverQueryLogConfigTypeDef"


class GetResolverRuleAssociationResponseTypeDef(TypedDict, total=False):
    ResolverRuleAssociation: "ResolverRuleAssociationTypeDef"


class GetResolverRulePolicyResponseTypeDef(TypedDict, total=False):
    ResolverRulePolicy: str


class GetResolverRuleResponseTypeDef(TypedDict, total=False):
    ResolverRule: "ResolverRuleTypeDef"


class ImportFirewallDomainsResponseTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Status: FirewallDomainListStatus
    StatusMessage: str


class _RequiredIpAddressRequestTypeDef(TypedDict):
    SubnetId: str


class IpAddressRequestTypeDef(_RequiredIpAddressRequestTypeDef, total=False):
    Ip: str


class IpAddressResponseTypeDef(TypedDict, total=False):
    IpId: str
    SubnetId: str
    Ip: str
    Status: IpAddressStatus
    StatusMessage: str
    CreationTime: str
    ModificationTime: str


class IpAddressUpdateTypeDef(TypedDict, total=False):
    IpId: str
    SubnetId: str
    Ip: str


class ListFirewallConfigsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    FirewallConfigs: List["FirewallConfigTypeDef"]


class ListFirewallDomainListsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    FirewallDomainLists: List["FirewallDomainListMetadataTypeDef"]


class ListFirewallDomainsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Domains: List[str]


class ListFirewallRuleGroupAssociationsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    FirewallRuleGroupAssociations: List["FirewallRuleGroupAssociationTypeDef"]


class ListFirewallRuleGroupsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    FirewallRuleGroups: List["FirewallRuleGroupMetadataTypeDef"]


class ListFirewallRulesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    FirewallRules: List["FirewallRuleTypeDef"]


class ListResolverDnssecConfigsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    ResolverDnssecConfigs: List["ResolverDnssecConfigTypeDef"]


class ListResolverEndpointIpAddressesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    MaxResults: int
    IpAddresses: List["IpAddressResponseTypeDef"]


class ListResolverEndpointsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    MaxResults: int
    ResolverEndpoints: List["ResolverEndpointTypeDef"]


class ListResolverQueryLogConfigAssociationsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    TotalCount: int
    TotalFilteredCount: int
    ResolverQueryLogConfigAssociations: List["ResolverQueryLogConfigAssociationTypeDef"]


class ListResolverQueryLogConfigsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    TotalCount: int
    TotalFilteredCount: int
    ResolverQueryLogConfigs: List["ResolverQueryLogConfigTypeDef"]


class ListResolverRuleAssociationsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    MaxResults: int
    ResolverRuleAssociations: List["ResolverRuleAssociationTypeDef"]


class ListResolverRulesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    MaxResults: int
    ResolverRules: List["ResolverRuleTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]
    NextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PutFirewallRuleGroupPolicyResponseTypeDef(TypedDict, total=False):
    ReturnValue: bool


class PutResolverQueryLogConfigPolicyResponseTypeDef(TypedDict, total=False):
    ReturnValue: bool


class PutResolverRulePolicyResponseTypeDef(TypedDict, total=False):
    ReturnValue: bool


class ResolverDnssecConfigTypeDef(TypedDict, total=False):
    Id: str
    OwnerId: str
    ResourceId: str
    ValidationStatus: ResolverDNSSECValidationStatus


class ResolverEndpointTypeDef(TypedDict, total=False):
    Id: str
    CreatorRequestId: str
    Arn: str
    Name: str
    SecurityGroupIds: List[str]
    Direction: ResolverEndpointDirection
    IpAddressCount: int
    HostVPCId: str
    Status: ResolverEndpointStatus
    StatusMessage: str
    CreationTime: str
    ModificationTime: str


class ResolverQueryLogConfigAssociationTypeDef(TypedDict, total=False):
    Id: str
    ResolverQueryLogConfigId: str
    ResourceId: str
    Status: ResolverQueryLogConfigAssociationStatus
    Error: ResolverQueryLogConfigAssociationError
    ErrorMessage: str
    CreationTime: str


class ResolverQueryLogConfigTypeDef(TypedDict, total=False):
    Id: str
    OwnerId: str
    Status: ResolverQueryLogConfigStatus
    ShareStatus: ShareStatus
    AssociationCount: int
    Arn: str
    Name: str
    DestinationArn: str
    CreatorRequestId: str
    CreationTime: str


class ResolverRuleAssociationTypeDef(TypedDict, total=False):
    Id: str
    ResolverRuleId: str
    Name: str
    VPCId: str
    Status: ResolverRuleAssociationStatus
    StatusMessage: str


class ResolverRuleConfigTypeDef(TypedDict, total=False):
    Name: str
    TargetIps: List["TargetAddressTypeDef"]
    ResolverEndpointId: str


class ResolverRuleTypeDef(TypedDict, total=False):
    Id: str
    CreatorRequestId: str
    Arn: str
    DomainName: str
    Status: ResolverRuleStatus
    StatusMessage: str
    RuleType: RuleTypeOption
    Name: str
    TargetIps: List["TargetAddressTypeDef"]
    ResolverEndpointId: str
    OwnerId: str
    ShareStatus: ShareStatus
    CreationTime: str
    ModificationTime: str


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class _RequiredTargetAddressTypeDef(TypedDict):
    Ip: str


class TargetAddressTypeDef(_RequiredTargetAddressTypeDef, total=False):
    Port: int


class UpdateFirewallConfigResponseTypeDef(TypedDict, total=False):
    FirewallConfig: "FirewallConfigTypeDef"


class UpdateFirewallDomainsResponseTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Status: FirewallDomainListStatus
    StatusMessage: str


class UpdateFirewallRuleGroupAssociationResponseTypeDef(TypedDict, total=False):
    FirewallRuleGroupAssociation: "FirewallRuleGroupAssociationTypeDef"


class UpdateFirewallRuleResponseTypeDef(TypedDict, total=False):
    FirewallRule: "FirewallRuleTypeDef"


class UpdateResolverDnssecConfigResponseTypeDef(TypedDict, total=False):
    ResolverDNSSECConfig: "ResolverDnssecConfigTypeDef"


class UpdateResolverEndpointResponseTypeDef(TypedDict, total=False):
    ResolverEndpoint: "ResolverEndpointTypeDef"


class UpdateResolverRuleResponseTypeDef(TypedDict, total=False):
    ResolverRule: "ResolverRuleTypeDef"
