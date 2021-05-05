"""
Type annotations for lookoutmetrics service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lookoutmetrics/literals.html)

Usage::

    ```python
    from mypy_boto3_lookoutmetrics.literals import AggregationFunction

    data: AggregationFunction = "AVG"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AggregationFunction",
    "AlertStatus",
    "AlertType",
    "AnomalyDetectionTaskStatus",
    "AnomalyDetectorStatus",
    "CSVFileCompression",
    "Frequency",
    "JsonFileCompression",
)


AggregationFunction = Literal["AVG", "SUM"]
AlertStatus = Literal["ACTIVE", "INACTIVE"]
AlertType = Literal["LAMBDA", "SNS"]
AnomalyDetectionTaskStatus = Literal[
    "COMPLETED", "FAILED", "FAILED_TO_SCHEDULE", "IN_PROGRESS", "PENDING"
]
AnomalyDetectorStatus = Literal[
    "ACTIVATING",
    "ACTIVE",
    "BACK_TEST_ACTIVATING",
    "BACK_TEST_ACTIVE",
    "BACK_TEST_COMPLETE",
    "DELETING",
    "FAILED",
    "INACTIVE",
]
CSVFileCompression = Literal["GZIP", "NONE"]
Frequency = Literal["P1D", "PT10M", "PT1H", "PT5M"]
JsonFileCompression = Literal["GZIP", "NONE"]
