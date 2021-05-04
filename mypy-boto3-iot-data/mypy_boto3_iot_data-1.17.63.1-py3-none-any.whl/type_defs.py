"""
Type annotations for iot-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iot_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iot_data.type_defs import DeleteThingShadowResponseTypeDef

    data: DeleteThingShadowResponseTypeDef = {...}
    ```
"""
import sys
from typing import IO, List, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "DeleteThingShadowResponseTypeDef",
    "GetThingShadowResponseTypeDef",
    "ListNamedShadowsForThingResponseTypeDef",
    "UpdateThingShadowResponseTypeDef",
)


class DeleteThingShadowResponseTypeDef(TypedDict):
    payload: Union[bytes, IO[bytes]]


class GetThingShadowResponseTypeDef(TypedDict, total=False):
    payload: Union[bytes, IO[bytes]]


class ListNamedShadowsForThingResponseTypeDef(TypedDict, total=False):
    results: List[str]
    nextToken: str
    timestamp: int


class UpdateThingShadowResponseTypeDef(TypedDict, total=False):
    payload: Union[bytes, IO[bytes]]
