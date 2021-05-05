"""
Type annotations for codebuild service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codebuild import CodeBuildClient

    client: CodeBuildClient = boto3.client("codebuild")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_codebuild.literals import (
    AuthType,
    ComputeType,
    EnvironmentType,
    ImagePullCredentialsType,
    ProjectSortByType,
    ReportCodeCoverageSortByType,
    ReportGroupSortByType,
    ReportGroupTrendFieldType,
    ReportType,
    RetryBuildBatchType,
    ServerType,
    SharedResourceSortByType,
    SortOrderType,
    SourceType,
    WebhookBuildType,
)
from mypy_boto3_codebuild.paginator import (
    DescribeCodeCoveragesPaginator,
    DescribeTestCasesPaginator,
    ListBuildBatchesForProjectPaginator,
    ListBuildBatchesPaginator,
    ListBuildsForProjectPaginator,
    ListBuildsPaginator,
    ListProjectsPaginator,
    ListReportGroupsPaginator,
    ListReportsForReportGroupPaginator,
    ListReportsPaginator,
    ListSharedProjectsPaginator,
    ListSharedReportGroupsPaginator,
)
from mypy_boto3_codebuild.type_defs import (
    BatchDeleteBuildsOutputTypeDef,
    BatchGetBuildBatchesOutputTypeDef,
    BatchGetBuildsOutputTypeDef,
    BatchGetProjectsOutputTypeDef,
    BatchGetReportGroupsOutputTypeDef,
    BatchGetReportsOutputTypeDef,
    BuildBatchFilterTypeDef,
    BuildStatusConfigTypeDef,
    CreateProjectOutputTypeDef,
    CreateReportGroupOutputTypeDef,
    CreateWebhookOutputTypeDef,
    DeleteBuildBatchOutputTypeDef,
    DeleteSourceCredentialsOutputTypeDef,
    DescribeCodeCoveragesOutputTypeDef,
    DescribeTestCasesOutputTypeDef,
    EnvironmentVariableTypeDef,
    GetReportGroupTrendOutputTypeDef,
    GetResourcePolicyOutputTypeDef,
    GitSubmodulesConfigTypeDef,
    ImportSourceCredentialsOutputTypeDef,
    ListBuildBatchesForProjectOutputTypeDef,
    ListBuildBatchesOutputTypeDef,
    ListBuildsForProjectOutputTypeDef,
    ListBuildsOutputTypeDef,
    ListCuratedEnvironmentImagesOutputTypeDef,
    ListProjectsOutputTypeDef,
    ListReportGroupsOutputTypeDef,
    ListReportsForReportGroupOutputTypeDef,
    ListReportsOutputTypeDef,
    ListSharedProjectsOutputTypeDef,
    ListSharedReportGroupsOutputTypeDef,
    ListSourceCredentialsOutputTypeDef,
    LogsConfigTypeDef,
    ProjectArtifactsTypeDef,
    ProjectBuildBatchConfigTypeDef,
    ProjectCacheTypeDef,
    ProjectEnvironmentTypeDef,
    ProjectFileSystemLocationTypeDef,
    ProjectSourceTypeDef,
    ProjectSourceVersionTypeDef,
    PutResourcePolicyOutputTypeDef,
    RegistryCredentialTypeDef,
    ReportExportConfigTypeDef,
    ReportFilterTypeDef,
    RetryBuildBatchOutputTypeDef,
    RetryBuildOutputTypeDef,
    SourceAuthTypeDef,
    StartBuildBatchOutputTypeDef,
    StartBuildOutputTypeDef,
    StopBuildBatchOutputTypeDef,
    StopBuildOutputTypeDef,
    TagTypeDef,
    TestCaseFilterTypeDef,
    UpdateProjectOutputTypeDef,
    UpdateReportGroupOutputTypeDef,
    UpdateWebhookOutputTypeDef,
    VpcConfigTypeDef,
    WebhookFilterTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CodeBuildClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccountLimitExceededException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    OAuthProviderException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class CodeBuildClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def batch_delete_builds(self, ids: List[str]) -> BatchDeleteBuildsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.batch_delete_builds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#batch-delete-builds)
        """

    def batch_get_build_batches(self, ids: List[str]) -> BatchGetBuildBatchesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.batch_get_build_batches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#batch-get-build-batches)
        """

    def batch_get_builds(self, ids: List[str]) -> BatchGetBuildsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.batch_get_builds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#batch-get-builds)
        """

    def batch_get_projects(self, names: List[str]) -> BatchGetProjectsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.batch_get_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#batch-get-projects)
        """

    def batch_get_report_groups(
        self, reportGroupArns: List[str]
    ) -> BatchGetReportGroupsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.batch_get_report_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#batch-get-report-groups)
        """

    def batch_get_reports(self, reportArns: List[str]) -> BatchGetReportsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.batch_get_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#batch-get-reports)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#can-paginate)
        """

    def create_project(
        self,
        name: str,
        source: "ProjectSourceTypeDef",
        artifacts: "ProjectArtifactsTypeDef",
        environment: "ProjectEnvironmentTypeDef",
        serviceRole: str,
        description: str = None,
        secondarySources: List["ProjectSourceTypeDef"] = None,
        sourceVersion: str = None,
        secondarySourceVersions: List["ProjectSourceVersionTypeDef"] = None,
        secondaryArtifacts: List["ProjectArtifactsTypeDef"] = None,
        cache: "ProjectCacheTypeDef" = None,
        timeoutInMinutes: int = None,
        queuedTimeoutInMinutes: int = None,
        encryptionKey: str = None,
        tags: List["TagTypeDef"] = None,
        vpcConfig: "VpcConfigTypeDef" = None,
        badgeEnabled: bool = None,
        logsConfig: "LogsConfigTypeDef" = None,
        fileSystemLocations: List["ProjectFileSystemLocationTypeDef"] = None,
        buildBatchConfig: "ProjectBuildBatchConfigTypeDef" = None,
        concurrentBuildLimit: int = None,
    ) -> CreateProjectOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.create_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#create-project)
        """

    def create_report_group(
        self,
        name: str,
        type: ReportType,
        exportConfig: "ReportExportConfigTypeDef",
        tags: List["TagTypeDef"] = None,
    ) -> CreateReportGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.create_report_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#create-report-group)
        """

    def create_webhook(
        self,
        projectName: str,
        branchFilter: str = None,
        filterGroups: List[List["WebhookFilterTypeDef"]] = None,
        buildType: WebhookBuildType = None,
    ) -> CreateWebhookOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.create_webhook)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#create-webhook)
        """

    def delete_build_batch(self, id: str) -> DeleteBuildBatchOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.delete_build_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#delete-build-batch)
        """

    def delete_project(self, name: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.delete_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#delete-project)
        """

    def delete_report(self, arn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.delete_report)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#delete-report)
        """

    def delete_report_group(self, arn: str, deleteReports: bool = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.delete_report_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#delete-report-group)
        """

    def delete_resource_policy(self, resourceArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#delete-resource-policy)
        """

    def delete_source_credentials(self, arn: str) -> DeleteSourceCredentialsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.delete_source_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#delete-source-credentials)
        """

    def delete_webhook(self, projectName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.delete_webhook)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#delete-webhook)
        """

    def describe_code_coverages(
        self,
        reportArn: str,
        nextToken: str = None,
        maxResults: int = None,
        sortOrder: SortOrderType = None,
        sortBy: ReportCodeCoverageSortByType = None,
        minLineCoveragePercentage: float = None,
        maxLineCoveragePercentage: float = None,
    ) -> DescribeCodeCoveragesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.describe_code_coverages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#describe-code-coverages)
        """

    def describe_test_cases(
        self,
        reportArn: str,
        nextToken: str = None,
        maxResults: int = None,
        filter: TestCaseFilterTypeDef = None,
    ) -> DescribeTestCasesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.describe_test_cases)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#describe-test-cases)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#generate-presigned-url)
        """

    def get_report_group_trend(
        self, reportGroupArn: str, trendField: ReportGroupTrendFieldType, numOfReports: int = None
    ) -> GetReportGroupTrendOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.get_report_group_trend)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#get-report-group-trend)
        """

    def get_resource_policy(self, resourceArn: str) -> GetResourcePolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.get_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#get-resource-policy)
        """

    def import_source_credentials(
        self,
        token: str,
        serverType: ServerType,
        authType: AuthType,
        username: str = None,
        shouldOverwrite: bool = None,
    ) -> ImportSourceCredentialsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.import_source_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#import-source-credentials)
        """

    def invalidate_project_cache(self, projectName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.invalidate_project_cache)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#invalidate-project-cache)
        """

    def list_build_batches(
        self,
        filter: BuildBatchFilterTypeDef = None,
        maxResults: int = None,
        sortOrder: SortOrderType = None,
        nextToken: str = None,
    ) -> ListBuildBatchesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.list_build_batches)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list-build-batches)
        """

    def list_build_batches_for_project(
        self,
        projectName: str = None,
        filter: BuildBatchFilterTypeDef = None,
        maxResults: int = None,
        sortOrder: SortOrderType = None,
        nextToken: str = None,
    ) -> ListBuildBatchesForProjectOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.list_build_batches_for_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list-build-batches-for-project)
        """

    def list_builds(
        self, sortOrder: SortOrderType = None, nextToken: str = None
    ) -> ListBuildsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.list_builds)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list-builds)
        """

    def list_builds_for_project(
        self, projectName: str, sortOrder: SortOrderType = None, nextToken: str = None
    ) -> ListBuildsForProjectOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.list_builds_for_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list-builds-for-project)
        """

    def list_curated_environment_images(self) -> ListCuratedEnvironmentImagesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.list_curated_environment_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list-curated-environment-images)
        """

    def list_projects(
        self,
        sortBy: ProjectSortByType = None,
        sortOrder: SortOrderType = None,
        nextToken: str = None,
    ) -> ListProjectsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.list_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list-projects)
        """

    def list_report_groups(
        self,
        sortOrder: SortOrderType = None,
        sortBy: ReportGroupSortByType = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListReportGroupsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.list_report_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list-report-groups)
        """

    def list_reports(
        self,
        sortOrder: SortOrderType = None,
        nextToken: str = None,
        maxResults: int = None,
        filter: ReportFilterTypeDef = None,
    ) -> ListReportsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.list_reports)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list-reports)
        """

    def list_reports_for_report_group(
        self,
        reportGroupArn: str,
        nextToken: str = None,
        sortOrder: SortOrderType = None,
        maxResults: int = None,
        filter: ReportFilterTypeDef = None,
    ) -> ListReportsForReportGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.list_reports_for_report_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list-reports-for-report-group)
        """

    def list_shared_projects(
        self,
        sortBy: SharedResourceSortByType = None,
        sortOrder: SortOrderType = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListSharedProjectsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.list_shared_projects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list-shared-projects)
        """

    def list_shared_report_groups(
        self,
        sortOrder: SortOrderType = None,
        sortBy: SharedResourceSortByType = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ListSharedReportGroupsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.list_shared_report_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list-shared-report-groups)
        """

    def list_source_credentials(self) -> ListSourceCredentialsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.list_source_credentials)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#list-source-credentials)
        """

    def put_resource_policy(self, policy: str, resourceArn: str) -> PutResourcePolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#put-resource-policy)
        """

    def retry_build(self, id: str = None, idempotencyToken: str = None) -> RetryBuildOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.retry_build)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#retry-build)
        """

    def retry_build_batch(
        self, id: str = None, idempotencyToken: str = None, retryType: RetryBuildBatchType = None
    ) -> RetryBuildBatchOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.retry_build_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#retry-build-batch)
        """

    def start_build(
        self,
        projectName: str,
        secondarySourcesOverride: List["ProjectSourceTypeDef"] = None,
        secondarySourcesVersionOverride: List["ProjectSourceVersionTypeDef"] = None,
        sourceVersion: str = None,
        artifactsOverride: "ProjectArtifactsTypeDef" = None,
        secondaryArtifactsOverride: List["ProjectArtifactsTypeDef"] = None,
        environmentVariablesOverride: List["EnvironmentVariableTypeDef"] = None,
        sourceTypeOverride: SourceType = None,
        sourceLocationOverride: str = None,
        sourceAuthOverride: "SourceAuthTypeDef" = None,
        gitCloneDepthOverride: int = None,
        gitSubmodulesConfigOverride: "GitSubmodulesConfigTypeDef" = None,
        buildspecOverride: str = None,
        insecureSslOverride: bool = None,
        reportBuildStatusOverride: bool = None,
        buildStatusConfigOverride: "BuildStatusConfigTypeDef" = None,
        environmentTypeOverride: EnvironmentType = None,
        imageOverride: str = None,
        computeTypeOverride: ComputeType = None,
        certificateOverride: str = None,
        cacheOverride: "ProjectCacheTypeDef" = None,
        serviceRoleOverride: str = None,
        privilegedModeOverride: bool = None,
        timeoutInMinutesOverride: int = None,
        queuedTimeoutInMinutesOverride: int = None,
        encryptionKeyOverride: str = None,
        idempotencyToken: str = None,
        logsConfigOverride: "LogsConfigTypeDef" = None,
        registryCredentialOverride: "RegistryCredentialTypeDef" = None,
        imagePullCredentialsTypeOverride: ImagePullCredentialsType = None,
        debugSessionEnabled: bool = None,
    ) -> StartBuildOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.start_build)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#start-build)
        """

    def start_build_batch(
        self,
        projectName: str,
        secondarySourcesOverride: List["ProjectSourceTypeDef"] = None,
        secondarySourcesVersionOverride: List["ProjectSourceVersionTypeDef"] = None,
        sourceVersion: str = None,
        artifactsOverride: "ProjectArtifactsTypeDef" = None,
        secondaryArtifactsOverride: List["ProjectArtifactsTypeDef"] = None,
        environmentVariablesOverride: List["EnvironmentVariableTypeDef"] = None,
        sourceTypeOverride: SourceType = None,
        sourceLocationOverride: str = None,
        sourceAuthOverride: "SourceAuthTypeDef" = None,
        gitCloneDepthOverride: int = None,
        gitSubmodulesConfigOverride: "GitSubmodulesConfigTypeDef" = None,
        buildspecOverride: str = None,
        insecureSslOverride: bool = None,
        reportBuildBatchStatusOverride: bool = None,
        environmentTypeOverride: EnvironmentType = None,
        imageOverride: str = None,
        computeTypeOverride: ComputeType = None,
        certificateOverride: str = None,
        cacheOverride: "ProjectCacheTypeDef" = None,
        serviceRoleOverride: str = None,
        privilegedModeOverride: bool = None,
        buildTimeoutInMinutesOverride: int = None,
        queuedTimeoutInMinutesOverride: int = None,
        encryptionKeyOverride: str = None,
        idempotencyToken: str = None,
        logsConfigOverride: "LogsConfigTypeDef" = None,
        registryCredentialOverride: "RegistryCredentialTypeDef" = None,
        imagePullCredentialsTypeOverride: ImagePullCredentialsType = None,
        buildBatchConfigOverride: "ProjectBuildBatchConfigTypeDef" = None,
        debugSessionEnabled: bool = None,
    ) -> StartBuildBatchOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.start_build_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#start-build-batch)
        """

    def stop_build(self, id: str) -> StopBuildOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.stop_build)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#stop-build)
        """

    def stop_build_batch(self, id: str) -> StopBuildBatchOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.stop_build_batch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#stop-build-batch)
        """

    def update_project(
        self,
        name: str,
        description: str = None,
        source: "ProjectSourceTypeDef" = None,
        secondarySources: List["ProjectSourceTypeDef"] = None,
        sourceVersion: str = None,
        secondarySourceVersions: List["ProjectSourceVersionTypeDef"] = None,
        artifacts: "ProjectArtifactsTypeDef" = None,
        secondaryArtifacts: List["ProjectArtifactsTypeDef"] = None,
        cache: "ProjectCacheTypeDef" = None,
        environment: "ProjectEnvironmentTypeDef" = None,
        serviceRole: str = None,
        timeoutInMinutes: int = None,
        queuedTimeoutInMinutes: int = None,
        encryptionKey: str = None,
        tags: List["TagTypeDef"] = None,
        vpcConfig: "VpcConfigTypeDef" = None,
        badgeEnabled: bool = None,
        logsConfig: "LogsConfigTypeDef" = None,
        fileSystemLocations: List["ProjectFileSystemLocationTypeDef"] = None,
        buildBatchConfig: "ProjectBuildBatchConfigTypeDef" = None,
        concurrentBuildLimit: int = None,
    ) -> UpdateProjectOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.update_project)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#update-project)
        """

    def update_report_group(
        self,
        arn: str,
        exportConfig: "ReportExportConfigTypeDef" = None,
        tags: List["TagTypeDef"] = None,
    ) -> UpdateReportGroupOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.update_report_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#update-report-group)
        """

    def update_webhook(
        self,
        projectName: str,
        branchFilter: str = None,
        rotateSecret: bool = None,
        filterGroups: List[List["WebhookFilterTypeDef"]] = None,
        buildType: WebhookBuildType = None,
    ) -> UpdateWebhookOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Client.update_webhook)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/client.html#update-webhook)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_code_coverages"]
    ) -> DescribeCodeCoveragesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Paginator.DescribeCodeCoverages)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#describecodecoveragespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_test_cases"]
    ) -> DescribeTestCasesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Paginator.DescribeTestCases)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#describetestcasespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_build_batches"]
    ) -> ListBuildBatchesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildBatches)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildbatchespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_build_batches_for_project"]
    ) -> ListBuildBatchesForProjectPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildBatchesForProject)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildbatchesforprojectpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_builds"]) -> ListBuildsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Paginator.ListBuilds)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_builds_for_project"]
    ) -> ListBuildsForProjectPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Paginator.ListBuildsForProject)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listbuildsforprojectpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_projects"]) -> ListProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Paginator.ListProjects)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listprojectspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_report_groups"]
    ) -> ListReportGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Paginator.ListReportGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listreportgroupspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_reports"]) -> ListReportsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Paginator.ListReports)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listreportspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_reports_for_report_group"]
    ) -> ListReportsForReportGroupPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Paginator.ListReportsForReportGroup)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listreportsforreportgrouppaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_shared_projects"]
    ) -> ListSharedProjectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Paginator.ListSharedProjects)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listsharedprojectspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_shared_report_groups"]
    ) -> ListSharedReportGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/codebuild.html#CodeBuild.Paginator.ListSharedReportGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/paginators.html#listsharedreportgroupspaginator)
        """
