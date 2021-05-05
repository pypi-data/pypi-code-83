"""
Type annotations for redshift service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/type_defs.html)

Usage::

    ```python
    from mypy_boto3_redshift.type_defs import AcceptReservedNodeExchangeOutputMessageTypeDef

    data: AcceptReservedNodeExchangeOutputMessageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_redshift.literals import (
    AquaConfigurationStatus,
    AquaStatus,
    AuthorizationStatus,
    Mode,
    NodeConfigurationOptionsFilterName,
    OperatorType,
    ParameterApplyType,
    PartnerIntegrationStatus,
    ReservedNodeOfferingType,
    ScheduledActionFilterName,
    ScheduledActionState,
    ScheduleState,
    SnapshotAttributeToSortBy,
    SortByOrder,
    SourceType,
    TableRestoreStatusType,
    UsageLimitBreachAction,
    UsageLimitFeatureType,
    UsageLimitLimitType,
    UsageLimitPeriod,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptReservedNodeExchangeOutputMessageTypeDef",
    "AccountAttributeListTypeDef",
    "AccountAttributeTypeDef",
    "AccountWithRestoreAccessTypeDef",
    "AquaConfigurationTypeDef",
    "AttributeValueTargetTypeDef",
    "AuthorizeClusterSecurityGroupIngressResultTypeDef",
    "AuthorizeSnapshotAccessResultTypeDef",
    "AvailabilityZoneTypeDef",
    "BatchDeleteClusterSnapshotsResultTypeDef",
    "BatchModifyClusterSnapshotsOutputMessageTypeDef",
    "ClusterAssociatedToScheduleTypeDef",
    "ClusterCredentialsTypeDef",
    "ClusterDbRevisionTypeDef",
    "ClusterDbRevisionsMessageTypeDef",
    "ClusterIamRoleTypeDef",
    "ClusterNodeTypeDef",
    "ClusterParameterGroupDetailsTypeDef",
    "ClusterParameterGroupNameMessageTypeDef",
    "ClusterParameterGroupStatusTypeDef",
    "ClusterParameterGroupTypeDef",
    "ClusterParameterGroupsMessageTypeDef",
    "ClusterParameterStatusTypeDef",
    "ClusterSecurityGroupMembershipTypeDef",
    "ClusterSecurityGroupMessageTypeDef",
    "ClusterSecurityGroupTypeDef",
    "ClusterSnapshotCopyStatusTypeDef",
    "ClusterSubnetGroupMessageTypeDef",
    "ClusterSubnetGroupTypeDef",
    "ClusterTypeDef",
    "ClusterVersionTypeDef",
    "ClusterVersionsMessageTypeDef",
    "ClustersMessageTypeDef",
    "CopyClusterSnapshotResultTypeDef",
    "CreateClusterParameterGroupResultTypeDef",
    "CreateClusterResultTypeDef",
    "CreateClusterSecurityGroupResultTypeDef",
    "CreateClusterSnapshotResultTypeDef",
    "CreateClusterSubnetGroupResultTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "CreateHsmClientCertificateResultTypeDef",
    "CreateHsmConfigurationResultTypeDef",
    "CreateSnapshotCopyGrantResultTypeDef",
    "CustomerStorageMessageTypeDef",
    "DataTransferProgressTypeDef",
    "DefaultClusterParametersTypeDef",
    "DeferredMaintenanceWindowTypeDef",
    "DeleteClusterResultTypeDef",
    "DeleteClusterSnapshotMessageTypeDef",
    "DeleteClusterSnapshotResultTypeDef",
    "DescribeDefaultClusterParametersResultTypeDef",
    "DescribePartnersOutputMessageTypeDef",
    "DescribeSnapshotSchedulesOutputMessageTypeDef",
    "DisableSnapshotCopyResultTypeDef",
    "EC2SecurityGroupTypeDef",
    "ElasticIpStatusTypeDef",
    "EnableSnapshotCopyResultTypeDef",
    "EndpointAccessListTypeDef",
    "EndpointAccessTypeDef",
    "EndpointAuthorizationListTypeDef",
    "EndpointAuthorizationTypeDef",
    "EndpointTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventInfoMapTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "GetReservedNodeExchangeOfferingsOutputMessageTypeDef",
    "HsmClientCertificateMessageTypeDef",
    "HsmClientCertificateTypeDef",
    "HsmConfigurationMessageTypeDef",
    "HsmConfigurationTypeDef",
    "HsmStatusTypeDef",
    "IPRangeTypeDef",
    "LoggingStatusTypeDef",
    "MaintenanceTrackTypeDef",
    "ModifyAquaOutputMessageTypeDef",
    "ModifyClusterDbRevisionResultTypeDef",
    "ModifyClusterIamRolesResultTypeDef",
    "ModifyClusterMaintenanceResultTypeDef",
    "ModifyClusterResultTypeDef",
    "ModifyClusterSnapshotResultTypeDef",
    "ModifyClusterSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "ModifySnapshotCopyRetentionPeriodResultTypeDef",
    "NetworkInterfaceTypeDef",
    "NodeConfigurationOptionTypeDef",
    "NodeConfigurationOptionsFilterTypeDef",
    "NodeConfigurationOptionsMessageTypeDef",
    "OrderableClusterOptionTypeDef",
    "OrderableClusterOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PartnerIntegrationInfoTypeDef",
    "PartnerIntegrationOutputMessageTypeDef",
    "PauseClusterMessageTypeDef",
    "PauseClusterResultTypeDef",
    "PendingModifiedValuesTypeDef",
    "PurchaseReservedNodeOfferingResultTypeDef",
    "RebootClusterResultTypeDef",
    "RecurringChargeTypeDef",
    "ReservedNodeOfferingTypeDef",
    "ReservedNodeOfferingsMessageTypeDef",
    "ReservedNodeTypeDef",
    "ReservedNodesMessageTypeDef",
    "ResizeClusterMessageTypeDef",
    "ResizeClusterResultTypeDef",
    "ResizeInfoTypeDef",
    "ResizeProgressMessageTypeDef",
    "RestoreFromClusterSnapshotResultTypeDef",
    "RestoreStatusTypeDef",
    "RestoreTableFromClusterSnapshotResultTypeDef",
    "ResumeClusterMessageTypeDef",
    "ResumeClusterResultTypeDef",
    "RevisionTargetTypeDef",
    "RevokeClusterSecurityGroupIngressResultTypeDef",
    "RevokeSnapshotAccessResultTypeDef",
    "RotateEncryptionKeyResultTypeDef",
    "ScheduledActionFilterTypeDef",
    "ScheduledActionTypeDef",
    "ScheduledActionTypeTypeDef",
    "ScheduledActionsMessageTypeDef",
    "SnapshotCopyGrantMessageTypeDef",
    "SnapshotCopyGrantTypeDef",
    "SnapshotErrorMessageTypeDef",
    "SnapshotMessageTypeDef",
    "SnapshotScheduleTypeDef",
    "SnapshotSortingEntityTypeDef",
    "SnapshotTypeDef",
    "SubnetTypeDef",
    "SupportedOperationTypeDef",
    "SupportedPlatformTypeDef",
    "TableRestoreStatusMessageTypeDef",
    "TableRestoreStatusTypeDef",
    "TagTypeDef",
    "TaggedResourceListMessageTypeDef",
    "TaggedResourceTypeDef",
    "TrackListMessageTypeDef",
    "UpdateTargetTypeDef",
    "UsageLimitListTypeDef",
    "UsageLimitTypeDef",
    "VpcEndpointTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)


class AcceptReservedNodeExchangeOutputMessageTypeDef(TypedDict, total=False):
    ExchangedReservedNode: "ReservedNodeTypeDef"


class AccountAttributeListTypeDef(TypedDict, total=False):
    AccountAttributes: List["AccountAttributeTypeDef"]


class AccountAttributeTypeDef(TypedDict, total=False):
    AttributeName: str
    AttributeValues: List["AttributeValueTargetTypeDef"]


class AccountWithRestoreAccessTypeDef(TypedDict, total=False):
    AccountId: str
    AccountAlias: str


class AquaConfigurationTypeDef(TypedDict, total=False):
    AquaStatus: AquaStatus
    AquaConfigurationStatus: AquaConfigurationStatus


class AttributeValueTargetTypeDef(TypedDict, total=False):
    AttributeValue: str


class AuthorizeClusterSecurityGroupIngressResultTypeDef(TypedDict, total=False):
    ClusterSecurityGroup: "ClusterSecurityGroupTypeDef"


class AuthorizeSnapshotAccessResultTypeDef(TypedDict, total=False):
    Snapshot: "SnapshotTypeDef"


class AvailabilityZoneTypeDef(TypedDict, total=False):
    Name: str
    SupportedPlatforms: List["SupportedPlatformTypeDef"]


class BatchDeleteClusterSnapshotsResultTypeDef(TypedDict, total=False):
    Resources: List[str]
    Errors: List["SnapshotErrorMessageTypeDef"]


class BatchModifyClusterSnapshotsOutputMessageTypeDef(TypedDict, total=False):
    Resources: List[str]
    Errors: List["SnapshotErrorMessageTypeDef"]


class ClusterAssociatedToScheduleTypeDef(TypedDict, total=False):
    ClusterIdentifier: str
    ScheduleAssociationState: ScheduleState


class ClusterCredentialsTypeDef(TypedDict, total=False):
    DbUser: str
    DbPassword: str
    Expiration: datetime


class ClusterDbRevisionTypeDef(TypedDict, total=False):
    ClusterIdentifier: str
    CurrentDatabaseRevision: str
    DatabaseRevisionReleaseDate: datetime
    RevisionTargets: List["RevisionTargetTypeDef"]


class ClusterDbRevisionsMessageTypeDef(TypedDict, total=False):
    Marker: str
    ClusterDbRevisions: List["ClusterDbRevisionTypeDef"]


class ClusterIamRoleTypeDef(TypedDict, total=False):
    IamRoleArn: str
    ApplyStatus: str


class ClusterNodeTypeDef(TypedDict, total=False):
    NodeRole: str
    PrivateIPAddress: str
    PublicIPAddress: str


class ClusterParameterGroupDetailsTypeDef(TypedDict, total=False):
    Parameters: List["ParameterTypeDef"]
    Marker: str


class ClusterParameterGroupNameMessageTypeDef(TypedDict, total=False):
    ParameterGroupName: str
    ParameterGroupStatus: str


class ClusterParameterGroupStatusTypeDef(TypedDict, total=False):
    ParameterGroupName: str
    ParameterApplyStatus: str
    ClusterParameterStatusList: List["ClusterParameterStatusTypeDef"]


class ClusterParameterGroupTypeDef(TypedDict, total=False):
    ParameterGroupName: str
    ParameterGroupFamily: str
    Description: str
    Tags: List["TagTypeDef"]


class ClusterParameterGroupsMessageTypeDef(TypedDict, total=False):
    Marker: str
    ParameterGroups: List["ClusterParameterGroupTypeDef"]


class ClusterParameterStatusTypeDef(TypedDict, total=False):
    ParameterName: str
    ParameterApplyStatus: str
    ParameterApplyErrorDescription: str


class ClusterSecurityGroupMembershipTypeDef(TypedDict, total=False):
    ClusterSecurityGroupName: str
    Status: str


class ClusterSecurityGroupMessageTypeDef(TypedDict, total=False):
    Marker: str
    ClusterSecurityGroups: List["ClusterSecurityGroupTypeDef"]


class ClusterSecurityGroupTypeDef(TypedDict, total=False):
    ClusterSecurityGroupName: str
    Description: str
    EC2SecurityGroups: List["EC2SecurityGroupTypeDef"]
    IPRanges: List["IPRangeTypeDef"]
    Tags: List["TagTypeDef"]


class ClusterSnapshotCopyStatusTypeDef(TypedDict, total=False):
    DestinationRegion: str
    RetentionPeriod: int
    ManualSnapshotRetentionPeriod: int
    SnapshotCopyGrantName: str


class ClusterSubnetGroupMessageTypeDef(TypedDict, total=False):
    Marker: str
    ClusterSubnetGroups: List["ClusterSubnetGroupTypeDef"]


class ClusterSubnetGroupTypeDef(TypedDict, total=False):
    ClusterSubnetGroupName: str
    Description: str
    VpcId: str
    SubnetGroupStatus: str
    Subnets: List["SubnetTypeDef"]
    Tags: List["TagTypeDef"]


class ClusterTypeDef(TypedDict, total=False):
    ClusterIdentifier: str
    NodeType: str
    ClusterStatus: str
    ClusterAvailabilityStatus: str
    ModifyStatus: str
    MasterUsername: str
    DBName: str
    Endpoint: "EndpointTypeDef"
    ClusterCreateTime: datetime
    AutomatedSnapshotRetentionPeriod: int
    ManualSnapshotRetentionPeriod: int
    ClusterSecurityGroups: List["ClusterSecurityGroupMembershipTypeDef"]
    VpcSecurityGroups: List["VpcSecurityGroupMembershipTypeDef"]
    ClusterParameterGroups: List["ClusterParameterGroupStatusTypeDef"]
    ClusterSubnetGroupName: str
    VpcId: str
    AvailabilityZone: str
    PreferredMaintenanceWindow: str
    PendingModifiedValues: "PendingModifiedValuesTypeDef"
    ClusterVersion: str
    AllowVersionUpgrade: bool
    NumberOfNodes: int
    PubliclyAccessible: bool
    Encrypted: bool
    RestoreStatus: "RestoreStatusTypeDef"
    DataTransferProgress: "DataTransferProgressTypeDef"
    HsmStatus: "HsmStatusTypeDef"
    ClusterSnapshotCopyStatus: "ClusterSnapshotCopyStatusTypeDef"
    ClusterPublicKey: str
    ClusterNodes: List["ClusterNodeTypeDef"]
    ElasticIpStatus: "ElasticIpStatusTypeDef"
    ClusterRevisionNumber: str
    Tags: List["TagTypeDef"]
    KmsKeyId: str
    EnhancedVpcRouting: bool
    IamRoles: List["ClusterIamRoleTypeDef"]
    PendingActions: List[str]
    MaintenanceTrackName: str
    ElasticResizeNumberOfNodeOptions: str
    DeferredMaintenanceWindows: List["DeferredMaintenanceWindowTypeDef"]
    SnapshotScheduleIdentifier: str
    SnapshotScheduleState: ScheduleState
    ExpectedNextSnapshotScheduleTime: datetime
    ExpectedNextSnapshotScheduleTimeStatus: str
    NextMaintenanceWindowStartTime: datetime
    ResizeInfo: "ResizeInfoTypeDef"
    AvailabilityZoneRelocationStatus: str
    ClusterNamespaceArn: str
    TotalStorageCapacityInMegaBytes: int
    AquaConfiguration: "AquaConfigurationTypeDef"


class ClusterVersionTypeDef(TypedDict, total=False):
    ClusterVersion: str
    ClusterParameterGroupFamily: str
    Description: str


class ClusterVersionsMessageTypeDef(TypedDict, total=False):
    Marker: str
    ClusterVersions: List["ClusterVersionTypeDef"]


class ClustersMessageTypeDef(TypedDict, total=False):
    Marker: str
    Clusters: List["ClusterTypeDef"]


class CopyClusterSnapshotResultTypeDef(TypedDict, total=False):
    Snapshot: "SnapshotTypeDef"


class CreateClusterParameterGroupResultTypeDef(TypedDict, total=False):
    ClusterParameterGroup: "ClusterParameterGroupTypeDef"


class CreateClusterResultTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class CreateClusterSecurityGroupResultTypeDef(TypedDict, total=False):
    ClusterSecurityGroup: "ClusterSecurityGroupTypeDef"


class CreateClusterSnapshotResultTypeDef(TypedDict, total=False):
    Snapshot: "SnapshotTypeDef"


class CreateClusterSubnetGroupResultTypeDef(TypedDict, total=False):
    ClusterSubnetGroup: "ClusterSubnetGroupTypeDef"


class CreateEventSubscriptionResultTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class CreateHsmClientCertificateResultTypeDef(TypedDict, total=False):
    HsmClientCertificate: "HsmClientCertificateTypeDef"


class CreateHsmConfigurationResultTypeDef(TypedDict, total=False):
    HsmConfiguration: "HsmConfigurationTypeDef"


class CreateSnapshotCopyGrantResultTypeDef(TypedDict, total=False):
    SnapshotCopyGrant: "SnapshotCopyGrantTypeDef"


class CustomerStorageMessageTypeDef(TypedDict, total=False):
    TotalBackupSizeInMegaBytes: float
    TotalProvisionedStorageInMegaBytes: float


class DataTransferProgressTypeDef(TypedDict, total=False):
    Status: str
    CurrentRateInMegaBytesPerSecond: float
    TotalDataInMegaBytes: int
    DataTransferredInMegaBytes: int
    EstimatedTimeToCompletionInSeconds: int
    ElapsedTimeInSeconds: int


class DefaultClusterParametersTypeDef(TypedDict, total=False):
    ParameterGroupFamily: str
    Marker: str
    Parameters: List["ParameterTypeDef"]


class DeferredMaintenanceWindowTypeDef(TypedDict, total=False):
    DeferMaintenanceIdentifier: str
    DeferMaintenanceStartTime: datetime
    DeferMaintenanceEndTime: datetime


class DeleteClusterResultTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class _RequiredDeleteClusterSnapshotMessageTypeDef(TypedDict):
    SnapshotIdentifier: str


class DeleteClusterSnapshotMessageTypeDef(
    _RequiredDeleteClusterSnapshotMessageTypeDef, total=False
):
    SnapshotClusterIdentifier: str


class DeleteClusterSnapshotResultTypeDef(TypedDict, total=False):
    Snapshot: "SnapshotTypeDef"


class DescribeDefaultClusterParametersResultTypeDef(TypedDict, total=False):
    DefaultClusterParameters: "DefaultClusterParametersTypeDef"


class DescribePartnersOutputMessageTypeDef(TypedDict, total=False):
    PartnerIntegrationInfoList: List["PartnerIntegrationInfoTypeDef"]


class DescribeSnapshotSchedulesOutputMessageTypeDef(TypedDict, total=False):
    SnapshotSchedules: List["SnapshotScheduleTypeDef"]
    Marker: str


class DisableSnapshotCopyResultTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class EC2SecurityGroupTypeDef(TypedDict, total=False):
    Status: str
    EC2SecurityGroupName: str
    EC2SecurityGroupOwnerId: str
    Tags: List["TagTypeDef"]


class ElasticIpStatusTypeDef(TypedDict, total=False):
    ElasticIp: str
    Status: str


class EnableSnapshotCopyResultTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class EndpointAccessListTypeDef(TypedDict, total=False):
    EndpointAccessList: List["EndpointAccessTypeDef"]
    Marker: str


class EndpointAccessTypeDef(TypedDict, total=False):
    ClusterIdentifier: str
    ResourceOwner: str
    SubnetGroupName: str
    EndpointStatus: str
    EndpointName: str
    EndpointCreateTime: datetime
    Port: int
    Address: str
    VpcSecurityGroups: List["VpcSecurityGroupMembershipTypeDef"]
    VpcEndpoint: "VpcEndpointTypeDef"


class EndpointAuthorizationListTypeDef(TypedDict, total=False):
    EndpointAuthorizationList: List["EndpointAuthorizationTypeDef"]
    Marker: str


class EndpointAuthorizationTypeDef(TypedDict, total=False):
    Grantor: str
    Grantee: str
    ClusterIdentifier: str
    AuthorizeTime: datetime
    ClusterStatus: str
    Status: AuthorizationStatus
    AllowedAllVPCs: bool
    AllowedVPCs: List[str]
    EndpointCount: int


class EndpointTypeDef(TypedDict, total=False):
    Address: str
    Port: int
    VpcEndpoints: List["VpcEndpointTypeDef"]


class EventCategoriesMapTypeDef(TypedDict, total=False):
    SourceType: str
    Events: List["EventInfoMapTypeDef"]


class EventCategoriesMessageTypeDef(TypedDict, total=False):
    EventCategoriesMapList: List["EventCategoriesMapTypeDef"]


class EventInfoMapTypeDef(TypedDict, total=False):
    EventId: str
    EventCategories: List[str]
    EventDescription: str
    Severity: str


class EventSubscriptionTypeDef(TypedDict, total=False):
    CustomerAwsId: str
    CustSubscriptionId: str
    SnsTopicArn: str
    Status: str
    SubscriptionCreationTime: datetime
    SourceType: str
    SourceIdsList: List[str]
    EventCategoriesList: List[str]
    Severity: str
    Enabled: bool
    Tags: List["TagTypeDef"]


class EventSubscriptionsMessageTypeDef(TypedDict, total=False):
    Marker: str
    EventSubscriptionsList: List["EventSubscriptionTypeDef"]


class EventTypeDef(TypedDict, total=False):
    SourceIdentifier: str
    SourceType: SourceType
    Message: str
    EventCategories: List[str]
    Severity: str
    Date: datetime
    EventId: str


class EventsMessageTypeDef(TypedDict, total=False):
    Marker: str
    Events: List["EventTypeDef"]


class GetReservedNodeExchangeOfferingsOutputMessageTypeDef(TypedDict, total=False):
    Marker: str
    ReservedNodeOfferings: List["ReservedNodeOfferingTypeDef"]


class HsmClientCertificateMessageTypeDef(TypedDict, total=False):
    Marker: str
    HsmClientCertificates: List["HsmClientCertificateTypeDef"]


class HsmClientCertificateTypeDef(TypedDict, total=False):
    HsmClientCertificateIdentifier: str
    HsmClientCertificatePublicKey: str
    Tags: List["TagTypeDef"]


class HsmConfigurationMessageTypeDef(TypedDict, total=False):
    Marker: str
    HsmConfigurations: List["HsmConfigurationTypeDef"]


class HsmConfigurationTypeDef(TypedDict, total=False):
    HsmConfigurationIdentifier: str
    Description: str
    HsmIpAddress: str
    HsmPartitionName: str
    Tags: List["TagTypeDef"]


class HsmStatusTypeDef(TypedDict, total=False):
    HsmClientCertificateIdentifier: str
    HsmConfigurationIdentifier: str
    Status: str


class IPRangeTypeDef(TypedDict, total=False):
    Status: str
    CIDRIP: str
    Tags: List["TagTypeDef"]


class LoggingStatusTypeDef(TypedDict, total=False):
    LoggingEnabled: bool
    BucketName: str
    S3KeyPrefix: str
    LastSuccessfulDeliveryTime: datetime
    LastFailureTime: datetime
    LastFailureMessage: str


class MaintenanceTrackTypeDef(TypedDict, total=False):
    MaintenanceTrackName: str
    DatabaseVersion: str
    UpdateTargets: List["UpdateTargetTypeDef"]


class ModifyAquaOutputMessageTypeDef(TypedDict, total=False):
    AquaConfiguration: "AquaConfigurationTypeDef"


class ModifyClusterDbRevisionResultTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class ModifyClusterIamRolesResultTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class ModifyClusterMaintenanceResultTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class ModifyClusterResultTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class ModifyClusterSnapshotResultTypeDef(TypedDict, total=False):
    Snapshot: "SnapshotTypeDef"


class ModifyClusterSubnetGroupResultTypeDef(TypedDict, total=False):
    ClusterSubnetGroup: "ClusterSubnetGroupTypeDef"


class ModifyEventSubscriptionResultTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class ModifySnapshotCopyRetentionPeriodResultTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class NetworkInterfaceTypeDef(TypedDict, total=False):
    NetworkInterfaceId: str
    SubnetId: str
    PrivateIpAddress: str
    AvailabilityZone: str


class NodeConfigurationOptionTypeDef(TypedDict, total=False):
    NodeType: str
    NumberOfNodes: int
    EstimatedDiskUtilizationPercent: float
    Mode: Mode


class NodeConfigurationOptionsFilterTypeDef(TypedDict, total=False):
    Name: NodeConfigurationOptionsFilterName
    Operator: OperatorType
    Values: List[str]


class NodeConfigurationOptionsMessageTypeDef(TypedDict, total=False):
    NodeConfigurationOptionList: List["NodeConfigurationOptionTypeDef"]
    Marker: str


class OrderableClusterOptionTypeDef(TypedDict, total=False):
    ClusterVersion: str
    ClusterType: str
    NodeType: str
    AvailabilityZones: List["AvailabilityZoneTypeDef"]


class OrderableClusterOptionsMessageTypeDef(TypedDict, total=False):
    OrderableClusterOptions: List["OrderableClusterOptionTypeDef"]
    Marker: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParameterTypeDef(TypedDict, total=False):
    ParameterName: str
    ParameterValue: str
    Description: str
    Source: str
    DataType: str
    AllowedValues: str
    ApplyType: ParameterApplyType
    IsModifiable: bool
    MinimumEngineVersion: str


class PartnerIntegrationInfoTypeDef(TypedDict, total=False):
    DatabaseName: str
    PartnerName: str
    Status: PartnerIntegrationStatus
    StatusMessage: str
    CreatedAt: datetime
    UpdatedAt: datetime


class PartnerIntegrationOutputMessageTypeDef(TypedDict, total=False):
    DatabaseName: str
    PartnerName: str


class PauseClusterMessageTypeDef(TypedDict):
    ClusterIdentifier: str


class PauseClusterResultTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class PendingModifiedValuesTypeDef(TypedDict, total=False):
    MasterUserPassword: str
    NodeType: str
    NumberOfNodes: int
    ClusterType: str
    ClusterVersion: str
    AutomatedSnapshotRetentionPeriod: int
    ClusterIdentifier: str
    PubliclyAccessible: bool
    EnhancedVpcRouting: bool
    MaintenanceTrackName: str
    EncryptionType: str


class PurchaseReservedNodeOfferingResultTypeDef(TypedDict, total=False):
    ReservedNode: "ReservedNodeTypeDef"


class RebootClusterResultTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class RecurringChargeTypeDef(TypedDict, total=False):
    RecurringChargeAmount: float
    RecurringChargeFrequency: str


class ReservedNodeOfferingTypeDef(TypedDict, total=False):
    ReservedNodeOfferingId: str
    NodeType: str
    Duration: int
    FixedPrice: float
    UsagePrice: float
    CurrencyCode: str
    OfferingType: str
    RecurringCharges: List["RecurringChargeTypeDef"]
    ReservedNodeOfferingType: ReservedNodeOfferingType


class ReservedNodeOfferingsMessageTypeDef(TypedDict, total=False):
    Marker: str
    ReservedNodeOfferings: List["ReservedNodeOfferingTypeDef"]


class ReservedNodeTypeDef(TypedDict, total=False):
    ReservedNodeId: str
    ReservedNodeOfferingId: str
    NodeType: str
    StartTime: datetime
    Duration: int
    FixedPrice: float
    UsagePrice: float
    CurrencyCode: str
    NodeCount: int
    State: str
    OfferingType: str
    RecurringCharges: List["RecurringChargeTypeDef"]
    ReservedNodeOfferingType: ReservedNodeOfferingType


class ReservedNodesMessageTypeDef(TypedDict, total=False):
    Marker: str
    ReservedNodes: List["ReservedNodeTypeDef"]


class _RequiredResizeClusterMessageTypeDef(TypedDict):
    ClusterIdentifier: str


class ResizeClusterMessageTypeDef(_RequiredResizeClusterMessageTypeDef, total=False):
    ClusterType: str
    NodeType: str
    NumberOfNodes: int
    Classic: bool


class ResizeClusterResultTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class ResizeInfoTypeDef(TypedDict, total=False):
    ResizeType: str
    AllowCancelResize: bool


class ResizeProgressMessageTypeDef(TypedDict, total=False):
    TargetNodeType: str
    TargetNumberOfNodes: int
    TargetClusterType: str
    Status: str
    ImportTablesCompleted: List[str]
    ImportTablesInProgress: List[str]
    ImportTablesNotStarted: List[str]
    AvgResizeRateInMegaBytesPerSecond: float
    TotalResizeDataInMegaBytes: int
    ProgressInMegaBytes: int
    ElapsedTimeInSeconds: int
    EstimatedTimeToCompletionInSeconds: int
    ResizeType: str
    Message: str
    TargetEncryptionType: str
    DataTransferProgressPercent: float


class RestoreFromClusterSnapshotResultTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class RestoreStatusTypeDef(TypedDict, total=False):
    Status: str
    CurrentRestoreRateInMegaBytesPerSecond: float
    SnapshotSizeInMegaBytes: int
    ProgressInMegaBytes: int
    ElapsedTimeInSeconds: int
    EstimatedTimeToCompletionInSeconds: int


class RestoreTableFromClusterSnapshotResultTypeDef(TypedDict, total=False):
    TableRestoreStatus: "TableRestoreStatusTypeDef"


class ResumeClusterMessageTypeDef(TypedDict):
    ClusterIdentifier: str


class ResumeClusterResultTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class RevisionTargetTypeDef(TypedDict, total=False):
    DatabaseRevision: str
    Description: str
    DatabaseRevisionReleaseDate: datetime


class RevokeClusterSecurityGroupIngressResultTypeDef(TypedDict, total=False):
    ClusterSecurityGroup: "ClusterSecurityGroupTypeDef"


class RevokeSnapshotAccessResultTypeDef(TypedDict, total=False):
    Snapshot: "SnapshotTypeDef"


class RotateEncryptionKeyResultTypeDef(TypedDict, total=False):
    Cluster: "ClusterTypeDef"


class ScheduledActionFilterTypeDef(TypedDict):
    Name: ScheduledActionFilterName
    Values: List[str]


class ScheduledActionTypeDef(TypedDict, total=False):
    ScheduledActionName: str
    TargetAction: "ScheduledActionTypeTypeDef"
    Schedule: str
    IamRole: str
    ScheduledActionDescription: str
    State: ScheduledActionState
    NextInvocations: List[datetime]
    StartTime: datetime
    EndTime: datetime


class ScheduledActionTypeTypeDef(TypedDict, total=False):
    ResizeCluster: "ResizeClusterMessageTypeDef"
    PauseCluster: "PauseClusterMessageTypeDef"
    ResumeCluster: "ResumeClusterMessageTypeDef"


class ScheduledActionsMessageTypeDef(TypedDict, total=False):
    Marker: str
    ScheduledActions: List["ScheduledActionTypeDef"]


class SnapshotCopyGrantMessageTypeDef(TypedDict, total=False):
    Marker: str
    SnapshotCopyGrants: List["SnapshotCopyGrantTypeDef"]


class SnapshotCopyGrantTypeDef(TypedDict, total=False):
    SnapshotCopyGrantName: str
    KmsKeyId: str
    Tags: List["TagTypeDef"]


class SnapshotErrorMessageTypeDef(TypedDict, total=False):
    SnapshotIdentifier: str
    SnapshotClusterIdentifier: str
    FailureCode: str
    FailureReason: str


class SnapshotMessageTypeDef(TypedDict, total=False):
    Marker: str
    Snapshots: List["SnapshotTypeDef"]


class SnapshotScheduleTypeDef(TypedDict, total=False):
    ScheduleDefinitions: List[str]
    ScheduleIdentifier: str
    ScheduleDescription: str
    Tags: List["TagTypeDef"]
    NextInvocations: List[datetime]
    AssociatedClusterCount: int
    AssociatedClusters: List["ClusterAssociatedToScheduleTypeDef"]


class _RequiredSnapshotSortingEntityTypeDef(TypedDict):
    Attribute: SnapshotAttributeToSortBy


class SnapshotSortingEntityTypeDef(_RequiredSnapshotSortingEntityTypeDef, total=False):
    SortOrder: SortByOrder


class SnapshotTypeDef(TypedDict, total=False):
    SnapshotIdentifier: str
    ClusterIdentifier: str
    SnapshotCreateTime: datetime
    Status: str
    Port: int
    AvailabilityZone: str
    ClusterCreateTime: datetime
    MasterUsername: str
    ClusterVersion: str
    EngineFullVersion: str
    SnapshotType: str
    NodeType: str
    NumberOfNodes: int
    DBName: str
    VpcId: str
    Encrypted: bool
    KmsKeyId: str
    EncryptedWithHSM: bool
    AccountsWithRestoreAccess: List["AccountWithRestoreAccessTypeDef"]
    OwnerAccount: str
    TotalBackupSizeInMegaBytes: float
    ActualIncrementalBackupSizeInMegaBytes: float
    BackupProgressInMegaBytes: float
    CurrentBackupRateInMegaBytesPerSecond: float
    EstimatedSecondsToCompletion: int
    ElapsedTimeInSeconds: int
    SourceRegion: str
    Tags: List["TagTypeDef"]
    RestorableNodeTypes: List[str]
    EnhancedVpcRouting: bool
    MaintenanceTrackName: str
    ManualSnapshotRetentionPeriod: int
    ManualSnapshotRemainingDays: int
    SnapshotRetentionStartTime: datetime


class SubnetTypeDef(TypedDict, total=False):
    SubnetIdentifier: str
    SubnetAvailabilityZone: "AvailabilityZoneTypeDef"
    SubnetStatus: str


class SupportedOperationTypeDef(TypedDict, total=False):
    OperationName: str


class SupportedPlatformTypeDef(TypedDict, total=False):
    Name: str


class TableRestoreStatusMessageTypeDef(TypedDict, total=False):
    TableRestoreStatusDetails: List["TableRestoreStatusTypeDef"]
    Marker: str


class TableRestoreStatusTypeDef(TypedDict, total=False):
    TableRestoreRequestId: str
    Status: TableRestoreStatusType
    Message: str
    RequestTime: datetime
    ProgressInMegaBytes: int
    TotalDataInMegaBytes: int
    ClusterIdentifier: str
    SnapshotIdentifier: str
    SourceDatabaseName: str
    SourceSchemaName: str
    SourceTableName: str
    TargetDatabaseName: str
    TargetSchemaName: str
    NewTableName: str


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class TaggedResourceListMessageTypeDef(TypedDict, total=False):
    TaggedResources: List["TaggedResourceTypeDef"]
    Marker: str


class TaggedResourceTypeDef(TypedDict, total=False):
    Tag: "TagTypeDef"
    ResourceName: str
    ResourceType: str


class TrackListMessageTypeDef(TypedDict, total=False):
    MaintenanceTracks: List["MaintenanceTrackTypeDef"]
    Marker: str


class UpdateTargetTypeDef(TypedDict, total=False):
    MaintenanceTrackName: str
    DatabaseVersion: str
    SupportedOperations: List["SupportedOperationTypeDef"]


class UsageLimitListTypeDef(TypedDict, total=False):
    UsageLimits: List["UsageLimitTypeDef"]
    Marker: str


class UsageLimitTypeDef(TypedDict, total=False):
    UsageLimitId: str
    ClusterIdentifier: str
    FeatureType: UsageLimitFeatureType
    LimitType: UsageLimitLimitType
    Amount: int
    Period: UsageLimitPeriod
    BreachAction: UsageLimitBreachAction
    Tags: List["TagTypeDef"]


class VpcEndpointTypeDef(TypedDict, total=False):
    VpcEndpointId: str
    VpcId: str
    NetworkInterfaces: List["NetworkInterfaceTypeDef"]


class VpcSecurityGroupMembershipTypeDef(TypedDict, total=False):
    VpcSecurityGroupId: str
    Status: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
