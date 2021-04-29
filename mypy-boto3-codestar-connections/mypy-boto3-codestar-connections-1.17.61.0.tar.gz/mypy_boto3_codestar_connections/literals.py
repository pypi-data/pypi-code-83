"""
Main interface for codestar-connections service literal definitions.

Usage::

    ```python
    from mypy_boto3_codestar_connections.literals import ConnectionStatus

    data: ConnectionStatus = "AVAILABLE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ConnectionStatus", "ProviderType")


ConnectionStatus = Literal["AVAILABLE", "ERROR", "PENDING"]
ProviderType = Literal["Bitbucket", "GitHub", "GitHubEnterpriseServer"]
