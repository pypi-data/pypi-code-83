"""
Type annotations for cloudfront service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudfront/literals.html)

Usage::

    ```python
    from mypy_boto3_cloudfront.literals import CachePolicyCookieBehavior

    data: CachePolicyCookieBehavior = "all"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CachePolicyCookieBehavior",
    "CachePolicyHeaderBehavior",
    "CachePolicyQueryStringBehavior",
    "CachePolicyType",
    "CertificateSource",
    "DistributionDeployedWaiterName",
    "EventType",
    "Format",
    "FunctionRuntime",
    "FunctionStage",
    "GeoRestrictionType",
    "HttpVersion",
    "ICPRecordalStatus",
    "InvalidationCompletedWaiterName",
    "ItemSelection",
    "ListCloudFrontOriginAccessIdentitiesPaginatorName",
    "ListDistributionsPaginatorName",
    "ListInvalidationsPaginatorName",
    "ListStreamingDistributionsPaginatorName",
    "Method",
    "MinimumProtocolVersion",
    "OriginProtocolPolicy",
    "OriginRequestPolicyCookieBehavior",
    "OriginRequestPolicyHeaderBehavior",
    "OriginRequestPolicyQueryStringBehavior",
    "OriginRequestPolicyType",
    "PriceClass",
    "RealtimeMetricsSubscriptionStatus",
    "SSLSupportMethod",
    "SslProtocol",
    "StreamingDistributionDeployedWaiterName",
    "ViewerProtocolPolicy",
)


CachePolicyCookieBehavior = Literal["all", "allExcept", "none", "whitelist"]
CachePolicyHeaderBehavior = Literal["none", "whitelist"]
CachePolicyQueryStringBehavior = Literal["all", "allExcept", "none", "whitelist"]
CachePolicyType = Literal["custom", "managed"]
CertificateSource = Literal["acm", "cloudfront", "iam"]
DistributionDeployedWaiterName = Literal["distribution_deployed"]
EventType = Literal["origin-request", "origin-response", "viewer-request", "viewer-response"]
Format = Literal["URLEncoded"]
FunctionRuntime = Literal["cloudfront-js-1.0"]
FunctionStage = Literal["DEVELOPMENT", "LIVE"]
GeoRestrictionType = Literal["blacklist", "none", "whitelist"]
HttpVersion = Literal["http1.1", "http2"]
ICPRecordalStatus = Literal["APPROVED", "PENDING", "SUSPENDED"]
InvalidationCompletedWaiterName = Literal["invalidation_completed"]
ItemSelection = Literal["all", "none", "whitelist"]
ListCloudFrontOriginAccessIdentitiesPaginatorName = Literal[
    "list_cloud_front_origin_access_identities"
]
ListDistributionsPaginatorName = Literal["list_distributions"]
ListInvalidationsPaginatorName = Literal["list_invalidations"]
ListStreamingDistributionsPaginatorName = Literal["list_streaming_distributions"]
Method = Literal["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"]
MinimumProtocolVersion = Literal[
    "SSLv3", "TLSv1", "TLSv1.1_2016", "TLSv1.2_2018", "TLSv1.2_2019", "TLSv1_2016"
]
OriginProtocolPolicy = Literal["http-only", "https-only", "match-viewer"]
OriginRequestPolicyCookieBehavior = Literal["all", "none", "whitelist"]
OriginRequestPolicyHeaderBehavior = Literal[
    "allViewer", "allViewerAndWhitelistCloudFront", "none", "whitelist"
]
OriginRequestPolicyQueryStringBehavior = Literal["all", "none", "whitelist"]
OriginRequestPolicyType = Literal["custom", "managed"]
PriceClass = Literal["PriceClass_100", "PriceClass_200", "PriceClass_All"]
RealtimeMetricsSubscriptionStatus = Literal["Disabled", "Enabled"]
SSLSupportMethod = Literal["sni-only", "static-ip", "vip"]
SslProtocol = Literal["SSLv3", "TLSv1", "TLSv1.1", "TLSv1.2"]
StreamingDistributionDeployedWaiterName = Literal["streaming_distribution_deployed"]
ViewerProtocolPolicy = Literal["allow-all", "https-only", "redirect-to-https"]
