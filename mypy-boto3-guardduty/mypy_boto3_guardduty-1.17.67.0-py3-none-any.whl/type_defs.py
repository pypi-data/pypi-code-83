"""
Type annotations for guardduty service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/type_defs.html)

Usage::

    ```python
    from mypy_boto3_guardduty.type_defs import AccessControlListTypeDef

    data: AccessControlListTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_guardduty.literals import (
    AdminStatus,
    DataSource,
    DataSourceStatus,
    DetectorStatus,
    FilterAction,
    FindingPublishingFrequency,
    IpSetFormat,
    IpSetStatus,
    OrderBy,
    PublishingStatus,
    ThreatIntelSetFormat,
    ThreatIntelSetStatus,
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
    "AccessKeyDetailsTypeDef",
    "AccountDetailTypeDef",
    "AccountLevelPermissionsTypeDef",
    "ActionTypeDef",
    "AdminAccountTypeDef",
    "AwsApiCallActionTypeDef",
    "BlockPublicAccessTypeDef",
    "BucketLevelPermissionsTypeDef",
    "BucketPolicyTypeDef",
    "CityTypeDef",
    "CloudTrailConfigurationResultTypeDef",
    "ConditionTypeDef",
    "CountryTypeDef",
    "CreateDetectorResponseTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateMembersResponseTypeDef",
    "CreatePublishingDestinationResponseTypeDef",
    "CreateThreatIntelSetResponseTypeDef",
    "DNSLogsConfigurationResultTypeDef",
    "DataSourceConfigurationsResultTypeDef",
    "DataSourceConfigurationsTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DefaultServerSideEncryptionTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMembersResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DescribePublishingDestinationResponseTypeDef",
    "DestinationPropertiesTypeDef",
    "DestinationTypeDef",
    "DisassociateMembersResponseTypeDef",
    "DnsRequestActionTypeDef",
    "DomainDetailsTypeDef",
    "EvidenceTypeDef",
    "FindingCriteriaTypeDef",
    "FindingStatisticsTypeDef",
    "FindingTypeDef",
    "FlowLogsConfigurationResultTypeDef",
    "GeoLocationTypeDef",
    "GetDetectorResponseTypeDef",
    "GetFilterResponseTypeDef",
    "GetFindingsResponseTypeDef",
    "GetFindingsStatisticsResponseTypeDef",
    "GetIPSetResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMemberDetectorsResponseTypeDef",
    "GetMembersResponseTypeDef",
    "GetThreatIntelSetResponseTypeDef",
    "GetUsageStatisticsResponseTypeDef",
    "IamInstanceProfileTypeDef",
    "InstanceDetailsTypeDef",
    "InvitationTypeDef",
    "InviteMembersResponseTypeDef",
    "ListDetectorsResponseTypeDef",
    "ListFiltersResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListPublishingDestinationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListThreatIntelSetsResponseTypeDef",
    "LocalIpDetailsTypeDef",
    "LocalPortDetailsTypeDef",
    "MasterTypeDef",
    "MemberDataSourceConfigurationTypeDef",
    "MemberTypeDef",
    "NetworkConnectionActionTypeDef",
    "NetworkInterfaceTypeDef",
    "OrganizationDataSourceConfigurationsResultTypeDef",
    "OrganizationDataSourceConfigurationsTypeDef",
    "OrganizationS3LogsConfigurationResultTypeDef",
    "OrganizationS3LogsConfigurationTypeDef",
    "OrganizationTypeDef",
    "OwnerTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionConfigurationTypeDef",
    "PortProbeActionTypeDef",
    "PortProbeDetailTypeDef",
    "PrivateIpAddressDetailsTypeDef",
    "ProductCodeTypeDef",
    "PublicAccessTypeDef",
    "RemoteIpDetailsTypeDef",
    "RemotePortDetailsTypeDef",
    "ResourceTypeDef",
    "S3BucketDetailTypeDef",
    "S3LogsConfigurationResultTypeDef",
    "S3LogsConfigurationTypeDef",
    "SecurityGroupTypeDef",
    "ServiceTypeDef",
    "SortCriteriaTypeDef",
    "StartMonitoringMembersResponseTypeDef",
    "StopMonitoringMembersResponseTypeDef",
    "TagTypeDef",
    "ThreatIntelligenceDetailTypeDef",
    "TotalTypeDef",
    "UnprocessedAccountTypeDef",
    "UpdateFilterResponseTypeDef",
    "UpdateMemberDetectorsResponseTypeDef",
    "UsageAccountResultTypeDef",
    "UsageCriteriaTypeDef",
    "UsageDataSourceResultTypeDef",
    "UsageResourceResultTypeDef",
    "UsageStatisticsTypeDef",
)


class AccessControlListTypeDef(TypedDict, total=False):
    AllowsPublicReadAccess: bool
    AllowsPublicWriteAccess: bool


class AccessKeyDetailsTypeDef(TypedDict, total=False):
    AccessKeyId: str
    PrincipalId: str
    UserName: str
    UserType: str


class AccountDetailTypeDef(TypedDict):
    AccountId: str
    Email: str


class AccountLevelPermissionsTypeDef(TypedDict, total=False):
    BlockPublicAccess: "BlockPublicAccessTypeDef"


class ActionTypeDef(TypedDict, total=False):
    ActionType: str
    AwsApiCallAction: "AwsApiCallActionTypeDef"
    DnsRequestAction: "DnsRequestActionTypeDef"
    NetworkConnectionAction: "NetworkConnectionActionTypeDef"
    PortProbeAction: "PortProbeActionTypeDef"


class AdminAccountTypeDef(TypedDict, total=False):
    AdminAccountId: str
    AdminStatus: AdminStatus


class AwsApiCallActionTypeDef(TypedDict, total=False):
    Api: str
    CallerType: str
    DomainDetails: "DomainDetailsTypeDef"
    ErrorCode: str
    RemoteIpDetails: "RemoteIpDetailsTypeDef"
    ServiceName: str


class BlockPublicAccessTypeDef(TypedDict, total=False):
    IgnorePublicAcls: bool
    RestrictPublicBuckets: bool
    BlockPublicAcls: bool
    BlockPublicPolicy: bool


class BucketLevelPermissionsTypeDef(TypedDict, total=False):
    AccessControlList: "AccessControlListTypeDef"
    BucketPolicy: "BucketPolicyTypeDef"
    BlockPublicAccess: "BlockPublicAccessTypeDef"


class BucketPolicyTypeDef(TypedDict, total=False):
    AllowsPublicReadAccess: bool
    AllowsPublicWriteAccess: bool


class CityTypeDef(TypedDict, total=False):
    CityName: str


class CloudTrailConfigurationResultTypeDef(TypedDict):
    Status: DataSourceStatus


class ConditionTypeDef(TypedDict, total=False):
    Eq: List[str]
    Neq: List[str]
    Gt: int
    Gte: int
    Lt: int
    Lte: int
    Equals: List[str]
    NotEquals: List[str]
    GreaterThan: int
    GreaterThanOrEqual: int
    LessThan: int
    LessThanOrEqual: int


class CountryTypeDef(TypedDict, total=False):
    CountryCode: str
    CountryName: str


class CreateDetectorResponseTypeDef(TypedDict, total=False):
    DetectorId: str


class CreateFilterResponseTypeDef(TypedDict):
    Name: str


class CreateIPSetResponseTypeDef(TypedDict):
    IpSetId: str


class CreateMembersResponseTypeDef(TypedDict):
    UnprocessedAccounts: List["UnprocessedAccountTypeDef"]


class CreatePublishingDestinationResponseTypeDef(TypedDict):
    DestinationId: str


class CreateThreatIntelSetResponseTypeDef(TypedDict):
    ThreatIntelSetId: str


class DNSLogsConfigurationResultTypeDef(TypedDict):
    Status: DataSourceStatus


class DataSourceConfigurationsResultTypeDef(TypedDict):
    CloudTrail: "CloudTrailConfigurationResultTypeDef"
    DNSLogs: "DNSLogsConfigurationResultTypeDef"
    FlowLogs: "FlowLogsConfigurationResultTypeDef"
    S3Logs: "S3LogsConfigurationResultTypeDef"


class DataSourceConfigurationsTypeDef(TypedDict, total=False):
    S3Logs: "S3LogsConfigurationTypeDef"


class DeclineInvitationsResponseTypeDef(TypedDict):
    UnprocessedAccounts: List["UnprocessedAccountTypeDef"]


class DefaultServerSideEncryptionTypeDef(TypedDict, total=False):
    EncryptionType: str
    KmsMasterKeyArn: str


class DeleteInvitationsResponseTypeDef(TypedDict):
    UnprocessedAccounts: List["UnprocessedAccountTypeDef"]


class DeleteMembersResponseTypeDef(TypedDict):
    UnprocessedAccounts: List["UnprocessedAccountTypeDef"]


class _RequiredDescribeOrganizationConfigurationResponseTypeDef(TypedDict):
    AutoEnable: bool
    MemberAccountLimitReached: bool


class DescribeOrganizationConfigurationResponseTypeDef(
    _RequiredDescribeOrganizationConfigurationResponseTypeDef, total=False
):
    DataSources: "OrganizationDataSourceConfigurationsResultTypeDef"


class DescribePublishingDestinationResponseTypeDef(TypedDict):
    DestinationId: str
    DestinationType: Literal["S3"]
    Status: PublishingStatus
    PublishingFailureStartTimestamp: int
    DestinationProperties: "DestinationPropertiesTypeDef"


class DestinationPropertiesTypeDef(TypedDict, total=False):
    DestinationArn: str
    KmsKeyArn: str


class DestinationTypeDef(TypedDict):
    DestinationId: str
    DestinationType: Literal["S3"]
    Status: PublishingStatus


class DisassociateMembersResponseTypeDef(TypedDict):
    UnprocessedAccounts: List["UnprocessedAccountTypeDef"]


class DnsRequestActionTypeDef(TypedDict, total=False):
    Domain: str


class DomainDetailsTypeDef(TypedDict, total=False):
    Domain: str


class EvidenceTypeDef(TypedDict, total=False):
    ThreatIntelligenceDetails: List["ThreatIntelligenceDetailTypeDef"]


class FindingCriteriaTypeDef(TypedDict, total=False):
    Criterion: Dict[str, "ConditionTypeDef"]


class FindingStatisticsTypeDef(TypedDict, total=False):
    CountBySeverity: Dict[str, int]


_RequiredFindingTypeDef = TypedDict(
    "_RequiredFindingTypeDef",
    {
        "AccountId": str,
        "Arn": str,
        "CreatedAt": str,
        "Id": str,
        "Region": str,
        "Resource": "ResourceTypeDef",
        "SchemaVersion": str,
        "Severity": float,
        "Type": str,
        "UpdatedAt": str,
    },
)
_OptionalFindingTypeDef = TypedDict(
    "_OptionalFindingTypeDef",
    {
        "Confidence": float,
        "Description": str,
        "Partition": str,
        "Service": "ServiceTypeDef",
        "Title": str,
    },
    total=False,
)


class FindingTypeDef(_RequiredFindingTypeDef, _OptionalFindingTypeDef):
    pass


class FlowLogsConfigurationResultTypeDef(TypedDict):
    Status: DataSourceStatus


class GeoLocationTypeDef(TypedDict, total=False):
    Lat: float
    Lon: float


class _RequiredGetDetectorResponseTypeDef(TypedDict):
    ServiceRole: str
    Status: DetectorStatus


class GetDetectorResponseTypeDef(_RequiredGetDetectorResponseTypeDef, total=False):
    CreatedAt: str
    FindingPublishingFrequency: FindingPublishingFrequency
    UpdatedAt: str
    DataSources: "DataSourceConfigurationsResultTypeDef"
    Tags: Dict[str, str]


class _RequiredGetFilterResponseTypeDef(TypedDict):
    Name: str
    Action: FilterAction
    FindingCriteria: "FindingCriteriaTypeDef"


class GetFilterResponseTypeDef(_RequiredGetFilterResponseTypeDef, total=False):
    Description: str
    Rank: int
    Tags: Dict[str, str]


class GetFindingsResponseTypeDef(TypedDict):
    Findings: List["FindingTypeDef"]


class GetFindingsStatisticsResponseTypeDef(TypedDict):
    FindingStatistics: "FindingStatisticsTypeDef"


class _RequiredGetIPSetResponseTypeDef(TypedDict):
    Name: str
    Format: IpSetFormat
    Location: str
    Status: IpSetStatus


class GetIPSetResponseTypeDef(_RequiredGetIPSetResponseTypeDef, total=False):
    Tags: Dict[str, str]


class GetInvitationsCountResponseTypeDef(TypedDict, total=False):
    InvitationsCount: int


class GetMasterAccountResponseTypeDef(TypedDict):
    Master: "MasterTypeDef"


class GetMemberDetectorsResponseTypeDef(TypedDict):
    MemberDataSourceConfigurations: List["MemberDataSourceConfigurationTypeDef"]
    UnprocessedAccounts: List["UnprocessedAccountTypeDef"]


class GetMembersResponseTypeDef(TypedDict):
    Members: List["MemberTypeDef"]
    UnprocessedAccounts: List["UnprocessedAccountTypeDef"]


class _RequiredGetThreatIntelSetResponseTypeDef(TypedDict):
    Name: str
    Format: ThreatIntelSetFormat
    Location: str
    Status: ThreatIntelSetStatus


class GetThreatIntelSetResponseTypeDef(_RequiredGetThreatIntelSetResponseTypeDef, total=False):
    Tags: Dict[str, str]


class GetUsageStatisticsResponseTypeDef(TypedDict, total=False):
    UsageStatistics: "UsageStatisticsTypeDef"
    NextToken: str


class IamInstanceProfileTypeDef(TypedDict, total=False):
    Arn: str
    Id: str


class InstanceDetailsTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    IamInstanceProfile: "IamInstanceProfileTypeDef"
    ImageDescription: str
    ImageId: str
    InstanceId: str
    InstanceState: str
    InstanceType: str
    OutpostArn: str
    LaunchTime: str
    NetworkInterfaces: List["NetworkInterfaceTypeDef"]
    Platform: str
    ProductCodes: List["ProductCodeTypeDef"]
    Tags: List["TagTypeDef"]


class InvitationTypeDef(TypedDict, total=False):
    AccountId: str
    InvitationId: str
    RelationshipStatus: str
    InvitedAt: str


class InviteMembersResponseTypeDef(TypedDict):
    UnprocessedAccounts: List["UnprocessedAccountTypeDef"]


class _RequiredListDetectorsResponseTypeDef(TypedDict):
    DetectorIds: List[str]


class ListDetectorsResponseTypeDef(_RequiredListDetectorsResponseTypeDef, total=False):
    NextToken: str


class _RequiredListFiltersResponseTypeDef(TypedDict):
    FilterNames: List[str]


class ListFiltersResponseTypeDef(_RequiredListFiltersResponseTypeDef, total=False):
    NextToken: str


class _RequiredListFindingsResponseTypeDef(TypedDict):
    FindingIds: List[str]


class ListFindingsResponseTypeDef(_RequiredListFindingsResponseTypeDef, total=False):
    NextToken: str


class _RequiredListIPSetsResponseTypeDef(TypedDict):
    IpSetIds: List[str]


class ListIPSetsResponseTypeDef(_RequiredListIPSetsResponseTypeDef, total=False):
    NextToken: str


class ListInvitationsResponseTypeDef(TypedDict, total=False):
    Invitations: List["InvitationTypeDef"]
    NextToken: str


class ListMembersResponseTypeDef(TypedDict, total=False):
    Members: List["MemberTypeDef"]
    NextToken: str


class ListOrganizationAdminAccountsResponseTypeDef(TypedDict, total=False):
    AdminAccounts: List["AdminAccountTypeDef"]
    NextToken: str


class _RequiredListPublishingDestinationsResponseTypeDef(TypedDict):
    Destinations: List["DestinationTypeDef"]


class ListPublishingDestinationsResponseTypeDef(
    _RequiredListPublishingDestinationsResponseTypeDef, total=False
):
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class _RequiredListThreatIntelSetsResponseTypeDef(TypedDict):
    ThreatIntelSetIds: List[str]


class ListThreatIntelSetsResponseTypeDef(_RequiredListThreatIntelSetsResponseTypeDef, total=False):
    NextToken: str


class LocalIpDetailsTypeDef(TypedDict, total=False):
    IpAddressV4: str


class LocalPortDetailsTypeDef(TypedDict, total=False):
    Port: int
    PortName: str


class MasterTypeDef(TypedDict, total=False):
    AccountId: str
    InvitationId: str
    RelationshipStatus: str
    InvitedAt: str


class MemberDataSourceConfigurationTypeDef(TypedDict):
    AccountId: str
    DataSources: "DataSourceConfigurationsResultTypeDef"


class _RequiredMemberTypeDef(TypedDict):
    AccountId: str
    MasterId: str
    Email: str
    RelationshipStatus: str
    UpdatedAt: str


class MemberTypeDef(_RequiredMemberTypeDef, total=False):
    DetectorId: str
    InvitedAt: str


NetworkConnectionActionTypeDef = TypedDict(
    "NetworkConnectionActionTypeDef",
    {
        "Blocked": bool,
        "ConnectionDirection": str,
        "LocalPortDetails": "LocalPortDetailsTypeDef",
        "Protocol": str,
        "LocalIpDetails": "LocalIpDetailsTypeDef",
        "RemoteIpDetails": "RemoteIpDetailsTypeDef",
        "RemotePortDetails": "RemotePortDetailsTypeDef",
    },
    total=False,
)


class NetworkInterfaceTypeDef(TypedDict, total=False):
    Ipv6Addresses: List[str]
    NetworkInterfaceId: str
    PrivateDnsName: str
    PrivateIpAddress: str
    PrivateIpAddresses: List["PrivateIpAddressDetailsTypeDef"]
    PublicDnsName: str
    PublicIp: str
    SecurityGroups: List["SecurityGroupTypeDef"]
    SubnetId: str
    VpcId: str


class OrganizationDataSourceConfigurationsResultTypeDef(TypedDict):
    S3Logs: "OrganizationS3LogsConfigurationResultTypeDef"


class OrganizationDataSourceConfigurationsTypeDef(TypedDict, total=False):
    S3Logs: "OrganizationS3LogsConfigurationTypeDef"


class OrganizationS3LogsConfigurationResultTypeDef(TypedDict):
    AutoEnable: bool


class OrganizationS3LogsConfigurationTypeDef(TypedDict):
    AutoEnable: bool


class OrganizationTypeDef(TypedDict, total=False):
    Asn: str
    AsnOrg: str
    Isp: str
    Org: str


class OwnerTypeDef(TypedDict, total=False):
    Id: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PermissionConfigurationTypeDef(TypedDict, total=False):
    BucketLevelPermissions: "BucketLevelPermissionsTypeDef"
    AccountLevelPermissions: "AccountLevelPermissionsTypeDef"


class PortProbeActionTypeDef(TypedDict, total=False):
    Blocked: bool
    PortProbeDetails: List["PortProbeDetailTypeDef"]


class PortProbeDetailTypeDef(TypedDict, total=False):
    LocalPortDetails: "LocalPortDetailsTypeDef"
    LocalIpDetails: "LocalIpDetailsTypeDef"
    RemoteIpDetails: "RemoteIpDetailsTypeDef"


class PrivateIpAddressDetailsTypeDef(TypedDict, total=False):
    PrivateDnsName: str
    PrivateIpAddress: str


class ProductCodeTypeDef(TypedDict, total=False):
    Code: str
    ProductType: str


class PublicAccessTypeDef(TypedDict, total=False):
    PermissionConfiguration: "PermissionConfigurationTypeDef"
    EffectivePermission: str


class RemoteIpDetailsTypeDef(TypedDict, total=False):
    City: "CityTypeDef"
    Country: "CountryTypeDef"
    GeoLocation: "GeoLocationTypeDef"
    IpAddressV4: str
    Organization: "OrganizationTypeDef"


class RemotePortDetailsTypeDef(TypedDict, total=False):
    Port: int
    PortName: str


class ResourceTypeDef(TypedDict, total=False):
    AccessKeyDetails: "AccessKeyDetailsTypeDef"
    S3BucketDetails: List["S3BucketDetailTypeDef"]
    InstanceDetails: "InstanceDetailsTypeDef"
    ResourceType: str


S3BucketDetailTypeDef = TypedDict(
    "S3BucketDetailTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": str,
        "CreatedAt": datetime,
        "Owner": "OwnerTypeDef",
        "Tags": List["TagTypeDef"],
        "DefaultServerSideEncryption": "DefaultServerSideEncryptionTypeDef",
        "PublicAccess": "PublicAccessTypeDef",
    },
    total=False,
)


class S3LogsConfigurationResultTypeDef(TypedDict):
    Status: DataSourceStatus


class S3LogsConfigurationTypeDef(TypedDict):
    Enable: bool


class SecurityGroupTypeDef(TypedDict, total=False):
    GroupId: str
    GroupName: str


class ServiceTypeDef(TypedDict, total=False):
    Action: "ActionTypeDef"
    Evidence: "EvidenceTypeDef"
    Archived: bool
    Count: int
    DetectorId: str
    EventFirstSeen: str
    EventLastSeen: str
    ResourceRole: str
    ServiceName: str
    UserFeedback: str


class SortCriteriaTypeDef(TypedDict, total=False):
    AttributeName: str
    OrderBy: OrderBy


class StartMonitoringMembersResponseTypeDef(TypedDict):
    UnprocessedAccounts: List["UnprocessedAccountTypeDef"]


class StopMonitoringMembersResponseTypeDef(TypedDict):
    UnprocessedAccounts: List["UnprocessedAccountTypeDef"]


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class ThreatIntelligenceDetailTypeDef(TypedDict, total=False):
    ThreatListName: str
    ThreatNames: List[str]


class TotalTypeDef(TypedDict, total=False):
    Amount: str
    Unit: str


class UnprocessedAccountTypeDef(TypedDict):
    AccountId: str
    Result: str


class UpdateFilterResponseTypeDef(TypedDict):
    Name: str


class UpdateMemberDetectorsResponseTypeDef(TypedDict):
    UnprocessedAccounts: List["UnprocessedAccountTypeDef"]


class UsageAccountResultTypeDef(TypedDict, total=False):
    AccountId: str
    Total: "TotalTypeDef"


class _RequiredUsageCriteriaTypeDef(TypedDict):
    DataSources: List[DataSource]


class UsageCriteriaTypeDef(_RequiredUsageCriteriaTypeDef, total=False):
    AccountIds: List[str]
    Resources: List[str]


class UsageDataSourceResultTypeDef(TypedDict, total=False):
    DataSource: DataSource
    Total: "TotalTypeDef"


class UsageResourceResultTypeDef(TypedDict, total=False):
    Resource: str
    Total: "TotalTypeDef"


class UsageStatisticsTypeDef(TypedDict, total=False):
    SumByAccount: List["UsageAccountResultTypeDef"]
    SumByDataSource: List["UsageDataSourceResultTypeDef"]
    SumByResource: List["UsageResourceResultTypeDef"]
    TopResources: List["UsageResourceResultTypeDef"]
