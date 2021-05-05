"""
Type annotations for cognito-idp service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cognito_idp.type_defs import AccountRecoverySettingTypeTypeDef

    data: AccountRecoverySettingTypeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_cognito_idp.literals import (
    AccountTakeoverEventActionType,
    AdvancedSecurityModeType,
    AliasAttributeType,
    AttributeDataType,
    ChallengeName,
    ChallengeNameType,
    ChallengeResponse,
    CompromisedCredentialsEventActionType,
    DefaultEmailOptionType,
    DeliveryMediumType,
    DomainStatusType,
    EmailSendingAccountType,
    EventFilterType,
    EventResponseType,
    EventType,
    ExplicitAuthFlowsType,
    FeedbackValueType,
    IdentityProviderTypeType,
    OAuthFlowType,
    PreventUserExistenceErrorTypes,
    RecoveryOptionNameType,
    RiskDecisionType,
    RiskLevelType,
    StatusType,
    TimeUnitsType,
    UserImportJobStatusType,
    UsernameAttributeType,
    UserPoolMfaType,
    UserStatusType,
    VerifiedAttributeType,
    VerifySoftwareTokenResponseType,
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
    "AccountRecoverySettingTypeTypeDef",
    "AccountTakeoverActionTypeTypeDef",
    "AccountTakeoverActionsTypeTypeDef",
    "AccountTakeoverRiskConfigurationTypeTypeDef",
    "AdminCreateUserConfigTypeTypeDef",
    "AdminCreateUserResponseTypeDef",
    "AdminGetDeviceResponseTypeDef",
    "AdminGetUserResponseTypeDef",
    "AdminInitiateAuthResponseTypeDef",
    "AdminListDevicesResponseTypeDef",
    "AdminListGroupsForUserResponseTypeDef",
    "AdminListUserAuthEventsResponseTypeDef",
    "AdminRespondToAuthChallengeResponseTypeDef",
    "AnalyticsConfigurationTypeTypeDef",
    "AnalyticsMetadataTypeTypeDef",
    "AssociateSoftwareTokenResponseTypeDef",
    "AttributeTypeTypeDef",
    "AuthEventTypeTypeDef",
    "AuthenticationResultTypeTypeDef",
    "ChallengeResponseTypeTypeDef",
    "CodeDeliveryDetailsTypeTypeDef",
    "CompromisedCredentialsActionsTypeTypeDef",
    "CompromisedCredentialsRiskConfigurationTypeTypeDef",
    "ConfirmDeviceResponseTypeDef",
    "ContextDataTypeTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateIdentityProviderResponseTypeDef",
    "CreateResourceServerResponseTypeDef",
    "CreateUserImportJobResponseTypeDef",
    "CreateUserPoolClientResponseTypeDef",
    "CreateUserPoolDomainResponseTypeDef",
    "CreateUserPoolResponseTypeDef",
    "CustomDomainConfigTypeTypeDef",
    "CustomEmailLambdaVersionConfigTypeTypeDef",
    "CustomSMSLambdaVersionConfigTypeTypeDef",
    "DescribeIdentityProviderResponseTypeDef",
    "DescribeResourceServerResponseTypeDef",
    "DescribeRiskConfigurationResponseTypeDef",
    "DescribeUserImportJobResponseTypeDef",
    "DescribeUserPoolClientResponseTypeDef",
    "DescribeUserPoolDomainResponseTypeDef",
    "DescribeUserPoolResponseTypeDef",
    "DeviceConfigurationTypeTypeDef",
    "DeviceSecretVerifierConfigTypeTypeDef",
    "DeviceTypeTypeDef",
    "DomainDescriptionTypeTypeDef",
    "EmailConfigurationTypeTypeDef",
    "EventContextDataTypeTypeDef",
    "EventFeedbackTypeTypeDef",
    "EventRiskTypeTypeDef",
    "ForgotPasswordResponseTypeDef",
    "GetCSVHeaderResponseTypeDef",
    "GetDeviceResponseTypeDef",
    "GetGroupResponseTypeDef",
    "GetIdentityProviderByIdentifierResponseTypeDef",
    "GetSigningCertificateResponseTypeDef",
    "GetUICustomizationResponseTypeDef",
    "GetUserAttributeVerificationCodeResponseTypeDef",
    "GetUserPoolMfaConfigResponseTypeDef",
    "GetUserResponseTypeDef",
    "GroupTypeTypeDef",
    "HttpHeaderTypeDef",
    "IdentityProviderTypeTypeDef",
    "InitiateAuthResponseTypeDef",
    "LambdaConfigTypeTypeDef",
    "ListDevicesResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListIdentityProvidersResponseTypeDef",
    "ListResourceServersResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUserImportJobsResponseTypeDef",
    "ListUserPoolClientsResponseTypeDef",
    "ListUserPoolsResponseTypeDef",
    "ListUsersInGroupResponseTypeDef",
    "ListUsersResponseTypeDef",
    "MFAOptionTypeTypeDef",
    "MessageTemplateTypeTypeDef",
    "NewDeviceMetadataTypeTypeDef",
    "NotifyConfigurationTypeTypeDef",
    "NotifyEmailTypeTypeDef",
    "NumberAttributeConstraintsTypeTypeDef",
    "PaginatorConfigTypeDef",
    "PasswordPolicyTypeTypeDef",
    "ProviderDescriptionTypeDef",
    "ProviderUserIdentifierTypeTypeDef",
    "RecoveryOptionTypeTypeDef",
    "ResendConfirmationCodeResponseTypeDef",
    "ResourceServerScopeTypeTypeDef",
    "ResourceServerTypeTypeDef",
    "RespondToAuthChallengeResponseTypeDef",
    "RiskConfigurationTypeTypeDef",
    "RiskExceptionConfigurationTypeTypeDef",
    "SMSMfaSettingsTypeTypeDef",
    "SchemaAttributeTypeTypeDef",
    "SetRiskConfigurationResponseTypeDef",
    "SetUICustomizationResponseTypeDef",
    "SetUserPoolMfaConfigResponseTypeDef",
    "SignUpResponseTypeDef",
    "SmsConfigurationTypeTypeDef",
    "SmsMfaConfigTypeTypeDef",
    "SoftwareTokenMfaConfigTypeTypeDef",
    "SoftwareTokenMfaSettingsTypeTypeDef",
    "StartUserImportJobResponseTypeDef",
    "StopUserImportJobResponseTypeDef",
    "StringAttributeConstraintsTypeTypeDef",
    "TokenValidityUnitsTypeTypeDef",
    "UICustomizationTypeTypeDef",
    "UpdateGroupResponseTypeDef",
    "UpdateIdentityProviderResponseTypeDef",
    "UpdateResourceServerResponseTypeDef",
    "UpdateUserAttributesResponseTypeDef",
    "UpdateUserPoolClientResponseTypeDef",
    "UpdateUserPoolDomainResponseTypeDef",
    "UserContextDataTypeTypeDef",
    "UserImportJobTypeTypeDef",
    "UserPoolAddOnsTypeTypeDef",
    "UserPoolClientDescriptionTypeDef",
    "UserPoolClientTypeTypeDef",
    "UserPoolDescriptionTypeTypeDef",
    "UserPoolPolicyTypeTypeDef",
    "UserPoolTypeTypeDef",
    "UserTypeTypeDef",
    "UsernameConfigurationTypeTypeDef",
    "VerificationMessageTemplateTypeTypeDef",
    "VerifySoftwareTokenResponseTypeDef",
)


class AccountRecoverySettingTypeTypeDef(TypedDict, total=False):
    RecoveryMechanisms: List["RecoveryOptionTypeTypeDef"]


class AccountTakeoverActionTypeTypeDef(TypedDict):
    Notify: bool
    EventAction: AccountTakeoverEventActionType


class AccountTakeoverActionsTypeTypeDef(TypedDict, total=False):
    LowAction: "AccountTakeoverActionTypeTypeDef"
    MediumAction: "AccountTakeoverActionTypeTypeDef"
    HighAction: "AccountTakeoverActionTypeTypeDef"


class _RequiredAccountTakeoverRiskConfigurationTypeTypeDef(TypedDict):
    Actions: "AccountTakeoverActionsTypeTypeDef"


class AccountTakeoverRiskConfigurationTypeTypeDef(
    _RequiredAccountTakeoverRiskConfigurationTypeTypeDef, total=False
):
    NotifyConfiguration: "NotifyConfigurationTypeTypeDef"


class AdminCreateUserConfigTypeTypeDef(TypedDict, total=False):
    AllowAdminCreateUserOnly: bool
    UnusedAccountValidityDays: int
    InviteMessageTemplate: "MessageTemplateTypeTypeDef"


class AdminCreateUserResponseTypeDef(TypedDict, total=False):
    User: "UserTypeTypeDef"


class AdminGetDeviceResponseTypeDef(TypedDict):
    Device: "DeviceTypeTypeDef"


class _RequiredAdminGetUserResponseTypeDef(TypedDict):
    Username: str


class AdminGetUserResponseTypeDef(_RequiredAdminGetUserResponseTypeDef, total=False):
    UserAttributes: List["AttributeTypeTypeDef"]
    UserCreateDate: datetime
    UserLastModifiedDate: datetime
    Enabled: bool
    UserStatus: UserStatusType
    MFAOptions: List["MFAOptionTypeTypeDef"]
    PreferredMfaSetting: str
    UserMFASettingList: List[str]


class AdminInitiateAuthResponseTypeDef(TypedDict, total=False):
    ChallengeName: ChallengeNameType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: "AuthenticationResultTypeTypeDef"


class AdminListDevicesResponseTypeDef(TypedDict, total=False):
    Devices: List["DeviceTypeTypeDef"]
    PaginationToken: str


class AdminListGroupsForUserResponseTypeDef(TypedDict, total=False):
    Groups: List["GroupTypeTypeDef"]
    NextToken: str


class AdminListUserAuthEventsResponseTypeDef(TypedDict, total=False):
    AuthEvents: List["AuthEventTypeTypeDef"]
    NextToken: str


class AdminRespondToAuthChallengeResponseTypeDef(TypedDict, total=False):
    ChallengeName: ChallengeNameType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: "AuthenticationResultTypeTypeDef"


class AnalyticsConfigurationTypeTypeDef(TypedDict, total=False):
    ApplicationId: str
    ApplicationArn: str
    RoleArn: str
    ExternalId: str
    UserDataShared: bool


class AnalyticsMetadataTypeTypeDef(TypedDict, total=False):
    AnalyticsEndpointId: str


class AssociateSoftwareTokenResponseTypeDef(TypedDict, total=False):
    SecretCode: str
    Session: str


class _RequiredAttributeTypeTypeDef(TypedDict):
    Name: str


class AttributeTypeTypeDef(_RequiredAttributeTypeTypeDef, total=False):
    Value: str


class AuthEventTypeTypeDef(TypedDict, total=False):
    EventId: str
    EventType: EventType
    CreationDate: datetime
    EventResponse: EventResponseType
    EventRisk: "EventRiskTypeTypeDef"
    ChallengeResponses: List["ChallengeResponseTypeTypeDef"]
    EventContextData: "EventContextDataTypeTypeDef"
    EventFeedback: "EventFeedbackTypeTypeDef"


class AuthenticationResultTypeTypeDef(TypedDict, total=False):
    AccessToken: str
    ExpiresIn: int
    TokenType: str
    RefreshToken: str
    IdToken: str
    NewDeviceMetadata: "NewDeviceMetadataTypeTypeDef"


class ChallengeResponseTypeTypeDef(TypedDict, total=False):
    ChallengeName: ChallengeName
    ChallengeResponse: ChallengeResponse


class CodeDeliveryDetailsTypeTypeDef(TypedDict, total=False):
    Destination: str
    DeliveryMedium: DeliveryMediumType
    AttributeName: str


class CompromisedCredentialsActionsTypeTypeDef(TypedDict):
    EventAction: CompromisedCredentialsEventActionType


class _RequiredCompromisedCredentialsRiskConfigurationTypeTypeDef(TypedDict):
    Actions: "CompromisedCredentialsActionsTypeTypeDef"


class CompromisedCredentialsRiskConfigurationTypeTypeDef(
    _RequiredCompromisedCredentialsRiskConfigurationTypeTypeDef, total=False
):
    EventFilter: List[EventFilterType]


class ConfirmDeviceResponseTypeDef(TypedDict, total=False):
    UserConfirmationNecessary: bool


class _RequiredContextDataTypeTypeDef(TypedDict):
    IpAddress: str
    ServerName: str
    ServerPath: str
    HttpHeaders: List["HttpHeaderTypeDef"]


class ContextDataTypeTypeDef(_RequiredContextDataTypeTypeDef, total=False):
    EncodedData: str


class CreateGroupResponseTypeDef(TypedDict, total=False):
    Group: "GroupTypeTypeDef"


class CreateIdentityProviderResponseTypeDef(TypedDict):
    IdentityProvider: "IdentityProviderTypeTypeDef"


class CreateResourceServerResponseTypeDef(TypedDict):
    ResourceServer: "ResourceServerTypeTypeDef"


class CreateUserImportJobResponseTypeDef(TypedDict, total=False):
    UserImportJob: "UserImportJobTypeTypeDef"


class CreateUserPoolClientResponseTypeDef(TypedDict, total=False):
    UserPoolClient: "UserPoolClientTypeTypeDef"


class CreateUserPoolDomainResponseTypeDef(TypedDict, total=False):
    CloudFrontDomain: str


class CreateUserPoolResponseTypeDef(TypedDict, total=False):
    UserPool: "UserPoolTypeTypeDef"


class CustomDomainConfigTypeTypeDef(TypedDict):
    CertificateArn: str


class CustomEmailLambdaVersionConfigTypeTypeDef(TypedDict):
    LambdaVersion: Literal["V1_0"]
    LambdaArn: str


class CustomSMSLambdaVersionConfigTypeTypeDef(TypedDict):
    LambdaVersion: Literal["V1_0"]
    LambdaArn: str


class DescribeIdentityProviderResponseTypeDef(TypedDict):
    IdentityProvider: "IdentityProviderTypeTypeDef"


class DescribeResourceServerResponseTypeDef(TypedDict):
    ResourceServer: "ResourceServerTypeTypeDef"


class DescribeRiskConfigurationResponseTypeDef(TypedDict):
    RiskConfiguration: "RiskConfigurationTypeTypeDef"


class DescribeUserImportJobResponseTypeDef(TypedDict, total=False):
    UserImportJob: "UserImportJobTypeTypeDef"


class DescribeUserPoolClientResponseTypeDef(TypedDict, total=False):
    UserPoolClient: "UserPoolClientTypeTypeDef"


class DescribeUserPoolDomainResponseTypeDef(TypedDict, total=False):
    DomainDescription: "DomainDescriptionTypeTypeDef"


class DescribeUserPoolResponseTypeDef(TypedDict, total=False):
    UserPool: "UserPoolTypeTypeDef"


class DeviceConfigurationTypeTypeDef(TypedDict, total=False):
    ChallengeRequiredOnNewDevice: bool
    DeviceOnlyRememberedOnUserPrompt: bool


class DeviceSecretVerifierConfigTypeTypeDef(TypedDict, total=False):
    PasswordVerifier: str
    Salt: str


class DeviceTypeTypeDef(TypedDict, total=False):
    DeviceKey: str
    DeviceAttributes: List["AttributeTypeTypeDef"]
    DeviceCreateDate: datetime
    DeviceLastModifiedDate: datetime
    DeviceLastAuthenticatedDate: datetime


class DomainDescriptionTypeTypeDef(TypedDict, total=False):
    UserPoolId: str
    AWSAccountId: str
    Domain: str
    S3Bucket: str
    CloudFrontDistribution: str
    Version: str
    Status: DomainStatusType
    CustomDomainConfig: "CustomDomainConfigTypeTypeDef"


class EmailConfigurationTypeTypeDef(TypedDict, total=False):
    SourceArn: str
    ReplyToEmailAddress: str
    EmailSendingAccount: EmailSendingAccountType
    From: str
    ConfigurationSet: str


class EventContextDataTypeTypeDef(TypedDict, total=False):
    IpAddress: str
    DeviceName: str
    Timezone: str
    City: str
    Country: str


class _RequiredEventFeedbackTypeTypeDef(TypedDict):
    FeedbackValue: FeedbackValueType
    Provider: str


class EventFeedbackTypeTypeDef(_RequiredEventFeedbackTypeTypeDef, total=False):
    FeedbackDate: datetime


class EventRiskTypeTypeDef(TypedDict, total=False):
    RiskDecision: RiskDecisionType
    RiskLevel: RiskLevelType
    CompromisedCredentialsDetected: bool


class ForgotPasswordResponseTypeDef(TypedDict, total=False):
    CodeDeliveryDetails: "CodeDeliveryDetailsTypeTypeDef"


class GetCSVHeaderResponseTypeDef(TypedDict, total=False):
    UserPoolId: str
    CSVHeader: List[str]


class GetDeviceResponseTypeDef(TypedDict):
    Device: "DeviceTypeTypeDef"


class GetGroupResponseTypeDef(TypedDict, total=False):
    Group: "GroupTypeTypeDef"


class GetIdentityProviderByIdentifierResponseTypeDef(TypedDict):
    IdentityProvider: "IdentityProviderTypeTypeDef"


class GetSigningCertificateResponseTypeDef(TypedDict, total=False):
    Certificate: str


class GetUICustomizationResponseTypeDef(TypedDict):
    UICustomization: "UICustomizationTypeTypeDef"


class GetUserAttributeVerificationCodeResponseTypeDef(TypedDict, total=False):
    CodeDeliveryDetails: "CodeDeliveryDetailsTypeTypeDef"


class GetUserPoolMfaConfigResponseTypeDef(TypedDict, total=False):
    SmsMfaConfiguration: "SmsMfaConfigTypeTypeDef"
    SoftwareTokenMfaConfiguration: "SoftwareTokenMfaConfigTypeTypeDef"
    MfaConfiguration: UserPoolMfaType


class _RequiredGetUserResponseTypeDef(TypedDict):
    Username: str
    UserAttributes: List["AttributeTypeTypeDef"]


class GetUserResponseTypeDef(_RequiredGetUserResponseTypeDef, total=False):
    MFAOptions: List["MFAOptionTypeTypeDef"]
    PreferredMfaSetting: str
    UserMFASettingList: List[str]


class GroupTypeTypeDef(TypedDict, total=False):
    GroupName: str
    UserPoolId: str
    Description: str
    RoleArn: str
    Precedence: int
    LastModifiedDate: datetime
    CreationDate: datetime


class HttpHeaderTypeDef(TypedDict, total=False):
    headerName: str
    headerValue: str


class IdentityProviderTypeTypeDef(TypedDict, total=False):
    UserPoolId: str
    ProviderName: str
    ProviderType: IdentityProviderTypeType
    ProviderDetails: Dict[str, str]
    AttributeMapping: Dict[str, str]
    IdpIdentifiers: List[str]
    LastModifiedDate: datetime
    CreationDate: datetime


class InitiateAuthResponseTypeDef(TypedDict, total=False):
    ChallengeName: ChallengeNameType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: "AuthenticationResultTypeTypeDef"


class LambdaConfigTypeTypeDef(TypedDict, total=False):
    PreSignUp: str
    CustomMessage: str
    PostConfirmation: str
    PreAuthentication: str
    PostAuthentication: str
    DefineAuthChallenge: str
    CreateAuthChallenge: str
    VerifyAuthChallengeResponse: str
    PreTokenGeneration: str
    UserMigration: str
    CustomSMSSender: "CustomSMSLambdaVersionConfigTypeTypeDef"
    CustomEmailSender: "CustomEmailLambdaVersionConfigTypeTypeDef"
    KMSKeyID: str


class ListDevicesResponseTypeDef(TypedDict, total=False):
    Devices: List["DeviceTypeTypeDef"]
    PaginationToken: str


class ListGroupsResponseTypeDef(TypedDict, total=False):
    Groups: List["GroupTypeTypeDef"]
    NextToken: str


class _RequiredListIdentityProvidersResponseTypeDef(TypedDict):
    Providers: List["ProviderDescriptionTypeDef"]


class ListIdentityProvidersResponseTypeDef(
    _RequiredListIdentityProvidersResponseTypeDef, total=False
):
    NextToken: str


class _RequiredListResourceServersResponseTypeDef(TypedDict):
    ResourceServers: List["ResourceServerTypeTypeDef"]


class ListResourceServersResponseTypeDef(_RequiredListResourceServersResponseTypeDef, total=False):
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class ListUserImportJobsResponseTypeDef(TypedDict, total=False):
    UserImportJobs: List["UserImportJobTypeTypeDef"]
    PaginationToken: str


class ListUserPoolClientsResponseTypeDef(TypedDict, total=False):
    UserPoolClients: List["UserPoolClientDescriptionTypeDef"]
    NextToken: str


class ListUserPoolsResponseTypeDef(TypedDict, total=False):
    UserPools: List["UserPoolDescriptionTypeTypeDef"]
    NextToken: str


class ListUsersInGroupResponseTypeDef(TypedDict, total=False):
    Users: List["UserTypeTypeDef"]
    NextToken: str


class ListUsersResponseTypeDef(TypedDict, total=False):
    Users: List["UserTypeTypeDef"]
    PaginationToken: str


class MFAOptionTypeTypeDef(TypedDict, total=False):
    DeliveryMedium: DeliveryMediumType
    AttributeName: str


class MessageTemplateTypeTypeDef(TypedDict, total=False):
    SMSMessage: str
    EmailMessage: str
    EmailSubject: str


class NewDeviceMetadataTypeTypeDef(TypedDict, total=False):
    DeviceKey: str
    DeviceGroupKey: str


class _RequiredNotifyConfigurationTypeTypeDef(TypedDict):
    SourceArn: str


class NotifyConfigurationTypeTypeDef(_RequiredNotifyConfigurationTypeTypeDef, total=False):
    From: str
    ReplyTo: str
    BlockEmail: "NotifyEmailTypeTypeDef"
    NoActionEmail: "NotifyEmailTypeTypeDef"
    MfaEmail: "NotifyEmailTypeTypeDef"


class _RequiredNotifyEmailTypeTypeDef(TypedDict):
    Subject: str


class NotifyEmailTypeTypeDef(_RequiredNotifyEmailTypeTypeDef, total=False):
    HtmlBody: str
    TextBody: str


class NumberAttributeConstraintsTypeTypeDef(TypedDict, total=False):
    MinValue: str
    MaxValue: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PasswordPolicyTypeTypeDef(TypedDict, total=False):
    MinimumLength: int
    RequireUppercase: bool
    RequireLowercase: bool
    RequireNumbers: bool
    RequireSymbols: bool
    TemporaryPasswordValidityDays: int


class ProviderDescriptionTypeDef(TypedDict, total=False):
    ProviderName: str
    ProviderType: IdentityProviderTypeType
    LastModifiedDate: datetime
    CreationDate: datetime


class ProviderUserIdentifierTypeTypeDef(TypedDict, total=False):
    ProviderName: str
    ProviderAttributeName: str
    ProviderAttributeValue: str


class RecoveryOptionTypeTypeDef(TypedDict):
    Priority: int
    Name: RecoveryOptionNameType


class ResendConfirmationCodeResponseTypeDef(TypedDict, total=False):
    CodeDeliveryDetails: "CodeDeliveryDetailsTypeTypeDef"


class ResourceServerScopeTypeTypeDef(TypedDict):
    ScopeName: str
    ScopeDescription: str


class ResourceServerTypeTypeDef(TypedDict, total=False):
    UserPoolId: str
    Identifier: str
    Name: str
    Scopes: List["ResourceServerScopeTypeTypeDef"]


class RespondToAuthChallengeResponseTypeDef(TypedDict, total=False):
    ChallengeName: ChallengeNameType
    Session: str
    ChallengeParameters: Dict[str, str]
    AuthenticationResult: "AuthenticationResultTypeTypeDef"


class RiskConfigurationTypeTypeDef(TypedDict, total=False):
    UserPoolId: str
    ClientId: str
    CompromisedCredentialsRiskConfiguration: "CompromisedCredentialsRiskConfigurationTypeTypeDef"
    AccountTakeoverRiskConfiguration: "AccountTakeoverRiskConfigurationTypeTypeDef"
    RiskExceptionConfiguration: "RiskExceptionConfigurationTypeTypeDef"
    LastModifiedDate: datetime


class RiskExceptionConfigurationTypeTypeDef(TypedDict, total=False):
    BlockedIPRangeList: List[str]
    SkippedIPRangeList: List[str]


class SMSMfaSettingsTypeTypeDef(TypedDict, total=False):
    Enabled: bool
    PreferredMfa: bool


class SchemaAttributeTypeTypeDef(TypedDict, total=False):
    Name: str
    AttributeDataType: AttributeDataType
    DeveloperOnlyAttribute: bool
    Mutable: bool
    Required: bool
    NumberAttributeConstraints: "NumberAttributeConstraintsTypeTypeDef"
    StringAttributeConstraints: "StringAttributeConstraintsTypeTypeDef"


class SetRiskConfigurationResponseTypeDef(TypedDict):
    RiskConfiguration: "RiskConfigurationTypeTypeDef"


class SetUICustomizationResponseTypeDef(TypedDict):
    UICustomization: "UICustomizationTypeTypeDef"


class SetUserPoolMfaConfigResponseTypeDef(TypedDict, total=False):
    SmsMfaConfiguration: "SmsMfaConfigTypeTypeDef"
    SoftwareTokenMfaConfiguration: "SoftwareTokenMfaConfigTypeTypeDef"
    MfaConfiguration: UserPoolMfaType


class _RequiredSignUpResponseTypeDef(TypedDict):
    UserConfirmed: bool
    UserSub: str


class SignUpResponseTypeDef(_RequiredSignUpResponseTypeDef, total=False):
    CodeDeliveryDetails: "CodeDeliveryDetailsTypeTypeDef"


class _RequiredSmsConfigurationTypeTypeDef(TypedDict):
    SnsCallerArn: str


class SmsConfigurationTypeTypeDef(_RequiredSmsConfigurationTypeTypeDef, total=False):
    ExternalId: str


class SmsMfaConfigTypeTypeDef(TypedDict, total=False):
    SmsAuthenticationMessage: str
    SmsConfiguration: "SmsConfigurationTypeTypeDef"


class SoftwareTokenMfaConfigTypeTypeDef(TypedDict, total=False):
    Enabled: bool


class SoftwareTokenMfaSettingsTypeTypeDef(TypedDict, total=False):
    Enabled: bool
    PreferredMfa: bool


class StartUserImportJobResponseTypeDef(TypedDict, total=False):
    UserImportJob: "UserImportJobTypeTypeDef"


class StopUserImportJobResponseTypeDef(TypedDict, total=False):
    UserImportJob: "UserImportJobTypeTypeDef"


class StringAttributeConstraintsTypeTypeDef(TypedDict, total=False):
    MinLength: str
    MaxLength: str


class TokenValidityUnitsTypeTypeDef(TypedDict, total=False):
    AccessToken: TimeUnitsType
    IdToken: TimeUnitsType
    RefreshToken: TimeUnitsType


class UICustomizationTypeTypeDef(TypedDict, total=False):
    UserPoolId: str
    ClientId: str
    ImageUrl: str
    CSS: str
    CSSVersion: str
    LastModifiedDate: datetime
    CreationDate: datetime


class UpdateGroupResponseTypeDef(TypedDict, total=False):
    Group: "GroupTypeTypeDef"


class UpdateIdentityProviderResponseTypeDef(TypedDict):
    IdentityProvider: "IdentityProviderTypeTypeDef"


class UpdateResourceServerResponseTypeDef(TypedDict):
    ResourceServer: "ResourceServerTypeTypeDef"


class UpdateUserAttributesResponseTypeDef(TypedDict, total=False):
    CodeDeliveryDetailsList: List["CodeDeliveryDetailsTypeTypeDef"]


class UpdateUserPoolClientResponseTypeDef(TypedDict, total=False):
    UserPoolClient: "UserPoolClientTypeTypeDef"


class UpdateUserPoolDomainResponseTypeDef(TypedDict, total=False):
    CloudFrontDomain: str


class UserContextDataTypeTypeDef(TypedDict, total=False):
    EncodedData: str


class UserImportJobTypeTypeDef(TypedDict, total=False):
    JobName: str
    JobId: str
    UserPoolId: str
    PreSignedUrl: str
    CreationDate: datetime
    StartDate: datetime
    CompletionDate: datetime
    Status: UserImportJobStatusType
    CloudWatchLogsRoleArn: str
    ImportedUsers: int
    SkippedUsers: int
    FailedUsers: int
    CompletionMessage: str


class UserPoolAddOnsTypeTypeDef(TypedDict):
    AdvancedSecurityMode: AdvancedSecurityModeType


class UserPoolClientDescriptionTypeDef(TypedDict, total=False):
    ClientId: str
    UserPoolId: str
    ClientName: str


class UserPoolClientTypeTypeDef(TypedDict, total=False):
    UserPoolId: str
    ClientName: str
    ClientId: str
    ClientSecret: str
    LastModifiedDate: datetime
    CreationDate: datetime
    RefreshTokenValidity: int
    AccessTokenValidity: int
    IdTokenValidity: int
    TokenValidityUnits: "TokenValidityUnitsTypeTypeDef"
    ReadAttributes: List[str]
    WriteAttributes: List[str]
    ExplicitAuthFlows: List[ExplicitAuthFlowsType]
    SupportedIdentityProviders: List[str]
    CallbackURLs: List[str]
    LogoutURLs: List[str]
    DefaultRedirectURI: str
    AllowedOAuthFlows: List[OAuthFlowType]
    AllowedOAuthScopes: List[str]
    AllowedOAuthFlowsUserPoolClient: bool
    AnalyticsConfiguration: "AnalyticsConfigurationTypeTypeDef"
    PreventUserExistenceErrors: PreventUserExistenceErrorTypes


class UserPoolDescriptionTypeTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    LambdaConfig: "LambdaConfigTypeTypeDef"
    Status: StatusType
    LastModifiedDate: datetime
    CreationDate: datetime


class UserPoolPolicyTypeTypeDef(TypedDict, total=False):
    PasswordPolicy: "PasswordPolicyTypeTypeDef"


class UserPoolTypeTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Policies: "UserPoolPolicyTypeTypeDef"
    LambdaConfig: "LambdaConfigTypeTypeDef"
    Status: StatusType
    LastModifiedDate: datetime
    CreationDate: datetime
    SchemaAttributes: List["SchemaAttributeTypeTypeDef"]
    AutoVerifiedAttributes: List[VerifiedAttributeType]
    AliasAttributes: List[AliasAttributeType]
    UsernameAttributes: List[UsernameAttributeType]
    SmsVerificationMessage: str
    EmailVerificationMessage: str
    EmailVerificationSubject: str
    VerificationMessageTemplate: "VerificationMessageTemplateTypeTypeDef"
    SmsAuthenticationMessage: str
    MfaConfiguration: UserPoolMfaType
    DeviceConfiguration: "DeviceConfigurationTypeTypeDef"
    EstimatedNumberOfUsers: int
    EmailConfiguration: "EmailConfigurationTypeTypeDef"
    SmsConfiguration: "SmsConfigurationTypeTypeDef"
    UserPoolTags: Dict[str, str]
    SmsConfigurationFailure: str
    EmailConfigurationFailure: str
    Domain: str
    CustomDomain: str
    AdminCreateUserConfig: "AdminCreateUserConfigTypeTypeDef"
    UserPoolAddOns: "UserPoolAddOnsTypeTypeDef"
    UsernameConfiguration: "UsernameConfigurationTypeTypeDef"
    Arn: str
    AccountRecoverySetting: "AccountRecoverySettingTypeTypeDef"


class UserTypeTypeDef(TypedDict, total=False):
    Username: str
    Attributes: List["AttributeTypeTypeDef"]
    UserCreateDate: datetime
    UserLastModifiedDate: datetime
    Enabled: bool
    UserStatus: UserStatusType
    MFAOptions: List["MFAOptionTypeTypeDef"]


class UsernameConfigurationTypeTypeDef(TypedDict):
    CaseSensitive: bool


class VerificationMessageTemplateTypeTypeDef(TypedDict, total=False):
    SmsMessage: str
    EmailMessage: str
    EmailSubject: str
    EmailMessageByLink: str
    EmailSubjectByLink: str
    DefaultEmailOption: DefaultEmailOptionType


class VerifySoftwareTokenResponseTypeDef(TypedDict, total=False):
    Status: VerifySoftwareTokenResponseType
    Session: str
