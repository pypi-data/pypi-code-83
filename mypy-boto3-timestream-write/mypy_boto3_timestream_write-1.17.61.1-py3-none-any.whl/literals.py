"""
Type annotations for timestream-write service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/literals.html)

Usage::

    ```python
    from mypy_boto3_timestream_write.literals import DimensionValueType

    data: DimensionValueType = "VARCHAR"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("DimensionValueType", "MeasureValueType", "TableStatus", "TimeUnit")


DimensionValueType = Literal["VARCHAR"]
MeasureValueType = Literal["BIGINT", "BOOLEAN", "DOUBLE", "VARCHAR"]
TableStatus = Literal["ACTIVE", "DELETING"]
TimeUnit = Literal["MICROSECONDS", "MILLISECONDS", "NANOSECONDS", "SECONDS"]
