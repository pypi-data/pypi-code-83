"""
Main interface for kinesis-video-signaling service literal definitions.

Usage::

    ```python
    from mypy_boto3_kinesis_video_signaling.literals import Service

    data: Service = "TURN"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("Service",)


Service = Literal["TURN"]
