"""
Type annotations for autoscaling service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_autoscaling/type_defs.html)

Usage::

    ```python
    from mypy_boto3_autoscaling.type_defs import ActivitiesTypeTypeDef

    data: ActivitiesTypeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_autoscaling.literals import (
    InstanceMetadataEndpointState,
    InstanceMetadataHttpTokensState,
    InstanceRefreshStatus,
    LifecycleState,
    MetricStatistic,
    MetricType,
    ScalingActivityStatusCode,
    WarmPoolState,
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
    "ActivitiesTypeTypeDef",
    "ActivityTypeDef",
    "ActivityTypeTypeDef",
    "AdjustmentTypeTypeDef",
    "AlarmTypeDef",
    "AutoScalingGroupTypeDef",
    "AutoScalingGroupsTypeTypeDef",
    "AutoScalingInstanceDetailsTypeDef",
    "AutoScalingInstancesTypeTypeDef",
    "BatchDeleteScheduledActionAnswerTypeDef",
    "BatchPutScheduledUpdateGroupActionAnswerTypeDef",
    "BlockDeviceMappingTypeDef",
    "CancelInstanceRefreshAnswerTypeDef",
    "CustomizedMetricSpecificationTypeDef",
    "DescribeAccountLimitsAnswerTypeDef",
    "DescribeAdjustmentTypesAnswerTypeDef",
    "DescribeAutoScalingNotificationTypesAnswerTypeDef",
    "DescribeInstanceRefreshesAnswerTypeDef",
    "DescribeLifecycleHookTypesAnswerTypeDef",
    "DescribeLifecycleHooksAnswerTypeDef",
    "DescribeLoadBalancerTargetGroupsResponseTypeDef",
    "DescribeLoadBalancersResponseTypeDef",
    "DescribeMetricCollectionTypesAnswerTypeDef",
    "DescribeNotificationConfigurationsAnswerTypeDef",
    "DescribeTerminationPolicyTypesAnswerTypeDef",
    "DescribeWarmPoolAnswerTypeDef",
    "DetachInstancesAnswerTypeDef",
    "EbsTypeDef",
    "EnabledMetricTypeDef",
    "EnterStandbyAnswerTypeDef",
    "ExitStandbyAnswerTypeDef",
    "FailedScheduledUpdateGroupActionRequestTypeDef",
    "FilterTypeDef",
    "InstanceMetadataOptionsTypeDef",
    "InstanceMonitoringTypeDef",
    "InstanceRefreshLivePoolProgressTypeDef",
    "InstanceRefreshProgressDetailsTypeDef",
    "InstanceRefreshTypeDef",
    "InstanceRefreshWarmPoolProgressTypeDef",
    "InstanceTypeDef",
    "InstancesDistributionTypeDef",
    "LaunchConfigurationTypeDef",
    "LaunchConfigurationsTypeTypeDef",
    "LaunchTemplateOverridesTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LaunchTemplateTypeDef",
    "LifecycleHookSpecificationTypeDef",
    "LifecycleHookTypeDef",
    "LoadBalancerStateTypeDef",
    "LoadBalancerTargetGroupStateTypeDef",
    "MetricCollectionTypeTypeDef",
    "MetricDimensionTypeDef",
    "MetricGranularityTypeTypeDef",
    "MixedInstancesPolicyTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PoliciesTypeTypeDef",
    "PolicyARNTypeTypeDef",
    "PredefinedMetricSpecificationTypeDef",
    "ProcessTypeTypeDef",
    "ProcessesTypeTypeDef",
    "RefreshPreferencesTypeDef",
    "ScalingPolicyTypeDef",
    "ScheduledActionsTypeTypeDef",
    "ScheduledUpdateGroupActionRequestTypeDef",
    "ScheduledUpdateGroupActionTypeDef",
    "StartInstanceRefreshAnswerTypeDef",
    "StepAdjustmentTypeDef",
    "SuspendedProcessTypeDef",
    "TagDescriptionTypeDef",
    "TagTypeDef",
    "TagsTypeTypeDef",
    "TargetTrackingConfigurationTypeDef",
    "WarmPoolConfigurationTypeDef",
)


class _RequiredActivitiesTypeTypeDef(TypedDict):
    Activities: List["ActivityTypeDef"]


class ActivitiesTypeTypeDef(_RequiredActivitiesTypeTypeDef, total=False):
    NextToken: str


class _RequiredActivityTypeDef(TypedDict):
    ActivityId: str
    AutoScalingGroupName: str
    Cause: str
    StartTime: datetime
    StatusCode: ScalingActivityStatusCode


class ActivityTypeDef(_RequiredActivityTypeDef, total=False):
    Description: str
    EndTime: datetime
    StatusMessage: str
    Progress: int
    Details: str
    AutoScalingGroupState: str
    AutoScalingGroupARN: str


class ActivityTypeTypeDef(TypedDict, total=False):
    Activity: "ActivityTypeDef"


class AdjustmentTypeTypeDef(TypedDict, total=False):
    AdjustmentType: str


class AlarmTypeDef(TypedDict, total=False):
    AlarmName: str
    AlarmARN: str


class _RequiredAutoScalingGroupTypeDef(TypedDict):
    AutoScalingGroupName: str
    MinSize: int
    MaxSize: int
    DesiredCapacity: int
    DefaultCooldown: int
    AvailabilityZones: List[str]
    HealthCheckType: str
    CreatedTime: datetime


class AutoScalingGroupTypeDef(_RequiredAutoScalingGroupTypeDef, total=False):
    AutoScalingGroupARN: str
    LaunchConfigurationName: str
    LaunchTemplate: "LaunchTemplateSpecificationTypeDef"
    MixedInstancesPolicy: "MixedInstancesPolicyTypeDef"
    LoadBalancerNames: List[str]
    TargetGroupARNs: List[str]
    HealthCheckGracePeriod: int
    Instances: List["InstanceTypeDef"]
    SuspendedProcesses: List["SuspendedProcessTypeDef"]
    PlacementGroup: str
    VPCZoneIdentifier: str
    EnabledMetrics: List["EnabledMetricTypeDef"]
    Status: str
    Tags: List["TagDescriptionTypeDef"]
    TerminationPolicies: List[str]
    NewInstancesProtectedFromScaleIn: bool
    ServiceLinkedRoleARN: str
    MaxInstanceLifetime: int
    CapacityRebalance: bool
    WarmPoolConfiguration: "WarmPoolConfigurationTypeDef"
    WarmPoolSize: int


class _RequiredAutoScalingGroupsTypeTypeDef(TypedDict):
    AutoScalingGroups: List["AutoScalingGroupTypeDef"]


class AutoScalingGroupsTypeTypeDef(_RequiredAutoScalingGroupsTypeTypeDef, total=False):
    NextToken: str


class _RequiredAutoScalingInstanceDetailsTypeDef(TypedDict):
    InstanceId: str
    AutoScalingGroupName: str
    AvailabilityZone: str
    LifecycleState: str
    HealthStatus: str
    ProtectedFromScaleIn: bool


class AutoScalingInstanceDetailsTypeDef(_RequiredAutoScalingInstanceDetailsTypeDef, total=False):
    InstanceType: str
    LaunchConfigurationName: str
    LaunchTemplate: "LaunchTemplateSpecificationTypeDef"
    WeightedCapacity: str


class AutoScalingInstancesTypeTypeDef(TypedDict, total=False):
    AutoScalingInstances: List["AutoScalingInstanceDetailsTypeDef"]
    NextToken: str


class BatchDeleteScheduledActionAnswerTypeDef(TypedDict, total=False):
    FailedScheduledActions: List["FailedScheduledUpdateGroupActionRequestTypeDef"]


class BatchPutScheduledUpdateGroupActionAnswerTypeDef(TypedDict, total=False):
    FailedScheduledUpdateGroupActions: List["FailedScheduledUpdateGroupActionRequestTypeDef"]


class _RequiredBlockDeviceMappingTypeDef(TypedDict):
    DeviceName: str


class BlockDeviceMappingTypeDef(_RequiredBlockDeviceMappingTypeDef, total=False):
    VirtualName: str
    Ebs: "EbsTypeDef"
    NoDevice: bool


class CancelInstanceRefreshAnswerTypeDef(TypedDict, total=False):
    InstanceRefreshId: str


class _RequiredCustomizedMetricSpecificationTypeDef(TypedDict):
    MetricName: str
    Namespace: str
    Statistic: MetricStatistic


class CustomizedMetricSpecificationTypeDef(
    _RequiredCustomizedMetricSpecificationTypeDef, total=False
):
    Dimensions: List["MetricDimensionTypeDef"]
    Unit: str


class DescribeAccountLimitsAnswerTypeDef(TypedDict, total=False):
    MaxNumberOfAutoScalingGroups: int
    MaxNumberOfLaunchConfigurations: int
    NumberOfAutoScalingGroups: int
    NumberOfLaunchConfigurations: int


class DescribeAdjustmentTypesAnswerTypeDef(TypedDict, total=False):
    AdjustmentTypes: List["AdjustmentTypeTypeDef"]


class DescribeAutoScalingNotificationTypesAnswerTypeDef(TypedDict, total=False):
    AutoScalingNotificationTypes: List[str]


class DescribeInstanceRefreshesAnswerTypeDef(TypedDict, total=False):
    InstanceRefreshes: List["InstanceRefreshTypeDef"]
    NextToken: str


class DescribeLifecycleHookTypesAnswerTypeDef(TypedDict, total=False):
    LifecycleHookTypes: List[str]


class DescribeLifecycleHooksAnswerTypeDef(TypedDict, total=False):
    LifecycleHooks: List["LifecycleHookTypeDef"]


class DescribeLoadBalancerTargetGroupsResponseTypeDef(TypedDict, total=False):
    LoadBalancerTargetGroups: List["LoadBalancerTargetGroupStateTypeDef"]
    NextToken: str


class DescribeLoadBalancersResponseTypeDef(TypedDict, total=False):
    LoadBalancers: List["LoadBalancerStateTypeDef"]
    NextToken: str


class DescribeMetricCollectionTypesAnswerTypeDef(TypedDict, total=False):
    Metrics: List["MetricCollectionTypeTypeDef"]
    Granularities: List["MetricGranularityTypeTypeDef"]


class _RequiredDescribeNotificationConfigurationsAnswerTypeDef(TypedDict):
    NotificationConfigurations: List["NotificationConfigurationTypeDef"]


class DescribeNotificationConfigurationsAnswerTypeDef(
    _RequiredDescribeNotificationConfigurationsAnswerTypeDef, total=False
):
    NextToken: str


class DescribeTerminationPolicyTypesAnswerTypeDef(TypedDict, total=False):
    TerminationPolicyTypes: List[str]


class DescribeWarmPoolAnswerTypeDef(TypedDict, total=False):
    WarmPoolConfiguration: "WarmPoolConfigurationTypeDef"
    Instances: List["InstanceTypeDef"]
    NextToken: str


class DetachInstancesAnswerTypeDef(TypedDict, total=False):
    Activities: List["ActivityTypeDef"]


class EbsTypeDef(TypedDict, total=False):
    SnapshotId: str
    VolumeSize: int
    VolumeType: str
    DeleteOnTermination: bool
    Iops: int
    Encrypted: bool


class EnabledMetricTypeDef(TypedDict, total=False):
    Metric: str
    Granularity: str


class EnterStandbyAnswerTypeDef(TypedDict, total=False):
    Activities: List["ActivityTypeDef"]


class ExitStandbyAnswerTypeDef(TypedDict, total=False):
    Activities: List["ActivityTypeDef"]


class _RequiredFailedScheduledUpdateGroupActionRequestTypeDef(TypedDict):
    ScheduledActionName: str


class FailedScheduledUpdateGroupActionRequestTypeDef(
    _RequiredFailedScheduledUpdateGroupActionRequestTypeDef, total=False
):
    ErrorCode: str
    ErrorMessage: str


class FilterTypeDef(TypedDict, total=False):
    Name: str
    Values: List[str]


class InstanceMetadataOptionsTypeDef(TypedDict, total=False):
    HttpTokens: InstanceMetadataHttpTokensState
    HttpPutResponseHopLimit: int
    HttpEndpoint: InstanceMetadataEndpointState


class InstanceMonitoringTypeDef(TypedDict, total=False):
    Enabled: bool


class InstanceRefreshLivePoolProgressTypeDef(TypedDict, total=False):
    PercentageComplete: int
    InstancesToUpdate: int


class InstanceRefreshProgressDetailsTypeDef(TypedDict, total=False):
    LivePoolProgress: "InstanceRefreshLivePoolProgressTypeDef"
    WarmPoolProgress: "InstanceRefreshWarmPoolProgressTypeDef"


class InstanceRefreshTypeDef(TypedDict, total=False):
    InstanceRefreshId: str
    AutoScalingGroupName: str
    Status: InstanceRefreshStatus
    StatusReason: str
    StartTime: datetime
    EndTime: datetime
    PercentageComplete: int
    InstancesToUpdate: int
    ProgressDetails: "InstanceRefreshProgressDetailsTypeDef"


class InstanceRefreshWarmPoolProgressTypeDef(TypedDict, total=False):
    PercentageComplete: int
    InstancesToUpdate: int


class _RequiredInstanceTypeDef(TypedDict):
    InstanceId: str
    AvailabilityZone: str
    LifecycleState: LifecycleState
    HealthStatus: str
    ProtectedFromScaleIn: bool


class InstanceTypeDef(_RequiredInstanceTypeDef, total=False):
    InstanceType: str
    LaunchConfigurationName: str
    LaunchTemplate: "LaunchTemplateSpecificationTypeDef"
    WeightedCapacity: str


class InstancesDistributionTypeDef(TypedDict, total=False):
    OnDemandAllocationStrategy: str
    OnDemandBaseCapacity: int
    OnDemandPercentageAboveBaseCapacity: int
    SpotAllocationStrategy: str
    SpotInstancePools: int
    SpotMaxPrice: str


class _RequiredLaunchConfigurationTypeDef(TypedDict):
    LaunchConfigurationName: str
    ImageId: str
    InstanceType: str
    CreatedTime: datetime


class LaunchConfigurationTypeDef(_RequiredLaunchConfigurationTypeDef, total=False):
    LaunchConfigurationARN: str
    KeyName: str
    SecurityGroups: List[str]
    ClassicLinkVPCId: str
    ClassicLinkVPCSecurityGroups: List[str]
    UserData: str
    KernelId: str
    RamdiskId: str
    BlockDeviceMappings: List["BlockDeviceMappingTypeDef"]
    InstanceMonitoring: "InstanceMonitoringTypeDef"
    SpotPrice: str
    IamInstanceProfile: str
    EbsOptimized: bool
    AssociatePublicIpAddress: bool
    PlacementTenancy: str
    MetadataOptions: "InstanceMetadataOptionsTypeDef"


class _RequiredLaunchConfigurationsTypeTypeDef(TypedDict):
    LaunchConfigurations: List["LaunchConfigurationTypeDef"]


class LaunchConfigurationsTypeTypeDef(_RequiredLaunchConfigurationsTypeTypeDef, total=False):
    NextToken: str


class LaunchTemplateOverridesTypeDef(TypedDict, total=False):
    InstanceType: str
    WeightedCapacity: str
    LaunchTemplateSpecification: "LaunchTemplateSpecificationTypeDef"


class LaunchTemplateSpecificationTypeDef(TypedDict, total=False):
    LaunchTemplateId: str
    LaunchTemplateName: str
    Version: str


class LaunchTemplateTypeDef(TypedDict, total=False):
    LaunchTemplateSpecification: "LaunchTemplateSpecificationTypeDef"
    Overrides: List["LaunchTemplateOverridesTypeDef"]


class _RequiredLifecycleHookSpecificationTypeDef(TypedDict):
    LifecycleHookName: str
    LifecycleTransition: str


class LifecycleHookSpecificationTypeDef(_RequiredLifecycleHookSpecificationTypeDef, total=False):
    NotificationMetadata: str
    HeartbeatTimeout: int
    DefaultResult: str
    NotificationTargetARN: str
    RoleARN: str


class LifecycleHookTypeDef(TypedDict, total=False):
    LifecycleHookName: str
    AutoScalingGroupName: str
    LifecycleTransition: str
    NotificationTargetARN: str
    RoleARN: str
    NotificationMetadata: str
    HeartbeatTimeout: int
    GlobalTimeout: int
    DefaultResult: str


class LoadBalancerStateTypeDef(TypedDict, total=False):
    LoadBalancerName: str
    State: str


class LoadBalancerTargetGroupStateTypeDef(TypedDict, total=False):
    LoadBalancerTargetGroupARN: str
    State: str


class MetricCollectionTypeTypeDef(TypedDict, total=False):
    Metric: str


class MetricDimensionTypeDef(TypedDict):
    Name: str
    Value: str


class MetricGranularityTypeTypeDef(TypedDict, total=False):
    Granularity: str


class MixedInstancesPolicyTypeDef(TypedDict, total=False):
    LaunchTemplate: "LaunchTemplateTypeDef"
    InstancesDistribution: "InstancesDistributionTypeDef"


class NotificationConfigurationTypeDef(TypedDict, total=False):
    AutoScalingGroupName: str
    TopicARN: str
    NotificationType: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PoliciesTypeTypeDef(TypedDict, total=False):
    ScalingPolicies: List["ScalingPolicyTypeDef"]
    NextToken: str


class PolicyARNTypeTypeDef(TypedDict, total=False):
    PolicyARN: str
    Alarms: List["AlarmTypeDef"]


class _RequiredPredefinedMetricSpecificationTypeDef(TypedDict):
    PredefinedMetricType: MetricType


class PredefinedMetricSpecificationTypeDef(
    _RequiredPredefinedMetricSpecificationTypeDef, total=False
):
    ResourceLabel: str


class ProcessTypeTypeDef(TypedDict):
    ProcessName: str


class ProcessesTypeTypeDef(TypedDict, total=False):
    Processes: List["ProcessTypeTypeDef"]


class RefreshPreferencesTypeDef(TypedDict, total=False):
    MinHealthyPercentage: int
    InstanceWarmup: int
    CheckpointPercentages: List[int]
    CheckpointDelay: int


class ScalingPolicyTypeDef(TypedDict, total=False):
    AutoScalingGroupName: str
    PolicyName: str
    PolicyARN: str
    PolicyType: str
    AdjustmentType: str
    MinAdjustmentStep: int
    MinAdjustmentMagnitude: int
    ScalingAdjustment: int
    Cooldown: int
    StepAdjustments: List["StepAdjustmentTypeDef"]
    MetricAggregationType: str
    EstimatedInstanceWarmup: int
    Alarms: List["AlarmTypeDef"]
    TargetTrackingConfiguration: "TargetTrackingConfigurationTypeDef"
    Enabled: bool


class ScheduledActionsTypeTypeDef(TypedDict, total=False):
    ScheduledUpdateGroupActions: List["ScheduledUpdateGroupActionTypeDef"]
    NextToken: str


class _RequiredScheduledUpdateGroupActionRequestTypeDef(TypedDict):
    ScheduledActionName: str


class ScheduledUpdateGroupActionRequestTypeDef(
    _RequiredScheduledUpdateGroupActionRequestTypeDef, total=False
):
    StartTime: datetime
    EndTime: datetime
    Recurrence: str
    MinSize: int
    MaxSize: int
    DesiredCapacity: int
    TimeZone: str


class ScheduledUpdateGroupActionTypeDef(TypedDict, total=False):
    AutoScalingGroupName: str
    ScheduledActionName: str
    ScheduledActionARN: str
    Time: datetime
    StartTime: datetime
    EndTime: datetime
    Recurrence: str
    MinSize: int
    MaxSize: int
    DesiredCapacity: int
    TimeZone: str


class StartInstanceRefreshAnswerTypeDef(TypedDict, total=False):
    InstanceRefreshId: str


class _RequiredStepAdjustmentTypeDef(TypedDict):
    ScalingAdjustment: int


class StepAdjustmentTypeDef(_RequiredStepAdjustmentTypeDef, total=False):
    MetricIntervalLowerBound: float
    MetricIntervalUpperBound: float


class SuspendedProcessTypeDef(TypedDict, total=False):
    ProcessName: str
    SuspensionReason: str


class TagDescriptionTypeDef(TypedDict, total=False):
    ResourceId: str
    ResourceType: str
    Key: str
    Value: str
    PropagateAtLaunch: bool


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    ResourceId: str
    ResourceType: str
    Value: str
    PropagateAtLaunch: bool


class TagsTypeTypeDef(TypedDict, total=False):
    Tags: List["TagDescriptionTypeDef"]
    NextToken: str


class _RequiredTargetTrackingConfigurationTypeDef(TypedDict):
    TargetValue: float


class TargetTrackingConfigurationTypeDef(_RequiredTargetTrackingConfigurationTypeDef, total=False):
    PredefinedMetricSpecification: "PredefinedMetricSpecificationTypeDef"
    CustomizedMetricSpecification: "CustomizedMetricSpecificationTypeDef"
    DisableScaleIn: bool


class WarmPoolConfigurationTypeDef(TypedDict, total=False):
    MaxGroupPreparedCapacity: int
    MinSize: int
    PoolState: WarmPoolState
    Status: Literal["PendingDelete"]
