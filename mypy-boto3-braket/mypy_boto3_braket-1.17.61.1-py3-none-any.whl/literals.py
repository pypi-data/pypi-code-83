"""
Type annotations for braket service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_braket/literals.html)

Usage::

    ```python
    from mypy_boto3_braket.literals import CancellationStatus

    data: CancellationStatus = "CANCELLED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CancellationStatus",
    "DeviceStatus",
    "DeviceType",
    "QuantumTaskStatus",
    "SearchDevicesPaginatorName",
    "SearchQuantumTasksFilterOperator",
    "SearchQuantumTasksPaginatorName",
)


CancellationStatus = Literal["CANCELLED", "CANCELLING"]
DeviceStatus = Literal["OFFLINE", "ONLINE"]
DeviceType = Literal["QPU", "SIMULATOR"]
QuantumTaskStatus = Literal[
    "CANCELLED", "CANCELLING", "COMPLETED", "CREATED", "FAILED", "QUEUED", "RUNNING"
]
SearchDevicesPaginatorName = Literal["search_devices"]
SearchQuantumTasksFilterOperator = Literal["BETWEEN", "EQUAL", "GT", "GTE", "LT", "LTE"]
SearchQuantumTasksPaginatorName = Literal["search_quantum_tasks"]
