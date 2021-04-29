"""
Main interface for nimble service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_nimble import NimbleStudioClient
    from mypy_boto3_nimble.paginator import (
        ListEulaAcceptancesPaginator,
        ListEulasPaginator,
        ListLaunchProfileMembersPaginator,
        ListLaunchProfilesPaginator,
        ListStreamingImagesPaginator,
        ListStreamingSessionsPaginator,
        ListStudioComponentsPaginator,
        ListStudioMembersPaginator,
        ListStudiosPaginator,
    )

    client: NimbleStudioClient = boto3.client("nimble")

    list_eula_acceptances_paginator: ListEulaAcceptancesPaginator = client.get_paginator("list_eula_acceptances")
    list_eulas_paginator: ListEulasPaginator = client.get_paginator("list_eulas")
    list_launch_profile_members_paginator: ListLaunchProfileMembersPaginator = client.get_paginator("list_launch_profile_members")
    list_launch_profiles_paginator: ListLaunchProfilesPaginator = client.get_paginator("list_launch_profiles")
    list_streaming_images_paginator: ListStreamingImagesPaginator = client.get_paginator("list_streaming_images")
    list_streaming_sessions_paginator: ListStreamingSessionsPaginator = client.get_paginator("list_streaming_sessions")
    list_studio_components_paginator: ListStudioComponentsPaginator = client.get_paginator("list_studio_components")
    list_studio_members_paginator: ListStudioMembersPaginator = client.get_paginator("list_studio_members")
    list_studios_paginator: ListStudiosPaginator = client.get_paginator("list_studios")
    ```
"""
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_nimble.type_defs import (
    ListEulaAcceptancesResponseTypeDef,
    ListEulasResponseTypeDef,
    ListLaunchProfileMembersResponseTypeDef,
    ListLaunchProfilesResponseTypeDef,
    ListStreamingImagesResponseTypeDef,
    ListStreamingSessionsResponseTypeDef,
    ListStudioComponentsResponseTypeDef,
    ListStudioMembersResponseTypeDef,
    ListStudiosResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListEulaAcceptancesPaginator",
    "ListEulasPaginator",
    "ListLaunchProfileMembersPaginator",
    "ListLaunchProfilesPaginator",
    "ListStreamingImagesPaginator",
    "ListStreamingSessionsPaginator",
    "ListStudioComponentsPaginator",
    "ListStudioMembersPaginator",
    "ListStudiosPaginator",
)


class ListEulaAcceptancesPaginator(Boto3Paginator):
    """
    [Paginator.ListEulaAcceptances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListEulaAcceptances)
    """

    def paginate(
        self,
        studioId: str,
        eulaIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListEulaAcceptancesResponseTypeDef]:
        """
        [ListEulaAcceptances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListEulaAcceptances.paginate)
        """


class ListEulasPaginator(Boto3Paginator):
    """
    [Paginator.ListEulas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListEulas)
    """

    def paginate(
        self, eulaIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListEulasResponseTypeDef]:
        """
        [ListEulas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListEulas.paginate)
        """


class ListLaunchProfileMembersPaginator(Boto3Paginator):
    """
    [Paginator.ListLaunchProfileMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfileMembers)
    """

    def paginate(
        self, launchProfileId: str, studioId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListLaunchProfileMembersResponseTypeDef]:
        """
        [ListLaunchProfileMembers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfileMembers.paginate)
        """


class ListLaunchProfilesPaginator(Boto3Paginator):
    """
    [Paginator.ListLaunchProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfiles)
    """

    def paginate(
        self,
        studioId: str,
        principalId: str = None,
        states: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListLaunchProfilesResponseTypeDef]:
        """
        [ListLaunchProfiles.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfiles.paginate)
        """


class ListStreamingImagesPaginator(Boto3Paginator):
    """
    [Paginator.ListStreamingImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingImages)
    """

    def paginate(
        self, studioId: str, owner: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStreamingImagesResponseTypeDef]:
        """
        [ListStreamingImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingImages.paginate)
        """


class ListStreamingSessionsPaginator(Boto3Paginator):
    """
    [Paginator.ListStreamingSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingSessions)
    """

    def paginate(
        self,
        studioId: str,
        createdBy: str = None,
        sessionIds: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListStreamingSessionsResponseTypeDef]:
        """
        [ListStreamingSessions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingSessions.paginate)
        """


class ListStudioComponentsPaginator(Boto3Paginator):
    """
    [Paginator.ListStudioComponents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioComponents)
    """

    def paginate(
        self,
        studioId: str,
        states: List[str] = None,
        types: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListStudioComponentsResponseTypeDef]:
        """
        [ListStudioComponents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioComponents.paginate)
        """


class ListStudioMembersPaginator(Boto3Paginator):
    """
    [Paginator.ListStudioMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioMembers)
    """

    def paginate(
        self, studioId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStudioMembersResponseTypeDef]:
        """
        [ListStudioMembers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioMembers.paginate)
        """


class ListStudiosPaginator(Boto3Paginator):
    """
    [Paginator.ListStudios documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListStudios)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListStudiosResponseTypeDef]:
        """
        [ListStudios.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.60/reference/services/nimble.html#NimbleStudio.Paginator.ListStudios.paginate)
        """
