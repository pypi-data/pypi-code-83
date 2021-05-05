"""
Type annotations for outposts service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_outposts import OutpostsClient

    client: OutpostsClient = boto3.client("outposts")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_outposts.type_defs import (
    CreateOutpostOutputTypeDef,
    GetOutpostInstanceTypesOutputTypeDef,
    GetOutpostOutputTypeDef,
    ListOutpostsOutputTypeDef,
    ListSitesOutputTypeDef,
    ListTagsForResourceResponseTypeDef,
)

__all__ = ("OutpostsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class OutpostsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/outposts.html#Outposts.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/outposts.html#Outposts.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#can-paginate)
        """

    def create_outpost(
        self,
        Name: str,
        SiteId: str,
        Description: str = None,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateOutpostOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/outposts.html#Outposts.Client.create_outpost)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#create-outpost)
        """

    def delete_outpost(self, OutpostId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/outposts.html#Outposts.Client.delete_outpost)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#delete-outpost)
        """

    def delete_site(self, SiteId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/outposts.html#Outposts.Client.delete_site)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#delete-site)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/outposts.html#Outposts.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#generate-presigned-url)
        """

    def get_outpost(self, OutpostId: str) -> GetOutpostOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/outposts.html#Outposts.Client.get_outpost)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#get-outpost)
        """

    def get_outpost_instance_types(
        self, OutpostId: str, NextToken: str = None, MaxResults: int = None
    ) -> GetOutpostInstanceTypesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/outposts.html#Outposts.Client.get_outpost_instance_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#get-outpost-instance-types)
        """

    def list_outposts(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListOutpostsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/outposts.html#Outposts.Client.list_outposts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#list-outposts)
        """

    def list_sites(self, NextToken: str = None, MaxResults: int = None) -> ListSitesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/outposts.html#Outposts.Client.list_sites)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#list-sites)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/outposts.html#Outposts.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#list-tags-for-resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/outposts.html#Outposts.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/outposts.html#Outposts.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_outposts/client.html#untag-resource)
        """
