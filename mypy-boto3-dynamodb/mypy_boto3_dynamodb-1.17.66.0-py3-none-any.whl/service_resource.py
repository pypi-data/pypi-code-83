"""
Type annotations for dynamodb service ServiceResource

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_dynamodb import DynamoDBServiceResource
    import mypy_boto3_dynamodb.service_resource as dynamodb_resources

    resource: DynamoDBServiceResource = boto3.resource("dynamodb")

    my_table: dynamodb_resources.Table = resource.Table(...)
```
"""
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, Iterator, List, Set, Union

from boto3.dynamodb.conditions import ConditionBase
from boto3.dynamodb.table import BatchWriter
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from mypy_boto3_dynamodb.literals import (
    BillingMode,
    ConditionalOperator,
    ReturnConsumedCapacity,
    ReturnItemCollectionMetrics,
    ReturnValue,
    Select,
)
from mypy_boto3_dynamodb.type_defs import (
    AttributeDefinitionTypeDef,
    AttributeValueUpdateTypeDef,
    BatchGetItemOutputTypeDef,
    BatchWriteItemOutputTypeDef,
    ConditionTypeDef,
    DeleteItemOutputTypeDef,
    DeleteTableOutputTypeDef,
    ExpectedAttributeValueTypeDef,
    GetItemOutputTypeDef,
    GlobalSecondaryIndexTypeDef,
    GlobalSecondaryIndexUpdateTypeDef,
    KeysAndAttributesTypeDef,
    KeySchemaElementTypeDef,
    LocalSecondaryIndexTypeDef,
    ProvisionedThroughputTypeDef,
    PutItemOutputTypeDef,
    QueryOutputTypeDef,
    ReplicationGroupUpdateTypeDef,
    ScanOutputTypeDef,
    SSESpecificationTypeDef,
    StreamSpecificationTypeDef,
    TagTypeDef,
    UpdateItemOutputTypeDef,
    WriteRequestTypeDef,
)

__all__ = ("DynamoDBServiceResource", "Table", "ServiceResourceTablesCollection")


class ServiceResourceTablesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.ServiceResource.tables)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#serviceresourcetablescollection)
    """

    def all(self) -> "ServiceResourceTablesCollection":
        pass

    def filter(  # type: ignore
        self, ExclusiveStartTableName: str = None, Limit: int = None
    ) -> "ServiceResourceTablesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceTablesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceTablesCollection":
        pass

    def pages(self) -> Iterator[List["Table"]]:
        pass

    def __iter__(self) -> Iterator["Table"]:
        pass


class Table(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.ServiceResource.Table)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#table)
    """

    attribute_definitions: List[Any]
    table_name: str
    key_schema: List[Any]
    table_status: str
    creation_date_time: datetime
    provisioned_throughput: Dict[str, Any]
    table_size_bytes: int
    item_count: int
    table_arn: str
    table_id: str
    billing_mode_summary: Dict[str, Any]
    local_secondary_indexes: List[Any]
    global_secondary_indexes: List[Any]
    stream_specification: Dict[str, Any]
    latest_stream_label: str
    latest_stream_arn: str
    global_table_version: str
    replicas: List[Any]
    restore_summary: Dict[str, Any]
    sse_description: Dict[str, Any]
    archival_summary: Dict[str, Any]
    name: str

    def batch_writer(self, overwrite_by_pkeys: List[str] = None) -> BatchWriter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.Table.batch_writer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#tablebatch-writermethod)
        """

    def delete(self) -> DeleteTableOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.Table.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#tabledeletemethod)
        """

    def delete_item(
        self,
        Key: Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        Expected: Dict[str, ExpectedAttributeValueTypeDef] = None,
        ConditionalOperator: ConditionalOperator = None,
        ReturnValues: ReturnValue = None,
        ReturnConsumedCapacity: ReturnConsumedCapacity = None,
        ReturnItemCollectionMetrics: ReturnItemCollectionMetrics = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ] = None,
    ) -> DeleteItemOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.Table.delete_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#tabledelete-itemmethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.Table.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#tableget-available-subresourcesmethod)
        """

    def get_item(
        self,
        Key: Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        AttributesToGet: List[str] = None,
        ConsistentRead: bool = None,
        ReturnConsumedCapacity: ReturnConsumedCapacity = None,
        ProjectionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
    ) -> GetItemOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.Table.get_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#tableget-itemmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.Table.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#tableloadmethod)
        """

    def put_item(
        self,
        Item: Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        Expected: Dict[str, ExpectedAttributeValueTypeDef] = None,
        ReturnValues: ReturnValue = None,
        ReturnConsumedCapacity: ReturnConsumedCapacity = None,
        ReturnItemCollectionMetrics: ReturnItemCollectionMetrics = None,
        ConditionalOperator: ConditionalOperator = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ] = None,
    ) -> PutItemOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.Table.put_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#tableput-itemmethod)
        """

    def query(
        self,
        IndexName: str = None,
        Select: Select = None,
        AttributesToGet: List[str] = None,
        Limit: int = None,
        ConsistentRead: bool = None,
        KeyConditions: Dict[str, ConditionTypeDef] = None,
        QueryFilter: Dict[str, ConditionTypeDef] = None,
        ConditionalOperator: ConditionalOperator = None,
        ScanIndexForward: bool = None,
        ExclusiveStartKey: Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ] = None,
        ReturnConsumedCapacity: ReturnConsumedCapacity = None,
        ProjectionExpression: str = None,
        FilterExpression: Union[str, ConditionBase] = None,
        KeyConditionExpression: Union[str, ConditionBase] = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ] = None,
    ) -> QueryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.Table.query)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#tablequerymethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.Table.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#tablereloadmethod)
        """

    def scan(
        self,
        IndexName: str = None,
        AttributesToGet: List[str] = None,
        Limit: int = None,
        Select: Select = None,
        ScanFilter: Dict[str, ConditionTypeDef] = None,
        ConditionalOperator: ConditionalOperator = None,
        ExclusiveStartKey: Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ] = None,
        ReturnConsumedCapacity: ReturnConsumedCapacity = None,
        TotalSegments: int = None,
        Segment: int = None,
        ProjectionExpression: str = None,
        FilterExpression: Union[str, ConditionBase] = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ] = None,
        ConsistentRead: bool = None,
    ) -> ScanOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.Table.scan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#tablescanmethod)
        """

    def update(
        self,
        AttributeDefinitions: List["AttributeDefinitionTypeDef"] = None,
        BillingMode: BillingMode = None,
        ProvisionedThroughput: "ProvisionedThroughputTypeDef" = None,
        GlobalSecondaryIndexUpdates: List[GlobalSecondaryIndexUpdateTypeDef] = None,
        StreamSpecification: "StreamSpecificationTypeDef" = None,
        SSESpecification: SSESpecificationTypeDef = None,
        ReplicaUpdates: List[ReplicationGroupUpdateTypeDef] = None,
    ) -> "_Table":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.Table.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#tableupdatemethod)
        """

    def update_item(
        self,
        Key: Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ],
        AttributeUpdates: Dict[str, AttributeValueUpdateTypeDef] = None,
        Expected: Dict[str, ExpectedAttributeValueTypeDef] = None,
        ConditionalOperator: ConditionalOperator = None,
        ReturnValues: ReturnValue = None,
        ReturnConsumedCapacity: ReturnConsumedCapacity = None,
        ReturnItemCollectionMetrics: ReturnItemCollectionMetrics = None,
        UpdateExpression: str = None,
        ConditionExpression: str = None,
        ExpressionAttributeNames: Dict[str, str] = None,
        ExpressionAttributeValues: Dict[
            str,
            Union[
                bytes,
                bytearray,
                str,
                int,
                Decimal,
                bool,
                Set[int],
                Set[Decimal],
                Set[str],
                Set[bytes],
                Set[bytearray],
                List[Any],
                Dict[str, Any],
                None,
            ],
        ] = None,
    ) -> UpdateItemOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.Table.update_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#tableupdate-itemmethod)
        """

    def wait_until_exists(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.Table.wait_until_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#tablewait-until-existsmethod)
        """

    def wait_until_not_exists(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.Table.wait_until_not_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#tablewait-until-not-existsmethod)
        """


_Table = Table


class DynamoDBServiceResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.ServiceResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html)
    """

    tables: ServiceResourceTablesCollection

    def Table(self, name: str) -> _Table:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.ServiceResource.Table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#dynamodbserviceresourcetablemethod)
        """

    def batch_get_item(
        self,
        RequestItems: Dict[str, "KeysAndAttributesTypeDef"],
        ReturnConsumedCapacity: ReturnConsumedCapacity = None,
    ) -> BatchGetItemOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.ServiceResource.batch_get_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#dynamodbserviceresourcebatch-get-itemmethod)
        """

    def batch_write_item(
        self,
        RequestItems: Dict[str, List["WriteRequestTypeDef"]],
        ReturnConsumedCapacity: ReturnConsumedCapacity = None,
        ReturnItemCollectionMetrics: ReturnItemCollectionMetrics = None,
    ) -> BatchWriteItemOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.ServiceResource.batch_write_item)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#dynamodbserviceresourcebatch-write-itemmethod)
        """

    def create_table(
        self,
        AttributeDefinitions: List["AttributeDefinitionTypeDef"],
        TableName: str,
        KeySchema: List["KeySchemaElementTypeDef"],
        LocalSecondaryIndexes: List[LocalSecondaryIndexTypeDef] = None,
        GlobalSecondaryIndexes: List[GlobalSecondaryIndexTypeDef] = None,
        BillingMode: BillingMode = None,
        ProvisionedThroughput: "ProvisionedThroughputTypeDef" = None,
        StreamSpecification: "StreamSpecificationTypeDef" = None,
        SSESpecification: SSESpecificationTypeDef = None,
        Tags: List["TagTypeDef"] = None,
    ) -> _Table:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.ServiceResource.create_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#dynamodbserviceresourcecreate-tablemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/dynamodb.html#DynamoDB.ServiceResource.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dynamodb/service_resource.html#dynamodbserviceresourceget-available-subresourcesmethod)
        """
