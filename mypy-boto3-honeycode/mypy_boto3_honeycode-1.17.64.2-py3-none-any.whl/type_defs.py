"""
Type annotations for honeycode service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_honeycode/type_defs.html)

Usage::

    ```python
    from mypy_boto3_honeycode.type_defs import BatchCreateTableRowsResultTypeDef

    data: BatchCreateTableRowsResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_honeycode.literals import (
    Format,
    ImportDataCharacterEncoding,
    TableDataImportJobStatus,
    UpsertAction,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchCreateTableRowsResultTypeDef",
    "BatchDeleteTableRowsResultTypeDef",
    "BatchUpdateTableRowsResultTypeDef",
    "BatchUpsertTableRowsResultTypeDef",
    "CellInputTypeDef",
    "CellTypeDef",
    "ColumnMetadataTypeDef",
    "CreateRowDataTypeDef",
    "DataItemTypeDef",
    "DelimitedTextImportOptionsTypeDef",
    "DescribeTableDataImportJobResultTypeDef",
    "DestinationOptionsTypeDef",
    "FailedBatchItemTypeDef",
    "FilterTypeDef",
    "GetScreenDataResultTypeDef",
    "ImportDataSourceConfigTypeDef",
    "ImportDataSourceTypeDef",
    "ImportJobSubmitterTypeDef",
    "ImportOptionsTypeDef",
    "InvokeScreenAutomationResultTypeDef",
    "ListTableColumnsResultTypeDef",
    "ListTableRowsResultTypeDef",
    "ListTablesResultTypeDef",
    "PaginatorConfigTypeDef",
    "QueryTableRowsResultTypeDef",
    "ResultRowTypeDef",
    "ResultSetTypeDef",
    "SourceDataColumnPropertiesTypeDef",
    "StartTableDataImportJobResultTypeDef",
    "TableColumnTypeDef",
    "TableDataImportJobMetadataTypeDef",
    "TableRowTypeDef",
    "TableTypeDef",
    "UpdateRowDataTypeDef",
    "UpsertRowDataTypeDef",
    "UpsertRowsResultTypeDef",
    "VariableValueTypeDef",
)


class _RequiredBatchCreateTableRowsResultTypeDef(TypedDict):
    workbookCursor: int
    createdRows: Dict[str, str]


class BatchCreateTableRowsResultTypeDef(_RequiredBatchCreateTableRowsResultTypeDef, total=False):
    failedBatchItems: List["FailedBatchItemTypeDef"]


class _RequiredBatchDeleteTableRowsResultTypeDef(TypedDict):
    workbookCursor: int


class BatchDeleteTableRowsResultTypeDef(_RequiredBatchDeleteTableRowsResultTypeDef, total=False):
    failedBatchItems: List["FailedBatchItemTypeDef"]


class _RequiredBatchUpdateTableRowsResultTypeDef(TypedDict):
    workbookCursor: int


class BatchUpdateTableRowsResultTypeDef(_RequiredBatchUpdateTableRowsResultTypeDef, total=False):
    failedBatchItems: List["FailedBatchItemTypeDef"]


class _RequiredBatchUpsertTableRowsResultTypeDef(TypedDict):
    rows: Dict[str, "UpsertRowsResultTypeDef"]
    workbookCursor: int


class BatchUpsertTableRowsResultTypeDef(_RequiredBatchUpsertTableRowsResultTypeDef, total=False):
    failedBatchItems: List["FailedBatchItemTypeDef"]


class CellInputTypeDef(TypedDict, total=False):
    fact: str


CellTypeDef = TypedDict(
    "CellTypeDef",
    {"formula": str, "format": Format, "rawValue": str, "formattedValue": str},
    total=False,
)

ColumnMetadataTypeDef = TypedDict("ColumnMetadataTypeDef", {"name": str, "format": Format})


class CreateRowDataTypeDef(TypedDict):
    batchItemId: str
    cellsToCreate: Dict[str, "CellInputTypeDef"]


class DataItemTypeDef(TypedDict, total=False):
    overrideFormat: Format
    rawValue: str
    formattedValue: str


class _RequiredDelimitedTextImportOptionsTypeDef(TypedDict):
    delimiter: str


class DelimitedTextImportOptionsTypeDef(_RequiredDelimitedTextImportOptionsTypeDef, total=False):
    hasHeaderRow: bool
    ignoreEmptyRows: bool
    dataCharacterEncoding: ImportDataCharacterEncoding


class DescribeTableDataImportJobResultTypeDef(TypedDict):
    jobStatus: TableDataImportJobStatus
    message: str
    jobMetadata: "TableDataImportJobMetadataTypeDef"


class DestinationOptionsTypeDef(TypedDict, total=False):
    columnMap: Dict[str, "SourceDataColumnPropertiesTypeDef"]


FailedBatchItemTypeDef = TypedDict("FailedBatchItemTypeDef", {"id": str, "errorMessage": str})


class _RequiredFilterTypeDef(TypedDict):
    formula: str


class FilterTypeDef(_RequiredFilterTypeDef, total=False):
    contextRowId: str


class _RequiredGetScreenDataResultTypeDef(TypedDict):
    results: Dict[str, "ResultSetTypeDef"]
    workbookCursor: int


class GetScreenDataResultTypeDef(_RequiredGetScreenDataResultTypeDef, total=False):
    nextToken: str


class ImportDataSourceConfigTypeDef(TypedDict, total=False):
    dataSourceUrl: str


class ImportDataSourceTypeDef(TypedDict):
    dataSourceConfig: "ImportDataSourceConfigTypeDef"


class ImportJobSubmitterTypeDef(TypedDict, total=False):
    email: str
    userArn: str


class ImportOptionsTypeDef(TypedDict, total=False):
    destinationOptions: "DestinationOptionsTypeDef"
    delimitedTextOptions: "DelimitedTextImportOptionsTypeDef"


class InvokeScreenAutomationResultTypeDef(TypedDict):
    workbookCursor: int


class _RequiredListTableColumnsResultTypeDef(TypedDict):
    tableColumns: List["TableColumnTypeDef"]


class ListTableColumnsResultTypeDef(_RequiredListTableColumnsResultTypeDef, total=False):
    nextToken: str
    workbookCursor: int


class _RequiredListTableRowsResultTypeDef(TypedDict):
    columnIds: List[str]
    rows: List["TableRowTypeDef"]
    workbookCursor: int


class ListTableRowsResultTypeDef(_RequiredListTableRowsResultTypeDef, total=False):
    rowIdsNotFound: List[str]
    nextToken: str


class _RequiredListTablesResultTypeDef(TypedDict):
    tables: List["TableTypeDef"]


class ListTablesResultTypeDef(_RequiredListTablesResultTypeDef, total=False):
    nextToken: str
    workbookCursor: int


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredQueryTableRowsResultTypeDef(TypedDict):
    columnIds: List[str]
    rows: List["TableRowTypeDef"]
    workbookCursor: int


class QueryTableRowsResultTypeDef(_RequiredQueryTableRowsResultTypeDef, total=False):
    nextToken: str


class _RequiredResultRowTypeDef(TypedDict):
    dataItems: List["DataItemTypeDef"]


class ResultRowTypeDef(_RequiredResultRowTypeDef, total=False):
    rowId: str


class ResultSetTypeDef(TypedDict):
    headers: List["ColumnMetadataTypeDef"]
    rows: List["ResultRowTypeDef"]


class SourceDataColumnPropertiesTypeDef(TypedDict, total=False):
    columnIndex: int


class StartTableDataImportJobResultTypeDef(TypedDict):
    jobId: str
    jobStatus: TableDataImportJobStatus


TableColumnTypeDef = TypedDict(
    "TableColumnTypeDef",
    {"tableColumnId": str, "tableColumnName": str, "format": Format},
    total=False,
)


class TableDataImportJobMetadataTypeDef(TypedDict):
    submitter: "ImportJobSubmitterTypeDef"
    submitTime: datetime
    importOptions: "ImportOptionsTypeDef"
    dataSource: "ImportDataSourceTypeDef"


class TableRowTypeDef(TypedDict):
    rowId: str
    cells: List["CellTypeDef"]


class TableTypeDef(TypedDict, total=False):
    tableId: str
    tableName: str


class UpdateRowDataTypeDef(TypedDict):
    rowId: str
    cellsToUpdate: Dict[str, "CellInputTypeDef"]


UpsertRowDataTypeDef = TypedDict(
    "UpsertRowDataTypeDef",
    {"batchItemId": str, "filter": "FilterTypeDef", "cellsToUpdate": Dict[str, "CellInputTypeDef"]},
)


class UpsertRowsResultTypeDef(TypedDict):
    rowIds: List[str]
    upsertAction: UpsertAction


class VariableValueTypeDef(TypedDict):
    rawValue: str
