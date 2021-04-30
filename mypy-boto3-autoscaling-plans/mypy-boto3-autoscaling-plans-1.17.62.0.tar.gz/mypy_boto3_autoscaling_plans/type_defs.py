"""
Main interface for autoscaling-plans service type definitions.

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
    PolicyType,
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
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationSourceTypeDef",
    "CustomizedLoadMetricSpecificationTypeDef",
    "CustomizedScalingMetricSpecificationTypeDef",
    "DatapointTypeDef",
    "MetricDimensionTypeDef",
    "PredefinedLoadMetricSpecificationTypeDef",
    "PredefinedScalingMetricSpecificationTypeDef",
    "ScalingInstructionTypeDef",
    "ScalingPlanResourceTypeDef",
    "ScalingPlanTypeDef",
    "ScalingPolicyTypeDef",
    "TagFilterTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "CreateScalingPlanResponseTypeDef",
    "DescribeScalingPlanResourcesResponseTypeDef",
    "DescribeScalingPlansResponseTypeDef",
    "GetScalingPlanResourceForecastDataResponseTypeDef",
    "PaginatorConfigTypeDef",
)

ApplicationSourceTypeDef = TypedDict(
    "ApplicationSourceTypeDef",
    {"CloudFormationStackARN": str, "TagFilters": List["TagFilterTypeDef"]},
    total=False,
)

_RequiredCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_RequiredCustomizedLoadMetricSpecificationTypeDef",
    {"MetricName": str, "Namespace": str, "Statistic": MetricStatistic},
)
_OptionalCustomizedLoadMetricSpecificationTypeDef = TypedDict(
    "_OptionalCustomizedLoadMetricSpecificationTypeDef",
    {"Dimensions": List["MetricDimensionTypeDef"], "Unit": str},
    total=False,
)


class CustomizedLoadMetricSpecificationTypeDef(
    _RequiredCustomizedLoadMetricSpecificationTypeDef,
    _OptionalCustomizedLoadMetricSpecificationTypeDef,
):
    pass


_RequiredCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_RequiredCustomizedScalingMetricSpecificationTypeDef",
    {"MetricName": str, "Namespace": str, "Statistic": MetricStatistic},
)
_OptionalCustomizedScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalCustomizedScalingMetricSpecificationTypeDef",
    {"Dimensions": List["MetricDimensionTypeDef"], "Unit": str},
    total=False,
)


class CustomizedScalingMetricSpecificationTypeDef(
    _RequiredCustomizedScalingMetricSpecificationTypeDef,
    _OptionalCustomizedScalingMetricSpecificationTypeDef,
):
    pass


DatapointTypeDef = TypedDict(
    "DatapointTypeDef", {"Timestamp": datetime, "Value": float}, total=False
)

MetricDimensionTypeDef = TypedDict("MetricDimensionTypeDef", {"Name": str, "Value": str})

_RequiredPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredefinedLoadMetricSpecificationTypeDef",
    {"PredefinedLoadMetricType": LoadMetricType},
)
_OptionalPredefinedLoadMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredefinedLoadMetricSpecificationTypeDef", {"ResourceLabel": str}, total=False
)


class PredefinedLoadMetricSpecificationTypeDef(
    _RequiredPredefinedLoadMetricSpecificationTypeDef,
    _OptionalPredefinedLoadMetricSpecificationTypeDef,
):
    pass


_RequiredPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_RequiredPredefinedScalingMetricSpecificationTypeDef",
    {"PredefinedScalingMetricType": ScalingMetricType},
)
_OptionalPredefinedScalingMetricSpecificationTypeDef = TypedDict(
    "_OptionalPredefinedScalingMetricSpecificationTypeDef", {"ResourceLabel": str}, total=False
)


class PredefinedScalingMetricSpecificationTypeDef(
    _RequiredPredefinedScalingMetricSpecificationTypeDef,
    _OptionalPredefinedScalingMetricSpecificationTypeDef,
):
    pass


_RequiredScalingInstructionTypeDef = TypedDict(
    "_RequiredScalingInstructionTypeDef",
    {
        "ServiceNamespace": ServiceNamespace,
        "ResourceId": str,
        "ScalableDimension": ScalableDimension,
        "MinCapacity": int,
        "MaxCapacity": int,
        "TargetTrackingConfigurations": List["TargetTrackingConfigurationTypeDef"],
    },
)
_OptionalScalingInstructionTypeDef = TypedDict(
    "_OptionalScalingInstructionTypeDef",
    {
        "PredefinedLoadMetricSpecification": "PredefinedLoadMetricSpecificationTypeDef",
        "CustomizedLoadMetricSpecification": "CustomizedLoadMetricSpecificationTypeDef",
        "ScheduledActionBufferTime": int,
        "PredictiveScalingMaxCapacityBehavior": PredictiveScalingMaxCapacityBehavior,
        "PredictiveScalingMaxCapacityBuffer": int,
        "PredictiveScalingMode": PredictiveScalingMode,
        "ScalingPolicyUpdateBehavior": ScalingPolicyUpdateBehavior,
        "DisableDynamicScaling": bool,
    },
    total=False,
)


class ScalingInstructionTypeDef(
    _RequiredScalingInstructionTypeDef, _OptionalScalingInstructionTypeDef
):
    pass


_RequiredScalingPlanResourceTypeDef = TypedDict(
    "_RequiredScalingPlanResourceTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ServiceNamespace": ServiceNamespace,
        "ResourceId": str,
        "ScalableDimension": ScalableDimension,
        "ScalingStatusCode": ScalingStatusCode,
    },
)
_OptionalScalingPlanResourceTypeDef = TypedDict(
    "_OptionalScalingPlanResourceTypeDef",
    {"ScalingPolicies": List["ScalingPolicyTypeDef"], "ScalingStatusMessage": str},
    total=False,
)


class ScalingPlanResourceTypeDef(
    _RequiredScalingPlanResourceTypeDef, _OptionalScalingPlanResourceTypeDef
):
    pass


_RequiredScalingPlanTypeDef = TypedDict(
    "_RequiredScalingPlanTypeDef",
    {
        "ScalingPlanName": str,
        "ScalingPlanVersion": int,
        "ApplicationSource": "ApplicationSourceTypeDef",
        "ScalingInstructions": List["ScalingInstructionTypeDef"],
        "StatusCode": ScalingPlanStatusCode,
    },
)
_OptionalScalingPlanTypeDef = TypedDict(
    "_OptionalScalingPlanTypeDef",
    {"StatusMessage": str, "StatusStartTime": datetime, "CreationTime": datetime},
    total=False,
)


class ScalingPlanTypeDef(_RequiredScalingPlanTypeDef, _OptionalScalingPlanTypeDef):
    pass


_RequiredScalingPolicyTypeDef = TypedDict(
    "_RequiredScalingPolicyTypeDef", {"PolicyName": str, "PolicyType": PolicyType}
)
_OptionalScalingPolicyTypeDef = TypedDict(
    "_OptionalScalingPolicyTypeDef",
    {"TargetTrackingConfiguration": "TargetTrackingConfigurationTypeDef"},
    total=False,
)


class ScalingPolicyTypeDef(_RequiredScalingPolicyTypeDef, _OptionalScalingPolicyTypeDef):
    pass


TagFilterTypeDef = TypedDict("TagFilterTypeDef", {"Key": str, "Values": List[str]}, total=False)

_RequiredTargetTrackingConfigurationTypeDef = TypedDict(
    "_RequiredTargetTrackingConfigurationTypeDef", {"TargetValue": float}
)
_OptionalTargetTrackingConfigurationTypeDef = TypedDict(
    "_OptionalTargetTrackingConfigurationTypeDef",
    {
        "PredefinedScalingMetricSpecification": "PredefinedScalingMetricSpecificationTypeDef",
        "CustomizedScalingMetricSpecification": "CustomizedScalingMetricSpecificationTypeDef",
        "DisableScaleIn": bool,
        "ScaleOutCooldown": int,
        "ScaleInCooldown": int,
        "EstimatedInstanceWarmup": int,
    },
    total=False,
)


class TargetTrackingConfigurationTypeDef(
    _RequiredTargetTrackingConfigurationTypeDef, _OptionalTargetTrackingConfigurationTypeDef
):
    pass


CreateScalingPlanResponseTypeDef = TypedDict(
    "CreateScalingPlanResponseTypeDef", {"ScalingPlanVersion": int}
)

DescribeScalingPlanResourcesResponseTypeDef = TypedDict(
    "DescribeScalingPlanResourcesResponseTypeDef",
    {"ScalingPlanResources": List["ScalingPlanResourceTypeDef"], "NextToken": str},
    total=False,
)

DescribeScalingPlansResponseTypeDef = TypedDict(
    "DescribeScalingPlansResponseTypeDef",
    {"ScalingPlans": List["ScalingPlanTypeDef"], "NextToken": str},
    total=False,
)

GetScalingPlanResourceForecastDataResponseTypeDef = TypedDict(
    "GetScalingPlanResourceForecastDataResponseTypeDef", {"Datapoints": List["DatapointTypeDef"]}
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)
