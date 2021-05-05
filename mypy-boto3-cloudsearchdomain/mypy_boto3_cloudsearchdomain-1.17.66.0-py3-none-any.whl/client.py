"""
Type annotations for cloudsearchdomain service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cloudsearchdomain import CloudSearchDomainClient

    client: CloudSearchDomainClient = boto3.client("cloudsearchdomain")
    ```
"""
from typing import IO, Any, Dict, Type, Union

from botocore.client import ClientMeta

from mypy_boto3_cloudsearchdomain.literals import ContentType, QueryParser
from mypy_boto3_cloudsearchdomain.type_defs import (
    SearchResponseTypeDef,
    SuggestResponseTypeDef,
    UploadDocumentsResponseTypeDef,
)

__all__ = ("CloudSearchDomainClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    DocumentServiceException: Type[BotocoreClientError]
    SearchException: Type[BotocoreClientError]


class CloudSearchDomainClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client.html#can-paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client.html#generate-presigned-url)
        """

    def search(
        self,
        query: str,
        cursor: str = None,
        expr: str = None,
        facet: str = None,
        filterQuery: str = None,
        highlight: str = None,
        partial: bool = None,
        queryOptions: str = None,
        queryParser: QueryParser = None,
        returnFields: str = None,
        size: int = None,
        sort: str = None,
        start: int = None,
        stats: str = None,
    ) -> SearchResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.search)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client.html#search)
        """

    def suggest(self, query: str, suggester: str, size: int = None) -> SuggestResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.suggest)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client.html#suggest)
        """

    def upload_documents(
        self, documents: Union[bytes, IO[bytes]], contentType: ContentType
    ) -> UploadDocumentsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/cloudsearchdomain.html#CloudSearchDomain.Client.upload_documents)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/client.html#upload-documents)
        """
