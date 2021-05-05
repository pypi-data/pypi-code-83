"""
Type annotations for iot1click-devices service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot1click_devices/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot1click_devices.type_defs import ClaimDevicesByClaimCodeResponseTypeDef

    data: ClaimDevicesByClaimCodeResponseTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ClaimDevicesByClaimCodeResponseTypeDef",
    "DescribeDeviceResponseTypeDef",
    "DeviceDescriptionTypeDef",
    "DeviceEventTypeDef",
    "DeviceMethodTypeDef",
    "DeviceTypeDef",
    "FinalizeDeviceClaimResponseTypeDef",
    "GetDeviceMethodsResponseTypeDef",
    "InitiateDeviceClaimResponseTypeDef",
    "InvokeDeviceMethodResponseTypeDef",
    "ListDeviceEventsResponseTypeDef",
    "ListDevicesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "UnclaimDeviceResponseTypeDef",
)


class ClaimDevicesByClaimCodeResponseTypeDef(TypedDict, total=False):
    ClaimCode: str
    Total: int


class DescribeDeviceResponseTypeDef(TypedDict, total=False):
    DeviceDescription: "DeviceDescriptionTypeDef"


DeviceDescriptionTypeDef = TypedDict(
    "DeviceDescriptionTypeDef",
    {
        "Arn": str,
        "Attributes": Dict[str, str],
        "DeviceId": str,
        "Enabled": bool,
        "RemainingLife": float,
        "Type": str,
        "Tags": Dict[str, str],
    },
    total=False,
)


class DeviceEventTypeDef(TypedDict, total=False):
    Device: "DeviceTypeDef"
    StdEvent: str


class DeviceMethodTypeDef(TypedDict, total=False):
    DeviceType: str
    MethodName: str


DeviceTypeDef = TypedDict(
    "DeviceTypeDef", {"Attributes": Dict[str, Any], "DeviceId": str, "Type": str}, total=False
)


class FinalizeDeviceClaimResponseTypeDef(TypedDict, total=False):
    State: str


class GetDeviceMethodsResponseTypeDef(TypedDict, total=False):
    DeviceMethods: List["DeviceMethodTypeDef"]


class InitiateDeviceClaimResponseTypeDef(TypedDict, total=False):
    State: str


class InvokeDeviceMethodResponseTypeDef(TypedDict, total=False):
    DeviceMethodResponse: str


class ListDeviceEventsResponseTypeDef(TypedDict, total=False):
    Events: List["DeviceEventTypeDef"]
    NextToken: str


class ListDevicesResponseTypeDef(TypedDict, total=False):
    Devices: List["DeviceDescriptionTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class UnclaimDeviceResponseTypeDef(TypedDict, total=False):
    State: str
