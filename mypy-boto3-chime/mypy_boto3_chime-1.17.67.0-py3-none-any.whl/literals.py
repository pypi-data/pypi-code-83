"""
Type annotations for chime service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_chime/literals.html)

Usage::

    ```python
    from mypy_boto3_chime.literals import AccountType

    data: AccountType = "EnterpriseDirectory"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccountType",
    "AppInstanceDataType",
    "BotType",
    "CallingNameStatus",
    "Capability",
    "ChannelMembershipType",
    "ChannelMessagePersistenceType",
    "ChannelMessageType",
    "ChannelMode",
    "ChannelPrivacy",
    "EmailStatus",
    "ErrorCode",
    "GeoMatchLevel",
    "InviteStatus",
    "License",
    "ListAccountsPaginatorName",
    "ListUsersPaginatorName",
    "MemberType",
    "NotificationTarget",
    "NumberSelectionBehavior",
    "OrderedPhoneNumberStatus",
    "OriginationRouteProtocol",
    "PhoneNumberAssociationName",
    "PhoneNumberOrderStatus",
    "PhoneNumberProductType",
    "PhoneNumberStatus",
    "PhoneNumberType",
    "ProxySessionStatus",
    "RegistrationStatus",
    "RoomMembershipRole",
    "SipRuleTriggerType",
    "SortOrder",
    "UserType",
    "VoiceConnectorAwsRegion",
)


AccountType = Literal["EnterpriseDirectory", "EnterpriseLWA", "EnterpriseOIDC", "Team"]
AppInstanceDataType = Literal["Channel", "ChannelMessage"]
BotType = Literal["ChatBot"]
CallingNameStatus = Literal["Unassigned", "UpdateFailed", "UpdateInProgress", "UpdateSucceeded"]
Capability = Literal["SMS", "Voice"]
ChannelMembershipType = Literal["DEFAULT", "HIDDEN"]
ChannelMessagePersistenceType = Literal["NON_PERSISTENT", "PERSISTENT"]
ChannelMessageType = Literal["CONTROL", "STANDARD"]
ChannelMode = Literal["RESTRICTED", "UNRESTRICTED"]
ChannelPrivacy = Literal["PRIVATE", "PUBLIC"]
EmailStatus = Literal["Failed", "NotSent", "Sent"]
ErrorCode = Literal[
    "AccessDenied",
    "BadRequest",
    "Conflict",
    "Forbidden",
    "NotFound",
    "PhoneNumberAssociationsExist",
    "PreconditionFailed",
    "ResourceLimitExceeded",
    "ServiceFailure",
    "ServiceUnavailable",
    "Throttled",
    "Throttling",
    "Unauthorized",
    "Unprocessable",
    "VoiceConnectorGroupAssociationsExist",
]
GeoMatchLevel = Literal["AreaCode", "Country"]
InviteStatus = Literal["Accepted", "Failed", "Pending"]
License = Literal["Basic", "Plus", "Pro", "ProTrial"]
ListAccountsPaginatorName = Literal["list_accounts"]
ListUsersPaginatorName = Literal["list_users"]
MemberType = Literal["Bot", "User", "Webhook"]
NotificationTarget = Literal["EventBridge", "SNS", "SQS"]
NumberSelectionBehavior = Literal["AvoidSticky", "PreferSticky"]
OrderedPhoneNumberStatus = Literal["Acquired", "Failed", "Processing"]
OriginationRouteProtocol = Literal["TCP", "UDP"]
PhoneNumberAssociationName = Literal[
    "AccountId", "SipRuleId", "UserId", "VoiceConnectorGroupId", "VoiceConnectorId"
]
PhoneNumberOrderStatus = Literal["Failed", "Partial", "Processing", "Successful"]
PhoneNumberProductType = Literal["BusinessCalling", "SipMediaApplicationDialIn", "VoiceConnector"]
PhoneNumberStatus = Literal[
    "AcquireFailed",
    "AcquireInProgress",
    "Assigned",
    "DeleteFailed",
    "DeleteInProgress",
    "ReleaseFailed",
    "ReleaseInProgress",
    "Unassigned",
]
PhoneNumberType = Literal["Local", "TollFree"]
ProxySessionStatus = Literal["Closed", "InProgress", "Open"]
RegistrationStatus = Literal["Registered", "Suspended", "Unregistered"]
RoomMembershipRole = Literal["Administrator", "Member"]
SipRuleTriggerType = Literal["RequestUriHostname", "ToPhoneNumber"]
SortOrder = Literal["ASCENDING", "DESCENDING"]
UserType = Literal["PrivateUser", "SharedDevice"]
VoiceConnectorAwsRegion = Literal["us-east-1", "us-west-2"]
