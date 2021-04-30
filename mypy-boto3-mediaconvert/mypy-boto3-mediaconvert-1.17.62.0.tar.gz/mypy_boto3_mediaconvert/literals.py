"""
Main interface for mediaconvert service literal definitions.

Usage::

    ```python
    from mypy_boto3_mediaconvert.literals import AacAudioDescriptionBroadcasterMix

    data: AacAudioDescriptionBroadcasterMix = "BROADCASTER_MIXED_AD"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AacAudioDescriptionBroadcasterMix",
    "AacCodecProfile",
    "AacCodingMode",
    "AacRateControlMode",
    "AacRawFormat",
    "AacSpecification",
    "AacVbrQuality",
    "Ac3BitstreamMode",
    "Ac3CodingMode",
    "Ac3DynamicRangeCompressionLine",
    "Ac3DynamicRangeCompressionProfile",
    "Ac3DynamicRangeCompressionRf",
    "Ac3LfeFilter",
    "Ac3MetadataControl",
    "AccelerationMode",
    "AccelerationStatus",
    "AfdSignaling",
    "AlphaBehavior",
    "AncillaryConvert608To708",
    "AncillaryTerminateCaptions",
    "AntiAlias",
    "AudioChannelTag",
    "AudioCodec",
    "AudioDefaultSelection",
    "AudioLanguageCodeControl",
    "AudioNormalizationAlgorithm",
    "AudioNormalizationAlgorithmControl",
    "AudioNormalizationLoudnessLogging",
    "AudioNormalizationPeakCalculation",
    "AudioSelectorType",
    "AudioTypeControl",
    "Av1AdaptiveQuantization",
    "Av1FramerateControl",
    "Av1FramerateConversionAlgorithm",
    "Av1RateControlMode",
    "Av1SpatialAdaptiveQuantization",
    "AvcIntraClass",
    "AvcIntraFramerateControl",
    "AvcIntraFramerateConversionAlgorithm",
    "AvcIntraInterlaceMode",
    "AvcIntraScanTypeConversionMode",
    "AvcIntraSlowPal",
    "AvcIntraTelecine",
    "AvcIntraUhdQualityTuningLevel",
    "BillingTagsSource",
    "BurninSubtitleAlignment",
    "BurninSubtitleBackgroundColor",
    "BurninSubtitleFontColor",
    "BurninSubtitleOutlineColor",
    "BurninSubtitleShadowColor",
    "BurninSubtitleTeletextSpacing",
    "CaptionDestinationType",
    "CaptionSourceType",
    "CmafClientCache",
    "CmafCodecSpecification",
    "CmafEncryptionType",
    "CmafInitializationVectorInManifest",
    "CmafKeyProviderType",
    "CmafManifestCompression",
    "CmafManifestDurationFormat",
    "CmafMpdProfile",
    "CmafPtsOffsetHandlingForBFrames",
    "CmafSegmentControl",
    "CmafStreamInfResolution",
    "CmafWriteDASHManifest",
    "CmafWriteHLSManifest",
    "CmafWriteSegmentTimelineInRepresentation",
    "CmfcAudioDuration",
    "CmfcAudioTrackType",
    "CmfcDescriptiveVideoServiceFlag",
    "CmfcIFrameOnlyManifest",
    "CmfcScte35Esam",
    "CmfcScte35Source",
    "ColorMetadata",
    "ColorSpace",
    "ColorSpaceConversion",
    "ColorSpaceUsage",
    "Commitment",
    "ContainerType",
    "DashIsoGroupAudioChannelConfigSchemeIdUri",
    "DashIsoHbbtvCompliance",
    "DashIsoMpdProfile",
    "DashIsoPlaybackDeviceCompatibility",
    "DashIsoPtsOffsetHandlingForBFrames",
    "DashIsoSegmentControl",
    "DashIsoWriteSegmentTimelineInRepresentation",
    "DecryptionMode",
    "DeinterlaceAlgorithm",
    "DeinterlacerControl",
    "DeinterlacerMode",
    "DescribeEndpointsMode",
    "DescribeEndpointsPaginatorName",
    "DolbyVisionLevel6Mode",
    "DolbyVisionProfile",
    "DropFrameTimecode",
    "DvbSubtitleAlignment",
    "DvbSubtitleBackgroundColor",
    "DvbSubtitleFontColor",
    "DvbSubtitleOutlineColor",
    "DvbSubtitleShadowColor",
    "DvbSubtitleTeletextSpacing",
    "DvbSubtitlingType",
    "Eac3AtmosBitstreamMode",
    "Eac3AtmosCodingMode",
    "Eac3AtmosDialogueIntelligence",
    "Eac3AtmosDynamicRangeCompressionLine",
    "Eac3AtmosDynamicRangeCompressionRf",
    "Eac3AtmosMeteringMode",
    "Eac3AtmosStereoDownmix",
    "Eac3AtmosSurroundExMode",
    "Eac3AttenuationControl",
    "Eac3BitstreamMode",
    "Eac3CodingMode",
    "Eac3DcFilter",
    "Eac3DynamicRangeCompressionLine",
    "Eac3DynamicRangeCompressionRf",
    "Eac3LfeControl",
    "Eac3LfeFilter",
    "Eac3MetadataControl",
    "Eac3PassthroughControl",
    "Eac3PhaseControl",
    "Eac3StereoDownmix",
    "Eac3SurroundExMode",
    "Eac3SurroundMode",
    "EmbeddedConvert608To708",
    "EmbeddedTerminateCaptions",
    "F4vMoovPlacement",
    "FileSourceConvert608To708",
    "FontScript",
    "H264AdaptiveQuantization",
    "H264CodecLevel",
    "H264CodecProfile",
    "H264DynamicSubGop",
    "H264EntropyEncoding",
    "H264FieldEncoding",
    "H264FlickerAdaptiveQuantization",
    "H264FramerateControl",
    "H264FramerateConversionAlgorithm",
    "H264GopBReference",
    "H264GopSizeUnits",
    "H264InterlaceMode",
    "H264ParControl",
    "H264QualityTuningLevel",
    "H264RateControlMode",
    "H264RepeatPps",
    "H264ScanTypeConversionMode",
    "H264SceneChangeDetect",
    "H264SlowPal",
    "H264SpatialAdaptiveQuantization",
    "H264Syntax",
    "H264Telecine",
    "H264TemporalAdaptiveQuantization",
    "H264UnregisteredSeiTimecode",
    "H265AdaptiveQuantization",
    "H265AlternateTransferFunctionSei",
    "H265CodecLevel",
    "H265CodecProfile",
    "H265DynamicSubGop",
    "H265FlickerAdaptiveQuantization",
    "H265FramerateControl",
    "H265FramerateConversionAlgorithm",
    "H265GopBReference",
    "H265GopSizeUnits",
    "H265InterlaceMode",
    "H265ParControl",
    "H265QualityTuningLevel",
    "H265RateControlMode",
    "H265SampleAdaptiveOffsetFilterMode",
    "H265ScanTypeConversionMode",
    "H265SceneChangeDetect",
    "H265SlowPal",
    "H265SpatialAdaptiveQuantization",
    "H265Telecine",
    "H265TemporalAdaptiveQuantization",
    "H265TemporalIds",
    "H265Tiles",
    "H265UnregisteredSeiTimecode",
    "H265WriteMp4PackagingType",
    "HlsAdMarkers",
    "HlsAudioOnlyContainer",
    "HlsAudioOnlyHeader",
    "HlsAudioTrackType",
    "HlsCaptionLanguageSetting",
    "HlsClientCache",
    "HlsCodecSpecification",
    "HlsDescriptiveVideoServiceFlag",
    "HlsDirectoryStructure",
    "HlsEncryptionType",
    "HlsIFrameOnlyManifest",
    "HlsInitializationVectorInManifest",
    "HlsKeyProviderType",
    "HlsManifestCompression",
    "HlsManifestDurationFormat",
    "HlsOfflineEncrypted",
    "HlsOutputSelection",
    "HlsProgramDateTime",
    "HlsSegmentControl",
    "HlsStreamInfResolution",
    "HlsTimedMetadataId3Frame",
    "ImscStylePassthrough",
    "InputDeblockFilter",
    "InputDenoiseFilter",
    "InputFilterEnable",
    "InputPsiControl",
    "InputRotate",
    "InputScanType",
    "InputTimecodeSource",
    "JobPhase",
    "JobStatus",
    "JobTemplateListBy",
    "LanguageCode",
    "ListJobTemplatesPaginatorName",
    "ListJobsPaginatorName",
    "ListPresetsPaginatorName",
    "ListQueuesPaginatorName",
    "M2tsAudioBufferModel",
    "M2tsAudioDuration",
    "M2tsBufferModel",
    "M2tsEbpAudioInterval",
    "M2tsEbpPlacement",
    "M2tsEsRateInPes",
    "M2tsForceTsVideoEbpOrder",
    "M2tsNielsenId3",
    "M2tsPcrControl",
    "M2tsRateMode",
    "M2tsScte35Source",
    "M2tsSegmentationMarkers",
    "M2tsSegmentationStyle",
    "M3u8AudioDuration",
    "M3u8NielsenId3",
    "M3u8PcrControl",
    "M3u8Scte35Source",
    "MotionImageInsertionMode",
    "MotionImagePlayback",
    "MovClapAtom",
    "MovCslgAtom",
    "MovMpeg2FourCCControl",
    "MovPaddingControl",
    "MovReference",
    "Mp3RateControlMode",
    "Mp4CslgAtom",
    "Mp4FreeSpaceBox",
    "Mp4MoovPlacement",
    "MpdAccessibilityCaptionHints",
    "MpdAudioDuration",
    "MpdCaptionContainerType",
    "MpdScte35Esam",
    "MpdScte35Source",
    "Mpeg2AdaptiveQuantization",
    "Mpeg2CodecLevel",
    "Mpeg2CodecProfile",
    "Mpeg2DynamicSubGop",
    "Mpeg2FramerateControl",
    "Mpeg2FramerateConversionAlgorithm",
    "Mpeg2GopSizeUnits",
    "Mpeg2InterlaceMode",
    "Mpeg2IntraDcPrecision",
    "Mpeg2ParControl",
    "Mpeg2QualityTuningLevel",
    "Mpeg2RateControlMode",
    "Mpeg2ScanTypeConversionMode",
    "Mpeg2SceneChangeDetect",
    "Mpeg2SlowPal",
    "Mpeg2SpatialAdaptiveQuantization",
    "Mpeg2Syntax",
    "Mpeg2Telecine",
    "Mpeg2TemporalAdaptiveQuantization",
    "MsSmoothAudioDeduplication",
    "MsSmoothManifestEncoding",
    "MxfAfdSignaling",
    "MxfProfile",
    "NielsenActiveWatermarkProcessType",
    "NielsenSourceWatermarkStatusType",
    "NielsenUniqueTicPerAudioTrackType",
    "NoiseFilterPostTemporalSharpening",
    "NoiseReducerFilter",
    "Order",
    "OutputGroupType",
    "OutputSdt",
    "PresetListBy",
    "PricingPlan",
    "ProresCodecProfile",
    "ProresFramerateControl",
    "ProresFramerateConversionAlgorithm",
    "ProresInterlaceMode",
    "ProresParControl",
    "ProresScanTypeConversionMode",
    "ProresSlowPal",
    "ProresTelecine",
    "QueueListBy",
    "QueueStatus",
    "RenewalType",
    "ReservationPlanStatus",
    "RespondToAfd",
    "S3ObjectCannedAcl",
    "S3ServerSideEncryptionType",
    "ScalingBehavior",
    "SccDestinationFramerate",
    "SimulateReservedQueue",
    "StatusUpdateInterval",
    "TeletextPageType",
    "TimecodeBurninPosition",
    "TimecodeSource",
    "TimedMetadata",
    "TtmlStylePassthrough",
    "TypeType",
    "Vc3Class",
    "Vc3FramerateControl",
    "Vc3FramerateConversionAlgorithm",
    "Vc3InterlaceMode",
    "Vc3ScanTypeConversionMode",
    "Vc3SlowPal",
    "Vc3Telecine",
    "VideoCodec",
    "VideoTimecodeInsertion",
    "Vp8FramerateControl",
    "Vp8FramerateConversionAlgorithm",
    "Vp8ParControl",
    "Vp8QualityTuningLevel",
    "Vp8RateControlMode",
    "Vp9FramerateControl",
    "Vp9FramerateConversionAlgorithm",
    "Vp9ParControl",
    "Vp9QualityTuningLevel",
    "Vp9RateControlMode",
    "WatermarkingStrength",
    "WavFormat",
    "WebvttStylePassthrough",
)


AacAudioDescriptionBroadcasterMix = Literal["BROADCASTER_MIXED_AD", "NORMAL"]
AacCodecProfile = Literal["HEV1", "HEV2", "LC"]
AacCodingMode = Literal[
    "AD_RECEIVER_MIX", "CODING_MODE_1_0", "CODING_MODE_1_1", "CODING_MODE_2_0", "CODING_MODE_5_1"
]
AacRateControlMode = Literal["CBR", "VBR"]
AacRawFormat = Literal["LATM_LOAS", "NONE"]
AacSpecification = Literal["MPEG2", "MPEG4"]
AacVbrQuality = Literal["HIGH", "LOW", "MEDIUM_HIGH", "MEDIUM_LOW"]
Ac3BitstreamMode = Literal[
    "COMMENTARY",
    "COMPLETE_MAIN",
    "DIALOGUE",
    "EMERGENCY",
    "HEARING_IMPAIRED",
    "MUSIC_AND_EFFECTS",
    "VISUALLY_IMPAIRED",
    "VOICE_OVER",
]
Ac3CodingMode = Literal[
    "CODING_MODE_1_0", "CODING_MODE_1_1", "CODING_MODE_2_0", "CODING_MODE_3_2_LFE"
]
Ac3DynamicRangeCompressionLine = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Ac3DynamicRangeCompressionProfile = Literal["FILM_STANDARD", "NONE"]
Ac3DynamicRangeCompressionRf = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Ac3LfeFilter = Literal["DISABLED", "ENABLED"]
Ac3MetadataControl = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AccelerationMode = Literal["DISABLED", "ENABLED", "PREFERRED"]
AccelerationStatus = Literal["ACCELERATED", "IN_PROGRESS", "NOT_ACCELERATED", "NOT_APPLICABLE"]
AfdSignaling = Literal["AUTO", "FIXED", "NONE"]
AlphaBehavior = Literal["DISCARD", "REMAP_TO_LUMA"]
AncillaryConvert608To708 = Literal["DISABLED", "UPCONVERT"]
AncillaryTerminateCaptions = Literal["DISABLED", "END_OF_INPUT"]
AntiAlias = Literal["DISABLED", "ENABLED"]
AudioChannelTag = Literal[
    "C", "CS", "L", "LC", "LFE", "LS", "LSD", "R", "RC", "RS", "RSD", "TCS", "VHC", "VHL", "VHR"
]
AudioCodec = Literal[
    "AAC", "AC3", "AIFF", "EAC3", "EAC3_ATMOS", "MP2", "MP3", "OPUS", "PASSTHROUGH", "VORBIS", "WAV"
]
AudioDefaultSelection = Literal["DEFAULT", "NOT_DEFAULT"]
AudioLanguageCodeControl = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AudioNormalizationAlgorithm = Literal[
    "ITU_BS_1770_1", "ITU_BS_1770_2", "ITU_BS_1770_3", "ITU_BS_1770_4"
]
AudioNormalizationAlgorithmControl = Literal["CORRECT_AUDIO", "MEASURE_ONLY"]
AudioNormalizationLoudnessLogging = Literal["DONT_LOG", "LOG"]
AudioNormalizationPeakCalculation = Literal["NONE", "TRUE_PEAK"]
AudioSelectorType = Literal["LANGUAGE_CODE", "PID", "TRACK"]
AudioTypeControl = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
Av1AdaptiveQuantization = Literal["HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
Av1FramerateControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Av1FramerateConversionAlgorithm = Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
Av1RateControlMode = Literal["QVBR"]
Av1SpatialAdaptiveQuantization = Literal["DISABLED", "ENABLED"]
AvcIntraClass = Literal["CLASS_100", "CLASS_200", "CLASS_4K_2K", "CLASS_50"]
AvcIntraFramerateControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
AvcIntraFramerateConversionAlgorithm = Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
AvcIntraInterlaceMode = Literal[
    "BOTTOM_FIELD", "FOLLOW_BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "PROGRESSIVE", "TOP_FIELD"
]
AvcIntraScanTypeConversionMode = Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
AvcIntraSlowPal = Literal["DISABLED", "ENABLED"]
AvcIntraTelecine = Literal["HARD", "NONE"]
AvcIntraUhdQualityTuningLevel = Literal["MULTI_PASS", "SINGLE_PASS"]
BillingTagsSource = Literal["JOB", "JOB_TEMPLATE", "PRESET", "QUEUE"]
BurninSubtitleAlignment = Literal["CENTERED", "LEFT"]
BurninSubtitleBackgroundColor = Literal["BLACK", "NONE", "WHITE"]
BurninSubtitleFontColor = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
BurninSubtitleOutlineColor = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
BurninSubtitleShadowColor = Literal["BLACK", "NONE", "WHITE"]
BurninSubtitleTeletextSpacing = Literal["FIXED_GRID", "PROPORTIONAL"]
CaptionDestinationType = Literal[
    "BURN_IN",
    "DVB_SUB",
    "EMBEDDED",
    "EMBEDDED_PLUS_SCTE20",
    "IMSC",
    "SCC",
    "SCTE20_PLUS_EMBEDDED",
    "SMI",
    "SRT",
    "TELETEXT",
    "TTML",
    "WEBVTT",
]
CaptionSourceType = Literal[
    "ANCILLARY",
    "DVB_SUB",
    "EMBEDDED",
    "IMSC",
    "NULL_SOURCE",
    "SCC",
    "SCTE20",
    "SMI",
    "SMPTE_TT",
    "SRT",
    "STL",
    "TELETEXT",
    "TTML",
    "WEBVTT",
]
CmafClientCache = Literal["DISABLED", "ENABLED"]
CmafCodecSpecification = Literal["RFC_4281", "RFC_6381"]
CmafEncryptionType = Literal["AES_CTR", "SAMPLE_AES"]
CmafInitializationVectorInManifest = Literal["EXCLUDE", "INCLUDE"]
CmafKeyProviderType = Literal["SPEKE", "STATIC_KEY"]
CmafManifestCompression = Literal["GZIP", "NONE"]
CmafManifestDurationFormat = Literal["FLOATING_POINT", "INTEGER"]
CmafMpdProfile = Literal["MAIN_PROFILE", "ON_DEMAND_PROFILE"]
CmafPtsOffsetHandlingForBFrames = Literal["MATCH_INITIAL_PTS", "ZERO_BASED"]
CmafSegmentControl = Literal["SEGMENTED_FILES", "SINGLE_FILE"]
CmafStreamInfResolution = Literal["EXCLUDE", "INCLUDE"]
CmafWriteDASHManifest = Literal["DISABLED", "ENABLED"]
CmafWriteHLSManifest = Literal["DISABLED", "ENABLED"]
CmafWriteSegmentTimelineInRepresentation = Literal["DISABLED", "ENABLED"]
CmfcAudioDuration = Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"]
CmfcAudioTrackType = Literal[
    "ALTERNATE_AUDIO_AUTO_SELECT",
    "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
    "ALTERNATE_AUDIO_NOT_AUTO_SELECT",
]
CmfcDescriptiveVideoServiceFlag = Literal["DONT_FLAG", "FLAG"]
CmfcIFrameOnlyManifest = Literal["EXCLUDE", "INCLUDE"]
CmfcScte35Esam = Literal["INSERT", "NONE"]
CmfcScte35Source = Literal["NONE", "PASSTHROUGH"]
ColorMetadata = Literal["IGNORE", "INSERT"]
ColorSpace = Literal["FOLLOW", "HDR10", "HLG_2020", "REC_601", "REC_709"]
ColorSpaceConversion = Literal["FORCE_601", "FORCE_709", "FORCE_HDR10", "FORCE_HLG_2020", "NONE"]
ColorSpaceUsage = Literal["FALLBACK", "FORCE"]
Commitment = Literal["ONE_YEAR"]
ContainerType = Literal[
    "CMFC", "F4V", "ISMV", "M2TS", "M3U8", "MOV", "MP4", "MPD", "MXF", "RAW", "WEBM"
]
DashIsoGroupAudioChannelConfigSchemeIdUri = Literal[
    "DOLBY_CHANNEL_CONFIGURATION", "MPEG_CHANNEL_CONFIGURATION"
]
DashIsoHbbtvCompliance = Literal["HBBTV_1_5", "NONE"]
DashIsoMpdProfile = Literal["MAIN_PROFILE", "ON_DEMAND_PROFILE"]
DashIsoPlaybackDeviceCompatibility = Literal["CENC_V1", "UNENCRYPTED_SEI"]
DashIsoPtsOffsetHandlingForBFrames = Literal["MATCH_INITIAL_PTS", "ZERO_BASED"]
DashIsoSegmentControl = Literal["SEGMENTED_FILES", "SINGLE_FILE"]
DashIsoWriteSegmentTimelineInRepresentation = Literal["DISABLED", "ENABLED"]
DecryptionMode = Literal["AES_CBC", "AES_CTR", "AES_GCM"]
DeinterlaceAlgorithm = Literal["BLEND", "BLEND_TICKER", "INTERPOLATE", "INTERPOLATE_TICKER"]
DeinterlacerControl = Literal["FORCE_ALL_FRAMES", "NORMAL"]
DeinterlacerMode = Literal["ADAPTIVE", "DEINTERLACE", "INVERSE_TELECINE"]
DescribeEndpointsMode = Literal["DEFAULT", "GET_ONLY"]
DescribeEndpointsPaginatorName = Literal["describe_endpoints"]
DolbyVisionLevel6Mode = Literal["PASSTHROUGH", "RECALCULATE", "SPECIFY"]
DolbyVisionProfile = Literal["PROFILE_5"]
DropFrameTimecode = Literal["DISABLED", "ENABLED"]
DvbSubtitleAlignment = Literal["CENTERED", "LEFT"]
DvbSubtitleBackgroundColor = Literal["BLACK", "NONE", "WHITE"]
DvbSubtitleFontColor = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
DvbSubtitleOutlineColor = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
DvbSubtitleShadowColor = Literal["BLACK", "NONE", "WHITE"]
DvbSubtitleTeletextSpacing = Literal["FIXED_GRID", "PROPORTIONAL"]
DvbSubtitlingType = Literal["HEARING_IMPAIRED", "STANDARD"]
Eac3AtmosBitstreamMode = Literal["COMPLETE_MAIN"]
Eac3AtmosCodingMode = Literal["CODING_MODE_9_1_6"]
Eac3AtmosDialogueIntelligence = Literal["DISABLED", "ENABLED"]
Eac3AtmosDynamicRangeCompressionLine = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Eac3AtmosDynamicRangeCompressionRf = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Eac3AtmosMeteringMode = Literal[
    "ITU_BS_1770_1", "ITU_BS_1770_2", "ITU_BS_1770_3", "ITU_BS_1770_4", "LEQ_A"
]
Eac3AtmosStereoDownmix = Literal["DPL2", "NOT_INDICATED", "STEREO", "SURROUND"]
Eac3AtmosSurroundExMode = Literal["DISABLED", "ENABLED", "NOT_INDICATED"]
Eac3AttenuationControl = Literal["ATTENUATE_3_DB", "NONE"]
Eac3BitstreamMode = Literal[
    "COMMENTARY", "COMPLETE_MAIN", "EMERGENCY", "HEARING_IMPAIRED", "VISUALLY_IMPAIRED"
]
Eac3CodingMode = Literal["CODING_MODE_1_0", "CODING_MODE_2_0", "CODING_MODE_3_2"]
Eac3DcFilter = Literal["DISABLED", "ENABLED"]
Eac3DynamicRangeCompressionLine = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Eac3DynamicRangeCompressionRf = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Eac3LfeControl = Literal["LFE", "NO_LFE"]
Eac3LfeFilter = Literal["DISABLED", "ENABLED"]
Eac3MetadataControl = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
Eac3PassthroughControl = Literal["NO_PASSTHROUGH", "WHEN_POSSIBLE"]
Eac3PhaseControl = Literal["NO_SHIFT", "SHIFT_90_DEGREES"]
Eac3StereoDownmix = Literal["DPL2", "LO_RO", "LT_RT", "NOT_INDICATED"]
Eac3SurroundExMode = Literal["DISABLED", "ENABLED", "NOT_INDICATED"]
Eac3SurroundMode = Literal["DISABLED", "ENABLED", "NOT_INDICATED"]
EmbeddedConvert608To708 = Literal["DISABLED", "UPCONVERT"]
EmbeddedTerminateCaptions = Literal["DISABLED", "END_OF_INPUT"]
F4vMoovPlacement = Literal["NORMAL", "PROGRESSIVE_DOWNLOAD"]
FileSourceConvert608To708 = Literal["DISABLED", "UPCONVERT"]
FontScript = Literal["AUTOMATIC", "HANS", "HANT"]
H264AdaptiveQuantization = Literal["AUTO", "HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
H264CodecLevel = Literal[
    "AUTO",
    "LEVEL_1",
    "LEVEL_1_1",
    "LEVEL_1_2",
    "LEVEL_1_3",
    "LEVEL_2",
    "LEVEL_2_1",
    "LEVEL_2_2",
    "LEVEL_3",
    "LEVEL_3_1",
    "LEVEL_3_2",
    "LEVEL_4",
    "LEVEL_4_1",
    "LEVEL_4_2",
    "LEVEL_5",
    "LEVEL_5_1",
    "LEVEL_5_2",
]
H264CodecProfile = Literal["BASELINE", "HIGH", "HIGH_10BIT", "HIGH_422", "HIGH_422_10BIT", "MAIN"]
H264DynamicSubGop = Literal["ADAPTIVE", "STATIC"]
H264EntropyEncoding = Literal["CABAC", "CAVLC"]
H264FieldEncoding = Literal["FORCE_FIELD", "PAFF"]
H264FlickerAdaptiveQuantization = Literal["DISABLED", "ENABLED"]
H264FramerateControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H264FramerateConversionAlgorithm = Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
H264GopBReference = Literal["DISABLED", "ENABLED"]
H264GopSizeUnits = Literal["FRAMES", "SECONDS"]
H264InterlaceMode = Literal[
    "BOTTOM_FIELD", "FOLLOW_BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "PROGRESSIVE", "TOP_FIELD"
]
H264ParControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H264QualityTuningLevel = Literal["MULTI_PASS_HQ", "SINGLE_PASS", "SINGLE_PASS_HQ"]
H264RateControlMode = Literal["CBR", "QVBR", "VBR"]
H264RepeatPps = Literal["DISABLED", "ENABLED"]
H264ScanTypeConversionMode = Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
H264SceneChangeDetect = Literal["DISABLED", "ENABLED", "TRANSITION_DETECTION"]
H264SlowPal = Literal["DISABLED", "ENABLED"]
H264SpatialAdaptiveQuantization = Literal["DISABLED", "ENABLED"]
H264Syntax = Literal["DEFAULT", "RP2027"]
H264Telecine = Literal["HARD", "NONE", "SOFT"]
H264TemporalAdaptiveQuantization = Literal["DISABLED", "ENABLED"]
H264UnregisteredSeiTimecode = Literal["DISABLED", "ENABLED"]
H265AdaptiveQuantization = Literal["HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
H265AlternateTransferFunctionSei = Literal["DISABLED", "ENABLED"]
H265CodecLevel = Literal[
    "AUTO",
    "LEVEL_1",
    "LEVEL_2",
    "LEVEL_2_1",
    "LEVEL_3",
    "LEVEL_3_1",
    "LEVEL_4",
    "LEVEL_4_1",
    "LEVEL_5",
    "LEVEL_5_1",
    "LEVEL_5_2",
    "LEVEL_6",
    "LEVEL_6_1",
    "LEVEL_6_2",
]
H265CodecProfile = Literal[
    "MAIN10_HIGH",
    "MAIN10_MAIN",
    "MAIN_422_10BIT_HIGH",
    "MAIN_422_10BIT_MAIN",
    "MAIN_422_8BIT_HIGH",
    "MAIN_422_8BIT_MAIN",
    "MAIN_HIGH",
    "MAIN_MAIN",
]
H265DynamicSubGop = Literal["ADAPTIVE", "STATIC"]
H265FlickerAdaptiveQuantization = Literal["DISABLED", "ENABLED"]
H265FramerateControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H265FramerateConversionAlgorithm = Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
H265GopBReference = Literal["DISABLED", "ENABLED"]
H265GopSizeUnits = Literal["FRAMES", "SECONDS"]
H265InterlaceMode = Literal[
    "BOTTOM_FIELD", "FOLLOW_BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "PROGRESSIVE", "TOP_FIELD"
]
H265ParControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H265QualityTuningLevel = Literal["MULTI_PASS_HQ", "SINGLE_PASS", "SINGLE_PASS_HQ"]
H265RateControlMode = Literal["CBR", "QVBR", "VBR"]
H265SampleAdaptiveOffsetFilterMode = Literal["ADAPTIVE", "DEFAULT", "OFF"]
H265ScanTypeConversionMode = Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
H265SceneChangeDetect = Literal["DISABLED", "ENABLED", "TRANSITION_DETECTION"]
H265SlowPal = Literal["DISABLED", "ENABLED"]
H265SpatialAdaptiveQuantization = Literal["DISABLED", "ENABLED"]
H265Telecine = Literal["HARD", "NONE", "SOFT"]
H265TemporalAdaptiveQuantization = Literal["DISABLED", "ENABLED"]
H265TemporalIds = Literal["DISABLED", "ENABLED"]
H265Tiles = Literal["DISABLED", "ENABLED"]
H265UnregisteredSeiTimecode = Literal["DISABLED", "ENABLED"]
H265WriteMp4PackagingType = Literal["HEV1", "HVC1"]
HlsAdMarkers = Literal["ELEMENTAL", "ELEMENTAL_SCTE35"]
HlsAudioOnlyContainer = Literal["AUTOMATIC", "M2TS"]
HlsAudioOnlyHeader = Literal["EXCLUDE", "INCLUDE"]
HlsAudioTrackType = Literal[
    "ALTERNATE_AUDIO_AUTO_SELECT",
    "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
    "ALTERNATE_AUDIO_NOT_AUTO_SELECT",
    "AUDIO_ONLY_VARIANT_STREAM",
]
HlsCaptionLanguageSetting = Literal["INSERT", "NONE", "OMIT"]
HlsClientCache = Literal["DISABLED", "ENABLED"]
HlsCodecSpecification = Literal["RFC_4281", "RFC_6381"]
HlsDescriptiveVideoServiceFlag = Literal["DONT_FLAG", "FLAG"]
HlsDirectoryStructure = Literal["SINGLE_DIRECTORY", "SUBDIRECTORY_PER_STREAM"]
HlsEncryptionType = Literal["AES128", "SAMPLE_AES"]
HlsIFrameOnlyManifest = Literal["EXCLUDE", "INCLUDE"]
HlsInitializationVectorInManifest = Literal["EXCLUDE", "INCLUDE"]
HlsKeyProviderType = Literal["SPEKE", "STATIC_KEY"]
HlsManifestCompression = Literal["GZIP", "NONE"]
HlsManifestDurationFormat = Literal["FLOATING_POINT", "INTEGER"]
HlsOfflineEncrypted = Literal["DISABLED", "ENABLED"]
HlsOutputSelection = Literal["MANIFESTS_AND_SEGMENTS", "SEGMENTS_ONLY"]
HlsProgramDateTime = Literal["EXCLUDE", "INCLUDE"]
HlsSegmentControl = Literal["SEGMENTED_FILES", "SINGLE_FILE"]
HlsStreamInfResolution = Literal["EXCLUDE", "INCLUDE"]
HlsTimedMetadataId3Frame = Literal["NONE", "PRIV", "TDRL"]
ImscStylePassthrough = Literal["DISABLED", "ENABLED"]
InputDeblockFilter = Literal["DISABLED", "ENABLED"]
InputDenoiseFilter = Literal["DISABLED", "ENABLED"]
InputFilterEnable = Literal["AUTO", "DISABLE", "FORCE"]
InputPsiControl = Literal["IGNORE_PSI", "USE_PSI"]
InputRotate = Literal["AUTO", "DEGREES_180", "DEGREES_270", "DEGREES_90", "DEGREE_0"]
InputScanType = Literal["AUTO", "PSF"]
InputTimecodeSource = Literal["EMBEDDED", "SPECIFIEDSTART", "ZEROBASED"]
JobPhase = Literal["PROBING", "TRANSCODING", "UPLOADING"]
JobStatus = Literal["CANCELED", "COMPLETE", "ERROR", "PROGRESSING", "SUBMITTED"]
JobTemplateListBy = Literal["CREATION_DATE", "NAME", "SYSTEM"]
LanguageCode = Literal[
    "AAR",
    "ABK",
    "AFR",
    "AKA",
    "AMH",
    "ARA",
    "ARG",
    "ASM",
    "AVA",
    "AVE",
    "AYM",
    "AZE",
    "BAK",
    "BAM",
    "BEL",
    "BEN",
    "BIH",
    "BIS",
    "BOD",
    "BOS",
    "BRE",
    "BUL",
    "CAT",
    "CES",
    "CHA",
    "CHE",
    "CHU",
    "CHV",
    "COR",
    "COS",
    "CRE",
    "CYM",
    "DAN",
    "DEU",
    "DIV",
    "DZO",
    "ELL",
    "ENG",
    "ENM",
    "EPO",
    "EST",
    "EUS",
    "EWE",
    "FAO",
    "FAS",
    "FIJ",
    "FIN",
    "FRA",
    "FRM",
    "FRY",
    "FUL",
    "GER",
    "GLA",
    "GLE",
    "GLG",
    "GLV",
    "GRN",
    "GUJ",
    "HAT",
    "HAU",
    "HEB",
    "HER",
    "HIN",
    "HMO",
    "HRV",
    "HUN",
    "HYE",
    "IBO",
    "IDO",
    "III",
    "IKU",
    "ILE",
    "INA",
    "IND",
    "IPK",
    "ISL",
    "ITA",
    "JAV",
    "JPN",
    "KAL",
    "KAN",
    "KAS",
    "KAT",
    "KAU",
    "KAZ",
    "KHM",
    "KIK",
    "KIN",
    "KIR",
    "KOM",
    "KON",
    "KOR",
    "KUA",
    "KUR",
    "LAO",
    "LAT",
    "LAV",
    "LIM",
    "LIN",
    "LIT",
    "LTZ",
    "LUB",
    "LUG",
    "MAH",
    "MAL",
    "MAR",
    "MKD",
    "MLG",
    "MLT",
    "MON",
    "MRI",
    "MSA",
    "MYA",
    "NAU",
    "NAV",
    "NBL",
    "NDE",
    "NDO",
    "NEP",
    "NLD",
    "NNO",
    "NOB",
    "NOR",
    "NYA",
    "OCI",
    "OJI",
    "ORI",
    "ORJ",
    "ORM",
    "OSS",
    "PAN",
    "PLI",
    "POL",
    "POR",
    "PUS",
    "QAA",
    "QPC",
    "QUE",
    "ROH",
    "RON",
    "RUN",
    "RUS",
    "SAG",
    "SAN",
    "SIN",
    "SLK",
    "SLV",
    "SME",
    "SMO",
    "SNA",
    "SND",
    "SOM",
    "SOT",
    "SPA",
    "SQI",
    "SRB",
    "SRD",
    "SSW",
    "SUN",
    "SWA",
    "SWE",
    "TAH",
    "TAM",
    "TAT",
    "TEL",
    "TGK",
    "TGL",
    "THA",
    "TIR",
    "TNG",
    "TON",
    "TSN",
    "TSO",
    "TUK",
    "TUR",
    "TWI",
    "UIG",
    "UKR",
    "URD",
    "UZB",
    "VEN",
    "VIE",
    "VOL",
    "WLN",
    "WOL",
    "XHO",
    "YID",
    "YOR",
    "ZHA",
    "ZHO",
    "ZUL",
]
ListJobTemplatesPaginatorName = Literal["list_job_templates"]
ListJobsPaginatorName = Literal["list_jobs"]
ListPresetsPaginatorName = Literal["list_presets"]
ListQueuesPaginatorName = Literal["list_queues"]
M2tsAudioBufferModel = Literal["ATSC", "DVB"]
M2tsAudioDuration = Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"]
M2tsBufferModel = Literal["MULTIPLEX", "NONE"]
M2tsEbpAudioInterval = Literal["VIDEO_AND_FIXED_INTERVALS", "VIDEO_INTERVAL"]
M2tsEbpPlacement = Literal["VIDEO_AND_AUDIO_PIDS", "VIDEO_PID"]
M2tsEsRateInPes = Literal["EXCLUDE", "INCLUDE"]
M2tsForceTsVideoEbpOrder = Literal["DEFAULT", "FORCE"]
M2tsNielsenId3 = Literal["INSERT", "NONE"]
M2tsPcrControl = Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
M2tsRateMode = Literal["CBR", "VBR"]
M2tsScte35Source = Literal["NONE", "PASSTHROUGH"]
M2tsSegmentationMarkers = Literal[
    "EBP", "EBP_LEGACY", "NONE", "PSI_SEGSTART", "RAI_ADAPT", "RAI_SEGSTART"
]
M2tsSegmentationStyle = Literal["MAINTAIN_CADENCE", "RESET_CADENCE"]
M3u8AudioDuration = Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"]
M3u8NielsenId3 = Literal["INSERT", "NONE"]
M3u8PcrControl = Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
M3u8Scte35Source = Literal["NONE", "PASSTHROUGH"]
MotionImageInsertionMode = Literal["MOV", "PNG"]
MotionImagePlayback = Literal["ONCE", "REPEAT"]
MovClapAtom = Literal["EXCLUDE", "INCLUDE"]
MovCslgAtom = Literal["EXCLUDE", "INCLUDE"]
MovMpeg2FourCCControl = Literal["MPEG", "XDCAM"]
MovPaddingControl = Literal["NONE", "OMNEON"]
MovReference = Literal["EXTERNAL", "SELF_CONTAINED"]
Mp3RateControlMode = Literal["CBR", "VBR"]
Mp4CslgAtom = Literal["EXCLUDE", "INCLUDE"]
Mp4FreeSpaceBox = Literal["EXCLUDE", "INCLUDE"]
Mp4MoovPlacement = Literal["NORMAL", "PROGRESSIVE_DOWNLOAD"]
MpdAccessibilityCaptionHints = Literal["EXCLUDE", "INCLUDE"]
MpdAudioDuration = Literal["DEFAULT_CODEC_DURATION", "MATCH_VIDEO_DURATION"]
MpdCaptionContainerType = Literal["FRAGMENTED_MP4", "RAW"]
MpdScte35Esam = Literal["INSERT", "NONE"]
MpdScte35Source = Literal["NONE", "PASSTHROUGH"]
Mpeg2AdaptiveQuantization = Literal["HIGH", "LOW", "MEDIUM", "OFF"]
Mpeg2CodecLevel = Literal["AUTO", "HIGH", "HIGH1440", "LOW", "MAIN"]
Mpeg2CodecProfile = Literal["MAIN", "PROFILE_422"]
Mpeg2DynamicSubGop = Literal["ADAPTIVE", "STATIC"]
Mpeg2FramerateControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Mpeg2FramerateConversionAlgorithm = Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
Mpeg2GopSizeUnits = Literal["FRAMES", "SECONDS"]
Mpeg2InterlaceMode = Literal[
    "BOTTOM_FIELD", "FOLLOW_BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "PROGRESSIVE", "TOP_FIELD"
]
Mpeg2IntraDcPrecision = Literal[
    "AUTO",
    "INTRA_DC_PRECISION_10",
    "INTRA_DC_PRECISION_11",
    "INTRA_DC_PRECISION_8",
    "INTRA_DC_PRECISION_9",
]
Mpeg2ParControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Mpeg2QualityTuningLevel = Literal["MULTI_PASS", "SINGLE_PASS"]
Mpeg2RateControlMode = Literal["CBR", "VBR"]
Mpeg2ScanTypeConversionMode = Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
Mpeg2SceneChangeDetect = Literal["DISABLED", "ENABLED"]
Mpeg2SlowPal = Literal["DISABLED", "ENABLED"]
Mpeg2SpatialAdaptiveQuantization = Literal["DISABLED", "ENABLED"]
Mpeg2Syntax = Literal["DEFAULT", "D_10"]
Mpeg2Telecine = Literal["HARD", "NONE", "SOFT"]
Mpeg2TemporalAdaptiveQuantization = Literal["DISABLED", "ENABLED"]
MsSmoothAudioDeduplication = Literal["COMBINE_DUPLICATE_STREAMS", "NONE"]
MsSmoothManifestEncoding = Literal["UTF16", "UTF8"]
MxfAfdSignaling = Literal["COPY_FROM_VIDEO", "NO_COPY"]
MxfProfile = Literal["D_10", "OP1A", "XDCAM"]
NielsenActiveWatermarkProcessType = Literal["CBET", "NAES2_AND_NW", "NAES2_AND_NW_AND_CBET"]
NielsenSourceWatermarkStatusType = Literal["CLEAN", "WATERMARKED"]
NielsenUniqueTicPerAudioTrackType = Literal["RESERVE_UNIQUE_TICS_PER_TRACK", "SAME_TICS_PER_TRACK"]
NoiseFilterPostTemporalSharpening = Literal["AUTO", "DISABLED", "ENABLED"]
NoiseReducerFilter = Literal[
    "BILATERAL", "CONSERVE", "GAUSSIAN", "LANCZOS", "MEAN", "SHARPEN", "SPATIAL", "TEMPORAL"
]
Order = Literal["ASCENDING", "DESCENDING"]
OutputGroupType = Literal[
    "CMAF_GROUP_SETTINGS",
    "DASH_ISO_GROUP_SETTINGS",
    "FILE_GROUP_SETTINGS",
    "HLS_GROUP_SETTINGS",
    "MS_SMOOTH_GROUP_SETTINGS",
]
OutputSdt = Literal["SDT_FOLLOW", "SDT_FOLLOW_IF_PRESENT", "SDT_MANUAL", "SDT_NONE"]
PresetListBy = Literal["CREATION_DATE", "NAME", "SYSTEM"]
PricingPlan = Literal["ON_DEMAND", "RESERVED"]
ProresCodecProfile = Literal[
    "APPLE_PRORES_422", "APPLE_PRORES_422_HQ", "APPLE_PRORES_422_LT", "APPLE_PRORES_422_PROXY"
]
ProresFramerateControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
ProresFramerateConversionAlgorithm = Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
ProresInterlaceMode = Literal[
    "BOTTOM_FIELD", "FOLLOW_BOTTOM_FIELD", "FOLLOW_TOP_FIELD", "PROGRESSIVE", "TOP_FIELD"
]
ProresParControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
ProresScanTypeConversionMode = Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
ProresSlowPal = Literal["DISABLED", "ENABLED"]
ProresTelecine = Literal["HARD", "NONE"]
QueueListBy = Literal["CREATION_DATE", "NAME"]
QueueStatus = Literal["ACTIVE", "PAUSED"]
RenewalType = Literal["AUTO_RENEW", "EXPIRE"]
ReservationPlanStatus = Literal["ACTIVE", "EXPIRED"]
RespondToAfd = Literal["NONE", "PASSTHROUGH", "RESPOND"]
S3ObjectCannedAcl = Literal[
    "AUTHENTICATED_READ", "BUCKET_OWNER_FULL_CONTROL", "BUCKET_OWNER_READ", "PUBLIC_READ"
]
S3ServerSideEncryptionType = Literal["SERVER_SIDE_ENCRYPTION_KMS", "SERVER_SIDE_ENCRYPTION_S3"]
ScalingBehavior = Literal["DEFAULT", "STRETCH_TO_OUTPUT"]
SccDestinationFramerate = Literal[
    "FRAMERATE_23_97",
    "FRAMERATE_24",
    "FRAMERATE_25",
    "FRAMERATE_29_97_DROPFRAME",
    "FRAMERATE_29_97_NON_DROPFRAME",
]
SimulateReservedQueue = Literal["DISABLED", "ENABLED"]
StatusUpdateInterval = Literal[
    "SECONDS_10",
    "SECONDS_12",
    "SECONDS_120",
    "SECONDS_15",
    "SECONDS_180",
    "SECONDS_20",
    "SECONDS_240",
    "SECONDS_30",
    "SECONDS_300",
    "SECONDS_360",
    "SECONDS_420",
    "SECONDS_480",
    "SECONDS_540",
    "SECONDS_60",
    "SECONDS_600",
]
TeletextPageType = Literal[
    "PAGE_TYPE_ADDL_INFO",
    "PAGE_TYPE_HEARING_IMPAIRED_SUBTITLE",
    "PAGE_TYPE_INITIAL",
    "PAGE_TYPE_PROGRAM_SCHEDULE",
    "PAGE_TYPE_SUBTITLE",
]
TimecodeBurninPosition = Literal[
    "BOTTOM_CENTER",
    "BOTTOM_LEFT",
    "BOTTOM_RIGHT",
    "MIDDLE_CENTER",
    "MIDDLE_LEFT",
    "MIDDLE_RIGHT",
    "TOP_CENTER",
    "TOP_LEFT",
    "TOP_RIGHT",
]
TimecodeSource = Literal["EMBEDDED", "SPECIFIEDSTART", "ZEROBASED"]
TimedMetadata = Literal["NONE", "PASSTHROUGH"]
TtmlStylePassthrough = Literal["DISABLED", "ENABLED"]
TypeType = Literal["CUSTOM", "SYSTEM"]
Vc3Class = Literal["CLASS_145_8BIT", "CLASS_220_10BIT", "CLASS_220_8BIT"]
Vc3FramerateControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Vc3FramerateConversionAlgorithm = Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
Vc3InterlaceMode = Literal["INTERLACED", "PROGRESSIVE"]
Vc3ScanTypeConversionMode = Literal["INTERLACED", "INTERLACED_OPTIMIZE"]
Vc3SlowPal = Literal["DISABLED", "ENABLED"]
Vc3Telecine = Literal["HARD", "NONE"]
VideoCodec = Literal[
    "AV1", "AVC_INTRA", "FRAME_CAPTURE", "H_264", "H_265", "MPEG2", "PRORES", "VC3", "VP8", "VP9"
]
VideoTimecodeInsertion = Literal["DISABLED", "PIC_TIMING_SEI"]
Vp8FramerateControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Vp8FramerateConversionAlgorithm = Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
Vp8ParControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Vp8QualityTuningLevel = Literal["MULTI_PASS", "MULTI_PASS_HQ"]
Vp8RateControlMode = Literal["VBR"]
Vp9FramerateControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Vp9FramerateConversionAlgorithm = Literal["DUPLICATE_DROP", "FRAMEFORMER", "INTERPOLATE"]
Vp9ParControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
Vp9QualityTuningLevel = Literal["MULTI_PASS", "MULTI_PASS_HQ"]
Vp9RateControlMode = Literal["VBR"]
WatermarkingStrength = Literal["DEFAULT", "LIGHTER", "LIGHTEST", "STRONGER", "STRONGEST"]
WavFormat = Literal["RF64", "RIFF"]
WebvttStylePassthrough = Literal["DISABLED", "ENABLED"]
