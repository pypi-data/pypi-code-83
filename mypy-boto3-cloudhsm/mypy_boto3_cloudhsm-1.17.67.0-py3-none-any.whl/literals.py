"""
Type annotations for cloudhsm service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudhsm/literals.html)

Usage::

    ```python
    from mypy_boto3_cloudhsm.literals import ClientVersion

    data: ClientVersion = "5.1"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ClientVersion",
    "CloudHsmObjectState",
    "HsmStatus",
    "ListHapgsPaginatorName",
    "ListHsmsPaginatorName",
    "ListLunaClientsPaginatorName",
    "SubscriptionType",
)


ClientVersion = Literal["5.1", "5.3"]
CloudHsmObjectState = Literal["DEGRADED", "READY", "UPDATING"]
HsmStatus = Literal[
    "DEGRADED", "PENDING", "RUNNING", "SUSPENDED", "TERMINATED", "TERMINATING", "UPDATING"
]
ListHapgsPaginatorName = Literal["list_hapgs"]
ListHsmsPaginatorName = Literal["list_hsms"]
ListLunaClientsPaginatorName = Literal["list_luna_clients"]
SubscriptionType = Literal["PRODUCTION"]
