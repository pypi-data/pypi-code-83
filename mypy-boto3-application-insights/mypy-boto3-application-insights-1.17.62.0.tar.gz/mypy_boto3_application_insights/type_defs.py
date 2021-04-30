"""
Main interface for application-insights service type definitions.

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
    FeedbackKey,
    FeedbackValue,
    LogFilter,
    OsType,
    SeverityLevel,
    Status,
    Tier,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationComponentTypeDef",
    "ApplicationInfoTypeDef",
    "ConfigurationEventTypeDef",
    "LogPatternTypeDef",
    "ObservationTypeDef",
    "ProblemTypeDef",
    "RelatedObservationsTypeDef",
    "TagTypeDef",
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
    "UpdateApplicationResponseTypeDef",
    "UpdateLogPatternResponseTypeDef",
)

ApplicationComponentTypeDef = TypedDict(
    "ApplicationComponentTypeDef",
    {
        "ComponentName": str,
        "ComponentRemarks": str,
        "ResourceType": str,
        "OsType": OsType,
        "Tier": Tier,
        "Monitor": bool,
        "DetectedWorkload": Dict[Tier, Dict[str, str]],
    },
    total=False,
)

ApplicationInfoTypeDef = TypedDict(
    "ApplicationInfoTypeDef",
    {
        "ResourceGroupName": str,
        "LifeCycle": str,
        "OpsItemSNSTopicArn": str,
        "OpsCenterEnabled": bool,
        "CWEMonitorEnabled": bool,
        "Remarks": str,
    },
    total=False,
)

ConfigurationEventTypeDef = TypedDict(
    "ConfigurationEventTypeDef",
    {
        "MonitoredResourceARN": str,
        "EventStatus": ConfigurationEventStatus,
        "EventResourceType": ConfigurationEventResourceType,
        "EventTime": datetime,
        "EventDetail": str,
        "EventResourceName": str,
    },
    total=False,
)

LogPatternTypeDef = TypedDict(
    "LogPatternTypeDef",
    {"PatternSetName": str, "PatternName": str, "Pattern": str, "Rank": int},
    total=False,
)

ObservationTypeDef = TypedDict(
    "ObservationTypeDef",
    {
        "Id": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SourceType": str,
        "SourceARN": str,
        "LogGroup": str,
        "LineTime": datetime,
        "LogText": str,
        "LogFilter": LogFilter,
        "MetricNamespace": str,
        "MetricName": str,
        "Unit": str,
        "Value": float,
        "CloudWatchEventId": str,
        "CloudWatchEventSource": CloudWatchEventSource,
        "CloudWatchEventDetailType": str,
        "HealthEventArn": str,
        "HealthService": str,
        "HealthEventTypeCode": str,
        "HealthEventTypeCategory": str,
        "HealthEventDescription": str,
        "CodeDeployDeploymentId": str,
        "CodeDeployDeploymentGroup": str,
        "CodeDeployState": str,
        "CodeDeployApplication": str,
        "CodeDeployInstanceGroupId": str,
        "Ec2State": str,
        "RdsEventCategories": str,
        "RdsEventMessage": str,
        "S3EventName": str,
        "StatesExecutionArn": str,
        "StatesArn": str,
        "StatesStatus": str,
        "StatesInput": str,
        "EbsEvent": str,
        "EbsResult": str,
        "EbsCause": str,
        "EbsRequestId": str,
        "XRayFaultPercent": int,
        "XRayThrottlePercent": int,
        "XRayErrorPercent": int,
        "XRayRequestCount": int,
        "XRayRequestAverageLatency": int,
        "XRayNodeName": str,
        "XRayNodeType": str,
    },
    total=False,
)

ProblemTypeDef = TypedDict(
    "ProblemTypeDef",
    {
        "Id": str,
        "Title": str,
        "Insights": str,
        "Status": Status,
        "AffectedResource": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "SeverityLevel": SeverityLevel,
        "ResourceGroupName": str,
        "Feedback": Dict[FeedbackKey, FeedbackValue],
    },
    total=False,
)

RelatedObservationsTypeDef = TypedDict(
    "RelatedObservationsTypeDef", {"ObservationList": List["ObservationTypeDef"]}, total=False
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

CreateApplicationResponseTypeDef = TypedDict(
    "CreateApplicationResponseTypeDef", {"ApplicationInfo": "ApplicationInfoTypeDef"}, total=False
)

CreateLogPatternResponseTypeDef = TypedDict(
    "CreateLogPatternResponseTypeDef",
    {"LogPattern": "LogPatternTypeDef", "ResourceGroupName": str},
    total=False,
)

DescribeApplicationResponseTypeDef = TypedDict(
    "DescribeApplicationResponseTypeDef", {"ApplicationInfo": "ApplicationInfoTypeDef"}, total=False
)

DescribeComponentConfigurationRecommendationResponseTypeDef = TypedDict(
    "DescribeComponentConfigurationRecommendationResponseTypeDef",
    {"ComponentConfiguration": str},
    total=False,
)

DescribeComponentConfigurationResponseTypeDef = TypedDict(
    "DescribeComponentConfigurationResponseTypeDef",
    {"Monitor": bool, "Tier": Tier, "ComponentConfiguration": str},
    total=False,
)

DescribeComponentResponseTypeDef = TypedDict(
    "DescribeComponentResponseTypeDef",
    {"ApplicationComponent": "ApplicationComponentTypeDef", "ResourceList": List[str]},
    total=False,
)

DescribeLogPatternResponseTypeDef = TypedDict(
    "DescribeLogPatternResponseTypeDef",
    {"ResourceGroupName": str, "LogPattern": "LogPatternTypeDef"},
    total=False,
)

DescribeObservationResponseTypeDef = TypedDict(
    "DescribeObservationResponseTypeDef", {"Observation": "ObservationTypeDef"}, total=False
)

DescribeProblemObservationsResponseTypeDef = TypedDict(
    "DescribeProblemObservationsResponseTypeDef",
    {"RelatedObservations": "RelatedObservationsTypeDef"},
    total=False,
)

DescribeProblemResponseTypeDef = TypedDict(
    "DescribeProblemResponseTypeDef", {"Problem": "ProblemTypeDef"}, total=False
)

ListApplicationsResponseTypeDef = TypedDict(
    "ListApplicationsResponseTypeDef",
    {"ApplicationInfoList": List["ApplicationInfoTypeDef"], "NextToken": str},
    total=False,
)

ListComponentsResponseTypeDef = TypedDict(
    "ListComponentsResponseTypeDef",
    {"ApplicationComponentList": List["ApplicationComponentTypeDef"], "NextToken": str},
    total=False,
)

ListConfigurationHistoryResponseTypeDef = TypedDict(
    "ListConfigurationHistoryResponseTypeDef",
    {"EventList": List["ConfigurationEventTypeDef"], "NextToken": str},
    total=False,
)

ListLogPatternSetsResponseTypeDef = TypedDict(
    "ListLogPatternSetsResponseTypeDef",
    {"ResourceGroupName": str, "LogPatternSets": List[str], "NextToken": str},
    total=False,
)

ListLogPatternsResponseTypeDef = TypedDict(
    "ListLogPatternsResponseTypeDef",
    {"ResourceGroupName": str, "LogPatterns": List["LogPatternTypeDef"], "NextToken": str},
    total=False,
)

ListProblemsResponseTypeDef = TypedDict(
    "ListProblemsResponseTypeDef",
    {"ProblemList": List["ProblemTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

UpdateApplicationResponseTypeDef = TypedDict(
    "UpdateApplicationResponseTypeDef", {"ApplicationInfo": "ApplicationInfoTypeDef"}, total=False
)

UpdateLogPatternResponseTypeDef = TypedDict(
    "UpdateLogPatternResponseTypeDef",
    {"ResourceGroupName": str, "LogPattern": "LogPatternTypeDef"},
    total=False,
)
