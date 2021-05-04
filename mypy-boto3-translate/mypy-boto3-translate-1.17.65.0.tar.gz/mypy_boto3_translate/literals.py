"""
Type annotations for translate service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_translate/literals.html)

Usage::

    ```python
    from mypy_boto3_translate.literals import EncryptionKeyType

    data: EncryptionKeyType = "KMS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "EncryptionKeyType",
    "JobStatus",
    "ListTerminologiesPaginatorName",
    "MergeStrategy",
    "ParallelDataFormat",
    "ParallelDataStatus",
    "TerminologyDataFormat",
)


EncryptionKeyType = Literal["KMS"]
JobStatus = Literal[
    "COMPLETED",
    "COMPLETED_WITH_ERROR",
    "FAILED",
    "IN_PROGRESS",
    "STOPPED",
    "STOP_REQUESTED",
    "SUBMITTED",
]
ListTerminologiesPaginatorName = Literal["list_terminologies"]
MergeStrategy = Literal["OVERWRITE"]
ParallelDataFormat = Literal["CSV", "TMX", "TSV"]
ParallelDataStatus = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
TerminologyDataFormat = Literal["CSV", "TMX"]
