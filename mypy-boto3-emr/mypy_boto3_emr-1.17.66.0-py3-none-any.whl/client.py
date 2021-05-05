"""
Type annotations for emr service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_emr import EMRClient

    client: EMRClient = boto3.client("emr")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_emr.literals import (
    AuthMode,
    ClusterState,
    IdentityType,
    InstanceFleetType,
    InstanceGroupType,
    InstanceState,
    JobFlowExecutionState,
    NotebookExecutionStatus,
    RepoUpgradeOnBoot,
    ScaleDownBehavior,
    StepCancellationOption,
    StepState,
)
from mypy_boto3_emr.paginator import (
    ListBootstrapActionsPaginator,
    ListClustersPaginator,
    ListInstanceFleetsPaginator,
    ListInstanceGroupsPaginator,
    ListInstancesPaginator,
    ListNotebookExecutionsPaginator,
    ListSecurityConfigurationsPaginator,
    ListStepsPaginator,
    ListStudioSessionMappingsPaginator,
    ListStudiosPaginator,
)
from mypy_boto3_emr.type_defs import (
    AddInstanceFleetOutputTypeDef,
    AddInstanceGroupsOutputTypeDef,
    AddJobFlowStepsOutputTypeDef,
    ApplicationTypeDef,
    AutoScalingPolicyTypeDef,
    BlockPublicAccessConfigurationTypeDef,
    BootstrapActionConfigTypeDef,
    CancelStepsOutputTypeDef,
    ConfigurationTypeDef,
    CreateSecurityConfigurationOutputTypeDef,
    CreateStudioOutputTypeDef,
    DescribeClusterOutputTypeDef,
    DescribeJobFlowsOutputTypeDef,
    DescribeNotebookExecutionOutputTypeDef,
    DescribeSecurityConfigurationOutputTypeDef,
    DescribeStepOutputTypeDef,
    DescribeStudioOutputTypeDef,
    ExecutionEngineConfigTypeDef,
    GetBlockPublicAccessConfigurationOutputTypeDef,
    GetManagedScalingPolicyOutputTypeDef,
    GetStudioSessionMappingOutputTypeDef,
    InstanceFleetConfigTypeDef,
    InstanceFleetModifyConfigTypeDef,
    InstanceGroupConfigTypeDef,
    InstanceGroupModifyConfigTypeDef,
    JobFlowInstancesConfigTypeDef,
    KerberosAttributesTypeDef,
    ListBootstrapActionsOutputTypeDef,
    ListClustersOutputTypeDef,
    ListInstanceFleetsOutputTypeDef,
    ListInstanceGroupsOutputTypeDef,
    ListInstancesOutputTypeDef,
    ListNotebookExecutionsOutputTypeDef,
    ListSecurityConfigurationsOutputTypeDef,
    ListStepsOutputTypeDef,
    ListStudioSessionMappingsOutputTypeDef,
    ListStudiosOutputTypeDef,
    ManagedScalingPolicyTypeDef,
    ModifyClusterOutputTypeDef,
    PlacementGroupConfigTypeDef,
    PutAutoScalingPolicyOutputTypeDef,
    RunJobFlowOutputTypeDef,
    StartNotebookExecutionOutputTypeDef,
    StepConfigTypeDef,
    SupportedProductConfigTypeDef,
    TagTypeDef,
)
from mypy_boto3_emr.waiter import ClusterRunningWaiter, ClusterTerminatedWaiter, StepCompleteWaiter

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EMRClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]


class EMRClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_instance_fleet(
        self, ClusterId: str, InstanceFleet: "InstanceFleetConfigTypeDef"
    ) -> AddInstanceFleetOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.add_instance_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#add-instance-fleet)
        """

    def add_instance_groups(
        self, InstanceGroups: List["InstanceGroupConfigTypeDef"], JobFlowId: str
    ) -> AddInstanceGroupsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.add_instance_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#add-instance-groups)
        """

    def add_job_flow_steps(
        self, JobFlowId: str, Steps: List["StepConfigTypeDef"]
    ) -> AddJobFlowStepsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.add_job_flow_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#add-job-flow-steps)
        """

    def add_tags(self, ResourceId: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.add_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#add-tags)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#can-paginate)
        """

    def cancel_steps(
        self,
        ClusterId: str,
        StepIds: List[str],
        StepCancellationOption: StepCancellationOption = None,
    ) -> CancelStepsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.cancel_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#cancel-steps)
        """

    def create_security_configuration(
        self, Name: str, SecurityConfiguration: str
    ) -> CreateSecurityConfigurationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.create_security_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#create-security-configuration)
        """

    def create_studio(
        self,
        Name: str,
        AuthMode: AuthMode,
        VpcId: str,
        SubnetIds: List[str],
        ServiceRole: str,
        UserRole: str,
        WorkspaceSecurityGroupId: str,
        EngineSecurityGroupId: str,
        DefaultS3Location: str,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateStudioOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.create_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#create-studio)
        """

    def create_studio_session_mapping(
        self,
        StudioId: str,
        IdentityType: IdentityType,
        SessionPolicyArn: str,
        IdentityId: str = None,
        IdentityName: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.create_studio_session_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#create-studio-session-mapping)
        """

    def delete_security_configuration(self, Name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.delete_security_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#delete-security-configuration)
        """

    def delete_studio(self, StudioId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.delete_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#delete-studio)
        """

    def delete_studio_session_mapping(
        self,
        StudioId: str,
        IdentityType: IdentityType,
        IdentityId: str = None,
        IdentityName: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.delete_studio_session_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#delete-studio-session-mapping)
        """

    def describe_cluster(self, ClusterId: str) -> DescribeClusterOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.describe_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe-cluster)
        """

    def describe_job_flows(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        JobFlowIds: List[str] = None,
        JobFlowStates: List[JobFlowExecutionState] = None,
    ) -> DescribeJobFlowsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.describe_job_flows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe-job-flows)
        """

    def describe_notebook_execution(
        self, NotebookExecutionId: str
    ) -> DescribeNotebookExecutionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.describe_notebook_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe-notebook-execution)
        """

    def describe_security_configuration(
        self, Name: str
    ) -> DescribeSecurityConfigurationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.describe_security_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe-security-configuration)
        """

    def describe_step(self, ClusterId: str, StepId: str) -> DescribeStepOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.describe_step)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe-step)
        """

    def describe_studio(self, StudioId: str) -> DescribeStudioOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.describe_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#describe-studio)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#generate-presigned-url)
        """

    def get_block_public_access_configuration(
        self,
    ) -> GetBlockPublicAccessConfigurationOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.get_block_public_access_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#get-block-public-access-configuration)
        """

    def get_managed_scaling_policy(self, ClusterId: str) -> GetManagedScalingPolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.get_managed_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#get-managed-scaling-policy)
        """

    def get_studio_session_mapping(
        self,
        StudioId: str,
        IdentityType: IdentityType,
        IdentityId: str = None,
        IdentityName: str = None,
    ) -> GetStudioSessionMappingOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.get_studio_session_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#get-studio-session-mapping)
        """

    def list_bootstrap_actions(
        self, ClusterId: str, Marker: str = None
    ) -> ListBootstrapActionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.list_bootstrap_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list-bootstrap-actions)
        """

    def list_clusters(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        ClusterStates: List[ClusterState] = None,
        Marker: str = None,
    ) -> ListClustersOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.list_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list-clusters)
        """

    def list_instance_fleets(
        self, ClusterId: str, Marker: str = None
    ) -> ListInstanceFleetsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.list_instance_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list-instance-fleets)
        """

    def list_instance_groups(
        self, ClusterId: str, Marker: str = None
    ) -> ListInstanceGroupsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.list_instance_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list-instance-groups)
        """

    def list_instances(
        self,
        ClusterId: str,
        InstanceGroupId: str = None,
        InstanceGroupTypes: List[InstanceGroupType] = None,
        InstanceFleetId: str = None,
        InstanceFleetType: InstanceFleetType = None,
        InstanceStates: List[InstanceState] = None,
        Marker: str = None,
    ) -> ListInstancesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.list_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list-instances)
        """

    def list_notebook_executions(
        self,
        EditorId: str = None,
        Status: NotebookExecutionStatus = None,
        From: datetime = None,
        To: datetime = None,
        Marker: str = None,
    ) -> ListNotebookExecutionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.list_notebook_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list-notebook-executions)
        """

    def list_security_configurations(
        self, Marker: str = None
    ) -> ListSecurityConfigurationsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.list_security_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list-security-configurations)
        """

    def list_steps(
        self,
        ClusterId: str,
        StepStates: List[StepState] = None,
        StepIds: List[str] = None,
        Marker: str = None,
    ) -> ListStepsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.list_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list-steps)
        """

    def list_studio_session_mappings(
        self, StudioId: str = None, IdentityType: IdentityType = None, Marker: str = None
    ) -> ListStudioSessionMappingsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.list_studio_session_mappings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list-studio-session-mappings)
        """

    def list_studios(self, Marker: str = None) -> ListStudiosOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.list_studios)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#list-studios)
        """

    def modify_cluster(
        self, ClusterId: str, StepConcurrencyLevel: int = None
    ) -> ModifyClusterOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.modify_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#modify-cluster)
        """

    def modify_instance_fleet(
        self, ClusterId: str, InstanceFleet: InstanceFleetModifyConfigTypeDef
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.modify_instance_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#modify-instance-fleet)
        """

    def modify_instance_groups(
        self, ClusterId: str = None, InstanceGroups: List[InstanceGroupModifyConfigTypeDef] = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.modify_instance_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#modify-instance-groups)
        """

    def put_auto_scaling_policy(
        self, ClusterId: str, InstanceGroupId: str, AutoScalingPolicy: "AutoScalingPolicyTypeDef"
    ) -> PutAutoScalingPolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.put_auto_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#put-auto-scaling-policy)
        """

    def put_block_public_access_configuration(
        self, BlockPublicAccessConfiguration: "BlockPublicAccessConfigurationTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.put_block_public_access_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#put-block-public-access-configuration)
        """

    def put_managed_scaling_policy(
        self, ClusterId: str, ManagedScalingPolicy: "ManagedScalingPolicyTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.put_managed_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#put-managed-scaling-policy)
        """

    def remove_auto_scaling_policy(self, ClusterId: str, InstanceGroupId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.remove_auto_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#remove-auto-scaling-policy)
        """

    def remove_managed_scaling_policy(self, ClusterId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.remove_managed_scaling_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#remove-managed-scaling-policy)
        """

    def remove_tags(self, ResourceId: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.remove_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#remove-tags)
        """

    def run_job_flow(
        self,
        Name: str,
        Instances: JobFlowInstancesConfigTypeDef,
        LogUri: str = None,
        LogEncryptionKmsKeyId: str = None,
        AdditionalInfo: str = None,
        AmiVersion: str = None,
        ReleaseLabel: str = None,
        Steps: List["StepConfigTypeDef"] = None,
        BootstrapActions: List["BootstrapActionConfigTypeDef"] = None,
        SupportedProducts: List[str] = None,
        NewSupportedProducts: List[SupportedProductConfigTypeDef] = None,
        Applications: List["ApplicationTypeDef"] = None,
        Configurations: List["ConfigurationTypeDef"] = None,
        VisibleToAllUsers: bool = None,
        JobFlowRole: str = None,
        ServiceRole: str = None,
        Tags: List["TagTypeDef"] = None,
        SecurityConfiguration: str = None,
        AutoScalingRole: str = None,
        ScaleDownBehavior: ScaleDownBehavior = None,
        CustomAmiId: str = None,
        EbsRootVolumeSize: int = None,
        RepoUpgradeOnBoot: RepoUpgradeOnBoot = None,
        KerberosAttributes: "KerberosAttributesTypeDef" = None,
        StepConcurrencyLevel: int = None,
        ManagedScalingPolicy: "ManagedScalingPolicyTypeDef" = None,
        PlacementGroupConfigs: List["PlacementGroupConfigTypeDef"] = None,
    ) -> RunJobFlowOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.run_job_flow)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#run-job-flow)
        """

    def set_termination_protection(self, JobFlowIds: List[str], TerminationProtected: bool) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.set_termination_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#set-termination-protection)
        """

    def set_visible_to_all_users(self, JobFlowIds: List[str], VisibleToAllUsers: bool) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.set_visible_to_all_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#set-visible-to-all-users)
        """

    def start_notebook_execution(
        self,
        EditorId: str,
        RelativePath: str,
        ExecutionEngine: "ExecutionEngineConfigTypeDef",
        ServiceRole: str,
        NotebookExecutionName: str = None,
        NotebookParams: str = None,
        NotebookInstanceSecurityGroupId: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> StartNotebookExecutionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.start_notebook_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#start-notebook-execution)
        """

    def stop_notebook_execution(self, NotebookExecutionId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.stop_notebook_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#stop-notebook-execution)
        """

    def terminate_job_flows(self, JobFlowIds: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.terminate_job_flows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#terminate-job-flows)
        """

    def update_studio(
        self,
        StudioId: str,
        Name: str = None,
        Description: str = None,
        SubnetIds: List[str] = None,
        DefaultS3Location: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.update_studio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#update-studio)
        """

    def update_studio_session_mapping(
        self,
        StudioId: str,
        IdentityType: IdentityType,
        SessionPolicyArn: str,
        IdentityId: str = None,
        IdentityName: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Client.update_studio_session_mapping)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/client.html#update-studio-session-mapping)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_bootstrap_actions"]
    ) -> ListBootstrapActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Paginator.ListBootstrapActions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listbootstrapactionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_clusters"]) -> ListClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Paginator.ListClusters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listclusterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_fleets"]
    ) -> ListInstanceFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Paginator.ListInstanceFleets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listinstancefleetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_instance_groups"]
    ) -> ListInstanceGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Paginator.ListInstanceGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listinstancegroupspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_instances"]) -> ListInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Paginator.ListInstances)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notebook_executions"]
    ) -> ListNotebookExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Paginator.ListNotebookExecutions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listnotebookexecutionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_security_configurations"]
    ) -> ListSecurityConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Paginator.ListSecurityConfigurations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#listsecurityconfigurationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_steps"]) -> ListStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Paginator.ListSteps)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#liststepspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_studio_session_mappings"]
    ) -> ListStudioSessionMappingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Paginator.ListStudioSessionMappings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#liststudiosessionmappingspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_studios"]) -> ListStudiosPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Paginator.ListStudios)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/paginators.html#liststudiospaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_running"]) -> ClusterRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Waiter.cluster_running)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html#clusterrunningwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["cluster_terminated"]) -> ClusterTerminatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Waiter.cluster_terminated)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html#clusterterminatedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["step_complete"]) -> StepCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr.html#EMR.Waiter.step_complete)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr/waiters.html#stepcompletewaiter)
        """
