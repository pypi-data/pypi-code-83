"""
Type annotations for application-insights service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/type_defs.html)

Usage::

    ```python
    from mypy_boto3_application_insights.type_defs import ApplicationComponentTypeDef

    data: ApplicationComponentTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_application_insights.literals import (
    CloudWatchEventSource,
    ConfigurationEventResourceType,
    ConfigurationEventStatus,
    FeedbackValue,
    LogFilter,
    OsType,
    SeverityLevel,
    Status,
    Tier,
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
    "ApplicationComponentTypeDef",
    "ApplicationInfoTypeDef",
    "ConfigurationEventTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateLogPatternResponseTypeDef",
    "DescribeApplicationResponseTypeDef",
    "DescribeComponentConfigurationRecommendationResponseTypeDef",
    "DescribeComponentConfigurationResponseTypeDef",
    "DescribeComponentResponseTypeDef",
    "DescribeLogPatternResponseTypeDef",
    "DescribeObservationResponseTypeDef",
    "DescribeProblemObservationsResponseTypeDef",
    "DescribeProblemResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "ListComponentsResponseTypeDef",
    "ListConfigurationHistoryResponseTypeDef",
    "ListLogPatternSetsResponseTypeDef",
    "ListLogPatternsResponseTypeDef",
    "ListProblemsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LogPatternTypeDef",
    "ObservationTypeDef",
    "ProblemTypeDef",
    "RelatedObservationsTypeDef",
    "TagTypeDef",
    "UpdateApplicationResponseTypeDef",
    "UpdateLogPatternResponseTypeDef",
)


class ApplicationComponentTypeDef(TypedDict, total=False):
    ComponentName: str
    ComponentRemarks: str
    ResourceType: str
    OsType: OsType
    Tier: Tier
    Monitor: bool
    DetectedWorkload: Dict[Tier, Dict[str, str]]


class ApplicationInfoTypeDef(TypedDict, total=False):
    ResourceGroupName: str
    LifeCycle: str
    OpsItemSNSTopicArn: str
    OpsCenterEnabled: bool
    CWEMonitorEnabled: bool
    Remarks: str


class ConfigurationEventTypeDef(TypedDict, total=False):
    MonitoredResourceARN: str
    EventStatus: ConfigurationEventStatus
    EventResourceType: ConfigurationEventResourceType
    EventTime: datetime
    EventDetail: str
    EventResourceName: str


class CreateApplicationResponseTypeDef(TypedDict, total=False):
    ApplicationInfo: "ApplicationInfoTypeDef"


class CreateLogPatternResponseTypeDef(TypedDict, total=False):
    LogPattern: "LogPatternTypeDef"
    ResourceGroupName: str


class DescribeApplicationResponseTypeDef(TypedDict, total=False):
    ApplicationInfo: "ApplicationInfoTypeDef"


class DescribeComponentConfigurationRecommendationResponseTypeDef(TypedDict, total=False):
    ComponentConfiguration: str


class DescribeComponentConfigurationResponseTypeDef(TypedDict, total=False):
    Monitor: bool
    Tier: Tier
    ComponentConfiguration: str


class DescribeComponentResponseTypeDef(TypedDict, total=False):
    ApplicationComponent: "ApplicationComponentTypeDef"
    ResourceList: List[str]


class DescribeLogPatternResponseTypeDef(TypedDict, total=False):
    ResourceGroupName: str
    LogPattern: "LogPatternTypeDef"


class DescribeObservationResponseTypeDef(TypedDict, total=False):
    Observation: "ObservationTypeDef"


class DescribeProblemObservationsResponseTypeDef(TypedDict, total=False):
    RelatedObservations: "RelatedObservationsTypeDef"


class DescribeProblemResponseTypeDef(TypedDict, total=False):
    Problem: "ProblemTypeDef"


class ListApplicationsResponseTypeDef(TypedDict, total=False):
    ApplicationInfoList: List["ApplicationInfoTypeDef"]
    NextToken: str


class ListComponentsResponseTypeDef(TypedDict, total=False):
    ApplicationComponentList: List["ApplicationComponentTypeDef"]
    NextToken: str


class ListConfigurationHistoryResponseTypeDef(TypedDict, total=False):
    EventList: List["ConfigurationEventTypeDef"]
    NextToken: str


class ListLogPatternSetsResponseTypeDef(TypedDict, total=False):
    ResourceGroupName: str
    LogPatternSets: List[str]
    NextToken: str


class ListLogPatternsResponseTypeDef(TypedDict, total=False):
    ResourceGroupName: str
    LogPatterns: List["LogPatternTypeDef"]
    NextToken: str


class ListProblemsResponseTypeDef(TypedDict, total=False):
    ProblemList: List["ProblemTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


LogPatternTypeDef = TypedDict(
    "LogPatternTypeDef",
    {"PatternSetName": str, "PatternName": str, "Pattern": str, "Rank": int},
    total=False,
)


class ObservationTypeDef(TypedDict, total=False):
    Id: str
    StartTime: datetime
    EndTime: datetime
    SourceType: str
    SourceARN: str
    LogGroup: str
    LineTime: datetime
    LogText: str
    LogFilter: LogFilter
    MetricNamespace: str
    MetricName: str
    Unit: str
    Value: float
    CloudWatchEventId: str
    CloudWatchEventSource: CloudWatchEventSource
    CloudWatchEventDetailType: str
    HealthEventArn: str
    HealthService: str
    HealthEventTypeCode: str
    HealthEventTypeCategory: str
    HealthEventDescription: str
    CodeDeployDeploymentId: str
    CodeDeployDeploymentGroup: str
    CodeDeployState: str
    CodeDeployApplication: str
    CodeDeployInstanceGroupId: str
    Ec2State: str
    RdsEventCategories: str
    RdsEventMessage: str
    S3EventName: str
    StatesExecutionArn: str
    StatesArn: str
    StatesStatus: str
    StatesInput: str
    EbsEvent: str
    EbsResult: str
    EbsCause: str
    EbsRequestId: str
    XRayFaultPercent: int
    XRayThrottlePercent: int
    XRayErrorPercent: int
    XRayRequestCount: int
    XRayRequestAverageLatency: int
    XRayNodeName: str
    XRayNodeType: str


class ProblemTypeDef(TypedDict, total=False):
    Id: str
    Title: str
    Insights: str
    Status: Status
    AffectedResource: str
    StartTime: datetime
    EndTime: datetime
    SeverityLevel: SeverityLevel
    ResourceGroupName: str
    Feedback: Dict[Literal["INSIGHTS_FEEDBACK"], FeedbackValue]


class RelatedObservationsTypeDef(TypedDict, total=False):
    ObservationList: List["ObservationTypeDef"]


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class UpdateApplicationResponseTypeDef(TypedDict, total=False):
    ApplicationInfo: "ApplicationInfoTypeDef"


class UpdateLogPatternResponseTypeDef(TypedDict, total=False):
    ResourceGroupName: str
    LogPattern: "LogPatternTypeDef"
