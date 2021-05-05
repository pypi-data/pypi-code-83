"""
Type annotations for swf service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/type_defs.html)

Usage::

    ```python
    from mypy_boto3_swf.type_defs import ActivityTaskCancelRequestedEventAttributesTypeDef

    data: ActivityTaskCancelRequestedEventAttributesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_swf.literals import (
    ActivityTaskTimeoutType,
    CancelTimerFailedCause,
    CancelWorkflowExecutionFailedCause,
    ChildPolicy,
    CloseStatus,
    CompleteWorkflowExecutionFailedCause,
    ContinueAsNewWorkflowExecutionFailedCause,
    DecisionType,
    EventType,
    ExecutionStatus,
    FailWorkflowExecutionFailedCause,
    RegistrationStatus,
    RequestCancelActivityTaskFailedCause,
    RequestCancelExternalWorkflowExecutionFailedCause,
    ScheduleActivityTaskFailedCause,
    ScheduleLambdaFunctionFailedCause,
    SignalExternalWorkflowExecutionFailedCause,
    StartChildWorkflowExecutionFailedCause,
    StartTimerFailedCause,
    WorkflowExecutionTerminatedCause,
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
    "ActivityTaskCancelRequestedEventAttributesTypeDef",
    "ActivityTaskCanceledEventAttributesTypeDef",
    "ActivityTaskCompletedEventAttributesTypeDef",
    "ActivityTaskFailedEventAttributesTypeDef",
    "ActivityTaskScheduledEventAttributesTypeDef",
    "ActivityTaskStartedEventAttributesTypeDef",
    "ActivityTaskStatusTypeDef",
    "ActivityTaskTimedOutEventAttributesTypeDef",
    "ActivityTaskTypeDef",
    "ActivityTypeConfigurationTypeDef",
    "ActivityTypeDetailTypeDef",
    "ActivityTypeInfoTypeDef",
    "ActivityTypeInfosTypeDef",
    "ActivityTypeTypeDef",
    "CancelTimerDecisionAttributesTypeDef",
    "CancelTimerFailedEventAttributesTypeDef",
    "CancelWorkflowExecutionDecisionAttributesTypeDef",
    "CancelWorkflowExecutionFailedEventAttributesTypeDef",
    "ChildWorkflowExecutionCanceledEventAttributesTypeDef",
    "ChildWorkflowExecutionCompletedEventAttributesTypeDef",
    "ChildWorkflowExecutionFailedEventAttributesTypeDef",
    "ChildWorkflowExecutionStartedEventAttributesTypeDef",
    "ChildWorkflowExecutionTerminatedEventAttributesTypeDef",
    "ChildWorkflowExecutionTimedOutEventAttributesTypeDef",
    "CloseStatusFilterTypeDef",
    "CompleteWorkflowExecutionDecisionAttributesTypeDef",
    "CompleteWorkflowExecutionFailedEventAttributesTypeDef",
    "ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef",
    "ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef",
    "DecisionTaskCompletedEventAttributesTypeDef",
    "DecisionTaskScheduledEventAttributesTypeDef",
    "DecisionTaskStartedEventAttributesTypeDef",
    "DecisionTaskTimedOutEventAttributesTypeDef",
    "DecisionTaskTypeDef",
    "DecisionTypeDef",
    "DomainConfigurationTypeDef",
    "DomainDetailTypeDef",
    "DomainInfoTypeDef",
    "DomainInfosTypeDef",
    "ExecutionTimeFilterTypeDef",
    "ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef",
    "ExternalWorkflowExecutionSignaledEventAttributesTypeDef",
    "FailWorkflowExecutionDecisionAttributesTypeDef",
    "FailWorkflowExecutionFailedEventAttributesTypeDef",
    "HistoryEventTypeDef",
    "HistoryTypeDef",
    "LambdaFunctionCompletedEventAttributesTypeDef",
    "LambdaFunctionFailedEventAttributesTypeDef",
    "LambdaFunctionScheduledEventAttributesTypeDef",
    "LambdaFunctionStartedEventAttributesTypeDef",
    "LambdaFunctionTimedOutEventAttributesTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "MarkerRecordedEventAttributesTypeDef",
    "PaginatorConfigTypeDef",
    "PendingTaskCountTypeDef",
    "RecordMarkerDecisionAttributesTypeDef",
    "RecordMarkerFailedEventAttributesTypeDef",
    "RequestCancelActivityTaskDecisionAttributesTypeDef",
    "RequestCancelActivityTaskFailedEventAttributesTypeDef",
    "RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef",
    "RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef",
    "RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    "ResourceTagTypeDef",
    "ResponseMetadata",
    "RunTypeDef",
    "ScheduleActivityTaskDecisionAttributesTypeDef",
    "ScheduleActivityTaskFailedEventAttributesTypeDef",
    "ScheduleLambdaFunctionDecisionAttributesTypeDef",
    "ScheduleLambdaFunctionFailedEventAttributesTypeDef",
    "SignalExternalWorkflowExecutionDecisionAttributesTypeDef",
    "SignalExternalWorkflowExecutionFailedEventAttributesTypeDef",
    "SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    "StartChildWorkflowExecutionDecisionAttributesTypeDef",
    "StartChildWorkflowExecutionFailedEventAttributesTypeDef",
    "StartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    "StartLambdaFunctionFailedEventAttributesTypeDef",
    "StartTimerDecisionAttributesTypeDef",
    "StartTimerFailedEventAttributesTypeDef",
    "TagFilterTypeDef",
    "TaskListTypeDef",
    "TimerCanceledEventAttributesTypeDef",
    "TimerFiredEventAttributesTypeDef",
    "TimerStartedEventAttributesTypeDef",
    "WorkflowExecutionCancelRequestedEventAttributesTypeDef",
    "WorkflowExecutionCanceledEventAttributesTypeDef",
    "WorkflowExecutionCompletedEventAttributesTypeDef",
    "WorkflowExecutionConfigurationTypeDef",
    "WorkflowExecutionContinuedAsNewEventAttributesTypeDef",
    "WorkflowExecutionCountTypeDef",
    "WorkflowExecutionDetailTypeDef",
    "WorkflowExecutionFailedEventAttributesTypeDef",
    "WorkflowExecutionFilterTypeDef",
    "WorkflowExecutionInfoTypeDef",
    "WorkflowExecutionInfosTypeDef",
    "WorkflowExecutionOpenCountsTypeDef",
    "WorkflowExecutionSignaledEventAttributesTypeDef",
    "WorkflowExecutionStartedEventAttributesTypeDef",
    "WorkflowExecutionTerminatedEventAttributesTypeDef",
    "WorkflowExecutionTimedOutEventAttributesTypeDef",
    "WorkflowExecutionTypeDef",
    "WorkflowTypeConfigurationTypeDef",
    "WorkflowTypeDetailTypeDef",
    "WorkflowTypeFilterTypeDef",
    "WorkflowTypeInfoTypeDef",
    "WorkflowTypeInfosTypeDef",
    "WorkflowTypeTypeDef",
)


class ActivityTaskCancelRequestedEventAttributesTypeDef(TypedDict):
    decisionTaskCompletedEventId: int
    activityId: str


class _RequiredActivityTaskCanceledEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    startedEventId: int


class ActivityTaskCanceledEventAttributesTypeDef(
    _RequiredActivityTaskCanceledEventAttributesTypeDef, total=False
):
    details: str
    latestCancelRequestedEventId: int


class _RequiredActivityTaskCompletedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    startedEventId: int


class ActivityTaskCompletedEventAttributesTypeDef(
    _RequiredActivityTaskCompletedEventAttributesTypeDef, total=False
):
    result: str


class _RequiredActivityTaskFailedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    startedEventId: int


class ActivityTaskFailedEventAttributesTypeDef(
    _RequiredActivityTaskFailedEventAttributesTypeDef, total=False
):
    reason: str
    details: str


_RequiredActivityTaskScheduledEventAttributesTypeDef = TypedDict(
    "_RequiredActivityTaskScheduledEventAttributesTypeDef",
    {
        "activityType": "ActivityTypeTypeDef",
        "activityId": str,
        "taskList": "TaskListTypeDef",
        "decisionTaskCompletedEventId": int,
    },
)
_OptionalActivityTaskScheduledEventAttributesTypeDef = TypedDict(
    "_OptionalActivityTaskScheduledEventAttributesTypeDef",
    {
        "input": str,
        "control": str,
        "scheduleToStartTimeout": str,
        "scheduleToCloseTimeout": str,
        "startToCloseTimeout": str,
        "taskPriority": str,
        "heartbeatTimeout": str,
    },
    total=False,
)


class ActivityTaskScheduledEventAttributesTypeDef(
    _RequiredActivityTaskScheduledEventAttributesTypeDef,
    _OptionalActivityTaskScheduledEventAttributesTypeDef,
):
    pass


class _RequiredActivityTaskStartedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int


class ActivityTaskStartedEventAttributesTypeDef(
    _RequiredActivityTaskStartedEventAttributesTypeDef, total=False
):
    identity: str


class ActivityTaskStatusTypeDef(TypedDict):
    cancelRequested: bool


class _RequiredActivityTaskTimedOutEventAttributesTypeDef(TypedDict):
    timeoutType: ActivityTaskTimeoutType
    scheduledEventId: int
    startedEventId: int


class ActivityTaskTimedOutEventAttributesTypeDef(
    _RequiredActivityTaskTimedOutEventAttributesTypeDef, total=False
):
    details: str


_RequiredActivityTaskTypeDef = TypedDict(
    "_RequiredActivityTaskTypeDef",
    {
        "taskToken": str,
        "activityId": str,
        "startedEventId": int,
        "workflowExecution": "WorkflowExecutionTypeDef",
        "activityType": "ActivityTypeTypeDef",
    },
)
_OptionalActivityTaskTypeDef = TypedDict(
    "_OptionalActivityTaskTypeDef", {"input": str}, total=False
)


class ActivityTaskTypeDef(_RequiredActivityTaskTypeDef, _OptionalActivityTaskTypeDef):
    pass


class ActivityTypeConfigurationTypeDef(TypedDict, total=False):
    defaultTaskStartToCloseTimeout: str
    defaultTaskHeartbeatTimeout: str
    defaultTaskList: "TaskListTypeDef"
    defaultTaskPriority: str
    defaultTaskScheduleToStartTimeout: str
    defaultTaskScheduleToCloseTimeout: str


class ActivityTypeDetailTypeDef(TypedDict):
    typeInfo: "ActivityTypeInfoTypeDef"
    configuration: "ActivityTypeConfigurationTypeDef"


class _RequiredActivityTypeInfoTypeDef(TypedDict):
    activityType: "ActivityTypeTypeDef"
    status: RegistrationStatus
    creationDate: datetime


class ActivityTypeInfoTypeDef(_RequiredActivityTypeInfoTypeDef, total=False):
    description: str
    deprecationDate: datetime


class _RequiredActivityTypeInfosTypeDef(TypedDict):
    typeInfos: List["ActivityTypeInfoTypeDef"]


class ActivityTypeInfosTypeDef(_RequiredActivityTypeInfosTypeDef, total=False):
    nextPageToken: str


class ActivityTypeTypeDef(TypedDict):
    name: str
    version: str


class CancelTimerDecisionAttributesTypeDef(TypedDict):
    timerId: str


class CancelTimerFailedEventAttributesTypeDef(TypedDict):
    timerId: str
    cause: CancelTimerFailedCause
    decisionTaskCompletedEventId: int


class CancelWorkflowExecutionDecisionAttributesTypeDef(TypedDict, total=False):
    details: str


class CancelWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    cause: CancelWorkflowExecutionFailedCause
    decisionTaskCompletedEventId: int


class _RequiredChildWorkflowExecutionCanceledEventAttributesTypeDef(TypedDict):
    workflowExecution: "WorkflowExecutionTypeDef"
    workflowType: "WorkflowTypeTypeDef"
    initiatedEventId: int
    startedEventId: int


class ChildWorkflowExecutionCanceledEventAttributesTypeDef(
    _RequiredChildWorkflowExecutionCanceledEventAttributesTypeDef, total=False
):
    details: str


class _RequiredChildWorkflowExecutionCompletedEventAttributesTypeDef(TypedDict):
    workflowExecution: "WorkflowExecutionTypeDef"
    workflowType: "WorkflowTypeTypeDef"
    initiatedEventId: int
    startedEventId: int


class ChildWorkflowExecutionCompletedEventAttributesTypeDef(
    _RequiredChildWorkflowExecutionCompletedEventAttributesTypeDef, total=False
):
    result: str


class _RequiredChildWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    workflowExecution: "WorkflowExecutionTypeDef"
    workflowType: "WorkflowTypeTypeDef"
    initiatedEventId: int
    startedEventId: int


class ChildWorkflowExecutionFailedEventAttributesTypeDef(
    _RequiredChildWorkflowExecutionFailedEventAttributesTypeDef, total=False
):
    reason: str
    details: str


class ChildWorkflowExecutionStartedEventAttributesTypeDef(TypedDict):
    workflowExecution: "WorkflowExecutionTypeDef"
    workflowType: "WorkflowTypeTypeDef"
    initiatedEventId: int


class ChildWorkflowExecutionTerminatedEventAttributesTypeDef(TypedDict):
    workflowExecution: "WorkflowExecutionTypeDef"
    workflowType: "WorkflowTypeTypeDef"
    initiatedEventId: int
    startedEventId: int


class ChildWorkflowExecutionTimedOutEventAttributesTypeDef(TypedDict):
    workflowExecution: "WorkflowExecutionTypeDef"
    workflowType: "WorkflowTypeTypeDef"
    timeoutType: Literal["START_TO_CLOSE"]
    initiatedEventId: int
    startedEventId: int


class CloseStatusFilterTypeDef(TypedDict):
    status: CloseStatus


class CompleteWorkflowExecutionDecisionAttributesTypeDef(TypedDict, total=False):
    result: str


class CompleteWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    cause: CompleteWorkflowExecutionFailedCause
    decisionTaskCompletedEventId: int


ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskList": "TaskListTypeDef",
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": ChildPolicy,
        "tagList": List[str],
        "workflowTypeVersion": str,
        "lambdaRole": str,
    },
    total=False,
)


class ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    cause: ContinueAsNewWorkflowExecutionFailedCause
    decisionTaskCompletedEventId: int


class _RequiredDecisionTaskCompletedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    startedEventId: int


class DecisionTaskCompletedEventAttributesTypeDef(
    _RequiredDecisionTaskCompletedEventAttributesTypeDef, total=False
):
    executionContext: str


class _RequiredDecisionTaskScheduledEventAttributesTypeDef(TypedDict):
    taskList: "TaskListTypeDef"


class DecisionTaskScheduledEventAttributesTypeDef(
    _RequiredDecisionTaskScheduledEventAttributesTypeDef, total=False
):
    taskPriority: str
    startToCloseTimeout: str


class _RequiredDecisionTaskStartedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int


class DecisionTaskStartedEventAttributesTypeDef(
    _RequiredDecisionTaskStartedEventAttributesTypeDef, total=False
):
    identity: str


class DecisionTaskTimedOutEventAttributesTypeDef(TypedDict):
    timeoutType: Literal["START_TO_CLOSE"]
    scheduledEventId: int
    startedEventId: int


class _RequiredDecisionTaskTypeDef(TypedDict):
    taskToken: str
    startedEventId: int
    workflowExecution: "WorkflowExecutionTypeDef"
    workflowType: "WorkflowTypeTypeDef"
    events: List["HistoryEventTypeDef"]


class DecisionTaskTypeDef(_RequiredDecisionTaskTypeDef, total=False):
    nextPageToken: str
    previousStartedEventId: int


class _RequiredDecisionTypeDef(TypedDict):
    decisionType: DecisionType


class DecisionTypeDef(_RequiredDecisionTypeDef, total=False):
    scheduleActivityTaskDecisionAttributes: "ScheduleActivityTaskDecisionAttributesTypeDef"
    requestCancelActivityTaskDecisionAttributes: "RequestCancelActivityTaskDecisionAttributesTypeDef"
    completeWorkflowExecutionDecisionAttributes: "CompleteWorkflowExecutionDecisionAttributesTypeDef"
    failWorkflowExecutionDecisionAttributes: "FailWorkflowExecutionDecisionAttributesTypeDef"
    cancelWorkflowExecutionDecisionAttributes: "CancelWorkflowExecutionDecisionAttributesTypeDef"
    continueAsNewWorkflowExecutionDecisionAttributes: "ContinueAsNewWorkflowExecutionDecisionAttributesTypeDef"
    recordMarkerDecisionAttributes: "RecordMarkerDecisionAttributesTypeDef"
    startTimerDecisionAttributes: "StartTimerDecisionAttributesTypeDef"
    cancelTimerDecisionAttributes: "CancelTimerDecisionAttributesTypeDef"
    signalExternalWorkflowExecutionDecisionAttributes: "SignalExternalWorkflowExecutionDecisionAttributesTypeDef"
    requestCancelExternalWorkflowExecutionDecisionAttributes: "RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef"
    startChildWorkflowExecutionDecisionAttributes: "StartChildWorkflowExecutionDecisionAttributesTypeDef"
    scheduleLambdaFunctionDecisionAttributes: "ScheduleLambdaFunctionDecisionAttributesTypeDef"


class DomainConfigurationTypeDef(TypedDict):
    workflowExecutionRetentionPeriodInDays: str


class DomainDetailTypeDef(TypedDict):
    domainInfo: "DomainInfoTypeDef"
    configuration: "DomainConfigurationTypeDef"


class _RequiredDomainInfoTypeDef(TypedDict):
    name: str
    status: RegistrationStatus


class DomainInfoTypeDef(_RequiredDomainInfoTypeDef, total=False):
    description: str
    arn: str


class _RequiredDomainInfosTypeDef(TypedDict):
    domainInfos: List["DomainInfoTypeDef"]


class DomainInfosTypeDef(_RequiredDomainInfosTypeDef, total=False):
    nextPageToken: str


class _RequiredExecutionTimeFilterTypeDef(TypedDict):
    oldestDate: datetime


class ExecutionTimeFilterTypeDef(_RequiredExecutionTimeFilterTypeDef, total=False):
    latestDate: datetime


class ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef(TypedDict):
    workflowExecution: "WorkflowExecutionTypeDef"
    initiatedEventId: int


class ExternalWorkflowExecutionSignaledEventAttributesTypeDef(TypedDict):
    workflowExecution: "WorkflowExecutionTypeDef"
    initiatedEventId: int


class FailWorkflowExecutionDecisionAttributesTypeDef(TypedDict, total=False):
    reason: str
    details: str


class FailWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    cause: FailWorkflowExecutionFailedCause
    decisionTaskCompletedEventId: int


class _RequiredHistoryEventTypeDef(TypedDict):
    eventTimestamp: datetime
    eventType: EventType
    eventId: int


class HistoryEventTypeDef(_RequiredHistoryEventTypeDef, total=False):
    workflowExecutionStartedEventAttributes: "WorkflowExecutionStartedEventAttributesTypeDef"
    workflowExecutionCompletedEventAttributes: "WorkflowExecutionCompletedEventAttributesTypeDef"
    completeWorkflowExecutionFailedEventAttributes: "CompleteWorkflowExecutionFailedEventAttributesTypeDef"
    workflowExecutionFailedEventAttributes: "WorkflowExecutionFailedEventAttributesTypeDef"
    failWorkflowExecutionFailedEventAttributes: "FailWorkflowExecutionFailedEventAttributesTypeDef"
    workflowExecutionTimedOutEventAttributes: "WorkflowExecutionTimedOutEventAttributesTypeDef"
    workflowExecutionCanceledEventAttributes: "WorkflowExecutionCanceledEventAttributesTypeDef"
    cancelWorkflowExecutionFailedEventAttributes: "CancelWorkflowExecutionFailedEventAttributesTypeDef"
    workflowExecutionContinuedAsNewEventAttributes: "WorkflowExecutionContinuedAsNewEventAttributesTypeDef"
    continueAsNewWorkflowExecutionFailedEventAttributes: "ContinueAsNewWorkflowExecutionFailedEventAttributesTypeDef"
    workflowExecutionTerminatedEventAttributes: "WorkflowExecutionTerminatedEventAttributesTypeDef"
    workflowExecutionCancelRequestedEventAttributes: "WorkflowExecutionCancelRequestedEventAttributesTypeDef"
    decisionTaskScheduledEventAttributes: "DecisionTaskScheduledEventAttributesTypeDef"
    decisionTaskStartedEventAttributes: "DecisionTaskStartedEventAttributesTypeDef"
    decisionTaskCompletedEventAttributes: "DecisionTaskCompletedEventAttributesTypeDef"
    decisionTaskTimedOutEventAttributes: "DecisionTaskTimedOutEventAttributesTypeDef"
    activityTaskScheduledEventAttributes: "ActivityTaskScheduledEventAttributesTypeDef"
    activityTaskStartedEventAttributes: "ActivityTaskStartedEventAttributesTypeDef"
    activityTaskCompletedEventAttributes: "ActivityTaskCompletedEventAttributesTypeDef"
    activityTaskFailedEventAttributes: "ActivityTaskFailedEventAttributesTypeDef"
    activityTaskTimedOutEventAttributes: "ActivityTaskTimedOutEventAttributesTypeDef"
    activityTaskCanceledEventAttributes: "ActivityTaskCanceledEventAttributesTypeDef"
    activityTaskCancelRequestedEventAttributes: "ActivityTaskCancelRequestedEventAttributesTypeDef"
    workflowExecutionSignaledEventAttributes: "WorkflowExecutionSignaledEventAttributesTypeDef"
    markerRecordedEventAttributes: "MarkerRecordedEventAttributesTypeDef"
    recordMarkerFailedEventAttributes: "RecordMarkerFailedEventAttributesTypeDef"
    timerStartedEventAttributes: "TimerStartedEventAttributesTypeDef"
    timerFiredEventAttributes: "TimerFiredEventAttributesTypeDef"
    timerCanceledEventAttributes: "TimerCanceledEventAttributesTypeDef"
    startChildWorkflowExecutionInitiatedEventAttributes: "StartChildWorkflowExecutionInitiatedEventAttributesTypeDef"
    childWorkflowExecutionStartedEventAttributes: "ChildWorkflowExecutionStartedEventAttributesTypeDef"
    childWorkflowExecutionCompletedEventAttributes: "ChildWorkflowExecutionCompletedEventAttributesTypeDef"
    childWorkflowExecutionFailedEventAttributes: "ChildWorkflowExecutionFailedEventAttributesTypeDef"
    childWorkflowExecutionTimedOutEventAttributes: "ChildWorkflowExecutionTimedOutEventAttributesTypeDef"
    childWorkflowExecutionCanceledEventAttributes: "ChildWorkflowExecutionCanceledEventAttributesTypeDef"
    childWorkflowExecutionTerminatedEventAttributes: "ChildWorkflowExecutionTerminatedEventAttributesTypeDef"
    signalExternalWorkflowExecutionInitiatedEventAttributes: "SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef"
    externalWorkflowExecutionSignaledEventAttributes: "ExternalWorkflowExecutionSignaledEventAttributesTypeDef"
    signalExternalWorkflowExecutionFailedEventAttributes: "SignalExternalWorkflowExecutionFailedEventAttributesTypeDef"
    externalWorkflowExecutionCancelRequestedEventAttributes: "ExternalWorkflowExecutionCancelRequestedEventAttributesTypeDef"
    requestCancelExternalWorkflowExecutionInitiatedEventAttributes: "RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef"
    requestCancelExternalWorkflowExecutionFailedEventAttributes: "RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef"
    scheduleActivityTaskFailedEventAttributes: "ScheduleActivityTaskFailedEventAttributesTypeDef"
    requestCancelActivityTaskFailedEventAttributes: "RequestCancelActivityTaskFailedEventAttributesTypeDef"
    startTimerFailedEventAttributes: "StartTimerFailedEventAttributesTypeDef"
    cancelTimerFailedEventAttributes: "CancelTimerFailedEventAttributesTypeDef"
    startChildWorkflowExecutionFailedEventAttributes: "StartChildWorkflowExecutionFailedEventAttributesTypeDef"
    lambdaFunctionScheduledEventAttributes: "LambdaFunctionScheduledEventAttributesTypeDef"
    lambdaFunctionStartedEventAttributes: "LambdaFunctionStartedEventAttributesTypeDef"
    lambdaFunctionCompletedEventAttributes: "LambdaFunctionCompletedEventAttributesTypeDef"
    lambdaFunctionFailedEventAttributes: "LambdaFunctionFailedEventAttributesTypeDef"
    lambdaFunctionTimedOutEventAttributes: "LambdaFunctionTimedOutEventAttributesTypeDef"
    scheduleLambdaFunctionFailedEventAttributes: "ScheduleLambdaFunctionFailedEventAttributesTypeDef"
    startLambdaFunctionFailedEventAttributes: "StartLambdaFunctionFailedEventAttributesTypeDef"


class _RequiredHistoryTypeDef(TypedDict):
    events: List["HistoryEventTypeDef"]


class HistoryTypeDef(_RequiredHistoryTypeDef, total=False):
    nextPageToken: str


class _RequiredLambdaFunctionCompletedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    startedEventId: int


class LambdaFunctionCompletedEventAttributesTypeDef(
    _RequiredLambdaFunctionCompletedEventAttributesTypeDef, total=False
):
    result: str


class _RequiredLambdaFunctionFailedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    startedEventId: int


class LambdaFunctionFailedEventAttributesTypeDef(
    _RequiredLambdaFunctionFailedEventAttributesTypeDef, total=False
):
    reason: str
    details: str


_RequiredLambdaFunctionScheduledEventAttributesTypeDef = TypedDict(
    "_RequiredLambdaFunctionScheduledEventAttributesTypeDef",
    {"id": str, "name": str, "decisionTaskCompletedEventId": int},
)
_OptionalLambdaFunctionScheduledEventAttributesTypeDef = TypedDict(
    "_OptionalLambdaFunctionScheduledEventAttributesTypeDef",
    {"control": str, "input": str, "startToCloseTimeout": str},
    total=False,
)


class LambdaFunctionScheduledEventAttributesTypeDef(
    _RequiredLambdaFunctionScheduledEventAttributesTypeDef,
    _OptionalLambdaFunctionScheduledEventAttributesTypeDef,
):
    pass


class LambdaFunctionStartedEventAttributesTypeDef(TypedDict):
    scheduledEventId: int


class _RequiredLambdaFunctionTimedOutEventAttributesTypeDef(TypedDict):
    scheduledEventId: int
    startedEventId: int


class LambdaFunctionTimedOutEventAttributesTypeDef(
    _RequiredLambdaFunctionTimedOutEventAttributesTypeDef, total=False
):
    timeoutType: Literal["START_TO_CLOSE"]


class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: List["ResourceTagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class _RequiredMarkerRecordedEventAttributesTypeDef(TypedDict):
    markerName: str
    decisionTaskCompletedEventId: int


class MarkerRecordedEventAttributesTypeDef(
    _RequiredMarkerRecordedEventAttributesTypeDef, total=False
):
    details: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredPendingTaskCountTypeDef(TypedDict):
    count: int


class PendingTaskCountTypeDef(_RequiredPendingTaskCountTypeDef, total=False):
    truncated: bool


class _RequiredRecordMarkerDecisionAttributesTypeDef(TypedDict):
    markerName: str


class RecordMarkerDecisionAttributesTypeDef(
    _RequiredRecordMarkerDecisionAttributesTypeDef, total=False
):
    details: str


class RecordMarkerFailedEventAttributesTypeDef(TypedDict):
    markerName: str
    cause: Literal["OPERATION_NOT_PERMITTED"]
    decisionTaskCompletedEventId: int


class RequestCancelActivityTaskDecisionAttributesTypeDef(TypedDict):
    activityId: str


class RequestCancelActivityTaskFailedEventAttributesTypeDef(TypedDict):
    activityId: str
    cause: RequestCancelActivityTaskFailedCause
    decisionTaskCompletedEventId: int


class _RequiredRequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef(TypedDict):
    workflowId: str


class RequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef(
    _RequiredRequestCancelExternalWorkflowExecutionDecisionAttributesTypeDef, total=False
):
    runId: str
    control: str


class _RequiredRequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    workflowId: str
    cause: RequestCancelExternalWorkflowExecutionFailedCause
    initiatedEventId: int
    decisionTaskCompletedEventId: int


class RequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef(
    _RequiredRequestCancelExternalWorkflowExecutionFailedEventAttributesTypeDef, total=False
):
    runId: str
    control: str


class _RequiredRequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef(TypedDict):
    workflowId: str
    decisionTaskCompletedEventId: int


class RequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef(
    _RequiredRequestCancelExternalWorkflowExecutionInitiatedEventAttributesTypeDef, total=False
):
    runId: str
    control: str


class _RequiredResourceTagTypeDef(TypedDict):
    key: str


class ResourceTagTypeDef(_RequiredResourceTagTypeDef, total=False):
    value: str


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RunTypeDef(TypedDict, total=False):
    runId: str


_RequiredScheduleActivityTaskDecisionAttributesTypeDef = TypedDict(
    "_RequiredScheduleActivityTaskDecisionAttributesTypeDef",
    {"activityType": "ActivityTypeTypeDef", "activityId": str},
)
_OptionalScheduleActivityTaskDecisionAttributesTypeDef = TypedDict(
    "_OptionalScheduleActivityTaskDecisionAttributesTypeDef",
    {
        "control": str,
        "input": str,
        "scheduleToCloseTimeout": str,
        "taskList": "TaskListTypeDef",
        "taskPriority": str,
        "scheduleToStartTimeout": str,
        "startToCloseTimeout": str,
        "heartbeatTimeout": str,
    },
    total=False,
)


class ScheduleActivityTaskDecisionAttributesTypeDef(
    _RequiredScheduleActivityTaskDecisionAttributesTypeDef,
    _OptionalScheduleActivityTaskDecisionAttributesTypeDef,
):
    pass


class ScheduleActivityTaskFailedEventAttributesTypeDef(TypedDict):
    activityType: "ActivityTypeTypeDef"
    activityId: str
    cause: ScheduleActivityTaskFailedCause
    decisionTaskCompletedEventId: int


_RequiredScheduleLambdaFunctionDecisionAttributesTypeDef = TypedDict(
    "_RequiredScheduleLambdaFunctionDecisionAttributesTypeDef", {"id": str, "name": str}
)
_OptionalScheduleLambdaFunctionDecisionAttributesTypeDef = TypedDict(
    "_OptionalScheduleLambdaFunctionDecisionAttributesTypeDef",
    {"control": str, "input": str, "startToCloseTimeout": str},
    total=False,
)


class ScheduleLambdaFunctionDecisionAttributesTypeDef(
    _RequiredScheduleLambdaFunctionDecisionAttributesTypeDef,
    _OptionalScheduleLambdaFunctionDecisionAttributesTypeDef,
):
    pass


ScheduleLambdaFunctionFailedEventAttributesTypeDef = TypedDict(
    "ScheduleLambdaFunctionFailedEventAttributesTypeDef",
    {
        "id": str,
        "name": str,
        "cause": ScheduleLambdaFunctionFailedCause,
        "decisionTaskCompletedEventId": int,
    },
)

_RequiredSignalExternalWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "_RequiredSignalExternalWorkflowExecutionDecisionAttributesTypeDef",
    {"workflowId": str, "signalName": str},
)
_OptionalSignalExternalWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "_OptionalSignalExternalWorkflowExecutionDecisionAttributesTypeDef",
    {"runId": str, "input": str, "control": str},
    total=False,
)


class SignalExternalWorkflowExecutionDecisionAttributesTypeDef(
    _RequiredSignalExternalWorkflowExecutionDecisionAttributesTypeDef,
    _OptionalSignalExternalWorkflowExecutionDecisionAttributesTypeDef,
):
    pass


class _RequiredSignalExternalWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    workflowId: str
    cause: SignalExternalWorkflowExecutionFailedCause
    initiatedEventId: int
    decisionTaskCompletedEventId: int


class SignalExternalWorkflowExecutionFailedEventAttributesTypeDef(
    _RequiredSignalExternalWorkflowExecutionFailedEventAttributesTypeDef, total=False
):
    runId: str
    control: str


_RequiredSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_RequiredSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"workflowId": str, "signalName": str, "decisionTaskCompletedEventId": int},
)
_OptionalSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_OptionalSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef",
    {"runId": str, "input": str, "control": str},
    total=False,
)


class SignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef(
    _RequiredSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
    _OptionalSignalExternalWorkflowExecutionInitiatedEventAttributesTypeDef,
):
    pass


_RequiredStartChildWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "_RequiredStartChildWorkflowExecutionDecisionAttributesTypeDef",
    {"workflowType": "WorkflowTypeTypeDef", "workflowId": str},
)
_OptionalStartChildWorkflowExecutionDecisionAttributesTypeDef = TypedDict(
    "_OptionalStartChildWorkflowExecutionDecisionAttributesTypeDef",
    {
        "control": str,
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskList": "TaskListTypeDef",
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "childPolicy": ChildPolicy,
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)


class StartChildWorkflowExecutionDecisionAttributesTypeDef(
    _RequiredStartChildWorkflowExecutionDecisionAttributesTypeDef,
    _OptionalStartChildWorkflowExecutionDecisionAttributesTypeDef,
):
    pass


class _RequiredStartChildWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    workflowType: "WorkflowTypeTypeDef"
    cause: StartChildWorkflowExecutionFailedCause
    workflowId: str
    initiatedEventId: int
    decisionTaskCompletedEventId: int


class StartChildWorkflowExecutionFailedEventAttributesTypeDef(
    _RequiredStartChildWorkflowExecutionFailedEventAttributesTypeDef, total=False
):
    control: str


_RequiredStartChildWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_RequiredStartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "workflowId": str,
        "workflowType": "WorkflowTypeTypeDef",
        "taskList": "TaskListTypeDef",
        "decisionTaskCompletedEventId": int,
        "childPolicy": ChildPolicy,
    },
)
_OptionalStartChildWorkflowExecutionInitiatedEventAttributesTypeDef = TypedDict(
    "_OptionalStartChildWorkflowExecutionInitiatedEventAttributesTypeDef",
    {
        "control": str,
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)


class StartChildWorkflowExecutionInitiatedEventAttributesTypeDef(
    _RequiredStartChildWorkflowExecutionInitiatedEventAttributesTypeDef,
    _OptionalStartChildWorkflowExecutionInitiatedEventAttributesTypeDef,
):
    pass


class StartLambdaFunctionFailedEventAttributesTypeDef(TypedDict, total=False):
    scheduledEventId: int
    cause: Literal["ASSUME_ROLE_FAILED"]
    message: str


class _RequiredStartTimerDecisionAttributesTypeDef(TypedDict):
    timerId: str
    startToFireTimeout: str


class StartTimerDecisionAttributesTypeDef(
    _RequiredStartTimerDecisionAttributesTypeDef, total=False
):
    control: str


class StartTimerFailedEventAttributesTypeDef(TypedDict):
    timerId: str
    cause: StartTimerFailedCause
    decisionTaskCompletedEventId: int


class TagFilterTypeDef(TypedDict):
    tag: str


class TaskListTypeDef(TypedDict):
    name: str


class TimerCanceledEventAttributesTypeDef(TypedDict):
    timerId: str
    startedEventId: int
    decisionTaskCompletedEventId: int


class TimerFiredEventAttributesTypeDef(TypedDict):
    timerId: str
    startedEventId: int


class _RequiredTimerStartedEventAttributesTypeDef(TypedDict):
    timerId: str
    startToFireTimeout: str
    decisionTaskCompletedEventId: int


class TimerStartedEventAttributesTypeDef(_RequiredTimerStartedEventAttributesTypeDef, total=False):
    control: str


class WorkflowExecutionCancelRequestedEventAttributesTypeDef(TypedDict, total=False):
    externalWorkflowExecution: "WorkflowExecutionTypeDef"
    externalInitiatedEventId: int
    cause: Literal["CHILD_POLICY_APPLIED"]


class _RequiredWorkflowExecutionCanceledEventAttributesTypeDef(TypedDict):
    decisionTaskCompletedEventId: int


class WorkflowExecutionCanceledEventAttributesTypeDef(
    _RequiredWorkflowExecutionCanceledEventAttributesTypeDef, total=False
):
    details: str


class _RequiredWorkflowExecutionCompletedEventAttributesTypeDef(TypedDict):
    decisionTaskCompletedEventId: int


class WorkflowExecutionCompletedEventAttributesTypeDef(
    _RequiredWorkflowExecutionCompletedEventAttributesTypeDef, total=False
):
    result: str


class _RequiredWorkflowExecutionConfigurationTypeDef(TypedDict):
    taskStartToCloseTimeout: str
    executionStartToCloseTimeout: str
    taskList: "TaskListTypeDef"
    childPolicy: ChildPolicy


class WorkflowExecutionConfigurationTypeDef(
    _RequiredWorkflowExecutionConfigurationTypeDef, total=False
):
    taskPriority: str
    lambdaRole: str


_RequiredWorkflowExecutionContinuedAsNewEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionContinuedAsNewEventAttributesTypeDef",
    {
        "decisionTaskCompletedEventId": int,
        "newExecutionRunId": str,
        "taskList": "TaskListTypeDef",
        "childPolicy": ChildPolicy,
        "workflowType": "WorkflowTypeTypeDef",
    },
)
_OptionalWorkflowExecutionContinuedAsNewEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionContinuedAsNewEventAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskPriority": str,
        "taskStartToCloseTimeout": str,
        "tagList": List[str],
        "lambdaRole": str,
    },
    total=False,
)


class WorkflowExecutionContinuedAsNewEventAttributesTypeDef(
    _RequiredWorkflowExecutionContinuedAsNewEventAttributesTypeDef,
    _OptionalWorkflowExecutionContinuedAsNewEventAttributesTypeDef,
):
    pass


class _RequiredWorkflowExecutionCountTypeDef(TypedDict):
    count: int


class WorkflowExecutionCountTypeDef(_RequiredWorkflowExecutionCountTypeDef, total=False):
    truncated: bool


class _RequiredWorkflowExecutionDetailTypeDef(TypedDict):
    executionInfo: "WorkflowExecutionInfoTypeDef"
    executionConfiguration: "WorkflowExecutionConfigurationTypeDef"
    openCounts: "WorkflowExecutionOpenCountsTypeDef"


class WorkflowExecutionDetailTypeDef(_RequiredWorkflowExecutionDetailTypeDef, total=False):
    latestActivityTaskTimestamp: datetime
    latestExecutionContext: str


class _RequiredWorkflowExecutionFailedEventAttributesTypeDef(TypedDict):
    decisionTaskCompletedEventId: int


class WorkflowExecutionFailedEventAttributesTypeDef(
    _RequiredWorkflowExecutionFailedEventAttributesTypeDef, total=False
):
    reason: str
    details: str


class WorkflowExecutionFilterTypeDef(TypedDict):
    workflowId: str


class _RequiredWorkflowExecutionInfoTypeDef(TypedDict):
    execution: "WorkflowExecutionTypeDef"
    workflowType: "WorkflowTypeTypeDef"
    startTimestamp: datetime
    executionStatus: ExecutionStatus


class WorkflowExecutionInfoTypeDef(_RequiredWorkflowExecutionInfoTypeDef, total=False):
    closeTimestamp: datetime
    closeStatus: CloseStatus
    parent: "WorkflowExecutionTypeDef"
    tagList: List[str]
    cancelRequested: bool


class _RequiredWorkflowExecutionInfosTypeDef(TypedDict):
    executionInfos: List["WorkflowExecutionInfoTypeDef"]


class WorkflowExecutionInfosTypeDef(_RequiredWorkflowExecutionInfosTypeDef, total=False):
    nextPageToken: str


class _RequiredWorkflowExecutionOpenCountsTypeDef(TypedDict):
    openActivityTasks: int
    openDecisionTasks: int
    openTimers: int
    openChildWorkflowExecutions: int


class WorkflowExecutionOpenCountsTypeDef(_RequiredWorkflowExecutionOpenCountsTypeDef, total=False):
    openLambdaFunctions: int


_RequiredWorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionSignaledEventAttributesTypeDef", {"signalName": str}
)
_OptionalWorkflowExecutionSignaledEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionSignaledEventAttributesTypeDef",
    {
        "input": str,
        "externalWorkflowExecution": "WorkflowExecutionTypeDef",
        "externalInitiatedEventId": int,
    },
    total=False,
)


class WorkflowExecutionSignaledEventAttributesTypeDef(
    _RequiredWorkflowExecutionSignaledEventAttributesTypeDef,
    _OptionalWorkflowExecutionSignaledEventAttributesTypeDef,
):
    pass


_RequiredWorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "_RequiredWorkflowExecutionStartedEventAttributesTypeDef",
    {
        "childPolicy": ChildPolicy,
        "taskList": "TaskListTypeDef",
        "workflowType": "WorkflowTypeTypeDef",
    },
)
_OptionalWorkflowExecutionStartedEventAttributesTypeDef = TypedDict(
    "_OptionalWorkflowExecutionStartedEventAttributesTypeDef",
    {
        "input": str,
        "executionStartToCloseTimeout": str,
        "taskStartToCloseTimeout": str,
        "taskPriority": str,
        "tagList": List[str],
        "continuedExecutionRunId": str,
        "parentWorkflowExecution": "WorkflowExecutionTypeDef",
        "parentInitiatedEventId": int,
        "lambdaRole": str,
    },
    total=False,
)


class WorkflowExecutionStartedEventAttributesTypeDef(
    _RequiredWorkflowExecutionStartedEventAttributesTypeDef,
    _OptionalWorkflowExecutionStartedEventAttributesTypeDef,
):
    pass


class _RequiredWorkflowExecutionTerminatedEventAttributesTypeDef(TypedDict):
    childPolicy: ChildPolicy


class WorkflowExecutionTerminatedEventAttributesTypeDef(
    _RequiredWorkflowExecutionTerminatedEventAttributesTypeDef, total=False
):
    reason: str
    details: str
    cause: WorkflowExecutionTerminatedCause


class WorkflowExecutionTimedOutEventAttributesTypeDef(TypedDict):
    timeoutType: Literal["START_TO_CLOSE"]
    childPolicy: ChildPolicy


class WorkflowExecutionTypeDef(TypedDict):
    workflowId: str
    runId: str


class WorkflowTypeConfigurationTypeDef(TypedDict, total=False):
    defaultTaskStartToCloseTimeout: str
    defaultExecutionStartToCloseTimeout: str
    defaultTaskList: "TaskListTypeDef"
    defaultTaskPriority: str
    defaultChildPolicy: ChildPolicy
    defaultLambdaRole: str


class WorkflowTypeDetailTypeDef(TypedDict):
    typeInfo: "WorkflowTypeInfoTypeDef"
    configuration: "WorkflowTypeConfigurationTypeDef"


class _RequiredWorkflowTypeFilterTypeDef(TypedDict):
    name: str


class WorkflowTypeFilterTypeDef(_RequiredWorkflowTypeFilterTypeDef, total=False):
    version: str


class _RequiredWorkflowTypeInfoTypeDef(TypedDict):
    workflowType: "WorkflowTypeTypeDef"
    status: RegistrationStatus
    creationDate: datetime


class WorkflowTypeInfoTypeDef(_RequiredWorkflowTypeInfoTypeDef, total=False):
    description: str
    deprecationDate: datetime


class _RequiredWorkflowTypeInfosTypeDef(TypedDict):
    typeInfos: List["WorkflowTypeInfoTypeDef"]


class WorkflowTypeInfosTypeDef(_RequiredWorkflowTypeInfosTypeDef, total=False):
    nextPageToken: str


class WorkflowTypeTypeDef(TypedDict):
    name: str
    version: str
