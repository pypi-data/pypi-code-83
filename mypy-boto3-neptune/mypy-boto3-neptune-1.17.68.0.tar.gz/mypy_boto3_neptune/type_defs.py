"""
Type annotations for neptune service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_neptune/type_defs.html)

Usage::

    ```python
    from mypy_boto3_neptune.type_defs import AddSourceIdentifierToSubscriptionResultTypeDef

    data: AddSourceIdentifierToSubscriptionResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_neptune.literals import ApplyMethod, SourceType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    "ApplyPendingMaintenanceActionResultTypeDef",
    "AvailabilityZoneTypeDef",
    "CharacterSetTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "CopyDBClusterParameterGroupResultTypeDef",
    "CopyDBClusterSnapshotResultTypeDef",
    "CopyDBParameterGroupResultTypeDef",
    "CreateDBClusterEndpointOutputTypeDef",
    "CreateDBClusterParameterGroupResultTypeDef",
    "CreateDBClusterResultTypeDef",
    "CreateDBClusterSnapshotResultTypeDef",
    "CreateDBInstanceResultTypeDef",
    "CreateDBParameterGroupResultTypeDef",
    "CreateDBSubnetGroupResultTypeDef",
    "CreateEventSubscriptionResultTypeDef",
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
    "DBInstanceMessageTypeDef",
    "DBInstanceStatusInfoTypeDef",
    "DBInstanceTypeDef",
    "DBParameterGroupDetailsTypeDef",
    "DBParameterGroupNameMessageTypeDef",
    "DBParameterGroupStatusTypeDef",
    "DBParameterGroupTypeDef",
    "DBParameterGroupsMessageTypeDef",
    "DBSecurityGroupMembershipTypeDef",
    "DBSubnetGroupMessageTypeDef",
    "DBSubnetGroupTypeDef",
    "DeleteDBClusterEndpointOutputTypeDef",
    "DeleteDBClusterResultTypeDef",
    "DeleteDBClusterSnapshotResultTypeDef",
    "DeleteDBInstanceResultTypeDef",
    "DeleteEventSubscriptionResultTypeDef",
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "DescribeValidDBInstanceModificationsResultTypeDef",
    "DomainMembershipTypeDef",
    "DoubleRangeTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventCategoriesMapTypeDef",
    "EventCategoriesMessageTypeDef",
    "EventSubscriptionTypeDef",
    "EventSubscriptionsMessageTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "FailoverDBClusterResultTypeDef",
    "FilterTypeDef",
    "ModifyDBClusterEndpointOutputTypeDef",
    "ModifyDBClusterResultTypeDef",
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    "ModifyDBInstanceResultTypeDef",
    "ModifyDBSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "OptionGroupMembershipTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "PendingModifiedValuesTypeDef",
    "PromoteReadReplicaDBClusterResultTypeDef",
    "RangeTypeDef",
    "RebootDBInstanceResultTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "ResponseMetadata",
    "RestoreDBClusterFromSnapshotResultTypeDef",
    "RestoreDBClusterToPointInTimeResultTypeDef",
    "StartDBClusterResultTypeDef",
    "StopDBClusterResultTypeDef",
    "SubnetTypeDef",
    "TagListMessageTypeDef",
    "TagTypeDef",
    "TimezoneTypeDef",
    "UpgradeTargetTypeDef",
    "ValidDBInstanceModificationsMessageTypeDef",
    "ValidStorageOptionsTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)


class AddSourceIdentifierToSubscriptionResultTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class ApplyPendingMaintenanceActionResultTypeDef(TypedDict, total=False):
    ResourcePendingMaintenanceActions: "ResourcePendingMaintenanceActionsTypeDef"


class AvailabilityZoneTypeDef(TypedDict, total=False):
    Name: str


class CharacterSetTypeDef(TypedDict, total=False):
    CharacterSetName: str
    CharacterSetDescription: str


class CloudwatchLogsExportConfigurationTypeDef(TypedDict, total=False):
    EnableLogTypes: List[str]
    DisableLogTypes: List[str]


class CopyDBClusterParameterGroupResultTypeDef(TypedDict, total=False):
    DBClusterParameterGroup: "DBClusterParameterGroupTypeDef"


class CopyDBClusterSnapshotResultTypeDef(TypedDict, total=False):
    DBClusterSnapshot: "DBClusterSnapshotTypeDef"


class CopyDBParameterGroupResultTypeDef(TypedDict, total=False):
    DBParameterGroup: "DBParameterGroupTypeDef"


class CreateDBClusterEndpointOutputTypeDef(TypedDict):
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
    ResponseMetadata: "ResponseMetadata"


class CreateDBClusterParameterGroupResultTypeDef(TypedDict, total=False):
    DBClusterParameterGroup: "DBClusterParameterGroupTypeDef"


class CreateDBClusterResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class CreateDBClusterSnapshotResultTypeDef(TypedDict, total=False):
    DBClusterSnapshot: "DBClusterSnapshotTypeDef"


class CreateDBInstanceResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class CreateDBParameterGroupResultTypeDef(TypedDict, total=False):
    DBParameterGroup: "DBParameterGroupTypeDef"


class CreateDBSubnetGroupResultTypeDef(TypedDict, total=False):
    DBSubnetGroup: "DBSubnetGroupTypeDef"


class CreateEventSubscriptionResultTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


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
    EnabledCloudwatchLogsExports: List[str]
    DeletionProtection: bool


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
    ValidUpgradeTarget: List["UpgradeTargetTypeDef"]
    SupportedTimezones: List["TimezoneTypeDef"]
    ExportableLogTypes: List[str]
    SupportsLogExportsToCloudwatchLogs: bool
    SupportsReadReplica: bool


class DBInstanceMessageTypeDef(TypedDict, total=False):
    Marker: str
    DBInstances: List["DBInstanceTypeDef"]


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
    LicenseModel: str
    Iops: int
    OptionGroupMemberships: List["OptionGroupMembershipTypeDef"]
    CharacterSetName: str
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
    EnabledCloudwatchLogsExports: List[str]
    DeletionProtection: bool


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


class DBSecurityGroupMembershipTypeDef(TypedDict, total=False):
    DBSecurityGroupName: str
    Status: str


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


class DeleteDBClusterEndpointOutputTypeDef(TypedDict):
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
    ResponseMetadata: "ResponseMetadata"


class DeleteDBClusterResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class DeleteDBClusterSnapshotResultTypeDef(TypedDict, total=False):
    DBClusterSnapshot: "DBClusterSnapshotTypeDef"


class DeleteDBInstanceResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class DeleteEventSubscriptionResultTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class DescribeDBClusterSnapshotAttributesResultTypeDef(TypedDict, total=False):
    DBClusterSnapshotAttributesResult: "DBClusterSnapshotAttributesResultTypeDef"


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


class FailoverDBClusterResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class FilterTypeDef(TypedDict):
    Name: str
    Values: List[str]


class ModifyDBClusterEndpointOutputTypeDef(TypedDict):
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
    ResponseMetadata: "ResponseMetadata"


class ModifyDBClusterResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class ModifyDBClusterSnapshotAttributeResultTypeDef(TypedDict, total=False):
    DBClusterSnapshotAttributesResult: "DBClusterSnapshotAttributesResultTypeDef"


class ModifyDBInstanceResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class ModifyDBSubnetGroupResultTypeDef(TypedDict, total=False):
    DBSubnetGroup: "DBSubnetGroupTypeDef"


class ModifyEventSubscriptionResultTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class OptionGroupMembershipTypeDef(TypedDict, total=False):
    OptionGroupName: str
    Status: str


class OrderableDBInstanceOptionTypeDef(TypedDict, total=False):
    Engine: str
    EngineVersion: str
    DBInstanceClass: str
    LicenseModel: str
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


class OrderableDBInstanceOptionsMessageTypeDef(TypedDict, total=False):
    OrderableDBInstanceOptions: List["OrderableDBInstanceOptionTypeDef"]
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
    ApplyType: str
    DataType: str
    AllowedValues: str
    IsModifiable: bool
    MinimumEngineVersion: str
    ApplyMethod: ApplyMethod


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


class PromoteReadReplicaDBClusterResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class RangeTypeDef(TypedDict, total=False):
    From: int
    To: int
    Step: int


class RebootDBInstanceResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class RemoveSourceIdentifierFromSubscriptionResultTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class ResourcePendingMaintenanceActionsTypeDef(TypedDict, total=False):
    ResourceIdentifier: str
    PendingMaintenanceActionDetails: List["PendingMaintenanceActionTypeDef"]


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RestoreDBClusterFromSnapshotResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class RestoreDBClusterToPointInTimeResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class StartDBClusterResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class StopDBClusterResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class SubnetTypeDef(TypedDict, total=False):
    SubnetIdentifier: str
    SubnetAvailabilityZone: "AvailabilityZoneTypeDef"
    SubnetStatus: str


class TagListMessageTypeDef(TypedDict, total=False):
    TagList: List["TagTypeDef"]


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class TimezoneTypeDef(TypedDict, total=False):
    TimezoneName: str


class UpgradeTargetTypeDef(TypedDict, total=False):
    Engine: str
    EngineVersion: str
    Description: str
    AutoUpgrade: bool
    IsMajorVersionUpgrade: bool


class ValidDBInstanceModificationsMessageTypeDef(TypedDict, total=False):
    Storage: List["ValidStorageOptionsTypeDef"]


class ValidStorageOptionsTypeDef(TypedDict, total=False):
    StorageType: str
    StorageSize: List["RangeTypeDef"]
    ProvisionedIops: List["RangeTypeDef"]
    IopsToStorageRatio: List["DoubleRangeTypeDef"]


class VpcSecurityGroupMembershipTypeDef(TypedDict, total=False):
    VpcSecurityGroupId: str
    Status: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
