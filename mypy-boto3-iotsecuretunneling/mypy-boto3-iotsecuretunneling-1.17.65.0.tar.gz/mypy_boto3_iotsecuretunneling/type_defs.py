"""
Type annotations for iotsecuretunneling service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsecuretunneling/type_defs.html)

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
    "DescribeTunnelResponseTypeDef",
    "DestinationConfigTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTunnelsResponseTypeDef",
    "OpenTunnelResponseTypeDef",
    "TagTypeDef",
    "TimeoutConfigTypeDef",
    "TunnelSummaryTypeDef",
    "TunnelTypeDef",
)


class ConnectionStateTypeDef(TypedDict, total=False):
    status: ConnectionStatus
    lastUpdatedAt: datetime


class DescribeTunnelResponseTypeDef(TypedDict, total=False):
    tunnel: "TunnelTypeDef"


class _RequiredDestinationConfigTypeDef(TypedDict):
    services: List[str]


class DestinationConfigTypeDef(_RequiredDestinationConfigTypeDef, total=False):
    thingName: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: List["TagTypeDef"]


class ListTunnelsResponseTypeDef(TypedDict, total=False):
    tunnelSummaries: List["TunnelSummaryTypeDef"]
    nextToken: str


class OpenTunnelResponseTypeDef(TypedDict, total=False):
    tunnelId: str
    tunnelArn: str
    sourceAccessToken: str
    destinationAccessToken: str


class TagTypeDef(TypedDict):
    key: str
    value: str


class TimeoutConfigTypeDef(TypedDict, total=False):
    maxLifetimeTimeoutMinutes: int


class TunnelSummaryTypeDef(TypedDict, total=False):
    tunnelId: str
    tunnelArn: str
    status: TunnelStatus
    description: str
    createdAt: datetime
    lastUpdatedAt: datetime


class TunnelTypeDef(TypedDict, total=False):
    tunnelId: str
    tunnelArn: str
    status: TunnelStatus
    sourceConnectionState: "ConnectionStateTypeDef"
    destinationConnectionState: "ConnectionStateTypeDef"
    description: str
    destinationConfig: "DestinationConfigTypeDef"
    timeoutConfig: "TimeoutConfigTypeDef"
    tags: List["TagTypeDef"]
    createdAt: datetime
    lastUpdatedAt: datetime
