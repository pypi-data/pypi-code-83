"""
Type annotations for accessanalyzer service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/type_defs.html)

Usage::

    ```python
    from mypy_boto3_accessanalyzer.type_defs import AccessPreviewFindingTypeDef

    data: AccessPreviewFindingTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_accessanalyzer.literals import (
    AccessPreviewStatus,
    AccessPreviewStatusReasonCode,
    AclPermission,
    AnalyzerStatus,
    FindingChangeType,
    FindingSourceType,
    FindingStatus,
    JobErrorCode,
    JobStatus,
    KmsGrantOperation,
    OrderBy,
    ReasonCode,
    ResourceType,
    TypeType,
    ValidatePolicyFindingType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessPreviewFindingTypeDef",
    "AccessPreviewStatusReasonTypeDef",
    "AccessPreviewSummaryTypeDef",
    "AccessPreviewTypeDef",
    "AclGranteeTypeDef",
    "AnalyzedResourceSummaryTypeDef",
    "AnalyzedResourceTypeDef",
    "AnalyzerSummaryTypeDef",
    "ArchiveRuleSummaryTypeDef",
    "CloudTrailDetailsTypeDef",
    "CloudTrailPropertiesTypeDef",
    "ConfigurationTypeDef",
    "CreateAccessPreviewResponseTypeDef",
    "CreateAnalyzerResponseTypeDef",
    "CriterionTypeDef",
    "FindingSourceDetailTypeDef",
    "FindingSourceTypeDef",
    "FindingSummaryTypeDef",
    "FindingTypeDef",
    "GeneratedPolicyPropertiesTypeDef",
    "GeneratedPolicyResultTypeDef",
    "GeneratedPolicyTypeDef",
    "GetAccessPreviewResponseTypeDef",
    "GetAnalyzedResourceResponseTypeDef",
    "GetAnalyzerResponseTypeDef",
    "GetArchiveRuleResponseTypeDef",
    "GetFindingResponseTypeDef",
    "GetGeneratedPolicyResponseTypeDef",
    "IamRoleConfigurationTypeDef",
    "InlineArchiveRuleTypeDef",
    "JobDetailsTypeDef",
    "JobErrorTypeDef",
    "KmsGrantConfigurationTypeDef",
    "KmsGrantConstraintsTypeDef",
    "KmsKeyConfigurationTypeDef",
    "ListAccessPreviewFindingsResponseTypeDef",
    "ListAccessPreviewsResponseTypeDef",
    "ListAnalyzedResourcesResponseTypeDef",
    "ListAnalyzersResponseTypeDef",
    "ListArchiveRulesResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "ListPolicyGenerationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LocationTypeDef",
    "NetworkOriginConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PathElementTypeDef",
    "PolicyGenerationDetailsTypeDef",
    "PolicyGenerationTypeDef",
    "PositionTypeDef",
    "S3AccessPointConfigurationTypeDef",
    "S3BucketAclGrantConfigurationTypeDef",
    "S3BucketConfigurationTypeDef",
    "S3PublicAccessBlockConfigurationTypeDef",
    "SecretsManagerSecretConfigurationTypeDef",
    "SortCriteriaTypeDef",
    "SpanTypeDef",
    "SqsQueueConfigurationTypeDef",
    "StartPolicyGenerationResponseTypeDef",
    "StatusReasonTypeDef",
    "SubstringTypeDef",
    "TrailPropertiesTypeDef",
    "TrailTypeDef",
    "ValidatePolicyFindingTypeDef",
    "ValidatePolicyResponseTypeDef",
    "VpcConfigurationTypeDef",
)

_RequiredAccessPreviewFindingTypeDef = TypedDict(
    "_RequiredAccessPreviewFindingTypeDef",
    {
        "changeType": FindingChangeType,
        "createdAt": datetime,
        "id": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceType,
        "status": FindingStatus,
    },
)
_OptionalAccessPreviewFindingTypeDef = TypedDict(
    "_OptionalAccessPreviewFindingTypeDef",
    {
        "action": List[str],
        "condition": Dict[str, str],
        "error": str,
        "existingFindingId": str,
        "existingFindingStatus": FindingStatus,
        "isPublic": bool,
        "principal": Dict[str, str],
        "resource": str,
        "sources": List["FindingSourceTypeDef"],
    },
    total=False,
)


class AccessPreviewFindingTypeDef(
    _RequiredAccessPreviewFindingTypeDef, _OptionalAccessPreviewFindingTypeDef
):
    pass


class AccessPreviewStatusReasonTypeDef(TypedDict):
    code: AccessPreviewStatusReasonCode


_RequiredAccessPreviewSummaryTypeDef = TypedDict(
    "_RequiredAccessPreviewSummaryTypeDef",
    {"analyzerArn": str, "createdAt": datetime, "id": str, "status": AccessPreviewStatus},
)
_OptionalAccessPreviewSummaryTypeDef = TypedDict(
    "_OptionalAccessPreviewSummaryTypeDef",
    {"statusReason": "AccessPreviewStatusReasonTypeDef"},
    total=False,
)


class AccessPreviewSummaryTypeDef(
    _RequiredAccessPreviewSummaryTypeDef, _OptionalAccessPreviewSummaryTypeDef
):
    pass


_RequiredAccessPreviewTypeDef = TypedDict(
    "_RequiredAccessPreviewTypeDef",
    {
        "analyzerArn": str,
        "configurations": Dict[str, "ConfigurationTypeDef"],
        "createdAt": datetime,
        "id": str,
        "status": AccessPreviewStatus,
    },
)
_OptionalAccessPreviewTypeDef = TypedDict(
    "_OptionalAccessPreviewTypeDef",
    {"statusReason": "AccessPreviewStatusReasonTypeDef"},
    total=False,
)


class AccessPreviewTypeDef(_RequiredAccessPreviewTypeDef, _OptionalAccessPreviewTypeDef):
    pass


AclGranteeTypeDef = TypedDict("AclGranteeTypeDef", {"id": str, "uri": str}, total=False)


class AnalyzedResourceSummaryTypeDef(TypedDict):
    resourceArn: str
    resourceOwnerAccount: str
    resourceType: ResourceType


class _RequiredAnalyzedResourceTypeDef(TypedDict):
    analyzedAt: datetime
    createdAt: datetime
    isPublic: bool
    resourceArn: str
    resourceOwnerAccount: str
    resourceType: ResourceType
    updatedAt: datetime


class AnalyzedResourceTypeDef(_RequiredAnalyzedResourceTypeDef, total=False):
    actions: List[str]
    error: str
    sharedVia: List[str]
    status: FindingStatus


_RequiredAnalyzerSummaryTypeDef = TypedDict(
    "_RequiredAnalyzerSummaryTypeDef",
    {"arn": str, "createdAt": datetime, "name": str, "status": AnalyzerStatus, "type": TypeType},
)
_OptionalAnalyzerSummaryTypeDef = TypedDict(
    "_OptionalAnalyzerSummaryTypeDef",
    {
        "lastResourceAnalyzed": str,
        "lastResourceAnalyzedAt": datetime,
        "statusReason": "StatusReasonTypeDef",
        "tags": Dict[str, str],
    },
    total=False,
)


class AnalyzerSummaryTypeDef(_RequiredAnalyzerSummaryTypeDef, _OptionalAnalyzerSummaryTypeDef):
    pass


ArchiveRuleSummaryTypeDef = TypedDict(
    "ArchiveRuleSummaryTypeDef",
    {
        "createdAt": datetime,
        "filter": Dict[str, "CriterionTypeDef"],
        "ruleName": str,
        "updatedAt": datetime,
    },
)


class _RequiredCloudTrailDetailsTypeDef(TypedDict):
    accessRole: str
    startTime: datetime
    trails: List["TrailTypeDef"]


class CloudTrailDetailsTypeDef(_RequiredCloudTrailDetailsTypeDef, total=False):
    endTime: datetime


class CloudTrailPropertiesTypeDef(TypedDict):
    endTime: datetime
    startTime: datetime
    trailProperties: List["TrailPropertiesTypeDef"]


class ConfigurationTypeDef(TypedDict, total=False):
    iamRole: "IamRoleConfigurationTypeDef"
    kmsKey: "KmsKeyConfigurationTypeDef"
    s3Bucket: "S3BucketConfigurationTypeDef"
    secretsManagerSecret: "SecretsManagerSecretConfigurationTypeDef"
    sqsQueue: "SqsQueueConfigurationTypeDef"


CreateAccessPreviewResponseTypeDef = TypedDict("CreateAccessPreviewResponseTypeDef", {"id": str})


class CreateAnalyzerResponseTypeDef(TypedDict, total=False):
    arn: str


class CriterionTypeDef(TypedDict, total=False):
    contains: List[str]
    eq: List[str]
    exists: bool
    neq: List[str]


class FindingSourceDetailTypeDef(TypedDict, total=False):
    accessPointArn: str


_RequiredFindingSourceTypeDef = TypedDict(
    "_RequiredFindingSourceTypeDef", {"type": FindingSourceType}
)
_OptionalFindingSourceTypeDef = TypedDict(
    "_OptionalFindingSourceTypeDef", {"detail": "FindingSourceDetailTypeDef"}, total=False
)


class FindingSourceTypeDef(_RequiredFindingSourceTypeDef, _OptionalFindingSourceTypeDef):
    pass


_RequiredFindingSummaryTypeDef = TypedDict(
    "_RequiredFindingSummaryTypeDef",
    {
        "analyzedAt": datetime,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "id": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceType,
        "status": FindingStatus,
        "updatedAt": datetime,
    },
)
_OptionalFindingSummaryTypeDef = TypedDict(
    "_OptionalFindingSummaryTypeDef",
    {
        "action": List[str],
        "error": str,
        "isPublic": bool,
        "principal": Dict[str, str],
        "resource": str,
        "sources": List["FindingSourceTypeDef"],
    },
    total=False,
)


class FindingSummaryTypeDef(_RequiredFindingSummaryTypeDef, _OptionalFindingSummaryTypeDef):
    pass


_RequiredFindingTypeDef = TypedDict(
    "_RequiredFindingTypeDef",
    {
        "analyzedAt": datetime,
        "condition": Dict[str, str],
        "createdAt": datetime,
        "id": str,
        "resourceOwnerAccount": str,
        "resourceType": ResourceType,
        "status": FindingStatus,
        "updatedAt": datetime,
    },
)
_OptionalFindingTypeDef = TypedDict(
    "_OptionalFindingTypeDef",
    {
        "action": List[str],
        "error": str,
        "isPublic": bool,
        "principal": Dict[str, str],
        "resource": str,
        "sources": List["FindingSourceTypeDef"],
    },
    total=False,
)


class FindingTypeDef(_RequiredFindingTypeDef, _OptionalFindingTypeDef):
    pass


class _RequiredGeneratedPolicyPropertiesTypeDef(TypedDict):
    principalArn: str


class GeneratedPolicyPropertiesTypeDef(_RequiredGeneratedPolicyPropertiesTypeDef, total=False):
    cloudTrailProperties: "CloudTrailPropertiesTypeDef"
    isComplete: bool


class _RequiredGeneratedPolicyResultTypeDef(TypedDict):
    properties: "GeneratedPolicyPropertiesTypeDef"


class GeneratedPolicyResultTypeDef(_RequiredGeneratedPolicyResultTypeDef, total=False):
    generatedPolicies: List["GeneratedPolicyTypeDef"]


class GeneratedPolicyTypeDef(TypedDict):
    policy: str


class GetAccessPreviewResponseTypeDef(TypedDict):
    accessPreview: "AccessPreviewTypeDef"


class GetAnalyzedResourceResponseTypeDef(TypedDict, total=False):
    resource: "AnalyzedResourceTypeDef"


class GetAnalyzerResponseTypeDef(TypedDict):
    analyzer: "AnalyzerSummaryTypeDef"


class GetArchiveRuleResponseTypeDef(TypedDict):
    archiveRule: "ArchiveRuleSummaryTypeDef"


class GetFindingResponseTypeDef(TypedDict, total=False):
    finding: "FindingTypeDef"


class GetGeneratedPolicyResponseTypeDef(TypedDict):
    generatedPolicyResult: "GeneratedPolicyResultTypeDef"
    jobDetails: "JobDetailsTypeDef"


class IamRoleConfigurationTypeDef(TypedDict, total=False):
    trustPolicy: str


InlineArchiveRuleTypeDef = TypedDict(
    "InlineArchiveRuleTypeDef", {"filter": Dict[str, "CriterionTypeDef"], "ruleName": str}
)


class _RequiredJobDetailsTypeDef(TypedDict):
    jobId: str
    startedOn: datetime
    status: JobStatus


class JobDetailsTypeDef(_RequiredJobDetailsTypeDef, total=False):
    completedOn: datetime
    jobError: "JobErrorTypeDef"


class JobErrorTypeDef(TypedDict):
    code: JobErrorCode
    message: str


class _RequiredKmsGrantConfigurationTypeDef(TypedDict):
    granteePrincipal: str
    issuingAccount: str
    operations: List[KmsGrantOperation]


class KmsGrantConfigurationTypeDef(_RequiredKmsGrantConfigurationTypeDef, total=False):
    constraints: "KmsGrantConstraintsTypeDef"
    retiringPrincipal: str


class KmsGrantConstraintsTypeDef(TypedDict, total=False):
    encryptionContextEquals: Dict[str, str]
    encryptionContextSubset: Dict[str, str]


class KmsKeyConfigurationTypeDef(TypedDict, total=False):
    grants: List["KmsGrantConfigurationTypeDef"]
    keyPolicies: Dict[str, str]


class _RequiredListAccessPreviewFindingsResponseTypeDef(TypedDict):
    findings: List["AccessPreviewFindingTypeDef"]


class ListAccessPreviewFindingsResponseTypeDef(
    _RequiredListAccessPreviewFindingsResponseTypeDef, total=False
):
    nextToken: str


class _RequiredListAccessPreviewsResponseTypeDef(TypedDict):
    accessPreviews: List["AccessPreviewSummaryTypeDef"]


class ListAccessPreviewsResponseTypeDef(_RequiredListAccessPreviewsResponseTypeDef, total=False):
    nextToken: str


class _RequiredListAnalyzedResourcesResponseTypeDef(TypedDict):
    analyzedResources: List["AnalyzedResourceSummaryTypeDef"]


class ListAnalyzedResourcesResponseTypeDef(
    _RequiredListAnalyzedResourcesResponseTypeDef, total=False
):
    nextToken: str


class _RequiredListAnalyzersResponseTypeDef(TypedDict):
    analyzers: List["AnalyzerSummaryTypeDef"]


class ListAnalyzersResponseTypeDef(_RequiredListAnalyzersResponseTypeDef, total=False):
    nextToken: str


class _RequiredListArchiveRulesResponseTypeDef(TypedDict):
    archiveRules: List["ArchiveRuleSummaryTypeDef"]


class ListArchiveRulesResponseTypeDef(_RequiredListArchiveRulesResponseTypeDef, total=False):
    nextToken: str


class _RequiredListFindingsResponseTypeDef(TypedDict):
    findings: List["FindingSummaryTypeDef"]


class ListFindingsResponseTypeDef(_RequiredListFindingsResponseTypeDef, total=False):
    nextToken: str


class _RequiredListPolicyGenerationsResponseTypeDef(TypedDict):
    policyGenerations: List["PolicyGenerationTypeDef"]


class ListPolicyGenerationsResponseTypeDef(
    _RequiredListPolicyGenerationsResponseTypeDef, total=False
):
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class LocationTypeDef(TypedDict):
    path: List["PathElementTypeDef"]
    span: "SpanTypeDef"


class NetworkOriginConfigurationTypeDef(TypedDict, total=False):
    internetConfiguration: Dict[str, Any]
    vpcConfiguration: "VpcConfigurationTypeDef"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PathElementTypeDef(TypedDict, total=False):
    index: int
    key: str
    substring: "SubstringTypeDef"
    value: str


class PolicyGenerationDetailsTypeDef(TypedDict):
    principalArn: str


class _RequiredPolicyGenerationTypeDef(TypedDict):
    jobId: str
    principalArn: str
    startedOn: datetime
    status: JobStatus


class PolicyGenerationTypeDef(_RequiredPolicyGenerationTypeDef, total=False):
    completedOn: datetime


class PositionTypeDef(TypedDict):
    column: int
    line: int
    offset: int


class S3AccessPointConfigurationTypeDef(TypedDict, total=False):
    accessPointPolicy: str
    networkOrigin: "NetworkOriginConfigurationTypeDef"
    publicAccessBlock: "S3PublicAccessBlockConfigurationTypeDef"


class S3BucketAclGrantConfigurationTypeDef(TypedDict):
    grantee: "AclGranteeTypeDef"
    permission: AclPermission


class S3BucketConfigurationTypeDef(TypedDict, total=False):
    accessPoints: Dict[str, "S3AccessPointConfigurationTypeDef"]
    bucketAclGrants: List["S3BucketAclGrantConfigurationTypeDef"]
    bucketPolicy: str
    bucketPublicAccessBlock: "S3PublicAccessBlockConfigurationTypeDef"


class S3PublicAccessBlockConfigurationTypeDef(TypedDict):
    ignorePublicAcls: bool
    restrictPublicBuckets: bool


class SecretsManagerSecretConfigurationTypeDef(TypedDict, total=False):
    kmsKeyId: str
    secretPolicy: str


class SortCriteriaTypeDef(TypedDict, total=False):
    attributeName: str
    orderBy: OrderBy


class SpanTypeDef(TypedDict):
    end: "PositionTypeDef"
    start: "PositionTypeDef"


class SqsQueueConfigurationTypeDef(TypedDict, total=False):
    queuePolicy: str


class StartPolicyGenerationResponseTypeDef(TypedDict):
    jobId: str


class StatusReasonTypeDef(TypedDict):
    code: ReasonCode


class SubstringTypeDef(TypedDict):
    length: int
    start: int


class _RequiredTrailPropertiesTypeDef(TypedDict):
    cloudTrailArn: str


class TrailPropertiesTypeDef(_RequiredTrailPropertiesTypeDef, total=False):
    allRegions: bool
    regions: List[str]


class _RequiredTrailTypeDef(TypedDict):
    cloudTrailArn: str


class TrailTypeDef(_RequiredTrailTypeDef, total=False):
    allRegions: bool
    regions: List[str]


class ValidatePolicyFindingTypeDef(TypedDict):
    findingDetails: str
    findingType: ValidatePolicyFindingType
    issueCode: str
    learnMoreLink: str
    locations: List["LocationTypeDef"]


class _RequiredValidatePolicyResponseTypeDef(TypedDict):
    findings: List["ValidatePolicyFindingTypeDef"]


class ValidatePolicyResponseTypeDef(_RequiredValidatePolicyResponseTypeDef, total=False):
    nextToken: str


class VpcConfigurationTypeDef(TypedDict):
    vpcId: str
