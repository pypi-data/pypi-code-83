"""
Type annotations for s3outposts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_s3outposts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_s3outposts.type_defs import CreateEndpointResultTypeDef

    data: CreateEndpointResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_s3outposts.literals import EndpointStatus

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateEndpointResultTypeDef",
    "EndpointTypeDef",
    "ListEndpointsResultTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
)


class CreateEndpointResultTypeDef(TypedDict, total=False):
    EndpointArn: str


class EndpointTypeDef(TypedDict, total=False):
    EndpointArn: str
    OutpostsId: str
    CidrBlock: str
    Status: EndpointStatus
    CreationTime: datetime
    NetworkInterfaces: List["NetworkInterfaceTypeDef"]


class ListEndpointsResultTypeDef(TypedDict, total=False):
    Endpoints: List["EndpointTypeDef"]
    NextToken: str


class NetworkInterfaceTypeDef(TypedDict, total=False):
    NetworkInterfaceId: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str
