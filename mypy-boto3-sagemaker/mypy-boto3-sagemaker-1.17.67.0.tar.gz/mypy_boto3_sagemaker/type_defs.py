"""
Type annotations for sagemaker service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker.type_defs import ActionSourceTypeDef

    data: ActionSourceTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_sagemaker.literals import (
    ActionStatus,
    AlgorithmStatus,
    AppInstanceType,
    AppNetworkAccessType,
    AppStatus,
    AppType,
    ArtifactSourceIdType,
    AssemblyType,
    AssociationEdgeType,
    AthenaResultCompressionType,
    AthenaResultFormat,
    AuthMode,
    AutoMLJobObjectiveType,
    AutoMLJobSecondaryStatus,
    AutoMLJobStatus,
    AutoMLMetricEnum,
    AutoMLS3DataType,
    AwsManagedHumanLoopRequestSource,
    BatchStrategy,
    BooleanOperator,
    CandidateStatus,
    CandidateStepType,
    CapacitySizeType,
    CaptureMode,
    CaptureStatus,
    CompilationJobStatus,
    CompressionType,
    ConditionOutcome,
    ContainerMode,
    ContentClassifier,
    DataDistributionType,
    DetailedAlgorithmStatus,
    DetailedModelPackageStatus,
    DirectInternetAccess,
    DomainStatus,
    EdgePackagingJobStatus,
    EndpointStatus,
    ExecutionStatus,
    FeatureGroupStatus,
    FeatureType,
    FileSystemAccessMode,
    FileSystemType,
    FlowDefinitionStatus,
    Framework,
    HumanTaskUiStatus,
    HyperParameterScalingType,
    HyperParameterTuningJobObjectiveType,
    HyperParameterTuningJobStatus,
    HyperParameterTuningJobStrategyType,
    HyperParameterTuningJobWarmStartType,
    ImageStatus,
    ImageVersionStatus,
    InferenceExecutionMode,
    InputMode,
    InstanceType,
    JoinSource,
    LabelingJobStatus,
    ModelApprovalStatus,
    ModelCacheSetting,
    ModelPackageGroupStatus,
    ModelPackageStatus,
    MonitoringProblemType,
    MonitoringType,
    NotebookInstanceAcceleratorType,
    NotebookInstanceStatus,
    NotebookOutputOption,
    ObjectiveStatus,
    OfflineStoreStatusValue,
    Operator,
    ParameterType,
    PipelineExecutionStatus,
    ProblemType,
    ProcessingInstanceType,
    ProcessingJobStatus,
    ProcessingS3CompressionType,
    ProcessingS3DataDistributionType,
    ProcessingS3DataType,
    ProcessingS3InputMode,
    ProcessingS3UploadMode,
    ProductionVariantAcceleratorType,
    ProductionVariantInstanceType,
    ProfilingStatus,
    ProjectStatus,
    RecordWrapper,
    RedshiftResultCompressionType,
    RedshiftResultFormat,
    RepositoryAccessMode,
    RetentionType,
    RootAccess,
    RuleEvaluationStatus,
    S3DataDistribution,
    S3DataType,
    SagemakerServicecatalogStatus,
    ScheduleStatus,
    SecondaryStatus,
    SplitType,
    StepStatus,
    TargetDevice,
    TargetPlatformAccelerator,
    TargetPlatformArch,
    TargetPlatformOs,
    TrafficRoutingConfigType,
    TrainingInputMode,
    TrainingInstanceType,
    TrainingJobEarlyStoppingType,
    TrainingJobStatus,
    TransformInstanceType,
    TransformJobStatus,
    TrialComponentPrimaryStatus,
    UserProfileStatus,
    VariantPropertyType,
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
    "ActionSourceTypeDef",
    "ActionSummaryTypeDef",
    "AddAssociationResponseTypeDef",
    "AddTagsOutputTypeDef",
    "AgentVersionTypeDef",
    "AlarmTypeDef",
    "AlgorithmSpecificationTypeDef",
    "AlgorithmStatusDetailsTypeDef",
    "AlgorithmStatusItemTypeDef",
    "AlgorithmSummaryTypeDef",
    "AlgorithmValidationProfileTypeDef",
    "AlgorithmValidationSpecificationTypeDef",
    "AnnotationConsolidationConfigTypeDef",
    "AppDetailsTypeDef",
    "AppImageConfigDetailsTypeDef",
    "AppSpecificationTypeDef",
    "ArtifactSourceTypeDef",
    "ArtifactSourceTypeTypeDef",
    "ArtifactSummaryTypeDef",
    "AssociateTrialComponentResponseTypeDef",
    "AssociationSummaryTypeDef",
    "AthenaDatasetDefinitionTypeDef",
    "AutoMLCandidateStepTypeDef",
    "AutoMLCandidateTypeDef",
    "AutoMLChannelTypeDef",
    "AutoMLContainerDefinitionTypeDef",
    "AutoMLDataSourceTypeDef",
    "AutoMLJobArtifactsTypeDef",
    "AutoMLJobCompletionCriteriaTypeDef",
    "AutoMLJobConfigTypeDef",
    "AutoMLJobObjectiveTypeDef",
    "AutoMLJobSummaryTypeDef",
    "AutoMLOutputDataConfigTypeDef",
    "AutoMLPartialFailureReasonTypeDef",
    "AutoMLS3DataSourceTypeDef",
    "AutoMLSecurityConfigTypeDef",
    "AutoRollbackConfigTypeDef",
    "BiasTypeDef",
    "BlueGreenUpdatePolicyTypeDef",
    "CacheHitResultTypeDef",
    "CandidateArtifactLocationsTypeDef",
    "CandidatePropertiesTypeDef",
    "CapacitySizeTypeDef",
    "CaptureContentTypeHeaderTypeDef",
    "CaptureOptionTypeDef",
    "CategoricalParameterRangeSpecificationTypeDef",
    "CategoricalParameterRangeTypeDef",
    "ChannelSpecificationTypeDef",
    "ChannelTypeDef",
    "CheckpointConfigTypeDef",
    "CodeRepositorySummaryTypeDef",
    "CognitoConfigTypeDef",
    "CognitoMemberDefinitionTypeDef",
    "CollectionConfigurationTypeDef",
    "CompilationJobSummaryTypeDef",
    "ConditionStepMetadataTypeDef",
    "ContainerDefinitionTypeDef",
    "ContextSourceTypeDef",
    "ContextSummaryTypeDef",
    "ContinuousParameterRangeSpecificationTypeDef",
    "ContinuousParameterRangeTypeDef",
    "CreateActionResponseTypeDef",
    "CreateAlgorithmOutputTypeDef",
    "CreateAppImageConfigResponseTypeDef",
    "CreateAppResponseTypeDef",
    "CreateArtifactResponseTypeDef",
    "CreateAutoMLJobResponseTypeDef",
    "CreateCodeRepositoryOutputTypeDef",
    "CreateCompilationJobResponseTypeDef",
    "CreateContextResponseTypeDef",
    "CreateDataQualityJobDefinitionResponseTypeDef",
    "CreateDomainResponseTypeDef",
    "CreateEndpointConfigOutputTypeDef",
    "CreateEndpointOutputTypeDef",
    "CreateExperimentResponseTypeDef",
    "CreateFeatureGroupResponseTypeDef",
    "CreateFlowDefinitionResponseTypeDef",
    "CreateHumanTaskUiResponseTypeDef",
    "CreateHyperParameterTuningJobResponseTypeDef",
    "CreateImageResponseTypeDef",
    "CreateImageVersionResponseTypeDef",
    "CreateLabelingJobResponseTypeDef",
    "CreateModelBiasJobDefinitionResponseTypeDef",
    "CreateModelExplainabilityJobDefinitionResponseTypeDef",
    "CreateModelOutputTypeDef",
    "CreateModelPackageGroupOutputTypeDef",
    "CreateModelPackageOutputTypeDef",
    "CreateModelQualityJobDefinitionResponseTypeDef",
    "CreateMonitoringScheduleResponseTypeDef",
    "CreateNotebookInstanceLifecycleConfigOutputTypeDef",
    "CreateNotebookInstanceOutputTypeDef",
    "CreatePipelineResponseTypeDef",
    "CreatePresignedDomainUrlResponseTypeDef",
    "CreatePresignedNotebookInstanceUrlOutputTypeDef",
    "CreateProcessingJobResponseTypeDef",
    "CreateProjectOutputTypeDef",
    "CreateTrainingJobResponseTypeDef",
    "CreateTransformJobResponseTypeDef",
    "CreateTrialComponentResponseTypeDef",
    "CreateTrialResponseTypeDef",
    "CreateUserProfileResponseTypeDef",
    "CreateWorkforceResponseTypeDef",
    "CreateWorkteamResponseTypeDef",
    "CustomImageTypeDef",
    "DataCaptureConfigSummaryTypeDef",
    "DataCaptureConfigTypeDef",
    "DataCatalogConfigTypeDef",
    "DataProcessingTypeDef",
    "DataQualityAppSpecificationTypeDef",
    "DataQualityBaselineConfigTypeDef",
    "DataQualityJobInputTypeDef",
    "DataSourceTypeDef",
    "DatasetDefinitionTypeDef",
    "DebugHookConfigTypeDef",
    "DebugRuleConfigurationTypeDef",
    "DebugRuleEvaluationStatusTypeDef",
    "DeleteActionResponseTypeDef",
    "DeleteArtifactResponseTypeDef",
    "DeleteAssociationResponseTypeDef",
    "DeleteContextResponseTypeDef",
    "DeleteExperimentResponseTypeDef",
    "DeletePipelineResponseTypeDef",
    "DeleteTrialComponentResponseTypeDef",
    "DeleteTrialResponseTypeDef",
    "DeleteWorkteamResponseTypeDef",
    "DeployedImageTypeDef",
    "DeploymentConfigTypeDef",
    "DescribeActionResponseTypeDef",
    "DescribeAlgorithmOutputTypeDef",
    "DescribeAppImageConfigResponseTypeDef",
    "DescribeAppResponseTypeDef",
    "DescribeArtifactResponseTypeDef",
    "DescribeAutoMLJobResponseTypeDef",
    "DescribeCodeRepositoryOutputTypeDef",
    "DescribeCompilationJobResponseTypeDef",
    "DescribeContextResponseTypeDef",
    "DescribeDataQualityJobDefinitionResponseTypeDef",
    "DescribeDeviceFleetResponseTypeDef",
    "DescribeDeviceResponseTypeDef",
    "DescribeDomainResponseTypeDef",
    "DescribeEdgePackagingJobResponseTypeDef",
    "DescribeEndpointConfigOutputTypeDef",
    "DescribeEndpointOutputTypeDef",
    "DescribeExperimentResponseTypeDef",
    "DescribeFeatureGroupResponseTypeDef",
    "DescribeFlowDefinitionResponseTypeDef",
    "DescribeHumanTaskUiResponseTypeDef",
    "DescribeHyperParameterTuningJobResponseTypeDef",
    "DescribeImageResponseTypeDef",
    "DescribeImageVersionResponseTypeDef",
    "DescribeLabelingJobResponseTypeDef",
    "DescribeModelBiasJobDefinitionResponseTypeDef",
    "DescribeModelExplainabilityJobDefinitionResponseTypeDef",
    "DescribeModelOutputTypeDef",
    "DescribeModelPackageGroupOutputTypeDef",
    "DescribeModelPackageOutputTypeDef",
    "DescribeModelQualityJobDefinitionResponseTypeDef",
    "DescribeMonitoringScheduleResponseTypeDef",
    "DescribeNotebookInstanceLifecycleConfigOutputTypeDef",
    "DescribeNotebookInstanceOutputTypeDef",
    "DescribePipelineDefinitionForExecutionResponseTypeDef",
    "DescribePipelineExecutionResponseTypeDef",
    "DescribePipelineResponseTypeDef",
    "DescribeProcessingJobResponseTypeDef",
    "DescribeProjectOutputTypeDef",
    "DescribeSubscribedWorkteamResponseTypeDef",
    "DescribeTrainingJobResponseTypeDef",
    "DescribeTransformJobResponseTypeDef",
    "DescribeTrialComponentResponseTypeDef",
    "DescribeTrialResponseTypeDef",
    "DescribeUserProfileResponseTypeDef",
    "DescribeWorkforceResponseTypeDef",
    "DescribeWorkteamResponseTypeDef",
    "DesiredWeightAndCapacityTypeDef",
    "DeviceFleetSummaryTypeDef",
    "DeviceStatsTypeDef",
    "DeviceSummaryTypeDef",
    "DeviceTypeDef",
    "DisassociateTrialComponentResponseTypeDef",
    "DomainDetailsTypeDef",
    "EdgeModelStatTypeDef",
    "EdgeModelSummaryTypeDef",
    "EdgeModelTypeDef",
    "EdgeOutputConfigTypeDef",
    "EdgePackagingJobSummaryTypeDef",
    "EndpointConfigSummaryTypeDef",
    "EndpointInputTypeDef",
    "EndpointSummaryTypeDef",
    "EndpointTypeDef",
    "ExperimentConfigTypeDef",
    "ExperimentSourceTypeDef",
    "ExperimentSummaryTypeDef",
    "ExperimentTypeDef",
    "ExplainabilityTypeDef",
    "FeatureDefinitionTypeDef",
    "FeatureGroupSummaryTypeDef",
    "FeatureGroupTypeDef",
    "FileSystemConfigTypeDef",
    "FileSystemDataSourceTypeDef",
    "FilterTypeDef",
    "FinalAutoMLJobObjectiveMetricTypeDef",
    "FinalHyperParameterTuningJobObjectiveMetricTypeDef",
    "FlowDefinitionOutputConfigTypeDef",
    "FlowDefinitionSummaryTypeDef",
    "GetDeviceFleetReportResponseTypeDef",
    "GetModelPackageGroupPolicyOutputTypeDef",
    "GetSagemakerServicecatalogPortfolioStatusOutputTypeDef",
    "GetSearchSuggestionsResponseTypeDef",
    "GitConfigForUpdateTypeDef",
    "GitConfigTypeDef",
    "HumanLoopActivationConditionsConfigTypeDef",
    "HumanLoopActivationConfigTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanLoopRequestSourceTypeDef",
    "HumanTaskConfigTypeDef",
    "HumanTaskUiSummaryTypeDef",
    "HyperParameterAlgorithmSpecificationTypeDef",
    "HyperParameterSpecificationTypeDef",
    "HyperParameterTrainingJobDefinitionTypeDef",
    "HyperParameterTrainingJobSummaryTypeDef",
    "HyperParameterTuningJobConfigTypeDef",
    "HyperParameterTuningJobObjectiveTypeDef",
    "HyperParameterTuningJobSummaryTypeDef",
    "HyperParameterTuningJobWarmStartConfigTypeDef",
    "ImageConfigTypeDef",
    "ImageTypeDef",
    "ImageVersionTypeDef",
    "InferenceExecutionConfigTypeDef",
    "InferenceSpecificationTypeDef",
    "InputConfigTypeDef",
    "IntegerParameterRangeSpecificationTypeDef",
    "IntegerParameterRangeTypeDef",
    "JupyterServerAppSettingsTypeDef",
    "KernelGatewayAppSettingsTypeDef",
    "KernelGatewayImageConfigTypeDef",
    "KernelSpecTypeDef",
    "LabelCountersForWorkteamTypeDef",
    "LabelCountersTypeDef",
    "LabelingJobAlgorithmsConfigTypeDef",
    "LabelingJobDataAttributesTypeDef",
    "LabelingJobDataSourceTypeDef",
    "LabelingJobForWorkteamSummaryTypeDef",
    "LabelingJobInputConfigTypeDef",
    "LabelingJobOutputConfigTypeDef",
    "LabelingJobOutputTypeDef",
    "LabelingJobResourceConfigTypeDef",
    "LabelingJobS3DataSourceTypeDef",
    "LabelingJobSnsDataSourceTypeDef",
    "LabelingJobStoppingConditionsTypeDef",
    "LabelingJobSummaryTypeDef",
    "ListActionsResponseTypeDef",
    "ListAlgorithmsOutputTypeDef",
    "ListAppImageConfigsResponseTypeDef",
    "ListAppsResponseTypeDef",
    "ListArtifactsResponseTypeDef",
    "ListAssociationsResponseTypeDef",
    "ListAutoMLJobsResponseTypeDef",
    "ListCandidatesForAutoMLJobResponseTypeDef",
    "ListCodeRepositoriesOutputTypeDef",
    "ListCompilationJobsResponseTypeDef",
    "ListContextsResponseTypeDef",
    "ListDataQualityJobDefinitionsResponseTypeDef",
    "ListDeviceFleetsResponseTypeDef",
    "ListDevicesResponseTypeDef",
    "ListDomainsResponseTypeDef",
    "ListEdgePackagingJobsResponseTypeDef",
    "ListEndpointConfigsOutputTypeDef",
    "ListEndpointsOutputTypeDef",
    "ListExperimentsResponseTypeDef",
    "ListFeatureGroupsResponseTypeDef",
    "ListFlowDefinitionsResponseTypeDef",
    "ListHumanTaskUisResponseTypeDef",
    "ListHyperParameterTuningJobsResponseTypeDef",
    "ListImageVersionsResponseTypeDef",
    "ListImagesResponseTypeDef",
    "ListLabelingJobsForWorkteamResponseTypeDef",
    "ListLabelingJobsResponseTypeDef",
    "ListModelBiasJobDefinitionsResponseTypeDef",
    "ListModelExplainabilityJobDefinitionsResponseTypeDef",
    "ListModelPackageGroupsOutputTypeDef",
    "ListModelPackagesOutputTypeDef",
    "ListModelQualityJobDefinitionsResponseTypeDef",
    "ListModelsOutputTypeDef",
    "ListMonitoringExecutionsResponseTypeDef",
    "ListMonitoringSchedulesResponseTypeDef",
    "ListNotebookInstanceLifecycleConfigsOutputTypeDef",
    "ListNotebookInstancesOutputTypeDef",
    "ListPipelineExecutionStepsResponseTypeDef",
    "ListPipelineExecutionsResponseTypeDef",
    "ListPipelineParametersForExecutionResponseTypeDef",
    "ListPipelinesResponseTypeDef",
    "ListProcessingJobsResponseTypeDef",
    "ListProjectsOutputTypeDef",
    "ListSubscribedWorkteamsResponseTypeDef",
    "ListTagsOutputTypeDef",
    "ListTrainingJobsForHyperParameterTuningJobResponseTypeDef",
    "ListTrainingJobsResponseTypeDef",
    "ListTransformJobsResponseTypeDef",
    "ListTrialComponentsResponseTypeDef",
    "ListTrialsResponseTypeDef",
    "ListUserProfilesResponseTypeDef",
    "ListWorkforcesResponseTypeDef",
    "ListWorkteamsResponseTypeDef",
    "MemberDefinitionTypeDef",
    "MetadataPropertiesTypeDef",
    "MetricDataTypeDef",
    "MetricDefinitionTypeDef",
    "MetricsSourceTypeDef",
    "ModelArtifactsTypeDef",
    "ModelBiasAppSpecificationTypeDef",
    "ModelBiasBaselineConfigTypeDef",
    "ModelBiasJobInputTypeDef",
    "ModelClientConfigTypeDef",
    "ModelDataQualityTypeDef",
    "ModelDeployConfigTypeDef",
    "ModelDeployResultTypeDef",
    "ModelDigestsTypeDef",
    "ModelExplainabilityAppSpecificationTypeDef",
    "ModelExplainabilityBaselineConfigTypeDef",
    "ModelExplainabilityJobInputTypeDef",
    "ModelMetricsTypeDef",
    "ModelPackageContainerDefinitionTypeDef",
    "ModelPackageGroupSummaryTypeDef",
    "ModelPackageGroupTypeDef",
    "ModelPackageStatusDetailsTypeDef",
    "ModelPackageStatusItemTypeDef",
    "ModelPackageSummaryTypeDef",
    "ModelPackageTypeDef",
    "ModelPackageValidationProfileTypeDef",
    "ModelPackageValidationSpecificationTypeDef",
    "ModelQualityAppSpecificationTypeDef",
    "ModelQualityBaselineConfigTypeDef",
    "ModelQualityJobInputTypeDef",
    "ModelQualityTypeDef",
    "ModelStepMetadataTypeDef",
    "ModelSummaryTypeDef",
    "MonitoringAppSpecificationTypeDef",
    "MonitoringBaselineConfigTypeDef",
    "MonitoringClusterConfigTypeDef",
    "MonitoringConstraintsResourceTypeDef",
    "MonitoringExecutionSummaryTypeDef",
    "MonitoringGroundTruthS3InputTypeDef",
    "MonitoringInputTypeDef",
    "MonitoringJobDefinitionSummaryTypeDef",
    "MonitoringJobDefinitionTypeDef",
    "MonitoringNetworkConfigTypeDef",
    "MonitoringOutputConfigTypeDef",
    "MonitoringOutputTypeDef",
    "MonitoringResourcesTypeDef",
    "MonitoringS3OutputTypeDef",
    "MonitoringScheduleConfigTypeDef",
    "MonitoringScheduleSummaryTypeDef",
    "MonitoringScheduleTypeDef",
    "MonitoringStatisticsResourceTypeDef",
    "MonitoringStoppingConditionTypeDef",
    "MultiModelConfigTypeDef",
    "NestedFiltersTypeDef",
    "NetworkConfigTypeDef",
    "NotebookInstanceLifecycleConfigSummaryTypeDef",
    "NotebookInstanceLifecycleHookTypeDef",
    "NotebookInstanceSummaryTypeDef",
    "NotificationConfigurationTypeDef",
    "ObjectiveStatusCountersTypeDef",
    "OfflineStoreConfigTypeDef",
    "OfflineStoreStatusTypeDef",
    "OidcConfigForResponseTypeDef",
    "OidcConfigTypeDef",
    "OidcMemberDefinitionTypeDef",
    "OnlineStoreConfigTypeDef",
    "OnlineStoreSecurityConfigTypeDef",
    "OutputConfigTypeDef",
    "OutputDataConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterRangeTypeDef",
    "ParameterRangesTypeDef",
    "ParameterTypeDef",
    "ParentHyperParameterTuningJobTypeDef",
    "ParentTypeDef",
    "PipelineExecutionStepMetadataTypeDef",
    "PipelineExecutionStepTypeDef",
    "PipelineExecutionSummaryTypeDef",
    "PipelineExecutionTypeDef",
    "PipelineSummaryTypeDef",
    "PipelineTypeDef",
    "ProcessingClusterConfigTypeDef",
    "ProcessingFeatureStoreOutputTypeDef",
    "ProcessingInputTypeDef",
    "ProcessingJobStepMetadataTypeDef",
    "ProcessingJobSummaryTypeDef",
    "ProcessingJobTypeDef",
    "ProcessingOutputConfigTypeDef",
    "ProcessingOutputTypeDef",
    "ProcessingResourcesTypeDef",
    "ProcessingS3InputTypeDef",
    "ProcessingS3OutputTypeDef",
    "ProcessingStoppingConditionTypeDef",
    "ProductionVariantCoreDumpConfigTypeDef",
    "ProductionVariantSummaryTypeDef",
    "ProductionVariantTypeDef",
    "ProfilerConfigForUpdateTypeDef",
    "ProfilerConfigTypeDef",
    "ProfilerRuleConfigurationTypeDef",
    "ProfilerRuleEvaluationStatusTypeDef",
    "ProjectSummaryTypeDef",
    "PropertyNameQueryTypeDef",
    "PropertyNameSuggestionTypeDef",
    "ProvisioningParameterTypeDef",
    "PublicWorkforceTaskPriceTypeDef",
    "PutModelPackageGroupPolicyOutputTypeDef",
    "RedshiftDatasetDefinitionTypeDef",
    "RegisterModelStepMetadataTypeDef",
    "RenderUiTemplateResponseTypeDef",
    "RenderableTaskTypeDef",
    "RenderingErrorTypeDef",
    "RepositoryAuthConfigTypeDef",
    "ResolvedAttributesTypeDef",
    "ResourceConfigTypeDef",
    "ResourceLimitsTypeDef",
    "ResourceSpecTypeDef",
    "ResponseMetadata",
    "RetentionPolicyTypeDef",
    "RetryStrategyTypeDef",
    "S3DataSourceTypeDef",
    "S3StorageConfigTypeDef",
    "ScheduleConfigTypeDef",
    "SearchExpressionTypeDef",
    "SearchRecordTypeDef",
    "SearchResponseTypeDef",
    "SecondaryStatusTransitionTypeDef",
    "ServiceCatalogProvisionedProductDetailsTypeDef",
    "ServiceCatalogProvisioningDetailsTypeDef",
    "SharingSettingsTypeDef",
    "ShuffleConfigTypeDef",
    "SourceAlgorithmSpecificationTypeDef",
    "SourceAlgorithmTypeDef",
    "SourceIpConfigTypeDef",
    "StartPipelineExecutionResponseTypeDef",
    "StopPipelineExecutionResponseTypeDef",
    "StoppingConditionTypeDef",
    "SubscribedWorkteamTypeDef",
    "SuggestionQueryTypeDef",
    "TagTypeDef",
    "TargetPlatformTypeDef",
    "TensorBoardAppSettingsTypeDef",
    "TensorBoardOutputConfigTypeDef",
    "TrafficRoutingConfigTypeDef",
    "TrainingJobDefinitionTypeDef",
    "TrainingJobStatusCountersTypeDef",
    "TrainingJobStepMetadataTypeDef",
    "TrainingJobSummaryTypeDef",
    "TrainingJobTypeDef",
    "TrainingSpecificationTypeDef",
    "TransformDataSourceTypeDef",
    "TransformInputTypeDef",
    "TransformJobDefinitionTypeDef",
    "TransformJobStepMetadataTypeDef",
    "TransformJobSummaryTypeDef",
    "TransformJobTypeDef",
    "TransformOutputTypeDef",
    "TransformResourcesTypeDef",
    "TransformS3DataSourceTypeDef",
    "TrialComponentArtifactTypeDef",
    "TrialComponentMetricSummaryTypeDef",
    "TrialComponentParameterValueTypeDef",
    "TrialComponentSimpleSummaryTypeDef",
    "TrialComponentSourceDetailTypeDef",
    "TrialComponentSourceTypeDef",
    "TrialComponentStatusTypeDef",
    "TrialComponentSummaryTypeDef",
    "TrialComponentTypeDef",
    "TrialSourceTypeDef",
    "TrialSummaryTypeDef",
    "TrialTypeDef",
    "TuningJobCompletionCriteriaTypeDef",
    "USDTypeDef",
    "UiConfigTypeDef",
    "UiTemplateInfoTypeDef",
    "UiTemplateTypeDef",
    "UpdateActionResponseTypeDef",
    "UpdateAppImageConfigResponseTypeDef",
    "UpdateArtifactResponseTypeDef",
    "UpdateCodeRepositoryOutputTypeDef",
    "UpdateContextResponseTypeDef",
    "UpdateDomainResponseTypeDef",
    "UpdateEndpointOutputTypeDef",
    "UpdateEndpointWeightsAndCapacitiesOutputTypeDef",
    "UpdateExperimentResponseTypeDef",
    "UpdateImageResponseTypeDef",
    "UpdateModelPackageOutputTypeDef",
    "UpdateMonitoringScheduleResponseTypeDef",
    "UpdatePipelineExecutionResponseTypeDef",
    "UpdatePipelineResponseTypeDef",
    "UpdateTrainingJobResponseTypeDef",
    "UpdateTrialComponentResponseTypeDef",
    "UpdateTrialResponseTypeDef",
    "UpdateUserProfileResponseTypeDef",
    "UpdateWorkforceResponseTypeDef",
    "UpdateWorkteamResponseTypeDef",
    "UserContextTypeDef",
    "UserProfileDetailsTypeDef",
    "UserSettingsTypeDef",
    "VariantPropertyTypeDef",
    "VpcConfigTypeDef",
    "WaiterConfigTypeDef",
    "WorkforceTypeDef",
    "WorkteamTypeDef",
)


class _RequiredActionSourceTypeDef(TypedDict):
    SourceUri: str


class ActionSourceTypeDef(_RequiredActionSourceTypeDef, total=False):
    SourceType: str
    SourceId: str


class ActionSummaryTypeDef(TypedDict, total=False):
    ActionArn: str
    ActionName: str
    Source: "ActionSourceTypeDef"
    ActionType: str
    Status: ActionStatus
    CreationTime: datetime
    LastModifiedTime: datetime


class AddAssociationResponseTypeDef(TypedDict, total=False):
    SourceArn: str
    DestinationArn: str


class AddTagsOutputTypeDef(TypedDict):
    Tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class AgentVersionTypeDef(TypedDict):
    Version: str
    AgentCount: int


class AlarmTypeDef(TypedDict, total=False):
    AlarmName: str


class _RequiredAlgorithmSpecificationTypeDef(TypedDict):
    TrainingInputMode: TrainingInputMode


class AlgorithmSpecificationTypeDef(_RequiredAlgorithmSpecificationTypeDef, total=False):
    TrainingImage: str
    AlgorithmName: str
    MetricDefinitions: List["MetricDefinitionTypeDef"]
    EnableSageMakerMetricsTimeSeries: bool


class AlgorithmStatusDetailsTypeDef(TypedDict, total=False):
    ValidationStatuses: List["AlgorithmStatusItemTypeDef"]
    ImageScanStatuses: List["AlgorithmStatusItemTypeDef"]


class _RequiredAlgorithmStatusItemTypeDef(TypedDict):
    Name: str
    Status: DetailedAlgorithmStatus


class AlgorithmStatusItemTypeDef(_RequiredAlgorithmStatusItemTypeDef, total=False):
    FailureReason: str


class _RequiredAlgorithmSummaryTypeDef(TypedDict):
    AlgorithmName: str
    AlgorithmArn: str
    CreationTime: datetime
    AlgorithmStatus: AlgorithmStatus


class AlgorithmSummaryTypeDef(_RequiredAlgorithmSummaryTypeDef, total=False):
    AlgorithmDescription: str


class _RequiredAlgorithmValidationProfileTypeDef(TypedDict):
    ProfileName: str
    TrainingJobDefinition: "TrainingJobDefinitionTypeDef"


class AlgorithmValidationProfileTypeDef(_RequiredAlgorithmValidationProfileTypeDef, total=False):
    TransformJobDefinition: "TransformJobDefinitionTypeDef"


class AlgorithmValidationSpecificationTypeDef(TypedDict):
    ValidationRole: str
    ValidationProfiles: List["AlgorithmValidationProfileTypeDef"]


class AnnotationConsolidationConfigTypeDef(TypedDict):
    AnnotationConsolidationLambdaArn: str


class AppDetailsTypeDef(TypedDict, total=False):
    DomainId: str
    UserProfileName: str
    AppType: AppType
    AppName: str
    Status: AppStatus
    CreationTime: datetime


class AppImageConfigDetailsTypeDef(TypedDict, total=False):
    AppImageConfigArn: str
    AppImageConfigName: str
    CreationTime: datetime
    LastModifiedTime: datetime
    KernelGatewayImageConfig: "KernelGatewayImageConfigTypeDef"


class _RequiredAppSpecificationTypeDef(TypedDict):
    ImageUri: str


class AppSpecificationTypeDef(_RequiredAppSpecificationTypeDef, total=False):
    ContainerEntrypoint: List[str]
    ContainerArguments: List[str]


class _RequiredArtifactSourceTypeDef(TypedDict):
    SourceUri: str


class ArtifactSourceTypeDef(_RequiredArtifactSourceTypeDef, total=False):
    SourceTypes: List["ArtifactSourceTypeTypeDef"]


class ArtifactSourceTypeTypeDef(TypedDict):
    SourceIdType: ArtifactSourceIdType
    Value: str


class ArtifactSummaryTypeDef(TypedDict, total=False):
    ArtifactArn: str
    ArtifactName: str
    Source: "ArtifactSourceTypeDef"
    ArtifactType: str
    CreationTime: datetime
    LastModifiedTime: datetime


class AssociateTrialComponentResponseTypeDef(TypedDict, total=False):
    TrialComponentArn: str
    TrialArn: str


class AssociationSummaryTypeDef(TypedDict, total=False):
    SourceArn: str
    DestinationArn: str
    SourceType: str
    DestinationType: str
    AssociationType: AssociationEdgeType
    SourceName: str
    DestinationName: str
    CreationTime: datetime
    CreatedBy: "UserContextTypeDef"


class _RequiredAthenaDatasetDefinitionTypeDef(TypedDict):
    Catalog: str
    Database: str
    QueryString: str
    OutputS3Uri: str
    OutputFormat: AthenaResultFormat


class AthenaDatasetDefinitionTypeDef(_RequiredAthenaDatasetDefinitionTypeDef, total=False):
    WorkGroup: str
    KmsKeyId: str
    OutputCompression: AthenaResultCompressionType


class AutoMLCandidateStepTypeDef(TypedDict):
    CandidateStepType: CandidateStepType
    CandidateStepArn: str
    CandidateStepName: str


class _RequiredAutoMLCandidateTypeDef(TypedDict):
    CandidateName: str
    ObjectiveStatus: ObjectiveStatus
    CandidateSteps: List["AutoMLCandidateStepTypeDef"]
    CandidateStatus: CandidateStatus
    CreationTime: datetime
    LastModifiedTime: datetime


class AutoMLCandidateTypeDef(_RequiredAutoMLCandidateTypeDef, total=False):
    FinalAutoMLJobObjectiveMetric: "FinalAutoMLJobObjectiveMetricTypeDef"
    InferenceContainers: List["AutoMLContainerDefinitionTypeDef"]
    EndTime: datetime
    FailureReason: str
    CandidateProperties: "CandidatePropertiesTypeDef"


class _RequiredAutoMLChannelTypeDef(TypedDict):
    DataSource: "AutoMLDataSourceTypeDef"
    TargetAttributeName: str


class AutoMLChannelTypeDef(_RequiredAutoMLChannelTypeDef, total=False):
    CompressionType: CompressionType


class _RequiredAutoMLContainerDefinitionTypeDef(TypedDict):
    Image: str
    ModelDataUrl: str


class AutoMLContainerDefinitionTypeDef(_RequiredAutoMLContainerDefinitionTypeDef, total=False):
    Environment: Dict[str, str]


class AutoMLDataSourceTypeDef(TypedDict):
    S3DataSource: "AutoMLS3DataSourceTypeDef"


class AutoMLJobArtifactsTypeDef(TypedDict, total=False):
    CandidateDefinitionNotebookLocation: str
    DataExplorationNotebookLocation: str


class AutoMLJobCompletionCriteriaTypeDef(TypedDict, total=False):
    MaxCandidates: int
    MaxRuntimePerTrainingJobInSeconds: int
    MaxAutoMLJobRuntimeInSeconds: int


class AutoMLJobConfigTypeDef(TypedDict, total=False):
    CompletionCriteria: "AutoMLJobCompletionCriteriaTypeDef"
    SecurityConfig: "AutoMLSecurityConfigTypeDef"


class AutoMLJobObjectiveTypeDef(TypedDict):
    MetricName: AutoMLMetricEnum


class _RequiredAutoMLJobSummaryTypeDef(TypedDict):
    AutoMLJobName: str
    AutoMLJobArn: str
    AutoMLJobStatus: AutoMLJobStatus
    AutoMLJobSecondaryStatus: AutoMLJobSecondaryStatus
    CreationTime: datetime
    LastModifiedTime: datetime


class AutoMLJobSummaryTypeDef(_RequiredAutoMLJobSummaryTypeDef, total=False):
    EndTime: datetime
    FailureReason: str
    PartialFailureReasons: List["AutoMLPartialFailureReasonTypeDef"]


class _RequiredAutoMLOutputDataConfigTypeDef(TypedDict):
    S3OutputPath: str


class AutoMLOutputDataConfigTypeDef(_RequiredAutoMLOutputDataConfigTypeDef, total=False):
    KmsKeyId: str


class AutoMLPartialFailureReasonTypeDef(TypedDict, total=False):
    PartialFailureMessage: str


class AutoMLS3DataSourceTypeDef(TypedDict):
    S3DataType: AutoMLS3DataType
    S3Uri: str


class AutoMLSecurityConfigTypeDef(TypedDict, total=False):
    VolumeKmsKeyId: str
    EnableInterContainerTrafficEncryption: bool
    VpcConfig: "VpcConfigTypeDef"


class AutoRollbackConfigTypeDef(TypedDict, total=False):
    Alarms: List["AlarmTypeDef"]


class BiasTypeDef(TypedDict, total=False):
    Report: "MetricsSourceTypeDef"


class _RequiredBlueGreenUpdatePolicyTypeDef(TypedDict):
    TrafficRoutingConfiguration: "TrafficRoutingConfigTypeDef"


class BlueGreenUpdatePolicyTypeDef(_RequiredBlueGreenUpdatePolicyTypeDef, total=False):
    TerminationWaitInSeconds: int
    MaximumExecutionTimeoutInSeconds: int


class CacheHitResultTypeDef(TypedDict, total=False):
    SourcePipelineExecutionArn: str


class CandidateArtifactLocationsTypeDef(TypedDict):
    Explainability: str


class CandidatePropertiesTypeDef(TypedDict, total=False):
    CandidateArtifactLocations: "CandidateArtifactLocationsTypeDef"


CapacitySizeTypeDef = TypedDict("CapacitySizeTypeDef", {"Type": CapacitySizeType, "Value": int})


class CaptureContentTypeHeaderTypeDef(TypedDict, total=False):
    CsvContentTypes: List[str]
    JsonContentTypes: List[str]


class CaptureOptionTypeDef(TypedDict):
    CaptureMode: CaptureMode


class CategoricalParameterRangeSpecificationTypeDef(TypedDict):
    Values: List[str]


class CategoricalParameterRangeTypeDef(TypedDict):
    Name: str
    Values: List[str]


class _RequiredChannelSpecificationTypeDef(TypedDict):
    Name: str
    SupportedContentTypes: List[str]
    SupportedInputModes: List[TrainingInputMode]


class ChannelSpecificationTypeDef(_RequiredChannelSpecificationTypeDef, total=False):
    Description: str
    IsRequired: bool
    SupportedCompressionTypes: List[CompressionType]


class _RequiredChannelTypeDef(TypedDict):
    ChannelName: str
    DataSource: "DataSourceTypeDef"


class ChannelTypeDef(_RequiredChannelTypeDef, total=False):
    ContentType: str
    CompressionType: CompressionType
    RecordWrapperType: RecordWrapper
    InputMode: TrainingInputMode
    ShuffleConfig: "ShuffleConfigTypeDef"


class _RequiredCheckpointConfigTypeDef(TypedDict):
    S3Uri: str


class CheckpointConfigTypeDef(_RequiredCheckpointConfigTypeDef, total=False):
    LocalPath: str


class _RequiredCodeRepositorySummaryTypeDef(TypedDict):
    CodeRepositoryName: str
    CodeRepositoryArn: str
    CreationTime: datetime
    LastModifiedTime: datetime


class CodeRepositorySummaryTypeDef(_RequiredCodeRepositorySummaryTypeDef, total=False):
    GitConfig: "GitConfigTypeDef"


class CognitoConfigTypeDef(TypedDict):
    UserPool: str
    ClientId: str


class CognitoMemberDefinitionTypeDef(TypedDict):
    UserPool: str
    UserGroup: str
    ClientId: str


class CollectionConfigurationTypeDef(TypedDict, total=False):
    CollectionName: str
    CollectionParameters: Dict[str, str]


class _RequiredCompilationJobSummaryTypeDef(TypedDict):
    CompilationJobName: str
    CompilationJobArn: str
    CreationTime: datetime
    CompilationJobStatus: CompilationJobStatus


class CompilationJobSummaryTypeDef(_RequiredCompilationJobSummaryTypeDef, total=False):
    CompilationStartTime: datetime
    CompilationEndTime: datetime
    CompilationTargetDevice: TargetDevice
    CompilationTargetPlatformOs: TargetPlatformOs
    CompilationTargetPlatformArch: TargetPlatformArch
    CompilationTargetPlatformAccelerator: TargetPlatformAccelerator
    LastModifiedTime: datetime


class ConditionStepMetadataTypeDef(TypedDict, total=False):
    Outcome: ConditionOutcome


class ContainerDefinitionTypeDef(TypedDict, total=False):
    ContainerHostname: str
    Image: str
    ImageConfig: "ImageConfigTypeDef"
    Mode: ContainerMode
    ModelDataUrl: str
    Environment: Dict[str, str]
    ModelPackageName: str
    MultiModelConfig: "MultiModelConfigTypeDef"


class _RequiredContextSourceTypeDef(TypedDict):
    SourceUri: str


class ContextSourceTypeDef(_RequiredContextSourceTypeDef, total=False):
    SourceType: str
    SourceId: str


class ContextSummaryTypeDef(TypedDict, total=False):
    ContextArn: str
    ContextName: str
    Source: "ContextSourceTypeDef"
    ContextType: str
    CreationTime: datetime
    LastModifiedTime: datetime


class ContinuousParameterRangeSpecificationTypeDef(TypedDict):
    MinValue: str
    MaxValue: str


class _RequiredContinuousParameterRangeTypeDef(TypedDict):
    Name: str
    MinValue: str
    MaxValue: str


class ContinuousParameterRangeTypeDef(_RequiredContinuousParameterRangeTypeDef, total=False):
    ScalingType: HyperParameterScalingType


class CreateActionResponseTypeDef(TypedDict, total=False):
    ActionArn: str


class CreateAlgorithmOutputTypeDef(TypedDict):
    AlgorithmArn: str
    ResponseMetadata: "ResponseMetadata"


class CreateAppImageConfigResponseTypeDef(TypedDict, total=False):
    AppImageConfigArn: str


class CreateAppResponseTypeDef(TypedDict, total=False):
    AppArn: str


class CreateArtifactResponseTypeDef(TypedDict, total=False):
    ArtifactArn: str


class CreateAutoMLJobResponseTypeDef(TypedDict):
    AutoMLJobArn: str


class CreateCodeRepositoryOutputTypeDef(TypedDict):
    CodeRepositoryArn: str
    ResponseMetadata: "ResponseMetadata"


class CreateCompilationJobResponseTypeDef(TypedDict):
    CompilationJobArn: str


class CreateContextResponseTypeDef(TypedDict, total=False):
    ContextArn: str


class CreateDataQualityJobDefinitionResponseTypeDef(TypedDict):
    JobDefinitionArn: str


class CreateDomainResponseTypeDef(TypedDict, total=False):
    DomainArn: str
    Url: str


class CreateEndpointConfigOutputTypeDef(TypedDict):
    EndpointConfigArn: str
    ResponseMetadata: "ResponseMetadata"


class CreateEndpointOutputTypeDef(TypedDict):
    EndpointArn: str
    ResponseMetadata: "ResponseMetadata"


class CreateExperimentResponseTypeDef(TypedDict, total=False):
    ExperimentArn: str


class CreateFeatureGroupResponseTypeDef(TypedDict):
    FeatureGroupArn: str


class CreateFlowDefinitionResponseTypeDef(TypedDict):
    FlowDefinitionArn: str


class CreateHumanTaskUiResponseTypeDef(TypedDict):
    HumanTaskUiArn: str


class CreateHyperParameterTuningJobResponseTypeDef(TypedDict):
    HyperParameterTuningJobArn: str


class CreateImageResponseTypeDef(TypedDict, total=False):
    ImageArn: str


class CreateImageVersionResponseTypeDef(TypedDict, total=False):
    ImageVersionArn: str


class CreateLabelingJobResponseTypeDef(TypedDict):
    LabelingJobArn: str


class CreateModelBiasJobDefinitionResponseTypeDef(TypedDict):
    JobDefinitionArn: str


class CreateModelExplainabilityJobDefinitionResponseTypeDef(TypedDict):
    JobDefinitionArn: str


class CreateModelOutputTypeDef(TypedDict):
    ModelArn: str
    ResponseMetadata: "ResponseMetadata"


class CreateModelPackageGroupOutputTypeDef(TypedDict):
    ModelPackageGroupArn: str
    ResponseMetadata: "ResponseMetadata"


class CreateModelPackageOutputTypeDef(TypedDict):
    ModelPackageArn: str
    ResponseMetadata: "ResponseMetadata"


class CreateModelQualityJobDefinitionResponseTypeDef(TypedDict):
    JobDefinitionArn: str


class CreateMonitoringScheduleResponseTypeDef(TypedDict):
    MonitoringScheduleArn: str


class CreateNotebookInstanceLifecycleConfigOutputTypeDef(TypedDict):
    NotebookInstanceLifecycleConfigArn: str
    ResponseMetadata: "ResponseMetadata"


class CreateNotebookInstanceOutputTypeDef(TypedDict):
    NotebookInstanceArn: str
    ResponseMetadata: "ResponseMetadata"


class CreatePipelineResponseTypeDef(TypedDict, total=False):
    PipelineArn: str


class CreatePresignedDomainUrlResponseTypeDef(TypedDict, total=False):
    AuthorizedUrl: str


class CreatePresignedNotebookInstanceUrlOutputTypeDef(TypedDict):
    AuthorizedUrl: str
    ResponseMetadata: "ResponseMetadata"


class CreateProcessingJobResponseTypeDef(TypedDict):
    ProcessingJobArn: str


class CreateProjectOutputTypeDef(TypedDict):
    ProjectArn: str
    ProjectId: str
    ResponseMetadata: "ResponseMetadata"


class CreateTrainingJobResponseTypeDef(TypedDict):
    TrainingJobArn: str


class CreateTransformJobResponseTypeDef(TypedDict):
    TransformJobArn: str


class CreateTrialComponentResponseTypeDef(TypedDict, total=False):
    TrialComponentArn: str


class CreateTrialResponseTypeDef(TypedDict, total=False):
    TrialArn: str


class CreateUserProfileResponseTypeDef(TypedDict, total=False):
    UserProfileArn: str


class CreateWorkforceResponseTypeDef(TypedDict):
    WorkforceArn: str


class CreateWorkteamResponseTypeDef(TypedDict, total=False):
    WorkteamArn: str


class _RequiredCustomImageTypeDef(TypedDict):
    ImageName: str
    AppImageConfigName: str


class CustomImageTypeDef(_RequiredCustomImageTypeDef, total=False):
    ImageVersionNumber: int


class DataCaptureConfigSummaryTypeDef(TypedDict):
    EnableCapture: bool
    CaptureStatus: CaptureStatus
    CurrentSamplingPercentage: int
    DestinationS3Uri: str
    KmsKeyId: str


class _RequiredDataCaptureConfigTypeDef(TypedDict):
    InitialSamplingPercentage: int
    DestinationS3Uri: str
    CaptureOptions: List["CaptureOptionTypeDef"]


class DataCaptureConfigTypeDef(_RequiredDataCaptureConfigTypeDef, total=False):
    EnableCapture: bool
    KmsKeyId: str
    CaptureContentTypeHeader: "CaptureContentTypeHeaderTypeDef"


class DataCatalogConfigTypeDef(TypedDict):
    TableName: str
    Catalog: str
    Database: str


class DataProcessingTypeDef(TypedDict, total=False):
    InputFilter: str
    OutputFilter: str
    JoinSource: JoinSource


class _RequiredDataQualityAppSpecificationTypeDef(TypedDict):
    ImageUri: str


class DataQualityAppSpecificationTypeDef(_RequiredDataQualityAppSpecificationTypeDef, total=False):
    ContainerEntrypoint: List[str]
    ContainerArguments: List[str]
    RecordPreprocessorSourceUri: str
    PostAnalyticsProcessorSourceUri: str
    Environment: Dict[str, str]


class DataQualityBaselineConfigTypeDef(TypedDict, total=False):
    BaseliningJobName: str
    ConstraintsResource: "MonitoringConstraintsResourceTypeDef"
    StatisticsResource: "MonitoringStatisticsResourceTypeDef"


class DataQualityJobInputTypeDef(TypedDict):
    EndpointInput: "EndpointInputTypeDef"


class DataSourceTypeDef(TypedDict, total=False):
    S3DataSource: "S3DataSourceTypeDef"
    FileSystemDataSource: "FileSystemDataSourceTypeDef"


class DatasetDefinitionTypeDef(TypedDict, total=False):
    AthenaDatasetDefinition: "AthenaDatasetDefinitionTypeDef"
    RedshiftDatasetDefinition: "RedshiftDatasetDefinitionTypeDef"
    LocalPath: str
    DataDistributionType: DataDistributionType
    InputMode: InputMode


class _RequiredDebugHookConfigTypeDef(TypedDict):
    S3OutputPath: str


class DebugHookConfigTypeDef(_RequiredDebugHookConfigTypeDef, total=False):
    LocalPath: str
    HookParameters: Dict[str, str]
    CollectionConfigurations: List["CollectionConfigurationTypeDef"]


class _RequiredDebugRuleConfigurationTypeDef(TypedDict):
    RuleConfigurationName: str
    RuleEvaluatorImage: str


class DebugRuleConfigurationTypeDef(_RequiredDebugRuleConfigurationTypeDef, total=False):
    LocalPath: str
    S3OutputPath: str
    InstanceType: ProcessingInstanceType
    VolumeSizeInGB: int
    RuleParameters: Dict[str, str]


class DebugRuleEvaluationStatusTypeDef(TypedDict, total=False):
    RuleConfigurationName: str
    RuleEvaluationJobArn: str
    RuleEvaluationStatus: RuleEvaluationStatus
    StatusDetails: str
    LastModifiedTime: datetime


class DeleteActionResponseTypeDef(TypedDict, total=False):
    ActionArn: str


class DeleteArtifactResponseTypeDef(TypedDict, total=False):
    ArtifactArn: str


class DeleteAssociationResponseTypeDef(TypedDict, total=False):
    SourceArn: str
    DestinationArn: str


class DeleteContextResponseTypeDef(TypedDict, total=False):
    ContextArn: str


class DeleteExperimentResponseTypeDef(TypedDict, total=False):
    ExperimentArn: str


class DeletePipelineResponseTypeDef(TypedDict, total=False):
    PipelineArn: str


class DeleteTrialComponentResponseTypeDef(TypedDict, total=False):
    TrialComponentArn: str


class DeleteTrialResponseTypeDef(TypedDict, total=False):
    TrialArn: str


class DeleteWorkteamResponseTypeDef(TypedDict):
    Success: bool


class DeployedImageTypeDef(TypedDict, total=False):
    SpecifiedImage: str
    ResolvedImage: str
    ResolutionTime: datetime


class _RequiredDeploymentConfigTypeDef(TypedDict):
    BlueGreenUpdatePolicy: "BlueGreenUpdatePolicyTypeDef"


class DeploymentConfigTypeDef(_RequiredDeploymentConfigTypeDef, total=False):
    AutoRollbackConfiguration: "AutoRollbackConfigTypeDef"


class DescribeActionResponseTypeDef(TypedDict, total=False):
    ActionName: str
    ActionArn: str
    Source: "ActionSourceTypeDef"
    ActionType: str
    Description: str
    Status: ActionStatus
    Properties: Dict[str, str]
    CreationTime: datetime
    CreatedBy: "UserContextTypeDef"
    LastModifiedTime: datetime
    LastModifiedBy: "UserContextTypeDef"
    MetadataProperties: "MetadataPropertiesTypeDef"


class DescribeAlgorithmOutputTypeDef(TypedDict):
    AlgorithmName: str
    AlgorithmArn: str
    AlgorithmDescription: str
    CreationTime: datetime
    TrainingSpecification: "TrainingSpecificationTypeDef"
    InferenceSpecification: "InferenceSpecificationTypeDef"
    ValidationSpecification: "AlgorithmValidationSpecificationTypeDef"
    AlgorithmStatus: AlgorithmStatus
    AlgorithmStatusDetails: "AlgorithmStatusDetailsTypeDef"
    ProductId: str
    CertifyForMarketplace: bool
    ResponseMetadata: "ResponseMetadata"


class DescribeAppImageConfigResponseTypeDef(TypedDict, total=False):
    AppImageConfigArn: str
    AppImageConfigName: str
    CreationTime: datetime
    LastModifiedTime: datetime
    KernelGatewayImageConfig: "KernelGatewayImageConfigTypeDef"


class DescribeAppResponseTypeDef(TypedDict, total=False):
    AppArn: str
    AppType: AppType
    AppName: str
    DomainId: str
    UserProfileName: str
    Status: AppStatus
    LastHealthCheckTimestamp: datetime
    LastUserActivityTimestamp: datetime
    CreationTime: datetime
    FailureReason: str
    ResourceSpec: "ResourceSpecTypeDef"


class DescribeArtifactResponseTypeDef(TypedDict, total=False):
    ArtifactName: str
    ArtifactArn: str
    Source: "ArtifactSourceTypeDef"
    ArtifactType: str
    Properties: Dict[str, str]
    CreationTime: datetime
    CreatedBy: "UserContextTypeDef"
    LastModifiedTime: datetime
    LastModifiedBy: "UserContextTypeDef"
    MetadataProperties: "MetadataPropertiesTypeDef"


class _RequiredDescribeAutoMLJobResponseTypeDef(TypedDict):
    AutoMLJobName: str
    AutoMLJobArn: str
    InputDataConfig: List["AutoMLChannelTypeDef"]
    OutputDataConfig: "AutoMLOutputDataConfigTypeDef"
    RoleArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    AutoMLJobStatus: AutoMLJobStatus
    AutoMLJobSecondaryStatus: AutoMLJobSecondaryStatus


class DescribeAutoMLJobResponseTypeDef(_RequiredDescribeAutoMLJobResponseTypeDef, total=False):
    AutoMLJobObjective: "AutoMLJobObjectiveTypeDef"
    ProblemType: ProblemType
    AutoMLJobConfig: "AutoMLJobConfigTypeDef"
    EndTime: datetime
    FailureReason: str
    PartialFailureReasons: List["AutoMLPartialFailureReasonTypeDef"]
    BestCandidate: "AutoMLCandidateTypeDef"
    GenerateCandidateDefinitionsOnly: bool
    AutoMLJobArtifacts: "AutoMLJobArtifactsTypeDef"
    ResolvedAttributes: "ResolvedAttributesTypeDef"
    ModelDeployConfig: "ModelDeployConfigTypeDef"
    ModelDeployResult: "ModelDeployResultTypeDef"


class DescribeCodeRepositoryOutputTypeDef(TypedDict):
    CodeRepositoryName: str
    CodeRepositoryArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    GitConfig: "GitConfigTypeDef"
    ResponseMetadata: "ResponseMetadata"


class _RequiredDescribeCompilationJobResponseTypeDef(TypedDict):
    CompilationJobName: str
    CompilationJobArn: str
    CompilationJobStatus: CompilationJobStatus
    StoppingCondition: "StoppingConditionTypeDef"
    CreationTime: datetime
    LastModifiedTime: datetime
    FailureReason: str
    ModelArtifacts: "ModelArtifactsTypeDef"
    RoleArn: str
    InputConfig: "InputConfigTypeDef"
    OutputConfig: "OutputConfigTypeDef"


class DescribeCompilationJobResponseTypeDef(
    _RequiredDescribeCompilationJobResponseTypeDef, total=False
):
    CompilationStartTime: datetime
    CompilationEndTime: datetime
    ModelDigests: "ModelDigestsTypeDef"


class DescribeContextResponseTypeDef(TypedDict, total=False):
    ContextName: str
    ContextArn: str
    Source: "ContextSourceTypeDef"
    ContextType: str
    Description: str
    Properties: Dict[str, str]
    CreationTime: datetime
    CreatedBy: "UserContextTypeDef"
    LastModifiedTime: datetime
    LastModifiedBy: "UserContextTypeDef"


class _RequiredDescribeDataQualityJobDefinitionResponseTypeDef(TypedDict):
    JobDefinitionArn: str
    JobDefinitionName: str
    CreationTime: datetime
    DataQualityAppSpecification: "DataQualityAppSpecificationTypeDef"
    DataQualityJobInput: "DataQualityJobInputTypeDef"
    DataQualityJobOutputConfig: "MonitoringOutputConfigTypeDef"
    JobResources: "MonitoringResourcesTypeDef"
    RoleArn: str


class DescribeDataQualityJobDefinitionResponseTypeDef(
    _RequiredDescribeDataQualityJobDefinitionResponseTypeDef, total=False
):
    DataQualityBaselineConfig: "DataQualityBaselineConfigTypeDef"
    NetworkConfig: "MonitoringNetworkConfigTypeDef"
    StoppingCondition: "MonitoringStoppingConditionTypeDef"


class _RequiredDescribeDeviceFleetResponseTypeDef(TypedDict):
    DeviceFleetName: str
    DeviceFleetArn: str
    OutputConfig: "EdgeOutputConfigTypeDef"
    CreationTime: datetime
    LastModifiedTime: datetime


class DescribeDeviceFleetResponseTypeDef(_RequiredDescribeDeviceFleetResponseTypeDef, total=False):
    Description: str
    RoleArn: str
    IotRoleAlias: str


class _RequiredDescribeDeviceResponseTypeDef(TypedDict):
    DeviceName: str
    DeviceFleetName: str
    RegistrationTime: datetime


class DescribeDeviceResponseTypeDef(_RequiredDescribeDeviceResponseTypeDef, total=False):
    DeviceArn: str
    Description: str
    IotThingName: str
    LatestHeartbeat: datetime
    Models: List["EdgeModelTypeDef"]
    MaxModels: int
    NextToken: str


class DescribeDomainResponseTypeDef(TypedDict, total=False):
    DomainArn: str
    DomainId: str
    DomainName: str
    HomeEfsFileSystemId: str
    SingleSignOnManagedApplicationInstanceId: str
    Status: DomainStatus
    CreationTime: datetime
    LastModifiedTime: datetime
    FailureReason: str
    AuthMode: AuthMode
    DefaultUserSettings: "UserSettingsTypeDef"
    AppNetworkAccessType: AppNetworkAccessType
    HomeEfsFileSystemKmsKeyId: str
    SubnetIds: List[str]
    Url: str
    VpcId: str
    KmsKeyId: str


class _RequiredDescribeEdgePackagingJobResponseTypeDef(TypedDict):
    EdgePackagingJobArn: str
    EdgePackagingJobName: str
    EdgePackagingJobStatus: EdgePackagingJobStatus


class DescribeEdgePackagingJobResponseTypeDef(
    _RequiredDescribeEdgePackagingJobResponseTypeDef, total=False
):
    CompilationJobName: str
    ModelName: str
    ModelVersion: str
    RoleArn: str
    OutputConfig: "EdgeOutputConfigTypeDef"
    ResourceKey: str
    EdgePackagingJobStatusMessage: str
    CreationTime: datetime
    LastModifiedTime: datetime
    ModelArtifact: str
    ModelSignature: str


class DescribeEndpointConfigOutputTypeDef(TypedDict):
    EndpointConfigName: str
    EndpointConfigArn: str
    ProductionVariants: List["ProductionVariantTypeDef"]
    DataCaptureConfig: "DataCaptureConfigTypeDef"
    KmsKeyId: str
    CreationTime: datetime
    ResponseMetadata: "ResponseMetadata"


class DescribeEndpointOutputTypeDef(TypedDict):
    EndpointName: str
    EndpointArn: str
    EndpointConfigName: str
    ProductionVariants: List["ProductionVariantSummaryTypeDef"]
    DataCaptureConfig: "DataCaptureConfigSummaryTypeDef"
    EndpointStatus: EndpointStatus
    FailureReason: str
    CreationTime: datetime
    LastModifiedTime: datetime
    LastDeploymentConfig: "DeploymentConfigTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeExperimentResponseTypeDef(TypedDict, total=False):
    ExperimentName: str
    ExperimentArn: str
    DisplayName: str
    Source: "ExperimentSourceTypeDef"
    Description: str
    CreationTime: datetime
    CreatedBy: "UserContextTypeDef"
    LastModifiedTime: datetime
    LastModifiedBy: "UserContextTypeDef"


class _RequiredDescribeFeatureGroupResponseTypeDef(TypedDict):
    FeatureGroupArn: str
    FeatureGroupName: str
    RecordIdentifierFeatureName: str
    EventTimeFeatureName: str
    FeatureDefinitions: List["FeatureDefinitionTypeDef"]
    CreationTime: datetime
    NextToken: str


class DescribeFeatureGroupResponseTypeDef(
    _RequiredDescribeFeatureGroupResponseTypeDef, total=False
):
    OnlineStoreConfig: "OnlineStoreConfigTypeDef"
    OfflineStoreConfig: "OfflineStoreConfigTypeDef"
    RoleArn: str
    FeatureGroupStatus: FeatureGroupStatus
    OfflineStoreStatus: "OfflineStoreStatusTypeDef"
    FailureReason: str
    Description: str


class _RequiredDescribeFlowDefinitionResponseTypeDef(TypedDict):
    FlowDefinitionArn: str
    FlowDefinitionName: str
    FlowDefinitionStatus: FlowDefinitionStatus
    CreationTime: datetime
    HumanLoopConfig: "HumanLoopConfigTypeDef"
    OutputConfig: "FlowDefinitionOutputConfigTypeDef"
    RoleArn: str


class DescribeFlowDefinitionResponseTypeDef(
    _RequiredDescribeFlowDefinitionResponseTypeDef, total=False
):
    HumanLoopRequestSource: "HumanLoopRequestSourceTypeDef"
    HumanLoopActivationConfig: "HumanLoopActivationConfigTypeDef"
    FailureReason: str


class _RequiredDescribeHumanTaskUiResponseTypeDef(TypedDict):
    HumanTaskUiArn: str
    HumanTaskUiName: str
    CreationTime: datetime
    UiTemplate: "UiTemplateInfoTypeDef"


class DescribeHumanTaskUiResponseTypeDef(_RequiredDescribeHumanTaskUiResponseTypeDef, total=False):
    HumanTaskUiStatus: HumanTaskUiStatus


class _RequiredDescribeHyperParameterTuningJobResponseTypeDef(TypedDict):
    HyperParameterTuningJobName: str
    HyperParameterTuningJobArn: str
    HyperParameterTuningJobConfig: "HyperParameterTuningJobConfigTypeDef"
    HyperParameterTuningJobStatus: HyperParameterTuningJobStatus
    CreationTime: datetime
    TrainingJobStatusCounters: "TrainingJobStatusCountersTypeDef"
    ObjectiveStatusCounters: "ObjectiveStatusCountersTypeDef"


class DescribeHyperParameterTuningJobResponseTypeDef(
    _RequiredDescribeHyperParameterTuningJobResponseTypeDef, total=False
):
    TrainingJobDefinition: "HyperParameterTrainingJobDefinitionTypeDef"
    TrainingJobDefinitions: List["HyperParameterTrainingJobDefinitionTypeDef"]
    HyperParameterTuningEndTime: datetime
    LastModifiedTime: datetime
    BestTrainingJob: "HyperParameterTrainingJobSummaryTypeDef"
    OverallBestTrainingJob: "HyperParameterTrainingJobSummaryTypeDef"
    WarmStartConfig: "HyperParameterTuningJobWarmStartConfigTypeDef"
    FailureReason: str


class DescribeImageResponseTypeDef(TypedDict, total=False):
    CreationTime: datetime
    Description: str
    DisplayName: str
    FailureReason: str
    ImageArn: str
    ImageName: str
    ImageStatus: ImageStatus
    LastModifiedTime: datetime
    RoleArn: str


class DescribeImageVersionResponseTypeDef(TypedDict, total=False):
    BaseImage: str
    ContainerImage: str
    CreationTime: datetime
    FailureReason: str
    ImageArn: str
    ImageVersionArn: str
    ImageVersionStatus: ImageVersionStatus
    LastModifiedTime: datetime
    Version: int


class _RequiredDescribeLabelingJobResponseTypeDef(TypedDict):
    LabelingJobStatus: LabelingJobStatus
    LabelCounters: "LabelCountersTypeDef"
    CreationTime: datetime
    LastModifiedTime: datetime
    JobReferenceCode: str
    LabelingJobName: str
    LabelingJobArn: str
    InputConfig: "LabelingJobInputConfigTypeDef"
    OutputConfig: "LabelingJobOutputConfigTypeDef"
    RoleArn: str
    HumanTaskConfig: "HumanTaskConfigTypeDef"


class DescribeLabelingJobResponseTypeDef(_RequiredDescribeLabelingJobResponseTypeDef, total=False):
    FailureReason: str
    LabelAttributeName: str
    LabelCategoryConfigS3Uri: str
    StoppingConditions: "LabelingJobStoppingConditionsTypeDef"
    LabelingJobAlgorithmsConfig: "LabelingJobAlgorithmsConfigTypeDef"
    Tags: List["TagTypeDef"]
    LabelingJobOutput: "LabelingJobOutputTypeDef"


class _RequiredDescribeModelBiasJobDefinitionResponseTypeDef(TypedDict):
    JobDefinitionArn: str
    JobDefinitionName: str
    CreationTime: datetime
    ModelBiasAppSpecification: "ModelBiasAppSpecificationTypeDef"
    ModelBiasJobInput: "ModelBiasJobInputTypeDef"
    ModelBiasJobOutputConfig: "MonitoringOutputConfigTypeDef"
    JobResources: "MonitoringResourcesTypeDef"
    RoleArn: str


class DescribeModelBiasJobDefinitionResponseTypeDef(
    _RequiredDescribeModelBiasJobDefinitionResponseTypeDef, total=False
):
    ModelBiasBaselineConfig: "ModelBiasBaselineConfigTypeDef"
    NetworkConfig: "MonitoringNetworkConfigTypeDef"
    StoppingCondition: "MonitoringStoppingConditionTypeDef"


class _RequiredDescribeModelExplainabilityJobDefinitionResponseTypeDef(TypedDict):
    JobDefinitionArn: str
    JobDefinitionName: str
    CreationTime: datetime
    ModelExplainabilityAppSpecification: "ModelExplainabilityAppSpecificationTypeDef"
    ModelExplainabilityJobInput: "ModelExplainabilityJobInputTypeDef"
    ModelExplainabilityJobOutputConfig: "MonitoringOutputConfigTypeDef"
    JobResources: "MonitoringResourcesTypeDef"
    RoleArn: str


class DescribeModelExplainabilityJobDefinitionResponseTypeDef(
    _RequiredDescribeModelExplainabilityJobDefinitionResponseTypeDef, total=False
):
    ModelExplainabilityBaselineConfig: "ModelExplainabilityBaselineConfigTypeDef"
    NetworkConfig: "MonitoringNetworkConfigTypeDef"
    StoppingCondition: "MonitoringStoppingConditionTypeDef"


class DescribeModelOutputTypeDef(TypedDict):
    ModelName: str
    PrimaryContainer: "ContainerDefinitionTypeDef"
    Containers: List["ContainerDefinitionTypeDef"]
    InferenceExecutionConfig: "InferenceExecutionConfigTypeDef"
    ExecutionRoleArn: str
    VpcConfig: "VpcConfigTypeDef"
    CreationTime: datetime
    ModelArn: str
    EnableNetworkIsolation: bool
    ResponseMetadata: "ResponseMetadata"


class DescribeModelPackageGroupOutputTypeDef(TypedDict):
    ModelPackageGroupName: str
    ModelPackageGroupArn: str
    ModelPackageGroupDescription: str
    CreationTime: datetime
    CreatedBy: "UserContextTypeDef"
    ModelPackageGroupStatus: ModelPackageGroupStatus
    ResponseMetadata: "ResponseMetadata"


class DescribeModelPackageOutputTypeDef(TypedDict):
    ModelPackageName: str
    ModelPackageGroupName: str
    ModelPackageVersion: int
    ModelPackageArn: str
    ModelPackageDescription: str
    CreationTime: datetime
    InferenceSpecification: "InferenceSpecificationTypeDef"
    SourceAlgorithmSpecification: "SourceAlgorithmSpecificationTypeDef"
    ValidationSpecification: "ModelPackageValidationSpecificationTypeDef"
    ModelPackageStatus: ModelPackageStatus
    ModelPackageStatusDetails: "ModelPackageStatusDetailsTypeDef"
    CertifyForMarketplace: bool
    ModelApprovalStatus: ModelApprovalStatus
    CreatedBy: "UserContextTypeDef"
    MetadataProperties: "MetadataPropertiesTypeDef"
    ModelMetrics: "ModelMetricsTypeDef"
    LastModifiedTime: datetime
    LastModifiedBy: "UserContextTypeDef"
    ApprovalDescription: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredDescribeModelQualityJobDefinitionResponseTypeDef(TypedDict):
    JobDefinitionArn: str
    JobDefinitionName: str
    CreationTime: datetime
    ModelQualityAppSpecification: "ModelQualityAppSpecificationTypeDef"
    ModelQualityJobInput: "ModelQualityJobInputTypeDef"
    ModelQualityJobOutputConfig: "MonitoringOutputConfigTypeDef"
    JobResources: "MonitoringResourcesTypeDef"
    RoleArn: str


class DescribeModelQualityJobDefinitionResponseTypeDef(
    _RequiredDescribeModelQualityJobDefinitionResponseTypeDef, total=False
):
    ModelQualityBaselineConfig: "ModelQualityBaselineConfigTypeDef"
    NetworkConfig: "MonitoringNetworkConfigTypeDef"
    StoppingCondition: "MonitoringStoppingConditionTypeDef"


class _RequiredDescribeMonitoringScheduleResponseTypeDef(TypedDict):
    MonitoringScheduleArn: str
    MonitoringScheduleName: str
    MonitoringScheduleStatus: ScheduleStatus
    CreationTime: datetime
    LastModifiedTime: datetime
    MonitoringScheduleConfig: "MonitoringScheduleConfigTypeDef"


class DescribeMonitoringScheduleResponseTypeDef(
    _RequiredDescribeMonitoringScheduleResponseTypeDef, total=False
):
    MonitoringType: MonitoringType
    FailureReason: str
    EndpointName: str
    LastMonitoringExecutionSummary: "MonitoringExecutionSummaryTypeDef"


class DescribeNotebookInstanceLifecycleConfigOutputTypeDef(TypedDict):
    NotebookInstanceLifecycleConfigArn: str
    NotebookInstanceLifecycleConfigName: str
    OnCreate: List["NotebookInstanceLifecycleHookTypeDef"]
    OnStart: List["NotebookInstanceLifecycleHookTypeDef"]
    LastModifiedTime: datetime
    CreationTime: datetime
    ResponseMetadata: "ResponseMetadata"


class DescribeNotebookInstanceOutputTypeDef(TypedDict):
    NotebookInstanceArn: str
    NotebookInstanceName: str
    NotebookInstanceStatus: NotebookInstanceStatus
    FailureReason: str
    Url: str
    InstanceType: InstanceType
    SubnetId: str
    SecurityGroups: List[str]
    RoleArn: str
    KmsKeyId: str
    NetworkInterfaceId: str
    LastModifiedTime: datetime
    CreationTime: datetime
    NotebookInstanceLifecycleConfigName: str
    DirectInternetAccess: DirectInternetAccess
    VolumeSizeInGB: int
    AcceleratorTypes: List[NotebookInstanceAcceleratorType]
    DefaultCodeRepository: str
    AdditionalCodeRepositories: List[str]
    RootAccess: RootAccess
    ResponseMetadata: "ResponseMetadata"


class DescribePipelineDefinitionForExecutionResponseTypeDef(TypedDict, total=False):
    PipelineDefinition: str
    CreationTime: datetime


class DescribePipelineExecutionResponseTypeDef(TypedDict, total=False):
    PipelineArn: str
    PipelineExecutionArn: str
    PipelineExecutionDisplayName: str
    PipelineExecutionStatus: PipelineExecutionStatus
    PipelineExecutionDescription: str
    CreationTime: datetime
    LastModifiedTime: datetime
    CreatedBy: "UserContextTypeDef"
    LastModifiedBy: "UserContextTypeDef"


class DescribePipelineResponseTypeDef(TypedDict, total=False):
    PipelineArn: str
    PipelineName: str
    PipelineDisplayName: str
    PipelineDefinition: str
    PipelineDescription: str
    RoleArn: str
    PipelineStatus: Literal["Active"]
    CreationTime: datetime
    LastModifiedTime: datetime
    LastRunTime: datetime
    CreatedBy: "UserContextTypeDef"
    LastModifiedBy: "UserContextTypeDef"


class _RequiredDescribeProcessingJobResponseTypeDef(TypedDict):
    ProcessingJobName: str
    ProcessingResources: "ProcessingResourcesTypeDef"
    AppSpecification: "AppSpecificationTypeDef"
    ProcessingJobArn: str
    ProcessingJobStatus: ProcessingJobStatus
    CreationTime: datetime


class DescribeProcessingJobResponseTypeDef(
    _RequiredDescribeProcessingJobResponseTypeDef, total=False
):
    ProcessingInputs: List["ProcessingInputTypeDef"]
    ProcessingOutputConfig: "ProcessingOutputConfigTypeDef"
    StoppingCondition: "ProcessingStoppingConditionTypeDef"
    Environment: Dict[str, str]
    NetworkConfig: "NetworkConfigTypeDef"
    RoleArn: str
    ExperimentConfig: "ExperimentConfigTypeDef"
    ExitMessage: str
    FailureReason: str
    ProcessingEndTime: datetime
    ProcessingStartTime: datetime
    LastModifiedTime: datetime
    MonitoringScheduleArn: str
    AutoMLJobArn: str
    TrainingJobArn: str


class DescribeProjectOutputTypeDef(TypedDict):
    ProjectArn: str
    ProjectName: str
    ProjectId: str
    ProjectDescription: str
    ServiceCatalogProvisioningDetails: "ServiceCatalogProvisioningDetailsTypeDef"
    ServiceCatalogProvisionedProductDetails: "ServiceCatalogProvisionedProductDetailsTypeDef"
    ProjectStatus: ProjectStatus
    CreatedBy: "UserContextTypeDef"
    CreationTime: datetime
    ResponseMetadata: "ResponseMetadata"


class DescribeSubscribedWorkteamResponseTypeDef(TypedDict):
    SubscribedWorkteam: "SubscribedWorkteamTypeDef"


class _RequiredDescribeTrainingJobResponseTypeDef(TypedDict):
    TrainingJobName: str
    TrainingJobArn: str
    ModelArtifacts: "ModelArtifactsTypeDef"
    TrainingJobStatus: TrainingJobStatus
    SecondaryStatus: SecondaryStatus
    AlgorithmSpecification: "AlgorithmSpecificationTypeDef"
    ResourceConfig: "ResourceConfigTypeDef"
    StoppingCondition: "StoppingConditionTypeDef"
    CreationTime: datetime


class DescribeTrainingJobResponseTypeDef(_RequiredDescribeTrainingJobResponseTypeDef, total=False):
    TuningJobArn: str
    LabelingJobArn: str
    AutoMLJobArn: str
    FailureReason: str
    HyperParameters: Dict[str, str]
    RoleArn: str
    InputDataConfig: List["ChannelTypeDef"]
    OutputDataConfig: "OutputDataConfigTypeDef"
    VpcConfig: "VpcConfigTypeDef"
    TrainingStartTime: datetime
    TrainingEndTime: datetime
    LastModifiedTime: datetime
    SecondaryStatusTransitions: List["SecondaryStatusTransitionTypeDef"]
    FinalMetricDataList: List["MetricDataTypeDef"]
    EnableNetworkIsolation: bool
    EnableInterContainerTrafficEncryption: bool
    EnableManagedSpotTraining: bool
    CheckpointConfig: "CheckpointConfigTypeDef"
    TrainingTimeInSeconds: int
    BillableTimeInSeconds: int
    DebugHookConfig: "DebugHookConfigTypeDef"
    ExperimentConfig: "ExperimentConfigTypeDef"
    DebugRuleConfigurations: List["DebugRuleConfigurationTypeDef"]
    TensorBoardOutputConfig: "TensorBoardOutputConfigTypeDef"
    DebugRuleEvaluationStatuses: List["DebugRuleEvaluationStatusTypeDef"]
    ProfilerConfig: "ProfilerConfigTypeDef"
    ProfilerRuleConfigurations: List["ProfilerRuleConfigurationTypeDef"]
    ProfilerRuleEvaluationStatuses: List["ProfilerRuleEvaluationStatusTypeDef"]
    ProfilingStatus: ProfilingStatus
    RetryStrategy: "RetryStrategyTypeDef"
    Environment: Dict[str, str]


class _RequiredDescribeTransformJobResponseTypeDef(TypedDict):
    TransformJobName: str
    TransformJobArn: str
    TransformJobStatus: TransformJobStatus
    ModelName: str
    TransformInput: "TransformInputTypeDef"
    TransformResources: "TransformResourcesTypeDef"
    CreationTime: datetime


class DescribeTransformJobResponseTypeDef(
    _RequiredDescribeTransformJobResponseTypeDef, total=False
):
    FailureReason: str
    MaxConcurrentTransforms: int
    ModelClientConfig: "ModelClientConfigTypeDef"
    MaxPayloadInMB: int
    BatchStrategy: BatchStrategy
    Environment: Dict[str, str]
    TransformOutput: "TransformOutputTypeDef"
    TransformStartTime: datetime
    TransformEndTime: datetime
    LabelingJobArn: str
    AutoMLJobArn: str
    DataProcessing: "DataProcessingTypeDef"
    ExperimentConfig: "ExperimentConfigTypeDef"


class DescribeTrialComponentResponseTypeDef(TypedDict, total=False):
    TrialComponentName: str
    TrialComponentArn: str
    DisplayName: str
    Source: "TrialComponentSourceTypeDef"
    Status: "TrialComponentStatusTypeDef"
    StartTime: datetime
    EndTime: datetime
    CreationTime: datetime
    CreatedBy: "UserContextTypeDef"
    LastModifiedTime: datetime
    LastModifiedBy: "UserContextTypeDef"
    Parameters: Dict[str, "TrialComponentParameterValueTypeDef"]
    InputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"]
    OutputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"]
    MetadataProperties: "MetadataPropertiesTypeDef"
    Metrics: List["TrialComponentMetricSummaryTypeDef"]


class DescribeTrialResponseTypeDef(TypedDict, total=False):
    TrialName: str
    TrialArn: str
    DisplayName: str
    ExperimentName: str
    Source: "TrialSourceTypeDef"
    CreationTime: datetime
    CreatedBy: "UserContextTypeDef"
    LastModifiedTime: datetime
    LastModifiedBy: "UserContextTypeDef"
    MetadataProperties: "MetadataPropertiesTypeDef"


class DescribeUserProfileResponseTypeDef(TypedDict, total=False):
    DomainId: str
    UserProfileArn: str
    UserProfileName: str
    HomeEfsFileSystemUid: str
    Status: UserProfileStatus
    LastModifiedTime: datetime
    CreationTime: datetime
    FailureReason: str
    SingleSignOnUserIdentifier: str
    SingleSignOnUserValue: str
    UserSettings: "UserSettingsTypeDef"


class DescribeWorkforceResponseTypeDef(TypedDict):
    Workforce: "WorkforceTypeDef"


class DescribeWorkteamResponseTypeDef(TypedDict):
    Workteam: "WorkteamTypeDef"


class _RequiredDesiredWeightAndCapacityTypeDef(TypedDict):
    VariantName: str


class DesiredWeightAndCapacityTypeDef(_RequiredDesiredWeightAndCapacityTypeDef, total=False):
    DesiredWeight: float
    DesiredInstanceCount: int


class _RequiredDeviceFleetSummaryTypeDef(TypedDict):
    DeviceFleetArn: str
    DeviceFleetName: str


class DeviceFleetSummaryTypeDef(_RequiredDeviceFleetSummaryTypeDef, total=False):
    CreationTime: datetime
    LastModifiedTime: datetime


class DeviceStatsTypeDef(TypedDict):
    ConnectedDeviceCount: int
    RegisteredDeviceCount: int


class _RequiredDeviceSummaryTypeDef(TypedDict):
    DeviceName: str
    DeviceArn: str


class DeviceSummaryTypeDef(_RequiredDeviceSummaryTypeDef, total=False):
    Description: str
    DeviceFleetName: str
    IotThingName: str
    RegistrationTime: datetime
    LatestHeartbeat: datetime
    Models: List["EdgeModelSummaryTypeDef"]


class _RequiredDeviceTypeDef(TypedDict):
    DeviceName: str


class DeviceTypeDef(_RequiredDeviceTypeDef, total=False):
    Description: str
    IotThingName: str


class DisassociateTrialComponentResponseTypeDef(TypedDict, total=False):
    TrialComponentArn: str
    TrialArn: str


class DomainDetailsTypeDef(TypedDict, total=False):
    DomainArn: str
    DomainId: str
    DomainName: str
    Status: DomainStatus
    CreationTime: datetime
    LastModifiedTime: datetime
    Url: str


class EdgeModelStatTypeDef(TypedDict):
    ModelName: str
    ModelVersion: str
    OfflineDeviceCount: int
    ConnectedDeviceCount: int
    ActiveDeviceCount: int
    SamplingDeviceCount: int


class EdgeModelSummaryTypeDef(TypedDict):
    ModelName: str
    ModelVersion: str


class _RequiredEdgeModelTypeDef(TypedDict):
    ModelName: str
    ModelVersion: str


class EdgeModelTypeDef(_RequiredEdgeModelTypeDef, total=False):
    LatestSampleTime: datetime
    LatestInference: datetime


class _RequiredEdgeOutputConfigTypeDef(TypedDict):
    S3OutputLocation: str


class EdgeOutputConfigTypeDef(_RequiredEdgeOutputConfigTypeDef, total=False):
    KmsKeyId: str


class _RequiredEdgePackagingJobSummaryTypeDef(TypedDict):
    EdgePackagingJobArn: str
    EdgePackagingJobName: str
    EdgePackagingJobStatus: EdgePackagingJobStatus


class EdgePackagingJobSummaryTypeDef(_RequiredEdgePackagingJobSummaryTypeDef, total=False):
    CompilationJobName: str
    ModelName: str
    ModelVersion: str
    CreationTime: datetime
    LastModifiedTime: datetime


class EndpointConfigSummaryTypeDef(TypedDict):
    EndpointConfigName: str
    EndpointConfigArn: str
    CreationTime: datetime


class _RequiredEndpointInputTypeDef(TypedDict):
    EndpointName: str
    LocalPath: str


class EndpointInputTypeDef(_RequiredEndpointInputTypeDef, total=False):
    S3InputMode: ProcessingS3InputMode
    S3DataDistributionType: ProcessingS3DataDistributionType
    FeaturesAttribute: str
    InferenceAttribute: str
    ProbabilityAttribute: str
    ProbabilityThresholdAttribute: float
    StartTimeOffset: str
    EndTimeOffset: str


class EndpointSummaryTypeDef(TypedDict):
    EndpointName: str
    EndpointArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    EndpointStatus: EndpointStatus


class _RequiredEndpointTypeDef(TypedDict):
    EndpointName: str
    EndpointArn: str
    EndpointConfigName: str
    EndpointStatus: EndpointStatus
    CreationTime: datetime
    LastModifiedTime: datetime


class EndpointTypeDef(_RequiredEndpointTypeDef, total=False):
    ProductionVariants: List["ProductionVariantSummaryTypeDef"]
    DataCaptureConfig: "DataCaptureConfigSummaryTypeDef"
    FailureReason: str
    MonitoringSchedules: List["MonitoringScheduleTypeDef"]
    Tags: List["TagTypeDef"]


class ExperimentConfigTypeDef(TypedDict, total=False):
    ExperimentName: str
    TrialName: str
    TrialComponentDisplayName: str


class _RequiredExperimentSourceTypeDef(TypedDict):
    SourceArn: str


class ExperimentSourceTypeDef(_RequiredExperimentSourceTypeDef, total=False):
    SourceType: str


class ExperimentSummaryTypeDef(TypedDict, total=False):
    ExperimentArn: str
    ExperimentName: str
    DisplayName: str
    ExperimentSource: "ExperimentSourceTypeDef"
    CreationTime: datetime
    LastModifiedTime: datetime


class ExperimentTypeDef(TypedDict, total=False):
    ExperimentName: str
    ExperimentArn: str
    DisplayName: str
    Source: "ExperimentSourceTypeDef"
    Description: str
    CreationTime: datetime
    CreatedBy: "UserContextTypeDef"
    LastModifiedTime: datetime
    LastModifiedBy: "UserContextTypeDef"
    Tags: List["TagTypeDef"]


class ExplainabilityTypeDef(TypedDict, total=False):
    Report: "MetricsSourceTypeDef"


class FeatureDefinitionTypeDef(TypedDict, total=False):
    FeatureName: str
    FeatureType: FeatureType


class _RequiredFeatureGroupSummaryTypeDef(TypedDict):
    FeatureGroupName: str
    FeatureGroupArn: str
    CreationTime: datetime


class FeatureGroupSummaryTypeDef(_RequiredFeatureGroupSummaryTypeDef, total=False):
    FeatureGroupStatus: FeatureGroupStatus
    OfflineStoreStatus: "OfflineStoreStatusTypeDef"


class FeatureGroupTypeDef(TypedDict, total=False):
    FeatureGroupArn: str
    FeatureGroupName: str
    RecordIdentifierFeatureName: str
    EventTimeFeatureName: str
    FeatureDefinitions: List["FeatureDefinitionTypeDef"]
    CreationTime: datetime
    OnlineStoreConfig: "OnlineStoreConfigTypeDef"
    OfflineStoreConfig: "OfflineStoreConfigTypeDef"
    RoleArn: str
    FeatureGroupStatus: FeatureGroupStatus
    OfflineStoreStatus: "OfflineStoreStatusTypeDef"
    FailureReason: str
    Description: str
    Tags: List["TagTypeDef"]


class FileSystemConfigTypeDef(TypedDict, total=False):
    MountPath: str
    DefaultUid: int
    DefaultGid: int


class FileSystemDataSourceTypeDef(TypedDict):
    FileSystemId: str
    FileSystemAccessMode: FileSystemAccessMode
    FileSystemType: FileSystemType
    DirectoryPath: str


class _RequiredFilterTypeDef(TypedDict):
    Name: str


class FilterTypeDef(_RequiredFilterTypeDef, total=False):
    Operator: Operator
    Value: str


_RequiredFinalAutoMLJobObjectiveMetricTypeDef = TypedDict(
    "_RequiredFinalAutoMLJobObjectiveMetricTypeDef",
    {"MetricName": AutoMLMetricEnum, "Value": float},
)
_OptionalFinalAutoMLJobObjectiveMetricTypeDef = TypedDict(
    "_OptionalFinalAutoMLJobObjectiveMetricTypeDef", {"Type": AutoMLJobObjectiveType}, total=False
)


class FinalAutoMLJobObjectiveMetricTypeDef(
    _RequiredFinalAutoMLJobObjectiveMetricTypeDef, _OptionalFinalAutoMLJobObjectiveMetricTypeDef
):
    pass


_RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {"MetricName": str, "Value": float},
)
_OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef = TypedDict(
    "_OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef",
    {"Type": HyperParameterTuningJobObjectiveType},
    total=False,
)


class FinalHyperParameterTuningJobObjectiveMetricTypeDef(
    _RequiredFinalHyperParameterTuningJobObjectiveMetricTypeDef,
    _OptionalFinalHyperParameterTuningJobObjectiveMetricTypeDef,
):
    pass


class _RequiredFlowDefinitionOutputConfigTypeDef(TypedDict):
    S3OutputPath: str


class FlowDefinitionOutputConfigTypeDef(_RequiredFlowDefinitionOutputConfigTypeDef, total=False):
    KmsKeyId: str


class _RequiredFlowDefinitionSummaryTypeDef(TypedDict):
    FlowDefinitionName: str
    FlowDefinitionArn: str
    FlowDefinitionStatus: FlowDefinitionStatus
    CreationTime: datetime


class FlowDefinitionSummaryTypeDef(_RequiredFlowDefinitionSummaryTypeDef, total=False):
    FailureReason: str


class _RequiredGetDeviceFleetReportResponseTypeDef(TypedDict):
    DeviceFleetArn: str
    DeviceFleetName: str


class GetDeviceFleetReportResponseTypeDef(
    _RequiredGetDeviceFleetReportResponseTypeDef, total=False
):
    OutputConfig: "EdgeOutputConfigTypeDef"
    Description: str
    ReportGenerated: datetime
    DeviceStats: "DeviceStatsTypeDef"
    AgentVersions: List["AgentVersionTypeDef"]
    ModelStats: List["EdgeModelStatTypeDef"]


class GetModelPackageGroupPolicyOutputTypeDef(TypedDict):
    ResourcePolicy: str
    ResponseMetadata: "ResponseMetadata"


class GetSagemakerServicecatalogPortfolioStatusOutputTypeDef(TypedDict):
    Status: SagemakerServicecatalogStatus
    ResponseMetadata: "ResponseMetadata"


class GetSearchSuggestionsResponseTypeDef(TypedDict, total=False):
    PropertyNameSuggestions: List["PropertyNameSuggestionTypeDef"]


class GitConfigForUpdateTypeDef(TypedDict, total=False):
    SecretArn: str


class _RequiredGitConfigTypeDef(TypedDict):
    RepositoryUrl: str


class GitConfigTypeDef(_RequiredGitConfigTypeDef, total=False):
    Branch: str
    SecretArn: str


class HumanLoopActivationConditionsConfigTypeDef(TypedDict):
    HumanLoopActivationConditions: str


class HumanLoopActivationConfigTypeDef(TypedDict):
    HumanLoopActivationConditionsConfig: "HumanLoopActivationConditionsConfigTypeDef"


class _RequiredHumanLoopConfigTypeDef(TypedDict):
    WorkteamArn: str
    HumanTaskUiArn: str
    TaskTitle: str
    TaskDescription: str
    TaskCount: int


class HumanLoopConfigTypeDef(_RequiredHumanLoopConfigTypeDef, total=False):
    TaskAvailabilityLifetimeInSeconds: int
    TaskTimeLimitInSeconds: int
    TaskKeywords: List[str]
    PublicWorkforceTaskPrice: "PublicWorkforceTaskPriceTypeDef"


class HumanLoopRequestSourceTypeDef(TypedDict):
    AwsManagedHumanLoopRequestSource: AwsManagedHumanLoopRequestSource


class _RequiredHumanTaskConfigTypeDef(TypedDict):
    WorkteamArn: str
    UiConfig: "UiConfigTypeDef"
    PreHumanTaskLambdaArn: str
    TaskTitle: str
    TaskDescription: str
    NumberOfHumanWorkersPerDataObject: int
    TaskTimeLimitInSeconds: int
    AnnotationConsolidationConfig: "AnnotationConsolidationConfigTypeDef"


class HumanTaskConfigTypeDef(_RequiredHumanTaskConfigTypeDef, total=False):
    TaskKeywords: List[str]
    TaskAvailabilityLifetimeInSeconds: int
    MaxConcurrentTaskCount: int
    PublicWorkforceTaskPrice: "PublicWorkforceTaskPriceTypeDef"


class HumanTaskUiSummaryTypeDef(TypedDict):
    HumanTaskUiName: str
    HumanTaskUiArn: str
    CreationTime: datetime


class _RequiredHyperParameterAlgorithmSpecificationTypeDef(TypedDict):
    TrainingInputMode: TrainingInputMode


class HyperParameterAlgorithmSpecificationTypeDef(
    _RequiredHyperParameterAlgorithmSpecificationTypeDef, total=False
):
    TrainingImage: str
    AlgorithmName: str
    MetricDefinitions: List["MetricDefinitionTypeDef"]


_RequiredHyperParameterSpecificationTypeDef = TypedDict(
    "_RequiredHyperParameterSpecificationTypeDef", {"Name": str, "Type": ParameterType}
)
_OptionalHyperParameterSpecificationTypeDef = TypedDict(
    "_OptionalHyperParameterSpecificationTypeDef",
    {
        "Description": str,
        "Range": "ParameterRangeTypeDef",
        "IsTunable": bool,
        "IsRequired": bool,
        "DefaultValue": str,
    },
    total=False,
)


class HyperParameterSpecificationTypeDef(
    _RequiredHyperParameterSpecificationTypeDef, _OptionalHyperParameterSpecificationTypeDef
):
    pass


class _RequiredHyperParameterTrainingJobDefinitionTypeDef(TypedDict):
    AlgorithmSpecification: "HyperParameterAlgorithmSpecificationTypeDef"
    RoleArn: str
    OutputDataConfig: "OutputDataConfigTypeDef"
    ResourceConfig: "ResourceConfigTypeDef"
    StoppingCondition: "StoppingConditionTypeDef"


class HyperParameterTrainingJobDefinitionTypeDef(
    _RequiredHyperParameterTrainingJobDefinitionTypeDef, total=False
):
    DefinitionName: str
    TuningObjective: "HyperParameterTuningJobObjectiveTypeDef"
    HyperParameterRanges: "ParameterRangesTypeDef"
    StaticHyperParameters: Dict[str, str]
    InputDataConfig: List["ChannelTypeDef"]
    VpcConfig: "VpcConfigTypeDef"
    EnableNetworkIsolation: bool
    EnableInterContainerTrafficEncryption: bool
    EnableManagedSpotTraining: bool
    CheckpointConfig: "CheckpointConfigTypeDef"
    RetryStrategy: "RetryStrategyTypeDef"


class _RequiredHyperParameterTrainingJobSummaryTypeDef(TypedDict):
    TrainingJobName: str
    TrainingJobArn: str
    CreationTime: datetime
    TrainingJobStatus: TrainingJobStatus
    TunedHyperParameters: Dict[str, str]


class HyperParameterTrainingJobSummaryTypeDef(
    _RequiredHyperParameterTrainingJobSummaryTypeDef, total=False
):
    TrainingJobDefinitionName: str
    TuningJobName: str
    TrainingStartTime: datetime
    TrainingEndTime: datetime
    FailureReason: str
    FinalHyperParameterTuningJobObjectiveMetric: "FinalHyperParameterTuningJobObjectiveMetricTypeDef"
    ObjectiveStatus: ObjectiveStatus


class _RequiredHyperParameterTuningJobConfigTypeDef(TypedDict):
    Strategy: HyperParameterTuningJobStrategyType
    ResourceLimits: "ResourceLimitsTypeDef"


class HyperParameterTuningJobConfigTypeDef(
    _RequiredHyperParameterTuningJobConfigTypeDef, total=False
):
    HyperParameterTuningJobObjective: "HyperParameterTuningJobObjectiveTypeDef"
    ParameterRanges: "ParameterRangesTypeDef"
    TrainingJobEarlyStoppingType: TrainingJobEarlyStoppingType
    TuningJobCompletionCriteria: "TuningJobCompletionCriteriaTypeDef"


HyperParameterTuningJobObjectiveTypeDef = TypedDict(
    "HyperParameterTuningJobObjectiveTypeDef",
    {"Type": HyperParameterTuningJobObjectiveType, "MetricName": str},
)


class _RequiredHyperParameterTuningJobSummaryTypeDef(TypedDict):
    HyperParameterTuningJobName: str
    HyperParameterTuningJobArn: str
    HyperParameterTuningJobStatus: HyperParameterTuningJobStatus
    Strategy: HyperParameterTuningJobStrategyType
    CreationTime: datetime
    TrainingJobStatusCounters: "TrainingJobStatusCountersTypeDef"
    ObjectiveStatusCounters: "ObjectiveStatusCountersTypeDef"


class HyperParameterTuningJobSummaryTypeDef(
    _RequiredHyperParameterTuningJobSummaryTypeDef, total=False
):
    HyperParameterTuningEndTime: datetime
    LastModifiedTime: datetime
    ResourceLimits: "ResourceLimitsTypeDef"


class HyperParameterTuningJobWarmStartConfigTypeDef(TypedDict):
    ParentHyperParameterTuningJobs: List["ParentHyperParameterTuningJobTypeDef"]
    WarmStartType: HyperParameterTuningJobWarmStartType


class _RequiredImageConfigTypeDef(TypedDict):
    RepositoryAccessMode: RepositoryAccessMode


class ImageConfigTypeDef(_RequiredImageConfigTypeDef, total=False):
    RepositoryAuthConfig: "RepositoryAuthConfigTypeDef"


class _RequiredImageTypeDef(TypedDict):
    CreationTime: datetime
    ImageArn: str
    ImageName: str
    ImageStatus: ImageStatus
    LastModifiedTime: datetime


class ImageTypeDef(_RequiredImageTypeDef, total=False):
    Description: str
    DisplayName: str
    FailureReason: str


class _RequiredImageVersionTypeDef(TypedDict):
    CreationTime: datetime
    ImageArn: str
    ImageVersionArn: str
    ImageVersionStatus: ImageVersionStatus
    LastModifiedTime: datetime
    Version: int


class ImageVersionTypeDef(_RequiredImageVersionTypeDef, total=False):
    FailureReason: str


class InferenceExecutionConfigTypeDef(TypedDict):
    Mode: InferenceExecutionMode


class _RequiredInferenceSpecificationTypeDef(TypedDict):
    Containers: List["ModelPackageContainerDefinitionTypeDef"]
    SupportedContentTypes: List[str]
    SupportedResponseMIMETypes: List[str]


class InferenceSpecificationTypeDef(_RequiredInferenceSpecificationTypeDef, total=False):
    SupportedTransformInstanceTypes: List[TransformInstanceType]
    SupportedRealtimeInferenceInstanceTypes: List[ProductionVariantInstanceType]


class _RequiredInputConfigTypeDef(TypedDict):
    S3Uri: str
    DataInputConfig: str
    Framework: Framework


class InputConfigTypeDef(_RequiredInputConfigTypeDef, total=False):
    FrameworkVersion: str


class IntegerParameterRangeSpecificationTypeDef(TypedDict):
    MinValue: str
    MaxValue: str


class _RequiredIntegerParameterRangeTypeDef(TypedDict):
    Name: str
    MinValue: str
    MaxValue: str


class IntegerParameterRangeTypeDef(_RequiredIntegerParameterRangeTypeDef, total=False):
    ScalingType: HyperParameterScalingType


class JupyterServerAppSettingsTypeDef(TypedDict, total=False):
    DefaultResourceSpec: "ResourceSpecTypeDef"


class KernelGatewayAppSettingsTypeDef(TypedDict, total=False):
    DefaultResourceSpec: "ResourceSpecTypeDef"
    CustomImages: List["CustomImageTypeDef"]


class _RequiredKernelGatewayImageConfigTypeDef(TypedDict):
    KernelSpecs: List["KernelSpecTypeDef"]


class KernelGatewayImageConfigTypeDef(_RequiredKernelGatewayImageConfigTypeDef, total=False):
    FileSystemConfig: "FileSystemConfigTypeDef"


class _RequiredKernelSpecTypeDef(TypedDict):
    Name: str


class KernelSpecTypeDef(_RequiredKernelSpecTypeDef, total=False):
    DisplayName: str


class LabelCountersForWorkteamTypeDef(TypedDict, total=False):
    HumanLabeled: int
    PendingHuman: int
    Total: int


class LabelCountersTypeDef(TypedDict, total=False):
    TotalLabeled: int
    HumanLabeled: int
    MachineLabeled: int
    FailedNonRetryableError: int
    Unlabeled: int


class _RequiredLabelingJobAlgorithmsConfigTypeDef(TypedDict):
    LabelingJobAlgorithmSpecificationArn: str


class LabelingJobAlgorithmsConfigTypeDef(_RequiredLabelingJobAlgorithmsConfigTypeDef, total=False):
    InitialActiveLearningModelArn: str
    LabelingJobResourceConfig: "LabelingJobResourceConfigTypeDef"


class LabelingJobDataAttributesTypeDef(TypedDict, total=False):
    ContentClassifiers: List[ContentClassifier]


class LabelingJobDataSourceTypeDef(TypedDict, total=False):
    S3DataSource: "LabelingJobS3DataSourceTypeDef"
    SnsDataSource: "LabelingJobSnsDataSourceTypeDef"


class _RequiredLabelingJobForWorkteamSummaryTypeDef(TypedDict):
    JobReferenceCode: str
    WorkRequesterAccountId: str
    CreationTime: datetime


class LabelingJobForWorkteamSummaryTypeDef(
    _RequiredLabelingJobForWorkteamSummaryTypeDef, total=False
):
    LabelingJobName: str
    LabelCounters: "LabelCountersForWorkteamTypeDef"
    NumberOfHumanWorkersPerDataObject: int


class _RequiredLabelingJobInputConfigTypeDef(TypedDict):
    DataSource: "LabelingJobDataSourceTypeDef"


class LabelingJobInputConfigTypeDef(_RequiredLabelingJobInputConfigTypeDef, total=False):
    DataAttributes: "LabelingJobDataAttributesTypeDef"


class _RequiredLabelingJobOutputConfigTypeDef(TypedDict):
    S3OutputPath: str


class LabelingJobOutputConfigTypeDef(_RequiredLabelingJobOutputConfigTypeDef, total=False):
    KmsKeyId: str
    SnsTopicArn: str


class LabelingJobOutputTypeDef(TypedDict):
    OutputDatasetS3Uri: str
    FinalActiveLearningModelArn: str
    ResponseMetadata: "ResponseMetadata"


class LabelingJobResourceConfigTypeDef(TypedDict, total=False):
    VolumeKmsKeyId: str


class LabelingJobS3DataSourceTypeDef(TypedDict):
    ManifestS3Uri: str


class LabelingJobSnsDataSourceTypeDef(TypedDict):
    SnsTopicArn: str


class LabelingJobStoppingConditionsTypeDef(TypedDict, total=False):
    MaxHumanLabeledObjectCount: int
    MaxPercentageOfInputDatasetLabeled: int


class _RequiredLabelingJobSummaryTypeDef(TypedDict):
    LabelingJobName: str
    LabelingJobArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    LabelingJobStatus: LabelingJobStatus
    LabelCounters: "LabelCountersTypeDef"
    WorkteamArn: str
    PreHumanTaskLambdaArn: str


class LabelingJobSummaryTypeDef(_RequiredLabelingJobSummaryTypeDef, total=False):
    AnnotationConsolidationLambdaArn: str
    FailureReason: str
    LabelingJobOutput: "LabelingJobOutputTypeDef"
    InputConfig: "LabelingJobInputConfigTypeDef"


class ListActionsResponseTypeDef(TypedDict, total=False):
    ActionSummaries: List["ActionSummaryTypeDef"]
    NextToken: str


class ListAlgorithmsOutputTypeDef(TypedDict):
    AlgorithmSummaryList: List["AlgorithmSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListAppImageConfigsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    AppImageConfigs: List["AppImageConfigDetailsTypeDef"]


class ListAppsResponseTypeDef(TypedDict, total=False):
    Apps: List["AppDetailsTypeDef"]
    NextToken: str


class ListArtifactsResponseTypeDef(TypedDict, total=False):
    ArtifactSummaries: List["ArtifactSummaryTypeDef"]
    NextToken: str


class ListAssociationsResponseTypeDef(TypedDict, total=False):
    AssociationSummaries: List["AssociationSummaryTypeDef"]
    NextToken: str


class _RequiredListAutoMLJobsResponseTypeDef(TypedDict):
    AutoMLJobSummaries: List["AutoMLJobSummaryTypeDef"]


class ListAutoMLJobsResponseTypeDef(_RequiredListAutoMLJobsResponseTypeDef, total=False):
    NextToken: str


class _RequiredListCandidatesForAutoMLJobResponseTypeDef(TypedDict):
    Candidates: List["AutoMLCandidateTypeDef"]


class ListCandidatesForAutoMLJobResponseTypeDef(
    _RequiredListCandidatesForAutoMLJobResponseTypeDef, total=False
):
    NextToken: str


class ListCodeRepositoriesOutputTypeDef(TypedDict):
    CodeRepositorySummaryList: List["CodeRepositorySummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredListCompilationJobsResponseTypeDef(TypedDict):
    CompilationJobSummaries: List["CompilationJobSummaryTypeDef"]


class ListCompilationJobsResponseTypeDef(_RequiredListCompilationJobsResponseTypeDef, total=False):
    NextToken: str


class ListContextsResponseTypeDef(TypedDict, total=False):
    ContextSummaries: List["ContextSummaryTypeDef"]
    NextToken: str


class _RequiredListDataQualityJobDefinitionsResponseTypeDef(TypedDict):
    JobDefinitionSummaries: List["MonitoringJobDefinitionSummaryTypeDef"]


class ListDataQualityJobDefinitionsResponseTypeDef(
    _RequiredListDataQualityJobDefinitionsResponseTypeDef, total=False
):
    NextToken: str


class _RequiredListDeviceFleetsResponseTypeDef(TypedDict):
    DeviceFleetSummaries: List["DeviceFleetSummaryTypeDef"]


class ListDeviceFleetsResponseTypeDef(_RequiredListDeviceFleetsResponseTypeDef, total=False):
    NextToken: str


class _RequiredListDevicesResponseTypeDef(TypedDict):
    DeviceSummaries: List["DeviceSummaryTypeDef"]


class ListDevicesResponseTypeDef(_RequiredListDevicesResponseTypeDef, total=False):
    NextToken: str


class ListDomainsResponseTypeDef(TypedDict, total=False):
    Domains: List["DomainDetailsTypeDef"]
    NextToken: str


class _RequiredListEdgePackagingJobsResponseTypeDef(TypedDict):
    EdgePackagingJobSummaries: List["EdgePackagingJobSummaryTypeDef"]


class ListEdgePackagingJobsResponseTypeDef(
    _RequiredListEdgePackagingJobsResponseTypeDef, total=False
):
    NextToken: str


class ListEndpointConfigsOutputTypeDef(TypedDict):
    EndpointConfigs: List["EndpointConfigSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListEndpointsOutputTypeDef(TypedDict):
    Endpoints: List["EndpointSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListExperimentsResponseTypeDef(TypedDict, total=False):
    ExperimentSummaries: List["ExperimentSummaryTypeDef"]
    NextToken: str


class ListFeatureGroupsResponseTypeDef(TypedDict):
    FeatureGroupSummaries: List["FeatureGroupSummaryTypeDef"]
    NextToken: str


class _RequiredListFlowDefinitionsResponseTypeDef(TypedDict):
    FlowDefinitionSummaries: List["FlowDefinitionSummaryTypeDef"]


class ListFlowDefinitionsResponseTypeDef(_RequiredListFlowDefinitionsResponseTypeDef, total=False):
    NextToken: str


class _RequiredListHumanTaskUisResponseTypeDef(TypedDict):
    HumanTaskUiSummaries: List["HumanTaskUiSummaryTypeDef"]


class ListHumanTaskUisResponseTypeDef(_RequiredListHumanTaskUisResponseTypeDef, total=False):
    NextToken: str


class _RequiredListHyperParameterTuningJobsResponseTypeDef(TypedDict):
    HyperParameterTuningJobSummaries: List["HyperParameterTuningJobSummaryTypeDef"]


class ListHyperParameterTuningJobsResponseTypeDef(
    _RequiredListHyperParameterTuningJobsResponseTypeDef, total=False
):
    NextToken: str


class ListImageVersionsResponseTypeDef(TypedDict, total=False):
    ImageVersions: List["ImageVersionTypeDef"]
    NextToken: str


class ListImagesResponseTypeDef(TypedDict, total=False):
    Images: List["ImageTypeDef"]
    NextToken: str


class _RequiredListLabelingJobsForWorkteamResponseTypeDef(TypedDict):
    LabelingJobSummaryList: List["LabelingJobForWorkteamSummaryTypeDef"]


class ListLabelingJobsForWorkteamResponseTypeDef(
    _RequiredListLabelingJobsForWorkteamResponseTypeDef, total=False
):
    NextToken: str


class ListLabelingJobsResponseTypeDef(TypedDict, total=False):
    LabelingJobSummaryList: List["LabelingJobSummaryTypeDef"]
    NextToken: str


class _RequiredListModelBiasJobDefinitionsResponseTypeDef(TypedDict):
    JobDefinitionSummaries: List["MonitoringJobDefinitionSummaryTypeDef"]


class ListModelBiasJobDefinitionsResponseTypeDef(
    _RequiredListModelBiasJobDefinitionsResponseTypeDef, total=False
):
    NextToken: str


class _RequiredListModelExplainabilityJobDefinitionsResponseTypeDef(TypedDict):
    JobDefinitionSummaries: List["MonitoringJobDefinitionSummaryTypeDef"]


class ListModelExplainabilityJobDefinitionsResponseTypeDef(
    _RequiredListModelExplainabilityJobDefinitionsResponseTypeDef, total=False
):
    NextToken: str


class ListModelPackageGroupsOutputTypeDef(TypedDict):
    ModelPackageGroupSummaryList: List["ModelPackageGroupSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListModelPackagesOutputTypeDef(TypedDict):
    ModelPackageSummaryList: List["ModelPackageSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredListModelQualityJobDefinitionsResponseTypeDef(TypedDict):
    JobDefinitionSummaries: List["MonitoringJobDefinitionSummaryTypeDef"]


class ListModelQualityJobDefinitionsResponseTypeDef(
    _RequiredListModelQualityJobDefinitionsResponseTypeDef, total=False
):
    NextToken: str


class ListModelsOutputTypeDef(TypedDict):
    Models: List["ModelSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredListMonitoringExecutionsResponseTypeDef(TypedDict):
    MonitoringExecutionSummaries: List["MonitoringExecutionSummaryTypeDef"]


class ListMonitoringExecutionsResponseTypeDef(
    _RequiredListMonitoringExecutionsResponseTypeDef, total=False
):
    NextToken: str


class _RequiredListMonitoringSchedulesResponseTypeDef(TypedDict):
    MonitoringScheduleSummaries: List["MonitoringScheduleSummaryTypeDef"]


class ListMonitoringSchedulesResponseTypeDef(
    _RequiredListMonitoringSchedulesResponseTypeDef, total=False
):
    NextToken: str


class ListNotebookInstanceLifecycleConfigsOutputTypeDef(TypedDict):
    NextToken: str
    NotebookInstanceLifecycleConfigs: List["NotebookInstanceLifecycleConfigSummaryTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListNotebookInstancesOutputTypeDef(TypedDict):
    NextToken: str
    NotebookInstances: List["NotebookInstanceSummaryTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListPipelineExecutionStepsResponseTypeDef(TypedDict, total=False):
    PipelineExecutionSteps: List["PipelineExecutionStepTypeDef"]
    NextToken: str


class ListPipelineExecutionsResponseTypeDef(TypedDict, total=False):
    PipelineExecutionSummaries: List["PipelineExecutionSummaryTypeDef"]
    NextToken: str


class ListPipelineParametersForExecutionResponseTypeDef(TypedDict, total=False):
    PipelineParameters: List["ParameterTypeDef"]
    NextToken: str


class ListPipelinesResponseTypeDef(TypedDict, total=False):
    PipelineSummaries: List["PipelineSummaryTypeDef"]
    NextToken: str


class _RequiredListProcessingJobsResponseTypeDef(TypedDict):
    ProcessingJobSummaries: List["ProcessingJobSummaryTypeDef"]


class ListProcessingJobsResponseTypeDef(_RequiredListProcessingJobsResponseTypeDef, total=False):
    NextToken: str


class ListProjectsOutputTypeDef(TypedDict):
    ProjectSummaryList: List["ProjectSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredListSubscribedWorkteamsResponseTypeDef(TypedDict):
    SubscribedWorkteams: List["SubscribedWorkteamTypeDef"]


class ListSubscribedWorkteamsResponseTypeDef(
    _RequiredListSubscribedWorkteamsResponseTypeDef, total=False
):
    NextToken: str


class ListTagsOutputTypeDef(TypedDict):
    Tags: List["TagTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredListTrainingJobsForHyperParameterTuningJobResponseTypeDef(TypedDict):
    TrainingJobSummaries: List["HyperParameterTrainingJobSummaryTypeDef"]


class ListTrainingJobsForHyperParameterTuningJobResponseTypeDef(
    _RequiredListTrainingJobsForHyperParameterTuningJobResponseTypeDef, total=False
):
    NextToken: str


class _RequiredListTrainingJobsResponseTypeDef(TypedDict):
    TrainingJobSummaries: List["TrainingJobSummaryTypeDef"]


class ListTrainingJobsResponseTypeDef(_RequiredListTrainingJobsResponseTypeDef, total=False):
    NextToken: str


class _RequiredListTransformJobsResponseTypeDef(TypedDict):
    TransformJobSummaries: List["TransformJobSummaryTypeDef"]


class ListTransformJobsResponseTypeDef(_RequiredListTransformJobsResponseTypeDef, total=False):
    NextToken: str


class ListTrialComponentsResponseTypeDef(TypedDict, total=False):
    TrialComponentSummaries: List["TrialComponentSummaryTypeDef"]
    NextToken: str


class ListTrialsResponseTypeDef(TypedDict, total=False):
    TrialSummaries: List["TrialSummaryTypeDef"]
    NextToken: str


class ListUserProfilesResponseTypeDef(TypedDict, total=False):
    UserProfiles: List["UserProfileDetailsTypeDef"]
    NextToken: str


class _RequiredListWorkforcesResponseTypeDef(TypedDict):
    Workforces: List["WorkforceTypeDef"]


class ListWorkforcesResponseTypeDef(_RequiredListWorkforcesResponseTypeDef, total=False):
    NextToken: str


class _RequiredListWorkteamsResponseTypeDef(TypedDict):
    Workteams: List["WorkteamTypeDef"]


class ListWorkteamsResponseTypeDef(_RequiredListWorkteamsResponseTypeDef, total=False):
    NextToken: str


class MemberDefinitionTypeDef(TypedDict, total=False):
    CognitoMemberDefinition: "CognitoMemberDefinitionTypeDef"
    OidcMemberDefinition: "OidcMemberDefinitionTypeDef"


class MetadataPropertiesTypeDef(TypedDict, total=False):
    CommitId: str
    Repository: str
    GeneratedBy: str
    ProjectId: str


class MetricDataTypeDef(TypedDict, total=False):
    MetricName: str
    Value: float
    Timestamp: datetime


class MetricDefinitionTypeDef(TypedDict):
    Name: str
    Regex: str


class _RequiredMetricsSourceTypeDef(TypedDict):
    ContentType: str
    S3Uri: str


class MetricsSourceTypeDef(_RequiredMetricsSourceTypeDef, total=False):
    ContentDigest: str


class ModelArtifactsTypeDef(TypedDict):
    S3ModelArtifacts: str


class _RequiredModelBiasAppSpecificationTypeDef(TypedDict):
    ImageUri: str
    ConfigUri: str


class ModelBiasAppSpecificationTypeDef(_RequiredModelBiasAppSpecificationTypeDef, total=False):
    Environment: Dict[str, str]


class ModelBiasBaselineConfigTypeDef(TypedDict, total=False):
    BaseliningJobName: str
    ConstraintsResource: "MonitoringConstraintsResourceTypeDef"


class ModelBiasJobInputTypeDef(TypedDict):
    EndpointInput: "EndpointInputTypeDef"
    GroundTruthS3Input: "MonitoringGroundTruthS3InputTypeDef"


class ModelClientConfigTypeDef(TypedDict, total=False):
    InvocationsTimeoutInSeconds: int
    InvocationsMaxRetries: int


class ModelDataQualityTypeDef(TypedDict, total=False):
    Statistics: "MetricsSourceTypeDef"
    Constraints: "MetricsSourceTypeDef"


class ModelDeployConfigTypeDef(TypedDict, total=False):
    AutoGenerateEndpointName: bool
    EndpointName: str


class ModelDeployResultTypeDef(TypedDict, total=False):
    EndpointName: str


class ModelDigestsTypeDef(TypedDict, total=False):
    ArtifactDigest: str


class _RequiredModelExplainabilityAppSpecificationTypeDef(TypedDict):
    ImageUri: str
    ConfigUri: str


class ModelExplainabilityAppSpecificationTypeDef(
    _RequiredModelExplainabilityAppSpecificationTypeDef, total=False
):
    Environment: Dict[str, str]


class ModelExplainabilityBaselineConfigTypeDef(TypedDict, total=False):
    BaseliningJobName: str
    ConstraintsResource: "MonitoringConstraintsResourceTypeDef"


class ModelExplainabilityJobInputTypeDef(TypedDict):
    EndpointInput: "EndpointInputTypeDef"


class ModelMetricsTypeDef(TypedDict, total=False):
    ModelQuality: "ModelQualityTypeDef"
    ModelDataQuality: "ModelDataQualityTypeDef"
    Bias: "BiasTypeDef"
    Explainability: "ExplainabilityTypeDef"


class _RequiredModelPackageContainerDefinitionTypeDef(TypedDict):
    Image: str


class ModelPackageContainerDefinitionTypeDef(
    _RequiredModelPackageContainerDefinitionTypeDef, total=False
):
    ContainerHostname: str
    ImageDigest: str
    ModelDataUrl: str
    ProductId: str


class _RequiredModelPackageGroupSummaryTypeDef(TypedDict):
    ModelPackageGroupName: str
    ModelPackageGroupArn: str
    CreationTime: datetime
    ModelPackageGroupStatus: ModelPackageGroupStatus


class ModelPackageGroupSummaryTypeDef(_RequiredModelPackageGroupSummaryTypeDef, total=False):
    ModelPackageGroupDescription: str


class ModelPackageGroupTypeDef(TypedDict, total=False):
    ModelPackageGroupName: str
    ModelPackageGroupArn: str
    ModelPackageGroupDescription: str
    CreationTime: datetime
    CreatedBy: "UserContextTypeDef"
    ModelPackageGroupStatus: ModelPackageGroupStatus
    Tags: List["TagTypeDef"]


class _RequiredModelPackageStatusDetailsTypeDef(TypedDict):
    ValidationStatuses: List["ModelPackageStatusItemTypeDef"]


class ModelPackageStatusDetailsTypeDef(_RequiredModelPackageStatusDetailsTypeDef, total=False):
    ImageScanStatuses: List["ModelPackageStatusItemTypeDef"]


class _RequiredModelPackageStatusItemTypeDef(TypedDict):
    Name: str
    Status: DetailedModelPackageStatus


class ModelPackageStatusItemTypeDef(_RequiredModelPackageStatusItemTypeDef, total=False):
    FailureReason: str


class _RequiredModelPackageSummaryTypeDef(TypedDict):
    ModelPackageName: str
    ModelPackageArn: str
    CreationTime: datetime
    ModelPackageStatus: ModelPackageStatus


class ModelPackageSummaryTypeDef(_RequiredModelPackageSummaryTypeDef, total=False):
    ModelPackageGroupName: str
    ModelPackageVersion: int
    ModelPackageDescription: str
    ModelApprovalStatus: ModelApprovalStatus


class ModelPackageTypeDef(TypedDict, total=False):
    ModelPackageName: str
    ModelPackageGroupName: str
    ModelPackageVersion: int
    ModelPackageArn: str
    ModelPackageDescription: str
    CreationTime: datetime
    InferenceSpecification: "InferenceSpecificationTypeDef"
    SourceAlgorithmSpecification: "SourceAlgorithmSpecificationTypeDef"
    ValidationSpecification: "ModelPackageValidationSpecificationTypeDef"
    ModelPackageStatus: ModelPackageStatus
    ModelPackageStatusDetails: "ModelPackageStatusDetailsTypeDef"
    CertifyForMarketplace: bool
    ModelApprovalStatus: ModelApprovalStatus
    CreatedBy: "UserContextTypeDef"
    MetadataProperties: "MetadataPropertiesTypeDef"
    ModelMetrics: "ModelMetricsTypeDef"
    LastModifiedTime: datetime
    LastModifiedBy: "UserContextTypeDef"
    ApprovalDescription: str
    Tags: List["TagTypeDef"]


class ModelPackageValidationProfileTypeDef(TypedDict):
    ProfileName: str
    TransformJobDefinition: "TransformJobDefinitionTypeDef"


class ModelPackageValidationSpecificationTypeDef(TypedDict):
    ValidationRole: str
    ValidationProfiles: List["ModelPackageValidationProfileTypeDef"]


class _RequiredModelQualityAppSpecificationTypeDef(TypedDict):
    ImageUri: str


class ModelQualityAppSpecificationTypeDef(
    _RequiredModelQualityAppSpecificationTypeDef, total=False
):
    ContainerEntrypoint: List[str]
    ContainerArguments: List[str]
    RecordPreprocessorSourceUri: str
    PostAnalyticsProcessorSourceUri: str
    ProblemType: MonitoringProblemType
    Environment: Dict[str, str]


class ModelQualityBaselineConfigTypeDef(TypedDict, total=False):
    BaseliningJobName: str
    ConstraintsResource: "MonitoringConstraintsResourceTypeDef"


class ModelQualityJobInputTypeDef(TypedDict):
    EndpointInput: "EndpointInputTypeDef"
    GroundTruthS3Input: "MonitoringGroundTruthS3InputTypeDef"


class ModelQualityTypeDef(TypedDict, total=False):
    Statistics: "MetricsSourceTypeDef"
    Constraints: "MetricsSourceTypeDef"


class ModelStepMetadataTypeDef(TypedDict, total=False):
    Arn: str


class ModelSummaryTypeDef(TypedDict):
    ModelName: str
    ModelArn: str
    CreationTime: datetime


class _RequiredMonitoringAppSpecificationTypeDef(TypedDict):
    ImageUri: str


class MonitoringAppSpecificationTypeDef(_RequiredMonitoringAppSpecificationTypeDef, total=False):
    ContainerEntrypoint: List[str]
    ContainerArguments: List[str]
    RecordPreprocessorSourceUri: str
    PostAnalyticsProcessorSourceUri: str


class MonitoringBaselineConfigTypeDef(TypedDict, total=False):
    BaseliningJobName: str
    ConstraintsResource: "MonitoringConstraintsResourceTypeDef"
    StatisticsResource: "MonitoringStatisticsResourceTypeDef"


class _RequiredMonitoringClusterConfigTypeDef(TypedDict):
    InstanceCount: int
    InstanceType: ProcessingInstanceType
    VolumeSizeInGB: int


class MonitoringClusterConfigTypeDef(_RequiredMonitoringClusterConfigTypeDef, total=False):
    VolumeKmsKeyId: str


class MonitoringConstraintsResourceTypeDef(TypedDict, total=False):
    S3Uri: str


class _RequiredMonitoringExecutionSummaryTypeDef(TypedDict):
    MonitoringScheduleName: str
    ScheduledTime: datetime
    CreationTime: datetime
    LastModifiedTime: datetime
    MonitoringExecutionStatus: ExecutionStatus


class MonitoringExecutionSummaryTypeDef(_RequiredMonitoringExecutionSummaryTypeDef, total=False):
    ProcessingJobArn: str
    EndpointName: str
    FailureReason: str
    MonitoringJobDefinitionName: str
    MonitoringType: MonitoringType


class MonitoringGroundTruthS3InputTypeDef(TypedDict, total=False):
    S3Uri: str


class MonitoringInputTypeDef(TypedDict):
    EndpointInput: "EndpointInputTypeDef"


class MonitoringJobDefinitionSummaryTypeDef(TypedDict):
    MonitoringJobDefinitionName: str
    MonitoringJobDefinitionArn: str
    CreationTime: datetime
    EndpointName: str


class _RequiredMonitoringJobDefinitionTypeDef(TypedDict):
    MonitoringInputs: List["MonitoringInputTypeDef"]
    MonitoringOutputConfig: "MonitoringOutputConfigTypeDef"
    MonitoringResources: "MonitoringResourcesTypeDef"
    MonitoringAppSpecification: "MonitoringAppSpecificationTypeDef"
    RoleArn: str


class MonitoringJobDefinitionTypeDef(_RequiredMonitoringJobDefinitionTypeDef, total=False):
    BaselineConfig: "MonitoringBaselineConfigTypeDef"
    StoppingCondition: "MonitoringStoppingConditionTypeDef"
    Environment: Dict[str, str]
    NetworkConfig: "NetworkConfigTypeDef"


class MonitoringNetworkConfigTypeDef(TypedDict, total=False):
    EnableInterContainerTrafficEncryption: bool
    EnableNetworkIsolation: bool
    VpcConfig: "VpcConfigTypeDef"


class _RequiredMonitoringOutputConfigTypeDef(TypedDict):
    MonitoringOutputs: List["MonitoringOutputTypeDef"]


class MonitoringOutputConfigTypeDef(_RequiredMonitoringOutputConfigTypeDef, total=False):
    KmsKeyId: str


class MonitoringOutputTypeDef(TypedDict):
    S3Output: "MonitoringS3OutputTypeDef"
    ResponseMetadata: "ResponseMetadata"


class MonitoringResourcesTypeDef(TypedDict):
    ClusterConfig: "MonitoringClusterConfigTypeDef"


class MonitoringS3OutputTypeDef(TypedDict):
    S3Uri: str
    LocalPath: str
    S3UploadMode: ProcessingS3UploadMode
    ResponseMetadata: "ResponseMetadata"


class MonitoringScheduleConfigTypeDef(TypedDict, total=False):
    ScheduleConfig: "ScheduleConfigTypeDef"
    MonitoringJobDefinition: "MonitoringJobDefinitionTypeDef"
    MonitoringJobDefinitionName: str
    MonitoringType: MonitoringType


class _RequiredMonitoringScheduleSummaryTypeDef(TypedDict):
    MonitoringScheduleName: str
    MonitoringScheduleArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    MonitoringScheduleStatus: ScheduleStatus


class MonitoringScheduleSummaryTypeDef(_RequiredMonitoringScheduleSummaryTypeDef, total=False):
    EndpointName: str
    MonitoringJobDefinitionName: str
    MonitoringType: MonitoringType


class MonitoringScheduleTypeDef(TypedDict, total=False):
    MonitoringScheduleArn: str
    MonitoringScheduleName: str
    MonitoringScheduleStatus: ScheduleStatus
    MonitoringType: MonitoringType
    FailureReason: str
    CreationTime: datetime
    LastModifiedTime: datetime
    MonitoringScheduleConfig: "MonitoringScheduleConfigTypeDef"
    EndpointName: str
    LastMonitoringExecutionSummary: "MonitoringExecutionSummaryTypeDef"
    Tags: List["TagTypeDef"]


class MonitoringStatisticsResourceTypeDef(TypedDict, total=False):
    S3Uri: str


class MonitoringStoppingConditionTypeDef(TypedDict):
    MaxRuntimeInSeconds: int


class MultiModelConfigTypeDef(TypedDict, total=False):
    ModelCacheSetting: ModelCacheSetting


class NestedFiltersTypeDef(TypedDict):
    NestedPropertyName: str
    Filters: List["FilterTypeDef"]


class NetworkConfigTypeDef(TypedDict, total=False):
    EnableInterContainerTrafficEncryption: bool
    EnableNetworkIsolation: bool
    VpcConfig: "VpcConfigTypeDef"


class _RequiredNotebookInstanceLifecycleConfigSummaryTypeDef(TypedDict):
    NotebookInstanceLifecycleConfigName: str
    NotebookInstanceLifecycleConfigArn: str


class NotebookInstanceLifecycleConfigSummaryTypeDef(
    _RequiredNotebookInstanceLifecycleConfigSummaryTypeDef, total=False
):
    CreationTime: datetime
    LastModifiedTime: datetime


class NotebookInstanceLifecycleHookTypeDef(TypedDict, total=False):
    Content: str


class _RequiredNotebookInstanceSummaryTypeDef(TypedDict):
    NotebookInstanceName: str
    NotebookInstanceArn: str


class NotebookInstanceSummaryTypeDef(_RequiredNotebookInstanceSummaryTypeDef, total=False):
    NotebookInstanceStatus: NotebookInstanceStatus
    Url: str
    InstanceType: InstanceType
    CreationTime: datetime
    LastModifiedTime: datetime
    NotebookInstanceLifecycleConfigName: str
    DefaultCodeRepository: str
    AdditionalCodeRepositories: List[str]


class NotificationConfigurationTypeDef(TypedDict, total=False):
    NotificationTopicArn: str


class ObjectiveStatusCountersTypeDef(TypedDict, total=False):
    Succeeded: int
    Pending: int
    Failed: int


class _RequiredOfflineStoreConfigTypeDef(TypedDict):
    S3StorageConfig: "S3StorageConfigTypeDef"


class OfflineStoreConfigTypeDef(_RequiredOfflineStoreConfigTypeDef, total=False):
    DisableGlueTableCreation: bool
    DataCatalogConfig: "DataCatalogConfigTypeDef"


class _RequiredOfflineStoreStatusTypeDef(TypedDict):
    Status: OfflineStoreStatusValue


class OfflineStoreStatusTypeDef(_RequiredOfflineStoreStatusTypeDef, total=False):
    BlockedReason: str


class OidcConfigForResponseTypeDef(TypedDict, total=False):
    ClientId: str
    Issuer: str
    AuthorizationEndpoint: str
    TokenEndpoint: str
    UserInfoEndpoint: str
    LogoutEndpoint: str
    JwksUri: str


class OidcConfigTypeDef(TypedDict):
    ClientId: str
    ClientSecret: str
    Issuer: str
    AuthorizationEndpoint: str
    TokenEndpoint: str
    UserInfoEndpoint: str
    LogoutEndpoint: str
    JwksUri: str


class OidcMemberDefinitionTypeDef(TypedDict):
    Groups: List[str]


class OnlineStoreConfigTypeDef(TypedDict, total=False):
    SecurityConfig: "OnlineStoreSecurityConfigTypeDef"
    EnableOnlineStore: bool


class OnlineStoreSecurityConfigTypeDef(TypedDict, total=False):
    KmsKeyId: str


class _RequiredOutputConfigTypeDef(TypedDict):
    S3OutputLocation: str


class OutputConfigTypeDef(_RequiredOutputConfigTypeDef, total=False):
    TargetDevice: TargetDevice
    TargetPlatform: "TargetPlatformTypeDef"
    CompilerOptions: str
    KmsKeyId: str


class _RequiredOutputDataConfigTypeDef(TypedDict):
    S3OutputPath: str


class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, total=False):
    KmsKeyId: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParameterRangeTypeDef(TypedDict, total=False):
    IntegerParameterRangeSpecification: "IntegerParameterRangeSpecificationTypeDef"
    ContinuousParameterRangeSpecification: "ContinuousParameterRangeSpecificationTypeDef"
    CategoricalParameterRangeSpecification: "CategoricalParameterRangeSpecificationTypeDef"


class ParameterRangesTypeDef(TypedDict, total=False):
    IntegerParameterRanges: List["IntegerParameterRangeTypeDef"]
    ContinuousParameterRanges: List["ContinuousParameterRangeTypeDef"]
    CategoricalParameterRanges: List["CategoricalParameterRangeTypeDef"]


class ParameterTypeDef(TypedDict):
    Name: str
    Value: str


class ParentHyperParameterTuningJobTypeDef(TypedDict, total=False):
    HyperParameterTuningJobName: str


class ParentTypeDef(TypedDict, total=False):
    TrialName: str
    ExperimentName: str


class PipelineExecutionStepMetadataTypeDef(TypedDict, total=False):
    TrainingJob: "TrainingJobStepMetadataTypeDef"
    ProcessingJob: "ProcessingJobStepMetadataTypeDef"
    TransformJob: "TransformJobStepMetadataTypeDef"
    Model: "ModelStepMetadataTypeDef"
    RegisterModel: "RegisterModelStepMetadataTypeDef"
    Condition: "ConditionStepMetadataTypeDef"


class PipelineExecutionStepTypeDef(TypedDict, total=False):
    StepName: str
    StartTime: datetime
    EndTime: datetime
    StepStatus: StepStatus
    CacheHitResult: "CacheHitResultTypeDef"
    FailureReason: str
    Metadata: "PipelineExecutionStepMetadataTypeDef"


class PipelineExecutionSummaryTypeDef(TypedDict, total=False):
    PipelineExecutionArn: str
    StartTime: datetime
    PipelineExecutionStatus: PipelineExecutionStatus
    PipelineExecutionDescription: str
    PipelineExecutionDisplayName: str


class PipelineExecutionTypeDef(TypedDict, total=False):
    PipelineArn: str
    PipelineExecutionArn: str
    PipelineExecutionDisplayName: str
    PipelineExecutionStatus: PipelineExecutionStatus
    PipelineExecutionDescription: str
    CreationTime: datetime
    LastModifiedTime: datetime
    CreatedBy: "UserContextTypeDef"
    LastModifiedBy: "UserContextTypeDef"
    PipelineParameters: List["ParameterTypeDef"]


class PipelineSummaryTypeDef(TypedDict, total=False):
    PipelineArn: str
    PipelineName: str
    PipelineDisplayName: str
    PipelineDescription: str
    RoleArn: str
    CreationTime: datetime
    LastModifiedTime: datetime
    LastExecutionTime: datetime


class PipelineTypeDef(TypedDict, total=False):
    PipelineArn: str
    PipelineName: str
    PipelineDisplayName: str
    PipelineDescription: str
    RoleArn: str
    PipelineStatus: Literal["Active"]
    CreationTime: datetime
    LastModifiedTime: datetime
    LastRunTime: datetime
    CreatedBy: "UserContextTypeDef"
    LastModifiedBy: "UserContextTypeDef"
    Tags: List["TagTypeDef"]


class _RequiredProcessingClusterConfigTypeDef(TypedDict):
    InstanceCount: int
    InstanceType: ProcessingInstanceType
    VolumeSizeInGB: int


class ProcessingClusterConfigTypeDef(_RequiredProcessingClusterConfigTypeDef, total=False):
    VolumeKmsKeyId: str


class ProcessingFeatureStoreOutputTypeDef(TypedDict):
    FeatureGroupName: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredProcessingInputTypeDef(TypedDict):
    InputName: str


class ProcessingInputTypeDef(_RequiredProcessingInputTypeDef, total=False):
    AppManaged: bool
    S3Input: "ProcessingS3InputTypeDef"
    DatasetDefinition: "DatasetDefinitionTypeDef"


class ProcessingJobStepMetadataTypeDef(TypedDict, total=False):
    Arn: str


class _RequiredProcessingJobSummaryTypeDef(TypedDict):
    ProcessingJobName: str
    ProcessingJobArn: str
    CreationTime: datetime
    ProcessingJobStatus: ProcessingJobStatus


class ProcessingJobSummaryTypeDef(_RequiredProcessingJobSummaryTypeDef, total=False):
    ProcessingEndTime: datetime
    LastModifiedTime: datetime
    FailureReason: str
    ExitMessage: str


class ProcessingJobTypeDef(TypedDict, total=False):
    ProcessingInputs: List["ProcessingInputTypeDef"]
    ProcessingOutputConfig: "ProcessingOutputConfigTypeDef"
    ProcessingJobName: str
    ProcessingResources: "ProcessingResourcesTypeDef"
    StoppingCondition: "ProcessingStoppingConditionTypeDef"
    AppSpecification: "AppSpecificationTypeDef"
    Environment: Dict[str, str]
    NetworkConfig: "NetworkConfigTypeDef"
    RoleArn: str
    ExperimentConfig: "ExperimentConfigTypeDef"
    ProcessingJobArn: str
    ProcessingJobStatus: ProcessingJobStatus
    ExitMessage: str
    FailureReason: str
    ProcessingEndTime: datetime
    ProcessingStartTime: datetime
    LastModifiedTime: datetime
    CreationTime: datetime
    MonitoringScheduleArn: str
    AutoMLJobArn: str
    TrainingJobArn: str
    Tags: List["TagTypeDef"]


class _RequiredProcessingOutputConfigTypeDef(TypedDict):
    Outputs: List["ProcessingOutputTypeDef"]


class ProcessingOutputConfigTypeDef(_RequiredProcessingOutputConfigTypeDef, total=False):
    KmsKeyId: str


class ProcessingOutputTypeDef(TypedDict):
    OutputName: str
    S3Output: "ProcessingS3OutputTypeDef"
    FeatureStoreOutput: "ProcessingFeatureStoreOutputTypeDef"
    AppManaged: bool
    ResponseMetadata: "ResponseMetadata"


class ProcessingResourcesTypeDef(TypedDict):
    ClusterConfig: "ProcessingClusterConfigTypeDef"


class _RequiredProcessingS3InputTypeDef(TypedDict):
    S3Uri: str
    S3DataType: ProcessingS3DataType


class ProcessingS3InputTypeDef(_RequiredProcessingS3InputTypeDef, total=False):
    LocalPath: str
    S3InputMode: ProcessingS3InputMode
    S3DataDistributionType: ProcessingS3DataDistributionType
    S3CompressionType: ProcessingS3CompressionType


class ProcessingS3OutputTypeDef(TypedDict):
    S3Uri: str
    LocalPath: str
    S3UploadMode: ProcessingS3UploadMode
    ResponseMetadata: "ResponseMetadata"


class ProcessingStoppingConditionTypeDef(TypedDict):
    MaxRuntimeInSeconds: int


class _RequiredProductionVariantCoreDumpConfigTypeDef(TypedDict):
    DestinationS3Uri: str


class ProductionVariantCoreDumpConfigTypeDef(
    _RequiredProductionVariantCoreDumpConfigTypeDef, total=False
):
    KmsKeyId: str


class _RequiredProductionVariantSummaryTypeDef(TypedDict):
    VariantName: str


class ProductionVariantSummaryTypeDef(_RequiredProductionVariantSummaryTypeDef, total=False):
    DeployedImages: List["DeployedImageTypeDef"]
    CurrentWeight: float
    DesiredWeight: float
    CurrentInstanceCount: int
    DesiredInstanceCount: int


class _RequiredProductionVariantTypeDef(TypedDict):
    VariantName: str
    ModelName: str
    InitialInstanceCount: int
    InstanceType: ProductionVariantInstanceType


class ProductionVariantTypeDef(_RequiredProductionVariantTypeDef, total=False):
    InitialVariantWeight: float
    AcceleratorType: ProductionVariantAcceleratorType
    CoreDumpConfig: "ProductionVariantCoreDumpConfigTypeDef"


class ProfilerConfigForUpdateTypeDef(TypedDict, total=False):
    S3OutputPath: str
    ProfilingIntervalInMilliseconds: int
    ProfilingParameters: Dict[str, str]
    DisableProfiler: bool


class _RequiredProfilerConfigTypeDef(TypedDict):
    S3OutputPath: str


class ProfilerConfigTypeDef(_RequiredProfilerConfigTypeDef, total=False):
    ProfilingIntervalInMilliseconds: int
    ProfilingParameters: Dict[str, str]


class _RequiredProfilerRuleConfigurationTypeDef(TypedDict):
    RuleConfigurationName: str
    RuleEvaluatorImage: str


class ProfilerRuleConfigurationTypeDef(_RequiredProfilerRuleConfigurationTypeDef, total=False):
    LocalPath: str
    S3OutputPath: str
    InstanceType: ProcessingInstanceType
    VolumeSizeInGB: int
    RuleParameters: Dict[str, str]


class ProfilerRuleEvaluationStatusTypeDef(TypedDict, total=False):
    RuleConfigurationName: str
    RuleEvaluationJobArn: str
    RuleEvaluationStatus: RuleEvaluationStatus
    StatusDetails: str
    LastModifiedTime: datetime


class _RequiredProjectSummaryTypeDef(TypedDict):
    ProjectName: str
    ProjectArn: str
    ProjectId: str
    CreationTime: datetime
    ProjectStatus: ProjectStatus


class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, total=False):
    ProjectDescription: str


class PropertyNameQueryTypeDef(TypedDict):
    PropertyNameHint: str


class PropertyNameSuggestionTypeDef(TypedDict, total=False):
    PropertyName: str


class ProvisioningParameterTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class PublicWorkforceTaskPriceTypeDef(TypedDict, total=False):
    AmountInUsd: "USDTypeDef"


class PutModelPackageGroupPolicyOutputTypeDef(TypedDict):
    ModelPackageGroupArn: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredRedshiftDatasetDefinitionTypeDef(TypedDict):
    ClusterId: str
    Database: str
    DbUser: str
    QueryString: str
    ClusterRoleArn: str
    OutputS3Uri: str
    OutputFormat: RedshiftResultFormat


class RedshiftDatasetDefinitionTypeDef(_RequiredRedshiftDatasetDefinitionTypeDef, total=False):
    KmsKeyId: str
    OutputCompression: RedshiftResultCompressionType


class RegisterModelStepMetadataTypeDef(TypedDict, total=False):
    Arn: str


class RenderUiTemplateResponseTypeDef(TypedDict):
    RenderedContent: str
    Errors: List["RenderingErrorTypeDef"]


class RenderableTaskTypeDef(TypedDict):
    Input: str


class RenderingErrorTypeDef(TypedDict):
    Code: str
    Message: str


class RepositoryAuthConfigTypeDef(TypedDict):
    RepositoryCredentialsProviderArn: str


class ResolvedAttributesTypeDef(TypedDict, total=False):
    AutoMLJobObjective: "AutoMLJobObjectiveTypeDef"
    ProblemType: ProblemType
    CompletionCriteria: "AutoMLJobCompletionCriteriaTypeDef"


class _RequiredResourceConfigTypeDef(TypedDict):
    InstanceType: TrainingInstanceType
    InstanceCount: int
    VolumeSizeInGB: int


class ResourceConfigTypeDef(_RequiredResourceConfigTypeDef, total=False):
    VolumeKmsKeyId: str


class ResourceLimitsTypeDef(TypedDict):
    MaxNumberOfTrainingJobs: int
    MaxParallelTrainingJobs: int


class ResourceSpecTypeDef(TypedDict, total=False):
    SageMakerImageArn: str
    SageMakerImageVersionArn: str
    InstanceType: AppInstanceType


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RetentionPolicyTypeDef(TypedDict, total=False):
    HomeEfsFileSystem: RetentionType


class RetryStrategyTypeDef(TypedDict):
    MaximumRetryAttempts: int


class _RequiredS3DataSourceTypeDef(TypedDict):
    S3DataType: S3DataType
    S3Uri: str


class S3DataSourceTypeDef(_RequiredS3DataSourceTypeDef, total=False):
    S3DataDistributionType: S3DataDistribution
    AttributeNames: List[str]


class _RequiredS3StorageConfigTypeDef(TypedDict):
    S3Uri: str


class S3StorageConfigTypeDef(_RequiredS3StorageConfigTypeDef, total=False):
    KmsKeyId: str
    ResolvedOutputS3Uri: str


class ScheduleConfigTypeDef(TypedDict):
    ScheduleExpression: str


class SearchExpressionTypeDef(TypedDict, total=False):
    Filters: List["FilterTypeDef"]
    NestedFilters: List["NestedFiltersTypeDef"]
    SubExpressions: List[Dict[str, Any]]
    Operator: BooleanOperator


class SearchRecordTypeDef(TypedDict, total=False):
    TrainingJob: "TrainingJobTypeDef"
    Experiment: "ExperimentTypeDef"
    Trial: "TrialTypeDef"
    TrialComponent: "TrialComponentTypeDef"
    Endpoint: "EndpointTypeDef"
    ModelPackage: "ModelPackageTypeDef"
    ModelPackageGroup: "ModelPackageGroupTypeDef"
    Pipeline: "PipelineTypeDef"
    PipelineExecution: "PipelineExecutionTypeDef"
    FeatureGroup: "FeatureGroupTypeDef"


class SearchResponseTypeDef(TypedDict, total=False):
    Results: List["SearchRecordTypeDef"]
    NextToken: str


class _RequiredSecondaryStatusTransitionTypeDef(TypedDict):
    Status: SecondaryStatus
    StartTime: datetime


class SecondaryStatusTransitionTypeDef(_RequiredSecondaryStatusTransitionTypeDef, total=False):
    EndTime: datetime
    StatusMessage: str


class ServiceCatalogProvisionedProductDetailsTypeDef(TypedDict, total=False):
    ProvisionedProductId: str
    ProvisionedProductStatusMessage: str


class _RequiredServiceCatalogProvisioningDetailsTypeDef(TypedDict):
    ProductId: str
    ProvisioningArtifactId: str


class ServiceCatalogProvisioningDetailsTypeDef(
    _RequiredServiceCatalogProvisioningDetailsTypeDef, total=False
):
    PathId: str
    ProvisioningParameters: List["ProvisioningParameterTypeDef"]


class SharingSettingsTypeDef(TypedDict, total=False):
    NotebookOutputOption: NotebookOutputOption
    S3OutputPath: str
    S3KmsKeyId: str


class ShuffleConfigTypeDef(TypedDict):
    Seed: int


class SourceAlgorithmSpecificationTypeDef(TypedDict):
    SourceAlgorithms: List["SourceAlgorithmTypeDef"]


class _RequiredSourceAlgorithmTypeDef(TypedDict):
    AlgorithmName: str


class SourceAlgorithmTypeDef(_RequiredSourceAlgorithmTypeDef, total=False):
    ModelDataUrl: str


class SourceIpConfigTypeDef(TypedDict):
    Cidrs: List[str]


class StartPipelineExecutionResponseTypeDef(TypedDict, total=False):
    PipelineExecutionArn: str


class StopPipelineExecutionResponseTypeDef(TypedDict, total=False):
    PipelineExecutionArn: str


class StoppingConditionTypeDef(TypedDict, total=False):
    MaxRuntimeInSeconds: int
    MaxWaitTimeInSeconds: int


class _RequiredSubscribedWorkteamTypeDef(TypedDict):
    WorkteamArn: str


class SubscribedWorkteamTypeDef(_RequiredSubscribedWorkteamTypeDef, total=False):
    MarketplaceTitle: str
    SellerName: str
    MarketplaceDescription: str
    ListingId: str


class SuggestionQueryTypeDef(TypedDict, total=False):
    PropertyNameQuery: "PropertyNameQueryTypeDef"


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class _RequiredTargetPlatformTypeDef(TypedDict):
    Os: TargetPlatformOs
    Arch: TargetPlatformArch


class TargetPlatformTypeDef(_RequiredTargetPlatformTypeDef, total=False):
    Accelerator: TargetPlatformAccelerator


class TensorBoardAppSettingsTypeDef(TypedDict, total=False):
    DefaultResourceSpec: "ResourceSpecTypeDef"


class _RequiredTensorBoardOutputConfigTypeDef(TypedDict):
    S3OutputPath: str


class TensorBoardOutputConfigTypeDef(_RequiredTensorBoardOutputConfigTypeDef, total=False):
    LocalPath: str


_RequiredTrafficRoutingConfigTypeDef = TypedDict(
    "_RequiredTrafficRoutingConfigTypeDef",
    {"Type": TrafficRoutingConfigType, "WaitIntervalInSeconds": int},
)
_OptionalTrafficRoutingConfigTypeDef = TypedDict(
    "_OptionalTrafficRoutingConfigTypeDef", {"CanarySize": "CapacitySizeTypeDef"}, total=False
)


class TrafficRoutingConfigTypeDef(
    _RequiredTrafficRoutingConfigTypeDef, _OptionalTrafficRoutingConfigTypeDef
):
    pass


class _RequiredTrainingJobDefinitionTypeDef(TypedDict):
    TrainingInputMode: TrainingInputMode
    InputDataConfig: List["ChannelTypeDef"]
    OutputDataConfig: "OutputDataConfigTypeDef"
    ResourceConfig: "ResourceConfigTypeDef"
    StoppingCondition: "StoppingConditionTypeDef"


class TrainingJobDefinitionTypeDef(_RequiredTrainingJobDefinitionTypeDef, total=False):
    HyperParameters: Dict[str, str]


class TrainingJobStatusCountersTypeDef(TypedDict, total=False):
    Completed: int
    InProgress: int
    RetryableError: int
    NonRetryableError: int
    Stopped: int


class TrainingJobStepMetadataTypeDef(TypedDict, total=False):
    Arn: str


class _RequiredTrainingJobSummaryTypeDef(TypedDict):
    TrainingJobName: str
    TrainingJobArn: str
    CreationTime: datetime
    TrainingJobStatus: TrainingJobStatus


class TrainingJobSummaryTypeDef(_RequiredTrainingJobSummaryTypeDef, total=False):
    TrainingEndTime: datetime
    LastModifiedTime: datetime


class TrainingJobTypeDef(TypedDict, total=False):
    TrainingJobName: str
    TrainingJobArn: str
    TuningJobArn: str
    LabelingJobArn: str
    AutoMLJobArn: str
    ModelArtifacts: "ModelArtifactsTypeDef"
    TrainingJobStatus: TrainingJobStatus
    SecondaryStatus: SecondaryStatus
    FailureReason: str
    HyperParameters: Dict[str, str]
    AlgorithmSpecification: "AlgorithmSpecificationTypeDef"
    RoleArn: str
    InputDataConfig: List["ChannelTypeDef"]
    OutputDataConfig: "OutputDataConfigTypeDef"
    ResourceConfig: "ResourceConfigTypeDef"
    VpcConfig: "VpcConfigTypeDef"
    StoppingCondition: "StoppingConditionTypeDef"
    CreationTime: datetime
    TrainingStartTime: datetime
    TrainingEndTime: datetime
    LastModifiedTime: datetime
    SecondaryStatusTransitions: List["SecondaryStatusTransitionTypeDef"]
    FinalMetricDataList: List["MetricDataTypeDef"]
    EnableNetworkIsolation: bool
    EnableInterContainerTrafficEncryption: bool
    EnableManagedSpotTraining: bool
    CheckpointConfig: "CheckpointConfigTypeDef"
    TrainingTimeInSeconds: int
    BillableTimeInSeconds: int
    DebugHookConfig: "DebugHookConfigTypeDef"
    ExperimentConfig: "ExperimentConfigTypeDef"
    DebugRuleConfigurations: List["DebugRuleConfigurationTypeDef"]
    TensorBoardOutputConfig: "TensorBoardOutputConfigTypeDef"
    DebugRuleEvaluationStatuses: List["DebugRuleEvaluationStatusTypeDef"]
    Environment: Dict[str, str]
    RetryStrategy: "RetryStrategyTypeDef"
    Tags: List["TagTypeDef"]


class _RequiredTrainingSpecificationTypeDef(TypedDict):
    TrainingImage: str
    SupportedTrainingInstanceTypes: List[TrainingInstanceType]
    TrainingChannels: List["ChannelSpecificationTypeDef"]


class TrainingSpecificationTypeDef(_RequiredTrainingSpecificationTypeDef, total=False):
    TrainingImageDigest: str
    SupportedHyperParameters: List["HyperParameterSpecificationTypeDef"]
    SupportsDistributedTraining: bool
    MetricDefinitions: List["MetricDefinitionTypeDef"]
    SupportedTuningJobObjectiveMetrics: List["HyperParameterTuningJobObjectiveTypeDef"]


class TransformDataSourceTypeDef(TypedDict):
    S3DataSource: "TransformS3DataSourceTypeDef"


class _RequiredTransformInputTypeDef(TypedDict):
    DataSource: "TransformDataSourceTypeDef"


class TransformInputTypeDef(_RequiredTransformInputTypeDef, total=False):
    ContentType: str
    CompressionType: CompressionType
    SplitType: SplitType


class _RequiredTransformJobDefinitionTypeDef(TypedDict):
    TransformInput: "TransformInputTypeDef"
    TransformOutput: "TransformOutputTypeDef"
    TransformResources: "TransformResourcesTypeDef"


class TransformJobDefinitionTypeDef(_RequiredTransformJobDefinitionTypeDef, total=False):
    MaxConcurrentTransforms: int
    MaxPayloadInMB: int
    BatchStrategy: BatchStrategy
    Environment: Dict[str, str]


class TransformJobStepMetadataTypeDef(TypedDict, total=False):
    Arn: str


class _RequiredTransformJobSummaryTypeDef(TypedDict):
    TransformJobName: str
    TransformJobArn: str
    CreationTime: datetime
    TransformJobStatus: TransformJobStatus


class TransformJobSummaryTypeDef(_RequiredTransformJobSummaryTypeDef, total=False):
    TransformEndTime: datetime
    LastModifiedTime: datetime
    FailureReason: str


class TransformJobTypeDef(TypedDict, total=False):
    TransformJobName: str
    TransformJobArn: str
    TransformJobStatus: TransformJobStatus
    FailureReason: str
    ModelName: str
    MaxConcurrentTransforms: int
    ModelClientConfig: "ModelClientConfigTypeDef"
    MaxPayloadInMB: int
    BatchStrategy: BatchStrategy
    Environment: Dict[str, str]
    TransformInput: "TransformInputTypeDef"
    TransformOutput: "TransformOutputTypeDef"
    TransformResources: "TransformResourcesTypeDef"
    CreationTime: datetime
    TransformStartTime: datetime
    TransformEndTime: datetime
    LabelingJobArn: str
    AutoMLJobArn: str
    DataProcessing: "DataProcessingTypeDef"
    ExperimentConfig: "ExperimentConfigTypeDef"
    Tags: List["TagTypeDef"]


class TransformOutputTypeDef(TypedDict):
    S3OutputPath: str
    Accept: str
    AssembleWith: AssemblyType
    KmsKeyId: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredTransformResourcesTypeDef(TypedDict):
    InstanceType: TransformInstanceType
    InstanceCount: int


class TransformResourcesTypeDef(_RequiredTransformResourcesTypeDef, total=False):
    VolumeKmsKeyId: str


class TransformS3DataSourceTypeDef(TypedDict):
    S3DataType: S3DataType
    S3Uri: str


class _RequiredTrialComponentArtifactTypeDef(TypedDict):
    Value: str


class TrialComponentArtifactTypeDef(_RequiredTrialComponentArtifactTypeDef, total=False):
    MediaType: str


class TrialComponentMetricSummaryTypeDef(TypedDict, total=False):
    MetricName: str
    SourceArn: str
    TimeStamp: datetime
    Max: float
    Min: float
    Last: float
    Count: int
    Avg: float
    StdDev: float


class TrialComponentParameterValueTypeDef(TypedDict, total=False):
    StringValue: str
    NumberValue: float


class TrialComponentSimpleSummaryTypeDef(TypedDict, total=False):
    TrialComponentName: str
    TrialComponentArn: str
    TrialComponentSource: "TrialComponentSourceTypeDef"
    CreationTime: datetime
    CreatedBy: "UserContextTypeDef"


class TrialComponentSourceDetailTypeDef(TypedDict, total=False):
    SourceArn: str
    TrainingJob: "TrainingJobTypeDef"
    ProcessingJob: "ProcessingJobTypeDef"
    TransformJob: "TransformJobTypeDef"


class _RequiredTrialComponentSourceTypeDef(TypedDict):
    SourceArn: str


class TrialComponentSourceTypeDef(_RequiredTrialComponentSourceTypeDef, total=False):
    SourceType: str


class TrialComponentStatusTypeDef(TypedDict, total=False):
    PrimaryStatus: TrialComponentPrimaryStatus
    Message: str


class TrialComponentSummaryTypeDef(TypedDict, total=False):
    TrialComponentName: str
    TrialComponentArn: str
    DisplayName: str
    TrialComponentSource: "TrialComponentSourceTypeDef"
    Status: "TrialComponentStatusTypeDef"
    StartTime: datetime
    EndTime: datetime
    CreationTime: datetime
    CreatedBy: "UserContextTypeDef"
    LastModifiedTime: datetime
    LastModifiedBy: "UserContextTypeDef"


class TrialComponentTypeDef(TypedDict, total=False):
    TrialComponentName: str
    DisplayName: str
    TrialComponentArn: str
    Source: "TrialComponentSourceTypeDef"
    Status: "TrialComponentStatusTypeDef"
    StartTime: datetime
    EndTime: datetime
    CreationTime: datetime
    CreatedBy: "UserContextTypeDef"
    LastModifiedTime: datetime
    LastModifiedBy: "UserContextTypeDef"
    Parameters: Dict[str, "TrialComponentParameterValueTypeDef"]
    InputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"]
    OutputArtifacts: Dict[str, "TrialComponentArtifactTypeDef"]
    Metrics: List["TrialComponentMetricSummaryTypeDef"]
    MetadataProperties: "MetadataPropertiesTypeDef"
    SourceDetail: "TrialComponentSourceDetailTypeDef"
    Tags: List["TagTypeDef"]
    Parents: List["ParentTypeDef"]


class _RequiredTrialSourceTypeDef(TypedDict):
    SourceArn: str


class TrialSourceTypeDef(_RequiredTrialSourceTypeDef, total=False):
    SourceType: str


class TrialSummaryTypeDef(TypedDict, total=False):
    TrialArn: str
    TrialName: str
    DisplayName: str
    TrialSource: "TrialSourceTypeDef"
    CreationTime: datetime
    LastModifiedTime: datetime


class TrialTypeDef(TypedDict, total=False):
    TrialName: str
    TrialArn: str
    DisplayName: str
    ExperimentName: str
    Source: "TrialSourceTypeDef"
    CreationTime: datetime
    CreatedBy: "UserContextTypeDef"
    LastModifiedTime: datetime
    LastModifiedBy: "UserContextTypeDef"
    MetadataProperties: "MetadataPropertiesTypeDef"
    Tags: List["TagTypeDef"]
    TrialComponentSummaries: List["TrialComponentSimpleSummaryTypeDef"]


class TuningJobCompletionCriteriaTypeDef(TypedDict):
    TargetObjectiveMetricValue: float


class USDTypeDef(TypedDict, total=False):
    Dollars: int
    Cents: int
    TenthFractionsOfACent: int


class UiConfigTypeDef(TypedDict, total=False):
    UiTemplateS3Uri: str
    HumanTaskUiArn: str


class UiTemplateInfoTypeDef(TypedDict, total=False):
    Url: str
    ContentSha256: str


class UiTemplateTypeDef(TypedDict):
    Content: str


class UpdateActionResponseTypeDef(TypedDict, total=False):
    ActionArn: str


class UpdateAppImageConfigResponseTypeDef(TypedDict, total=False):
    AppImageConfigArn: str


class UpdateArtifactResponseTypeDef(TypedDict, total=False):
    ArtifactArn: str


class UpdateCodeRepositoryOutputTypeDef(TypedDict):
    CodeRepositoryArn: str
    ResponseMetadata: "ResponseMetadata"


class UpdateContextResponseTypeDef(TypedDict, total=False):
    ContextArn: str


class UpdateDomainResponseTypeDef(TypedDict, total=False):
    DomainArn: str


class UpdateEndpointOutputTypeDef(TypedDict):
    EndpointArn: str
    ResponseMetadata: "ResponseMetadata"


class UpdateEndpointWeightsAndCapacitiesOutputTypeDef(TypedDict):
    EndpointArn: str
    ResponseMetadata: "ResponseMetadata"


class UpdateExperimentResponseTypeDef(TypedDict, total=False):
    ExperimentArn: str


class UpdateImageResponseTypeDef(TypedDict, total=False):
    ImageArn: str


class UpdateModelPackageOutputTypeDef(TypedDict):
    ModelPackageArn: str
    ResponseMetadata: "ResponseMetadata"


class UpdateMonitoringScheduleResponseTypeDef(TypedDict):
    MonitoringScheduleArn: str


class UpdatePipelineExecutionResponseTypeDef(TypedDict, total=False):
    PipelineExecutionArn: str


class UpdatePipelineResponseTypeDef(TypedDict, total=False):
    PipelineArn: str


class UpdateTrainingJobResponseTypeDef(TypedDict):
    TrainingJobArn: str


class UpdateTrialComponentResponseTypeDef(TypedDict, total=False):
    TrialComponentArn: str


class UpdateTrialResponseTypeDef(TypedDict, total=False):
    TrialArn: str


class UpdateUserProfileResponseTypeDef(TypedDict, total=False):
    UserProfileArn: str


class UpdateWorkforceResponseTypeDef(TypedDict):
    Workforce: "WorkforceTypeDef"


class UpdateWorkteamResponseTypeDef(TypedDict):
    Workteam: "WorkteamTypeDef"


class UserContextTypeDef(TypedDict, total=False):
    UserProfileArn: str
    UserProfileName: str
    DomainId: str


class UserProfileDetailsTypeDef(TypedDict, total=False):
    DomainId: str
    UserProfileName: str
    Status: UserProfileStatus
    CreationTime: datetime
    LastModifiedTime: datetime


class UserSettingsTypeDef(TypedDict, total=False):
    ExecutionRole: str
    SecurityGroups: List[str]
    SharingSettings: "SharingSettingsTypeDef"
    JupyterServerAppSettings: "JupyterServerAppSettingsTypeDef"
    KernelGatewayAppSettings: "KernelGatewayAppSettingsTypeDef"
    TensorBoardAppSettings: "TensorBoardAppSettingsTypeDef"


class VariantPropertyTypeDef(TypedDict):
    VariantPropertyType: VariantPropertyType


class VpcConfigTypeDef(TypedDict):
    SecurityGroupIds: List[str]
    Subnets: List[str]


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int


class _RequiredWorkforceTypeDef(TypedDict):
    WorkforceName: str
    WorkforceArn: str


class WorkforceTypeDef(_RequiredWorkforceTypeDef, total=False):
    LastUpdatedDate: datetime
    SourceIpConfig: "SourceIpConfigTypeDef"
    SubDomain: str
    CognitoConfig: "CognitoConfigTypeDef"
    OidcConfig: "OidcConfigForResponseTypeDef"
    CreateDate: datetime


class _RequiredWorkteamTypeDef(TypedDict):
    WorkteamName: str
    MemberDefinitions: List["MemberDefinitionTypeDef"]
    WorkteamArn: str
    Description: str


class WorkteamTypeDef(_RequiredWorkteamTypeDef, total=False):
    WorkforceArn: str
    ProductListingIds: List[str]
    SubDomain: str
    CreateDate: datetime
    LastUpdatedDate: datetime
    NotificationConfiguration: "NotificationConfigurationTypeDef"
