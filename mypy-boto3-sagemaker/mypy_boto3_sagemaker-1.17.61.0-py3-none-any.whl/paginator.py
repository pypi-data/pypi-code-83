"""
Main interface for sagemaker service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_sagemaker import SageMakerClient
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
        ListImageVersionsPaginator,
        ListImagesPaginator,
        ListLabelingJobsPaginator,
        ListLabelingJobsForWorkteamPaginator,
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
        ListPipelineExecutionStepsPaginator,
        ListPipelineExecutionsPaginator,
        ListPipelineParametersForExecutionPaginator,
        ListPipelinesPaginator,
        ListProcessingJobsPaginator,
        ListSubscribedWorkteamsPaginator,
        ListTagsPaginator,
        ListTrainingJobsPaginator,
        ListTrainingJobsForHyperParameterTuningJobPaginator,
        ListTransformJobsPaginator,
        ListTrialComponentsPaginator,
        ListTrialsPaginator,
        ListUserProfilesPaginator,
        ListWorkforcesPaginator,
        ListWorkteamsPaginator,
        SearchPaginator,
    )

    client: SageMakerClient = boto3.client("sagemaker")

    list_actions_paginator: ListActionsPaginator = client.get_paginator("list_actions")
    list_algorithms_paginator: ListAlgorithmsPaginator = client.get_paginator("list_algorithms")
    list_app_image_configs_paginator: ListAppImageConfigsPaginator = client.get_paginator("list_app_image_configs")
    list_apps_paginator: ListAppsPaginator = client.get_paginator("list_apps")
    list_artifacts_paginator: ListArtifactsPaginator = client.get_paginator("list_artifacts")
    list_associations_paginator: ListAssociationsPaginator = client.get_paginator("list_associations")
    list_auto_ml_jobs_paginator: ListAutoMLJobsPaginator = client.get_paginator("list_auto_ml_jobs")
    list_candidates_for_auto_ml_job_paginator: ListCandidatesForAutoMLJobPaginator = client.get_paginator("list_candidates_for_auto_ml_job")
    list_code_repositories_paginator: ListCodeRepositoriesPaginator = client.get_paginator("list_code_repositories")
    list_compilation_jobs_paginator: ListCompilationJobsPaginator = client.get_paginator("list_compilation_jobs")
    list_contexts_paginator: ListContextsPaginator = client.get_paginator("list_contexts")
    list_data_quality_job_definitions_paginator: ListDataQualityJobDefinitionsPaginator = client.get_paginator("list_data_quality_job_definitions")
    list_device_fleets_paginator: ListDeviceFleetsPaginator = client.get_paginator("list_device_fleets")
    list_devices_paginator: ListDevicesPaginator = client.get_paginator("list_devices")
    list_domains_paginator: ListDomainsPaginator = client.get_paginator("list_domains")
    list_edge_packaging_jobs_paginator: ListEdgePackagingJobsPaginator = client.get_paginator("list_edge_packaging_jobs")
    list_endpoint_configs_paginator: ListEndpointConfigsPaginator = client.get_paginator("list_endpoint_configs")
    list_endpoints_paginator: ListEndpointsPaginator = client.get_paginator("list_endpoints")
    list_experiments_paginator: ListExperimentsPaginator = client.get_paginator("list_experiments")
    list_feature_groups_paginator: ListFeatureGroupsPaginator = client.get_paginator("list_feature_groups")
    list_flow_definitions_paginator: ListFlowDefinitionsPaginator = client.get_paginator("list_flow_definitions")
    list_human_task_uis_paginator: ListHumanTaskUisPaginator = client.get_paginator("list_human_task_uis")
    list_hyper_parameter_tuning_jobs_paginator: ListHyperParameterTuningJobsPaginator = client.get_paginator("list_hyper_parameter_tuning_jobs")
    list_image_versions_paginator: ListImageVersionsPaginator = client.get_paginator("list_image_versions")
    list_images_paginator: ListImagesPaginator = client.get_paginator("list_images")
    list_labeling_jobs_paginator: ListLabelingJobsPaginator = client.get_paginator("list_labeling_jobs")
    list_labeling_jobs_for_workteam_paginator: ListLabelingJobsForWorkteamPaginator = client.get_paginator("list_labeling_jobs_for_workteam")
    list_model_bias_job_definitions_paginator: ListModelBiasJobDefinitionsPaginator = client.get_paginator("list_model_bias_job_definitions")
    list_model_explainability_job_definitions_paginator: ListModelExplainabilityJobDefinitionsPaginator = client.get_paginator("list_model_explainability_job_definitions")
    list_model_package_groups_paginator: ListModelPackageGroupsPaginator = client.get_paginator("list_model_package_groups")
    list_model_packages_paginator: ListModelPackagesPaginator = client.get_paginator("list_model_packages")
    list_model_quality_job_definitions_paginator: ListModelQualityJobDefinitionsPaginator = client.get_paginator("list_model_quality_job_definitions")
    list_models_paginator: ListModelsPaginator = client.get_paginator("list_models")
    list_monitoring_executions_paginator: ListMonitoringExecutionsPaginator = client.get_paginator("list_monitoring_executions")
    list_monitoring_schedules_paginator: ListMonitoringSchedulesPaginator = client.get_paginator("list_monitoring_schedules")
    list_notebook_instance_lifecycle_configs_paginator: ListNotebookInstanceLifecycleConfigsPaginator = client.get_paginator("list_notebook_instance_lifecycle_configs")
    list_notebook_instances_paginator: ListNotebookInstancesPaginator = client.get_paginator("list_notebook_instances")
    list_pipeline_execution_steps_paginator: ListPipelineExecutionStepsPaginator = client.get_paginator("list_pipeline_execution_steps")
    list_pipeline_executions_paginator: ListPipelineExecutionsPaginator = client.get_paginator("list_pipeline_executions")
    list_pipeline_parameters_for_execution_paginator: ListPipelineParametersForExecutionPaginator = client.get_paginator("list_pipeline_parameters_for_execution")
    list_pipelines_paginator: ListPipelinesPaginator = client.get_paginator("list_pipelines")
    list_processing_jobs_paginator: ListProcessingJobsPaginator = client.get_paginator("list_processing_jobs")
    list_subscribed_workteams_paginator: ListSubscribedWorkteamsPaginator = client.get_paginator("list_subscribed_workteams")
    list_tags_paginator: ListTagsPaginator = client.get_paginator("list_tags")
    list_training_jobs_paginator: ListTrainingJobsPaginator = client.get_paginator("list_training_jobs")
    list_training_jobs_for_hyper_parameter_tuning_job_paginator: ListTrainingJobsForHyperParameterTuningJobPaginator = client.get_paginator("list_training_jobs_for_hyper_parameter_tuning_job")
    list_transform_jobs_paginator: ListTransformJobsPaginator = client.get_paginator("list_transform_jobs")
    list_trial_components_paginator: ListTrialComponentsPaginator = client.get_paginator("list_trial_components")
    list_trials_paginator: ListTrialsPaginator = client.get_paginator("list_trials")
    list_user_profiles_paginator: ListUserProfilesPaginator = client.get_paginator("list_user_profiles")
    list_workforces_paginator: ListWorkforcesPaginator = client.get_paginator("list_workforces")
    list_workteams_paginator: ListWorkteamsPaginator = client.get_paginator("list_workteams")
    search_paginator: SearchPaginator = client.get_paginator("search")
    ```
"""
from datetime import datetime
from typing import Any, Dict, Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_sagemaker.literals import (
    AlgorithmSortBy,
    AppImageConfigSortKey,
    AppSortKey,
    AssociationEdgeType,
    AutoMLJobStatus,
    AutoMLSortBy,
    AutoMLSortOrder,
    CandidateSortBy,
    CandidateStatus,
    CodeRepositorySortBy,
    CodeRepositorySortOrder,
    CompilationJobStatus,
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
    LabelingJobStatus,
    ListCompilationJobsSortBy,
    ListDeviceFleetsSortBy,
    ListEdgePackagingJobsSortBy,
    ListLabelingJobsForWorkteamSortByOptions,
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
    NotebookInstanceLifecycleConfigSortKey,
    NotebookInstanceLifecycleConfigSortOrder,
    NotebookInstanceSortKey,
    NotebookInstanceSortOrder,
    NotebookInstanceStatus,
    OfflineStoreStatusValue,
    OrderKey,
    ProcessingJobStatus,
    ResourceType,
    ScheduleStatus,
    SearchSortOrder,
    SortActionsBy,
    SortArtifactsBy,
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
from mypy_boto3_sagemaker.type_defs import (
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
    PaginatorConfigTypeDef,
    SearchResponseTypeDef,
)

__all__ = (
    "ListActionsPaginator",
    "ListAlgorithmsPaginator",
    "ListAppImageConfigsPaginator",
    "ListAppsPaginator",
    "ListArtifactsPaginator",
    "ListAssociationsPaginator",
    "ListAutoMLJobsPaginator",
    "ListCandidatesForAutoMLJobPaginator",
    "ListCodeRepositoriesPaginator",
    "ListCompilationJobsPaginator",
    "ListContextsPaginator",
    "ListDataQualityJobDefinitionsPaginator",
    "ListDeviceFleetsPaginator",
    "ListDevicesPaginator",
    "ListDomainsPaginator",
    "ListEdgePackagingJobsPaginator",
    "ListEndpointConfigsPaginator",
    "ListEndpointsPaginator",
    "ListExperimentsPaginator",
    "ListFeatureGroupsPaginator",
    "ListFlowDefinitionsPaginator",
    "ListHumanTaskUisPaginator",
    "ListHyperParameterTuningJobsPaginator",
    "ListImageVersionsPaginator",
    "ListImagesPaginator",
    "ListLabelingJobsPaginator",
    "ListLabelingJobsForWorkteamPaginator",
    "ListModelBiasJobDefinitionsPaginator",
    "ListModelExplainabilityJobDefinitionsPaginator",
    "ListModelPackageGroupsPaginator",
    "ListModelPackagesPaginator",
    "ListModelQualityJobDefinitionsPaginator",
    "ListModelsPaginator",
    "ListMonitoringExecutionsPaginator",
    "ListMonitoringSchedulesPaginator",
    "ListNotebookInstanceLifecycleConfigsPaginator",
    "ListNotebookInstancesPaginator",
    "ListPipelineExecutionStepsPaginator",
    "ListPipelineExecutionsPaginator",
    "ListPipelineParametersForExecutionPaginator",
    "ListPipelinesPaginator",
    "ListProcessingJobsPaginator",
    "ListSubscribedWorkteamsPaginator",
    "ListTagsPaginator",
    "ListTrainingJobsPaginator",
    "ListTrainingJobsForHyperParameterTuningJobPaginator",
    "ListTransformJobsPaginator",
    "ListTrialComponentsPaginator",
    "ListTrialsPaginator",
    "ListUserProfilesPaginator",
    "ListWorkforcesPaginator",
    "ListWorkteamsPaginator",
    "SearchPaginator",
)


class ListActionsPaginator(Boto3Paginator):
    """
    [Paginator.ListActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListActions)
    """

    def paginate(
        self,
        SourceUri: str = None,
        ActionType: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortActionsBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListActionsResponseTypeDef]:
        """
        [ListActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListActions.paginate)
        """


class ListAlgorithmsPaginator(Boto3Paginator):
    """
    [Paginator.ListAlgorithms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListAlgorithms)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: AlgorithmSortBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAlgorithmsOutputTypeDef]:
        """
        [ListAlgorithms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListAlgorithms.paginate)
        """


class ListAppImageConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListAppImageConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListAppImageConfigs)
    """

    def paginate(
        self,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        ModifiedTimeBefore: datetime = None,
        ModifiedTimeAfter: datetime = None,
        SortBy: AppImageConfigSortKey = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAppImageConfigsResponseTypeDef]:
        """
        [ListAppImageConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListAppImageConfigs.paginate)
        """


class ListAppsPaginator(Boto3Paginator):
    """
    [Paginator.ListApps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListApps)
    """

    def paginate(
        self,
        SortOrder: SortOrder = None,
        SortBy: AppSortKey = None,
        DomainIdEquals: str = None,
        UserProfileNameEquals: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAppsResponseTypeDef]:
        """
        [ListApps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListApps.paginate)
        """


class ListArtifactsPaginator(Boto3Paginator):
    """
    [Paginator.ListArtifacts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListArtifacts)
    """

    def paginate(
        self,
        SourceUri: str = None,
        ArtifactType: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortArtifactsBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListArtifactsResponseTypeDef]:
        """
        [ListArtifacts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListArtifacts.paginate)
        """


class ListAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListAssociations)
    """

    def paginate(
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
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAssociationsResponseTypeDef]:
        """
        [ListAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListAssociations.paginate)
        """


class ListAutoMLJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListAutoMLJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListAutoMLJobs)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: AutoMLJobStatus = None,
        SortOrder: AutoMLSortOrder = None,
        SortBy: AutoMLSortBy = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListAutoMLJobsResponseTypeDef]:
        """
        [ListAutoMLJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListAutoMLJobs.paginate)
        """


class ListCandidatesForAutoMLJobPaginator(Boto3Paginator):
    """
    [Paginator.ListCandidatesForAutoMLJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListCandidatesForAutoMLJob)
    """

    def paginate(
        self,
        AutoMLJobName: str,
        StatusEquals: CandidateStatus = None,
        CandidateNameEquals: str = None,
        SortOrder: AutoMLSortOrder = None,
        SortBy: CandidateSortBy = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCandidatesForAutoMLJobResponseTypeDef]:
        """
        [ListCandidatesForAutoMLJob.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListCandidatesForAutoMLJob.paginate)
        """


class ListCodeRepositoriesPaginator(Boto3Paginator):
    """
    [Paginator.ListCodeRepositories documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListCodeRepositories)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: CodeRepositorySortBy = None,
        SortOrder: CodeRepositorySortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCodeRepositoriesOutputTypeDef]:
        """
        [ListCodeRepositories.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListCodeRepositories.paginate)
        """


class ListCompilationJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListCompilationJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListCompilationJobs)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: CompilationJobStatus = None,
        SortBy: ListCompilationJobsSortBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListCompilationJobsResponseTypeDef]:
        """
        [ListCompilationJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListCompilationJobs.paginate)
        """


class ListContextsPaginator(Boto3Paginator):
    """
    [Paginator.ListContexts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListContexts)
    """

    def paginate(
        self,
        SourceUri: str = None,
        ContextType: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortContextsBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListContextsResponseTypeDef]:
        """
        [ListContexts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListContexts.paginate)
        """


class ListDataQualityJobDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListDataQualityJobDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListDataQualityJobDefinitions)
    """

    def paginate(
        self,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKey = None,
        SortOrder: SortOrder = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDataQualityJobDefinitionsResponseTypeDef]:
        """
        [ListDataQualityJobDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListDataQualityJobDefinitions.paginate)
        """


class ListDeviceFleetsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeviceFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListDeviceFleets)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: ListDeviceFleetsSortBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDeviceFleetsResponseTypeDef]:
        """
        [ListDeviceFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListDeviceFleets.paginate)
        """


class ListDevicesPaginator(Boto3Paginator):
    """
    [Paginator.ListDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListDevices)
    """

    def paginate(
        self,
        LatestHeartbeatAfter: datetime = None,
        ModelName: str = None,
        DeviceFleetName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListDevicesResponseTypeDef]:
        """
        [ListDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListDevices.paginate)
        """


class ListDomainsPaginator(Boto3Paginator):
    """
    [Paginator.ListDomains documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListDomains)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDomainsResponseTypeDef]:
        """
        [ListDomains.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListDomains.paginate)
        """


class ListEdgePackagingJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListEdgePackagingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListEdgePackagingJobs)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        ModelNameContains: str = None,
        StatusEquals: EdgePackagingJobStatus = None,
        SortBy: ListEdgePackagingJobsSortBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListEdgePackagingJobsResponseTypeDef]:
        """
        [ListEdgePackagingJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListEdgePackagingJobs.paginate)
        """


class ListEndpointConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListEndpointConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpointConfigs)
    """

    def paginate(
        self,
        SortBy: EndpointConfigSortKey = None,
        SortOrder: OrderKey = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListEndpointConfigsOutputTypeDef]:
        """
        [ListEndpointConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpointConfigs.paginate)
        """


class ListEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.ListEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpoints)
    """

    def paginate(
        self,
        SortBy: EndpointSortKey = None,
        SortOrder: OrderKey = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: EndpointStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListEndpointsOutputTypeDef]:
        """
        [ListEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListEndpoints.paginate)
        """


class ListExperimentsPaginator(Boto3Paginator):
    """
    [Paginator.ListExperiments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListExperiments)
    """

    def paginate(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortExperimentsBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListExperimentsResponseTypeDef]:
        """
        [ListExperiments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListExperiments.paginate)
        """


class ListFeatureGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListFeatureGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListFeatureGroups)
    """

    def paginate(
        self,
        NameContains: str = None,
        FeatureGroupStatusEquals: FeatureGroupStatus = None,
        OfflineStoreStatusEquals: OfflineStoreStatusValue = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: FeatureGroupSortOrder = None,
        SortBy: FeatureGroupSortBy = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListFeatureGroupsResponseTypeDef]:
        """
        [ListFeatureGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListFeatureGroups.paginate)
        """


class ListFlowDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListFlowDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListFlowDefinitions)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListFlowDefinitionsResponseTypeDef]:
        """
        [ListFlowDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListFlowDefinitions.paginate)
        """


class ListHumanTaskUisPaginator(Boto3Paginator):
    """
    [Paginator.ListHumanTaskUis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListHumanTaskUis)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListHumanTaskUisResponseTypeDef]:
        """
        [ListHumanTaskUis.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListHumanTaskUis.paginate)
        """


class ListHyperParameterTuningJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListHyperParameterTuningJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListHyperParameterTuningJobs)
    """

    def paginate(
        self,
        SortBy: HyperParameterTuningJobSortByOptions = None,
        SortOrder: SortOrder = None,
        NameContains: str = None,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        StatusEquals: HyperParameterTuningJobStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListHyperParameterTuningJobsResponseTypeDef]:
        """
        [ListHyperParameterTuningJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListHyperParameterTuningJobs.paginate)
        """


class ListImageVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListImageVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListImageVersions)
    """

    def paginate(
        self,
        ImageName: str,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        SortBy: ImageVersionSortBy = None,
        SortOrder: ImageVersionSortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListImageVersionsResponseTypeDef]:
        """
        [ListImageVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListImageVersions.paginate)
        """


class ListImagesPaginator(Boto3Paginator):
    """
    [Paginator.ListImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListImages)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: ImageSortBy = None,
        SortOrder: ImageSortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListImagesResponseTypeDef]:
        """
        [ListImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListImages.paginate)
        """


class ListLabelingJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListLabelingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobs)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: SortBy = None,
        SortOrder: SortOrder = None,
        StatusEquals: LabelingJobStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListLabelingJobsResponseTypeDef]:
        """
        [ListLabelingJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobs.paginate)
        """


class ListLabelingJobsForWorkteamPaginator(Boto3Paginator):
    """
    [Paginator.ListLabelingJobsForWorkteam documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobsForWorkteam)
    """

    def paginate(
        self,
        WorkteamArn: str,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        JobReferenceCodeContains: str = None,
        SortBy: ListLabelingJobsForWorkteamSortByOptions = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListLabelingJobsForWorkteamResponseTypeDef]:
        """
        [ListLabelingJobsForWorkteam.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListLabelingJobsForWorkteam.paginate)
        """


class ListModelBiasJobDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListModelBiasJobDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListModelBiasJobDefinitions)
    """

    def paginate(
        self,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKey = None,
        SortOrder: SortOrder = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListModelBiasJobDefinitionsResponseTypeDef]:
        """
        [ListModelBiasJobDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListModelBiasJobDefinitions.paginate)
        """


class ListModelExplainabilityJobDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListModelExplainabilityJobDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListModelExplainabilityJobDefinitions)
    """

    def paginate(
        self,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKey = None,
        SortOrder: SortOrder = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListModelExplainabilityJobDefinitionsResponseTypeDef]:
        """
        [ListModelExplainabilityJobDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListModelExplainabilityJobDefinitions.paginate)
        """


class ListModelPackageGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListModelPackageGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackageGroups)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        NameContains: str = None,
        SortBy: ModelPackageGroupSortBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListModelPackageGroupsOutputTypeDef]:
        """
        [ListModelPackageGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackageGroups.paginate)
        """


class ListModelPackagesPaginator(Boto3Paginator):
    """
    [Paginator.ListModelPackages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackages)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        NameContains: str = None,
        ModelApprovalStatus: ModelApprovalStatus = None,
        ModelPackageGroupName: str = None,
        ModelPackageType: ModelPackageType = None,
        SortBy: ModelPackageSortBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListModelPackagesOutputTypeDef]:
        """
        [ListModelPackages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListModelPackages.paginate)
        """


class ListModelQualityJobDefinitionsPaginator(Boto3Paginator):
    """
    [Paginator.ListModelQualityJobDefinitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListModelQualityJobDefinitions)
    """

    def paginate(
        self,
        EndpointName: str = None,
        SortBy: MonitoringJobDefinitionSortKey = None,
        SortOrder: SortOrder = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListModelQualityJobDefinitionsResponseTypeDef]:
        """
        [ListModelQualityJobDefinitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListModelQualityJobDefinitions.paginate)
        """


class ListModelsPaginator(Boto3Paginator):
    """
    [Paginator.ListModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListModels)
    """

    def paginate(
        self,
        SortBy: ModelSortKey = None,
        SortOrder: OrderKey = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListModelsOutputTypeDef]:
        """
        [ListModels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListModels.paginate)
        """


class ListMonitoringExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListMonitoringExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringExecutions)
    """

    def paginate(
        self,
        MonitoringScheduleName: str = None,
        EndpointName: str = None,
        SortBy: MonitoringExecutionSortKey = None,
        SortOrder: SortOrder = None,
        ScheduledTimeBefore: datetime = None,
        ScheduledTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: ExecutionStatus = None,
        MonitoringJobDefinitionName: str = None,
        MonitoringTypeEquals: MonitoringType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListMonitoringExecutionsResponseTypeDef]:
        """
        [ListMonitoringExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringExecutions.paginate)
        """


class ListMonitoringSchedulesPaginator(Boto3Paginator):
    """
    [Paginator.ListMonitoringSchedules documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringSchedules)
    """

    def paginate(
        self,
        EndpointName: str = None,
        SortBy: MonitoringScheduleSortKey = None,
        SortOrder: SortOrder = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        StatusEquals: ScheduleStatus = None,
        MonitoringJobDefinitionName: str = None,
        MonitoringTypeEquals: MonitoringType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListMonitoringSchedulesResponseTypeDef]:
        """
        [ListMonitoringSchedules.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListMonitoringSchedules.paginate)
        """


class ListNotebookInstanceLifecycleConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListNotebookInstanceLifecycleConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstanceLifecycleConfigs)
    """

    def paginate(
        self,
        SortBy: NotebookInstanceLifecycleConfigSortKey = None,
        SortOrder: NotebookInstanceLifecycleConfigSortOrder = None,
        NameContains: str = None,
        CreationTimeBefore: datetime = None,
        CreationTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListNotebookInstanceLifecycleConfigsOutputTypeDef]:
        """
        [ListNotebookInstanceLifecycleConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstanceLifecycleConfigs.paginate)
        """


class ListNotebookInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListNotebookInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstances)
    """

    def paginate(
        self,
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
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListNotebookInstancesOutputTypeDef]:
        """
        [ListNotebookInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListNotebookInstances.paginate)
        """


class ListPipelineExecutionStepsPaginator(Boto3Paginator):
    """
    [Paginator.ListPipelineExecutionSteps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutionSteps)
    """

    def paginate(
        self,
        PipelineExecutionArn: str = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPipelineExecutionStepsResponseTypeDef]:
        """
        [ListPipelineExecutionSteps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutionSteps.paginate)
        """


class ListPipelineExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListPipelineExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutions)
    """

    def paginate(
        self,
        PipelineName: str,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortPipelineExecutionsBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPipelineExecutionsResponseTypeDef]:
        """
        [ListPipelineExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineExecutions.paginate)
        """


class ListPipelineParametersForExecutionPaginator(Boto3Paginator):
    """
    [Paginator.ListPipelineParametersForExecution documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineParametersForExecution)
    """

    def paginate(
        self, PipelineExecutionArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListPipelineParametersForExecutionResponseTypeDef]:
        """
        [ListPipelineParametersForExecution.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelineParametersForExecution.paginate)
        """


class ListPipelinesPaginator(Boto3Paginator):
    """
    [Paginator.ListPipelines documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelines)
    """

    def paginate(
        self,
        PipelineNamePrefix: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortPipelinesBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPipelinesResponseTypeDef]:
        """
        [ListPipelines.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListPipelines.paginate)
        """


class ListProcessingJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListProcessingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListProcessingJobs)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: ProcessingJobStatus = None,
        SortBy: SortBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListProcessingJobsResponseTypeDef]:
        """
        [ListProcessingJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListProcessingJobs.paginate)
        """


class ListSubscribedWorkteamsPaginator(Boto3Paginator):
    """
    [Paginator.ListSubscribedWorkteams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListSubscribedWorkteams)
    """

    def paginate(
        self, NameContains: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSubscribedWorkteamsResponseTypeDef]:
        """
        [ListSubscribedWorkteams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListSubscribedWorkteams.paginate)
        """


class ListTagsPaginator(Boto3Paginator):
    """
    [Paginator.ListTags documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListTags)
    """

    def paginate(
        self, ResourceArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListTagsOutputTypeDef]:
        """
        [ListTags.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListTags.paginate)
        """


class ListTrainingJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListTrainingJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobs)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: TrainingJobStatus = None,
        SortBy: SortBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTrainingJobsResponseTypeDef]:
        """
        [ListTrainingJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobs.paginate)
        """


class ListTrainingJobsForHyperParameterTuningJobPaginator(Boto3Paginator):
    """
    [Paginator.ListTrainingJobsForHyperParameterTuningJob documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobsForHyperParameterTuningJob)
    """

    def paginate(
        self,
        HyperParameterTuningJobName: str,
        StatusEquals: TrainingJobStatus = None,
        SortBy: TrainingJobSortByOptions = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTrainingJobsForHyperParameterTuningJobResponseTypeDef]:
        """
        [ListTrainingJobsForHyperParameterTuningJob.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListTrainingJobsForHyperParameterTuningJob.paginate)
        """


class ListTransformJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListTransformJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListTransformJobs)
    """

    def paginate(
        self,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        LastModifiedTimeAfter: datetime = None,
        LastModifiedTimeBefore: datetime = None,
        NameContains: str = None,
        StatusEquals: TransformJobStatus = None,
        SortBy: SortBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTransformJobsResponseTypeDef]:
        """
        [ListTransformJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListTransformJobs.paginate)
        """


class ListTrialComponentsPaginator(Boto3Paginator):
    """
    [Paginator.ListTrialComponents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListTrialComponents)
    """

    def paginate(
        self,
        ExperimentName: str = None,
        TrialName: str = None,
        SourceArn: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortTrialComponentsBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTrialComponentsResponseTypeDef]:
        """
        [ListTrialComponents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListTrialComponents.paginate)
        """


class ListTrialsPaginator(Boto3Paginator):
    """
    [Paginator.ListTrials documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListTrials)
    """

    def paginate(
        self,
        ExperimentName: str = None,
        TrialComponentName: str = None,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        SortBy: SortTrialsBy = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListTrialsResponseTypeDef]:
        """
        [ListTrials.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListTrials.paginate)
        """


class ListUserProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListUserProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListUserProfiles)
    """

    def paginate(
        self,
        SortOrder: SortOrder = None,
        SortBy: UserProfileSortKey = None,
        DomainIdEquals: str = None,
        UserProfileNameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListUserProfilesResponseTypeDef]:
        """
        [ListUserProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListUserProfiles.paginate)
        """


class ListWorkforcesPaginator(Boto3Paginator):
    """
    [Paginator.ListWorkforces documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkforces)
    """

    def paginate(
        self,
        SortBy: ListWorkforcesSortByOptions = None,
        SortOrder: SortOrder = None,
        NameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListWorkforcesResponseTypeDef]:
        """
        [ListWorkforces.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkforces.paginate)
        """


class ListWorkteamsPaginator(Boto3Paginator):
    """
    [Paginator.ListWorkteams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkteams)
    """

    def paginate(
        self,
        SortBy: ListWorkteamsSortByOptions = None,
        SortOrder: SortOrder = None,
        NameContains: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListWorkteamsResponseTypeDef]:
        """
        [ListWorkteams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.ListWorkteams.paginate)
        """


class SearchPaginator(Boto3Paginator):
    """
    [Paginator.Search documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.Search)
    """

    def paginate(
        self,
        Resource: ResourceType,
        SearchExpression: Dict[str, Any] = None,
        SortBy: str = None,
        SortOrder: SearchSortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[SearchResponseTypeDef]:
        """
        [Search.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker.html#SageMaker.Paginator.Search.paginate)
        """
