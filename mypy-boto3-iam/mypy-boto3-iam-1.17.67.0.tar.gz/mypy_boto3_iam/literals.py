"""
Type annotations for iam service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/literals.html)

Usage::

    ```python
    from mypy_boto3_iam.literals import AccessAdvisorUsageGranularityType

    data: AccessAdvisorUsageGranularityType = "ACTION_LEVEL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccessAdvisorUsageGranularityType",
    "ContextKeyTypeEnum",
    "DeletionTaskStatusType",
    "EntityType",
    "GetAccountAuthorizationDetailsPaginatorName",
    "GetGroupPaginatorName",
    "InstanceProfileExistsWaiterName",
    "ListAccessKeysPaginatorName",
    "ListAccountAliasesPaginatorName",
    "ListAttachedGroupPoliciesPaginatorName",
    "ListAttachedRolePoliciesPaginatorName",
    "ListAttachedUserPoliciesPaginatorName",
    "ListEntitiesForPolicyPaginatorName",
    "ListGroupPoliciesPaginatorName",
    "ListGroupsForUserPaginatorName",
    "ListGroupsPaginatorName",
    "ListInstanceProfilesForRolePaginatorName",
    "ListInstanceProfilesPaginatorName",
    "ListMFADevicesPaginatorName",
    "ListPoliciesPaginatorName",
    "ListPolicyVersionsPaginatorName",
    "ListRolePoliciesPaginatorName",
    "ListRolesPaginatorName",
    "ListSSHPublicKeysPaginatorName",
    "ListServerCertificatesPaginatorName",
    "ListSigningCertificatesPaginatorName",
    "ListUserPoliciesPaginatorName",
    "ListUsersPaginatorName",
    "ListVirtualMFADevicesPaginatorName",
    "PermissionsBoundaryAttachmentType",
    "PolicyEvaluationDecisionType",
    "PolicyExistsWaiterName",
    "PolicySourceType",
    "PolicyUsageType",
    "ReportFormatType",
    "ReportStateType",
    "RoleExistsWaiterName",
    "SimulateCustomPolicyPaginatorName",
    "SimulatePrincipalPolicyPaginatorName",
    "UserExistsWaiterName",
    "assignmentStatusType",
    "encodingType",
    "globalEndpointTokenVersion",
    "jobStatusType",
    "policyOwnerEntityType",
    "policyScopeType",
    "policyType",
    "sortKeyType",
    "statusType",
    "summaryKeyType",
)


AccessAdvisorUsageGranularityType = Literal["ACTION_LEVEL", "SERVICE_LEVEL"]
ContextKeyTypeEnum = Literal[
    "binary",
    "binaryList",
    "boolean",
    "booleanList",
    "date",
    "dateList",
    "ip",
    "ipList",
    "numeric",
    "numericList",
    "string",
    "stringList",
]
DeletionTaskStatusType = Literal["FAILED", "IN_PROGRESS", "NOT_STARTED", "SUCCEEDED"]
EntityType = Literal["AWSManagedPolicy", "Group", "LocalManagedPolicy", "Role", "User"]
GetAccountAuthorizationDetailsPaginatorName = Literal["get_account_authorization_details"]
GetGroupPaginatorName = Literal["get_group"]
InstanceProfileExistsWaiterName = Literal["instance_profile_exists"]
ListAccessKeysPaginatorName = Literal["list_access_keys"]
ListAccountAliasesPaginatorName = Literal["list_account_aliases"]
ListAttachedGroupPoliciesPaginatorName = Literal["list_attached_group_policies"]
ListAttachedRolePoliciesPaginatorName = Literal["list_attached_role_policies"]
ListAttachedUserPoliciesPaginatorName = Literal["list_attached_user_policies"]
ListEntitiesForPolicyPaginatorName = Literal["list_entities_for_policy"]
ListGroupPoliciesPaginatorName = Literal["list_group_policies"]
ListGroupsForUserPaginatorName = Literal["list_groups_for_user"]
ListGroupsPaginatorName = Literal["list_groups"]
ListInstanceProfilesForRolePaginatorName = Literal["list_instance_profiles_for_role"]
ListInstanceProfilesPaginatorName = Literal["list_instance_profiles"]
ListMFADevicesPaginatorName = Literal["list_mfa_devices"]
ListPoliciesPaginatorName = Literal["list_policies"]
ListPolicyVersionsPaginatorName = Literal["list_policy_versions"]
ListRolePoliciesPaginatorName = Literal["list_role_policies"]
ListRolesPaginatorName = Literal["list_roles"]
ListSSHPublicKeysPaginatorName = Literal["list_ssh_public_keys"]
ListServerCertificatesPaginatorName = Literal["list_server_certificates"]
ListSigningCertificatesPaginatorName = Literal["list_signing_certificates"]
ListUserPoliciesPaginatorName = Literal["list_user_policies"]
ListUsersPaginatorName = Literal["list_users"]
ListVirtualMFADevicesPaginatorName = Literal["list_virtual_mfa_devices"]
PermissionsBoundaryAttachmentType = Literal["PermissionsBoundaryPolicy"]
PolicyEvaluationDecisionType = Literal["allowed", "explicitDeny", "implicitDeny"]
PolicyExistsWaiterName = Literal["policy_exists"]
PolicySourceType = Literal[
    "aws-managed", "group", "none", "resource", "role", "user", "user-managed"
]
PolicyUsageType = Literal["PermissionsBoundary", "PermissionsPolicy"]
ReportFormatType = Literal["text/csv"]
ReportStateType = Literal["COMPLETE", "INPROGRESS", "STARTED"]
RoleExistsWaiterName = Literal["role_exists"]
SimulateCustomPolicyPaginatorName = Literal["simulate_custom_policy"]
SimulatePrincipalPolicyPaginatorName = Literal["simulate_principal_policy"]
UserExistsWaiterName = Literal["user_exists"]
assignmentStatusType = Literal["Any", "Assigned", "Unassigned"]
encodingType = Literal["PEM", "SSH"]
globalEndpointTokenVersion = Literal["v1Token", "v2Token"]
jobStatusType = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
policyOwnerEntityType = Literal["GROUP", "ROLE", "USER"]
policyScopeType = Literal["AWS", "All", "Local"]
policyType = Literal["INLINE", "MANAGED"]
sortKeyType = Literal[
    "LAST_AUTHENTICATED_TIME_ASCENDING",
    "LAST_AUTHENTICATED_TIME_DESCENDING",
    "SERVICE_NAMESPACE_ASCENDING",
    "SERVICE_NAMESPACE_DESCENDING",
]
statusType = Literal["Active", "Inactive"]
summaryKeyType = Literal[
    "AccessKeysPerUserQuota",
    "AccountAccessKeysPresent",
    "AccountMFAEnabled",
    "AccountSigningCertificatesPresent",
    "AttachedPoliciesPerGroupQuota",
    "AttachedPoliciesPerRoleQuota",
    "AttachedPoliciesPerUserQuota",
    "GlobalEndpointTokenVersion",
    "GroupPolicySizeQuota",
    "Groups",
    "GroupsPerUserQuota",
    "GroupsQuota",
    "MFADevices",
    "MFADevicesInUse",
    "Policies",
    "PoliciesQuota",
    "PolicySizeQuota",
    "PolicyVersionsInUse",
    "PolicyVersionsInUseQuota",
    "ServerCertificates",
    "ServerCertificatesQuota",
    "SigningCertificatesPerUserQuota",
    "UserPolicySizeQuota",
    "Users",
    "UsersQuota",
    "VersionsPerPolicyQuota",
]
