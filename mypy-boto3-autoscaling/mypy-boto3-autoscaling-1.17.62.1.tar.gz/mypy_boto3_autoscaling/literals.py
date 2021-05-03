"""
Type annotations for autoscaling service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/literals.html)

Usage::

    ```python
    from mypy_boto3_autoscaling.literals import DescribeAutoScalingGroupsPaginatorName

    data: DescribeAutoScalingGroupsPaginatorName = "describe_auto_scaling_groups"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeAutoScalingGroupsPaginatorName",
    "DescribeAutoScalingInstancesPaginatorName",
    "DescribeLaunchConfigurationsPaginatorName",
    "DescribeLoadBalancerTargetGroupsPaginatorName",
    "DescribeLoadBalancersPaginatorName",
    "DescribeNotificationConfigurationsPaginatorName",
    "DescribePoliciesPaginatorName",
    "DescribeScalingActivitiesPaginatorName",
    "DescribeScheduledActionsPaginatorName",
    "DescribeTagsPaginatorName",
    "InstanceMetadataEndpointState",
    "InstanceMetadataHttpTokensState",
    "InstanceRefreshStatus",
    "LifecycleState",
    "MetricStatistic",
    "MetricType",
    "RefreshStrategy",
    "ScalingActivityStatusCode",
    "WarmPoolState",
    "WarmPoolStatus",
)


DescribeAutoScalingGroupsPaginatorName = Literal["describe_auto_scaling_groups"]
DescribeAutoScalingInstancesPaginatorName = Literal["describe_auto_scaling_instances"]
DescribeLaunchConfigurationsPaginatorName = Literal["describe_launch_configurations"]
DescribeLoadBalancerTargetGroupsPaginatorName = Literal["describe_load_balancer_target_groups"]
DescribeLoadBalancersPaginatorName = Literal["describe_load_balancers"]
DescribeNotificationConfigurationsPaginatorName = Literal["describe_notification_configurations"]
DescribePoliciesPaginatorName = Literal["describe_policies"]
DescribeScalingActivitiesPaginatorName = Literal["describe_scaling_activities"]
DescribeScheduledActionsPaginatorName = Literal["describe_scheduled_actions"]
DescribeTagsPaginatorName = Literal["describe_tags"]
InstanceMetadataEndpointState = Literal["disabled", "enabled"]
InstanceMetadataHttpTokensState = Literal["optional", "required"]
InstanceRefreshStatus = Literal[
    "Cancelled", "Cancelling", "Failed", "InProgress", "Pending", "Successful"
]
LifecycleState = Literal[
    "Detached",
    "Detaching",
    "EnteringStandby",
    "InService",
    "Pending",
    "Pending:Proceed",
    "Pending:Wait",
    "Quarantined",
    "Standby",
    "Terminated",
    "Terminating",
    "Terminating:Proceed",
    "Terminating:Wait",
    "Warmed:Pending",
    "Warmed:Pending:Proceed",
    "Warmed:Pending:Wait",
    "Warmed:Running",
    "Warmed:Stopped",
    "Warmed:Terminated",
    "Warmed:Terminating",
    "Warmed:Terminating:Proceed",
    "Warmed:Terminating:Wait",
]
MetricStatistic = Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
MetricType = Literal[
    "ALBRequestCountPerTarget",
    "ASGAverageCPUUtilization",
    "ASGAverageNetworkIn",
    "ASGAverageNetworkOut",
]
RefreshStrategy = Literal["Rolling"]
ScalingActivityStatusCode = Literal[
    "Cancelled",
    "Failed",
    "InProgress",
    "MidLifecycleAction",
    "PendingSpotBidPlacement",
    "PreInService",
    "Successful",
    "WaitingForELBConnectionDraining",
    "WaitingForInstanceId",
    "WaitingForInstanceWarmup",
    "WaitingForSpotInstanceId",
    "WaitingForSpotInstanceRequestId",
]
WarmPoolState = Literal["Running", "Stopped"]
WarmPoolStatus = Literal["PendingDelete"]
