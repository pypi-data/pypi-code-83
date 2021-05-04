"""
Type annotations for translate service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/type_defs.html)

Usage::

    ```python
    from mypy_boto3_translate.type_defs import AppliedTerminologyTypeDef

    data: AppliedTerminologyTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, List, Union

from mypy_boto3_translate.literals import (
    JobStatus,
    ParallelDataFormat,
    ParallelDataStatus,
    TerminologyDataFormat,
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
    "AppliedTerminologyTypeDef",
    "CreateParallelDataResponseTypeDef",
    "DeleteParallelDataResponseTypeDef",
    "DescribeTextTranslationJobResponseTypeDef",
    "EncryptionKeyTypeDef",
    "GetParallelDataResponseTypeDef",
    "GetTerminologyResponseTypeDef",
    "ImportTerminologyResponseTypeDef",
    "InputDataConfigTypeDef",
    "JobDetailsTypeDef",
    "ListParallelDataResponseTypeDef",
    "ListTerminologiesResponseTypeDef",
    "ListTextTranslationJobsResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PaginatorConfigTypeDef",
    "ParallelDataConfigTypeDef",
    "ParallelDataDataLocationTypeDef",
    "ParallelDataPropertiesTypeDef",
    "StartTextTranslationJobResponseTypeDef",
    "StopTextTranslationJobResponseTypeDef",
    "TermTypeDef",
    "TerminologyDataLocationTypeDef",
    "TerminologyDataTypeDef",
    "TerminologyPropertiesTypeDef",
    "TextTranslationJobFilterTypeDef",
    "TextTranslationJobPropertiesTypeDef",
    "TranslateTextResponseTypeDef",
    "UpdateParallelDataResponseTypeDef",
)


class AppliedTerminologyTypeDef(TypedDict, total=False):
    Name: str
    Terms: List["TermTypeDef"]


class CreateParallelDataResponseTypeDef(TypedDict, total=False):
    Name: str
    Status: ParallelDataStatus


class DeleteParallelDataResponseTypeDef(TypedDict, total=False):
    Name: str
    Status: ParallelDataStatus


class DescribeTextTranslationJobResponseTypeDef(TypedDict, total=False):
    TextTranslationJobProperties: "TextTranslationJobPropertiesTypeDef"


EncryptionKeyTypeDef = TypedDict("EncryptionKeyTypeDef", {"Type": Literal["KMS"], "Id": str})


class GetParallelDataResponseTypeDef(TypedDict, total=False):
    ParallelDataProperties: "ParallelDataPropertiesTypeDef"
    DataLocation: "ParallelDataDataLocationTypeDef"
    AuxiliaryDataLocation: "ParallelDataDataLocationTypeDef"
    LatestUpdateAttemptAuxiliaryDataLocation: "ParallelDataDataLocationTypeDef"


class GetTerminologyResponseTypeDef(TypedDict, total=False):
    TerminologyProperties: "TerminologyPropertiesTypeDef"
    TerminologyDataLocation: "TerminologyDataLocationTypeDef"


class ImportTerminologyResponseTypeDef(TypedDict, total=False):
    TerminologyProperties: "TerminologyPropertiesTypeDef"


class InputDataConfigTypeDef(TypedDict):
    S3Uri: str
    ContentType: str


class JobDetailsTypeDef(TypedDict, total=False):
    TranslatedDocumentsCount: int
    DocumentsWithErrorsCount: int
    InputDocumentsCount: int


class ListParallelDataResponseTypeDef(TypedDict, total=False):
    ParallelDataPropertiesList: List["ParallelDataPropertiesTypeDef"]
    NextToken: str


class ListTerminologiesResponseTypeDef(TypedDict, total=False):
    TerminologyPropertiesList: List["TerminologyPropertiesTypeDef"]
    NextToken: str


class ListTextTranslationJobsResponseTypeDef(TypedDict, total=False):
    TextTranslationJobPropertiesList: List["TextTranslationJobPropertiesTypeDef"]
    NextToken: str


class OutputDataConfigTypeDef(TypedDict):
    S3Uri: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParallelDataConfigTypeDef(TypedDict):
    S3Uri: str
    Format: ParallelDataFormat


class ParallelDataDataLocationTypeDef(TypedDict):
    RepositoryType: str
    Location: str


class ParallelDataPropertiesTypeDef(TypedDict, total=False):
    Name: str
    Arn: str
    Description: str
    Status: ParallelDataStatus
    SourceLanguageCode: str
    TargetLanguageCodes: List[str]
    ParallelDataConfig: "ParallelDataConfigTypeDef"
    Message: str
    ImportedDataSize: int
    ImportedRecordCount: int
    FailedRecordCount: int
    SkippedRecordCount: int
    EncryptionKey: "EncryptionKeyTypeDef"
    CreatedAt: datetime
    LastUpdatedAt: datetime
    LatestUpdateAttemptStatus: ParallelDataStatus
    LatestUpdateAttemptAt: datetime


class StartTextTranslationJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


class StopTextTranslationJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


class TermTypeDef(TypedDict, total=False):
    SourceText: str
    TargetText: str


class TerminologyDataLocationTypeDef(TypedDict):
    RepositoryType: str
    Location: str


class TerminologyDataTypeDef(TypedDict):
    File: Union[bytes, IO[bytes]]
    Format: TerminologyDataFormat


class TerminologyPropertiesTypeDef(TypedDict, total=False):
    Name: str
    Description: str
    Arn: str
    SourceLanguageCode: str
    TargetLanguageCodes: List[str]
    EncryptionKey: "EncryptionKeyTypeDef"
    SizeBytes: int
    TermCount: int
    CreatedAt: datetime
    LastUpdatedAt: datetime


class TextTranslationJobFilterTypeDef(TypedDict, total=False):
    JobName: str
    JobStatus: JobStatus
    SubmittedBeforeTime: datetime
    SubmittedAfterTime: datetime


class TextTranslationJobPropertiesTypeDef(TypedDict, total=False):
    JobId: str
    JobName: str
    JobStatus: JobStatus
    JobDetails: "JobDetailsTypeDef"
    SourceLanguageCode: str
    TargetLanguageCodes: List[str]
    TerminologyNames: List[str]
    ParallelDataNames: List[str]
    Message: str
    SubmittedTime: datetime
    EndTime: datetime
    InputDataConfig: "InputDataConfigTypeDef"
    OutputDataConfig: "OutputDataConfigTypeDef"
    DataAccessRoleArn: str


class _RequiredTranslateTextResponseTypeDef(TypedDict):
    TranslatedText: str
    SourceLanguageCode: str
    TargetLanguageCode: str


class TranslateTextResponseTypeDef(_RequiredTranslateTextResponseTypeDef, total=False):
    AppliedTerminologies: List["AppliedTerminologyTypeDef"]


class UpdateParallelDataResponseTypeDef(TypedDict, total=False):
    Name: str
    Status: ParallelDataStatus
    LatestUpdateAttemptStatus: ParallelDataStatus
    LatestUpdateAttemptAt: datetime
