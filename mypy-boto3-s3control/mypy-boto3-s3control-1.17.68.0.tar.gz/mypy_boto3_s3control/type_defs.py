"""
Type annotations for s3control service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3control/type_defs.html)

Usage::

    ```python
    from mypy_boto3_s3control.type_defs import AbortIncompleteMultipartUploadTypeDef

    data: AbortIncompleteMultipartUploadTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_s3control.literals import (
    BucketLocationConstraint,
    ExpirationStatus,
    Format,
    JobManifestFieldName,
    JobManifestFormat,
    JobReportScope,
    JobStatus,
    NetworkOrigin,
    ObjectLambdaAllowedFeature,
    OperationName,
    S3CannedAccessControlList,
    S3GlacierJobTier,
    S3GranteeTypeIdentifier,
    S3MetadataDirective,
    S3ObjectLockLegalHoldStatus,
    S3ObjectLockMode,
    S3ObjectLockRetentionMode,
    S3Permission,
    S3SSEAlgorithm,
    S3StorageClass,
    TransitionStorageClass,
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
    "AccessPointTypeDef",
    "AccountLevelTypeDef",
    "ActivityMetricsTypeDef",
    "AwsLambdaTransformationTypeDef",
    "BucketLevelTypeDef",
    "CreateAccessPointForObjectLambdaResultTypeDef",
    "CreateAccessPointResultTypeDef",
    "CreateBucketConfigurationTypeDef",
    "CreateBucketResultTypeDef",
    "CreateJobResultTypeDef",
    "DescribeJobResultTypeDef",
    "ExcludeTypeDef",
    "GetAccessPointConfigurationForObjectLambdaResultTypeDef",
    "GetAccessPointForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyResultTypeDef",
    "GetAccessPointPolicyStatusForObjectLambdaResultTypeDef",
    "GetAccessPointPolicyStatusResultTypeDef",
    "GetAccessPointResultTypeDef",
    "GetBucketLifecycleConfigurationResultTypeDef",
    "GetBucketPolicyResultTypeDef",
    "GetBucketResultTypeDef",
    "GetBucketTaggingResultTypeDef",
    "GetJobTaggingResultTypeDef",
    "GetPublicAccessBlockOutputTypeDef",
    "GetStorageLensConfigurationResultTypeDef",
    "GetStorageLensConfigurationTaggingResultTypeDef",
    "IncludeTypeDef",
    "JobDescriptorTypeDef",
    "JobFailureTypeDef",
    "JobListDescriptorTypeDef",
    "JobManifestLocationTypeDef",
    "JobManifestSpecTypeDef",
    "JobManifestTypeDef",
    "JobOperationTypeDef",
    "JobProgressSummaryTypeDef",
    "JobReportTypeDef",
    "LambdaInvokeOperationTypeDef",
    "LifecycleConfigurationTypeDef",
    "LifecycleExpirationTypeDef",
    "LifecycleRuleAndOperatorTypeDef",
    "LifecycleRuleFilterTypeDef",
    "LifecycleRuleTypeDef",
    "ListAccessPointsForObjectLambdaResultTypeDef",
    "ListAccessPointsResultTypeDef",
    "ListJobsResultTypeDef",
    "ListRegionalBucketsResultTypeDef",
    "ListStorageLensConfigurationEntryTypeDef",
    "ListStorageLensConfigurationsResultTypeDef",
    "NoncurrentVersionExpirationTypeDef",
    "NoncurrentVersionTransitionTypeDef",
    "ObjectLambdaAccessPointTypeDef",
    "ObjectLambdaConfigurationTypeDef",
    "ObjectLambdaContentTransformationTypeDef",
    "ObjectLambdaTransformationConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyStatusTypeDef",
    "PrefixLevelStorageMetricsTypeDef",
    "PrefixLevelTypeDef",
    "PublicAccessBlockConfigurationTypeDef",
    "RegionalBucketTypeDef",
    "ResponseMetadata",
    "S3AccessControlListTypeDef",
    "S3AccessControlPolicyTypeDef",
    "S3BucketDestinationTypeDef",
    "S3CopyObjectOperationTypeDef",
    "S3GrantTypeDef",
    "S3GranteeTypeDef",
    "S3InitiateRestoreObjectOperationTypeDef",
    "S3ObjectLockLegalHoldTypeDef",
    "S3ObjectMetadataTypeDef",
    "S3ObjectOwnerTypeDef",
    "S3RetentionTypeDef",
    "S3SetObjectAclOperationTypeDef",
    "S3SetObjectLegalHoldOperationTypeDef",
    "S3SetObjectRetentionOperationTypeDef",
    "S3SetObjectTaggingOperationTypeDef",
    "S3TagTypeDef",
    "SSEKMSTypeDef",
    "SelectionCriteriaTypeDef",
    "StorageLensAwsOrgTypeDef",
    "StorageLensConfigurationTypeDef",
    "StorageLensDataExportEncryptionTypeDef",
    "StorageLensDataExportTypeDef",
    "StorageLensTagTypeDef",
    "TaggingTypeDef",
    "TransitionTypeDef",
    "UpdateJobPriorityResultTypeDef",
    "UpdateJobStatusResultTypeDef",
    "VpcConfigurationTypeDef",
)


class AbortIncompleteMultipartUploadTypeDef(TypedDict, total=False):
    DaysAfterInitiation: int


class _RequiredAccessPointTypeDef(TypedDict):
    Name: str
    NetworkOrigin: NetworkOrigin
    Bucket: str


class AccessPointTypeDef(_RequiredAccessPointTypeDef, total=False):
    VpcConfiguration: "VpcConfigurationTypeDef"
    AccessPointArn: str


class _RequiredAccountLevelTypeDef(TypedDict):
    BucketLevel: "BucketLevelTypeDef"


class AccountLevelTypeDef(_RequiredAccountLevelTypeDef, total=False):
    ActivityMetrics: "ActivityMetricsTypeDef"


class ActivityMetricsTypeDef(TypedDict, total=False):
    IsEnabled: bool


class _RequiredAwsLambdaTransformationTypeDef(TypedDict):
    FunctionArn: str


class AwsLambdaTransformationTypeDef(_RequiredAwsLambdaTransformationTypeDef, total=False):
    FunctionPayload: str


class BucketLevelTypeDef(TypedDict, total=False):
    ActivityMetrics: "ActivityMetricsTypeDef"
    PrefixLevel: "PrefixLevelTypeDef"


class CreateAccessPointForObjectLambdaResultTypeDef(TypedDict, total=False):
    ObjectLambdaAccessPointArn: str


class CreateAccessPointResultTypeDef(TypedDict, total=False):
    AccessPointArn: str


class CreateBucketConfigurationTypeDef(TypedDict, total=False):
    LocationConstraint: BucketLocationConstraint


class CreateBucketResultTypeDef(TypedDict, total=False):
    Location: str
    BucketArn: str


class CreateJobResultTypeDef(TypedDict, total=False):
    JobId: str


class DescribeJobResultTypeDef(TypedDict, total=False):
    Job: "JobDescriptorTypeDef"


class ExcludeTypeDef(TypedDict, total=False):
    Buckets: List[str]
    Regions: List[str]


class GetAccessPointConfigurationForObjectLambdaResultTypeDef(TypedDict, total=False):
    Configuration: "ObjectLambdaConfigurationTypeDef"


class GetAccessPointForObjectLambdaResultTypeDef(TypedDict, total=False):
    Name: str
    PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef"
    CreationDate: datetime


class GetAccessPointPolicyForObjectLambdaResultTypeDef(TypedDict, total=False):
    Policy: str


class GetAccessPointPolicyResultTypeDef(TypedDict, total=False):
    Policy: str


class GetAccessPointPolicyStatusForObjectLambdaResultTypeDef(TypedDict, total=False):
    PolicyStatus: "PolicyStatusTypeDef"


class GetAccessPointPolicyStatusResultTypeDef(TypedDict, total=False):
    PolicyStatus: "PolicyStatusTypeDef"


class GetAccessPointResultTypeDef(TypedDict, total=False):
    Name: str
    Bucket: str
    NetworkOrigin: NetworkOrigin
    VpcConfiguration: "VpcConfigurationTypeDef"
    PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef"
    CreationDate: datetime


class GetBucketLifecycleConfigurationResultTypeDef(TypedDict, total=False):
    Rules: List["LifecycleRuleTypeDef"]


class GetBucketPolicyResultTypeDef(TypedDict, total=False):
    Policy: str


class GetBucketResultTypeDef(TypedDict, total=False):
    Bucket: str
    PublicAccessBlockEnabled: bool
    CreationDate: datetime


class GetBucketTaggingResultTypeDef(TypedDict):
    TagSet: List["S3TagTypeDef"]


class GetJobTaggingResultTypeDef(TypedDict, total=False):
    Tags: List["S3TagTypeDef"]


class GetPublicAccessBlockOutputTypeDef(TypedDict):
    PublicAccessBlockConfiguration: "PublicAccessBlockConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetStorageLensConfigurationResultTypeDef(TypedDict, total=False):
    StorageLensConfiguration: "StorageLensConfigurationTypeDef"


class GetStorageLensConfigurationTaggingResultTypeDef(TypedDict, total=False):
    Tags: List["StorageLensTagTypeDef"]


class IncludeTypeDef(TypedDict, total=False):
    Buckets: List[str]
    Regions: List[str]


class JobDescriptorTypeDef(TypedDict, total=False):
    JobId: str
    ConfirmationRequired: bool
    Description: str
    JobArn: str
    Status: JobStatus
    Manifest: "JobManifestTypeDef"
    Operation: "JobOperationTypeDef"
    Priority: int
    ProgressSummary: "JobProgressSummaryTypeDef"
    StatusUpdateReason: str
    FailureReasons: List["JobFailureTypeDef"]
    Report: "JobReportTypeDef"
    CreationTime: datetime
    TerminationDate: datetime
    RoleArn: str
    SuspendedDate: datetime
    SuspendedCause: str


class JobFailureTypeDef(TypedDict, total=False):
    FailureCode: str
    FailureReason: str


class JobListDescriptorTypeDef(TypedDict, total=False):
    JobId: str
    Description: str
    Operation: OperationName
    Priority: int
    Status: JobStatus
    CreationTime: datetime
    TerminationDate: datetime
    ProgressSummary: "JobProgressSummaryTypeDef"


class _RequiredJobManifestLocationTypeDef(TypedDict):
    ObjectArn: str
    ETag: str


class JobManifestLocationTypeDef(_RequiredJobManifestLocationTypeDef, total=False):
    ObjectVersionId: str


class _RequiredJobManifestSpecTypeDef(TypedDict):
    Format: JobManifestFormat


class JobManifestSpecTypeDef(_RequiredJobManifestSpecTypeDef, total=False):
    Fields: List[JobManifestFieldName]


class JobManifestTypeDef(TypedDict):
    Spec: "JobManifestSpecTypeDef"
    Location: "JobManifestLocationTypeDef"


class JobOperationTypeDef(TypedDict, total=False):
    LambdaInvoke: "LambdaInvokeOperationTypeDef"
    S3PutObjectCopy: "S3CopyObjectOperationTypeDef"
    S3PutObjectAcl: "S3SetObjectAclOperationTypeDef"
    S3PutObjectTagging: "S3SetObjectTaggingOperationTypeDef"
    S3DeleteObjectTagging: Dict[str, Any]
    S3InitiateRestoreObject: "S3InitiateRestoreObjectOperationTypeDef"
    S3PutObjectLegalHold: "S3SetObjectLegalHoldOperationTypeDef"
    S3PutObjectRetention: "S3SetObjectRetentionOperationTypeDef"


class JobProgressSummaryTypeDef(TypedDict, total=False):
    TotalNumberOfTasks: int
    NumberOfTasksSucceeded: int
    NumberOfTasksFailed: int


class _RequiredJobReportTypeDef(TypedDict):
    Enabled: bool


class JobReportTypeDef(_RequiredJobReportTypeDef, total=False):
    Bucket: str
    Format: Literal["Report_CSV_20180820"]
    Prefix: str
    ReportScope: JobReportScope


class LambdaInvokeOperationTypeDef(TypedDict, total=False):
    FunctionArn: str


class LifecycleConfigurationTypeDef(TypedDict, total=False):
    Rules: List["LifecycleRuleTypeDef"]


class LifecycleExpirationTypeDef(TypedDict, total=False):
    Date: datetime
    Days: int
    ExpiredObjectDeleteMarker: bool


class LifecycleRuleAndOperatorTypeDef(TypedDict, total=False):
    Prefix: str
    Tags: List["S3TagTypeDef"]


class LifecycleRuleFilterTypeDef(TypedDict, total=False):
    Prefix: str
    Tag: "S3TagTypeDef"
    And: "LifecycleRuleAndOperatorTypeDef"


class _RequiredLifecycleRuleTypeDef(TypedDict):
    Status: ExpirationStatus


class LifecycleRuleTypeDef(_RequiredLifecycleRuleTypeDef, total=False):
    Expiration: "LifecycleExpirationTypeDef"
    ID: str
    Filter: "LifecycleRuleFilterTypeDef"
    Transitions: List["TransitionTypeDef"]
    NoncurrentVersionTransitions: List["NoncurrentVersionTransitionTypeDef"]
    NoncurrentVersionExpiration: "NoncurrentVersionExpirationTypeDef"
    AbortIncompleteMultipartUpload: "AbortIncompleteMultipartUploadTypeDef"


class ListAccessPointsForObjectLambdaResultTypeDef(TypedDict, total=False):
    ObjectLambdaAccessPointList: List["ObjectLambdaAccessPointTypeDef"]
    NextToken: str


class ListAccessPointsResultTypeDef(TypedDict, total=False):
    AccessPointList: List["AccessPointTypeDef"]
    NextToken: str


class ListJobsResultTypeDef(TypedDict, total=False):
    NextToken: str
    Jobs: List["JobListDescriptorTypeDef"]


class ListRegionalBucketsResultTypeDef(TypedDict, total=False):
    RegionalBucketList: List["RegionalBucketTypeDef"]
    NextToken: str


class _RequiredListStorageLensConfigurationEntryTypeDef(TypedDict):
    Id: str
    StorageLensArn: str
    HomeRegion: str


class ListStorageLensConfigurationEntryTypeDef(
    _RequiredListStorageLensConfigurationEntryTypeDef, total=False
):
    IsEnabled: bool


class ListStorageLensConfigurationsResultTypeDef(TypedDict, total=False):
    NextToken: str
    StorageLensConfigurationList: List["ListStorageLensConfigurationEntryTypeDef"]


class NoncurrentVersionExpirationTypeDef(TypedDict, total=False):
    NoncurrentDays: int


class NoncurrentVersionTransitionTypeDef(TypedDict, total=False):
    NoncurrentDays: int
    StorageClass: TransitionStorageClass


class _RequiredObjectLambdaAccessPointTypeDef(TypedDict):
    Name: str


class ObjectLambdaAccessPointTypeDef(_RequiredObjectLambdaAccessPointTypeDef, total=False):
    ObjectLambdaAccessPointArn: str


class _RequiredObjectLambdaConfigurationTypeDef(TypedDict):
    SupportingAccessPoint: str
    TransformationConfigurations: List["ObjectLambdaTransformationConfigurationTypeDef"]


class ObjectLambdaConfigurationTypeDef(_RequiredObjectLambdaConfigurationTypeDef, total=False):
    CloudWatchMetricsEnabled: bool
    AllowedFeatures: List[ObjectLambdaAllowedFeature]


class ObjectLambdaContentTransformationTypeDef(TypedDict, total=False):
    AwsLambda: "AwsLambdaTransformationTypeDef"


class ObjectLambdaTransformationConfigurationTypeDef(TypedDict):
    Actions: List[Literal["GetObject"]]
    ContentTransformation: "ObjectLambdaContentTransformationTypeDef"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PolicyStatusTypeDef(TypedDict, total=False):
    IsPublic: bool


class PrefixLevelStorageMetricsTypeDef(TypedDict, total=False):
    IsEnabled: bool
    SelectionCriteria: "SelectionCriteriaTypeDef"


class PrefixLevelTypeDef(TypedDict):
    StorageMetrics: "PrefixLevelStorageMetricsTypeDef"


class PublicAccessBlockConfigurationTypeDef(TypedDict, total=False):
    BlockPublicAcls: bool
    IgnorePublicAcls: bool
    BlockPublicPolicy: bool
    RestrictPublicBuckets: bool


class _RequiredRegionalBucketTypeDef(TypedDict):
    Bucket: str
    PublicAccessBlockEnabled: bool
    CreationDate: datetime


class RegionalBucketTypeDef(_RequiredRegionalBucketTypeDef, total=False):
    BucketArn: str
    OutpostId: str


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class _RequiredS3AccessControlListTypeDef(TypedDict):
    Owner: "S3ObjectOwnerTypeDef"


class S3AccessControlListTypeDef(_RequiredS3AccessControlListTypeDef, total=False):
    Grants: List["S3GrantTypeDef"]


class S3AccessControlPolicyTypeDef(TypedDict, total=False):
    AccessControlList: "S3AccessControlListTypeDef"
    CannedAccessControlList: S3CannedAccessControlList


class _RequiredS3BucketDestinationTypeDef(TypedDict):
    Format: Format
    OutputSchemaVersion: Literal["V_1"]
    AccountId: str
    Arn: str


class S3BucketDestinationTypeDef(_RequiredS3BucketDestinationTypeDef, total=False):
    Prefix: str
    Encryption: "StorageLensDataExportEncryptionTypeDef"


class S3CopyObjectOperationTypeDef(TypedDict, total=False):
    TargetResource: str
    CannedAccessControlList: S3CannedAccessControlList
    AccessControlGrants: List["S3GrantTypeDef"]
    MetadataDirective: S3MetadataDirective
    ModifiedSinceConstraint: datetime
    NewObjectMetadata: "S3ObjectMetadataTypeDef"
    NewObjectTagging: List["S3TagTypeDef"]
    RedirectLocation: str
    RequesterPays: bool
    StorageClass: S3StorageClass
    UnModifiedSinceConstraint: datetime
    SSEAwsKmsKeyId: str
    TargetKeyPrefix: str
    ObjectLockLegalHoldStatus: S3ObjectLockLegalHoldStatus
    ObjectLockMode: S3ObjectLockMode
    ObjectLockRetainUntilDate: datetime


class S3GrantTypeDef(TypedDict, total=False):
    Grantee: "S3GranteeTypeDef"
    Permission: S3Permission


class S3GranteeTypeDef(TypedDict, total=False):
    TypeIdentifier: S3GranteeTypeIdentifier
    Identifier: str
    DisplayName: str


class S3InitiateRestoreObjectOperationTypeDef(TypedDict, total=False):
    ExpirationInDays: int
    GlacierJobTier: S3GlacierJobTier


class S3ObjectLockLegalHoldTypeDef(TypedDict):
    Status: S3ObjectLockLegalHoldStatus


class S3ObjectMetadataTypeDef(TypedDict, total=False):
    CacheControl: str
    ContentDisposition: str
    ContentEncoding: str
    ContentLanguage: str
    UserMetadata: Dict[str, str]
    ContentLength: int
    ContentMD5: str
    ContentType: str
    HttpExpiresDate: datetime
    RequesterCharged: bool
    SSEAlgorithm: S3SSEAlgorithm


class S3ObjectOwnerTypeDef(TypedDict, total=False):
    ID: str
    DisplayName: str


class S3RetentionTypeDef(TypedDict, total=False):
    RetainUntilDate: datetime
    Mode: S3ObjectLockRetentionMode


class S3SetObjectAclOperationTypeDef(TypedDict, total=False):
    AccessControlPolicy: "S3AccessControlPolicyTypeDef"


class S3SetObjectLegalHoldOperationTypeDef(TypedDict):
    LegalHold: "S3ObjectLockLegalHoldTypeDef"


class _RequiredS3SetObjectRetentionOperationTypeDef(TypedDict):
    Retention: "S3RetentionTypeDef"


class S3SetObjectRetentionOperationTypeDef(
    _RequiredS3SetObjectRetentionOperationTypeDef, total=False
):
    BypassGovernanceRetention: bool


class S3SetObjectTaggingOperationTypeDef(TypedDict, total=False):
    TagSet: List["S3TagTypeDef"]


class S3TagTypeDef(TypedDict):
    Key: str
    Value: str


class SSEKMSTypeDef(TypedDict):
    KeyId: str


class SelectionCriteriaTypeDef(TypedDict, total=False):
    Delimiter: str
    MaxDepth: int
    MinStorageBytesPercentage: float


class StorageLensAwsOrgTypeDef(TypedDict):
    Arn: str


class _RequiredStorageLensConfigurationTypeDef(TypedDict):
    Id: str
    AccountLevel: "AccountLevelTypeDef"
    IsEnabled: bool


class StorageLensConfigurationTypeDef(_RequiredStorageLensConfigurationTypeDef, total=False):
    Include: "IncludeTypeDef"
    Exclude: "ExcludeTypeDef"
    DataExport: "StorageLensDataExportTypeDef"
    AwsOrg: "StorageLensAwsOrgTypeDef"
    StorageLensArn: str


class StorageLensDataExportEncryptionTypeDef(TypedDict, total=False):
    SSES3: Dict[str, Any]
    SSEKMS: "SSEKMSTypeDef"


class StorageLensDataExportTypeDef(TypedDict):
    S3BucketDestination: "S3BucketDestinationTypeDef"


class StorageLensTagTypeDef(TypedDict):
    Key: str
    Value: str


class TaggingTypeDef(TypedDict):
    TagSet: List["S3TagTypeDef"]


class TransitionTypeDef(TypedDict, total=False):
    Date: datetime
    Days: int
    StorageClass: TransitionStorageClass


class UpdateJobPriorityResultTypeDef(TypedDict):
    JobId: str
    Priority: int


class UpdateJobStatusResultTypeDef(TypedDict, total=False):
    JobId: str
    Status: JobStatus
    StatusUpdateReason: str


class VpcConfigurationTypeDef(TypedDict):
    VpcId: str
