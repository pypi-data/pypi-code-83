"""
Type annotations for mediapackage service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediapackage/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediapackage.type_defs import AuthorizationTypeDef

    data: AuthorizationTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_mediapackage.literals import (
    AdMarkers,
    AdsOnDeliveryRestrictions,
    EncryptionMethod,
    ManifestLayout,
    Origination,
    PlaylistType,
    Profile,
    SegmentTemplateFormat,
    Status,
    StreamOrder,
    UtcTiming,
    __AdTriggersElement,
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
    "AuthorizationTypeDef",
    "ChannelTypeDef",
    "CmafEncryptionTypeDef",
    "CmafPackageCreateOrUpdateParametersTypeDef",
    "CmafPackageTypeDef",
    "ConfigureLogsResponseTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateHarvestJobResponseTypeDef",
    "CreateOriginEndpointResponseTypeDef",
    "DashEncryptionTypeDef",
    "DashPackageTypeDef",
    "DescribeChannelResponseTypeDef",
    "DescribeHarvestJobResponseTypeDef",
    "DescribeOriginEndpointResponseTypeDef",
    "EgressAccessLogsTypeDef",
    "EncryptionContractConfigurationTypeDef",
    "HarvestJobTypeDef",
    "HlsEncryptionTypeDef",
    "HlsIngestTypeDef",
    "HlsManifestCreateOrUpdateParametersTypeDef",
    "HlsManifestTypeDef",
    "HlsPackageTypeDef",
    "IngestEndpointTypeDef",
    "IngressAccessLogsTypeDef",
    "ListChannelsResponseTypeDef",
    "ListHarvestJobsResponseTypeDef",
    "ListOriginEndpointsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MssEncryptionTypeDef",
    "MssPackageTypeDef",
    "OriginEndpointTypeDef",
    "PaginatorConfigTypeDef",
    "RotateChannelCredentialsResponseTypeDef",
    "RotateIngestEndpointCredentialsResponseTypeDef",
    "S3DestinationTypeDef",
    "SpekeKeyProviderTypeDef",
    "StreamSelectionTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateOriginEndpointResponseTypeDef",
)


class AuthorizationTypeDef(TypedDict):
    CdnIdentifierSecret: str
    SecretsRoleArn: str


class ChannelTypeDef(TypedDict, total=False):
    Arn: str
    Description: str
    EgressAccessLogs: "EgressAccessLogsTypeDef"
    HlsIngest: "HlsIngestTypeDef"
    Id: str
    IngressAccessLogs: "IngressAccessLogsTypeDef"
    Tags: Dict[str, str]


class _RequiredCmafEncryptionTypeDef(TypedDict):
    SpekeKeyProvider: "SpekeKeyProviderTypeDef"


class CmafEncryptionTypeDef(_RequiredCmafEncryptionTypeDef, total=False):
    ConstantInitializationVector: str
    KeyRotationIntervalSeconds: int


class CmafPackageCreateOrUpdateParametersTypeDef(TypedDict, total=False):
    Encryption: "CmafEncryptionTypeDef"
    HlsManifests: List["HlsManifestCreateOrUpdateParametersTypeDef"]
    SegmentDurationSeconds: int
    SegmentPrefix: str
    StreamSelection: "StreamSelectionTypeDef"


class CmafPackageTypeDef(TypedDict, total=False):
    Encryption: "CmafEncryptionTypeDef"
    HlsManifests: List["HlsManifestTypeDef"]
    SegmentDurationSeconds: int
    SegmentPrefix: str
    StreamSelection: "StreamSelectionTypeDef"


class ConfigureLogsResponseTypeDef(TypedDict, total=False):
    Arn: str
    Description: str
    EgressAccessLogs: "EgressAccessLogsTypeDef"
    HlsIngest: "HlsIngestTypeDef"
    Id: str
    IngressAccessLogs: "IngressAccessLogsTypeDef"
    Tags: Dict[str, str]


class CreateChannelResponseTypeDef(TypedDict, total=False):
    Arn: str
    Description: str
    EgressAccessLogs: "EgressAccessLogsTypeDef"
    HlsIngest: "HlsIngestTypeDef"
    Id: str
    IngressAccessLogs: "IngressAccessLogsTypeDef"
    Tags: Dict[str, str]


class CreateHarvestJobResponseTypeDef(TypedDict, total=False):
    Arn: str
    ChannelId: str
    CreatedAt: str
    EndTime: str
    Id: str
    OriginEndpointId: str
    S3Destination: "S3DestinationTypeDef"
    StartTime: str
    Status: Status


class CreateOriginEndpointResponseTypeDef(TypedDict, total=False):
    Arn: str
    Authorization: "AuthorizationTypeDef"
    ChannelId: str
    CmafPackage: "CmafPackageTypeDef"
    DashPackage: "DashPackageTypeDef"
    Description: str
    HlsPackage: "HlsPackageTypeDef"
    Id: str
    ManifestName: str
    MssPackage: "MssPackageTypeDef"
    Origination: Origination
    StartoverWindowSeconds: int
    Tags: Dict[str, str]
    TimeDelaySeconds: int
    Url: str
    Whitelist: List[str]


class _RequiredDashEncryptionTypeDef(TypedDict):
    SpekeKeyProvider: "SpekeKeyProviderTypeDef"


class DashEncryptionTypeDef(_RequiredDashEncryptionTypeDef, total=False):
    KeyRotationIntervalSeconds: int


class DashPackageTypeDef(TypedDict, total=False):
    AdTriggers: List[__AdTriggersElement]
    AdsOnDeliveryRestrictions: AdsOnDeliveryRestrictions
    Encryption: "DashEncryptionTypeDef"
    ManifestLayout: ManifestLayout
    ManifestWindowSeconds: int
    MinBufferTimeSeconds: int
    MinUpdatePeriodSeconds: int
    PeriodTriggers: List[Literal["ADS"]]
    Profile: Profile
    SegmentDurationSeconds: int
    SegmentTemplateFormat: SegmentTemplateFormat
    StreamSelection: "StreamSelectionTypeDef"
    SuggestedPresentationDelaySeconds: int
    UtcTiming: UtcTiming
    UtcTimingUri: str


class DescribeChannelResponseTypeDef(TypedDict, total=False):
    Arn: str
    Description: str
    EgressAccessLogs: "EgressAccessLogsTypeDef"
    HlsIngest: "HlsIngestTypeDef"
    Id: str
    IngressAccessLogs: "IngressAccessLogsTypeDef"
    Tags: Dict[str, str]


class DescribeHarvestJobResponseTypeDef(TypedDict, total=False):
    Arn: str
    ChannelId: str
    CreatedAt: str
    EndTime: str
    Id: str
    OriginEndpointId: str
    S3Destination: "S3DestinationTypeDef"
    StartTime: str
    Status: Status


class DescribeOriginEndpointResponseTypeDef(TypedDict, total=False):
    Arn: str
    Authorization: "AuthorizationTypeDef"
    ChannelId: str
    CmafPackage: "CmafPackageTypeDef"
    DashPackage: "DashPackageTypeDef"
    Description: str
    HlsPackage: "HlsPackageTypeDef"
    Id: str
    ManifestName: str
    MssPackage: "MssPackageTypeDef"
    Origination: Origination
    StartoverWindowSeconds: int
    Tags: Dict[str, str]
    TimeDelaySeconds: int
    Url: str
    Whitelist: List[str]


class EgressAccessLogsTypeDef(TypedDict, total=False):
    LogGroupName: str


class EncryptionContractConfigurationTypeDef(TypedDict):
    PresetSpeke20Audio: Literal["PRESET-AUDIO-1"]
    PresetSpeke20Video: Literal["PRESET-VIDEO-1"]


class HarvestJobTypeDef(TypedDict, total=False):
    Arn: str
    ChannelId: str
    CreatedAt: str
    EndTime: str
    Id: str
    OriginEndpointId: str
    S3Destination: "S3DestinationTypeDef"
    StartTime: str
    Status: Status


class _RequiredHlsEncryptionTypeDef(TypedDict):
    SpekeKeyProvider: "SpekeKeyProviderTypeDef"


class HlsEncryptionTypeDef(_RequiredHlsEncryptionTypeDef, total=False):
    ConstantInitializationVector: str
    EncryptionMethod: EncryptionMethod
    KeyRotationIntervalSeconds: int
    RepeatExtXKey: bool


class HlsIngestTypeDef(TypedDict, total=False):
    IngestEndpoints: List["IngestEndpointTypeDef"]


class _RequiredHlsManifestCreateOrUpdateParametersTypeDef(TypedDict):
    Id: str


class HlsManifestCreateOrUpdateParametersTypeDef(
    _RequiredHlsManifestCreateOrUpdateParametersTypeDef, total=False
):
    AdMarkers: AdMarkers
    AdTriggers: List[__AdTriggersElement]
    AdsOnDeliveryRestrictions: AdsOnDeliveryRestrictions
    IncludeIframeOnlyStream: bool
    ManifestName: str
    PlaylistType: PlaylistType
    PlaylistWindowSeconds: int
    ProgramDateTimeIntervalSeconds: int


class _RequiredHlsManifestTypeDef(TypedDict):
    Id: str


class HlsManifestTypeDef(_RequiredHlsManifestTypeDef, total=False):
    AdMarkers: AdMarkers
    IncludeIframeOnlyStream: bool
    ManifestName: str
    PlaylistType: PlaylistType
    PlaylistWindowSeconds: int
    ProgramDateTimeIntervalSeconds: int
    Url: str


class HlsPackageTypeDef(TypedDict, total=False):
    AdMarkers: AdMarkers
    AdTriggers: List[__AdTriggersElement]
    AdsOnDeliveryRestrictions: AdsOnDeliveryRestrictions
    Encryption: "HlsEncryptionTypeDef"
    IncludeIframeOnlyStream: bool
    PlaylistType: PlaylistType
    PlaylistWindowSeconds: int
    ProgramDateTimeIntervalSeconds: int
    SegmentDurationSeconds: int
    StreamSelection: "StreamSelectionTypeDef"
    UseAudioRenditionGroup: bool


class IngestEndpointTypeDef(TypedDict, total=False):
    Id: str
    Password: str
    Url: str
    Username: str


class IngressAccessLogsTypeDef(TypedDict, total=False):
    LogGroupName: str


class ListChannelsResponseTypeDef(TypedDict, total=False):
    Channels: List["ChannelTypeDef"]
    NextToken: str


class ListHarvestJobsResponseTypeDef(TypedDict, total=False):
    HarvestJobs: List["HarvestJobTypeDef"]
    NextToken: str


class ListOriginEndpointsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    OriginEndpoints: List["OriginEndpointTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class MssEncryptionTypeDef(TypedDict):
    SpekeKeyProvider: "SpekeKeyProviderTypeDef"


class MssPackageTypeDef(TypedDict, total=False):
    Encryption: "MssEncryptionTypeDef"
    ManifestWindowSeconds: int
    SegmentDurationSeconds: int
    StreamSelection: "StreamSelectionTypeDef"


class OriginEndpointTypeDef(TypedDict, total=False):
    Arn: str
    Authorization: "AuthorizationTypeDef"
    ChannelId: str
    CmafPackage: "CmafPackageTypeDef"
    DashPackage: "DashPackageTypeDef"
    Description: str
    HlsPackage: "HlsPackageTypeDef"
    Id: str
    ManifestName: str
    MssPackage: "MssPackageTypeDef"
    Origination: Origination
    StartoverWindowSeconds: int
    Tags: Dict[str, str]
    TimeDelaySeconds: int
    Url: str
    Whitelist: List[str]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RotateChannelCredentialsResponseTypeDef(TypedDict, total=False):
    Arn: str
    Description: str
    EgressAccessLogs: "EgressAccessLogsTypeDef"
    HlsIngest: "HlsIngestTypeDef"
    Id: str
    IngressAccessLogs: "IngressAccessLogsTypeDef"
    Tags: Dict[str, str]


class RotateIngestEndpointCredentialsResponseTypeDef(TypedDict, total=False):
    Arn: str
    Description: str
    EgressAccessLogs: "EgressAccessLogsTypeDef"
    HlsIngest: "HlsIngestTypeDef"
    Id: str
    IngressAccessLogs: "IngressAccessLogsTypeDef"
    Tags: Dict[str, str]


class S3DestinationTypeDef(TypedDict):
    BucketName: str
    ManifestKey: str
    RoleArn: str


class _RequiredSpekeKeyProviderTypeDef(TypedDict):
    ResourceId: str
    RoleArn: str
    SystemIds: List[str]
    Url: str


class SpekeKeyProviderTypeDef(_RequiredSpekeKeyProviderTypeDef, total=False):
    CertificateArn: str
    EncryptionContractConfiguration: "EncryptionContractConfigurationTypeDef"


class StreamSelectionTypeDef(TypedDict, total=False):
    MaxVideoBitsPerSecond: int
    MinVideoBitsPerSecond: int
    StreamOrder: StreamOrder


class UpdateChannelResponseTypeDef(TypedDict, total=False):
    Arn: str
    Description: str
    EgressAccessLogs: "EgressAccessLogsTypeDef"
    HlsIngest: "HlsIngestTypeDef"
    Id: str
    IngressAccessLogs: "IngressAccessLogsTypeDef"
    Tags: Dict[str, str]


class UpdateOriginEndpointResponseTypeDef(TypedDict, total=False):
    Arn: str
    Authorization: "AuthorizationTypeDef"
    ChannelId: str
    CmafPackage: "CmafPackageTypeDef"
    DashPackage: "DashPackageTypeDef"
    Description: str
    HlsPackage: "HlsPackageTypeDef"
    Id: str
    ManifestName: str
    MssPackage: "MssPackageTypeDef"
    Origination: Origination
    StartoverWindowSeconds: int
    Tags: Dict[str, str]
    TimeDelaySeconds: int
    Url: str
    Whitelist: List[str]
