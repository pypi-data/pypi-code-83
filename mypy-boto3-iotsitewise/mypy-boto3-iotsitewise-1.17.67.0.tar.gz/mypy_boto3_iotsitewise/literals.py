"""
Type annotations for iotsitewise service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/literals.html)

Usage::

    ```python
    from mypy_boto3_iotsitewise.literals import AggregateType

    data: AggregateType = "AVERAGE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AggregateType",
    "AssetActiveWaiterName",
    "AssetErrorCode",
    "AssetModelActiveWaiterName",
    "AssetModelNotExistsWaiterName",
    "AssetModelState",
    "AssetNotExistsWaiterName",
    "AssetRelationshipType",
    "AssetState",
    "AuthMode",
    "BatchPutAssetPropertyValueErrorCode",
    "CapabilitySyncStatus",
    "ConfigurationState",
    "EncryptionType",
    "ErrorCode",
    "GetAssetPropertyAggregatesPaginatorName",
    "GetAssetPropertyValueHistoryPaginatorName",
    "GetInterpolatedAssetPropertyValuesPaginatorName",
    "IdentityType",
    "ImageFileType",
    "ListAccessPoliciesPaginatorName",
    "ListAssetModelsPaginatorName",
    "ListAssetRelationshipsPaginatorName",
    "ListAssetsFilter",
    "ListAssetsPaginatorName",
    "ListAssociatedAssetsPaginatorName",
    "ListDashboardsPaginatorName",
    "ListGatewaysPaginatorName",
    "ListPortalsPaginatorName",
    "ListProjectAssetsPaginatorName",
    "ListProjectsPaginatorName",
    "LoggingLevel",
    "MonitorErrorCode",
    "Permission",
    "PortalActiveWaiterName",
    "PortalNotExistsWaiterName",
    "PortalState",
    "PropertyDataType",
    "PropertyNotificationState",
    "Quality",
    "ResourceType",
    "TimeOrdering",
    "TraversalDirection",
    "TraversalType",
)


AggregateType = Literal["AVERAGE", "COUNT", "MAXIMUM", "MINIMUM", "STANDARD_DEVIATION", "SUM"]
AssetActiveWaiterName = Literal["asset_active"]
AssetErrorCode = Literal["INTERNAL_FAILURE"]
AssetModelActiveWaiterName = Literal["asset_model_active"]
AssetModelNotExistsWaiterName = Literal["asset_model_not_exists"]
AssetModelState = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "PROPAGATING", "UPDATING"]
AssetNotExistsWaiterName = Literal["asset_not_exists"]
AssetRelationshipType = Literal["HIERARCHY"]
AssetState = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
AuthMode = Literal["IAM", "SSO"]
BatchPutAssetPropertyValueErrorCode = Literal[
    "AccessDeniedException",
    "ConflictingOperationException",
    "InternalFailureException",
    "InvalidRequestException",
    "LimitExceededException",
    "ResourceNotFoundException",
    "ServiceUnavailableException",
    "ThrottlingException",
    "TimestampOutOfRangeException",
]
CapabilitySyncStatus = Literal["IN_SYNC", "OUT_OF_SYNC", "SYNC_FAILED"]
ConfigurationState = Literal["ACTIVE", "UPDATE_FAILED", "UPDATE_IN_PROGRESS"]
EncryptionType = Literal["KMS_BASED_ENCRYPTION", "SITEWISE_DEFAULT_ENCRYPTION"]
ErrorCode = Literal["INTERNAL_FAILURE", "VALIDATION_ERROR"]
GetAssetPropertyAggregatesPaginatorName = Literal["get_asset_property_aggregates"]
GetAssetPropertyValueHistoryPaginatorName = Literal["get_asset_property_value_history"]
GetInterpolatedAssetPropertyValuesPaginatorName = Literal["get_interpolated_asset_property_values"]
IdentityType = Literal["GROUP", "IAM", "USER"]
ImageFileType = Literal["PNG"]
ListAccessPoliciesPaginatorName = Literal["list_access_policies"]
ListAssetModelsPaginatorName = Literal["list_asset_models"]
ListAssetRelationshipsPaginatorName = Literal["list_asset_relationships"]
ListAssetsFilter = Literal["ALL", "TOP_LEVEL"]
ListAssetsPaginatorName = Literal["list_assets"]
ListAssociatedAssetsPaginatorName = Literal["list_associated_assets"]
ListDashboardsPaginatorName = Literal["list_dashboards"]
ListGatewaysPaginatorName = Literal["list_gateways"]
ListPortalsPaginatorName = Literal["list_portals"]
ListProjectAssetsPaginatorName = Literal["list_project_assets"]
ListProjectsPaginatorName = Literal["list_projects"]
LoggingLevel = Literal["ERROR", "INFO", "OFF"]
MonitorErrorCode = Literal["INTERNAL_FAILURE", "LIMIT_EXCEEDED", "VALIDATION_ERROR"]
Permission = Literal["ADMINISTRATOR", "VIEWER"]
PortalActiveWaiterName = Literal["portal_active"]
PortalNotExistsWaiterName = Literal["portal_not_exists"]
PortalState = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
PropertyDataType = Literal["BOOLEAN", "DOUBLE", "INTEGER", "STRING", "STRUCT"]
PropertyNotificationState = Literal["DISABLED", "ENABLED"]
Quality = Literal["BAD", "GOOD", "UNCERTAIN"]
ResourceType = Literal["PORTAL", "PROJECT"]
TimeOrdering = Literal["ASCENDING", "DESCENDING"]
TraversalDirection = Literal["CHILD", "PARENT"]
TraversalType = Literal["PATH_TO_ROOT"]
