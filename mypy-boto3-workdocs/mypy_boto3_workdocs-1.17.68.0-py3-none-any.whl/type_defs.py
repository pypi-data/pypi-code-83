"""
Type annotations for workdocs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_workdocs.type_defs import ActivateUserResponseTypeDef

    data: ActivateUserResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_workdocs.literals import (
    ActivityType,
    CommentStatusType,
    CommentVisibilityType,
    DocumentSourceType,
    DocumentStatusType,
    DocumentThumbnailType,
    LocaleType,
    PrincipalType,
    ResourceStateType,
    ResourceType,
    RolePermissionType,
    RoleType,
    ShareStatusType,
    StorageType,
    UserStatusType,
    UserType,
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
    "ActivateUserResponseTypeDef",
    "ActivityTypeDef",
    "AddResourcePermissionsResponseTypeDef",
    "CommentMetadataTypeDef",
    "CommentTypeDef",
    "CreateCommentResponseTypeDef",
    "CreateFolderResponseTypeDef",
    "CreateNotificationSubscriptionResponseTypeDef",
    "CreateUserResponseTypeDef",
    "DescribeActivitiesResponseTypeDef",
    "DescribeCommentsResponseTypeDef",
    "DescribeDocumentVersionsResponseTypeDef",
    "DescribeFolderContentsResponseTypeDef",
    "DescribeGroupsResponseTypeDef",
    "DescribeNotificationSubscriptionsResponseTypeDef",
    "DescribeResourcePermissionsResponseTypeDef",
    "DescribeRootFoldersResponseTypeDef",
    "DescribeUsersResponseTypeDef",
    "DocumentMetadataTypeDef",
    "DocumentVersionMetadataTypeDef",
    "FolderMetadataTypeDef",
    "GetCurrentUserResponseTypeDef",
    "GetDocumentPathResponseTypeDef",
    "GetDocumentResponseTypeDef",
    "GetDocumentVersionResponseTypeDef",
    "GetFolderPathResponseTypeDef",
    "GetFolderResponseTypeDef",
    "GetResourcesResponseTypeDef",
    "GroupMetadataTypeDef",
    "InitiateDocumentVersionUploadResponseTypeDef",
    "NotificationOptionsTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantsTypeDef",
    "PermissionInfoTypeDef",
    "PrincipalTypeDef",
    "ResourceMetadataTypeDef",
    "ResourcePathComponentTypeDef",
    "ResourcePathTypeDef",
    "SharePrincipalTypeDef",
    "ShareResultTypeDef",
    "StorageRuleTypeTypeDef",
    "SubscriptionTypeDef",
    "UpdateUserResponseTypeDef",
    "UploadMetadataTypeDef",
    "UserMetadataTypeDef",
    "UserStorageMetadataTypeDef",
    "UserTypeDef",
)


class ActivateUserResponseTypeDef(TypedDict, total=False):
    User: "UserTypeDef"


ActivityTypeDef = TypedDict(
    "ActivityTypeDef",
    {
        "Type": ActivityType,
        "TimeStamp": datetime,
        "IsIndirectActivity": bool,
        "OrganizationId": str,
        "Initiator": "UserMetadataTypeDef",
        "Participants": "ParticipantsTypeDef",
        "ResourceMetadata": "ResourceMetadataTypeDef",
        "OriginalParent": "ResourceMetadataTypeDef",
        "CommentMetadata": "CommentMetadataTypeDef",
    },
    total=False,
)


class AddResourcePermissionsResponseTypeDef(TypedDict, total=False):
    ShareResults: List["ShareResultTypeDef"]


class CommentMetadataTypeDef(TypedDict, total=False):
    CommentId: str
    Contributor: "UserTypeDef"
    CreatedTimestamp: datetime
    CommentStatus: CommentStatusType
    RecipientId: str


_RequiredCommentTypeDef = TypedDict("_RequiredCommentTypeDef", {"CommentId": str})
_OptionalCommentTypeDef = TypedDict(
    "_OptionalCommentTypeDef",
    {
        "ParentId": str,
        "ThreadId": str,
        "Text": str,
        "Contributor": "UserTypeDef",
        "CreatedTimestamp": datetime,
        "Status": CommentStatusType,
        "Visibility": CommentVisibilityType,
        "RecipientId": str,
    },
    total=False,
)


class CommentTypeDef(_RequiredCommentTypeDef, _OptionalCommentTypeDef):
    pass


class CreateCommentResponseTypeDef(TypedDict, total=False):
    Comment: "CommentTypeDef"


class CreateFolderResponseTypeDef(TypedDict, total=False):
    Metadata: "FolderMetadataTypeDef"


class CreateNotificationSubscriptionResponseTypeDef(TypedDict, total=False):
    Subscription: "SubscriptionTypeDef"


class CreateUserResponseTypeDef(TypedDict, total=False):
    User: "UserTypeDef"


class DescribeActivitiesResponseTypeDef(TypedDict, total=False):
    UserActivities: List["ActivityTypeDef"]
    Marker: str


class DescribeCommentsResponseTypeDef(TypedDict, total=False):
    Comments: List["CommentTypeDef"]
    Marker: str


class DescribeDocumentVersionsResponseTypeDef(TypedDict, total=False):
    DocumentVersions: List["DocumentVersionMetadataTypeDef"]
    Marker: str


class DescribeFolderContentsResponseTypeDef(TypedDict, total=False):
    Folders: List["FolderMetadataTypeDef"]
    Documents: List["DocumentMetadataTypeDef"]
    Marker: str


class DescribeGroupsResponseTypeDef(TypedDict, total=False):
    Groups: List["GroupMetadataTypeDef"]
    Marker: str


class DescribeNotificationSubscriptionsResponseTypeDef(TypedDict, total=False):
    Subscriptions: List["SubscriptionTypeDef"]
    Marker: str


class DescribeResourcePermissionsResponseTypeDef(TypedDict, total=False):
    Principals: List["PrincipalTypeDef"]
    Marker: str


class DescribeRootFoldersResponseTypeDef(TypedDict, total=False):
    Folders: List["FolderMetadataTypeDef"]
    Marker: str


class DescribeUsersResponseTypeDef(TypedDict, total=False):
    Users: List["UserTypeDef"]
    TotalNumberOfUsers: int
    Marker: str


class DocumentMetadataTypeDef(TypedDict, total=False):
    Id: str
    CreatorId: str
    ParentFolderId: str
    CreatedTimestamp: datetime
    ModifiedTimestamp: datetime
    LatestVersionMetadata: "DocumentVersionMetadataTypeDef"
    ResourceState: ResourceStateType
    Labels: List[str]


class DocumentVersionMetadataTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    ContentType: str
    Size: int
    Signature: str
    Status: DocumentStatusType
    CreatedTimestamp: datetime
    ModifiedTimestamp: datetime
    ContentCreatedTimestamp: datetime
    ContentModifiedTimestamp: datetime
    CreatorId: str
    Thumbnail: Dict[DocumentThumbnailType, str]
    Source: Dict[DocumentSourceType, str]


class FolderMetadataTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    CreatorId: str
    ParentFolderId: str
    CreatedTimestamp: datetime
    ModifiedTimestamp: datetime
    ResourceState: ResourceStateType
    Signature: str
    Labels: List[str]
    Size: int
    LatestVersionSize: int


class GetCurrentUserResponseTypeDef(TypedDict, total=False):
    User: "UserTypeDef"


class GetDocumentPathResponseTypeDef(TypedDict, total=False):
    Path: "ResourcePathTypeDef"


class GetDocumentResponseTypeDef(TypedDict, total=False):
    Metadata: "DocumentMetadataTypeDef"
    CustomMetadata: Dict[str, str]


class GetDocumentVersionResponseTypeDef(TypedDict, total=False):
    Metadata: "DocumentVersionMetadataTypeDef"
    CustomMetadata: Dict[str, str]


class GetFolderPathResponseTypeDef(TypedDict, total=False):
    Path: "ResourcePathTypeDef"


class GetFolderResponseTypeDef(TypedDict, total=False):
    Metadata: "FolderMetadataTypeDef"
    CustomMetadata: Dict[str, str]


class GetResourcesResponseTypeDef(TypedDict, total=False):
    Folders: List["FolderMetadataTypeDef"]
    Documents: List["DocumentMetadataTypeDef"]
    Marker: str


class GroupMetadataTypeDef(TypedDict, total=False):
    Id: str
    Name: str


class InitiateDocumentVersionUploadResponseTypeDef(TypedDict, total=False):
    Metadata: "DocumentMetadataTypeDef"
    UploadMetadata: "UploadMetadataTypeDef"


class NotificationOptionsTypeDef(TypedDict, total=False):
    SendEmail: bool
    EmailMessage: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParticipantsTypeDef(TypedDict, total=False):
    Users: List["UserMetadataTypeDef"]
    Groups: List["GroupMetadataTypeDef"]


PermissionInfoTypeDef = TypedDict(
    "PermissionInfoTypeDef", {"Role": RoleType, "Type": RolePermissionType}, total=False
)

PrincipalTypeDef = TypedDict(
    "PrincipalTypeDef",
    {"Id": str, "Type": PrincipalType, "Roles": List["PermissionInfoTypeDef"]},
    total=False,
)

ResourceMetadataTypeDef = TypedDict(
    "ResourceMetadataTypeDef",
    {
        "Type": ResourceType,
        "Name": str,
        "OriginalName": str,
        "Id": str,
        "VersionId": str,
        "Owner": "UserMetadataTypeDef",
        "ParentId": str,
    },
    total=False,
)


class ResourcePathComponentTypeDef(TypedDict, total=False):
    Id: str
    Name: str


class ResourcePathTypeDef(TypedDict, total=False):
    Components: List["ResourcePathComponentTypeDef"]


SharePrincipalTypeDef = TypedDict(
    "SharePrincipalTypeDef", {"Id": str, "Type": PrincipalType, "Role": RoleType}
)


class ShareResultTypeDef(TypedDict, total=False):
    PrincipalId: str
    InviteePrincipalId: str
    Role: RoleType
    Status: ShareStatusType
    ShareId: str
    StatusMessage: str


class StorageRuleTypeTypeDef(TypedDict, total=False):
    StorageAllocatedInBytes: int
    StorageType: StorageType


SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {"SubscriptionId": str, "EndPoint": str, "Protocol": Literal["HTTPS"]},
    total=False,
)


class UpdateUserResponseTypeDef(TypedDict, total=False):
    User: "UserTypeDef"


class UploadMetadataTypeDef(TypedDict, total=False):
    UploadUrl: str
    SignedHeaders: Dict[str, str]


class UserMetadataTypeDef(TypedDict, total=False):
    Id: str
    Username: str
    GivenName: str
    Surname: str
    EmailAddress: str


class UserStorageMetadataTypeDef(TypedDict, total=False):
    StorageUtilizedInBytes: int
    StorageRule: "StorageRuleTypeTypeDef"


UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Id": str,
        "Username": str,
        "EmailAddress": str,
        "GivenName": str,
        "Surname": str,
        "OrganizationId": str,
        "RootFolderId": str,
        "RecycleBinFolderId": str,
        "Status": UserStatusType,
        "Type": UserType,
        "CreatedTimestamp": datetime,
        "ModifiedTimestamp": datetime,
        "TimeZoneId": str,
        "Locale": LocaleType,
        "Storage": "UserStorageMetadataTypeDef",
    },
    total=False,
)
