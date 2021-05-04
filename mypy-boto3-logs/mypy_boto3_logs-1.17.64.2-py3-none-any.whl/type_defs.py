"""
Type annotations for logs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_logs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_logs.type_defs import CreateExportTaskResponseTypeDef

    data: CreateExportTaskResponseTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_logs.literals import Distribution, ExportTaskStatusCode, QueryStatus

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateExportTaskResponseTypeDef",
    "DeleteQueryDefinitionResponseTypeDef",
    "DescribeDestinationsResponseTypeDef",
    "DescribeExportTasksResponseTypeDef",
    "DescribeLogGroupsResponseTypeDef",
    "DescribeLogStreamsResponseTypeDef",
    "DescribeMetricFiltersResponseTypeDef",
    "DescribeQueriesResponseTypeDef",
    "DescribeQueryDefinitionsResponseTypeDef",
    "DescribeResourcePoliciesResponseTypeDef",
    "DescribeSubscriptionFiltersResponseTypeDef",
    "DestinationTypeDef",
    "ExportTaskExecutionInfoTypeDef",
    "ExportTaskStatusTypeDef",
    "ExportTaskTypeDef",
    "FilterLogEventsResponseTypeDef",
    "FilteredLogEventTypeDef",
    "GetLogEventsResponseTypeDef",
    "GetLogGroupFieldsResponseTypeDef",
    "GetLogRecordResponseTypeDef",
    "GetQueryResultsResponseTypeDef",
    "InputLogEventTypeDef",
    "ListTagsLogGroupResponseTypeDef",
    "LogGroupFieldTypeDef",
    "LogGroupTypeDef",
    "LogStreamTypeDef",
    "MetricFilterMatchRecordTypeDef",
    "MetricFilterTypeDef",
    "MetricTransformationTypeDef",
    "OutputLogEventTypeDef",
    "PaginatorConfigTypeDef",
    "PutDestinationResponseTypeDef",
    "PutLogEventsResponseTypeDef",
    "PutQueryDefinitionResponseTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "QueryDefinitionTypeDef",
    "QueryInfoTypeDef",
    "QueryStatisticsTypeDef",
    "RejectedLogEventsInfoTypeDef",
    "ResourcePolicyTypeDef",
    "ResultFieldTypeDef",
    "SearchedLogStreamTypeDef",
    "StartQueryResponseTypeDef",
    "StopQueryResponseTypeDef",
    "SubscriptionFilterTypeDef",
    "TestMetricFilterResponseTypeDef",
)


class CreateExportTaskResponseTypeDef(TypedDict, total=False):
    taskId: str


class DeleteQueryDefinitionResponseTypeDef(TypedDict, total=False):
    success: bool


class DescribeDestinationsResponseTypeDef(TypedDict, total=False):
    destinations: List["DestinationTypeDef"]
    nextToken: str


class DescribeExportTasksResponseTypeDef(TypedDict, total=False):
    exportTasks: List["ExportTaskTypeDef"]
    nextToken: str


class DescribeLogGroupsResponseTypeDef(TypedDict, total=False):
    logGroups: List["LogGroupTypeDef"]
    nextToken: str


class DescribeLogStreamsResponseTypeDef(TypedDict, total=False):
    logStreams: List["LogStreamTypeDef"]
    nextToken: str


class DescribeMetricFiltersResponseTypeDef(TypedDict, total=False):
    metricFilters: List["MetricFilterTypeDef"]
    nextToken: str


class DescribeQueriesResponseTypeDef(TypedDict, total=False):
    queries: List["QueryInfoTypeDef"]
    nextToken: str


class DescribeQueryDefinitionsResponseTypeDef(TypedDict, total=False):
    queryDefinitions: List["QueryDefinitionTypeDef"]
    nextToken: str


class DescribeResourcePoliciesResponseTypeDef(TypedDict, total=False):
    resourcePolicies: List["ResourcePolicyTypeDef"]
    nextToken: str


class DescribeSubscriptionFiltersResponseTypeDef(TypedDict, total=False):
    subscriptionFilters: List["SubscriptionFilterTypeDef"]
    nextToken: str


class DestinationTypeDef(TypedDict, total=False):
    destinationName: str
    targetArn: str
    roleArn: str
    accessPolicy: str
    arn: str
    creationTime: int


class ExportTaskExecutionInfoTypeDef(TypedDict, total=False):
    creationTime: int
    completionTime: int


class ExportTaskStatusTypeDef(TypedDict, total=False):
    code: ExportTaskStatusCode
    message: str


ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "taskId": str,
        "taskName": str,
        "logGroupName": str,
        "from": int,
        "to": int,
        "destination": str,
        "destinationPrefix": str,
        "status": "ExportTaskStatusTypeDef",
        "executionInfo": "ExportTaskExecutionInfoTypeDef",
    },
    total=False,
)


class FilterLogEventsResponseTypeDef(TypedDict, total=False):
    events: List["FilteredLogEventTypeDef"]
    searchedLogStreams: List["SearchedLogStreamTypeDef"]
    nextToken: str


class FilteredLogEventTypeDef(TypedDict, total=False):
    logStreamName: str
    timestamp: int
    message: str
    ingestionTime: int
    eventId: str


class GetLogEventsResponseTypeDef(TypedDict, total=False):
    events: List["OutputLogEventTypeDef"]
    nextForwardToken: str
    nextBackwardToken: str


class GetLogGroupFieldsResponseTypeDef(TypedDict, total=False):
    logGroupFields: List["LogGroupFieldTypeDef"]


class GetLogRecordResponseTypeDef(TypedDict, total=False):
    logRecord: Dict[str, str]


class GetQueryResultsResponseTypeDef(TypedDict, total=False):
    results: List[List["ResultFieldTypeDef"]]
    statistics: "QueryStatisticsTypeDef"
    status: QueryStatus


class InputLogEventTypeDef(TypedDict):
    timestamp: int
    message: str


class ListTagsLogGroupResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class LogGroupFieldTypeDef(TypedDict, total=False):
    name: str
    percent: int


class LogGroupTypeDef(TypedDict, total=False):
    logGroupName: str
    creationTime: int
    retentionInDays: int
    metricFilterCount: int
    arn: str
    storedBytes: int
    kmsKeyId: str


class LogStreamTypeDef(TypedDict, total=False):
    logStreamName: str
    creationTime: int
    firstEventTimestamp: int
    lastEventTimestamp: int
    lastIngestionTime: int
    uploadSequenceToken: str
    arn: str
    storedBytes: int


class MetricFilterMatchRecordTypeDef(TypedDict, total=False):
    eventNumber: int
    eventMessage: str
    extractedValues: Dict[str, str]


class MetricFilterTypeDef(TypedDict, total=False):
    filterName: str
    filterPattern: str
    metricTransformations: List["MetricTransformationTypeDef"]
    creationTime: int
    logGroupName: str


class _RequiredMetricTransformationTypeDef(TypedDict):
    metricName: str
    metricNamespace: str
    metricValue: str


class MetricTransformationTypeDef(_RequiredMetricTransformationTypeDef, total=False):
    defaultValue: float


class OutputLogEventTypeDef(TypedDict, total=False):
    timestamp: int
    message: str
    ingestionTime: int


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PutDestinationResponseTypeDef(TypedDict, total=False):
    destination: "DestinationTypeDef"


class PutLogEventsResponseTypeDef(TypedDict, total=False):
    nextSequenceToken: str
    rejectedLogEventsInfo: "RejectedLogEventsInfoTypeDef"


class PutQueryDefinitionResponseTypeDef(TypedDict, total=False):
    queryDefinitionId: str


class PutResourcePolicyResponseTypeDef(TypedDict, total=False):
    resourcePolicy: "ResourcePolicyTypeDef"


class QueryDefinitionTypeDef(TypedDict, total=False):
    queryDefinitionId: str
    name: str
    queryString: str
    lastModified: int
    logGroupNames: List[str]


class QueryInfoTypeDef(TypedDict, total=False):
    queryId: str
    queryString: str
    status: QueryStatus
    createTime: int
    logGroupName: str


class QueryStatisticsTypeDef(TypedDict, total=False):
    recordsMatched: float
    recordsScanned: float
    bytesScanned: float


class RejectedLogEventsInfoTypeDef(TypedDict, total=False):
    tooNewLogEventStartIndex: int
    tooOldLogEventEndIndex: int
    expiredLogEventEndIndex: int


class ResourcePolicyTypeDef(TypedDict, total=False):
    policyName: str
    policyDocument: str
    lastUpdatedTime: int


class ResultFieldTypeDef(TypedDict, total=False):
    field: str
    value: str


class SearchedLogStreamTypeDef(TypedDict, total=False):
    logStreamName: str
    searchedCompletely: bool


class StartQueryResponseTypeDef(TypedDict, total=False):
    queryId: str


class StopQueryResponseTypeDef(TypedDict, total=False):
    success: bool


class SubscriptionFilterTypeDef(TypedDict, total=False):
    filterName: str
    logGroupName: str
    filterPattern: str
    destinationArn: str
    roleArn: str
    distribution: Distribution
    creationTime: int


class TestMetricFilterResponseTypeDef(TypedDict, total=False):
    matches: List["MetricFilterMatchRecordTypeDef"]
