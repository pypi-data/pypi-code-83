"""
Type annotations for shield service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_shield/literals.html)

Usage::

    ```python
    from mypy_boto3_shield.literals import AttackLayer

    data: AttackLayer = "APPLICATION"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AttackLayer",
    "AttackPropertyIdentifier",
    "AutoRenew",
    "ListAttacksPaginatorName",
    "ListProtectionsPaginatorName",
    "ProactiveEngagementStatus",
    "ProtectedResourceType",
    "ProtectionGroupAggregation",
    "ProtectionGroupPattern",
    "SubResourceType",
    "SubscriptionState",
    "Unit",
)


AttackLayer = Literal["APPLICATION", "NETWORK"]
AttackPropertyIdentifier = Literal[
    "DESTINATION_URL",
    "REFERRER",
    "SOURCE_ASN",
    "SOURCE_COUNTRY",
    "SOURCE_IP_ADDRESS",
    "SOURCE_USER_AGENT",
    "WORDPRESS_PINGBACK_REFLECTOR",
    "WORDPRESS_PINGBACK_SOURCE",
]
AutoRenew = Literal["DISABLED", "ENABLED"]
ListAttacksPaginatorName = Literal["list_attacks"]
ListProtectionsPaginatorName = Literal["list_protections"]
ProactiveEngagementStatus = Literal["DISABLED", "ENABLED", "PENDING"]
ProtectedResourceType = Literal[
    "APPLICATION_LOAD_BALANCER",
    "CLASSIC_LOAD_BALANCER",
    "CLOUDFRONT_DISTRIBUTION",
    "ELASTIC_IP_ALLOCATION",
    "GLOBAL_ACCELERATOR",
    "ROUTE_53_HOSTED_ZONE",
]
ProtectionGroupAggregation = Literal["MAX", "MEAN", "SUM"]
ProtectionGroupPattern = Literal["ALL", "ARBITRARY", "BY_RESOURCE_TYPE"]
SubResourceType = Literal["IP", "URL"]
SubscriptionState = Literal["ACTIVE", "INACTIVE"]
Unit = Literal["BITS", "BYTES", "PACKETS", "REQUESTS"]
