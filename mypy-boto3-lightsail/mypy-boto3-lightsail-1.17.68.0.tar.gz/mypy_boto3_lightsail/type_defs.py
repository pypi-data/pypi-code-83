"""
Type annotations for lightsail service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lightsail/type_defs.html)

Usage::

    ```python
    from mypy_boto3_lightsail.type_defs import AddOnRequestTypeDef

    data: AddOnRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_lightsail.literals import (
    AccessDirection,
    AlarmState,
    AutoSnapshotStatus,
    BehaviorEnum,
    BlueprintType,
    CertificateStatus,
    ComparisonOperator,
    ContactMethodStatus,
    ContactProtocol,
    ContainerServiceDeploymentState,
    ContainerServiceMetricName,
    ContainerServicePowerName,
    ContainerServiceProtocol,
    ContainerServiceState,
    ContainerServiceStateDetailCode,
    DiskSnapshotState,
    DiskState,
    DistributionMetricName,
    ExportSnapshotRecordSourceType,
    ForwardValues,
    HeaderEnum,
    InstanceAccessProtocol,
    InstanceHealthReason,
    InstanceHealthState,
    InstanceMetricName,
    InstancePlatform,
    InstanceSnapshotState,
    IpAddressType,
    LoadBalancerAttributeName,
    LoadBalancerMetricName,
    LoadBalancerProtocol,
    LoadBalancerState,
    LoadBalancerTlsCertificateDomainStatus,
    LoadBalancerTlsCertificateFailureReason,
    LoadBalancerTlsCertificateRenewalStatus,
    LoadBalancerTlsCertificateRevocationReason,
    LoadBalancerTlsCertificateStatus,
    MetricName,
    MetricStatistic,
    MetricUnit,
    NetworkProtocol,
    OperationStatus,
    OperationType,
    OriginProtocolPolicyEnum,
    PortAccessType,
    PortInfoSourceType,
    PortState,
    RecordState,
    RegionName,
    RelationalDatabaseMetricName,
    RenewalStatus,
    ResourceType,
    TreatMissingData,
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
    "AddOnRequestTypeDef",
    "AddOnTypeDef",
    "AlarmTypeDef",
    "AllocateStaticIpResultTypeDef",
    "AttachCertificateToDistributionResultTypeDef",
    "AttachDiskResultTypeDef",
    "AttachInstancesToLoadBalancerResultTypeDef",
    "AttachLoadBalancerTlsCertificateResultTypeDef",
    "AttachStaticIpResultTypeDef",
    "AttachedDiskTypeDef",
    "AutoSnapshotAddOnRequestTypeDef",
    "AutoSnapshotDetailsTypeDef",
    "AvailabilityZoneTypeDef",
    "BlueprintTypeDef",
    "BundleTypeDef",
    "CacheBehaviorPerPathTypeDef",
    "CacheBehaviorTypeDef",
    "CacheSettingsTypeDef",
    "CertificateSummaryTypeDef",
    "CertificateTypeDef",
    "CloseInstancePublicPortsResultTypeDef",
    "CloudFormationStackRecordSourceInfoTypeDef",
    "CloudFormationStackRecordTypeDef",
    "ContactMethodTypeDef",
    "ContainerImageTypeDef",
    "ContainerServiceDeploymentRequestTypeDef",
    "ContainerServiceDeploymentTypeDef",
    "ContainerServiceEndpointTypeDef",
    "ContainerServiceHealthCheckConfigTypeDef",
    "ContainerServiceLogEventTypeDef",
    "ContainerServicePowerTypeDef",
    "ContainerServiceRegistryLoginTypeDef",
    "ContainerServiceStateDetailTypeDef",
    "ContainerServiceTypeDef",
    "ContainerServicesListResultTypeDef",
    "ContainerTypeDef",
    "CookieObjectTypeDef",
    "CopySnapshotResultTypeDef",
    "CreateCertificateResultTypeDef",
    "CreateCloudFormationStackResultTypeDef",
    "CreateContactMethodResultTypeDef",
    "CreateContainerServiceDeploymentResultTypeDef",
    "CreateContainerServiceRegistryLoginResultTypeDef",
    "CreateContainerServiceResultTypeDef",
    "CreateDiskFromSnapshotResultTypeDef",
    "CreateDiskResultTypeDef",
    "CreateDiskSnapshotResultTypeDef",
    "CreateDistributionResultTypeDef",
    "CreateDomainEntryResultTypeDef",
    "CreateDomainResultTypeDef",
    "CreateInstanceSnapshotResultTypeDef",
    "CreateInstancesFromSnapshotResultTypeDef",
    "CreateInstancesResultTypeDef",
    "CreateKeyPairResultTypeDef",
    "CreateLoadBalancerResultTypeDef",
    "CreateLoadBalancerTlsCertificateResultTypeDef",
    "CreateRelationalDatabaseFromSnapshotResultTypeDef",
    "CreateRelationalDatabaseResultTypeDef",
    "CreateRelationalDatabaseSnapshotResultTypeDef",
    "DeleteAlarmResultTypeDef",
    "DeleteAutoSnapshotResultTypeDef",
    "DeleteCertificateResultTypeDef",
    "DeleteContactMethodResultTypeDef",
    "DeleteDiskResultTypeDef",
    "DeleteDiskSnapshotResultTypeDef",
    "DeleteDistributionResultTypeDef",
    "DeleteDomainEntryResultTypeDef",
    "DeleteDomainResultTypeDef",
    "DeleteInstanceResultTypeDef",
    "DeleteInstanceSnapshotResultTypeDef",
    "DeleteKeyPairResultTypeDef",
    "DeleteKnownHostKeysResultTypeDef",
    "DeleteLoadBalancerResultTypeDef",
    "DeleteLoadBalancerTlsCertificateResultTypeDef",
    "DeleteRelationalDatabaseResultTypeDef",
    "DeleteRelationalDatabaseSnapshotResultTypeDef",
    "DestinationInfoTypeDef",
    "DetachCertificateFromDistributionResultTypeDef",
    "DetachDiskResultTypeDef",
    "DetachInstancesFromLoadBalancerResultTypeDef",
    "DetachStaticIpResultTypeDef",
    "DisableAddOnResultTypeDef",
    "DiskInfoTypeDef",
    "DiskMapTypeDef",
    "DiskSnapshotInfoTypeDef",
    "DiskSnapshotTypeDef",
    "DiskTypeDef",
    "DistributionBundleTypeDef",
    "DomainEntryTypeDef",
    "DomainTypeDef",
    "DomainValidationRecordTypeDef",
    "DownloadDefaultKeyPairResultTypeDef",
    "EnableAddOnResultTypeDef",
    "EndpointRequestTypeDef",
    "ExportSnapshotRecordSourceInfoTypeDef",
    "ExportSnapshotRecordTypeDef",
    "ExportSnapshotResultTypeDef",
    "GetActiveNamesResultTypeDef",
    "GetAlarmsResultTypeDef",
    "GetAutoSnapshotsResultTypeDef",
    "GetBlueprintsResultTypeDef",
    "GetBundlesResultTypeDef",
    "GetCertificatesResultTypeDef",
    "GetCloudFormationStackRecordsResultTypeDef",
    "GetContactMethodsResultTypeDef",
    "GetContainerAPIMetadataResultTypeDef",
    "GetContainerImagesResultTypeDef",
    "GetContainerLogResultTypeDef",
    "GetContainerServiceDeploymentsResultTypeDef",
    "GetContainerServiceMetricDataResultTypeDef",
    "GetContainerServicePowersResultTypeDef",
    "GetDiskResultTypeDef",
    "GetDiskSnapshotResultTypeDef",
    "GetDiskSnapshotsResultTypeDef",
    "GetDisksResultTypeDef",
    "GetDistributionBundlesResultTypeDef",
    "GetDistributionLatestCacheResetResultTypeDef",
    "GetDistributionMetricDataResultTypeDef",
    "GetDistributionsResultTypeDef",
    "GetDomainResultTypeDef",
    "GetDomainsResultTypeDef",
    "GetExportSnapshotRecordsResultTypeDef",
    "GetInstanceAccessDetailsResultTypeDef",
    "GetInstanceMetricDataResultTypeDef",
    "GetInstancePortStatesResultTypeDef",
    "GetInstanceResultTypeDef",
    "GetInstanceSnapshotResultTypeDef",
    "GetInstanceSnapshotsResultTypeDef",
    "GetInstanceStateResultTypeDef",
    "GetInstancesResultTypeDef",
    "GetKeyPairResultTypeDef",
    "GetKeyPairsResultTypeDef",
    "GetLoadBalancerMetricDataResultTypeDef",
    "GetLoadBalancerResultTypeDef",
    "GetLoadBalancerTlsCertificatesResultTypeDef",
    "GetLoadBalancersResultTypeDef",
    "GetOperationResultTypeDef",
    "GetOperationsForResourceResultTypeDef",
    "GetOperationsResultTypeDef",
    "GetRegionsResultTypeDef",
    "GetRelationalDatabaseBlueprintsResultTypeDef",
    "GetRelationalDatabaseBundlesResultTypeDef",
    "GetRelationalDatabaseEventsResultTypeDef",
    "GetRelationalDatabaseLogEventsResultTypeDef",
    "GetRelationalDatabaseLogStreamsResultTypeDef",
    "GetRelationalDatabaseMasterUserPasswordResultTypeDef",
    "GetRelationalDatabaseMetricDataResultTypeDef",
    "GetRelationalDatabaseParametersResultTypeDef",
    "GetRelationalDatabaseResultTypeDef",
    "GetRelationalDatabaseSnapshotResultTypeDef",
    "GetRelationalDatabaseSnapshotsResultTypeDef",
    "GetRelationalDatabasesResultTypeDef",
    "GetStaticIpResultTypeDef",
    "GetStaticIpsResultTypeDef",
    "HeaderObjectTypeDef",
    "HostKeyAttributesTypeDef",
    "ImportKeyPairResultTypeDef",
    "InputOriginTypeDef",
    "InstanceAccessDetailsTypeDef",
    "InstanceEntryTypeDef",
    "InstanceHardwareTypeDef",
    "InstanceHealthSummaryTypeDef",
    "InstanceNetworkingTypeDef",
    "InstancePortInfoTypeDef",
    "InstancePortStateTypeDef",
    "InstanceSnapshotInfoTypeDef",
    "InstanceSnapshotTypeDef",
    "InstanceStateTypeDef",
    "InstanceTypeDef",
    "IsVpcPeeredResultTypeDef",
    "KeyPairTypeDef",
    "LightsailDistributionTypeDef",
    "LoadBalancerTlsCertificateDomainValidationOptionTypeDef",
    "LoadBalancerTlsCertificateDomainValidationRecordTypeDef",
    "LoadBalancerTlsCertificateRenewalSummaryTypeDef",
    "LoadBalancerTlsCertificateSummaryTypeDef",
    "LoadBalancerTlsCertificateTypeDef",
    "LoadBalancerTypeDef",
    "LogEventTypeDef",
    "MetricDatapointTypeDef",
    "MonitoredResourceInfoTypeDef",
    "MonthlyTransferTypeDef",
    "OpenInstancePublicPortsResultTypeDef",
    "OperationTypeDef",
    "OriginTypeDef",
    "PaginatorConfigTypeDef",
    "PasswordDataTypeDef",
    "PeerVpcResultTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingModifiedRelationalDatabaseValuesTypeDef",
    "PortInfoTypeDef",
    "PutAlarmResultTypeDef",
    "PutInstancePublicPortsResultTypeDef",
    "QueryStringObjectTypeDef",
    "RebootInstanceResultTypeDef",
    "RebootRelationalDatabaseResultTypeDef",
    "RegionTypeDef",
    "RegisterContainerImageResultTypeDef",
    "RelationalDatabaseBlueprintTypeDef",
    "RelationalDatabaseBundleTypeDef",
    "RelationalDatabaseEndpointTypeDef",
    "RelationalDatabaseEventTypeDef",
    "RelationalDatabaseHardwareTypeDef",
    "RelationalDatabaseParameterTypeDef",
    "RelationalDatabaseSnapshotTypeDef",
    "RelationalDatabaseTypeDef",
    "ReleaseStaticIpResultTypeDef",
    "RenewalSummaryTypeDef",
    "ResetDistributionCacheResultTypeDef",
    "ResourceLocationTypeDef",
    "ResourceRecordTypeDef",
    "SendContactMethodVerificationResultTypeDef",
    "SetIpAddressTypeResultTypeDef",
    "StartInstanceResultTypeDef",
    "StartRelationalDatabaseResultTypeDef",
    "StaticIpTypeDef",
    "StopInstanceResultTypeDef",
    "StopRelationalDatabaseResultTypeDef",
    "TagResourceResultTypeDef",
    "TagTypeDef",
    "TestAlarmResultTypeDef",
    "UnpeerVpcResultTypeDef",
    "UntagResourceResultTypeDef",
    "UpdateContainerServiceResultTypeDef",
    "UpdateDistributionBundleResultTypeDef",
    "UpdateDistributionResultTypeDef",
    "UpdateDomainEntryResultTypeDef",
    "UpdateLoadBalancerAttributeResultTypeDef",
    "UpdateRelationalDatabaseParametersResultTypeDef",
    "UpdateRelationalDatabaseResultTypeDef",
)


class _RequiredAddOnRequestTypeDef(TypedDict):
    addOnType: Literal["AutoSnapshot"]


class AddOnRequestTypeDef(_RequiredAddOnRequestTypeDef, total=False):
    autoSnapshotAddOnRequest: "AutoSnapshotAddOnRequestTypeDef"


class AddOnTypeDef(TypedDict, total=False):
    name: str
    status: str
    snapshotTimeOfDay: str
    nextSnapshotTimeOfDay: str


class AlarmTypeDef(TypedDict, total=False):
    name: str
    arn: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    supportCode: str
    monitoredResourceInfo: "MonitoredResourceInfoTypeDef"
    comparisonOperator: ComparisonOperator
    evaluationPeriods: int
    period: int
    threshold: float
    datapointsToAlarm: int
    treatMissingData: TreatMissingData
    statistic: MetricStatistic
    metricName: MetricName
    state: AlarmState
    unit: MetricUnit
    contactProtocols: List[ContactProtocol]
    notificationTriggers: List[AlarmState]
    notificationEnabled: bool


class AllocateStaticIpResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class AttachCertificateToDistributionResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class AttachDiskResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class AttachInstancesToLoadBalancerResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class AttachLoadBalancerTlsCertificateResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class AttachStaticIpResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class AttachedDiskTypeDef(TypedDict, total=False):
    path: str
    sizeInGb: int


class AutoSnapshotAddOnRequestTypeDef(TypedDict, total=False):
    snapshotTimeOfDay: str


class AutoSnapshotDetailsTypeDef(TypedDict, total=False):
    date: str
    createdAt: datetime
    status: AutoSnapshotStatus
    fromAttachedDisks: List["AttachedDiskTypeDef"]


class AvailabilityZoneTypeDef(TypedDict, total=False):
    zoneName: str
    state: str


BlueprintTypeDef = TypedDict(
    "BlueprintTypeDef",
    {
        "blueprintId": str,
        "name": str,
        "group": str,
        "type": BlueprintType,
        "description": str,
        "isActive": bool,
        "minPower": int,
        "version": str,
        "versionCode": str,
        "productUrl": str,
        "licenseUrl": str,
        "platform": InstancePlatform,
    },
    total=False,
)


class BundleTypeDef(TypedDict, total=False):
    price: float
    cpuCount: int
    diskSizeInGb: int
    bundleId: str
    instanceType: str
    isActive: bool
    name: str
    power: int
    ramSizeInGb: float
    transferPerMonthInGb: int
    supportedPlatforms: List[InstancePlatform]


class CacheBehaviorPerPathTypeDef(TypedDict, total=False):
    path: str
    behavior: BehaviorEnum


class CacheBehaviorTypeDef(TypedDict, total=False):
    behavior: BehaviorEnum


class CacheSettingsTypeDef(TypedDict, total=False):
    defaultTTL: int
    minimumTTL: int
    maximumTTL: int
    allowedHTTPMethods: str
    cachedHTTPMethods: str
    forwardedCookies: "CookieObjectTypeDef"
    forwardedHeaders: "HeaderObjectTypeDef"
    forwardedQueryStrings: "QueryStringObjectTypeDef"


class CertificateSummaryTypeDef(TypedDict, total=False):
    certificateArn: str
    certificateName: str
    domainName: str
    certificateDetail: "CertificateTypeDef"
    tags: List["TagTypeDef"]


class CertificateTypeDef(TypedDict, total=False):
    arn: str
    name: str
    domainName: str
    status: CertificateStatus
    serialNumber: str
    subjectAlternativeNames: List[str]
    domainValidationRecords: List["DomainValidationRecordTypeDef"]
    requestFailureReason: str
    inUseResourceCount: int
    keyAlgorithm: str
    createdAt: datetime
    issuedAt: datetime
    issuerCA: str
    notBefore: datetime
    notAfter: datetime
    eligibleToRenew: str
    renewalSummary: "RenewalSummaryTypeDef"
    revokedAt: datetime
    revocationReason: str
    tags: List["TagTypeDef"]
    supportCode: str


class CloseInstancePublicPortsResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class CloudFormationStackRecordSourceInfoTypeDef(TypedDict, total=False):
    resourceType: Literal["ExportSnapshotRecord"]
    name: str
    arn: str


class CloudFormationStackRecordTypeDef(TypedDict, total=False):
    name: str
    arn: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    state: RecordState
    sourceInfo: List["CloudFormationStackRecordSourceInfoTypeDef"]
    destinationInfo: "DestinationInfoTypeDef"


class ContactMethodTypeDef(TypedDict, total=False):
    contactEndpoint: str
    status: ContactMethodStatus
    protocol: ContactProtocol
    name: str
    arn: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    supportCode: str


class ContainerImageTypeDef(TypedDict, total=False):
    image: str
    digest: str
    createdAt: datetime


class ContainerServiceDeploymentRequestTypeDef(TypedDict, total=False):
    containers: Dict[str, "ContainerTypeDef"]
    publicEndpoint: "EndpointRequestTypeDef"


class ContainerServiceDeploymentTypeDef(TypedDict, total=False):
    version: int
    state: ContainerServiceDeploymentState
    containers: Dict[str, "ContainerTypeDef"]
    publicEndpoint: "ContainerServiceEndpointTypeDef"
    createdAt: datetime


class ContainerServiceEndpointTypeDef(TypedDict, total=False):
    containerName: str
    containerPort: int
    healthCheck: "ContainerServiceHealthCheckConfigTypeDef"


class ContainerServiceHealthCheckConfigTypeDef(TypedDict, total=False):
    healthyThreshold: int
    unhealthyThreshold: int
    timeoutSeconds: int
    intervalSeconds: int
    path: str
    successCodes: str


class ContainerServiceLogEventTypeDef(TypedDict, total=False):
    createdAt: datetime
    message: str


class ContainerServicePowerTypeDef(TypedDict, total=False):
    powerId: str
    price: float
    cpuCount: float
    ramSizeInGb: float
    name: str
    isActive: bool


class ContainerServiceRegistryLoginTypeDef(TypedDict, total=False):
    username: str
    password: str
    expiresAt: datetime
    registry: str


class ContainerServiceStateDetailTypeDef(TypedDict, total=False):
    code: ContainerServiceStateDetailCode
    message: str


class ContainerServiceTypeDef(TypedDict, total=False):
    containerServiceName: str
    arn: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    tags: List["TagTypeDef"]
    power: ContainerServicePowerName
    powerId: str
    state: ContainerServiceState
    stateDetail: "ContainerServiceStateDetailTypeDef"
    scale: int
    currentDeployment: "ContainerServiceDeploymentTypeDef"
    nextDeployment: "ContainerServiceDeploymentTypeDef"
    isDisabled: bool
    principalArn: str
    privateDomainName: str
    publicDomainNames: Dict[str, List[str]]
    url: str


class ContainerServicesListResultTypeDef(TypedDict, total=False):
    containerServices: List["ContainerServiceTypeDef"]


class ContainerTypeDef(TypedDict, total=False):
    image: str
    command: List[str]
    environment: Dict[str, str]
    ports: Dict[str, ContainerServiceProtocol]


class CookieObjectTypeDef(TypedDict, total=False):
    option: ForwardValues
    cookiesAllowList: List[str]


class CopySnapshotResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class CreateCertificateResultTypeDef(TypedDict, total=False):
    certificate: "CertificateSummaryTypeDef"
    operations: List["OperationTypeDef"]


class CreateCloudFormationStackResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class CreateContactMethodResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class CreateContainerServiceDeploymentResultTypeDef(TypedDict, total=False):
    containerService: "ContainerServiceTypeDef"


class CreateContainerServiceRegistryLoginResultTypeDef(TypedDict, total=False):
    registryLogin: "ContainerServiceRegistryLoginTypeDef"


class CreateContainerServiceResultTypeDef(TypedDict, total=False):
    containerService: "ContainerServiceTypeDef"


class CreateDiskFromSnapshotResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class CreateDiskResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class CreateDiskSnapshotResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class CreateDistributionResultTypeDef(TypedDict, total=False):
    distribution: "LightsailDistributionTypeDef"
    operation: "OperationTypeDef"


class CreateDomainEntryResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class CreateDomainResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class CreateInstanceSnapshotResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class CreateInstancesFromSnapshotResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class CreateInstancesResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class CreateKeyPairResultTypeDef(TypedDict, total=False):
    keyPair: "KeyPairTypeDef"
    publicKeyBase64: str
    privateKeyBase64: str
    operation: "OperationTypeDef"


class CreateLoadBalancerResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class CreateLoadBalancerTlsCertificateResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class CreateRelationalDatabaseFromSnapshotResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class CreateRelationalDatabaseResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class CreateRelationalDatabaseSnapshotResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DeleteAlarmResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DeleteAutoSnapshotResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DeleteCertificateResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DeleteContactMethodResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DeleteDiskResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DeleteDiskSnapshotResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DeleteDistributionResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class DeleteDomainEntryResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class DeleteDomainResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class DeleteInstanceResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DeleteInstanceSnapshotResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DeleteKeyPairResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class DeleteKnownHostKeysResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DeleteLoadBalancerResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DeleteLoadBalancerTlsCertificateResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DeleteRelationalDatabaseResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DeleteRelationalDatabaseSnapshotResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


DestinationInfoTypeDef = TypedDict(
    "DestinationInfoTypeDef", {"id": str, "service": str}, total=False
)


class DetachCertificateFromDistributionResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class DetachDiskResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DetachInstancesFromLoadBalancerResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DetachStaticIpResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DisableAddOnResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class DiskInfoTypeDef(TypedDict, total=False):
    name: str
    path: str
    sizeInGb: int
    isSystemDisk: bool


class DiskMapTypeDef(TypedDict, total=False):
    originalDiskPath: str
    newDiskName: str


class DiskSnapshotInfoTypeDef(TypedDict, total=False):
    sizeInGb: int


class DiskSnapshotTypeDef(TypedDict, total=False):
    name: str
    arn: str
    supportCode: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    tags: List["TagTypeDef"]
    sizeInGb: int
    state: DiskSnapshotState
    progress: str
    fromDiskName: str
    fromDiskArn: str
    fromInstanceName: str
    fromInstanceArn: str
    isFromAutoSnapshot: bool


class DiskTypeDef(TypedDict, total=False):
    name: str
    arn: str
    supportCode: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    tags: List["TagTypeDef"]
    addOns: List["AddOnTypeDef"]
    sizeInGb: int
    isSystemDisk: bool
    iops: int
    path: str
    state: DiskState
    attachedTo: str
    isAttached: bool
    attachmentState: str
    gbInUse: int


class DistributionBundleTypeDef(TypedDict, total=False):
    bundleId: str
    name: str
    price: float
    transferPerMonthInGb: int
    isActive: bool


DomainEntryTypeDef = TypedDict(
    "DomainEntryTypeDef",
    {
        "id": str,
        "name": str,
        "target": str,
        "isAlias": bool,
        "type": str,
        "options": Dict[str, str],
    },
    total=False,
)


class DomainTypeDef(TypedDict, total=False):
    name: str
    arn: str
    supportCode: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    tags: List["TagTypeDef"]
    domainEntries: List["DomainEntryTypeDef"]


class DomainValidationRecordTypeDef(TypedDict, total=False):
    domainName: str
    resourceRecord: "ResourceRecordTypeDef"


class DownloadDefaultKeyPairResultTypeDef(TypedDict, total=False):
    publicKeyBase64: str
    privateKeyBase64: str


class EnableAddOnResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class _RequiredEndpointRequestTypeDef(TypedDict):
    containerName: str
    containerPort: int


class EndpointRequestTypeDef(_RequiredEndpointRequestTypeDef, total=False):
    healthCheck: "ContainerServiceHealthCheckConfigTypeDef"


class ExportSnapshotRecordSourceInfoTypeDef(TypedDict, total=False):
    resourceType: ExportSnapshotRecordSourceType
    createdAt: datetime
    name: str
    arn: str
    fromResourceName: str
    fromResourceArn: str
    instanceSnapshotInfo: "InstanceSnapshotInfoTypeDef"
    diskSnapshotInfo: "DiskSnapshotInfoTypeDef"


class ExportSnapshotRecordTypeDef(TypedDict, total=False):
    name: str
    arn: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    state: RecordState
    sourceInfo: "ExportSnapshotRecordSourceInfoTypeDef"
    destinationInfo: "DestinationInfoTypeDef"


class ExportSnapshotResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class GetActiveNamesResultTypeDef(TypedDict, total=False):
    activeNames: List[str]
    nextPageToken: str


class GetAlarmsResultTypeDef(TypedDict, total=False):
    alarms: List["AlarmTypeDef"]
    nextPageToken: str


class GetAutoSnapshotsResultTypeDef(TypedDict, total=False):
    resourceName: str
    resourceType: ResourceType
    autoSnapshots: List["AutoSnapshotDetailsTypeDef"]


class GetBlueprintsResultTypeDef(TypedDict, total=False):
    blueprints: List["BlueprintTypeDef"]
    nextPageToken: str


class GetBundlesResultTypeDef(TypedDict, total=False):
    bundles: List["BundleTypeDef"]
    nextPageToken: str


class GetCertificatesResultTypeDef(TypedDict, total=False):
    certificates: List["CertificateSummaryTypeDef"]


class GetCloudFormationStackRecordsResultTypeDef(TypedDict, total=False):
    cloudFormationStackRecords: List["CloudFormationStackRecordTypeDef"]
    nextPageToken: str


class GetContactMethodsResultTypeDef(TypedDict, total=False):
    contactMethods: List["ContactMethodTypeDef"]


class GetContainerAPIMetadataResultTypeDef(TypedDict, total=False):
    metadata: List[Dict[str, str]]


class GetContainerImagesResultTypeDef(TypedDict, total=False):
    containerImages: List["ContainerImageTypeDef"]


class GetContainerLogResultTypeDef(TypedDict, total=False):
    logEvents: List["ContainerServiceLogEventTypeDef"]
    nextPageToken: str


class GetContainerServiceDeploymentsResultTypeDef(TypedDict, total=False):
    deployments: List["ContainerServiceDeploymentTypeDef"]


class GetContainerServiceMetricDataResultTypeDef(TypedDict, total=False):
    metricName: ContainerServiceMetricName
    metricData: List["MetricDatapointTypeDef"]


class GetContainerServicePowersResultTypeDef(TypedDict, total=False):
    powers: List["ContainerServicePowerTypeDef"]


class GetDiskResultTypeDef(TypedDict, total=False):
    disk: "DiskTypeDef"


class GetDiskSnapshotResultTypeDef(TypedDict, total=False):
    diskSnapshot: "DiskSnapshotTypeDef"


class GetDiskSnapshotsResultTypeDef(TypedDict, total=False):
    diskSnapshots: List["DiskSnapshotTypeDef"]
    nextPageToken: str


class GetDisksResultTypeDef(TypedDict, total=False):
    disks: List["DiskTypeDef"]
    nextPageToken: str


class GetDistributionBundlesResultTypeDef(TypedDict, total=False):
    bundles: List["DistributionBundleTypeDef"]


class GetDistributionLatestCacheResetResultTypeDef(TypedDict, total=False):
    status: str
    createTime: datetime


class GetDistributionMetricDataResultTypeDef(TypedDict, total=False):
    metricName: DistributionMetricName
    metricData: List["MetricDatapointTypeDef"]


class GetDistributionsResultTypeDef(TypedDict, total=False):
    distributions: List["LightsailDistributionTypeDef"]
    nextPageToken: str


class GetDomainResultTypeDef(TypedDict, total=False):
    domain: "DomainTypeDef"


class GetDomainsResultTypeDef(TypedDict, total=False):
    domains: List["DomainTypeDef"]
    nextPageToken: str


class GetExportSnapshotRecordsResultTypeDef(TypedDict, total=False):
    exportSnapshotRecords: List["ExportSnapshotRecordTypeDef"]
    nextPageToken: str


class GetInstanceAccessDetailsResultTypeDef(TypedDict, total=False):
    accessDetails: "InstanceAccessDetailsTypeDef"


class GetInstanceMetricDataResultTypeDef(TypedDict, total=False):
    metricName: InstanceMetricName
    metricData: List["MetricDatapointTypeDef"]


class GetInstancePortStatesResultTypeDef(TypedDict, total=False):
    portStates: List["InstancePortStateTypeDef"]


class GetInstanceResultTypeDef(TypedDict, total=False):
    instance: "InstanceTypeDef"


class GetInstanceSnapshotResultTypeDef(TypedDict, total=False):
    instanceSnapshot: "InstanceSnapshotTypeDef"


class GetInstanceSnapshotsResultTypeDef(TypedDict, total=False):
    instanceSnapshots: List["InstanceSnapshotTypeDef"]
    nextPageToken: str


class GetInstanceStateResultTypeDef(TypedDict, total=False):
    state: "InstanceStateTypeDef"


class GetInstancesResultTypeDef(TypedDict, total=False):
    instances: List["InstanceTypeDef"]
    nextPageToken: str


class GetKeyPairResultTypeDef(TypedDict, total=False):
    keyPair: "KeyPairTypeDef"


class GetKeyPairsResultTypeDef(TypedDict, total=False):
    keyPairs: List["KeyPairTypeDef"]
    nextPageToken: str


class GetLoadBalancerMetricDataResultTypeDef(TypedDict, total=False):
    metricName: LoadBalancerMetricName
    metricData: List["MetricDatapointTypeDef"]


class GetLoadBalancerResultTypeDef(TypedDict, total=False):
    loadBalancer: "LoadBalancerTypeDef"


class GetLoadBalancerTlsCertificatesResultTypeDef(TypedDict, total=False):
    tlsCertificates: List["LoadBalancerTlsCertificateTypeDef"]


class GetLoadBalancersResultTypeDef(TypedDict, total=False):
    loadBalancers: List["LoadBalancerTypeDef"]
    nextPageToken: str


class GetOperationResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class GetOperationsForResourceResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]
    nextPageCount: str
    nextPageToken: str


class GetOperationsResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]
    nextPageToken: str


class GetRegionsResultTypeDef(TypedDict, total=False):
    regions: List["RegionTypeDef"]


class GetRelationalDatabaseBlueprintsResultTypeDef(TypedDict, total=False):
    blueprints: List["RelationalDatabaseBlueprintTypeDef"]
    nextPageToken: str


class GetRelationalDatabaseBundlesResultTypeDef(TypedDict, total=False):
    bundles: List["RelationalDatabaseBundleTypeDef"]
    nextPageToken: str


class GetRelationalDatabaseEventsResultTypeDef(TypedDict, total=False):
    relationalDatabaseEvents: List["RelationalDatabaseEventTypeDef"]
    nextPageToken: str


class GetRelationalDatabaseLogEventsResultTypeDef(TypedDict, total=False):
    resourceLogEvents: List["LogEventTypeDef"]
    nextBackwardToken: str
    nextForwardToken: str


class GetRelationalDatabaseLogStreamsResultTypeDef(TypedDict, total=False):
    logStreams: List[str]


class GetRelationalDatabaseMasterUserPasswordResultTypeDef(TypedDict, total=False):
    masterUserPassword: str
    createdAt: datetime


class GetRelationalDatabaseMetricDataResultTypeDef(TypedDict, total=False):
    metricName: RelationalDatabaseMetricName
    metricData: List["MetricDatapointTypeDef"]


class GetRelationalDatabaseParametersResultTypeDef(TypedDict, total=False):
    parameters: List["RelationalDatabaseParameterTypeDef"]
    nextPageToken: str


class GetRelationalDatabaseResultTypeDef(TypedDict, total=False):
    relationalDatabase: "RelationalDatabaseTypeDef"


class GetRelationalDatabaseSnapshotResultTypeDef(TypedDict, total=False):
    relationalDatabaseSnapshot: "RelationalDatabaseSnapshotTypeDef"


class GetRelationalDatabaseSnapshotsResultTypeDef(TypedDict, total=False):
    relationalDatabaseSnapshots: List["RelationalDatabaseSnapshotTypeDef"]
    nextPageToken: str


class GetRelationalDatabasesResultTypeDef(TypedDict, total=False):
    relationalDatabases: List["RelationalDatabaseTypeDef"]
    nextPageToken: str


class GetStaticIpResultTypeDef(TypedDict, total=False):
    staticIp: "StaticIpTypeDef"


class GetStaticIpsResultTypeDef(TypedDict, total=False):
    staticIps: List["StaticIpTypeDef"]
    nextPageToken: str


class HeaderObjectTypeDef(TypedDict, total=False):
    option: ForwardValues
    headersAllowList: List[HeaderEnum]


class HostKeyAttributesTypeDef(TypedDict, total=False):
    algorithm: str
    publicKey: str
    witnessedAt: datetime
    fingerprintSHA1: str
    fingerprintSHA256: str
    notValidBefore: datetime
    notValidAfter: datetime


class ImportKeyPairResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class InputOriginTypeDef(TypedDict, total=False):
    name: str
    regionName: RegionName
    protocolPolicy: OriginProtocolPolicyEnum


class InstanceAccessDetailsTypeDef(TypedDict, total=False):
    certKey: str
    expiresAt: datetime
    ipAddress: str
    password: str
    passwordData: "PasswordDataTypeDef"
    privateKey: str
    protocol: InstanceAccessProtocol
    instanceName: str
    username: str
    hostKeys: List["HostKeyAttributesTypeDef"]


class _RequiredInstanceEntryTypeDef(TypedDict):
    sourceName: str
    instanceType: str
    portInfoSource: PortInfoSourceType
    availabilityZone: str


class InstanceEntryTypeDef(_RequiredInstanceEntryTypeDef, total=False):
    userData: str


class InstanceHardwareTypeDef(TypedDict, total=False):
    cpuCount: int
    disks: List["DiskTypeDef"]
    ramSizeInGb: float


class InstanceHealthSummaryTypeDef(TypedDict, total=False):
    instanceName: str
    instanceHealth: InstanceHealthState
    instanceHealthReason: InstanceHealthReason


class InstanceNetworkingTypeDef(TypedDict, total=False):
    monthlyTransfer: "MonthlyTransferTypeDef"
    ports: List["InstancePortInfoTypeDef"]


class InstancePortInfoTypeDef(TypedDict, total=False):
    fromPort: int
    toPort: int
    protocol: NetworkProtocol
    accessFrom: str
    accessType: PortAccessType
    commonName: str
    accessDirection: AccessDirection
    cidrs: List[str]
    ipv6Cidrs: List[str]
    cidrListAliases: List[str]


class InstancePortStateTypeDef(TypedDict, total=False):
    fromPort: int
    toPort: int
    protocol: NetworkProtocol
    state: PortState
    cidrs: List[str]
    ipv6Cidrs: List[str]
    cidrListAliases: List[str]


class InstanceSnapshotInfoTypeDef(TypedDict, total=False):
    fromBundleId: str
    fromBlueprintId: str
    fromDiskInfo: List["DiskInfoTypeDef"]


class InstanceSnapshotTypeDef(TypedDict, total=False):
    name: str
    arn: str
    supportCode: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    tags: List["TagTypeDef"]
    state: InstanceSnapshotState
    progress: str
    fromAttachedDisks: List["DiskTypeDef"]
    fromInstanceName: str
    fromInstanceArn: str
    fromBlueprintId: str
    fromBundleId: str
    isFromAutoSnapshot: bool
    sizeInGb: int


class InstanceStateTypeDef(TypedDict, total=False):
    code: int
    name: str


class InstanceTypeDef(TypedDict, total=False):
    name: str
    arn: str
    supportCode: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    tags: List["TagTypeDef"]
    blueprintId: str
    blueprintName: str
    bundleId: str
    addOns: List["AddOnTypeDef"]
    isStaticIp: bool
    privateIpAddress: str
    publicIpAddress: str
    ipv6Addresses: List[str]
    ipAddressType: IpAddressType
    hardware: "InstanceHardwareTypeDef"
    networking: "InstanceNetworkingTypeDef"
    state: "InstanceStateTypeDef"
    username: str
    sshKeyName: str


class IsVpcPeeredResultTypeDef(TypedDict, total=False):
    isPeered: bool


class KeyPairTypeDef(TypedDict, total=False):
    name: str
    arn: str
    supportCode: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    tags: List["TagTypeDef"]
    fingerprint: str


class LightsailDistributionTypeDef(TypedDict, total=False):
    name: str
    arn: str
    supportCode: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    alternativeDomainNames: List[str]
    status: str
    isEnabled: bool
    domainName: str
    bundleId: str
    certificateName: str
    origin: "OriginTypeDef"
    originPublicDNS: str
    defaultCacheBehavior: "CacheBehaviorTypeDef"
    cacheBehaviorSettings: "CacheSettingsTypeDef"
    cacheBehaviors: List["CacheBehaviorPerPathTypeDef"]
    ableToUpdateBundle: bool
    ipAddressType: IpAddressType
    tags: List["TagTypeDef"]


class LoadBalancerTlsCertificateDomainValidationOptionTypeDef(TypedDict, total=False):
    domainName: str
    validationStatus: LoadBalancerTlsCertificateDomainStatus


LoadBalancerTlsCertificateDomainValidationRecordTypeDef = TypedDict(
    "LoadBalancerTlsCertificateDomainValidationRecordTypeDef",
    {
        "name": str,
        "type": str,
        "value": str,
        "validationStatus": LoadBalancerTlsCertificateDomainStatus,
        "domainName": str,
    },
    total=False,
)


class LoadBalancerTlsCertificateRenewalSummaryTypeDef(TypedDict, total=False):
    renewalStatus: LoadBalancerTlsCertificateRenewalStatus
    domainValidationOptions: List["LoadBalancerTlsCertificateDomainValidationOptionTypeDef"]


class LoadBalancerTlsCertificateSummaryTypeDef(TypedDict, total=False):
    name: str
    isAttached: bool


class LoadBalancerTlsCertificateTypeDef(TypedDict, total=False):
    name: str
    arn: str
    supportCode: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    tags: List["TagTypeDef"]
    loadBalancerName: str
    isAttached: bool
    status: LoadBalancerTlsCertificateStatus
    domainName: str
    domainValidationRecords: List["LoadBalancerTlsCertificateDomainValidationRecordTypeDef"]
    failureReason: LoadBalancerTlsCertificateFailureReason
    issuedAt: datetime
    issuer: str
    keyAlgorithm: str
    notAfter: datetime
    notBefore: datetime
    renewalSummary: "LoadBalancerTlsCertificateRenewalSummaryTypeDef"
    revocationReason: LoadBalancerTlsCertificateRevocationReason
    revokedAt: datetime
    serial: str
    signatureAlgorithm: str
    subject: str
    subjectAlternativeNames: List[str]


class LoadBalancerTypeDef(TypedDict, total=False):
    name: str
    arn: str
    supportCode: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    tags: List["TagTypeDef"]
    dnsName: str
    state: LoadBalancerState
    protocol: LoadBalancerProtocol
    publicPorts: List[int]
    healthCheckPath: str
    instancePort: int
    instanceHealthSummary: List["InstanceHealthSummaryTypeDef"]
    tlsCertificateSummaries: List["LoadBalancerTlsCertificateSummaryTypeDef"]
    configurationOptions: Dict[LoadBalancerAttributeName, str]
    ipAddressType: IpAddressType


class LogEventTypeDef(TypedDict, total=False):
    createdAt: datetime
    message: str


MetricDatapointTypeDef = TypedDict(
    "MetricDatapointTypeDef",
    {
        "average": float,
        "maximum": float,
        "minimum": float,
        "sampleCount": float,
        "sum": float,
        "timestamp": datetime,
        "unit": MetricUnit,
    },
    total=False,
)


class MonitoredResourceInfoTypeDef(TypedDict, total=False):
    arn: str
    name: str
    resourceType: ResourceType


class MonthlyTransferTypeDef(TypedDict, total=False):
    gbPerMonthAllocated: int


class OpenInstancePublicPortsResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


OperationTypeDef = TypedDict(
    "OperationTypeDef",
    {
        "id": str,
        "resourceName": str,
        "resourceType": ResourceType,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "isTerminal": bool,
        "operationDetails": str,
        "operationType": OperationType,
        "status": OperationStatus,
        "statusChangedAt": datetime,
        "errorCode": str,
        "errorDetails": str,
    },
    total=False,
)


class OriginTypeDef(TypedDict, total=False):
    name: str
    resourceType: ResourceType
    regionName: RegionName
    protocolPolicy: OriginProtocolPolicyEnum


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PasswordDataTypeDef(TypedDict, total=False):
    ciphertext: str
    keyPairName: str


class PeerVpcResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class PendingMaintenanceActionTypeDef(TypedDict, total=False):
    action: str
    description: str
    currentApplyDate: datetime


class PendingModifiedRelationalDatabaseValuesTypeDef(TypedDict, total=False):
    masterUserPassword: str
    engineVersion: str
    backupRetentionEnabled: bool


class PortInfoTypeDef(TypedDict, total=False):
    fromPort: int
    toPort: int
    protocol: NetworkProtocol
    cidrs: List[str]
    ipv6Cidrs: List[str]
    cidrListAliases: List[str]


class PutAlarmResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class PutInstancePublicPortsResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class QueryStringObjectTypeDef(TypedDict, total=False):
    option: bool
    queryStringsAllowList: List[str]


class RebootInstanceResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class RebootRelationalDatabaseResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class RegionTypeDef(TypedDict, total=False):
    continentCode: str
    description: str
    displayName: str
    name: RegionName
    availabilityZones: List["AvailabilityZoneTypeDef"]
    relationalDatabaseAvailabilityZones: List["AvailabilityZoneTypeDef"]


class RegisterContainerImageResultTypeDef(TypedDict, total=False):
    containerImage: "ContainerImageTypeDef"


class RelationalDatabaseBlueprintTypeDef(TypedDict, total=False):
    blueprintId: str
    engine: Literal["mysql"]
    engineVersion: str
    engineDescription: str
    engineVersionDescription: str
    isEngineDefault: bool


class RelationalDatabaseBundleTypeDef(TypedDict, total=False):
    bundleId: str
    name: str
    price: float
    ramSizeInGb: float
    diskSizeInGb: int
    transferPerMonthInGb: int
    cpuCount: int
    isEncrypted: bool
    isActive: bool


class RelationalDatabaseEndpointTypeDef(TypedDict, total=False):
    port: int
    address: str


class RelationalDatabaseEventTypeDef(TypedDict, total=False):
    resource: str
    createdAt: datetime
    message: str
    eventCategories: List[str]


class RelationalDatabaseHardwareTypeDef(TypedDict, total=False):
    cpuCount: int
    diskSizeInGb: int
    ramSizeInGb: float


class RelationalDatabaseParameterTypeDef(TypedDict, total=False):
    allowedValues: str
    applyMethod: str
    applyType: str
    dataType: str
    description: str
    isModifiable: bool
    parameterName: str
    parameterValue: str


class RelationalDatabaseSnapshotTypeDef(TypedDict, total=False):
    name: str
    arn: str
    supportCode: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    tags: List["TagTypeDef"]
    engine: str
    engineVersion: str
    sizeInGb: int
    state: str
    fromRelationalDatabaseName: str
    fromRelationalDatabaseArn: str
    fromRelationalDatabaseBundleId: str
    fromRelationalDatabaseBlueprintId: str


class RelationalDatabaseTypeDef(TypedDict, total=False):
    name: str
    arn: str
    supportCode: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    tags: List["TagTypeDef"]
    relationalDatabaseBlueprintId: str
    relationalDatabaseBundleId: str
    masterDatabaseName: str
    hardware: "RelationalDatabaseHardwareTypeDef"
    state: str
    secondaryAvailabilityZone: str
    backupRetentionEnabled: bool
    pendingModifiedValues: "PendingModifiedRelationalDatabaseValuesTypeDef"
    engine: str
    engineVersion: str
    latestRestorableTime: datetime
    masterUsername: str
    parameterApplyStatus: str
    preferredBackupWindow: str
    preferredMaintenanceWindow: str
    publiclyAccessible: bool
    masterEndpoint: "RelationalDatabaseEndpointTypeDef"
    pendingMaintenanceActions: List["PendingMaintenanceActionTypeDef"]
    caCertificateIdentifier: str


class ReleaseStaticIpResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class RenewalSummaryTypeDef(TypedDict, total=False):
    domainValidationRecords: List["DomainValidationRecordTypeDef"]
    renewalStatus: RenewalStatus
    renewalStatusReason: str
    updatedAt: datetime


class ResetDistributionCacheResultTypeDef(TypedDict, total=False):
    status: str
    createTime: datetime
    operation: "OperationTypeDef"


class ResourceLocationTypeDef(TypedDict, total=False):
    availabilityZone: str
    regionName: RegionName


ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef", {"name": str, "type": str, "value": str}, total=False
)


class SendContactMethodVerificationResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class SetIpAddressTypeResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class StartInstanceResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class StartRelationalDatabaseResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class StaticIpTypeDef(TypedDict, total=False):
    name: str
    arn: str
    supportCode: str
    createdAt: datetime
    location: "ResourceLocationTypeDef"
    resourceType: ResourceType
    ipAddress: str
    attachedTo: str
    isAttached: bool


class StopInstanceResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class StopRelationalDatabaseResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class TagResourceResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class TagTypeDef(TypedDict, total=False):
    key: str
    value: str


class TestAlarmResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class UnpeerVpcResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class UntagResourceResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class UpdateContainerServiceResultTypeDef(TypedDict, total=False):
    containerService: "ContainerServiceTypeDef"


class UpdateDistributionBundleResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class UpdateDistributionResultTypeDef(TypedDict, total=False):
    operation: "OperationTypeDef"


class UpdateDomainEntryResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class UpdateLoadBalancerAttributeResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class UpdateRelationalDatabaseParametersResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]


class UpdateRelationalDatabaseResultTypeDef(TypedDict, total=False):
    operations: List["OperationTypeDef"]
