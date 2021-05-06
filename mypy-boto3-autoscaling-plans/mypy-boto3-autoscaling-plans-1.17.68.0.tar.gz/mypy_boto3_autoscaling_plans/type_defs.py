"""
Type annotations for autoscaling-plans service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/type_defs.html)

Usage::

    ```python
    from mypy_boto3_autoscaling_plans.type_defs import ApplicationSourceTypeDef

    data: ApplicationSourceTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_autoscaling_plans.literals import (
    LoadMetricType,
    MetricStatistic,
    PredictiveScalingMaxCapacityBehavior,
    PredictiveScalingMode,
    ScalableDimension,
    ScalingMetricType,
    ScalingPlanStatusCode,
    ScalingPolicyUpdateBehavior,
    ScalingStatusCode,
    ServiceNamespace,
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
    "ApplicationSourceTypeDef",
    "CreateScalingPlanResponseTypeDef",
    "CustomizedLoadMetricSpecificationTypeDef",
    "CustomizedScalingMetricSpecificationTypeDef",
    "DatapointTypeDef",
    "DescribeScalingPlanResourcesResponseTypeDef",
    "DescribeScalingPlansResponseTypeDef",
    "GetScalingPlanResourceForecastDataResponseTypeDef",
    "MetricDimensionTypeDef",
    "PaginatorConfigTypeDef",
    "PredefinedLoadMetricSpecificationTypeDef",
    "PredefinedScalingMetricSpecificationTypeDef",
    "ScalingInstructionTypeDef",
    "ScalingPlanResourceTypeDef",
    "ScalingPlanTypeDef",
    "ScalingPolicyTypeDef",
    "TagFilterTypeDef",
    "TargetTrackingConfigurationTypeDef",
)


class ApplicationSourceTypeDef(TypedDict, total=False):
    CloudFormationStackARN: str
    TagFilters: List["TagFilterTypeDef"]


class CreateScalingPlanResponseTypeDef(TypedDict):
    ScalingPlanVersion: int


class _RequiredCustomizedLoadMetricSpecificationTypeDef(TypedDict):
    MetricName: str
    Namespace: str
    Statistic: MetricStatistic


class CustomizedLoadMetricSpecificationTypeDef(
    _RequiredCustomizedLoadMetricSpecificationTypeDef, total=False
):
    Dimensions: List["MetricDimensionTypeDef"]
    Unit: str


class _RequiredCustomizedScalingMetricSpecificationTypeDef(TypedDict):
    MetricName: str
    Namespace: str
    Statistic: MetricStatistic


class CustomizedScalingMetricSpecificationTypeDef(
    _RequiredCustomizedScalingMetricSpecificationTypeDef, total=False
):
    Dimensions: List["MetricDimensionTypeDef"]
    Unit: str


class DatapointTypeDef(TypedDict, total=False):
    Timestamp: datetime
    Value: float


class DescribeScalingPlanResourcesResponseTypeDef(TypedDict, total=False):
    ScalingPlanResources: List["ScalingPlanResourceTypeDef"]
    NextToken: str


class DescribeScalingPlansResponseTypeDef(TypedDict, total=False):
    ScalingPlans: List["ScalingPlanTypeDef"]
    NextToken: str


class GetScalingPlanResourceForecastDataResponseTypeDef(TypedDict):
    Datapoints: List["DatapointTypeDef"]


class MetricDimensionTypeDef(TypedDict):
    Name: str
    Value: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredPredefinedLoadMetricSpecificationTypeDef(TypedDict):
    PredefinedLoadMetricType: LoadMetricType


class PredefinedLoadMetricSpecificationTypeDef(
    _RequiredPredefinedLoadMetricSpecificationTypeDef, total=False
):
    ResourceLabel: str


class _RequiredPredefinedScalingMetricSpecificationTypeDef(TypedDict):
    PredefinedScalingMetricType: ScalingMetricType


class PredefinedScalingMetricSpecificationTypeDef(
    _RequiredPredefinedScalingMetricSpecificationTypeDef, total=False
):
    ResourceLabel: str


class _RequiredScalingInstructionTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespace
    ResourceId: str
    ScalableDimension: ScalableDimension
    MinCapacity: int
    MaxCapacity: int
    TargetTrackingConfigurations: List["TargetTrackingConfigurationTypeDef"]


class ScalingInstructionTypeDef(_RequiredScalingInstructionTypeDef, total=False):
    PredefinedLoadMetricSpecification: "PredefinedLoadMetricSpecificationTypeDef"
    CustomizedLoadMetricSpecification: "CustomizedLoadMetricSpecificationTypeDef"
    ScheduledActionBufferTime: int
    PredictiveScalingMaxCapacityBehavior: PredictiveScalingMaxCapacityBehavior
    PredictiveScalingMaxCapacityBuffer: int
    PredictiveScalingMode: PredictiveScalingMode
    ScalingPolicyUpdateBehavior: ScalingPolicyUpdateBehavior
    DisableDynamicScaling: bool


class _RequiredScalingPlanResourceTypeDef(TypedDict):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ServiceNamespace: ServiceNamespace
    ResourceId: str
    ScalableDimension: ScalableDimension
    ScalingStatusCode: ScalingStatusCode


class ScalingPlanResourceTypeDef(_RequiredScalingPlanResourceTypeDef, total=False):
    ScalingPolicies: List["ScalingPolicyTypeDef"]
    ScalingStatusMessage: str


class _RequiredScalingPlanTypeDef(TypedDict):
    ScalingPlanName: str
    ScalingPlanVersion: int
    ApplicationSource: "ApplicationSourceTypeDef"
    ScalingInstructions: List["ScalingInstructionTypeDef"]
    StatusCode: ScalingPlanStatusCode


class ScalingPlanTypeDef(_RequiredScalingPlanTypeDef, total=False):
    StatusMessage: str
    StatusStartTime: datetime
    CreationTime: datetime


class _RequiredScalingPolicyTypeDef(TypedDict):
    PolicyName: str
    PolicyType: Literal["TargetTrackingScaling"]


class ScalingPolicyTypeDef(_RequiredScalingPolicyTypeDef, total=False):
    TargetTrackingConfiguration: "TargetTrackingConfigurationTypeDef"


class TagFilterTypeDef(TypedDict, total=False):
    Key: str
    Values: List[str]


class _RequiredTargetTrackingConfigurationTypeDef(TypedDict):
    TargetValue: float


class TargetTrackingConfigurationTypeDef(_RequiredTargetTrackingConfigurationTypeDef, total=False):
    PredefinedScalingMetricSpecification: "PredefinedScalingMetricSpecificationTypeDef"
    CustomizedScalingMetricSpecification: "CustomizedScalingMetricSpecificationTypeDef"
    DisableScaleIn: bool
    ScaleOutCooldown: int
    ScaleInCooldown: int
    EstimatedInstanceWarmup: int
