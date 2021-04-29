"""
Main interface for mediaconvert service type definitions.

Usage::

    ```python
    from mypy_boto3_mediaconvert.type_defs import AacSettingsTypeDef

    data: AacSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_mediaconvert.literals import (
    AacAudioDescriptionBroadcasterMix,
    AacCodecProfile,
    AacCodingMode,
    AacRateControlMode,
    AacRawFormat,
    AacSpecification,
    AacVbrQuality,
    Ac3BitstreamMode,
    Ac3CodingMode,
    Ac3DynamicRangeCompressionLine,
    Ac3DynamicRangeCompressionProfile,
    Ac3DynamicRangeCompressionRf,
    Ac3LfeFilter,
    Ac3MetadataControl,
    AccelerationMode,
    AccelerationStatus,
    AfdSignaling,
    AlphaBehavior,
    AncillaryConvert608To708,
    AncillaryTerminateCaptions,
    AntiAlias,
    AudioChannelTag,
    AudioCodec,
    AudioDefaultSelection,
    AudioLanguageCodeControl,
    AudioNormalizationAlgorithm,
    AudioNormalizationAlgorithmControl,
    AudioNormalizationLoudnessLogging,
    AudioNormalizationPeakCalculation,
    AudioSelectorType,
    AudioTypeControl,
    Av1AdaptiveQuantization,
    Av1FramerateControl,
    Av1FramerateConversionAlgorithm,
    Av1RateControlMode,
    Av1SpatialAdaptiveQuantization,
    AvcIntraClass,
    AvcIntraFramerateControl,
    AvcIntraFramerateConversionAlgorithm,
    AvcIntraInterlaceMode,
    AvcIntraScanTypeConversionMode,
    AvcIntraSlowPal,
    AvcIntraTelecine,
    AvcIntraUhdQualityTuningLevel,
    BillingTagsSource,
    BurninSubtitleAlignment,
    BurninSubtitleBackgroundColor,
    BurninSubtitleFontColor,
    BurninSubtitleOutlineColor,
    BurninSubtitleShadowColor,
    BurninSubtitleTeletextSpacing,
    CaptionDestinationType,
    CaptionSourceType,
    CmafClientCache,
    CmafCodecSpecification,
    CmafEncryptionType,
    CmafInitializationVectorInManifest,
    CmafKeyProviderType,
    CmafManifestCompression,
    CmafManifestDurationFormat,
    CmafMpdProfile,
    CmafPtsOffsetHandlingForBFrames,
    CmafSegmentControl,
    CmafStreamInfResolution,
    CmafWriteDASHManifest,
    CmafWriteHLSManifest,
    CmafWriteSegmentTimelineInRepresentation,
    CmfcAudioDuration,
    CmfcAudioTrackType,
    CmfcDescriptiveVideoServiceFlag,
    CmfcIFrameOnlyManifest,
    CmfcScte35Esam,
    CmfcScte35Source,
    ColorMetadata,
    ColorSpace,
    ColorSpaceConversion,
    ColorSpaceUsage,
    Commitment,
    ContainerType,
    DashIsoGroupAudioChannelConfigSchemeIdUri,
    DashIsoHbbtvCompliance,
    DashIsoMpdProfile,
    DashIsoPlaybackDeviceCompatibility,
    DashIsoPtsOffsetHandlingForBFrames,
    DashIsoSegmentControl,
    DashIsoWriteSegmentTimelineInRepresentation,
    DecryptionMode,
    DeinterlaceAlgorithm,
    DeinterlacerControl,
    DeinterlacerMode,
    DolbyVisionLevel6Mode,
    DolbyVisionProfile,
    DropFrameTimecode,
    DvbSubtitleAlignment,
    DvbSubtitleBackgroundColor,
    DvbSubtitleFontColor,
    DvbSubtitleOutlineColor,
    DvbSubtitleShadowColor,
    DvbSubtitleTeletextSpacing,
    DvbSubtitlingType,
    Eac3AtmosBitstreamMode,
    Eac3AtmosCodingMode,
    Eac3AtmosDialogueIntelligence,
    Eac3AtmosDynamicRangeCompressionLine,
    Eac3AtmosDynamicRangeCompressionRf,
    Eac3AtmosMeteringMode,
    Eac3AtmosStereoDownmix,
    Eac3AtmosSurroundExMode,
    Eac3AttenuationControl,
    Eac3BitstreamMode,
    Eac3CodingMode,
    Eac3DcFilter,
    Eac3DynamicRangeCompressionLine,
    Eac3DynamicRangeCompressionRf,
    Eac3LfeControl,
    Eac3LfeFilter,
    Eac3MetadataControl,
    Eac3PassthroughControl,
    Eac3PhaseControl,
    Eac3StereoDownmix,
    Eac3SurroundExMode,
    Eac3SurroundMode,
    EmbeddedConvert608To708,
    EmbeddedTerminateCaptions,
    F4vMoovPlacement,
    FileSourceConvert608To708,
    FontScript,
    H264AdaptiveQuantization,
    H264CodecLevel,
    H264CodecProfile,
    H264DynamicSubGop,
    H264EntropyEncoding,
    H264FieldEncoding,
    H264FlickerAdaptiveQuantization,
    H264FramerateControl,
    H264FramerateConversionAlgorithm,
    H264GopBReference,
    H264GopSizeUnits,
    H264InterlaceMode,
    H264ParControl,
    H264QualityTuningLevel,
    H264RateControlMode,
    H264RepeatPps,
    H264ScanTypeConversionMode,
    H264SceneChangeDetect,
    H264SlowPal,
    H264SpatialAdaptiveQuantization,
    H264Syntax,
    H264Telecine,
    H264TemporalAdaptiveQuantization,
    H264UnregisteredSeiTimecode,
    H265AdaptiveQuantization,
    H265AlternateTransferFunctionSei,
    H265CodecLevel,
    H265CodecProfile,
    H265DynamicSubGop,
    H265FlickerAdaptiveQuantization,
    H265FramerateControl,
    H265FramerateConversionAlgorithm,
    H265GopBReference,
    H265GopSizeUnits,
    H265InterlaceMode,
    H265ParControl,
    H265QualityTuningLevel,
    H265RateControlMode,
    H265SampleAdaptiveOffsetFilterMode,
    H265ScanTypeConversionMode,
    H265SceneChangeDetect,
    H265SlowPal,
    H265SpatialAdaptiveQuantization,
    H265Telecine,
    H265TemporalAdaptiveQuantization,
    H265TemporalIds,
    H265Tiles,
    H265UnregisteredSeiTimecode,
    H265WriteMp4PackagingType,
    HlsAdMarkers,
    HlsAudioOnlyContainer,
    HlsAudioOnlyHeader,
    HlsAudioTrackType,
    HlsCaptionLanguageSetting,
    HlsClientCache,
    HlsCodecSpecification,
    HlsDescriptiveVideoServiceFlag,
    HlsDirectoryStructure,
    HlsEncryptionType,
    HlsIFrameOnlyManifest,
    HlsInitializationVectorInManifest,
    HlsKeyProviderType,
    HlsManifestCompression,
    HlsManifestDurationFormat,
    HlsOfflineEncrypted,
    HlsOutputSelection,
    HlsProgramDateTime,
    HlsSegmentControl,
    HlsStreamInfResolution,
    HlsTimedMetadataId3Frame,
    ImscStylePassthrough,
    InputDeblockFilter,
    InputDenoiseFilter,
    InputFilterEnable,
    InputPsiControl,
    InputRotate,
    InputScanType,
    InputTimecodeSource,
    JobPhase,
    JobStatus,
    LanguageCode,
    M2tsAudioBufferModel,
    M2tsAudioDuration,
    M2tsBufferModel,
    M2tsEbpAudioInterval,
    M2tsEbpPlacement,
    M2tsEsRateInPes,
    M2tsForceTsVideoEbpOrder,
    M2tsNielsenId3,
    M2tsPcrControl,
    M2tsRateMode,
    M2tsScte35Source,
    M2tsSegmentationMarkers,
    M2tsSegmentationStyle,
    M3u8AudioDuration,
    M3u8NielsenId3,
    M3u8PcrControl,
    M3u8Scte35Source,
    MotionImageInsertionMode,
    MotionImagePlayback,
    MovClapAtom,
    MovCslgAtom,
    MovMpeg2FourCCControl,
    MovPaddingControl,
    MovReference,
    Mp3RateControlMode,
    Mp4CslgAtom,
    Mp4FreeSpaceBox,
    Mp4MoovPlacement,
    MpdAccessibilityCaptionHints,
    MpdAudioDuration,
    MpdCaptionContainerType,
    MpdScte35Esam,
    MpdScte35Source,
    Mpeg2AdaptiveQuantization,
    Mpeg2CodecLevel,
    Mpeg2CodecProfile,
    Mpeg2DynamicSubGop,
    Mpeg2FramerateControl,
    Mpeg2FramerateConversionAlgorithm,
    Mpeg2GopSizeUnits,
    Mpeg2InterlaceMode,
    Mpeg2IntraDcPrecision,
    Mpeg2ParControl,
    Mpeg2QualityTuningLevel,
    Mpeg2RateControlMode,
    Mpeg2ScanTypeConversionMode,
    Mpeg2SceneChangeDetect,
    Mpeg2SlowPal,
    Mpeg2SpatialAdaptiveQuantization,
    Mpeg2Syntax,
    Mpeg2Telecine,
    Mpeg2TemporalAdaptiveQuantization,
    MsSmoothAudioDeduplication,
    MsSmoothManifestEncoding,
    MxfAfdSignaling,
    MxfProfile,
    NielsenActiveWatermarkProcessType,
    NielsenSourceWatermarkStatusType,
    NielsenUniqueTicPerAudioTrackType,
    NoiseFilterPostTemporalSharpening,
    NoiseReducerFilter,
    OutputGroupType,
    OutputSdt,
    PricingPlan,
    ProresCodecProfile,
    ProresFramerateControl,
    ProresFramerateConversionAlgorithm,
    ProresInterlaceMode,
    ProresParControl,
    ProresScanTypeConversionMode,
    ProresSlowPal,
    ProresTelecine,
    QueueStatus,
    RenewalType,
    ReservationPlanStatus,
    RespondToAfd,
    S3ObjectCannedAcl,
    S3ServerSideEncryptionType,
    ScalingBehavior,
    SccDestinationFramerate,
    SimulateReservedQueue,
    StatusUpdateInterval,
    TeletextPageType,
    TimecodeBurninPosition,
    TimecodeSource,
    TimedMetadata,
    TtmlStylePassthrough,
    TypeType,
    Vc3Class,
    Vc3FramerateControl,
    Vc3FramerateConversionAlgorithm,
    Vc3InterlaceMode,
    Vc3ScanTypeConversionMode,
    Vc3SlowPal,
    Vc3Telecine,
    VideoCodec,
    VideoTimecodeInsertion,
    Vp8FramerateControl,
    Vp8FramerateConversionAlgorithm,
    Vp8ParControl,
    Vp8QualityTuningLevel,
    Vp8RateControlMode,
    Vp9FramerateControl,
    Vp9FramerateConversionAlgorithm,
    Vp9ParControl,
    Vp9QualityTuningLevel,
    Vp9RateControlMode,
    WatermarkingStrength,
    WavFormat,
    WebvttStylePassthrough,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AacSettingsTypeDef",
    "Ac3SettingsTypeDef",
    "AccelerationSettingsTypeDef",
    "AiffSettingsTypeDef",
    "AncillarySourceSettingsTypeDef",
    "AudioChannelTaggingSettingsTypeDef",
    "AudioCodecSettingsTypeDef",
    "AudioDescriptionTypeDef",
    "AudioNormalizationSettingsTypeDef",
    "AudioSelectorGroupTypeDef",
    "AudioSelectorTypeDef",
    "AutomatedAbrSettingsTypeDef",
    "AutomatedEncodingSettingsTypeDef",
    "Av1QvbrSettingsTypeDef",
    "Av1SettingsTypeDef",
    "AvailBlankingTypeDef",
    "AvcIntraSettingsTypeDef",
    "AvcIntraUhdSettingsTypeDef",
    "BurninDestinationSettingsTypeDef",
    "CaptionDescriptionPresetTypeDef",
    "CaptionDescriptionTypeDef",
    "CaptionDestinationSettingsTypeDef",
    "CaptionSelectorTypeDef",
    "CaptionSourceFramerateTypeDef",
    "CaptionSourceSettingsTypeDef",
    "ChannelMappingTypeDef",
    "CmafAdditionalManifestTypeDef",
    "CmafEncryptionSettingsTypeDef",
    "CmafGroupSettingsTypeDef",
    "CmfcSettingsTypeDef",
    "ColorCorrectorTypeDef",
    "ContainerSettingsTypeDef",
    "DashAdditionalManifestTypeDef",
    "DashIsoEncryptionSettingsTypeDef",
    "DashIsoGroupSettingsTypeDef",
    "DeinterlacerTypeDef",
    "DestinationSettingsTypeDef",
    "DolbyVisionLevel6MetadataTypeDef",
    "DolbyVisionTypeDef",
    "DvbNitSettingsTypeDef",
    "DvbSdtSettingsTypeDef",
    "DvbSubDestinationSettingsTypeDef",
    "DvbSubSourceSettingsTypeDef",
    "DvbTdtSettingsTypeDef",
    "Eac3AtmosSettingsTypeDef",
    "Eac3SettingsTypeDef",
    "EmbeddedDestinationSettingsTypeDef",
    "EmbeddedSourceSettingsTypeDef",
    "EndpointTypeDef",
    "EsamManifestConfirmConditionNotificationTypeDef",
    "EsamSettingsTypeDef",
    "EsamSignalProcessingNotificationTypeDef",
    "F4vSettingsTypeDef",
    "FileGroupSettingsTypeDef",
    "FileSourceSettingsTypeDef",
    "FrameCaptureSettingsTypeDef",
    "H264QvbrSettingsTypeDef",
    "H264SettingsTypeDef",
    "H265QvbrSettingsTypeDef",
    "H265SettingsTypeDef",
    "Hdr10MetadataTypeDef",
    "HlsAdditionalManifestTypeDef",
    "HlsCaptionLanguageMappingTypeDef",
    "HlsEncryptionSettingsTypeDef",
    "HlsGroupSettingsTypeDef",
    "HlsSettingsTypeDef",
    "HopDestinationTypeDef",
    "Id3InsertionTypeDef",
    "ImageInserterTypeDef",
    "ImscDestinationSettingsTypeDef",
    "InputClippingTypeDef",
    "InputDecryptionSettingsTypeDef",
    "InputTemplateTypeDef",
    "InputTypeDef",
    "InsertableImageTypeDef",
    "JobMessagesTypeDef",
    "JobSettingsTypeDef",
    "JobTemplateSettingsTypeDef",
    "JobTemplateTypeDef",
    "JobTypeDef",
    "M2tsScte35EsamTypeDef",
    "M2tsSettingsTypeDef",
    "M3u8SettingsTypeDef",
    "MotionImageInserterTypeDef",
    "MotionImageInsertionFramerateTypeDef",
    "MotionImageInsertionOffsetTypeDef",
    "MovSettingsTypeDef",
    "Mp2SettingsTypeDef",
    "Mp3SettingsTypeDef",
    "Mp4SettingsTypeDef",
    "MpdSettingsTypeDef",
    "Mpeg2SettingsTypeDef",
    "MsSmoothAdditionalManifestTypeDef",
    "MsSmoothEncryptionSettingsTypeDef",
    "MsSmoothGroupSettingsTypeDef",
    "MxfSettingsTypeDef",
    "NexGuardFileMarkerSettingsTypeDef",
    "NielsenConfigurationTypeDef",
    "NielsenNonLinearWatermarkSettingsTypeDef",
    "NoiseReducerFilterSettingsTypeDef",
    "NoiseReducerSpatialFilterSettingsTypeDef",
    "NoiseReducerTemporalFilterSettingsTypeDef",
    "NoiseReducerTypeDef",
    "OpusSettingsTypeDef",
    "OutputChannelMappingTypeDef",
    "OutputDetailTypeDef",
    "OutputGroupDetailTypeDef",
    "OutputGroupSettingsTypeDef",
    "OutputGroupTypeDef",
    "OutputSettingsTypeDef",
    "OutputTypeDef",
    "PartnerWatermarkingTypeDef",
    "PresetSettingsTypeDef",
    "PresetTypeDef",
    "ProresSettingsTypeDef",
    "QueueTransitionTypeDef",
    "QueueTypeDef",
    "RectangleTypeDef",
    "RemixSettingsTypeDef",
    "ReservationPlanTypeDef",
    "ResourceTagsTypeDef",
    "ResponseMetadata",
    "S3DestinationAccessControlTypeDef",
    "S3DestinationSettingsTypeDef",
    "S3EncryptionSettingsTypeDef",
    "SccDestinationSettingsTypeDef",
    "SpekeKeyProviderCmafTypeDef",
    "SpekeKeyProviderTypeDef",
    "StaticKeyProviderTypeDef",
    "TeletextDestinationSettingsTypeDef",
    "TeletextSourceSettingsTypeDef",
    "TimecodeBurninTypeDef",
    "TimecodeConfigTypeDef",
    "TimedMetadataInsertionTypeDef",
    "TimingTypeDef",
    "TrackSourceSettingsTypeDef",
    "TtmlDestinationSettingsTypeDef",
    "Vc3SettingsTypeDef",
    "VideoCodecSettingsTypeDef",
    "VideoDescriptionTypeDef",
    "VideoDetailTypeDef",
    "VideoPreprocessorTypeDef",
    "VideoSelectorTypeDef",
    "VorbisSettingsTypeDef",
    "Vp8SettingsTypeDef",
    "Vp9SettingsTypeDef",
    "WavSettingsTypeDef",
    "WebvttDestinationSettingsTypeDef",
    "CreateJobResponseTypeDef",
    "CreateJobTemplateResponseTypeDef",
    "CreatePresetResponseTypeDef",
    "CreateQueueResponseTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "GetJobResponseTypeDef",
    "GetJobTemplateResponseTypeDef",
    "GetPresetResponseTypeDef",
    "GetQueueResponseTypeDef",
    "ListJobTemplatesResponseTypeDef",
    "ListJobsResponseTypeDef",
    "ListPresetsResponseTypeDef",
    "ListQueuesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ReservationPlanSettingsTypeDef",
    "UpdateJobTemplateResponseTypeDef",
    "UpdatePresetResponseTypeDef",
    "UpdateQueueResponseTypeDef",
)

AacSettingsTypeDef = TypedDict(
    "AacSettingsTypeDef",
    {
        "AudioDescriptionBroadcasterMix": AacAudioDescriptionBroadcasterMix,
        "Bitrate": int,
        "CodecProfile": AacCodecProfile,
        "CodingMode": AacCodingMode,
        "RateControlMode": AacRateControlMode,
        "RawFormat": AacRawFormat,
        "SampleRate": int,
        "Specification": AacSpecification,
        "VbrQuality": AacVbrQuality,
    },
    total=False,
)

Ac3SettingsTypeDef = TypedDict(
    "Ac3SettingsTypeDef",
    {
        "Bitrate": int,
        "BitstreamMode": Ac3BitstreamMode,
        "CodingMode": Ac3CodingMode,
        "Dialnorm": int,
        "DynamicRangeCompressionLine": Ac3DynamicRangeCompressionLine,
        "DynamicRangeCompressionProfile": Ac3DynamicRangeCompressionProfile,
        "DynamicRangeCompressionRf": Ac3DynamicRangeCompressionRf,
        "LfeFilter": Ac3LfeFilter,
        "MetadataControl": Ac3MetadataControl,
        "SampleRate": int,
    },
    total=False,
)

AccelerationSettingsTypeDef = TypedDict("AccelerationSettingsTypeDef", {"Mode": AccelerationMode})

AiffSettingsTypeDef = TypedDict(
    "AiffSettingsTypeDef", {"BitDepth": int, "Channels": int, "SampleRate": int}, total=False
)

AncillarySourceSettingsTypeDef = TypedDict(
    "AncillarySourceSettingsTypeDef",
    {
        "Convert608To708": AncillaryConvert608To708,
        "SourceAncillaryChannelNumber": int,
        "TerminateCaptions": AncillaryTerminateCaptions,
    },
    total=False,
)

AudioChannelTaggingSettingsTypeDef = TypedDict(
    "AudioChannelTaggingSettingsTypeDef", {"ChannelTag": AudioChannelTag}, total=False
)

AudioCodecSettingsTypeDef = TypedDict(
    "AudioCodecSettingsTypeDef",
    {
        "AacSettings": "AacSettingsTypeDef",
        "Ac3Settings": "Ac3SettingsTypeDef",
        "AiffSettings": "AiffSettingsTypeDef",
        "Codec": AudioCodec,
        "Eac3AtmosSettings": "Eac3AtmosSettingsTypeDef",
        "Eac3Settings": "Eac3SettingsTypeDef",
        "Mp2Settings": "Mp2SettingsTypeDef",
        "Mp3Settings": "Mp3SettingsTypeDef",
        "OpusSettings": "OpusSettingsTypeDef",
        "VorbisSettings": "VorbisSettingsTypeDef",
        "WavSettings": "WavSettingsTypeDef",
    },
    total=False,
)

AudioDescriptionTypeDef = TypedDict(
    "AudioDescriptionTypeDef",
    {
        "AudioChannelTaggingSettings": "AudioChannelTaggingSettingsTypeDef",
        "AudioNormalizationSettings": "AudioNormalizationSettingsTypeDef",
        "AudioSourceName": str,
        "AudioType": int,
        "AudioTypeControl": AudioTypeControl,
        "CodecSettings": "AudioCodecSettingsTypeDef",
        "CustomLanguageCode": str,
        "LanguageCode": LanguageCode,
        "LanguageCodeControl": AudioLanguageCodeControl,
        "RemixSettings": "RemixSettingsTypeDef",
        "StreamName": str,
    },
    total=False,
)

AudioNormalizationSettingsTypeDef = TypedDict(
    "AudioNormalizationSettingsTypeDef",
    {
        "Algorithm": AudioNormalizationAlgorithm,
        "AlgorithmControl": AudioNormalizationAlgorithmControl,
        "CorrectionGateLevel": int,
        "LoudnessLogging": AudioNormalizationLoudnessLogging,
        "PeakCalculation": AudioNormalizationPeakCalculation,
        "TargetLkfs": float,
    },
    total=False,
)

AudioSelectorGroupTypeDef = TypedDict(
    "AudioSelectorGroupTypeDef", {"AudioSelectorNames": List[str]}, total=False
)

AudioSelectorTypeDef = TypedDict(
    "AudioSelectorTypeDef",
    {
        "CustomLanguageCode": str,
        "DefaultSelection": AudioDefaultSelection,
        "ExternalAudioFileInput": str,
        "LanguageCode": LanguageCode,
        "Offset": int,
        "Pids": List[int],
        "ProgramSelection": int,
        "RemixSettings": "RemixSettingsTypeDef",
        "SelectorType": AudioSelectorType,
        "Tracks": List[int],
    },
    total=False,
)

AutomatedAbrSettingsTypeDef = TypedDict(
    "AutomatedAbrSettingsTypeDef",
    {"MaxAbrBitrate": int, "MaxRenditions": int, "MinAbrBitrate": int},
    total=False,
)

AutomatedEncodingSettingsTypeDef = TypedDict(
    "AutomatedEncodingSettingsTypeDef", {"AbrSettings": "AutomatedAbrSettingsTypeDef"}, total=False
)

Av1QvbrSettingsTypeDef = TypedDict(
    "Av1QvbrSettingsTypeDef",
    {"QvbrQualityLevel": int, "QvbrQualityLevelFineTune": float},
    total=False,
)

Av1SettingsTypeDef = TypedDict(
    "Av1SettingsTypeDef",
    {
        "AdaptiveQuantization": Av1AdaptiveQuantization,
        "FramerateControl": Av1FramerateControl,
        "FramerateConversionAlgorithm": Av1FramerateConversionAlgorithm,
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "GopSize": float,
        "MaxBitrate": int,
        "NumberBFramesBetweenReferenceFrames": int,
        "QvbrSettings": "Av1QvbrSettingsTypeDef",
        "RateControlMode": Av1RateControlMode,
        "Slices": int,
        "SpatialAdaptiveQuantization": Av1SpatialAdaptiveQuantization,
    },
    total=False,
)

AvailBlankingTypeDef = TypedDict("AvailBlankingTypeDef", {"AvailBlankingImage": str}, total=False)

AvcIntraSettingsTypeDef = TypedDict(
    "AvcIntraSettingsTypeDef",
    {
        "AvcIntraClass": AvcIntraClass,
        "AvcIntraUhdSettings": "AvcIntraUhdSettingsTypeDef",
        "FramerateControl": AvcIntraFramerateControl,
        "FramerateConversionAlgorithm": AvcIntraFramerateConversionAlgorithm,
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "InterlaceMode": AvcIntraInterlaceMode,
        "ScanTypeConversionMode": AvcIntraScanTypeConversionMode,
        "SlowPal": AvcIntraSlowPal,
        "Telecine": AvcIntraTelecine,
    },
    total=False,
)

AvcIntraUhdSettingsTypeDef = TypedDict(
    "AvcIntraUhdSettingsTypeDef", {"QualityTuningLevel": AvcIntraUhdQualityTuningLevel}, total=False
)

BurninDestinationSettingsTypeDef = TypedDict(
    "BurninDestinationSettingsTypeDef",
    {
        "Alignment": BurninSubtitleAlignment,
        "BackgroundColor": BurninSubtitleBackgroundColor,
        "BackgroundOpacity": int,
        "FontColor": BurninSubtitleFontColor,
        "FontOpacity": int,
        "FontResolution": int,
        "FontScript": FontScript,
        "FontSize": int,
        "OutlineColor": BurninSubtitleOutlineColor,
        "OutlineSize": int,
        "ShadowColor": BurninSubtitleShadowColor,
        "ShadowOpacity": int,
        "ShadowXOffset": int,
        "ShadowYOffset": int,
        "TeletextSpacing": BurninSubtitleTeletextSpacing,
        "XPosition": int,
        "YPosition": int,
    },
    total=False,
)

CaptionDescriptionPresetTypeDef = TypedDict(
    "CaptionDescriptionPresetTypeDef",
    {
        "CustomLanguageCode": str,
        "DestinationSettings": "CaptionDestinationSettingsTypeDef",
        "LanguageCode": LanguageCode,
        "LanguageDescription": str,
    },
    total=False,
)

CaptionDescriptionTypeDef = TypedDict(
    "CaptionDescriptionTypeDef",
    {
        "CaptionSelectorName": str,
        "CustomLanguageCode": str,
        "DestinationSettings": "CaptionDestinationSettingsTypeDef",
        "LanguageCode": LanguageCode,
        "LanguageDescription": str,
    },
    total=False,
)

CaptionDestinationSettingsTypeDef = TypedDict(
    "CaptionDestinationSettingsTypeDef",
    {
        "BurninDestinationSettings": "BurninDestinationSettingsTypeDef",
        "DestinationType": CaptionDestinationType,
        "DvbSubDestinationSettings": "DvbSubDestinationSettingsTypeDef",
        "EmbeddedDestinationSettings": "EmbeddedDestinationSettingsTypeDef",
        "ImscDestinationSettings": "ImscDestinationSettingsTypeDef",
        "SccDestinationSettings": "SccDestinationSettingsTypeDef",
        "TeletextDestinationSettings": "TeletextDestinationSettingsTypeDef",
        "TtmlDestinationSettings": "TtmlDestinationSettingsTypeDef",
        "WebvttDestinationSettings": "WebvttDestinationSettingsTypeDef",
    },
    total=False,
)

CaptionSelectorTypeDef = TypedDict(
    "CaptionSelectorTypeDef",
    {
        "CustomLanguageCode": str,
        "LanguageCode": LanguageCode,
        "SourceSettings": "CaptionSourceSettingsTypeDef",
    },
    total=False,
)

CaptionSourceFramerateTypeDef = TypedDict(
    "CaptionSourceFramerateTypeDef",
    {"FramerateDenominator": int, "FramerateNumerator": int},
    total=False,
)

CaptionSourceSettingsTypeDef = TypedDict(
    "CaptionSourceSettingsTypeDef",
    {
        "AncillarySourceSettings": "AncillarySourceSettingsTypeDef",
        "DvbSubSourceSettings": "DvbSubSourceSettingsTypeDef",
        "EmbeddedSourceSettings": "EmbeddedSourceSettingsTypeDef",
        "FileSourceSettings": "FileSourceSettingsTypeDef",
        "SourceType": CaptionSourceType,
        "TeletextSourceSettings": "TeletextSourceSettingsTypeDef",
        "TrackSourceSettings": "TrackSourceSettingsTypeDef",
    },
    total=False,
)

ChannelMappingTypeDef = TypedDict(
    "ChannelMappingTypeDef", {"OutputChannels": List["OutputChannelMappingTypeDef"]}, total=False
)

CmafAdditionalManifestTypeDef = TypedDict(
    "CmafAdditionalManifestTypeDef",
    {"ManifestNameModifier": str, "SelectedOutputs": List[str]},
    total=False,
)

CmafEncryptionSettingsTypeDef = TypedDict(
    "CmafEncryptionSettingsTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": CmafEncryptionType,
        "InitializationVectorInManifest": CmafInitializationVectorInManifest,
        "SpekeKeyProvider": "SpekeKeyProviderCmafTypeDef",
        "StaticKeyProvider": "StaticKeyProviderTypeDef",
        "Type": CmafKeyProviderType,
    },
    total=False,
)

CmafGroupSettingsTypeDef = TypedDict(
    "CmafGroupSettingsTypeDef",
    {
        "AdditionalManifests": List["CmafAdditionalManifestTypeDef"],
        "BaseUrl": str,
        "ClientCache": CmafClientCache,
        "CodecSpecification": CmafCodecSpecification,
        "Destination": str,
        "DestinationSettings": "DestinationSettingsTypeDef",
        "Encryption": "CmafEncryptionSettingsTypeDef",
        "FragmentLength": int,
        "ManifestCompression": CmafManifestCompression,
        "ManifestDurationFormat": CmafManifestDurationFormat,
        "MinBufferTime": int,
        "MinFinalSegmentLength": float,
        "MpdProfile": CmafMpdProfile,
        "PtsOffsetHandlingForBFrames": CmafPtsOffsetHandlingForBFrames,
        "SegmentControl": CmafSegmentControl,
        "SegmentLength": int,
        "StreamInfResolution": CmafStreamInfResolution,
        "WriteDashManifest": CmafWriteDASHManifest,
        "WriteHlsManifest": CmafWriteHLSManifest,
        "WriteSegmentTimelineInRepresentation": CmafWriteSegmentTimelineInRepresentation,
    },
    total=False,
)

CmfcSettingsTypeDef = TypedDict(
    "CmfcSettingsTypeDef",
    {
        "AudioDuration": CmfcAudioDuration,
        "AudioGroupId": str,
        "AudioRenditionSets": str,
        "AudioTrackType": CmfcAudioTrackType,
        "DescriptiveVideoServiceFlag": CmfcDescriptiveVideoServiceFlag,
        "IFrameOnlyManifest": CmfcIFrameOnlyManifest,
        "Scte35Esam": CmfcScte35Esam,
        "Scte35Source": CmfcScte35Source,
    },
    total=False,
)

ColorCorrectorTypeDef = TypedDict(
    "ColorCorrectorTypeDef",
    {
        "Brightness": int,
        "ColorSpaceConversion": ColorSpaceConversion,
        "Contrast": int,
        "Hdr10Metadata": "Hdr10MetadataTypeDef",
        "Hue": int,
        "Saturation": int,
    },
    total=False,
)

ContainerSettingsTypeDef = TypedDict(
    "ContainerSettingsTypeDef",
    {
        "CmfcSettings": "CmfcSettingsTypeDef",
        "Container": ContainerType,
        "F4vSettings": "F4vSettingsTypeDef",
        "M2tsSettings": "M2tsSettingsTypeDef",
        "M3u8Settings": "M3u8SettingsTypeDef",
        "MovSettings": "MovSettingsTypeDef",
        "Mp4Settings": "Mp4SettingsTypeDef",
        "MpdSettings": "MpdSettingsTypeDef",
        "MxfSettings": "MxfSettingsTypeDef",
    },
    total=False,
)

DashAdditionalManifestTypeDef = TypedDict(
    "DashAdditionalManifestTypeDef",
    {"ManifestNameModifier": str, "SelectedOutputs": List[str]},
    total=False,
)

DashIsoEncryptionSettingsTypeDef = TypedDict(
    "DashIsoEncryptionSettingsTypeDef",
    {
        "PlaybackDeviceCompatibility": DashIsoPlaybackDeviceCompatibility,
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
    },
    total=False,
)

DashIsoGroupSettingsTypeDef = TypedDict(
    "DashIsoGroupSettingsTypeDef",
    {
        "AdditionalManifests": List["DashAdditionalManifestTypeDef"],
        "AudioChannelConfigSchemeIdUri": DashIsoGroupAudioChannelConfigSchemeIdUri,
        "BaseUrl": str,
        "Destination": str,
        "DestinationSettings": "DestinationSettingsTypeDef",
        "Encryption": "DashIsoEncryptionSettingsTypeDef",
        "FragmentLength": int,
        "HbbtvCompliance": DashIsoHbbtvCompliance,
        "MinBufferTime": int,
        "MinFinalSegmentLength": float,
        "MpdProfile": DashIsoMpdProfile,
        "PtsOffsetHandlingForBFrames": DashIsoPtsOffsetHandlingForBFrames,
        "SegmentControl": DashIsoSegmentControl,
        "SegmentLength": int,
        "WriteSegmentTimelineInRepresentation": DashIsoWriteSegmentTimelineInRepresentation,
    },
    total=False,
)

DeinterlacerTypeDef = TypedDict(
    "DeinterlacerTypeDef",
    {"Algorithm": DeinterlaceAlgorithm, "Control": DeinterlacerControl, "Mode": DeinterlacerMode},
    total=False,
)

DestinationSettingsTypeDef = TypedDict(
    "DestinationSettingsTypeDef", {"S3Settings": "S3DestinationSettingsTypeDef"}, total=False
)

DolbyVisionLevel6MetadataTypeDef = TypedDict(
    "DolbyVisionLevel6MetadataTypeDef", {"MaxCll": int, "MaxFall": int}, total=False
)

DolbyVisionTypeDef = TypedDict(
    "DolbyVisionTypeDef",
    {
        "L6Metadata": "DolbyVisionLevel6MetadataTypeDef",
        "L6Mode": DolbyVisionLevel6Mode,
        "Profile": DolbyVisionProfile,
    },
    total=False,
)

DvbNitSettingsTypeDef = TypedDict(
    "DvbNitSettingsTypeDef", {"NetworkId": int, "NetworkName": str, "NitInterval": int}, total=False
)

DvbSdtSettingsTypeDef = TypedDict(
    "DvbSdtSettingsTypeDef",
    {"OutputSdt": OutputSdt, "SdtInterval": int, "ServiceName": str, "ServiceProviderName": str},
    total=False,
)

DvbSubDestinationSettingsTypeDef = TypedDict(
    "DvbSubDestinationSettingsTypeDef",
    {
        "Alignment": DvbSubtitleAlignment,
        "BackgroundColor": DvbSubtitleBackgroundColor,
        "BackgroundOpacity": int,
        "FontColor": DvbSubtitleFontColor,
        "FontOpacity": int,
        "FontResolution": int,
        "FontScript": FontScript,
        "FontSize": int,
        "OutlineColor": DvbSubtitleOutlineColor,
        "OutlineSize": int,
        "ShadowColor": DvbSubtitleShadowColor,
        "ShadowOpacity": int,
        "ShadowXOffset": int,
        "ShadowYOffset": int,
        "SubtitlingType": DvbSubtitlingType,
        "TeletextSpacing": DvbSubtitleTeletextSpacing,
        "XPosition": int,
        "YPosition": int,
    },
    total=False,
)

DvbSubSourceSettingsTypeDef = TypedDict("DvbSubSourceSettingsTypeDef", {"Pid": int}, total=False)

DvbTdtSettingsTypeDef = TypedDict("DvbTdtSettingsTypeDef", {"TdtInterval": int}, total=False)

Eac3AtmosSettingsTypeDef = TypedDict(
    "Eac3AtmosSettingsTypeDef",
    {
        "Bitrate": int,
        "BitstreamMode": Eac3AtmosBitstreamMode,
        "CodingMode": Eac3AtmosCodingMode,
        "DialogueIntelligence": Eac3AtmosDialogueIntelligence,
        "DynamicRangeCompressionLine": Eac3AtmosDynamicRangeCompressionLine,
        "DynamicRangeCompressionRf": Eac3AtmosDynamicRangeCompressionRf,
        "LoRoCenterMixLevel": float,
        "LoRoSurroundMixLevel": float,
        "LtRtCenterMixLevel": float,
        "LtRtSurroundMixLevel": float,
        "MeteringMode": Eac3AtmosMeteringMode,
        "SampleRate": int,
        "SpeechThreshold": int,
        "StereoDownmix": Eac3AtmosStereoDownmix,
        "SurroundExMode": Eac3AtmosSurroundExMode,
    },
    total=False,
)

Eac3SettingsTypeDef = TypedDict(
    "Eac3SettingsTypeDef",
    {
        "AttenuationControl": Eac3AttenuationControl,
        "Bitrate": int,
        "BitstreamMode": Eac3BitstreamMode,
        "CodingMode": Eac3CodingMode,
        "DcFilter": Eac3DcFilter,
        "Dialnorm": int,
        "DynamicRangeCompressionLine": Eac3DynamicRangeCompressionLine,
        "DynamicRangeCompressionRf": Eac3DynamicRangeCompressionRf,
        "LfeControl": Eac3LfeControl,
        "LfeFilter": Eac3LfeFilter,
        "LoRoCenterMixLevel": float,
        "LoRoSurroundMixLevel": float,
        "LtRtCenterMixLevel": float,
        "LtRtSurroundMixLevel": float,
        "MetadataControl": Eac3MetadataControl,
        "PassthroughControl": Eac3PassthroughControl,
        "PhaseControl": Eac3PhaseControl,
        "SampleRate": int,
        "StereoDownmix": Eac3StereoDownmix,
        "SurroundExMode": Eac3SurroundExMode,
        "SurroundMode": Eac3SurroundMode,
    },
    total=False,
)

EmbeddedDestinationSettingsTypeDef = TypedDict(
    "EmbeddedDestinationSettingsTypeDef",
    {"Destination608ChannelNumber": int, "Destination708ServiceNumber": int},
    total=False,
)

EmbeddedSourceSettingsTypeDef = TypedDict(
    "EmbeddedSourceSettingsTypeDef",
    {
        "Convert608To708": EmbeddedConvert608To708,
        "Source608ChannelNumber": int,
        "Source608TrackNumber": int,
        "TerminateCaptions": EmbeddedTerminateCaptions,
    },
    total=False,
)

EndpointTypeDef = TypedDict("EndpointTypeDef", {"Url": str}, total=False)

EsamManifestConfirmConditionNotificationTypeDef = TypedDict(
    "EsamManifestConfirmConditionNotificationTypeDef", {"MccXml": str}, total=False
)

EsamSettingsTypeDef = TypedDict(
    "EsamSettingsTypeDef",
    {
        "ManifestConfirmConditionNotification": "EsamManifestConfirmConditionNotificationTypeDef",
        "ResponseSignalPreroll": int,
        "SignalProcessingNotification": "EsamSignalProcessingNotificationTypeDef",
    },
    total=False,
)

EsamSignalProcessingNotificationTypeDef = TypedDict(
    "EsamSignalProcessingNotificationTypeDef", {"SccXml": str}, total=False
)

F4vSettingsTypeDef = TypedDict(
    "F4vSettingsTypeDef", {"MoovPlacement": F4vMoovPlacement}, total=False
)

FileGroupSettingsTypeDef = TypedDict(
    "FileGroupSettingsTypeDef",
    {"Destination": str, "DestinationSettings": "DestinationSettingsTypeDef"},
    total=False,
)

FileSourceSettingsTypeDef = TypedDict(
    "FileSourceSettingsTypeDef",
    {
        "Convert608To708": FileSourceConvert608To708,
        "Framerate": "CaptionSourceFramerateTypeDef",
        "SourceFile": str,
        "TimeDelta": int,
    },
    total=False,
)

FrameCaptureSettingsTypeDef = TypedDict(
    "FrameCaptureSettingsTypeDef",
    {"FramerateDenominator": int, "FramerateNumerator": int, "MaxCaptures": int, "Quality": int},
    total=False,
)

H264QvbrSettingsTypeDef = TypedDict(
    "H264QvbrSettingsTypeDef",
    {"MaxAverageBitrate": int, "QvbrQualityLevel": int, "QvbrQualityLevelFineTune": float},
    total=False,
)

H264SettingsTypeDef = TypedDict(
    "H264SettingsTypeDef",
    {
        "AdaptiveQuantization": H264AdaptiveQuantization,
        "Bitrate": int,
        "CodecLevel": H264CodecLevel,
        "CodecProfile": H264CodecProfile,
        "DynamicSubGop": H264DynamicSubGop,
        "EntropyEncoding": H264EntropyEncoding,
        "FieldEncoding": H264FieldEncoding,
        "FlickerAdaptiveQuantization": H264FlickerAdaptiveQuantization,
        "FramerateControl": H264FramerateControl,
        "FramerateConversionAlgorithm": H264FramerateConversionAlgorithm,
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "GopBReference": H264GopBReference,
        "GopClosedCadence": int,
        "GopSize": float,
        "GopSizeUnits": H264GopSizeUnits,
        "HrdBufferInitialFillPercentage": int,
        "HrdBufferSize": int,
        "InterlaceMode": H264InterlaceMode,
        "MaxBitrate": int,
        "MinIInterval": int,
        "NumberBFramesBetweenReferenceFrames": int,
        "NumberReferenceFrames": int,
        "ParControl": H264ParControl,
        "ParDenominator": int,
        "ParNumerator": int,
        "QualityTuningLevel": H264QualityTuningLevel,
        "QvbrSettings": "H264QvbrSettingsTypeDef",
        "RateControlMode": H264RateControlMode,
        "RepeatPps": H264RepeatPps,
        "ScanTypeConversionMode": H264ScanTypeConversionMode,
        "SceneChangeDetect": H264SceneChangeDetect,
        "Slices": int,
        "SlowPal": H264SlowPal,
        "Softness": int,
        "SpatialAdaptiveQuantization": H264SpatialAdaptiveQuantization,
        "Syntax": H264Syntax,
        "Telecine": H264Telecine,
        "TemporalAdaptiveQuantization": H264TemporalAdaptiveQuantization,
        "UnregisteredSeiTimecode": H264UnregisteredSeiTimecode,
    },
    total=False,
)

H265QvbrSettingsTypeDef = TypedDict(
    "H265QvbrSettingsTypeDef",
    {"MaxAverageBitrate": int, "QvbrQualityLevel": int, "QvbrQualityLevelFineTune": float},
    total=False,
)

H265SettingsTypeDef = TypedDict(
    "H265SettingsTypeDef",
    {
        "AdaptiveQuantization": H265AdaptiveQuantization,
        "AlternateTransferFunctionSei": H265AlternateTransferFunctionSei,
        "Bitrate": int,
        "CodecLevel": H265CodecLevel,
        "CodecProfile": H265CodecProfile,
        "DynamicSubGop": H265DynamicSubGop,
        "FlickerAdaptiveQuantization": H265FlickerAdaptiveQuantization,
        "FramerateControl": H265FramerateControl,
        "FramerateConversionAlgorithm": H265FramerateConversionAlgorithm,
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "GopBReference": H265GopBReference,
        "GopClosedCadence": int,
        "GopSize": float,
        "GopSizeUnits": H265GopSizeUnits,
        "HrdBufferInitialFillPercentage": int,
        "HrdBufferSize": int,
        "InterlaceMode": H265InterlaceMode,
        "MaxBitrate": int,
        "MinIInterval": int,
        "NumberBFramesBetweenReferenceFrames": int,
        "NumberReferenceFrames": int,
        "ParControl": H265ParControl,
        "ParDenominator": int,
        "ParNumerator": int,
        "QualityTuningLevel": H265QualityTuningLevel,
        "QvbrSettings": "H265QvbrSettingsTypeDef",
        "RateControlMode": H265RateControlMode,
        "SampleAdaptiveOffsetFilterMode": H265SampleAdaptiveOffsetFilterMode,
        "ScanTypeConversionMode": H265ScanTypeConversionMode,
        "SceneChangeDetect": H265SceneChangeDetect,
        "Slices": int,
        "SlowPal": H265SlowPal,
        "SpatialAdaptiveQuantization": H265SpatialAdaptiveQuantization,
        "Telecine": H265Telecine,
        "TemporalAdaptiveQuantization": H265TemporalAdaptiveQuantization,
        "TemporalIds": H265TemporalIds,
        "Tiles": H265Tiles,
        "UnregisteredSeiTimecode": H265UnregisteredSeiTimecode,
        "WriteMp4PackagingType": H265WriteMp4PackagingType,
    },
    total=False,
)

Hdr10MetadataTypeDef = TypedDict(
    "Hdr10MetadataTypeDef",
    {
        "BluePrimaryX": int,
        "BluePrimaryY": int,
        "GreenPrimaryX": int,
        "GreenPrimaryY": int,
        "MaxContentLightLevel": int,
        "MaxFrameAverageLightLevel": int,
        "MaxLuminance": int,
        "MinLuminance": int,
        "RedPrimaryX": int,
        "RedPrimaryY": int,
        "WhitePointX": int,
        "WhitePointY": int,
    },
    total=False,
)

HlsAdditionalManifestTypeDef = TypedDict(
    "HlsAdditionalManifestTypeDef",
    {"ManifestNameModifier": str, "SelectedOutputs": List[str]},
    total=False,
)

HlsCaptionLanguageMappingTypeDef = TypedDict(
    "HlsCaptionLanguageMappingTypeDef",
    {
        "CaptionChannel": int,
        "CustomLanguageCode": str,
        "LanguageCode": LanguageCode,
        "LanguageDescription": str,
    },
    total=False,
)

HlsEncryptionSettingsTypeDef = TypedDict(
    "HlsEncryptionSettingsTypeDef",
    {
        "ConstantInitializationVector": str,
        "EncryptionMethod": HlsEncryptionType,
        "InitializationVectorInManifest": HlsInitializationVectorInManifest,
        "OfflineEncrypted": HlsOfflineEncrypted,
        "SpekeKeyProvider": "SpekeKeyProviderTypeDef",
        "StaticKeyProvider": "StaticKeyProviderTypeDef",
        "Type": HlsKeyProviderType,
    },
    total=False,
)

HlsGroupSettingsTypeDef = TypedDict(
    "HlsGroupSettingsTypeDef",
    {
        "AdMarkers": List[HlsAdMarkers],
        "AdditionalManifests": List["HlsAdditionalManifestTypeDef"],
        "AudioOnlyHeader": HlsAudioOnlyHeader,
        "BaseUrl": str,
        "CaptionLanguageMappings": List["HlsCaptionLanguageMappingTypeDef"],
        "CaptionLanguageSetting": HlsCaptionLanguageSetting,
        "ClientCache": HlsClientCache,
        "CodecSpecification": HlsCodecSpecification,
        "Destination": str,
        "DestinationSettings": "DestinationSettingsTypeDef",
        "DirectoryStructure": HlsDirectoryStructure,
        "Encryption": "HlsEncryptionSettingsTypeDef",
        "ManifestCompression": HlsManifestCompression,
        "ManifestDurationFormat": HlsManifestDurationFormat,
        "MinFinalSegmentLength": float,
        "MinSegmentLength": int,
        "OutputSelection": HlsOutputSelection,
        "ProgramDateTime": HlsProgramDateTime,
        "ProgramDateTimePeriod": int,
        "SegmentControl": HlsSegmentControl,
        "SegmentLength": int,
        "SegmentsPerSubdirectory": int,
        "StreamInfResolution": HlsStreamInfResolution,
        "TimedMetadataId3Frame": HlsTimedMetadataId3Frame,
        "TimedMetadataId3Period": int,
        "TimestampDeltaMilliseconds": int,
    },
    total=False,
)

HlsSettingsTypeDef = TypedDict(
    "HlsSettingsTypeDef",
    {
        "AudioGroupId": str,
        "AudioOnlyContainer": HlsAudioOnlyContainer,
        "AudioRenditionSets": str,
        "AudioTrackType": HlsAudioTrackType,
        "DescriptiveVideoServiceFlag": HlsDescriptiveVideoServiceFlag,
        "IFrameOnlyManifest": HlsIFrameOnlyManifest,
        "SegmentModifier": str,
    },
    total=False,
)

HopDestinationTypeDef = TypedDict(
    "HopDestinationTypeDef", {"Priority": int, "Queue": str, "WaitMinutes": int}, total=False
)

Id3InsertionTypeDef = TypedDict("Id3InsertionTypeDef", {"Id3": str, "Timecode": str}, total=False)

ImageInserterTypeDef = TypedDict(
    "ImageInserterTypeDef", {"InsertableImages": List["InsertableImageTypeDef"]}, total=False
)

ImscDestinationSettingsTypeDef = TypedDict(
    "ImscDestinationSettingsTypeDef", {"StylePassthrough": ImscStylePassthrough}, total=False
)

InputClippingTypeDef = TypedDict(
    "InputClippingTypeDef", {"EndTimecode": str, "StartTimecode": str}, total=False
)

InputDecryptionSettingsTypeDef = TypedDict(
    "InputDecryptionSettingsTypeDef",
    {
        "DecryptionMode": DecryptionMode,
        "EncryptedDecryptionKey": str,
        "InitializationVector": str,
        "KmsKeyRegion": str,
    },
    total=False,
)

InputTemplateTypeDef = TypedDict(
    "InputTemplateTypeDef",
    {
        "AudioSelectorGroups": Dict[str, "AudioSelectorGroupTypeDef"],
        "AudioSelectors": Dict[str, "AudioSelectorTypeDef"],
        "CaptionSelectors": Dict[str, "CaptionSelectorTypeDef"],
        "Crop": "RectangleTypeDef",
        "DeblockFilter": InputDeblockFilter,
        "DenoiseFilter": InputDenoiseFilter,
        "FilterEnable": InputFilterEnable,
        "FilterStrength": int,
        "ImageInserter": "ImageInserterTypeDef",
        "InputClippings": List["InputClippingTypeDef"],
        "InputScanType": InputScanType,
        "Position": "RectangleTypeDef",
        "ProgramNumber": int,
        "PsiControl": InputPsiControl,
        "TimecodeSource": InputTimecodeSource,
        "TimecodeStart": str,
        "VideoSelector": "VideoSelectorTypeDef",
    },
    total=False,
)

InputTypeDef = TypedDict(
    "InputTypeDef",
    {
        "AudioSelectorGroups": Dict[str, "AudioSelectorGroupTypeDef"],
        "AudioSelectors": Dict[str, "AudioSelectorTypeDef"],
        "CaptionSelectors": Dict[str, "CaptionSelectorTypeDef"],
        "Crop": "RectangleTypeDef",
        "DeblockFilter": InputDeblockFilter,
        "DecryptionSettings": "InputDecryptionSettingsTypeDef",
        "DenoiseFilter": InputDenoiseFilter,
        "FileInput": str,
        "FilterEnable": InputFilterEnable,
        "FilterStrength": int,
        "ImageInserter": "ImageInserterTypeDef",
        "InputClippings": List["InputClippingTypeDef"],
        "InputScanType": InputScanType,
        "Position": "RectangleTypeDef",
        "ProgramNumber": int,
        "PsiControl": InputPsiControl,
        "SupplementalImps": List[str],
        "TimecodeSource": InputTimecodeSource,
        "TimecodeStart": str,
        "VideoSelector": "VideoSelectorTypeDef",
    },
    total=False,
)

InsertableImageTypeDef = TypedDict(
    "InsertableImageTypeDef",
    {
        "Duration": int,
        "FadeIn": int,
        "FadeOut": int,
        "Height": int,
        "ImageInserterInput": str,
        "ImageX": int,
        "ImageY": int,
        "Layer": int,
        "Opacity": int,
        "StartTime": str,
        "Width": int,
    },
    total=False,
)

JobMessagesTypeDef = TypedDict(
    "JobMessagesTypeDef", {"Info": List[str], "Warning": List[str]}, total=False
)

JobSettingsTypeDef = TypedDict(
    "JobSettingsTypeDef",
    {
        "AdAvailOffset": int,
        "AvailBlanking": "AvailBlankingTypeDef",
        "Esam": "EsamSettingsTypeDef",
        "Inputs": List["InputTypeDef"],
        "MotionImageInserter": "MotionImageInserterTypeDef",
        "NielsenConfiguration": "NielsenConfigurationTypeDef",
        "NielsenNonLinearWatermark": "NielsenNonLinearWatermarkSettingsTypeDef",
        "OutputGroups": List["OutputGroupTypeDef"],
        "TimecodeConfig": "TimecodeConfigTypeDef",
        "TimedMetadataInsertion": "TimedMetadataInsertionTypeDef",
    },
    total=False,
)

JobTemplateSettingsTypeDef = TypedDict(
    "JobTemplateSettingsTypeDef",
    {
        "AdAvailOffset": int,
        "AvailBlanking": "AvailBlankingTypeDef",
        "Esam": "EsamSettingsTypeDef",
        "Inputs": List["InputTemplateTypeDef"],
        "MotionImageInserter": "MotionImageInserterTypeDef",
        "NielsenConfiguration": "NielsenConfigurationTypeDef",
        "NielsenNonLinearWatermark": "NielsenNonLinearWatermarkSettingsTypeDef",
        "OutputGroups": List["OutputGroupTypeDef"],
        "TimecodeConfig": "TimecodeConfigTypeDef",
        "TimedMetadataInsertion": "TimedMetadataInsertionTypeDef",
    },
    total=False,
)

_RequiredJobTemplateTypeDef = TypedDict(
    "_RequiredJobTemplateTypeDef", {"Name": str, "Settings": "JobTemplateSettingsTypeDef"}
)
_OptionalJobTemplateTypeDef = TypedDict(
    "_OptionalJobTemplateTypeDef",
    {
        "AccelerationSettings": "AccelerationSettingsTypeDef",
        "Arn": str,
        "Category": str,
        "CreatedAt": datetime,
        "Description": str,
        "HopDestinations": List["HopDestinationTypeDef"],
        "LastUpdated": datetime,
        "Priority": int,
        "Queue": str,
        "StatusUpdateInterval": StatusUpdateInterval,
        "Type": TypeType,
    },
    total=False,
)


class JobTemplateTypeDef(_RequiredJobTemplateTypeDef, _OptionalJobTemplateTypeDef):
    pass


_RequiredJobTypeDef = TypedDict(
    "_RequiredJobTypeDef", {"Role": str, "Settings": "JobSettingsTypeDef"}
)
_OptionalJobTypeDef = TypedDict(
    "_OptionalJobTypeDef",
    {
        "AccelerationSettings": "AccelerationSettingsTypeDef",
        "AccelerationStatus": AccelerationStatus,
        "Arn": str,
        "BillingTagsSource": BillingTagsSource,
        "CreatedAt": datetime,
        "CurrentPhase": JobPhase,
        "ErrorCode": int,
        "ErrorMessage": str,
        "HopDestinations": List["HopDestinationTypeDef"],
        "Id": str,
        "JobPercentComplete": int,
        "JobTemplate": str,
        "Messages": "JobMessagesTypeDef",
        "OutputGroupDetails": List["OutputGroupDetailTypeDef"],
        "Priority": int,
        "Queue": str,
        "QueueTransitions": List["QueueTransitionTypeDef"],
        "RetryCount": int,
        "SimulateReservedQueue": SimulateReservedQueue,
        "Status": JobStatus,
        "StatusUpdateInterval": StatusUpdateInterval,
        "Timing": "TimingTypeDef",
        "UserMetadata": Dict[str, str],
    },
    total=False,
)


class JobTypeDef(_RequiredJobTypeDef, _OptionalJobTypeDef):
    pass


M2tsScte35EsamTypeDef = TypedDict("M2tsScte35EsamTypeDef", {"Scte35EsamPid": int}, total=False)

M2tsSettingsTypeDef = TypedDict(
    "M2tsSettingsTypeDef",
    {
        "AudioBufferModel": M2tsAudioBufferModel,
        "AudioDuration": M2tsAudioDuration,
        "AudioFramesPerPes": int,
        "AudioPids": List[int],
        "Bitrate": int,
        "BufferModel": M2tsBufferModel,
        "DvbNitSettings": "DvbNitSettingsTypeDef",
        "DvbSdtSettings": "DvbSdtSettingsTypeDef",
        "DvbSubPids": List[int],
        "DvbTdtSettings": "DvbTdtSettingsTypeDef",
        "DvbTeletextPid": int,
        "EbpAudioInterval": M2tsEbpAudioInterval,
        "EbpPlacement": M2tsEbpPlacement,
        "EsRateInPes": M2tsEsRateInPes,
        "ForceTsVideoEbpOrder": M2tsForceTsVideoEbpOrder,
        "FragmentTime": float,
        "MaxPcrInterval": int,
        "MinEbpInterval": int,
        "NielsenId3": M2tsNielsenId3,
        "NullPacketBitrate": float,
        "PatInterval": int,
        "PcrControl": M2tsPcrControl,
        "PcrPid": int,
        "PmtInterval": int,
        "PmtPid": int,
        "PrivateMetadataPid": int,
        "ProgramNumber": int,
        "RateMode": M2tsRateMode,
        "Scte35Esam": "M2tsScte35EsamTypeDef",
        "Scte35Pid": int,
        "Scte35Source": M2tsScte35Source,
        "SegmentationMarkers": M2tsSegmentationMarkers,
        "SegmentationStyle": M2tsSegmentationStyle,
        "SegmentationTime": float,
        "TimedMetadataPid": int,
        "TransportStreamId": int,
        "VideoPid": int,
    },
    total=False,
)

M3u8SettingsTypeDef = TypedDict(
    "M3u8SettingsTypeDef",
    {
        "AudioDuration": M3u8AudioDuration,
        "AudioFramesPerPes": int,
        "AudioPids": List[int],
        "NielsenId3": M3u8NielsenId3,
        "PatInterval": int,
        "PcrControl": M3u8PcrControl,
        "PcrPid": int,
        "PmtInterval": int,
        "PmtPid": int,
        "PrivateMetadataPid": int,
        "ProgramNumber": int,
        "Scte35Pid": int,
        "Scte35Source": M3u8Scte35Source,
        "TimedMetadata": TimedMetadata,
        "TimedMetadataPid": int,
        "TransportStreamId": int,
        "VideoPid": int,
    },
    total=False,
)

MotionImageInserterTypeDef = TypedDict(
    "MotionImageInserterTypeDef",
    {
        "Framerate": "MotionImageInsertionFramerateTypeDef",
        "Input": str,
        "InsertionMode": MotionImageInsertionMode,
        "Offset": "MotionImageInsertionOffsetTypeDef",
        "Playback": MotionImagePlayback,
        "StartTime": str,
    },
    total=False,
)

MotionImageInsertionFramerateTypeDef = TypedDict(
    "MotionImageInsertionFramerateTypeDef",
    {"FramerateDenominator": int, "FramerateNumerator": int},
    total=False,
)

MotionImageInsertionOffsetTypeDef = TypedDict(
    "MotionImageInsertionOffsetTypeDef", {"ImageX": int, "ImageY": int}, total=False
)

MovSettingsTypeDef = TypedDict(
    "MovSettingsTypeDef",
    {
        "ClapAtom": MovClapAtom,
        "CslgAtom": MovCslgAtom,
        "Mpeg2FourCCControl": MovMpeg2FourCCControl,
        "PaddingControl": MovPaddingControl,
        "Reference": MovReference,
    },
    total=False,
)

Mp2SettingsTypeDef = TypedDict(
    "Mp2SettingsTypeDef", {"Bitrate": int, "Channels": int, "SampleRate": int}, total=False
)

Mp3SettingsTypeDef = TypedDict(
    "Mp3SettingsTypeDef",
    {
        "Bitrate": int,
        "Channels": int,
        "RateControlMode": Mp3RateControlMode,
        "SampleRate": int,
        "VbrQuality": int,
    },
    total=False,
)

Mp4SettingsTypeDef = TypedDict(
    "Mp4SettingsTypeDef",
    {
        "AudioDuration": CmfcAudioDuration,
        "CslgAtom": Mp4CslgAtom,
        "CttsVersion": int,
        "FreeSpaceBox": Mp4FreeSpaceBox,
        "MoovPlacement": Mp4MoovPlacement,
        "Mp4MajorBrand": str,
    },
    total=False,
)

MpdSettingsTypeDef = TypedDict(
    "MpdSettingsTypeDef",
    {
        "AccessibilityCaptionHints": MpdAccessibilityCaptionHints,
        "AudioDuration": MpdAudioDuration,
        "CaptionContainerType": MpdCaptionContainerType,
        "Scte35Esam": MpdScte35Esam,
        "Scte35Source": MpdScte35Source,
    },
    total=False,
)

Mpeg2SettingsTypeDef = TypedDict(
    "Mpeg2SettingsTypeDef",
    {
        "AdaptiveQuantization": Mpeg2AdaptiveQuantization,
        "Bitrate": int,
        "CodecLevel": Mpeg2CodecLevel,
        "CodecProfile": Mpeg2CodecProfile,
        "DynamicSubGop": Mpeg2DynamicSubGop,
        "FramerateControl": Mpeg2FramerateControl,
        "FramerateConversionAlgorithm": Mpeg2FramerateConversionAlgorithm,
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "GopClosedCadence": int,
        "GopSize": float,
        "GopSizeUnits": Mpeg2GopSizeUnits,
        "HrdBufferInitialFillPercentage": int,
        "HrdBufferSize": int,
        "InterlaceMode": Mpeg2InterlaceMode,
        "IntraDcPrecision": Mpeg2IntraDcPrecision,
        "MaxBitrate": int,
        "MinIInterval": int,
        "NumberBFramesBetweenReferenceFrames": int,
        "ParControl": Mpeg2ParControl,
        "ParDenominator": int,
        "ParNumerator": int,
        "QualityTuningLevel": Mpeg2QualityTuningLevel,
        "RateControlMode": Mpeg2RateControlMode,
        "ScanTypeConversionMode": Mpeg2ScanTypeConversionMode,
        "SceneChangeDetect": Mpeg2SceneChangeDetect,
        "SlowPal": Mpeg2SlowPal,
        "Softness": int,
        "SpatialAdaptiveQuantization": Mpeg2SpatialAdaptiveQuantization,
        "Syntax": Mpeg2Syntax,
        "Telecine": Mpeg2Telecine,
        "TemporalAdaptiveQuantization": Mpeg2TemporalAdaptiveQuantization,
    },
    total=False,
)

MsSmoothAdditionalManifestTypeDef = TypedDict(
    "MsSmoothAdditionalManifestTypeDef",
    {"ManifestNameModifier": str, "SelectedOutputs": List[str]},
    total=False,
)

MsSmoothEncryptionSettingsTypeDef = TypedDict(
    "MsSmoothEncryptionSettingsTypeDef",
    {"SpekeKeyProvider": "SpekeKeyProviderTypeDef"},
    total=False,
)

MsSmoothGroupSettingsTypeDef = TypedDict(
    "MsSmoothGroupSettingsTypeDef",
    {
        "AdditionalManifests": List["MsSmoothAdditionalManifestTypeDef"],
        "AudioDeduplication": MsSmoothAudioDeduplication,
        "Destination": str,
        "DestinationSettings": "DestinationSettingsTypeDef",
        "Encryption": "MsSmoothEncryptionSettingsTypeDef",
        "FragmentLength": int,
        "ManifestEncoding": MsSmoothManifestEncoding,
    },
    total=False,
)

MxfSettingsTypeDef = TypedDict(
    "MxfSettingsTypeDef", {"AfdSignaling": MxfAfdSignaling, "Profile": MxfProfile}, total=False
)

NexGuardFileMarkerSettingsTypeDef = TypedDict(
    "NexGuardFileMarkerSettingsTypeDef",
    {"License": str, "Payload": int, "Preset": str, "Strength": WatermarkingStrength},
    total=False,
)

NielsenConfigurationTypeDef = TypedDict(
    "NielsenConfigurationTypeDef", {"BreakoutCode": int, "DistributorId": str}, total=False
)

NielsenNonLinearWatermarkSettingsTypeDef = TypedDict(
    "NielsenNonLinearWatermarkSettingsTypeDef",
    {
        "ActiveWatermarkProcess": NielsenActiveWatermarkProcessType,
        "AdiFilename": str,
        "AssetId": str,
        "AssetName": str,
        "CbetSourceId": str,
        "EpisodeId": str,
        "MetadataDestination": str,
        "SourceId": int,
        "SourceWatermarkStatus": NielsenSourceWatermarkStatusType,
        "TicServerUrl": str,
        "UniqueTicPerAudioTrack": NielsenUniqueTicPerAudioTrackType,
    },
    total=False,
)

NoiseReducerFilterSettingsTypeDef = TypedDict(
    "NoiseReducerFilterSettingsTypeDef", {"Strength": int}, total=False
)

NoiseReducerSpatialFilterSettingsTypeDef = TypedDict(
    "NoiseReducerSpatialFilterSettingsTypeDef",
    {"PostFilterSharpenStrength": int, "Speed": int, "Strength": int},
    total=False,
)

NoiseReducerTemporalFilterSettingsTypeDef = TypedDict(
    "NoiseReducerTemporalFilterSettingsTypeDef",
    {
        "AggressiveMode": int,
        "PostTemporalSharpening": NoiseFilterPostTemporalSharpening,
        "Speed": int,
        "Strength": int,
    },
    total=False,
)

NoiseReducerTypeDef = TypedDict(
    "NoiseReducerTypeDef",
    {
        "Filter": NoiseReducerFilter,
        "FilterSettings": "NoiseReducerFilterSettingsTypeDef",
        "SpatialFilterSettings": "NoiseReducerSpatialFilterSettingsTypeDef",
        "TemporalFilterSettings": "NoiseReducerTemporalFilterSettingsTypeDef",
    },
    total=False,
)

OpusSettingsTypeDef = TypedDict(
    "OpusSettingsTypeDef", {"Bitrate": int, "Channels": int, "SampleRate": int}, total=False
)

OutputChannelMappingTypeDef = TypedDict(
    "OutputChannelMappingTypeDef",
    {"InputChannels": List[int], "InputChannelsFineTune": List[float]},
    total=False,
)

OutputDetailTypeDef = TypedDict(
    "OutputDetailTypeDef", {"DurationInMs": int, "VideoDetails": "VideoDetailTypeDef"}, total=False
)

OutputGroupDetailTypeDef = TypedDict(
    "OutputGroupDetailTypeDef", {"OutputDetails": List["OutputDetailTypeDef"]}, total=False
)

OutputGroupSettingsTypeDef = TypedDict(
    "OutputGroupSettingsTypeDef",
    {
        "CmafGroupSettings": "CmafGroupSettingsTypeDef",
        "DashIsoGroupSettings": "DashIsoGroupSettingsTypeDef",
        "FileGroupSettings": "FileGroupSettingsTypeDef",
        "HlsGroupSettings": "HlsGroupSettingsTypeDef",
        "MsSmoothGroupSettings": "MsSmoothGroupSettingsTypeDef",
        "Type": OutputGroupType,
    },
    total=False,
)

OutputGroupTypeDef = TypedDict(
    "OutputGroupTypeDef",
    {
        "AutomatedEncodingSettings": "AutomatedEncodingSettingsTypeDef",
        "CustomName": str,
        "Name": str,
        "OutputGroupSettings": "OutputGroupSettingsTypeDef",
        "Outputs": List["OutputTypeDef"],
    },
    total=False,
)

OutputSettingsTypeDef = TypedDict(
    "OutputSettingsTypeDef", {"HlsSettings": "HlsSettingsTypeDef"}, total=False
)

OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "AudioDescriptions": List["AudioDescriptionTypeDef"],
        "CaptionDescriptions": List["CaptionDescriptionTypeDef"],
        "ContainerSettings": "ContainerSettingsTypeDef",
        "Extension": str,
        "NameModifier": str,
        "OutputSettings": "OutputSettingsTypeDef",
        "Preset": str,
        "VideoDescription": "VideoDescriptionTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

PartnerWatermarkingTypeDef = TypedDict(
    "PartnerWatermarkingTypeDef",
    {"NexguardFileMarkerSettings": "NexGuardFileMarkerSettingsTypeDef"},
    total=False,
)

PresetSettingsTypeDef = TypedDict(
    "PresetSettingsTypeDef",
    {
        "AudioDescriptions": List["AudioDescriptionTypeDef"],
        "CaptionDescriptions": List["CaptionDescriptionPresetTypeDef"],
        "ContainerSettings": "ContainerSettingsTypeDef",
        "VideoDescription": "VideoDescriptionTypeDef",
    },
    total=False,
)

_RequiredPresetTypeDef = TypedDict(
    "_RequiredPresetTypeDef", {"Name": str, "Settings": "PresetSettingsTypeDef"}
)
_OptionalPresetTypeDef = TypedDict(
    "_OptionalPresetTypeDef",
    {
        "Arn": str,
        "Category": str,
        "CreatedAt": datetime,
        "Description": str,
        "LastUpdated": datetime,
        "Type": TypeType,
    },
    total=False,
)


class PresetTypeDef(_RequiredPresetTypeDef, _OptionalPresetTypeDef):
    pass


ProresSettingsTypeDef = TypedDict(
    "ProresSettingsTypeDef",
    {
        "CodecProfile": ProresCodecProfile,
        "FramerateControl": ProresFramerateControl,
        "FramerateConversionAlgorithm": ProresFramerateConversionAlgorithm,
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "InterlaceMode": ProresInterlaceMode,
        "ParControl": ProresParControl,
        "ParDenominator": int,
        "ParNumerator": int,
        "ScanTypeConversionMode": ProresScanTypeConversionMode,
        "SlowPal": ProresSlowPal,
        "Telecine": ProresTelecine,
    },
    total=False,
)

QueueTransitionTypeDef = TypedDict(
    "QueueTransitionTypeDef",
    {"DestinationQueue": str, "SourceQueue": str, "Timestamp": datetime},
    total=False,
)

_RequiredQueueTypeDef = TypedDict("_RequiredQueueTypeDef", {"Name": str})
_OptionalQueueTypeDef = TypedDict(
    "_OptionalQueueTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Description": str,
        "LastUpdated": datetime,
        "PricingPlan": PricingPlan,
        "ProgressingJobsCount": int,
        "ReservationPlan": "ReservationPlanTypeDef",
        "Status": QueueStatus,
        "SubmittedJobsCount": int,
        "Type": TypeType,
    },
    total=False,
)


class QueueTypeDef(_RequiredQueueTypeDef, _OptionalQueueTypeDef):
    pass


RectangleTypeDef = TypedDict(
    "RectangleTypeDef", {"Height": int, "Width": int, "X": int, "Y": int}, total=False
)

RemixSettingsTypeDef = TypedDict(
    "RemixSettingsTypeDef",
    {"ChannelMapping": "ChannelMappingTypeDef", "ChannelsIn": int, "ChannelsOut": int},
    total=False,
)

ReservationPlanTypeDef = TypedDict(
    "ReservationPlanTypeDef",
    {
        "Commitment": Commitment,
        "ExpiresAt": datetime,
        "PurchasedAt": datetime,
        "RenewalType": RenewalType,
        "ReservedSlots": int,
        "Status": ReservationPlanStatus,
    },
    total=False,
)

ResourceTagsTypeDef = TypedDict(
    "ResourceTagsTypeDef", {"Arn": str, "Tags": Dict[str, str]}, total=False
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

S3DestinationAccessControlTypeDef = TypedDict(
    "S3DestinationAccessControlTypeDef", {"CannedAcl": S3ObjectCannedAcl}, total=False
)

S3DestinationSettingsTypeDef = TypedDict(
    "S3DestinationSettingsTypeDef",
    {
        "AccessControl": "S3DestinationAccessControlTypeDef",
        "Encryption": "S3EncryptionSettingsTypeDef",
    },
    total=False,
)

S3EncryptionSettingsTypeDef = TypedDict(
    "S3EncryptionSettingsTypeDef",
    {"EncryptionType": S3ServerSideEncryptionType, "KmsKeyArn": str},
    total=False,
)

SccDestinationSettingsTypeDef = TypedDict(
    "SccDestinationSettingsTypeDef", {"Framerate": SccDestinationFramerate}, total=False
)

SpekeKeyProviderCmafTypeDef = TypedDict(
    "SpekeKeyProviderCmafTypeDef",
    {
        "CertificateArn": str,
        "DashSignaledSystemIds": List[str],
        "HlsSignaledSystemIds": List[str],
        "ResourceId": str,
        "Url": str,
    },
    total=False,
)

SpekeKeyProviderTypeDef = TypedDict(
    "SpekeKeyProviderTypeDef",
    {"CertificateArn": str, "ResourceId": str, "SystemIds": List[str], "Url": str},
    total=False,
)

StaticKeyProviderTypeDef = TypedDict(
    "StaticKeyProviderTypeDef",
    {"KeyFormat": str, "KeyFormatVersions": str, "StaticKeyValue": str, "Url": str},
    total=False,
)

TeletextDestinationSettingsTypeDef = TypedDict(
    "TeletextDestinationSettingsTypeDef",
    {"PageNumber": str, "PageTypes": List[TeletextPageType]},
    total=False,
)

TeletextSourceSettingsTypeDef = TypedDict(
    "TeletextSourceSettingsTypeDef", {"PageNumber": str}, total=False
)

TimecodeBurninTypeDef = TypedDict(
    "TimecodeBurninTypeDef",
    {"FontSize": int, "Position": TimecodeBurninPosition, "Prefix": str},
    total=False,
)

TimecodeConfigTypeDef = TypedDict(
    "TimecodeConfigTypeDef",
    {"Anchor": str, "Source": TimecodeSource, "Start": str, "TimestampOffset": str},
    total=False,
)

TimedMetadataInsertionTypeDef = TypedDict(
    "TimedMetadataInsertionTypeDef", {"Id3Insertions": List["Id3InsertionTypeDef"]}, total=False
)

TimingTypeDef = TypedDict(
    "TimingTypeDef",
    {"FinishTime": datetime, "StartTime": datetime, "SubmitTime": datetime},
    total=False,
)

TrackSourceSettingsTypeDef = TypedDict(
    "TrackSourceSettingsTypeDef", {"TrackNumber": int}, total=False
)

TtmlDestinationSettingsTypeDef = TypedDict(
    "TtmlDestinationSettingsTypeDef", {"StylePassthrough": TtmlStylePassthrough}, total=False
)

Vc3SettingsTypeDef = TypedDict(
    "Vc3SettingsTypeDef",
    {
        "FramerateControl": Vc3FramerateControl,
        "FramerateConversionAlgorithm": Vc3FramerateConversionAlgorithm,
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "InterlaceMode": Vc3InterlaceMode,
        "ScanTypeConversionMode": Vc3ScanTypeConversionMode,
        "SlowPal": Vc3SlowPal,
        "Telecine": Vc3Telecine,
        "Vc3Class": Vc3Class,
    },
    total=False,
)

VideoCodecSettingsTypeDef = TypedDict(
    "VideoCodecSettingsTypeDef",
    {
        "Av1Settings": "Av1SettingsTypeDef",
        "AvcIntraSettings": "AvcIntraSettingsTypeDef",
        "Codec": VideoCodec,
        "FrameCaptureSettings": "FrameCaptureSettingsTypeDef",
        "H264Settings": "H264SettingsTypeDef",
        "H265Settings": "H265SettingsTypeDef",
        "Mpeg2Settings": "Mpeg2SettingsTypeDef",
        "ProresSettings": "ProresSettingsTypeDef",
        "Vc3Settings": "Vc3SettingsTypeDef",
        "Vp8Settings": "Vp8SettingsTypeDef",
        "Vp9Settings": "Vp9SettingsTypeDef",
    },
    total=False,
)

VideoDescriptionTypeDef = TypedDict(
    "VideoDescriptionTypeDef",
    {
        "AfdSignaling": AfdSignaling,
        "AntiAlias": AntiAlias,
        "CodecSettings": "VideoCodecSettingsTypeDef",
        "ColorMetadata": ColorMetadata,
        "Crop": "RectangleTypeDef",
        "DropFrameTimecode": DropFrameTimecode,
        "FixedAfd": int,
        "Height": int,
        "Position": "RectangleTypeDef",
        "RespondToAfd": RespondToAfd,
        "ScalingBehavior": ScalingBehavior,
        "Sharpness": int,
        "TimecodeInsertion": VideoTimecodeInsertion,
        "VideoPreprocessors": "VideoPreprocessorTypeDef",
        "Width": int,
    },
    total=False,
)

VideoDetailTypeDef = TypedDict(
    "VideoDetailTypeDef", {"HeightInPx": int, "WidthInPx": int}, total=False
)

VideoPreprocessorTypeDef = TypedDict(
    "VideoPreprocessorTypeDef",
    {
        "ColorCorrector": "ColorCorrectorTypeDef",
        "Deinterlacer": "DeinterlacerTypeDef",
        "DolbyVision": "DolbyVisionTypeDef",
        "ImageInserter": "ImageInserterTypeDef",
        "NoiseReducer": "NoiseReducerTypeDef",
        "PartnerWatermarking": "PartnerWatermarkingTypeDef",
        "TimecodeBurnin": "TimecodeBurninTypeDef",
    },
    total=False,
)

VideoSelectorTypeDef = TypedDict(
    "VideoSelectorTypeDef",
    {
        "AlphaBehavior": AlphaBehavior,
        "ColorSpace": ColorSpace,
        "ColorSpaceUsage": ColorSpaceUsage,
        "Hdr10Metadata": "Hdr10MetadataTypeDef",
        "Pid": int,
        "ProgramNumber": int,
        "Rotate": InputRotate,
    },
    total=False,
)

VorbisSettingsTypeDef = TypedDict(
    "VorbisSettingsTypeDef", {"Channels": int, "SampleRate": int, "VbrQuality": int}, total=False
)

Vp8SettingsTypeDef = TypedDict(
    "Vp8SettingsTypeDef",
    {
        "Bitrate": int,
        "FramerateControl": Vp8FramerateControl,
        "FramerateConversionAlgorithm": Vp8FramerateConversionAlgorithm,
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "GopSize": float,
        "HrdBufferSize": int,
        "MaxBitrate": int,
        "ParControl": Vp8ParControl,
        "ParDenominator": int,
        "ParNumerator": int,
        "QualityTuningLevel": Vp8QualityTuningLevel,
        "RateControlMode": Vp8RateControlMode,
    },
    total=False,
)

Vp9SettingsTypeDef = TypedDict(
    "Vp9SettingsTypeDef",
    {
        "Bitrate": int,
        "FramerateControl": Vp9FramerateControl,
        "FramerateConversionAlgorithm": Vp9FramerateConversionAlgorithm,
        "FramerateDenominator": int,
        "FramerateNumerator": int,
        "GopSize": float,
        "HrdBufferSize": int,
        "MaxBitrate": int,
        "ParControl": Vp9ParControl,
        "ParDenominator": int,
        "ParNumerator": int,
        "QualityTuningLevel": Vp9QualityTuningLevel,
        "RateControlMode": Vp9RateControlMode,
    },
    total=False,
)

WavSettingsTypeDef = TypedDict(
    "WavSettingsTypeDef",
    {"BitDepth": int, "Channels": int, "Format": WavFormat, "SampleRate": int},
    total=False,
)

WebvttDestinationSettingsTypeDef = TypedDict(
    "WebvttDestinationSettingsTypeDef", {"StylePassthrough": WebvttStylePassthrough}, total=False
)

CreateJobResponseTypeDef = TypedDict("CreateJobResponseTypeDef", {"Job": "JobTypeDef"}, total=False)

CreateJobTemplateResponseTypeDef = TypedDict(
    "CreateJobTemplateResponseTypeDef", {"JobTemplate": "JobTemplateTypeDef"}, total=False
)

CreatePresetResponseTypeDef = TypedDict(
    "CreatePresetResponseTypeDef", {"Preset": "PresetTypeDef"}, total=False
)

CreateQueueResponseTypeDef = TypedDict(
    "CreateQueueResponseTypeDef", {"Queue": "QueueTypeDef"}, total=False
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef",
    {"Endpoints": List["EndpointTypeDef"], "NextToken": str},
    total=False,
)

GetJobResponseTypeDef = TypedDict("GetJobResponseTypeDef", {"Job": "JobTypeDef"}, total=False)

GetJobTemplateResponseTypeDef = TypedDict(
    "GetJobTemplateResponseTypeDef", {"JobTemplate": "JobTemplateTypeDef"}, total=False
)

GetPresetResponseTypeDef = TypedDict(
    "GetPresetResponseTypeDef", {"Preset": "PresetTypeDef"}, total=False
)

GetQueueResponseTypeDef = TypedDict(
    "GetQueueResponseTypeDef", {"Queue": "QueueTypeDef"}, total=False
)

ListJobTemplatesResponseTypeDef = TypedDict(
    "ListJobTemplatesResponseTypeDef",
    {"JobTemplates": List["JobTemplateTypeDef"], "NextToken": str},
    total=False,
)

ListJobsResponseTypeDef = TypedDict(
    "ListJobsResponseTypeDef", {"Jobs": List["JobTypeDef"], "NextToken": str}, total=False
)

ListPresetsResponseTypeDef = TypedDict(
    "ListPresetsResponseTypeDef", {"NextToken": str, "Presets": List["PresetTypeDef"]}, total=False
)

ListQueuesResponseTypeDef = TypedDict(
    "ListQueuesResponseTypeDef", {"NextToken": str, "Queues": List["QueueTypeDef"]}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"ResourceTags": "ResourceTagsTypeDef"}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ReservationPlanSettingsTypeDef = TypedDict(
    "ReservationPlanSettingsTypeDef",
    {"Commitment": Commitment, "RenewalType": RenewalType, "ReservedSlots": int},
)

UpdateJobTemplateResponseTypeDef = TypedDict(
    "UpdateJobTemplateResponseTypeDef", {"JobTemplate": "JobTemplateTypeDef"}, total=False
)

UpdatePresetResponseTypeDef = TypedDict(
    "UpdatePresetResponseTypeDef", {"Preset": "PresetTypeDef"}, total=False
)

UpdateQueueResponseTypeDef = TypedDict(
    "UpdateQueueResponseTypeDef", {"Queue": "QueueTypeDef"}, total=False
)
