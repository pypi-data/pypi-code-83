"""
Main interface for transcribe service type definitions.

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
    RedactionType,
    Specialty,
    TranscriptionJobStatus,
    TypeType,
    VocabularyFilterMethod,
    VocabularyState,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ContentRedactionTypeDef",
    "InputDataConfigTypeDef",
    "JobExecutionSettingsTypeDef",
    "LanguageModelTypeDef",
    "MediaTypeDef",
    "MedicalTranscriptTypeDef",
    "MedicalTranscriptionJobSummaryTypeDef",
    "MedicalTranscriptionJobTypeDef",
    "MedicalTranscriptionSettingTypeDef",
    "ModelSettingsTypeDef",
    "SettingsTypeDef",
    "TranscriptTypeDef",
    "TranscriptionJobSummaryTypeDef",
    "TranscriptionJobTypeDef",
    "VocabularyFilterInfoTypeDef",
    "VocabularyInfoTypeDef",
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
    "ListLanguageModelsResponseTypeDef",
    "ListMedicalTranscriptionJobsResponseTypeDef",
    "ListMedicalVocabulariesResponseTypeDef",
    "ListTranscriptionJobsResponseTypeDef",
    "ListVocabulariesResponseTypeDef",
    "ListVocabularyFiltersResponseTypeDef",
    "StartMedicalTranscriptionJobResponseTypeDef",
    "StartTranscriptionJobResponseTypeDef",
    "UpdateMedicalVocabularyResponseTypeDef",
    "UpdateVocabularyFilterResponseTypeDef",
    "UpdateVocabularyResponseTypeDef",
)

ContentRedactionTypeDef = TypedDict(
    "ContentRedactionTypeDef", {"RedactionType": RedactionType, "RedactionOutput": RedactionOutput}
)

_RequiredInputDataConfigTypeDef = TypedDict(
    "_RequiredInputDataConfigTypeDef", {"S3Uri": str, "DataAccessRoleArn": str}
)
_OptionalInputDataConfigTypeDef = TypedDict(
    "_OptionalInputDataConfigTypeDef", {"TuningDataS3Uri": str}, total=False
)


class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, _OptionalInputDataConfigTypeDef):
    pass


JobExecutionSettingsTypeDef = TypedDict(
    "JobExecutionSettingsTypeDef",
    {"AllowDeferredExecution": bool, "DataAccessRoleArn": str},
    total=False,
)

LanguageModelTypeDef = TypedDict(
    "LanguageModelTypeDef",
    {
        "ModelName": str,
        "CreateTime": datetime,
        "LastModifiedTime": datetime,
        "LanguageCode": CLMLanguageCode,
        "BaseModelName": BaseModelName,
        "ModelStatus": ModelStatus,
        "UpgradeAvailability": bool,
        "FailureReason": str,
        "InputDataConfig": "InputDataConfigTypeDef",
    },
    total=False,
)

MediaTypeDef = TypedDict("MediaTypeDef", {"MediaFileUri": str}, total=False)

MedicalTranscriptTypeDef = TypedDict(
    "MedicalTranscriptTypeDef", {"TranscriptFileUri": str}, total=False
)

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
        "Specialty": Specialty,
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
        "Specialty": Specialty,
        "Type": TypeType,
    },
    total=False,
)

MedicalTranscriptionSettingTypeDef = TypedDict(
    "MedicalTranscriptionSettingTypeDef",
    {
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
        "ShowAlternatives": bool,
        "MaxAlternatives": int,
        "VocabularyName": str,
    },
    total=False,
)

ModelSettingsTypeDef = TypedDict("ModelSettingsTypeDef", {"LanguageModelName": str}, total=False)

SettingsTypeDef = TypedDict(
    "SettingsTypeDef",
    {
        "VocabularyName": str,
        "ShowSpeakerLabels": bool,
        "MaxSpeakerLabels": int,
        "ChannelIdentification": bool,
        "ShowAlternatives": bool,
        "MaxAlternatives": int,
        "VocabularyFilterName": str,
        "VocabularyFilterMethod": VocabularyFilterMethod,
    },
    total=False,
)

TranscriptTypeDef = TypedDict(
    "TranscriptTypeDef", {"TranscriptFileUri": str, "RedactedTranscriptFileUri": str}, total=False
)

TranscriptionJobSummaryTypeDef = TypedDict(
    "TranscriptionJobSummaryTypeDef",
    {
        "TranscriptionJobName": str,
        "CreationTime": datetime,
        "StartTime": datetime,
        "CompletionTime": datetime,
        "LanguageCode": LanguageCode,
        "TranscriptionJobStatus": TranscriptionJobStatus,
        "FailureReason": str,
        "OutputLocationType": OutputLocationType,
        "ContentRedaction": "ContentRedactionTypeDef",
        "ModelSettings": "ModelSettingsTypeDef",
        "IdentifyLanguage": bool,
        "IdentifiedLanguageScore": float,
    },
    total=False,
)

TranscriptionJobTypeDef = TypedDict(
    "TranscriptionJobTypeDef",
    {
        "TranscriptionJobName": str,
        "TranscriptionJobStatus": TranscriptionJobStatus,
        "LanguageCode": LanguageCode,
        "MediaSampleRateHertz": int,
        "MediaFormat": MediaFormat,
        "Media": "MediaTypeDef",
        "Transcript": "TranscriptTypeDef",
        "StartTime": datetime,
        "CreationTime": datetime,
        "CompletionTime": datetime,
        "FailureReason": str,
        "Settings": "SettingsTypeDef",
        "ModelSettings": "ModelSettingsTypeDef",
        "JobExecutionSettings": "JobExecutionSettingsTypeDef",
        "ContentRedaction": "ContentRedactionTypeDef",
        "IdentifyLanguage": bool,
        "LanguageOptions": List[LanguageCode],
        "IdentifiedLanguageScore": float,
    },
    total=False,
)

VocabularyFilterInfoTypeDef = TypedDict(
    "VocabularyFilterInfoTypeDef",
    {"VocabularyFilterName": str, "LanguageCode": LanguageCode, "LastModifiedTime": datetime},
    total=False,
)

VocabularyInfoTypeDef = TypedDict(
    "VocabularyInfoTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCode,
        "LastModifiedTime": datetime,
        "VocabularyState": VocabularyState,
    },
    total=False,
)

CreateLanguageModelResponseTypeDef = TypedDict(
    "CreateLanguageModelResponseTypeDef",
    {
        "LanguageCode": CLMLanguageCode,
        "BaseModelName": BaseModelName,
        "ModelName": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "ModelStatus": ModelStatus,
    },
    total=False,
)

CreateMedicalVocabularyResponseTypeDef = TypedDict(
    "CreateMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCode,
        "VocabularyState": VocabularyState,
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)

CreateVocabularyFilterResponseTypeDef = TypedDict(
    "CreateVocabularyFilterResponseTypeDef",
    {"VocabularyFilterName": str, "LanguageCode": LanguageCode, "LastModifiedTime": datetime},
    total=False,
)

CreateVocabularyResponseTypeDef = TypedDict(
    "CreateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCode,
        "VocabularyState": VocabularyState,
        "LastModifiedTime": datetime,
        "FailureReason": str,
    },
    total=False,
)

DescribeLanguageModelResponseTypeDef = TypedDict(
    "DescribeLanguageModelResponseTypeDef", {"LanguageModel": "LanguageModelTypeDef"}, total=False
)

GetMedicalTranscriptionJobResponseTypeDef = TypedDict(
    "GetMedicalTranscriptionJobResponseTypeDef",
    {"MedicalTranscriptionJob": "MedicalTranscriptionJobTypeDef"},
    total=False,
)

GetMedicalVocabularyResponseTypeDef = TypedDict(
    "GetMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCode,
        "VocabularyState": VocabularyState,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
    },
    total=False,
)

GetTranscriptionJobResponseTypeDef = TypedDict(
    "GetTranscriptionJobResponseTypeDef",
    {"TranscriptionJob": "TranscriptionJobTypeDef"},
    total=False,
)

GetVocabularyFilterResponseTypeDef = TypedDict(
    "GetVocabularyFilterResponseTypeDef",
    {
        "VocabularyFilterName": str,
        "LanguageCode": LanguageCode,
        "LastModifiedTime": datetime,
        "DownloadUri": str,
    },
    total=False,
)

GetVocabularyResponseTypeDef = TypedDict(
    "GetVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCode,
        "VocabularyState": VocabularyState,
        "LastModifiedTime": datetime,
        "FailureReason": str,
        "DownloadUri": str,
    },
    total=False,
)

ListLanguageModelsResponseTypeDef = TypedDict(
    "ListLanguageModelsResponseTypeDef",
    {"NextToken": str, "Models": List["LanguageModelTypeDef"]},
    total=False,
)

ListMedicalTranscriptionJobsResponseTypeDef = TypedDict(
    "ListMedicalTranscriptionJobsResponseTypeDef",
    {
        "Status": TranscriptionJobStatus,
        "NextToken": str,
        "MedicalTranscriptionJobSummaries": List["MedicalTranscriptionJobSummaryTypeDef"],
    },
    total=False,
)

ListMedicalVocabulariesResponseTypeDef = TypedDict(
    "ListMedicalVocabulariesResponseTypeDef",
    {"Status": VocabularyState, "NextToken": str, "Vocabularies": List["VocabularyInfoTypeDef"]},
    total=False,
)

ListTranscriptionJobsResponseTypeDef = TypedDict(
    "ListTranscriptionJobsResponseTypeDef",
    {
        "Status": TranscriptionJobStatus,
        "NextToken": str,
        "TranscriptionJobSummaries": List["TranscriptionJobSummaryTypeDef"],
    },
    total=False,
)

ListVocabulariesResponseTypeDef = TypedDict(
    "ListVocabulariesResponseTypeDef",
    {"Status": VocabularyState, "NextToken": str, "Vocabularies": List["VocabularyInfoTypeDef"]},
    total=False,
)

ListVocabularyFiltersResponseTypeDef = TypedDict(
    "ListVocabularyFiltersResponseTypeDef",
    {"NextToken": str, "VocabularyFilters": List["VocabularyFilterInfoTypeDef"]},
    total=False,
)

StartMedicalTranscriptionJobResponseTypeDef = TypedDict(
    "StartMedicalTranscriptionJobResponseTypeDef",
    {"MedicalTranscriptionJob": "MedicalTranscriptionJobTypeDef"},
    total=False,
)

StartTranscriptionJobResponseTypeDef = TypedDict(
    "StartTranscriptionJobResponseTypeDef",
    {"TranscriptionJob": "TranscriptionJobTypeDef"},
    total=False,
)

UpdateMedicalVocabularyResponseTypeDef = TypedDict(
    "UpdateMedicalVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCode,
        "LastModifiedTime": datetime,
        "VocabularyState": VocabularyState,
    },
    total=False,
)

UpdateVocabularyFilterResponseTypeDef = TypedDict(
    "UpdateVocabularyFilterResponseTypeDef",
    {"VocabularyFilterName": str, "LanguageCode": LanguageCode, "LastModifiedTime": datetime},
    total=False,
)

UpdateVocabularyResponseTypeDef = TypedDict(
    "UpdateVocabularyResponseTypeDef",
    {
        "VocabularyName": str,
        "LanguageCode": LanguageCode,
        "LastModifiedTime": datetime,
        "VocabularyState": VocabularyState,
    },
    total=False,
)
