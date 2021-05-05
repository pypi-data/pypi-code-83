"""
Type annotations for compute-optimizer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_compute_optimizer.type_defs import AutoScalingGroupConfigurationTypeDef

    data: AutoScalingGroupConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_compute_optimizer.literals import (
    EBSFinding,
    EBSMetricName,
    FilterName,
    Finding,
    FindingReasonCode,
    JobFilterName,
    JobStatus,
    LambdaFunctionMemoryMetricStatistic,
    LambdaFunctionMetricName,
    LambdaFunctionMetricStatistic,
    LambdaFunctionRecommendationFilterName,
    LambdaFunctionRecommendationFinding,
    LambdaFunctionRecommendationFindingReasonCode,
    MetricName,
    MetricStatistic,
    RecommendationSourceType,
    ResourceType,
    Status,
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
    "AutoScalingGroupConfigurationTypeDef",
    "AutoScalingGroupRecommendationOptionTypeDef",
    "AutoScalingGroupRecommendationTypeDef",
    "DescribeRecommendationExportJobsResponseTypeDef",
    "EBSFilterTypeDef",
    "EBSUtilizationMetricTypeDef",
    "ExportAutoScalingGroupRecommendationsResponseTypeDef",
    "ExportDestinationTypeDef",
    "ExportEC2InstanceRecommendationsResponseTypeDef",
    "FilterTypeDef",
    "GetAutoScalingGroupRecommendationsResponseTypeDef",
    "GetEBSVolumeRecommendationsResponseTypeDef",
    "GetEC2InstanceRecommendationsResponseTypeDef",
    "GetEC2RecommendationProjectedMetricsResponseTypeDef",
    "GetEnrollmentStatusResponseTypeDef",
    "GetLambdaFunctionRecommendationsResponseTypeDef",
    "GetRecommendationErrorTypeDef",
    "GetRecommendationSummariesResponseTypeDef",
    "InstanceRecommendationOptionTypeDef",
    "InstanceRecommendationTypeDef",
    "JobFilterTypeDef",
    "LambdaFunctionMemoryProjectedMetricTypeDef",
    "LambdaFunctionMemoryRecommendationOptionTypeDef",
    "LambdaFunctionRecommendationFilterTypeDef",
    "LambdaFunctionRecommendationTypeDef",
    "LambdaFunctionUtilizationMetricTypeDef",
    "ProjectedMetricTypeDef",
    "ReasonCodeSummaryTypeDef",
    "RecommendationExportJobTypeDef",
    "RecommendationSourceTypeDef",
    "RecommendationSummaryTypeDef",
    "RecommendedOptionProjectedMetricTypeDef",
    "S3DestinationConfigTypeDef",
    "S3DestinationTypeDef",
    "SummaryTypeDef",
    "UpdateEnrollmentStatusResponseTypeDef",
    "UtilizationMetricTypeDef",
    "VolumeConfigurationTypeDef",
    "VolumeRecommendationOptionTypeDef",
    "VolumeRecommendationTypeDef",
)


class AutoScalingGroupConfigurationTypeDef(TypedDict, total=False):
    desiredCapacity: int
    minSize: int
    maxSize: int
    instanceType: str


class AutoScalingGroupRecommendationOptionTypeDef(TypedDict, total=False):
    configuration: "AutoScalingGroupConfigurationTypeDef"
    projectedUtilizationMetrics: List["UtilizationMetricTypeDef"]
    performanceRisk: float
    rank: int


class AutoScalingGroupRecommendationTypeDef(TypedDict, total=False):
    accountId: str
    autoScalingGroupArn: str
    autoScalingGroupName: str
    finding: Finding
    utilizationMetrics: List["UtilizationMetricTypeDef"]
    lookBackPeriodInDays: float
    currentConfiguration: "AutoScalingGroupConfigurationTypeDef"
    recommendationOptions: List["AutoScalingGroupRecommendationOptionTypeDef"]
    lastRefreshTimestamp: datetime


class DescribeRecommendationExportJobsResponseTypeDef(TypedDict, total=False):
    recommendationExportJobs: List["RecommendationExportJobTypeDef"]
    nextToken: str


class EBSFilterTypeDef(TypedDict, total=False):
    name: Literal["Finding"]
    values: List[str]


class EBSUtilizationMetricTypeDef(TypedDict, total=False):
    name: EBSMetricName
    statistic: MetricStatistic
    value: float


class ExportAutoScalingGroupRecommendationsResponseTypeDef(TypedDict, total=False):
    jobId: str
    s3Destination: "S3DestinationTypeDef"


class ExportDestinationTypeDef(TypedDict, total=False):
    s3: "S3DestinationTypeDef"


class ExportEC2InstanceRecommendationsResponseTypeDef(TypedDict, total=False):
    jobId: str
    s3Destination: "S3DestinationTypeDef"


class FilterTypeDef(TypedDict, total=False):
    name: FilterName
    values: List[str]


class GetAutoScalingGroupRecommendationsResponseTypeDef(TypedDict, total=False):
    nextToken: str
    autoScalingGroupRecommendations: List["AutoScalingGroupRecommendationTypeDef"]
    errors: List["GetRecommendationErrorTypeDef"]


class GetEBSVolumeRecommendationsResponseTypeDef(TypedDict, total=False):
    nextToken: str
    volumeRecommendations: List["VolumeRecommendationTypeDef"]
    errors: List["GetRecommendationErrorTypeDef"]


class GetEC2InstanceRecommendationsResponseTypeDef(TypedDict, total=False):
    nextToken: str
    instanceRecommendations: List["InstanceRecommendationTypeDef"]
    errors: List["GetRecommendationErrorTypeDef"]


class GetEC2RecommendationProjectedMetricsResponseTypeDef(TypedDict, total=False):
    recommendedOptionProjectedMetrics: List["RecommendedOptionProjectedMetricTypeDef"]


class GetEnrollmentStatusResponseTypeDef(TypedDict, total=False):
    status: Status
    statusReason: str
    memberAccountsEnrolled: bool


class GetLambdaFunctionRecommendationsResponseTypeDef(TypedDict, total=False):
    nextToken: str
    lambdaFunctionRecommendations: List["LambdaFunctionRecommendationTypeDef"]


class GetRecommendationErrorTypeDef(TypedDict, total=False):
    identifier: str
    code: str
    message: str


class GetRecommendationSummariesResponseTypeDef(TypedDict, total=False):
    nextToken: str
    recommendationSummaries: List["RecommendationSummaryTypeDef"]


class InstanceRecommendationOptionTypeDef(TypedDict, total=False):
    instanceType: str
    projectedUtilizationMetrics: List["UtilizationMetricTypeDef"]
    performanceRisk: float
    rank: int


class InstanceRecommendationTypeDef(TypedDict, total=False):
    instanceArn: str
    accountId: str
    instanceName: str
    currentInstanceType: str
    finding: Finding
    utilizationMetrics: List["UtilizationMetricTypeDef"]
    lookBackPeriodInDays: float
    recommendationOptions: List["InstanceRecommendationOptionTypeDef"]
    recommendationSources: List["RecommendationSourceTypeDef"]
    lastRefreshTimestamp: datetime


class JobFilterTypeDef(TypedDict, total=False):
    name: JobFilterName
    values: List[str]


class LambdaFunctionMemoryProjectedMetricTypeDef(TypedDict, total=False):
    name: Literal["Duration"]
    statistic: LambdaFunctionMemoryMetricStatistic
    value: float


class LambdaFunctionMemoryRecommendationOptionTypeDef(TypedDict, total=False):
    rank: int
    memorySize: int
    projectedUtilizationMetrics: List["LambdaFunctionMemoryProjectedMetricTypeDef"]


class LambdaFunctionRecommendationFilterTypeDef(TypedDict, total=False):
    name: LambdaFunctionRecommendationFilterName
    values: List[str]


class LambdaFunctionRecommendationTypeDef(TypedDict, total=False):
    functionArn: str
    functionVersion: str
    accountId: str
    currentMemorySize: int
    numberOfInvocations: int
    utilizationMetrics: List["LambdaFunctionUtilizationMetricTypeDef"]
    lookbackPeriodInDays: float
    lastRefreshTimestamp: datetime
    finding: LambdaFunctionRecommendationFinding
    findingReasonCodes: List[LambdaFunctionRecommendationFindingReasonCode]
    memorySizeRecommendationOptions: List["LambdaFunctionMemoryRecommendationOptionTypeDef"]


class LambdaFunctionUtilizationMetricTypeDef(TypedDict, total=False):
    name: LambdaFunctionMetricName
    statistic: LambdaFunctionMetricStatistic
    value: float


class ProjectedMetricTypeDef(TypedDict, total=False):
    name: MetricName
    timestamps: List[datetime]
    values: List[float]


class ReasonCodeSummaryTypeDef(TypedDict, total=False):
    name: FindingReasonCode
    value: float


class RecommendationExportJobTypeDef(TypedDict, total=False):
    jobId: str
    destination: "ExportDestinationTypeDef"
    resourceType: ResourceType
    status: JobStatus
    creationTimestamp: datetime
    lastUpdatedTimestamp: datetime
    failureReason: str


class RecommendationSourceTypeDef(TypedDict, total=False):
    recommendationSourceArn: str
    recommendationSourceType: RecommendationSourceType


class RecommendationSummaryTypeDef(TypedDict, total=False):
    summaries: List["SummaryTypeDef"]
    recommendationResourceType: RecommendationSourceType
    accountId: str


class RecommendedOptionProjectedMetricTypeDef(TypedDict, total=False):
    recommendedInstanceType: str
    rank: int
    projectedMetrics: List["ProjectedMetricTypeDef"]


class S3DestinationConfigTypeDef(TypedDict, total=False):
    bucket: str
    keyPrefix: str


class S3DestinationTypeDef(TypedDict, total=False):
    bucket: str
    key: str
    metadataKey: str


class SummaryTypeDef(TypedDict, total=False):
    name: Finding
    value: float
    reasonCodeSummaries: List["ReasonCodeSummaryTypeDef"]


class UpdateEnrollmentStatusResponseTypeDef(TypedDict, total=False):
    status: Status
    statusReason: str


class UtilizationMetricTypeDef(TypedDict, total=False):
    name: MetricName
    statistic: MetricStatistic
    value: float


class VolumeConfigurationTypeDef(TypedDict, total=False):
    volumeType: str
    volumeSize: int
    volumeBaselineIOPS: int
    volumeBurstIOPS: int
    volumeBaselineThroughput: int
    volumeBurstThroughput: int


class VolumeRecommendationOptionTypeDef(TypedDict, total=False):
    configuration: "VolumeConfigurationTypeDef"
    performanceRisk: float
    rank: int


class VolumeRecommendationTypeDef(TypedDict, total=False):
    volumeArn: str
    accountId: str
    currentConfiguration: "VolumeConfigurationTypeDef"
    finding: EBSFinding
    utilizationMetrics: List["EBSUtilizationMetricTypeDef"]
    lookBackPeriodInDays: float
    volumeRecommendationOptions: List["VolumeRecommendationOptionTypeDef"]
    lastRefreshTimestamp: datetime
