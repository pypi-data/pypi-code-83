"""
Main interface for mediaconvert service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_mediaconvert import MediaConvertClient
    from mypy_boto3_mediaconvert.paginator import (
        DescribeEndpointsPaginator,
        ListJobTemplatesPaginator,
        ListJobsPaginator,
        ListPresetsPaginator,
        ListQueuesPaginator,
    )

    client: MediaConvertClient = boto3.client("mediaconvert")

    describe_endpoints_paginator: DescribeEndpointsPaginator = client.get_paginator("describe_endpoints")
    list_job_templates_paginator: ListJobTemplatesPaginator = client.get_paginator("list_job_templates")
    list_jobs_paginator: ListJobsPaginator = client.get_paginator("list_jobs")
    list_presets_paginator: ListPresetsPaginator = client.get_paginator("list_presets")
    list_queues_paginator: ListQueuesPaginator = client.get_paginator("list_queues")
    ```
"""
from typing import Iterator

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_mediaconvert.literals import (
    DescribeEndpointsMode,
    JobStatus,
    JobTemplateListBy,
    Order,
    PresetListBy,
    QueueListBy,
)
from mypy_boto3_mediaconvert.type_defs import (
    DescribeEndpointsResponseTypeDef,
    ListJobsResponseTypeDef,
    ListJobTemplatesResponseTypeDef,
    ListPresetsResponseTypeDef,
    ListQueuesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "DescribeEndpointsPaginator",
    "ListJobTemplatesPaginator",
    "ListJobsPaginator",
    "ListPresetsPaginator",
    "ListQueuesPaginator",
)


class DescribeEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/mediaconvert.html#MediaConvert.Paginator.DescribeEndpoints)
    """

    def paginate(
        self, Mode: DescribeEndpointsMode = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEndpointsResponseTypeDef]:
        """
        [DescribeEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/mediaconvert.html#MediaConvert.Paginator.DescribeEndpoints.paginate)
        """


class ListJobTemplatesPaginator(Boto3Paginator):
    """
    [Paginator.ListJobTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobTemplates)
    """

    def paginate(
        self,
        Category: str = None,
        ListBy: JobTemplateListBy = None,
        Order: Order = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListJobTemplatesResponseTypeDef]:
        """
        [ListJobTemplates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobTemplates.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobs)
    """

    def paginate(
        self,
        Order: Order = None,
        Queue: str = None,
        Status: JobStatus = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListJobsResponseTypeDef]:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/mediaconvert.html#MediaConvert.Paginator.ListJobs.paginate)
        """


class ListPresetsPaginator(Boto3Paginator):
    """
    [Paginator.ListPresets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/mediaconvert.html#MediaConvert.Paginator.ListPresets)
    """

    def paginate(
        self,
        Category: str = None,
        ListBy: PresetListBy = None,
        Order: Order = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListPresetsResponseTypeDef]:
        """
        [ListPresets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/mediaconvert.html#MediaConvert.Paginator.ListPresets.paginate)
        """


class ListQueuesPaginator(Boto3Paginator):
    """
    [Paginator.ListQueues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/mediaconvert.html#MediaConvert.Paginator.ListQueues)
    """

    def paginate(
        self,
        ListBy: QueueListBy = None,
        Order: Order = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListQueuesResponseTypeDef]:
        """
        [ListQueues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/mediaconvert.html#MediaConvert.Paginator.ListQueues.paginate)
        """
