"""
Type annotations for polly service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_polly/type_defs.html)

Usage::

    ```python
    from mypy_boto3_polly.type_defs import DescribeVoicesOutputTypeDef

    data: DescribeVoicesOutputTypeDef = {...}
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
    "DescribeVoicesOutputTypeDef",
    "GetLexiconOutputTypeDef",
    "GetSpeechSynthesisTaskOutputTypeDef",
    "LexiconAttributesTypeDef",
    "LexiconDescriptionTypeDef",
    "LexiconTypeDef",
    "ListLexiconsOutputTypeDef",
    "ListSpeechSynthesisTasksOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadata",
    "StartSpeechSynthesisTaskOutputTypeDef",
    "SynthesisTaskTypeDef",
    "SynthesizeSpeechOutputTypeDef",
    "VoiceTypeDef",
)


class DescribeVoicesOutputTypeDef(TypedDict):
    Voices: List["VoiceTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class GetLexiconOutputTypeDef(TypedDict):
    Lexicon: "LexiconTypeDef"
    LexiconAttributes: "LexiconAttributesTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetSpeechSynthesisTaskOutputTypeDef(TypedDict):
    SynthesisTask: "SynthesisTaskTypeDef"
    ResponseMetadata: "ResponseMetadata"


class LexiconAttributesTypeDef(TypedDict, total=False):
    Alphabet: str
    LanguageCode: LanguageCode
    LastModified: datetime
    LexiconArn: str
    LexemesCount: int
    Size: int


class LexiconDescriptionTypeDef(TypedDict, total=False):
    Name: str
    Attributes: "LexiconAttributesTypeDef"


class LexiconTypeDef(TypedDict, total=False):
    Content: str
    Name: str


class ListLexiconsOutputTypeDef(TypedDict):
    Lexicons: List["LexiconDescriptionTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListSpeechSynthesisTasksOutputTypeDef(TypedDict):
    NextToken: str
    SynthesisTasks: List["SynthesisTaskTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class StartSpeechSynthesisTaskOutputTypeDef(TypedDict):
    SynthesisTask: "SynthesisTaskTypeDef"
    ResponseMetadata: "ResponseMetadata"


class SynthesisTaskTypeDef(TypedDict, total=False):
    Engine: Engine
    TaskId: str
    TaskStatus: TaskStatus
    TaskStatusReason: str
    OutputUri: str
    CreationTime: datetime
    RequestCharacters: int
    SnsTopicArn: str
    LexiconNames: List[str]
    OutputFormat: OutputFormat
    SampleRate: str
    SpeechMarkTypes: List[SpeechMarkType]
    TextType: TextType
    VoiceId: VoiceId
    LanguageCode: LanguageCode


class SynthesizeSpeechOutputTypeDef(TypedDict):
    AudioStream: StreamingBody
    ContentType: str
    RequestCharacters: int
    ResponseMetadata: "ResponseMetadata"


class VoiceTypeDef(TypedDict, total=False):
    Gender: Gender
    Id: VoiceId
    LanguageCode: LanguageCode
    LanguageName: str
    Name: str
    AdditionalLanguageCodes: List[LanguageCode]
    SupportedEngines: List[Engine]
