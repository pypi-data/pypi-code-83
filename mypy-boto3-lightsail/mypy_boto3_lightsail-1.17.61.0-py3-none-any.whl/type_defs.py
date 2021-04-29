"""
Main interface for lightsail service type definitions.

Usage::

    ```python
    from mypy_boto3_lightsail.type_defs import AddOnTypeDef

    data: AddOnTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_lightsail.literals import (
    AccessDirection,
    AddOnType,
    AlarmState,
    AutoSnapshotStatus,
    BehaviorEnum,
    BlueprintType,
    CertificateStatus,
    CloudFormationStackRecordSourceType,
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
    RelationalDatabaseEngine,
    RelationalDatabaseMetricName,
    RenewalStatus,
    ResourceType,
    TreatMissingData,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddOnTypeDef",
    "AlarmTypeDef",
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
    "CloudFormationStackRecordSourceInfoTypeDef",
    "CloudFormationStackRecordTypeDef",
    "ContactMethodTypeDef",
    "ContainerImageTypeDef",
    "ContainerServiceDeploymentTypeDef",
    "ContainerServiceEndpointTypeDef",
    "ContainerServiceHealthCheckConfigTypeDef",
    "ContainerServiceLogEventTypeDef",
    "ContainerServicePowerTypeDef",
    "ContainerServiceRegistryLoginTypeDef",
    "ContainerServiceStateDetailTypeDef",
    "ContainerServiceTypeDef",
    "ContainerTypeDef",
    "CookieObjectTypeDef",
    "DestinationInfoTypeDef",
    "DiskInfoTypeDef",
    "DiskSnapshotInfoTypeDef",
    "DiskSnapshotTypeDef",
    "DiskTypeDef",
    "DistributionBundleTypeDef",
    "DomainEntryTypeDef",
    "DomainTypeDef",
    "DomainValidationRecordTypeDef",
    "EndpointRequestTypeDef",
    "ExportSnapshotRecordSourceInfoTypeDef",
    "ExportSnapshotRecordTypeDef",
    "HeaderObjectTypeDef",
    "HostKeyAttributesTypeDef",
    "InstanceAccessDetailsTypeDef",
    "InstanceHardwareTypeDef",
    "InstanceHealthSummaryTypeDef",
    "InstanceNetworkingTypeDef",
    "InstancePortInfoTypeDef",
    "InstancePortStateTypeDef",
    "InstanceSnapshotInfoTypeDef",
    "InstanceSnapshotTypeDef",
    "InstanceStateTypeDef",
    "InstanceTypeDef",
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
    "OperationTypeDef",
    "OriginTypeDef",
    "PasswordDataTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingModifiedRelationalDatabaseValuesTypeDef",
    "QueryStringObjectTypeDef",
    "RegionTypeDef",
    "RelationalDatabaseBlueprintTypeDef",
    "RelationalDatabaseBundleTypeDef",
    "RelationalDatabaseEndpointTypeDef",
    "RelationalDatabaseEventTypeDef",
    "RelationalDatabaseHardwareTypeDef",
    "RelationalDatabaseParameterTypeDef",
    "RelationalDatabaseSnapshotTypeDef",
    "RelationalDatabaseTypeDef",
    "RenewalSummaryTypeDef",
    "ResourceLocationTypeDef",
    "ResourceRecordTypeDef",
    "StaticIpTypeDef",
    "TagTypeDef",
    "AddOnRequestTypeDef",
    "AllocateStaticIpResultTypeDef",
    "AttachCertificateToDistributionResultTypeDef",
    "AttachDiskResultTypeDef",
    "AttachInstancesToLoadBalancerResultTypeDef",
    "AttachLoadBalancerTlsCertificateResultTypeDef",
    "AttachStaticIpResultTypeDef",
    "CloseInstancePublicPortsResultTypeDef",
    "ContainerServiceDeploymentRequestTypeDef",
    "ContainerServicesListResultTypeDef",
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
    "DetachCertificateFromDistributionResultTypeDef",
    "DetachDiskResultTypeDef",
    "DetachInstancesFromLoadBalancerResultTypeDef",
    "DetachStaticIpResultTypeDef",
    "DisableAddOnResultTypeDef",
    "DiskMapTypeDef",
    "DownloadDefaultKeyPairResultTypeDef",
    "EnableAddOnResultTypeDef",
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
    "ImportKeyPairResultTypeDef",
    "InputOriginTypeDef",
    "InstanceEntryTypeDef",
    "IsVpcPeeredResultTypeDef",
    "OpenInstancePublicPortsResultTypeDef",
    "PaginatorConfigTypeDef",
    "PeerVpcResultTypeDef",
    "PortInfoTypeDef",
    "PutAlarmResultTypeDef",
    "PutInstancePublicPortsResultTypeDef",
    "RebootInstanceResultTypeDef",
    "RebootRelationalDatabaseResultTypeDef",
    "RegisterContainerImageResultTypeDef",
    "ReleaseStaticIpResultTypeDef",
    "ResetDistributionCacheResultTypeDef",
    "SendContactMethodVerificationResultTypeDef",
    "SetIpAddressTypeResultTypeDef",
    "StartInstanceResultTypeDef",
    "StartRelationalDatabaseResultTypeDef",
    "StopInstanceResultTypeDef",
    "StopRelationalDatabaseResultTypeDef",
    "TagResourceResultTypeDef",
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

AddOnTypeDef = TypedDict(
    "AddOnTypeDef",
    {"name": str, "status": str, "snapshotTimeOfDay": str, "nextSnapshotTimeOfDay": str},
    total=False,
)

AlarmTypeDef = TypedDict(
    "AlarmTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "supportCode": str,
        "monitoredResourceInfo": "MonitoredResourceInfoTypeDef",
        "comparisonOperator": ComparisonOperator,
        "evaluationPeriods": int,
        "period": int,
        "threshold": float,
        "datapointsToAlarm": int,
        "treatMissingData": TreatMissingData,
        "statistic": MetricStatistic,
        "metricName": MetricName,
        "state": AlarmState,
        "unit": MetricUnit,
        "contactProtocols": List[ContactProtocol],
        "notificationTriggers": List[AlarmState],
        "notificationEnabled": bool,
    },
    total=False,
)

AttachedDiskTypeDef = TypedDict("AttachedDiskTypeDef", {"path": str, "sizeInGb": int}, total=False)

AutoSnapshotAddOnRequestTypeDef = TypedDict(
    "AutoSnapshotAddOnRequestTypeDef", {"snapshotTimeOfDay": str}, total=False
)

AutoSnapshotDetailsTypeDef = TypedDict(
    "AutoSnapshotDetailsTypeDef",
    {
        "date": str,
        "createdAt": datetime,
        "status": AutoSnapshotStatus,
        "fromAttachedDisks": List["AttachedDiskTypeDef"],
    },
    total=False,
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef", {"zoneName": str, "state": str}, total=False
)

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

BundleTypeDef = TypedDict(
    "BundleTypeDef",
    {
        "price": float,
        "cpuCount": int,
        "diskSizeInGb": int,
        "bundleId": str,
        "instanceType": str,
        "isActive": bool,
        "name": str,
        "power": int,
        "ramSizeInGb": float,
        "transferPerMonthInGb": int,
        "supportedPlatforms": List[InstancePlatform],
    },
    total=False,
)

CacheBehaviorPerPathTypeDef = TypedDict(
    "CacheBehaviorPerPathTypeDef", {"path": str, "behavior": BehaviorEnum}, total=False
)

CacheBehaviorTypeDef = TypedDict("CacheBehaviorTypeDef", {"behavior": BehaviorEnum}, total=False)

CacheSettingsTypeDef = TypedDict(
    "CacheSettingsTypeDef",
    {
        "defaultTTL": int,
        "minimumTTL": int,
        "maximumTTL": int,
        "allowedHTTPMethods": str,
        "cachedHTTPMethods": str,
        "forwardedCookies": "CookieObjectTypeDef",
        "forwardedHeaders": "HeaderObjectTypeDef",
        "forwardedQueryStrings": "QueryStringObjectTypeDef",
    },
    total=False,
)

CertificateSummaryTypeDef = TypedDict(
    "CertificateSummaryTypeDef",
    {
        "certificateArn": str,
        "certificateName": str,
        "domainName": str,
        "certificateDetail": "CertificateTypeDef",
        "tags": List["TagTypeDef"],
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "arn": str,
        "name": str,
        "domainName": str,
        "status": CertificateStatus,
        "serialNumber": str,
        "subjectAlternativeNames": List[str],
        "domainValidationRecords": List["DomainValidationRecordTypeDef"],
        "requestFailureReason": str,
        "inUseResourceCount": int,
        "keyAlgorithm": str,
        "createdAt": datetime,
        "issuedAt": datetime,
        "issuerCA": str,
        "notBefore": datetime,
        "notAfter": datetime,
        "eligibleToRenew": str,
        "renewalSummary": "RenewalSummaryTypeDef",
        "revokedAt": datetime,
        "revocationReason": str,
        "tags": List["TagTypeDef"],
        "supportCode": str,
    },
    total=False,
)

CloudFormationStackRecordSourceInfoTypeDef = TypedDict(
    "CloudFormationStackRecordSourceInfoTypeDef",
    {"resourceType": CloudFormationStackRecordSourceType, "name": str, "arn": str},
    total=False,
)

CloudFormationStackRecordTypeDef = TypedDict(
    "CloudFormationStackRecordTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "state": RecordState,
        "sourceInfo": List["CloudFormationStackRecordSourceInfoTypeDef"],
        "destinationInfo": "DestinationInfoTypeDef",
    },
    total=False,
)

ContactMethodTypeDef = TypedDict(
    "ContactMethodTypeDef",
    {
        "contactEndpoint": str,
        "status": ContactMethodStatus,
        "protocol": ContactProtocol,
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "supportCode": str,
    },
    total=False,
)

ContainerImageTypeDef = TypedDict(
    "ContainerImageTypeDef", {"image": str, "digest": str, "createdAt": datetime}, total=False
)

ContainerServiceDeploymentTypeDef = TypedDict(
    "ContainerServiceDeploymentTypeDef",
    {
        "version": int,
        "state": ContainerServiceDeploymentState,
        "containers": Dict[str, "ContainerTypeDef"],
        "publicEndpoint": "ContainerServiceEndpointTypeDef",
        "createdAt": datetime,
    },
    total=False,
)

ContainerServiceEndpointTypeDef = TypedDict(
    "ContainerServiceEndpointTypeDef",
    {
        "containerName": str,
        "containerPort": int,
        "healthCheck": "ContainerServiceHealthCheckConfigTypeDef",
    },
    total=False,
)

ContainerServiceHealthCheckConfigTypeDef = TypedDict(
    "ContainerServiceHealthCheckConfigTypeDef",
    {
        "healthyThreshold": int,
        "unhealthyThreshold": int,
        "timeoutSeconds": int,
        "intervalSeconds": int,
        "path": str,
        "successCodes": str,
    },
    total=False,
)

ContainerServiceLogEventTypeDef = TypedDict(
    "ContainerServiceLogEventTypeDef", {"createdAt": datetime, "message": str}, total=False
)

ContainerServicePowerTypeDef = TypedDict(
    "ContainerServicePowerTypeDef",
    {
        "powerId": str,
        "price": float,
        "cpuCount": float,
        "ramSizeInGb": float,
        "name": str,
        "isActive": bool,
    },
    total=False,
)

ContainerServiceRegistryLoginTypeDef = TypedDict(
    "ContainerServiceRegistryLoginTypeDef",
    {"username": str, "password": str, "expiresAt": datetime, "registry": str},
    total=False,
)

ContainerServiceStateDetailTypeDef = TypedDict(
    "ContainerServiceStateDetailTypeDef",
    {"code": ContainerServiceStateDetailCode, "message": str},
    total=False,
)

ContainerServiceTypeDef = TypedDict(
    "ContainerServiceTypeDef",
    {
        "containerServiceName": str,
        "arn": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "tags": List["TagTypeDef"],
        "power": ContainerServicePowerName,
        "powerId": str,
        "state": ContainerServiceState,
        "stateDetail": "ContainerServiceStateDetailTypeDef",
        "scale": int,
        "currentDeployment": "ContainerServiceDeploymentTypeDef",
        "nextDeployment": "ContainerServiceDeploymentTypeDef",
        "isDisabled": bool,
        "principalArn": str,
        "privateDomainName": str,
        "publicDomainNames": Dict[str, List[str]],
        "url": str,
    },
    total=False,
)

ContainerTypeDef = TypedDict(
    "ContainerTypeDef",
    {
        "image": str,
        "command": List[str],
        "environment": Dict[str, str],
        "ports": Dict[str, ContainerServiceProtocol],
    },
    total=False,
)

CookieObjectTypeDef = TypedDict(
    "CookieObjectTypeDef", {"option": ForwardValues, "cookiesAllowList": List[str]}, total=False
)

DestinationInfoTypeDef = TypedDict(
    "DestinationInfoTypeDef", {"id": str, "service": str}, total=False
)

DiskInfoTypeDef = TypedDict(
    "DiskInfoTypeDef",
    {"name": str, "path": str, "sizeInGb": int, "isSystemDisk": bool},
    total=False,
)

DiskSnapshotInfoTypeDef = TypedDict("DiskSnapshotInfoTypeDef", {"sizeInGb": int}, total=False)

DiskSnapshotTypeDef = TypedDict(
    "DiskSnapshotTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "tags": List["TagTypeDef"],
        "sizeInGb": int,
        "state": DiskSnapshotState,
        "progress": str,
        "fromDiskName": str,
        "fromDiskArn": str,
        "fromInstanceName": str,
        "fromInstanceArn": str,
        "isFromAutoSnapshot": bool,
    },
    total=False,
)

DiskTypeDef = TypedDict(
    "DiskTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "tags": List["TagTypeDef"],
        "addOns": List["AddOnTypeDef"],
        "sizeInGb": int,
        "isSystemDisk": bool,
        "iops": int,
        "path": str,
        "state": DiskState,
        "attachedTo": str,
        "isAttached": bool,
        "attachmentState": str,
        "gbInUse": int,
    },
    total=False,
)

DistributionBundleTypeDef = TypedDict(
    "DistributionBundleTypeDef",
    {"bundleId": str, "name": str, "price": float, "transferPerMonthInGb": int, "isActive": bool},
    total=False,
)

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

DomainTypeDef = TypedDict(
    "DomainTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "tags": List["TagTypeDef"],
        "domainEntries": List["DomainEntryTypeDef"],
    },
    total=False,
)

DomainValidationRecordTypeDef = TypedDict(
    "DomainValidationRecordTypeDef",
    {"domainName": str, "resourceRecord": "ResourceRecordTypeDef"},
    total=False,
)

_RequiredEndpointRequestTypeDef = TypedDict(
    "_RequiredEndpointRequestTypeDef", {"containerName": str, "containerPort": int}
)
_OptionalEndpointRequestTypeDef = TypedDict(
    "_OptionalEndpointRequestTypeDef",
    {"healthCheck": "ContainerServiceHealthCheckConfigTypeDef"},
    total=False,
)


class EndpointRequestTypeDef(_RequiredEndpointRequestTypeDef, _OptionalEndpointRequestTypeDef):
    pass


ExportSnapshotRecordSourceInfoTypeDef = TypedDict(
    "ExportSnapshotRecordSourceInfoTypeDef",
    {
        "resourceType": ExportSnapshotRecordSourceType,
        "createdAt": datetime,
        "name": str,
        "arn": str,
        "fromResourceName": str,
        "fromResourceArn": str,
        "instanceSnapshotInfo": "InstanceSnapshotInfoTypeDef",
        "diskSnapshotInfo": "DiskSnapshotInfoTypeDef",
    },
    total=False,
)

ExportSnapshotRecordTypeDef = TypedDict(
    "ExportSnapshotRecordTypeDef",
    {
        "name": str,
        "arn": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "state": RecordState,
        "sourceInfo": "ExportSnapshotRecordSourceInfoTypeDef",
        "destinationInfo": "DestinationInfoTypeDef",
    },
    total=False,
)

HeaderObjectTypeDef = TypedDict(
    "HeaderObjectTypeDef",
    {"option": ForwardValues, "headersAllowList": List[HeaderEnum]},
    total=False,
)

HostKeyAttributesTypeDef = TypedDict(
    "HostKeyAttributesTypeDef",
    {
        "algorithm": str,
        "publicKey": str,
        "witnessedAt": datetime,
        "fingerprintSHA1": str,
        "fingerprintSHA256": str,
        "notValidBefore": datetime,
        "notValidAfter": datetime,
    },
    total=False,
)

InstanceAccessDetailsTypeDef = TypedDict(
    "InstanceAccessDetailsTypeDef",
    {
        "certKey": str,
        "expiresAt": datetime,
        "ipAddress": str,
        "password": str,
        "passwordData": "PasswordDataTypeDef",
        "privateKey": str,
        "protocol": InstanceAccessProtocol,
        "instanceName": str,
        "username": str,
        "hostKeys": List["HostKeyAttributesTypeDef"],
    },
    total=False,
)

InstanceHardwareTypeDef = TypedDict(
    "InstanceHardwareTypeDef",
    {"cpuCount": int, "disks": List["DiskTypeDef"], "ramSizeInGb": float},
    total=False,
)

InstanceHealthSummaryTypeDef = TypedDict(
    "InstanceHealthSummaryTypeDef",
    {
        "instanceName": str,
        "instanceHealth": InstanceHealthState,
        "instanceHealthReason": InstanceHealthReason,
    },
    total=False,
)

InstanceNetworkingTypeDef = TypedDict(
    "InstanceNetworkingTypeDef",
    {"monthlyTransfer": "MonthlyTransferTypeDef", "ports": List["InstancePortInfoTypeDef"]},
    total=False,
)

InstancePortInfoTypeDef = TypedDict(
    "InstancePortInfoTypeDef",
    {
        "fromPort": int,
        "toPort": int,
        "protocol": NetworkProtocol,
        "accessFrom": str,
        "accessType": PortAccessType,
        "commonName": str,
        "accessDirection": AccessDirection,
        "cidrs": List[str],
        "ipv6Cidrs": List[str],
        "cidrListAliases": List[str],
    },
    total=False,
)

InstancePortStateTypeDef = TypedDict(
    "InstancePortStateTypeDef",
    {
        "fromPort": int,
        "toPort": int,
        "protocol": NetworkProtocol,
        "state": PortState,
        "cidrs": List[str],
        "ipv6Cidrs": List[str],
        "cidrListAliases": List[str],
    },
    total=False,
)

InstanceSnapshotInfoTypeDef = TypedDict(
    "InstanceSnapshotInfoTypeDef",
    {"fromBundleId": str, "fromBlueprintId": str, "fromDiskInfo": List["DiskInfoTypeDef"]},
    total=False,
)

InstanceSnapshotTypeDef = TypedDict(
    "InstanceSnapshotTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "tags": List["TagTypeDef"],
        "state": InstanceSnapshotState,
        "progress": str,
        "fromAttachedDisks": List["DiskTypeDef"],
        "fromInstanceName": str,
        "fromInstanceArn": str,
        "fromBlueprintId": str,
        "fromBundleId": str,
        "isFromAutoSnapshot": bool,
        "sizeInGb": int,
    },
    total=False,
)

InstanceStateTypeDef = TypedDict("InstanceStateTypeDef", {"code": int, "name": str}, total=False)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "tags": List["TagTypeDef"],
        "blueprintId": str,
        "blueprintName": str,
        "bundleId": str,
        "addOns": List["AddOnTypeDef"],
        "isStaticIp": bool,
        "privateIpAddress": str,
        "publicIpAddress": str,
        "ipv6Addresses": List[str],
        "ipAddressType": IpAddressType,
        "hardware": "InstanceHardwareTypeDef",
        "networking": "InstanceNetworkingTypeDef",
        "state": "InstanceStateTypeDef",
        "username": str,
        "sshKeyName": str,
    },
    total=False,
)

KeyPairTypeDef = TypedDict(
    "KeyPairTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "tags": List["TagTypeDef"],
        "fingerprint": str,
    },
    total=False,
)

LightsailDistributionTypeDef = TypedDict(
    "LightsailDistributionTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "alternativeDomainNames": List[str],
        "status": str,
        "isEnabled": bool,
        "domainName": str,
        "bundleId": str,
        "certificateName": str,
        "origin": "OriginTypeDef",
        "originPublicDNS": str,
        "defaultCacheBehavior": "CacheBehaviorTypeDef",
        "cacheBehaviorSettings": "CacheSettingsTypeDef",
        "cacheBehaviors": List["CacheBehaviorPerPathTypeDef"],
        "ableToUpdateBundle": bool,
        "ipAddressType": IpAddressType,
        "tags": List["TagTypeDef"],
    },
    total=False,
)

LoadBalancerTlsCertificateDomainValidationOptionTypeDef = TypedDict(
    "LoadBalancerTlsCertificateDomainValidationOptionTypeDef",
    {"domainName": str, "validationStatus": LoadBalancerTlsCertificateDomainStatus},
    total=False,
)

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

LoadBalancerTlsCertificateRenewalSummaryTypeDef = TypedDict(
    "LoadBalancerTlsCertificateRenewalSummaryTypeDef",
    {
        "renewalStatus": LoadBalancerTlsCertificateRenewalStatus,
        "domainValidationOptions": List["LoadBalancerTlsCertificateDomainValidationOptionTypeDef"],
    },
    total=False,
)

LoadBalancerTlsCertificateSummaryTypeDef = TypedDict(
    "LoadBalancerTlsCertificateSummaryTypeDef", {"name": str, "isAttached": bool}, total=False
)

LoadBalancerTlsCertificateTypeDef = TypedDict(
    "LoadBalancerTlsCertificateTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "tags": List["TagTypeDef"],
        "loadBalancerName": str,
        "isAttached": bool,
        "status": LoadBalancerTlsCertificateStatus,
        "domainName": str,
        "domainValidationRecords": List["LoadBalancerTlsCertificateDomainValidationRecordTypeDef"],
        "failureReason": LoadBalancerTlsCertificateFailureReason,
        "issuedAt": datetime,
        "issuer": str,
        "keyAlgorithm": str,
        "notAfter": datetime,
        "notBefore": datetime,
        "renewalSummary": "LoadBalancerTlsCertificateRenewalSummaryTypeDef",
        "revocationReason": LoadBalancerTlsCertificateRevocationReason,
        "revokedAt": datetime,
        "serial": str,
        "signatureAlgorithm": str,
        "subject": str,
        "subjectAlternativeNames": List[str],
    },
    total=False,
)

LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "tags": List["TagTypeDef"],
        "dnsName": str,
        "state": LoadBalancerState,
        "protocol": LoadBalancerProtocol,
        "publicPorts": List[int],
        "healthCheckPath": str,
        "instancePort": int,
        "instanceHealthSummary": List["InstanceHealthSummaryTypeDef"],
        "tlsCertificateSummaries": List["LoadBalancerTlsCertificateSummaryTypeDef"],
        "configurationOptions": Dict[LoadBalancerAttributeName, str],
        "ipAddressType": IpAddressType,
    },
    total=False,
)

LogEventTypeDef = TypedDict("LogEventTypeDef", {"createdAt": datetime, "message": str}, total=False)

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

MonitoredResourceInfoTypeDef = TypedDict(
    "MonitoredResourceInfoTypeDef",
    {"arn": str, "name": str, "resourceType": ResourceType},
    total=False,
)

MonthlyTransferTypeDef = TypedDict(
    "MonthlyTransferTypeDef", {"gbPerMonthAllocated": int}, total=False
)

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

OriginTypeDef = TypedDict(
    "OriginTypeDef",
    {
        "name": str,
        "resourceType": ResourceType,
        "regionName": RegionName,
        "protocolPolicy": OriginProtocolPolicyEnum,
    },
    total=False,
)

PasswordDataTypeDef = TypedDict(
    "PasswordDataTypeDef", {"ciphertext": str, "keyPairName": str}, total=False
)

PendingMaintenanceActionTypeDef = TypedDict(
    "PendingMaintenanceActionTypeDef",
    {"action": str, "description": str, "currentApplyDate": datetime},
    total=False,
)

PendingModifiedRelationalDatabaseValuesTypeDef = TypedDict(
    "PendingModifiedRelationalDatabaseValuesTypeDef",
    {"masterUserPassword": str, "engineVersion": str, "backupRetentionEnabled": bool},
    total=False,
)

QueryStringObjectTypeDef = TypedDict(
    "QueryStringObjectTypeDef", {"option": bool, "queryStringsAllowList": List[str]}, total=False
)

RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "continentCode": str,
        "description": str,
        "displayName": str,
        "name": RegionName,
        "availabilityZones": List["AvailabilityZoneTypeDef"],
        "relationalDatabaseAvailabilityZones": List["AvailabilityZoneTypeDef"],
    },
    total=False,
)

RelationalDatabaseBlueprintTypeDef = TypedDict(
    "RelationalDatabaseBlueprintTypeDef",
    {
        "blueprintId": str,
        "engine": RelationalDatabaseEngine,
        "engineVersion": str,
        "engineDescription": str,
        "engineVersionDescription": str,
        "isEngineDefault": bool,
    },
    total=False,
)

RelationalDatabaseBundleTypeDef = TypedDict(
    "RelationalDatabaseBundleTypeDef",
    {
        "bundleId": str,
        "name": str,
        "price": float,
        "ramSizeInGb": float,
        "diskSizeInGb": int,
        "transferPerMonthInGb": int,
        "cpuCount": int,
        "isEncrypted": bool,
        "isActive": bool,
    },
    total=False,
)

RelationalDatabaseEndpointTypeDef = TypedDict(
    "RelationalDatabaseEndpointTypeDef", {"port": int, "address": str}, total=False
)

RelationalDatabaseEventTypeDef = TypedDict(
    "RelationalDatabaseEventTypeDef",
    {"resource": str, "createdAt": datetime, "message": str, "eventCategories": List[str]},
    total=False,
)

RelationalDatabaseHardwareTypeDef = TypedDict(
    "RelationalDatabaseHardwareTypeDef",
    {"cpuCount": int, "diskSizeInGb": int, "ramSizeInGb": float},
    total=False,
)

RelationalDatabaseParameterTypeDef = TypedDict(
    "RelationalDatabaseParameterTypeDef",
    {
        "allowedValues": str,
        "applyMethod": str,
        "applyType": str,
        "dataType": str,
        "description": str,
        "isModifiable": bool,
        "parameterName": str,
        "parameterValue": str,
    },
    total=False,
)

RelationalDatabaseSnapshotTypeDef = TypedDict(
    "RelationalDatabaseSnapshotTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "tags": List["TagTypeDef"],
        "engine": str,
        "engineVersion": str,
        "sizeInGb": int,
        "state": str,
        "fromRelationalDatabaseName": str,
        "fromRelationalDatabaseArn": str,
        "fromRelationalDatabaseBundleId": str,
        "fromRelationalDatabaseBlueprintId": str,
    },
    total=False,
)

RelationalDatabaseTypeDef = TypedDict(
    "RelationalDatabaseTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "tags": List["TagTypeDef"],
        "relationalDatabaseBlueprintId": str,
        "relationalDatabaseBundleId": str,
        "masterDatabaseName": str,
        "hardware": "RelationalDatabaseHardwareTypeDef",
        "state": str,
        "secondaryAvailabilityZone": str,
        "backupRetentionEnabled": bool,
        "pendingModifiedValues": "PendingModifiedRelationalDatabaseValuesTypeDef",
        "engine": str,
        "engineVersion": str,
        "latestRestorableTime": datetime,
        "masterUsername": str,
        "parameterApplyStatus": str,
        "preferredBackupWindow": str,
        "preferredMaintenanceWindow": str,
        "publiclyAccessible": bool,
        "masterEndpoint": "RelationalDatabaseEndpointTypeDef",
        "pendingMaintenanceActions": List["PendingMaintenanceActionTypeDef"],
        "caCertificateIdentifier": str,
    },
    total=False,
)

RenewalSummaryTypeDef = TypedDict(
    "RenewalSummaryTypeDef",
    {
        "domainValidationRecords": List["DomainValidationRecordTypeDef"],
        "renewalStatus": RenewalStatus,
        "renewalStatusReason": str,
        "updatedAt": datetime,
    },
    total=False,
)

ResourceLocationTypeDef = TypedDict(
    "ResourceLocationTypeDef", {"availabilityZone": str, "regionName": RegionName}, total=False
)

ResourceRecordTypeDef = TypedDict(
    "ResourceRecordTypeDef", {"name": str, "type": str, "value": str}, total=False
)

StaticIpTypeDef = TypedDict(
    "StaticIpTypeDef",
    {
        "name": str,
        "arn": str,
        "supportCode": str,
        "createdAt": datetime,
        "location": "ResourceLocationTypeDef",
        "resourceType": ResourceType,
        "ipAddress": str,
        "attachedTo": str,
        "isAttached": bool,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str}, total=False)

_RequiredAddOnRequestTypeDef = TypedDict("_RequiredAddOnRequestTypeDef", {"addOnType": AddOnType})
_OptionalAddOnRequestTypeDef = TypedDict(
    "_OptionalAddOnRequestTypeDef",
    {"autoSnapshotAddOnRequest": "AutoSnapshotAddOnRequestTypeDef"},
    total=False,
)


class AddOnRequestTypeDef(_RequiredAddOnRequestTypeDef, _OptionalAddOnRequestTypeDef):
    pass


AllocateStaticIpResultTypeDef = TypedDict(
    "AllocateStaticIpResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

AttachCertificateToDistributionResultTypeDef = TypedDict(
    "AttachCertificateToDistributionResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

AttachDiskResultTypeDef = TypedDict(
    "AttachDiskResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

AttachInstancesToLoadBalancerResultTypeDef = TypedDict(
    "AttachInstancesToLoadBalancerResultTypeDef",
    {"operations": List["OperationTypeDef"]},
    total=False,
)

AttachLoadBalancerTlsCertificateResultTypeDef = TypedDict(
    "AttachLoadBalancerTlsCertificateResultTypeDef",
    {"operations": List["OperationTypeDef"]},
    total=False,
)

AttachStaticIpResultTypeDef = TypedDict(
    "AttachStaticIpResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

CloseInstancePublicPortsResultTypeDef = TypedDict(
    "CloseInstancePublicPortsResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

ContainerServiceDeploymentRequestTypeDef = TypedDict(
    "ContainerServiceDeploymentRequestTypeDef",
    {"containers": Dict[str, "ContainerTypeDef"], "publicEndpoint": "EndpointRequestTypeDef"},
    total=False,
)

ContainerServicesListResultTypeDef = TypedDict(
    "ContainerServicesListResultTypeDef",
    {"containerServices": List["ContainerServiceTypeDef"]},
    total=False,
)

CopySnapshotResultTypeDef = TypedDict(
    "CopySnapshotResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

CreateCertificateResultTypeDef = TypedDict(
    "CreateCertificateResultTypeDef",
    {"certificate": "CertificateSummaryTypeDef", "operations": List["OperationTypeDef"]},
    total=False,
)

CreateCloudFormationStackResultTypeDef = TypedDict(
    "CreateCloudFormationStackResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

CreateContactMethodResultTypeDef = TypedDict(
    "CreateContactMethodResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

CreateContainerServiceDeploymentResultTypeDef = TypedDict(
    "CreateContainerServiceDeploymentResultTypeDef",
    {"containerService": "ContainerServiceTypeDef"},
    total=False,
)

CreateContainerServiceRegistryLoginResultTypeDef = TypedDict(
    "CreateContainerServiceRegistryLoginResultTypeDef",
    {"registryLogin": "ContainerServiceRegistryLoginTypeDef"},
    total=False,
)

CreateContainerServiceResultTypeDef = TypedDict(
    "CreateContainerServiceResultTypeDef",
    {"containerService": "ContainerServiceTypeDef"},
    total=False,
)

CreateDiskFromSnapshotResultTypeDef = TypedDict(
    "CreateDiskFromSnapshotResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

CreateDiskResultTypeDef = TypedDict(
    "CreateDiskResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

CreateDiskSnapshotResultTypeDef = TypedDict(
    "CreateDiskSnapshotResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

CreateDistributionResultTypeDef = TypedDict(
    "CreateDistributionResultTypeDef",
    {"distribution": "LightsailDistributionTypeDef", "operation": "OperationTypeDef"},
    total=False,
)

CreateDomainEntryResultTypeDef = TypedDict(
    "CreateDomainEntryResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

CreateDomainResultTypeDef = TypedDict(
    "CreateDomainResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

CreateInstanceSnapshotResultTypeDef = TypedDict(
    "CreateInstanceSnapshotResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

CreateInstancesFromSnapshotResultTypeDef = TypedDict(
    "CreateInstancesFromSnapshotResultTypeDef",
    {"operations": List["OperationTypeDef"]},
    total=False,
)

CreateInstancesResultTypeDef = TypedDict(
    "CreateInstancesResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

CreateKeyPairResultTypeDef = TypedDict(
    "CreateKeyPairResultTypeDef",
    {
        "keyPair": "KeyPairTypeDef",
        "publicKeyBase64": str,
        "privateKeyBase64": str,
        "operation": "OperationTypeDef",
    },
    total=False,
)

CreateLoadBalancerResultTypeDef = TypedDict(
    "CreateLoadBalancerResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

CreateLoadBalancerTlsCertificateResultTypeDef = TypedDict(
    "CreateLoadBalancerTlsCertificateResultTypeDef",
    {"operations": List["OperationTypeDef"]},
    total=False,
)

CreateRelationalDatabaseFromSnapshotResultTypeDef = TypedDict(
    "CreateRelationalDatabaseFromSnapshotResultTypeDef",
    {"operations": List["OperationTypeDef"]},
    total=False,
)

CreateRelationalDatabaseResultTypeDef = TypedDict(
    "CreateRelationalDatabaseResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

CreateRelationalDatabaseSnapshotResultTypeDef = TypedDict(
    "CreateRelationalDatabaseSnapshotResultTypeDef",
    {"operations": List["OperationTypeDef"]},
    total=False,
)

DeleteAlarmResultTypeDef = TypedDict(
    "DeleteAlarmResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

DeleteAutoSnapshotResultTypeDef = TypedDict(
    "DeleteAutoSnapshotResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

DeleteCertificateResultTypeDef = TypedDict(
    "DeleteCertificateResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

DeleteContactMethodResultTypeDef = TypedDict(
    "DeleteContactMethodResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

DeleteDiskResultTypeDef = TypedDict(
    "DeleteDiskResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

DeleteDiskSnapshotResultTypeDef = TypedDict(
    "DeleteDiskSnapshotResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

DeleteDistributionResultTypeDef = TypedDict(
    "DeleteDistributionResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

DeleteDomainEntryResultTypeDef = TypedDict(
    "DeleteDomainEntryResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

DeleteDomainResultTypeDef = TypedDict(
    "DeleteDomainResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

DeleteInstanceResultTypeDef = TypedDict(
    "DeleteInstanceResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

DeleteInstanceSnapshotResultTypeDef = TypedDict(
    "DeleteInstanceSnapshotResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

DeleteKeyPairResultTypeDef = TypedDict(
    "DeleteKeyPairResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

DeleteKnownHostKeysResultTypeDef = TypedDict(
    "DeleteKnownHostKeysResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

DeleteLoadBalancerResultTypeDef = TypedDict(
    "DeleteLoadBalancerResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

DeleteLoadBalancerTlsCertificateResultTypeDef = TypedDict(
    "DeleteLoadBalancerTlsCertificateResultTypeDef",
    {"operations": List["OperationTypeDef"]},
    total=False,
)

DeleteRelationalDatabaseResultTypeDef = TypedDict(
    "DeleteRelationalDatabaseResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

DeleteRelationalDatabaseSnapshotResultTypeDef = TypedDict(
    "DeleteRelationalDatabaseSnapshotResultTypeDef",
    {"operations": List["OperationTypeDef"]},
    total=False,
)

DetachCertificateFromDistributionResultTypeDef = TypedDict(
    "DetachCertificateFromDistributionResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

DetachDiskResultTypeDef = TypedDict(
    "DetachDiskResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

DetachInstancesFromLoadBalancerResultTypeDef = TypedDict(
    "DetachInstancesFromLoadBalancerResultTypeDef",
    {"operations": List["OperationTypeDef"]},
    total=False,
)

DetachStaticIpResultTypeDef = TypedDict(
    "DetachStaticIpResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

DisableAddOnResultTypeDef = TypedDict(
    "DisableAddOnResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

DiskMapTypeDef = TypedDict(
    "DiskMapTypeDef", {"originalDiskPath": str, "newDiskName": str}, total=False
)

DownloadDefaultKeyPairResultTypeDef = TypedDict(
    "DownloadDefaultKeyPairResultTypeDef",
    {"publicKeyBase64": str, "privateKeyBase64": str},
    total=False,
)

EnableAddOnResultTypeDef = TypedDict(
    "EnableAddOnResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

ExportSnapshotResultTypeDef = TypedDict(
    "ExportSnapshotResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

GetActiveNamesResultTypeDef = TypedDict(
    "GetActiveNamesResultTypeDef", {"activeNames": List[str], "nextPageToken": str}, total=False
)

GetAlarmsResultTypeDef = TypedDict(
    "GetAlarmsResultTypeDef", {"alarms": List["AlarmTypeDef"], "nextPageToken": str}, total=False
)

GetAutoSnapshotsResultTypeDef = TypedDict(
    "GetAutoSnapshotsResultTypeDef",
    {
        "resourceName": str,
        "resourceType": ResourceType,
        "autoSnapshots": List["AutoSnapshotDetailsTypeDef"],
    },
    total=False,
)

GetBlueprintsResultTypeDef = TypedDict(
    "GetBlueprintsResultTypeDef",
    {"blueprints": List["BlueprintTypeDef"], "nextPageToken": str},
    total=False,
)

GetBundlesResultTypeDef = TypedDict(
    "GetBundlesResultTypeDef", {"bundles": List["BundleTypeDef"], "nextPageToken": str}, total=False
)

GetCertificatesResultTypeDef = TypedDict(
    "GetCertificatesResultTypeDef", {"certificates": List["CertificateSummaryTypeDef"]}, total=False
)

GetCloudFormationStackRecordsResultTypeDef = TypedDict(
    "GetCloudFormationStackRecordsResultTypeDef",
    {"cloudFormationStackRecords": List["CloudFormationStackRecordTypeDef"], "nextPageToken": str},
    total=False,
)

GetContactMethodsResultTypeDef = TypedDict(
    "GetContactMethodsResultTypeDef", {"contactMethods": List["ContactMethodTypeDef"]}, total=False
)

GetContainerAPIMetadataResultTypeDef = TypedDict(
    "GetContainerAPIMetadataResultTypeDef", {"metadata": List[Dict[str, str]]}, total=False
)

GetContainerImagesResultTypeDef = TypedDict(
    "GetContainerImagesResultTypeDef",
    {"containerImages": List["ContainerImageTypeDef"]},
    total=False,
)

GetContainerLogResultTypeDef = TypedDict(
    "GetContainerLogResultTypeDef",
    {"logEvents": List["ContainerServiceLogEventTypeDef"], "nextPageToken": str},
    total=False,
)

GetContainerServiceDeploymentsResultTypeDef = TypedDict(
    "GetContainerServiceDeploymentsResultTypeDef",
    {"deployments": List["ContainerServiceDeploymentTypeDef"]},
    total=False,
)

GetContainerServiceMetricDataResultTypeDef = TypedDict(
    "GetContainerServiceMetricDataResultTypeDef",
    {"metricName": ContainerServiceMetricName, "metricData": List["MetricDatapointTypeDef"]},
    total=False,
)

GetContainerServicePowersResultTypeDef = TypedDict(
    "GetContainerServicePowersResultTypeDef",
    {"powers": List["ContainerServicePowerTypeDef"]},
    total=False,
)

GetDiskResultTypeDef = TypedDict("GetDiskResultTypeDef", {"disk": "DiskTypeDef"}, total=False)

GetDiskSnapshotResultTypeDef = TypedDict(
    "GetDiskSnapshotResultTypeDef", {"diskSnapshot": "DiskSnapshotTypeDef"}, total=False
)

GetDiskSnapshotsResultTypeDef = TypedDict(
    "GetDiskSnapshotsResultTypeDef",
    {"diskSnapshots": List["DiskSnapshotTypeDef"], "nextPageToken": str},
    total=False,
)

GetDisksResultTypeDef = TypedDict(
    "GetDisksResultTypeDef", {"disks": List["DiskTypeDef"], "nextPageToken": str}, total=False
)

GetDistributionBundlesResultTypeDef = TypedDict(
    "GetDistributionBundlesResultTypeDef",
    {"bundles": List["DistributionBundleTypeDef"]},
    total=False,
)

GetDistributionLatestCacheResetResultTypeDef = TypedDict(
    "GetDistributionLatestCacheResetResultTypeDef",
    {"status": str, "createTime": datetime},
    total=False,
)

GetDistributionMetricDataResultTypeDef = TypedDict(
    "GetDistributionMetricDataResultTypeDef",
    {"metricName": DistributionMetricName, "metricData": List["MetricDatapointTypeDef"]},
    total=False,
)

GetDistributionsResultTypeDef = TypedDict(
    "GetDistributionsResultTypeDef",
    {"distributions": List["LightsailDistributionTypeDef"], "nextPageToken": str},
    total=False,
)

GetDomainResultTypeDef = TypedDict(
    "GetDomainResultTypeDef", {"domain": "DomainTypeDef"}, total=False
)

GetDomainsResultTypeDef = TypedDict(
    "GetDomainsResultTypeDef", {"domains": List["DomainTypeDef"], "nextPageToken": str}, total=False
)

GetExportSnapshotRecordsResultTypeDef = TypedDict(
    "GetExportSnapshotRecordsResultTypeDef",
    {"exportSnapshotRecords": List["ExportSnapshotRecordTypeDef"], "nextPageToken": str},
    total=False,
)

GetInstanceAccessDetailsResultTypeDef = TypedDict(
    "GetInstanceAccessDetailsResultTypeDef",
    {"accessDetails": "InstanceAccessDetailsTypeDef"},
    total=False,
)

GetInstanceMetricDataResultTypeDef = TypedDict(
    "GetInstanceMetricDataResultTypeDef",
    {"metricName": InstanceMetricName, "metricData": List["MetricDatapointTypeDef"]},
    total=False,
)

GetInstancePortStatesResultTypeDef = TypedDict(
    "GetInstancePortStatesResultTypeDef",
    {"portStates": List["InstancePortStateTypeDef"]},
    total=False,
)

GetInstanceResultTypeDef = TypedDict(
    "GetInstanceResultTypeDef", {"instance": "InstanceTypeDef"}, total=False
)

GetInstanceSnapshotResultTypeDef = TypedDict(
    "GetInstanceSnapshotResultTypeDef", {"instanceSnapshot": "InstanceSnapshotTypeDef"}, total=False
)

GetInstanceSnapshotsResultTypeDef = TypedDict(
    "GetInstanceSnapshotsResultTypeDef",
    {"instanceSnapshots": List["InstanceSnapshotTypeDef"], "nextPageToken": str},
    total=False,
)

GetInstanceStateResultTypeDef = TypedDict(
    "GetInstanceStateResultTypeDef", {"state": "InstanceStateTypeDef"}, total=False
)

GetInstancesResultTypeDef = TypedDict(
    "GetInstancesResultTypeDef",
    {"instances": List["InstanceTypeDef"], "nextPageToken": str},
    total=False,
)

GetKeyPairResultTypeDef = TypedDict(
    "GetKeyPairResultTypeDef", {"keyPair": "KeyPairTypeDef"}, total=False
)

GetKeyPairsResultTypeDef = TypedDict(
    "GetKeyPairsResultTypeDef",
    {"keyPairs": List["KeyPairTypeDef"], "nextPageToken": str},
    total=False,
)

GetLoadBalancerMetricDataResultTypeDef = TypedDict(
    "GetLoadBalancerMetricDataResultTypeDef",
    {"metricName": LoadBalancerMetricName, "metricData": List["MetricDatapointTypeDef"]},
    total=False,
)

GetLoadBalancerResultTypeDef = TypedDict(
    "GetLoadBalancerResultTypeDef", {"loadBalancer": "LoadBalancerTypeDef"}, total=False
)

GetLoadBalancerTlsCertificatesResultTypeDef = TypedDict(
    "GetLoadBalancerTlsCertificatesResultTypeDef",
    {"tlsCertificates": List["LoadBalancerTlsCertificateTypeDef"]},
    total=False,
)

GetLoadBalancersResultTypeDef = TypedDict(
    "GetLoadBalancersResultTypeDef",
    {"loadBalancers": List["LoadBalancerTypeDef"], "nextPageToken": str},
    total=False,
)

GetOperationResultTypeDef = TypedDict(
    "GetOperationResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

GetOperationsForResourceResultTypeDef = TypedDict(
    "GetOperationsForResourceResultTypeDef",
    {"operations": List["OperationTypeDef"], "nextPageCount": str, "nextPageToken": str},
    total=False,
)

GetOperationsResultTypeDef = TypedDict(
    "GetOperationsResultTypeDef",
    {"operations": List["OperationTypeDef"], "nextPageToken": str},
    total=False,
)

GetRegionsResultTypeDef = TypedDict(
    "GetRegionsResultTypeDef", {"regions": List["RegionTypeDef"]}, total=False
)

GetRelationalDatabaseBlueprintsResultTypeDef = TypedDict(
    "GetRelationalDatabaseBlueprintsResultTypeDef",
    {"blueprints": List["RelationalDatabaseBlueprintTypeDef"], "nextPageToken": str},
    total=False,
)

GetRelationalDatabaseBundlesResultTypeDef = TypedDict(
    "GetRelationalDatabaseBundlesResultTypeDef",
    {"bundles": List["RelationalDatabaseBundleTypeDef"], "nextPageToken": str},
    total=False,
)

GetRelationalDatabaseEventsResultTypeDef = TypedDict(
    "GetRelationalDatabaseEventsResultTypeDef",
    {"relationalDatabaseEvents": List["RelationalDatabaseEventTypeDef"], "nextPageToken": str},
    total=False,
)

GetRelationalDatabaseLogEventsResultTypeDef = TypedDict(
    "GetRelationalDatabaseLogEventsResultTypeDef",
    {
        "resourceLogEvents": List["LogEventTypeDef"],
        "nextBackwardToken": str,
        "nextForwardToken": str,
    },
    total=False,
)

GetRelationalDatabaseLogStreamsResultTypeDef = TypedDict(
    "GetRelationalDatabaseLogStreamsResultTypeDef", {"logStreams": List[str]}, total=False
)

GetRelationalDatabaseMasterUserPasswordResultTypeDef = TypedDict(
    "GetRelationalDatabaseMasterUserPasswordResultTypeDef",
    {"masterUserPassword": str, "createdAt": datetime},
    total=False,
)

GetRelationalDatabaseMetricDataResultTypeDef = TypedDict(
    "GetRelationalDatabaseMetricDataResultTypeDef",
    {"metricName": RelationalDatabaseMetricName, "metricData": List["MetricDatapointTypeDef"]},
    total=False,
)

GetRelationalDatabaseParametersResultTypeDef = TypedDict(
    "GetRelationalDatabaseParametersResultTypeDef",
    {"parameters": List["RelationalDatabaseParameterTypeDef"], "nextPageToken": str},
    total=False,
)

GetRelationalDatabaseResultTypeDef = TypedDict(
    "GetRelationalDatabaseResultTypeDef",
    {"relationalDatabase": "RelationalDatabaseTypeDef"},
    total=False,
)

GetRelationalDatabaseSnapshotResultTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotResultTypeDef",
    {"relationalDatabaseSnapshot": "RelationalDatabaseSnapshotTypeDef"},
    total=False,
)

GetRelationalDatabaseSnapshotsResultTypeDef = TypedDict(
    "GetRelationalDatabaseSnapshotsResultTypeDef",
    {
        "relationalDatabaseSnapshots": List["RelationalDatabaseSnapshotTypeDef"],
        "nextPageToken": str,
    },
    total=False,
)

GetRelationalDatabasesResultTypeDef = TypedDict(
    "GetRelationalDatabasesResultTypeDef",
    {"relationalDatabases": List["RelationalDatabaseTypeDef"], "nextPageToken": str},
    total=False,
)

GetStaticIpResultTypeDef = TypedDict(
    "GetStaticIpResultTypeDef", {"staticIp": "StaticIpTypeDef"}, total=False
)

GetStaticIpsResultTypeDef = TypedDict(
    "GetStaticIpsResultTypeDef",
    {"staticIps": List["StaticIpTypeDef"], "nextPageToken": str},
    total=False,
)

ImportKeyPairResultTypeDef = TypedDict(
    "ImportKeyPairResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

InputOriginTypeDef = TypedDict(
    "InputOriginTypeDef",
    {"name": str, "regionName": RegionName, "protocolPolicy": OriginProtocolPolicyEnum},
    total=False,
)

_RequiredInstanceEntryTypeDef = TypedDict(
    "_RequiredInstanceEntryTypeDef",
    {
        "sourceName": str,
        "instanceType": str,
        "portInfoSource": PortInfoSourceType,
        "availabilityZone": str,
    },
)
_OptionalInstanceEntryTypeDef = TypedDict(
    "_OptionalInstanceEntryTypeDef", {"userData": str}, total=False
)


class InstanceEntryTypeDef(_RequiredInstanceEntryTypeDef, _OptionalInstanceEntryTypeDef):
    pass


IsVpcPeeredResultTypeDef = TypedDict("IsVpcPeeredResultTypeDef", {"isPeered": bool}, total=False)

OpenInstancePublicPortsResultTypeDef = TypedDict(
    "OpenInstancePublicPortsResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PeerVpcResultTypeDef = TypedDict(
    "PeerVpcResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

PortInfoTypeDef = TypedDict(
    "PortInfoTypeDef",
    {
        "fromPort": int,
        "toPort": int,
        "protocol": NetworkProtocol,
        "cidrs": List[str],
        "ipv6Cidrs": List[str],
        "cidrListAliases": List[str],
    },
    total=False,
)

PutAlarmResultTypeDef = TypedDict(
    "PutAlarmResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

PutInstancePublicPortsResultTypeDef = TypedDict(
    "PutInstancePublicPortsResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

RebootInstanceResultTypeDef = TypedDict(
    "RebootInstanceResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

RebootRelationalDatabaseResultTypeDef = TypedDict(
    "RebootRelationalDatabaseResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

RegisterContainerImageResultTypeDef = TypedDict(
    "RegisterContainerImageResultTypeDef", {"containerImage": "ContainerImageTypeDef"}, total=False
)

ReleaseStaticIpResultTypeDef = TypedDict(
    "ReleaseStaticIpResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

ResetDistributionCacheResultTypeDef = TypedDict(
    "ResetDistributionCacheResultTypeDef",
    {"status": str, "createTime": datetime, "operation": "OperationTypeDef"},
    total=False,
)

SendContactMethodVerificationResultTypeDef = TypedDict(
    "SendContactMethodVerificationResultTypeDef",
    {"operations": List["OperationTypeDef"]},
    total=False,
)

SetIpAddressTypeResultTypeDef = TypedDict(
    "SetIpAddressTypeResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

StartInstanceResultTypeDef = TypedDict(
    "StartInstanceResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

StartRelationalDatabaseResultTypeDef = TypedDict(
    "StartRelationalDatabaseResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

StopInstanceResultTypeDef = TypedDict(
    "StopInstanceResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

StopRelationalDatabaseResultTypeDef = TypedDict(
    "StopRelationalDatabaseResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

TagResourceResultTypeDef = TypedDict(
    "TagResourceResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

TestAlarmResultTypeDef = TypedDict(
    "TestAlarmResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

UnpeerVpcResultTypeDef = TypedDict(
    "UnpeerVpcResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

UntagResourceResultTypeDef = TypedDict(
    "UntagResourceResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

UpdateContainerServiceResultTypeDef = TypedDict(
    "UpdateContainerServiceResultTypeDef",
    {"containerService": "ContainerServiceTypeDef"},
    total=False,
)

UpdateDistributionBundleResultTypeDef = TypedDict(
    "UpdateDistributionBundleResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

UpdateDistributionResultTypeDef = TypedDict(
    "UpdateDistributionResultTypeDef", {"operation": "OperationTypeDef"}, total=False
)

UpdateDomainEntryResultTypeDef = TypedDict(
    "UpdateDomainEntryResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)

UpdateLoadBalancerAttributeResultTypeDef = TypedDict(
    "UpdateLoadBalancerAttributeResultTypeDef",
    {"operations": List["OperationTypeDef"]},
    total=False,
)

UpdateRelationalDatabaseParametersResultTypeDef = TypedDict(
    "UpdateRelationalDatabaseParametersResultTypeDef",
    {"operations": List["OperationTypeDef"]},
    total=False,
)

UpdateRelationalDatabaseResultTypeDef = TypedDict(
    "UpdateRelationalDatabaseResultTypeDef", {"operations": List["OperationTypeDef"]}, total=False
)
