"""
Type annotations for autoscaling-plans service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling_plans/literals.html)

Usage::

    ```python
    from mypy_boto3_autoscaling_plans.literals import DescribeScalingPlanResourcesPaginatorName

    data: DescribeScalingPlanResourcesPaginatorName = "describe_scaling_plan_resources"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeScalingPlanResourcesPaginatorName",
    "DescribeScalingPlansPaginatorName",
    "ForecastDataType",
    "LoadMetricType",
    "MetricStatistic",
    "PolicyType",
    "PredictiveScalingMaxCapacityBehavior",
    "PredictiveScalingMode",
    "ScalableDimension",
    "ScalingMetricType",
    "ScalingPlanStatusCode",
    "ScalingPolicyUpdateBehavior",
    "ScalingStatusCode",
    "ServiceNamespace",
)


DescribeScalingPlanResourcesPaginatorName = Literal["describe_scaling_plan_resources"]
DescribeScalingPlansPaginatorName = Literal["describe_scaling_plans"]
ForecastDataType = Literal[
    "CapacityForecast", "LoadForecast", "ScheduledActionMaxCapacity", "ScheduledActionMinCapacity"
]
LoadMetricType = Literal[
    "ALBTargetGroupRequestCount",
    "ASGTotalCPUUtilization",
    "ASGTotalNetworkIn",
    "ASGTotalNetworkOut",
]
MetricStatistic = Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
PolicyType = Literal["TargetTrackingScaling"]
PredictiveScalingMaxCapacityBehavior = Literal[
    "SetForecastCapacityToMaxCapacity",
    "SetMaxCapacityAboveForecastCapacity",
    "SetMaxCapacityToForecastCapacity",
]
PredictiveScalingMode = Literal["ForecastAndScale", "ForecastOnly"]
ScalableDimension = Literal[
    "autoscaling:autoScalingGroup:DesiredCapacity",
    "dynamodb:index:ReadCapacityUnits",
    "dynamodb:index:WriteCapacityUnits",
    "dynamodb:table:ReadCapacityUnits",
    "dynamodb:table:WriteCapacityUnits",
    "ec2:spot-fleet-request:TargetCapacity",
    "ecs:service:DesiredCount",
    "rds:cluster:ReadReplicaCount",
]
ScalingMetricType = Literal[
    "ALBRequestCountPerTarget",
    "ASGAverageCPUUtilization",
    "ASGAverageNetworkIn",
    "ASGAverageNetworkOut",
    "DynamoDBReadCapacityUtilization",
    "DynamoDBWriteCapacityUtilization",
    "EC2SpotFleetRequestAverageCPUUtilization",
    "EC2SpotFleetRequestAverageNetworkIn",
    "EC2SpotFleetRequestAverageNetworkOut",
    "ECSServiceAverageCPUUtilization",
    "ECSServiceAverageMemoryUtilization",
    "RDSReaderAverageCPUUtilization",
    "RDSReaderAverageDatabaseConnections",
]
ScalingPlanStatusCode = Literal[
    "Active",
    "ActiveWithProblems",
    "CreationFailed",
    "CreationInProgress",
    "DeletionFailed",
    "DeletionInProgress",
    "UpdateFailed",
    "UpdateInProgress",
]
ScalingPolicyUpdateBehavior = Literal["KeepExternalPolicies", "ReplaceExternalPolicies"]
ScalingStatusCode = Literal["Active", "Inactive", "PartiallyActive"]
ServiceNamespace = Literal["autoscaling", "dynamodb", "ec2", "ecs", "rds"]
