"""
Type annotations for sagemaker-a2i-runtime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_a2i_runtime.type_defs import DescribeHumanLoopResponseTypeDef

    data: DescribeHumanLoopResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_sagemaker_a2i_runtime.literals import ContentClassifier, HumanLoopStatus

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DescribeHumanLoopResponseTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "HumanLoopInputTypeDef",
    "HumanLoopOutputTypeDef",
    "HumanLoopSummaryTypeDef",
    "ListHumanLoopsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadata",
    "StartHumanLoopResponseTypeDef",
)


class _RequiredDescribeHumanLoopResponseTypeDef(TypedDict):
    CreationTime: datetime
    HumanLoopStatus: HumanLoopStatus
    HumanLoopName: str
    HumanLoopArn: str
    FlowDefinitionArn: str


class DescribeHumanLoopResponseTypeDef(_RequiredDescribeHumanLoopResponseTypeDef, total=False):
    FailureReason: str
    FailureCode: str
    HumanLoopOutput: "HumanLoopOutputTypeDef"


class HumanLoopDataAttributesTypeDef(TypedDict):
    ContentClassifiers: List[ContentClassifier]


class HumanLoopInputTypeDef(TypedDict):
    InputContent: str


class HumanLoopOutputTypeDef(TypedDict):
    OutputS3Uri: str
    ResponseMetadata: "ResponseMetadata"


class HumanLoopSummaryTypeDef(TypedDict, total=False):
    HumanLoopName: str
    HumanLoopStatus: HumanLoopStatus
    CreationTime: datetime
    FailureReason: str
    FlowDefinitionArn: str


class _RequiredListHumanLoopsResponseTypeDef(TypedDict):
    HumanLoopSummaries: List["HumanLoopSummaryTypeDef"]


class ListHumanLoopsResponseTypeDef(_RequiredListHumanLoopsResponseTypeDef, total=False):
    NextToken: str


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


class StartHumanLoopResponseTypeDef(TypedDict, total=False):
    HumanLoopArn: str
