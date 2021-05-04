"""
Type annotations for cloudfront service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudfront.type_defs import ActiveTrustedKeyGroupsTypeDef

    data: ActiveTrustedKeyGroupsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, List, Union

from mypy_boto3_cloudfront.literals import (
    CachePolicyCookieBehavior,
    CachePolicyHeaderBehavior,
    CachePolicyQueryStringBehavior,
    CachePolicyType,
    CertificateSource,
    EventType,
    FunctionStage,
    GeoRestrictionType,
    HttpVersion,
    ICPRecordalStatus,
    ItemSelection,
    Method,
    MinimumProtocolVersion,
    OriginProtocolPolicy,
    OriginRequestPolicyCookieBehavior,
    OriginRequestPolicyHeaderBehavior,
    OriginRequestPolicyQueryStringBehavior,
    OriginRequestPolicyType,
    PriceClass,
    RealtimeMetricsSubscriptionStatus,
    SslProtocol,
    SSLSupportMethod,
    ViewerProtocolPolicy,
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
    "ActiveTrustedKeyGroupsTypeDef",
    "ActiveTrustedSignersTypeDef",
    "AliasICPRecordalTypeDef",
    "AliasesTypeDef",
    "AllowedMethodsTypeDef",
    "CacheBehaviorTypeDef",
    "CacheBehaviorsTypeDef",
    "CachePolicyConfigTypeDef",
    "CachePolicyCookiesConfigTypeDef",
    "CachePolicyHeadersConfigTypeDef",
    "CachePolicyListTypeDef",
    "CachePolicyQueryStringsConfigTypeDef",
    "CachePolicySummaryTypeDef",
    "CachePolicyTypeDef",
    "CachedMethodsTypeDef",
    "CloudFrontOriginAccessIdentityConfigTypeDef",
    "CloudFrontOriginAccessIdentityListTypeDef",
    "CloudFrontOriginAccessIdentitySummaryTypeDef",
    "CloudFrontOriginAccessIdentityTypeDef",
    "ContentTypeProfileConfigTypeDef",
    "ContentTypeProfileTypeDef",
    "ContentTypeProfilesTypeDef",
    "CookieNamesTypeDef",
    "CookiePreferenceTypeDef",
    "CreateCachePolicyResultTypeDef",
    "CreateCloudFrontOriginAccessIdentityResultTypeDef",
    "CreateDistributionResultTypeDef",
    "CreateDistributionWithTagsResultTypeDef",
    "CreateFieldLevelEncryptionConfigResultTypeDef",
    "CreateFieldLevelEncryptionProfileResultTypeDef",
    "CreateFunctionResultTypeDef",
    "CreateInvalidationResultTypeDef",
    "CreateKeyGroupResultTypeDef",
    "CreateMonitoringSubscriptionResultTypeDef",
    "CreateOriginRequestPolicyResultTypeDef",
    "CreatePublicKeyResultTypeDef",
    "CreateRealtimeLogConfigResultTypeDef",
    "CreateStreamingDistributionResultTypeDef",
    "CreateStreamingDistributionWithTagsResultTypeDef",
    "CustomErrorResponseTypeDef",
    "CustomErrorResponsesTypeDef",
    "CustomHeadersTypeDef",
    "CustomOriginConfigTypeDef",
    "DefaultCacheBehaviorTypeDef",
    "DescribeFunctionResultTypeDef",
    "DistributionConfigTypeDef",
    "DistributionConfigWithTagsTypeDef",
    "DistributionIdListTypeDef",
    "DistributionListTypeDef",
    "DistributionSummaryTypeDef",
    "DistributionTypeDef",
    "EncryptionEntitiesTypeDef",
    "EncryptionEntityTypeDef",
    "EndPointTypeDef",
    "FieldLevelEncryptionConfigTypeDef",
    "FieldLevelEncryptionListTypeDef",
    "FieldLevelEncryptionProfileConfigTypeDef",
    "FieldLevelEncryptionProfileListTypeDef",
    "FieldLevelEncryptionProfileSummaryTypeDef",
    "FieldLevelEncryptionProfileTypeDef",
    "FieldLevelEncryptionSummaryTypeDef",
    "FieldLevelEncryptionTypeDef",
    "FieldPatternsTypeDef",
    "ForwardedValuesTypeDef",
    "FunctionAssociationTypeDef",
    "FunctionAssociationsTypeDef",
    "FunctionConfigTypeDef",
    "FunctionListTypeDef",
    "FunctionMetadataTypeDef",
    "FunctionSummaryTypeDef",
    "GeoRestrictionTypeDef",
    "GetCachePolicyConfigResultTypeDef",
    "GetCachePolicyResultTypeDef",
    "GetCloudFrontOriginAccessIdentityConfigResultTypeDef",
    "GetCloudFrontOriginAccessIdentityResultTypeDef",
    "GetDistributionConfigResultTypeDef",
    "GetDistributionResultTypeDef",
    "GetFieldLevelEncryptionConfigResultTypeDef",
    "GetFieldLevelEncryptionProfileConfigResultTypeDef",
    "GetFieldLevelEncryptionProfileResultTypeDef",
    "GetFieldLevelEncryptionResultTypeDef",
    "GetFunctionResultTypeDef",
    "GetInvalidationResultTypeDef",
    "GetKeyGroupConfigResultTypeDef",
    "GetKeyGroupResultTypeDef",
    "GetMonitoringSubscriptionResultTypeDef",
    "GetOriginRequestPolicyConfigResultTypeDef",
    "GetOriginRequestPolicyResultTypeDef",
    "GetPublicKeyConfigResultTypeDef",
    "GetPublicKeyResultTypeDef",
    "GetRealtimeLogConfigResultTypeDef",
    "GetStreamingDistributionConfigResultTypeDef",
    "GetStreamingDistributionResultTypeDef",
    "HeadersTypeDef",
    "InvalidationBatchTypeDef",
    "InvalidationListTypeDef",
    "InvalidationSummaryTypeDef",
    "InvalidationTypeDef",
    "KGKeyPairIdsTypeDef",
    "KeyGroupConfigTypeDef",
    "KeyGroupListTypeDef",
    "KeyGroupSummaryTypeDef",
    "KeyGroupTypeDef",
    "KeyPairIdsTypeDef",
    "KinesisStreamConfigTypeDef",
    "LambdaFunctionAssociationTypeDef",
    "LambdaFunctionAssociationsTypeDef",
    "ListCachePoliciesResultTypeDef",
    "ListCloudFrontOriginAccessIdentitiesResultTypeDef",
    "ListDistributionsByCachePolicyIdResultTypeDef",
    "ListDistributionsByKeyGroupResultTypeDef",
    "ListDistributionsByOriginRequestPolicyIdResultTypeDef",
    "ListDistributionsByRealtimeLogConfigResultTypeDef",
    "ListDistributionsByWebACLIdResultTypeDef",
    "ListDistributionsResultTypeDef",
    "ListFieldLevelEncryptionConfigsResultTypeDef",
    "ListFieldLevelEncryptionProfilesResultTypeDef",
    "ListFunctionsResultTypeDef",
    "ListInvalidationsResultTypeDef",
    "ListKeyGroupsResultTypeDef",
    "ListOriginRequestPoliciesResultTypeDef",
    "ListPublicKeysResultTypeDef",
    "ListRealtimeLogConfigsResultTypeDef",
    "ListStreamingDistributionsResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "LoggingConfigTypeDef",
    "MonitoringSubscriptionTypeDef",
    "OriginCustomHeaderTypeDef",
    "OriginGroupFailoverCriteriaTypeDef",
    "OriginGroupMemberTypeDef",
    "OriginGroupMembersTypeDef",
    "OriginGroupTypeDef",
    "OriginGroupsTypeDef",
    "OriginRequestPolicyConfigTypeDef",
    "OriginRequestPolicyCookiesConfigTypeDef",
    "OriginRequestPolicyHeadersConfigTypeDef",
    "OriginRequestPolicyListTypeDef",
    "OriginRequestPolicyQueryStringsConfigTypeDef",
    "OriginRequestPolicySummaryTypeDef",
    "OriginRequestPolicyTypeDef",
    "OriginShieldTypeDef",
    "OriginSslProtocolsTypeDef",
    "OriginTypeDef",
    "OriginsTypeDef",
    "PaginatorConfigTypeDef",
    "ParametersInCacheKeyAndForwardedToOriginTypeDef",
    "PathsTypeDef",
    "PublicKeyConfigTypeDef",
    "PublicKeyListTypeDef",
    "PublicKeySummaryTypeDef",
    "PublicKeyTypeDef",
    "PublishFunctionResultTypeDef",
    "QueryArgProfileConfigTypeDef",
    "QueryArgProfileTypeDef",
    "QueryArgProfilesTypeDef",
    "QueryStringCacheKeysTypeDef",
    "QueryStringNamesTypeDef",
    "RealtimeLogConfigTypeDef",
    "RealtimeLogConfigsTypeDef",
    "RealtimeMetricsSubscriptionConfigTypeDef",
    "RestrictionsTypeDef",
    "S3OriginConfigTypeDef",
    "S3OriginTypeDef",
    "SignerTypeDef",
    "StatusCodesTypeDef",
    "StreamingDistributionConfigTypeDef",
    "StreamingDistributionConfigWithTagsTypeDef",
    "StreamingDistributionListTypeDef",
    "StreamingDistributionSummaryTypeDef",
    "StreamingDistributionTypeDef",
    "StreamingLoggingConfigTypeDef",
    "TagKeysTypeDef",
    "TagTypeDef",
    "TagsTypeDef",
    "TestFunctionResultTypeDef",
    "TestResultTypeDef",
    "TrustedKeyGroupsTypeDef",
    "TrustedSignersTypeDef",
    "UpdateCachePolicyResultTypeDef",
    "UpdateCloudFrontOriginAccessIdentityResultTypeDef",
    "UpdateDistributionResultTypeDef",
    "UpdateFieldLevelEncryptionConfigResultTypeDef",
    "UpdateFieldLevelEncryptionProfileResultTypeDef",
    "UpdateFunctionResultTypeDef",
    "UpdateKeyGroupResultTypeDef",
    "UpdateOriginRequestPolicyResultTypeDef",
    "UpdatePublicKeyResultTypeDef",
    "UpdateRealtimeLogConfigResultTypeDef",
    "UpdateStreamingDistributionResultTypeDef",
    "ViewerCertificateTypeDef",
    "WaiterConfigTypeDef",
)


class _RequiredActiveTrustedKeyGroupsTypeDef(TypedDict):
    Enabled: bool
    Quantity: int


class ActiveTrustedKeyGroupsTypeDef(_RequiredActiveTrustedKeyGroupsTypeDef, total=False):
    Items: List["KGKeyPairIdsTypeDef"]


class _RequiredActiveTrustedSignersTypeDef(TypedDict):
    Enabled: bool
    Quantity: int


class ActiveTrustedSignersTypeDef(_RequiredActiveTrustedSignersTypeDef, total=False):
    Items: List["SignerTypeDef"]


class AliasICPRecordalTypeDef(TypedDict, total=False):
    CNAME: str
    ICPRecordalStatus: ICPRecordalStatus


class _RequiredAliasesTypeDef(TypedDict):
    Quantity: int


class AliasesTypeDef(_RequiredAliasesTypeDef, total=False):
    Items: List[str]


class _RequiredAllowedMethodsTypeDef(TypedDict):
    Quantity: int
    Items: List[Method]


class AllowedMethodsTypeDef(_RequiredAllowedMethodsTypeDef, total=False):
    CachedMethods: "CachedMethodsTypeDef"


class _RequiredCacheBehaviorTypeDef(TypedDict):
    PathPattern: str
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicy


class CacheBehaviorTypeDef(_RequiredCacheBehaviorTypeDef, total=False):
    TrustedSigners: "TrustedSignersTypeDef"
    TrustedKeyGroups: "TrustedKeyGroupsTypeDef"
    AllowedMethods: "AllowedMethodsTypeDef"
    SmoothStreaming: bool
    Compress: bool
    LambdaFunctionAssociations: "LambdaFunctionAssociationsTypeDef"
    FunctionAssociations: "FunctionAssociationsTypeDef"
    FieldLevelEncryptionId: str
    RealtimeLogConfigArn: str
    CachePolicyId: str
    OriginRequestPolicyId: str
    ForwardedValues: "ForwardedValuesTypeDef"
    MinTTL: int
    DefaultTTL: int
    MaxTTL: int


class _RequiredCacheBehaviorsTypeDef(TypedDict):
    Quantity: int


class CacheBehaviorsTypeDef(_RequiredCacheBehaviorsTypeDef, total=False):
    Items: List["CacheBehaviorTypeDef"]


class _RequiredCachePolicyConfigTypeDef(TypedDict):
    Name: str
    MinTTL: int


class CachePolicyConfigTypeDef(_RequiredCachePolicyConfigTypeDef, total=False):
    Comment: str
    DefaultTTL: int
    MaxTTL: int
    ParametersInCacheKeyAndForwardedToOrigin: "ParametersInCacheKeyAndForwardedToOriginTypeDef"


class _RequiredCachePolicyCookiesConfigTypeDef(TypedDict):
    CookieBehavior: CachePolicyCookieBehavior


class CachePolicyCookiesConfigTypeDef(_RequiredCachePolicyCookiesConfigTypeDef, total=False):
    Cookies: "CookieNamesTypeDef"


class _RequiredCachePolicyHeadersConfigTypeDef(TypedDict):
    HeaderBehavior: CachePolicyHeaderBehavior


class CachePolicyHeadersConfigTypeDef(_RequiredCachePolicyHeadersConfigTypeDef, total=False):
    Headers: "HeadersTypeDef"


class _RequiredCachePolicyListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int


class CachePolicyListTypeDef(_RequiredCachePolicyListTypeDef, total=False):
    NextMarker: str
    Items: List["CachePolicySummaryTypeDef"]


class _RequiredCachePolicyQueryStringsConfigTypeDef(TypedDict):
    QueryStringBehavior: CachePolicyQueryStringBehavior


class CachePolicyQueryStringsConfigTypeDef(
    _RequiredCachePolicyQueryStringsConfigTypeDef, total=False
):
    QueryStrings: "QueryStringNamesTypeDef"


CachePolicySummaryTypeDef = TypedDict(
    "CachePolicySummaryTypeDef", {"Type": CachePolicyType, "CachePolicy": "CachePolicyTypeDef"}
)


class CachePolicyTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime
    CachePolicyConfig: "CachePolicyConfigTypeDef"


class CachedMethodsTypeDef(TypedDict):
    Quantity: int
    Items: List[Method]


class CloudFrontOriginAccessIdentityConfigTypeDef(TypedDict):
    CallerReference: str
    Comment: str


class _RequiredCloudFrontOriginAccessIdentityListTypeDef(TypedDict):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int


class CloudFrontOriginAccessIdentityListTypeDef(
    _RequiredCloudFrontOriginAccessIdentityListTypeDef, total=False
):
    NextMarker: str
    Items: List["CloudFrontOriginAccessIdentitySummaryTypeDef"]


class CloudFrontOriginAccessIdentitySummaryTypeDef(TypedDict):
    Id: str
    S3CanonicalUserId: str
    Comment: str


class _RequiredCloudFrontOriginAccessIdentityTypeDef(TypedDict):
    Id: str
    S3CanonicalUserId: str


class CloudFrontOriginAccessIdentityTypeDef(
    _RequiredCloudFrontOriginAccessIdentityTypeDef, total=False
):
    CloudFrontOriginAccessIdentityConfig: "CloudFrontOriginAccessIdentityConfigTypeDef"


class _RequiredContentTypeProfileConfigTypeDef(TypedDict):
    ForwardWhenContentTypeIsUnknown: bool


class ContentTypeProfileConfigTypeDef(_RequiredContentTypeProfileConfigTypeDef, total=False):
    ContentTypeProfiles: "ContentTypeProfilesTypeDef"


class _RequiredContentTypeProfileTypeDef(TypedDict):
    Format: Literal["URLEncoded"]
    ContentType: str


class ContentTypeProfileTypeDef(_RequiredContentTypeProfileTypeDef, total=False):
    ProfileId: str


class _RequiredContentTypeProfilesTypeDef(TypedDict):
    Quantity: int


class ContentTypeProfilesTypeDef(_RequiredContentTypeProfilesTypeDef, total=False):
    Items: List["ContentTypeProfileTypeDef"]


class _RequiredCookieNamesTypeDef(TypedDict):
    Quantity: int


class CookieNamesTypeDef(_RequiredCookieNamesTypeDef, total=False):
    Items: List[str]


class _RequiredCookiePreferenceTypeDef(TypedDict):
    Forward: ItemSelection


class CookiePreferenceTypeDef(_RequiredCookiePreferenceTypeDef, total=False):
    WhitelistedNames: "CookieNamesTypeDef"


class CreateCachePolicyResultTypeDef(TypedDict, total=False):
    CachePolicy: "CachePolicyTypeDef"
    Location: str
    ETag: str


class CreateCloudFrontOriginAccessIdentityResultTypeDef(TypedDict, total=False):
    CloudFrontOriginAccessIdentity: "CloudFrontOriginAccessIdentityTypeDef"
    Location: str
    ETag: str


class CreateDistributionResultTypeDef(TypedDict, total=False):
    Distribution: "DistributionTypeDef"
    Location: str
    ETag: str


class CreateDistributionWithTagsResultTypeDef(TypedDict, total=False):
    Distribution: "DistributionTypeDef"
    Location: str
    ETag: str


class CreateFieldLevelEncryptionConfigResultTypeDef(TypedDict, total=False):
    FieldLevelEncryption: "FieldLevelEncryptionTypeDef"
    Location: str
    ETag: str


class CreateFieldLevelEncryptionProfileResultTypeDef(TypedDict, total=False):
    FieldLevelEncryptionProfile: "FieldLevelEncryptionProfileTypeDef"
    Location: str
    ETag: str


class CreateFunctionResultTypeDef(TypedDict, total=False):
    FunctionSummary: "FunctionSummaryTypeDef"
    Location: str
    ETag: str


class CreateInvalidationResultTypeDef(TypedDict, total=False):
    Location: str
    Invalidation: "InvalidationTypeDef"


class CreateKeyGroupResultTypeDef(TypedDict, total=False):
    KeyGroup: "KeyGroupTypeDef"
    Location: str
    ETag: str


class CreateMonitoringSubscriptionResultTypeDef(TypedDict, total=False):
    MonitoringSubscription: "MonitoringSubscriptionTypeDef"


class CreateOriginRequestPolicyResultTypeDef(TypedDict, total=False):
    OriginRequestPolicy: "OriginRequestPolicyTypeDef"
    Location: str
    ETag: str


class CreatePublicKeyResultTypeDef(TypedDict, total=False):
    PublicKey: "PublicKeyTypeDef"
    Location: str
    ETag: str


class CreateRealtimeLogConfigResultTypeDef(TypedDict, total=False):
    RealtimeLogConfig: "RealtimeLogConfigTypeDef"


class CreateStreamingDistributionResultTypeDef(TypedDict, total=False):
    StreamingDistribution: "StreamingDistributionTypeDef"
    Location: str
    ETag: str


class CreateStreamingDistributionWithTagsResultTypeDef(TypedDict, total=False):
    StreamingDistribution: "StreamingDistributionTypeDef"
    Location: str
    ETag: str


class _RequiredCustomErrorResponseTypeDef(TypedDict):
    ErrorCode: int


class CustomErrorResponseTypeDef(_RequiredCustomErrorResponseTypeDef, total=False):
    ResponsePagePath: str
    ResponseCode: str
    ErrorCachingMinTTL: int


class _RequiredCustomErrorResponsesTypeDef(TypedDict):
    Quantity: int


class CustomErrorResponsesTypeDef(_RequiredCustomErrorResponsesTypeDef, total=False):
    Items: List["CustomErrorResponseTypeDef"]


class _RequiredCustomHeadersTypeDef(TypedDict):
    Quantity: int


class CustomHeadersTypeDef(_RequiredCustomHeadersTypeDef, total=False):
    Items: List["OriginCustomHeaderTypeDef"]


class _RequiredCustomOriginConfigTypeDef(TypedDict):
    HTTPPort: int
    HTTPSPort: int
    OriginProtocolPolicy: OriginProtocolPolicy


class CustomOriginConfigTypeDef(_RequiredCustomOriginConfigTypeDef, total=False):
    OriginSslProtocols: "OriginSslProtocolsTypeDef"
    OriginReadTimeout: int
    OriginKeepaliveTimeout: int


class _RequiredDefaultCacheBehaviorTypeDef(TypedDict):
    TargetOriginId: str
    ViewerProtocolPolicy: ViewerProtocolPolicy


class DefaultCacheBehaviorTypeDef(_RequiredDefaultCacheBehaviorTypeDef, total=False):
    TrustedSigners: "TrustedSignersTypeDef"
    TrustedKeyGroups: "TrustedKeyGroupsTypeDef"
    AllowedMethods: "AllowedMethodsTypeDef"
    SmoothStreaming: bool
    Compress: bool
    LambdaFunctionAssociations: "LambdaFunctionAssociationsTypeDef"
    FunctionAssociations: "FunctionAssociationsTypeDef"
    FieldLevelEncryptionId: str
    RealtimeLogConfigArn: str
    CachePolicyId: str
    OriginRequestPolicyId: str
    ForwardedValues: "ForwardedValuesTypeDef"
    MinTTL: int
    DefaultTTL: int
    MaxTTL: int


class DescribeFunctionResultTypeDef(TypedDict, total=False):
    FunctionSummary: "FunctionSummaryTypeDef"
    ETag: str


class _RequiredDistributionConfigTypeDef(TypedDict):
    CallerReference: str
    Origins: "OriginsTypeDef"
    DefaultCacheBehavior: "DefaultCacheBehaviorTypeDef"
    Comment: str
    Enabled: bool


class DistributionConfigTypeDef(_RequiredDistributionConfigTypeDef, total=False):
    Aliases: "AliasesTypeDef"
    DefaultRootObject: str
    OriginGroups: "OriginGroupsTypeDef"
    CacheBehaviors: "CacheBehaviorsTypeDef"
    CustomErrorResponses: "CustomErrorResponsesTypeDef"
    Logging: "LoggingConfigTypeDef"
    PriceClass: PriceClass
    ViewerCertificate: "ViewerCertificateTypeDef"
    Restrictions: "RestrictionsTypeDef"
    WebACLId: str
    HttpVersion: HttpVersion
    IsIPV6Enabled: bool


class DistributionConfigWithTagsTypeDef(TypedDict):
    DistributionConfig: "DistributionConfigTypeDef"
    Tags: "TagsTypeDef"


class _RequiredDistributionIdListTypeDef(TypedDict):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int


class DistributionIdListTypeDef(_RequiredDistributionIdListTypeDef, total=False):
    NextMarker: str
    Items: List[str]


class _RequiredDistributionListTypeDef(TypedDict):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int


class DistributionListTypeDef(_RequiredDistributionListTypeDef, total=False):
    NextMarker: str
    Items: List["DistributionSummaryTypeDef"]


class _RequiredDistributionSummaryTypeDef(TypedDict):
    Id: str
    ARN: str
    Status: str
    LastModifiedTime: datetime
    DomainName: str
    Aliases: "AliasesTypeDef"
    Origins: "OriginsTypeDef"
    DefaultCacheBehavior: "DefaultCacheBehaviorTypeDef"
    CacheBehaviors: "CacheBehaviorsTypeDef"
    CustomErrorResponses: "CustomErrorResponsesTypeDef"
    Comment: str
    PriceClass: PriceClass
    Enabled: bool
    ViewerCertificate: "ViewerCertificateTypeDef"
    Restrictions: "RestrictionsTypeDef"
    WebACLId: str
    HttpVersion: HttpVersion
    IsIPV6Enabled: bool


class DistributionSummaryTypeDef(_RequiredDistributionSummaryTypeDef, total=False):
    OriginGroups: "OriginGroupsTypeDef"
    AliasICPRecordals: List["AliasICPRecordalTypeDef"]


class _RequiredDistributionTypeDef(TypedDict):
    Id: str
    ARN: str
    Status: str
    LastModifiedTime: datetime
    InProgressInvalidationBatches: int
    DomainName: str
    DistributionConfig: "DistributionConfigTypeDef"


class DistributionTypeDef(_RequiredDistributionTypeDef, total=False):
    ActiveTrustedSigners: "ActiveTrustedSignersTypeDef"
    ActiveTrustedKeyGroups: "ActiveTrustedKeyGroupsTypeDef"
    AliasICPRecordals: List["AliasICPRecordalTypeDef"]


class _RequiredEncryptionEntitiesTypeDef(TypedDict):
    Quantity: int


class EncryptionEntitiesTypeDef(_RequiredEncryptionEntitiesTypeDef, total=False):
    Items: List["EncryptionEntityTypeDef"]


class EncryptionEntityTypeDef(TypedDict):
    PublicKeyId: str
    ProviderId: str
    FieldPatterns: "FieldPatternsTypeDef"


class _RequiredEndPointTypeDef(TypedDict):
    StreamType: str


class EndPointTypeDef(_RequiredEndPointTypeDef, total=False):
    KinesisStreamConfig: "KinesisStreamConfigTypeDef"


class _RequiredFieldLevelEncryptionConfigTypeDef(TypedDict):
    CallerReference: str


class FieldLevelEncryptionConfigTypeDef(_RequiredFieldLevelEncryptionConfigTypeDef, total=False):
    Comment: str
    QueryArgProfileConfig: "QueryArgProfileConfigTypeDef"
    ContentTypeProfileConfig: "ContentTypeProfileConfigTypeDef"


class _RequiredFieldLevelEncryptionListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int


class FieldLevelEncryptionListTypeDef(_RequiredFieldLevelEncryptionListTypeDef, total=False):
    NextMarker: str
    Items: List["FieldLevelEncryptionSummaryTypeDef"]


class _RequiredFieldLevelEncryptionProfileConfigTypeDef(TypedDict):
    Name: str
    CallerReference: str
    EncryptionEntities: "EncryptionEntitiesTypeDef"


class FieldLevelEncryptionProfileConfigTypeDef(
    _RequiredFieldLevelEncryptionProfileConfigTypeDef, total=False
):
    Comment: str


class _RequiredFieldLevelEncryptionProfileListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int


class FieldLevelEncryptionProfileListTypeDef(
    _RequiredFieldLevelEncryptionProfileListTypeDef, total=False
):
    NextMarker: str
    Items: List["FieldLevelEncryptionProfileSummaryTypeDef"]


class _RequiredFieldLevelEncryptionProfileSummaryTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime
    Name: str
    EncryptionEntities: "EncryptionEntitiesTypeDef"


class FieldLevelEncryptionProfileSummaryTypeDef(
    _RequiredFieldLevelEncryptionProfileSummaryTypeDef, total=False
):
    Comment: str


class FieldLevelEncryptionProfileTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime
    FieldLevelEncryptionProfileConfig: "FieldLevelEncryptionProfileConfigTypeDef"


class _RequiredFieldLevelEncryptionSummaryTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime


class FieldLevelEncryptionSummaryTypeDef(_RequiredFieldLevelEncryptionSummaryTypeDef, total=False):
    Comment: str
    QueryArgProfileConfig: "QueryArgProfileConfigTypeDef"
    ContentTypeProfileConfig: "ContentTypeProfileConfigTypeDef"


class FieldLevelEncryptionTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime
    FieldLevelEncryptionConfig: "FieldLevelEncryptionConfigTypeDef"


class _RequiredFieldPatternsTypeDef(TypedDict):
    Quantity: int


class FieldPatternsTypeDef(_RequiredFieldPatternsTypeDef, total=False):
    Items: List[str]


class _RequiredForwardedValuesTypeDef(TypedDict):
    QueryString: bool
    Cookies: "CookiePreferenceTypeDef"


class ForwardedValuesTypeDef(_RequiredForwardedValuesTypeDef, total=False):
    Headers: "HeadersTypeDef"
    QueryStringCacheKeys: "QueryStringCacheKeysTypeDef"


class FunctionAssociationTypeDef(TypedDict):
    FunctionARN: str
    EventType: EventType


class _RequiredFunctionAssociationsTypeDef(TypedDict):
    Quantity: int


class FunctionAssociationsTypeDef(_RequiredFunctionAssociationsTypeDef, total=False):
    Items: List["FunctionAssociationTypeDef"]


class FunctionConfigTypeDef(TypedDict):
    Comment: str
    Runtime: Literal["cloudfront-js-1.0"]


class _RequiredFunctionListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int


class FunctionListTypeDef(_RequiredFunctionListTypeDef, total=False):
    NextMarker: str
    Items: List["FunctionSummaryTypeDef"]


class _RequiredFunctionMetadataTypeDef(TypedDict):
    FunctionARN: str
    LastModifiedTime: datetime


class FunctionMetadataTypeDef(_RequiredFunctionMetadataTypeDef, total=False):
    Stage: FunctionStage
    CreatedTime: datetime


class _RequiredFunctionSummaryTypeDef(TypedDict):
    Name: str
    FunctionConfig: "FunctionConfigTypeDef"
    FunctionMetadata: "FunctionMetadataTypeDef"


class FunctionSummaryTypeDef(_RequiredFunctionSummaryTypeDef, total=False):
    Status: str


class _RequiredGeoRestrictionTypeDef(TypedDict):
    RestrictionType: GeoRestrictionType
    Quantity: int


class GeoRestrictionTypeDef(_RequiredGeoRestrictionTypeDef, total=False):
    Items: List[str]


class GetCachePolicyConfigResultTypeDef(TypedDict, total=False):
    CachePolicyConfig: "CachePolicyConfigTypeDef"
    ETag: str


class GetCachePolicyResultTypeDef(TypedDict, total=False):
    CachePolicy: "CachePolicyTypeDef"
    ETag: str


class GetCloudFrontOriginAccessIdentityConfigResultTypeDef(TypedDict, total=False):
    CloudFrontOriginAccessIdentityConfig: "CloudFrontOriginAccessIdentityConfigTypeDef"
    ETag: str


class GetCloudFrontOriginAccessIdentityResultTypeDef(TypedDict, total=False):
    CloudFrontOriginAccessIdentity: "CloudFrontOriginAccessIdentityTypeDef"
    ETag: str


class GetDistributionConfigResultTypeDef(TypedDict, total=False):
    DistributionConfig: "DistributionConfigTypeDef"
    ETag: str


class GetDistributionResultTypeDef(TypedDict, total=False):
    Distribution: "DistributionTypeDef"
    ETag: str


class GetFieldLevelEncryptionConfigResultTypeDef(TypedDict, total=False):
    FieldLevelEncryptionConfig: "FieldLevelEncryptionConfigTypeDef"
    ETag: str


class GetFieldLevelEncryptionProfileConfigResultTypeDef(TypedDict, total=False):
    FieldLevelEncryptionProfileConfig: "FieldLevelEncryptionProfileConfigTypeDef"
    ETag: str


class GetFieldLevelEncryptionProfileResultTypeDef(TypedDict, total=False):
    FieldLevelEncryptionProfile: "FieldLevelEncryptionProfileTypeDef"
    ETag: str


class GetFieldLevelEncryptionResultTypeDef(TypedDict, total=False):
    FieldLevelEncryption: "FieldLevelEncryptionTypeDef"
    ETag: str


class GetFunctionResultTypeDef(TypedDict, total=False):
    FunctionCode: Union[bytes, IO[bytes]]
    ETag: str
    ContentType: str


class GetInvalidationResultTypeDef(TypedDict, total=False):
    Invalidation: "InvalidationTypeDef"


class GetKeyGroupConfigResultTypeDef(TypedDict, total=False):
    KeyGroupConfig: "KeyGroupConfigTypeDef"
    ETag: str


class GetKeyGroupResultTypeDef(TypedDict, total=False):
    KeyGroup: "KeyGroupTypeDef"
    ETag: str


class GetMonitoringSubscriptionResultTypeDef(TypedDict, total=False):
    MonitoringSubscription: "MonitoringSubscriptionTypeDef"


class GetOriginRequestPolicyConfigResultTypeDef(TypedDict, total=False):
    OriginRequestPolicyConfig: "OriginRequestPolicyConfigTypeDef"
    ETag: str


class GetOriginRequestPolicyResultTypeDef(TypedDict, total=False):
    OriginRequestPolicy: "OriginRequestPolicyTypeDef"
    ETag: str


class GetPublicKeyConfigResultTypeDef(TypedDict, total=False):
    PublicKeyConfig: "PublicKeyConfigTypeDef"
    ETag: str


class GetPublicKeyResultTypeDef(TypedDict, total=False):
    PublicKey: "PublicKeyTypeDef"
    ETag: str


class GetRealtimeLogConfigResultTypeDef(TypedDict, total=False):
    RealtimeLogConfig: "RealtimeLogConfigTypeDef"


class GetStreamingDistributionConfigResultTypeDef(TypedDict, total=False):
    StreamingDistributionConfig: "StreamingDistributionConfigTypeDef"
    ETag: str


class GetStreamingDistributionResultTypeDef(TypedDict, total=False):
    StreamingDistribution: "StreamingDistributionTypeDef"
    ETag: str


class _RequiredHeadersTypeDef(TypedDict):
    Quantity: int


class HeadersTypeDef(_RequiredHeadersTypeDef, total=False):
    Items: List[str]


class InvalidationBatchTypeDef(TypedDict):
    Paths: "PathsTypeDef"
    CallerReference: str


class _RequiredInvalidationListTypeDef(TypedDict):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int


class InvalidationListTypeDef(_RequiredInvalidationListTypeDef, total=False):
    NextMarker: str
    Items: List["InvalidationSummaryTypeDef"]


class InvalidationSummaryTypeDef(TypedDict):
    Id: str
    CreateTime: datetime
    Status: str


class InvalidationTypeDef(TypedDict):
    Id: str
    Status: str
    CreateTime: datetime
    InvalidationBatch: "InvalidationBatchTypeDef"


class KGKeyPairIdsTypeDef(TypedDict, total=False):
    KeyGroupId: str
    KeyPairIds: "KeyPairIdsTypeDef"


class _RequiredKeyGroupConfigTypeDef(TypedDict):
    Name: str
    Items: List[str]


class KeyGroupConfigTypeDef(_RequiredKeyGroupConfigTypeDef, total=False):
    Comment: str


class _RequiredKeyGroupListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int


class KeyGroupListTypeDef(_RequiredKeyGroupListTypeDef, total=False):
    NextMarker: str
    Items: List["KeyGroupSummaryTypeDef"]


class KeyGroupSummaryTypeDef(TypedDict):
    KeyGroup: "KeyGroupTypeDef"


class KeyGroupTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime
    KeyGroupConfig: "KeyGroupConfigTypeDef"


class _RequiredKeyPairIdsTypeDef(TypedDict):
    Quantity: int


class KeyPairIdsTypeDef(_RequiredKeyPairIdsTypeDef, total=False):
    Items: List[str]


class KinesisStreamConfigTypeDef(TypedDict):
    RoleARN: str
    StreamARN: str


class _RequiredLambdaFunctionAssociationTypeDef(TypedDict):
    LambdaFunctionARN: str
    EventType: EventType


class LambdaFunctionAssociationTypeDef(_RequiredLambdaFunctionAssociationTypeDef, total=False):
    IncludeBody: bool


class _RequiredLambdaFunctionAssociationsTypeDef(TypedDict):
    Quantity: int


class LambdaFunctionAssociationsTypeDef(_RequiredLambdaFunctionAssociationsTypeDef, total=False):
    Items: List["LambdaFunctionAssociationTypeDef"]


class ListCachePoliciesResultTypeDef(TypedDict, total=False):
    CachePolicyList: "CachePolicyListTypeDef"


class ListCloudFrontOriginAccessIdentitiesResultTypeDef(TypedDict, total=False):
    CloudFrontOriginAccessIdentityList: "CloudFrontOriginAccessIdentityListTypeDef"


class ListDistributionsByCachePolicyIdResultTypeDef(TypedDict, total=False):
    DistributionIdList: "DistributionIdListTypeDef"


class ListDistributionsByKeyGroupResultTypeDef(TypedDict, total=False):
    DistributionIdList: "DistributionIdListTypeDef"


class ListDistributionsByOriginRequestPolicyIdResultTypeDef(TypedDict, total=False):
    DistributionIdList: "DistributionIdListTypeDef"


class ListDistributionsByRealtimeLogConfigResultTypeDef(TypedDict, total=False):
    DistributionList: "DistributionListTypeDef"


class ListDistributionsByWebACLIdResultTypeDef(TypedDict, total=False):
    DistributionList: "DistributionListTypeDef"


class ListDistributionsResultTypeDef(TypedDict, total=False):
    DistributionList: "DistributionListTypeDef"


class ListFieldLevelEncryptionConfigsResultTypeDef(TypedDict, total=False):
    FieldLevelEncryptionList: "FieldLevelEncryptionListTypeDef"


class ListFieldLevelEncryptionProfilesResultTypeDef(TypedDict, total=False):
    FieldLevelEncryptionProfileList: "FieldLevelEncryptionProfileListTypeDef"


class ListFunctionsResultTypeDef(TypedDict, total=False):
    FunctionList: "FunctionListTypeDef"


class ListInvalidationsResultTypeDef(TypedDict, total=False):
    InvalidationList: "InvalidationListTypeDef"


class ListKeyGroupsResultTypeDef(TypedDict, total=False):
    KeyGroupList: "KeyGroupListTypeDef"


class ListOriginRequestPoliciesResultTypeDef(TypedDict, total=False):
    OriginRequestPolicyList: "OriginRequestPolicyListTypeDef"


class ListPublicKeysResultTypeDef(TypedDict, total=False):
    PublicKeyList: "PublicKeyListTypeDef"


class ListRealtimeLogConfigsResultTypeDef(TypedDict, total=False):
    RealtimeLogConfigs: "RealtimeLogConfigsTypeDef"


class ListStreamingDistributionsResultTypeDef(TypedDict, total=False):
    StreamingDistributionList: "StreamingDistributionListTypeDef"


class ListTagsForResourceResultTypeDef(TypedDict):
    Tags: "TagsTypeDef"


class LoggingConfigTypeDef(TypedDict):
    Enabled: bool
    IncludeCookies: bool
    Bucket: str
    Prefix: str


class MonitoringSubscriptionTypeDef(TypedDict, total=False):
    RealtimeMetricsSubscriptionConfig: "RealtimeMetricsSubscriptionConfigTypeDef"


class OriginCustomHeaderTypeDef(TypedDict):
    HeaderName: str
    HeaderValue: str


class OriginGroupFailoverCriteriaTypeDef(TypedDict):
    StatusCodes: "StatusCodesTypeDef"


class OriginGroupMemberTypeDef(TypedDict):
    OriginId: str


class OriginGroupMembersTypeDef(TypedDict):
    Quantity: int
    Items: List["OriginGroupMemberTypeDef"]


class OriginGroupTypeDef(TypedDict):
    Id: str
    FailoverCriteria: "OriginGroupFailoverCriteriaTypeDef"
    Members: "OriginGroupMembersTypeDef"


class _RequiredOriginGroupsTypeDef(TypedDict):
    Quantity: int


class OriginGroupsTypeDef(_RequiredOriginGroupsTypeDef, total=False):
    Items: List["OriginGroupTypeDef"]


class _RequiredOriginRequestPolicyConfigTypeDef(TypedDict):
    Name: str
    HeadersConfig: "OriginRequestPolicyHeadersConfigTypeDef"
    CookiesConfig: "OriginRequestPolicyCookiesConfigTypeDef"
    QueryStringsConfig: "OriginRequestPolicyQueryStringsConfigTypeDef"


class OriginRequestPolicyConfigTypeDef(_RequiredOriginRequestPolicyConfigTypeDef, total=False):
    Comment: str


class _RequiredOriginRequestPolicyCookiesConfigTypeDef(TypedDict):
    CookieBehavior: OriginRequestPolicyCookieBehavior


class OriginRequestPolicyCookiesConfigTypeDef(
    _RequiredOriginRequestPolicyCookiesConfigTypeDef, total=False
):
    Cookies: "CookieNamesTypeDef"


class _RequiredOriginRequestPolicyHeadersConfigTypeDef(TypedDict):
    HeaderBehavior: OriginRequestPolicyHeaderBehavior


class OriginRequestPolicyHeadersConfigTypeDef(
    _RequiredOriginRequestPolicyHeadersConfigTypeDef, total=False
):
    Headers: "HeadersTypeDef"


class _RequiredOriginRequestPolicyListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int


class OriginRequestPolicyListTypeDef(_RequiredOriginRequestPolicyListTypeDef, total=False):
    NextMarker: str
    Items: List["OriginRequestPolicySummaryTypeDef"]


class _RequiredOriginRequestPolicyQueryStringsConfigTypeDef(TypedDict):
    QueryStringBehavior: OriginRequestPolicyQueryStringBehavior


class OriginRequestPolicyQueryStringsConfigTypeDef(
    _RequiredOriginRequestPolicyQueryStringsConfigTypeDef, total=False
):
    QueryStrings: "QueryStringNamesTypeDef"


OriginRequestPolicySummaryTypeDef = TypedDict(
    "OriginRequestPolicySummaryTypeDef",
    {"Type": OriginRequestPolicyType, "OriginRequestPolicy": "OriginRequestPolicyTypeDef"},
)


class OriginRequestPolicyTypeDef(TypedDict):
    Id: str
    LastModifiedTime: datetime
    OriginRequestPolicyConfig: "OriginRequestPolicyConfigTypeDef"


class _RequiredOriginShieldTypeDef(TypedDict):
    Enabled: bool


class OriginShieldTypeDef(_RequiredOriginShieldTypeDef, total=False):
    OriginShieldRegion: str


class OriginSslProtocolsTypeDef(TypedDict):
    Quantity: int
    Items: List[SslProtocol]


class _RequiredOriginTypeDef(TypedDict):
    Id: str
    DomainName: str


class OriginTypeDef(_RequiredOriginTypeDef, total=False):
    OriginPath: str
    CustomHeaders: "CustomHeadersTypeDef"
    S3OriginConfig: "S3OriginConfigTypeDef"
    CustomOriginConfig: "CustomOriginConfigTypeDef"
    ConnectionAttempts: int
    ConnectionTimeout: int
    OriginShield: "OriginShieldTypeDef"


class OriginsTypeDef(TypedDict):
    Quantity: int
    Items: List["OriginTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredParametersInCacheKeyAndForwardedToOriginTypeDef(TypedDict):
    EnableAcceptEncodingGzip: bool
    HeadersConfig: "CachePolicyHeadersConfigTypeDef"
    CookiesConfig: "CachePolicyCookiesConfigTypeDef"
    QueryStringsConfig: "CachePolicyQueryStringsConfigTypeDef"


class ParametersInCacheKeyAndForwardedToOriginTypeDef(
    _RequiredParametersInCacheKeyAndForwardedToOriginTypeDef, total=False
):
    EnableAcceptEncodingBrotli: bool


class _RequiredPathsTypeDef(TypedDict):
    Quantity: int


class PathsTypeDef(_RequiredPathsTypeDef, total=False):
    Items: List[str]


class _RequiredPublicKeyConfigTypeDef(TypedDict):
    CallerReference: str
    Name: str
    EncodedKey: str


class PublicKeyConfigTypeDef(_RequiredPublicKeyConfigTypeDef, total=False):
    Comment: str


class _RequiredPublicKeyListTypeDef(TypedDict):
    MaxItems: int
    Quantity: int


class PublicKeyListTypeDef(_RequiredPublicKeyListTypeDef, total=False):
    NextMarker: str
    Items: List["PublicKeySummaryTypeDef"]


class _RequiredPublicKeySummaryTypeDef(TypedDict):
    Id: str
    Name: str
    CreatedTime: datetime
    EncodedKey: str


class PublicKeySummaryTypeDef(_RequiredPublicKeySummaryTypeDef, total=False):
    Comment: str


class PublicKeyTypeDef(TypedDict):
    Id: str
    CreatedTime: datetime
    PublicKeyConfig: "PublicKeyConfigTypeDef"


class PublishFunctionResultTypeDef(TypedDict, total=False):
    FunctionSummary: "FunctionSummaryTypeDef"


class _RequiredQueryArgProfileConfigTypeDef(TypedDict):
    ForwardWhenQueryArgProfileIsUnknown: bool


class QueryArgProfileConfigTypeDef(_RequiredQueryArgProfileConfigTypeDef, total=False):
    QueryArgProfiles: "QueryArgProfilesTypeDef"


class QueryArgProfileTypeDef(TypedDict):
    QueryArg: str
    ProfileId: str


class _RequiredQueryArgProfilesTypeDef(TypedDict):
    Quantity: int


class QueryArgProfilesTypeDef(_RequiredQueryArgProfilesTypeDef, total=False):
    Items: List["QueryArgProfileTypeDef"]


class _RequiredQueryStringCacheKeysTypeDef(TypedDict):
    Quantity: int


class QueryStringCacheKeysTypeDef(_RequiredQueryStringCacheKeysTypeDef, total=False):
    Items: List[str]


class _RequiredQueryStringNamesTypeDef(TypedDict):
    Quantity: int


class QueryStringNamesTypeDef(_RequiredQueryStringNamesTypeDef, total=False):
    Items: List[str]


class RealtimeLogConfigTypeDef(TypedDict):
    ARN: str
    Name: str
    SamplingRate: int
    EndPoints: List["EndPointTypeDef"]
    Fields: List[str]


class _RequiredRealtimeLogConfigsTypeDef(TypedDict):
    MaxItems: int
    IsTruncated: bool
    Marker: str


class RealtimeLogConfigsTypeDef(_RequiredRealtimeLogConfigsTypeDef, total=False):
    Items: List["RealtimeLogConfigTypeDef"]
    NextMarker: str


class RealtimeMetricsSubscriptionConfigTypeDef(TypedDict):
    RealtimeMetricsSubscriptionStatus: RealtimeMetricsSubscriptionStatus


class RestrictionsTypeDef(TypedDict):
    GeoRestriction: "GeoRestrictionTypeDef"


class S3OriginConfigTypeDef(TypedDict):
    OriginAccessIdentity: str


class S3OriginTypeDef(TypedDict):
    DomainName: str
    OriginAccessIdentity: str


class SignerTypeDef(TypedDict, total=False):
    AwsAccountNumber: str
    KeyPairIds: "KeyPairIdsTypeDef"


class StatusCodesTypeDef(TypedDict):
    Quantity: int
    Items: List[int]


class _RequiredStreamingDistributionConfigTypeDef(TypedDict):
    CallerReference: str
    S3Origin: "S3OriginTypeDef"
    Comment: str
    TrustedSigners: "TrustedSignersTypeDef"
    Enabled: bool


class StreamingDistributionConfigTypeDef(_RequiredStreamingDistributionConfigTypeDef, total=False):
    Aliases: "AliasesTypeDef"
    Logging: "StreamingLoggingConfigTypeDef"
    PriceClass: PriceClass


class StreamingDistributionConfigWithTagsTypeDef(TypedDict):
    StreamingDistributionConfig: "StreamingDistributionConfigTypeDef"
    Tags: "TagsTypeDef"


class _RequiredStreamingDistributionListTypeDef(TypedDict):
    Marker: str
    MaxItems: int
    IsTruncated: bool
    Quantity: int


class StreamingDistributionListTypeDef(_RequiredStreamingDistributionListTypeDef, total=False):
    NextMarker: str
    Items: List["StreamingDistributionSummaryTypeDef"]


class StreamingDistributionSummaryTypeDef(TypedDict):
    Id: str
    ARN: str
    Status: str
    LastModifiedTime: datetime
    DomainName: str
    S3Origin: "S3OriginTypeDef"
    Aliases: "AliasesTypeDef"
    TrustedSigners: "TrustedSignersTypeDef"
    Comment: str
    PriceClass: PriceClass
    Enabled: bool


class _RequiredStreamingDistributionTypeDef(TypedDict):
    Id: str
    ARN: str
    Status: str
    DomainName: str
    ActiveTrustedSigners: "ActiveTrustedSignersTypeDef"
    StreamingDistributionConfig: "StreamingDistributionConfigTypeDef"


class StreamingDistributionTypeDef(_RequiredStreamingDistributionTypeDef, total=False):
    LastModifiedTime: datetime


class StreamingLoggingConfigTypeDef(TypedDict):
    Enabled: bool
    Bucket: str
    Prefix: str


class TagKeysTypeDef(TypedDict, total=False):
    Items: List[str]


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    Value: str


class TagsTypeDef(TypedDict, total=False):
    Items: List["TagTypeDef"]


class TestFunctionResultTypeDef(TypedDict, total=False):
    TestResult: "TestResultTypeDef"


class TestResultTypeDef(TypedDict, total=False):
    FunctionSummary: "FunctionSummaryTypeDef"
    ComputeUtilization: str
    FunctionExecutionLogs: List[str]
    FunctionErrorMessage: str
    FunctionOutput: str


class _RequiredTrustedKeyGroupsTypeDef(TypedDict):
    Enabled: bool
    Quantity: int


class TrustedKeyGroupsTypeDef(_RequiredTrustedKeyGroupsTypeDef, total=False):
    Items: List[str]


class _RequiredTrustedSignersTypeDef(TypedDict):
    Enabled: bool
    Quantity: int


class TrustedSignersTypeDef(_RequiredTrustedSignersTypeDef, total=False):
    Items: List[str]


class UpdateCachePolicyResultTypeDef(TypedDict, total=False):
    CachePolicy: "CachePolicyTypeDef"
    ETag: str


class UpdateCloudFrontOriginAccessIdentityResultTypeDef(TypedDict, total=False):
    CloudFrontOriginAccessIdentity: "CloudFrontOriginAccessIdentityTypeDef"
    ETag: str


class UpdateDistributionResultTypeDef(TypedDict, total=False):
    Distribution: "DistributionTypeDef"
    ETag: str


class UpdateFieldLevelEncryptionConfigResultTypeDef(TypedDict, total=False):
    FieldLevelEncryption: "FieldLevelEncryptionTypeDef"
    ETag: str


class UpdateFieldLevelEncryptionProfileResultTypeDef(TypedDict, total=False):
    FieldLevelEncryptionProfile: "FieldLevelEncryptionProfileTypeDef"
    ETag: str


class UpdateFunctionResultTypeDef(TypedDict, total=False):
    FunctionSummary: "FunctionSummaryTypeDef"
    ETag: str


class UpdateKeyGroupResultTypeDef(TypedDict, total=False):
    KeyGroup: "KeyGroupTypeDef"
    ETag: str


class UpdateOriginRequestPolicyResultTypeDef(TypedDict, total=False):
    OriginRequestPolicy: "OriginRequestPolicyTypeDef"
    ETag: str


class UpdatePublicKeyResultTypeDef(TypedDict, total=False):
    PublicKey: "PublicKeyTypeDef"
    ETag: str


class UpdateRealtimeLogConfigResultTypeDef(TypedDict, total=False):
    RealtimeLogConfig: "RealtimeLogConfigTypeDef"


class UpdateStreamingDistributionResultTypeDef(TypedDict, total=False):
    StreamingDistribution: "StreamingDistributionTypeDef"
    ETag: str


class ViewerCertificateTypeDef(TypedDict, total=False):
    CloudFrontDefaultCertificate: bool
    IAMCertificateId: str
    ACMCertificateArn: str
    SSLSupportMethod: SSLSupportMethod
    MinimumProtocolVersion: MinimumProtocolVersion
    Certificate: str
    CertificateSource: CertificateSource


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
