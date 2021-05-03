"""
Type annotations for rekognition service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rekognition/literals.html)

Usage::

    ```python
    from mypy_boto3_rekognition.literals import Attribute

    data: Attribute = "ALL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "Attribute",
    "BodyPart",
    "CelebrityRecognitionSortBy",
    "ContentClassifier",
    "ContentModerationSortBy",
    "DescribeProjectVersionsPaginatorName",
    "DescribeProjectsPaginatorName",
    "EmotionName",
    "FaceAttributes",
    "FaceSearchSortBy",
    "GenderType",
    "LabelDetectionSortBy",
    "LandmarkType",
    "ListCollectionsPaginatorName",
    "ListFacesPaginatorName",
    "ListStreamProcessorsPaginatorName",
    "OrientationCorrection",
    "PersonTrackingSortBy",
    "ProjectStatus",
    "ProjectVersionRunningWaiterName",
    "ProjectVersionStatus",
    "ProjectVersionTrainingCompletedWaiterName",
    "ProtectiveEquipmentType",
    "QualityFilter",
    "Reason",
    "SegmentType",
    "StreamProcessorStatus",
    "TechnicalCueType",
    "TextTypes",
    "VideoJobStatus",
)


Attribute = Literal["ALL", "DEFAULT"]
BodyPart = Literal["FACE", "HEAD", "LEFT_HAND", "RIGHT_HAND"]
CelebrityRecognitionSortBy = Literal["ID", "TIMESTAMP"]
ContentClassifier = Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
ContentModerationSortBy = Literal["NAME", "TIMESTAMP"]
DescribeProjectVersionsPaginatorName = Literal["describe_project_versions"]
DescribeProjectsPaginatorName = Literal["describe_projects"]
EmotionName = Literal[
    "ANGRY", "CALM", "CONFUSED", "DISGUSTED", "FEAR", "HAPPY", "SAD", "SURPRISED", "UNKNOWN"
]
FaceAttributes = Literal["ALL", "DEFAULT"]
FaceSearchSortBy = Literal["INDEX", "TIMESTAMP"]
GenderType = Literal["Female", "Male"]
LabelDetectionSortBy = Literal["NAME", "TIMESTAMP"]
LandmarkType = Literal[
    "chinBottom",
    "eyeLeft",
    "eyeRight",
    "leftEyeBrowLeft",
    "leftEyeBrowRight",
    "leftEyeBrowUp",
    "leftEyeDown",
    "leftEyeLeft",
    "leftEyeRight",
    "leftEyeUp",
    "leftPupil",
    "midJawlineLeft",
    "midJawlineRight",
    "mouthDown",
    "mouthLeft",
    "mouthRight",
    "mouthUp",
    "nose",
    "noseLeft",
    "noseRight",
    "rightEyeBrowLeft",
    "rightEyeBrowRight",
    "rightEyeBrowUp",
    "rightEyeDown",
    "rightEyeLeft",
    "rightEyeRight",
    "rightEyeUp",
    "rightPupil",
    "upperJawlineLeft",
    "upperJawlineRight",
]
ListCollectionsPaginatorName = Literal["list_collections"]
ListFacesPaginatorName = Literal["list_faces"]
ListStreamProcessorsPaginatorName = Literal["list_stream_processors"]
OrientationCorrection = Literal["ROTATE_0", "ROTATE_180", "ROTATE_270", "ROTATE_90"]
PersonTrackingSortBy = Literal["INDEX", "TIMESTAMP"]
ProjectStatus = Literal["CREATED", "CREATING", "DELETING"]
ProjectVersionRunningWaiterName = Literal["project_version_running"]
ProjectVersionStatus = Literal[
    "DELETING",
    "FAILED",
    "RUNNING",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "TRAINING_COMPLETED",
    "TRAINING_FAILED",
    "TRAINING_IN_PROGRESS",
]
ProjectVersionTrainingCompletedWaiterName = Literal["project_version_training_completed"]
ProtectiveEquipmentType = Literal["FACE_COVER", "HAND_COVER", "HEAD_COVER"]
QualityFilter = Literal["AUTO", "HIGH", "LOW", "MEDIUM", "NONE"]
Reason = Literal[
    "EXCEEDS_MAX_FACES",
    "EXTREME_POSE",
    "LOW_BRIGHTNESS",
    "LOW_CONFIDENCE",
    "LOW_FACE_QUALITY",
    "LOW_SHARPNESS",
    "SMALL_BOUNDING_BOX",
]
SegmentType = Literal["SHOT", "TECHNICAL_CUE"]
StreamProcessorStatus = Literal["FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING"]
TechnicalCueType = Literal["BlackFrames", "ColorBars", "EndCredits"]
TextTypes = Literal["LINE", "WORD"]
VideoJobStatus = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
