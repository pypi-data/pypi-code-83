"""
Type annotations for synthetics service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_synthetics/type_defs.html)

Usage::

    ```python
    from mypy_boto3_synthetics.type_defs import CanaryCodeInputTypeDef

    data: CanaryCodeInputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_synthetics.literals import CanaryRunState, CanaryRunStateReasonCode, CanaryState

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CanaryCodeInputTypeDef",
    "CanaryCodeOutputTypeDef",
    "CanaryLastRunTypeDef",
    "CanaryRunConfigInputTypeDef",
    "CanaryRunConfigOutputTypeDef",
    "CanaryRunStatusTypeDef",
    "CanaryRunTimelineTypeDef",
    "CanaryRunTypeDef",
    "CanaryScheduleInputTypeDef",
    "CanaryScheduleOutputTypeDef",
    "CanaryStatusTypeDef",
    "CanaryTimelineTypeDef",
    "CanaryTypeDef",
    "CreateCanaryResponseTypeDef",
    "DescribeCanariesLastRunResponseTypeDef",
    "DescribeCanariesResponseTypeDef",
    "DescribeRuntimeVersionsResponseTypeDef",
    "GetCanaryResponseTypeDef",
    "GetCanaryRunsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ResponseMetadata",
    "RuntimeVersionTypeDef",
    "VpcConfigInputTypeDef",
    "VpcConfigOutputTypeDef",
)


class _RequiredCanaryCodeInputTypeDef(TypedDict):
    Handler: str


class CanaryCodeInputTypeDef(_RequiredCanaryCodeInputTypeDef, total=False):
    S3Bucket: str
    S3Key: str
    S3Version: str
    ZipFile: Union[bytes, IO[bytes]]


class CanaryCodeOutputTypeDef(TypedDict):
    SourceLocationArn: str
    Handler: str
    ResponseMetadata: "ResponseMetadata"


class CanaryLastRunTypeDef(TypedDict, total=False):
    CanaryName: str
    LastRun: "CanaryRunTypeDef"


class CanaryRunConfigInputTypeDef(TypedDict, total=False):
    TimeoutInSeconds: int
    MemoryInMB: int
    ActiveTracing: bool
    EnvironmentVariables: Dict[str, str]


class CanaryRunConfigOutputTypeDef(TypedDict):
    TimeoutInSeconds: int
    MemoryInMB: int
    ActiveTracing: bool
    ResponseMetadata: "ResponseMetadata"


class CanaryRunStatusTypeDef(TypedDict, total=False):
    State: CanaryRunState
    StateReason: str
    StateReasonCode: CanaryRunStateReasonCode


class CanaryRunTimelineTypeDef(TypedDict, total=False):
    Started: datetime
    Completed: datetime


class CanaryRunTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Status: "CanaryRunStatusTypeDef"
    Timeline: "CanaryRunTimelineTypeDef"
    ArtifactS3Location: str


class _RequiredCanaryScheduleInputTypeDef(TypedDict):
    Expression: str


class CanaryScheduleInputTypeDef(_RequiredCanaryScheduleInputTypeDef, total=False):
    DurationInSeconds: int


class CanaryScheduleOutputTypeDef(TypedDict):
    Expression: str
    DurationInSeconds: int
    ResponseMetadata: "ResponseMetadata"


class CanaryStatusTypeDef(TypedDict, total=False):
    State: CanaryState
    StateReason: str
    StateReasonCode: Literal["INVALID_PERMISSIONS"]


class CanaryTimelineTypeDef(TypedDict, total=False):
    Created: datetime
    LastModified: datetime
    LastStarted: datetime
    LastStopped: datetime


class CanaryTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Code: "CanaryCodeOutputTypeDef"
    ExecutionRoleArn: str
    Schedule: "CanaryScheduleOutputTypeDef"
    RunConfig: "CanaryRunConfigOutputTypeDef"
    SuccessRetentionPeriodInDays: int
    FailureRetentionPeriodInDays: int
    Status: "CanaryStatusTypeDef"
    Timeline: "CanaryTimelineTypeDef"
    ArtifactS3Location: str
    EngineArn: str
    RuntimeVersion: str
    VpcConfig: "VpcConfigOutputTypeDef"
    Tags: Dict[str, str]


class CreateCanaryResponseTypeDef(TypedDict, total=False):
    Canary: "CanaryTypeDef"


class DescribeCanariesLastRunResponseTypeDef(TypedDict, total=False):
    CanariesLastRun: List["CanaryLastRunTypeDef"]
    NextToken: str


class DescribeCanariesResponseTypeDef(TypedDict, total=False):
    Canaries: List["CanaryTypeDef"]
    NextToken: str


class DescribeRuntimeVersionsResponseTypeDef(TypedDict, total=False):
    RuntimeVersions: List["RuntimeVersionTypeDef"]
    NextToken: str


class GetCanaryResponseTypeDef(TypedDict, total=False):
    Canary: "CanaryTypeDef"


class GetCanaryRunsResponseTypeDef(TypedDict, total=False):
    CanaryRuns: List["CanaryRunTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RuntimeVersionTypeDef(TypedDict, total=False):
    VersionName: str
    Description: str
    ReleaseDate: datetime
    DeprecationDate: datetime


class VpcConfigInputTypeDef(TypedDict, total=False):
    SubnetIds: List[str]
    SecurityGroupIds: List[str]


class VpcConfigOutputTypeDef(TypedDict):
    VpcId: str
    SubnetIds: List[str]
    SecurityGroupIds: List[str]
    ResponseMetadata: "ResponseMetadata"
