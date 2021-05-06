"""
Type annotations for s3 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3/type_defs.html)

Usage::

    ```python
    from mypy_boto3_s3.type_defs import AbortIncompleteMultipartUploadTypeDef

    data: AbortIncompleteMultipartUploadTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from botocore.response import StreamingBody

from mypy_boto3_s3.literals import (
    ArchiveStatus,
    BucketAccelerateStatus,
    BucketLocationConstraint,
    BucketLogsPermission,
    BucketVersioningStatus,
    CompressionType,
    DeleteMarkerReplicationStatus,
    Event,
    ExistingObjectReplicationStatus,
    ExpirationStatus,
    FileHeaderInfo,
    FilterRuleName,
    IntelligentTieringAccessTier,
    IntelligentTieringStatus,
    InventoryFormat,
    InventoryFrequency,
    InventoryIncludedObjectVersions,
    InventoryOptionalField,
    JSONType,
    MetricsStatus,
    MFADelete,
    MFADeleteStatus,
    ObjectCannedACL,
    ObjectLockLegalHoldStatus,
    ObjectLockMode,
    ObjectLockRetentionMode,
    ObjectOwnership,
    ObjectStorageClass,
    Payer,
    Permission,
    ProtocolType,
    QuoteFields,
    ReplicaModificationsStatus,
    ReplicationRuleStatus,
    ReplicationStatus,
    ReplicationTimeStatus,
    ServerSideEncryption,
    SseKmsEncryptedObjectsStatus,
    StorageClass,
    Tier,
    TransitionStorageClass,
    TypeType,
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
    "AbortIncompleteMultipartUploadTypeDef",
    "AbortMultipartUploadOutputTypeDef",
    "AccelerateConfigurationTypeDef",
    "AccessControlPolicyTypeDef",
    "AccessControlTranslationTypeDef",
    "AnalyticsAndOperatorTypeDef",
    "AnalyticsConfigurationTypeDef",
    "AnalyticsExportDestinationTypeDef",
    "AnalyticsFilterTypeDef",
    "AnalyticsS3BucketDestinationTypeDef",
    "BucketLifecycleConfigurationTypeDef",
    "BucketLoggingStatusTypeDef",
    "BucketTypeDef",
    "CORSConfigurationTypeDef",
    "CORSRuleTypeDef",
    "CSVInputTypeDef",
    "CSVOutputTypeDef",
    "CloudFunctionConfigurationTypeDef",
    "CommonPrefixTypeDef",
    "CompleteMultipartUploadOutputTypeDef",
    "CompletedMultipartUploadTypeDef",
    "CompletedPartTypeDef",
    "ConditionTypeDef",
    "CopyObjectOutputTypeDef",
    "CopyObjectResultTypeDef",
    "CopyPartResultTypeDef",
    "CopySourceTypeDef",
    "CreateBucketConfigurationTypeDef",
    "CreateBucketOutputTypeDef",
    "CreateMultipartUploadOutputTypeDef",
    "DefaultRetentionTypeDef",
    "DeleteMarkerEntryTypeDef",
    "DeleteMarkerReplicationTypeDef",
    "DeleteObjectOutputTypeDef",
    "DeleteObjectTaggingOutputTypeDef",
    "DeleteObjectsOutputTypeDef",
    "DeleteTypeDef",
    "DeletedObjectTypeDef",
    "DestinationTypeDef",
    "EncryptionConfigurationTypeDef",
    "EncryptionTypeDef",
    "ErrorDocumentTypeDef",
    "ErrorTypeDef",
    "ExistingObjectReplicationTypeDef",
    "FilterRuleTypeDef",
    "GetBucketAccelerateConfigurationOutputTypeDef",
    "GetBucketAclOutputTypeDef",
    "GetBucketAnalyticsConfigurationOutputTypeDef",
    "GetBucketCorsOutputTypeDef",
    "GetBucketEncryptionOutputTypeDef",
    "GetBucketIntelligentTieringConfigurationOutputTypeDef",
    "GetBucketInventoryConfigurationOutputTypeDef",
    "GetBucketLifecycleConfigurationOutputTypeDef",
    "GetBucketLifecycleOutputTypeDef",
    "GetBucketLocationOutputTypeDef",
    "GetBucketLoggingOutputTypeDef",
    "GetBucketMetricsConfigurationOutputTypeDef",
    "GetBucketOwnershipControlsOutputTypeDef",
    "GetBucketPolicyOutputTypeDef",
    "GetBucketPolicyStatusOutputTypeDef",
    "GetBucketReplicationOutputTypeDef",
    "GetBucketRequestPaymentOutputTypeDef",
    "GetBucketTaggingOutputTypeDef",
    "GetBucketVersioningOutputTypeDef",
    "GetBucketWebsiteOutputTypeDef",
    "GetObjectAclOutputTypeDef",
    "GetObjectLegalHoldOutputTypeDef",
    "GetObjectLockConfigurationOutputTypeDef",
    "GetObjectOutputTypeDef",
    "GetObjectRetentionOutputTypeDef",
    "GetObjectTaggingOutputTypeDef",
    "GetObjectTorrentOutputTypeDef",
    "GetPublicAccessBlockOutputTypeDef",
    "GlacierJobParametersTypeDef",
    "GrantTypeDef",
    "GranteeTypeDef",
    "HeadObjectOutputTypeDef",
    "IndexDocumentTypeDef",
    "InitiatorTypeDef",
    "InputSerializationTypeDef",
    "IntelligentTieringAndOperatorTypeDef",
    "IntelligentTieringConfigurationTypeDef",
    "IntelligentTieringFilterTypeDef",
    "InventoryConfigurationTypeDef",
    "InventoryDestinationTypeDef",
    "InventoryEncryptionTypeDef",
    "InventoryFilterTypeDef",
    "InventoryS3BucketDestinationTypeDef",
    "InventoryScheduleTypeDef",
    "JSONInputTypeDef",
    "JSONOutputTypeDef",
    "LambdaFunctionConfigurationTypeDef",
    "LifecycleConfigurationTypeDef",
    "LifecycleExpirationTypeDef",
    "LifecycleRuleAndOperatorTypeDef",
    "LifecycleRuleFilterTypeDef",
    "LifecycleRuleTypeDef",
    "ListBucketAnalyticsConfigurationsOutputTypeDef",
    "ListBucketIntelligentTieringConfigurationsOutputTypeDef",
    "ListBucketInventoryConfigurationsOutputTypeDef",
    "ListBucketMetricsConfigurationsOutputTypeDef",
    "ListBucketsOutputTypeDef",
    "ListMultipartUploadsOutputTypeDef",
    "ListObjectVersionsOutputTypeDef",
    "ListObjectsOutputTypeDef",
    "ListObjectsV2OutputTypeDef",
    "ListPartsOutputTypeDef",
    "LoggingEnabledTypeDef",
    "MetadataEntryTypeDef",
    "MetricsAndOperatorTypeDef",
    "MetricsConfigurationTypeDef",
    "MetricsFilterTypeDef",
    "MetricsTypeDef",
    "MultipartUploadTypeDef",
    "NoncurrentVersionExpirationTypeDef",
    "NoncurrentVersionTransitionTypeDef",
    "NotificationConfigurationDeprecatedTypeDef",
    "NotificationConfigurationFilterTypeDef",
    "NotificationConfigurationTypeDef",
    "ObjectIdentifierTypeDef",
    "ObjectLockConfigurationTypeDef",
    "ObjectLockLegalHoldTypeDef",
    "ObjectLockRetentionTypeDef",
    "ObjectLockRuleTypeDef",
    "ObjectTypeDef",
    "ObjectVersionTypeDef",
    "OutputLocationTypeDef",
    "OutputSerializationTypeDef",
    "OwnerTypeDef",
    "OwnershipControlsRuleTypeDef",
    "OwnershipControlsTypeDef",
    "PaginatorConfigTypeDef",
    "PartTypeDef",
    "PolicyStatusTypeDef",
    "ProgressEventTypeDef",
    "ProgressTypeDef",
    "PublicAccessBlockConfigurationTypeDef",
    "PutObjectAclOutputTypeDef",
    "PutObjectLegalHoldOutputTypeDef",
    "PutObjectLockConfigurationOutputTypeDef",
    "PutObjectOutputTypeDef",
    "PutObjectRetentionOutputTypeDef",
    "PutObjectTaggingOutputTypeDef",
    "QueueConfigurationDeprecatedTypeDef",
    "QueueConfigurationTypeDef",
    "RecordsEventTypeDef",
    "RedirectAllRequestsToTypeDef",
    "RedirectTypeDef",
    "ReplicaModificationsTypeDef",
    "ReplicationConfigurationTypeDef",
    "ReplicationRuleAndOperatorTypeDef",
    "ReplicationRuleFilterTypeDef",
    "ReplicationRuleTypeDef",
    "ReplicationTimeTypeDef",
    "ReplicationTimeValueTypeDef",
    "RequestPaymentConfigurationTypeDef",
    "RequestProgressTypeDef",
    "ResponseMetadata",
    "RestoreObjectOutputTypeDef",
    "RestoreRequestTypeDef",
    "RoutingRuleTypeDef",
    "RuleTypeDef",
    "S3KeyFilterTypeDef",
    "S3LocationTypeDef",
    "SSEKMSTypeDef",
    "ScanRangeTypeDef",
    "SelectObjectContentEventStreamTypeDef",
    "SelectObjectContentOutputTypeDef",
    "SelectParametersTypeDef",
    "ServerSideEncryptionByDefaultTypeDef",
    "ServerSideEncryptionConfigurationTypeDef",
    "ServerSideEncryptionRuleTypeDef",
    "SourceSelectionCriteriaTypeDef",
    "SseKmsEncryptedObjectsTypeDef",
    "StatsEventTypeDef",
    "StatsTypeDef",
    "StorageClassAnalysisDataExportTypeDef",
    "StorageClassAnalysisTypeDef",
    "TagTypeDef",
    "TaggingTypeDef",
    "TargetGrantTypeDef",
    "TieringTypeDef",
    "TopicConfigurationDeprecatedTypeDef",
    "TopicConfigurationTypeDef",
    "TransitionTypeDef",
    "UploadPartCopyOutputTypeDef",
    "UploadPartOutputTypeDef",
    "VersioningConfigurationTypeDef",
    "WaiterConfigTypeDef",
    "WebsiteConfigurationTypeDef",
)


class AbortIncompleteMultipartUploadTypeDef(TypedDict, total=False):
    DaysAfterInitiation: int


class AbortMultipartUploadOutputTypeDef(TypedDict):
    RequestCharged: Literal["requester"]
    ResponseMetadata: "ResponseMetadata"


class AccelerateConfigurationTypeDef(TypedDict, total=False):
    Status: BucketAccelerateStatus


class AccessControlPolicyTypeDef(TypedDict, total=False):
    Grants: List["GrantTypeDef"]
    Owner: "OwnerTypeDef"


class AccessControlTranslationTypeDef(TypedDict):
    Owner: Literal["Destination"]


class AnalyticsAndOperatorTypeDef(TypedDict, total=False):
    Prefix: str
    Tags: List["TagTypeDef"]


class _RequiredAnalyticsConfigurationTypeDef(TypedDict):
    Id: str
    StorageClassAnalysis: "StorageClassAnalysisTypeDef"


class AnalyticsConfigurationTypeDef(_RequiredAnalyticsConfigurationTypeDef, total=False):
    Filter: "AnalyticsFilterTypeDef"


class AnalyticsExportDestinationTypeDef(TypedDict):
    S3BucketDestination: "AnalyticsS3BucketDestinationTypeDef"


class AnalyticsFilterTypeDef(TypedDict, total=False):
    Prefix: str
    Tag: "TagTypeDef"
    And: "AnalyticsAndOperatorTypeDef"


class _RequiredAnalyticsS3BucketDestinationTypeDef(TypedDict):
    Format: Literal["CSV"]
    Bucket: str


class AnalyticsS3BucketDestinationTypeDef(
    _RequiredAnalyticsS3BucketDestinationTypeDef, total=False
):
    BucketAccountId: str
    Prefix: str


class BucketLifecycleConfigurationTypeDef(TypedDict):
    Rules: List["LifecycleRuleTypeDef"]


class BucketLoggingStatusTypeDef(TypedDict, total=False):
    LoggingEnabled: "LoggingEnabledTypeDef"


class BucketTypeDef(TypedDict, total=False):
    Name: str
    CreationDate: datetime


class CORSConfigurationTypeDef(TypedDict):
    CORSRules: List["CORSRuleTypeDef"]


class _RequiredCORSRuleTypeDef(TypedDict):
    AllowedMethods: List[str]
    AllowedOrigins: List[str]


class CORSRuleTypeDef(_RequiredCORSRuleTypeDef, total=False):
    ID: str
    AllowedHeaders: List[str]
    ExposeHeaders: List[str]
    MaxAgeSeconds: int


class CSVInputTypeDef(TypedDict, total=False):
    FileHeaderInfo: FileHeaderInfo
    Comments: str
    QuoteEscapeCharacter: str
    RecordDelimiter: str
    FieldDelimiter: str
    QuoteCharacter: str
    AllowQuotedRecordDelimiter: bool


class CSVOutputTypeDef(TypedDict):
    QuoteFields: QuoteFields
    QuoteEscapeCharacter: str
    RecordDelimiter: str
    FieldDelimiter: str
    QuoteCharacter: str
    ResponseMetadata: "ResponseMetadata"


class CloudFunctionConfigurationTypeDef(TypedDict, total=False):
    Id: str
    Event: Event
    Events: List[Event]
    CloudFunction: str
    InvocationRole: str


class CommonPrefixTypeDef(TypedDict, total=False):
    Prefix: str


class CompleteMultipartUploadOutputTypeDef(TypedDict):
    Location: str
    Bucket: str
    Key: str
    Expiration: str
    ETag: str
    ServerSideEncryption: ServerSideEncryption
    VersionId: str
    SSEKMSKeyId: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ResponseMetadata: "ResponseMetadata"


class CompletedMultipartUploadTypeDef(TypedDict, total=False):
    Parts: List["CompletedPartTypeDef"]


class CompletedPartTypeDef(TypedDict, total=False):
    ETag: str
    PartNumber: int


class ConditionTypeDef(TypedDict, total=False):
    HttpErrorCodeReturnedEquals: str
    KeyPrefixEquals: str


class CopyObjectOutputTypeDef(TypedDict):
    CopyObjectResult: "CopyObjectResultTypeDef"
    Expiration: str
    CopySourceVersionId: str
    VersionId: str
    ServerSideEncryption: ServerSideEncryption
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    SSEKMSEncryptionContext: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ResponseMetadata: "ResponseMetadata"


class CopyObjectResultTypeDef(TypedDict, total=False):
    ETag: str
    LastModified: datetime


class CopyPartResultTypeDef(TypedDict, total=False):
    ETag: str
    LastModified: datetime


class _RequiredCopySourceTypeDef(TypedDict):
    Bucket: str
    Key: str


class CopySourceTypeDef(_RequiredCopySourceTypeDef, total=False):
    VersionId: str


class CreateBucketConfigurationTypeDef(TypedDict, total=False):
    LocationConstraint: BucketLocationConstraint


class CreateBucketOutputTypeDef(TypedDict):
    Location: str
    ResponseMetadata: "ResponseMetadata"


class CreateMultipartUploadOutputTypeDef(TypedDict):
    AbortDate: datetime
    AbortRuleId: str
    Bucket: str
    Key: str
    UploadId: str
    ServerSideEncryption: ServerSideEncryption
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    SSEKMSEncryptionContext: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ResponseMetadata: "ResponseMetadata"


class DefaultRetentionTypeDef(TypedDict, total=False):
    Mode: ObjectLockRetentionMode
    Days: int
    Years: int


class DeleteMarkerEntryTypeDef(TypedDict, total=False):
    Owner: "OwnerTypeDef"
    Key: str
    VersionId: str
    IsLatest: bool
    LastModified: datetime


class DeleteMarkerReplicationTypeDef(TypedDict, total=False):
    Status: DeleteMarkerReplicationStatus


class DeleteObjectOutputTypeDef(TypedDict):
    DeleteMarker: bool
    VersionId: str
    RequestCharged: Literal["requester"]
    ResponseMetadata: "ResponseMetadata"


class DeleteObjectTaggingOutputTypeDef(TypedDict):
    VersionId: str
    ResponseMetadata: "ResponseMetadata"


class DeleteObjectsOutputTypeDef(TypedDict):
    Deleted: List["DeletedObjectTypeDef"]
    RequestCharged: Literal["requester"]
    Errors: List["ErrorTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class _RequiredDeleteTypeDef(TypedDict):
    Objects: List["ObjectIdentifierTypeDef"]


class DeleteTypeDef(_RequiredDeleteTypeDef, total=False):
    Quiet: bool


class DeletedObjectTypeDef(TypedDict, total=False):
    Key: str
    VersionId: str
    DeleteMarker: bool
    DeleteMarkerVersionId: str


class _RequiredDestinationTypeDef(TypedDict):
    Bucket: str


class DestinationTypeDef(_RequiredDestinationTypeDef, total=False):
    Account: str
    StorageClass: StorageClass
    AccessControlTranslation: "AccessControlTranslationTypeDef"
    EncryptionConfiguration: "EncryptionConfigurationTypeDef"
    ReplicationTime: "ReplicationTimeTypeDef"
    Metrics: "MetricsTypeDef"


class EncryptionConfigurationTypeDef(TypedDict, total=False):
    ReplicaKmsKeyID: str


class _RequiredEncryptionTypeDef(TypedDict):
    EncryptionType: ServerSideEncryption


class EncryptionTypeDef(_RequiredEncryptionTypeDef, total=False):
    KMSKeyId: str
    KMSContext: str


class ErrorDocumentTypeDef(TypedDict):
    Key: str


class ErrorTypeDef(TypedDict, total=False):
    Key: str
    VersionId: str
    Code: str
    Message: str


class ExistingObjectReplicationTypeDef(TypedDict):
    Status: ExistingObjectReplicationStatus


class FilterRuleTypeDef(TypedDict, total=False):
    Name: FilterRuleName
    Value: str


class GetBucketAccelerateConfigurationOutputTypeDef(TypedDict):
    Status: BucketAccelerateStatus
    ResponseMetadata: "ResponseMetadata"


class GetBucketAclOutputTypeDef(TypedDict):
    Owner: "OwnerTypeDef"
    Grants: List["GrantTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetBucketAnalyticsConfigurationOutputTypeDef(TypedDict):
    AnalyticsConfiguration: "AnalyticsConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetBucketCorsOutputTypeDef(TypedDict):
    CORSRules: List["CORSRuleTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetBucketEncryptionOutputTypeDef(TypedDict):
    ServerSideEncryptionConfiguration: "ServerSideEncryptionConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetBucketIntelligentTieringConfigurationOutputTypeDef(TypedDict):
    IntelligentTieringConfiguration: "IntelligentTieringConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetBucketInventoryConfigurationOutputTypeDef(TypedDict):
    InventoryConfiguration: "InventoryConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetBucketLifecycleConfigurationOutputTypeDef(TypedDict):
    Rules: List["LifecycleRuleTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetBucketLifecycleOutputTypeDef(TypedDict):
    Rules: List["RuleTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetBucketLocationOutputTypeDef(TypedDict):
    LocationConstraint: BucketLocationConstraint
    ResponseMetadata: "ResponseMetadata"


class GetBucketLoggingOutputTypeDef(TypedDict):
    LoggingEnabled: "LoggingEnabledTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetBucketMetricsConfigurationOutputTypeDef(TypedDict):
    MetricsConfiguration: "MetricsConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetBucketOwnershipControlsOutputTypeDef(TypedDict):
    OwnershipControls: "OwnershipControlsTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetBucketPolicyOutputTypeDef(TypedDict):
    Policy: str
    ResponseMetadata: "ResponseMetadata"


class GetBucketPolicyStatusOutputTypeDef(TypedDict):
    PolicyStatus: "PolicyStatusTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetBucketReplicationOutputTypeDef(TypedDict):
    ReplicationConfiguration: "ReplicationConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetBucketRequestPaymentOutputTypeDef(TypedDict):
    Payer: Payer
    ResponseMetadata: "ResponseMetadata"


class GetBucketTaggingOutputTypeDef(TypedDict):
    TagSet: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetBucketVersioningOutputTypeDef(TypedDict):
    Status: BucketVersioningStatus
    MFADelete: MFADeleteStatus
    ResponseMetadata: "ResponseMetadata"


class GetBucketWebsiteOutputTypeDef(TypedDict):
    RedirectAllRequestsTo: "RedirectAllRequestsToTypeDef"
    IndexDocument: "IndexDocumentTypeDef"
    ErrorDocument: "ErrorDocumentTypeDef"
    RoutingRules: List["RoutingRuleTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetObjectAclOutputTypeDef(TypedDict):
    Owner: "OwnerTypeDef"
    Grants: List["GrantTypeDef"]
    RequestCharged: Literal["requester"]
    ResponseMetadata: "ResponseMetadata"


class GetObjectLegalHoldOutputTypeDef(TypedDict):
    LegalHold: "ObjectLockLegalHoldTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetObjectLockConfigurationOutputTypeDef(TypedDict):
    ObjectLockConfiguration: "ObjectLockConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetObjectOutputTypeDef(TypedDict):
    Body: StreamingBody
    DeleteMarker: bool
    AcceptRanges: str
    Expiration: str
    Restore: str
    LastModified: datetime
    ContentLength: int
    ETag: str
    MissingMeta: int
    VersionId: str
    CacheControl: str
    ContentDisposition: str
    ContentEncoding: str
    ContentLanguage: str
    ContentRange: str
    ContentType: str
    Expires: datetime
    WebsiteRedirectLocation: str
    ServerSideEncryption: ServerSideEncryption
    Metadata: Dict[str, str]
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    BucketKeyEnabled: bool
    StorageClass: StorageClass
    RequestCharged: Literal["requester"]
    ReplicationStatus: ReplicationStatus
    PartsCount: int
    TagCount: int
    ObjectLockMode: ObjectLockMode
    ObjectLockRetainUntilDate: datetime
    ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatus
    ResponseMetadata: "ResponseMetadata"


class GetObjectRetentionOutputTypeDef(TypedDict):
    Retention: "ObjectLockRetentionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetObjectTaggingOutputTypeDef(TypedDict):
    VersionId: str
    TagSet: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetObjectTorrentOutputTypeDef(TypedDict):
    Body: StreamingBody
    RequestCharged: Literal["requester"]
    ResponseMetadata: "ResponseMetadata"


class GetPublicAccessBlockOutputTypeDef(TypedDict):
    PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GlacierJobParametersTypeDef(TypedDict):
    Tier: Tier


class GrantTypeDef(TypedDict, total=False):
    Grantee: "GranteeTypeDef"
    Permission: Permission


_RequiredGranteeTypeDef = TypedDict("_RequiredGranteeTypeDef", {"Type": TypeType})
_OptionalGranteeTypeDef = TypedDict(
    "_OptionalGranteeTypeDef",
    {"DisplayName": str, "EmailAddress": str, "ID": str, "URI": str},
    total=False,
)


class GranteeTypeDef(_RequiredGranteeTypeDef, _OptionalGranteeTypeDef):
    pass


class HeadObjectOutputTypeDef(TypedDict):
    DeleteMarker: bool
    AcceptRanges: str
    Expiration: str
    Restore: str
    ArchiveStatus: ArchiveStatus
    LastModified: datetime
    ContentLength: int
    ETag: str
    MissingMeta: int
    VersionId: str
    CacheControl: str
    ContentDisposition: str
    ContentEncoding: str
    ContentLanguage: str
    ContentType: str
    Expires: datetime
    WebsiteRedirectLocation: str
    ServerSideEncryption: ServerSideEncryption
    Metadata: Dict[str, str]
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    BucketKeyEnabled: bool
    StorageClass: StorageClass
    RequestCharged: Literal["requester"]
    ReplicationStatus: ReplicationStatus
    PartsCount: int
    ObjectLockMode: ObjectLockMode
    ObjectLockRetainUntilDate: datetime
    ObjectLockLegalHoldStatus: ObjectLockLegalHoldStatus
    ResponseMetadata: "ResponseMetadata"


class IndexDocumentTypeDef(TypedDict):
    Suffix: str


class InitiatorTypeDef(TypedDict, total=False):
    ID: str
    DisplayName: str


class InputSerializationTypeDef(TypedDict, total=False):
    CSV: "CSVInputTypeDef"
    CompressionType: CompressionType
    JSON: "JSONInputTypeDef"
    Parquet: Dict[str, Any]


class IntelligentTieringAndOperatorTypeDef(TypedDict, total=False):
    Prefix: str
    Tags: List["TagTypeDef"]


class _RequiredIntelligentTieringConfigurationTypeDef(TypedDict):
    Id: str
    Status: IntelligentTieringStatus
    Tierings: List["TieringTypeDef"]


class IntelligentTieringConfigurationTypeDef(
    _RequiredIntelligentTieringConfigurationTypeDef, total=False
):
    Filter: "IntelligentTieringFilterTypeDef"


class IntelligentTieringFilterTypeDef(TypedDict, total=False):
    Prefix: str
    Tag: "TagTypeDef"
    And: "IntelligentTieringAndOperatorTypeDef"


class _RequiredInventoryConfigurationTypeDef(TypedDict):
    Destination: "InventoryDestinationTypeDef"
    IsEnabled: bool
    Id: str
    IncludedObjectVersions: InventoryIncludedObjectVersions
    Schedule: "InventoryScheduleTypeDef"


class InventoryConfigurationTypeDef(_RequiredInventoryConfigurationTypeDef, total=False):
    Filter: "InventoryFilterTypeDef"
    OptionalFields: List[InventoryOptionalField]


class InventoryDestinationTypeDef(TypedDict):
    S3BucketDestination: "InventoryS3BucketDestinationTypeDef"


class InventoryEncryptionTypeDef(TypedDict, total=False):
    SSES3: Dict[str, Any]
    SSEKMS: "SSEKMSTypeDef"


class InventoryFilterTypeDef(TypedDict):
    Prefix: str


class _RequiredInventoryS3BucketDestinationTypeDef(TypedDict):
    Bucket: str
    Format: InventoryFormat


class InventoryS3BucketDestinationTypeDef(
    _RequiredInventoryS3BucketDestinationTypeDef, total=False
):
    AccountId: str
    Prefix: str
    Encryption: "InventoryEncryptionTypeDef"


class InventoryScheduleTypeDef(TypedDict):
    Frequency: InventoryFrequency


JSONInputTypeDef = TypedDict("JSONInputTypeDef", {"Type": JSONType}, total=False)


class JSONOutputTypeDef(TypedDict):
    RecordDelimiter: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredLambdaFunctionConfigurationTypeDef(TypedDict):
    LambdaFunctionArn: str
    Events: List[Event]


class LambdaFunctionConfigurationTypeDef(_RequiredLambdaFunctionConfigurationTypeDef, total=False):
    Id: str
    Filter: "NotificationConfigurationFilterTypeDef"


class LifecycleConfigurationTypeDef(TypedDict):
    Rules: List["RuleTypeDef"]


class LifecycleExpirationTypeDef(TypedDict, total=False):
    Date: datetime
    Days: int
    ExpiredObjectDeleteMarker: bool


class LifecycleRuleAndOperatorTypeDef(TypedDict, total=False):
    Prefix: str
    Tags: List["TagTypeDef"]


class LifecycleRuleFilterTypeDef(TypedDict, total=False):
    Prefix: str
    Tag: "TagTypeDef"
    And: "LifecycleRuleAndOperatorTypeDef"


class _RequiredLifecycleRuleTypeDef(TypedDict):
    Status: ExpirationStatus


class LifecycleRuleTypeDef(_RequiredLifecycleRuleTypeDef, total=False):
    Expiration: "LifecycleExpirationTypeDef"
    ID: str
    Prefix: str
    Filter: "LifecycleRuleFilterTypeDef"
    Transitions: List["TransitionTypeDef"]
    NoncurrentVersionTransitions: List["NoncurrentVersionTransitionTypeDef"]
    NoncurrentVersionExpiration: "NoncurrentVersionExpirationTypeDef"
    AbortIncompleteMultipartUpload: "AbortIncompleteMultipartUploadTypeDef"


class ListBucketAnalyticsConfigurationsOutputTypeDef(TypedDict):
    IsTruncated: bool
    ContinuationToken: str
    NextContinuationToken: str
    AnalyticsConfigurationList: List["AnalyticsConfigurationTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListBucketIntelligentTieringConfigurationsOutputTypeDef(TypedDict):
    IsTruncated: bool
    ContinuationToken: str
    NextContinuationToken: str
    IntelligentTieringConfigurationList: List["IntelligentTieringConfigurationTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListBucketInventoryConfigurationsOutputTypeDef(TypedDict):
    ContinuationToken: str
    InventoryConfigurationList: List["InventoryConfigurationTypeDef"]
    IsTruncated: bool
    NextContinuationToken: str
    ResponseMetadata: "ResponseMetadata"


class ListBucketMetricsConfigurationsOutputTypeDef(TypedDict):
    IsTruncated: bool
    ContinuationToken: str
    NextContinuationToken: str
    MetricsConfigurationList: List["MetricsConfigurationTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListBucketsOutputTypeDef(TypedDict):
    Buckets: List["BucketTypeDef"]
    Owner: "OwnerTypeDef"
    ResponseMetadata: "ResponseMetadata"


class ListMultipartUploadsOutputTypeDef(TypedDict):
    Bucket: str
    KeyMarker: str
    UploadIdMarker: str
    NextKeyMarker: str
    Prefix: str
    Delimiter: str
    NextUploadIdMarker: str
    MaxUploads: int
    IsTruncated: bool
    Uploads: List["MultipartUploadTypeDef"]
    CommonPrefixes: List["CommonPrefixTypeDef"]
    EncodingType: Literal["url"]
    ResponseMetadata: "ResponseMetadata"


class ListObjectVersionsOutputTypeDef(TypedDict):
    IsTruncated: bool
    KeyMarker: str
    VersionIdMarker: str
    NextKeyMarker: str
    NextVersionIdMarker: str
    Versions: List["ObjectVersionTypeDef"]
    DeleteMarkers: List["DeleteMarkerEntryTypeDef"]
    Name: str
    Prefix: str
    Delimiter: str
    MaxKeys: int
    CommonPrefixes: List["CommonPrefixTypeDef"]
    EncodingType: Literal["url"]
    ResponseMetadata: "ResponseMetadata"


class ListObjectsOutputTypeDef(TypedDict):
    IsTruncated: bool
    Marker: str
    NextMarker: str
    Contents: List["ObjectTypeDef"]
    Name: str
    Prefix: str
    Delimiter: str
    MaxKeys: int
    CommonPrefixes: List["CommonPrefixTypeDef"]
    EncodingType: Literal["url"]
    ResponseMetadata: "ResponseMetadata"


class ListObjectsV2OutputTypeDef(TypedDict):
    IsTruncated: bool
    Contents: List["ObjectTypeDef"]
    Name: str
    Prefix: str
    Delimiter: str
    MaxKeys: int
    CommonPrefixes: List["CommonPrefixTypeDef"]
    EncodingType: Literal["url"]
    KeyCount: int
    ContinuationToken: str
    NextContinuationToken: str
    StartAfter: str
    ResponseMetadata: "ResponseMetadata"


class ListPartsOutputTypeDef(TypedDict):
    AbortDate: datetime
    AbortRuleId: str
    Bucket: str
    Key: str
    UploadId: str
    PartNumberMarker: int
    NextPartNumberMarker: int
    MaxParts: int
    IsTruncated: bool
    Parts: List["PartTypeDef"]
    Initiator: "InitiatorTypeDef"
    Owner: "OwnerTypeDef"
    StorageClass: StorageClass
    RequestCharged: Literal["requester"]
    ResponseMetadata: "ResponseMetadata"


class _RequiredLoggingEnabledTypeDef(TypedDict):
    TargetBucket: str
    TargetPrefix: str


class LoggingEnabledTypeDef(_RequiredLoggingEnabledTypeDef, total=False):
    TargetGrants: List["TargetGrantTypeDef"]


class MetadataEntryTypeDef(TypedDict, total=False):
    Name: str
    Value: str


class MetricsAndOperatorTypeDef(TypedDict, total=False):
    Prefix: str
    Tags: List["TagTypeDef"]


class _RequiredMetricsConfigurationTypeDef(TypedDict):
    Id: str


class MetricsConfigurationTypeDef(_RequiredMetricsConfigurationTypeDef, total=False):
    Filter: "MetricsFilterTypeDef"


class MetricsFilterTypeDef(TypedDict, total=False):
    Prefix: str
    Tag: "TagTypeDef"
    And: "MetricsAndOperatorTypeDef"


class _RequiredMetricsTypeDef(TypedDict):
    Status: MetricsStatus


class MetricsTypeDef(_RequiredMetricsTypeDef, total=False):
    EventThreshold: "ReplicationTimeValueTypeDef"


class MultipartUploadTypeDef(TypedDict, total=False):
    UploadId: str
    Key: str
    Initiated: datetime
    StorageClass: StorageClass
    Owner: "OwnerTypeDef"
    Initiator: "InitiatorTypeDef"


class NoncurrentVersionExpirationTypeDef(TypedDict, total=False):
    NoncurrentDays: int


class NoncurrentVersionTransitionTypeDef(TypedDict, total=False):
    NoncurrentDays: int
    StorageClass: TransitionStorageClass


class NotificationConfigurationDeprecatedTypeDef(TypedDict, total=False):
    TopicConfiguration: "TopicConfigurationDeprecatedTypeDef"
    QueueConfiguration: "QueueConfigurationDeprecatedTypeDef"
    CloudFunctionConfiguration: "CloudFunctionConfigurationTypeDef"


class NotificationConfigurationFilterTypeDef(TypedDict, total=False):
    Key: "S3KeyFilterTypeDef"


class NotificationConfigurationTypeDef(TypedDict, total=False):
    TopicConfigurations: List["TopicConfigurationTypeDef"]
    QueueConfigurations: List["QueueConfigurationTypeDef"]
    LambdaFunctionConfigurations: List["LambdaFunctionConfigurationTypeDef"]


class _RequiredObjectIdentifierTypeDef(TypedDict):
    Key: str


class ObjectIdentifierTypeDef(_RequiredObjectIdentifierTypeDef, total=False):
    VersionId: str


class ObjectLockConfigurationTypeDef(TypedDict, total=False):
    ObjectLockEnabled: Literal["Enabled"]
    Rule: "ObjectLockRuleTypeDef"


class ObjectLockLegalHoldTypeDef(TypedDict, total=False):
    Status: ObjectLockLegalHoldStatus


class ObjectLockRetentionTypeDef(TypedDict, total=False):
    Mode: ObjectLockRetentionMode
    RetainUntilDate: datetime


class ObjectLockRuleTypeDef(TypedDict, total=False):
    DefaultRetention: "DefaultRetentionTypeDef"


class ObjectTypeDef(TypedDict, total=False):
    Key: str
    LastModified: datetime
    ETag: str
    Size: int
    StorageClass: ObjectStorageClass
    Owner: "OwnerTypeDef"


class ObjectVersionTypeDef(TypedDict, total=False):
    ETag: str
    Size: int
    StorageClass: Literal["STANDARD"]
    Key: str
    VersionId: str
    IsLatest: bool
    LastModified: datetime
    Owner: "OwnerTypeDef"


class OutputLocationTypeDef(TypedDict, total=False):
    S3: "S3LocationTypeDef"


class OutputSerializationTypeDef(TypedDict, total=False):
    CSV: "CSVOutputTypeDef"
    JSON: "JSONOutputTypeDef"


class OwnerTypeDef(TypedDict, total=False):
    DisplayName: str
    ID: str


class OwnershipControlsRuleTypeDef(TypedDict):
    ObjectOwnership: ObjectOwnership


class OwnershipControlsTypeDef(TypedDict):
    Rules: List["OwnershipControlsRuleTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PartTypeDef(TypedDict, total=False):
    PartNumber: int
    LastModified: datetime
    ETag: str
    Size: int


class PolicyStatusTypeDef(TypedDict, total=False):
    IsPublic: bool


class ProgressEventTypeDef(TypedDict, total=False):
    Details: "ProgressTypeDef"


class ProgressTypeDef(TypedDict, total=False):
    BytesScanned: int
    BytesProcessed: int
    BytesReturned: int


class PublicAccessBlockConfigurationTypeDef(TypedDict, total=False):
    BlockPublicAcls: bool
    IgnorePublicAcls: bool
    BlockPublicPolicy: bool
    RestrictPublicBuckets: bool


class PutObjectAclOutputTypeDef(TypedDict):
    RequestCharged: Literal["requester"]
    ResponseMetadata: "ResponseMetadata"


class PutObjectLegalHoldOutputTypeDef(TypedDict):
    RequestCharged: Literal["requester"]
    ResponseMetadata: "ResponseMetadata"


class PutObjectLockConfigurationOutputTypeDef(TypedDict):
    RequestCharged: Literal["requester"]
    ResponseMetadata: "ResponseMetadata"


class PutObjectOutputTypeDef(TypedDict):
    Expiration: str
    ETag: str
    ServerSideEncryption: ServerSideEncryption
    VersionId: str
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    SSEKMSEncryptionContext: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ResponseMetadata: "ResponseMetadata"


class PutObjectRetentionOutputTypeDef(TypedDict):
    RequestCharged: Literal["requester"]
    ResponseMetadata: "ResponseMetadata"


class PutObjectTaggingOutputTypeDef(TypedDict):
    VersionId: str
    ResponseMetadata: "ResponseMetadata"


class QueueConfigurationDeprecatedTypeDef(TypedDict, total=False):
    Id: str
    Event: Event
    Events: List[Event]
    Queue: str


class _RequiredQueueConfigurationTypeDef(TypedDict):
    QueueArn: str
    Events: List[Event]


class QueueConfigurationTypeDef(_RequiredQueueConfigurationTypeDef, total=False):
    Id: str
    Filter: "NotificationConfigurationFilterTypeDef"


class RecordsEventTypeDef(TypedDict, total=False):
    Payload: Union[bytes, IO[bytes]]


_RequiredRedirectAllRequestsToTypeDef = TypedDict(
    "_RequiredRedirectAllRequestsToTypeDef", {"HostName": str}
)
_OptionalRedirectAllRequestsToTypeDef = TypedDict(
    "_OptionalRedirectAllRequestsToTypeDef", {"Protocol": ProtocolType}, total=False
)


class RedirectAllRequestsToTypeDef(
    _RequiredRedirectAllRequestsToTypeDef, _OptionalRedirectAllRequestsToTypeDef
):
    pass


RedirectTypeDef = TypedDict(
    "RedirectTypeDef",
    {
        "HostName": str,
        "HttpRedirectCode": str,
        "Protocol": ProtocolType,
        "ReplaceKeyPrefixWith": str,
        "ReplaceKeyWith": str,
    },
    total=False,
)


class ReplicaModificationsTypeDef(TypedDict):
    Status: ReplicaModificationsStatus


class ReplicationConfigurationTypeDef(TypedDict):
    Role: str
    Rules: List["ReplicationRuleTypeDef"]


class ReplicationRuleAndOperatorTypeDef(TypedDict, total=False):
    Prefix: str
    Tags: List["TagTypeDef"]


class ReplicationRuleFilterTypeDef(TypedDict, total=False):
    Prefix: str
    Tag: "TagTypeDef"
    And: "ReplicationRuleAndOperatorTypeDef"


class _RequiredReplicationRuleTypeDef(TypedDict):
    Status: ReplicationRuleStatus
    Destination: "DestinationTypeDef"


class ReplicationRuleTypeDef(_RequiredReplicationRuleTypeDef, total=False):
    ID: str
    Priority: int
    Prefix: str
    Filter: "ReplicationRuleFilterTypeDef"
    SourceSelectionCriteria: "SourceSelectionCriteriaTypeDef"
    ExistingObjectReplication: "ExistingObjectReplicationTypeDef"
    DeleteMarkerReplication: "DeleteMarkerReplicationTypeDef"


class ReplicationTimeTypeDef(TypedDict):
    Status: ReplicationTimeStatus
    Time: "ReplicationTimeValueTypeDef"


class ReplicationTimeValueTypeDef(TypedDict, total=False):
    Minutes: int


class RequestPaymentConfigurationTypeDef(TypedDict):
    Payer: Payer


class RequestProgressTypeDef(TypedDict, total=False):
    Enabled: bool


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RestoreObjectOutputTypeDef(TypedDict):
    RequestCharged: Literal["requester"]
    RestoreOutputPath: str
    ResponseMetadata: "ResponseMetadata"


RestoreRequestTypeDef = TypedDict(
    "RestoreRequestTypeDef",
    {
        "Days": int,
        "GlacierJobParameters": "GlacierJobParametersTypeDef",
        "Type": Literal["SELECT"],
        "Tier": Tier,
        "Description": str,
        "SelectParameters": "SelectParametersTypeDef",
        "OutputLocation": "OutputLocationTypeDef",
    },
    total=False,
)


class _RequiredRoutingRuleTypeDef(TypedDict):
    Redirect: "RedirectTypeDef"


class RoutingRuleTypeDef(_RequiredRoutingRuleTypeDef, total=False):
    Condition: "ConditionTypeDef"


class _RequiredRuleTypeDef(TypedDict):
    Prefix: str
    Status: ExpirationStatus


class RuleTypeDef(_RequiredRuleTypeDef, total=False):
    Expiration: "LifecycleExpirationTypeDef"
    ID: str
    Transition: "TransitionTypeDef"
    NoncurrentVersionTransition: "NoncurrentVersionTransitionTypeDef"
    NoncurrentVersionExpiration: "NoncurrentVersionExpirationTypeDef"
    AbortIncompleteMultipartUpload: "AbortIncompleteMultipartUploadTypeDef"


class S3KeyFilterTypeDef(TypedDict, total=False):
    FilterRules: List["FilterRuleTypeDef"]


class _RequiredS3LocationTypeDef(TypedDict):
    BucketName: str
    Prefix: str


class S3LocationTypeDef(_RequiredS3LocationTypeDef, total=False):
    Encryption: "EncryptionTypeDef"
    CannedACL: ObjectCannedACL
    AccessControlList: List["GrantTypeDef"]
    Tagging: "TaggingTypeDef"
    UserMetadata: List["MetadataEntryTypeDef"]
    StorageClass: StorageClass


class SSEKMSTypeDef(TypedDict):
    KeyId: str


class ScanRangeTypeDef(TypedDict, total=False):
    Start: int
    End: int


class SelectObjectContentEventStreamTypeDef(TypedDict, total=False):
    Records: "RecordsEventTypeDef"
    Stats: "StatsEventTypeDef"
    Progress: "ProgressEventTypeDef"
    Cont: Dict[str, Any]
    End: Dict[str, Any]


class SelectObjectContentOutputTypeDef(TypedDict):
    Payload: "SelectObjectContentEventStreamTypeDef"
    ResponseMetadata: "ResponseMetadata"


class SelectParametersTypeDef(TypedDict):
    InputSerialization: "InputSerializationTypeDef"
    ExpressionType: Literal["SQL"]
    Expression: str
    OutputSerialization: "OutputSerializationTypeDef"


class _RequiredServerSideEncryptionByDefaultTypeDef(TypedDict):
    SSEAlgorithm: ServerSideEncryption


class ServerSideEncryptionByDefaultTypeDef(
    _RequiredServerSideEncryptionByDefaultTypeDef, total=False
):
    KMSMasterKeyID: str


class ServerSideEncryptionConfigurationTypeDef(TypedDict):
    Rules: List["ServerSideEncryptionRuleTypeDef"]


class ServerSideEncryptionRuleTypeDef(TypedDict, total=False):
    ApplyServerSideEncryptionByDefault: "ServerSideEncryptionByDefaultTypeDef"
    BucketKeyEnabled: bool


class SourceSelectionCriteriaTypeDef(TypedDict, total=False):
    SseKmsEncryptedObjects: "SseKmsEncryptedObjectsTypeDef"
    ReplicaModifications: "ReplicaModificationsTypeDef"


class SseKmsEncryptedObjectsTypeDef(TypedDict):
    Status: SseKmsEncryptedObjectsStatus


class StatsEventTypeDef(TypedDict, total=False):
    Details: "StatsTypeDef"


class StatsTypeDef(TypedDict, total=False):
    BytesScanned: int
    BytesProcessed: int
    BytesReturned: int


class StorageClassAnalysisDataExportTypeDef(TypedDict):
    OutputSchemaVersion: Literal["V_1"]
    Destination: "AnalyticsExportDestinationTypeDef"


class StorageClassAnalysisTypeDef(TypedDict, total=False):
    DataExport: "StorageClassAnalysisDataExportTypeDef"


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TaggingTypeDef(TypedDict):
    TagSet: List["TagTypeDef"]


class TargetGrantTypeDef(TypedDict, total=False):
    Grantee: "GranteeTypeDef"
    Permission: BucketLogsPermission


class TieringTypeDef(TypedDict):
    Days: int
    AccessTier: IntelligentTieringAccessTier


class TopicConfigurationDeprecatedTypeDef(TypedDict, total=False):
    Id: str
    Events: List[Event]
    Event: Event
    Topic: str


class _RequiredTopicConfigurationTypeDef(TypedDict):
    TopicArn: str
    Events: List[Event]


class TopicConfigurationTypeDef(_RequiredTopicConfigurationTypeDef, total=False):
    Id: str
    Filter: "NotificationConfigurationFilterTypeDef"


class TransitionTypeDef(TypedDict, total=False):
    Date: datetime
    Days: int
    StorageClass: TransitionStorageClass


class UploadPartCopyOutputTypeDef(TypedDict):
    CopySourceVersionId: str
    CopyPartResult: "CopyPartResultTypeDef"
    ServerSideEncryption: ServerSideEncryption
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ResponseMetadata: "ResponseMetadata"


class UploadPartOutputTypeDef(TypedDict):
    ServerSideEncryption: ServerSideEncryption
    ETag: str
    SSECustomerAlgorithm: str
    SSECustomerKeyMD5: str
    SSEKMSKeyId: str
    BucketKeyEnabled: bool
    RequestCharged: Literal["requester"]
    ResponseMetadata: "ResponseMetadata"


class VersioningConfigurationTypeDef(TypedDict, total=False):
    MFADelete: MFADelete
    Status: BucketVersioningStatus


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int


class WebsiteConfigurationTypeDef(TypedDict, total=False):
    ErrorDocument: "ErrorDocumentTypeDef"
    IndexDocument: "IndexDocumentTypeDef"
    RedirectAllRequestsTo: "RedirectAllRequestsToTypeDef"
    RoutingRules: List["RoutingRuleTypeDef"]
