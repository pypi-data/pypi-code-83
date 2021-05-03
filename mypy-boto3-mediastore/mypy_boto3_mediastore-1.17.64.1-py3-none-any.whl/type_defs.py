"""
Type annotations for mediastore service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediastore.type_defs import ContainerTypeDef

    data: ContainerTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_mediastore.literals import ContainerLevelMetrics, ContainerStatus, MethodName

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ContainerTypeDef",
    "CorsRuleTypeDef",
    "CreateContainerOutputTypeDef",
    "DescribeContainerOutputTypeDef",
    "GetContainerPolicyOutputTypeDef",
    "GetCorsPolicyOutputTypeDef",
    "GetLifecyclePolicyOutputTypeDef",
    "GetMetricPolicyOutputTypeDef",
    "ListContainersOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MetricPolicyRuleTypeDef",
    "MetricPolicyTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadata",
    "TagTypeDef",
)


class ContainerTypeDef(TypedDict, total=False):
    Endpoint: str
    CreationTime: datetime
    ARN: str
    Name: str
    Status: ContainerStatus
    AccessLoggingEnabled: bool


class _RequiredCorsRuleTypeDef(TypedDict):
    AllowedOrigins: List[str]
    AllowedHeaders: List[str]


class CorsRuleTypeDef(_RequiredCorsRuleTypeDef, total=False):
    AllowedMethods: List[MethodName]
    MaxAgeSeconds: int
    ExposeHeaders: List[str]


CreateContainerOutputTypeDef = TypedDict(
    "CreateContainerOutputTypeDef",
    {"Container": "ContainerTypeDef", "ResponseMetadata": "ResponseMetadata"},
)

DescribeContainerOutputTypeDef = TypedDict(
    "DescribeContainerOutputTypeDef",
    {"Container": "ContainerTypeDef", "ResponseMetadata": "ResponseMetadata"},
)


class GetContainerPolicyOutputTypeDef(TypedDict):
    Policy: str
    ResponseMetadata: "ResponseMetadata"


class GetCorsPolicyOutputTypeDef(TypedDict):
    CorsPolicy: List["CorsRuleTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetLifecyclePolicyOutputTypeDef(TypedDict):
    LifecyclePolicy: str
    ResponseMetadata: "ResponseMetadata"


class GetMetricPolicyOutputTypeDef(TypedDict):
    MetricPolicy: "MetricPolicyTypeDef"
    ResponseMetadata: "ResponseMetadata"


class ListContainersOutputTypeDef(TypedDict):
    Containers: List["ContainerTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class MetricPolicyRuleTypeDef(TypedDict):
    ObjectGroup: str
    ObjectGroupName: str


class _RequiredMetricPolicyTypeDef(TypedDict):
    ContainerLevelMetrics: ContainerLevelMetrics


class MetricPolicyTypeDef(_RequiredMetricPolicyTypeDef, total=False):
    MetricPolicyRules: List["MetricPolicyRuleTypeDef"]


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


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    Value: str
