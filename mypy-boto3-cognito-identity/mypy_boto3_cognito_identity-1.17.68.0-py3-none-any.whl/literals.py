"""
Type annotations for cognito-identity service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/literals.html)

Usage::

    ```python
    from mypy_boto3_cognito_identity.literals import AmbiguousRoleResolutionType

    data: AmbiguousRoleResolutionType = "AuthenticatedRole"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AmbiguousRoleResolutionType",
    "ErrorCode",
    "ListIdentityPoolsPaginatorName",
    "MappingRuleMatchType",
    "RoleMappingType",
)


AmbiguousRoleResolutionType = Literal["AuthenticatedRole", "Deny"]
ErrorCode = Literal["AccessDenied", "InternalServerError"]
ListIdentityPoolsPaginatorName = Literal["list_identity_pools"]
MappingRuleMatchType = Literal["Contains", "Equals", "NotEqual", "StartsWith"]
RoleMappingType = Literal["Rules", "Token"]
