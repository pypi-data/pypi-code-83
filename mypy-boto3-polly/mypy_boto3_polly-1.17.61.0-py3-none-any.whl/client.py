"""
Main interface for polly service client

Usage::

    ```python
    import boto3
    from mypy_boto3_polly import PollyClient

    client: PollyClient = boto3.client("polly")
    ```
"""
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_polly.literals import (
    DescribeVoicesPaginatorName,
    Engine,
    LanguageCode,
    ListLexiconsPaginatorName,
    ListSpeechSynthesisTasksPaginatorName,
    OutputFormat,
    SpeechMarkType,
    TaskStatus,
    TextType,
    VoiceId,
)
from mypy_boto3_polly.paginator import (
    DescribeVoicesPaginator,
    ListLexiconsPaginator,
    ListSpeechSynthesisTasksPaginator,
)
from mypy_boto3_polly.type_defs import (
    DescribeVoicesOutputTypeDef,
    GetLexiconOutputTypeDef,
    GetSpeechSynthesisTaskOutputTypeDef,
    ListLexiconsOutputTypeDef,
    ListSpeechSynthesisTasksOutputTypeDef,
    StartSpeechSynthesisTaskOutputTypeDef,
    SynthesizeSpeechOutputTypeDef,
)

__all__ = ("PollyClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    EngineNotSupportedException: Type[BotocoreClientError]
    InvalidLexiconException: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidS3BucketException: Type[BotocoreClientError]
    InvalidS3KeyException: Type[BotocoreClientError]
    InvalidSampleRateException: Type[BotocoreClientError]
    InvalidSnsTopicArnException: Type[BotocoreClientError]
    InvalidSsmlException: Type[BotocoreClientError]
    InvalidTaskIdException: Type[BotocoreClientError]
    LanguageNotSupportedException: Type[BotocoreClientError]
    LexiconNotFoundException: Type[BotocoreClientError]
    LexiconSizeExceededException: Type[BotocoreClientError]
    MarksNotSupportedForFormatException: Type[BotocoreClientError]
    MaxLexemeLengthExceededException: Type[BotocoreClientError]
    MaxLexiconsNumberExceededException: Type[BotocoreClientError]
    ServiceFailureException: Type[BotocoreClientError]
    SsmlMarksNotSupportedForTextTypeException: Type[BotocoreClientError]
    SynthesisTaskNotFoundException: Type[BotocoreClientError]
    TextLengthExceededException: Type[BotocoreClientError]
    UnsupportedPlsAlphabetException: Type[BotocoreClientError]
    UnsupportedPlsLanguageException: Type[BotocoreClientError]


class PollyClient:
    """
    [Polly.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Client.can_paginate)
        """

    def delete_lexicon(self, Name: str) -> Dict[str, Any]:
        """
        [Client.delete_lexicon documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Client.delete_lexicon)
        """

    def describe_voices(
        self,
        Engine: Engine = None,
        LanguageCode: LanguageCode = None,
        IncludeAdditionalLanguageCodes: bool = None,
        NextToken: str = None,
    ) -> DescribeVoicesOutputTypeDef:
        """
        [Client.describe_voices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Client.describe_voices)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Client.generate_presigned_url)
        """

    def get_lexicon(self, Name: str) -> GetLexiconOutputTypeDef:
        """
        [Client.get_lexicon documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Client.get_lexicon)
        """

    def get_speech_synthesis_task(self, TaskId: str) -> GetSpeechSynthesisTaskOutputTypeDef:
        """
        [Client.get_speech_synthesis_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Client.get_speech_synthesis_task)
        """

    def list_lexicons(self, NextToken: str = None) -> ListLexiconsOutputTypeDef:
        """
        [Client.list_lexicons documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Client.list_lexicons)
        """

    def list_speech_synthesis_tasks(
        self, MaxResults: int = None, NextToken: str = None, Status: TaskStatus = None
    ) -> ListSpeechSynthesisTasksOutputTypeDef:
        """
        [Client.list_speech_synthesis_tasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Client.list_speech_synthesis_tasks)
        """

    def put_lexicon(self, Name: str, Content: str) -> Dict[str, Any]:
        """
        [Client.put_lexicon documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Client.put_lexicon)
        """

    def start_speech_synthesis_task(
        self,
        OutputFormat: OutputFormat,
        OutputS3BucketName: str,
        Text: str,
        VoiceId: VoiceId,
        Engine: Engine = None,
        LanguageCode: LanguageCode = None,
        LexiconNames: List[str] = None,
        OutputS3KeyPrefix: str = None,
        SampleRate: str = None,
        SnsTopicArn: str = None,
        SpeechMarkTypes: List[SpeechMarkType] = None,
        TextType: TextType = None,
    ) -> StartSpeechSynthesisTaskOutputTypeDef:
        """
        [Client.start_speech_synthesis_task documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Client.start_speech_synthesis_task)
        """

    def synthesize_speech(
        self,
        OutputFormat: OutputFormat,
        Text: str,
        VoiceId: VoiceId,
        Engine: Engine = None,
        LanguageCode: LanguageCode = None,
        LexiconNames: List[str] = None,
        SampleRate: str = None,
        SpeechMarkTypes: List[SpeechMarkType] = None,
        TextType: TextType = None,
    ) -> SynthesizeSpeechOutputTypeDef:
        """
        [Client.synthesize_speech documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Client.synthesize_speech)
        """

    @overload
    def get_paginator(self, operation_name: DescribeVoicesPaginatorName) -> DescribeVoicesPaginator:
        """
        [Paginator.DescribeVoices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Paginator.DescribeVoices)
        """

    @overload
    def get_paginator(self, operation_name: ListLexiconsPaginatorName) -> ListLexiconsPaginator:
        """
        [Paginator.ListLexicons documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Paginator.ListLexicons)
        """

    @overload
    def get_paginator(
        self, operation_name: ListSpeechSynthesisTasksPaginatorName
    ) -> ListSpeechSynthesisTasksPaginator:
        """
        [Paginator.ListSpeechSynthesisTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Paginator.ListSpeechSynthesisTasks)
        """
