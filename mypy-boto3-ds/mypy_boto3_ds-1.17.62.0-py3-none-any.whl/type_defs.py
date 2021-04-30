"""
Main interface for ds service type definitions.

Usage::

    ```python
    from mypy_boto3_ds.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
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
    ReplicationScope,
    SchemaExtensionStatus,
    SelectiveAuth,
    ShareMethod,
    ShareStatus,
    SnapshotStatus,
    SnapshotType,
    TargetType,
    TopicStatus,
    TrustDirection,
    TrustState,
    TrustType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AttributeTypeDef",
    "CertificateInfoTypeDef",
    "CertificateTypeDef",
    "ClientCertAuthSettingsTypeDef",
    "ComputerTypeDef",
    "ConditionalForwarderTypeDef",
    "DirectoryConnectSettingsDescriptionTypeDef",
    "DirectoryDescriptionTypeDef",
    "DirectoryLimitsTypeDef",
    "DirectoryVpcSettingsDescriptionTypeDef",
    "DirectoryVpcSettingsTypeDef",
    "DomainControllerTypeDef",
    "EventTopicTypeDef",
    "IpRouteInfoTypeDef",
    "LDAPSSettingInfoTypeDef",
    "LogSubscriptionTypeDef",
    "OwnerDirectoryDescriptionTypeDef",
    "RadiusSettingsTypeDef",
    "RegionDescriptionTypeDef",
    "RegionsInfoTypeDef",
    "SchemaExtensionInfoTypeDef",
    "SharedDirectoryTypeDef",
    "SnapshotLimitsTypeDef",
    "SnapshotTypeDef",
    "TagTypeDef",
    "TrustTypeDef",
    "AcceptSharedDirectoryResultTypeDef",
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
    "DirectoryConnectSettingsTypeDef",
    "GetDirectoryLimitsResultTypeDef",
    "GetSnapshotLimitsResultTypeDef",
    "IpRouteTypeDef",
    "ListCertificatesResultTypeDef",
    "ListIpRoutesResultTypeDef",
    "ListLogSubscriptionsResultTypeDef",
    "ListSchemaExtensionsResultTypeDef",
    "ListTagsForResourceResultTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterCertificateResultTypeDef",
    "RejectSharedDirectoryResultTypeDef",
    "ShareDirectoryResultTypeDef",
    "ShareTargetTypeDef",
    "StartSchemaExtensionResultTypeDef",
    "UnshareDirectoryResultTypeDef",
    "UnshareTargetTypeDef",
    "UpdateTrustResultTypeDef",
    "VerifyTrustResultTypeDef",
)

AttributeTypeDef = TypedDict("AttributeTypeDef", {"Name": str, "Value": str}, total=False)

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

ClientCertAuthSettingsTypeDef = TypedDict(
    "ClientCertAuthSettingsTypeDef", {"OCSPUrl": str}, total=False
)

ComputerTypeDef = TypedDict(
    "ComputerTypeDef",
    {"ComputerId": str, "ComputerName": str, "ComputerAttributes": List["AttributeTypeDef"]},
    total=False,
)

ConditionalForwarderTypeDef = TypedDict(
    "ConditionalForwarderTypeDef",
    {"RemoteDomainName": str, "DnsIpAddrs": List[str], "ReplicationScope": ReplicationScope},
    total=False,
)

DirectoryConnectSettingsDescriptionTypeDef = TypedDict(
    "DirectoryConnectSettingsDescriptionTypeDef",
    {
        "VpcId": str,
        "SubnetIds": List[str],
        "CustomerUserName": str,
        "SecurityGroupId": str,
        "AvailabilityZones": List[str],
        "ConnectIps": List[str],
    },
    total=False,
)

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

DirectoryLimitsTypeDef = TypedDict(
    "DirectoryLimitsTypeDef",
    {
        "CloudOnlyDirectoriesLimit": int,
        "CloudOnlyDirectoriesCurrentCount": int,
        "CloudOnlyDirectoriesLimitReached": bool,
        "CloudOnlyMicrosoftADLimit": int,
        "CloudOnlyMicrosoftADCurrentCount": int,
        "CloudOnlyMicrosoftADLimitReached": bool,
        "ConnectedDirectoriesLimit": int,
        "ConnectedDirectoriesCurrentCount": int,
        "ConnectedDirectoriesLimitReached": bool,
    },
    total=False,
)

DirectoryVpcSettingsDescriptionTypeDef = TypedDict(
    "DirectoryVpcSettingsDescriptionTypeDef",
    {"VpcId": str, "SubnetIds": List[str], "SecurityGroupId": str, "AvailabilityZones": List[str]},
    total=False,
)

DirectoryVpcSettingsTypeDef = TypedDict(
    "DirectoryVpcSettingsTypeDef", {"VpcId": str, "SubnetIds": List[str]}
)

DomainControllerTypeDef = TypedDict(
    "DomainControllerTypeDef",
    {
        "DirectoryId": str,
        "DomainControllerId": str,
        "DnsIpAddr": str,
        "VpcId": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "Status": DomainControllerStatus,
        "StatusReason": str,
        "LaunchTime": datetime,
        "StatusLastUpdatedDateTime": datetime,
    },
    total=False,
)

EventTopicTypeDef = TypedDict(
    "EventTopicTypeDef",
    {
        "DirectoryId": str,
        "TopicName": str,
        "TopicArn": str,
        "CreatedDateTime": datetime,
        "Status": TopicStatus,
    },
    total=False,
)

IpRouteInfoTypeDef = TypedDict(
    "IpRouteInfoTypeDef",
    {
        "DirectoryId": str,
        "CidrIp": str,
        "IpRouteStatusMsg": IpRouteStatusMsg,
        "AddedDateTime": datetime,
        "IpRouteStatusReason": str,
        "Description": str,
    },
    total=False,
)

LDAPSSettingInfoTypeDef = TypedDict(
    "LDAPSSettingInfoTypeDef",
    {"LDAPSStatus": LDAPSStatus, "LDAPSStatusReason": str, "LastUpdatedDateTime": datetime},
    total=False,
)

LogSubscriptionTypeDef = TypedDict(
    "LogSubscriptionTypeDef",
    {"DirectoryId": str, "LogGroupName": str, "SubscriptionCreatedDateTime": datetime},
    total=False,
)

OwnerDirectoryDescriptionTypeDef = TypedDict(
    "OwnerDirectoryDescriptionTypeDef",
    {
        "DirectoryId": str,
        "AccountId": str,
        "DnsIpAddrs": List[str],
        "VpcSettings": "DirectoryVpcSettingsDescriptionTypeDef",
        "RadiusSettings": "RadiusSettingsTypeDef",
        "RadiusStatus": RadiusStatus,
    },
    total=False,
)

RadiusSettingsTypeDef = TypedDict(
    "RadiusSettingsTypeDef",
    {
        "RadiusServers": List[str],
        "RadiusPort": int,
        "RadiusTimeout": int,
        "RadiusRetries": int,
        "SharedSecret": str,
        "AuthenticationProtocol": RadiusAuthenticationProtocol,
        "DisplayLabel": str,
        "UseSameUsername": bool,
    },
    total=False,
)

RegionDescriptionTypeDef = TypedDict(
    "RegionDescriptionTypeDef",
    {
        "DirectoryId": str,
        "RegionName": str,
        "RegionType": RegionType,
        "Status": DirectoryStage,
        "VpcSettings": "DirectoryVpcSettingsTypeDef",
        "DesiredNumberOfDomainControllers": int,
        "LaunchTime": datetime,
        "StatusLastUpdatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)

RegionsInfoTypeDef = TypedDict(
    "RegionsInfoTypeDef", {"PrimaryRegion": str, "AdditionalRegions": List[str]}, total=False
)

SchemaExtensionInfoTypeDef = TypedDict(
    "SchemaExtensionInfoTypeDef",
    {
        "DirectoryId": str,
        "SchemaExtensionId": str,
        "Description": str,
        "SchemaExtensionStatus": SchemaExtensionStatus,
        "SchemaExtensionStatusReason": str,
        "StartDateTime": datetime,
        "EndDateTime": datetime,
    },
    total=False,
)

SharedDirectoryTypeDef = TypedDict(
    "SharedDirectoryTypeDef",
    {
        "OwnerAccountId": str,
        "OwnerDirectoryId": str,
        "ShareMethod": ShareMethod,
        "SharedAccountId": str,
        "SharedDirectoryId": str,
        "ShareStatus": ShareStatus,
        "ShareNotes": str,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
    },
    total=False,
)

SnapshotLimitsTypeDef = TypedDict(
    "SnapshotLimitsTypeDef",
    {
        "ManualSnapshotsLimit": int,
        "ManualSnapshotsCurrentCount": int,
        "ManualSnapshotsLimitReached": bool,
    },
    total=False,
)

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

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TrustTypeDef = TypedDict(
    "TrustTypeDef",
    {
        "DirectoryId": str,
        "TrustId": str,
        "RemoteDomainName": str,
        "TrustType": TrustType,
        "TrustDirection": TrustDirection,
        "TrustState": TrustState,
        "CreatedDateTime": datetime,
        "LastUpdatedDateTime": datetime,
        "StateLastUpdatedDateTime": datetime,
        "TrustStateReason": str,
        "SelectiveAuth": SelectiveAuth,
    },
    total=False,
)

AcceptSharedDirectoryResultTypeDef = TypedDict(
    "AcceptSharedDirectoryResultTypeDef", {"SharedDirectory": "SharedDirectoryTypeDef"}, total=False
)

ConnectDirectoryResultTypeDef = TypedDict(
    "ConnectDirectoryResultTypeDef", {"DirectoryId": str}, total=False
)

CreateAliasResultTypeDef = TypedDict(
    "CreateAliasResultTypeDef", {"DirectoryId": str, "Alias": str}, total=False
)

CreateComputerResultTypeDef = TypedDict(
    "CreateComputerResultTypeDef", {"Computer": "ComputerTypeDef"}, total=False
)

CreateDirectoryResultTypeDef = TypedDict(
    "CreateDirectoryResultTypeDef", {"DirectoryId": str}, total=False
)

CreateMicrosoftADResultTypeDef = TypedDict(
    "CreateMicrosoftADResultTypeDef", {"DirectoryId": str}, total=False
)

CreateSnapshotResultTypeDef = TypedDict(
    "CreateSnapshotResultTypeDef", {"SnapshotId": str}, total=False
)

CreateTrustResultTypeDef = TypedDict("CreateTrustResultTypeDef", {"TrustId": str}, total=False)

DeleteDirectoryResultTypeDef = TypedDict(
    "DeleteDirectoryResultTypeDef", {"DirectoryId": str}, total=False
)

DeleteSnapshotResultTypeDef = TypedDict(
    "DeleteSnapshotResultTypeDef", {"SnapshotId": str}, total=False
)

DeleteTrustResultTypeDef = TypedDict("DeleteTrustResultTypeDef", {"TrustId": str}, total=False)

DescribeCertificateResultTypeDef = TypedDict(
    "DescribeCertificateResultTypeDef", {"Certificate": "CertificateTypeDef"}, total=False
)

DescribeConditionalForwardersResultTypeDef = TypedDict(
    "DescribeConditionalForwardersResultTypeDef",
    {"ConditionalForwarders": List["ConditionalForwarderTypeDef"]},
    total=False,
)

DescribeDirectoriesResultTypeDef = TypedDict(
    "DescribeDirectoriesResultTypeDef",
    {"DirectoryDescriptions": List["DirectoryDescriptionTypeDef"], "NextToken": str},
    total=False,
)

DescribeDomainControllersResultTypeDef = TypedDict(
    "DescribeDomainControllersResultTypeDef",
    {"DomainControllers": List["DomainControllerTypeDef"], "NextToken": str},
    total=False,
)

DescribeEventTopicsResultTypeDef = TypedDict(
    "DescribeEventTopicsResultTypeDef", {"EventTopics": List["EventTopicTypeDef"]}, total=False
)

DescribeLDAPSSettingsResultTypeDef = TypedDict(
    "DescribeLDAPSSettingsResultTypeDef",
    {"LDAPSSettingsInfo": List["LDAPSSettingInfoTypeDef"], "NextToken": str},
    total=False,
)

DescribeRegionsResultTypeDef = TypedDict(
    "DescribeRegionsResultTypeDef",
    {"RegionsDescription": List["RegionDescriptionTypeDef"], "NextToken": str},
    total=False,
)

DescribeSharedDirectoriesResultTypeDef = TypedDict(
    "DescribeSharedDirectoriesResultTypeDef",
    {"SharedDirectories": List["SharedDirectoryTypeDef"], "NextToken": str},
    total=False,
)

DescribeSnapshotsResultTypeDef = TypedDict(
    "DescribeSnapshotsResultTypeDef",
    {"Snapshots": List["SnapshotTypeDef"], "NextToken": str},
    total=False,
)

DescribeTrustsResultTypeDef = TypedDict(
    "DescribeTrustsResultTypeDef", {"Trusts": List["TrustTypeDef"], "NextToken": str}, total=False
)

DirectoryConnectSettingsTypeDef = TypedDict(
    "DirectoryConnectSettingsTypeDef",
    {"VpcId": str, "SubnetIds": List[str], "CustomerDnsIps": List[str], "CustomerUserName": str},
)

GetDirectoryLimitsResultTypeDef = TypedDict(
    "GetDirectoryLimitsResultTypeDef", {"DirectoryLimits": "DirectoryLimitsTypeDef"}, total=False
)

GetSnapshotLimitsResultTypeDef = TypedDict(
    "GetSnapshotLimitsResultTypeDef", {"SnapshotLimits": "SnapshotLimitsTypeDef"}, total=False
)

IpRouteTypeDef = TypedDict("IpRouteTypeDef", {"CidrIp": str, "Description": str}, total=False)

ListCertificatesResultTypeDef = TypedDict(
    "ListCertificatesResultTypeDef",
    {"NextToken": str, "CertificatesInfo": List["CertificateInfoTypeDef"]},
    total=False,
)

ListIpRoutesResultTypeDef = TypedDict(
    "ListIpRoutesResultTypeDef",
    {"IpRoutesInfo": List["IpRouteInfoTypeDef"], "NextToken": str},
    total=False,
)

ListLogSubscriptionsResultTypeDef = TypedDict(
    "ListLogSubscriptionsResultTypeDef",
    {"LogSubscriptions": List["LogSubscriptionTypeDef"], "NextToken": str},
    total=False,
)

ListSchemaExtensionsResultTypeDef = TypedDict(
    "ListSchemaExtensionsResultTypeDef",
    {"SchemaExtensionsInfo": List["SchemaExtensionInfoTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResultTypeDef = TypedDict(
    "ListTagsForResourceResultTypeDef", {"Tags": List["TagTypeDef"], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RegisterCertificateResultTypeDef = TypedDict(
    "RegisterCertificateResultTypeDef", {"CertificateId": str}, total=False
)

RejectSharedDirectoryResultTypeDef = TypedDict(
    "RejectSharedDirectoryResultTypeDef", {"SharedDirectoryId": str}, total=False
)

ShareDirectoryResultTypeDef = TypedDict(
    "ShareDirectoryResultTypeDef", {"SharedDirectoryId": str}, total=False
)

ShareTargetTypeDef = TypedDict("ShareTargetTypeDef", {"Id": str, "Type": TargetType})

StartSchemaExtensionResultTypeDef = TypedDict(
    "StartSchemaExtensionResultTypeDef", {"SchemaExtensionId": str}, total=False
)

UnshareDirectoryResultTypeDef = TypedDict(
    "UnshareDirectoryResultTypeDef", {"SharedDirectoryId": str}, total=False
)

UnshareTargetTypeDef = TypedDict("UnshareTargetTypeDef", {"Id": str, "Type": TargetType})

UpdateTrustResultTypeDef = TypedDict(
    "UpdateTrustResultTypeDef", {"RequestId": str, "TrustId": str}, total=False
)

VerifyTrustResultTypeDef = TypedDict("VerifyTrustResultTypeDef", {"TrustId": str}, total=False)
