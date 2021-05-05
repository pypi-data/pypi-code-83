"""
Type annotations for alexaforbusiness service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_alexaforbusiness/literals.html)

Usage::

    ```python
    from mypy_boto3_alexaforbusiness.literals import BusinessReportFailureCode

    data: BusinessReportFailureCode = "ACCESS_DENIED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BusinessReportFailureCode",
    "BusinessReportFormat",
    "BusinessReportInterval",
    "BusinessReportStatus",
    "CommsProtocol",
    "ConferenceProviderType",
    "ConnectionStatus",
    "DeviceEventType",
    "DeviceStatus",
    "DeviceStatusDetailCode",
    "DeviceUsageType",
    "DistanceUnit",
    "EnablementType",
    "EnablementTypeFilter",
    "EndOfMeetingReminderType",
    "EnrollmentStatus",
    "Feature",
    "ListBusinessReportSchedulesPaginatorName",
    "ListConferenceProvidersPaginatorName",
    "ListDeviceEventsPaginatorName",
    "ListSkillsPaginatorName",
    "ListSkillsStoreCategoriesPaginatorName",
    "ListSkillsStoreSkillsByCategoryPaginatorName",
    "ListSmartHomeAppliancesPaginatorName",
    "ListTagsPaginatorName",
    "Locale",
    "NetworkEapMethod",
    "NetworkSecurityType",
    "PhoneNumberType",
    "RequirePin",
    "SearchDevicesPaginatorName",
    "SearchProfilesPaginatorName",
    "SearchRoomsPaginatorName",
    "SearchSkillGroupsPaginatorName",
    "SearchUsersPaginatorName",
    "SipType",
    "SkillType",
    "SkillTypeFilter",
    "SortValue",
    "TemperatureUnit",
    "WakeWord",
)


BusinessReportFailureCode = Literal["ACCESS_DENIED", "INTERNAL_FAILURE", "NO_SUCH_BUCKET"]
BusinessReportFormat = Literal["CSV", "CSV_ZIP"]
BusinessReportInterval = Literal["ONE_DAY", "ONE_WEEK", "THIRTY_DAYS"]
BusinessReportStatus = Literal["FAILED", "RUNNING", "SUCCEEDED"]
CommsProtocol = Literal["H323", "SIP", "SIPS"]
ConferenceProviderType = Literal[
    "BLUEJEANS",
    "CHIME",
    "CUSTOM",
    "FUZE",
    "GOOGLE_HANGOUTS",
    "POLYCOM",
    "RINGCENTRAL",
    "SKYPE_FOR_BUSINESS",
    "WEBEX",
    "ZOOM",
]
ConnectionStatus = Literal["OFFLINE", "ONLINE"]
DeviceEventType = Literal["CONNECTION_STATUS", "DEVICE_STATUS"]
DeviceStatus = Literal["DEREGISTERED", "FAILED", "PENDING", "READY", "WAS_OFFLINE"]
DeviceStatusDetailCode = Literal[
    "ASSOCIATION_REJECTION",
    "AUTHENTICATION_FAILURE",
    "CERTIFICATE_AUTHORITY_ACCESS_DENIED",
    "CERTIFICATE_ISSUING_LIMIT_EXCEEDED",
    "CREDENTIALS_ACCESS_FAILURE",
    "DEVICE_SOFTWARE_UPDATE_NEEDED",
    "DEVICE_WAS_OFFLINE",
    "DHCP_FAILURE",
    "DNS_FAILURE",
    "INTERNET_UNAVAILABLE",
    "INVALID_CERTIFICATE_AUTHORITY",
    "INVALID_PASSWORD_STATE",
    "NETWORK_PROFILE_NOT_FOUND",
    "PASSWORD_MANAGER_ACCESS_DENIED",
    "PASSWORD_NOT_FOUND",
    "TLS_VERSION_MISMATCH",
    "UNKNOWN_FAILURE",
]
DeviceUsageType = Literal["VOICE"]
DistanceUnit = Literal["IMPERIAL", "METRIC"]
EnablementType = Literal["ENABLED", "PENDING"]
EnablementTypeFilter = Literal["ENABLED", "PENDING"]
EndOfMeetingReminderType = Literal[
    "ANNOUNCEMENT_TIME_CHECK", "ANNOUNCEMENT_VARIABLE_TIME_LEFT", "CHIME", "KNOCK"
]
EnrollmentStatus = Literal[
    "DEREGISTERING", "DISASSOCIATING", "INITIALIZED", "PENDING", "REGISTERED"
]
Feature = Literal[
    "ALL", "BLUETOOTH", "LISTS", "NETWORK_PROFILE", "NOTIFICATIONS", "SETTINGS", "SKILLS", "VOLUME"
]
ListBusinessReportSchedulesPaginatorName = Literal["list_business_report_schedules"]
ListConferenceProvidersPaginatorName = Literal["list_conference_providers"]
ListDeviceEventsPaginatorName = Literal["list_device_events"]
ListSkillsPaginatorName = Literal["list_skills"]
ListSkillsStoreCategoriesPaginatorName = Literal["list_skills_store_categories"]
ListSkillsStoreSkillsByCategoryPaginatorName = Literal["list_skills_store_skills_by_category"]
ListSmartHomeAppliancesPaginatorName = Literal["list_smart_home_appliances"]
ListTagsPaginatorName = Literal["list_tags"]
Locale = Literal["en-US"]
NetworkEapMethod = Literal["EAP_TLS"]
NetworkSecurityType = Literal["OPEN", "WEP", "WPA2_ENTERPRISE", "WPA2_PSK", "WPA_PSK"]
PhoneNumberType = Literal["HOME", "MOBILE", "WORK"]
RequirePin = Literal["NO", "OPTIONAL", "YES"]
SearchDevicesPaginatorName = Literal["search_devices"]
SearchProfilesPaginatorName = Literal["search_profiles"]
SearchRoomsPaginatorName = Literal["search_rooms"]
SearchSkillGroupsPaginatorName = Literal["search_skill_groups"]
SearchUsersPaginatorName = Literal["search_users"]
SipType = Literal["WORK"]
SkillType = Literal["PRIVATE", "PUBLIC"]
SkillTypeFilter = Literal["ALL", "PRIVATE", "PUBLIC"]
SortValue = Literal["ASC", "DESC"]
TemperatureUnit = Literal["CELSIUS", "FAHRENHEIT"]
WakeWord = Literal["ALEXA", "AMAZON", "COMPUTER", "ECHO"]
