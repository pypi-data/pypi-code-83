"""
Main interface for alexaforbusiness service type definitions.

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
    Locale,
    NetworkEapMethod,
    NetworkSecurityType,
    PhoneNumberType,
    RequirePin,
    SipType,
    SkillType,
    SortValue,
    TemperatureUnit,
    WakeWord,
)

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
    "CreateEndOfMeetingReminderTypeDef",
    "CreateInstantBookingTypeDef",
    "CreateRequireCheckInTypeDef",
    "DeveloperInfoTypeDef",
    "DeviceDataTypeDef",
    "DeviceEventTypeDef",
    "DeviceNetworkProfileInfoTypeDef",
    "DeviceStatusDetailTypeDef",
    "DeviceStatusInfoTypeDef",
    "DeviceTypeDef",
    "EndOfMeetingReminderTypeDef",
    "GatewayGroupSummaryTypeDef",
    "GatewayGroupTypeDef",
    "GatewaySummaryTypeDef",
    "GatewayTypeDef",
    "IPDialInTypeDef",
    "InstantBookingTypeDef",
    "MeetingRoomConfigurationTypeDef",
    "MeetingSettingTypeDef",
    "NetworkProfileDataTypeDef",
    "NetworkProfileTypeDef",
    "PSTNDialInTypeDef",
    "PhoneNumberTypeDef",
    "ProfileDataTypeDef",
    "ProfileTypeDef",
    "RequireCheckInTypeDef",
    "RoomDataTypeDef",
    "RoomSkillParameterTypeDef",
    "RoomTypeDef",
    "SipAddressTypeDef",
    "SkillDetailsTypeDef",
    "SkillGroupDataTypeDef",
    "SkillGroupTypeDef",
    "SkillSummaryTypeDef",
    "SkillsStoreSkillTypeDef",
    "SmartHomeApplianceTypeDef",
    "SsmlTypeDef",
    "TagTypeDef",
    "TextTypeDef",
    "UpdateEndOfMeetingReminderTypeDef",
    "UpdateInstantBookingTypeDef",
    "UpdateRequireCheckInTypeDef",
    "UserDataTypeDef",
    "ContentTypeDef",
    "CreateAddressBookResponseTypeDef",
    "CreateBusinessReportScheduleResponseTypeDef",
    "CreateConferenceProviderResponseTypeDef",
    "CreateContactResponseTypeDef",
    "CreateGatewayGroupResponseTypeDef",
    "CreateMeetingRoomConfigurationTypeDef",
    "CreateNetworkProfileResponseTypeDef",
    "CreateProfileResponseTypeDef",
    "CreateRoomResponseTypeDef",
    "CreateSkillGroupResponseTypeDef",
    "CreateUserResponseTypeDef",
    "FilterTypeDef",
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
    "PaginatorConfigTypeDef",
    "RegisterAVSDeviceResponseTypeDef",
    "ResolveRoomResponseTypeDef",
    "SearchAddressBooksResponseTypeDef",
    "SearchContactsResponseTypeDef",
    "SearchDevicesResponseTypeDef",
    "SearchNetworkProfilesResponseTypeDef",
    "SearchProfilesResponseTypeDef",
    "SearchRoomsResponseTypeDef",
    "SearchSkillGroupsResponseTypeDef",
    "SearchUsersResponseTypeDef",
    "SendAnnouncementResponseTypeDef",
    "SortTypeDef",
    "UpdateMeetingRoomConfigurationTypeDef",
)

AddressBookDataTypeDef = TypedDict(
    "AddressBookDataTypeDef", {"AddressBookArn": str, "Name": str, "Description": str}, total=False
)

AddressBookTypeDef = TypedDict(
    "AddressBookTypeDef", {"AddressBookArn": str, "Name": str, "Description": str}, total=False
)

AudioTypeDef = TypedDict("AudioTypeDef", {"Locale": Locale, "Location": str})

BusinessReportContentRangeTypeDef = TypedDict(
    "BusinessReportContentRangeTypeDef", {"Interval": BusinessReportInterval}
)

BusinessReportRecurrenceTypeDef = TypedDict(
    "BusinessReportRecurrenceTypeDef", {"StartDate": str}, total=False
)

BusinessReportS3LocationTypeDef = TypedDict(
    "BusinessReportS3LocationTypeDef", {"Path": str, "BucketName": str}, total=False
)

BusinessReportScheduleTypeDef = TypedDict(
    "BusinessReportScheduleTypeDef",
    {
        "ScheduleArn": str,
        "ScheduleName": str,
        "S3BucketName": str,
        "S3KeyPrefix": str,
        "Format": BusinessReportFormat,
        "ContentRange": "BusinessReportContentRangeTypeDef",
        "Recurrence": "BusinessReportRecurrenceTypeDef",
        "LastBusinessReport": "BusinessReportTypeDef",
    },
    total=False,
)

BusinessReportTypeDef = TypedDict(
    "BusinessReportTypeDef",
    {
        "Status": BusinessReportStatus,
        "FailureCode": BusinessReportFailureCode,
        "S3Location": "BusinessReportS3LocationTypeDef",
        "DeliveryTime": datetime,
        "DownloadUrl": str,
    },
    total=False,
)

CategoryTypeDef = TypedDict(
    "CategoryTypeDef", {"CategoryId": int, "CategoryName": str}, total=False
)

ConferencePreferenceTypeDef = TypedDict(
    "ConferencePreferenceTypeDef", {"DefaultConferenceProviderArn": str}, total=False
)

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

ContactDataTypeDef = TypedDict(
    "ContactDataTypeDef",
    {
        "ContactArn": str,
        "DisplayName": str,
        "FirstName": str,
        "LastName": str,
        "PhoneNumber": str,
        "PhoneNumbers": List["PhoneNumberTypeDef"],
        "SipAddresses": List["SipAddressTypeDef"],
    },
    total=False,
)

ContactTypeDef = TypedDict(
    "ContactTypeDef",
    {
        "ContactArn": str,
        "DisplayName": str,
        "FirstName": str,
        "LastName": str,
        "PhoneNumber": str,
        "PhoneNumbers": List["PhoneNumberTypeDef"],
        "SipAddresses": List["SipAddressTypeDef"],
    },
    total=False,
)

CreateEndOfMeetingReminderTypeDef = TypedDict(
    "CreateEndOfMeetingReminderTypeDef",
    {"ReminderAtMinutes": List[int], "ReminderType": EndOfMeetingReminderType, "Enabled": bool},
)

CreateInstantBookingTypeDef = TypedDict(
    "CreateInstantBookingTypeDef", {"DurationInMinutes": int, "Enabled": bool}
)

CreateRequireCheckInTypeDef = TypedDict(
    "CreateRequireCheckInTypeDef", {"ReleaseAfterMinutes": int, "Enabled": bool}
)

DeveloperInfoTypeDef = TypedDict(
    "DeveloperInfoTypeDef",
    {"DeveloperName": str, "PrivacyPolicy": str, "Email": str, "Url": str},
    total=False,
)

DeviceDataTypeDef = TypedDict(
    "DeviceDataTypeDef",
    {
        "DeviceArn": str,
        "DeviceSerialNumber": str,
        "DeviceType": str,
        "DeviceName": str,
        "SoftwareVersion": str,
        "MacAddress": str,
        "DeviceStatus": DeviceStatus,
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "RoomArn": str,
        "RoomName": str,
        "DeviceStatusInfo": "DeviceStatusInfoTypeDef",
        "CreatedTime": datetime,
    },
    total=False,
)

DeviceEventTypeDef = TypedDict(
    "DeviceEventTypeDef",
    {"Type": DeviceEventType, "Value": str, "Timestamp": datetime},
    total=False,
)

DeviceNetworkProfileInfoTypeDef = TypedDict(
    "DeviceNetworkProfileInfoTypeDef",
    {"NetworkProfileArn": str, "CertificateArn": str, "CertificateExpirationTime": datetime},
    total=False,
)

DeviceStatusDetailTypeDef = TypedDict(
    "DeviceStatusDetailTypeDef", {"Feature": Feature, "Code": DeviceStatusDetailCode}, total=False
)

DeviceStatusInfoTypeDef = TypedDict(
    "DeviceStatusInfoTypeDef",
    {
        "DeviceStatusDetails": List["DeviceStatusDetailTypeDef"],
        "ConnectionStatus": ConnectionStatus,
        "ConnectionStatusUpdatedTime": datetime,
    },
    total=False,
)

DeviceTypeDef = TypedDict(
    "DeviceTypeDef",
    {
        "DeviceArn": str,
        "DeviceSerialNumber": str,
        "DeviceType": str,
        "DeviceName": str,
        "SoftwareVersion": str,
        "MacAddress": str,
        "RoomArn": str,
        "DeviceStatus": DeviceStatus,
        "DeviceStatusInfo": "DeviceStatusInfoTypeDef",
        "NetworkProfileInfo": "DeviceNetworkProfileInfoTypeDef",
    },
    total=False,
)

EndOfMeetingReminderTypeDef = TypedDict(
    "EndOfMeetingReminderTypeDef",
    {"ReminderAtMinutes": List[int], "ReminderType": EndOfMeetingReminderType, "Enabled": bool},
    total=False,
)

GatewayGroupSummaryTypeDef = TypedDict(
    "GatewayGroupSummaryTypeDef", {"Arn": str, "Name": str, "Description": str}, total=False
)

GatewayGroupTypeDef = TypedDict(
    "GatewayGroupTypeDef", {"Arn": str, "Name": str, "Description": str}, total=False
)

GatewaySummaryTypeDef = TypedDict(
    "GatewaySummaryTypeDef",
    {"Arn": str, "Name": str, "Description": str, "GatewayGroupArn": str, "SoftwareVersion": str},
    total=False,
)

GatewayTypeDef = TypedDict(
    "GatewayTypeDef",
    {"Arn": str, "Name": str, "Description": str, "GatewayGroupArn": str, "SoftwareVersion": str},
    total=False,
)

IPDialInTypeDef = TypedDict("IPDialInTypeDef", {"Endpoint": str, "CommsProtocol": CommsProtocol})

InstantBookingTypeDef = TypedDict(
    "InstantBookingTypeDef", {"DurationInMinutes": int, "Enabled": bool}, total=False
)

MeetingRoomConfigurationTypeDef = TypedDict(
    "MeetingRoomConfigurationTypeDef",
    {
        "RoomUtilizationMetricsEnabled": bool,
        "EndOfMeetingReminder": "EndOfMeetingReminderTypeDef",
        "InstantBooking": "InstantBookingTypeDef",
        "RequireCheckIn": "RequireCheckInTypeDef",
    },
    total=False,
)

MeetingSettingTypeDef = TypedDict("MeetingSettingTypeDef", {"RequirePin": RequirePin})

NetworkProfileDataTypeDef = TypedDict(
    "NetworkProfileDataTypeDef",
    {
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "Description": str,
        "Ssid": str,
        "SecurityType": NetworkSecurityType,
        "EapMethod": NetworkEapMethod,
        "CertificateAuthorityArn": str,
    },
    total=False,
)

NetworkProfileTypeDef = TypedDict(
    "NetworkProfileTypeDef",
    {
        "NetworkProfileArn": str,
        "NetworkProfileName": str,
        "Description": str,
        "Ssid": str,
        "SecurityType": NetworkSecurityType,
        "EapMethod": NetworkEapMethod,
        "CurrentPassword": str,
        "NextPassword": str,
        "CertificateAuthorityArn": str,
        "TrustAnchors": List[str],
    },
    total=False,
)

PSTNDialInTypeDef = TypedDict(
    "PSTNDialInTypeDef",
    {"CountryCode": str, "PhoneNumber": str, "OneClickIdDelay": str, "OneClickPinDelay": str},
)

PhoneNumberTypeDef = TypedDict("PhoneNumberTypeDef", {"Number": str, "Type": PhoneNumberType})

ProfileDataTypeDef = TypedDict(
    "ProfileDataTypeDef",
    {
        "ProfileArn": str,
        "ProfileName": str,
        "IsDefault": bool,
        "Address": str,
        "Timezone": str,
        "DistanceUnit": DistanceUnit,
        "TemperatureUnit": TemperatureUnit,
        "WakeWord": WakeWord,
        "Locale": str,
    },
    total=False,
)

ProfileTypeDef = TypedDict(
    "ProfileTypeDef",
    {
        "ProfileArn": str,
        "ProfileName": str,
        "IsDefault": bool,
        "Address": str,
        "Timezone": str,
        "DistanceUnit": DistanceUnit,
        "TemperatureUnit": TemperatureUnit,
        "WakeWord": WakeWord,
        "Locale": str,
        "SetupModeDisabled": bool,
        "MaxVolumeLimit": int,
        "PSTNEnabled": bool,
        "DataRetentionOptIn": bool,
        "AddressBookArn": str,
        "MeetingRoomConfiguration": "MeetingRoomConfigurationTypeDef",
    },
    total=False,
)

RequireCheckInTypeDef = TypedDict(
    "RequireCheckInTypeDef", {"ReleaseAfterMinutes": int, "Enabled": bool}, total=False
)

RoomDataTypeDef = TypedDict(
    "RoomDataTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "Description": str,
        "ProviderCalendarId": str,
        "ProfileArn": str,
        "ProfileName": str,
    },
    total=False,
)

RoomSkillParameterTypeDef = TypedDict(
    "RoomSkillParameterTypeDef", {"ParameterKey": str, "ParameterValue": str}
)

RoomTypeDef = TypedDict(
    "RoomTypeDef",
    {
        "RoomArn": str,
        "RoomName": str,
        "Description": str,
        "ProviderCalendarId": str,
        "ProfileArn": str,
    },
    total=False,
)

SipAddressTypeDef = TypedDict("SipAddressTypeDef", {"Uri": str, "Type": SipType})

SkillDetailsTypeDef = TypedDict(
    "SkillDetailsTypeDef",
    {
        "ProductDescription": str,
        "InvocationPhrase": str,
        "ReleaseDate": str,
        "EndUserLicenseAgreement": str,
        "GenericKeywords": List[str],
        "BulletPoints": List[str],
        "NewInThisVersionBulletPoints": List[str],
        "SkillTypes": List[str],
        "Reviews": Dict[str, str],
        "DeveloperInfo": "DeveloperInfoTypeDef",
    },
    total=False,
)

SkillGroupDataTypeDef = TypedDict(
    "SkillGroupDataTypeDef",
    {"SkillGroupArn": str, "SkillGroupName": str, "Description": str},
    total=False,
)

SkillGroupTypeDef = TypedDict(
    "SkillGroupTypeDef",
    {"SkillGroupArn": str, "SkillGroupName": str, "Description": str},
    total=False,
)

SkillSummaryTypeDef = TypedDict(
    "SkillSummaryTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "SupportsLinking": bool,
        "EnablementType": EnablementType,
        "SkillType": SkillType,
    },
    total=False,
)

SkillsStoreSkillTypeDef = TypedDict(
    "SkillsStoreSkillTypeDef",
    {
        "SkillId": str,
        "SkillName": str,
        "ShortDescription": str,
        "IconUrl": str,
        "SampleUtterances": List[str],
        "SkillDetails": "SkillDetailsTypeDef",
        "SupportsLinking": bool,
    },
    total=False,
)

SmartHomeApplianceTypeDef = TypedDict(
    "SmartHomeApplianceTypeDef",
    {"FriendlyName": str, "Description": str, "ManufacturerName": str},
    total=False,
)

SsmlTypeDef = TypedDict("SsmlTypeDef", {"Locale": Locale, "Value": str})

TagTypeDef = TypedDict("TagTypeDef", {"Key": str, "Value": str})

TextTypeDef = TypedDict("TextTypeDef", {"Locale": Locale, "Value": str})

UpdateEndOfMeetingReminderTypeDef = TypedDict(
    "UpdateEndOfMeetingReminderTypeDef",
    {"ReminderAtMinutes": List[int], "ReminderType": EndOfMeetingReminderType, "Enabled": bool},
    total=False,
)

UpdateInstantBookingTypeDef = TypedDict(
    "UpdateInstantBookingTypeDef", {"DurationInMinutes": int, "Enabled": bool}, total=False
)

UpdateRequireCheckInTypeDef = TypedDict(
    "UpdateRequireCheckInTypeDef", {"ReleaseAfterMinutes": int, "Enabled": bool}, total=False
)

UserDataTypeDef = TypedDict(
    "UserDataTypeDef",
    {
        "UserArn": str,
        "FirstName": str,
        "LastName": str,
        "Email": str,
        "EnrollmentStatus": EnrollmentStatus,
        "EnrollmentId": str,
    },
    total=False,
)

ContentTypeDef = TypedDict(
    "ContentTypeDef",
    {
        "TextList": List["TextTypeDef"],
        "SsmlList": List["SsmlTypeDef"],
        "AudioList": List["AudioTypeDef"],
    },
    total=False,
)

CreateAddressBookResponseTypeDef = TypedDict(
    "CreateAddressBookResponseTypeDef", {"AddressBookArn": str}, total=False
)

CreateBusinessReportScheduleResponseTypeDef = TypedDict(
    "CreateBusinessReportScheduleResponseTypeDef", {"ScheduleArn": str}, total=False
)

CreateConferenceProviderResponseTypeDef = TypedDict(
    "CreateConferenceProviderResponseTypeDef", {"ConferenceProviderArn": str}, total=False
)

CreateContactResponseTypeDef = TypedDict(
    "CreateContactResponseTypeDef", {"ContactArn": str}, total=False
)

CreateGatewayGroupResponseTypeDef = TypedDict(
    "CreateGatewayGroupResponseTypeDef", {"GatewayGroupArn": str}, total=False
)

CreateMeetingRoomConfigurationTypeDef = TypedDict(
    "CreateMeetingRoomConfigurationTypeDef",
    {
        "RoomUtilizationMetricsEnabled": bool,
        "EndOfMeetingReminder": "CreateEndOfMeetingReminderTypeDef",
        "InstantBooking": "CreateInstantBookingTypeDef",
        "RequireCheckIn": "CreateRequireCheckInTypeDef",
    },
    total=False,
)

CreateNetworkProfileResponseTypeDef = TypedDict(
    "CreateNetworkProfileResponseTypeDef", {"NetworkProfileArn": str}, total=False
)

CreateProfileResponseTypeDef = TypedDict(
    "CreateProfileResponseTypeDef", {"ProfileArn": str}, total=False
)

CreateRoomResponseTypeDef = TypedDict("CreateRoomResponseTypeDef", {"RoomArn": str}, total=False)

CreateSkillGroupResponseTypeDef = TypedDict(
    "CreateSkillGroupResponseTypeDef", {"SkillGroupArn": str}, total=False
)

CreateUserResponseTypeDef = TypedDict("CreateUserResponseTypeDef", {"UserArn": str}, total=False)

FilterTypeDef = TypedDict("FilterTypeDef", {"Key": str, "Values": List[str]})

GetAddressBookResponseTypeDef = TypedDict(
    "GetAddressBookResponseTypeDef", {"AddressBook": "AddressBookTypeDef"}, total=False
)

GetConferencePreferenceResponseTypeDef = TypedDict(
    "GetConferencePreferenceResponseTypeDef",
    {"Preference": "ConferencePreferenceTypeDef"},
    total=False,
)

GetConferenceProviderResponseTypeDef = TypedDict(
    "GetConferenceProviderResponseTypeDef",
    {"ConferenceProvider": "ConferenceProviderTypeDef"},
    total=False,
)

GetContactResponseTypeDef = TypedDict(
    "GetContactResponseTypeDef", {"Contact": "ContactTypeDef"}, total=False
)

GetDeviceResponseTypeDef = TypedDict(
    "GetDeviceResponseTypeDef", {"Device": "DeviceTypeDef"}, total=False
)

GetGatewayGroupResponseTypeDef = TypedDict(
    "GetGatewayGroupResponseTypeDef", {"GatewayGroup": "GatewayGroupTypeDef"}, total=False
)

GetGatewayResponseTypeDef = TypedDict(
    "GetGatewayResponseTypeDef", {"Gateway": "GatewayTypeDef"}, total=False
)

GetInvitationConfigurationResponseTypeDef = TypedDict(
    "GetInvitationConfigurationResponseTypeDef",
    {"OrganizationName": str, "ContactEmail": str, "PrivateSkillIds": List[str]},
    total=False,
)

GetNetworkProfileResponseTypeDef = TypedDict(
    "GetNetworkProfileResponseTypeDef", {"NetworkProfile": "NetworkProfileTypeDef"}, total=False
)

GetProfileResponseTypeDef = TypedDict(
    "GetProfileResponseTypeDef", {"Profile": "ProfileTypeDef"}, total=False
)

GetRoomResponseTypeDef = TypedDict("GetRoomResponseTypeDef", {"Room": "RoomTypeDef"}, total=False)

GetRoomSkillParameterResponseTypeDef = TypedDict(
    "GetRoomSkillParameterResponseTypeDef",
    {"RoomSkillParameter": "RoomSkillParameterTypeDef"},
    total=False,
)

GetSkillGroupResponseTypeDef = TypedDict(
    "GetSkillGroupResponseTypeDef", {"SkillGroup": "SkillGroupTypeDef"}, total=False
)

ListBusinessReportSchedulesResponseTypeDef = TypedDict(
    "ListBusinessReportSchedulesResponseTypeDef",
    {"BusinessReportSchedules": List["BusinessReportScheduleTypeDef"], "NextToken": str},
    total=False,
)

ListConferenceProvidersResponseTypeDef = TypedDict(
    "ListConferenceProvidersResponseTypeDef",
    {"ConferenceProviders": List["ConferenceProviderTypeDef"], "NextToken": str},
    total=False,
)

ListDeviceEventsResponseTypeDef = TypedDict(
    "ListDeviceEventsResponseTypeDef",
    {"DeviceEvents": List["DeviceEventTypeDef"], "NextToken": str},
    total=False,
)

ListGatewayGroupsResponseTypeDef = TypedDict(
    "ListGatewayGroupsResponseTypeDef",
    {"GatewayGroups": List["GatewayGroupSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListGatewaysResponseTypeDef = TypedDict(
    "ListGatewaysResponseTypeDef",
    {"Gateways": List["GatewaySummaryTypeDef"], "NextToken": str},
    total=False,
)

ListSkillsResponseTypeDef = TypedDict(
    "ListSkillsResponseTypeDef",
    {"SkillSummaries": List["SkillSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListSkillsStoreCategoriesResponseTypeDef = TypedDict(
    "ListSkillsStoreCategoriesResponseTypeDef",
    {"CategoryList": List["CategoryTypeDef"], "NextToken": str},
    total=False,
)

ListSkillsStoreSkillsByCategoryResponseTypeDef = TypedDict(
    "ListSkillsStoreSkillsByCategoryResponseTypeDef",
    {"SkillsStoreSkills": List["SkillsStoreSkillTypeDef"], "NextToken": str},
    total=False,
)

ListSmartHomeAppliancesResponseTypeDef = TypedDict(
    "ListSmartHomeAppliancesResponseTypeDef",
    {"SmartHomeAppliances": List["SmartHomeApplianceTypeDef"], "NextToken": str},
    total=False,
)

ListTagsResponseTypeDef = TypedDict(
    "ListTagsResponseTypeDef", {"Tags": List["TagTypeDef"], "NextToken": str}, total=False
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

RegisterAVSDeviceResponseTypeDef = TypedDict(
    "RegisterAVSDeviceResponseTypeDef", {"DeviceArn": str}, total=False
)

ResolveRoomResponseTypeDef = TypedDict(
    "ResolveRoomResponseTypeDef",
    {"RoomArn": str, "RoomName": str, "RoomSkillParameters": List["RoomSkillParameterTypeDef"]},
    total=False,
)

SearchAddressBooksResponseTypeDef = TypedDict(
    "SearchAddressBooksResponseTypeDef",
    {"AddressBooks": List["AddressBookDataTypeDef"], "NextToken": str, "TotalCount": int},
    total=False,
)

SearchContactsResponseTypeDef = TypedDict(
    "SearchContactsResponseTypeDef",
    {"Contacts": List["ContactDataTypeDef"], "NextToken": str, "TotalCount": int},
    total=False,
)

SearchDevicesResponseTypeDef = TypedDict(
    "SearchDevicesResponseTypeDef",
    {"Devices": List["DeviceDataTypeDef"], "NextToken": str, "TotalCount": int},
    total=False,
)

SearchNetworkProfilesResponseTypeDef = TypedDict(
    "SearchNetworkProfilesResponseTypeDef",
    {"NetworkProfiles": List["NetworkProfileDataTypeDef"], "NextToken": str, "TotalCount": int},
    total=False,
)

SearchProfilesResponseTypeDef = TypedDict(
    "SearchProfilesResponseTypeDef",
    {"Profiles": List["ProfileDataTypeDef"], "NextToken": str, "TotalCount": int},
    total=False,
)

SearchRoomsResponseTypeDef = TypedDict(
    "SearchRoomsResponseTypeDef",
    {"Rooms": List["RoomDataTypeDef"], "NextToken": str, "TotalCount": int},
    total=False,
)

SearchSkillGroupsResponseTypeDef = TypedDict(
    "SearchSkillGroupsResponseTypeDef",
    {"SkillGroups": List["SkillGroupDataTypeDef"], "NextToken": str, "TotalCount": int},
    total=False,
)

SearchUsersResponseTypeDef = TypedDict(
    "SearchUsersResponseTypeDef",
    {"Users": List["UserDataTypeDef"], "NextToken": str, "TotalCount": int},
    total=False,
)

SendAnnouncementResponseTypeDef = TypedDict(
    "SendAnnouncementResponseTypeDef", {"AnnouncementArn": str}, total=False
)

SortTypeDef = TypedDict("SortTypeDef", {"Key": str, "Value": SortValue})

UpdateMeetingRoomConfigurationTypeDef = TypedDict(
    "UpdateMeetingRoomConfigurationTypeDef",
    {
        "RoomUtilizationMetricsEnabled": bool,
        "EndOfMeetingReminder": "UpdateEndOfMeetingReminderTypeDef",
        "InstantBooking": "UpdateInstantBookingTypeDef",
        "RequireCheckIn": "UpdateRequireCheckInTypeDef",
    },
    total=False,
)
