"""
Type annotations for athena service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_athena/literals.html)

Usage::

    ```python
    from mypy_boto3_athena.literals import ColumnNullable

    data: ColumnNullable = "NOT_NULL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ColumnNullable",
    "DataCatalogType",
    "EncryptionOption",
    "GetQueryResultsPaginatorName",
    "ListDataCatalogsPaginatorName",
    "ListDatabasesPaginatorName",
    "ListNamedQueriesPaginatorName",
    "ListQueryExecutionsPaginatorName",
    "ListTableMetadataPaginatorName",
    "ListTagsForResourcePaginatorName",
    "QueryExecutionState",
    "StatementType",
    "WorkGroupState",
)


ColumnNullable = Literal["NOT_NULL", "NULLABLE", "UNKNOWN"]
DataCatalogType = Literal["GLUE", "HIVE", "LAMBDA"]
EncryptionOption = Literal["CSE_KMS", "SSE_KMS", "SSE_S3"]
GetQueryResultsPaginatorName = Literal["get_query_results"]
ListDataCatalogsPaginatorName = Literal["list_data_catalogs"]
ListDatabasesPaginatorName = Literal["list_databases"]
ListNamedQueriesPaginatorName = Literal["list_named_queries"]
ListQueryExecutionsPaginatorName = Literal["list_query_executions"]
ListTableMetadataPaginatorName = Literal["list_table_metadata"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
QueryExecutionState = Literal["CANCELLED", "FAILED", "QUEUED", "RUNNING", "SUCCEEDED"]
StatementType = Literal["DDL", "DML", "UTILITY"]
WorkGroupState = Literal["DISABLED", "ENABLED"]
