"""
Type annotations for timestream-write service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_timestream_write/type_defs.html)

Usage::

    ```python
    from mypy_boto3_timestream_write.type_defs import CreateDatabaseResponseTypeDef

    data: CreateDatabaseResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_timestream_write.literals import MeasureValueType, TableStatus, TimeUnit

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateDatabaseResponseTypeDef",
    "CreateTableResponseTypeDef",
    "DatabaseTypeDef",
    "DescribeDatabaseResponseTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeTableResponseTypeDef",
    "DimensionTypeDef",
    "EndpointTypeDef",
    "ListDatabasesResponseTypeDef",
    "ListTablesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RecordTypeDef",
    "RetentionPropertiesTypeDef",
    "TableTypeDef",
    "TagTypeDef",
    "UpdateDatabaseResponseTypeDef",
    "UpdateTableResponseTypeDef",
)


class CreateDatabaseResponseTypeDef(TypedDict, total=False):
    Database: "DatabaseTypeDef"


class CreateTableResponseTypeDef(TypedDict, total=False):
    Table: "TableTypeDef"


class DatabaseTypeDef(TypedDict, total=False):
    Arn: str
    DatabaseName: str
    TableCount: int
    KmsKeyId: str
    CreationTime: datetime
    LastUpdatedTime: datetime


class DescribeDatabaseResponseTypeDef(TypedDict, total=False):
    Database: "DatabaseTypeDef"


class DescribeEndpointsResponseTypeDef(TypedDict):
    Endpoints: List["EndpointTypeDef"]


class DescribeTableResponseTypeDef(TypedDict, total=False):
    Table: "TableTypeDef"


class _RequiredDimensionTypeDef(TypedDict):
    Name: str
    Value: str


class DimensionTypeDef(_RequiredDimensionTypeDef, total=False):
    DimensionValueType: Literal["VARCHAR"]


class EndpointTypeDef(TypedDict):
    Address: str
    CachePeriodInMinutes: int


class ListDatabasesResponseTypeDef(TypedDict, total=False):
    Databases: List["DatabaseTypeDef"]
    NextToken: str


class ListTablesResponseTypeDef(TypedDict, total=False):
    Tables: List["TableTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class RecordTypeDef(TypedDict, total=False):
    Dimensions: List["DimensionTypeDef"]
    MeasureName: str
    MeasureValue: str
    MeasureValueType: MeasureValueType
    Time: str
    TimeUnit: TimeUnit
    Version: int


class RetentionPropertiesTypeDef(TypedDict):
    MemoryStoreRetentionPeriodInHours: int
    MagneticStoreRetentionPeriodInDays: int


class TableTypeDef(TypedDict, total=False):
    Arn: str
    TableName: str
    DatabaseName: str
    TableStatus: TableStatus
    RetentionProperties: "RetentionPropertiesTypeDef"
    CreationTime: datetime
    LastUpdatedTime: datetime


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class UpdateDatabaseResponseTypeDef(TypedDict, total=False):
    Database: "DatabaseTypeDef"


class UpdateTableResponseTypeDef(TypedDict, total=False):
    Table: "TableTypeDef"
