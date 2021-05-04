"""
Type annotations for route53 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53/type_defs.html)

Usage::

    ```python
    from mypy_boto3_route53.type_defs import AccountLimitTypeDef

    data: AccountLimitTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_route53.literals import (
    AccountLimitType,
    ChangeAction,
    ChangeStatus,
    CloudWatchRegion,
    ComparisonOperator,
    HealthCheckRegion,
    HealthCheckType,
    HostedZoneLimitType,
    InsufficientDataHealthStatus,
    ResourceRecordSetFailover,
    ResourceRecordSetRegion,
    RRType,
    Statistic,
    TagResourceType,
    VPCRegion,
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
    "AccountLimitTypeDef",
    "ActivateKeySigningKeyResponseTypeDef",
    "AlarmIdentifierTypeDef",
    "AliasTargetTypeDef",
    "AssociateVPCWithHostedZoneResponseTypeDef",
    "ChangeBatchTypeDef",
    "ChangeInfoTypeDef",
    "ChangeResourceRecordSetsResponseTypeDef",
    "ChangeTypeDef",
    "CloudWatchAlarmConfigurationTypeDef",
    "CreateHealthCheckResponseTypeDef",
    "CreateHostedZoneResponseTypeDef",
    "CreateKeySigningKeyResponseTypeDef",
    "CreateQueryLoggingConfigResponseTypeDef",
    "CreateReusableDelegationSetResponseTypeDef",
    "CreateTrafficPolicyInstanceResponseTypeDef",
    "CreateTrafficPolicyResponseTypeDef",
    "CreateTrafficPolicyVersionResponseTypeDef",
    "CreateVPCAssociationAuthorizationResponseTypeDef",
    "DNSSECStatusTypeDef",
    "DeactivateKeySigningKeyResponseTypeDef",
    "DelegationSetTypeDef",
    "DeleteHostedZoneResponseTypeDef",
    "DeleteKeySigningKeyResponseTypeDef",
    "DimensionTypeDef",
    "DisableHostedZoneDNSSECResponseTypeDef",
    "DisassociateVPCFromHostedZoneResponseTypeDef",
    "EnableHostedZoneDNSSECResponseTypeDef",
    "GeoLocationDetailsTypeDef",
    "GeoLocationTypeDef",
    "GetAccountLimitResponseTypeDef",
    "GetChangeResponseTypeDef",
    "GetCheckerIpRangesResponseTypeDef",
    "GetDNSSECResponseTypeDef",
    "GetGeoLocationResponseTypeDef",
    "GetHealthCheckCountResponseTypeDef",
    "GetHealthCheckLastFailureReasonResponseTypeDef",
    "GetHealthCheckResponseTypeDef",
    "GetHealthCheckStatusResponseTypeDef",
    "GetHostedZoneCountResponseTypeDef",
    "GetHostedZoneLimitResponseTypeDef",
    "GetHostedZoneResponseTypeDef",
    "GetQueryLoggingConfigResponseTypeDef",
    "GetReusableDelegationSetLimitResponseTypeDef",
    "GetReusableDelegationSetResponseTypeDef",
    "GetTrafficPolicyInstanceCountResponseTypeDef",
    "GetTrafficPolicyInstanceResponseTypeDef",
    "GetTrafficPolicyResponseTypeDef",
    "HealthCheckConfigTypeDef",
    "HealthCheckObservationTypeDef",
    "HealthCheckTypeDef",
    "HostedZoneConfigTypeDef",
    "HostedZoneLimitTypeDef",
    "HostedZoneOwnerTypeDef",
    "HostedZoneSummaryTypeDef",
    "HostedZoneTypeDef",
    "KeySigningKeyTypeDef",
    "LinkedServiceTypeDef",
    "ListGeoLocationsResponseTypeDef",
    "ListHealthChecksResponseTypeDef",
    "ListHostedZonesByNameResponseTypeDef",
    "ListHostedZonesByVPCResponseTypeDef",
    "ListHostedZonesResponseTypeDef",
    "ListQueryLoggingConfigsResponseTypeDef",
    "ListResourceRecordSetsResponseTypeDef",
    "ListReusableDelegationSetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTagsForResourcesResponseTypeDef",
    "ListTrafficPoliciesResponseTypeDef",
    "ListTrafficPolicyInstancesByHostedZoneResponseTypeDef",
    "ListTrafficPolicyInstancesByPolicyResponseTypeDef",
    "ListTrafficPolicyInstancesResponseTypeDef",
    "ListTrafficPolicyVersionsResponseTypeDef",
    "ListVPCAssociationAuthorizationsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "QueryLoggingConfigTypeDef",
    "ResourceRecordSetTypeDef",
    "ResourceRecordTypeDef",
    "ResourceTagSetTypeDef",
    "ReusableDelegationSetLimitTypeDef",
    "StatusReportTypeDef",
    "TagTypeDef",
    "TestDNSAnswerResponseTypeDef",
    "TrafficPolicyInstanceTypeDef",
    "TrafficPolicySummaryTypeDef",
    "TrafficPolicyTypeDef",
    "UpdateHealthCheckResponseTypeDef",
    "UpdateHostedZoneCommentResponseTypeDef",
    "UpdateTrafficPolicyCommentResponseTypeDef",
    "UpdateTrafficPolicyInstanceResponseTypeDef",
    "VPCTypeDef",
    "WaiterConfigTypeDef",
)

AccountLimitTypeDef = TypedDict("AccountLimitTypeDef", {"Type": AccountLimitType, "Value": int})


class ActivateKeySigningKeyResponseTypeDef(TypedDict):
    ChangeInfo: "ChangeInfoTypeDef"


class AlarmIdentifierTypeDef(TypedDict):
    Region: CloudWatchRegion
    Name: str


class AliasTargetTypeDef(TypedDict):
    HostedZoneId: str
    DNSName: str
    EvaluateTargetHealth: bool


class AssociateVPCWithHostedZoneResponseTypeDef(TypedDict):
    ChangeInfo: "ChangeInfoTypeDef"


class _RequiredChangeBatchTypeDef(TypedDict):
    Changes: List["ChangeTypeDef"]


class ChangeBatchTypeDef(_RequiredChangeBatchTypeDef, total=False):
    Comment: str


class _RequiredChangeInfoTypeDef(TypedDict):
    Id: str
    Status: ChangeStatus
    SubmittedAt: datetime


class ChangeInfoTypeDef(_RequiredChangeInfoTypeDef, total=False):
    Comment: str


class ChangeResourceRecordSetsResponseTypeDef(TypedDict):
    ChangeInfo: "ChangeInfoTypeDef"


class ChangeTypeDef(TypedDict):
    Action: ChangeAction
    ResourceRecordSet: "ResourceRecordSetTypeDef"


class _RequiredCloudWatchAlarmConfigurationTypeDef(TypedDict):
    EvaluationPeriods: int
    Threshold: float
    ComparisonOperator: ComparisonOperator
    Period: int
    MetricName: str
    Namespace: str
    Statistic: Statistic


class CloudWatchAlarmConfigurationTypeDef(
    _RequiredCloudWatchAlarmConfigurationTypeDef, total=False
):
    Dimensions: List["DimensionTypeDef"]


class CreateHealthCheckResponseTypeDef(TypedDict):
    HealthCheck: "HealthCheckTypeDef"
    Location: str


class _RequiredCreateHostedZoneResponseTypeDef(TypedDict):
    HostedZone: "HostedZoneTypeDef"
    ChangeInfo: "ChangeInfoTypeDef"
    DelegationSet: "DelegationSetTypeDef"
    Location: str


class CreateHostedZoneResponseTypeDef(_RequiredCreateHostedZoneResponseTypeDef, total=False):
    VPC: "VPCTypeDef"


class CreateKeySigningKeyResponseTypeDef(TypedDict):
    ChangeInfo: "ChangeInfoTypeDef"
    KeySigningKey: "KeySigningKeyTypeDef"
    Location: str


class CreateQueryLoggingConfigResponseTypeDef(TypedDict):
    QueryLoggingConfig: "QueryLoggingConfigTypeDef"
    Location: str


class CreateReusableDelegationSetResponseTypeDef(TypedDict):
    DelegationSet: "DelegationSetTypeDef"
    Location: str


class CreateTrafficPolicyInstanceResponseTypeDef(TypedDict):
    TrafficPolicyInstance: "TrafficPolicyInstanceTypeDef"
    Location: str


class CreateTrafficPolicyResponseTypeDef(TypedDict):
    TrafficPolicy: "TrafficPolicyTypeDef"
    Location: str


class CreateTrafficPolicyVersionResponseTypeDef(TypedDict):
    TrafficPolicy: "TrafficPolicyTypeDef"
    Location: str


class CreateVPCAssociationAuthorizationResponseTypeDef(TypedDict):
    HostedZoneId: str
    VPC: "VPCTypeDef"


class DNSSECStatusTypeDef(TypedDict, total=False):
    ServeSignature: str
    StatusMessage: str


class DeactivateKeySigningKeyResponseTypeDef(TypedDict):
    ChangeInfo: "ChangeInfoTypeDef"


class _RequiredDelegationSetTypeDef(TypedDict):
    NameServers: List[str]


class DelegationSetTypeDef(_RequiredDelegationSetTypeDef, total=False):
    Id: str
    CallerReference: str


class DeleteHostedZoneResponseTypeDef(TypedDict):
    ChangeInfo: "ChangeInfoTypeDef"


class DeleteKeySigningKeyResponseTypeDef(TypedDict):
    ChangeInfo: "ChangeInfoTypeDef"


class DimensionTypeDef(TypedDict):
    Name: str
    Value: str


class DisableHostedZoneDNSSECResponseTypeDef(TypedDict):
    ChangeInfo: "ChangeInfoTypeDef"


class DisassociateVPCFromHostedZoneResponseTypeDef(TypedDict):
    ChangeInfo: "ChangeInfoTypeDef"


class EnableHostedZoneDNSSECResponseTypeDef(TypedDict):
    ChangeInfo: "ChangeInfoTypeDef"


class GeoLocationDetailsTypeDef(TypedDict, total=False):
    ContinentCode: str
    ContinentName: str
    CountryCode: str
    CountryName: str
    SubdivisionCode: str
    SubdivisionName: str


class GeoLocationTypeDef(TypedDict, total=False):
    ContinentCode: str
    CountryCode: str
    SubdivisionCode: str


class GetAccountLimitResponseTypeDef(TypedDict):
    Limit: "AccountLimitTypeDef"
    Count: int


class GetChangeResponseTypeDef(TypedDict):
    ChangeInfo: "ChangeInfoTypeDef"


class GetCheckerIpRangesResponseTypeDef(TypedDict):
    CheckerIpRanges: List[str]


class GetDNSSECResponseTypeDef(TypedDict):
    Status: "DNSSECStatusTypeDef"
    KeySigningKeys: List["KeySigningKeyTypeDef"]


class GetGeoLocationResponseTypeDef(TypedDict):
    GeoLocationDetails: "GeoLocationDetailsTypeDef"


class GetHealthCheckCountResponseTypeDef(TypedDict):
    HealthCheckCount: int


class GetHealthCheckLastFailureReasonResponseTypeDef(TypedDict):
    HealthCheckObservations: List["HealthCheckObservationTypeDef"]


class GetHealthCheckResponseTypeDef(TypedDict):
    HealthCheck: "HealthCheckTypeDef"


class GetHealthCheckStatusResponseTypeDef(TypedDict):
    HealthCheckObservations: List["HealthCheckObservationTypeDef"]


class GetHostedZoneCountResponseTypeDef(TypedDict):
    HostedZoneCount: int


class GetHostedZoneLimitResponseTypeDef(TypedDict):
    Limit: "HostedZoneLimitTypeDef"
    Count: int


class _RequiredGetHostedZoneResponseTypeDef(TypedDict):
    HostedZone: "HostedZoneTypeDef"


class GetHostedZoneResponseTypeDef(_RequiredGetHostedZoneResponseTypeDef, total=False):
    DelegationSet: "DelegationSetTypeDef"
    VPCs: List["VPCTypeDef"]


class GetQueryLoggingConfigResponseTypeDef(TypedDict):
    QueryLoggingConfig: "QueryLoggingConfigTypeDef"


class GetReusableDelegationSetLimitResponseTypeDef(TypedDict):
    Limit: "ReusableDelegationSetLimitTypeDef"
    Count: int


class GetReusableDelegationSetResponseTypeDef(TypedDict):
    DelegationSet: "DelegationSetTypeDef"


class GetTrafficPolicyInstanceCountResponseTypeDef(TypedDict):
    TrafficPolicyInstanceCount: int


class GetTrafficPolicyInstanceResponseTypeDef(TypedDict):
    TrafficPolicyInstance: "TrafficPolicyInstanceTypeDef"


class GetTrafficPolicyResponseTypeDef(TypedDict):
    TrafficPolicy: "TrafficPolicyTypeDef"


_RequiredHealthCheckConfigTypeDef = TypedDict(
    "_RequiredHealthCheckConfigTypeDef", {"Type": HealthCheckType}
)
_OptionalHealthCheckConfigTypeDef = TypedDict(
    "_OptionalHealthCheckConfigTypeDef",
    {
        "IPAddress": str,
        "Port": int,
        "ResourcePath": str,
        "FullyQualifiedDomainName": str,
        "SearchString": str,
        "RequestInterval": int,
        "FailureThreshold": int,
        "MeasureLatency": bool,
        "Inverted": bool,
        "Disabled": bool,
        "HealthThreshold": int,
        "ChildHealthChecks": List[str],
        "EnableSNI": bool,
        "Regions": List[HealthCheckRegion],
        "AlarmIdentifier": "AlarmIdentifierTypeDef",
        "InsufficientDataHealthStatus": InsufficientDataHealthStatus,
    },
    total=False,
)


class HealthCheckConfigTypeDef(
    _RequiredHealthCheckConfigTypeDef, _OptionalHealthCheckConfigTypeDef
):
    pass


class HealthCheckObservationTypeDef(TypedDict, total=False):
    Region: HealthCheckRegion
    IPAddress: str
    StatusReport: "StatusReportTypeDef"


class _RequiredHealthCheckTypeDef(TypedDict):
    Id: str
    CallerReference: str
    HealthCheckConfig: "HealthCheckConfigTypeDef"
    HealthCheckVersion: int


class HealthCheckTypeDef(_RequiredHealthCheckTypeDef, total=False):
    LinkedService: "LinkedServiceTypeDef"
    CloudWatchAlarmConfiguration: "CloudWatchAlarmConfigurationTypeDef"


class HostedZoneConfigTypeDef(TypedDict, total=False):
    Comment: str
    PrivateZone: bool


HostedZoneLimitTypeDef = TypedDict(
    "HostedZoneLimitTypeDef", {"Type": HostedZoneLimitType, "Value": int}
)


class HostedZoneOwnerTypeDef(TypedDict, total=False):
    OwningAccount: str
    OwningService: str


class HostedZoneSummaryTypeDef(TypedDict):
    HostedZoneId: str
    Name: str
    Owner: "HostedZoneOwnerTypeDef"


class _RequiredHostedZoneTypeDef(TypedDict):
    Id: str
    Name: str
    CallerReference: str


class HostedZoneTypeDef(_RequiredHostedZoneTypeDef, total=False):
    Config: "HostedZoneConfigTypeDef"
    ResourceRecordSetCount: int
    LinkedService: "LinkedServiceTypeDef"


class KeySigningKeyTypeDef(TypedDict, total=False):
    Name: str
    KmsArn: str
    Flag: int
    SigningAlgorithmMnemonic: str
    SigningAlgorithmType: int
    DigestAlgorithmMnemonic: str
    DigestAlgorithmType: int
    KeyTag: int
    DigestValue: str
    PublicKey: str
    DSRecord: str
    DNSKEYRecord: str
    Status: str
    StatusMessage: str
    CreatedDate: datetime
    LastModifiedDate: datetime


class LinkedServiceTypeDef(TypedDict, total=False):
    ServicePrincipal: str
    Description: str


class _RequiredListGeoLocationsResponseTypeDef(TypedDict):
    GeoLocationDetailsList: List["GeoLocationDetailsTypeDef"]
    IsTruncated: bool
    MaxItems: str


class ListGeoLocationsResponseTypeDef(_RequiredListGeoLocationsResponseTypeDef, total=False):
    NextContinentCode: str
    NextCountryCode: str
    NextSubdivisionCode: str


class _RequiredListHealthChecksResponseTypeDef(TypedDict):
    HealthChecks: List["HealthCheckTypeDef"]
    Marker: str
    IsTruncated: bool
    MaxItems: str


class ListHealthChecksResponseTypeDef(_RequiredListHealthChecksResponseTypeDef, total=False):
    NextMarker: str


class _RequiredListHostedZonesByNameResponseTypeDef(TypedDict):
    HostedZones: List["HostedZoneTypeDef"]
    IsTruncated: bool
    MaxItems: str


class ListHostedZonesByNameResponseTypeDef(
    _RequiredListHostedZonesByNameResponseTypeDef, total=False
):
    DNSName: str
    HostedZoneId: str
    NextDNSName: str
    NextHostedZoneId: str


class _RequiredListHostedZonesByVPCResponseTypeDef(TypedDict):
    HostedZoneSummaries: List["HostedZoneSummaryTypeDef"]
    MaxItems: str


class ListHostedZonesByVPCResponseTypeDef(
    _RequiredListHostedZonesByVPCResponseTypeDef, total=False
):
    NextToken: str


class _RequiredListHostedZonesResponseTypeDef(TypedDict):
    HostedZones: List["HostedZoneTypeDef"]
    Marker: str
    IsTruncated: bool
    MaxItems: str


class ListHostedZonesResponseTypeDef(_RequiredListHostedZonesResponseTypeDef, total=False):
    NextMarker: str


class _RequiredListQueryLoggingConfigsResponseTypeDef(TypedDict):
    QueryLoggingConfigs: List["QueryLoggingConfigTypeDef"]


class ListQueryLoggingConfigsResponseTypeDef(
    _RequiredListQueryLoggingConfigsResponseTypeDef, total=False
):
    NextToken: str


class _RequiredListResourceRecordSetsResponseTypeDef(TypedDict):
    ResourceRecordSets: List["ResourceRecordSetTypeDef"]
    IsTruncated: bool
    MaxItems: str


class ListResourceRecordSetsResponseTypeDef(
    _RequiredListResourceRecordSetsResponseTypeDef, total=False
):
    NextRecordName: str
    NextRecordType: RRType
    NextRecordIdentifier: str


class _RequiredListReusableDelegationSetsResponseTypeDef(TypedDict):
    DelegationSets: List["DelegationSetTypeDef"]
    Marker: str
    IsTruncated: bool
    MaxItems: str


class ListReusableDelegationSetsResponseTypeDef(
    _RequiredListReusableDelegationSetsResponseTypeDef, total=False
):
    NextMarker: str


class ListTagsForResourceResponseTypeDef(TypedDict):
    ResourceTagSet: "ResourceTagSetTypeDef"


class ListTagsForResourcesResponseTypeDef(TypedDict):
    ResourceTagSets: List["ResourceTagSetTypeDef"]


class ListTrafficPoliciesResponseTypeDef(TypedDict):
    TrafficPolicySummaries: List["TrafficPolicySummaryTypeDef"]
    IsTruncated: bool
    TrafficPolicyIdMarker: str
    MaxItems: str


class _RequiredListTrafficPolicyInstancesByHostedZoneResponseTypeDef(TypedDict):
    TrafficPolicyInstances: List["TrafficPolicyInstanceTypeDef"]
    IsTruncated: bool
    MaxItems: str


class ListTrafficPolicyInstancesByHostedZoneResponseTypeDef(
    _RequiredListTrafficPolicyInstancesByHostedZoneResponseTypeDef, total=False
):
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRType


class _RequiredListTrafficPolicyInstancesByPolicyResponseTypeDef(TypedDict):
    TrafficPolicyInstances: List["TrafficPolicyInstanceTypeDef"]
    IsTruncated: bool
    MaxItems: str


class ListTrafficPolicyInstancesByPolicyResponseTypeDef(
    _RequiredListTrafficPolicyInstancesByPolicyResponseTypeDef, total=False
):
    HostedZoneIdMarker: str
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRType


class _RequiredListTrafficPolicyInstancesResponseTypeDef(TypedDict):
    TrafficPolicyInstances: List["TrafficPolicyInstanceTypeDef"]
    IsTruncated: bool
    MaxItems: str


class ListTrafficPolicyInstancesResponseTypeDef(
    _RequiredListTrafficPolicyInstancesResponseTypeDef, total=False
):
    HostedZoneIdMarker: str
    TrafficPolicyInstanceNameMarker: str
    TrafficPolicyInstanceTypeMarker: RRType


class ListTrafficPolicyVersionsResponseTypeDef(TypedDict):
    TrafficPolicies: List["TrafficPolicyTypeDef"]
    IsTruncated: bool
    TrafficPolicyVersionMarker: str
    MaxItems: str


class _RequiredListVPCAssociationAuthorizationsResponseTypeDef(TypedDict):
    HostedZoneId: str
    VPCs: List["VPCTypeDef"]


class ListVPCAssociationAuthorizationsResponseTypeDef(
    _RequiredListVPCAssociationAuthorizationsResponseTypeDef, total=False
):
    NextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class QueryLoggingConfigTypeDef(TypedDict):
    Id: str
    HostedZoneId: str
    CloudWatchLogsLogGroupArn: str


_RequiredResourceRecordSetTypeDef = TypedDict(
    "_RequiredResourceRecordSetTypeDef", {"Name": str, "Type": RRType}
)
_OptionalResourceRecordSetTypeDef = TypedDict(
    "_OptionalResourceRecordSetTypeDef",
    {
        "SetIdentifier": str,
        "Weight": int,
        "Region": ResourceRecordSetRegion,
        "GeoLocation": "GeoLocationTypeDef",
        "Failover": ResourceRecordSetFailover,
        "MultiValueAnswer": bool,
        "TTL": int,
        "ResourceRecords": List["ResourceRecordTypeDef"],
        "AliasTarget": "AliasTargetTypeDef",
        "HealthCheckId": str,
        "TrafficPolicyInstanceId": str,
    },
    total=False,
)


class ResourceRecordSetTypeDef(
    _RequiredResourceRecordSetTypeDef, _OptionalResourceRecordSetTypeDef
):
    pass


class ResourceRecordTypeDef(TypedDict):
    Value: str


class ResourceTagSetTypeDef(TypedDict, total=False):
    ResourceType: TagResourceType
    ResourceId: str
    Tags: List["TagTypeDef"]


ReusableDelegationSetLimitTypeDef = TypedDict(
    "ReusableDelegationSetLimitTypeDef",
    {"Type": Literal["MAX_ZONES_BY_REUSABLE_DELEGATION_SET"], "Value": int},
)


class StatusReportTypeDef(TypedDict, total=False):
    Status: str
    CheckedTime: datetime


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


TestDNSAnswerResponseTypeDef = TypedDict(
    "TestDNSAnswerResponseTypeDef",
    {
        "Nameserver": str,
        "RecordName": str,
        "RecordType": RRType,
        "RecordData": List[str],
        "ResponseCode": str,
        "Protocol": str,
    },
)


class TrafficPolicyInstanceTypeDef(TypedDict):
    Id: str
    HostedZoneId: str
    Name: str
    TTL: int
    State: str
    Message: str
    TrafficPolicyId: str
    TrafficPolicyVersion: int
    TrafficPolicyType: RRType


TrafficPolicySummaryTypeDef = TypedDict(
    "TrafficPolicySummaryTypeDef",
    {"Id": str, "Name": str, "Type": RRType, "LatestVersion": int, "TrafficPolicyCount": int},
)

_RequiredTrafficPolicyTypeDef = TypedDict(
    "_RequiredTrafficPolicyTypeDef",
    {"Id": str, "Version": int, "Name": str, "Type": RRType, "Document": str},
)
_OptionalTrafficPolicyTypeDef = TypedDict(
    "_OptionalTrafficPolicyTypeDef", {"Comment": str}, total=False
)


class TrafficPolicyTypeDef(_RequiredTrafficPolicyTypeDef, _OptionalTrafficPolicyTypeDef):
    pass


class UpdateHealthCheckResponseTypeDef(TypedDict):
    HealthCheck: "HealthCheckTypeDef"


class UpdateHostedZoneCommentResponseTypeDef(TypedDict):
    HostedZone: "HostedZoneTypeDef"


class UpdateTrafficPolicyCommentResponseTypeDef(TypedDict):
    TrafficPolicy: "TrafficPolicyTypeDef"


class UpdateTrafficPolicyInstanceResponseTypeDef(TypedDict):
    TrafficPolicyInstance: "TrafficPolicyInstanceTypeDef"


class VPCTypeDef(TypedDict, total=False):
    VPCRegion: VPCRegion
    VPCId: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
