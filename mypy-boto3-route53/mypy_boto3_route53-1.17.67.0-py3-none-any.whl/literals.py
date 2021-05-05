"""
Type annotations for route53 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/literals.html)

Usage::

    ```python
    from mypy_boto3_route53.literals import AccountLimitType

    data: AccountLimitType = "MAX_HEALTH_CHECKS_BY_OWNER"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccountLimitType",
    "ChangeAction",
    "ChangeStatus",
    "CloudWatchRegion",
    "ComparisonOperator",
    "HealthCheckRegion",
    "HealthCheckType",
    "HostedZoneLimitType",
    "InsufficientDataHealthStatus",
    "ListHealthChecksPaginatorName",
    "ListHostedZonesPaginatorName",
    "ListQueryLoggingConfigsPaginatorName",
    "ListResourceRecordSetsPaginatorName",
    "ListVPCAssociationAuthorizationsPaginatorName",
    "RRType",
    "ResettableElementName",
    "ResourceRecordSetFailover",
    "ResourceRecordSetRegion",
    "ResourceRecordSetsChangedWaiterName",
    "ReusableDelegationSetLimitType",
    "Statistic",
    "TagResourceType",
    "VPCRegion",
)


AccountLimitType = Literal[
    "MAX_HEALTH_CHECKS_BY_OWNER",
    "MAX_HOSTED_ZONES_BY_OWNER",
    "MAX_REUSABLE_DELEGATION_SETS_BY_OWNER",
    "MAX_TRAFFIC_POLICIES_BY_OWNER",
    "MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER",
]
ChangeAction = Literal["CREATE", "DELETE", "UPSERT"]
ChangeStatus = Literal["INSYNC", "PENDING"]
CloudWatchRegion = Literal[
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
    "us-east-1",
    "us-east-2",
    "us-gov-east-1",
    "us-gov-west-1",
    "us-iso-east-1",
    "us-isob-east-1",
    "us-west-1",
    "us-west-2",
]
ComparisonOperator = Literal[
    "GreaterThanOrEqualToThreshold",
    "GreaterThanThreshold",
    "LessThanOrEqualToThreshold",
    "LessThanThreshold",
]
HealthCheckRegion = Literal[
    "ap-northeast-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "eu-west-1",
    "sa-east-1",
    "us-east-1",
    "us-west-1",
    "us-west-2",
]
HealthCheckType = Literal[
    "CALCULATED", "CLOUDWATCH_METRIC", "HTTP", "HTTPS", "HTTPS_STR_MATCH", "HTTP_STR_MATCH", "TCP"
]
HostedZoneLimitType = Literal["MAX_RRSETS_BY_ZONE", "MAX_VPCS_ASSOCIATED_BY_ZONE"]
InsufficientDataHealthStatus = Literal["Healthy", "LastKnownStatus", "Unhealthy"]
ListHealthChecksPaginatorName = Literal["list_health_checks"]
ListHostedZonesPaginatorName = Literal["list_hosted_zones"]
ListQueryLoggingConfigsPaginatorName = Literal["list_query_logging_configs"]
ListResourceRecordSetsPaginatorName = Literal["list_resource_record_sets"]
ListVPCAssociationAuthorizationsPaginatorName = Literal["list_vpc_association_authorizations"]
RRType = Literal[
    "A", "AAAA", "CAA", "CNAME", "DS", "MX", "NAPTR", "NS", "PTR", "SOA", "SPF", "SRV", "TXT"
]
ResettableElementName = Literal[
    "ChildHealthChecks", "FullyQualifiedDomainName", "Regions", "ResourcePath"
]
ResourceRecordSetFailover = Literal["PRIMARY", "SECONDARY"]
ResourceRecordSetRegion = Literal[
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
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
]
ResourceRecordSetsChangedWaiterName = Literal["resource_record_sets_changed"]
ReusableDelegationSetLimitType = Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"]
Statistic = Literal["Average", "Maximum", "Minimum", "SampleCount", "Sum"]
TagResourceType = Literal["healthcheck", "hostedzone"]
VPCRegion = Literal[
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
    "eu-central-1",
    "eu-north-1",
    "eu-south-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "me-south-1",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-gov-east-1",
    "us-gov-west-1",
    "us-iso-east-1",
    "us-isob-east-1",
    "us-west-1",
    "us-west-2",
]
