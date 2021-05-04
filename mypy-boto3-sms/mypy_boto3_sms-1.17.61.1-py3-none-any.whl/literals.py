"""
Type annotations for sms service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sms/literals.html)

Usage::

    ```python
    from mypy_boto3_sms.literals import AppLaunchConfigurationStatus

    data: AppLaunchConfigurationStatus = "CONFIGURED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AppLaunchConfigurationStatus",
    "AppLaunchStatus",
    "AppReplicationConfigurationStatus",
    "AppReplicationStatus",
    "AppStatus",
    "AppValidationStrategy",
    "ConnectorCapability",
    "ConnectorStatus",
    "GetConnectorsPaginatorName",
    "GetReplicationJobsPaginatorName",
    "GetReplicationRunsPaginatorName",
    "GetServersPaginatorName",
    "LicenseType",
    "ListAppsPaginatorName",
    "OutputFormat",
    "ReplicationJobState",
    "ReplicationRunState",
    "ReplicationRunType",
    "ScriptType",
    "ServerCatalogStatus",
    "ServerType",
    "ServerValidationStrategy",
    "ValidationStatus",
    "VmManagerType",
)


AppLaunchConfigurationStatus = Literal["CONFIGURED", "NOT_CONFIGURED"]
AppLaunchStatus = Literal[
    "CONFIGURATION_INVALID",
    "CONFIGURATION_IN_PROGRESS",
    "DELTA_LAUNCH_FAILED",
    "DELTA_LAUNCH_IN_PROGRESS",
    "LAUNCHED",
    "LAUNCH_FAILED",
    "LAUNCH_IN_PROGRESS",
    "LAUNCH_PENDING",
    "PARTIALLY_LAUNCHED",
    "READY_FOR_CONFIGURATION",
    "READY_FOR_LAUNCH",
    "TERMINATED",
    "TERMINATE_FAILED",
    "TERMINATE_IN_PROGRESS",
    "VALIDATION_IN_PROGRESS",
]
AppReplicationConfigurationStatus = Literal["CONFIGURED", "NOT_CONFIGURED"]
AppReplicationStatus = Literal[
    "CONFIGURATION_INVALID",
    "CONFIGURATION_IN_PROGRESS",
    "DELTA_REPLICATED",
    "DELTA_REPLICATION_FAILED",
    "DELTA_REPLICATION_IN_PROGRESS",
    "PARTIALLY_REPLICATED",
    "READY_FOR_CONFIGURATION",
    "READY_FOR_REPLICATION",
    "REPLICATED",
    "REPLICATION_FAILED",
    "REPLICATION_IN_PROGRESS",
    "REPLICATION_PENDING",
    "REPLICATION_STOPPED",
    "REPLICATION_STOPPING",
    "REPLICATION_STOP_FAILED",
    "VALIDATION_IN_PROGRESS",
]
AppStatus = Literal["ACTIVE", "CREATING", "DELETED", "DELETE_FAILED", "DELETING", "UPDATING"]
AppValidationStrategy = Literal["SSM"]
ConnectorCapability = Literal[
    "HYPERV-MANAGER", "SCVMM", "SMS_OPTIMIZED", "SNAPSHOT_BATCHING", "VSPHERE"
]
ConnectorStatus = Literal["HEALTHY", "UNHEALTHY"]
GetConnectorsPaginatorName = Literal["get_connectors"]
GetReplicationJobsPaginatorName = Literal["get_replication_jobs"]
GetReplicationRunsPaginatorName = Literal["get_replication_runs"]
GetServersPaginatorName = Literal["get_servers"]
LicenseType = Literal["AWS", "BYOL"]
ListAppsPaginatorName = Literal["list_apps"]
OutputFormat = Literal["JSON", "YAML"]
ReplicationJobState = Literal[
    "ACTIVE",
    "COMPLETED",
    "DELETED",
    "DELETING",
    "FAILED",
    "FAILING",
    "PAUSED_ON_FAILURE",
    "PENDING",
]
ReplicationRunState = Literal[
    "ACTIVE", "COMPLETED", "DELETED", "DELETING", "FAILED", "MISSED", "PENDING"
]
ReplicationRunType = Literal["AUTOMATIC", "ON_DEMAND"]
ScriptType = Literal["POWERSHELL_SCRIPT", "SHELL_SCRIPT"]
ServerCatalogStatus = Literal["AVAILABLE", "DELETED", "EXPIRED", "IMPORTING", "NOT_IMPORTED"]
ServerType = Literal["VIRTUAL_MACHINE"]
ServerValidationStrategy = Literal["USERDATA"]
ValidationStatus = Literal["FAILED", "IN_PROGRESS", "PENDING", "READY_FOR_VALIDATION", "SUCCEEDED"]
VmManagerType = Literal["HYPERV-MANAGER", "SCVMM", "VSPHERE"]
