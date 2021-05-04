"""
Type annotations for swf service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_swf/literals.html)

Usage::

    ```python
    from mypy_boto3_swf.literals import ActivityTaskTimeoutType

    data: ActivityTaskTimeoutType = "HEARTBEAT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActivityTaskTimeoutType",
    "CancelTimerFailedCause",
    "CancelWorkflowExecutionFailedCause",
    "ChildPolicy",
    "CloseStatus",
    "CompleteWorkflowExecutionFailedCause",
    "ContinueAsNewWorkflowExecutionFailedCause",
    "DecisionTaskTimeoutType",
    "DecisionType",
    "EventType",
    "ExecutionStatus",
    "FailWorkflowExecutionFailedCause",
    "GetWorkflowExecutionHistoryPaginatorName",
    "LambdaFunctionTimeoutType",
    "ListActivityTypesPaginatorName",
    "ListClosedWorkflowExecutionsPaginatorName",
    "ListDomainsPaginatorName",
    "ListOpenWorkflowExecutionsPaginatorName",
    "ListWorkflowTypesPaginatorName",
    "PollForDecisionTaskPaginatorName",
    "RecordMarkerFailedCause",
    "RegistrationStatus",
    "RequestCancelActivityTaskFailedCause",
    "RequestCancelExternalWorkflowExecutionFailedCause",
    "ScheduleActivityTaskFailedCause",
    "ScheduleLambdaFunctionFailedCause",
    "SignalExternalWorkflowExecutionFailedCause",
    "StartChildWorkflowExecutionFailedCause",
    "StartLambdaFunctionFailedCause",
    "StartTimerFailedCause",
    "WorkflowExecutionCancelRequestedCause",
    "WorkflowExecutionTerminatedCause",
    "WorkflowExecutionTimeoutType",
)


ActivityTaskTimeoutType = Literal[
    "HEARTBEAT", "SCHEDULE_TO_CLOSE", "SCHEDULE_TO_START", "START_TO_CLOSE"
]
CancelTimerFailedCause = Literal["OPERATION_NOT_PERMITTED", "TIMER_ID_UNKNOWN"]
CancelWorkflowExecutionFailedCause = Literal["OPERATION_NOT_PERMITTED", "UNHANDLED_DECISION"]
ChildPolicy = Literal["ABANDON", "REQUEST_CANCEL", "TERMINATE"]
CloseStatus = Literal[
    "CANCELED", "COMPLETED", "CONTINUED_AS_NEW", "FAILED", "TERMINATED", "TIMED_OUT"
]
CompleteWorkflowExecutionFailedCause = Literal["OPERATION_NOT_PERMITTED", "UNHANDLED_DECISION"]
ContinueAsNewWorkflowExecutionFailedCause = Literal[
    "CONTINUE_AS_NEW_WORKFLOW_EXECUTION_RATE_EXCEEDED",
    "DEFAULT_CHILD_POLICY_UNDEFINED",
    "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_TASK_LIST_UNDEFINED",
    "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "OPERATION_NOT_PERMITTED",
    "UNHANDLED_DECISION",
    "WORKFLOW_TYPE_DEPRECATED",
    "WORKFLOW_TYPE_DOES_NOT_EXIST",
]
DecisionTaskTimeoutType = Literal["START_TO_CLOSE"]
DecisionType = Literal[
    "CancelTimer",
    "CancelWorkflowExecution",
    "CompleteWorkflowExecution",
    "ContinueAsNewWorkflowExecution",
    "FailWorkflowExecution",
    "RecordMarker",
    "RequestCancelActivityTask",
    "RequestCancelExternalWorkflowExecution",
    "ScheduleActivityTask",
    "ScheduleLambdaFunction",
    "SignalExternalWorkflowExecution",
    "StartChildWorkflowExecution",
    "StartTimer",
]
EventType = Literal[
    "ActivityTaskCancelRequested",
    "ActivityTaskCanceled",
    "ActivityTaskCompleted",
    "ActivityTaskFailed",
    "ActivityTaskScheduled",
    "ActivityTaskStarted",
    "ActivityTaskTimedOut",
    "CancelTimerFailed",
    "CancelWorkflowExecutionFailed",
    "ChildWorkflowExecutionCanceled",
    "ChildWorkflowExecutionCompleted",
    "ChildWorkflowExecutionFailed",
    "ChildWorkflowExecutionStarted",
    "ChildWorkflowExecutionTerminated",
    "ChildWorkflowExecutionTimedOut",
    "CompleteWorkflowExecutionFailed",
    "ContinueAsNewWorkflowExecutionFailed",
    "DecisionTaskCompleted",
    "DecisionTaskScheduled",
    "DecisionTaskStarted",
    "DecisionTaskTimedOut",
    "ExternalWorkflowExecutionCancelRequested",
    "ExternalWorkflowExecutionSignaled",
    "FailWorkflowExecutionFailed",
    "LambdaFunctionCompleted",
    "LambdaFunctionFailed",
    "LambdaFunctionScheduled",
    "LambdaFunctionStarted",
    "LambdaFunctionTimedOut",
    "MarkerRecorded",
    "RecordMarkerFailed",
    "RequestCancelActivityTaskFailed",
    "RequestCancelExternalWorkflowExecutionFailed",
    "RequestCancelExternalWorkflowExecutionInitiated",
    "ScheduleActivityTaskFailed",
    "ScheduleLambdaFunctionFailed",
    "SignalExternalWorkflowExecutionFailed",
    "SignalExternalWorkflowExecutionInitiated",
    "StartChildWorkflowExecutionFailed",
    "StartChildWorkflowExecutionInitiated",
    "StartLambdaFunctionFailed",
    "StartTimerFailed",
    "TimerCanceled",
    "TimerFired",
    "TimerStarted",
    "WorkflowExecutionCancelRequested",
    "WorkflowExecutionCanceled",
    "WorkflowExecutionCompleted",
    "WorkflowExecutionContinuedAsNew",
    "WorkflowExecutionFailed",
    "WorkflowExecutionSignaled",
    "WorkflowExecutionStarted",
    "WorkflowExecutionTerminated",
    "WorkflowExecutionTimedOut",
]
ExecutionStatus = Literal["CLOSED", "OPEN"]
FailWorkflowExecutionFailedCause = Literal["OPERATION_NOT_PERMITTED", "UNHANDLED_DECISION"]
GetWorkflowExecutionHistoryPaginatorName = Literal["get_workflow_execution_history"]
LambdaFunctionTimeoutType = Literal["START_TO_CLOSE"]
ListActivityTypesPaginatorName = Literal["list_activity_types"]
ListClosedWorkflowExecutionsPaginatorName = Literal["list_closed_workflow_executions"]
ListDomainsPaginatorName = Literal["list_domains"]
ListOpenWorkflowExecutionsPaginatorName = Literal["list_open_workflow_executions"]
ListWorkflowTypesPaginatorName = Literal["list_workflow_types"]
PollForDecisionTaskPaginatorName = Literal["poll_for_decision_task"]
RecordMarkerFailedCause = Literal["OPERATION_NOT_PERMITTED"]
RegistrationStatus = Literal["DEPRECATED", "REGISTERED"]
RequestCancelActivityTaskFailedCause = Literal["ACTIVITY_ID_UNKNOWN", "OPERATION_NOT_PERMITTED"]
RequestCancelExternalWorkflowExecutionFailedCause = Literal[
    "OPERATION_NOT_PERMITTED",
    "REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
    "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
]
ScheduleActivityTaskFailedCause = Literal[
    "ACTIVITY_CREATION_RATE_EXCEEDED",
    "ACTIVITY_ID_ALREADY_IN_USE",
    "ACTIVITY_TYPE_DEPRECATED",
    "ACTIVITY_TYPE_DOES_NOT_EXIST",
    "DEFAULT_HEARTBEAT_TIMEOUT_UNDEFINED",
    "DEFAULT_SCHEDULE_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_SCHEDULE_TO_START_TIMEOUT_UNDEFINED",
    "DEFAULT_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_TASK_LIST_UNDEFINED",
    "OPEN_ACTIVITIES_LIMIT_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
]
ScheduleLambdaFunctionFailedCause = Literal[
    "ID_ALREADY_IN_USE",
    "LAMBDA_FUNCTION_CREATION_RATE_EXCEEDED",
    "LAMBDA_SERVICE_NOT_AVAILABLE_IN_REGION",
    "OPEN_LAMBDA_FUNCTIONS_LIMIT_EXCEEDED",
]
SignalExternalWorkflowExecutionFailedCause = Literal[
    "OPERATION_NOT_PERMITTED",
    "SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_RATE_EXCEEDED",
    "UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION",
]
StartChildWorkflowExecutionFailedCause = Literal[
    "CHILD_CREATION_RATE_EXCEEDED",
    "DEFAULT_CHILD_POLICY_UNDEFINED",
    "DEFAULT_EXECUTION_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "DEFAULT_TASK_LIST_UNDEFINED",
    "DEFAULT_TASK_START_TO_CLOSE_TIMEOUT_UNDEFINED",
    "OPEN_CHILDREN_LIMIT_EXCEEDED",
    "OPEN_WORKFLOWS_LIMIT_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
    "WORKFLOW_ALREADY_RUNNING",
    "WORKFLOW_TYPE_DEPRECATED",
    "WORKFLOW_TYPE_DOES_NOT_EXIST",
]
StartLambdaFunctionFailedCause = Literal["ASSUME_ROLE_FAILED"]
StartTimerFailedCause = Literal[
    "OPEN_TIMERS_LIMIT_EXCEEDED",
    "OPERATION_NOT_PERMITTED",
    "TIMER_CREATION_RATE_EXCEEDED",
    "TIMER_ID_ALREADY_IN_USE",
]
WorkflowExecutionCancelRequestedCause = Literal["CHILD_POLICY_APPLIED"]
WorkflowExecutionTerminatedCause = Literal[
    "CHILD_POLICY_APPLIED", "EVENT_LIMIT_EXCEEDED", "OPERATOR_INITIATED"
]
WorkflowExecutionTimeoutType = Literal["START_TO_CLOSE"]
