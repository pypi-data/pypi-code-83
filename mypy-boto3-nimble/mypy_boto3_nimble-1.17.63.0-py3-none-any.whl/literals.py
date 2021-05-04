"""
Type annotations for nimble service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/literals.html)

Usage::

    ```python
    from mypy_boto3_nimble.literals import LaunchProfilePersona

    data: LaunchProfilePersona = "USER"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "LaunchProfilePersona",
    "LaunchProfilePlatform",
    "LaunchProfileState",
    "LaunchProfileStatusCode",
    "ListEulaAcceptancesPaginatorName",
    "ListEulasPaginatorName",
    "ListLaunchProfileMembersPaginatorName",
    "ListLaunchProfilesPaginatorName",
    "ListStreamingImagesPaginatorName",
    "ListStreamingSessionsPaginatorName",
    "ListStudioComponentsPaginatorName",
    "ListStudioMembersPaginatorName",
    "ListStudiosPaginatorName",
    "StreamingClipboardMode",
    "StreamingImageEncryptionConfigurationKeyType",
    "StreamingImageState",
    "StreamingImageStatusCode",
    "StreamingInstanceType",
    "StreamingSessionState",
    "StreamingSessionStatusCode",
    "StreamingSessionStreamState",
    "StreamingSessionStreamStatusCode",
    "StudioComponentInitializationScriptRunContext",
    "StudioComponentState",
    "StudioComponentStatusCode",
    "StudioComponentSubtype",
    "StudioComponentType",
    "StudioEncryptionConfigurationKeyType",
    "StudioPersona",
    "StudioState",
    "StudioStatusCode",
)


LaunchProfilePersona = Literal["USER"]
LaunchProfilePlatform = Literal["LINUX", "WINDOWS"]
LaunchProfileState = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
LaunchProfileStatusCode = Literal[
    "ENCRYPTION_KEY_ACCESS_DENIED",
    "ENCRYPTION_KEY_NOT_FOUND",
    "INTERNAL_ERROR",
    "INVALID_SUBNETS_PROVIDED",
    "LAUNCH_PROFILE_CREATED",
    "LAUNCH_PROFILE_CREATE_IN_PROGRESS",
    "LAUNCH_PROFILE_DELETED",
    "LAUNCH_PROFILE_DELETE_IN_PROGRESS",
    "LAUNCH_PROFILE_UPDATED",
    "LAUNCH_PROFILE_UPDATE_IN_PROGRESS",
    "LAUNCH_PROFILE_WITH_STREAM_SESSIONS_NOT_DELETED",
    "STREAMING_IMAGE_NOT_FOUND",
    "STREAMING_IMAGE_NOT_READY",
]
ListEulaAcceptancesPaginatorName = Literal["list_eula_acceptances"]
ListEulasPaginatorName = Literal["list_eulas"]
ListLaunchProfileMembersPaginatorName = Literal["list_launch_profile_members"]
ListLaunchProfilesPaginatorName = Literal["list_launch_profiles"]
ListStreamingImagesPaginatorName = Literal["list_streaming_images"]
ListStreamingSessionsPaginatorName = Literal["list_streaming_sessions"]
ListStudioComponentsPaginatorName = Literal["list_studio_components"]
ListStudioMembersPaginatorName = Literal["list_studio_members"]
ListStudiosPaginatorName = Literal["list_studios"]
StreamingClipboardMode = Literal["DISABLED", "ENABLED"]
StreamingImageEncryptionConfigurationKeyType = Literal["CUSTOMER_MANAGED_KEY"]
StreamingImageState = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
StreamingImageStatusCode = Literal[
    "INTERNAL_ERROR",
    "STREAMING_IMAGE_CREATE_IN_PROGRESS",
    "STREAMING_IMAGE_DELETED",
    "STREAMING_IMAGE_DELETE_IN_PROGRESS",
    "STREAMING_IMAGE_READY",
    "STREAMING_IMAGE_UPDATE_IN_PROGRESS",
]
StreamingInstanceType = Literal[
    "g4dn.12xlarge", "g4dn.16xlarge", "g4dn.2xlarge", "g4dn.4xlarge", "g4dn.8xlarge", "g4dn.xlarge"
]
StreamingSessionState = Literal[
    "CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETED", "DELETE_FAILED", "DELETE_IN_PROGRESS", "READY"
]
StreamingSessionStatusCode = Literal[
    "ACTIVE_DIRECTORY_DOMAIN_JOIN_ERROR",
    "DECRYPT_STREAMING_IMAGE_ERROR",
    "INITIALIZATION_SCRIPT_ERROR",
    "INSUFFICIENT_CAPACITY",
    "INTERNAL_ERROR",
    "NETWORK_CONNECTION_ERROR",
    "NETWORK_INTERFACE_ERROR",
    "STREAMING_SESSION_CREATE_IN_PROGRESS",
    "STREAMING_SESSION_DELETED",
    "STREAMING_SESSION_DELETE_IN_PROGRESS",
    "STREAMING_SESSION_READY",
]
StreamingSessionStreamState = Literal[
    "CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETED", "DELETE_FAILED", "DELETE_IN_PROGRESS", "READY"
]
StreamingSessionStreamStatusCode = Literal[
    "INTERNAL_ERROR",
    "NETWORK_CONNECTION_ERROR",
    "STREAM_CREATE_IN_PROGRESS",
    "STREAM_DELETED",
    "STREAM_DELETE_IN_PROGRESS",
    "STREAM_READY",
]
StudioComponentInitializationScriptRunContext = Literal[
    "SYSTEM_INITIALIZATION", "USER_INITIALIZATION"
]
StudioComponentState = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
StudioComponentStatusCode = Literal[
    "ACTIVE_DIRECTORY_ALREADY_EXISTS",
    "ENCRYPTION_KEY_ACCESS_DENIED",
    "ENCRYPTION_KEY_NOT_FOUND",
    "INTERNAL_ERROR",
    "STUDIO_COMPONENT_CREATED",
    "STUDIO_COMPONENT_CREATE_IN_PROGRESS",
    "STUDIO_COMPONENT_DELETED",
    "STUDIO_COMPONENT_DELETE_IN_PROGRESS",
    "STUDIO_COMPONENT_UPDATED",
    "STUDIO_COMPONENT_UPDATE_IN_PROGRESS",
]
StudioComponentSubtype = Literal[
    "AMAZON_FSX_FOR_LUSTRE", "AMAZON_FSX_FOR_WINDOWS", "AWS_MANAGED_MICROSOFT_AD", "CUSTOM"
]
StudioComponentType = Literal[
    "ACTIVE_DIRECTORY", "COMPUTE_FARM", "CUSTOM", "LICENSE_SERVICE", "SHARED_FILE_SYSTEM"
]
StudioEncryptionConfigurationKeyType = Literal["AWS_OWNED_KEY", "CUSTOMER_MANAGED_KEY"]
StudioPersona = Literal["ADMINISTRATOR"]
StudioState = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "DELETED",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "READY",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
]
StudioStatusCode = Literal[
    "AWS_SSO_ACCESS_DENIED",
    "AWS_SSO_CONFIGURATION_REPAIRED",
    "AWS_SSO_CONFIGURATION_REPAIR_IN_PROGRESS",
    "AWS_SSO_NOT_ENABLED",
    "ENCRYPTION_KEY_ACCESS_DENIED",
    "ENCRYPTION_KEY_NOT_FOUND",
    "INTERNAL_ERROR",
    "ROLE_COULD_NOT_BE_ASSUMED",
    "ROLE_NOT_OWNED_BY_STUDIO_OWNER",
    "STUDIO_CREATED",
    "STUDIO_CREATE_IN_PROGRESS",
    "STUDIO_DELETED",
    "STUDIO_DELETE_IN_PROGRESS",
    "STUDIO_UPDATED",
    "STUDIO_UPDATE_IN_PROGRESS",
    "STUDIO_WITH_LAUNCH_PROFILES_NOT_DELETED",
    "STUDIO_WITH_STREAMING_IMAGES_NOT_DELETED",
    "STUDIO_WITH_STUDIO_COMPONENTS_NOT_DELETED",
]
