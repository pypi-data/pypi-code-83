"""
Type annotations for macie2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_macie2.type_defs import AccessControlListTypeDef

    data: AccessControlListTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_macie2.literals import (
    AdminStatus,
    AllowsUnencryptedObjectUploads,
    DayOfWeek,
    EffectivePermission,
    EncryptionType,
    ErrorCode,
    FindingCategory,
    FindingPublishingFrequency,
    FindingsFilterAction,
    FindingStatisticsSortAttributeName,
    FindingType,
    IsDefinedInJob,
    IsMonitoredByJob,
    JobComparator,
    JobStatus,
    JobType,
    LastRunErrorStatusCode,
    ListJobsFilterKey,
    ListJobsSortAttributeName,
    MacieStatus,
    OrderBy,
    RelationshipStatus,
    ScopeFilterKey,
    SensitiveDataItemCategory,
    SeverityDescription,
    SharedAccess,
    StorageClass,
    TimeRange,
    TypeType,
    UsageStatisticsFilterComparator,
    UsageStatisticsFilterKey,
    UsageStatisticsSortKey,
    UsageType,
    UserIdentityType,
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
    "AccessControlListTypeDef",
    "AccountDetailTypeDef",
    "AccountLevelPermissionsTypeDef",
    "AdminAccountTypeDef",
    "ApiCallDetailsTypeDef",
    "AssumedRoleTypeDef",
    "AwsAccountTypeDef",
    "AwsServiceTypeDef",
    "BatchGetCustomDataIdentifierSummaryTypeDef",
    "BatchGetCustomDataIdentifiersResponseTypeDef",
    "BlockPublicAccessTypeDef",
    "BucketCountByEffectivePermissionTypeDef",
    "BucketCountByEncryptionTypeTypeDef",
    "BucketCountBySharedAccessTypeTypeDef",
    "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
    "BucketCriteriaAdditionalPropertiesTypeDef",
    "BucketLevelPermissionsTypeDef",
    "BucketMetadataTypeDef",
    "BucketPermissionConfigurationTypeDef",
    "BucketPolicyTypeDef",
    "BucketPublicAccessTypeDef",
    "BucketServerSideEncryptionTypeDef",
    "BucketSortCriteriaTypeDef",
    "CellTypeDef",
    "ClassificationDetailsTypeDef",
    "ClassificationExportConfigurationTypeDef",
    "ClassificationResultStatusTypeDef",
    "ClassificationResultTypeDef",
    "CreateClassificationJobResponseTypeDef",
    "CreateCustomDataIdentifierResponseTypeDef",
    "CreateFindingsFilterResponseTypeDef",
    "CreateInvitationsResponseTypeDef",
    "CreateMemberResponseTypeDef",
    "CriterionAdditionalPropertiesTypeDef",
    "CustomDataIdentifierSummaryTypeDef",
    "CustomDataIdentifiersTypeDef",
    "CustomDetectionTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DefaultDetectionTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DescribeBucketsResponseTypeDef",
    "DescribeClassificationJobResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DomainDetailsTypeDef",
    "FederatedUserTypeDef",
    "FindingActionTypeDef",
    "FindingActorTypeDef",
    "FindingCriteriaTypeDef",
    "FindingStatisticsSortCriteriaTypeDef",
    "FindingTypeDef",
    "FindingsFilterListItemTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetBucketStatisticsResponseTypeDef",
    "GetClassificationExportConfigurationResponseTypeDef",
    "GetCustomDataIdentifierResponseTypeDef",
    "GetFindingStatisticsResponseTypeDef",
    "GetFindingsFilterResponseTypeDef",
    "GetFindingsPublicationConfigurationResponseTypeDef",
    "GetFindingsResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMacieSessionResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMemberResponseTypeDef",
    "GetUsageStatisticsResponseTypeDef",
    "GetUsageTotalsResponseTypeDef",
    "GroupCountTypeDef",
    "IamUserTypeDef",
    "InvitationTypeDef",
    "IpAddressDetailsTypeDef",
    "IpCityTypeDef",
    "IpCountryTypeDef",
    "IpGeoLocationTypeDef",
    "IpOwnerTypeDef",
    "JobDetailsTypeDef",
    "JobScheduleFrequencyTypeDef",
    "JobScopeTermTypeDef",
    "JobScopingBlockTypeDef",
    "JobSummaryTypeDef",
    "KeyValuePairTypeDef",
    "LastRunErrorStatusTypeDef",
    "ListClassificationJobsResponseTypeDef",
    "ListCustomDataIdentifiersResponseTypeDef",
    "ListFindingsFiltersResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListJobsFilterCriteriaTypeDef",
    "ListJobsFilterTermTypeDef",
    "ListJobsSortCriteriaTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MemberTypeDef",
    "MonthlyScheduleTypeDef",
    "ObjectCountByEncryptionTypeTypeDef",
    "ObjectLevelStatisticsTypeDef",
    "OccurrencesTypeDef",
    "PageTypeDef",
    "PaginatorConfigTypeDef",
    "PolicyDetailsTypeDef",
    "PutClassificationExportConfigurationResponseTypeDef",
    "RangeTypeDef",
    "RecordTypeDef",
    "ReplicationDetailsTypeDef",
    "ResourcesAffectedTypeDef",
    "S3BucketDefinitionForJobTypeDef",
    "S3BucketOwnerTypeDef",
    "S3BucketTypeDef",
    "S3DestinationTypeDef",
    "S3JobDefinitionTypeDef",
    "S3ObjectTypeDef",
    "ScopingTypeDef",
    "SecurityHubConfigurationTypeDef",
    "SensitiveDataItemTypeDef",
    "ServerSideEncryptionTypeDef",
    "ServiceLimitTypeDef",
    "SessionContextAttributesTypeDef",
    "SessionContextTypeDef",
    "SessionIssuerTypeDef",
    "SeverityTypeDef",
    "SimpleScopeTermTypeDef",
    "SortCriteriaTypeDef",
    "StatisticsTypeDef",
    "TagScopeTermTypeDef",
    "TagValuePairTypeDef",
    "TestCustomDataIdentifierResponseTypeDef",
    "UnprocessedAccountTypeDef",
    "UpdateFindingsFilterResponseTypeDef",
    "UsageByAccountTypeDef",
    "UsageRecordTypeDef",
    "UsageStatisticsFilterTypeDef",
    "UsageStatisticsSortByTypeDef",
    "UsageTotalTypeDef",
    "UserIdentityRootTypeDef",
    "UserIdentityTypeDef",
    "UserPausedDetailsTypeDef",
    "WeeklyScheduleTypeDef",
)


class AccessControlListTypeDef(TypedDict, total=False):
    allowsPublicReadAccess: bool
    allowsPublicWriteAccess: bool


class AccountDetailTypeDef(TypedDict):
    accountId: str
    email: str


class AccountLevelPermissionsTypeDef(TypedDict, total=False):
    blockPublicAccess: "BlockPublicAccessTypeDef"


class AdminAccountTypeDef(TypedDict, total=False):
    accountId: str
    status: AdminStatus


class ApiCallDetailsTypeDef(TypedDict, total=False):
    api: str
    apiServiceName: str
    firstSeen: datetime
    lastSeen: datetime


class AssumedRoleTypeDef(TypedDict, total=False):
    accessKeyId: str
    accountId: str
    arn: str
    principalId: str
    sessionContext: "SessionContextTypeDef"


class AwsAccountTypeDef(TypedDict, total=False):
    accountId: str
    principalId: str


class AwsServiceTypeDef(TypedDict, total=False):
    invokedBy: str


BatchGetCustomDataIdentifierSummaryTypeDef = TypedDict(
    "BatchGetCustomDataIdentifierSummaryTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deleted": bool,
        "description": str,
        "id": str,
        "name": str,
    },
    total=False,
)


class BatchGetCustomDataIdentifiersResponseTypeDef(TypedDict, total=False):
    customDataIdentifiers: List["BatchGetCustomDataIdentifierSummaryTypeDef"]
    notFoundIdentifierIds: List[str]


class BlockPublicAccessTypeDef(TypedDict, total=False):
    blockPublicAcls: bool
    blockPublicPolicy: bool
    ignorePublicAcls: bool
    restrictPublicBuckets: bool


class BucketCountByEffectivePermissionTypeDef(TypedDict, total=False):
    publiclyAccessible: int
    publiclyReadable: int
    publiclyWritable: int
    unknown: int


class BucketCountByEncryptionTypeTypeDef(TypedDict, total=False):
    kmsManaged: int
    s3Managed: int
    unencrypted: int
    unknown: int


class BucketCountBySharedAccessTypeTypeDef(TypedDict, total=False):
    external: int
    internal: int
    notShared: int
    unknown: int


class BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef(TypedDict, total=False):
    allowsUnencryptedObjectUploads: int
    deniesUnencryptedObjectUploads: int
    unknown: int


class BucketCriteriaAdditionalPropertiesTypeDef(TypedDict, total=False):
    eq: List[str]
    gt: int
    gte: int
    lt: int
    lte: int
    neq: List[str]
    prefix: str


class BucketLevelPermissionsTypeDef(TypedDict, total=False):
    accessControlList: "AccessControlListTypeDef"
    blockPublicAccess: "BlockPublicAccessTypeDef"
    bucketPolicy: "BucketPolicyTypeDef"


class BucketMetadataTypeDef(TypedDict, total=False):
    accountId: str
    allowsUnencryptedObjectUploads: AllowsUnencryptedObjectUploads
    bucketArn: str
    bucketCreatedAt: datetime
    bucketName: str
    classifiableObjectCount: int
    classifiableSizeInBytes: int
    jobDetails: "JobDetailsTypeDef"
    lastUpdated: datetime
    objectCount: int
    objectCountByEncryptionType: "ObjectCountByEncryptionTypeTypeDef"
    publicAccess: "BucketPublicAccessTypeDef"
    region: str
    replicationDetails: "ReplicationDetailsTypeDef"
    serverSideEncryption: "BucketServerSideEncryptionTypeDef"
    sharedAccess: SharedAccess
    sizeInBytes: int
    sizeInBytesCompressed: int
    tags: List["KeyValuePairTypeDef"]
    unclassifiableObjectCount: "ObjectLevelStatisticsTypeDef"
    unclassifiableObjectSizeInBytes: "ObjectLevelStatisticsTypeDef"
    versioning: bool


class BucketPermissionConfigurationTypeDef(TypedDict, total=False):
    accountLevelPermissions: "AccountLevelPermissionsTypeDef"
    bucketLevelPermissions: "BucketLevelPermissionsTypeDef"


class BucketPolicyTypeDef(TypedDict, total=False):
    allowsPublicReadAccess: bool
    allowsPublicWriteAccess: bool


class BucketPublicAccessTypeDef(TypedDict, total=False):
    effectivePermission: EffectivePermission
    permissionConfiguration: "BucketPermissionConfigurationTypeDef"


BucketServerSideEncryptionTypeDef = TypedDict(
    "BucketServerSideEncryptionTypeDef", {"kmsMasterKeyId": str, "type": TypeType}, total=False
)


class BucketSortCriteriaTypeDef(TypedDict, total=False):
    attributeName: str
    orderBy: OrderBy


class CellTypeDef(TypedDict, total=False):
    cellReference: str
    column: int
    columnName: str
    row: int


class ClassificationDetailsTypeDef(TypedDict, total=False):
    detailedResultsLocation: str
    jobArn: str
    jobId: str
    result: "ClassificationResultTypeDef"


class ClassificationExportConfigurationTypeDef(TypedDict, total=False):
    s3Destination: "S3DestinationTypeDef"


class ClassificationResultStatusTypeDef(TypedDict, total=False):
    code: str
    reason: str


class ClassificationResultTypeDef(TypedDict, total=False):
    additionalOccurrences: bool
    customDataIdentifiers: "CustomDataIdentifiersTypeDef"
    mimeType: str
    sensitiveData: List["SensitiveDataItemTypeDef"]
    sizeClassified: int
    status: "ClassificationResultStatusTypeDef"


class CreateClassificationJobResponseTypeDef(TypedDict, total=False):
    jobArn: str
    jobId: str


class CreateCustomDataIdentifierResponseTypeDef(TypedDict, total=False):
    customDataIdentifierId: str


CreateFindingsFilterResponseTypeDef = TypedDict(
    "CreateFindingsFilterResponseTypeDef", {"arn": str, "id": str}, total=False
)


class CreateInvitationsResponseTypeDef(TypedDict, total=False):
    unprocessedAccounts: List["UnprocessedAccountTypeDef"]


class CreateMemberResponseTypeDef(TypedDict, total=False):
    arn: str


class CriterionAdditionalPropertiesTypeDef(TypedDict, total=False):
    eq: List[str]
    eqExactMatch: List[str]
    gt: int
    gte: int
    lt: int
    lte: int
    neq: List[str]


CustomDataIdentifierSummaryTypeDef = TypedDict(
    "CustomDataIdentifierSummaryTypeDef",
    {"arn": str, "createdAt": datetime, "description": str, "id": str, "name": str},
    total=False,
)


class CustomDataIdentifiersTypeDef(TypedDict, total=False):
    detections: List["CustomDetectionTypeDef"]
    totalCount: int


class CustomDetectionTypeDef(TypedDict, total=False):
    arn: str
    count: int
    name: str
    occurrences: "OccurrencesTypeDef"


class DeclineInvitationsResponseTypeDef(TypedDict, total=False):
    unprocessedAccounts: List["UnprocessedAccountTypeDef"]


DefaultDetectionTypeDef = TypedDict(
    "DefaultDetectionTypeDef",
    {"count": int, "occurrences": "OccurrencesTypeDef", "type": str},
    total=False,
)


class DeleteInvitationsResponseTypeDef(TypedDict, total=False):
    unprocessedAccounts: List["UnprocessedAccountTypeDef"]


class DescribeBucketsResponseTypeDef(TypedDict, total=False):
    buckets: List["BucketMetadataTypeDef"]
    nextToken: str


class DescribeClassificationJobResponseTypeDef(TypedDict, total=False):
    clientToken: str
    createdAt: datetime
    customDataIdentifierIds: List[str]
    description: str
    initialRun: bool
    jobArn: str
    jobId: str
    jobStatus: JobStatus
    jobType: JobType
    lastRunErrorStatus: "LastRunErrorStatusTypeDef"
    lastRunTime: datetime
    name: str
    s3JobDefinition: "S3JobDefinitionTypeDef"
    samplingPercentage: int
    scheduleFrequency: "JobScheduleFrequencyTypeDef"
    statistics: "StatisticsTypeDef"
    tags: Dict[str, str]
    userPausedDetails: "UserPausedDetailsTypeDef"


class DescribeOrganizationConfigurationResponseTypeDef(TypedDict, total=False):
    autoEnable: bool
    maxAccountLimitReached: bool


class DomainDetailsTypeDef(TypedDict, total=False):
    domainName: str


class FederatedUserTypeDef(TypedDict, total=False):
    accessKeyId: str
    accountId: str
    arn: str
    principalId: str
    sessionContext: "SessionContextTypeDef"


class FindingActionTypeDef(TypedDict, total=False):
    actionType: Literal["AWS_API_CALL"]
    apiCallDetails: "ApiCallDetailsTypeDef"


class FindingActorTypeDef(TypedDict, total=False):
    domainDetails: "DomainDetailsTypeDef"
    ipAddressDetails: "IpAddressDetailsTypeDef"
    userIdentity: "UserIdentityTypeDef"


class FindingCriteriaTypeDef(TypedDict, total=False):
    criterion: Dict[str, "CriterionAdditionalPropertiesTypeDef"]


class FindingStatisticsSortCriteriaTypeDef(TypedDict, total=False):
    attributeName: FindingStatisticsSortAttributeName
    orderBy: OrderBy


FindingTypeDef = TypedDict(
    "FindingTypeDef",
    {
        "accountId": str,
        "archived": bool,
        "category": FindingCategory,
        "classificationDetails": "ClassificationDetailsTypeDef",
        "count": int,
        "createdAt": datetime,
        "description": str,
        "id": str,
        "partition": str,
        "policyDetails": "PolicyDetailsTypeDef",
        "region": str,
        "resourcesAffected": "ResourcesAffectedTypeDef",
        "sample": bool,
        "schemaVersion": str,
        "severity": "SeverityTypeDef",
        "title": str,
        "type": FindingType,
        "updatedAt": datetime,
    },
    total=False,
)

FindingsFilterListItemTypeDef = TypedDict(
    "FindingsFilterListItemTypeDef",
    {"action": FindingsFilterAction, "arn": str, "id": str, "name": str, "tags": Dict[str, str]},
    total=False,
)


class GetAdministratorAccountResponseTypeDef(TypedDict, total=False):
    administrator: "InvitationTypeDef"


class GetBucketStatisticsResponseTypeDef(TypedDict, total=False):
    bucketCount: int
    bucketCountByEffectivePermission: "BucketCountByEffectivePermissionTypeDef"
    bucketCountByEncryptionType: "BucketCountByEncryptionTypeTypeDef"
    bucketCountByObjectEncryptionRequirement: "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef"
    bucketCountBySharedAccessType: "BucketCountBySharedAccessTypeTypeDef"
    classifiableObjectCount: int
    classifiableSizeInBytes: int
    lastUpdated: datetime
    objectCount: int
    sizeInBytes: int
    sizeInBytesCompressed: int
    unclassifiableObjectCount: "ObjectLevelStatisticsTypeDef"
    unclassifiableObjectSizeInBytes: "ObjectLevelStatisticsTypeDef"


class GetClassificationExportConfigurationResponseTypeDef(TypedDict, total=False):
    configuration: "ClassificationExportConfigurationTypeDef"


GetCustomDataIdentifierResponseTypeDef = TypedDict(
    "GetCustomDataIdentifierResponseTypeDef",
    {
        "arn": str,
        "createdAt": datetime,
        "deleted": bool,
        "description": str,
        "id": str,
        "ignoreWords": List[str],
        "keywords": List[str],
        "maximumMatchDistance": int,
        "name": str,
        "regex": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class GetFindingStatisticsResponseTypeDef(TypedDict, total=False):
    countsByGroup: List["GroupCountTypeDef"]


GetFindingsFilterResponseTypeDef = TypedDict(
    "GetFindingsFilterResponseTypeDef",
    {
        "action": FindingsFilterAction,
        "arn": str,
        "description": str,
        "findingCriteria": "FindingCriteriaTypeDef",
        "id": str,
        "name": str,
        "position": int,
        "tags": Dict[str, str],
    },
    total=False,
)


class GetFindingsPublicationConfigurationResponseTypeDef(TypedDict, total=False):
    securityHubConfiguration: "SecurityHubConfigurationTypeDef"


class GetFindingsResponseTypeDef(TypedDict, total=False):
    findings: List["FindingTypeDef"]


class GetInvitationsCountResponseTypeDef(TypedDict, total=False):
    invitationsCount: int


class GetMacieSessionResponseTypeDef(TypedDict, total=False):
    createdAt: datetime
    findingPublishingFrequency: FindingPublishingFrequency
    serviceRole: str
    status: MacieStatus
    updatedAt: datetime


class GetMasterAccountResponseTypeDef(TypedDict, total=False):
    master: "InvitationTypeDef"


class GetMemberResponseTypeDef(TypedDict, total=False):
    accountId: str
    administratorAccountId: str
    arn: str
    email: str
    invitedAt: datetime
    masterAccountId: str
    relationshipStatus: RelationshipStatus
    tags: Dict[str, str]
    updatedAt: datetime


class GetUsageStatisticsResponseTypeDef(TypedDict, total=False):
    nextToken: str
    records: List["UsageRecordTypeDef"]
    timeRange: TimeRange


class GetUsageTotalsResponseTypeDef(TypedDict, total=False):
    timeRange: TimeRange
    usageTotals: List["UsageTotalTypeDef"]


class GroupCountTypeDef(TypedDict, total=False):
    count: int
    groupKey: str


class IamUserTypeDef(TypedDict, total=False):
    accountId: str
    arn: str
    principalId: str
    userName: str


class InvitationTypeDef(TypedDict, total=False):
    accountId: str
    invitationId: str
    invitedAt: datetime
    relationshipStatus: RelationshipStatus


class IpAddressDetailsTypeDef(TypedDict, total=False):
    ipAddressV4: str
    ipCity: "IpCityTypeDef"
    ipCountry: "IpCountryTypeDef"
    ipGeoLocation: "IpGeoLocationTypeDef"
    ipOwner: "IpOwnerTypeDef"


class IpCityTypeDef(TypedDict, total=False):
    name: str


class IpCountryTypeDef(TypedDict, total=False):
    code: str
    name: str


class IpGeoLocationTypeDef(TypedDict, total=False):
    lat: float
    lon: float


class IpOwnerTypeDef(TypedDict, total=False):
    asn: str
    asnOrg: str
    isp: str
    org: str


class JobDetailsTypeDef(TypedDict, total=False):
    isDefinedInJob: IsDefinedInJob
    isMonitoredByJob: IsMonitoredByJob
    lastJobId: str
    lastJobRunTime: datetime


class JobScheduleFrequencyTypeDef(TypedDict, total=False):
    dailySchedule: Dict[str, Any]
    monthlySchedule: "MonthlyScheduleTypeDef"
    weeklySchedule: "WeeklyScheduleTypeDef"


class JobScopeTermTypeDef(TypedDict, total=False):
    simpleScopeTerm: "SimpleScopeTermTypeDef"
    tagScopeTerm: "TagScopeTermTypeDef"


JobScopingBlockTypeDef = TypedDict(
    "JobScopingBlockTypeDef", {"and": List["JobScopeTermTypeDef"]}, total=False
)


class JobSummaryTypeDef(TypedDict, total=False):
    bucketDefinitions: List["S3BucketDefinitionForJobTypeDef"]
    createdAt: datetime
    jobId: str
    jobStatus: JobStatus
    jobType: JobType
    lastRunErrorStatus: "LastRunErrorStatusTypeDef"
    name: str
    userPausedDetails: "UserPausedDetailsTypeDef"


class KeyValuePairTypeDef(TypedDict, total=False):
    key: str
    value: str


class LastRunErrorStatusTypeDef(TypedDict, total=False):
    code: LastRunErrorStatusCode


class ListClassificationJobsResponseTypeDef(TypedDict, total=False):
    items: List["JobSummaryTypeDef"]
    nextToken: str


class ListCustomDataIdentifiersResponseTypeDef(TypedDict, total=False):
    items: List["CustomDataIdentifierSummaryTypeDef"]
    nextToken: str


class ListFindingsFiltersResponseTypeDef(TypedDict, total=False):
    findingsFilterListItems: List["FindingsFilterListItemTypeDef"]
    nextToken: str


class ListFindingsResponseTypeDef(TypedDict, total=False):
    findingIds: List[str]
    nextToken: str


class ListInvitationsResponseTypeDef(TypedDict, total=False):
    invitations: List["InvitationTypeDef"]
    nextToken: str


class ListJobsFilterCriteriaTypeDef(TypedDict, total=False):
    excludes: List["ListJobsFilterTermTypeDef"]
    includes: List["ListJobsFilterTermTypeDef"]


class ListJobsFilterTermTypeDef(TypedDict, total=False):
    comparator: JobComparator
    key: ListJobsFilterKey
    values: List[str]


class ListJobsSortCriteriaTypeDef(TypedDict, total=False):
    attributeName: ListJobsSortAttributeName
    orderBy: OrderBy


class ListMembersResponseTypeDef(TypedDict, total=False):
    members: List["MemberTypeDef"]
    nextToken: str


class ListOrganizationAdminAccountsResponseTypeDef(TypedDict, total=False):
    adminAccounts: List["AdminAccountTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class MemberTypeDef(TypedDict, total=False):
    accountId: str
    administratorAccountId: str
    arn: str
    email: str
    invitedAt: datetime
    masterAccountId: str
    relationshipStatus: RelationshipStatus
    tags: Dict[str, str]
    updatedAt: datetime


class MonthlyScheduleTypeDef(TypedDict, total=False):
    dayOfMonth: int


class ObjectCountByEncryptionTypeTypeDef(TypedDict, total=False):
    customerManaged: int
    kmsManaged: int
    s3Managed: int
    unencrypted: int
    unknown: int


class ObjectLevelStatisticsTypeDef(TypedDict, total=False):
    fileType: int
    storageClass: int
    total: int


class OccurrencesTypeDef(TypedDict, total=False):
    cells: List["CellTypeDef"]
    lineRanges: List["RangeTypeDef"]
    offsetRanges: List["RangeTypeDef"]
    pages: List["PageTypeDef"]
    records: List["RecordTypeDef"]


class PageTypeDef(TypedDict, total=False):
    lineRange: "RangeTypeDef"
    offsetRange: "RangeTypeDef"
    pageNumber: int


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PolicyDetailsTypeDef(TypedDict, total=False):
    action: "FindingActionTypeDef"
    actor: "FindingActorTypeDef"


class PutClassificationExportConfigurationResponseTypeDef(TypedDict, total=False):
    configuration: "ClassificationExportConfigurationTypeDef"


class RangeTypeDef(TypedDict, total=False):
    end: int
    start: int
    startColumn: int


class RecordTypeDef(TypedDict, total=False):
    jsonPath: str
    recordIndex: int


class ReplicationDetailsTypeDef(TypedDict, total=False):
    replicated: bool
    replicatedExternally: bool
    replicationAccounts: List[str]


class ResourcesAffectedTypeDef(TypedDict, total=False):
    s3Bucket: "S3BucketTypeDef"
    s3Object: "S3ObjectTypeDef"


class S3BucketDefinitionForJobTypeDef(TypedDict):
    accountId: str
    buckets: List[str]


S3BucketOwnerTypeDef = TypedDict(
    "S3BucketOwnerTypeDef", {"displayName": str, "id": str}, total=False
)


class S3BucketTypeDef(TypedDict, total=False):
    allowsUnencryptedObjectUploads: AllowsUnencryptedObjectUploads
    arn: str
    createdAt: datetime
    defaultServerSideEncryption: "ServerSideEncryptionTypeDef"
    name: str
    owner: "S3BucketOwnerTypeDef"
    publicAccess: "BucketPublicAccessTypeDef"
    tags: List["KeyValuePairTypeDef"]


class _RequiredS3DestinationTypeDef(TypedDict):
    bucketName: str
    kmsKeyArn: str


class S3DestinationTypeDef(_RequiredS3DestinationTypeDef, total=False):
    keyPrefix: str


class S3JobDefinitionTypeDef(TypedDict, total=False):
    bucketDefinitions: List["S3BucketDefinitionForJobTypeDef"]
    scoping: "ScopingTypeDef"


class S3ObjectTypeDef(TypedDict, total=False):
    bucketArn: str
    eTag: str
    extension: str
    key: str
    lastModified: datetime
    path: str
    publicAccess: bool
    serverSideEncryption: "ServerSideEncryptionTypeDef"
    size: int
    storageClass: StorageClass
    tags: List["KeyValuePairTypeDef"]
    versionId: str


class ScopingTypeDef(TypedDict, total=False):
    excludes: "JobScopingBlockTypeDef"
    includes: "JobScopingBlockTypeDef"


class SecurityHubConfigurationTypeDef(TypedDict):
    publishClassificationFindings: bool
    publishPolicyFindings: bool


class SensitiveDataItemTypeDef(TypedDict, total=False):
    category: SensitiveDataItemCategory
    detections: List["DefaultDetectionTypeDef"]
    totalCount: int


class ServerSideEncryptionTypeDef(TypedDict, total=False):
    encryptionType: EncryptionType
    kmsMasterKeyId: str


class ServiceLimitTypeDef(TypedDict, total=False):
    isServiceLimited: bool
    unit: Literal["TERABYTES"]
    value: int


class SessionContextAttributesTypeDef(TypedDict, total=False):
    creationDate: datetime
    mfaAuthenticated: bool


class SessionContextTypeDef(TypedDict, total=False):
    attributes: "SessionContextAttributesTypeDef"
    sessionIssuer: "SessionIssuerTypeDef"


SessionIssuerTypeDef = TypedDict(
    "SessionIssuerTypeDef",
    {"accountId": str, "arn": str, "principalId": str, "type": str, "userName": str},
    total=False,
)


class SeverityTypeDef(TypedDict, total=False):
    description: SeverityDescription
    score: int


class SimpleScopeTermTypeDef(TypedDict, total=False):
    comparator: JobComparator
    key: ScopeFilterKey
    values: List[str]


class SortCriteriaTypeDef(TypedDict, total=False):
    attributeName: str
    orderBy: OrderBy


class StatisticsTypeDef(TypedDict, total=False):
    approximateNumberOfObjectsToProcess: float
    numberOfRuns: float


class TagScopeTermTypeDef(TypedDict, total=False):
    comparator: JobComparator
    key: str
    tagValues: List["TagValuePairTypeDef"]
    target: Literal["S3_OBJECT"]


class TagValuePairTypeDef(TypedDict, total=False):
    key: str
    value: str


class TestCustomDataIdentifierResponseTypeDef(TypedDict, total=False):
    matchCount: int


class UnprocessedAccountTypeDef(TypedDict, total=False):
    accountId: str
    errorCode: ErrorCode
    errorMessage: str


UpdateFindingsFilterResponseTypeDef = TypedDict(
    "UpdateFindingsFilterResponseTypeDef", {"arn": str, "id": str}, total=False
)

UsageByAccountTypeDef = TypedDict(
    "UsageByAccountTypeDef",
    {
        "currency": Literal["USD"],
        "estimatedCost": str,
        "serviceLimit": "ServiceLimitTypeDef",
        "type": UsageType,
    },
    total=False,
)


class UsageRecordTypeDef(TypedDict, total=False):
    accountId: str
    freeTrialStartDate: datetime
    usage: List["UsageByAccountTypeDef"]


class UsageStatisticsFilterTypeDef(TypedDict, total=False):
    comparator: UsageStatisticsFilterComparator
    key: UsageStatisticsFilterKey
    values: List[str]


class UsageStatisticsSortByTypeDef(TypedDict, total=False):
    key: UsageStatisticsSortKey
    orderBy: OrderBy


UsageTotalTypeDef = TypedDict(
    "UsageTotalTypeDef",
    {"currency": Literal["USD"], "estimatedCost": str, "type": UsageType},
    total=False,
)


class UserIdentityRootTypeDef(TypedDict, total=False):
    accountId: str
    arn: str
    principalId: str


UserIdentityTypeDef = TypedDict(
    "UserIdentityTypeDef",
    {
        "assumedRole": "AssumedRoleTypeDef",
        "awsAccount": "AwsAccountTypeDef",
        "awsService": "AwsServiceTypeDef",
        "federatedUser": "FederatedUserTypeDef",
        "iamUser": "IamUserTypeDef",
        "root": "UserIdentityRootTypeDef",
        "type": UserIdentityType,
    },
    total=False,
)


class UserPausedDetailsTypeDef(TypedDict, total=False):
    jobExpiresAt: datetime
    jobImminentExpirationHealthEventArn: str
    jobPausedAt: datetime


class WeeklyScheduleTypeDef(TypedDict, total=False):
    dayOfWeek: DayOfWeek
