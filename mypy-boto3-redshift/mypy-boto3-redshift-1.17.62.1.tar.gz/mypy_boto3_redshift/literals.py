"""
Type annotations for redshift service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift/literals.html)

Usage::

    ```python
    from mypy_boto3_redshift.literals import ActionType

    data: ActionType = "recommend-node-config"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActionType",
    "AquaConfigurationStatus",
    "AquaStatus",
    "AuthorizationStatus",
    "ClusterAvailableWaiterName",
    "ClusterDeletedWaiterName",
    "ClusterRestoredWaiterName",
    "DescribeClusterDbRevisionsPaginatorName",
    "DescribeClusterParameterGroupsPaginatorName",
    "DescribeClusterParametersPaginatorName",
    "DescribeClusterSecurityGroupsPaginatorName",
    "DescribeClusterSnapshotsPaginatorName",
    "DescribeClusterSubnetGroupsPaginatorName",
    "DescribeClusterTracksPaginatorName",
    "DescribeClusterVersionsPaginatorName",
    "DescribeClustersPaginatorName",
    "DescribeDefaultClusterParametersPaginatorName",
    "DescribeEndpointAccessPaginatorName",
    "DescribeEndpointAuthorizationPaginatorName",
    "DescribeEventSubscriptionsPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeHsmClientCertificatesPaginatorName",
    "DescribeHsmConfigurationsPaginatorName",
    "DescribeNodeConfigurationOptionsPaginatorName",
    "DescribeOrderableClusterOptionsPaginatorName",
    "DescribeReservedNodeOfferingsPaginatorName",
    "DescribeReservedNodesPaginatorName",
    "DescribeScheduledActionsPaginatorName",
    "DescribeSnapshotCopyGrantsPaginatorName",
    "DescribeSnapshotSchedulesPaginatorName",
    "DescribeTableRestoreStatusPaginatorName",
    "DescribeTagsPaginatorName",
    "DescribeUsageLimitsPaginatorName",
    "GetReservedNodeExchangeOfferingsPaginatorName",
    "Mode",
    "NodeConfigurationOptionsFilterName",
    "OperatorType",
    "ParameterApplyType",
    "PartnerIntegrationStatus",
    "ReservedNodeOfferingType",
    "ScheduleState",
    "ScheduledActionFilterName",
    "ScheduledActionState",
    "ScheduledActionTypeValues",
    "SnapshotAttributeToSortBy",
    "SnapshotAvailableWaiterName",
    "SortByOrder",
    "SourceType",
    "TableRestoreStatusType",
    "UsageLimitBreachAction",
    "UsageLimitFeatureType",
    "UsageLimitLimitType",
    "UsageLimitPeriod",
)


ActionType = Literal["recommend-node-config", "resize-cluster", "restore-cluster"]
AquaConfigurationStatus = Literal["auto", "disabled", "enabled"]
AquaStatus = Literal["applying", "disabled", "enabled"]
AuthorizationStatus = Literal["Authorized", "Revoking"]
ClusterAvailableWaiterName = Literal["cluster_available"]
ClusterDeletedWaiterName = Literal["cluster_deleted"]
ClusterRestoredWaiterName = Literal["cluster_restored"]
DescribeClusterDbRevisionsPaginatorName = Literal["describe_cluster_db_revisions"]
DescribeClusterParameterGroupsPaginatorName = Literal["describe_cluster_parameter_groups"]
DescribeClusterParametersPaginatorName = Literal["describe_cluster_parameters"]
DescribeClusterSecurityGroupsPaginatorName = Literal["describe_cluster_security_groups"]
DescribeClusterSnapshotsPaginatorName = Literal["describe_cluster_snapshots"]
DescribeClusterSubnetGroupsPaginatorName = Literal["describe_cluster_subnet_groups"]
DescribeClusterTracksPaginatorName = Literal["describe_cluster_tracks"]
DescribeClusterVersionsPaginatorName = Literal["describe_cluster_versions"]
DescribeClustersPaginatorName = Literal["describe_clusters"]
DescribeDefaultClusterParametersPaginatorName = Literal["describe_default_cluster_parameters"]
DescribeEndpointAccessPaginatorName = Literal["describe_endpoint_access"]
DescribeEndpointAuthorizationPaginatorName = Literal["describe_endpoint_authorization"]
DescribeEventSubscriptionsPaginatorName = Literal["describe_event_subscriptions"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeHsmClientCertificatesPaginatorName = Literal["describe_hsm_client_certificates"]
DescribeHsmConfigurationsPaginatorName = Literal["describe_hsm_configurations"]
DescribeNodeConfigurationOptionsPaginatorName = Literal["describe_node_configuration_options"]
DescribeOrderableClusterOptionsPaginatorName = Literal["describe_orderable_cluster_options"]
DescribeReservedNodeOfferingsPaginatorName = Literal["describe_reserved_node_offerings"]
DescribeReservedNodesPaginatorName = Literal["describe_reserved_nodes"]
DescribeScheduledActionsPaginatorName = Literal["describe_scheduled_actions"]
DescribeSnapshotCopyGrantsPaginatorName = Literal["describe_snapshot_copy_grants"]
DescribeSnapshotSchedulesPaginatorName = Literal["describe_snapshot_schedules"]
DescribeTableRestoreStatusPaginatorName = Literal["describe_table_restore_status"]
DescribeTagsPaginatorName = Literal["describe_tags"]
DescribeUsageLimitsPaginatorName = Literal["describe_usage_limits"]
GetReservedNodeExchangeOfferingsPaginatorName = Literal["get_reserved_node_exchange_offerings"]
Mode = Literal["high-performance", "standard"]
NodeConfigurationOptionsFilterName = Literal[
    "EstimatedDiskUtilizationPercent", "Mode", "NodeType", "NumberOfNodes"
]
OperatorType = Literal["between", "eq", "ge", "gt", "in", "le", "lt"]
ParameterApplyType = Literal["dynamic", "static"]
PartnerIntegrationStatus = Literal["Active", "ConnectionFailure", "Inactive", "RuntimeFailure"]
ReservedNodeOfferingType = Literal["Regular", "Upgradable"]
ScheduleState = Literal["ACTIVE", "FAILED", "MODIFYING"]
ScheduledActionFilterName = Literal["cluster-identifier", "iam-role"]
ScheduledActionState = Literal["ACTIVE", "DISABLED"]
ScheduledActionTypeValues = Literal["PauseCluster", "ResizeCluster", "ResumeCluster"]
SnapshotAttributeToSortBy = Literal["CREATE_TIME", "SOURCE_TYPE", "TOTAL_SIZE"]
SnapshotAvailableWaiterName = Literal["snapshot_available"]
SortByOrder = Literal["ASC", "DESC"]
SourceType = Literal[
    "cluster",
    "cluster-parameter-group",
    "cluster-security-group",
    "cluster-snapshot",
    "scheduled-action",
]
TableRestoreStatusType = Literal["CANCELED", "FAILED", "IN_PROGRESS", "PENDING", "SUCCEEDED"]
UsageLimitBreachAction = Literal["disable", "emit-metric", "log"]
UsageLimitFeatureType = Literal["concurrency-scaling", "spectrum"]
UsageLimitLimitType = Literal["data-scanned", "time"]
UsageLimitPeriod = Literal["daily", "monthly", "weekly"]
