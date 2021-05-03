"""
Type annotations for braket service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/type_defs.html)

Usage::

    ```python
    from mypy_boto3_braket.type_defs import CancelQuantumTaskResponseTypeDef

    data: CancelQuantumTaskResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_braket.literals import (
    CancellationStatus,
    DeviceStatus,
    DeviceType,
    QuantumTaskStatus,
    SearchQuantumTasksFilterOperator,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelQuantumTaskResponseTypeDef",
    "CreateQuantumTaskResponseTypeDef",
    "DeviceSummaryTypeDef",
    "GetDeviceResponseTypeDef",
    "GetQuantumTaskResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QuantumTaskSummaryTypeDef",
    "SearchDevicesFilterTypeDef",
    "SearchDevicesResponseTypeDef",
    "SearchQuantumTasksFilterTypeDef",
    "SearchQuantumTasksResponseTypeDef",
)


class CancelQuantumTaskResponseTypeDef(TypedDict):
    cancellationStatus: CancellationStatus
    quantumTaskArn: str


class CreateQuantumTaskResponseTypeDef(TypedDict):
    quantumTaskArn: str


class DeviceSummaryTypeDef(TypedDict):
    deviceArn: str
    deviceName: str
    deviceStatus: DeviceStatus
    deviceType: DeviceType
    providerName: str


class GetDeviceResponseTypeDef(TypedDict):
    deviceArn: str
    deviceCapabilities: str
    deviceName: str
    deviceStatus: DeviceStatus
    deviceType: DeviceType
    providerName: str


class _RequiredGetQuantumTaskResponseTypeDef(TypedDict):
    createdAt: datetime
    deviceArn: str
    deviceParameters: str
    outputS3Bucket: str
    outputS3Directory: str
    quantumTaskArn: str
    shots: int
    status: QuantumTaskStatus


class GetQuantumTaskResponseTypeDef(_RequiredGetQuantumTaskResponseTypeDef, total=False):
    endedAt: datetime
    failureReason: str
    tags: Dict[str, str]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredQuantumTaskSummaryTypeDef(TypedDict):
    createdAt: datetime
    deviceArn: str
    outputS3Bucket: str
    outputS3Directory: str
    quantumTaskArn: str
    shots: int
    status: QuantumTaskStatus


class QuantumTaskSummaryTypeDef(_RequiredQuantumTaskSummaryTypeDef, total=False):
    endedAt: datetime
    tags: Dict[str, str]


class SearchDevicesFilterTypeDef(TypedDict):
    name: str
    values: List[str]


class _RequiredSearchDevicesResponseTypeDef(TypedDict):
    devices: List["DeviceSummaryTypeDef"]


class SearchDevicesResponseTypeDef(_RequiredSearchDevicesResponseTypeDef, total=False):
    nextToken: str


SearchQuantumTasksFilterTypeDef = TypedDict(
    "SearchQuantumTasksFilterTypeDef",
    {"name": str, "operator": SearchQuantumTasksFilterOperator, "values": List[str]},
)


class _RequiredSearchQuantumTasksResponseTypeDef(TypedDict):
    quantumTasks: List["QuantumTaskSummaryTypeDef"]


class SearchQuantumTasksResponseTypeDef(_RequiredSearchQuantumTasksResponseTypeDef, total=False):
    nextToken: str
