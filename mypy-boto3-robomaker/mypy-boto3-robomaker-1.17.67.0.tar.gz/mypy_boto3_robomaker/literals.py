"""
Type annotations for robomaker service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_robomaker/literals.html)

Usage::

    ```python
    from mypy_boto3_robomaker.literals import Architecture

    data: Architecture = "ARM64"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "Architecture",
    "DeploymentJobErrorCode",
    "DeploymentStatus",
    "ExitBehavior",
    "FailureBehavior",
    "ListDeploymentJobsPaginatorName",
    "ListFleetsPaginatorName",
    "ListRobotApplicationsPaginatorName",
    "ListRobotsPaginatorName",
    "ListSimulationApplicationsPaginatorName",
    "ListSimulationJobBatchesPaginatorName",
    "ListSimulationJobsPaginatorName",
    "ListWorldExportJobsPaginatorName",
    "ListWorldGenerationJobsPaginatorName",
    "ListWorldTemplatesPaginatorName",
    "ListWorldsPaginatorName",
    "RenderingEngineType",
    "RobotDeploymentStep",
    "RobotSoftwareSuiteType",
    "RobotSoftwareSuiteVersionType",
    "RobotStatus",
    "SimulationJobBatchErrorCode",
    "SimulationJobBatchStatus",
    "SimulationJobErrorCode",
    "SimulationJobStatus",
    "SimulationSoftwareSuiteType",
    "UploadBehavior",
    "WorldExportJobErrorCode",
    "WorldExportJobStatus",
    "WorldGenerationJobErrorCode",
    "WorldGenerationJobStatus",
)


Architecture = Literal["ARM64", "ARMHF", "X86_64"]
DeploymentJobErrorCode = Literal[
    "BadLambdaAssociated",
    "BadPermissionError",
    "DeploymentFleetDoesNotExist",
    "DownloadConditionFailed",
    "EnvironmentSetupError",
    "EtagMismatch",
    "ExtractingBundleFailure",
    "FailureThresholdBreached",
    "FleetDeploymentTimeout",
    "GreengrassDeploymentFailed",
    "GreengrassGroupVersionDoesNotExist",
    "InternalServerError",
    "InvalidGreengrassGroup",
    "LambdaDeleted",
    "MissingRobotApplicationArchitecture",
    "MissingRobotArchitecture",
    "MissingRobotDeploymentResource",
    "PostLaunchFileFailure",
    "PreLaunchFileFailure",
    "ResourceNotFound",
    "RobotAgentConnectionTimeout",
    "RobotApplicationDoesNotExist",
    "RobotDeploymentAborted",
    "RobotDeploymentNoResponse",
]
DeploymentStatus = Literal["Canceled", "Failed", "InProgress", "Pending", "Preparing", "Succeeded"]
ExitBehavior = Literal["FAIL", "RESTART"]
FailureBehavior = Literal["Continue", "Fail"]
ListDeploymentJobsPaginatorName = Literal["list_deployment_jobs"]
ListFleetsPaginatorName = Literal["list_fleets"]
ListRobotApplicationsPaginatorName = Literal["list_robot_applications"]
ListRobotsPaginatorName = Literal["list_robots"]
ListSimulationApplicationsPaginatorName = Literal["list_simulation_applications"]
ListSimulationJobBatchesPaginatorName = Literal["list_simulation_job_batches"]
ListSimulationJobsPaginatorName = Literal["list_simulation_jobs"]
ListWorldExportJobsPaginatorName = Literal["list_world_export_jobs"]
ListWorldGenerationJobsPaginatorName = Literal["list_world_generation_jobs"]
ListWorldTemplatesPaginatorName = Literal["list_world_templates"]
ListWorldsPaginatorName = Literal["list_worlds"]
RenderingEngineType = Literal["OGRE"]
RobotDeploymentStep = Literal[
    "DownloadingExtracting",
    "ExecutingDownloadCondition",
    "ExecutingPostLaunch",
    "ExecutingPreLaunch",
    "Finished",
    "Launching",
    "Validating",
]
RobotSoftwareSuiteType = Literal["ROS", "ROS2"]
RobotSoftwareSuiteVersionType = Literal["Dashing", "Foxy", "Kinetic", "Melodic"]
RobotStatus = Literal[
    "Available", "Deploying", "Failed", "InSync", "NoResponse", "PendingNewDeployment", "Registered"
]
SimulationJobBatchErrorCode = Literal["InternalServiceError"]
SimulationJobBatchStatus = Literal[
    "Canceled",
    "Canceling",
    "Completed",
    "Completing",
    "Failed",
    "InProgress",
    "Pending",
    "TimedOut",
    "TimingOut",
]
SimulationJobErrorCode = Literal[
    "BadPermissionsCloudwatchLogs",
    "BadPermissionsRobotApplication",
    "BadPermissionsS3Object",
    "BadPermissionsS3Output",
    "BadPermissionsSimulationApplication",
    "BadPermissionsUserCredentials",
    "BatchCanceled",
    "BatchTimedOut",
    "ENILimitExceeded",
    "InternalServiceError",
    "InvalidBundleRobotApplication",
    "InvalidBundleSimulationApplication",
    "InvalidInput",
    "InvalidS3Resource",
    "LimitExceeded",
    "MismatchedEtag",
    "RequestThrottled",
    "ResourceNotFound",
    "RobotApplicationCrash",
    "RobotApplicationHealthCheckFailure",
    "RobotApplicationVersionMismatchedEtag",
    "SimulationApplicationCrash",
    "SimulationApplicationHealthCheckFailure",
    "SimulationApplicationVersionMismatchedEtag",
    "SubnetIpLimitExceeded",
    "ThrottlingError",
    "UploadContentMismatchError",
    "WrongRegionRobotApplication",
    "WrongRegionS3Bucket",
    "WrongRegionS3Output",
    "WrongRegionSimulationApplication",
]
SimulationJobStatus = Literal[
    "Canceled",
    "Completed",
    "Failed",
    "Pending",
    "Preparing",
    "Restarting",
    "Running",
    "RunningFailed",
    "Terminated",
    "Terminating",
]
SimulationSoftwareSuiteType = Literal["Gazebo", "RosbagPlay"]
UploadBehavior = Literal["UPLOAD_ON_TERMINATE", "UPLOAD_ROLLING_AUTO_REMOVE"]
WorldExportJobErrorCode = Literal[
    "AccessDenied",
    "InternalServiceError",
    "InvalidInput",
    "LimitExceeded",
    "RequestThrottled",
    "ResourceNotFound",
]
WorldExportJobStatus = Literal["Canceled", "Canceling", "Completed", "Failed", "Pending", "Running"]
WorldGenerationJobErrorCode = Literal[
    "AllWorldGenerationFailed",
    "InternalServiceError",
    "InvalidInput",
    "LimitExceeded",
    "RequestThrottled",
    "ResourceNotFound",
]
WorldGenerationJobStatus = Literal[
    "Canceled", "Canceling", "Completed", "Failed", "PartialFailed", "Pending", "Running"
]
