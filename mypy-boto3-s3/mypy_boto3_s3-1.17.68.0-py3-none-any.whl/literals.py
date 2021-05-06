"""
Type annotations for s3 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/literals.html)

Usage::

    ```python
    from mypy_boto3_s3.literals import AnalyticsS3ExportFileFormat

    data: AnalyticsS3ExportFileFormat = "CSV"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AnalyticsS3ExportFileFormat",
    "ArchiveStatus",
    "BucketAccelerateStatus",
    "BucketCannedACL",
    "BucketExistsWaiterName",
    "BucketLocationConstraint",
    "BucketLogsPermission",
    "BucketNotExistsWaiterName",
    "BucketVersioningStatus",
    "CompressionType",
    "DeleteMarkerReplicationStatus",
    "EncodingType",
    "Event",
    "ExistingObjectReplicationStatus",
    "ExpirationStatus",
    "ExpressionType",
    "FileHeaderInfo",
    "FilterRuleName",
    "IntelligentTieringAccessTier",
    "IntelligentTieringStatus",
    "InventoryFormat",
    "InventoryFrequency",
    "InventoryIncludedObjectVersions",
    "InventoryOptionalField",
    "JSONType",
    "ListMultipartUploadsPaginatorName",
    "ListObjectVersionsPaginatorName",
    "ListObjectsPaginatorName",
    "ListObjectsV2PaginatorName",
    "ListPartsPaginatorName",
    "MFADelete",
    "MFADeleteStatus",
    "MetadataDirective",
    "MetricsStatus",
    "ObjectCannedACL",
    "ObjectExistsWaiterName",
    "ObjectLockEnabled",
    "ObjectLockLegalHoldStatus",
    "ObjectLockMode",
    "ObjectLockRetentionMode",
    "ObjectNotExistsWaiterName",
    "ObjectOwnership",
    "ObjectStorageClass",
    "ObjectVersionStorageClass",
    "OwnerOverride",
    "Payer",
    "Permission",
    "ProtocolType",
    "QuoteFields",
    "ReplicaModificationsStatus",
    "ReplicationRuleStatus",
    "ReplicationStatus",
    "ReplicationTimeStatus",
    "RequestCharged",
    "RequestPayer",
    "RestoreRequestType",
    "ServerSideEncryption",
    "SseKmsEncryptedObjectsStatus",
    "StorageClass",
    "StorageClassAnalysisSchemaVersion",
    "TaggingDirective",
    "Tier",
    "TransitionStorageClass",
    "TypeType",
)


AnalyticsS3ExportFileFormat = Literal["CSV"]
ArchiveStatus = Literal["ARCHIVE_ACCESS", "DEEP_ARCHIVE_ACCESS"]
BucketAccelerateStatus = Literal["Enabled", "Suspended"]
BucketCannedACL = Literal["authenticated-read", "private", "public-read", "public-read-write"]
BucketExistsWaiterName = Literal["bucket_exists"]
BucketLocationConstraint = Literal[
    "EU",
    "af-south-1",
    "ap-east-1",
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-northeast-3",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "cn-north-1",
    "cn-northwest-1",
    "eu-central-1",
    "eu-north-1",
    "eu-south-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "me-south-1",
    "sa-east-1",
    "us-east-2",
    "us-gov-east-1",
    "us-gov-west-1",
    "us-west-1",
    "us-west-2",
]
BucketLogsPermission = Literal["FULL_CONTROL", "READ", "WRITE"]
BucketNotExistsWaiterName = Literal["bucket_not_exists"]
BucketVersioningStatus = Literal["Enabled", "Suspended"]
CompressionType = Literal["BZIP2", "GZIP", "NONE"]
DeleteMarkerReplicationStatus = Literal["Disabled", "Enabled"]
EncodingType = Literal["url"]
Event = Literal[
    "s3:ObjectCreated:*",
    "s3:ObjectCreated:CompleteMultipartUpload",
    "s3:ObjectCreated:Copy",
    "s3:ObjectCreated:Post",
    "s3:ObjectCreated:Put",
    "s3:ObjectRemoved:*",
    "s3:ObjectRemoved:Delete",
    "s3:ObjectRemoved:DeleteMarkerCreated",
    "s3:ObjectRestore:*",
    "s3:ObjectRestore:Completed",
    "s3:ObjectRestore:Post",
    "s3:ReducedRedundancyLostObject",
    "s3:Replication:*",
    "s3:Replication:OperationFailedReplication",
    "s3:Replication:OperationMissedThreshold",
    "s3:Replication:OperationNotTracked",
    "s3:Replication:OperationReplicatedAfterThreshold",
]
ExistingObjectReplicationStatus = Literal["Disabled", "Enabled"]
ExpirationStatus = Literal["Disabled", "Enabled"]
ExpressionType = Literal["SQL"]
FileHeaderInfo = Literal["IGNORE", "NONE", "USE"]
FilterRuleName = Literal["prefix", "suffix"]
IntelligentTieringAccessTier = Literal["ARCHIVE_ACCESS", "DEEP_ARCHIVE_ACCESS"]
IntelligentTieringStatus = Literal["Disabled", "Enabled"]
InventoryFormat = Literal["CSV", "ORC", "Parquet"]
InventoryFrequency = Literal["Daily", "Weekly"]
InventoryIncludedObjectVersions = Literal["All", "Current"]
InventoryOptionalField = Literal[
    "ETag",
    "EncryptionStatus",
    "IntelligentTieringAccessTier",
    "IsMultipartUploaded",
    "LastModifiedDate",
    "ObjectLockLegalHoldStatus",
    "ObjectLockMode",
    "ObjectLockRetainUntilDate",
    "ReplicationStatus",
    "Size",
    "StorageClass",
]
JSONType = Literal["DOCUMENT", "LINES"]
ListMultipartUploadsPaginatorName = Literal["list_multipart_uploads"]
ListObjectVersionsPaginatorName = Literal["list_object_versions"]
ListObjectsPaginatorName = Literal["list_objects"]
ListObjectsV2PaginatorName = Literal["list_objects_v2"]
ListPartsPaginatorName = Literal["list_parts"]
MFADelete = Literal["Disabled", "Enabled"]
MFADeleteStatus = Literal["Disabled", "Enabled"]
MetadataDirective = Literal["COPY", "REPLACE"]
MetricsStatus = Literal["Disabled", "Enabled"]
ObjectCannedACL = Literal[
    "authenticated-read",
    "aws-exec-read",
    "bucket-owner-full-control",
    "bucket-owner-read",
    "private",
    "public-read",
    "public-read-write",
]
ObjectExistsWaiterName = Literal["object_exists"]
ObjectLockEnabled = Literal["Enabled"]
ObjectLockLegalHoldStatus = Literal["OFF", "ON"]
ObjectLockMode = Literal["COMPLIANCE", "GOVERNANCE"]
ObjectLockRetentionMode = Literal["COMPLIANCE", "GOVERNANCE"]
ObjectNotExistsWaiterName = Literal["object_not_exists"]
ObjectOwnership = Literal["BucketOwnerPreferred", "ObjectWriter"]
ObjectStorageClass = Literal[
    "DEEP_ARCHIVE",
    "GLACIER",
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "OUTPOSTS",
    "REDUCED_REDUNDANCY",
    "STANDARD",
    "STANDARD_IA",
]
ObjectVersionStorageClass = Literal["STANDARD"]
OwnerOverride = Literal["Destination"]
Payer = Literal["BucketOwner", "Requester"]
Permission = Literal["FULL_CONTROL", "READ", "READ_ACP", "WRITE", "WRITE_ACP"]
ProtocolType = Literal["http", "https"]
QuoteFields = Literal["ALWAYS", "ASNEEDED"]
ReplicaModificationsStatus = Literal["Disabled", "Enabled"]
ReplicationRuleStatus = Literal["Disabled", "Enabled"]
ReplicationStatus = Literal["COMPLETE", "FAILED", "PENDING", "REPLICA"]
ReplicationTimeStatus = Literal["Disabled", "Enabled"]
RequestCharged = Literal["requester"]
RequestPayer = Literal["requester"]
RestoreRequestType = Literal["SELECT"]
ServerSideEncryption = Literal["AES256", "aws:kms"]
SseKmsEncryptedObjectsStatus = Literal["Disabled", "Enabled"]
StorageClass = Literal[
    "DEEP_ARCHIVE",
    "GLACIER",
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "OUTPOSTS",
    "REDUCED_REDUNDANCY",
    "STANDARD",
    "STANDARD_IA",
]
StorageClassAnalysisSchemaVersion = Literal["V_1"]
TaggingDirective = Literal["COPY", "REPLACE"]
Tier = Literal["Bulk", "Expedited", "Standard"]
TransitionStorageClass = Literal[
    "DEEP_ARCHIVE", "GLACIER", "INTELLIGENT_TIERING", "ONEZONE_IA", "STANDARD_IA"
]
TypeType = Literal["AmazonCustomerByEmail", "CanonicalUser", "Group"]
