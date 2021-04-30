"""
Main interface for lakeformation service literal definitions.

Usage::

    ```python
    from mypy_boto3_lakeformation.literals import ComparisonOperator

    data: ComparisonOperator = "BEGINS_WITH"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ComparisonOperator", "DataLakeResourceType", "FieldNameString", "Permission")


ComparisonOperator = Literal[
    "BEGINS_WITH", "BETWEEN", "CONTAINS", "EQ", "GE", "GT", "IN", "LE", "LT", "NE", "NOT_CONTAINS"
]
DataLakeResourceType = Literal["CATALOG", "DATABASE", "DATA_LOCATION", "TABLE"]
FieldNameString = Literal["LAST_MODIFIED", "RESOURCE_ARN", "ROLE_ARN"]
Permission = Literal[
    "ALL",
    "ALTER",
    "CREATE_DATABASE",
    "CREATE_TABLE",
    "DATA_LOCATION_ACCESS",
    "DELETE",
    "DESCRIBE",
    "DROP",
    "INSERT",
    "SELECT",
]
