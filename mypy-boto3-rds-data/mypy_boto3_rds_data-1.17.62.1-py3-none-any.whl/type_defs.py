"""
Type annotations for rds-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_rds_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_rds_data.type_defs import ArrayValueTypeDef

    data: ArrayValueTypeDef = {...}
    ```
"""
import sys
from typing import IO, Any, Dict, List, Union

from mypy_boto3_rds_data.literals import DecimalReturnType, TypeHint

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ArrayValueTypeDef",
    "BatchExecuteStatementResponseTypeDef",
    "BeginTransactionResponseTypeDef",
    "ColumnMetadataTypeDef",
    "CommitTransactionResponseTypeDef",
    "ExecuteSqlResponseTypeDef",
    "ExecuteStatementResponseTypeDef",
    "FieldTypeDef",
    "RecordTypeDef",
    "ResultFrameTypeDef",
    "ResultSetMetadataTypeDef",
    "ResultSetOptionsTypeDef",
    "RollbackTransactionResponseTypeDef",
    "SqlParameterTypeDef",
    "SqlStatementResultTypeDef",
    "StructValueTypeDef",
    "UpdateResultTypeDef",
    "ValueTypeDef",
)


class ArrayValueTypeDef(TypedDict, total=False):
    arrayValues: List[Dict[str, Any]]
    booleanValues: List[bool]
    doubleValues: List[float]
    longValues: List[int]
    stringValues: List[str]


class BatchExecuteStatementResponseTypeDef(TypedDict, total=False):
    updateResults: List["UpdateResultTypeDef"]


class BeginTransactionResponseTypeDef(TypedDict, total=False):
    transactionId: str


ColumnMetadataTypeDef = TypedDict(
    "ColumnMetadataTypeDef",
    {
        "arrayBaseColumnType": int,
        "isAutoIncrement": bool,
        "isCaseSensitive": bool,
        "isCurrency": bool,
        "isSigned": bool,
        "label": str,
        "name": str,
        "nullable": int,
        "precision": int,
        "scale": int,
        "schemaName": str,
        "tableName": str,
        "type": int,
        "typeName": str,
    },
    total=False,
)


class CommitTransactionResponseTypeDef(TypedDict, total=False):
    transactionStatus: str


class ExecuteSqlResponseTypeDef(TypedDict, total=False):
    sqlStatementResults: List["SqlStatementResultTypeDef"]


class ExecuteStatementResponseTypeDef(TypedDict, total=False):
    columnMetadata: List["ColumnMetadataTypeDef"]
    generatedFields: List["FieldTypeDef"]
    numberOfRecordsUpdated: int
    records: List[List["FieldTypeDef"]]


class FieldTypeDef(TypedDict, total=False):
    arrayValue: "ArrayValueTypeDef"
    blobValue: Union[bytes, IO[bytes]]
    booleanValue: bool
    doubleValue: float
    isNull: bool
    longValue: int
    stringValue: str


class RecordTypeDef(TypedDict, total=False):
    values: List["ValueTypeDef"]


class ResultFrameTypeDef(TypedDict, total=False):
    records: List["RecordTypeDef"]
    resultSetMetadata: "ResultSetMetadataTypeDef"


class ResultSetMetadataTypeDef(TypedDict, total=False):
    columnCount: int
    columnMetadata: List["ColumnMetadataTypeDef"]


class ResultSetOptionsTypeDef(TypedDict, total=False):
    decimalReturnType: DecimalReturnType


class RollbackTransactionResponseTypeDef(TypedDict, total=False):
    transactionStatus: str


class SqlParameterTypeDef(TypedDict, total=False):
    name: str
    typeHint: TypeHint
    value: "FieldTypeDef"


class SqlStatementResultTypeDef(TypedDict, total=False):
    numberOfRecordsUpdated: int
    resultFrame: "ResultFrameTypeDef"


class StructValueTypeDef(TypedDict, total=False):
    attributes: List[Dict[str, Any]]


class UpdateResultTypeDef(TypedDict, total=False):
    generatedFields: List["FieldTypeDef"]


class ValueTypeDef(TypedDict, total=False):
    arrayValues: List[Dict[str, Any]]
    bigIntValue: int
    bitValue: bool
    blobValue: Union[bytes, IO[bytes]]
    doubleValue: float
    intValue: int
    isNull: bool
    realValue: float
    stringValue: str
    structValue: Dict[str, Any]
