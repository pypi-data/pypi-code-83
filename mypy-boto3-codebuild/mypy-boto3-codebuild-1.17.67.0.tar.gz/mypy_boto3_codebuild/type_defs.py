"""
Type annotations for codebuild service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codebuild/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codebuild.type_defs import BatchDeleteBuildsOutputTypeDef

    data: BatchDeleteBuildsOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_codebuild.literals import (
    ArtifactNamespace,
    ArtifactPackaging,
    ArtifactsType,
    AuthType,
    BucketOwnerAccess,
    BuildBatchPhaseType,
    BuildPhaseType,
    CacheMode,
    CacheType,
    ComputeType,
    EnvironmentType,
    EnvironmentVariableType,
    ImagePullCredentialsType,
    LanguageType,
    LogsConfigStatusType,
    PlatformType,
    ReportExportConfigType,
    ReportGroupStatusType,
    ReportPackagingType,
    ReportStatusType,
    ReportType,
    ServerType,
    SourceType,
    StatusType,
    WebhookBuildType,
    WebhookFilterType,
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
    "BatchDeleteBuildsOutputTypeDef",
    "BatchGetBuildBatchesOutputTypeDef",
    "BatchGetBuildsOutputTypeDef",
    "BatchGetProjectsOutputTypeDef",
    "BatchGetReportGroupsOutputTypeDef",
    "BatchGetReportsOutputTypeDef",
    "BatchRestrictionsTypeDef",
    "BuildArtifactsTypeDef",
    "BuildBatchFilterTypeDef",
    "BuildBatchPhaseTypeDef",
    "BuildBatchTypeDef",
    "BuildGroupTypeDef",
    "BuildNotDeletedTypeDef",
    "BuildPhaseTypeDef",
    "BuildStatusConfigTypeDef",
    "BuildSummaryTypeDef",
    "BuildTypeDef",
    "CloudWatchLogsConfigTypeDef",
    "CodeCoverageReportSummaryTypeDef",
    "CodeCoverageTypeDef",
    "CreateProjectOutputTypeDef",
    "CreateReportGroupOutputTypeDef",
    "CreateWebhookOutputTypeDef",
    "DebugSessionTypeDef",
    "DeleteBuildBatchOutputTypeDef",
    "DeleteSourceCredentialsOutputTypeDef",
    "DescribeCodeCoveragesOutputTypeDef",
    "DescribeTestCasesOutputTypeDef",
    "EnvironmentImageTypeDef",
    "EnvironmentLanguageTypeDef",
    "EnvironmentPlatformTypeDef",
    "EnvironmentVariableTypeDef",
    "ExportedEnvironmentVariableTypeDef",
    "GetReportGroupTrendOutputTypeDef",
    "GetResourcePolicyOutputTypeDef",
    "GitSubmodulesConfigTypeDef",
    "ImportSourceCredentialsOutputTypeDef",
    "ListBuildBatchesForProjectOutputTypeDef",
    "ListBuildBatchesOutputTypeDef",
    "ListBuildsForProjectOutputTypeDef",
    "ListBuildsOutputTypeDef",
    "ListCuratedEnvironmentImagesOutputTypeDef",
    "ListProjectsOutputTypeDef",
    "ListReportGroupsOutputTypeDef",
    "ListReportsForReportGroupOutputTypeDef",
    "ListReportsOutputTypeDef",
    "ListSharedProjectsOutputTypeDef",
    "ListSharedReportGroupsOutputTypeDef",
    "ListSourceCredentialsOutputTypeDef",
    "LogsConfigTypeDef",
    "LogsLocationTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PhaseContextTypeDef",
    "ProjectArtifactsTypeDef",
    "ProjectBadgeTypeDef",
    "ProjectBuildBatchConfigTypeDef",
    "ProjectCacheTypeDef",
    "ProjectEnvironmentTypeDef",
    "ProjectFileSystemLocationTypeDef",
    "ProjectSourceTypeDef",
    "ProjectSourceVersionTypeDef",
    "ProjectTypeDef",
    "PutResourcePolicyOutputTypeDef",
    "RegistryCredentialTypeDef",
    "ReportExportConfigTypeDef",
    "ReportFilterTypeDef",
    "ReportGroupTrendStatsTypeDef",
    "ReportGroupTypeDef",
    "ReportTypeDef",
    "ReportWithRawDataTypeDef",
    "ResolvedArtifactTypeDef",
    "ResponseMetadata",
    "RetryBuildBatchOutputTypeDef",
    "RetryBuildOutputTypeDef",
    "S3LogsConfigTypeDef",
    "S3ReportExportConfigTypeDef",
    "SourceAuthTypeDef",
    "SourceCredentialsInfoTypeDef",
    "StartBuildBatchOutputTypeDef",
    "StartBuildOutputTypeDef",
    "StopBuildBatchOutputTypeDef",
    "StopBuildOutputTypeDef",
    "TagTypeDef",
    "TestCaseFilterTypeDef",
    "TestCaseTypeDef",
    "TestReportSummaryTypeDef",
    "UpdateProjectOutputTypeDef",
    "UpdateReportGroupOutputTypeDef",
    "UpdateWebhookOutputTypeDef",
    "VpcConfigTypeDef",
    "WebhookFilterTypeDef",
    "WebhookTypeDef",
)


class BatchDeleteBuildsOutputTypeDef(TypedDict):
    buildsDeleted: List[str]
    buildsNotDeleted: List["BuildNotDeletedTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class BatchGetBuildBatchesOutputTypeDef(TypedDict):
    buildBatches: List["BuildBatchTypeDef"]
    buildBatchesNotFound: List[str]
    ResponseMetadata: "ResponseMetadata"


class BatchGetBuildsOutputTypeDef(TypedDict):
    builds: List["BuildTypeDef"]
    buildsNotFound: List[str]
    ResponseMetadata: "ResponseMetadata"


class BatchGetProjectsOutputTypeDef(TypedDict):
    projects: List["ProjectTypeDef"]
    projectsNotFound: List[str]
    ResponseMetadata: "ResponseMetadata"


class BatchGetReportGroupsOutputTypeDef(TypedDict):
    reportGroups: List["ReportGroupTypeDef"]
    reportGroupsNotFound: List[str]
    ResponseMetadata: "ResponseMetadata"


class BatchGetReportsOutputTypeDef(TypedDict):
    reports: List["ReportTypeDef"]
    reportsNotFound: List[str]
    ResponseMetadata: "ResponseMetadata"


class BatchRestrictionsTypeDef(TypedDict, total=False):
    maximumBuildsAllowed: int
    computeTypesAllowed: List[str]


class BuildArtifactsTypeDef(TypedDict, total=False):
    location: str
    sha256sum: str
    md5sum: str
    overrideArtifactName: bool
    encryptionDisabled: bool
    artifactIdentifier: str
    bucketOwnerAccess: BucketOwnerAccess


class BuildBatchFilterTypeDef(TypedDict, total=False):
    status: StatusType


class BuildBatchPhaseTypeDef(TypedDict, total=False):
    phaseType: BuildBatchPhaseType
    phaseStatus: StatusType
    startTime: datetime
    endTime: datetime
    durationInSeconds: int
    contexts: List["PhaseContextTypeDef"]


BuildBatchTypeDef = TypedDict(
    "BuildBatchTypeDef",
    {
        "id": str,
        "arn": str,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildBatchStatus": StatusType,
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List["BuildBatchPhaseTypeDef"],
        "source": "ProjectSourceTypeDef",
        "secondarySources": List["ProjectSourceTypeDef"],
        "secondarySourceVersions": List["ProjectSourceVersionTypeDef"],
        "artifacts": "BuildArtifactsTypeDef",
        "secondaryArtifacts": List["BuildArtifactsTypeDef"],
        "cache": "ProjectCacheTypeDef",
        "environment": "ProjectEnvironmentTypeDef",
        "serviceRole": str,
        "logConfig": "LogsConfigTypeDef",
        "buildTimeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "complete": bool,
        "initiator": str,
        "vpcConfig": "VpcConfigTypeDef",
        "encryptionKey": str,
        "buildBatchNumber": int,
        "fileSystemLocations": List["ProjectFileSystemLocationTypeDef"],
        "buildBatchConfig": "ProjectBuildBatchConfigTypeDef",
        "buildGroups": List["BuildGroupTypeDef"],
        "debugSessionEnabled": bool,
    },
    total=False,
)


class BuildGroupTypeDef(TypedDict, total=False):
    identifier: str
    dependsOn: List[str]
    ignoreFailure: bool
    currentBuildSummary: "BuildSummaryTypeDef"
    priorBuildSummaryList: List["BuildSummaryTypeDef"]


BuildNotDeletedTypeDef = TypedDict(
    "BuildNotDeletedTypeDef", {"id": str, "statusCode": str}, total=False
)


class BuildPhaseTypeDef(TypedDict, total=False):
    phaseType: BuildPhaseType
    phaseStatus: StatusType
    startTime: datetime
    endTime: datetime
    durationInSeconds: int
    contexts: List["PhaseContextTypeDef"]


class BuildStatusConfigTypeDef(TypedDict, total=False):
    context: str
    targetUrl: str


class BuildSummaryTypeDef(TypedDict, total=False):
    arn: str
    requestedOn: datetime
    buildStatus: StatusType
    primaryArtifact: "ResolvedArtifactTypeDef"
    secondaryArtifacts: List["ResolvedArtifactTypeDef"]


BuildTypeDef = TypedDict(
    "BuildTypeDef",
    {
        "id": str,
        "arn": str,
        "buildNumber": int,
        "startTime": datetime,
        "endTime": datetime,
        "currentPhase": str,
        "buildStatus": StatusType,
        "sourceVersion": str,
        "resolvedSourceVersion": str,
        "projectName": str,
        "phases": List["BuildPhaseTypeDef"],
        "source": "ProjectSourceTypeDef",
        "secondarySources": List["ProjectSourceTypeDef"],
        "secondarySourceVersions": List["ProjectSourceVersionTypeDef"],
        "artifacts": "BuildArtifactsTypeDef",
        "secondaryArtifacts": List["BuildArtifactsTypeDef"],
        "cache": "ProjectCacheTypeDef",
        "environment": "ProjectEnvironmentTypeDef",
        "serviceRole": str,
        "logs": "LogsLocationTypeDef",
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "buildComplete": bool,
        "initiator": str,
        "vpcConfig": "VpcConfigTypeDef",
        "networkInterface": "NetworkInterfaceTypeDef",
        "encryptionKey": str,
        "exportedEnvironmentVariables": List["ExportedEnvironmentVariableTypeDef"],
        "reportArns": List[str],
        "fileSystemLocations": List["ProjectFileSystemLocationTypeDef"],
        "debugSession": "DebugSessionTypeDef",
        "buildBatchArn": str,
    },
    total=False,
)


class _RequiredCloudWatchLogsConfigTypeDef(TypedDict):
    status: LogsConfigStatusType


class CloudWatchLogsConfigTypeDef(_RequiredCloudWatchLogsConfigTypeDef, total=False):
    groupName: str
    streamName: str


class CodeCoverageReportSummaryTypeDef(TypedDict, total=False):
    lineCoveragePercentage: float
    linesCovered: int
    linesMissed: int
    branchCoveragePercentage: float
    branchesCovered: int
    branchesMissed: int


CodeCoverageTypeDef = TypedDict(
    "CodeCoverageTypeDef",
    {
        "id": str,
        "reportARN": str,
        "filePath": str,
        "lineCoveragePercentage": float,
        "linesCovered": int,
        "linesMissed": int,
        "branchCoveragePercentage": float,
        "branchesCovered": int,
        "branchesMissed": int,
        "expired": datetime,
    },
    total=False,
)


class CreateProjectOutputTypeDef(TypedDict):
    project: "ProjectTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateReportGroupOutputTypeDef(TypedDict):
    reportGroup: "ReportGroupTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateWebhookOutputTypeDef(TypedDict):
    webhook: "WebhookTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DebugSessionTypeDef(TypedDict, total=False):
    sessionEnabled: bool
    sessionTarget: str


class DeleteBuildBatchOutputTypeDef(TypedDict):
    statusCode: str
    buildsDeleted: List[str]
    buildsNotDeleted: List["BuildNotDeletedTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DeleteSourceCredentialsOutputTypeDef(TypedDict):
    arn: str
    ResponseMetadata: "ResponseMetadata"


class DescribeCodeCoveragesOutputTypeDef(TypedDict):
    nextToken: str
    codeCoverages: List["CodeCoverageTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeTestCasesOutputTypeDef(TypedDict):
    nextToken: str
    testCases: List["TestCaseTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class EnvironmentImageTypeDef(TypedDict, total=False):
    name: str
    description: str
    versions: List[str]


class EnvironmentLanguageTypeDef(TypedDict, total=False):
    language: LanguageType
    images: List["EnvironmentImageTypeDef"]


class EnvironmentPlatformTypeDef(TypedDict, total=False):
    platform: PlatformType
    languages: List["EnvironmentLanguageTypeDef"]


_RequiredEnvironmentVariableTypeDef = TypedDict(
    "_RequiredEnvironmentVariableTypeDef", {"name": str, "value": str}
)
_OptionalEnvironmentVariableTypeDef = TypedDict(
    "_OptionalEnvironmentVariableTypeDef", {"type": EnvironmentVariableType}, total=False
)


class EnvironmentVariableTypeDef(
    _RequiredEnvironmentVariableTypeDef, _OptionalEnvironmentVariableTypeDef
):
    pass


class ExportedEnvironmentVariableTypeDef(TypedDict, total=False):
    name: str
    value: str


class GetReportGroupTrendOutputTypeDef(TypedDict):
    stats: "ReportGroupTrendStatsTypeDef"
    rawData: List["ReportWithRawDataTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetResourcePolicyOutputTypeDef(TypedDict):
    policy: str
    ResponseMetadata: "ResponseMetadata"


class GitSubmodulesConfigTypeDef(TypedDict):
    fetchSubmodules: bool


class ImportSourceCredentialsOutputTypeDef(TypedDict):
    arn: str
    ResponseMetadata: "ResponseMetadata"


class ListBuildBatchesForProjectOutputTypeDef(TypedDict):
    ids: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListBuildBatchesOutputTypeDef(TypedDict):
    ids: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListBuildsForProjectOutputTypeDef(TypedDict):
    ids: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListBuildsOutputTypeDef(TypedDict):
    ids: List[str]
    nextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListCuratedEnvironmentImagesOutputTypeDef(TypedDict):
    platforms: List["EnvironmentPlatformTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListProjectsOutputTypeDef(TypedDict):
    nextToken: str
    projects: List[str]
    ResponseMetadata: "ResponseMetadata"


class ListReportGroupsOutputTypeDef(TypedDict):
    nextToken: str
    reportGroups: List[str]
    ResponseMetadata: "ResponseMetadata"


class ListReportsForReportGroupOutputTypeDef(TypedDict):
    nextToken: str
    reports: List[str]
    ResponseMetadata: "ResponseMetadata"


class ListReportsOutputTypeDef(TypedDict):
    nextToken: str
    reports: List[str]
    ResponseMetadata: "ResponseMetadata"


class ListSharedProjectsOutputTypeDef(TypedDict):
    nextToken: str
    projects: List[str]
    ResponseMetadata: "ResponseMetadata"


class ListSharedReportGroupsOutputTypeDef(TypedDict):
    nextToken: str
    reportGroups: List[str]
    ResponseMetadata: "ResponseMetadata"


class ListSourceCredentialsOutputTypeDef(TypedDict):
    sourceCredentialsInfos: List["SourceCredentialsInfoTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class LogsConfigTypeDef(TypedDict, total=False):
    cloudWatchLogs: "CloudWatchLogsConfigTypeDef"
    s3Logs: "S3LogsConfigTypeDef"


class LogsLocationTypeDef(TypedDict, total=False):
    groupName: str
    streamName: str
    deepLink: str
    s3DeepLink: str
    cloudWatchLogsArn: str
    s3LogsArn: str
    cloudWatchLogs: "CloudWatchLogsConfigTypeDef"
    s3Logs: "S3LogsConfigTypeDef"


class NetworkInterfaceTypeDef(TypedDict, total=False):
    subnetId: str
    networkInterfaceId: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PhaseContextTypeDef(TypedDict, total=False):
    statusCode: str
    message: str


_RequiredProjectArtifactsTypeDef = TypedDict(
    "_RequiredProjectArtifactsTypeDef", {"type": ArtifactsType}
)
_OptionalProjectArtifactsTypeDef = TypedDict(
    "_OptionalProjectArtifactsTypeDef",
    {
        "location": str,
        "path": str,
        "namespaceType": ArtifactNamespace,
        "name": str,
        "packaging": ArtifactPackaging,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
        "bucketOwnerAccess": BucketOwnerAccess,
    },
    total=False,
)


class ProjectArtifactsTypeDef(_RequiredProjectArtifactsTypeDef, _OptionalProjectArtifactsTypeDef):
    pass


class ProjectBadgeTypeDef(TypedDict, total=False):
    badgeEnabled: bool
    badgeRequestUrl: str


class ProjectBuildBatchConfigTypeDef(TypedDict, total=False):
    serviceRole: str
    combineArtifacts: bool
    restrictions: "BatchRestrictionsTypeDef"
    timeoutInMins: int


_RequiredProjectCacheTypeDef = TypedDict("_RequiredProjectCacheTypeDef", {"type": CacheType})
_OptionalProjectCacheTypeDef = TypedDict(
    "_OptionalProjectCacheTypeDef", {"location": str, "modes": List[CacheMode]}, total=False
)


class ProjectCacheTypeDef(_RequiredProjectCacheTypeDef, _OptionalProjectCacheTypeDef):
    pass


_RequiredProjectEnvironmentTypeDef = TypedDict(
    "_RequiredProjectEnvironmentTypeDef",
    {"type": EnvironmentType, "image": str, "computeType": ComputeType},
)
_OptionalProjectEnvironmentTypeDef = TypedDict(
    "_OptionalProjectEnvironmentTypeDef",
    {
        "environmentVariables": List["EnvironmentVariableTypeDef"],
        "privilegedMode": bool,
        "certificate": str,
        "registryCredential": "RegistryCredentialTypeDef",
        "imagePullCredentialsType": ImagePullCredentialsType,
    },
    total=False,
)


class ProjectEnvironmentTypeDef(
    _RequiredProjectEnvironmentTypeDef, _OptionalProjectEnvironmentTypeDef
):
    pass


ProjectFileSystemLocationTypeDef = TypedDict(
    "ProjectFileSystemLocationTypeDef",
    {
        "type": Literal["EFS"],
        "location": str,
        "mountPoint": str,
        "identifier": str,
        "mountOptions": str,
    },
    total=False,
)

_RequiredProjectSourceTypeDef = TypedDict("_RequiredProjectSourceTypeDef", {"type": SourceType})
_OptionalProjectSourceTypeDef = TypedDict(
    "_OptionalProjectSourceTypeDef",
    {
        "location": str,
        "gitCloneDepth": int,
        "gitSubmodulesConfig": "GitSubmodulesConfigTypeDef",
        "buildspec": str,
        "auth": "SourceAuthTypeDef",
        "reportBuildStatus": bool,
        "buildStatusConfig": "BuildStatusConfigTypeDef",
        "insecureSsl": bool,
        "sourceIdentifier": str,
    },
    total=False,
)


class ProjectSourceTypeDef(_RequiredProjectSourceTypeDef, _OptionalProjectSourceTypeDef):
    pass


class ProjectSourceVersionTypeDef(TypedDict):
    sourceIdentifier: str
    sourceVersion: str


class ProjectTypeDef(TypedDict, total=False):
    name: str
    arn: str
    description: str
    source: "ProjectSourceTypeDef"
    secondarySources: List["ProjectSourceTypeDef"]
    sourceVersion: str
    secondarySourceVersions: List["ProjectSourceVersionTypeDef"]
    artifacts: "ProjectArtifactsTypeDef"
    secondaryArtifacts: List["ProjectArtifactsTypeDef"]
    cache: "ProjectCacheTypeDef"
    environment: "ProjectEnvironmentTypeDef"
    serviceRole: str
    timeoutInMinutes: int
    queuedTimeoutInMinutes: int
    encryptionKey: str
    tags: List["TagTypeDef"]
    created: datetime
    lastModified: datetime
    webhook: "WebhookTypeDef"
    vpcConfig: "VpcConfigTypeDef"
    badge: "ProjectBadgeTypeDef"
    logsConfig: "LogsConfigTypeDef"
    fileSystemLocations: List["ProjectFileSystemLocationTypeDef"]
    buildBatchConfig: "ProjectBuildBatchConfigTypeDef"
    concurrentBuildLimit: int


class PutResourcePolicyOutputTypeDef(TypedDict):
    resourceArn: str
    ResponseMetadata: "ResponseMetadata"


class RegistryCredentialTypeDef(TypedDict):
    credential: str
    credentialProvider: Literal["SECRETS_MANAGER"]


class ReportExportConfigTypeDef(TypedDict, total=False):
    exportConfigType: ReportExportConfigType
    s3Destination: "S3ReportExportConfigTypeDef"


class ReportFilterTypeDef(TypedDict, total=False):
    status: ReportStatusType


ReportGroupTrendStatsTypeDef = TypedDict(
    "ReportGroupTrendStatsTypeDef", {"average": str, "max": str, "min": str}, total=False
)

ReportGroupTypeDef = TypedDict(
    "ReportGroupTypeDef",
    {
        "arn": str,
        "name": str,
        "type": ReportType,
        "exportConfig": "ReportExportConfigTypeDef",
        "created": datetime,
        "lastModified": datetime,
        "tags": List["TagTypeDef"],
        "status": ReportGroupStatusType,
    },
    total=False,
)

ReportTypeDef = TypedDict(
    "ReportTypeDef",
    {
        "arn": str,
        "type": ReportType,
        "name": str,
        "reportGroupArn": str,
        "executionId": str,
        "status": ReportStatusType,
        "created": datetime,
        "expired": datetime,
        "exportConfig": "ReportExportConfigTypeDef",
        "truncated": bool,
        "testSummary": "TestReportSummaryTypeDef",
        "codeCoverageSummary": "CodeCoverageReportSummaryTypeDef",
    },
    total=False,
)


class ReportWithRawDataTypeDef(TypedDict, total=False):
    reportArn: str
    data: str


ResolvedArtifactTypeDef = TypedDict(
    "ResolvedArtifactTypeDef",
    {"type": ArtifactsType, "location": str, "identifier": str},
    total=False,
)


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RetryBuildBatchOutputTypeDef(TypedDict):
    buildBatch: "BuildBatchTypeDef"
    ResponseMetadata: "ResponseMetadata"


class RetryBuildOutputTypeDef(TypedDict):
    build: "BuildTypeDef"
    ResponseMetadata: "ResponseMetadata"


class _RequiredS3LogsConfigTypeDef(TypedDict):
    status: LogsConfigStatusType


class S3LogsConfigTypeDef(_RequiredS3LogsConfigTypeDef, total=False):
    location: str
    encryptionDisabled: bool
    bucketOwnerAccess: BucketOwnerAccess


class S3ReportExportConfigTypeDef(TypedDict, total=False):
    bucket: str
    bucketOwner: str
    path: str
    packaging: ReportPackagingType
    encryptionKey: str
    encryptionDisabled: bool


_RequiredSourceAuthTypeDef = TypedDict("_RequiredSourceAuthTypeDef", {"type": Literal["OAUTH"]})
_OptionalSourceAuthTypeDef = TypedDict("_OptionalSourceAuthTypeDef", {"resource": str}, total=False)


class SourceAuthTypeDef(_RequiredSourceAuthTypeDef, _OptionalSourceAuthTypeDef):
    pass


class SourceCredentialsInfoTypeDef(TypedDict, total=False):
    arn: str
    serverType: ServerType
    authType: AuthType


class StartBuildBatchOutputTypeDef(TypedDict):
    buildBatch: "BuildBatchTypeDef"
    ResponseMetadata: "ResponseMetadata"


class StartBuildOutputTypeDef(TypedDict):
    build: "BuildTypeDef"
    ResponseMetadata: "ResponseMetadata"


class StopBuildBatchOutputTypeDef(TypedDict):
    buildBatch: "BuildBatchTypeDef"
    ResponseMetadata: "ResponseMetadata"


class StopBuildOutputTypeDef(TypedDict):
    build: "BuildTypeDef"
    ResponseMetadata: "ResponseMetadata"


class TagTypeDef(TypedDict, total=False):
    key: str
    value: str


class TestCaseFilterTypeDef(TypedDict, total=False):
    status: str
    keyword: str


class TestCaseTypeDef(TypedDict, total=False):
    reportArn: str
    testRawDataPath: str
    prefix: str
    name: str
    status: str
    durationInNanoSeconds: int
    message: str
    expired: datetime


class TestReportSummaryTypeDef(TypedDict):
    total: int
    statusCounts: Dict[str, int]
    durationInNanoSeconds: int


class UpdateProjectOutputTypeDef(TypedDict):
    project: "ProjectTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateReportGroupOutputTypeDef(TypedDict):
    reportGroup: "ReportGroupTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateWebhookOutputTypeDef(TypedDict):
    webhook: "WebhookTypeDef"
    ResponseMetadata: "ResponseMetadata"


class VpcConfigTypeDef(TypedDict, total=False):
    vpcId: str
    subnets: List[str]
    securityGroupIds: List[str]


_RequiredWebhookFilterTypeDef = TypedDict(
    "_RequiredWebhookFilterTypeDef", {"type": WebhookFilterType, "pattern": str}
)
_OptionalWebhookFilterTypeDef = TypedDict(
    "_OptionalWebhookFilterTypeDef", {"excludeMatchedPattern": bool}, total=False
)


class WebhookFilterTypeDef(_RequiredWebhookFilterTypeDef, _OptionalWebhookFilterTypeDef):
    pass


class WebhookTypeDef(TypedDict, total=False):
    url: str
    payloadUrl: str
    secret: str
    branchFilter: str
    filterGroups: List[List["WebhookFilterTypeDef"]]
    buildType: WebhookBuildType
    lastModifiedSecret: datetime
