"""
Main interface for mediapackage-vod service type definitions.

Usage::

    ```python
    from mypy_boto3_mediapackage_vod.type_defs import AssetShallowTypeDef

    data: AssetShallowTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_mediapackage_vod.literals import (
    AdMarkers,
    EncryptionMethod,
    ManifestLayout,
    Profile,
    SegmentTemplateFormat,
    StreamOrder,
    __PeriodTriggersElement,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssetShallowTypeDef",
    "AuthorizationTypeDef",
    "CmafEncryptionTypeDef",
    "CmafPackageTypeDef",
    "DashEncryptionTypeDef",
    "DashManifestTypeDef",
    "DashPackageTypeDef",
    "EgressAccessLogsTypeDef",
    "EgressEndpointTypeDef",
    "HlsEncryptionTypeDef",
    "HlsManifestTypeDef",
    "HlsPackageTypeDef",
    "MssEncryptionTypeDef",
    "MssManifestTypeDef",
    "MssPackageTypeDef",
    "PackagingConfigurationTypeDef",
    "PackagingGroupTypeDef",
    "SpekeKeyProviderTypeDef",
    "StreamSelectionTypeDef",
    "ConfigureLogsResponseTypeDef",
    "CreateAssetResponseTypeDef",
    "CreatePackagingConfigurationResponseTypeDef",
    "CreatePackagingGroupResponseTypeDef",
    "DescribeAssetResponseTypeDef",
    "DescribePackagingConfigurationResponseTypeDef",
    "DescribePackagingGroupResponseTypeDef",
    "ListAssetsResponseTypeDef",
    "ListPackagingConfigurationsResponseTypeDef",
    "ListPackagingGroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "UpdatePackagingGroupResponseTypeDef",
)

AssetShallowTypeDef = TypedDict(
    "AssetShallowTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

AuthorizationTypeDef = TypedDict(
    "AuthorizationTypeDef", {"CdnIdentifierSecret": str, "SecretsRoleArn": str}
)

CmafEncryptionTypeDef = TypedDict(
    "CmafEncryptionTypeDef", {"SpekeKeyProvider": "SpekeKeyProviderTypeDef"}
)

_RequiredCmafPackageTypeDef = TypedDict(
    "_RequiredCmafPackageTypeDef", {"HlsManifests": List["HlsManifestTypeDef"]}
)
_OptionalCmafPackageTypeDef = TypedDict(
    "_OptionalCmafPackageTypeDef",
    {
        "Encryption": "CmafEncryptionTypeDef",
        "IncludeEncoderConfigurationInSegments": bool,
        "SegmentDurationSeconds": int,
    },
    total=False,
)


class CmafPackageTypeDef(_RequiredCmafPackageTypeDef, _OptionalCmafPackageTypeDef):
    pass


DashEncryptionTypeDef = TypedDict(
    "DashEncryptionTypeDef", {"SpekeKeyProvider": "SpekeKeyProviderTypeDef"}
)

DashManifestTypeDef = TypedDict(
    "DashManifestTypeDef",
    {
        "ManifestLayout": ManifestLayout,
        "ManifestName": str,
        "MinBufferTimeSeconds": int,
        "Profile": Profile,
        "StreamSelection": "StreamSelectionTypeDef",
    },
    total=False,
)

_RequiredDashPackageTypeDef = TypedDict(
    "_RequiredDashPackageTypeDef", {"DashManifests": List["DashManifestTypeDef"]}
)
_OptionalDashPackageTypeDef = TypedDict(
    "_OptionalDashPackageTypeDef",
    {
        "Encryption": "DashEncryptionTypeDef",
        "IncludeEncoderConfigurationInSegments": bool,
        "PeriodTriggers": List[__PeriodTriggersElement],
        "SegmentDurationSeconds": int,
        "SegmentTemplateFormat": SegmentTemplateFormat,
    },
    total=False,
)


class DashPackageTypeDef(_RequiredDashPackageTypeDef, _OptionalDashPackageTypeDef):
    pass


EgressAccessLogsTypeDef = TypedDict("EgressAccessLogsTypeDef", {"LogGroupName": str}, total=False)

EgressEndpointTypeDef = TypedDict(
    "EgressEndpointTypeDef", {"PackagingConfigurationId": str, "Url": str}, total=False
)

_RequiredHlsEncryptionTypeDef = TypedDict(
    "_RequiredHlsEncryptionTypeDef", {"SpekeKeyProvider": "SpekeKeyProviderTypeDef"}
)
_OptionalHlsEncryptionTypeDef = TypedDict(
    "_OptionalHlsEncryptionTypeDef",
    {"ConstantInitializationVector": str, "EncryptionMethod": EncryptionMethod},
    total=False,
)


class HlsEncryptionTypeDef(_RequiredHlsEncryptionTypeDef, _OptionalHlsEncryptionTypeDef):
    pass


HlsManifestTypeDef = TypedDict(
    "HlsManifestTypeDef",
    {
        "AdMarkers": AdMarkers,
        "IncludeIframeOnlyStream": bool,
        "ManifestName": str,
        "ProgramDateTimeIntervalSeconds": int,
        "RepeatExtXKey": bool,
        "StreamSelection": "StreamSelectionTypeDef",
    },
    total=False,
)

_RequiredHlsPackageTypeDef = TypedDict(
    "_RequiredHlsPackageTypeDef", {"HlsManifests": List["HlsManifestTypeDef"]}
)
_OptionalHlsPackageTypeDef = TypedDict(
    "_OptionalHlsPackageTypeDef",
    {
        "Encryption": "HlsEncryptionTypeDef",
        "SegmentDurationSeconds": int,
        "UseAudioRenditionGroup": bool,
    },
    total=False,
)


class HlsPackageTypeDef(_RequiredHlsPackageTypeDef, _OptionalHlsPackageTypeDef):
    pass


MssEncryptionTypeDef = TypedDict(
    "MssEncryptionTypeDef", {"SpekeKeyProvider": "SpekeKeyProviderTypeDef"}
)

MssManifestTypeDef = TypedDict(
    "MssManifestTypeDef",
    {"ManifestName": str, "StreamSelection": "StreamSelectionTypeDef"},
    total=False,
)

_RequiredMssPackageTypeDef = TypedDict(
    "_RequiredMssPackageTypeDef", {"MssManifests": List["MssManifestTypeDef"]}
)
_OptionalMssPackageTypeDef = TypedDict(
    "_OptionalMssPackageTypeDef",
    {"Encryption": "MssEncryptionTypeDef", "SegmentDurationSeconds": int},
    total=False,
)


class MssPackageTypeDef(_RequiredMssPackageTypeDef, _OptionalMssPackageTypeDef):
    pass


PackagingConfigurationTypeDef = TypedDict(
    "PackagingConfigurationTypeDef",
    {
        "Arn": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "MssPackage": "MssPackageTypeDef",
        "PackagingGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

PackagingGroupTypeDef = TypedDict(
    "PackagingGroupTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

SpekeKeyProviderTypeDef = TypedDict(
    "SpekeKeyProviderTypeDef", {"RoleArn": str, "SystemIds": List[str], "Url": str}
)

StreamSelectionTypeDef = TypedDict(
    "StreamSelectionTypeDef",
    {"MaxVideoBitsPerSecond": int, "MinVideoBitsPerSecond": int, "StreamOrder": StreamOrder},
    total=False,
)

ConfigureLogsResponseTypeDef = TypedDict(
    "ConfigureLogsResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

CreateAssetResponseTypeDef = TypedDict(
    "CreateAssetResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List["EgressEndpointTypeDef"],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

CreatePackagingConfigurationResponseTypeDef = TypedDict(
    "CreatePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "MssPackage": "MssPackageTypeDef",
        "PackagingGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

CreatePackagingGroupResponseTypeDef = TypedDict(
    "CreatePackagingGroupResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

DescribeAssetResponseTypeDef = TypedDict(
    "DescribeAssetResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": str,
        "EgressEndpoints": List["EgressEndpointTypeDef"],
        "Id": str,
        "PackagingGroupId": str,
        "ResourceId": str,
        "SourceArn": str,
        "SourceRoleArn": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

DescribePackagingConfigurationResponseTypeDef = TypedDict(
    "DescribePackagingConfigurationResponseTypeDef",
    {
        "Arn": str,
        "CmafPackage": "CmafPackageTypeDef",
        "DashPackage": "DashPackageTypeDef",
        "HlsPackage": "HlsPackageTypeDef",
        "Id": str,
        "MssPackage": "MssPackageTypeDef",
        "PackagingGroupId": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

DescribePackagingGroupResponseTypeDef = TypedDict(
    "DescribePackagingGroupResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)

ListAssetsResponseTypeDef = TypedDict(
    "ListAssetsResponseTypeDef",
    {"Assets": List["AssetShallowTypeDef"], "NextToken": str},
    total=False,
)

ListPackagingConfigurationsResponseTypeDef = TypedDict(
    "ListPackagingConfigurationsResponseTypeDef",
    {"NextToken": str, "PackagingConfigurations": List["PackagingConfigurationTypeDef"]},
    total=False,
)

ListPackagingGroupsResponseTypeDef = TypedDict(
    "ListPackagingGroupsResponseTypeDef",
    {"NextToken": str, "PackagingGroups": List["PackagingGroupTypeDef"]},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

UpdatePackagingGroupResponseTypeDef = TypedDict(
    "UpdatePackagingGroupResponseTypeDef",
    {
        "Arn": str,
        "Authorization": "AuthorizationTypeDef",
        "DomainName": str,
        "EgressAccessLogs": "EgressAccessLogsTypeDef",
        "Id": str,
        "Tags": Dict[str, str],
    },
    total=False,
)
