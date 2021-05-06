"""
Type annotations for stepfunctions service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/literals.html)

Usage::

    ```python
    from mypy_boto3_stepfunctions.literals import ExecutionStatus

    data: ExecutionStatus = "ABORTED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ExecutionStatus",
    "GetExecutionHistoryPaginatorName",
    "HistoryEventType",
    "ListActivitiesPaginatorName",
    "ListExecutionsPaginatorName",
    "ListStateMachinesPaginatorName",
    "LogLevel",
    "StateMachineStatus",
    "StateMachineType",
    "SyncExecutionStatus",
)


ExecutionStatus = Literal["ABORTED", "FAILED", "RUNNING", "SUCCEEDED", "TIMED_OUT"]
GetExecutionHistoryPaginatorName = Literal["get_execution_history"]
HistoryEventType = Literal[
    "ActivityFailed",
    "ActivityScheduleFailed",
    "ActivityScheduled",
    "ActivityStarted",
    "ActivitySucceeded",
    "ActivityTimedOut",
    "ChoiceStateEntered",
    "ChoiceStateExited",
    "ExecutionAborted",
    "ExecutionFailed",
    "ExecutionStarted",
    "ExecutionSucceeded",
    "ExecutionTimedOut",
    "FailStateEntered",
    "LambdaFunctionFailed",
    "LambdaFunctionScheduleFailed",
    "LambdaFunctionScheduled",
    "LambdaFunctionStartFailed",
    "LambdaFunctionStarted",
    "LambdaFunctionSucceeded",
    "LambdaFunctionTimedOut",
    "MapIterationAborted",
    "MapIterationFailed",
    "MapIterationStarted",
    "MapIterationSucceeded",
    "MapStateAborted",
    "MapStateEntered",
    "MapStateExited",
    "MapStateFailed",
    "MapStateStarted",
    "MapStateSucceeded",
    "ParallelStateAborted",
    "ParallelStateEntered",
    "ParallelStateExited",
    "ParallelStateFailed",
    "ParallelStateStarted",
    "ParallelStateSucceeded",
    "PassStateEntered",
    "PassStateExited",
    "SucceedStateEntered",
    "SucceedStateExited",
    "TaskFailed",
    "TaskScheduled",
    "TaskStartFailed",
    "TaskStarted",
    "TaskStateAborted",
    "TaskStateEntered",
    "TaskStateExited",
    "TaskSubmitFailed",
    "TaskSubmitted",
    "TaskSucceeded",
    "TaskTimedOut",
    "WaitStateAborted",
    "WaitStateEntered",
    "WaitStateExited",
]
ListActivitiesPaginatorName = Literal["list_activities"]
ListExecutionsPaginatorName = Literal["list_executions"]
ListStateMachinesPaginatorName = Literal["list_state_machines"]
LogLevel = Literal["ALL", "ERROR", "FATAL", "OFF"]
StateMachineStatus = Literal["ACTIVE", "DELETING"]
StateMachineType = Literal["EXPRESS", "STANDARD"]
SyncExecutionStatus = Literal["FAILED", "SUCCEEDED", "TIMED_OUT"]
