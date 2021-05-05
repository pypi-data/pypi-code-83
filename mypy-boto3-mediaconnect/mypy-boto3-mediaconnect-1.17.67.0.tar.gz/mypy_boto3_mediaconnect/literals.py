"""
Type annotations for mediaconnect service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconnect/literals.html)

Usage::

    ```python
    from mypy_boto3_mediaconnect.literals import Algorithm

    data: Algorithm = "aes128"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "Algorithm",
    "DurationUnits",
    "EntitlementStatus",
    "FlowActiveWaiterName",
    "FlowDeletedWaiterName",
    "FlowStandbyWaiterName",
    "KeyType",
    "ListEntitlementsPaginatorName",
    "ListFlowsPaginatorName",
    "ListOfferingsPaginatorName",
    "ListReservationsPaginatorName",
    "PriceUnits",
    "ProtocolType",
    "ReservationState",
    "ResourceType",
    "SourceType",
    "State",
    "Status",
)


Algorithm = Literal["aes128", "aes192", "aes256"]
DurationUnits = Literal["MONTHS"]
EntitlementStatus = Literal["DISABLED", "ENABLED"]
FlowActiveWaiterName = Literal["flow_active"]
FlowDeletedWaiterName = Literal["flow_deleted"]
FlowStandbyWaiterName = Literal["flow_standby"]
KeyType = Literal["speke", "srt-password", "static-key"]
ListEntitlementsPaginatorName = Literal["list_entitlements"]
ListFlowsPaginatorName = Literal["list_flows"]
ListOfferingsPaginatorName = Literal["list_offerings"]
ListReservationsPaginatorName = Literal["list_reservations"]
PriceUnits = Literal["HOURLY"]
ProtocolType = Literal["rist", "rtp", "rtp-fec", "srt-listener", "zixi-pull", "zixi-push"]
ReservationState = Literal["ACTIVE", "CANCELED", "EXPIRED", "PROCESSING"]
ResourceType = Literal["Mbps_Outbound_Bandwidth"]
SourceType = Literal["ENTITLED", "OWNED"]
State = Literal["DISABLED", "ENABLED"]
Status = Literal["ACTIVE", "DELETING", "ERROR", "STANDBY", "STARTING", "STOPPING", "UPDATING"]
