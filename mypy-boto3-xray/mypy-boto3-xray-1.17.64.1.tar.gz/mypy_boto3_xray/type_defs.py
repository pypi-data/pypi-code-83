"""
Type annotations for xray service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_xray/type_defs.html)

Usage::

    ```python
    from mypy_boto3_xray.type_defs import AliasTypeDef

    data: AliasTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_xray.literals import (
    EncryptionStatus,
    EncryptionType,
    InsightState,
    SamplingStrategyName,
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
    "AliasTypeDef",
    "AnnotationValueTypeDef",
    "AnomalousServiceTypeDef",
    "AvailabilityZoneDetailTypeDef",
    "BackendConnectionErrorsTypeDef",
    "BatchGetTracesResultTypeDef",
    "CreateGroupResultTypeDef",
    "CreateSamplingRuleResultTypeDef",
    "DeleteSamplingRuleResultTypeDef",
    "EdgeStatisticsTypeDef",
    "EdgeTypeDef",
    "EncryptionConfigTypeDef",
    "ErrorRootCauseEntityTypeDef",
    "ErrorRootCauseServiceTypeDef",
    "ErrorRootCauseTypeDef",
    "ErrorStatisticsTypeDef",
    "FaultRootCauseEntityTypeDef",
    "FaultRootCauseServiceTypeDef",
    "FaultRootCauseTypeDef",
    "FaultStatisticsTypeDef",
    "ForecastStatisticsTypeDef",
    "GetEncryptionConfigResultTypeDef",
    "GetGroupResultTypeDef",
    "GetGroupsResultTypeDef",
    "GetInsightEventsResultTypeDef",
    "GetInsightImpactGraphResultTypeDef",
    "GetInsightResultTypeDef",
    "GetInsightSummariesResultTypeDef",
    "GetSamplingRulesResultTypeDef",
    "GetSamplingStatisticSummariesResultTypeDef",
    "GetSamplingTargetsResultTypeDef",
    "GetServiceGraphResultTypeDef",
    "GetTimeSeriesServiceStatisticsResultTypeDef",
    "GetTraceGraphResultTypeDef",
    "GetTraceSummariesResultTypeDef",
    "GroupSummaryTypeDef",
    "GroupTypeDef",
    "HistogramEntryTypeDef",
    "HttpTypeDef",
    "InsightEventTypeDef",
    "InsightImpactGraphEdgeTypeDef",
    "InsightImpactGraphServiceTypeDef",
    "InsightSummaryTypeDef",
    "InsightTypeDef",
    "InsightsConfigurationTypeDef",
    "InstanceIdDetailTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutEncryptionConfigResultTypeDef",
    "PutTraceSegmentsResultTypeDef",
    "RequestImpactStatisticsTypeDef",
    "ResourceARNDetailTypeDef",
    "ResponseTimeRootCauseEntityTypeDef",
    "ResponseTimeRootCauseServiceTypeDef",
    "ResponseTimeRootCauseTypeDef",
    "RootCauseExceptionTypeDef",
    "SamplingRuleRecordTypeDef",
    "SamplingRuleTypeDef",
    "SamplingRuleUpdateTypeDef",
    "SamplingStatisticSummaryTypeDef",
    "SamplingStatisticsDocumentTypeDef",
    "SamplingStrategyTypeDef",
    "SamplingTargetDocumentTypeDef",
    "SegmentTypeDef",
    "ServiceIdTypeDef",
    "ServiceStatisticsTypeDef",
    "ServiceTypeDef",
    "TagTypeDef",
    "TelemetryRecordTypeDef",
    "TimeSeriesServiceStatisticsTypeDef",
    "TraceSummaryTypeDef",
    "TraceTypeDef",
    "TraceUserTypeDef",
    "UnprocessedStatisticsTypeDef",
    "UnprocessedTraceSegmentTypeDef",
    "UpdateGroupResultTypeDef",
    "UpdateSamplingRuleResultTypeDef",
    "ValueWithServiceIdsTypeDef",
)

AliasTypeDef = TypedDict(
    "AliasTypeDef", {"Name": str, "Names": List[str], "Type": str}, total=False
)


class AnnotationValueTypeDef(TypedDict, total=False):
    NumberValue: float
    BooleanValue: bool
    StringValue: str


class AnomalousServiceTypeDef(TypedDict, total=False):
    ServiceId: "ServiceIdTypeDef"


class AvailabilityZoneDetailTypeDef(TypedDict, total=False):
    Name: str


class BackendConnectionErrorsTypeDef(TypedDict, total=False):
    TimeoutCount: int
    ConnectionRefusedCount: int
    HTTPCode4XXCount: int
    HTTPCode5XXCount: int
    UnknownHostCount: int
    OtherCount: int


class BatchGetTracesResultTypeDef(TypedDict, total=False):
    Traces: List["TraceTypeDef"]
    UnprocessedTraceIds: List[str]
    NextToken: str


class CreateGroupResultTypeDef(TypedDict, total=False):
    Group: "GroupTypeDef"


class CreateSamplingRuleResultTypeDef(TypedDict, total=False):
    SamplingRuleRecord: "SamplingRuleRecordTypeDef"


class DeleteSamplingRuleResultTypeDef(TypedDict, total=False):
    SamplingRuleRecord: "SamplingRuleRecordTypeDef"


class EdgeStatisticsTypeDef(TypedDict, total=False):
    OkCount: int
    ErrorStatistics: "ErrorStatisticsTypeDef"
    FaultStatistics: "FaultStatisticsTypeDef"
    TotalCount: int
    TotalResponseTime: float


class EdgeTypeDef(TypedDict, total=False):
    ReferenceId: int
    StartTime: datetime
    EndTime: datetime
    SummaryStatistics: "EdgeStatisticsTypeDef"
    ResponseTimeHistogram: List["HistogramEntryTypeDef"]
    Aliases: List["AliasTypeDef"]


EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {"KeyId": str, "Status": EncryptionStatus, "Type": EncryptionType},
    total=False,
)


class ErrorRootCauseEntityTypeDef(TypedDict, total=False):
    Name: str
    Exceptions: List["RootCauseExceptionTypeDef"]
    Remote: bool


ErrorRootCauseServiceTypeDef = TypedDict(
    "ErrorRootCauseServiceTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List["ErrorRootCauseEntityTypeDef"],
        "Inferred": bool,
    },
    total=False,
)


class ErrorRootCauseTypeDef(TypedDict, total=False):
    Services: List["ErrorRootCauseServiceTypeDef"]
    ClientImpacting: bool


class ErrorStatisticsTypeDef(TypedDict, total=False):
    ThrottleCount: int
    OtherCount: int
    TotalCount: int


class FaultRootCauseEntityTypeDef(TypedDict, total=False):
    Name: str
    Exceptions: List["RootCauseExceptionTypeDef"]
    Remote: bool


FaultRootCauseServiceTypeDef = TypedDict(
    "FaultRootCauseServiceTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List["FaultRootCauseEntityTypeDef"],
        "Inferred": bool,
    },
    total=False,
)


class FaultRootCauseTypeDef(TypedDict, total=False):
    Services: List["FaultRootCauseServiceTypeDef"]
    ClientImpacting: bool


class FaultStatisticsTypeDef(TypedDict, total=False):
    OtherCount: int
    TotalCount: int


class ForecastStatisticsTypeDef(TypedDict, total=False):
    FaultCountHigh: int
    FaultCountLow: int


class GetEncryptionConfigResultTypeDef(TypedDict, total=False):
    EncryptionConfig: "EncryptionConfigTypeDef"


class GetGroupResultTypeDef(TypedDict, total=False):
    Group: "GroupTypeDef"


class GetGroupsResultTypeDef(TypedDict, total=False):
    Groups: List["GroupSummaryTypeDef"]
    NextToken: str


class GetInsightEventsResultTypeDef(TypedDict, total=False):
    InsightEvents: List["InsightEventTypeDef"]
    NextToken: str


class GetInsightImpactGraphResultTypeDef(TypedDict, total=False):
    InsightId: str
    StartTime: datetime
    EndTime: datetime
    ServiceGraphStartTime: datetime
    ServiceGraphEndTime: datetime
    Services: List["InsightImpactGraphServiceTypeDef"]
    NextToken: str


class GetInsightResultTypeDef(TypedDict, total=False):
    Insight: "InsightTypeDef"


class GetInsightSummariesResultTypeDef(TypedDict, total=False):
    InsightSummaries: List["InsightSummaryTypeDef"]
    NextToken: str


class GetSamplingRulesResultTypeDef(TypedDict, total=False):
    SamplingRuleRecords: List["SamplingRuleRecordTypeDef"]
    NextToken: str


class GetSamplingStatisticSummariesResultTypeDef(TypedDict, total=False):
    SamplingStatisticSummaries: List["SamplingStatisticSummaryTypeDef"]
    NextToken: str


class GetSamplingTargetsResultTypeDef(TypedDict, total=False):
    SamplingTargetDocuments: List["SamplingTargetDocumentTypeDef"]
    LastRuleModification: datetime
    UnprocessedStatistics: List["UnprocessedStatisticsTypeDef"]


class GetServiceGraphResultTypeDef(TypedDict, total=False):
    StartTime: datetime
    EndTime: datetime
    Services: List["ServiceTypeDef"]
    ContainsOldGroupVersions: bool
    NextToken: str


class GetTimeSeriesServiceStatisticsResultTypeDef(TypedDict, total=False):
    TimeSeriesServiceStatistics: List["TimeSeriesServiceStatisticsTypeDef"]
    ContainsOldGroupVersions: bool
    NextToken: str


class GetTraceGraphResultTypeDef(TypedDict, total=False):
    Services: List["ServiceTypeDef"]
    NextToken: str


class GetTraceSummariesResultTypeDef(TypedDict, total=False):
    TraceSummaries: List["TraceSummaryTypeDef"]
    ApproximateTime: datetime
    TracesProcessedCount: int
    NextToken: str


class GroupSummaryTypeDef(TypedDict, total=False):
    GroupName: str
    GroupARN: str
    FilterExpression: str
    InsightsConfiguration: "InsightsConfigurationTypeDef"


class GroupTypeDef(TypedDict, total=False):
    GroupName: str
    GroupARN: str
    FilterExpression: str
    InsightsConfiguration: "InsightsConfigurationTypeDef"


class HistogramEntryTypeDef(TypedDict, total=False):
    Value: float
    Count: int


class HttpTypeDef(TypedDict, total=False):
    HttpURL: str
    HttpStatus: int
    HttpMethod: str
    UserAgent: str
    ClientIp: str


class InsightEventTypeDef(TypedDict, total=False):
    Summary: str
    EventTime: datetime
    ClientRequestImpactStatistics: "RequestImpactStatisticsTypeDef"
    RootCauseServiceRequestImpactStatistics: "RequestImpactStatisticsTypeDef"
    TopAnomalousServices: List["AnomalousServiceTypeDef"]


class InsightImpactGraphEdgeTypeDef(TypedDict, total=False):
    ReferenceId: int


InsightImpactGraphServiceTypeDef = TypedDict(
    "InsightImpactGraphServiceTypeDef",
    {
        "ReferenceId": int,
        "Type": str,
        "Name": str,
        "Names": List[str],
        "AccountId": str,
        "Edges": List["InsightImpactGraphEdgeTypeDef"],
    },
    total=False,
)


class InsightSummaryTypeDef(TypedDict, total=False):
    InsightId: str
    GroupARN: str
    GroupName: str
    RootCauseServiceId: "ServiceIdTypeDef"
    Categories: List[Literal["FAULT"]]
    State: InsightState
    StartTime: datetime
    EndTime: datetime
    Summary: str
    ClientRequestImpactStatistics: "RequestImpactStatisticsTypeDef"
    RootCauseServiceRequestImpactStatistics: "RequestImpactStatisticsTypeDef"
    TopAnomalousServices: List["AnomalousServiceTypeDef"]
    LastUpdateTime: datetime


class InsightTypeDef(TypedDict, total=False):
    InsightId: str
    GroupARN: str
    GroupName: str
    RootCauseServiceId: "ServiceIdTypeDef"
    Categories: List[Literal["FAULT"]]
    State: InsightState
    StartTime: datetime
    EndTime: datetime
    Summary: str
    ClientRequestImpactStatistics: "RequestImpactStatisticsTypeDef"
    RootCauseServiceRequestImpactStatistics: "RequestImpactStatisticsTypeDef"
    TopAnomalousServices: List["AnomalousServiceTypeDef"]


class InsightsConfigurationTypeDef(TypedDict, total=False):
    InsightsEnabled: bool
    NotificationsEnabled: bool


class InstanceIdDetailTypeDef(TypedDict, total=False):
    Id: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]
    NextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PutEncryptionConfigResultTypeDef(TypedDict, total=False):
    EncryptionConfig: "EncryptionConfigTypeDef"


class PutTraceSegmentsResultTypeDef(TypedDict, total=False):
    UnprocessedTraceSegments: List["UnprocessedTraceSegmentTypeDef"]


class RequestImpactStatisticsTypeDef(TypedDict, total=False):
    FaultCount: int
    OkCount: int
    TotalCount: int


class ResourceARNDetailTypeDef(TypedDict, total=False):
    ARN: str


class ResponseTimeRootCauseEntityTypeDef(TypedDict, total=False):
    Name: str
    Coverage: float
    Remote: bool


ResponseTimeRootCauseServiceTypeDef = TypedDict(
    "ResponseTimeRootCauseServiceTypeDef",
    {
        "Name": str,
        "Names": List[str],
        "Type": str,
        "AccountId": str,
        "EntityPath": List["ResponseTimeRootCauseEntityTypeDef"],
        "Inferred": bool,
    },
    total=False,
)


class ResponseTimeRootCauseTypeDef(TypedDict, total=False):
    Services: List["ResponseTimeRootCauseServiceTypeDef"]
    ClientImpacting: bool


class RootCauseExceptionTypeDef(TypedDict, total=False):
    Name: str
    Message: str


class SamplingRuleRecordTypeDef(TypedDict, total=False):
    SamplingRule: "SamplingRuleTypeDef"
    CreatedAt: datetime
    ModifiedAt: datetime


class _RequiredSamplingRuleTypeDef(TypedDict):
    ResourceARN: str
    Priority: int
    FixedRate: float
    ReservoirSize: int
    ServiceName: str
    ServiceType: str
    Host: str
    HTTPMethod: str
    URLPath: str
    Version: int


class SamplingRuleTypeDef(_RequiredSamplingRuleTypeDef, total=False):
    RuleName: str
    RuleARN: str
    Attributes: Dict[str, str]


class SamplingRuleUpdateTypeDef(TypedDict, total=False):
    RuleName: str
    RuleARN: str
    ResourceARN: str
    Priority: int
    FixedRate: float
    ReservoirSize: int
    Host: str
    ServiceName: str
    ServiceType: str
    HTTPMethod: str
    URLPath: str
    Attributes: Dict[str, str]


class SamplingStatisticSummaryTypeDef(TypedDict, total=False):
    RuleName: str
    Timestamp: datetime
    RequestCount: int
    BorrowCount: int
    SampledCount: int


class _RequiredSamplingStatisticsDocumentTypeDef(TypedDict):
    RuleName: str
    ClientID: str
    Timestamp: datetime
    RequestCount: int
    SampledCount: int


class SamplingStatisticsDocumentTypeDef(_RequiredSamplingStatisticsDocumentTypeDef, total=False):
    BorrowCount: int


class SamplingStrategyTypeDef(TypedDict, total=False):
    Name: SamplingStrategyName
    Value: float


class SamplingTargetDocumentTypeDef(TypedDict, total=False):
    RuleName: str
    FixedRate: float
    ReservoirQuota: int
    ReservoirQuotaTTL: datetime
    Interval: int


class SegmentTypeDef(TypedDict, total=False):
    Id: str
    Document: str


ServiceIdTypeDef = TypedDict(
    "ServiceIdTypeDef",
    {"Name": str, "Names": List[str], "AccountId": str, "Type": str},
    total=False,
)


class ServiceStatisticsTypeDef(TypedDict, total=False):
    OkCount: int
    ErrorStatistics: "ErrorStatisticsTypeDef"
    FaultStatistics: "FaultStatisticsTypeDef"
    TotalCount: int
    TotalResponseTime: float


ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "ReferenceId": int,
        "Name": str,
        "Names": List[str],
        "Root": bool,
        "AccountId": str,
        "Type": str,
        "State": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "Edges": List["EdgeTypeDef"],
        "SummaryStatistics": "ServiceStatisticsTypeDef",
        "DurationHistogram": List["HistogramEntryTypeDef"],
        "ResponseTimeHistogram": List["HistogramEntryTypeDef"],
    },
    total=False,
)


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class _RequiredTelemetryRecordTypeDef(TypedDict):
    Timestamp: datetime


class TelemetryRecordTypeDef(_RequiredTelemetryRecordTypeDef, total=False):
    SegmentsReceivedCount: int
    SegmentsSentCount: int
    SegmentsSpilloverCount: int
    SegmentsRejectedCount: int
    BackendConnectionErrors: "BackendConnectionErrorsTypeDef"


class TimeSeriesServiceStatisticsTypeDef(TypedDict, total=False):
    Timestamp: datetime
    EdgeSummaryStatistics: "EdgeStatisticsTypeDef"
    ServiceSummaryStatistics: "ServiceStatisticsTypeDef"
    ServiceForecastStatistics: "ForecastStatisticsTypeDef"
    ResponseTimeHistogram: List["HistogramEntryTypeDef"]


class TraceSummaryTypeDef(TypedDict, total=False):
    Id: str
    Duration: float
    ResponseTime: float
    HasFault: bool
    HasError: bool
    HasThrottle: bool
    IsPartial: bool
    Http: "HttpTypeDef"
    Annotations: Dict[str, List["ValueWithServiceIdsTypeDef"]]
    Users: List["TraceUserTypeDef"]
    ServiceIds: List["ServiceIdTypeDef"]
    ResourceARNs: List["ResourceARNDetailTypeDef"]
    InstanceIds: List["InstanceIdDetailTypeDef"]
    AvailabilityZones: List["AvailabilityZoneDetailTypeDef"]
    EntryPoint: "ServiceIdTypeDef"
    FaultRootCauses: List["FaultRootCauseTypeDef"]
    ErrorRootCauses: List["ErrorRootCauseTypeDef"]
    ResponseTimeRootCauses: List["ResponseTimeRootCauseTypeDef"]
    Revision: int
    MatchedEventTime: datetime


class TraceTypeDef(TypedDict, total=False):
    Id: str
    Duration: float
    LimitExceeded: bool
    Segments: List["SegmentTypeDef"]


class TraceUserTypeDef(TypedDict, total=False):
    UserName: str
    ServiceIds: List["ServiceIdTypeDef"]


class UnprocessedStatisticsTypeDef(TypedDict, total=False):
    RuleName: str
    ErrorCode: str
    Message: str


class UnprocessedTraceSegmentTypeDef(TypedDict, total=False):
    Id: str
    ErrorCode: str
    Message: str


class UpdateGroupResultTypeDef(TypedDict, total=False):
    Group: "GroupTypeDef"


class UpdateSamplingRuleResultTypeDef(TypedDict, total=False):
    SamplingRuleRecord: "SamplingRuleRecordTypeDef"


class ValueWithServiceIdsTypeDef(TypedDict, total=False):
    AnnotationValue: "AnnotationValueTypeDef"
    ServiceIds: List["ServiceIdTypeDef"]
