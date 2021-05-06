"""
Type annotations for networkmanager service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/literals.html)

Usage::

    ```python
    from mypy_boto3_networkmanager.literals import ConnectionState

    data: ConnectionState = "AVAILABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ConnectionState",
    "CustomerGatewayAssociationState",
    "DescribeGlobalNetworksPaginatorName",
    "DeviceState",
    "GetConnectionsPaginatorName",
    "GetCustomerGatewayAssociationsPaginatorName",
    "GetDevicesPaginatorName",
    "GetLinkAssociationsPaginatorName",
    "GetLinksPaginatorName",
    "GetSitesPaginatorName",
    "GetTransitGatewayConnectPeerAssociationsPaginatorName",
    "GetTransitGatewayRegistrationsPaginatorName",
    "GlobalNetworkState",
    "LinkAssociationState",
    "LinkState",
    "SiteState",
    "TransitGatewayConnectPeerAssociationState",
    "TransitGatewayRegistrationState",
)


ConnectionState = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
CustomerGatewayAssociationState = Literal["AVAILABLE", "DELETED", "DELETING", "PENDING"]
DescribeGlobalNetworksPaginatorName = Literal["describe_global_networks"]
DeviceState = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
GetConnectionsPaginatorName = Literal["get_connections"]
GetCustomerGatewayAssociationsPaginatorName = Literal["get_customer_gateway_associations"]
GetDevicesPaginatorName = Literal["get_devices"]
GetLinkAssociationsPaginatorName = Literal["get_link_associations"]
GetLinksPaginatorName = Literal["get_links"]
GetSitesPaginatorName = Literal["get_sites"]
GetTransitGatewayConnectPeerAssociationsPaginatorName = Literal[
    "get_transit_gateway_connect_peer_associations"
]
GetTransitGatewayRegistrationsPaginatorName = Literal["get_transit_gateway_registrations"]
GlobalNetworkState = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
LinkAssociationState = Literal["AVAILABLE", "DELETED", "DELETING", "PENDING"]
LinkState = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
SiteState = Literal["AVAILABLE", "DELETING", "PENDING", "UPDATING"]
TransitGatewayConnectPeerAssociationState = Literal["AVAILABLE", "DELETED", "DELETING", "PENDING"]
TransitGatewayRegistrationState = Literal["AVAILABLE", "DELETED", "DELETING", "FAILED", "PENDING"]
