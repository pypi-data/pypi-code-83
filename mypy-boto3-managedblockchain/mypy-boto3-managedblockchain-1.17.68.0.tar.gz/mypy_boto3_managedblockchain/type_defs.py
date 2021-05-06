"""
Type annotations for managedblockchain service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_managedblockchain/type_defs.html)

Usage::

    ```python
    from mypy_boto3_managedblockchain.type_defs import ApprovalThresholdPolicyTypeDef

    data: ApprovalThresholdPolicyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_managedblockchain.literals import (
    Edition,
    Framework,
    InvitationStatus,
    MemberStatus,
    NetworkStatus,
    NodeStatus,
    ProposalStatus,
    StateDBType,
    ThresholdComparator,
    VoteValue,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApprovalThresholdPolicyTypeDef",
    "CreateMemberOutputTypeDef",
    "CreateNetworkOutputTypeDef",
    "CreateNodeOutputTypeDef",
    "CreateProposalOutputTypeDef",
    "GetMemberOutputTypeDef",
    "GetNetworkOutputTypeDef",
    "GetNodeOutputTypeDef",
    "GetProposalOutputTypeDef",
    "InvitationTypeDef",
    "InviteActionTypeDef",
    "ListInvitationsOutputTypeDef",
    "ListMembersOutputTypeDef",
    "ListNetworksOutputTypeDef",
    "ListNodesOutputTypeDef",
    "ListProposalVotesOutputTypeDef",
    "ListProposalsOutputTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogConfigurationTypeDef",
    "LogConfigurationsTypeDef",
    "MemberConfigurationTypeDef",
    "MemberFabricAttributesTypeDef",
    "MemberFabricConfigurationTypeDef",
    "MemberFabricLogPublishingConfigurationTypeDef",
    "MemberFrameworkAttributesTypeDef",
    "MemberFrameworkConfigurationTypeDef",
    "MemberLogPublishingConfigurationTypeDef",
    "MemberSummaryTypeDef",
    "MemberTypeDef",
    "NetworkEthereumAttributesTypeDef",
    "NetworkFabricAttributesTypeDef",
    "NetworkFabricConfigurationTypeDef",
    "NetworkFrameworkAttributesTypeDef",
    "NetworkFrameworkConfigurationTypeDef",
    "NetworkSummaryTypeDef",
    "NetworkTypeDef",
    "NodeConfigurationTypeDef",
    "NodeEthereumAttributesTypeDef",
    "NodeFabricAttributesTypeDef",
    "NodeFabricLogPublishingConfigurationTypeDef",
    "NodeFrameworkAttributesTypeDef",
    "NodeLogPublishingConfigurationTypeDef",
    "NodeSummaryTypeDef",
    "NodeTypeDef",
    "ProposalActionsTypeDef",
    "ProposalSummaryTypeDef",
    "ProposalTypeDef",
    "RemoveActionTypeDef",
    "ResponseMetadata",
    "VoteSummaryTypeDef",
    "VotingPolicyTypeDef",
)


class ApprovalThresholdPolicyTypeDef(TypedDict, total=False):
    ThresholdPercentage: int
    ProposalDurationInHours: int
    ThresholdComparator: ThresholdComparator


class CreateMemberOutputTypeDef(TypedDict):
    MemberId: str
    ResponseMetadata: "ResponseMetadata"


class CreateNetworkOutputTypeDef(TypedDict):
    NetworkId: str
    MemberId: str
    ResponseMetadata: "ResponseMetadata"


class CreateNodeOutputTypeDef(TypedDict):
    NodeId: str
    ResponseMetadata: "ResponseMetadata"


class CreateProposalOutputTypeDef(TypedDict):
    ProposalId: str
    ResponseMetadata: "ResponseMetadata"


class GetMemberOutputTypeDef(TypedDict):
    Member: "MemberTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetNetworkOutputTypeDef(TypedDict):
    Network: "NetworkTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetNodeOutputTypeDef(TypedDict):
    Node: "NodeTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetProposalOutputTypeDef(TypedDict):
    Proposal: "ProposalTypeDef"
    ResponseMetadata: "ResponseMetadata"


class InvitationTypeDef(TypedDict, total=False):
    InvitationId: str
    CreationDate: datetime
    ExpirationDate: datetime
    Status: InvitationStatus
    NetworkSummary: "NetworkSummaryTypeDef"
    Arn: str


class InviteActionTypeDef(TypedDict):
    Principal: str


class ListInvitationsOutputTypeDef(TypedDict):
    Invitations: List["InvitationTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListMembersOutputTypeDef(TypedDict):
    Members: List["MemberSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListNetworksOutputTypeDef(TypedDict):
    Networks: List["NetworkSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListNodesOutputTypeDef(TypedDict):
    Nodes: List["NodeSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListProposalVotesOutputTypeDef(TypedDict):
    ProposalVotes: List["VoteSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListProposalsOutputTypeDef(TypedDict):
    Proposals: List["ProposalSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class LogConfigurationTypeDef(TypedDict, total=False):
    Enabled: bool


class LogConfigurationsTypeDef(TypedDict, total=False):
    Cloudwatch: "LogConfigurationTypeDef"


class _RequiredMemberConfigurationTypeDef(TypedDict):
    Name: str
    FrameworkConfiguration: "MemberFrameworkConfigurationTypeDef"


class MemberConfigurationTypeDef(_RequiredMemberConfigurationTypeDef, total=False):
    Description: str
    LogPublishingConfiguration: "MemberLogPublishingConfigurationTypeDef"
    Tags: Dict[str, str]


class MemberFabricAttributesTypeDef(TypedDict, total=False):
    AdminUsername: str
    CaEndpoint: str


class MemberFabricConfigurationTypeDef(TypedDict):
    AdminUsername: str
    AdminPassword: str


class MemberFabricLogPublishingConfigurationTypeDef(TypedDict, total=False):
    CaLogs: "LogConfigurationsTypeDef"


class MemberFrameworkAttributesTypeDef(TypedDict, total=False):
    Fabric: "MemberFabricAttributesTypeDef"


class MemberFrameworkConfigurationTypeDef(TypedDict, total=False):
    Fabric: "MemberFabricConfigurationTypeDef"


class MemberLogPublishingConfigurationTypeDef(TypedDict, total=False):
    Fabric: "MemberFabricLogPublishingConfigurationTypeDef"


class MemberSummaryTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Description: str
    Status: MemberStatus
    CreationDate: datetime
    IsOwned: bool
    Arn: str


class MemberTypeDef(TypedDict, total=False):
    NetworkId: str
    Id: str
    Name: str
    Description: str
    FrameworkAttributes: "MemberFrameworkAttributesTypeDef"
    LogPublishingConfiguration: "MemberLogPublishingConfigurationTypeDef"
    Status: MemberStatus
    CreationDate: datetime
    Tags: Dict[str, str]
    Arn: str


class NetworkEthereumAttributesTypeDef(TypedDict, total=False):
    ChainId: str


class NetworkFabricAttributesTypeDef(TypedDict, total=False):
    OrderingServiceEndpoint: str
    Edition: Edition


class NetworkFabricConfigurationTypeDef(TypedDict):
    Edition: Edition


class NetworkFrameworkAttributesTypeDef(TypedDict, total=False):
    Fabric: "NetworkFabricAttributesTypeDef"
    Ethereum: "NetworkEthereumAttributesTypeDef"


class NetworkFrameworkConfigurationTypeDef(TypedDict, total=False):
    Fabric: "NetworkFabricConfigurationTypeDef"


class NetworkSummaryTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Description: str
    Framework: Framework
    FrameworkVersion: str
    Status: NetworkStatus
    CreationDate: datetime
    Arn: str


class NetworkTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Description: str
    Framework: Framework
    FrameworkVersion: str
    FrameworkAttributes: "NetworkFrameworkAttributesTypeDef"
    VpcEndpointServiceName: str
    VotingPolicy: "VotingPolicyTypeDef"
    Status: NetworkStatus
    CreationDate: datetime
    Tags: Dict[str, str]
    Arn: str


class _RequiredNodeConfigurationTypeDef(TypedDict):
    InstanceType: str


class NodeConfigurationTypeDef(_RequiredNodeConfigurationTypeDef, total=False):
    AvailabilityZone: str
    LogPublishingConfiguration: "NodeLogPublishingConfigurationTypeDef"
    StateDB: StateDBType


class NodeEthereumAttributesTypeDef(TypedDict, total=False):
    HttpEndpoint: str
    WebSocketEndpoint: str


class NodeFabricAttributesTypeDef(TypedDict, total=False):
    PeerEndpoint: str
    PeerEventEndpoint: str


class NodeFabricLogPublishingConfigurationTypeDef(TypedDict, total=False):
    ChaincodeLogs: "LogConfigurationsTypeDef"
    PeerLogs: "LogConfigurationsTypeDef"


class NodeFrameworkAttributesTypeDef(TypedDict, total=False):
    Fabric: "NodeFabricAttributesTypeDef"
    Ethereum: "NodeEthereumAttributesTypeDef"


class NodeLogPublishingConfigurationTypeDef(TypedDict, total=False):
    Fabric: "NodeFabricLogPublishingConfigurationTypeDef"


class NodeSummaryTypeDef(TypedDict, total=False):
    Id: str
    Status: NodeStatus
    CreationDate: datetime
    AvailabilityZone: str
    InstanceType: str
    Arn: str


class NodeTypeDef(TypedDict, total=False):
    NetworkId: str
    MemberId: str
    Id: str
    InstanceType: str
    AvailabilityZone: str
    FrameworkAttributes: "NodeFrameworkAttributesTypeDef"
    LogPublishingConfiguration: "NodeLogPublishingConfigurationTypeDef"
    StateDB: StateDBType
    Status: NodeStatus
    CreationDate: datetime
    Tags: Dict[str, str]
    Arn: str


class ProposalActionsTypeDef(TypedDict, total=False):
    Invitations: List["InviteActionTypeDef"]
    Removals: List["RemoveActionTypeDef"]


class ProposalSummaryTypeDef(TypedDict, total=False):
    ProposalId: str
    Description: str
    ProposedByMemberId: str
    ProposedByMemberName: str
    Status: ProposalStatus
    CreationDate: datetime
    ExpirationDate: datetime
    Arn: str


class ProposalTypeDef(TypedDict, total=False):
    ProposalId: str
    NetworkId: str
    Description: str
    Actions: "ProposalActionsTypeDef"
    ProposedByMemberId: str
    ProposedByMemberName: str
    Status: ProposalStatus
    CreationDate: datetime
    ExpirationDate: datetime
    YesVoteCount: int
    NoVoteCount: int
    OutstandingVoteCount: int
    Tags: Dict[str, str]
    Arn: str


class RemoveActionTypeDef(TypedDict):
    MemberId: str


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class VoteSummaryTypeDef(TypedDict, total=False):
    Vote: VoteValue
    MemberName: str
    MemberId: str


class VotingPolicyTypeDef(TypedDict, total=False):
    ApprovalThresholdPolicy: "ApprovalThresholdPolicyTypeDef"
