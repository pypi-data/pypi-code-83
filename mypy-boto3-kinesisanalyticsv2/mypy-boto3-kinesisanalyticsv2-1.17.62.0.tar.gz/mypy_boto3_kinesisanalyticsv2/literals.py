"""
Main interface for kinesisanalyticsv2 service literal definitions.

Usage::

    ```python
    from mypy_boto3_kinesisanalyticsv2.literals import ApplicationRestoreType

    data: ApplicationRestoreType = "RESTORE_FROM_CUSTOM_SNAPSHOT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ApplicationRestoreType",
    "ApplicationStatus",
    "CodeContentType",
    "ConfigurationType",
    "InputStartingPosition",
    "ListApplicationSnapshotsPaginatorName",
    "ListApplicationsPaginatorName",
    "LogLevel",
    "MetricsLevel",
    "RecordFormatType",
    "RuntimeEnvironment",
    "SnapshotStatus",
    "UrlType",
)


ApplicationRestoreType = Literal[
    "RESTORE_FROM_CUSTOM_SNAPSHOT", "RESTORE_FROM_LATEST_SNAPSHOT", "SKIP_RESTORE_FROM_SNAPSHOT"
]
ApplicationStatus = Literal[
    "AUTOSCALING",
    "DELETING",
    "FORCE_STOPPING",
    "MAINTENANCE",
    "READY",
    "RUNNING",
    "STARTING",
    "STOPPING",
    "UPDATING",
]
CodeContentType = Literal["PLAINTEXT", "ZIPFILE"]
ConfigurationType = Literal["CUSTOM", "DEFAULT"]
InputStartingPosition = Literal["LAST_STOPPED_POINT", "NOW", "TRIM_HORIZON"]
ListApplicationSnapshotsPaginatorName = Literal["list_application_snapshots"]
ListApplicationsPaginatorName = Literal["list_applications"]
LogLevel = Literal["DEBUG", "ERROR", "INFO", "WARN"]
MetricsLevel = Literal["APPLICATION", "OPERATOR", "PARALLELISM", "TASK"]
RecordFormatType = Literal["CSV", "JSON"]
RuntimeEnvironment = Literal["FLINK-1_11", "FLINK-1_6", "FLINK-1_8", "SQL-1_0"]
SnapshotStatus = Literal["CREATING", "DELETING", "FAILED", "READY"]
UrlType = Literal["FLINK_DASHBOARD_URL"]
