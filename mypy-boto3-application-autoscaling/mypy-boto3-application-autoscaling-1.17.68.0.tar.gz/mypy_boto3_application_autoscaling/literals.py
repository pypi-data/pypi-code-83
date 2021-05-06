"""
Type annotations for application-autoscaling service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_autoscaling/literals.html)

Usage::

    ```python
    from mypy_boto3_application_autoscaling.literals import AdjustmentType

    data: AdjustmentType = "ChangeInCapacity"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AdjustmentType",
    "DescribeScalableTargetsPaginatorName",
    "DescribeScalingActivitiesPaginatorName",
    "DescribeScalingPoliciesPaginatorName",
    "DescribeScheduledActionsPaginatorName",
    "MetricAggregationType",
    "MetricStatistic",
    "MetricType",
    "PolicyType",
    "ScalableDimension",
    "ScalingActivityStatusCode",
    "ServiceNamespace",
)


AdjustmentType = Literal["ChangeInCapacity", "ExactCapacity", "PercentChangeInCapacity"]
DescribeScalableTargetsPaginatorName = Literal["describe_scalable_targets"]
DescribeScalingActivitiesPaginatorName = Literal["describe_scaling_activities"]
DescribeScalingPoliciesPaginatorName = Literal["describe_scaling_policies"]
DescribeScheduledActionsPaginatorName = Literal["describe_scheduled_actions"]
MetricAggregationType = Literal["Average", "Maximum", "Minimum"]
MetricStatistic = Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
MetricType = Literal[
    "ALBRequestCountPerTarget",
    "AppStreamAverageCapacityUtilization",
    "CassandraReadCapacityUtilization",
    "CassandraWriteCapacityUtilization",
    "ComprehendInferenceUtilization",
    "DynamoDBReadCapacityUtilization",
    "DynamoDBWriteCapacityUtilization",
    "EC2SpotFleetRequestAverageCPUUtilization",
    "EC2SpotFleetRequestAverageNetworkIn",
    "EC2SpotFleetRequestAverageNetworkOut",
    "ECSServiceAverageCPUUtilization",
    "ECSServiceAverageMemoryUtilization",
    "KafkaBrokerStorageUtilization",
    "LambdaProvisionedConcurrencyUtilization",
    "RDSReaderAverageCPUUtilization",
    "RDSReaderAverageDatabaseConnections",
    "SageMakerVariantInvocationsPerInstance",
]
PolicyType = Literal["StepScaling", "TargetTrackingScaling"]
ScalableDimension = Literal[
    "appstream:fleet:DesiredCapacity",
    "cassandra:table:ReadCapacityUnits",
    "cassandra:table:WriteCapacityUnits",
    "comprehend:document-classifier-endpoint:DesiredInferenceUnits",
    "comprehend:entity-recognizer-endpoint:DesiredInferenceUnits",
    "custom-resource:ResourceType:Property",
    "dynamodb:index:ReadCapacityUnits",
    "dynamodb:index:WriteCapacityUnits",
    "dynamodb:table:ReadCapacityUnits",
    "dynamodb:table:WriteCapacityUnits",
    "ec2:spot-fleet-request:TargetCapacity",
    "ecs:service:DesiredCount",
    "elasticmapreduce:instancegroup:InstanceCount",
    "kafka:broker-storage:VolumeSize",
    "lambda:function:ProvisionedConcurrency",
    "rds:cluster:ReadReplicaCount",
    "sagemaker:variant:DesiredInstanceCount",
]
ScalingActivityStatusCode = Literal[
    "Failed", "InProgress", "Overridden", "Pending", "Successful", "Unfulfilled"
]
ServiceNamespace = Literal[
    "appstream",
    "cassandra",
    "comprehend",
    "custom-resource",
    "dynamodb",
    "ec2",
    "ecs",
    "elasticmapreduce",
    "kafka",
    "lambda",
    "rds",
    "sagemaker",
]
