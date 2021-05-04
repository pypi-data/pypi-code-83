"""
Type annotations for directconnect service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_directconnect/literals.html)

Usage::

    ```python
    from mypy_boto3_directconnect.literals import AddressFamily

    data: AddressFamily = "ipv4"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AddressFamily",
    "BGPPeerState",
    "BGPStatus",
    "ConnectionState",
    "DescribeDirectConnectGatewayAssociationsPaginatorName",
    "DescribeDirectConnectGatewayAttachmentsPaginatorName",
    "DescribeDirectConnectGatewaysPaginatorName",
    "DirectConnectGatewayAssociationProposalState",
    "DirectConnectGatewayAssociationState",
    "DirectConnectGatewayAttachmentState",
    "DirectConnectGatewayAttachmentType",
    "DirectConnectGatewayState",
    "GatewayType",
    "HasLogicalRedundancy",
    "InterconnectState",
    "LagState",
    "LoaContentType",
    "VirtualInterfaceState",
)


AddressFamily = Literal["ipv4", "ipv6"]
BGPPeerState = Literal["available", "deleted", "deleting", "pending", "verifying"]
BGPStatus = Literal["down", "unknown", "up"]
ConnectionState = Literal[
    "available",
    "deleted",
    "deleting",
    "down",
    "ordering",
    "pending",
    "rejected",
    "requested",
    "unknown",
]
DescribeDirectConnectGatewayAssociationsPaginatorName = Literal[
    "describe_direct_connect_gateway_associations"
]
DescribeDirectConnectGatewayAttachmentsPaginatorName = Literal[
    "describe_direct_connect_gateway_attachments"
]
DescribeDirectConnectGatewaysPaginatorName = Literal["describe_direct_connect_gateways"]
DirectConnectGatewayAssociationProposalState = Literal["accepted", "deleted", "requested"]
DirectConnectGatewayAssociationState = Literal[
    "associated", "associating", "disassociated", "disassociating", "updating"
]
DirectConnectGatewayAttachmentState = Literal["attached", "attaching", "detached", "detaching"]
DirectConnectGatewayAttachmentType = Literal["PrivateVirtualInterface", "TransitVirtualInterface"]
DirectConnectGatewayState = Literal["available", "deleted", "deleting", "pending"]
GatewayType = Literal["transitGateway", "virtualPrivateGateway"]
HasLogicalRedundancy = Literal["no", "unknown", "yes"]
InterconnectState = Literal[
    "available", "deleted", "deleting", "down", "pending", "requested", "unknown"
]
LagState = Literal["available", "deleted", "deleting", "down", "pending", "requested", "unknown"]
LoaContentType = Literal["application/pdf"]
VirtualInterfaceState = Literal[
    "available",
    "confirming",
    "deleted",
    "deleting",
    "down",
    "pending",
    "rejected",
    "unknown",
    "verifying",
]
