"""
Type annotations for forecastquery service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecastquery/type_defs.html)

Usage::

    ```python
    from mypy_boto3_forecastquery.type_defs import DataPointTypeDef

    data: DataPointTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = ("DataPointTypeDef", "ForecastTypeDef", "QueryForecastResponseTypeDef")


class DataPointTypeDef(TypedDict, total=False):
    Timestamp: str
    Value: float


class ForecastTypeDef(TypedDict, total=False):
    Predictions: Dict[str, List["DataPointTypeDef"]]


class QueryForecastResponseTypeDef(TypedDict, total=False):
    Forecast: "ForecastTypeDef"
