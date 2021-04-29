"""
Main interface for sms service type definitions.

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
    AppValidationStrategy,
    ConnectorCapability,
    ConnectorStatus,
    LicenseType,
    ReplicationJobState,
    ReplicationRunState,
    ReplicationRunType,
    ScriptType,
    ServerCatalogStatus,
    ServerType,
    ServerValidationStrategy,
    ValidationStatus,
    VmManagerType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AppSummaryTypeDef",
    "AppValidationConfigurationTypeDef",
    "AppValidationOutputTypeDef",
    "ConnectorTypeDef",
    "LaunchDetailsTypeDef",
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
    "TagTypeDef",
    "UserDataTypeDef",
    "UserDataValidationParametersTypeDef",
    "ValidationOutputTypeDef",
    "VmServerAddressTypeDef",
    "VmServerTypeDef",
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
    "ListAppsResponseTypeDef",
    "NotificationContextTypeDef",
    "PaginatorConfigTypeDef",
    "StartOnDemandReplicationRunResponseTypeDef",
    "UpdateAppResponseTypeDef",
)

AppSummaryTypeDef = TypedDict(
    "AppSummaryTypeDef",
    {
        "appId": str,
        "importedAppId": str,
        "name": str,
        "description": str,
        "status": AppStatus,
        "statusMessage": str,
        "replicationConfigurationStatus": AppReplicationConfigurationStatus,
        "replicationStatus": AppReplicationStatus,
        "replicationStatusMessage": str,
        "latestReplicationTime": datetime,
        "launchConfigurationStatus": AppLaunchConfigurationStatus,
        "launchStatus": AppLaunchStatus,
        "launchStatusMessage": str,
        "launchDetails": "LaunchDetailsTypeDef",
        "creationTime": datetime,
        "lastModified": datetime,
        "roleName": str,
        "totalServerGroups": int,
        "totalServers": int,
    },
    total=False,
)

AppValidationConfigurationTypeDef = TypedDict(
    "AppValidationConfigurationTypeDef",
    {
        "validationId": str,
        "name": str,
        "appValidationStrategy": AppValidationStrategy,
        "ssmValidationParameters": "SSMValidationParametersTypeDef",
    },
    total=False,
)

AppValidationOutputTypeDef = TypedDict(
    "AppValidationOutputTypeDef",
    {"ssmOutput": "SSMOutputTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ConnectorTypeDef = TypedDict(
    "ConnectorTypeDef",
    {
        "connectorId": str,
        "version": str,
        "status": ConnectorStatus,
        "capabilityList": List[ConnectorCapability],
        "vmManagerName": str,
        "vmManagerType": VmManagerType,
        "vmManagerId": str,
        "ipAddress": str,
        "macAddress": str,
        "associatedOn": datetime,
    },
    total=False,
)

LaunchDetailsTypeDef = TypedDict(
    "LaunchDetailsTypeDef",
    {"latestLaunchTime": datetime, "stackName": str, "stackId": str},
    total=False,
)

ReplicationJobTypeDef = TypedDict(
    "ReplicationJobTypeDef",
    {
        "replicationJobId": str,
        "serverId": str,
        "serverType": ServerType,
        "vmServer": "VmServerTypeDef",
        "seedReplicationTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "nextReplicationRunStartTime": datetime,
        "licenseType": LicenseType,
        "roleName": str,
        "latestAmiId": str,
        "state": ReplicationJobState,
        "statusMessage": str,
        "description": str,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
        "replicationRunList": List["ReplicationRunTypeDef"],
    },
    total=False,
)

ReplicationRunStageDetailsTypeDef = TypedDict(
    "ReplicationRunStageDetailsTypeDef", {"stage": str, "stageProgress": str}, total=False
)

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

S3LocationTypeDef = TypedDict("S3LocationTypeDef", {"bucket": str, "key": str}, total=False)

SSMOutputTypeDef = TypedDict(
    "SSMOutputTypeDef",
    {"s3Location": "S3LocationTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

SSMValidationParametersTypeDef = TypedDict(
    "SSMValidationParametersTypeDef",
    {
        "source": "SourceTypeDef",
        "instanceId": str,
        "scriptType": ScriptType,
        "command": str,
        "executionTimeoutSeconds": int,
        "outputS3BucketName": str,
    },
    total=False,
)

ServerGroupLaunchConfigurationTypeDef = TypedDict(
    "ServerGroupLaunchConfigurationTypeDef",
    {
        "serverGroupId": str,
        "launchOrder": int,
        "serverLaunchConfigurations": List["ServerLaunchConfigurationTypeDef"],
    },
    total=False,
)

ServerGroupReplicationConfigurationTypeDef = TypedDict(
    "ServerGroupReplicationConfigurationTypeDef",
    {
        "serverGroupId": str,
        "serverReplicationConfigurations": List["ServerReplicationConfigurationTypeDef"],
    },
    total=False,
)

ServerGroupTypeDef = TypedDict(
    "ServerGroupTypeDef",
    {"serverGroupId": str, "name": str, "serverList": List["ServerTypeDef"]},
    total=False,
)

ServerGroupValidationConfigurationTypeDef = TypedDict(
    "ServerGroupValidationConfigurationTypeDef",
    {
        "serverGroupId": str,
        "serverValidationConfigurations": List["ServerValidationConfigurationTypeDef"],
    },
    total=False,
)

ServerLaunchConfigurationTypeDef = TypedDict(
    "ServerLaunchConfigurationTypeDef",
    {
        "server": "ServerTypeDef",
        "logicalId": str,
        "vpc": str,
        "subnet": str,
        "securityGroup": str,
        "ec2KeyName": str,
        "userData": "UserDataTypeDef",
        "instanceType": str,
        "associatePublicIpAddress": bool,
        "iamInstanceProfileName": str,
        "configureScript": "S3LocationTypeDef",
        "configureScriptType": ScriptType,
    },
    total=False,
)

ServerReplicationConfigurationTypeDef = TypedDict(
    "ServerReplicationConfigurationTypeDef",
    {
        "server": "ServerTypeDef",
        "serverReplicationParameters": "ServerReplicationParametersTypeDef",
    },
    total=False,
)

ServerReplicationParametersTypeDef = TypedDict(
    "ServerReplicationParametersTypeDef",
    {
        "seedTime": datetime,
        "frequency": int,
        "runOnce": bool,
        "licenseType": LicenseType,
        "numberOfRecentAmisToKeep": int,
        "encrypted": bool,
        "kmsKeyId": str,
    },
    total=False,
)

ServerTypeDef = TypedDict(
    "ServerTypeDef",
    {
        "serverId": str,
        "serverType": ServerType,
        "vmServer": "VmServerTypeDef",
        "replicationJobId": str,
        "replicationJobTerminated": bool,
    },
    total=False,
)

ServerValidationConfigurationTypeDef = TypedDict(
    "ServerValidationConfigurationTypeDef",
    {
        "server": "ServerTypeDef",
        "validationId": str,
        "name": str,
        "serverValidationStrategy": ServerValidationStrategy,
        "userDataValidationParameters": "UserDataValidationParametersTypeDef",
    },
    total=False,
)

ServerValidationOutputTypeDef = TypedDict(
    "ServerValidationOutputTypeDef",
    {"server": "ServerTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

SourceTypeDef = TypedDict("SourceTypeDef", {"s3Location": "S3LocationTypeDef"}, total=False)

TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str}, total=False)

UserDataTypeDef = TypedDict("UserDataTypeDef", {"s3Location": "S3LocationTypeDef"}, total=False)

UserDataValidationParametersTypeDef = TypedDict(
    "UserDataValidationParametersTypeDef",
    {"source": "SourceTypeDef", "scriptType": ScriptType},
    total=False,
)

ValidationOutputTypeDef = TypedDict(
    "ValidationOutputTypeDef",
    {
        "validationId": str,
        "name": str,
        "status": ValidationStatus,
        "statusMessage": str,
        "latestValidationTime": datetime,
        "appValidationOutput": "AppValidationOutputTypeDef",
        "serverValidationOutput": "ServerValidationOutputTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

VmServerAddressTypeDef = TypedDict(
    "VmServerAddressTypeDef", {"vmManagerId": str, "vmId": str}, total=False
)

VmServerTypeDef = TypedDict(
    "VmServerTypeDef",
    {
        "vmServerAddress": "VmServerAddressTypeDef",
        "vmName": str,
        "vmManagerName": str,
        "vmManagerType": VmManagerType,
        "vmPath": str,
    },
    total=False,
)

CreateAppResponseTypeDef = TypedDict(
    "CreateAppResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

CreateReplicationJobResponseTypeDef = TypedDict(
    "CreateReplicationJobResponseTypeDef", {"replicationJobId": str}, total=False
)

GenerateChangeSetResponseTypeDef = TypedDict(
    "GenerateChangeSetResponseTypeDef", {"s3Location": "S3LocationTypeDef"}, total=False
)

GenerateTemplateResponseTypeDef = TypedDict(
    "GenerateTemplateResponseTypeDef", {"s3Location": "S3LocationTypeDef"}, total=False
)

GetAppLaunchConfigurationResponseTypeDef = TypedDict(
    "GetAppLaunchConfigurationResponseTypeDef",
    {
        "appId": str,
        "roleName": str,
        "autoLaunch": bool,
        "serverGroupLaunchConfigurations": List["ServerGroupLaunchConfigurationTypeDef"],
    },
    total=False,
)

GetAppReplicationConfigurationResponseTypeDef = TypedDict(
    "GetAppReplicationConfigurationResponseTypeDef",
    {"serverGroupReplicationConfigurations": List["ServerGroupReplicationConfigurationTypeDef"]},
    total=False,
)

GetAppResponseTypeDef = TypedDict(
    "GetAppResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)

GetAppValidationConfigurationResponseTypeDef = TypedDict(
    "GetAppValidationConfigurationResponseTypeDef",
    {
        "appValidationConfigurations": List["AppValidationConfigurationTypeDef"],
        "serverGroupValidationConfigurations": List["ServerGroupValidationConfigurationTypeDef"],
    },
    total=False,
)

GetAppValidationOutputResponseTypeDef = TypedDict(
    "GetAppValidationOutputResponseTypeDef",
    {"validationOutputList": List["ValidationOutputTypeDef"]},
    total=False,
)

GetConnectorsResponseTypeDef = TypedDict(
    "GetConnectorsResponseTypeDef",
    {"connectorList": List["ConnectorTypeDef"], "nextToken": str},
    total=False,
)

GetReplicationJobsResponseTypeDef = TypedDict(
    "GetReplicationJobsResponseTypeDef",
    {"replicationJobList": List["ReplicationJobTypeDef"], "nextToken": str},
    total=False,
)

GetReplicationRunsResponseTypeDef = TypedDict(
    "GetReplicationRunsResponseTypeDef",
    {
        "replicationJob": "ReplicationJobTypeDef",
        "replicationRunList": List["ReplicationRunTypeDef"],
        "nextToken": str,
    },
    total=False,
)

GetServersResponseTypeDef = TypedDict(
    "GetServersResponseTypeDef",
    {
        "lastModifiedOn": datetime,
        "serverCatalogStatus": ServerCatalogStatus,
        "serverList": List["ServerTypeDef"],
        "nextToken": str,
    },
    total=False,
)

ListAppsResponseTypeDef = TypedDict(
    "ListAppsResponseTypeDef", {"apps": List["AppSummaryTypeDef"], "nextToken": str}, total=False
)

NotificationContextTypeDef = TypedDict(
    "NotificationContextTypeDef",
    {"validationId": str, "status": ValidationStatus, "statusMessage": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartOnDemandReplicationRunResponseTypeDef = TypedDict(
    "StartOnDemandReplicationRunResponseTypeDef", {"replicationRunId": str}, total=False
)

UpdateAppResponseTypeDef = TypedDict(
    "UpdateAppResponseTypeDef",
    {
        "appSummary": "AppSummaryTypeDef",
        "serverGroups": List["ServerGroupTypeDef"],
        "tags": List["TagTypeDef"],
    },
    total=False,
)
