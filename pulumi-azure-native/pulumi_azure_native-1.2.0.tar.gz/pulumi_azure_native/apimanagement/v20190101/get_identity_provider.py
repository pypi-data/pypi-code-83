# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetIdentityProviderResult',
    'AwaitableGetIdentityProviderResult',
    'get_identity_provider',
]

@pulumi.output_type
class GetIdentityProviderResult:
    """
    Identity Provider details.
    """
    def __init__(__self__, allowed_tenants=None, authority=None, client_id=None, client_secret=None, id=None, name=None, password_reset_policy_name=None, profile_editing_policy_name=None, signin_policy_name=None, signin_tenant=None, signup_policy_name=None, type=None):
        if allowed_tenants and not isinstance(allowed_tenants, list):
            raise TypeError("Expected argument 'allowed_tenants' to be a list")
        pulumi.set(__self__, "allowed_tenants", allowed_tenants)
        if authority and not isinstance(authority, str):
            raise TypeError("Expected argument 'authority' to be a str")
        pulumi.set(__self__, "authority", authority)
        if client_id and not isinstance(client_id, str):
            raise TypeError("Expected argument 'client_id' to be a str")
        pulumi.set(__self__, "client_id", client_id)
        if client_secret and not isinstance(client_secret, str):
            raise TypeError("Expected argument 'client_secret' to be a str")
        pulumi.set(__self__, "client_secret", client_secret)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if password_reset_policy_name and not isinstance(password_reset_policy_name, str):
            raise TypeError("Expected argument 'password_reset_policy_name' to be a str")
        pulumi.set(__self__, "password_reset_policy_name", password_reset_policy_name)
        if profile_editing_policy_name and not isinstance(profile_editing_policy_name, str):
            raise TypeError("Expected argument 'profile_editing_policy_name' to be a str")
        pulumi.set(__self__, "profile_editing_policy_name", profile_editing_policy_name)
        if signin_policy_name and not isinstance(signin_policy_name, str):
            raise TypeError("Expected argument 'signin_policy_name' to be a str")
        pulumi.set(__self__, "signin_policy_name", signin_policy_name)
        if signin_tenant and not isinstance(signin_tenant, str):
            raise TypeError("Expected argument 'signin_tenant' to be a str")
        pulumi.set(__self__, "signin_tenant", signin_tenant)
        if signup_policy_name and not isinstance(signup_policy_name, str):
            raise TypeError("Expected argument 'signup_policy_name' to be a str")
        pulumi.set(__self__, "signup_policy_name", signup_policy_name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="allowedTenants")
    def allowed_tenants(self) -> Optional[Sequence[str]]:
        """
        List of Allowed Tenants when configuring Azure Active Directory login.
        """
        return pulumi.get(self, "allowed_tenants")

    @property
    @pulumi.getter
    def authority(self) -> Optional[str]:
        """
        OpenID Connect discovery endpoint hostname for AAD or AAD B2C.
        """
        return pulumi.get(self, "authority")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> str:
        """
        Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft.
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="passwordResetPolicyName")
    def password_reset_policy_name(self) -> Optional[str]:
        """
        Password Reset Policy Name. Only applies to AAD B2C Identity Provider.
        """
        return pulumi.get(self, "password_reset_policy_name")

    @property
    @pulumi.getter(name="profileEditingPolicyName")
    def profile_editing_policy_name(self) -> Optional[str]:
        """
        Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.
        """
        return pulumi.get(self, "profile_editing_policy_name")

    @property
    @pulumi.getter(name="signinPolicyName")
    def signin_policy_name(self) -> Optional[str]:
        """
        Signin Policy Name. Only applies to AAD B2C Identity Provider.
        """
        return pulumi.get(self, "signin_policy_name")

    @property
    @pulumi.getter(name="signinTenant")
    def signin_tenant(self) -> Optional[str]:
        """
        The TenantId to use instead of Common when logging into Active Directory
        """
        return pulumi.get(self, "signin_tenant")

    @property
    @pulumi.getter(name="signupPolicyName")
    def signup_policy_name(self) -> Optional[str]:
        """
        Signup Policy Name. Only applies to AAD B2C Identity Provider.
        """
        return pulumi.get(self, "signup_policy_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetIdentityProviderResult(GetIdentityProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIdentityProviderResult(
            allowed_tenants=self.allowed_tenants,
            authority=self.authority,
            client_id=self.client_id,
            client_secret=self.client_secret,
            id=self.id,
            name=self.name,
            password_reset_policy_name=self.password_reset_policy_name,
            profile_editing_policy_name=self.profile_editing_policy_name,
            signin_policy_name=self.signin_policy_name,
            signin_tenant=self.signin_tenant,
            signup_policy_name=self.signup_policy_name,
            type=self.type)


def get_identity_provider(identity_provider_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          service_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIdentityProviderResult:
    """
    Identity Provider details.


    :param str identity_provider_name: Identity Provider Type identifier.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['identityProviderName'] = identity_provider_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20190101:getIdentityProvider', __args__, opts=opts, typ=GetIdentityProviderResult).value

    return AwaitableGetIdentityProviderResult(
        allowed_tenants=__ret__.allowed_tenants,
        authority=__ret__.authority,
        client_id=__ret__.client_id,
        client_secret=__ret__.client_secret,
        id=__ret__.id,
        name=__ret__.name,
        password_reset_policy_name=__ret__.password_reset_policy_name,
        profile_editing_policy_name=__ret__.profile_editing_policy_name,
        signin_policy_name=__ret__.signin_policy_name,
        signin_tenant=__ret__.signin_tenant,
        signup_policy_name=__ret__.signup_policy_name,
        type=__ret__.type)
