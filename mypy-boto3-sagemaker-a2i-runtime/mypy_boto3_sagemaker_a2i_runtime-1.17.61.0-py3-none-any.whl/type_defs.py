"""
Main interface for sagemaker-a2i-runtime service type definitions.

Usage::

    ```python
    from mypy_boto3_sagemaker_a2i_runtime.type_defs import HumanLoopOutputTypeDef

    data: HumanLoopOutputTypeDef = {...}
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
    "HumanLoopOutputTypeDef",
    "HumanLoopSummaryTypeDef",
    "ResponseMetadata",
    "DescribeHumanLoopResponseTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "HumanLoopInputTypeDef",
    "ListHumanLoopsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "StartHumanLoopResponseTypeDef",
)

_RequiredHumanLoopOutputTypeDef = TypedDict("_RequiredHumanLoopOutputTypeDef", {"OutputS3Uri": str})
_OptionalHumanLoopOutputTypeDef = TypedDict(
    "_OptionalHumanLoopOutputTypeDef", {"ResponseMetadata": "ResponseMetadata"}, total=False
)


class HumanLoopOutputTypeDef(_RequiredHumanLoopOutputTypeDef, _OptionalHumanLoopOutputTypeDef):
    pass


HumanLoopSummaryTypeDef = TypedDict(
    "HumanLoopSummaryTypeDef",
    {
        "HumanLoopName": str,
        "HumanLoopStatus": HumanLoopStatus,
        "CreationTime": datetime,
        "FailureReason": str,
        "FlowDefinitionArn": str,
    },
    total=False,
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredDescribeHumanLoopResponseTypeDef = TypedDict(
    "_RequiredDescribeHumanLoopResponseTypeDef",
    {
        "CreationTime": datetime,
        "HumanLoopStatus": HumanLoopStatus,
        "HumanLoopName": str,
        "HumanLoopArn": str,
        "FlowDefinitionArn": str,
    },
)
_OptionalDescribeHumanLoopResponseTypeDef = TypedDict(
    "_OptionalDescribeHumanLoopResponseTypeDef",
    {"FailureReason": str, "FailureCode": str, "HumanLoopOutput": "HumanLoopOutputTypeDef"},
    total=False,
)


class DescribeHumanLoopResponseTypeDef(
    _RequiredDescribeHumanLoopResponseTypeDef, _OptionalDescribeHumanLoopResponseTypeDef
):
    pass


HumanLoopDataAttributesTypeDef = TypedDict(
    "HumanLoopDataAttributesTypeDef", {"ContentClassifiers": List[ContentClassifier]}
)

HumanLoopInputTypeDef = TypedDict("HumanLoopInputTypeDef", {"InputContent": str})

_RequiredListHumanLoopsResponseTypeDef = TypedDict(
    "_RequiredListHumanLoopsResponseTypeDef",
    {"HumanLoopSummaries": List["HumanLoopSummaryTypeDef"]},
)
_OptionalListHumanLoopsResponseTypeDef = TypedDict(
    "_OptionalListHumanLoopsResponseTypeDef", {"NextToken": str}, total=False
)


class ListHumanLoopsResponseTypeDef(
    _RequiredListHumanLoopsResponseTypeDef, _OptionalListHumanLoopsResponseTypeDef
):
    pass


PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartHumanLoopResponseTypeDef = TypedDict(
    "StartHumanLoopResponseTypeDef", {"HumanLoopArn": str}, total=False
)
