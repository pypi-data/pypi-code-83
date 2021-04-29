"""
Main interface for emr service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_emr import EMRClient
    from mypy_boto3_emr.paginator import (
        ListBootstrapActionsPaginator,
        ListClustersPaginator,
        ListInstanceFleetsPaginator,
        ListInstanceGroupsPaginator,
        ListInstancesPaginator,
        ListNotebookExecutionsPaginator,
        ListSecurityConfigurationsPaginator,
        ListStepsPaginator,
        ListStudioSessionMappingsPaginator,
        ListStudiosPaginator,
    )

    client: EMRClient = boto3.client("emr")

    list_bootstrap_actions_paginator: ListBootstrapActionsPaginator = client.get_paginator("list_bootstrap_actions")
    list_clusters_paginator: ListClustersPaginator = client.get_paginator("list_clusters")
    list_instance_fleets_paginator: ListInstanceFleetsPaginator = client.get_paginator("list_instance_fleets")
    list_instance_groups_paginator: ListInstanceGroupsPaginator = client.get_paginator("list_instance_groups")
    list_instances_paginator: ListInstancesPaginator = client.get_paginator("list_instances")
    list_notebook_executions_paginator: ListNotebookExecutionsPaginator = client.get_paginator("list_notebook_executions")
    list_security_configurations_paginator: ListSecurityConfigurationsPaginator = client.get_paginator("list_security_configurations")
    list_steps_paginator: ListStepsPaginator = client.get_paginator("list_steps")
    list_studio_session_mappings_paginator: ListStudioSessionMappingsPaginator = client.get_paginator("list_studio_session_mappings")
    list_studios_paginator: ListStudiosPaginator = client.get_paginator("list_studios")
    ```
"""
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_emr.literals import (
    ClusterState,
    IdentityType,
    InstanceFleetType,
    InstanceGroupType,
    InstanceState,
    NotebookExecutionStatus,
    StepState,
)
from mypy_boto3_emr.type_defs import (
    ListBootstrapActionsOutputTypeDef,
    ListClustersOutputTypeDef,
    ListInstanceFleetsOutputTypeDef,
    ListInstanceGroupsOutputTypeDef,
    ListInstancesOutputTypeDef,
    ListNotebookExecutionsOutputTypeDef,
    ListSecurityConfigurationsOutputTypeDef,
    ListStepsOutputTypeDef,
    ListStudioSessionMappingsOutputTypeDef,
    ListStudiosOutputTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListBootstrapActionsPaginator",
    "ListClustersPaginator",
    "ListInstanceFleetsPaginator",
    "ListInstanceGroupsPaginator",
    "ListInstancesPaginator",
    "ListNotebookExecutionsPaginator",
    "ListSecurityConfigurationsPaginator",
    "ListStepsPaginator",
    "ListStudioSessionMappingsPaginator",
    "ListStudiosPaginator",
)


class ListBootstrapActionsPaginator(Boto3Paginator):
    """
    [Paginator.ListBootstrapActions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListBootstrapActions)
    """

    def paginate(
        self, ClusterId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListBootstrapActionsOutputTypeDef]:
        """
        [ListBootstrapActions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListBootstrapActions.paginate)
        """


class ListClustersPaginator(Boto3Paginator):
    """
    [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListClusters)
    """

    def paginate(
        self,
        CreatedAfter: datetime = None,
        CreatedBefore: datetime = None,
        ClusterStates: List[ClusterState] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListClustersOutputTypeDef]:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListClusters.paginate)
        """


class ListInstanceFleetsPaginator(Boto3Paginator):
    """
    [Paginator.ListInstanceFleets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListInstanceFleets)
    """

    def paginate(
        self, ClusterId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstanceFleetsOutputTypeDef]:
        """
        [ListInstanceFleets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListInstanceFleets.paginate)
        """


class ListInstanceGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListInstanceGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListInstanceGroups)
    """

    def paginate(
        self, ClusterId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListInstanceGroupsOutputTypeDef]:
        """
        [ListInstanceGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListInstanceGroups.paginate)
        """


class ListInstancesPaginator(Boto3Paginator):
    """
    [Paginator.ListInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListInstances)
    """

    def paginate(
        self,
        ClusterId: str,
        InstanceGroupId: str = None,
        InstanceGroupTypes: List[InstanceGroupType] = None,
        InstanceFleetId: str = None,
        InstanceFleetType: InstanceFleetType = None,
        InstanceStates: List[InstanceState] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListInstancesOutputTypeDef]:
        """
        [ListInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListInstances.paginate)
        """


class ListNotebookExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListNotebookExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListNotebookExecutions)
    """

    def paginate(
        self,
        EditorId: str = None,
        Status: NotebookExecutionStatus = None,
        From: datetime = None,
        To: datetime = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListNotebookExecutionsOutputTypeDef]:
        """
        [ListNotebookExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListNotebookExecutions.paginate)
        """


class ListSecurityConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListSecurityConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListSecurityConfigurations)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSecurityConfigurationsOutputTypeDef]:
        """
        [ListSecurityConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListSecurityConfigurations.paginate)
        """


class ListStepsPaginator(Boto3Paginator):
    """
    [Paginator.ListSteps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListSteps)
    """

    def paginate(
        self,
        ClusterId: str,
        StepStates: List[StepState] = None,
        StepIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListStepsOutputTypeDef]:
        """
        [ListSteps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListSteps.paginate)
        """


class ListStudioSessionMappingsPaginator(Boto3Paginator):
    """
    [Paginator.ListStudioSessionMappings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListStudioSessionMappings)
    """

    def paginate(
        self,
        StudioId: str = None,
        IdentityType: IdentityType = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListStudioSessionMappingsOutputTypeDef]:
        """
        [ListStudioSessionMappings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListStudioSessionMappings.paginate)
        """


class ListStudiosPaginator(Boto3Paginator):
    """
    [Paginator.ListStudios documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListStudios)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStudiosOutputTypeDef]:
        """
        [ListStudios.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/emr.html#EMR.Paginator.ListStudios.paginate)
        """
