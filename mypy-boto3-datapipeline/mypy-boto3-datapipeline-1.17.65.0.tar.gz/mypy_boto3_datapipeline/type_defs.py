"""
Type annotations for datapipeline service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_datapipeline/type_defs.html)

Usage::

    ```python
    from mypy_boto3_datapipeline.type_defs import CreatePipelineOutputTypeDef

    data: CreatePipelineOutputTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from mypy_boto3_datapipeline.literals import OperatorType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreatePipelineOutputTypeDef",
    "DescribeObjectsOutputTypeDef",
    "DescribePipelinesOutputTypeDef",
    "EvaluateExpressionOutputTypeDef",
    "FieldTypeDef",
    "GetPipelineDefinitionOutputTypeDef",
    "InstanceIdentityTypeDef",
    "ListPipelinesOutputTypeDef",
    "OperatorTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterAttributeTypeDef",
    "ParameterObjectTypeDef",
    "ParameterValueTypeDef",
    "PipelineDescriptionTypeDef",
    "PipelineIdNameTypeDef",
    "PipelineObjectTypeDef",
    "PollForTaskOutputTypeDef",
    "PutPipelineDefinitionOutputTypeDef",
    "QueryObjectsOutputTypeDef",
    "QueryTypeDef",
    "ReportTaskProgressOutputTypeDef",
    "ReportTaskRunnerHeartbeatOutputTypeDef",
    "ResponseMetadata",
    "SelectorTypeDef",
    "TagTypeDef",
    "TaskObjectTypeDef",
    "ValidatePipelineDefinitionOutputTypeDef",
    "ValidationErrorTypeDef",
    "ValidationWarningTypeDef",
)


class CreatePipelineOutputTypeDef(TypedDict):
    pipelineId: str
    ResponseMetadata: "ResponseMetadata"


class DescribeObjectsOutputTypeDef(TypedDict):
    pipelineObjects: List["PipelineObjectTypeDef"]
    marker: str
    hasMoreResults: bool
    ResponseMetadata: "ResponseMetadata"


class DescribePipelinesOutputTypeDef(TypedDict):
    pipelineDescriptionList: List["PipelineDescriptionTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class EvaluateExpressionOutputTypeDef(TypedDict):
    evaluatedExpression: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredFieldTypeDef(TypedDict):
    key: str


class FieldTypeDef(_RequiredFieldTypeDef, total=False):
    stringValue: str
    refValue: str


class GetPipelineDefinitionOutputTypeDef(TypedDict):
    pipelineObjects: List["PipelineObjectTypeDef"]
    parameterObjects: List["ParameterObjectTypeDef"]
    parameterValues: List["ParameterValueTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class InstanceIdentityTypeDef(TypedDict, total=False):
    document: str
    signature: str


class ListPipelinesOutputTypeDef(TypedDict):
    pipelineIdList: List["PipelineIdNameTypeDef"]
    marker: str
    hasMoreResults: bool
    ResponseMetadata: "ResponseMetadata"


OperatorTypeDef = TypedDict(
    "OperatorTypeDef", {"type": OperatorType, "values": List[str]}, total=False
)


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParameterAttributeTypeDef(TypedDict):
    key: str
    stringValue: str


ParameterObjectTypeDef = TypedDict(
    "ParameterObjectTypeDef", {"id": str, "attributes": List["ParameterAttributeTypeDef"]}
)

ParameterValueTypeDef = TypedDict("ParameterValueTypeDef", {"id": str, "stringValue": str})


class _RequiredPipelineDescriptionTypeDef(TypedDict):
    pipelineId: str
    name: str
    fields: List["FieldTypeDef"]


class PipelineDescriptionTypeDef(_RequiredPipelineDescriptionTypeDef, total=False):
    description: str
    tags: List["TagTypeDef"]


PipelineIdNameTypeDef = TypedDict("PipelineIdNameTypeDef", {"id": str, "name": str}, total=False)

PipelineObjectTypeDef = TypedDict(
    "PipelineObjectTypeDef", {"id": str, "name": str, "fields": List["FieldTypeDef"]}
)


class PollForTaskOutputTypeDef(TypedDict):
    taskObject: "TaskObjectTypeDef"
    ResponseMetadata: "ResponseMetadata"


class PutPipelineDefinitionOutputTypeDef(TypedDict):
    validationErrors: List["ValidationErrorTypeDef"]
    validationWarnings: List["ValidationWarningTypeDef"]
    errored: bool
    ResponseMetadata: "ResponseMetadata"


class QueryObjectsOutputTypeDef(TypedDict):
    ids: List[str]
    marker: str
    hasMoreResults: bool
    ResponseMetadata: "ResponseMetadata"


class QueryTypeDef(TypedDict, total=False):
    selectors: List["SelectorTypeDef"]


class ReportTaskProgressOutputTypeDef(TypedDict):
    canceled: bool
    ResponseMetadata: "ResponseMetadata"


class ReportTaskRunnerHeartbeatOutputTypeDef(TypedDict):
    terminate: bool
    ResponseMetadata: "ResponseMetadata"


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


SelectorTypeDef = TypedDict(
    "SelectorTypeDef", {"fieldName": str, "operator": "OperatorTypeDef"}, total=False
)


class TagTypeDef(TypedDict):
    key: str
    value: str


class TaskObjectTypeDef(TypedDict, total=False):
    taskId: str
    pipelineId: str
    attemptId: str
    objects: Dict[str, "PipelineObjectTypeDef"]


class ValidatePipelineDefinitionOutputTypeDef(TypedDict):
    validationErrors: List["ValidationErrorTypeDef"]
    validationWarnings: List["ValidationWarningTypeDef"]
    errored: bool
    ResponseMetadata: "ResponseMetadata"


ValidationErrorTypeDef = TypedDict(
    "ValidationErrorTypeDef", {"id": str, "errors": List[str]}, total=False
)

ValidationWarningTypeDef = TypedDict(
    "ValidationWarningTypeDef", {"id": str, "warnings": List[str]}, total=False
)
