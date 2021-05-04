"""
Type annotations for elastictranscoder service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastictranscoder/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elastictranscoder.type_defs import ArtworkTypeDef

    data: ArtworkTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArtworkTypeDef",
    "AudioCodecOptionsTypeDef",
    "AudioParametersTypeDef",
    "CaptionFormatTypeDef",
    "CaptionSourceTypeDef",
    "CaptionsTypeDef",
    "ClipTypeDef",
    "CreateJobOutputTypeDef",
    "CreateJobPlaylistTypeDef",
    "CreateJobResponseTypeDef",
    "CreatePipelineResponseTypeDef",
    "CreatePresetResponseTypeDef",
    "DetectedPropertiesTypeDef",
    "EncryptionTypeDef",
    "HlsContentProtectionTypeDef",
    "InputCaptionsTypeDef",
    "JobAlbumArtTypeDef",
    "JobInputTypeDef",
    "JobOutputTypeDef",
    "JobTypeDef",
    "JobWatermarkTypeDef",
    "ListJobsByPipelineResponseTypeDef",
    "ListJobsByStatusResponseTypeDef",
    "ListPipelinesResponseTypeDef",
    "ListPresetsResponseTypeDef",
    "NotificationsTypeDef",
    "PaginatorConfigTypeDef",
    "PermissionTypeDef",
    "PipelineOutputConfigTypeDef",
    "PipelineTypeDef",
    "PlayReadyDrmTypeDef",
    "PlaylistTypeDef",
    "PresetTypeDef",
    "PresetWatermarkTypeDef",
    "ReadJobResponseTypeDef",
    "ReadPipelineResponseTypeDef",
    "ReadPresetResponseTypeDef",
    "ResponseMetadata",
    "TestRoleResponseTypeDef",
    "ThumbnailsTypeDef",
    "TimeSpanTypeDef",
    "TimingTypeDef",
    "UpdatePipelineNotificationsResponseTypeDef",
    "UpdatePipelineResponseTypeDef",
    "UpdatePipelineStatusResponseTypeDef",
    "VideoParametersTypeDef",
    "WaiterConfigTypeDef",
    "WarningTypeDef",
)


class ArtworkTypeDef(TypedDict, total=False):
    InputKey: str
    MaxWidth: str
    MaxHeight: str
    SizingPolicy: str
    PaddingPolicy: str
    AlbumArtFormat: str
    Encryption: "EncryptionTypeDef"


class AudioCodecOptionsTypeDef(TypedDict, total=False):
    Profile: str
    BitDepth: str
    BitOrder: str
    Signed: str


class AudioParametersTypeDef(TypedDict, total=False):
    Codec: str
    SampleRate: str
    BitRate: str
    Channels: str
    AudioPackingMode: str
    CodecOptions: "AudioCodecOptionsTypeDef"


CaptionFormatTypeDef = TypedDict(
    "CaptionFormatTypeDef",
    {"Format": str, "Pattern": str, "Encryption": "EncryptionTypeDef"},
    total=False,
)


class CaptionSourceTypeDef(TypedDict, total=False):
    Key: str
    Language: str
    TimeOffset: str
    Label: str
    Encryption: "EncryptionTypeDef"


class CaptionsTypeDef(TypedDict, total=False):
    MergePolicy: str
    CaptionSources: List["CaptionSourceTypeDef"]
    CaptionFormats: List["CaptionFormatTypeDef"]


class ClipTypeDef(TypedDict, total=False):
    TimeSpan: "TimeSpanTypeDef"


class CreateJobOutputTypeDef(TypedDict):
    Key: str
    ThumbnailPattern: str
    ThumbnailEncryption: "EncryptionTypeDef"
    Rotate: str
    PresetId: str
    SegmentDuration: str
    Watermarks: List["JobWatermarkTypeDef"]
    AlbumArt: "JobAlbumArtTypeDef"
    Composition: List["ClipTypeDef"]
    Captions: "CaptionsTypeDef"
    Encryption: "EncryptionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateJobPlaylistTypeDef(TypedDict, total=False):
    Name: str
    Format: str
    OutputKeys: List[str]
    HlsContentProtection: "HlsContentProtectionTypeDef"
    PlayReadyDrm: "PlayReadyDrmTypeDef"


class CreateJobResponseTypeDef(TypedDict, total=False):
    Job: "JobTypeDef"


class CreatePipelineResponseTypeDef(TypedDict, total=False):
    Pipeline: "PipelineTypeDef"
    Warnings: List["WarningTypeDef"]


CreatePresetResponseTypeDef = TypedDict(
    "CreatePresetResponseTypeDef", {"Preset": "PresetTypeDef", "Warning": str}, total=False
)


class DetectedPropertiesTypeDef(TypedDict, total=False):
    Width: int
    Height: int
    FrameRate: str
    FileSize: int
    DurationMillis: int


class EncryptionTypeDef(TypedDict, total=False):
    Mode: str
    Key: str
    KeyMd5: str
    InitializationVector: str


class HlsContentProtectionTypeDef(TypedDict, total=False):
    Method: str
    Key: str
    KeyMd5: str
    InitializationVector: str
    LicenseAcquisitionUrl: str
    KeyStoragePolicy: str


class InputCaptionsTypeDef(TypedDict, total=False):
    MergePolicy: str
    CaptionSources: List["CaptionSourceTypeDef"]


class JobAlbumArtTypeDef(TypedDict, total=False):
    MergePolicy: str
    Artwork: List["ArtworkTypeDef"]


JobInputTypeDef = TypedDict(
    "JobInputTypeDef",
    {
        "Key": str,
        "FrameRate": str,
        "Resolution": str,
        "AspectRatio": str,
        "Interlaced": str,
        "Container": str,
        "Encryption": "EncryptionTypeDef",
        "TimeSpan": "TimeSpanTypeDef",
        "InputCaptions": "InputCaptionsTypeDef",
        "DetectedProperties": "DetectedPropertiesTypeDef",
    },
    total=False,
)


class JobOutputTypeDef(TypedDict):
    Id: str
    Key: str
    ThumbnailPattern: str
    ThumbnailEncryption: "EncryptionTypeDef"
    Rotate: str
    PresetId: str
    SegmentDuration: str
    Status: str
    StatusDetail: str
    Duration: int
    Width: int
    Height: int
    FrameRate: str
    FileSize: int
    DurationMillis: int
    Watermarks: List["JobWatermarkTypeDef"]
    AlbumArt: "JobAlbumArtTypeDef"
    Composition: List["ClipTypeDef"]
    Captions: "CaptionsTypeDef"
    Encryption: "EncryptionTypeDef"
    AppliedColorSpaceConversion: str
    ResponseMetadata: "ResponseMetadata"


class JobTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    PipelineId: str
    Input: "JobInputTypeDef"
    Inputs: List["JobInputTypeDef"]
    Output: "JobOutputTypeDef"
    Outputs: List["JobOutputTypeDef"]
    OutputKeyPrefix: str
    Playlists: List["PlaylistTypeDef"]
    Status: str
    UserMetadata: Dict[str, str]
    Timing: "TimingTypeDef"


class JobWatermarkTypeDef(TypedDict, total=False):
    PresetWatermarkId: str
    InputKey: str
    Encryption: "EncryptionTypeDef"


class ListJobsByPipelineResponseTypeDef(TypedDict, total=False):
    Jobs: List["JobTypeDef"]
    NextPageToken: str


class ListJobsByStatusResponseTypeDef(TypedDict, total=False):
    Jobs: List["JobTypeDef"]
    NextPageToken: str


class ListPipelinesResponseTypeDef(TypedDict, total=False):
    Pipelines: List["PipelineTypeDef"]
    NextPageToken: str


class ListPresetsResponseTypeDef(TypedDict, total=False):
    Presets: List["PresetTypeDef"]
    NextPageToken: str


NotificationsTypeDef = TypedDict(
    "NotificationsTypeDef",
    {"Progressing": str, "Completed": str, "Warning": str, "Error": str},
    total=False,
)


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PermissionTypeDef(TypedDict, total=False):
    GranteeType: str
    Grantee: str
    Access: List[str]


class PipelineOutputConfigTypeDef(TypedDict, total=False):
    Bucket: str
    StorageClass: str
    Permissions: List["PermissionTypeDef"]


class PipelineTypeDef(TypedDict, total=False):
    Id: str
    Arn: str
    Name: str
    Status: str
    InputBucket: str
    OutputBucket: str
    Role: str
    AwsKmsKeyArn: str
    Notifications: "NotificationsTypeDef"
    ContentConfig: "PipelineOutputConfigTypeDef"
    ThumbnailConfig: "PipelineOutputConfigTypeDef"


class PlayReadyDrmTypeDef(TypedDict, total=False):
    Format: str
    Key: str
    KeyMd5: str
    KeyId: str
    InitializationVector: str
    LicenseAcquisitionUrl: str


class PlaylistTypeDef(TypedDict, total=False):
    Name: str
    Format: str
    OutputKeys: List[str]
    HlsContentProtection: "HlsContentProtectionTypeDef"
    PlayReadyDrm: "PlayReadyDrmTypeDef"
    Status: str
    StatusDetail: str


PresetTypeDef = TypedDict(
    "PresetTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
        "Description": str,
        "Container": str,
        "Audio": "AudioParametersTypeDef",
        "Video": "VideoParametersTypeDef",
        "Thumbnails": "ThumbnailsTypeDef",
        "Type": str,
    },
    total=False,
)


class PresetWatermarkTypeDef(TypedDict, total=False):
    Id: str
    MaxWidth: str
    MaxHeight: str
    SizingPolicy: str
    HorizontalAlign: str
    HorizontalOffset: str
    VerticalAlign: str
    VerticalOffset: str
    Opacity: str
    Target: str


class ReadJobResponseTypeDef(TypedDict, total=False):
    Job: "JobTypeDef"


class ReadPipelineResponseTypeDef(TypedDict, total=False):
    Pipeline: "PipelineTypeDef"
    Warnings: List["WarningTypeDef"]


class ReadPresetResponseTypeDef(TypedDict, total=False):
    Preset: "PresetTypeDef"


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class TestRoleResponseTypeDef(TypedDict, total=False):
    Success: str
    Messages: List[str]


class ThumbnailsTypeDef(TypedDict, total=False):
    Format: str
    Interval: str
    Resolution: str
    AspectRatio: str
    MaxWidth: str
    MaxHeight: str
    SizingPolicy: str
    PaddingPolicy: str


class TimeSpanTypeDef(TypedDict, total=False):
    StartTime: str
    Duration: str


class TimingTypeDef(TypedDict, total=False):
    SubmitTimeMillis: int
    StartTimeMillis: int
    FinishTimeMillis: int


class UpdatePipelineNotificationsResponseTypeDef(TypedDict, total=False):
    Pipeline: "PipelineTypeDef"


class UpdatePipelineResponseTypeDef(TypedDict, total=False):
    Pipeline: "PipelineTypeDef"
    Warnings: List["WarningTypeDef"]


class UpdatePipelineStatusResponseTypeDef(TypedDict, total=False):
    Pipeline: "PipelineTypeDef"


class VideoParametersTypeDef(TypedDict, total=False):
    Codec: str
    CodecOptions: Dict[str, str]
    KeyframesMaxDist: str
    FixedGOP: str
    BitRate: str
    FrameRate: str
    MaxFrameRate: str
    Resolution: str
    AspectRatio: str
    MaxWidth: str
    MaxHeight: str
    DisplayAspectRatio: str
    SizingPolicy: str
    PaddingPolicy: str
    Watermarks: List["PresetWatermarkTypeDef"]


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int


class WarningTypeDef(TypedDict, total=False):
    Code: str
    Message: str
