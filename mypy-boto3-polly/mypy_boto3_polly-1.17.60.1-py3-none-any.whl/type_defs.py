"""
Main interface for polly service type definitions.

Usage::

    ```python
    from mypy_boto3_polly.type_defs import LexiconAttributesTypeDef

    data: LexiconAttributesTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from botocore.response import StreamingBody

from mypy_boto3_polly.literals import (
    Engine,
    Gender,
    LanguageCode,
    OutputFormat,
    SpeechMarkType,
    TaskStatus,
    TextType,
    VoiceId,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "LexiconAttributesTypeDef",
    "LexiconDescriptionTypeDef",
    "LexiconTypeDef",
    "ResponseMetadata",
    "SynthesisTaskTypeDef",
    "VoiceTypeDef",
    "DescribeVoicesOutputTypeDef",
    "GetLexiconOutputTypeDef",
    "GetSpeechSynthesisTaskOutputTypeDef",
    "ListLexiconsOutputTypeDef",
    "ListSpeechSynthesisTasksOutputTypeDef",
    "PaginatorConfigTypeDef",
    "StartSpeechSynthesisTaskOutputTypeDef",
    "SynthesizeSpeechOutputTypeDef",
)

LexiconAttributesTypeDef = TypedDict(
    "LexiconAttributesTypeDef",
    {
        "Alphabet": str,
        "LanguageCode": LanguageCode,
        "LastModified": datetime,
        "LexiconArn": str,
        "LexemesCount": int,
        "Size": int,
    },
    total=False,
)

LexiconDescriptionTypeDef = TypedDict(
    "LexiconDescriptionTypeDef",
    {"Name": str, "Attributes": "LexiconAttributesTypeDef"},
    total=False,
)

LexiconTypeDef = TypedDict("LexiconTypeDef", {"Content": str, "Name": str}, total=False)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

SynthesisTaskTypeDef = TypedDict(
    "SynthesisTaskTypeDef",
    {
        "Engine": Engine,
        "TaskId": str,
        "TaskStatus": TaskStatus,
        "TaskStatusReason": str,
        "OutputUri": str,
        "CreationTime": datetime,
        "RequestCharacters": int,
        "SnsTopicArn": str,
        "LexiconNames": List[str],
        "OutputFormat": OutputFormat,
        "SampleRate": str,
        "SpeechMarkTypes": List[SpeechMarkType],
        "TextType": TextType,
        "VoiceId": VoiceId,
        "LanguageCode": LanguageCode,
    },
    total=False,
)

VoiceTypeDef = TypedDict(
    "VoiceTypeDef",
    {
        "Gender": Gender,
        "Id": VoiceId,
        "LanguageCode": LanguageCode,
        "LanguageName": str,
        "Name": str,
        "AdditionalLanguageCodes": List[LanguageCode],
        "SupportedEngines": List[Engine],
    },
    total=False,
)

DescribeVoicesOutputTypeDef = TypedDict(
    "DescribeVoicesOutputTypeDef",
    {"Voices": List["VoiceTypeDef"], "NextToken": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetLexiconOutputTypeDef = TypedDict(
    "GetLexiconOutputTypeDef",
    {
        "Lexicon": "LexiconTypeDef",
        "LexiconAttributes": "LexiconAttributesTypeDef",
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

GetSpeechSynthesisTaskOutputTypeDef = TypedDict(
    "GetSpeechSynthesisTaskOutputTypeDef",
    {"SynthesisTask": "SynthesisTaskTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListLexiconsOutputTypeDef = TypedDict(
    "ListLexiconsOutputTypeDef",
    {
        "Lexicons": List["LexiconDescriptionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListSpeechSynthesisTasksOutputTypeDef = TypedDict(
    "ListSpeechSynthesisTasksOutputTypeDef",
    {
        "NextToken": str,
        "SynthesisTasks": List["SynthesisTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

StartSpeechSynthesisTaskOutputTypeDef = TypedDict(
    "StartSpeechSynthesisTaskOutputTypeDef",
    {"SynthesisTask": "SynthesisTaskTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

SynthesizeSpeechOutputTypeDef = TypedDict(
    "SynthesizeSpeechOutputTypeDef",
    {
        "AudioStream": StreamingBody,
        "ContentType": str,
        "RequestCharacters": int,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)
