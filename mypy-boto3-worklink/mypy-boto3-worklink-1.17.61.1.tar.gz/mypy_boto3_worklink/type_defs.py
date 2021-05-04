"""
Type annotations for worklink service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_worklink/type_defs.html)

Usage::

    ```python
    from mypy_boto3_worklink.type_defs import AssociateWebsiteAuthorizationProviderResponseTypeDef

    data: AssociateWebsiteAuthorizationProviderResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_worklink.literals import DeviceStatus, DomainStatus, FleetStatus

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateWebsiteAuthorizationProviderResponseTypeDef",
    "AssociateWebsiteCertificateAuthorityResponseTypeDef",
    "CreateFleetResponseTypeDef",
    "DescribeAuditStreamConfigurationResponseTypeDef",
    "DescribeCompanyNetworkConfigurationResponseTypeDef",
    "DescribeDevicePolicyConfigurationResponseTypeDef",
    "DescribeDeviceResponseTypeDef",
    "DescribeDomainResponseTypeDef",
    "DescribeFleetMetadataResponseTypeDef",
    "DescribeIdentityProviderConfigurationResponseTypeDef",
    "DescribeWebsiteCertificateAuthorityResponseTypeDef",
    "DeviceSummaryTypeDef",
    "DomainSummaryTypeDef",
    "FleetSummaryTypeDef",
    "ListDevicesResponseTypeDef",
    "ListDomainsResponseTypeDef",
    "ListFleetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebsiteAuthorizationProvidersResponseTypeDef",
    "ListWebsiteCertificateAuthoritiesResponseTypeDef",
    "WebsiteAuthorizationProviderSummaryTypeDef",
    "WebsiteCaSummaryTypeDef",
)


class AssociateWebsiteAuthorizationProviderResponseTypeDef(TypedDict, total=False):
    AuthorizationProviderId: str


class AssociateWebsiteCertificateAuthorityResponseTypeDef(TypedDict, total=False):
    WebsiteCaId: str


class CreateFleetResponseTypeDef(TypedDict, total=False):
    FleetArn: str


class DescribeAuditStreamConfigurationResponseTypeDef(TypedDict, total=False):
    AuditStreamArn: str


class DescribeCompanyNetworkConfigurationResponseTypeDef(TypedDict, total=False):
    VpcId: str
    SubnetIds: List[str]
    SecurityGroupIds: List[str]


class DescribeDevicePolicyConfigurationResponseTypeDef(TypedDict, total=False):
    DeviceCaCertificate: str


class DescribeDeviceResponseTypeDef(TypedDict, total=False):
    Status: DeviceStatus
    Model: str
    Manufacturer: str
    OperatingSystem: str
    OperatingSystemVersion: str
    PatchLevel: str
    FirstAccessedTime: datetime
    LastAccessedTime: datetime
    Username: str


class DescribeDomainResponseTypeDef(TypedDict, total=False):
    DomainName: str
    DisplayName: str
    CreatedTime: datetime
    DomainStatus: DomainStatus
    AcmCertificateArn: str


class DescribeFleetMetadataResponseTypeDef(TypedDict, total=False):
    CreatedTime: datetime
    LastUpdatedTime: datetime
    FleetName: str
    DisplayName: str
    OptimizeForEndUserLocation: bool
    CompanyCode: str
    FleetStatus: FleetStatus
    Tags: Dict[str, str]


class DescribeIdentityProviderConfigurationResponseTypeDef(TypedDict, total=False):
    IdentityProviderType: Literal["SAML"]
    ServiceProviderSamlMetadata: str
    IdentityProviderSamlMetadata: str


class DescribeWebsiteCertificateAuthorityResponseTypeDef(TypedDict, total=False):
    Certificate: str
    CreatedTime: datetime
    DisplayName: str


class DeviceSummaryTypeDef(TypedDict, total=False):
    DeviceId: str
    DeviceStatus: DeviceStatus


class _RequiredDomainSummaryTypeDef(TypedDict):
    DomainName: str
    CreatedTime: datetime
    DomainStatus: DomainStatus


class DomainSummaryTypeDef(_RequiredDomainSummaryTypeDef, total=False):
    DisplayName: str


class FleetSummaryTypeDef(TypedDict, total=False):
    FleetArn: str
    CreatedTime: datetime
    LastUpdatedTime: datetime
    FleetName: str
    DisplayName: str
    CompanyCode: str
    FleetStatus: FleetStatus
    Tags: Dict[str, str]


class ListDevicesResponseTypeDef(TypedDict, total=False):
    Devices: List["DeviceSummaryTypeDef"]
    NextToken: str


class ListDomainsResponseTypeDef(TypedDict, total=False):
    Domains: List["DomainSummaryTypeDef"]
    NextToken: str


class ListFleetsResponseTypeDef(TypedDict, total=False):
    FleetSummaryList: List["FleetSummaryTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class ListWebsiteAuthorizationProvidersResponseTypeDef(TypedDict, total=False):
    WebsiteAuthorizationProviders: List["WebsiteAuthorizationProviderSummaryTypeDef"]
    NextToken: str


class ListWebsiteCertificateAuthoritiesResponseTypeDef(TypedDict, total=False):
    WebsiteCertificateAuthorities: List["WebsiteCaSummaryTypeDef"]
    NextToken: str


class _RequiredWebsiteAuthorizationProviderSummaryTypeDef(TypedDict):
    AuthorizationProviderType: Literal["SAML"]


class WebsiteAuthorizationProviderSummaryTypeDef(
    _RequiredWebsiteAuthorizationProviderSummaryTypeDef, total=False
):
    AuthorizationProviderId: str
    DomainName: str
    CreatedTime: datetime


class WebsiteCaSummaryTypeDef(TypedDict, total=False):
    WebsiteCaId: str
    CreatedTime: datetime
    DisplayName: str
