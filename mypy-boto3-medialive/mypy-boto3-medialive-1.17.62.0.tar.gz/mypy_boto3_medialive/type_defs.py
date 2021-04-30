"""
Main interface for medialive service type definitions.

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
    AudioNormalizationAlgorithmControl,
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
    ContentType,
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
    HlsMediaStoreStorageClass,
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
    InputDeviceType,
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
    OfferingDurationUnits,
    OfferingType,
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
    RtmpAdMarkers,
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
    "BatchFailedResultModelTypeDef",
    "BatchScheduleActionCreateResultTypeDef",
    "BatchScheduleActionDeleteResultTypeDef",
    "BatchSuccessfulResultModelTypeDef",
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
    "InputDestinationTypeDef",
    "InputDestinationVpcTypeDef",
    "InputDeviceHdSettingsTypeDef",
    "InputDeviceNetworkSettingsTypeDef",
    "InputDeviceSettingsTypeDef",
    "InputDeviceSummaryTypeDef",
    "InputDeviceUhdSettingsTypeDef",
    "InputLocationTypeDef",
    "InputLossBehaviorTypeDef",
    "InputLossFailoverSettingsTypeDef",
    "InputPrepareScheduleActionSettingsTypeDef",
    "InputSecurityGroupTypeDef",
    "InputSettingsTypeDef",
    "InputSourceTypeDef",
    "InputSpecificationTypeDef",
    "InputSwitchScheduleActionSettingsTypeDef",
    "InputTypeDef",
    "InputWhitelistRuleTypeDef",
    "KeyProviderSettingsTypeDef",
    "M2tsSettingsTypeDef",
    "M3u8SettingsTypeDef",
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
    "PauseStateScheduleActionSettingsTypeDef",
    "PipelineDetailTypeDef",
    "PipelinePauseStateSettingsTypeDef",
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
    "StartTimecodeTypeDef",
    "StaticImageActivateScheduleActionSettingsTypeDef",
    "StaticImageDeactivateScheduleActionSettingsTypeDef",
    "StaticKeySettingsTypeDef",
    "StopTimecodeTypeDef",
    "TeletextSourceSettingsTypeDef",
    "TemporalFilterSettingsTypeDef",
    "TimecodeConfigTypeDef",
    "TransferringInputDeviceSummaryTypeDef",
    "TtmlDestinationSettingsTypeDef",
    "UdpContainerSettingsTypeDef",
    "UdpGroupSettingsTypeDef",
    "UdpOutputSettingsTypeDef",
    "VideoBlackFailoverSettingsTypeDef",
    "VideoCodecSettingsTypeDef",
    "VideoDescriptionTypeDef",
    "VideoSelectorColorSpaceSettingsTypeDef",
    "VideoSelectorPidTypeDef",
    "VideoSelectorProgramIdTypeDef",
    "VideoSelectorSettingsTypeDef",
    "VideoSelectorTypeDef",
    "VpcOutputSettingsDescriptionTypeDef",
    "WavSettingsTypeDef",
    "BatchDeleteResponseTypeDef",
    "BatchScheduleActionCreateRequestTypeDef",
    "BatchScheduleActionDeleteRequestTypeDef",
    "BatchStartResponseTypeDef",
    "BatchStopResponseTypeDef",
    "BatchUpdateScheduleResponseTypeDef",
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
    "InputDestinationRequestTypeDef",
    "InputDeviceConfigurableSettingsTypeDef",
    "InputDeviceRequestTypeDef",
    "InputSourceRequestTypeDef",
    "InputVpcRequestTypeDef",
    "InputWhitelistRuleCidrTypeDef",
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
    "MediaConnectFlowRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PurchaseOfferingResponseTypeDef",
    "StartChannelResponseTypeDef",
    "StartMultiplexResponseTypeDef",
    "StopChannelResponseTypeDef",
    "StopMultiplexResponseTypeDef",
    "UpdateChannelClassResponseTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdateInputDeviceResponseTypeDef",
    "UpdateInputResponseTypeDef",
    "UpdateInputSecurityGroupResponseTypeDef",
    "UpdateMultiplexProgramResponseTypeDef",
    "UpdateMultiplexResponseTypeDef",
    "UpdateReservationResponseTypeDef",
    "VpcOutputSettingsTypeDef",
    "WaiterConfigTypeDef",
)

AacSettingsTypeDef = TypedDict(
    "AacSettingsTypeDef",
    {
        "Bitrate": float,
        "CodingMode": AacCodingMode,
        "InputType": AacInputType,
        "Profile": AacProfile,
        "RateControlMode": AacRateControlMode,
        "RawFormat": AacRawFormat,
        "SampleRate": float,
        "Spec": AacSpec,
        "VbrQuality": AacVbrQuality,
    },
    total=False,
)

Ac3SettingsTypeDef = TypedDict(
    "Ac3SettingsTypeDef",
    {
        "Bitrate": float,
        "BitstreamMode": Ac3BitstreamMode,
        "CodingMode": Ac3CodingMode,
        "Dialnorm": int,
        "DrcProfile": Ac3DrcProfile,
        "LfeFilter": Ac3LfeFilter,
        "MetadataControl": Ac3MetadataControl,
    },
    total=False,
)

AncillarySourceSettingsTypeDef = TypedDict(
    "AncillarySourceSettingsTypeDef", {"SourceAncillaryChannelNumber": int}, total=False
)

ArchiveCdnSettingsTypeDef = TypedDict(
    "ArchiveCdnSettingsTypeDef", {"ArchiveS3Settings": "ArchiveS3SettingsTypeDef"}, total=False
)

ArchiveContainerSettingsTypeDef = TypedDict(
    "ArchiveContainerSettingsTypeDef",
    {"M2tsSettings": "M2tsSettingsTypeDef", "RawSettings": Dict[str, Any]},
    total=False,
)

_RequiredArchiveGroupSettingsTypeDef = TypedDict(
    "_RequiredArchiveGroupSettingsTypeDef", {"Destination": "OutputLocationRefTypeDef"}
)
_OptionalArchiveGroupSettingsTypeDef = TypedDict(
    "_OptionalArchiveGroupSettingsTypeDef",
    {"ArchiveCdnSettings": "ArchiveCdnSettingsTypeDef", "RolloverInterval": int},
    total=False,
)


class ArchiveGroupSettingsTypeDef(
    _RequiredArchiveGroupSettingsTypeDef, _OptionalArchiveGroupSettingsTypeDef
):
    pass


_RequiredArchiveOutputSettingsTypeDef = TypedDict(
    "_RequiredArchiveOutputSettingsTypeDef",
    {"ContainerSettings": "ArchiveContainerSettingsTypeDef"},
)
_OptionalArchiveOutputSettingsTypeDef = TypedDict(
    "_OptionalArchiveOutputSettingsTypeDef", {"Extension": str, "NameModifier": str}, total=False
)


class ArchiveOutputSettingsTypeDef(
    _RequiredArchiveOutputSettingsTypeDef, _OptionalArchiveOutputSettingsTypeDef
):
    pass


ArchiveS3SettingsTypeDef = TypedDict(
    "ArchiveS3SettingsTypeDef", {"CannedAcl": S3CannedAcl}, total=False
)

AudioChannelMappingTypeDef = TypedDict(
    "AudioChannelMappingTypeDef",
    {"InputChannelLevels": List["InputChannelLevelTypeDef"], "OutputChannel": int},
)

AudioCodecSettingsTypeDef = TypedDict(
    "AudioCodecSettingsTypeDef",
    {
        "AacSettings": "AacSettingsTypeDef",
        "Ac3Settings": "Ac3SettingsTypeDef",
        "Eac3Settings": "Eac3SettingsTypeDef",
        "Mp2Settings": "Mp2SettingsTypeDef",
        "PassThroughSettings": Dict[str, Any],
        "WavSettings": "WavSettingsTypeDef",
    },
    total=False,
)

_RequiredAudioDescriptionTypeDef = TypedDict(
    "_RequiredAudioDescriptionTypeDef", {"AudioSelectorName": str, "Name": str}
)
_OptionalAudioDescriptionTypeDef = TypedDict(
    "_OptionalAudioDescriptionTypeDef",
    {
        "AudioNormalizationSettings": "AudioNormalizationSettingsTypeDef",
        "AudioType": AudioType,
        "AudioTypeControl": AudioDescriptionAudioTypeControl,
        "CodecSettings": "AudioCodecSettingsTypeDef",
        "LanguageCode": str,
        "LanguageCodeControl": AudioDescriptionLanguageCodeControl,
        "RemixSettings": "RemixSettingsTypeDef",
        "StreamName": str,
    },
    total=False,
)


class AudioDescriptionTypeDef(_RequiredAudioDescriptionTypeDef, _OptionalAudioDescriptionTypeDef):
    pass


_RequiredAudioLanguageSelectionTypeDef = TypedDict(
    "_RequiredAudioLanguageSelectionTypeDef", {"LanguageCode": str}
)
_OptionalAudioLanguageSelectionTypeDef = TypedDict(
    "_OptionalAudioLanguageSelectionTypeDef",
    {"LanguageSelectionPolicy": AudioLanguageSelectionPolicy},
    total=False,
)


class AudioLanguageSelectionTypeDef(
    _RequiredAudioLanguageSelectionTypeDef, _OptionalAudioLanguageSelectionTypeDef
):
    pass


AudioNormalizationSettingsTypeDef = TypedDict(
    "AudioNormalizationSettingsTypeDef",
    {
        "Algorithm": AudioNormalizationAlgorithm,
        "AlgorithmControl": AudioNormalizationAlgorithmControl,
        "TargetLkfs": float,
    },
    total=False,
)

AudioOnlyHlsSettingsTypeDef = TypedDict(
    "AudioOnlyHlsSettingsTypeDef",
    {
        "AudioGroupId": str,
        "AudioOnlyImage": "InputLocationTypeDef",
        "AudioTrackType": AudioOnlyHlsTrackType,
        "SegmentType": AudioOnlyHlsSegmentType,
    },
    total=False,
)

AudioPidSelectionTypeDef = TypedDict("AudioPidSelectionTypeDef", {"Pid": int})

AudioSelectorSettingsTypeDef = TypedDict(
    "AudioSelectorSettingsTypeDef",
    {
        "AudioLanguageSelection": "AudioLanguageSelectionTypeDef",
        "AudioPidSelection": "AudioPidSelectionTypeDef",
        "AudioTrackSelection": "AudioTrackSelectionTypeDef",
    },
    total=False,
)

_RequiredAudioSelectorTypeDef = TypedDict("_RequiredAudioSelectorTypeDef", {"Name": str})
_OptionalAudioSelectorTypeDef = TypedDict(
    "_OptionalAudioSelectorTypeDef",
    {"SelectorSettings": "AudioSelectorSettingsTypeDef"},
    total=False,
)


class AudioSelectorTypeDef(_RequiredAudioSelectorTypeDef, _OptionalAudioSelectorTypeDef):
    pass


_RequiredAudioSilenceFailoverSettingsTypeDef = TypedDict(
    "_RequiredAudioSilenceFailoverSettingsTypeDef", {"AudioSelectorName": str}
)
_OptionalAudioSilenceFailoverSettingsTypeDef = TypedDict(
    "_OptionalAudioSilenceFailoverSettingsTypeDef", {"AudioSilenceThresholdMsec": int}, total=False
)


class AudioSilenceFailoverSettingsTypeDef(
    _RequiredAudioSilenceFailoverSettingsTypeDef, _OptionalAudioSilenceFailoverSettingsTypeDef
):
    pass


AudioTrackSelectionTypeDef = TypedDict(
    "AudioTrackSelectionTypeDef", {"Tracks": List["AudioTrackTypeDef"]}
)

AudioTrackTypeDef = TypedDict("AudioTrackTypeDef", {"Track": int})

_RequiredAutomaticInputFailoverSettingsTypeDef = TypedDict(
    "_RequiredAutomaticInputFailoverSettingsTypeDef", {"SecondaryInputId": str}
)
_OptionalAutomaticInputFailoverSettingsTypeDef = TypedDict(
    "_OptionalAutomaticInputFailoverSettingsTypeDef",
    {
        "ErrorClearTimeMsec": int,
        "FailoverConditions": List["FailoverConditionTypeDef"],
        "InputPreference": InputPreference,
    },
    total=False,
)


class AutomaticInputFailoverSettingsTypeDef(
    _RequiredAutomaticInputFailoverSettingsTypeDef, _OptionalAutomaticInputFailoverSettingsTypeDef
):
    pass


AvailBlankingTypeDef = TypedDict(
    "AvailBlankingTypeDef",
    {"AvailBlankingImage": "InputLocationTypeDef", "State": AvailBlankingState},
    total=False,
)

AvailConfigurationTypeDef = TypedDict(
    "AvailConfigurationTypeDef", {"AvailSettings": "AvailSettingsTypeDef"}, total=False
)

AvailSettingsTypeDef = TypedDict(
    "AvailSettingsTypeDef",
    {
        "Scte35SpliceInsert": "Scte35SpliceInsertTypeDef",
        "Scte35TimeSignalApos": "Scte35TimeSignalAposTypeDef",
    },
    total=False,
)

BatchFailedResultModelTypeDef = TypedDict(
    "BatchFailedResultModelTypeDef",
    {"Arn": str, "Code": str, "Id": str, "Message": str},
    total=False,
)

BatchScheduleActionCreateResultTypeDef = TypedDict(
    "BatchScheduleActionCreateResultTypeDef", {"ScheduleActions": List["ScheduleActionTypeDef"]}
)

BatchScheduleActionDeleteResultTypeDef = TypedDict(
    "BatchScheduleActionDeleteResultTypeDef", {"ScheduleActions": List["ScheduleActionTypeDef"]}
)

BatchSuccessfulResultModelTypeDef = TypedDict(
    "BatchSuccessfulResultModelTypeDef", {"Arn": str, "Id": str, "State": str}, total=False
)

BlackoutSlateTypeDef = TypedDict(
    "BlackoutSlateTypeDef",
    {
        "BlackoutSlateImage": "InputLocationTypeDef",
        "NetworkEndBlackout": BlackoutSlateNetworkEndBlackout,
        "NetworkEndBlackoutImage": "InputLocationTypeDef",
        "NetworkId": str,
        "State": BlackoutSlateState,
    },
    total=False,
)

BurnInDestinationSettingsTypeDef = TypedDict(
    "BurnInDestinationSettingsTypeDef",
    {
        "Alignment": BurnInAlignment,
        "BackgroundColor": BurnInBackgroundColor,
        "BackgroundOpacity": int,
        "Font": "InputLocationTypeDef",
        "FontColor": BurnInFontColor,
        "FontOpacity": int,
        "FontResolution": int,
        "FontSize": str,
        "OutlineColor": BurnInOutlineColor,
        "OutlineSize": int,
        "ShadowColor": BurnInShadowColor,
        "ShadowOpacity": int,
        "ShadowXOffset": int,
        "ShadowYOffset": int,
        "TeletextGridControl": BurnInTeletextGridControl,
        "XPosition": int,
        "YPosition": int,
    },
    total=False,
)

_RequiredCaptionDescriptionTypeDef = TypedDict(
    "_RequiredCaptionDescriptionTypeDef", {"CaptionSelectorName": str, "Name": str}
)
_OptionalCaptionDescriptionTypeDef = TypedDict(
    "_OptionalCaptionDescriptionTypeDef",
    {
        "DestinationSettings": "CaptionDestinationSettingsTypeDef",
        "LanguageCode": str,
        "LanguageDescription": str,
    },
    total=False,
)


class CaptionDescriptionTypeDef(
    _RequiredCaptionDescriptionTypeDef, _OptionalCaptionDescriptionTypeDef
):
    pass


CaptionDestinationSettingsTypeDef = TypedDict(
    "CaptionDestinationSettingsTypeDef",
    {
        "AribDestinationSettings": Dict[str, Any],
        "BurnInDestinationSettings": "BurnInDestinationSettingsTypeDef",
        "DvbSubDestinationSettings": "DvbSubDestinationSettingsTypeDef",
        "EbuTtDDestinationSettings": "EbuTtDDestinationSettingsTypeDef",
        "EmbeddedDestinationSettings": Dict[str, Any],
        "EmbeddedPlusScte20DestinationSettings": Dict[str, Any],
        "RtmpCaptionInfoDestinationSettings": Dict[str, Any],
        "Scte20PlusEmbeddedDestinationSettings": Dict[str, Any],
        "Scte27DestinationSettings": Dict[str, Any],
        "SmpteTtDestinationSettings": Dict[str, Any],
        "TeletextDestinationSettings": Dict[str, Any],
        "TtmlDestinationSettings": "TtmlDestinationSettingsTypeDef",
        "WebvttDestinationSettings": Dict[str, Any],
    },
    total=False,
)

CaptionLanguageMappingTypeDef = TypedDict(
    "CaptionLanguageMappingTypeDef",
    {"CaptionChannel": int, "LanguageCode": str, "LanguageDescription": str},
)

CaptionRectangleTypeDef = TypedDict(
    "CaptionRectangleTypeDef",
    {"Height": float, "LeftOffset": float, "TopOffset": float, "Width": float},
)

CaptionSelectorSettingsTypeDef = TypedDict(
    "CaptionSelectorSettingsTypeDef",
    {
        "AncillarySourceSettings": "AncillarySourceSettingsTypeDef",
        "AribSourceSettings": Dict[str, Any],
        "DvbSubSourceSettings": "DvbSubSourceSettingsTypeDef",
        "EmbeddedSourceSettings": "EmbeddedSourceSettingsTypeDef",
        "Scte20SourceSettings": "Scte20SourceSettingsTypeDef",
        "Scte27SourceSettings": "Scte27SourceSettingsTypeDef",
        "TeletextSourceSettings": "TeletextSourceSettingsTypeDef",
    },
    total=False,
)

_RequiredCaptionSelectorTypeDef = TypedDict("_RequiredCaptionSelectorTypeDef", {"Name": str})
_OptionalCaptionSelectorTypeDef = TypedDict(
    "_OptionalCaptionSelectorTypeDef",
    {"LanguageCode": str, "SelectorSettings": "CaptionSelectorSettingsTypeDef"},
    total=False,
)


class CaptionSelectorTypeDef(_RequiredCaptionSelectorTypeDef, _OptionalCaptionSelectorTypeDef):
    pass


CdiInputSpecificationTypeDef = TypedDict(
    "CdiInputSpecificationTypeDef", {"Resolution": CdiInputResolution}, total=False
)

ChannelEgressEndpointTypeDef = TypedDict(
    "ChannelEgressEndpointTypeDef", {"SourceIp": str}, total=False
)

ChannelSummaryTypeDef = TypedDict(
    "ChannelSummaryTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClass,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevel,
        "Name": str,
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelState,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
    },
    total=False,
)

ChannelTypeDef = TypedDict(
    "ChannelTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClass,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevel,
        "Name": str,
        "PipelineDetails": List["PipelineDetailTypeDef"],
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelState,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
    },
    total=False,
)

_RequiredDvbNitSettingsTypeDef = TypedDict(
    "_RequiredDvbNitSettingsTypeDef", {"NetworkId": int, "NetworkName": str}
)
_OptionalDvbNitSettingsTypeDef = TypedDict(
    "_OptionalDvbNitSettingsTypeDef", {"RepInterval": int}, total=False
)


class DvbNitSettingsTypeDef(_RequiredDvbNitSettingsTypeDef, _OptionalDvbNitSettingsTypeDef):
    pass


DvbSdtSettingsTypeDef = TypedDict(
    "DvbSdtSettingsTypeDef",
    {
        "OutputSdt": DvbSdtOutputSdt,
        "RepInterval": int,
        "ServiceName": str,
        "ServiceProviderName": str,
    },
    total=False,
)

DvbSubDestinationSettingsTypeDef = TypedDict(
    "DvbSubDestinationSettingsTypeDef",
    {
        "Alignment": DvbSubDestinationAlignment,
        "BackgroundColor": DvbSubDestinationBackgroundColor,
        "BackgroundOpacity": int,
        "Font": "InputLocationTypeDef",
        "FontColor": DvbSubDestinationFontColor,
        "FontOpacity": int,
        "FontResolution": int,
        "FontSize": str,
        "OutlineColor": DvbSubDestinationOutlineColor,
        "OutlineSize": int,
        "ShadowColor": DvbSubDestinationShadowColor,
        "ShadowOpacity": int,
        "ShadowXOffset": int,
        "ShadowYOffset": int,
        "TeletextGridControl": DvbSubDestinationTeletextGridControl,
        "XPosition": int,
        "YPosition": int,
    },
    total=False,
)

DvbSubSourceSettingsTypeDef = TypedDict("DvbSubSourceSettingsTypeDef", {"Pid": int}, total=False)

DvbTdtSettingsTypeDef = TypedDict("DvbTdtSettingsTypeDef", {"RepInterval": int}, total=False)

Eac3SettingsTypeDef = TypedDict(
    "Eac3SettingsTypeDef",
    {
        "AttenuationControl": Eac3AttenuationControl,
        "Bitrate": float,
        "BitstreamMode": Eac3BitstreamMode,
        "CodingMode": Eac3CodingMode,
        "DcFilter": Eac3DcFilter,
        "Dialnorm": int,
        "DrcLine": Eac3DrcLine,
        "DrcRf": Eac3DrcRf,
        "LfeControl": Eac3LfeControl,
        "LfeFilter": Eac3LfeFilter,
        "LoRoCenterMixLevel": float,
        "LoRoSurroundMixLevel": float,
        "LtRtCenterMixLevel": float,
        "LtRtSurroundMixLevel": float,
        "MetadataControl": Eac3MetadataControl,
        "PassthroughControl": Eac3PassthroughControl,
        "PhaseControl": Eac3PhaseControl,
        "StereoDownmix": Eac3StereoDownmix,
        "SurroundExMode": Eac3SurroundExMode,
        "SurroundMode": Eac3SurroundMode,
    },
    total=False,
)

EbuTtDDestinationSettingsTypeDef = TypedDict(
    "EbuTtDDestinationSettingsTypeDef",
    {
        "CopyrightHolder": str,
        "FillLineGap": EbuTtDFillLineGapControl,
        "FontFamily": str,
        "StyleControl": EbuTtDDestinationStyleControl,
    },
    total=False,
)

EmbeddedSourceSettingsTypeDef = TypedDict(
    "EmbeddedSourceSettingsTypeDef",
    {
        "Convert608To708": EmbeddedConvert608To708,
        "Scte20Detection": EmbeddedScte20Detection,
        "Source608ChannelNumber": int,
        "Source608TrackNumber": int,
    },
    total=False,
)

_RequiredEncoderSettingsTypeDef = TypedDict(
    "_RequiredEncoderSettingsTypeDef",
    {
        "AudioDescriptions": List["AudioDescriptionTypeDef"],
        "OutputGroups": List["OutputGroupTypeDef"],
        "TimecodeConfig": "TimecodeConfigTypeDef",
        "VideoDescriptions": List["VideoDescriptionTypeDef"],
    },
)
_OptionalEncoderSettingsTypeDef = TypedDict(
    "_OptionalEncoderSettingsTypeDef",
    {
        "AvailBlanking": "AvailBlankingTypeDef",
        "AvailConfiguration": "AvailConfigurationTypeDef",
        "BlackoutSlate": "BlackoutSlateTypeDef",
        "CaptionDescriptions": List["CaptionDescriptionTypeDef"],
        "FeatureActivations": "FeatureActivationsTypeDef",
        "GlobalConfiguration": "GlobalConfigurationTypeDef",
        "MotionGraphicsConfiguration": "MotionGraphicsConfigurationTypeDef",
        "NielsenConfiguration": "NielsenConfigurationTypeDef",
    },
    total=False,
)


class EncoderSettingsTypeDef(_RequiredEncoderSettingsTypeDef, _OptionalEncoderSettingsTypeDef):
    pass


FailoverConditionSettingsTypeDef = TypedDict(
    "FailoverConditionSettingsTypeDef",
    {
        "AudioSilenceSettings": "AudioSilenceFailoverSettingsTypeDef",
        "InputLossSettings": "InputLossFailoverSettingsTypeDef",
        "VideoBlackSettings": "VideoBlackFailoverSettingsTypeDef",
    },
    total=False,
)

FailoverConditionTypeDef = TypedDict(
    "FailoverConditionTypeDef",
    {"FailoverConditionSettings": "FailoverConditionSettingsTypeDef"},
    total=False,
)

FeatureActivationsTypeDef = TypedDict(
    "FeatureActivationsTypeDef",
    {"InputPrepareScheduleActions": FeatureActivationsInputPrepareScheduleActions},
    total=False,
)

FecOutputSettingsTypeDef = TypedDict(
    "FecOutputSettingsTypeDef",
    {"ColumnDepth": int, "IncludeFec": FecOutputIncludeFec, "RowLength": int},
    total=False,
)

FixedModeScheduleActionStartSettingsTypeDef = TypedDict(
    "FixedModeScheduleActionStartSettingsTypeDef", {"Time": str}
)

Fmp4HlsSettingsTypeDef = TypedDict(
    "Fmp4HlsSettingsTypeDef",
    {
        "AudioRenditionSets": str,
        "NielsenId3Behavior": Fmp4NielsenId3Behavior,
        "TimedMetadataBehavior": Fmp4TimedMetadataBehavior,
    },
    total=False,
)

FollowModeScheduleActionStartSettingsTypeDef = TypedDict(
    "FollowModeScheduleActionStartSettingsTypeDef",
    {"FollowPoint": FollowPoint, "ReferenceActionName": str},
)

FrameCaptureCdnSettingsTypeDef = TypedDict(
    "FrameCaptureCdnSettingsTypeDef",
    {"FrameCaptureS3Settings": "FrameCaptureS3SettingsTypeDef"},
    total=False,
)

_RequiredFrameCaptureGroupSettingsTypeDef = TypedDict(
    "_RequiredFrameCaptureGroupSettingsTypeDef", {"Destination": "OutputLocationRefTypeDef"}
)
_OptionalFrameCaptureGroupSettingsTypeDef = TypedDict(
    "_OptionalFrameCaptureGroupSettingsTypeDef",
    {"FrameCaptureCdnSettings": "FrameCaptureCdnSettingsTypeDef"},
    total=False,
)


class FrameCaptureGroupSettingsTypeDef(
    _RequiredFrameCaptureGroupSettingsTypeDef, _OptionalFrameCaptureGroupSettingsTypeDef
):
    pass


FrameCaptureOutputSettingsTypeDef = TypedDict(
    "FrameCaptureOutputSettingsTypeDef", {"NameModifier": str}, total=False
)

FrameCaptureS3SettingsTypeDef = TypedDict(
    "FrameCaptureS3SettingsTypeDef", {"CannedAcl": S3CannedAcl}, total=False
)

FrameCaptureSettingsTypeDef = TypedDict(
    "FrameCaptureSettingsTypeDef",
    {"CaptureInterval": int, "CaptureIntervalUnits": FrameCaptureIntervalUnit},
    total=False,
)

GlobalConfigurationTypeDef = TypedDict(
    "GlobalConfigurationTypeDef",
    {
        "InitialAudioGain": int,
        "InputEndAction": GlobalConfigurationInputEndAction,
        "InputLossBehavior": "InputLossBehaviorTypeDef",
        "OutputLockingMode": GlobalConfigurationOutputLockingMode,
        "OutputTimingSource": GlobalConfigurationOutputTimingSource,
        "SupportLowFramerateInputs": GlobalConfigurationLowFramerateInputs,
    },
    total=False,
)

H264ColorSpaceSettingsTypeDef = TypedDict(
    "H264ColorSpaceSettingsTypeDef",
    {
        "ColorSpacePassthroughSettings": Dict[str, Any],
        "Rec601Settings": Dict[str, Any],
        "Rec709Settings": Dict[str, Any],
    },
    total=False,
)

H264FilterSettingsTypeDef = TypedDict(
    "H264FilterSettingsTypeDef",
    {"TemporalFilterSettings": "TemporalFilterSettingsTypeDef"},
    total=False,
)

H264SettingsTypeDef = TypedDict(
    "H264SettingsTypeDef",
    {
        "AdaptiveQuantization": H264AdaptiveQuantization,
        "AfdSignaling": AfdSignaling,
        "Bitrate": int,
        "BufFillPct": int,
        "BufSize": int,
        "ColorMetadata": H264ColorMetadata,
        "ColorSpaceSettings": "H264ColorSpaceSettingsTypeDef",
        "EntropyEncoding": H264EntropyEncoding,
        "FilterSettings": "H264FilterSettingsTypeDef",
        "FixedAfd": FixedAfd,
        "FlickerAq": H264FlickerAq,
        "ForceFieldPictures": H264ForceFieldPictures,
        "FramerateControl": H264FramerateControl,
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "GopBReference": H264GopBReference,
        "GopClosedCadence": int,
        "GopNumBFrames": int,
        "GopSize": float,
        "GopSizeUnits": H264GopSizeUnits,
        "Level": H264Level,
        "LookAheadRateControl": H264LookAheadRateControl,
        "MaxBitrate": int,
        "MinIInterval": int,
        "NumRefFrames": int,
        "ParControl": H264ParControl,
        "ParDenominator": int,
        "ParNumerator": int,
        "Profile": H264Profile,
        "QualityLevel": H264QualityLevel,
        "QvbrQualityLevel": int,
        "RateControlMode": H264RateControlMode,
        "ScanType": H264ScanType,
        "SceneChangeDetect": H264SceneChangeDetect,
        "Slices": int,
        "Softness": int,
        "SpatialAq": H264SpatialAq,
        "SubgopLength": H264SubGopLength,
        "Syntax": H264Syntax,
        "TemporalAq": H264TemporalAq,
        "TimecodeInsertion": H264TimecodeInsertionBehavior,
    },
    total=False,
)

H265ColorSpaceSettingsTypeDef = TypedDict(
    "H265ColorSpaceSettingsTypeDef",
    {
        "ColorSpacePassthroughSettings": Dict[str, Any],
        "Hdr10Settings": "Hdr10SettingsTypeDef",
        "Rec601Settings": Dict[str, Any],
        "Rec709Settings": Dict[str, Any],
    },
    total=False,
)

H265FilterSettingsTypeDef = TypedDict(
    "H265FilterSettingsTypeDef",
    {"TemporalFilterSettings": "TemporalFilterSettingsTypeDef"},
    total=False,
)

_RequiredH265SettingsTypeDef = TypedDict(
    "_RequiredH265SettingsTypeDef", {"FramerateDenominator": int, "FramerateNumerator": int}
)
_OptionalH265SettingsTypeDef = TypedDict(
    "_OptionalH265SettingsTypeDef",
    {
        "AdaptiveQuantization": H265AdaptiveQuantization,
        "AfdSignaling": AfdSignaling,
        "AlternativeTransferFunction": H265AlternativeTransferFunction,
        "Bitrate": int,
        "BufSize": int,
        "ColorMetadata": H265ColorMetadata,
        "ColorSpaceSettings": "H265ColorSpaceSettingsTypeDef",
        "FilterSettings": "H265FilterSettingsTypeDef",
        "FixedAfd": FixedAfd,
        "FlickerAq": H265FlickerAq,
        "GopClosedCadence": int,
        "GopSize": float,
        "GopSizeUnits": H265GopSizeUnits,
        "Level": H265Level,
        "LookAheadRateControl": H265LookAheadRateControl,
        "MaxBitrate": int,
        "MinIInterval": int,
        "ParDenominator": int,
        "ParNumerator": int,
        "Profile": H265Profile,
        "QvbrQualityLevel": int,
        "RateControlMode": H265RateControlMode,
        "ScanType": H265ScanType,
        "SceneChangeDetect": H265SceneChangeDetect,
        "Slices": int,
        "Tier": H265Tier,
        "TimecodeInsertion": H265TimecodeInsertionBehavior,
    },
    total=False,
)


class H265SettingsTypeDef(_RequiredH265SettingsTypeDef, _OptionalH265SettingsTypeDef):
    pass


Hdr10SettingsTypeDef = TypedDict(
    "Hdr10SettingsTypeDef", {"MaxCll": int, "MaxFall": int}, total=False
)

HlsAkamaiSettingsTypeDef = TypedDict(
    "HlsAkamaiSettingsTypeDef",
    {
        "ConnectionRetryInterval": int,
        "FilecacheDuration": int,
        "HttpTransferMode": HlsAkamaiHttpTransferMode,
        "NumRetries": int,
        "RestartDelay": int,
        "Salt": str,
        "Token": str,
    },
    total=False,
)

HlsBasicPutSettingsTypeDef = TypedDict(
    "HlsBasicPutSettingsTypeDef",
    {
        "ConnectionRetryInterval": int,
        "FilecacheDuration": int,
        "NumRetries": int,
        "RestartDelay": int,
    },
    total=False,
)

HlsCdnSettingsTypeDef = TypedDict(
    "HlsCdnSettingsTypeDef",
    {
        "HlsAkamaiSettings": "HlsAkamaiSettingsTypeDef",
        "HlsBasicPutSettings": "HlsBasicPutSettingsTypeDef",
        "HlsMediaStoreSettings": "HlsMediaStoreSettingsTypeDef",
        "HlsS3Settings": "HlsS3SettingsTypeDef",
        "HlsWebdavSettings": "HlsWebdavSettingsTypeDef",
    },
    total=False,
)

_RequiredHlsGroupSettingsTypeDef = TypedDict(
    "_RequiredHlsGroupSettingsTypeDef", {"Destination": "OutputLocationRefTypeDef"}
)
_OptionalHlsGroupSettingsTypeDef = TypedDict(
    "_OptionalHlsGroupSettingsTypeDef",
    {
        "AdMarkers": List[HlsAdMarkers],
        "BaseUrlContent": str,
        "BaseUrlContent1": str,
        "BaseUrlManifest": str,
        "BaseUrlManifest1": str,
        "CaptionLanguageMappings": List["CaptionLanguageMappingTypeDef"],
        "CaptionLanguageSetting": HlsCaptionLanguageSetting,
        "ClientCache": HlsClientCache,
        "CodecSpecification": HlsCodecSpecification,
        "ConstantIv": str,
        "DirectoryStructure": HlsDirectoryStructure,
        "DiscontinuityTags": HlsDiscontinuityTags,
        "EncryptionType": HlsEncryptionType,
        "HlsCdnSettings": "HlsCdnSettingsTypeDef",
        "HlsId3SegmentTagging": HlsId3SegmentTaggingState,
        "IFrameOnlyPlaylists": IFrameOnlyPlaylistType,
        "IncompleteSegmentBehavior": HlsIncompleteSegmentBehavior,
        "IndexNSegments": int,
        "InputLossAction": InputLossActionForHlsOut,
        "IvInManifest": HlsIvInManifest,
        "IvSource": HlsIvSource,
        "KeepSegments": int,
        "KeyFormat": str,
        "KeyFormatVersions": str,
        "KeyProviderSettings": "KeyProviderSettingsTypeDef",
        "ManifestCompression": HlsManifestCompression,
        "ManifestDurationFormat": HlsManifestDurationFormat,
        "MinSegmentLength": int,
        "Mode": HlsMode,
        "OutputSelection": HlsOutputSelection,
        "ProgramDateTime": HlsProgramDateTime,
        "ProgramDateTimePeriod": int,
        "RedundantManifest": HlsRedundantManifest,
        "SegmentLength": int,
        "SegmentationMode": HlsSegmentationMode,
        "SegmentsPerSubdirectory": int,
        "StreamInfResolution": HlsStreamInfResolution,
        "TimedMetadataId3Frame": HlsTimedMetadataId3Frame,
        "TimedMetadataId3Period": int,
        "TimestampDeltaMilliseconds": int,
        "TsFileMode": HlsTsFileMode,
    },
    total=False,
)


class HlsGroupSettingsTypeDef(_RequiredHlsGroupSettingsTypeDef, _OptionalHlsGroupSettingsTypeDef):
    pass


HlsId3SegmentTaggingScheduleActionSettingsTypeDef = TypedDict(
    "HlsId3SegmentTaggingScheduleActionSettingsTypeDef", {"Tag": str}
)

HlsInputSettingsTypeDef = TypedDict(
    "HlsInputSettingsTypeDef",
    {"Bandwidth": int, "BufferSegments": int, "Retries": int, "RetryInterval": int},
    total=False,
)

HlsMediaStoreSettingsTypeDef = TypedDict(
    "HlsMediaStoreSettingsTypeDef",
    {
        "ConnectionRetryInterval": int,
        "FilecacheDuration": int,
        "MediaStoreStorageClass": HlsMediaStoreStorageClass,
        "NumRetries": int,
        "RestartDelay": int,
    },
    total=False,
)

_RequiredHlsOutputSettingsTypeDef = TypedDict(
    "_RequiredHlsOutputSettingsTypeDef", {"HlsSettings": "HlsSettingsTypeDef"}
)
_OptionalHlsOutputSettingsTypeDef = TypedDict(
    "_OptionalHlsOutputSettingsTypeDef",
    {"H265PackagingType": HlsH265PackagingType, "NameModifier": str, "SegmentModifier": str},
    total=False,
)


class HlsOutputSettingsTypeDef(
    _RequiredHlsOutputSettingsTypeDef, _OptionalHlsOutputSettingsTypeDef
):
    pass


HlsS3SettingsTypeDef = TypedDict("HlsS3SettingsTypeDef", {"CannedAcl": S3CannedAcl}, total=False)

HlsSettingsTypeDef = TypedDict(
    "HlsSettingsTypeDef",
    {
        "AudioOnlyHlsSettings": "AudioOnlyHlsSettingsTypeDef",
        "Fmp4HlsSettings": "Fmp4HlsSettingsTypeDef",
        "FrameCaptureHlsSettings": Dict[str, Any],
        "StandardHlsSettings": "StandardHlsSettingsTypeDef",
    },
    total=False,
)

HlsTimedMetadataScheduleActionSettingsTypeDef = TypedDict(
    "HlsTimedMetadataScheduleActionSettingsTypeDef", {"Id3": str}
)

HlsWebdavSettingsTypeDef = TypedDict(
    "HlsWebdavSettingsTypeDef",
    {
        "ConnectionRetryInterval": int,
        "FilecacheDuration": int,
        "HttpTransferMode": HlsWebdavHttpTransferMode,
        "NumRetries": int,
        "RestartDelay": int,
    },
    total=False,
)

InputAttachmentTypeDef = TypedDict(
    "InputAttachmentTypeDef",
    {
        "AutomaticInputFailoverSettings": "AutomaticInputFailoverSettingsTypeDef",
        "InputAttachmentName": str,
        "InputId": str,
        "InputSettings": "InputSettingsTypeDef",
    },
    total=False,
)

InputChannelLevelTypeDef = TypedDict("InputChannelLevelTypeDef", {"Gain": int, "InputChannel": int})

_RequiredInputClippingSettingsTypeDef = TypedDict(
    "_RequiredInputClippingSettingsTypeDef", {"InputTimecodeSource": InputTimecodeSource}
)
_OptionalInputClippingSettingsTypeDef = TypedDict(
    "_OptionalInputClippingSettingsTypeDef",
    {"StartTimecode": "StartTimecodeTypeDef", "StopTimecode": "StopTimecodeTypeDef"},
    total=False,
)


class InputClippingSettingsTypeDef(
    _RequiredInputClippingSettingsTypeDef, _OptionalInputClippingSettingsTypeDef
):
    pass


InputDestinationTypeDef = TypedDict(
    "InputDestinationTypeDef",
    {"Ip": str, "Port": str, "Url": str, "Vpc": "InputDestinationVpcTypeDef"},
    total=False,
)

InputDestinationVpcTypeDef = TypedDict(
    "InputDestinationVpcTypeDef", {"AvailabilityZone": str, "NetworkInterfaceId": str}, total=False
)

InputDeviceHdSettingsTypeDef = TypedDict(
    "InputDeviceHdSettingsTypeDef",
    {
        "ActiveInput": InputDeviceActiveInput,
        "ConfiguredInput": InputDeviceConfiguredInput,
        "DeviceState": InputDeviceState,
        "Framerate": float,
        "Height": int,
        "MaxBitrate": int,
        "ScanType": InputDeviceScanType,
        "Width": int,
    },
    total=False,
)

InputDeviceNetworkSettingsTypeDef = TypedDict(
    "InputDeviceNetworkSettingsTypeDef",
    {
        "DnsAddresses": List[str],
        "Gateway": str,
        "IpAddress": str,
        "IpScheme": InputDeviceIpScheme,
        "SubnetMask": str,
    },
    total=False,
)

InputDeviceSettingsTypeDef = TypedDict("InputDeviceSettingsTypeDef", {"Id": str}, total=False)

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
        "Type": InputDeviceType,
        "UhdDeviceSettings": "InputDeviceUhdSettingsTypeDef",
    },
    total=False,
)

InputDeviceUhdSettingsTypeDef = TypedDict(
    "InputDeviceUhdSettingsTypeDef",
    {
        "ActiveInput": InputDeviceActiveInput,
        "ConfiguredInput": InputDeviceConfiguredInput,
        "DeviceState": InputDeviceState,
        "Framerate": float,
        "Height": int,
        "MaxBitrate": int,
        "ScanType": InputDeviceScanType,
        "Width": int,
    },
    total=False,
)

_RequiredInputLocationTypeDef = TypedDict("_RequiredInputLocationTypeDef", {"Uri": str})
_OptionalInputLocationTypeDef = TypedDict(
    "_OptionalInputLocationTypeDef", {"PasswordParam": str, "Username": str}, total=False
)


class InputLocationTypeDef(_RequiredInputLocationTypeDef, _OptionalInputLocationTypeDef):
    pass


InputLossBehaviorTypeDef = TypedDict(
    "InputLossBehaviorTypeDef",
    {
        "BlackFrameMsec": int,
        "InputLossImageColor": str,
        "InputLossImageSlate": "InputLocationTypeDef",
        "InputLossImageType": InputLossImageType,
        "RepeatFrameMsec": int,
    },
    total=False,
)

InputLossFailoverSettingsTypeDef = TypedDict(
    "InputLossFailoverSettingsTypeDef", {"InputLossThresholdMsec": int}, total=False
)

InputPrepareScheduleActionSettingsTypeDef = TypedDict(
    "InputPrepareScheduleActionSettingsTypeDef",
    {
        "InputAttachmentNameReference": str,
        "InputClippingSettings": "InputClippingSettingsTypeDef",
        "UrlPath": List[str],
    },
    total=False,
)

InputSecurityGroupTypeDef = TypedDict(
    "InputSecurityGroupTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Inputs": List[str],
        "State": InputSecurityGroupState,
        "Tags": Dict[str, str],
        "WhitelistRules": List["InputWhitelistRuleTypeDef"],
    },
    total=False,
)

InputSettingsTypeDef = TypedDict(
    "InputSettingsTypeDef",
    {
        "AudioSelectors": List["AudioSelectorTypeDef"],
        "CaptionSelectors": List["CaptionSelectorTypeDef"],
        "DeblockFilter": InputDeblockFilter,
        "DenoiseFilter": InputDenoiseFilter,
        "FilterStrength": int,
        "InputFilter": InputFilter,
        "NetworkInputSettings": "NetworkInputSettingsTypeDef",
        "Smpte2038DataPreference": Smpte2038DataPreference,
        "SourceEndBehavior": InputSourceEndBehavior,
        "VideoSelector": "VideoSelectorTypeDef",
    },
    total=False,
)

InputSourceTypeDef = TypedDict(
    "InputSourceTypeDef", {"PasswordParam": str, "Url": str, "Username": str}, total=False
)

InputSpecificationTypeDef = TypedDict(
    "InputSpecificationTypeDef",
    {"Codec": InputCodec, "MaximumBitrate": InputMaximumBitrate, "Resolution": InputResolution},
    total=False,
)

_RequiredInputSwitchScheduleActionSettingsTypeDef = TypedDict(
    "_RequiredInputSwitchScheduleActionSettingsTypeDef", {"InputAttachmentNameReference": str}
)
_OptionalInputSwitchScheduleActionSettingsTypeDef = TypedDict(
    "_OptionalInputSwitchScheduleActionSettingsTypeDef",
    {"InputClippingSettings": "InputClippingSettingsTypeDef", "UrlPath": List[str]},
    total=False,
)


class InputSwitchScheduleActionSettingsTypeDef(
    _RequiredInputSwitchScheduleActionSettingsTypeDef,
    _OptionalInputSwitchScheduleActionSettingsTypeDef,
):
    pass


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

InputWhitelistRuleTypeDef = TypedDict("InputWhitelistRuleTypeDef", {"Cidr": str}, total=False)

KeyProviderSettingsTypeDef = TypedDict(
    "KeyProviderSettingsTypeDef", {"StaticKeySettings": "StaticKeySettingsTypeDef"}, total=False
)

M2tsSettingsTypeDef = TypedDict(
    "M2tsSettingsTypeDef",
    {
        "AbsentInputAudioBehavior": M2tsAbsentInputAudioBehavior,
        "Arib": M2tsArib,
        "AribCaptionsPid": str,
        "AribCaptionsPidControl": M2tsAribCaptionsPidControl,
        "AudioBufferModel": M2tsAudioBufferModel,
        "AudioFramesPerPes": int,
        "AudioPids": str,
        "AudioStreamType": M2tsAudioStreamType,
        "Bitrate": int,
        "BufferModel": M2tsBufferModel,
        "CcDescriptor": M2tsCcDescriptor,
        "DvbNitSettings": "DvbNitSettingsTypeDef",
        "DvbSdtSettings": "DvbSdtSettingsTypeDef",
        "DvbSubPids": str,
        "DvbTdtSettings": "DvbTdtSettingsTypeDef",
        "DvbTeletextPid": str,
        "Ebif": M2tsEbifControl,
        "EbpAudioInterval": M2tsAudioInterval,
        "EbpLookaheadMs": int,
        "EbpPlacement": M2tsEbpPlacement,
        "EcmPid": str,
        "EsRateInPes": M2tsEsRateInPes,
        "EtvPlatformPid": str,
        "EtvSignalPid": str,
        "FragmentTime": float,
        "Klv": M2tsKlv,
        "KlvDataPids": str,
        "NielsenId3Behavior": M2tsNielsenId3Behavior,
        "NullPacketBitrate": float,
        "PatInterval": int,
        "PcrControl": M2tsPcrControl,
        "PcrPeriod": int,
        "PcrPid": str,
        "PmtInterval": int,
        "PmtPid": str,
        "ProgramNum": int,
        "RateMode": M2tsRateMode,
        "Scte27Pids": str,
        "Scte35Control": M2tsScte35Control,
        "Scte35Pid": str,
        "SegmentationMarkers": M2tsSegmentationMarkers,
        "SegmentationStyle": M2tsSegmentationStyle,
        "SegmentationTime": float,
        "TimedMetadataBehavior": M2tsTimedMetadataBehavior,
        "TimedMetadataPid": str,
        "TransportStreamId": int,
        "VideoPid": str,
    },
    total=False,
)

M3u8SettingsTypeDef = TypedDict(
    "M3u8SettingsTypeDef",
    {
        "AudioFramesPerPes": int,
        "AudioPids": str,
        "EcmPid": str,
        "NielsenId3Behavior": M3u8NielsenId3Behavior,
        "PatInterval": int,
        "PcrControl": M3u8PcrControl,
        "PcrPeriod": int,
        "PcrPid": str,
        "PmtInterval": int,
        "PmtPid": str,
        "ProgramNum": int,
        "Scte35Behavior": M3u8Scte35Behavior,
        "Scte35Pid": str,
        "TimedMetadataBehavior": M3u8TimedMetadataBehavior,
        "TimedMetadataPid": str,
        "TransportStreamId": int,
        "VideoPid": str,
    },
    total=False,
)

MediaConnectFlowTypeDef = TypedDict("MediaConnectFlowTypeDef", {"FlowArn": str}, total=False)

MediaPackageGroupSettingsTypeDef = TypedDict(
    "MediaPackageGroupSettingsTypeDef", {"Destination": "OutputLocationRefTypeDef"}
)

MediaPackageOutputDestinationSettingsTypeDef = TypedDict(
    "MediaPackageOutputDestinationSettingsTypeDef", {"ChannelId": str}, total=False
)

MotionGraphicsActivateScheduleActionSettingsTypeDef = TypedDict(
    "MotionGraphicsActivateScheduleActionSettingsTypeDef",
    {"Duration": int, "PasswordParam": str, "Url": str, "Username": str},
    total=False,
)

_RequiredMotionGraphicsConfigurationTypeDef = TypedDict(
    "_RequiredMotionGraphicsConfigurationTypeDef",
    {"MotionGraphicsSettings": "MotionGraphicsSettingsTypeDef"},
)
_OptionalMotionGraphicsConfigurationTypeDef = TypedDict(
    "_OptionalMotionGraphicsConfigurationTypeDef",
    {"MotionGraphicsInsertion": MotionGraphicsInsertion},
    total=False,
)


class MotionGraphicsConfigurationTypeDef(
    _RequiredMotionGraphicsConfigurationTypeDef, _OptionalMotionGraphicsConfigurationTypeDef
):
    pass


MotionGraphicsSettingsTypeDef = TypedDict(
    "MotionGraphicsSettingsTypeDef", {"HtmlMotionGraphicsSettings": Dict[str, Any]}, total=False
)

Mp2SettingsTypeDef = TypedDict(
    "Mp2SettingsTypeDef",
    {"Bitrate": float, "CodingMode": Mp2CodingMode, "SampleRate": float},
    total=False,
)

Mpeg2FilterSettingsTypeDef = TypedDict(
    "Mpeg2FilterSettingsTypeDef",
    {"TemporalFilterSettings": "TemporalFilterSettingsTypeDef"},
    total=False,
)

_RequiredMpeg2SettingsTypeDef = TypedDict(
    "_RequiredMpeg2SettingsTypeDef", {"FramerateDenominator": int, "FramerateNumerator": int}
)
_OptionalMpeg2SettingsTypeDef = TypedDict(
    "_OptionalMpeg2SettingsTypeDef",
    {
        "AdaptiveQuantization": Mpeg2AdaptiveQuantization,
        "AfdSignaling": AfdSignaling,
        "ColorMetadata": Mpeg2ColorMetadata,
        "ColorSpace": Mpeg2ColorSpace,
        "DisplayAspectRatio": Mpeg2DisplayRatio,
        "FilterSettings": "Mpeg2FilterSettingsTypeDef",
        "FixedAfd": FixedAfd,
        "GopClosedCadence": int,
        "GopNumBFrames": int,
        "GopSize": float,
        "GopSizeUnits": Mpeg2GopSizeUnits,
        "ScanType": Mpeg2ScanType,
        "SubgopLength": Mpeg2SubGopLength,
        "TimecodeInsertion": Mpeg2TimecodeInsertionBehavior,
    },
    total=False,
)


class Mpeg2SettingsTypeDef(_RequiredMpeg2SettingsTypeDef, _OptionalMpeg2SettingsTypeDef):
    pass


_RequiredMsSmoothGroupSettingsTypeDef = TypedDict(
    "_RequiredMsSmoothGroupSettingsTypeDef", {"Destination": "OutputLocationRefTypeDef"}
)
_OptionalMsSmoothGroupSettingsTypeDef = TypedDict(
    "_OptionalMsSmoothGroupSettingsTypeDef",
    {
        "AcquisitionPointId": str,
        "AudioOnlyTimecodeControl": SmoothGroupAudioOnlyTimecodeControl,
        "CertificateMode": SmoothGroupCertificateMode,
        "ConnectionRetryInterval": int,
        "EventId": str,
        "EventIdMode": SmoothGroupEventIdMode,
        "EventStopBehavior": SmoothGroupEventStopBehavior,
        "FilecacheDuration": int,
        "FragmentLength": int,
        "InputLossAction": InputLossActionForMsSmoothOut,
        "NumRetries": int,
        "RestartDelay": int,
        "SegmentationMode": SmoothGroupSegmentationMode,
        "SendDelayMs": int,
        "SparseTrackType": SmoothGroupSparseTrackType,
        "StreamManifestBehavior": SmoothGroupStreamManifestBehavior,
        "TimestampOffset": str,
        "TimestampOffsetMode": SmoothGroupTimestampOffsetMode,
    },
    total=False,
)


class MsSmoothGroupSettingsTypeDef(
    _RequiredMsSmoothGroupSettingsTypeDef, _OptionalMsSmoothGroupSettingsTypeDef
):
    pass


MsSmoothOutputSettingsTypeDef = TypedDict(
    "MsSmoothOutputSettingsTypeDef",
    {"H265PackagingType": MsSmoothH265PackagingType, "NameModifier": str},
    total=False,
)

MultiplexMediaConnectOutputDestinationSettingsTypeDef = TypedDict(
    "MultiplexMediaConnectOutputDestinationSettingsTypeDef", {"EntitlementArn": str}, total=False
)

MultiplexOutputDestinationTypeDef = TypedDict(
    "MultiplexOutputDestinationTypeDef",
    {"MediaConnectSettings": "MultiplexMediaConnectOutputDestinationSettingsTypeDef"},
    total=False,
)

MultiplexOutputSettingsTypeDef = TypedDict(
    "MultiplexOutputSettingsTypeDef", {"Destination": "OutputLocationRefTypeDef"}
)

MultiplexProgramChannelDestinationSettingsTypeDef = TypedDict(
    "MultiplexProgramChannelDestinationSettingsTypeDef",
    {"MultiplexId": str, "ProgramName": str},
    total=False,
)

MultiplexProgramPacketIdentifiersMapTypeDef = TypedDict(
    "MultiplexProgramPacketIdentifiersMapTypeDef",
    {
        "AudioPids": List[int],
        "DvbSubPids": List[int],
        "DvbTeletextPid": int,
        "EtvPlatformPid": int,
        "EtvSignalPid": int,
        "KlvDataPids": List[int],
        "PcrPid": int,
        "PmtPid": int,
        "PrivateMetadataPid": int,
        "Scte27Pids": List[int],
        "Scte35Pid": int,
        "TimedMetadataPid": int,
        "VideoPid": int,
    },
    total=False,
)

MultiplexProgramPipelineDetailTypeDef = TypedDict(
    "MultiplexProgramPipelineDetailTypeDef",
    {"ActiveChannelPipeline": str, "PipelineId": str},
    total=False,
)

MultiplexProgramServiceDescriptorTypeDef = TypedDict(
    "MultiplexProgramServiceDescriptorTypeDef", {"ProviderName": str, "ServiceName": str}
)

_RequiredMultiplexProgramSettingsTypeDef = TypedDict(
    "_RequiredMultiplexProgramSettingsTypeDef", {"ProgramNumber": int}
)
_OptionalMultiplexProgramSettingsTypeDef = TypedDict(
    "_OptionalMultiplexProgramSettingsTypeDef",
    {
        "PreferredChannelPipeline": PreferredChannelPipeline,
        "ServiceDescriptor": "MultiplexProgramServiceDescriptorTypeDef",
        "VideoSettings": "MultiplexVideoSettingsTypeDef",
    },
    total=False,
)


class MultiplexProgramSettingsTypeDef(
    _RequiredMultiplexProgramSettingsTypeDef, _OptionalMultiplexProgramSettingsTypeDef
):
    pass


MultiplexProgramSummaryTypeDef = TypedDict(
    "MultiplexProgramSummaryTypeDef", {"ChannelId": str, "ProgramName": str}, total=False
)

MultiplexProgramTypeDef = TypedDict(
    "MultiplexProgramTypeDef",
    {
        "ChannelId": str,
        "MultiplexProgramSettings": "MultiplexProgramSettingsTypeDef",
        "PacketIdentifiersMap": "MultiplexProgramPacketIdentifiersMapTypeDef",
        "PipelineDetails": List["MultiplexProgramPipelineDetailTypeDef"],
        "ProgramName": str,
    },
    total=False,
)

MultiplexSettingsSummaryTypeDef = TypedDict(
    "MultiplexSettingsSummaryTypeDef", {"TransportStreamBitrate": int}, total=False
)

_RequiredMultiplexSettingsTypeDef = TypedDict(
    "_RequiredMultiplexSettingsTypeDef", {"TransportStreamBitrate": int, "TransportStreamId": int}
)
_OptionalMultiplexSettingsTypeDef = TypedDict(
    "_OptionalMultiplexSettingsTypeDef",
    {"MaximumVideoBufferDelayMilliseconds": int, "TransportStreamReservedBitrate": int},
    total=False,
)


class MultiplexSettingsTypeDef(
    _RequiredMultiplexSettingsTypeDef, _OptionalMultiplexSettingsTypeDef
):
    pass


MultiplexStatmuxVideoSettingsTypeDef = TypedDict(
    "MultiplexStatmuxVideoSettingsTypeDef",
    {"MaximumBitrate": int, "MinimumBitrate": int, "Priority": int},
    total=False,
)

MultiplexSummaryTypeDef = TypedDict(
    "MultiplexSummaryTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsSummaryTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexState,
        "Tags": Dict[str, str],
    },
    total=False,
)

MultiplexTypeDef = TypedDict(
    "MultiplexTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Destinations": List["MultiplexOutputDestinationTypeDef"],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexState,
        "Tags": Dict[str, str],
    },
    total=False,
)

MultiplexVideoSettingsTypeDef = TypedDict(
    "MultiplexVideoSettingsTypeDef",
    {"ConstantBitrate": int, "StatmuxSettings": "MultiplexStatmuxVideoSettingsTypeDef"},
    total=False,
)

NetworkInputSettingsTypeDef = TypedDict(
    "NetworkInputSettingsTypeDef",
    {
        "HlsInputSettings": "HlsInputSettingsTypeDef",
        "ServerValidation": NetworkInputServerValidation,
    },
    total=False,
)

NielsenConfigurationTypeDef = TypedDict(
    "NielsenConfigurationTypeDef",
    {"DistributorId": str, "NielsenPcmToId3Tagging": NielsenPcmToId3TaggingState},
    total=False,
)

OfferingTypeDef = TypedDict(
    "OfferingTypeDef",
    {
        "Arn": str,
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": OfferingDurationUnits,
        "FixedPrice": float,
        "OfferingDescription": str,
        "OfferingId": str,
        "OfferingType": OfferingType,
        "Region": str,
        "ResourceSpecification": "ReservationResourceSpecificationTypeDef",
        "UsagePrice": float,
    },
    total=False,
)

OutputDestinationSettingsTypeDef = TypedDict(
    "OutputDestinationSettingsTypeDef",
    {"PasswordParam": str, "StreamName": str, "Url": str, "Username": str},
    total=False,
)

OutputDestinationTypeDef = TypedDict(
    "OutputDestinationTypeDef",
    {
        "Id": str,
        "MediaPackageSettings": List["MediaPackageOutputDestinationSettingsTypeDef"],
        "MultiplexSettings": "MultiplexProgramChannelDestinationSettingsTypeDef",
        "Settings": List["OutputDestinationSettingsTypeDef"],
    },
    total=False,
)

OutputGroupSettingsTypeDef = TypedDict(
    "OutputGroupSettingsTypeDef",
    {
        "ArchiveGroupSettings": "ArchiveGroupSettingsTypeDef",
        "FrameCaptureGroupSettings": "FrameCaptureGroupSettingsTypeDef",
        "HlsGroupSettings": "HlsGroupSettingsTypeDef",
        "MediaPackageGroupSettings": "MediaPackageGroupSettingsTypeDef",
        "MsSmoothGroupSettings": "MsSmoothGroupSettingsTypeDef",
        "MultiplexGroupSettings": Dict[str, Any],
        "RtmpGroupSettings": "RtmpGroupSettingsTypeDef",
        "UdpGroupSettings": "UdpGroupSettingsTypeDef",
    },
    total=False,
)

_RequiredOutputGroupTypeDef = TypedDict(
    "_RequiredOutputGroupTypeDef",
    {"OutputGroupSettings": "OutputGroupSettingsTypeDef", "Outputs": List["OutputTypeDef"]},
)
_OptionalOutputGroupTypeDef = TypedDict("_OptionalOutputGroupTypeDef", {"Name": str}, total=False)


class OutputGroupTypeDef(_RequiredOutputGroupTypeDef, _OptionalOutputGroupTypeDef):
    pass


OutputLocationRefTypeDef = TypedDict(
    "OutputLocationRefTypeDef", {"DestinationRefId": str}, total=False
)

OutputSettingsTypeDef = TypedDict(
    "OutputSettingsTypeDef",
    {
        "ArchiveOutputSettings": "ArchiveOutputSettingsTypeDef",
        "FrameCaptureOutputSettings": "FrameCaptureOutputSettingsTypeDef",
        "HlsOutputSettings": "HlsOutputSettingsTypeDef",
        "MediaPackageOutputSettings": Dict[str, Any],
        "MsSmoothOutputSettings": "MsSmoothOutputSettingsTypeDef",
        "MultiplexOutputSettings": "MultiplexOutputSettingsTypeDef",
        "RtmpOutputSettings": "RtmpOutputSettingsTypeDef",
        "UdpOutputSettings": "UdpOutputSettingsTypeDef",
    },
    total=False,
)

_RequiredOutputTypeDef = TypedDict(
    "_RequiredOutputTypeDef", {"OutputSettings": "OutputSettingsTypeDef"}
)
_OptionalOutputTypeDef = TypedDict(
    "_OptionalOutputTypeDef",
    {
        "AudioDescriptionNames": List[str],
        "CaptionDescriptionNames": List[str],
        "OutputName": str,
        "VideoDescriptionName": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)


class OutputTypeDef(_RequiredOutputTypeDef, _OptionalOutputTypeDef):
    pass


PauseStateScheduleActionSettingsTypeDef = TypedDict(
    "PauseStateScheduleActionSettingsTypeDef",
    {"Pipelines": List["PipelinePauseStateSettingsTypeDef"]},
    total=False,
)

PipelineDetailTypeDef = TypedDict(
    "PipelineDetailTypeDef",
    {
        "ActiveInputAttachmentName": str,
        "ActiveInputSwitchActionName": str,
        "ActiveMotionGraphicsActionName": str,
        "ActiveMotionGraphicsUri": str,
        "PipelineId": str,
    },
    total=False,
)

PipelinePauseStateSettingsTypeDef = TypedDict(
    "PipelinePauseStateSettingsTypeDef", {"PipelineId": PipelineId}
)

_RequiredRemixSettingsTypeDef = TypedDict(
    "_RequiredRemixSettingsTypeDef", {"ChannelMappings": List["AudioChannelMappingTypeDef"]}
)
_OptionalRemixSettingsTypeDef = TypedDict(
    "_OptionalRemixSettingsTypeDef", {"ChannelsIn": int, "ChannelsOut": int}, total=False
)


class RemixSettingsTypeDef(_RequiredRemixSettingsTypeDef, _OptionalRemixSettingsTypeDef):
    pass


ReservationResourceSpecificationTypeDef = TypedDict(
    "ReservationResourceSpecificationTypeDef",
    {
        "ChannelClass": ChannelClass,
        "Codec": ReservationCodec,
        "MaximumBitrate": ReservationMaximumBitrate,
        "MaximumFramerate": ReservationMaximumFramerate,
        "Resolution": ReservationResolution,
        "ResourceType": ReservationResourceType,
        "SpecialFeature": ReservationSpecialFeature,
        "VideoQuality": ReservationVideoQuality,
    },
    total=False,
)

ReservationTypeDef = TypedDict(
    "ReservationTypeDef",
    {
        "Arn": str,
        "Count": int,
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": OfferingDurationUnits,
        "End": str,
        "FixedPrice": float,
        "Name": str,
        "OfferingDescription": str,
        "OfferingId": str,
        "OfferingType": OfferingType,
        "Region": str,
        "ReservationId": str,
        "ResourceSpecification": "ReservationResourceSpecificationTypeDef",
        "Start": str,
        "State": ReservationState,
        "Tags": Dict[str, str],
        "UsagePrice": float,
    },
    total=False,
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

RtmpGroupSettingsTypeDef = TypedDict(
    "RtmpGroupSettingsTypeDef",
    {
        "AdMarkers": List[RtmpAdMarkers],
        "AuthenticationScheme": AuthenticationScheme,
        "CacheFullBehavior": RtmpCacheFullBehavior,
        "CacheLength": int,
        "CaptionData": RtmpCaptionData,
        "InputLossAction": InputLossActionForRtmpOut,
        "RestartDelay": int,
    },
    total=False,
)

_RequiredRtmpOutputSettingsTypeDef = TypedDict(
    "_RequiredRtmpOutputSettingsTypeDef", {"Destination": "OutputLocationRefTypeDef"}
)
_OptionalRtmpOutputSettingsTypeDef = TypedDict(
    "_OptionalRtmpOutputSettingsTypeDef",
    {
        "CertificateMode": RtmpOutputCertificateMode,
        "ConnectionRetryInterval": int,
        "NumRetries": int,
    },
    total=False,
)


class RtmpOutputSettingsTypeDef(
    _RequiredRtmpOutputSettingsTypeDef, _OptionalRtmpOutputSettingsTypeDef
):
    pass


ScheduleActionSettingsTypeDef = TypedDict(
    "ScheduleActionSettingsTypeDef",
    {
        "HlsId3SegmentTaggingSettings": "HlsId3SegmentTaggingScheduleActionSettingsTypeDef",
        "HlsTimedMetadataSettings": "HlsTimedMetadataScheduleActionSettingsTypeDef",
        "InputPrepareSettings": "InputPrepareScheduleActionSettingsTypeDef",
        "InputSwitchSettings": "InputSwitchScheduleActionSettingsTypeDef",
        "MotionGraphicsImageActivateSettings": "MotionGraphicsActivateScheduleActionSettingsTypeDef",
        "MotionGraphicsImageDeactivateSettings": Dict[str, Any],
        "PauseStateSettings": "PauseStateScheduleActionSettingsTypeDef",
        "Scte35ReturnToNetworkSettings": "Scte35ReturnToNetworkScheduleActionSettingsTypeDef",
        "Scte35SpliceInsertSettings": "Scte35SpliceInsertScheduleActionSettingsTypeDef",
        "Scte35TimeSignalSettings": "Scte35TimeSignalScheduleActionSettingsTypeDef",
        "StaticImageActivateSettings": "StaticImageActivateScheduleActionSettingsTypeDef",
        "StaticImageDeactivateSettings": "StaticImageDeactivateScheduleActionSettingsTypeDef",
    },
    total=False,
)

ScheduleActionStartSettingsTypeDef = TypedDict(
    "ScheduleActionStartSettingsTypeDef",
    {
        "FixedModeScheduleActionStartSettings": "FixedModeScheduleActionStartSettingsTypeDef",
        "FollowModeScheduleActionStartSettings": "FollowModeScheduleActionStartSettingsTypeDef",
        "ImmediateModeScheduleActionStartSettings": Dict[str, Any],
    },
    total=False,
)

ScheduleActionTypeDef = TypedDict(
    "ScheduleActionTypeDef",
    {
        "ActionName": str,
        "ScheduleActionSettings": "ScheduleActionSettingsTypeDef",
        "ScheduleActionStartSettings": "ScheduleActionStartSettingsTypeDef",
    },
)

Scte20SourceSettingsTypeDef = TypedDict(
    "Scte20SourceSettingsTypeDef",
    {"Convert608To708": Scte20Convert608To708, "Source608ChannelNumber": int},
    total=False,
)

Scte27SourceSettingsTypeDef = TypedDict("Scte27SourceSettingsTypeDef", {"Pid": int}, total=False)

Scte35DeliveryRestrictionsTypeDef = TypedDict(
    "Scte35DeliveryRestrictionsTypeDef",
    {
        "ArchiveAllowedFlag": Scte35ArchiveAllowedFlag,
        "DeviceRestrictions": Scte35DeviceRestrictions,
        "NoRegionalBlackoutFlag": Scte35NoRegionalBlackoutFlag,
        "WebDeliveryAllowedFlag": Scte35WebDeliveryAllowedFlag,
    },
)

Scte35DescriptorSettingsTypeDef = TypedDict(
    "Scte35DescriptorSettingsTypeDef",
    {"SegmentationDescriptorScte35DescriptorSettings": "Scte35SegmentationDescriptorTypeDef"},
)

Scte35DescriptorTypeDef = TypedDict(
    "Scte35DescriptorTypeDef", {"Scte35DescriptorSettings": "Scte35DescriptorSettingsTypeDef"}
)

Scte35ReturnToNetworkScheduleActionSettingsTypeDef = TypedDict(
    "Scte35ReturnToNetworkScheduleActionSettingsTypeDef", {"SpliceEventId": int}
)

_RequiredScte35SegmentationDescriptorTypeDef = TypedDict(
    "_RequiredScte35SegmentationDescriptorTypeDef",
    {"SegmentationCancelIndicator": Scte35SegmentationCancelIndicator, "SegmentationEventId": int},
)
_OptionalScte35SegmentationDescriptorTypeDef = TypedDict(
    "_OptionalScte35SegmentationDescriptorTypeDef",
    {
        "DeliveryRestrictions": "Scte35DeliveryRestrictionsTypeDef",
        "SegmentNum": int,
        "SegmentationDuration": int,
        "SegmentationTypeId": int,
        "SegmentationUpid": str,
        "SegmentationUpidType": int,
        "SegmentsExpected": int,
        "SubSegmentNum": int,
        "SubSegmentsExpected": int,
    },
    total=False,
)


class Scte35SegmentationDescriptorTypeDef(
    _RequiredScte35SegmentationDescriptorTypeDef, _OptionalScte35SegmentationDescriptorTypeDef
):
    pass


_RequiredScte35SpliceInsertScheduleActionSettingsTypeDef = TypedDict(
    "_RequiredScte35SpliceInsertScheduleActionSettingsTypeDef", {"SpliceEventId": int}
)
_OptionalScte35SpliceInsertScheduleActionSettingsTypeDef = TypedDict(
    "_OptionalScte35SpliceInsertScheduleActionSettingsTypeDef", {"Duration": int}, total=False
)


class Scte35SpliceInsertScheduleActionSettingsTypeDef(
    _RequiredScte35SpliceInsertScheduleActionSettingsTypeDef,
    _OptionalScte35SpliceInsertScheduleActionSettingsTypeDef,
):
    pass


Scte35SpliceInsertTypeDef = TypedDict(
    "Scte35SpliceInsertTypeDef",
    {
        "AdAvailOffset": int,
        "NoRegionalBlackoutFlag": Scte35SpliceInsertNoRegionalBlackoutBehavior,
        "WebDeliveryAllowedFlag": Scte35SpliceInsertWebDeliveryAllowedBehavior,
    },
    total=False,
)

Scte35TimeSignalAposTypeDef = TypedDict(
    "Scte35TimeSignalAposTypeDef",
    {
        "AdAvailOffset": int,
        "NoRegionalBlackoutFlag": Scte35AposNoRegionalBlackoutBehavior,
        "WebDeliveryAllowedFlag": Scte35AposWebDeliveryAllowedBehavior,
    },
    total=False,
)

Scte35TimeSignalScheduleActionSettingsTypeDef = TypedDict(
    "Scte35TimeSignalScheduleActionSettingsTypeDef",
    {"Scte35Descriptors": List["Scte35DescriptorTypeDef"]},
)

_RequiredStandardHlsSettingsTypeDef = TypedDict(
    "_RequiredStandardHlsSettingsTypeDef", {"M3u8Settings": "M3u8SettingsTypeDef"}
)
_OptionalStandardHlsSettingsTypeDef = TypedDict(
    "_OptionalStandardHlsSettingsTypeDef", {"AudioRenditionSets": str}, total=False
)


class StandardHlsSettingsTypeDef(
    _RequiredStandardHlsSettingsTypeDef, _OptionalStandardHlsSettingsTypeDef
):
    pass


StartTimecodeTypeDef = TypedDict("StartTimecodeTypeDef", {"Timecode": str}, total=False)

_RequiredStaticImageActivateScheduleActionSettingsTypeDef = TypedDict(
    "_RequiredStaticImageActivateScheduleActionSettingsTypeDef", {"Image": "InputLocationTypeDef"}
)
_OptionalStaticImageActivateScheduleActionSettingsTypeDef = TypedDict(
    "_OptionalStaticImageActivateScheduleActionSettingsTypeDef",
    {
        "Duration": int,
        "FadeIn": int,
        "FadeOut": int,
        "Height": int,
        "ImageX": int,
        "ImageY": int,
        "Layer": int,
        "Opacity": int,
        "Width": int,
    },
    total=False,
)


class StaticImageActivateScheduleActionSettingsTypeDef(
    _RequiredStaticImageActivateScheduleActionSettingsTypeDef,
    _OptionalStaticImageActivateScheduleActionSettingsTypeDef,
):
    pass


StaticImageDeactivateScheduleActionSettingsTypeDef = TypedDict(
    "StaticImageDeactivateScheduleActionSettingsTypeDef",
    {"FadeOut": int, "Layer": int},
    total=False,
)

_RequiredStaticKeySettingsTypeDef = TypedDict(
    "_RequiredStaticKeySettingsTypeDef", {"StaticKeyValue": str}
)
_OptionalStaticKeySettingsTypeDef = TypedDict(
    "_OptionalStaticKeySettingsTypeDef", {"KeyProviderServer": "InputLocationTypeDef"}, total=False
)


class StaticKeySettingsTypeDef(
    _RequiredStaticKeySettingsTypeDef, _OptionalStaticKeySettingsTypeDef
):
    pass


StopTimecodeTypeDef = TypedDict(
    "StopTimecodeTypeDef",
    {"LastFrameClippingBehavior": LastFrameClippingBehavior, "Timecode": str},
    total=False,
)

TeletextSourceSettingsTypeDef = TypedDict(
    "TeletextSourceSettingsTypeDef",
    {"OutputRectangle": "CaptionRectangleTypeDef", "PageNumber": str},
    total=False,
)

TemporalFilterSettingsTypeDef = TypedDict(
    "TemporalFilterSettingsTypeDef",
    {
        "PostFilterSharpening": TemporalFilterPostFilterSharpening,
        "Strength": TemporalFilterStrength,
    },
    total=False,
)

_RequiredTimecodeConfigTypeDef = TypedDict(
    "_RequiredTimecodeConfigTypeDef", {"Source": TimecodeConfigSource}
)
_OptionalTimecodeConfigTypeDef = TypedDict(
    "_OptionalTimecodeConfigTypeDef", {"SyncThreshold": int}, total=False
)


class TimecodeConfigTypeDef(_RequiredTimecodeConfigTypeDef, _OptionalTimecodeConfigTypeDef):
    pass


TransferringInputDeviceSummaryTypeDef = TypedDict(
    "TransferringInputDeviceSummaryTypeDef",
    {"Id": str, "Message": str, "TargetCustomerId": str, "TransferType": InputDeviceTransferType},
    total=False,
)

TtmlDestinationSettingsTypeDef = TypedDict(
    "TtmlDestinationSettingsTypeDef", {"StyleControl": TtmlDestinationStyleControl}, total=False
)

UdpContainerSettingsTypeDef = TypedDict(
    "UdpContainerSettingsTypeDef", {"M2tsSettings": "M2tsSettingsTypeDef"}, total=False
)

UdpGroupSettingsTypeDef = TypedDict(
    "UdpGroupSettingsTypeDef",
    {
        "InputLossAction": InputLossActionForUdpOut,
        "TimedMetadataId3Frame": UdpTimedMetadataId3Frame,
        "TimedMetadataId3Period": int,
    },
    total=False,
)

_RequiredUdpOutputSettingsTypeDef = TypedDict(
    "_RequiredUdpOutputSettingsTypeDef",
    {"ContainerSettings": "UdpContainerSettingsTypeDef", "Destination": "OutputLocationRefTypeDef"},
)
_OptionalUdpOutputSettingsTypeDef = TypedDict(
    "_OptionalUdpOutputSettingsTypeDef",
    {"BufferMsec": int, "FecOutputSettings": "FecOutputSettingsTypeDef"},
    total=False,
)


class UdpOutputSettingsTypeDef(
    _RequiredUdpOutputSettingsTypeDef, _OptionalUdpOutputSettingsTypeDef
):
    pass


VideoBlackFailoverSettingsTypeDef = TypedDict(
    "VideoBlackFailoverSettingsTypeDef",
    {"BlackDetectThreshold": float, "VideoBlackThresholdMsec": int},
    total=False,
)

VideoCodecSettingsTypeDef = TypedDict(
    "VideoCodecSettingsTypeDef",
    {
        "FrameCaptureSettings": "FrameCaptureSettingsTypeDef",
        "H264Settings": "H264SettingsTypeDef",
        "H265Settings": "H265SettingsTypeDef",
        "Mpeg2Settings": "Mpeg2SettingsTypeDef",
    },
    total=False,
)

_RequiredVideoDescriptionTypeDef = TypedDict("_RequiredVideoDescriptionTypeDef", {"Name": str})
_OptionalVideoDescriptionTypeDef = TypedDict(
    "_OptionalVideoDescriptionTypeDef",
    {
        "CodecSettings": "VideoCodecSettingsTypeDef",
        "Height": int,
        "RespondToAfd": VideoDescriptionRespondToAfd,
        "ScalingBehavior": VideoDescriptionScalingBehavior,
        "Sharpness": int,
        "Width": int,
    },
    total=False,
)


class VideoDescriptionTypeDef(_RequiredVideoDescriptionTypeDef, _OptionalVideoDescriptionTypeDef):
    pass


VideoSelectorColorSpaceSettingsTypeDef = TypedDict(
    "VideoSelectorColorSpaceSettingsTypeDef", {"Hdr10Settings": "Hdr10SettingsTypeDef"}, total=False
)

VideoSelectorPidTypeDef = TypedDict("VideoSelectorPidTypeDef", {"Pid": int}, total=False)

VideoSelectorProgramIdTypeDef = TypedDict(
    "VideoSelectorProgramIdTypeDef", {"ProgramId": int}, total=False
)

VideoSelectorSettingsTypeDef = TypedDict(
    "VideoSelectorSettingsTypeDef",
    {
        "VideoSelectorPid": "VideoSelectorPidTypeDef",
        "VideoSelectorProgramId": "VideoSelectorProgramIdTypeDef",
    },
    total=False,
)

VideoSelectorTypeDef = TypedDict(
    "VideoSelectorTypeDef",
    {
        "ColorSpace": VideoSelectorColorSpace,
        "ColorSpaceSettings": "VideoSelectorColorSpaceSettingsTypeDef",
        "ColorSpaceUsage": VideoSelectorColorSpaceUsage,
        "SelectorSettings": "VideoSelectorSettingsTypeDef",
    },
    total=False,
)

VpcOutputSettingsDescriptionTypeDef = TypedDict(
    "VpcOutputSettingsDescriptionTypeDef",
    {
        "AvailabilityZones": List[str],
        "NetworkInterfaceIds": List[str],
        "SecurityGroupIds": List[str],
        "SubnetIds": List[str],
    },
    total=False,
)

WavSettingsTypeDef = TypedDict(
    "WavSettingsTypeDef",
    {"BitDepth": float, "CodingMode": WavCodingMode, "SampleRate": float},
    total=False,
)

BatchDeleteResponseTypeDef = TypedDict(
    "BatchDeleteResponseTypeDef",
    {
        "Failed": List["BatchFailedResultModelTypeDef"],
        "Successful": List["BatchSuccessfulResultModelTypeDef"],
    },
    total=False,
)

BatchScheduleActionCreateRequestTypeDef = TypedDict(
    "BatchScheduleActionCreateRequestTypeDef", {"ScheduleActions": List["ScheduleActionTypeDef"]}
)

BatchScheduleActionDeleteRequestTypeDef = TypedDict(
    "BatchScheduleActionDeleteRequestTypeDef", {"ActionNames": List[str]}
)

BatchStartResponseTypeDef = TypedDict(
    "BatchStartResponseTypeDef",
    {
        "Failed": List["BatchFailedResultModelTypeDef"],
        "Successful": List["BatchSuccessfulResultModelTypeDef"],
    },
    total=False,
)

BatchStopResponseTypeDef = TypedDict(
    "BatchStopResponseTypeDef",
    {
        "Failed": List["BatchFailedResultModelTypeDef"],
        "Successful": List["BatchSuccessfulResultModelTypeDef"],
    },
    total=False,
)

BatchUpdateScheduleResponseTypeDef = TypedDict(
    "BatchUpdateScheduleResponseTypeDef",
    {
        "Creates": "BatchScheduleActionCreateResultTypeDef",
        "Deletes": "BatchScheduleActionDeleteResultTypeDef",
    },
    total=False,
)

CreateChannelResponseTypeDef = TypedDict(
    "CreateChannelResponseTypeDef", {"Channel": "ChannelTypeDef"}, total=False
)

CreateInputResponseTypeDef = TypedDict(
    "CreateInputResponseTypeDef", {"Input": "InputTypeDef"}, total=False
)

CreateInputSecurityGroupResponseTypeDef = TypedDict(
    "CreateInputSecurityGroupResponseTypeDef",
    {"SecurityGroup": "InputSecurityGroupTypeDef"},
    total=False,
)

CreateMultiplexProgramResponseTypeDef = TypedDict(
    "CreateMultiplexProgramResponseTypeDef",
    {"MultiplexProgram": "MultiplexProgramTypeDef"},
    total=False,
)

CreateMultiplexResponseTypeDef = TypedDict(
    "CreateMultiplexResponseTypeDef", {"Multiplex": "MultiplexTypeDef"}, total=False
)

CreatePartnerInputResponseTypeDef = TypedDict(
    "CreatePartnerInputResponseTypeDef", {"Input": "InputTypeDef"}, total=False
)

DeleteChannelResponseTypeDef = TypedDict(
    "DeleteChannelResponseTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClass,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevel,
        "Name": str,
        "PipelineDetails": List["PipelineDetailTypeDef"],
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelState,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
    },
    total=False,
)

DeleteMultiplexProgramResponseTypeDef = TypedDict(
    "DeleteMultiplexProgramResponseTypeDef",
    {
        "ChannelId": str,
        "MultiplexProgramSettings": "MultiplexProgramSettingsTypeDef",
        "PacketIdentifiersMap": "MultiplexProgramPacketIdentifiersMapTypeDef",
        "PipelineDetails": List["MultiplexProgramPipelineDetailTypeDef"],
        "ProgramName": str,
    },
    total=False,
)

DeleteMultiplexResponseTypeDef = TypedDict(
    "DeleteMultiplexResponseTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Destinations": List["MultiplexOutputDestinationTypeDef"],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexState,
        "Tags": Dict[str, str],
    },
    total=False,
)

DeleteReservationResponseTypeDef = TypedDict(
    "DeleteReservationResponseTypeDef",
    {
        "Arn": str,
        "Count": int,
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": OfferingDurationUnits,
        "End": str,
        "FixedPrice": float,
        "Name": str,
        "OfferingDescription": str,
        "OfferingId": str,
        "OfferingType": OfferingType,
        "Region": str,
        "ReservationId": str,
        "ResourceSpecification": "ReservationResourceSpecificationTypeDef",
        "Start": str,
        "State": ReservationState,
        "Tags": Dict[str, str],
        "UsagePrice": float,
    },
    total=False,
)

DescribeChannelResponseTypeDef = TypedDict(
    "DescribeChannelResponseTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClass,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevel,
        "Name": str,
        "PipelineDetails": List["PipelineDetailTypeDef"],
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelState,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
    },
    total=False,
)

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
        "Type": InputDeviceType,
        "UhdDeviceSettings": "InputDeviceUhdSettingsTypeDef",
    },
    total=False,
)

DescribeInputDeviceThumbnailResponseTypeDef = TypedDict(
    "DescribeInputDeviceThumbnailResponseTypeDef",
    {
        "Body": StreamingBody,
        "ContentType": ContentType,
        "ContentLength": int,
        "ETag": str,
        "LastModified": datetime,
    },
    total=False,
)

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

DescribeInputSecurityGroupResponseTypeDef = TypedDict(
    "DescribeInputSecurityGroupResponseTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Inputs": List[str],
        "State": InputSecurityGroupState,
        "Tags": Dict[str, str],
        "WhitelistRules": List["InputWhitelistRuleTypeDef"],
    },
    total=False,
)

DescribeMultiplexProgramResponseTypeDef = TypedDict(
    "DescribeMultiplexProgramResponseTypeDef",
    {
        "ChannelId": str,
        "MultiplexProgramSettings": "MultiplexProgramSettingsTypeDef",
        "PacketIdentifiersMap": "MultiplexProgramPacketIdentifiersMapTypeDef",
        "PipelineDetails": List["MultiplexProgramPipelineDetailTypeDef"],
        "ProgramName": str,
    },
    total=False,
)

DescribeMultiplexResponseTypeDef = TypedDict(
    "DescribeMultiplexResponseTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Destinations": List["MultiplexOutputDestinationTypeDef"],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexState,
        "Tags": Dict[str, str],
    },
    total=False,
)

DescribeOfferingResponseTypeDef = TypedDict(
    "DescribeOfferingResponseTypeDef",
    {
        "Arn": str,
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": OfferingDurationUnits,
        "FixedPrice": float,
        "OfferingDescription": str,
        "OfferingId": str,
        "OfferingType": OfferingType,
        "Region": str,
        "ResourceSpecification": "ReservationResourceSpecificationTypeDef",
        "UsagePrice": float,
    },
    total=False,
)

DescribeReservationResponseTypeDef = TypedDict(
    "DescribeReservationResponseTypeDef",
    {
        "Arn": str,
        "Count": int,
        "CurrencyCode": str,
        "Duration": int,
        "DurationUnits": OfferingDurationUnits,
        "End": str,
        "FixedPrice": float,
        "Name": str,
        "OfferingDescription": str,
        "OfferingId": str,
        "OfferingType": OfferingType,
        "Region": str,
        "ReservationId": str,
        "ResourceSpecification": "ReservationResourceSpecificationTypeDef",
        "Start": str,
        "State": ReservationState,
        "Tags": Dict[str, str],
        "UsagePrice": float,
    },
    total=False,
)

DescribeScheduleResponseTypeDef = TypedDict(
    "DescribeScheduleResponseTypeDef",
    {"NextToken": str, "ScheduleActions": List["ScheduleActionTypeDef"]},
    total=False,
)

InputDestinationRequestTypeDef = TypedDict(
    "InputDestinationRequestTypeDef", {"StreamName": str}, total=False
)

InputDeviceConfigurableSettingsTypeDef = TypedDict(
    "InputDeviceConfigurableSettingsTypeDef",
    {"ConfiguredInput": InputDeviceConfiguredInput, "MaxBitrate": int},
    total=False,
)

InputDeviceRequestTypeDef = TypedDict("InputDeviceRequestTypeDef", {"Id": str}, total=False)

InputSourceRequestTypeDef = TypedDict(
    "InputSourceRequestTypeDef", {"PasswordParam": str, "Url": str, "Username": str}, total=False
)

_RequiredInputVpcRequestTypeDef = TypedDict(
    "_RequiredInputVpcRequestTypeDef", {"SubnetIds": List[str]}
)
_OptionalInputVpcRequestTypeDef = TypedDict(
    "_OptionalInputVpcRequestTypeDef", {"SecurityGroupIds": List[str]}, total=False
)


class InputVpcRequestTypeDef(_RequiredInputVpcRequestTypeDef, _OptionalInputVpcRequestTypeDef):
    pass


InputWhitelistRuleCidrTypeDef = TypedDict(
    "InputWhitelistRuleCidrTypeDef", {"Cidr": str}, total=False
)

ListChannelsResponseTypeDef = TypedDict(
    "ListChannelsResponseTypeDef",
    {"Channels": List["ChannelSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListInputDeviceTransfersResponseTypeDef = TypedDict(
    "ListInputDeviceTransfersResponseTypeDef",
    {"InputDeviceTransfers": List["TransferringInputDeviceSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListInputDevicesResponseTypeDef = TypedDict(
    "ListInputDevicesResponseTypeDef",
    {"InputDevices": List["InputDeviceSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListInputSecurityGroupsResponseTypeDef = TypedDict(
    "ListInputSecurityGroupsResponseTypeDef",
    {"InputSecurityGroups": List["InputSecurityGroupTypeDef"], "NextToken": str},
    total=False,
)

ListInputsResponseTypeDef = TypedDict(
    "ListInputsResponseTypeDef", {"Inputs": List["InputTypeDef"], "NextToken": str}, total=False
)

ListMultiplexProgramsResponseTypeDef = TypedDict(
    "ListMultiplexProgramsResponseTypeDef",
    {"MultiplexPrograms": List["MultiplexProgramSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListMultiplexesResponseTypeDef = TypedDict(
    "ListMultiplexesResponseTypeDef",
    {"Multiplexes": List["MultiplexSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListOfferingsResponseTypeDef = TypedDict(
    "ListOfferingsResponseTypeDef",
    {"NextToken": str, "Offerings": List["OfferingTypeDef"]},
    total=False,
)

ListReservationsResponseTypeDef = TypedDict(
    "ListReservationsResponseTypeDef",
    {"NextToken": str, "Reservations": List["ReservationTypeDef"]},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

MediaConnectFlowRequestTypeDef = TypedDict(
    "MediaConnectFlowRequestTypeDef", {"FlowArn": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PurchaseOfferingResponseTypeDef = TypedDict(
    "PurchaseOfferingResponseTypeDef", {"Reservation": "ReservationTypeDef"}, total=False
)

StartChannelResponseTypeDef = TypedDict(
    "StartChannelResponseTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClass,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevel,
        "Name": str,
        "PipelineDetails": List["PipelineDetailTypeDef"],
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelState,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
    },
    total=False,
)

StartMultiplexResponseTypeDef = TypedDict(
    "StartMultiplexResponseTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Destinations": List["MultiplexOutputDestinationTypeDef"],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexState,
        "Tags": Dict[str, str],
    },
    total=False,
)

StopChannelResponseTypeDef = TypedDict(
    "StopChannelResponseTypeDef",
    {
        "Arn": str,
        "CdiInputSpecification": "CdiInputSpecificationTypeDef",
        "ChannelClass": ChannelClass,
        "Destinations": List["OutputDestinationTypeDef"],
        "EgressEndpoints": List["ChannelEgressEndpointTypeDef"],
        "EncoderSettings": "EncoderSettingsTypeDef",
        "Id": str,
        "InputAttachments": List["InputAttachmentTypeDef"],
        "InputSpecification": "InputSpecificationTypeDef",
        "LogLevel": LogLevel,
        "Name": str,
        "PipelineDetails": List["PipelineDetailTypeDef"],
        "PipelinesRunningCount": int,
        "RoleArn": str,
        "State": ChannelState,
        "Tags": Dict[str, str],
        "Vpc": "VpcOutputSettingsDescriptionTypeDef",
    },
    total=False,
)

StopMultiplexResponseTypeDef = TypedDict(
    "StopMultiplexResponseTypeDef",
    {
        "Arn": str,
        "AvailabilityZones": List[str],
        "Destinations": List["MultiplexOutputDestinationTypeDef"],
        "Id": str,
        "MultiplexSettings": "MultiplexSettingsTypeDef",
        "Name": str,
        "PipelinesRunningCount": int,
        "ProgramCount": int,
        "State": MultiplexState,
        "Tags": Dict[str, str],
    },
    total=False,
)

UpdateChannelClassResponseTypeDef = TypedDict(
    "UpdateChannelClassResponseTypeDef", {"Channel": "ChannelTypeDef"}, total=False
)

UpdateChannelResponseTypeDef = TypedDict(
    "UpdateChannelResponseTypeDef", {"Channel": "ChannelTypeDef"}, total=False
)

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
        "Type": InputDeviceType,
        "UhdDeviceSettings": "InputDeviceUhdSettingsTypeDef",
    },
    total=False,
)

UpdateInputResponseTypeDef = TypedDict(
    "UpdateInputResponseTypeDef", {"Input": "InputTypeDef"}, total=False
)

UpdateInputSecurityGroupResponseTypeDef = TypedDict(
    "UpdateInputSecurityGroupResponseTypeDef",
    {"SecurityGroup": "InputSecurityGroupTypeDef"},
    total=False,
)

UpdateMultiplexProgramResponseTypeDef = TypedDict(
    "UpdateMultiplexProgramResponseTypeDef",
    {"MultiplexProgram": "MultiplexProgramTypeDef"},
    total=False,
)

UpdateMultiplexResponseTypeDef = TypedDict(
    "UpdateMultiplexResponseTypeDef", {"Multiplex": "MultiplexTypeDef"}, total=False
)

UpdateReservationResponseTypeDef = TypedDict(
    "UpdateReservationResponseTypeDef", {"Reservation": "ReservationTypeDef"}, total=False
)

_RequiredVpcOutputSettingsTypeDef = TypedDict(
    "_RequiredVpcOutputSettingsTypeDef", {"SubnetIds": List[str]}
)
_OptionalVpcOutputSettingsTypeDef = TypedDict(
    "_OptionalVpcOutputSettingsTypeDef",
    {"PublicAddressAllocationIds": List[str], "SecurityGroupIds": List[str]},
    total=False,
)


class VpcOutputSettingsTypeDef(
    _RequiredVpcOutputSettingsTypeDef, _OptionalVpcOutputSettingsTypeDef
):
    pass


WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef", {"Delay": int, "MaxAttempts": int}, total=False
)
