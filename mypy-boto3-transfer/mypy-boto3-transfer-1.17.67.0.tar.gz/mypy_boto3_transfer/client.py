"""
Type annotations for transfer service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_transfer import TransferClient

    client: TransferClient = boto3.client("transfer")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_transfer.literals import (
    Domain,
    EndpointType,
    HomeDirectoryType,
    IdentityProviderType,
    ProtocolType,
)
from mypy_boto3_transfer.paginator import ListServersPaginator
from mypy_boto3_transfer.type_defs import (
    CreateServerResponseTypeDef,
    CreateUserResponseTypeDef,
    DescribeSecurityPolicyResponseTypeDef,
    DescribeServerResponseTypeDef,
    DescribeUserResponseTypeDef,
    EndpointDetailsTypeDef,
    HomeDirectoryMapEntryTypeDef,
    IdentityProviderDetailsTypeDef,
    ImportSshPublicKeyResponseTypeDef,
    ListSecurityPoliciesResponseTypeDef,
    ListServersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUsersResponseTypeDef,
    PosixProfileTypeDef,
    TagTypeDef,
    TestIdentityProviderResponseTypeDef,
    UpdateServerResponseTypeDef,
    UpdateUserResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("TransferClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServiceError: Type[BotocoreClientError]
    InvalidNextTokenException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    ResourceExistsException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class TransferClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#can-paginate)
        """

    def create_server(
        self,
        Certificate: str = None,
        Domain: Domain = None,
        EndpointDetails: "EndpointDetailsTypeDef" = None,
        EndpointType: EndpointType = None,
        HostKey: str = None,
        IdentityProviderDetails: "IdentityProviderDetailsTypeDef" = None,
        IdentityProviderType: IdentityProviderType = None,
        LoggingRole: str = None,
        Protocols: List[ProtocolType] = None,
        SecurityPolicyName: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateServerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.create_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#create-server)
        """

    def create_user(
        self,
        Role: str,
        ServerId: str,
        UserName: str,
        HomeDirectory: str = None,
        HomeDirectoryType: HomeDirectoryType = None,
        HomeDirectoryMappings: List["HomeDirectoryMapEntryTypeDef"] = None,
        Policy: str = None,
        PosixProfile: "PosixProfileTypeDef" = None,
        SshPublicKeyBody: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#create-user)
        """

    def delete_server(self, ServerId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.delete_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete-server)
        """

    def delete_ssh_public_key(self, ServerId: str, SshPublicKeyId: str, UserName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.delete_ssh_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete-ssh-public-key)
        """

    def delete_user(self, ServerId: str, UserName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#delete-user)
        """

    def describe_security_policy(
        self, SecurityPolicyName: str
    ) -> DescribeSecurityPolicyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.describe_security_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe-security-policy)
        """

    def describe_server(self, ServerId: str) -> DescribeServerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.describe_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe-server)
        """

    def describe_user(self, ServerId: str, UserName: str) -> DescribeUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.describe_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#describe-user)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#generate-presigned-url)
        """

    def import_ssh_public_key(
        self, ServerId: str, SshPublicKeyBody: str, UserName: str
    ) -> ImportSshPublicKeyResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.import_ssh_public_key)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#import-ssh-public-key)
        """

    def list_security_policies(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListSecurityPoliciesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.list_security_policies)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list-security-policies)
        """

    def list_servers(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListServersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.list_servers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list-servers)
        """

    def list_tags_for_resource(
        self, Arn: str, MaxResults: int = None, NextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list-tags-for-resource)
        """

    def list_users(
        self, ServerId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListUsersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#list-users)
        """

    def start_server(self, ServerId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.start_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#start-server)
        """

    def stop_server(self, ServerId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.stop_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#stop-server)
        """

    def tag_resource(self, Arn: str, Tags: List["TagTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#tag-resource)
        """

    def test_identity_provider(
        self,
        ServerId: str,
        UserName: str,
        ServerProtocol: ProtocolType = None,
        SourceIp: str = None,
        UserPassword: str = None,
    ) -> TestIdentityProviderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.test_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#test-identity-provider)
        """

    def untag_resource(self, Arn: str, TagKeys: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#untag-resource)
        """

    def update_server(
        self,
        ServerId: str,
        Certificate: str = None,
        EndpointDetails: "EndpointDetailsTypeDef" = None,
        EndpointType: EndpointType = None,
        HostKey: str = None,
        IdentityProviderDetails: "IdentityProviderDetailsTypeDef" = None,
        LoggingRole: str = None,
        Protocols: List[ProtocolType] = None,
        SecurityPolicyName: str = None,
    ) -> UpdateServerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.update_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#update-server)
        """

    def update_user(
        self,
        ServerId: str,
        UserName: str,
        HomeDirectory: str = None,
        HomeDirectoryType: HomeDirectoryType = None,
        HomeDirectoryMappings: List["HomeDirectoryMapEntryTypeDef"] = None,
        Policy: str = None,
        PosixProfile: "PosixProfileTypeDef" = None,
        Role: str = None,
    ) -> UpdateUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Client.update_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/client.html#update-user)
        """

    def get_paginator(self, operation_name: Literal["list_servers"]) -> ListServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/transfer.html#Transfer.Paginator.ListServers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transfer/paginators.html#listserverspaginator)
        """
