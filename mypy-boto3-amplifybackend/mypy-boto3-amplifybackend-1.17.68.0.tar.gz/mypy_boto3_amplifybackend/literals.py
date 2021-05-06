"""
Type annotations for amplifybackend service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/literals.html)

Usage::

    ```python
    from mypy_boto3_amplifybackend.literals import AdditionalConstraintsElement

    data: AdditionalConstraintsElement = "REQUIRE_DIGIT"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AdditionalConstraintsElement",
    "AuthResources",
    "DeliveryMethod",
    "ListBackendJobsPaginatorName",
    "MFAMode",
    "MfaTypesElement",
    "Mode",
    "OAuthGrantType",
    "OAuthScopesElement",
    "RequiredSignUpAttributesElement",
    "ResolutionStrategy",
    "Service",
    "SignInMethod",
    "Status",
)


AdditionalConstraintsElement = Literal[
    "REQUIRE_DIGIT", "REQUIRE_LOWERCASE", "REQUIRE_SYMBOL", "REQUIRE_UPPERCASE"
]
AuthResources = Literal["IDENTITY_POOL_AND_USER_POOL", "USER_POOL_ONLY"]
DeliveryMethod = Literal["EMAIL", "SMS"]
ListBackendJobsPaginatorName = Literal["list_backend_jobs"]
MFAMode = Literal["OFF", "ON", "OPTIONAL"]
MfaTypesElement = Literal["SMS", "TOTP"]
Mode = Literal["AMAZON_COGNITO_USER_POOLS", "API_KEY", "AWS_IAM", "OPENID_CONNECT"]
OAuthGrantType = Literal["CODE", "IMPLICIT"]
OAuthScopesElement = Literal["AWS_COGNITO_SIGNIN_USER_ADMIN", "EMAIL", "OPENID", "PHONE", "PROFILE"]
RequiredSignUpAttributesElement = Literal[
    "ADDRESS",
    "BIRTHDATE",
    "EMAIL",
    "FAMILY_NAME",
    "GENDER",
    "GIVEN_NAME",
    "LOCALE",
    "MIDDLE_NAME",
    "NAME",
    "NICKNAME",
    "PHONE_NUMBER",
    "PICTURE",
    "PREFERRED_USERNAME",
    "PROFILE",
    "UPDATED_AT",
    "WEBSITE",
    "ZONE_INFO",
]
ResolutionStrategy = Literal["AUTOMERGE", "LAMBDA", "NONE", "OPTIMISTIC_CONCURRENCY"]
Service = Literal["COGNITO"]
SignInMethod = Literal["EMAIL", "EMAIL_AND_PHONE_NUMBER", "PHONE_NUMBER", "USERNAME"]
Status = Literal["LATEST", "STALE"]
