"""
Type annotations for codeguruprofiler service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguruprofiler/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codeguruprofiler.type_defs import AddNotificationChannelsResponseTypeDef

    data: AddNotificationChannelsResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_codeguruprofiler.literals import (
    AgentParameterField,
    AggregationPeriod,
    ComputePlatform,
    FeedbackType,
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
    "AddNotificationChannelsResponseTypeDef",
    "AgentConfigurationTypeDef",
    "AgentOrchestrationConfigTypeDef",
    "AggregatedProfileTimeTypeDef",
    "AnomalyInstanceTypeDef",
    "AnomalyTypeDef",
    "BatchGetFrameMetricDataResponseTypeDef",
    "ChannelTypeDef",
    "ConfigureAgentResponseTypeDef",
    "CreateProfilingGroupResponseTypeDef",
    "DescribeProfilingGroupResponseTypeDef",
    "FindingsReportSummaryTypeDef",
    "FrameMetricDatumTypeDef",
    "FrameMetricTypeDef",
    "GetFindingsReportAccountSummaryResponseTypeDef",
    "GetNotificationConfigurationResponseTypeDef",
    "GetPolicyResponseTypeDef",
    "GetProfileResponseTypeDef",
    "GetRecommendationsResponseTypeDef",
    "ListFindingsReportsResponseTypeDef",
    "ListProfileTimesResponseTypeDef",
    "ListProfilingGroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MatchTypeDef",
    "MetricTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PatternTypeDef",
    "ProfileTimeTypeDef",
    "ProfilingGroupDescriptionTypeDef",
    "ProfilingStatusTypeDef",
    "PutPermissionResponseTypeDef",
    "RecommendationTypeDef",
    "RemoveNotificationChannelResponseTypeDef",
    "RemovePermissionResponseTypeDef",
    "TimestampStructureTypeDef",
    "UpdateProfilingGroupResponseTypeDef",
    "UserFeedbackTypeDef",
)


class AddNotificationChannelsResponseTypeDef(TypedDict, total=False):
    notificationConfiguration: "NotificationConfigurationTypeDef"


class _RequiredAgentConfigurationTypeDef(TypedDict):
    periodInSeconds: int
    shouldProfile: bool


class AgentConfigurationTypeDef(_RequiredAgentConfigurationTypeDef, total=False):
    agentParameters: Dict[AgentParameterField, str]


class AgentOrchestrationConfigTypeDef(TypedDict):
    profilingEnabled: bool


class AggregatedProfileTimeTypeDef(TypedDict, total=False):
    period: AggregationPeriod
    start: datetime


_RequiredAnomalyInstanceTypeDef = TypedDict(
    "_RequiredAnomalyInstanceTypeDef", {"id": str, "startTime": datetime}
)
_OptionalAnomalyInstanceTypeDef = TypedDict(
    "_OptionalAnomalyInstanceTypeDef",
    {"endTime": datetime, "userFeedback": "UserFeedbackTypeDef"},
    total=False,
)


class AnomalyInstanceTypeDef(_RequiredAnomalyInstanceTypeDef, _OptionalAnomalyInstanceTypeDef):
    pass


class AnomalyTypeDef(TypedDict):
    instances: List["AnomalyInstanceTypeDef"]
    metric: "MetricTypeDef"
    reason: str


class BatchGetFrameMetricDataResponseTypeDef(TypedDict):
    endTime: datetime
    endTimes: List["TimestampStructureTypeDef"]
    frameMetricData: List["FrameMetricDatumTypeDef"]
    resolution: AggregationPeriod
    startTime: datetime
    unprocessedEndTimes: Dict[str, List["TimestampStructureTypeDef"]]


_RequiredChannelTypeDef = TypedDict(
    "_RequiredChannelTypeDef", {"eventPublishers": List[Literal["AnomalyDetection"]], "uri": str}
)
_OptionalChannelTypeDef = TypedDict("_OptionalChannelTypeDef", {"id": str}, total=False)


class ChannelTypeDef(_RequiredChannelTypeDef, _OptionalChannelTypeDef):
    pass


class ConfigureAgentResponseTypeDef(TypedDict):
    configuration: "AgentConfigurationTypeDef"


class CreateProfilingGroupResponseTypeDef(TypedDict):
    profilingGroup: "ProfilingGroupDescriptionTypeDef"


class DescribeProfilingGroupResponseTypeDef(TypedDict):
    profilingGroup: "ProfilingGroupDescriptionTypeDef"


FindingsReportSummaryTypeDef = TypedDict(
    "FindingsReportSummaryTypeDef",
    {
        "id": str,
        "profileEndTime": datetime,
        "profileStartTime": datetime,
        "profilingGroupName": str,
        "totalNumberOfFindings": int,
    },
    total=False,
)


class FrameMetricDatumTypeDef(TypedDict):
    frameMetric: "FrameMetricTypeDef"
    values: List[float]


FrameMetricTypeDef = TypedDict(
    "FrameMetricTypeDef",
    {"frameName": str, "threadStates": List[str], "type": Literal["AggregatedRelativeTotalTime"]},
)


class _RequiredGetFindingsReportAccountSummaryResponseTypeDef(TypedDict):
    reportSummaries: List["FindingsReportSummaryTypeDef"]


class GetFindingsReportAccountSummaryResponseTypeDef(
    _RequiredGetFindingsReportAccountSummaryResponseTypeDef, total=False
):
    nextToken: str


class GetNotificationConfigurationResponseTypeDef(TypedDict):
    notificationConfiguration: "NotificationConfigurationTypeDef"


class GetPolicyResponseTypeDef(TypedDict):
    policy: str
    revisionId: str


class _RequiredGetProfileResponseTypeDef(TypedDict):
    contentType: str
    profile: Union[bytes, IO[bytes]]


class GetProfileResponseTypeDef(_RequiredGetProfileResponseTypeDef, total=False):
    contentEncoding: str


class GetRecommendationsResponseTypeDef(TypedDict):
    anomalies: List["AnomalyTypeDef"]
    profileEndTime: datetime
    profileStartTime: datetime
    profilingGroupName: str
    recommendations: List["RecommendationTypeDef"]


class _RequiredListFindingsReportsResponseTypeDef(TypedDict):
    findingsReportSummaries: List["FindingsReportSummaryTypeDef"]


class ListFindingsReportsResponseTypeDef(_RequiredListFindingsReportsResponseTypeDef, total=False):
    nextToken: str


class _RequiredListProfileTimesResponseTypeDef(TypedDict):
    profileTimes: List["ProfileTimeTypeDef"]


class ListProfileTimesResponseTypeDef(_RequiredListProfileTimesResponseTypeDef, total=False):
    nextToken: str


class _RequiredListProfilingGroupsResponseTypeDef(TypedDict):
    profilingGroupNames: List[str]


class ListProfilingGroupsResponseTypeDef(_RequiredListProfilingGroupsResponseTypeDef, total=False):
    nextToken: str
    profilingGroups: List["ProfilingGroupDescriptionTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class MatchTypeDef(TypedDict, total=False):
    frameAddress: str
    targetFramesIndex: int
    thresholdBreachValue: float


MetricTypeDef = TypedDict(
    "MetricTypeDef",
    {"frameName": str, "threadStates": List[str], "type": Literal["AggregatedRelativeTotalTime"]},
)


class NotificationConfigurationTypeDef(TypedDict, total=False):
    channels: List["ChannelTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


PatternTypeDef = TypedDict(
    "PatternTypeDef",
    {
        "countersToAggregate": List[str],
        "description": str,
        "id": str,
        "name": str,
        "resolutionSteps": str,
        "targetFrames": List[List[str]],
        "thresholdPercent": float,
    },
    total=False,
)


class ProfileTimeTypeDef(TypedDict, total=False):
    start: datetime


class ProfilingGroupDescriptionTypeDef(TypedDict, total=False):
    agentOrchestrationConfig: "AgentOrchestrationConfigTypeDef"
    arn: str
    computePlatform: ComputePlatform
    createdAt: datetime
    name: str
    profilingStatus: "ProfilingStatusTypeDef"
    tags: Dict[str, str]
    updatedAt: datetime


class ProfilingStatusTypeDef(TypedDict, total=False):
    latestAgentOrchestratedAt: datetime
    latestAgentProfileReportedAt: datetime
    latestAggregatedProfile: "AggregatedProfileTimeTypeDef"


class PutPermissionResponseTypeDef(TypedDict):
    policy: str
    revisionId: str


class RecommendationTypeDef(TypedDict):
    allMatchesCount: int
    allMatchesSum: float
    endTime: datetime
    pattern: "PatternTypeDef"
    startTime: datetime
    topMatches: List["MatchTypeDef"]


class RemoveNotificationChannelResponseTypeDef(TypedDict, total=False):
    notificationConfiguration: "NotificationConfigurationTypeDef"


class RemovePermissionResponseTypeDef(TypedDict):
    policy: str
    revisionId: str


class TimestampStructureTypeDef(TypedDict):
    value: datetime


class UpdateProfilingGroupResponseTypeDef(TypedDict):
    profilingGroup: "ProfilingGroupDescriptionTypeDef"


UserFeedbackTypeDef = TypedDict("UserFeedbackTypeDef", {"type": FeedbackType})
