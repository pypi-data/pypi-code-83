"""
Type annotations for mediastore service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_mediastore import MediaStoreClient

    client: MediaStoreClient = boto3.client("mediastore")
    ```
"""
import sys
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_mediastore.paginator import ListContainersPaginator
from mypy_boto3_mediastore.type_defs import (
    CorsRuleTypeDef,
    CreateContainerOutputTypeDef,
    DescribeContainerOutputTypeDef,
    GetContainerPolicyOutputTypeDef,
    GetCorsPolicyOutputTypeDef,
    GetLifecyclePolicyOutputTypeDef,
    GetMetricPolicyOutputTypeDef,
    ListContainersOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    MetricPolicyTypeDef,
    TagTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("MediaStoreClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ContainerInUseException: Type[BotocoreClientError]
    ContainerNotFoundException: Type[BotocoreClientError]
    CorsPolicyNotFoundException: Type[BotocoreClientError]
    InternalServerError: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    PolicyNotFoundException: Type[BotocoreClientError]


class MediaStoreClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#can-paginate)
        """

    def create_container(
        self, ContainerName: str, Tags: List["TagTypeDef"] = None
    ) -> CreateContainerOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.create_container)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#create-container)
        """

    def delete_container(self, ContainerName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.delete_container)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#delete-container)
        """

    def delete_container_policy(self, ContainerName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.delete_container_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#delete-container-policy)
        """

    def delete_cors_policy(self, ContainerName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.delete_cors_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#delete-cors-policy)
        """

    def delete_lifecycle_policy(self, ContainerName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.delete_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#delete-lifecycle-policy)
        """

    def delete_metric_policy(self, ContainerName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.delete_metric_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#delete-metric-policy)
        """

    def describe_container(self, ContainerName: str = None) -> DescribeContainerOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.describe_container)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#describe-container)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#generate-presigned-url)
        """

    def get_container_policy(self, ContainerName: str) -> GetContainerPolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.get_container_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#get-container-policy)
        """

    def get_cors_policy(self, ContainerName: str) -> GetCorsPolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.get_cors_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#get-cors-policy)
        """

    def get_lifecycle_policy(self, ContainerName: str) -> GetLifecyclePolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.get_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#get-lifecycle-policy)
        """

    def get_metric_policy(self, ContainerName: str) -> GetMetricPolicyOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.get_metric_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#get-metric-policy)
        """

    def list_containers(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListContainersOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.list_containers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#list-containers)
        """

    def list_tags_for_resource(self, Resource: str) -> ListTagsForResourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#list-tags-for-resource)
        """

    def put_container_policy(self, ContainerName: str, Policy: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.put_container_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#put-container-policy)
        """

    def put_cors_policy(
        self, ContainerName: str, CorsPolicy: List["CorsRuleTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.put_cors_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#put-cors-policy)
        """

    def put_lifecycle_policy(self, ContainerName: str, LifecyclePolicy: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.put_lifecycle_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#put-lifecycle-policy)
        """

    def put_metric_policy(
        self, ContainerName: str, MetricPolicy: "MetricPolicyTypeDef"
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.put_metric_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#put-metric-policy)
        """

    def start_access_logging(self, ContainerName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.start_access_logging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#start-access-logging)
        """

    def stop_access_logging(self, ContainerName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.stop_access_logging)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#stop-access-logging)
        """

    def tag_resource(self, Resource: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#tag-resource)
        """

    def untag_resource(self, Resource: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/client.html#untag-resource)
        """

    def get_paginator(self, operation_name: Literal["list_containers"]) -> ListContainersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/mediastore.html#MediaStore.Paginator.ListContainers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/paginators.html#listcontainerspaginator)
        """
