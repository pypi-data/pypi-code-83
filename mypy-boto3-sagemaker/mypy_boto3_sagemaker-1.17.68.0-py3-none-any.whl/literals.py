"""
Type annotations for sagemaker service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker/literals.html)

Usage::

    ```python
    from mypy_boto3_sagemaker.literals import ActionStatus

    data: ActionStatus = "Completed"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActionStatus",
    "AlgorithmSortBy",
    "AlgorithmStatus",
    "AppImageConfigSortKey",
    "AppInstanceType",
    "AppNetworkAccessType",
    "AppSortKey",
    "AppStatus",
    "AppType",
    "ArtifactSourceIdType",
    "AssemblyType",
    "AssociationEdgeType",
    "AthenaResultCompressionType",
    "AthenaResultFormat",
    "AuthMode",
    "AutoMLJobObjectiveType",
    "AutoMLJobSecondaryStatus",
    "AutoMLJobStatus",
    "AutoMLMetricEnum",
    "AutoMLS3DataType",
    "AutoMLSortBy",
    "AutoMLSortOrder",
    "AwsManagedHumanLoopRequestSource",
    "BatchStrategy",
    "BooleanOperator",
    "CandidateSortBy",
    "CandidateStatus",
    "CandidateStepType",
    "CapacitySizeType",
    "CaptureMode",
    "CaptureStatus",
    "CodeRepositorySortBy",
    "CodeRepositorySortOrder",
    "CompilationJobStatus",
    "CompressionType",
    "ConditionOutcome",
    "ContainerMode",
    "ContentClassifier",
    "DataDistributionType",
    "DetailedAlgorithmStatus",
    "DetailedModelPackageStatus",
    "DirectInternetAccess",
    "DomainStatus",
    "EdgePackagingJobStatus",
    "EndpointConfigSortKey",
    "EndpointDeletedWaiterName",
    "EndpointInServiceWaiterName",
    "EndpointSortKey",
    "EndpointStatus",
    "ExecutionStatus",
    "FeatureGroupSortBy",
    "FeatureGroupSortOrder",
    "FeatureGroupStatus",
    "FeatureType",
    "FileSystemAccessMode",
    "FileSystemType",
    "FlowDefinitionStatus",
    "Framework",
    "HumanTaskUiStatus",
    "HyperParameterScalingType",
    "HyperParameterTuningJobObjectiveType",
    "HyperParameterTuningJobSortByOptions",
    "HyperParameterTuningJobStatus",
    "HyperParameterTuningJobStrategyType",
    "HyperParameterTuningJobWarmStartType",
    "ImageSortBy",
    "ImageSortOrder",
    "ImageStatus",
    "ImageVersionSortBy",
    "ImageVersionSortOrder",
    "ImageVersionStatus",
    "InferenceExecutionMode",
    "InputMode",
    "InstanceType",
    "JoinSource",
    "LabelingJobStatus",
    "ListActionsPaginatorName",
    "ListAlgorithmsPaginatorName",
    "ListAppImageConfigsPaginatorName",
    "ListAppsPaginatorName",
    "ListArtifactsPaginatorName",
    "ListAssociationsPaginatorName",
    "ListAutoMLJobsPaginatorName",
    "ListCandidatesForAutoMLJobPaginatorName",
    "ListCodeRepositoriesPaginatorName",
    "ListCompilationJobsPaginatorName",
    "ListCompilationJobsSortBy",
    "ListContextsPaginatorName",
    "ListDataQualityJobDefinitionsPaginatorName",
    "ListDeviceFleetsPaginatorName",
    "ListDeviceFleetsSortBy",
    "ListDevicesPaginatorName",
    "ListDomainsPaginatorName",
    "ListEdgePackagingJobsPaginatorName",
    "ListEdgePackagingJobsSortBy",
    "ListEndpointConfigsPaginatorName",
    "ListEndpointsPaginatorName",
    "ListExperimentsPaginatorName",
    "ListFeatureGroupsPaginatorName",
    "ListFlowDefinitionsPaginatorName",
    "ListHumanTaskUisPaginatorName",
    "ListHyperParameterTuningJobsPaginatorName",
    "ListImageVersionsPaginatorName",
    "ListImagesPaginatorName",
    "ListLabelingJobsForWorkteamPaginatorName",
    "ListLabelingJobsForWorkteamSortByOptions",
    "ListLabelingJobsPaginatorName",
    "ListModelBiasJobDefinitionsPaginatorName",
    "ListModelExplainabilityJobDefinitionsPaginatorName",
    "ListModelPackageGroupsPaginatorName",
    "ListModelPackagesPaginatorName",
    "ListModelQualityJobDefinitionsPaginatorName",
    "ListModelsPaginatorName",
    "ListMonitoringExecutionsPaginatorName",
    "ListMonitoringSchedulesPaginatorName",
    "ListNotebookInstanceLifecycleConfigsPaginatorName",
    "ListNotebookInstancesPaginatorName",
    "ListPipelineExecutionStepsPaginatorName",
    "ListPipelineExecutionsPaginatorName",
    "ListPipelineParametersForExecutionPaginatorName",
    "ListPipelinesPaginatorName",
    "ListProcessingJobsPaginatorName",
    "ListSubscribedWorkteamsPaginatorName",
    "ListTagsPaginatorName",
    "ListTrainingJobsForHyperParameterTuningJobPaginatorName",
    "ListTrainingJobsPaginatorName",
    "ListTransformJobsPaginatorName",
    "ListTrialComponentsPaginatorName",
    "ListTrialsPaginatorName",
    "ListUserProfilesPaginatorName",
    "ListWorkforcesPaginatorName",
    "ListWorkforcesSortByOptions",
    "ListWorkteamsPaginatorName",
    "ListWorkteamsSortByOptions",
    "ModelApprovalStatus",
    "ModelCacheSetting",
    "ModelPackageGroupSortBy",
    "ModelPackageGroupStatus",
    "ModelPackageSortBy",
    "ModelPackageStatus",
    "ModelPackageType",
    "ModelSortKey",
    "MonitoringExecutionSortKey",
    "MonitoringJobDefinitionSortKey",
    "MonitoringProblemType",
    "MonitoringScheduleSortKey",
    "MonitoringType",
    "NotebookInstanceAcceleratorType",
    "NotebookInstanceDeletedWaiterName",
    "NotebookInstanceInServiceWaiterName",
    "NotebookInstanceLifecycleConfigSortKey",
    "NotebookInstanceLifecycleConfigSortOrder",
    "NotebookInstanceSortKey",
    "NotebookInstanceSortOrder",
    "NotebookInstanceStatus",
    "NotebookInstanceStoppedWaiterName",
    "NotebookOutputOption",
    "ObjectiveStatus",
    "OfflineStoreStatusValue",
    "Operator",
    "OrderKey",
    "ParameterType",
    "PipelineExecutionStatus",
    "PipelineStatus",
    "ProblemType",
    "ProcessingInstanceType",
    "ProcessingJobCompletedOrStoppedWaiterName",
    "ProcessingJobStatus",
    "ProcessingS3CompressionType",
    "ProcessingS3DataDistributionType",
    "ProcessingS3DataType",
    "ProcessingS3InputMode",
    "ProcessingS3UploadMode",
    "ProductionVariantAcceleratorType",
    "ProductionVariantInstanceType",
    "ProfilingStatus",
    "ProjectSortBy",
    "ProjectSortOrder",
    "ProjectStatus",
    "RecordWrapper",
    "RedshiftResultCompressionType",
    "RedshiftResultFormat",
    "RepositoryAccessMode",
    "ResourceType",
    "RetentionType",
    "RootAccess",
    "RuleEvaluationStatus",
    "S3DataDistribution",
    "S3DataType",
    "SagemakerServicecatalogStatus",
    "ScheduleStatus",
    "SearchPaginatorName",
    "SearchSortOrder",
    "SecondaryStatus",
    "SortActionsBy",
    "SortArtifactsBy",
    "SortAssociationsBy",
    "SortBy",
    "SortContextsBy",
    "SortExperimentsBy",
    "SortOrder",
    "SortPipelineExecutionsBy",
    "SortPipelinesBy",
    "SortTrialComponentsBy",
    "SortTrialsBy",
    "SplitType",
    "StepStatus",
    "TargetDevice",
    "TargetPlatformAccelerator",
    "TargetPlatformArch",
    "TargetPlatformOs",
    "TrafficRoutingConfigType",
    "TrainingInputMode",
    "TrainingInstanceType",
    "TrainingJobCompletedOrStoppedWaiterName",
    "TrainingJobEarlyStoppingType",
    "TrainingJobSortByOptions",
    "TrainingJobStatus",
    "TransformInstanceType",
    "TransformJobCompletedOrStoppedWaiterName",
    "TransformJobStatus",
    "TrialComponentPrimaryStatus",
    "UserProfileSortKey",
    "UserProfileStatus",
    "VariantPropertyType",
)


ActionStatus = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping", "Unknown"]
AlgorithmSortBy = Literal["CreationTime", "Name"]
AlgorithmStatus = Literal["Completed", "Deleting", "Failed", "InProgress", "Pending"]
AppImageConfigSortKey = Literal["CreationTime", "LastModifiedTime", "Name"]
AppInstanceType = Literal[
    "ml.c5.12xlarge",
    "ml.c5.18xlarge",
    "ml.c5.24xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.large",
    "ml.c5.xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.16xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.8xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.t3.2xlarge",
    "ml.t3.large",
    "ml.t3.medium",
    "ml.t3.micro",
    "ml.t3.small",
    "ml.t3.xlarge",
    "system",
]
AppNetworkAccessType = Literal["PublicInternetOnly", "VpcOnly"]
AppSortKey = Literal["CreationTime"]
AppStatus = Literal["Deleted", "Deleting", "Failed", "InService", "Pending"]
AppType = Literal["JupyterServer", "KernelGateway", "TensorBoard"]
ArtifactSourceIdType = Literal["Custom", "MD5Hash", "S3ETag", "S3Version"]
AssemblyType = Literal["Line", "None"]
AssociationEdgeType = Literal["AssociatedWith", "ContributedTo", "DerivedFrom", "Produced"]
AthenaResultCompressionType = Literal["GZIP", "SNAPPY", "ZLIB"]
AthenaResultFormat = Literal["AVRO", "JSON", "ORC", "PARQUET", "TEXTFILE"]
AuthMode = Literal["IAM", "SSO"]
AutoMLJobObjectiveType = Literal["Maximize", "Minimize"]
AutoMLJobSecondaryStatus = Literal[
    "AnalyzingData",
    "CandidateDefinitionsGenerated",
    "Completed",
    "DeployingModel",
    "ExplainabilityError",
    "Failed",
    "FeatureEngineering",
    "GeneratingExplainabilityReport",
    "MaxAutoMLJobRuntimeReached",
    "MaxCandidatesReached",
    "ModelDeploymentError",
    "ModelTuning",
    "Starting",
    "Stopped",
    "Stopping",
]
AutoMLJobStatus = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
AutoMLMetricEnum = Literal["AUC", "Accuracy", "F1", "F1macro", "MSE"]
AutoMLS3DataType = Literal["ManifestFile", "S3Prefix"]
AutoMLSortBy = Literal["CreationTime", "Name", "Status"]
AutoMLSortOrder = Literal["Ascending", "Descending"]
AwsManagedHumanLoopRequestSource = Literal[
    "AWS/Rekognition/DetectModerationLabels/Image/V3", "AWS/Textract/AnalyzeDocument/Forms/V1"
]
BatchStrategy = Literal["MultiRecord", "SingleRecord"]
BooleanOperator = Literal["And", "Or"]
CandidateSortBy = Literal["CreationTime", "FinalObjectiveMetricValue", "Status"]
CandidateStatus = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
CandidateStepType = Literal[
    "AWS::SageMaker::ProcessingJob", "AWS::SageMaker::TrainingJob", "AWS::SageMaker::TransformJob"
]
CapacitySizeType = Literal["CAPACITY_PERCENT", "INSTANCE_COUNT"]
CaptureMode = Literal["Input", "Output"]
CaptureStatus = Literal["Started", "Stopped"]
CodeRepositorySortBy = Literal["CreationTime", "LastModifiedTime", "Name"]
CodeRepositorySortOrder = Literal["Ascending", "Descending"]
CompilationJobStatus = Literal[
    "COMPLETED", "FAILED", "INPROGRESS", "STARTING", "STOPPED", "STOPPING"
]
CompressionType = Literal["Gzip", "None"]
ConditionOutcome = Literal["False", "True"]
ContainerMode = Literal["MultiModel", "SingleModel"]
ContentClassifier = Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
DataDistributionType = Literal["FullyReplicated", "ShardedByS3Key"]
DetailedAlgorithmStatus = Literal["Completed", "Failed", "InProgress", "NotStarted"]
DetailedModelPackageStatus = Literal["Completed", "Failed", "InProgress", "NotStarted"]
DirectInternetAccess = Literal["Disabled", "Enabled"]
DomainStatus = Literal[
    "Delete_Failed", "Deleting", "Failed", "InService", "Pending", "Update_Failed", "Updating"
]
EdgePackagingJobStatus = Literal[
    "COMPLETED", "FAILED", "INPROGRESS", "STARTING", "STOPPED", "STOPPING"
]
EndpointConfigSortKey = Literal["CreationTime", "Name"]
EndpointDeletedWaiterName = Literal["endpoint_deleted"]
EndpointInServiceWaiterName = Literal["endpoint_in_service"]
EndpointSortKey = Literal["CreationTime", "Name", "Status"]
EndpointStatus = Literal[
    "Creating",
    "Deleting",
    "Failed",
    "InService",
    "OutOfService",
    "RollingBack",
    "SystemUpdating",
    "Updating",
]
ExecutionStatus = Literal[
    "Completed", "CompletedWithViolations", "Failed", "InProgress", "Pending", "Stopped", "Stopping"
]
FeatureGroupSortBy = Literal["CreationTime", "FeatureGroupStatus", "Name", "OfflineStoreStatus"]
FeatureGroupSortOrder = Literal["Ascending", "Descending"]
FeatureGroupStatus = Literal["CreateFailed", "Created", "Creating", "DeleteFailed", "Deleting"]
FeatureType = Literal["Fractional", "Integral", "String"]
FileSystemAccessMode = Literal["ro", "rw"]
FileSystemType = Literal["EFS", "FSxLustre"]
FlowDefinitionStatus = Literal["Active", "Deleting", "Failed", "Initializing"]
Framework = Literal[
    "DARKNET", "KERAS", "MXNET", "ONNX", "PYTORCH", "SKLEARN", "TENSORFLOW", "TFLITE", "XGBOOST"
]
HumanTaskUiStatus = Literal["Active", "Deleting"]
HyperParameterScalingType = Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"]
HyperParameterTuningJobObjectiveType = Literal["Maximize", "Minimize"]
HyperParameterTuningJobSortByOptions = Literal["CreationTime", "Name", "Status"]
HyperParameterTuningJobStatus = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
HyperParameterTuningJobStrategyType = Literal["Bayesian", "Random"]
HyperParameterTuningJobWarmStartType = Literal["IdenticalDataAndAlgorithm", "TransferLearning"]
ImageSortBy = Literal["CREATION_TIME", "IMAGE_NAME", "LAST_MODIFIED_TIME"]
ImageSortOrder = Literal["ASCENDING", "DESCENDING"]
ImageStatus = Literal[
    "CREATED", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING", "UPDATE_FAILED", "UPDATING"
]
ImageVersionSortBy = Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "VERSION"]
ImageVersionSortOrder = Literal["ASCENDING", "DESCENDING"]
ImageVersionStatus = Literal["CREATED", "CREATE_FAILED", "CREATING", "DELETE_FAILED", "DELETING"]
InferenceExecutionMode = Literal["Direct", "Serial"]
InputMode = Literal["File", "Pipe"]
InstanceType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.xlarge",
    "ml.c5d.18xlarge",
    "ml.c5d.2xlarge",
    "ml.c5d.4xlarge",
    "ml.c5d.9xlarge",
    "ml.c5d.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.t2.2xlarge",
    "ml.t2.large",
    "ml.t2.medium",
    "ml.t2.xlarge",
    "ml.t3.2xlarge",
    "ml.t3.large",
    "ml.t3.medium",
    "ml.t3.xlarge",
]
JoinSource = Literal["Input", "None"]
LabelingJobStatus = Literal[
    "Completed", "Failed", "InProgress", "Initializing", "Stopped", "Stopping"
]
ListActionsPaginatorName = Literal["list_actions"]
ListAlgorithmsPaginatorName = Literal["list_algorithms"]
ListAppImageConfigsPaginatorName = Literal["list_app_image_configs"]
ListAppsPaginatorName = Literal["list_apps"]
ListArtifactsPaginatorName = Literal["list_artifacts"]
ListAssociationsPaginatorName = Literal["list_associations"]
ListAutoMLJobsPaginatorName = Literal["list_auto_ml_jobs"]
ListCandidatesForAutoMLJobPaginatorName = Literal["list_candidates_for_auto_ml_job"]
ListCodeRepositoriesPaginatorName = Literal["list_code_repositories"]
ListCompilationJobsPaginatorName = Literal["list_compilation_jobs"]
ListCompilationJobsSortBy = Literal["CreationTime", "Name", "Status"]
ListContextsPaginatorName = Literal["list_contexts"]
ListDataQualityJobDefinitionsPaginatorName = Literal["list_data_quality_job_definitions"]
ListDeviceFleetsPaginatorName = Literal["list_device_fleets"]
ListDeviceFleetsSortBy = Literal["CREATION_TIME", "LAST_MODIFIED_TIME", "NAME"]
ListDevicesPaginatorName = Literal["list_devices"]
ListDomainsPaginatorName = Literal["list_domains"]
ListEdgePackagingJobsPaginatorName = Literal["list_edge_packaging_jobs"]
ListEdgePackagingJobsSortBy = Literal[
    "CREATION_TIME", "LAST_MODIFIED_TIME", "MODEL_NAME", "NAME", "STATUS"
]
ListEndpointConfigsPaginatorName = Literal["list_endpoint_configs"]
ListEndpointsPaginatorName = Literal["list_endpoints"]
ListExperimentsPaginatorName = Literal["list_experiments"]
ListFeatureGroupsPaginatorName = Literal["list_feature_groups"]
ListFlowDefinitionsPaginatorName = Literal["list_flow_definitions"]
ListHumanTaskUisPaginatorName = Literal["list_human_task_uis"]
ListHyperParameterTuningJobsPaginatorName = Literal["list_hyper_parameter_tuning_jobs"]
ListImageVersionsPaginatorName = Literal["list_image_versions"]
ListImagesPaginatorName = Literal["list_images"]
ListLabelingJobsForWorkteamPaginatorName = Literal["list_labeling_jobs_for_workteam"]
ListLabelingJobsForWorkteamSortByOptions = Literal["CreationTime"]
ListLabelingJobsPaginatorName = Literal["list_labeling_jobs"]
ListModelBiasJobDefinitionsPaginatorName = Literal["list_model_bias_job_definitions"]
ListModelExplainabilityJobDefinitionsPaginatorName = Literal[
    "list_model_explainability_job_definitions"
]
ListModelPackageGroupsPaginatorName = Literal["list_model_package_groups"]
ListModelPackagesPaginatorName = Literal["list_model_packages"]
ListModelQualityJobDefinitionsPaginatorName = Literal["list_model_quality_job_definitions"]
ListModelsPaginatorName = Literal["list_models"]
ListMonitoringExecutionsPaginatorName = Literal["list_monitoring_executions"]
ListMonitoringSchedulesPaginatorName = Literal["list_monitoring_schedules"]
ListNotebookInstanceLifecycleConfigsPaginatorName = Literal[
    "list_notebook_instance_lifecycle_configs"
]
ListNotebookInstancesPaginatorName = Literal["list_notebook_instances"]
ListPipelineExecutionStepsPaginatorName = Literal["list_pipeline_execution_steps"]
ListPipelineExecutionsPaginatorName = Literal["list_pipeline_executions"]
ListPipelineParametersForExecutionPaginatorName = Literal["list_pipeline_parameters_for_execution"]
ListPipelinesPaginatorName = Literal["list_pipelines"]
ListProcessingJobsPaginatorName = Literal["list_processing_jobs"]
ListSubscribedWorkteamsPaginatorName = Literal["list_subscribed_workteams"]
ListTagsPaginatorName = Literal["list_tags"]
ListTrainingJobsForHyperParameterTuningJobPaginatorName = Literal[
    "list_training_jobs_for_hyper_parameter_tuning_job"
]
ListTrainingJobsPaginatorName = Literal["list_training_jobs"]
ListTransformJobsPaginatorName = Literal["list_transform_jobs"]
ListTrialComponentsPaginatorName = Literal["list_trial_components"]
ListTrialsPaginatorName = Literal["list_trials"]
ListUserProfilesPaginatorName = Literal["list_user_profiles"]
ListWorkforcesPaginatorName = Literal["list_workforces"]
ListWorkforcesSortByOptions = Literal["CreateDate", "Name"]
ListWorkteamsPaginatorName = Literal["list_workteams"]
ListWorkteamsSortByOptions = Literal["CreateDate", "Name"]
ModelApprovalStatus = Literal["Approved", "PendingManualApproval", "Rejected"]
ModelCacheSetting = Literal["Disabled", "Enabled"]
ModelPackageGroupSortBy = Literal["CreationTime", "Name"]
ModelPackageGroupStatus = Literal[
    "Completed", "DeleteFailed", "Deleting", "Failed", "InProgress", "Pending"
]
ModelPackageSortBy = Literal["CreationTime", "Name"]
ModelPackageStatus = Literal["Completed", "Deleting", "Failed", "InProgress", "Pending"]
ModelPackageType = Literal["Both", "Unversioned", "Versioned"]
ModelSortKey = Literal["CreationTime", "Name"]
MonitoringExecutionSortKey = Literal["CreationTime", "ScheduledTime", "Status"]
MonitoringJobDefinitionSortKey = Literal["CreationTime", "Name"]
MonitoringProblemType = Literal["BinaryClassification", "MulticlassClassification", "Regression"]
MonitoringScheduleSortKey = Literal["CreationTime", "Name", "Status"]
MonitoringType = Literal["DataQuality", "ModelBias", "ModelExplainability", "ModelQuality"]
NotebookInstanceAcceleratorType = Literal[
    "ml.eia1.large",
    "ml.eia1.medium",
    "ml.eia1.xlarge",
    "ml.eia2.large",
    "ml.eia2.medium",
    "ml.eia2.xlarge",
]
NotebookInstanceDeletedWaiterName = Literal["notebook_instance_deleted"]
NotebookInstanceInServiceWaiterName = Literal["notebook_instance_in_service"]
NotebookInstanceLifecycleConfigSortKey = Literal["CreationTime", "LastModifiedTime", "Name"]
NotebookInstanceLifecycleConfigSortOrder = Literal["Ascending", "Descending"]
NotebookInstanceSortKey = Literal["CreationTime", "Name", "Status"]
NotebookInstanceSortOrder = Literal["Ascending", "Descending"]
NotebookInstanceStatus = Literal[
    "Deleting", "Failed", "InService", "Pending", "Stopped", "Stopping", "Updating"
]
NotebookInstanceStoppedWaiterName = Literal["notebook_instance_stopped"]
NotebookOutputOption = Literal["Allowed", "Disabled"]
ObjectiveStatus = Literal["Failed", "Pending", "Succeeded"]
OfflineStoreStatusValue = Literal["Active", "Blocked", "Disabled"]
Operator = Literal[
    "Contains",
    "Equals",
    "Exists",
    "GreaterThan",
    "GreaterThanOrEqualTo",
    "In",
    "LessThan",
    "LessThanOrEqualTo",
    "NotEquals",
    "NotExists",
]
OrderKey = Literal["Ascending", "Descending"]
ParameterType = Literal["Categorical", "Continuous", "FreeText", "Integer"]
PipelineExecutionStatus = Literal["Executing", "Failed", "Stopped", "Stopping", "Succeeded"]
PipelineStatus = Literal["Active"]
ProblemType = Literal["BinaryClassification", "MulticlassClassification", "Regression"]
ProcessingInstanceType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.r5.12xlarge",
    "ml.r5.16xlarge",
    "ml.r5.24xlarge",
    "ml.r5.2xlarge",
    "ml.r5.4xlarge",
    "ml.r5.8xlarge",
    "ml.r5.large",
    "ml.r5.xlarge",
    "ml.t3.2xlarge",
    "ml.t3.large",
    "ml.t3.medium",
    "ml.t3.xlarge",
]
ProcessingJobCompletedOrStoppedWaiterName = Literal["processing_job_completed_or_stopped"]
ProcessingJobStatus = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
ProcessingS3CompressionType = Literal["Gzip", "None"]
ProcessingS3DataDistributionType = Literal["FullyReplicated", "ShardedByS3Key"]
ProcessingS3DataType = Literal["ManifestFile", "S3Prefix"]
ProcessingS3InputMode = Literal["File", "Pipe"]
ProcessingS3UploadMode = Literal["Continuous", "EndOfJob"]
ProductionVariantAcceleratorType = Literal[
    "ml.eia1.large",
    "ml.eia1.medium",
    "ml.eia1.xlarge",
    "ml.eia2.large",
    "ml.eia2.medium",
    "ml.eia2.xlarge",
]
ProductionVariantInstanceType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.large",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.large",
    "ml.c5.xlarge",
    "ml.c5d.18xlarge",
    "ml.c5d.2xlarge",
    "ml.c5d.4xlarge",
    "ml.c5d.9xlarge",
    "ml.c5d.large",
    "ml.c5d.xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.xlarge",
    "ml.inf1.24xlarge",
    "ml.inf1.2xlarge",
    "ml.inf1.6xlarge",
    "ml.inf1.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.m5d.12xlarge",
    "ml.m5d.24xlarge",
    "ml.m5d.2xlarge",
    "ml.m5d.4xlarge",
    "ml.m5d.large",
    "ml.m5d.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.r5.12xlarge",
    "ml.r5.24xlarge",
    "ml.r5.2xlarge",
    "ml.r5.4xlarge",
    "ml.r5.large",
    "ml.r5.xlarge",
    "ml.r5d.12xlarge",
    "ml.r5d.24xlarge",
    "ml.r5d.2xlarge",
    "ml.r5d.4xlarge",
    "ml.r5d.large",
    "ml.r5d.xlarge",
    "ml.t2.2xlarge",
    "ml.t2.large",
    "ml.t2.medium",
    "ml.t2.xlarge",
]
ProfilingStatus = Literal["Disabled", "Enabled"]
ProjectSortBy = Literal["CreationTime", "Name"]
ProjectSortOrder = Literal["Ascending", "Descending"]
ProjectStatus = Literal[
    "CreateCompleted",
    "CreateFailed",
    "CreateInProgress",
    "DeleteCompleted",
    "DeleteFailed",
    "DeleteInProgress",
    "Pending",
]
RecordWrapper = Literal["None", "RecordIO"]
RedshiftResultCompressionType = Literal["BZIP2", "GZIP", "None", "SNAPPY", "ZSTD"]
RedshiftResultFormat = Literal["CSV", "PARQUET"]
RepositoryAccessMode = Literal["Platform", "Vpc"]
ResourceType = Literal[
    "Endpoint",
    "Experiment",
    "ExperimentTrial",
    "ExperimentTrialComponent",
    "FeatureGroup",
    "ModelPackage",
    "ModelPackageGroup",
    "Pipeline",
    "PipelineExecution",
    "TrainingJob",
]
RetentionType = Literal["Delete", "Retain"]
RootAccess = Literal["Disabled", "Enabled"]
RuleEvaluationStatus = Literal[
    "Error", "InProgress", "IssuesFound", "NoIssuesFound", "Stopped", "Stopping"
]
S3DataDistribution = Literal["FullyReplicated", "ShardedByS3Key"]
S3DataType = Literal["AugmentedManifestFile", "ManifestFile", "S3Prefix"]
SagemakerServicecatalogStatus = Literal["Disabled", "Enabled"]
ScheduleStatus = Literal["Failed", "Pending", "Scheduled", "Stopped"]
SearchPaginatorName = Literal["search"]
SearchSortOrder = Literal["Ascending", "Descending"]
SecondaryStatus = Literal[
    "Completed",
    "Downloading",
    "DownloadingTrainingImage",
    "Failed",
    "Interrupted",
    "LaunchingMLInstances",
    "MaxRuntimeExceeded",
    "MaxWaitTimeExceeded",
    "PreparingTrainingStack",
    "Restarting",
    "Starting",
    "Stopped",
    "Stopping",
    "Training",
    "Updating",
    "Uploading",
]
SortActionsBy = Literal["CreationTime", "Name"]
SortArtifactsBy = Literal["CreationTime"]
SortAssociationsBy = Literal[
    "CreationTime", "DestinationArn", "DestinationType", "SourceArn", "SourceType"
]
SortBy = Literal["CreationTime", "Name", "Status"]
SortContextsBy = Literal["CreationTime", "Name"]
SortExperimentsBy = Literal["CreationTime", "Name"]
SortOrder = Literal["Ascending", "Descending"]
SortPipelineExecutionsBy = Literal["CreationTime", "PipelineExecutionArn"]
SortPipelinesBy = Literal["CreationTime", "Name"]
SortTrialComponentsBy = Literal["CreationTime", "Name"]
SortTrialsBy = Literal["CreationTime", "Name"]
SplitType = Literal["Line", "None", "RecordIO", "TFRecord"]
StepStatus = Literal["Executing", "Failed", "Starting", "Stopped", "Stopping", "Succeeded"]
TargetDevice = Literal[
    "aisage",
    "amba_cv22",
    "coreml",
    "deeplens",
    "imx8qm",
    "jacinto_tda4vm",
    "jetson_nano",
    "jetson_tx1",
    "jetson_tx2",
    "jetson_xavier",
    "lambda",
    "ml_c4",
    "ml_c5",
    "ml_eia2",
    "ml_g4dn",
    "ml_inf1",
    "ml_m4",
    "ml_m5",
    "ml_p2",
    "ml_p3",
    "qcs603",
    "qcs605",
    "rasp3b",
    "rk3288",
    "rk3399",
    "sbe_c",
    "sitara_am57x",
    "x86_win32",
    "x86_win64",
]
TargetPlatformAccelerator = Literal["INTEL_GRAPHICS", "MALI", "NVIDIA"]
TargetPlatformArch = Literal["ARM64", "ARM_EABI", "ARM_EABIHF", "X86", "X86_64"]
TargetPlatformOs = Literal["ANDROID", "LINUX"]
TrafficRoutingConfigType = Literal["ALL_AT_ONCE", "CANARY"]
TrainingInputMode = Literal["File", "Pipe"]
TrainingInstanceType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.xlarge",
    "ml.c5n.18xlarge",
    "ml.c5n.2xlarge",
    "ml.c5n.4xlarge",
    "ml.c5n.9xlarge",
    "ml.c5n.xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
    "ml.p3dn.24xlarge",
    "ml.p4d.24xlarge",
]
TrainingJobCompletedOrStoppedWaiterName = Literal["training_job_completed_or_stopped"]
TrainingJobEarlyStoppingType = Literal["Auto", "Off"]
TrainingJobSortByOptions = Literal["CreationTime", "FinalObjectiveMetricValue", "Name", "Status"]
TrainingJobStatus = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
TransformInstanceType = Literal[
    "ml.c4.2xlarge",
    "ml.c4.4xlarge",
    "ml.c4.8xlarge",
    "ml.c4.xlarge",
    "ml.c5.18xlarge",
    "ml.c5.2xlarge",
    "ml.c5.4xlarge",
    "ml.c5.9xlarge",
    "ml.c5.xlarge",
    "ml.m4.10xlarge",
    "ml.m4.16xlarge",
    "ml.m4.2xlarge",
    "ml.m4.4xlarge",
    "ml.m4.xlarge",
    "ml.m5.12xlarge",
    "ml.m5.24xlarge",
    "ml.m5.2xlarge",
    "ml.m5.4xlarge",
    "ml.m5.large",
    "ml.m5.xlarge",
    "ml.p2.16xlarge",
    "ml.p2.8xlarge",
    "ml.p2.xlarge",
    "ml.p3.16xlarge",
    "ml.p3.2xlarge",
    "ml.p3.8xlarge",
]
TransformJobCompletedOrStoppedWaiterName = Literal["transform_job_completed_or_stopped"]
TransformJobStatus = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
TrialComponentPrimaryStatus = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
UserProfileSortKey = Literal["CreationTime", "LastModifiedTime"]
UserProfileStatus = Literal[
    "Delete_Failed", "Deleting", "Failed", "InService", "Pending", "Update_Failed", "Updating"
]
VariantPropertyType = Literal["DataCaptureConfig", "DesiredInstanceCount", "DesiredWeight"]
