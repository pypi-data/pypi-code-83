"""
Type annotations for elbv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elbv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elbv2.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_elbv2.literals import (
    ActionTypeEnum,
    AuthenticateCognitoActionConditionalBehaviorEnum,
    AuthenticateOidcActionConditionalBehaviorEnum,
    IpAddressType,
    LoadBalancerSchemeEnum,
    LoadBalancerStateEnum,
    LoadBalancerTypeEnum,
    ProtocolEnum,
    RedirectActionStatusCodeEnum,
    TargetHealthReasonEnum,
    TargetHealthStateEnum,
    TargetTypeEnum,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionTypeDef",
    "AddListenerCertificatesOutputTypeDef",
    "AuthenticateCognitoActionConfigTypeDef",
    "AuthenticateOidcActionConfigTypeDef",
    "AvailabilityZoneTypeDef",
    "CertificateTypeDef",
    "CipherTypeDef",
    "CreateListenerOutputTypeDef",
    "CreateLoadBalancerOutputTypeDef",
    "CreateRuleOutputTypeDef",
    "CreateTargetGroupOutputTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeListenerCertificatesOutputTypeDef",
    "DescribeListenersOutputTypeDef",
    "DescribeLoadBalancerAttributesOutputTypeDef",
    "DescribeLoadBalancersOutputTypeDef",
    "DescribeRulesOutputTypeDef",
    "DescribeSSLPoliciesOutputTypeDef",
    "DescribeTagsOutputTypeDef",
    "DescribeTargetGroupAttributesOutputTypeDef",
    "DescribeTargetGroupsOutputTypeDef",
    "DescribeTargetHealthOutputTypeDef",
    "FixedResponseActionConfigTypeDef",
    "ForwardActionConfigTypeDef",
    "HostHeaderConditionConfigTypeDef",
    "HttpHeaderConditionConfigTypeDef",
    "HttpRequestMethodConditionConfigTypeDef",
    "LimitTypeDef",
    "ListenerTypeDef",
    "LoadBalancerAddressTypeDef",
    "LoadBalancerAttributeTypeDef",
    "LoadBalancerStateTypeDef",
    "LoadBalancerTypeDef",
    "MatcherTypeDef",
    "ModifyListenerOutputTypeDef",
    "ModifyLoadBalancerAttributesOutputTypeDef",
    "ModifyRuleOutputTypeDef",
    "ModifyTargetGroupAttributesOutputTypeDef",
    "ModifyTargetGroupOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PathPatternConditionConfigTypeDef",
    "QueryStringConditionConfigTypeDef",
    "QueryStringKeyValuePairTypeDef",
    "RedirectActionConfigTypeDef",
    "ResponseMetadata",
    "RuleConditionTypeDef",
    "RulePriorityPairTypeDef",
    "RuleTypeDef",
    "SetIpAddressTypeOutputTypeDef",
    "SetRulePrioritiesOutputTypeDef",
    "SetSecurityGroupsOutputTypeDef",
    "SetSubnetsOutputTypeDef",
    "SourceIpConditionConfigTypeDef",
    "SslPolicyTypeDef",
    "SubnetMappingTypeDef",
    "TagDescriptionTypeDef",
    "TagTypeDef",
    "TargetDescriptionTypeDef",
    "TargetGroupAttributeTypeDef",
    "TargetGroupStickinessConfigTypeDef",
    "TargetGroupTupleTypeDef",
    "TargetGroupTypeDef",
    "TargetHealthDescriptionTypeDef",
    "TargetHealthTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredActionTypeDef = TypedDict("_RequiredActionTypeDef", {"Type": ActionTypeEnum})
_OptionalActionTypeDef = TypedDict(
    "_OptionalActionTypeDef",
    {
        "TargetGroupArn": str,
        "AuthenticateOidcConfig": "AuthenticateOidcActionConfigTypeDef",
        "AuthenticateCognitoConfig": "AuthenticateCognitoActionConfigTypeDef",
        "Order": int,
        "RedirectConfig": "RedirectActionConfigTypeDef",
        "FixedResponseConfig": "FixedResponseActionConfigTypeDef",
        "ForwardConfig": "ForwardActionConfigTypeDef",
    },
    total=False,
)


class ActionTypeDef(_RequiredActionTypeDef, _OptionalActionTypeDef):
    pass


class AddListenerCertificatesOutputTypeDef(TypedDict):
    Certificates: List["CertificateTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class _RequiredAuthenticateCognitoActionConfigTypeDef(TypedDict):
    UserPoolArn: str
    UserPoolClientId: str
    UserPoolDomain: str


class AuthenticateCognitoActionConfigTypeDef(
    _RequiredAuthenticateCognitoActionConfigTypeDef, total=False
):
    SessionCookieName: str
    Scope: str
    SessionTimeout: int
    AuthenticationRequestExtraParams: Dict[str, str]
    OnUnauthenticatedRequest: AuthenticateCognitoActionConditionalBehaviorEnum


class _RequiredAuthenticateOidcActionConfigTypeDef(TypedDict):
    Issuer: str
    AuthorizationEndpoint: str
    TokenEndpoint: str
    UserInfoEndpoint: str
    ClientId: str


class AuthenticateOidcActionConfigTypeDef(
    _RequiredAuthenticateOidcActionConfigTypeDef, total=False
):
    ClientSecret: str
    SessionCookieName: str
    Scope: str
    SessionTimeout: int
    AuthenticationRequestExtraParams: Dict[str, str]
    OnUnauthenticatedRequest: AuthenticateOidcActionConditionalBehaviorEnum
    UseExistingClientSecret: bool


class AvailabilityZoneTypeDef(TypedDict, total=False):
    ZoneName: str
    SubnetId: str
    OutpostId: str
    LoadBalancerAddresses: List["LoadBalancerAddressTypeDef"]


class CertificateTypeDef(TypedDict, total=False):
    CertificateArn: str
    IsDefault: bool


class CipherTypeDef(TypedDict, total=False):
    Name: str
    Priority: int


class CreateListenerOutputTypeDef(TypedDict):
    Listeners: List["ListenerTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class CreateLoadBalancerOutputTypeDef(TypedDict):
    LoadBalancers: List["LoadBalancerTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class CreateRuleOutputTypeDef(TypedDict):
    Rules: List["RuleTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class CreateTargetGroupOutputTypeDef(TypedDict):
    TargetGroups: List["TargetGroupTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeAccountLimitsOutputTypeDef(TypedDict):
    Limits: List["LimitTypeDef"]
    NextMarker: str
    ResponseMetadata: "ResponseMetadata"


class DescribeListenerCertificatesOutputTypeDef(TypedDict):
    Certificates: List["CertificateTypeDef"]
    NextMarker: str
    ResponseMetadata: "ResponseMetadata"


class DescribeListenersOutputTypeDef(TypedDict):
    Listeners: List["ListenerTypeDef"]
    NextMarker: str
    ResponseMetadata: "ResponseMetadata"


class DescribeLoadBalancerAttributesOutputTypeDef(TypedDict):
    Attributes: List["LoadBalancerAttributeTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeLoadBalancersOutputTypeDef(TypedDict):
    LoadBalancers: List["LoadBalancerTypeDef"]
    NextMarker: str
    ResponseMetadata: "ResponseMetadata"


class DescribeRulesOutputTypeDef(TypedDict):
    Rules: List["RuleTypeDef"]
    NextMarker: str
    ResponseMetadata: "ResponseMetadata"


class DescribeSSLPoliciesOutputTypeDef(TypedDict):
    SslPolicies: List["SslPolicyTypeDef"]
    NextMarker: str
    ResponseMetadata: "ResponseMetadata"


class DescribeTagsOutputTypeDef(TypedDict):
    TagDescriptions: List["TagDescriptionTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeTargetGroupAttributesOutputTypeDef(TypedDict):
    Attributes: List["TargetGroupAttributeTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeTargetGroupsOutputTypeDef(TypedDict):
    TargetGroups: List["TargetGroupTypeDef"]
    NextMarker: str
    ResponseMetadata: "ResponseMetadata"


class DescribeTargetHealthOutputTypeDef(TypedDict):
    TargetHealthDescriptions: List["TargetHealthDescriptionTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class _RequiredFixedResponseActionConfigTypeDef(TypedDict):
    StatusCode: str


class FixedResponseActionConfigTypeDef(_RequiredFixedResponseActionConfigTypeDef, total=False):
    MessageBody: str
    ContentType: str


class ForwardActionConfigTypeDef(TypedDict, total=False):
    TargetGroups: List["TargetGroupTupleTypeDef"]
    TargetGroupStickinessConfig: "TargetGroupStickinessConfigTypeDef"


class HostHeaderConditionConfigTypeDef(TypedDict, total=False):
    Values: List[str]


class HttpHeaderConditionConfigTypeDef(TypedDict, total=False):
    HttpHeaderName: str
    Values: List[str]


class HttpRequestMethodConditionConfigTypeDef(TypedDict, total=False):
    Values: List[str]


class LimitTypeDef(TypedDict, total=False):
    Name: str
    Max: str


ListenerTypeDef = TypedDict(
    "ListenerTypeDef",
    {
        "ListenerArn": str,
        "LoadBalancerArn": str,
        "Port": int,
        "Protocol": ProtocolEnum,
        "Certificates": List["CertificateTypeDef"],
        "SslPolicy": str,
        "DefaultActions": List["ActionTypeDef"],
        "AlpnPolicy": List[str],
    },
    total=False,
)


class LoadBalancerAddressTypeDef(TypedDict, total=False):
    IpAddress: str
    AllocationId: str
    PrivateIPv4Address: str
    IPv6Address: str


class LoadBalancerAttributeTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class LoadBalancerStateTypeDef(TypedDict, total=False):
    Code: LoadBalancerStateEnum
    Reason: str


LoadBalancerTypeDef = TypedDict(
    "LoadBalancerTypeDef",
    {
        "LoadBalancerArn": str,
        "DNSName": str,
        "CanonicalHostedZoneId": str,
        "CreatedTime": datetime,
        "LoadBalancerName": str,
        "Scheme": LoadBalancerSchemeEnum,
        "VpcId": str,
        "State": "LoadBalancerStateTypeDef",
        "Type": LoadBalancerTypeEnum,
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "SecurityGroups": List[str],
        "IpAddressType": IpAddressType,
        "CustomerOwnedIpv4Pool": str,
    },
    total=False,
)


class MatcherTypeDef(TypedDict, total=False):
    HttpCode: str
    GrpcCode: str


class ModifyListenerOutputTypeDef(TypedDict):
    Listeners: List["ListenerTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ModifyLoadBalancerAttributesOutputTypeDef(TypedDict):
    Attributes: List["LoadBalancerAttributeTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ModifyRuleOutputTypeDef(TypedDict):
    Rules: List["RuleTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ModifyTargetGroupAttributesOutputTypeDef(TypedDict):
    Attributes: List["TargetGroupAttributeTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ModifyTargetGroupOutputTypeDef(TypedDict):
    TargetGroups: List["TargetGroupTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PathPatternConditionConfigTypeDef(TypedDict, total=False):
    Values: List[str]


class QueryStringConditionConfigTypeDef(TypedDict, total=False):
    Values: List["QueryStringKeyValuePairTypeDef"]


class QueryStringKeyValuePairTypeDef(TypedDict, total=False):
    Key: str
    Value: str


_RequiredRedirectActionConfigTypeDef = TypedDict(
    "_RequiredRedirectActionConfigTypeDef", {"StatusCode": RedirectActionStatusCodeEnum}
)
_OptionalRedirectActionConfigTypeDef = TypedDict(
    "_OptionalRedirectActionConfigTypeDef",
    {"Protocol": str, "Port": str, "Host": str, "Path": str, "Query": str},
    total=False,
)


class RedirectActionConfigTypeDef(
    _RequiredRedirectActionConfigTypeDef, _OptionalRedirectActionConfigTypeDef
):
    pass


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RuleConditionTypeDef(TypedDict, total=False):
    Field: str
    Values: List[str]
    HostHeaderConfig: "HostHeaderConditionConfigTypeDef"
    PathPatternConfig: "PathPatternConditionConfigTypeDef"
    HttpHeaderConfig: "HttpHeaderConditionConfigTypeDef"
    QueryStringConfig: "QueryStringConditionConfigTypeDef"
    HttpRequestMethodConfig: "HttpRequestMethodConditionConfigTypeDef"
    SourceIpConfig: "SourceIpConditionConfigTypeDef"


class RulePriorityPairTypeDef(TypedDict, total=False):
    RuleArn: str
    Priority: int


class RuleTypeDef(TypedDict, total=False):
    RuleArn: str
    Priority: str
    Conditions: List["RuleConditionTypeDef"]
    Actions: List["ActionTypeDef"]
    IsDefault: bool


class SetIpAddressTypeOutputTypeDef(TypedDict):
    IpAddressType: IpAddressType
    ResponseMetadata: "ResponseMetadata"


class SetRulePrioritiesOutputTypeDef(TypedDict):
    Rules: List["RuleTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class SetSecurityGroupsOutputTypeDef(TypedDict):
    SecurityGroupIds: List[str]
    ResponseMetadata: "ResponseMetadata"


class SetSubnetsOutputTypeDef(TypedDict):
    AvailabilityZones: List["AvailabilityZoneTypeDef"]
    IpAddressType: IpAddressType
    ResponseMetadata: "ResponseMetadata"


class SourceIpConditionConfigTypeDef(TypedDict, total=False):
    Values: List[str]


class SslPolicyTypeDef(TypedDict, total=False):
    SslProtocols: List[str]
    Ciphers: List["CipherTypeDef"]
    Name: str


class SubnetMappingTypeDef(TypedDict, total=False):
    SubnetId: str
    AllocationId: str
    PrivateIPv4Address: str
    IPv6Address: str


class TagDescriptionTypeDef(TypedDict, total=False):
    ResourceArn: str
    Tags: List["TagTypeDef"]


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    Value: str


class _RequiredTargetDescriptionTypeDef(TypedDict):
    Id: str


class TargetDescriptionTypeDef(_RequiredTargetDescriptionTypeDef, total=False):
    Port: int
    AvailabilityZone: str


class TargetGroupAttributeTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class TargetGroupStickinessConfigTypeDef(TypedDict, total=False):
    Enabled: bool
    DurationSeconds: int


class TargetGroupTupleTypeDef(TypedDict, total=False):
    TargetGroupArn: str
    Weight: int


TargetGroupTypeDef = TypedDict(
    "TargetGroupTypeDef",
    {
        "TargetGroupArn": str,
        "TargetGroupName": str,
        "Protocol": ProtocolEnum,
        "Port": int,
        "VpcId": str,
        "HealthCheckProtocol": ProtocolEnum,
        "HealthCheckPort": str,
        "HealthCheckEnabled": bool,
        "HealthCheckIntervalSeconds": int,
        "HealthCheckTimeoutSeconds": int,
        "HealthyThresholdCount": int,
        "UnhealthyThresholdCount": int,
        "HealthCheckPath": str,
        "Matcher": "MatcherTypeDef",
        "LoadBalancerArns": List[str],
        "TargetType": TargetTypeEnum,
        "ProtocolVersion": str,
    },
    total=False,
)


class TargetHealthDescriptionTypeDef(TypedDict, total=False):
    Target: "TargetDescriptionTypeDef"
    HealthCheckPort: str
    TargetHealth: "TargetHealthTypeDef"


class TargetHealthTypeDef(TypedDict, total=False):
    State: TargetHealthStateEnum
    Reason: TargetHealthReasonEnum
    Description: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
