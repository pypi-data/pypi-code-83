"""
Type annotations for docdb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_docdb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_docdb.type_defs import AddSourceIdentifierToSubscriptionResultTypeDef

    data: AddSourceIdentifierToSubscriptionResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_docdb.literals import ApplyMethod, SourceType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AddSourceIdentifierToSubscriptionResultTypeDef",
    "ApplyPendingMaintenanceActionResultTypeDef",
    "AvailabilityZoneTypeDef",
    "CertificateMessageTypeDef",
    "CertificateTypeDef",
    "CloudwatchLogsExportConfigurationTypeDef",
    "CopyDBClusterParameterGroupResultTypeDef",
    "CopyDBClusterSnapshotResultTypeDef",
    "CreateDBClusterParameterGroupResultTypeDef",
    "CreateDBClusterResultTypeDef",
    "CreateDBClusterSnapshotResultTypeDef",
    "CreateDBInstanceResultTypeDef",
    "CreateDBSubnetGroupResultTypeDef",
    "CreateEventSubscriptionResultTypeDef",
    "DBClusterMemberTypeDef",
    "DBClusterMessageTypeDef",
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
    "DBSubnetGroupMessageTypeDef",
    "DBSubnetGroupTypeDef",
    "DeleteDBClusterResultTypeDef",
    "DeleteDBClusterSnapshotResultTypeDef",
    "DeleteDBInstanceResultTypeDef",
    "DeleteEventSubscriptionResultTypeDef",
    "DescribeDBClusterSnapshotAttributesResultTypeDef",
    "DescribeEngineDefaultClusterParametersResultTypeDef",
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
    "ModifyDBClusterResultTypeDef",
    "ModifyDBClusterSnapshotAttributeResultTypeDef",
    "ModifyDBInstanceResultTypeDef",
    "ModifyDBSubnetGroupResultTypeDef",
    "ModifyEventSubscriptionResultTypeDef",
    "OrderableDBInstanceOptionTypeDef",
    "OrderableDBInstanceOptionsMessageTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterTypeDef",
    "PendingCloudwatchLogsExportsTypeDef",
    "PendingMaintenanceActionTypeDef",
    "PendingMaintenanceActionsMessageTypeDef",
    "PendingModifiedValuesTypeDef",
    "RebootDBInstanceResultTypeDef",
    "RemoveSourceIdentifierFromSubscriptionResultTypeDef",
    "ResourcePendingMaintenanceActionsTypeDef",
    "RestoreDBClusterFromSnapshotResultTypeDef",
    "RestoreDBClusterToPointInTimeResultTypeDef",
    "StartDBClusterResultTypeDef",
    "StopDBClusterResultTypeDef",
    "SubnetTypeDef",
    "TagListMessageTypeDef",
    "TagTypeDef",
    "UpgradeTargetTypeDef",
    "VpcSecurityGroupMembershipTypeDef",
    "WaiterConfigTypeDef",
)


class AddSourceIdentifierToSubscriptionResultTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class ApplyPendingMaintenanceActionResultTypeDef(TypedDict, total=False):
    ResourcePendingMaintenanceActions: "ResourcePendingMaintenanceActionsTypeDef"


class AvailabilityZoneTypeDef(TypedDict, total=False):
    Name: str


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


class CloudwatchLogsExportConfigurationTypeDef(TypedDict, total=False):
    EnableLogTypes: List[str]
    DisableLogTypes: List[str]


class CopyDBClusterParameterGroupResultTypeDef(TypedDict, total=False):
    DBClusterParameterGroup: "DBClusterParameterGroupTypeDef"


class CopyDBClusterSnapshotResultTypeDef(TypedDict, total=False):
    DBClusterSnapshot: "DBClusterSnapshotTypeDef"


class CreateDBClusterParameterGroupResultTypeDef(TypedDict, total=False):
    DBClusterParameterGroup: "DBClusterParameterGroupTypeDef"


class CreateDBClusterResultTypeDef(TypedDict, total=False):
    DBCluster: "DBClusterTypeDef"


class CreateDBClusterSnapshotResultTypeDef(TypedDict, total=False):
    DBClusterSnapshot: "DBClusterSnapshotTypeDef"


class CreateDBInstanceResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class CreateDBSubnetGroupResultTypeDef(TypedDict, total=False):
    DBSubnetGroup: "DBSubnetGroupTypeDef"


class CreateEventSubscriptionResultTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class DBClusterMemberTypeDef(TypedDict, total=False):
    DBInstanceIdentifier: str
    IsClusterWriter: bool
    DBClusterParameterGroupStatus: str
    PromotionTier: int


class DBClusterMessageTypeDef(TypedDict, total=False):
    Marker: str
    DBClusters: List["DBClusterTypeDef"]


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
    Status: str
    Port: int
    VpcId: str
    ClusterCreateTime: datetime
    MasterUsername: str
    EngineVersion: str
    SnapshotType: str
    PercentProgress: int
    StorageEncrypted: bool
    KmsKeyId: str
    DBClusterSnapshotArn: str
    SourceDBClusterSnapshotArn: str


class DBClusterTypeDef(TypedDict, total=False):
    AvailabilityZones: List[str]
    BackupRetentionPeriod: int
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
    PreferredBackupWindow: str
    PreferredMaintenanceWindow: str
    DBClusterMembers: List["DBClusterMemberTypeDef"]
    VpcSecurityGroups: List["VpcSecurityGroupMembershipTypeDef"]
    HostedZoneId: str
    StorageEncrypted: bool
    KmsKeyId: str
    DbClusterResourceId: str
    DBClusterArn: str
    AssociatedRoles: List["DBClusterRoleTypeDef"]
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
    ValidUpgradeTarget: List["UpgradeTargetTypeDef"]
    ExportableLogTypes: List[str]
    SupportsLogExportsToCloudwatchLogs: bool


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
    Endpoint: "EndpointTypeDef"
    InstanceCreateTime: datetime
    PreferredBackupWindow: str
    BackupRetentionPeriod: int
    VpcSecurityGroups: List["VpcSecurityGroupMembershipTypeDef"]
    AvailabilityZone: str
    DBSubnetGroup: "DBSubnetGroupTypeDef"
    PreferredMaintenanceWindow: str
    PendingModifiedValues: "PendingModifiedValuesTypeDef"
    LatestRestorableTime: datetime
    EngineVersion: str
    AutoMinorVersionUpgrade: bool
    PubliclyAccessible: bool
    StatusInfos: List["DBInstanceStatusInfoTypeDef"]
    DBClusterIdentifier: str
    StorageEncrypted: bool
    KmsKeyId: str
    DbiResourceId: str
    CACertificateIdentifier: str
    PromotionTier: int
    DBInstanceArn: str
    EnabledCloudwatchLogsExports: List[str]


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


class OrderableDBInstanceOptionTypeDef(TypedDict, total=False):
    Engine: str
    EngineVersion: str
    DBInstanceClass: str
    LicenseModel: str
    AvailabilityZones: List["AvailabilityZoneTypeDef"]
    Vpc: bool


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


class RebootDBInstanceResultTypeDef(TypedDict, total=False):
    DBInstance: "DBInstanceTypeDef"


class RemoveSourceIdentifierFromSubscriptionResultTypeDef(TypedDict, total=False):
    EventSubscription: "EventSubscriptionTypeDef"


class ResourcePendingMaintenanceActionsTypeDef(TypedDict, total=False):
    ResourceIdentifier: str
    PendingMaintenanceActionDetails: List["PendingMaintenanceActionTypeDef"]


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


class UpgradeTargetTypeDef(TypedDict, total=False):
    Engine: str
    EngineVersion: str
    Description: str
    AutoUpgrade: bool
    IsMajorVersionUpgrade: bool


class VpcSecurityGroupMembershipTypeDef(TypedDict, total=False):
    VpcSecurityGroupId: str
    Status: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
