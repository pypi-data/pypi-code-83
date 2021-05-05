"""
Type annotations for emr-containers service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_emr_containers import EMRContainersClient

    client: EMRContainersClient = boto3.client("emr-containers")
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_emr_containers.literals import EndpointState, JobRunState, VirtualClusterState
from mypy_boto3_emr_containers.paginator import (
    ListJobRunsPaginator,
    ListManagedEndpointsPaginator,
    ListVirtualClustersPaginator,
)
from mypy_boto3_emr_containers.type_defs import (
    CancelJobRunResponseTypeDef,
    ConfigurationOverridesTypeDef,
    ContainerProviderTypeDef,
    CreateManagedEndpointResponseTypeDef,
    CreateVirtualClusterResponseTypeDef,
    DeleteManagedEndpointResponseTypeDef,
    DeleteVirtualClusterResponseTypeDef,
    DescribeJobRunResponseTypeDef,
    DescribeManagedEndpointResponseTypeDef,
    DescribeVirtualClusterResponseTypeDef,
    JobDriverTypeDef,
    ListJobRunsResponseTypeDef,
    ListManagedEndpointsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListVirtualClustersResponseTypeDef,
    StartJobRunResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EMRContainersClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class EMRContainersClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#can-paginate)
        """

    def cancel_job_run(self, id: str, virtualClusterId: str) -> CancelJobRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.cancel_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#cancel-job-run)
        """

    def create_managed_endpoint(
        self,
        name: str,
        virtualClusterId: str,
        type: str,
        releaseLabel: str,
        executionRoleArn: str,
        certificateArn: str,
        clientToken: str,
        configurationOverrides: "ConfigurationOverridesTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreateManagedEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.create_managed_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#create-managed-endpoint)
        """

    def create_virtual_cluster(
        self,
        name: str,
        containerProvider: "ContainerProviderTypeDef",
        clientToken: str,
        tags: Dict[str, str] = None,
    ) -> CreateVirtualClusterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.create_virtual_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#create-virtual-cluster)
        """

    def delete_managed_endpoint(
        self, id: str, virtualClusterId: str
    ) -> DeleteManagedEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.delete_managed_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#delete-managed-endpoint)
        """

    def delete_virtual_cluster(self, id: str) -> DeleteVirtualClusterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.delete_virtual_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#delete-virtual-cluster)
        """

    def describe_job_run(self, id: str, virtualClusterId: str) -> DescribeJobRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.describe_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#describe-job-run)
        """

    def describe_managed_endpoint(
        self, id: str, virtualClusterId: str
    ) -> DescribeManagedEndpointResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.describe_managed_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#describe-managed-endpoint)
        """

    def describe_virtual_cluster(self, id: str) -> DescribeVirtualClusterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.describe_virtual_cluster)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#describe-virtual-cluster)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#generate-presigned-url)
        """

    def list_job_runs(
        self,
        virtualClusterId: str,
        createdBefore: datetime = None,
        createdAfter: datetime = None,
        name: str = None,
        states: List[JobRunState] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListJobRunsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.list_job_runs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#list-job-runs)
        """

    def list_managed_endpoints(
        self,
        virtualClusterId: str,
        createdBefore: datetime = None,
        createdAfter: datetime = None,
        types: List[str] = None,
        states: List[EndpointState] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListManagedEndpointsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.list_managed_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#list-managed-endpoints)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#list-tags-for-resource)
        """

    def list_virtual_clusters(
        self,
        containerProviderId: str = None,
        containerProviderType: Literal["EKS"] = None,
        createdAfter: datetime = None,
        createdBefore: datetime = None,
        states: List[VirtualClusterState] = None,
        maxResults: int = None,
        nextToken: str = None,
    ) -> ListVirtualClustersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.list_virtual_clusters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#list-virtual-clusters)
        """

    def start_job_run(
        self,
        virtualClusterId: str,
        clientToken: str,
        executionRoleArn: str,
        releaseLabel: str,
        jobDriver: "JobDriverTypeDef",
        name: str = None,
        configurationOverrides: "ConfigurationOverridesTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> StartJobRunResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.start_job_run)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#start-job-run)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#tag-resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/client.html#untag-resource)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_job_runs"]) -> ListJobRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Paginator.ListJobRuns)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators.html#listjobrunspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_managed_endpoints"]
    ) -> ListManagedEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Paginator.ListManagedEndpoints)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators.html#listmanagedendpointspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_virtual_clusters"]
    ) -> ListVirtualClustersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/emr-containers.html#EMRContainers.Paginator.ListVirtualClusters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_emr_containers/paginators.html#listvirtualclusterspaginator)
        """
