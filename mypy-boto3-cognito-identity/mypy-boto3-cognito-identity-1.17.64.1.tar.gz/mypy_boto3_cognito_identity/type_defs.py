"""
Type annotations for cognito-identity service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_identity/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cognito_identity.type_defs import CognitoIdentityProviderTypeDef

    data: CognitoIdentityProviderTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_cognito_identity.literals import (
    AmbiguousRoleResolutionType,
    ErrorCode,
    MappingRuleMatchType,
    RoleMappingType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CognitoIdentityProviderTypeDef",
    "CredentialsTypeDef",
    "DeleteIdentitiesResponseTypeDef",
    "GetCredentialsForIdentityResponseTypeDef",
    "GetIdResponseTypeDef",
    "GetIdentityPoolRolesResponseTypeDef",
    "GetOpenIdTokenForDeveloperIdentityResponseTypeDef",
    "GetOpenIdTokenResponseTypeDef",
    "GetPrincipalTagAttributeMapResponseTypeDef",
    "IdentityDescriptionTypeDef",
    "IdentityPoolShortDescriptionTypeDef",
    "IdentityPoolTypeDef",
    "ListIdentitiesResponseTypeDef",
    "ListIdentityPoolsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LookupDeveloperIdentityResponseTypeDef",
    "MappingRuleTypeDef",
    "MergeDeveloperIdentitiesResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RoleMappingTypeDef",
    "RulesConfigurationTypeTypeDef",
    "SetPrincipalTagAttributeMapResponseTypeDef",
    "UnprocessedIdentityIdTypeDef",
)


class CognitoIdentityProviderTypeDef(TypedDict, total=False):
    ProviderName: str
    ClientId: str
    ServerSideTokenCheck: bool


class CredentialsTypeDef(TypedDict, total=False):
    AccessKeyId: str
    SecretKey: str
    SessionToken: str
    Expiration: datetime


class DeleteIdentitiesResponseTypeDef(TypedDict, total=False):
    UnprocessedIdentityIds: List["UnprocessedIdentityIdTypeDef"]


class GetCredentialsForIdentityResponseTypeDef(TypedDict, total=False):
    IdentityId: str
    Credentials: "CredentialsTypeDef"


class GetIdResponseTypeDef(TypedDict, total=False):
    IdentityId: str


class GetIdentityPoolRolesResponseTypeDef(TypedDict, total=False):
    IdentityPoolId: str
    Roles: Dict[str, str]
    RoleMappings: Dict[str, "RoleMappingTypeDef"]


class GetOpenIdTokenForDeveloperIdentityResponseTypeDef(TypedDict, total=False):
    IdentityId: str
    Token: str


class GetOpenIdTokenResponseTypeDef(TypedDict, total=False):
    IdentityId: str
    Token: str


class GetPrincipalTagAttributeMapResponseTypeDef(TypedDict, total=False):
    IdentityPoolId: str
    IdentityProviderName: str
    UseDefaults: bool
    PrincipalTags: Dict[str, str]


class IdentityDescriptionTypeDef(TypedDict, total=False):
    IdentityId: str
    Logins: List[str]
    CreationDate: datetime
    LastModifiedDate: datetime


class IdentityPoolShortDescriptionTypeDef(TypedDict, total=False):
    IdentityPoolId: str
    IdentityPoolName: str


class _RequiredIdentityPoolTypeDef(TypedDict):
    IdentityPoolId: str
    IdentityPoolName: str
    AllowUnauthenticatedIdentities: bool


class IdentityPoolTypeDef(_RequiredIdentityPoolTypeDef, total=False):
    AllowClassicFlow: bool
    SupportedLoginProviders: Dict[str, str]
    DeveloperProviderName: str
    OpenIdConnectProviderARNs: List[str]
    CognitoIdentityProviders: List["CognitoIdentityProviderTypeDef"]
    SamlProviderARNs: List[str]
    IdentityPoolTags: Dict[str, str]


class ListIdentitiesResponseTypeDef(TypedDict, total=False):
    IdentityPoolId: str
    Identities: List["IdentityDescriptionTypeDef"]
    NextToken: str


class ListIdentityPoolsResponseTypeDef(TypedDict, total=False):
    IdentityPools: List["IdentityPoolShortDescriptionTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class LookupDeveloperIdentityResponseTypeDef(TypedDict, total=False):
    IdentityId: str
    DeveloperUserIdentifierList: List[str]
    NextToken: str


class MappingRuleTypeDef(TypedDict):
    Claim: str
    MatchType: MappingRuleMatchType
    Value: str
    RoleARN: str


class MergeDeveloperIdentitiesResponseTypeDef(TypedDict, total=False):
    IdentityId: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


_RequiredRoleMappingTypeDef = TypedDict("_RequiredRoleMappingTypeDef", {"Type": RoleMappingType})
_OptionalRoleMappingTypeDef = TypedDict(
    "_OptionalRoleMappingTypeDef",
    {
        "AmbiguousRoleResolution": AmbiguousRoleResolutionType,
        "RulesConfiguration": "RulesConfigurationTypeTypeDef",
    },
    total=False,
)


class RoleMappingTypeDef(_RequiredRoleMappingTypeDef, _OptionalRoleMappingTypeDef):
    pass


class RulesConfigurationTypeTypeDef(TypedDict):
    Rules: List["MappingRuleTypeDef"]


class SetPrincipalTagAttributeMapResponseTypeDef(TypedDict, total=False):
    IdentityPoolId: str
    IdentityProviderName: str
    UseDefaults: bool
    PrincipalTags: Dict[str, str]


class UnprocessedIdentityIdTypeDef(TypedDict, total=False):
    IdentityId: str
    ErrorCode: ErrorCode
