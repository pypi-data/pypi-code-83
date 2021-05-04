"""
Type annotations for mediatailor service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediatailor/literals.html)

Usage::

    ```python
    from mypy_boto3_mediatailor.literals import AccessType

    data: AccessType = "S3_SIGV4"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccessType",
    "ChannelState",
    "GetChannelSchedulePaginatorName",
    "ListChannelsPaginatorName",
    "ListPlaybackConfigurationsPaginatorName",
    "ListSourceLocationsPaginatorName",
    "ListVodSourcesPaginatorName",
    "MessageType",
    "Mode",
    "OriginManifestType",
    "PlaybackMode",
    "RelativePosition",
    "TypeType",
)


AccessType = Literal["S3_SIGV4"]
ChannelState = Literal["RUNNING", "STOPPED"]
GetChannelSchedulePaginatorName = Literal["get_channel_schedule"]
ListChannelsPaginatorName = Literal["list_channels"]
ListPlaybackConfigurationsPaginatorName = Literal["list_playback_configurations"]
ListSourceLocationsPaginatorName = Literal["list_source_locations"]
ListVodSourcesPaginatorName = Literal["list_vod_sources"]
MessageType = Literal["SPLICE_INSERT"]
Mode = Literal["BEHIND_LIVE_EDGE", "OFF"]
OriginManifestType = Literal["MULTI_PERIOD", "SINGLE_PERIOD"]
PlaybackMode = Literal["LOOP"]
RelativePosition = Literal["AFTER_PROGRAM", "BEFORE_PROGRAM"]
TypeType = Literal["DASH", "HLS"]
