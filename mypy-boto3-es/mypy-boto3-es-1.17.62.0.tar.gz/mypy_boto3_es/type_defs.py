"""
Main interface for es service type definitions.

Usage::

    ```python
    from mypy_boto3_es.type_defs import AccessPoliciesStatusTypeDef

    data: AccessPoliciesStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_es.literals import (
    AutoTuneDesiredState,
    AutoTuneState,
    AutoTuneType,
    DeploymentStatus,
    DescribePackagesFilterName,
    DomainPackageStatus,
    ESPartitionInstanceType,
    ESWarmPartitionInstanceType,
    InboundCrossClusterSearchConnectionStatusCode,
    LogType,
    OptionState,
    OutboundCrossClusterSearchConnectionStatusCode,
    PackageStatus,
    PackageType,
    ReservedElasticsearchInstancePaymentOption,
    RollbackOnDisable,
    ScheduledAutoTuneActionType,
    ScheduledAutoTuneSeverityType,
    TimeUnit,
    TLSSecurityPolicy,
    UpgradeStatus,
    UpgradeStep,
    VolumeType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessPoliciesStatusTypeDef",
    "AdditionalLimitTypeDef",
    "AdvancedOptionsStatusTypeDef",
    "AdvancedSecurityOptionsStatusTypeDef",
    "AdvancedSecurityOptionsTypeDef",
    "AutoTuneDetailsTypeDef",
    "AutoTuneMaintenanceScheduleTypeDef",
    "AutoTuneOptionsOutputTypeDef",
    "AutoTuneOptionsStatusTypeDef",
    "AutoTuneOptionsTypeDef",
    "AutoTuneStatusTypeDef",
    "AutoTuneTypeDef",
    "CognitoOptionsStatusTypeDef",
    "CognitoOptionsTypeDef",
    "CompatibleVersionsMapTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "DomainEndpointOptionsTypeDef",
    "DomainInfoTypeDef",
    "DomainInformationTypeDef",
    "DomainPackageDetailsTypeDef",
    "DurationTypeDef",
    "EBSOptionsStatusTypeDef",
    "EBSOptionsTypeDef",
    "ElasticsearchClusterConfigStatusTypeDef",
    "ElasticsearchClusterConfigTypeDef",
    "ElasticsearchDomainConfigTypeDef",
    "ElasticsearchDomainStatusTypeDef",
    "ElasticsearchVersionStatusTypeDef",
    "EncryptionAtRestOptionsStatusTypeDef",
    "EncryptionAtRestOptionsTypeDef",
    "ErrorDetailsTypeDef",
    "InboundCrossClusterSearchConnectionStatusTypeDef",
    "InboundCrossClusterSearchConnectionTypeDef",
    "InstanceCountLimitsTypeDef",
    "InstanceLimitsTypeDef",
    "LimitsTypeDef",
    "LogPublishingOptionTypeDef",
    "LogPublishingOptionsStatusTypeDef",
    "MasterUserOptionsTypeDef",
    "NodeToNodeEncryptionOptionsStatusTypeDef",
    "NodeToNodeEncryptionOptionsTypeDef",
    "OptionStatusTypeDef",
    "OutboundCrossClusterSearchConnectionStatusTypeDef",
    "OutboundCrossClusterSearchConnectionTypeDef",
    "PackageDetailsTypeDef",
    "PackageVersionHistoryTypeDef",
    "RecurringChargeTypeDef",
    "ReservedElasticsearchInstanceOfferingTypeDef",
    "ReservedElasticsearchInstanceTypeDef",
    "ResponseMetadata",
    "SAMLIdpTypeDef",
    "SAMLOptionsInputTypeDef",
    "SAMLOptionsOutputTypeDef",
    "ScheduledAutoTuneDetailsTypeDef",
    "ServiceSoftwareOptionsTypeDef",
    "SnapshotOptionsStatusTypeDef",
    "SnapshotOptionsTypeDef",
    "StorageTypeLimitTypeDef",
    "StorageTypeTypeDef",
    "TagTypeDef",
    "UpgradeHistoryTypeDef",
    "UpgradeStepItemTypeDef",
    "VPCDerivedInfoStatusTypeDef",
    "VPCDerivedInfoTypeDef",
    "ZoneAwarenessConfigTypeDef",
    "AcceptInboundCrossClusterSearchConnectionResponseTypeDef",
    "AdvancedSecurityOptionsInputTypeDef",
    "AssociatePackageResponseTypeDef",
    "AutoTuneOptionsInputTypeDef",
    "CancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "CreateElasticsearchDomainResponseTypeDef",
    "CreateOutboundCrossClusterSearchConnectionResponseTypeDef",
    "CreatePackageResponseTypeDef",
    "DeleteElasticsearchDomainResponseTypeDef",
    "DeleteInboundCrossClusterSearchConnectionResponseTypeDef",
    "DeleteOutboundCrossClusterSearchConnectionResponseTypeDef",
    "DeletePackageResponseTypeDef",
    "DescribeDomainAutoTunesResponseTypeDef",
    "DescribeElasticsearchDomainConfigResponseTypeDef",
    "DescribeElasticsearchDomainResponseTypeDef",
    "DescribeElasticsearchDomainsResponseTypeDef",
    "DescribeElasticsearchInstanceTypeLimitsResponseTypeDef",
    "DescribeInboundCrossClusterSearchConnectionsResponseTypeDef",
    "DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef",
    "DescribePackagesFilterTypeDef",
    "DescribePackagesResponseTypeDef",
    "DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    "DescribeReservedElasticsearchInstancesResponseTypeDef",
    "DissociatePackageResponseTypeDef",
    "FilterTypeDef",
    "GetCompatibleElasticsearchVersionsResponseTypeDef",
    "GetPackageVersionHistoryResponseTypeDef",
    "GetUpgradeHistoryResponseTypeDef",
    "GetUpgradeStatusResponseTypeDef",
    "ListDomainNamesResponseTypeDef",
    "ListDomainsForPackageResponseTypeDef",
    "ListElasticsearchInstanceTypesResponseTypeDef",
    "ListElasticsearchVersionsResponseTypeDef",
    "ListPackagesForDomainResponseTypeDef",
    "ListTagsResponseTypeDef",
    "PackageSourceTypeDef",
    "PaginatorConfigTypeDef",
    "PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    "RejectInboundCrossClusterSearchConnectionResponseTypeDef",
    "StartElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "UpdateElasticsearchDomainConfigResponseTypeDef",
    "UpdatePackageResponseTypeDef",
    "UpgradeElasticsearchDomainResponseTypeDef",
    "VPCOptionsTypeDef",
)

AccessPoliciesStatusTypeDef = TypedDict(
    "AccessPoliciesStatusTypeDef", {"Options": str, "Status": "OptionStatusTypeDef"}
)

AdditionalLimitTypeDef = TypedDict(
    "AdditionalLimitTypeDef", {"LimitName": str, "LimitValues": List[str]}, total=False
)

AdvancedOptionsStatusTypeDef = TypedDict(
    "AdvancedOptionsStatusTypeDef", {"Options": Dict[str, str], "Status": "OptionStatusTypeDef"}
)

AdvancedSecurityOptionsStatusTypeDef = TypedDict(
    "AdvancedSecurityOptionsStatusTypeDef",
    {"Options": "AdvancedSecurityOptionsTypeDef", "Status": "OptionStatusTypeDef"},
)

AdvancedSecurityOptionsTypeDef = TypedDict(
    "AdvancedSecurityOptionsTypeDef",
    {
        "Enabled": bool,
        "InternalUserDatabaseEnabled": bool,
        "SAMLOptions": "SAMLOptionsOutputTypeDef",
    },
    total=False,
)

AutoTuneDetailsTypeDef = TypedDict(
    "AutoTuneDetailsTypeDef",
    {"ScheduledAutoTuneDetails": "ScheduledAutoTuneDetailsTypeDef"},
    total=False,
)

AutoTuneMaintenanceScheduleTypeDef = TypedDict(
    "AutoTuneMaintenanceScheduleTypeDef",
    {"StartAt": datetime, "Duration": "DurationTypeDef", "CronExpressionForRecurrence": str},
    total=False,
)

AutoTuneOptionsOutputTypeDef = TypedDict(
    "AutoTuneOptionsOutputTypeDef",
    {"State": AutoTuneState, "ErrorMessage": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

AutoTuneOptionsStatusTypeDef = TypedDict(
    "AutoTuneOptionsStatusTypeDef",
    {"Options": "AutoTuneOptionsTypeDef", "Status": "AutoTuneStatusTypeDef"},
    total=False,
)

AutoTuneOptionsTypeDef = TypedDict(
    "AutoTuneOptionsTypeDef",
    {
        "DesiredState": AutoTuneDesiredState,
        "RollbackOnDisable": RollbackOnDisable,
        "MaintenanceSchedules": List["AutoTuneMaintenanceScheduleTypeDef"],
    },
    total=False,
)

_RequiredAutoTuneStatusTypeDef = TypedDict(
    "_RequiredAutoTuneStatusTypeDef",
    {"CreationDate": datetime, "UpdateDate": datetime, "State": AutoTuneState},
)
_OptionalAutoTuneStatusTypeDef = TypedDict(
    "_OptionalAutoTuneStatusTypeDef",
    {"UpdateVersion": int, "ErrorMessage": str, "PendingDeletion": bool},
    total=False,
)


class AutoTuneStatusTypeDef(_RequiredAutoTuneStatusTypeDef, _OptionalAutoTuneStatusTypeDef):
    pass


AutoTuneTypeDef = TypedDict(
    "AutoTuneTypeDef",
    {"AutoTuneType": AutoTuneType, "AutoTuneDetails": "AutoTuneDetailsTypeDef"},
    total=False,
)

CognitoOptionsStatusTypeDef = TypedDict(
    "CognitoOptionsStatusTypeDef",
    {"Options": "CognitoOptionsTypeDef", "Status": "OptionStatusTypeDef"},
)

CognitoOptionsTypeDef = TypedDict(
    "CognitoOptionsTypeDef",
    {"Enabled": bool, "UserPoolId": str, "IdentityPoolId": str, "RoleArn": str},
    total=False,
)

CompatibleVersionsMapTypeDef = TypedDict(
    "CompatibleVersionsMapTypeDef", {"SourceVersion": str, "TargetVersions": List[str]}, total=False
)

DomainEndpointOptionsStatusTypeDef = TypedDict(
    "DomainEndpointOptionsStatusTypeDef",
    {"Options": "DomainEndpointOptionsTypeDef", "Status": "OptionStatusTypeDef"},
)

DomainEndpointOptionsTypeDef = TypedDict(
    "DomainEndpointOptionsTypeDef",
    {
        "EnforceHTTPS": bool,
        "TLSSecurityPolicy": TLSSecurityPolicy,
        "CustomEndpointEnabled": bool,
        "CustomEndpoint": str,
        "CustomEndpointCertificateArn": str,
    },
    total=False,
)

DomainInfoTypeDef = TypedDict("DomainInfoTypeDef", {"DomainName": str}, total=False)

_RequiredDomainInformationTypeDef = TypedDict(
    "_RequiredDomainInformationTypeDef", {"DomainName": str}
)
_OptionalDomainInformationTypeDef = TypedDict(
    "_OptionalDomainInformationTypeDef", {"OwnerId": str, "Region": str}, total=False
)


class DomainInformationTypeDef(
    _RequiredDomainInformationTypeDef, _OptionalDomainInformationTypeDef
):
    pass


DomainPackageDetailsTypeDef = TypedDict(
    "DomainPackageDetailsTypeDef",
    {
        "PackageID": str,
        "PackageName": str,
        "PackageType": PackageType,
        "LastUpdated": datetime,
        "DomainName": str,
        "DomainPackageStatus": DomainPackageStatus,
        "PackageVersion": str,
        "ReferencePath": str,
        "ErrorDetails": "ErrorDetailsTypeDef",
    },
    total=False,
)

DurationTypeDef = TypedDict("DurationTypeDef", {"Value": int, "Unit": TimeUnit}, total=False)

EBSOptionsStatusTypeDef = TypedDict(
    "EBSOptionsStatusTypeDef", {"Options": "EBSOptionsTypeDef", "Status": "OptionStatusTypeDef"}
)

EBSOptionsTypeDef = TypedDict(
    "EBSOptionsTypeDef",
    {"EBSEnabled": bool, "VolumeType": VolumeType, "VolumeSize": int, "Iops": int},
    total=False,
)

ElasticsearchClusterConfigStatusTypeDef = TypedDict(
    "ElasticsearchClusterConfigStatusTypeDef",
    {"Options": "ElasticsearchClusterConfigTypeDef", "Status": "OptionStatusTypeDef"},
)

ElasticsearchClusterConfigTypeDef = TypedDict(
    "ElasticsearchClusterConfigTypeDef",
    {
        "InstanceType": ESPartitionInstanceType,
        "InstanceCount": int,
        "DedicatedMasterEnabled": bool,
        "ZoneAwarenessEnabled": bool,
        "ZoneAwarenessConfig": "ZoneAwarenessConfigTypeDef",
        "DedicatedMasterType": ESPartitionInstanceType,
        "DedicatedMasterCount": int,
        "WarmEnabled": bool,
        "WarmType": ESWarmPartitionInstanceType,
        "WarmCount": int,
    },
    total=False,
)

ElasticsearchDomainConfigTypeDef = TypedDict(
    "ElasticsearchDomainConfigTypeDef",
    {
        "ElasticsearchVersion": "ElasticsearchVersionStatusTypeDef",
        "ElasticsearchClusterConfig": "ElasticsearchClusterConfigStatusTypeDef",
        "EBSOptions": "EBSOptionsStatusTypeDef",
        "AccessPolicies": "AccessPoliciesStatusTypeDef",
        "SnapshotOptions": "SnapshotOptionsStatusTypeDef",
        "VPCOptions": "VPCDerivedInfoStatusTypeDef",
        "CognitoOptions": "CognitoOptionsStatusTypeDef",
        "EncryptionAtRestOptions": "EncryptionAtRestOptionsStatusTypeDef",
        "NodeToNodeEncryptionOptions": "NodeToNodeEncryptionOptionsStatusTypeDef",
        "AdvancedOptions": "AdvancedOptionsStatusTypeDef",
        "LogPublishingOptions": "LogPublishingOptionsStatusTypeDef",
        "DomainEndpointOptions": "DomainEndpointOptionsStatusTypeDef",
        "AdvancedSecurityOptions": "AdvancedSecurityOptionsStatusTypeDef",
        "AutoTuneOptions": "AutoTuneOptionsStatusTypeDef",
    },
    total=False,
)

_RequiredElasticsearchDomainStatusTypeDef = TypedDict(
    "_RequiredElasticsearchDomainStatusTypeDef",
    {
        "DomainId": str,
        "DomainName": str,
        "ARN": str,
        "ElasticsearchClusterConfig": "ElasticsearchClusterConfigTypeDef",
    },
)
_OptionalElasticsearchDomainStatusTypeDef = TypedDict(
    "_OptionalElasticsearchDomainStatusTypeDef",
    {
        "Created": bool,
        "Deleted": bool,
        "Endpoint": str,
        "Endpoints": Dict[str, str],
        "Processing": bool,
        "UpgradeProcessing": bool,
        "ElasticsearchVersion": str,
        "EBSOptions": "EBSOptionsTypeDef",
        "AccessPolicies": str,
        "SnapshotOptions": "SnapshotOptionsTypeDef",
        "VPCOptions": "VPCDerivedInfoTypeDef",
        "CognitoOptions": "CognitoOptionsTypeDef",
        "EncryptionAtRestOptions": "EncryptionAtRestOptionsTypeDef",
        "NodeToNodeEncryptionOptions": "NodeToNodeEncryptionOptionsTypeDef",
        "AdvancedOptions": Dict[str, str],
        "LogPublishingOptions": Dict[LogType, "LogPublishingOptionTypeDef"],
        "ServiceSoftwareOptions": "ServiceSoftwareOptionsTypeDef",
        "DomainEndpointOptions": "DomainEndpointOptionsTypeDef",
        "AdvancedSecurityOptions": "AdvancedSecurityOptionsTypeDef",
        "AutoTuneOptions": "AutoTuneOptionsOutputTypeDef",
    },
    total=False,
)


class ElasticsearchDomainStatusTypeDef(
    _RequiredElasticsearchDomainStatusTypeDef, _OptionalElasticsearchDomainStatusTypeDef
):
    pass


ElasticsearchVersionStatusTypeDef = TypedDict(
    "ElasticsearchVersionStatusTypeDef", {"Options": str, "Status": "OptionStatusTypeDef"}
)

EncryptionAtRestOptionsStatusTypeDef = TypedDict(
    "EncryptionAtRestOptionsStatusTypeDef",
    {"Options": "EncryptionAtRestOptionsTypeDef", "Status": "OptionStatusTypeDef"},
)

EncryptionAtRestOptionsTypeDef = TypedDict(
    "EncryptionAtRestOptionsTypeDef", {"Enabled": bool, "KmsKeyId": str}, total=False
)

ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef", {"ErrorType": str, "ErrorMessage": str}, total=False
)

InboundCrossClusterSearchConnectionStatusTypeDef = TypedDict(
    "InboundCrossClusterSearchConnectionStatusTypeDef",
    {"StatusCode": InboundCrossClusterSearchConnectionStatusCode, "Message": str},
    total=False,
)

InboundCrossClusterSearchConnectionTypeDef = TypedDict(
    "InboundCrossClusterSearchConnectionTypeDef",
    {
        "SourceDomainInfo": "DomainInformationTypeDef",
        "DestinationDomainInfo": "DomainInformationTypeDef",
        "CrossClusterSearchConnectionId": str,
        "ConnectionStatus": "InboundCrossClusterSearchConnectionStatusTypeDef",
    },
    total=False,
)

InstanceCountLimitsTypeDef = TypedDict(
    "InstanceCountLimitsTypeDef",
    {"MinimumInstanceCount": int, "MaximumInstanceCount": int},
    total=False,
)

InstanceLimitsTypeDef = TypedDict(
    "InstanceLimitsTypeDef", {"InstanceCountLimits": "InstanceCountLimitsTypeDef"}, total=False
)

LimitsTypeDef = TypedDict(
    "LimitsTypeDef",
    {
        "StorageTypes": List["StorageTypeTypeDef"],
        "InstanceLimits": "InstanceLimitsTypeDef",
        "AdditionalLimits": List["AdditionalLimitTypeDef"],
    },
    total=False,
)

LogPublishingOptionTypeDef = TypedDict(
    "LogPublishingOptionTypeDef", {"CloudWatchLogsLogGroupArn": str, "Enabled": bool}, total=False
)

LogPublishingOptionsStatusTypeDef = TypedDict(
    "LogPublishingOptionsStatusTypeDef",
    {"Options": Dict[LogType, "LogPublishingOptionTypeDef"], "Status": "OptionStatusTypeDef"},
    total=False,
)

MasterUserOptionsTypeDef = TypedDict(
    "MasterUserOptionsTypeDef",
    {"MasterUserARN": str, "MasterUserName": str, "MasterUserPassword": str},
    total=False,
)

NodeToNodeEncryptionOptionsStatusTypeDef = TypedDict(
    "NodeToNodeEncryptionOptionsStatusTypeDef",
    {"Options": "NodeToNodeEncryptionOptionsTypeDef", "Status": "OptionStatusTypeDef"},
)

NodeToNodeEncryptionOptionsTypeDef = TypedDict(
    "NodeToNodeEncryptionOptionsTypeDef", {"Enabled": bool}, total=False
)

_RequiredOptionStatusTypeDef = TypedDict(
    "_RequiredOptionStatusTypeDef",
    {"CreationDate": datetime, "UpdateDate": datetime, "State": OptionState},
)
_OptionalOptionStatusTypeDef = TypedDict(
    "_OptionalOptionStatusTypeDef", {"UpdateVersion": int, "PendingDeletion": bool}, total=False
)


class OptionStatusTypeDef(_RequiredOptionStatusTypeDef, _OptionalOptionStatusTypeDef):
    pass


OutboundCrossClusterSearchConnectionStatusTypeDef = TypedDict(
    "OutboundCrossClusterSearchConnectionStatusTypeDef",
    {"StatusCode": OutboundCrossClusterSearchConnectionStatusCode, "Message": str},
    total=False,
)

OutboundCrossClusterSearchConnectionTypeDef = TypedDict(
    "OutboundCrossClusterSearchConnectionTypeDef",
    {
        "SourceDomainInfo": "DomainInformationTypeDef",
        "DestinationDomainInfo": "DomainInformationTypeDef",
        "CrossClusterSearchConnectionId": str,
        "ConnectionAlias": str,
        "ConnectionStatus": "OutboundCrossClusterSearchConnectionStatusTypeDef",
    },
    total=False,
)

PackageDetailsTypeDef = TypedDict(
    "PackageDetailsTypeDef",
    {
        "PackageID": str,
        "PackageName": str,
        "PackageType": PackageType,
        "PackageDescription": str,
        "PackageStatus": PackageStatus,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "AvailablePackageVersion": str,
        "ErrorDetails": "ErrorDetailsTypeDef",
    },
    total=False,
)

PackageVersionHistoryTypeDef = TypedDict(
    "PackageVersionHistoryTypeDef",
    {"PackageVersion": str, "CommitMessage": str, "CreatedAt": datetime},
    total=False,
)

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {"RecurringChargeAmount": float, "RecurringChargeFrequency": str},
    total=False,
)

ReservedElasticsearchInstanceOfferingTypeDef = TypedDict(
    "ReservedElasticsearchInstanceOfferingTypeDef",
    {
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": ESPartitionInstanceType,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "PaymentOption": ReservedElasticsearchInstancePaymentOption,
        "RecurringCharges": List["RecurringChargeTypeDef"],
    },
    total=False,
)

ReservedElasticsearchInstanceTypeDef = TypedDict(
    "ReservedElasticsearchInstanceTypeDef",
    {
        "ReservationName": str,
        "ReservedElasticsearchInstanceId": str,
        "ReservedElasticsearchInstanceOfferingId": str,
        "ElasticsearchInstanceType": ESPartitionInstanceType,
        "StartTime": datetime,
        "Duration": int,
        "FixedPrice": float,
        "UsagePrice": float,
        "CurrencyCode": str,
        "ElasticsearchInstanceCount": int,
        "State": str,
        "PaymentOption": ReservedElasticsearchInstancePaymentOption,
        "RecurringCharges": List["RecurringChargeTypeDef"],
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

SAMLIdpTypeDef = TypedDict("SAMLIdpTypeDef", {"MetadataContent": str, "EntityId": str})

SAMLOptionsInputTypeDef = TypedDict(
    "SAMLOptionsInputTypeDef",
    {
        "Enabled": bool,
        "Idp": "SAMLIdpTypeDef",
        "MasterUserName": str,
        "MasterBackendRole": str,
        "SubjectKey": str,
        "RolesKey": str,
        "SessionTimeoutMinutes": int,
    },
    total=False,
)

SAMLOptionsOutputTypeDef = TypedDict(
    "SAMLOptionsOutputTypeDef",
    {
        "Enabled": bool,
        "Idp": "SAMLIdpTypeDef",
        "SubjectKey": str,
        "RolesKey": str,
        "SessionTimeoutMinutes": int,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ScheduledAutoTuneDetailsTypeDef = TypedDict(
    "ScheduledAutoTuneDetailsTypeDef",
    {
        "Date": datetime,
        "ActionType": ScheduledAutoTuneActionType,
        "Action": str,
        "Severity": ScheduledAutoTuneSeverityType,
    },
    total=False,
)

ServiceSoftwareOptionsTypeDef = TypedDict(
    "ServiceSoftwareOptionsTypeDef",
    {
        "CurrentVersion": str,
        "NewVersion": str,
        "UpdateAvailable": bool,
        "Cancellable": bool,
        "UpdateStatus": DeploymentStatus,
        "Description": str,
        "AutomatedUpdateDate": datetime,
        "OptionalDeployment": bool,
    },
    total=False,
)

SnapshotOptionsStatusTypeDef = TypedDict(
    "SnapshotOptionsStatusTypeDef",
    {"Options": "SnapshotOptionsTypeDef", "Status": "OptionStatusTypeDef"},
)

SnapshotOptionsTypeDef = TypedDict(
    "SnapshotOptionsTypeDef", {"AutomatedSnapshotStartHour": int}, total=False
)

StorageTypeLimitTypeDef = TypedDict(
    "StorageTypeLimitTypeDef", {"LimitName": str, "LimitValues": List[str]}, total=False
)

StorageTypeTypeDef = TypedDict(
    "StorageTypeTypeDef",
    {
        "StorageTypeName": str,
        "StorageSubTypeName": str,
        "StorageTypeLimits": List["StorageTypeLimitTypeDef"],
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

UpgradeHistoryTypeDef = TypedDict(
    "UpgradeHistoryTypeDef",
    {
        "UpgradeName": str,
        "StartTimestamp": datetime,
        "UpgradeStatus": UpgradeStatus,
        "StepsList": List["UpgradeStepItemTypeDef"],
    },
    total=False,
)

UpgradeStepItemTypeDef = TypedDict(
    "UpgradeStepItemTypeDef",
    {
        "UpgradeStep": UpgradeStep,
        "UpgradeStepStatus": UpgradeStatus,
        "Issues": List[str],
        "ProgressPercent": float,
    },
    total=False,
)

VPCDerivedInfoStatusTypeDef = TypedDict(
    "VPCDerivedInfoStatusTypeDef",
    {"Options": "VPCDerivedInfoTypeDef", "Status": "OptionStatusTypeDef"},
)

VPCDerivedInfoTypeDef = TypedDict(
    "VPCDerivedInfoTypeDef",
    {
        "VPCId": str,
        "SubnetIds": List[str],
        "AvailabilityZones": List[str],
        "SecurityGroupIds": List[str],
    },
    total=False,
)

ZoneAwarenessConfigTypeDef = TypedDict(
    "ZoneAwarenessConfigTypeDef", {"AvailabilityZoneCount": int}, total=False
)

AcceptInboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "AcceptInboundCrossClusterSearchConnectionResponseTypeDef",
    {"CrossClusterSearchConnection": "InboundCrossClusterSearchConnectionTypeDef"},
    total=False,
)

AdvancedSecurityOptionsInputTypeDef = TypedDict(
    "AdvancedSecurityOptionsInputTypeDef",
    {
        "Enabled": bool,
        "InternalUserDatabaseEnabled": bool,
        "MasterUserOptions": "MasterUserOptionsTypeDef",
        "SAMLOptions": "SAMLOptionsInputTypeDef",
    },
    total=False,
)

AssociatePackageResponseTypeDef = TypedDict(
    "AssociatePackageResponseTypeDef",
    {"DomainPackageDetails": "DomainPackageDetailsTypeDef"},
    total=False,
)

AutoTuneOptionsInputTypeDef = TypedDict(
    "AutoTuneOptionsInputTypeDef",
    {
        "DesiredState": AutoTuneDesiredState,
        "MaintenanceSchedules": List["AutoTuneMaintenanceScheduleTypeDef"],
    },
    total=False,
)

CancelElasticsearchServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "CancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
    {"ServiceSoftwareOptions": "ServiceSoftwareOptionsTypeDef"},
    total=False,
)

CreateElasticsearchDomainResponseTypeDef = TypedDict(
    "CreateElasticsearchDomainResponseTypeDef",
    {"DomainStatus": "ElasticsearchDomainStatusTypeDef"},
    total=False,
)

CreateOutboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "CreateOutboundCrossClusterSearchConnectionResponseTypeDef",
    {
        "SourceDomainInfo": "DomainInformationTypeDef",
        "DestinationDomainInfo": "DomainInformationTypeDef",
        "ConnectionAlias": str,
        "ConnectionStatus": "OutboundCrossClusterSearchConnectionStatusTypeDef",
        "CrossClusterSearchConnectionId": str,
    },
    total=False,
)

CreatePackageResponseTypeDef = TypedDict(
    "CreatePackageResponseTypeDef", {"PackageDetails": "PackageDetailsTypeDef"}, total=False
)

DeleteElasticsearchDomainResponseTypeDef = TypedDict(
    "DeleteElasticsearchDomainResponseTypeDef",
    {"DomainStatus": "ElasticsearchDomainStatusTypeDef"},
    total=False,
)

DeleteInboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "DeleteInboundCrossClusterSearchConnectionResponseTypeDef",
    {"CrossClusterSearchConnection": "InboundCrossClusterSearchConnectionTypeDef"},
    total=False,
)

DeleteOutboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "DeleteOutboundCrossClusterSearchConnectionResponseTypeDef",
    {"CrossClusterSearchConnection": "OutboundCrossClusterSearchConnectionTypeDef"},
    total=False,
)

DeletePackageResponseTypeDef = TypedDict(
    "DeletePackageResponseTypeDef", {"PackageDetails": "PackageDetailsTypeDef"}, total=False
)

DescribeDomainAutoTunesResponseTypeDef = TypedDict(
    "DescribeDomainAutoTunesResponseTypeDef",
    {"AutoTunes": List["AutoTuneTypeDef"], "NextToken": str},
    total=False,
)

DescribeElasticsearchDomainConfigResponseTypeDef = TypedDict(
    "DescribeElasticsearchDomainConfigResponseTypeDef",
    {"DomainConfig": "ElasticsearchDomainConfigTypeDef"},
)

DescribeElasticsearchDomainResponseTypeDef = TypedDict(
    "DescribeElasticsearchDomainResponseTypeDef",
    {"DomainStatus": "ElasticsearchDomainStatusTypeDef"},
)

DescribeElasticsearchDomainsResponseTypeDef = TypedDict(
    "DescribeElasticsearchDomainsResponseTypeDef",
    {"DomainStatusList": List["ElasticsearchDomainStatusTypeDef"]},
)

DescribeElasticsearchInstanceTypeLimitsResponseTypeDef = TypedDict(
    "DescribeElasticsearchInstanceTypeLimitsResponseTypeDef",
    {"LimitsByRole": Dict[str, "LimitsTypeDef"]},
    total=False,
)

DescribeInboundCrossClusterSearchConnectionsResponseTypeDef = TypedDict(
    "DescribeInboundCrossClusterSearchConnectionsResponseTypeDef",
    {
        "CrossClusterSearchConnections": List["InboundCrossClusterSearchConnectionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef = TypedDict(
    "DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef",
    {
        "CrossClusterSearchConnections": List["OutboundCrossClusterSearchConnectionTypeDef"],
        "NextToken": str,
    },
    total=False,
)

DescribePackagesFilterTypeDef = TypedDict(
    "DescribePackagesFilterTypeDef",
    {"Name": DescribePackagesFilterName, "Value": List[str]},
    total=False,
)

DescribePackagesResponseTypeDef = TypedDict(
    "DescribePackagesResponseTypeDef",
    {"PackageDetailsList": List["PackageDetailsTypeDef"], "NextToken": str},
    total=False,
)

DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstanceOfferings": List[
            "ReservedElasticsearchInstanceOfferingTypeDef"
        ],
    },
    total=False,
)

DescribeReservedElasticsearchInstancesResponseTypeDef = TypedDict(
    "DescribeReservedElasticsearchInstancesResponseTypeDef",
    {
        "NextToken": str,
        "ReservedElasticsearchInstances": List["ReservedElasticsearchInstanceTypeDef"],
    },
    total=False,
)

DissociatePackageResponseTypeDef = TypedDict(
    "DissociatePackageResponseTypeDef",
    {"DomainPackageDetails": "DomainPackageDetailsTypeDef"},
    total=False,
)

FilterTypeDef = TypedDict("FilterTypeDef", {"Name": str, "Values": List[str]}, total=False)

GetCompatibleElasticsearchVersionsResponseTypeDef = TypedDict(
    "GetCompatibleElasticsearchVersionsResponseTypeDef",
    {"CompatibleElasticsearchVersions": List["CompatibleVersionsMapTypeDef"]},
    total=False,
)

GetPackageVersionHistoryResponseTypeDef = TypedDict(
    "GetPackageVersionHistoryResponseTypeDef",
    {
        "PackageID": str,
        "PackageVersionHistoryList": List["PackageVersionHistoryTypeDef"],
        "NextToken": str,
    },
    total=False,
)

GetUpgradeHistoryResponseTypeDef = TypedDict(
    "GetUpgradeHistoryResponseTypeDef",
    {"UpgradeHistories": List["UpgradeHistoryTypeDef"], "NextToken": str},
    total=False,
)

GetUpgradeStatusResponseTypeDef = TypedDict(
    "GetUpgradeStatusResponseTypeDef",
    {"UpgradeStep": UpgradeStep, "StepStatus": UpgradeStatus, "UpgradeName": str},
    total=False,
)

ListDomainNamesResponseTypeDef = TypedDict(
    "ListDomainNamesResponseTypeDef", {"DomainNames": List["DomainInfoTypeDef"]}, total=False
)

ListDomainsForPackageResponseTypeDef = TypedDict(
    "ListDomainsForPackageResponseTypeDef",
    {"DomainPackageDetailsList": List["DomainPackageDetailsTypeDef"], "NextToken": str},
    total=False,
)

ListElasticsearchInstanceTypesResponseTypeDef = TypedDict(
    "ListElasticsearchInstanceTypesResponseTypeDef",
    {"ElasticsearchInstanceTypes": List[ESPartitionInstanceType], "NextToken": str},
    total=False,
)

ListElasticsearchVersionsResponseTypeDef = TypedDict(
    "ListElasticsearchVersionsResponseTypeDef",
    {"ElasticsearchVersions": List[str], "NextToken": str},
    total=False,
)

ListPackagesForDomainResponseTypeDef = TypedDict(
    "ListPackagesForDomainResponseTypeDef",
    {"DomainPackageDetailsList": List["DomainPackageDetailsTypeDef"], "NextToken": str},
    total=False,
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef", {"TagList": List["TagTypeDef"]}, total=False
)

PackageSourceTypeDef = TypedDict(
    "PackageSourceTypeDef", {"S3BucketName": str, "S3Key": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef = TypedDict(
    "PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    {"ReservedElasticsearchInstanceId": str, "ReservationName": str},
    total=False,
)

RejectInboundCrossClusterSearchConnectionResponseTypeDef = TypedDict(
    "RejectInboundCrossClusterSearchConnectionResponseTypeDef",
    {"CrossClusterSearchConnection": "InboundCrossClusterSearchConnectionTypeDef"},
    total=False,
)

StartElasticsearchServiceSoftwareUpdateResponseTypeDef = TypedDict(
    "StartElasticsearchServiceSoftwareUpdateResponseTypeDef",
    {"ServiceSoftwareOptions": "ServiceSoftwareOptionsTypeDef"},
    total=False,
)

UpdateElasticsearchDomainConfigResponseTypeDef = TypedDict(
    "UpdateElasticsearchDomainConfigResponseTypeDef",
    {"DomainConfig": "ElasticsearchDomainConfigTypeDef"},
)

UpdatePackageResponseTypeDef = TypedDict(
    "UpdatePackageResponseTypeDef", {"PackageDetails": "PackageDetailsTypeDef"}, total=False
)

UpgradeElasticsearchDomainResponseTypeDef = TypedDict(
    "UpgradeElasticsearchDomainResponseTypeDef",
    {"DomainName": str, "TargetVersion": str, "PerformCheckOnly": bool},
    total=False,
)

VPCOptionsTypeDef = TypedDict(
    "VPCOptionsTypeDef", {"SubnetIds": List[str], "SecurityGroupIds": List[str]}, total=False
)
