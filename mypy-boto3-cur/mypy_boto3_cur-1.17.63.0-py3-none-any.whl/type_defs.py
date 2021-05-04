"""
Type annotations for cur service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cur/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cur.type_defs import DeleteReportDefinitionResponseTypeDef

    data: DeleteReportDefinitionResponseTypeDef = {...}
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
    TimeUnit,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeleteReportDefinitionResponseTypeDef",
    "DescribeReportDefinitionsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ReportDefinitionTypeDef",
)


class DeleteReportDefinitionResponseTypeDef(TypedDict, total=False):
    ResponseMessage: str


class DescribeReportDefinitionsResponseTypeDef(TypedDict, total=False):
    ReportDefinitions: List["ReportDefinitionTypeDef"]
    NextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredReportDefinitionTypeDef(TypedDict):
    ReportName: str
    TimeUnit: TimeUnit
    Format: ReportFormat
    Compression: CompressionFormat
    AdditionalSchemaElements: List[Literal["RESOURCES"]]
    S3Bucket: str
    S3Prefix: str
    S3Region: AWSRegion


class ReportDefinitionTypeDef(_RequiredReportDefinitionTypeDef, total=False):
    AdditionalArtifacts: List[AdditionalArtifact]
    RefreshClosedReports: bool
    ReportVersioning: ReportVersioning
    BillingViewArn: str
