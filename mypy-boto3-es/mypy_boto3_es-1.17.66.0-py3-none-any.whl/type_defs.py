"""
Type annotations for es service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_es/type_defs.html)

Usage::

    ```python
    from mypy_boto3_es.type_defs import AcceptInboundCrossClusterSearchConnectionResponseTypeDef

    data: AcceptInboundCrossClusterSearchConnectionResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_es.literals import (
    AutoTuneDesiredState,
    AutoTuneState,
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
    ReservedElasticsearchInstancePaymentOption,
    RollbackOnDisable,
    ScheduledAutoTuneActionType,
    ScheduledAutoTuneSeverityType,
    TLSSecurityPolicy,
    UpgradeStatus,
    UpgradeStep,
    VolumeType,
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
    "AcceptInboundCrossClusterSearchConnectionResponseTypeDef",
    "AccessPoliciesStatusTypeDef",
    "AdditionalLimitTypeDef",
    "AdvancedOptionsStatusTypeDef",
    "AdvancedSecurityOptionsInputTypeDef",
    "AdvancedSecurityOptionsStatusTypeDef",
    "AdvancedSecurityOptionsTypeDef",
    "AssociatePackageResponseTypeDef",
    "AutoTuneDetailsTypeDef",
    "AutoTuneMaintenanceScheduleTypeDef",
    "AutoTuneOptionsInputTypeDef",
    "AutoTuneOptionsOutputTypeDef",
    "AutoTuneOptionsStatusTypeDef",
    "AutoTuneOptionsTypeDef",
    "AutoTuneStatusTypeDef",
    "AutoTuneTypeDef",
    "CancelElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "CognitoOptionsStatusTypeDef",
    "CognitoOptionsTypeDef",
    "CompatibleVersionsMapTypeDef",
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
    "FilterTypeDef",
    "GetCompatibleElasticsearchVersionsResponseTypeDef",
    "GetPackageVersionHistoryResponseTypeDef",
    "GetUpgradeHistoryResponseTypeDef",
    "GetUpgradeStatusResponseTypeDef",
    "InboundCrossClusterSearchConnectionStatusTypeDef",
    "InboundCrossClusterSearchConnectionTypeDef",
    "InstanceCountLimitsTypeDef",
    "InstanceLimitsTypeDef",
    "LimitsTypeDef",
    "ListDomainNamesResponseTypeDef",
    "ListDomainsForPackageResponseTypeDef",
    "ListElasticsearchInstanceTypesResponseTypeDef",
    "ListElasticsearchVersionsResponseTypeDef",
    "ListPackagesForDomainResponseTypeDef",
    "ListTagsResponseTypeDef",
    "LogPublishingOptionTypeDef",
    "LogPublishingOptionsStatusTypeDef",
    "MasterUserOptionsTypeDef",
    "NodeToNodeEncryptionOptionsStatusTypeDef",
    "NodeToNodeEncryptionOptionsTypeDef",
    "OptionStatusTypeDef",
    "OutboundCrossClusterSearchConnectionStatusTypeDef",
    "OutboundCrossClusterSearchConnectionTypeDef",
    "PackageDetailsTypeDef",
    "PackageSourceTypeDef",
    "PackageVersionHistoryTypeDef",
    "PaginatorConfigTypeDef",
    "PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef",
    "RecurringChargeTypeDef",
    "RejectInboundCrossClusterSearchConnectionResponseTypeDef",
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
    "StartElasticsearchServiceSoftwareUpdateResponseTypeDef",
    "StorageTypeLimitTypeDef",
    "StorageTypeTypeDef",
    "TagTypeDef",
    "UpdateElasticsearchDomainConfigResponseTypeDef",
    "UpdatePackageResponseTypeDef",
    "UpgradeElasticsearchDomainResponseTypeDef",
    "UpgradeHistoryTypeDef",
    "UpgradeStepItemTypeDef",
    "VPCDerivedInfoStatusTypeDef",
    "VPCDerivedInfoTypeDef",
    "VPCOptionsTypeDef",
    "ZoneAwarenessConfigTypeDef",
)


class AcceptInboundCrossClusterSearchConnectionResponseTypeDef(TypedDict, total=False):
    CrossClusterSearchConnection: "InboundCrossClusterSearchConnectionTypeDef"


class AccessPoliciesStatusTypeDef(TypedDict):
    Options: str
    Status: "OptionStatusTypeDef"


class AdditionalLimitTypeDef(TypedDict, total=False):
    LimitName: str
    LimitValues: List[str]


class AdvancedOptionsStatusTypeDef(TypedDict):
    Options: Dict[str, str]
    Status: "OptionStatusTypeDef"


class AdvancedSecurityOptionsInputTypeDef(TypedDict, total=False):
    Enabled: bool
    InternalUserDatabaseEnabled: bool
    MasterUserOptions: "MasterUserOptionsTypeDef"
    SAMLOptions: "SAMLOptionsInputTypeDef"


class AdvancedSecurityOptionsStatusTypeDef(TypedDict):
    Options: "AdvancedSecurityOptionsTypeDef"
    Status: "OptionStatusTypeDef"


class AdvancedSecurityOptionsTypeDef(TypedDict, total=False):
    Enabled: bool
    InternalUserDatabaseEnabled: bool
    SAMLOptions: "SAMLOptionsOutputTypeDef"


class AssociatePackageResponseTypeDef(TypedDict, total=False):
    DomainPackageDetails: "DomainPackageDetailsTypeDef"


class AutoTuneDetailsTypeDef(TypedDict, total=False):
    ScheduledAutoTuneDetails: "ScheduledAutoTuneDetailsTypeDef"


class AutoTuneMaintenanceScheduleTypeDef(TypedDict, total=False):
    StartAt: datetime
    Duration: "DurationTypeDef"
    CronExpressionForRecurrence: str


class AutoTuneOptionsInputTypeDef(TypedDict, total=False):
    DesiredState: AutoTuneDesiredState
    MaintenanceSchedules: List["AutoTuneMaintenanceScheduleTypeDef"]


class AutoTuneOptionsOutputTypeDef(TypedDict):
    State: AutoTuneState
    ErrorMessage: str
    ResponseMetadata: "ResponseMetadata"


class AutoTuneOptionsStatusTypeDef(TypedDict, total=False):
    Options: "AutoTuneOptionsTypeDef"
    Status: "AutoTuneStatusTypeDef"


class AutoTuneOptionsTypeDef(TypedDict, total=False):
    DesiredState: AutoTuneDesiredState
    RollbackOnDisable: RollbackOnDisable
    MaintenanceSchedules: List["AutoTuneMaintenanceScheduleTypeDef"]


class _RequiredAutoTuneStatusTypeDef(TypedDict):
    CreationDate: datetime
    UpdateDate: datetime
    State: AutoTuneState


class AutoTuneStatusTypeDef(_RequiredAutoTuneStatusTypeDef, total=False):
    UpdateVersion: int
    ErrorMessage: str
    PendingDeletion: bool


class AutoTuneTypeDef(TypedDict, total=False):
    AutoTuneType: Literal["SCHEDULED_ACTION"]
    AutoTuneDetails: "AutoTuneDetailsTypeDef"


class CancelElasticsearchServiceSoftwareUpdateResponseTypeDef(TypedDict, total=False):
    ServiceSoftwareOptions: "ServiceSoftwareOptionsTypeDef"


class CognitoOptionsStatusTypeDef(TypedDict):
    Options: "CognitoOptionsTypeDef"
    Status: "OptionStatusTypeDef"


class CognitoOptionsTypeDef(TypedDict, total=False):
    Enabled: bool
    UserPoolId: str
    IdentityPoolId: str
    RoleArn: str


class CompatibleVersionsMapTypeDef(TypedDict, total=False):
    SourceVersion: str
    TargetVersions: List[str]


class CreateElasticsearchDomainResponseTypeDef(TypedDict, total=False):
    DomainStatus: "ElasticsearchDomainStatusTypeDef"


class CreateOutboundCrossClusterSearchConnectionResponseTypeDef(TypedDict, total=False):
    SourceDomainInfo: "DomainInformationTypeDef"
    DestinationDomainInfo: "DomainInformationTypeDef"
    ConnectionAlias: str
    ConnectionStatus: "OutboundCrossClusterSearchConnectionStatusTypeDef"
    CrossClusterSearchConnectionId: str


class CreatePackageResponseTypeDef(TypedDict, total=False):
    PackageDetails: "PackageDetailsTypeDef"


class DeleteElasticsearchDomainResponseTypeDef(TypedDict, total=False):
    DomainStatus: "ElasticsearchDomainStatusTypeDef"


class DeleteInboundCrossClusterSearchConnectionResponseTypeDef(TypedDict, total=False):
    CrossClusterSearchConnection: "InboundCrossClusterSearchConnectionTypeDef"


class DeleteOutboundCrossClusterSearchConnectionResponseTypeDef(TypedDict, total=False):
    CrossClusterSearchConnection: "OutboundCrossClusterSearchConnectionTypeDef"


class DeletePackageResponseTypeDef(TypedDict, total=False):
    PackageDetails: "PackageDetailsTypeDef"


class DescribeDomainAutoTunesResponseTypeDef(TypedDict, total=False):
    AutoTunes: List["AutoTuneTypeDef"]
    NextToken: str


class DescribeElasticsearchDomainConfigResponseTypeDef(TypedDict):
    DomainConfig: "ElasticsearchDomainConfigTypeDef"


class DescribeElasticsearchDomainResponseTypeDef(TypedDict):
    DomainStatus: "ElasticsearchDomainStatusTypeDef"


class DescribeElasticsearchDomainsResponseTypeDef(TypedDict):
    DomainStatusList: List["ElasticsearchDomainStatusTypeDef"]


class DescribeElasticsearchInstanceTypeLimitsResponseTypeDef(TypedDict, total=False):
    LimitsByRole: Dict[str, "LimitsTypeDef"]


class DescribeInboundCrossClusterSearchConnectionsResponseTypeDef(TypedDict, total=False):
    CrossClusterSearchConnections: List["InboundCrossClusterSearchConnectionTypeDef"]
    NextToken: str


class DescribeOutboundCrossClusterSearchConnectionsResponseTypeDef(TypedDict, total=False):
    CrossClusterSearchConnections: List["OutboundCrossClusterSearchConnectionTypeDef"]
    NextToken: str


class DescribePackagesFilterTypeDef(TypedDict, total=False):
    Name: DescribePackagesFilterName
    Value: List[str]


class DescribePackagesResponseTypeDef(TypedDict, total=False):
    PackageDetailsList: List["PackageDetailsTypeDef"]
    NextToken: str


class DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    ReservedElasticsearchInstanceOfferings: List["ReservedElasticsearchInstanceOfferingTypeDef"]


class DescribeReservedElasticsearchInstancesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    ReservedElasticsearchInstances: List["ReservedElasticsearchInstanceTypeDef"]


class DissociatePackageResponseTypeDef(TypedDict, total=False):
    DomainPackageDetails: "DomainPackageDetailsTypeDef"


class DomainEndpointOptionsStatusTypeDef(TypedDict):
    Options: "DomainEndpointOptionsTypeDef"
    Status: "OptionStatusTypeDef"


class DomainEndpointOptionsTypeDef(TypedDict, total=False):
    EnforceHTTPS: bool
    TLSSecurityPolicy: TLSSecurityPolicy
    CustomEndpointEnabled: bool
    CustomEndpoint: str
    CustomEndpointCertificateArn: str


class DomainInfoTypeDef(TypedDict, total=False):
    DomainName: str


class _RequiredDomainInformationTypeDef(TypedDict):
    DomainName: str


class DomainInformationTypeDef(_RequiredDomainInformationTypeDef, total=False):
    OwnerId: str
    Region: str


class DomainPackageDetailsTypeDef(TypedDict, total=False):
    PackageID: str
    PackageName: str
    PackageType: Literal["TXT-DICTIONARY"]
    LastUpdated: datetime
    DomainName: str
    DomainPackageStatus: DomainPackageStatus
    PackageVersion: str
    ReferencePath: str
    ErrorDetails: "ErrorDetailsTypeDef"


class DurationTypeDef(TypedDict, total=False):
    Value: int
    Unit: Literal["HOURS"]


class EBSOptionsStatusTypeDef(TypedDict):
    Options: "EBSOptionsTypeDef"
    Status: "OptionStatusTypeDef"


class EBSOptionsTypeDef(TypedDict, total=False):
    EBSEnabled: bool
    VolumeType: VolumeType
    VolumeSize: int
    Iops: int


class ElasticsearchClusterConfigStatusTypeDef(TypedDict):
    Options: "ElasticsearchClusterConfigTypeDef"
    Status: "OptionStatusTypeDef"


class ElasticsearchClusterConfigTypeDef(TypedDict, total=False):
    InstanceType: ESPartitionInstanceType
    InstanceCount: int
    DedicatedMasterEnabled: bool
    ZoneAwarenessEnabled: bool
    ZoneAwarenessConfig: "ZoneAwarenessConfigTypeDef"
    DedicatedMasterType: ESPartitionInstanceType
    DedicatedMasterCount: int
    WarmEnabled: bool
    WarmType: ESWarmPartitionInstanceType
    WarmCount: int


class ElasticsearchDomainConfigTypeDef(TypedDict, total=False):
    ElasticsearchVersion: "ElasticsearchVersionStatusTypeDef"
    ElasticsearchClusterConfig: "ElasticsearchClusterConfigStatusTypeDef"
    EBSOptions: "EBSOptionsStatusTypeDef"
    AccessPolicies: "AccessPoliciesStatusTypeDef"
    SnapshotOptions: "SnapshotOptionsStatusTypeDef"
    VPCOptions: "VPCDerivedInfoStatusTypeDef"
    CognitoOptions: "CognitoOptionsStatusTypeDef"
    EncryptionAtRestOptions: "EncryptionAtRestOptionsStatusTypeDef"
    NodeToNodeEncryptionOptions: "NodeToNodeEncryptionOptionsStatusTypeDef"
    AdvancedOptions: "AdvancedOptionsStatusTypeDef"
    LogPublishingOptions: "LogPublishingOptionsStatusTypeDef"
    DomainEndpointOptions: "DomainEndpointOptionsStatusTypeDef"
    AdvancedSecurityOptions: "AdvancedSecurityOptionsStatusTypeDef"
    AutoTuneOptions: "AutoTuneOptionsStatusTypeDef"


class _RequiredElasticsearchDomainStatusTypeDef(TypedDict):
    DomainId: str
    DomainName: str
    ARN: str
    ElasticsearchClusterConfig: "ElasticsearchClusterConfigTypeDef"


class ElasticsearchDomainStatusTypeDef(_RequiredElasticsearchDomainStatusTypeDef, total=False):
    Created: bool
    Deleted: bool
    Endpoint: str
    Endpoints: Dict[str, str]
    Processing: bool
    UpgradeProcessing: bool
    ElasticsearchVersion: str
    EBSOptions: "EBSOptionsTypeDef"
    AccessPolicies: str
    SnapshotOptions: "SnapshotOptionsTypeDef"
    VPCOptions: "VPCDerivedInfoTypeDef"
    CognitoOptions: "CognitoOptionsTypeDef"
    EncryptionAtRestOptions: "EncryptionAtRestOptionsTypeDef"
    NodeToNodeEncryptionOptions: "NodeToNodeEncryptionOptionsTypeDef"
    AdvancedOptions: Dict[str, str]
    LogPublishingOptions: Dict[LogType, "LogPublishingOptionTypeDef"]
    ServiceSoftwareOptions: "ServiceSoftwareOptionsTypeDef"
    DomainEndpointOptions: "DomainEndpointOptionsTypeDef"
    AdvancedSecurityOptions: "AdvancedSecurityOptionsTypeDef"
    AutoTuneOptions: "AutoTuneOptionsOutputTypeDef"


class ElasticsearchVersionStatusTypeDef(TypedDict):
    Options: str
    Status: "OptionStatusTypeDef"


class EncryptionAtRestOptionsStatusTypeDef(TypedDict):
    Options: "EncryptionAtRestOptionsTypeDef"
    Status: "OptionStatusTypeDef"


class EncryptionAtRestOptionsTypeDef(TypedDict, total=False):
    Enabled: bool
    KmsKeyId: str


class ErrorDetailsTypeDef(TypedDict, total=False):
    ErrorType: str
    ErrorMessage: str


class FilterTypeDef(TypedDict, total=False):
    Name: str
    Values: List[str]


class GetCompatibleElasticsearchVersionsResponseTypeDef(TypedDict, total=False):
    CompatibleElasticsearchVersions: List["CompatibleVersionsMapTypeDef"]


class GetPackageVersionHistoryResponseTypeDef(TypedDict, total=False):
    PackageID: str
    PackageVersionHistoryList: List["PackageVersionHistoryTypeDef"]
    NextToken: str


class GetUpgradeHistoryResponseTypeDef(TypedDict, total=False):
    UpgradeHistories: List["UpgradeHistoryTypeDef"]
    NextToken: str


class GetUpgradeStatusResponseTypeDef(TypedDict, total=False):
    UpgradeStep: UpgradeStep
    StepStatus: UpgradeStatus
    UpgradeName: str


class InboundCrossClusterSearchConnectionStatusTypeDef(TypedDict, total=False):
    StatusCode: InboundCrossClusterSearchConnectionStatusCode
    Message: str


class InboundCrossClusterSearchConnectionTypeDef(TypedDict, total=False):
    SourceDomainInfo: "DomainInformationTypeDef"
    DestinationDomainInfo: "DomainInformationTypeDef"
    CrossClusterSearchConnectionId: str
    ConnectionStatus: "InboundCrossClusterSearchConnectionStatusTypeDef"


class InstanceCountLimitsTypeDef(TypedDict, total=False):
    MinimumInstanceCount: int
    MaximumInstanceCount: int


class InstanceLimitsTypeDef(TypedDict, total=False):
    InstanceCountLimits: "InstanceCountLimitsTypeDef"


class LimitsTypeDef(TypedDict, total=False):
    StorageTypes: List["StorageTypeTypeDef"]
    InstanceLimits: "InstanceLimitsTypeDef"
    AdditionalLimits: List["AdditionalLimitTypeDef"]


class ListDomainNamesResponseTypeDef(TypedDict, total=False):
    DomainNames: List["DomainInfoTypeDef"]


class ListDomainsForPackageResponseTypeDef(TypedDict, total=False):
    DomainPackageDetailsList: List["DomainPackageDetailsTypeDef"]
    NextToken: str


class ListElasticsearchInstanceTypesResponseTypeDef(TypedDict, total=False):
    ElasticsearchInstanceTypes: List[ESPartitionInstanceType]
    NextToken: str


class ListElasticsearchVersionsResponseTypeDef(TypedDict, total=False):
    ElasticsearchVersions: List[str]
    NextToken: str


class ListPackagesForDomainResponseTypeDef(TypedDict, total=False):
    DomainPackageDetailsList: List["DomainPackageDetailsTypeDef"]
    NextToken: str


class ListTagsResponseTypeDef(TypedDict, total=False):
    TagList: List["TagTypeDef"]


class LogPublishingOptionTypeDef(TypedDict, total=False):
    CloudWatchLogsLogGroupArn: str
    Enabled: bool


class LogPublishingOptionsStatusTypeDef(TypedDict, total=False):
    Options: Dict[LogType, "LogPublishingOptionTypeDef"]
    Status: "OptionStatusTypeDef"


class MasterUserOptionsTypeDef(TypedDict, total=False):
    MasterUserARN: str
    MasterUserName: str
    MasterUserPassword: str


class NodeToNodeEncryptionOptionsStatusTypeDef(TypedDict):
    Options: "NodeToNodeEncryptionOptionsTypeDef"
    Status: "OptionStatusTypeDef"


class NodeToNodeEncryptionOptionsTypeDef(TypedDict, total=False):
    Enabled: bool


class _RequiredOptionStatusTypeDef(TypedDict):
    CreationDate: datetime
    UpdateDate: datetime
    State: OptionState


class OptionStatusTypeDef(_RequiredOptionStatusTypeDef, total=False):
    UpdateVersion: int
    PendingDeletion: bool


class OutboundCrossClusterSearchConnectionStatusTypeDef(TypedDict, total=False):
    StatusCode: OutboundCrossClusterSearchConnectionStatusCode
    Message: str


class OutboundCrossClusterSearchConnectionTypeDef(TypedDict, total=False):
    SourceDomainInfo: "DomainInformationTypeDef"
    DestinationDomainInfo: "DomainInformationTypeDef"
    CrossClusterSearchConnectionId: str
    ConnectionAlias: str
    ConnectionStatus: "OutboundCrossClusterSearchConnectionStatusTypeDef"


class PackageDetailsTypeDef(TypedDict, total=False):
    PackageID: str
    PackageName: str
    PackageType: Literal["TXT-DICTIONARY"]
    PackageDescription: str
    PackageStatus: PackageStatus
    CreatedAt: datetime
    LastUpdatedAt: datetime
    AvailablePackageVersion: str
    ErrorDetails: "ErrorDetailsTypeDef"


class PackageSourceTypeDef(TypedDict, total=False):
    S3BucketName: str
    S3Key: str


class PackageVersionHistoryTypeDef(TypedDict, total=False):
    PackageVersion: str
    CommitMessage: str
    CreatedAt: datetime


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PurchaseReservedElasticsearchInstanceOfferingResponseTypeDef(TypedDict, total=False):
    ReservedElasticsearchInstanceId: str
    ReservationName: str


class RecurringChargeTypeDef(TypedDict, total=False):
    RecurringChargeAmount: float
    RecurringChargeFrequency: str


class RejectInboundCrossClusterSearchConnectionResponseTypeDef(TypedDict, total=False):
    CrossClusterSearchConnection: "InboundCrossClusterSearchConnectionTypeDef"


class ReservedElasticsearchInstanceOfferingTypeDef(TypedDict, total=False):
    ReservedElasticsearchInstanceOfferingId: str
    ElasticsearchInstanceType: ESPartitionInstanceType
    Duration: int
    FixedPrice: float
    UsagePrice: float
    CurrencyCode: str
    PaymentOption: ReservedElasticsearchInstancePaymentOption
    RecurringCharges: List["RecurringChargeTypeDef"]


class ReservedElasticsearchInstanceTypeDef(TypedDict, total=False):
    ReservationName: str
    ReservedElasticsearchInstanceId: str
    ReservedElasticsearchInstanceOfferingId: str
    ElasticsearchInstanceType: ESPartitionInstanceType
    StartTime: datetime
    Duration: int
    FixedPrice: float
    UsagePrice: float
    CurrencyCode: str
    ElasticsearchInstanceCount: int
    State: str
    PaymentOption: ReservedElasticsearchInstancePaymentOption
    RecurringCharges: List["RecurringChargeTypeDef"]


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class SAMLIdpTypeDef(TypedDict):
    MetadataContent: str
    EntityId: str


class SAMLOptionsInputTypeDef(TypedDict, total=False):
    Enabled: bool
    Idp: "SAMLIdpTypeDef"
    MasterUserName: str
    MasterBackendRole: str
    SubjectKey: str
    RolesKey: str
    SessionTimeoutMinutes: int


class SAMLOptionsOutputTypeDef(TypedDict):
    Enabled: bool
    Idp: "SAMLIdpTypeDef"
    SubjectKey: str
    RolesKey: str
    SessionTimeoutMinutes: int
    ResponseMetadata: "ResponseMetadata"


class ScheduledAutoTuneDetailsTypeDef(TypedDict, total=False):
    Date: datetime
    ActionType: ScheduledAutoTuneActionType
    Action: str
    Severity: ScheduledAutoTuneSeverityType


class ServiceSoftwareOptionsTypeDef(TypedDict, total=False):
    CurrentVersion: str
    NewVersion: str
    UpdateAvailable: bool
    Cancellable: bool
    UpdateStatus: DeploymentStatus
    Description: str
    AutomatedUpdateDate: datetime
    OptionalDeployment: bool


class SnapshotOptionsStatusTypeDef(TypedDict):
    Options: "SnapshotOptionsTypeDef"
    Status: "OptionStatusTypeDef"


class SnapshotOptionsTypeDef(TypedDict, total=False):
    AutomatedSnapshotStartHour: int


class StartElasticsearchServiceSoftwareUpdateResponseTypeDef(TypedDict, total=False):
    ServiceSoftwareOptions: "ServiceSoftwareOptionsTypeDef"


class StorageTypeLimitTypeDef(TypedDict, total=False):
    LimitName: str
    LimitValues: List[str]


class StorageTypeTypeDef(TypedDict, total=False):
    StorageTypeName: str
    StorageSubTypeName: str
    StorageTypeLimits: List["StorageTypeLimitTypeDef"]


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class UpdateElasticsearchDomainConfigResponseTypeDef(TypedDict):
    DomainConfig: "ElasticsearchDomainConfigTypeDef"


class UpdatePackageResponseTypeDef(TypedDict, total=False):
    PackageDetails: "PackageDetailsTypeDef"


class UpgradeElasticsearchDomainResponseTypeDef(TypedDict, total=False):
    DomainName: str
    TargetVersion: str
    PerformCheckOnly: bool


class UpgradeHistoryTypeDef(TypedDict, total=False):
    UpgradeName: str
    StartTimestamp: datetime
    UpgradeStatus: UpgradeStatus
    StepsList: List["UpgradeStepItemTypeDef"]


class UpgradeStepItemTypeDef(TypedDict, total=False):
    UpgradeStep: UpgradeStep
    UpgradeStepStatus: UpgradeStatus
    Issues: List[str]
    ProgressPercent: float


class VPCDerivedInfoStatusTypeDef(TypedDict):
    Options: "VPCDerivedInfoTypeDef"
    Status: "OptionStatusTypeDef"


class VPCDerivedInfoTypeDef(TypedDict, total=False):
    VPCId: str
    SubnetIds: List[str]
    AvailabilityZones: List[str]
    SecurityGroupIds: List[str]


class VPCOptionsTypeDef(TypedDict, total=False):
    SubnetIds: List[str]
    SecurityGroupIds: List[str]


class ZoneAwarenessConfigTypeDef(TypedDict, total=False):
    AvailabilityZoneCount: int
