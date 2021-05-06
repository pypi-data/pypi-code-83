"""
Type annotations for network-firewall service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_network_firewall/type_defs.html)

Usage::

    ```python
    from mypy_boto3_network_firewall.type_defs import ActionDefinitionTypeDef

    data: ActionDefinitionTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_network_firewall.literals import (
    AttachmentStatus,
    ConfigurationSyncState,
    FirewallStatusValue,
    GeneratedRulesType,
    LogDestinationType,
    LogType,
    PerObjectSyncStatus,
    ResourceStatus,
    RuleGroupType,
    StatefulAction,
    StatefulRuleDirection,
    StatefulRuleProtocol,
    TargetType,
    TCPFlag,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionDefinitionTypeDef",
    "AddressTypeDef",
    "AssociateFirewallPolicyResponseTypeDef",
    "AssociateSubnetsResponseTypeDef",
    "AttachmentTypeDef",
    "CreateFirewallPolicyResponseTypeDef",
    "CreateFirewallResponseTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "CustomActionTypeDef",
    "DeleteFirewallPolicyResponseTypeDef",
    "DeleteFirewallResponseTypeDef",
    "DeleteRuleGroupResponseTypeDef",
    "DescribeFirewallPolicyResponseTypeDef",
    "DescribeFirewallResponseTypeDef",
    "DescribeLoggingConfigurationResponseTypeDef",
    "DescribeResourcePolicyResponseTypeDef",
    "DescribeRuleGroupResponseTypeDef",
    "DimensionTypeDef",
    "DisassociateSubnetsResponseTypeDef",
    "FirewallMetadataTypeDef",
    "FirewallPolicyMetadataTypeDef",
    "FirewallPolicyResponseTypeDef",
    "FirewallPolicyTypeDef",
    "FirewallStatusTypeDef",
    "FirewallTypeDef",
    "HeaderTypeDef",
    "IPSetTypeDef",
    "ListFirewallPoliciesResponseTypeDef",
    "ListFirewallsResponseTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogDestinationConfigTypeDef",
    "LoggingConfigurationTypeDef",
    "MatchAttributesTypeDef",
    "PaginatorConfigTypeDef",
    "PerObjectStatusTypeDef",
    "PortRangeTypeDef",
    "PortSetTypeDef",
    "PublishMetricActionTypeDef",
    "RuleDefinitionTypeDef",
    "RuleGroupMetadataTypeDef",
    "RuleGroupResponseTypeDef",
    "RuleGroupTypeDef",
    "RuleOptionTypeDef",
    "RuleVariablesTypeDef",
    "RulesSourceListTypeDef",
    "RulesSourceTypeDef",
    "StatefulRuleGroupReferenceTypeDef",
    "StatefulRuleTypeDef",
    "StatelessRuleGroupReferenceTypeDef",
    "StatelessRuleTypeDef",
    "StatelessRulesAndCustomActionsTypeDef",
    "SubnetMappingTypeDef",
    "SyncStateTypeDef",
    "TCPFlagFieldTypeDef",
    "TagTypeDef",
    "UpdateFirewallDeleteProtectionResponseTypeDef",
    "UpdateFirewallDescriptionResponseTypeDef",
    "UpdateFirewallPolicyChangeProtectionResponseTypeDef",
    "UpdateFirewallPolicyResponseTypeDef",
    "UpdateLoggingConfigurationResponseTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateSubnetChangeProtectionResponseTypeDef",
)


class ActionDefinitionTypeDef(TypedDict, total=False):
    PublishMetricAction: "PublishMetricActionTypeDef"


class AddressTypeDef(TypedDict):
    AddressDefinition: str


class AssociateFirewallPolicyResponseTypeDef(TypedDict, total=False):
    FirewallArn: str
    FirewallName: str
    FirewallPolicyArn: str
    UpdateToken: str


class AssociateSubnetsResponseTypeDef(TypedDict, total=False):
    FirewallArn: str
    FirewallName: str
    SubnetMappings: List["SubnetMappingTypeDef"]
    UpdateToken: str


class AttachmentTypeDef(TypedDict, total=False):
    SubnetId: str
    EndpointId: str
    Status: AttachmentStatus


class CreateFirewallPolicyResponseTypeDef(TypedDict):
    UpdateToken: str
    FirewallPolicyResponse: "FirewallPolicyResponseTypeDef"


class CreateFirewallResponseTypeDef(TypedDict, total=False):
    Firewall: "FirewallTypeDef"
    FirewallStatus: "FirewallStatusTypeDef"


class CreateRuleGroupResponseTypeDef(TypedDict):
    UpdateToken: str
    RuleGroupResponse: "RuleGroupResponseTypeDef"


class CustomActionTypeDef(TypedDict):
    ActionName: str
    ActionDefinition: "ActionDefinitionTypeDef"


class DeleteFirewallPolicyResponseTypeDef(TypedDict):
    FirewallPolicyResponse: "FirewallPolicyResponseTypeDef"


class DeleteFirewallResponseTypeDef(TypedDict, total=False):
    Firewall: "FirewallTypeDef"
    FirewallStatus: "FirewallStatusTypeDef"


class DeleteRuleGroupResponseTypeDef(TypedDict):
    RuleGroupResponse: "RuleGroupResponseTypeDef"


class _RequiredDescribeFirewallPolicyResponseTypeDef(TypedDict):
    UpdateToken: str
    FirewallPolicyResponse: "FirewallPolicyResponseTypeDef"


class DescribeFirewallPolicyResponseTypeDef(
    _RequiredDescribeFirewallPolicyResponseTypeDef, total=False
):
    FirewallPolicy: "FirewallPolicyTypeDef"


class DescribeFirewallResponseTypeDef(TypedDict, total=False):
    UpdateToken: str
    Firewall: "FirewallTypeDef"
    FirewallStatus: "FirewallStatusTypeDef"


class DescribeLoggingConfigurationResponseTypeDef(TypedDict, total=False):
    FirewallArn: str
    LoggingConfiguration: "LoggingConfigurationTypeDef"


class DescribeResourcePolicyResponseTypeDef(TypedDict, total=False):
    Policy: str


class _RequiredDescribeRuleGroupResponseTypeDef(TypedDict):
    UpdateToken: str
    RuleGroupResponse: "RuleGroupResponseTypeDef"


class DescribeRuleGroupResponseTypeDef(_RequiredDescribeRuleGroupResponseTypeDef, total=False):
    RuleGroup: "RuleGroupTypeDef"


class DimensionTypeDef(TypedDict):
    Value: str


class DisassociateSubnetsResponseTypeDef(TypedDict, total=False):
    FirewallArn: str
    FirewallName: str
    SubnetMappings: List["SubnetMappingTypeDef"]
    UpdateToken: str


class FirewallMetadataTypeDef(TypedDict, total=False):
    FirewallName: str
    FirewallArn: str


class FirewallPolicyMetadataTypeDef(TypedDict, total=False):
    Name: str
    Arn: str


class _RequiredFirewallPolicyResponseTypeDef(TypedDict):
    FirewallPolicyName: str
    FirewallPolicyArn: str
    FirewallPolicyId: str


class FirewallPolicyResponseTypeDef(_RequiredFirewallPolicyResponseTypeDef, total=False):
    Description: str
    FirewallPolicyStatus: ResourceStatus
    Tags: List["TagTypeDef"]


class _RequiredFirewallPolicyTypeDef(TypedDict):
    StatelessDefaultActions: List[str]
    StatelessFragmentDefaultActions: List[str]


class FirewallPolicyTypeDef(_RequiredFirewallPolicyTypeDef, total=False):
    StatelessRuleGroupReferences: List["StatelessRuleGroupReferenceTypeDef"]
    StatelessCustomActions: List["CustomActionTypeDef"]
    StatefulRuleGroupReferences: List["StatefulRuleGroupReferenceTypeDef"]


class _RequiredFirewallStatusTypeDef(TypedDict):
    Status: FirewallStatusValue
    ConfigurationSyncStateSummary: ConfigurationSyncState


class FirewallStatusTypeDef(_RequiredFirewallStatusTypeDef, total=False):
    SyncStates: Dict[str, "SyncStateTypeDef"]


class _RequiredFirewallTypeDef(TypedDict):
    FirewallPolicyArn: str
    VpcId: str
    SubnetMappings: List["SubnetMappingTypeDef"]
    FirewallId: str


class FirewallTypeDef(_RequiredFirewallTypeDef, total=False):
    FirewallName: str
    FirewallArn: str
    DeleteProtection: bool
    SubnetChangeProtection: bool
    FirewallPolicyChangeProtection: bool
    Description: str
    Tags: List["TagTypeDef"]


HeaderTypeDef = TypedDict(
    "HeaderTypeDef",
    {
        "Protocol": StatefulRuleProtocol,
        "Source": str,
        "SourcePort": str,
        "Direction": StatefulRuleDirection,
        "Destination": str,
        "DestinationPort": str,
    },
)


class IPSetTypeDef(TypedDict):
    Definition: List[str]


class ListFirewallPoliciesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    FirewallPolicies: List["FirewallPolicyMetadataTypeDef"]


class ListFirewallsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Firewalls: List["FirewallMetadataTypeDef"]


class ListRuleGroupsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    RuleGroups: List["RuleGroupMetadataTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Tags: List["TagTypeDef"]


class LogDestinationConfigTypeDef(TypedDict):
    LogType: LogType
    LogDestinationType: LogDestinationType
    LogDestination: Dict[str, str]


class LoggingConfigurationTypeDef(TypedDict):
    LogDestinationConfigs: List["LogDestinationConfigTypeDef"]


class MatchAttributesTypeDef(TypedDict, total=False):
    Sources: List["AddressTypeDef"]
    Destinations: List["AddressTypeDef"]
    SourcePorts: List["PortRangeTypeDef"]
    DestinationPorts: List["PortRangeTypeDef"]
    Protocols: List[int]
    TCPFlags: List["TCPFlagFieldTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PerObjectStatusTypeDef(TypedDict, total=False):
    SyncStatus: PerObjectSyncStatus
    UpdateToken: str


class PortRangeTypeDef(TypedDict):
    FromPort: int
    ToPort: int


class PortSetTypeDef(TypedDict, total=False):
    Definition: List[str]


class PublishMetricActionTypeDef(TypedDict):
    Dimensions: List["DimensionTypeDef"]


class RuleDefinitionTypeDef(TypedDict):
    MatchAttributes: "MatchAttributesTypeDef"
    Actions: List[str]


class RuleGroupMetadataTypeDef(TypedDict, total=False):
    Name: str
    Arn: str


_RequiredRuleGroupResponseTypeDef = TypedDict(
    "_RequiredRuleGroupResponseTypeDef",
    {"RuleGroupArn": str, "RuleGroupName": str, "RuleGroupId": str},
)
_OptionalRuleGroupResponseTypeDef = TypedDict(
    "_OptionalRuleGroupResponseTypeDef",
    {
        "Description": str,
        "Type": RuleGroupType,
        "Capacity": int,
        "RuleGroupStatus": ResourceStatus,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class RuleGroupResponseTypeDef(
    _RequiredRuleGroupResponseTypeDef, _OptionalRuleGroupResponseTypeDef
):
    pass


class _RequiredRuleGroupTypeDef(TypedDict):
    RulesSource: "RulesSourceTypeDef"


class RuleGroupTypeDef(_RequiredRuleGroupTypeDef, total=False):
    RuleVariables: "RuleVariablesTypeDef"


class _RequiredRuleOptionTypeDef(TypedDict):
    Keyword: str


class RuleOptionTypeDef(_RequiredRuleOptionTypeDef, total=False):
    Settings: List[str]


class RuleVariablesTypeDef(TypedDict, total=False):
    IPSets: Dict[str, "IPSetTypeDef"]
    PortSets: Dict[str, "PortSetTypeDef"]


class RulesSourceListTypeDef(TypedDict):
    Targets: List[str]
    TargetTypes: List[TargetType]
    GeneratedRulesType: GeneratedRulesType


class RulesSourceTypeDef(TypedDict, total=False):
    RulesString: str
    RulesSourceList: "RulesSourceListTypeDef"
    StatefulRules: List["StatefulRuleTypeDef"]
    StatelessRulesAndCustomActions: "StatelessRulesAndCustomActionsTypeDef"


class StatefulRuleGroupReferenceTypeDef(TypedDict):
    ResourceArn: str


class StatefulRuleTypeDef(TypedDict):
    Action: StatefulAction
    Header: "HeaderTypeDef"
    RuleOptions: List["RuleOptionTypeDef"]


class StatelessRuleGroupReferenceTypeDef(TypedDict):
    ResourceArn: str
    Priority: int


class StatelessRuleTypeDef(TypedDict):
    RuleDefinition: "RuleDefinitionTypeDef"
    Priority: int


class _RequiredStatelessRulesAndCustomActionsTypeDef(TypedDict):
    StatelessRules: List["StatelessRuleTypeDef"]


class StatelessRulesAndCustomActionsTypeDef(
    _RequiredStatelessRulesAndCustomActionsTypeDef, total=False
):
    CustomActions: List["CustomActionTypeDef"]


class SubnetMappingTypeDef(TypedDict):
    SubnetId: str


class SyncStateTypeDef(TypedDict, total=False):
    Attachment: "AttachmentTypeDef"
    Config: Dict[str, "PerObjectStatusTypeDef"]


class _RequiredTCPFlagFieldTypeDef(TypedDict):
    Flags: List[TCPFlag]


class TCPFlagFieldTypeDef(_RequiredTCPFlagFieldTypeDef, total=False):
    Masks: List[TCPFlag]


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class UpdateFirewallDeleteProtectionResponseTypeDef(TypedDict, total=False):
    FirewallArn: str
    FirewallName: str
    DeleteProtection: bool
    UpdateToken: str


class UpdateFirewallDescriptionResponseTypeDef(TypedDict, total=False):
    FirewallArn: str
    FirewallName: str
    Description: str
    UpdateToken: str


class UpdateFirewallPolicyChangeProtectionResponseTypeDef(TypedDict, total=False):
    UpdateToken: str
    FirewallArn: str
    FirewallName: str
    FirewallPolicyChangeProtection: bool


class UpdateFirewallPolicyResponseTypeDef(TypedDict):
    UpdateToken: str
    FirewallPolicyResponse: "FirewallPolicyResponseTypeDef"


class UpdateLoggingConfigurationResponseTypeDef(TypedDict, total=False):
    FirewallArn: str
    FirewallName: str
    LoggingConfiguration: "LoggingConfigurationTypeDef"


class UpdateRuleGroupResponseTypeDef(TypedDict):
    UpdateToken: str
    RuleGroupResponse: "RuleGroupResponseTypeDef"


class UpdateSubnetChangeProtectionResponseTypeDef(TypedDict, total=False):
    UpdateToken: str
    FirewallArn: str
    FirewallName: str
    SubnetChangeProtection: bool
