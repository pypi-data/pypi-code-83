"""
Main interface for emr-containers service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_emr_containers import EMRContainersClient
    from mypy_boto3_emr_containers.paginator import (
        ListJobRunsPaginator,
        ListManagedEndpointsPaginator,
        ListVirtualClustersPaginator,
    )

    client: EMRContainersClient = boto3.client("emr-containers")

    list_job_runs_paginator: ListJobRunsPaginator = client.get_paginator("list_job_runs")
    list_managed_endpoints_paginator: ListManagedEndpointsPaginator = client.get_paginator("list_managed_endpoints")
    list_virtual_clusters_paginator: ListVirtualClustersPaginator = client.get_paginator("list_virtual_clusters")
    ```
"""
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_emr_containers.literals import (
    ContainerProviderType,
    EndpointState,
    JobRunState,
    VirtualClusterState,
)
from mypy_boto3_emr_containers.type_defs import (
    ListJobRunsResponseTypeDef,
    ListManagedEndpointsResponseTypeDef,
    ListVirtualClustersResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListJobRunsPaginator", "ListManagedEndpointsPaginator", "ListVirtualClustersPaginator")


class ListJobRunsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr-containers.html#EMRContainers.Paginator.ListJobRuns)
    """

    def paginate(
        self,
        virtualClusterId: str,
        createdBefore: datetime = None,
        createdAfter: datetime = None,
        name: str = None,
        states: List[JobRunState] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListJobRunsResponseTypeDef]:
        """
        [ListJobRuns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr-containers.html#EMRContainers.Paginator.ListJobRuns.paginate)
        """


class ListManagedEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.ListManagedEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr-containers.html#EMRContainers.Paginator.ListManagedEndpoints)
    """

    def paginate(
        self,
        virtualClusterId: str,
        createdBefore: datetime = None,
        createdAfter: datetime = None,
        types: List[str] = None,
        states: List[EndpointState] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListManagedEndpointsResponseTypeDef]:
        """
        [ListManagedEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr-containers.html#EMRContainers.Paginator.ListManagedEndpoints.paginate)
        """


class ListVirtualClustersPaginator(Boto3Paginator):
    """
    [Paginator.ListVirtualClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr-containers.html#EMRContainers.Paginator.ListVirtualClusters)
    """

    def paginate(
        self,
        containerProviderId: str = None,
        containerProviderType: ContainerProviderType = None,
        createdAfter: datetime = None,
        createdBefore: datetime = None,
        states: List[VirtualClusterState] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListVirtualClustersResponseTypeDef]:
        """
        [ListVirtualClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr-containers.html#EMRContainers.Paginator.ListVirtualClusters.paginate)
        """
