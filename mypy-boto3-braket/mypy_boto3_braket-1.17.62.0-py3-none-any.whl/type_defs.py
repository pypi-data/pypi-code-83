"""
Main interface for braket service type definitions.

Usage::

    ```python
    from mypy_boto3_braket.type_defs import DeviceSummaryTypeDef

    data: DeviceSummaryTypeDef = {...}
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
    "DeviceSummaryTypeDef",
    "QuantumTaskSummaryTypeDef",
    "CancelQuantumTaskResponseTypeDef",
    "CreateQuantumTaskResponseTypeDef",
    "GetDeviceResponseTypeDef",
    "GetQuantumTaskResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "SearchDevicesFilterTypeDef",
    "SearchDevicesResponseTypeDef",
    "SearchQuantumTasksFilterTypeDef",
    "SearchQuantumTasksResponseTypeDef",
)

DeviceSummaryTypeDef = TypedDict(
    "DeviceSummaryTypeDef",
    {
        "deviceArn": str,
        "deviceName": str,
        "deviceStatus": DeviceStatus,
        "deviceType": DeviceType,
        "providerName": str,
    },
)

_RequiredQuantumTaskSummaryTypeDef = TypedDict(
    "_RequiredQuantumTaskSummaryTypeDef",
    {
        "createdAt": datetime,
        "deviceArn": str,
        "outputS3Bucket": str,
        "outputS3Directory": str,
        "quantumTaskArn": str,
        "shots": int,
        "status": QuantumTaskStatus,
    },
)
_OptionalQuantumTaskSummaryTypeDef = TypedDict(
    "_OptionalQuantumTaskSummaryTypeDef", {"endedAt": datetime, "tags": Dict[str, str]}, total=False
)


class QuantumTaskSummaryTypeDef(
    _RequiredQuantumTaskSummaryTypeDef, _OptionalQuantumTaskSummaryTypeDef
):
    pass


CancelQuantumTaskResponseTypeDef = TypedDict(
    "CancelQuantumTaskResponseTypeDef",
    {"cancellationStatus": CancellationStatus, "quantumTaskArn": str},
)

CreateQuantumTaskResponseTypeDef = TypedDict(
    "CreateQuantumTaskResponseTypeDef", {"quantumTaskArn": str}
)

GetDeviceResponseTypeDef = TypedDict(
    "GetDeviceResponseTypeDef",
    {
        "deviceArn": str,
        "deviceCapabilities": str,
        "deviceName": str,
        "deviceStatus": DeviceStatus,
        "deviceType": DeviceType,
        "providerName": str,
    },
)

_RequiredGetQuantumTaskResponseTypeDef = TypedDict(
    "_RequiredGetQuantumTaskResponseTypeDef",
    {
        "createdAt": datetime,
        "deviceArn": str,
        "deviceParameters": str,
        "outputS3Bucket": str,
        "outputS3Directory": str,
        "quantumTaskArn": str,
        "shots": int,
        "status": QuantumTaskStatus,
    },
)
_OptionalGetQuantumTaskResponseTypeDef = TypedDict(
    "_OptionalGetQuantumTaskResponseTypeDef",
    {"endedAt": datetime, "failureReason": str, "tags": Dict[str, str]},
    total=False,
)


class GetQuantumTaskResponseTypeDef(
    _RequiredGetQuantumTaskResponseTypeDef, _OptionalGetQuantumTaskResponseTypeDef
):
    pass


ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SearchDevicesFilterTypeDef = TypedDict(
    "SearchDevicesFilterTypeDef", {"name": str, "values": List[str]}
)

_RequiredSearchDevicesResponseTypeDef = TypedDict(
    "_RequiredSearchDevicesResponseTypeDef", {"devices": List["DeviceSummaryTypeDef"]}
)
_OptionalSearchDevicesResponseTypeDef = TypedDict(
    "_OptionalSearchDevicesResponseTypeDef", {"nextToken": str}, total=False
)


class SearchDevicesResponseTypeDef(
    _RequiredSearchDevicesResponseTypeDef, _OptionalSearchDevicesResponseTypeDef
):
    pass


SearchQuantumTasksFilterTypeDef = TypedDict(
    "SearchQuantumTasksFilterTypeDef",
    {"name": str, "operator": SearchQuantumTasksFilterOperator, "values": List[str]},
)

_RequiredSearchQuantumTasksResponseTypeDef = TypedDict(
    "_RequiredSearchQuantumTasksResponseTypeDef",
    {"quantumTasks": List["QuantumTaskSummaryTypeDef"]},
)
_OptionalSearchQuantumTasksResponseTypeDef = TypedDict(
    "_OptionalSearchQuantumTasksResponseTypeDef", {"nextToken": str}, total=False
)


class SearchQuantumTasksResponseTypeDef(
    _RequiredSearchQuantumTasksResponseTypeDef, _OptionalSearchQuantumTasksResponseTypeDef
):
    pass
