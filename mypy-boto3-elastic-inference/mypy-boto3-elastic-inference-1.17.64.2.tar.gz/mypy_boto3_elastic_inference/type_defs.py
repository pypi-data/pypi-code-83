"""
Type annotations for elastic-inference service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elastic_inference/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elastic_inference.type_defs import AcceleratorTypeOfferingTypeDef

    data: AcceleratorTypeOfferingTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_elastic_inference.literals import LocationType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceleratorTypeOfferingTypeDef",
    "AcceleratorTypeTypeDef",
    "DescribeAcceleratorOfferingsResponseTypeDef",
    "DescribeAcceleratorTypesResponseTypeDef",
    "DescribeAcceleratorsResponseTypeDef",
    "ElasticInferenceAcceleratorHealthTypeDef",
    "ElasticInferenceAcceleratorTypeDef",
    "FilterTypeDef",
    "KeyValuePairTypeDef",
    "ListTagsForResourceResultTypeDef",
    "MemoryInfoTypeDef",
    "PaginatorConfigTypeDef",
)


class AcceleratorTypeOfferingTypeDef(TypedDict, total=False):
    acceleratorType: str
    locationType: LocationType
    location: str


class AcceleratorTypeTypeDef(TypedDict, total=False):
    acceleratorTypeName: str
    memoryInfo: "MemoryInfoTypeDef"
    throughputInfo: List["KeyValuePairTypeDef"]


class DescribeAcceleratorOfferingsResponseTypeDef(TypedDict, total=False):
    acceleratorTypeOfferings: List["AcceleratorTypeOfferingTypeDef"]


class DescribeAcceleratorTypesResponseTypeDef(TypedDict, total=False):
    acceleratorTypes: List["AcceleratorTypeTypeDef"]


class DescribeAcceleratorsResponseTypeDef(TypedDict, total=False):
    acceleratorSet: List["ElasticInferenceAcceleratorTypeDef"]
    nextToken: str


class ElasticInferenceAcceleratorHealthTypeDef(TypedDict, total=False):
    status: str


class ElasticInferenceAcceleratorTypeDef(TypedDict, total=False):
    acceleratorHealth: "ElasticInferenceAcceleratorHealthTypeDef"
    acceleratorType: str
    acceleratorId: str
    availabilityZone: str
    attachedResource: str


class FilterTypeDef(TypedDict, total=False):
    name: str
    values: List[str]


class KeyValuePairTypeDef(TypedDict, total=False):
    key: str
    value: int


class ListTagsForResourceResultTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class MemoryInfoTypeDef(TypedDict, total=False):
    sizeInMiB: int


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str
