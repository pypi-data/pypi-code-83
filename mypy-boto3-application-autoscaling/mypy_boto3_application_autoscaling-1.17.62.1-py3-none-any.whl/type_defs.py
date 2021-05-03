"""
Type annotations for application-autoscaling service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/type_defs.html)

Usage::

    ```python
    from mypy_boto3_application_autoscaling.type_defs import AlarmTypeDef

    data: AlarmTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_application_autoscaling.literals import (
    AdjustmentType,
    MetricAggregationType,
    MetricStatistic,
    MetricType,
    PolicyType,
    ScalableDimension,
    ScalingActivityStatusCode,
    ServiceNamespace,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AlarmTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "DescribeScalableTargetsResponseTypeDef",
    "DescribeScalingActivitiesResponseTypeDef",
    "DescribeScalingPoliciesResponseTypeDef",
    "DescribeScheduledActionsResponseTypeDef",
    "MetricDimensionTypeDef",
    "PaginatorConfigTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "PutScalingPolicyResponseTypeDef",
    "ScalableTargetActionTypeDef",
    "ScalableTargetTypeDef",
    "ScalingActivityTypeDef",
    "ScalingPolicyTypeDef",
    "ScheduledActionTypeDef",
    "StepAdjustmentTypeDef",
    "StepScalingPolicyConfigurationTypeDef",
    "SuspendedStateTypeDef",
    "TargetTrackingScalingPolicyConfigurationTypeDef",
)


class AlarmTypeDef(TypedDict):
    AlarmName: str
    AlarmARN: str


class _RequiredCustomizedMetricSpecificationTypeDef(TypedDict):
    MetricName: str
    Namespace: str
    Statistic: MetricStatistic


class CustomizedMetricSpecificationTypeDef(
    _RequiredCustomizedMetricSpecificationTypeDef, total=False
):
    Dimensions: List["MetricDimensionTypeDef"]
    Unit: str


class DescribeScalableTargetsResponseTypeDef(TypedDict, total=False):
    ScalableTargets: List["ScalableTargetTypeDef"]
    NextToken: str


class DescribeScalingActivitiesResponseTypeDef(TypedDict, total=False):
    ScalingActivities: List["ScalingActivityTypeDef"]
    NextToken: str


class DescribeScalingPoliciesResponseTypeDef(TypedDict, total=False):
    ScalingPolicies: List["ScalingPolicyTypeDef"]
    NextToken: str


class DescribeScheduledActionsResponseTypeDef(TypedDict, total=False):
    ScheduledActions: List["ScheduledActionTypeDef"]
    NextToken: str


class MetricDimensionTypeDef(TypedDict):
    Name: str
    Value: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredPredefinedMetricSpecificationTypeDef(TypedDict):
    PredefinedMetricType: MetricType


class PredefinedMetricSpecificationTypeDef(
    _RequiredPredefinedMetricSpecificationTypeDef, total=False
):
    ResourceLabel: str


class _RequiredPutScalingPolicyResponseTypeDef(TypedDict):
    PolicyARN: str


class PutScalingPolicyResponseTypeDef(_RequiredPutScalingPolicyResponseTypeDef, total=False):
    Alarms: List["AlarmTypeDef"]


class ScalableTargetActionTypeDef(TypedDict, total=False):
    MinCapacity: int
    MaxCapacity: int


class _RequiredScalableTargetTypeDef(TypedDict):
    ServiceNamespace: ServiceNamespace
    ResourceId: str
    ScalableDimension: ScalableDimension
    MinCapacity: int
    MaxCapacity: int
    RoleARN: str
    CreationTime: datetime


class ScalableTargetTypeDef(_RequiredScalableTargetTypeDef, total=False):
    SuspendedState: "SuspendedStateTypeDef"


class _RequiredScalingActivityTypeDef(TypedDict):
    ActivityId: str
    ServiceNamespace: ServiceNamespace
    ResourceId: str
    ScalableDimension: ScalableDimension
    Description: str
    Cause: str
    StartTime: datetime
    StatusCode: ScalingActivityStatusCode


class ScalingActivityTypeDef(_RequiredScalingActivityTypeDef, total=False):
    EndTime: datetime
    StatusMessage: str
    Details: str


class _RequiredScalingPolicyTypeDef(TypedDict):
    PolicyARN: str
    PolicyName: str
    ServiceNamespace: ServiceNamespace
    ResourceId: str
    ScalableDimension: ScalableDimension
    PolicyType: PolicyType
    CreationTime: datetime


class ScalingPolicyTypeDef(_RequiredScalingPolicyTypeDef, total=False):
    StepScalingPolicyConfiguration: "StepScalingPolicyConfigurationTypeDef"
    TargetTrackingScalingPolicyConfiguration: "TargetTrackingScalingPolicyConfigurationTypeDef"
    Alarms: List["AlarmTypeDef"]


class _RequiredScheduledActionTypeDef(TypedDict):
    ScheduledActionName: str
    ScheduledActionARN: str
    ServiceNamespace: ServiceNamespace
    Schedule: str
    ResourceId: str
    CreationTime: datetime


class ScheduledActionTypeDef(_RequiredScheduledActionTypeDef, total=False):
    Timezone: str
    ScalableDimension: ScalableDimension
    StartTime: datetime
    EndTime: datetime
    ScalableTargetAction: "ScalableTargetActionTypeDef"


class _RequiredStepAdjustmentTypeDef(TypedDict):
    ScalingAdjustment: int


class StepAdjustmentTypeDef(_RequiredStepAdjustmentTypeDef, total=False):
    MetricIntervalLowerBound: float
    MetricIntervalUpperBound: float


class StepScalingPolicyConfigurationTypeDef(TypedDict, total=False):
    AdjustmentType: AdjustmentType
    StepAdjustments: List["StepAdjustmentTypeDef"]
    MinAdjustmentMagnitude: int
    Cooldown: int
    MetricAggregationType: MetricAggregationType


class SuspendedStateTypeDef(TypedDict, total=False):
    DynamicScalingInSuspended: bool
    DynamicScalingOutSuspended: bool
    ScheduledScalingSuspended: bool


class _RequiredTargetTrackingScalingPolicyConfigurationTypeDef(TypedDict):
    TargetValue: float


class TargetTrackingScalingPolicyConfigurationTypeDef(
    _RequiredTargetTrackingScalingPolicyConfigurationTypeDef, total=False
):
    PredefinedMetricSpecification: "PredefinedMetricSpecificationTypeDef"
    CustomizedMetricSpecification: "CustomizedMetricSpecificationTypeDef"
    ScaleOutCooldown: int
    ScaleInCooldown: int
    DisableScaleIn: bool
