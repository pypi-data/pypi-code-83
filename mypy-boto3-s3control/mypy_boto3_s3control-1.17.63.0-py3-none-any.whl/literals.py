"""
Type annotations for s3control service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/literals.html)

Usage::

    ```python
    from mypy_boto3_s3control.literals import BucketCannedACL

    data: BucketCannedACL = "authenticated-read"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BucketCannedACL",
    "BucketLocationConstraint",
    "ExpirationStatus",
    "Format",
    "JobManifestFieldName",
    "JobManifestFormat",
    "JobReportFormat",
    "JobReportScope",
    "JobStatus",
    "ListAccessPointsForObjectLambdaPaginatorName",
    "NetworkOrigin",
    "ObjectLambdaAllowedFeature",
    "ObjectLambdaTransformationConfigurationAction",
    "OperationName",
    "OutputSchemaVersion",
    "RequestedJobStatus",
    "S3CannedAccessControlList",
    "S3GlacierJobTier",
    "S3GranteeTypeIdentifier",
    "S3MetadataDirective",
    "S3ObjectLockLegalHoldStatus",
    "S3ObjectLockMode",
    "S3ObjectLockRetentionMode",
    "S3Permission",
    "S3SSEAlgorithm",
    "S3StorageClass",
    "TransitionStorageClass",
)


BucketCannedACL = Literal["authenticated-read", "private", "public-read", "public-read-write"]
BucketLocationConstraint = Literal[
    "EU",
    "ap-northeast-1",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "cn-north-1",
    "eu-central-1",
    "eu-west-1",
    "sa-east-1",
    "us-west-1",
    "us-west-2",
]
ExpirationStatus = Literal["Disabled", "Enabled"]
Format = Literal["CSV", "Parquet"]
JobManifestFieldName = Literal["Bucket", "Ignore", "Key", "VersionId"]
JobManifestFormat = Literal["S3BatchOperations_CSV_20180820", "S3InventoryReport_CSV_20161130"]
JobReportFormat = Literal["Report_CSV_20180820"]
JobReportScope = Literal["AllTasks", "FailedTasksOnly"]
JobStatus = Literal[
    "Active",
    "Cancelled",
    "Cancelling",
    "Complete",
    "Completing",
    "Failed",
    "Failing",
    "New",
    "Paused",
    "Pausing",
    "Preparing",
    "Ready",
    "Suspended",
]
ListAccessPointsForObjectLambdaPaginatorName = Literal["list_access_points_for_object_lambda"]
NetworkOrigin = Literal["Internet", "VPC"]
ObjectLambdaAllowedFeature = Literal["GetObject-PartNumber", "GetObject-Range"]
ObjectLambdaTransformationConfigurationAction = Literal["GetObject"]
OperationName = Literal[
    "LambdaInvoke",
    "S3DeleteObjectTagging",
    "S3InitiateRestoreObject",
    "S3PutObjectAcl",
    "S3PutObjectCopy",
    "S3PutObjectLegalHold",
    "S3PutObjectRetention",
    "S3PutObjectTagging",
]
OutputSchemaVersion = Literal["V_1"]
RequestedJobStatus = Literal["Cancelled", "Ready"]
S3CannedAccessControlList = Literal[
    "authenticated-read",
    "aws-exec-read",
    "bucket-owner-full-control",
    "bucket-owner-read",
    "private",
    "public-read",
    "public-read-write",
]
S3GlacierJobTier = Literal["BULK", "STANDARD"]
S3GranteeTypeIdentifier = Literal["emailAddress", "id", "uri"]
S3MetadataDirective = Literal["COPY", "REPLACE"]
S3ObjectLockLegalHoldStatus = Literal["OFF", "ON"]
S3ObjectLockMode = Literal["COMPLIANCE", "GOVERNANCE"]
S3ObjectLockRetentionMode = Literal["COMPLIANCE", "GOVERNANCE"]
S3Permission = Literal["FULL_CONTROL", "READ", "READ_ACP", "WRITE", "WRITE_ACP"]
S3SSEAlgorithm = Literal["AES256", "KMS"]
S3StorageClass = Literal[
    "DEEP_ARCHIVE", "GLACIER", "INTELLIGENT_TIERING", "ONEZONE_IA", "STANDARD", "STANDARD_IA"
]
TransitionStorageClass = Literal[
    "DEEP_ARCHIVE", "GLACIER", "INTELLIGENT_TIERING", "ONEZONE_IA", "STANDARD_IA"
]
