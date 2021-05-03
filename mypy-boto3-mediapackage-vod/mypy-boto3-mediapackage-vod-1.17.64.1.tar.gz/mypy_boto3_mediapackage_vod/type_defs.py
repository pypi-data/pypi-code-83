"""
Type annotations for mediapackage-vod service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage_vod/type_defs.html)

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
    "AssetShallowTypeDef",
    "AuthorizationTypeDef",
    "CmafEncryptionTypeDef",
    "CmafPackageTypeDef",
    "ConfigureLogsResponseTypeDef",
    "CreateAssetResponseTypeDef",
    "CreatePackagingConfigurationResponseTypeDef",
    "CreatePackagingGroupResponseTypeDef",
    "DashEncryptionTypeDef",
    "DashManifestTypeDef",
    "DashPackageTypeDef",
    "DescribeAssetResponseTypeDef",
    "DescribePackagingConfigurationResponseTypeDef",
    "DescribePackagingGroupResponseTypeDef",
    "EgressAccessLogsTypeDef",
    "EgressEndpointTypeDef",
    "HlsEncryptionTypeDef",
    "HlsManifestTypeDef",
    "HlsPackageTypeDef",
    "ListAssetsResponseTypeDef",
    "ListPackagingConfigurationsResponseTypeDef",
    "ListPackagingGroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MssEncryptionTypeDef",
    "MssManifestTypeDef",
    "MssPackageTypeDef",
    "PackagingConfigurationTypeDef",
    "PackagingGroupTypeDef",
    "PaginatorConfigTypeDef",
    "SpekeKeyProviderTypeDef",
    "StreamSelectionTypeDef",
    "UpdatePackagingGroupResponseTypeDef",
)


class AssetShallowTypeDef(TypedDict, total=False):
    Arn: str
    CreatedAt: str
    Id: str
    PackagingGroupId: str
    ResourceId: str
    SourceArn: str
    SourceRoleArn: str
    Tags: Dict[str, str]


class AuthorizationTypeDef(TypedDict):
    CdnIdentifierSecret: str
    SecretsRoleArn: str


class CmafEncryptionTypeDef(TypedDict):
    SpekeKeyProvider: "SpekeKeyProviderTypeDef"


class _RequiredCmafPackageTypeDef(TypedDict):
    HlsManifests: List["HlsManifestTypeDef"]


class CmafPackageTypeDef(_RequiredCmafPackageTypeDef, total=False):
    Encryption: "CmafEncryptionTypeDef"
    IncludeEncoderConfigurationInSegments: bool
    SegmentDurationSeconds: int


class ConfigureLogsResponseTypeDef(TypedDict, total=False):
    Arn: str
    Authorization: "AuthorizationTypeDef"
    DomainName: str
    EgressAccessLogs: "EgressAccessLogsTypeDef"
    Id: str
    Tags: Dict[str, str]


class CreateAssetResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreatedAt: str
    EgressEndpoints: List["EgressEndpointTypeDef"]
    Id: str
    PackagingGroupId: str
    ResourceId: str
    SourceArn: str
    SourceRoleArn: str
    Tags: Dict[str, str]


class CreatePackagingConfigurationResponseTypeDef(TypedDict, total=False):
    Arn: str
    CmafPackage: "CmafPackageTypeDef"
    DashPackage: "DashPackageTypeDef"
    HlsPackage: "HlsPackageTypeDef"
    Id: str
    MssPackage: "MssPackageTypeDef"
    PackagingGroupId: str
    Tags: Dict[str, str]


class CreatePackagingGroupResponseTypeDef(TypedDict, total=False):
    Arn: str
    Authorization: "AuthorizationTypeDef"
    DomainName: str
    EgressAccessLogs: "EgressAccessLogsTypeDef"
    Id: str
    Tags: Dict[str, str]


class DashEncryptionTypeDef(TypedDict):
    SpekeKeyProvider: "SpekeKeyProviderTypeDef"


class DashManifestTypeDef(TypedDict, total=False):
    ManifestLayout: ManifestLayout
    ManifestName: str
    MinBufferTimeSeconds: int
    Profile: Profile
    StreamSelection: "StreamSelectionTypeDef"


class _RequiredDashPackageTypeDef(TypedDict):
    DashManifests: List["DashManifestTypeDef"]


class DashPackageTypeDef(_RequiredDashPackageTypeDef, total=False):
    Encryption: "DashEncryptionTypeDef"
    IncludeEncoderConfigurationInSegments: bool
    PeriodTriggers: List[Literal["ADS"]]
    SegmentDurationSeconds: int
    SegmentTemplateFormat: SegmentTemplateFormat


class DescribeAssetResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreatedAt: str
    EgressEndpoints: List["EgressEndpointTypeDef"]
    Id: str
    PackagingGroupId: str
    ResourceId: str
    SourceArn: str
    SourceRoleArn: str
    Tags: Dict[str, str]


class DescribePackagingConfigurationResponseTypeDef(TypedDict, total=False):
    Arn: str
    CmafPackage: "CmafPackageTypeDef"
    DashPackage: "DashPackageTypeDef"
    HlsPackage: "HlsPackageTypeDef"
    Id: str
    MssPackage: "MssPackageTypeDef"
    PackagingGroupId: str
    Tags: Dict[str, str]


class DescribePackagingGroupResponseTypeDef(TypedDict, total=False):
    Arn: str
    Authorization: "AuthorizationTypeDef"
    DomainName: str
    EgressAccessLogs: "EgressAccessLogsTypeDef"
    Id: str
    Tags: Dict[str, str]


class EgressAccessLogsTypeDef(TypedDict, total=False):
    LogGroupName: str


class EgressEndpointTypeDef(TypedDict, total=False):
    PackagingConfigurationId: str
    Url: str


class _RequiredHlsEncryptionTypeDef(TypedDict):
    SpekeKeyProvider: "SpekeKeyProviderTypeDef"


class HlsEncryptionTypeDef(_RequiredHlsEncryptionTypeDef, total=False):
    ConstantInitializationVector: str
    EncryptionMethod: EncryptionMethod


class HlsManifestTypeDef(TypedDict, total=False):
    AdMarkers: AdMarkers
    IncludeIframeOnlyStream: bool
    ManifestName: str
    ProgramDateTimeIntervalSeconds: int
    RepeatExtXKey: bool
    StreamSelection: "StreamSelectionTypeDef"


class _RequiredHlsPackageTypeDef(TypedDict):
    HlsManifests: List["HlsManifestTypeDef"]


class HlsPackageTypeDef(_RequiredHlsPackageTypeDef, total=False):
    Encryption: "HlsEncryptionTypeDef"
    SegmentDurationSeconds: int
    UseAudioRenditionGroup: bool


class ListAssetsResponseTypeDef(TypedDict, total=False):
    Assets: List["AssetShallowTypeDef"]
    NextToken: str


class ListPackagingConfigurationsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    PackagingConfigurations: List["PackagingConfigurationTypeDef"]


class ListPackagingGroupsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    PackagingGroups: List["PackagingGroupTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class MssEncryptionTypeDef(TypedDict):
    SpekeKeyProvider: "SpekeKeyProviderTypeDef"


class MssManifestTypeDef(TypedDict, total=False):
    ManifestName: str
    StreamSelection: "StreamSelectionTypeDef"


class _RequiredMssPackageTypeDef(TypedDict):
    MssManifests: List["MssManifestTypeDef"]


class MssPackageTypeDef(_RequiredMssPackageTypeDef, total=False):
    Encryption: "MssEncryptionTypeDef"
    SegmentDurationSeconds: int


class PackagingConfigurationTypeDef(TypedDict, total=False):
    Arn: str
    CmafPackage: "CmafPackageTypeDef"
    DashPackage: "DashPackageTypeDef"
    HlsPackage: "HlsPackageTypeDef"
    Id: str
    MssPackage: "MssPackageTypeDef"
    PackagingGroupId: str
    Tags: Dict[str, str]


class PackagingGroupTypeDef(TypedDict, total=False):
    Arn: str
    Authorization: "AuthorizationTypeDef"
    DomainName: str
    EgressAccessLogs: "EgressAccessLogsTypeDef"
    Id: str
    Tags: Dict[str, str]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class SpekeKeyProviderTypeDef(TypedDict):
    RoleArn: str
    SystemIds: List[str]
    Url: str


class StreamSelectionTypeDef(TypedDict, total=False):
    MaxVideoBitsPerSecond: int
    MinVideoBitsPerSecond: int
    StreamOrder: StreamOrder


class UpdatePackagingGroupResponseTypeDef(TypedDict, total=False):
    Arn: str
    Authorization: "AuthorizationTypeDef"
    DomainName: str
    EgressAccessLogs: "EgressAccessLogsTypeDef"
    Id: str
    Tags: Dict[str, str]
