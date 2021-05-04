"""
Type annotations for transcribe service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/type_defs.html)

Usage::

    ```python
    from mypy_boto3_transcribe.type_defs import ContentRedactionTypeDef

    data: ContentRedactionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_transcribe.literals import (
    BaseModelName,
    CLMLanguageCode,
    LanguageCode,
    MediaFormat,
    ModelStatus,
    OutputLocationType,
    RedactionOutput,
    TranscriptionJobStatus,
    TypeType,
    VocabularyFilterMethod,
    VocabularyState,
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
    "ContentRedactionTypeDef",
    "CreateLanguageModelResponseTypeDef",
    "CreateMedicalVocabularyResponseTypeDef",
    "CreateVocabularyFilterResponseTypeDef",
    "CreateVocabularyResponseTypeDef",
    "DescribeLanguageModelResponseTypeDef",
    "GetMedicalTranscriptionJobResponseTypeDef",
    "GetMedicalVocabularyResponseTypeDef",
    "GetTranscriptionJobResponseTypeDef",
    "GetVocabularyFilterResponseTypeDef",
    "GetVocabularyResponseTypeDef",
    "InputDataConfigTypeDef",
    "JobExecutionSettingsTypeDef",
    "LanguageModelTypeDef",
    "ListLanguageModelsResponseTypeDef",
    "ListMedicalTranscriptionJobsResponseTypeDef",
    "ListMedicalVocabulariesResponseTypeDef",
    "ListTranscriptionJobsResponseTypeDef",
    "ListVocabulariesResponseTypeDef",
    "ListVocabularyFiltersResponseTypeDef",
    "MediaTypeDef",
    "MedicalTranscriptTypeDef",
    "MedicalTranscriptionJobSummaryTypeDef",
    "MedicalTranscriptionJobTypeDef",
    "MedicalTranscriptionSettingTypeDef",
    "ModelSettingsTypeDef",
    "SettingsTypeDef",
    "StartMedicalTranscriptionJobResponseTypeDef",
    "StartTranscriptionJobResponseTypeDef",
    "TranscriptTypeDef",
    "TranscriptionJobSummaryTypeDef",
    "TranscriptionJobTypeDef",
    "UpdateMedicalVocabularyResponseTypeDef",
    "UpdateVocabularyFilterResponseTypeDef",
    "UpdateVocabularyResponseTypeDef",
    "VocabularyFilterInfoTypeDef",
    "VocabularyInfoTypeDef",
)


class ContentRedactionTypeDef(TypedDict):
    RedactionType: Literal["PII"]
    RedactionOutput: RedactionOutput


class CreateLanguageModelResponseTypeDef(TypedDict, total=False):
    LanguageCode: CLMLanguageCode
    BaseModelName: BaseModelName
    ModelName: str
    InputDataConfig: "InputDataConfigTypeDef"
    ModelStatus: ModelStatus


class CreateMedicalVocabularyResponseTypeDef(TypedDict, total=False):
    VocabularyName: str
    LanguageCode: LanguageCode
    VocabularyState: VocabularyState
    LastModifiedTime: datetime
    FailureReason: str


class CreateVocabularyFilterResponseTypeDef(TypedDict, total=False):
    VocabularyFilterName: str
    LanguageCode: LanguageCode
    LastModifiedTime: datetime


class CreateVocabularyResponseTypeDef(TypedDict, total=False):
    VocabularyName: str
    LanguageCode: LanguageCode
    VocabularyState: VocabularyState
    LastModifiedTime: datetime
    FailureReason: str


class DescribeLanguageModelResponseTypeDef(TypedDict, total=False):
    LanguageModel: "LanguageModelTypeDef"


class GetMedicalTranscriptionJobResponseTypeDef(TypedDict, total=False):
    MedicalTranscriptionJob: "MedicalTranscriptionJobTypeDef"


class GetMedicalVocabularyResponseTypeDef(TypedDict, total=False):
    VocabularyName: str
    LanguageCode: LanguageCode
    VocabularyState: VocabularyState
    LastModifiedTime: datetime
    FailureReason: str
    DownloadUri: str


class GetTranscriptionJobResponseTypeDef(TypedDict, total=False):
    TranscriptionJob: "TranscriptionJobTypeDef"


class GetVocabularyFilterResponseTypeDef(TypedDict, total=False):
    VocabularyFilterName: str
    LanguageCode: LanguageCode
    LastModifiedTime: datetime
    DownloadUri: str


class GetVocabularyResponseTypeDef(TypedDict, total=False):
    VocabularyName: str
    LanguageCode: LanguageCode
    VocabularyState: VocabularyState
    LastModifiedTime: datetime
    FailureReason: str
    DownloadUri: str


class _RequiredInputDataConfigTypeDef(TypedDict):
    S3Uri: str
    DataAccessRoleArn: str


class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, total=False):
    TuningDataS3Uri: str


class JobExecutionSettingsTypeDef(TypedDict, total=False):
    AllowDeferredExecution: bool
    DataAccessRoleArn: str


class LanguageModelTypeDef(TypedDict, total=False):
    ModelName: str
    CreateTime: datetime
    LastModifiedTime: datetime
    LanguageCode: CLMLanguageCode
    BaseModelName: BaseModelName
    ModelStatus: ModelStatus
    UpgradeAvailability: bool
    FailureReason: str
    InputDataConfig: "InputDataConfigTypeDef"


class ListLanguageModelsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Models: List["LanguageModelTypeDef"]


class ListMedicalTranscriptionJobsResponseTypeDef(TypedDict, total=False):
    Status: TranscriptionJobStatus
    NextToken: str
    MedicalTranscriptionJobSummaries: List["MedicalTranscriptionJobSummaryTypeDef"]


class ListMedicalVocabulariesResponseTypeDef(TypedDict, total=False):
    Status: VocabularyState
    NextToken: str
    Vocabularies: List["VocabularyInfoTypeDef"]


class ListTranscriptionJobsResponseTypeDef(TypedDict, total=False):
    Status: TranscriptionJobStatus
    NextToken: str
    TranscriptionJobSummaries: List["TranscriptionJobSummaryTypeDef"]


class ListVocabulariesResponseTypeDef(TypedDict, total=False):
    Status: VocabularyState
    NextToken: str
    Vocabularies: List["VocabularyInfoTypeDef"]


class ListVocabularyFiltersResponseTypeDef(TypedDict, total=False):
    NextToken: str
    VocabularyFilters: List["VocabularyFilterInfoTypeDef"]


class MediaTypeDef(TypedDict, total=False):
    MediaFileUri: str


class MedicalTranscriptTypeDef(TypedDict, total=False):
    TranscriptFileUri: str


MedicalTranscriptionJobSummaryTypeDef = TypedDict(
    "MedicalTranscriptionJobSummaryTypeDef",
    {
        "MedicalTranscriptionJobName": str,
        "CreationTime": datetime,
        "StartTime": datetime,
        "CompletionTime": datetime,
        "LanguageCode": LanguageCode,
        "TranscriptionJobStatus": TranscriptionJobStatus,
        "FailureReason": str,
        "OutputLocationType": OutputLocationType,
        "Specialty": Literal["PRIMARYCARE"],
        "Type": TypeType,
    },
    total=False,
)

MedicalTranscriptionJobTypeDef = TypedDict(
    "MedicalTranscriptionJobTypeDef",
    {
        "MedicalTranscriptionJobName": str,
        "TranscriptionJobStatus": TranscriptionJobStatus,
        "LanguageCode": LanguageCode,
        "MediaSampleRateHertz": int,
        "MediaFormat": MediaFormat,
        "Media": "MediaTypeDef",
        "Transcript": "MedicalTranscriptTypeDef",
        "StartTime": datetime,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "FailureReason": str,
        "Settings": "MedicalTranscriptionSettingTypeDef",
        "Specialty": Literal["PRIMARYCARE"],
        "Type": TypeType,
    },
    total=False,
)


class MedicalTranscriptionSettingTypeDef(TypedDict, total=False):
    ShowSpeakerLabels: bool
    MaxSpeakerLabels: int
    ChannelIdentification: bool
    ShowAlternatives: bool
    MaxAlternatives: int
    VocabularyName: str


class ModelSettingsTypeDef(TypedDict, total=False):
    LanguageModelName: str


class SettingsTypeDef(TypedDict, total=False):
    VocabularyName: str
    ShowSpeakerLabels: bool
    MaxSpeakerLabels: int
    ChannelIdentification: bool
    ShowAlternatives: bool
    MaxAlternatives: int
    VocabularyFilterName: str
    VocabularyFilterMethod: VocabularyFilterMethod


class StartMedicalTranscriptionJobResponseTypeDef(TypedDict, total=False):
    MedicalTranscriptionJob: "MedicalTranscriptionJobTypeDef"


class StartTranscriptionJobResponseTypeDef(TypedDict, total=False):
    TranscriptionJob: "TranscriptionJobTypeDef"


class TranscriptTypeDef(TypedDict, total=False):
    TranscriptFileUri: str
    RedactedTranscriptFileUri: str


class TranscriptionJobSummaryTypeDef(TypedDict, total=False):
    TranscriptionJobName: str
    CreationTime: datetime
    StartTime: datetime
    CompletionTime: datetime
    LanguageCode: LanguageCode
    TranscriptionJobStatus: TranscriptionJobStatus
    FailureReason: str
    OutputLocationType: OutputLocationType
    ContentRedaction: "ContentRedactionTypeDef"
    ModelSettings: "ModelSettingsTypeDef"
    IdentifyLanguage: bool
    IdentifiedLanguageScore: float


class TranscriptionJobTypeDef(TypedDict, total=False):
    TranscriptionJobName: str
    TranscriptionJobStatus: TranscriptionJobStatus
    LanguageCode: LanguageCode
    MediaSampleRateHertz: int
    MediaFormat: MediaFormat
    Media: "MediaTypeDef"
    Transcript: "TranscriptTypeDef"
    StartTime: datetime
    CreationTime: datetime
    CompletionTime: datetime
    FailureReason: str
    Settings: "SettingsTypeDef"
    ModelSettings: "ModelSettingsTypeDef"
    JobExecutionSettings: "JobExecutionSettingsTypeDef"
    ContentRedaction: "ContentRedactionTypeDef"
    IdentifyLanguage: bool
    LanguageOptions: List[LanguageCode]
    IdentifiedLanguageScore: float


class UpdateMedicalVocabularyResponseTypeDef(TypedDict, total=False):
    VocabularyName: str
    LanguageCode: LanguageCode
    LastModifiedTime: datetime
    VocabularyState: VocabularyState


class UpdateVocabularyFilterResponseTypeDef(TypedDict, total=False):
    VocabularyFilterName: str
    LanguageCode: LanguageCode
    LastModifiedTime: datetime


class UpdateVocabularyResponseTypeDef(TypedDict, total=False):
    VocabularyName: str
    LanguageCode: LanguageCode
    LastModifiedTime: datetime
    VocabularyState: VocabularyState


class VocabularyFilterInfoTypeDef(TypedDict, total=False):
    VocabularyFilterName: str
    LanguageCode: LanguageCode
    LastModifiedTime: datetime


class VocabularyInfoTypeDef(TypedDict, total=False):
    VocabularyName: str
    LanguageCode: LanguageCode
    LastModifiedTime: datetime
    VocabularyState: VocabularyState
