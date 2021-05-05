"""
Type annotations for opsworks service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_opsworks import OpsWorksClient

    client: OpsWorksClient = boto3.client("opsworks")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_opsworks.literals import (
    AppAttributesKeys,
    AppType,
    Architecture,
    AutoScalingType,
    LayerAttributesKeys,
    LayerType,
    RootDeviceType,
)
from mypy_boto3_opsworks.paginator import DescribeEcsClustersPaginator
from mypy_boto3_opsworks.type_defs import (
    AutoScalingThresholdsTypeDef,
    BlockDeviceMappingTypeDef,
    ChefConfigurationTypeDef,
    CloneStackResultTypeDef,
    CloudWatchLogsConfigurationTypeDef,
    CreateAppResultTypeDef,
    CreateDeploymentResultTypeDef,
    CreateInstanceResultTypeDef,
    CreateLayerResultTypeDef,
    CreateStackResultTypeDef,
    CreateUserProfileResultTypeDef,
    DataSourceTypeDef,
    DeploymentCommandTypeDef,
    DescribeAgentVersionsResultTypeDef,
    DescribeAppsResultTypeDef,
    DescribeCommandsResultTypeDef,
    DescribeDeploymentsResultTypeDef,
    DescribeEcsClustersResultTypeDef,
    DescribeElasticIpsResultTypeDef,
    DescribeElasticLoadBalancersResultTypeDef,
    DescribeInstancesResultTypeDef,
    DescribeLayersResultTypeDef,
    DescribeLoadBasedAutoScalingResultTypeDef,
    DescribeMyUserProfileResultTypeDef,
    DescribeOperatingSystemsResponseTypeDef,
    DescribePermissionsResultTypeDef,
    DescribeRaidArraysResultTypeDef,
    DescribeRdsDbInstancesResultTypeDef,
    DescribeServiceErrorsResultTypeDef,
    DescribeStackProvisioningParametersResultTypeDef,
    DescribeStacksResultTypeDef,
    DescribeStackSummaryResultTypeDef,
    DescribeTimeBasedAutoScalingResultTypeDef,
    DescribeUserProfilesResultTypeDef,
    DescribeVolumesResultTypeDef,
    EnvironmentVariableTypeDef,
    GetHostnameSuggestionResultTypeDef,
    GrantAccessResultTypeDef,
    InstanceIdentityTypeDef,
    LifecycleEventConfigurationTypeDef,
    ListTagsResultTypeDef,
    RecipesTypeDef,
    RegisterEcsClusterResultTypeDef,
    RegisterElasticIpResultTypeDef,
    RegisterInstanceResultTypeDef,
    RegisterVolumeResultTypeDef,
    SourceTypeDef,
    SslConfigurationTypeDef,
    StackConfigurationManagerTypeDef,
    VolumeConfigurationTypeDef,
    WeeklyAutoScalingScheduleTypeDef,
)
from mypy_boto3_opsworks.waiter import (
    AppExistsWaiter,
    DeploymentSuccessfulWaiter,
    InstanceOnlineWaiter,
    InstanceRegisteredWaiter,
    InstanceStoppedWaiter,
    InstanceTerminatedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("OpsWorksClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class OpsWorksClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def assign_instance(self, InstanceId: str, LayerIds: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.assign_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#assign-instance)
        """

    def assign_volume(self, VolumeId: str, InstanceId: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.assign_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#assign-volume)
        """

    def associate_elastic_ip(self, ElasticIp: str, InstanceId: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.associate_elastic_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#associate-elastic-ip)
        """

    def attach_elastic_load_balancer(self, ElasticLoadBalancerName: str, LayerId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.attach_elastic_load_balancer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#attach-elastic-load-balancer)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#can-paginate)
        """

    def clone_stack(
        self,
        SourceStackId: str,
        ServiceRoleArn: str,
        Name: str = None,
        Region: str = None,
        VpcId: str = None,
        Attributes: Dict[Literal["Color"], str] = None,
        DefaultInstanceProfileArn: str = None,
        DefaultOs: str = None,
        HostnameTheme: str = None,
        DefaultAvailabilityZone: str = None,
        DefaultSubnetId: str = None,
        CustomJson: str = None,
        ConfigurationManager: "StackConfigurationManagerTypeDef" = None,
        ChefConfiguration: "ChefConfigurationTypeDef" = None,
        UseCustomCookbooks: bool = None,
        UseOpsworksSecurityGroups: bool = None,
        CustomCookbooksSource: "SourceTypeDef" = None,
        DefaultSshKeyName: str = None,
        ClonePermissions: bool = None,
        CloneAppIds: List[str] = None,
        DefaultRootDeviceType: RootDeviceType = None,
        AgentVersion: str = None,
    ) -> CloneStackResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.clone_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#clone-stack)
        """

    def create_app(
        self,
        StackId: str,
        Name: str,
        Type: AppType,
        Shortname: str = None,
        Description: str = None,
        DataSources: List["DataSourceTypeDef"] = None,
        AppSource: "SourceTypeDef" = None,
        Domains: List[str] = None,
        EnableSsl: bool = None,
        SslConfiguration: "SslConfigurationTypeDef" = None,
        Attributes: Dict[AppAttributesKeys, str] = None,
        Environment: List["EnvironmentVariableTypeDef"] = None,
    ) -> CreateAppResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.create_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#create-app)
        """

    def create_deployment(
        self,
        StackId: str,
        Command: "DeploymentCommandTypeDef",
        AppId: str = None,
        InstanceIds: List[str] = None,
        LayerIds: List[str] = None,
        Comment: str = None,
        CustomJson: str = None,
    ) -> CreateDeploymentResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.create_deployment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#create-deployment)
        """

    def create_instance(
        self,
        StackId: str,
        LayerIds: List[str],
        InstanceType: str,
        AutoScalingType: AutoScalingType = None,
        Hostname: str = None,
        Os: str = None,
        AmiId: str = None,
        SshKeyName: str = None,
        AvailabilityZone: str = None,
        VirtualizationType: str = None,
        SubnetId: str = None,
        Architecture: Architecture = None,
        RootDeviceType: RootDeviceType = None,
        BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
        InstallUpdatesOnBoot: bool = None,
        EbsOptimized: bool = None,
        AgentVersion: str = None,
        Tenancy: str = None,
    ) -> CreateInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.create_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#create-instance)
        """

    def create_layer(
        self,
        StackId: str,
        Type: LayerType,
        Name: str,
        Shortname: str,
        Attributes: Dict[LayerAttributesKeys, str] = None,
        CloudWatchLogsConfiguration: "CloudWatchLogsConfigurationTypeDef" = None,
        CustomInstanceProfileArn: str = None,
        CustomJson: str = None,
        CustomSecurityGroupIds: List[str] = None,
        Packages: List[str] = None,
        VolumeConfigurations: List["VolumeConfigurationTypeDef"] = None,
        EnableAutoHealing: bool = None,
        AutoAssignElasticIps: bool = None,
        AutoAssignPublicIps: bool = None,
        CustomRecipes: "RecipesTypeDef" = None,
        InstallUpdatesOnBoot: bool = None,
        UseEbsOptimizedInstances: bool = None,
        LifecycleEventConfiguration: "LifecycleEventConfigurationTypeDef" = None,
    ) -> CreateLayerResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.create_layer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#create-layer)
        """

    def create_stack(
        self,
        Name: str,
        Region: str,
        ServiceRoleArn: str,
        DefaultInstanceProfileArn: str,
        VpcId: str = None,
        Attributes: Dict[Literal["Color"], str] = None,
        DefaultOs: str = None,
        HostnameTheme: str = None,
        DefaultAvailabilityZone: str = None,
        DefaultSubnetId: str = None,
        CustomJson: str = None,
        ConfigurationManager: "StackConfigurationManagerTypeDef" = None,
        ChefConfiguration: "ChefConfigurationTypeDef" = None,
        UseCustomCookbooks: bool = None,
        UseOpsworksSecurityGroups: bool = None,
        CustomCookbooksSource: "SourceTypeDef" = None,
        DefaultSshKeyName: str = None,
        DefaultRootDeviceType: RootDeviceType = None,
        AgentVersion: str = None,
    ) -> CreateStackResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.create_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#create-stack)
        """

    def create_user_profile(
        self,
        IamUserArn: str,
        SshUsername: str = None,
        SshPublicKey: str = None,
        AllowSelfManagement: bool = None,
    ) -> CreateUserProfileResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.create_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#create-user-profile)
        """

    def delete_app(self, AppId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.delete_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#delete-app)
        """

    def delete_instance(
        self, InstanceId: str, DeleteElasticIp: bool = None, DeleteVolumes: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.delete_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#delete-instance)
        """

    def delete_layer(self, LayerId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.delete_layer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#delete-layer)
        """

    def delete_stack(self, StackId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.delete_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#delete-stack)
        """

    def delete_user_profile(self, IamUserArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.delete_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#delete-user-profile)
        """

    def deregister_ecs_cluster(self, EcsClusterArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.deregister_ecs_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#deregister-ecs-cluster)
        """

    def deregister_elastic_ip(self, ElasticIp: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.deregister_elastic_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#deregister-elastic-ip)
        """

    def deregister_instance(self, InstanceId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.deregister_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#deregister-instance)
        """

    def deregister_rds_db_instance(self, RdsDbInstanceArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.deregister_rds_db_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#deregister-rds-db-instance)
        """

    def deregister_volume(self, VolumeId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.deregister_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#deregister-volume)
        """

    def describe_agent_versions(
        self, StackId: str = None, ConfigurationManager: "StackConfigurationManagerTypeDef" = None
    ) -> DescribeAgentVersionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_agent_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-agent-versions)
        """

    def describe_apps(
        self, StackId: str = None, AppIds: List[str] = None
    ) -> DescribeAppsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_apps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-apps)
        """

    def describe_commands(
        self, DeploymentId: str = None, InstanceId: str = None, CommandIds: List[str] = None
    ) -> DescribeCommandsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_commands)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-commands)
        """

    def describe_deployments(
        self, StackId: str = None, AppId: str = None, DeploymentIds: List[str] = None
    ) -> DescribeDeploymentsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_deployments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-deployments)
        """

    def describe_ecs_clusters(
        self,
        EcsClusterArns: List[str] = None,
        StackId: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeEcsClustersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_ecs_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-ecs-clusters)
        """

    def describe_elastic_ips(
        self, InstanceId: str = None, StackId: str = None, Ips: List[str] = None
    ) -> DescribeElasticIpsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_elastic_ips)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-elastic-ips)
        """

    def describe_elastic_load_balancers(
        self, StackId: str = None, LayerIds: List[str] = None
    ) -> DescribeElasticLoadBalancersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_elastic_load_balancers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-elastic-load-balancers)
        """

    def describe_instances(
        self, StackId: str = None, LayerId: str = None, InstanceIds: List[str] = None
    ) -> DescribeInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-instances)
        """

    def describe_layers(
        self, StackId: str = None, LayerIds: List[str] = None
    ) -> DescribeLayersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_layers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-layers)
        """

    def describe_load_based_auto_scaling(
        self, LayerIds: List[str]
    ) -> DescribeLoadBasedAutoScalingResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_load_based_auto_scaling)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-load-based-auto-scaling)
        """

    def describe_my_user_profile(self) -> DescribeMyUserProfileResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_my_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-my-user-profile)
        """

    def describe_operating_systems(self) -> DescribeOperatingSystemsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_operating_systems)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-operating-systems)
        """

    def describe_permissions(
        self, IamUserArn: str = None, StackId: str = None
    ) -> DescribePermissionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-permissions)
        """

    def describe_raid_arrays(
        self, InstanceId: str = None, StackId: str = None, RaidArrayIds: List[str] = None
    ) -> DescribeRaidArraysResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_raid_arrays)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-raid-arrays)
        """

    def describe_rds_db_instances(
        self, StackId: str, RdsDbInstanceArns: List[str] = None
    ) -> DescribeRdsDbInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_rds_db_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-rds-db-instances)
        """

    def describe_service_errors(
        self, StackId: str = None, InstanceId: str = None, ServiceErrorIds: List[str] = None
    ) -> DescribeServiceErrorsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_service_errors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-service-errors)
        """

    def describe_stack_provisioning_parameters(
        self, StackId: str
    ) -> DescribeStackProvisioningParametersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_stack_provisioning_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-stack-provisioning-parameters)
        """

    def describe_stack_summary(self, StackId: str) -> DescribeStackSummaryResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_stack_summary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-stack-summary)
        """

    def describe_stacks(self, StackIds: List[str] = None) -> DescribeStacksResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_stacks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-stacks)
        """

    def describe_time_based_auto_scaling(
        self, InstanceIds: List[str]
    ) -> DescribeTimeBasedAutoScalingResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_time_based_auto_scaling)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-time-based-auto-scaling)
        """

    def describe_user_profiles(
        self, IamUserArns: List[str] = None
    ) -> DescribeUserProfilesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_user_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-user-profiles)
        """

    def describe_volumes(
        self,
        InstanceId: str = None,
        StackId: str = None,
        RaidArrayId: str = None,
        VolumeIds: List[str] = None,
    ) -> DescribeVolumesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.describe_volumes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#describe-volumes)
        """

    def detach_elastic_load_balancer(self, ElasticLoadBalancerName: str, LayerId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.detach_elastic_load_balancer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#detach-elastic-load-balancer)
        """

    def disassociate_elastic_ip(self, ElasticIp: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.disassociate_elastic_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#disassociate-elastic-ip)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#generate-presigned-url)
        """

    def get_hostname_suggestion(self, LayerId: str) -> GetHostnameSuggestionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.get_hostname_suggestion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#get-hostname-suggestion)
        """

    def grant_access(
        self, InstanceId: str, ValidForInMinutes: int = None
    ) -> GrantAccessResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.grant_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#grant-access)
        """

    def list_tags(
        self, ResourceArn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#list-tags)
        """

    def reboot_instance(self, InstanceId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.reboot_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#reboot-instance)
        """

    def register_ecs_cluster(
        self, EcsClusterArn: str, StackId: str
    ) -> RegisterEcsClusterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.register_ecs_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#register-ecs-cluster)
        """

    def register_elastic_ip(self, ElasticIp: str, StackId: str) -> RegisterElasticIpResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.register_elastic_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#register-elastic-ip)
        """

    def register_instance(
        self,
        StackId: str,
        Hostname: str = None,
        PublicIp: str = None,
        PrivateIp: str = None,
        RsaPublicKey: str = None,
        RsaPublicKeyFingerprint: str = None,
        InstanceIdentity: InstanceIdentityTypeDef = None,
    ) -> RegisterInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.register_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#register-instance)
        """

    def register_rds_db_instance(
        self, StackId: str, RdsDbInstanceArn: str, DbUser: str, DbPassword: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.register_rds_db_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#register-rds-db-instance)
        """

    def register_volume(self, StackId: str, Ec2VolumeId: str = None) -> RegisterVolumeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.register_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#register-volume)
        """

    def set_load_based_auto_scaling(
        self,
        LayerId: str,
        Enable: bool = None,
        UpScaling: "AutoScalingThresholdsTypeDef" = None,
        DownScaling: "AutoScalingThresholdsTypeDef" = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.set_load_based_auto_scaling)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#set-load-based-auto-scaling)
        """

    def set_permission(
        self,
        StackId: str,
        IamUserArn: str,
        AllowSsh: bool = None,
        AllowSudo: bool = None,
        Level: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.set_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#set-permission)
        """

    def set_time_based_auto_scaling(
        self, InstanceId: str, AutoScalingSchedule: "WeeklyAutoScalingScheduleTypeDef" = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.set_time_based_auto_scaling)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#set-time-based-auto-scaling)
        """

    def start_instance(self, InstanceId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.start_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#start-instance)
        """

    def start_stack(self, StackId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.start_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#start-stack)
        """

    def stop_instance(self, InstanceId: str, Force: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.stop_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#stop-instance)
        """

    def stop_stack(self, StackId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.stop_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#stop-stack)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#tag-resource)
        """

    def unassign_instance(self, InstanceId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.unassign_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#unassign-instance)
        """

    def unassign_volume(self, VolumeId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.unassign_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#unassign-volume)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#untag-resource)
        """

    def update_app(
        self,
        AppId: str,
        Name: str = None,
        Description: str = None,
        DataSources: List["DataSourceTypeDef"] = None,
        Type: AppType = None,
        AppSource: "SourceTypeDef" = None,
        Domains: List[str] = None,
        EnableSsl: bool = None,
        SslConfiguration: "SslConfigurationTypeDef" = None,
        Attributes: Dict[AppAttributesKeys, str] = None,
        Environment: List["EnvironmentVariableTypeDef"] = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.update_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#update-app)
        """

    def update_elastic_ip(self, ElasticIp: str, Name: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.update_elastic_ip)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#update-elastic-ip)
        """

    def update_instance(
        self,
        InstanceId: str,
        LayerIds: List[str] = None,
        InstanceType: str = None,
        AutoScalingType: AutoScalingType = None,
        Hostname: str = None,
        Os: str = None,
        AmiId: str = None,
        SshKeyName: str = None,
        Architecture: Architecture = None,
        InstallUpdatesOnBoot: bool = None,
        EbsOptimized: bool = None,
        AgentVersion: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.update_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#update-instance)
        """

    def update_layer(
        self,
        LayerId: str,
        Name: str = None,
        Shortname: str = None,
        Attributes: Dict[LayerAttributesKeys, str] = None,
        CloudWatchLogsConfiguration: "CloudWatchLogsConfigurationTypeDef" = None,
        CustomInstanceProfileArn: str = None,
        CustomJson: str = None,
        CustomSecurityGroupIds: List[str] = None,
        Packages: List[str] = None,
        VolumeConfigurations: List["VolumeConfigurationTypeDef"] = None,
        EnableAutoHealing: bool = None,
        AutoAssignElasticIps: bool = None,
        AutoAssignPublicIps: bool = None,
        CustomRecipes: "RecipesTypeDef" = None,
        InstallUpdatesOnBoot: bool = None,
        UseEbsOptimizedInstances: bool = None,
        LifecycleEventConfiguration: "LifecycleEventConfigurationTypeDef" = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.update_layer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#update-layer)
        """

    def update_my_user_profile(self, SshPublicKey: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.update_my_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#update-my-user-profile)
        """

    def update_rds_db_instance(
        self, RdsDbInstanceArn: str, DbUser: str = None, DbPassword: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.update_rds_db_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#update-rds-db-instance)
        """

    def update_stack(
        self,
        StackId: str,
        Name: str = None,
        Attributes: Dict[Literal["Color"], str] = None,
        ServiceRoleArn: str = None,
        DefaultInstanceProfileArn: str = None,
        DefaultOs: str = None,
        HostnameTheme: str = None,
        DefaultAvailabilityZone: str = None,
        DefaultSubnetId: str = None,
        CustomJson: str = None,
        ConfigurationManager: "StackConfigurationManagerTypeDef" = None,
        ChefConfiguration: "ChefConfigurationTypeDef" = None,
        UseCustomCookbooks: bool = None,
        CustomCookbooksSource: "SourceTypeDef" = None,
        DefaultSshKeyName: str = None,
        DefaultRootDeviceType: RootDeviceType = None,
        UseOpsworksSecurityGroups: bool = None,
        AgentVersion: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.update_stack)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#update-stack)
        """

    def update_user_profile(
        self,
        IamUserArn: str,
        SshUsername: str = None,
        SshPublicKey: str = None,
        AllowSelfManagement: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.update_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#update-user-profile)
        """

    def update_volume(self, VolumeId: str, Name: str = None, MountPoint: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Client.update_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/client.html#update-volume)
        """

    def get_paginator(
        self, operation_name: Literal["describe_ecs_clusters"]
    ) -> DescribeEcsClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Paginator.DescribeEcsClusters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/paginators.html#describeecsclusterspaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["app_exists"]) -> AppExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Waiter.app_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#appexistswaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["deployment_successful"]
    ) -> DeploymentSuccessfulWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Waiter.deployment_successful)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#deploymentsuccessfulwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_online"]) -> InstanceOnlineWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Waiter.instance_online)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#instanceonlinewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_registered"]) -> InstanceRegisteredWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Waiter.instance_registered)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#instanceregisteredwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_stopped"]) -> InstanceStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Waiter.instance_stopped)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#instancestoppedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_terminated"]) -> InstanceTerminatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/opsworks.html#OpsWorks.Waiter.instance_terminated)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_opsworks/waiters.html#instanceterminatedwaiter)
        """
