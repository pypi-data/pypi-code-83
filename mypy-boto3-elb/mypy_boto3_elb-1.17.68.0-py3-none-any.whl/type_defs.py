"""
Type annotations for elb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elb.type_defs import AccessLogTypeDef

    data: AccessLogTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessLogTypeDef",
    "AddAvailabilityZonesOutputTypeDef",
    "AdditionalAttributeTypeDef",
    "AppCookieStickinessPolicyTypeDef",
    "ApplySecurityGroupsToLoadBalancerOutputTypeDef",
    "AttachLoadBalancerToSubnetsOutputTypeDef",
    "BackendServerDescriptionTypeDef",
    "ConfigureHealthCheckOutputTypeDef",
    "ConnectionDrainingTypeDef",
    "ConnectionSettingsTypeDef",
    "CreateAccessPointOutputTypeDef",
    "CrossZoneLoadBalancingTypeDef",
    "DeregisterEndPointsOutputTypeDef",
    "DescribeAccessPointsOutputTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeEndPointStateOutputTypeDef",
    "DescribeLoadBalancerAttributesOutputTypeDef",
    "DescribeLoadBalancerPoliciesOutputTypeDef",
    "DescribeLoadBalancerPolicyTypesOutputTypeDef",
    "DescribeTagsOutputTypeDef",
    "DetachLoadBalancerFromSubnetsOutputTypeDef",
    "HealthCheckTypeDef",
    "InstanceStateTypeDef",
    "InstanceTypeDef",
    "LBCookieStickinessPolicyTypeDef",
    "LimitTypeDef",
    "ListenerDescriptionTypeDef",
    "ListenerTypeDef",
    "LoadBalancerAttributesTypeDef",
    "LoadBalancerDescriptionTypeDef",
    "ModifyLoadBalancerAttributesOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PoliciesTypeDef",
    "PolicyAttributeDescriptionTypeDef",
    "PolicyAttributeTypeDef",
    "PolicyAttributeTypeDescriptionTypeDef",
    "PolicyDescriptionTypeDef",
    "PolicyTypeDescriptionTypeDef",
    "RegisterEndPointsOutputTypeDef",
    "RemoveAvailabilityZonesOutputTypeDef",
    "ResponseMetadata",
    "SourceSecurityGroupTypeDef",
    "TagDescriptionTypeDef",
    "TagKeyOnlyTypeDef",
    "TagTypeDef",
    "WaiterConfigTypeDef",
)


class _RequiredAccessLogTypeDef(TypedDict):
    Enabled: bool


class AccessLogTypeDef(_RequiredAccessLogTypeDef, total=False):
    S3BucketName: str
    EmitInterval: int
    S3BucketPrefix: str


class AddAvailabilityZonesOutputTypeDef(TypedDict):
    AvailabilityZones: List[str]
    ResponseMetadata: "ResponseMetadata"


class AdditionalAttributeTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class AppCookieStickinessPolicyTypeDef(TypedDict, total=False):
    PolicyName: str
    CookieName: str


class ApplySecurityGroupsToLoadBalancerOutputTypeDef(TypedDict):
    SecurityGroups: List[str]
    ResponseMetadata: "ResponseMetadata"


class AttachLoadBalancerToSubnetsOutputTypeDef(TypedDict):
    Subnets: List[str]
    ResponseMetadata: "ResponseMetadata"


class BackendServerDescriptionTypeDef(TypedDict, total=False):
    InstancePort: int
    PolicyNames: List[str]


class ConfigureHealthCheckOutputTypeDef(TypedDict):
    HealthCheck: "HealthCheckTypeDef"
    ResponseMetadata: "ResponseMetadata"


class _RequiredConnectionDrainingTypeDef(TypedDict):
    Enabled: bool


class ConnectionDrainingTypeDef(_RequiredConnectionDrainingTypeDef, total=False):
    Timeout: int


class ConnectionSettingsTypeDef(TypedDict):
    IdleTimeout: int


class CreateAccessPointOutputTypeDef(TypedDict):
    DNSName: str
    ResponseMetadata: "ResponseMetadata"


class CrossZoneLoadBalancingTypeDef(TypedDict):
    Enabled: bool


class DeregisterEndPointsOutputTypeDef(TypedDict):
    Instances: List["InstanceTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeAccessPointsOutputTypeDef(TypedDict):
    LoadBalancerDescriptions: List["LoadBalancerDescriptionTypeDef"]
    NextMarker: str
    ResponseMetadata: "ResponseMetadata"


class DescribeAccountLimitsOutputTypeDef(TypedDict):
    Limits: List["LimitTypeDef"]
    NextMarker: str
    ResponseMetadata: "ResponseMetadata"


class DescribeEndPointStateOutputTypeDef(TypedDict):
    InstanceStates: List["InstanceStateTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeLoadBalancerAttributesOutputTypeDef(TypedDict):
    LoadBalancerAttributes: "LoadBalancerAttributesTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeLoadBalancerPoliciesOutputTypeDef(TypedDict):
    PolicyDescriptions: List["PolicyDescriptionTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeLoadBalancerPolicyTypesOutputTypeDef(TypedDict):
    PolicyTypeDescriptions: List["PolicyTypeDescriptionTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeTagsOutputTypeDef(TypedDict):
    TagDescriptions: List["TagDescriptionTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DetachLoadBalancerFromSubnetsOutputTypeDef(TypedDict):
    Subnets: List[str]
    ResponseMetadata: "ResponseMetadata"


class HealthCheckTypeDef(TypedDict):
    Target: str
    Interval: int
    Timeout: int
    UnhealthyThreshold: int
    HealthyThreshold: int


class InstanceStateTypeDef(TypedDict, total=False):
    InstanceId: str
    State: str
    ReasonCode: str
    Description: str


class InstanceTypeDef(TypedDict, total=False):
    InstanceId: str


class LBCookieStickinessPolicyTypeDef(TypedDict, total=False):
    PolicyName: str
    CookieExpirationPeriod: int


class LimitTypeDef(TypedDict, total=False):
    Name: str
    Max: str


class ListenerDescriptionTypeDef(TypedDict, total=False):
    Listener: "ListenerTypeDef"
    PolicyNames: List[str]


_RequiredListenerTypeDef = TypedDict(
    "_RequiredListenerTypeDef", {"Protocol": str, "LoadBalancerPort": int, "InstancePort": int}
)
_OptionalListenerTypeDef = TypedDict(
    "_OptionalListenerTypeDef", {"InstanceProtocol": str, "SSLCertificateId": str}, total=False
)


class ListenerTypeDef(_RequiredListenerTypeDef, _OptionalListenerTypeDef):
    pass


class LoadBalancerAttributesTypeDef(TypedDict, total=False):
    CrossZoneLoadBalancing: "CrossZoneLoadBalancingTypeDef"
    AccessLog: "AccessLogTypeDef"
    ConnectionDraining: "ConnectionDrainingTypeDef"
    ConnectionSettings: "ConnectionSettingsTypeDef"
    AdditionalAttributes: List["AdditionalAttributeTypeDef"]


class LoadBalancerDescriptionTypeDef(TypedDict, total=False):
    LoadBalancerName: str
    DNSName: str
    CanonicalHostedZoneName: str
    CanonicalHostedZoneNameID: str
    ListenerDescriptions: List["ListenerDescriptionTypeDef"]
    Policies: "PoliciesTypeDef"
    BackendServerDescriptions: List["BackendServerDescriptionTypeDef"]
    AvailabilityZones: List[str]
    Subnets: List[str]
    VPCId: str
    Instances: List["InstanceTypeDef"]
    HealthCheck: "HealthCheckTypeDef"
    SourceSecurityGroup: "SourceSecurityGroupTypeDef"
    SecurityGroups: List[str]
    CreatedTime: datetime
    Scheme: str


class ModifyLoadBalancerAttributesOutputTypeDef(TypedDict):
    LoadBalancerName: str
    LoadBalancerAttributes: "LoadBalancerAttributesTypeDef"
    ResponseMetadata: "ResponseMetadata"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PoliciesTypeDef(TypedDict, total=False):
    AppCookieStickinessPolicies: List["AppCookieStickinessPolicyTypeDef"]
    LBCookieStickinessPolicies: List["LBCookieStickinessPolicyTypeDef"]
    OtherPolicies: List[str]


class PolicyAttributeDescriptionTypeDef(TypedDict, total=False):
    AttributeName: str
    AttributeValue: str


class PolicyAttributeTypeDef(TypedDict, total=False):
    AttributeName: str
    AttributeValue: str


class PolicyAttributeTypeDescriptionTypeDef(TypedDict, total=False):
    AttributeName: str
    AttributeType: str
    Description: str
    DefaultValue: str
    Cardinality: str


class PolicyDescriptionTypeDef(TypedDict, total=False):
    PolicyName: str
    PolicyTypeName: str
    PolicyAttributeDescriptions: List["PolicyAttributeDescriptionTypeDef"]


class PolicyTypeDescriptionTypeDef(TypedDict, total=False):
    PolicyTypeName: str
    Description: str
    PolicyAttributeTypeDescriptions: List["PolicyAttributeTypeDescriptionTypeDef"]


class RegisterEndPointsOutputTypeDef(TypedDict):
    Instances: List["InstanceTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class RemoveAvailabilityZonesOutputTypeDef(TypedDict):
    AvailabilityZones: List[str]
    ResponseMetadata: "ResponseMetadata"


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class SourceSecurityGroupTypeDef(TypedDict, total=False):
    OwnerAlias: str
    GroupName: str


class TagDescriptionTypeDef(TypedDict, total=False):
    LoadBalancerName: str
    Tags: List["TagTypeDef"]


class TagKeyOnlyTypeDef(TypedDict, total=False):
    Key: str


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    Value: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
