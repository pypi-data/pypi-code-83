"""
Type annotations for codestar-connections service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_codestar_connections import CodeStarconnectionsClient

    client: CodeStarconnectionsClient = boto3.client("codestar-connections")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_codestar_connections.literals import ProviderType
from mypy_boto3_codestar_connections.type_defs import (
    CreateConnectionOutputTypeDef,
    CreateHostOutputTypeDef,
    GetConnectionOutputTypeDef,
    GetHostOutputTypeDef,
    ListConnectionsOutputTypeDef,
    ListHostsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    TagTypeDef,
    VpcConfigurationTypeDef,
)

__all__ = ("CodeStarconnectionsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceUnavailableException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]


class CodeStarconnectionsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-connections.html#CodeStarconnections.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-connections.html#CodeStarconnections.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#can-paginate)
        """

    def create_connection(
        self,
        ConnectionName: str,
        ProviderType: ProviderType = None,
        Tags: List["TagTypeDef"] = None,
        HostArn: str = None,
    ) -> CreateConnectionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-connections.html#CodeStarconnections.Client.create_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#create-connection)
        """

    def create_host(
        self,
        Name: str,
        ProviderType: ProviderType,
        ProviderEndpoint: str,
        VpcConfiguration: "VpcConfigurationTypeDef" = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateHostOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-connections.html#CodeStarconnections.Client.create_host)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#create-host)
        """

    def delete_connection(self, ConnectionArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-connections.html#CodeStarconnections.Client.delete_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#delete-connection)
        """

    def delete_host(self, HostArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-connections.html#CodeStarconnections.Client.delete_host)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#delete-host)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-connections.html#CodeStarconnections.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#generate-presigned-url)
        """

    def get_connection(self, ConnectionArn: str) -> GetConnectionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-connections.html#CodeStarconnections.Client.get_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#get-connection)
        """

    def get_host(self, HostArn: str) -> GetHostOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-connections.html#CodeStarconnections.Client.get_host)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#get-host)
        """

    def list_connections(
        self,
        ProviderTypeFilter: ProviderType = None,
        HostArnFilter: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListConnectionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-connections.html#CodeStarconnections.Client.list_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#list-connections)
        """

    def list_hosts(self, MaxResults: int = None, NextToken: str = None) -> ListHostsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-connections.html#CodeStarconnections.Client.list_hosts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#list-hosts)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-connections.html#CodeStarconnections.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#list-tags-for-resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-connections.html#CodeStarconnections.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-connections.html#CodeStarconnections.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#untag-resource)
        """

    def update_host(
        self,
        HostArn: str,
        ProviderEndpoint: str = None,
        VpcConfiguration: "VpcConfigurationTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/codestar-connections.html#CodeStarconnections.Client.update_host)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/client.html#update-host)
        """
