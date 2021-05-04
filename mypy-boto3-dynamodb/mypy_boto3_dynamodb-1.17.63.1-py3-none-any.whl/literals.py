"""
Type annotations for dynamodb service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/literals.html)

Usage::

    ```python
    from mypy_boto3_dynamodb.literals import AttributeAction

    data: AttributeAction = "ADD"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AttributeAction",
    "BackupStatus",
    "BackupType",
    "BackupTypeFilter",
    "BatchStatementErrorCodeEnum",
    "BillingMode",
    "ComparisonOperator",
    "ConditionalOperator",
    "ContinuousBackupsStatus",
    "ContributorInsightsAction",
    "ContributorInsightsStatus",
    "DestinationStatus",
    "ExportFormat",
    "ExportStatus",
    "GlobalTableStatus",
    "IndexStatus",
    "KeyType",
    "ListBackupsPaginatorName",
    "ListTablesPaginatorName",
    "ListTagsOfResourcePaginatorName",
    "PointInTimeRecoveryStatus",
    "ProjectionType",
    "QueryPaginatorName",
    "ReplicaStatus",
    "ReturnConsumedCapacity",
    "ReturnItemCollectionMetrics",
    "ReturnValue",
    "ReturnValuesOnConditionCheckFailure",
    "S3SseAlgorithm",
    "SSEStatus",
    "SSEType",
    "ScalarAttributeType",
    "ScanPaginatorName",
    "Select",
    "StreamViewType",
    "TableExistsWaiterName",
    "TableNotExistsWaiterName",
    "TableStatus",
    "TimeToLiveStatus",
)


AttributeAction = Literal["ADD", "DELETE", "PUT"]
BackupStatus = Literal["AVAILABLE", "CREATING", "DELETED"]
BackupType = Literal["AWS_BACKUP", "SYSTEM", "USER"]
BackupTypeFilter = Literal["ALL", "AWS_BACKUP", "SYSTEM", "USER"]
BatchStatementErrorCodeEnum = Literal[
    "AccessDenied",
    "ConditionalCheckFailed",
    "DuplicateItem",
    "InternalServerError",
    "ItemCollectionSizeLimitExceeded",
    "ProvisionedThroughputExceeded",
    "RequestLimitExceeded",
    "ResourceNotFound",
    "ThrottlingError",
    "TransactionConflict",
    "ValidationError",
]
BillingMode = Literal["PAY_PER_REQUEST", "PROVISIONED"]
ComparisonOperator = Literal[
    "BEGINS_WITH",
    "BETWEEN",
    "CONTAINS",
    "EQ",
    "GE",
    "GT",
    "IN",
    "LE",
    "LT",
    "NE",
    "NOT_CONTAINS",
    "NOT_NULL",
    "NULL",
]
ConditionalOperator = Literal["AND", "OR"]
ContinuousBackupsStatus = Literal["DISABLED", "ENABLED"]
ContributorInsightsAction = Literal["DISABLE", "ENABLE"]
ContributorInsightsStatus = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING", "FAILED"]
DestinationStatus = Literal["ACTIVE", "DISABLED", "DISABLING", "ENABLE_FAILED", "ENABLING"]
ExportFormat = Literal["DYNAMODB_JSON", "ION"]
ExportStatus = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
GlobalTableStatus = Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
IndexStatus = Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
KeyType = Literal["HASH", "RANGE"]
ListBackupsPaginatorName = Literal["list_backups"]
ListTablesPaginatorName = Literal["list_tables"]
ListTagsOfResourcePaginatorName = Literal["list_tags_of_resource"]
PointInTimeRecoveryStatus = Literal["DISABLED", "ENABLED"]
ProjectionType = Literal["ALL", "INCLUDE", "KEYS_ONLY"]
QueryPaginatorName = Literal["query"]
ReplicaStatus = Literal[
    "ACTIVE",
    "CREATING",
    "CREATION_FAILED",
    "DELETING",
    "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
    "REGION_DISABLED",
    "UPDATING",
]
ReturnConsumedCapacity = Literal["INDEXES", "NONE", "TOTAL"]
ReturnItemCollectionMetrics = Literal["NONE", "SIZE"]
ReturnValue = Literal["ALL_NEW", "ALL_OLD", "NONE", "UPDATED_NEW", "UPDATED_OLD"]
ReturnValuesOnConditionCheckFailure = Literal["ALL_OLD", "NONE"]
S3SseAlgorithm = Literal["AES256", "KMS"]
SSEStatus = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING", "UPDATING"]
SSEType = Literal["AES256", "KMS"]
ScalarAttributeType = Literal["B", "N", "S"]
ScanPaginatorName = Literal["scan"]
Select = Literal["ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "COUNT", "SPECIFIC_ATTRIBUTES"]
StreamViewType = Literal["KEYS_ONLY", "NEW_AND_OLD_IMAGES", "NEW_IMAGE", "OLD_IMAGE"]
TableExistsWaiterName = Literal["table_exists"]
TableNotExistsWaiterName = Literal["table_not_exists"]
TableStatus = Literal[
    "ACTIVE",
    "ARCHIVED",
    "ARCHIVING",
    "CREATING",
    "DELETING",
    "INACCESSIBLE_ENCRYPTION_CREDENTIALS",
    "UPDATING",
]
TimeToLiveStatus = Literal["DISABLED", "DISABLING", "ENABLED", "ENABLING"]
