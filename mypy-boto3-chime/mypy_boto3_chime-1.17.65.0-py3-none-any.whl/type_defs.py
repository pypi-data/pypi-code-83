"""
Type annotations for chime service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/type_defs.html)

Usage::

    ```python
    from mypy_boto3_chime.type_defs import AccountSettingsTypeDef

    data: AccountSettingsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_chime.literals import (
    AccountType,
    AppInstanceDataType,
    CallingNameStatus,
    Capability,
    ChannelMembershipType,
    ChannelMessagePersistenceType,
    ChannelMessageType,
    ChannelMode,
    ChannelPrivacy,
    EmailStatus,
    ErrorCode,
    GeoMatchLevel,
    InviteStatus,
    License,
    MemberType,
    NotificationTarget,
    NumberSelectionBehavior,
    OrderedPhoneNumberStatus,
    OriginationRouteProtocol,
    PhoneNumberAssociationName,
    PhoneNumberOrderStatus,
    PhoneNumberProductType,
    PhoneNumberStatus,
    PhoneNumberType,
    ProxySessionStatus,
    RegistrationStatus,
    RoomMembershipRole,
    SipRuleTriggerType,
    UserType,
    VoiceConnectorAwsRegion,
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
    "AccountSettingsTypeDef",
    "AccountTypeDef",
    "AlexaForBusinessMetadataTypeDef",
    "AppInstanceAdminSummaryTypeDef",
    "AppInstanceAdminTypeDef",
    "AppInstanceRetentionSettingsTypeDef",
    "AppInstanceStreamingConfigurationTypeDef",
    "AppInstanceSummaryTypeDef",
    "AppInstanceTypeDef",
    "AppInstanceUserMembershipSummaryTypeDef",
    "AppInstanceUserSummaryTypeDef",
    "AppInstanceUserTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef",
    "AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef",
    "AttendeeTypeDef",
    "BatchChannelMembershipsTypeDef",
    "BatchCreateAttendeeResponseTypeDef",
    "BatchCreateChannelMembershipErrorTypeDef",
    "BatchCreateChannelMembershipResponseTypeDef",
    "BatchCreateRoomMembershipResponseTypeDef",
    "BatchDeletePhoneNumberResponseTypeDef",
    "BatchSuspendUserResponseTypeDef",
    "BatchUnsuspendUserResponseTypeDef",
    "BatchUpdatePhoneNumberResponseTypeDef",
    "BatchUpdateUserResponseTypeDef",
    "BotTypeDef",
    "BusinessCallingSettingsTypeDef",
    "ChannelBanSummaryTypeDef",
    "ChannelBanTypeDef",
    "ChannelMembershipForAppInstanceUserSummaryTypeDef",
    "ChannelMembershipSummaryTypeDef",
    "ChannelMembershipTypeDef",
    "ChannelMessageSummaryTypeDef",
    "ChannelMessageTypeDef",
    "ChannelModeratedByAppInstanceUserSummaryTypeDef",
    "ChannelModeratorSummaryTypeDef",
    "ChannelModeratorTypeDef",
    "ChannelRetentionSettingsTypeDef",
    "ChannelSummaryTypeDef",
    "ChannelTypeDef",
    "ConversationRetentionSettingsTypeDef",
    "CreateAccountResponseTypeDef",
    "CreateAppInstanceAdminResponseTypeDef",
    "CreateAppInstanceResponseTypeDef",
    "CreateAppInstanceUserResponseTypeDef",
    "CreateAttendeeErrorTypeDef",
    "CreateAttendeeRequestItemTypeDef",
    "CreateAttendeeResponseTypeDef",
    "CreateBotResponseTypeDef",
    "CreateChannelBanResponseTypeDef",
    "CreateChannelMembershipResponseTypeDef",
    "CreateChannelModeratorResponseTypeDef",
    "CreateChannelResponseTypeDef",
    "CreateMeetingDialOutResponseTypeDef",
    "CreateMeetingResponseTypeDef",
    "CreateMeetingWithAttendeesResponseTypeDef",
    "CreatePhoneNumberOrderResponseTypeDef",
    "CreateProxySessionResponseTypeDef",
    "CreateRoomMembershipResponseTypeDef",
    "CreateRoomResponseTypeDef",
    "CreateSipMediaApplicationCallResponseTypeDef",
    "CreateSipMediaApplicationResponseTypeDef",
    "CreateSipRuleResponseTypeDef",
    "CreateUserResponseTypeDef",
    "CreateVoiceConnectorGroupResponseTypeDef",
    "CreateVoiceConnectorResponseTypeDef",
    "CredentialTypeDef",
    "DNISEmergencyCallingConfigurationTypeDef",
    "DescribeAppInstanceAdminResponseTypeDef",
    "DescribeAppInstanceResponseTypeDef",
    "DescribeAppInstanceUserResponseTypeDef",
    "DescribeChannelBanResponseTypeDef",
    "DescribeChannelMembershipForAppInstanceUserResponseTypeDef",
    "DescribeChannelMembershipResponseTypeDef",
    "DescribeChannelModeratedByAppInstanceUserResponseTypeDef",
    "DescribeChannelModeratorResponseTypeDef",
    "DescribeChannelResponseTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef",
    "DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef",
    "EmergencyCallingConfigurationTypeDef",
    "EventsConfigurationTypeDef",
    "GeoMatchParamsTypeDef",
    "GetAccountResponseTypeDef",
    "GetAccountSettingsResponseTypeDef",
    "GetAppInstanceRetentionSettingsResponseTypeDef",
    "GetAppInstanceStreamingConfigurationsResponseTypeDef",
    "GetAttendeeResponseTypeDef",
    "GetBotResponseTypeDef",
    "GetChannelMessageResponseTypeDef",
    "GetEventsConfigurationResponseTypeDef",
    "GetGlobalSettingsResponseTypeDef",
    "GetMeetingResponseTypeDef",
    "GetMessagingSessionEndpointResponseTypeDef",
    "GetPhoneNumberOrderResponseTypeDef",
    "GetPhoneNumberResponseTypeDef",
    "GetPhoneNumberSettingsResponseTypeDef",
    "GetProxySessionResponseTypeDef",
    "GetRetentionSettingsResponseTypeDef",
    "GetRoomResponseTypeDef",
    "GetSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "GetSipMediaApplicationResponseTypeDef",
    "GetSipRuleResponseTypeDef",
    "GetUserResponseTypeDef",
    "GetUserSettingsResponseTypeDef",
    "GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "GetVoiceConnectorGroupResponseTypeDef",
    "GetVoiceConnectorLoggingConfigurationResponseTypeDef",
    "GetVoiceConnectorOriginationResponseTypeDef",
    "GetVoiceConnectorProxyResponseTypeDef",
    "GetVoiceConnectorResponseTypeDef",
    "GetVoiceConnectorStreamingConfigurationResponseTypeDef",
    "GetVoiceConnectorTerminationHealthResponseTypeDef",
    "GetVoiceConnectorTerminationResponseTypeDef",
    "IdentityTypeDef",
    "InviteTypeDef",
    "InviteUsersResponseTypeDef",
    "ListAccountsResponseTypeDef",
    "ListAppInstanceAdminsResponseTypeDef",
    "ListAppInstanceUsersResponseTypeDef",
    "ListAppInstancesResponseTypeDef",
    "ListAttendeeTagsResponseTypeDef",
    "ListAttendeesResponseTypeDef",
    "ListBotsResponseTypeDef",
    "ListChannelBansResponseTypeDef",
    "ListChannelMembershipsForAppInstanceUserResponseTypeDef",
    "ListChannelMembershipsResponseTypeDef",
    "ListChannelMessagesResponseTypeDef",
    "ListChannelModeratorsResponseTypeDef",
    "ListChannelsModeratedByAppInstanceUserResponseTypeDef",
    "ListChannelsResponseTypeDef",
    "ListMeetingTagsResponseTypeDef",
    "ListMeetingsResponseTypeDef",
    "ListPhoneNumberOrdersResponseTypeDef",
    "ListPhoneNumbersResponseTypeDef",
    "ListProxySessionsResponseTypeDef",
    "ListRoomMembershipsResponseTypeDef",
    "ListRoomsResponseTypeDef",
    "ListSipMediaApplicationsResponseTypeDef",
    "ListSipRulesResponseTypeDef",
    "ListSupportedPhoneNumberCountriesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListUsersResponseTypeDef",
    "ListVoiceConnectorGroupsResponseTypeDef",
    "ListVoiceConnectorTerminationCredentialsResponseTypeDef",
    "ListVoiceConnectorsResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "MediaPlacementTypeDef",
    "MeetingNotificationConfigurationTypeDef",
    "MeetingTypeDef",
    "MemberErrorTypeDef",
    "MemberTypeDef",
    "MembershipItemTypeDef",
    "MessagingSessionEndpointTypeDef",
    "OrderedPhoneNumberTypeDef",
    "OriginationRouteTypeDef",
    "OriginationTypeDef",
    "PaginatorConfigTypeDef",
    "ParticipantTypeDef",
    "PhoneNumberAssociationTypeDef",
    "PhoneNumberCapabilitiesTypeDef",
    "PhoneNumberCountryTypeDef",
    "PhoneNumberErrorTypeDef",
    "PhoneNumberOrderTypeDef",
    "PhoneNumberTypeDef",
    "ProxySessionTypeDef",
    "ProxyTypeDef",
    "PutAppInstanceRetentionSettingsResponseTypeDef",
    "PutAppInstanceStreamingConfigurationsResponseTypeDef",
    "PutEventsConfigurationResponseTypeDef",
    "PutRetentionSettingsResponseTypeDef",
    "PutSipMediaApplicationLoggingConfigurationResponseTypeDef",
    "PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef",
    "PutVoiceConnectorLoggingConfigurationResponseTypeDef",
    "PutVoiceConnectorOriginationResponseTypeDef",
    "PutVoiceConnectorProxyResponseTypeDef",
    "PutVoiceConnectorStreamingConfigurationResponseTypeDef",
    "PutVoiceConnectorTerminationResponseTypeDef",
    "RedactChannelMessageResponseTypeDef",
    "RegenerateSecurityTokenResponseTypeDef",
    "ResetPersonalPINResponseTypeDef",
    "RestorePhoneNumberResponseTypeDef",
    "RetentionSettingsTypeDef",
    "RoomMembershipTypeDef",
    "RoomRetentionSettingsTypeDef",
    "RoomTypeDef",
    "SearchAvailablePhoneNumbersResponseTypeDef",
    "SendChannelMessageResponseTypeDef",
    "SigninDelegateGroupTypeDef",
    "SipMediaApplicationCallTypeDef",
    "SipMediaApplicationEndpointTypeDef",
    "SipMediaApplicationLoggingConfigurationTypeDef",
    "SipMediaApplicationTypeDef",
    "SipRuleTargetApplicationTypeDef",
    "SipRuleTypeDef",
    "StreamingConfigurationTypeDef",
    "StreamingNotificationTargetTypeDef",
    "TagTypeDef",
    "TelephonySettingsTypeDef",
    "TerminationHealthTypeDef",
    "TerminationTypeDef",
    "UpdateAccountResponseTypeDef",
    "UpdateAppInstanceResponseTypeDef",
    "UpdateAppInstanceUserResponseTypeDef",
    "UpdateBotResponseTypeDef",
    "UpdateChannelMessageResponseTypeDef",
    "UpdateChannelReadMarkerResponseTypeDef",
    "UpdateChannelResponseTypeDef",
    "UpdatePhoneNumberRequestItemTypeDef",
    "UpdatePhoneNumberResponseTypeDef",
    "UpdateProxySessionResponseTypeDef",
    "UpdateRoomMembershipResponseTypeDef",
    "UpdateRoomResponseTypeDef",
    "UpdateSipMediaApplicationResponseTypeDef",
    "UpdateSipRuleResponseTypeDef",
    "UpdateUserRequestItemTypeDef",
    "UpdateUserResponseTypeDef",
    "UpdateVoiceConnectorGroupResponseTypeDef",
    "UpdateVoiceConnectorResponseTypeDef",
    "UserErrorTypeDef",
    "UserSettingsTypeDef",
    "UserTypeDef",
    "VoiceConnectorGroupTypeDef",
    "VoiceConnectorItemTypeDef",
    "VoiceConnectorSettingsTypeDef",
    "VoiceConnectorTypeDef",
)


class AccountSettingsTypeDef(TypedDict, total=False):
    DisableRemoteControl: bool
    EnableDialOut: bool


class _RequiredAccountTypeDef(TypedDict):
    AwsAccountId: str
    AccountId: str
    Name: str


class AccountTypeDef(_RequiredAccountTypeDef, total=False):
    AccountType: AccountType
    CreatedTimestamp: datetime
    DefaultLicense: License
    SupportedLicenses: List[License]
    SigninDelegateGroups: List["SigninDelegateGroupTypeDef"]


class AlexaForBusinessMetadataTypeDef(TypedDict, total=False):
    IsAlexaForBusinessEnabled: bool
    AlexaForBusinessRoomArn: str


class AppInstanceAdminSummaryTypeDef(TypedDict, total=False):
    Admin: "IdentityTypeDef"


class AppInstanceAdminTypeDef(TypedDict, total=False):
    Admin: "IdentityTypeDef"
    AppInstanceArn: str
    CreatedTimestamp: datetime


class AppInstanceRetentionSettingsTypeDef(TypedDict, total=False):
    ChannelRetentionSettings: "ChannelRetentionSettingsTypeDef"


class AppInstanceStreamingConfigurationTypeDef(TypedDict):
    AppInstanceDataType: AppInstanceDataType
    ResourceArn: str


class AppInstanceSummaryTypeDef(TypedDict, total=False):
    AppInstanceArn: str
    Name: str
    Metadata: str


class AppInstanceTypeDef(TypedDict, total=False):
    AppInstanceArn: str
    Name: str
    Metadata: str
    CreatedTimestamp: datetime
    LastUpdatedTimestamp: datetime


AppInstanceUserMembershipSummaryTypeDef = TypedDict(
    "AppInstanceUserMembershipSummaryTypeDef",
    {"Type": ChannelMembershipType, "ReadMarkerTimestamp": datetime},
    total=False,
)


class AppInstanceUserSummaryTypeDef(TypedDict, total=False):
    AppInstanceUserArn: str
    Name: str
    Metadata: str


class AppInstanceUserTypeDef(TypedDict, total=False):
    AppInstanceUserArn: str
    Name: str
    CreatedTimestamp: datetime
    Metadata: str
    LastUpdatedTimestamp: datetime


class AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef(TypedDict, total=False):
    PhoneNumberErrors: List["PhoneNumberErrorTypeDef"]


class AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef(TypedDict, total=False):
    PhoneNumberErrors: List["PhoneNumberErrorTypeDef"]


class AttendeeTypeDef(TypedDict, total=False):
    ExternalUserId: str
    AttendeeId: str
    JoinToken: str


BatchChannelMembershipsTypeDef = TypedDict(
    "BatchChannelMembershipsTypeDef",
    {
        "InvitedBy": "IdentityTypeDef",
        "Type": ChannelMembershipType,
        "Members": List["IdentityTypeDef"],
        "ChannelArn": str,
    },
    total=False,
)


class BatchCreateAttendeeResponseTypeDef(TypedDict, total=False):
    Attendees: List["AttendeeTypeDef"]
    Errors: List["CreateAttendeeErrorTypeDef"]


class BatchCreateChannelMembershipErrorTypeDef(TypedDict, total=False):
    MemberArn: str
    ErrorCode: ErrorCode
    ErrorMessage: str


class BatchCreateChannelMembershipResponseTypeDef(TypedDict, total=False):
    BatchChannelMemberships: "BatchChannelMembershipsTypeDef"
    Errors: List["BatchCreateChannelMembershipErrorTypeDef"]


class BatchCreateRoomMembershipResponseTypeDef(TypedDict, total=False):
    Errors: List["MemberErrorTypeDef"]


class BatchDeletePhoneNumberResponseTypeDef(TypedDict, total=False):
    PhoneNumberErrors: List["PhoneNumberErrorTypeDef"]


class BatchSuspendUserResponseTypeDef(TypedDict, total=False):
    UserErrors: List["UserErrorTypeDef"]


class BatchUnsuspendUserResponseTypeDef(TypedDict, total=False):
    UserErrors: List["UserErrorTypeDef"]


class BatchUpdatePhoneNumberResponseTypeDef(TypedDict, total=False):
    PhoneNumberErrors: List["PhoneNumberErrorTypeDef"]


class BatchUpdateUserResponseTypeDef(TypedDict, total=False):
    UserErrors: List["UserErrorTypeDef"]


class BotTypeDef(TypedDict, total=False):
    BotId: str
    UserId: str
    DisplayName: str
    BotType: Literal["ChatBot"]
    Disabled: bool
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    BotEmail: str
    SecurityToken: str


class BusinessCallingSettingsTypeDef(TypedDict, total=False):
    CdrBucket: str


class ChannelBanSummaryTypeDef(TypedDict, total=False):
    Member: "IdentityTypeDef"


class ChannelBanTypeDef(TypedDict, total=False):
    Member: "IdentityTypeDef"
    ChannelArn: str
    CreatedTimestamp: datetime
    CreatedBy: "IdentityTypeDef"


class ChannelMembershipForAppInstanceUserSummaryTypeDef(TypedDict, total=False):
    ChannelSummary: "ChannelSummaryTypeDef"
    AppInstanceUserMembershipSummary: "AppInstanceUserMembershipSummaryTypeDef"


class ChannelMembershipSummaryTypeDef(TypedDict, total=False):
    Member: "IdentityTypeDef"


ChannelMembershipTypeDef = TypedDict(
    "ChannelMembershipTypeDef",
    {
        "InvitedBy": "IdentityTypeDef",
        "Type": ChannelMembershipType,
        "Member": "IdentityTypeDef",
        "ChannelArn": str,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
    },
    total=False,
)

ChannelMessageSummaryTypeDef = TypedDict(
    "ChannelMessageSummaryTypeDef",
    {
        "MessageId": str,
        "Content": str,
        "Metadata": str,
        "Type": ChannelMessageType,
        "CreatedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "LastEditedTimestamp": datetime,
        "Sender": "IdentityTypeDef",
        "Redacted": bool,
    },
    total=False,
)

ChannelMessageTypeDef = TypedDict(
    "ChannelMessageTypeDef",
    {
        "ChannelArn": str,
        "MessageId": str,
        "Content": str,
        "Metadata": str,
        "Type": ChannelMessageType,
        "CreatedTimestamp": datetime,
        "LastEditedTimestamp": datetime,
        "LastUpdatedTimestamp": datetime,
        "Sender": "IdentityTypeDef",
        "Redacted": bool,
        "Persistence": ChannelMessagePersistenceType,
    },
    total=False,
)


class ChannelModeratedByAppInstanceUserSummaryTypeDef(TypedDict, total=False):
    ChannelSummary: "ChannelSummaryTypeDef"


class ChannelModeratorSummaryTypeDef(TypedDict, total=False):
    Moderator: "IdentityTypeDef"


class ChannelModeratorTypeDef(TypedDict, total=False):
    Moderator: "IdentityTypeDef"
    ChannelArn: str
    CreatedTimestamp: datetime
    CreatedBy: "IdentityTypeDef"


class ChannelRetentionSettingsTypeDef(TypedDict, total=False):
    RetentionDays: int


class ChannelSummaryTypeDef(TypedDict, total=False):
    Name: str
    ChannelArn: str
    Mode: ChannelMode
    Privacy: ChannelPrivacy
    Metadata: str
    LastMessageTimestamp: datetime


class ChannelTypeDef(TypedDict, total=False):
    Name: str
    ChannelArn: str
    Mode: ChannelMode
    Privacy: ChannelPrivacy
    Metadata: str
    CreatedBy: "IdentityTypeDef"
    CreatedTimestamp: datetime
    LastMessageTimestamp: datetime
    LastUpdatedTimestamp: datetime


class ConversationRetentionSettingsTypeDef(TypedDict, total=False):
    RetentionDays: int


class CreateAccountResponseTypeDef(TypedDict, total=False):
    Account: "AccountTypeDef"


class CreateAppInstanceAdminResponseTypeDef(TypedDict, total=False):
    AppInstanceAdmin: "IdentityTypeDef"
    AppInstanceArn: str


class CreateAppInstanceResponseTypeDef(TypedDict, total=False):
    AppInstanceArn: str


class CreateAppInstanceUserResponseTypeDef(TypedDict, total=False):
    AppInstanceUserArn: str


class CreateAttendeeErrorTypeDef(TypedDict, total=False):
    ExternalUserId: str
    ErrorCode: str
    ErrorMessage: str


class _RequiredCreateAttendeeRequestItemTypeDef(TypedDict):
    ExternalUserId: str


class CreateAttendeeRequestItemTypeDef(_RequiredCreateAttendeeRequestItemTypeDef, total=False):
    Tags: List["TagTypeDef"]


class CreateAttendeeResponseTypeDef(TypedDict, total=False):
    Attendee: "AttendeeTypeDef"


class CreateBotResponseTypeDef(TypedDict, total=False):
    Bot: "BotTypeDef"


class CreateChannelBanResponseTypeDef(TypedDict, total=False):
    ChannelArn: str
    Member: "IdentityTypeDef"


class CreateChannelMembershipResponseTypeDef(TypedDict, total=False):
    ChannelArn: str
    Member: "IdentityTypeDef"


class CreateChannelModeratorResponseTypeDef(TypedDict, total=False):
    ChannelArn: str
    ChannelModerator: "IdentityTypeDef"


class CreateChannelResponseTypeDef(TypedDict, total=False):
    ChannelArn: str


class CreateMeetingDialOutResponseTypeDef(TypedDict, total=False):
    TransactionId: str


class CreateMeetingResponseTypeDef(TypedDict, total=False):
    Meeting: "MeetingTypeDef"


class CreateMeetingWithAttendeesResponseTypeDef(TypedDict, total=False):
    Meeting: "MeetingTypeDef"
    Attendees: List["AttendeeTypeDef"]
    Errors: List["CreateAttendeeErrorTypeDef"]


class CreatePhoneNumberOrderResponseTypeDef(TypedDict, total=False):
    PhoneNumberOrder: "PhoneNumberOrderTypeDef"


class CreateProxySessionResponseTypeDef(TypedDict, total=False):
    ProxySession: "ProxySessionTypeDef"


class CreateRoomMembershipResponseTypeDef(TypedDict, total=False):
    RoomMembership: "RoomMembershipTypeDef"


class CreateRoomResponseTypeDef(TypedDict, total=False):
    Room: "RoomTypeDef"


class CreateSipMediaApplicationCallResponseTypeDef(TypedDict, total=False):
    SipMediaApplicationCall: "SipMediaApplicationCallTypeDef"


class CreateSipMediaApplicationResponseTypeDef(TypedDict, total=False):
    SipMediaApplication: "SipMediaApplicationTypeDef"


class CreateSipRuleResponseTypeDef(TypedDict, total=False):
    SipRule: "SipRuleTypeDef"


class CreateUserResponseTypeDef(TypedDict, total=False):
    User: "UserTypeDef"


class CreateVoiceConnectorGroupResponseTypeDef(TypedDict, total=False):
    VoiceConnectorGroup: "VoiceConnectorGroupTypeDef"


class CreateVoiceConnectorResponseTypeDef(TypedDict, total=False):
    VoiceConnector: "VoiceConnectorTypeDef"


class CredentialTypeDef(TypedDict, total=False):
    Username: str
    Password: str


class _RequiredDNISEmergencyCallingConfigurationTypeDef(TypedDict):
    EmergencyPhoneNumber: str
    CallingCountry: str


class DNISEmergencyCallingConfigurationTypeDef(
    _RequiredDNISEmergencyCallingConfigurationTypeDef, total=False
):
    TestPhoneNumber: str


class DescribeAppInstanceAdminResponseTypeDef(TypedDict, total=False):
    AppInstanceAdmin: "AppInstanceAdminTypeDef"


class DescribeAppInstanceResponseTypeDef(TypedDict, total=False):
    AppInstance: "AppInstanceTypeDef"


class DescribeAppInstanceUserResponseTypeDef(TypedDict, total=False):
    AppInstanceUser: "AppInstanceUserTypeDef"


class DescribeChannelBanResponseTypeDef(TypedDict, total=False):
    ChannelBan: "ChannelBanTypeDef"


class DescribeChannelMembershipForAppInstanceUserResponseTypeDef(TypedDict, total=False):
    ChannelMembership: "ChannelMembershipForAppInstanceUserSummaryTypeDef"


class DescribeChannelMembershipResponseTypeDef(TypedDict, total=False):
    ChannelMembership: "ChannelMembershipTypeDef"


class DescribeChannelModeratedByAppInstanceUserResponseTypeDef(TypedDict, total=False):
    Channel: "ChannelModeratedByAppInstanceUserSummaryTypeDef"


class DescribeChannelModeratorResponseTypeDef(TypedDict, total=False):
    ChannelModerator: "ChannelModeratorTypeDef"


class DescribeChannelResponseTypeDef(TypedDict, total=False):
    Channel: "ChannelTypeDef"


class DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef(TypedDict, total=False):
    PhoneNumberErrors: List["PhoneNumberErrorTypeDef"]


class DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef(TypedDict, total=False):
    PhoneNumberErrors: List["PhoneNumberErrorTypeDef"]


class EmergencyCallingConfigurationTypeDef(TypedDict, total=False):
    DNIS: List["DNISEmergencyCallingConfigurationTypeDef"]


class EventsConfigurationTypeDef(TypedDict, total=False):
    BotId: str
    OutboundEventsHTTPSEndpoint: str
    LambdaFunctionArn: str


class GeoMatchParamsTypeDef(TypedDict):
    Country: str
    AreaCode: str


class GetAccountResponseTypeDef(TypedDict, total=False):
    Account: "AccountTypeDef"


class GetAccountSettingsResponseTypeDef(TypedDict, total=False):
    AccountSettings: "AccountSettingsTypeDef"


class GetAppInstanceRetentionSettingsResponseTypeDef(TypedDict, total=False):
    AppInstanceRetentionSettings: "AppInstanceRetentionSettingsTypeDef"
    InitiateDeletionTimestamp: datetime


class GetAppInstanceStreamingConfigurationsResponseTypeDef(TypedDict, total=False):
    AppInstanceStreamingConfigurations: List["AppInstanceStreamingConfigurationTypeDef"]


class GetAttendeeResponseTypeDef(TypedDict, total=False):
    Attendee: "AttendeeTypeDef"


class GetBotResponseTypeDef(TypedDict, total=False):
    Bot: "BotTypeDef"


class GetChannelMessageResponseTypeDef(TypedDict, total=False):
    ChannelMessage: "ChannelMessageTypeDef"


class GetEventsConfigurationResponseTypeDef(TypedDict, total=False):
    EventsConfiguration: "EventsConfigurationTypeDef"


class GetGlobalSettingsResponseTypeDef(TypedDict, total=False):
    BusinessCalling: "BusinessCallingSettingsTypeDef"
    VoiceConnector: "VoiceConnectorSettingsTypeDef"


class GetMeetingResponseTypeDef(TypedDict, total=False):
    Meeting: "MeetingTypeDef"


class GetMessagingSessionEndpointResponseTypeDef(TypedDict, total=False):
    Endpoint: "MessagingSessionEndpointTypeDef"


class GetPhoneNumberOrderResponseTypeDef(TypedDict, total=False):
    PhoneNumberOrder: "PhoneNumberOrderTypeDef"


class GetPhoneNumberResponseTypeDef(TypedDict, total=False):
    PhoneNumber: "PhoneNumberTypeDef"


class GetPhoneNumberSettingsResponseTypeDef(TypedDict, total=False):
    CallingName: str
    CallingNameUpdatedTimestamp: datetime


class GetProxySessionResponseTypeDef(TypedDict, total=False):
    ProxySession: "ProxySessionTypeDef"


class GetRetentionSettingsResponseTypeDef(TypedDict, total=False):
    RetentionSettings: "RetentionSettingsTypeDef"
    InitiateDeletionTimestamp: datetime


class GetRoomResponseTypeDef(TypedDict, total=False):
    Room: "RoomTypeDef"


class GetSipMediaApplicationLoggingConfigurationResponseTypeDef(TypedDict, total=False):
    SipMediaApplicationLoggingConfiguration: "SipMediaApplicationLoggingConfigurationTypeDef"


class GetSipMediaApplicationResponseTypeDef(TypedDict, total=False):
    SipMediaApplication: "SipMediaApplicationTypeDef"


class GetSipRuleResponseTypeDef(TypedDict, total=False):
    SipRule: "SipRuleTypeDef"


class GetUserResponseTypeDef(TypedDict, total=False):
    User: "UserTypeDef"


class GetUserSettingsResponseTypeDef(TypedDict, total=False):
    UserSettings: "UserSettingsTypeDef"


class GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef(TypedDict, total=False):
    EmergencyCallingConfiguration: "EmergencyCallingConfigurationTypeDef"


class GetVoiceConnectorGroupResponseTypeDef(TypedDict, total=False):
    VoiceConnectorGroup: "VoiceConnectorGroupTypeDef"


class GetVoiceConnectorLoggingConfigurationResponseTypeDef(TypedDict, total=False):
    LoggingConfiguration: "LoggingConfigurationTypeDef"


class GetVoiceConnectorOriginationResponseTypeDef(TypedDict, total=False):
    Origination: "OriginationTypeDef"


class GetVoiceConnectorProxyResponseTypeDef(TypedDict, total=False):
    Proxy: "ProxyTypeDef"


class GetVoiceConnectorResponseTypeDef(TypedDict, total=False):
    VoiceConnector: "VoiceConnectorTypeDef"


class GetVoiceConnectorStreamingConfigurationResponseTypeDef(TypedDict, total=False):
    StreamingConfiguration: "StreamingConfigurationTypeDef"


class GetVoiceConnectorTerminationHealthResponseTypeDef(TypedDict, total=False):
    TerminationHealth: "TerminationHealthTypeDef"


class GetVoiceConnectorTerminationResponseTypeDef(TypedDict, total=False):
    Termination: "TerminationTypeDef"


class IdentityTypeDef(TypedDict, total=False):
    Arn: str
    Name: str


class InviteTypeDef(TypedDict, total=False):
    InviteId: str
    Status: InviteStatus
    EmailAddress: str
    EmailStatus: EmailStatus


class InviteUsersResponseTypeDef(TypedDict, total=False):
    Invites: List["InviteTypeDef"]


class ListAccountsResponseTypeDef(TypedDict, total=False):
    Accounts: List["AccountTypeDef"]
    NextToken: str


class ListAppInstanceAdminsResponseTypeDef(TypedDict, total=False):
    AppInstanceArn: str
    AppInstanceAdmins: List["AppInstanceAdminSummaryTypeDef"]
    NextToken: str


class ListAppInstanceUsersResponseTypeDef(TypedDict, total=False):
    AppInstanceArn: str
    AppInstanceUsers: List["AppInstanceUserSummaryTypeDef"]
    NextToken: str


class ListAppInstancesResponseTypeDef(TypedDict, total=False):
    AppInstances: List["AppInstanceSummaryTypeDef"]
    NextToken: str


class ListAttendeeTagsResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class ListAttendeesResponseTypeDef(TypedDict, total=False):
    Attendees: List["AttendeeTypeDef"]
    NextToken: str


class ListBotsResponseTypeDef(TypedDict, total=False):
    Bots: List["BotTypeDef"]
    NextToken: str


class ListChannelBansResponseTypeDef(TypedDict, total=False):
    ChannelArn: str
    NextToken: str
    ChannelBans: List["ChannelBanSummaryTypeDef"]


class ListChannelMembershipsForAppInstanceUserResponseTypeDef(TypedDict, total=False):
    ChannelMemberships: List["ChannelMembershipForAppInstanceUserSummaryTypeDef"]
    NextToken: str


class ListChannelMembershipsResponseTypeDef(TypedDict, total=False):
    ChannelArn: str
    ChannelMemberships: List["ChannelMembershipSummaryTypeDef"]
    NextToken: str


class ListChannelMessagesResponseTypeDef(TypedDict, total=False):
    ChannelArn: str
    NextToken: str
    ChannelMessages: List["ChannelMessageSummaryTypeDef"]


class ListChannelModeratorsResponseTypeDef(TypedDict, total=False):
    ChannelArn: str
    NextToken: str
    ChannelModerators: List["ChannelModeratorSummaryTypeDef"]


class ListChannelsModeratedByAppInstanceUserResponseTypeDef(TypedDict, total=False):
    Channels: List["ChannelModeratedByAppInstanceUserSummaryTypeDef"]
    NextToken: str


class ListChannelsResponseTypeDef(TypedDict, total=False):
    Channels: List["ChannelSummaryTypeDef"]
    NextToken: str


class ListMeetingTagsResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class ListMeetingsResponseTypeDef(TypedDict, total=False):
    Meetings: List["MeetingTypeDef"]
    NextToken: str


class ListPhoneNumberOrdersResponseTypeDef(TypedDict, total=False):
    PhoneNumberOrders: List["PhoneNumberOrderTypeDef"]
    NextToken: str


class ListPhoneNumbersResponseTypeDef(TypedDict, total=False):
    PhoneNumbers: List["PhoneNumberTypeDef"]
    NextToken: str


class ListProxySessionsResponseTypeDef(TypedDict, total=False):
    ProxySessions: List["ProxySessionTypeDef"]
    NextToken: str


class ListRoomMembershipsResponseTypeDef(TypedDict, total=False):
    RoomMemberships: List["RoomMembershipTypeDef"]
    NextToken: str


class ListRoomsResponseTypeDef(TypedDict, total=False):
    Rooms: List["RoomTypeDef"]
    NextToken: str


class ListSipMediaApplicationsResponseTypeDef(TypedDict, total=False):
    SipMediaApplications: List["SipMediaApplicationTypeDef"]
    NextToken: str


class ListSipRulesResponseTypeDef(TypedDict, total=False):
    SipRules: List["SipRuleTypeDef"]
    NextToken: str


class ListSupportedPhoneNumberCountriesResponseTypeDef(TypedDict, total=False):
    PhoneNumberCountries: List["PhoneNumberCountryTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class ListUsersResponseTypeDef(TypedDict, total=False):
    Users: List["UserTypeDef"]
    NextToken: str


class ListVoiceConnectorGroupsResponseTypeDef(TypedDict, total=False):
    VoiceConnectorGroups: List["VoiceConnectorGroupTypeDef"]
    NextToken: str


class ListVoiceConnectorTerminationCredentialsResponseTypeDef(TypedDict, total=False):
    Usernames: List[str]


class ListVoiceConnectorsResponseTypeDef(TypedDict, total=False):
    VoiceConnectors: List["VoiceConnectorTypeDef"]
    NextToken: str


class LoggingConfigurationTypeDef(TypedDict, total=False):
    EnableSIPLogs: bool


class MediaPlacementTypeDef(TypedDict, total=False):
    AudioHostUrl: str
    AudioFallbackUrl: str
    ScreenDataUrl: str
    ScreenSharingUrl: str
    ScreenViewingUrl: str
    SignalingUrl: str
    TurnControlUrl: str


class MeetingNotificationConfigurationTypeDef(TypedDict, total=False):
    SnsTopicArn: str
    SqsQueueArn: str


class MeetingTypeDef(TypedDict, total=False):
    MeetingId: str
    ExternalMeetingId: str
    MediaPlacement: "MediaPlacementTypeDef"
    MediaRegion: str


class MemberErrorTypeDef(TypedDict, total=False):
    MemberId: str
    ErrorCode: ErrorCode
    ErrorMessage: str


class MemberTypeDef(TypedDict, total=False):
    MemberId: str
    MemberType: MemberType
    Email: str
    FullName: str
    AccountId: str


class MembershipItemTypeDef(TypedDict, total=False):
    MemberId: str
    Role: RoomMembershipRole


class MessagingSessionEndpointTypeDef(TypedDict, total=False):
    Url: str


class OrderedPhoneNumberTypeDef(TypedDict, total=False):
    E164PhoneNumber: str
    Status: OrderedPhoneNumberStatus


OriginationRouteTypeDef = TypedDict(
    "OriginationRouteTypeDef",
    {
        "Host": str,
        "Port": int,
        "Protocol": OriginationRouteProtocol,
        "Priority": int,
        "Weight": int,
    },
    total=False,
)


class OriginationTypeDef(TypedDict, total=False):
    Routes: List["OriginationRouteTypeDef"]
    Disabled: bool


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParticipantTypeDef(TypedDict, total=False):
    PhoneNumber: str
    ProxyPhoneNumber: str


class PhoneNumberAssociationTypeDef(TypedDict, total=False):
    Value: str
    Name: PhoneNumberAssociationName
    AssociatedTimestamp: datetime


class PhoneNumberCapabilitiesTypeDef(TypedDict, total=False):
    InboundCall: bool
    OutboundCall: bool
    InboundSMS: bool
    OutboundSMS: bool
    InboundMMS: bool
    OutboundMMS: bool


class PhoneNumberCountryTypeDef(TypedDict, total=False):
    CountryCode: str
    SupportedPhoneNumberTypes: List[PhoneNumberType]


class PhoneNumberErrorTypeDef(TypedDict, total=False):
    PhoneNumberId: str
    ErrorCode: ErrorCode
    ErrorMessage: str


class PhoneNumberOrderTypeDef(TypedDict, total=False):
    PhoneNumberOrderId: str
    ProductType: PhoneNumberProductType
    Status: PhoneNumberOrderStatus
    OrderedPhoneNumbers: List["OrderedPhoneNumberTypeDef"]
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime


PhoneNumberTypeDef = TypedDict(
    "PhoneNumberTypeDef",
    {
        "PhoneNumberId": str,
        "E164PhoneNumber": str,
        "Country": str,
        "Type": PhoneNumberType,
        "ProductType": PhoneNumberProductType,
        "Status": PhoneNumberStatus,
        "Capabilities": "PhoneNumberCapabilitiesTypeDef",
        "Associations": List["PhoneNumberAssociationTypeDef"],
        "CallingName": str,
        "CallingNameStatus": CallingNameStatus,
        "CreatedTimestamp": datetime,
        "UpdatedTimestamp": datetime,
        "DeletionTimestamp": datetime,
    },
    total=False,
)


class ProxySessionTypeDef(TypedDict, total=False):
    VoiceConnectorId: str
    ProxySessionId: str
    Name: str
    Status: ProxySessionStatus
    ExpiryMinutes: int
    Capabilities: List[Capability]
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
    EndedTimestamp: datetime
    Participants: List["ParticipantTypeDef"]
    NumberSelectionBehavior: NumberSelectionBehavior
    GeoMatchLevel: GeoMatchLevel
    GeoMatchParams: "GeoMatchParamsTypeDef"


class ProxyTypeDef(TypedDict, total=False):
    DefaultSessionExpiryMinutes: int
    Disabled: bool
    FallBackPhoneNumber: str
    PhoneNumberCountries: List[str]


class PutAppInstanceRetentionSettingsResponseTypeDef(TypedDict, total=False):
    AppInstanceRetentionSettings: "AppInstanceRetentionSettingsTypeDef"
    InitiateDeletionTimestamp: datetime


class PutAppInstanceStreamingConfigurationsResponseTypeDef(TypedDict, total=False):
    AppInstanceStreamingConfigurations: List["AppInstanceStreamingConfigurationTypeDef"]


class PutEventsConfigurationResponseTypeDef(TypedDict, total=False):
    EventsConfiguration: "EventsConfigurationTypeDef"


class PutRetentionSettingsResponseTypeDef(TypedDict, total=False):
    RetentionSettings: "RetentionSettingsTypeDef"
    InitiateDeletionTimestamp: datetime


class PutSipMediaApplicationLoggingConfigurationResponseTypeDef(TypedDict, total=False):
    SipMediaApplicationLoggingConfiguration: "SipMediaApplicationLoggingConfigurationTypeDef"


class PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef(TypedDict, total=False):
    EmergencyCallingConfiguration: "EmergencyCallingConfigurationTypeDef"


class PutVoiceConnectorLoggingConfigurationResponseTypeDef(TypedDict, total=False):
    LoggingConfiguration: "LoggingConfigurationTypeDef"


class PutVoiceConnectorOriginationResponseTypeDef(TypedDict, total=False):
    Origination: "OriginationTypeDef"


class PutVoiceConnectorProxyResponseTypeDef(TypedDict, total=False):
    Proxy: "ProxyTypeDef"


class PutVoiceConnectorStreamingConfigurationResponseTypeDef(TypedDict, total=False):
    StreamingConfiguration: "StreamingConfigurationTypeDef"


class PutVoiceConnectorTerminationResponseTypeDef(TypedDict, total=False):
    Termination: "TerminationTypeDef"


class RedactChannelMessageResponseTypeDef(TypedDict, total=False):
    ChannelArn: str
    MessageId: str


class RegenerateSecurityTokenResponseTypeDef(TypedDict, total=False):
    Bot: "BotTypeDef"


class ResetPersonalPINResponseTypeDef(TypedDict, total=False):
    User: "UserTypeDef"


class RestorePhoneNumberResponseTypeDef(TypedDict, total=False):
    PhoneNumber: "PhoneNumberTypeDef"


class RetentionSettingsTypeDef(TypedDict, total=False):
    RoomRetentionSettings: "RoomRetentionSettingsTypeDef"
    ConversationRetentionSettings: "ConversationRetentionSettingsTypeDef"


class RoomMembershipTypeDef(TypedDict, total=False):
    RoomId: str
    Member: "MemberTypeDef"
    Role: RoomMembershipRole
    InvitedBy: str
    UpdatedTimestamp: datetime


class RoomRetentionSettingsTypeDef(TypedDict, total=False):
    RetentionDays: int


class RoomTypeDef(TypedDict, total=False):
    RoomId: str
    Name: str
    AccountId: str
    CreatedBy: str
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime


class SearchAvailablePhoneNumbersResponseTypeDef(TypedDict, total=False):
    E164PhoneNumbers: List[str]
    NextToken: str


class SendChannelMessageResponseTypeDef(TypedDict, total=False):
    ChannelArn: str
    MessageId: str


class SigninDelegateGroupTypeDef(TypedDict, total=False):
    GroupName: str


class SipMediaApplicationCallTypeDef(TypedDict, total=False):
    TransactionId: str


class SipMediaApplicationEndpointTypeDef(TypedDict, total=False):
    LambdaArn: str


class SipMediaApplicationLoggingConfigurationTypeDef(TypedDict, total=False):
    EnableSipMediaApplicationMessageLogs: bool


class SipMediaApplicationTypeDef(TypedDict, total=False):
    SipMediaApplicationId: str
    AwsRegion: str
    Name: str
    Endpoints: List["SipMediaApplicationEndpointTypeDef"]
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime


class SipRuleTargetApplicationTypeDef(TypedDict, total=False):
    SipMediaApplicationId: str
    Priority: int
    AwsRegion: str


class SipRuleTypeDef(TypedDict, total=False):
    SipRuleId: str
    Name: str
    Disabled: bool
    TriggerType: SipRuleTriggerType
    TriggerValue: str
    TargetApplications: List["SipRuleTargetApplicationTypeDef"]
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime


class _RequiredStreamingConfigurationTypeDef(TypedDict):
    DataRetentionInHours: int


class StreamingConfigurationTypeDef(_RequiredStreamingConfigurationTypeDef, total=False):
    Disabled: bool
    StreamingNotificationTargets: List["StreamingNotificationTargetTypeDef"]


class StreamingNotificationTargetTypeDef(TypedDict):
    NotificationTarget: NotificationTarget


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TelephonySettingsTypeDef(TypedDict):
    InboundCalling: bool
    OutboundCalling: bool
    SMS: bool


class TerminationHealthTypeDef(TypedDict, total=False):
    Timestamp: datetime
    Source: str


class TerminationTypeDef(TypedDict, total=False):
    CpsLimit: int
    DefaultPhoneNumber: str
    CallingRegions: List[str]
    CidrAllowedList: List[str]
    Disabled: bool


class UpdateAccountResponseTypeDef(TypedDict, total=False):
    Account: "AccountTypeDef"


class UpdateAppInstanceResponseTypeDef(TypedDict, total=False):
    AppInstanceArn: str


class UpdateAppInstanceUserResponseTypeDef(TypedDict, total=False):
    AppInstanceUserArn: str


class UpdateBotResponseTypeDef(TypedDict, total=False):
    Bot: "BotTypeDef"


class UpdateChannelMessageResponseTypeDef(TypedDict, total=False):
    ChannelArn: str
    MessageId: str


class UpdateChannelReadMarkerResponseTypeDef(TypedDict, total=False):
    ChannelArn: str


class UpdateChannelResponseTypeDef(TypedDict, total=False):
    ChannelArn: str


class _RequiredUpdatePhoneNumberRequestItemTypeDef(TypedDict):
    PhoneNumberId: str


class UpdatePhoneNumberRequestItemTypeDef(
    _RequiredUpdatePhoneNumberRequestItemTypeDef, total=False
):
    ProductType: PhoneNumberProductType
    CallingName: str


class UpdatePhoneNumberResponseTypeDef(TypedDict, total=False):
    PhoneNumber: "PhoneNumberTypeDef"


class UpdateProxySessionResponseTypeDef(TypedDict, total=False):
    ProxySession: "ProxySessionTypeDef"


class UpdateRoomMembershipResponseTypeDef(TypedDict, total=False):
    RoomMembership: "RoomMembershipTypeDef"


class UpdateRoomResponseTypeDef(TypedDict, total=False):
    Room: "RoomTypeDef"


class UpdateSipMediaApplicationResponseTypeDef(TypedDict, total=False):
    SipMediaApplication: "SipMediaApplicationTypeDef"


class UpdateSipRuleResponseTypeDef(TypedDict, total=False):
    SipRule: "SipRuleTypeDef"


class _RequiredUpdateUserRequestItemTypeDef(TypedDict):
    UserId: str


class UpdateUserRequestItemTypeDef(_RequiredUpdateUserRequestItemTypeDef, total=False):
    LicenseType: License
    UserType: UserType
    AlexaForBusinessMetadata: "AlexaForBusinessMetadataTypeDef"


class UpdateUserResponseTypeDef(TypedDict, total=False):
    User: "UserTypeDef"


class UpdateVoiceConnectorGroupResponseTypeDef(TypedDict, total=False):
    VoiceConnectorGroup: "VoiceConnectorGroupTypeDef"


class UpdateVoiceConnectorResponseTypeDef(TypedDict, total=False):
    VoiceConnector: "VoiceConnectorTypeDef"


class UserErrorTypeDef(TypedDict, total=False):
    UserId: str
    ErrorCode: ErrorCode
    ErrorMessage: str


class UserSettingsTypeDef(TypedDict):
    Telephony: "TelephonySettingsTypeDef"


class _RequiredUserTypeDef(TypedDict):
    UserId: str


class UserTypeDef(_RequiredUserTypeDef, total=False):
    AccountId: str
    PrimaryEmail: str
    PrimaryProvisionedNumber: str
    DisplayName: str
    LicenseType: License
    UserType: UserType
    UserRegistrationStatus: RegistrationStatus
    UserInvitationStatus: InviteStatus
    RegisteredOn: datetime
    InvitedOn: datetime
    AlexaForBusinessMetadata: "AlexaForBusinessMetadataTypeDef"
    PersonalPIN: str


class VoiceConnectorGroupTypeDef(TypedDict, total=False):
    VoiceConnectorGroupId: str
    Name: str
    VoiceConnectorItems: List["VoiceConnectorItemTypeDef"]
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime


class VoiceConnectorItemTypeDef(TypedDict):
    VoiceConnectorId: str
    Priority: int


class VoiceConnectorSettingsTypeDef(TypedDict, total=False):
    CdrBucket: str


class VoiceConnectorTypeDef(TypedDict, total=False):
    VoiceConnectorId: str
    AwsRegion: VoiceConnectorAwsRegion
    Name: str
    OutboundHostName: str
    RequireEncryption: bool
    CreatedTimestamp: datetime
    UpdatedTimestamp: datetime
