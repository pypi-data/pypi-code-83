"""
Type annotations for kinesisvideo service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kinesisvideo.type_defs import ChannelInfoTypeDef

    data: ChannelInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_kinesisvideo.literals import ChannelProtocol, ChannelRole, Status

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ChannelInfoTypeDef",
    "ChannelNameConditionTypeDef",
    "CreateSignalingChannelOutputTypeDef",
    "CreateStreamOutputTypeDef",
    "DescribeSignalingChannelOutputTypeDef",
    "DescribeStreamOutputTypeDef",
    "GetDataEndpointOutputTypeDef",
    "GetSignalingChannelEndpointOutputTypeDef",
    "ListSignalingChannelsOutputTypeDef",
    "ListStreamsOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTagsForStreamOutputTypeDef",
    "PaginatorConfigTypeDef",
    "ResourceEndpointListItemTypeDef",
    "ResponseMetadata",
    "SingleMasterChannelEndpointConfigurationTypeDef",
    "SingleMasterConfigurationTypeDef",
    "StreamInfoTypeDef",
    "StreamNameConditionTypeDef",
    "TagTypeDef",
)


class ChannelInfoTypeDef(TypedDict, total=False):
    ChannelName: str
    ChannelARN: str
    ChannelType: Literal["SINGLE_MASTER"]
    ChannelStatus: Status
    CreationTime: datetime
    SingleMasterConfiguration: "SingleMasterConfigurationTypeDef"
    Version: str


class ChannelNameConditionTypeDef(TypedDict, total=False):
    ComparisonOperator: Literal["BEGINS_WITH"]
    ComparisonValue: str


class CreateSignalingChannelOutputTypeDef(TypedDict):
    ChannelARN: str
    ResponseMetadata: "ResponseMetadata"


class CreateStreamOutputTypeDef(TypedDict):
    StreamARN: str
    ResponseMetadata: "ResponseMetadata"


class DescribeSignalingChannelOutputTypeDef(TypedDict):
    ChannelInfo: "ChannelInfoTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeStreamOutputTypeDef(TypedDict):
    StreamInfo: "StreamInfoTypeDef"
    ResponseMetadata: "ResponseMetadata"


class GetDataEndpointOutputTypeDef(TypedDict):
    DataEndpoint: str
    ResponseMetadata: "ResponseMetadata"


class GetSignalingChannelEndpointOutputTypeDef(TypedDict):
    ResourceEndpointList: List["ResourceEndpointListItemTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListSignalingChannelsOutputTypeDef(TypedDict):
    ChannelInfoList: List["ChannelInfoTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListStreamsOutputTypeDef(TypedDict):
    StreamInfoList: List["StreamInfoTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagsForResourceOutputTypeDef(TypedDict):
    NextToken: str
    Tags: Dict[str, str]
    ResponseMetadata: "ResponseMetadata"


class ListTagsForStreamOutputTypeDef(TypedDict):
    NextToken: str
    Tags: Dict[str, str]
    ResponseMetadata: "ResponseMetadata"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


ResourceEndpointListItemTypeDef = TypedDict(
    "ResourceEndpointListItemTypeDef",
    {"Protocol": ChannelProtocol, "ResourceEndpoint": str},
    total=False,
)


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class SingleMasterChannelEndpointConfigurationTypeDef(TypedDict, total=False):
    Protocols: List[ChannelProtocol]
    Role: ChannelRole


class SingleMasterConfigurationTypeDef(TypedDict, total=False):
    MessageTtlSeconds: int


class StreamInfoTypeDef(TypedDict, total=False):
    DeviceName: str
    StreamName: str
    StreamARN: str
    MediaType: str
    KmsKeyId: str
    Version: str
    Status: Status
    CreationTime: datetime
    DataRetentionInHours: int


class StreamNameConditionTypeDef(TypedDict, total=False):
    ComparisonOperator: Literal["BEGINS_WITH"]
    ComparisonValue: str


class TagTypeDef(TypedDict):
    Key: str
    Value: str
