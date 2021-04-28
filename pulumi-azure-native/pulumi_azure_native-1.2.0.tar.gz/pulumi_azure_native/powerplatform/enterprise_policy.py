# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['EnterprisePolicyArgs', 'EnterprisePolicy']

@pulumi.input_type
class EnterprisePolicyArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 encryption: Optional[pulumi.Input['PropertiesEncryptionArgs']] = None,
                 enterprise_policy_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['EnterprisePolicyIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 lockbox: Optional[pulumi.Input['PropertiesLockboxArgs']] = None,
                 network_injection: Optional[pulumi.Input['PropertiesNetworkInjectionArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a EnterprisePolicy resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['PropertiesEncryptionArgs'] encryption: The encryption settings for a configuration store.
        :param pulumi.Input[str] enterprise_policy_name: Name of the EnterprisePolicy.
        :param pulumi.Input['EnterprisePolicyIdentityArgs'] identity: The identity of the EnterprisePolicy.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['PropertiesLockboxArgs'] lockbox: Settings concerning lockbox.
        :param pulumi.Input['PropertiesNetworkInjectionArgs'] network_injection: Settings concerning network injection.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if encryption is not None:
            pulumi.set(__self__, "encryption", encryption)
        if enterprise_policy_name is not None:
            pulumi.set(__self__, "enterprise_policy_name", enterprise_policy_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if lockbox is not None:
            pulumi.set(__self__, "lockbox", lockbox)
        if network_injection is not None:
            pulumi.set(__self__, "network_injection", network_injection)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input['PropertiesEncryptionArgs']]:
        """
        The encryption settings for a configuration store.
        """
        return pulumi.get(self, "encryption")

    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input['PropertiesEncryptionArgs']]):
        pulumi.set(self, "encryption", value)

    @property
    @pulumi.getter(name="enterprisePolicyName")
    def enterprise_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the EnterprisePolicy.
        """
        return pulumi.get(self, "enterprise_policy_name")

    @enterprise_policy_name.setter
    def enterprise_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enterprise_policy_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['EnterprisePolicyIdentityArgs']]:
        """
        The identity of the EnterprisePolicy.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['EnterprisePolicyIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def lockbox(self) -> Optional[pulumi.Input['PropertiesLockboxArgs']]:
        """
        Settings concerning lockbox.
        """
        return pulumi.get(self, "lockbox")

    @lockbox.setter
    def lockbox(self, value: Optional[pulumi.Input['PropertiesLockboxArgs']]):
        pulumi.set(self, "lockbox", value)

    @property
    @pulumi.getter(name="networkInjection")
    def network_injection(self) -> Optional[pulumi.Input['PropertiesNetworkInjectionArgs']]:
        """
        Settings concerning network injection.
        """
        return pulumi.get(self, "network_injection")

    @network_injection.setter
    def network_injection(self, value: Optional[pulumi.Input['PropertiesNetworkInjectionArgs']]):
        pulumi.set(self, "network_injection", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class EnterprisePolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encryption: Optional[pulumi.Input[pulumi.InputType['PropertiesEncryptionArgs']]] = None,
                 enterprise_policy_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['EnterprisePolicyIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 lockbox: Optional[pulumi.Input[pulumi.InputType['PropertiesLockboxArgs']]] = None,
                 network_injection: Optional[pulumi.Input[pulumi.InputType['PropertiesNetworkInjectionArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Definition of the EnterprisePolicy.
        API Version: 2020-10-30-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['PropertiesEncryptionArgs']] encryption: The encryption settings for a configuration store.
        :param pulumi.Input[str] enterprise_policy_name: Name of the EnterprisePolicy.
        :param pulumi.Input[pulumi.InputType['EnterprisePolicyIdentityArgs']] identity: The identity of the EnterprisePolicy.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['PropertiesLockboxArgs']] lockbox: Settings concerning lockbox.
        :param pulumi.Input[pulumi.InputType['PropertiesNetworkInjectionArgs']] network_injection: Settings concerning network injection.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnterprisePolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the EnterprisePolicy.
        API Version: 2020-10-30-preview.

        :param str resource_name: The name of the resource.
        :param EnterprisePolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnterprisePolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encryption: Optional[pulumi.Input[pulumi.InputType['PropertiesEncryptionArgs']]] = None,
                 enterprise_policy_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['EnterprisePolicyIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 lockbox: Optional[pulumi.Input[pulumi.InputType['PropertiesLockboxArgs']]] = None,
                 network_injection: Optional[pulumi.Input[pulumi.InputType['PropertiesNetworkInjectionArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = EnterprisePolicyArgs.__new__(EnterprisePolicyArgs)

            __props__.__dict__["encryption"] = encryption
            __props__.__dict__["enterprise_policy_name"] = enterprise_policy_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["lockbox"] = lockbox
            __props__.__dict__["network_injection"] = network_injection
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:powerplatform:EnterprisePolicy"), pulumi.Alias(type_="azure-native:powerplatform/v20201030preview:EnterprisePolicy"), pulumi.Alias(type_="azure-nextgen:powerplatform/v20201030preview:EnterprisePolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(EnterprisePolicy, __self__).__init__(
            'azure-native:powerplatform:EnterprisePolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EnterprisePolicy':
        """
        Get an existing EnterprisePolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EnterprisePolicyArgs.__new__(EnterprisePolicyArgs)

        __props__.__dict__["encryption"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["lockbox"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_injection"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return EnterprisePolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional['outputs.PropertiesResponseEncryption']]:
        """
        The encryption settings for a configuration store.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.EnterprisePolicyIdentityResponse']]:
        """
        The identity of the EnterprisePolicy.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def lockbox(self) -> pulumi.Output[Optional['outputs.PropertiesResponseLockbox']]:
        """
        Settings concerning lockbox.
        """
        return pulumi.get(self, "lockbox")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkInjection")
    def network_injection(self) -> pulumi.Output[Optional['outputs.PropertiesResponseNetworkInjection']]:
        """
        Settings concerning network injection.
        """
        return pulumi.get(self, "network_injection")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

