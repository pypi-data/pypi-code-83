"""
Type annotations for workdocs service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_workdocs/literals.html)

Usage::

    ```python
    from mypy_boto3_workdocs.literals import ActivityType

    data: ActivityType = "DOCUMENT_ANNOTATION_ADDED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActivityType",
    "BooleanEnumType",
    "CommentStatusType",
    "CommentVisibilityType",
    "DescribeActivitiesPaginatorName",
    "DescribeCommentsPaginatorName",
    "DescribeDocumentVersionsPaginatorName",
    "DescribeFolderContentsPaginatorName",
    "DescribeGroupsPaginatorName",
    "DescribeNotificationSubscriptionsPaginatorName",
    "DescribeResourcePermissionsPaginatorName",
    "DescribeRootFoldersPaginatorName",
    "DescribeUsersPaginatorName",
    "DocumentSourceType",
    "DocumentStatusType",
    "DocumentThumbnailType",
    "DocumentVersionStatus",
    "FolderContentType",
    "LocaleType",
    "OrderType",
    "PrincipalType",
    "ResourceCollectionType",
    "ResourceSortType",
    "ResourceStateType",
    "ResourceType",
    "RolePermissionType",
    "RoleType",
    "ShareStatusType",
    "StorageType",
    "SubscriptionProtocolType",
    "SubscriptionType",
    "UserFilterType",
    "UserSortType",
    "UserStatusType",
    "UserType",
)


ActivityType = Literal[
    "DOCUMENT_ANNOTATION_ADDED",
    "DOCUMENT_ANNOTATION_DELETED",
    "DOCUMENT_CHECKED_IN",
    "DOCUMENT_CHECKED_OUT",
    "DOCUMENT_COMMENT_ADDED",
    "DOCUMENT_COMMENT_DELETED",
    "DOCUMENT_MOVED",
    "DOCUMENT_RECYCLED",
    "DOCUMENT_RENAMED",
    "DOCUMENT_RESTORED",
    "DOCUMENT_REVERTED",
    "DOCUMENT_SHAREABLE_LINK_CREATED",
    "DOCUMENT_SHAREABLE_LINK_PERMISSION_CHANGED",
    "DOCUMENT_SHAREABLE_LINK_REMOVED",
    "DOCUMENT_SHARED",
    "DOCUMENT_SHARE_PERMISSION_CHANGED",
    "DOCUMENT_UNSHARED",
    "DOCUMENT_VERSION_DELETED",
    "DOCUMENT_VERSION_DOWNLOADED",
    "DOCUMENT_VERSION_UPLOADED",
    "DOCUMENT_VERSION_VIEWED",
    "FOLDER_CREATED",
    "FOLDER_DELETED",
    "FOLDER_MOVED",
    "FOLDER_RECYCLED",
    "FOLDER_RENAMED",
    "FOLDER_RESTORED",
    "FOLDER_SHAREABLE_LINK_CREATED",
    "FOLDER_SHAREABLE_LINK_PERMISSION_CHANGED",
    "FOLDER_SHAREABLE_LINK_REMOVED",
    "FOLDER_SHARED",
    "FOLDER_SHARE_PERMISSION_CHANGED",
    "FOLDER_UNSHARED",
]
BooleanEnumType = Literal["FALSE", "TRUE"]
CommentStatusType = Literal["DELETED", "DRAFT", "PUBLISHED"]
CommentVisibilityType = Literal["PRIVATE", "PUBLIC"]
DescribeActivitiesPaginatorName = Literal["describe_activities"]
DescribeCommentsPaginatorName = Literal["describe_comments"]
DescribeDocumentVersionsPaginatorName = Literal["describe_document_versions"]
DescribeFolderContentsPaginatorName = Literal["describe_folder_contents"]
DescribeGroupsPaginatorName = Literal["describe_groups"]
DescribeNotificationSubscriptionsPaginatorName = Literal["describe_notification_subscriptions"]
DescribeResourcePermissionsPaginatorName = Literal["describe_resource_permissions"]
DescribeRootFoldersPaginatorName = Literal["describe_root_folders"]
DescribeUsersPaginatorName = Literal["describe_users"]
DocumentSourceType = Literal["ORIGINAL", "WITH_COMMENTS"]
DocumentStatusType = Literal["ACTIVE", "INITIALIZED"]
DocumentThumbnailType = Literal["LARGE", "SMALL", "SMALL_HQ"]
DocumentVersionStatus = Literal["ACTIVE"]
FolderContentType = Literal["ALL", "DOCUMENT", "FOLDER"]
LocaleType = Literal["de", "default", "en", "es", "fr", "ja", "ko", "pt_BR", "ru", "zh_CN", "zh_TW"]
OrderType = Literal["ASCENDING", "DESCENDING"]
PrincipalType = Literal["ANONYMOUS", "GROUP", "INVITE", "ORGANIZATION", "USER"]
ResourceCollectionType = Literal["SHARED_WITH_ME"]
ResourceSortType = Literal["DATE", "NAME"]
ResourceStateType = Literal["ACTIVE", "RECYCLED", "RECYCLING", "RESTORING"]
ResourceType = Literal["DOCUMENT", "FOLDER"]
RolePermissionType = Literal["DIRECT", "INHERITED"]
RoleType = Literal["CONTRIBUTOR", "COOWNER", "OWNER", "VIEWER"]
ShareStatusType = Literal["FAILURE", "SUCCESS"]
StorageType = Literal["QUOTA", "UNLIMITED"]
SubscriptionProtocolType = Literal["HTTPS"]
SubscriptionType = Literal["ALL"]
UserFilterType = Literal["ACTIVE_PENDING", "ALL"]
UserSortType = Literal["FULL_NAME", "STORAGE_LIMIT", "STORAGE_USED", "USER_NAME", "USER_STATUS"]
UserStatusType = Literal["ACTIVE", "INACTIVE", "PENDING"]
UserType = Literal["ADMIN", "MINIMALUSER", "POWERUSER", "USER", "WORKSPACESUSER"]
