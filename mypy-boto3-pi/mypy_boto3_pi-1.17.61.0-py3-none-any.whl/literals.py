"""
Main interface for pi service literal definitions.

Usage::

    ```python
    from mypy_boto3_pi.literals import ServiceType

    data: ServiceType = "RDS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServiceType",)


ServiceType = Literal["RDS"]
