"""
Type annotations for emr service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/type_defs.html)

Usage::

    ```python
    from mypy_boto3_emr.type_defs import AddInstanceFleetOutputTypeDef

    data: AddInstanceFleetOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_emr.literals import (
    ActionOnFailure,
    AdjustmentType,
    AuthMode,
    AutoScalingPolicyState,
    AutoScalingPolicyStateChangeReasonCode,
    CancelStepsRequestStatus,
    ClusterState,
    ClusterStateChangeReasonCode,
    ComparisonOperator,
    ComputeLimitsUnitType,
    IdentityType,
    InstanceCollectionType,
    InstanceFleetState,
    InstanceFleetStateChangeReasonCode,
    InstanceFleetType,
    InstanceGroupState,
    InstanceGroupStateChangeReasonCode,
    InstanceGroupType,
    InstanceRoleType,
    InstanceState,
    InstanceStateChangeReasonCode,
    JobFlowExecutionState,
    MarketType,
    NotebookExecutionStatus,
    OnDemandCapacityReservationPreference,
    PlacementGroupStrategy,
    RepoUpgradeOnBoot,
    ScaleDownBehavior,
    SpotProvisioningTimeoutAction,
    Statistic,
    StepExecutionState,
    StepState,
    Unit,
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
    "AddInstanceFleetOutputTypeDef",
    "AddInstanceGroupsOutputTypeDef",
    "AddJobFlowStepsOutputTypeDef",
    "ApplicationTypeDef",
    "AutoScalingPolicyDescriptionTypeDef",
    "AutoScalingPolicyStateChangeReasonTypeDef",
    "AutoScalingPolicyStatusTypeDef",
    "AutoScalingPolicyTypeDef",
    "BlockPublicAccessConfigurationMetadataTypeDef",
    "BlockPublicAccessConfigurationTypeDef",
    "BootstrapActionConfigTypeDef",
    "BootstrapActionDetailTypeDef",
    "CancelStepsInfoTypeDef",
    "CancelStepsOutputTypeDef",
    "CloudWatchAlarmDefinitionTypeDef",
    "ClusterStateChangeReasonTypeDef",
    "ClusterStatusTypeDef",
    "ClusterSummaryTypeDef",
    "ClusterTimelineTypeDef",
    "ClusterTypeDef",
    "CommandTypeDef",
    "ComputeLimitsTypeDef",
    "ConfigurationTypeDef",
    "CreateSecurityConfigurationOutputTypeDef",
    "CreateStudioOutputTypeDef",
    "DescribeClusterOutputTypeDef",
    "DescribeJobFlowsOutputTypeDef",
    "DescribeNotebookExecutionOutputTypeDef",
    "DescribeSecurityConfigurationOutputTypeDef",
    "DescribeStepOutputTypeDef",
    "DescribeStudioOutputTypeDef",
    "EbsBlockDeviceConfigTypeDef",
    "EbsBlockDeviceTypeDef",
    "EbsConfigurationTypeDef",
    "EbsVolumeTypeDef",
    "Ec2InstanceAttributesTypeDef",
    "ExecutionEngineConfigTypeDef",
    "FailureDetailsTypeDef",
    "GetBlockPublicAccessConfigurationOutputTypeDef",
    "GetManagedScalingPolicyOutputTypeDef",
    "GetStudioSessionMappingOutputTypeDef",
    "HadoopJarStepConfigTypeDef",
    "HadoopStepConfigTypeDef",
    "InstanceFleetConfigTypeDef",
    "InstanceFleetModifyConfigTypeDef",
    "InstanceFleetProvisioningSpecificationsTypeDef",
    "InstanceFleetStateChangeReasonTypeDef",
    "InstanceFleetStatusTypeDef",
    "InstanceFleetTimelineTypeDef",
    "InstanceFleetTypeDef",
    "InstanceGroupConfigTypeDef",
    "InstanceGroupDetailTypeDef",
    "InstanceGroupModifyConfigTypeDef",
    "InstanceGroupStateChangeReasonTypeDef",
    "InstanceGroupStatusTypeDef",
    "InstanceGroupTimelineTypeDef",
    "InstanceGroupTypeDef",
    "InstanceResizePolicyTypeDef",
    "InstanceStateChangeReasonTypeDef",
    "InstanceStatusTypeDef",
    "InstanceTimelineTypeDef",
    "InstanceTypeConfigTypeDef",
    "InstanceTypeDef",
    "InstanceTypeSpecificationTypeDef",
    "JobFlowDetailTypeDef",
    "JobFlowExecutionStatusDetailTypeDef",
    "JobFlowInstancesConfigTypeDef",
    "JobFlowInstancesDetailTypeDef",
    "KerberosAttributesTypeDef",
    "KeyValueTypeDef",
    "ListBootstrapActionsOutputTypeDef",
    "ListClustersOutputTypeDef",
    "ListInstanceFleetsOutputTypeDef",
    "ListInstanceGroupsOutputTypeDef",
    "ListInstancesOutputTypeDef",
    "ListNotebookExecutionsOutputTypeDef",
    "ListSecurityConfigurationsOutputTypeDef",
    "ListStepsOutputTypeDef",
    "ListStudioSessionMappingsOutputTypeDef",
    "ListStudiosOutputTypeDef",
    "ManagedScalingPolicyTypeDef",
    "MetricDimensionTypeDef",
    "ModifyClusterOutputTypeDef",
    "NotebookExecutionSummaryTypeDef",
    "NotebookExecutionTypeDef",
    "OnDemandCapacityReservationOptionsTypeDef",
    "OnDemandProvisioningSpecificationTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementGroupConfigTypeDef",
    "PlacementTypeTypeDef",
    "PortRangeTypeDef",
    "PutAutoScalingPolicyOutputTypeDef",
    "ResponseMetadata",
    "RunJobFlowOutputTypeDef",
    "ScalingActionTypeDef",
    "ScalingConstraintsTypeDef",
    "ScalingRuleTypeDef",
    "ScalingTriggerTypeDef",
    "ScriptBootstrapActionConfigTypeDef",
    "SecurityConfigurationSummaryTypeDef",
    "SessionMappingDetailTypeDef",
    "SessionMappingSummaryTypeDef",
    "ShrinkPolicyTypeDef",
    "SimpleScalingPolicyConfigurationTypeDef",
    "SpotProvisioningSpecificationTypeDef",
    "StartNotebookExecutionOutputTypeDef",
    "StepConfigTypeDef",
    "StepDetailTypeDef",
    "StepExecutionStatusDetailTypeDef",
    "StepStateChangeReasonTypeDef",
    "StepStatusTypeDef",
    "StepSummaryTypeDef",
    "StepTimelineTypeDef",
    "StepTypeDef",
    "StudioSummaryTypeDef",
    "StudioTypeDef",
    "SupportedProductConfigTypeDef",
    "TagTypeDef",
    "VolumeSpecificationTypeDef",
    "WaiterConfigTypeDef",
)


class AddInstanceFleetOutputTypeDef(TypedDict):
    ClusterId: str
    InstanceFleetId: str
    ClusterArn: str
    ResponseMetadata: "ResponseMetadata"


class AddInstanceGroupsOutputTypeDef(TypedDict):
    JobFlowId: str
    InstanceGroupIds: List[str]
    ClusterArn: str
    ResponseMetadata: "ResponseMetadata"


class AddJobFlowStepsOutputTypeDef(TypedDict):
    StepIds: List[str]
    ResponseMetadata: "ResponseMetadata"


class ApplicationTypeDef(TypedDict, total=False):
    Name: str
    Version: str
    Args: List[str]
    AdditionalInfo: Dict[str, str]


class AutoScalingPolicyDescriptionTypeDef(TypedDict, total=False):
    Status: "AutoScalingPolicyStatusTypeDef"
    Constraints: "ScalingConstraintsTypeDef"
    Rules: List["ScalingRuleTypeDef"]


class AutoScalingPolicyStateChangeReasonTypeDef(TypedDict, total=False):
    Code: AutoScalingPolicyStateChangeReasonCode
    Message: str


class AutoScalingPolicyStatusTypeDef(TypedDict, total=False):
    State: AutoScalingPolicyState
    StateChangeReason: "AutoScalingPolicyStateChangeReasonTypeDef"


class AutoScalingPolicyTypeDef(TypedDict):
    Constraints: "ScalingConstraintsTypeDef"
    Rules: List["ScalingRuleTypeDef"]


class BlockPublicAccessConfigurationMetadataTypeDef(TypedDict):
    CreationDateTime: datetime
    CreatedByArn: str


class _RequiredBlockPublicAccessConfigurationTypeDef(TypedDict):
    BlockPublicSecurityGroupRules: bool


class BlockPublicAccessConfigurationTypeDef(
    _RequiredBlockPublicAccessConfigurationTypeDef, total=False
):
    PermittedPublicSecurityGroupRuleRanges: List["PortRangeTypeDef"]


class BootstrapActionConfigTypeDef(TypedDict):
    Name: str
    ScriptBootstrapAction: "ScriptBootstrapActionConfigTypeDef"


class BootstrapActionDetailTypeDef(TypedDict, total=False):
    BootstrapActionConfig: "BootstrapActionConfigTypeDef"


class CancelStepsInfoTypeDef(TypedDict, total=False):
    StepId: str
    Status: CancelStepsRequestStatus
    Reason: str


class CancelStepsOutputTypeDef(TypedDict):
    CancelStepsInfoList: List["CancelStepsInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class _RequiredCloudWatchAlarmDefinitionTypeDef(TypedDict):
    ComparisonOperator: ComparisonOperator
    MetricName: str
    Period: int
    Threshold: float


class CloudWatchAlarmDefinitionTypeDef(_RequiredCloudWatchAlarmDefinitionTypeDef, total=False):
    EvaluationPeriods: int
    Namespace: str
    Statistic: Statistic
    Unit: Unit
    Dimensions: List["MetricDimensionTypeDef"]


class ClusterStateChangeReasonTypeDef(TypedDict, total=False):
    Code: ClusterStateChangeReasonCode
    Message: str


class ClusterStatusTypeDef(TypedDict, total=False):
    State: ClusterState
    StateChangeReason: "ClusterStateChangeReasonTypeDef"
    Timeline: "ClusterTimelineTypeDef"


class ClusterSummaryTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Status: "ClusterStatusTypeDef"
    NormalizedInstanceHours: int
    ClusterArn: str
    OutpostArn: str


class ClusterTimelineTypeDef(TypedDict, total=False):
    CreationDateTime: datetime
    ReadyDateTime: datetime
    EndDateTime: datetime


class ClusterTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Status: "ClusterStatusTypeDef"
    Ec2InstanceAttributes: "Ec2InstanceAttributesTypeDef"
    InstanceCollectionType: InstanceCollectionType
    LogUri: str
    LogEncryptionKmsKeyId: str
    RequestedAmiVersion: str
    RunningAmiVersion: str
    ReleaseLabel: str
    AutoTerminate: bool
    TerminationProtected: bool
    VisibleToAllUsers: bool
    Applications: List["ApplicationTypeDef"]
    Tags: List["TagTypeDef"]
    ServiceRole: str
    NormalizedInstanceHours: int
    MasterPublicDnsName: str
    Configurations: List["ConfigurationTypeDef"]
    SecurityConfiguration: str
    AutoScalingRole: str
    ScaleDownBehavior: ScaleDownBehavior
    CustomAmiId: str
    EbsRootVolumeSize: int
    RepoUpgradeOnBoot: RepoUpgradeOnBoot
    KerberosAttributes: "KerberosAttributesTypeDef"
    ClusterArn: str
    OutpostArn: str
    StepConcurrencyLevel: int
    PlacementGroups: List["PlacementGroupConfigTypeDef"]


class CommandTypeDef(TypedDict, total=False):
    Name: str
    ScriptPath: str
    Args: List[str]


class _RequiredComputeLimitsTypeDef(TypedDict):
    UnitType: ComputeLimitsUnitType
    MinimumCapacityUnits: int
    MaximumCapacityUnits: int


class ComputeLimitsTypeDef(_RequiredComputeLimitsTypeDef, total=False):
    MaximumOnDemandCapacityUnits: int
    MaximumCoreCapacityUnits: int


class ConfigurationTypeDef(TypedDict, total=False):
    Classification: str
    Configurations: List[Dict[str, Any]]
    Properties: Dict[str, str]


class CreateSecurityConfigurationOutputTypeDef(TypedDict):
    Name: str
    CreationDateTime: datetime
    ResponseMetadata: "ResponseMetadata"


class CreateStudioOutputTypeDef(TypedDict):
    StudioId: str
    Url: str
    ResponseMetadata: "ResponseMetadata"


class DescribeClusterOutputTypeDef(TypedDict):
    Cluster: "ClusterTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeJobFlowsOutputTypeDef(TypedDict):
    JobFlows: List["JobFlowDetailTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeNotebookExecutionOutputTypeDef(TypedDict):
    NotebookExecution: "NotebookExecutionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeSecurityConfigurationOutputTypeDef(TypedDict):
    Name: str
    SecurityConfiguration: str
    CreationDateTime: datetime
    ResponseMetadata: "ResponseMetadata"


class DescribeStepOutputTypeDef(TypedDict):
    Step: "StepTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeStudioOutputTypeDef(TypedDict):
    Studio: "StudioTypeDef"
    ResponseMetadata: "ResponseMetadata"


class _RequiredEbsBlockDeviceConfigTypeDef(TypedDict):
    VolumeSpecification: "VolumeSpecificationTypeDef"


class EbsBlockDeviceConfigTypeDef(_RequiredEbsBlockDeviceConfigTypeDef, total=False):
    VolumesPerInstance: int


class EbsBlockDeviceTypeDef(TypedDict, total=False):
    VolumeSpecification: "VolumeSpecificationTypeDef"
    Device: str


class EbsConfigurationTypeDef(TypedDict, total=False):
    EbsBlockDeviceConfigs: List["EbsBlockDeviceConfigTypeDef"]
    EbsOptimized: bool


class EbsVolumeTypeDef(TypedDict, total=False):
    Device: str
    VolumeId: str


class Ec2InstanceAttributesTypeDef(TypedDict, total=False):
    Ec2KeyName: str
    Ec2SubnetId: str
    RequestedEc2SubnetIds: List[str]
    Ec2AvailabilityZone: str
    RequestedEc2AvailabilityZones: List[str]
    IamInstanceProfile: str
    EmrManagedMasterSecurityGroup: str
    EmrManagedSlaveSecurityGroup: str
    ServiceAccessSecurityGroup: str
    AdditionalMasterSecurityGroups: List[str]
    AdditionalSlaveSecurityGroups: List[str]


_RequiredExecutionEngineConfigTypeDef = TypedDict(
    "_RequiredExecutionEngineConfigTypeDef", {"Id": str}
)
_OptionalExecutionEngineConfigTypeDef = TypedDict(
    "_OptionalExecutionEngineConfigTypeDef",
    {"Type": Literal["EMR"], "MasterInstanceSecurityGroupId": str},
    total=False,
)


class ExecutionEngineConfigTypeDef(
    _RequiredExecutionEngineConfigTypeDef, _OptionalExecutionEngineConfigTypeDef
):
    pass


class FailureDetailsTypeDef(TypedDict, total=False):
    Reason: str
    Message: str
    LogFile: str


class GetBlockPublicAccessConfigurationOutputTypeDef(TypedDict):
    BlockPublicAccessConfiguration: "BlockPublicAccessConfigurationTypeDef"
    BlockPublicAccessConfigurationMetadata: "BlockPublicAccessConfigurationMetadataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetManagedScalingPolicyOutputTypeDef(TypedDict):
    ManagedScalingPolicy: "ManagedScalingPolicyTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetStudioSessionMappingOutputTypeDef(TypedDict):
    SessionMapping: "SessionMappingDetailTypeDef"
    ResponseMetadata: "ResponseMetadata"


class _RequiredHadoopJarStepConfigTypeDef(TypedDict):
    Jar: str


class HadoopJarStepConfigTypeDef(_RequiredHadoopJarStepConfigTypeDef, total=False):
    Properties: List["KeyValueTypeDef"]
    MainClass: str
    Args: List[str]


class HadoopStepConfigTypeDef(TypedDict, total=False):
    Jar: str
    Properties: Dict[str, str]
    MainClass: str
    Args: List[str]


class _RequiredInstanceFleetConfigTypeDef(TypedDict):
    InstanceFleetType: InstanceFleetType


class InstanceFleetConfigTypeDef(_RequiredInstanceFleetConfigTypeDef, total=False):
    Name: str
    TargetOnDemandCapacity: int
    TargetSpotCapacity: int
    InstanceTypeConfigs: List["InstanceTypeConfigTypeDef"]
    LaunchSpecifications: "InstanceFleetProvisioningSpecificationsTypeDef"


class _RequiredInstanceFleetModifyConfigTypeDef(TypedDict):
    InstanceFleetId: str


class InstanceFleetModifyConfigTypeDef(_RequiredInstanceFleetModifyConfigTypeDef, total=False):
    TargetOnDemandCapacity: int
    TargetSpotCapacity: int


class InstanceFleetProvisioningSpecificationsTypeDef(TypedDict, total=False):
    SpotSpecification: "SpotProvisioningSpecificationTypeDef"
    OnDemandSpecification: "OnDemandProvisioningSpecificationTypeDef"


class InstanceFleetStateChangeReasonTypeDef(TypedDict, total=False):
    Code: InstanceFleetStateChangeReasonCode
    Message: str


class InstanceFleetStatusTypeDef(TypedDict, total=False):
    State: InstanceFleetState
    StateChangeReason: "InstanceFleetStateChangeReasonTypeDef"
    Timeline: "InstanceFleetTimelineTypeDef"


class InstanceFleetTimelineTypeDef(TypedDict, total=False):
    CreationDateTime: datetime
    ReadyDateTime: datetime
    EndDateTime: datetime


class InstanceFleetTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Status: "InstanceFleetStatusTypeDef"
    InstanceFleetType: InstanceFleetType
    TargetOnDemandCapacity: int
    TargetSpotCapacity: int
    ProvisionedOnDemandCapacity: int
    ProvisionedSpotCapacity: int
    InstanceTypeSpecifications: List["InstanceTypeSpecificationTypeDef"]
    LaunchSpecifications: "InstanceFleetProvisioningSpecificationsTypeDef"


class _RequiredInstanceGroupConfigTypeDef(TypedDict):
    InstanceRole: InstanceRoleType
    InstanceType: str
    InstanceCount: int


class InstanceGroupConfigTypeDef(_RequiredInstanceGroupConfigTypeDef, total=False):
    Name: str
    Market: MarketType
    BidPrice: str
    Configurations: List["ConfigurationTypeDef"]
    EbsConfiguration: "EbsConfigurationTypeDef"
    AutoScalingPolicy: "AutoScalingPolicyTypeDef"


class _RequiredInstanceGroupDetailTypeDef(TypedDict):
    Market: MarketType
    InstanceRole: InstanceRoleType
    InstanceType: str
    InstanceRequestCount: int
    InstanceRunningCount: int
    State: InstanceGroupState
    CreationDateTime: datetime


class InstanceGroupDetailTypeDef(_RequiredInstanceGroupDetailTypeDef, total=False):
    InstanceGroupId: str
    Name: str
    BidPrice: str
    LastStateChangeReason: str
    StartDateTime: datetime
    ReadyDateTime: datetime
    EndDateTime: datetime


class _RequiredInstanceGroupModifyConfigTypeDef(TypedDict):
    InstanceGroupId: str


class InstanceGroupModifyConfigTypeDef(_RequiredInstanceGroupModifyConfigTypeDef, total=False):
    InstanceCount: int
    EC2InstanceIdsToTerminate: List[str]
    ShrinkPolicy: "ShrinkPolicyTypeDef"
    Configurations: List["ConfigurationTypeDef"]


class InstanceGroupStateChangeReasonTypeDef(TypedDict, total=False):
    Code: InstanceGroupStateChangeReasonCode
    Message: str


class InstanceGroupStatusTypeDef(TypedDict, total=False):
    State: InstanceGroupState
    StateChangeReason: "InstanceGroupStateChangeReasonTypeDef"
    Timeline: "InstanceGroupTimelineTypeDef"


class InstanceGroupTimelineTypeDef(TypedDict, total=False):
    CreationDateTime: datetime
    ReadyDateTime: datetime
    EndDateTime: datetime


class InstanceGroupTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Market: MarketType
    InstanceGroupType: InstanceGroupType
    BidPrice: str
    InstanceType: str
    RequestedInstanceCount: int
    RunningInstanceCount: int
    Status: "InstanceGroupStatusTypeDef"
    Configurations: List["ConfigurationTypeDef"]
    ConfigurationsVersion: int
    LastSuccessfullyAppliedConfigurations: List["ConfigurationTypeDef"]
    LastSuccessfullyAppliedConfigurationsVersion: int
    EbsBlockDevices: List["EbsBlockDeviceTypeDef"]
    EbsOptimized: bool
    ShrinkPolicy: "ShrinkPolicyTypeDef"
    AutoScalingPolicy: "AutoScalingPolicyDescriptionTypeDef"


class InstanceResizePolicyTypeDef(TypedDict, total=False):
    InstancesToTerminate: List[str]
    InstancesToProtect: List[str]
    InstanceTerminationTimeout: int


class InstanceStateChangeReasonTypeDef(TypedDict, total=False):
    Code: InstanceStateChangeReasonCode
    Message: str


class InstanceStatusTypeDef(TypedDict, total=False):
    State: InstanceState
    StateChangeReason: "InstanceStateChangeReasonTypeDef"
    Timeline: "InstanceTimelineTypeDef"


class InstanceTimelineTypeDef(TypedDict, total=False):
    CreationDateTime: datetime
    ReadyDateTime: datetime
    EndDateTime: datetime


class _RequiredInstanceTypeConfigTypeDef(TypedDict):
    InstanceType: str


class InstanceTypeConfigTypeDef(_RequiredInstanceTypeConfigTypeDef, total=False):
    WeightedCapacity: int
    BidPrice: str
    BidPriceAsPercentageOfOnDemandPrice: float
    EbsConfiguration: "EbsConfigurationTypeDef"
    Configurations: List["ConfigurationTypeDef"]


class InstanceTypeDef(TypedDict, total=False):
    Id: str
    Ec2InstanceId: str
    PublicDnsName: str
    PublicIpAddress: str
    PrivateDnsName: str
    PrivateIpAddress: str
    Status: "InstanceStatusTypeDef"
    InstanceGroupId: str
    InstanceFleetId: str
    Market: MarketType
    InstanceType: str
    EbsVolumes: List["EbsVolumeTypeDef"]


class InstanceTypeSpecificationTypeDef(TypedDict, total=False):
    InstanceType: str
    WeightedCapacity: int
    BidPrice: str
    BidPriceAsPercentageOfOnDemandPrice: float
    Configurations: List["ConfigurationTypeDef"]
    EbsBlockDevices: List["EbsBlockDeviceTypeDef"]
    EbsOptimized: bool


class _RequiredJobFlowDetailTypeDef(TypedDict):
    JobFlowId: str
    Name: str
    ExecutionStatusDetail: "JobFlowExecutionStatusDetailTypeDef"
    Instances: "JobFlowInstancesDetailTypeDef"


class JobFlowDetailTypeDef(_RequiredJobFlowDetailTypeDef, total=False):
    LogUri: str
    LogEncryptionKmsKeyId: str
    AmiVersion: str
    Steps: List["StepDetailTypeDef"]
    BootstrapActions: List["BootstrapActionDetailTypeDef"]
    SupportedProducts: List[str]
    VisibleToAllUsers: bool
    JobFlowRole: str
    ServiceRole: str
    AutoScalingRole: str
    ScaleDownBehavior: ScaleDownBehavior


class _RequiredJobFlowExecutionStatusDetailTypeDef(TypedDict):
    State: JobFlowExecutionState
    CreationDateTime: datetime


class JobFlowExecutionStatusDetailTypeDef(
    _RequiredJobFlowExecutionStatusDetailTypeDef, total=False
):
    StartDateTime: datetime
    ReadyDateTime: datetime
    EndDateTime: datetime
    LastStateChangeReason: str


class JobFlowInstancesConfigTypeDef(TypedDict, total=False):
    MasterInstanceType: str
    SlaveInstanceType: str
    InstanceCount: int
    InstanceGroups: List["InstanceGroupConfigTypeDef"]
    InstanceFleets: List["InstanceFleetConfigTypeDef"]
    Ec2KeyName: str
    Placement: "PlacementTypeTypeDef"
    KeepJobFlowAliveWhenNoSteps: bool
    TerminationProtected: bool
    HadoopVersion: str
    Ec2SubnetId: str
    Ec2SubnetIds: List[str]
    EmrManagedMasterSecurityGroup: str
    EmrManagedSlaveSecurityGroup: str
    ServiceAccessSecurityGroup: str
    AdditionalMasterSecurityGroups: List[str]
    AdditionalSlaveSecurityGroups: List[str]


class _RequiredJobFlowInstancesDetailTypeDef(TypedDict):
    MasterInstanceType: str
    SlaveInstanceType: str
    InstanceCount: int


class JobFlowInstancesDetailTypeDef(_RequiredJobFlowInstancesDetailTypeDef, total=False):
    MasterPublicDnsName: str
    MasterInstanceId: str
    InstanceGroups: List["InstanceGroupDetailTypeDef"]
    NormalizedInstanceHours: int
    Ec2KeyName: str
    Ec2SubnetId: str
    Placement: "PlacementTypeTypeDef"
    KeepJobFlowAliveWhenNoSteps: bool
    TerminationProtected: bool
    HadoopVersion: str


class _RequiredKerberosAttributesTypeDef(TypedDict):
    Realm: str
    KdcAdminPassword: str


class KerberosAttributesTypeDef(_RequiredKerberosAttributesTypeDef, total=False):
    CrossRealmTrustPrincipalPassword: str
    ADDomainJoinUser: str
    ADDomainJoinPassword: str


class KeyValueTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class ListBootstrapActionsOutputTypeDef(TypedDict):
    BootstrapActions: List["CommandTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ListClustersOutputTypeDef(TypedDict):
    Clusters: List["ClusterSummaryTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ListInstanceFleetsOutputTypeDef(TypedDict):
    InstanceFleets: List["InstanceFleetTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ListInstanceGroupsOutputTypeDef(TypedDict):
    InstanceGroups: List["InstanceGroupTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ListInstancesOutputTypeDef(TypedDict):
    Instances: List["InstanceTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ListNotebookExecutionsOutputTypeDef(TypedDict):
    NotebookExecutions: List["NotebookExecutionSummaryTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ListSecurityConfigurationsOutputTypeDef(TypedDict):
    SecurityConfigurations: List["SecurityConfigurationSummaryTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ListStepsOutputTypeDef(TypedDict):
    Steps: List["StepSummaryTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ListStudioSessionMappingsOutputTypeDef(TypedDict):
    SessionMappings: List["SessionMappingSummaryTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ListStudiosOutputTypeDef(TypedDict):
    Studios: List["StudioSummaryTypeDef"]
    Marker: str
    ResponseMetadata: "ResponseMetadata"


class ManagedScalingPolicyTypeDef(TypedDict, total=False):
    ComputeLimits: "ComputeLimitsTypeDef"


class MetricDimensionTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class ModifyClusterOutputTypeDef(TypedDict):
    StepConcurrencyLevel: int
    ResponseMetadata: "ResponseMetadata"


class NotebookExecutionSummaryTypeDef(TypedDict, total=False):
    NotebookExecutionId: str
    EditorId: str
    NotebookExecutionName: str
    Status: NotebookExecutionStatus
    StartTime: datetime
    EndTime: datetime


class NotebookExecutionTypeDef(TypedDict, total=False):
    NotebookExecutionId: str
    EditorId: str
    ExecutionEngine: "ExecutionEngineConfigTypeDef"
    NotebookExecutionName: str
    NotebookParams: str
    Status: NotebookExecutionStatus
    StartTime: datetime
    EndTime: datetime
    Arn: str
    OutputNotebookURI: str
    LastStateChangeReason: str
    NotebookInstanceSecurityGroupId: str
    Tags: List["TagTypeDef"]


class OnDemandCapacityReservationOptionsTypeDef(TypedDict, total=False):
    UsageStrategy: Literal["use-capacity-reservations-first"]
    CapacityReservationPreference: OnDemandCapacityReservationPreference
    CapacityReservationResourceGroupArn: str


class _RequiredOnDemandProvisioningSpecificationTypeDef(TypedDict):
    AllocationStrategy: Literal["lowest-price"]


class OnDemandProvisioningSpecificationTypeDef(
    _RequiredOnDemandProvisioningSpecificationTypeDef, total=False
):
    CapacityReservationOptions: "OnDemandCapacityReservationOptionsTypeDef"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredPlacementGroupConfigTypeDef(TypedDict):
    InstanceRole: InstanceRoleType


class PlacementGroupConfigTypeDef(_RequiredPlacementGroupConfigTypeDef, total=False):
    PlacementStrategy: PlacementGroupStrategy


class PlacementTypeTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    AvailabilityZones: List[str]


class _RequiredPortRangeTypeDef(TypedDict):
    MinRange: int


class PortRangeTypeDef(_RequiredPortRangeTypeDef, total=False):
    MaxRange: int


class PutAutoScalingPolicyOutputTypeDef(TypedDict):
    ClusterId: str
    InstanceGroupId: str
    AutoScalingPolicy: "AutoScalingPolicyDescriptionTypeDef"
    ClusterArn: str
    ResponseMetadata: "ResponseMetadata"


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RunJobFlowOutputTypeDef(TypedDict):
    JobFlowId: str
    ClusterArn: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredScalingActionTypeDef(TypedDict):
    SimpleScalingPolicyConfiguration: "SimpleScalingPolicyConfigurationTypeDef"


class ScalingActionTypeDef(_RequiredScalingActionTypeDef, total=False):
    Market: MarketType


class ScalingConstraintsTypeDef(TypedDict):
    MinCapacity: int
    MaxCapacity: int


class _RequiredScalingRuleTypeDef(TypedDict):
    Name: str
    Action: "ScalingActionTypeDef"
    Trigger: "ScalingTriggerTypeDef"


class ScalingRuleTypeDef(_RequiredScalingRuleTypeDef, total=False):
    Description: str


class ScalingTriggerTypeDef(TypedDict):
    CloudWatchAlarmDefinition: "CloudWatchAlarmDefinitionTypeDef"


class _RequiredScriptBootstrapActionConfigTypeDef(TypedDict):
    Path: str


class ScriptBootstrapActionConfigTypeDef(_RequiredScriptBootstrapActionConfigTypeDef, total=False):
    Args: List[str]


class SecurityConfigurationSummaryTypeDef(TypedDict, total=False):
    Name: str
    CreationDateTime: datetime


class SessionMappingDetailTypeDef(TypedDict, total=False):
    StudioId: str
    IdentityId: str
    IdentityName: str
    IdentityType: IdentityType
    SessionPolicyArn: str
    CreationTime: datetime
    LastModifiedTime: datetime


class SessionMappingSummaryTypeDef(TypedDict, total=False):
    StudioId: str
    IdentityId: str
    IdentityName: str
    IdentityType: IdentityType
    SessionPolicyArn: str
    CreationTime: datetime


class ShrinkPolicyTypeDef(TypedDict, total=False):
    DecommissionTimeout: int
    InstanceResizePolicy: "InstanceResizePolicyTypeDef"


class _RequiredSimpleScalingPolicyConfigurationTypeDef(TypedDict):
    ScalingAdjustment: int


class SimpleScalingPolicyConfigurationTypeDef(
    _RequiredSimpleScalingPolicyConfigurationTypeDef, total=False
):
    AdjustmentType: AdjustmentType
    CoolDown: int


class _RequiredSpotProvisioningSpecificationTypeDef(TypedDict):
    TimeoutDurationMinutes: int
    TimeoutAction: SpotProvisioningTimeoutAction


class SpotProvisioningSpecificationTypeDef(
    _RequiredSpotProvisioningSpecificationTypeDef, total=False
):
    BlockDurationMinutes: int
    AllocationStrategy: Literal["capacity-optimized"]


class StartNotebookExecutionOutputTypeDef(TypedDict):
    NotebookExecutionId: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredStepConfigTypeDef(TypedDict):
    Name: str
    HadoopJarStep: "HadoopJarStepConfigTypeDef"


class StepConfigTypeDef(_RequiredStepConfigTypeDef, total=False):
    ActionOnFailure: ActionOnFailure


class StepDetailTypeDef(TypedDict):
    StepConfig: "StepConfigTypeDef"
    ExecutionStatusDetail: "StepExecutionStatusDetailTypeDef"


class _RequiredStepExecutionStatusDetailTypeDef(TypedDict):
    State: StepExecutionState
    CreationDateTime: datetime


class StepExecutionStatusDetailTypeDef(_RequiredStepExecutionStatusDetailTypeDef, total=False):
    StartDateTime: datetime
    EndDateTime: datetime
    LastStateChangeReason: str


class StepStateChangeReasonTypeDef(TypedDict, total=False):
    Code: Literal["NONE"]
    Message: str


class StepStatusTypeDef(TypedDict, total=False):
    State: StepState
    StateChangeReason: "StepStateChangeReasonTypeDef"
    FailureDetails: "FailureDetailsTypeDef"
    Timeline: "StepTimelineTypeDef"


class StepSummaryTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Config: "HadoopStepConfigTypeDef"
    ActionOnFailure: ActionOnFailure
    Status: "StepStatusTypeDef"


class StepTimelineTypeDef(TypedDict, total=False):
    CreationDateTime: datetime
    StartDateTime: datetime
    EndDateTime: datetime


class StepTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Config: "HadoopStepConfigTypeDef"
    ActionOnFailure: ActionOnFailure
    Status: "StepStatusTypeDef"


class StudioSummaryTypeDef(TypedDict, total=False):
    StudioId: str
    Name: str
    VpcId: str
    Description: str
    Url: str
    CreationTime: datetime


class StudioTypeDef(TypedDict, total=False):
    StudioId: str
    StudioArn: str
    Name: str
    Description: str
    AuthMode: AuthMode
    VpcId: str
    SubnetIds: List[str]
    ServiceRole: str
    UserRole: str
    WorkspaceSecurityGroupId: str
    EngineSecurityGroupId: str
    Url: str
    CreationTime: datetime
    DefaultS3Location: str
    Tags: List["TagTypeDef"]


class SupportedProductConfigTypeDef(TypedDict, total=False):
    Name: str
    Args: List[str]


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class _RequiredVolumeSpecificationTypeDef(TypedDict):
    VolumeType: str
    SizeInGB: int


class VolumeSpecificationTypeDef(_RequiredVolumeSpecificationTypeDef, total=False):
    Iops: int


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
