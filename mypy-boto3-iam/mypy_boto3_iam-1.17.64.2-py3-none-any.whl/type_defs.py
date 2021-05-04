"""
Type annotations for iam service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iam.type_defs import AccessDetailTypeDef

    data: AccessDetailTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_iam.literals import (
    AccessAdvisorUsageGranularityType,
    ContextKeyTypeEnum,
    DeletionTaskStatusType,
    PolicyEvaluationDecisionType,
    PolicySourceType,
    ReportStateType,
    jobStatusType,
    policyOwnerEntityType,
    policyType,
    statusType,
    summaryKeyType,
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
    "AccessDetailTypeDef",
    "AccessKeyLastUsedTypeDef",
    "AccessKeyMetadataTypeDef",
    "AccessKeyTypeDef",
    "AttachedPermissionsBoundaryTypeDef",
    "AttachedPolicyTypeDef",
    "ContextEntryTypeDef",
    "CreateAccessKeyResponseTypeDef",
    "CreateGroupResponseTypeDef",
    "CreateInstanceProfileResponseTypeDef",
    "CreateLoginProfileResponseTypeDef",
    "CreateOpenIDConnectProviderResponseTypeDef",
    "CreatePolicyResponseTypeDef",
    "CreatePolicyVersionResponseTypeDef",
    "CreateRoleResponseTypeDef",
    "CreateSAMLProviderResponseTypeDef",
    "CreateServiceLinkedRoleResponseTypeDef",
    "CreateServiceSpecificCredentialResponseTypeDef",
    "CreateUserResponseTypeDef",
    "CreateVirtualMFADeviceResponseTypeDef",
    "DeleteServiceLinkedRoleResponseTypeDef",
    "DeletionTaskFailureReasonTypeTypeDef",
    "EntityDetailsTypeDef",
    "EntityInfoTypeDef",
    "ErrorDetailsTypeDef",
    "EvaluationResultTypeDef",
    "GenerateCredentialReportResponseTypeDef",
    "GenerateOrganizationsAccessReportResponseTypeDef",
    "GenerateServiceLastAccessedDetailsResponseTypeDef",
    "GetAccessKeyLastUsedResponseTypeDef",
    "GetAccountAuthorizationDetailsResponseTypeDef",
    "GetAccountPasswordPolicyResponseTypeDef",
    "GetAccountSummaryResponseTypeDef",
    "GetContextKeysForPolicyResponseTypeDef",
    "GetCredentialReportResponseTypeDef",
    "GetGroupPolicyResponseTypeDef",
    "GetGroupResponseTypeDef",
    "GetInstanceProfileResponseTypeDef",
    "GetLoginProfileResponseTypeDef",
    "GetOpenIDConnectProviderResponseTypeDef",
    "GetOrganizationsAccessReportResponseTypeDef",
    "GetPolicyResponseTypeDef",
    "GetPolicyVersionResponseTypeDef",
    "GetRolePolicyResponseTypeDef",
    "GetRoleResponseTypeDef",
    "GetSAMLProviderResponseTypeDef",
    "GetSSHPublicKeyResponseTypeDef",
    "GetServerCertificateResponseTypeDef",
    "GetServiceLastAccessedDetailsResponseTypeDef",
    "GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
    "GetServiceLinkedRoleDeletionStatusResponseTypeDef",
    "GetUserPolicyResponseTypeDef",
    "GetUserResponseTypeDef",
    "GroupDetailTypeDef",
    "GroupTypeDef",
    "InstanceProfileTypeDef",
    "ListAccessKeysResponseTypeDef",
    "ListAccountAliasesResponseTypeDef",
    "ListAttachedGroupPoliciesResponseTypeDef",
    "ListAttachedRolePoliciesResponseTypeDef",
    "ListAttachedUserPoliciesResponseTypeDef",
    "ListEntitiesForPolicyResponseTypeDef",
    "ListGroupPoliciesResponseTypeDef",
    "ListGroupsForUserResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "ListInstanceProfileTagsResponseTypeDef",
    "ListInstanceProfilesForRoleResponseTypeDef",
    "ListInstanceProfilesResponseTypeDef",
    "ListMFADeviceTagsResponseTypeDef",
    "ListMFADevicesResponseTypeDef",
    "ListOpenIDConnectProviderTagsResponseTypeDef",
    "ListOpenIDConnectProvidersResponseTypeDef",
    "ListPoliciesGrantingServiceAccessEntryTypeDef",
    "ListPoliciesGrantingServiceAccessResponseTypeDef",
    "ListPoliciesResponseTypeDef",
    "ListPolicyTagsResponseTypeDef",
    "ListPolicyVersionsResponseTypeDef",
    "ListRolePoliciesResponseTypeDef",
    "ListRoleTagsResponseTypeDef",
    "ListRolesResponseTypeDef",
    "ListSAMLProviderTagsResponseTypeDef",
    "ListSAMLProvidersResponseTypeDef",
    "ListSSHPublicKeysResponseTypeDef",
    "ListServerCertificateTagsResponseTypeDef",
    "ListServerCertificatesResponseTypeDef",
    "ListServiceSpecificCredentialsResponseTypeDef",
    "ListSigningCertificatesResponseTypeDef",
    "ListUserPoliciesResponseTypeDef",
    "ListUserTagsResponseTypeDef",
    "ListUsersResponseTypeDef",
    "ListVirtualMFADevicesResponseTypeDef",
    "LoginProfileTypeDef",
    "MFADeviceTypeDef",
    "ManagedPolicyDetailTypeDef",
    "OpenIDConnectProviderListEntryTypeDef",
    "OrganizationsDecisionDetailTypeDef",
    "PaginatorConfigTypeDef",
    "PasswordPolicyTypeDef",
    "PermissionsBoundaryDecisionDetailTypeDef",
    "PolicyDetailTypeDef",
    "PolicyGrantingServiceAccessTypeDef",
    "PolicyGroupTypeDef",
    "PolicyRoleTypeDef",
    "PolicyTypeDef",
    "PolicyUserTypeDef",
    "PolicyVersionTypeDef",
    "PositionTypeDef",
    "ResetServiceSpecificCredentialResponseTypeDef",
    "ResourceSpecificResultTypeDef",
    "RoleDetailTypeDef",
    "RoleLastUsedTypeDef",
    "RoleTypeDef",
    "RoleUsageTypeTypeDef",
    "SAMLProviderListEntryTypeDef",
    "SSHPublicKeyMetadataTypeDef",
    "SSHPublicKeyTypeDef",
    "ServerCertificateMetadataTypeDef",
    "ServerCertificateTypeDef",
    "ServiceLastAccessedTypeDef",
    "ServiceSpecificCredentialMetadataTypeDef",
    "ServiceSpecificCredentialTypeDef",
    "SigningCertificateTypeDef",
    "SimulatePolicyResponseTypeDef",
    "StatementTypeDef",
    "TagTypeDef",
    "TrackedActionLastAccessedTypeDef",
    "UpdateRoleDescriptionResponseTypeDef",
    "UpdateSAMLProviderResponseTypeDef",
    "UploadSSHPublicKeyResponseTypeDef",
    "UploadServerCertificateResponseTypeDef",
    "UploadSigningCertificateResponseTypeDef",
    "UserDetailTypeDef",
    "UserTypeDef",
    "VirtualMFADeviceTypeDef",
    "WaiterConfigTypeDef",
)


class _RequiredAccessDetailTypeDef(TypedDict):
    ServiceName: str
    ServiceNamespace: str


class AccessDetailTypeDef(_RequiredAccessDetailTypeDef, total=False):
    Region: str
    EntityPath: str
    LastAuthenticatedTime: datetime
    TotalAuthenticatedEntities: int


class AccessKeyLastUsedTypeDef(TypedDict):
    LastUsedDate: datetime
    ServiceName: str
    Region: str


class AccessKeyMetadataTypeDef(TypedDict, total=False):
    UserName: str
    AccessKeyId: str
    Status: statusType
    CreateDate: datetime


class _RequiredAccessKeyTypeDef(TypedDict):
    UserName: str
    AccessKeyId: str
    Status: statusType
    SecretAccessKey: str


class AccessKeyTypeDef(_RequiredAccessKeyTypeDef, total=False):
    CreateDate: datetime


class AttachedPermissionsBoundaryTypeDef(TypedDict, total=False):
    PermissionsBoundaryType: Literal["PermissionsBoundaryPolicy"]
    PermissionsBoundaryArn: str


class AttachedPolicyTypeDef(TypedDict, total=False):
    PolicyName: str
    PolicyArn: str


class ContextEntryTypeDef(TypedDict, total=False):
    ContextKeyName: str
    ContextKeyValues: List[str]
    ContextKeyType: ContextKeyTypeEnum


class CreateAccessKeyResponseTypeDef(TypedDict):
    AccessKey: "AccessKeyTypeDef"


class CreateGroupResponseTypeDef(TypedDict):
    Group: "GroupTypeDef"


class CreateInstanceProfileResponseTypeDef(TypedDict):
    InstanceProfile: "InstanceProfileTypeDef"


class CreateLoginProfileResponseTypeDef(TypedDict):
    LoginProfile: "LoginProfileTypeDef"


class CreateOpenIDConnectProviderResponseTypeDef(TypedDict, total=False):
    OpenIDConnectProviderArn: str
    Tags: List["TagTypeDef"]


class CreatePolicyResponseTypeDef(TypedDict, total=False):
    Policy: "PolicyTypeDef"


class CreatePolicyVersionResponseTypeDef(TypedDict, total=False):
    PolicyVersion: "PolicyVersionTypeDef"


class CreateRoleResponseTypeDef(TypedDict):
    Role: "RoleTypeDef"


class CreateSAMLProviderResponseTypeDef(TypedDict, total=False):
    SAMLProviderArn: str
    Tags: List["TagTypeDef"]


class CreateServiceLinkedRoleResponseTypeDef(TypedDict, total=False):
    Role: "RoleTypeDef"


class CreateServiceSpecificCredentialResponseTypeDef(TypedDict, total=False):
    ServiceSpecificCredential: "ServiceSpecificCredentialTypeDef"


class CreateUserResponseTypeDef(TypedDict, total=False):
    User: "UserTypeDef"


class CreateVirtualMFADeviceResponseTypeDef(TypedDict):
    VirtualMFADevice: "VirtualMFADeviceTypeDef"


class DeleteServiceLinkedRoleResponseTypeDef(TypedDict):
    DeletionTaskId: str


class DeletionTaskFailureReasonTypeTypeDef(TypedDict, total=False):
    Reason: str
    RoleUsageList: List["RoleUsageTypeTypeDef"]


class _RequiredEntityDetailsTypeDef(TypedDict):
    EntityInfo: "EntityInfoTypeDef"


class EntityDetailsTypeDef(_RequiredEntityDetailsTypeDef, total=False):
    LastAuthenticated: datetime


_RequiredEntityInfoTypeDef = TypedDict(
    "_RequiredEntityInfoTypeDef",
    {"Arn": str, "Name": str, "Type": policyOwnerEntityType, "Id": str},
)
_OptionalEntityInfoTypeDef = TypedDict("_OptionalEntityInfoTypeDef", {"Path": str}, total=False)


class EntityInfoTypeDef(_RequiredEntityInfoTypeDef, _OptionalEntityInfoTypeDef):
    pass


class ErrorDetailsTypeDef(TypedDict):
    Message: str
    Code: str


class _RequiredEvaluationResultTypeDef(TypedDict):
    EvalActionName: str
    EvalDecision: PolicyEvaluationDecisionType


class EvaluationResultTypeDef(_RequiredEvaluationResultTypeDef, total=False):
    EvalResourceName: str
    MatchedStatements: List["StatementTypeDef"]
    MissingContextValues: List[str]
    OrganizationsDecisionDetail: "OrganizationsDecisionDetailTypeDef"
    PermissionsBoundaryDecisionDetail: "PermissionsBoundaryDecisionDetailTypeDef"
    EvalDecisionDetails: Dict[str, PolicyEvaluationDecisionType]
    ResourceSpecificResults: List["ResourceSpecificResultTypeDef"]


class GenerateCredentialReportResponseTypeDef(TypedDict, total=False):
    State: ReportStateType
    Description: str


class GenerateOrganizationsAccessReportResponseTypeDef(TypedDict, total=False):
    JobId: str


class GenerateServiceLastAccessedDetailsResponseTypeDef(TypedDict, total=False):
    JobId: str


class GetAccessKeyLastUsedResponseTypeDef(TypedDict, total=False):
    UserName: str
    AccessKeyLastUsed: "AccessKeyLastUsedTypeDef"


class GetAccountAuthorizationDetailsResponseTypeDef(TypedDict, total=False):
    UserDetailList: List["UserDetailTypeDef"]
    GroupDetailList: List["GroupDetailTypeDef"]
    RoleDetailList: List["RoleDetailTypeDef"]
    Policies: List["ManagedPolicyDetailTypeDef"]
    IsTruncated: bool
    Marker: str


class GetAccountPasswordPolicyResponseTypeDef(TypedDict):
    PasswordPolicy: "PasswordPolicyTypeDef"


class GetAccountSummaryResponseTypeDef(TypedDict, total=False):
    SummaryMap: Dict[summaryKeyType, int]


class GetContextKeysForPolicyResponseTypeDef(TypedDict, total=False):
    ContextKeyNames: List[str]


class GetCredentialReportResponseTypeDef(TypedDict, total=False):
    Content: Union[bytes, IO[bytes]]
    ReportFormat: Literal["text/csv"]
    GeneratedTime: datetime


class GetGroupPolicyResponseTypeDef(TypedDict):
    GroupName: str
    PolicyName: str
    PolicyDocument: str


class _RequiredGetGroupResponseTypeDef(TypedDict):
    Group: "GroupTypeDef"
    Users: List["UserTypeDef"]


class GetGroupResponseTypeDef(_RequiredGetGroupResponseTypeDef, total=False):
    IsTruncated: bool
    Marker: str


class GetInstanceProfileResponseTypeDef(TypedDict):
    InstanceProfile: "InstanceProfileTypeDef"


class GetLoginProfileResponseTypeDef(TypedDict):
    LoginProfile: "LoginProfileTypeDef"


class GetOpenIDConnectProviderResponseTypeDef(TypedDict, total=False):
    Url: str
    ClientIDList: List[str]
    ThumbprintList: List[str]
    CreateDate: datetime
    Tags: List["TagTypeDef"]


class _RequiredGetOrganizationsAccessReportResponseTypeDef(TypedDict):
    JobStatus: jobStatusType
    JobCreationDate: datetime


class GetOrganizationsAccessReportResponseTypeDef(
    _RequiredGetOrganizationsAccessReportResponseTypeDef, total=False
):
    JobCompletionDate: datetime
    NumberOfServicesAccessible: int
    NumberOfServicesNotAccessed: int
    AccessDetails: List["AccessDetailTypeDef"]
    IsTruncated: bool
    Marker: str
    ErrorDetails: "ErrorDetailsTypeDef"


class GetPolicyResponseTypeDef(TypedDict, total=False):
    Policy: "PolicyTypeDef"


class GetPolicyVersionResponseTypeDef(TypedDict, total=False):
    PolicyVersion: "PolicyVersionTypeDef"


class GetRolePolicyResponseTypeDef(TypedDict):
    RoleName: str
    PolicyName: str
    PolicyDocument: str


class GetRoleResponseTypeDef(TypedDict):
    Role: "RoleTypeDef"


class GetSAMLProviderResponseTypeDef(TypedDict, total=False):
    SAMLMetadataDocument: str
    CreateDate: datetime
    ValidUntil: datetime
    Tags: List["TagTypeDef"]


class GetSSHPublicKeyResponseTypeDef(TypedDict, total=False):
    SSHPublicKey: "SSHPublicKeyTypeDef"


class GetServerCertificateResponseTypeDef(TypedDict):
    ServerCertificate: "ServerCertificateTypeDef"


class _RequiredGetServiceLastAccessedDetailsResponseTypeDef(TypedDict):
    JobStatus: jobStatusType
    JobCreationDate: datetime
    ServicesLastAccessed: List["ServiceLastAccessedTypeDef"]
    JobCompletionDate: datetime


class GetServiceLastAccessedDetailsResponseTypeDef(
    _RequiredGetServiceLastAccessedDetailsResponseTypeDef, total=False
):
    JobType: AccessAdvisorUsageGranularityType
    IsTruncated: bool
    Marker: str
    Error: "ErrorDetailsTypeDef"


class _RequiredGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef(TypedDict):
    JobStatus: jobStatusType
    JobCreationDate: datetime
    JobCompletionDate: datetime
    EntityDetailsList: List["EntityDetailsTypeDef"]


class GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef(
    _RequiredGetServiceLastAccessedDetailsWithEntitiesResponseTypeDef, total=False
):
    IsTruncated: bool
    Marker: str
    Error: "ErrorDetailsTypeDef"


class _RequiredGetServiceLinkedRoleDeletionStatusResponseTypeDef(TypedDict):
    Status: DeletionTaskStatusType


class GetServiceLinkedRoleDeletionStatusResponseTypeDef(
    _RequiredGetServiceLinkedRoleDeletionStatusResponseTypeDef, total=False
):
    Reason: "DeletionTaskFailureReasonTypeTypeDef"


class GetUserPolicyResponseTypeDef(TypedDict):
    UserName: str
    PolicyName: str
    PolicyDocument: str


class GetUserResponseTypeDef(TypedDict):
    User: "UserTypeDef"


class GroupDetailTypeDef(TypedDict, total=False):
    Path: str
    GroupName: str
    GroupId: str
    Arn: str
    CreateDate: datetime
    GroupPolicyList: List["PolicyDetailTypeDef"]
    AttachedManagedPolicies: List["AttachedPolicyTypeDef"]


class GroupTypeDef(TypedDict):
    Path: str
    GroupName: str
    GroupId: str
    Arn: str
    CreateDate: datetime


class _RequiredInstanceProfileTypeDef(TypedDict):
    Path: str
    InstanceProfileName: str
    InstanceProfileId: str
    Arn: str
    CreateDate: datetime
    Roles: List["RoleTypeDef"]


class InstanceProfileTypeDef(_RequiredInstanceProfileTypeDef, total=False):
    Tags: List["TagTypeDef"]


class _RequiredListAccessKeysResponseTypeDef(TypedDict):
    AccessKeyMetadata: List["AccessKeyMetadataTypeDef"]


class ListAccessKeysResponseTypeDef(_RequiredListAccessKeysResponseTypeDef, total=False):
    IsTruncated: bool
    Marker: str


class _RequiredListAccountAliasesResponseTypeDef(TypedDict):
    AccountAliases: List[str]


class ListAccountAliasesResponseTypeDef(_RequiredListAccountAliasesResponseTypeDef, total=False):
    IsTruncated: bool
    Marker: str


class ListAttachedGroupPoliciesResponseTypeDef(TypedDict, total=False):
    AttachedPolicies: List["AttachedPolicyTypeDef"]
    IsTruncated: bool
    Marker: str


class ListAttachedRolePoliciesResponseTypeDef(TypedDict, total=False):
    AttachedPolicies: List["AttachedPolicyTypeDef"]
    IsTruncated: bool
    Marker: str


class ListAttachedUserPoliciesResponseTypeDef(TypedDict, total=False):
    AttachedPolicies: List["AttachedPolicyTypeDef"]
    IsTruncated: bool
    Marker: str


class ListEntitiesForPolicyResponseTypeDef(TypedDict, total=False):
    PolicyGroups: List["PolicyGroupTypeDef"]
    PolicyUsers: List["PolicyUserTypeDef"]
    PolicyRoles: List["PolicyRoleTypeDef"]
    IsTruncated: bool
    Marker: str


class _RequiredListGroupPoliciesResponseTypeDef(TypedDict):
    PolicyNames: List[str]


class ListGroupPoliciesResponseTypeDef(_RequiredListGroupPoliciesResponseTypeDef, total=False):
    IsTruncated: bool
    Marker: str


class _RequiredListGroupsForUserResponseTypeDef(TypedDict):
    Groups: List["GroupTypeDef"]


class ListGroupsForUserResponseTypeDef(_RequiredListGroupsForUserResponseTypeDef, total=False):
    IsTruncated: bool
    Marker: str


class _RequiredListGroupsResponseTypeDef(TypedDict):
    Groups: List["GroupTypeDef"]


class ListGroupsResponseTypeDef(_RequiredListGroupsResponseTypeDef, total=False):
    IsTruncated: bool
    Marker: str


class _RequiredListInstanceProfileTagsResponseTypeDef(TypedDict):
    Tags: List["TagTypeDef"]


class ListInstanceProfileTagsResponseTypeDef(
    _RequiredListInstanceProfileTagsResponseTypeDef, total=False
):
    IsTruncated: bool
    Marker: str


class _RequiredListInstanceProfilesForRoleResponseTypeDef(TypedDict):
    InstanceProfiles: List["InstanceProfileTypeDef"]


class ListInstanceProfilesForRoleResponseTypeDef(
    _RequiredListInstanceProfilesForRoleResponseTypeDef, total=False
):
    IsTruncated: bool
    Marker: str


class _RequiredListInstanceProfilesResponseTypeDef(TypedDict):
    InstanceProfiles: List["InstanceProfileTypeDef"]


class ListInstanceProfilesResponseTypeDef(
    _RequiredListInstanceProfilesResponseTypeDef, total=False
):
    IsTruncated: bool
    Marker: str


class _RequiredListMFADeviceTagsResponseTypeDef(TypedDict):
    Tags: List["TagTypeDef"]


class ListMFADeviceTagsResponseTypeDef(_RequiredListMFADeviceTagsResponseTypeDef, total=False):
    IsTruncated: bool
    Marker: str


class _RequiredListMFADevicesResponseTypeDef(TypedDict):
    MFADevices: List["MFADeviceTypeDef"]


class ListMFADevicesResponseTypeDef(_RequiredListMFADevicesResponseTypeDef, total=False):
    IsTruncated: bool
    Marker: str


class _RequiredListOpenIDConnectProviderTagsResponseTypeDef(TypedDict):
    Tags: List["TagTypeDef"]


class ListOpenIDConnectProviderTagsResponseTypeDef(
    _RequiredListOpenIDConnectProviderTagsResponseTypeDef, total=False
):
    IsTruncated: bool
    Marker: str


class ListOpenIDConnectProvidersResponseTypeDef(TypedDict, total=False):
    OpenIDConnectProviderList: List["OpenIDConnectProviderListEntryTypeDef"]


class ListPoliciesGrantingServiceAccessEntryTypeDef(TypedDict, total=False):
    ServiceNamespace: str
    Policies: List["PolicyGrantingServiceAccessTypeDef"]


class _RequiredListPoliciesGrantingServiceAccessResponseTypeDef(TypedDict):
    PoliciesGrantingServiceAccess: List["ListPoliciesGrantingServiceAccessEntryTypeDef"]


class ListPoliciesGrantingServiceAccessResponseTypeDef(
    _RequiredListPoliciesGrantingServiceAccessResponseTypeDef, total=False
):
    IsTruncated: bool
    Marker: str


class ListPoliciesResponseTypeDef(TypedDict, total=False):
    Policies: List["PolicyTypeDef"]
    IsTruncated: bool
    Marker: str


class _RequiredListPolicyTagsResponseTypeDef(TypedDict):
    Tags: List["TagTypeDef"]


class ListPolicyTagsResponseTypeDef(_RequiredListPolicyTagsResponseTypeDef, total=False):
    IsTruncated: bool
    Marker: str


class ListPolicyVersionsResponseTypeDef(TypedDict, total=False):
    Versions: List["PolicyVersionTypeDef"]
    IsTruncated: bool
    Marker: str


class _RequiredListRolePoliciesResponseTypeDef(TypedDict):
    PolicyNames: List[str]


class ListRolePoliciesResponseTypeDef(_RequiredListRolePoliciesResponseTypeDef, total=False):
    IsTruncated: bool
    Marker: str


class _RequiredListRoleTagsResponseTypeDef(TypedDict):
    Tags: List["TagTypeDef"]


class ListRoleTagsResponseTypeDef(_RequiredListRoleTagsResponseTypeDef, total=False):
    IsTruncated: bool
    Marker: str


class _RequiredListRolesResponseTypeDef(TypedDict):
    Roles: List["RoleTypeDef"]


class ListRolesResponseTypeDef(_RequiredListRolesResponseTypeDef, total=False):
    IsTruncated: bool
    Marker: str


class _RequiredListSAMLProviderTagsResponseTypeDef(TypedDict):
    Tags: List["TagTypeDef"]


class ListSAMLProviderTagsResponseTypeDef(
    _RequiredListSAMLProviderTagsResponseTypeDef, total=False
):
    IsTruncated: bool
    Marker: str


class ListSAMLProvidersResponseTypeDef(TypedDict, total=False):
    SAMLProviderList: List["SAMLProviderListEntryTypeDef"]


class ListSSHPublicKeysResponseTypeDef(TypedDict, total=False):
    SSHPublicKeys: List["SSHPublicKeyMetadataTypeDef"]
    IsTruncated: bool
    Marker: str


class _RequiredListServerCertificateTagsResponseTypeDef(TypedDict):
    Tags: List["TagTypeDef"]


class ListServerCertificateTagsResponseTypeDef(
    _RequiredListServerCertificateTagsResponseTypeDef, total=False
):
    IsTruncated: bool
    Marker: str


class _RequiredListServerCertificatesResponseTypeDef(TypedDict):
    ServerCertificateMetadataList: List["ServerCertificateMetadataTypeDef"]


class ListServerCertificatesResponseTypeDef(
    _RequiredListServerCertificatesResponseTypeDef, total=False
):
    IsTruncated: bool
    Marker: str


class ListServiceSpecificCredentialsResponseTypeDef(TypedDict, total=False):
    ServiceSpecificCredentials: List["ServiceSpecificCredentialMetadataTypeDef"]


class _RequiredListSigningCertificatesResponseTypeDef(TypedDict):
    Certificates: List["SigningCertificateTypeDef"]


class ListSigningCertificatesResponseTypeDef(
    _RequiredListSigningCertificatesResponseTypeDef, total=False
):
    IsTruncated: bool
    Marker: str


class _RequiredListUserPoliciesResponseTypeDef(TypedDict):
    PolicyNames: List[str]


class ListUserPoliciesResponseTypeDef(_RequiredListUserPoliciesResponseTypeDef, total=False):
    IsTruncated: bool
    Marker: str


class _RequiredListUserTagsResponseTypeDef(TypedDict):
    Tags: List["TagTypeDef"]


class ListUserTagsResponseTypeDef(_RequiredListUserTagsResponseTypeDef, total=False):
    IsTruncated: bool
    Marker: str


class _RequiredListUsersResponseTypeDef(TypedDict):
    Users: List["UserTypeDef"]


class ListUsersResponseTypeDef(_RequiredListUsersResponseTypeDef, total=False):
    IsTruncated: bool
    Marker: str


class _RequiredListVirtualMFADevicesResponseTypeDef(TypedDict):
    VirtualMFADevices: List["VirtualMFADeviceTypeDef"]


class ListVirtualMFADevicesResponseTypeDef(
    _RequiredListVirtualMFADevicesResponseTypeDef, total=False
):
    IsTruncated: bool
    Marker: str


class _RequiredLoginProfileTypeDef(TypedDict):
    UserName: str
    CreateDate: datetime


class LoginProfileTypeDef(_RequiredLoginProfileTypeDef, total=False):
    PasswordResetRequired: bool


class MFADeviceTypeDef(TypedDict):
    UserName: str
    SerialNumber: str
    EnableDate: datetime


class ManagedPolicyDetailTypeDef(TypedDict, total=False):
    PolicyName: str
    PolicyId: str
    Arn: str
    Path: str
    DefaultVersionId: str
    AttachmentCount: int
    PermissionsBoundaryUsageCount: int
    IsAttachable: bool
    Description: str
    CreateDate: datetime
    UpdateDate: datetime
    PolicyVersionList: List["PolicyVersionTypeDef"]


class OpenIDConnectProviderListEntryTypeDef(TypedDict, total=False):
    Arn: str


class OrganizationsDecisionDetailTypeDef(TypedDict, total=False):
    AllowedByOrganizations: bool


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PasswordPolicyTypeDef(TypedDict, total=False):
    MinimumPasswordLength: int
    RequireSymbols: bool
    RequireNumbers: bool
    RequireUppercaseCharacters: bool
    RequireLowercaseCharacters: bool
    AllowUsersToChangePassword: bool
    ExpirePasswords: bool
    MaxPasswordAge: int
    PasswordReusePrevention: int
    HardExpiry: bool


class PermissionsBoundaryDecisionDetailTypeDef(TypedDict, total=False):
    AllowedByPermissionsBoundary: bool


class PolicyDetailTypeDef(TypedDict, total=False):
    PolicyName: str
    PolicyDocument: str


class _RequiredPolicyGrantingServiceAccessTypeDef(TypedDict):
    PolicyName: str
    PolicyType: policyType


class PolicyGrantingServiceAccessTypeDef(_RequiredPolicyGrantingServiceAccessTypeDef, total=False):
    PolicyArn: str
    EntityType: policyOwnerEntityType
    EntityName: str


class PolicyGroupTypeDef(TypedDict, total=False):
    GroupName: str
    GroupId: str


class PolicyRoleTypeDef(TypedDict, total=False):
    RoleName: str
    RoleId: str


class PolicyTypeDef(TypedDict, total=False):
    PolicyName: str
    PolicyId: str
    Arn: str
    Path: str
    DefaultVersionId: str
    AttachmentCount: int
    PermissionsBoundaryUsageCount: int
    IsAttachable: bool
    Description: str
    CreateDate: datetime
    UpdateDate: datetime
    Tags: List["TagTypeDef"]


class PolicyUserTypeDef(TypedDict, total=False):
    UserName: str
    UserId: str


class PolicyVersionTypeDef(TypedDict, total=False):
    Document: str
    VersionId: str
    IsDefaultVersion: bool
    CreateDate: datetime


class PositionTypeDef(TypedDict, total=False):
    Line: int
    Column: int


class ResetServiceSpecificCredentialResponseTypeDef(TypedDict, total=False):
    ServiceSpecificCredential: "ServiceSpecificCredentialTypeDef"


class _RequiredResourceSpecificResultTypeDef(TypedDict):
    EvalResourceName: str
    EvalResourceDecision: PolicyEvaluationDecisionType


class ResourceSpecificResultTypeDef(_RequiredResourceSpecificResultTypeDef, total=False):
    MatchedStatements: List["StatementTypeDef"]
    MissingContextValues: List[str]
    EvalDecisionDetails: Dict[str, PolicyEvaluationDecisionType]
    PermissionsBoundaryDecisionDetail: "PermissionsBoundaryDecisionDetailTypeDef"


class RoleDetailTypeDef(TypedDict, total=False):
    Path: str
    RoleName: str
    RoleId: str
    Arn: str
    CreateDate: datetime
    AssumeRolePolicyDocument: str
    InstanceProfileList: List["InstanceProfileTypeDef"]
    RolePolicyList: List["PolicyDetailTypeDef"]
    AttachedManagedPolicies: List["AttachedPolicyTypeDef"]
    PermissionsBoundary: "AttachedPermissionsBoundaryTypeDef"
    Tags: List["TagTypeDef"]
    RoleLastUsed: "RoleLastUsedTypeDef"


class RoleLastUsedTypeDef(TypedDict, total=False):
    LastUsedDate: datetime
    Region: str


class _RequiredRoleTypeDef(TypedDict):
    Path: str
    RoleName: str
    RoleId: str
    Arn: str
    CreateDate: datetime


class RoleTypeDef(_RequiredRoleTypeDef, total=False):
    AssumeRolePolicyDocument: str
    Description: str
    MaxSessionDuration: int
    PermissionsBoundary: "AttachedPermissionsBoundaryTypeDef"
    Tags: List["TagTypeDef"]
    RoleLastUsed: "RoleLastUsedTypeDef"


class RoleUsageTypeTypeDef(TypedDict, total=False):
    Region: str
    Resources: List[str]


class SAMLProviderListEntryTypeDef(TypedDict, total=False):
    Arn: str
    ValidUntil: datetime
    CreateDate: datetime


class SSHPublicKeyMetadataTypeDef(TypedDict):
    UserName: str
    SSHPublicKeyId: str
    Status: statusType
    UploadDate: datetime


class _RequiredSSHPublicKeyTypeDef(TypedDict):
    UserName: str
    SSHPublicKeyId: str
    Fingerprint: str
    SSHPublicKeyBody: str
    Status: statusType


class SSHPublicKeyTypeDef(_RequiredSSHPublicKeyTypeDef, total=False):
    UploadDate: datetime


class _RequiredServerCertificateMetadataTypeDef(TypedDict):
    Path: str
    ServerCertificateName: str
    ServerCertificateId: str
    Arn: str


class ServerCertificateMetadataTypeDef(_RequiredServerCertificateMetadataTypeDef, total=False):
    UploadDate: datetime
    Expiration: datetime


class _RequiredServerCertificateTypeDef(TypedDict):
    ServerCertificateMetadata: "ServerCertificateMetadataTypeDef"
    CertificateBody: str


class ServerCertificateTypeDef(_RequiredServerCertificateTypeDef, total=False):
    CertificateChain: str
    Tags: List["TagTypeDef"]


class _RequiredServiceLastAccessedTypeDef(TypedDict):
    ServiceName: str
    ServiceNamespace: str


class ServiceLastAccessedTypeDef(_RequiredServiceLastAccessedTypeDef, total=False):
    LastAuthenticated: datetime
    LastAuthenticatedEntity: str
    LastAuthenticatedRegion: str
    TotalAuthenticatedEntities: int
    TrackedActionsLastAccessed: List["TrackedActionLastAccessedTypeDef"]


class ServiceSpecificCredentialMetadataTypeDef(TypedDict):
    UserName: str
    Status: statusType
    ServiceUserName: str
    CreateDate: datetime
    ServiceSpecificCredentialId: str
    ServiceName: str


class ServiceSpecificCredentialTypeDef(TypedDict):
    CreateDate: datetime
    ServiceName: str
    ServiceUserName: str
    ServicePassword: str
    ServiceSpecificCredentialId: str
    UserName: str
    Status: statusType


class _RequiredSigningCertificateTypeDef(TypedDict):
    UserName: str
    CertificateId: str
    CertificateBody: str
    Status: statusType


class SigningCertificateTypeDef(_RequiredSigningCertificateTypeDef, total=False):
    UploadDate: datetime


class SimulatePolicyResponseTypeDef(TypedDict, total=False):
    EvaluationResults: List["EvaluationResultTypeDef"]
    IsTruncated: bool
    Marker: str


class StatementTypeDef(TypedDict, total=False):
    SourcePolicyId: str
    SourcePolicyType: PolicySourceType
    StartPosition: "PositionTypeDef"
    EndPosition: "PositionTypeDef"


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TrackedActionLastAccessedTypeDef(TypedDict, total=False):
    ActionName: str
    LastAccessedEntity: str
    LastAccessedTime: datetime
    LastAccessedRegion: str


class UpdateRoleDescriptionResponseTypeDef(TypedDict, total=False):
    Role: "RoleTypeDef"


class UpdateSAMLProviderResponseTypeDef(TypedDict, total=False):
    SAMLProviderArn: str


class UploadSSHPublicKeyResponseTypeDef(TypedDict, total=False):
    SSHPublicKey: "SSHPublicKeyTypeDef"


class UploadServerCertificateResponseTypeDef(TypedDict, total=False):
    ServerCertificateMetadata: "ServerCertificateMetadataTypeDef"
    Tags: List["TagTypeDef"]


class UploadSigningCertificateResponseTypeDef(TypedDict):
    Certificate: "SigningCertificateTypeDef"


class UserDetailTypeDef(TypedDict, total=False):
    Path: str
    UserName: str
    UserId: str
    Arn: str
    CreateDate: datetime
    UserPolicyList: List["PolicyDetailTypeDef"]
    GroupList: List[str]
    AttachedManagedPolicies: List["AttachedPolicyTypeDef"]
    PermissionsBoundary: "AttachedPermissionsBoundaryTypeDef"
    Tags: List["TagTypeDef"]


class _RequiredUserTypeDef(TypedDict):
    Path: str
    UserName: str
    UserId: str
    Arn: str
    CreateDate: datetime


class UserTypeDef(_RequiredUserTypeDef, total=False):
    PasswordLastUsed: datetime
    PermissionsBoundary: "AttachedPermissionsBoundaryTypeDef"
    Tags: List["TagTypeDef"]


class _RequiredVirtualMFADeviceTypeDef(TypedDict):
    SerialNumber: str


class VirtualMFADeviceTypeDef(_RequiredVirtualMFADeviceTypeDef, total=False):
    Base32StringSeed: Union[bytes, IO[bytes]]
    QRCodePNG: Union[bytes, IO[bytes]]
    User: "UserTypeDef"
    EnableDate: datetime
    Tags: List["TagTypeDef"]


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
