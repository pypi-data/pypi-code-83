"""
Type annotations for resourcegroupstaggingapi service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_resourcegroupstaggingapi/type_defs.html)

Usage::

    ```python
    from mypy_boto3_resourcegroupstaggingapi.type_defs import ComplianceDetailsTypeDef

    data: ComplianceDetailsTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from mypy_boto3_resourcegroupstaggingapi.literals import ErrorCode, TargetIdType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ComplianceDetailsTypeDef",
    "DescribeReportCreationOutputTypeDef",
    "FailureInfoTypeDef",
    "GetComplianceSummaryOutputTypeDef",
    "GetResourcesOutputTypeDef",
    "GetTagKeysOutputTypeDef",
    "GetTagValuesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceTagMappingTypeDef",
    "ResponseMetadata",
    "SummaryTypeDef",
    "TagFilterTypeDef",
    "TagResourcesOutputTypeDef",
    "TagTypeDef",
    "UntagResourcesOutputTypeDef",
)


class ComplianceDetailsTypeDef(TypedDict, total=False):
    NoncompliantKeys: List[str]
    KeysWithNoncompliantValues: List[str]
    ComplianceStatus: bool


class DescribeReportCreationOutputTypeDef(TypedDict):
    Status: str
    S3Location: str
    ErrorMessage: str
    ResponseMetadata: "ResponseMetadata"


class FailureInfoTypeDef(TypedDict, total=False):
    StatusCode: int
    ErrorCode: ErrorCode
    ErrorMessage: str


class GetComplianceSummaryOutputTypeDef(TypedDict):
    SummaryList: List["SummaryTypeDef"]
    PaginationToken: str
    ResponseMetadata: "ResponseMetadata"


class GetResourcesOutputTypeDef(TypedDict):
    PaginationToken: str
    ResourceTagMappingList: List["ResourceTagMappingTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetTagKeysOutputTypeDef(TypedDict):
    PaginationToken: str
    TagKeys: List[str]
    ResponseMetadata: "ResponseMetadata"


class GetTagValuesOutputTypeDef(TypedDict):
    PaginationToken: str
    TagValues: List[str]
    ResponseMetadata: "ResponseMetadata"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ResourceTagMappingTypeDef(TypedDict, total=False):
    ResourceARN: str
    Tags: List["TagTypeDef"]
    ComplianceDetails: "ComplianceDetailsTypeDef"


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class SummaryTypeDef(TypedDict, total=False):
    LastUpdated: str
    TargetId: str
    TargetIdType: TargetIdType
    Region: str
    ResourceType: str
    NonCompliantResources: int


class TagFilterTypeDef(TypedDict, total=False):
    Key: str
    Values: List[str]


class TagResourcesOutputTypeDef(TypedDict):
    FailedResourcesMap: Dict[str, "FailureInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class UntagResourcesOutputTypeDef(TypedDict):
    FailedResourcesMap: Dict[str, "FailureInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"
