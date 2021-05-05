"""
Type annotations for ecs service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ecs import ECSClient

    client: ECSClient = boto3.client("ecs")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_ecs.literals import (
    ClusterField,
    Compatibility,
    ContainerInstanceStatus,
    DesiredStatus,
    IpcMode,
    LaunchType,
    NetworkMode,
    PidMode,
    PropagateTags,
    SchedulingStrategy,
    SettingName,
    SortOrder,
    TaskDefinitionFamilyStatus,
    TaskDefinitionStatus,
)
from mypy_boto3_ecs.paginator import (
    ListAccountSettingsPaginator,
    ListAttributesPaginator,
    ListClustersPaginator,
    ListContainerInstancesPaginator,
    ListServicesPaginator,
    ListTaskDefinitionFamiliesPaginator,
    ListTaskDefinitionsPaginator,
    ListTasksPaginator,
)
from mypy_boto3_ecs.type_defs import (
    AttachmentStateChangeTypeDef,
    AttributeTypeDef,
    AutoScalingGroupProviderTypeDef,
    AutoScalingGroupProviderUpdateTypeDef,
    CapacityProviderStrategyItemTypeDef,
    ClusterConfigurationTypeDef,
    ClusterSettingTypeDef,
    ContainerDefinitionTypeDef,
    ContainerStateChangeTypeDef,
    CreateCapacityProviderResponseTypeDef,
    CreateClusterResponseTypeDef,
    CreateServiceResponseTypeDef,
    CreateTaskSetResponseTypeDef,
    DeleteAccountSettingResponseTypeDef,
    DeleteAttributesResponseTypeDef,
    DeleteCapacityProviderResponseTypeDef,
    DeleteClusterResponseTypeDef,
    DeleteServiceResponseTypeDef,
    DeleteTaskSetResponseTypeDef,
    DeploymentConfigurationTypeDef,
    DeploymentControllerTypeDef,
    DeregisterContainerInstanceResponseTypeDef,
    DeregisterTaskDefinitionResponseTypeDef,
    DescribeCapacityProvidersResponseTypeDef,
    DescribeClustersResponseTypeDef,
    DescribeContainerInstancesResponseTypeDef,
    DescribeServicesResponseTypeDef,
    DescribeTaskDefinitionResponseTypeDef,
    DescribeTaskSetsResponseTypeDef,
    DescribeTasksResponseTypeDef,
    DiscoverPollEndpointResponseTypeDef,
    EphemeralStorageTypeDef,
    ExecuteCommandResponseTypeDef,
    InferenceAcceleratorTypeDef,
    ListAccountSettingsResponseTypeDef,
    ListAttributesResponseTypeDef,
    ListClustersResponseTypeDef,
    ListContainerInstancesResponseTypeDef,
    ListServicesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTaskDefinitionFamiliesResponseTypeDef,
    ListTaskDefinitionsResponseTypeDef,
    ListTasksResponseTypeDef,
    LoadBalancerTypeDef,
    ManagedAgentStateChangeTypeDef,
    NetworkBindingTypeDef,
    NetworkConfigurationTypeDef,
    PlacementConstraintTypeDef,
    PlacementStrategyTypeDef,
    PlatformDeviceTypeDef,
    ProxyConfigurationTypeDef,
    PutAccountSettingDefaultResponseTypeDef,
    PutAccountSettingResponseTypeDef,
    PutAttributesResponseTypeDef,
    PutClusterCapacityProvidersResponseTypeDef,
    RegisterContainerInstanceResponseTypeDef,
    RegisterTaskDefinitionResponseTypeDef,
    ResourceTypeDef,
    RunTaskResponseTypeDef,
    ScaleTypeDef,
    ServiceRegistryTypeDef,
    StartTaskResponseTypeDef,
    StopTaskResponseTypeDef,
    SubmitAttachmentStateChangesResponseTypeDef,
    SubmitContainerStateChangeResponseTypeDef,
    SubmitTaskStateChangeResponseTypeDef,
    TagTypeDef,
    TaskDefinitionPlacementConstraintTypeDef,
    TaskOverrideTypeDef,
    UpdateCapacityProviderResponseTypeDef,
    UpdateClusterResponseTypeDef,
    UpdateClusterSettingsResponseTypeDef,
    UpdateContainerAgentResponseTypeDef,
    UpdateContainerInstancesStateResponseTypeDef,
    UpdateServicePrimaryTaskSetResponseTypeDef,
    UpdateServiceResponseTypeDef,
    UpdateTaskSetResponseTypeDef,
    VersionInfoTypeDef,
    VolumeTypeDef,
)
from mypy_boto3_ecs.waiter import (
    ServicesInactiveWaiter,
    ServicesStableWaiter,
    TasksRunningWaiter,
    TasksStoppedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ECSClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    AttributeLimitExceededException: Type[BotocoreClientError]
    BlockedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ClientException: Type[BotocoreClientError]
    ClusterContainsContainerInstancesException: Type[BotocoreClientError]
    ClusterContainsServicesException: Type[BotocoreClientError]
    ClusterContainsTasksException: Type[BotocoreClientError]
    ClusterNotFoundException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MissingVersionException: Type[BotocoreClientError]
    NoUpdateAvailableException: Type[BotocoreClientError]
    PlatformTaskDefinitionIncompatibilityException: Type[BotocoreClientError]
    PlatformUnknownException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServerException: Type[BotocoreClientError]
    ServiceNotActiveException: Type[BotocoreClientError]
    ServiceNotFoundException: Type[BotocoreClientError]
    TargetNotConnectedException: Type[BotocoreClientError]
    TargetNotFoundException: Type[BotocoreClientError]
    TaskSetNotFoundException: Type[BotocoreClientError]
    UnsupportedFeatureException: Type[BotocoreClientError]
    UpdateInProgressException: Type[BotocoreClientError]


class ECSClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#can-paginate)
        """

    def create_capacity_provider(
        self,
        name: str,
        autoScalingGroupProvider: "AutoScalingGroupProviderTypeDef",
        tags: List["TagTypeDef"] = None,
    ) -> CreateCapacityProviderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.create_capacity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#create-capacity-provider)
        """

    def create_cluster(
        self,
        clusterName: str = None,
        tags: List["TagTypeDef"] = None,
        settings: List["ClusterSettingTypeDef"] = None,
        configuration: "ClusterConfigurationTypeDef" = None,
        capacityProviders: List[str] = None,
        defaultCapacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
    ) -> CreateClusterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.create_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#create-cluster)
        """

    def create_service(
        self,
        serviceName: str,
        cluster: str = None,
        taskDefinition: str = None,
        loadBalancers: List["LoadBalancerTypeDef"] = None,
        serviceRegistries: List["ServiceRegistryTypeDef"] = None,
        desiredCount: int = None,
        clientToken: str = None,
        launchType: LaunchType = None,
        capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
        platformVersion: str = None,
        role: str = None,
        deploymentConfiguration: "DeploymentConfigurationTypeDef" = None,
        placementConstraints: List["PlacementConstraintTypeDef"] = None,
        placementStrategy: List["PlacementStrategyTypeDef"] = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None,
        healthCheckGracePeriodSeconds: int = None,
        schedulingStrategy: SchedulingStrategy = None,
        deploymentController: "DeploymentControllerTypeDef" = None,
        tags: List["TagTypeDef"] = None,
        enableECSManagedTags: bool = None,
        propagateTags: PropagateTags = None,
        enableExecuteCommand: bool = None,
    ) -> CreateServiceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.create_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#create-service)
        """

    def create_task_set(
        self,
        service: str,
        cluster: str,
        taskDefinition: str,
        externalId: str = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None,
        loadBalancers: List["LoadBalancerTypeDef"] = None,
        serviceRegistries: List["ServiceRegistryTypeDef"] = None,
        launchType: LaunchType = None,
        capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
        platformVersion: str = None,
        scale: "ScaleTypeDef" = None,
        clientToken: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> CreateTaskSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.create_task_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#create-task-set)
        """

    def delete_account_setting(
        self, name: SettingName, principalArn: str = None
    ) -> DeleteAccountSettingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.delete_account_setting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#delete-account-setting)
        """

    def delete_attributes(
        self, attributes: List["AttributeTypeDef"], cluster: str = None
    ) -> DeleteAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.delete_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#delete-attributes)
        """

    def delete_capacity_provider(
        self, capacityProvider: str
    ) -> DeleteCapacityProviderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.delete_capacity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#delete-capacity-provider)
        """

    def delete_cluster(self, cluster: str) -> DeleteClusterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.delete_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#delete-cluster)
        """

    def delete_service(
        self, service: str, cluster: str = None, force: bool = None
    ) -> DeleteServiceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.delete_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#delete-service)
        """

    def delete_task_set(
        self, cluster: str, service: str, taskSet: str, force: bool = None
    ) -> DeleteTaskSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.delete_task_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#delete-task-set)
        """

    def deregister_container_instance(
        self, containerInstance: str, cluster: str = None, force: bool = None
    ) -> DeregisterContainerInstanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.deregister_container_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#deregister-container-instance)
        """

    def deregister_task_definition(
        self, taskDefinition: str
    ) -> DeregisterTaskDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.deregister_task_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#deregister-task-definition)
        """

    def describe_capacity_providers(
        self,
        capacityProviders: List[str] = None,
        include: List[Literal["TAGS"]] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> DescribeCapacityProvidersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.describe_capacity_providers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#describe-capacity-providers)
        """

    def describe_clusters(
        self, clusters: List[str] = None, include: List[ClusterField] = None
    ) -> DescribeClustersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.describe_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#describe-clusters)
        """

    def describe_container_instances(
        self,
        containerInstances: List[str],
        cluster: str = None,
        include: List[Literal["TAGS"]] = None,
    ) -> DescribeContainerInstancesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.describe_container_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#describe-container-instances)
        """

    def describe_services(
        self, services: List[str], cluster: str = None, include: List[Literal["TAGS"]] = None
    ) -> DescribeServicesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.describe_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#describe-services)
        """

    def describe_task_definition(
        self, taskDefinition: str, include: List[Literal["TAGS"]] = None
    ) -> DescribeTaskDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.describe_task_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#describe-task-definition)
        """

    def describe_task_sets(
        self,
        cluster: str,
        service: str,
        taskSets: List[str] = None,
        include: List[Literal["TAGS"]] = None,
    ) -> DescribeTaskSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.describe_task_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#describe-task-sets)
        """

    def describe_tasks(
        self, tasks: List[str], cluster: str = None, include: List[Literal["TAGS"]] = None
    ) -> DescribeTasksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.describe_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#describe-tasks)
        """

    def discover_poll_endpoint(
        self, containerInstance: str = None, cluster: str = None
    ) -> DiscoverPollEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.discover_poll_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#discover-poll-endpoint)
        """

    def execute_command(
        self, command: str, interactive: bool, task: str, cluster: str = None, container: str = None
    ) -> ExecuteCommandResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.execute_command)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#execute-command)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#generate-presigned-url)
        """

    def list_account_settings(
        self,
        name: SettingName = None,
        value: str = None,
        principalArn: str = None,
        effectiveSettings: bool = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAccountSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.list_account_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list-account-settings)
        """

    def list_attributes(
        self,
        targetType: Literal["container-instance"],
        cluster: str = None,
        attributeName: str = None,
        attributeValue: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.list_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list-attributes)
        """

    def list_clusters(
        self, nextToken: str = None, maxResults: int = None
    ) -> ListClustersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.list_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list-clusters)
        """

    def list_container_instances(
        self,
        cluster: str = None,
        filter: str = None,
        nextToken: str = None,
        maxResults: int = None,
        status: ContainerInstanceStatus = None,
    ) -> ListContainerInstancesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.list_container_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list-container-instances)
        """

    def list_services(
        self,
        cluster: str = None,
        nextToken: str = None,
        maxResults: int = None,
        launchType: LaunchType = None,
        schedulingStrategy: SchedulingStrategy = None,
    ) -> ListServicesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.list_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list-services)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list-tags-for-resource)
        """

    def list_task_definition_families(
        self,
        familyPrefix: str = None,
        status: TaskDefinitionFamilyStatus = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListTaskDefinitionFamiliesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.list_task_definition_families)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list-task-definition-families)
        """

    def list_task_definitions(
        self,
        familyPrefix: str = None,
        status: TaskDefinitionStatus = None,
        sort: SortOrder = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListTaskDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.list_task_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list-task-definitions)
        """

    def list_tasks(
        self,
        cluster: str = None,
        containerInstance: str = None,
        family: str = None,
        nextToken: str = None,
        maxResults: int = None,
        startedBy: str = None,
        serviceName: str = None,
        desiredStatus: DesiredStatus = None,
        launchType: LaunchType = None,
    ) -> ListTasksResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.list_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#list-tasks)
        """

    def put_account_setting(
        self, name: SettingName, value: str, principalArn: str = None
    ) -> PutAccountSettingResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.put_account_setting)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#put-account-setting)
        """

    def put_account_setting_default(
        self, name: SettingName, value: str
    ) -> PutAccountSettingDefaultResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.put_account_setting_default)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#put-account-setting-default)
        """

    def put_attributes(
        self, attributes: List["AttributeTypeDef"], cluster: str = None
    ) -> PutAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.put_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#put-attributes)
        """

    def put_cluster_capacity_providers(
        self,
        cluster: str,
        capacityProviders: List[str],
        defaultCapacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"],
    ) -> PutClusterCapacityProvidersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.put_cluster_capacity_providers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#put-cluster-capacity-providers)
        """

    def register_container_instance(
        self,
        cluster: str = None,
        instanceIdentityDocument: str = None,
        instanceIdentityDocumentSignature: str = None,
        totalResources: List["ResourceTypeDef"] = None,
        versionInfo: "VersionInfoTypeDef" = None,
        containerInstanceArn: str = None,
        attributes: List["AttributeTypeDef"] = None,
        platformDevices: List[PlatformDeviceTypeDef] = None,
        tags: List["TagTypeDef"] = None,
    ) -> RegisterContainerInstanceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.register_container_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#register-container-instance)
        """

    def register_task_definition(
        self,
        family: str,
        containerDefinitions: List["ContainerDefinitionTypeDef"],
        taskRoleArn: str = None,
        executionRoleArn: str = None,
        networkMode: NetworkMode = None,
        volumes: List["VolumeTypeDef"] = None,
        placementConstraints: List["TaskDefinitionPlacementConstraintTypeDef"] = None,
        requiresCompatibilities: List[Compatibility] = None,
        cpu: str = None,
        memory: str = None,
        tags: List["TagTypeDef"] = None,
        pidMode: PidMode = None,
        ipcMode: IpcMode = None,
        proxyConfiguration: "ProxyConfigurationTypeDef" = None,
        inferenceAccelerators: List["InferenceAcceleratorTypeDef"] = None,
        ephemeralStorage: "EphemeralStorageTypeDef" = None,
    ) -> RegisterTaskDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.register_task_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#register-task-definition)
        """

    def run_task(
        self,
        taskDefinition: str,
        capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
        cluster: str = None,
        count: int = None,
        enableECSManagedTags: bool = None,
        enableExecuteCommand: bool = None,
        group: str = None,
        launchType: LaunchType = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None,
        overrides: "TaskOverrideTypeDef" = None,
        placementConstraints: List["PlacementConstraintTypeDef"] = None,
        placementStrategy: List["PlacementStrategyTypeDef"] = None,
        platformVersion: str = None,
        propagateTags: PropagateTags = None,
        referenceId: str = None,
        startedBy: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> RunTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.run_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#run-task)
        """

    def start_task(
        self,
        containerInstances: List[str],
        taskDefinition: str,
        cluster: str = None,
        enableECSManagedTags: bool = None,
        enableExecuteCommand: bool = None,
        group: str = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None,
        overrides: "TaskOverrideTypeDef" = None,
        propagateTags: PropagateTags = None,
        referenceId: str = None,
        startedBy: str = None,
        tags: List["TagTypeDef"] = None,
    ) -> StartTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.start_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#start-task)
        """

    def stop_task(
        self, task: str, cluster: str = None, reason: str = None
    ) -> StopTaskResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.stop_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#stop-task)
        """

    def submit_attachment_state_changes(
        self, attachments: List[AttachmentStateChangeTypeDef], cluster: str = None
    ) -> SubmitAttachmentStateChangesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.submit_attachment_state_changes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#submit-attachment-state-changes)
        """

    def submit_container_state_change(
        self,
        cluster: str = None,
        task: str = None,
        containerName: str = None,
        runtimeId: str = None,
        status: str = None,
        exitCode: int = None,
        reason: str = None,
        networkBindings: List["NetworkBindingTypeDef"] = None,
    ) -> SubmitContainerStateChangeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.submit_container_state_change)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#submit-container-state-change)
        """

    def submit_task_state_change(
        self,
        cluster: str = None,
        task: str = None,
        status: str = None,
        reason: str = None,
        containers: List[ContainerStateChangeTypeDef] = None,
        attachments: List[AttachmentStateChangeTypeDef] = None,
        managedAgents: List[ManagedAgentStateChangeTypeDef] = None,
        pullStartedAt: datetime = None,
        pullStoppedAt: datetime = None,
        executionStoppedAt: datetime = None,
    ) -> SubmitTaskStateChangeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.submit_task_state_change)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#submit-task-state-change)
        """

    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#tag-resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#untag-resource)
        """

    def update_capacity_provider(
        self, name: str, autoScalingGroupProvider: AutoScalingGroupProviderUpdateTypeDef
    ) -> UpdateCapacityProviderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.update_capacity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update-capacity-provider)
        """

    def update_cluster(
        self,
        cluster: str,
        settings: List["ClusterSettingTypeDef"] = None,
        configuration: "ClusterConfigurationTypeDef" = None,
    ) -> UpdateClusterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.update_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update-cluster)
        """

    def update_cluster_settings(
        self, cluster: str, settings: List["ClusterSettingTypeDef"]
    ) -> UpdateClusterSettingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.update_cluster_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update-cluster-settings)
        """

    def update_container_agent(
        self, containerInstance: str, cluster: str = None
    ) -> UpdateContainerAgentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.update_container_agent)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update-container-agent)
        """

    def update_container_instances_state(
        self, containerInstances: List[str], status: ContainerInstanceStatus, cluster: str = None
    ) -> UpdateContainerInstancesStateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.update_container_instances_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update-container-instances-state)
        """

    def update_service(
        self,
        service: str,
        cluster: str = None,
        desiredCount: int = None,
        taskDefinition: str = None,
        capacityProviderStrategy: List["CapacityProviderStrategyItemTypeDef"] = None,
        deploymentConfiguration: "DeploymentConfigurationTypeDef" = None,
        networkConfiguration: "NetworkConfigurationTypeDef" = None,
        placementConstraints: List["PlacementConstraintTypeDef"] = None,
        placementStrategy: List["PlacementStrategyTypeDef"] = None,
        platformVersion: str = None,
        forceNewDeployment: bool = None,
        healthCheckGracePeriodSeconds: int = None,
        enableExecuteCommand: bool = None,
    ) -> UpdateServiceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.update_service)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update-service)
        """

    def update_service_primary_task_set(
        self, cluster: str, service: str, primaryTaskSet: str
    ) -> UpdateServicePrimaryTaskSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.update_service_primary_task_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update-service-primary-task-set)
        """

    def update_task_set(
        self, cluster: str, service: str, taskSet: str, scale: "ScaleTypeDef"
    ) -> UpdateTaskSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Client.update_task_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/client.html#update-task-set)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_account_settings"]
    ) -> ListAccountSettingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Paginator.ListAccountSettings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listaccountsettingspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_attributes"]) -> ListAttributesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Paginator.ListAttributes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listattributespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Paginator.ListClusters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listclusterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_container_instances"]
    ) -> ListContainerInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Paginator.ListContainerInstances)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listcontainerinstancespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_services"]) -> ListServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Paginator.ListServices)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listservicespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_task_definition_families"]
    ) -> ListTaskDefinitionFamiliesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitionFamilies)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listtaskdefinitionfamiliespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_task_definitions"]
    ) -> ListTaskDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Paginator.ListTaskDefinitions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listtaskdefinitionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tasks"]) -> ListTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Paginator.ListTasks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/paginators.html#listtaskspaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["services_inactive"]) -> ServicesInactiveWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Waiter.services_inactive)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#servicesinactivewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["services_stable"]) -> ServicesStableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Waiter.services_stable)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#servicesstablewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["tasks_running"]) -> TasksRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Waiter.tasks_running)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#tasksrunningwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["tasks_stopped"]) -> TasksStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/ecs.html#ECS.Waiter.tasks_stopped)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ecs/waiters.html#tasksstoppedwaiter)
        """
