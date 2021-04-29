"""
Main interface for kinesisvideo service type definitions.

Usage::

    ```python
    from mypy_boto3_kinesisvideo.type_defs import ChannelInfoTypeDef

    data: ChannelInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_kinesisvideo.literals import (
    ChannelProtocol,
    ChannelRole,
    ChannelType,
    ComparisonOperator,
    Status,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ChannelInfoTypeDef",
    "ResourceEndpointListItemTypeDef",
    "ResponseMetadata",
    "SingleMasterConfigurationTypeDef",
    "StreamInfoTypeDef",
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
    "SingleMasterChannelEndpointConfigurationTypeDef",
    "StreamNameConditionTypeDef",
    "TagTypeDef",
)

ChannelInfoTypeDef = TypedDict(
    "ChannelInfoTypeDef",
    {
        "ChannelName": str,
        "ChannelARN": str,
        "ChannelType": ChannelType,
        "ChannelStatus": Status,
        "CreationTime": datetime,
        "SingleMasterConfiguration": "SingleMasterConfigurationTypeDef",
        "Version": str,
    },
    total=False,
)

ResourceEndpointListItemTypeDef = TypedDict(
    "ResourceEndpointListItemTypeDef",
    {"Protocol": ChannelProtocol, "ResourceEndpoint": str},
    total=False,
)

ResponseMetadata = TypedDict(
    "ResponseMetadata",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, Any],
        "RetryAttempts": int,
    },
)

SingleMasterConfigurationTypeDef = TypedDict(
    "SingleMasterConfigurationTypeDef", {"MessageTtlSeconds": int}, total=False
)

StreamInfoTypeDef = TypedDict(
    "StreamInfoTypeDef",
    {
        "DeviceName": str,
        "StreamName": str,
        "StreamARN": str,
        "MediaType": str,
        "KmsKeyId": str,
        "Version": str,
        "Status": Status,
        "CreationTime": datetime,
        "DataRetentionInHours": int,
    },
    total=False,
)

ChannelNameConditionTypeDef = TypedDict(
    "ChannelNameConditionTypeDef",
    {"ComparisonOperator": ComparisonOperator, "ComparisonValue": str},
    total=False,
)

CreateSignalingChannelOutputTypeDef = TypedDict(
    "CreateSignalingChannelOutputTypeDef",
    {"ChannelARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

CreateStreamOutputTypeDef = TypedDict(
    "CreateStreamOutputTypeDef",
    {"StreamARN": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeSignalingChannelOutputTypeDef = TypedDict(
    "DescribeSignalingChannelOutputTypeDef",
    {"ChannelInfo": "ChannelInfoTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

DescribeStreamOutputTypeDef = TypedDict(
    "DescribeStreamOutputTypeDef",
    {"StreamInfo": "StreamInfoTypeDef", "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetDataEndpointOutputTypeDef = TypedDict(
    "GetDataEndpointOutputTypeDef",
    {"DataEndpoint": str, "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

GetSignalingChannelEndpointOutputTypeDef = TypedDict(
    "GetSignalingChannelEndpointOutputTypeDef",
    {
        "ResourceEndpointList": List["ResourceEndpointListItemTypeDef"],
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListSignalingChannelsOutputTypeDef = TypedDict(
    "ListSignalingChannelsOutputTypeDef",
    {
        "ChannelInfoList": List["ChannelInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {
        "StreamInfoList": List["StreamInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadata",
    },
    total=False,
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {"NextToken": str, "Tags": Dict[str, str], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

ListTagsForStreamOutputTypeDef = TypedDict(
    "ListTagsForStreamOutputTypeDef",
    {"NextToken": str, "Tags": Dict[str, str], "ResponseMetadata": "ResponseMetadata"},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

SingleMasterChannelEndpointConfigurationTypeDef = TypedDict(
    "SingleMasterChannelEndpointConfigurationTypeDef",
    {"Protocols": List[ChannelProtocol], "Role": ChannelRole},
    total=False,
)

StreamNameConditionTypeDef = TypedDict(
    "StreamNameConditionTypeDef",
    {"ComparisonOperator": ComparisonOperator, "ComparisonValue": str},
    total=False,
)

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})
