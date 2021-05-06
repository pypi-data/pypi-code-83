"""
Type annotations for mgh service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/literals.html)

Usage::

    ```python
    from mypy_boto3_mgh.literals import ApplicationStatus

    data: ApplicationStatus = "COMPLETED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ApplicationStatus",
    "ListApplicationStatesPaginatorName",
    "ListCreatedArtifactsPaginatorName",
    "ListDiscoveredResourcesPaginatorName",
    "ListMigrationTasksPaginatorName",
    "ListProgressUpdateStreamsPaginatorName",
    "ResourceAttributeType",
    "Status",
)


ApplicationStatus = Literal["COMPLETED", "IN_PROGRESS", "NOT_STARTED"]
ListApplicationStatesPaginatorName = Literal["list_application_states"]
ListCreatedArtifactsPaginatorName = Literal["list_created_artifacts"]
ListDiscoveredResourcesPaginatorName = Literal["list_discovered_resources"]
ListMigrationTasksPaginatorName = Literal["list_migration_tasks"]
ListProgressUpdateStreamsPaginatorName = Literal["list_progress_update_streams"]
ResourceAttributeType = Literal[
    "BIOS_ID",
    "FQDN",
    "IPV4_ADDRESS",
    "IPV6_ADDRESS",
    "MAC_ADDRESS",
    "MOTHERBOARD_SERIAL_NUMBER",
    "VM_MANAGED_OBJECT_REFERENCE",
    "VM_MANAGER_ID",
    "VM_NAME",
    "VM_PATH",
]
Status = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "NOT_STARTED"]
