"""
Main interface for iotthingsgraph service client

Usage::

    ```python
    import boto3
    from mypy_boto3_iotthingsgraph import IoTThingsGraphClient

    client: IoTThingsGraphClient = boto3.client("iotthingsgraph")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_iotthingsgraph.literals import (
    DeploymentTarget,
    EntityType,
    GetFlowTemplateRevisionsPaginatorName,
    GetSystemTemplateRevisionsPaginatorName,
    ListFlowExecutionMessagesPaginatorName,
    ListTagsForResourcePaginatorName,
    SearchEntitiesPaginatorName,
    SearchFlowExecutionsPaginatorName,
    SearchFlowTemplatesPaginatorName,
    SearchSystemInstancesPaginatorName,
    SearchSystemTemplatesPaginatorName,
    SearchThingsPaginatorName,
)
from mypy_boto3_iotthingsgraph.paginator import (
    GetFlowTemplateRevisionsPaginator,
    GetSystemTemplateRevisionsPaginator,
    ListFlowExecutionMessagesPaginator,
    ListTagsForResourcePaginator,
    SearchEntitiesPaginator,
    SearchFlowExecutionsPaginator,
    SearchFlowTemplatesPaginator,
    SearchSystemInstancesPaginator,
    SearchSystemTemplatesPaginator,
    SearchThingsPaginator,
)
from mypy_boto3_iotthingsgraph.type_defs import (
    CreateFlowTemplateResponseTypeDef,
    CreateSystemInstanceResponseTypeDef,
    CreateSystemTemplateResponseTypeDef,
    DefinitionDocumentTypeDef,
    DeleteNamespaceResponseTypeDef,
    DeploySystemInstanceResponseTypeDef,
    DescribeNamespaceResponseTypeDef,
    EntityFilterTypeDef,
    FlowTemplateFilterTypeDef,
    GetEntitiesResponseTypeDef,
    GetFlowTemplateResponseTypeDef,
    GetFlowTemplateRevisionsResponseTypeDef,
    GetNamespaceDeletionStatusResponseTypeDef,
    GetSystemInstanceResponseTypeDef,
    GetSystemTemplateResponseTypeDef,
    GetSystemTemplateRevisionsResponseTypeDef,
    GetUploadStatusResponseTypeDef,
    ListFlowExecutionMessagesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    MetricsConfigurationTypeDef,
    SearchEntitiesResponseTypeDef,
    SearchFlowExecutionsResponseTypeDef,
    SearchFlowTemplatesResponseTypeDef,
    SearchSystemInstancesResponseTypeDef,
    SearchSystemTemplatesResponseTypeDef,
    SearchThingsResponseTypeDef,
    SystemInstanceFilterTypeDef,
    SystemTemplateFilterTypeDef,
    TagTypeDef,
    UndeploySystemInstanceResponseTypeDef,
    UpdateFlowTemplateResponseTypeDef,
    UpdateSystemTemplateResponseTypeDef,
    UploadEntityDefinitionsResponseTypeDef,
)

__all__ = ("IoTThingsGraphClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceAlreadyExistsException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ThrottlingException: Type[BotocoreClientError]


class IoTThingsGraphClient:
    """
    [IoTThingsGraph.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def associate_entity_to_thing(
        self, thingName: str, entityId: str, namespaceVersion: int = None
    ) -> Dict[str, Any]:
        """
        [Client.associate_entity_to_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.associate_entity_to_thing)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.can_paginate)
        """

    def create_flow_template(
        self, definition: "DefinitionDocumentTypeDef", compatibleNamespaceVersion: int = None
    ) -> CreateFlowTemplateResponseTypeDef:
        """
        [Client.create_flow_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.create_flow_template)
        """

    def create_system_instance(
        self,
        definition: "DefinitionDocumentTypeDef",
        target: DeploymentTarget,
        tags: List["TagTypeDef"] = None,
        greengrassGroupName: str = None,
        s3BucketName: str = None,
        metricsConfiguration: "MetricsConfigurationTypeDef" = None,
        flowActionsRoleArn: str = None,
    ) -> CreateSystemInstanceResponseTypeDef:
        """
        [Client.create_system_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.create_system_instance)
        """

    def create_system_template(
        self, definition: "DefinitionDocumentTypeDef", compatibleNamespaceVersion: int = None
    ) -> CreateSystemTemplateResponseTypeDef:
        """
        [Client.create_system_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.create_system_template)
        """

    def delete_flow_template(self, id: str) -> Dict[str, Any]:
        """
        [Client.delete_flow_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_flow_template)
        """

    def delete_namespace(self) -> DeleteNamespaceResponseTypeDef:
        """
        [Client.delete_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_namespace)
        """

    def delete_system_instance(self, id: str = None) -> Dict[str, Any]:
        """
        [Client.delete_system_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_system_instance)
        """

    def delete_system_template(self, id: str) -> Dict[str, Any]:
        """
        [Client.delete_system_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.delete_system_template)
        """

    def deploy_system_instance(self, id: str = None) -> DeploySystemInstanceResponseTypeDef:
        """
        [Client.deploy_system_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.deploy_system_instance)
        """

    def deprecate_flow_template(self, id: str) -> Dict[str, Any]:
        """
        [Client.deprecate_flow_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.deprecate_flow_template)
        """

    def deprecate_system_template(self, id: str) -> Dict[str, Any]:
        """
        [Client.deprecate_system_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.deprecate_system_template)
        """

    def describe_namespace(self, namespaceName: str = None) -> DescribeNamespaceResponseTypeDef:
        """
        [Client.describe_namespace documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.describe_namespace)
        """

    def dissociate_entity_from_thing(
        self, thingName: str, entityType: EntityType
    ) -> Dict[str, Any]:
        """
        [Client.dissociate_entity_from_thing documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.dissociate_entity_from_thing)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.generate_presigned_url)
        """

    def get_entities(
        self, ids: List[str], namespaceVersion: int = None
    ) -> GetEntitiesResponseTypeDef:
        """
        [Client.get_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_entities)
        """

    def get_flow_template(
        self, id: str, revisionNumber: int = None
    ) -> GetFlowTemplateResponseTypeDef:
        """
        [Client.get_flow_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_flow_template)
        """

    def get_flow_template_revisions(
        self, id: str, nextToken: str = None, maxResults: int = None
    ) -> GetFlowTemplateRevisionsResponseTypeDef:
        """
        [Client.get_flow_template_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_flow_template_revisions)
        """

    def get_namespace_deletion_status(self) -> GetNamespaceDeletionStatusResponseTypeDef:
        """
        [Client.get_namespace_deletion_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_namespace_deletion_status)
        """

    def get_system_instance(self, id: str) -> GetSystemInstanceResponseTypeDef:
        """
        [Client.get_system_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_system_instance)
        """

    def get_system_template(
        self, id: str, revisionNumber: int = None
    ) -> GetSystemTemplateResponseTypeDef:
        """
        [Client.get_system_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_system_template)
        """

    def get_system_template_revisions(
        self, id: str, nextToken: str = None, maxResults: int = None
    ) -> GetSystemTemplateRevisionsResponseTypeDef:
        """
        [Client.get_system_template_revisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_system_template_revisions)
        """

    def get_upload_status(self, uploadId: str) -> GetUploadStatusResponseTypeDef:
        """
        [Client.get_upload_status documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.get_upload_status)
        """

    def list_flow_execution_messages(
        self, flowExecutionId: str, nextToken: str = None, maxResults: int = None
    ) -> ListFlowExecutionMessagesResponseTypeDef:
        """
        [Client.list_flow_execution_messages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.list_flow_execution_messages)
        """

    def list_tags_for_resource(
        self, resourceArn: str, maxResults: int = None, nextToken: str = None
    ) -> ListTagsForResourceResponseTypeDef:
        """
        [Client.list_tags_for_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.list_tags_for_resource)
        """

    def search_entities(
        self,
        entityTypes: List[EntityType],
        filters: List[EntityFilterTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
        namespaceVersion: int = None,
    ) -> SearchEntitiesResponseTypeDef:
        """
        [Client.search_entities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_entities)
        """

    def search_flow_executions(
        self,
        systemInstanceId: str,
        flowExecutionId: str = None,
        startTime: datetime = None,
        endTime: datetime = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> SearchFlowExecutionsResponseTypeDef:
        """
        [Client.search_flow_executions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_flow_executions)
        """

    def search_flow_templates(
        self,
        filters: List[FlowTemplateFilterTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> SearchFlowTemplatesResponseTypeDef:
        """
        [Client.search_flow_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_flow_templates)
        """

    def search_system_instances(
        self,
        filters: List[SystemInstanceFilterTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> SearchSystemInstancesResponseTypeDef:
        """
        [Client.search_system_instances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_system_instances)
        """

    def search_system_templates(
        self,
        filters: List[SystemTemplateFilterTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> SearchSystemTemplatesResponseTypeDef:
        """
        [Client.search_system_templates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_system_templates)
        """

    def search_things(
        self,
        entityId: str,
        nextToken: str = None,
        maxResults: int = None,
        namespaceVersion: int = None,
    ) -> SearchThingsResponseTypeDef:
        """
        [Client.search_things documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.search_things)
        """

    def tag_resource(self, resourceArn: str, tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Client.tag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.tag_resource)
        """

    def undeploy_system_instance(self, id: str = None) -> UndeploySystemInstanceResponseTypeDef:
        """
        [Client.undeploy_system_instance documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.undeploy_system_instance)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Client.untag_resource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.untag_resource)
        """

    def update_flow_template(
        self,
        id: str,
        definition: "DefinitionDocumentTypeDef",
        compatibleNamespaceVersion: int = None,
    ) -> UpdateFlowTemplateResponseTypeDef:
        """
        [Client.update_flow_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.update_flow_template)
        """

    def update_system_template(
        self,
        id: str,
        definition: "DefinitionDocumentTypeDef",
        compatibleNamespaceVersion: int = None,
    ) -> UpdateSystemTemplateResponseTypeDef:
        """
        [Client.update_system_template documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.update_system_template)
        """

    def upload_entity_definitions(
        self,
        document: "DefinitionDocumentTypeDef" = None,
        syncWithPublicNamespace: bool = None,
        deprecateExistingEntities: bool = None,
    ) -> UploadEntityDefinitionsResponseTypeDef:
        """
        [Client.upload_entity_definitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Client.upload_entity_definitions)
        """

    @overload
    def get_paginator(
        self, operation_name: GetFlowTemplateRevisionsPaginatorName
    ) -> GetFlowTemplateRevisionsPaginator:
        """
        [Paginator.GetFlowTemplateRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetFlowTemplateRevisions)
        """

    @overload
    def get_paginator(
        self, operation_name: GetSystemTemplateRevisionsPaginatorName
    ) -> GetSystemTemplateRevisionsPaginator:
        """
        [Paginator.GetSystemTemplateRevisions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.GetSystemTemplateRevisions)
        """

    @overload
    def get_paginator(
        self, operation_name: ListFlowExecutionMessagesPaginatorName
    ) -> ListFlowExecutionMessagesPaginator:
        """
        [Paginator.ListFlowExecutionMessages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListFlowExecutionMessages)
        """

    @overload
    def get_paginator(
        self, operation_name: ListTagsForResourcePaginatorName
    ) -> ListTagsForResourcePaginator:
        """
        [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.ListTagsForResource)
        """

    @overload
    def get_paginator(self, operation_name: SearchEntitiesPaginatorName) -> SearchEntitiesPaginator:
        """
        [Paginator.SearchEntities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchEntities)
        """

    @overload
    def get_paginator(
        self, operation_name: SearchFlowExecutionsPaginatorName
    ) -> SearchFlowExecutionsPaginator:
        """
        [Paginator.SearchFlowExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowExecutions)
        """

    @overload
    def get_paginator(
        self, operation_name: SearchFlowTemplatesPaginatorName
    ) -> SearchFlowTemplatesPaginator:
        """
        [Paginator.SearchFlowTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchFlowTemplates)
        """

    @overload
    def get_paginator(
        self, operation_name: SearchSystemInstancesPaginatorName
    ) -> SearchSystemInstancesPaginator:
        """
        [Paginator.SearchSystemInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemInstances)
        """

    @overload
    def get_paginator(
        self, operation_name: SearchSystemTemplatesPaginatorName
    ) -> SearchSystemTemplatesPaginator:
        """
        [Paginator.SearchSystemTemplates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchSystemTemplates)
        """

    @overload
    def get_paginator(self, operation_name: SearchThingsPaginatorName) -> SearchThingsPaginator:
        """
        [Paginator.SearchThings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iotthingsgraph.html#IoTThingsGraph.Paginator.SearchThings)
        """
