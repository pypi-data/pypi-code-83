"""
Type annotations for robomaker service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/type_defs.html)

Usage::

    ```python
    from mypy_boto3_robomaker.type_defs import BatchDeleteWorldsResponseTypeDef

    data: BatchDeleteWorldsResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_robomaker.literals import (
    Architecture,
    DeploymentJobErrorCode,
    DeploymentStatus,
    ExitBehavior,
    FailureBehavior,
    RobotDeploymentStep,
    RobotSoftwareSuiteType,
    RobotSoftwareSuiteVersionType,
    RobotStatus,
    SimulationJobBatchStatus,
    SimulationJobErrorCode,
    SimulationJobStatus,
    SimulationSoftwareSuiteType,
    UploadBehavior,
    WorldExportJobErrorCode,
    WorldExportJobStatus,
    WorldGenerationJobErrorCode,
    WorldGenerationJobStatus,
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
    "BatchDeleteWorldsResponseTypeDef",
    "BatchDescribeSimulationJobResponseTypeDef",
    "BatchPolicyTypeDef",
    "ComputeResponseTypeDef",
    "ComputeTypeDef",
    "CreateDeploymentJobResponseTypeDef",
    "CreateFleetResponseTypeDef",
    "CreateRobotApplicationResponseTypeDef",
    "CreateRobotApplicationVersionResponseTypeDef",
    "CreateRobotResponseTypeDef",
    "CreateSimulationApplicationResponseTypeDef",
    "CreateSimulationApplicationVersionResponseTypeDef",
    "CreateSimulationJobResponseTypeDef",
    "CreateWorldExportJobResponseTypeDef",
    "CreateWorldGenerationJobResponseTypeDef",
    "CreateWorldTemplateResponseTypeDef",
    "DataSourceConfigTypeDef",
    "DataSourceTypeDef",
    "DeploymentApplicationConfigTypeDef",
    "DeploymentConfigTypeDef",
    "DeploymentJobTypeDef",
    "DeploymentLaunchConfigTypeDef",
    "DeregisterRobotResponseTypeDef",
    "DescribeDeploymentJobResponseTypeDef",
    "DescribeFleetResponseTypeDef",
    "DescribeRobotApplicationResponseTypeDef",
    "DescribeRobotResponseTypeDef",
    "DescribeSimulationApplicationResponseTypeDef",
    "DescribeSimulationJobBatchResponseTypeDef",
    "DescribeSimulationJobResponseTypeDef",
    "DescribeWorldExportJobResponseTypeDef",
    "DescribeWorldGenerationJobResponseTypeDef",
    "DescribeWorldResponseTypeDef",
    "DescribeWorldTemplateResponseTypeDef",
    "FailedCreateSimulationJobRequestTypeDef",
    "FailureSummaryTypeDef",
    "FilterTypeDef",
    "FinishedWorldsSummaryTypeDef",
    "FleetTypeDef",
    "GetWorldTemplateBodyResponseTypeDef",
    "LaunchConfigTypeDef",
    "ListDeploymentJobsResponseTypeDef",
    "ListFleetsResponseTypeDef",
    "ListRobotApplicationsResponseTypeDef",
    "ListRobotsResponseTypeDef",
    "ListSimulationApplicationsResponseTypeDef",
    "ListSimulationJobBatchesResponseTypeDef",
    "ListSimulationJobsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorldExportJobsResponseTypeDef",
    "ListWorldGenerationJobsResponseTypeDef",
    "ListWorldTemplatesResponseTypeDef",
    "ListWorldsResponseTypeDef",
    "LoggingConfigTypeDef",
    "NetworkInterfaceTypeDef",
    "OutputLocationTypeDef",
    "PaginatorConfigTypeDef",
    "PortForwardingConfigTypeDef",
    "PortMappingTypeDef",
    "ProgressDetailTypeDef",
    "RegisterRobotResponseTypeDef",
    "RenderingEngineTypeDef",
    "ResponseMetadata",
    "RobotApplicationConfigTypeDef",
    "RobotApplicationSummaryTypeDef",
    "RobotDeploymentTypeDef",
    "RobotSoftwareSuiteTypeDef",
    "RobotTypeDef",
    "S3KeyOutputTypeDef",
    "S3ObjectTypeDef",
    "SimulationApplicationConfigTypeDef",
    "SimulationApplicationSummaryTypeDef",
    "SimulationJobBatchSummaryTypeDef",
    "SimulationJobRequestTypeDef",
    "SimulationJobSummaryTypeDef",
    "SimulationJobTypeDef",
    "SimulationSoftwareSuiteTypeDef",
    "SourceConfigTypeDef",
    "SourceTypeDef",
    "StartSimulationJobBatchResponseTypeDef",
    "SyncDeploymentJobResponseTypeDef",
    "TemplateLocationTypeDef",
    "TemplateSummaryTypeDef",
    "ToolTypeDef",
    "UpdateRobotApplicationResponseTypeDef",
    "UpdateSimulationApplicationResponseTypeDef",
    "UpdateWorldTemplateResponseTypeDef",
    "UploadConfigurationTypeDef",
    "VPCConfigResponseTypeDef",
    "VPCConfigTypeDef",
    "WorldConfigTypeDef",
    "WorldCountTypeDef",
    "WorldExportJobSummaryTypeDef",
    "WorldFailureTypeDef",
    "WorldGenerationJobSummaryTypeDef",
    "WorldSummaryTypeDef",
)


class BatchDeleteWorldsResponseTypeDef(TypedDict, total=False):
    unprocessedWorlds: List[str]


class BatchDescribeSimulationJobResponseTypeDef(TypedDict, total=False):
    jobs: List["SimulationJobTypeDef"]
    unprocessedJobs: List[str]


class BatchPolicyTypeDef(TypedDict, total=False):
    timeoutInSeconds: int
    maxConcurrency: int


class ComputeResponseTypeDef(TypedDict, total=False):
    simulationUnitLimit: int


class ComputeTypeDef(TypedDict, total=False):
    simulationUnitLimit: int


class CreateDeploymentJobResponseTypeDef(TypedDict, total=False):
    arn: str
    fleet: str
    status: DeploymentStatus
    deploymentApplicationConfigs: List["DeploymentApplicationConfigTypeDef"]
    failureReason: str
    failureCode: DeploymentJobErrorCode
    createdAt: datetime
    deploymentConfig: "DeploymentConfigTypeDef"
    tags: Dict[str, str]


class CreateFleetResponseTypeDef(TypedDict, total=False):
    arn: str
    name: str
    createdAt: datetime
    tags: Dict[str, str]


class CreateRobotApplicationResponseTypeDef(TypedDict, total=False):
    arn: str
    name: str
    version: str
    sources: List["SourceTypeDef"]
    robotSoftwareSuite: "RobotSoftwareSuiteTypeDef"
    lastUpdatedAt: datetime
    revisionId: str
    tags: Dict[str, str]


class CreateRobotApplicationVersionResponseTypeDef(TypedDict, total=False):
    arn: str
    name: str
    version: str
    sources: List["SourceTypeDef"]
    robotSoftwareSuite: "RobotSoftwareSuiteTypeDef"
    lastUpdatedAt: datetime
    revisionId: str


class CreateRobotResponseTypeDef(TypedDict, total=False):
    arn: str
    name: str
    createdAt: datetime
    greengrassGroupId: str
    architecture: Architecture
    tags: Dict[str, str]


class CreateSimulationApplicationResponseTypeDef(TypedDict, total=False):
    arn: str
    name: str
    version: str
    sources: List["SourceTypeDef"]
    simulationSoftwareSuite: "SimulationSoftwareSuiteTypeDef"
    robotSoftwareSuite: "RobotSoftwareSuiteTypeDef"
    renderingEngine: "RenderingEngineTypeDef"
    lastUpdatedAt: datetime
    revisionId: str
    tags: Dict[str, str]


class CreateSimulationApplicationVersionResponseTypeDef(TypedDict, total=False):
    arn: str
    name: str
    version: str
    sources: List["SourceTypeDef"]
    simulationSoftwareSuite: "SimulationSoftwareSuiteTypeDef"
    robotSoftwareSuite: "RobotSoftwareSuiteTypeDef"
    renderingEngine: "RenderingEngineTypeDef"
    lastUpdatedAt: datetime
    revisionId: str


class CreateSimulationJobResponseTypeDef(TypedDict, total=False):
    arn: str
    status: SimulationJobStatus
    lastStartedAt: datetime
    lastUpdatedAt: datetime
    failureBehavior: FailureBehavior
    failureCode: SimulationJobErrorCode
    clientRequestToken: str
    outputLocation: "OutputLocationTypeDef"
    loggingConfig: "LoggingConfigTypeDef"
    maxJobDurationInSeconds: int
    simulationTimeMillis: int
    iamRole: str
    robotApplications: List["RobotApplicationConfigTypeDef"]
    simulationApplications: List["SimulationApplicationConfigTypeDef"]
    dataSources: List["DataSourceTypeDef"]
    tags: Dict[str, str]
    vpcConfig: "VPCConfigResponseTypeDef"
    compute: "ComputeResponseTypeDef"


class CreateWorldExportJobResponseTypeDef(TypedDict, total=False):
    arn: str
    status: WorldExportJobStatus
    createdAt: datetime
    failureCode: WorldExportJobErrorCode
    clientRequestToken: str
    outputLocation: "OutputLocationTypeDef"
    iamRole: str
    tags: Dict[str, str]


class CreateWorldGenerationJobResponseTypeDef(TypedDict, total=False):
    arn: str
    status: WorldGenerationJobStatus
    createdAt: datetime
    failureCode: WorldGenerationJobErrorCode
    clientRequestToken: str
    template: str
    worldCount: "WorldCountTypeDef"
    tags: Dict[str, str]
    worldTags: Dict[str, str]


class CreateWorldTemplateResponseTypeDef(TypedDict, total=False):
    arn: str
    clientRequestToken: str
    createdAt: datetime
    name: str
    tags: Dict[str, str]


class DataSourceConfigTypeDef(TypedDict):
    name: str
    s3Bucket: str
    s3Keys: List[str]


class DataSourceTypeDef(TypedDict, total=False):
    name: str
    s3Bucket: str
    s3Keys: List["S3KeyOutputTypeDef"]


class DeploymentApplicationConfigTypeDef(TypedDict):
    application: str
    applicationVersion: str
    launchConfig: "DeploymentLaunchConfigTypeDef"


class DeploymentConfigTypeDef(TypedDict, total=False):
    concurrentDeploymentPercentage: int
    failureThresholdPercentage: int
    robotDeploymentTimeoutInSeconds: int
    downloadConditionFile: "S3ObjectTypeDef"


class DeploymentJobTypeDef(TypedDict, total=False):
    arn: str
    fleet: str
    status: DeploymentStatus
    deploymentApplicationConfigs: List["DeploymentApplicationConfigTypeDef"]
    deploymentConfig: "DeploymentConfigTypeDef"
    failureReason: str
    failureCode: DeploymentJobErrorCode
    createdAt: datetime


class _RequiredDeploymentLaunchConfigTypeDef(TypedDict):
    packageName: str
    launchFile: str


class DeploymentLaunchConfigTypeDef(_RequiredDeploymentLaunchConfigTypeDef, total=False):
    preLaunchFile: str
    postLaunchFile: str
    environmentVariables: Dict[str, str]


class DeregisterRobotResponseTypeDef(TypedDict, total=False):
    fleet: str
    robot: str


class DescribeDeploymentJobResponseTypeDef(TypedDict, total=False):
    arn: str
    fleet: str
    status: DeploymentStatus
    deploymentConfig: "DeploymentConfigTypeDef"
    deploymentApplicationConfigs: List["DeploymentApplicationConfigTypeDef"]
    failureReason: str
    failureCode: DeploymentJobErrorCode
    createdAt: datetime
    robotDeploymentSummary: List["RobotDeploymentTypeDef"]
    tags: Dict[str, str]


class DescribeFleetResponseTypeDef(TypedDict, total=False):
    name: str
    arn: str
    robots: List["RobotTypeDef"]
    createdAt: datetime
    lastDeploymentStatus: DeploymentStatus
    lastDeploymentJob: str
    lastDeploymentTime: datetime
    tags: Dict[str, str]


class DescribeRobotApplicationResponseTypeDef(TypedDict, total=False):
    arn: str
    name: str
    version: str
    sources: List["SourceTypeDef"]
    robotSoftwareSuite: "RobotSoftwareSuiteTypeDef"
    revisionId: str
    lastUpdatedAt: datetime
    tags: Dict[str, str]


class DescribeRobotResponseTypeDef(TypedDict, total=False):
    arn: str
    name: str
    fleetArn: str
    status: RobotStatus
    greengrassGroupId: str
    createdAt: datetime
    architecture: Architecture
    lastDeploymentJob: str
    lastDeploymentTime: datetime
    tags: Dict[str, str]


class DescribeSimulationApplicationResponseTypeDef(TypedDict, total=False):
    arn: str
    name: str
    version: str
    sources: List["SourceTypeDef"]
    simulationSoftwareSuite: "SimulationSoftwareSuiteTypeDef"
    robotSoftwareSuite: "RobotSoftwareSuiteTypeDef"
    renderingEngine: "RenderingEngineTypeDef"
    revisionId: str
    lastUpdatedAt: datetime
    tags: Dict[str, str]


class DescribeSimulationJobBatchResponseTypeDef(TypedDict, total=False):
    arn: str
    status: SimulationJobBatchStatus
    lastUpdatedAt: datetime
    createdAt: datetime
    clientRequestToken: str
    batchPolicy: "BatchPolicyTypeDef"
    failureCode: Literal["InternalServiceError"]
    failureReason: str
    failedRequests: List["FailedCreateSimulationJobRequestTypeDef"]
    pendingRequests: List["SimulationJobRequestTypeDef"]
    createdRequests: List["SimulationJobSummaryTypeDef"]
    tags: Dict[str, str]


class DescribeSimulationJobResponseTypeDef(TypedDict, total=False):
    arn: str
    name: str
    status: SimulationJobStatus
    lastStartedAt: datetime
    lastUpdatedAt: datetime
    failureBehavior: FailureBehavior
    failureCode: SimulationJobErrorCode
    failureReason: str
    clientRequestToken: str
    outputLocation: "OutputLocationTypeDef"
    loggingConfig: "LoggingConfigTypeDef"
    maxJobDurationInSeconds: int
    simulationTimeMillis: int
    iamRole: str
    robotApplications: List["RobotApplicationConfigTypeDef"]
    simulationApplications: List["SimulationApplicationConfigTypeDef"]
    dataSources: List["DataSourceTypeDef"]
    tags: Dict[str, str]
    vpcConfig: "VPCConfigResponseTypeDef"
    networkInterface: "NetworkInterfaceTypeDef"
    compute: "ComputeResponseTypeDef"


class DescribeWorldExportJobResponseTypeDef(TypedDict, total=False):
    arn: str
    status: WorldExportJobStatus
    createdAt: datetime
    failureCode: WorldExportJobErrorCode
    failureReason: str
    clientRequestToken: str
    worlds: List[str]
    outputLocation: "OutputLocationTypeDef"
    iamRole: str
    tags: Dict[str, str]


class DescribeWorldGenerationJobResponseTypeDef(TypedDict, total=False):
    arn: str
    status: WorldGenerationJobStatus
    createdAt: datetime
    failureCode: WorldGenerationJobErrorCode
    failureReason: str
    clientRequestToken: str
    template: str
    worldCount: "WorldCountTypeDef"
    finishedWorldsSummary: "FinishedWorldsSummaryTypeDef"
    tags: Dict[str, str]
    worldTags: Dict[str, str]


class DescribeWorldResponseTypeDef(TypedDict, total=False):
    arn: str
    generationJob: str
    template: str
    createdAt: datetime
    tags: Dict[str, str]


class DescribeWorldTemplateResponseTypeDef(TypedDict, total=False):
    arn: str
    clientRequestToken: str
    name: str
    createdAt: datetime
    lastUpdatedAt: datetime
    tags: Dict[str, str]


class FailedCreateSimulationJobRequestTypeDef(TypedDict, total=False):
    request: "SimulationJobRequestTypeDef"
    failureReason: str
    failureCode: SimulationJobErrorCode
    failedAt: datetime


class FailureSummaryTypeDef(TypedDict, total=False):
    totalFailureCount: int
    failures: List["WorldFailureTypeDef"]


class FilterTypeDef(TypedDict, total=False):
    name: str
    values: List[str]


class FinishedWorldsSummaryTypeDef(TypedDict, total=False):
    finishedCount: int
    succeededWorlds: List[str]
    failureSummary: "FailureSummaryTypeDef"


class FleetTypeDef(TypedDict, total=False):
    name: str
    arn: str
    createdAt: datetime
    lastDeploymentStatus: DeploymentStatus
    lastDeploymentJob: str
    lastDeploymentTime: datetime


class GetWorldTemplateBodyResponseTypeDef(TypedDict, total=False):
    templateBody: str


class _RequiredLaunchConfigTypeDef(TypedDict):
    packageName: str
    launchFile: str


class LaunchConfigTypeDef(_RequiredLaunchConfigTypeDef, total=False):
    environmentVariables: Dict[str, str]
    portForwardingConfig: "PortForwardingConfigTypeDef"
    streamUI: bool


class ListDeploymentJobsResponseTypeDef(TypedDict, total=False):
    deploymentJobs: List["DeploymentJobTypeDef"]
    nextToken: str


class ListFleetsResponseTypeDef(TypedDict, total=False):
    fleetDetails: List["FleetTypeDef"]
    nextToken: str


class ListRobotApplicationsResponseTypeDef(TypedDict, total=False):
    robotApplicationSummaries: List["RobotApplicationSummaryTypeDef"]
    nextToken: str


class ListRobotsResponseTypeDef(TypedDict, total=False):
    robots: List["RobotTypeDef"]
    nextToken: str


class ListSimulationApplicationsResponseTypeDef(TypedDict, total=False):
    simulationApplicationSummaries: List["SimulationApplicationSummaryTypeDef"]
    nextToken: str


class ListSimulationJobBatchesResponseTypeDef(TypedDict, total=False):
    simulationJobBatchSummaries: List["SimulationJobBatchSummaryTypeDef"]
    nextToken: str


class _RequiredListSimulationJobsResponseTypeDef(TypedDict):
    simulationJobSummaries: List["SimulationJobSummaryTypeDef"]


class ListSimulationJobsResponseTypeDef(_RequiredListSimulationJobsResponseTypeDef, total=False):
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class _RequiredListWorldExportJobsResponseTypeDef(TypedDict):
    worldExportJobSummaries: List["WorldExportJobSummaryTypeDef"]


class ListWorldExportJobsResponseTypeDef(_RequiredListWorldExportJobsResponseTypeDef, total=False):
    nextToken: str


class _RequiredListWorldGenerationJobsResponseTypeDef(TypedDict):
    worldGenerationJobSummaries: List["WorldGenerationJobSummaryTypeDef"]


class ListWorldGenerationJobsResponseTypeDef(
    _RequiredListWorldGenerationJobsResponseTypeDef, total=False
):
    nextToken: str


class ListWorldTemplatesResponseTypeDef(TypedDict, total=False):
    templateSummaries: List["TemplateSummaryTypeDef"]
    nextToken: str


class ListWorldsResponseTypeDef(TypedDict, total=False):
    worldSummaries: List["WorldSummaryTypeDef"]
    nextToken: str


class LoggingConfigTypeDef(TypedDict):
    recordAllRosTopics: bool


class NetworkInterfaceTypeDef(TypedDict, total=False):
    networkInterfaceId: str
    privateIpAddress: str
    publicIpAddress: str


class OutputLocationTypeDef(TypedDict, total=False):
    s3Bucket: str
    s3Prefix: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PortForwardingConfigTypeDef(TypedDict, total=False):
    portMappings: List["PortMappingTypeDef"]


class _RequiredPortMappingTypeDef(TypedDict):
    jobPort: int
    applicationPort: int


class PortMappingTypeDef(_RequiredPortMappingTypeDef, total=False):
    enableOnPublicIp: bool


class ProgressDetailTypeDef(TypedDict, total=False):
    currentProgress: RobotDeploymentStep
    percentDone: float
    estimatedTimeRemainingSeconds: int
    targetResource: str


class RegisterRobotResponseTypeDef(TypedDict, total=False):
    fleet: str
    robot: str


class RenderingEngineTypeDef(TypedDict, total=False):
    name: Literal["OGRE"]
    version: str


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class _RequiredRobotApplicationConfigTypeDef(TypedDict):
    application: str
    launchConfig: "LaunchConfigTypeDef"


class RobotApplicationConfigTypeDef(_RequiredRobotApplicationConfigTypeDef, total=False):
    applicationVersion: str
    uploadConfigurations: List["UploadConfigurationTypeDef"]
    useDefaultUploadConfigurations: bool
    tools: List["ToolTypeDef"]
    useDefaultTools: bool


class RobotApplicationSummaryTypeDef(TypedDict, total=False):
    name: str
    arn: str
    version: str
    lastUpdatedAt: datetime
    robotSoftwareSuite: "RobotSoftwareSuiteTypeDef"


class RobotDeploymentTypeDef(TypedDict, total=False):
    arn: str
    deploymentStartTime: datetime
    deploymentFinishTime: datetime
    status: RobotStatus
    progressDetail: "ProgressDetailTypeDef"
    failureReason: str
    failureCode: DeploymentJobErrorCode


class RobotSoftwareSuiteTypeDef(TypedDict, total=False):
    name: RobotSoftwareSuiteType
    version: RobotSoftwareSuiteVersionType


class RobotTypeDef(TypedDict, total=False):
    arn: str
    name: str
    fleetArn: str
    status: RobotStatus
    greenGrassGroupId: str
    createdAt: datetime
    architecture: Architecture
    lastDeploymentJob: str
    lastDeploymentTime: datetime


class S3KeyOutputTypeDef(TypedDict):
    s3Key: str
    etag: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredS3ObjectTypeDef(TypedDict):
    bucket: str
    key: str


class S3ObjectTypeDef(_RequiredS3ObjectTypeDef, total=False):
    etag: str


class _RequiredSimulationApplicationConfigTypeDef(TypedDict):
    application: str
    launchConfig: "LaunchConfigTypeDef"


class SimulationApplicationConfigTypeDef(_RequiredSimulationApplicationConfigTypeDef, total=False):
    applicationVersion: str
    uploadConfigurations: List["UploadConfigurationTypeDef"]
    worldConfigs: List["WorldConfigTypeDef"]
    useDefaultUploadConfigurations: bool
    tools: List["ToolTypeDef"]
    useDefaultTools: bool


class SimulationApplicationSummaryTypeDef(TypedDict, total=False):
    name: str
    arn: str
    version: str
    lastUpdatedAt: datetime
    robotSoftwareSuite: "RobotSoftwareSuiteTypeDef"
    simulationSoftwareSuite: "SimulationSoftwareSuiteTypeDef"


class SimulationJobBatchSummaryTypeDef(TypedDict, total=False):
    arn: str
    lastUpdatedAt: datetime
    createdAt: datetime
    status: SimulationJobBatchStatus
    failedRequestCount: int
    pendingRequestCount: int
    createdRequestCount: int


class _RequiredSimulationJobRequestTypeDef(TypedDict):
    maxJobDurationInSeconds: int


class SimulationJobRequestTypeDef(_RequiredSimulationJobRequestTypeDef, total=False):
    outputLocation: "OutputLocationTypeDef"
    loggingConfig: "LoggingConfigTypeDef"
    iamRole: str
    failureBehavior: FailureBehavior
    useDefaultApplications: bool
    robotApplications: List["RobotApplicationConfigTypeDef"]
    simulationApplications: List["SimulationApplicationConfigTypeDef"]
    dataSources: List["DataSourceConfigTypeDef"]
    vpcConfig: "VPCConfigTypeDef"
    compute: "ComputeTypeDef"
    tags: Dict[str, str]


class SimulationJobSummaryTypeDef(TypedDict, total=False):
    arn: str
    lastUpdatedAt: datetime
    name: str
    status: SimulationJobStatus
    simulationApplicationNames: List[str]
    robotApplicationNames: List[str]
    dataSourceNames: List[str]


class SimulationJobTypeDef(TypedDict, total=False):
    arn: str
    name: str
    status: SimulationJobStatus
    lastStartedAt: datetime
    lastUpdatedAt: datetime
    failureBehavior: FailureBehavior
    failureCode: SimulationJobErrorCode
    failureReason: str
    clientRequestToken: str
    outputLocation: "OutputLocationTypeDef"
    loggingConfig: "LoggingConfigTypeDef"
    maxJobDurationInSeconds: int
    simulationTimeMillis: int
    iamRole: str
    robotApplications: List["RobotApplicationConfigTypeDef"]
    simulationApplications: List["SimulationApplicationConfigTypeDef"]
    dataSources: List["DataSourceTypeDef"]
    tags: Dict[str, str]
    vpcConfig: "VPCConfigResponseTypeDef"
    networkInterface: "NetworkInterfaceTypeDef"
    compute: "ComputeResponseTypeDef"


class SimulationSoftwareSuiteTypeDef(TypedDict, total=False):
    name: SimulationSoftwareSuiteType
    version: str


class SourceConfigTypeDef(TypedDict, total=False):
    s3Bucket: str
    s3Key: str
    architecture: Architecture


class SourceTypeDef(TypedDict, total=False):
    s3Bucket: str
    s3Key: str
    etag: str
    architecture: Architecture


class StartSimulationJobBatchResponseTypeDef(TypedDict, total=False):
    arn: str
    status: SimulationJobBatchStatus
    createdAt: datetime
    clientRequestToken: str
    batchPolicy: "BatchPolicyTypeDef"
    failureCode: Literal["InternalServiceError"]
    failureReason: str
    failedRequests: List["FailedCreateSimulationJobRequestTypeDef"]
    pendingRequests: List["SimulationJobRequestTypeDef"]
    createdRequests: List["SimulationJobSummaryTypeDef"]
    tags: Dict[str, str]


class SyncDeploymentJobResponseTypeDef(TypedDict, total=False):
    arn: str
    fleet: str
    status: DeploymentStatus
    deploymentConfig: "DeploymentConfigTypeDef"
    deploymentApplicationConfigs: List["DeploymentApplicationConfigTypeDef"]
    failureReason: str
    failureCode: DeploymentJobErrorCode
    createdAt: datetime


class TemplateLocationTypeDef(TypedDict):
    s3Bucket: str
    s3Key: str


class TemplateSummaryTypeDef(TypedDict, total=False):
    arn: str
    createdAt: datetime
    lastUpdatedAt: datetime
    name: str


class _RequiredToolTypeDef(TypedDict):
    name: str
    command: str


class ToolTypeDef(_RequiredToolTypeDef, total=False):
    streamUI: bool
    streamOutputToCloudWatch: bool
    exitBehavior: ExitBehavior


class UpdateRobotApplicationResponseTypeDef(TypedDict, total=False):
    arn: str
    name: str
    version: str
    sources: List["SourceTypeDef"]
    robotSoftwareSuite: "RobotSoftwareSuiteTypeDef"
    lastUpdatedAt: datetime
    revisionId: str


class UpdateSimulationApplicationResponseTypeDef(TypedDict, total=False):
    arn: str
    name: str
    version: str
    sources: List["SourceTypeDef"]
    simulationSoftwareSuite: "SimulationSoftwareSuiteTypeDef"
    robotSoftwareSuite: "RobotSoftwareSuiteTypeDef"
    renderingEngine: "RenderingEngineTypeDef"
    lastUpdatedAt: datetime
    revisionId: str


class UpdateWorldTemplateResponseTypeDef(TypedDict, total=False):
    arn: str
    name: str
    createdAt: datetime
    lastUpdatedAt: datetime


class UploadConfigurationTypeDef(TypedDict):
    name: str
    path: str
    uploadBehavior: UploadBehavior


class VPCConfigResponseTypeDef(TypedDict, total=False):
    subnets: List[str]
    securityGroups: List[str]
    vpcId: str
    assignPublicIp: bool


class _RequiredVPCConfigTypeDef(TypedDict):
    subnets: List[str]


class VPCConfigTypeDef(_RequiredVPCConfigTypeDef, total=False):
    securityGroups: List[str]
    assignPublicIp: bool


class WorldConfigTypeDef(TypedDict, total=False):
    world: str


class WorldCountTypeDef(TypedDict, total=False):
    floorplanCount: int
    interiorCountPerFloorplan: int


class WorldExportJobSummaryTypeDef(TypedDict, total=False):
    arn: str
    status: WorldExportJobStatus
    createdAt: datetime
    worlds: List[str]


class WorldFailureTypeDef(TypedDict, total=False):
    failureCode: WorldGenerationJobErrorCode
    sampleFailureReason: str
    failureCount: int


class WorldGenerationJobSummaryTypeDef(TypedDict, total=False):
    arn: str
    template: str
    createdAt: datetime
    status: WorldGenerationJobStatus
    worldCount: "WorldCountTypeDef"
    succeededWorldCount: int
    failedWorldCount: int


class WorldSummaryTypeDef(TypedDict, total=False):
    arn: str
    createdAt: datetime
    generationJob: str
    template: str
