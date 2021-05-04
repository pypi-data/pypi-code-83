"""
Type annotations for codebuild service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/literals.html)

Usage::

    ```python
    from mypy_boto3_codebuild.literals import ArtifactNamespace

    data: ArtifactNamespace = "BUILD_ID"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ArtifactNamespace",
    "ArtifactPackaging",
    "ArtifactsType",
    "AuthType",
    "BucketOwnerAccess",
    "BuildBatchPhaseType",
    "BuildPhaseType",
    "CacheMode",
    "CacheType",
    "ComputeType",
    "CredentialProviderType",
    "DescribeCodeCoveragesPaginatorName",
    "DescribeTestCasesPaginatorName",
    "EnvironmentType",
    "EnvironmentVariableType",
    "FileSystemType",
    "ImagePullCredentialsType",
    "LanguageType",
    "ListBuildBatchesForProjectPaginatorName",
    "ListBuildBatchesPaginatorName",
    "ListBuildsForProjectPaginatorName",
    "ListBuildsPaginatorName",
    "ListProjectsPaginatorName",
    "ListReportGroupsPaginatorName",
    "ListReportsForReportGroupPaginatorName",
    "ListReportsPaginatorName",
    "ListSharedProjectsPaginatorName",
    "ListSharedReportGroupsPaginatorName",
    "LogsConfigStatusType",
    "PlatformType",
    "ProjectSortByType",
    "ReportCodeCoverageSortByType",
    "ReportExportConfigType",
    "ReportGroupSortByType",
    "ReportGroupStatusType",
    "ReportGroupTrendFieldType",
    "ReportPackagingType",
    "ReportStatusType",
    "ReportType",
    "RetryBuildBatchType",
    "ServerType",
    "SharedResourceSortByType",
    "SortOrderType",
    "SourceAuthType",
    "SourceType",
    "StatusType",
    "WebhookBuildType",
    "WebhookFilterType",
)


ArtifactNamespace = Literal["BUILD_ID", "NONE"]
ArtifactPackaging = Literal["NONE", "ZIP"]
ArtifactsType = Literal["CODEPIPELINE", "NO_ARTIFACTS", "S3"]
AuthType = Literal["BASIC_AUTH", "OAUTH", "PERSONAL_ACCESS_TOKEN"]
BucketOwnerAccess = Literal["FULL", "NONE", "READ_ONLY"]
BuildBatchPhaseType = Literal[
    "COMBINE_ARTIFACTS",
    "DOWNLOAD_BATCHSPEC",
    "FAILED",
    "IN_PROGRESS",
    "STOPPED",
    "SUBMITTED",
    "SUCCEEDED",
]
BuildPhaseType = Literal[
    "BUILD",
    "COMPLETED",
    "DOWNLOAD_SOURCE",
    "FINALIZING",
    "INSTALL",
    "POST_BUILD",
    "PRE_BUILD",
    "PROVISIONING",
    "QUEUED",
    "SUBMITTED",
    "UPLOAD_ARTIFACTS",
]
CacheMode = Literal["LOCAL_CUSTOM_CACHE", "LOCAL_DOCKER_LAYER_CACHE", "LOCAL_SOURCE_CACHE"]
CacheType = Literal["LOCAL", "NO_CACHE", "S3"]
ComputeType = Literal[
    "BUILD_GENERAL1_2XLARGE",
    "BUILD_GENERAL1_LARGE",
    "BUILD_GENERAL1_MEDIUM",
    "BUILD_GENERAL1_SMALL",
]
CredentialProviderType = Literal["SECRETS_MANAGER"]
DescribeCodeCoveragesPaginatorName = Literal["describe_code_coverages"]
DescribeTestCasesPaginatorName = Literal["describe_test_cases"]
EnvironmentType = Literal[
    "ARM_CONTAINER",
    "LINUX_CONTAINER",
    "LINUX_GPU_CONTAINER",
    "WINDOWS_CONTAINER",
    "WINDOWS_SERVER_2019_CONTAINER",
]
EnvironmentVariableType = Literal["PARAMETER_STORE", "PLAINTEXT", "SECRETS_MANAGER"]
FileSystemType = Literal["EFS"]
ImagePullCredentialsType = Literal["CODEBUILD", "SERVICE_ROLE"]
LanguageType = Literal[
    "ANDROID", "BASE", "DOCKER", "DOTNET", "GOLANG", "JAVA", "NODE_JS", "PHP", "PYTHON", "RUBY"
]
ListBuildBatchesForProjectPaginatorName = Literal["list_build_batches_for_project"]
ListBuildBatchesPaginatorName = Literal["list_build_batches"]
ListBuildsForProjectPaginatorName = Literal["list_builds_for_project"]
ListBuildsPaginatorName = Literal["list_builds"]
ListProjectsPaginatorName = Literal["list_projects"]
ListReportGroupsPaginatorName = Literal["list_report_groups"]
ListReportsForReportGroupPaginatorName = Literal["list_reports_for_report_group"]
ListReportsPaginatorName = Literal["list_reports"]
ListSharedProjectsPaginatorName = Literal["list_shared_projects"]
ListSharedReportGroupsPaginatorName = Literal["list_shared_report_groups"]
LogsConfigStatusType = Literal["DISABLED", "ENABLED"]
PlatformType = Literal["AMAZON_LINUX", "DEBIAN", "UBUNTU", "WINDOWS_SERVER"]
ProjectSortByType = Literal["CREATED_TIME", "LAST_MODIFIED_TIME", "NAME"]
ReportCodeCoverageSortByType = Literal["FILE_PATH", "LINE_COVERAGE_PERCENTAGE"]
ReportExportConfigType = Literal["NO_EXPORT", "S3"]
ReportGroupSortByType = Literal["CREATED_TIME", "LAST_MODIFIED_TIME", "NAME"]
ReportGroupStatusType = Literal["ACTIVE", "DELETING"]
ReportGroupTrendFieldType = Literal[
    "BRANCHES_COVERED",
    "BRANCHES_MISSED",
    "BRANCH_COVERAGE",
    "DURATION",
    "LINES_COVERED",
    "LINES_MISSED",
    "LINE_COVERAGE",
    "PASS_RATE",
    "TOTAL",
]
ReportPackagingType = Literal["NONE", "ZIP"]
ReportStatusType = Literal["DELETING", "FAILED", "GENERATING", "INCOMPLETE", "SUCCEEDED"]
ReportType = Literal["CODE_COVERAGE", "TEST"]
RetryBuildBatchType = Literal["RETRY_ALL_BUILDS", "RETRY_FAILED_BUILDS"]
ServerType = Literal["BITBUCKET", "GITHUB", "GITHUB_ENTERPRISE"]
SharedResourceSortByType = Literal["ARN", "MODIFIED_TIME"]
SortOrderType = Literal["ASCENDING", "DESCENDING"]
SourceAuthType = Literal["OAUTH"]
SourceType = Literal[
    "BITBUCKET", "CODECOMMIT", "CODEPIPELINE", "GITHUB", "GITHUB_ENTERPRISE", "NO_SOURCE", "S3"
]
StatusType = Literal["FAILED", "FAULT", "IN_PROGRESS", "STOPPED", "SUCCEEDED", "TIMED_OUT"]
WebhookBuildType = Literal["BUILD", "BUILD_BATCH"]
WebhookFilterType = Literal[
    "ACTOR_ACCOUNT_ID", "BASE_REF", "COMMIT_MESSAGE", "EVENT", "FILE_PATH", "HEAD_REF"
]
