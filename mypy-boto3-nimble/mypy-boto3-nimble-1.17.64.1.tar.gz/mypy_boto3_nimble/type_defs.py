"""
Type annotations for nimble service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_nimble/type_defs.html)

Usage::

    ```python
    from mypy_boto3_nimble.type_defs import AcceptEulasResponseTypeDef

    data: AcceptEulasResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_nimble.literals import (
    LaunchProfilePlatform,
    LaunchProfileState,
    LaunchProfileStatusCode,
    StreamingClipboardMode,
    StreamingImageState,
    StreamingImageStatusCode,
    StreamingInstanceType,
    StreamingSessionState,
    StreamingSessionStatusCode,
    StreamingSessionStreamState,
    StreamingSessionStreamStatusCode,
    StudioComponentInitializationScriptRunContext,
    StudioComponentState,
    StudioComponentStatusCode,
    StudioComponentSubtype,
    StudioComponentType,
    StudioEncryptionConfigurationKeyType,
    StudioState,
    StudioStatusCode,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptEulasResponseTypeDef",
    "ActiveDirectoryComputerAttributeTypeDef",
    "ActiveDirectoryConfigurationTypeDef",
    "ComputeFarmConfigurationTypeDef",
    "CreateLaunchProfileResponseTypeDef",
    "CreateStreamingImageResponseTypeDef",
    "CreateStreamingSessionResponseTypeDef",
    "CreateStreamingSessionStreamResponseTypeDef",
    "CreateStudioComponentResponseTypeDef",
    "CreateStudioResponseTypeDef",
    "DeleteLaunchProfileResponseTypeDef",
    "DeleteStreamingImageResponseTypeDef",
    "DeleteStreamingSessionResponseTypeDef",
    "DeleteStudioComponentResponseTypeDef",
    "DeleteStudioResponseTypeDef",
    "EulaAcceptanceTypeDef",
    "EulaTypeDef",
    "GetEulaResponseTypeDef",
    "GetLaunchProfileDetailsResponseTypeDef",
    "GetLaunchProfileInitializationResponseTypeDef",
    "GetLaunchProfileMemberResponseTypeDef",
    "GetLaunchProfileResponseTypeDef",
    "GetStreamingImageResponseTypeDef",
    "GetStreamingSessionResponseTypeDef",
    "GetStreamingSessionStreamResponseTypeDef",
    "GetStudioComponentResponseTypeDef",
    "GetStudioMemberResponseTypeDef",
    "GetStudioResponseTypeDef",
    "LaunchProfileInitializationActiveDirectoryTypeDef",
    "LaunchProfileInitializationScriptTypeDef",
    "LaunchProfileInitializationTypeDef",
    "LaunchProfileMembershipTypeDef",
    "LaunchProfileTypeDef",
    "LicenseServiceConfigurationTypeDef",
    "ListEulaAcceptancesResponseTypeDef",
    "ListEulasResponseTypeDef",
    "ListLaunchProfileMembersResponseTypeDef",
    "ListLaunchProfilesResponseTypeDef",
    "ListStreamingImagesResponseTypeDef",
    "ListStreamingSessionsResponseTypeDef",
    "ListStudioComponentsResponseTypeDef",
    "ListStudioMembersResponseTypeDef",
    "ListStudiosResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NewLaunchProfileMemberTypeDef",
    "NewStudioMemberTypeDef",
    "PaginatorConfigTypeDef",
    "ScriptParameterKeyValueTypeDef",
    "SharedFileSystemConfigurationTypeDef",
    "StartStudioSSOConfigurationRepairResponseTypeDef",
    "StreamConfigurationCreateTypeDef",
    "StreamConfigurationTypeDef",
    "StreamingImageEncryptionConfigurationTypeDef",
    "StreamingImageTypeDef",
    "StreamingSessionStreamTypeDef",
    "StreamingSessionTypeDef",
    "StudioComponentConfigurationTypeDef",
    "StudioComponentInitializationScriptTypeDef",
    "StudioComponentSummaryTypeDef",
    "StudioComponentTypeDef",
    "StudioEncryptionConfigurationTypeDef",
    "StudioMembershipTypeDef",
    "StudioTypeDef",
    "UpdateLaunchProfileMemberResponseTypeDef",
    "UpdateLaunchProfileResponseTypeDef",
    "UpdateStreamingImageResponseTypeDef",
    "UpdateStudioComponentResponseTypeDef",
    "UpdateStudioResponseTypeDef",
)


class AcceptEulasResponseTypeDef(TypedDict, total=False):
    eulaAcceptances: List["EulaAcceptanceTypeDef"]


class ActiveDirectoryComputerAttributeTypeDef(TypedDict, total=False):
    name: str
    value: str


class ActiveDirectoryConfigurationTypeDef(TypedDict, total=False):
    computerAttributes: List["ActiveDirectoryComputerAttributeTypeDef"]
    directoryId: str
    organizationalUnitDistinguishedName: str


class ComputeFarmConfigurationTypeDef(TypedDict, total=False):
    activeDirectoryUser: str
    endpoint: str


class CreateLaunchProfileResponseTypeDef(TypedDict, total=False):
    launchProfile: "LaunchProfileTypeDef"


class CreateStreamingImageResponseTypeDef(TypedDict, total=False):
    streamingImage: "StreamingImageTypeDef"


class CreateStreamingSessionResponseTypeDef(TypedDict, total=False):
    session: "StreamingSessionTypeDef"


class CreateStreamingSessionStreamResponseTypeDef(TypedDict, total=False):
    stream: "StreamingSessionStreamTypeDef"


class CreateStudioComponentResponseTypeDef(TypedDict, total=False):
    studioComponent: "StudioComponentTypeDef"


class CreateStudioResponseTypeDef(TypedDict, total=False):
    studio: "StudioTypeDef"


class DeleteLaunchProfileResponseTypeDef(TypedDict, total=False):
    launchProfile: "LaunchProfileTypeDef"


class DeleteStreamingImageResponseTypeDef(TypedDict, total=False):
    streamingImage: "StreamingImageTypeDef"


class DeleteStreamingSessionResponseTypeDef(TypedDict, total=False):
    session: "StreamingSessionTypeDef"


class DeleteStudioComponentResponseTypeDef(TypedDict, total=False):
    studioComponent: "StudioComponentTypeDef"


class DeleteStudioResponseTypeDef(TypedDict, total=False):
    studio: "StudioTypeDef"


class EulaAcceptanceTypeDef(TypedDict, total=False):
    acceptedAt: datetime
    acceptedBy: str
    accepteeId: str
    eulaAcceptanceId: str
    eulaId: str


class EulaTypeDef(TypedDict, total=False):
    content: str
    createdAt: datetime
    eulaId: str
    name: str
    updatedAt: datetime


class GetEulaResponseTypeDef(TypedDict, total=False):
    eula: "EulaTypeDef"


class GetLaunchProfileDetailsResponseTypeDef(TypedDict, total=False):
    launchProfile: "LaunchProfileTypeDef"
    streamingImages: List["StreamingImageTypeDef"]
    studioComponentSummaries: List["StudioComponentSummaryTypeDef"]


class GetLaunchProfileInitializationResponseTypeDef(TypedDict, total=False):
    launchProfileInitialization: "LaunchProfileInitializationTypeDef"


class GetLaunchProfileMemberResponseTypeDef(TypedDict, total=False):
    member: "LaunchProfileMembershipTypeDef"


class GetLaunchProfileResponseTypeDef(TypedDict, total=False):
    launchProfile: "LaunchProfileTypeDef"


class GetStreamingImageResponseTypeDef(TypedDict, total=False):
    streamingImage: "StreamingImageTypeDef"


class GetStreamingSessionResponseTypeDef(TypedDict, total=False):
    session: "StreamingSessionTypeDef"


class GetStreamingSessionStreamResponseTypeDef(TypedDict, total=False):
    stream: "StreamingSessionStreamTypeDef"


class GetStudioComponentResponseTypeDef(TypedDict, total=False):
    studioComponent: "StudioComponentTypeDef"


class GetStudioMemberResponseTypeDef(TypedDict, total=False):
    member: "StudioMembershipTypeDef"


class GetStudioResponseTypeDef(TypedDict, total=False):
    studio: "StudioTypeDef"


class LaunchProfileInitializationActiveDirectoryTypeDef(TypedDict, total=False):
    computerAttributes: List["ActiveDirectoryComputerAttributeTypeDef"]
    directoryId: str
    directoryName: str
    dnsIpAddresses: List[str]
    organizationalUnitDistinguishedName: str
    studioComponentId: str
    studioComponentName: str


class LaunchProfileInitializationScriptTypeDef(TypedDict, total=False):
    script: str
    studioComponentId: str
    studioComponentName: str


class LaunchProfileInitializationTypeDef(TypedDict, total=False):
    activeDirectory: "LaunchProfileInitializationActiveDirectoryTypeDef"
    ec2SecurityGroupIds: List[str]
    launchProfileId: str
    launchProfileProtocolVersion: str
    launchPurpose: str
    name: str
    platform: LaunchProfilePlatform
    systemInitializationScripts: List["LaunchProfileInitializationScriptTypeDef"]
    userInitializationScripts: List["LaunchProfileInitializationScriptTypeDef"]


class LaunchProfileMembershipTypeDef(TypedDict, total=False):
    identityStoreId: str
    persona: Literal["USER"]
    principalId: str


class LaunchProfileTypeDef(TypedDict, total=False):
    arn: str
    createdAt: datetime
    createdBy: str
    description: str
    ec2SubnetIds: List[str]
    launchProfileId: str
    launchProfileProtocolVersions: List[str]
    name: str
    state: LaunchProfileState
    statusCode: LaunchProfileStatusCode
    statusMessage: str
    streamConfiguration: "StreamConfigurationTypeDef"
    studioComponentIds: List[str]
    tags: Dict[str, str]
    updatedAt: datetime
    updatedBy: str


class LicenseServiceConfigurationTypeDef(TypedDict, total=False):
    endpoint: str


class ListEulaAcceptancesResponseTypeDef(TypedDict, total=False):
    eulaAcceptances: List["EulaAcceptanceTypeDef"]
    nextToken: str


class ListEulasResponseTypeDef(TypedDict, total=False):
    eulas: List["EulaTypeDef"]
    nextToken: str


class ListLaunchProfileMembersResponseTypeDef(TypedDict, total=False):
    members: List["LaunchProfileMembershipTypeDef"]
    nextToken: str


class ListLaunchProfilesResponseTypeDef(TypedDict, total=False):
    launchProfiles: List["LaunchProfileTypeDef"]
    nextToken: str


class ListStreamingImagesResponseTypeDef(TypedDict, total=False):
    nextToken: str
    streamingImages: List["StreamingImageTypeDef"]


class ListStreamingSessionsResponseTypeDef(TypedDict, total=False):
    nextToken: str
    sessions: List["StreamingSessionTypeDef"]


class ListStudioComponentsResponseTypeDef(TypedDict, total=False):
    nextToken: str
    studioComponents: List["StudioComponentTypeDef"]


class ListStudioMembersResponseTypeDef(TypedDict, total=False):
    members: List["StudioMembershipTypeDef"]
    nextToken: str


class ListStudiosResponseTypeDef(TypedDict, total=False):
    nextToken: str
    studios: List["StudioTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class NewLaunchProfileMemberTypeDef(TypedDict):
    persona: Literal["USER"]
    principalId: str


class NewStudioMemberTypeDef(TypedDict):
    persona: Literal["ADMINISTRATOR"]
    principalId: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ScriptParameterKeyValueTypeDef(TypedDict, total=False):
    key: str
    value: str


class SharedFileSystemConfigurationTypeDef(TypedDict, total=False):
    endpoint: str
    fileSystemId: str
    linuxMountPoint: str
    shareName: str
    windowsMountDrive: str


class StartStudioSSOConfigurationRepairResponseTypeDef(TypedDict, total=False):
    studio: "StudioTypeDef"


class _RequiredStreamConfigurationCreateTypeDef(TypedDict):
    clipboardMode: StreamingClipboardMode
    ec2InstanceTypes: List[StreamingInstanceType]
    streamingImageIds: List[str]


class StreamConfigurationCreateTypeDef(_RequiredStreamConfigurationCreateTypeDef, total=False):
    maxSessionLengthInMinutes: int


class StreamConfigurationTypeDef(TypedDict, total=False):
    clipboardMode: StreamingClipboardMode
    ec2InstanceTypes: List[StreamingInstanceType]
    maxSessionLengthInMinutes: int
    streamingImageIds: List[str]


class _RequiredStreamingImageEncryptionConfigurationTypeDef(TypedDict):
    keyType: Literal["CUSTOMER_MANAGED_KEY"]


class StreamingImageEncryptionConfigurationTypeDef(
    _RequiredStreamingImageEncryptionConfigurationTypeDef, total=False
):
    keyArn: str


class StreamingImageTypeDef(TypedDict, total=False):
    arn: str
    description: str
    ec2ImageId: str
    encryptionConfiguration: "StreamingImageEncryptionConfigurationTypeDef"
    eulaIds: List[str]
    name: str
    owner: str
    platform: str
    state: StreamingImageState
    statusCode: StreamingImageStatusCode
    statusMessage: str
    streamingImageId: str
    tags: Dict[str, str]


class StreamingSessionStreamTypeDef(TypedDict, total=False):
    createdAt: datetime
    createdBy: str
    expiresAt: datetime
    state: StreamingSessionStreamState
    statusCode: StreamingSessionStreamStatusCode
    streamId: str
    url: str


class StreamingSessionTypeDef(TypedDict, total=False):
    arn: str
    createdAt: datetime
    createdBy: str
    ec2InstanceType: str
    launchProfileId: str
    sessionId: str
    state: StreamingSessionState
    statusCode: StreamingSessionStatusCode
    statusMessage: str
    streamingImageId: str
    tags: Dict[str, str]
    terminateAt: datetime
    updatedAt: datetime
    updatedBy: str


class StudioComponentConfigurationTypeDef(TypedDict, total=False):
    activeDirectoryConfiguration: "ActiveDirectoryConfigurationTypeDef"
    computeFarmConfiguration: "ComputeFarmConfigurationTypeDef"
    licenseServiceConfiguration: "LicenseServiceConfigurationTypeDef"
    sharedFileSystemConfiguration: "SharedFileSystemConfigurationTypeDef"


class StudioComponentInitializationScriptTypeDef(TypedDict, total=False):
    launchProfileProtocolVersion: str
    platform: LaunchProfilePlatform
    runContext: StudioComponentInitializationScriptRunContext
    script: str


StudioComponentSummaryTypeDef = TypedDict(
    "StudioComponentSummaryTypeDef",
    {
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "name": str,
        "studioComponentId": str,
        "subtype": StudioComponentSubtype,
        "type": StudioComponentType,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)

StudioComponentTypeDef = TypedDict(
    "StudioComponentTypeDef",
    {
        "arn": str,
        "configuration": "StudioComponentConfigurationTypeDef",
        "createdAt": datetime,
        "createdBy": str,
        "description": str,
        "ec2SecurityGroupIds": List[str],
        "initializationScripts": List["StudioComponentInitializationScriptTypeDef"],
        "name": str,
        "scriptParameters": List["ScriptParameterKeyValueTypeDef"],
        "state": StudioComponentState,
        "statusCode": StudioComponentStatusCode,
        "statusMessage": str,
        "studioComponentId": str,
        "subtype": StudioComponentSubtype,
        "tags": Dict[str, str],
        "type": StudioComponentType,
        "updatedAt": datetime,
        "updatedBy": str,
    },
    total=False,
)


class _RequiredStudioEncryptionConfigurationTypeDef(TypedDict):
    keyType: StudioEncryptionConfigurationKeyType


class StudioEncryptionConfigurationTypeDef(
    _RequiredStudioEncryptionConfigurationTypeDef, total=False
):
    keyArn: str


class StudioMembershipTypeDef(TypedDict, total=False):
    identityStoreId: str
    persona: Literal["ADMINISTRATOR"]
    principalId: str


class StudioTypeDef(TypedDict, total=False):
    adminRoleArn: str
    arn: str
    createdAt: datetime
    displayName: str
    homeRegion: str
    ssoClientId: str
    state: StudioState
    statusCode: StudioStatusCode
    statusMessage: str
    studioEncryptionConfiguration: "StudioEncryptionConfigurationTypeDef"
    studioId: str
    studioName: str
    studioUrl: str
    tags: Dict[str, str]
    updatedAt: datetime
    userRoleArn: str


class UpdateLaunchProfileMemberResponseTypeDef(TypedDict, total=False):
    member: "LaunchProfileMembershipTypeDef"


class UpdateLaunchProfileResponseTypeDef(TypedDict, total=False):
    launchProfile: "LaunchProfileTypeDef"


class UpdateStreamingImageResponseTypeDef(TypedDict, total=False):
    streamingImage: "StreamingImageTypeDef"


class UpdateStudioComponentResponseTypeDef(TypedDict, total=False):
    studioComponent: "StudioComponentTypeDef"


class UpdateStudioResponseTypeDef(TypedDict, total=False):
    studio: "StudioTypeDef"
