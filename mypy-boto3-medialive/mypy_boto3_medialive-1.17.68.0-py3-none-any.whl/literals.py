"""
Type annotations for medialive service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_medialive/literals.html)

Usage::

    ```python
    from mypy_boto3_medialive.literals import AacCodingMode

    data: AacCodingMode = "AD_RECEIVER_MIX"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AacCodingMode",
    "AacInputType",
    "AacProfile",
    "AacRateControlMode",
    "AacRawFormat",
    "AacSpec",
    "AacVbrQuality",
    "Ac3BitstreamMode",
    "Ac3CodingMode",
    "Ac3DrcProfile",
    "Ac3LfeFilter",
    "Ac3MetadataControl",
    "AcceptHeader",
    "AfdSignaling",
    "AudioDescriptionAudioTypeControl",
    "AudioDescriptionLanguageCodeControl",
    "AudioLanguageSelectionPolicy",
    "AudioNormalizationAlgorithm",
    "AudioNormalizationAlgorithmControl",
    "AudioOnlyHlsSegmentType",
    "AudioOnlyHlsTrackType",
    "AudioType",
    "AuthenticationScheme",
    "AvailBlankingState",
    "BlackoutSlateNetworkEndBlackout",
    "BlackoutSlateState",
    "BurnInAlignment",
    "BurnInBackgroundColor",
    "BurnInFontColor",
    "BurnInOutlineColor",
    "BurnInShadowColor",
    "BurnInTeletextGridControl",
    "CdiInputResolution",
    "ChannelClass",
    "ChannelCreatedWaiterName",
    "ChannelDeletedWaiterName",
    "ChannelRunningWaiterName",
    "ChannelState",
    "ChannelStoppedWaiterName",
    "ContentType",
    "DescribeSchedulePaginatorName",
    "DeviceSettingsSyncState",
    "DeviceUpdateStatus",
    "DvbSdtOutputSdt",
    "DvbSubDestinationAlignment",
    "DvbSubDestinationBackgroundColor",
    "DvbSubDestinationFontColor",
    "DvbSubDestinationOutlineColor",
    "DvbSubDestinationShadowColor",
    "DvbSubDestinationTeletextGridControl",
    "Eac3AttenuationControl",
    "Eac3BitstreamMode",
    "Eac3CodingMode",
    "Eac3DcFilter",
    "Eac3DrcLine",
    "Eac3DrcRf",
    "Eac3LfeControl",
    "Eac3LfeFilter",
    "Eac3MetadataControl",
    "Eac3PassthroughControl",
    "Eac3PhaseControl",
    "Eac3StereoDownmix",
    "Eac3SurroundExMode",
    "Eac3SurroundMode",
    "EbuTtDDestinationStyleControl",
    "EbuTtDFillLineGapControl",
    "EmbeddedConvert608To708",
    "EmbeddedScte20Detection",
    "FeatureActivationsInputPrepareScheduleActions",
    "FecOutputIncludeFec",
    "FixedAfd",
    "Fmp4NielsenId3Behavior",
    "Fmp4TimedMetadataBehavior",
    "FollowPoint",
    "FrameCaptureIntervalUnit",
    "GlobalConfigurationInputEndAction",
    "GlobalConfigurationLowFramerateInputs",
    "GlobalConfigurationOutputLockingMode",
    "GlobalConfigurationOutputTimingSource",
    "H264AdaptiveQuantization",
    "H264ColorMetadata",
    "H264EntropyEncoding",
    "H264FlickerAq",
    "H264ForceFieldPictures",
    "H264FramerateControl",
    "H264GopBReference",
    "H264GopSizeUnits",
    "H264Level",
    "H264LookAheadRateControl",
    "H264ParControl",
    "H264Profile",
    "H264QualityLevel",
    "H264RateControlMode",
    "H264ScanType",
    "H264SceneChangeDetect",
    "H264SpatialAq",
    "H264SubGopLength",
    "H264Syntax",
    "H264TemporalAq",
    "H264TimecodeInsertionBehavior",
    "H265AdaptiveQuantization",
    "H265AlternativeTransferFunction",
    "H265ColorMetadata",
    "H265FlickerAq",
    "H265GopSizeUnits",
    "H265Level",
    "H265LookAheadRateControl",
    "H265Profile",
    "H265RateControlMode",
    "H265ScanType",
    "H265SceneChangeDetect",
    "H265Tier",
    "H265TimecodeInsertionBehavior",
    "HlsAdMarkers",
    "HlsAkamaiHttpTransferMode",
    "HlsCaptionLanguageSetting",
    "HlsClientCache",
    "HlsCodecSpecification",
    "HlsDirectoryStructure",
    "HlsDiscontinuityTags",
    "HlsEncryptionType",
    "HlsH265PackagingType",
    "HlsId3SegmentTaggingState",
    "HlsIncompleteSegmentBehavior",
    "HlsIvInManifest",
    "HlsIvSource",
    "HlsManifestCompression",
    "HlsManifestDurationFormat",
    "HlsMediaStoreStorageClass",
    "HlsMode",
    "HlsOutputSelection",
    "HlsProgramDateTime",
    "HlsRedundantManifest",
    "HlsSegmentationMode",
    "HlsStreamInfResolution",
    "HlsTimedMetadataId3Frame",
    "HlsTsFileMode",
    "HlsWebdavHttpTransferMode",
    "IFrameOnlyPlaylistType",
    "InputAttachedWaiterName",
    "InputClass",
    "InputCodec",
    "InputDeblockFilter",
    "InputDeletedWaiterName",
    "InputDenoiseFilter",
    "InputDetachedWaiterName",
    "InputDeviceActiveInput",
    "InputDeviceConfiguredInput",
    "InputDeviceConnectionState",
    "InputDeviceIpScheme",
    "InputDeviceScanType",
    "InputDeviceState",
    "InputDeviceTransferType",
    "InputDeviceType",
    "InputFilter",
    "InputLossActionForHlsOut",
    "InputLossActionForMsSmoothOut",
    "InputLossActionForRtmpOut",
    "InputLossActionForUdpOut",
    "InputLossImageType",
    "InputMaximumBitrate",
    "InputPreference",
    "InputResolution",
    "InputSecurityGroupState",
    "InputSourceEndBehavior",
    "InputSourceType",
    "InputState",
    "InputTimecodeSource",
    "InputType",
    "LastFrameClippingBehavior",
    "ListChannelsPaginatorName",
    "ListInputDeviceTransfersPaginatorName",
    "ListInputDevicesPaginatorName",
    "ListInputSecurityGroupsPaginatorName",
    "ListInputsPaginatorName",
    "ListMultiplexProgramsPaginatorName",
    "ListMultiplexesPaginatorName",
    "ListOfferingsPaginatorName",
    "ListReservationsPaginatorName",
    "LogLevel",
    "M2tsAbsentInputAudioBehavior",
    "M2tsArib",
    "M2tsAribCaptionsPidControl",
    "M2tsAudioBufferModel",
    "M2tsAudioInterval",
    "M2tsAudioStreamType",
    "M2tsBufferModel",
    "M2tsCcDescriptor",
    "M2tsEbifControl",
    "M2tsEbpPlacement",
    "M2tsEsRateInPes",
    "M2tsKlv",
    "M2tsNielsenId3Behavior",
    "M2tsPcrControl",
    "M2tsRateMode",
    "M2tsScte35Control",
    "M2tsSegmentationMarkers",
    "M2tsSegmentationStyle",
    "M2tsTimedMetadataBehavior",
    "M3u8NielsenId3Behavior",
    "M3u8PcrControl",
    "M3u8Scte35Behavior",
    "M3u8TimedMetadataBehavior",
    "MotionGraphicsInsertion",
    "Mp2CodingMode",
    "Mpeg2AdaptiveQuantization",
    "Mpeg2ColorMetadata",
    "Mpeg2ColorSpace",
    "Mpeg2DisplayRatio",
    "Mpeg2GopSizeUnits",
    "Mpeg2ScanType",
    "Mpeg2SubGopLength",
    "Mpeg2TimecodeInsertionBehavior",
    "MsSmoothH265PackagingType",
    "MultiplexCreatedWaiterName",
    "MultiplexDeletedWaiterName",
    "MultiplexRunningWaiterName",
    "MultiplexState",
    "MultiplexStoppedWaiterName",
    "NetworkInputServerValidation",
    "NielsenPcmToId3TaggingState",
    "OfferingDurationUnits",
    "OfferingType",
    "PipelineId",
    "PreferredChannelPipeline",
    "ReservationCodec",
    "ReservationMaximumBitrate",
    "ReservationMaximumFramerate",
    "ReservationResolution",
    "ReservationResourceType",
    "ReservationSpecialFeature",
    "ReservationState",
    "ReservationVideoQuality",
    "RtmpAdMarkers",
    "RtmpCacheFullBehavior",
    "RtmpCaptionData",
    "RtmpOutputCertificateMode",
    "S3CannedAcl",
    "Scte20Convert608To708",
    "Scte35AposNoRegionalBlackoutBehavior",
    "Scte35AposWebDeliveryAllowedBehavior",
    "Scte35ArchiveAllowedFlag",
    "Scte35DeviceRestrictions",
    "Scte35NoRegionalBlackoutFlag",
    "Scte35SegmentationCancelIndicator",
    "Scte35SpliceInsertNoRegionalBlackoutBehavior",
    "Scte35SpliceInsertWebDeliveryAllowedBehavior",
    "Scte35WebDeliveryAllowedFlag",
    "SmoothGroupAudioOnlyTimecodeControl",
    "SmoothGroupCertificateMode",
    "SmoothGroupEventIdMode",
    "SmoothGroupEventStopBehavior",
    "SmoothGroupSegmentationMode",
    "SmoothGroupSparseTrackType",
    "SmoothGroupStreamManifestBehavior",
    "SmoothGroupTimestampOffsetMode",
    "Smpte2038DataPreference",
    "TemporalFilterPostFilterSharpening",
    "TemporalFilterStrength",
    "TimecodeConfigSource",
    "TtmlDestinationStyleControl",
    "UdpTimedMetadataId3Frame",
    "VideoDescriptionRespondToAfd",
    "VideoDescriptionScalingBehavior",
    "VideoSelectorColorSpace",
    "VideoSelectorColorSpaceUsage",
    "WavCodingMode",
)


AacCodingMode = Literal[
    "AD_RECEIVER_MIX", "CODING_MODE_1_0", "CODING_MODE_1_1", "CODING_MODE_2_0", "CODING_MODE_5_1"
]
AacInputType = Literal["BROADCASTER_MIXED_AD", "NORMAL"]
AacProfile = Literal["HEV1", "HEV2", "LC"]
AacRateControlMode = Literal["CBR", "VBR"]
AacRawFormat = Literal["LATM_LOAS", "NONE"]
AacSpec = Literal["MPEG2", "MPEG4"]
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
Ac3DrcProfile = Literal["FILM_STANDARD", "NONE"]
Ac3LfeFilter = Literal["DISABLED", "ENABLED"]
Ac3MetadataControl = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AcceptHeader = Literal["image/jpeg"]
AfdSignaling = Literal["AUTO", "FIXED", "NONE"]
AudioDescriptionAudioTypeControl = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AudioDescriptionLanguageCodeControl = Literal["FOLLOW_INPUT", "USE_CONFIGURED"]
AudioLanguageSelectionPolicy = Literal["LOOSE", "STRICT"]
AudioNormalizationAlgorithm = Literal["ITU_1770_1", "ITU_1770_2"]
AudioNormalizationAlgorithmControl = Literal["CORRECT_AUDIO"]
AudioOnlyHlsSegmentType = Literal["AAC", "FMP4"]
AudioOnlyHlsTrackType = Literal[
    "ALTERNATE_AUDIO_AUTO_SELECT",
    "ALTERNATE_AUDIO_AUTO_SELECT_DEFAULT",
    "ALTERNATE_AUDIO_NOT_AUTO_SELECT",
    "AUDIO_ONLY_VARIANT_STREAM",
]
AudioType = Literal["CLEAN_EFFECTS", "HEARING_IMPAIRED", "UNDEFINED", "VISUAL_IMPAIRED_COMMENTARY"]
AuthenticationScheme = Literal["AKAMAI", "COMMON"]
AvailBlankingState = Literal["DISABLED", "ENABLED"]
BlackoutSlateNetworkEndBlackout = Literal["DISABLED", "ENABLED"]
BlackoutSlateState = Literal["DISABLED", "ENABLED"]
BurnInAlignment = Literal["CENTERED", "LEFT", "SMART"]
BurnInBackgroundColor = Literal["BLACK", "NONE", "WHITE"]
BurnInFontColor = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
BurnInOutlineColor = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
BurnInShadowColor = Literal["BLACK", "NONE", "WHITE"]
BurnInTeletextGridControl = Literal["FIXED", "SCALED"]
CdiInputResolution = Literal["FHD", "HD", "SD", "UHD"]
ChannelClass = Literal["SINGLE_PIPELINE", "STANDARD"]
ChannelCreatedWaiterName = Literal["channel_created"]
ChannelDeletedWaiterName = Literal["channel_deleted"]
ChannelRunningWaiterName = Literal["channel_running"]
ChannelState = Literal[
    "CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETING",
    "IDLE",
    "RECOVERING",
    "RUNNING",
    "STARTING",
    "STOPPING",
    "UPDATE_FAILED",
    "UPDATING",
]
ChannelStoppedWaiterName = Literal["channel_stopped"]
ContentType = Literal["image/jpeg"]
DescribeSchedulePaginatorName = Literal["describe_schedule"]
DeviceSettingsSyncState = Literal["SYNCED", "SYNCING"]
DeviceUpdateStatus = Literal["NOT_UP_TO_DATE", "UP_TO_DATE"]
DvbSdtOutputSdt = Literal["SDT_FOLLOW", "SDT_FOLLOW_IF_PRESENT", "SDT_MANUAL", "SDT_NONE"]
DvbSubDestinationAlignment = Literal["CENTERED", "LEFT", "SMART"]
DvbSubDestinationBackgroundColor = Literal["BLACK", "NONE", "WHITE"]
DvbSubDestinationFontColor = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
DvbSubDestinationOutlineColor = Literal["BLACK", "BLUE", "GREEN", "RED", "WHITE", "YELLOW"]
DvbSubDestinationShadowColor = Literal["BLACK", "NONE", "WHITE"]
DvbSubDestinationTeletextGridControl = Literal["FIXED", "SCALED"]
Eac3AttenuationControl = Literal["ATTENUATE_3_DB", "NONE"]
Eac3BitstreamMode = Literal[
    "COMMENTARY", "COMPLETE_MAIN", "EMERGENCY", "HEARING_IMPAIRED", "VISUALLY_IMPAIRED"
]
Eac3CodingMode = Literal["CODING_MODE_1_0", "CODING_MODE_2_0", "CODING_MODE_3_2"]
Eac3DcFilter = Literal["DISABLED", "ENABLED"]
Eac3DrcLine = Literal[
    "FILM_LIGHT", "FILM_STANDARD", "MUSIC_LIGHT", "MUSIC_STANDARD", "NONE", "SPEECH"
]
Eac3DrcRf = Literal[
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
EbuTtDDestinationStyleControl = Literal["EXCLUDE", "INCLUDE"]
EbuTtDFillLineGapControl = Literal["DISABLED", "ENABLED"]
EmbeddedConvert608To708 = Literal["DISABLED", "UPCONVERT"]
EmbeddedScte20Detection = Literal["AUTO", "OFF"]
FeatureActivationsInputPrepareScheduleActions = Literal["DISABLED", "ENABLED"]
FecOutputIncludeFec = Literal["COLUMN", "COLUMN_AND_ROW"]
FixedAfd = Literal[
    "AFD_0000",
    "AFD_0010",
    "AFD_0011",
    "AFD_0100",
    "AFD_1000",
    "AFD_1001",
    "AFD_1010",
    "AFD_1011",
    "AFD_1101",
    "AFD_1110",
    "AFD_1111",
]
Fmp4NielsenId3Behavior = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
Fmp4TimedMetadataBehavior = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
FollowPoint = Literal["END", "START"]
FrameCaptureIntervalUnit = Literal["MILLISECONDS", "SECONDS"]
GlobalConfigurationInputEndAction = Literal["NONE", "SWITCH_AND_LOOP_INPUTS"]
GlobalConfigurationLowFramerateInputs = Literal["DISABLED", "ENABLED"]
GlobalConfigurationOutputLockingMode = Literal["EPOCH_LOCKING", "PIPELINE_LOCKING"]
GlobalConfigurationOutputTimingSource = Literal["INPUT_CLOCK", "SYSTEM_CLOCK"]
H264AdaptiveQuantization = Literal["HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
H264ColorMetadata = Literal["IGNORE", "INSERT"]
H264EntropyEncoding = Literal["CABAC", "CAVLC"]
H264FlickerAq = Literal["DISABLED", "ENABLED"]
H264ForceFieldPictures = Literal["DISABLED", "ENABLED"]
H264FramerateControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H264GopBReference = Literal["DISABLED", "ENABLED"]
H264GopSizeUnits = Literal["FRAMES", "SECONDS"]
H264Level = Literal[
    "H264_LEVEL_1",
    "H264_LEVEL_1_1",
    "H264_LEVEL_1_2",
    "H264_LEVEL_1_3",
    "H264_LEVEL_2",
    "H264_LEVEL_2_1",
    "H264_LEVEL_2_2",
    "H264_LEVEL_3",
    "H264_LEVEL_3_1",
    "H264_LEVEL_3_2",
    "H264_LEVEL_4",
    "H264_LEVEL_4_1",
    "H264_LEVEL_4_2",
    "H264_LEVEL_5",
    "H264_LEVEL_5_1",
    "H264_LEVEL_5_2",
    "H264_LEVEL_AUTO",
]
H264LookAheadRateControl = Literal["HIGH", "LOW", "MEDIUM"]
H264ParControl = Literal["INITIALIZE_FROM_SOURCE", "SPECIFIED"]
H264Profile = Literal["BASELINE", "HIGH", "HIGH_10BIT", "HIGH_422", "HIGH_422_10BIT", "MAIN"]
H264QualityLevel = Literal["ENHANCED_QUALITY", "STANDARD_QUALITY"]
H264RateControlMode = Literal["CBR", "MULTIPLEX", "QVBR", "VBR"]
H264ScanType = Literal["INTERLACED", "PROGRESSIVE"]
H264SceneChangeDetect = Literal["DISABLED", "ENABLED"]
H264SpatialAq = Literal["DISABLED", "ENABLED"]
H264SubGopLength = Literal["DYNAMIC", "FIXED"]
H264Syntax = Literal["DEFAULT", "RP2027"]
H264TemporalAq = Literal["DISABLED", "ENABLED"]
H264TimecodeInsertionBehavior = Literal["DISABLED", "PIC_TIMING_SEI"]
H265AdaptiveQuantization = Literal["HIGH", "HIGHER", "LOW", "MAX", "MEDIUM", "OFF"]
H265AlternativeTransferFunction = Literal["INSERT", "OMIT"]
H265ColorMetadata = Literal["IGNORE", "INSERT"]
H265FlickerAq = Literal["DISABLED", "ENABLED"]
H265GopSizeUnits = Literal["FRAMES", "SECONDS"]
H265Level = Literal[
    "H265_LEVEL_1",
    "H265_LEVEL_2",
    "H265_LEVEL_2_1",
    "H265_LEVEL_3",
    "H265_LEVEL_3_1",
    "H265_LEVEL_4",
    "H265_LEVEL_4_1",
    "H265_LEVEL_5",
    "H265_LEVEL_5_1",
    "H265_LEVEL_5_2",
    "H265_LEVEL_6",
    "H265_LEVEL_6_1",
    "H265_LEVEL_6_2",
    "H265_LEVEL_AUTO",
]
H265LookAheadRateControl = Literal["HIGH", "LOW", "MEDIUM"]
H265Profile = Literal["MAIN", "MAIN_10BIT"]
H265RateControlMode = Literal["CBR", "MULTIPLEX", "QVBR"]
H265ScanType = Literal["INTERLACED", "PROGRESSIVE"]
H265SceneChangeDetect = Literal["DISABLED", "ENABLED"]
H265Tier = Literal["HIGH", "MAIN"]
H265TimecodeInsertionBehavior = Literal["DISABLED", "PIC_TIMING_SEI"]
HlsAdMarkers = Literal["ADOBE", "ELEMENTAL", "ELEMENTAL_SCTE35"]
HlsAkamaiHttpTransferMode = Literal["CHUNKED", "NON_CHUNKED"]
HlsCaptionLanguageSetting = Literal["INSERT", "NONE", "OMIT"]
HlsClientCache = Literal["DISABLED", "ENABLED"]
HlsCodecSpecification = Literal["RFC_4281", "RFC_6381"]
HlsDirectoryStructure = Literal["SINGLE_DIRECTORY", "SUBDIRECTORY_PER_STREAM"]
HlsDiscontinuityTags = Literal["INSERT", "NEVER_INSERT"]
HlsEncryptionType = Literal["AES128", "SAMPLE_AES"]
HlsH265PackagingType = Literal["HEV1", "HVC1"]
HlsId3SegmentTaggingState = Literal["DISABLED", "ENABLED"]
HlsIncompleteSegmentBehavior = Literal["AUTO", "SUPPRESS"]
HlsIvInManifest = Literal["EXCLUDE", "INCLUDE"]
HlsIvSource = Literal["EXPLICIT", "FOLLOWS_SEGMENT_NUMBER"]
HlsManifestCompression = Literal["GZIP", "NONE"]
HlsManifestDurationFormat = Literal["FLOATING_POINT", "INTEGER"]
HlsMediaStoreStorageClass = Literal["TEMPORAL"]
HlsMode = Literal["LIVE", "VOD"]
HlsOutputSelection = Literal[
    "MANIFESTS_AND_SEGMENTS", "SEGMENTS_ONLY", "VARIANT_MANIFESTS_AND_SEGMENTS"
]
HlsProgramDateTime = Literal["EXCLUDE", "INCLUDE"]
HlsRedundantManifest = Literal["DISABLED", "ENABLED"]
HlsSegmentationMode = Literal["USE_INPUT_SEGMENTATION", "USE_SEGMENT_DURATION"]
HlsStreamInfResolution = Literal["EXCLUDE", "INCLUDE"]
HlsTimedMetadataId3Frame = Literal["NONE", "PRIV", "TDRL"]
HlsTsFileMode = Literal["SEGMENTED_FILES", "SINGLE_FILE"]
HlsWebdavHttpTransferMode = Literal["CHUNKED", "NON_CHUNKED"]
IFrameOnlyPlaylistType = Literal["DISABLED", "STANDARD"]
InputAttachedWaiterName = Literal["input_attached"]
InputClass = Literal["SINGLE_PIPELINE", "STANDARD"]
InputCodec = Literal["AVC", "HEVC", "MPEG2"]
InputDeblockFilter = Literal["DISABLED", "ENABLED"]
InputDeletedWaiterName = Literal["input_deleted"]
InputDenoiseFilter = Literal["DISABLED", "ENABLED"]
InputDetachedWaiterName = Literal["input_detached"]
InputDeviceActiveInput = Literal["HDMI", "SDI"]
InputDeviceConfiguredInput = Literal["AUTO", "HDMI", "SDI"]
InputDeviceConnectionState = Literal["CONNECTED", "DISCONNECTED"]
InputDeviceIpScheme = Literal["DHCP", "STATIC"]
InputDeviceScanType = Literal["INTERLACED", "PROGRESSIVE"]
InputDeviceState = Literal["IDLE", "STREAMING"]
InputDeviceTransferType = Literal["INCOMING", "OUTGOING"]
InputDeviceType = Literal["HD"]
InputFilter = Literal["AUTO", "DISABLED", "FORCED"]
InputLossActionForHlsOut = Literal["EMIT_OUTPUT", "PAUSE_OUTPUT"]
InputLossActionForMsSmoothOut = Literal["EMIT_OUTPUT", "PAUSE_OUTPUT"]
InputLossActionForRtmpOut = Literal["EMIT_OUTPUT", "PAUSE_OUTPUT"]
InputLossActionForUdpOut = Literal["DROP_PROGRAM", "DROP_TS", "EMIT_PROGRAM"]
InputLossImageType = Literal["COLOR", "SLATE"]
InputMaximumBitrate = Literal["MAX_10_MBPS", "MAX_20_MBPS", "MAX_50_MBPS"]
InputPreference = Literal["EQUAL_INPUT_PREFERENCE", "PRIMARY_INPUT_PREFERRED"]
InputResolution = Literal["HD", "SD", "UHD"]
InputSecurityGroupState = Literal["DELETED", "IDLE", "IN_USE", "UPDATING"]
InputSourceEndBehavior = Literal["CONTINUE", "LOOP"]
InputSourceType = Literal["DYNAMIC", "STATIC"]
InputState = Literal["ATTACHED", "CREATING", "DELETED", "DELETING", "DETACHED"]
InputTimecodeSource = Literal["EMBEDDED", "ZEROBASED"]
InputType = Literal[
    "AWS_CDI",
    "INPUT_DEVICE",
    "MEDIACONNECT",
    "MP4_FILE",
    "RTMP_PULL",
    "RTMP_PUSH",
    "RTP_PUSH",
    "UDP_PUSH",
    "URL_PULL",
]
LastFrameClippingBehavior = Literal["EXCLUDE_LAST_FRAME", "INCLUDE_LAST_FRAME"]
ListChannelsPaginatorName = Literal["list_channels"]
ListInputDeviceTransfersPaginatorName = Literal["list_input_device_transfers"]
ListInputDevicesPaginatorName = Literal["list_input_devices"]
ListInputSecurityGroupsPaginatorName = Literal["list_input_security_groups"]
ListInputsPaginatorName = Literal["list_inputs"]
ListMultiplexProgramsPaginatorName = Literal["list_multiplex_programs"]
ListMultiplexesPaginatorName = Literal["list_multiplexes"]
ListOfferingsPaginatorName = Literal["list_offerings"]
ListReservationsPaginatorName = Literal["list_reservations"]
LogLevel = Literal["DEBUG", "DISABLED", "ERROR", "INFO", "WARNING"]
M2tsAbsentInputAudioBehavior = Literal["DROP", "ENCODE_SILENCE"]
M2tsArib = Literal["DISABLED", "ENABLED"]
M2tsAribCaptionsPidControl = Literal["AUTO", "USE_CONFIGURED"]
M2tsAudioBufferModel = Literal["ATSC", "DVB"]
M2tsAudioInterval = Literal["VIDEO_AND_FIXED_INTERVALS", "VIDEO_INTERVAL"]
M2tsAudioStreamType = Literal["ATSC", "DVB"]
M2tsBufferModel = Literal["MULTIPLEX", "NONE"]
M2tsCcDescriptor = Literal["DISABLED", "ENABLED"]
M2tsEbifControl = Literal["NONE", "PASSTHROUGH"]
M2tsEbpPlacement = Literal["VIDEO_AND_AUDIO_PIDS", "VIDEO_PID"]
M2tsEsRateInPes = Literal["EXCLUDE", "INCLUDE"]
M2tsKlv = Literal["NONE", "PASSTHROUGH"]
M2tsNielsenId3Behavior = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M2tsPcrControl = Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
M2tsRateMode = Literal["CBR", "VBR"]
M2tsScte35Control = Literal["NONE", "PASSTHROUGH"]
M2tsSegmentationMarkers = Literal[
    "EBP", "EBP_LEGACY", "NONE", "PSI_SEGSTART", "RAI_ADAPT", "RAI_SEGSTART"
]
M2tsSegmentationStyle = Literal["MAINTAIN_CADENCE", "RESET_CADENCE"]
M2tsTimedMetadataBehavior = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M3u8NielsenId3Behavior = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M3u8PcrControl = Literal["CONFIGURED_PCR_PERIOD", "PCR_EVERY_PES_PACKET"]
M3u8Scte35Behavior = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
M3u8TimedMetadataBehavior = Literal["NO_PASSTHROUGH", "PASSTHROUGH"]
MotionGraphicsInsertion = Literal["DISABLED", "ENABLED"]
Mp2CodingMode = Literal["CODING_MODE_1_0", "CODING_MODE_2_0"]
Mpeg2AdaptiveQuantization = Literal["AUTO", "HIGH", "LOW", "MEDIUM", "OFF"]
Mpeg2ColorMetadata = Literal["IGNORE", "INSERT"]
Mpeg2ColorSpace = Literal["AUTO", "PASSTHROUGH"]
Mpeg2DisplayRatio = Literal["DISPLAYRATIO16X9", "DISPLAYRATIO4X3"]
Mpeg2GopSizeUnits = Literal["FRAMES", "SECONDS"]
Mpeg2ScanType = Literal["INTERLACED", "PROGRESSIVE"]
Mpeg2SubGopLength = Literal["DYNAMIC", "FIXED"]
Mpeg2TimecodeInsertionBehavior = Literal["DISABLED", "GOP_TIMECODE"]
MsSmoothH265PackagingType = Literal["HEV1", "HVC1"]
MultiplexCreatedWaiterName = Literal["multiplex_created"]
MultiplexDeletedWaiterName = Literal["multiplex_deleted"]
MultiplexRunningWaiterName = Literal["multiplex_running"]
MultiplexState = Literal[
    "CREATE_FAILED",
    "CREATING",
    "DELETED",
    "DELETING",
    "IDLE",
    "RECOVERING",
    "RUNNING",
    "STARTING",
    "STOPPING",
]
MultiplexStoppedWaiterName = Literal["multiplex_stopped"]
NetworkInputServerValidation = Literal[
    "CHECK_CRYPTOGRAPHY_AND_VALIDATE_NAME", "CHECK_CRYPTOGRAPHY_ONLY"
]
NielsenPcmToId3TaggingState = Literal["DISABLED", "ENABLED"]
OfferingDurationUnits = Literal["MONTHS"]
OfferingType = Literal["NO_UPFRONT"]
PipelineId = Literal["PIPELINE_0", "PIPELINE_1"]
PreferredChannelPipeline = Literal["CURRENTLY_ACTIVE", "PIPELINE_0", "PIPELINE_1"]
ReservationCodec = Literal["AUDIO", "AVC", "HEVC", "LINK", "MPEG2"]
ReservationMaximumBitrate = Literal["MAX_10_MBPS", "MAX_20_MBPS", "MAX_50_MBPS"]
ReservationMaximumFramerate = Literal["MAX_30_FPS", "MAX_60_FPS"]
ReservationResolution = Literal["FHD", "HD", "SD", "UHD"]
ReservationResourceType = Literal["CHANNEL", "INPUT", "MULTIPLEX", "OUTPUT"]
ReservationSpecialFeature = Literal["ADVANCED_AUDIO", "AUDIO_NORMALIZATION"]
ReservationState = Literal["ACTIVE", "CANCELED", "DELETED", "EXPIRED"]
ReservationVideoQuality = Literal["ENHANCED", "PREMIUM", "STANDARD"]
RtmpAdMarkers = Literal["ON_CUE_POINT_SCTE35"]
RtmpCacheFullBehavior = Literal["DISCONNECT_IMMEDIATELY", "WAIT_FOR_SERVER"]
RtmpCaptionData = Literal["ALL", "FIELD1_608", "FIELD1_AND_FIELD2_608"]
RtmpOutputCertificateMode = Literal["SELF_SIGNED", "VERIFY_AUTHENTICITY"]
S3CannedAcl = Literal[
    "AUTHENTICATED_READ", "BUCKET_OWNER_FULL_CONTROL", "BUCKET_OWNER_READ", "PUBLIC_READ"
]
Scte20Convert608To708 = Literal["DISABLED", "UPCONVERT"]
Scte35AposNoRegionalBlackoutBehavior = Literal["FOLLOW", "IGNORE"]
Scte35AposWebDeliveryAllowedBehavior = Literal["FOLLOW", "IGNORE"]
Scte35ArchiveAllowedFlag = Literal["ARCHIVE_ALLOWED", "ARCHIVE_NOT_ALLOWED"]
Scte35DeviceRestrictions = Literal["NONE", "RESTRICT_GROUP0", "RESTRICT_GROUP1", "RESTRICT_GROUP2"]
Scte35NoRegionalBlackoutFlag = Literal["NO_REGIONAL_BLACKOUT", "REGIONAL_BLACKOUT"]
Scte35SegmentationCancelIndicator = Literal[
    "SEGMENTATION_EVENT_CANCELED", "SEGMENTATION_EVENT_NOT_CANCELED"
]
Scte35SpliceInsertNoRegionalBlackoutBehavior = Literal["FOLLOW", "IGNORE"]
Scte35SpliceInsertWebDeliveryAllowedBehavior = Literal["FOLLOW", "IGNORE"]
Scte35WebDeliveryAllowedFlag = Literal["WEB_DELIVERY_ALLOWED", "WEB_DELIVERY_NOT_ALLOWED"]
SmoothGroupAudioOnlyTimecodeControl = Literal["PASSTHROUGH", "USE_CONFIGURED_CLOCK"]
SmoothGroupCertificateMode = Literal["SELF_SIGNED", "VERIFY_AUTHENTICITY"]
SmoothGroupEventIdMode = Literal["NO_EVENT_ID", "USE_CONFIGURED", "USE_TIMESTAMP"]
SmoothGroupEventStopBehavior = Literal["NONE", "SEND_EOS"]
SmoothGroupSegmentationMode = Literal["USE_INPUT_SEGMENTATION", "USE_SEGMENT_DURATION"]
SmoothGroupSparseTrackType = Literal["NONE", "SCTE_35", "SCTE_35_WITHOUT_SEGMENTATION"]
SmoothGroupStreamManifestBehavior = Literal["DO_NOT_SEND", "SEND"]
SmoothGroupTimestampOffsetMode = Literal["USE_CONFIGURED_OFFSET", "USE_EVENT_START_DATE"]
Smpte2038DataPreference = Literal["IGNORE", "PREFER"]
TemporalFilterPostFilterSharpening = Literal["AUTO", "DISABLED", "ENABLED"]
TemporalFilterStrength = Literal[
    "AUTO",
    "STRENGTH_1",
    "STRENGTH_10",
    "STRENGTH_11",
    "STRENGTH_12",
    "STRENGTH_13",
    "STRENGTH_14",
    "STRENGTH_15",
    "STRENGTH_16",
    "STRENGTH_2",
    "STRENGTH_3",
    "STRENGTH_4",
    "STRENGTH_5",
    "STRENGTH_6",
    "STRENGTH_7",
    "STRENGTH_8",
    "STRENGTH_9",
]
TimecodeConfigSource = Literal["EMBEDDED", "SYSTEMCLOCK", "ZEROBASED"]
TtmlDestinationStyleControl = Literal["PASSTHROUGH", "USE_CONFIGURED"]
UdpTimedMetadataId3Frame = Literal["NONE", "PRIV", "TDRL"]
VideoDescriptionRespondToAfd = Literal["NONE", "PASSTHROUGH", "RESPOND"]
VideoDescriptionScalingBehavior = Literal["DEFAULT", "STRETCH_TO_OUTPUT"]
VideoSelectorColorSpace = Literal["FOLLOW", "HDR10", "HLG_2020", "REC_601", "REC_709"]
VideoSelectorColorSpaceUsage = Literal["FALLBACK", "FORCE"]
WavCodingMode = Literal["CODING_MODE_1_0", "CODING_MODE_2_0", "CODING_MODE_4_0", "CODING_MODE_8_0"]
