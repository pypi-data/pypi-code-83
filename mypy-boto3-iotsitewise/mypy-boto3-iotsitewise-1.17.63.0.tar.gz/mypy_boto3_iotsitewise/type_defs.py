"""
Type annotations for iotsitewise service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotsitewise/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotsitewise.type_defs import AccessPolicySummaryTypeDef

    data: AccessPolicySummaryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_iotsitewise.literals import (
    AssetModelState,
    AssetState,
    AuthMode,
    BatchPutAssetPropertyValueErrorCode,
    CapabilitySyncStatus,
    ConfigurationState,
    EncryptionType,
    ErrorCode,
    LoggingLevel,
    MonitorErrorCode,
    Permission,
    PortalState,
    PropertyDataType,
    PropertyNotificationState,
    Quality,
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
    "AccessPolicySummaryTypeDef",
    "AggregatedValueTypeDef",
    "AggregatesTypeDef",
    "AssetCompositeModelTypeDef",
    "AssetErrorDetailsTypeDef",
    "AssetHierarchyInfoTypeDef",
    "AssetHierarchyTypeDef",
    "AssetModelCompositeModelDefinitionTypeDef",
    "AssetModelCompositeModelTypeDef",
    "AssetModelHierarchyDefinitionTypeDef",
    "AssetModelHierarchyTypeDef",
    "AssetModelPropertyDefinitionTypeDef",
    "AssetModelPropertyTypeDef",
    "AssetModelStatusTypeDef",
    "AssetModelSummaryTypeDef",
    "AssetPropertyTypeDef",
    "AssetPropertyValueTypeDef",
    "AssetRelationshipSummaryTypeDef",
    "AssetStatusTypeDef",
    "AssetSummaryTypeDef",
    "AssociatedAssetsSummaryTypeDef",
    "AttributeTypeDef",
    "BatchAssociateProjectAssetsResponseTypeDef",
    "BatchDisassociateProjectAssetsResponseTypeDef",
    "BatchPutAssetPropertyErrorEntryTypeDef",
    "BatchPutAssetPropertyErrorTypeDef",
    "BatchPutAssetPropertyValueResponseTypeDef",
    "CompositeModelPropertyTypeDef",
    "ConfigurationErrorDetailsTypeDef",
    "ConfigurationStatusTypeDef",
    "CreateAccessPolicyResponseTypeDef",
    "CreateAssetModelResponseTypeDef",
    "CreateAssetResponseTypeDef",
    "CreateDashboardResponseTypeDef",
    "CreateGatewayResponseTypeDef",
    "CreatePortalResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "DashboardSummaryTypeDef",
    "DeleteAssetModelResponseTypeDef",
    "DeleteAssetResponseTypeDef",
    "DeletePortalResponseTypeDef",
    "DescribeAccessPolicyResponseTypeDef",
    "DescribeAssetModelResponseTypeDef",
    "DescribeAssetPropertyResponseTypeDef",
    "DescribeAssetResponseTypeDef",
    "DescribeDashboardResponseTypeDef",
    "DescribeDefaultEncryptionConfigurationResponseTypeDef",
    "DescribeGatewayCapabilityConfigurationResponseTypeDef",
    "DescribeGatewayResponseTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "DescribePortalResponseTypeDef",
    "DescribeProjectResponseTypeDef",
    "ErrorDetailsTypeDef",
    "ExpressionVariableTypeDef",
    "GatewayCapabilitySummaryTypeDef",
    "GatewayPlatformTypeDef",
    "GatewaySummaryTypeDef",
    "GetAssetPropertyAggregatesResponseTypeDef",
    "GetAssetPropertyValueHistoryResponseTypeDef",
    "GetAssetPropertyValueResponseTypeDef",
    "GetInterpolatedAssetPropertyValuesResponseTypeDef",
    "GreengrassTypeDef",
    "GroupIdentityTypeDef",
    "IAMRoleIdentityTypeDef",
    "IAMUserIdentityTypeDef",
    "IdentityTypeDef",
    "ImageFileTypeDef",
    "ImageLocationTypeDef",
    "ImageTypeDef",
    "InterpolatedAssetPropertyValueTypeDef",
    "ListAccessPoliciesResponseTypeDef",
    "ListAssetModelsResponseTypeDef",
    "ListAssetRelationshipsResponseTypeDef",
    "ListAssetsResponseTypeDef",
    "ListAssociatedAssetsResponseTypeDef",
    "ListDashboardsResponseTypeDef",
    "ListGatewaysResponseTypeDef",
    "ListPortalsResponseTypeDef",
    "ListProjectAssetsResponseTypeDef",
    "ListProjectsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingOptionsTypeDef",
    "MetricTypeDef",
    "MetricWindowTypeDef",
    "MonitorErrorDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "PortalResourceTypeDef",
    "PortalStatusTypeDef",
    "PortalSummaryTypeDef",
    "ProjectResourceTypeDef",
    "ProjectSummaryTypeDef",
    "PropertyNotificationTypeDef",
    "PropertyTypeDef",
    "PropertyTypeTypeDef",
    "PutAssetPropertyValueEntryTypeDef",
    "PutDefaultEncryptionConfigurationResponseTypeDef",
    "ResourceTypeDef",
    "TimeInNanosTypeDef",
    "TransformTypeDef",
    "TumblingWindowTypeDef",
    "UpdateAssetModelResponseTypeDef",
    "UpdateAssetResponseTypeDef",
    "UpdateGatewayCapabilityConfigurationResponseTypeDef",
    "UpdatePortalResponseTypeDef",
    "UserIdentityTypeDef",
    "VariableValueTypeDef",
    "VariantTypeDef",
    "WaiterConfigTypeDef",
)

_RequiredAccessPolicySummaryTypeDef = TypedDict(
    "_RequiredAccessPolicySummaryTypeDef",
    {
        "id": str,
        "identity": "IdentityTypeDef",
        "resource": "ResourceTypeDef",
        "permission": Permission,
    },
)
_OptionalAccessPolicySummaryTypeDef = TypedDict(
    "_OptionalAccessPolicySummaryTypeDef",
    {"creationDate": datetime, "lastUpdateDate": datetime},
    total=False,
)


class AccessPolicySummaryTypeDef(
    _RequiredAccessPolicySummaryTypeDef, _OptionalAccessPolicySummaryTypeDef
):
    pass


class _RequiredAggregatedValueTypeDef(TypedDict):
    timestamp: datetime
    value: "AggregatesTypeDef"


class AggregatedValueTypeDef(_RequiredAggregatedValueTypeDef, total=False):
    quality: Quality


AggregatesTypeDef = TypedDict(
    "AggregatesTypeDef",
    {
        "average": float,
        "count": float,
        "maximum": float,
        "minimum": float,
        "sum": float,
        "standardDeviation": float,
    },
    total=False,
)

_RequiredAssetCompositeModelTypeDef = TypedDict(
    "_RequiredAssetCompositeModelTypeDef",
    {"name": str, "type": str, "properties": List["AssetPropertyTypeDef"]},
)
_OptionalAssetCompositeModelTypeDef = TypedDict(
    "_OptionalAssetCompositeModelTypeDef", {"description": str}, total=False
)


class AssetCompositeModelTypeDef(
    _RequiredAssetCompositeModelTypeDef, _OptionalAssetCompositeModelTypeDef
):
    pass


class AssetErrorDetailsTypeDef(TypedDict):
    assetId: str
    code: Literal["INTERNAL_FAILURE"]
    message: str


class AssetHierarchyInfoTypeDef(TypedDict, total=False):
    parentAssetId: str
    childAssetId: str


_RequiredAssetHierarchyTypeDef = TypedDict("_RequiredAssetHierarchyTypeDef", {"name": str})
_OptionalAssetHierarchyTypeDef = TypedDict(
    "_OptionalAssetHierarchyTypeDef", {"id": str}, total=False
)


class AssetHierarchyTypeDef(_RequiredAssetHierarchyTypeDef, _OptionalAssetHierarchyTypeDef):
    pass


_RequiredAssetModelCompositeModelDefinitionTypeDef = TypedDict(
    "_RequiredAssetModelCompositeModelDefinitionTypeDef", {"name": str, "type": str}
)
_OptionalAssetModelCompositeModelDefinitionTypeDef = TypedDict(
    "_OptionalAssetModelCompositeModelDefinitionTypeDef",
    {"description": str, "properties": List["AssetModelPropertyDefinitionTypeDef"]},
    total=False,
)


class AssetModelCompositeModelDefinitionTypeDef(
    _RequiredAssetModelCompositeModelDefinitionTypeDef,
    _OptionalAssetModelCompositeModelDefinitionTypeDef,
):
    pass


_RequiredAssetModelCompositeModelTypeDef = TypedDict(
    "_RequiredAssetModelCompositeModelTypeDef", {"name": str, "type": str}
)
_OptionalAssetModelCompositeModelTypeDef = TypedDict(
    "_OptionalAssetModelCompositeModelTypeDef",
    {"description": str, "properties": List["AssetModelPropertyTypeDef"]},
    total=False,
)


class AssetModelCompositeModelTypeDef(
    _RequiredAssetModelCompositeModelTypeDef, _OptionalAssetModelCompositeModelTypeDef
):
    pass


class AssetModelHierarchyDefinitionTypeDef(TypedDict):
    name: str
    childAssetModelId: str


_RequiredAssetModelHierarchyTypeDef = TypedDict(
    "_RequiredAssetModelHierarchyTypeDef", {"name": str, "childAssetModelId": str}
)
_OptionalAssetModelHierarchyTypeDef = TypedDict(
    "_OptionalAssetModelHierarchyTypeDef", {"id": str}, total=False
)


class AssetModelHierarchyTypeDef(
    _RequiredAssetModelHierarchyTypeDef, _OptionalAssetModelHierarchyTypeDef
):
    pass


_RequiredAssetModelPropertyDefinitionTypeDef = TypedDict(
    "_RequiredAssetModelPropertyDefinitionTypeDef",
    {"name": str, "dataType": PropertyDataType, "type": "PropertyTypeTypeDef"},
)
_OptionalAssetModelPropertyDefinitionTypeDef = TypedDict(
    "_OptionalAssetModelPropertyDefinitionTypeDef", {"dataTypeSpec": str, "unit": str}, total=False
)


class AssetModelPropertyDefinitionTypeDef(
    _RequiredAssetModelPropertyDefinitionTypeDef, _OptionalAssetModelPropertyDefinitionTypeDef
):
    pass


_RequiredAssetModelPropertyTypeDef = TypedDict(
    "_RequiredAssetModelPropertyTypeDef",
    {"name": str, "dataType": PropertyDataType, "type": "PropertyTypeTypeDef"},
)
_OptionalAssetModelPropertyTypeDef = TypedDict(
    "_OptionalAssetModelPropertyTypeDef", {"id": str, "dataTypeSpec": str, "unit": str}, total=False
)


class AssetModelPropertyTypeDef(
    _RequiredAssetModelPropertyTypeDef, _OptionalAssetModelPropertyTypeDef
):
    pass


class _RequiredAssetModelStatusTypeDef(TypedDict):
    state: AssetModelState


class AssetModelStatusTypeDef(_RequiredAssetModelStatusTypeDef, total=False):
    error: "ErrorDetailsTypeDef"


AssetModelSummaryTypeDef = TypedDict(
    "AssetModelSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "description": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": "AssetModelStatusTypeDef",
    },
)

_RequiredAssetPropertyTypeDef = TypedDict(
    "_RequiredAssetPropertyTypeDef", {"id": str, "name": str, "dataType": PropertyDataType}
)
_OptionalAssetPropertyTypeDef = TypedDict(
    "_OptionalAssetPropertyTypeDef",
    {"alias": str, "notification": "PropertyNotificationTypeDef", "dataTypeSpec": str, "unit": str},
    total=False,
)


class AssetPropertyTypeDef(_RequiredAssetPropertyTypeDef, _OptionalAssetPropertyTypeDef):
    pass


class _RequiredAssetPropertyValueTypeDef(TypedDict):
    value: "VariantTypeDef"
    timestamp: "TimeInNanosTypeDef"


class AssetPropertyValueTypeDef(_RequiredAssetPropertyValueTypeDef, total=False):
    quality: Quality


class _RequiredAssetRelationshipSummaryTypeDef(TypedDict):
    relationshipType: Literal["HIERARCHY"]


class AssetRelationshipSummaryTypeDef(_RequiredAssetRelationshipSummaryTypeDef, total=False):
    hierarchyInfo: "AssetHierarchyInfoTypeDef"


class _RequiredAssetStatusTypeDef(TypedDict):
    state: AssetState


class AssetStatusTypeDef(_RequiredAssetStatusTypeDef, total=False):
    error: "ErrorDetailsTypeDef"


AssetSummaryTypeDef = TypedDict(
    "AssetSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "assetModelId": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": "AssetStatusTypeDef",
        "hierarchies": List["AssetHierarchyTypeDef"],
    },
)

AssociatedAssetsSummaryTypeDef = TypedDict(
    "AssociatedAssetsSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "name": str,
        "assetModelId": str,
        "creationDate": datetime,
        "lastUpdateDate": datetime,
        "status": "AssetStatusTypeDef",
        "hierarchies": List["AssetHierarchyTypeDef"],
    },
)


class AttributeTypeDef(TypedDict, total=False):
    defaultValue: str


class BatchAssociateProjectAssetsResponseTypeDef(TypedDict, total=False):
    errors: List["AssetErrorDetailsTypeDef"]


class BatchDisassociateProjectAssetsResponseTypeDef(TypedDict, total=False):
    errors: List["AssetErrorDetailsTypeDef"]


class BatchPutAssetPropertyErrorEntryTypeDef(TypedDict):
    entryId: str
    errors: List["BatchPutAssetPropertyErrorTypeDef"]


class BatchPutAssetPropertyErrorTypeDef(TypedDict):
    errorCode: BatchPutAssetPropertyValueErrorCode
    errorMessage: str
    timestamps: List["TimeInNanosTypeDef"]


class BatchPutAssetPropertyValueResponseTypeDef(TypedDict):
    errorEntries: List["BatchPutAssetPropertyErrorEntryTypeDef"]


CompositeModelPropertyTypeDef = TypedDict(
    "CompositeModelPropertyTypeDef", {"name": str, "type": str, "assetProperty": "PropertyTypeDef"}
)


class ConfigurationErrorDetailsTypeDef(TypedDict):
    code: ErrorCode
    message: str


class _RequiredConfigurationStatusTypeDef(TypedDict):
    state: ConfigurationState


class ConfigurationStatusTypeDef(_RequiredConfigurationStatusTypeDef, total=False):
    error: "ConfigurationErrorDetailsTypeDef"


class CreateAccessPolicyResponseTypeDef(TypedDict):
    accessPolicyId: str
    accessPolicyArn: str


class CreateAssetModelResponseTypeDef(TypedDict):
    assetModelId: str
    assetModelArn: str
    assetModelStatus: "AssetModelStatusTypeDef"


class CreateAssetResponseTypeDef(TypedDict):
    assetId: str
    assetArn: str
    assetStatus: "AssetStatusTypeDef"


class CreateDashboardResponseTypeDef(TypedDict):
    dashboardId: str
    dashboardArn: str


class CreateGatewayResponseTypeDef(TypedDict):
    gatewayId: str
    gatewayArn: str


class CreatePortalResponseTypeDef(TypedDict):
    portalId: str
    portalArn: str
    portalStartUrl: str
    portalStatus: "PortalStatusTypeDef"
    ssoApplicationId: str


class CreateProjectResponseTypeDef(TypedDict):
    projectId: str
    projectArn: str


_RequiredDashboardSummaryTypeDef = TypedDict(
    "_RequiredDashboardSummaryTypeDef", {"id": str, "name": str}
)
_OptionalDashboardSummaryTypeDef = TypedDict(
    "_OptionalDashboardSummaryTypeDef",
    {"description": str, "creationDate": datetime, "lastUpdateDate": datetime},
    total=False,
)


class DashboardSummaryTypeDef(_RequiredDashboardSummaryTypeDef, _OptionalDashboardSummaryTypeDef):
    pass


class DeleteAssetModelResponseTypeDef(TypedDict):
    assetModelStatus: "AssetModelStatusTypeDef"


class DeleteAssetResponseTypeDef(TypedDict):
    assetStatus: "AssetStatusTypeDef"


class DeletePortalResponseTypeDef(TypedDict):
    portalStatus: "PortalStatusTypeDef"


class DescribeAccessPolicyResponseTypeDef(TypedDict):
    accessPolicyId: str
    accessPolicyArn: str
    accessPolicyIdentity: "IdentityTypeDef"
    accessPolicyResource: "ResourceTypeDef"
    accessPolicyPermission: Permission
    accessPolicyCreationDate: datetime
    accessPolicyLastUpdateDate: datetime


class _RequiredDescribeAssetModelResponseTypeDef(TypedDict):
    assetModelId: str
    assetModelArn: str
    assetModelName: str
    assetModelDescription: str
    assetModelProperties: List["AssetModelPropertyTypeDef"]
    assetModelHierarchies: List["AssetModelHierarchyTypeDef"]
    assetModelCreationDate: datetime
    assetModelLastUpdateDate: datetime
    assetModelStatus: "AssetModelStatusTypeDef"


class DescribeAssetModelResponseTypeDef(_RequiredDescribeAssetModelResponseTypeDef, total=False):
    assetModelCompositeModels: List["AssetModelCompositeModelTypeDef"]


class _RequiredDescribeAssetPropertyResponseTypeDef(TypedDict):
    assetId: str
    assetName: str
    assetModelId: str


class DescribeAssetPropertyResponseTypeDef(
    _RequiredDescribeAssetPropertyResponseTypeDef, total=False
):
    assetProperty: "PropertyTypeDef"
    compositeModel: "CompositeModelPropertyTypeDef"


class _RequiredDescribeAssetResponseTypeDef(TypedDict):
    assetId: str
    assetArn: str
    assetName: str
    assetModelId: str
    assetProperties: List["AssetPropertyTypeDef"]
    assetHierarchies: List["AssetHierarchyTypeDef"]
    assetCreationDate: datetime
    assetLastUpdateDate: datetime
    assetStatus: "AssetStatusTypeDef"


class DescribeAssetResponseTypeDef(_RequiredDescribeAssetResponseTypeDef, total=False):
    assetCompositeModels: List["AssetCompositeModelTypeDef"]


class _RequiredDescribeDashboardResponseTypeDef(TypedDict):
    dashboardId: str
    dashboardArn: str
    dashboardName: str
    projectId: str
    dashboardDefinition: str
    dashboardCreationDate: datetime
    dashboardLastUpdateDate: datetime


class DescribeDashboardResponseTypeDef(_RequiredDescribeDashboardResponseTypeDef, total=False):
    dashboardDescription: str


class _RequiredDescribeDefaultEncryptionConfigurationResponseTypeDef(TypedDict):
    encryptionType: EncryptionType
    configurationStatus: "ConfigurationStatusTypeDef"


class DescribeDefaultEncryptionConfigurationResponseTypeDef(
    _RequiredDescribeDefaultEncryptionConfigurationResponseTypeDef, total=False
):
    kmsKeyArn: str


class DescribeGatewayCapabilityConfigurationResponseTypeDef(TypedDict):
    gatewayId: str
    capabilityNamespace: str
    capabilityConfiguration: str
    capabilitySyncStatus: CapabilitySyncStatus


class _RequiredDescribeGatewayResponseTypeDef(TypedDict):
    gatewayId: str
    gatewayName: str
    gatewayArn: str
    gatewayCapabilitySummaries: List["GatewayCapabilitySummaryTypeDef"]
    creationDate: datetime
    lastUpdateDate: datetime


class DescribeGatewayResponseTypeDef(_RequiredDescribeGatewayResponseTypeDef, total=False):
    gatewayPlatform: "GatewayPlatformTypeDef"


class DescribeLoggingOptionsResponseTypeDef(TypedDict):
    loggingOptions: "LoggingOptionsTypeDef"


class _RequiredDescribePortalResponseTypeDef(TypedDict):
    portalId: str
    portalArn: str
    portalName: str
    portalClientId: str
    portalStartUrl: str
    portalContactEmail: str
    portalStatus: "PortalStatusTypeDef"
    portalCreationDate: datetime
    portalLastUpdateDate: datetime


class DescribePortalResponseTypeDef(_RequiredDescribePortalResponseTypeDef, total=False):
    portalDescription: str
    portalLogoImageLocation: "ImageLocationTypeDef"
    roleArn: str
    portalAuthMode: AuthMode


class _RequiredDescribeProjectResponseTypeDef(TypedDict):
    projectId: str
    projectArn: str
    projectName: str
    portalId: str
    projectCreationDate: datetime
    projectLastUpdateDate: datetime


class DescribeProjectResponseTypeDef(_RequiredDescribeProjectResponseTypeDef, total=False):
    projectDescription: str


class ErrorDetailsTypeDef(TypedDict):
    code: ErrorCode
    message: str


class ExpressionVariableTypeDef(TypedDict):
    name: str
    value: "VariableValueTypeDef"


class GatewayCapabilitySummaryTypeDef(TypedDict):
    capabilityNamespace: str
    capabilitySyncStatus: CapabilitySyncStatus


class GatewayPlatformTypeDef(TypedDict):
    greengrass: "GreengrassTypeDef"


class _RequiredGatewaySummaryTypeDef(TypedDict):
    gatewayId: str
    gatewayName: str
    creationDate: datetime
    lastUpdateDate: datetime


class GatewaySummaryTypeDef(_RequiredGatewaySummaryTypeDef, total=False):
    gatewayCapabilitySummaries: List["GatewayCapabilitySummaryTypeDef"]


class _RequiredGetAssetPropertyAggregatesResponseTypeDef(TypedDict):
    aggregatedValues: List["AggregatedValueTypeDef"]


class GetAssetPropertyAggregatesResponseTypeDef(
    _RequiredGetAssetPropertyAggregatesResponseTypeDef, total=False
):
    nextToken: str


class _RequiredGetAssetPropertyValueHistoryResponseTypeDef(TypedDict):
    assetPropertyValueHistory: List["AssetPropertyValueTypeDef"]


class GetAssetPropertyValueHistoryResponseTypeDef(
    _RequiredGetAssetPropertyValueHistoryResponseTypeDef, total=False
):
    nextToken: str


class GetAssetPropertyValueResponseTypeDef(TypedDict, total=False):
    propertyValue: "AssetPropertyValueTypeDef"


class _RequiredGetInterpolatedAssetPropertyValuesResponseTypeDef(TypedDict):
    interpolatedAssetPropertyValues: List["InterpolatedAssetPropertyValueTypeDef"]


class GetInterpolatedAssetPropertyValuesResponseTypeDef(
    _RequiredGetInterpolatedAssetPropertyValuesResponseTypeDef, total=False
):
    nextToken: str


class GreengrassTypeDef(TypedDict):
    groupArn: str


GroupIdentityTypeDef = TypedDict("GroupIdentityTypeDef", {"id": str})


class IAMRoleIdentityTypeDef(TypedDict):
    arn: str


class IAMUserIdentityTypeDef(TypedDict):
    arn: str


class IdentityTypeDef(TypedDict, total=False):
    user: "UserIdentityTypeDef"
    group: "GroupIdentityTypeDef"
    iamUser: "IAMUserIdentityTypeDef"
    iamRole: "IAMRoleIdentityTypeDef"


ImageFileTypeDef = TypedDict(
    "ImageFileTypeDef", {"data": Union[bytes, IO[bytes]], "type": Literal["PNG"]}
)

ImageLocationTypeDef = TypedDict("ImageLocationTypeDef", {"id": str, "url": str})

ImageTypeDef = TypedDict("ImageTypeDef", {"id": str, "file": "ImageFileTypeDef"}, total=False)


class InterpolatedAssetPropertyValueTypeDef(TypedDict):
    timestamp: "TimeInNanosTypeDef"
    value: "VariantTypeDef"


class _RequiredListAccessPoliciesResponseTypeDef(TypedDict):
    accessPolicySummaries: List["AccessPolicySummaryTypeDef"]


class ListAccessPoliciesResponseTypeDef(_RequiredListAccessPoliciesResponseTypeDef, total=False):
    nextToken: str


class _RequiredListAssetModelsResponseTypeDef(TypedDict):
    assetModelSummaries: List["AssetModelSummaryTypeDef"]


class ListAssetModelsResponseTypeDef(_RequiredListAssetModelsResponseTypeDef, total=False):
    nextToken: str


class _RequiredListAssetRelationshipsResponseTypeDef(TypedDict):
    assetRelationshipSummaries: List["AssetRelationshipSummaryTypeDef"]


class ListAssetRelationshipsResponseTypeDef(
    _RequiredListAssetRelationshipsResponseTypeDef, total=False
):
    nextToken: str


class _RequiredListAssetsResponseTypeDef(TypedDict):
    assetSummaries: List["AssetSummaryTypeDef"]


class ListAssetsResponseTypeDef(_RequiredListAssetsResponseTypeDef, total=False):
    nextToken: str


class _RequiredListAssociatedAssetsResponseTypeDef(TypedDict):
    assetSummaries: List["AssociatedAssetsSummaryTypeDef"]


class ListAssociatedAssetsResponseTypeDef(
    _RequiredListAssociatedAssetsResponseTypeDef, total=False
):
    nextToken: str


class _RequiredListDashboardsResponseTypeDef(TypedDict):
    dashboardSummaries: List["DashboardSummaryTypeDef"]


class ListDashboardsResponseTypeDef(_RequiredListDashboardsResponseTypeDef, total=False):
    nextToken: str


class _RequiredListGatewaysResponseTypeDef(TypedDict):
    gatewaySummaries: List["GatewaySummaryTypeDef"]


class ListGatewaysResponseTypeDef(_RequiredListGatewaysResponseTypeDef, total=False):
    nextToken: str


class ListPortalsResponseTypeDef(TypedDict, total=False):
    portalSummaries: List["PortalSummaryTypeDef"]
    nextToken: str


class _RequiredListProjectAssetsResponseTypeDef(TypedDict):
    assetIds: List[str]


class ListProjectAssetsResponseTypeDef(_RequiredListProjectAssetsResponseTypeDef, total=False):
    nextToken: str


class _RequiredListProjectsResponseTypeDef(TypedDict):
    projectSummaries: List["ProjectSummaryTypeDef"]


class ListProjectsResponseTypeDef(_RequiredListProjectsResponseTypeDef, total=False):
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class LoggingOptionsTypeDef(TypedDict):
    level: LoggingLevel


class MetricTypeDef(TypedDict):
    expression: str
    variables: List["ExpressionVariableTypeDef"]
    window: "MetricWindowTypeDef"


class MetricWindowTypeDef(TypedDict, total=False):
    tumbling: "TumblingWindowTypeDef"


class MonitorErrorDetailsTypeDef(TypedDict, total=False):
    code: MonitorErrorCode
    message: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


PortalResourceTypeDef = TypedDict("PortalResourceTypeDef", {"id": str})


class _RequiredPortalStatusTypeDef(TypedDict):
    state: PortalState


class PortalStatusTypeDef(_RequiredPortalStatusTypeDef, total=False):
    error: "MonitorErrorDetailsTypeDef"


_RequiredPortalSummaryTypeDef = TypedDict(
    "_RequiredPortalSummaryTypeDef",
    {"id": str, "name": str, "startUrl": str, "status": "PortalStatusTypeDef"},
)
_OptionalPortalSummaryTypeDef = TypedDict(
    "_OptionalPortalSummaryTypeDef",
    {"description": str, "creationDate": datetime, "lastUpdateDate": datetime, "roleArn": str},
    total=False,
)


class PortalSummaryTypeDef(_RequiredPortalSummaryTypeDef, _OptionalPortalSummaryTypeDef):
    pass


ProjectResourceTypeDef = TypedDict("ProjectResourceTypeDef", {"id": str})

_RequiredProjectSummaryTypeDef = TypedDict(
    "_RequiredProjectSummaryTypeDef", {"id": str, "name": str}
)
_OptionalProjectSummaryTypeDef = TypedDict(
    "_OptionalProjectSummaryTypeDef",
    {"description": str, "creationDate": datetime, "lastUpdateDate": datetime},
    total=False,
)


class ProjectSummaryTypeDef(_RequiredProjectSummaryTypeDef, _OptionalProjectSummaryTypeDef):
    pass


class PropertyNotificationTypeDef(TypedDict):
    topic: str
    state: PropertyNotificationState


_RequiredPropertyTypeDef = TypedDict(
    "_RequiredPropertyTypeDef", {"id": str, "name": str, "dataType": PropertyDataType}
)
_OptionalPropertyTypeDef = TypedDict(
    "_OptionalPropertyTypeDef",
    {
        "alias": str,
        "notification": "PropertyNotificationTypeDef",
        "unit": str,
        "type": "PropertyTypeTypeDef",
    },
    total=False,
)


class PropertyTypeDef(_RequiredPropertyTypeDef, _OptionalPropertyTypeDef):
    pass


class PropertyTypeTypeDef(TypedDict, total=False):
    attribute: "AttributeTypeDef"
    measurement: Dict[str, Any]
    transform: "TransformTypeDef"
    metric: "MetricTypeDef"


class _RequiredPutAssetPropertyValueEntryTypeDef(TypedDict):
    entryId: str
    propertyValues: List["AssetPropertyValueTypeDef"]


class PutAssetPropertyValueEntryTypeDef(_RequiredPutAssetPropertyValueEntryTypeDef, total=False):
    assetId: str
    propertyId: str
    propertyAlias: str


class _RequiredPutDefaultEncryptionConfigurationResponseTypeDef(TypedDict):
    encryptionType: EncryptionType
    configurationStatus: "ConfigurationStatusTypeDef"


class PutDefaultEncryptionConfigurationResponseTypeDef(
    _RequiredPutDefaultEncryptionConfigurationResponseTypeDef, total=False
):
    kmsKeyArn: str


class ResourceTypeDef(TypedDict, total=False):
    portal: "PortalResourceTypeDef"
    project: "ProjectResourceTypeDef"


class _RequiredTimeInNanosTypeDef(TypedDict):
    timeInSeconds: int


class TimeInNanosTypeDef(_RequiredTimeInNanosTypeDef, total=False):
    offsetInNanos: int


class TransformTypeDef(TypedDict):
    expression: str
    variables: List["ExpressionVariableTypeDef"]


class TumblingWindowTypeDef(TypedDict):
    interval: str


class UpdateAssetModelResponseTypeDef(TypedDict):
    assetModelStatus: "AssetModelStatusTypeDef"


class UpdateAssetResponseTypeDef(TypedDict):
    assetStatus: "AssetStatusTypeDef"


class UpdateGatewayCapabilityConfigurationResponseTypeDef(TypedDict):
    capabilityNamespace: str
    capabilitySyncStatus: CapabilitySyncStatus


class UpdatePortalResponseTypeDef(TypedDict):
    portalStatus: "PortalStatusTypeDef"


UserIdentityTypeDef = TypedDict("UserIdentityTypeDef", {"id": str})


class _RequiredVariableValueTypeDef(TypedDict):
    propertyId: str


class VariableValueTypeDef(_RequiredVariableValueTypeDef, total=False):
    hierarchyId: str


class VariantTypeDef(TypedDict, total=False):
    stringValue: str
    integerValue: int
    doubleValue: float
    booleanValue: bool


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
