"""
Type annotations for fis service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_fis/type_defs.html)

Usage::

    ```python
    from mypy_boto3_fis.type_defs import ActionParameterTypeDef

    data: ActionParameterTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_fis.literals import ExperimentActionStatus, ExperimentStatus

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionParameterTypeDef",
    "ActionSummaryTypeDef",
    "ActionTargetTypeDef",
    "ActionTypeDef",
    "CreateExperimentTemplateActionInputTypeDef",
    "CreateExperimentTemplateResponseTypeDef",
    "CreateExperimentTemplateStopConditionInputTypeDef",
    "CreateExperimentTemplateTargetInputTypeDef",
    "DeleteExperimentTemplateResponseTypeDef",
    "ExperimentActionStateTypeDef",
    "ExperimentActionTypeDef",
    "ExperimentStateTypeDef",
    "ExperimentStopConditionTypeDef",
    "ExperimentSummaryTypeDef",
    "ExperimentTargetFilterTypeDef",
    "ExperimentTargetTypeDef",
    "ExperimentTemplateActionTypeDef",
    "ExperimentTemplateStopConditionTypeDef",
    "ExperimentTemplateSummaryTypeDef",
    "ExperimentTemplateTargetFilterTypeDef",
    "ExperimentTemplateTargetInputFilterTypeDef",
    "ExperimentTemplateTargetTypeDef",
    "ExperimentTemplateTypeDef",
    "ExperimentTypeDef",
    "GetActionResponseTypeDef",
    "GetExperimentResponseTypeDef",
    "GetExperimentTemplateResponseTypeDef",
    "ListActionsResponseTypeDef",
    "ListExperimentTemplatesResponseTypeDef",
    "ListExperimentsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartExperimentResponseTypeDef",
    "StopExperimentResponseTypeDef",
    "UpdateExperimentTemplateActionInputItemTypeDef",
    "UpdateExperimentTemplateResponseTypeDef",
    "UpdateExperimentTemplateStopConditionInputTypeDef",
    "UpdateExperimentTemplateTargetInputTypeDef",
)


class ActionParameterTypeDef(TypedDict, total=False):
    description: str
    required: bool


ActionSummaryTypeDef = TypedDict(
    "ActionSummaryTypeDef",
    {
        "id": str,
        "description": str,
        "targets": Dict[str, "ActionTargetTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)


class ActionTargetTypeDef(TypedDict, total=False):
    resourceType: str


ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "id": str,
        "description": str,
        "parameters": Dict[str, "ActionParameterTypeDef"],
        "targets": Dict[str, "ActionTargetTypeDef"],
        "tags": Dict[str, str],
    },
    total=False,
)


class _RequiredCreateExperimentTemplateActionInputTypeDef(TypedDict):
    actionId: str


class CreateExperimentTemplateActionInputTypeDef(
    _RequiredCreateExperimentTemplateActionInputTypeDef, total=False
):
    description: str
    parameters: Dict[str, str]
    targets: Dict[str, str]
    startAfter: List[str]


class CreateExperimentTemplateResponseTypeDef(TypedDict, total=False):
    experimentTemplate: "ExperimentTemplateTypeDef"


class _RequiredCreateExperimentTemplateStopConditionInputTypeDef(TypedDict):
    source: str


class CreateExperimentTemplateStopConditionInputTypeDef(
    _RequiredCreateExperimentTemplateStopConditionInputTypeDef, total=False
):
    value: str


class _RequiredCreateExperimentTemplateTargetInputTypeDef(TypedDict):
    resourceType: str
    selectionMode: str


class CreateExperimentTemplateTargetInputTypeDef(
    _RequiredCreateExperimentTemplateTargetInputTypeDef, total=False
):
    resourceArns: List[str]
    resourceTags: Dict[str, str]
    filters: List["ExperimentTemplateTargetInputFilterTypeDef"]


class DeleteExperimentTemplateResponseTypeDef(TypedDict, total=False):
    experimentTemplate: "ExperimentTemplateTypeDef"


class ExperimentActionStateTypeDef(TypedDict, total=False):
    status: ExperimentActionStatus
    reason: str


class ExperimentActionTypeDef(TypedDict, total=False):
    actionId: str
    description: str
    parameters: Dict[str, str]
    targets: Dict[str, str]
    startAfter: List[str]
    state: "ExperimentActionStateTypeDef"


class ExperimentStateTypeDef(TypedDict, total=False):
    status: ExperimentStatus
    reason: str


class ExperimentStopConditionTypeDef(TypedDict, total=False):
    source: str
    value: str


ExperimentSummaryTypeDef = TypedDict(
    "ExperimentSummaryTypeDef",
    {
        "id": str,
        "experimentTemplateId": str,
        "state": "ExperimentStateTypeDef",
        "creationTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ExperimentTargetFilterTypeDef(TypedDict, total=False):
    path: str
    values: List[str]


class ExperimentTargetTypeDef(TypedDict, total=False):
    resourceType: str
    resourceArns: List[str]
    resourceTags: Dict[str, str]
    filters: List["ExperimentTargetFilterTypeDef"]
    selectionMode: str


class ExperimentTemplateActionTypeDef(TypedDict, total=False):
    actionId: str
    description: str
    parameters: Dict[str, str]
    targets: Dict[str, str]
    startAfter: List[str]


class ExperimentTemplateStopConditionTypeDef(TypedDict, total=False):
    source: str
    value: str


ExperimentTemplateSummaryTypeDef = TypedDict(
    "ExperimentTemplateSummaryTypeDef",
    {
        "id": str,
        "description": str,
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class ExperimentTemplateTargetFilterTypeDef(TypedDict, total=False):
    path: str
    values: List[str]


class ExperimentTemplateTargetInputFilterTypeDef(TypedDict):
    path: str
    values: List[str]


class ExperimentTemplateTargetTypeDef(TypedDict, total=False):
    resourceType: str
    resourceArns: List[str]
    resourceTags: Dict[str, str]
    filters: List["ExperimentTemplateTargetFilterTypeDef"]
    selectionMode: str


ExperimentTemplateTypeDef = TypedDict(
    "ExperimentTemplateTypeDef",
    {
        "id": str,
        "description": str,
        "targets": Dict[str, "ExperimentTemplateTargetTypeDef"],
        "actions": Dict[str, "ExperimentTemplateActionTypeDef"],
        "stopConditions": List["ExperimentTemplateStopConditionTypeDef"],
        "creationTime": datetime,
        "lastUpdateTime": datetime,
        "roleArn": str,
        "tags": Dict[str, str],
    },
    total=False,
)

ExperimentTypeDef = TypedDict(
    "ExperimentTypeDef",
    {
        "id": str,
        "experimentTemplateId": str,
        "roleArn": str,
        "state": "ExperimentStateTypeDef",
        "targets": Dict[str, "ExperimentTargetTypeDef"],
        "actions": Dict[str, "ExperimentActionTypeDef"],
        "stopConditions": List["ExperimentStopConditionTypeDef"],
        "creationTime": datetime,
        "startTime": datetime,
        "endTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)


class GetActionResponseTypeDef(TypedDict, total=False):
    action: "ActionTypeDef"


class GetExperimentResponseTypeDef(TypedDict, total=False):
    experiment: "ExperimentTypeDef"


class GetExperimentTemplateResponseTypeDef(TypedDict, total=False):
    experimentTemplate: "ExperimentTemplateTypeDef"


class ListActionsResponseTypeDef(TypedDict, total=False):
    actions: List["ActionSummaryTypeDef"]
    nextToken: str


class ListExperimentTemplatesResponseTypeDef(TypedDict, total=False):
    experimentTemplates: List["ExperimentTemplateSummaryTypeDef"]
    nextToken: str


class ListExperimentsResponseTypeDef(TypedDict, total=False):
    experiments: List["ExperimentSummaryTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class StartExperimentResponseTypeDef(TypedDict, total=False):
    experiment: "ExperimentTypeDef"


class StopExperimentResponseTypeDef(TypedDict, total=False):
    experiment: "ExperimentTypeDef"


class UpdateExperimentTemplateActionInputItemTypeDef(TypedDict, total=False):
    actionId: str
    description: str
    parameters: Dict[str, str]
    targets: Dict[str, str]
    startAfter: List[str]


class UpdateExperimentTemplateResponseTypeDef(TypedDict, total=False):
    experimentTemplate: "ExperimentTemplateTypeDef"


class _RequiredUpdateExperimentTemplateStopConditionInputTypeDef(TypedDict):
    source: str


class UpdateExperimentTemplateStopConditionInputTypeDef(
    _RequiredUpdateExperimentTemplateStopConditionInputTypeDef, total=False
):
    value: str


class _RequiredUpdateExperimentTemplateTargetInputTypeDef(TypedDict):
    resourceType: str
    selectionMode: str


class UpdateExperimentTemplateTargetInputTypeDef(
    _RequiredUpdateExperimentTemplateTargetInputTypeDef, total=False
):
    resourceArns: List[str]
    resourceTags: Dict[str, str]
    filters: List["ExperimentTemplateTargetInputFilterTypeDef"]
