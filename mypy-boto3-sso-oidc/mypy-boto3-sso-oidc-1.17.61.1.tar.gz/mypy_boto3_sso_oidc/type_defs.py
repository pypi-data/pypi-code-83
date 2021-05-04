"""
Type annotations for sso-oidc service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sso_oidc/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sso_oidc.type_defs import CreateTokenResponseTypeDef

    data: CreateTokenResponseTypeDef = {...}
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateTokenResponseTypeDef",
    "RegisterClientResponseTypeDef",
    "StartDeviceAuthorizationResponseTypeDef",
)


class CreateTokenResponseTypeDef(TypedDict, total=False):
    accessToken: str
    tokenType: str
    expiresIn: int
    refreshToken: str
    idToken: str


class RegisterClientResponseTypeDef(TypedDict, total=False):
    clientId: str
    clientSecret: str
    clientIdIssuedAt: int
    clientSecretExpiresAt: int
    authorizationEndpoint: str
    tokenEndpoint: str


class StartDeviceAuthorizationResponseTypeDef(TypedDict, total=False):
    deviceCode: str
    userCode: str
    verificationUri: str
    verificationUriComplete: str
    expiresIn: int
    interval: int
