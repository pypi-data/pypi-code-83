"""
Type annotations for rds service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rds.type_defs import AccountAttributesMessageTypeDef

    data: AccountAttributesMessageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_rds.literals import (
    ActivityStreamMode,
    ActivityStreamStatus,
    ApplyMethod,
    DBProxyEndpointStatus,
    DBProxyEndpointTargetRole,
    DBProxyStatus,
    FailoverStatus,
    IAMAuthMode,
    ReplicaMode,
    SourceType,
    TargetHealthReason,
    TargetRole,
    TargetState,
    TargetType,
    WriteForwardingStatus,
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
    "AccountAttributesMessageTypeDef",
    "AccountQuotaTypeDef",
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    "ApplyPendingMaintenanceActionResultTypeDef",
    "AuthorizeDBSecurityGroupIngressResultTypeDef",
    "AvailabilityZoneTypeDef",
    "AvailableProcessorFeatureTypeDef",
    "CertificateMessageTypeDef",
    "CertificateTypeDef",
    "CharacterSetTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "ClusterPendingModifiedValuesTypeDef",
    "ConnectionPoolConfigurationInfoTypeDef",
    "ConnectionPoolConfigurationTypeDef",
    "CopyDBClusterParameterGroupResultTypeDef",
    "CopyDBClusterSnapshotResultTypeDef",
    "CopyDBParameterGroupResultTypeDef",
    "CopyDBSnapshotResultTypeDef",
    "CopyOptionGroupResultTypeDef",
    "CreateCustomAvailabilityZoneResultTypeDef",
    "CreateDBClusterParameterGroupResultTypeDef",
    "CreateDBClusterResultTypeDef",
    "CreateDBClusterSnapshotResultTypeDef",
    "CreateDBInstanceReadReplicaResultTypeDef",
    "CreateDBInstanceResultTypeDef",
    "CreateDBParameterGroupResultTypeDef",
    "CreateDBProxyEndpointResponseTypeDef",
    "CreateDBProxyResponseTypeDef",
    "CreateDBSecurityGroupResultTypeDef",
    "CreateDBSnapshotResultTypeDef",
    "CreateDBSubnetGroupResultTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "CreateGlobalClusterResultTypeDef",
    "CreateOptionGroupResultTypeDef",
    "CustomAvailabilityZoneMessageTypeDef",
    "CustomAvailabilityZoneTypeDef",
    "DBClusterBacktrackMessageTypeDef",
    "DBClusterBacktrackTypeDef",
    "DBClusterCapacityInfoTypeDef",
    "DBClusterEndpointMessageTypeDef",
    "DBClusterEndpointTypeDef",
    "DBClusterMemberTypeDef",
    "DBClusterMessageTypeDef",
    "DBClusterOptionGroupStatusTypeDef",
    "DBClusterParameterGroupDetailsTypeDef",
    "DBClusterParameterGroupNameMessageTypeDef",
    "DBClusterParameterGroupTypeDef",
    "DBClusterParameterGroupsMessageTypeDef",
    "DBClusterRoleTypeDef",
    "DBClusterSnapshotAttributeTypeDef",
    "DBClusterSnapshotAttributesResultTypeDef",
    "DBClusterSnapshotMessageTypeDef",
    "DBClusterSnapshotTypeDef",
    "DBClusterTypeDef",
    "DBEngineVersionMessageTypeDef",
    "DBEngineVersionTypeDef",
    "DBInstanceAutomatedBackupMessageTypeDef",
    "DBInstanceAutomatedBackupTypeDef",
    "DBInstanceAutomatedBackupsReplicationTypeDef",
    "DBInstanceMessageTypeDef",
    "DBInstanceRoleTypeDef",
    "DBInstanceStatusInfoTypeDef",
    "DBInstanceTypeDef",
    "DBParameterGroupDetailsTypeDef",
    "DBParameterGroupNameMessageTypeDef",
    "DBParameterGroupStatusTypeDef",
    "DBParameterGroupTypeDef",
    "DBParameterGroupsMessageTypeDef",
    "DBProxyEndpointTypeDef",
    "DBProxyTargetGroupTypeDef",
    "DBProxyTargetTypeDef",
    "DBProxyTypeDef",
    "DBSecurityGroupMembershipTypeDef",
    "DBSecurityGroupMessageTypeDef",
    "DBSecurityGroupTypeDef",
    "DBSnapshotAttributeTypeDef",
    "DBSnapshotAttributesResultTypeDef",
    "DBSnapshotMessageTypeDef",
    "DBSnapshotTypeDef",
    "DBSubnetGroupMessageTypeDef",
    "DBSubnetGroupTypeDef",
    "DeleteCustomAvailabilityZoneResultTypeDef",
    "DeleteDBClusterResultTypeDef",
    "DeleteDBClusterSnapshotResultTypeDef",
    "DeleteDBInstanceAutomatedBackupResultTypeDef",
    "DeleteDBInstanceResultTypeDef",
    "DeleteDBProxyEndpointResponseTypeDef",
    "DeleteDBProxyResponseTypeDef",
    "DeleteDBSnapshotResultTypeDef",
    "DeleteEventSubscriptionResultTypeDef",
    "DeleteGlobalClusterResultTypeDef",
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    "DescribeDBLogFilesDetailsTypeDef",
    "DescribeDBLogFilesResponseTypeDef",
    "DescribeDBProxiesResponseTypeDef",
    "DescribeDBProxyEndpointsResponseTypeDef",
    "DescribeDBProxyTargetGroupsResponseTypeDef",
    "DescribeDBProxyTargetsResponseTypeDef",
    "DescribeDBSnapshotAttributesResultTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "DescribeValidDBInstanceModificationsResultTypeDef",
    "DomainMembershipTypeDef",
    "DoubleRangeTypeDef",
    "DownloadDBLogFilePortionDetailsTypeDef",
    "EC2SecurityGroupTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "ExportTaskTypeDef",
    "ExportTasksMessageTypeDef",
    "FailoverDBClusterResultTypeDef",
    "FailoverGlobalClusterResultTypeDef",
    "FailoverStateTypeDef",
    "FilterTypeDef",
    "GlobalClusterMemberTypeDef",
    "GlobalClusterTypeDef",
    "GlobalClustersMessageTypeDef",
    "IPRangeTypeDef",
    "InstallationMediaFailureCauseTypeDef",
    "InstallationMediaMessageTypeDef",
    "InstallationMediaTypeDef",
    "MinimumEngineVersionPerAllowedValueTypeDef",
    "ModifyCertificatesResultTypeDef",
    "ModifyDBClusterResultTypeDef",
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    "ModifyDBInstanceResultTypeDef",
    "ModifyDBProxyEndpointResponseTypeDef",
    "ModifyDBProxyResponseTypeDef",
    "ModifyDBProxyTargetGroupResponseTypeDef",
    "ModifyDBSnapshotAttributeResultTypeDef",
    "ModifyDBSnapshotResultTypeDef",
    "ModifyDBSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "ModifyGlobalClusterResultTypeDef",
    "ModifyOptionGroupResultTypeDef",
    "OptionConfigurationTypeDef",
    "OptionGroupMembershipTypeDef",
    "OptionGroupOptionSettingTypeDef",
    "OptionGroupOptionTypeDef",
    "OptionGroupOptionsMessageTypeDef",
    "OptionGroupTypeDef",
    "OptionGroupsTypeDef",
    "OptionSettingTypeDef",
    "OptionTypeDef",
    "OptionVersionTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "OutpostTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "PendingModifiedValuesTypeDef",
    "ProcessorFeatureTypeDef",
    "PromoteReadReplicaDBClusterResultTypeDef",
    "PromoteReadReplicaResultTypeDef",
    "PurchaseReservedDBInstancesOfferingResultTypeDef",
    "RangeTypeDef",
    "RebootDBInstanceResultTypeDef",
    "RecurringChargeTypeDef",
    "RegisterDBProxyTargetsResponseTypeDef",
    "RemoveFromGlobalClusterResultTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    "ReservedDBInstanceMessageTypeDef",
    "ReservedDBInstanceTypeDef",
    "ReservedDBInstancesOfferingMessageTypeDef",
    "ReservedDBInstancesOfferingTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "RestoreDBClusterFromS3ResultTypeDef",
    "RestoreDBClusterFromSnapshotResultTypeDef",
    "RestoreDBClusterToPointInTimeResultTypeDef",
    "RestoreDBInstanceFromDBSnapshotResultTypeDef",
    "RestoreDBInstanceFromS3ResultTypeDef",
    "RestoreDBInstanceToPointInTimeResultTypeDef",
    "RestoreWindowTypeDef",
    "RevokeDBSecurityGroupIngressResultTypeDef",
    "ScalingConfigurationInfoTypeDef",
    "ScalingConfigurationTypeDef",
    "SourceRegionMessageTypeDef",
    "SourceRegionTypeDef",
    "StartActivityStreamResponseTypeDef",
    "StartDBClusterResultTypeDef",
    "StartDBInstanceAutomatedBackupsReplicationResultTypeDef",
    "StartDBInstanceResultTypeDef",
    "StopActivityStreamResponseTypeDef",
    "StopDBClusterResultTypeDef",
    "StopDBInstanceAutomatedBackupsReplicationResultTypeDef",
    "StopDBInstanceResultTypeDef",
    "SubnetTypeDef",
    "TagListMessageTypeDef",
    "TagTypeDef",
    "TargetHealthTypeDef",
    "TimezoneTypeDef",
    "UpgradeTargetTypeDef",
    "UserAuthConfigInfoTypeDef",
    "UserAuthConfigTypeDef",
    "ValidDBInstanceModificationsMessageTypeDef",
    "ValidStorageOptionsTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "VpnDetailsTypeDef",
    "WaiterConfigTypeDef",
)


class AccountAttributesMessageTypeDef(TypedDict, total=False):
    AccountQuotas: List["AccountQuotaTypeDef"]


class AccountQuotaTypeDef(TypedDict, total=False):
    AccountQuotaName: str
    Used: int
    Max: int


class AddSourceIdentifierToSubscriptionResultTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class ApplyPendingMaintenanceActionResultTypeDef(TypedDict, total=False):
    ResourcePendingMaintenanceActions: "ResourcePendingMaintenanceActionsTypeDef"


class AuthorizeDBSecurityGroupIngressResultTypeDef(TypedDict, total=False):
    DBSecurityGroup: "DBSecurityGroupTypeDef"


class AvailabilityZoneTypeDef(TypedDict, total=False):
    Name: str


class AvailableProcessorFeatureTypeDef(TypedDict, total=False):
    Name: str
    DefaultValue: str
    AllowedValues: str


class CertificateMessageTypeDef(TypedDict, total=False):
    Certificates: List["CertificateTypeDef"]
    Marker: str


class CertificateTypeDef(TypedDict, total=False):
    CertificateIdentifier: str
    CertificateType: str
    Thumbprint: str
    ValidFrom: datetime
    ValidTill: datetime
    CertificateArn: str
    CustomerOverride: bool
    CustomerOverrideValidTill: datetime


class CharacterSetTypeDef(TypedDict, total=False):
    CharacterSetName: str
    CharacterSetDescription: str


class CloudwatchLogsExportConfigurationTypeDef(TypedDict, total=False):
    EnableLogTypes: List[str]
    DisableLogTypes: List[str]


class ClusterPendingModifiedValuesTypeDef(TypedDict, total=False):
    PendingCloudwatchLogsExports: "PendingCloudwatchLogsExportsTypeDef"
    DBClusterIdentifier: str
    MasterUserPassword: str
    IAMDatabaseAuthenticationEnabled: bool
    EngineVersion: str


class ConnectionPoolConfigurationInfoTypeDef(TypedDict, total=False):
    MaxConnectionsPercent: int
    MaxIdleConnectionsPercent: int
    ConnectionBorrowTimeout: int
    SessionPinningFilters: List[str]
    InitQuery: str


class ConnectionPoolConfigurationTypeDef(TypedDict, total=False):
    MaxConnectionsPercent: int
    MaxIdleConnectionsPercent: int
    ConnectionBorrowTimeout: int
    SessionPinningFilters: List[str]
    InitQuery: str


class CopyDBClusterParameterGroupResultTypeDef(TypedDict, total=False):
    DBClusterParameterGroup: "DBClusterParameterGroupTypeDef"


class CopyDBClusterSnapshotResultTypeDef(TypedDict, total=False):
    DBClusterSnapshot: "DBClusterSnapshotTypeDef"


class CopyDBParameterGroupResultTypeDef(TypedDict, total=False):
    DBParameterGroup: "DBParameterGroupTypeDef"


class CopyDBSnapshotResultTypeDef(TypedDict, total=False):
    DBSnapshot: "DBSnapshotTypeDef"


class CopyOptionGroupResultTypeDef(TypedDict, total=False):
    OptionGroup: "OptionGroupTypeDef"


class CreateCustomAvailabilityZoneResultTypeDef(TypedDict, total=False):
    CustomAvailabilityZone: "CustomAvailabilityZoneTypeDef"


class CreateDBClusterParameterGroupResultTypeDef(TypedDict, total=False):
    DBClusterParameterGroup: "DBClusterParameterGroupTypeDef"


class CreateDBClusterResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class CreateDBClusterSnapshotResultTypeDef(TypedDict, total=False):
    DBClusterSnapshot: "DBClusterSnapshotTypeDef"


class CreateDBInstanceReadReplicaResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class CreateDBInstanceResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class CreateDBParameterGroupResultTypeDef(TypedDict, total=False):
    DBParameterGroup: "DBParameterGroupTypeDef"


class CreateDBProxyEndpointResponseTypeDef(TypedDict, total=False):
    DBProxyEndpoint: "DBProxyEndpointTypeDef"


class CreateDBProxyResponseTypeDef(TypedDict, total=False):
    DBProxy: "DBProxyTypeDef"


class CreateDBSecurityGroupResultTypeDef(TypedDict, total=False):
    DBSecurityGroup: "DBSecurityGroupTypeDef"


class CreateDBSnapshotResultTypeDef(TypedDict, total=False):
    DBSnapshot: "DBSnapshotTypeDef"


class CreateDBSubnetGroupResultTypeDef(TypedDict, total=False):
    DBSubnetGroup: "DBSubnetGroupTypeDef"


class CreateEventSubscriptionResultTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class CreateGlobalClusterResultTypeDef(TypedDict, total=False):
    GlobalCluster: "GlobalClusterTypeDef"


class CreateOptionGroupResultTypeDef(TypedDict, total=False):
    OptionGroup: "OptionGroupTypeDef"


class CustomAvailabilityZoneMessageTypeDef(TypedDict, total=False):
    Marker: str
    CustomAvailabilityZones: List["CustomAvailabilityZoneTypeDef"]


class CustomAvailabilityZoneTypeDef(TypedDict, total=False):
    CustomAvailabilityZoneId: str
    CustomAvailabilityZoneName: str
    CustomAvailabilityZoneStatus: str
    VpnDetails: "VpnDetailsTypeDef"


class DBClusterBacktrackMessageTypeDef(TypedDict, total=False):
    Marker: str
    DBClusterBacktracks: List["DBClusterBacktrackTypeDef"]


class DBClusterBacktrackTypeDef(TypedDict, total=False):
    DBClusterIdentifier: str
    BacktrackIdentifier: str
    BacktrackTo: datetime
    BacktrackedFrom: datetime
    BacktrackRequestCreationTime: datetime
    Status: str


class DBClusterCapacityInfoTypeDef(TypedDict, total=False):
    DBClusterIdentifier: str
    PendingCapacity: int
    CurrentCapacity: int
    SecondsBeforeTimeout: int
    TimeoutAction: str


class DBClusterEndpointMessageTypeDef(TypedDict, total=False):
    Marker: str
    DBClusterEndpoints: List["DBClusterEndpointTypeDef"]


class DBClusterEndpointTypeDef(TypedDict, total=False):
    DBClusterEndpointIdentifier: str
    DBClusterIdentifier: str
    DBClusterEndpointResourceIdentifier: str
    Endpoint: str
    Status: str
    EndpointType: str
    CustomEndpointType: str
    StaticMembers: List[str]
    ExcludedMembers: List[str]
    DBClusterEndpointArn: str


class DBClusterMemberTypeDef(TypedDict, total=False):
    DBInstanceIdentifier: str
    IsClusterWriter: bool
    DBClusterParameterGroupStatus: str
    PromotionTier: int


class DBClusterMessageTypeDef(TypedDict, total=False):
    Marker: str
    DBClusters: List["DBClusterTypeDef"]


class DBClusterOptionGroupStatusTypeDef(TypedDict, total=False):
    DBClusterOptionGroupName: str
    Status: str


class DBClusterParameterGroupDetailsTypeDef(TypedDict, total=False):
    Parameters: List["ParameterTypeDef"]
    Marker: str


class DBClusterParameterGroupNameMessageTypeDef(TypedDict, total=False):
    DBClusterParameterGroupName: str


class DBClusterParameterGroupTypeDef(TypedDict, total=False):
    DBClusterParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    DBClusterParameterGroupArn: str


class DBClusterParameterGroupsMessageTypeDef(TypedDict, total=False):
    Marker: str
    DBClusterParameterGroups: List["DBClusterParameterGroupTypeDef"]


class DBClusterRoleTypeDef(TypedDict, total=False):
    RoleArn: str
    Status: str
    FeatureName: str


class DBClusterSnapshotAttributeTypeDef(TypedDict, total=False):
    AttributeName: str
    AttributeValues: List[str]


class DBClusterSnapshotAttributesResultTypeDef(TypedDict, total=False):
    DBClusterSnapshotIdentifier: str
    DBClusterSnapshotAttributes: List["DBClusterSnapshotAttributeTypeDef"]


class DBClusterSnapshotMessageTypeDef(TypedDict, total=False):
    Marker: str
    DBClusterSnapshots: List["DBClusterSnapshotTypeDef"]


class DBClusterSnapshotTypeDef(TypedDict, total=False):
    AvailabilityZones: List[str]
    DBClusterSnapshotIdentifier: str
    DBClusterIdentifier: str
    SnapshotCreateTime: datetime
    Engine: str
    EngineMode: str
    AllocatedStorage: int
    Status: str
    Port: int
    VpcId: str
    ClusterCreateTime: datetime
    MasterUsername: str
    EngineVersion: str
    LicenseModel: str
    SnapshotType: str
    PercentProgress: int
    StorageEncrypted: bool
    KmsKeyId: str
    DBClusterSnapshotArn: str
    SourceDBClusterSnapshotArn: str
    IAMDatabaseAuthenticationEnabled: bool
    TagList: List["TagTypeDef"]


class DBClusterTypeDef(TypedDict, total=False):
    AllocatedStorage: int
    AvailabilityZones: List[str]
    BackupRetentionPeriod: int
    CharacterSetName: str
    DatabaseName: str
    DBClusterIdentifier: str
    DBClusterParameterGroup: str
    DBSubnetGroup: str
    Status: str
    PercentProgress: str
    EarliestRestorableTime: datetime
    Endpoint: str
    ReaderEndpoint: str
    CustomEndpoints: List[str]
    MultiAZ: bool
    Engine: str
    EngineVersion: str
    LatestRestorableTime: datetime
    Port: int
    MasterUsername: str
    DBClusterOptionGroupMemberships: List["DBClusterOptionGroupStatusTypeDef"]
    PreferredBackupWindow: str
    PreferredMaintenanceWindow: str
    ReplicationSourceIdentifier: str
    ReadReplicaIdentifiers: List[str]
    DBClusterMembers: List["DBClusterMemberTypeDef"]
    VpcSecurityGroups: List["VpcSecurityGroupMembershipTypeDef"]
    HostedZoneId: str
    StorageEncrypted: bool
    KmsKeyId: str
    DbClusterResourceId: str
    DBClusterArn: str
    AssociatedRoles: List["DBClusterRoleTypeDef"]
    IAMDatabaseAuthenticationEnabled: bool
    CloneGroupId: str
    ClusterCreateTime: datetime
    EarliestBacktrackTime: datetime
    BacktrackWindow: int
    BacktrackConsumedChangeRecords: int
    EnabledCloudwatchLogsExports: List[str]
    Capacity: int
    EngineMode: str
    ScalingConfigurationInfo: "ScalingConfigurationInfoTypeDef"
    DeletionProtection: bool
    HttpEndpointEnabled: bool
    ActivityStreamMode: ActivityStreamMode
    ActivityStreamStatus: ActivityStreamStatus
    ActivityStreamKmsKeyId: str
    ActivityStreamKinesisStreamName: str
    CopyTagsToSnapshot: bool
    CrossAccountClone: bool
    DomainMemberships: List["DomainMembershipTypeDef"]
    TagList: List["TagTypeDef"]
    GlobalWriteForwardingStatus: WriteForwardingStatus
    GlobalWriteForwardingRequested: bool
    PendingModifiedValues: "ClusterPendingModifiedValuesTypeDef"


class DBEngineVersionMessageTypeDef(TypedDict, total=False):
    Marker: str
    DBEngineVersions: List["DBEngineVersionTypeDef"]


class DBEngineVersionTypeDef(TypedDict, total=False):
    Engine: str
    EngineVersion: str
    DBParameterGroupFamily: str
    DBEngineDescription: str
    DBEngineVersionDescription: str
    DefaultCharacterSet: "CharacterSetTypeDef"
    SupportedCharacterSets: List["CharacterSetTypeDef"]
    SupportedNcharCharacterSets: List["CharacterSetTypeDef"]
    ValidUpgradeTarget: List["UpgradeTargetTypeDef"]
    SupportedTimezones: List["TimezoneTypeDef"]
    ExportableLogTypes: List[str]
    SupportsLogExportsToCloudwatchLogs: bool
    SupportsReadReplica: bool
    SupportedEngineModes: List[str]
    SupportedFeatureNames: List[str]
    Status: str
    SupportsParallelQuery: bool
    SupportsGlobalDatabases: bool


class DBInstanceAutomatedBackupMessageTypeDef(TypedDict, total=False):
    Marker: str
    DBInstanceAutomatedBackups: List["DBInstanceAutomatedBackupTypeDef"]


class DBInstanceAutomatedBackupTypeDef(TypedDict, total=False):
    DBInstanceArn: str
    DbiResourceId: str
    Region: str
    DBInstanceIdentifier: str
    RestoreWindow: "RestoreWindowTypeDef"
    AllocatedStorage: int
    Status: str
    Port: int
    AvailabilityZone: str
    VpcId: str
    InstanceCreateTime: datetime
    MasterUsername: str
    Engine: str
    EngineVersion: str
    LicenseModel: str
    Iops: int
    OptionGroupName: str
    TdeCredentialArn: str
    Encrypted: bool
    StorageType: str
    KmsKeyId: str
    Timezone: str
    IAMDatabaseAuthenticationEnabled: bool
    BackupRetentionPeriod: int
    DBInstanceAutomatedBackupsArn: str
    DBInstanceAutomatedBackupsReplications: List["DBInstanceAutomatedBackupsReplicationTypeDef"]


class DBInstanceAutomatedBackupsReplicationTypeDef(TypedDict, total=False):
    DBInstanceAutomatedBackupsArn: str


class DBInstanceMessageTypeDef(TypedDict, total=False):
    Marker: str
    DBInstances: List["DBInstanceTypeDef"]


class DBInstanceRoleTypeDef(TypedDict, total=False):
    RoleArn: str
    FeatureName: str
    Status: str


class DBInstanceStatusInfoTypeDef(TypedDict, total=False):
    StatusType: str
    Normal: bool
    Status: str
    Message: str


class DBInstanceTypeDef(TypedDict, total=False):
    DBInstanceIdentifier: str
    DBInstanceClass: str
    Engine: str
    DBInstanceStatus: str
    MasterUsername: str
    DBName: str
    Endpoint: "EndpointTypeDef"
    AllocatedStorage: int
    InstanceCreateTime: datetime
    PreferredBackupWindow: str
    BackupRetentionPeriod: int
    DBSecurityGroups: List["DBSecurityGroupMembershipTypeDef"]
    VpcSecurityGroups: List["VpcSecurityGroupMembershipTypeDef"]
    DBParameterGroups: List["DBParameterGroupStatusTypeDef"]
    AvailabilityZone: str
    DBSubnetGroup: "DBSubnetGroupTypeDef"
    PreferredMaintenanceWindow: str
    PendingModifiedValues: "PendingModifiedValuesTypeDef"
    LatestRestorableTime: datetime
    MultiAZ: bool
    EngineVersion: str
    AutoMinorVersionUpgrade: bool
    ReadReplicaSourceDBInstanceIdentifier: str
    ReadReplicaDBInstanceIdentifiers: List[str]
    ReadReplicaDBClusterIdentifiers: List[str]
    ReplicaMode: ReplicaMode
    LicenseModel: str
    Iops: int
    OptionGroupMemberships: List["OptionGroupMembershipTypeDef"]
    CharacterSetName: str
    NcharCharacterSetName: str
    SecondaryAvailabilityZone: str
    PubliclyAccessible: bool
    StatusInfos: List["DBInstanceStatusInfoTypeDef"]
    StorageType: str
    TdeCredentialArn: str
    DbInstancePort: int
    DBClusterIdentifier: str
    StorageEncrypted: bool
    KmsKeyId: str
    DbiResourceId: str
    CACertificateIdentifier: str
    DomainMemberships: List["DomainMembershipTypeDef"]
    CopyTagsToSnapshot: bool
    MonitoringInterval: int
    EnhancedMonitoringResourceArn: str
    MonitoringRoleArn: str
    PromotionTier: int
    DBInstanceArn: str
    Timezone: str
    IAMDatabaseAuthenticationEnabled: bool
    PerformanceInsightsEnabled: bool
    PerformanceInsightsKMSKeyId: str
    PerformanceInsightsRetentionPeriod: int
    EnabledCloudwatchLogsExports: List[str]
    ProcessorFeatures: List["ProcessorFeatureTypeDef"]
    DeletionProtection: bool
    AssociatedRoles: List["DBInstanceRoleTypeDef"]
    ListenerEndpoint: "EndpointTypeDef"
    MaxAllocatedStorage: int
    TagList: List["TagTypeDef"]
    DBInstanceAutomatedBackupsReplications: List["DBInstanceAutomatedBackupsReplicationTypeDef"]
    CustomerOwnedIpEnabled: bool
    AwsBackupRecoveryPointArn: str


class DBParameterGroupDetailsTypeDef(TypedDict, total=False):
    Parameters: List["ParameterTypeDef"]
    Marker: str


class DBParameterGroupNameMessageTypeDef(TypedDict, total=False):
    DBParameterGroupName: str


class DBParameterGroupStatusTypeDef(TypedDict, total=False):
    DBParameterGroupName: str
    ParameterApplyStatus: str


class DBParameterGroupTypeDef(TypedDict, total=False):
    DBParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    DBParameterGroupArn: str


class DBParameterGroupsMessageTypeDef(TypedDict, total=False):
    Marker: str
    DBParameterGroups: List["DBParameterGroupTypeDef"]


class DBProxyEndpointTypeDef(TypedDict, total=False):
    DBProxyEndpointName: str
    DBProxyEndpointArn: str
    DBProxyName: str
    Status: DBProxyEndpointStatus
    VpcId: str
    VpcSecurityGroupIds: List[str]
    VpcSubnetIds: List[str]
    Endpoint: str
    CreatedDate: datetime
    TargetRole: DBProxyEndpointTargetRole
    IsDefault: bool


class DBProxyTargetGroupTypeDef(TypedDict, total=False):
    DBProxyName: str
    TargetGroupName: str
    TargetGroupArn: str
    IsDefault: bool
    Status: str
    ConnectionPoolConfig: "ConnectionPoolConfigurationInfoTypeDef"
    CreatedDate: datetime
    UpdatedDate: datetime


DBProxyTargetTypeDef = TypedDict(
    "DBProxyTargetTypeDef",
    {
        "TargetArn": str,
        "Endpoint": str,
        "TrackedClusterId": str,
        "RdsResourceId": str,
        "Port": int,
        "Type": TargetType,
        "Role": TargetRole,
        "TargetHealth": "TargetHealthTypeDef",
    },
    total=False,
)


class DBProxyTypeDef(TypedDict, total=False):
    DBProxyName: str
    DBProxyArn: str
    Status: DBProxyStatus
    EngineFamily: str
    VpcId: str
    VpcSecurityGroupIds: List[str]
    VpcSubnetIds: List[str]
    Auth: List["UserAuthConfigInfoTypeDef"]
    RoleArn: str
    Endpoint: str
    RequireTLS: bool
    IdleClientTimeout: int
    DebugLogging: bool
    CreatedDate: datetime
    UpdatedDate: datetime


class DBSecurityGroupMembershipTypeDef(TypedDict, total=False):
    DBSecurityGroupName: str
    Status: str


class DBSecurityGroupMessageTypeDef(TypedDict, total=False):
    Marker: str
    DBSecurityGroups: List["DBSecurityGroupTypeDef"]


class DBSecurityGroupTypeDef(TypedDict, total=False):
    OwnerId: str
    DBSecurityGroupName: str
    DBSecurityGroupDescription: str
    VpcId: str
    EC2SecurityGroups: List["EC2SecurityGroupTypeDef"]
    IPRanges: List["IPRangeTypeDef"]
    DBSecurityGroupArn: str


class DBSnapshotAttributeTypeDef(TypedDict, total=False):
    AttributeName: str
    AttributeValues: List[str]


class DBSnapshotAttributesResultTypeDef(TypedDict, total=False):
    DBSnapshotIdentifier: str
    DBSnapshotAttributes: List["DBSnapshotAttributeTypeDef"]


class DBSnapshotMessageTypeDef(TypedDict, total=False):
    Marker: str
    DBSnapshots: List["DBSnapshotTypeDef"]


class DBSnapshotTypeDef(TypedDict, total=False):
    DBSnapshotIdentifier: str
    DBInstanceIdentifier: str
    SnapshotCreateTime: datetime
    Engine: str
    AllocatedStorage: int
    Status: str
    Port: int
    AvailabilityZone: str
    VpcId: str
    InstanceCreateTime: datetime
    MasterUsername: str
    EngineVersion: str
    LicenseModel: str
    SnapshotType: str
    Iops: int
    OptionGroupName: str
    PercentProgress: int
    SourceRegion: str
    SourceDBSnapshotIdentifier: str
    StorageType: str
    TdeCredentialArn: str
    Encrypted: bool
    KmsKeyId: str
    DBSnapshotArn: str
    Timezone: str
    IAMDatabaseAuthenticationEnabled: bool
    ProcessorFeatures: List["ProcessorFeatureTypeDef"]
    DbiResourceId: str
    TagList: List["TagTypeDef"]


class DBSubnetGroupMessageTypeDef(TypedDict, total=False):
    Marker: str
    DBSubnetGroups: List["DBSubnetGroupTypeDef"]


class DBSubnetGroupTypeDef(TypedDict, total=False):
    DBSubnetGroupName: str
    DBSubnetGroupDescription: str
    VpcId: str
    SubnetGroupStatus: str
    Subnets: List["SubnetTypeDef"]
    DBSubnetGroupArn: str


class DeleteCustomAvailabilityZoneResultTypeDef(TypedDict, total=False):
    CustomAvailabilityZone: "CustomAvailabilityZoneTypeDef"


class DeleteDBClusterResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class DeleteDBClusterSnapshotResultTypeDef(TypedDict, total=False):
    DBClusterSnapshot: "DBClusterSnapshotTypeDef"


class DeleteDBInstanceAutomatedBackupResultTypeDef(TypedDict, total=False):
    DBInstanceAutomatedBackup: "DBInstanceAutomatedBackupTypeDef"


class DeleteDBInstanceResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class DeleteDBProxyEndpointResponseTypeDef(TypedDict, total=False):
    DBProxyEndpoint: "DBProxyEndpointTypeDef"


class DeleteDBProxyResponseTypeDef(TypedDict, total=False):
    DBProxy: "DBProxyTypeDef"


class DeleteDBSnapshotResultTypeDef(TypedDict, total=False):
    DBSnapshot: "DBSnapshotTypeDef"


class DeleteEventSubscriptionResultTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class DeleteGlobalClusterResultTypeDef(TypedDict, total=False):
    GlobalCluster: "GlobalClusterTypeDef"


class DescribeDBClusterSnapshotAttributesResultTypeDef(TypedDict, total=False):
    DBClusterSnapshotAttributesResult: "DBClusterSnapshotAttributesResultTypeDef"


class DescribeDBLogFilesDetailsTypeDef(TypedDict, total=False):
    LogFileName: str
    LastWritten: int
    Size: int


class DescribeDBLogFilesResponseTypeDef(TypedDict, total=False):
    DescribeDBLogFiles: List["DescribeDBLogFilesDetailsTypeDef"]
    Marker: str


class DescribeDBProxiesResponseTypeDef(TypedDict, total=False):
    DBProxies: List["DBProxyTypeDef"]
    Marker: str


class DescribeDBProxyEndpointsResponseTypeDef(TypedDict, total=False):
    DBProxyEndpoints: List["DBProxyEndpointTypeDef"]
    Marker: str


class DescribeDBProxyTargetGroupsResponseTypeDef(TypedDict, total=False):
    TargetGroups: List["DBProxyTargetGroupTypeDef"]
    Marker: str


class DescribeDBProxyTargetsResponseTypeDef(TypedDict, total=False):
    Targets: List["DBProxyTargetTypeDef"]
    Marker: str


class DescribeDBSnapshotAttributesResultTypeDef(TypedDict, total=False):
    DBSnapshotAttributesResult: "DBSnapshotAttributesResultTypeDef"


class DescribeEngineDefaultClusterParametersResultTypeDef(TypedDict, total=False):
    EngineDefaults: "EngineDefaultsTypeDef"


class DescribeEngineDefaultParametersResultTypeDef(TypedDict, total=False):
    EngineDefaults: "EngineDefaultsTypeDef"


class DescribeValidDBInstanceModificationsResultTypeDef(TypedDict, total=False):
    ValidDBInstanceModificationsMessage: "ValidDBInstanceModificationsMessageTypeDef"


class DomainMembershipTypeDef(TypedDict, total=False):
    Domain: str
    Status: str
    FQDN: str
    IAMRoleName: str


class DoubleRangeTypeDef(TypedDict, total=False):
    From: float
    To: float


class DownloadDBLogFilePortionDetailsTypeDef(TypedDict, total=False):
    LogFileData: str
    Marker: str
    AdditionalDataPending: bool


class EC2SecurityGroupTypeDef(TypedDict, total=False):
    Status: str
    EC2SecurityGroupName: str
    EC2SecurityGroupId: str
    EC2SecurityGroupOwnerId: str


class EndpointTypeDef(TypedDict, total=False):
    Address: str
    Port: int
    HostedZoneId: str


class EngineDefaultsTypeDef(TypedDict, total=False):
    DBParameterGroupFamily: str
    Marker: str
    Parameters: List["ParameterTypeDef"]


class EventCategoriesMapTypeDef(TypedDict, total=False):
    SourceType: str
    EventCategories: List[str]


class EventCategoriesMessageTypeDef(TypedDict, total=False):
    EventCategoriesMapList: List["EventCategoriesMapTypeDef"]


class EventSubscriptionTypeDef(TypedDict, total=False):
    CustomerAwsId: str
    CustSubscriptionId: str
    SnsTopicArn: str
    Status: str
    SubscriptionCreationTime: str
    SourceType: str
    SourceIdsList: List[str]
    EventCategoriesList: List[str]
    Enabled: bool
    EventSubscriptionArn: str


class EventSubscriptionsMessageTypeDef(TypedDict, total=False):
    Marker: str
    EventSubscriptionsList: List["EventSubscriptionTypeDef"]


class EventTypeDef(TypedDict, total=False):
    SourceIdentifier: str
    SourceType: SourceType
    Message: str
    EventCategories: List[str]
    Date: datetime
    SourceArn: str


class EventsMessageTypeDef(TypedDict, total=False):
    Marker: str
    Events: List["EventTypeDef"]


class ExportTaskTypeDef(TypedDict, total=False):
    ExportTaskIdentifier: str
    SourceArn: str
    ExportOnly: List[str]
    SnapshotTime: datetime
    TaskStartTime: datetime
    TaskEndTime: datetime
    S3Bucket: str
    S3Prefix: str
    IamRoleArn: str
    KmsKeyId: str
    Status: str
    PercentProgress: int
    TotalExtractedDataInGB: int
    FailureCause: str
    WarningMessage: str


class ExportTasksMessageTypeDef(TypedDict, total=False):
    Marker: str
    ExportTasks: List["ExportTaskTypeDef"]


class FailoverDBClusterResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class FailoverGlobalClusterResultTypeDef(TypedDict, total=False):
    GlobalCluster: "GlobalClusterTypeDef"


class FailoverStateTypeDef(TypedDict, total=False):
    Status: FailoverStatus
    FromDbClusterArn: str
    ToDbClusterArn: str


class FilterTypeDef(TypedDict):
    Name: str
    Values: List[str]


class GlobalClusterMemberTypeDef(TypedDict, total=False):
    DBClusterArn: str
    Readers: List[str]
    IsWriter: bool
    GlobalWriteForwardingStatus: WriteForwardingStatus


class GlobalClusterTypeDef(TypedDict, total=False):
    GlobalClusterIdentifier: str
    GlobalClusterResourceId: str
    GlobalClusterArn: str
    Status: str
    Engine: str
    EngineVersion: str
    DatabaseName: str
    StorageEncrypted: bool
    DeletionProtection: bool
    GlobalClusterMembers: List["GlobalClusterMemberTypeDef"]
    FailoverState: "FailoverStateTypeDef"


class GlobalClustersMessageTypeDef(TypedDict, total=False):
    Marker: str
    GlobalClusters: List["GlobalClusterTypeDef"]


class IPRangeTypeDef(TypedDict, total=False):
    Status: str
    CIDRIP: str


class InstallationMediaFailureCauseTypeDef(TypedDict, total=False):
    Message: str


class InstallationMediaMessageTypeDef(TypedDict, total=False):
    Marker: str
    InstallationMedia: List["InstallationMediaTypeDef"]


class InstallationMediaTypeDef(TypedDict, total=False):
    InstallationMediaId: str
    CustomAvailabilityZoneId: str
    Engine: str
    EngineVersion: str
    EngineInstallationMediaPath: str
    OSInstallationMediaPath: str
    Status: str
    FailureCause: "InstallationMediaFailureCauseTypeDef"


class MinimumEngineVersionPerAllowedValueTypeDef(TypedDict, total=False):
    AllowedValue: str
    MinimumEngineVersion: str


class ModifyCertificatesResultTypeDef(TypedDict, total=False):
    Certificate: "CertificateTypeDef"


class ModifyDBClusterResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class ModifyDBClusterSnapshotAttributeResultTypeDef(TypedDict, total=False):
    DBClusterSnapshotAttributesResult: "DBClusterSnapshotAttributesResultTypeDef"


class ModifyDBInstanceResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class ModifyDBProxyEndpointResponseTypeDef(TypedDict, total=False):
    DBProxyEndpoint: "DBProxyEndpointTypeDef"


class ModifyDBProxyResponseTypeDef(TypedDict, total=False):
    DBProxy: "DBProxyTypeDef"


class ModifyDBProxyTargetGroupResponseTypeDef(TypedDict, total=False):
    DBProxyTargetGroup: "DBProxyTargetGroupTypeDef"


class ModifyDBSnapshotAttributeResultTypeDef(TypedDict, total=False):
    DBSnapshotAttributesResult: "DBSnapshotAttributesResultTypeDef"


class ModifyDBSnapshotResultTypeDef(TypedDict, total=False):
    DBSnapshot: "DBSnapshotTypeDef"


class ModifyDBSubnetGroupResultTypeDef(TypedDict, total=False):
    DBSubnetGroup: "DBSubnetGroupTypeDef"


class ModifyEventSubscriptionResultTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class ModifyGlobalClusterResultTypeDef(TypedDict, total=False):
    GlobalCluster: "GlobalClusterTypeDef"


class ModifyOptionGroupResultTypeDef(TypedDict, total=False):
    OptionGroup: "OptionGroupTypeDef"


class _RequiredOptionConfigurationTypeDef(TypedDict):
    OptionName: str


class OptionConfigurationTypeDef(_RequiredOptionConfigurationTypeDef, total=False):
    Port: int
    OptionVersion: str
    DBSecurityGroupMemberships: List[str]
    VpcSecurityGroupMemberships: List[str]
    OptionSettings: List["OptionSettingTypeDef"]


class OptionGroupMembershipTypeDef(TypedDict, total=False):
    OptionGroupName: str
    Status: str


class OptionGroupOptionSettingTypeDef(TypedDict, total=False):
    SettingName: str
    SettingDescription: str
    DefaultValue: str
    ApplyType: str
    AllowedValues: str
    IsModifiable: bool
    IsRequired: bool
    MinimumEngineVersionPerAllowedValue: List["MinimumEngineVersionPerAllowedValueTypeDef"]


class OptionGroupOptionTypeDef(TypedDict, total=False):
    Name: str
    Description: str
    EngineName: str
    MajorEngineVersion: str
    MinimumRequiredMinorEngineVersion: str
    PortRequired: bool
    DefaultPort: int
    OptionsDependedOn: List[str]
    OptionsConflictsWith: List[str]
    Persistent: bool
    Permanent: bool
    RequiresAutoMinorEngineVersionUpgrade: bool
    VpcOnly: bool
    SupportsOptionVersionDowngrade: bool
    OptionGroupOptionSettings: List["OptionGroupOptionSettingTypeDef"]
    OptionGroupOptionVersions: List["OptionVersionTypeDef"]


class OptionGroupOptionsMessageTypeDef(TypedDict, total=False):
    OptionGroupOptions: List["OptionGroupOptionTypeDef"]
    Marker: str


class OptionGroupTypeDef(TypedDict, total=False):
    OptionGroupName: str
    OptionGroupDescription: str
    EngineName: str
    MajorEngineVersion: str
    Options: List["OptionTypeDef"]
    AllowsVpcAndNonVpcInstanceMemberships: bool
    VpcId: str
    OptionGroupArn: str


class OptionGroupsTypeDef(TypedDict, total=False):
    OptionGroupsList: List["OptionGroupTypeDef"]
    Marker: str


class OptionSettingTypeDef(TypedDict, total=False):
    Name: str
    Value: str
    DefaultValue: str
    Description: str
    ApplyType: str
    DataType: str
    AllowedValues: str
    IsModifiable: bool
    IsCollection: bool


class OptionTypeDef(TypedDict, total=False):
    OptionName: str
    OptionDescription: str
    Persistent: bool
    Permanent: bool
    Port: int
    OptionVersion: str
    OptionSettings: List["OptionSettingTypeDef"]
    DBSecurityGroupMemberships: List["DBSecurityGroupMembershipTypeDef"]
    VpcSecurityGroupMemberships: List["VpcSecurityGroupMembershipTypeDef"]


class OptionVersionTypeDef(TypedDict, total=False):
    Version: str
    IsDefault: bool


class OrderableDBInstanceOptionTypeDef(TypedDict, total=False):
    Engine: str
    EngineVersion: str
    DBInstanceClass: str
    LicenseModel: str
    AvailabilityZoneGroup: str
    AvailabilityZones: List["AvailabilityZoneTypeDef"]
    MultiAZCapable: bool
    ReadReplicaCapable: bool
    Vpc: bool
    SupportsStorageEncryption: bool
    StorageType: str
    SupportsIops: bool
    SupportsEnhancedMonitoring: bool
    SupportsIAMDatabaseAuthentication: bool
    SupportsPerformanceInsights: bool
    MinStorageSize: int
    MaxStorageSize: int
    MinIopsPerDbInstance: int
    MaxIopsPerDbInstance: int
    MinIopsPerGib: float
    MaxIopsPerGib: float
    AvailableProcessorFeatures: List["AvailableProcessorFeatureTypeDef"]
    SupportedEngineModes: List[str]
    SupportsStorageAutoscaling: bool
    SupportsKerberosAuthentication: bool
    OutpostCapable: bool
    SupportsGlobalDatabases: bool


class OrderableDBInstanceOptionsMessageTypeDef(TypedDict, total=False):
    OrderableDBInstanceOptions: List["OrderableDBInstanceOptionTypeDef"]
    Marker: str


class OutpostTypeDef(TypedDict, total=False):
    Arn: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParameterTypeDef(TypedDict, total=False):
    ParameterName: str
    ParameterValue: str
    Description: str
    Source: str
    ApplyType: str
    DataType: str
    AllowedValues: str
    IsModifiable: bool
    MinimumEngineVersion: str
    ApplyMethod: ApplyMethod
    SupportedEngineModes: List[str]


class PendingCloudwatchLogsExportsTypeDef(TypedDict, total=False):
    LogTypesToEnable: List[str]
    LogTypesToDisable: List[str]


class PendingMaintenanceActionTypeDef(TypedDict, total=False):
    Action: str
    AutoAppliedAfterDate: datetime
    ForcedApplyDate: datetime
    OptInStatus: str
    CurrentApplyDate: datetime
    Description: str


class PendingMaintenanceActionsMessageTypeDef(TypedDict, total=False):
    PendingMaintenanceActions: List["ResourcePendingMaintenanceActionsTypeDef"]
    Marker: str


class PendingModifiedValuesTypeDef(TypedDict, total=False):
    DBInstanceClass: str
    AllocatedStorage: int
    MasterUserPassword: str
    Port: int
    BackupRetentionPeriod: int
    MultiAZ: bool
    EngineVersion: str
    LicenseModel: str
    Iops: int
    DBInstanceIdentifier: str
    StorageType: str
    CACertificateIdentifier: str
    DBSubnetGroupName: str
    PendingCloudwatchLogsExports: "PendingCloudwatchLogsExportsTypeDef"
    ProcessorFeatures: List["ProcessorFeatureTypeDef"]
    IAMDatabaseAuthenticationEnabled: bool


class ProcessorFeatureTypeDef(TypedDict, total=False):
    Name: str
    Value: str


class PromoteReadReplicaDBClusterResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class PromoteReadReplicaResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class PurchaseReservedDBInstancesOfferingResultTypeDef(TypedDict, total=False):
    ReservedDBInstance: "ReservedDBInstanceTypeDef"


class RangeTypeDef(TypedDict, total=False):
    From: int
    To: int
    Step: int


class RebootDBInstanceResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class RecurringChargeTypeDef(TypedDict, total=False):
    RecurringChargeAmount: float
    RecurringChargeFrequency: str


class RegisterDBProxyTargetsResponseTypeDef(TypedDict, total=False):
    DBProxyTargets: List["DBProxyTargetTypeDef"]


class RemoveFromGlobalClusterResultTypeDef(TypedDict, total=False):
    GlobalCluster: "GlobalClusterTypeDef"


class RemoveSourceIdentifierFromSubscriptionResultTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class ReservedDBInstanceMessageTypeDef(TypedDict, total=False):
    Marker: str
    ReservedDBInstances: List["ReservedDBInstanceTypeDef"]


class ReservedDBInstanceTypeDef(TypedDict, total=False):
    ReservedDBInstanceId: str
    ReservedDBInstancesOfferingId: str
    DBInstanceClass: str
    StartTime: datetime
    Duration: int
    FixedPrice: float
    UsagePrice: float
    CurrencyCode: str
    DBInstanceCount: int
    ProductDescription: str
    OfferingType: str
    MultiAZ: bool
    State: str
    RecurringCharges: List["RecurringChargeTypeDef"]
    ReservedDBInstanceArn: str
    LeaseId: str


class ReservedDBInstancesOfferingMessageTypeDef(TypedDict, total=False):
    Marker: str
    ReservedDBInstancesOfferings: List["ReservedDBInstancesOfferingTypeDef"]


class ReservedDBInstancesOfferingTypeDef(TypedDict, total=False):
    ReservedDBInstancesOfferingId: str
    DBInstanceClass: str
    Duration: int
    FixedPrice: float
    UsagePrice: float
    CurrencyCode: str
    ProductDescription: str
    OfferingType: str
    MultiAZ: bool
    RecurringCharges: List["RecurringChargeTypeDef"]


class ResourcePendingMaintenanceActionsTypeDef(TypedDict, total=False):
    ResourceIdentifier: str
    PendingMaintenanceActionDetails: List["PendingMaintenanceActionTypeDef"]


class RestoreDBClusterFromS3ResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class RestoreDBClusterFromSnapshotResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class RestoreDBClusterToPointInTimeResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class RestoreDBInstanceFromDBSnapshotResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class RestoreDBInstanceFromS3ResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class RestoreDBInstanceToPointInTimeResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class RestoreWindowTypeDef(TypedDict, total=False):
    EarliestTime: datetime
    LatestTime: datetime


class RevokeDBSecurityGroupIngressResultTypeDef(TypedDict, total=False):
    DBSecurityGroup: "DBSecurityGroupTypeDef"


class ScalingConfigurationInfoTypeDef(TypedDict, total=False):
    MinCapacity: int
    MaxCapacity: int
    AutoPause: bool
    SecondsUntilAutoPause: int
    TimeoutAction: str


class ScalingConfigurationTypeDef(TypedDict, total=False):
    MinCapacity: int
    MaxCapacity: int
    AutoPause: bool
    SecondsUntilAutoPause: int
    TimeoutAction: str


class SourceRegionMessageTypeDef(TypedDict, total=False):
    Marker: str
    SourceRegions: List["SourceRegionTypeDef"]


class SourceRegionTypeDef(TypedDict, total=False):
    RegionName: str
    Endpoint: str
    Status: str
    SupportsDBInstanceAutomatedBackupsReplication: bool


class StartActivityStreamResponseTypeDef(TypedDict, total=False):
    KmsKeyId: str
    KinesisStreamName: str
    Status: ActivityStreamStatus
    Mode: ActivityStreamMode
    ApplyImmediately: bool


class StartDBClusterResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class StartDBInstanceAutomatedBackupsReplicationResultTypeDef(TypedDict, total=False):
    DBInstanceAutomatedBackup: "DBInstanceAutomatedBackupTypeDef"


class StartDBInstanceResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class StopActivityStreamResponseTypeDef(TypedDict, total=False):
    KmsKeyId: str
    KinesisStreamName: str
    Status: ActivityStreamStatus


class StopDBClusterResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class StopDBInstanceAutomatedBackupsReplicationResultTypeDef(TypedDict, total=False):
    DBInstanceAutomatedBackup: "DBInstanceAutomatedBackupTypeDef"


class StopDBInstanceResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class SubnetTypeDef(TypedDict, total=False):
    SubnetIdentifier: str
    SubnetAvailabilityZone: "AvailabilityZoneTypeDef"
    SubnetOutpost: "OutpostTypeDef"
    SubnetStatus: str


class TagListMessageTypeDef(TypedDict, total=False):
    TagList: List["TagTypeDef"]


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class TargetHealthTypeDef(TypedDict, total=False):
    State: TargetState
    Reason: TargetHealthReason
    Description: str


class TimezoneTypeDef(TypedDict, total=False):
    TimezoneName: str


class UpgradeTargetTypeDef(TypedDict, total=False):
    Engine: str
    EngineVersion: str
    Description: str
    AutoUpgrade: bool
    IsMajorVersionUpgrade: bool
    SupportedEngineModes: List[str]
    SupportsParallelQuery: bool
    SupportsGlobalDatabases: bool


class UserAuthConfigInfoTypeDef(TypedDict, total=False):
    Description: str
    UserName: str
    AuthScheme: Literal["SECRETS"]
    SecretArn: str
    IAMAuth: IAMAuthMode


class UserAuthConfigTypeDef(TypedDict, total=False):
    Description: str
    UserName: str
    AuthScheme: Literal["SECRETS"]
    SecretArn: str
    IAMAuth: IAMAuthMode


class ValidDBInstanceModificationsMessageTypeDef(TypedDict, total=False):
    Storage: List["ValidStorageOptionsTypeDef"]
    ValidProcessorFeatures: List["AvailableProcessorFeatureTypeDef"]


class ValidStorageOptionsTypeDef(TypedDict, total=False):
    StorageType: str
    StorageSize: List["RangeTypeDef"]
    ProvisionedIops: List["RangeTypeDef"]
    IopsToStorageRatio: List["DoubleRangeTypeDef"]
    SupportsStorageAutoscaling: bool


class VpcSecurityGroupMembershipTypeDef(TypedDict, total=False):
    VpcSecurityGroupId: str
    Status: str


class VpnDetailsTypeDef(TypedDict, total=False):
    VpnId: str
    VpnTunnelOriginatorIP: str
    VpnGatewayIp: str
    VpnPSK: str
    VpnName: str
    VpnState: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
