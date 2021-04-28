# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['IdentityProviderArgs', 'IdentityProvider']

@pulumi.input_type
class IdentityProviderArgs:
    def __init__(__self__, *,
                 client_id: pulumi.Input[str],
                 client_secret: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 allowed_tenants: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 authority: Optional[pulumi.Input[str]] = None,
                 identity_provider_name: Optional[pulumi.Input[str]] = None,
                 password_reset_policy_name: Optional[pulumi.Input[str]] = None,
                 profile_editing_policy_name: Optional[pulumi.Input[str]] = None,
                 signin_policy_name: Optional[pulumi.Input[str]] = None,
                 signin_tenant: Optional[pulumi.Input[str]] = None,
                 signup_policy_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[Union[str, 'IdentityProviderType']]] = None):
        """
        The set of arguments for constructing a IdentityProvider resource.
        :param pulumi.Input[str] client_id: Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.
        :param pulumi.Input[str] client_secret: Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_tenants: List of Allowed Tenants when configuring Azure Active Directory login.
        :param pulumi.Input[str] authority: OpenID Connect discovery endpoint hostname for AAD or AAD B2C.
        :param pulumi.Input[str] identity_provider_name: Identity Provider Type identifier.
        :param pulumi.Input[str] password_reset_policy_name: Password Reset Policy Name. Only applies to AAD B2C Identity Provider.
        :param pulumi.Input[str] profile_editing_policy_name: Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.
        :param pulumi.Input[str] signin_policy_name: Signin Policy Name. Only applies to AAD B2C Identity Provider.
        :param pulumi.Input[str] signin_tenant: The TenantId to use instead of Common when logging into Active Directory
        :param pulumi.Input[str] signup_policy_name: Signup Policy Name. Only applies to AAD B2C Identity Provider.
        :param pulumi.Input[Union[str, 'IdentityProviderType']] type: Identity Provider Type identifier.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "client_secret", client_secret)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if allowed_tenants is not None:
            pulumi.set(__self__, "allowed_tenants", allowed_tenants)
        if authority is not None:
            pulumi.set(__self__, "authority", authority)
        if identity_provider_name is not None:
            pulumi.set(__self__, "identity_provider_name", identity_provider_name)
        if password_reset_policy_name is not None:
            pulumi.set(__self__, "password_reset_policy_name", password_reset_policy_name)
        if profile_editing_policy_name is not None:
            pulumi.set(__self__, "profile_editing_policy_name", profile_editing_policy_name)
        if signin_policy_name is not None:
            pulumi.set(__self__, "signin_policy_name", signin_policy_name)
        if signin_tenant is not None:
            pulumi.set(__self__, "signin_tenant", signin_tenant)
        if signup_policy_name is not None:
            pulumi.set(__self__, "signup_policy_name", signup_policy_name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[str]:
        """
        Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Input[str]:
        """
        Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value.
        """
        return pulumi.get(self, "client_secret")

    @client_secret.setter
    def client_secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_secret", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="allowedTenants")
    def allowed_tenants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Allowed Tenants when configuring Azure Active Directory login.
        """
        return pulumi.get(self, "allowed_tenants")

    @allowed_tenants.setter
    def allowed_tenants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_tenants", value)

    @property
    @pulumi.getter
    def authority(self) -> Optional[pulumi.Input[str]]:
        """
        OpenID Connect discovery endpoint hostname for AAD or AAD B2C.
        """
        return pulumi.get(self, "authority")

    @authority.setter
    def authority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authority", value)

    @property
    @pulumi.getter(name="identityProviderName")
    def identity_provider_name(self) -> Optional[pulumi.Input[str]]:
        """
        Identity Provider Type identifier.
        """
        return pulumi.get(self, "identity_provider_name")

    @identity_provider_name.setter
    def identity_provider_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_provider_name", value)

    @property
    @pulumi.getter(name="passwordResetPolicyName")
    def password_reset_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        Password Reset Policy Name. Only applies to AAD B2C Identity Provider.
        """
        return pulumi.get(self, "password_reset_policy_name")

    @password_reset_policy_name.setter
    def password_reset_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password_reset_policy_name", value)

    @property
    @pulumi.getter(name="profileEditingPolicyName")
    def profile_editing_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.
        """
        return pulumi.get(self, "profile_editing_policy_name")

    @profile_editing_policy_name.setter
    def profile_editing_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "profile_editing_policy_name", value)

    @property
    @pulumi.getter(name="signinPolicyName")
    def signin_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        Signin Policy Name. Only applies to AAD B2C Identity Provider.
        """
        return pulumi.get(self, "signin_policy_name")

    @signin_policy_name.setter
    def signin_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "signin_policy_name", value)

    @property
    @pulumi.getter(name="signinTenant")
    def signin_tenant(self) -> Optional[pulumi.Input[str]]:
        """
        The TenantId to use instead of Common when logging into Active Directory
        """
        return pulumi.get(self, "signin_tenant")

    @signin_tenant.setter
    def signin_tenant(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "signin_tenant", value)

    @property
    @pulumi.getter(name="signupPolicyName")
    def signup_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        Signup Policy Name. Only applies to AAD B2C Identity Provider.
        """
        return pulumi.get(self, "signup_policy_name")

    @signup_policy_name.setter
    def signup_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "signup_policy_name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'IdentityProviderType']]]:
        """
        Identity Provider Type identifier.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'IdentityProviderType']]]):
        pulumi.set(self, "type", value)


class IdentityProvider(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_tenants: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 authority: Optional[pulumi.Input[str]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 identity_provider_name: Optional[pulumi.Input[str]] = None,
                 password_reset_policy_name: Optional[pulumi.Input[str]] = None,
                 profile_editing_policy_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 signin_policy_name: Optional[pulumi.Input[str]] = None,
                 signin_tenant: Optional[pulumi.Input[str]] = None,
                 signup_policy_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[Union[str, 'IdentityProviderType']]] = None,
                 __props__=None):
        """
        Identity Provider details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_tenants: List of Allowed Tenants when configuring Azure Active Directory login.
        :param pulumi.Input[str] authority: OpenID Connect discovery endpoint hostname for AAD or AAD B2C.
        :param pulumi.Input[str] client_id: Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.
        :param pulumi.Input[str] client_secret: Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value.
        :param pulumi.Input[str] identity_provider_name: Identity Provider Type identifier.
        :param pulumi.Input[str] password_reset_policy_name: Password Reset Policy Name. Only applies to AAD B2C Identity Provider.
        :param pulumi.Input[str] profile_editing_policy_name: Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] signin_policy_name: Signin Policy Name. Only applies to AAD B2C Identity Provider.
        :param pulumi.Input[str] signin_tenant: The TenantId to use instead of Common when logging into Active Directory
        :param pulumi.Input[str] signup_policy_name: Signup Policy Name. Only applies to AAD B2C Identity Provider.
        :param pulumi.Input[Union[str, 'IdentityProviderType']] type: Identity Provider Type identifier.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IdentityProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Identity Provider details.

        :param str resource_name: The name of the resource.
        :param IdentityProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IdentityProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allowed_tenants: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 authority: Optional[pulumi.Input[str]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 identity_provider_name: Optional[pulumi.Input[str]] = None,
                 password_reset_policy_name: Optional[pulumi.Input[str]] = None,
                 profile_editing_policy_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 signin_policy_name: Optional[pulumi.Input[str]] = None,
                 signin_tenant: Optional[pulumi.Input[str]] = None,
                 signup_policy_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[Union[str, 'IdentityProviderType']]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IdentityProviderArgs.__new__(IdentityProviderArgs)

            __props__.__dict__["allowed_tenants"] = allowed_tenants
            __props__.__dict__["authority"] = authority
            if client_id is None and not opts.urn:
                raise TypeError("Missing required property 'client_id'")
            __props__.__dict__["client_id"] = client_id
            if client_secret is None and not opts.urn:
                raise TypeError("Missing required property 'client_secret'")
            __props__.__dict__["client_secret"] = client_secret
            __props__.__dict__["identity_provider_name"] = identity_provider_name
            __props__.__dict__["password_reset_policy_name"] = password_reset_policy_name
            __props__.__dict__["profile_editing_policy_name"] = profile_editing_policy_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["signin_policy_name"] = signin_policy_name
            __props__.__dict__["signin_tenant"] = signin_tenant
            __props__.__dict__["signup_policy_name"] = signup_policy_name
            __props__.__dict__["type"] = type
            __props__.__dict__["name"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:apimanagement/v20201201:IdentityProvider"), pulumi.Alias(type_="azure-native:apimanagement:IdentityProvider"), pulumi.Alias(type_="azure-nextgen:apimanagement:IdentityProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20160707:IdentityProvider"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20160707:IdentityProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20161010:IdentityProvider"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20161010:IdentityProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20170301:IdentityProvider"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20170301:IdentityProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20180101:IdentityProvider"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180101:IdentityProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:IdentityProvider"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180601preview:IdentityProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:IdentityProvider"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20190101:IdentityProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:IdentityProvider"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201:IdentityProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:IdentityProvider"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201preview:IdentityProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:IdentityProvider"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20200601preview:IdentityProvider"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:IdentityProvider"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210101preview:IdentityProvider")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IdentityProvider, __self__).__init__(
            'azure-native:apimanagement/v20201201:IdentityProvider',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IdentityProvider':
        """
        Get an existing IdentityProvider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IdentityProviderArgs.__new__(IdentityProviderArgs)

        __props__.__dict__["allowed_tenants"] = None
        __props__.__dict__["authority"] = None
        __props__.__dict__["client_id"] = None
        __props__.__dict__["client_secret"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["password_reset_policy_name"] = None
        __props__.__dict__["profile_editing_policy_name"] = None
        __props__.__dict__["signin_policy_name"] = None
        __props__.__dict__["signin_tenant"] = None
        __props__.__dict__["signup_policy_name"] = None
        __props__.__dict__["type"] = None
        return IdentityProvider(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowedTenants")
    def allowed_tenants(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of Allowed Tenants when configuring Azure Active Directory login.
        """
        return pulumi.get(self, "allowed_tenants")

    @property
    @pulumi.getter
    def authority(self) -> pulumi.Output[Optional[str]]:
        """
        OpenID Connect discovery endpoint hostname for AAD or AAD B2C.
        """
        return pulumi.get(self, "authority")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[str]:
        """
        Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Output[Optional[str]]:
        """
        Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft. This property will not be filled on 'GET' operations! Use '/listSecrets' POST request to get the value.
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="passwordResetPolicyName")
    def password_reset_policy_name(self) -> pulumi.Output[Optional[str]]:
        """
        Password Reset Policy Name. Only applies to AAD B2C Identity Provider.
        """
        return pulumi.get(self, "password_reset_policy_name")

    @property
    @pulumi.getter(name="profileEditingPolicyName")
    def profile_editing_policy_name(self) -> pulumi.Output[Optional[str]]:
        """
        Profile Editing Policy Name. Only applies to AAD B2C Identity Provider.
        """
        return pulumi.get(self, "profile_editing_policy_name")

    @property
    @pulumi.getter(name="signinPolicyName")
    def signin_policy_name(self) -> pulumi.Output[Optional[str]]:
        """
        Signin Policy Name. Only applies to AAD B2C Identity Provider.
        """
        return pulumi.get(self, "signin_policy_name")

    @property
    @pulumi.getter(name="signinTenant")
    def signin_tenant(self) -> pulumi.Output[Optional[str]]:
        """
        The TenantId to use instead of Common when logging into Active Directory
        """
        return pulumi.get(self, "signin_tenant")

    @property
    @pulumi.getter(name="signupPolicyName")
    def signup_policy_name(self) -> pulumi.Output[Optional[str]]:
        """
        Signup Policy Name. Only applies to AAD B2C Identity Provider.
        """
        return pulumi.get(self, "signup_policy_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

