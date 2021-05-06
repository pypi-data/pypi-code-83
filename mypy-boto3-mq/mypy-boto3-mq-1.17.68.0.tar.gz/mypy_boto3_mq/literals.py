"""
Type annotations for mq service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mq/literals.html)

Usage::

    ```python
    from mypy_boto3_mq.literals import AuthenticationStrategy

    data: AuthenticationStrategy = "LDAP"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AuthenticationStrategy",
    "BrokerState",
    "BrokerStorageType",
    "ChangeType",
    "DayOfWeek",
    "DeploymentMode",
    "EngineType",
    "ListBrokersPaginatorName",
    "SanitizationWarningReason",
)


AuthenticationStrategy = Literal["LDAP", "SIMPLE"]
BrokerState = Literal[
    "CREATION_FAILED",
    "CREATION_IN_PROGRESS",
    "DELETION_IN_PROGRESS",
    "REBOOT_IN_PROGRESS",
    "RUNNING",
]
BrokerStorageType = Literal["EBS", "EFS"]
ChangeType = Literal["CREATE", "DELETE", "UPDATE"]
DayOfWeek = Literal["FRIDAY", "MONDAY", "SATURDAY", "SUNDAY", "THURSDAY", "TUESDAY", "WEDNESDAY"]
DeploymentMode = Literal["ACTIVE_STANDBY_MULTI_AZ", "CLUSTER_MULTI_AZ", "SINGLE_INSTANCE"]
EngineType = Literal["ACTIVEMQ", "RABBITMQ"]
ListBrokersPaginatorName = Literal["list_brokers"]
SanitizationWarningReason = Literal[
    "DISALLOWED_ATTRIBUTE_REMOVED", "DISALLOWED_ELEMENT_REMOVED", "INVALID_ATTRIBUTE_VALUE_REMOVED"
]
