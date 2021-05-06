"""
Type annotations for codestar-connections service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar_connections/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codestar_connections.type_defs import ConnectionTypeDef

    data: ConnectionTypeDef = {...}
    ```
"""
import sys
from typing import Any, Dict, List

from mypy_boto3_codestar_connections.literals import ConnectionStatus, ProviderType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ConnectionTypeDef",
    "CreateConnectionOutputTypeDef",
    "CreateHostOutputTypeDef",
    "GetConnectionOutputTypeDef",
    "GetHostOutputTypeDef",
    "HostTypeDef",
    "ListConnectionsOutputTypeDef",
    "ListHostsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ResponseMetadata",
    "TagTypeDef",
    "VpcConfigurationTypeDef",
)


class ConnectionTypeDef(TypedDict, total=False):
    ConnectionName: str
    ConnectionArn: str
    ProviderType: ProviderType
    OwnerAccountId: str
    ConnectionStatus: ConnectionStatus
    HostArn: str


class CreateConnectionOutputTypeDef(TypedDict):
    ConnectionArn: str
    Tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class CreateHostOutputTypeDef(TypedDict):
    HostArn: str
    Tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class GetConnectionOutputTypeDef(TypedDict):
    Connection: "ConnectionTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetHostOutputTypeDef(TypedDict):
    Name: str
    Status: str
    ProviderType: ProviderType
    ProviderEndpoint: str
    VpcConfiguration: "VpcConfigurationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class HostTypeDef(TypedDict, total=False):
    Name: str
    HostArn: str
    ProviderType: ProviderType
    ProviderEndpoint: str
    VpcConfiguration: "VpcConfigurationTypeDef"
    Status: str
    StatusMessage: str


class ListConnectionsOutputTypeDef(TypedDict):
    Connections: List["ConnectionTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListHostsOutputTypeDef(TypedDict):
    Hosts: List["HostTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceOutputTypeDef(TypedDict):
    Tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class _RequiredVpcConfigurationTypeDef(TypedDict):
    VpcId: str
    SubnetIds: List[str]
    SecurityGroupIds: List[str]


class VpcConfigurationTypeDef(_RequiredVpcConfigurationTypeDef, total=False):
    TlsCertificate: str
