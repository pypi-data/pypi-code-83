"""
Type annotations for meteringmarketplace service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_meteringmarketplace/type_defs.html)

Usage::

    ```python
    from mypy_boto3_meteringmarketplace.type_defs import BatchMeterUsageResultTypeDef

    data: BatchMeterUsageResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_meteringmarketplace.literals import UsageRecordResultStatus

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchMeterUsageResultTypeDef",
    "MeterUsageResultTypeDef",
    "RegisterUsageResultTypeDef",
    "ResolveCustomerResultTypeDef",
    "TagTypeDef",
    "UsageAllocationTypeDef",
    "UsageRecordResultTypeDef",
    "UsageRecordTypeDef",
)


class BatchMeterUsageResultTypeDef(TypedDict, total=False):
    Results: List["UsageRecordResultTypeDef"]
    UnprocessedRecords: List["UsageRecordTypeDef"]


class MeterUsageResultTypeDef(TypedDict, total=False):
    MeteringRecordId: str


class RegisterUsageResultTypeDef(TypedDict, total=False):
    PublicKeyRotationTimestamp: datetime
    Signature: str


class ResolveCustomerResultTypeDef(TypedDict, total=False):
    CustomerIdentifier: str
    ProductCode: str


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class _RequiredUsageAllocationTypeDef(TypedDict):
    AllocatedUsageQuantity: int


class UsageAllocationTypeDef(_RequiredUsageAllocationTypeDef, total=False):
    Tags: List["TagTypeDef"]


class UsageRecordResultTypeDef(TypedDict, total=False):
    UsageRecord: "UsageRecordTypeDef"
    MeteringRecordId: str
    Status: UsageRecordResultStatus


class _RequiredUsageRecordTypeDef(TypedDict):
    Timestamp: datetime
    CustomerIdentifier: str
    Dimension: str


class UsageRecordTypeDef(_RequiredUsageRecordTypeDef, total=False):
    Quantity: int
    UsageAllocations: List["UsageAllocationTypeDef"]
