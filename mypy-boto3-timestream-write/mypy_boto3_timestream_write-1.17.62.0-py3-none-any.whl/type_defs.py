"""
Main interface for timestream-write service type definitions.

Usage::

    ```python
    from mypy_boto3_timestream_write.type_defs import DatabaseTypeDef

    data: DatabaseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_timestream_write.literals import (
    DimensionValueType,
    MeasureValueType,
    TableStatus,
    TimeUnit,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DatabaseTypeDef",
    "DimensionTypeDef",
    "EndpointTypeDef",
    "RetentionPropertiesTypeDef",
    "TableTypeDef",
    "TagTypeDef",
    "CreateDatabaseResponseTypeDef",
    "CreateTableResponseTypeDef",
    "DescribeDatabaseResponseTypeDef",
    "DescribeEndpointsResponseTypeDef",
    "DescribeTableResponseTypeDef",
    "ListDatabasesResponseTypeDef",
    "ListTablesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "RecordTypeDef",
    "UpdateDatabaseResponseTypeDef",
    "UpdateTableResponseTypeDef",
)

DatabaseTypeDef = TypedDict(
    "DatabaseTypeDef",
    {
        "Arn": str,
        "DatabaseName": str,
        "TableCount": int,
        "KmsKeyId": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

_RequiredDimensionTypeDef = TypedDict("_RequiredDimensionTypeDef", {"Name": str, "Value": str})
_OptionalDimensionTypeDef = TypedDict(
    "_OptionalDimensionTypeDef", {"DimensionValueType": DimensionValueType}, total=False
)


class DimensionTypeDef(_RequiredDimensionTypeDef, _OptionalDimensionTypeDef):
    pass


EndpointTypeDef = TypedDict("EndpointTypeDef", {"Address": str, "CachePeriodInMinutes": int})

RetentionPropertiesTypeDef = TypedDict(
    "RetentionPropertiesTypeDef",
    {"MemoryStoreRetentionPeriodInHours": int, "MagneticStoreRetentionPeriodInDays": int},
)

TableTypeDef = TypedDict(
    "TableTypeDef",
    {
        "Arn": str,
        "TableName": str,
        "DatabaseName": str,
        "TableStatus": TableStatus,
        "RetentionProperties": "RetentionPropertiesTypeDef",
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
    },
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

CreateDatabaseResponseTypeDef = TypedDict(
    "CreateDatabaseResponseTypeDef", {"Database": "DatabaseTypeDef"}, total=False
)

CreateTableResponseTypeDef = TypedDict(
    "CreateTableResponseTypeDef", {"Table": "TableTypeDef"}, total=False
)

DescribeDatabaseResponseTypeDef = TypedDict(
    "DescribeDatabaseResponseTypeDef", {"Database": "DatabaseTypeDef"}, total=False
)

DescribeEndpointsResponseTypeDef = TypedDict(
    "DescribeEndpointsResponseTypeDef", {"Endpoints": List["EndpointTypeDef"]}
)

DescribeTableResponseTypeDef = TypedDict(
    "DescribeTableResponseTypeDef", {"Table": "TableTypeDef"}, total=False
)

ListDatabasesResponseTypeDef = TypedDict(
    "ListDatabasesResponseTypeDef",
    {"Databases": List["DatabaseTypeDef"], "NextToken": str},
    total=False,
)

ListTablesResponseTypeDef = TypedDict(
    "ListTablesResponseTypeDef", {"Tables": List["TableTypeDef"], "NextToken": str}, total=False
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": List["TagTypeDef"]}, total=False
)

RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "Dimensions": List["DimensionTypeDef"],
        "MeasureName": str,
        "MeasureValue": str,
        "MeasureValueType": MeasureValueType,
        "Time": str,
        "TimeUnit": TimeUnit,
        "Version": int,
    },
    total=False,
)

UpdateDatabaseResponseTypeDef = TypedDict(
    "UpdateDatabaseResponseTypeDef", {"Database": "DatabaseTypeDef"}, total=False
)

UpdateTableResponseTypeDef = TypedDict(
    "UpdateTableResponseTypeDef", {"Table": "TableTypeDef"}, total=False
)
