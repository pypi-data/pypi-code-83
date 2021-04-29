"""
Main interface for iotwireless service literal definitions.

Usage::

    ```python
    from mypy_boto3_iotwireless.literals import BatteryLevel

    data: BatteryLevel = "critical"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BatteryLevel",
    "ConnectionStatus",
    "DeviceState",
    "Event",
    "ExpressionType",
    "MessageType",
    "PartnerType",
    "SigningAlg",
    "WirelessDeviceIdType",
    "WirelessDeviceType",
    "WirelessGatewayIdType",
    "WirelessGatewayServiceType",
    "WirelessGatewayTaskDefinitionType",
    "WirelessGatewayTaskStatus",
)


BatteryLevel = Literal["critical", "low", "normal"]
ConnectionStatus = Literal["Connected", "Disconnected"]
DeviceState = Literal[
    "Provisioned", "RegisteredNotSeen", "RegisteredReachable", "RegisteredUnreachable"
]
Event = Literal["ack", "discovered", "lost", "nack", "passthrough"]
ExpressionType = Literal["MqttTopic", "RuleName"]
MessageType = Literal[
    "CUSTOM_COMMAND_ID_GET",
    "CUSTOM_COMMAND_ID_NOTIFY",
    "CUSTOM_COMMAND_ID_RESP",
    "CUSTOM_COMMAND_ID_SET",
]
PartnerType = Literal["Sidewalk"]
SigningAlg = Literal["Ed25519", "P256r1"]
WirelessDeviceIdType = Literal["DevEui", "ThingName", "WirelessDeviceId"]
WirelessDeviceType = Literal["LoRaWAN", "Sidewalk"]
WirelessGatewayIdType = Literal["GatewayEui", "ThingName", "WirelessGatewayId"]
WirelessGatewayServiceType = Literal["CUPS", "LNS"]
WirelessGatewayTaskDefinitionType = Literal["UPDATE"]
WirelessGatewayTaskStatus = Literal[
    "COMPLETED", "FAILED", "FIRST_RETRY", "IN_PROGRESS", "PENDING", "SECOND_RETRY"
]
