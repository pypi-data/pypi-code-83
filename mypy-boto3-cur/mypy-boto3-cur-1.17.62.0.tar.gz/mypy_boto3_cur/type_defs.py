"""
Main interface for cur service type definitions.

Usage::

    ```python
    from mypy_boto3_cur.type_defs import ReportDefinitionTypeDef

    data: ReportDefinitionTypeDef = {...}
    ```
"""
import sys
from typing import List

from mypy_boto3_cur.literals import (
    AdditionalArtifact,
    AWSRegion,
    CompressionFormat,
    ReportFormat,
    ReportVersioning,
    SchemaElement,
    TimeUnit,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ReportDefinitionTypeDef",
    "DeleteReportDefinitionResponseTypeDef",
    "DescribeReportDefinitionsResponseTypeDef",
    "PaginatorConfigTypeDef",
)

_RequiredReportDefinitionTypeDef = TypedDict(
    "_RequiredReportDefinitionTypeDef",
    {
        "ReportName": str,
        "TimeUnit": TimeUnit,
        "Format": ReportFormat,
        "Compression": CompressionFormat,
        "AdditionalSchemaElements": List[SchemaElement],
        "S3Bucket": str,
        "S3Prefix": str,
        "S3Region": AWSRegion,
    },
)
_OptionalReportDefinitionTypeDef = TypedDict(
    "_OptionalReportDefinitionTypeDef",
    {
        "AdditionalArtifacts": List[AdditionalArtifact],
        "RefreshClosedReports": bool,
        "ReportVersioning": ReportVersioning,
        "BillingViewArn": str,
    },
    total=False,
)


class ReportDefinitionTypeDef(_RequiredReportDefinitionTypeDef, _OptionalReportDefinitionTypeDef):
    pass


DeleteReportDefinitionResponseTypeDef = TypedDict(
    "DeleteReportDefinitionResponseTypeDef", {"ResponseMessage": str}, total=False
)

DescribeReportDefinitionsResponseTypeDef = TypedDict(
    "DescribeReportDefinitionsResponseTypeDef",
    {"ReportDefinitions": List["ReportDefinitionTypeDef"], "NextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
