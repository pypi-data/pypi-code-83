"""
Main interface for codebuild service type definitions.

Usage::

    ```python
    from mypy_boto3_codebuild.type_defs import BatchRestrictionsTypeDef

    data: BatchRestrictionsTypeDef = {...}
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
    CredentialProviderType,
    EnvironmentType,
    EnvironmentVariableType,
    FileSystemType,
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
    SourceAuthType,
    SourceType,
    StatusType,
    WebhookBuildType,
    WebhookFilterType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchRestrictionsTypeDef",
    "BuildArtifactsTypeDef",
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
    "DebugSessionTypeDef",
    "EnvironmentImageTypeDef",
    "EnvironmentLanguageTypeDef",
    "EnvironmentPlatformTypeDef",
    "EnvironmentVariableTypeDef",
    "ExportedEnvironmentVariableTypeDef",
    "GitSubmodulesConfigTypeDef",
    "LogsConfigTypeDef",
    "LogsLocationTypeDef",
    "NetworkInterfaceTypeDef",
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
    "RegistryCredentialTypeDef",
    "ReportExportConfigTypeDef",
    "ReportGroupTrendStatsTypeDef",
    "ReportGroupTypeDef",
    "ReportTypeDef",
    "ReportWithRawDataTypeDef",
    "ResolvedArtifactTypeDef",
    "ResponseMetadata",
    "S3LogsConfigTypeDef",
    "S3ReportExportConfigTypeDef",
    "SourceAuthTypeDef",
    "SourceCredentialsInfoTypeDef",
    "TagTypeDef",
    "TestCaseTypeDef",
    "TestReportSummaryTypeDef",
    "VpcConfigTypeDef",
    "WebhookFilterTypeDef",
    "WebhookTypeDef",
    "BatchDeleteBuildsOutputTypeDef",
    "BatchGetBuildBatchesOutputTypeDef",
    "BatchGetBuildsOutputTypeDef",
    "BatchGetProjectsOutputTypeDef",
    "BatchGetReportGroupsOutputTypeDef",
    "BatchGetReportsOutputTypeDef",
    "BuildBatchFilterTypeDef",
    "CreateProjectOutputTypeDef",
    "CreateReportGroupOutputTypeDef",
    "CreateWebhookOutputTypeDef",
    "DeleteBuildBatchOutputTypeDef",
    "DeleteSourceCredentialsOutputTypeDef",
    "DescribeCodeCoveragesOutputTypeDef",
    "DescribeTestCasesOutputTypeDef",
    "GetReportGroupTrendOutputTypeDef",
    "GetResourcePolicyOutputTypeDef",
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
    "PaginatorConfigTypeDef",
    "PutResourcePolicyOutputTypeDef",
    "ReportFilterTypeDef",
    "RetryBuildBatchOutputTypeDef",
    "RetryBuildOutputTypeDef",
    "StartBuildBatchOutputTypeDef",
    "StartBuildOutputTypeDef",
    "StopBuildBatchOutputTypeDef",
    "StopBuildOutputTypeDef",
    "TestCaseFilterTypeDef",
    "UpdateProjectOutputTypeDef",
    "UpdateReportGroupOutputTypeDef",
    "UpdateWebhookOutputTypeDef",
)

BatchRestrictionsTypeDef = TypedDict(
    "BatchRestrictionsTypeDef",
    {"maximumBuildsAllowed": int, "computeTypesAllowed": List[str]},
    total=False,
)

BuildArtifactsTypeDef = TypedDict(
    "BuildArtifactsTypeDef",
    {
        "location": str,
        "sha256sum": str,
        "md5sum": str,
        "overrideArtifactName": bool,
        "encryptionDisabled": bool,
        "artifactIdentifier": str,
        "bucketOwnerAccess": BucketOwnerAccess,
    },
    total=False,
)

BuildBatchPhaseTypeDef = TypedDict(
    "BuildBatchPhaseTypeDef",
    {
        "phaseType": BuildBatchPhaseType,
        "phaseStatus": StatusType,
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List["PhaseContextTypeDef"],
    },
    total=False,
)

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

BuildGroupTypeDef = TypedDict(
    "BuildGroupTypeDef",
    {
        "identifier": str,
        "dependsOn": List[str],
        "ignoreFailure": bool,
        "currentBuildSummary": "BuildSummaryTypeDef",
        "priorBuildSummaryList": List["BuildSummaryTypeDef"],
    },
    total=False,
)

BuildNotDeletedTypeDef = TypedDict(
    "BuildNotDeletedTypeDef", {"id": str, "statusCode": str}, total=False
)

BuildPhaseTypeDef = TypedDict(
    "BuildPhaseTypeDef",
    {
        "phaseType": BuildPhaseType,
        "phaseStatus": StatusType,
        "startTime": datetime,
        "endTime": datetime,
        "durationInSeconds": int,
        "contexts": List["PhaseContextTypeDef"],
    },
    total=False,
)

BuildStatusConfigTypeDef = TypedDict(
    "BuildStatusConfigTypeDef", {"context": str, "targetUrl": str}, total=False
)

BuildSummaryTypeDef = TypedDict(
    "BuildSummaryTypeDef",
    {
        "arn": str,
        "requestedOn": datetime,
        "buildStatus": StatusType,
        "primaryArtifact": "ResolvedArtifactTypeDef",
        "secondaryArtifacts": List["ResolvedArtifactTypeDef"],
    },
    total=False,
)

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

_RequiredCloudWatchLogsConfigTypeDef = TypedDict(
    "_RequiredCloudWatchLogsConfigTypeDef", {"status": LogsConfigStatusType}
)
_OptionalCloudWatchLogsConfigTypeDef = TypedDict(
    "_OptionalCloudWatchLogsConfigTypeDef", {"groupName": str, "streamName": str}, total=False
)


class CloudWatchLogsConfigTypeDef(
    _RequiredCloudWatchLogsConfigTypeDef, _OptionalCloudWatchLogsConfigTypeDef
):
    pass


CodeCoverageReportSummaryTypeDef = TypedDict(
    "CodeCoverageReportSummaryTypeDef",
    {
        "lineCoveragePercentage": float,
        "linesCovered": int,
        "linesMissed": int,
        "branchCoveragePercentage": float,
        "branchesCovered": int,
        "branchesMissed": int,
    },
    total=False,
)

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

DebugSessionTypeDef = TypedDict(
    "DebugSessionTypeDef", {"sessionEnabled": bool, "sessionTarget": str}, total=False
)

EnvironmentImageTypeDef = TypedDict(
    "EnvironmentImageTypeDef", {"name": str, "description": str, "versions": List[str]}, total=False
)

EnvironmentLanguageTypeDef = TypedDict(
    "EnvironmentLanguageTypeDef",
    {"language": LanguageType, "images": List["EnvironmentImageTypeDef"]},
    total=False,
)

EnvironmentPlatformTypeDef = TypedDict(
    "EnvironmentPlatformTypeDef",
    {"platform": PlatformType, "languages": List["EnvironmentLanguageTypeDef"]},
    total=False,
)

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


ExportedEnvironmentVariableTypeDef = TypedDict(
    "ExportedEnvironmentVariableTypeDef", {"name": str, "value": str}, total=False
)

GitSubmodulesConfigTypeDef = TypedDict("GitSubmodulesConfigTypeDef", {"fetchSubmodules": bool})

LogsConfigTypeDef = TypedDict(
    "LogsConfigTypeDef",
    {"cloudWatchLogs": "CloudWatchLogsConfigTypeDef", "s3Logs": "S3LogsConfigTypeDef"},
    total=False,
)

LogsLocationTypeDef = TypedDict(
    "LogsLocationTypeDef",
    {
        "groupName": str,
        "streamName": str,
        "deepLink": str,
        "s3DeepLink": str,
        "cloudWatchLogsArn": str,
        "s3LogsArn": str,
        "cloudWatchLogs": "CloudWatchLogsConfigTypeDef",
        "s3Logs": "S3LogsConfigTypeDef",
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef", {"subnetId": str, "networkInterfaceId": str}, total=False
)

PhaseContextTypeDef = TypedDict(
    "PhaseContextTypeDef", {"statusCode": str, "message": str}, total=False
)

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


ProjectBadgeTypeDef = TypedDict(
    "ProjectBadgeTypeDef", {"badgeEnabled": bool, "badgeRequestUrl": str}, total=False
)

ProjectBuildBatchConfigTypeDef = TypedDict(
    "ProjectBuildBatchConfigTypeDef",
    {
        "serviceRole": str,
        "combineArtifacts": bool,
        "restrictions": "BatchRestrictionsTypeDef",
        "timeoutInMins": int,
    },
    total=False,
)

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
        "type": FileSystemType,
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


ProjectSourceVersionTypeDef = TypedDict(
    "ProjectSourceVersionTypeDef", {"sourceIdentifier": str, "sourceVersion": str}
)

ProjectTypeDef = TypedDict(
    "ProjectTypeDef",
    {
        "name": str,
        "arn": str,
        "description": str,
        "source": "ProjectSourceTypeDef",
        "secondarySources": List["ProjectSourceTypeDef"],
        "sourceVersion": str,
        "secondarySourceVersions": List["ProjectSourceVersionTypeDef"],
        "artifacts": "ProjectArtifactsTypeDef",
        "secondaryArtifacts": List["ProjectArtifactsTypeDef"],
        "cache": "ProjectCacheTypeDef",
        "environment": "ProjectEnvironmentTypeDef",
        "serviceRole": str,
        "timeoutInMinutes": int,
        "queuedTimeoutInMinutes": int,
        "encryptionKey": str,
        "tags": List["TagTypeDef"],
        "created": datetime,
        "lastModified": datetime,
        "webhook": "WebhookTypeDef",
        "vpcConfig": "VpcConfigTypeDef",
        "badge": "ProjectBadgeTypeDef",
        "logsConfig": "LogsConfigTypeDef",
        "fileSystemLocations": List["ProjectFileSystemLocationTypeDef"],
        "buildBatchConfig": "ProjectBuildBatchConfigTypeDef",
        "concurrentBuildLimit": int,
    },
    total=False,
)

RegistryCredentialTypeDef = TypedDict(
    "RegistryCredentialTypeDef", {"credential": str, "credentialProvider": CredentialProviderType}
)

ReportExportConfigTypeDef = TypedDict(
    "ReportExportConfigTypeDef",
    {"exportConfigType": ReportExportConfigType, "s3Destination": "S3ReportExportConfigTypeDef"},
    total=False,
)

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

ReportWithRawDataTypeDef = TypedDict(
    "ReportWithRawDataTypeDef", {"reportArn": str, "data": str}, total=False
)

ResolvedArtifactTypeDef = TypedDict(
    "ResolvedArtifactTypeDef",
    {"type": ArtifactsType, "location": str, "identifier": str},
    total=False,
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

_RequiredS3LogsConfigTypeDef = TypedDict(
    "_RequiredS3LogsConfigTypeDef", {"status": LogsConfigStatusType}
)
_OptionalS3LogsConfigTypeDef = TypedDict(
    "_OptionalS3LogsConfigTypeDef",
    {"location": str, "encryptionDisabled": bool, "bucketOwnerAccess": BucketOwnerAccess},
    total=False,
)


class S3LogsConfigTypeDef(_RequiredS3LogsConfigTypeDef, _OptionalS3LogsConfigTypeDef):
    pass


S3ReportExportConfigTypeDef = TypedDict(
    "S3ReportExportConfigTypeDef",
    {
        "bucket": str,
        "bucketOwner": str,
        "path": str,
        "packaging": ReportPackagingType,
        "encryptionKey": str,
        "encryptionDisabled": bool,
    },
    total=False,
)

_RequiredSourceAuthTypeDef = TypedDict("_RequiredSourceAuthTypeDef", {"type": SourceAuthType})
_OptionalSourceAuthTypeDef = TypedDict("_OptionalSourceAuthTypeDef", {"resource": str}, total=False)


class SourceAuthTypeDef(_RequiredSourceAuthTypeDef, _OptionalSourceAuthTypeDef):
    pass


SourceCredentialsInfoTypeDef = TypedDict(
    "SourceCredentialsInfoTypeDef",
    {"arn": str, "serverType": ServerType, "authType": AuthType},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str}, total=False)

TestCaseTypeDef = TypedDict(
    "TestCaseTypeDef",
    {
        "reportArn": str,
        "testRawDataPath": str,
        "prefix": str,
        "name": str,
        "status": str,
        "durationInNanoSeconds": int,
        "message": str,
        "expired": datetime,
    },
    total=False,
)

TestReportSummaryTypeDef = TypedDict(
    "TestReportSummaryTypeDef",
    {"total": int, "statusCounts": Dict[str, int], "durationInNanoSeconds": int},
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef",
    {"vpcId": str, "subnets": List[str], "securityGroupIds": List[str]},
    total=False,
)

_RequiredWebhookFilterTypeDef = TypedDict(
    "_RequiredWebhookFilterTypeDef", {"type": WebhookFilterType, "pattern": str}
)
_OptionalWebhookFilterTypeDef = TypedDict(
    "_OptionalWebhookFilterTypeDef", {"excludeMatchedPattern": bool}, total=False
)


class WebhookFilterTypeDef(_RequiredWebhookFilterTypeDef, _OptionalWebhookFilterTypeDef):
    pass


WebhookTypeDef = TypedDict(
    "WebhookTypeDef",
    {
        "url": str,
        "payloadUrl": str,
        "secret": str,
        "branchFilter": str,
        "filterGroups": List[List["WebhookFilterTypeDef"]],
        "buildType": WebhookBuildType,
        "lastModifiedSecret": datetime,
    },
    total=False,
)

BatchDeleteBuildsOutputTypeDef = TypedDict(
    "BatchDeleteBuildsOutputTypeDef",
    {
        "buildsDeleted": List[str],
        "buildsNotDeleted": List["BuildNotDeletedTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

BatchGetBuildBatchesOutputTypeDef = TypedDict(
    "BatchGetBuildBatchesOutputTypeDef",
    {
        "buildBatches": List["BuildBatchTypeDef"],
        "buildBatchesNotFound": List[str],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

BatchGetBuildsOutputTypeDef = TypedDict(
    "BatchGetBuildsOutputTypeDef",
    {
        "builds": List["BuildTypeDef"],
        "buildsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

BatchGetProjectsOutputTypeDef = TypedDict(
    "BatchGetProjectsOutputTypeDef",
    {
        "projects": List["ProjectTypeDef"],
        "projectsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

BatchGetReportGroupsOutputTypeDef = TypedDict(
    "BatchGetReportGroupsOutputTypeDef",
    {
        "reportGroups": List["ReportGroupTypeDef"],
        "reportGroupsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

BatchGetReportsOutputTypeDef = TypedDict(
    "BatchGetReportsOutputTypeDef",
    {
        "reports": List["ReportTypeDef"],
        "reportsNotFound": List[str],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

BuildBatchFilterTypeDef = TypedDict("BuildBatchFilterTypeDef", {"status": StatusType}, total=False)

CreateProjectOutputTypeDef = TypedDict(
    "CreateProjectOutputTypeDef",
    {"project": "ProjectTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateReportGroupOutputTypeDef = TypedDict(
    "CreateReportGroupOutputTypeDef",
    {"reportGroup": "ReportGroupTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateWebhookOutputTypeDef = TypedDict(
    "CreateWebhookOutputTypeDef",
    {"webhook": "WebhookTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DeleteBuildBatchOutputTypeDef = TypedDict(
    "DeleteBuildBatchOutputTypeDef",
    {
        "statusCode": str,
        "buildsDeleted": List[str],
        "buildsNotDeleted": List["BuildNotDeletedTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DeleteSourceCredentialsOutputTypeDef = TypedDict(
    "DeleteSourceCredentialsOutputTypeDef",
    {"arn": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeCodeCoveragesOutputTypeDef = TypedDict(
    "DescribeCodeCoveragesOutputTypeDef",
    {
        "nextToken": str,
        "codeCoverages": List["CodeCoverageTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

DescribeTestCasesOutputTypeDef = TypedDict(
    "DescribeTestCasesOutputTypeDef",
    {
        "nextToken": str,
        "testCases": List["TestCaseTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetReportGroupTrendOutputTypeDef = TypedDict(
    "GetReportGroupTrendOutputTypeDef",
    {
        "stats": "ReportGroupTrendStatsTypeDef",
        "rawData": List["ReportWithRawDataTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetResourcePolicyOutputTypeDef = TypedDict(
    "GetResourcePolicyOutputTypeDef",
    {"policy": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ImportSourceCredentialsOutputTypeDef = TypedDict(
    "ImportSourceCredentialsOutputTypeDef",
    {"arn": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListBuildBatchesForProjectOutputTypeDef = TypedDict(
    "ListBuildBatchesForProjectOutputTypeDef",
    {"ids": List[str], "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListBuildBatchesOutputTypeDef = TypedDict(
    "ListBuildBatchesOutputTypeDef",
    {"ids": List[str], "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListBuildsForProjectOutputTypeDef = TypedDict(
    "ListBuildsForProjectOutputTypeDef",
    {"ids": List[str], "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListBuildsOutputTypeDef = TypedDict(
    "ListBuildsOutputTypeDef",
    {"ids": List[str], "nextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListCuratedEnvironmentImagesOutputTypeDef = TypedDict(
    "ListCuratedEnvironmentImagesOutputTypeDef",
    {"platforms": List["EnvironmentPlatformTypeDef"], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListProjectsOutputTypeDef = TypedDict(
    "ListProjectsOutputTypeDef",
    {"nextToken": str, "projects": List[str], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListReportGroupsOutputTypeDef = TypedDict(
    "ListReportGroupsOutputTypeDef",
    {"nextToken": str, "reportGroups": List[str], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListReportsForReportGroupOutputTypeDef = TypedDict(
    "ListReportsForReportGroupOutputTypeDef",
    {"nextToken": str, "reports": List[str], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListReportsOutputTypeDef = TypedDict(
    "ListReportsOutputTypeDef",
    {"nextToken": str, "reports": List[str], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListSharedProjectsOutputTypeDef = TypedDict(
    "ListSharedProjectsOutputTypeDef",
    {"nextToken": str, "projects": List[str], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListSharedReportGroupsOutputTypeDef = TypedDict(
    "ListSharedReportGroupsOutputTypeDef",
    {"nextToken": str, "reportGroups": List[str], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListSourceCredentialsOutputTypeDef = TypedDict(
    "ListSourceCredentialsOutputTypeDef",
    {
        "sourceCredentialsInfos": List["SourceCredentialsInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutResourcePolicyOutputTypeDef = TypedDict(
    "PutResourcePolicyOutputTypeDef",
    {"resourceArn": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ReportFilterTypeDef = TypedDict("ReportFilterTypeDef", {"status": ReportStatusType}, total=False)

RetryBuildBatchOutputTypeDef = TypedDict(
    "RetryBuildBatchOutputTypeDef",
    {"buildBatch": "BuildBatchTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

RetryBuildOutputTypeDef = TypedDict(
    "RetryBuildOutputTypeDef",
    {"build": "BuildTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

StartBuildBatchOutputTypeDef = TypedDict(
    "StartBuildBatchOutputTypeDef",
    {"buildBatch": "BuildBatchTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

StartBuildOutputTypeDef = TypedDict(
    "StartBuildOutputTypeDef",
    {"build": "BuildTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

StopBuildBatchOutputTypeDef = TypedDict(
    "StopBuildBatchOutputTypeDef",
    {"buildBatch": "BuildBatchTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

StopBuildOutputTypeDef = TypedDict(
    "StopBuildOutputTypeDef",
    {"build": "BuildTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

TestCaseFilterTypeDef = TypedDict(
    "TestCaseFilterTypeDef", {"status": str, "keyword": str}, total=False
)

UpdateProjectOutputTypeDef = TypedDict(
    "UpdateProjectOutputTypeDef",
    {"project": "ProjectTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateReportGroupOutputTypeDef = TypedDict(
    "UpdateReportGroupOutputTypeDef",
    {"reportGroup": "ReportGroupTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

UpdateWebhookOutputTypeDef = TypedDict(
    "UpdateWebhookOutputTypeDef",
    {"webhook": "WebhookTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)
