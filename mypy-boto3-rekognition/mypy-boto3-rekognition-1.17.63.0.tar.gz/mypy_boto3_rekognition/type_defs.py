"""
Type annotations for rekognition service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rekognition.type_defs import AgeRangeTypeDef

    data: AgeRangeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_rekognition.literals import (
    BodyPart,
    ContentClassifier,
    EmotionName,
    GenderType,
    LandmarkType,
    OrientationCorrection,
    ProjectStatus,
    ProjectVersionStatus,
    ProtectiveEquipmentType,
    Reason,
    SegmentType,
    StreamProcessorStatus,
    TechnicalCueType,
    TextTypes,
    VideoJobStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AgeRangeTypeDef",
    "AssetTypeDef",
    "AudioMetadataTypeDef",
    "BeardTypeDef",
    "BoundingBoxTypeDef",
    "CelebrityDetailTypeDef",
    "CelebrityRecognitionTypeDef",
    "CelebrityTypeDef",
    "CompareFacesMatchTypeDef",
    "CompareFacesResponseTypeDef",
    "ComparedFaceTypeDef",
    "ComparedSourceImageFaceTypeDef",
    "ContentModerationDetectionTypeDef",
    "CoversBodyPartTypeDef",
    "CreateCollectionResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateProjectVersionResponseTypeDef",
    "CreateStreamProcessorResponseTypeDef",
    "CustomLabelTypeDef",
    "DeleteCollectionResponseTypeDef",
    "DeleteFacesResponseTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteProjectVersionResponseTypeDef",
    "DescribeCollectionResponseTypeDef",
    "DescribeProjectVersionsResponseTypeDef",
    "DescribeProjectsResponseTypeDef",
    "DescribeStreamProcessorResponseTypeDef",
    "DetectCustomLabelsResponseTypeDef",
    "DetectFacesResponseTypeDef",
    "DetectLabelsResponseTypeDef",
    "DetectModerationLabelsResponseTypeDef",
    "DetectProtectiveEquipmentResponseTypeDef",
    "DetectTextFiltersTypeDef",
    "DetectTextResponseTypeDef",
    "DetectionFilterTypeDef",
    "EmotionTypeDef",
    "EquipmentDetectionTypeDef",
    "EvaluationResultTypeDef",
    "EyeOpenTypeDef",
    "EyeglassesTypeDef",
    "FaceDetailTypeDef",
    "FaceDetectionTypeDef",
    "FaceMatchTypeDef",
    "FaceRecordTypeDef",
    "FaceSearchSettingsTypeDef",
    "FaceTypeDef",
    "GenderTypeDef",
    "GeometryTypeDef",
    "GetCelebrityInfoResponseTypeDef",
    "GetCelebrityRecognitionResponseTypeDef",
    "GetContentModerationResponseTypeDef",
    "GetFaceDetectionResponseTypeDef",
    "GetFaceSearchResponseTypeDef",
    "GetLabelDetectionResponseTypeDef",
    "GetPersonTrackingResponseTypeDef",
    "GetSegmentDetectionResponseTypeDef",
    "GetTextDetectionResponseTypeDef",
    "GroundTruthManifestTypeDef",
    "HumanLoopActivationOutputTypeDef",
    "HumanLoopConfigTypeDef",
    "HumanLoopDataAttributesTypeDef",
    "ImageQualityTypeDef",
    "ImageTypeDef",
    "IndexFacesResponseTypeDef",
    "InstanceTypeDef",
    "KinesisDataStreamTypeDef",
    "KinesisVideoStreamTypeDef",
    "LabelDetectionTypeDef",
    "LabelTypeDef",
    "LandmarkTypeDef",
    "ListCollectionsResponseTypeDef",
    "ListFacesResponseTypeDef",
    "ListStreamProcessorsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModerationLabelTypeDef",
    "MouthOpenTypeDef",
    "MustacheTypeDef",
    "NotificationChannelTypeDef",
    "OutputConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParentTypeDef",
    "PersonDetailTypeDef",
    "PersonDetectionTypeDef",
    "PersonMatchTypeDef",
    "PointTypeDef",
    "PoseTypeDef",
    "ProjectDescriptionTypeDef",
    "ProjectVersionDescriptionTypeDef",
    "ProtectiveEquipmentBodyPartTypeDef",
    "ProtectiveEquipmentPersonTypeDef",
    "ProtectiveEquipmentSummarizationAttributesTypeDef",
    "ProtectiveEquipmentSummaryTypeDef",
    "RecognizeCelebritiesResponseTypeDef",
    "RegionOfInterestTypeDef",
    "ResponseMetadata",
    "S3ObjectTypeDef",
    "SearchFacesByImageResponseTypeDef",
    "SearchFacesResponseTypeDef",
    "SegmentDetectionTypeDef",
    "SegmentTypeInfoTypeDef",
    "ShotSegmentTypeDef",
    "SmileTypeDef",
    "StartCelebrityRecognitionResponseTypeDef",
    "StartContentModerationResponseTypeDef",
    "StartFaceDetectionResponseTypeDef",
    "StartFaceSearchResponseTypeDef",
    "StartLabelDetectionResponseTypeDef",
    "StartPersonTrackingResponseTypeDef",
    "StartProjectVersionResponseTypeDef",
    "StartSegmentDetectionFiltersTypeDef",
    "StartSegmentDetectionResponseTypeDef",
    "StartShotDetectionFilterTypeDef",
    "StartTechnicalCueDetectionFilterTypeDef",
    "StartTextDetectionFiltersTypeDef",
    "StartTextDetectionResponseTypeDef",
    "StopProjectVersionResponseTypeDef",
    "StreamProcessorInputTypeDef",
    "StreamProcessorOutputTypeDef",
    "StreamProcessorSettingsTypeDef",
    "StreamProcessorTypeDef",
    "SummaryTypeDef",
    "SunglassesTypeDef",
    "TechnicalCueSegmentTypeDef",
    "TestingDataResultTypeDef",
    "TestingDataTypeDef",
    "TextDetectionResultTypeDef",
    "TextDetectionTypeDef",
    "TrainingDataResultTypeDef",
    "TrainingDataTypeDef",
    "UnindexedFaceTypeDef",
    "ValidationDataTypeDef",
    "VideoMetadataTypeDef",
    "VideoTypeDef",
    "WaiterConfigTypeDef",
)


class AgeRangeTypeDef(TypedDict, total=False):
    Low: int
    High: int


class AssetTypeDef(TypedDict, total=False):
    GroundTruthManifest: "GroundTruthManifestTypeDef"


class AudioMetadataTypeDef(TypedDict, total=False):
    Codec: str
    DurationMillis: int
    SampleRate: int
    NumberOfChannels: int


class BeardTypeDef(TypedDict, total=False):
    Value: bool
    Confidence: float


class BoundingBoxTypeDef(TypedDict, total=False):
    Width: float
    Height: float
    Left: float
    Top: float


class CelebrityDetailTypeDef(TypedDict, total=False):
    Urls: List[str]
    Name: str
    Id: str
    Confidence: float
    BoundingBox: "BoundingBoxTypeDef"
    Face: "FaceDetailTypeDef"


class CelebrityRecognitionTypeDef(TypedDict, total=False):
    Timestamp: int
    Celebrity: "CelebrityDetailTypeDef"


class CelebrityTypeDef(TypedDict, total=False):
    Urls: List[str]
    Name: str
    Id: str
    Face: "ComparedFaceTypeDef"
    MatchConfidence: float


class CompareFacesMatchTypeDef(TypedDict, total=False):
    Similarity: float
    Face: "ComparedFaceTypeDef"


class CompareFacesResponseTypeDef(TypedDict, total=False):
    SourceImageFace: "ComparedSourceImageFaceTypeDef"
    FaceMatches: List["CompareFacesMatchTypeDef"]
    UnmatchedFaces: List["ComparedFaceTypeDef"]
    SourceImageOrientationCorrection: OrientationCorrection
    TargetImageOrientationCorrection: OrientationCorrection


class ComparedFaceTypeDef(TypedDict, total=False):
    BoundingBox: "BoundingBoxTypeDef"
    Confidence: float
    Landmarks: List["LandmarkTypeDef"]
    Pose: "PoseTypeDef"
    Quality: "ImageQualityTypeDef"


class ComparedSourceImageFaceTypeDef(TypedDict, total=False):
    BoundingBox: "BoundingBoxTypeDef"
    Confidence: float


class ContentModerationDetectionTypeDef(TypedDict, total=False):
    Timestamp: int
    ModerationLabel: "ModerationLabelTypeDef"


class CoversBodyPartTypeDef(TypedDict, total=False):
    Confidence: float
    Value: bool


class CreateCollectionResponseTypeDef(TypedDict, total=False):
    StatusCode: int
    CollectionArn: str
    FaceModelVersion: str


class CreateProjectResponseTypeDef(TypedDict, total=False):
    ProjectArn: str


class CreateProjectVersionResponseTypeDef(TypedDict, total=False):
    ProjectVersionArn: str


class CreateStreamProcessorResponseTypeDef(TypedDict, total=False):
    StreamProcessorArn: str


class CustomLabelTypeDef(TypedDict, total=False):
    Name: str
    Confidence: float
    Geometry: "GeometryTypeDef"


class DeleteCollectionResponseTypeDef(TypedDict, total=False):
    StatusCode: int


class DeleteFacesResponseTypeDef(TypedDict, total=False):
    DeletedFaces: List[str]


class DeleteProjectResponseTypeDef(TypedDict, total=False):
    Status: ProjectStatus


class DeleteProjectVersionResponseTypeDef(TypedDict, total=False):
    Status: ProjectVersionStatus


class DescribeCollectionResponseTypeDef(TypedDict, total=False):
    FaceCount: int
    FaceModelVersion: str
    CollectionARN: str
    CreationTimestamp: datetime


class DescribeProjectVersionsResponseTypeDef(TypedDict, total=False):
    ProjectVersionDescriptions: List["ProjectVersionDescriptionTypeDef"]
    NextToken: str


class DescribeProjectsResponseTypeDef(TypedDict, total=False):
    ProjectDescriptions: List["ProjectDescriptionTypeDef"]
    NextToken: str


class DescribeStreamProcessorResponseTypeDef(TypedDict, total=False):
    Name: str
    StreamProcessorArn: str
    Status: StreamProcessorStatus
    StatusMessage: str
    CreationTimestamp: datetime
    LastUpdateTimestamp: datetime
    Input: "StreamProcessorInputTypeDef"
    Output: "StreamProcessorOutputTypeDef"
    RoleArn: str
    Settings: "StreamProcessorSettingsTypeDef"


class DetectCustomLabelsResponseTypeDef(TypedDict, total=False):
    CustomLabels: List["CustomLabelTypeDef"]


class DetectFacesResponseTypeDef(TypedDict, total=False):
    FaceDetails: List["FaceDetailTypeDef"]
    OrientationCorrection: OrientationCorrection


class DetectLabelsResponseTypeDef(TypedDict, total=False):
    Labels: List["LabelTypeDef"]
    OrientationCorrection: OrientationCorrection
    LabelModelVersion: str


class DetectModerationLabelsResponseTypeDef(TypedDict, total=False):
    ModerationLabels: List["ModerationLabelTypeDef"]
    ModerationModelVersion: str
    HumanLoopActivationOutput: "HumanLoopActivationOutputTypeDef"


class DetectProtectiveEquipmentResponseTypeDef(TypedDict, total=False):
    ProtectiveEquipmentModelVersion: str
    Persons: List["ProtectiveEquipmentPersonTypeDef"]
    Summary: "ProtectiveEquipmentSummaryTypeDef"


class DetectTextFiltersTypeDef(TypedDict, total=False):
    WordFilter: "DetectionFilterTypeDef"
    RegionsOfInterest: List["RegionOfInterestTypeDef"]


class DetectTextResponseTypeDef(TypedDict, total=False):
    TextDetections: List["TextDetectionTypeDef"]
    TextModelVersion: str


class DetectionFilterTypeDef(TypedDict, total=False):
    MinConfidence: float
    MinBoundingBoxHeight: float
    MinBoundingBoxWidth: float


EmotionTypeDef = TypedDict(
    "EmotionTypeDef", {"Type": EmotionName, "Confidence": float}, total=False
)

EquipmentDetectionTypeDef = TypedDict(
    "EquipmentDetectionTypeDef",
    {
        "BoundingBox": "BoundingBoxTypeDef",
        "Confidence": float,
        "Type": ProtectiveEquipmentType,
        "CoversBodyPart": "CoversBodyPartTypeDef",
    },
    total=False,
)


class EvaluationResultTypeDef(TypedDict, total=False):
    F1Score: float
    Summary: "SummaryTypeDef"


class EyeOpenTypeDef(TypedDict, total=False):
    Value: bool
    Confidence: float


class EyeglassesTypeDef(TypedDict, total=False):
    Value: bool
    Confidence: float


class FaceDetailTypeDef(TypedDict, total=False):
    BoundingBox: "BoundingBoxTypeDef"
    AgeRange: "AgeRangeTypeDef"
    Smile: "SmileTypeDef"
    Eyeglasses: "EyeglassesTypeDef"
    Sunglasses: "SunglassesTypeDef"
    Gender: "GenderTypeDef"
    Beard: "BeardTypeDef"
    Mustache: "MustacheTypeDef"
    EyesOpen: "EyeOpenTypeDef"
    MouthOpen: "MouthOpenTypeDef"
    Emotions: List["EmotionTypeDef"]
    Landmarks: List["LandmarkTypeDef"]
    Pose: "PoseTypeDef"
    Quality: "ImageQualityTypeDef"
    Confidence: float


class FaceDetectionTypeDef(TypedDict, total=False):
    Timestamp: int
    Face: "FaceDetailTypeDef"


class FaceMatchTypeDef(TypedDict, total=False):
    Similarity: float
    Face: "FaceTypeDef"


class FaceRecordTypeDef(TypedDict, total=False):
    Face: "FaceTypeDef"
    FaceDetail: "FaceDetailTypeDef"


class FaceSearchSettingsTypeDef(TypedDict, total=False):
    CollectionId: str
    FaceMatchThreshold: float


class FaceTypeDef(TypedDict, total=False):
    FaceId: str
    BoundingBox: "BoundingBoxTypeDef"
    ImageId: str
    ExternalImageId: str
    Confidence: float


class GenderTypeDef(TypedDict, total=False):
    Value: GenderType
    Confidence: float


class GeometryTypeDef(TypedDict, total=False):
    BoundingBox: "BoundingBoxTypeDef"
    Polygon: List["PointTypeDef"]


class GetCelebrityInfoResponseTypeDef(TypedDict, total=False):
    Urls: List[str]
    Name: str


class GetCelebrityRecognitionResponseTypeDef(TypedDict, total=False):
    JobStatus: VideoJobStatus
    StatusMessage: str
    VideoMetadata: "VideoMetadataTypeDef"
    NextToken: str
    Celebrities: List["CelebrityRecognitionTypeDef"]


class GetContentModerationResponseTypeDef(TypedDict, total=False):
    JobStatus: VideoJobStatus
    StatusMessage: str
    VideoMetadata: "VideoMetadataTypeDef"
    ModerationLabels: List["ContentModerationDetectionTypeDef"]
    NextToken: str
    ModerationModelVersion: str


class GetFaceDetectionResponseTypeDef(TypedDict, total=False):
    JobStatus: VideoJobStatus
    StatusMessage: str
    VideoMetadata: "VideoMetadataTypeDef"
    NextToken: str
    Faces: List["FaceDetectionTypeDef"]


class GetFaceSearchResponseTypeDef(TypedDict, total=False):
    JobStatus: VideoJobStatus
    StatusMessage: str
    NextToken: str
    VideoMetadata: "VideoMetadataTypeDef"
    Persons: List["PersonMatchTypeDef"]


class GetLabelDetectionResponseTypeDef(TypedDict, total=False):
    JobStatus: VideoJobStatus
    StatusMessage: str
    VideoMetadata: "VideoMetadataTypeDef"
    NextToken: str
    Labels: List["LabelDetectionTypeDef"]
    LabelModelVersion: str


class GetPersonTrackingResponseTypeDef(TypedDict, total=False):
    JobStatus: VideoJobStatus
    StatusMessage: str
    VideoMetadata: "VideoMetadataTypeDef"
    NextToken: str
    Persons: List["PersonDetectionTypeDef"]


class GetSegmentDetectionResponseTypeDef(TypedDict, total=False):
    JobStatus: VideoJobStatus
    StatusMessage: str
    VideoMetadata: List["VideoMetadataTypeDef"]
    AudioMetadata: List["AudioMetadataTypeDef"]
    NextToken: str
    Segments: List["SegmentDetectionTypeDef"]
    SelectedSegmentTypes: List["SegmentTypeInfoTypeDef"]


class GetTextDetectionResponseTypeDef(TypedDict, total=False):
    JobStatus: VideoJobStatus
    StatusMessage: str
    VideoMetadata: "VideoMetadataTypeDef"
    TextDetections: List["TextDetectionResultTypeDef"]
    NextToken: str
    TextModelVersion: str


class GroundTruthManifestTypeDef(TypedDict, total=False):
    S3Object: "S3ObjectTypeDef"


class HumanLoopActivationOutputTypeDef(TypedDict):
    HumanLoopArn: str
    HumanLoopActivationReasons: List[str]
    HumanLoopActivationConditionsEvaluationResults: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredHumanLoopConfigTypeDef(TypedDict):
    HumanLoopName: str
    FlowDefinitionArn: str


class HumanLoopConfigTypeDef(_RequiredHumanLoopConfigTypeDef, total=False):
    DataAttributes: "HumanLoopDataAttributesTypeDef"


class HumanLoopDataAttributesTypeDef(TypedDict, total=False):
    ContentClassifiers: List[ContentClassifier]


class ImageQualityTypeDef(TypedDict, total=False):
    Brightness: float
    Sharpness: float


class ImageTypeDef(TypedDict, total=False):
    Bytes: Union[bytes, IO[bytes]]
    S3Object: "S3ObjectTypeDef"


class IndexFacesResponseTypeDef(TypedDict, total=False):
    FaceRecords: List["FaceRecordTypeDef"]
    OrientationCorrection: OrientationCorrection
    FaceModelVersion: str
    UnindexedFaces: List["UnindexedFaceTypeDef"]


class InstanceTypeDef(TypedDict, total=False):
    BoundingBox: "BoundingBoxTypeDef"
    Confidence: float


class KinesisDataStreamTypeDef(TypedDict, total=False):
    Arn: str


class KinesisVideoStreamTypeDef(TypedDict, total=False):
    Arn: str


class LabelDetectionTypeDef(TypedDict, total=False):
    Timestamp: int
    Label: "LabelTypeDef"


class LabelTypeDef(TypedDict, total=False):
    Name: str
    Confidence: float
    Instances: List["InstanceTypeDef"]
    Parents: List["ParentTypeDef"]


LandmarkTypeDef = TypedDict(
    "LandmarkTypeDef", {"Type": LandmarkType, "X": float, "Y": float}, total=False
)


class ListCollectionsResponseTypeDef(TypedDict, total=False):
    CollectionIds: List[str]
    NextToken: str
    FaceModelVersions: List[str]


class ListFacesResponseTypeDef(TypedDict, total=False):
    Faces: List["FaceTypeDef"]
    NextToken: str
    FaceModelVersion: str


class ListStreamProcessorsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    StreamProcessors: List["StreamProcessorTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class ModerationLabelTypeDef(TypedDict, total=False):
    Confidence: float
    Name: str
    ParentName: str


class MouthOpenTypeDef(TypedDict, total=False):
    Value: bool
    Confidence: float


class MustacheTypeDef(TypedDict, total=False):
    Value: bool
    Confidence: float


class NotificationChannelTypeDef(TypedDict):
    SNSTopicArn: str
    RoleArn: str


class OutputConfigTypeDef(TypedDict, total=False):
    S3Bucket: str
    S3KeyPrefix: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParentTypeDef(TypedDict, total=False):
    Name: str


class PersonDetailTypeDef(TypedDict, total=False):
    Index: int
    BoundingBox: "BoundingBoxTypeDef"
    Face: "FaceDetailTypeDef"


class PersonDetectionTypeDef(TypedDict, total=False):
    Timestamp: int
    Person: "PersonDetailTypeDef"


class PersonMatchTypeDef(TypedDict, total=False):
    Timestamp: int
    Person: "PersonDetailTypeDef"
    FaceMatches: List["FaceMatchTypeDef"]


class PointTypeDef(TypedDict, total=False):
    X: float
    Y: float


class PoseTypeDef(TypedDict, total=False):
    Roll: float
    Yaw: float
    Pitch: float


class ProjectDescriptionTypeDef(TypedDict, total=False):
    ProjectArn: str
    CreationTimestamp: datetime
    Status: ProjectStatus


class ProjectVersionDescriptionTypeDef(TypedDict, total=False):
    ProjectVersionArn: str
    CreationTimestamp: datetime
    MinInferenceUnits: int
    Status: ProjectVersionStatus
    StatusMessage: str
    BillableTrainingTimeInSeconds: int
    TrainingEndTimestamp: datetime
    OutputConfig: "OutputConfigTypeDef"
    TrainingDataResult: "TrainingDataResultTypeDef"
    TestingDataResult: "TestingDataResultTypeDef"
    EvaluationResult: "EvaluationResultTypeDef"
    ManifestSummary: "GroundTruthManifestTypeDef"


class ProtectiveEquipmentBodyPartTypeDef(TypedDict, total=False):
    Name: BodyPart
    Confidence: float
    EquipmentDetections: List["EquipmentDetectionTypeDef"]


class ProtectiveEquipmentPersonTypeDef(TypedDict, total=False):
    BodyParts: List["ProtectiveEquipmentBodyPartTypeDef"]
    BoundingBox: "BoundingBoxTypeDef"
    Confidence: float
    Id: int


class ProtectiveEquipmentSummarizationAttributesTypeDef(TypedDict):
    MinConfidence: float
    RequiredEquipmentTypes: List[ProtectiveEquipmentType]


class ProtectiveEquipmentSummaryTypeDef(TypedDict, total=False):
    PersonsWithRequiredEquipment: List[int]
    PersonsWithoutRequiredEquipment: List[int]
    PersonsIndeterminate: List[int]


class RecognizeCelebritiesResponseTypeDef(TypedDict, total=False):
    CelebrityFaces: List["CelebrityTypeDef"]
    UnrecognizedFaces: List["ComparedFaceTypeDef"]
    OrientationCorrection: OrientationCorrection


class RegionOfInterestTypeDef(TypedDict, total=False):
    BoundingBox: "BoundingBoxTypeDef"


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class S3ObjectTypeDef(TypedDict, total=False):
    Bucket: str
    Name: str
    Version: str


class SearchFacesByImageResponseTypeDef(TypedDict, total=False):
    SearchedFaceBoundingBox: "BoundingBoxTypeDef"
    SearchedFaceConfidence: float
    FaceMatches: List["FaceMatchTypeDef"]
    FaceModelVersion: str


class SearchFacesResponseTypeDef(TypedDict, total=False):
    SearchedFaceId: str
    FaceMatches: List["FaceMatchTypeDef"]
    FaceModelVersion: str


SegmentDetectionTypeDef = TypedDict(
    "SegmentDetectionTypeDef",
    {
        "Type": SegmentType,
        "StartTimestampMillis": int,
        "EndTimestampMillis": int,
        "DurationMillis": int,
        "StartTimecodeSMPTE": str,
        "EndTimecodeSMPTE": str,
        "DurationSMPTE": str,
        "TechnicalCueSegment": "TechnicalCueSegmentTypeDef",
        "ShotSegment": "ShotSegmentTypeDef",
    },
    total=False,
)

SegmentTypeInfoTypeDef = TypedDict(
    "SegmentTypeInfoTypeDef", {"Type": SegmentType, "ModelVersion": str}, total=False
)


class ShotSegmentTypeDef(TypedDict, total=False):
    Index: int
    Confidence: float


class SmileTypeDef(TypedDict, total=False):
    Value: bool
    Confidence: float


class StartCelebrityRecognitionResponseTypeDef(TypedDict, total=False):
    JobId: str


class StartContentModerationResponseTypeDef(TypedDict, total=False):
    JobId: str


class StartFaceDetectionResponseTypeDef(TypedDict, total=False):
    JobId: str


class StartFaceSearchResponseTypeDef(TypedDict, total=False):
    JobId: str


class StartLabelDetectionResponseTypeDef(TypedDict, total=False):
    JobId: str


class StartPersonTrackingResponseTypeDef(TypedDict, total=False):
    JobId: str


class StartProjectVersionResponseTypeDef(TypedDict, total=False):
    Status: ProjectVersionStatus


class StartSegmentDetectionFiltersTypeDef(TypedDict, total=False):
    TechnicalCueFilter: "StartTechnicalCueDetectionFilterTypeDef"
    ShotFilter: "StartShotDetectionFilterTypeDef"


class StartSegmentDetectionResponseTypeDef(TypedDict, total=False):
    JobId: str


class StartShotDetectionFilterTypeDef(TypedDict, total=False):
    MinSegmentConfidence: float


class StartTechnicalCueDetectionFilterTypeDef(TypedDict, total=False):
    MinSegmentConfidence: float


class StartTextDetectionFiltersTypeDef(TypedDict, total=False):
    WordFilter: "DetectionFilterTypeDef"
    RegionsOfInterest: List["RegionOfInterestTypeDef"]


class StartTextDetectionResponseTypeDef(TypedDict, total=False):
    JobId: str


class StopProjectVersionResponseTypeDef(TypedDict, total=False):
    Status: ProjectVersionStatus


class StreamProcessorInputTypeDef(TypedDict, total=False):
    KinesisVideoStream: "KinesisVideoStreamTypeDef"


class StreamProcessorOutputTypeDef(TypedDict):
    KinesisDataStream: "KinesisDataStreamTypeDef"
    ResponseMetadata: "ResponseMetadata"


class StreamProcessorSettingsTypeDef(TypedDict, total=False):
    FaceSearch: "FaceSearchSettingsTypeDef"


class StreamProcessorTypeDef(TypedDict, total=False):
    Name: str
    Status: StreamProcessorStatus


class SummaryTypeDef(TypedDict, total=False):
    S3Object: "S3ObjectTypeDef"


class SunglassesTypeDef(TypedDict, total=False):
    Value: bool
    Confidence: float


TechnicalCueSegmentTypeDef = TypedDict(
    "TechnicalCueSegmentTypeDef", {"Type": TechnicalCueType, "Confidence": float}, total=False
)


class TestingDataResultTypeDef(TypedDict, total=False):
    Input: "TestingDataTypeDef"
    Output: "TestingDataTypeDef"
    Validation: "ValidationDataTypeDef"


class TestingDataTypeDef(TypedDict, total=False):
    Assets: List["AssetTypeDef"]
    AutoCreate: bool


class TextDetectionResultTypeDef(TypedDict, total=False):
    Timestamp: int
    TextDetection: "TextDetectionTypeDef"


TextDetectionTypeDef = TypedDict(
    "TextDetectionTypeDef",
    {
        "DetectedText": str,
        "Type": TextTypes,
        "Id": int,
        "ParentId": int,
        "Confidence": float,
        "Geometry": "GeometryTypeDef",
    },
    total=False,
)


class TrainingDataResultTypeDef(TypedDict, total=False):
    Input: "TrainingDataTypeDef"
    Output: "TrainingDataTypeDef"
    Validation: "ValidationDataTypeDef"


class TrainingDataTypeDef(TypedDict, total=False):
    Assets: List["AssetTypeDef"]


class UnindexedFaceTypeDef(TypedDict, total=False):
    Reasons: List[Reason]
    FaceDetail: "FaceDetailTypeDef"


class ValidationDataTypeDef(TypedDict, total=False):
    Assets: List["AssetTypeDef"]


class VideoMetadataTypeDef(TypedDict, total=False):
    Codec: str
    DurationMillis: int
    Format: str
    FrameRate: float
    FrameHeight: int
    FrameWidth: int


class VideoTypeDef(TypedDict, total=False):
    S3Object: "S3ObjectTypeDef"


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
