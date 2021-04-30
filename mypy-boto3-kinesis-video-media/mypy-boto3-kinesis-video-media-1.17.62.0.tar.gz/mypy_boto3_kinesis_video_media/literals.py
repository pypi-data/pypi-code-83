"""
Main interface for kinesis-video-media service literal definitions.

Usage::

    ```python
    from mypy_boto3_kinesis_video_media.literals import StartSelectorType

    data: StartSelectorType = "CONTINUATION_TOKEN"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("StartSelectorType",)


StartSelectorType = Literal[
    "CONTINUATION_TOKEN",
    "EARLIEST",
    "FRAGMENT_NUMBER",
    "NOW",
    "PRODUCER_TIMESTAMP",
    "SERVER_TIMESTAMP",
]
