"""
Type annotations for iotevents-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotevents_data.type_defs import BatchPutMessageErrorEntryTypeDef

    data: BatchPutMessageErrorEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, List, Union

from mypy_boto3_iotevents_data.literals import ErrorCode

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchPutMessageErrorEntryTypeDef",
    "BatchPutMessageResponseTypeDef",
    "BatchUpdateDetectorErrorEntryTypeDef",
    "BatchUpdateDetectorResponseTypeDef",
    "DescribeDetectorResponseTypeDef",
    "DetectorStateDefinitionTypeDef",
    "DetectorStateSummaryTypeDef",
    "DetectorStateTypeDef",
    "DetectorSummaryTypeDef",
    "DetectorTypeDef",
    "ListDetectorsResponseTypeDef",
    "MessageTypeDef",
    "TimerDefinitionTypeDef",
    "TimerTypeDef",
    "UpdateDetectorRequestTypeDef",
    "VariableDefinitionTypeDef",
    "VariableTypeDef",
)


class BatchPutMessageErrorEntryTypeDef(TypedDict, total=False):
    messageId: str
    errorCode: ErrorCode
    errorMessage: str


class BatchPutMessageResponseTypeDef(TypedDict, total=False):
    BatchPutMessageErrorEntries: List["BatchPutMessageErrorEntryTypeDef"]


class BatchUpdateDetectorErrorEntryTypeDef(TypedDict, total=False):
    messageId: str
    errorCode: ErrorCode
    errorMessage: str


class BatchUpdateDetectorResponseTypeDef(TypedDict, total=False):
    batchUpdateDetectorErrorEntries: List["BatchUpdateDetectorErrorEntryTypeDef"]


class DescribeDetectorResponseTypeDef(TypedDict, total=False):
    detector: "DetectorTypeDef"


class DetectorStateDefinitionTypeDef(TypedDict):
    stateName: str
    variables: List["VariableDefinitionTypeDef"]
    timers: List["TimerDefinitionTypeDef"]


class DetectorStateSummaryTypeDef(TypedDict, total=False):
    stateName: str


class DetectorStateTypeDef(TypedDict):
    stateName: str
    variables: List["VariableTypeDef"]
    timers: List["TimerTypeDef"]


class DetectorSummaryTypeDef(TypedDict, total=False):
    detectorModelName: str
    keyValue: str
    detectorModelVersion: str
    state: "DetectorStateSummaryTypeDef"
    creationTime: datetime
    lastUpdateTime: datetime


class DetectorTypeDef(TypedDict, total=False):
    detectorModelName: str
    keyValue: str
    detectorModelVersion: str
    state: "DetectorStateTypeDef"
    creationTime: datetime
    lastUpdateTime: datetime


class ListDetectorsResponseTypeDef(TypedDict, total=False):
    detectorSummaries: List["DetectorSummaryTypeDef"]
    nextToken: str


class MessageTypeDef(TypedDict):
    messageId: str
    inputName: str
    payload: Union[bytes, IO[bytes]]


class TimerDefinitionTypeDef(TypedDict):
    name: str
    seconds: int


class TimerTypeDef(TypedDict):
    name: str
    timestamp: datetime


class _RequiredUpdateDetectorRequestTypeDef(TypedDict):
    messageId: str
    detectorModelName: str
    state: "DetectorStateDefinitionTypeDef"


class UpdateDetectorRequestTypeDef(_RequiredUpdateDetectorRequestTypeDef, total=False):
    keyValue: str


class VariableDefinitionTypeDef(TypedDict):
    name: str
    value: str


class VariableTypeDef(TypedDict):
    name: str
    value: str
