"""
Type annotations for compute-optimizer service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_compute_optimizer/literals.html)

Usage::

    ```python
    from mypy_boto3_compute_optimizer.literals import EBSFilterName

    data: EBSFilterName = "Finding"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "EBSFilterName",
    "EBSFinding",
    "EBSMetricName",
    "ExportableAutoScalingGroupField",
    "ExportableInstanceField",
    "FileFormat",
    "FilterName",
    "Finding",
    "FindingReasonCode",
    "JobFilterName",
    "JobStatus",
    "LambdaFunctionMemoryMetricName",
    "LambdaFunctionMemoryMetricStatistic",
    "LambdaFunctionMetricName",
    "LambdaFunctionMetricStatistic",
    "LambdaFunctionRecommendationFilterName",
    "LambdaFunctionRecommendationFinding",
    "LambdaFunctionRecommendationFindingReasonCode",
    "MetricName",
    "MetricStatistic",
    "RecommendationSourceType",
    "ResourceType",
    "Status",
)


EBSFilterName = Literal["Finding"]
EBSFinding = Literal["NotOptimized", "Optimized"]
EBSMetricName = Literal[
    "VolumeReadBytesPerSecond",
    "VolumeReadOpsPerSecond",
    "VolumeWriteBytesPerSecond",
    "VolumeWriteOpsPerSecond",
]
ExportableAutoScalingGroupField = Literal[
    "AccountId",
    "AutoScalingGroupArn",
    "AutoScalingGroupName",
    "CurrentConfigurationDesiredCapacity",
    "CurrentConfigurationInstanceType",
    "CurrentConfigurationMaxSize",
    "CurrentConfigurationMinSize",
    "CurrentMemory",
    "CurrentNetwork",
    "CurrentOnDemandPrice",
    "CurrentStandardOneYearNoUpfrontReservedPrice",
    "CurrentStandardThreeYearNoUpfrontReservedPrice",
    "CurrentStorage",
    "CurrentVCpus",
    "Finding",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsConfigurationDesiredCapacity",
    "RecommendationOptionsConfigurationInstanceType",
    "RecommendationOptionsConfigurationMaxSize",
    "RecommendationOptionsConfigurationMinSize",
    "RecommendationOptionsMemory",
    "RecommendationOptionsNetwork",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
    "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
    "RecommendationOptionsStorage",
    "RecommendationOptionsVcpus",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsEbsReadBytesPerSecondMaximum",
    "UtilizationMetricsEbsReadOpsPerSecondMaximum",
    "UtilizationMetricsEbsWriteBytesPerSecondMaximum",
    "UtilizationMetricsEbsWriteOpsPerSecondMaximum",
    "UtilizationMetricsMemoryMaximum",
]
ExportableInstanceField = Literal[
    "AccountId",
    "CurrentInstanceType",
    "CurrentMemory",
    "CurrentNetwork",
    "CurrentOnDemandPrice",
    "CurrentStandardOneYearNoUpfrontReservedPrice",
    "CurrentStandardThreeYearNoUpfrontReservedPrice",
    "CurrentStorage",
    "CurrentVCpus",
    "Finding",
    "InstanceArn",
    "InstanceName",
    "LastRefreshTimestamp",
    "LookbackPeriodInDays",
    "RecommendationOptionsInstanceType",
    "RecommendationOptionsMemory",
    "RecommendationOptionsNetwork",
    "RecommendationOptionsOnDemandPrice",
    "RecommendationOptionsPerformanceRisk",
    "RecommendationOptionsProjectedUtilizationMetricsCpuMaximum",
    "RecommendationOptionsProjectedUtilizationMetricsMemoryMaximum",
    "RecommendationOptionsStandardOneYearNoUpfrontReservedPrice",
    "RecommendationOptionsStandardThreeYearNoUpfrontReservedPrice",
    "RecommendationOptionsStorage",
    "RecommendationOptionsVcpus",
    "RecommendationsSourcesRecommendationSourceArn",
    "RecommendationsSourcesRecommendationSourceType",
    "UtilizationMetricsCpuMaximum",
    "UtilizationMetricsEbsReadBytesPerSecondMaximum",
    "UtilizationMetricsEbsReadOpsPerSecondMaximum",
    "UtilizationMetricsEbsWriteBytesPerSecondMaximum",
    "UtilizationMetricsEbsWriteOpsPerSecondMaximum",
    "UtilizationMetricsMemoryMaximum",
]
FileFormat = Literal["Csv"]
FilterName = Literal["Finding", "RecommendationSourceType"]
Finding = Literal["NotOptimized", "Optimized", "Overprovisioned", "Underprovisioned"]
FindingReasonCode = Literal["MemoryOverprovisioned", "MemoryUnderprovisioned"]
JobFilterName = Literal["JobStatus", "ResourceType"]
JobStatus = Literal["Complete", "Failed", "InProgress", "Queued"]
LambdaFunctionMemoryMetricName = Literal["Duration"]
LambdaFunctionMemoryMetricStatistic = Literal["Expected", "LowerBound", "UpperBound"]
LambdaFunctionMetricName = Literal["Duration", "Memory"]
LambdaFunctionMetricStatistic = Literal["Average", "Maximum"]
LambdaFunctionRecommendationFilterName = Literal["Finding", "FindingReasonCode"]
LambdaFunctionRecommendationFinding = Literal["NotOptimized", "Optimized", "Unavailable"]
LambdaFunctionRecommendationFindingReasonCode = Literal[
    "Inconclusive", "InsufficientData", "MemoryOverprovisioned", "MemoryUnderprovisioned"
]
MetricName = Literal[
    "Cpu",
    "EBS_READ_BYTES_PER_SECOND",
    "EBS_READ_OPS_PER_SECOND",
    "EBS_WRITE_BYTES_PER_SECOND",
    "EBS_WRITE_OPS_PER_SECOND",
    "Memory",
]
MetricStatistic = Literal["Average", "Maximum"]
RecommendationSourceType = Literal["AutoScalingGroup", "EbsVolume", "Ec2Instance", "LambdaFunction"]
ResourceType = Literal["AutoScalingGroup", "Ec2Instance"]
Status = Literal["Active", "Failed", "Inactive", "Pending"]
