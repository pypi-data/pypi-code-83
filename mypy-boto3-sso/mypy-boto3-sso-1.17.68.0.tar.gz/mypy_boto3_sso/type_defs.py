"""
Type annotations for sso service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sso.type_defs import AccountInfoTypeDef

    data: AccountInfoTypeDef = {...}
    ```
"""
import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccountInfoTypeDef",
    "GetRoleCredentialsResponseTypeDef",
    "ListAccountRolesResponseTypeDef",
    "ListAccountsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RoleCredentialsTypeDef",
    "RoleInfoTypeDef",
)


class AccountInfoTypeDef(TypedDict, total=False):
    accountId: str
    accountName: str
    emailAddress: str


class GetRoleCredentialsResponseTypeDef(TypedDict, total=False):
    roleCredentials: "RoleCredentialsTypeDef"


class ListAccountRolesResponseTypeDef(TypedDict, total=False):
    nextToken: str
    roleList: List["RoleInfoTypeDef"]


class ListAccountsResponseTypeDef(TypedDict, total=False):
    nextToken: str
    accountList: List["AccountInfoTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RoleCredentialsTypeDef(TypedDict, total=False):
    accessKeyId: str
    secretAccessKey: str
    sessionToken: str
    expiration: int


class RoleInfoTypeDef(TypedDict, total=False):
    roleName: str
    accountId: str
