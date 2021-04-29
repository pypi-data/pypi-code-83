"""
Main interface for sagemaker-a2i-runtime service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_sagemaker_a2i_runtime import AugmentedAIRuntimeClient
    from mypy_boto3_sagemaker_a2i_runtime.paginator import (
        ListHumanLoopsPaginator,
    )

    client: AugmentedAIRuntimeClient = boto3.client("sagemaker-a2i-runtime")

    list_human_loops_paginator: ListHumanLoopsPaginator = client.get_paginator("list_human_loops")
    ```
"""
from datetime import datetime
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_sagemaker_a2i_runtime.literals import SortOrder
from mypy_boto3_sagemaker_a2i_runtime.type_defs import (
    ListHumanLoopsResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("ListHumanLoopsPaginator",)


class ListHumanLoopsPaginator(Boto3Paginator):
    """
    [Paginator.ListHumanLoops documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Paginator.ListHumanLoops)
    """

    def paginate(
        self,
        FlowDefinitionArn: str,
        CreationTimeAfter: datetime = None,
        CreationTimeBefore: datetime = None,
        SortOrder: SortOrder = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListHumanLoopsResponseTypeDef]:
        """
        [ListHumanLoops.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/sagemaker-a2i-runtime.html#AugmentedAIRuntime.Paginator.ListHumanLoops.paginate)
        """
