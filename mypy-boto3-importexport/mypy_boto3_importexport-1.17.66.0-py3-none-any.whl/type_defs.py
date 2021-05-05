"""
Type annotations for importexport service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_importexport/type_defs.html)

Usage::

    ```python
    from mypy_boto3_importexport.type_defs import ArtifactTypeDef

    data: ArtifactTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_importexport.literals import JobType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArtifactTypeDef",
    "CancelJobOutputTypeDef",
    "CreateJobOutputTypeDef",
    "GetShippingLabelOutputTypeDef",
    "GetStatusOutputTypeDef",
    "JobTypeDef",
    "ListJobsOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadata",
    "UpdateJobOutputTypeDef",
)


class ArtifactTypeDef(TypedDict, total=False):
    Description: str
    URL: str


class CancelJobOutputTypeDef(TypedDict):
    Success: bool
    ResponseMetadata: "ResponseMetadata"


class CreateJobOutputTypeDef(TypedDict):
    JobId: str
    JobType: JobType
    Signature: str
    SignatureFileContents: str
    WarningMessage: str
    ArtifactList: List["ArtifactTypeDef"]
    ResponseMetadata: "ResponseMetadata"


GetShippingLabelOutputTypeDef = TypedDict(
    "GetShippingLabelOutputTypeDef",
    {"ShippingLabelURL": str, "Warning": str, "ResponseMetadata": "ResponseMetadata"},
)


class GetStatusOutputTypeDef(TypedDict):
    JobId: str
    JobType: JobType
    LocationCode: str
    LocationMessage: str
    ProgressCode: str
    ProgressMessage: str
    Carrier: str
    TrackingNumber: str
    LogBucket: str
    LogKey: str
    ErrorCount: int
    Signature: str
    SignatureFileContents: str
    CurrentManifest: str
    CreationDate: datetime
    ArtifactList: List["ArtifactTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class JobTypeDef(TypedDict, total=False):
    JobId: str
    CreationDate: datetime
    IsCanceled: bool
    JobType: JobType


class ListJobsOutputTypeDef(TypedDict):
    Jobs: List["JobTypeDef"]
    IsTruncated: bool
    ResponseMetadata: "ResponseMetadata"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class UpdateJobOutputTypeDef(TypedDict):
    Success: bool
    WarningMessage: str
    ArtifactList: List["ArtifactTypeDef"]
    ResponseMetadata: "ResponseMetadata"
