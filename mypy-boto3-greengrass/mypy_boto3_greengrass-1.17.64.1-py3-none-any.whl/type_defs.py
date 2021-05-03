"""
Type annotations for greengrass service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_greengrass/type_defs.html)

Usage::

    ```python
    from mypy_boto3_greengrass.type_defs import AssociateRoleToGroupResponseTypeDef

    data: AssociateRoleToGroupResponseTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_greengrass.literals import (
    BulkDeploymentStatus,
    ConfigurationSyncStatus,
    DeploymentType,
    EncodingType,
    FunctionIsolationMode,
    LoggerComponent,
    LoggerLevel,
    LoggerType,
    Permission,
    Telemetry,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateRoleToGroupResponseTypeDef",
    "AssociateServiceRoleToAccountResponseTypeDef",
    "BulkDeploymentMetricsTypeDef",
    "BulkDeploymentResultTypeDef",
    "BulkDeploymentTypeDef",
    "ConnectivityInfoTypeDef",
    "ConnectorDefinitionVersionTypeDef",
    "ConnectorTypeDef",
    "CoreDefinitionVersionTypeDef",
    "CoreTypeDef",
    "CreateConnectorDefinitionResponseTypeDef",
    "CreateConnectorDefinitionVersionResponseTypeDef",
    "CreateCoreDefinitionResponseTypeDef",
    "CreateCoreDefinitionVersionResponseTypeDef",
    "CreateDeploymentResponseTypeDef",
    "CreateDeviceDefinitionResponseTypeDef",
    "CreateDeviceDefinitionVersionResponseTypeDef",
    "CreateFunctionDefinitionResponseTypeDef",
    "CreateFunctionDefinitionVersionResponseTypeDef",
    "CreateGroupCertificateAuthorityResponseTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateGroupVersionResponseTypeDef",
    "CreateLoggerDefinitionResponseTypeDef",
    "CreateLoggerDefinitionVersionResponseTypeDef",
    "CreateResourceDefinitionResponseTypeDef",
    "CreateResourceDefinitionVersionResponseTypeDef",
    "CreateSoftwareUpdateJobResponseTypeDef",
    "CreateSubscriptionDefinitionResponseTypeDef",
    "CreateSubscriptionDefinitionVersionResponseTypeDef",
    "DefinitionInformationTypeDef",
    "DeploymentTypeDef",
    "DeviceDefinitionVersionTypeDef",
    "DeviceTypeDef",
    "DisassociateRoleFromGroupResponseTypeDef",
    "DisassociateServiceRoleFromAccountResponseTypeDef",
    "ErrorDetailTypeDef",
    "FunctionConfigurationEnvironmentTypeDef",
    "FunctionConfigurationTypeDef",
    "FunctionDefaultConfigTypeDef",
    "FunctionDefaultExecutionConfigTypeDef",
    "FunctionDefinitionVersionTypeDef",
    "FunctionExecutionConfigTypeDef",
    "FunctionRunAsConfigTypeDef",
    "FunctionTypeDef",
    "GetAssociatedRoleResponseTypeDef",
    "GetBulkDeploymentStatusResponseTypeDef",
    "GetConnectivityInfoResponseTypeDef",
    "GetConnectorDefinitionResponseTypeDef",
    "GetConnectorDefinitionVersionResponseTypeDef",
    "GetCoreDefinitionResponseTypeDef",
    "GetCoreDefinitionVersionResponseTypeDef",
    "GetDeploymentStatusResponseTypeDef",
    "GetDeviceDefinitionResponseTypeDef",
    "GetDeviceDefinitionVersionResponseTypeDef",
    "GetFunctionDefinitionResponseTypeDef",
    "GetFunctionDefinitionVersionResponseTypeDef",
    "GetGroupCertificateAuthorityResponseTypeDef",
    "GetGroupCertificateConfigurationResponseTypeDef",
    "GetGroupResponseTypeDef",
    "GetGroupVersionResponseTypeDef",
    "GetLoggerDefinitionResponseTypeDef",
    "GetLoggerDefinitionVersionResponseTypeDef",
    "GetResourceDefinitionResponseTypeDef",
    "GetResourceDefinitionVersionResponseTypeDef",
    "GetServiceRoleForAccountResponseTypeDef",
    "GetSubscriptionDefinitionResponseTypeDef",
    "GetSubscriptionDefinitionVersionResponseTypeDef",
    "GetThingRuntimeConfigurationResponseTypeDef",
    "GroupCertificateAuthorityPropertiesTypeDef",
    "GroupInformationTypeDef",
    "GroupOwnerSettingTypeDef",
    "GroupVersionTypeDef",
    "ListBulkDeploymentDetailedReportsResponseTypeDef",
    "ListBulkDeploymentsResponseTypeDef",
    "ListConnectorDefinitionVersionsResponseTypeDef",
    "ListConnectorDefinitionsResponseTypeDef",
    "ListCoreDefinitionVersionsResponseTypeDef",
    "ListCoreDefinitionsResponseTypeDef",
    "ListDeploymentsResponseTypeDef",
    "ListDeviceDefinitionVersionsResponseTypeDef",
    "ListDeviceDefinitionsResponseTypeDef",
    "ListFunctionDefinitionVersionsResponseTypeDef",
    "ListFunctionDefinitionsResponseTypeDef",
    "ListGroupCertificateAuthoritiesResponseTypeDef",
    "ListGroupVersionsResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListLoggerDefinitionVersionsResponseTypeDef",
    "ListLoggerDefinitionsResponseTypeDef",
    "ListResourceDefinitionVersionsResponseTypeDef",
    "ListResourceDefinitionsResponseTypeDef",
    "ListSubscriptionDefinitionVersionsResponseTypeDef",
    "ListSubscriptionDefinitionsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocalDeviceResourceDataTypeDef",
    "LocalVolumeResourceDataTypeDef",
    "LoggerDefinitionVersionTypeDef",
    "LoggerTypeDef",
    "PaginatorConfigTypeDef",
    "ResetDeploymentsResponseTypeDef",
    "ResourceAccessPolicyTypeDef",
    "ResourceDataContainerTypeDef",
    "ResourceDefinitionVersionTypeDef",
    "ResourceDownloadOwnerSettingTypeDef",
    "ResourceTypeDef",
    "RuntimeConfigurationTypeDef",
    "S3MachineLearningModelResourceDataTypeDef",
    "SageMakerMachineLearningModelResourceDataTypeDef",
    "SecretsManagerSecretResourceDataTypeDef",
    "StartBulkDeploymentResponseTypeDef",
    "SubscriptionDefinitionVersionTypeDef",
    "SubscriptionTypeDef",
    "TelemetryConfigurationTypeDef",
    "TelemetryConfigurationUpdateTypeDef",
    "UpdateConnectivityInfoResponseTypeDef",
    "UpdateGroupCertificateConfigurationResponseTypeDef",
    "VersionInformationTypeDef",
)


class AssociateRoleToGroupResponseTypeDef(TypedDict, total=False):
    AssociatedAt: str


class AssociateServiceRoleToAccountResponseTypeDef(TypedDict, total=False):
    AssociatedAt: str


class BulkDeploymentMetricsTypeDef(TypedDict, total=False):
    InvalidInputRecords: int
    RecordsProcessed: int
    RetryAttempts: int


class BulkDeploymentResultTypeDef(TypedDict, total=False):
    CreatedAt: str
    DeploymentArn: str
    DeploymentId: str
    DeploymentStatus: str
    DeploymentType: DeploymentType
    ErrorDetails: List["ErrorDetailTypeDef"]
    ErrorMessage: str
    GroupArn: str


class BulkDeploymentTypeDef(TypedDict, total=False):
    BulkDeploymentArn: str
    BulkDeploymentId: str
    CreatedAt: str


class ConnectivityInfoTypeDef(TypedDict, total=False):
    HostAddress: str
    Id: str
    Metadata: str
    PortNumber: int


class ConnectorDefinitionVersionTypeDef(TypedDict, total=False):
    Connectors: List["ConnectorTypeDef"]


class _RequiredConnectorTypeDef(TypedDict):
    ConnectorArn: str
    Id: str


class ConnectorTypeDef(_RequiredConnectorTypeDef, total=False):
    Parameters: Dict[str, str]


class CoreDefinitionVersionTypeDef(TypedDict, total=False):
    Cores: List["CoreTypeDef"]


class _RequiredCoreTypeDef(TypedDict):
    CertificateArn: str
    Id: str
    ThingArn: str


class CoreTypeDef(_RequiredCoreTypeDef, total=False):
    SyncShadow: bool


class CreateConnectorDefinitionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str


class CreateConnectorDefinitionVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str


class CreateCoreDefinitionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str


class CreateCoreDefinitionVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str


class CreateDeploymentResponseTypeDef(TypedDict, total=False):
    DeploymentArn: str
    DeploymentId: str


class CreateDeviceDefinitionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str


class CreateDeviceDefinitionVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str


class CreateFunctionDefinitionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str


class CreateFunctionDefinitionVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str


class CreateGroupCertificateAuthorityResponseTypeDef(TypedDict, total=False):
    GroupCertificateAuthorityArn: str


class CreateGroupResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str


class CreateGroupVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str


class CreateLoggerDefinitionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str


class CreateLoggerDefinitionVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str


class CreateResourceDefinitionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str


class CreateResourceDefinitionVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str


class CreateSoftwareUpdateJobResponseTypeDef(TypedDict, total=False):
    IotJobArn: str
    IotJobId: str
    PlatformSoftwareVersion: str


class CreateSubscriptionDefinitionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str


class CreateSubscriptionDefinitionVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str


class DefinitionInformationTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    Tags: Dict[str, str]


class DeploymentTypeDef(TypedDict, total=False):
    CreatedAt: str
    DeploymentArn: str
    DeploymentId: str
    DeploymentType: DeploymentType
    GroupArn: str


class DeviceDefinitionVersionTypeDef(TypedDict, total=False):
    Devices: List["DeviceTypeDef"]


class _RequiredDeviceTypeDef(TypedDict):
    CertificateArn: str
    Id: str
    ThingArn: str


class DeviceTypeDef(_RequiredDeviceTypeDef, total=False):
    SyncShadow: bool


class DisassociateRoleFromGroupResponseTypeDef(TypedDict, total=False):
    DisassociatedAt: str


class DisassociateServiceRoleFromAccountResponseTypeDef(TypedDict, total=False):
    DisassociatedAt: str


class ErrorDetailTypeDef(TypedDict, total=False):
    DetailedErrorCode: str
    DetailedErrorMessage: str


class FunctionConfigurationEnvironmentTypeDef(TypedDict, total=False):
    AccessSysfs: bool
    Execution: "FunctionExecutionConfigTypeDef"
    ResourceAccessPolicies: List["ResourceAccessPolicyTypeDef"]
    Variables: Dict[str, str]


class FunctionConfigurationTypeDef(TypedDict, total=False):
    EncodingType: EncodingType
    Environment: "FunctionConfigurationEnvironmentTypeDef"
    ExecArgs: str
    Executable: str
    MemorySize: int
    Pinned: bool
    Timeout: int


class FunctionDefaultConfigTypeDef(TypedDict, total=False):
    Execution: "FunctionDefaultExecutionConfigTypeDef"


class FunctionDefaultExecutionConfigTypeDef(TypedDict, total=False):
    IsolationMode: FunctionIsolationMode
    RunAs: "FunctionRunAsConfigTypeDef"


class FunctionDefinitionVersionTypeDef(TypedDict, total=False):
    DefaultConfig: "FunctionDefaultConfigTypeDef"
    Functions: List["FunctionTypeDef"]


class FunctionExecutionConfigTypeDef(TypedDict, total=False):
    IsolationMode: FunctionIsolationMode
    RunAs: "FunctionRunAsConfigTypeDef"


class FunctionRunAsConfigTypeDef(TypedDict, total=False):
    Gid: int
    Uid: int


class _RequiredFunctionTypeDef(TypedDict):
    Id: str


class FunctionTypeDef(_RequiredFunctionTypeDef, total=False):
    FunctionArn: str
    FunctionConfiguration: "FunctionConfigurationTypeDef"


class GetAssociatedRoleResponseTypeDef(TypedDict, total=False):
    AssociatedAt: str
    RoleArn: str


class GetBulkDeploymentStatusResponseTypeDef(TypedDict, total=False):
    BulkDeploymentMetrics: "BulkDeploymentMetricsTypeDef"
    BulkDeploymentStatus: BulkDeploymentStatus
    CreatedAt: str
    ErrorDetails: List["ErrorDetailTypeDef"]
    ErrorMessage: str
    tags: Dict[str, str]


class GetConnectivityInfoResponseTypeDef(TypedDict, total=False):
    ConnectivityInfo: List["ConnectivityInfoTypeDef"]
    Message: str


class GetConnectorDefinitionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]


class GetConnectorDefinitionVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Definition: "ConnectorDefinitionVersionTypeDef"
    Id: str
    NextToken: str
    Version: str


class GetCoreDefinitionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]


class GetCoreDefinitionVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Definition: "CoreDefinitionVersionTypeDef"
    Id: str
    NextToken: str
    Version: str


class GetDeploymentStatusResponseTypeDef(TypedDict, total=False):
    DeploymentStatus: str
    DeploymentType: DeploymentType
    ErrorDetails: List["ErrorDetailTypeDef"]
    ErrorMessage: str
    UpdatedAt: str


class GetDeviceDefinitionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]


class GetDeviceDefinitionVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Definition: "DeviceDefinitionVersionTypeDef"
    Id: str
    NextToken: str
    Version: str


class GetFunctionDefinitionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]


class GetFunctionDefinitionVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Definition: "FunctionDefinitionVersionTypeDef"
    Id: str
    NextToken: str
    Version: str


class GetGroupCertificateAuthorityResponseTypeDef(TypedDict, total=False):
    GroupCertificateAuthorityArn: str
    GroupCertificateAuthorityId: str
    PemEncodedCertificate: str


class GetGroupCertificateConfigurationResponseTypeDef(TypedDict, total=False):
    CertificateAuthorityExpiryInMilliseconds: str
    CertificateExpiryInMilliseconds: str
    GroupId: str


class GetGroupResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]


class GetGroupVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Definition: "GroupVersionTypeDef"
    Id: str
    Version: str


class GetLoggerDefinitionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]


class GetLoggerDefinitionVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Definition: "LoggerDefinitionVersionTypeDef"
    Id: str
    Version: str


class GetResourceDefinitionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]


class GetResourceDefinitionVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Definition: "ResourceDefinitionVersionTypeDef"
    Id: str
    Version: str


class GetServiceRoleForAccountResponseTypeDef(TypedDict, total=False):
    AssociatedAt: str
    RoleArn: str


class GetSubscriptionDefinitionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str
    tags: Dict[str, str]


class GetSubscriptionDefinitionVersionResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Definition: "SubscriptionDefinitionVersionTypeDef"
    Id: str
    NextToken: str
    Version: str


class GetThingRuntimeConfigurationResponseTypeDef(TypedDict, total=False):
    RuntimeConfiguration: "RuntimeConfigurationTypeDef"


class GroupCertificateAuthorityPropertiesTypeDef(TypedDict, total=False):
    GroupCertificateAuthorityArn: str
    GroupCertificateAuthorityId: str


class GroupInformationTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    LastUpdatedTimestamp: str
    LatestVersion: str
    LatestVersionArn: str
    Name: str


class GroupOwnerSettingTypeDef(TypedDict, total=False):
    AutoAddGroupOwner: bool
    GroupOwner: str


class GroupVersionTypeDef(TypedDict, total=False):
    ConnectorDefinitionVersionArn: str
    CoreDefinitionVersionArn: str
    DeviceDefinitionVersionArn: str
    FunctionDefinitionVersionArn: str
    LoggerDefinitionVersionArn: str
    ResourceDefinitionVersionArn: str
    SubscriptionDefinitionVersionArn: str


class ListBulkDeploymentDetailedReportsResponseTypeDef(TypedDict, total=False):
    Deployments: List["BulkDeploymentResultTypeDef"]
    NextToken: str


class ListBulkDeploymentsResponseTypeDef(TypedDict, total=False):
    BulkDeployments: List["BulkDeploymentTypeDef"]
    NextToken: str


class ListConnectorDefinitionVersionsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Versions: List["VersionInformationTypeDef"]


class ListConnectorDefinitionsResponseTypeDef(TypedDict, total=False):
    Definitions: List["DefinitionInformationTypeDef"]
    NextToken: str


class ListCoreDefinitionVersionsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Versions: List["VersionInformationTypeDef"]


class ListCoreDefinitionsResponseTypeDef(TypedDict, total=False):
    Definitions: List["DefinitionInformationTypeDef"]
    NextToken: str


class ListDeploymentsResponseTypeDef(TypedDict, total=False):
    Deployments: List["DeploymentTypeDef"]
    NextToken: str


class ListDeviceDefinitionVersionsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Versions: List["VersionInformationTypeDef"]


class ListDeviceDefinitionsResponseTypeDef(TypedDict, total=False):
    Definitions: List["DefinitionInformationTypeDef"]
    NextToken: str


class ListFunctionDefinitionVersionsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Versions: List["VersionInformationTypeDef"]


class ListFunctionDefinitionsResponseTypeDef(TypedDict, total=False):
    Definitions: List["DefinitionInformationTypeDef"]
    NextToken: str


class ListGroupCertificateAuthoritiesResponseTypeDef(TypedDict, total=False):
    GroupCertificateAuthorities: List["GroupCertificateAuthorityPropertiesTypeDef"]


class ListGroupVersionsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Versions: List["VersionInformationTypeDef"]


class ListGroupsResponseTypeDef(TypedDict, total=False):
    Groups: List["GroupInformationTypeDef"]
    NextToken: str


class ListLoggerDefinitionVersionsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Versions: List["VersionInformationTypeDef"]


class ListLoggerDefinitionsResponseTypeDef(TypedDict, total=False):
    Definitions: List["DefinitionInformationTypeDef"]
    NextToken: str


class ListResourceDefinitionVersionsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Versions: List["VersionInformationTypeDef"]


class ListResourceDefinitionsResponseTypeDef(TypedDict, total=False):
    Definitions: List["DefinitionInformationTypeDef"]
    NextToken: str


class ListSubscriptionDefinitionVersionsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Versions: List["VersionInformationTypeDef"]


class ListSubscriptionDefinitionsResponseTypeDef(TypedDict, total=False):
    Definitions: List["DefinitionInformationTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class LocalDeviceResourceDataTypeDef(TypedDict, total=False):
    GroupOwnerSetting: "GroupOwnerSettingTypeDef"
    SourcePath: str


class LocalVolumeResourceDataTypeDef(TypedDict, total=False):
    DestinationPath: str
    GroupOwnerSetting: "GroupOwnerSettingTypeDef"
    SourcePath: str


class LoggerDefinitionVersionTypeDef(TypedDict, total=False):
    Loggers: List["LoggerTypeDef"]


_RequiredLoggerTypeDef = TypedDict(
    "_RequiredLoggerTypeDef",
    {"Component": LoggerComponent, "Id": str, "Level": LoggerLevel, "Type": LoggerType},
)
_OptionalLoggerTypeDef = TypedDict("_OptionalLoggerTypeDef", {"Space": int}, total=False)


class LoggerTypeDef(_RequiredLoggerTypeDef, _OptionalLoggerTypeDef):
    pass


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ResetDeploymentsResponseTypeDef(TypedDict, total=False):
    DeploymentArn: str
    DeploymentId: str


class _RequiredResourceAccessPolicyTypeDef(TypedDict):
    ResourceId: str


class ResourceAccessPolicyTypeDef(_RequiredResourceAccessPolicyTypeDef, total=False):
    Permission: Permission


class ResourceDataContainerTypeDef(TypedDict, total=False):
    LocalDeviceResourceData: "LocalDeviceResourceDataTypeDef"
    LocalVolumeResourceData: "LocalVolumeResourceDataTypeDef"
    S3MachineLearningModelResourceData: "S3MachineLearningModelResourceDataTypeDef"
    SageMakerMachineLearningModelResourceData: "SageMakerMachineLearningModelResourceDataTypeDef"
    SecretsManagerSecretResourceData: "SecretsManagerSecretResourceDataTypeDef"


class ResourceDefinitionVersionTypeDef(TypedDict, total=False):
    Resources: List["ResourceTypeDef"]


class ResourceDownloadOwnerSettingTypeDef(TypedDict):
    GroupOwner: str
    GroupPermission: Permission


class ResourceTypeDef(TypedDict):
    Id: str
    Name: str
    ResourceDataContainer: "ResourceDataContainerTypeDef"


class RuntimeConfigurationTypeDef(TypedDict, total=False):
    TelemetryConfiguration: "TelemetryConfigurationTypeDef"


class S3MachineLearningModelResourceDataTypeDef(TypedDict, total=False):
    DestinationPath: str
    OwnerSetting: "ResourceDownloadOwnerSettingTypeDef"
    S3Uri: str


class SageMakerMachineLearningModelResourceDataTypeDef(TypedDict, total=False):
    DestinationPath: str
    OwnerSetting: "ResourceDownloadOwnerSettingTypeDef"
    SageMakerJobArn: str


class SecretsManagerSecretResourceDataTypeDef(TypedDict, total=False):
    ARN: str
    AdditionalStagingLabelsToDownload: List[str]


class StartBulkDeploymentResponseTypeDef(TypedDict, total=False):
    BulkDeploymentArn: str
    BulkDeploymentId: str


class SubscriptionDefinitionVersionTypeDef(TypedDict, total=False):
    Subscriptions: List["SubscriptionTypeDef"]


class SubscriptionTypeDef(TypedDict):
    Id: str
    Source: str
    Subject: str
    Target: str


class _RequiredTelemetryConfigurationTypeDef(TypedDict):
    Telemetry: Telemetry


class TelemetryConfigurationTypeDef(_RequiredTelemetryConfigurationTypeDef, total=False):
    ConfigurationSyncStatus: ConfigurationSyncStatus


class TelemetryConfigurationUpdateTypeDef(TypedDict):
    Telemetry: Telemetry


class UpdateConnectivityInfoResponseTypeDef(TypedDict, total=False):
    Message: str
    Version: str


class UpdateGroupCertificateConfigurationResponseTypeDef(TypedDict, total=False):
    CertificateAuthorityExpiryInMilliseconds: str
    CertificateExpiryInMilliseconds: str
    GroupId: str


class VersionInformationTypeDef(TypedDict, total=False):
    Arn: str
    CreationTimestamp: str
    Id: str
    Version: str
