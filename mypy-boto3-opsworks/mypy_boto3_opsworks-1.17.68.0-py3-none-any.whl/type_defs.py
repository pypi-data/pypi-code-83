"""
Type annotations for opsworks service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/type_defs.html)

Usage::

    ```python
    from mypy_boto3_opsworks.type_defs import AgentVersionTypeDef

    data: AgentVersionTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_opsworks.literals import (
    AppAttributesKeys,
    AppType,
    Architecture,
    AutoScalingType,
    CloudWatchLogsEncoding,
    CloudWatchLogsInitialPosition,
    CloudWatchLogsTimeZone,
    DeploymentCommandName,
    LayerAttributesKeys,
    LayerType,
    RootDeviceType,
    SourceType,
    VirtualizationType,
    VolumeType,
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
    "AgentVersionTypeDef",
    "AppTypeDef",
    "AutoScalingThresholdsTypeDef",
    "BlockDeviceMappingTypeDef",
    "ChefConfigurationTypeDef",
    "CloneStackResultTypeDef",
    "CloudWatchLogsConfigurationTypeDef",
    "CloudWatchLogsLogStreamTypeDef",
    "CommandTypeDef",
    "CreateAppResultTypeDef",
    "CreateDeploymentResultTypeDef",
    "CreateInstanceResultTypeDef",
    "CreateLayerResultTypeDef",
    "CreateStackResultTypeDef",
    "CreateUserProfileResultTypeDef",
    "DataSourceTypeDef",
    "DeploymentCommandTypeDef",
    "DeploymentTypeDef",
    "DescribeAgentVersionsResultTypeDef",
    "DescribeAppsResultTypeDef",
    "DescribeCommandsResultTypeDef",
    "DescribeDeploymentsResultTypeDef",
    "DescribeEcsClustersResultTypeDef",
    "DescribeElasticIpsResultTypeDef",
    "DescribeElasticLoadBalancersResultTypeDef",
    "DescribeInstancesResultTypeDef",
    "DescribeLayersResultTypeDef",
    "DescribeLoadBasedAutoScalingResultTypeDef",
    "DescribeMyUserProfileResultTypeDef",
    "DescribeOperatingSystemsResponseTypeDef",
    "DescribePermissionsResultTypeDef",
    "DescribeRaidArraysResultTypeDef",
    "DescribeRdsDbInstancesResultTypeDef",
    "DescribeServiceErrorsResultTypeDef",
    "DescribeStackProvisioningParametersResultTypeDef",
    "DescribeStackSummaryResultTypeDef",
    "DescribeStacksResultTypeDef",
    "DescribeTimeBasedAutoScalingResultTypeDef",
    "DescribeUserProfilesResultTypeDef",
    "DescribeVolumesResultTypeDef",
    "EbsBlockDeviceTypeDef",
    "EcsClusterTypeDef",
    "ElasticIpTypeDef",
    "ElasticLoadBalancerTypeDef",
    "EnvironmentVariableTypeDef",
    "GetHostnameSuggestionResultTypeDef",
    "GrantAccessResultTypeDef",
    "InstanceIdentityTypeDef",
    "InstanceTypeDef",
    "InstancesCountTypeDef",
    "LayerTypeDef",
    "LifecycleEventConfigurationTypeDef",
    "ListTagsResultTypeDef",
    "LoadBasedAutoScalingConfigurationTypeDef",
    "OperatingSystemConfigurationManagerTypeDef",
    "OperatingSystemTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "RaidArrayTypeDef",
    "RdsDbInstanceTypeDef",
    "RecipesTypeDef",
    "RegisterEcsClusterResultTypeDef",
    "RegisterElasticIpResultTypeDef",
    "RegisterInstanceResultTypeDef",
    "RegisterVolumeResultTypeDef",
    "ReportedOsTypeDef",
    "SelfUserProfileTypeDef",
    "ServiceErrorTypeDef",
    "ShutdownEventConfigurationTypeDef",
    "SourceTypeDef",
    "SslConfigurationTypeDef",
    "StackConfigurationManagerTypeDef",
    "StackSummaryTypeDef",
    "StackTypeDef",
    "TemporaryCredentialTypeDef",
    "TimeBasedAutoScalingConfigurationTypeDef",
    "UserProfileTypeDef",
    "VolumeConfigurationTypeDef",
    "VolumeTypeDef",
    "WaiterConfigTypeDef",
    "WeeklyAutoScalingScheduleTypeDef",
)


class AgentVersionTypeDef(TypedDict, total=False):
    Version: str
    ConfigurationManager: "StackConfigurationManagerTypeDef"


AppTypeDef = TypedDict(
    "AppTypeDef",
    {
        "AppId": str,
        "StackId": str,
        "Shortname": str,
        "Name": str,
        "Description": str,
        "DataSources": List["DataSourceTypeDef"],
        "Type": AppType,
        "AppSource": "SourceTypeDef",
        "Domains": List[str],
        "EnableSsl": bool,
        "SslConfiguration": "SslConfigurationTypeDef",
        "Attributes": Dict[AppAttributesKeys, str],
        "CreatedAt": str,
        "Environment": List["EnvironmentVariableTypeDef"],
    },
    total=False,
)


class AutoScalingThresholdsTypeDef(TypedDict, total=False):
    InstanceCount: int
    ThresholdsWaitTime: int
    IgnoreMetricsTime: int
    CpuThreshold: float
    MemoryThreshold: float
    LoadThreshold: float
    Alarms: List[str]


class BlockDeviceMappingTypeDef(TypedDict, total=False):
    DeviceName: str
    NoDevice: str
    VirtualName: str
    Ebs: "EbsBlockDeviceTypeDef"


class ChefConfigurationTypeDef(TypedDict, total=False):
    ManageBerkshelf: bool
    BerkshelfVersion: str


class CloneStackResultTypeDef(TypedDict, total=False):
    StackId: str


class CloudWatchLogsConfigurationTypeDef(TypedDict, total=False):
    Enabled: bool
    LogStreams: List["CloudWatchLogsLogStreamTypeDef"]


class CloudWatchLogsLogStreamTypeDef(TypedDict, total=False):
    LogGroupName: str
    DatetimeFormat: str
    TimeZone: CloudWatchLogsTimeZone
    File: str
    FileFingerprintLines: str
    MultiLineStartPattern: str
    InitialPosition: CloudWatchLogsInitialPosition
    Encoding: CloudWatchLogsEncoding
    BufferDuration: int
    BatchCount: int
    BatchSize: int


CommandTypeDef = TypedDict(
    "CommandTypeDef",
    {
        "CommandId": str,
        "InstanceId": str,
        "DeploymentId": str,
        "CreatedAt": str,
        "AcknowledgedAt": str,
        "CompletedAt": str,
        "Status": str,
        "ExitCode": int,
        "LogUrl": str,
        "Type": str,
    },
    total=False,
)


class CreateAppResultTypeDef(TypedDict, total=False):
    AppId: str


class CreateDeploymentResultTypeDef(TypedDict, total=False):
    DeploymentId: str


class CreateInstanceResultTypeDef(TypedDict, total=False):
    InstanceId: str


class CreateLayerResultTypeDef(TypedDict, total=False):
    LayerId: str


class CreateStackResultTypeDef(TypedDict, total=False):
    StackId: str


class CreateUserProfileResultTypeDef(TypedDict, total=False):
    IamUserArn: str


DataSourceTypeDef = TypedDict(
    "DataSourceTypeDef", {"Type": str, "Arn": str, "DatabaseName": str}, total=False
)


class _RequiredDeploymentCommandTypeDef(TypedDict):
    Name: DeploymentCommandName


class DeploymentCommandTypeDef(_RequiredDeploymentCommandTypeDef, total=False):
    Args: Dict[str, List[str]]


class DeploymentTypeDef(TypedDict, total=False):
    DeploymentId: str
    StackId: str
    AppId: str
    CreatedAt: str
    CompletedAt: str
    Duration: int
    IamUserArn: str
    Comment: str
    Command: "DeploymentCommandTypeDef"
    Status: str
    CustomJson: str
    InstanceIds: List[str]


class DescribeAgentVersionsResultTypeDef(TypedDict, total=False):
    AgentVersions: List["AgentVersionTypeDef"]


class DescribeAppsResultTypeDef(TypedDict, total=False):
    Apps: List["AppTypeDef"]


class DescribeCommandsResultTypeDef(TypedDict, total=False):
    Commands: List["CommandTypeDef"]


class DescribeDeploymentsResultTypeDef(TypedDict, total=False):
    Deployments: List["DeploymentTypeDef"]


class DescribeEcsClustersResultTypeDef(TypedDict, total=False):
    EcsClusters: List["EcsClusterTypeDef"]
    NextToken: str


class DescribeElasticIpsResultTypeDef(TypedDict, total=False):
    ElasticIps: List["ElasticIpTypeDef"]


class DescribeElasticLoadBalancersResultTypeDef(TypedDict, total=False):
    ElasticLoadBalancers: List["ElasticLoadBalancerTypeDef"]


class DescribeInstancesResultTypeDef(TypedDict, total=False):
    Instances: List["InstanceTypeDef"]


class DescribeLayersResultTypeDef(TypedDict, total=False):
    Layers: List["LayerTypeDef"]


class DescribeLoadBasedAutoScalingResultTypeDef(TypedDict, total=False):
    LoadBasedAutoScalingConfigurations: List["LoadBasedAutoScalingConfigurationTypeDef"]


class DescribeMyUserProfileResultTypeDef(TypedDict, total=False):
    UserProfile: "SelfUserProfileTypeDef"


class DescribeOperatingSystemsResponseTypeDef(TypedDict, total=False):
    OperatingSystems: List["OperatingSystemTypeDef"]


class DescribePermissionsResultTypeDef(TypedDict, total=False):
    Permissions: List["PermissionTypeDef"]


class DescribeRaidArraysResultTypeDef(TypedDict, total=False):
    RaidArrays: List["RaidArrayTypeDef"]


class DescribeRdsDbInstancesResultTypeDef(TypedDict, total=False):
    RdsDbInstances: List["RdsDbInstanceTypeDef"]


class DescribeServiceErrorsResultTypeDef(TypedDict, total=False):
    ServiceErrors: List["ServiceErrorTypeDef"]


class DescribeStackProvisioningParametersResultTypeDef(TypedDict, total=False):
    AgentInstallerUrl: str
    Parameters: Dict[str, str]


class DescribeStackSummaryResultTypeDef(TypedDict, total=False):
    StackSummary: "StackSummaryTypeDef"


class DescribeStacksResultTypeDef(TypedDict, total=False):
    Stacks: List["StackTypeDef"]


class DescribeTimeBasedAutoScalingResultTypeDef(TypedDict, total=False):
    TimeBasedAutoScalingConfigurations: List["TimeBasedAutoScalingConfigurationTypeDef"]


class DescribeUserProfilesResultTypeDef(TypedDict, total=False):
    UserProfiles: List["UserProfileTypeDef"]


class DescribeVolumesResultTypeDef(TypedDict, total=False):
    Volumes: List["VolumeTypeDef"]


class EbsBlockDeviceTypeDef(TypedDict, total=False):
    SnapshotId: str
    Iops: int
    VolumeSize: int
    VolumeType: VolumeType
    DeleteOnTermination: bool


class EcsClusterTypeDef(TypedDict, total=False):
    EcsClusterArn: str
    EcsClusterName: str
    StackId: str
    RegisteredAt: str


class ElasticIpTypeDef(TypedDict, total=False):
    Ip: str
    Name: str
    Domain: str
    Region: str
    InstanceId: str


class ElasticLoadBalancerTypeDef(TypedDict, total=False):
    ElasticLoadBalancerName: str
    Region: str
    DnsName: str
    StackId: str
    LayerId: str
    VpcId: str
    AvailabilityZones: List[str]
    SubnetIds: List[str]
    Ec2InstanceIds: List[str]


class _RequiredEnvironmentVariableTypeDef(TypedDict):
    Key: str
    Value: str


class EnvironmentVariableTypeDef(_RequiredEnvironmentVariableTypeDef, total=False):
    Secure: bool


class GetHostnameSuggestionResultTypeDef(TypedDict, total=False):
    LayerId: str
    Hostname: str


class GrantAccessResultTypeDef(TypedDict, total=False):
    TemporaryCredential: "TemporaryCredentialTypeDef"


class InstanceIdentityTypeDef(TypedDict, total=False):
    Document: str
    Signature: str


class InstanceTypeDef(TypedDict, total=False):
    AgentVersion: str
    AmiId: str
    Architecture: Architecture
    Arn: str
    AutoScalingType: AutoScalingType
    AvailabilityZone: str
    BlockDeviceMappings: List["BlockDeviceMappingTypeDef"]
    CreatedAt: str
    EbsOptimized: bool
    Ec2InstanceId: str
    EcsClusterArn: str
    EcsContainerInstanceArn: str
    ElasticIp: str
    Hostname: str
    InfrastructureClass: str
    InstallUpdatesOnBoot: bool
    InstanceId: str
    InstanceProfileArn: str
    InstanceType: str
    LastServiceErrorId: str
    LayerIds: List[str]
    Os: str
    Platform: str
    PrivateDns: str
    PrivateIp: str
    PublicDns: str
    PublicIp: str
    RegisteredBy: str
    ReportedAgentVersion: str
    ReportedOs: "ReportedOsTypeDef"
    RootDeviceType: RootDeviceType
    RootDeviceVolumeId: str
    SecurityGroupIds: List[str]
    SshHostDsaKeyFingerprint: str
    SshHostRsaKeyFingerprint: str
    SshKeyName: str
    StackId: str
    Status: str
    SubnetId: str
    Tenancy: str
    VirtualizationType: VirtualizationType


class InstancesCountTypeDef(TypedDict, total=False):
    Assigning: int
    Booting: int
    ConnectionLost: int
    Deregistering: int
    Online: int
    Pending: int
    Rebooting: int
    Registered: int
    Registering: int
    Requested: int
    RunningSetup: int
    SetupFailed: int
    ShuttingDown: int
    StartFailed: int
    StopFailed: int
    Stopped: int
    Stopping: int
    Terminated: int
    Terminating: int
    Unassigning: int


LayerTypeDef = TypedDict(
    "LayerTypeDef",
    {
        "Arn": str,
        "StackId": str,
        "LayerId": str,
        "Type": LayerType,
        "Name": str,
        "Shortname": str,
        "Attributes": Dict[LayerAttributesKeys, str],
        "CloudWatchLogsConfiguration": "CloudWatchLogsConfigurationTypeDef",
        "CustomInstanceProfileArn": str,
        "CustomJson": str,
        "CustomSecurityGroupIds": List[str],
        "DefaultSecurityGroupNames": List[str],
        "Packages": List[str],
        "VolumeConfigurations": List["VolumeConfigurationTypeDef"],
        "EnableAutoHealing": bool,
        "AutoAssignElasticIps": bool,
        "AutoAssignPublicIps": bool,
        "DefaultRecipes": "RecipesTypeDef",
        "CustomRecipes": "RecipesTypeDef",
        "CreatedAt": str,
        "InstallUpdatesOnBoot": bool,
        "UseEbsOptimizedInstances": bool,
        "LifecycleEventConfiguration": "LifecycleEventConfigurationTypeDef",
    },
    total=False,
)


class LifecycleEventConfigurationTypeDef(TypedDict, total=False):
    Shutdown: "ShutdownEventConfigurationTypeDef"


class ListTagsResultTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]
    NextToken: str


class LoadBasedAutoScalingConfigurationTypeDef(TypedDict, total=False):
    LayerId: str
    Enable: bool
    UpScaling: "AutoScalingThresholdsTypeDef"
    DownScaling: "AutoScalingThresholdsTypeDef"


class OperatingSystemConfigurationManagerTypeDef(TypedDict, total=False):
    Name: str
    Version: str


OperatingSystemTypeDef = TypedDict(
    "OperatingSystemTypeDef",
    {
        "Name": str,
        "Id": str,
        "Type": str,
        "ConfigurationManagers": List["OperatingSystemConfigurationManagerTypeDef"],
        "ReportedName": str,
        "ReportedVersion": str,
        "Supported": bool,
    },
    total=False,
)


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PermissionTypeDef(TypedDict, total=False):
    StackId: str
    IamUserArn: str
    AllowSsh: bool
    AllowSudo: bool
    Level: str


class RaidArrayTypeDef(TypedDict, total=False):
    RaidArrayId: str
    InstanceId: str
    Name: str
    RaidLevel: int
    NumberOfDisks: int
    Size: int
    Device: str
    MountPoint: str
    AvailabilityZone: str
    CreatedAt: str
    StackId: str
    VolumeType: str
    Iops: int


class RdsDbInstanceTypeDef(TypedDict, total=False):
    RdsDbInstanceArn: str
    DbInstanceIdentifier: str
    DbUser: str
    DbPassword: str
    Region: str
    Address: str
    Engine: str
    StackId: str
    MissingOnRds: bool


class RecipesTypeDef(TypedDict, total=False):
    Setup: List[str]
    Configure: List[str]
    Deploy: List[str]
    Undeploy: List[str]
    Shutdown: List[str]


class RegisterEcsClusterResultTypeDef(TypedDict, total=False):
    EcsClusterArn: str


class RegisterElasticIpResultTypeDef(TypedDict, total=False):
    ElasticIp: str


class RegisterInstanceResultTypeDef(TypedDict, total=False):
    InstanceId: str


class RegisterVolumeResultTypeDef(TypedDict, total=False):
    VolumeId: str


class ReportedOsTypeDef(TypedDict, total=False):
    Family: str
    Name: str
    Version: str


class SelfUserProfileTypeDef(TypedDict, total=False):
    IamUserArn: str
    Name: str
    SshUsername: str
    SshPublicKey: str


ServiceErrorTypeDef = TypedDict(
    "ServiceErrorTypeDef",
    {
        "ServiceErrorId": str,
        "StackId": str,
        "InstanceId": str,
        "Type": str,
        "Message": str,
        "CreatedAt": str,
    },
    total=False,
)


class ShutdownEventConfigurationTypeDef(TypedDict, total=False):
    ExecutionTimeout: int
    DelayUntilElbConnectionsDrained: bool


SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "Type": SourceType,
        "Url": str,
        "Username": str,
        "Password": str,
        "SshKey": str,
        "Revision": str,
    },
    total=False,
)


class _RequiredSslConfigurationTypeDef(TypedDict):
    Certificate: str
    PrivateKey: str


class SslConfigurationTypeDef(_RequiredSslConfigurationTypeDef, total=False):
    Chain: str


class StackConfigurationManagerTypeDef(TypedDict, total=False):
    Name: str
    Version: str


class StackSummaryTypeDef(TypedDict, total=False):
    StackId: str
    Name: str
    Arn: str
    LayersCount: int
    AppsCount: int
    InstancesCount: "InstancesCountTypeDef"


class StackTypeDef(TypedDict, total=False):
    StackId: str
    Name: str
    Arn: str
    Region: str
    VpcId: str
    Attributes: Dict[Literal["Color"], str]
    ServiceRoleArn: str
    DefaultInstanceProfileArn: str
    DefaultOs: str
    HostnameTheme: str
    DefaultAvailabilityZone: str
    DefaultSubnetId: str
    CustomJson: str
    ConfigurationManager: "StackConfigurationManagerTypeDef"
    ChefConfiguration: "ChefConfigurationTypeDef"
    UseCustomCookbooks: bool
    UseOpsworksSecurityGroups: bool
    CustomCookbooksSource: "SourceTypeDef"
    DefaultSshKeyName: str
    CreatedAt: str
    DefaultRootDeviceType: RootDeviceType
    AgentVersion: str


class TemporaryCredentialTypeDef(TypedDict, total=False):
    Username: str
    Password: str
    ValidForInMinutes: int
    InstanceId: str


class TimeBasedAutoScalingConfigurationTypeDef(TypedDict, total=False):
    InstanceId: str
    AutoScalingSchedule: "WeeklyAutoScalingScheduleTypeDef"


class UserProfileTypeDef(TypedDict, total=False):
    IamUserArn: str
    Name: str
    SshUsername: str
    SshPublicKey: str
    AllowSelfManagement: bool


class _RequiredVolumeConfigurationTypeDef(TypedDict):
    MountPoint: str
    NumberOfDisks: int
    Size: int


class VolumeConfigurationTypeDef(_RequiredVolumeConfigurationTypeDef, total=False):
    RaidLevel: int
    VolumeType: str
    Iops: int
    Encrypted: bool


class VolumeTypeDef(TypedDict, total=False):
    VolumeId: str
    Ec2VolumeId: str
    Name: str
    RaidArrayId: str
    InstanceId: str
    Status: str
    Size: int
    Device: str
    MountPoint: str
    Region: str
    AvailabilityZone: str
    VolumeType: str
    Iops: int
    Encrypted: bool


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int


class WeeklyAutoScalingScheduleTypeDef(TypedDict, total=False):
    Monday: Dict[str, str]
    Tuesday: Dict[str, str]
    Wednesday: Dict[str, str]
    Thursday: Dict[str, str]
    Friday: Dict[str, str]
    Saturday: Dict[str, str]
    Sunday: Dict[str, str]
