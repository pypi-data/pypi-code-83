"""
Type annotations for cognito-idp service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_cognito_idp import CognitoIdentityProviderClient

    client: CognitoIdentityProviderClient = boto3.client("cognito-idp")
    ```
"""
import sys
from typing import IO, Any, Dict, List, Type, Union, overload

from botocore.client import ClientMeta

from mypy_boto3_cognito_idp.literals import (
    AliasAttributeType,
    AuthFlowType,
    ChallengeNameType,
    DeliveryMediumType,
    DeviceRememberedStatusType,
    ExplicitAuthFlowsType,
    FeedbackValueType,
    IdentityProviderTypeType,
    MessageActionType,
    OAuthFlowType,
    PreventUserExistenceErrorTypes,
    UsernameAttributeType,
    UserPoolMfaType,
    VerifiedAttributeType,
)
from mypy_boto3_cognito_idp.paginator import (
    AdminListGroupsForUserPaginator,
    AdminListUserAuthEventsPaginator,
    ListGroupsPaginator,
    ListIdentityProvidersPaginator,
    ListResourceServersPaginator,
    ListUserPoolClientsPaginator,
    ListUserPoolsPaginator,
    ListUsersInGroupPaginator,
    ListUsersPaginator,
)
from mypy_boto3_cognito_idp.type_defs import (
    AccountRecoverySettingTypeTypeDef,
    AccountTakeoverRiskConfigurationTypeTypeDef,
    AdminCreateUserConfigTypeTypeDef,
    AdminCreateUserResponseTypeDef,
    AdminGetDeviceResponseTypeDef,
    AdminGetUserResponseTypeDef,
    AdminInitiateAuthResponseTypeDef,
    AdminListDevicesResponseTypeDef,
    AdminListGroupsForUserResponseTypeDef,
    AdminListUserAuthEventsResponseTypeDef,
    AdminRespondToAuthChallengeResponseTypeDef,
    AnalyticsConfigurationTypeTypeDef,
    AnalyticsMetadataTypeTypeDef,
    AssociateSoftwareTokenResponseTypeDef,
    AttributeTypeTypeDef,
    CompromisedCredentialsRiskConfigurationTypeTypeDef,
    ConfirmDeviceResponseTypeDef,
    ContextDataTypeTypeDef,
    CreateGroupResponseTypeDef,
    CreateIdentityProviderResponseTypeDef,
    CreateResourceServerResponseTypeDef,
    CreateUserImportJobResponseTypeDef,
    CreateUserPoolClientResponseTypeDef,
    CreateUserPoolDomainResponseTypeDef,
    CreateUserPoolResponseTypeDef,
    CustomDomainConfigTypeTypeDef,
    DescribeIdentityProviderResponseTypeDef,
    DescribeResourceServerResponseTypeDef,
    DescribeRiskConfigurationResponseTypeDef,
    DescribeUserImportJobResponseTypeDef,
    DescribeUserPoolClientResponseTypeDef,
    DescribeUserPoolDomainResponseTypeDef,
    DescribeUserPoolResponseTypeDef,
    DeviceConfigurationTypeTypeDef,
    DeviceSecretVerifierConfigTypeTypeDef,
    EmailConfigurationTypeTypeDef,
    ForgotPasswordResponseTypeDef,
    GetCSVHeaderResponseTypeDef,
    GetDeviceResponseTypeDef,
    GetGroupResponseTypeDef,
    GetIdentityProviderByIdentifierResponseTypeDef,
    GetSigningCertificateResponseTypeDef,
    GetUICustomizationResponseTypeDef,
    GetUserAttributeVerificationCodeResponseTypeDef,
    GetUserPoolMfaConfigResponseTypeDef,
    GetUserResponseTypeDef,
    InitiateAuthResponseTypeDef,
    LambdaConfigTypeTypeDef,
    ListDevicesResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListResourceServersResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListUserImportJobsResponseTypeDef,
    ListUserPoolClientsResponseTypeDef,
    ListUserPoolsResponseTypeDef,
    ListUsersInGroupResponseTypeDef,
    ListUsersResponseTypeDef,
    MFAOptionTypeTypeDef,
    ProviderUserIdentifierTypeTypeDef,
    ResendConfirmationCodeResponseTypeDef,
    ResourceServerScopeTypeTypeDef,
    RespondToAuthChallengeResponseTypeDef,
    RiskExceptionConfigurationTypeTypeDef,
    SchemaAttributeTypeTypeDef,
    SetRiskConfigurationResponseTypeDef,
    SetUICustomizationResponseTypeDef,
    SetUserPoolMfaConfigResponseTypeDef,
    SignUpResponseTypeDef,
    SmsConfigurationTypeTypeDef,
    SmsMfaConfigTypeTypeDef,
    SMSMfaSettingsTypeTypeDef,
    SoftwareTokenMfaConfigTypeTypeDef,
    SoftwareTokenMfaSettingsTypeTypeDef,
    StartUserImportJobResponseTypeDef,
    StopUserImportJobResponseTypeDef,
    TokenValidityUnitsTypeTypeDef,
    UpdateGroupResponseTypeDef,
    UpdateIdentityProviderResponseTypeDef,
    UpdateResourceServerResponseTypeDef,
    UpdateUserAttributesResponseTypeDef,
    UpdateUserPoolClientResponseTypeDef,
    UpdateUserPoolDomainResponseTypeDef,
    UserContextDataTypeTypeDef,
    UsernameConfigurationTypeTypeDef,
    UserPoolAddOnsTypeTypeDef,
    UserPoolPolicyTypeTypeDef,
    VerificationMessageTemplateTypeTypeDef,
    VerifySoftwareTokenResponseTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("CognitoIdentityProviderClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AliasExistsException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    CodeDeliveryFailureException: Type[BotocoreClientError]
    CodeMismatchException: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    DuplicateProviderException: Type[BotocoreClientError]
    EnableSoftwareTokenMFAException: Type[BotocoreClientError]
    ExpiredCodeException: Type[BotocoreClientError]
    GroupExistsException: Type[BotocoreClientError]
    InternalErrorException: Type[BotocoreClientError]
    InvalidEmailRoleAccessPolicyException: Type[BotocoreClientError]
    InvalidLambdaResponseException: Type[BotocoreClientError]
    InvalidOAuthFlowException: Type[BotocoreClientError]
    InvalidParameterException: Type[BotocoreClientError]
    InvalidPasswordException: Type[BotocoreClientError]
    InvalidSmsRoleAccessPolicyException: Type[BotocoreClientError]
    InvalidSmsRoleTrustRelationshipException: Type[BotocoreClientError]
    InvalidUserPoolConfigurationException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    MFAMethodNotFoundException: Type[BotocoreClientError]
    NotAuthorizedException: Type[BotocoreClientError]
    PasswordResetRequiredException: Type[BotocoreClientError]
    PreconditionNotMetException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ScopeDoesNotExistException: Type[BotocoreClientError]
    SoftwareTokenMFANotFoundException: Type[BotocoreClientError]
    TooManyFailedAttemptsException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnexpectedLambdaException: Type[BotocoreClientError]
    UnsupportedIdentityProviderException: Type[BotocoreClientError]
    UnsupportedUserStateException: Type[BotocoreClientError]
    UserImportInProgressException: Type[BotocoreClientError]
    UserLambdaValidationException: Type[BotocoreClientError]
    UserNotConfirmedException: Type[BotocoreClientError]
    UserNotFoundException: Type[BotocoreClientError]
    UserPoolAddOnNotEnabledException: Type[BotocoreClientError]
    UserPoolTaggingException: Type[BotocoreClientError]
    UsernameExistsException: Type[BotocoreClientError]


class CognitoIdentityProviderClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_custom_attributes(
        self, UserPoolId: str, CustomAttributes: List["SchemaAttributeTypeTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.add_custom_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#add-custom-attributes)
        """

    def admin_add_user_to_group(self, UserPoolId: str, Username: str, GroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_add_user_to_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-add-user-to-group)
        """

    def admin_confirm_sign_up(
        self, UserPoolId: str, Username: str, ClientMetadata: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_confirm_sign_up)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-confirm-sign-up)
        """

    def admin_create_user(
        self,
        UserPoolId: str,
        Username: str,
        UserAttributes: List["AttributeTypeTypeDef"] = None,
        ValidationData: List["AttributeTypeTypeDef"] = None,
        TemporaryPassword: str = None,
        ForceAliasCreation: bool = None,
        MessageAction: MessageActionType = None,
        DesiredDeliveryMediums: List[DeliveryMediumType] = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> AdminCreateUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-create-user)
        """

    def admin_delete_user(self, UserPoolId: str, Username: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-delete-user)
        """

    def admin_delete_user_attributes(
        self, UserPoolId: str, Username: str, UserAttributeNames: List[str]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_delete_user_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-delete-user-attributes)
        """

    def admin_disable_provider_for_user(
        self, UserPoolId: str, User: ProviderUserIdentifierTypeTypeDef
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_disable_provider_for_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-disable-provider-for-user)
        """

    def admin_disable_user(self, UserPoolId: str, Username: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_disable_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-disable-user)
        """

    def admin_enable_user(self, UserPoolId: str, Username: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_enable_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-enable-user)
        """

    def admin_forget_device(self, UserPoolId: str, Username: str, DeviceKey: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_forget_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-forget-device)
        """

    def admin_get_device(
        self, DeviceKey: str, UserPoolId: str, Username: str
    ) -> AdminGetDeviceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_get_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-get-device)
        """

    def admin_get_user(self, UserPoolId: str, Username: str) -> AdminGetUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_get_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-get-user)
        """

    def admin_initiate_auth(
        self,
        UserPoolId: str,
        ClientId: str,
        AuthFlow: AuthFlowType,
        AuthParameters: Dict[str, str] = None,
        ClientMetadata: Dict[str, str] = None,
        AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
        ContextData: ContextDataTypeTypeDef = None,
    ) -> AdminInitiateAuthResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_initiate_auth)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-initiate-auth)
        """

    def admin_link_provider_for_user(
        self,
        UserPoolId: str,
        DestinationUser: ProviderUserIdentifierTypeTypeDef,
        SourceUser: ProviderUserIdentifierTypeTypeDef,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_link_provider_for_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-link-provider-for-user)
        """

    def admin_list_devices(
        self, UserPoolId: str, Username: str, Limit: int = None, PaginationToken: str = None
    ) -> AdminListDevicesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_list_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-list-devices)
        """

    def admin_list_groups_for_user(
        self, Username: str, UserPoolId: str, Limit: int = None, NextToken: str = None
    ) -> AdminListGroupsForUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_list_groups_for_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-list-groups-for-user)
        """

    def admin_list_user_auth_events(
        self, UserPoolId: str, Username: str, MaxResults: int = None, NextToken: str = None
    ) -> AdminListUserAuthEventsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_list_user_auth_events)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-list-user-auth-events)
        """

    def admin_remove_user_from_group(self, UserPoolId: str, Username: str, GroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_remove_user_from_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-remove-user-from-group)
        """

    def admin_reset_user_password(
        self, UserPoolId: str, Username: str, ClientMetadata: Dict[str, str] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_reset_user_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-reset-user-password)
        """

    def admin_respond_to_auth_challenge(
        self,
        UserPoolId: str,
        ClientId: str,
        ChallengeName: ChallengeNameType,
        ChallengeResponses: Dict[str, str] = None,
        Session: str = None,
        AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
        ContextData: ContextDataTypeTypeDef = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> AdminRespondToAuthChallengeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_respond_to_auth_challenge)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-respond-to-auth-challenge)
        """

    def admin_set_user_mfa_preference(
        self,
        Username: str,
        UserPoolId: str,
        SMSMfaSettings: SMSMfaSettingsTypeTypeDef = None,
        SoftwareTokenMfaSettings: SoftwareTokenMfaSettingsTypeTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_set_user_mfa_preference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-set-user-mfa-preference)
        """

    def admin_set_user_password(
        self, UserPoolId: str, Username: str, Password: str, Permanent: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_set_user_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-set-user-password)
        """

    def admin_set_user_settings(
        self, UserPoolId: str, Username: str, MFAOptions: List["MFAOptionTypeTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_set_user_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-set-user-settings)
        """

    def admin_update_auth_event_feedback(
        self, UserPoolId: str, Username: str, EventId: str, FeedbackValue: FeedbackValueType
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_update_auth_event_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-update-auth-event-feedback)
        """

    def admin_update_device_status(
        self,
        UserPoolId: str,
        Username: str,
        DeviceKey: str,
        DeviceRememberedStatus: DeviceRememberedStatusType = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_update_device_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-update-device-status)
        """

    def admin_update_user_attributes(
        self,
        UserPoolId: str,
        Username: str,
        UserAttributes: List["AttributeTypeTypeDef"],
        ClientMetadata: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_update_user_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-update-user-attributes)
        """

    def admin_user_global_sign_out(self, UserPoolId: str, Username: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.admin_user_global_sign_out)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#admin-user-global-sign-out)
        """

    def associate_software_token(
        self, AccessToken: str = None, Session: str = None
    ) -> AssociateSoftwareTokenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.associate_software_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#associate-software-token)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#can-paginate)
        """

    def change_password(
        self, PreviousPassword: str, ProposedPassword: str, AccessToken: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.change_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#change-password)
        """

    def confirm_device(
        self,
        AccessToken: str,
        DeviceKey: str,
        DeviceSecretVerifierConfig: DeviceSecretVerifierConfigTypeTypeDef = None,
        DeviceName: str = None,
    ) -> ConfirmDeviceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.confirm_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#confirm-device)
        """

    def confirm_forgot_password(
        self,
        ClientId: str,
        Username: str,
        ConfirmationCode: str,
        Password: str,
        SecretHash: str = None,
        AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
        UserContextData: UserContextDataTypeTypeDef = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.confirm_forgot_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#confirm-forgot-password)
        """

    def confirm_sign_up(
        self,
        ClientId: str,
        Username: str,
        ConfirmationCode: str,
        SecretHash: str = None,
        ForceAliasCreation: bool = None,
        AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
        UserContextData: UserContextDataTypeTypeDef = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.confirm_sign_up)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#confirm-sign-up)
        """

    def create_group(
        self,
        GroupName: str,
        UserPoolId: str,
        Description: str = None,
        RoleArn: str = None,
        Precedence: int = None,
    ) -> CreateGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#create-group)
        """

    def create_identity_provider(
        self,
        UserPoolId: str,
        ProviderName: str,
        ProviderType: IdentityProviderTypeType,
        ProviderDetails: Dict[str, str],
        AttributeMapping: Dict[str, str] = None,
        IdpIdentifiers: List[str] = None,
    ) -> CreateIdentityProviderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#create-identity-provider)
        """

    def create_resource_server(
        self,
        UserPoolId: str,
        Identifier: str,
        Name: str,
        Scopes: List["ResourceServerScopeTypeTypeDef"] = None,
    ) -> CreateResourceServerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_resource_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#create-resource-server)
        """

    def create_user_import_job(
        self, JobName: str, UserPoolId: str, CloudWatchLogsRoleArn: str
    ) -> CreateUserImportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#create-user-import-job)
        """

    def create_user_pool(
        self,
        PoolName: str,
        Policies: "UserPoolPolicyTypeTypeDef" = None,
        LambdaConfig: "LambdaConfigTypeTypeDef" = None,
        AutoVerifiedAttributes: List[VerifiedAttributeType] = None,
        AliasAttributes: List[AliasAttributeType] = None,
        UsernameAttributes: List[UsernameAttributeType] = None,
        SmsVerificationMessage: str = None,
        EmailVerificationMessage: str = None,
        EmailVerificationSubject: str = None,
        VerificationMessageTemplate: "VerificationMessageTemplateTypeTypeDef" = None,
        SmsAuthenticationMessage: str = None,
        MfaConfiguration: UserPoolMfaType = None,
        DeviceConfiguration: "DeviceConfigurationTypeTypeDef" = None,
        EmailConfiguration: "EmailConfigurationTypeTypeDef" = None,
        SmsConfiguration: "SmsConfigurationTypeTypeDef" = None,
        UserPoolTags: Dict[str, str] = None,
        AdminCreateUserConfig: "AdminCreateUserConfigTypeTypeDef" = None,
        Schema: List["SchemaAttributeTypeTypeDef"] = None,
        UserPoolAddOns: "UserPoolAddOnsTypeTypeDef" = None,
        UsernameConfiguration: "UsernameConfigurationTypeTypeDef" = None,
        AccountRecoverySetting: "AccountRecoverySettingTypeTypeDef" = None,
    ) -> CreateUserPoolResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#create-user-pool)
        """

    def create_user_pool_client(
        self,
        UserPoolId: str,
        ClientName: str,
        GenerateSecret: bool = None,
        RefreshTokenValidity: int = None,
        AccessTokenValidity: int = None,
        IdTokenValidity: int = None,
        TokenValidityUnits: "TokenValidityUnitsTypeTypeDef" = None,
        ReadAttributes: List[str] = None,
        WriteAttributes: List[str] = None,
        ExplicitAuthFlows: List[ExplicitAuthFlowsType] = None,
        SupportedIdentityProviders: List[str] = None,
        CallbackURLs: List[str] = None,
        LogoutURLs: List[str] = None,
        DefaultRedirectURI: str = None,
        AllowedOAuthFlows: List[OAuthFlowType] = None,
        AllowedOAuthScopes: List[str] = None,
        AllowedOAuthFlowsUserPoolClient: bool = None,
        AnalyticsConfiguration: "AnalyticsConfigurationTypeTypeDef" = None,
        PreventUserExistenceErrors: PreventUserExistenceErrorTypes = None,
    ) -> CreateUserPoolClientResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool_client)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#create-user-pool-client)
        """

    def create_user_pool_domain(
        self,
        Domain: str,
        UserPoolId: str,
        CustomDomainConfig: "CustomDomainConfigTypeTypeDef" = None,
    ) -> CreateUserPoolDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.create_user_pool_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#create-user-pool-domain)
        """

    def delete_group(self, GroupName: str, UserPoolId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete-group)
        """

    def delete_identity_provider(self, UserPoolId: str, ProviderName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete-identity-provider)
        """

    def delete_resource_server(self, UserPoolId: str, Identifier: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_resource_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete-resource-server)
        """

    def delete_user(self, AccessToken: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete-user)
        """

    def delete_user_attributes(
        self, UserAttributeNames: List[str], AccessToken: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete-user-attributes)
        """

    def delete_user_pool(self, UserPoolId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete-user-pool)
        """

    def delete_user_pool_client(self, UserPoolId: str, ClientId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_pool_client)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete-user-pool-client)
        """

    def delete_user_pool_domain(self, Domain: str, UserPoolId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.delete_user_pool_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#delete-user-pool-domain)
        """

    def describe_identity_provider(
        self, UserPoolId: str, ProviderName: str
    ) -> DescribeIdentityProviderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#describe-identity-provider)
        """

    def describe_resource_server(
        self, UserPoolId: str, Identifier: str
    ) -> DescribeResourceServerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_resource_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#describe-resource-server)
        """

    def describe_risk_configuration(
        self, UserPoolId: str, ClientId: str = None
    ) -> DescribeRiskConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_risk_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#describe-risk-configuration)
        """

    def describe_user_import_job(
        self, UserPoolId: str, JobId: str
    ) -> DescribeUserImportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#describe-user-import-job)
        """

    def describe_user_pool(self, UserPoolId: str) -> DescribeUserPoolResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#describe-user-pool)
        """

    def describe_user_pool_client(
        self, UserPoolId: str, ClientId: str
    ) -> DescribeUserPoolClientResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool_client)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#describe-user-pool-client)
        """

    def describe_user_pool_domain(self, Domain: str) -> DescribeUserPoolDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.describe_user_pool_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#describe-user-pool-domain)
        """

    def forget_device(self, DeviceKey: str, AccessToken: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.forget_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#forget-device)
        """

    def forgot_password(
        self,
        ClientId: str,
        Username: str,
        SecretHash: str = None,
        UserContextData: UserContextDataTypeTypeDef = None,
        AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> ForgotPasswordResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.forgot_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#forgot-password)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#generate-presigned-url)
        """

    def get_csv_header(self, UserPoolId: str) -> GetCSVHeaderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_csv_header)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get-csv-header)
        """

    def get_device(self, DeviceKey: str, AccessToken: str = None) -> GetDeviceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get-device)
        """

    def get_group(self, GroupName: str, UserPoolId: str) -> GetGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get-group)
        """

    def get_identity_provider_by_identifier(
        self, UserPoolId: str, IdpIdentifier: str
    ) -> GetIdentityProviderByIdentifierResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_identity_provider_by_identifier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get-identity-provider-by-identifier)
        """

    def get_signing_certificate(self, UserPoolId: str) -> GetSigningCertificateResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_signing_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get-signing-certificate)
        """

    def get_ui_customization(
        self, UserPoolId: str, ClientId: str = None
    ) -> GetUICustomizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_ui_customization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get-ui-customization)
        """

    def get_user(self, AccessToken: str) -> GetUserResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get-user)
        """

    def get_user_attribute_verification_code(
        self, AccessToken: str, AttributeName: str, ClientMetadata: Dict[str, str] = None
    ) -> GetUserAttributeVerificationCodeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_user_attribute_verification_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get-user-attribute-verification-code)
        """

    def get_user_pool_mfa_config(self, UserPoolId: str) -> GetUserPoolMfaConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.get_user_pool_mfa_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#get-user-pool-mfa-config)
        """

    def global_sign_out(self, AccessToken: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.global_sign_out)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#global-sign-out)
        """

    def initiate_auth(
        self,
        AuthFlow: AuthFlowType,
        ClientId: str,
        AuthParameters: Dict[str, str] = None,
        ClientMetadata: Dict[str, str] = None,
        AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
        UserContextData: UserContextDataTypeTypeDef = None,
    ) -> InitiateAuthResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.initiate_auth)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#initiate-auth)
        """

    def list_devices(
        self, AccessToken: str, Limit: int = None, PaginationToken: str = None
    ) -> ListDevicesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_devices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list-devices)
        """

    def list_groups(
        self, UserPoolId: str, Limit: int = None, NextToken: str = None
    ) -> ListGroupsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list-groups)
        """

    def list_identity_providers(
        self, UserPoolId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListIdentityProvidersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_identity_providers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list-identity-providers)
        """

    def list_resource_servers(
        self, UserPoolId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListResourceServersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_resource_servers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list-resource-servers)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list-tags-for-resource)
        """

    def list_user_import_jobs(
        self, UserPoolId: str, MaxResults: int, PaginationToken: str = None
    ) -> ListUserImportJobsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_user_import_jobs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list-user-import-jobs)
        """

    def list_user_pool_clients(
        self, UserPoolId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListUserPoolClientsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_user_pool_clients)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list-user-pool-clients)
        """

    def list_user_pools(
        self, MaxResults: int, NextToken: str = None
    ) -> ListUserPoolsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_user_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list-user-pools)
        """

    def list_users(
        self,
        UserPoolId: str,
        AttributesToGet: List[str] = None,
        Limit: int = None,
        PaginationToken: str = None,
        Filter: str = None,
    ) -> ListUsersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_users)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list-users)
        """

    def list_users_in_group(
        self, UserPoolId: str, GroupName: str, Limit: int = None, NextToken: str = None
    ) -> ListUsersInGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.list_users_in_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#list-users-in-group)
        """

    def resend_confirmation_code(
        self,
        ClientId: str,
        Username: str,
        SecretHash: str = None,
        UserContextData: UserContextDataTypeTypeDef = None,
        AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> ResendConfirmationCodeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.resend_confirmation_code)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#resend-confirmation-code)
        """

    def respond_to_auth_challenge(
        self,
        ClientId: str,
        ChallengeName: ChallengeNameType,
        Session: str = None,
        ChallengeResponses: Dict[str, str] = None,
        AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
        UserContextData: UserContextDataTypeTypeDef = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> RespondToAuthChallengeResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.respond_to_auth_challenge)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#respond-to-auth-challenge)
        """

    def set_risk_configuration(
        self,
        UserPoolId: str,
        ClientId: str = None,
        CompromisedCredentialsRiskConfiguration: "CompromisedCredentialsRiskConfigurationTypeTypeDef" = None,
        AccountTakeoverRiskConfiguration: "AccountTakeoverRiskConfigurationTypeTypeDef" = None,
        RiskExceptionConfiguration: "RiskExceptionConfigurationTypeTypeDef" = None,
    ) -> SetRiskConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_risk_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#set-risk-configuration)
        """

    def set_ui_customization(
        self,
        UserPoolId: str,
        ClientId: str = None,
        CSS: str = None,
        ImageFile: Union[bytes, IO[bytes]] = None,
    ) -> SetUICustomizationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_ui_customization)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#set-ui-customization)
        """

    def set_user_mfa_preference(
        self,
        AccessToken: str,
        SMSMfaSettings: SMSMfaSettingsTypeTypeDef = None,
        SoftwareTokenMfaSettings: SoftwareTokenMfaSettingsTypeTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_user_mfa_preference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#set-user-mfa-preference)
        """

    def set_user_pool_mfa_config(
        self,
        UserPoolId: str,
        SmsMfaConfiguration: "SmsMfaConfigTypeTypeDef" = None,
        SoftwareTokenMfaConfiguration: "SoftwareTokenMfaConfigTypeTypeDef" = None,
        MfaConfiguration: UserPoolMfaType = None,
    ) -> SetUserPoolMfaConfigResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_user_pool_mfa_config)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#set-user-pool-mfa-config)
        """

    def set_user_settings(
        self, AccessToken: str, MFAOptions: List["MFAOptionTypeTypeDef"]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.set_user_settings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#set-user-settings)
        """

    def sign_up(
        self,
        ClientId: str,
        Username: str,
        Password: str,
        SecretHash: str = None,
        UserAttributes: List["AttributeTypeTypeDef"] = None,
        ValidationData: List["AttributeTypeTypeDef"] = None,
        AnalyticsMetadata: AnalyticsMetadataTypeTypeDef = None,
        UserContextData: UserContextDataTypeTypeDef = None,
        ClientMetadata: Dict[str, str] = None,
    ) -> SignUpResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.sign_up)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#sign-up)
        """

    def start_user_import_job(
        self, UserPoolId: str, JobId: str
    ) -> StartUserImportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.start_user_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#start-user-import-job)
        """

    def stop_user_import_job(self, UserPoolId: str, JobId: str) -> StopUserImportJobResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.stop_user_import_job)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#stop-user-import-job)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#untag-resource)
        """

    def update_auth_event_feedback(
        self,
        UserPoolId: str,
        Username: str,
        EventId: str,
        FeedbackToken: str,
        FeedbackValue: FeedbackValueType,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_auth_event_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update-auth-event-feedback)
        """

    def update_device_status(
        self,
        AccessToken: str,
        DeviceKey: str,
        DeviceRememberedStatus: DeviceRememberedStatusType = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_device_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update-device-status)
        """

    def update_group(
        self,
        GroupName: str,
        UserPoolId: str,
        Description: str = None,
        RoleArn: str = None,
        Precedence: int = None,
    ) -> UpdateGroupResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update-group)
        """

    def update_identity_provider(
        self,
        UserPoolId: str,
        ProviderName: str,
        ProviderDetails: Dict[str, str] = None,
        AttributeMapping: Dict[str, str] = None,
        IdpIdentifiers: List[str] = None,
    ) -> UpdateIdentityProviderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_identity_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update-identity-provider)
        """

    def update_resource_server(
        self,
        UserPoolId: str,
        Identifier: str,
        Name: str,
        Scopes: List["ResourceServerScopeTypeTypeDef"] = None,
    ) -> UpdateResourceServerResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_resource_server)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update-resource-server)
        """

    def update_user_attributes(
        self,
        UserAttributes: List["AttributeTypeTypeDef"],
        AccessToken: str,
        ClientMetadata: Dict[str, str] = None,
    ) -> UpdateUserAttributesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update-user-attributes)
        """

    def update_user_pool(
        self,
        UserPoolId: str,
        Policies: "UserPoolPolicyTypeTypeDef" = None,
        LambdaConfig: "LambdaConfigTypeTypeDef" = None,
        AutoVerifiedAttributes: List[VerifiedAttributeType] = None,
        SmsVerificationMessage: str = None,
        EmailVerificationMessage: str = None,
        EmailVerificationSubject: str = None,
        VerificationMessageTemplate: "VerificationMessageTemplateTypeTypeDef" = None,
        SmsAuthenticationMessage: str = None,
        MfaConfiguration: UserPoolMfaType = None,
        DeviceConfiguration: "DeviceConfigurationTypeTypeDef" = None,
        EmailConfiguration: "EmailConfigurationTypeTypeDef" = None,
        SmsConfiguration: "SmsConfigurationTypeTypeDef" = None,
        UserPoolTags: Dict[str, str] = None,
        AdminCreateUserConfig: "AdminCreateUserConfigTypeTypeDef" = None,
        UserPoolAddOns: "UserPoolAddOnsTypeTypeDef" = None,
        AccountRecoverySetting: "AccountRecoverySettingTypeTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update-user-pool)
        """

    def update_user_pool_client(
        self,
        UserPoolId: str,
        ClientId: str,
        ClientName: str = None,
        RefreshTokenValidity: int = None,
        AccessTokenValidity: int = None,
        IdTokenValidity: int = None,
        TokenValidityUnits: "TokenValidityUnitsTypeTypeDef" = None,
        ReadAttributes: List[str] = None,
        WriteAttributes: List[str] = None,
        ExplicitAuthFlows: List[ExplicitAuthFlowsType] = None,
        SupportedIdentityProviders: List[str] = None,
        CallbackURLs: List[str] = None,
        LogoutURLs: List[str] = None,
        DefaultRedirectURI: str = None,
        AllowedOAuthFlows: List[OAuthFlowType] = None,
        AllowedOAuthScopes: List[str] = None,
        AllowedOAuthFlowsUserPoolClient: bool = None,
        AnalyticsConfiguration: "AnalyticsConfigurationTypeTypeDef" = None,
        PreventUserExistenceErrors: PreventUserExistenceErrorTypes = None,
    ) -> UpdateUserPoolClientResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_pool_client)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update-user-pool-client)
        """

    def update_user_pool_domain(
        self, Domain: str, UserPoolId: str, CustomDomainConfig: "CustomDomainConfigTypeTypeDef"
    ) -> UpdateUserPoolDomainResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.update_user_pool_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#update-user-pool-domain)
        """

    def verify_software_token(
        self,
        UserCode: str,
        AccessToken: str = None,
        Session: str = None,
        FriendlyDeviceName: str = None,
    ) -> VerifySoftwareTokenResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.verify_software_token)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#verify-software-token)
        """

    def verify_user_attribute(
        self, AccessToken: str, AttributeName: str, Code: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Client.verify_user_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/client.html#verify-user-attribute)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["admin_list_groups_for_user"]
    ) -> AdminListGroupsForUserPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListGroupsForUser)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#adminlistgroupsforuserpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["admin_list_user_auth_events"]
    ) -> AdminListUserAuthEventsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListUserAuthEvents)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#adminlistuserautheventspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_groups"]) -> ListGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listgroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_identity_providers"]
    ) -> ListIdentityProvidersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListIdentityProviders)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listidentityproviderspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_servers"]
    ) -> ListResourceServersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListResourceServers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listresourceserverspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_user_pool_clients"]
    ) -> ListUserPoolClientsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPoolClients)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listuserpoolclientspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_user_pools"]) -> ListUserPoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPools)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listuserpoolspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_users"]) -> ListUsersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listuserspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_users_in_group"]
    ) -> ListUsersInGroupPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsersInGroup)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_idp/paginators.html#listusersingrouppaginator)
        """
