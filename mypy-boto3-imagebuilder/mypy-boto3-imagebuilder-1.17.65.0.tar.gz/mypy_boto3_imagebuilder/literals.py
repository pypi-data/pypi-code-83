"""
Type annotations for imagebuilder service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_imagebuilder/literals.html)

Usage::

    ```python
    from mypy_boto3_imagebuilder.literals import ComponentFormat

    data: ComponentFormat = "SHELL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ComponentFormat",
    "ComponentType",
    "ContainerRepositoryService",
    "ContainerType",
    "EbsVolumeType",
    "ImageStatus",
    "ImageType",
    "Ownership",
    "PipelineExecutionStartCondition",
    "PipelineStatus",
    "Platform",
)


ComponentFormat = Literal["SHELL"]
ComponentType = Literal["BUILD", "TEST"]
ContainerRepositoryService = Literal["ECR"]
ContainerType = Literal["DOCKER"]
EbsVolumeType = Literal["gp2", "gp3", "io1", "io2", "sc1", "st1", "standard"]
ImageStatus = Literal[
    "AVAILABLE",
    "BUILDING",
    "CANCELLED",
    "CREATING",
    "DELETED",
    "DEPRECATED",
    "DISTRIBUTING",
    "FAILED",
    "INTEGRATING",
    "PENDING",
    "TESTING",
]
ImageType = Literal["AMI", "DOCKER"]
Ownership = Literal["Amazon", "Self", "Shared"]
PipelineExecutionStartCondition = Literal[
    "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE", "EXPRESSION_MATCH_ONLY"
]
PipelineStatus = Literal["DISABLED", "ENABLED"]
Platform = Literal["Linux", "Windows"]
