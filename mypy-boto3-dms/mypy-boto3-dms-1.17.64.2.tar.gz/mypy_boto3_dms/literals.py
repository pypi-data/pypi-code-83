"""
Type annotations for dms service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dms/literals.html)

Usage::

    ```python
    from mypy_boto3_dms.literals import AuthMechanismValue

    data: AuthMechanismValue = "default"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AuthMechanismValue",
    "AuthTypeValue",
    "CharLengthSemantics",
    "CompressionTypeValue",
    "DataFormatValue",
    "DatePartitionDelimiterValue",
    "DatePartitionSequenceValue",
    "DescribeCertificatesPaginatorName",
    "DescribeConnectionsPaginatorName",
    "DescribeEndpointTypesPaginatorName",
    "DescribeEndpointsPaginatorName",
    "DescribeEventSubscriptionsPaginatorName",
    "DescribeEventsPaginatorName",
    "DescribeOrderableReplicationInstancesPaginatorName",
    "DescribeReplicationInstancesPaginatorName",
    "DescribeReplicationSubnetGroupsPaginatorName",
    "DescribeReplicationTaskAssessmentResultsPaginatorName",
    "DescribeReplicationTasksPaginatorName",
    "DescribeSchemasPaginatorName",
    "DescribeTableStatisticsPaginatorName",
    "DmsSslModeValue",
    "EncodingTypeValue",
    "EncryptionModeValue",
    "EndpointDeletedWaiterName",
    "EndpointSettingTypeValue",
    "KafkaSecurityProtocol",
    "MessageFormatValue",
    "MigrationTypeValue",
    "NestingLevelValue",
    "ParquetVersionValue",
    "RefreshSchemasStatusTypeValue",
    "ReleaseStatusValues",
    "ReloadOptionValue",
    "ReplicationEndpointTypeValue",
    "ReplicationInstanceAvailableWaiterName",
    "ReplicationInstanceDeletedWaiterName",
    "ReplicationTaskDeletedWaiterName",
    "ReplicationTaskReadyWaiterName",
    "ReplicationTaskRunningWaiterName",
    "ReplicationTaskStoppedWaiterName",
    "SafeguardPolicy",
    "SourceType",
    "StartReplicationTaskTypeValue",
    "TargetDbType",
    "TestConnectionSucceedsWaiterName",
)


AuthMechanismValue = Literal["default", "mongodb_cr", "scram_sha_1"]
AuthTypeValue = Literal["no", "password"]
CharLengthSemantics = Literal["byte", "char", "default"]
CompressionTypeValue = Literal["gzip", "none"]
DataFormatValue = Literal["csv", "parquet"]
DatePartitionDelimiterValue = Literal["DASH", "NONE", "SLASH", "UNDERSCORE"]
DatePartitionSequenceValue = Literal["DDMMYYYY", "MMYYYYDD", "YYYYMM", "YYYYMMDD", "YYYYMMDDHH"]
DescribeCertificatesPaginatorName = Literal["describe_certificates"]
DescribeConnectionsPaginatorName = Literal["describe_connections"]
DescribeEndpointTypesPaginatorName = Literal["describe_endpoint_types"]
DescribeEndpointsPaginatorName = Literal["describe_endpoints"]
DescribeEventSubscriptionsPaginatorName = Literal["describe_event_subscriptions"]
DescribeEventsPaginatorName = Literal["describe_events"]
DescribeOrderableReplicationInstancesPaginatorName = Literal[
    "describe_orderable_replication_instances"
]
DescribeReplicationInstancesPaginatorName = Literal["describe_replication_instances"]
DescribeReplicationSubnetGroupsPaginatorName = Literal["describe_replication_subnet_groups"]
DescribeReplicationTaskAssessmentResultsPaginatorName = Literal[
    "describe_replication_task_assessment_results"
]
DescribeReplicationTasksPaginatorName = Literal["describe_replication_tasks"]
DescribeSchemasPaginatorName = Literal["describe_schemas"]
DescribeTableStatisticsPaginatorName = Literal["describe_table_statistics"]
DmsSslModeValue = Literal["none", "require", "verify-ca", "verify-full"]
EncodingTypeValue = Literal["plain", "plain-dictionary", "rle-dictionary"]
EncryptionModeValue = Literal["sse-kms", "sse-s3"]
EndpointDeletedWaiterName = Literal["endpoint_deleted"]
EndpointSettingTypeValue = Literal["boolean", "enum", "integer", "string"]
KafkaSecurityProtocol = Literal["plaintext", "sasl-ssl", "ssl-authentication", "ssl-encryption"]
MessageFormatValue = Literal["json", "json-unformatted"]
MigrationTypeValue = Literal["cdc", "full-load", "full-load-and-cdc"]
NestingLevelValue = Literal["none", "one"]
ParquetVersionValue = Literal["parquet-1-0", "parquet-2-0"]
RefreshSchemasStatusTypeValue = Literal["failed", "refreshing", "successful"]
ReleaseStatusValues = Literal["beta"]
ReloadOptionValue = Literal["data-reload", "validate-only"]
ReplicationEndpointTypeValue = Literal["source", "target"]
ReplicationInstanceAvailableWaiterName = Literal["replication_instance_available"]
ReplicationInstanceDeletedWaiterName = Literal["replication_instance_deleted"]
ReplicationTaskDeletedWaiterName = Literal["replication_task_deleted"]
ReplicationTaskReadyWaiterName = Literal["replication_task_ready"]
ReplicationTaskRunningWaiterName = Literal["replication_task_running"]
ReplicationTaskStoppedWaiterName = Literal["replication_task_stopped"]
SafeguardPolicy = Literal[
    "exclusive-automatic-truncation",
    "rely-on-sql-server-replication-agent",
    "shared-automatic-truncation",
]
SourceType = Literal["replication-instance"]
StartReplicationTaskTypeValue = Literal["reload-target", "resume-processing", "start-replication"]
TargetDbType = Literal["multiple-databases", "specific-database"]
TestConnectionSucceedsWaiterName = Literal["test_connection_succeeds"]
