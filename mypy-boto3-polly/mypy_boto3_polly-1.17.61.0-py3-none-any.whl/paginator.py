"""
Main interface for polly service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_polly import PollyClient
    from mypy_boto3_polly.paginator import (
        DescribeVoicesPaginator,
        ListLexiconsPaginator,
        ListSpeechSynthesisTasksPaginator,
    )

    client: PollyClient = boto3.client("polly")

    describe_voices_paginator: DescribeVoicesPaginator = client.get_paginator("describe_voices")
    list_lexicons_paginator: ListLexiconsPaginator = client.get_paginator("list_lexicons")
    list_speech_synthesis_tasks_paginator: ListSpeechSynthesisTasksPaginator = client.get_paginator("list_speech_synthesis_tasks")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_polly.literals import Engine, LanguageCode, TaskStatus
from mypy_boto3_polly.type_defs import (
    DescribeVoicesOutputTypeDef,
    ListLexiconsOutputTypeDef,
    ListSpeechSynthesisTasksOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("DescribeVoicesPaginator", "ListLexiconsPaginator", "ListSpeechSynthesisTasksPaginator")


class DescribeVoicesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVoices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Paginator.DescribeVoices)
    """

    def paginate(
        self,
        Engine: Engine = None,
        LanguageCode: LanguageCode = None,
        IncludeAdditionalLanguageCodes: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[DescribeVoicesOutputTypeDef]:
        """
        [DescribeVoices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Paginator.DescribeVoices.paginate)
        """


class ListLexiconsPaginator(Boto3Paginator):
    """
    [Paginator.ListLexicons documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Paginator.ListLexicons)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLexiconsOutputTypeDef]:
        """
        [ListLexicons.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Paginator.ListLexicons.paginate)
        """


class ListSpeechSynthesisTasksPaginator(Boto3Paginator):
    """
    [Paginator.ListSpeechSynthesisTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Paginator.ListSpeechSynthesisTasks)
    """

    def paginate(
        self, Status: TaskStatus = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSpeechSynthesisTasksOutputTypeDef]:
        """
        [ListSpeechSynthesisTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/polly.html#Polly.Paginator.ListSpeechSynthesisTasks.paginate)
        """
