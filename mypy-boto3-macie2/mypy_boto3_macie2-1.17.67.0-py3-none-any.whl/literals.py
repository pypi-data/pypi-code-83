"""
Type annotations for macie2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/literals.html)

Usage::

    ```python
    from mypy_boto3_macie2.literals import AdminStatus

    data: AdminStatus = "DISABLING_IN_PROGRESS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AdminStatus",
    "AllowsUnencryptedObjectUploads",
    "Currency",
    "DayOfWeek",
    "DescribeBucketsPaginatorName",
    "EffectivePermission",
    "EncryptionType",
    "ErrorCode",
    "FindingActionType",
    "FindingCategory",
    "FindingPublishingFrequency",
    "FindingStatisticsSortAttributeName",
    "FindingType",
    "FindingsFilterAction",
    "GetUsageStatisticsPaginatorName",
    "GroupBy",
    "IsDefinedInJob",
    "IsMonitoredByJob",
    "JobComparator",
    "JobStatus",
    "JobType",
    "LastRunErrorStatusCode",
    "ListClassificationJobsPaginatorName",
    "ListCustomDataIdentifiersPaginatorName",
    "ListFindingsFiltersPaginatorName",
    "ListFindingsPaginatorName",
    "ListInvitationsPaginatorName",
    "ListJobsFilterKey",
    "ListJobsSortAttributeName",
    "ListMembersPaginatorName",
    "ListOrganizationAdminAccountsPaginatorName",
    "MacieStatus",
    "OrderBy",
    "RelationshipStatus",
    "ScopeFilterKey",
    "SensitiveDataItemCategory",
    "SeverityDescription",
    "SharedAccess",
    "StorageClass",
    "TagTarget",
    "TimeRange",
    "TypeType",
    "Unit",
    "UsageStatisticsFilterComparator",
    "UsageStatisticsFilterKey",
    "UsageStatisticsSortKey",
    "UsageType",
    "UserIdentityType",
)


AdminStatus = Literal["DISABLING_IN_PROGRESS", "ENABLED"]
AllowsUnencryptedObjectUploads = Literal["FALSE", "TRUE", "UNKNOWN"]
Currency = Literal["USD"]
DayOfWeek = Literal["FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"]
DescribeBucketsPaginatorName = Literal["describe_buckets"]
EffectivePermission = Literal["NOT_PUBLIC", "PUBLIC", "UNKNOWN"]
EncryptionType = Literal["AES256", "NONE", "UNKNOWN", "aws:kms"]
ErrorCode = Literal["ClientError", "InternalError"]
FindingActionType = Literal["AWS_API_CALL"]
FindingCategory = Literal["CLASSIFICATION", "POLICY"]
FindingPublishingFrequency = Literal["FIFTEEN_MINUTES", "ONE_HOUR", "SIX_HOURS"]
FindingStatisticsSortAttributeName = Literal["count", "groupKey"]
FindingType = Literal[
    "Policy:IAMUser/S3BlockPublicAccessDisabled",
    "Policy:IAMUser/S3BucketEncryptionDisabled",
    "Policy:IAMUser/S3BucketPublic",
    "Policy:IAMUser/S3BucketReplicatedExternally",
    "Policy:IAMUser/S3BucketSharedExternally",
    "SensitiveData:S3Object/Credentials",
    "SensitiveData:S3Object/CustomIdentifier",
    "SensitiveData:S3Object/Financial",
    "SensitiveData:S3Object/Multiple",
    "SensitiveData:S3Object/Personal",
]
FindingsFilterAction = Literal["ARCHIVE", "NOOP"]
GetUsageStatisticsPaginatorName = Literal["get_usage_statistics"]
GroupBy = Literal[
    "classificationDetails.jobId", "resourcesAffected.s3Bucket.name", "severity.description", "type"
]
IsDefinedInJob = Literal["FALSE", "TRUE", "UNKNOWN"]
IsMonitoredByJob = Literal["FALSE", "TRUE", "UNKNOWN"]
JobComparator = Literal["CONTAINS", "EQ", "GT", "GTE", "LT", "LTE", "NE", "STARTS_WITH"]
JobStatus = Literal["CANCELLED", "COMPLETE", "IDLE", "PAUSED", "RUNNING", "USER_PAUSED"]
JobType = Literal["ONE_TIME", "SCHEDULED"]
LastRunErrorStatusCode = Literal["ERROR", "NONE"]
ListClassificationJobsPaginatorName = Literal["list_classification_jobs"]
ListCustomDataIdentifiersPaginatorName = Literal["list_custom_data_identifiers"]
ListFindingsFiltersPaginatorName = Literal["list_findings_filters"]
ListFindingsPaginatorName = Literal["list_findings"]
ListInvitationsPaginatorName = Literal["list_invitations"]
ListJobsFilterKey = Literal["createdAt", "jobStatus", "jobType", "name"]
ListJobsSortAttributeName = Literal["createdAt", "jobStatus", "jobType", "name"]
ListMembersPaginatorName = Literal["list_members"]
ListOrganizationAdminAccountsPaginatorName = Literal["list_organization_admin_accounts"]
MacieStatus = Literal["ENABLED", "PAUSED"]
OrderBy = Literal["ASC", "DESC"]
RelationshipStatus = Literal[
    "AccountSuspended",
    "Created",
    "EmailVerificationFailed",
    "EmailVerificationInProgress",
    "Enabled",
    "Invited",
    "Paused",
    "RegionDisabled",
    "Removed",
    "Resigned",
]
ScopeFilterKey = Literal[
    "BUCKET_CREATION_DATE",
    "OBJECT_EXTENSION",
    "OBJECT_KEY",
    "OBJECT_LAST_MODIFIED_DATE",
    "OBJECT_SIZE",
    "TAG",
]
SensitiveDataItemCategory = Literal[
    "CREDENTIALS", "CUSTOM_IDENTIFIER", "FINANCIAL_INFORMATION", "PERSONAL_INFORMATION"
]
SeverityDescription = Literal["High", "Low", "Medium"]
SharedAccess = Literal["EXTERNAL", "INTERNAL", "NOT_SHARED", "UNKNOWN"]
StorageClass = Literal[
    "DEEP_ARCHIVE",
    "GLACIER",
    "INTELLIGENT_TIERING",
    "ONEZONE_IA",
    "REDUCED_REDUNDANCY",
    "STANDARD",
    "STANDARD_IA",
]
TagTarget = Literal["S3_OBJECT"]
TimeRange = Literal["MONTH_TO_DATE", "PAST_30_DAYS"]
TypeType = Literal["AES256", "NONE", "aws:kms"]
Unit = Literal["TERABYTES"]
UsageStatisticsFilterComparator = Literal["CONTAINS", "EQ", "GT", "GTE", "LT", "LTE", "NE"]
UsageStatisticsFilterKey = Literal["accountId", "freeTrialStartDate", "serviceLimit", "total"]
UsageStatisticsSortKey = Literal["accountId", "freeTrialStartDate", "serviceLimitValue", "total"]
UsageType = Literal["DATA_INVENTORY_EVALUATION", "SENSITIVE_DATA_DISCOVERY"]
UserIdentityType = Literal[
    "AWSAccount", "AWSService", "AssumedRole", "FederatedUser", "IAMUser", "Root"
]
