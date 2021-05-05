"""
Type annotations for kinesisvideo service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisvideo/literals.html)

Usage::

    ```python
    from mypy_boto3_kinesisvideo.literals import APIName

    data: APIName = "GET_CLIP"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "APIName",
    "ChannelProtocol",
    "ChannelRole",
    "ChannelType",
    "ComparisonOperator",
    "ListSignalingChannelsPaginatorName",
    "ListStreamsPaginatorName",
    "Status",
    "UpdateDataRetentionOperation",
)


APIName = Literal[
    "GET_CLIP",
    "GET_DASH_STREAMING_SESSION_URL",
    "GET_HLS_STREAMING_SESSION_URL",
    "GET_MEDIA",
    "GET_MEDIA_FOR_FRAGMENT_LIST",
    "LIST_FRAGMENTS",
    "PUT_MEDIA",
]
ChannelProtocol = Literal["HTTPS", "WSS"]
ChannelRole = Literal["MASTER", "VIEWER"]
ChannelType = Literal["SINGLE_MASTER"]
ComparisonOperator = Literal["BEGINS_WITH"]
ListSignalingChannelsPaginatorName = Literal["list_signaling_channels"]
ListStreamsPaginatorName = Literal["list_streams"]
Status = Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
UpdateDataRetentionOperation = Literal["DECREASE_DATA_RETENTION", "INCREASE_DATA_RETENTION"]
