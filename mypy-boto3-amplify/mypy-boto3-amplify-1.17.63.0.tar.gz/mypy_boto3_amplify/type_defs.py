"""
Type annotations for amplify service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplify/type_defs.html)

Usage::

    ```python
    from mypy_boto3_amplify.type_defs import AppTypeDef

    data: AppTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_amplify.literals import DomainStatus, JobStatus, JobType, Stage

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AppTypeDef",
    "ArtifactTypeDef",
    "AutoBranchCreationConfigTypeDef",
    "BackendEnvironmentTypeDef",
    "BranchTypeDef",
    "CreateAppResultTypeDef",
    "CreateBackendEnvironmentResultTypeDef",
    "CreateBranchResultTypeDef",
    "CreateDeploymentResultTypeDef",
    "CreateDomainAssociationResultTypeDef",
    "CreateWebhookResultTypeDef",
    "CustomRuleTypeDef",
    "DeleteAppResultTypeDef",
    "DeleteBackendEnvironmentResultTypeDef",
    "DeleteBranchResultTypeDef",
    "DeleteDomainAssociationResultTypeDef",
    "DeleteJobResultTypeDef",
    "DeleteWebhookResultTypeDef",
    "DomainAssociationTypeDef",
    "GenerateAccessLogsResultTypeDef",
    "GetAppResultTypeDef",
    "GetArtifactUrlResultTypeDef",
    "GetBackendEnvironmentResultTypeDef",
    "GetBranchResultTypeDef",
    "GetDomainAssociationResultTypeDef",
    "GetJobResultTypeDef",
    "GetWebhookResultTypeDef",
    "JobSummaryTypeDef",
    "JobTypeDef",
    "ListAppsResultTypeDef",
    "ListArtifactsResultTypeDef",
    "ListBackendEnvironmentsResultTypeDef",
    "ListBranchesResultTypeDef",
    "ListDomainAssociationsResultTypeDef",
    "ListJobsResultTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebhooksResultTypeDef",
    "PaginatorConfigTypeDef",
    "ProductionBranchTypeDef",
    "StartDeploymentResultTypeDef",
    "StartJobResultTypeDef",
    "StepTypeDef",
    "StopJobResultTypeDef",
    "SubDomainSettingTypeDef",
    "SubDomainTypeDef",
    "UpdateAppResultTypeDef",
    "UpdateBranchResultTypeDef",
    "UpdateDomainAssociationResultTypeDef",
    "UpdateWebhookResultTypeDef",
    "WebhookTypeDef",
)


class _RequiredAppTypeDef(TypedDict):
    appId: str
    appArn: str
    name: str
    description: str
    repository: str
    platform: Literal["WEB"]
    createTime: datetime
    updateTime: datetime
    environmentVariables: Dict[str, str]
    defaultDomain: str
    enableBranchAutoBuild: bool
    enableBasicAuth: bool


class AppTypeDef(_RequiredAppTypeDef, total=False):
    tags: Dict[str, str]
    iamServiceRoleArn: str
    enableBranchAutoDeletion: bool
    basicAuthCredentials: str
    customRules: List["CustomRuleTypeDef"]
    productionBranch: "ProductionBranchTypeDef"
    buildSpec: str
    customHeaders: str
    enableAutoBranchCreation: bool
    autoBranchCreationPatterns: List[str]
    autoBranchCreationConfig: "AutoBranchCreationConfigTypeDef"


class ArtifactTypeDef(TypedDict):
    artifactFileName: str
    artifactId: str


class AutoBranchCreationConfigTypeDef(TypedDict, total=False):
    stage: Stage
    framework: str
    enableAutoBuild: bool
    environmentVariables: Dict[str, str]
    basicAuthCredentials: str
    enableBasicAuth: bool
    enablePerformanceMode: bool
    buildSpec: str
    enablePullRequestPreview: bool
    pullRequestEnvironmentName: str


class _RequiredBackendEnvironmentTypeDef(TypedDict):
    backendEnvironmentArn: str
    environmentName: str
    createTime: datetime
    updateTime: datetime


class BackendEnvironmentTypeDef(_RequiredBackendEnvironmentTypeDef, total=False):
    stackName: str
    deploymentArtifacts: str


class _RequiredBranchTypeDef(TypedDict):
    branchArn: str
    branchName: str
    description: str
    stage: Stage
    displayName: str
    enableNotification: bool
    createTime: datetime
    updateTime: datetime
    environmentVariables: Dict[str, str]
    enableAutoBuild: bool
    customDomains: List[str]
    framework: str
    activeJobId: str
    totalNumberOfJobs: str
    enableBasicAuth: bool
    ttl: str
    enablePullRequestPreview: bool


class BranchTypeDef(_RequiredBranchTypeDef, total=False):
    tags: Dict[str, str]
    enablePerformanceMode: bool
    thumbnailUrl: str
    basicAuthCredentials: str
    buildSpec: str
    associatedResources: List[str]
    pullRequestEnvironmentName: str
    destinationBranch: str
    sourceBranch: str
    backendEnvironmentArn: str


class CreateAppResultTypeDef(TypedDict):
    app: "AppTypeDef"


class CreateBackendEnvironmentResultTypeDef(TypedDict):
    backendEnvironment: "BackendEnvironmentTypeDef"


class CreateBranchResultTypeDef(TypedDict):
    branch: "BranchTypeDef"


class _RequiredCreateDeploymentResultTypeDef(TypedDict):
    fileUploadUrls: Dict[str, str]
    zipUploadUrl: str


class CreateDeploymentResultTypeDef(_RequiredCreateDeploymentResultTypeDef, total=False):
    jobId: str


class CreateDomainAssociationResultTypeDef(TypedDict):
    domainAssociation: "DomainAssociationTypeDef"


class CreateWebhookResultTypeDef(TypedDict):
    webhook: "WebhookTypeDef"


class _RequiredCustomRuleTypeDef(TypedDict):
    source: str
    target: str


class CustomRuleTypeDef(_RequiredCustomRuleTypeDef, total=False):
    status: str
    condition: str


class DeleteAppResultTypeDef(TypedDict):
    app: "AppTypeDef"


class DeleteBackendEnvironmentResultTypeDef(TypedDict):
    backendEnvironment: "BackendEnvironmentTypeDef"


class DeleteBranchResultTypeDef(TypedDict):
    branch: "BranchTypeDef"


class DeleteDomainAssociationResultTypeDef(TypedDict):
    domainAssociation: "DomainAssociationTypeDef"


class DeleteJobResultTypeDef(TypedDict):
    jobSummary: "JobSummaryTypeDef"


class DeleteWebhookResultTypeDef(TypedDict):
    webhook: "WebhookTypeDef"


class _RequiredDomainAssociationTypeDef(TypedDict):
    domainAssociationArn: str
    domainName: str
    enableAutoSubDomain: bool
    domainStatus: DomainStatus
    statusReason: str
    subDomains: List["SubDomainTypeDef"]


class DomainAssociationTypeDef(_RequiredDomainAssociationTypeDef, total=False):
    autoSubDomainCreationPatterns: List[str]
    autoSubDomainIAMRole: str
    certificateVerificationDNSRecord: str


class GenerateAccessLogsResultTypeDef(TypedDict, total=False):
    logUrl: str


class GetAppResultTypeDef(TypedDict):
    app: "AppTypeDef"


class GetArtifactUrlResultTypeDef(TypedDict):
    artifactId: str
    artifactUrl: str


class GetBackendEnvironmentResultTypeDef(TypedDict):
    backendEnvironment: "BackendEnvironmentTypeDef"


class GetBranchResultTypeDef(TypedDict):
    branch: "BranchTypeDef"


class GetDomainAssociationResultTypeDef(TypedDict):
    domainAssociation: "DomainAssociationTypeDef"


class GetJobResultTypeDef(TypedDict):
    job: "JobTypeDef"


class GetWebhookResultTypeDef(TypedDict):
    webhook: "WebhookTypeDef"


class _RequiredJobSummaryTypeDef(TypedDict):
    jobArn: str
    jobId: str
    commitId: str
    commitMessage: str
    commitTime: datetime
    startTime: datetime
    status: JobStatus
    jobType: JobType


class JobSummaryTypeDef(_RequiredJobSummaryTypeDef, total=False):
    endTime: datetime


class JobTypeDef(TypedDict):
    summary: "JobSummaryTypeDef"
    steps: List["StepTypeDef"]


class _RequiredListAppsResultTypeDef(TypedDict):
    apps: List["AppTypeDef"]


class ListAppsResultTypeDef(_RequiredListAppsResultTypeDef, total=False):
    nextToken: str


class _RequiredListArtifactsResultTypeDef(TypedDict):
    artifacts: List["ArtifactTypeDef"]


class ListArtifactsResultTypeDef(_RequiredListArtifactsResultTypeDef, total=False):
    nextToken: str


class _RequiredListBackendEnvironmentsResultTypeDef(TypedDict):
    backendEnvironments: List["BackendEnvironmentTypeDef"]


class ListBackendEnvironmentsResultTypeDef(
    _RequiredListBackendEnvironmentsResultTypeDef, total=False
):
    nextToken: str


class _RequiredListBranchesResultTypeDef(TypedDict):
    branches: List["BranchTypeDef"]


class ListBranchesResultTypeDef(_RequiredListBranchesResultTypeDef, total=False):
    nextToken: str


class _RequiredListDomainAssociationsResultTypeDef(TypedDict):
    domainAssociations: List["DomainAssociationTypeDef"]


class ListDomainAssociationsResultTypeDef(
    _RequiredListDomainAssociationsResultTypeDef, total=False
):
    nextToken: str


class _RequiredListJobsResultTypeDef(TypedDict):
    jobSummaries: List["JobSummaryTypeDef"]


class ListJobsResultTypeDef(_RequiredListJobsResultTypeDef, total=False):
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class _RequiredListWebhooksResultTypeDef(TypedDict):
    webhooks: List["WebhookTypeDef"]


class ListWebhooksResultTypeDef(_RequiredListWebhooksResultTypeDef, total=False):
    nextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ProductionBranchTypeDef(TypedDict, total=False):
    lastDeployTime: datetime
    status: str
    thumbnailUrl: str
    branchName: str


class StartDeploymentResultTypeDef(TypedDict):
    jobSummary: "JobSummaryTypeDef"


class StartJobResultTypeDef(TypedDict):
    jobSummary: "JobSummaryTypeDef"


class _RequiredStepTypeDef(TypedDict):
    stepName: str
    startTime: datetime
    status: JobStatus
    endTime: datetime


class StepTypeDef(_RequiredStepTypeDef, total=False):
    logUrl: str
    artifactsUrl: str
    testArtifactsUrl: str
    testConfigUrl: str
    screenshots: Dict[str, str]
    statusReason: str
    context: str


class StopJobResultTypeDef(TypedDict):
    jobSummary: "JobSummaryTypeDef"


class SubDomainSettingTypeDef(TypedDict):
    prefix: str
    branchName: str


class SubDomainTypeDef(TypedDict):
    subDomainSetting: "SubDomainSettingTypeDef"
    verified: bool
    dnsRecord: str


class UpdateAppResultTypeDef(TypedDict):
    app: "AppTypeDef"


class UpdateBranchResultTypeDef(TypedDict):
    branch: "BranchTypeDef"


class UpdateDomainAssociationResultTypeDef(TypedDict):
    domainAssociation: "DomainAssociationTypeDef"


class UpdateWebhookResultTypeDef(TypedDict):
    webhook: "WebhookTypeDef"


class WebhookTypeDef(TypedDict):
    webhookArn: str
    webhookId: str
    webhookUrl: str
    branchName: str
    description: str
    createTime: datetime
    updateTime: datetime
