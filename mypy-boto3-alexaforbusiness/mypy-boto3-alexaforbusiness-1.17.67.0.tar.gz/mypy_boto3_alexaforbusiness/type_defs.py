"""
Type annotations for alexaforbusiness service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/type_defs.html)

Usage::

    ```python
    from mypy_boto3_alexaforbusiness.type_defs import AddressBookDataTypeDef

    data: AddressBookDataTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_alexaforbusiness.literals import (
    BusinessReportFailureCode,
    BusinessReportFormat,
    BusinessReportInterval,
    BusinessReportStatus,
    CommsProtocol,
    ConferenceProviderType,
    ConnectionStatus,
    DeviceEventType,
    DeviceStatus,
    DeviceStatusDetailCode,
    DistanceUnit,
    EnablementType,
    EndOfMeetingReminderType,
    EnrollmentStatus,
    Feature,
    NetworkSecurityType,
    PhoneNumberType,
    RequirePin,
    SkillType,
    SortValue,
    TemperatureUnit,
    WakeWord,
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
    "AddressBookDataTypeDef",
    "AddressBookTypeDef",
    "AudioTypeDef",
    "BusinessReportContentRangeTypeDef",
    "BusinessReportRecurrenceTypeDef",
    "BusinessReportS3LocationTypeDef",
    "BusinessReportScheduleTypeDef",
    "BusinessReportTypeDef",
    "CategoryTypeDef",
    "ConferencePreferenceTypeDef",
    "ConferenceProviderTypeDef",
    "ContactDataTypeDef",
    "ContactTypeDef",
    "ContentTypeDef",
    "CreateAddressBookResponseTypeDef",
    "CreateBusinessReportScheduleResponseTypeDef",
    "CreateConferenceProviderResponseTypeDef",
    "CreateContactResponseTypeDef",
    "CreateEndOfMeetingReminderTypeDef",
    "CreateGatewayGroupResponseTypeDef",
    "CreateInstantBookingTypeDef",
    "CreateMeetingRoomConfigurationTypeDef",
    "CreateNetworkProfileResponseTypeDef",
    "CreateProfileResponseTypeDef",
    "CreateRequireCheckInTypeDef",
    "CreateRoomResponseTypeDef",
    "CreateSkillGroupResponseTypeDef",
    "CreateUserResponseTypeDef",
    "DeveloperInfoTypeDef",
    "DeviceDataTypeDef",
    "DeviceEventTypeDef",
    "DeviceNetworkProfileInfoTypeDef",
    "DeviceStatusDetailTypeDef",
    "DeviceStatusInfoTypeDef",
    "DeviceTypeDef",
    "EndOfMeetingReminderTypeDef",
    "FilterTypeDef",
    "GatewayGroupSummaryTypeDef",
    "GatewayGroupTypeDef",
    "GatewaySummaryTypeDef",
    "GatewayTypeDef",
    "GetAddressBookResponseTypeDef",
    "GetConferencePreferenceResponseTypeDef",
    "GetConferenceProviderResponseTypeDef",
    "GetContactResponseTypeDef",
    "GetDeviceResponseTypeDef",
    "GetGatewayGroupResponseTypeDef",
    "GetGatewayResponseTypeDef",
    "GetInvitationConfigurationResponseTypeDef",
    "GetNetworkProfileResponseTypeDef",
    "GetProfileResponseTypeDef",
    "GetRoomResponseTypeDef",
    "GetRoomSkillParameterResponseTypeDef",
    "GetSkillGroupResponseTypeDef",
    "IPDialInTypeDef",
    "InstantBookingTypeDef",
    "ListBusinessReportSchedulesResponseTypeDef",
    "ListConferenceProvidersResponseTypeDef",
    "ListDeviceEventsResponseTypeDef",
    "ListGatewayGroupsResponseTypeDef",
    "ListGatewaysResponseTypeDef",
    "ListSkillsResponseTypeDef",
    "ListSkillsStoreCategoriesResponseTypeDef",
    "ListSkillsStoreSkillsByCategoryResponseTypeDef",
    "ListSmartHomeAppliancesResponseTypeDef",
    "ListTagsResponseTypeDef",
    "MeetingRoomConfigurationTypeDef",
    "MeetingSettingTypeDef",
    "NetworkProfileDataTypeDef",
    "NetworkProfileTypeDef",
    "PSTNDialInTypeDef",
    "PaginatorConfigTypeDef",
    "PhoneNumberTypeDef",
    "ProfileDataTypeDef",
    "ProfileTypeDef",
    "RegisterAVSDeviceResponseTypeDef",
    "RequireCheckInTypeDef",
    "ResolveRoomResponseTypeDef",
    "RoomDataTypeDef",
    "RoomSkillParameterTypeDef",
    "RoomTypeDef",
    "SearchAddressBooksResponseTypeDef",
    "SearchContactsResponseTypeDef",
    "SearchDevicesResponseTypeDef",
    "SearchNetworkProfilesResponseTypeDef",
    "SearchProfilesResponseTypeDef",
    "SearchRoomsResponseTypeDef",
    "SearchSkillGroupsResponseTypeDef",
    "SearchUsersResponseTypeDef",
    "SendAnnouncementResponseTypeDef",
    "SipAddressTypeDef",
    "SkillDetailsTypeDef",
    "SkillGroupDataTypeDef",
    "SkillGroupTypeDef",
    "SkillSummaryTypeDef",
    "SkillsStoreSkillTypeDef",
    "SmartHomeApplianceTypeDef",
    "SortTypeDef",
    "SsmlTypeDef",
    "TagTypeDef",
    "TextTypeDef",
    "UpdateEndOfMeetingReminderTypeDef",
    "UpdateInstantBookingTypeDef",
    "UpdateMeetingRoomConfigurationTypeDef",
    "UpdateRequireCheckInTypeDef",
    "UserDataTypeDef",
)


class AddressBookDataTypeDef(TypedDict, total=False):
    AddressBookArn: str
    Name: str
    Description: str


class AddressBookTypeDef(TypedDict, total=False):
    AddressBookArn: str
    Name: str
    Description: str


class AudioTypeDef(TypedDict):
    Locale: Literal["en-US"]
    Location: str


class BusinessReportContentRangeTypeDef(TypedDict):
    Interval: BusinessReportInterval


class BusinessReportRecurrenceTypeDef(TypedDict, total=False):
    StartDate: str


class BusinessReportS3LocationTypeDef(TypedDict, total=False):
    Path: str
    BucketName: str


class BusinessReportScheduleTypeDef(TypedDict, total=False):
    ScheduleArn: str
    ScheduleName: str
    S3BucketName: str
    S3KeyPrefix: str
    Format: BusinessReportFormat
    ContentRange: "BusinessReportContentRangeTypeDef"
    Recurrence: "BusinessReportRecurrenceTypeDef"
    LastBusinessReport: "BusinessReportTypeDef"


class BusinessReportTypeDef(TypedDict, total=False):
    Status: BusinessReportStatus
    FailureCode: BusinessReportFailureCode
    S3Location: "BusinessReportS3LocationTypeDef"
    DeliveryTime: datetime
    DownloadUrl: str


class CategoryTypeDef(TypedDict, total=False):
    CategoryId: int
    CategoryName: str


class ConferencePreferenceTypeDef(TypedDict, total=False):
    DefaultConferenceProviderArn: str


ConferenceProviderTypeDef = TypedDict(
    "ConferenceProviderTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": ConferenceProviderType,
        "IPDialIn": "IPDialInTypeDef",
        "PSTNDialIn": "PSTNDialInTypeDef",
        "MeetingSetting": "MeetingSettingTypeDef",
    },
    total=False,
)


class ContactDataTypeDef(TypedDict, total=False):
    ContactArn: str
    DisplayName: str
    FirstName: str
    LastName: str
    PhoneNumber: str
    PhoneNumbers: List["PhoneNumberTypeDef"]
    SipAddresses: List["SipAddressTypeDef"]


class ContactTypeDef(TypedDict, total=False):
    ContactArn: str
    DisplayName: str
    FirstName: str
    LastName: str
    PhoneNumber: str
    PhoneNumbers: List["PhoneNumberTypeDef"]
    SipAddresses: List["SipAddressTypeDef"]


class ContentTypeDef(TypedDict, total=False):
    TextList: List["TextTypeDef"]
    SsmlList: List["SsmlTypeDef"]
    AudioList: List["AudioTypeDef"]


class CreateAddressBookResponseTypeDef(TypedDict, total=False):
    AddressBookArn: str


class CreateBusinessReportScheduleResponseTypeDef(TypedDict, total=False):
    ScheduleArn: str


class CreateConferenceProviderResponseTypeDef(TypedDict, total=False):
    ConferenceProviderArn: str


class CreateContactResponseTypeDef(TypedDict, total=False):
    ContactArn: str


class CreateEndOfMeetingReminderTypeDef(TypedDict):
    ReminderAtMinutes: List[int]
    ReminderType: EndOfMeetingReminderType
    Enabled: bool


class CreateGatewayGroupResponseTypeDef(TypedDict, total=False):
    GatewayGroupArn: str


class CreateInstantBookingTypeDef(TypedDict):
    DurationInMinutes: int
    Enabled: bool


class CreateMeetingRoomConfigurationTypeDef(TypedDict, total=False):
    RoomUtilizationMetricsEnabled: bool
    EndOfMeetingReminder: "CreateEndOfMeetingReminderTypeDef"
    InstantBooking: "CreateInstantBookingTypeDef"
    RequireCheckIn: "CreateRequireCheckInTypeDef"


class CreateNetworkProfileResponseTypeDef(TypedDict, total=False):
    NetworkProfileArn: str


class CreateProfileResponseTypeDef(TypedDict, total=False):
    ProfileArn: str


class CreateRequireCheckInTypeDef(TypedDict):
    ReleaseAfterMinutes: int
    Enabled: bool


class CreateRoomResponseTypeDef(TypedDict, total=False):
    RoomArn: str


class CreateSkillGroupResponseTypeDef(TypedDict, total=False):
    SkillGroupArn: str


class CreateUserResponseTypeDef(TypedDict, total=False):
    UserArn: str


class DeveloperInfoTypeDef(TypedDict, total=False):
    DeveloperName: str
    PrivacyPolicy: str
    Email: str
    Url: str


class DeviceDataTypeDef(TypedDict, total=False):
    DeviceArn: str
    DeviceSerialNumber: str
    DeviceType: str
    DeviceName: str
    SoftwareVersion: str
    MacAddress: str
    DeviceStatus: DeviceStatus
    NetworkProfileArn: str
    NetworkProfileName: str
    RoomArn: str
    RoomName: str
    DeviceStatusInfo: "DeviceStatusInfoTypeDef"
    CreatedTime: datetime


DeviceEventTypeDef = TypedDict(
    "DeviceEventTypeDef",
    {"Type": DeviceEventType, "Value": str, "Timestamp": datetime},
    total=False,
)


class DeviceNetworkProfileInfoTypeDef(TypedDict, total=False):
    NetworkProfileArn: str
    CertificateArn: str
    CertificateExpirationTime: datetime


class DeviceStatusDetailTypeDef(TypedDict, total=False):
    Feature: Feature
    Code: DeviceStatusDetailCode


class DeviceStatusInfoTypeDef(TypedDict, total=False):
    DeviceStatusDetails: List["DeviceStatusDetailTypeDef"]
    ConnectionStatus: ConnectionStatus
    ConnectionStatusUpdatedTime: datetime


class DeviceTypeDef(TypedDict, total=False):
    DeviceArn: str
    DeviceSerialNumber: str
    DeviceType: str
    DeviceName: str
    SoftwareVersion: str
    MacAddress: str
    RoomArn: str
    DeviceStatus: DeviceStatus
    DeviceStatusInfo: "DeviceStatusInfoTypeDef"
    NetworkProfileInfo: "DeviceNetworkProfileInfoTypeDef"


class EndOfMeetingReminderTypeDef(TypedDict, total=False):
    ReminderAtMinutes: List[int]
    ReminderType: EndOfMeetingReminderType
    Enabled: bool


class FilterTypeDef(TypedDict):
    Key: str
    Values: List[str]


class GatewayGroupSummaryTypeDef(TypedDict, total=False):
    Arn: str
    Name: str
    Description: str


class GatewayGroupTypeDef(TypedDict, total=False):
    Arn: str
    Name: str
    Description: str


class GatewaySummaryTypeDef(TypedDict, total=False):
    Arn: str
    Name: str
    Description: str
    GatewayGroupArn: str
    SoftwareVersion: str


class GatewayTypeDef(TypedDict, total=False):
    Arn: str
    Name: str
    Description: str
    GatewayGroupArn: str
    SoftwareVersion: str


class GetAddressBookResponseTypeDef(TypedDict, total=False):
    AddressBook: "AddressBookTypeDef"


class GetConferencePreferenceResponseTypeDef(TypedDict, total=False):
    Preference: "ConferencePreferenceTypeDef"


class GetConferenceProviderResponseTypeDef(TypedDict, total=False):
    ConferenceProvider: "ConferenceProviderTypeDef"


class GetContactResponseTypeDef(TypedDict, total=False):
    Contact: "ContactTypeDef"


class GetDeviceResponseTypeDef(TypedDict, total=False):
    Device: "DeviceTypeDef"


class GetGatewayGroupResponseTypeDef(TypedDict, total=False):
    GatewayGroup: "GatewayGroupTypeDef"


class GetGatewayResponseTypeDef(TypedDict, total=False):
    Gateway: "GatewayTypeDef"


class GetInvitationConfigurationResponseTypeDef(TypedDict, total=False):
    OrganizationName: str
    ContactEmail: str
    PrivateSkillIds: List[str]


class GetNetworkProfileResponseTypeDef(TypedDict, total=False):
    NetworkProfile: "NetworkProfileTypeDef"


class GetProfileResponseTypeDef(TypedDict, total=False):
    Profile: "ProfileTypeDef"


class GetRoomResponseTypeDef(TypedDict, total=False):
    Room: "RoomTypeDef"


class GetRoomSkillParameterResponseTypeDef(TypedDict, total=False):
    RoomSkillParameter: "RoomSkillParameterTypeDef"


class GetSkillGroupResponseTypeDef(TypedDict, total=False):
    SkillGroup: "SkillGroupTypeDef"


class IPDialInTypeDef(TypedDict):
    Endpoint: str
    CommsProtocol: CommsProtocol


class InstantBookingTypeDef(TypedDict, total=False):
    DurationInMinutes: int
    Enabled: bool


class ListBusinessReportSchedulesResponseTypeDef(TypedDict, total=False):
    BusinessReportSchedules: List["BusinessReportScheduleTypeDef"]
    NextToken: str


class ListConferenceProvidersResponseTypeDef(TypedDict, total=False):
    ConferenceProviders: List["ConferenceProviderTypeDef"]
    NextToken: str


class ListDeviceEventsResponseTypeDef(TypedDict, total=False):
    DeviceEvents: List["DeviceEventTypeDef"]
    NextToken: str


class ListGatewayGroupsResponseTypeDef(TypedDict, total=False):
    GatewayGroups: List["GatewayGroupSummaryTypeDef"]
    NextToken: str


class ListGatewaysResponseTypeDef(TypedDict, total=False):
    Gateways: List["GatewaySummaryTypeDef"]
    NextToken: str


class ListSkillsResponseTypeDef(TypedDict, total=False):
    SkillSummaries: List["SkillSummaryTypeDef"]
    NextToken: str


class ListSkillsStoreCategoriesResponseTypeDef(TypedDict, total=False):
    CategoryList: List["CategoryTypeDef"]
    NextToken: str


class ListSkillsStoreSkillsByCategoryResponseTypeDef(TypedDict, total=False):
    SkillsStoreSkills: List["SkillsStoreSkillTypeDef"]
    NextToken: str


class ListSmartHomeAppliancesResponseTypeDef(TypedDict, total=False):
    SmartHomeAppliances: List["SmartHomeApplianceTypeDef"]
    NextToken: str


class ListTagsResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]
    NextToken: str


class MeetingRoomConfigurationTypeDef(TypedDict, total=False):
    RoomUtilizationMetricsEnabled: bool
    EndOfMeetingReminder: "EndOfMeetingReminderTypeDef"
    InstantBooking: "InstantBookingTypeDef"
    RequireCheckIn: "RequireCheckInTypeDef"


class MeetingSettingTypeDef(TypedDict):
    RequirePin: RequirePin


class NetworkProfileDataTypeDef(TypedDict, total=False):
    NetworkProfileArn: str
    NetworkProfileName: str
    Description: str
    Ssid: str
    SecurityType: NetworkSecurityType
    EapMethod: Literal["EAP_TLS"]
    CertificateAuthorityArn: str


class NetworkProfileTypeDef(TypedDict, total=False):
    NetworkProfileArn: str
    NetworkProfileName: str
    Description: str
    Ssid: str
    SecurityType: NetworkSecurityType
    EapMethod: Literal["EAP_TLS"]
    CurrentPassword: str
    NextPassword: str
    CertificateAuthorityArn: str
    TrustAnchors: List[str]


class PSTNDialInTypeDef(TypedDict):
    CountryCode: str
    PhoneNumber: str
    OneClickIdDelay: str
    OneClickPinDelay: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


PhoneNumberTypeDef = TypedDict("PhoneNumberTypeDef", {"Number": str, "Type": PhoneNumberType})


class ProfileDataTypeDef(TypedDict, total=False):
    ProfileArn: str
    ProfileName: str
    IsDefault: bool
    Address: str
    Timezone: str
    DistanceUnit: DistanceUnit
    TemperatureUnit: TemperatureUnit
    WakeWord: WakeWord
    Locale: str


class ProfileTypeDef(TypedDict, total=False):
    ProfileArn: str
    ProfileName: str
    IsDefault: bool
    Address: str
    Timezone: str
    DistanceUnit: DistanceUnit
    TemperatureUnit: TemperatureUnit
    WakeWord: WakeWord
    Locale: str
    SetupModeDisabled: bool
    MaxVolumeLimit: int
    PSTNEnabled: bool
    DataRetentionOptIn: bool
    AddressBookArn: str
    MeetingRoomConfiguration: "MeetingRoomConfigurationTypeDef"


class RegisterAVSDeviceResponseTypeDef(TypedDict, total=False):
    DeviceArn: str


class RequireCheckInTypeDef(TypedDict, total=False):
    ReleaseAfterMinutes: int
    Enabled: bool


class ResolveRoomResponseTypeDef(TypedDict, total=False):
    RoomArn: str
    RoomName: str
    RoomSkillParameters: List["RoomSkillParameterTypeDef"]


class RoomDataTypeDef(TypedDict, total=False):
    RoomArn: str
    RoomName: str
    Description: str
    ProviderCalendarId: str
    ProfileArn: str
    ProfileName: str


class RoomSkillParameterTypeDef(TypedDict):
    ParameterKey: str
    ParameterValue: str


class RoomTypeDef(TypedDict, total=False):
    RoomArn: str
    RoomName: str
    Description: str
    ProviderCalendarId: str
    ProfileArn: str


class SearchAddressBooksResponseTypeDef(TypedDict, total=False):
    AddressBooks: List["AddressBookDataTypeDef"]
    NextToken: str
    TotalCount: int


class SearchContactsResponseTypeDef(TypedDict, total=False):
    Contacts: List["ContactDataTypeDef"]
    NextToken: str
    TotalCount: int


class SearchDevicesResponseTypeDef(TypedDict, total=False):
    Devices: List["DeviceDataTypeDef"]
    NextToken: str
    TotalCount: int


class SearchNetworkProfilesResponseTypeDef(TypedDict, total=False):
    NetworkProfiles: List["NetworkProfileDataTypeDef"]
    NextToken: str
    TotalCount: int


class SearchProfilesResponseTypeDef(TypedDict, total=False):
    Profiles: List["ProfileDataTypeDef"]
    NextToken: str
    TotalCount: int


class SearchRoomsResponseTypeDef(TypedDict, total=False):
    Rooms: List["RoomDataTypeDef"]
    NextToken: str
    TotalCount: int


class SearchSkillGroupsResponseTypeDef(TypedDict, total=False):
    SkillGroups: List["SkillGroupDataTypeDef"]
    NextToken: str
    TotalCount: int


class SearchUsersResponseTypeDef(TypedDict, total=False):
    Users: List["UserDataTypeDef"]
    NextToken: str
    TotalCount: int


class SendAnnouncementResponseTypeDef(TypedDict, total=False):
    AnnouncementArn: str


SipAddressTypeDef = TypedDict("SipAddressTypeDef", {"Uri": str, "Type": Literal["WORK"]})


class SkillDetailsTypeDef(TypedDict, total=False):
    ProductDescription: str
    InvocationPhrase: str
    ReleaseDate: str
    EndUserLicenseAgreement: str
    GenericKeywords: List[str]
    BulletPoints: List[str]
    NewInThisVersionBulletPoints: List[str]
    SkillTypes: List[str]
    Reviews: Dict[str, str]
    DeveloperInfo: "DeveloperInfoTypeDef"


class SkillGroupDataTypeDef(TypedDict, total=False):
    SkillGroupArn: str
    SkillGroupName: str
    Description: str


class SkillGroupTypeDef(TypedDict, total=False):
    SkillGroupArn: str
    SkillGroupName: str
    Description: str


class SkillSummaryTypeDef(TypedDict, total=False):
    SkillId: str
    SkillName: str
    SupportsLinking: bool
    EnablementType: EnablementType
    SkillType: SkillType


class SkillsStoreSkillTypeDef(TypedDict, total=False):
    SkillId: str
    SkillName: str
    ShortDescription: str
    IconUrl: str
    SampleUtterances: List[str]
    SkillDetails: "SkillDetailsTypeDef"
    SupportsLinking: bool


class SmartHomeApplianceTypeDef(TypedDict, total=False):
    FriendlyName: str
    Description: str
    ManufacturerName: str


class SortTypeDef(TypedDict):
    Key: str
    Value: SortValue


class SsmlTypeDef(TypedDict):
    Locale: Literal["en-US"]
    Value: str


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TextTypeDef(TypedDict):
    Locale: Literal["en-US"]
    Value: str


class UpdateEndOfMeetingReminderTypeDef(TypedDict, total=False):
    ReminderAtMinutes: List[int]
    ReminderType: EndOfMeetingReminderType
    Enabled: bool


class UpdateInstantBookingTypeDef(TypedDict, total=False):
    DurationInMinutes: int
    Enabled: bool


class UpdateMeetingRoomConfigurationTypeDef(TypedDict, total=False):
    RoomUtilizationMetricsEnabled: bool
    EndOfMeetingReminder: "UpdateEndOfMeetingReminderTypeDef"
    InstantBooking: "UpdateInstantBookingTypeDef"
    RequireCheckIn: "UpdateRequireCheckInTypeDef"


class UpdateRequireCheckInTypeDef(TypedDict, total=False):
    ReleaseAfterMinutes: int
    Enabled: bool


class UserDataTypeDef(TypedDict, total=False):
    UserArn: str
    FirstName: str
    LastName: str
    Email: str
    EnrollmentStatus: EnrollmentStatus
    EnrollmentId: str
