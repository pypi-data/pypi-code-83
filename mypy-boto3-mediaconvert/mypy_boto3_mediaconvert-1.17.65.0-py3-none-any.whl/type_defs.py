"""
Type annotations for mediaconvert service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediaconvert/type_defs.html)

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
    DropFrameTimecode,
    DvbSubtitleAlignment,
    DvbSubtitleBackgroundColor,
    DvbSubtitleFontColor,
    DvbSubtitleOutlineColor,
    DvbSubtitleShadowColor,
    DvbSubtitleTeletextSpacing,
    DvbSubtitlingType,
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
    Vp9FramerateControl,
    Vp9FramerateConversionAlgorithm,
    Vp9ParControl,
    Vp9QualityTuningLevel,
    WatermarkingStrength,
    WavFormat,
    WebvttStylePassthrough,
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
    "CreateJobResponseTypeDef",
    "CreateJobTemplateResponseTypeDef",
    "CreatePresetResponseTypeDef",
    "CreateQueueResponseTypeDef",
    "DashAdditionalManifestTypeDef",
    "DashIsoEncryptionSettingsTypeDef",
    "DashIsoGroupSettingsTypeDef",
    "DeinterlacerTypeDef",
    "DescribeEndpointsResponseTypeDef",
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
    "GetJobResponseTypeDef",
    "GetJobTemplateResponseTypeDef",
    "GetPresetResponseTypeDef",
    "GetQueueResponseTypeDef",
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
    "ListJobTemplatesResponseTypeDef",
    "ListJobsResponseTypeDef",
    "ListPresetsResponseTypeDef",
    "ListQueuesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
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
    "PaginatorConfigTypeDef",
    "PartnerWatermarkingTypeDef",
    "PresetSettingsTypeDef",
    "PresetTypeDef",
    "ProresSettingsTypeDef",
    "QueueTransitionTypeDef",
    "QueueTypeDef",
    "RectangleTypeDef",
    "RemixSettingsTypeDef",
    "ReservationPlanSettingsTypeDef",
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
    "UpdateJobTemplateResponseTypeDef",
    "UpdatePresetResponseTypeDef",
    "UpdateQueueResponseTypeDef",
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
)


class AacSettingsTypeDef(TypedDict, total=False):
    AudioDescriptionBroadcasterMix: AacAudioDescriptionBroadcasterMix
    Bitrate: int
    CodecProfile: AacCodecProfile
    CodingMode: AacCodingMode
    RateControlMode: AacRateControlMode
    RawFormat: AacRawFormat
    SampleRate: int
    Specification: AacSpecification
    VbrQuality: AacVbrQuality


class Ac3SettingsTypeDef(TypedDict, total=False):
    Bitrate: int
    BitstreamMode: Ac3BitstreamMode
    CodingMode: Ac3CodingMode
    Dialnorm: int
    DynamicRangeCompressionLine: Ac3DynamicRangeCompressionLine
    DynamicRangeCompressionProfile: Ac3DynamicRangeCompressionProfile
    DynamicRangeCompressionRf: Ac3DynamicRangeCompressionRf
    LfeFilter: Ac3LfeFilter
    MetadataControl: Ac3MetadataControl
    SampleRate: int


class AccelerationSettingsTypeDef(TypedDict):
    Mode: AccelerationMode


class AiffSettingsTypeDef(TypedDict, total=False):
    BitDepth: int
    Channels: int
    SampleRate: int


class AncillarySourceSettingsTypeDef(TypedDict, total=False):
    Convert608To708: AncillaryConvert608To708
    SourceAncillaryChannelNumber: int
    TerminateCaptions: AncillaryTerminateCaptions


class AudioChannelTaggingSettingsTypeDef(TypedDict, total=False):
    ChannelTag: AudioChannelTag


class AudioCodecSettingsTypeDef(TypedDict, total=False):
    AacSettings: "AacSettingsTypeDef"
    Ac3Settings: "Ac3SettingsTypeDef"
    AiffSettings: "AiffSettingsTypeDef"
    Codec: AudioCodec
    Eac3AtmosSettings: "Eac3AtmosSettingsTypeDef"
    Eac3Settings: "Eac3SettingsTypeDef"
    Mp2Settings: "Mp2SettingsTypeDef"
    Mp3Settings: "Mp3SettingsTypeDef"
    OpusSettings: "OpusSettingsTypeDef"
    VorbisSettings: "VorbisSettingsTypeDef"
    WavSettings: "WavSettingsTypeDef"


class AudioDescriptionTypeDef(TypedDict, total=False):
    AudioChannelTaggingSettings: "AudioChannelTaggingSettingsTypeDef"
    AudioNormalizationSettings: "AudioNormalizationSettingsTypeDef"
    AudioSourceName: str
    AudioType: int
    AudioTypeControl: AudioTypeControl
    CodecSettings: "AudioCodecSettingsTypeDef"
    CustomLanguageCode: str
    LanguageCode: LanguageCode
    LanguageCodeControl: AudioLanguageCodeControl
    RemixSettings: "RemixSettingsTypeDef"
    StreamName: str


class AudioNormalizationSettingsTypeDef(TypedDict, total=False):
    Algorithm: AudioNormalizationAlgorithm
    AlgorithmControl: AudioNormalizationAlgorithmControl
    CorrectionGateLevel: int
    LoudnessLogging: AudioNormalizationLoudnessLogging
    PeakCalculation: AudioNormalizationPeakCalculation
    TargetLkfs: float


class AudioSelectorGroupTypeDef(TypedDict, total=False):
    AudioSelectorNames: List[str]


class AudioSelectorTypeDef(TypedDict, total=False):
    CustomLanguageCode: str
    DefaultSelection: AudioDefaultSelection
    ExternalAudioFileInput: str
    LanguageCode: LanguageCode
    Offset: int
    Pids: List[int]
    ProgramSelection: int
    RemixSettings: "RemixSettingsTypeDef"
    SelectorType: AudioSelectorType
    Tracks: List[int]


class AutomatedAbrSettingsTypeDef(TypedDict, total=False):
    MaxAbrBitrate: int
    MaxRenditions: int
    MinAbrBitrate: int


class AutomatedEncodingSettingsTypeDef(TypedDict, total=False):
    AbrSettings: "AutomatedAbrSettingsTypeDef"


class Av1QvbrSettingsTypeDef(TypedDict, total=False):
    QvbrQualityLevel: int
    QvbrQualityLevelFineTune: float


class Av1SettingsTypeDef(TypedDict, total=False):
    AdaptiveQuantization: Av1AdaptiveQuantization
    FramerateControl: Av1FramerateControl
    FramerateConversionAlgorithm: Av1FramerateConversionAlgorithm
    FramerateDenominator: int
    FramerateNumerator: int
    GopSize: float
    MaxBitrate: int
    NumberBFramesBetweenReferenceFrames: int
    QvbrSettings: "Av1QvbrSettingsTypeDef"
    RateControlMode: Literal["QVBR"]
    Slices: int
    SpatialAdaptiveQuantization: Av1SpatialAdaptiveQuantization


class AvailBlankingTypeDef(TypedDict, total=False):
    AvailBlankingImage: str


class AvcIntraSettingsTypeDef(TypedDict, total=False):
    AvcIntraClass: AvcIntraClass
    AvcIntraUhdSettings: "AvcIntraUhdSettingsTypeDef"
    FramerateControl: AvcIntraFramerateControl
    FramerateConversionAlgorithm: AvcIntraFramerateConversionAlgorithm
    FramerateDenominator: int
    FramerateNumerator: int
    InterlaceMode: AvcIntraInterlaceMode
    ScanTypeConversionMode: AvcIntraScanTypeConversionMode
    SlowPal: AvcIntraSlowPal
    Telecine: AvcIntraTelecine


class AvcIntraUhdSettingsTypeDef(TypedDict, total=False):
    QualityTuningLevel: AvcIntraUhdQualityTuningLevel


class BurninDestinationSettingsTypeDef(TypedDict, total=False):
    Alignment: BurninSubtitleAlignment
    BackgroundColor: BurninSubtitleBackgroundColor
    BackgroundOpacity: int
    FontColor: BurninSubtitleFontColor
    FontOpacity: int
    FontResolution: int
    FontScript: FontScript
    FontSize: int
    OutlineColor: BurninSubtitleOutlineColor
    OutlineSize: int
    ShadowColor: BurninSubtitleShadowColor
    ShadowOpacity: int
    ShadowXOffset: int
    ShadowYOffset: int
    TeletextSpacing: BurninSubtitleTeletextSpacing
    XPosition: int
    YPosition: int


class CaptionDescriptionPresetTypeDef(TypedDict, total=False):
    CustomLanguageCode: str
    DestinationSettings: "CaptionDestinationSettingsTypeDef"
    LanguageCode: LanguageCode
    LanguageDescription: str


class CaptionDescriptionTypeDef(TypedDict, total=False):
    CaptionSelectorName: str
    CustomLanguageCode: str
    DestinationSettings: "CaptionDestinationSettingsTypeDef"
    LanguageCode: LanguageCode
    LanguageDescription: str


class CaptionDestinationSettingsTypeDef(TypedDict, total=False):
    BurninDestinationSettings: "BurninDestinationSettingsTypeDef"
    DestinationType: CaptionDestinationType
    DvbSubDestinationSettings: "DvbSubDestinationSettingsTypeDef"
    EmbeddedDestinationSettings: "EmbeddedDestinationSettingsTypeDef"
    ImscDestinationSettings: "ImscDestinationSettingsTypeDef"
    SccDestinationSettings: "SccDestinationSettingsTypeDef"
    TeletextDestinationSettings: "TeletextDestinationSettingsTypeDef"
    TtmlDestinationSettings: "TtmlDestinationSettingsTypeDef"
    WebvttDestinationSettings: "WebvttDestinationSettingsTypeDef"


class CaptionSelectorTypeDef(TypedDict, total=False):
    CustomLanguageCode: str
    LanguageCode: LanguageCode
    SourceSettings: "CaptionSourceSettingsTypeDef"


class CaptionSourceFramerateTypeDef(TypedDict, total=False):
    FramerateDenominator: int
    FramerateNumerator: int


class CaptionSourceSettingsTypeDef(TypedDict, total=False):
    AncillarySourceSettings: "AncillarySourceSettingsTypeDef"
    DvbSubSourceSettings: "DvbSubSourceSettingsTypeDef"
    EmbeddedSourceSettings: "EmbeddedSourceSettingsTypeDef"
    FileSourceSettings: "FileSourceSettingsTypeDef"
    SourceType: CaptionSourceType
    TeletextSourceSettings: "TeletextSourceSettingsTypeDef"
    TrackSourceSettings: "TrackSourceSettingsTypeDef"


class ChannelMappingTypeDef(TypedDict, total=False):
    OutputChannels: List["OutputChannelMappingTypeDef"]


class CmafAdditionalManifestTypeDef(TypedDict, total=False):
    ManifestNameModifier: str
    SelectedOutputs: List[str]


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


class CmafGroupSettingsTypeDef(TypedDict, total=False):
    AdditionalManifests: List["CmafAdditionalManifestTypeDef"]
    BaseUrl: str
    ClientCache: CmafClientCache
    CodecSpecification: CmafCodecSpecification
    Destination: str
    DestinationSettings: "DestinationSettingsTypeDef"
    Encryption: "CmafEncryptionSettingsTypeDef"
    FragmentLength: int
    ManifestCompression: CmafManifestCompression
    ManifestDurationFormat: CmafManifestDurationFormat
    MinBufferTime: int
    MinFinalSegmentLength: float
    MpdProfile: CmafMpdProfile
    PtsOffsetHandlingForBFrames: CmafPtsOffsetHandlingForBFrames
    SegmentControl: CmafSegmentControl
    SegmentLength: int
    StreamInfResolution: CmafStreamInfResolution
    WriteDashManifest: CmafWriteDASHManifest
    WriteHlsManifest: CmafWriteHLSManifest
    WriteSegmentTimelineInRepresentation: CmafWriteSegmentTimelineInRepresentation


class CmfcSettingsTypeDef(TypedDict, total=False):
    AudioDuration: CmfcAudioDuration
    AudioGroupId: str
    AudioRenditionSets: str
    AudioTrackType: CmfcAudioTrackType
    DescriptiveVideoServiceFlag: CmfcDescriptiveVideoServiceFlag
    IFrameOnlyManifest: CmfcIFrameOnlyManifest
    Scte35Esam: CmfcScte35Esam
    Scte35Source: CmfcScte35Source


class ColorCorrectorTypeDef(TypedDict, total=False):
    Brightness: int
    ColorSpaceConversion: ColorSpaceConversion
    Contrast: int
    Hdr10Metadata: "Hdr10MetadataTypeDef"
    Hue: int
    Saturation: int


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


class CreateJobResponseTypeDef(TypedDict, total=False):
    Job: "JobTypeDef"


class CreateJobTemplateResponseTypeDef(TypedDict, total=False):
    JobTemplate: "JobTemplateTypeDef"


class CreatePresetResponseTypeDef(TypedDict, total=False):
    Preset: "PresetTypeDef"


class CreateQueueResponseTypeDef(TypedDict, total=False):
    Queue: "QueueTypeDef"


class DashAdditionalManifestTypeDef(TypedDict, total=False):
    ManifestNameModifier: str
    SelectedOutputs: List[str]


class DashIsoEncryptionSettingsTypeDef(TypedDict, total=False):
    PlaybackDeviceCompatibility: DashIsoPlaybackDeviceCompatibility
    SpekeKeyProvider: "SpekeKeyProviderTypeDef"


class DashIsoGroupSettingsTypeDef(TypedDict, total=False):
    AdditionalManifests: List["DashAdditionalManifestTypeDef"]
    AudioChannelConfigSchemeIdUri: DashIsoGroupAudioChannelConfigSchemeIdUri
    BaseUrl: str
    Destination: str
    DestinationSettings: "DestinationSettingsTypeDef"
    Encryption: "DashIsoEncryptionSettingsTypeDef"
    FragmentLength: int
    HbbtvCompliance: DashIsoHbbtvCompliance
    MinBufferTime: int
    MinFinalSegmentLength: float
    MpdProfile: DashIsoMpdProfile
    PtsOffsetHandlingForBFrames: DashIsoPtsOffsetHandlingForBFrames
    SegmentControl: DashIsoSegmentControl
    SegmentLength: int
    WriteSegmentTimelineInRepresentation: DashIsoWriteSegmentTimelineInRepresentation


class DeinterlacerTypeDef(TypedDict, total=False):
    Algorithm: DeinterlaceAlgorithm
    Control: DeinterlacerControl
    Mode: DeinterlacerMode


class DescribeEndpointsResponseTypeDef(TypedDict, total=False):
    Endpoints: List["EndpointTypeDef"]
    NextToken: str


class DestinationSettingsTypeDef(TypedDict, total=False):
    S3Settings: "S3DestinationSettingsTypeDef"


class DolbyVisionLevel6MetadataTypeDef(TypedDict, total=False):
    MaxCll: int
    MaxFall: int


class DolbyVisionTypeDef(TypedDict, total=False):
    L6Metadata: "DolbyVisionLevel6MetadataTypeDef"
    L6Mode: DolbyVisionLevel6Mode
    Profile: Literal["PROFILE_5"]


class DvbNitSettingsTypeDef(TypedDict, total=False):
    NetworkId: int
    NetworkName: str
    NitInterval: int


class DvbSdtSettingsTypeDef(TypedDict, total=False):
    OutputSdt: OutputSdt
    SdtInterval: int
    ServiceName: str
    ServiceProviderName: str


class DvbSubDestinationSettingsTypeDef(TypedDict, total=False):
    Alignment: DvbSubtitleAlignment
    BackgroundColor: DvbSubtitleBackgroundColor
    BackgroundOpacity: int
    FontColor: DvbSubtitleFontColor
    FontOpacity: int
    FontResolution: int
    FontScript: FontScript
    FontSize: int
    OutlineColor: DvbSubtitleOutlineColor
    OutlineSize: int
    ShadowColor: DvbSubtitleShadowColor
    ShadowOpacity: int
    ShadowXOffset: int
    ShadowYOffset: int
    SubtitlingType: DvbSubtitlingType
    TeletextSpacing: DvbSubtitleTeletextSpacing
    XPosition: int
    YPosition: int


class DvbSubSourceSettingsTypeDef(TypedDict, total=False):
    Pid: int


class DvbTdtSettingsTypeDef(TypedDict, total=False):
    TdtInterval: int


class Eac3AtmosSettingsTypeDef(TypedDict, total=False):
    Bitrate: int
    BitstreamMode: Literal["COMPLETE_MAIN"]
    CodingMode: Literal["CODING_MODE_9_1_6"]
    DialogueIntelligence: Eac3AtmosDialogueIntelligence
    DynamicRangeCompressionLine: Eac3AtmosDynamicRangeCompressionLine
    DynamicRangeCompressionRf: Eac3AtmosDynamicRangeCompressionRf
    LoRoCenterMixLevel: float
    LoRoSurroundMixLevel: float
    LtRtCenterMixLevel: float
    LtRtSurroundMixLevel: float
    MeteringMode: Eac3AtmosMeteringMode
    SampleRate: int
    SpeechThreshold: int
    StereoDownmix: Eac3AtmosStereoDownmix
    SurroundExMode: Eac3AtmosSurroundExMode


class Eac3SettingsTypeDef(TypedDict, total=False):
    AttenuationControl: Eac3AttenuationControl
    Bitrate: int
    BitstreamMode: Eac3BitstreamMode
    CodingMode: Eac3CodingMode
    DcFilter: Eac3DcFilter
    Dialnorm: int
    DynamicRangeCompressionLine: Eac3DynamicRangeCompressionLine
    DynamicRangeCompressionRf: Eac3DynamicRangeCompressionRf
    LfeControl: Eac3LfeControl
    LfeFilter: Eac3LfeFilter
    LoRoCenterMixLevel: float
    LoRoSurroundMixLevel: float
    LtRtCenterMixLevel: float
    LtRtSurroundMixLevel: float
    MetadataControl: Eac3MetadataControl
    PassthroughControl: Eac3PassthroughControl
    PhaseControl: Eac3PhaseControl
    SampleRate: int
    StereoDownmix: Eac3StereoDownmix
    SurroundExMode: Eac3SurroundExMode
    SurroundMode: Eac3SurroundMode


class EmbeddedDestinationSettingsTypeDef(TypedDict, total=False):
    Destination608ChannelNumber: int
    Destination708ServiceNumber: int


class EmbeddedSourceSettingsTypeDef(TypedDict, total=False):
    Convert608To708: EmbeddedConvert608To708
    Source608ChannelNumber: int
    Source608TrackNumber: int
    TerminateCaptions: EmbeddedTerminateCaptions


class EndpointTypeDef(TypedDict, total=False):
    Url: str


class EsamManifestConfirmConditionNotificationTypeDef(TypedDict, total=False):
    MccXml: str


class EsamSettingsTypeDef(TypedDict, total=False):
    ManifestConfirmConditionNotification: "EsamManifestConfirmConditionNotificationTypeDef"
    ResponseSignalPreroll: int
    SignalProcessingNotification: "EsamSignalProcessingNotificationTypeDef"


class EsamSignalProcessingNotificationTypeDef(TypedDict, total=False):
    SccXml: str


class F4vSettingsTypeDef(TypedDict, total=False):
    MoovPlacement: F4vMoovPlacement


class FileGroupSettingsTypeDef(TypedDict, total=False):
    Destination: str
    DestinationSettings: "DestinationSettingsTypeDef"


class FileSourceSettingsTypeDef(TypedDict, total=False):
    Convert608To708: FileSourceConvert608To708
    Framerate: "CaptionSourceFramerateTypeDef"
    SourceFile: str
    TimeDelta: int


class FrameCaptureSettingsTypeDef(TypedDict, total=False):
    FramerateDenominator: int
    FramerateNumerator: int
    MaxCaptures: int
    Quality: int


class GetJobResponseTypeDef(TypedDict, total=False):
    Job: "JobTypeDef"


class GetJobTemplateResponseTypeDef(TypedDict, total=False):
    JobTemplate: "JobTemplateTypeDef"


class GetPresetResponseTypeDef(TypedDict, total=False):
    Preset: "PresetTypeDef"


class GetQueueResponseTypeDef(TypedDict, total=False):
    Queue: "QueueTypeDef"


class H264QvbrSettingsTypeDef(TypedDict, total=False):
    MaxAverageBitrate: int
    QvbrQualityLevel: int
    QvbrQualityLevelFineTune: float


class H264SettingsTypeDef(TypedDict, total=False):
    AdaptiveQuantization: H264AdaptiveQuantization
    Bitrate: int
    CodecLevel: H264CodecLevel
    CodecProfile: H264CodecProfile
    DynamicSubGop: H264DynamicSubGop
    EntropyEncoding: H264EntropyEncoding
    FieldEncoding: H264FieldEncoding
    FlickerAdaptiveQuantization: H264FlickerAdaptiveQuantization
    FramerateControl: H264FramerateControl
    FramerateConversionAlgorithm: H264FramerateConversionAlgorithm
    FramerateDenominator: int
    FramerateNumerator: int
    GopBReference: H264GopBReference
    GopClosedCadence: int
    GopSize: float
    GopSizeUnits: H264GopSizeUnits
    HrdBufferInitialFillPercentage: int
    HrdBufferSize: int
    InterlaceMode: H264InterlaceMode
    MaxBitrate: int
    MinIInterval: int
    NumberBFramesBetweenReferenceFrames: int
    NumberReferenceFrames: int
    ParControl: H264ParControl
    ParDenominator: int
    ParNumerator: int
    QualityTuningLevel: H264QualityTuningLevel
    QvbrSettings: "H264QvbrSettingsTypeDef"
    RateControlMode: H264RateControlMode
    RepeatPps: H264RepeatPps
    ScanTypeConversionMode: H264ScanTypeConversionMode
    SceneChangeDetect: H264SceneChangeDetect
    Slices: int
    SlowPal: H264SlowPal
    Softness: int
    SpatialAdaptiveQuantization: H264SpatialAdaptiveQuantization
    Syntax: H264Syntax
    Telecine: H264Telecine
    TemporalAdaptiveQuantization: H264TemporalAdaptiveQuantization
    UnregisteredSeiTimecode: H264UnregisteredSeiTimecode


class H265QvbrSettingsTypeDef(TypedDict, total=False):
    MaxAverageBitrate: int
    QvbrQualityLevel: int
    QvbrQualityLevelFineTune: float


class H265SettingsTypeDef(TypedDict, total=False):
    AdaptiveQuantization: H265AdaptiveQuantization
    AlternateTransferFunctionSei: H265AlternateTransferFunctionSei
    Bitrate: int
    CodecLevel: H265CodecLevel
    CodecProfile: H265CodecProfile
    DynamicSubGop: H265DynamicSubGop
    FlickerAdaptiveQuantization: H265FlickerAdaptiveQuantization
    FramerateControl: H265FramerateControl
    FramerateConversionAlgorithm: H265FramerateConversionAlgorithm
    FramerateDenominator: int
    FramerateNumerator: int
    GopBReference: H265GopBReference
    GopClosedCadence: int
    GopSize: float
    GopSizeUnits: H265GopSizeUnits
    HrdBufferInitialFillPercentage: int
    HrdBufferSize: int
    InterlaceMode: H265InterlaceMode
    MaxBitrate: int
    MinIInterval: int
    NumberBFramesBetweenReferenceFrames: int
    NumberReferenceFrames: int
    ParControl: H265ParControl
    ParDenominator: int
    ParNumerator: int
    QualityTuningLevel: H265QualityTuningLevel
    QvbrSettings: "H265QvbrSettingsTypeDef"
    RateControlMode: H265RateControlMode
    SampleAdaptiveOffsetFilterMode: H265SampleAdaptiveOffsetFilterMode
    ScanTypeConversionMode: H265ScanTypeConversionMode
    SceneChangeDetect: H265SceneChangeDetect
    Slices: int
    SlowPal: H265SlowPal
    SpatialAdaptiveQuantization: H265SpatialAdaptiveQuantization
    Telecine: H265Telecine
    TemporalAdaptiveQuantization: H265TemporalAdaptiveQuantization
    TemporalIds: H265TemporalIds
    Tiles: H265Tiles
    UnregisteredSeiTimecode: H265UnregisteredSeiTimecode
    WriteMp4PackagingType: H265WriteMp4PackagingType


class Hdr10MetadataTypeDef(TypedDict, total=False):
    BluePrimaryX: int
    BluePrimaryY: int
    GreenPrimaryX: int
    GreenPrimaryY: int
    MaxContentLightLevel: int
    MaxFrameAverageLightLevel: int
    MaxLuminance: int
    MinLuminance: int
    RedPrimaryX: int
    RedPrimaryY: int
    WhitePointX: int
    WhitePointY: int


class HlsAdditionalManifestTypeDef(TypedDict, total=False):
    ManifestNameModifier: str
    SelectedOutputs: List[str]


class HlsCaptionLanguageMappingTypeDef(TypedDict, total=False):
    CaptionChannel: int
    CustomLanguageCode: str
    LanguageCode: LanguageCode
    LanguageDescription: str


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


class HlsGroupSettingsTypeDef(TypedDict, total=False):
    AdMarkers: List[HlsAdMarkers]
    AdditionalManifests: List["HlsAdditionalManifestTypeDef"]
    AudioOnlyHeader: HlsAudioOnlyHeader
    BaseUrl: str
    CaptionLanguageMappings: List["HlsCaptionLanguageMappingTypeDef"]
    CaptionLanguageSetting: HlsCaptionLanguageSetting
    ClientCache: HlsClientCache
    CodecSpecification: HlsCodecSpecification
    Destination: str
    DestinationSettings: "DestinationSettingsTypeDef"
    DirectoryStructure: HlsDirectoryStructure
    Encryption: "HlsEncryptionSettingsTypeDef"
    ManifestCompression: HlsManifestCompression
    ManifestDurationFormat: HlsManifestDurationFormat
    MinFinalSegmentLength: float
    MinSegmentLength: int
    OutputSelection: HlsOutputSelection
    ProgramDateTime: HlsProgramDateTime
    ProgramDateTimePeriod: int
    SegmentControl: HlsSegmentControl
    SegmentLength: int
    SegmentsPerSubdirectory: int
    StreamInfResolution: HlsStreamInfResolution
    TimedMetadataId3Frame: HlsTimedMetadataId3Frame
    TimedMetadataId3Period: int
    TimestampDeltaMilliseconds: int


class HlsSettingsTypeDef(TypedDict, total=False):
    AudioGroupId: str
    AudioOnlyContainer: HlsAudioOnlyContainer
    AudioRenditionSets: str
    AudioTrackType: HlsAudioTrackType
    DescriptiveVideoServiceFlag: HlsDescriptiveVideoServiceFlag
    IFrameOnlyManifest: HlsIFrameOnlyManifest
    SegmentModifier: str


class HopDestinationTypeDef(TypedDict, total=False):
    Priority: int
    Queue: str
    WaitMinutes: int


class Id3InsertionTypeDef(TypedDict, total=False):
    Id3: str
    Timecode: str


class ImageInserterTypeDef(TypedDict, total=False):
    InsertableImages: List["InsertableImageTypeDef"]


class ImscDestinationSettingsTypeDef(TypedDict, total=False):
    StylePassthrough: ImscStylePassthrough


class InputClippingTypeDef(TypedDict, total=False):
    EndTimecode: str
    StartTimecode: str


class InputDecryptionSettingsTypeDef(TypedDict, total=False):
    DecryptionMode: DecryptionMode
    EncryptedDecryptionKey: str
    InitializationVector: str
    KmsKeyRegion: str


class InputTemplateTypeDef(TypedDict, total=False):
    AudioSelectorGroups: Dict[str, "AudioSelectorGroupTypeDef"]
    AudioSelectors: Dict[str, "AudioSelectorTypeDef"]
    CaptionSelectors: Dict[str, "CaptionSelectorTypeDef"]
    Crop: "RectangleTypeDef"
    DeblockFilter: InputDeblockFilter
    DenoiseFilter: InputDenoiseFilter
    FilterEnable: InputFilterEnable
    FilterStrength: int
    ImageInserter: "ImageInserterTypeDef"
    InputClippings: List["InputClippingTypeDef"]
    InputScanType: InputScanType
    Position: "RectangleTypeDef"
    ProgramNumber: int
    PsiControl: InputPsiControl
    TimecodeSource: InputTimecodeSource
    TimecodeStart: str
    VideoSelector: "VideoSelectorTypeDef"


class InputTypeDef(TypedDict, total=False):
    AudioSelectorGroups: Dict[str, "AudioSelectorGroupTypeDef"]
    AudioSelectors: Dict[str, "AudioSelectorTypeDef"]
    CaptionSelectors: Dict[str, "CaptionSelectorTypeDef"]
    Crop: "RectangleTypeDef"
    DeblockFilter: InputDeblockFilter
    DecryptionSettings: "InputDecryptionSettingsTypeDef"
    DenoiseFilter: InputDenoiseFilter
    FileInput: str
    FilterEnable: InputFilterEnable
    FilterStrength: int
    ImageInserter: "ImageInserterTypeDef"
    InputClippings: List["InputClippingTypeDef"]
    InputScanType: InputScanType
    Position: "RectangleTypeDef"
    ProgramNumber: int
    PsiControl: InputPsiControl
    SupplementalImps: List[str]
    TimecodeSource: InputTimecodeSource
    TimecodeStart: str
    VideoSelector: "VideoSelectorTypeDef"


class InsertableImageTypeDef(TypedDict, total=False):
    Duration: int
    FadeIn: int
    FadeOut: int
    Height: int
    ImageInserterInput: str
    ImageX: int
    ImageY: int
    Layer: int
    Opacity: int
    StartTime: str
    Width: int


JobMessagesTypeDef = TypedDict(
    "JobMessagesTypeDef", {"Info": List[str], "Warning": List[str]}, total=False
)


class JobSettingsTypeDef(TypedDict, total=False):
    AdAvailOffset: int
    AvailBlanking: "AvailBlankingTypeDef"
    Esam: "EsamSettingsTypeDef"
    Inputs: List["InputTypeDef"]
    MotionImageInserter: "MotionImageInserterTypeDef"
    NielsenConfiguration: "NielsenConfigurationTypeDef"
    NielsenNonLinearWatermark: "NielsenNonLinearWatermarkSettingsTypeDef"
    OutputGroups: List["OutputGroupTypeDef"]
    TimecodeConfig: "TimecodeConfigTypeDef"
    TimedMetadataInsertion: "TimedMetadataInsertionTypeDef"


class JobTemplateSettingsTypeDef(TypedDict, total=False):
    AdAvailOffset: int
    AvailBlanking: "AvailBlankingTypeDef"
    Esam: "EsamSettingsTypeDef"
    Inputs: List["InputTemplateTypeDef"]
    MotionImageInserter: "MotionImageInserterTypeDef"
    NielsenConfiguration: "NielsenConfigurationTypeDef"
    NielsenNonLinearWatermark: "NielsenNonLinearWatermarkSettingsTypeDef"
    OutputGroups: List["OutputGroupTypeDef"]
    TimecodeConfig: "TimecodeConfigTypeDef"
    TimedMetadataInsertion: "TimedMetadataInsertionTypeDef"


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


class _RequiredJobTypeDef(TypedDict):
    Role: str
    Settings: "JobSettingsTypeDef"


class JobTypeDef(_RequiredJobTypeDef, total=False):
    AccelerationSettings: "AccelerationSettingsTypeDef"
    AccelerationStatus: AccelerationStatus
    Arn: str
    BillingTagsSource: BillingTagsSource
    CreatedAt: datetime
    CurrentPhase: JobPhase
    ErrorCode: int
    ErrorMessage: str
    HopDestinations: List["HopDestinationTypeDef"]
    Id: str
    JobPercentComplete: int
    JobTemplate: str
    Messages: "JobMessagesTypeDef"
    OutputGroupDetails: List["OutputGroupDetailTypeDef"]
    Priority: int
    Queue: str
    QueueTransitions: List["QueueTransitionTypeDef"]
    RetryCount: int
    SimulateReservedQueue: SimulateReservedQueue
    Status: JobStatus
    StatusUpdateInterval: StatusUpdateInterval
    Timing: "TimingTypeDef"
    UserMetadata: Dict[str, str]


class ListJobTemplatesResponseTypeDef(TypedDict, total=False):
    JobTemplates: List["JobTemplateTypeDef"]
    NextToken: str


class ListJobsResponseTypeDef(TypedDict, total=False):
    Jobs: List["JobTypeDef"]
    NextToken: str


class ListPresetsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Presets: List["PresetTypeDef"]


class ListQueuesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Queues: List["QueueTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    ResourceTags: "ResourceTagsTypeDef"


class M2tsScte35EsamTypeDef(TypedDict, total=False):
    Scte35EsamPid: int


class M2tsSettingsTypeDef(TypedDict, total=False):
    AudioBufferModel: M2tsAudioBufferModel
    AudioDuration: M2tsAudioDuration
    AudioFramesPerPes: int
    AudioPids: List[int]
    Bitrate: int
    BufferModel: M2tsBufferModel
    DvbNitSettings: "DvbNitSettingsTypeDef"
    DvbSdtSettings: "DvbSdtSettingsTypeDef"
    DvbSubPids: List[int]
    DvbTdtSettings: "DvbTdtSettingsTypeDef"
    DvbTeletextPid: int
    EbpAudioInterval: M2tsEbpAudioInterval
    EbpPlacement: M2tsEbpPlacement
    EsRateInPes: M2tsEsRateInPes
    ForceTsVideoEbpOrder: M2tsForceTsVideoEbpOrder
    FragmentTime: float
    MaxPcrInterval: int
    MinEbpInterval: int
    NielsenId3: M2tsNielsenId3
    NullPacketBitrate: float
    PatInterval: int
    PcrControl: M2tsPcrControl
    PcrPid: int
    PmtInterval: int
    PmtPid: int
    PrivateMetadataPid: int
    ProgramNumber: int
    RateMode: M2tsRateMode
    Scte35Esam: "M2tsScte35EsamTypeDef"
    Scte35Pid: int
    Scte35Source: M2tsScte35Source
    SegmentationMarkers: M2tsSegmentationMarkers
    SegmentationStyle: M2tsSegmentationStyle
    SegmentationTime: float
    TimedMetadataPid: int
    TransportStreamId: int
    VideoPid: int


class M3u8SettingsTypeDef(TypedDict, total=False):
    AudioDuration: M3u8AudioDuration
    AudioFramesPerPes: int
    AudioPids: List[int]
    NielsenId3: M3u8NielsenId3
    PatInterval: int
    PcrControl: M3u8PcrControl
    PcrPid: int
    PmtInterval: int
    PmtPid: int
    PrivateMetadataPid: int
    ProgramNumber: int
    Scte35Pid: int
    Scte35Source: M3u8Scte35Source
    TimedMetadata: TimedMetadata
    TimedMetadataPid: int
    TransportStreamId: int
    VideoPid: int


class MotionImageInserterTypeDef(TypedDict, total=False):
    Framerate: "MotionImageInsertionFramerateTypeDef"
    Input: str
    InsertionMode: MotionImageInsertionMode
    Offset: "MotionImageInsertionOffsetTypeDef"
    Playback: MotionImagePlayback
    StartTime: str


class MotionImageInsertionFramerateTypeDef(TypedDict, total=False):
    FramerateDenominator: int
    FramerateNumerator: int


class MotionImageInsertionOffsetTypeDef(TypedDict, total=False):
    ImageX: int
    ImageY: int


class MovSettingsTypeDef(TypedDict, total=False):
    ClapAtom: MovClapAtom
    CslgAtom: MovCslgAtom
    Mpeg2FourCCControl: MovMpeg2FourCCControl
    PaddingControl: MovPaddingControl
    Reference: MovReference


class Mp2SettingsTypeDef(TypedDict, total=False):
    Bitrate: int
    Channels: int
    SampleRate: int


class Mp3SettingsTypeDef(TypedDict, total=False):
    Bitrate: int
    Channels: int
    RateControlMode: Mp3RateControlMode
    SampleRate: int
    VbrQuality: int


class Mp4SettingsTypeDef(TypedDict, total=False):
    AudioDuration: CmfcAudioDuration
    CslgAtom: Mp4CslgAtom
    CttsVersion: int
    FreeSpaceBox: Mp4FreeSpaceBox
    MoovPlacement: Mp4MoovPlacement
    Mp4MajorBrand: str


class MpdSettingsTypeDef(TypedDict, total=False):
    AccessibilityCaptionHints: MpdAccessibilityCaptionHints
    AudioDuration: MpdAudioDuration
    CaptionContainerType: MpdCaptionContainerType
    Scte35Esam: MpdScte35Esam
    Scte35Source: MpdScte35Source


class Mpeg2SettingsTypeDef(TypedDict, total=False):
    AdaptiveQuantization: Mpeg2AdaptiveQuantization
    Bitrate: int
    CodecLevel: Mpeg2CodecLevel
    CodecProfile: Mpeg2CodecProfile
    DynamicSubGop: Mpeg2DynamicSubGop
    FramerateControl: Mpeg2FramerateControl
    FramerateConversionAlgorithm: Mpeg2FramerateConversionAlgorithm
    FramerateDenominator: int
    FramerateNumerator: int
    GopClosedCadence: int
    GopSize: float
    GopSizeUnits: Mpeg2GopSizeUnits
    HrdBufferInitialFillPercentage: int
    HrdBufferSize: int
    InterlaceMode: Mpeg2InterlaceMode
    IntraDcPrecision: Mpeg2IntraDcPrecision
    MaxBitrate: int
    MinIInterval: int
    NumberBFramesBetweenReferenceFrames: int
    ParControl: Mpeg2ParControl
    ParDenominator: int
    ParNumerator: int
    QualityTuningLevel: Mpeg2QualityTuningLevel
    RateControlMode: Mpeg2RateControlMode
    ScanTypeConversionMode: Mpeg2ScanTypeConversionMode
    SceneChangeDetect: Mpeg2SceneChangeDetect
    SlowPal: Mpeg2SlowPal
    Softness: int
    SpatialAdaptiveQuantization: Mpeg2SpatialAdaptiveQuantization
    Syntax: Mpeg2Syntax
    Telecine: Mpeg2Telecine
    TemporalAdaptiveQuantization: Mpeg2TemporalAdaptiveQuantization


class MsSmoothAdditionalManifestTypeDef(TypedDict, total=False):
    ManifestNameModifier: str
    SelectedOutputs: List[str]


class MsSmoothEncryptionSettingsTypeDef(TypedDict, total=False):
    SpekeKeyProvider: "SpekeKeyProviderTypeDef"


class MsSmoothGroupSettingsTypeDef(TypedDict, total=False):
    AdditionalManifests: List["MsSmoothAdditionalManifestTypeDef"]
    AudioDeduplication: MsSmoothAudioDeduplication
    Destination: str
    DestinationSettings: "DestinationSettingsTypeDef"
    Encryption: "MsSmoothEncryptionSettingsTypeDef"
    FragmentLength: int
    ManifestEncoding: MsSmoothManifestEncoding


class MxfSettingsTypeDef(TypedDict, total=False):
    AfdSignaling: MxfAfdSignaling
    Profile: MxfProfile


class NexGuardFileMarkerSettingsTypeDef(TypedDict, total=False):
    License: str
    Payload: int
    Preset: str
    Strength: WatermarkingStrength


class NielsenConfigurationTypeDef(TypedDict, total=False):
    BreakoutCode: int
    DistributorId: str


class NielsenNonLinearWatermarkSettingsTypeDef(TypedDict, total=False):
    ActiveWatermarkProcess: NielsenActiveWatermarkProcessType
    AdiFilename: str
    AssetId: str
    AssetName: str
    CbetSourceId: str
    EpisodeId: str
    MetadataDestination: str
    SourceId: int
    SourceWatermarkStatus: NielsenSourceWatermarkStatusType
    TicServerUrl: str
    UniqueTicPerAudioTrack: NielsenUniqueTicPerAudioTrackType


class NoiseReducerFilterSettingsTypeDef(TypedDict, total=False):
    Strength: int


class NoiseReducerSpatialFilterSettingsTypeDef(TypedDict, total=False):
    PostFilterSharpenStrength: int
    Speed: int
    Strength: int


class NoiseReducerTemporalFilterSettingsTypeDef(TypedDict, total=False):
    AggressiveMode: int
    PostTemporalSharpening: NoiseFilterPostTemporalSharpening
    Speed: int
    Strength: int


class NoiseReducerTypeDef(TypedDict, total=False):
    Filter: NoiseReducerFilter
    FilterSettings: "NoiseReducerFilterSettingsTypeDef"
    SpatialFilterSettings: "NoiseReducerSpatialFilterSettingsTypeDef"
    TemporalFilterSettings: "NoiseReducerTemporalFilterSettingsTypeDef"


class OpusSettingsTypeDef(TypedDict, total=False):
    Bitrate: int
    Channels: int
    SampleRate: int


class OutputChannelMappingTypeDef(TypedDict, total=False):
    InputChannels: List[int]
    InputChannelsFineTune: List[float]


class OutputDetailTypeDef(TypedDict, total=False):
    DurationInMs: int
    VideoDetails: "VideoDetailTypeDef"


class OutputGroupDetailTypeDef(TypedDict, total=False):
    OutputDetails: List["OutputDetailTypeDef"]


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


class OutputGroupTypeDef(TypedDict, total=False):
    AutomatedEncodingSettings: "AutomatedEncodingSettingsTypeDef"
    CustomName: str
    Name: str
    OutputGroupSettings: "OutputGroupSettingsTypeDef"
    Outputs: List["OutputTypeDef"]


class OutputSettingsTypeDef(TypedDict, total=False):
    HlsSettings: "HlsSettingsTypeDef"


class OutputTypeDef(TypedDict):
    AudioDescriptions: List["AudioDescriptionTypeDef"]
    CaptionDescriptions: List["CaptionDescriptionTypeDef"]
    ContainerSettings: "ContainerSettingsTypeDef"
    Extension: str
    NameModifier: str
    OutputSettings: "OutputSettingsTypeDef"
    Preset: str
    VideoDescription: "VideoDescriptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PartnerWatermarkingTypeDef(TypedDict, total=False):
    NexguardFileMarkerSettings: "NexGuardFileMarkerSettingsTypeDef"


class PresetSettingsTypeDef(TypedDict, total=False):
    AudioDescriptions: List["AudioDescriptionTypeDef"]
    CaptionDescriptions: List["CaptionDescriptionPresetTypeDef"]
    ContainerSettings: "ContainerSettingsTypeDef"
    VideoDescription: "VideoDescriptionTypeDef"


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


class ProresSettingsTypeDef(TypedDict, total=False):
    CodecProfile: ProresCodecProfile
    FramerateControl: ProresFramerateControl
    FramerateConversionAlgorithm: ProresFramerateConversionAlgorithm
    FramerateDenominator: int
    FramerateNumerator: int
    InterlaceMode: ProresInterlaceMode
    ParControl: ProresParControl
    ParDenominator: int
    ParNumerator: int
    ScanTypeConversionMode: ProresScanTypeConversionMode
    SlowPal: ProresSlowPal
    Telecine: ProresTelecine


class QueueTransitionTypeDef(TypedDict, total=False):
    DestinationQueue: str
    SourceQueue: str
    Timestamp: datetime


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


class RectangleTypeDef(TypedDict, total=False):
    Height: int
    Width: int
    X: int
    Y: int


class RemixSettingsTypeDef(TypedDict, total=False):
    ChannelMapping: "ChannelMappingTypeDef"
    ChannelsIn: int
    ChannelsOut: int


class ReservationPlanSettingsTypeDef(TypedDict):
    Commitment: Literal["ONE_YEAR"]
    RenewalType: RenewalType
    ReservedSlots: int


class ReservationPlanTypeDef(TypedDict, total=False):
    Commitment: Literal["ONE_YEAR"]
    ExpiresAt: datetime
    PurchasedAt: datetime
    RenewalType: RenewalType
    ReservedSlots: int
    Status: ReservationPlanStatus


class ResourceTagsTypeDef(TypedDict, total=False):
    Arn: str
    Tags: Dict[str, str]


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class S3DestinationAccessControlTypeDef(TypedDict, total=False):
    CannedAcl: S3ObjectCannedAcl


class S3DestinationSettingsTypeDef(TypedDict, total=False):
    AccessControl: "S3DestinationAccessControlTypeDef"
    Encryption: "S3EncryptionSettingsTypeDef"


class S3EncryptionSettingsTypeDef(TypedDict, total=False):
    EncryptionType: S3ServerSideEncryptionType
    KmsKeyArn: str


class SccDestinationSettingsTypeDef(TypedDict, total=False):
    Framerate: SccDestinationFramerate


class SpekeKeyProviderCmafTypeDef(TypedDict, total=False):
    CertificateArn: str
    DashSignaledSystemIds: List[str]
    HlsSignaledSystemIds: List[str]
    ResourceId: str
    Url: str


class SpekeKeyProviderTypeDef(TypedDict, total=False):
    CertificateArn: str
    ResourceId: str
    SystemIds: List[str]
    Url: str


class StaticKeyProviderTypeDef(TypedDict, total=False):
    KeyFormat: str
    KeyFormatVersions: str
    StaticKeyValue: str
    Url: str


class TeletextDestinationSettingsTypeDef(TypedDict, total=False):
    PageNumber: str
    PageTypes: List[TeletextPageType]


class TeletextSourceSettingsTypeDef(TypedDict, total=False):
    PageNumber: str


class TimecodeBurninTypeDef(TypedDict, total=False):
    FontSize: int
    Position: TimecodeBurninPosition
    Prefix: str


class TimecodeConfigTypeDef(TypedDict, total=False):
    Anchor: str
    Source: TimecodeSource
    Start: str
    TimestampOffset: str


class TimedMetadataInsertionTypeDef(TypedDict, total=False):
    Id3Insertions: List["Id3InsertionTypeDef"]


class TimingTypeDef(TypedDict, total=False):
    FinishTime: datetime
    StartTime: datetime
    SubmitTime: datetime


class TrackSourceSettingsTypeDef(TypedDict, total=False):
    TrackNumber: int


class TtmlDestinationSettingsTypeDef(TypedDict, total=False):
    StylePassthrough: TtmlStylePassthrough


class UpdateJobTemplateResponseTypeDef(TypedDict, total=False):
    JobTemplate: "JobTemplateTypeDef"


class UpdatePresetResponseTypeDef(TypedDict, total=False):
    Preset: "PresetTypeDef"


class UpdateQueueResponseTypeDef(TypedDict, total=False):
    Queue: "QueueTypeDef"


class Vc3SettingsTypeDef(TypedDict, total=False):
    FramerateControl: Vc3FramerateControl
    FramerateConversionAlgorithm: Vc3FramerateConversionAlgorithm
    FramerateDenominator: int
    FramerateNumerator: int
    InterlaceMode: Vc3InterlaceMode
    ScanTypeConversionMode: Vc3ScanTypeConversionMode
    SlowPal: Vc3SlowPal
    Telecine: Vc3Telecine
    Vc3Class: Vc3Class


class VideoCodecSettingsTypeDef(TypedDict, total=False):
    Av1Settings: "Av1SettingsTypeDef"
    AvcIntraSettings: "AvcIntraSettingsTypeDef"
    Codec: VideoCodec
    FrameCaptureSettings: "FrameCaptureSettingsTypeDef"
    H264Settings: "H264SettingsTypeDef"
    H265Settings: "H265SettingsTypeDef"
    Mpeg2Settings: "Mpeg2SettingsTypeDef"
    ProresSettings: "ProresSettingsTypeDef"
    Vc3Settings: "Vc3SettingsTypeDef"
    Vp8Settings: "Vp8SettingsTypeDef"
    Vp9Settings: "Vp9SettingsTypeDef"


class VideoDescriptionTypeDef(TypedDict, total=False):
    AfdSignaling: AfdSignaling
    AntiAlias: AntiAlias
    CodecSettings: "VideoCodecSettingsTypeDef"
    ColorMetadata: ColorMetadata
    Crop: "RectangleTypeDef"
    DropFrameTimecode: DropFrameTimecode
    FixedAfd: int
    Height: int
    Position: "RectangleTypeDef"
    RespondToAfd: RespondToAfd
    ScalingBehavior: ScalingBehavior
    Sharpness: int
    TimecodeInsertion: VideoTimecodeInsertion
    VideoPreprocessors: "VideoPreprocessorTypeDef"
    Width: int


class VideoDetailTypeDef(TypedDict, total=False):
    HeightInPx: int
    WidthInPx: int


class VideoPreprocessorTypeDef(TypedDict, total=False):
    ColorCorrector: "ColorCorrectorTypeDef"
    Deinterlacer: "DeinterlacerTypeDef"
    DolbyVision: "DolbyVisionTypeDef"
    ImageInserter: "ImageInserterTypeDef"
    NoiseReducer: "NoiseReducerTypeDef"
    PartnerWatermarking: "PartnerWatermarkingTypeDef"
    TimecodeBurnin: "TimecodeBurninTypeDef"


class VideoSelectorTypeDef(TypedDict, total=False):
    AlphaBehavior: AlphaBehavior
    ColorSpace: ColorSpace
    ColorSpaceUsage: ColorSpaceUsage
    Hdr10Metadata: "Hdr10MetadataTypeDef"
    Pid: int
    ProgramNumber: int
    Rotate: InputRotate


class VorbisSettingsTypeDef(TypedDict, total=False):
    Channels: int
    SampleRate: int
    VbrQuality: int


class Vp8SettingsTypeDef(TypedDict, total=False):
    Bitrate: int
    FramerateControl: Vp8FramerateControl
    FramerateConversionAlgorithm: Vp8FramerateConversionAlgorithm
    FramerateDenominator: int
    FramerateNumerator: int
    GopSize: float
    HrdBufferSize: int
    MaxBitrate: int
    ParControl: Vp8ParControl
    ParDenominator: int
    ParNumerator: int
    QualityTuningLevel: Vp8QualityTuningLevel
    RateControlMode: Literal["VBR"]


class Vp9SettingsTypeDef(TypedDict, total=False):
    Bitrate: int
    FramerateControl: Vp9FramerateControl
    FramerateConversionAlgorithm: Vp9FramerateConversionAlgorithm
    FramerateDenominator: int
    FramerateNumerator: int
    GopSize: float
    HrdBufferSize: int
    MaxBitrate: int
    ParControl: Vp9ParControl
    ParDenominator: int
    ParNumerator: int
    QualityTuningLevel: Vp9QualityTuningLevel
    RateControlMode: Literal["VBR"]


class WavSettingsTypeDef(TypedDict, total=False):
    BitDepth: int
    Channels: int
    Format: WavFormat
    SampleRate: int


class WebvttDestinationSettingsTypeDef(TypedDict, total=False):
    StylePassthrough: WebvttStylePassthrough
