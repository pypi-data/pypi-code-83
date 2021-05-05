"""
Type annotations for organizations service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_organizations/literals.html)

Usage::

    ```python
    from mypy_boto3_organizations.literals import AccountJoinedMethod

    data: AccountJoinedMethod = "CREATED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccountJoinedMethod",
    "AccountStatus",
    "ActionType",
    "ChildType",
    "CreateAccountFailureReason",
    "CreateAccountState",
    "EffectivePolicyType",
    "HandshakePartyType",
    "HandshakeResourceType",
    "HandshakeState",
    "IAMUserAccessToBilling",
    "ListAWSServiceAccessForOrganizationPaginatorName",
    "ListAccountsForParentPaginatorName",
    "ListAccountsPaginatorName",
    "ListChildrenPaginatorName",
    "ListCreateAccountStatusPaginatorName",
    "ListDelegatedAdministratorsPaginatorName",
    "ListDelegatedServicesForAccountPaginatorName",
    "ListHandshakesForAccountPaginatorName",
    "ListHandshakesForOrganizationPaginatorName",
    "ListOrganizationalUnitsForParentPaginatorName",
    "ListParentsPaginatorName",
    "ListPoliciesForTargetPaginatorName",
    "ListPoliciesPaginatorName",
    "ListRootsPaginatorName",
    "ListTagsForResourcePaginatorName",
    "ListTargetsForPolicyPaginatorName",
    "OrganizationFeatureSet",
    "ParentType",
    "PolicyType",
    "PolicyTypeStatus",
    "TargetType",
)


AccountJoinedMethod = Literal["CREATED", "INVITED"]
AccountStatus = Literal["ACTIVE", "SUSPENDED"]
ActionType = Literal[
    "ADD_ORGANIZATIONS_SERVICE_LINKED_ROLE", "APPROVE_ALL_FEATURES", "ENABLE_ALL_FEATURES", "INVITE"
]
ChildType = Literal["ACCOUNT", "ORGANIZATIONAL_UNIT"]
CreateAccountFailureReason = Literal[
    "ACCOUNT_LIMIT_EXCEEDED",
    "CONCURRENT_ACCOUNT_MODIFICATION",
    "EMAIL_ALREADY_EXISTS",
    "FAILED_BUSINESS_VALIDATION",
    "GOVCLOUD_ACCOUNT_ALREADY_EXISTS",
    "INTERNAL_FAILURE",
    "INVALID_ADDRESS",
    "INVALID_EMAIL",
    "INVALID_IDENTITY_FOR_BUSINESS_VALIDATION",
    "MISSING_BUSINESS_VALIDATION",
    "MISSING_PAYMENT_INSTRUMENT",
    "PENDING_BUSINESS_VALIDATION",
    "UNKNOWN_BUSINESS_VALIDATION",
]
CreateAccountState = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
EffectivePolicyType = Literal["AISERVICES_OPT_OUT_POLICY", "BACKUP_POLICY", "TAG_POLICY"]
HandshakePartyType = Literal["ACCOUNT", "EMAIL", "ORGANIZATION"]
HandshakeResourceType = Literal[
    "ACCOUNT",
    "EMAIL",
    "MASTER_EMAIL",
    "MASTER_NAME",
    "NOTES",
    "ORGANIZATION",
    "ORGANIZATION_FEATURE_SET",
    "PARENT_HANDSHAKE",
]
HandshakeState = Literal["ACCEPTED", "CANCELED", "DECLINED", "EXPIRED", "OPEN", "REQUESTED"]
IAMUserAccessToBilling = Literal["ALLOW", "DENY"]
ListAWSServiceAccessForOrganizationPaginatorName = Literal[
    "list_aws_service_access_for_organization"
]
ListAccountsForParentPaginatorName = Literal["list_accounts_for_parent"]
ListAccountsPaginatorName = Literal["list_accounts"]
ListChildrenPaginatorName = Literal["list_children"]
ListCreateAccountStatusPaginatorName = Literal["list_create_account_status"]
ListDelegatedAdministratorsPaginatorName = Literal["list_delegated_administrators"]
ListDelegatedServicesForAccountPaginatorName = Literal["list_delegated_services_for_account"]
ListHandshakesForAccountPaginatorName = Literal["list_handshakes_for_account"]
ListHandshakesForOrganizationPaginatorName = Literal["list_handshakes_for_organization"]
ListOrganizationalUnitsForParentPaginatorName = Literal["list_organizational_units_for_parent"]
ListParentsPaginatorName = Literal["list_parents"]
ListPoliciesForTargetPaginatorName = Literal["list_policies_for_target"]
ListPoliciesPaginatorName = Literal["list_policies"]
ListRootsPaginatorName = Literal["list_roots"]
ListTagsForResourcePaginatorName = Literal["list_tags_for_resource"]
ListTargetsForPolicyPaginatorName = Literal["list_targets_for_policy"]
OrganizationFeatureSet = Literal["ALL", "CONSOLIDATED_BILLING"]
ParentType = Literal["ORGANIZATIONAL_UNIT", "ROOT"]
PolicyType = Literal[
    "AISERVICES_OPT_OUT_POLICY", "BACKUP_POLICY", "SERVICE_CONTROL_POLICY", "TAG_POLICY"
]
PolicyTypeStatus = Literal["ENABLED", "PENDING_DISABLE", "PENDING_ENABLE"]
TargetType = Literal["ACCOUNT", "ORGANIZATIONAL_UNIT", "ROOT"]
