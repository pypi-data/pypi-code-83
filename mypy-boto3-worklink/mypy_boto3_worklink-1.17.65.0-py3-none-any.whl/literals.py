"""
Type annotations for worklink service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_worklink/literals.html)

Usage::

    ```python
    from mypy_boto3_worklink.literals import AuthorizationProviderType

    data: AuthorizationProviderType = "SAML"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AuthorizationProviderType",
    "DeviceStatus",
    "DomainStatus",
    "FleetStatus",
    "IdentityProviderType",
)


AuthorizationProviderType = Literal["SAML"]
DeviceStatus = Literal["ACTIVE", "SIGNED_OUT"]
DomainStatus = Literal[
    "ACTIVE",
    "ASSOCIATING",
    "DISASSOCIATED",
    "DISASSOCIATING",
    "FAILED_TO_ASSOCIATE",
    "FAILED_TO_DISASSOCIATE",
    "INACTIVE",
    "PENDING_VALIDATION",
]
FleetStatus = Literal[
    "ACTIVE", "CREATING", "DELETED", "DELETING", "FAILED_TO_CREATE", "FAILED_TO_DELETE"
]
IdentityProviderType = Literal["SAML"]
