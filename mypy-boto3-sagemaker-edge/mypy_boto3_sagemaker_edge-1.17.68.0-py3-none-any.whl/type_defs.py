"""
Type annotations for sagemaker-edge service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_edge/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_edge.type_defs import EdgeMetricTypeDef

    data: EdgeMetricTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("EdgeMetricTypeDef", "GetDeviceRegistrationResultTypeDef", "ModelTypeDef")


class EdgeMetricTypeDef(TypedDict, total=False):
    Dimension: str
    MetricName: str
    Value: float
    Timestamp: datetime


class GetDeviceRegistrationResultTypeDef(TypedDict, total=False):
    DeviceRegistration: str
    CacheTTL: str


class ModelTypeDef(TypedDict, total=False):
    ModelName: str
    ModelVersion: str
    LatestSampleTime: datetime
    LatestInference: datetime
    ModelMetrics: List["EdgeMetricTypeDef"]
