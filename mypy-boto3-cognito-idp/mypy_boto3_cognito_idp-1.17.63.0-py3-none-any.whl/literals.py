"""
Type annotations for cognito-idp service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/literals.html)

Usage::

    ```python
    from mypy_boto3_cognito_idp.literals import AccountTakeoverEventActionType

    data: AccountTakeoverEventActionType = "BLOCK"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccountTakeoverEventActionType",
    "AdminListGroupsForUserPaginatorName",
    "AdminListUserAuthEventsPaginatorName",
    "AdvancedSecurityModeType",
    "AliasAttributeType",
    "AttributeDataType",
    "AuthFlowType",
    "ChallengeName",
    "ChallengeNameType",
    "ChallengeResponse",
    "CompromisedCredentialsEventActionType",
    "CustomEmailSenderLambdaVersionType",
    "CustomSMSSenderLambdaVersionType",
    "DefaultEmailOptionType",
    "DeliveryMediumType",
    "DeviceRememberedStatusType",
    "DomainStatusType",
    "EmailSendingAccountType",
    "EventFilterType",
    "EventResponseType",
    "EventType",
    "ExplicitAuthFlowsType",
    "FeedbackValueType",
    "IdentityProviderTypeType",
    "ListGroupsPaginatorName",
    "ListIdentityProvidersPaginatorName",
    "ListResourceServersPaginatorName",
    "ListUserPoolClientsPaginatorName",
    "ListUserPoolsPaginatorName",
    "ListUsersInGroupPaginatorName",
    "ListUsersPaginatorName",
    "MessageActionType",
    "OAuthFlowType",
    "PreventUserExistenceErrorTypes",
    "RecoveryOptionNameType",
    "RiskDecisionType",
    "RiskLevelType",
    "StatusType",
    "TimeUnitsType",
    "UserImportJobStatusType",
    "UserPoolMfaType",
    "UserStatusType",
    "UsernameAttributeType",
    "VerifiedAttributeType",
    "VerifySoftwareTokenResponseType",
)


AccountTakeoverEventActionType = Literal["BLOCK", "MFA_IF_CONFIGURED", "MFA_REQUIRED", "NO_ACTION"]
AdminListGroupsForUserPaginatorName = Literal["admin_list_groups_for_user"]
AdminListUserAuthEventsPaginatorName = Literal["admin_list_user_auth_events"]
AdvancedSecurityModeType = Literal["AUDIT", "ENFORCED", "OFF"]
AliasAttributeType = Literal["email", "phone_number", "preferred_username"]
AttributeDataType = Literal["Boolean", "DateTime", "Number", "String"]
AuthFlowType = Literal[
    "ADMIN_NO_SRP_AUTH",
    "ADMIN_USER_PASSWORD_AUTH",
    "CUSTOM_AUTH",
    "REFRESH_TOKEN",
    "REFRESH_TOKEN_AUTH",
    "USER_PASSWORD_AUTH",
    "USER_SRP_AUTH",
]
ChallengeName = Literal["Mfa", "Password"]
ChallengeNameType = Literal[
    "ADMIN_NO_SRP_AUTH",
    "CUSTOM_CHALLENGE",
    "DEVICE_PASSWORD_VERIFIER",
    "DEVICE_SRP_AUTH",
    "MFA_SETUP",
    "NEW_PASSWORD_REQUIRED",
    "PASSWORD_VERIFIER",
    "SELECT_MFA_TYPE",
    "SMS_MFA",
    "SOFTWARE_TOKEN_MFA",
]
ChallengeResponse = Literal["Failure", "Success"]
CompromisedCredentialsEventActionType = Literal["BLOCK", "NO_ACTION"]
CustomEmailSenderLambdaVersionType = Literal["V1_0"]
CustomSMSSenderLambdaVersionType = Literal["V1_0"]
DefaultEmailOptionType = Literal["CONFIRM_WITH_CODE", "CONFIRM_WITH_LINK"]
DeliveryMediumType = Literal["EMAIL", "SMS"]
DeviceRememberedStatusType = Literal["not_remembered", "remembered"]
DomainStatusType = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
EmailSendingAccountType = Literal["COGNITO_DEFAULT", "DEVELOPER"]
EventFilterType = Literal["PASSWORD_CHANGE", "SIGN_IN", "SIGN_UP"]
EventResponseType = Literal["Failure", "Success"]
EventType = Literal["ForgotPassword", "SignIn", "SignUp"]
ExplicitAuthFlowsType = Literal[
    "ADMIN_NO_SRP_AUTH",
    "ALLOW_ADMIN_USER_PASSWORD_AUTH",
    "ALLOW_CUSTOM_AUTH",
    "ALLOW_REFRESH_TOKEN_AUTH",
    "ALLOW_USER_PASSWORD_AUTH",
    "ALLOW_USER_SRP_AUTH",
    "CUSTOM_AUTH_FLOW_ONLY",
    "USER_PASSWORD_AUTH",
]
FeedbackValueType = Literal["Invalid", "Valid"]
IdentityProviderTypeType = Literal[
    "Facebook", "Google", "LoginWithAmazon", "OIDC", "SAML", "SignInWithApple"
]
ListGroupsPaginatorName = Literal["list_groups"]
ListIdentityProvidersPaginatorName = Literal["list_identity_providers"]
ListResourceServersPaginatorName = Literal["list_resource_servers"]
ListUserPoolClientsPaginatorName = Literal["list_user_pool_clients"]
ListUserPoolsPaginatorName = Literal["list_user_pools"]
ListUsersInGroupPaginatorName = Literal["list_users_in_group"]
ListUsersPaginatorName = Literal["list_users"]
MessageActionType = Literal["RESEND", "SUPPRESS"]
OAuthFlowType = Literal["client_credentials", "code", "implicit"]
PreventUserExistenceErrorTypes = Literal["ENABLED", "LEGACY"]
RecoveryOptionNameType = Literal["admin_only", "verified_email", "verified_phone_number"]
RiskDecisionType = Literal["AccountTakeover", "Block", "NoRisk"]
RiskLevelType = Literal["High", "Low", "Medium"]
StatusType = Literal["Disabled", "Enabled"]
TimeUnitsType = Literal["days", "hours", "minutes", "seconds"]
UserImportJobStatusType = Literal[
    "Created", "Expired", "Failed", "InProgress", "Pending", "Stopped", "Stopping", "Succeeded"
]
UserPoolMfaType = Literal["OFF", "ON", "OPTIONAL"]
UserStatusType = Literal[
    "ARCHIVED",
    "COMPROMISED",
    "CONFIRMED",
    "FORCE_CHANGE_PASSWORD",
    "RESET_REQUIRED",
    "UNCONFIRMED",
    "UNKNOWN",
]
UsernameAttributeType = Literal["email", "phone_number"]
VerifiedAttributeType = Literal["email", "phone_number"]
VerifySoftwareTokenResponseType = Literal["ERROR", "SUCCESS"]
