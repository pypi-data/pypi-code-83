"""
Type annotations for guardduty service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_guardduty import GuardDutyClient

    client: GuardDutyClient = boto3.client("guardduty")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_guardduty.literals import (
    Feedback,
    FilterAction,
    FindingPublishingFrequency,
    IpSetFormat,
    ThreatIntelSetFormat,
    UsageStatisticType,
)
from mypy_boto3_guardduty.paginator import (
    ListDetectorsPaginator,
    ListFiltersPaginator,
    ListFindingsPaginator,
    ListInvitationsPaginator,
    ListIPSetsPaginator,
    ListMembersPaginator,
    ListOrganizationAdminAccountsPaginator,
    ListThreatIntelSetsPaginator,
)
from mypy_boto3_guardduty.type_defs import (
    AccountDetailTypeDef,
    CreateDetectorResponseTypeDef,
    CreateFilterResponseTypeDef,
    CreateIPSetResponseTypeDef,
    CreateMembersResponseTypeDef,
    CreatePublishingDestinationResponseTypeDef,
    CreateThreatIntelSetResponseTypeDef,
    DataSourceConfigurationsTypeDef,
    DeclineInvitationsResponseTypeDef,
    DeleteInvitationsResponseTypeDef,
    DeleteMembersResponseTypeDef,
    DescribeOrganizationConfigurationResponseTypeDef,
    DescribePublishingDestinationResponseTypeDef,
    DestinationPropertiesTypeDef,
    DisassociateMembersResponseTypeDef,
    FindingCriteriaTypeDef,
    GetDetectorResponseTypeDef,
    GetFilterResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetFindingsStatisticsResponseTypeDef,
    GetInvitationsCountResponseTypeDef,
    GetIPSetResponseTypeDef,
    GetMasterAccountResponseTypeDef,
    GetMemberDetectorsResponseTypeDef,
    GetMembersResponseTypeDef,
    GetThreatIntelSetResponseTypeDef,
    GetUsageStatisticsResponseTypeDef,
    InviteMembersResponseTypeDef,
    ListDetectorsResponseTypeDef,
    ListFiltersResponseTypeDef,
    ListFindingsResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListIPSetsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListOrganizationAdminAccountsResponseTypeDef,
    ListPublishingDestinationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListThreatIntelSetsResponseTypeDef,
    OrganizationDataSourceConfigurationsTypeDef,
    SortCriteriaTypeDef,
    StartMonitoringMembersResponseTypeDef,
    StopMonitoringMembersResponseTypeDef,
    UpdateFilterResponseTypeDef,
    UpdateMemberDetectorsResponseTypeDef,
    UsageCriteriaTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("GuardDutyClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]


class GuardDutyClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_invitation(
        self, DetectorId: str, MasterId: str, InvitationId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.accept_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#accept-invitation)
        """

    def archive_findings(self, DetectorId: str, FindingIds: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.archive_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#archive-findings)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#can-paginate)
        """

    def create_detector(
        self,
        Enable: bool,
        ClientToken: str = None,
        FindingPublishingFrequency: FindingPublishingFrequency = None,
        DataSources: DataSourceConfigurationsTypeDef = None,
        Tags: Dict[str, str] = None,
    ) -> CreateDetectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.create_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#create-detector)
        """

    def create_filter(
        self,
        DetectorId: str,
        Name: str,
        FindingCriteria: "FindingCriteriaTypeDef",
        Description: str = None,
        Action: FilterAction = None,
        Rank: int = None,
        ClientToken: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateFilterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.create_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#create-filter)
        """

    def create_ip_set(
        self,
        DetectorId: str,
        Name: str,
        Format: IpSetFormat,
        Location: str,
        Activate: bool,
        ClientToken: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateIPSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.create_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#create-ip-set)
        """

    def create_members(
        self, DetectorId: str, AccountDetails: List[AccountDetailTypeDef]
    ) -> CreateMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.create_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#create-members)
        """

    def create_publishing_destination(
        self,
        DetectorId: str,
        DestinationType: Literal["S3"],
        DestinationProperties: "DestinationPropertiesTypeDef",
        ClientToken: str = None,
    ) -> CreatePublishingDestinationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.create_publishing_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#create-publishing-destination)
        """

    def create_sample_findings(
        self, DetectorId: str, FindingTypes: List[str] = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.create_sample_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#create-sample-findings)
        """

    def create_threat_intel_set(
        self,
        DetectorId: str,
        Name: str,
        Format: ThreatIntelSetFormat,
        Location: str,
        Activate: bool,
        ClientToken: str = None,
        Tags: Dict[str, str] = None,
    ) -> CreateThreatIntelSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.create_threat_intel_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#create-threat-intel-set)
        """

    def decline_invitations(self, AccountIds: List[str]) -> DeclineInvitationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.decline_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#decline-invitations)
        """

    def delete_detector(self, DetectorId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.delete_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#delete-detector)
        """

    def delete_filter(self, DetectorId: str, FilterName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.delete_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#delete-filter)
        """

    def delete_invitations(self, AccountIds: List[str]) -> DeleteInvitationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.delete_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#delete-invitations)
        """

    def delete_ip_set(self, DetectorId: str, IpSetId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.delete_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#delete-ip-set)
        """

    def delete_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> DeleteMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.delete_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#delete-members)
        """

    def delete_publishing_destination(self, DetectorId: str, DestinationId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.delete_publishing_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#delete-publishing-destination)
        """

    def delete_threat_intel_set(self, DetectorId: str, ThreatIntelSetId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.delete_threat_intel_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#delete-threat-intel-set)
        """

    def describe_organization_configuration(
        self, DetectorId: str
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.describe_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#describe-organization-configuration)
        """

    def describe_publishing_destination(
        self, DetectorId: str, DestinationId: str
    ) -> DescribePublishingDestinationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.describe_publishing_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#describe-publishing-destination)
        """

    def disable_organization_admin_account(self, AdminAccountId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.disable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#disable-organization-admin-account)
        """

    def disassociate_from_master_account(self, DetectorId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.disassociate_from_master_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#disassociate-from-master-account)
        """

    def disassociate_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> DisassociateMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.disassociate_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#disassociate-members)
        """

    def enable_organization_admin_account(self, AdminAccountId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.enable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#enable-organization-admin-account)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#generate-presigned-url)
        """

    def get_detector(self, DetectorId: str) -> GetDetectorResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.get_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get-detector)
        """

    def get_filter(self, DetectorId: str, FilterName: str) -> GetFilterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.get_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get-filter)
        """

    def get_findings(
        self, DetectorId: str, FindingIds: List[str], SortCriteria: SortCriteriaTypeDef = None
    ) -> GetFindingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.get_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get-findings)
        """

    def get_findings_statistics(
        self,
        DetectorId: str,
        FindingStatisticTypes: List[Literal["COUNT_BY_SEVERITY"]],
        FindingCriteria: "FindingCriteriaTypeDef" = None,
    ) -> GetFindingsStatisticsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.get_findings_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get-findings-statistics)
        """

    def get_invitations_count(self) -> GetInvitationsCountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.get_invitations_count)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get-invitations-count)
        """

    def get_ip_set(self, DetectorId: str, IpSetId: str) -> GetIPSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.get_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get-ip-set)
        """

    def get_master_account(self, DetectorId: str) -> GetMasterAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.get_master_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get-master-account)
        """

    def get_member_detectors(
        self, DetectorId: str, AccountIds: List[str]
    ) -> GetMemberDetectorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.get_member_detectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get-member-detectors)
        """

    def get_members(self, DetectorId: str, AccountIds: List[str]) -> GetMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.get_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get-members)
        """

    def get_threat_intel_set(
        self, DetectorId: str, ThreatIntelSetId: str
    ) -> GetThreatIntelSetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.get_threat_intel_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get-threat-intel-set)
        """

    def get_usage_statistics(
        self,
        DetectorId: str,
        UsageStatisticType: UsageStatisticType,
        UsageCriteria: UsageCriteriaTypeDef,
        Unit: str = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetUsageStatisticsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.get_usage_statistics)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#get-usage-statistics)
        """

    def invite_members(
        self,
        DetectorId: str,
        AccountIds: List[str],
        DisableEmailNotification: bool = None,
        Message: str = None,
    ) -> InviteMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.invite_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#invite-members)
        """

    def list_detectors(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListDetectorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.list_detectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list-detectors)
        """

    def list_filters(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListFiltersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.list_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list-filters)
        """

    def list_findings(
        self,
        DetectorId: str,
        FindingCriteria: "FindingCriteriaTypeDef" = None,
        SortCriteria: SortCriteriaTypeDef = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> ListFindingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.list_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list-findings)
        """

    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListInvitationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.list_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list-invitations)
        """

    def list_ip_sets(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListIPSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.list_ip_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list-ip-sets)
        """

    def list_members(
        self,
        DetectorId: str,
        MaxResults: int = None,
        NextToken: str = None,
        OnlyAssociated: str = None,
    ) -> ListMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.list_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list-members)
        """

    def list_organization_admin_accounts(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListOrganizationAdminAccountsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.list_organization_admin_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list-organization-admin-accounts)
        """

    def list_publishing_destinations(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListPublishingDestinationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.list_publishing_destinations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list-publishing-destinations)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list-tags-for-resource)
        """

    def list_threat_intel_sets(
        self, DetectorId: str, MaxResults: int = None, NextToken: str = None
    ) -> ListThreatIntelSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.list_threat_intel_sets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#list-threat-intel-sets)
        """

    def start_monitoring_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> StartMonitoringMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.start_monitoring_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#start-monitoring-members)
        """

    def stop_monitoring_members(
        self, DetectorId: str, AccountIds: List[str]
    ) -> StopMonitoringMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.stop_monitoring_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#stop-monitoring-members)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#tag-resource)
        """

    def unarchive_findings(self, DetectorId: str, FindingIds: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.unarchive_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#unarchive-findings)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#untag-resource)
        """

    def update_detector(
        self,
        DetectorId: str,
        Enable: bool = None,
        FindingPublishingFrequency: FindingPublishingFrequency = None,
        DataSources: DataSourceConfigurationsTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.update_detector)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update-detector)
        """

    def update_filter(
        self,
        DetectorId: str,
        FilterName: str,
        Description: str = None,
        Action: FilterAction = None,
        Rank: int = None,
        FindingCriteria: "FindingCriteriaTypeDef" = None,
    ) -> UpdateFilterResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.update_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update-filter)
        """

    def update_findings_feedback(
        self, DetectorId: str, FindingIds: List[str], Feedback: Feedback, Comments: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.update_findings_feedback)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update-findings-feedback)
        """

    def update_ip_set(
        self,
        DetectorId: str,
        IpSetId: str,
        Name: str = None,
        Location: str = None,
        Activate: bool = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.update_ip_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update-ip-set)
        """

    def update_member_detectors(
        self,
        DetectorId: str,
        AccountIds: List[str],
        DataSources: DataSourceConfigurationsTypeDef = None,
    ) -> UpdateMemberDetectorsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.update_member_detectors)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update-member-detectors)
        """

    def update_organization_configuration(
        self,
        DetectorId: str,
        AutoEnable: bool,
        DataSources: OrganizationDataSourceConfigurationsTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.update_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update-organization-configuration)
        """

    def update_publishing_destination(
        self,
        DetectorId: str,
        DestinationId: str,
        DestinationProperties: "DestinationPropertiesTypeDef" = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.update_publishing_destination)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update-publishing-destination)
        """

    def update_threat_intel_set(
        self,
        DetectorId: str,
        ThreatIntelSetId: str,
        Name: str = None,
        Location: str = None,
        Activate: bool = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Client.update_threat_intel_set)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/client.html#update-threat-intel-set)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_detectors"]) -> ListDetectorsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Paginator.ListDetectors)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listdetectorspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_filters"]) -> ListFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Paginator.ListFilters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listfilterspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_findings"]) -> ListFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Paginator.ListFindings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listfindingspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_ip_sets"]) -> ListIPSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Paginator.ListIPSets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listipsetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_invitations"]
    ) -> ListInvitationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Paginator.ListInvitations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listinvitationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_members"]) -> ListMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Paginator.ListMembers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listmemberspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_admin_accounts"]
    ) -> ListOrganizationAdminAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Paginator.ListOrganizationAdminAccounts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listorganizationadminaccountspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_threat_intel_sets"]
    ) -> ListThreatIntelSetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/guardduty.html#GuardDuty.Paginator.ListThreatIntelSets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_guardduty/paginators.html#listthreatintelsetspaginator)
        """
