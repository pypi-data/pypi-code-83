"""
Main interface for iotsecuretunneling service type definitions.

Usage::

    ```python
    from mypy_boto3_iotsecuretunneling.type_defs import ConnectionStateTypeDef

    data: ConnectionStateTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_iotsecuretunneling.literals import ConnectionStatus, TunnelStatus

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ConnectionStateTypeDef",
    "DestinationConfigTypeDef",
    "TagTypeDef",
    "TimeoutConfigTypeDef",
    "TunnelSummaryTypeDef",
    "TunnelTypeDef",
    "DescribeTunnelResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTunnelsResponseTypeDef",
    "OpenTunnelResponseTypeDef",
)

ConnectionStateTypeDef = TypedDict(
    "ConnectionStateTypeDef", {"status": ConnectionStatus, "lastUpdatedAt": datetime}, total=False
)

_RequiredDestinationConfigTypeDef = TypedDict(
    "_RequiredDestinationConfigTypeDef", {"services": List[str]}
)
_OptionalDestinationConfigTypeDef = TypedDict(
    "_OptionalDestinationConfigTypeDef", {"thingName": str}, total=False
)


class DestinationConfigTypeDef(
    _RequiredDestinationConfigTypeDef, _OptionalDestinationConfigTypeDef
):
    pass


TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str})

TimeoutConfigTypeDef = TypedDict(
    "TimeoutConfigTypeDef", {"maxLifetimeTimeoutMinutes": int}, total=False
)

TunnelSummaryTypeDef = TypedDict(
    "TunnelSummaryTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "status": TunnelStatus,
        "description": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

TunnelTypeDef = TypedDict(
    "TunnelTypeDef",
    {
        "tunnelId": str,
        "tunnelArn": str,
        "status": TunnelStatus,
        "sourceConnectionState": "ConnectionStateTypeDef",
        "destinationConnectionState": "ConnectionStateTypeDef",
        "description": str,
        "destinationConfig": "DestinationConfigTypeDef",
        "timeoutConfig": "TimeoutConfigTypeDef",
        "tags": List["TagTypeDef"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

DescribeTunnelResponseTypeDef = TypedDict(
    "DescribeTunnelResponseTypeDef", {"tunnel": "TunnelTypeDef"}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": List["TagTypeDef"]}, total=False
)

ListTunnelsResponseTypeDef = TypedDict(
    "ListTunnelsResponseTypeDef",
    {"tunnelSummaries": List["TunnelSummaryTypeDef"], "nextToken": str},
    total=False,
)

OpenTunnelResponseTypeDef = TypedDict(
    "OpenTunnelResponseTypeDef",
    {"tunnelId": str, "tunnelArn": str, "sourceAccessToken": str, "destinationAccessToken": str},
    total=False,
)
