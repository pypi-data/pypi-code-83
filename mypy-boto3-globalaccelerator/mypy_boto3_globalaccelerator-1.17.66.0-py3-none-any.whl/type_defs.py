"""
Type annotations for globalaccelerator service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_globalaccelerator/type_defs.html)

Usage::

    ```python
    from mypy_boto3_globalaccelerator.type_defs import AcceleratorAttributesTypeDef

    data: AcceleratorAttributesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_globalaccelerator.literals import (
    AcceleratorStatus,
    ByoipCidrState,
    ClientAffinity,
    CustomRoutingAcceleratorStatus,
    CustomRoutingDestinationTrafficState,
    CustomRoutingProtocol,
    HealthCheckProtocol,
    HealthState,
    ProtocolType,
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
    "AcceleratorAttributesTypeDef",
    "AcceleratorTypeDef",
    "AddCustomRoutingEndpointsResponseTypeDef",
    "AdvertiseByoipCidrResponseTypeDef",
    "ByoipCidrEventTypeDef",
    "ByoipCidrTypeDef",
    "CidrAuthorizationContextTypeDef",
    "CreateAcceleratorResponseTypeDef",
    "CreateCustomRoutingAcceleratorResponseTypeDef",
    "CreateCustomRoutingEndpointGroupResponseTypeDef",
    "CreateCustomRoutingListenerResponseTypeDef",
    "CreateEndpointGroupResponseTypeDef",
    "CreateListenerResponseTypeDef",
    "CustomRoutingAcceleratorAttributesTypeDef",
    "CustomRoutingAcceleratorTypeDef",
    "CustomRoutingDestinationConfigurationTypeDef",
    "CustomRoutingDestinationDescriptionTypeDef",
    "CustomRoutingEndpointConfigurationTypeDef",
    "CustomRoutingEndpointDescriptionTypeDef",
    "CustomRoutingEndpointGroupTypeDef",
    "CustomRoutingListenerTypeDef",
    "DeprovisionByoipCidrResponseTypeDef",
    "DescribeAcceleratorAttributesResponseTypeDef",
    "DescribeAcceleratorResponseTypeDef",
    "DescribeCustomRoutingAcceleratorAttributesResponseTypeDef",
    "DescribeCustomRoutingAcceleratorResponseTypeDef",
    "DescribeCustomRoutingEndpointGroupResponseTypeDef",
    "DescribeCustomRoutingListenerResponseTypeDef",
    "DescribeEndpointGroupResponseTypeDef",
    "DescribeListenerResponseTypeDef",
    "DestinationPortMappingTypeDef",
    "EndpointConfigurationTypeDef",
    "EndpointDescriptionTypeDef",
    "EndpointGroupTypeDef",
    "IpSetTypeDef",
    "ListAcceleratorsResponseTypeDef",
    "ListByoipCidrsResponseTypeDef",
    "ListCustomRoutingAcceleratorsResponseTypeDef",
    "ListCustomRoutingEndpointGroupsResponseTypeDef",
    "ListCustomRoutingListenersResponseTypeDef",
    "ListCustomRoutingPortMappingsByDestinationResponseTypeDef",
    "ListCustomRoutingPortMappingsResponseTypeDef",
    "ListEndpointGroupsResponseTypeDef",
    "ListListenersResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListenerTypeDef",
    "PaginatorConfigTypeDef",
    "PortMappingTypeDef",
    "PortOverrideTypeDef",
    "PortRangeTypeDef",
    "ProvisionByoipCidrResponseTypeDef",
    "SocketAddressTypeDef",
    "TagTypeDef",
    "UpdateAcceleratorAttributesResponseTypeDef",
    "UpdateAcceleratorResponseTypeDef",
    "UpdateCustomRoutingAcceleratorAttributesResponseTypeDef",
    "UpdateCustomRoutingAcceleratorResponseTypeDef",
    "UpdateCustomRoutingListenerResponseTypeDef",
    "UpdateEndpointGroupResponseTypeDef",
    "UpdateListenerResponseTypeDef",
    "WithdrawByoipCidrResponseTypeDef",
)


class AcceleratorAttributesTypeDef(TypedDict, total=False):
    FlowLogsEnabled: bool
    FlowLogsS3Bucket: str
    FlowLogsS3Prefix: str


class AcceleratorTypeDef(TypedDict, total=False):
    AcceleratorArn: str
    Name: str
    IpAddressType: Literal["IPV4"]
    Enabled: bool
    IpSets: List["IpSetTypeDef"]
    DnsName: str
    Status: AcceleratorStatus
    CreatedTime: datetime
    LastModifiedTime: datetime


class AddCustomRoutingEndpointsResponseTypeDef(TypedDict, total=False):
    EndpointDescriptions: List["CustomRoutingEndpointDescriptionTypeDef"]
    EndpointGroupArn: str


class AdvertiseByoipCidrResponseTypeDef(TypedDict, total=False):
    ByoipCidr: "ByoipCidrTypeDef"


class ByoipCidrEventTypeDef(TypedDict, total=False):
    Message: str
    Timestamp: datetime


class ByoipCidrTypeDef(TypedDict, total=False):
    Cidr: str
    State: ByoipCidrState
    Events: List["ByoipCidrEventTypeDef"]


class CidrAuthorizationContextTypeDef(TypedDict):
    Message: str
    Signature: str


class CreateAcceleratorResponseTypeDef(TypedDict, total=False):
    Accelerator: "AcceleratorTypeDef"


class CreateCustomRoutingAcceleratorResponseTypeDef(TypedDict, total=False):
    Accelerator: "CustomRoutingAcceleratorTypeDef"


class CreateCustomRoutingEndpointGroupResponseTypeDef(TypedDict, total=False):
    EndpointGroup: "CustomRoutingEndpointGroupTypeDef"


class CreateCustomRoutingListenerResponseTypeDef(TypedDict, total=False):
    Listener: "CustomRoutingListenerTypeDef"


class CreateEndpointGroupResponseTypeDef(TypedDict, total=False):
    EndpointGroup: "EndpointGroupTypeDef"


class CreateListenerResponseTypeDef(TypedDict, total=False):
    Listener: "ListenerTypeDef"


class CustomRoutingAcceleratorAttributesTypeDef(TypedDict, total=False):
    FlowLogsEnabled: bool
    FlowLogsS3Bucket: str
    FlowLogsS3Prefix: str


class CustomRoutingAcceleratorTypeDef(TypedDict, total=False):
    AcceleratorArn: str
    Name: str
    IpAddressType: Literal["IPV4"]
    Enabled: bool
    IpSets: List["IpSetTypeDef"]
    DnsName: str
    Status: CustomRoutingAcceleratorStatus
    CreatedTime: datetime
    LastModifiedTime: datetime


class CustomRoutingDestinationConfigurationTypeDef(TypedDict):
    FromPort: int
    ToPort: int
    Protocols: List[CustomRoutingProtocol]


class CustomRoutingDestinationDescriptionTypeDef(TypedDict, total=False):
    FromPort: int
    ToPort: int
    Protocols: List[ProtocolType]


class CustomRoutingEndpointConfigurationTypeDef(TypedDict, total=False):
    EndpointId: str


class CustomRoutingEndpointDescriptionTypeDef(TypedDict, total=False):
    EndpointId: str


class CustomRoutingEndpointGroupTypeDef(TypedDict, total=False):
    EndpointGroupArn: str
    EndpointGroupRegion: str
    DestinationDescriptions: List["CustomRoutingDestinationDescriptionTypeDef"]
    EndpointDescriptions: List["CustomRoutingEndpointDescriptionTypeDef"]


class CustomRoutingListenerTypeDef(TypedDict, total=False):
    ListenerArn: str
    PortRanges: List["PortRangeTypeDef"]


class DeprovisionByoipCidrResponseTypeDef(TypedDict, total=False):
    ByoipCidr: "ByoipCidrTypeDef"


class DescribeAcceleratorAttributesResponseTypeDef(TypedDict, total=False):
    AcceleratorAttributes: "AcceleratorAttributesTypeDef"


class DescribeAcceleratorResponseTypeDef(TypedDict, total=False):
    Accelerator: "AcceleratorTypeDef"


class DescribeCustomRoutingAcceleratorAttributesResponseTypeDef(TypedDict, total=False):
    AcceleratorAttributes: "CustomRoutingAcceleratorAttributesTypeDef"


class DescribeCustomRoutingAcceleratorResponseTypeDef(TypedDict, total=False):
    Accelerator: "CustomRoutingAcceleratorTypeDef"


class DescribeCustomRoutingEndpointGroupResponseTypeDef(TypedDict, total=False):
    EndpointGroup: "CustomRoutingEndpointGroupTypeDef"


class DescribeCustomRoutingListenerResponseTypeDef(TypedDict, total=False):
    Listener: "CustomRoutingListenerTypeDef"


class DescribeEndpointGroupResponseTypeDef(TypedDict, total=False):
    EndpointGroup: "EndpointGroupTypeDef"


class DescribeListenerResponseTypeDef(TypedDict, total=False):
    Listener: "ListenerTypeDef"


class DestinationPortMappingTypeDef(TypedDict, total=False):
    AcceleratorArn: str
    AcceleratorSocketAddresses: List["SocketAddressTypeDef"]
    EndpointGroupArn: str
    EndpointId: str
    EndpointGroupRegion: str
    DestinationSocketAddress: "SocketAddressTypeDef"
    IpAddressType: Literal["IPV4"]
    DestinationTrafficState: CustomRoutingDestinationTrafficState


class EndpointConfigurationTypeDef(TypedDict, total=False):
    EndpointId: str
    Weight: int
    ClientIPPreservationEnabled: bool


class EndpointDescriptionTypeDef(TypedDict, total=False):
    EndpointId: str
    Weight: int
    HealthState: HealthState
    HealthReason: str
    ClientIPPreservationEnabled: bool


class EndpointGroupTypeDef(TypedDict, total=False):
    EndpointGroupArn: str
    EndpointGroupRegion: str
    EndpointDescriptions: List["EndpointDescriptionTypeDef"]
    TrafficDialPercentage: float
    HealthCheckPort: int
    HealthCheckProtocol: HealthCheckProtocol
    HealthCheckPath: str
    HealthCheckIntervalSeconds: int
    ThresholdCount: int
    PortOverrides: List["PortOverrideTypeDef"]


class IpSetTypeDef(TypedDict, total=False):
    IpFamily: str
    IpAddresses: List[str]


class ListAcceleratorsResponseTypeDef(TypedDict, total=False):
    Accelerators: List["AcceleratorTypeDef"]
    NextToken: str


class ListByoipCidrsResponseTypeDef(TypedDict, total=False):
    ByoipCidrs: List["ByoipCidrTypeDef"]
    NextToken: str


class ListCustomRoutingAcceleratorsResponseTypeDef(TypedDict, total=False):
    Accelerators: List["CustomRoutingAcceleratorTypeDef"]
    NextToken: str


class ListCustomRoutingEndpointGroupsResponseTypeDef(TypedDict, total=False):
    EndpointGroups: List["CustomRoutingEndpointGroupTypeDef"]
    NextToken: str


class ListCustomRoutingListenersResponseTypeDef(TypedDict, total=False):
    Listeners: List["CustomRoutingListenerTypeDef"]
    NextToken: str


class ListCustomRoutingPortMappingsByDestinationResponseTypeDef(TypedDict, total=False):
    DestinationPortMappings: List["DestinationPortMappingTypeDef"]
    NextToken: str


class ListCustomRoutingPortMappingsResponseTypeDef(TypedDict, total=False):
    PortMappings: List["PortMappingTypeDef"]
    NextToken: str


class ListEndpointGroupsResponseTypeDef(TypedDict, total=False):
    EndpointGroups: List["EndpointGroupTypeDef"]
    NextToken: str


class ListListenersResponseTypeDef(TypedDict, total=False):
    Listeners: List["ListenerTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": str,
        "PortRanges": List["PortRangeTypeDef"],
        "Protocol": ProtocolType,
        "ClientAffinity": ClientAffinity,
    },
    total=False,
)


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PortMappingTypeDef(TypedDict, total=False):
    AcceleratorPort: int
    EndpointGroupArn: str
    EndpointId: str
    DestinationSocketAddress: "SocketAddressTypeDef"
    Protocols: List[CustomRoutingProtocol]
    DestinationTrafficState: CustomRoutingDestinationTrafficState


class PortOverrideTypeDef(TypedDict, total=False):
    ListenerPort: int
    EndpointPort: int


class PortRangeTypeDef(TypedDict, total=False):
    FromPort: int
    ToPort: int


class ProvisionByoipCidrResponseTypeDef(TypedDict, total=False):
    ByoipCidr: "ByoipCidrTypeDef"


class SocketAddressTypeDef(TypedDict, total=False):
    IpAddress: str
    Port: int


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class UpdateAcceleratorAttributesResponseTypeDef(TypedDict, total=False):
    AcceleratorAttributes: "AcceleratorAttributesTypeDef"


class UpdateAcceleratorResponseTypeDef(TypedDict, total=False):
    Accelerator: "AcceleratorTypeDef"


class UpdateCustomRoutingAcceleratorAttributesResponseTypeDef(TypedDict, total=False):
    AcceleratorAttributes: "CustomRoutingAcceleratorAttributesTypeDef"


class UpdateCustomRoutingAcceleratorResponseTypeDef(TypedDict, total=False):
    Accelerator: "CustomRoutingAcceleratorTypeDef"


class UpdateCustomRoutingListenerResponseTypeDef(TypedDict, total=False):
    Listener: "CustomRoutingListenerTypeDef"


class UpdateEndpointGroupResponseTypeDef(TypedDict, total=False):
    EndpointGroup: "EndpointGroupTypeDef"


class UpdateListenerResponseTypeDef(TypedDict, total=False):
    Listener: "ListenerTypeDef"


class WithdrawByoipCidrResponseTypeDef(TypedDict, total=False):
    ByoipCidr: "ByoipCidrTypeDef"
