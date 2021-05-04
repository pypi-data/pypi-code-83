"""
Type annotations for elasticache service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticache/literals.html)

Usage::

    ```python
    from mypy_boto3_elasticache.literals import AZMode

    data: AZMode = "cross-az"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AZMode",
    "AuthTokenUpdateStatus",
    "AuthTokenUpdateStrategyType",
    "AuthenticationType",
    "AutomaticFailoverStatus",
    "CacheClusterAvailableWaiterName",
    "CacheClusterDeletedWaiterName",
    "ChangeType",
    "DescribeCacheClustersPaginatorName",
    "DescribeCacheEngineVersionsPaginatorName",
    "DescribeCacheParameterGroupsPaginatorName",
    "DescribeCacheParametersPaginatorName",
    "DescribeCacheSecurityGroupsPaginatorName",
    "DescribeCacheSubnetGroupsPaginatorName",
    "DescribeEngineDefaultParametersPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeGlobalReplicationGroupsPaginatorName",
    "DescribeReplicationGroupsPaginatorName",
    "DescribeReservedCacheNodesOfferingsPaginatorName",
    "DescribeReservedCacheNodesPaginatorName",
    "DescribeServiceUpdatesPaginatorName",
    "DescribeSnapshotsPaginatorName",
    "DescribeUpdateActionsPaginatorName",
    "DescribeUserGroupsPaginatorName",
    "DescribeUsersPaginatorName",
    "DestinationType",
    "LogDeliveryConfigurationStatus",
    "LogFormat",
    "LogType",
    "MultiAZStatus",
    "NodeUpdateInitiatedBy",
    "NodeUpdateStatus",
    "OutpostMode",
    "PendingAutomaticFailoverStatus",
    "ReplicationGroupAvailableWaiterName",
    "ReplicationGroupDeletedWaiterName",
    "ServiceUpdateSeverity",
    "ServiceUpdateStatus",
    "ServiceUpdateType",
    "SlaMet",
    "SourceType",
    "UpdateActionStatus",
)


AZMode = Literal["cross-az", "single-az"]
AuthTokenUpdateStatus = Literal["ROTATING", "SETTING"]
AuthTokenUpdateStrategyType = Literal["DELETE", "ROTATE", "SET"]
AuthenticationType = Literal["no-password", "password"]
AutomaticFailoverStatus = Literal["disabled", "disabling", "enabled", "enabling"]
CacheClusterAvailableWaiterName = Literal["cache_cluster_available"]
CacheClusterDeletedWaiterName = Literal["cache_cluster_deleted"]
ChangeType = Literal["immediate", "requires-reboot"]
DescribeCacheClustersPaginatorName = Literal["describe_cache_clusters"]
DescribeCacheEngineVersionsPaginatorName = Literal["describe_cache_engine_versions"]
DescribeCacheParameterGroupsPaginatorName = Literal["describe_cache_parameter_groups"]
DescribeCacheParametersPaginatorName = Literal["describe_cache_parameters"]
DescribeCacheSecurityGroupsPaginatorName = Literal["describe_cache_security_groups"]
DescribeCacheSubnetGroupsPaginatorName = Literal["describe_cache_subnet_groups"]
DescribeEngineDefaultParametersPaginatorName = Literal["describe_engine_default_parameters"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeGlobalReplicationGroupsPaginatorName = Literal["describe_global_replication_groups"]
DescribeReplicationGroupsPaginatorName = Literal["describe_replication_groups"]
DescribeReservedCacheNodesOfferingsPaginatorName = Literal[
    "describe_reserved_cache_nodes_offerings"
]
DescribeReservedCacheNodesPaginatorName = Literal["describe_reserved_cache_nodes"]
DescribeServiceUpdatesPaginatorName = Literal["describe_service_updates"]
DescribeSnapshotsPaginatorName = Literal["describe_snapshots"]
DescribeUpdateActionsPaginatorName = Literal["describe_update_actions"]
DescribeUserGroupsPaginatorName = Literal["describe_user_groups"]
DescribeUsersPaginatorName = Literal["describe_users"]
DestinationType = Literal["cloudwatch-logs", "kinesis-firehose"]
LogDeliveryConfigurationStatus = Literal["active", "disabling", "enabling", "error", "modifying"]
LogFormat = Literal["json", "text"]
LogType = Literal["slow-log"]
MultiAZStatus = Literal["disabled", "enabled"]
NodeUpdateInitiatedBy = Literal["customer", "system"]
NodeUpdateStatus = Literal[
    "complete", "in-progress", "not-applied", "stopped", "stopping", "waiting-to-start"
]
OutpostMode = Literal["cross-outpost", "single-outpost"]
PendingAutomaticFailoverStatus = Literal["disabled", "enabled"]
ReplicationGroupAvailableWaiterName = Literal["replication_group_available"]
ReplicationGroupDeletedWaiterName = Literal["replication_group_deleted"]
ServiceUpdateSeverity = Literal["critical", "important", "low", "medium"]
ServiceUpdateStatus = Literal["available", "cancelled", "expired"]
ServiceUpdateType = Literal["security-update"]
SlaMet = Literal["n/a", "no", "yes"]
SourceType = Literal[
    "cache-cluster",
    "cache-parameter-group",
    "cache-security-group",
    "cache-subnet-group",
    "replication-group",
    "user",
    "user-group",
]
UpdateActionStatus = Literal[
    "complete",
    "in-progress",
    "not-applicable",
    "not-applied",
    "scheduled",
    "scheduling",
    "stopped",
    "stopping",
    "waiting-to-start",
]
