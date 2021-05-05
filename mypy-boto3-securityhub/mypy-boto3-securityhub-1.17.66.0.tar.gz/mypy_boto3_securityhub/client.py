"""
Type annotations for securityhub service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_securityhub import SecurityHubClient

    client: SecurityHubClient = boto3.client("securityhub")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_securityhub.literals import ControlStatus, RecordState, VerificationState
from mypy_boto3_securityhub.paginator import (
    GetEnabledStandardsPaginator,
    GetFindingsPaginator,
    GetInsightsPaginator,
    ListEnabledProductsForImportPaginator,
    ListInvitationsPaginator,
    ListMembersPaginator,
)
from mypy_boto3_securityhub.type_defs import (
    AccountDetailsTypeDef,
    AwsSecurityFindingFiltersTypeDef,
    AwsSecurityFindingIdentifierTypeDef,
    AwsSecurityFindingTypeDef,
    BatchDisableStandardsResponseTypeDef,
    BatchEnableStandardsResponseTypeDef,
    BatchImportFindingsResponseTypeDef,
    BatchUpdateFindingsResponseTypeDef,
    CreateActionTargetResponseTypeDef,
    CreateInsightResponseTypeDef,
    CreateMembersResponseTypeDef,
    DeclineInvitationsResponseTypeDef,
    DeleteActionTargetResponseTypeDef,
    DeleteInsightResponseTypeDef,
    DeleteInvitationsResponseTypeDef,
    DeleteMembersResponseTypeDef,
    DescribeActionTargetsResponseTypeDef,
    DescribeHubResponseTypeDef,
    DescribeOrganizationConfigurationResponseTypeDef,
    DescribeProductsResponseTypeDef,
    DescribeStandardsControlsResponseTypeDef,
    DescribeStandardsResponseTypeDef,
    EnableImportFindingsForProductResponseTypeDef,
    GetAdministratorAccountResponseTypeDef,
    GetEnabledStandardsResponseTypeDef,
    GetFindingsResponseTypeDef,
    GetInsightResultsResponseTypeDef,
    GetInsightsResponseTypeDef,
    GetInvitationsCountResponseTypeDef,
    GetMasterAccountResponseTypeDef,
    GetMembersResponseTypeDef,
    InviteMembersResponseTypeDef,
    ListEnabledProductsForImportResponseTypeDef,
    ListInvitationsResponseTypeDef,
    ListMembersResponseTypeDef,
    ListOrganizationAdminAccountsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    NoteUpdateTypeDef,
    RelatedFindingTypeDef,
    SeverityUpdateTypeDef,
    SortCriterionTypeDef,
    StandardsSubscriptionRequestTypeDef,
    WorkflowUpdateTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SecurityHubClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessDeniedException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalException: Type[BotocoreClientError]
    InvalidAccessException: Type[BotocoreClientError]
    InvalidInputException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceConflictException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]


class SecurityHubClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_administrator_invitation(
        self, AdministratorId: str, InvitationId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.accept_administrator_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#accept-administrator-invitation)
        """

    def accept_invitation(self, MasterId: str, InvitationId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.accept_invitation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#accept-invitation)
        """

    def batch_disable_standards(
        self, StandardsSubscriptionArns: List[str]
    ) -> BatchDisableStandardsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.batch_disable_standards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch-disable-standards)
        """

    def batch_enable_standards(
        self, StandardsSubscriptionRequests: List[StandardsSubscriptionRequestTypeDef]
    ) -> BatchEnableStandardsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.batch_enable_standards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch-enable-standards)
        """

    def batch_import_findings(
        self, Findings: List["AwsSecurityFindingTypeDef"]
    ) -> BatchImportFindingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.batch_import_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch-import-findings)
        """

    def batch_update_findings(
        self,
        FindingIdentifiers: List["AwsSecurityFindingIdentifierTypeDef"],
        Note: NoteUpdateTypeDef = None,
        Severity: SeverityUpdateTypeDef = None,
        VerificationState: VerificationState = None,
        Confidence: int = None,
        Criticality: int = None,
        Types: List[str] = None,
        UserDefinedFields: Dict[str, str] = None,
        Workflow: WorkflowUpdateTypeDef = None,
        RelatedFindings: List["RelatedFindingTypeDef"] = None,
    ) -> BatchUpdateFindingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.batch_update_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#batch-update-findings)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#can-paginate)
        """

    def create_action_target(
        self, Name: str, Description: str, Id: str
    ) -> CreateActionTargetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.create_action_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#create-action-target)
        """

    def create_insight(
        self, Name: str, Filters: "AwsSecurityFindingFiltersTypeDef", GroupByAttribute: str
    ) -> CreateInsightResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.create_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#create-insight)
        """

    def create_members(
        self, AccountDetails: List[AccountDetailsTypeDef]
    ) -> CreateMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.create_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#create-members)
        """

    def decline_invitations(self, AccountIds: List[str]) -> DeclineInvitationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.decline_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#decline-invitations)
        """

    def delete_action_target(self, ActionTargetArn: str) -> DeleteActionTargetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.delete_action_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#delete-action-target)
        """

    def delete_insight(self, InsightArn: str) -> DeleteInsightResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.delete_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#delete-insight)
        """

    def delete_invitations(self, AccountIds: List[str]) -> DeleteInvitationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.delete_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#delete-invitations)
        """

    def delete_members(self, AccountIds: List[str]) -> DeleteMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.delete_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#delete-members)
        """

    def describe_action_targets(
        self, ActionTargetArns: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> DescribeActionTargetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.describe_action_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe-action-targets)
        """

    def describe_hub(self, HubArn: str = None) -> DescribeHubResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.describe_hub)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe-hub)
        """

    def describe_organization_configuration(
        self,
    ) -> DescribeOrganizationConfigurationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.describe_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe-organization-configuration)
        """

    def describe_products(
        self, NextToken: str = None, MaxResults: int = None, ProductArn: str = None
    ) -> DescribeProductsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.describe_products)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe-products)
        """

    def describe_standards(
        self, NextToken: str = None, MaxResults: int = None
    ) -> DescribeStandardsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.describe_standards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe-standards)
        """

    def describe_standards_controls(
        self, StandardsSubscriptionArn: str, NextToken: str = None, MaxResults: int = None
    ) -> DescribeStandardsControlsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.describe_standards_controls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#describe-standards-controls)
        """

    def disable_import_findings_for_product(self, ProductSubscriptionArn: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.disable_import_findings_for_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disable-import-findings-for-product)
        """

    def disable_organization_admin_account(self, AdminAccountId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.disable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disable-organization-admin-account)
        """

    def disable_security_hub(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.disable_security_hub)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disable-security-hub)
        """

    def disassociate_from_administrator_account(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.disassociate_from_administrator_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disassociate-from-administrator-account)
        """

    def disassociate_from_master_account(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.disassociate_from_master_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disassociate-from-master-account)
        """

    def disassociate_members(self, AccountIds: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.disassociate_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#disassociate-members)
        """

    def enable_import_findings_for_product(
        self, ProductArn: str
    ) -> EnableImportFindingsForProductResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.enable_import_findings_for_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#enable-import-findings-for-product)
        """

    def enable_organization_admin_account(self, AdminAccountId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.enable_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#enable-organization-admin-account)
        """

    def enable_security_hub(
        self, Tags: Dict[str, str] = None, EnableDefaultStandards: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.enable_security_hub)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#enable-security-hub)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#generate-presigned-url)
        """

    def get_administrator_account(self) -> GetAdministratorAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.get_administrator_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get-administrator-account)
        """

    def get_enabled_standards(
        self,
        StandardsSubscriptionArns: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetEnabledStandardsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.get_enabled_standards)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get-enabled-standards)
        """

    def get_findings(
        self,
        Filters: "AwsSecurityFindingFiltersTypeDef" = None,
        SortCriteria: List[SortCriterionTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> GetFindingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.get_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get-findings)
        """

    def get_insight_results(self, InsightArn: str) -> GetInsightResultsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.get_insight_results)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get-insight-results)
        """

    def get_insights(
        self, InsightArns: List[str] = None, NextToken: str = None, MaxResults: int = None
    ) -> GetInsightsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.get_insights)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get-insights)
        """

    def get_invitations_count(self) -> GetInvitationsCountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.get_invitations_count)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get-invitations-count)
        """

    def get_master_account(self) -> GetMasterAccountResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.get_master_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get-master-account)
        """

    def get_members(self, AccountIds: List[str]) -> GetMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.get_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#get-members)
        """

    def invite_members(self, AccountIds: List[str]) -> InviteMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.invite_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#invite-members)
        """

    def list_enabled_products_for_import(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ListEnabledProductsForImportResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.list_enabled_products_for_import)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list-enabled-products-for-import)
        """

    def list_invitations(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListInvitationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.list_invitations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list-invitations)
        """

    def list_members(
        self, OnlyAssociated: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> ListMembersResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.list_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list-members)
        """

    def list_organization_admin_accounts(
        self, MaxResults: int = None, NextToken: str = None
    ) -> ListOrganizationAdminAccountsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.list_organization_admin_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list-organization-admin-accounts)
        """

    def list_tags_for_resource(self, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#list-tags-for-resource)
        """

    def tag_resource(self, ResourceArn: str, Tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#tag-resource)
        """

    def untag_resource(self, ResourceArn: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#untag-resource)
        """

    def update_action_target(
        self, ActionTargetArn: str, Name: str = None, Description: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.update_action_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update-action-target)
        """

    def update_findings(
        self,
        Filters: "AwsSecurityFindingFiltersTypeDef",
        Note: NoteUpdateTypeDef = None,
        RecordState: RecordState = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.update_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update-findings)
        """

    def update_insight(
        self,
        InsightArn: str,
        Name: str = None,
        Filters: "AwsSecurityFindingFiltersTypeDef" = None,
        GroupByAttribute: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.update_insight)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update-insight)
        """

    def update_organization_configuration(self, AutoEnable: bool) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.update_organization_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update-organization-configuration)
        """

    def update_security_hub_configuration(self, AutoEnableControls: bool = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.update_security_hub_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update-security-hub-configuration)
        """

    def update_standards_control(
        self,
        StandardsControlArn: str,
        ControlStatus: ControlStatus = None,
        DisabledReason: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Client.update_standards_control)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/client.html#update-standards-control)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_enabled_standards"]
    ) -> GetEnabledStandardsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Paginator.GetEnabledStandards)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#getenabledstandardspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_findings"]) -> GetFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Paginator.GetFindings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#getfindingspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_insights"]) -> GetInsightsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Paginator.GetInsights)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#getinsightspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_enabled_products_for_import"]
    ) -> ListEnabledProductsForImportPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Paginator.ListEnabledProductsForImport)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#listenabledproductsforimportpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_invitations"]
    ) -> ListInvitationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Paginator.ListInvitations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#listinvitationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_members"]) -> ListMembersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/securityhub.html#SecurityHub.Paginator.ListMembers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/paginators.html#listmemberspaginator)
        """
