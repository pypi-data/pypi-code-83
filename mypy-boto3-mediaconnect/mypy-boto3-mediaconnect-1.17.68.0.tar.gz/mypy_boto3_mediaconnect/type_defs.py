"""
Type annotations for mediaconnect service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediaconnect.type_defs import AddFlowOutputsResponseTypeDef

    data: AddFlowOutputsResponseTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from mypy_boto3_mediaconnect.literals import (
    Algorithm,
    EntitlementStatus,
    KeyType,
    ProtocolType,
    ReservationState,
    SourceType,
    State,
    Status,
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
    "AddFlowOutputsResponseTypeDef",
    "AddFlowSourcesResponseTypeDef",
    "AddFlowVpcInterfacesResponseTypeDef",
    "AddOutputRequestTypeDef",
    "CreateFlowResponseTypeDef",
    "DeleteFlowResponseTypeDef",
    "DescribeFlowResponseTypeDef",
    "DescribeOfferingResponseTypeDef",
    "DescribeReservationResponseTypeDef",
    "EncryptionTypeDef",
    "EntitlementTypeDef",
    "FailoverConfigTypeDef",
    "FlowTypeDef",
    "GrantEntitlementRequestTypeDef",
    "GrantFlowEntitlementsResponseTypeDef",
    "ListEntitlementsResponseTypeDef",
    "ListFlowsResponseTypeDef",
    "ListOfferingsResponseTypeDef",
    "ListReservationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListedEntitlementTypeDef",
    "ListedFlowTypeDef",
    "MessagesTypeDef",
    "OfferingTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PurchaseOfferingResponseTypeDef",
    "RemoveFlowOutputResponseTypeDef",
    "RemoveFlowSourceResponseTypeDef",
    "RemoveFlowVpcInterfaceResponseTypeDef",
    "ReservationTypeDef",
    "ResourceSpecificationTypeDef",
    "ResponseMetadata",
    "RevokeFlowEntitlementResponseTypeDef",
    "SetSourceRequestTypeDef",
    "SourceTypeDef",
    "StartFlowResponseTypeDef",
    "StopFlowResponseTypeDef",
    "TransportTypeDef",
    "UpdateEncryptionTypeDef",
    "UpdateFailoverConfigTypeDef",
    "UpdateFlowEntitlementResponseTypeDef",
    "UpdateFlowOutputResponseTypeDef",
    "UpdateFlowResponseTypeDef",
    "UpdateFlowSourceResponseTypeDef",
    "VpcInterfaceAttachmentTypeDef",
    "VpcInterfaceRequestTypeDef",
    "VpcInterfaceTypeDef",
    "WaiterConfigTypeDef",
)


class AddFlowOutputsResponseTypeDef(TypedDict, total=False):
    FlowArn: str
    Outputs: List["OutputTypeDef"]


class AddFlowSourcesResponseTypeDef(TypedDict, total=False):
    FlowArn: str
    Sources: List["SourceTypeDef"]


class AddFlowVpcInterfacesResponseTypeDef(TypedDict, total=False):
    FlowArn: str
    VpcInterfaces: List["VpcInterfaceTypeDef"]


_RequiredAddOutputRequestTypeDef = TypedDict(
    "_RequiredAddOutputRequestTypeDef", {"Protocol": ProtocolType}
)
_OptionalAddOutputRequestTypeDef = TypedDict(
    "_OptionalAddOutputRequestTypeDef",
    {
        "CidrAllowList": List[str],
        "Description": str,
        "Destination": str,
        "Encryption": "EncryptionTypeDef",
        "MaxLatency": int,
        "MinLatency": int,
        "Name": str,
        "Port": int,
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
        "VpcInterfaceAttachment": "VpcInterfaceAttachmentTypeDef",
    },
    total=False,
)


class AddOutputRequestTypeDef(_RequiredAddOutputRequestTypeDef, _OptionalAddOutputRequestTypeDef):
    pass


class CreateFlowResponseTypeDef(TypedDict, total=False):
    Flow: "FlowTypeDef"


class DeleteFlowResponseTypeDef(TypedDict, total=False):
    FlowArn: str
    Status: Status


class DescribeFlowResponseTypeDef(TypedDict, total=False):
    Flow: "FlowTypeDef"
    Messages: "MessagesTypeDef"


class DescribeOfferingResponseTypeDef(TypedDict, total=False):
    Offering: "OfferingTypeDef"


class DescribeReservationResponseTypeDef(TypedDict, total=False):
    Reservation: "ReservationTypeDef"


class _RequiredEncryptionTypeDef(TypedDict):
    RoleArn: str


class EncryptionTypeDef(_RequiredEncryptionTypeDef, total=False):
    Algorithm: Algorithm
    ConstantInitializationVector: str
    DeviceId: str
    KeyType: KeyType
    Region: str
    ResourceId: str
    SecretArn: str
    Url: str


class _RequiredEntitlementTypeDef(TypedDict):
    EntitlementArn: str
    Name: str
    Subscribers: List[str]


class EntitlementTypeDef(_RequiredEntitlementTypeDef, total=False):
    DataTransferSubscriberFeePercent: int
    Description: str
    Encryption: "EncryptionTypeDef"
    EntitlementStatus: EntitlementStatus


class FailoverConfigTypeDef(TypedDict, total=False):
    RecoveryWindow: int
    State: State


class _RequiredFlowTypeDef(TypedDict):
    AvailabilityZone: str
    Entitlements: List["EntitlementTypeDef"]
    FlowArn: str
    Name: str
    Outputs: List["OutputTypeDef"]
    Source: "SourceTypeDef"
    Status: Status


class FlowTypeDef(_RequiredFlowTypeDef, total=False):
    Description: str
    EgressIp: str
    SourceFailoverConfig: "FailoverConfigTypeDef"
    Sources: List["SourceTypeDef"]
    VpcInterfaces: List["VpcInterfaceTypeDef"]


class _RequiredGrantEntitlementRequestTypeDef(TypedDict):
    Subscribers: List[str]


class GrantEntitlementRequestTypeDef(_RequiredGrantEntitlementRequestTypeDef, total=False):
    DataTransferSubscriberFeePercent: int
    Description: str
    Encryption: "EncryptionTypeDef"
    EntitlementStatus: EntitlementStatus
    Name: str


class GrantFlowEntitlementsResponseTypeDef(TypedDict, total=False):
    Entitlements: List["EntitlementTypeDef"]
    FlowArn: str


class ListEntitlementsResponseTypeDef(TypedDict, total=False):
    Entitlements: List["ListedEntitlementTypeDef"]
    NextToken: str


class ListFlowsResponseTypeDef(TypedDict, total=False):
    Flows: List["ListedFlowTypeDef"]
    NextToken: str


class ListOfferingsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Offerings: List["OfferingTypeDef"]


class ListReservationsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Reservations: List["ReservationTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class _RequiredListedEntitlementTypeDef(TypedDict):
    EntitlementArn: str
    EntitlementName: str


class ListedEntitlementTypeDef(_RequiredListedEntitlementTypeDef, total=False):
    DataTransferSubscriberFeePercent: int


class ListedFlowTypeDef(TypedDict):
    AvailabilityZone: str
    Description: str
    FlowArn: str
    Name: str
    SourceType: SourceType
    Status: Status


class MessagesTypeDef(TypedDict):
    Errors: List[str]


class OfferingTypeDef(TypedDict):
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal["MONTHS"]
    OfferingArn: str
    OfferingDescription: str
    PricePerUnit: str
    PriceUnits: Literal["HOURLY"]
    ResourceSpecification: "ResourceSpecificationTypeDef"


class OutputTypeDef(TypedDict):
    DataTransferSubscriberFeePercent: int
    Description: str
    Destination: str
    Encryption: "EncryptionTypeDef"
    EntitlementArn: str
    ListenerAddress: str
    MediaLiveInputArn: str
    Name: str
    OutputArn: str
    Port: int
    Transport: "TransportTypeDef"
    VpcInterfaceAttachment: "VpcInterfaceAttachmentTypeDef"
    ResponseMetadata: "ResponseMetadata"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PurchaseOfferingResponseTypeDef(TypedDict, total=False):
    Reservation: "ReservationTypeDef"


class RemoveFlowOutputResponseTypeDef(TypedDict, total=False):
    FlowArn: str
    OutputArn: str


class RemoveFlowSourceResponseTypeDef(TypedDict, total=False):
    FlowArn: str
    SourceArn: str


class RemoveFlowVpcInterfaceResponseTypeDef(TypedDict, total=False):
    FlowArn: str
    NonDeletedNetworkInterfaceIds: List[str]
    VpcInterfaceName: str


class ReservationTypeDef(TypedDict):
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal["MONTHS"]
    End: str
    OfferingArn: str
    OfferingDescription: str
    PricePerUnit: str
    PriceUnits: Literal["HOURLY"]
    ReservationArn: str
    ReservationName: str
    ReservationState: ReservationState
    ResourceSpecification: "ResourceSpecificationTypeDef"
    Start: str


class _RequiredResourceSpecificationTypeDef(TypedDict):
    ResourceType: Literal["Mbps_Outbound_Bandwidth"]


class ResourceSpecificationTypeDef(_RequiredResourceSpecificationTypeDef, total=False):
    ReservedBitrate: int


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RevokeFlowEntitlementResponseTypeDef(TypedDict, total=False):
    EntitlementArn: str
    FlowArn: str


SetSourceRequestTypeDef = TypedDict(
    "SetSourceRequestTypeDef",
    {
        "Decryption": "EncryptionTypeDef",
        "Description": str,
        "EntitlementArn": str,
        "IngestPort": int,
        "MaxBitrate": int,
        "MaxLatency": int,
        "MinLatency": int,
        "Name": str,
        "Protocol": ProtocolType,
        "StreamId": str,
        "VpcInterfaceName": str,
        "WhitelistCidr": str,
    },
    total=False,
)


class _RequiredSourceTypeDef(TypedDict):
    Name: str
    SourceArn: str


class SourceTypeDef(_RequiredSourceTypeDef, total=False):
    DataTransferSubscriberFeePercent: int
    Decryption: "EncryptionTypeDef"
    Description: str
    EntitlementArn: str
    IngestIp: str
    IngestPort: int
    Transport: "TransportTypeDef"
    VpcInterfaceName: str
    WhitelistCidr: str


class StartFlowResponseTypeDef(TypedDict, total=False):
    FlowArn: str
    Status: Status


class StopFlowResponseTypeDef(TypedDict, total=False):
    FlowArn: str
    Status: Status


_RequiredTransportTypeDef = TypedDict("_RequiredTransportTypeDef", {"Protocol": ProtocolType})
_OptionalTransportTypeDef = TypedDict(
    "_OptionalTransportTypeDef",
    {
        "CidrAllowList": List[str],
        "MaxBitrate": int,
        "MaxLatency": int,
        "MinLatency": int,
        "RemoteId": str,
        "SmoothingLatency": int,
        "StreamId": str,
    },
    total=False,
)


class TransportTypeDef(_RequiredTransportTypeDef, _OptionalTransportTypeDef):
    pass


class UpdateEncryptionTypeDef(TypedDict, total=False):
    Algorithm: Algorithm
    ConstantInitializationVector: str
    DeviceId: str
    KeyType: KeyType
    Region: str
    ResourceId: str
    RoleArn: str
    SecretArn: str
    Url: str


class UpdateFailoverConfigTypeDef(TypedDict, total=False):
    RecoveryWindow: int
    State: State


class UpdateFlowEntitlementResponseTypeDef(TypedDict, total=False):
    Entitlement: "EntitlementTypeDef"
    FlowArn: str


class UpdateFlowOutputResponseTypeDef(TypedDict, total=False):
    FlowArn: str
    Output: "OutputTypeDef"


class UpdateFlowResponseTypeDef(TypedDict, total=False):
    Flow: "FlowTypeDef"


class UpdateFlowSourceResponseTypeDef(TypedDict, total=False):
    FlowArn: str
    Source: "SourceTypeDef"


class VpcInterfaceAttachmentTypeDef(TypedDict, total=False):
    VpcInterfaceName: str


class VpcInterfaceRequestTypeDef(TypedDict):
    Name: str
    RoleArn: str
    SecurityGroupIds: List[str]
    SubnetId: str


class VpcInterfaceTypeDef(TypedDict):
    Name: str
    NetworkInterfaceIds: List[str]
    RoleArn: str
    SecurityGroupIds: List[str]
    SubnetId: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
