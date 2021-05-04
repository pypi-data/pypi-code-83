"""
Type annotations for amplifybackend service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_amplifybackend/type_defs.html)

Usage::

    ```python
    from mypy_boto3_amplifybackend.type_defs import BackendAPIAppSyncAuthSettingsTypeDef

    data: BackendAPIAppSyncAuthSettingsTypeDef = {...}
    ```
"""
import sys
from typing import List

from mypy_boto3_amplifybackend.literals import (
    AdditionalConstraintsElement,
    AuthResources,
    DeliveryMethod,
    MFAMode,
    MfaTypesElement,
    Mode,
    OAuthGrantType,
    OAuthScopesElement,
    RequiredSignUpAttributesElement,
    ResolutionStrategy,
    SignInMethod,
    Status,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BackendAPIAppSyncAuthSettingsTypeDef",
    "BackendAPIAuthTypeTypeDef",
    "BackendAPIConflictResolutionTypeDef",
    "BackendAPIResourceConfigTypeDef",
    "BackendAuthSocialProviderConfigTypeDef",
    "BackendJobRespObjTypeDef",
    "CloneBackendResponseTypeDef",
    "CreateBackendAPIResponseTypeDef",
    "CreateBackendAuthForgotPasswordConfigTypeDef",
    "CreateBackendAuthIdentityPoolConfigTypeDef",
    "CreateBackendAuthMFAConfigTypeDef",
    "CreateBackendAuthOAuthConfigTypeDef",
    "CreateBackendAuthPasswordPolicyConfigTypeDef",
    "CreateBackendAuthResourceConfigTypeDef",
    "CreateBackendAuthResponseTypeDef",
    "CreateBackendAuthUserPoolConfigTypeDef",
    "CreateBackendConfigResponseTypeDef",
    "CreateBackendResponseTypeDef",
    "CreateTokenResponseTypeDef",
    "DeleteBackendAPIResponseTypeDef",
    "DeleteBackendAuthResponseTypeDef",
    "DeleteBackendResponseTypeDef",
    "DeleteTokenResponseTypeDef",
    "EmailSettingsTypeDef",
    "GenerateBackendAPIModelsResponseTypeDef",
    "GetBackendAPIModelsResponseTypeDef",
    "GetBackendAPIResponseTypeDef",
    "GetBackendAuthResponseTypeDef",
    "GetBackendJobResponseTypeDef",
    "GetBackendResponseTypeDef",
    "GetTokenResponseTypeDef",
    "ListBackendJobsResponseTypeDef",
    "LoginAuthConfigReqObjTypeDef",
    "PaginatorConfigTypeDef",
    "RemoveAllBackendsResponseTypeDef",
    "RemoveBackendConfigResponseTypeDef",
    "SettingsTypeDef",
    "SmsSettingsTypeDef",
    "SocialProviderSettingsTypeDef",
    "UpdateBackendAPIResponseTypeDef",
    "UpdateBackendAuthForgotPasswordConfigTypeDef",
    "UpdateBackendAuthIdentityPoolConfigTypeDef",
    "UpdateBackendAuthMFAConfigTypeDef",
    "UpdateBackendAuthOAuthConfigTypeDef",
    "UpdateBackendAuthPasswordPolicyConfigTypeDef",
    "UpdateBackendAuthResourceConfigTypeDef",
    "UpdateBackendAuthResponseTypeDef",
    "UpdateBackendAuthUserPoolConfigTypeDef",
    "UpdateBackendConfigResponseTypeDef",
    "UpdateBackendJobResponseTypeDef",
)


class BackendAPIAppSyncAuthSettingsTypeDef(TypedDict, total=False):
    CognitoUserPoolId: str
    Description: str
    ExpirationTime: float
    OpenIDAuthTTL: str
    OpenIDClientId: str
    OpenIDIatTTL: str
    OpenIDIssueURL: str
    OpenIDProviderName: str


class BackendAPIAuthTypeTypeDef(TypedDict, total=False):
    Mode: Mode
    Settings: "BackendAPIAppSyncAuthSettingsTypeDef"


class BackendAPIConflictResolutionTypeDef(TypedDict, total=False):
    ResolutionStrategy: ResolutionStrategy


class BackendAPIResourceConfigTypeDef(TypedDict, total=False):
    AdditionalAuthTypes: List["BackendAPIAuthTypeTypeDef"]
    ApiName: str
    ConflictResolution: "BackendAPIConflictResolutionTypeDef"
    DefaultAuthType: "BackendAPIAuthTypeTypeDef"
    Service: str
    TransformSchema: str


class BackendAuthSocialProviderConfigTypeDef(TypedDict, total=False):
    ClientId: str
    ClientSecret: str


class _RequiredBackendJobRespObjTypeDef(TypedDict):
    AppId: str
    BackendEnvironmentName: str


class BackendJobRespObjTypeDef(_RequiredBackendJobRespObjTypeDef, total=False):
    CreateTime: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    UpdateTime: str


class CloneBackendResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str


class CreateBackendAPIResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str


class _RequiredCreateBackendAuthForgotPasswordConfigTypeDef(TypedDict):
    DeliveryMethod: DeliveryMethod


class CreateBackendAuthForgotPasswordConfigTypeDef(
    _RequiredCreateBackendAuthForgotPasswordConfigTypeDef, total=False
):
    EmailSettings: "EmailSettingsTypeDef"
    SmsSettings: "SmsSettingsTypeDef"


class CreateBackendAuthIdentityPoolConfigTypeDef(TypedDict):
    IdentityPoolName: str
    UnauthenticatedLogin: bool


class _RequiredCreateBackendAuthMFAConfigTypeDef(TypedDict):
    MFAMode: MFAMode


class CreateBackendAuthMFAConfigTypeDef(_RequiredCreateBackendAuthMFAConfigTypeDef, total=False):
    Settings: "SettingsTypeDef"


class _RequiredCreateBackendAuthOAuthConfigTypeDef(TypedDict):
    OAuthGrantType: OAuthGrantType
    OAuthScopes: List[OAuthScopesElement]
    RedirectSignInURIs: List[str]
    RedirectSignOutURIs: List[str]


class CreateBackendAuthOAuthConfigTypeDef(
    _RequiredCreateBackendAuthOAuthConfigTypeDef, total=False
):
    DomainPrefix: str
    SocialProviderSettings: "SocialProviderSettingsTypeDef"


class _RequiredCreateBackendAuthPasswordPolicyConfigTypeDef(TypedDict):
    MinimumLength: float


class CreateBackendAuthPasswordPolicyConfigTypeDef(
    _RequiredCreateBackendAuthPasswordPolicyConfigTypeDef, total=False
):
    AdditionalConstraints: List[AdditionalConstraintsElement]


class _RequiredCreateBackendAuthResourceConfigTypeDef(TypedDict):
    AuthResources: AuthResources
    Service: Literal["COGNITO"]
    UserPoolConfigs: "CreateBackendAuthUserPoolConfigTypeDef"


class CreateBackendAuthResourceConfigTypeDef(
    _RequiredCreateBackendAuthResourceConfigTypeDef, total=False
):
    IdentityPoolConfigs: "CreateBackendAuthIdentityPoolConfigTypeDef"


class CreateBackendAuthResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str


class _RequiredCreateBackendAuthUserPoolConfigTypeDef(TypedDict):
    RequiredSignUpAttributes: List[RequiredSignUpAttributesElement]
    SignInMethod: SignInMethod
    UserPoolName: str


class CreateBackendAuthUserPoolConfigTypeDef(
    _RequiredCreateBackendAuthUserPoolConfigTypeDef, total=False
):
    ForgotPassword: "CreateBackendAuthForgotPasswordConfigTypeDef"
    Mfa: "CreateBackendAuthMFAConfigTypeDef"
    OAuth: "CreateBackendAuthOAuthConfigTypeDef"
    PasswordPolicy: "CreateBackendAuthPasswordPolicyConfigTypeDef"


class CreateBackendConfigResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendEnvironmentName: str
    JobId: str
    Status: str


class CreateBackendResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str


class CreateTokenResponseTypeDef(TypedDict, total=False):
    AppId: str
    ChallengeCode: str
    SessionId: str
    Ttl: str


class DeleteBackendAPIResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str


class DeleteBackendAuthResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str


class DeleteBackendResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str


class DeleteTokenResponseTypeDef(TypedDict, total=False):
    IsSuccess: bool


class EmailSettingsTypeDef(TypedDict, total=False):
    EmailMessage: str
    EmailSubject: str


class GenerateBackendAPIModelsResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str


class GetBackendAPIModelsResponseTypeDef(TypedDict, total=False):
    Models: str
    Status: Status


class GetBackendAPIResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    ResourceConfig: "BackendAPIResourceConfigTypeDef"
    ResourceName: str


class GetBackendAuthResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    ResourceConfig: "CreateBackendAuthResourceConfigTypeDef"
    ResourceName: str


class GetBackendJobResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendEnvironmentName: str
    CreateTime: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    UpdateTime: str


class GetBackendResponseTypeDef(TypedDict, total=False):
    AmplifyMetaConfig: str
    AppId: str
    AppName: str
    BackendEnvironmentList: List[str]
    BackendEnvironmentName: str
    Error: str


class GetTokenResponseTypeDef(TypedDict, total=False):
    AppId: str
    ChallengeCode: str
    SessionId: str
    Ttl: str


class ListBackendJobsResponseTypeDef(TypedDict, total=False):
    Jobs: List["BackendJobRespObjTypeDef"]
    NextToken: str


class LoginAuthConfigReqObjTypeDef(TypedDict, total=False):
    AwsCognitoIdentityPoolId: str
    AwsCognitoRegion: str
    AwsUserPoolsId: str
    AwsUserPoolsWebClientId: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RemoveAllBackendsResponseTypeDef(TypedDict, total=False):
    AppId: str
    Error: str
    JobId: str
    Operation: str
    Status: str


class RemoveBackendConfigResponseTypeDef(TypedDict, total=False):
    Error: str


class SettingsTypeDef(TypedDict, total=False):
    MfaTypes: List[MfaTypesElement]
    SmsMessage: str


class SmsSettingsTypeDef(TypedDict, total=False):
    SmsMessage: str


class SocialProviderSettingsTypeDef(TypedDict, total=False):
    Facebook: "BackendAuthSocialProviderConfigTypeDef"
    Google: "BackendAuthSocialProviderConfigTypeDef"
    LoginWithAmazon: "BackendAuthSocialProviderConfigTypeDef"


class UpdateBackendAPIResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str


class UpdateBackendAuthForgotPasswordConfigTypeDef(TypedDict, total=False):
    DeliveryMethod: DeliveryMethod
    EmailSettings: "EmailSettingsTypeDef"
    SmsSettings: "SmsSettingsTypeDef"


class UpdateBackendAuthIdentityPoolConfigTypeDef(TypedDict, total=False):
    UnauthenticatedLogin: bool


class UpdateBackendAuthMFAConfigTypeDef(TypedDict, total=False):
    MFAMode: MFAMode
    Settings: "SettingsTypeDef"


class UpdateBackendAuthOAuthConfigTypeDef(TypedDict, total=False):
    DomainPrefix: str
    OAuthGrantType: OAuthGrantType
    OAuthScopes: List[OAuthScopesElement]
    RedirectSignInURIs: List[str]
    RedirectSignOutURIs: List[str]
    SocialProviderSettings: "SocialProviderSettingsTypeDef"


class UpdateBackendAuthPasswordPolicyConfigTypeDef(TypedDict, total=False):
    AdditionalConstraints: List[AdditionalConstraintsElement]
    MinimumLength: float


class _RequiredUpdateBackendAuthResourceConfigTypeDef(TypedDict):
    AuthResources: AuthResources
    Service: Literal["COGNITO"]
    UserPoolConfigs: "UpdateBackendAuthUserPoolConfigTypeDef"


class UpdateBackendAuthResourceConfigTypeDef(
    _RequiredUpdateBackendAuthResourceConfigTypeDef, total=False
):
    IdentityPoolConfigs: "UpdateBackendAuthIdentityPoolConfigTypeDef"


class UpdateBackendAuthResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendEnvironmentName: str
    Error: str
    JobId: str
    Operation: str
    Status: str


class UpdateBackendAuthUserPoolConfigTypeDef(TypedDict, total=False):
    ForgotPassword: "UpdateBackendAuthForgotPasswordConfigTypeDef"
    Mfa: "UpdateBackendAuthMFAConfigTypeDef"
    OAuth: "UpdateBackendAuthOAuthConfigTypeDef"
    PasswordPolicy: "UpdateBackendAuthPasswordPolicyConfigTypeDef"


class UpdateBackendConfigResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendManagerAppId: str
    Error: str
    LoginAuthConfig: "LoginAuthConfigReqObjTypeDef"


class UpdateBackendJobResponseTypeDef(TypedDict, total=False):
    AppId: str
    BackendEnvironmentName: str
    CreateTime: str
    Error: str
    JobId: str
    Operation: str
    Status: str
    UpdateTime: str
