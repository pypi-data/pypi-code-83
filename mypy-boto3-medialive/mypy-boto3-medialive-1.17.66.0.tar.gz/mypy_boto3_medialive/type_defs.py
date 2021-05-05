"""
Type annotations for medialive service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/type_defs.html)

Usage::

    ```python
    from mypy_boto3_medialive.type_defs import AacSettingsTypeDef

    data: AacSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from botocore.response import StreamingBody

from mypy_boto3_medialive.literals import (
    AacCodingMode,
    AacInputType,
    AacProfile,
    AacRateControlMode,
    AacRawFormat,
    AacSpec,
    AacVbrQuality,
    Ac3BitstreamMode,
    Ac3CodingMode,
    Ac3DrcProfile,
    Ac3LfeFilter,
    Ac3MetadataControl,
    AfdSignaling,
    AudioDescriptionAudioTypeControl,
    AudioDescriptionLanguageCodeControl,
    AudioLanguageSelectionPolicy,
    AudioNormalizationAlgorithm,
    AudioOnlyHlsSegmentType,
    AudioOnlyHlsTrackType,
    AudioType,
    AuthenticationScheme,
    AvailBlankingState,
    BlackoutSlateNetworkEndBlackout,
    BlackoutSlateState,
    BurnInAlignment,
    BurnInBackgroundColor,
    BurnInFontColor,
    BurnInOutlineColor,
    BurnInShadowColor,
    BurnInTeletextGridControl,
    CdiInputResolution,
    ChannelClass,
    ChannelState,
    DeviceSettingsSyncState,
    DeviceUpdateStatus,
    DvbSdtOutputSdt,
    DvbSubDestinationAlignment,
    DvbSubDestinationBackgroundColor,
    DvbSubDestinationFontColor,
    DvbSubDestinationOutlineColor,
    DvbSubDestinationShadowColor,
    DvbSubDestinationTeletextGridControl,
    Eac3AttenuationControl,
    Eac3BitstreamMode,
    Eac3CodingMode,
    Eac3DcFilter,
    Eac3DrcLine,
    Eac3DrcRf,
    Eac3LfeControl,
    Eac3LfeFilter,
    Eac3MetadataControl,
    Eac3PassthroughControl,
    Eac3PhaseControl,
    Eac3StereoDownmix,
    Eac3SurroundExMode,
    Eac3SurroundMode,
    EbuTtDDestinationStyleControl,
    EbuTtDFillLineGapControl,
    EmbeddedConvert608To708,
    EmbeddedScte20Detection,
    FeatureActivationsInputPrepareScheduleActions,
    FecOutputIncludeFec,
    FixedAfd,
    Fmp4NielsenId3Behavior,
    Fmp4TimedMetadataBehavior,
    FollowPoint,
    FrameCaptureIntervalUnit,
    GlobalConfigurationInputEndAction,
    GlobalConfigurationLowFramerateInputs,
    GlobalConfigurationOutputLockingMode,
    GlobalConfigurationOutputTimingSource,
    H264AdaptiveQuantization,
    H264ColorMetadata,
    H264EntropyEncoding,
    H264FlickerAq,
    H264ForceFieldPictures,
    H264FramerateControl,
    H264GopBReference,
    H264GopSizeUnits,
    H264Level,
    H264LookAheadRateControl,
    H264ParControl,
    H264Profile,
    H264QualityLevel,
    H264RateControlMode,
    H264ScanType,
    H264SceneChangeDetect,
    H264SpatialAq,
    H264SubGopLength,
    H264Syntax,
    H264TemporalAq,
    H264TimecodeInsertionBehavior,
    H265AdaptiveQuantization,
    H265AlternativeTransferFunction,
    H265ColorMetadata,
    H265FlickerAq,
    H265GopSizeUnits,
    H265Level,
    H265LookAheadRateControl,
    H265Profile,
    H265RateControlMode,
    H265ScanType,
    H265SceneChangeDetect,
    H265Tier,
    H265TimecodeInsertionBehavior,
    HlsAdMarkers,
    HlsAkamaiHttpTransferMode,
    HlsCaptionLanguageSetting,
    HlsClientCache,
    HlsCodecSpecification,
    HlsDirectoryStructure,
    HlsDiscontinuityTags,
    HlsEncryptionType,
    HlsH265PackagingType,
    HlsId3SegmentTaggingState,
    HlsIncompleteSegmentBehavior,
    HlsIvInManifest,
    HlsIvSource,
    HlsManifestCompression,
    HlsManifestDurationFormat,
    HlsMode,
    HlsOutputSelection,
    HlsProgramDateTime,
    HlsRedundantManifest,
    HlsSegmentationMode,
    HlsStreamInfResolution,
    HlsTimedMetadataId3Frame,
    HlsTsFileMode,
    HlsWebdavHttpTransferMode,
    IFrameOnlyPlaylistType,
    InputClass,
    InputCodec,
    InputDeblockFilter,
    InputDenoiseFilter,
    InputDeviceActiveInput,
    InputDeviceConfiguredInput,
    InputDeviceConnectionState,
    InputDeviceIpScheme,
    InputDeviceScanType,
    InputDeviceState,
    InputDeviceTransferType,
    InputFilter,
    InputLossActionForHlsOut,
    InputLossActionForMsSmoothOut,
    InputLossActionForRtmpOut,
    InputLossActionForUdpOut,
    InputLossImageType,
    InputMaximumBitrate,
    InputPreference,
    InputResolution,
    InputSecurityGroupState,
    InputSourceEndBehavior,
    InputSourceType,
    InputState,
    InputTimecodeSource,
    InputType,
    LastFrameClippingBehavior,
    LogLevel,
    M2tsAbsentInputAudioBehavior,
    M2tsArib,
    M2tsAribCaptionsPidControl,
    M2tsAudioBufferModel,
    M2tsAudioInterval,
    M2tsAudioStreamType,
    M2tsBufferModel,
    M2tsCcDescriptor,
    M2tsEbifControl,
    M2tsEbpPlacement,
    M2tsEsRateInPes,
    M2tsKlv,
    M2tsNielsenId3Behavior,
    M2tsPcrControl,
    M2tsRateMode,
    M2tsScte35Control,
    M2tsSegmentationMarkers,
    M2tsSegmentationStyle,
    M2tsTimedMetadataBehavior,
    M3u8NielsenId3Behavior,
    M3u8PcrControl,
    M3u8Scte35Behavior,
    M3u8TimedMetadataBehavior,
    MotionGraphicsInsertion,
    Mp2CodingMode,
    Mpeg2AdaptiveQuantization,
    Mpeg2ColorMetadata,
    Mpeg2ColorSpace,
    Mpeg2DisplayRatio,
    Mpeg2GopSizeUnits,
    Mpeg2ScanType,
    Mpeg2SubGopLength,
    Mpeg2TimecodeInsertionBehavior,
    MsSmoothH265PackagingType,
    MultiplexState,
    NetworkInputServerValidation,
    NielsenPcmToId3TaggingState,
    PipelineId,
    PreferredChannelPipeline,
    ReservationCodec,
    ReservationMaximumBitrate,
    ReservationMaximumFramerate,
    ReservationResolution,
    ReservationResourceType,
    ReservationSpecialFeature,
    ReservationState,
    ReservationVideoQuality,
    RtmpCacheFullBehavior,
    RtmpCaptionData,
    RtmpOutputCertificateMode,
    S3CannedAcl,
    Scte20Convert608To708,
    Scte35AposNoRegionalBlackoutBehavior,
    Scte35AposWebDeliveryAllowedBehavior,
    Scte35ArchiveAllowedFlag,
    Scte35DeviceRestrictions,
    Scte35NoRegionalBlackoutFlag,
    Scte35SegmentationCancelIndicator,
    Scte35SpliceInsertNoRegionalBlackoutBehavior,
    Scte35SpliceInsertWebDeliveryAllowedBehavior,
    Scte35WebDeliveryAllowedFlag,
    SmoothGroupAudioOnlyTimecodeControl,
    SmoothGroupCertificateMode,
    SmoothGroupEventIdMode,
    SmoothGroupEventStopBehavior,
    SmoothGroupSegmentationMode,
    SmoothGroupSparseTrackType,
    SmoothGroupStreamManifestBehavior,
    SmoothGroupTimestampOffsetMode,
    Smpte2038DataPreference,
    TemporalFilterPostFilterSharpening,
    TemporalFilterStrength,
    TimecodeConfigSource,
    TtmlDestinationStyleControl,
    UdpTimedMetadataId3Frame,
    VideoDescriptionRespondToAfd,
    VideoDescriptionScalingBehavior,
    VideoSelectorColorSpace,
    VideoSelectorColorSpaceUsage,
    WavCodingMode,
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
    "AacSettingsTypeDef",
    "Ac3SettingsTypeDef",
    "AncillarySourceSettingsTypeDef",
    "ArchiveCdnSettingsTypeDef",
    "ArchiveContainerSettingsTypeDef",
    "ArchiveGroupSettingsTypeDef",
    "ArchiveOutputSettingsTypeDef",
    "ArchiveS3SettingsTypeDef",
    "AudioChannelMappingTypeDef",
    "AudioCodecSettingsTypeDef",
    "AudioDescriptionTypeDef",
    "AudioLanguageSelectionTypeDef",
    "AudioNormalizationSettingsTypeDef",
    "AudioOnlyHlsSettingsTypeDef",
    "AudioPidSelectionTypeDef",
    "AudioSelectorSettingsTypeDef",
    "AudioSelectorTypeDef",
    "AudioSilenceFailoverSettingsTypeDef",
    "AudioTrackSelectionTypeDef",
    "AudioTrackTypeDef",
    "AutomaticInputFailoverSettingsTypeDef",
    "AvailBlankingTypeDef",
    "AvailConfigurationTypeDef",
    "AvailSettingsTypeDef",
    "BatchDeleteResponseTypeDef",
    "BatchFailedResultModelTypeDef",
    "BatchScheduleActionCreateRequestTypeDef",
    "BatchScheduleActionCreateResultTypeDef",
    "BatchScheduleActionDeleteRequestTypeDef",
    "BatchScheduleActionDeleteResultTypeDef",
    "BatchStartResponseTypeDef",
    "BatchStopResponseTypeDef",
    "BatchSuccessfulResultModelTypeDef",
    "BatchUpdateScheduleResponseTypeDef",
    "BlackoutSlateTypeDef",
    "BurnInDestinationSettingsTypeDef",
    "CaptionDescriptionTypeDef",
    "CaptionDestinationSettingsTypeDef",
    "CaptionLanguageMappingTypeDef",
    "CaptionRectangleTypeDef",
    "CaptionSelectorSettingsTypeDef",
    "CaptionSelectorTypeDef",
    "CdiInputSpecificationTypeDef",
    "ChannelEgressEndpointTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateInputResponseTypeDef",
    "CreateInputSecurityGroupResponseTypeDef",
    "CreateMultiplexProgramResponseTypeDef",
    "CreateMultiplexResponseTypeDef",
    "CreatePartnerInputResponseTypeDef",
    "DeleteChannelResponseTypeDef",
    "DeleteMultiplexProgramResponseTypeDef",
    "DeleteMultiplexResponseTypeDef",
    "DeleteReservationResponseTypeDef",
    "DescribeChannelResponseTypeDef",
    "DescribeInputDeviceResponseTypeDef",
    "DescribeInputDeviceThumbnailResponseTypeDef",
    "DescribeInputResponseTypeDef",
    "DescribeInputSecurityGroupResponseTypeDef",
    "DescribeMultiplexProgramResponseTypeDef",
    "DescribeMultiplexResponseTypeDef",
    "DescribeOfferingResponseTypeDef",
    "DescribeReservationResponseTypeDef",
    "DescribeScheduleResponseTypeDef",
    "DvbNitSettingsTypeDef",
    "DvbSdtSettingsTypeDef",
    "DvbSubDestinationSettingsTypeDef",
    "DvbSubSourceSettingsTypeDef",
    "DvbTdtSettingsTypeDef",
    "Eac3SettingsTypeDef",
    "EbuTtDDestinationSettingsTypeDef",
    "EmbeddedSourceSettingsTypeDef",
    "EncoderSettingsTypeDef",
    "FailoverConditionSettingsTypeDef",
    "FailoverConditionTypeDef",
    "FeatureActivationsTypeDef",
    "FecOutputSettingsTypeDef",
    "FixedModeScheduleActionStartSettingsTypeDef",
    "Fmp4HlsSettingsTypeDef",
    "FollowModeScheduleActionStartSettingsTypeDef",
    "FrameCaptureCdnSettingsTypeDef",
    "FrameCaptureGroupSettingsTypeDef",
    "FrameCaptureOutputSettingsTypeDef",
    "FrameCaptureS3SettingsTypeDef",
    "FrameCaptureSettingsTypeDef",
    "GlobalConfigurationTypeDef",
    "H264ColorSpaceSettingsTypeDef",
    "H264FilterSettingsTypeDef",
    "H264SettingsTypeDef",
    "H265ColorSpaceSettingsTypeDef",
    "H265FilterSettingsTypeDef",
    "H265SettingsTypeDef",
    "Hdr10SettingsTypeDef",
    "HlsAkamaiSettingsTypeDef",
    "HlsBasicPutSettingsTypeDef",
    "HlsCdnSettingsTypeDef",
    "HlsGroupSettingsTypeDef",
    "HlsId3SegmentTaggingScheduleActionSettingsTypeDef",
    "HlsInputSettingsTypeDef",
    "HlsMediaStoreSettingsTypeDef",
    "HlsOutputSettingsTypeDef",
    "HlsS3SettingsTypeDef",
    "HlsSettingsTypeDef",
    "HlsTimedMetadataScheduleActionSettingsTypeDef",
    "HlsWebdavSettingsTypeDef",
    "InputAttachmentTypeDef",
    "InputChannelLevelTypeDef",
    "InputClippingSettingsTypeDef",
    "InputDestinationRequestTypeDef",
    "InputDestinationTypeDef",
    "InputDestinationVpcTypeDef",
    "InputDeviceConfigurableSettingsTypeDef",
    "InputDeviceHdSettingsTypeDef",
    "InputDeviceNetworkSettingsTypeDef",
    "InputDeviceRequestTypeDef",
    "InputDeviceSettingsTypeDef",
    "InputDeviceSummaryTypeDef",
    "InputDeviceUhdSettingsTypeDef",
    "InputLocationTypeDef",
    "InputLossBehaviorTypeDef",
    "InputLossFailoverSettingsTypeDef",
    "InputPrepareScheduleActionSettingsTypeDef",
    "InputSecurityGroupTypeDef",
    "InputSettingsTypeDef",
    "InputSourceRequestTypeDef",
    "InputSourceTypeDef",
    "InputSpecificationTypeDef",
    "InputSwitchScheduleActionSettingsTypeDef",
    "InputTypeDef",
    "InputVpcRequestTypeDef",
    "InputWhitelistRuleCidrTypeDef",
    "InputWhitelistRuleTypeDef",
    "KeyProviderSettingsTypeDef",
    "ListChannelsResponseTypeDef",
    "ListInputDeviceTransfersResponseTypeDef",
    "ListInputDevicesResponseTypeDef",
    "ListInputSecurityGroupsResponseTypeDef",
    "ListInputsResponseTypeDef",
    "ListMultiplexProgramsResponseTypeDef",
    "ListMultiplexesResponseTypeDef",
    "ListOfferingsResponseTypeDef",
    "ListReservationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "M2tsSettingsTypeDef",
    "M3u8SettingsTypeDef",
    "MediaConnectFlowRequestTypeDef",
    "MediaConnectFlowTypeDef",
    "MediaPackageGroupSettingsTypeDef",
    "MediaPackageOutputDestinationSettingsTypeDef",
    "MotionGraphicsActivateScheduleActionSettingsTypeDef",
    "MotionGraphicsConfigurationTypeDef",
    "MotionGraphicsSettingsTypeDef",
    "Mp2SettingsTypeDef",
    "Mpeg2FilterSettingsTypeDef",
    "Mpeg2SettingsTypeDef",
    "MsSmoothGroupSettingsTypeDef",
    "MsSmoothOutputSettingsTypeDef",
    "MultiplexMediaConnectOutputDestinationSettingsTypeDef",
    "MultiplexOutputDestinationTypeDef",
    "MultiplexOutputSettingsTypeDef",
    "MultiplexProgramChannelDestinationSettingsTypeDef",
    "MultiplexProgramPacketIdentifiersMapTypeDef",
    "MultiplexProgramPipelineDetailTypeDef",
    "MultiplexProgramServiceDescriptorTypeDef",
    "MultiplexProgramSettingsTypeDef",
    "MultiplexProgramSummaryTypeDef",
    "MultiplexProgramTypeDef",
    "MultiplexSettingsSummaryTypeDef",
    "MultiplexSettingsTypeDef",
    "MultiplexStatmuxVideoSettingsTypeDef",
    "MultiplexSummaryTypeDef",
    "MultiplexTypeDef",
    "MultiplexVideoSettingsTypeDef",
    "NetworkInputSettingsTypeDef",
    "NielsenConfigurationTypeDef",
    "OfferingTypeDef",
    "OutputDestinationSettingsTypeDef",
    "OutputDestinationTypeDef",
    "OutputGroupSettingsTypeDef",
    "OutputGroupTypeDef",
    "OutputLocationRefTypeDef",
    "OutputSettingsTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PauseStateScheduleActionSettingsTypeDef",
    "PipelineDetailTypeDef",
    "PipelinePauseStateSettingsTypeDef",
    "PurchaseOfferingResponseTypeDef",
    "RemixSettingsTypeDef",
    "ReservationResourceSpecificationTypeDef",
    "ReservationTypeDef",
    "ResponseMetadata",
    "RtmpGroupSettingsTypeDef",
    "RtmpOutputSettingsTypeDef",
    "ScheduleActionSettingsTypeDef",
    "ScheduleActionStartSettingsTypeDef",
    "ScheduleActionTypeDef",
    "Scte20SourceSettingsTypeDef",
    "Scte27SourceSettingsTypeDef",
    "Scte35DeliveryRestrictionsTypeDef",
    "Scte35DescriptorSettingsTypeDef",
    "Scte35DescriptorTypeDef",
    "Scte35ReturnToNetworkScheduleActionSettingsTypeDef",
    "Scte35SegmentationDescriptorTypeDef",
    "Scte35SpliceInsertScheduleActionSettingsTypeDef",
    "Scte35SpliceInsertTypeDef",
    "Scte35TimeSignalAposTypeDef",
    "Scte35TimeSignalScheduleActionSettingsTypeDef",
    "StandardHlsSettingsTypeDef",
    "StartChannelResponseTypeDef",
    "StartMultiplexResponseTypeDef",
    "StartTimecodeTypeDef",
    "StaticImageActivateScheduleActionSettingsTypeDef",
    "StaticImageDeactivateScheduleActionSettingsTypeDef",
    "StaticKeySettingsTypeDef",
    "StopChannelResponseTypeDef",
    "StopMultiplexResponseTypeDef",
    "StopTimecodeTypeDef",
    "TeletextSourceSettingsTypeDef",
    "TemporalFilterSettingsTypeDef",
    "TimecodeConfigTypeDef",
    "TransferringInputDeviceSummaryTypeDef",
    "TtmlDestinationSettingsTypeDef",
    "UdpContainerSettingsTypeDef",
    "UdpGroupSettingsTypeDef",
    "UdpOutputSettingsTypeDef",
    "UpdateChannelClassResponseTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateInputDeviceResponseTypeDef",
    "UpdateInputResponseTypeDef",
    "UpdateInputSecurityGroupResponseTypeDef",
    "UpdateMultiplexProgramResponseTypeDef",
    "UpdateMultiplexResponseTypeDef",
    "UpdateReservationResponseTypeDef",
    "VideoBlackFailoverSettingsTypeDef",
    "VideoCodecSettingsTypeDef",
    "VideoDescriptionTypeDef",
    "VideoSelectorColorSpaceSettingsTypeDef",
    "VideoSelectorPidTypeDef",
    "VideoSelectorProgramIdTypeDef",
    "VideoSelectorSettingsTypeDef",
    "VideoSelectorTypeDef",
    "VpcOutputSettingsDescriptionTypeDef",
    "VpcOutputSettingsTypeDef",
    "WaiterConfigTypeDef",
    "WavSettingsTypeDef",
)


class AacSettingsTypeDef(TypedDict, total=False):
    Bitrate: float
    CodingMode: AacCodingMode
    InputType: AacInputType
    Profile: AacProfile
    RateControlMode: AacRateControlMode
    RawFormat: AacRawFormat
    SampleRate: float
    Spec: AacSpec
    VbrQuality: AacVbrQuality


class Ac3SettingsTypeDef(TypedDict, total=False):
    Bitrate: float
    BitstreamMode: Ac3BitstreamMode
    CodingMode: Ac3CodingMode
    Dialnorm: int
    DrcProfile: Ac3DrcProfile
    LfeFilter: Ac3LfeFilter
    MetadataControl: Ac3MetadataControl


class AncillarySourceSettingsTypeDef(TypedDict, total=False):
    SourceAncillaryChannelNumber: int


class ArchiveCdnSettingsTypeDef(TypedDict, total=False):
    ArchiveS3Settings: "ArchiveS3SettingsTypeDef"


class ArchiveContainerSettingsTypeDef(TypedDict, total=False):
    M2tsSettings: "M2tsSettingsTypeDef"
    RawSettings: Dict[str, Any]


class _RequiredArchiveGroupSettingsTypeDef(TypedDict):
    Destination: "OutputLocationRefTypeDef"


class ArchiveGroupSettingsTypeDef(_RequiredArchiveGroupSettingsTypeDef, total=False):
    ArchiveCdnSettings: "ArchiveCdnSettingsTypeDef"
    RolloverInterval: int


class _RequiredArchiveOutputSettingsTypeDef(TypedDict):
    ContainerSettings: "ArchiveContainerSettingsTypeDef"


class ArchiveOutputSettingsTypeDef(_RequiredArchiveOutputSettingsTypeDef, total=False):
    Extension: str
    NameModifier: str


class ArchiveS3SettingsTypeDef(TypedDict, total=False):
    CannedAcl: S3CannedAcl


class AudioChannelMappingTypeDef(TypedDict):
    InputChannelLevels: List["InputChannelLevelTypeDef"]
    OutputChannel: int


class AudioCodecSettingsTypeDef(TypedDict, total=False):
    AacSettings: "AacSettingsTypeDef"
    Ac3Settings: "Ac3SettingsTypeDef"
    Eac3Settings: "Eac3SettingsTypeDef"
    Mp2Settings: "Mp2SettingsTypeDef"
    PassThroughSettings: Dict[str, Any]
    WavSettings: "WavSettingsTypeDef"


class _RequiredAudioDescriptionTypeDef(TypedDict):
    AudioSelectorName: str
    Name: str


class AudioDescriptionTypeDef(_RequiredAudioDescriptionTypeDef, total=False):
    AudioNormalizationSettings: "AudioNormalizationSettingsTypeDef"
    AudioType: AudioType
    AudioTypeControl: AudioDescriptionAudioTypeControl
    CodecSettings: "AudioCodecSettingsTypeDef"
    LanguageCode: str
    LanguageCodeControl: AudioDescriptionLanguageCodeControl
    RemixSettings: "RemixSettingsTypeDef"
    StreamName: str


class _RequiredAudioLanguageSelectionTypeDef(TypedDict):
    LanguageCode: str


class AudioLanguageSelectionTypeDef(_RequiredAudioLanguageSelectionTypeDef, total=False):
    LanguageSelectionPolicy: AudioLanguageSelectionPolicy


class AudioNormalizationSettingsTypeDef(TypedDict, total=False):
    Algorithm: AudioNormalizationAlgorithm
    AlgorithmControl: Literal["CORRECT_AUDIO"]
    TargetLkfs: float


class AudioOnlyHlsSettingsTypeDef(TypedDict, total=False):
    AudioGroupId: str
    AudioOnlyImage: "InputLocationTypeDef"
    AudioTrackType: AudioOnlyHlsTrackType
    SegmentType: AudioOnlyHlsSegmentType


class AudioPidSelectionTypeDef(TypedDict):
    Pid: int


class AudioSelectorSettingsTypeDef(TypedDict, total=False):
    AudioLanguageSelection: "AudioLanguageSelectionTypeDef"
    AudioPidSelection: "AudioPidSelectionTypeDef"
    AudioTrackSelection: "AudioTrackSelectionTypeDef"


class _RequiredAudioSelectorTypeDef(TypedDict):
    Name: str


class AudioSelectorTypeDef(_RequiredAudioSelectorTypeDef, total=False):
    SelectorSettings: "AudioSelectorSettingsTypeDef"


class _RequiredAudioSilenceFailoverSettingsTypeDef(TypedDict):
    AudioSelectorName: str


class AudioSilenceFailoverSettingsTypeDef(
    _RequiredAudioSilenceFailoverSettingsTypeDef, total=False
):
    AudioSilenceThresholdMsec: int


class AudioTrackSelectionTypeDef(TypedDict):
    Tracks: List["AudioTrackTypeDef"]


class AudioTrackTypeDef(TypedDict):
    Track: int


class _RequiredAutomaticInputFailoverSettingsTypeDef(TypedDict):
    SecondaryInputId: str


class AutomaticInputFailoverSettingsTypeDef(
    _RequiredAutomaticInputFailoverSettingsTypeDef, total=False
):
    ErrorClearTimeMsec: int
    FailoverConditions: List["FailoverConditionTypeDef"]
    InputPreference: InputPreference


class AvailBlankingTypeDef(TypedDict, total=False):
    AvailBlankingImage: "InputLocationTypeDef"
    State: AvailBlankingState


class AvailConfigurationTypeDef(TypedDict, total=False):
    AvailSettings: "AvailSettingsTypeDef"


class AvailSettingsTypeDef(TypedDict, total=False):
    Scte35SpliceInsert: "Scte35SpliceInsertTypeDef"
    Scte35TimeSignalApos: "Scte35TimeSignalAposTypeDef"


class BatchDeleteResponseTypeDef(TypedDict, total=False):
    Failed: List["BatchFailedResultModelTypeDef"]
    Successful: List["BatchSuccessfulResultModelTypeDef"]


class BatchFailedResultModelTypeDef(TypedDict, total=False):
    Arn: str
    Code: str
    Id: str
    Message: str


class BatchScheduleActionCreateRequestTypeDef(TypedDict):
    ScheduleActions: List["ScheduleActionTypeDef"]


class BatchScheduleActionCreateResultTypeDef(TypedDict):
    ScheduleActions: List["ScheduleActionTypeDef"]


class BatchScheduleActionDeleteRequestTypeDef(TypedDict):
    ActionNames: List[str]


class BatchScheduleActionDeleteResultTypeDef(TypedDict):
    ScheduleActions: List["ScheduleActionTypeDef"]


class BatchStartResponseTypeDef(TypedDict, total=False):
    Failed: List["BatchFailedResultModelTypeDef"]
    Successful: List["BatchSuccessfulResultModelTypeDef"]


class BatchStopResponseTypeDef(TypedDict, total=False):
    Failed: List["BatchFailedResultModelTypeDef"]
    Successful: List["BatchSuccessfulResultModelTypeDef"]


class BatchSuccessfulResultModelTypeDef(TypedDict, total=False):
    Arn: str
    Id: str
    State: str


class BatchUpdateScheduleResponseTypeDef(TypedDict, total=False):
    Creates: "BatchScheduleActionCreateResultTypeDef"
    Deletes: "BatchScheduleActionDeleteResultTypeDef"


class BlackoutSlateTypeDef(TypedDict, total=False):
    BlackoutSlateImage: "InputLocationTypeDef"
    NetworkEndBlackout: BlackoutSlateNetworkEndBlackout
    NetworkEndBlackoutImage: "InputLocationTypeDef"
    NetworkId: str
    State: BlackoutSlateState


class BurnInDestinationSettingsTypeDef(TypedDict, total=False):
    Alignment: BurnInAlignment
    BackgroundColor: BurnInBackgroundColor
    BackgroundOpacity: int
    Font: "InputLocationTypeDef"
    FontColor: BurnInFontColor
    FontOpacity: int
    FontResolution: int
    FontSize: str
    OutlineColor: BurnInOutlineColor
    OutlineSize: int
    ShadowColor: BurnInShadowColor
    ShadowOpacity: int
    ShadowXOffset: int
    ShadowYOffset: int
    TeletextGridControl: BurnInTeletextGridControl
    XPosition: int
    YPosition: int


class _RequiredCaptionDescriptionTypeDef(TypedDict):
    CaptionSelectorName: str
    Name: str


class CaptionDescriptionTypeDef(_RequiredCaptionDescriptionTypeDef, total=False):
    DestinationSettings: "CaptionDestinationSettingsTypeDef"
    LanguageCode: str
    LanguageDescription: str


class CaptionDestinationSettingsTypeDef(TypedDict, total=False):
    AribDestinationSettings: Dict[str, Any]
    BurnInDestinationSettings: "BurnInDestinationSettingsTypeDef"
    DvbSubDestinationSettings: "DvbSubDestinationSettingsTypeDef"
    EbuTtDDestinationSettings: "EbuTtDDestinationSettingsTypeDef"
    EmbeddedDestinationSettings: Dict[str, Any]
    EmbeddedPlusScte20DestinationSettings: Dict[str, Any]
    RtmpCaptionInfoDestinationSettings: Dict[str, Any]
    Scte20PlusEmbeddedDestinationSettings: Dict[str, Any]
    Scte27DestinationSettings: Dict[str, Any]
    SmpteTtDestinationSettings: Dict[str, Any]
    TeletextDestinationSettings: Dict[str, Any]
    TtmlDestinationSettings: "TtmlDestinationSettingsTypeDef"
    WebvttDestinationSettings: Dict[str, Any]


class CaptionLanguageMappingTypeDef(TypedDict):
    CaptionChannel: int
    LanguageCode: str
    LanguageDescription: str


class CaptionRectangleTypeDef(TypedDict):
    Height: float
    LeftOffset: float
    TopOffset: float
    Width: float


class CaptionSelectorSettingsTypeDef(TypedDict, total=False):
    AncillarySourceSettings: "AncillarySourceSettingsTypeDef"
    AribSourceSettings: Dict[str, Any]
    DvbSubSourceSettings: "DvbSubSourceSettingsTypeDef"
    EmbeddedSourceSettings: "EmbeddedSourceSettingsTypeDef"
    Scte20SourceSettings: "Scte20SourceSettingsTypeDef"
    Scte27SourceSettings: "Scte27SourceSettingsTypeDef"
    TeletextSourceSettings: "TeletextSourceSettingsTypeDef"


class _RequiredCaptionSelectorTypeDef(TypedDict):
    Name: str


class CaptionSelectorTypeDef(_RequiredCaptionSelectorTypeDef, total=False):
    LanguageCode: str
    SelectorSettings: "CaptionSelectorSettingsTypeDef"


class CdiInputSpecificationTypeDef(TypedDict, total=False):
    Resolution: CdiInputResolution


class ChannelEgressEndpointTypeDef(TypedDict, total=False):
    SourceIp: str


class ChannelSummaryTypeDef(TypedDict, total=False):
    Arn: str
    CdiInputSpecification: "CdiInputSpecificationTypeDef"
    ChannelClass: ChannelClass
    Destinations: List["OutputDestinationTypeDef"]
    EgressEndpoints: List["ChannelEgressEndpointTypeDef"]
    Id: str
    InputAttachments: List["InputAttachmentTypeDef"]
    InputSpecification: "InputSpecificationTypeDef"
    LogLevel: LogLevel
    Name: str
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelState
    Tags: Dict[str, str]
    Vpc: "VpcOutputSettingsDescriptionTypeDef"


class ChannelTypeDef(TypedDict, total=False):
    Arn: str
    CdiInputSpecification: "CdiInputSpecificationTypeDef"
    ChannelClass: ChannelClass
    Destinations: List["OutputDestinationTypeDef"]
    EgressEndpoints: List["ChannelEgressEndpointTypeDef"]
    EncoderSettings: "EncoderSettingsTypeDef"
    Id: str
    InputAttachments: List["InputAttachmentTypeDef"]
    InputSpecification: "InputSpecificationTypeDef"
    LogLevel: LogLevel
    Name: str
    PipelineDetails: List["PipelineDetailTypeDef"]
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelState
    Tags: Dict[str, str]
    Vpc: "VpcOutputSettingsDescriptionTypeDef"


class CreateChannelResponseTypeDef(TypedDict, total=False):
    Channel: "ChannelTypeDef"


class CreateInputResponseTypeDef(TypedDict, total=False):
    Input: "InputTypeDef"


class CreateInputSecurityGroupResponseTypeDef(TypedDict, total=False):
    SecurityGroup: "InputSecurityGroupTypeDef"


class CreateMultiplexProgramResponseTypeDef(TypedDict, total=False):
    MultiplexProgram: "MultiplexProgramTypeDef"


class CreateMultiplexResponseTypeDef(TypedDict, total=False):
    Multiplex: "MultiplexTypeDef"


class CreatePartnerInputResponseTypeDef(TypedDict, total=False):
    Input: "InputTypeDef"


class DeleteChannelResponseTypeDef(TypedDict, total=False):
    Arn: str
    CdiInputSpecification: "CdiInputSpecificationTypeDef"
    ChannelClass: ChannelClass
    Destinations: List["OutputDestinationTypeDef"]
    EgressEndpoints: List["ChannelEgressEndpointTypeDef"]
    EncoderSettings: "EncoderSettingsTypeDef"
    Id: str
    InputAttachments: List["InputAttachmentTypeDef"]
    InputSpecification: "InputSpecificationTypeDef"
    LogLevel: LogLevel
    Name: str
    PipelineDetails: List["PipelineDetailTypeDef"]
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelState
    Tags: Dict[str, str]
    Vpc: "VpcOutputSettingsDescriptionTypeDef"


class DeleteMultiplexProgramResponseTypeDef(TypedDict, total=False):
    ChannelId: str
    MultiplexProgramSettings: "MultiplexProgramSettingsTypeDef"
    PacketIdentifiersMap: "MultiplexProgramPacketIdentifiersMapTypeDef"
    PipelineDetails: List["MultiplexProgramPipelineDetailTypeDef"]
    ProgramName: str


class DeleteMultiplexResponseTypeDef(TypedDict, total=False):
    Arn: str
    AvailabilityZones: List[str]
    Destinations: List["MultiplexOutputDestinationTypeDef"]
    Id: str
    MultiplexSettings: "MultiplexSettingsTypeDef"
    Name: str
    PipelinesRunningCount: int
    ProgramCount: int
    State: MultiplexState
    Tags: Dict[str, str]


class DeleteReservationResponseTypeDef(TypedDict, total=False):
    Arn: str
    Count: int
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal["MONTHS"]
    End: str
    FixedPrice: float
    Name: str
    OfferingDescription: str
    OfferingId: str
    OfferingType: Literal["NO_UPFRONT"]
    Region: str
    ReservationId: str
    ResourceSpecification: "ReservationResourceSpecificationTypeDef"
    Start: str
    State: ReservationState
    Tags: Dict[str, str]
    UsagePrice: float


class DescribeChannelResponseTypeDef(TypedDict, total=False):
    Arn: str
    CdiInputSpecification: "CdiInputSpecificationTypeDef"
    ChannelClass: ChannelClass
    Destinations: List["OutputDestinationTypeDef"]
    EgressEndpoints: List["ChannelEgressEndpointTypeDef"]
    EncoderSettings: "EncoderSettingsTypeDef"
    Id: str
    InputAttachments: List["InputAttachmentTypeDef"]
    InputSpecification: "InputSpecificationTypeDef"
    LogLevel: LogLevel
    Name: str
    PipelineDetails: List["PipelineDetailTypeDef"]
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelState
    Tags: Dict[str, str]
    Vpc: "VpcOutputSettingsDescriptionTypeDef"


DescribeInputDeviceResponseTypeDef = TypedDict(
    "DescribeInputDeviceResponseTypeDef",
    {
        "Arn": str,
        "ConnectionState": InputDeviceConnectionState,
        "DeviceSettingsSyncState": DeviceSettingsSyncState,
        "DeviceUpdateStatus": DeviceUpdateStatus,
        "HdDeviceSettings": "InputDeviceHdSettingsTypeDef",
        "Id": str,
        "MacAddress": str,
        "Name": str,
        "NetworkSettings": "InputDeviceNetworkSettingsTypeDef",
        "SerialNumber": str,
        "Type": Literal["HD"],
        "UhdDeviceSettings": "InputDeviceUhdSettingsTypeDef",
    },
    total=False,
)


class DescribeInputDeviceThumbnailResponseTypeDef(TypedDict, total=False):
    Body: StreamingBody
    ContentType: Literal["image/jpeg"]
    ContentLength: int
    ETag: str
    LastModified: datetime


DescribeInputResponseTypeDef = TypedDict(
    "DescribeInputResponseTypeDef",
    {
        "Arn": str,
        "AttachedChannels": List[str],
        "Destinations": List["InputDestinationTypeDef"],
        "Id": str,
        "InputClass": InputClass,
        "InputDevices": List["InputDeviceSettingsTypeDef"],
        "InputPartnerIds": List[str],
        "InputSourceType": InputSourceType,
        "MediaConnectFlows": List["MediaConnectFlowTypeDef"],
        "Name": str,
        "RoleArn": str,
        "SecurityGroups": List[str],
        "Sources": List["InputSourceTypeDef"],
        "State": InputState,
        "Tags": Dict[str, str],
        "Type": InputType,
    },
    total=False,
)


class DescribeInputSecurityGroupResponseTypeDef(TypedDict, total=False):
    Arn: str
    Id: str
    Inputs: List[str]
    State: InputSecurityGroupState
    Tags: Dict[str, str]
    WhitelistRules: List["InputWhitelistRuleTypeDef"]


class DescribeMultiplexProgramResponseTypeDef(TypedDict, total=False):
    ChannelId: str
    MultiplexProgramSettings: "MultiplexProgramSettingsTypeDef"
    PacketIdentifiersMap: "MultiplexProgramPacketIdentifiersMapTypeDef"
    PipelineDetails: List["MultiplexProgramPipelineDetailTypeDef"]
    ProgramName: str


class DescribeMultiplexResponseTypeDef(TypedDict, total=False):
    Arn: str
    AvailabilityZones: List[str]
    Destinations: List["MultiplexOutputDestinationTypeDef"]
    Id: str
    MultiplexSettings: "MultiplexSettingsTypeDef"
    Name: str
    PipelinesRunningCount: int
    ProgramCount: int
    State: MultiplexState
    Tags: Dict[str, str]


class DescribeOfferingResponseTypeDef(TypedDict, total=False):
    Arn: str
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal["MONTHS"]
    FixedPrice: float
    OfferingDescription: str
    OfferingId: str
    OfferingType: Literal["NO_UPFRONT"]
    Region: str
    ResourceSpecification: "ReservationResourceSpecificationTypeDef"
    UsagePrice: float


class DescribeReservationResponseTypeDef(TypedDict, total=False):
    Arn: str
    Count: int
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal["MONTHS"]
    End: str
    FixedPrice: float
    Name: str
    OfferingDescription: str
    OfferingId: str
    OfferingType: Literal["NO_UPFRONT"]
    Region: str
    ReservationId: str
    ResourceSpecification: "ReservationResourceSpecificationTypeDef"
    Start: str
    State: ReservationState
    Tags: Dict[str, str]
    UsagePrice: float


class DescribeScheduleResponseTypeDef(TypedDict, total=False):
    NextToken: str
    ScheduleActions: List["ScheduleActionTypeDef"]


class _RequiredDvbNitSettingsTypeDef(TypedDict):
    NetworkId: int
    NetworkName: str


class DvbNitSettingsTypeDef(_RequiredDvbNitSettingsTypeDef, total=False):
    RepInterval: int


class DvbSdtSettingsTypeDef(TypedDict, total=False):
    OutputSdt: DvbSdtOutputSdt
    RepInterval: int
    ServiceName: str
    ServiceProviderName: str


class DvbSubDestinationSettingsTypeDef(TypedDict, total=False):
    Alignment: DvbSubDestinationAlignment
    BackgroundColor: DvbSubDestinationBackgroundColor
    BackgroundOpacity: int
    Font: "InputLocationTypeDef"
    FontColor: DvbSubDestinationFontColor
    FontOpacity: int
    FontResolution: int
    FontSize: str
    OutlineColor: DvbSubDestinationOutlineColor
    OutlineSize: int
    ShadowColor: DvbSubDestinationShadowColor
    ShadowOpacity: int
    ShadowXOffset: int
    ShadowYOffset: int
    TeletextGridControl: DvbSubDestinationTeletextGridControl
    XPosition: int
    YPosition: int


class DvbSubSourceSettingsTypeDef(TypedDict, total=False):
    Pid: int


class DvbTdtSettingsTypeDef(TypedDict, total=False):
    RepInterval: int


class Eac3SettingsTypeDef(TypedDict, total=False):
    AttenuationControl: Eac3AttenuationControl
    Bitrate: float
    BitstreamMode: Eac3BitstreamMode
    CodingMode: Eac3CodingMode
    DcFilter: Eac3DcFilter
    Dialnorm: int
    DrcLine: Eac3DrcLine
    DrcRf: Eac3DrcRf
    LfeControl: Eac3LfeControl
    LfeFilter: Eac3LfeFilter
    LoRoCenterMixLevel: float
    LoRoSurroundMixLevel: float
    LtRtCenterMixLevel: float
    LtRtSurroundMixLevel: float
    MetadataControl: Eac3MetadataControl
    PassthroughControl: Eac3PassthroughControl
    PhaseControl: Eac3PhaseControl
    StereoDownmix: Eac3StereoDownmix
    SurroundExMode: Eac3SurroundExMode
    SurroundMode: Eac3SurroundMode


class EbuTtDDestinationSettingsTypeDef(TypedDict, total=False):
    CopyrightHolder: str
    FillLineGap: EbuTtDFillLineGapControl
    FontFamily: str
    StyleControl: EbuTtDDestinationStyleControl


class EmbeddedSourceSettingsTypeDef(TypedDict, total=False):
    Convert608To708: EmbeddedConvert608To708
    Scte20Detection: EmbeddedScte20Detection
    Source608ChannelNumber: int
    Source608TrackNumber: int


class _RequiredEncoderSettingsTypeDef(TypedDict):
    AudioDescriptions: List["AudioDescriptionTypeDef"]
    OutputGroups: List["OutputGroupTypeDef"]
    TimecodeConfig: "TimecodeConfigTypeDef"
    VideoDescriptions: List["VideoDescriptionTypeDef"]


class EncoderSettingsTypeDef(_RequiredEncoderSettingsTypeDef, total=False):
    AvailBlanking: "AvailBlankingTypeDef"
    AvailConfiguration: "AvailConfigurationTypeDef"
    BlackoutSlate: "BlackoutSlateTypeDef"
    CaptionDescriptions: List["CaptionDescriptionTypeDef"]
    FeatureActivations: "FeatureActivationsTypeDef"
    GlobalConfiguration: "GlobalConfigurationTypeDef"
    MotionGraphicsConfiguration: "MotionGraphicsConfigurationTypeDef"
    NielsenConfiguration: "NielsenConfigurationTypeDef"


class FailoverConditionSettingsTypeDef(TypedDict, total=False):
    AudioSilenceSettings: "AudioSilenceFailoverSettingsTypeDef"
    InputLossSettings: "InputLossFailoverSettingsTypeDef"
    VideoBlackSettings: "VideoBlackFailoverSettingsTypeDef"


class FailoverConditionTypeDef(TypedDict, total=False):
    FailoverConditionSettings: "FailoverConditionSettingsTypeDef"


class FeatureActivationsTypeDef(TypedDict, total=False):
    InputPrepareScheduleActions: FeatureActivationsInputPrepareScheduleActions


class FecOutputSettingsTypeDef(TypedDict, total=False):
    ColumnDepth: int
    IncludeFec: FecOutputIncludeFec
    RowLength: int


class FixedModeScheduleActionStartSettingsTypeDef(TypedDict):
    Time: str


class Fmp4HlsSettingsTypeDef(TypedDict, total=False):
    AudioRenditionSets: str
    NielsenId3Behavior: Fmp4NielsenId3Behavior
    TimedMetadataBehavior: Fmp4TimedMetadataBehavior


class FollowModeScheduleActionStartSettingsTypeDef(TypedDict):
    FollowPoint: FollowPoint
    ReferenceActionName: str


class FrameCaptureCdnSettingsTypeDef(TypedDict, total=False):
    FrameCaptureS3Settings: "FrameCaptureS3SettingsTypeDef"


class _RequiredFrameCaptureGroupSettingsTypeDef(TypedDict):
    Destination: "OutputLocationRefTypeDef"


class FrameCaptureGroupSettingsTypeDef(_RequiredFrameCaptureGroupSettingsTypeDef, total=False):
    FrameCaptureCdnSettings: "FrameCaptureCdnSettingsTypeDef"


class FrameCaptureOutputSettingsTypeDef(TypedDict, total=False):
    NameModifier: str


class FrameCaptureS3SettingsTypeDef(TypedDict, total=False):
    CannedAcl: S3CannedAcl


class FrameCaptureSettingsTypeDef(TypedDict, total=False):
    CaptureInterval: int
    CaptureIntervalUnits: FrameCaptureIntervalUnit


class GlobalConfigurationTypeDef(TypedDict, total=False):
    InitialAudioGain: int
    InputEndAction: GlobalConfigurationInputEndAction
    InputLossBehavior: "InputLossBehaviorTypeDef"
    OutputLockingMode: GlobalConfigurationOutputLockingMode
    OutputTimingSource: GlobalConfigurationOutputTimingSource
    SupportLowFramerateInputs: GlobalConfigurationLowFramerateInputs


class H264ColorSpaceSettingsTypeDef(TypedDict, total=False):
    ColorSpacePassthroughSettings: Dict[str, Any]
    Rec601Settings: Dict[str, Any]
    Rec709Settings: Dict[str, Any]


class H264FilterSettingsTypeDef(TypedDict, total=False):
    TemporalFilterSettings: "TemporalFilterSettingsTypeDef"


class H264SettingsTypeDef(TypedDict, total=False):
    AdaptiveQuantization: H264AdaptiveQuantization
    AfdSignaling: AfdSignaling
    Bitrate: int
    BufFillPct: int
    BufSize: int
    ColorMetadata: H264ColorMetadata
    ColorSpaceSettings: "H264ColorSpaceSettingsTypeDef"
    EntropyEncoding: H264EntropyEncoding
    FilterSettings: "H264FilterSettingsTypeDef"
    FixedAfd: FixedAfd
    FlickerAq: H264FlickerAq
    ForceFieldPictures: H264ForceFieldPictures
    FramerateControl: H264FramerateControl
    FramerateDenominator: int
    FramerateNumerator: int
    GopBReference: H264GopBReference
    GopClosedCadence: int
    GopNumBFrames: int
    GopSize: float
    GopSizeUnits: H264GopSizeUnits
    Level: H264Level
    LookAheadRateControl: H264LookAheadRateControl
    MaxBitrate: int
    MinIInterval: int
    NumRefFrames: int
    ParControl: H264ParControl
    ParDenominator: int
    ParNumerator: int
    Profile: H264Profile
    QualityLevel: H264QualityLevel
    QvbrQualityLevel: int
    RateControlMode: H264RateControlMode
    ScanType: H264ScanType
    SceneChangeDetect: H264SceneChangeDetect
    Slices: int
    Softness: int
    SpatialAq: H264SpatialAq
    SubgopLength: H264SubGopLength
    Syntax: H264Syntax
    TemporalAq: H264TemporalAq
    TimecodeInsertion: H264TimecodeInsertionBehavior


class H265ColorSpaceSettingsTypeDef(TypedDict, total=False):
    ColorSpacePassthroughSettings: Dict[str, Any]
    Hdr10Settings: "Hdr10SettingsTypeDef"
    Rec601Settings: Dict[str, Any]
    Rec709Settings: Dict[str, Any]


class H265FilterSettingsTypeDef(TypedDict, total=False):
    TemporalFilterSettings: "TemporalFilterSettingsTypeDef"


class _RequiredH265SettingsTypeDef(TypedDict):
    FramerateDenominator: int
    FramerateNumerator: int


class H265SettingsTypeDef(_RequiredH265SettingsTypeDef, total=False):
    AdaptiveQuantization: H265AdaptiveQuantization
    AfdSignaling: AfdSignaling
    AlternativeTransferFunction: H265AlternativeTransferFunction
    Bitrate: int
    BufSize: int
    ColorMetadata: H265ColorMetadata
    ColorSpaceSettings: "H265ColorSpaceSettingsTypeDef"
    FilterSettings: "H265FilterSettingsTypeDef"
    FixedAfd: FixedAfd
    FlickerAq: H265FlickerAq
    GopClosedCadence: int
    GopSize: float
    GopSizeUnits: H265GopSizeUnits
    Level: H265Level
    LookAheadRateControl: H265LookAheadRateControl
    MaxBitrate: int
    MinIInterval: int
    ParDenominator: int
    ParNumerator: int
    Profile: H265Profile
    QvbrQualityLevel: int
    RateControlMode: H265RateControlMode
    ScanType: H265ScanType
    SceneChangeDetect: H265SceneChangeDetect
    Slices: int
    Tier: H265Tier
    TimecodeInsertion: H265TimecodeInsertionBehavior


class Hdr10SettingsTypeDef(TypedDict, total=False):
    MaxCll: int
    MaxFall: int


class HlsAkamaiSettingsTypeDef(TypedDict, total=False):
    ConnectionRetryInterval: int
    FilecacheDuration: int
    HttpTransferMode: HlsAkamaiHttpTransferMode
    NumRetries: int
    RestartDelay: int
    Salt: str
    Token: str


class HlsBasicPutSettingsTypeDef(TypedDict, total=False):
    ConnectionRetryInterval: int
    FilecacheDuration: int
    NumRetries: int
    RestartDelay: int


class HlsCdnSettingsTypeDef(TypedDict, total=False):
    HlsAkamaiSettings: "HlsAkamaiSettingsTypeDef"
    HlsBasicPutSettings: "HlsBasicPutSettingsTypeDef"
    HlsMediaStoreSettings: "HlsMediaStoreSettingsTypeDef"
    HlsS3Settings: "HlsS3SettingsTypeDef"
    HlsWebdavSettings: "HlsWebdavSettingsTypeDef"


class _RequiredHlsGroupSettingsTypeDef(TypedDict):
    Destination: "OutputLocationRefTypeDef"


class HlsGroupSettingsTypeDef(_RequiredHlsGroupSettingsTypeDef, total=False):
    AdMarkers: List[HlsAdMarkers]
    BaseUrlContent: str
    BaseUrlContent1: str
    BaseUrlManifest: str
    BaseUrlManifest1: str
    CaptionLanguageMappings: List["CaptionLanguageMappingTypeDef"]
    CaptionLanguageSetting: HlsCaptionLanguageSetting
    ClientCache: HlsClientCache
    CodecSpecification: HlsCodecSpecification
    ConstantIv: str
    DirectoryStructure: HlsDirectoryStructure
    DiscontinuityTags: HlsDiscontinuityTags
    EncryptionType: HlsEncryptionType
    HlsCdnSettings: "HlsCdnSettingsTypeDef"
    HlsId3SegmentTagging: HlsId3SegmentTaggingState
    IFrameOnlyPlaylists: IFrameOnlyPlaylistType
    IncompleteSegmentBehavior: HlsIncompleteSegmentBehavior
    IndexNSegments: int
    InputLossAction: InputLossActionForHlsOut
    IvInManifest: HlsIvInManifest
    IvSource: HlsIvSource
    KeepSegments: int
    KeyFormat: str
    KeyFormatVersions: str
    KeyProviderSettings: "KeyProviderSettingsTypeDef"
    ManifestCompression: HlsManifestCompression
    ManifestDurationFormat: HlsManifestDurationFormat
    MinSegmentLength: int
    Mode: HlsMode
    OutputSelection: HlsOutputSelection
    ProgramDateTime: HlsProgramDateTime
    ProgramDateTimePeriod: int
    RedundantManifest: HlsRedundantManifest
    SegmentLength: int
    SegmentationMode: HlsSegmentationMode
    SegmentsPerSubdirectory: int
    StreamInfResolution: HlsStreamInfResolution
    TimedMetadataId3Frame: HlsTimedMetadataId3Frame
    TimedMetadataId3Period: int
    TimestampDeltaMilliseconds: int
    TsFileMode: HlsTsFileMode


class HlsId3SegmentTaggingScheduleActionSettingsTypeDef(TypedDict):
    Tag: str


class HlsInputSettingsTypeDef(TypedDict, total=False):
    Bandwidth: int
    BufferSegments: int
    Retries: int
    RetryInterval: int


class HlsMediaStoreSettingsTypeDef(TypedDict, total=False):
    ConnectionRetryInterval: int
    FilecacheDuration: int
    MediaStoreStorageClass: Literal["TEMPORAL"]
    NumRetries: int
    RestartDelay: int


class _RequiredHlsOutputSettingsTypeDef(TypedDict):
    HlsSettings: "HlsSettingsTypeDef"


class HlsOutputSettingsTypeDef(_RequiredHlsOutputSettingsTypeDef, total=False):
    H265PackagingType: HlsH265PackagingType
    NameModifier: str
    SegmentModifier: str


class HlsS3SettingsTypeDef(TypedDict, total=False):
    CannedAcl: S3CannedAcl


class HlsSettingsTypeDef(TypedDict, total=False):
    AudioOnlyHlsSettings: "AudioOnlyHlsSettingsTypeDef"
    Fmp4HlsSettings: "Fmp4HlsSettingsTypeDef"
    FrameCaptureHlsSettings: Dict[str, Any]
    StandardHlsSettings: "StandardHlsSettingsTypeDef"


class HlsTimedMetadataScheduleActionSettingsTypeDef(TypedDict):
    Id3: str


class HlsWebdavSettingsTypeDef(TypedDict, total=False):
    ConnectionRetryInterval: int
    FilecacheDuration: int
    HttpTransferMode: HlsWebdavHttpTransferMode
    NumRetries: int
    RestartDelay: int


class InputAttachmentTypeDef(TypedDict, total=False):
    AutomaticInputFailoverSettings: "AutomaticInputFailoverSettingsTypeDef"
    InputAttachmentName: str
    InputId: str
    InputSettings: "InputSettingsTypeDef"


class InputChannelLevelTypeDef(TypedDict):
    Gain: int
    InputChannel: int


class _RequiredInputClippingSettingsTypeDef(TypedDict):
    InputTimecodeSource: InputTimecodeSource


class InputClippingSettingsTypeDef(_RequiredInputClippingSettingsTypeDef, total=False):
    StartTimecode: "StartTimecodeTypeDef"
    StopTimecode: "StopTimecodeTypeDef"


class InputDestinationRequestTypeDef(TypedDict, total=False):
    StreamName: str


class InputDestinationTypeDef(TypedDict, total=False):
    Ip: str
    Port: str
    Url: str
    Vpc: "InputDestinationVpcTypeDef"


class InputDestinationVpcTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    NetworkInterfaceId: str


class InputDeviceConfigurableSettingsTypeDef(TypedDict, total=False):
    ConfiguredInput: InputDeviceConfiguredInput
    MaxBitrate: int


class InputDeviceHdSettingsTypeDef(TypedDict, total=False):
    ActiveInput: InputDeviceActiveInput
    ConfiguredInput: InputDeviceConfiguredInput
    DeviceState: InputDeviceState
    Framerate: float
    Height: int
    MaxBitrate: int
    ScanType: InputDeviceScanType
    Width: int


class InputDeviceNetworkSettingsTypeDef(TypedDict, total=False):
    DnsAddresses: List[str]
    Gateway: str
    IpAddress: str
    IpScheme: InputDeviceIpScheme
    SubnetMask: str


class InputDeviceRequestTypeDef(TypedDict, total=False):
    Id: str


class InputDeviceSettingsTypeDef(TypedDict, total=False):
    Id: str


InputDeviceSummaryTypeDef = TypedDict(
    "InputDeviceSummaryTypeDef",
    {
        "Arn": str,
        "ConnectionState": InputDeviceConnectionState,
        "DeviceSettingsSyncState": DeviceSettingsSyncState,
        "DeviceUpdateStatus": DeviceUpdateStatus,
        "HdDeviceSettings": "InputDeviceHdSettingsTypeDef",
        "Id": str,
        "MacAddress": str,
        "Name": str,
        "NetworkSettings": "InputDeviceNetworkSettingsTypeDef",
        "SerialNumber": str,
        "Type": Literal["HD"],
        "UhdDeviceSettings": "InputDeviceUhdSettingsTypeDef",
    },
    total=False,
)


class InputDeviceUhdSettingsTypeDef(TypedDict, total=False):
    ActiveInput: InputDeviceActiveInput
    ConfiguredInput: InputDeviceConfiguredInput
    DeviceState: InputDeviceState
    Framerate: float
    Height: int
    MaxBitrate: int
    ScanType: InputDeviceScanType
    Width: int


class _RequiredInputLocationTypeDef(TypedDict):
    Uri: str


class InputLocationTypeDef(_RequiredInputLocationTypeDef, total=False):
    PasswordParam: str
    Username: str


class InputLossBehaviorTypeDef(TypedDict, total=False):
    BlackFrameMsec: int
    InputLossImageColor: str
    InputLossImageSlate: "InputLocationTypeDef"
    InputLossImageType: InputLossImageType
    RepeatFrameMsec: int


class InputLossFailoverSettingsTypeDef(TypedDict, total=False):
    InputLossThresholdMsec: int


class InputPrepareScheduleActionSettingsTypeDef(TypedDict, total=False):
    InputAttachmentNameReference: str
    InputClippingSettings: "InputClippingSettingsTypeDef"
    UrlPath: List[str]


class InputSecurityGroupTypeDef(TypedDict, total=False):
    Arn: str
    Id: str
    Inputs: List[str]
    State: InputSecurityGroupState
    Tags: Dict[str, str]
    WhitelistRules: List["InputWhitelistRuleTypeDef"]


class InputSettingsTypeDef(TypedDict, total=False):
    AudioSelectors: List["AudioSelectorTypeDef"]
    CaptionSelectors: List["CaptionSelectorTypeDef"]
    DeblockFilter: InputDeblockFilter
    DenoiseFilter: InputDenoiseFilter
    FilterStrength: int
    InputFilter: InputFilter
    NetworkInputSettings: "NetworkInputSettingsTypeDef"
    Smpte2038DataPreference: Smpte2038DataPreference
    SourceEndBehavior: InputSourceEndBehavior
    VideoSelector: "VideoSelectorTypeDef"


class InputSourceRequestTypeDef(TypedDict, total=False):
    PasswordParam: str
    Url: str
    Username: str


class InputSourceTypeDef(TypedDict, total=False):
    PasswordParam: str
    Url: str
    Username: str


class InputSpecificationTypeDef(TypedDict, total=False):
    Codec: InputCodec
    MaximumBitrate: InputMaximumBitrate
    Resolution: InputResolution


class _RequiredInputSwitchScheduleActionSettingsTypeDef(TypedDict):
    InputAttachmentNameReference: str


class InputSwitchScheduleActionSettingsTypeDef(
    _RequiredInputSwitchScheduleActionSettingsTypeDef, total=False
):
    InputClippingSettings: "InputClippingSettingsTypeDef"
    UrlPath: List[str]


InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "Arn": str,
        "AttachedChannels": List[str],
        "Destinations": List["InputDestinationTypeDef"],
        "Id": str,
        "InputClass": InputClass,
        "InputDevices": List["InputDeviceSettingsTypeDef"],
        "InputPartnerIds": List[str],
        "InputSourceType": InputSourceType,
        "MediaConnectFlows": List["MediaConnectFlowTypeDef"],
        "Name": str,
        "RoleArn": str,
        "SecurityGroups": List[str],
        "Sources": List["InputSourceTypeDef"],
        "State": InputState,
        "Tags": Dict[str, str],
        "Type": InputType,
    },
    total=False,
)


class _RequiredInputVpcRequestTypeDef(TypedDict):
    SubnetIds: List[str]


class InputVpcRequestTypeDef(_RequiredInputVpcRequestTypeDef, total=False):
    SecurityGroupIds: List[str]


class InputWhitelistRuleCidrTypeDef(TypedDict, total=False):
    Cidr: str


class InputWhitelistRuleTypeDef(TypedDict, total=False):
    Cidr: str


class KeyProviderSettingsTypeDef(TypedDict, total=False):
    StaticKeySettings: "StaticKeySettingsTypeDef"


class ListChannelsResponseTypeDef(TypedDict, total=False):
    Channels: List["ChannelSummaryTypeDef"]
    NextToken: str


class ListInputDeviceTransfersResponseTypeDef(TypedDict, total=False):
    InputDeviceTransfers: List["TransferringInputDeviceSummaryTypeDef"]
    NextToken: str


class ListInputDevicesResponseTypeDef(TypedDict, total=False):
    InputDevices: List["InputDeviceSummaryTypeDef"]
    NextToken: str


class ListInputSecurityGroupsResponseTypeDef(TypedDict, total=False):
    InputSecurityGroups: List["InputSecurityGroupTypeDef"]
    NextToken: str


class ListInputsResponseTypeDef(TypedDict, total=False):
    Inputs: List["InputTypeDef"]
    NextToken: str


class ListMultiplexProgramsResponseTypeDef(TypedDict, total=False):
    MultiplexPrograms: List["MultiplexProgramSummaryTypeDef"]
    NextToken: str


class ListMultiplexesResponseTypeDef(TypedDict, total=False):
    Multiplexes: List["MultiplexSummaryTypeDef"]
    NextToken: str


class ListOfferingsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Offerings: List["OfferingTypeDef"]


class ListReservationsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Reservations: List["ReservationTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class M2tsSettingsTypeDef(TypedDict, total=False):
    AbsentInputAudioBehavior: M2tsAbsentInputAudioBehavior
    Arib: M2tsArib
    AribCaptionsPid: str
    AribCaptionsPidControl: M2tsAribCaptionsPidControl
    AudioBufferModel: M2tsAudioBufferModel
    AudioFramesPerPes: int
    AudioPids: str
    AudioStreamType: M2tsAudioStreamType
    Bitrate: int
    BufferModel: M2tsBufferModel
    CcDescriptor: M2tsCcDescriptor
    DvbNitSettings: "DvbNitSettingsTypeDef"
    DvbSdtSettings: "DvbSdtSettingsTypeDef"
    DvbSubPids: str
    DvbTdtSettings: "DvbTdtSettingsTypeDef"
    DvbTeletextPid: str
    Ebif: M2tsEbifControl
    EbpAudioInterval: M2tsAudioInterval
    EbpLookaheadMs: int
    EbpPlacement: M2tsEbpPlacement
    EcmPid: str
    EsRateInPes: M2tsEsRateInPes
    EtvPlatformPid: str
    EtvSignalPid: str
    FragmentTime: float
    Klv: M2tsKlv
    KlvDataPids: str
    NielsenId3Behavior: M2tsNielsenId3Behavior
    NullPacketBitrate: float
    PatInterval: int
    PcrControl: M2tsPcrControl
    PcrPeriod: int
    PcrPid: str
    PmtInterval: int
    PmtPid: str
    ProgramNum: int
    RateMode: M2tsRateMode
    Scte27Pids: str
    Scte35Control: M2tsScte35Control
    Scte35Pid: str
    SegmentationMarkers: M2tsSegmentationMarkers
    SegmentationStyle: M2tsSegmentationStyle
    SegmentationTime: float
    TimedMetadataBehavior: M2tsTimedMetadataBehavior
    TimedMetadataPid: str
    TransportStreamId: int
    VideoPid: str


class M3u8SettingsTypeDef(TypedDict, total=False):
    AudioFramesPerPes: int
    AudioPids: str
    EcmPid: str
    NielsenId3Behavior: M3u8NielsenId3Behavior
    PatInterval: int
    PcrControl: M3u8PcrControl
    PcrPeriod: int
    PcrPid: str
    PmtInterval: int
    PmtPid: str
    ProgramNum: int
    Scte35Behavior: M3u8Scte35Behavior
    Scte35Pid: str
    TimedMetadataBehavior: M3u8TimedMetadataBehavior
    TimedMetadataPid: str
    TransportStreamId: int
    VideoPid: str


class MediaConnectFlowRequestTypeDef(TypedDict, total=False):
    FlowArn: str


class MediaConnectFlowTypeDef(TypedDict, total=False):
    FlowArn: str


class MediaPackageGroupSettingsTypeDef(TypedDict):
    Destination: "OutputLocationRefTypeDef"


class MediaPackageOutputDestinationSettingsTypeDef(TypedDict, total=False):
    ChannelId: str


class MotionGraphicsActivateScheduleActionSettingsTypeDef(TypedDict, total=False):
    Duration: int
    PasswordParam: str
    Url: str
    Username: str


class _RequiredMotionGraphicsConfigurationTypeDef(TypedDict):
    MotionGraphicsSettings: "MotionGraphicsSettingsTypeDef"


class MotionGraphicsConfigurationTypeDef(_RequiredMotionGraphicsConfigurationTypeDef, total=False):
    MotionGraphicsInsertion: MotionGraphicsInsertion


class MotionGraphicsSettingsTypeDef(TypedDict, total=False):
    HtmlMotionGraphicsSettings: Dict[str, Any]


class Mp2SettingsTypeDef(TypedDict, total=False):
    Bitrate: float
    CodingMode: Mp2CodingMode
    SampleRate: float


class Mpeg2FilterSettingsTypeDef(TypedDict, total=False):
    TemporalFilterSettings: "TemporalFilterSettingsTypeDef"


class _RequiredMpeg2SettingsTypeDef(TypedDict):
    FramerateDenominator: int
    FramerateNumerator: int


class Mpeg2SettingsTypeDef(_RequiredMpeg2SettingsTypeDef, total=False):
    AdaptiveQuantization: Mpeg2AdaptiveQuantization
    AfdSignaling: AfdSignaling
    ColorMetadata: Mpeg2ColorMetadata
    ColorSpace: Mpeg2ColorSpace
    DisplayAspectRatio: Mpeg2DisplayRatio
    FilterSettings: "Mpeg2FilterSettingsTypeDef"
    FixedAfd: FixedAfd
    GopClosedCadence: int
    GopNumBFrames: int
    GopSize: float
    GopSizeUnits: Mpeg2GopSizeUnits
    ScanType: Mpeg2ScanType
    SubgopLength: Mpeg2SubGopLength
    TimecodeInsertion: Mpeg2TimecodeInsertionBehavior


class _RequiredMsSmoothGroupSettingsTypeDef(TypedDict):
    Destination: "OutputLocationRefTypeDef"


class MsSmoothGroupSettingsTypeDef(_RequiredMsSmoothGroupSettingsTypeDef, total=False):
    AcquisitionPointId: str
    AudioOnlyTimecodeControl: SmoothGroupAudioOnlyTimecodeControl
    CertificateMode: SmoothGroupCertificateMode
    ConnectionRetryInterval: int
    EventId: str
    EventIdMode: SmoothGroupEventIdMode
    EventStopBehavior: SmoothGroupEventStopBehavior
    FilecacheDuration: int
    FragmentLength: int
    InputLossAction: InputLossActionForMsSmoothOut
    NumRetries: int
    RestartDelay: int
    SegmentationMode: SmoothGroupSegmentationMode
    SendDelayMs: int
    SparseTrackType: SmoothGroupSparseTrackType
    StreamManifestBehavior: SmoothGroupStreamManifestBehavior
    TimestampOffset: str
    TimestampOffsetMode: SmoothGroupTimestampOffsetMode


class MsSmoothOutputSettingsTypeDef(TypedDict, total=False):
    H265PackagingType: MsSmoothH265PackagingType
    NameModifier: str


class MultiplexMediaConnectOutputDestinationSettingsTypeDef(TypedDict, total=False):
    EntitlementArn: str


class MultiplexOutputDestinationTypeDef(TypedDict, total=False):
    MediaConnectSettings: "MultiplexMediaConnectOutputDestinationSettingsTypeDef"


class MultiplexOutputSettingsTypeDef(TypedDict):
    Destination: "OutputLocationRefTypeDef"


class MultiplexProgramChannelDestinationSettingsTypeDef(TypedDict, total=False):
    MultiplexId: str
    ProgramName: str


class MultiplexProgramPacketIdentifiersMapTypeDef(TypedDict, total=False):
    AudioPids: List[int]
    DvbSubPids: List[int]
    DvbTeletextPid: int
    EtvPlatformPid: int
    EtvSignalPid: int
    KlvDataPids: List[int]
    PcrPid: int
    PmtPid: int
    PrivateMetadataPid: int
    Scte27Pids: List[int]
    Scte35Pid: int
    TimedMetadataPid: int
    VideoPid: int


class MultiplexProgramPipelineDetailTypeDef(TypedDict, total=False):
    ActiveChannelPipeline: str
    PipelineId: str


class MultiplexProgramServiceDescriptorTypeDef(TypedDict):
    ProviderName: str
    ServiceName: str


class _RequiredMultiplexProgramSettingsTypeDef(TypedDict):
    ProgramNumber: int


class MultiplexProgramSettingsTypeDef(_RequiredMultiplexProgramSettingsTypeDef, total=False):
    PreferredChannelPipeline: PreferredChannelPipeline
    ServiceDescriptor: "MultiplexProgramServiceDescriptorTypeDef"
    VideoSettings: "MultiplexVideoSettingsTypeDef"


class MultiplexProgramSummaryTypeDef(TypedDict, total=False):
    ChannelId: str
    ProgramName: str


class MultiplexProgramTypeDef(TypedDict, total=False):
    ChannelId: str
    MultiplexProgramSettings: "MultiplexProgramSettingsTypeDef"
    PacketIdentifiersMap: "MultiplexProgramPacketIdentifiersMapTypeDef"
    PipelineDetails: List["MultiplexProgramPipelineDetailTypeDef"]
    ProgramName: str


class MultiplexSettingsSummaryTypeDef(TypedDict, total=False):
    TransportStreamBitrate: int


class _RequiredMultiplexSettingsTypeDef(TypedDict):
    TransportStreamBitrate: int
    TransportStreamId: int


class MultiplexSettingsTypeDef(_RequiredMultiplexSettingsTypeDef, total=False):
    MaximumVideoBufferDelayMilliseconds: int
    TransportStreamReservedBitrate: int


class MultiplexStatmuxVideoSettingsTypeDef(TypedDict, total=False):
    MaximumBitrate: int
    MinimumBitrate: int
    Priority: int


class MultiplexSummaryTypeDef(TypedDict, total=False):
    Arn: str
    AvailabilityZones: List[str]
    Id: str
    MultiplexSettings: "MultiplexSettingsSummaryTypeDef"
    Name: str
    PipelinesRunningCount: int
    ProgramCount: int
    State: MultiplexState
    Tags: Dict[str, str]


class MultiplexTypeDef(TypedDict, total=False):
    Arn: str
    AvailabilityZones: List[str]
    Destinations: List["MultiplexOutputDestinationTypeDef"]
    Id: str
    MultiplexSettings: "MultiplexSettingsTypeDef"
    Name: str
    PipelinesRunningCount: int
    ProgramCount: int
    State: MultiplexState
    Tags: Dict[str, str]


class MultiplexVideoSettingsTypeDef(TypedDict, total=False):
    ConstantBitrate: int
    StatmuxSettings: "MultiplexStatmuxVideoSettingsTypeDef"


class NetworkInputSettingsTypeDef(TypedDict, total=False):
    HlsInputSettings: "HlsInputSettingsTypeDef"
    ServerValidation: NetworkInputServerValidation


class NielsenConfigurationTypeDef(TypedDict, total=False):
    DistributorId: str
    NielsenPcmToId3Tagging: NielsenPcmToId3TaggingState


class OfferingTypeDef(TypedDict, total=False):
    Arn: str
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal["MONTHS"]
    FixedPrice: float
    OfferingDescription: str
    OfferingId: str
    OfferingType: Literal["NO_UPFRONT"]
    Region: str
    ResourceSpecification: "ReservationResourceSpecificationTypeDef"
    UsagePrice: float


class OutputDestinationSettingsTypeDef(TypedDict, total=False):
    PasswordParam: str
    StreamName: str
    Url: str
    Username: str


class OutputDestinationTypeDef(TypedDict, total=False):
    Id: str
    MediaPackageSettings: List["MediaPackageOutputDestinationSettingsTypeDef"]
    MultiplexSettings: "MultiplexProgramChannelDestinationSettingsTypeDef"
    Settings: List["OutputDestinationSettingsTypeDef"]


class OutputGroupSettingsTypeDef(TypedDict, total=False):
    ArchiveGroupSettings: "ArchiveGroupSettingsTypeDef"
    FrameCaptureGroupSettings: "FrameCaptureGroupSettingsTypeDef"
    HlsGroupSettings: "HlsGroupSettingsTypeDef"
    MediaPackageGroupSettings: "MediaPackageGroupSettingsTypeDef"
    MsSmoothGroupSettings: "MsSmoothGroupSettingsTypeDef"
    MultiplexGroupSettings: Dict[str, Any]
    RtmpGroupSettings: "RtmpGroupSettingsTypeDef"
    UdpGroupSettings: "UdpGroupSettingsTypeDef"


class _RequiredOutputGroupTypeDef(TypedDict):
    OutputGroupSettings: "OutputGroupSettingsTypeDef"
    Outputs: List["OutputTypeDef"]


class OutputGroupTypeDef(_RequiredOutputGroupTypeDef, total=False):
    Name: str


class OutputLocationRefTypeDef(TypedDict, total=False):
    DestinationRefId: str


class OutputSettingsTypeDef(TypedDict, total=False):
    ArchiveOutputSettings: "ArchiveOutputSettingsTypeDef"
    FrameCaptureOutputSettings: "FrameCaptureOutputSettingsTypeDef"
    HlsOutputSettings: "HlsOutputSettingsTypeDef"
    MediaPackageOutputSettings: Dict[str, Any]
    MsSmoothOutputSettings: "MsSmoothOutputSettingsTypeDef"
    MultiplexOutputSettings: "MultiplexOutputSettingsTypeDef"
    RtmpOutputSettings: "RtmpOutputSettingsTypeDef"
    UdpOutputSettings: "UdpOutputSettingsTypeDef"


class OutputTypeDef(TypedDict):
    AudioDescriptionNames: List[str]
    CaptionDescriptionNames: List[str]
    OutputName: str
    OutputSettings: "OutputSettingsTypeDef"
    VideoDescriptionName: str
    ResponseMetadata: "ResponseMetadata"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PauseStateScheduleActionSettingsTypeDef(TypedDict, total=False):
    Pipelines: List["PipelinePauseStateSettingsTypeDef"]


class PipelineDetailTypeDef(TypedDict, total=False):
    ActiveInputAttachmentName: str
    ActiveInputSwitchActionName: str
    ActiveMotionGraphicsActionName: str
    ActiveMotionGraphicsUri: str
    PipelineId: str


class PipelinePauseStateSettingsTypeDef(TypedDict):
    PipelineId: PipelineId


class PurchaseOfferingResponseTypeDef(TypedDict, total=False):
    Reservation: "ReservationTypeDef"


class _RequiredRemixSettingsTypeDef(TypedDict):
    ChannelMappings: List["AudioChannelMappingTypeDef"]


class RemixSettingsTypeDef(_RequiredRemixSettingsTypeDef, total=False):
    ChannelsIn: int
    ChannelsOut: int


class ReservationResourceSpecificationTypeDef(TypedDict, total=False):
    ChannelClass: ChannelClass
    Codec: ReservationCodec
    MaximumBitrate: ReservationMaximumBitrate
    MaximumFramerate: ReservationMaximumFramerate
    Resolution: ReservationResolution
    ResourceType: ReservationResourceType
    SpecialFeature: ReservationSpecialFeature
    VideoQuality: ReservationVideoQuality


class ReservationTypeDef(TypedDict, total=False):
    Arn: str
    Count: int
    CurrencyCode: str
    Duration: int
    DurationUnits: Literal["MONTHS"]
    End: str
    FixedPrice: float
    Name: str
    OfferingDescription: str
    OfferingId: str
    OfferingType: Literal["NO_UPFRONT"]
    Region: str
    ReservationId: str
    ResourceSpecification: "ReservationResourceSpecificationTypeDef"
    Start: str
    State: ReservationState
    Tags: Dict[str, str]
    UsagePrice: float


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RtmpGroupSettingsTypeDef(TypedDict, total=False):
    AdMarkers: List[Literal["ON_CUE_POINT_SCTE35"]]
    AuthenticationScheme: AuthenticationScheme
    CacheFullBehavior: RtmpCacheFullBehavior
    CacheLength: int
    CaptionData: RtmpCaptionData
    InputLossAction: InputLossActionForRtmpOut
    RestartDelay: int


class _RequiredRtmpOutputSettingsTypeDef(TypedDict):
    Destination: "OutputLocationRefTypeDef"


class RtmpOutputSettingsTypeDef(_RequiredRtmpOutputSettingsTypeDef, total=False):
    CertificateMode: RtmpOutputCertificateMode
    ConnectionRetryInterval: int
    NumRetries: int


class ScheduleActionSettingsTypeDef(TypedDict, total=False):
    HlsId3SegmentTaggingSettings: "HlsId3SegmentTaggingScheduleActionSettingsTypeDef"
    HlsTimedMetadataSettings: "HlsTimedMetadataScheduleActionSettingsTypeDef"
    InputPrepareSettings: "InputPrepareScheduleActionSettingsTypeDef"
    InputSwitchSettings: "InputSwitchScheduleActionSettingsTypeDef"
    MotionGraphicsImageActivateSettings: "MotionGraphicsActivateScheduleActionSettingsTypeDef"
    MotionGraphicsImageDeactivateSettings: Dict[str, Any]
    PauseStateSettings: "PauseStateScheduleActionSettingsTypeDef"
    Scte35ReturnToNetworkSettings: "Scte35ReturnToNetworkScheduleActionSettingsTypeDef"
    Scte35SpliceInsertSettings: "Scte35SpliceInsertScheduleActionSettingsTypeDef"
    Scte35TimeSignalSettings: "Scte35TimeSignalScheduleActionSettingsTypeDef"
    StaticImageActivateSettings: "StaticImageActivateScheduleActionSettingsTypeDef"
    StaticImageDeactivateSettings: "StaticImageDeactivateScheduleActionSettingsTypeDef"


class ScheduleActionStartSettingsTypeDef(TypedDict, total=False):
    FixedModeScheduleActionStartSettings: "FixedModeScheduleActionStartSettingsTypeDef"
    FollowModeScheduleActionStartSettings: "FollowModeScheduleActionStartSettingsTypeDef"
    ImmediateModeScheduleActionStartSettings: Dict[str, Any]


class ScheduleActionTypeDef(TypedDict):
    ActionName: str
    ScheduleActionSettings: "ScheduleActionSettingsTypeDef"
    ScheduleActionStartSettings: "ScheduleActionStartSettingsTypeDef"


class Scte20SourceSettingsTypeDef(TypedDict, total=False):
    Convert608To708: Scte20Convert608To708
    Source608ChannelNumber: int


class Scte27SourceSettingsTypeDef(TypedDict, total=False):
    Pid: int


class Scte35DeliveryRestrictionsTypeDef(TypedDict):
    ArchiveAllowedFlag: Scte35ArchiveAllowedFlag
    DeviceRestrictions: Scte35DeviceRestrictions
    NoRegionalBlackoutFlag: Scte35NoRegionalBlackoutFlag
    WebDeliveryAllowedFlag: Scte35WebDeliveryAllowedFlag


class Scte35DescriptorSettingsTypeDef(TypedDict):
    SegmentationDescriptorScte35DescriptorSettings: "Scte35SegmentationDescriptorTypeDef"


class Scte35DescriptorTypeDef(TypedDict):
    Scte35DescriptorSettings: "Scte35DescriptorSettingsTypeDef"


class Scte35ReturnToNetworkScheduleActionSettingsTypeDef(TypedDict):
    SpliceEventId: int


class _RequiredScte35SegmentationDescriptorTypeDef(TypedDict):
    SegmentationCancelIndicator: Scte35SegmentationCancelIndicator
    SegmentationEventId: int


class Scte35SegmentationDescriptorTypeDef(
    _RequiredScte35SegmentationDescriptorTypeDef, total=False
):
    DeliveryRestrictions: "Scte35DeliveryRestrictionsTypeDef"
    SegmentNum: int
    SegmentationDuration: int
    SegmentationTypeId: int
    SegmentationUpid: str
    SegmentationUpidType: int
    SegmentsExpected: int
    SubSegmentNum: int
    SubSegmentsExpected: int


class _RequiredScte35SpliceInsertScheduleActionSettingsTypeDef(TypedDict):
    SpliceEventId: int


class Scte35SpliceInsertScheduleActionSettingsTypeDef(
    _RequiredScte35SpliceInsertScheduleActionSettingsTypeDef, total=False
):
    Duration: int


class Scte35SpliceInsertTypeDef(TypedDict, total=False):
    AdAvailOffset: int
    NoRegionalBlackoutFlag: Scte35SpliceInsertNoRegionalBlackoutBehavior
    WebDeliveryAllowedFlag: Scte35SpliceInsertWebDeliveryAllowedBehavior


class Scte35TimeSignalAposTypeDef(TypedDict, total=False):
    AdAvailOffset: int
    NoRegionalBlackoutFlag: Scte35AposNoRegionalBlackoutBehavior
    WebDeliveryAllowedFlag: Scte35AposWebDeliveryAllowedBehavior


class Scte35TimeSignalScheduleActionSettingsTypeDef(TypedDict):
    Scte35Descriptors: List["Scte35DescriptorTypeDef"]


class _RequiredStandardHlsSettingsTypeDef(TypedDict):
    M3u8Settings: "M3u8SettingsTypeDef"


class StandardHlsSettingsTypeDef(_RequiredStandardHlsSettingsTypeDef, total=False):
    AudioRenditionSets: str


class StartChannelResponseTypeDef(TypedDict, total=False):
    Arn: str
    CdiInputSpecification: "CdiInputSpecificationTypeDef"
    ChannelClass: ChannelClass
    Destinations: List["OutputDestinationTypeDef"]
    EgressEndpoints: List["ChannelEgressEndpointTypeDef"]
    EncoderSettings: "EncoderSettingsTypeDef"
    Id: str
    InputAttachments: List["InputAttachmentTypeDef"]
    InputSpecification: "InputSpecificationTypeDef"
    LogLevel: LogLevel
    Name: str
    PipelineDetails: List["PipelineDetailTypeDef"]
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelState
    Tags: Dict[str, str]
    Vpc: "VpcOutputSettingsDescriptionTypeDef"


class StartMultiplexResponseTypeDef(TypedDict, total=False):
    Arn: str
    AvailabilityZones: List[str]
    Destinations: List["MultiplexOutputDestinationTypeDef"]
    Id: str
    MultiplexSettings: "MultiplexSettingsTypeDef"
    Name: str
    PipelinesRunningCount: int
    ProgramCount: int
    State: MultiplexState
    Tags: Dict[str, str]


class StartTimecodeTypeDef(TypedDict, total=False):
    Timecode: str


class _RequiredStaticImageActivateScheduleActionSettingsTypeDef(TypedDict):
    Image: "InputLocationTypeDef"


class StaticImageActivateScheduleActionSettingsTypeDef(
    _RequiredStaticImageActivateScheduleActionSettingsTypeDef, total=False
):
    Duration: int
    FadeIn: int
    FadeOut: int
    Height: int
    ImageX: int
    ImageY: int
    Layer: int
    Opacity: int
    Width: int


class StaticImageDeactivateScheduleActionSettingsTypeDef(TypedDict, total=False):
    FadeOut: int
    Layer: int


class _RequiredStaticKeySettingsTypeDef(TypedDict):
    StaticKeyValue: str


class StaticKeySettingsTypeDef(_RequiredStaticKeySettingsTypeDef, total=False):
    KeyProviderServer: "InputLocationTypeDef"


class StopChannelResponseTypeDef(TypedDict, total=False):
    Arn: str
    CdiInputSpecification: "CdiInputSpecificationTypeDef"
    ChannelClass: ChannelClass
    Destinations: List["OutputDestinationTypeDef"]
    EgressEndpoints: List["ChannelEgressEndpointTypeDef"]
    EncoderSettings: "EncoderSettingsTypeDef"
    Id: str
    InputAttachments: List["InputAttachmentTypeDef"]
    InputSpecification: "InputSpecificationTypeDef"
    LogLevel: LogLevel
    Name: str
    PipelineDetails: List["PipelineDetailTypeDef"]
    PipelinesRunningCount: int
    RoleArn: str
    State: ChannelState
    Tags: Dict[str, str]
    Vpc: "VpcOutputSettingsDescriptionTypeDef"


class StopMultiplexResponseTypeDef(TypedDict, total=False):
    Arn: str
    AvailabilityZones: List[str]
    Destinations: List["MultiplexOutputDestinationTypeDef"]
    Id: str
    MultiplexSettings: "MultiplexSettingsTypeDef"
    Name: str
    PipelinesRunningCount: int
    ProgramCount: int
    State: MultiplexState
    Tags: Dict[str, str]


class StopTimecodeTypeDef(TypedDict, total=False):
    LastFrameClippingBehavior: LastFrameClippingBehavior
    Timecode: str


class TeletextSourceSettingsTypeDef(TypedDict, total=False):
    OutputRectangle: "CaptionRectangleTypeDef"
    PageNumber: str


class TemporalFilterSettingsTypeDef(TypedDict, total=False):
    PostFilterSharpening: TemporalFilterPostFilterSharpening
    Strength: TemporalFilterStrength


class _RequiredTimecodeConfigTypeDef(TypedDict):
    Source: TimecodeConfigSource


class TimecodeConfigTypeDef(_RequiredTimecodeConfigTypeDef, total=False):
    SyncThreshold: int


class TransferringInputDeviceSummaryTypeDef(TypedDict, total=False):
    Id: str
    Message: str
    TargetCustomerId: str
    TransferType: InputDeviceTransferType


class TtmlDestinationSettingsTypeDef(TypedDict, total=False):
    StyleControl: TtmlDestinationStyleControl


class UdpContainerSettingsTypeDef(TypedDict, total=False):
    M2tsSettings: "M2tsSettingsTypeDef"


class UdpGroupSettingsTypeDef(TypedDict, total=False):
    InputLossAction: InputLossActionForUdpOut
    TimedMetadataId3Frame: UdpTimedMetadataId3Frame
    TimedMetadataId3Period: int


class _RequiredUdpOutputSettingsTypeDef(TypedDict):
    ContainerSettings: "UdpContainerSettingsTypeDef"
    Destination: "OutputLocationRefTypeDef"


class UdpOutputSettingsTypeDef(_RequiredUdpOutputSettingsTypeDef, total=False):
    BufferMsec: int
    FecOutputSettings: "FecOutputSettingsTypeDef"


class UpdateChannelClassResponseTypeDef(TypedDict, total=False):
    Channel: "ChannelTypeDef"


class UpdateChannelResponseTypeDef(TypedDict, total=False):
    Channel: "ChannelTypeDef"


UpdateInputDeviceResponseTypeDef = TypedDict(
    "UpdateInputDeviceResponseTypeDef",
    {
        "Arn": str,
        "ConnectionState": InputDeviceConnectionState,
        "DeviceSettingsSyncState": DeviceSettingsSyncState,
        "DeviceUpdateStatus": DeviceUpdateStatus,
        "HdDeviceSettings": "InputDeviceHdSettingsTypeDef",
        "Id": str,
        "MacAddress": str,
        "Name": str,
        "NetworkSettings": "InputDeviceNetworkSettingsTypeDef",
        "SerialNumber": str,
        "Type": Literal["HD"],
        "UhdDeviceSettings": "InputDeviceUhdSettingsTypeDef",
    },
    total=False,
)


class UpdateInputResponseTypeDef(TypedDict, total=False):
    Input: "InputTypeDef"


class UpdateInputSecurityGroupResponseTypeDef(TypedDict, total=False):
    SecurityGroup: "InputSecurityGroupTypeDef"


class UpdateMultiplexProgramResponseTypeDef(TypedDict, total=False):
    MultiplexProgram: "MultiplexProgramTypeDef"


class UpdateMultiplexResponseTypeDef(TypedDict, total=False):
    Multiplex: "MultiplexTypeDef"


class UpdateReservationResponseTypeDef(TypedDict, total=False):
    Reservation: "ReservationTypeDef"


class VideoBlackFailoverSettingsTypeDef(TypedDict, total=False):
    BlackDetectThreshold: float
    VideoBlackThresholdMsec: int


class VideoCodecSettingsTypeDef(TypedDict, total=False):
    FrameCaptureSettings: "FrameCaptureSettingsTypeDef"
    H264Settings: "H264SettingsTypeDef"
    H265Settings: "H265SettingsTypeDef"
    Mpeg2Settings: "Mpeg2SettingsTypeDef"


class _RequiredVideoDescriptionTypeDef(TypedDict):
    Name: str


class VideoDescriptionTypeDef(_RequiredVideoDescriptionTypeDef, total=False):
    CodecSettings: "VideoCodecSettingsTypeDef"
    Height: int
    RespondToAfd: VideoDescriptionRespondToAfd
    ScalingBehavior: VideoDescriptionScalingBehavior
    Sharpness: int
    Width: int


class VideoSelectorColorSpaceSettingsTypeDef(TypedDict, total=False):
    Hdr10Settings: "Hdr10SettingsTypeDef"


class VideoSelectorPidTypeDef(TypedDict, total=False):
    Pid: int


class VideoSelectorProgramIdTypeDef(TypedDict, total=False):
    ProgramId: int


class VideoSelectorSettingsTypeDef(TypedDict, total=False):
    VideoSelectorPid: "VideoSelectorPidTypeDef"
    VideoSelectorProgramId: "VideoSelectorProgramIdTypeDef"


class VideoSelectorTypeDef(TypedDict, total=False):
    ColorSpace: VideoSelectorColorSpace
    ColorSpaceSettings: "VideoSelectorColorSpaceSettingsTypeDef"
    ColorSpaceUsage: VideoSelectorColorSpaceUsage
    SelectorSettings: "VideoSelectorSettingsTypeDef"


class VpcOutputSettingsDescriptionTypeDef(TypedDict, total=False):
    AvailabilityZones: List[str]
    NetworkInterfaceIds: List[str]
    SecurityGroupIds: List[str]
    SubnetIds: List[str]


class _RequiredVpcOutputSettingsTypeDef(TypedDict):
    SubnetIds: List[str]


class VpcOutputSettingsTypeDef(_RequiredVpcOutputSettingsTypeDef, total=False):
    PublicAddressAllocationIds: List[str]
    SecurityGroupIds: List[str]


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int


class WavSettingsTypeDef(TypedDict, total=False):
    BitDepth: float
    CodingMode: WavCodingMode
    SampleRate: float
