"""
Type annotations for glue service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_glue/literals.html)

Usage::

    ```python
    from mypy_boto3_glue.literals import BackfillErrorCode

    data: BackfillErrorCode = "ENCRYPTED_PARTITION_ERROR"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BackfillErrorCode",
    "CatalogEncryptionMode",
    "CloudWatchEncryptionMode",
    "ColumnStatisticsType",
    "Comparator",
    "Compatibility",
    "ConnectionPropertyKey",
    "ConnectionType",
    "CrawlState",
    "CrawlerLineageSettings",
    "CrawlerState",
    "CsvHeaderOption",
    "DataFormat",
    "DeleteBehavior",
    "EnableHybridValues",
    "ExistCondition",
    "GetClassifiersPaginatorName",
    "GetConnectionsPaginatorName",
    "GetCrawlerMetricsPaginatorName",
    "GetCrawlersPaginatorName",
    "GetDatabasesPaginatorName",
    "GetDevEndpointsPaginatorName",
    "GetJobRunsPaginatorName",
    "GetJobsPaginatorName",
    "GetPartitionIndexesPaginatorName",
    "GetPartitionsPaginatorName",
    "GetResourcePoliciesPaginatorName",
    "GetSecurityConfigurationsPaginatorName",
    "GetTableVersionsPaginatorName",
    "GetTablesPaginatorName",
    "GetTriggersPaginatorName",
    "GetUserDefinedFunctionsPaginatorName",
    "JobBookmarksEncryptionMode",
    "JobRunState",
    "Language",
    "LastCrawlStatus",
    "ListRegistriesPaginatorName",
    "ListSchemaVersionsPaginatorName",
    "ListSchemasPaginatorName",
    "Logical",
    "LogicalOperator",
    "MLUserDataEncryptionModeString",
    "NodeType",
    "PartitionIndexStatus",
    "Permission",
    "PrincipalType",
    "RecrawlBehavior",
    "RegistryStatus",
    "ResourceShareType",
    "ResourceType",
    "S3EncryptionMode",
    "ScheduleState",
    "SchemaDiffType",
    "SchemaStatus",
    "SchemaVersionStatus",
    "Sort",
    "SortDirectionType",
    "TaskRunSortColumnType",
    "TaskStatusType",
    "TaskType",
    "TransformSortColumnType",
    "TransformStatusType",
    "TransformType",
    "TriggerState",
    "TriggerType",
    "UpdateBehavior",
    "WorkerType",
    "WorkflowRunStatus",
)


BackfillErrorCode = Literal[
    "ENCRYPTED_PARTITION_ERROR",
    "INTERNAL_ERROR",
    "INVALID_PARTITION_TYPE_DATA_ERROR",
    "MISSING_PARTITION_VALUE_ERROR",
    "UNSUPPORTED_PARTITION_CHARACTER_ERROR",
]
CatalogEncryptionMode = Literal["DISABLED", "SSE-KMS"]
CloudWatchEncryptionMode = Literal["DISABLED", "SSE-KMS"]
ColumnStatisticsType = Literal["BINARY", "BOOLEAN", "DATE", "DECIMAL", "DOUBLE", "LONG", "STRING"]
Comparator = Literal[
    "EQUALS", "GREATER_THAN", "GREATER_THAN_EQUALS", "LESS_THAN", "LESS_THAN_EQUALS"
]
Compatibility = Literal[
    "BACKWARD", "BACKWARD_ALL", "DISABLED", "FORWARD", "FORWARD_ALL", "FULL", "FULL_ALL", "NONE"
]
ConnectionPropertyKey = Literal[
    "CONFIG_FILES",
    "CONNECTION_URL",
    "CONNECTOR_CLASS_NAME",
    "CONNECTOR_TYPE",
    "CONNECTOR_URL",
    "CUSTOM_JDBC_CERT",
    "CUSTOM_JDBC_CERT_STRING",
    "ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD",
    "ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD",
    "ENCRYPTED_PASSWORD",
    "HOST",
    "INSTANCE_ID",
    "JDBC_CONNECTION_URL",
    "JDBC_DRIVER_CLASS_NAME",
    "JDBC_DRIVER_JAR_URI",
    "JDBC_ENFORCE_SSL",
    "JDBC_ENGINE",
    "JDBC_ENGINE_VERSION",
    "KAFKA_BOOTSTRAP_SERVERS",
    "KAFKA_CLIENT_KEYSTORE",
    "KAFKA_CLIENT_KEYSTORE_PASSWORD",
    "KAFKA_CLIENT_KEY_PASSWORD",
    "KAFKA_CUSTOM_CERT",
    "KAFKA_SKIP_CUSTOM_CERT_VALIDATION",
    "KAFKA_SSL_ENABLED",
    "PASSWORD",
    "PORT",
    "SECRET_ID",
    "SKIP_CUSTOM_JDBC_CERT_VALIDATION",
    "USERNAME",
]
ConnectionType = Literal["CUSTOM", "JDBC", "KAFKA", "MARKETPLACE", "MONGODB", "NETWORK", "SFTP"]
CrawlState = Literal["CANCELLED", "CANCELLING", "FAILED", "RUNNING", "SUCCEEDED"]
CrawlerLineageSettings = Literal["DISABLE", "ENABLE"]
CrawlerState = Literal["READY", "RUNNING", "STOPPING"]
CsvHeaderOption = Literal["ABSENT", "PRESENT", "UNKNOWN"]
DataFormat = Literal["AVRO"]
DeleteBehavior = Literal["DELETE_FROM_DATABASE", "DEPRECATE_IN_DATABASE", "LOG"]
EnableHybridValues = Literal["FALSE", "TRUE"]
ExistCondition = Literal["MUST_EXIST", "NONE", "NOT_EXIST"]
GetClassifiersPaginatorName = Literal["get_classifiers"]
GetConnectionsPaginatorName = Literal["get_connections"]
GetCrawlerMetricsPaginatorName = Literal["get_crawler_metrics"]
GetCrawlersPaginatorName = Literal["get_crawlers"]
GetDatabasesPaginatorName = Literal["get_databases"]
GetDevEndpointsPaginatorName = Literal["get_dev_endpoints"]
GetJobRunsPaginatorName = Literal["get_job_runs"]
GetJobsPaginatorName = Literal["get_jobs"]
GetPartitionIndexesPaginatorName = Literal["get_partition_indexes"]
GetPartitionsPaginatorName = Literal["get_partitions"]
GetResourcePoliciesPaginatorName = Literal["get_resource_policies"]
GetSecurityConfigurationsPaginatorName = Literal["get_security_configurations"]
GetTableVersionsPaginatorName = Literal["get_table_versions"]
GetTablesPaginatorName = Literal["get_tables"]
GetTriggersPaginatorName = Literal["get_triggers"]
GetUserDefinedFunctionsPaginatorName = Literal["get_user_defined_functions"]
JobBookmarksEncryptionMode = Literal["CSE-KMS", "DISABLED"]
JobRunState = Literal[
    "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "SUCCEEDED", "TIMEOUT"
]
Language = Literal["PYTHON", "SCALA"]
LastCrawlStatus = Literal["CANCELLED", "FAILED", "SUCCEEDED"]
ListRegistriesPaginatorName = Literal["list_registries"]
ListSchemaVersionsPaginatorName = Literal["list_schema_versions"]
ListSchemasPaginatorName = Literal["list_schemas"]
Logical = Literal["AND", "ANY"]
LogicalOperator = Literal["EQUALS"]
MLUserDataEncryptionModeString = Literal["DISABLED", "SSE-KMS"]
NodeType = Literal["CRAWLER", "JOB", "TRIGGER"]
PartitionIndexStatus = Literal["ACTIVE", "CREATING", "DELETING", "FAILED"]
Permission = Literal[
    "ALL",
    "ALTER",
    "CREATE_DATABASE",
    "CREATE_TABLE",
    "DATA_LOCATION_ACCESS",
    "DELETE",
    "DROP",
    "INSERT",
    "SELECT",
]
PrincipalType = Literal["GROUP", "ROLE", "USER"]
RecrawlBehavior = Literal["CRAWL_EVERYTHING", "CRAWL_NEW_FOLDERS_ONLY"]
RegistryStatus = Literal["AVAILABLE", "DELETING"]
ResourceShareType = Literal["ALL", "FOREIGN"]
ResourceType = Literal["ARCHIVE", "FILE", "JAR"]
S3EncryptionMode = Literal["DISABLED", "SSE-KMS", "SSE-S3"]
ScheduleState = Literal["NOT_SCHEDULED", "SCHEDULED", "TRANSITIONING"]
SchemaDiffType = Literal["SYNTAX_DIFF"]
SchemaStatus = Literal["AVAILABLE", "DELETING", "PENDING"]
SchemaVersionStatus = Literal["AVAILABLE", "DELETING", "FAILURE", "PENDING"]
Sort = Literal["ASC", "DESC"]
SortDirectionType = Literal["ASCENDING", "DESCENDING"]
TaskRunSortColumnType = Literal["STARTED", "STATUS", "TASK_RUN_TYPE"]
TaskStatusType = Literal[
    "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "SUCCEEDED", "TIMEOUT"
]
TaskType = Literal[
    "EVALUATION", "EXPORT_LABELS", "FIND_MATCHES", "IMPORT_LABELS", "LABELING_SET_GENERATION"
]
TransformSortColumnType = Literal["CREATED", "LAST_MODIFIED", "NAME", "STATUS", "TRANSFORM_TYPE"]
TransformStatusType = Literal["DELETING", "NOT_READY", "READY"]
TransformType = Literal["FIND_MATCHES"]
TriggerState = Literal[
    "ACTIVATED",
    "ACTIVATING",
    "CREATED",
    "CREATING",
    "DEACTIVATED",
    "DEACTIVATING",
    "DELETING",
    "UPDATING",
]
TriggerType = Literal["CONDITIONAL", "ON_DEMAND", "SCHEDULED"]
UpdateBehavior = Literal["LOG", "UPDATE_IN_DATABASE"]
WorkerType = Literal["G.1X", "G.2X", "Standard"]
WorkflowRunStatus = Literal["COMPLETED", "ERROR", "RUNNING", "STOPPED", "STOPPING"]
