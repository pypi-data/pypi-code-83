"""
Main interface for ebs service literal definitions.

Usage::

    ```python
    from mypy_boto3_ebs.literals import ChecksumAggregationMethod

    data: ChecksumAggregationMethod = "LINEAR"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ChecksumAggregationMethod", "ChecksumAlgorithm", "Status")


ChecksumAggregationMethod = Literal["LINEAR"]
ChecksumAlgorithm = Literal["SHA256"]
Status = Literal["completed", "error", "pending"]
