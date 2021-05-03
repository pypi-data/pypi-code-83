"""
Type annotations for ds service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ds/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ds.type_defs import AcceptSharedDirectoryResultTypeDef

    data: AcceptSharedDirectoryResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_ds.literals import (
    CertificateState,
    CertificateType,
    DirectoryEdition,
    DirectorySize,
    DirectoryStage,
    DirectoryType,
    DomainControllerStatus,
    IpRouteStatusMsg,
    LDAPSStatus,
    RadiusAuthenticationProtocol,
    RadiusStatus,
    RegionType,
    SchemaExtensionStatus,
    SelectiveAuth,
    ShareMethod,
    ShareStatus,
    SnapshotStatus,
    SnapshotType,
    TopicStatus,
    TrustDirection,
    TrustState,
    TrustType,
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
    "AcceptSharedDirectoryResultTypeDef",
    "AttributeTypeDef",
    "CertificateInfoTypeDef",
    "CertificateTypeDef",
    "ClientCertAuthSettingsTypeDef",
    "ComputerTypeDef",
    "ConditionalForwarderTypeDef",
    "ConnectDirectoryResultTypeDef",
    "CreateAliasResultTypeDef",
    "CreateComputerResultTypeDef",
    "CreateDirectoryResultTypeDef",
    "CreateMicrosoftADResultTypeDef",
    "CreateSnapshotResultTypeDef",
    "CreateTrustResultTypeDef",
    "DeleteDirectoryResultTypeDef",
    "DeleteSnapshotResultTypeDef",
    "DeleteTrustResultTypeDef",
    "DescribeCertificateResultTypeDef",
    "DescribeConditionalForwardersResultTypeDef",
    "DescribeDirectoriesResultTypeDef",
    "DescribeDomainControllersResultTypeDef",
    "DescribeEventTopicsResultTypeDef",
    "DescribeLDAPSSettingsResultTypeDef",
    "DescribeRegionsResultTypeDef",
    "DescribeSharedDirectoriesResultTypeDef",
    "DescribeSnapshotsResultTypeDef",
    "DescribeTrustsResultTypeDef",
    "DirectoryConnectSettingsDescriptionTypeDef",
    "DirectoryConnectSettingsTypeDef",
    "DirectoryDescriptionTypeDef",
    "DirectoryLimitsTypeDef",
    "DirectoryVpcSettingsDescriptionTypeDef",
    "DirectoryVpcSettingsTypeDef",
    "DomainControllerTypeDef",
    "EventTopicTypeDef",
    "GetDirectoryLimitsResultTypeDef",
    "GetSnapshotLimitsResultTypeDef",
    "IpRouteInfoTypeDef",
    "IpRouteTypeDef",
    "LDAPSSettingInfoTypeDef",
    "ListCertificatesResultTypeDef",
    "ListIpRoutesResultTypeDef",
    "ListLogSubscriptionsResultTypeDef",
    "ListSchemaExtensionsResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "LogSubscriptionTypeDef",
    "OwnerDirectoryDescriptionTypeDef",
    "PaginatorConfigTypeDef",
    "RadiusSettingsTypeDef",
    "RegionDescriptionTypeDef",
    "RegionsInfoTypeDef",
    "RegisterCertificateResultTypeDef",
    "RejectSharedDirectoryResultTypeDef",
    "SchemaExtensionInfoTypeDef",
    "ShareDirectoryResultTypeDef",
    "ShareTargetTypeDef",
    "SharedDirectoryTypeDef",
    "SnapshotLimitsTypeDef",
    "SnapshotTypeDef",
    "StartSchemaExtensionResultTypeDef",
    "TagTypeDef",
    "TrustTypeDef",
    "UnshareDirectoryResultTypeDef",
    "UnshareTargetTypeDef",
    "UpdateTrustResultTypeDef",
    "VerifyTrustResultTypeDef",
)


class AcceptSharedDirectoryResultTypeDef(TypedDict, total=False):
    SharedDirectory: "SharedDirectoryTypeDef"


class AttributeTypeDef(TypedDict, total=False):
    Name: str
    Value: str


CertificateInfoTypeDef = TypedDict(
    "CertificateInfoTypeDef",
    {
        "CertificateId": str,
        "CommonName": str,
        "State": CertificateState,
        "ExpiryDateTime": datetime,
        "Type": CertificateType,
    },
    total=False,
)

CertificateTypeDef = TypedDict(
    "CertificateTypeDef",
    {
        "CertificateId": str,
        "State": CertificateState,
        "StateReason": str,
        "CommonName": str,
        "RegisteredDateTime": datetime,
        "ExpiryDateTime": datetime,
        "Type": CertificateType,
        "ClientCertAuthSettings": "ClientCertAuthSettingsTypeDef",
    },
    total=False,
)


class ClientCertAuthSettingsTypeDef(TypedDict, total=False):
    OCSPUrl: str


class ComputerTypeDef(TypedDict, total=False):
    ComputerId: str
    ComputerName: str
    ComputerAttributes: List["AttributeTypeDef"]


class ConditionalForwarderTypeDef(TypedDict, total=False):
    RemoteDomainName: str
    DnsIpAddrs: List[str]
    ReplicationScope: Literal["Domain"]


class ConnectDirectoryResultTypeDef(TypedDict, total=False):
    DirectoryId: str


class CreateAliasResultTypeDef(TypedDict, total=False):
    DirectoryId: str
    Alias: str


class CreateComputerResultTypeDef(TypedDict, total=False):
    Computer: "ComputerTypeDef"


class CreateDirectoryResultTypeDef(TypedDict, total=False):
    DirectoryId: str


class CreateMicrosoftADResultTypeDef(TypedDict, total=False):
    DirectoryId: str


class CreateSnapshotResultTypeDef(TypedDict, total=False):
    SnapshotId: str


class CreateTrustResultTypeDef(TypedDict, total=False):
    TrustId: str


class DeleteDirectoryResultTypeDef(TypedDict, total=False):
    DirectoryId: str


class DeleteSnapshotResultTypeDef(TypedDict, total=False):
    SnapshotId: str


class DeleteTrustResultTypeDef(TypedDict, total=False):
    TrustId: str


class DescribeCertificateResultTypeDef(TypedDict, total=False):
    Certificate: "CertificateTypeDef"


class DescribeConditionalForwardersResultTypeDef(TypedDict, total=False):
    ConditionalForwarders: List["ConditionalForwarderTypeDef"]


class DescribeDirectoriesResultTypeDef(TypedDict, total=False):
    DirectoryDescriptions: List["DirectoryDescriptionTypeDef"]
    NextToken: str


class DescribeDomainControllersResultTypeDef(TypedDict, total=False):
    DomainControllers: List["DomainControllerTypeDef"]
    NextToken: str


class DescribeEventTopicsResultTypeDef(TypedDict, total=False):
    EventTopics: List["EventTopicTypeDef"]


class DescribeLDAPSSettingsResultTypeDef(TypedDict, total=False):
    LDAPSSettingsInfo: List["LDAPSSettingInfoTypeDef"]
    NextToken: str


class DescribeRegionsResultTypeDef(TypedDict, total=False):
    RegionsDescription: List["RegionDescriptionTypeDef"]
    NextToken: str


class DescribeSharedDirectoriesResultTypeDef(TypedDict, total=False):
    SharedDirectories: List["SharedDirectoryTypeDef"]
    NextToken: str


class DescribeSnapshotsResultTypeDef(TypedDict, total=False):
    Snapshots: List["SnapshotTypeDef"]
    NextToken: str


class DescribeTrustsResultTypeDef(TypedDict, total=False):
    Trusts: List["TrustTypeDef"]
    NextToken: str


class DirectoryConnectSettingsDescriptionTypeDef(TypedDict, total=False):
    VpcId: str
    SubnetIds: List[str]
    CustomerUserName: str
    SecurityGroupId: str
    AvailabilityZones: List[str]
    ConnectIps: List[str]


class DirectoryConnectSettingsTypeDef(TypedDict):
    VpcId: str
    SubnetIds: List[str]
    CustomerDnsIps: List[str]
    CustomerUserName: str


DirectoryDescriptionTypeDef = TypedDict(
    "DirectoryDescriptionTypeDef",
    {
        "DirectoryId": str,
        "Name": str,
        "ShortName": str,
        "Size": DirectorySize,
        "Edition": DirectoryEdition,
        "Alias": str,
        "AccessUrl": str,
        "Description": str,
        "DnsIpAddrs": List[str],
        "Stage": DirectoryStage,
        "ShareStatus": ShareStatus,
        "ShareMethod": ShareMethod,
        "ShareNotes": str,
        "LaunchTime": datetime,
        "StageLastUpdatedDateTime": datetime,
        "Type": DirectoryType,
        "VpcSettings": "DirectoryVpcSettingsDescriptionTypeDef",
        "ConnectSettings": "DirectoryConnectSettingsDescriptionTypeDef",
        "RadiusSettings": "RadiusSettingsTypeDef",
        "RadiusStatus": RadiusStatus,
        "StageReason": str,
        "SsoEnabled": bool,
        "DesiredNumberOfDomainControllers": int,
        "OwnerDirectoryDescription": "OwnerDirectoryDescriptionTypeDef",
        "RegionsInfo": "RegionsInfoTypeDef",
    },
    total=False,
)


class DirectoryLimitsTypeDef(TypedDict, total=False):
    CloudOnlyDirectoriesLimit: int
    CloudOnlyDirectoriesCurrentCount: int
    CloudOnlyDirectoriesLimitReached: bool
    CloudOnlyMicrosoftADLimit: int
    CloudOnlyMicrosoftADCurrentCount: int
    CloudOnlyMicrosoftADLimitReached: bool
    ConnectedDirectoriesLimit: int
    ConnectedDirectoriesCurrentCount: int
    ConnectedDirectoriesLimitReached: bool


class DirectoryVpcSettingsDescriptionTypeDef(TypedDict, total=False):
    VpcId: str
    SubnetIds: List[str]
    SecurityGroupId: str
    AvailabilityZones: List[str]


class DirectoryVpcSettingsTypeDef(TypedDict):
    VpcId: str
    SubnetIds: List[str]


class DomainControllerTypeDef(TypedDict, total=False):
    DirectoryId: str
    DomainControllerId: str
    DnsIpAddr: str
    VpcId: str
    SubnetId: str
    AvailabilityZone: str
    Status: DomainControllerStatus
    StatusReason: str
    LaunchTime: datetime
    StatusLastUpdatedDateTime: datetime


class EventTopicTypeDef(TypedDict, total=False):
    DirectoryId: str
    TopicName: str
    TopicArn: str
    CreatedDateTime: datetime
    Status: TopicStatus


class GetDirectoryLimitsResultTypeDef(TypedDict, total=False):
    DirectoryLimits: "DirectoryLimitsTypeDef"


class GetSnapshotLimitsResultTypeDef(TypedDict, total=False):
    SnapshotLimits: "SnapshotLimitsTypeDef"


class IpRouteInfoTypeDef(TypedDict, total=False):
    DirectoryId: str
    CidrIp: str
    IpRouteStatusMsg: IpRouteStatusMsg
    AddedDateTime: datetime
    IpRouteStatusReason: str
    Description: str


class IpRouteTypeDef(TypedDict, total=False):
    CidrIp: str
    Description: str


class LDAPSSettingInfoTypeDef(TypedDict, total=False):
    LDAPSStatus: LDAPSStatus
    LDAPSStatusReason: str
    LastUpdatedDateTime: datetime


class ListCertificatesResultTypeDef(TypedDict, total=False):
    NextToken: str
    CertificatesInfo: List["CertificateInfoTypeDef"]


class ListIpRoutesResultTypeDef(TypedDict, total=False):
    IpRoutesInfo: List["IpRouteInfoTypeDef"]
    NextToken: str


class ListLogSubscriptionsResultTypeDef(TypedDict, total=False):
    LogSubscriptions: List["LogSubscriptionTypeDef"]
    NextToken: str


class ListSchemaExtensionsResultTypeDef(TypedDict, total=False):
    SchemaExtensionsInfo: List["SchemaExtensionInfoTypeDef"]
    NextToken: str


class ListTagsForResourceResultTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]
    NextToken: str


class LogSubscriptionTypeDef(TypedDict, total=False):
    DirectoryId: str
    LogGroupName: str
    SubscriptionCreatedDateTime: datetime


class OwnerDirectoryDescriptionTypeDef(TypedDict, total=False):
    DirectoryId: str
    AccountId: str
    DnsIpAddrs: List[str]
    VpcSettings: "DirectoryVpcSettingsDescriptionTypeDef"
    RadiusSettings: "RadiusSettingsTypeDef"
    RadiusStatus: RadiusStatus


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RadiusSettingsTypeDef(TypedDict, total=False):
    RadiusServers: List[str]
    RadiusPort: int
    RadiusTimeout: int
    RadiusRetries: int
    SharedSecret: str
    AuthenticationProtocol: RadiusAuthenticationProtocol
    DisplayLabel: str
    UseSameUsername: bool


class RegionDescriptionTypeDef(TypedDict, total=False):
    DirectoryId: str
    RegionName: str
    RegionType: RegionType
    Status: DirectoryStage
    VpcSettings: "DirectoryVpcSettingsTypeDef"
    DesiredNumberOfDomainControllers: int
    LaunchTime: datetime
    StatusLastUpdatedDateTime: datetime
    LastUpdatedDateTime: datetime


class RegionsInfoTypeDef(TypedDict, total=False):
    PrimaryRegion: str
    AdditionalRegions: List[str]


class RegisterCertificateResultTypeDef(TypedDict, total=False):
    CertificateId: str


class RejectSharedDirectoryResultTypeDef(TypedDict, total=False):
    SharedDirectoryId: str


class SchemaExtensionInfoTypeDef(TypedDict, total=False):
    DirectoryId: str
    SchemaExtensionId: str
    Description: str
    SchemaExtensionStatus: SchemaExtensionStatus
    SchemaExtensionStatusReason: str
    StartDateTime: datetime
    EndDateTime: datetime


class ShareDirectoryResultTypeDef(TypedDict, total=False):
    SharedDirectoryId: str


ShareTargetTypeDef = TypedDict("ShareTargetTypeDef", {"Id": str, "Type": Literal["ACCOUNT"]})


class SharedDirectoryTypeDef(TypedDict, total=False):
    OwnerAccountId: str
    OwnerDirectoryId: str
    ShareMethod: ShareMethod
    SharedAccountId: str
    SharedDirectoryId: str
    ShareStatus: ShareStatus
    ShareNotes: str
    CreatedDateTime: datetime
    LastUpdatedDateTime: datetime


class SnapshotLimitsTypeDef(TypedDict, total=False):
    ManualSnapshotsLimit: int
    ManualSnapshotsCurrentCount: int
    ManualSnapshotsLimitReached: bool


SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "DirectoryId": str,
        "SnapshotId": str,
        "Type": SnapshotType,
        "Name": str,
        "Status": SnapshotStatus,
        "StartTime": datetime,
    },
    total=False,
)


class StartSchemaExtensionResultTypeDef(TypedDict, total=False):
    SchemaExtensionId: str


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TrustTypeDef(TypedDict, total=False):
    DirectoryId: str
    TrustId: str
    RemoteDomainName: str
    TrustType: TrustType
    TrustDirection: TrustDirection
    TrustState: TrustState
    CreatedDateTime: datetime
    LastUpdatedDateTime: datetime
    StateLastUpdatedDateTime: datetime
    TrustStateReason: str
    SelectiveAuth: SelectiveAuth


class UnshareDirectoryResultTypeDef(TypedDict, total=False):
    SharedDirectoryId: str


UnshareTargetTypeDef = TypedDict("UnshareTargetTypeDef", {"Id": str, "Type": Literal["ACCOUNT"]})


class UpdateTrustResultTypeDef(TypedDict, total=False):
    RequestId: str
    TrustId: str


class VerifyTrustResultTypeDef(TypedDict, total=False):
    TrustId: str
