"""
Type annotations for stepfunctions service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/type_defs.html)

Usage::

    ```python
    from mypy_boto3_stepfunctions.type_defs import ActivityFailedEventDetailsTypeDef

    data: ActivityFailedEventDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_stepfunctions.literals import (
    ExecutionStatus,
    HistoryEventType,
    LogLevel,
    StateMachineStatus,
    StateMachineType,
    SyncExecutionStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActivityFailedEventDetailsTypeDef",
    "ActivityListItemTypeDef",
    "ActivityScheduleFailedEventDetailsTypeDef",
    "ActivityScheduledEventDetailsTypeDef",
    "ActivityStartedEventDetailsTypeDef",
    "ActivitySucceededEventDetailsTypeDef",
    "ActivityTimedOutEventDetailsTypeDef",
    "BillingDetailsTypeDef",
    "CloudWatchEventsExecutionDataDetailsTypeDef",
    "CloudWatchLogsLogGroupTypeDef",
    "CreateActivityOutputTypeDef",
    "CreateStateMachineOutputTypeDef",
    "DescribeActivityOutputTypeDef",
    "DescribeExecutionOutputTypeDef",
    "DescribeStateMachineForExecutionOutputTypeDef",
    "DescribeStateMachineOutputTypeDef",
    "ExecutionAbortedEventDetailsTypeDef",
    "ExecutionFailedEventDetailsTypeDef",
    "ExecutionListItemTypeDef",
    "ExecutionStartedEventDetailsTypeDef",
    "ExecutionSucceededEventDetailsTypeDef",
    "ExecutionTimedOutEventDetailsTypeDef",
    "GetActivityTaskOutputTypeDef",
    "GetExecutionHistoryOutputTypeDef",
    "HistoryEventExecutionDataDetailsTypeDef",
    "HistoryEventTypeDef",
    "LambdaFunctionFailedEventDetailsTypeDef",
    "LambdaFunctionScheduleFailedEventDetailsTypeDef",
    "LambdaFunctionScheduledEventDetailsTypeDef",
    "LambdaFunctionStartFailedEventDetailsTypeDef",
    "LambdaFunctionSucceededEventDetailsTypeDef",
    "LambdaFunctionTimedOutEventDetailsTypeDef",
    "ListActivitiesOutputTypeDef",
    "ListExecutionsOutputTypeDef",
    "ListStateMachinesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "LogDestinationTypeDef",
    "LoggingConfigurationTypeDef",
    "MapIterationEventDetailsTypeDef",
    "MapStateStartedEventDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadata",
    "StartExecutionOutputTypeDef",
    "StartSyncExecutionOutputTypeDef",
    "StateEnteredEventDetailsTypeDef",
    "StateExitedEventDetailsTypeDef",
    "StateMachineListItemTypeDef",
    "StopExecutionOutputTypeDef",
    "TagTypeDef",
    "TaskFailedEventDetailsTypeDef",
    "TaskScheduledEventDetailsTypeDef",
    "TaskStartFailedEventDetailsTypeDef",
    "TaskStartedEventDetailsTypeDef",
    "TaskSubmitFailedEventDetailsTypeDef",
    "TaskSubmittedEventDetailsTypeDef",
    "TaskSucceededEventDetailsTypeDef",
    "TaskTimedOutEventDetailsTypeDef",
    "TracingConfigurationTypeDef",
    "UpdateStateMachineOutputTypeDef",
)


class ActivityFailedEventDetailsTypeDef(TypedDict, total=False):
    error: str
    cause: str


class ActivityListItemTypeDef(TypedDict):
    activityArn: str
    name: str
    creationDate: datetime


class ActivityScheduleFailedEventDetailsTypeDef(TypedDict, total=False):
    error: str
    cause: str


_RequiredActivityScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredActivityScheduledEventDetailsTypeDef", {"resource": str}
)
_OptionalActivityScheduledEventDetailsTypeDef = TypedDict(
    "_OptionalActivityScheduledEventDetailsTypeDef",
    {
        "input": str,
        "inputDetails": "HistoryEventExecutionDataDetailsTypeDef",
        "timeoutInSeconds": int,
        "heartbeatInSeconds": int,
    },
    total=False,
)


class ActivityScheduledEventDetailsTypeDef(
    _RequiredActivityScheduledEventDetailsTypeDef, _OptionalActivityScheduledEventDetailsTypeDef
):
    pass


class ActivityStartedEventDetailsTypeDef(TypedDict, total=False):
    workerName: str


class ActivitySucceededEventDetailsTypeDef(TypedDict, total=False):
    output: str
    outputDetails: "HistoryEventExecutionDataDetailsTypeDef"


class ActivityTimedOutEventDetailsTypeDef(TypedDict, total=False):
    error: str
    cause: str


class BillingDetailsTypeDef(TypedDict, total=False):
    billedMemoryUsedInMB: int
    billedDurationInMilliseconds: int


class CloudWatchEventsExecutionDataDetailsTypeDef(TypedDict, total=False):
    included: bool


class CloudWatchLogsLogGroupTypeDef(TypedDict, total=False):
    logGroupArn: str


class CreateActivityOutputTypeDef(TypedDict):
    activityArn: str
    creationDate: datetime
    ResponseMetadata: "ResponseMetadata"


class CreateStateMachineOutputTypeDef(TypedDict):
    stateMachineArn: str
    creationDate: datetime
    ResponseMetadata: "ResponseMetadata"


class DescribeActivityOutputTypeDef(TypedDict):
    activityArn: str
    name: str
    creationDate: datetime
    ResponseMetadata: "ResponseMetadata"


DescribeExecutionOutputTypeDef = TypedDict(
    "DescribeExecutionOutputTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": ExecutionStatus,
        "startDate": datetime,
        "stopDate": datetime,
        "input": str,
        "inputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "output": str,
        "outputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "traceHeader": str,
        "ResponseMetadata": "ResponseMetadata",
    },
)


class DescribeStateMachineForExecutionOutputTypeDef(TypedDict):
    stateMachineArn: str
    name: str
    definition: str
    roleArn: str
    updateDate: datetime
    loggingConfiguration: "LoggingConfigurationTypeDef"
    tracingConfiguration: "TracingConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


DescribeStateMachineOutputTypeDef = TypedDict(
    "DescribeStateMachineOutputTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "status": StateMachineStatus,
        "definition": str,
        "roleArn": str,
        "type": StateMachineType,
        "creationDate": datetime,
        "loggingConfiguration": "LoggingConfigurationTypeDef",
        "tracingConfiguration": "TracingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
)


class ExecutionAbortedEventDetailsTypeDef(TypedDict, total=False):
    error: str
    cause: str


class ExecutionFailedEventDetailsTypeDef(TypedDict, total=False):
    error: str
    cause: str


class _RequiredExecutionListItemTypeDef(TypedDict):
    executionArn: str
    stateMachineArn: str
    name: str
    status: ExecutionStatus
    startDate: datetime


class ExecutionListItemTypeDef(_RequiredExecutionListItemTypeDef, total=False):
    stopDate: datetime


ExecutionStartedEventDetailsTypeDef = TypedDict(
    "ExecutionStartedEventDetailsTypeDef",
    {"input": str, "inputDetails": "HistoryEventExecutionDataDetailsTypeDef", "roleArn": str},
    total=False,
)


class ExecutionSucceededEventDetailsTypeDef(TypedDict, total=False):
    output: str
    outputDetails: "HistoryEventExecutionDataDetailsTypeDef"


class ExecutionTimedOutEventDetailsTypeDef(TypedDict, total=False):
    error: str
    cause: str


GetActivityTaskOutputTypeDef = TypedDict(
    "GetActivityTaskOutputTypeDef",
    {"taskToken": str, "input": str, "ResponseMetadata": "ResponseMetadata"},
)


class GetExecutionHistoryOutputTypeDef(TypedDict):
    events: List["HistoryEventTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class HistoryEventExecutionDataDetailsTypeDef(TypedDict, total=False):
    truncated: bool


_RequiredHistoryEventTypeDef = TypedDict(
    "_RequiredHistoryEventTypeDef", {"timestamp": datetime, "type": HistoryEventType, "id": int}
)
_OptionalHistoryEventTypeDef = TypedDict(
    "_OptionalHistoryEventTypeDef",
    {
        "previousEventId": int,
        "activityFailedEventDetails": "ActivityFailedEventDetailsTypeDef",
        "activityScheduleFailedEventDetails": "ActivityScheduleFailedEventDetailsTypeDef",
        "activityScheduledEventDetails": "ActivityScheduledEventDetailsTypeDef",
        "activityStartedEventDetails": "ActivityStartedEventDetailsTypeDef",
        "activitySucceededEventDetails": "ActivitySucceededEventDetailsTypeDef",
        "activityTimedOutEventDetails": "ActivityTimedOutEventDetailsTypeDef",
        "taskFailedEventDetails": "TaskFailedEventDetailsTypeDef",
        "taskScheduledEventDetails": "TaskScheduledEventDetailsTypeDef",
        "taskStartFailedEventDetails": "TaskStartFailedEventDetailsTypeDef",
        "taskStartedEventDetails": "TaskStartedEventDetailsTypeDef",
        "taskSubmitFailedEventDetails": "TaskSubmitFailedEventDetailsTypeDef",
        "taskSubmittedEventDetails": "TaskSubmittedEventDetailsTypeDef",
        "taskSucceededEventDetails": "TaskSucceededEventDetailsTypeDef",
        "taskTimedOutEventDetails": "TaskTimedOutEventDetailsTypeDef",
        "executionFailedEventDetails": "ExecutionFailedEventDetailsTypeDef",
        "executionStartedEventDetails": "ExecutionStartedEventDetailsTypeDef",
        "executionSucceededEventDetails": "ExecutionSucceededEventDetailsTypeDef",
        "executionAbortedEventDetails": "ExecutionAbortedEventDetailsTypeDef",
        "executionTimedOutEventDetails": "ExecutionTimedOutEventDetailsTypeDef",
        "mapStateStartedEventDetails": "MapStateStartedEventDetailsTypeDef",
        "mapIterationStartedEventDetails": "MapIterationEventDetailsTypeDef",
        "mapIterationSucceededEventDetails": "MapIterationEventDetailsTypeDef",
        "mapIterationFailedEventDetails": "MapIterationEventDetailsTypeDef",
        "mapIterationAbortedEventDetails": "MapIterationEventDetailsTypeDef",
        "lambdaFunctionFailedEventDetails": "LambdaFunctionFailedEventDetailsTypeDef",
        "lambdaFunctionScheduleFailedEventDetails": "LambdaFunctionScheduleFailedEventDetailsTypeDef",
        "lambdaFunctionScheduledEventDetails": "LambdaFunctionScheduledEventDetailsTypeDef",
        "lambdaFunctionStartFailedEventDetails": "LambdaFunctionStartFailedEventDetailsTypeDef",
        "lambdaFunctionSucceededEventDetails": "LambdaFunctionSucceededEventDetailsTypeDef",
        "lambdaFunctionTimedOutEventDetails": "LambdaFunctionTimedOutEventDetailsTypeDef",
        "stateEnteredEventDetails": "StateEnteredEventDetailsTypeDef",
        "stateExitedEventDetails": "StateExitedEventDetailsTypeDef",
    },
    total=False,
)


class HistoryEventTypeDef(_RequiredHistoryEventTypeDef, _OptionalHistoryEventTypeDef):
    pass


class LambdaFunctionFailedEventDetailsTypeDef(TypedDict, total=False):
    error: str
    cause: str


class LambdaFunctionScheduleFailedEventDetailsTypeDef(TypedDict, total=False):
    error: str
    cause: str


_RequiredLambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "_RequiredLambdaFunctionScheduledEventDetailsTypeDef", {"resource": str}
)
_OptionalLambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "_OptionalLambdaFunctionScheduledEventDetailsTypeDef",
    {
        "input": str,
        "inputDetails": "HistoryEventExecutionDataDetailsTypeDef",
        "timeoutInSeconds": int,
    },
    total=False,
)


class LambdaFunctionScheduledEventDetailsTypeDef(
    _RequiredLambdaFunctionScheduledEventDetailsTypeDef,
    _OptionalLambdaFunctionScheduledEventDetailsTypeDef,
):
    pass


class LambdaFunctionStartFailedEventDetailsTypeDef(TypedDict, total=False):
    error: str
    cause: str


class LambdaFunctionSucceededEventDetailsTypeDef(TypedDict, total=False):
    output: str
    outputDetails: "HistoryEventExecutionDataDetailsTypeDef"


class LambdaFunctionTimedOutEventDetailsTypeDef(TypedDict, total=False):
    error: str
    cause: str


class ListActivitiesOutputTypeDef(TypedDict):
    activities: List["ActivityListItemTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListExecutionsOutputTypeDef(TypedDict):
    executions: List["ExecutionListItemTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListStateMachinesOutputTypeDef(TypedDict):
    stateMachines: List["StateMachineListItemTypeDef"]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceOutputTypeDef(TypedDict):
    tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class LogDestinationTypeDef(TypedDict, total=False):
    cloudWatchLogsLogGroup: "CloudWatchLogsLogGroupTypeDef"


class LoggingConfigurationTypeDef(TypedDict, total=False):
    level: LogLevel
    includeExecutionData: bool
    destinations: List["LogDestinationTypeDef"]


class MapIterationEventDetailsTypeDef(TypedDict, total=False):
    name: str
    index: int


class MapStateStartedEventDetailsTypeDef(TypedDict, total=False):
    length: int


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


class StartExecutionOutputTypeDef(TypedDict):
    executionArn: str
    startDate: datetime
    ResponseMetadata: "ResponseMetadata"


StartSyncExecutionOutputTypeDef = TypedDict(
    "StartSyncExecutionOutputTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "startDate": datetime,
        "stopDate": datetime,
        "status": SyncExecutionStatus,
        "error": str,
        "cause": str,
        "input": str,
        "inputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "output": str,
        "outputDetails": "CloudWatchEventsExecutionDataDetailsTypeDef",
        "traceHeader": str,
        "billingDetails": "BillingDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
)

_RequiredStateEnteredEventDetailsTypeDef = TypedDict(
    "_RequiredStateEnteredEventDetailsTypeDef", {"name": str}
)
_OptionalStateEnteredEventDetailsTypeDef = TypedDict(
    "_OptionalStateEnteredEventDetailsTypeDef",
    {"input": str, "inputDetails": "HistoryEventExecutionDataDetailsTypeDef"},
    total=False,
)


class StateEnteredEventDetailsTypeDef(
    _RequiredStateEnteredEventDetailsTypeDef, _OptionalStateEnteredEventDetailsTypeDef
):
    pass


class _RequiredStateExitedEventDetailsTypeDef(TypedDict):
    name: str


class StateExitedEventDetailsTypeDef(_RequiredStateExitedEventDetailsTypeDef, total=False):
    output: str
    outputDetails: "HistoryEventExecutionDataDetailsTypeDef"


StateMachineListItemTypeDef = TypedDict(
    "StateMachineListItemTypeDef",
    {"stateMachineArn": str, "name": str, "type": StateMachineType, "creationDate": datetime},
)


class StopExecutionOutputTypeDef(TypedDict):
    stopDate: datetime
    ResponseMetadata: "ResponseMetadata"


class TagTypeDef(TypedDict, total=False):
    key: str
    value: str


class _RequiredTaskFailedEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str


class TaskFailedEventDetailsTypeDef(_RequiredTaskFailedEventDetailsTypeDef, total=False):
    error: str
    cause: str


class _RequiredTaskScheduledEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str
    region: str
    parameters: str


class TaskScheduledEventDetailsTypeDef(_RequiredTaskScheduledEventDetailsTypeDef, total=False):
    timeoutInSeconds: int
    heartbeatInSeconds: int


class _RequiredTaskStartFailedEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str


class TaskStartFailedEventDetailsTypeDef(_RequiredTaskStartFailedEventDetailsTypeDef, total=False):
    error: str
    cause: str


class TaskStartedEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str


class _RequiredTaskSubmitFailedEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str


class TaskSubmitFailedEventDetailsTypeDef(
    _RequiredTaskSubmitFailedEventDetailsTypeDef, total=False
):
    error: str
    cause: str


class _RequiredTaskSubmittedEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str


class TaskSubmittedEventDetailsTypeDef(_RequiredTaskSubmittedEventDetailsTypeDef, total=False):
    output: str
    outputDetails: "HistoryEventExecutionDataDetailsTypeDef"


class _RequiredTaskSucceededEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str


class TaskSucceededEventDetailsTypeDef(_RequiredTaskSucceededEventDetailsTypeDef, total=False):
    output: str
    outputDetails: "HistoryEventExecutionDataDetailsTypeDef"


class _RequiredTaskTimedOutEventDetailsTypeDef(TypedDict):
    resourceType: str
    resource: str


class TaskTimedOutEventDetailsTypeDef(_RequiredTaskTimedOutEventDetailsTypeDef, total=False):
    error: str
    cause: str


class TracingConfigurationTypeDef(TypedDict, total=False):
    enabled: bool


class UpdateStateMachineOutputTypeDef(TypedDict):
    updateDate: datetime
    ResponseMetadata: "ResponseMetadata"
