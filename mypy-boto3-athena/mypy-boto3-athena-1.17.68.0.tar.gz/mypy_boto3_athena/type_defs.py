"""
Type annotations for athena service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/type_defs.html)

Usage::

    ```python
    from mypy_boto3_athena.type_defs import BatchGetNamedQueryOutputTypeDef

    data: BatchGetNamedQueryOutputTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_athena.literals import (
    ColumnNullable,
    DataCatalogType,
    EncryptionOption,
    QueryExecutionState,
    StatementType,
    WorkGroupState,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchGetNamedQueryOutputTypeDef",
    "BatchGetQueryExecutionOutputTypeDef",
    "ColumnInfoTypeDef",
    "ColumnTypeDef",
    "CreateNamedQueryOutputTypeDef",
    "DataCatalogSummaryTypeDef",
    "DataCatalogTypeDef",
    "DatabaseTypeDef",
    "DatumTypeDef",
    "EncryptionConfigurationTypeDef",
    "EngineVersionTypeDef",
    "GetDataCatalogOutputTypeDef",
    "GetDatabaseOutputTypeDef",
    "GetNamedQueryOutputTypeDef",
    "GetPreparedStatementOutputTypeDef",
    "GetQueryExecutionOutputTypeDef",
    "GetQueryResultsOutputTypeDef",
    "GetTableMetadataOutputTypeDef",
    "GetWorkGroupOutputTypeDef",
    "ListDataCatalogsOutputTypeDef",
    "ListDatabasesOutputTypeDef",
    "ListEngineVersionsOutputTypeDef",
    "ListNamedQueriesOutputTypeDef",
    "ListPreparedStatementsOutputTypeDef",
    "ListQueryExecutionsOutputTypeDef",
    "ListTableMetadataOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListWorkGroupsOutputTypeDef",
    "NamedQueryTypeDef",
    "PaginatorConfigTypeDef",
    "PreparedStatementSummaryTypeDef",
    "PreparedStatementTypeDef",
    "QueryExecutionContextTypeDef",
    "QueryExecutionStatisticsTypeDef",
    "QueryExecutionStatusTypeDef",
    "QueryExecutionTypeDef",
    "ResponseMetadata",
    "ResultConfigurationTypeDef",
    "ResultConfigurationUpdatesTypeDef",
    "ResultSetMetadataTypeDef",
    "ResultSetTypeDef",
    "RowTypeDef",
    "StartQueryExecutionOutputTypeDef",
    "TableMetadataTypeDef",
    "TagTypeDef",
    "UnprocessedNamedQueryIdTypeDef",
    "UnprocessedQueryExecutionIdTypeDef",
    "WorkGroupConfigurationTypeDef",
    "WorkGroupConfigurationUpdatesTypeDef",
    "WorkGroupSummaryTypeDef",
    "WorkGroupTypeDef",
)


class BatchGetNamedQueryOutputTypeDef(TypedDict):
    NamedQueries: List["NamedQueryTypeDef"]
    UnprocessedNamedQueryIds: List["UnprocessedNamedQueryIdTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class BatchGetQueryExecutionOutputTypeDef(TypedDict):
    QueryExecutions: List["QueryExecutionTypeDef"]
    UnprocessedQueryExecutionIds: List["UnprocessedQueryExecutionIdTypeDef"]
    ResponseMetadata: "ResponseMetadata"


_RequiredColumnInfoTypeDef = TypedDict("_RequiredColumnInfoTypeDef", {"Name": str, "Type": str})
_OptionalColumnInfoTypeDef = TypedDict(
    "_OptionalColumnInfoTypeDef",
    {
        "CatalogName": str,
        "SchemaName": str,
        "TableName": str,
        "Label": str,
        "Precision": int,
        "Scale": int,
        "Nullable": ColumnNullable,
        "CaseSensitive": bool,
    },
    total=False,
)


class ColumnInfoTypeDef(_RequiredColumnInfoTypeDef, _OptionalColumnInfoTypeDef):
    pass


_RequiredColumnTypeDef = TypedDict("_RequiredColumnTypeDef", {"Name": str})
_OptionalColumnTypeDef = TypedDict(
    "_OptionalColumnTypeDef", {"Type": str, "Comment": str}, total=False
)


class ColumnTypeDef(_RequiredColumnTypeDef, _OptionalColumnTypeDef):
    pass


class CreateNamedQueryOutputTypeDef(TypedDict):
    NamedQueryId: str
    ResponseMetadata: "ResponseMetadata"


DataCatalogSummaryTypeDef = TypedDict(
    "DataCatalogSummaryTypeDef", {"CatalogName": str, "Type": DataCatalogType}, total=False
)

_RequiredDataCatalogTypeDef = TypedDict(
    "_RequiredDataCatalogTypeDef", {"Name": str, "Type": DataCatalogType}
)
_OptionalDataCatalogTypeDef = TypedDict(
    "_OptionalDataCatalogTypeDef", {"Description": str, "Parameters": Dict[str, str]}, total=False
)


class DataCatalogTypeDef(_RequiredDataCatalogTypeDef, _OptionalDataCatalogTypeDef):
    pass


class _RequiredDatabaseTypeDef(TypedDict):
    Name: str


class DatabaseTypeDef(_RequiredDatabaseTypeDef, total=False):
    Description: str
    Parameters: Dict[str, str]


class DatumTypeDef(TypedDict, total=False):
    VarCharValue: str


class _RequiredEncryptionConfigurationTypeDef(TypedDict):
    EncryptionOption: EncryptionOption


class EncryptionConfigurationTypeDef(_RequiredEncryptionConfigurationTypeDef, total=False):
    KmsKey: str


class EngineVersionTypeDef(TypedDict, total=False):
    SelectedEngineVersion: str
    EffectiveEngineVersion: str


class GetDataCatalogOutputTypeDef(TypedDict):
    DataCatalog: "DataCatalogTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetDatabaseOutputTypeDef(TypedDict):
    Database: "DatabaseTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetNamedQueryOutputTypeDef(TypedDict):
    NamedQuery: "NamedQueryTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetPreparedStatementOutputTypeDef(TypedDict):
    PreparedStatement: "PreparedStatementTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetQueryExecutionOutputTypeDef(TypedDict):
    QueryExecution: "QueryExecutionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetQueryResultsOutputTypeDef(TypedDict):
    UpdateCount: int
    ResultSet: "ResultSetTypeDef"
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class GetTableMetadataOutputTypeDef(TypedDict):
    TableMetadata: "TableMetadataTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetWorkGroupOutputTypeDef(TypedDict):
    WorkGroup: "WorkGroupTypeDef"
    ResponseMetadata: "ResponseMetadata"


class ListDataCatalogsOutputTypeDef(TypedDict):
    DataCatalogsSummary: List["DataCatalogSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListDatabasesOutputTypeDef(TypedDict):
    DatabaseList: List["DatabaseTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListEngineVersionsOutputTypeDef(TypedDict):
    EngineVersions: List["EngineVersionTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListNamedQueriesOutputTypeDef(TypedDict):
    NamedQueryIds: List[str]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListPreparedStatementsOutputTypeDef(TypedDict):
    PreparedStatements: List["PreparedStatementSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListQueryExecutionsOutputTypeDef(TypedDict):
    QueryExecutionIds: List[str]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTableMetadataOutputTypeDef(TypedDict):
    TableMetadataList: List["TableMetadataTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: List["TagTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListWorkGroupsOutputTypeDef(TypedDict):
    WorkGroups: List["WorkGroupSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredNamedQueryTypeDef(TypedDict):
    Name: str
    Database: str
    QueryString: str


class NamedQueryTypeDef(_RequiredNamedQueryTypeDef, total=False):
    Description: str
    NamedQueryId: str
    WorkGroup: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PreparedStatementSummaryTypeDef(TypedDict, total=False):
    StatementName: str
    LastModifiedTime: datetime


class PreparedStatementTypeDef(TypedDict, total=False):
    StatementName: str
    QueryStatement: str
    WorkGroupName: str
    Description: str
    LastModifiedTime: datetime


class QueryExecutionContextTypeDef(TypedDict, total=False):
    Database: str
    Catalog: str


class QueryExecutionStatisticsTypeDef(TypedDict, total=False):
    EngineExecutionTimeInMillis: int
    DataScannedInBytes: int
    DataManifestLocation: str
    TotalExecutionTimeInMillis: int
    QueryQueueTimeInMillis: int
    QueryPlanningTimeInMillis: int
    ServiceProcessingTimeInMillis: int


class QueryExecutionStatusTypeDef(TypedDict, total=False):
    State: QueryExecutionState
    StateChangeReason: str
    SubmissionDateTime: datetime
    CompletionDateTime: datetime


class QueryExecutionTypeDef(TypedDict, total=False):
    QueryExecutionId: str
    Query: str
    StatementType: StatementType
    ResultConfiguration: "ResultConfigurationTypeDef"
    QueryExecutionContext: "QueryExecutionContextTypeDef"
    Status: "QueryExecutionStatusTypeDef"
    Statistics: "QueryExecutionStatisticsTypeDef"
    WorkGroup: str
    EngineVersion: "EngineVersionTypeDef"


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class ResultConfigurationTypeDef(TypedDict, total=False):
    OutputLocation: str
    EncryptionConfiguration: "EncryptionConfigurationTypeDef"


class ResultConfigurationUpdatesTypeDef(TypedDict, total=False):
    OutputLocation: str
    RemoveOutputLocation: bool
    EncryptionConfiguration: "EncryptionConfigurationTypeDef"
    RemoveEncryptionConfiguration: bool


class ResultSetMetadataTypeDef(TypedDict, total=False):
    ColumnInfo: List["ColumnInfoTypeDef"]


class ResultSetTypeDef(TypedDict, total=False):
    Rows: List["RowTypeDef"]
    ResultSetMetadata: "ResultSetMetadataTypeDef"


class RowTypeDef(TypedDict, total=False):
    Data: List["DatumTypeDef"]


class StartQueryExecutionOutputTypeDef(TypedDict):
    QueryExecutionId: str
    ResponseMetadata: "ResponseMetadata"


class _RequiredTableMetadataTypeDef(TypedDict):
    Name: str


class TableMetadataTypeDef(_RequiredTableMetadataTypeDef, total=False):
    CreateTime: datetime
    LastAccessTime: datetime
    TableType: str
    Columns: List["ColumnTypeDef"]
    PartitionKeys: List["ColumnTypeDef"]
    Parameters: Dict[str, str]


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class UnprocessedNamedQueryIdTypeDef(TypedDict, total=False):
    NamedQueryId: str
    ErrorCode: str
    ErrorMessage: str


class UnprocessedQueryExecutionIdTypeDef(TypedDict, total=False):
    QueryExecutionId: str
    ErrorCode: str
    ErrorMessage: str


class WorkGroupConfigurationTypeDef(TypedDict, total=False):
    ResultConfiguration: "ResultConfigurationTypeDef"
    EnforceWorkGroupConfiguration: bool
    PublishCloudWatchMetricsEnabled: bool
    BytesScannedCutoffPerQuery: int
    RequesterPaysEnabled: bool
    EngineVersion: "EngineVersionTypeDef"


class WorkGroupConfigurationUpdatesTypeDef(TypedDict, total=False):
    EnforceWorkGroupConfiguration: bool
    ResultConfigurationUpdates: "ResultConfigurationUpdatesTypeDef"
    PublishCloudWatchMetricsEnabled: bool
    BytesScannedCutoffPerQuery: int
    RemoveBytesScannedCutoffPerQuery: bool
    RequesterPaysEnabled: bool
    EngineVersion: "EngineVersionTypeDef"


class WorkGroupSummaryTypeDef(TypedDict, total=False):
    Name: str
    State: WorkGroupState
    Description: str
    CreationTime: datetime
    EngineVersion: "EngineVersionTypeDef"


class _RequiredWorkGroupTypeDef(TypedDict):
    Name: str


class WorkGroupTypeDef(_RequiredWorkGroupTypeDef, total=False):
    State: WorkGroupState
    Configuration: "WorkGroupConfigurationTypeDef"
    Description: str
    CreationTime: datetime
