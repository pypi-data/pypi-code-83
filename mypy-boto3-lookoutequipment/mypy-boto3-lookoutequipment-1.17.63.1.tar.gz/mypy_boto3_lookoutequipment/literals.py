"""
Type annotations for lookoutequipment service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutequipment/literals.html)

Usage::

    ```python
    from mypy_boto3_lookoutequipment.literals import DataUploadFrequency

    data: DataUploadFrequency = "PT10M"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DataUploadFrequency",
    "DatasetStatus",
    "InferenceExecutionStatus",
    "InferenceSchedulerStatus",
    "IngestionJobStatus",
    "ModelStatus",
    "TargetSamplingRate",
)


DataUploadFrequency = Literal["PT10M", "PT15M", "PT1H", "PT30M", "PT5M"]
DatasetStatus = Literal["ACTIVE", "CREATED", "INGESTION_IN_PROGRESS"]
InferenceExecutionStatus = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
InferenceSchedulerStatus = Literal["PENDING", "RUNNING", "STOPPED", "STOPPING"]
IngestionJobStatus = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
ModelStatus = Literal["FAILED", "IN_PROGRESS", "SUCCESS"]
TargetSamplingRate = Literal[
    "PT10M", "PT10S", "PT15M", "PT15S", "PT1H", "PT1M", "PT1S", "PT30M", "PT30S", "PT5M", "PT5S"
]
