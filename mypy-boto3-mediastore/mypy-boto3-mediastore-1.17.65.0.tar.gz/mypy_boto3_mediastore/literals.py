"""
Type annotations for mediastore service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mediastore/literals.html)

Usage::

    ```python
    from mypy_boto3_mediastore.literals import ContainerLevelMetrics

    data: ContainerLevelMetrics = "DISABLED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ContainerLevelMetrics", "ContainerStatus", "ListContainersPaginatorName", "MethodName")


ContainerLevelMetrics = Literal["DISABLED", "ENABLED"]
ContainerStatus = Literal["ACTIVE", "CREATING", "DELETING"]
ListContainersPaginatorName = Literal["list_containers"]
MethodName = Literal["DELETE", "GET", "HEAD", "PUT"]
