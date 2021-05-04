"""
Type annotations for iam service ServiceResource

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_iam import IAMServiceResource
    import mypy_boto3_iam.service_resource as iam_resources

    resource: IAMServiceResource = boto3.resource("iam")

    my_access_key: iam_resources.AccessKey = resource.AccessKey(...)
    my_access_key_pair: iam_resources.AccessKeyPair = resource.AccessKeyPair(...)
    my_account_password_policy: iam_resources.AccountPasswordPolicy = resource.AccountPasswordPolicy(...)
    my_account_summary: iam_resources.AccountSummary = resource.AccountSummary(...)
    my_assume_role_policy: iam_resources.AssumeRolePolicy = resource.AssumeRolePolicy(...)
    my_current_user: iam_resources.CurrentUser = resource.CurrentUser(...)
    my_group: iam_resources.Group = resource.Group(...)
    my_group_policy: iam_resources.GroupPolicy = resource.GroupPolicy(...)
    my_instance_profile: iam_resources.InstanceProfile = resource.InstanceProfile(...)
    my_login_profile: iam_resources.LoginProfile = resource.LoginProfile(...)
    my_mfa_device: iam_resources.MfaDevice = resource.MfaDevice(...)
    my_policy: iam_resources.Policy = resource.Policy(...)
    my_policy_version: iam_resources.PolicyVersion = resource.PolicyVersion(...)
    my_role: iam_resources.Role = resource.Role(...)
    my_role_policy: iam_resources.RolePolicy = resource.RolePolicy(...)
    my_saml_provider: iam_resources.SamlProvider = resource.SamlProvider(...)
    my_server_certificate: iam_resources.ServerCertificate = resource.ServerCertificate(...)
    my_signing_certificate: iam_resources.SigningCertificate = resource.SigningCertificate(...)
    my_user: iam_resources.User = resource.User(...)
    my_user_policy: iam_resources.UserPolicy = resource.UserPolicy(...)
    my_virtual_mfa_device: iam_resources.VirtualMfaDevice = resource.VirtualMfaDevice(...)
```
"""
from datetime import datetime
from typing import Any, Dict, Iterator, List

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from mypy_boto3_iam.literals import (
    EntityType,
    PolicyUsageType,
    assignmentStatusType,
    policyScopeType,
    statusType,
)
from mypy_boto3_iam.type_defs import TagTypeDef, UpdateSAMLProviderResponseTypeDef

__all__ = (
    "IAMServiceResource",
    "AccessKey",
    "AccessKeyPair",
    "AccountPasswordPolicy",
    "AccountSummary",
    "AssumeRolePolicy",
    "CurrentUser",
    "Group",
    "GroupPolicy",
    "InstanceProfile",
    "LoginProfile",
    "MfaDevice",
    "Policy",
    "PolicyVersion",
    "Role",
    "RolePolicy",
    "SamlProvider",
    "ServerCertificate",
    "SigningCertificate",
    "User",
    "UserPolicy",
    "VirtualMfaDevice",
    "ServiceResourceGroupsCollection",
    "ServiceResourceInstanceProfilesCollection",
    "ServiceResourcePoliciesCollection",
    "ServiceResourceRolesCollection",
    "ServiceResourceSamlProvidersCollection",
    "ServiceResourceServerCertificatesCollection",
    "ServiceResourceUsersCollection",
    "ServiceResourceVirtualMfaDevicesCollection",
    "CurrentUserAccessKeysCollection",
    "CurrentUserMfaDevicesCollection",
    "CurrentUserSigningCertificatesCollection",
    "GroupAttachedPoliciesCollection",
    "GroupPoliciesCollection",
    "GroupUsersCollection",
    "PolicyAttachedGroupsCollection",
    "PolicyAttachedRolesCollection",
    "PolicyAttachedUsersCollection",
    "PolicyVersionsCollection",
    "RoleAttachedPoliciesCollection",
    "RoleInstanceProfilesCollection",
    "RolePoliciesCollection",
    "UserAccessKeysCollection",
    "UserAttachedPoliciesCollection",
    "UserGroupsCollection",
    "UserMfaDevicesCollection",
    "UserPoliciesCollection",
    "UserSigningCertificatesCollection",
)


class ServiceResourceGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.ServiceResourceGroupsCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcegroups)
    """

    def all(self) -> "ServiceResourceGroupsCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "ServiceResourceGroupsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceGroupsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceGroupsCollection":
        pass

    def pages(self) -> Iterator[List["Group"]]:
        pass

    def __iter__(self) -> Iterator["Group"]:
        pass


class ServiceResourceInstanceProfilesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.ServiceResourceInstanceProfilesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceinstance-profiles)
    """

    def all(self) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceInstanceProfilesCollection":
        pass

    def pages(self) -> Iterator[List["InstanceProfile"]]:
        pass

    def __iter__(self) -> Iterator["InstanceProfile"]:
        pass


class ServiceResourcePoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.ServiceResourcePoliciesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcepolicies)
    """

    def all(self) -> "ServiceResourcePoliciesCollection":
        pass

    def filter(  # type: ignore
        self,
        Scope: policyScopeType = None,
        OnlyAttached: bool = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageType = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> "ServiceResourcePoliciesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourcePoliciesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourcePoliciesCollection":
        pass

    def pages(self) -> Iterator[List["Policy"]]:
        pass

    def __iter__(self) -> Iterator["Policy"]:
        pass


class ServiceResourceRolesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.ServiceResourceRolesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceroles)
    """

    def all(self) -> "ServiceResourceRolesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "ServiceResourceRolesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceRolesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceRolesCollection":
        pass

    def pages(self) -> Iterator[List["Role"]]:
        pass

    def __iter__(self) -> Iterator["Role"]:
        pass


class ServiceResourceSamlProvidersCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.ServiceResourceSamlProvidersCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcesaml-providers)
    """

    def all(self) -> "ServiceResourceSamlProvidersCollection":
        pass

    def filter(self) -> "ServiceResourceSamlProvidersCollection":  # type: ignore
        pass

    def limit(self, count: int) -> "ServiceResourceSamlProvidersCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceSamlProvidersCollection":
        pass

    def pages(self) -> Iterator[List["SamlProvider"]]:
        pass

    def __iter__(self) -> Iterator["SamlProvider"]:
        pass


class ServiceResourceServerCertificatesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.ServiceResourceServerCertificatesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceserver-certificates)
    """

    def all(self) -> "ServiceResourceServerCertificatesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "ServiceResourceServerCertificatesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceServerCertificatesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceServerCertificatesCollection":
        pass

    def pages(self) -> Iterator[List["ServerCertificate"]]:
        pass

    def __iter__(self) -> Iterator["ServerCertificate"]:
        pass


class ServiceResourceUsersCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.ServiceResourceUsersCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceusers)
    """

    def all(self) -> "ServiceResourceUsersCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "ServiceResourceUsersCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceUsersCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceUsersCollection":
        pass

    def pages(self) -> Iterator[List["User"]]:
        pass

    def __iter__(self) -> Iterator["User"]:
        pass


class ServiceResourceVirtualMfaDevicesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.ServiceResourceVirtualMfaDevicesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcevirtual-mfa-devices)
    """

    def all(self) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def filter(  # type: ignore
        self,
        AssignmentStatus: assignmentStatusType = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceVirtualMfaDevicesCollection":
        pass

    def pages(self) -> Iterator[List["VirtualMfaDevice"]]:
        pass

    def __iter__(self) -> Iterator["VirtualMfaDevice"]:
        pass


class CurrentUserAccessKeysCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.CurrentUser.CurrentUserAccessKeysCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceaccess-keys)
    """

    def all(self) -> "CurrentUserAccessKeysCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "CurrentUserAccessKeysCollection":
        pass

    def limit(self, count: int) -> "CurrentUserAccessKeysCollection":
        pass

    def page_size(self, count: int) -> "CurrentUserAccessKeysCollection":
        pass

    def pages(self) -> Iterator[List["AccessKey"]]:
        pass

    def __iter__(self) -> Iterator["AccessKey"]:
        pass


class CurrentUserMfaDevicesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.CurrentUser.CurrentUserMfaDevicesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcemfa-devices)
    """

    def all(self) -> "CurrentUserMfaDevicesCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "CurrentUserMfaDevicesCollection":
        pass

    def limit(self, count: int) -> "CurrentUserMfaDevicesCollection":
        pass

    def page_size(self, count: int) -> "CurrentUserMfaDevicesCollection":
        pass

    def pages(self) -> Iterator[List["MfaDevice"]]:
        pass

    def __iter__(self) -> Iterator["MfaDevice"]:
        pass


class CurrentUserSigningCertificatesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.CurrentUser.CurrentUserSigningCertificatesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcesigning-certificates)
    """

    def all(self) -> "CurrentUserSigningCertificatesCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "CurrentUserSigningCertificatesCollection":
        pass

    def limit(self, count: int) -> "CurrentUserSigningCertificatesCollection":
        pass

    def page_size(self, count: int) -> "CurrentUserSigningCertificatesCollection":
        pass

    def pages(self) -> Iterator[List["SigningCertificate"]]:
        pass

    def __iter__(self) -> Iterator["SigningCertificate"]:
        pass


class GroupAttachedPoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Group.GroupAttachedPoliciesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceattached-policies)
    """

    def all(self) -> "GroupAttachedPoliciesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "GroupAttachedPoliciesCollection":
        pass

    def limit(self, count: int) -> "GroupAttachedPoliciesCollection":
        pass

    def page_size(self, count: int) -> "GroupAttachedPoliciesCollection":
        pass

    def pages(self) -> Iterator[List["Policy"]]:
        pass

    def __iter__(self) -> Iterator["Policy"]:
        pass


class GroupPoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Group.GroupPoliciesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcepolicies)
    """

    def all(self) -> "GroupPoliciesCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "GroupPoliciesCollection":
        pass

    def limit(self, count: int) -> "GroupPoliciesCollection":
        pass

    def page_size(self, count: int) -> "GroupPoliciesCollection":
        pass

    def pages(self) -> Iterator[List["GroupPolicy"]]:
        pass

    def __iter__(self) -> Iterator["GroupPolicy"]:
        pass


class GroupUsersCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Group.GroupUsersCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceusers)
    """

    def all(self) -> "GroupUsersCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "GroupUsersCollection":
        pass

    def limit(self, count: int) -> "GroupUsersCollection":
        pass

    def page_size(self, count: int) -> "GroupUsersCollection":
        pass

    def pages(self) -> Iterator[List["User"]]:
        pass

    def __iter__(self) -> Iterator["User"]:
        pass


class PolicyAttachedGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Policy.PolicyAttachedGroupsCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceattached-groups)
    """

    def all(self) -> "PolicyAttachedGroupsCollection":
        pass

    def filter(  # type: ignore
        self,
        EntityFilter: EntityType = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageType = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> "PolicyAttachedGroupsCollection":
        pass

    def limit(self, count: int) -> "PolicyAttachedGroupsCollection":
        pass

    def page_size(self, count: int) -> "PolicyAttachedGroupsCollection":
        pass

    def pages(self) -> Iterator[List["Group"]]:
        pass

    def __iter__(self) -> Iterator["Group"]:
        pass


class PolicyAttachedRolesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Policy.PolicyAttachedRolesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceattached-roles)
    """

    def all(self) -> "PolicyAttachedRolesCollection":
        pass

    def filter(  # type: ignore
        self,
        EntityFilter: EntityType = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageType = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> "PolicyAttachedRolesCollection":
        pass

    def limit(self, count: int) -> "PolicyAttachedRolesCollection":
        pass

    def page_size(self, count: int) -> "PolicyAttachedRolesCollection":
        pass

    def pages(self) -> Iterator[List["Role"]]:
        pass

    def __iter__(self) -> Iterator["Role"]:
        pass


class PolicyAttachedUsersCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Policy.PolicyAttachedUsersCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceattached-users)
    """

    def all(self) -> "PolicyAttachedUsersCollection":
        pass

    def filter(  # type: ignore
        self,
        EntityFilter: EntityType = None,
        PathPrefix: str = None,
        PolicyUsageFilter: PolicyUsageType = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> "PolicyAttachedUsersCollection":
        pass

    def limit(self, count: int) -> "PolicyAttachedUsersCollection":
        pass

    def page_size(self, count: int) -> "PolicyAttachedUsersCollection":
        pass

    def pages(self) -> Iterator[List["User"]]:
        pass

    def __iter__(self) -> Iterator["User"]:
        pass


class PolicyVersionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Policy.PolicyVersionsCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceversions)
    """

    def all(self) -> "PolicyVersionsCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "PolicyVersionsCollection":
        pass

    def limit(self, count: int) -> "PolicyVersionsCollection":
        pass

    def page_size(self, count: int) -> "PolicyVersionsCollection":
        pass

    def pages(self) -> Iterator[List["PolicyVersion"]]:
        pass

    def __iter__(self) -> Iterator["PolicyVersion"]:
        pass


class RoleAttachedPoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Role.RoleAttachedPoliciesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceattached-policies)
    """

    def all(self) -> "RoleAttachedPoliciesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "RoleAttachedPoliciesCollection":
        pass

    def limit(self, count: int) -> "RoleAttachedPoliciesCollection":
        pass

    def page_size(self, count: int) -> "RoleAttachedPoliciesCollection":
        pass

    def pages(self) -> Iterator[List["Policy"]]:
        pass

    def __iter__(self) -> Iterator["Policy"]:
        pass


class RoleInstanceProfilesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Role.RoleInstanceProfilesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceinstance-profiles)
    """

    def all(self) -> "RoleInstanceProfilesCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "RoleInstanceProfilesCollection":
        pass

    def limit(self, count: int) -> "RoleInstanceProfilesCollection":
        pass

    def page_size(self, count: int) -> "RoleInstanceProfilesCollection":
        pass

    def pages(self) -> Iterator[List["InstanceProfile"]]:
        pass

    def __iter__(self) -> Iterator["InstanceProfile"]:
        pass


class RolePoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Role.RolePoliciesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcepolicies)
    """

    def all(self) -> "RolePoliciesCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "RolePoliciesCollection":
        pass

    def limit(self, count: int) -> "RolePoliciesCollection":
        pass

    def page_size(self, count: int) -> "RolePoliciesCollection":
        pass

    def pages(self) -> Iterator[List["RolePolicy"]]:
        pass

    def __iter__(self) -> Iterator["RolePolicy"]:
        pass


class UserAccessKeysCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.UserAccessKeysCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceaccess-keys)
    """

    def all(self) -> "UserAccessKeysCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "UserAccessKeysCollection":
        pass

    def limit(self, count: int) -> "UserAccessKeysCollection":
        pass

    def page_size(self, count: int) -> "UserAccessKeysCollection":
        pass

    def pages(self) -> Iterator[List["AccessKey"]]:
        pass

    def __iter__(self) -> Iterator["AccessKey"]:
        pass


class UserAttachedPoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.UserAttachedPoliciesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceattached-policies)
    """

    def all(self) -> "UserAttachedPoliciesCollection":
        pass

    def filter(  # type: ignore
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> "UserAttachedPoliciesCollection":
        pass

    def limit(self, count: int) -> "UserAttachedPoliciesCollection":
        pass

    def page_size(self, count: int) -> "UserAttachedPoliciesCollection":
        pass

    def pages(self) -> Iterator[List["Policy"]]:
        pass

    def __iter__(self) -> Iterator["Policy"]:
        pass


class UserGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.UserGroupsCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcegroups)
    """

    def all(self) -> "UserGroupsCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "UserGroupsCollection":
        pass

    def limit(self, count: int) -> "UserGroupsCollection":
        pass

    def page_size(self, count: int) -> "UserGroupsCollection":
        pass

    def pages(self) -> Iterator[List["Group"]]:
        pass

    def __iter__(self) -> Iterator["Group"]:
        pass


class UserMfaDevicesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.UserMfaDevicesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcemfa-devices)
    """

    def all(self) -> "UserMfaDevicesCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "UserMfaDevicesCollection":
        pass

    def limit(self, count: int) -> "UserMfaDevicesCollection":
        pass

    def page_size(self, count: int) -> "UserMfaDevicesCollection":
        pass

    def pages(self) -> Iterator[List["MfaDevice"]]:
        pass

    def __iter__(self) -> Iterator["MfaDevice"]:
        pass


class UserPoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.UserPoliciesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcepolicies)
    """

    def all(self) -> "UserPoliciesCollection":
        pass

    def filter(  # type: ignore
        self, Marker: str = None, MaxItems: int = None
    ) -> "UserPoliciesCollection":
        pass

    def limit(self, count: int) -> "UserPoliciesCollection":
        pass

    def page_size(self, count: int) -> "UserPoliciesCollection":
        pass

    def pages(self) -> Iterator[List["UserPolicy"]]:
        pass

    def __iter__(self) -> Iterator["UserPolicy"]:
        pass


class UserSigningCertificatesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.UserSigningCertificatesCollection)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcesigning-certificates)
    """

    def all(self) -> "UserSigningCertificatesCollection":
        pass

    def filter(  # type: ignore
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> "UserSigningCertificatesCollection":
        pass

    def limit(self, count: int) -> "UserSigningCertificatesCollection":
        pass

    def page_size(self, count: int) -> "UserSigningCertificatesCollection":
        pass

    def pages(self) -> Iterator[List["SigningCertificate"]]:
        pass

    def __iter__(self) -> Iterator["SigningCertificate"]:
        pass


class AccessKeyPair(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.AccessKeyPair)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeypair)
    """

    access_key_id: str
    status: str
    secret_access_key: str
    create_date: datetime
    user_name: str
    id: str
    secret: str

    def activate(self, Status: statusType) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccessKeyPair.activate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeypairactivate)
        """

    def deactivate(self, Status: statusType) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccessKeyPair.deactivate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeypairdeactivate)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccessKeyPair.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeypairdelete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccessKeyPair.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeypairget-available-subresources)
        """


_AccessKeyPair = AccessKeyPair


class AccountPasswordPolicy(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.AccountPasswordPolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountpasswordpolicy)
    """

    minimum_password_length: int
    require_symbols: bool
    require_numbers: bool
    require_uppercase_characters: bool
    require_lowercase_characters: bool
    allow_users_to_change_password: bool
    expire_passwords: bool
    max_password_age: int
    password_reuse_prevention: int
    hard_expiry: bool

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccountPasswordPolicy.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountpasswordpolicydelete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccountPasswordPolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountpasswordpolicyget-available-subresources)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccountPasswordPolicy.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountpasswordpolicyload)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccountPasswordPolicy.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountpasswordpolicyreload)
        """

    def update(
        self,
        MinimumPasswordLength: int = None,
        RequireSymbols: bool = None,
        RequireNumbers: bool = None,
        RequireUppercaseCharacters: bool = None,
        RequireLowercaseCharacters: bool = None,
        AllowUsersToChangePassword: bool = None,
        MaxPasswordAge: int = None,
        PasswordReusePrevention: int = None,
        HardExpiry: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccountPasswordPolicy.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountpasswordpolicyupdate)
        """


_AccountPasswordPolicy = AccountPasswordPolicy


class AccountSummary(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.AccountSummary)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountsummary)
    """

    summary_map: Dict[str, Any]

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccountSummary.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountsummaryget-available-subresources)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccountSummary.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountsummaryload)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccountSummary.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accountsummaryreload)
        """


_AccountSummary = AccountSummary


class CurrentUser(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.CurrentUser)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#currentuser)
    """

    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    user: "User"
    access_keys: CurrentUserAccessKeysCollection
    mfa_devices: CurrentUserMfaDevicesCollection
    signing_certificates: CurrentUserSigningCertificatesCollection

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.CurrentUser.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#currentuserget-available-subresources)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.CurrentUser.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#currentuserload)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.CurrentUser.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#currentuserreload)
        """


_CurrentUser = CurrentUser


class InstanceProfile(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.InstanceProfile)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#instanceprofile)
    """

    path: str
    instance_profile_name: str
    instance_profile_id: str
    arn: str
    create_date: datetime
    roles_attribute: List[Any]
    tags: List[Any]
    name: str
    roles: "Role"

    def add_role(self, RoleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.InstanceProfile.add_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#instanceprofileadd-role)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.InstanceProfile.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#instanceprofiledelete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.InstanceProfile.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#instanceprofileget-available-subresources)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.InstanceProfile.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#instanceprofileload)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.InstanceProfile.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#instanceprofilereload)
        """

    def remove_role(self, RoleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.InstanceProfile.remove_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#instanceprofileremove-role)
        """


_InstanceProfile = InstanceProfile


class PolicyVersion(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.PolicyVersion)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyversion)
    """

    document: str
    is_default_version: bool
    create_date: datetime
    arn: str
    version_id: str

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.PolicyVersion.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyversiondelete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.PolicyVersion.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyversionget-available-subresources)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.PolicyVersion.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyversionload)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.PolicyVersion.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyversionreload)
        """

    def set_as_default(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.PolicyVersion.set_as_default)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyversionset-as-default)
        """


_PolicyVersion = PolicyVersion


class SamlProvider(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.SamlProvider)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#samlprovider)
    """

    saml_metadata_document: str
    create_date: datetime
    valid_until: datetime
    tags: List[Any]
    arn: str

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.SamlProvider.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#samlproviderdelete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.SamlProvider.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#samlproviderget-available-subresources)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.SamlProvider.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#samlproviderload)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.SamlProvider.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#samlproviderreload)
        """

    def update(self, SAMLMetadataDocument: str) -> UpdateSAMLProviderResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.SamlProvider.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#samlproviderupdate)
        """


_SamlProvider = SamlProvider


class VirtualMfaDevice(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.VirtualMfaDevice)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#virtualmfadevice)
    """

    base32_string_seed: bytes
    qr_code_png: bytes
    user_attribute: Dict[str, Any]
    enable_date: datetime
    tags: List[Any]
    serial_number: str
    user: "User"

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.VirtualMfaDevice.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#virtualmfadevicedelete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.VirtualMfaDevice.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#virtualmfadeviceget-available-subresources)
        """


_VirtualMfaDevice = VirtualMfaDevice


class AccessKey(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.AccessKey)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskey)
    """

    access_key_id: str
    status: str
    create_date: datetime
    user_name: str
    id: str

    def User(self) -> "_User":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccessKey.User)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeyuser)
        """

    def activate(self, Status: statusType) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccessKey.activate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeyactivate)
        """

    def deactivate(self, Status: statusType) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccessKey.deactivate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeydeactivate)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccessKey.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeydelete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AccessKey.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#accesskeyget-available-subresources)
        """


_AccessKey = AccessKey


class AssumeRolePolicy(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.AssumeRolePolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#assumerolepolicy)
    """

    role_name: str

    def Role(self) -> "_Role":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AssumeRolePolicy.Role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#assumerolepolicyrole)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AssumeRolePolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#assumerolepolicyget-available-subresources)
        """

    def update(self, PolicyDocument: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.AssumeRolePolicy.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#assumerolepolicyupdate)
        """


_AssumeRolePolicy = AssumeRolePolicy


class GroupPolicy(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.GroupPolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicy)
    """

    policy_name: str
    policy_document: str
    group_name: str
    name: str

    def Group(self) -> "_Group":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.GroupPolicy.Group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicygroup)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.GroupPolicy.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicydelete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.GroupPolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicyget-available-subresources)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.GroupPolicy.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicyload)
        """

    def put(self, PolicyDocument: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.GroupPolicy.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicyput)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.GroupPolicy.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicyreload)
        """


_GroupPolicy = GroupPolicy


class MfaDevice(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.MfaDevice)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#mfadevice)
    """

    enable_date: datetime
    user_name: str
    serial_number: str

    def User(self) -> "_User":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.MfaDevice.User)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#mfadeviceuser)
        """

    def associate(self, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.MfaDevice.associate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#mfadeviceassociate)
        """

    def disassociate(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.MfaDevice.disassociate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#mfadevicedisassociate)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.MfaDevice.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#mfadeviceget-available-subresources)
        """

    def resync(self, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.MfaDevice.resync)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#mfadeviceresync)
        """


_MfaDevice = MfaDevice


class Policy(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.Policy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policy)
    """

    policy_name: str
    policy_id: str
    path: str
    default_version_id: str
    attachment_count: int
    permissions_boundary_usage_count: int
    is_attachable: bool
    description: str
    create_date: datetime
    update_date: datetime
    tags: List[Any]
    arn: str
    default_version: "PolicyVersion"
    attached_groups: PolicyAttachedGroupsCollection
    attached_roles: PolicyAttachedRolesCollection
    attached_users: PolicyAttachedUsersCollection
    versions: PolicyVersionsCollection

    def attach_group(self, GroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Policy.attach_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyattach-group)
        """

    def attach_role(self, RoleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Policy.attach_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyattach-role)
        """

    def attach_user(self, UserName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Policy.attach_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyattach-user)
        """

    def create_version(self, PolicyDocument: str, SetAsDefault: bool = None) -> _PolicyVersion:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Policy.create_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policycreate-version)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Policy.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policydelete)
        """

    def detach_group(self, GroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Policy.detach_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policydetach-group)
        """

    def detach_role(self, RoleName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Policy.detach_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policydetach-role)
        """

    def detach_user(self, UserName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Policy.detach_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policydetach-user)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Policy.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyget-available-subresources)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Policy.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyload)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Policy.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#policyreload)
        """


_Policy = Policy


class RolePolicy(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.RolePolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicy)
    """

    policy_name: str
    policy_document: str
    role_name: str
    name: str

    def Role(self) -> "_Role":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.RolePolicy.Role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicyrole)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.RolePolicy.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicydelete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.RolePolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicyget-available-subresources)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.RolePolicy.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicyload)
        """

    def put(self, PolicyDocument: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.RolePolicy.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicyput)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.RolePolicy.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicyreload)
        """


_RolePolicy = RolePolicy


class ServerCertificate(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.ServerCertificate)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#servercertificate)
    """

    server_certificate_metadata: Dict[str, Any]
    certificate_body: str
    certificate_chain: str
    tags: List[Any]
    name: str

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServerCertificate.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#servercertificatedelete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServerCertificate.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#servercertificateget-available-subresources)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServerCertificate.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#servercertificateload)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServerCertificate.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#servercertificatereload)
        """

    def update(
        self, NewPath: str = None, NewServerCertificateName: str = None
    ) -> "_ServerCertificate":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServerCertificate.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#servercertificateupdate)
        """


_ServerCertificate = ServerCertificate


class SigningCertificate(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.SigningCertificate)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#signingcertificate)
    """

    certificate_id: str
    certificate_body: str
    status: str
    upload_date: datetime
    user_name: str
    id: str

    def User(self) -> "_User":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.SigningCertificate.User)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#signingcertificateuser)
        """

    def activate(self, Status: statusType) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.SigningCertificate.activate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#signingcertificateactivate)
        """

    def deactivate(self, Status: statusType) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.SigningCertificate.deactivate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#signingcertificatedeactivate)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.SigningCertificate.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#signingcertificatedelete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.SigningCertificate.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#signingcertificateget-available-subresources)
        """


_SigningCertificate = SigningCertificate


class UserPolicy(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.UserPolicy)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicy)
    """

    policy_name: str
    policy_document: str
    user_name: str
    name: str

    def User(self) -> "_User":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.UserPolicy.User)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicyuser)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.UserPolicy.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicydelete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.UserPolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicyget-available-subresources)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.UserPolicy.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicyload)
        """

    def put(self, PolicyDocument: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.UserPolicy.put)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicyput)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.UserPolicy.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicyreload)
        """


_UserPolicy = UserPolicy


class LoginProfile(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.LoginProfile)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofile)
    """

    create_date: datetime
    password_reset_required: bool
    user_name: str

    def User(self) -> "_User":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.LoginProfile.User)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofileuser)
        """

    def create(self, Password: str, PasswordResetRequired: bool = None) -> "_LoginProfile":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.LoginProfile.create)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofilecreate)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.LoginProfile.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofiledelete)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.LoginProfile.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofileget-available-subresources)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.LoginProfile.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofileload)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.LoginProfile.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofilereload)
        """

    def update(self, Password: str = None, PasswordResetRequired: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.LoginProfile.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#loginprofileupdate)
        """


_LoginProfile = LoginProfile


class Role(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.Role)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#role)
    """

    path: str
    role_name: str
    role_id: str
    arn: str
    create_date: datetime
    assume_role_policy_document: str
    description: str
    max_session_duration: int
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    role_last_used: Dict[str, Any]
    name: str
    attached_policies: RoleAttachedPoliciesCollection
    instance_profiles: RoleInstanceProfilesCollection
    policies: RolePoliciesCollection

    def AssumeRolePolicy(self) -> _AssumeRolePolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Role.AssumeRolePolicy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#roleassumerolepolicy)
        """

    def Policy(self, name: str) -> _RolePolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Role.Policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolepolicy)
        """

    def attach_policy(self, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Role.attach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#roleattach-policy)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Role.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#roledelete)
        """

    def detach_policy(self, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Role.detach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#roledetach-policy)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Role.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#roleget-available-subresources)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Role.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#roleload)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Role.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#rolereload)
        """


_Role = Role


class Group(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.Group)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#group)
    """

    path: str
    group_name: str
    group_id: str
    arn: str
    create_date: datetime
    name: str
    attached_policies: GroupAttachedPoliciesCollection
    policies: GroupPoliciesCollection
    users: GroupUsersCollection

    def Policy(self, name: str) -> _GroupPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Group.Policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#grouppolicy)
        """

    def add_user(self, UserName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Group.add_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupadd-user)
        """

    def attach_policy(self, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Group.attach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupattach-policy)
        """

    def create(self, Path: str = None) -> "_Group":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Group.create)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupcreate)
        """

    def create_policy(self, PolicyName: str, PolicyDocument: str) -> _GroupPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Group.create_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupcreate-policy)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Group.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupdelete)
        """

    def detach_policy(self, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Group.detach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupdetach-policy)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Group.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupget-available-subresources)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Group.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupload)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Group.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupreload)
        """

    def remove_user(self, UserName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Group.remove_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupremove-user)
        """

    def update(self, NewPath: str = None, NewGroupName: str = None) -> "_Group":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.Group.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#groupupdate)
        """


_Group = Group


class User(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.User)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#user)
    """

    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    name: str
    access_keys: UserAccessKeysCollection
    attached_policies: UserAttachedPoliciesCollection
    groups: UserGroupsCollection
    mfa_devices: UserMfaDevicesCollection
    policies: UserPoliciesCollection
    signing_certificates: UserSigningCertificatesCollection

    def AccessKey(self, id: str) -> _AccessKey:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.AccessKey)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#useraccesskey)
        """

    def LoginProfile(self) -> _LoginProfile:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.LoginProfile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userloginprofile)
        """

    def MfaDevice(self, serial_number: str) -> _MfaDevice:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.MfaDevice)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#usermfadevice)
        """

    def Policy(self, name: str) -> _UserPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.Policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userpolicy)
        """

    def SigningCertificate(self, id: str) -> _SigningCertificate:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.SigningCertificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#usersigningcertificate)
        """

    def add_group(self, GroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.add_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#useradd-group)
        """

    def attach_policy(self, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.attach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userattach-policy)
        """

    def create(
        self, Path: str = None, PermissionsBoundary: str = None, Tags: List["TagTypeDef"] = None
    ) -> "_User":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.create)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#usercreate)
        """

    def create_access_key_pair(self) -> _AccessKeyPair:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.create_access_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#usercreate-access-key-pair)
        """

    def create_login_profile(
        self, Password: str, PasswordResetRequired: bool = None
    ) -> _LoginProfile:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.create_login_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#usercreate-login-profile)
        """

    def create_policy(self, PolicyName: str, PolicyDocument: str) -> _UserPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.create_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#usercreate-policy)
        """

    def delete(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userdelete)
        """

    def detach_policy(self, PolicyArn: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.detach_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userdetach-policy)
        """

    def enable_mfa(
        self, SerialNumber: str, AuthenticationCode1: str, AuthenticationCode2: str
    ) -> _MfaDevice:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.enable_mfa)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userenable-mfa)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userget-available-subresources)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userload)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userreload)
        """

    def remove_group(self, GroupName: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.remove_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userremove-group)
        """

    def update(self, NewPath: str = None, NewUserName: str = None) -> "_User":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.User.update)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#userupdate)
        """


_User = User


class IAMServiceResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html)
    """

    groups: ServiceResourceGroupsCollection
    instance_profiles: ServiceResourceInstanceProfilesCollection
    policies: ServiceResourcePoliciesCollection
    roles: ServiceResourceRolesCollection
    saml_providers: ServiceResourceSamlProvidersCollection
    server_certificates: ServiceResourceServerCertificatesCollection
    users: ServiceResourceUsersCollection
    virtual_mfa_devices: ServiceResourceVirtualMfaDevicesCollection

    def AccessKey(self, user_name: str, id: str) -> _AccessKey:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.AccessKey)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceaccesskey)
        """

    def AccessKeyPair(self, user_name: str, id: str, secret: str) -> _AccessKeyPair:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.AccessKeyPair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceaccesskeypair)
        """

    def AccountPasswordPolicy(self) -> _AccountPasswordPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.AccountPasswordPolicy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceaccountpasswordpolicy)
        """

    def AccountSummary(self) -> _AccountSummary:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.AccountSummary)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceaccountsummary)
        """

    def AssumeRolePolicy(self, role_name: str) -> _AssumeRolePolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.AssumeRolePolicy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceassumerolepolicy)
        """

    def CurrentUser(self) -> _CurrentUser:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.CurrentUser)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecurrentuser)
        """

    def Group(self, name: str) -> _Group:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.Group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcegroup)
        """

    def GroupPolicy(self, group_name: str, name: str) -> _GroupPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.GroupPolicy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcegrouppolicy)
        """

    def InstanceProfile(self, name: str) -> _InstanceProfile:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.InstanceProfile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceinstanceprofile)
        """

    def LoginProfile(self, user_name: str) -> _LoginProfile:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.LoginProfile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceloginprofile)
        """

    def MfaDevice(self, user_name: str, serial_number: str) -> _MfaDevice:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.MfaDevice)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcemfadevice)
        """

    def Policy(self, policy_arn: str) -> _Policy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.Policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcepolicy)
        """

    def PolicyVersion(self, arn: str, version_id: str) -> _PolicyVersion:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.PolicyVersion)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcepolicyversion)
        """

    def Role(self, name: str) -> _Role:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.Role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcerole)
        """

    def RolePolicy(self, role_name: str, name: str) -> _RolePolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.RolePolicy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcerolepolicy)
        """

    def SamlProvider(self, arn: str) -> _SamlProvider:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.SamlProvider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcesamlprovider)
        """

    def ServerCertificate(self, name: str) -> _ServerCertificate:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.ServerCertificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceservercertificate)
        """

    def SigningCertificate(self, user_name: str, id: str) -> _SigningCertificate:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.SigningCertificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcesigningcertificate)
        """

    def User(self, name: str) -> _User:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.User)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceuser)
        """

    def UserPolicy(self, user_name: str, name: str) -> _UserPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.UserPolicy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceuserpolicy)
        """

    def VirtualMfaDevice(self, serial_number: str) -> _VirtualMfaDevice:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.VirtualMfaDevice)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcevirtualmfadevice)
        """

    def change_password(self, OldPassword: str, NewPassword: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.change_password)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcechange-password)
        """

    def create_account_alias(self, AccountAlias: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.create_account_alias)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-account-alias)
        """

    def create_account_password_policy(
        self,
        MinimumPasswordLength: int = None,
        RequireSymbols: bool = None,
        RequireNumbers: bool = None,
        RequireUppercaseCharacters: bool = None,
        RequireLowercaseCharacters: bool = None,
        AllowUsersToChangePassword: bool = None,
        MaxPasswordAge: int = None,
        PasswordReusePrevention: int = None,
        HardExpiry: bool = None,
    ) -> _AccountPasswordPolicy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.create_account_password_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-account-password-policy)
        """

    def create_group(self, GroupName: str, Path: str = None) -> _Group:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.create_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-group)
        """

    def create_instance_profile(
        self, InstanceProfileName: str, Path: str = None, Tags: List["TagTypeDef"] = None
    ) -> _InstanceProfile:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.create_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-instance-profile)
        """

    def create_policy(
        self,
        PolicyName: str,
        PolicyDocument: str,
        Path: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> _Policy:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.create_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-policy)
        """

    def create_role(
        self,
        RoleName: str,
        AssumeRolePolicyDocument: str,
        Path: str = None,
        Description: str = None,
        MaxSessionDuration: int = None,
        PermissionsBoundary: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> _Role:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.create_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-role)
        """

    def create_saml_provider(
        self, SAMLMetadataDocument: str, Name: str, Tags: List["TagTypeDef"] = None
    ) -> _SamlProvider:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.create_saml_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-saml-provider)
        """

    def create_server_certificate(
        self,
        ServerCertificateName: str,
        CertificateBody: str,
        PrivateKey: str,
        Path: str = None,
        CertificateChain: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> _ServerCertificate:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.create_server_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-server-certificate)
        """

    def create_signing_certificate(
        self, CertificateBody: str, UserName: str = None
    ) -> _SigningCertificate:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.create_signing_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-signing-certificate)
        """

    def create_user(
        self,
        UserName: str,
        Path: str = None,
        PermissionsBoundary: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> _User:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.create_user)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-user)
        """

    def create_virtual_mfa_device(
        self, VirtualMFADeviceName: str, Path: str = None, Tags: List["TagTypeDef"] = None
    ) -> _VirtualMfaDevice:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.create_virtual_mfa_device)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourcecreate-virtual-mfa-device)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/iam.html#IAM.ServiceResource.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource.html#iamserviceresourceget-available-subresources)
        """
