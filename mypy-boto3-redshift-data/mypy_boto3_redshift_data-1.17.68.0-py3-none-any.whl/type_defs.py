"""
Type annotations for redshift-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_redshift_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_redshift_data.type_defs import CancelStatementResponseTypeDef

    data: CancelStatementResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_redshift_data.literals import StatusString

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelStatementResponseTypeDef",
    "ColumnMetadataTypeDef",
    "DescribeStatementResponseTypeDef",
    "DescribeTableResponseTypeDef",
    "ExecuteStatementOutputTypeDef",
    "FieldTypeDef",
    "GetStatementResultResponseTypeDef",
    "ListDatabasesResponseTypeDef",
    "ListSchemasResponseTypeDef",
    "ListStatementsResponseTypeDef",
    "ListTablesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ResponseMetadata",
    "StatementDataTypeDef",
    "TableMemberTypeDef",
)


class CancelStatementResponseTypeDef(TypedDict, total=False):
    Status: bool


class ColumnMetadataTypeDef(TypedDict, total=False):
    columnDefault: str
    isCaseSensitive: bool
    isCurrency: bool
    isSigned: bool
    label: str
    length: int
    name: str
    nullable: int
    precision: int
    scale: int
    schemaName: str
    tableName: str
    typeName: str


class _RequiredDescribeStatementResponseTypeDef(TypedDict):
    Id: str


class DescribeStatementResponseTypeDef(_RequiredDescribeStatementResponseTypeDef, total=False):
    ClusterIdentifier: str
    CreatedAt: datetime
    Database: str
    DbUser: str
    Duration: int
    Error: str
    HasResultSet: bool
    QueryString: str
    RedshiftPid: int
    RedshiftQueryId: int
    ResultRows: int
    ResultSize: int
    SecretArn: str
    Status: StatusString
    UpdatedAt: datetime


class DescribeTableResponseTypeDef(TypedDict, total=False):
    ColumnList: List["ColumnMetadataTypeDef"]
    NextToken: str
    TableName: str


class ExecuteStatementOutputTypeDef(TypedDict):
    ClusterIdentifier: str
    CreatedAt: datetime
    Database: str
    DbUser: str
    Id: str
    SecretArn: str
    ResponseMetadata: "ResponseMetadata"


class FieldTypeDef(TypedDict, total=False):
    blobValue: Union[bytes, IO[bytes]]
    booleanValue: bool
    doubleValue: float
    isNull: bool
    longValue: int
    stringValue: str


class _RequiredGetStatementResultResponseTypeDef(TypedDict):
    Records: List[List["FieldTypeDef"]]


class GetStatementResultResponseTypeDef(_RequiredGetStatementResultResponseTypeDef, total=False):
    ColumnMetadata: List["ColumnMetadataTypeDef"]
    NextToken: str
    TotalNumRows: int


class ListDatabasesResponseTypeDef(TypedDict, total=False):
    Databases: List[str]
    NextToken: str


class ListSchemasResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Schemas: List[str]


class _RequiredListStatementsResponseTypeDef(TypedDict):
    Statements: List["StatementDataTypeDef"]


class ListStatementsResponseTypeDef(_RequiredListStatementsResponseTypeDef, total=False):
    NextToken: str


class ListTablesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Tables: List["TableMemberTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class _RequiredStatementDataTypeDef(TypedDict):
    Id: str


class StatementDataTypeDef(_RequiredStatementDataTypeDef, total=False):
    CreatedAt: datetime
    QueryString: str
    SecretArn: str
    StatementName: str
    Status: StatusString
    UpdatedAt: datetime


TableMemberTypeDef = TypedDict(
    "TableMemberTypeDef", {"name": str, "schema": str, "type": str}, total=False
)
