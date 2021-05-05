"""
Type annotations for iotthingsgraph service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotthingsgraph/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotthingsgraph.type_defs import CreateFlowTemplateResponseTypeDef

    data: CreateFlowTemplateResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_iotthingsgraph.literals import (
    DeploymentTarget,
    EntityFilterName,
    EntityType,
    FlowExecutionEventType,
    FlowExecutionStatus,
    NamespaceDeletionStatus,
    SystemInstanceDeploymentStatus,
    SystemInstanceFilterName,
    UploadStatus,
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
    "CreateFlowTemplateResponseTypeDef",
    "CreateSystemInstanceResponseTypeDef",
    "CreateSystemTemplateResponseTypeDef",
    "DefinitionDocumentTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DependencyRevisionTypeDef",
    "DeploySystemInstanceResponseTypeDef",
    "DescribeNamespaceResponseTypeDef",
    "EntityDescriptionTypeDef",
    "EntityFilterTypeDef",
    "FlowExecutionMessageTypeDef",
    "FlowExecutionSummaryTypeDef",
    "FlowTemplateDescriptionTypeDef",
    "FlowTemplateFilterTypeDef",
    "FlowTemplateSummaryTypeDef",
    "GetEntitiesResponseTypeDef",
    "GetFlowTemplateResponseTypeDef",
    "GetFlowTemplateRevisionsResponseTypeDef",
    "GetNamespaceDeletionStatusResponseTypeDef",
    "GetSystemInstanceResponseTypeDef",
    "GetSystemTemplateResponseTypeDef",
    "GetSystemTemplateRevisionsResponseTypeDef",
    "GetUploadStatusResponseTypeDef",
    "ListFlowExecutionMessagesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MetricsConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "SearchEntitiesResponseTypeDef",
    "SearchFlowExecutionsResponseTypeDef",
    "SearchFlowTemplatesResponseTypeDef",
    "SearchSystemInstancesResponseTypeDef",
    "SearchSystemTemplatesResponseTypeDef",
    "SearchThingsResponseTypeDef",
    "SystemInstanceDescriptionTypeDef",
    "SystemInstanceFilterTypeDef",
    "SystemInstanceSummaryTypeDef",
    "SystemTemplateDescriptionTypeDef",
    "SystemTemplateFilterTypeDef",
    "SystemTemplateSummaryTypeDef",
    "TagTypeDef",
    "ThingTypeDef",
    "UndeploySystemInstanceResponseTypeDef",
    "UpdateFlowTemplateResponseTypeDef",
    "UpdateSystemTemplateResponseTypeDef",
    "UploadEntityDefinitionsResponseTypeDef",
)


class CreateFlowTemplateResponseTypeDef(TypedDict, total=False):
    summary: "FlowTemplateSummaryTypeDef"


class CreateSystemInstanceResponseTypeDef(TypedDict, total=False):
    summary: "SystemInstanceSummaryTypeDef"


class CreateSystemTemplateResponseTypeDef(TypedDict, total=False):
    summary: "SystemTemplateSummaryTypeDef"


class DefinitionDocumentTypeDef(TypedDict):
    language: Literal["GRAPHQL"]
    text: str


class DeleteNamespaceResponseTypeDef(TypedDict, total=False):
    namespaceArn: str
    namespaceName: str


DependencyRevisionTypeDef = TypedDict(
    "DependencyRevisionTypeDef", {"id": str, "revisionNumber": int}, total=False
)


class _RequiredDeploySystemInstanceResponseTypeDef(TypedDict):
    summary: "SystemInstanceSummaryTypeDef"


class DeploySystemInstanceResponseTypeDef(
    _RequiredDeploySystemInstanceResponseTypeDef, total=False
):
    greengrassDeploymentId: str


class DescribeNamespaceResponseTypeDef(TypedDict, total=False):
    namespaceArn: str
    namespaceName: str
    trackingNamespaceName: str
    trackingNamespaceVersion: int
    namespaceVersion: int


EntityDescriptionTypeDef = TypedDict(
    "EntityDescriptionTypeDef",
    {
        "id": str,
        "arn": str,
        "type": EntityType,
        "createdAt": datetime,
        "definition": "DefinitionDocumentTypeDef",
    },
    total=False,
)


class EntityFilterTypeDef(TypedDict, total=False):
    name: EntityFilterName
    value: List[str]


class FlowExecutionMessageTypeDef(TypedDict, total=False):
    messageId: str
    eventType: FlowExecutionEventType
    timestamp: datetime
    payload: str


class FlowExecutionSummaryTypeDef(TypedDict, total=False):
    flowExecutionId: str
    status: FlowExecutionStatus
    systemInstanceId: str
    flowTemplateId: str
    createdAt: datetime
    updatedAt: datetime


class FlowTemplateDescriptionTypeDef(TypedDict, total=False):
    summary: "FlowTemplateSummaryTypeDef"
    definition: "DefinitionDocumentTypeDef"
    validatedNamespaceVersion: int


class FlowTemplateFilterTypeDef(TypedDict):
    name: Literal["DEVICE_MODEL_ID"]
    value: List[str]


FlowTemplateSummaryTypeDef = TypedDict(
    "FlowTemplateSummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class GetEntitiesResponseTypeDef(TypedDict, total=False):
    descriptions: List["EntityDescriptionTypeDef"]


class GetFlowTemplateResponseTypeDef(TypedDict, total=False):
    description: "FlowTemplateDescriptionTypeDef"


class GetFlowTemplateRevisionsResponseTypeDef(TypedDict, total=False):
    summaries: List["FlowTemplateSummaryTypeDef"]
    nextToken: str


class GetNamespaceDeletionStatusResponseTypeDef(TypedDict, total=False):
    namespaceArn: str
    namespaceName: str
    status: NamespaceDeletionStatus
    errorCode: Literal["VALIDATION_FAILED"]
    errorMessage: str


class GetSystemInstanceResponseTypeDef(TypedDict, total=False):
    description: "SystemInstanceDescriptionTypeDef"


class GetSystemTemplateResponseTypeDef(TypedDict, total=False):
    description: "SystemTemplateDescriptionTypeDef"


class GetSystemTemplateRevisionsResponseTypeDef(TypedDict, total=False):
    summaries: List["SystemTemplateSummaryTypeDef"]
    nextToken: str


class _RequiredGetUploadStatusResponseTypeDef(TypedDict):
    uploadId: str
    uploadStatus: UploadStatus
    createdDate: datetime


class GetUploadStatusResponseTypeDef(_RequiredGetUploadStatusResponseTypeDef, total=False):
    namespaceArn: str
    namespaceName: str
    namespaceVersion: int
    failureReason: List[str]


class ListFlowExecutionMessagesResponseTypeDef(TypedDict, total=False):
    messages: List["FlowExecutionMessageTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: List["TagTypeDef"]
    nextToken: str


class MetricsConfigurationTypeDef(TypedDict, total=False):
    cloudMetricEnabled: bool
    metricRuleRoleArn: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class SearchEntitiesResponseTypeDef(TypedDict, total=False):
    descriptions: List["EntityDescriptionTypeDef"]
    nextToken: str


class SearchFlowExecutionsResponseTypeDef(TypedDict, total=False):
    summaries: List["FlowExecutionSummaryTypeDef"]
    nextToken: str


class SearchFlowTemplatesResponseTypeDef(TypedDict, total=False):
    summaries: List["FlowTemplateSummaryTypeDef"]
    nextToken: str


class SearchSystemInstancesResponseTypeDef(TypedDict, total=False):
    summaries: List["SystemInstanceSummaryTypeDef"]
    nextToken: str


class SearchSystemTemplatesResponseTypeDef(TypedDict, total=False):
    summaries: List["SystemTemplateSummaryTypeDef"]
    nextToken: str


class SearchThingsResponseTypeDef(TypedDict, total=False):
    things: List["ThingTypeDef"]
    nextToken: str


class SystemInstanceDescriptionTypeDef(TypedDict, total=False):
    summary: "SystemInstanceSummaryTypeDef"
    definition: "DefinitionDocumentTypeDef"
    s3BucketName: str
    metricsConfiguration: "MetricsConfigurationTypeDef"
    validatedNamespaceVersion: int
    validatedDependencyRevisions: List["DependencyRevisionTypeDef"]
    flowActionsRoleArn: str


class SystemInstanceFilterTypeDef(TypedDict, total=False):
    name: SystemInstanceFilterName
    value: List[str]


SystemInstanceSummaryTypeDef = TypedDict(
    "SystemInstanceSummaryTypeDef",
    {
        "id": str,
        "arn": str,
        "status": SystemInstanceDeploymentStatus,
        "target": DeploymentTarget,
        "greengrassGroupName": str,
        "createdAt": datetime,
        "updatedAt": datetime,
        "greengrassGroupId": str,
        "greengrassGroupVersionId": str,
    },
    total=False,
)


class SystemTemplateDescriptionTypeDef(TypedDict, total=False):
    summary: "SystemTemplateSummaryTypeDef"
    definition: "DefinitionDocumentTypeDef"
    validatedNamespaceVersion: int


class SystemTemplateFilterTypeDef(TypedDict):
    name: Literal["FLOW_TEMPLATE_ID"]
    value: List[str]


SystemTemplateSummaryTypeDef = TypedDict(
    "SystemTemplateSummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)


class TagTypeDef(TypedDict):
    key: str
    value: str


class ThingTypeDef(TypedDict, total=False):
    thingArn: str
    thingName: str


class UndeploySystemInstanceResponseTypeDef(TypedDict, total=False):
    summary: "SystemInstanceSummaryTypeDef"


class UpdateFlowTemplateResponseTypeDef(TypedDict, total=False):
    summary: "FlowTemplateSummaryTypeDef"


class UpdateSystemTemplateResponseTypeDef(TypedDict, total=False):
    summary: "SystemTemplateSummaryTypeDef"


class UploadEntityDefinitionsResponseTypeDef(TypedDict):
    uploadId: str
