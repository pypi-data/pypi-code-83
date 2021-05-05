"""
Type annotations for sagemaker service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker import SageMakerClient

    client: SageMakerClient = boto3.client("sagemaker")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_sagemaker.literals import (
    ActionStatus,
    AlgorithmSortBy,
    AppImageConfigSortKey,
    AppNetworkAccessType,
    AppType,
    AssociationEdgeType,
    AuthMode,
    AutoMLJobStatus,
    AutoMLSortBy,
    AutoMLSortOrder,
    BatchStrategy,
    CandidateSortBy,
    CandidateStatus,
    CodeRepositorySortBy,
    CodeRepositorySortOrder,
    CompilationJobStatus,
    DirectInternetAccess,
    EdgePackagingJobStatus,
    EndpointConfigSortKey,
    EndpointSortKey,
    EndpointStatus,
    ExecutionStatus,
    FeatureGroupSortBy,
    FeatureGroupSortOrder,
    FeatureGroupStatus,
    HyperParameterTuningJobSortByOptions,
    HyperParameterTuningJobStatus,
    ImageSortBy,
    ImageSortOrder,
    ImageVersionSortBy,
    ImageVersionSortOrder,
    InstanceType,
    LabelingJobStatus,
    ListCompilationJobsSortBy,
    ListDeviceFleetsSortBy,
    ListEdgePackagingJobsSortBy,
    ListWorkforcesSortByOptions,
    ListWorkteamsSortByOptions,
    ModelApprovalStatus,
    ModelPackageGroupSortBy,
    ModelPackageSortBy,
    ModelPackageType,
    ModelSortKey,
    MonitoringExecutionSortKey,
    MonitoringJobDefinitionSortKey,
    MonitoringScheduleSortKey,
    MonitoringType,
    NotebookInstanceAcceleratorType,
    NotebookInstanceLifecycleConfigSortKey,
    NotebookInstanceLifecycleConfigSortOrder,
    NotebookInstanceSortKey,
    NotebookInstanceSortOrder,
    NotebookInstanceStatus,
    OfflineStoreStatusValue,
    OrderKey,
    ProblemType,
    ProcessingJobStatus,
    ProjectSortBy,
    ProjectSortOrder,
    ResourceType,
    RootAccess,
    ScheduleStatus,
    SearchSortOrder,
    SortActionsBy,
    SortAssociationsBy,
    SortBy,
    SortContextsBy,
    SortExperimentsBy,
    SortOrder,
    SortPipelineExecutionsBy,
    SortPipelinesBy,
    SortTrialComponentsBy,
    SortTrialsBy,
    TrainingJobSortByOptions,
    TrainingJobStatus,
    TransformJobStatus,
    UserProfileSortKey,
)
from mypy_boto3_sagemaker.paginator import (
    ListActionsPaginator,
    ListAlgorithmsPaginator,
    ListAppImageConfigsPaginator,
    ListAppsPaginator,
    ListArtifactsPaginator,
    ListAssociationsPaginator,
    ListAutoMLJobsPaginator,
    ListCandidatesForAutoMLJobPaginator,
    ListCodeRepositoriesPaginator,
    ListCompilationJobsPaginator,
    ListContextsPaginator,
    ListDataQualityJobDefinitionsPaginator,
    ListDeviceFleetsPaginator,
    ListDevicesPaginator,
    ListDomainsPaginator,
    ListEdgePackagingJobsPaginator,
    ListEndpointConfigsPaginator,
    ListEndpointsPaginator,
    ListExperimentsPaginator,
    ListFeatureGroupsPaginator,
    ListFlowDefinitionsPaginator,
    ListHumanTaskUisPaginator,
    ListHyperParameterTuningJobsPaginator,
    ListImagesPaginator,
    ListImageVersionsPaginator,
    ListLabelingJobsForWorkteamPaginator,
    ListLabelingJobsPaginator,
    ListModelBiasJobDefinitionsPaginator,
    ListModelExplainabilityJobDefinitionsPaginator,
    ListModelPackageGroupsPaginator,
    ListModelPackagesPaginator,
    ListModelQualityJobDefinitionsPaginator,
    ListModelsPaginator,
    ListMonitoringExecutionsPaginator,
    ListMonitoringSchedulesPaginator,
    ListNotebookInstanceLifecycleConfigsPaginator,
    ListNotebookInstancesPaginator,
    ListPipelineExecutionsPaginator,
    ListPipelineExecutionStepsPaginator,
    ListPipelineParametersForExecutionPaginator,
    ListPipelinesPaginator,
    ListProcessingJobsPaginator,
    ListSubscribedWorkteamsPaginator,
    ListTagsPaginator,
    ListTrainingJobsForHyperParameterTuningJobPaginator,
    ListTrainingJobsPaginator,
    ListTransformJobsPaginator,
    ListTrialComponentsPaginator,
    ListTrialsPaginator,
    ListUserProfilesPaginator,
    ListWorkforcesPaginator,
    ListWorkteamsPaginator,
    SearchPaginator,
)
from mypy_boto3_sagemaker.type_defs import (
    ActionSourceTypeDef,
    AddAssociationResponseTypeDef,
    AddTagsOutputTypeDef,
    AlgorithmSpecificationTypeDef,
    AlgorithmValidationSpecificationTypeDef,
    AppSpecificationTypeDef,
    ArtifactSourceTypeDef,
    AssociateTrialComponentResponseTypeDef,
    AutoMLChannelTypeDef,
    AutoMLJobConfigTypeDef,
    AutoMLJobObjectiveTypeDef,
    AutoMLOutputDataConfigTypeDef,
    ChannelTypeDef,
    CheckpointConfigTypeDef,
    CognitoConfigTypeDef,
    ContainerDefinitionTypeDef,
    ContextSourceTypeDef,
    CreateActionResponseTypeDef,
    CreateAlgorithmOutputTypeDef,
    CreateAppImageConfigResponseTypeDef,
    CreateAppResponseTypeDef,
    CreateArtifactResponseTypeDef,
    CreateAutoMLJobResponseTypeDef,
    CreateCodeRepositoryOutputTypeDef,
    CreateCompilationJobResponseTypeDef,
    CreateContextResponseTypeDef,
    CreateDataQualityJobDefinitionResponseTypeDef,
    CreateDomainResponseTypeDef,
    CreateEndpointConfigOutputTypeDef,
    CreateEndpointOutputTypeDef,
    CreateExperimentResponseTypeDef,
    CreateFeatureGroupResponseTypeDef,
    CreateFlowDefinitionResponseTypeDef,
    CreateHumanTaskUiResponseTypeDef,
    CreateHyperParameterTuningJobResponseTypeDef,
    CreateImageResponseTypeDef,
    CreateImageVersionResponseTypeDef,
    CreateLabelingJobResponseTypeDef,
    CreateModelBiasJobDefinitionResponseTypeDef,
    CreateModelExplainabilityJobDefinitionResponseTypeDef,
    CreateModelOutputTypeDef,
    CreateModelPackageGroupOutputTypeDef,
    CreateModelPackageOutputTypeDef,
    CreateModelQualityJobDefinitionResponseTypeDef,
    CreateMonitoringScheduleResponseTypeDef,
    CreateNotebookInstanceLifecycleConfigOutputTypeDef,
    CreateNotebookInstanceOutputTypeDef,
    CreatePipelineResponseTypeDef,
    CreatePresignedDomainUrlResponseTypeDef,
    CreatePresignedNotebookInstanceUrlOutputTypeDef,
    CreateProcessingJobResponseTypeDef,
    CreateProjectOutputTypeDef,
    CreateTrainingJobResponseTypeDef,
    CreateTransformJobResponseTypeDef,
    CreateTrialComponentResponseTypeDef,
    CreateTrialResponseTypeDef,
    CreateUserProfileResponseTypeDef,
    CreateWorkforceResponseTypeDef,
    CreateWorkteamResponseTypeDef,
    DataCaptureConfigTypeDef,
    DataProcessingTypeDef,
    DataQualityAppSpecificationTypeDef,
    DataQualityBaselineConfigTypeDef,
    DataQualityJobInputTypeDef,
    DebugHookConfigTypeDef,
    DebugRuleConfigurationTypeDef,
    DeleteActionResponseTypeDef,
    DeleteArtifactResponseTypeDef,
    DeleteAssociationResponseTypeDef,
    DeleteContextResponseTypeDef,
    DeleteExperimentResponseTypeDef,
    DeletePipelineResponseTypeDef,
    DeleteTrialComponentResponseTypeDef,
    DeleteTrialResponseTypeDef,
    DeleteWorkteamResponseTypeDef,
    DeploymentConfigTypeDef,
    DescribeActionResponseTypeDef,
    DescribeAlgorithmOutputTypeDef,
    DescribeAppImageConfigResponseTypeDef,
    DescribeAppResponseTypeDef,
    DescribeArtifactResponseTypeDef,
    DescribeAutoMLJobResponseTypeDef,
    DescribeCodeRepositoryOutputTypeDef,
    DescribeCompilationJobResponseTypeDef,
    DescribeContextResponseTypeDef,
    DescribeDataQualityJobDefinitionResponseTypeDef,
    DescribeDeviceFleetResponseTypeDef,
    DescribeDeviceResponseTypeDef,
    DescribeDomainResponseTypeDef,
    DescribeEdgePackagingJobResponseTypeDef,
    DescribeEndpointConfigOutputTypeDef,
    DescribeEndpointOutputTypeDef,
    DescribeExperimentResponseTypeDef,
    DescribeFeatureGroupResponseTypeDef,
    DescribeFlowDefinitionResponseTypeDef,
    DescribeHumanTaskUiResponseTypeDef,
    DescribeHyperParameterTuningJobResponseTypeDef,
    DescribeImageResponseTypeDef,
    DescribeImageVersionResponseTypeDef,
    DescribeLabelingJobResponseTypeDef,
    DescribeModelBiasJobDefinitionResponseTypeDef,
    DescribeModelExplainabilityJobDefinitionResponseTypeDef,
    DescribeModelOutputTypeDef,
    DescribeModelPackageGroupOutputTypeDef,
    DescribeModelPackageOutputTypeDef,
    DescribeModelQualityJobDefinitionResponseTypeDef,
    DescribeMonitoringScheduleResponseTypeDef,
    DescribeNotebookInstanceLifecycleConfigOutputTypeDef,
    DescribeNotebookInstanceOutputTypeDef,
    DescribePipelineDefinitionForExecutionResponseTypeDef,
    DescribePipelineExecutionResponseTypeDef,
    DescribePipelineResponseTypeDef,
    DescribeProcessingJobResponseTypeDef,
    DescribeProjectOutputTypeDef,
    DescribeSubscribedWorkteamResponseTypeDef,
    DescribeTrainingJobResponseTypeDef,
    DescribeTransformJobResponseTypeDef,
    DescribeTrialComponentResponseTypeDef,
    DescribeTrialResponseTypeDef,
    DescribeUserProfileResponseTypeDef,
    DescribeWorkforceResponseTypeDef,
    DescribeWorkteamResponseTypeDef,
    DesiredWeightAndCapacityTypeDef,
    DeviceTypeDef,
    DisassociateTrialComponentResponseTypeDef,
    EdgeOutputConfigTypeDef,
    ExperimentConfigTypeDef,
    FeatureDefinitionTypeDef,
    FlowDefinitionOutputConfigTypeDef,
    GetDeviceFleetReportResponseTypeDef,
    GetModelPackageGroupPolicyOutputTypeDef,
    GetSagemakerServicecatalogPortfolioStatusOutputTypeDef,
    GetSearchSuggestionsResponseTypeDef,
    GitConfigForUpdateTypeDef,
    GitConfigTypeDef,
    HumanLoopActivationConfigTypeDef,
    HumanLoopConfigTypeDef,
    HumanLoopRequestSourceTypeDef,
    HumanTaskConfigTypeDef,
    HyperParameterTrainingJobDefinitionTypeDef,
    HyperParameterTuningJobConfigTypeDef,
    HyperParameterTuningJobWarmStartConfigTypeDef,
    InferenceExecutionConfigTypeDef,
    InferenceSpecificationTypeDef,
    InputConfigTypeDef,
    KernelGatewayImageConfigTypeDef,
    LabelingJobAlgorithmsConfigTypeDef,
    LabelingJobInputConfigTypeDef,
    LabelingJobOutputConfigTypeDef,
    LabelingJobStoppingConditionsTypeDef,
    ListActionsResponseTypeDef,
    ListAlgorithmsOutputTypeDef,
    ListAppImageConfigsResponseTypeDef,
    ListAppsResponseTypeDef,
    ListArtifactsResponseTypeDef,
    ListAssociationsResponseTypeDef,
    ListAutoMLJobsResponseTypeDef,
    ListCandidatesForAutoMLJobResponseTypeDef,
    ListCodeRepositoriesOutputTypeDef,
    ListCompilationJobsResponseTypeDef,
    ListContextsResponseTypeDef,
    ListDataQualityJobDefinitionsResponseTypeDef,
    ListDeviceFleetsResponseTypeDef,
    ListDevicesResponseTypeDef,
    ListDomainsResponseTypeDef,
    ListEdgePackagingJobsResponseTypeDef,
    ListEndpointConfigsOutputTypeDef,
    ListEndpointsOutputTypeDef,
    ListExperimentsResponseTypeDef,
    ListFeatureGroupsResponseTypeDef,
    ListFlowDefinitionsResponseTypeDef,
    ListHumanTaskUisResponseTypeDef,
    ListHyperParameterTuningJobsResponseTypeDef,
    ListImagesResponseTypeDef,
    ListImageVersionsResponseTypeDef,
    ListLabelingJobsForWorkteamResponseTypeDef,
    ListLabelingJobsResponseTypeDef,
    ListModelBiasJobDefinitionsResponseTypeDef,
    ListModelExplainabilityJobDefinitionsResponseTypeDef,
    ListModelPackageGroupsOutputTypeDef,
    ListModelPackagesOutputTypeDef,
    ListModelQualityJobDefinitionsResponseTypeDef,
    ListModelsOutputTypeDef,
    ListMonitoringExecutionsResponseTypeDef,
    ListMonitoringSchedulesResponseTypeDef,
    ListNotebookInstanceLifecycleConfigsOutputTypeDef,
    ListNotebookInstancesOutputTypeDef,
    ListPipelineExecutionsResponseTypeDef,
    ListPipelineExecutionStepsResponseTypeDef,
    ListPipelineParametersForExecutionResponseTypeDef,
    ListPipelinesResponseTypeDef,
    ListProcessingJobsResponseTypeDef,
    ListProjectsOutputTypeDef,
    ListSubscribedWorkteamsResponseTypeDef,
    ListTagsOutputTypeDef,
    ListTrainingJobsForHyperParameterTuningJobResponseTypeDef,
    ListTrainingJobsResponseTypeDef,
    ListTransformJobsResponseTypeDef,
    ListTrialComponentsResponseTypeDef,
    ListTrialsResponseTypeDef,
    ListUserProfilesResponseTypeDef,
    ListWorkforcesResponseTypeDef,
    ListWorkteamsResponseTypeDef,
    MemberDefinitionTypeDef,
    MetadataPropertiesTypeDef,
    ModelBiasAppSpecificationTypeDef,
    ModelBiasBaselineConfigTypeDef,
    ModelBiasJobInputTypeDef,
    ModelClientConfigTypeDef,
    ModelDeployConfigTypeDef,
    ModelExplainabilityAppSpecificationTypeDef,
    ModelExplainabilityBaselineConfigTypeDef,
    ModelExplainabilityJobInputTypeDef,
    ModelMetricsTypeDef,
    ModelPackageValidationSpecificationTypeDef,
    ModelQualityAppSpecificationTypeDef,
    ModelQualityBaselineConfigTypeDef,
    ModelQualityJobInputTypeDef,
    MonitoringNetworkConfigTypeDef,
    MonitoringOutputConfigTypeDef,
    MonitoringResourcesTypeDef,
    MonitoringScheduleConfigTypeDef,
    MonitoringStoppingConditionTypeDef,
    NetworkConfigTypeDef,
    NotebookInstanceLifecycleHookTypeDef,
    NotificationConfigurationTypeDef,
    OfflineStoreConfigTypeDef,
    OidcConfigTypeDef,
    OnlineStoreConfigTypeDef,
    OutputConfigTypeDef,
    OutputDataConfigTypeDef,
    ParameterTypeDef,
    ProcessingInputTypeDef,
    ProcessingOutputConfigTypeDef,
    ProcessingResourcesTypeDef,
    ProcessingStoppingConditionTypeDef,
    ProductionVariantTypeDef,
    ProfilerConfigForUpdateTypeDef,
    ProfilerConfigTypeDef,
    ProfilerRuleConfigurationTypeDef,
    PutModelPackageGroupPolicyOutputTypeDef,
    RenderableTaskTypeDef,
    RenderUiTemplateResponseTypeDef,
    ResourceConfigTypeDef,
    ResourceSpecTypeDef,
    RetentionPolicyTypeDef,
    RetryStrategyTypeDef,
    SearchExpressionTypeDef,
    SearchResponseTypeDef,
    ServiceCatalogProvisioningDetailsTypeDef,
    SourceAlgorithmSpecificationTypeDef,
    SourceIpConfigTypeDef,
    StartPipelineExecutionResponseTypeDef,
    StoppingConditionTypeDef,
    StopPipelineExecutionResponseTypeDef,
    SuggestionQueryTypeDef,
    TagTypeDef,
    TensorBoardOutputConfigTypeDef,
    TrainingSpecificationTypeDef,
    TransformInputTypeDef,
    TransformOutputTypeDef,
    TransformResourcesTypeDef,
    TrialComponentArtifactTypeDef,
    TrialComponentParameterValueTypeDef,
    TrialComponentStatusTypeDef,
    UiTemplateTypeDef,
    UpdateActionResponseTypeDef,
    UpdateAppImageConfigResponseTypeDef,
    UpdateArtifactResponseTypeDef,
    UpdateCodeRepositoryOutputTypeDef,
    UpdateContextResponseTypeDef,
    UpdateDomainResponseTypeDef,
    UpdateEndpointOutputTypeDef,
    UpdateEndpointWeightsAndCapacitiesOutputTypeDef,
    UpdateExperimentResponseTypeDef,
    UpdateImageResponseTypeDef,
    UpdateModelPackageOutputTypeDef,
    UpdateMonitoringScheduleResponseTypeDef,
    UpdatePipelineExecutionResponseTypeDef,
    UpdatePipelineResponseTypeDef,
    UpdateTrainingJobResponseTypeDef,
    UpdateTrialComponentResponseTypeDef,
    UpdateTrialResponseTypeDef,
    UpdateUserProfileResponseTypeDef,
    UpdateWorkforceResponseTypeDef,
    UpdateWorkteamResponseTypeDef,
    UserSettingsTypeDef,
    VariantPropertyTypeDef,
    VpcConfigTypeDef,
)
from mypy_boto3_sagemaker.waiter import (
    EndpointDeletedWaiter,
    EndpointInServiceWaiter,
    NotebookInstanceDeletedWaiter,
    NotebookInstanceInServiceWaiter,
    NotebookInstanceStoppedWaiter,
    ProcessingJobCompletedOrStoppedWaiter,
    TrainingJobCompletedOrStoppedWaiter,
    TransformJobCompletedOrStoppedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SageMakerClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ResourceInUse: Type[BotocoreClientError]
    ResourceLimitExceeded: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]


class SageMakerClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_association(
        self, SourceArn: str, DestinationArn: str, AssociationType: AssociationEdgeType = None
    ) -> AddAssociationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.add_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#add-association)
        """

    def add_tags(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> AddTagsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.add_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#add-tags)
        """

    def associate_trial_component(
        self, TrialComponentName: str, TrialName: str
    ) -> AssociateTrialComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.associate_trial_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#associate-trial-component)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#can-paginate)
        """

    def create_action(
        self,
        ActionName: str,
        Source: "ActionSourceTypeDef",
        ActionType: str,
        Description: str = None,
        Status: ActionStatus = None,
        Properties: Dict[str, str] = None,
        MetadataProperties: "MetadataPropertiesTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateActionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-action)
        """

    def create_algorithm(
        self,
        AlgorithmName: str,
        TrainingSpecification: "TrainingSpecificationTypeDef",
        AlgorithmDescription: str = None,
        InferenceSpecification: "InferenceSpecificationTypeDef" = None,
        ValidationSpecification: "AlgorithmValidationSpecificationTypeDef" = None,
        CertifyForMarketplace: bool = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateAlgorithmOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_algorithm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-algorithm)
        """

    def create_app(
        self,
        DomainId: str,
        UserProfileName: str,
        AppType: AppType,
        AppName: str,
        Tags: List["TagTypeDef"] = None,
        ResourceSpec: "ResourceSpecTypeDef" = None,
    ) -> CreateAppResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-app)
        """

    def create_app_image_config(
        self,
        AppImageConfigName: str,
        Tags: List["TagTypeDef"] = None,
        KernelGatewayImageConfig: "KernelGatewayImageConfigTypeDef" = None,
    ) -> CreateAppImageConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_app_image_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-app-image-config)
        """

    def create_artifact(
        self,
        Source: "ArtifactSourceTypeDef",
        ArtifactType: str,
        ArtifactName: str = None,
        Properties: Dict[str, str] = None,
        MetadataProperties: "MetadataPropertiesTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateArtifactResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-artifact)
        """

    def create_auto_ml_job(
        self,
        AutoMLJobName: str,
        InputDataConfig: List["AutoMLChannelTypeDef"],
        OutputDataConfig: "AutoMLOutputDataConfigTypeDef",
        RoleArn: str,
        ProblemType: ProblemType = None,
        AutoMLJobObjective: "AutoMLJobObjectiveTypeDef" = None,
        AutoMLJobConfig: "AutoMLJobConfigTypeDef" = None,
        GenerateCandidateDefinitionsOnly: bool = None,
        Tags: List["TagTypeDef"] = None,
        ModelDeployConfig: "ModelDeployConfigTypeDef" = None,
    ) -> CreateAutoMLJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_auto_ml_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-auto-ml-job)
        """

    def create_code_repository(
        self,
        CodeRepositoryName: str,
        GitConfig: "GitConfigTypeDef",
        Tags: List["TagTypeDef"] = None,
    ) -> CreateCodeRepositoryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_code_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-code-repository)
        """

    def create_compilation_job(
        self,
        CompilationJobName: str,
        RoleArn: str,
        InputConfig: "InputConfigTypeDef",
        OutputConfig: "OutputConfigTypeDef",
        StoppingCondition: "StoppingConditionTypeDef",
        Tags: List["TagTypeDef"] = None,
    ) -> CreateCompilationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_compilation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-compilation-job)
        """

    def create_context(
        self,
        ContextName: str,
        Source: "ContextSourceTypeDef",
        ContextType: str,
        Description: str = None,
        Properties: Dict[str, str] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateContextResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_context)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-context)
        """

    def create_data_quality_job_definition(
        self,
        JobDefinitionName: str,
        DataQualityAppSpecification: "DataQualityAppSpecificationTypeDef",
        DataQualityJobInput: "DataQualityJobInputTypeDef",
        DataQualityJobOutputConfig: "MonitoringOutputConfigTypeDef",
        JobResources: "MonitoringResourcesTypeDef",
        RoleArn: str,
        DataQualityBaselineConfig: "DataQualityBaselineConfigTypeDef" = None,
        NetworkConfig: "MonitoringNetworkConfigTypeDef" = None,
        StoppingCondition: "MonitoringStoppingConditionTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateDataQualityJobDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_data_quality_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-data-quality-job-definition)
        """

    def create_device_fleet(
        self,
        DeviceFleetName: str,
        OutputConfig: "EdgeOutputConfigTypeDef",
        RoleArn: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_device_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-device-fleet)
        """

    def create_domain(
        self,
        DomainName: str,
        AuthMode: AuthMode,
        DefaultUserSettings: "UserSettingsTypeDef",
        SubnetIds: List[str],
        VpcId: str,
        Tags: List["TagTypeDef"] = None,
        AppNetworkAccessType: AppNetworkAccessType = None,
        HomeEfsFileSystemKmsKeyId: str = None,
        KmsKeyId: str = None,
    ) -> CreateDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-domain)
        """

    def create_edge_packaging_job(
        self,
        EdgePackagingJobName: str,
        CompilationJobName: str,
        ModelName: str,
        ModelVersion: str,
        RoleArn: str,
        OutputConfig: "EdgeOutputConfigTypeDef",
        ResourceKey: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_edge_packaging_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-edge-packaging-job)
        """

    def create_endpoint(
        self, EndpointName: str, EndpointConfigName: str, Tags: List["TagTypeDef"] = None
    ) -> CreateEndpointOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-endpoint)
        """

    def create_endpoint_config(
        self,
        EndpointConfigName: str,
        ProductionVariants: List["ProductionVariantTypeDef"],
        DataCaptureConfig: "DataCaptureConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        KmsKeyId: str = None,
    ) -> CreateEndpointConfigOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_endpoint_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-endpoint-config)
        """

    def create_experiment(
        self,
        ExperimentName: str,
        DisplayName: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateExperimentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-experiment)
        """

    def create_feature_group(
        self,
        FeatureGroupName: str,
        RecordIdentifierFeatureName: str,
        EventTimeFeatureName: str,
        FeatureDefinitions: List["FeatureDefinitionTypeDef"],
        OnlineStoreConfig: "OnlineStoreConfigTypeDef" = None,
        OfflineStoreConfig: "OfflineStoreConfigTypeDef" = None,
        RoleArn: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateFeatureGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_feature_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-feature-group)
        """

    def create_flow_definition(
        self,
        FlowDefinitionName: str,
        HumanLoopConfig: "HumanLoopConfigTypeDef",
        OutputConfig: "FlowDefinitionOutputConfigTypeDef",
        RoleArn: str,
        HumanLoopRequestSource: "HumanLoopRequestSourceTypeDef" = None,
        HumanLoopActivationConfig: "HumanLoopActivationConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateFlowDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_flow_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-flow-definition)
        """

    def create_human_task_ui(
        self, HumanTaskUiName: str, UiTemplate: UiTemplateTypeDef, Tags: List["TagTypeDef"] = None
    ) -> CreateHumanTaskUiResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_human_task_ui)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-human-task-ui)
        """

    def create_hyper_parameter_tuning_job(
        self,
        HyperParameterTuningJobName: str,
        HyperParameterTuningJobConfig: "HyperParameterTuningJobConfigTypeDef",
        TrainingJobDefinition: "HyperParameterTrainingJobDefinitionTypeDef" = None,
        TrainingJobDefinitions: List["HyperParameterTrainingJobDefinitionTypeDef"] = None,
        WarmStartConfig: "HyperParameterTuningJobWarmStartConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateHyperParameterTuningJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_hyper_parameter_tuning_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-hyper-parameter-tuning-job)
        """

    def create_image(
        self,
        ImageName: str,
        RoleArn: str,
        Description: str = None,
        DisplayName: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-image)
        """

    def create_image_version(
        self, BaseImage: str, ClientToken: str, ImageName: str
    ) -> CreateImageVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_image_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-image-version)
        """

    def create_labeling_job(
        self,
        LabelingJobName: str,
        LabelAttributeName: str,
        InputConfig: "LabelingJobInputConfigTypeDef",
        OutputConfig: "LabelingJobOutputConfigTypeDef",
        RoleArn: str,
        HumanTaskConfig: "HumanTaskConfigTypeDef",
        LabelCategoryConfigS3Uri: str = None,
        StoppingConditions: "LabelingJobStoppingConditionsTypeDef" = None,
        LabelingJobAlgorithmsConfig: "LabelingJobAlgorithmsConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateLabelingJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_labeling_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-labeling-job)
        """

    def create_model(
        self,
        ModelName: str,
        ExecutionRoleArn: str,
        PrimaryContainer: "ContainerDefinitionTypeDef" = None,
        Containers: List["ContainerDefinitionTypeDef"] = None,
        InferenceExecutionConfig: "InferenceExecutionConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        EnableNetworkIsolation: bool = None,
    ) -> CreateModelOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-model)
        """

    def create_model_bias_job_definition(
        self,
        JobDefinitionName: str,
        ModelBiasAppSpecification: "ModelBiasAppSpecificationTypeDef",
        ModelBiasJobInput: "ModelBiasJobInputTypeDef",
        ModelBiasJobOutputConfig: "MonitoringOutputConfigTypeDef",
        JobResources: "MonitoringResourcesTypeDef",
        RoleArn: str,
        ModelBiasBaselineConfig: "ModelBiasBaselineConfigTypeDef" = None,
        NetworkConfig: "MonitoringNetworkConfigTypeDef" = None,
        StoppingCondition: "MonitoringStoppingConditionTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateModelBiasJobDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_model_bias_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-model-bias-job-definition)
        """

    def create_model_explainability_job_definition(
        self,
        JobDefinitionName: str,
        ModelExplainabilityAppSpecification: "ModelExplainabilityAppSpecificationTypeDef",
        ModelExplainabilityJobInput: "ModelExplainabilityJobInputTypeDef",
        ModelExplainabilityJobOutputConfig: "MonitoringOutputConfigTypeDef",
        JobResources: "MonitoringResourcesTypeDef",
        RoleArn: str,
        ModelExplainabilityBaselineConfig: "ModelExplainabilityBaselineConfigTypeDef" = None,
        NetworkConfig: "MonitoringNetworkConfigTypeDef" = None,
        StoppingCondition: "MonitoringStoppingConditionTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateModelExplainabilityJobDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_model_explainability_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-model-explainability-job-definition)
        """

    def create_model_package(
        self,
        ModelPackageName: str = None,
        ModelPackageGroupName: str = None,
        ModelPackageDescription: str = None,
        InferenceSpecification: "InferenceSpecificationTypeDef" = None,
        ValidationSpecification: "ModelPackageValidationSpecificationTypeDef" = None,
        SourceAlgorithmSpecification: "SourceAlgorithmSpecificationTypeDef" = None,
        CertifyForMarketplace: bool = None,
        Tags: List["TagTypeDef"] = None,
        ModelApprovalStatus: ModelApprovalStatus = None,
        MetadataProperties: "MetadataPropertiesTypeDef" = None,
        ModelMetrics: "ModelMetricsTypeDef" = None,
        ClientToken: str = None,
    ) -> CreateModelPackageOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_model_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-model-package)
        """

    def create_model_package_group(
        self,
        ModelPackageGroupName: str,
        ModelPackageGroupDescription: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateModelPackageGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_model_package_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-model-package-group)
        """

    def create_model_quality_job_definition(
        self,
        JobDefinitionName: str,
        ModelQualityAppSpecification: "ModelQualityAppSpecificationTypeDef",
        ModelQualityJobInput: "ModelQualityJobInputTypeDef",
        ModelQualityJobOutputConfig: "MonitoringOutputConfigTypeDef",
        JobResources: "MonitoringResourcesTypeDef",
        RoleArn: str,
        ModelQualityBaselineConfig: "ModelQualityBaselineConfigTypeDef" = None,
        NetworkConfig: "MonitoringNetworkConfigTypeDef" = None,
        StoppingCondition: "MonitoringStoppingConditionTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateModelQualityJobDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_model_quality_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-model-quality-job-definition)
        """

    def create_monitoring_schedule(
        self,
        MonitoringScheduleName: str,
        MonitoringScheduleConfig: "MonitoringScheduleConfigTypeDef",
        Tags: List["TagTypeDef"] = None,
    ) -> CreateMonitoringScheduleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_monitoring_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-monitoring-schedule)
        """

    def create_notebook_instance(
        self,
        NotebookInstanceName: str,
        InstanceType: InstanceType,
        RoleArn: str,
        SubnetId: str = None,
        SecurityGroupIds: List[str] = None,
        KmsKeyId: str = None,
        Tags: List["TagTypeDef"] = None,
        LifecycleConfigName: str = None,
        DirectInternetAccess: DirectInternetAccess = None,
        VolumeSizeInGB: int = None,
        AcceleratorTypes: List[NotebookInstanceAcceleratorType] = None,
        DefaultCodeRepository: str = None,
        AdditionalCodeRepositories: List[str] = None,
        RootAccess: RootAccess = None,
    ) -> CreateNotebookInstanceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_notebook_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-notebook-instance)
        """

    def create_notebook_instance_lifecycle_config(
        self,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: List["NotebookInstanceLifecycleHookTypeDef"] = None,
        OnStart: List["NotebookInstanceLifecycleHookTypeDef"] = None,
    ) -> CreateNotebookInstanceLifecycleConfigOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_notebook_instance_lifecycle_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-notebook-instance-lifecycle-config)
        """

    def create_pipeline(
        self,
        PipelineName: str,
        PipelineDefinition: str,
        ClientRequestToken: str,
        RoleArn: str,
        PipelineDisplayName: str = None,
        PipelineDescription: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreatePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-pipeline)
        """

    def create_presigned_domain_url(
        self,
        DomainId: str,
        UserProfileName: str,
        SessionExpirationDurationInSeconds: int = None,
        ExpiresInSeconds: int = None,
    ) -> CreatePresignedDomainUrlResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_presigned_domain_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-presigned-domain-url)
        """

    def create_presigned_notebook_instance_url(
        self, NotebookInstanceName: str, SessionExpirationDurationInSeconds: int = None
    ) -> CreatePresignedNotebookInstanceUrlOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_presigned_notebook_instance_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-presigned-notebook-instance-url)
        """

    def create_processing_job(
        self,
        ProcessingJobName: str,
        ProcessingResources: "ProcessingResourcesTypeDef",
        AppSpecification: "AppSpecificationTypeDef",
        RoleArn: str,
        ProcessingInputs: List["ProcessingInputTypeDef"] = None,
        ProcessingOutputConfig: "ProcessingOutputConfigTypeDef" = None,
        StoppingCondition: "ProcessingStoppingConditionTypeDef" = None,
        Environment: Dict[str, str] = None,
        NetworkConfig: "NetworkConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        ExperimentConfig: "ExperimentConfigTypeDef" = None,
    ) -> CreateProcessingJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_processing_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-processing-job)
        """

    def create_project(
        self,
        ProjectName: str,
        ServiceCatalogProvisioningDetails: "ServiceCatalogProvisioningDetailsTypeDef",
        ProjectDescription: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateProjectOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-project)
        """

    def create_training_job(
        self,
        TrainingJobName: str,
        AlgorithmSpecification: "AlgorithmSpecificationTypeDef",
        RoleArn: str,
        OutputDataConfig: "OutputDataConfigTypeDef",
        ResourceConfig: "ResourceConfigTypeDef",
        StoppingCondition: "StoppingConditionTypeDef",
        HyperParameters: Dict[str, str] = None,
        InputDataConfig: List["ChannelTypeDef"] = None,
        VpcConfig: "VpcConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        EnableNetworkIsolation: bool = None,
        EnableInterContainerTrafficEncryption: bool = None,
        EnableManagedSpotTraining: bool = None,
        CheckpointConfig: "CheckpointConfigTypeDef" = None,
        DebugHookConfig: "DebugHookConfigTypeDef" = None,
        DebugRuleConfigurations: List["DebugRuleConfigurationTypeDef"] = None,
        TensorBoardOutputConfig: "TensorBoardOutputConfigTypeDef" = None,
        ExperimentConfig: "ExperimentConfigTypeDef" = None,
        ProfilerConfig: "ProfilerConfigTypeDef" = None,
        ProfilerRuleConfigurations: List["ProfilerRuleConfigurationTypeDef"] = None,
        Environment: Dict[str, str] = None,
        RetryStrategy: "RetryStrategyTypeDef" = None,
    ) -> CreateTrainingJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_training_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-training-job)
        """

    def create_transform_job(
        self,
        TransformJobName: str,
        ModelName: str,
        TransformInput: "TransformInputTypeDef",
        TransformOutput: "TransformOutputTypeDef",
        TransformResources: "TransformResourcesTypeDef",
        MaxConcurrentTransforms: int = None,
        ModelClientConfig: "ModelClientConfigTypeDef" = None,
        MaxPayloadInMB: int = None,
        BatchStrategy: BatchStrategy = None,
        Environment: Dict[str, str] = None,
        DataProcessing: "DataProcessingTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
        ExperimentConfig: "ExperimentConfigTypeDef" = None,
    ) -> CreateTransformJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_transform_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-transform-job)
        """

    def create_trial(
        self,
        TrialName: str,
        ExperimentName: str,
        DisplayName: str = None,
        MetadataProperties: "MetadataPropertiesTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateTrialResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_trial)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-trial)
        """

    def create_trial_component(
        self,
        TrialComponentName: str,
        DisplayName: str = None,
        Status: "TrialComponentStatusTypeDef" = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Parameters: Dict[str, "TrialComponentParameterValueTypeDef"] = None,
        InputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
        OutputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
        MetadataProperties: "MetadataPropertiesTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateTrialComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_trial_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-trial-component)
        """

    def create_user_profile(
        self,
        DomainId: str,
        UserProfileName: str,
        SingleSignOnUserIdentifier: str = None,
        SingleSignOnUserValue: str = None,
        Tags: List["TagTypeDef"] = None,
        UserSettings: "UserSettingsTypeDef" = None,
    ) -> CreateUserProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-user-profile)
        """

    def create_workforce(
        self,
        WorkforceName: str,
        CognitoConfig: "CognitoConfigTypeDef" = None,
        OidcConfig: OidcConfigTypeDef = None,
        SourceIpConfig: "SourceIpConfigTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateWorkforceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_workforce)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-workforce)
        """

    def create_workteam(
        self,
        WorkteamName: str,
        MemberDefinitions: List["MemberDefinitionTypeDef"],
        Description: str,
        WorkforceName: str = None,
        NotificationConfiguration: "NotificationConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateWorkteamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.create_workteam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#create-workteam)
        """

    def delete_action(self, ActionName: str) -> DeleteActionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-action)
        """

    def delete_algorithm(self, AlgorithmName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_algorithm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-algorithm)
        """

    def delete_app(
        self, DomainId: str, UserProfileName: str, AppType: AppType, AppName: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-app)
        """

    def delete_app_image_config(self, AppImageConfigName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_app_image_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-app-image-config)
        """

    def delete_artifact(
        self, ArtifactArn: str = None, Source: "ArtifactSourceTypeDef" = None
    ) -> DeleteArtifactResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-artifact)
        """

    def delete_association(
        self, SourceArn: str, DestinationArn: str
    ) -> DeleteAssociationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-association)
        """

    def delete_code_repository(self, CodeRepositoryName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_code_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-code-repository)
        """

    def delete_context(self, ContextName: str) -> DeleteContextResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_context)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-context)
        """

    def delete_data_quality_job_definition(self, JobDefinitionName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_data_quality_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-data-quality-job-definition)
        """

    def delete_device_fleet(self, DeviceFleetName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_device_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-device-fleet)
        """

    def delete_domain(self, DomainId: str, RetentionPolicy: RetentionPolicyTypeDef = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-domain)
        """

    def delete_endpoint(self, EndpointName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-endpoint)
        """

    def delete_endpoint_config(self, EndpointConfigName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_endpoint_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-endpoint-config)
        """

    def delete_experiment(self, ExperimentName: str) -> DeleteExperimentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-experiment)
        """

    def delete_feature_group(self, FeatureGroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_feature_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-feature-group)
        """

    def delete_flow_definition(self, FlowDefinitionName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_flow_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-flow-definition)
        """

    def delete_human_task_ui(self, HumanTaskUiName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_human_task_ui)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-human-task-ui)
        """

    def delete_image(self, ImageName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-image)
        """

    def delete_image_version(self, ImageName: str, Version: int) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_image_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-image-version)
        """

    def delete_model(self, ModelName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-model)
        """

    def delete_model_bias_job_definition(self, JobDefinitionName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_model_bias_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-model-bias-job-definition)
        """

    def delete_model_explainability_job_definition(self, JobDefinitionName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_model_explainability_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-model-explainability-job-definition)
        """

    def delete_model_package(self, ModelPackageName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_model_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-model-package)
        """

    def delete_model_package_group(self, ModelPackageGroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_model_package_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-model-package-group)
        """

    def delete_model_package_group_policy(self, ModelPackageGroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_model_package_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-model-package-group-policy)
        """

    def delete_model_quality_job_definition(self, JobDefinitionName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_model_quality_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-model-quality-job-definition)
        """

    def delete_monitoring_schedule(self, MonitoringScheduleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_monitoring_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-monitoring-schedule)
        """

    def delete_notebook_instance(self, NotebookInstanceName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_notebook_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-notebook-instance)
        """

    def delete_notebook_instance_lifecycle_config(
        self, NotebookInstanceLifecycleConfigName: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_notebook_instance_lifecycle_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-notebook-instance-lifecycle-config)
        """

    def delete_pipeline(
        self, PipelineName: str, ClientRequestToken: str
    ) -> DeletePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-pipeline)
        """

    def delete_project(self, ProjectName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-project)
        """

    def delete_tags(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-tags)
        """

    def delete_trial(self, TrialName: str) -> DeleteTrialResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_trial)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-trial)
        """

    def delete_trial_component(
        self, TrialComponentName: str
    ) -> DeleteTrialComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_trial_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-trial-component)
        """

    def delete_user_profile(self, DomainId: str, UserProfileName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-user-profile)
        """

    def delete_workforce(self, WorkforceName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_workforce)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-workforce)
        """

    def delete_workteam(self, WorkteamName: str) -> DeleteWorkteamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.delete_workteam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#delete-workteam)
        """

    def deregister_devices(self, DeviceFleetName: str, DeviceNames: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.deregister_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#deregister-devices)
        """

    def describe_action(self, ActionName: str) -> DescribeActionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-action)
        """

    def describe_algorithm(self, AlgorithmName: str) -> DescribeAlgorithmOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_algorithm)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-algorithm)
        """

    def describe_app(
        self, DomainId: str, UserProfileName: str, AppType: AppType, AppName: str
    ) -> DescribeAppResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_app)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-app)
        """

    def describe_app_image_config(
        self, AppImageConfigName: str
    ) -> DescribeAppImageConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_app_image_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-app-image-config)
        """

    def describe_artifact(self, ArtifactArn: str) -> DescribeArtifactResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-artifact)
        """

    def describe_auto_ml_job(self, AutoMLJobName: str) -> DescribeAutoMLJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_auto_ml_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-auto-ml-job)
        """

    def describe_code_repository(
        self, CodeRepositoryName: str
    ) -> DescribeCodeRepositoryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_code_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-code-repository)
        """

    def describe_compilation_job(
        self, CompilationJobName: str
    ) -> DescribeCompilationJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_compilation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-compilation-job)
        """

    def describe_context(self, ContextName: str) -> DescribeContextResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_context)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-context)
        """

    def describe_data_quality_job_definition(
        self, JobDefinitionName: str
    ) -> DescribeDataQualityJobDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_data_quality_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-data-quality-job-definition)
        """

    def describe_device(
        self, DeviceName: str, DeviceFleetName: str, NextToken: str = None
    ) -> DescribeDeviceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-device)
        """

    def describe_device_fleet(self, DeviceFleetName: str) -> DescribeDeviceFleetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_device_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-device-fleet)
        """

    def describe_domain(self, DomainId: str) -> DescribeDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-domain)
        """

    def describe_edge_packaging_job(
        self, EdgePackagingJobName: str
    ) -> DescribeEdgePackagingJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_edge_packaging_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-edge-packaging-job)
        """

    def describe_endpoint(self, EndpointName: str) -> DescribeEndpointOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-endpoint)
        """

    def describe_endpoint_config(
        self, EndpointConfigName: str
    ) -> DescribeEndpointConfigOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_endpoint_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-endpoint-config)
        """

    def describe_experiment(self, ExperimentName: str) -> DescribeExperimentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-experiment)
        """

    def describe_feature_group(
        self, FeatureGroupName: str, NextToken: str = None
    ) -> DescribeFeatureGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_feature_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-feature-group)
        """

    def describe_flow_definition(
        self, FlowDefinitionName: str
    ) -> DescribeFlowDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_flow_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-flow-definition)
        """

    def describe_human_task_ui(self, HumanTaskUiName: str) -> DescribeHumanTaskUiResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_human_task_ui)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-human-task-ui)
        """

    def describe_hyper_parameter_tuning_job(
        self, HyperParameterTuningJobName: str
    ) -> DescribeHyperParameterTuningJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_hyper_parameter_tuning_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-hyper-parameter-tuning-job)
        """

    def describe_image(self, ImageName: str) -> DescribeImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-image)
        """

    def describe_image_version(
        self, ImageName: str, Version: int = None
    ) -> DescribeImageVersionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_image_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-image-version)
        """

    def describe_labeling_job(self, LabelingJobName: str) -> DescribeLabelingJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_labeling_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-labeling-job)
        """

    def describe_model(self, ModelName: str) -> DescribeModelOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_model)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-model)
        """

    def describe_model_bias_job_definition(
        self, JobDefinitionName: str
    ) -> DescribeModelBiasJobDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_model_bias_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-model-bias-job-definition)
        """

    def describe_model_explainability_job_definition(
        self, JobDefinitionName: str
    ) -> DescribeModelExplainabilityJobDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_model_explainability_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-model-explainability-job-definition)
        """

    def describe_model_package(self, ModelPackageName: str) -> DescribeModelPackageOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_model_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-model-package)
        """

    def describe_model_package_group(
        self, ModelPackageGroupName: str
    ) -> DescribeModelPackageGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_model_package_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-model-package-group)
        """

    def describe_model_quality_job_definition(
        self, JobDefinitionName: str
    ) -> DescribeModelQualityJobDefinitionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_model_quality_job_definition)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-model-quality-job-definition)
        """

    def describe_monitoring_schedule(
        self, MonitoringScheduleName: str
    ) -> DescribeMonitoringScheduleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_monitoring_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-monitoring-schedule)
        """

    def describe_notebook_instance(
        self, NotebookInstanceName: str
    ) -> DescribeNotebookInstanceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_notebook_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-notebook-instance)
        """

    def describe_notebook_instance_lifecycle_config(
        self, NotebookInstanceLifecycleConfigName: str
    ) -> DescribeNotebookInstanceLifecycleConfigOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_notebook_instance_lifecycle_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-notebook-instance-lifecycle-config)
        """

    def describe_pipeline(self, PipelineName: str) -> DescribePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-pipeline)
        """

    def describe_pipeline_definition_for_execution(
        self, PipelineExecutionArn: str
    ) -> DescribePipelineDefinitionForExecutionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_pipeline_definition_for_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-pipeline-definition-for-execution)
        """

    def describe_pipeline_execution(
        self, PipelineExecutionArn: str
    ) -> DescribePipelineExecutionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-pipeline-execution)
        """

    def describe_processing_job(
        self, ProcessingJobName: str
    ) -> DescribeProcessingJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_processing_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-processing-job)
        """

    def describe_project(self, ProjectName: str) -> DescribeProjectOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-project)
        """

    def describe_subscribed_workteam(
        self, WorkteamArn: str
    ) -> DescribeSubscribedWorkteamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_subscribed_workteam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-subscribed-workteam)
        """

    def describe_training_job(self, TrainingJobName: str) -> DescribeTrainingJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_training_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-training-job)
        """

    def describe_transform_job(self, TransformJobName: str) -> DescribeTransformJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_transform_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-transform-job)
        """

    def describe_trial(self, TrialName: str) -> DescribeTrialResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_trial)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-trial)
        """

    def describe_trial_component(
        self, TrialComponentName: str
    ) -> DescribeTrialComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_trial_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-trial-component)
        """

    def describe_user_profile(
        self, DomainId: str, UserProfileName: str
    ) -> DescribeUserProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-user-profile)
        """

    def describe_workforce(self, WorkforceName: str) -> DescribeWorkforceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_workforce)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-workforce)
        """

    def describe_workteam(self, WorkteamName: str) -> DescribeWorkteamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.describe_workteam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#describe-workteam)
        """

    def disable_sagemaker_servicecatalog_portfolio(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.disable_sagemaker_servicecatalog_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#disable-sagemaker-servicecatalog-portfolio)
        """

    def disassociate_trial_component(
        self, TrialComponentName: str, TrialName: str
    ) -> DisassociateTrialComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.disassociate_trial_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#disassociate-trial-component)
        """

    def enable_sagemaker_servicecatalog_portfolio(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.enable_sagemaker_servicecatalog_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#enable-sagemaker-servicecatalog-portfolio)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#generate-presigned-url)
        """

    def get_device_fleet_report(self, DeviceFleetName: str) -> GetDeviceFleetReportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.get_device_fleet_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#get-device-fleet-report)
        """

    def get_model_package_group_policy(
        self, ModelPackageGroupName: str
    ) -> GetModelPackageGroupPolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.get_model_package_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#get-model-package-group-policy)
        """

    def get_sagemaker_servicecatalog_portfolio_status(
        self,
    ) -> GetSagemakerServicecatalogPortfolioStatusOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.get_sagemaker_servicecatalog_portfolio_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#get-sagemaker-servicecatalog-portfolio-status)
        """

    def get_search_suggestions(
        self, Resource: ResourceType, SuggestionQuery: SuggestionQueryTypeDef = None
    ) -> GetSearchSuggestionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.get_search_suggestions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#get-search-suggestions)
        """

    def list_actions(
        self,
        SourceUri: str = None,
        ActionType: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortActionsBy = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListActionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-actions)
        """

    def list_algorithms(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: AlgorithmSortBy = None,
        SortOrder: SortOrder = None,
    ) -> ListAlgorithmsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_algorithms)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-algorithms)
        """

    def list_app_image_configs(
        self,
        MaxResults: int = None,
        NextToken: str = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        ModifiedTimeBefore: datetime = None,
        ModifiedTimeAfter: datetime = None,
        SortBy: AppImageConfigSortKey = None,
        SortOrder: SortOrder = None,
    ) -> ListAppImageConfigsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_app_image_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-app-image-configs)
        """

    def list_apps(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        SortOrder: SortOrder = None,
        SortBy: Literal["CreationTime"] = None,
        DomainIdEquals: str = None,
        UserProfileNameEquals: str = None,
    ) -> ListAppsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_apps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-apps)
        """

    def list_artifacts(
        self,
        SourceUri: str = None,
        ArtifactType: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: Literal["CreationTime"] = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListArtifactsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_artifacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-artifacts)
        """

    def list_associations(
        self,
        SourceArn: str = None,
        DestinationArn: str = None,
        SourceType: str = None,
        DestinationType: str = None,
        AssociationType: AssociationEdgeType = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortAssociationsBy = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListAssociationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-associations)
        """

    def list_auto_ml_jobs(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: AutoMLJobStatus = None,
        SortOrder: AutoMLSortOrder = None,
        SortBy: AutoMLSortBy = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListAutoMLJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_auto_ml_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-auto-ml-jobs)
        """

    def list_candidates_for_auto_ml_job(
        self,
        AutoMLJobName: str,
        StatusEquals: CandidateStatus = None,
        CandidateNameEquals: str = None,
        SortOrder: AutoMLSortOrder = None,
        SortBy: CandidateSortBy = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListCandidatesForAutoMLJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_candidates_for_auto_ml_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-candidates-for-auto-ml-job)
        """

    def list_code_repositories(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: CodeRepositorySortBy = None,
        SortOrder: CodeRepositorySortOrder = None,
    ) -> ListCodeRepositoriesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_code_repositories)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-code-repositories)
        """

    def list_compilation_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: CompilationJobStatus = None,
        SortBy: ListCompilationJobsSortBy = None,
        SortOrder: SortOrder = None,
    ) -> ListCompilationJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_compilation_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-compilation-jobs)
        """

    def list_contexts(
        self,
        SourceUri: str = None,
        ContextType: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortContextsBy = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListContextsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_contexts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-contexts)
        """

    def list_data_quality_job_definitions(
        self,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKey = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
    ) -> ListDataQualityJobDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_data_quality_job_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-data-quality-job-definitions)
        """

    def list_device_fleets(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: ListDeviceFleetsSortBy = None,
        SortOrder: SortOrder = None,
    ) -> ListDeviceFleetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_device_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-device-fleets)
        """

    def list_devices(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        LatestHeartbeatAfter: datetime = None,
        ModelName: str = None,
        DeviceFleetName: str = None,
    ) -> ListDevicesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-devices)
        """

    def list_domains(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListDomainsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-domains)
        """

    def list_edge_packaging_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        ModelNameContains: str = None,
        StatusEquals: EdgePackagingJobStatus = None,
        SortBy: ListEdgePackagingJobsSortBy = None,
        SortOrder: SortOrder = None,
    ) -> ListEdgePackagingJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_edge_packaging_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-edge-packaging-jobs)
        """

    def list_endpoint_configs(
        self,
        SortBy: EndpointConfigSortKey = None,
        SortOrder: OrderKey = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
    ) -> ListEndpointConfigsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_endpoint_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-endpoint-configs)
        """

    def list_endpoints(
        self,
        SortBy: EndpointSortKey = None,
        SortOrder: OrderKey = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: EndpointStatus = None,
    ) -> ListEndpointsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-endpoints)
        """

    def list_experiments(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortExperimentsBy = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListExperimentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_experiments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-experiments)
        """

    def list_feature_groups(
        self,
        NameContains: str = None,
        FeatureGroupStatusEquals: FeatureGroupStatus = None,
        OfflineStoreStatusEquals: OfflineStoreStatusValue = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: FeatureGroupSortOrder = None,
        SortBy: FeatureGroupSortBy = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListFeatureGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_feature_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-feature-groups)
        """

    def list_flow_definitions(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListFlowDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_flow_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-flow-definitions)
        """

    def list_human_task_uis(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListHumanTaskUisResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_human_task_uis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-human-task-uis)
        """

    def list_hyper_parameter_tuning_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        SortBy: HyperParameterTuningJobSortByOptions = None,
        SortOrder: SortOrder = None,
        NameContains: str = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        StatusEquals: HyperParameterTuningJobStatus = None,
    ) -> ListHyperParameterTuningJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_hyper_parameter_tuning_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-hyper-parameter-tuning-jobs)
        """

    def list_image_versions(
        self,
        ImageName: str,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        MaxResults: int = None,
        NextToken: str = None,
        SortBy: ImageVersionSortBy = None,
        SortOrder: ImageVersionSortOrder = None,
    ) -> ListImageVersionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_image_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-image-versions)
        """

    def list_images(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: ImageSortBy = None,
        SortOrder: ImageSortOrder = None,
    ) -> ListImagesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-images)
        """

    def list_labeling_jobs(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        MaxResults: int = None,
        NextToken: str = None,
        NameContains: str = None,
        SortBy: SortBy = None,
        SortOrder: SortOrder = None,
        StatusEquals: LabelingJobStatus = None,
    ) -> ListLabelingJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_labeling_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-labeling-jobs)
        """

    def list_labeling_jobs_for_workteam(
        self,
        WorkteamArn: str,
        MaxResults: int = None,
        NextToken: str = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        JobReferenceCodeContains: str = None,
        SortBy: Literal["CreationTime"] = None,
        SortOrder: SortOrder = None,
    ) -> ListLabelingJobsForWorkteamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_labeling_jobs_for_workteam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-labeling-jobs-for-workteam)
        """

    def list_model_bias_job_definitions(
        self,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKey = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
    ) -> ListModelBiasJobDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_model_bias_job_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-model-bias-job-definitions)
        """

    def list_model_explainability_job_definitions(
        self,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKey = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
    ) -> ListModelExplainabilityJobDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_model_explainability_job_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-model-explainability-job-definitions)
        """

    def list_model_package_groups(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: ModelPackageGroupSortBy = None,
        SortOrder: SortOrder = None,
    ) -> ListModelPackageGroupsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_model_package_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-model-package-groups)
        """

    def list_model_packages(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        MaxResults: int = None,
        NameContains: str = None,
        ModelApprovalStatus: ModelApprovalStatus = None,
        ModelPackageGroupName: str = None,
        ModelPackageType: ModelPackageType = None,
        NextToken: str = None,
        SortBy: ModelPackageSortBy = None,
        SortOrder: SortOrder = None,
    ) -> ListModelPackagesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_model_packages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-model-packages)
        """

    def list_model_quality_job_definitions(
        self,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKey = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
    ) -> ListModelQualityJobDefinitionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_model_quality_job_definitions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-model-quality-job-definitions)
        """

    def list_models(
        self,
        SortBy: ModelSortKey = None,
        SortOrder: OrderKey = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
    ) -> ListModelsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_models)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-models)
        """

    def list_monitoring_executions(
        self,
        MonitoringScheduleName: str = None,
        EndpointName: str = None,
        SortBy: MonitoringExecutionSortKey = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
        ScheduledTimeBefore: datetime = None,
        ScheduledTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: ExecutionStatus = None,
        MonitoringJobDefinitionName: str = None,
        MonitoringTypeEquals: MonitoringType = None,
    ) -> ListMonitoringExecutionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-monitoring-executions)
        """

    def list_monitoring_schedules(
        self,
        EndpointName: str = None,
        SortBy: MonitoringScheduleSortKey = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: ScheduleStatus = None,
        MonitoringJobDefinitionName: str = None,
        MonitoringTypeEquals: MonitoringType = None,
    ) -> ListMonitoringSchedulesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_monitoring_schedules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-monitoring-schedules)
        """

    def list_notebook_instance_lifecycle_configs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        SortBy: NotebookInstanceLifecycleConfigSortKey = None,
        SortOrder: NotebookInstanceLifecycleConfigSortOrder = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
    ) -> ListNotebookInstanceLifecycleConfigsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_notebook_instance_lifecycle_configs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-notebook-instance-lifecycle-configs)
        """

    def list_notebook_instances(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        SortBy: NotebookInstanceSortKey = None,
        SortOrder: NotebookInstanceSortOrder = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: NotebookInstanceStatus = None,
        NotebookInstanceLifecycleConfigNameContains: str = None,
        DefaultCodeRepositoryContains: str = None,
        AdditionalCodeRepositoryEquals: str = None,
    ) -> ListNotebookInstancesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_notebook_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-notebook-instances)
        """

    def list_pipeline_execution_steps(
        self,
        PipelineExecutionArn: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        SortOrder: SortOrder = None,
    ) -> ListPipelineExecutionStepsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_pipeline_execution_steps)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-pipeline-execution-steps)
        """

    def list_pipeline_executions(
        self,
        PipelineName: str,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortPipelineExecutionsBy = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListPipelineExecutionsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_pipeline_executions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-pipeline-executions)
        """

    def list_pipeline_parameters_for_execution(
        self, PipelineExecutionArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListPipelineParametersForExecutionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_pipeline_parameters_for_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-pipeline-parameters-for-execution)
        """

    def list_pipelines(
        self,
        PipelineNamePrefix: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortPipelinesBy = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListPipelinesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_pipelines)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-pipelines)
        """

    def list_processing_jobs(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: ProcessingJobStatus = None,
        SortBy: SortBy = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListProcessingJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_processing_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-processing-jobs)
        """

    def list_projects(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        MaxResults: int = None,
        NameContains: str = None,
        NextToken: str = None,
        SortBy: ProjectSortBy = None,
        SortOrder: ProjectSortOrder = None,
    ) -> ListProjectsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-projects)
        """

    def list_subscribed_workteams(
        self, NameContains: str = None, NextToken: str = None, MaxResults: int = None
    ) -> ListSubscribedWorkteamsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_subscribed_workteams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-subscribed-workteams)
        """

    def list_tags(
        self, ResourceArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListTagsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-tags)
        """

    def list_training_jobs(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: TrainingJobStatus = None,
        SortBy: SortBy = None,
        SortOrder: SortOrder = None,
    ) -> ListTrainingJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_training_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-training-jobs)
        """

    def list_training_jobs_for_hyper_parameter_tuning_job(
        self,
        HyperParameterTuningJobName: str,
        NextToken: str = None,
        MaxResults: int = None,
        StatusEquals: TrainingJobStatus = None,
        SortBy: TrainingJobSortByOptions = None,
        SortOrder: SortOrder = None,
    ) -> ListTrainingJobsForHyperParameterTuningJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_training_jobs_for_hyper_parameter_tuning_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-training-jobs-for-hyper-parameter-tuning-job)
        """

    def list_transform_jobs(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: TransformJobStatus = None,
        SortBy: SortBy = None,
        SortOrder: SortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListTransformJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_transform_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-transform-jobs)
        """

    def list_trial_components(
        self,
        ExperimentName: str = None,
        TrialName: str = None,
        SourceArn: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortTrialComponentsBy = None,
        SortOrder: SortOrder = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListTrialComponentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_trial_components)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-trial-components)
        """

    def list_trials(
        self,
        ExperimentName: str = None,
        TrialComponentName: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortTrialsBy = None,
        SortOrder: SortOrder = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListTrialsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_trials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-trials)
        """

    def list_user_profiles(
        self,
        NextToken: str = None,
        MaxResults: int = None,
        SortOrder: SortOrder = None,
        SortBy: UserProfileSortKey = None,
        DomainIdEquals: str = None,
        UserProfileNameContains: str = None,
    ) -> ListUserProfilesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_user_profiles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-user-profiles)
        """

    def list_workforces(
        self,
        SortBy: ListWorkforcesSortByOptions = None,
        SortOrder: SortOrder = None,
        NameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListWorkforcesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_workforces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-workforces)
        """

    def list_workteams(
        self,
        SortBy: ListWorkteamsSortByOptions = None,
        SortOrder: SortOrder = None,
        NameContains: str = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> ListWorkteamsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.list_workteams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#list-workteams)
        """

    def put_model_package_group_policy(
        self, ModelPackageGroupName: str, ResourcePolicy: str
    ) -> PutModelPackageGroupPolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.put_model_package_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#put-model-package-group-policy)
        """

    def register_devices(
        self, DeviceFleetName: str, Devices: List[DeviceTypeDef], Tags: List["TagTypeDef"] = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.register_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#register-devices)
        """

    def render_ui_template(
        self,
        Task: RenderableTaskTypeDef,
        RoleArn: str,
        UiTemplate: UiTemplateTypeDef = None,
        HumanTaskUiArn: str = None,
    ) -> RenderUiTemplateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.render_ui_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#render-ui-template)
        """

    def search(
        self,
        Resource: ResourceType,
        SearchExpression: "SearchExpressionTypeDef" = None,
        SortBy: str = None,
        SortOrder: SearchSortOrder = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> SearchResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#search)
        """

    def start_monitoring_schedule(self, MonitoringScheduleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.start_monitoring_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#start-monitoring-schedule)
        """

    def start_notebook_instance(self, NotebookInstanceName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.start_notebook_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#start-notebook-instance)
        """

    def start_pipeline_execution(
        self,
        PipelineName: str,
        ClientRequestToken: str,
        PipelineExecutionDisplayName: str = None,
        PipelineParameters: List["ParameterTypeDef"] = None,
        PipelineExecutionDescription: str = None,
    ) -> StartPipelineExecutionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.start_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#start-pipeline-execution)
        """

    def stop_auto_ml_job(self, AutoMLJobName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.stop_auto_ml_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop-auto-ml-job)
        """

    def stop_compilation_job(self, CompilationJobName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.stop_compilation_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop-compilation-job)
        """

    def stop_edge_packaging_job(self, EdgePackagingJobName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.stop_edge_packaging_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop-edge-packaging-job)
        """

    def stop_hyper_parameter_tuning_job(self, HyperParameterTuningJobName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.stop_hyper_parameter_tuning_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop-hyper-parameter-tuning-job)
        """

    def stop_labeling_job(self, LabelingJobName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.stop_labeling_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop-labeling-job)
        """

    def stop_monitoring_schedule(self, MonitoringScheduleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.stop_monitoring_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop-monitoring-schedule)
        """

    def stop_notebook_instance(self, NotebookInstanceName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.stop_notebook_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop-notebook-instance)
        """

    def stop_pipeline_execution(
        self, PipelineExecutionArn: str, ClientRequestToken: str
    ) -> StopPipelineExecutionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.stop_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop-pipeline-execution)
        """

    def stop_processing_job(self, ProcessingJobName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.stop_processing_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop-processing-job)
        """

    def stop_training_job(self, TrainingJobName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.stop_training_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop-training-job)
        """

    def stop_transform_job(self, TransformJobName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.stop_transform_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#stop-transform-job)
        """

    def update_action(
        self,
        ActionName: str,
        Description: str = None,
        Status: ActionStatus = None,
        Properties: Dict[str, str] = None,
        PropertiesToRemove: List[str] = None,
    ) -> UpdateActionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-action)
        """

    def update_app_image_config(
        self,
        AppImageConfigName: str,
        KernelGatewayImageConfig: "KernelGatewayImageConfigTypeDef" = None,
    ) -> UpdateAppImageConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_app_image_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-app-image-config)
        """

    def update_artifact(
        self,
        ArtifactArn: str,
        ArtifactName: str = None,
        Properties: Dict[str, str] = None,
        PropertiesToRemove: List[str] = None,
    ) -> UpdateArtifactResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-artifact)
        """

    def update_code_repository(
        self, CodeRepositoryName: str, GitConfig: GitConfigForUpdateTypeDef = None
    ) -> UpdateCodeRepositoryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_code_repository)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-code-repository)
        """

    def update_context(
        self,
        ContextName: str,
        Description: str = None,
        Properties: Dict[str, str] = None,
        PropertiesToRemove: List[str] = None,
    ) -> UpdateContextResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_context)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-context)
        """

    def update_device_fleet(
        self,
        DeviceFleetName: str,
        OutputConfig: "EdgeOutputConfigTypeDef",
        RoleArn: str = None,
        Description: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_device_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-device-fleet)
        """

    def update_devices(self, DeviceFleetName: str, Devices: List[DeviceTypeDef]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-devices)
        """

    def update_domain(
        self, DomainId: str, DefaultUserSettings: "UserSettingsTypeDef" = None
    ) -> UpdateDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-domain)
        """

    def update_endpoint(
        self,
        EndpointName: str,
        EndpointConfigName: str,
        RetainAllVariantProperties: bool = None,
        ExcludeRetainedVariantProperties: List[VariantPropertyTypeDef] = None,
        DeploymentConfig: "DeploymentConfigTypeDef" = None,
    ) -> UpdateEndpointOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-endpoint)
        """

    def update_endpoint_weights_and_capacities(
        self, EndpointName: str, DesiredWeightsAndCapacities: List[DesiredWeightAndCapacityTypeDef]
    ) -> UpdateEndpointWeightsAndCapacitiesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_endpoint_weights_and_capacities)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-endpoint-weights-and-capacities)
        """

    def update_experiment(
        self, ExperimentName: str, DisplayName: str = None, Description: str = None
    ) -> UpdateExperimentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_experiment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-experiment)
        """

    def update_image(
        self,
        ImageName: str,
        DeleteProperties: List[str] = None,
        Description: str = None,
        DisplayName: str = None,
        RoleArn: str = None,
    ) -> UpdateImageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-image)
        """

    def update_model_package(
        self,
        ModelPackageArn: str,
        ModelApprovalStatus: ModelApprovalStatus,
        ApprovalDescription: str = None,
    ) -> UpdateModelPackageOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_model_package)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-model-package)
        """

    def update_monitoring_schedule(
        self,
        MonitoringScheduleName: str,
        MonitoringScheduleConfig: "MonitoringScheduleConfigTypeDef",
    ) -> UpdateMonitoringScheduleResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_monitoring_schedule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-monitoring-schedule)
        """

    def update_notebook_instance(
        self,
        NotebookInstanceName: str,
        InstanceType: InstanceType = None,
        RoleArn: str = None,
        LifecycleConfigName: str = None,
        DisassociateLifecycleConfig: bool = None,
        VolumeSizeInGB: int = None,
        DefaultCodeRepository: str = None,
        AdditionalCodeRepositories: List[str] = None,
        AcceleratorTypes: List[NotebookInstanceAcceleratorType] = None,
        DisassociateAcceleratorTypes: bool = None,
        DisassociateDefaultCodeRepository: bool = None,
        DisassociateAdditionalCodeRepositories: bool = None,
        RootAccess: RootAccess = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_notebook_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-notebook-instance)
        """

    def update_notebook_instance_lifecycle_config(
        self,
        NotebookInstanceLifecycleConfigName: str,
        OnCreate: List["NotebookInstanceLifecycleHookTypeDef"] = None,
        OnStart: List["NotebookInstanceLifecycleHookTypeDef"] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_notebook_instance_lifecycle_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-notebook-instance-lifecycle-config)
        """

    def update_pipeline(
        self,
        PipelineName: str,
        PipelineDisplayName: str = None,
        PipelineDefinition: str = None,
        PipelineDescription: str = None,
        RoleArn: str = None,
    ) -> UpdatePipelineResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_pipeline)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-pipeline)
        """

    def update_pipeline_execution(
        self,
        PipelineExecutionArn: str,
        PipelineExecutionDescription: str = None,
        PipelineExecutionDisplayName: str = None,
    ) -> UpdatePipelineExecutionResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_pipeline_execution)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-pipeline-execution)
        """

    def update_training_job(
        self,
        TrainingJobName: str,
        ProfilerConfig: ProfilerConfigForUpdateTypeDef = None,
        ProfilerRuleConfigurations: List["ProfilerRuleConfigurationTypeDef"] = None,
    ) -> UpdateTrainingJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_training_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-training-job)
        """

    def update_trial(self, TrialName: str, DisplayName: str = None) -> UpdateTrialResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_trial)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-trial)
        """

    def update_trial_component(
        self,
        TrialComponentName: str,
        DisplayName: str = None,
        Status: "TrialComponentStatusTypeDef" = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Parameters: Dict[str, "TrialComponentParameterValueTypeDef"] = None,
        ParametersToRemove: List[str] = None,
        InputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
        InputArtifactsToRemove: List[str] = None,
        OutputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"] = None,
        OutputArtifactsToRemove: List[str] = None,
    ) -> UpdateTrialComponentResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_trial_component)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-trial-component)
        """

    def update_user_profile(
        self, DomainId: str, UserProfileName: str, UserSettings: "UserSettingsTypeDef" = None
    ) -> UpdateUserProfileResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_user_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-user-profile)
        """

    def update_workforce(
        self,
        WorkforceName: str,
        SourceIpConfig: "SourceIpConfigTypeDef" = None,
        OidcConfig: OidcConfigTypeDef = None,
    ) -> UpdateWorkforceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_workforce)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-workforce)
        """

    def update_workteam(
        self,
        WorkteamName: str,
        MemberDefinitions: List["MemberDefinitionTypeDef"] = None,
        Description: str = None,
        NotificationConfiguration: "NotificationConfigurationTypeDef" = None,
    ) -> UpdateWorkteamResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Client.update_workteam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/client.html#update-workteam)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_actions"]) -> ListActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListActions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listactionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_algorithms"]) -> ListAlgorithmsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListAlgorithms)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listalgorithmspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_app_image_configs"]
    ) -> ListAppImageConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListAppImageConfigs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listappimageconfigspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_apps"]) -> ListAppsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListApps)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listappspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_artifacts"]) -> ListArtifactsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListArtifacts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listartifactspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_associations"]
    ) -> ListAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListAssociations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_auto_ml_jobs"]
    ) -> ListAutoMLJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListAutoMLJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listautomljobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_candidates_for_auto_ml_job"]
    ) -> ListCandidatesForAutoMLJobPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListCandidatesForAutoMLJob)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcandidatesforautomljobpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_code_repositories"]
    ) -> ListCodeRepositoriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListCodeRepositories)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcoderepositoriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_compilation_jobs"]
    ) -> ListCompilationJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListCompilationJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcompilationjobspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_contexts"]) -> ListContextsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListContexts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listcontextspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_data_quality_job_definitions"]
    ) -> ListDataQualityJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListDataQualityJobDefinitions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdataqualityjobdefinitionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_device_fleets"]
    ) -> ListDeviceFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListDeviceFleets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdevicefleetspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_devices"]) -> ListDevicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListDevices)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdevicespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_domains"]) -> ListDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListDomains)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listdomainspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_edge_packaging_jobs"]
    ) -> ListEdgePackagingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListEdgePackagingJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listedgepackagingjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_endpoint_configs"]
    ) -> ListEndpointConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpointConfigs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listendpointconfigspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_endpoints"]) -> ListEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpoints)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listendpointspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_experiments"]
    ) -> ListExperimentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListExperiments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listexperimentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_feature_groups"]
    ) -> ListFeatureGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListFeatureGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listfeaturegroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_flow_definitions"]
    ) -> ListFlowDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListFlowDefinitions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listflowdefinitionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_human_task_uis"]
    ) -> ListHumanTaskUisPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListHumanTaskUis)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listhumantaskuispaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_hyper_parameter_tuning_jobs"]
    ) -> ListHyperParameterTuningJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListHyperParameterTuningJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listhyperparametertuningjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_image_versions"]
    ) -> ListImageVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListImageVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listimageversionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_images"]) -> ListImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListImages)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listimagespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_labeling_jobs"]
    ) -> ListLabelingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listlabelingjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_labeling_jobs_for_workteam"]
    ) -> ListLabelingJobsForWorkteamPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobsForWorkteam)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listlabelingjobsforworkteampaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_bias_job_definitions"]
    ) -> ListModelBiasJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListModelBiasJobDefinitions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelbiasjobdefinitionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_explainability_job_definitions"]
    ) -> ListModelExplainabilityJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListModelExplainabilityJobDefinitions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelexplainabilityjobdefinitionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_package_groups"]
    ) -> ListModelPackageGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackageGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelpackagegroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_packages"]
    ) -> ListModelPackagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackages)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelpackagespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_model_quality_job_definitions"]
    ) -> ListModelQualityJobDefinitionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListModelQualityJobDefinitions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelqualityjobdefinitionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_models"]) -> ListModelsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListModels)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmodelspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_executions"]
    ) -> ListMonitoringExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringExecutions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmonitoringexecutionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_monitoring_schedules"]
    ) -> ListMonitoringSchedulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringSchedules)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listmonitoringschedulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notebook_instance_lifecycle_configs"]
    ) -> ListNotebookInstanceLifecycleConfigsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstanceLifecycleConfigs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listnotebookinstancelifecycleconfigspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_notebook_instances"]
    ) -> ListNotebookInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstances)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listnotebookinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipeline_execution_steps"]
    ) -> ListPipelineExecutionStepsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutionSteps)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelineexecutionstepspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipeline_executions"]
    ) -> ListPipelineExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelineexecutionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_pipeline_parameters_for_execution"]
    ) -> ListPipelineParametersForExecutionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineParametersForExecution)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelineparametersforexecutionpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_pipelines"]) -> ListPipelinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelines)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listpipelinespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_processing_jobs"]
    ) -> ListProcessingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListProcessingJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listprocessingjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_subscribed_workteams"]
    ) -> ListSubscribedWorkteamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListSubscribedWorkteams)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listsubscribedworkteamspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tags"]) -> ListTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListTags)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtagspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_training_jobs"]
    ) -> ListTrainingJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrainingjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_training_jobs_for_hyper_parameter_tuning_job"]
    ) -> ListTrainingJobsForHyperParameterTuningJobPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobsForHyperParameterTuningJob)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrainingjobsforhyperparametertuningjobpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_transform_jobs"]
    ) -> ListTransformJobsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListTransformJobs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtransformjobspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_trial_components"]
    ) -> ListTrialComponentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListTrialComponents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrialcomponentspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_trials"]) -> ListTrialsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListTrials)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listtrialspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_profiles"]
    ) -> ListUserProfilesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListUserProfiles)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listuserprofilespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workforces"]) -> ListWorkforcesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkforces)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listworkforcespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_workteams"]) -> ListWorkteamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkteams)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#listworkteamspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search"]) -> SearchPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Paginator.Search)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/paginators.html#searchpaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["endpoint_deleted"]) -> EndpointDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Waiter.endpoint_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#endpointdeletedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["endpoint_in_service"]) -> EndpointInServiceWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Waiter.endpoint_in_service)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#endpointinservicewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_deleted"]
    ) -> NotebookInstanceDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Waiter.notebook_instance_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#notebookinstancedeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_in_service"]
    ) -> NotebookInstanceInServiceWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Waiter.notebook_instance_in_service)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#notebookinstanceinservicewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["notebook_instance_stopped"]
    ) -> NotebookInstanceStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Waiter.notebook_instance_stopped)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#notebookinstancestoppedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["processing_job_completed_or_stopped"]
    ) -> ProcessingJobCompletedOrStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Waiter.processing_job_completed_or_stopped)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#processingjobcompletedorstoppedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["training_job_completed_or_stopped"]
    ) -> TrainingJobCompletedOrStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Waiter.training_job_completed_or_stopped)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#trainingjobcompletedorstoppedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["transform_job_completed_or_stopped"]
    ) -> TransformJobCompletedOrStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker.html#SageMaker.Waiter.transform_job_completed_or_stopped)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/waiters.html#transformjobcompletedorstoppedwaiter)
        """
