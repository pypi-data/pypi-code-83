"""
Type annotations for fms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_fms.type_defs import AppTypeDef

    data: AppTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_fms.literals import (
    AccountRoleStatus,
    CustomerPolicyScopeIdType,
    DependentServiceName,
    PolicyComplianceStatusType,
    RemediationActionType,
    SecurityServiceType,
    ViolationReason,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AppTypeDef",
    "AppsListDataSummaryTypeDef",
    "AppsListDataTypeDef",
    "AwsEc2InstanceViolationTypeDef",
    "AwsEc2NetworkInterfaceViolationTypeDef",
    "AwsVPCSecurityGroupViolationTypeDef",
    "ComplianceViolatorTypeDef",
    "DnsDuplicateRuleGroupViolationTypeDef",
    "DnsRuleGroupLimitExceededViolationTypeDef",
    "DnsRuleGroupPriorityConflictViolationTypeDef",
    "EvaluationResultTypeDef",
    "GetAdminAccountResponseTypeDef",
    "GetAppsListResponseTypeDef",
    "GetComplianceDetailResponseTypeDef",
    "GetNotificationChannelResponseTypeDef",
    "GetPolicyResponseTypeDef",
    "GetProtectionStatusResponseTypeDef",
    "GetProtocolsListResponseTypeDef",
    "GetViolationDetailsResponseTypeDef",
    "ListAppsListsResponseTypeDef",
    "ListComplianceStatusResponseTypeDef",
    "ListMemberAccountsResponseTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListProtocolsListsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkFirewallMissingExpectedRTViolationTypeDef",
    "NetworkFirewallMissingFirewallViolationTypeDef",
    "NetworkFirewallMissingSubnetViolationTypeDef",
    "NetworkFirewallPolicyDescriptionTypeDef",
    "NetworkFirewallPolicyModifiedViolationTypeDef",
    "PaginatorConfigTypeDef",
    "PartialMatchTypeDef",
    "PolicyComplianceDetailTypeDef",
    "PolicyComplianceStatusTypeDef",
    "PolicySummaryTypeDef",
    "PolicyTypeDef",
    "ProtocolsListDataSummaryTypeDef",
    "ProtocolsListDataTypeDef",
    "PutAppsListResponseTypeDef",
    "PutPolicyResponseTypeDef",
    "PutProtocolsListResponseTypeDef",
    "ResourceTagTypeDef",
    "ResourceViolationTypeDef",
    "SecurityGroupRemediationActionTypeDef",
    "SecurityGroupRuleDescriptionTypeDef",
    "SecurityServicePolicyDataTypeDef",
    "StatefulRuleGroupTypeDef",
    "StatelessRuleGroupTypeDef",
    "TagTypeDef",
    "ViolationDetailTypeDef",
)

AppTypeDef = TypedDict("AppTypeDef", {"AppName": str, "Protocol": str, "Port": int})


class AppsListDataSummaryTypeDef(TypedDict, total=False):
    ListArn: str
    ListId: str
    ListName: str
    AppsList: List["AppTypeDef"]


class _RequiredAppsListDataTypeDef(TypedDict):
    ListName: str
    AppsList: List["AppTypeDef"]


class AppsListDataTypeDef(_RequiredAppsListDataTypeDef, total=False):
    ListId: str
    ListUpdateToken: str
    CreateTime: datetime
    LastUpdateTime: datetime
    PreviousAppsList: Dict[str, List["AppTypeDef"]]


class AwsEc2InstanceViolationTypeDef(TypedDict, total=False):
    ViolationTarget: str
    AwsEc2NetworkInterfaceViolations: List["AwsEc2NetworkInterfaceViolationTypeDef"]


class AwsEc2NetworkInterfaceViolationTypeDef(TypedDict, total=False):
    ViolationTarget: str
    ViolatingSecurityGroups: List[str]


class AwsVPCSecurityGroupViolationTypeDef(TypedDict, total=False):
    ViolationTarget: str
    ViolationTargetDescription: str
    PartialMatches: List["PartialMatchTypeDef"]
    PossibleSecurityGroupRemediationActions: List["SecurityGroupRemediationActionTypeDef"]


class ComplianceViolatorTypeDef(TypedDict, total=False):
    ResourceId: str
    ViolationReason: ViolationReason
    ResourceType: str


class DnsDuplicateRuleGroupViolationTypeDef(TypedDict, total=False):
    ViolationTarget: str
    ViolationTargetDescription: str


class DnsRuleGroupLimitExceededViolationTypeDef(TypedDict, total=False):
    ViolationTarget: str
    ViolationTargetDescription: str
    NumberOfRuleGroupsAlreadyAssociated: int


class DnsRuleGroupPriorityConflictViolationTypeDef(TypedDict, total=False):
    ViolationTarget: str
    ViolationTargetDescription: str
    ConflictingPriority: int
    ConflictingPolicyId: str
    UnavailablePriorities: List[int]


class EvaluationResultTypeDef(TypedDict, total=False):
    ComplianceStatus: PolicyComplianceStatusType
    ViolatorCount: int
    EvaluationLimitExceeded: bool


class GetAdminAccountResponseTypeDef(TypedDict, total=False):
    AdminAccount: str
    RoleStatus: AccountRoleStatus


class GetAppsListResponseTypeDef(TypedDict, total=False):
    AppsList: "AppsListDataTypeDef"
    AppsListArn: str


class GetComplianceDetailResponseTypeDef(TypedDict, total=False):
    PolicyComplianceDetail: "PolicyComplianceDetailTypeDef"


class GetNotificationChannelResponseTypeDef(TypedDict, total=False):
    SnsTopicArn: str
    SnsRoleName: str


class GetPolicyResponseTypeDef(TypedDict, total=False):
    Policy: "PolicyTypeDef"
    PolicyArn: str


class GetProtectionStatusResponseTypeDef(TypedDict, total=False):
    AdminAccountId: str
    ServiceType: SecurityServiceType
    Data: str
    NextToken: str


class GetProtocolsListResponseTypeDef(TypedDict, total=False):
    ProtocolsList: "ProtocolsListDataTypeDef"
    ProtocolsListArn: str


class GetViolationDetailsResponseTypeDef(TypedDict, total=False):
    ViolationDetail: "ViolationDetailTypeDef"


class ListAppsListsResponseTypeDef(TypedDict, total=False):
    AppsLists: List["AppsListDataSummaryTypeDef"]
    NextToken: str


class ListComplianceStatusResponseTypeDef(TypedDict, total=False):
    PolicyComplianceStatusList: List["PolicyComplianceStatusTypeDef"]
    NextToken: str


class ListMemberAccountsResponseTypeDef(TypedDict, total=False):
    MemberAccounts: List[str]
    NextToken: str


class ListPoliciesResponseTypeDef(TypedDict, total=False):
    PolicyList: List["PolicySummaryTypeDef"]
    NextToken: str


class ListProtocolsListsResponseTypeDef(TypedDict, total=False):
    ProtocolsLists: List["ProtocolsListDataSummaryTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    TagList: List["TagTypeDef"]


class NetworkFirewallMissingExpectedRTViolationTypeDef(TypedDict, total=False):
    ViolationTarget: str
    VPC: str
    AvailabilityZone: str
    CurrentRouteTable: str
    ExpectedRouteTable: str


class NetworkFirewallMissingFirewallViolationTypeDef(TypedDict, total=False):
    ViolationTarget: str
    VPC: str
    AvailabilityZone: str
    TargetViolationReason: str


class NetworkFirewallMissingSubnetViolationTypeDef(TypedDict, total=False):
    ViolationTarget: str
    VPC: str
    AvailabilityZone: str
    TargetViolationReason: str


class NetworkFirewallPolicyDescriptionTypeDef(TypedDict, total=False):
    StatelessRuleGroups: List["StatelessRuleGroupTypeDef"]
    StatelessDefaultActions: List[str]
    StatelessFragmentDefaultActions: List[str]
    StatelessCustomActions: List[str]
    StatefulRuleGroups: List["StatefulRuleGroupTypeDef"]


class NetworkFirewallPolicyModifiedViolationTypeDef(TypedDict, total=False):
    ViolationTarget: str
    CurrentPolicyDescription: "NetworkFirewallPolicyDescriptionTypeDef"
    ExpectedPolicyDescription: "NetworkFirewallPolicyDescriptionTypeDef"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PartialMatchTypeDef(TypedDict, total=False):
    Reference: str
    TargetViolationReasons: List[str]


class PolicyComplianceDetailTypeDef(TypedDict, total=False):
    PolicyOwner: str
    PolicyId: str
    MemberAccount: str
    Violators: List["ComplianceViolatorTypeDef"]
    EvaluationLimitExceeded: bool
    ExpiredAt: datetime
    IssueInfoMap: Dict[DependentServiceName, str]


class PolicyComplianceStatusTypeDef(TypedDict, total=False):
    PolicyOwner: str
    PolicyId: str
    PolicyName: str
    MemberAccount: str
    EvaluationResults: List["EvaluationResultTypeDef"]
    LastUpdated: datetime
    IssueInfoMap: Dict[DependentServiceName, str]


class PolicySummaryTypeDef(TypedDict, total=False):
    PolicyArn: str
    PolicyId: str
    PolicyName: str
    ResourceType: str
    SecurityServiceType: SecurityServiceType
    RemediationEnabled: bool


class _RequiredPolicyTypeDef(TypedDict):
    PolicyName: str
    SecurityServicePolicyData: "SecurityServicePolicyDataTypeDef"
    ResourceType: str
    ExcludeResourceTags: bool
    RemediationEnabled: bool


class PolicyTypeDef(_RequiredPolicyTypeDef, total=False):
    PolicyId: str
    PolicyUpdateToken: str
    ResourceTypeList: List[str]
    ResourceTags: List["ResourceTagTypeDef"]
    IncludeMap: Dict[CustomerPolicyScopeIdType, List[str]]
    ExcludeMap: Dict[CustomerPolicyScopeIdType, List[str]]


class ProtocolsListDataSummaryTypeDef(TypedDict, total=False):
    ListArn: str
    ListId: str
    ListName: str
    ProtocolsList: List[str]


class _RequiredProtocolsListDataTypeDef(TypedDict):
    ListName: str
    ProtocolsList: List[str]


class ProtocolsListDataTypeDef(_RequiredProtocolsListDataTypeDef, total=False):
    ListId: str
    ListUpdateToken: str
    CreateTime: datetime
    LastUpdateTime: datetime
    PreviousProtocolsList: Dict[str, List[str]]


class PutAppsListResponseTypeDef(TypedDict, total=False):
    AppsList: "AppsListDataTypeDef"
    AppsListArn: str


class PutPolicyResponseTypeDef(TypedDict, total=False):
    Policy: "PolicyTypeDef"
    PolicyArn: str


class PutProtocolsListResponseTypeDef(TypedDict, total=False):
    ProtocolsList: "ProtocolsListDataTypeDef"
    ProtocolsListArn: str


class _RequiredResourceTagTypeDef(TypedDict):
    Key: str


class ResourceTagTypeDef(_RequiredResourceTagTypeDef, total=False):
    Value: str


class ResourceViolationTypeDef(TypedDict, total=False):
    AwsVPCSecurityGroupViolation: "AwsVPCSecurityGroupViolationTypeDef"
    AwsEc2NetworkInterfaceViolation: "AwsEc2NetworkInterfaceViolationTypeDef"
    AwsEc2InstanceViolation: "AwsEc2InstanceViolationTypeDef"
    NetworkFirewallMissingFirewallViolation: "NetworkFirewallMissingFirewallViolationTypeDef"
    NetworkFirewallMissingSubnetViolation: "NetworkFirewallMissingSubnetViolationTypeDef"
    NetworkFirewallMissingExpectedRTViolation: "NetworkFirewallMissingExpectedRTViolationTypeDef"
    NetworkFirewallPolicyModifiedViolation: "NetworkFirewallPolicyModifiedViolationTypeDef"
    DnsRuleGroupPriorityConflictViolation: "DnsRuleGroupPriorityConflictViolationTypeDef"
    DnsDuplicateRuleGroupViolation: "DnsDuplicateRuleGroupViolationTypeDef"
    DnsRuleGroupLimitExceededViolation: "DnsRuleGroupLimitExceededViolationTypeDef"


class SecurityGroupRemediationActionTypeDef(TypedDict, total=False):
    RemediationActionType: RemediationActionType
    Description: str
    RemediationResult: "SecurityGroupRuleDescriptionTypeDef"
    IsDefaultAction: bool


SecurityGroupRuleDescriptionTypeDef = TypedDict(
    "SecurityGroupRuleDescriptionTypeDef",
    {
        "IPV4Range": str,
        "IPV6Range": str,
        "PrefixListId": str,
        "Protocol": str,
        "FromPort": int,
        "ToPort": int,
    },
    total=False,
)

_RequiredSecurityServicePolicyDataTypeDef = TypedDict(
    "_RequiredSecurityServicePolicyDataTypeDef", {"Type": SecurityServiceType}
)
_OptionalSecurityServicePolicyDataTypeDef = TypedDict(
    "_OptionalSecurityServicePolicyDataTypeDef", {"ManagedServiceData": str}, total=False
)


class SecurityServicePolicyDataTypeDef(
    _RequiredSecurityServicePolicyDataTypeDef, _OptionalSecurityServicePolicyDataTypeDef
):
    pass


class StatefulRuleGroupTypeDef(TypedDict, total=False):
    RuleGroupName: str
    ResourceId: str


class StatelessRuleGroupTypeDef(TypedDict, total=False):
    RuleGroupName: str
    ResourceId: str
    Priority: int


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class _RequiredViolationDetailTypeDef(TypedDict):
    PolicyId: str
    MemberAccount: str
    ResourceId: str
    ResourceType: str
    ResourceViolations: List["ResourceViolationTypeDef"]


class ViolationDetailTypeDef(_RequiredViolationDetailTypeDef, total=False):
    ResourceTags: List["TagTypeDef"]
    ResourceDescription: str
