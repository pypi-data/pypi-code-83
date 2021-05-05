"""
Type annotations for frauddetector service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_frauddetector/literals.html)

Usage::

    ```python
    from mypy_boto3_frauddetector.literals import AsyncJobStatus

    data: AsyncJobStatus = "CANCEL_IN_PROGRESS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AsyncJobStatus",
    "DataSource",
    "DataType",
    "DetectorVersionStatus",
    "Language",
    "ModelEndpointStatus",
    "ModelInputDataFormat",
    "ModelOutputDataFormat",
    "ModelSource",
    "ModelTypeEnum",
    "ModelVersionStatus",
    "RuleExecutionMode",
    "TrainingDataSourceEnum",
)


AsyncJobStatus = Literal[
    "CANCELED",
    "CANCEL_IN_PROGRESS",
    "COMPLETE",
    "FAILED",
    "IN_PROGRESS",
    "IN_PROGRESS_INITIALIZING",
]
DataSource = Literal["EVENT", "EXTERNAL_MODEL_SCORE", "MODEL_SCORE"]
DataType = Literal["BOOLEAN", "FLOAT", "INTEGER", "STRING"]
DetectorVersionStatus = Literal["ACTIVE", "DRAFT", "INACTIVE"]
Language = Literal["DETECTORPL"]
ModelEndpointStatus = Literal["ASSOCIATED", "DISSOCIATED"]
ModelInputDataFormat = Literal["APPLICATION_JSON", "TEXT_CSV"]
ModelOutputDataFormat = Literal["APPLICATION_JSONLINES", "TEXT_CSV"]
ModelSource = Literal["SAGEMAKER"]
ModelTypeEnum = Literal["ONLINE_FRAUD_INSIGHTS"]
ModelVersionStatus = Literal["ACTIVE", "INACTIVE", "TRAINING_CANCELLED"]
RuleExecutionMode = Literal["ALL_MATCHED", "FIRST_MATCHED"]
TrainingDataSourceEnum = Literal["EXTERNAL_EVENTS"]
