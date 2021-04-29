"""
Main interface for codeguru-reviewer service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_codeguru_reviewer import CodeGuruReviewerClient
    from mypy_boto3_codeguru_reviewer.paginator import (
        ListRepositoryAssociationsPaginator,
    )

    client: CodeGuruReviewerClient = boto3.client("codeguru-reviewer")

    list_repository_associations_paginator: ListRepositoryAssociationsPaginator = client.get_paginator("list_repository_associations")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_codeguru_reviewer.literals import ProviderType, RepositoryAssociationState
from mypy_boto3_codeguru_reviewer.type_defs import (
    ListRepositoryAssociationsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListRepositoryAssociationsPaginator",)


class ListRepositoryAssociationsPaginator(Boto3Paginator):
    """
    [Paginator.ListRepositoryAssociations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Paginator.ListRepositoryAssociations)
    """

    def paginate(
        self,
        ProviderTypes: List[ProviderType] = None,
        States: List[RepositoryAssociationState] = None,
        Names: List[str] = None,
        Owners: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListRepositoryAssociationsResponseTypeDef]:
        """
        [ListRepositoryAssociations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/codeguru-reviewer.html#CodeGuruReviewer.Paginator.ListRepositoryAssociations.paginate)
        """
