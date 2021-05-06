"""
Type annotations for timestream-query service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_query/type_defs.html)

Usage::

    ```python
    from mypy_boto3_timestream_query.type_defs import CancelQueryResponseTypeDef

    data: CancelQueryResponseTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from mypy_boto3_timestream_query.literals import ScalarType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelQueryResponseTypeDef",
    "ColumnInfoTypeDef",
    "DatumTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "EndpointTypeDef",
    "PaginatorConfigTypeDef",
    "QueryResponseTypeDef",
    "QueryStatusTypeDef",
    "RowTypeDef",
    "TimeSeriesDataPointTypeDef",
    "TypeTypeDef",
)


class CancelQueryResponseTypeDef(TypedDict, total=False):
    CancellationMessage: str


_RequiredColumnInfoTypeDef = TypedDict("_RequiredColumnInfoTypeDef", {"Type": Dict[str, Any]})
_OptionalColumnInfoTypeDef = TypedDict("_OptionalColumnInfoTypeDef", {"Name": str}, total=False)


class ColumnInfoTypeDef(_RequiredColumnInfoTypeDef, _OptionalColumnInfoTypeDef):
    pass


class DatumTypeDef(TypedDict, total=False):
    ScalarValue: str
    TimeSeriesValue: List[Dict[str, Any]]
    ArrayValue: List[Dict[str, Any]]
    RowValue: Dict[str, Any]
    NullValue: bool


class DescribeEndpointsResponseTypeDef(TypedDict):
    Endpoints: List["EndpointTypeDef"]


class EndpointTypeDef(TypedDict):
    Address: str
    CachePeriodInMinutes: int


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredQueryResponseTypeDef(TypedDict):
    QueryId: str
    Rows: List["RowTypeDef"]
    ColumnInfo: List["ColumnInfoTypeDef"]


class QueryResponseTypeDef(_RequiredQueryResponseTypeDef, total=False):
    NextToken: str
    QueryStatus: "QueryStatusTypeDef"


class QueryStatusTypeDef(TypedDict, total=False):
    ProgressPercentage: float
    CumulativeBytesScanned: int
    CumulativeBytesMetered: int


class RowTypeDef(TypedDict):
    Data: List[Dict[str, Any]]


class TimeSeriesDataPointTypeDef(TypedDict):
    Time: str
    Value: "DatumTypeDef"


class TypeTypeDef(TypedDict, total=False):
    ScalarType: ScalarType
    ArrayColumnInfo: Dict[str, Any]
    TimeSeriesMeasureValueColumnInfo: Dict[str, Any]
    RowColumnInfo: List[Dict[str, Any]]
