"""
Main interface for translate service type definitions.

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
    EncryptionKeyType,
    JobStatus,
    ParallelDataFormat,
    ParallelDataStatus,
    TerminologyDataFormat,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AppliedTerminologyTypeDef",
    "EncryptionKeyTypeDef",
    "InputDataConfigTypeDef",
    "JobDetailsTypeDef",
    "OutputDataConfigTypeDef",
    "ParallelDataConfigTypeDef",
    "ParallelDataDataLocationTypeDef",
    "ParallelDataPropertiesTypeDef",
    "TermTypeDef",
    "TerminologyDataLocationTypeDef",
    "TerminologyPropertiesTypeDef",
    "TextTranslationJobPropertiesTypeDef",
    "CreateParallelDataResponseTypeDef",
    "DeleteParallelDataResponseTypeDef",
    "DescribeTextTranslationJobResponseTypeDef",
    "GetParallelDataResponseTypeDef",
    "GetTerminologyResponseTypeDef",
    "ImportTerminologyResponseTypeDef",
    "ListParallelDataResponseTypeDef",
    "ListTerminologiesResponseTypeDef",
    "ListTextTranslationJobsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "StartTextTranslationJobResponseTypeDef",
    "StopTextTranslationJobResponseTypeDef",
    "TerminologyDataTypeDef",
    "TextTranslationJobFilterTypeDef",
    "TranslateTextResponseTypeDef",
    "UpdateParallelDataResponseTypeDef",
)

AppliedTerminologyTypeDef = TypedDict(
    "AppliedTerminologyTypeDef", {"Name": str, "Terms": List["TermTypeDef"]}, total=False
)

EncryptionKeyTypeDef = TypedDict("EncryptionKeyTypeDef", {"Type": EncryptionKeyType, "Id": str})

InputDataConfigTypeDef = TypedDict("InputDataConfigTypeDef", {"S3Uri": str, "ContentType": str})

JobDetailsTypeDef = TypedDict(
    "JobDetailsTypeDef",
    {"TranslatedDocumentsCount": int, "DocumentsWithErrorsCount": int, "InputDocumentsCount": int},
    total=False,
)

OutputDataConfigTypeDef = TypedDict("OutputDataConfigTypeDef", {"S3Uri": str})

ParallelDataConfigTypeDef = TypedDict(
    "ParallelDataConfigTypeDef", {"S3Uri": str, "Format": ParallelDataFormat}
)

ParallelDataDataLocationTypeDef = TypedDict(
    "ParallelDataDataLocationTypeDef", {"RepositoryType": str, "Location": str}
)

ParallelDataPropertiesTypeDef = TypedDict(
    "ParallelDataPropertiesTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Description": str,
        "Status": ParallelDataStatus,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "ParallelDataConfig": "ParallelDataConfigTypeDef",
        "Message": str,
        "ImportedDataSize": int,
        "ImportedRecordCount": int,
        "FailedRecordCount": int,
        "SkippedRecordCount": int,
        "EncryptionKey": "EncryptionKeyTypeDef",
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "LatestUpdateAttemptStatus": ParallelDataStatus,
        "LatestUpdateAttemptAt": datetime,
    },
    total=False,
)

TermTypeDef = TypedDict("TermTypeDef", {"SourceText": str, "TargetText": str}, total=False)

TerminologyDataLocationTypeDef = TypedDict(
    "TerminologyDataLocationTypeDef", {"RepositoryType": str, "Location": str}
)

TerminologyPropertiesTypeDef = TypedDict(
    "TerminologyPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Arn": str,
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "EncryptionKey": "EncryptionKeyTypeDef",
        "SizeBytes": int,
        "TermCount": int,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
    },
    total=False,
)

TextTranslationJobPropertiesTypeDef = TypedDict(
    "TextTranslationJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatus,
        "JobDetails": "JobDetailsTypeDef",
        "SourceLanguageCode": str,
        "TargetLanguageCodes": List[str],
        "TerminologyNames": List[str],
        "ParallelDataNames": List[str],
        "Message": str,
        "SubmittedTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
    },
    total=False,
)

CreateParallelDataResponseTypeDef = TypedDict(
    "CreateParallelDataResponseTypeDef", {"Name": str, "Status": ParallelDataStatus}, total=False
)

DeleteParallelDataResponseTypeDef = TypedDict(
    "DeleteParallelDataResponseTypeDef", {"Name": str, "Status": ParallelDataStatus}, total=False
)

DescribeTextTranslationJobResponseTypeDef = TypedDict(
    "DescribeTextTranslationJobResponseTypeDef",
    {"TextTranslationJobProperties": "TextTranslationJobPropertiesTypeDef"},
    total=False,
)

GetParallelDataResponseTypeDef = TypedDict(
    "GetParallelDataResponseTypeDef",
    {
        "ParallelDataProperties": "ParallelDataPropertiesTypeDef",
        "DataLocation": "ParallelDataDataLocationTypeDef",
        "AuxiliaryDataLocation": "ParallelDataDataLocationTypeDef",
        "LatestUpdateAttemptAuxiliaryDataLocation": "ParallelDataDataLocationTypeDef",
    },
    total=False,
)

GetTerminologyResponseTypeDef = TypedDict(
    "GetTerminologyResponseTypeDef",
    {
        "TerminologyProperties": "TerminologyPropertiesTypeDef",
        "TerminologyDataLocation": "TerminologyDataLocationTypeDef",
    },
    total=False,
)

ImportTerminologyResponseTypeDef = TypedDict(
    "ImportTerminologyResponseTypeDef",
    {"TerminologyProperties": "TerminologyPropertiesTypeDef"},
    total=False,
)

ListParallelDataResponseTypeDef = TypedDict(
    "ListParallelDataResponseTypeDef",
    {"ParallelDataPropertiesList": List["ParallelDataPropertiesTypeDef"], "NextToken": str},
    total=False,
)

ListTerminologiesResponseTypeDef = TypedDict(
    "ListTerminologiesResponseTypeDef",
    {"TerminologyPropertiesList": List["TerminologyPropertiesTypeDef"], "NextToken": str},
    total=False,
)

ListTextTranslationJobsResponseTypeDef = TypedDict(
    "ListTextTranslationJobsResponseTypeDef",
    {
        "TextTranslationJobPropertiesList": List["TextTranslationJobPropertiesTypeDef"],
        "NextToken": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartTextTranslationJobResponseTypeDef = TypedDict(
    "StartTextTranslationJobResponseTypeDef", {"JobId": str, "JobStatus": JobStatus}, total=False
)

StopTextTranslationJobResponseTypeDef = TypedDict(
    "StopTextTranslationJobResponseTypeDef", {"JobId": str, "JobStatus": JobStatus}, total=False
)

TerminologyDataTypeDef = TypedDict(
    "TerminologyDataTypeDef", {"File": Union[bytes, IO[bytes]], "Format": TerminologyDataFormat}
)

TextTranslationJobFilterTypeDef = TypedDict(
    "TextTranslationJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatus,
        "SubmittedBeforeTime": datetime,
        "SubmittedAfterTime": datetime,
    },
    total=False,
)

_RequiredTranslateTextResponseTypeDef = TypedDict(
    "_RequiredTranslateTextResponseTypeDef",
    {"TranslatedText": str, "SourceLanguageCode": str, "TargetLanguageCode": str},
)
_OptionalTranslateTextResponseTypeDef = TypedDict(
    "_OptionalTranslateTextResponseTypeDef",
    {"AppliedTerminologies": List["AppliedTerminologyTypeDef"]},
    total=False,
)


class TranslateTextResponseTypeDef(
    _RequiredTranslateTextResponseTypeDef, _OptionalTranslateTextResponseTypeDef
):
    pass


UpdateParallelDataResponseTypeDef = TypedDict(
    "UpdateParallelDataResponseTypeDef",
    {
        "Name": str,
        "Status": ParallelDataStatus,
        "LatestUpdateAttemptStatus": ParallelDataStatus,
        "LatestUpdateAttemptAt": datetime,
    },
    total=False,
)
