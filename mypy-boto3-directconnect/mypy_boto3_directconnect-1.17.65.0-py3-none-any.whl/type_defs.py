"""
Type annotations for directconnect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_directconnect.type_defs import AcceptDirectConnectGatewayAssociationProposalResultTypeDef

    data: AcceptDirectConnectGatewayAssociationProposalResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, List, Union

from mypy_boto3_directconnect.literals import (
    AddressFamily,
    BGPPeerState,
    BGPStatus,
    ConnectionState,
    DirectConnectGatewayAssociationProposalState,
    DirectConnectGatewayAssociationState,
    DirectConnectGatewayAttachmentState,
    DirectConnectGatewayAttachmentType,
    DirectConnectGatewayState,
    GatewayType,
    HasLogicalRedundancy,
    InterconnectState,
    LagState,
    VirtualInterfaceState,
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
    "AcceptDirectConnectGatewayAssociationProposalResultTypeDef",
    "AllocateTransitVirtualInterfaceResultTypeDef",
    "AssociateMacSecKeyResponseTypeDef",
    "AssociatedGatewayTypeDef",
    "BGPPeerTypeDef",
    "ConfirmConnectionResponseTypeDef",
    "ConfirmPrivateVirtualInterfaceResponseTypeDef",
    "ConfirmPublicVirtualInterfaceResponseTypeDef",
    "ConfirmTransitVirtualInterfaceResponseTypeDef",
    "ConnectionTypeDef",
    "ConnectionsTypeDef",
    "CreateBGPPeerResponseTypeDef",
    "CreateDirectConnectGatewayAssociationProposalResultTypeDef",
    "CreateDirectConnectGatewayAssociationResultTypeDef",
    "CreateDirectConnectGatewayResultTypeDef",
    "CreateTransitVirtualInterfaceResultTypeDef",
    "DeleteBGPPeerResponseTypeDef",
    "DeleteDirectConnectGatewayAssociationProposalResultTypeDef",
    "DeleteDirectConnectGatewayAssociationResultTypeDef",
    "DeleteDirectConnectGatewayResultTypeDef",
    "DeleteInterconnectResponseTypeDef",
    "DeleteVirtualInterfaceResponseTypeDef",
    "DescribeConnectionLoaResponseTypeDef",
    "DescribeDirectConnectGatewayAssociationProposalsResultTypeDef",
    "DescribeDirectConnectGatewayAssociationsResultTypeDef",
    "DescribeDirectConnectGatewayAttachmentsResultTypeDef",
    "DescribeDirectConnectGatewaysResultTypeDef",
    "DescribeInterconnectLoaResponseTypeDef",
    "DescribeTagsResponseTypeDef",
    "DirectConnectGatewayAssociationProposalTypeDef",
    "DirectConnectGatewayAssociationTypeDef",
    "DirectConnectGatewayAttachmentTypeDef",
    "DirectConnectGatewayTypeDef",
    "DisassociateMacSecKeyResponseTypeDef",
    "InterconnectTypeDef",
    "InterconnectsTypeDef",
    "LagTypeDef",
    "LagsTypeDef",
    "ListVirtualInterfaceTestHistoryResponseTypeDef",
    "LoaTypeDef",
    "LocationTypeDef",
    "LocationsTypeDef",
    "MacSecKeyTypeDef",
    "NewBGPPeerTypeDef",
    "NewPrivateVirtualInterfaceAllocationTypeDef",
    "NewPrivateVirtualInterfaceTypeDef",
    "NewPublicVirtualInterfaceAllocationTypeDef",
    "NewPublicVirtualInterfaceTypeDef",
    "NewTransitVirtualInterfaceAllocationTypeDef",
    "NewTransitVirtualInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceTagTypeDef",
    "RouteFilterPrefixTypeDef",
    "StartBgpFailoverTestResponseTypeDef",
    "StopBgpFailoverTestResponseTypeDef",
    "TagTypeDef",
    "UpdateDirectConnectGatewayAssociationResultTypeDef",
    "VirtualGatewayTypeDef",
    "VirtualGatewaysTypeDef",
    "VirtualInterfaceTestHistoryTypeDef",
    "VirtualInterfaceTypeDef",
    "VirtualInterfacesTypeDef",
)


class AcceptDirectConnectGatewayAssociationProposalResultTypeDef(TypedDict, total=False):
    directConnectGatewayAssociation: "DirectConnectGatewayAssociationTypeDef"


class AllocateTransitVirtualInterfaceResultTypeDef(TypedDict, total=False):
    virtualInterface: "VirtualInterfaceTypeDef"


class AssociateMacSecKeyResponseTypeDef(TypedDict, total=False):
    connectionId: str
    macSecKeys: List["MacSecKeyTypeDef"]


AssociatedGatewayTypeDef = TypedDict(
    "AssociatedGatewayTypeDef",
    {"id": str, "type": GatewayType, "ownerAccount": str, "region": str},
    total=False,
)


class BGPPeerTypeDef(TypedDict, total=False):
    bgpPeerId: str
    asn: int
    authKey: str
    addressFamily: AddressFamily
    amazonAddress: str
    customerAddress: str
    bgpPeerState: BGPPeerState
    bgpStatus: BGPStatus
    awsDeviceV2: str


class ConfirmConnectionResponseTypeDef(TypedDict, total=False):
    connectionState: ConnectionState


class ConfirmPrivateVirtualInterfaceResponseTypeDef(TypedDict, total=False):
    virtualInterfaceState: VirtualInterfaceState


class ConfirmPublicVirtualInterfaceResponseTypeDef(TypedDict, total=False):
    virtualInterfaceState: VirtualInterfaceState


class ConfirmTransitVirtualInterfaceResponseTypeDef(TypedDict, total=False):
    virtualInterfaceState: VirtualInterfaceState


class ConnectionTypeDef(TypedDict, total=False):
    ownerAccount: str
    connectionId: str
    connectionName: str
    connectionState: ConnectionState
    region: str
    location: str
    bandwidth: str
    vlan: int
    partnerName: str
    loaIssueTime: datetime
    lagId: str
    awsDevice: str
    jumboFrameCapable: bool
    awsDeviceV2: str
    hasLogicalRedundancy: HasLogicalRedundancy
    tags: List["TagTypeDef"]
    providerName: str
    macSecCapable: bool
    portEncryptionStatus: str
    encryptionMode: str
    macSecKeys: List["MacSecKeyTypeDef"]


class ConnectionsTypeDef(TypedDict, total=False):
    connections: List["ConnectionTypeDef"]


class CreateBGPPeerResponseTypeDef(TypedDict, total=False):
    virtualInterface: "VirtualInterfaceTypeDef"


class CreateDirectConnectGatewayAssociationProposalResultTypeDef(TypedDict, total=False):
    directConnectGatewayAssociationProposal: "DirectConnectGatewayAssociationProposalTypeDef"


class CreateDirectConnectGatewayAssociationResultTypeDef(TypedDict, total=False):
    directConnectGatewayAssociation: "DirectConnectGatewayAssociationTypeDef"


class CreateDirectConnectGatewayResultTypeDef(TypedDict, total=False):
    directConnectGateway: "DirectConnectGatewayTypeDef"


class CreateTransitVirtualInterfaceResultTypeDef(TypedDict, total=False):
    virtualInterface: "VirtualInterfaceTypeDef"


class DeleteBGPPeerResponseTypeDef(TypedDict, total=False):
    virtualInterface: "VirtualInterfaceTypeDef"


class DeleteDirectConnectGatewayAssociationProposalResultTypeDef(TypedDict, total=False):
    directConnectGatewayAssociationProposal: "DirectConnectGatewayAssociationProposalTypeDef"


class DeleteDirectConnectGatewayAssociationResultTypeDef(TypedDict, total=False):
    directConnectGatewayAssociation: "DirectConnectGatewayAssociationTypeDef"


class DeleteDirectConnectGatewayResultTypeDef(TypedDict, total=False):
    directConnectGateway: "DirectConnectGatewayTypeDef"


class DeleteInterconnectResponseTypeDef(TypedDict, total=False):
    interconnectState: InterconnectState


class DeleteVirtualInterfaceResponseTypeDef(TypedDict, total=False):
    virtualInterfaceState: VirtualInterfaceState


class DescribeConnectionLoaResponseTypeDef(TypedDict, total=False):
    loa: "LoaTypeDef"


class DescribeDirectConnectGatewayAssociationProposalsResultTypeDef(TypedDict, total=False):
    directConnectGatewayAssociationProposals: List["DirectConnectGatewayAssociationProposalTypeDef"]
    nextToken: str


class DescribeDirectConnectGatewayAssociationsResultTypeDef(TypedDict, total=False):
    directConnectGatewayAssociations: List["DirectConnectGatewayAssociationTypeDef"]
    nextToken: str


class DescribeDirectConnectGatewayAttachmentsResultTypeDef(TypedDict, total=False):
    directConnectGatewayAttachments: List["DirectConnectGatewayAttachmentTypeDef"]
    nextToken: str


class DescribeDirectConnectGatewaysResultTypeDef(TypedDict, total=False):
    directConnectGateways: List["DirectConnectGatewayTypeDef"]
    nextToken: str


class DescribeInterconnectLoaResponseTypeDef(TypedDict, total=False):
    loa: "LoaTypeDef"


class DescribeTagsResponseTypeDef(TypedDict, total=False):
    resourceTags: List["ResourceTagTypeDef"]


class DirectConnectGatewayAssociationProposalTypeDef(TypedDict, total=False):
    proposalId: str
    directConnectGatewayId: str
    directConnectGatewayOwnerAccount: str
    proposalState: DirectConnectGatewayAssociationProposalState
    associatedGateway: "AssociatedGatewayTypeDef"
    existingAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"]
    requestedAllowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"]


class DirectConnectGatewayAssociationTypeDef(TypedDict, total=False):
    directConnectGatewayId: str
    directConnectGatewayOwnerAccount: str
    associationState: DirectConnectGatewayAssociationState
    stateChangeError: str
    associatedGateway: "AssociatedGatewayTypeDef"
    associationId: str
    allowedPrefixesToDirectConnectGateway: List["RouteFilterPrefixTypeDef"]
    virtualGatewayId: str
    virtualGatewayRegion: str
    virtualGatewayOwnerAccount: str


class DirectConnectGatewayAttachmentTypeDef(TypedDict, total=False):
    directConnectGatewayId: str
    virtualInterfaceId: str
    virtualInterfaceRegion: str
    virtualInterfaceOwnerAccount: str
    attachmentState: DirectConnectGatewayAttachmentState
    attachmentType: DirectConnectGatewayAttachmentType
    stateChangeError: str


class DirectConnectGatewayTypeDef(TypedDict, total=False):
    directConnectGatewayId: str
    directConnectGatewayName: str
    amazonSideAsn: int
    ownerAccount: str
    directConnectGatewayState: DirectConnectGatewayState
    stateChangeError: str


class DisassociateMacSecKeyResponseTypeDef(TypedDict, total=False):
    connectionId: str
    macSecKeys: List["MacSecKeyTypeDef"]


class InterconnectTypeDef(TypedDict, total=False):
    interconnectId: str
    interconnectName: str
    interconnectState: InterconnectState
    region: str
    location: str
    bandwidth: str
    loaIssueTime: datetime
    lagId: str
    awsDevice: str
    jumboFrameCapable: bool
    awsDeviceV2: str
    hasLogicalRedundancy: HasLogicalRedundancy
    tags: List["TagTypeDef"]
    providerName: str


class InterconnectsTypeDef(TypedDict, total=False):
    interconnects: List["InterconnectTypeDef"]


class LagTypeDef(TypedDict, total=False):
    connectionsBandwidth: str
    numberOfConnections: int
    lagId: str
    ownerAccount: str
    lagName: str
    lagState: LagState
    location: str
    region: str
    minimumLinks: int
    awsDevice: str
    awsDeviceV2: str
    connections: List["ConnectionTypeDef"]
    allowsHostedConnections: bool
    jumboFrameCapable: bool
    hasLogicalRedundancy: HasLogicalRedundancy
    tags: List["TagTypeDef"]
    providerName: str
    macSecCapable: bool
    encryptionMode: str
    macSecKeys: List["MacSecKeyTypeDef"]


class LagsTypeDef(TypedDict, total=False):
    lags: List["LagTypeDef"]


class ListVirtualInterfaceTestHistoryResponseTypeDef(TypedDict, total=False):
    virtualInterfaceTestHistory: List["VirtualInterfaceTestHistoryTypeDef"]
    nextToken: str


class LoaTypeDef(TypedDict, total=False):
    loaContent: Union[bytes, IO[bytes]]
    loaContentType: Literal["application/pdf"]


class LocationTypeDef(TypedDict, total=False):
    locationCode: str
    locationName: str
    region: str
    availablePortSpeeds: List[str]
    availableProviders: List[str]
    availableMacSecPortSpeeds: List[str]


class LocationsTypeDef(TypedDict, total=False):
    locations: List["LocationTypeDef"]


class MacSecKeyTypeDef(TypedDict, total=False):
    secretARN: str
    ckn: str
    state: str
    startOn: str


class NewBGPPeerTypeDef(TypedDict, total=False):
    asn: int
    authKey: str
    addressFamily: AddressFamily
    amazonAddress: str
    customerAddress: str


class _RequiredNewPrivateVirtualInterfaceAllocationTypeDef(TypedDict):
    virtualInterfaceName: str
    vlan: int
    asn: int


class NewPrivateVirtualInterfaceAllocationTypeDef(
    _RequiredNewPrivateVirtualInterfaceAllocationTypeDef, total=False
):
    mtu: int
    authKey: str
    amazonAddress: str
    addressFamily: AddressFamily
    customerAddress: str
    tags: List["TagTypeDef"]


class _RequiredNewPrivateVirtualInterfaceTypeDef(TypedDict):
    virtualInterfaceName: str
    vlan: int
    asn: int


class NewPrivateVirtualInterfaceTypeDef(_RequiredNewPrivateVirtualInterfaceTypeDef, total=False):
    mtu: int
    authKey: str
    amazonAddress: str
    customerAddress: str
    addressFamily: AddressFamily
    virtualGatewayId: str
    directConnectGatewayId: str
    tags: List["TagTypeDef"]


class _RequiredNewPublicVirtualInterfaceAllocationTypeDef(TypedDict):
    virtualInterfaceName: str
    vlan: int
    asn: int


class NewPublicVirtualInterfaceAllocationTypeDef(
    _RequiredNewPublicVirtualInterfaceAllocationTypeDef, total=False
):
    authKey: str
    amazonAddress: str
    customerAddress: str
    addressFamily: AddressFamily
    routeFilterPrefixes: List["RouteFilterPrefixTypeDef"]
    tags: List["TagTypeDef"]


class _RequiredNewPublicVirtualInterfaceTypeDef(TypedDict):
    virtualInterfaceName: str
    vlan: int
    asn: int


class NewPublicVirtualInterfaceTypeDef(_RequiredNewPublicVirtualInterfaceTypeDef, total=False):
    authKey: str
    amazonAddress: str
    customerAddress: str
    addressFamily: AddressFamily
    routeFilterPrefixes: List["RouteFilterPrefixTypeDef"]
    tags: List["TagTypeDef"]


class NewTransitVirtualInterfaceAllocationTypeDef(TypedDict, total=False):
    virtualInterfaceName: str
    vlan: int
    asn: int
    mtu: int
    authKey: str
    amazonAddress: str
    customerAddress: str
    addressFamily: AddressFamily
    tags: List["TagTypeDef"]


class NewTransitVirtualInterfaceTypeDef(TypedDict, total=False):
    virtualInterfaceName: str
    vlan: int
    asn: int
    mtu: int
    authKey: str
    amazonAddress: str
    customerAddress: str
    addressFamily: AddressFamily
    directConnectGatewayId: str
    tags: List["TagTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ResourceTagTypeDef(TypedDict, total=False):
    resourceArn: str
    tags: List["TagTypeDef"]


class RouteFilterPrefixTypeDef(TypedDict, total=False):
    cidr: str


class StartBgpFailoverTestResponseTypeDef(TypedDict, total=False):
    virtualInterfaceTest: "VirtualInterfaceTestHistoryTypeDef"


class StopBgpFailoverTestResponseTypeDef(TypedDict, total=False):
    virtualInterfaceTest: "VirtualInterfaceTestHistoryTypeDef"


class _RequiredTagTypeDef(TypedDict):
    key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    value: str


class UpdateDirectConnectGatewayAssociationResultTypeDef(TypedDict, total=False):
    directConnectGatewayAssociation: "DirectConnectGatewayAssociationTypeDef"


class VirtualGatewayTypeDef(TypedDict, total=False):
    virtualGatewayId: str
    virtualGatewayState: str


class VirtualGatewaysTypeDef(TypedDict, total=False):
    virtualGateways: List["VirtualGatewayTypeDef"]


class VirtualInterfaceTestHistoryTypeDef(TypedDict, total=False):
    testId: str
    virtualInterfaceId: str
    bgpPeers: List[str]
    status: str
    ownerAccount: str
    testDurationInMinutes: int
    startTime: datetime
    endTime: datetime


class VirtualInterfaceTypeDef(TypedDict, total=False):
    ownerAccount: str
    virtualInterfaceId: str
    location: str
    connectionId: str
    virtualInterfaceType: str
    virtualInterfaceName: str
    vlan: int
    asn: int
    amazonSideAsn: int
    authKey: str
    amazonAddress: str
    customerAddress: str
    addressFamily: AddressFamily
    virtualInterfaceState: VirtualInterfaceState
    customerRouterConfig: str
    mtu: int
    jumboFrameCapable: bool
    virtualGatewayId: str
    directConnectGatewayId: str
    routeFilterPrefixes: List["RouteFilterPrefixTypeDef"]
    bgpPeers: List["BGPPeerTypeDef"]
    region: str
    awsDeviceV2: str
    tags: List["TagTypeDef"]


class VirtualInterfacesTypeDef(TypedDict, total=False):
    virtualInterfaces: List["VirtualInterfaceTypeDef"]
