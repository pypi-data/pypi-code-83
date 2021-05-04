"""
Type annotations for elasticache service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elasticache.type_defs import AllowedNodeTypeModificationsMessageTypeDef

    data: AllowedNodeTypeModificationsMessageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_elasticache.literals import (
    AuthenticationType,
    AuthTokenUpdateStatus,
    AutomaticFailoverStatus,
    ChangeType,
    DestinationType,
    LogDeliveryConfigurationStatus,
    LogFormat,
    MultiAZStatus,
    NodeUpdateInitiatedBy,
    NodeUpdateStatus,
    PendingAutomaticFailoverStatus,
    ServiceUpdateSeverity,
    ServiceUpdateStatus,
    SlaMet,
    SourceType,
    UpdateActionStatus,
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
    "AllowedNodeTypeModificationsMessageTypeDef",
    "AuthenticationTypeDef",
    "AuthorizeCacheSecurityGroupIngressResultTypeDef",
    "AvailabilityZoneTypeDef",
    "CacheClusterMessageTypeDef",
    "CacheClusterTypeDef",
    "CacheEngineVersionMessageTypeDef",
    "CacheEngineVersionTypeDef",
    "CacheNodeTypeDef",
    "CacheNodeTypeSpecificParameterTypeDef",
    "CacheNodeTypeSpecificValueTypeDef",
    "CacheNodeUpdateStatusTypeDef",
    "CacheParameterGroupDetailsTypeDef",
    "CacheParameterGroupNameMessageTypeDef",
    "CacheParameterGroupStatusTypeDef",
    "CacheParameterGroupTypeDef",
    "CacheParameterGroupsMessageTypeDef",
    "CacheSecurityGroupMembershipTypeDef",
    "CacheSecurityGroupMessageTypeDef",
    "CacheSecurityGroupTypeDef",
    "CacheSubnetGroupMessageTypeDef",
    "CacheSubnetGroupTypeDef",
    "CloudWatchLogsDestinationDetailsTypeDef",
    "CompleteMigrationResponseTypeDef",
    "ConfigureShardTypeDef",
    "CopySnapshotResultTypeDef",
    "CreateCacheClusterResultTypeDef",
    "CreateCacheParameterGroupResultTypeDef",
    "CreateCacheSecurityGroupResultTypeDef",
    "CreateCacheSubnetGroupResultTypeDef",
    "CreateGlobalReplicationGroupResultTypeDef",
    "CreateReplicationGroupResultTypeDef",
    "CreateSnapshotResultTypeDef",
    "CustomerNodeEndpointTypeDef",
    "DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    "DecreaseReplicaCountResultTypeDef",
    "DeleteCacheClusterResultTypeDef",
    "DeleteGlobalReplicationGroupResultTypeDef",
    "DeleteReplicationGroupResultTypeDef",
    "DeleteSnapshotResultTypeDef",
    "DescribeEngineDefaultParametersResultTypeDef",
    "DescribeGlobalReplicationGroupsResultTypeDef",
    "DescribeSnapshotsListMessageTypeDef",
    "DescribeUserGroupsResultTypeDef",
    "DescribeUsersResultTypeDef",
    "DestinationDetailsTypeDef",
    "DisassociateGlobalReplicationGroupResultTypeDef",
    "EC2SecurityGroupTypeDef",
    "EndpointTypeDef",
    "EngineDefaultsTypeDef",
    "EventTypeDef",
    "EventsMessageTypeDef",
    "FailoverGlobalReplicationGroupResultTypeDef",
    "FilterTypeDef",
    "GlobalNodeGroupTypeDef",
    "GlobalReplicationGroupInfoTypeDef",
    "GlobalReplicationGroupMemberTypeDef",
    "GlobalReplicationGroupTypeDef",
    "IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef",
    "IncreaseReplicaCountResultTypeDef",
    "KinesisFirehoseDestinationDetailsTypeDef",
    "LogDeliveryConfigurationRequestTypeDef",
    "LogDeliveryConfigurationTypeDef",
    "ModifyCacheClusterResultTypeDef",
    "ModifyCacheSubnetGroupResultTypeDef",
    "ModifyGlobalReplicationGroupResultTypeDef",
    "ModifyReplicationGroupResultTypeDef",
    "ModifyReplicationGroupShardConfigurationResultTypeDef",
    "NodeGroupConfigurationTypeDef",
    "NodeGroupMemberTypeDef",
    "NodeGroupMemberUpdateStatusTypeDef",
    "NodeGroupTypeDef",
    "NodeGroupUpdateStatusTypeDef",
    "NodeSnapshotTypeDef",
    "NotificationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterNameValueTypeDef",
    "ParameterTypeDef",
    "PendingLogDeliveryConfigurationTypeDef",
    "PendingModifiedValuesTypeDef",
    "ProcessedUpdateActionTypeDef",
    "PurchaseReservedCacheNodesOfferingResultTypeDef",
    "RebalanceSlotsInGlobalReplicationGroupResultTypeDef",
    "RebootCacheClusterResultTypeDef",
    "RecurringChargeTypeDef",
    "RegionalConfigurationTypeDef",
    "ReplicationGroupMessageTypeDef",
    "ReplicationGroupPendingModifiedValuesTypeDef",
    "ReplicationGroupTypeDef",
    "ReservedCacheNodeMessageTypeDef",
    "ReservedCacheNodeTypeDef",
    "ReservedCacheNodesOfferingMessageTypeDef",
    "ReservedCacheNodesOfferingTypeDef",
    "ReshardingConfigurationTypeDef",
    "ReshardingStatusTypeDef",
    "RevokeCacheSecurityGroupIngressResultTypeDef",
    "SecurityGroupMembershipTypeDef",
    "ServiceUpdateTypeDef",
    "ServiceUpdatesMessageTypeDef",
    "SlotMigrationTypeDef",
    "SnapshotTypeDef",
    "StartMigrationResponseTypeDef",
    "SubnetOutpostTypeDef",
    "SubnetTypeDef",
    "TagListMessageTypeDef",
    "TagTypeDef",
    "TestFailoverResultTypeDef",
    "TimeRangeFilterTypeDef",
    "UnprocessedUpdateActionTypeDef",
    "UpdateActionResultsMessageTypeDef",
    "UpdateActionTypeDef",
    "UpdateActionsMessageTypeDef",
    "UserGroupPendingChangesTypeDef",
    "UserGroupTypeDef",
    "UserGroupsUpdateStatusTypeDef",
    "UserTypeDef",
    "WaiterConfigTypeDef",
)


class AllowedNodeTypeModificationsMessageTypeDef(TypedDict, total=False):
    ScaleUpModifications: List[str]
    ScaleDownModifications: List[str]


AuthenticationTypeDef = TypedDict(
    "AuthenticationTypeDef", {"Type": AuthenticationType, "PasswordCount": int}, total=False
)


class AuthorizeCacheSecurityGroupIngressResultTypeDef(TypedDict, total=False):
    CacheSecurityGroup: "CacheSecurityGroupTypeDef"


class AvailabilityZoneTypeDef(TypedDict, total=False):
    Name: str


class CacheClusterMessageTypeDef(TypedDict, total=False):
    Marker: str
    CacheClusters: List["CacheClusterTypeDef"]


class CacheClusterTypeDef(TypedDict, total=False):
    CacheClusterId: str
    ConfigurationEndpoint: "EndpointTypeDef"
    ClientDownloadLandingPage: str
    CacheNodeType: str
    Engine: str
    EngineVersion: str
    CacheClusterStatus: str
    NumCacheNodes: int
    PreferredAvailabilityZone: str
    PreferredOutpostArn: str
    CacheClusterCreateTime: datetime
    PreferredMaintenanceWindow: str
    PendingModifiedValues: "PendingModifiedValuesTypeDef"
    NotificationConfiguration: "NotificationConfigurationTypeDef"
    CacheSecurityGroups: List["CacheSecurityGroupMembershipTypeDef"]
    CacheParameterGroup: "CacheParameterGroupStatusTypeDef"
    CacheSubnetGroupName: str
    CacheNodes: List["CacheNodeTypeDef"]
    AutoMinorVersionUpgrade: bool
    SecurityGroups: List["SecurityGroupMembershipTypeDef"]
    ReplicationGroupId: str
    SnapshotRetentionLimit: int
    SnapshotWindow: str
    AuthTokenEnabled: bool
    AuthTokenLastModifiedDate: datetime
    TransitEncryptionEnabled: bool
    AtRestEncryptionEnabled: bool
    ARN: str
    ReplicationGroupLogDeliveryEnabled: bool
    LogDeliveryConfigurations: List["LogDeliveryConfigurationTypeDef"]


class CacheEngineVersionMessageTypeDef(TypedDict, total=False):
    Marker: str
    CacheEngineVersions: List["CacheEngineVersionTypeDef"]


class CacheEngineVersionTypeDef(TypedDict, total=False):
    Engine: str
    EngineVersion: str
    CacheParameterGroupFamily: str
    CacheEngineDescription: str
    CacheEngineVersionDescription: str


class CacheNodeTypeDef(TypedDict, total=False):
    CacheNodeId: str
    CacheNodeStatus: str
    CacheNodeCreateTime: datetime
    Endpoint: "EndpointTypeDef"
    ParameterGroupStatus: str
    SourceCacheNodeId: str
    CustomerAvailabilityZone: str
    CustomerOutpostArn: str


class CacheNodeTypeSpecificParameterTypeDef(TypedDict, total=False):
    ParameterName: str
    Description: str
    Source: str
    DataType: str
    AllowedValues: str
    IsModifiable: bool
    MinimumEngineVersion: str
    CacheNodeTypeSpecificValues: List["CacheNodeTypeSpecificValueTypeDef"]
    ChangeType: ChangeType


class CacheNodeTypeSpecificValueTypeDef(TypedDict, total=False):
    CacheNodeType: str
    Value: str


class CacheNodeUpdateStatusTypeDef(TypedDict, total=False):
    CacheNodeId: str
    NodeUpdateStatus: NodeUpdateStatus
    NodeDeletionDate: datetime
    NodeUpdateStartDate: datetime
    NodeUpdateEndDate: datetime
    NodeUpdateInitiatedBy: NodeUpdateInitiatedBy
    NodeUpdateInitiatedDate: datetime
    NodeUpdateStatusModifiedDate: datetime


class CacheParameterGroupDetailsTypeDef(TypedDict, total=False):
    Marker: str
    Parameters: List["ParameterTypeDef"]
    CacheNodeTypeSpecificParameters: List["CacheNodeTypeSpecificParameterTypeDef"]


class CacheParameterGroupNameMessageTypeDef(TypedDict, total=False):
    CacheParameterGroupName: str


class CacheParameterGroupStatusTypeDef(TypedDict, total=False):
    CacheParameterGroupName: str
    ParameterApplyStatus: str
    CacheNodeIdsToReboot: List[str]


class CacheParameterGroupTypeDef(TypedDict, total=False):
    CacheParameterGroupName: str
    CacheParameterGroupFamily: str
    Description: str
    IsGlobal: bool
    ARN: str


class CacheParameterGroupsMessageTypeDef(TypedDict, total=False):
    Marker: str
    CacheParameterGroups: List["CacheParameterGroupTypeDef"]


class CacheSecurityGroupMembershipTypeDef(TypedDict, total=False):
    CacheSecurityGroupName: str
    Status: str


class CacheSecurityGroupMessageTypeDef(TypedDict, total=False):
    Marker: str
    CacheSecurityGroups: List["CacheSecurityGroupTypeDef"]


class CacheSecurityGroupTypeDef(TypedDict, total=False):
    OwnerId: str
    CacheSecurityGroupName: str
    Description: str
    EC2SecurityGroups: List["EC2SecurityGroupTypeDef"]
    ARN: str


class CacheSubnetGroupMessageTypeDef(TypedDict, total=False):
    Marker: str
    CacheSubnetGroups: List["CacheSubnetGroupTypeDef"]


class CacheSubnetGroupTypeDef(TypedDict, total=False):
    CacheSubnetGroupName: str
    CacheSubnetGroupDescription: str
    VpcId: str
    Subnets: List["SubnetTypeDef"]
    ARN: str


class CloudWatchLogsDestinationDetailsTypeDef(TypedDict, total=False):
    LogGroup: str


class CompleteMigrationResponseTypeDef(TypedDict, total=False):
    ReplicationGroup: "ReplicationGroupTypeDef"


class _RequiredConfigureShardTypeDef(TypedDict):
    NodeGroupId: str
    NewReplicaCount: int


class ConfigureShardTypeDef(_RequiredConfigureShardTypeDef, total=False):
    PreferredAvailabilityZones: List[str]
    PreferredOutpostArns: List[str]


class CopySnapshotResultTypeDef(TypedDict, total=False):
    Snapshot: "SnapshotTypeDef"


class CreateCacheClusterResultTypeDef(TypedDict, total=False):
    CacheCluster: "CacheClusterTypeDef"


class CreateCacheParameterGroupResultTypeDef(TypedDict, total=False):
    CacheParameterGroup: "CacheParameterGroupTypeDef"


class CreateCacheSecurityGroupResultTypeDef(TypedDict, total=False):
    CacheSecurityGroup: "CacheSecurityGroupTypeDef"


class CreateCacheSubnetGroupResultTypeDef(TypedDict, total=False):
    CacheSubnetGroup: "CacheSubnetGroupTypeDef"


class CreateGlobalReplicationGroupResultTypeDef(TypedDict, total=False):
    GlobalReplicationGroup: "GlobalReplicationGroupTypeDef"


class CreateReplicationGroupResultTypeDef(TypedDict, total=False):
    ReplicationGroup: "ReplicationGroupTypeDef"


class CreateSnapshotResultTypeDef(TypedDict, total=False):
    Snapshot: "SnapshotTypeDef"


class CustomerNodeEndpointTypeDef(TypedDict, total=False):
    Address: str
    Port: int


class DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef(TypedDict, total=False):
    GlobalReplicationGroup: "GlobalReplicationGroupTypeDef"


class DecreaseReplicaCountResultTypeDef(TypedDict, total=False):
    ReplicationGroup: "ReplicationGroupTypeDef"


class DeleteCacheClusterResultTypeDef(TypedDict, total=False):
    CacheCluster: "CacheClusterTypeDef"


class DeleteGlobalReplicationGroupResultTypeDef(TypedDict, total=False):
    GlobalReplicationGroup: "GlobalReplicationGroupTypeDef"


class DeleteReplicationGroupResultTypeDef(TypedDict, total=False):
    ReplicationGroup: "ReplicationGroupTypeDef"


class DeleteSnapshotResultTypeDef(TypedDict, total=False):
    Snapshot: "SnapshotTypeDef"


class DescribeEngineDefaultParametersResultTypeDef(TypedDict, total=False):
    EngineDefaults: "EngineDefaultsTypeDef"


class DescribeGlobalReplicationGroupsResultTypeDef(TypedDict, total=False):
    Marker: str
    GlobalReplicationGroups: List["GlobalReplicationGroupTypeDef"]


class DescribeSnapshotsListMessageTypeDef(TypedDict, total=False):
    Marker: str
    Snapshots: List["SnapshotTypeDef"]


class DescribeUserGroupsResultTypeDef(TypedDict, total=False):
    UserGroups: List["UserGroupTypeDef"]
    Marker: str


class DescribeUsersResultTypeDef(TypedDict, total=False):
    Users: List["UserTypeDef"]
    Marker: str


class DestinationDetailsTypeDef(TypedDict, total=False):
    CloudWatchLogsDetails: "CloudWatchLogsDestinationDetailsTypeDef"
    KinesisFirehoseDetails: "KinesisFirehoseDestinationDetailsTypeDef"


class DisassociateGlobalReplicationGroupResultTypeDef(TypedDict, total=False):
    GlobalReplicationGroup: "GlobalReplicationGroupTypeDef"


class EC2SecurityGroupTypeDef(TypedDict, total=False):
    Status: str
    EC2SecurityGroupName: str
    EC2SecurityGroupOwnerId: str


class EndpointTypeDef(TypedDict, total=False):
    Address: str
    Port: int


class EngineDefaultsTypeDef(TypedDict, total=False):
    CacheParameterGroupFamily: str
    Marker: str
    Parameters: List["ParameterTypeDef"]
    CacheNodeTypeSpecificParameters: List["CacheNodeTypeSpecificParameterTypeDef"]


class EventTypeDef(TypedDict, total=False):
    SourceIdentifier: str
    SourceType: SourceType
    Message: str
    Date: datetime


class EventsMessageTypeDef(TypedDict, total=False):
    Marker: str
    Events: List["EventTypeDef"]


class FailoverGlobalReplicationGroupResultTypeDef(TypedDict, total=False):
    GlobalReplicationGroup: "GlobalReplicationGroupTypeDef"


class FilterTypeDef(TypedDict):
    Name: str
    Values: List[str]


class GlobalNodeGroupTypeDef(TypedDict, total=False):
    GlobalNodeGroupId: str
    Slots: str


class GlobalReplicationGroupInfoTypeDef(TypedDict, total=False):
    GlobalReplicationGroupId: str
    GlobalReplicationGroupMemberRole: str


class GlobalReplicationGroupMemberTypeDef(TypedDict, total=False):
    ReplicationGroupId: str
    ReplicationGroupRegion: str
    Role: str
    AutomaticFailover: AutomaticFailoverStatus
    Status: str


class GlobalReplicationGroupTypeDef(TypedDict, total=False):
    GlobalReplicationGroupId: str
    GlobalReplicationGroupDescription: str
    Status: str
    CacheNodeType: str
    Engine: str
    EngineVersion: str
    Members: List["GlobalReplicationGroupMemberTypeDef"]
    ClusterEnabled: bool
    GlobalNodeGroups: List["GlobalNodeGroupTypeDef"]
    AuthTokenEnabled: bool
    TransitEncryptionEnabled: bool
    AtRestEncryptionEnabled: bool
    ARN: str


class IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef(TypedDict, total=False):
    GlobalReplicationGroup: "GlobalReplicationGroupTypeDef"


class IncreaseReplicaCountResultTypeDef(TypedDict, total=False):
    ReplicationGroup: "ReplicationGroupTypeDef"


class KinesisFirehoseDestinationDetailsTypeDef(TypedDict, total=False):
    DeliveryStream: str


class LogDeliveryConfigurationRequestTypeDef(TypedDict, total=False):
    LogType: Literal["slow-log"]
    DestinationType: DestinationType
    DestinationDetails: "DestinationDetailsTypeDef"
    LogFormat: LogFormat
    Enabled: bool


class LogDeliveryConfigurationTypeDef(TypedDict, total=False):
    LogType: Literal["slow-log"]
    DestinationType: DestinationType
    DestinationDetails: "DestinationDetailsTypeDef"
    LogFormat: LogFormat
    Status: LogDeliveryConfigurationStatus
    Message: str


class ModifyCacheClusterResultTypeDef(TypedDict, total=False):
    CacheCluster: "CacheClusterTypeDef"


class ModifyCacheSubnetGroupResultTypeDef(TypedDict, total=False):
    CacheSubnetGroup: "CacheSubnetGroupTypeDef"


class ModifyGlobalReplicationGroupResultTypeDef(TypedDict, total=False):
    GlobalReplicationGroup: "GlobalReplicationGroupTypeDef"


class ModifyReplicationGroupResultTypeDef(TypedDict, total=False):
    ReplicationGroup: "ReplicationGroupTypeDef"


class ModifyReplicationGroupShardConfigurationResultTypeDef(TypedDict, total=False):
    ReplicationGroup: "ReplicationGroupTypeDef"


class NodeGroupConfigurationTypeDef(TypedDict, total=False):
    NodeGroupId: str
    Slots: str
    ReplicaCount: int
    PrimaryAvailabilityZone: str
    ReplicaAvailabilityZones: List[str]
    PrimaryOutpostArn: str
    ReplicaOutpostArns: List[str]


class NodeGroupMemberTypeDef(TypedDict, total=False):
    CacheClusterId: str
    CacheNodeId: str
    ReadEndpoint: "EndpointTypeDef"
    PreferredAvailabilityZone: str
    PreferredOutpostArn: str
    CurrentRole: str


class NodeGroupMemberUpdateStatusTypeDef(TypedDict, total=False):
    CacheClusterId: str
    CacheNodeId: str
    NodeUpdateStatus: NodeUpdateStatus
    NodeDeletionDate: datetime
    NodeUpdateStartDate: datetime
    NodeUpdateEndDate: datetime
    NodeUpdateInitiatedBy: NodeUpdateInitiatedBy
    NodeUpdateInitiatedDate: datetime
    NodeUpdateStatusModifiedDate: datetime


class NodeGroupTypeDef(TypedDict, total=False):
    NodeGroupId: str
    Status: str
    PrimaryEndpoint: "EndpointTypeDef"
    ReaderEndpoint: "EndpointTypeDef"
    Slots: str
    NodeGroupMembers: List["NodeGroupMemberTypeDef"]


class NodeGroupUpdateStatusTypeDef(TypedDict, total=False):
    NodeGroupId: str
    NodeGroupMemberUpdateStatus: List["NodeGroupMemberUpdateStatusTypeDef"]


class NodeSnapshotTypeDef(TypedDict, total=False):
    CacheClusterId: str
    NodeGroupId: str
    CacheNodeId: str
    NodeGroupConfiguration: "NodeGroupConfigurationTypeDef"
    CacheSize: str
    CacheNodeCreateTime: datetime
    SnapshotCreateTime: datetime


class NotificationConfigurationTypeDef(TypedDict, total=False):
    TopicArn: str
    TopicStatus: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParameterNameValueTypeDef(TypedDict, total=False):
    ParameterName: str
    ParameterValue: str


class ParameterTypeDef(TypedDict, total=False):
    ParameterName: str
    ParameterValue: str
    Description: str
    Source: str
    DataType: str
    AllowedValues: str
    IsModifiable: bool
    MinimumEngineVersion: str
    ChangeType: ChangeType


class PendingLogDeliveryConfigurationTypeDef(TypedDict, total=False):
    LogType: Literal["slow-log"]
    DestinationType: DestinationType
    DestinationDetails: "DestinationDetailsTypeDef"
    LogFormat: LogFormat


class PendingModifiedValuesTypeDef(TypedDict, total=False):
    NumCacheNodes: int
    CacheNodeIdsToRemove: List[str]
    EngineVersion: str
    CacheNodeType: str
    AuthTokenStatus: AuthTokenUpdateStatus
    LogDeliveryConfigurations: List["PendingLogDeliveryConfigurationTypeDef"]


class ProcessedUpdateActionTypeDef(TypedDict, total=False):
    ReplicationGroupId: str
    CacheClusterId: str
    ServiceUpdateName: str
    UpdateActionStatus: UpdateActionStatus


class PurchaseReservedCacheNodesOfferingResultTypeDef(TypedDict, total=False):
    ReservedCacheNode: "ReservedCacheNodeTypeDef"


class RebalanceSlotsInGlobalReplicationGroupResultTypeDef(TypedDict, total=False):
    GlobalReplicationGroup: "GlobalReplicationGroupTypeDef"


class RebootCacheClusterResultTypeDef(TypedDict, total=False):
    CacheCluster: "CacheClusterTypeDef"


class RecurringChargeTypeDef(TypedDict, total=False):
    RecurringChargeAmount: float
    RecurringChargeFrequency: str


class RegionalConfigurationTypeDef(TypedDict):
    ReplicationGroupId: str
    ReplicationGroupRegion: str
    ReshardingConfiguration: List["ReshardingConfigurationTypeDef"]


class ReplicationGroupMessageTypeDef(TypedDict, total=False):
    Marker: str
    ReplicationGroups: List["ReplicationGroupTypeDef"]


class ReplicationGroupPendingModifiedValuesTypeDef(TypedDict, total=False):
    PrimaryClusterId: str
    AutomaticFailoverStatus: PendingAutomaticFailoverStatus
    Resharding: "ReshardingStatusTypeDef"
    AuthTokenStatus: AuthTokenUpdateStatus
    UserGroups: "UserGroupsUpdateStatusTypeDef"
    LogDeliveryConfigurations: List["PendingLogDeliveryConfigurationTypeDef"]


class ReplicationGroupTypeDef(TypedDict, total=False):
    ReplicationGroupId: str
    Description: str
    GlobalReplicationGroupInfo: "GlobalReplicationGroupInfoTypeDef"
    Status: str
    PendingModifiedValues: "ReplicationGroupPendingModifiedValuesTypeDef"
    MemberClusters: List[str]
    NodeGroups: List["NodeGroupTypeDef"]
    SnapshottingClusterId: str
    AutomaticFailover: AutomaticFailoverStatus
    MultiAZ: MultiAZStatus
    ConfigurationEndpoint: "EndpointTypeDef"
    SnapshotRetentionLimit: int
    SnapshotWindow: str
    ClusterEnabled: bool
    CacheNodeType: str
    AuthTokenEnabled: bool
    AuthTokenLastModifiedDate: datetime
    TransitEncryptionEnabled: bool
    AtRestEncryptionEnabled: bool
    MemberClustersOutpostArns: List[str]
    KmsKeyId: str
    ARN: str
    UserGroupIds: List[str]
    LogDeliveryConfigurations: List["LogDeliveryConfigurationTypeDef"]


class ReservedCacheNodeMessageTypeDef(TypedDict, total=False):
    Marker: str
    ReservedCacheNodes: List["ReservedCacheNodeTypeDef"]


class ReservedCacheNodeTypeDef(TypedDict, total=False):
    ReservedCacheNodeId: str
    ReservedCacheNodesOfferingId: str
    CacheNodeType: str
    StartTime: datetime
    Duration: int
    FixedPrice: float
    UsagePrice: float
    CacheNodeCount: int
    ProductDescription: str
    OfferingType: str
    State: str
    RecurringCharges: List["RecurringChargeTypeDef"]
    ReservationARN: str


class ReservedCacheNodesOfferingMessageTypeDef(TypedDict, total=False):
    Marker: str
    ReservedCacheNodesOfferings: List["ReservedCacheNodesOfferingTypeDef"]


class ReservedCacheNodesOfferingTypeDef(TypedDict, total=False):
    ReservedCacheNodesOfferingId: str
    CacheNodeType: str
    Duration: int
    FixedPrice: float
    UsagePrice: float
    ProductDescription: str
    OfferingType: str
    RecurringCharges: List["RecurringChargeTypeDef"]


class ReshardingConfigurationTypeDef(TypedDict, total=False):
    NodeGroupId: str
    PreferredAvailabilityZones: List[str]


class ReshardingStatusTypeDef(TypedDict, total=False):
    SlotMigration: "SlotMigrationTypeDef"


class RevokeCacheSecurityGroupIngressResultTypeDef(TypedDict, total=False):
    CacheSecurityGroup: "CacheSecurityGroupTypeDef"


class SecurityGroupMembershipTypeDef(TypedDict, total=False):
    SecurityGroupId: str
    Status: str


class ServiceUpdateTypeDef(TypedDict, total=False):
    ServiceUpdateName: str
    ServiceUpdateReleaseDate: datetime
    ServiceUpdateEndDate: datetime
    ServiceUpdateSeverity: ServiceUpdateSeverity
    ServiceUpdateRecommendedApplyByDate: datetime
    ServiceUpdateStatus: ServiceUpdateStatus
    ServiceUpdateDescription: str
    ServiceUpdateType: Literal["security-update"]
    Engine: str
    EngineVersion: str
    AutoUpdateAfterRecommendedApplyByDate: bool
    EstimatedUpdateTime: str


class ServiceUpdatesMessageTypeDef(TypedDict, total=False):
    Marker: str
    ServiceUpdates: List["ServiceUpdateTypeDef"]


class SlotMigrationTypeDef(TypedDict, total=False):
    ProgressPercentage: float


class SnapshotTypeDef(TypedDict, total=False):
    SnapshotName: str
    ReplicationGroupId: str
    ReplicationGroupDescription: str
    CacheClusterId: str
    SnapshotStatus: str
    SnapshotSource: str
    CacheNodeType: str
    Engine: str
    EngineVersion: str
    NumCacheNodes: int
    PreferredAvailabilityZone: str
    PreferredOutpostArn: str
    CacheClusterCreateTime: datetime
    PreferredMaintenanceWindow: str
    TopicArn: str
    Port: int
    CacheParameterGroupName: str
    CacheSubnetGroupName: str
    VpcId: str
    AutoMinorVersionUpgrade: bool
    SnapshotRetentionLimit: int
    SnapshotWindow: str
    NumNodeGroups: int
    AutomaticFailover: AutomaticFailoverStatus
    NodeSnapshots: List["NodeSnapshotTypeDef"]
    KmsKeyId: str
    ARN: str


class StartMigrationResponseTypeDef(TypedDict, total=False):
    ReplicationGroup: "ReplicationGroupTypeDef"


class SubnetOutpostTypeDef(TypedDict, total=False):
    SubnetOutpostArn: str


class SubnetTypeDef(TypedDict, total=False):
    SubnetIdentifier: str
    SubnetAvailabilityZone: "AvailabilityZoneTypeDef"
    SubnetOutpost: "SubnetOutpostTypeDef"


class TagListMessageTypeDef(TypedDict, total=False):
    TagList: List["TagTypeDef"]


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class TestFailoverResultTypeDef(TypedDict, total=False):
    ReplicationGroup: "ReplicationGroupTypeDef"


class TimeRangeFilterTypeDef(TypedDict, total=False):
    StartTime: datetime
    EndTime: datetime


class UnprocessedUpdateActionTypeDef(TypedDict, total=False):
    ReplicationGroupId: str
    CacheClusterId: str
    ServiceUpdateName: str
    ErrorType: str
    ErrorMessage: str


class UpdateActionResultsMessageTypeDef(TypedDict, total=False):
    ProcessedUpdateActions: List["ProcessedUpdateActionTypeDef"]
    UnprocessedUpdateActions: List["UnprocessedUpdateActionTypeDef"]


class UpdateActionTypeDef(TypedDict, total=False):
    ReplicationGroupId: str
    CacheClusterId: str
    ServiceUpdateName: str
    ServiceUpdateReleaseDate: datetime
    ServiceUpdateSeverity: ServiceUpdateSeverity
    ServiceUpdateStatus: ServiceUpdateStatus
    ServiceUpdateRecommendedApplyByDate: datetime
    ServiceUpdateType: Literal["security-update"]
    UpdateActionAvailableDate: datetime
    UpdateActionStatus: UpdateActionStatus
    NodesUpdated: str
    UpdateActionStatusModifiedDate: datetime
    SlaMet: SlaMet
    NodeGroupUpdateStatus: List["NodeGroupUpdateStatusTypeDef"]
    CacheNodeUpdateStatus: List["CacheNodeUpdateStatusTypeDef"]
    EstimatedUpdateTime: str
    Engine: str


class UpdateActionsMessageTypeDef(TypedDict, total=False):
    Marker: str
    UpdateActions: List["UpdateActionTypeDef"]


class UserGroupPendingChangesTypeDef(TypedDict, total=False):
    UserIdsToRemove: List[str]
    UserIdsToAdd: List[str]


class UserGroupTypeDef(TypedDict, total=False):
    UserGroupId: str
    Status: str
    Engine: str
    UserIds: List[str]
    PendingChanges: "UserGroupPendingChangesTypeDef"
    ReplicationGroups: List[str]
    ARN: str


class UserGroupsUpdateStatusTypeDef(TypedDict, total=False):
    UserGroupIdsToAdd: List[str]
    UserGroupIdsToRemove: List[str]


class UserTypeDef(TypedDict, total=False):
    UserId: str
    UserName: str
    Status: str
    Engine: str
    AccessString: str
    UserGroupIds: List[str]
    Authentication: "AuthenticationTypeDef"
    ARN: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
