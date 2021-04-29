"""
Main interface for iotsecuretunneling service literal definitions.

Usage::

    ```python
    from mypy_boto3_iotsecuretunneling.literals import ConnectionStatus

    data: ConnectionStatus = "CONNECTED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ConnectionStatus", "TunnelStatus")


ConnectionStatus = Literal["CONNECTED", "DISCONNECTED"]
TunnelStatus = Literal["CLOSED", "OPEN"]
