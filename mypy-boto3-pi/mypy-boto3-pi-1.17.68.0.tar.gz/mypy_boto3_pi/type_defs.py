"""
Type annotations for pi service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_pi/type_defs.html)

Usage::

    ```python
    from mypy_boto3_pi.type_defs import DataPointTypeDef

    data: DataPointTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DataPointTypeDef",
    "DescribeDimensionKeysResponseTypeDef",
    "DimensionGroupTypeDef",
    "DimensionKeyDescriptionTypeDef",
    "GetResourceMetricsResponseTypeDef",
    "MetricKeyDataPointsTypeDef",
    "MetricQueryTypeDef",
    "ResponsePartitionKeyTypeDef",
    "ResponseResourceMetricKeyTypeDef",
)


class DataPointTypeDef(TypedDict):
    Timestamp: datetime
    Value: float


class DescribeDimensionKeysResponseTypeDef(TypedDict, total=False):
    AlignedStartTime: datetime
    AlignedEndTime: datetime
    PartitionKeys: List["ResponsePartitionKeyTypeDef"]
    Keys: List["DimensionKeyDescriptionTypeDef"]
    NextToken: str


class _RequiredDimensionGroupTypeDef(TypedDict):
    Group: str


class DimensionGroupTypeDef(_RequiredDimensionGroupTypeDef, total=False):
    Dimensions: List[str]
    Limit: int


class DimensionKeyDescriptionTypeDef(TypedDict, total=False):
    Dimensions: Dict[str, str]
    Total: float
    Partitions: List[float]


class GetResourceMetricsResponseTypeDef(TypedDict, total=False):
    AlignedStartTime: datetime
    AlignedEndTime: datetime
    Identifier: str
    MetricList: List["MetricKeyDataPointsTypeDef"]
    NextToken: str


class MetricKeyDataPointsTypeDef(TypedDict, total=False):
    Key: "ResponseResourceMetricKeyTypeDef"
    DataPoints: List["DataPointTypeDef"]


class _RequiredMetricQueryTypeDef(TypedDict):
    Metric: str


class MetricQueryTypeDef(_RequiredMetricQueryTypeDef, total=False):
    GroupBy: "DimensionGroupTypeDef"
    Filter: Dict[str, str]


class ResponsePartitionKeyTypeDef(TypedDict):
    Dimensions: Dict[str, str]


class _RequiredResponseResourceMetricKeyTypeDef(TypedDict):
    Metric: str


class ResponseResourceMetricKeyTypeDef(_RequiredResponseResourceMetricKeyTypeDef, total=False):
    Dimensions: Dict[str, str]
