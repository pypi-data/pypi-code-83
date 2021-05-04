"""
Type annotations for sms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sms.type_defs import AppSummaryTypeDef

    data: AppSummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_sms.literals import (
    AppLaunchConfigurationStatus,
    AppLaunchStatus,
    AppReplicationConfigurationStatus,
    AppReplicationStatus,
    AppStatus,
    ConnectorCapability,
    ConnectorStatus,
    LicenseType,
    ReplicationJobState,
    ReplicationRunState,
    ReplicationRunType,
    ScriptType,
    ServerCatalogStatus,
    ValidationStatus,
    VmManagerType,
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
    "AppSummaryTypeDef",
    "AppValidationConfigurationTypeDef",
    "AppValidationOutputTypeDef",
    "ConnectorTypeDef",
    "CreateAppResponseTypeDef",
    "CreateReplicationJobResponseTypeDef",
    "GenerateChangeSetResponseTypeDef",
    "GenerateTemplateResponseTypeDef",
    "GetAppLaunchConfigurationResponseTypeDef",
    "GetAppReplicationConfigurationResponseTypeDef",
    "GetAppResponseTypeDef",
    "GetAppValidationConfigurationResponseTypeDef",
    "GetAppValidationOutputResponseTypeDef",
    "GetConnectorsResponseTypeDef",
    "GetReplicationJobsResponseTypeDef",
    "GetReplicationRunsResponseTypeDef",
    "GetServersResponseTypeDef",
    "LaunchDetailsTypeDef",
    "ListAppsResponseTypeDef",
    "NotificationContextTypeDef",
    "PaginatorConfigTypeDef",
    "ReplicationJobTypeDef",
    "ReplicationRunStageDetailsTypeDef",
    "ReplicationRunTypeDef",
    "ResponseMetadata",
    "S3LocationTypeDef",
    "SSMOutputTypeDef",
    "SSMValidationParametersTypeDef",
    "ServerGroupLaunchConfigurationTypeDef",
    "ServerGroupReplicationConfigurationTypeDef",
    "ServerGroupTypeDef",
    "ServerGroupValidationConfigurationTypeDef",
    "ServerLaunchConfigurationTypeDef",
    "ServerReplicationConfigurationTypeDef",
    "ServerReplicationParametersTypeDef",
    "ServerTypeDef",
    "ServerValidationConfigurationTypeDef",
    "ServerValidationOutputTypeDef",
    "SourceTypeDef",
    "StartOnDemandReplicationRunResponseTypeDef",
    "TagTypeDef",
    "UpdateAppResponseTypeDef",
    "UserDataTypeDef",
    "UserDataValidationParametersTypeDef",
    "ValidationOutputTypeDef",
    "VmServerAddressTypeDef",
    "VmServerTypeDef",
)


class AppSummaryTypeDef(TypedDict, total=False):
    appId: str
    importedAppId: str
    name: str
    description: str
    status: AppStatus
    statusMessage: str
    replicationConfigurationStatus: AppReplicationConfigurationStatus
    replicationStatus: AppReplicationStatus
    replicationStatusMessage: str
    latestReplicationTime: datetime
    launchConfigurationStatus: AppLaunchConfigurationStatus
    launchStatus: AppLaunchStatus
    launchStatusMessage: str
    launchDetails: "LaunchDetailsTypeDef"
    creationTime: datetime
    lastModified: datetime
    roleName: str
    totalServerGroups: int
    totalServers: int


class AppValidationConfigurationTypeDef(TypedDict, total=False):
    validationId: str
    name: str
    appValidationStrategy: Literal["SSM"]
    ssmValidationParameters: "SSMValidationParametersTypeDef"


class AppValidationOutputTypeDef(TypedDict):
    ssmOutput: "SSMOutputTypeDef"
    ResponseMetadata: "ResponseMetadata"


class ConnectorTypeDef(TypedDict, total=False):
    connectorId: str
    version: str
    status: ConnectorStatus
    capabilityList: List[ConnectorCapability]
    vmManagerName: str
    vmManagerType: VmManagerType
    vmManagerId: str
    ipAddress: str
    macAddress: str
    associatedOn: datetime


class CreateAppResponseTypeDef(TypedDict, total=False):
    appSummary: "AppSummaryTypeDef"
    serverGroups: List["ServerGroupTypeDef"]
    tags: List["TagTypeDef"]


class CreateReplicationJobResponseTypeDef(TypedDict, total=False):
    replicationJobId: str


class GenerateChangeSetResponseTypeDef(TypedDict, total=False):
    s3Location: "S3LocationTypeDef"


class GenerateTemplateResponseTypeDef(TypedDict, total=False):
    s3Location: "S3LocationTypeDef"


class GetAppLaunchConfigurationResponseTypeDef(TypedDict, total=False):
    appId: str
    roleName: str
    autoLaunch: bool
    serverGroupLaunchConfigurations: List["ServerGroupLaunchConfigurationTypeDef"]


class GetAppReplicationConfigurationResponseTypeDef(TypedDict, total=False):
    serverGroupReplicationConfigurations: List["ServerGroupReplicationConfigurationTypeDef"]


class GetAppResponseTypeDef(TypedDict, total=False):
    appSummary: "AppSummaryTypeDef"
    serverGroups: List["ServerGroupTypeDef"]
    tags: List["TagTypeDef"]


class GetAppValidationConfigurationResponseTypeDef(TypedDict, total=False):
    appValidationConfigurations: List["AppValidationConfigurationTypeDef"]
    serverGroupValidationConfigurations: List["ServerGroupValidationConfigurationTypeDef"]


class GetAppValidationOutputResponseTypeDef(TypedDict, total=False):
    validationOutputList: List["ValidationOutputTypeDef"]


class GetConnectorsResponseTypeDef(TypedDict, total=False):
    connectorList: List["ConnectorTypeDef"]
    nextToken: str


class GetReplicationJobsResponseTypeDef(TypedDict, total=False):
    replicationJobList: List["ReplicationJobTypeDef"]
    nextToken: str


class GetReplicationRunsResponseTypeDef(TypedDict, total=False):
    replicationJob: "ReplicationJobTypeDef"
    replicationRunList: List["ReplicationRunTypeDef"]
    nextToken: str


class GetServersResponseTypeDef(TypedDict, total=False):
    lastModifiedOn: datetime
    serverCatalogStatus: ServerCatalogStatus
    serverList: List["ServerTypeDef"]
    nextToken: str


class LaunchDetailsTypeDef(TypedDict, total=False):
    latestLaunchTime: datetime
    stackName: str
    stackId: str


class ListAppsResponseTypeDef(TypedDict, total=False):
    apps: List["AppSummaryTypeDef"]
    nextToken: str


class NotificationContextTypeDef(TypedDict, total=False):
    validationId: str
    status: ValidationStatus
    statusMessage: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ReplicationJobTypeDef(TypedDict, total=False):
    replicationJobId: str
    serverId: str
    serverType: Literal["VIRTUAL_MACHINE"]
    vmServer: "VmServerTypeDef"
    seedReplicationTime: datetime
    frequency: int
    runOnce: bool
    nextReplicationRunStartTime: datetime
    licenseType: LicenseType
    roleName: str
    latestAmiId: str
    state: ReplicationJobState
    statusMessage: str
    description: str
    numberOfRecentAmisToKeep: int
    encrypted: bool
    kmsKeyId: str
    replicationRunList: List["ReplicationRunTypeDef"]


class ReplicationRunStageDetailsTypeDef(TypedDict, total=False):
    stage: str
    stageProgress: str


ReplicationRunTypeDef = TypedDict(
    "ReplicationRunTypeDef",
    {
        "replicationRunId": str,
        "state": ReplicationRunState,
        "type": ReplicationRunType,
        "stageDetails": "ReplicationRunStageDetailsTypeDef",
        "statusMessage": str,
        "amiId": str,
        "scheduledStartTime": datetime,
        "completedTime": datetime,
        "description": str,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class S3LocationTypeDef(TypedDict, total=False):
    bucket: str
    key: str


class SSMOutputTypeDef(TypedDict):
    s3Location: "S3LocationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class SSMValidationParametersTypeDef(TypedDict, total=False):
    source: "SourceTypeDef"
    instanceId: str
    scriptType: ScriptType
    command: str
    executionTimeoutSeconds: int
    outputS3BucketName: str


class ServerGroupLaunchConfigurationTypeDef(TypedDict, total=False):
    serverGroupId: str
    launchOrder: int
    serverLaunchConfigurations: List["ServerLaunchConfigurationTypeDef"]


class ServerGroupReplicationConfigurationTypeDef(TypedDict, total=False):
    serverGroupId: str
    serverReplicationConfigurations: List["ServerReplicationConfigurationTypeDef"]


class ServerGroupTypeDef(TypedDict, total=False):
    serverGroupId: str
    name: str
    serverList: List["ServerTypeDef"]


class ServerGroupValidationConfigurationTypeDef(TypedDict, total=False):
    serverGroupId: str
    serverValidationConfigurations: List["ServerValidationConfigurationTypeDef"]


class ServerLaunchConfigurationTypeDef(TypedDict, total=False):
    server: "ServerTypeDef"
    logicalId: str
    vpc: str
    subnet: str
    securityGroup: str
    ec2KeyName: str
    userData: "UserDataTypeDef"
    instanceType: str
    associatePublicIpAddress: bool
    iamInstanceProfileName: str
    configureScript: "S3LocationTypeDef"
    configureScriptType: ScriptType


class ServerReplicationConfigurationTypeDef(TypedDict, total=False):
    server: "ServerTypeDef"
    serverReplicationParameters: "ServerReplicationParametersTypeDef"


class ServerReplicationParametersTypeDef(TypedDict, total=False):
    seedTime: datetime
    frequency: int
    runOnce: bool
    licenseType: LicenseType
    numberOfRecentAmisToKeep: int
    encrypted: bool
    kmsKeyId: str


class ServerTypeDef(TypedDict, total=False):
    serverId: str
    serverType: Literal["VIRTUAL_MACHINE"]
    vmServer: "VmServerTypeDef"
    replicationJobId: str
    replicationJobTerminated: bool


class ServerValidationConfigurationTypeDef(TypedDict, total=False):
    server: "ServerTypeDef"
    validationId: str
    name: str
    serverValidationStrategy: Literal["USERDATA"]
    userDataValidationParameters: "UserDataValidationParametersTypeDef"


class ServerValidationOutputTypeDef(TypedDict):
    server: "ServerTypeDef"
    ResponseMetadata: "ResponseMetadata"


class SourceTypeDef(TypedDict, total=False):
    s3Location: "S3LocationTypeDef"


class StartOnDemandReplicationRunResponseTypeDef(TypedDict, total=False):
    replicationRunId: str


class TagTypeDef(TypedDict, total=False):
    key: str
    value: str


class UpdateAppResponseTypeDef(TypedDict, total=False):
    appSummary: "AppSummaryTypeDef"
    serverGroups: List["ServerGroupTypeDef"]
    tags: List["TagTypeDef"]


class UserDataTypeDef(TypedDict, total=False):
    s3Location: "S3LocationTypeDef"


class UserDataValidationParametersTypeDef(TypedDict, total=False):
    source: "SourceTypeDef"
    scriptType: ScriptType


class ValidationOutputTypeDef(TypedDict):
    validationId: str
    name: str
    status: ValidationStatus
    statusMessage: str
    latestValidationTime: datetime
    appValidationOutput: "AppValidationOutputTypeDef"
    serverValidationOutput: "ServerValidationOutputTypeDef"
    ResponseMetadata: "ResponseMetadata"


class VmServerAddressTypeDef(TypedDict, total=False):
    vmManagerId: str
    vmId: str


class VmServerTypeDef(TypedDict, total=False):
    vmServerAddress: "VmServerAddressTypeDef"
    vmName: str
    vmManagerName: str
    vmManagerType: VmManagerType
    vmPath: str
