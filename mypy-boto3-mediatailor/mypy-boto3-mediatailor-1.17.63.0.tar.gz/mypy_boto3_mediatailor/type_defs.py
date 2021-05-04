"""
Type annotations for mediatailor service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/type_defs.html)

Usage::

    ```python
    from mypy_boto3_mediatailor.type_defs import AccessConfigurationTypeDef

    data: AccessConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_mediatailor.literals import (
    ChannelState,
    Mode,
    OriginManifestType,
    RelativePosition,
    TypeType,
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
    "AccessConfigurationTypeDef",
    "AdBreakTypeDef",
    "AdMarkerPassthroughTypeDef",
    "AvailSuppressionTypeDef",
    "BumperTypeDef",
    "CdnConfigurationTypeDef",
    "ChannelTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateProgramResponseTypeDef",
    "CreateSourceLocationResponseTypeDef",
    "CreateVodSourceResponseTypeDef",
    "DashConfigurationForPutTypeDef",
    "DashConfigurationTypeDef",
    "DashPlaylistSettingsTypeDef",
    "DefaultSegmentDeliveryConfigurationTypeDef",
    "DescribeChannelResponseTypeDef",
    "DescribeProgramResponseTypeDef",
    "DescribeSourceLocationResponseTypeDef",
    "DescribeVodSourceResponseTypeDef",
    "GetChannelPolicyResponseTypeDef",
    "GetChannelScheduleResponseTypeDef",
    "GetPlaybackConfigurationResponseTypeDef",
    "HlsConfigurationTypeDef",
    "HlsPlaylistSettingsTypeDef",
    "HttpConfigurationTypeDef",
    "HttpPackageConfigurationTypeDef",
    "ListChannelsResponseTypeDef",
    "ListPlaybackConfigurationsResponseTypeDef",
    "ListSourceLocationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListVodSourcesResponseTypeDef",
    "LivePreRollConfigurationTypeDef",
    "ManifestProcessingRulesTypeDef",
    "PaginatorConfigTypeDef",
    "PlaybackConfigurationTypeDef",
    "PutPlaybackConfigurationResponseTypeDef",
    "RequestOutputItemTypeDef",
    "ResponseOutputItemTypeDef",
    "ScheduleConfigurationTypeDef",
    "ScheduleEntryTypeDef",
    "SlateSourceTypeDef",
    "SourceLocationTypeDef",
    "SpliceInsertMessageTypeDef",
    "TransitionTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateSourceLocationResponseTypeDef",
    "UpdateVodSourceResponseTypeDef",
    "VodSourceTypeDef",
)


class AccessConfigurationTypeDef(TypedDict, total=False):
    AccessType: Literal["S3_SIGV4"]


class AdBreakTypeDef(TypedDict, total=False):
    MessageType: Literal["SPLICE_INSERT"]
    OffsetMillis: int
    Slate: "SlateSourceTypeDef"
    SpliceInsertMessage: "SpliceInsertMessageTypeDef"


class AdMarkerPassthroughTypeDef(TypedDict, total=False):
    Enabled: bool


class AvailSuppressionTypeDef(TypedDict, total=False):
    Mode: Mode
    Value: str


class BumperTypeDef(TypedDict, total=False):
    EndUrl: str
    StartUrl: str


class CdnConfigurationTypeDef(TypedDict, total=False):
    AdSegmentUrlPrefix: str
    ContentSegmentUrlPrefix: str


class _RequiredChannelTypeDef(TypedDict):
    Arn: str
    ChannelName: str
    ChannelState: str
    Outputs: List["ResponseOutputItemTypeDef"]
    PlaybackMode: str


class ChannelTypeDef(_RequiredChannelTypeDef, total=False):
    CreationTime: datetime
    LastModifiedTime: datetime
    Tags: Dict[str, str]


class CreateChannelResponseTypeDef(TypedDict, total=False):
    Arn: str
    ChannelName: str
    ChannelState: ChannelState
    CreationTime: datetime
    LastModifiedTime: datetime
    Outputs: List["ResponseOutputItemTypeDef"]
    PlaybackMode: str
    Tags: Dict[str, str]


class CreateProgramResponseTypeDef(TypedDict, total=False):
    AdBreaks: List["AdBreakTypeDef"]
    Arn: str
    ChannelName: str
    CreationTime: datetime
    ProgramName: str
    SourceLocationName: str
    VodSourceName: str


class CreateSourceLocationResponseTypeDef(TypedDict, total=False):
    AccessConfiguration: "AccessConfigurationTypeDef"
    Arn: str
    CreationTime: datetime
    DefaultSegmentDeliveryConfiguration: "DefaultSegmentDeliveryConfigurationTypeDef"
    HttpConfiguration: "HttpConfigurationTypeDef"
    LastModifiedTime: datetime
    SourceLocationName: str
    Tags: Dict[str, str]


class CreateVodSourceResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List["HttpPackageConfigurationTypeDef"]
    LastModifiedTime: datetime
    SourceLocationName: str
    Tags: Dict[str, str]
    VodSourceName: str


class DashConfigurationForPutTypeDef(TypedDict, total=False):
    MpdLocation: str
    OriginManifestType: OriginManifestType


class DashConfigurationTypeDef(TypedDict, total=False):
    ManifestEndpointPrefix: str
    MpdLocation: str
    OriginManifestType: OriginManifestType


class DashPlaylistSettingsTypeDef(TypedDict, total=False):
    ManifestWindowSeconds: int
    MinBufferTimeSeconds: int
    MinUpdatePeriodSeconds: int
    SuggestedPresentationDelaySeconds: int


class DefaultSegmentDeliveryConfigurationTypeDef(TypedDict, total=False):
    BaseUrl: str


class DescribeChannelResponseTypeDef(TypedDict, total=False):
    Arn: str
    ChannelName: str
    ChannelState: ChannelState
    CreationTime: datetime
    LastModifiedTime: datetime
    Outputs: List["ResponseOutputItemTypeDef"]
    PlaybackMode: str
    Tags: Dict[str, str]


class DescribeProgramResponseTypeDef(TypedDict, total=False):
    AdBreaks: List["AdBreakTypeDef"]
    Arn: str
    ChannelName: str
    CreationTime: datetime
    ProgramName: str
    SourceLocationName: str
    VodSourceName: str


class DescribeSourceLocationResponseTypeDef(TypedDict, total=False):
    AccessConfiguration: "AccessConfigurationTypeDef"
    Arn: str
    CreationTime: datetime
    DefaultSegmentDeliveryConfiguration: "DefaultSegmentDeliveryConfigurationTypeDef"
    HttpConfiguration: "HttpConfigurationTypeDef"
    LastModifiedTime: datetime
    SourceLocationName: str
    Tags: Dict[str, str]


class DescribeVodSourceResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List["HttpPackageConfigurationTypeDef"]
    LastModifiedTime: datetime
    SourceLocationName: str
    Tags: Dict[str, str]
    VodSourceName: str


class GetChannelPolicyResponseTypeDef(TypedDict, total=False):
    Policy: str


class GetChannelScheduleResponseTypeDef(TypedDict, total=False):
    Items: List["ScheduleEntryTypeDef"]
    NextToken: str


class GetPlaybackConfigurationResponseTypeDef(TypedDict, total=False):
    AdDecisionServerUrl: str
    AvailSuppression: "AvailSuppressionTypeDef"
    Bumper: "BumperTypeDef"
    CdnConfiguration: "CdnConfigurationTypeDef"
    ConfigurationAliases: Dict[str, Dict[str, str]]
    DashConfiguration: "DashConfigurationTypeDef"
    HlsConfiguration: "HlsConfigurationTypeDef"
    LivePreRollConfiguration: "LivePreRollConfigurationTypeDef"
    ManifestProcessingRules: "ManifestProcessingRulesTypeDef"
    Name: str
    PersonalizationThresholdSeconds: int
    PlaybackConfigurationArn: str
    PlaybackEndpointPrefix: str
    SessionInitializationEndpointPrefix: str
    SlateAdUrl: str
    Tags: Dict[str, str]
    TranscodeProfileName: str
    VideoContentSourceUrl: str


class HlsConfigurationTypeDef(TypedDict, total=False):
    ManifestEndpointPrefix: str


class HlsPlaylistSettingsTypeDef(TypedDict, total=False):
    ManifestWindowSeconds: int


class HttpConfigurationTypeDef(TypedDict):
    BaseUrl: str


HttpPackageConfigurationTypeDef = TypedDict(
    "HttpPackageConfigurationTypeDef", {"Path": str, "SourceGroup": str, "Type": TypeType}
)


class ListChannelsResponseTypeDef(TypedDict, total=False):
    Items: List["ChannelTypeDef"]
    NextToken: str


class ListPlaybackConfigurationsResponseTypeDef(TypedDict, total=False):
    Items: List["PlaybackConfigurationTypeDef"]
    NextToken: str


class ListSourceLocationsResponseTypeDef(TypedDict, total=False):
    Items: List["SourceLocationTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class ListVodSourcesResponseTypeDef(TypedDict, total=False):
    Items: List["VodSourceTypeDef"]
    NextToken: str


class LivePreRollConfigurationTypeDef(TypedDict, total=False):
    AdDecisionServerUrl: str
    MaxDurationSeconds: int


class ManifestProcessingRulesTypeDef(TypedDict, total=False):
    AdMarkerPassthrough: "AdMarkerPassthroughTypeDef"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PlaybackConfigurationTypeDef(TypedDict, total=False):
    AdDecisionServerUrl: str
    AvailSuppression: "AvailSuppressionTypeDef"
    Bumper: "BumperTypeDef"
    CdnConfiguration: "CdnConfigurationTypeDef"
    ConfigurationAliases: Dict[str, Dict[str, str]]
    DashConfiguration: "DashConfigurationTypeDef"
    HlsConfiguration: "HlsConfigurationTypeDef"
    LivePreRollConfiguration: "LivePreRollConfigurationTypeDef"
    ManifestProcessingRules: "ManifestProcessingRulesTypeDef"
    Name: str
    PersonalizationThresholdSeconds: int
    PlaybackConfigurationArn: str
    PlaybackEndpointPrefix: str
    SessionInitializationEndpointPrefix: str
    SlateAdUrl: str
    Tags: Dict[str, str]
    TranscodeProfileName: str
    VideoContentSourceUrl: str


class PutPlaybackConfigurationResponseTypeDef(TypedDict, total=False):
    AdDecisionServerUrl: str
    AvailSuppression: "AvailSuppressionTypeDef"
    Bumper: "BumperTypeDef"
    CdnConfiguration: "CdnConfigurationTypeDef"
    ConfigurationAliases: Dict[str, Dict[str, str]]
    DashConfiguration: "DashConfigurationTypeDef"
    HlsConfiguration: "HlsConfigurationTypeDef"
    LivePreRollConfiguration: "LivePreRollConfigurationTypeDef"
    ManifestProcessingRules: "ManifestProcessingRulesTypeDef"
    Name: str
    PersonalizationThresholdSeconds: int
    PlaybackConfigurationArn: str
    PlaybackEndpointPrefix: str
    SessionInitializationEndpointPrefix: str
    SlateAdUrl: str
    Tags: Dict[str, str]
    TranscodeProfileName: str
    VideoContentSourceUrl: str


class _RequiredRequestOutputItemTypeDef(TypedDict):
    ManifestName: str
    SourceGroup: str


class RequestOutputItemTypeDef(_RequiredRequestOutputItemTypeDef, total=False):
    DashPlaylistSettings: "DashPlaylistSettingsTypeDef"
    HlsPlaylistSettings: "HlsPlaylistSettingsTypeDef"


class _RequiredResponseOutputItemTypeDef(TypedDict):
    ManifestName: str
    PlaybackUrl: str
    SourceGroup: str


class ResponseOutputItemTypeDef(_RequiredResponseOutputItemTypeDef, total=False):
    DashPlaylistSettings: "DashPlaylistSettingsTypeDef"
    HlsPlaylistSettings: "HlsPlaylistSettingsTypeDef"


class ScheduleConfigurationTypeDef(TypedDict):
    Transition: "TransitionTypeDef"


class _RequiredScheduleEntryTypeDef(TypedDict):
    Arn: str
    ChannelName: str
    ProgramName: str
    SourceLocationName: str
    VodSourceName: str


class ScheduleEntryTypeDef(_RequiredScheduleEntryTypeDef, total=False):
    ApproximateDurationSeconds: int
    ApproximateStartTime: datetime


class SlateSourceTypeDef(TypedDict, total=False):
    SourceLocationName: str
    VodSourceName: str


class _RequiredSourceLocationTypeDef(TypedDict):
    Arn: str
    HttpConfiguration: "HttpConfigurationTypeDef"
    SourceLocationName: str


class SourceLocationTypeDef(_RequiredSourceLocationTypeDef, total=False):
    AccessConfiguration: "AccessConfigurationTypeDef"
    CreationTime: datetime
    DefaultSegmentDeliveryConfiguration: "DefaultSegmentDeliveryConfigurationTypeDef"
    LastModifiedTime: datetime
    Tags: Dict[str, str]


class SpliceInsertMessageTypeDef(TypedDict, total=False):
    AvailNum: int
    AvailsExpected: int
    SpliceEventId: int
    UniqueProgramId: int


_RequiredTransitionTypeDef = TypedDict(
    "_RequiredTransitionTypeDef", {"RelativePosition": RelativePosition, "Type": str}
)
_OptionalTransitionTypeDef = TypedDict(
    "_OptionalTransitionTypeDef", {"RelativeProgram": str}, total=False
)


class TransitionTypeDef(_RequiredTransitionTypeDef, _OptionalTransitionTypeDef):
    pass


class UpdateChannelResponseTypeDef(TypedDict, total=False):
    Arn: str
    ChannelName: str
    ChannelState: ChannelState
    CreationTime: datetime
    LastModifiedTime: datetime
    Outputs: List["ResponseOutputItemTypeDef"]
    PlaybackMode: str
    Tags: Dict[str, str]


class UpdateSourceLocationResponseTypeDef(TypedDict, total=False):
    AccessConfiguration: "AccessConfigurationTypeDef"
    Arn: str
    CreationTime: datetime
    DefaultSegmentDeliveryConfiguration: "DefaultSegmentDeliveryConfigurationTypeDef"
    HttpConfiguration: "HttpConfigurationTypeDef"
    LastModifiedTime: datetime
    SourceLocationName: str
    Tags: Dict[str, str]


class UpdateVodSourceResponseTypeDef(TypedDict, total=False):
    Arn: str
    CreationTime: datetime
    HttpPackageConfigurations: List["HttpPackageConfigurationTypeDef"]
    LastModifiedTime: datetime
    SourceLocationName: str
    Tags: Dict[str, str]
    VodSourceName: str


class _RequiredVodSourceTypeDef(TypedDict):
    Arn: str
    HttpPackageConfigurations: List["HttpPackageConfigurationTypeDef"]
    SourceLocationName: str
    VodSourceName: str


class VodSourceTypeDef(_RequiredVodSourceTypeDef, total=False):
    CreationTime: datetime
    LastModifiedTime: datetime
    Tags: Dict[str, str]
