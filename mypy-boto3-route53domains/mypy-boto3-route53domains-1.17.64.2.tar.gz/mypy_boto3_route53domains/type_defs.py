"""
Type annotations for route53domains service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_route53domains/type_defs.html)

Usage::

    ```python
    from mypy_boto3_route53domains.type_defs import AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef

    data: AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_route53domains.literals import (
    ContactType,
    CountryCode,
    DomainAvailability,
    ExtraParamName,
    OperationStatus,
    OperationType,
    ReachabilityStatus,
    Transferable,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef",
    "BillingRecordTypeDef",
    "CancelDomainTransferToAnotherAwsAccountResponseTypeDef",
    "CheckDomainAvailabilityResponseTypeDef",
    "CheckDomainTransferabilityResponseTypeDef",
    "ContactDetailTypeDef",
    "DisableDomainTransferLockResponseTypeDef",
    "DomainSuggestionTypeDef",
    "DomainSummaryTypeDef",
    "DomainTransferabilityTypeDef",
    "EnableDomainTransferLockResponseTypeDef",
    "ExtraParamTypeDef",
    "GetContactReachabilityStatusResponseTypeDef",
    "GetDomainDetailResponseTypeDef",
    "GetDomainSuggestionsResponseTypeDef",
    "GetOperationDetailResponseTypeDef",
    "ListDomainsResponseTypeDef",
    "ListOperationsResponseTypeDef",
    "ListTagsForDomainResponseTypeDef",
    "NameserverTypeDef",
    "OperationSummaryTypeDef",
    "PaginatorConfigTypeDef",
    "RegisterDomainResponseTypeDef",
    "RejectDomainTransferFromAnotherAwsAccountResponseTypeDef",
    "RenewDomainResponseTypeDef",
    "ResendContactReachabilityEmailResponseTypeDef",
    "RetrieveDomainAuthCodeResponseTypeDef",
    "TagTypeDef",
    "TransferDomainResponseTypeDef",
    "TransferDomainToAnotherAwsAccountResponseTypeDef",
    "UpdateDomainContactPrivacyResponseTypeDef",
    "UpdateDomainContactResponseTypeDef",
    "UpdateDomainNameserversResponseTypeDef",
    "ViewBillingResponseTypeDef",
)


class AcceptDomainTransferFromAnotherAwsAccountResponseTypeDef(TypedDict, total=False):
    OperationId: str


class BillingRecordTypeDef(TypedDict, total=False):
    DomainName: str
    Operation: OperationType
    InvoiceId: str
    BillDate: datetime
    Price: float


class CancelDomainTransferToAnotherAwsAccountResponseTypeDef(TypedDict, total=False):
    OperationId: str


class CheckDomainAvailabilityResponseTypeDef(TypedDict):
    Availability: DomainAvailability


class CheckDomainTransferabilityResponseTypeDef(TypedDict):
    Transferability: "DomainTransferabilityTypeDef"


class ContactDetailTypeDef(TypedDict, total=False):
    FirstName: str
    LastName: str
    ContactType: ContactType
    OrganizationName: str
    AddressLine1: str
    AddressLine2: str
    City: str
    State: str
    CountryCode: CountryCode
    ZipCode: str
    PhoneNumber: str
    Email: str
    Fax: str
    ExtraParams: List["ExtraParamTypeDef"]


class DisableDomainTransferLockResponseTypeDef(TypedDict):
    OperationId: str


class DomainSuggestionTypeDef(TypedDict, total=False):
    DomainName: str
    Availability: str


class _RequiredDomainSummaryTypeDef(TypedDict):
    DomainName: str


class DomainSummaryTypeDef(_RequiredDomainSummaryTypeDef, total=False):
    AutoRenew: bool
    TransferLock: bool
    Expiry: datetime


class DomainTransferabilityTypeDef(TypedDict, total=False):
    Transferable: Transferable


class EnableDomainTransferLockResponseTypeDef(TypedDict):
    OperationId: str


class ExtraParamTypeDef(TypedDict):
    Name: ExtraParamName
    Value: str


class GetContactReachabilityStatusResponseTypeDef(TypedDict, total=False):
    domainName: str
    status: ReachabilityStatus


class _RequiredGetDomainDetailResponseTypeDef(TypedDict):
    DomainName: str
    Nameservers: List["NameserverTypeDef"]
    AdminContact: "ContactDetailTypeDef"
    RegistrantContact: "ContactDetailTypeDef"
    TechContact: "ContactDetailTypeDef"


class GetDomainDetailResponseTypeDef(_RequiredGetDomainDetailResponseTypeDef, total=False):
    AutoRenew: bool
    AdminPrivacy: bool
    RegistrantPrivacy: bool
    TechPrivacy: bool
    RegistrarName: str
    WhoIsServer: str
    RegistrarUrl: str
    AbuseContactEmail: str
    AbuseContactPhone: str
    RegistryDomainId: str
    CreationDate: datetime
    UpdatedDate: datetime
    ExpirationDate: datetime
    Reseller: str
    DnsSec: str
    StatusList: List[str]


class GetDomainSuggestionsResponseTypeDef(TypedDict, total=False):
    SuggestionsList: List["DomainSuggestionTypeDef"]


GetOperationDetailResponseTypeDef = TypedDict(
    "GetOperationDetailResponseTypeDef",
    {
        "OperationId": str,
        "Status": OperationStatus,
        "Message": str,
        "DomainName": str,
        "Type": OperationType,
        "SubmittedDate": datetime,
    },
    total=False,
)


class _RequiredListDomainsResponseTypeDef(TypedDict):
    Domains: List["DomainSummaryTypeDef"]


class ListDomainsResponseTypeDef(_RequiredListDomainsResponseTypeDef, total=False):
    NextPageMarker: str


class _RequiredListOperationsResponseTypeDef(TypedDict):
    Operations: List["OperationSummaryTypeDef"]


class ListOperationsResponseTypeDef(_RequiredListOperationsResponseTypeDef, total=False):
    NextPageMarker: str


class ListTagsForDomainResponseTypeDef(TypedDict):
    TagList: List["TagTypeDef"]


class _RequiredNameserverTypeDef(TypedDict):
    Name: str


class NameserverTypeDef(_RequiredNameserverTypeDef, total=False):
    GlueIps: List[str]


OperationSummaryTypeDef = TypedDict(
    "OperationSummaryTypeDef",
    {
        "OperationId": str,
        "Status": OperationStatus,
        "Type": OperationType,
        "SubmittedDate": datetime,
    },
)


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RegisterDomainResponseTypeDef(TypedDict):
    OperationId: str


class RejectDomainTransferFromAnotherAwsAccountResponseTypeDef(TypedDict, total=False):
    OperationId: str


class RenewDomainResponseTypeDef(TypedDict):
    OperationId: str


class ResendContactReachabilityEmailResponseTypeDef(TypedDict, total=False):
    domainName: str
    emailAddress: str
    isAlreadyVerified: bool


class RetrieveDomainAuthCodeResponseTypeDef(TypedDict):
    AuthCode: str


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class TransferDomainResponseTypeDef(TypedDict):
    OperationId: str


class TransferDomainToAnotherAwsAccountResponseTypeDef(TypedDict, total=False):
    OperationId: str
    Password: str


class UpdateDomainContactPrivacyResponseTypeDef(TypedDict):
    OperationId: str


class UpdateDomainContactResponseTypeDef(TypedDict):
    OperationId: str


class UpdateDomainNameserversResponseTypeDef(TypedDict):
    OperationId: str


class ViewBillingResponseTypeDef(TypedDict, total=False):
    NextPageMarker: str
    BillingRecords: List["BillingRecordTypeDef"]
