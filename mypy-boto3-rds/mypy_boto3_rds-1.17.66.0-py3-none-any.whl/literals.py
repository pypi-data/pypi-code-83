"""
Type annotations for rds service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds/literals.html)

Usage::

    ```python
    from mypy_boto3_rds.literals import ActivityStreamMode

    data: ActivityStreamMode = "async"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActivityStreamMode",
    "ActivityStreamStatus",
    "ApplyMethod",
    "AuthScheme",
    "DBClusterSnapshotAvailableWaiterName",
    "DBClusterSnapshotDeletedWaiterName",
    "DBInstanceAvailableWaiterName",
    "DBInstanceDeletedWaiterName",
    "DBProxyEndpointStatus",
    "DBProxyEndpointTargetRole",
    "DBProxyStatus",
    "DBSnapshotAvailableWaiterName",
    "DBSnapshotCompletedWaiterName",
    "DBSnapshotDeletedWaiterName",
    "DescribeCertificatesPaginatorName",
    "DescribeCustomAvailabilityZonesPaginatorName",
    "DescribeDBClusterBacktracksPaginatorName",
    "DescribeDBClusterEndpointsPaginatorName",
    "DescribeDBClusterParameterGroupsPaginatorName",
    "DescribeDBClusterParametersPaginatorName",
    "DescribeDBClusterSnapshotsPaginatorName",
    "DescribeDBClustersPaginatorName",
    "DescribeDBEngineVersionsPaginatorName",
    "DescribeDBInstanceAutomatedBackupsPaginatorName",
    "DescribeDBInstancesPaginatorName",
    "DescribeDBLogFilesPaginatorName",
    "DescribeDBParameterGroupsPaginatorName",
    "DescribeDBParametersPaginatorName",
    "DescribeDBProxiesPaginatorName",
    "DescribeDBProxyEndpointsPaginatorName",
    "DescribeDBProxyTargetGroupsPaginatorName",
    "DescribeDBProxyTargetsPaginatorName",
    "DescribeDBSecurityGroupsPaginatorName",
    "DescribeDBSnapshotsPaginatorName",
    "DescribeDBSubnetGroupsPaginatorName",
    "DescribeEngineDefaultClusterParametersPaginatorName",
    "DescribeEngineDefaultParametersPaginatorName",
    "DescribeEventSubscriptionsPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeExportTasksPaginatorName",
    "DescribeGlobalClustersPaginatorName",
    "DescribeInstallationMediaPaginatorName",
    "DescribeOptionGroupOptionsPaginatorName",
    "DescribeOptionGroupsPaginatorName",
    "DescribeOrderableDBInstanceOptionsPaginatorName",
    "DescribePendingMaintenanceActionsPaginatorName",
    "DescribeReservedDBInstancesOfferingsPaginatorName",
    "DescribeReservedDBInstancesPaginatorName",
    "DescribeSourceRegionsPaginatorName",
    "DownloadDBLogFilePortionPaginatorName",
    "EngineFamily",
    "FailoverStatus",
    "IAMAuthMode",
    "ReplicaMode",
    "SourceType",
    "TargetHealthReason",
    "TargetRole",
    "TargetState",
    "TargetType",
    "WriteForwardingStatus",
)


ActivityStreamMode = Literal["async", "sync"]
ActivityStreamStatus = Literal["started", "starting", "stopped", "stopping"]
ApplyMethod = Literal["immediate", "pending-reboot"]
AuthScheme = Literal["SECRETS"]
DBClusterSnapshotAvailableWaiterName = Literal["db_cluster_snapshot_available"]
DBClusterSnapshotDeletedWaiterName = Literal["db_cluster_snapshot_deleted"]
DBInstanceAvailableWaiterName = Literal["db_instance_available"]
DBInstanceDeletedWaiterName = Literal["db_instance_deleted"]
DBProxyEndpointStatus = Literal[
    "available",
    "creating",
    "deleting",
    "incompatible-network",
    "insufficient-resource-limits",
    "modifying",
]
DBProxyEndpointTargetRole = Literal["READ_ONLY", "READ_WRITE"]
DBProxyStatus = Literal[
    "available",
    "creating",
    "deleting",
    "incompatible-network",
    "insufficient-resource-limits",
    "modifying",
    "reactivating",
    "suspended",
    "suspending",
]
DBSnapshotAvailableWaiterName = Literal["db_snapshot_available"]
DBSnapshotCompletedWaiterName = Literal["db_snapshot_completed"]
DBSnapshotDeletedWaiterName = Literal["db_snapshot_deleted"]
DescribeCertificatesPaginatorName = Literal["describe_certificates"]
DescribeCustomAvailabilityZonesPaginatorName = Literal["describe_custom_availability_zones"]
DescribeDBClusterBacktracksPaginatorName = Literal["describe_db_cluster_backtracks"]
DescribeDBClusterEndpointsPaginatorName = Literal["describe_db_cluster_endpoints"]
DescribeDBClusterParameterGroupsPaginatorName = Literal["describe_db_cluster_parameter_groups"]
DescribeDBClusterParametersPaginatorName = Literal["describe_db_cluster_parameters"]
DescribeDBClusterSnapshotsPaginatorName = Literal["describe_db_cluster_snapshots"]
DescribeDBClustersPaginatorName = Literal["describe_db_clusters"]
DescribeDBEngineVersionsPaginatorName = Literal["describe_db_engine_versions"]
DescribeDBInstanceAutomatedBackupsPaginatorName = Literal["describe_db_instance_automated_backups"]
DescribeDBInstancesPaginatorName = Literal["describe_db_instances"]
DescribeDBLogFilesPaginatorName = Literal["describe_db_log_files"]
DescribeDBParameterGroupsPaginatorName = Literal["describe_db_parameter_groups"]
DescribeDBParametersPaginatorName = Literal["describe_db_parameters"]
DescribeDBProxiesPaginatorName = Literal["describe_db_proxies"]
DescribeDBProxyEndpointsPaginatorName = Literal["describe_db_proxy_endpoints"]
DescribeDBProxyTargetGroupsPaginatorName = Literal["describe_db_proxy_target_groups"]
DescribeDBProxyTargetsPaginatorName = Literal["describe_db_proxy_targets"]
DescribeDBSecurityGroupsPaginatorName = Literal["describe_db_security_groups"]
DescribeDBSnapshotsPaginatorName = Literal["describe_db_snapshots"]
DescribeDBSubnetGroupsPaginatorName = Literal["describe_db_subnet_groups"]
DescribeEngineDefaultClusterParametersPaginatorName = Literal[
    "describe_engine_default_cluster_parameters"
]
DescribeEngineDefaultParametersPaginatorName = Literal["describe_engine_default_parameters"]
DescribeEventSubscriptionsPaginatorName = Literal["describe_event_subscriptions"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeExportTasksPaginatorName = Literal["describe_export_tasks"]
DescribeGlobalClustersPaginatorName = Literal["describe_global_clusters"]
DescribeInstallationMediaPaginatorName = Literal["describe_installation_media"]
DescribeOptionGroupOptionsPaginatorName = Literal["describe_option_group_options"]
DescribeOptionGroupsPaginatorName = Literal["describe_option_groups"]
DescribeOrderableDBInstanceOptionsPaginatorName = Literal["describe_orderable_db_instance_options"]
DescribePendingMaintenanceActionsPaginatorName = Literal["describe_pending_maintenance_actions"]
DescribeReservedDBInstancesOfferingsPaginatorName = Literal[
    "describe_reserved_db_instances_offerings"
]
DescribeReservedDBInstancesPaginatorName = Literal["describe_reserved_db_instances"]
DescribeSourceRegionsPaginatorName = Literal["describe_source_regions"]
DownloadDBLogFilePortionPaginatorName = Literal["download_db_log_file_portion"]
EngineFamily = Literal["MYSQL", "POSTGRESQL"]
FailoverStatus = Literal["cancelling", "failing-over", "pending"]
IAMAuthMode = Literal["DISABLED", "REQUIRED"]
ReplicaMode = Literal["mounted", "open-read-only"]
SourceType = Literal[
    "db-cluster",
    "db-cluster-snapshot",
    "db-instance",
    "db-parameter-group",
    "db-security-group",
    "db-snapshot",
]
TargetHealthReason = Literal[
    "AUTH_FAILURE",
    "CONNECTION_FAILED",
    "INVALID_REPLICATION_STATE",
    "PENDING_PROXY_CAPACITY",
    "UNREACHABLE",
]
TargetRole = Literal["READ_ONLY", "READ_WRITE", "UNKNOWN"]
TargetState = Literal["AVAILABLE", "REGISTERING", "UNAVAILABLE"]
TargetType = Literal["RDS_INSTANCE", "RDS_SERVERLESS_ENDPOINT", "TRACKED_CLUSTER"]
WriteForwardingStatus = Literal["disabled", "disabling", "enabled", "enabling", "unknown"]
