"""
Main interface for iotthingsgraph service type definitions.

Usage::

    ```python
    from mypy_boto3_iotthingsgraph.type_defs import DefinitionDocumentTypeDef

    data: DefinitionDocumentTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_iotthingsgraph.literals import (
    DefinitionLanguage,
    DeploymentTarget,
    EntityFilterName,
    EntityType,
    FlowExecutionEventType,
    FlowExecutionStatus,
    FlowTemplateFilterName,
    NamespaceDeletionStatus,
    NamespaceDeletionStatusErrorCodes,
    SystemInstanceDeploymentStatus,
    SystemInstanceFilterName,
    SystemTemplateFilterName,
    UploadStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DefinitionDocumentTypeDef",
    "DependencyRevisionTypeDef",
    "EntityDescriptionTypeDef",
    "FlowExecutionMessageTypeDef",
    "FlowExecutionSummaryTypeDef",
    "FlowTemplateDescriptionTypeDef",
    "FlowTemplateSummaryTypeDef",
    "MetricsConfigurationTypeDef",
    "SystemInstanceDescriptionTypeDef",
    "SystemInstanceSummaryTypeDef",
    "SystemTemplateDescriptionTypeDef",
    "SystemTemplateSummaryTypeDef",
    "TagTypeDef",
    "ThingTypeDef",
    "CreateFlowTemplateResponseTypeDef",
    "CreateSystemInstanceResponseTypeDef",
    "CreateSystemTemplateResponseTypeDef",
    "DeleteNamespaceResponseTypeDef",
    "DeploySystemInstanceResponseTypeDef",
    "DescribeNamespaceResponseTypeDef",
    "EntityFilterTypeDef",
    "FlowTemplateFilterTypeDef",
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
    "PaginatorConfigTypeDef",
    "SearchEntitiesResponseTypeDef",
    "SearchFlowExecutionsResponseTypeDef",
    "SearchFlowTemplatesResponseTypeDef",
    "SearchSystemInstancesResponseTypeDef",
    "SearchSystemTemplatesResponseTypeDef",
    "SearchThingsResponseTypeDef",
    "SystemInstanceFilterTypeDef",
    "SystemTemplateFilterTypeDef",
    "UndeploySystemInstanceResponseTypeDef",
    "UpdateFlowTemplateResponseTypeDef",
    "UpdateSystemTemplateResponseTypeDef",
    "UploadEntityDefinitionsResponseTypeDef",
)

DefinitionDocumentTypeDef = TypedDict(
    "DefinitionDocumentTypeDef", {"language": DefinitionLanguage, "text": str}
)

DependencyRevisionTypeDef = TypedDict(
    "DependencyRevisionTypeDef", {"id": str, "revisionNumber": int}, total=False
)

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

FlowExecutionMessageTypeDef = TypedDict(
    "FlowExecutionMessageTypeDef",
    {"messageId": str, "eventType": FlowExecutionEventType, "timestamp": datetime, "payload": str},
    total=False,
)

FlowExecutionSummaryTypeDef = TypedDict(
    "FlowExecutionSummaryTypeDef",
    {
        "flowExecutionId": str,
        "status": FlowExecutionStatus,
        "systemInstanceId": str,
        "flowTemplateId": str,
        "createdAt": datetime,
        "updatedAt": datetime,
    },
    total=False,
)

FlowTemplateDescriptionTypeDef = TypedDict(
    "FlowTemplateDescriptionTypeDef",
    {
        "summary": "FlowTemplateSummaryTypeDef",
        "definition": "DefinitionDocumentTypeDef",
        "validatedNamespaceVersion": int,
    },
    total=False,
)

FlowTemplateSummaryTypeDef = TypedDict(
    "FlowTemplateSummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

MetricsConfigurationTypeDef = TypedDict(
    "MetricsConfigurationTypeDef",
    {"cloudMetricEnabled": bool, "metricRuleRoleArn": str},
    total=False,
)

SystemInstanceDescriptionTypeDef = TypedDict(
    "SystemInstanceDescriptionTypeDef",
    {
        "summary": "SystemInstanceSummaryTypeDef",
        "definition": "DefinitionDocumentTypeDef",
        "s3BucketName": str,
        "metricsConfiguration": "MetricsConfigurationTypeDef",
        "validatedNamespaceVersion": int,
        "validatedDependencyRevisions": List["DependencyRevisionTypeDef"],
        "flowActionsRoleArn": str,
    },
    total=False,
)

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

SystemTemplateDescriptionTypeDef = TypedDict(
    "SystemTemplateDescriptionTypeDef",
    {
        "summary": "SystemTemplateSummaryTypeDef",
        "definition": "DefinitionDocumentTypeDef",
        "validatedNamespaceVersion": int,
    },
    total=False,
)

SystemTemplateSummaryTypeDef = TypedDict(
    "SystemTemplateSummaryTypeDef",
    {"id": str, "arn": str, "revisionNumber": int, "createdAt": datetime},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"key": str, "value": str})

ThingTypeDef = TypedDict("ThingTypeDef", {"thingArn": str, "thingName": str}, total=False)

CreateFlowTemplateResponseTypeDef = TypedDict(
    "CreateFlowTemplateResponseTypeDef", {"summary": "FlowTemplateSummaryTypeDef"}, total=False
)

CreateSystemInstanceResponseTypeDef = TypedDict(
    "CreateSystemInstanceResponseTypeDef", {"summary": "SystemInstanceSummaryTypeDef"}, total=False
)

CreateSystemTemplateResponseTypeDef = TypedDict(
    "CreateSystemTemplateResponseTypeDef", {"summary": "SystemTemplateSummaryTypeDef"}, total=False
)

DeleteNamespaceResponseTypeDef = TypedDict(
    "DeleteNamespaceResponseTypeDef", {"namespaceArn": str, "namespaceName": str}, total=False
)

_RequiredDeploySystemInstanceResponseTypeDef = TypedDict(
    "_RequiredDeploySystemInstanceResponseTypeDef", {"summary": "SystemInstanceSummaryTypeDef"}
)
_OptionalDeploySystemInstanceResponseTypeDef = TypedDict(
    "_OptionalDeploySystemInstanceResponseTypeDef", {"greengrassDeploymentId": str}, total=False
)


class DeploySystemInstanceResponseTypeDef(
    _RequiredDeploySystemInstanceResponseTypeDef, _OptionalDeploySystemInstanceResponseTypeDef
):
    pass


DescribeNamespaceResponseTypeDef = TypedDict(
    "DescribeNamespaceResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "trackingNamespaceName": str,
        "trackingNamespaceVersion": int,
        "namespaceVersion": int,
    },
    total=False,
)

EntityFilterTypeDef = TypedDict(
    "EntityFilterTypeDef", {"name": EntityFilterName, "value": List[str]}, total=False
)

FlowTemplateFilterTypeDef = TypedDict(
    "FlowTemplateFilterTypeDef", {"name": FlowTemplateFilterName, "value": List[str]}
)

GetEntitiesResponseTypeDef = TypedDict(
    "GetEntitiesResponseTypeDef", {"descriptions": List["EntityDescriptionTypeDef"]}, total=False
)

GetFlowTemplateResponseTypeDef = TypedDict(
    "GetFlowTemplateResponseTypeDef", {"description": "FlowTemplateDescriptionTypeDef"}, total=False
)

GetFlowTemplateRevisionsResponseTypeDef = TypedDict(
    "GetFlowTemplateRevisionsResponseTypeDef",
    {"summaries": List["FlowTemplateSummaryTypeDef"], "nextToken": str},
    total=False,
)

GetNamespaceDeletionStatusResponseTypeDef = TypedDict(
    "GetNamespaceDeletionStatusResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "status": NamespaceDeletionStatus,
        "errorCode": NamespaceDeletionStatusErrorCodes,
        "errorMessage": str,
    },
    total=False,
)

GetSystemInstanceResponseTypeDef = TypedDict(
    "GetSystemInstanceResponseTypeDef",
    {"description": "SystemInstanceDescriptionTypeDef"},
    total=False,
)

GetSystemTemplateResponseTypeDef = TypedDict(
    "GetSystemTemplateResponseTypeDef",
    {"description": "SystemTemplateDescriptionTypeDef"},
    total=False,
)

GetSystemTemplateRevisionsResponseTypeDef = TypedDict(
    "GetSystemTemplateRevisionsResponseTypeDef",
    {"summaries": List["SystemTemplateSummaryTypeDef"], "nextToken": str},
    total=False,
)

_RequiredGetUploadStatusResponseTypeDef = TypedDict(
    "_RequiredGetUploadStatusResponseTypeDef",
    {"uploadId": str, "uploadStatus": UploadStatus, "createdDate": datetime},
)
_OptionalGetUploadStatusResponseTypeDef = TypedDict(
    "_OptionalGetUploadStatusResponseTypeDef",
    {
        "namespaceArn": str,
        "namespaceName": str,
        "namespaceVersion": int,
        "failureReason": List[str],
    },
    total=False,
)


class GetUploadStatusResponseTypeDef(
    _RequiredGetUploadStatusResponseTypeDef, _OptionalGetUploadStatusResponseTypeDef
):
    pass


ListFlowExecutionMessagesResponseTypeDef = TypedDict(
    "ListFlowExecutionMessagesResponseTypeDef",
    {"messages": List["FlowExecutionMessageTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"tags": List["TagTypeDef"], "nextToken": str},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SearchEntitiesResponseTypeDef = TypedDict(
    "SearchEntitiesResponseTypeDef",
    {"descriptions": List["EntityDescriptionTypeDef"], "nextToken": str},
    total=False,
)

SearchFlowExecutionsResponseTypeDef = TypedDict(
    "SearchFlowExecutionsResponseTypeDef",
    {"summaries": List["FlowExecutionSummaryTypeDef"], "nextToken": str},
    total=False,
)

SearchFlowTemplatesResponseTypeDef = TypedDict(
    "SearchFlowTemplatesResponseTypeDef",
    {"summaries": List["FlowTemplateSummaryTypeDef"], "nextToken": str},
    total=False,
)

SearchSystemInstancesResponseTypeDef = TypedDict(
    "SearchSystemInstancesResponseTypeDef",
    {"summaries": List["SystemInstanceSummaryTypeDef"], "nextToken": str},
    total=False,
)

SearchSystemTemplatesResponseTypeDef = TypedDict(
    "SearchSystemTemplatesResponseTypeDef",
    {"summaries": List["SystemTemplateSummaryTypeDef"], "nextToken": str},
    total=False,
)

SearchThingsResponseTypeDef = TypedDict(
    "SearchThingsResponseTypeDef", {"things": List["ThingTypeDef"], "nextToken": str}, total=False
)

SystemInstanceFilterTypeDef = TypedDict(
    "SystemInstanceFilterTypeDef",
    {"name": SystemInstanceFilterName, "value": List[str]},
    total=False,
)

SystemTemplateFilterTypeDef = TypedDict(
    "SystemTemplateFilterTypeDef", {"name": SystemTemplateFilterName, "value": List[str]}
)

UndeploySystemInstanceResponseTypeDef = TypedDict(
    "UndeploySystemInstanceResponseTypeDef",
    {"summary": "SystemInstanceSummaryTypeDef"},
    total=False,
)

UpdateFlowTemplateResponseTypeDef = TypedDict(
    "UpdateFlowTemplateResponseTypeDef", {"summary": "FlowTemplateSummaryTypeDef"}, total=False
)

UpdateSystemTemplateResponseTypeDef = TypedDict(
    "UpdateSystemTemplateResponseTypeDef", {"summary": "SystemTemplateSummaryTypeDef"}, total=False
)

UploadEntityDefinitionsResponseTypeDef = TypedDict(
    "UploadEntityDefinitionsResponseTypeDef", {"uploadId": str}
)
