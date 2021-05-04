"""
Type annotations for sts service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sts/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sts.type_defs import AssumeRoleResponseTypeDef

    data: AssumeRoleResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssumeRoleResponseTypeDef",
    "AssumeRoleWithSAMLResponseTypeDef",
    "AssumeRoleWithWebIdentityResponseTypeDef",
    "AssumedRoleUserTypeDef",
    "CredentialsTypeDef",
    "DecodeAuthorizationMessageResponseTypeDef",
    "FederatedUserTypeDef",
    "GetAccessKeyInfoResponseTypeDef",
    "GetCallerIdentityResponseTypeDef",
    "GetFederationTokenResponseTypeDef",
    "GetSessionTokenResponseTypeDef",
    "PolicyDescriptorTypeTypeDef",
    "TagTypeDef",
)


class AssumeRoleResponseTypeDef(TypedDict, total=False):
    Credentials: "CredentialsTypeDef"
    AssumedRoleUser: "AssumedRoleUserTypeDef"
    PackedPolicySize: int
    SourceIdentity: str


class AssumeRoleWithSAMLResponseTypeDef(TypedDict, total=False):
    Credentials: "CredentialsTypeDef"
    AssumedRoleUser: "AssumedRoleUserTypeDef"
    PackedPolicySize: int
    Subject: str
    SubjectType: str
    Issuer: str
    Audience: str
    NameQualifier: str
    SourceIdentity: str


class AssumeRoleWithWebIdentityResponseTypeDef(TypedDict, total=False):
    Credentials: "CredentialsTypeDef"
    SubjectFromWebIdentityToken: str
    AssumedRoleUser: "AssumedRoleUserTypeDef"
    PackedPolicySize: int
    Provider: str
    Audience: str
    SourceIdentity: str


class AssumedRoleUserTypeDef(TypedDict):
    AssumedRoleId: str
    Arn: str


class CredentialsTypeDef(TypedDict):
    AccessKeyId: str
    SecretAccessKey: str
    SessionToken: str
    Expiration: datetime


class DecodeAuthorizationMessageResponseTypeDef(TypedDict, total=False):
    DecodedMessage: str


class FederatedUserTypeDef(TypedDict):
    FederatedUserId: str
    Arn: str


class GetAccessKeyInfoResponseTypeDef(TypedDict, total=False):
    Account: str


class GetCallerIdentityResponseTypeDef(TypedDict, total=False):
    UserId: str
    Account: str
    Arn: str


class GetFederationTokenResponseTypeDef(TypedDict, total=False):
    Credentials: "CredentialsTypeDef"
    FederatedUser: "FederatedUserTypeDef"
    PackedPolicySize: int


class GetSessionTokenResponseTypeDef(TypedDict, total=False):
    Credentials: "CredentialsTypeDef"


class PolicyDescriptorTypeTypeDef(TypedDict, total=False):
    arn: str


class TagTypeDef(TypedDict):
    Key: str
    Value: str
