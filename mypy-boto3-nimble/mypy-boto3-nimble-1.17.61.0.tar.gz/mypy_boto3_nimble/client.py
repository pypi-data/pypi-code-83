"""
Main interface for nimble service client

Usage::

    ```python
    import boto3
    from mypy_boto3_nimble import NimbleStudioClient

    client: NimbleStudioClient = boto3.client("nimble")
    ```
"""
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_nimble.literals import (
    LaunchProfilePersona,
    ListEulaAcceptancesPaginatorName,
    ListEulasPaginatorName,
    ListLaunchProfileMembersPaginatorName,
    ListLaunchProfilesPaginatorName,
    ListStreamingImagesPaginatorName,
    ListStreamingSessionsPaginatorName,
    ListStudioComponentsPaginatorName,
    ListStudioMembersPaginatorName,
    ListStudiosPaginatorName,
    StreamingInstanceType,
    StudioComponentSubtype,
    StudioComponentType,
)
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
from mypy_boto3_nimble.type_defs import (
    AcceptEulasResponseTypeDef,
    CreateLaunchProfileResponseTypeDef,
    CreateStreamingImageResponseTypeDef,
    CreateStreamingSessionResponseTypeDef,
    CreateStreamingSessionStreamResponseTypeDef,
    CreateStudioComponentResponseTypeDef,
    CreateStudioResponseTypeDef,
    DeleteLaunchProfileResponseTypeDef,
    DeleteStreamingImageResponseTypeDef,
    DeleteStreamingSessionResponseTypeDef,
    DeleteStudioComponentResponseTypeDef,
    DeleteStudioResponseTypeDef,
    GetEulaResponseTypeDef,
    GetLaunchProfileDetailsResponseTypeDef,
    GetLaunchProfileInitializationResponseTypeDef,
    GetLaunchProfileMemberResponseTypeDef,
    GetLaunchProfileResponseTypeDef,
    GetStreamingImageResponseTypeDef,
    GetStreamingSessionResponseTypeDef,
    GetStreamingSessionStreamResponseTypeDef,
    GetStudioComponentResponseTypeDef,
    GetStudioMemberResponseTypeDef,
    GetStudioResponseTypeDef,
    ListEulaAcceptancesResponseTypeDef,
    ListEulasResponseTypeDef,
    ListLaunchProfileMembersResponseTypeDef,
    ListLaunchProfilesResponseTypeDef,
    ListStreamingImagesResponseTypeDef,
    ListStreamingSessionsResponseTypeDef,
    ListStudioComponentsResponseTypeDef,
    ListStudioMembersResponseTypeDef,
    ListStudiosResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    NewLaunchProfileMemberTypeDef,
    NewStudioMemberTypeDef,
    ScriptParameterKeyValueTypeDef,
    StartStudioSSOConfigurationRepairResponseTypeDef,
    StreamConfigurationCreateTypeDef,
    StudioComponentConfigurationTypeDef,
    StudioComponentInitializationScriptTypeDef,
    StudioEncryptionConfigurationTypeDef,
    UpdateLaunchProfileMemberResponseTypeDef,
    UpdateLaunchProfileResponseTypeDef,
    UpdateStreamingImageResponseTypeDef,
    UpdateStudioComponentResponseTypeDef,
    UpdateStudioResponseTypeDef,
)

__all__ = ("NimbleStudioClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class NimbleStudioClient:
    """
    [NimbleStudio.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_eulas(
        self, studioId: str, clientToken: str = None, eulaIds: List[str] = None
    ) -> AcceptEulasResponseTypeDef:
        """
        [Client.accept_eulas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.accept_eulas)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.can_paginate)
        """

    def create_launch_profile(
        self,
        ec2SubnetIds: List[str],
        launchProfileProtocolVersions: List[str],
        name: str,
        streamConfiguration: StreamConfigurationCreateTypeDef,
        studioComponentIds: List[str],
        studioId: str,
        clientToken: str = None,
        description: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateLaunchProfileResponseTypeDef:
        """
        [Client.create_launch_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.create_launch_profile)
        """

    def create_streaming_image(
        self,
        ec2ImageId: str,
        name: str,
        studioId: str,
        clientToken: str = None,
        description: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateStreamingImageResponseTypeDef:
        """
        [Client.create_streaming_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.create_streaming_image)
        """

    def create_streaming_session(
        self,
        studioId: str,
        clientToken: str = None,
        ec2InstanceType: StreamingInstanceType = None,
        launchProfileId: str = None,
        streamingImageId: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateStreamingSessionResponseTypeDef:
        """
        [Client.create_streaming_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.create_streaming_session)
        """

    def create_streaming_session_stream(
        self,
        sessionId: str,
        studioId: str,
        clientToken: str = None,
        expirationInSeconds: int = None,
    ) -> CreateStreamingSessionStreamResponseTypeDef:
        """
        [Client.create_streaming_session_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.create_streaming_session_stream)
        """

    def create_studio(
        self,
        adminRoleArn: str,
        displayName: str,
        studioName: str,
        userRoleArn: str,
        clientToken: str = None,
        studioEncryptionConfiguration: "StudioEncryptionConfigurationTypeDef" = None,
        tags: Dict[str, str] = None,
    ) -> CreateStudioResponseTypeDef:
        """
        [Client.create_studio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.create_studio)
        """

    def create_studio_component(
        self,
        name: str,
        studioId: str,
        type: StudioComponentType,
        clientToken: str = None,
        configuration: "StudioComponentConfigurationTypeDef" = None,
        description: str = None,
        ec2SecurityGroupIds: List[str] = None,
        initializationScripts: List["StudioComponentInitializationScriptTypeDef"] = None,
        scriptParameters: List["ScriptParameterKeyValueTypeDef"] = None,
        subtype: StudioComponentSubtype = None,
        tags: Dict[str, str] = None,
    ) -> CreateStudioComponentResponseTypeDef:
        """
        [Client.create_studio_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.create_studio_component)
        """

    def delete_launch_profile(
        self, launchProfileId: str, studioId: str, clientToken: str = None
    ) -> DeleteLaunchProfileResponseTypeDef:
        """
        [Client.delete_launch_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.delete_launch_profile)
        """

    def delete_launch_profile_member(
        self, launchProfileId: str, principalId: str, studioId: str, clientToken: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_launch_profile_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.delete_launch_profile_member)
        """

    def delete_streaming_image(
        self, streamingImageId: str, studioId: str, clientToken: str = None
    ) -> DeleteStreamingImageResponseTypeDef:
        """
        [Client.delete_streaming_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.delete_streaming_image)
        """

    def delete_streaming_session(
        self, sessionId: str, studioId: str, clientToken: str = None
    ) -> DeleteStreamingSessionResponseTypeDef:
        """
        [Client.delete_streaming_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.delete_streaming_session)
        """

    def delete_studio(self, studioId: str, clientToken: str = None) -> DeleteStudioResponseTypeDef:
        """
        [Client.delete_studio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.delete_studio)
        """

    def delete_studio_component(
        self, studioComponentId: str, studioId: str, clientToken: str = None
    ) -> DeleteStudioComponentResponseTypeDef:
        """
        [Client.delete_studio_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.delete_studio_component)
        """

    def delete_studio_member(
        self, principalId: str, studioId: str, clientToken: str = None
    ) -> Dict[str, Any]:
        """
        [Client.delete_studio_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.delete_studio_member)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.generate_presigned_url)
        """

    def get_eula(self, eulaId: str) -> GetEulaResponseTypeDef:
        """
        [Client.get_eula documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.get_eula)
        """

    def get_launch_profile(
        self, launchProfileId: str, studioId: str
    ) -> GetLaunchProfileResponseTypeDef:
        """
        [Client.get_launch_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile)
        """

    def get_launch_profile_details(
        self, launchProfileId: str, studioId: str
    ) -> GetLaunchProfileDetailsResponseTypeDef:
        """
        [Client.get_launch_profile_details documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile_details)
        """

    def get_launch_profile_initialization(
        self,
        launchProfileId: str,
        launchProfileProtocolVersions: List[str],
        launchPurpose: str,
        platform: str,
        studioId: str,
    ) -> GetLaunchProfileInitializationResponseTypeDef:
        """
        [Client.get_launch_profile_initialization documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile_initialization)
        """

    def get_launch_profile_member(
        self, launchProfileId: str, principalId: str, studioId: str
    ) -> GetLaunchProfileMemberResponseTypeDef:
        """
        [Client.get_launch_profile_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.get_launch_profile_member)
        """

    def get_streaming_image(
        self, streamingImageId: str, studioId: str
    ) -> GetStreamingImageResponseTypeDef:
        """
        [Client.get_streaming_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.get_streaming_image)
        """

    def get_streaming_session(
        self, sessionId: str, studioId: str
    ) -> GetStreamingSessionResponseTypeDef:
        """
        [Client.get_streaming_session documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.get_streaming_session)
        """

    def get_streaming_session_stream(
        self, sessionId: str, streamId: str, studioId: str
    ) -> GetStreamingSessionStreamResponseTypeDef:
        """
        [Client.get_streaming_session_stream documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.get_streaming_session_stream)
        """

    def get_studio(self, studioId: str) -> GetStudioResponseTypeDef:
        """
        [Client.get_studio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.get_studio)
        """

    def get_studio_component(
        self, studioComponentId: str, studioId: str
    ) -> GetStudioComponentResponseTypeDef:
        """
        [Client.get_studio_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.get_studio_component)
        """

    def get_studio_member(self, principalId: str, studioId: str) -> GetStudioMemberResponseTypeDef:
        """
        [Client.get_studio_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.get_studio_member)
        """

    def list_eula_acceptances(
        self, studioId: str, eulaIds: List[str] = None, nextToken: str = None
    ) -> ListEulaAcceptancesResponseTypeDef:
        """
        [Client.list_eula_acceptances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.list_eula_acceptances)
        """

    def list_eulas(
        self, eulaIds: List[str] = None, nextToken: str = None
    ) -> ListEulasResponseTypeDef:
        """
        [Client.list_eulas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.list_eulas)
        """

    def list_launch_profile_members(
        self, launchProfileId: str, studioId: str, maxResults: int = None, nextToken: str = None
    ) -> ListLaunchProfileMembersResponseTypeDef:
        """
        [Client.list_launch_profile_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.list_launch_profile_members)
        """

    def list_launch_profiles(
        self,
        studioId: str,
        maxResults: int = None,
        nextToken: str = None,
        principalId: str = None,
        states: List[str] = None,
    ) -> ListLaunchProfilesResponseTypeDef:
        """
        [Client.list_launch_profiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.list_launch_profiles)
        """

    def list_streaming_images(
        self, studioId: str, nextToken: str = None, owner: str = None
    ) -> ListStreamingImagesResponseTypeDef:
        """
        [Client.list_streaming_images documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.list_streaming_images)
        """

    def list_streaming_sessions(
        self, studioId: str, createdBy: str = None, nextToken: str = None, sessionIds: str = None
    ) -> ListStreamingSessionsResponseTypeDef:
        """
        [Client.list_streaming_sessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.list_streaming_sessions)
        """

    def list_studio_components(
        self,
        studioId: str,
        maxResults: int = None,
        nextToken: str = None,
        states: List[str] = None,
        types: List[str] = None,
    ) -> ListStudioComponentsResponseTypeDef:
        """
        [Client.list_studio_components documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.list_studio_components)
        """

    def list_studio_members(
        self, studioId: str, maxResults: int = None, nextToken: str = None
    ) -> ListStudioMembersResponseTypeDef:
        """
        [Client.list_studio_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.list_studio_members)
        """

    def list_studios(self, nextToken: str = None) -> ListStudiosResponseTypeDef:
        """
        [Client.list_studios documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.list_studios)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.list_tags_for_resource)
        """

    def put_launch_profile_members(
        self,
        identityStoreId: str,
        launchProfileId: str,
        members: List[NewLaunchProfileMemberTypeDef],
        studioId: str,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_launch_profile_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.put_launch_profile_members)
        """

    def put_studio_members(
        self,
        identityStoreId: str,
        members: List[NewStudioMemberTypeDef],
        studioId: str,
        clientToken: str = None,
    ) -> Dict[str, Any]:
        """
        [Client.put_studio_members documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.put_studio_members)
        """

    def start_studio_sso_configuration_repair(
        self, studioId: str, clientToken: str = None
    ) -> StartStudioSSOConfigurationRepairResponseTypeDef:
        """
        [Client.start_studio_sso_configuration_repair documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.start_studio_sso_configuration_repair)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str] = None) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.tag_resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.untag_resource)
        """

    def update_launch_profile(
        self,
        launchProfileId: str,
        studioId: str,
        clientToken: str = None,
        description: str = None,
        launchProfileProtocolVersions: List[str] = None,
        name: str = None,
        streamConfiguration: StreamConfigurationCreateTypeDef = None,
        studioComponentIds: List[str] = None,
    ) -> UpdateLaunchProfileResponseTypeDef:
        """
        [Client.update_launch_profile documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.update_launch_profile)
        """

    def update_launch_profile_member(
        self,
        launchProfileId: str,
        persona: LaunchProfilePersona,
        principalId: str,
        studioId: str,
        clientToken: str = None,
    ) -> UpdateLaunchProfileMemberResponseTypeDef:
        """
        [Client.update_launch_profile_member documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.update_launch_profile_member)
        """

    def update_streaming_image(
        self,
        streamingImageId: str,
        studioId: str,
        clientToken: str = None,
        description: str = None,
        name: str = None,
    ) -> UpdateStreamingImageResponseTypeDef:
        """
        [Client.update_streaming_image documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.update_streaming_image)
        """

    def update_studio(
        self,
        studioId: str,
        adminRoleArn: str = None,
        clientToken: str = None,
        displayName: str = None,
        userRoleArn: str = None,
    ) -> UpdateStudioResponseTypeDef:
        """
        [Client.update_studio documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.update_studio)
        """

    def update_studio_component(
        self,
        studioComponentId: str,
        studioId: str,
        clientToken: str = None,
        configuration: "StudioComponentConfigurationTypeDef" = None,
        description: str = None,
        ec2SecurityGroupIds: List[str] = None,
        initializationScripts: List["StudioComponentInitializationScriptTypeDef"] = None,
        name: str = None,
        scriptParameters: List["ScriptParameterKeyValueTypeDef"] = None,
        subtype: StudioComponentSubtype = None,
        type: StudioComponentType = None,
    ) -> UpdateStudioComponentResponseTypeDef:
        """
        [Client.update_studio_component documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Client.update_studio_component)
        """

    @overload
    def get_paginator(
        self, operation_name: ListEulaAcceptancesPaginatorName
    ) -> ListEulaAcceptancesPaginator:
        """
        [Paginator.ListEulaAcceptances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Paginator.ListEulaAcceptances)
        """

    @overload
    def get_paginator(self, operation_name: ListEulasPaginatorName) -> ListEulasPaginator:
        """
        [Paginator.ListEulas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Paginator.ListEulas)
        """

    @overload
    def get_paginator(
        self, operation_name: ListLaunchProfileMembersPaginatorName
    ) -> ListLaunchProfileMembersPaginator:
        """
        [Paginator.ListLaunchProfileMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfileMembers)
        """

    @overload
    def get_paginator(
        self, operation_name: ListLaunchProfilesPaginatorName
    ) -> ListLaunchProfilesPaginator:
        """
        [Paginator.ListLaunchProfiles documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Paginator.ListLaunchProfiles)
        """

    @overload
    def get_paginator(
        self, operation_name: ListStreamingImagesPaginatorName
    ) -> ListStreamingImagesPaginator:
        """
        [Paginator.ListStreamingImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingImages)
        """

    @overload
    def get_paginator(
        self, operation_name: ListStreamingSessionsPaginatorName
    ) -> ListStreamingSessionsPaginator:
        """
        [Paginator.ListStreamingSessions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Paginator.ListStreamingSessions)
        """

    @overload
    def get_paginator(
        self, operation_name: ListStudioComponentsPaginatorName
    ) -> ListStudioComponentsPaginator:
        """
        [Paginator.ListStudioComponents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioComponents)
        """

    @overload
    def get_paginator(
        self, operation_name: ListStudioMembersPaginatorName
    ) -> ListStudioMembersPaginator:
        """
        [Paginator.ListStudioMembers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Paginator.ListStudioMembers)
        """

    @overload
    def get_paginator(self, operation_name: ListStudiosPaginatorName) -> ListStudiosPaginator:
        """
        [Paginator.ListStudios documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/nimble.html#NimbleStudio.Paginator.ListStudios)
        """
