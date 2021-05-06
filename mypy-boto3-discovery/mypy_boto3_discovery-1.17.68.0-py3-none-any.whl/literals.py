"""
Type annotations for discovery service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_discovery/literals.html)

Usage::

    ```python
    from mypy_boto3_discovery.literals import AgentStatus

    data: AgentStatus = "BLACKLISTED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AgentStatus",
    "BatchDeleteImportDataErrorCode",
    "ConfigurationItemType",
    "ContinuousExportStatus",
    "DataSource",
    "DescribeAgentsPaginatorName",
    "DescribeContinuousExportsPaginatorName",
    "DescribeExportConfigurationsPaginatorName",
    "DescribeExportTasksPaginatorName",
    "DescribeTagsPaginatorName",
    "ExportDataFormat",
    "ExportStatus",
    "ImportStatus",
    "ImportTaskFilterName",
    "ListConfigurationsPaginatorName",
    "orderString",
)


AgentStatus = Literal["BLACKLISTED", "HEALTHY", "RUNNING", "SHUTDOWN", "UNHEALTHY", "UNKNOWN"]
BatchDeleteImportDataErrorCode = Literal["INTERNAL_SERVER_ERROR", "NOT_FOUND", "OVER_LIMIT"]
ConfigurationItemType = Literal["APPLICATION", "CONNECTION", "PROCESS", "SERVER"]
ContinuousExportStatus = Literal[
    "ACTIVE",
    "ERROR",
    "INACTIVE",
    "START_FAILED",
    "START_IN_PROGRESS",
    "STOP_FAILED",
    "STOP_IN_PROGRESS",
]
DataSource = Literal["AGENT"]
DescribeAgentsPaginatorName = Literal["describe_agents"]
DescribeContinuousExportsPaginatorName = Literal["describe_continuous_exports"]
DescribeExportConfigurationsPaginatorName = Literal["describe_export_configurations"]
DescribeExportTasksPaginatorName = Literal["describe_export_tasks"]
DescribeTagsPaginatorName = Literal["describe_tags"]
ExportDataFormat = Literal["CSV", "GRAPHML"]
ExportStatus = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
ImportStatus = Literal[
    "DELETE_COMPLETE",
    "DELETE_FAILED",
    "DELETE_FAILED_LIMIT_EXCEEDED",
    "DELETE_IN_PROGRESS",
    "IMPORT_COMPLETE",
    "IMPORT_COMPLETE_WITH_ERRORS",
    "IMPORT_FAILED",
    "IMPORT_FAILED_RECORD_LIMIT_EXCEEDED",
    "IMPORT_FAILED_SERVER_LIMIT_EXCEEDED",
    "IMPORT_IN_PROGRESS",
    "INTERNAL_ERROR",
]
ImportTaskFilterName = Literal["IMPORT_TASK_ID", "NAME", "STATUS"]
ListConfigurationsPaginatorName = Literal["list_configurations"]
orderString = Literal["ASC", "DESC"]
