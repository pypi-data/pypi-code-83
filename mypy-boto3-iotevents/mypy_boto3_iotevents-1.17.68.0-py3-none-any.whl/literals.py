"""
Type annotations for iotevents service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/literals.html)

Usage::

    ```python
    from mypy_boto3_iotevents.literals import AnalysisResultLevel

    data: AnalysisResultLevel = "ERROR"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AnalysisResultLevel",
    "AnalysisStatus",
    "DetectorModelVersionStatus",
    "EvaluationMethod",
    "InputStatus",
    "LoggingLevel",
    "PayloadType",
)


AnalysisResultLevel = Literal["ERROR", "INFO", "WARNING"]
AnalysisStatus = Literal["COMPLETE", "FAILED", "RUNNING"]
DetectorModelVersionStatus = Literal[
    "ACTIVATING", "ACTIVE", "DEPRECATED", "DRAFT", "FAILED", "INACTIVE", "PAUSED"
]
EvaluationMethod = Literal["BATCH", "SERIAL"]
InputStatus = Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
LoggingLevel = Literal["DEBUG", "ERROR", "INFO"]
PayloadType = Literal["JSON", "STRING"]
