"""
Type annotations for codeguruprofiler service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/literals.html)

Usage::

    ```python
    from mypy_boto3_codeguruprofiler.literals import ActionGroup

    data: ActionGroup = "agentPermissions"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActionGroup",
    "AgentParameterField",
    "AggregationPeriod",
    "ComputePlatform",
    "EventPublisher",
    "FeedbackType",
    "ListProfileTimesPaginatorName",
    "MetadataField",
    "MetricType",
    "OrderBy",
)


ActionGroup = Literal["agentPermissions"]
AgentParameterField = Literal[
    "MaxStackDepth",
    "MemoryUsageLimitPercent",
    "MinimumTimeForReportingInMilliseconds",
    "ReportingIntervalInMilliseconds",
    "SamplingIntervalInMilliseconds",
]
AggregationPeriod = Literal["P1D", "PT1H", "PT5M"]
ComputePlatform = Literal["AWSLambda", "Default"]
EventPublisher = Literal["AnomalyDetection"]
FeedbackType = Literal["Negative", "Positive"]
ListProfileTimesPaginatorName = Literal["list_profile_times"]
MetadataField = Literal[
    "AgentId",
    "AwsRequestId",
    "ComputePlatform",
    "ExecutionEnvironment",
    "LambdaFunctionArn",
    "LambdaMemoryLimitInMB",
    "LambdaPreviousExecutionTimeInMilliseconds",
    "LambdaRemainingTimeInMilliseconds",
    "LambdaTimeGapBetweenInvokesInMilliseconds",
]
MetricType = Literal["AggregatedRelativeTotalTime"]
OrderBy = Literal["TimestampAscending", "TimestampDescending"]
