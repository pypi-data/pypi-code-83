"""
Type annotations for kinesis-video-archived-media service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis_video_archived_media/literals.html)

Usage::

    ```python
    from mypy_boto3_kinesis_video_archived_media.literals import ClipFragmentSelectorType

    data: ClipFragmentSelectorType = "PRODUCER_TIMESTAMP"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ClipFragmentSelectorType",
    "ContainerFormat",
    "DASHDisplayFragmentNumber",
    "DASHDisplayFragmentTimestamp",
    "DASHFragmentSelectorType",
    "DASHPlaybackMode",
    "FragmentSelectorType",
    "HLSDiscontinuityMode",
    "HLSDisplayFragmentTimestamp",
    "HLSFragmentSelectorType",
    "HLSPlaybackMode",
    "ListFragmentsPaginatorName",
)


ClipFragmentSelectorType = Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"]
ContainerFormat = Literal["FRAGMENTED_MP4", "MPEG_TS"]
DASHDisplayFragmentNumber = Literal["ALWAYS", "NEVER"]
DASHDisplayFragmentTimestamp = Literal["ALWAYS", "NEVER"]
DASHFragmentSelectorType = Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"]
DASHPlaybackMode = Literal["LIVE", "LIVE_REPLAY", "ON_DEMAND"]
FragmentSelectorType = Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"]
HLSDiscontinuityMode = Literal["ALWAYS", "NEVER", "ON_DISCONTINUITY"]
HLSDisplayFragmentTimestamp = Literal["ALWAYS", "NEVER"]
HLSFragmentSelectorType = Literal["PRODUCER_TIMESTAMP", "SERVER_TIMESTAMP"]
HLSPlaybackMode = Literal["LIVE", "LIVE_REPLAY", "ON_DEMAND"]
ListFragmentsPaginatorName = Literal["list_fragments"]
