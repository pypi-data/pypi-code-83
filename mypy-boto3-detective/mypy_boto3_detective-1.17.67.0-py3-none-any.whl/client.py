"""
Type annotations for detective service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_detective import DetectiveClient

    client: DetectiveClient = boto3.client("detective")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_detective.type_defs import (
    AccountTypeDef,
    CreateGraphResponseTypeDef,
    CreateMembersResponseTypeDef,
    DeleteMembersResponseTypeDef,
    GetMembersResponseTypeDef,
    ListGraphsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
)

__all__ = ("DetectiveClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class DetectiveClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_invitation(self, GraphArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.accept_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#accept-invitation)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#can-paginate)
        """

    def create_graph(self, Tags: Dict[str, str] = None) -> CreateGraphResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.create_graph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#create-graph)
        """

    def create_members(
        self,
        GraphArn: str,
        Accounts: List[AccountTypeDef],
        Message: str = None,
        DisableEmailNotification: bool = None,
    ) -> CreateMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.create_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#create-members)
        """

    def delete_graph(self, GraphArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.delete_graph)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#delete-graph)
        """

    def delete_members(self, GraphArn: str, AccountIds: List[str]) -> DeleteMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.delete_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#delete-members)
        """

    def disassociate_membership(self, GraphArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.disassociate_membership)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#disassociate-membership)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#generate-presigned-url)
        """

    def get_members(self, GraphArn: str, AccountIds: List[str]) -> GetMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.get_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#get-members)
        """

    def list_graphs(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListGraphsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.list_graphs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#list-graphs)
        """

    def list_invitations(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListInvitationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.list_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#list-invitations)
        """

    def list_members(
        self, GraphArn: str, NextToken: str = None, MaxResults: int = None
    ) -> ListMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.list_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#list-members)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#list-tags-for-resource)
        """

    def reject_invitation(self, GraphArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.reject_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#reject-invitation)
        """

    def start_monitoring_member(self, GraphArn: str, AccountId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.start_monitoring_member)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#start-monitoring-member)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/detective.html#Detective.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_detective/client.html#untag-resource)
        """
