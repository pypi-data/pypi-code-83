"""
Main interface for macie2 service type definitions.

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
    Currency,
    DayOfWeek,
    EffectivePermission,
    EncryptionType,
    ErrorCode,
    FindingActionType,
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
    TagTarget,
    TimeRange,
    TypeType,
    Unit,
    UsageStatisticsFilterComparator,
    UsageStatisticsFilterKey,
    UsageStatisticsSortKey,
    UsageType,
    UserIdentityType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessControlListTypeDef",
    "AccountLevelPermissionsTypeDef",
    "AdminAccountTypeDef",
    "ApiCallDetailsTypeDef",
    "AssumedRoleTypeDef",
    "AwsAccountTypeDef",
    "AwsServiceTypeDef",
    "BatchGetCustomDataIdentifierSummaryTypeDef",
    "BlockPublicAccessTypeDef",
    "BucketCountByEffectivePermissionTypeDef",
    "BucketCountByEncryptionTypeTypeDef",
    "BucketCountBySharedAccessTypeTypeDef",
    "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
    "BucketLevelPermissionsTypeDef",
    "BucketMetadataTypeDef",
    "BucketPermissionConfigurationTypeDef",
    "BucketPolicyTypeDef",
    "BucketPublicAccessTypeDef",
    "BucketServerSideEncryptionTypeDef",
    "CellTypeDef",
    "ClassificationDetailsTypeDef",
    "ClassificationExportConfigurationTypeDef",
    "ClassificationResultStatusTypeDef",
    "ClassificationResultTypeDef",
    "CriterionAdditionalPropertiesTypeDef",
    "CustomDataIdentifierSummaryTypeDef",
    "CustomDataIdentifiersTypeDef",
    "CustomDetectionTypeDef",
    "DefaultDetectionTypeDef",
    "DomainDetailsTypeDef",
    "FederatedUserTypeDef",
    "FindingActionTypeDef",
    "FindingActorTypeDef",
    "FindingCriteriaTypeDef",
    "FindingTypeDef",
    "FindingsFilterListItemTypeDef",
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
    "ListJobsFilterTermTypeDef",
    "MemberTypeDef",
    "MonthlyScheduleTypeDef",
    "ObjectCountByEncryptionTypeTypeDef",
    "ObjectLevelStatisticsTypeDef",
    "OccurrencesTypeDef",
    "PageTypeDef",
    "PolicyDetailsTypeDef",
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
    "StatisticsTypeDef",
    "TagScopeTermTypeDef",
    "TagValuePairTypeDef",
    "UnprocessedAccountTypeDef",
    "UsageByAccountTypeDef",
    "UsageRecordTypeDef",
    "UsageTotalTypeDef",
    "UserIdentityRootTypeDef",
    "UserIdentityTypeDef",
    "UserPausedDetailsTypeDef",
    "WeeklyScheduleTypeDef",
    "AccountDetailTypeDef",
    "BatchGetCustomDataIdentifiersResponseTypeDef",
    "BucketCriteriaAdditionalPropertiesTypeDef",
    "BucketSortCriteriaTypeDef",
    "CreateClassificationJobResponseTypeDef",
    "CreateCustomDataIdentifierResponseTypeDef",
    "CreateFindingsFilterResponseTypeDef",
    "CreateInvitationsResponseTypeDef",
    "CreateMemberResponseTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DescribeBucketsResponseTypeDef",
    "DescribeClassificationJobResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "FindingStatisticsSortCriteriaTypeDef",
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
    "ListClassificationJobsResponseTypeDef",
    "ListCustomDataIdentifiersResponseTypeDef",
    "ListFindingsFiltersResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListJobsFilterCriteriaTypeDef",
    "ListJobsSortCriteriaTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutClassificationExportConfigurationResponseTypeDef",
    "SortCriteriaTypeDef",
    "TestCustomDataIdentifierResponseTypeDef",
    "UpdateFindingsFilterResponseTypeDef",
    "UsageStatisticsFilterTypeDef",
    "UsageStatisticsSortByTypeDef",
)

AccessControlListTypeDef = TypedDict(
    "AccessControlListTypeDef",
    {"allowsPublicReadAccess": bool, "allowsPublicWriteAccess": bool},
    total=False,
)

AccountLevelPermissionsTypeDef = TypedDict(
    "AccountLevelPermissionsTypeDef", {"blockPublicAccess": "BlockPublicAccessTypeDef"}, total=False
)

AdminAccountTypeDef = TypedDict(
    "AdminAccountTypeDef", {"accountId": str, "status": AdminStatus}, total=False
)

ApiCallDetailsTypeDef = TypedDict(
    "ApiCallDetailsTypeDef",
    {"api": str, "apiServiceName": str, "firstSeen": datetime, "lastSeen": datetime},
    total=False,
)

AssumedRoleTypeDef = TypedDict(
    "AssumedRoleTypeDef",
    {
        "accessKeyId": str,
        "accountId": str,
        "arn": str,
        "principalId": str,
        "sessionContext": "SessionContextTypeDef",
    },
    total=False,
)

AwsAccountTypeDef = TypedDict(
    "AwsAccountTypeDef", {"accountId": str, "principalId": str}, total=False
)

AwsServiceTypeDef = TypedDict("AwsServiceTypeDef", {"invokedBy": str}, total=False)

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

BlockPublicAccessTypeDef = TypedDict(
    "BlockPublicAccessTypeDef",
    {
        "blockPublicAcls": bool,
        "blockPublicPolicy": bool,
        "ignorePublicAcls": bool,
        "restrictPublicBuckets": bool,
    },
    total=False,
)

BucketCountByEffectivePermissionTypeDef = TypedDict(
    "BucketCountByEffectivePermissionTypeDef",
    {"publiclyAccessible": int, "publiclyReadable": int, "publiclyWritable": int, "unknown": int},
    total=False,
)

BucketCountByEncryptionTypeTypeDef = TypedDict(
    "BucketCountByEncryptionTypeTypeDef",
    {"kmsManaged": int, "s3Managed": int, "unencrypted": int, "unknown": int},
    total=False,
)

BucketCountBySharedAccessTypeTypeDef = TypedDict(
    "BucketCountBySharedAccessTypeTypeDef",
    {"external": int, "internal": int, "notShared": int, "unknown": int},
    total=False,
)

BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef = TypedDict(
    "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
    {"allowsUnencryptedObjectUploads": int, "deniesUnencryptedObjectUploads": int, "unknown": int},
    total=False,
)

BucketLevelPermissionsTypeDef = TypedDict(
    "BucketLevelPermissionsTypeDef",
    {
        "accessControlList": "AccessControlListTypeDef",
        "blockPublicAccess": "BlockPublicAccessTypeDef",
        "bucketPolicy": "BucketPolicyTypeDef",
    },
    total=False,
)

BucketMetadataTypeDef = TypedDict(
    "BucketMetadataTypeDef",
    {
        "accountId": str,
        "allowsUnencryptedObjectUploads": AllowsUnencryptedObjectUploads,
        "bucketArn": str,
        "bucketCreatedAt": datetime,
        "bucketName": str,
        "classifiableObjectCount": int,
        "classifiableSizeInBytes": int,
        "jobDetails": "JobDetailsTypeDef",
        "lastUpdated": datetime,
        "objectCount": int,
        "objectCountByEncryptionType": "ObjectCountByEncryptionTypeTypeDef",
        "publicAccess": "BucketPublicAccessTypeDef",
        "region": str,
        "replicationDetails": "ReplicationDetailsTypeDef",
        "serverSideEncryption": "BucketServerSideEncryptionTypeDef",
        "sharedAccess": SharedAccess,
        "sizeInBytes": int,
        "sizeInBytesCompressed": int,
        "tags": List["KeyValuePairTypeDef"],
        "unclassifiableObjectCount": "ObjectLevelStatisticsTypeDef",
        "unclassifiableObjectSizeInBytes": "ObjectLevelStatisticsTypeDef",
        "versioning": bool,
    },
    total=False,
)

BucketPermissionConfigurationTypeDef = TypedDict(
    "BucketPermissionConfigurationTypeDef",
    {
        "accountLevelPermissions": "AccountLevelPermissionsTypeDef",
        "bucketLevelPermissions": "BucketLevelPermissionsTypeDef",
    },
    total=False,
)

BucketPolicyTypeDef = TypedDict(
    "BucketPolicyTypeDef",
    {"allowsPublicReadAccess": bool, "allowsPublicWriteAccess": bool},
    total=False,
)

BucketPublicAccessTypeDef = TypedDict(
    "BucketPublicAccessTypeDef",
    {
        "effectivePermission": EffectivePermission,
        "permissionConfiguration": "BucketPermissionConfigurationTypeDef",
    },
    total=False,
)

BucketServerSideEncryptionTypeDef = TypedDict(
    "BucketServerSideEncryptionTypeDef", {"kmsMasterKeyId": str, "type": TypeType}, total=False
)

CellTypeDef = TypedDict(
    "CellTypeDef", {"cellReference": str, "column": int, "columnName": str, "row": int}, total=False
)

ClassificationDetailsTypeDef = TypedDict(
    "ClassificationDetailsTypeDef",
    {
        "detailedResultsLocation": str,
        "jobArn": str,
        "jobId": str,
        "result": "ClassificationResultTypeDef",
    },
    total=False,
)

ClassificationExportConfigurationTypeDef = TypedDict(
    "ClassificationExportConfigurationTypeDef",
    {"s3Destination": "S3DestinationTypeDef"},
    total=False,
)

ClassificationResultStatusTypeDef = TypedDict(
    "ClassificationResultStatusTypeDef", {"code": str, "reason": str}, total=False
)

ClassificationResultTypeDef = TypedDict(
    "ClassificationResultTypeDef",
    {
        "additionalOccurrences": bool,
        "customDataIdentifiers": "CustomDataIdentifiersTypeDef",
        "mimeType": str,
        "sensitiveData": List["SensitiveDataItemTypeDef"],
        "sizeClassified": int,
        "status": "ClassificationResultStatusTypeDef",
    },
    total=False,
)

CriterionAdditionalPropertiesTypeDef = TypedDict(
    "CriterionAdditionalPropertiesTypeDef",
    {
        "eq": List[str],
        "eqExactMatch": List[str],
        "gt": int,
        "gte": int,
        "lt": int,
        "lte": int,
        "neq": List[str],
    },
    total=False,
)

CustomDataIdentifierSummaryTypeDef = TypedDict(
    "CustomDataIdentifierSummaryTypeDef",
    {"arn": str, "createdAt": datetime, "description": str, "id": str, "name": str},
    total=False,
)

CustomDataIdentifiersTypeDef = TypedDict(
    "CustomDataIdentifiersTypeDef",
    {"detections": List["CustomDetectionTypeDef"], "totalCount": int},
    total=False,
)

CustomDetectionTypeDef = TypedDict(
    "CustomDetectionTypeDef",
    {"arn": str, "count": int, "name": str, "occurrences": "OccurrencesTypeDef"},
    total=False,
)

DefaultDetectionTypeDef = TypedDict(
    "DefaultDetectionTypeDef",
    {"count": int, "occurrences": "OccurrencesTypeDef", "type": str},
    total=False,
)

DomainDetailsTypeDef = TypedDict("DomainDetailsTypeDef", {"domainName": str}, total=False)

FederatedUserTypeDef = TypedDict(
    "FederatedUserTypeDef",
    {
        "accessKeyId": str,
        "accountId": str,
        "arn": str,
        "principalId": str,
        "sessionContext": "SessionContextTypeDef",
    },
    total=False,
)

FindingActionTypeDef = TypedDict(
    "FindingActionTypeDef",
    {"actionType": FindingActionType, "apiCallDetails": "ApiCallDetailsTypeDef"},
    total=False,
)

FindingActorTypeDef = TypedDict(
    "FindingActorTypeDef",
    {
        "domainDetails": "DomainDetailsTypeDef",
        "ipAddressDetails": "IpAddressDetailsTypeDef",
        "userIdentity": "UserIdentityTypeDef",
    },
    total=False,
)

FindingCriteriaTypeDef = TypedDict(
    "FindingCriteriaTypeDef",
    {"criterion": Dict[str, "CriterionAdditionalPropertiesTypeDef"]},
    total=False,
)

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

GroupCountTypeDef = TypedDict("GroupCountTypeDef", {"count": int, "groupKey": str}, total=False)

IamUserTypeDef = TypedDict(
    "IamUserTypeDef",
    {"accountId": str, "arn": str, "principalId": str, "userName": str},
    total=False,
)

InvitationTypeDef = TypedDict(
    "InvitationTypeDef",
    {
        "accountId": str,
        "invitationId": str,
        "invitedAt": datetime,
        "relationshipStatus": RelationshipStatus,
    },
    total=False,
)

IpAddressDetailsTypeDef = TypedDict(
    "IpAddressDetailsTypeDef",
    {
        "ipAddressV4": str,
        "ipCity": "IpCityTypeDef",
        "ipCountry": "IpCountryTypeDef",
        "ipGeoLocation": "IpGeoLocationTypeDef",
        "ipOwner": "IpOwnerTypeDef",
    },
    total=False,
)

IpCityTypeDef = TypedDict("IpCityTypeDef", {"name": str}, total=False)

IpCountryTypeDef = TypedDict("IpCountryTypeDef", {"code": str, "name": str}, total=False)

IpGeoLocationTypeDef = TypedDict("IpGeoLocationTypeDef", {"lat": float, "lon": float}, total=False)

IpOwnerTypeDef = TypedDict(
    "IpOwnerTypeDef", {"asn": str, "asnOrg": str, "isp": str, "org": str}, total=False
)

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {
        "isDefinedInJob": IsDefinedInJob,
        "isMonitoredByJob": IsMonitoredByJob,
        "lastJobId": str,
        "lastJobRunTime": datetime,
    },
    total=False,
)

JobScheduleFrequencyTypeDef = TypedDict(
    "JobScheduleFrequencyTypeDef",
    {
        "dailySchedule": Dict[str, Any],
        "monthlySchedule": "MonthlyScheduleTypeDef",
        "weeklySchedule": "WeeklyScheduleTypeDef",
    },
    total=False,
)

JobScopeTermTypeDef = TypedDict(
    "JobScopeTermTypeDef",
    {"simpleScopeTerm": "SimpleScopeTermTypeDef", "tagScopeTerm": "TagScopeTermTypeDef"},
    total=False,
)

JobScopingBlockTypeDef = TypedDict(
    "JobScopingBlockTypeDef", {"and": List["JobScopeTermTypeDef"]}, total=False
)

JobSummaryTypeDef = TypedDict(
    "JobSummaryTypeDef",
    {
        "bucketDefinitions": List["S3BucketDefinitionForJobTypeDef"],
        "createdAt": datetime,
        "jobId": str,
        "jobStatus": JobStatus,
        "jobType": JobType,
        "lastRunErrorStatus": "LastRunErrorStatusTypeDef",
        "name": str,
        "userPausedDetails": "UserPausedDetailsTypeDef",
    },
    total=False,
)

KeyValuePairTypeDef = TypedDict("KeyValuePairTypeDef", {"key": str, "value": str}, total=False)

LastRunErrorStatusTypeDef = TypedDict(
    "LastRunErrorStatusTypeDef", {"code": LastRunErrorStatusCode}, total=False
)

ListJobsFilterTermTypeDef = TypedDict(
    "ListJobsFilterTermTypeDef",
    {"comparator": JobComparator, "key": ListJobsFilterKey, "values": List[str]},
    total=False,
)

MemberTypeDef = TypedDict(
    "MemberTypeDef",
    {
        "accountId": str,
        "administratorAccountId": str,
        "arn": str,
        "email": str,
        "invitedAt": datetime,
        "masterAccountId": str,
        "relationshipStatus": RelationshipStatus,
        "tags": Dict[str, str],
        "updatedAt": datetime,
    },
    total=False,
)

MonthlyScheduleTypeDef = TypedDict("MonthlyScheduleTypeDef", {"dayOfMonth": int}, total=False)

ObjectCountByEncryptionTypeTypeDef = TypedDict(
    "ObjectCountByEncryptionTypeTypeDef",
    {
        "customerManaged": int,
        "kmsManaged": int,
        "s3Managed": int,
        "unencrypted": int,
        "unknown": int,
    },
    total=False,
)

ObjectLevelStatisticsTypeDef = TypedDict(
    "ObjectLevelStatisticsTypeDef",
    {"fileType": int, "storageClass": int, "total": int},
    total=False,
)

OccurrencesTypeDef = TypedDict(
    "OccurrencesTypeDef",
    {
        "cells": List["CellTypeDef"],
        "lineRanges": List["RangeTypeDef"],
        "offsetRanges": List["RangeTypeDef"],
        "pages": List["PageTypeDef"],
        "records": List["RecordTypeDef"],
    },
    total=False,
)

PageTypeDef = TypedDict(
    "PageTypeDef",
    {"lineRange": "RangeTypeDef", "offsetRange": "RangeTypeDef", "pageNumber": int},
    total=False,
)

PolicyDetailsTypeDef = TypedDict(
    "PolicyDetailsTypeDef",
    {"action": "FindingActionTypeDef", "actor": "FindingActorTypeDef"},
    total=False,
)

RangeTypeDef = TypedDict(
    "RangeTypeDef", {"end": int, "start": int, "startColumn": int}, total=False
)

RecordTypeDef = TypedDict("RecordTypeDef", {"jsonPath": str, "recordIndex": int}, total=False)

ReplicationDetailsTypeDef = TypedDict(
    "ReplicationDetailsTypeDef",
    {"replicated": bool, "replicatedExternally": bool, "replicationAccounts": List[str]},
    total=False,
)

ResourcesAffectedTypeDef = TypedDict(
    "ResourcesAffectedTypeDef",
    {"s3Bucket": "S3BucketTypeDef", "s3Object": "S3ObjectTypeDef"},
    total=False,
)

S3BucketDefinitionForJobTypeDef = TypedDict(
    "S3BucketDefinitionForJobTypeDef", {"accountId": str, "buckets": List[str]}
)

S3BucketOwnerTypeDef = TypedDict(
    "S3BucketOwnerTypeDef", {"displayName": str, "id": str}, total=False
)

S3BucketTypeDef = TypedDict(
    "S3BucketTypeDef",
    {
        "allowsUnencryptedObjectUploads": AllowsUnencryptedObjectUploads,
        "arn": str,
        "createdAt": datetime,
        "defaultServerSideEncryption": "ServerSideEncryptionTypeDef",
        "name": str,
        "owner": "S3BucketOwnerTypeDef",
        "publicAccess": "BucketPublicAccessTypeDef",
        "tags": List["KeyValuePairTypeDef"],
    },
    total=False,
)

_RequiredS3DestinationTypeDef = TypedDict(
    "_RequiredS3DestinationTypeDef", {"bucketName": str, "kmsKeyArn": str}
)
_OptionalS3DestinationTypeDef = TypedDict(
    "_OptionalS3DestinationTypeDef", {"keyPrefix": str}, total=False
)


class S3DestinationTypeDef(_RequiredS3DestinationTypeDef, _OptionalS3DestinationTypeDef):
    pass


S3JobDefinitionTypeDef = TypedDict(
    "S3JobDefinitionTypeDef",
    {"bucketDefinitions": List["S3BucketDefinitionForJobTypeDef"], "scoping": "ScopingTypeDef"},
    total=False,
)

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "bucketArn": str,
        "eTag": str,
        "extension": str,
        "key": str,
        "lastModified": datetime,
        "path": str,
        "publicAccess": bool,
        "serverSideEncryption": "ServerSideEncryptionTypeDef",
        "size": int,
        "storageClass": StorageClass,
        "tags": List["KeyValuePairTypeDef"],
        "versionId": str,
    },
    total=False,
)

ScopingTypeDef = TypedDict(
    "ScopingTypeDef",
    {"excludes": "JobScopingBlockTypeDef", "includes": "JobScopingBlockTypeDef"},
    total=False,
)

SecurityHubConfigurationTypeDef = TypedDict(
    "SecurityHubConfigurationTypeDef",
    {"publishClassificationFindings": bool, "publishPolicyFindings": bool},
)

SensitiveDataItemTypeDef = TypedDict(
    "SensitiveDataItemTypeDef",
    {
        "category": SensitiveDataItemCategory,
        "detections": List["DefaultDetectionTypeDef"],
        "totalCount": int,
    },
    total=False,
)

ServerSideEncryptionTypeDef = TypedDict(
    "ServerSideEncryptionTypeDef",
    {"encryptionType": EncryptionType, "kmsMasterKeyId": str},
    total=False,
)

ServiceLimitTypeDef = TypedDict(
    "ServiceLimitTypeDef", {"isServiceLimited": bool, "unit": Unit, "value": int}, total=False
)

SessionContextAttributesTypeDef = TypedDict(
    "SessionContextAttributesTypeDef",
    {"creationDate": datetime, "mfaAuthenticated": bool},
    total=False,
)

SessionContextTypeDef = TypedDict(
    "SessionContextTypeDef",
    {"attributes": "SessionContextAttributesTypeDef", "sessionIssuer": "SessionIssuerTypeDef"},
    total=False,
)

SessionIssuerTypeDef = TypedDict(
    "SessionIssuerTypeDef",
    {"accountId": str, "arn": str, "principalId": str, "type": str, "userName": str},
    total=False,
)

SeverityTypeDef = TypedDict(
    "SeverityTypeDef", {"description": SeverityDescription, "score": int}, total=False
)

SimpleScopeTermTypeDef = TypedDict(
    "SimpleScopeTermTypeDef",
    {"comparator": JobComparator, "key": ScopeFilterKey, "values": List[str]},
    total=False,
)

StatisticsTypeDef = TypedDict(
    "StatisticsTypeDef",
    {"approximateNumberOfObjectsToProcess": float, "numberOfRuns": float},
    total=False,
)

TagScopeTermTypeDef = TypedDict(
    "TagScopeTermTypeDef",
    {
        "comparator": JobComparator,
        "key": str,
        "tagValues": List["TagValuePairTypeDef"],
        "target": TagTarget,
    },
    total=False,
)

TagValuePairTypeDef = TypedDict("TagValuePairTypeDef", {"key": str, "value": str}, total=False)

UnprocessedAccountTypeDef = TypedDict(
    "UnprocessedAccountTypeDef",
    {"accountId": str, "errorCode": ErrorCode, "errorMessage": str},
    total=False,
)

UsageByAccountTypeDef = TypedDict(
    "UsageByAccountTypeDef",
    {
        "currency": Currency,
        "estimatedCost": str,
        "serviceLimit": "ServiceLimitTypeDef",
        "type": UsageType,
    },
    total=False,
)

UsageRecordTypeDef = TypedDict(
    "UsageRecordTypeDef",
    {"accountId": str, "freeTrialStartDate": datetime, "usage": List["UsageByAccountTypeDef"]},
    total=False,
)

UsageTotalTypeDef = TypedDict(
    "UsageTotalTypeDef",
    {"currency": Currency, "estimatedCost": str, "type": UsageType},
    total=False,
)

UserIdentityRootTypeDef = TypedDict(
    "UserIdentityRootTypeDef", {"accountId": str, "arn": str, "principalId": str}, total=False
)

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

UserPausedDetailsTypeDef = TypedDict(
    "UserPausedDetailsTypeDef",
    {"jobExpiresAt": datetime, "jobImminentExpirationHealthEventArn": str, "jobPausedAt": datetime},
    total=False,
)

WeeklyScheduleTypeDef = TypedDict("WeeklyScheduleTypeDef", {"dayOfWeek": DayOfWeek}, total=False)

AccountDetailTypeDef = TypedDict("AccountDetailTypeDef", {"accountId": str, "email": str})

BatchGetCustomDataIdentifiersResponseTypeDef = TypedDict(
    "BatchGetCustomDataIdentifiersResponseTypeDef",
    {
        "customDataIdentifiers": List["BatchGetCustomDataIdentifierSummaryTypeDef"],
        "notFoundIdentifierIds": List[str],
    },
    total=False,
)

BucketCriteriaAdditionalPropertiesTypeDef = TypedDict(
    "BucketCriteriaAdditionalPropertiesTypeDef",
    {
        "eq": List[str],
        "gt": int,
        "gte": int,
        "lt": int,
        "lte": int,
        "neq": List[str],
        "prefix": str,
    },
    total=False,
)

BucketSortCriteriaTypeDef = TypedDict(
    "BucketSortCriteriaTypeDef", {"attributeName": str, "orderBy": OrderBy}, total=False
)

CreateClassificationJobResponseTypeDef = TypedDict(
    "CreateClassificationJobResponseTypeDef", {"jobArn": str, "jobId": str}, total=False
)

CreateCustomDataIdentifierResponseTypeDef = TypedDict(
    "CreateCustomDataIdentifierResponseTypeDef", {"customDataIdentifierId": str}, total=False
)

CreateFindingsFilterResponseTypeDef = TypedDict(
    "CreateFindingsFilterResponseTypeDef", {"arn": str, "id": str}, total=False
)

CreateInvitationsResponseTypeDef = TypedDict(
    "CreateInvitationsResponseTypeDef",
    {"unprocessedAccounts": List["UnprocessedAccountTypeDef"]},
    total=False,
)

CreateMemberResponseTypeDef = TypedDict("CreateMemberResponseTypeDef", {"arn": str}, total=False)

DeclineInvitationsResponseTypeDef = TypedDict(
    "DeclineInvitationsResponseTypeDef",
    {"unprocessedAccounts": List["UnprocessedAccountTypeDef"]},
    total=False,
)

DeleteInvitationsResponseTypeDef = TypedDict(
    "DeleteInvitationsResponseTypeDef",
    {"unprocessedAccounts": List["UnprocessedAccountTypeDef"]},
    total=False,
)

DescribeBucketsResponseTypeDef = TypedDict(
    "DescribeBucketsResponseTypeDef",
    {"buckets": List["BucketMetadataTypeDef"], "nextToken": str},
    total=False,
)

DescribeClassificationJobResponseTypeDef = TypedDict(
    "DescribeClassificationJobResponseTypeDef",
    {
        "clientToken": str,
        "createdAt": datetime,
        "customDataIdentifierIds": List[str],
        "description": str,
        "initialRun": bool,
        "jobArn": str,
        "jobId": str,
        "jobStatus": JobStatus,
        "jobType": JobType,
        "lastRunErrorStatus": "LastRunErrorStatusTypeDef",
        "lastRunTime": datetime,
        "name": str,
        "s3JobDefinition": "S3JobDefinitionTypeDef",
        "samplingPercentage": int,
        "scheduleFrequency": "JobScheduleFrequencyTypeDef",
        "statistics": "StatisticsTypeDef",
        "tags": Dict[str, str],
        "userPausedDetails": "UserPausedDetailsTypeDef",
    },
    total=False,
)

DescribeOrganizationConfigurationResponseTypeDef = TypedDict(
    "DescribeOrganizationConfigurationResponseTypeDef",
    {"autoEnable": bool, "maxAccountLimitReached": bool},
    total=False,
)

FindingStatisticsSortCriteriaTypeDef = TypedDict(
    "FindingStatisticsSortCriteriaTypeDef",
    {"attributeName": FindingStatisticsSortAttributeName, "orderBy": OrderBy},
    total=False,
)

GetAdministratorAccountResponseTypeDef = TypedDict(
    "GetAdministratorAccountResponseTypeDef", {"administrator": "InvitationTypeDef"}, total=False
)

GetBucketStatisticsResponseTypeDef = TypedDict(
    "GetBucketStatisticsResponseTypeDef",
    {
        "bucketCount": int,
        "bucketCountByEffectivePermission": "BucketCountByEffectivePermissionTypeDef",
        "bucketCountByEncryptionType": "BucketCountByEncryptionTypeTypeDef",
        "bucketCountByObjectEncryptionRequirement": "BucketCountPolicyAllowsUnencryptedObjectUploadsTypeDef",
        "bucketCountBySharedAccessType": "BucketCountBySharedAccessTypeTypeDef",
        "classifiableObjectCount": int,
        "classifiableSizeInBytes": int,
        "lastUpdated": datetime,
        "objectCount": int,
        "sizeInBytes": int,
        "sizeInBytesCompressed": int,
        "unclassifiableObjectCount": "ObjectLevelStatisticsTypeDef",
        "unclassifiableObjectSizeInBytes": "ObjectLevelStatisticsTypeDef",
    },
    total=False,
)

GetClassificationExportConfigurationResponseTypeDef = TypedDict(
    "GetClassificationExportConfigurationResponseTypeDef",
    {"configuration": "ClassificationExportConfigurationTypeDef"},
    total=False,
)

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

GetFindingStatisticsResponseTypeDef = TypedDict(
    "GetFindingStatisticsResponseTypeDef", {"countsByGroup": List["GroupCountTypeDef"]}, total=False
)

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

GetFindingsPublicationConfigurationResponseTypeDef = TypedDict(
    "GetFindingsPublicationConfigurationResponseTypeDef",
    {"securityHubConfiguration": "SecurityHubConfigurationTypeDef"},
    total=False,
)

GetFindingsResponseTypeDef = TypedDict(
    "GetFindingsResponseTypeDef", {"findings": List["FindingTypeDef"]}, total=False
)

GetInvitationsCountResponseTypeDef = TypedDict(
    "GetInvitationsCountResponseTypeDef", {"invitationsCount": int}, total=False
)

GetMacieSessionResponseTypeDef = TypedDict(
    "GetMacieSessionResponseTypeDef",
    {
        "createdAt": datetime,
        "findingPublishingFrequency": FindingPublishingFrequency,
        "serviceRole": str,
        "status": MacieStatus,
        "updatedAt": datetime,
    },
    total=False,
)

GetMasterAccountResponseTypeDef = TypedDict(
    "GetMasterAccountResponseTypeDef", {"master": "InvitationTypeDef"}, total=False
)

GetMemberResponseTypeDef = TypedDict(
    "GetMemberResponseTypeDef",
    {
        "accountId": str,
        "administratorAccountId": str,
        "arn": str,
        "email": str,
        "invitedAt": datetime,
        "masterAccountId": str,
        "relationshipStatus": RelationshipStatus,
        "tags": Dict[str, str],
        "updatedAt": datetime,
    },
    total=False,
)

GetUsageStatisticsResponseTypeDef = TypedDict(
    "GetUsageStatisticsResponseTypeDef",
    {"nextToken": str, "records": List["UsageRecordTypeDef"], "timeRange": TimeRange},
    total=False,
)

GetUsageTotalsResponseTypeDef = TypedDict(
    "GetUsageTotalsResponseTypeDef",
    {"timeRange": TimeRange, "usageTotals": List["UsageTotalTypeDef"]},
    total=False,
)

ListClassificationJobsResponseTypeDef = TypedDict(
    "ListClassificationJobsResponseTypeDef",
    {"items": List["JobSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListCustomDataIdentifiersResponseTypeDef = TypedDict(
    "ListCustomDataIdentifiersResponseTypeDef",
    {"items": List["CustomDataIdentifierSummaryTypeDef"], "nextToken": str},
    total=False,
)

ListFindingsFiltersResponseTypeDef = TypedDict(
    "ListFindingsFiltersResponseTypeDef",
    {"findingsFilterListItems": List["FindingsFilterListItemTypeDef"], "nextToken": str},
    total=False,
)

ListFindingsResponseTypeDef = TypedDict(
    "ListFindingsResponseTypeDef", {"findingIds": List[str], "nextToken": str}, total=False
)

ListInvitationsResponseTypeDef = TypedDict(
    "ListInvitationsResponseTypeDef",
    {"invitations": List["InvitationTypeDef"], "nextToken": str},
    total=False,
)

ListJobsFilterCriteriaTypeDef = TypedDict(
    "ListJobsFilterCriteriaTypeDef",
    {"excludes": List["ListJobsFilterTermTypeDef"], "includes": List["ListJobsFilterTermTypeDef"]},
    total=False,
)

ListJobsSortCriteriaTypeDef = TypedDict(
    "ListJobsSortCriteriaTypeDef",
    {"attributeName": ListJobsSortAttributeName, "orderBy": OrderBy},
    total=False,
)

ListMembersResponseTypeDef = TypedDict(
    "ListMembersResponseTypeDef", {"members": List["MemberTypeDef"], "nextToken": str}, total=False
)

ListOrganizationAdminAccountsResponseTypeDef = TypedDict(
    "ListOrganizationAdminAccountsResponseTypeDef",
    {"adminAccounts": List["AdminAccountTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PutClassificationExportConfigurationResponseTypeDef = TypedDict(
    "PutClassificationExportConfigurationResponseTypeDef",
    {"configuration": "ClassificationExportConfigurationTypeDef"},
    total=False,
)

SortCriteriaTypeDef = TypedDict(
    "SortCriteriaTypeDef", {"attributeName": str, "orderBy": OrderBy}, total=False
)

TestCustomDataIdentifierResponseTypeDef = TypedDict(
    "TestCustomDataIdentifierResponseTypeDef", {"matchCount": int}, total=False
)

UpdateFindingsFilterResponseTypeDef = TypedDict(
    "UpdateFindingsFilterResponseTypeDef", {"arn": str, "id": str}, total=False
)

UsageStatisticsFilterTypeDef = TypedDict(
    "UsageStatisticsFilterTypeDef",
    {
        "comparator": UsageStatisticsFilterComparator,
        "key": UsageStatisticsFilterKey,
        "values": List[str],
    },
    total=False,
)

UsageStatisticsSortByTypeDef = TypedDict(
    "UsageStatisticsSortByTypeDef", {"key": UsageStatisticsSortKey, "orderBy": OrderBy}, total=False
)
