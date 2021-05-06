"""
Type annotations for networkmanager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_networkmanager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_networkmanager.type_defs import AWSLocationTypeDef

    data: AWSLocationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_networkmanager.literals import (
    ConnectionState,
    CustomerGatewayAssociationState,
    DeviceState,
    GlobalNetworkState,
    LinkAssociationState,
    LinkState,
    SiteState,
    TransitGatewayConnectPeerAssociationState,
    TransitGatewayRegistrationState,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AWSLocationTypeDef",
    "AssociateCustomerGatewayResponseTypeDef",
    "AssociateLinkResponseTypeDef",
    "AssociateTransitGatewayConnectPeerResponseTypeDef",
    "BandwidthTypeDef",
    "ConnectionTypeDef",
    "CreateConnectionResponseTypeDef",
    "CreateDeviceResponseTypeDef",
    "CreateGlobalNetworkResponseTypeDef",
    "CreateLinkResponseTypeDef",
    "CreateSiteResponseTypeDef",
    "CustomerGatewayAssociationTypeDef",
    "DeleteConnectionResponseTypeDef",
    "DeleteDeviceResponseTypeDef",
    "DeleteGlobalNetworkResponseTypeDef",
    "DeleteLinkResponseTypeDef",
    "DeleteSiteResponseTypeDef",
    "DeregisterTransitGatewayResponseTypeDef",
    "DescribeGlobalNetworksResponseTypeDef",
    "DeviceTypeDef",
    "DisassociateCustomerGatewayResponseTypeDef",
    "DisassociateLinkResponseTypeDef",
    "DisassociateTransitGatewayConnectPeerResponseTypeDef",
    "GetConnectionsResponseTypeDef",
    "GetCustomerGatewayAssociationsResponseTypeDef",
    "GetDevicesResponseTypeDef",
    "GetLinkAssociationsResponseTypeDef",
    "GetLinksResponseTypeDef",
    "GetSitesResponseTypeDef",
    "GetTransitGatewayConnectPeerAssociationsResponseTypeDef",
    "GetTransitGatewayRegistrationsResponseTypeDef",
    "GlobalNetworkTypeDef",
    "LinkAssociationTypeDef",
    "LinkTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterTransitGatewayResponseTypeDef",
    "SiteTypeDef",
    "TagTypeDef",
    "TransitGatewayConnectPeerAssociationTypeDef",
    "TransitGatewayRegistrationStateReasonTypeDef",
    "TransitGatewayRegistrationTypeDef",
    "UpdateConnectionResponseTypeDef",
    "UpdateDeviceResponseTypeDef",
    "UpdateGlobalNetworkResponseTypeDef",
    "UpdateLinkResponseTypeDef",
    "UpdateSiteResponseTypeDef",
)


class AWSLocationTypeDef(TypedDict, total=False):
    Zone: str
    SubnetArn: str


class AssociateCustomerGatewayResponseTypeDef(TypedDict, total=False):
    CustomerGatewayAssociation: "CustomerGatewayAssociationTypeDef"


class AssociateLinkResponseTypeDef(TypedDict, total=False):
    LinkAssociation: "LinkAssociationTypeDef"


class AssociateTransitGatewayConnectPeerResponseTypeDef(TypedDict, total=False):
    TransitGatewayConnectPeerAssociation: "TransitGatewayConnectPeerAssociationTypeDef"


class BandwidthTypeDef(TypedDict, total=False):
    UploadSpeed: int
    DownloadSpeed: int


class ConnectionTypeDef(TypedDict, total=False):
    ConnectionId: str
    ConnectionArn: str
    GlobalNetworkId: str
    DeviceId: str
    ConnectedDeviceId: str
    LinkId: str
    ConnectedLinkId: str
    Description: str
    CreatedAt: datetime
    State: ConnectionState
    Tags: List["TagTypeDef"]


class CreateConnectionResponseTypeDef(TypedDict, total=False):
    Connection: "ConnectionTypeDef"


class CreateDeviceResponseTypeDef(TypedDict, total=False):
    Device: "DeviceTypeDef"


class CreateGlobalNetworkResponseTypeDef(TypedDict, total=False):
    GlobalNetwork: "GlobalNetworkTypeDef"


class CreateLinkResponseTypeDef(TypedDict, total=False):
    Link: "LinkTypeDef"


class CreateSiteResponseTypeDef(TypedDict, total=False):
    Site: "SiteTypeDef"


class CustomerGatewayAssociationTypeDef(TypedDict, total=False):
    CustomerGatewayArn: str
    GlobalNetworkId: str
    DeviceId: str
    LinkId: str
    State: CustomerGatewayAssociationState


class DeleteConnectionResponseTypeDef(TypedDict, total=False):
    Connection: "ConnectionTypeDef"


class DeleteDeviceResponseTypeDef(TypedDict, total=False):
    Device: "DeviceTypeDef"


class DeleteGlobalNetworkResponseTypeDef(TypedDict, total=False):
    GlobalNetwork: "GlobalNetworkTypeDef"


class DeleteLinkResponseTypeDef(TypedDict, total=False):
    Link: "LinkTypeDef"


class DeleteSiteResponseTypeDef(TypedDict, total=False):
    Site: "SiteTypeDef"


class DeregisterTransitGatewayResponseTypeDef(TypedDict, total=False):
    TransitGatewayRegistration: "TransitGatewayRegistrationTypeDef"


class DescribeGlobalNetworksResponseTypeDef(TypedDict, total=False):
    GlobalNetworks: List["GlobalNetworkTypeDef"]
    NextToken: str


DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "DeviceId": str,
        "DeviceArn": str,
        "GlobalNetworkId": str,
        "AWSLocation": "AWSLocationTypeDef",
        "Description": str,
        "Type": str,
        "Vendor": str,
        "Model": str,
        "SerialNumber": str,
        "Location": "LocationTypeDef",
        "SiteId": str,
        "CreatedAt": datetime,
        "State": DeviceState,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class DisassociateCustomerGatewayResponseTypeDef(TypedDict, total=False):
    CustomerGatewayAssociation: "CustomerGatewayAssociationTypeDef"


class DisassociateLinkResponseTypeDef(TypedDict, total=False):
    LinkAssociation: "LinkAssociationTypeDef"


class DisassociateTransitGatewayConnectPeerResponseTypeDef(TypedDict, total=False):
    TransitGatewayConnectPeerAssociation: "TransitGatewayConnectPeerAssociationTypeDef"


class GetConnectionsResponseTypeDef(TypedDict, total=False):
    Connections: List["ConnectionTypeDef"]
    NextToken: str


class GetCustomerGatewayAssociationsResponseTypeDef(TypedDict, total=False):
    CustomerGatewayAssociations: List["CustomerGatewayAssociationTypeDef"]
    NextToken: str


class GetDevicesResponseTypeDef(TypedDict, total=False):
    Devices: List["DeviceTypeDef"]
    NextToken: str


class GetLinkAssociationsResponseTypeDef(TypedDict, total=False):
    LinkAssociations: List["LinkAssociationTypeDef"]
    NextToken: str


class GetLinksResponseTypeDef(TypedDict, total=False):
    Links: List["LinkTypeDef"]
    NextToken: str


class GetSitesResponseTypeDef(TypedDict, total=False):
    Sites: List["SiteTypeDef"]
    NextToken: str


class GetTransitGatewayConnectPeerAssociationsResponseTypeDef(TypedDict, total=False):
    TransitGatewayConnectPeerAssociations: List["TransitGatewayConnectPeerAssociationTypeDef"]
    NextToken: str


class GetTransitGatewayRegistrationsResponseTypeDef(TypedDict, total=False):
    TransitGatewayRegistrations: List["TransitGatewayRegistrationTypeDef"]
    NextToken: str


class GlobalNetworkTypeDef(TypedDict, total=False):
    GlobalNetworkId: str
    GlobalNetworkArn: str
    Description: str
    CreatedAt: datetime
    State: GlobalNetworkState
    Tags: List["TagTypeDef"]


class LinkAssociationTypeDef(TypedDict, total=False):
    GlobalNetworkId: str
    DeviceId: str
    LinkId: str
    LinkAssociationState: LinkAssociationState


LinkTypeDef = TypedDict(
    "LinkTypeDef",
    {
        "LinkId": str,
        "LinkArn": str,
        "GlobalNetworkId": str,
        "SiteId": str,
        "Description": str,
        "Type": str,
        "Bandwidth": "BandwidthTypeDef",
        "Provider": str,
        "CreatedAt": datetime,
        "State": LinkState,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    TagList: List["TagTypeDef"]


class LocationTypeDef(TypedDict, total=False):
    Address: str
    Latitude: str
    Longitude: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RegisterTransitGatewayResponseTypeDef(TypedDict, total=False):
    TransitGatewayRegistration: "TransitGatewayRegistrationTypeDef"


class SiteTypeDef(TypedDict, total=False):
    SiteId: str
    SiteArn: str
    GlobalNetworkId: str
    Description: str
    Location: "LocationTypeDef"
    CreatedAt: datetime
    State: SiteState
    Tags: List["TagTypeDef"]


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class TransitGatewayConnectPeerAssociationTypeDef(TypedDict, total=False):
    TransitGatewayConnectPeerArn: str
    GlobalNetworkId: str
    DeviceId: str
    LinkId: str
    State: TransitGatewayConnectPeerAssociationState


class TransitGatewayRegistrationStateReasonTypeDef(TypedDict, total=False):
    Code: TransitGatewayRegistrationState
    Message: str


class TransitGatewayRegistrationTypeDef(TypedDict, total=False):
    GlobalNetworkId: str
    TransitGatewayArn: str
    State: "TransitGatewayRegistrationStateReasonTypeDef"


class UpdateConnectionResponseTypeDef(TypedDict, total=False):
    Connection: "ConnectionTypeDef"


class UpdateDeviceResponseTypeDef(TypedDict, total=False):
    Device: "DeviceTypeDef"


class UpdateGlobalNetworkResponseTypeDef(TypedDict, total=False):
    GlobalNetwork: "GlobalNetworkTypeDef"


class UpdateLinkResponseTypeDef(TypedDict, total=False):
    Link: "LinkTypeDef"


class UpdateSiteResponseTypeDef(TypedDict, total=False):
    Site: "SiteTypeDef"
