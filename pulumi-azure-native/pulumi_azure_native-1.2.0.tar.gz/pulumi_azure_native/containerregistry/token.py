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

__all__ = ['TokenArgs', 'Token']

@pulumi.input_type
class TokenArgs:
    def __init__(__self__, *,
                 registry_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 credentials: Optional[pulumi.Input['TokenCredentialsPropertiesArgs']] = None,
                 scope_map_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'TokenStatus']]] = None,
                 token_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Token resource.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        :param pulumi.Input['TokenCredentialsPropertiesArgs'] credentials: The credentials that can be used for authenticating the token.
        :param pulumi.Input[str] scope_map_id: The resource ID of the scope map to which the token will be associated with.
        :param pulumi.Input[Union[str, 'TokenStatus']] status: The status of the token example enabled or disabled.
        :param pulumi.Input[str] token_name: The name of the token.
        """
        pulumi.set(__self__, "registry_name", registry_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)
        if scope_map_id is not None:
            pulumi.set(__self__, "scope_map_id", scope_map_id)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if token_name is not None:
            pulumi.set(__self__, "token_name", token_name)

    @property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[str]:
        """
        The name of the container registry.
        """
        return pulumi.get(self, "registry_name")

    @registry_name.setter
    def registry_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "registry_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group to which the container registry belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input['TokenCredentialsPropertiesArgs']]:
        """
        The credentials that can be used for authenticating the token.
        """
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input['TokenCredentialsPropertiesArgs']]):
        pulumi.set(self, "credentials", value)

    @property
    @pulumi.getter(name="scopeMapId")
    def scope_map_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the scope map to which the token will be associated with.
        """
        return pulumi.get(self, "scope_map_id")

    @scope_map_id.setter
    def scope_map_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope_map_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'TokenStatus']]]:
        """
        The status of the token example enabled or disabled.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'TokenStatus']]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="tokenName")
    def token_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the token.
        """
        return pulumi.get(self, "token_name")

    @token_name.setter
    def token_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token_name", value)


class Token(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credentials: Optional[pulumi.Input[pulumi.InputType['TokenCredentialsPropertiesArgs']]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope_map_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'TokenStatus']]] = None,
                 token_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An object that represents a token for a container registry.
        API Version: 2020-11-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['TokenCredentialsPropertiesArgs']] credentials: The credentials that can be used for authenticating the token.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        :param pulumi.Input[str] scope_map_id: The resource ID of the scope map to which the token will be associated with.
        :param pulumi.Input[Union[str, 'TokenStatus']] status: The status of the token example enabled or disabled.
        :param pulumi.Input[str] token_name: The name of the token.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TokenArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An object that represents a token for a container registry.
        API Version: 2020-11-01-preview.

        :param str resource_name: The name of the resource.
        :param TokenArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TokenArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credentials: Optional[pulumi.Input[pulumi.InputType['TokenCredentialsPropertiesArgs']]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope_map_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'TokenStatus']]] = None,
                 token_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = TokenArgs.__new__(TokenArgs)

            __props__.__dict__["credentials"] = credentials
            if registry_name is None and not opts.urn:
                raise TypeError("Missing required property 'registry_name'")
            __props__.__dict__["registry_name"] = registry_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["scope_map_id"] = scope_map_id
            __props__.__dict__["status"] = status
            __props__.__dict__["token_name"] = token_name
            __props__.__dict__["creation_date"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:containerregistry:Token"), pulumi.Alias(type_="azure-native:containerregistry/v20190501preview:Token"), pulumi.Alias(type_="azure-nextgen:containerregistry/v20190501preview:Token"), pulumi.Alias(type_="azure-native:containerregistry/v20201101preview:Token"), pulumi.Alias(type_="azure-nextgen:containerregistry/v20201101preview:Token")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Token, __self__).__init__(
            'azure-native:containerregistry:Token',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Token':
        """
        Get an existing Token resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TokenArgs.__new__(TokenArgs)

        __props__.__dict__["creation_date"] = None
        __props__.__dict__["credentials"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["scope_map_id"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Token(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        The creation date of scope map.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional['outputs.TokenCredentialsPropertiesResponse']]:
        """
        The credentials that can be used for authenticating the token.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="scopeMapId")
    def scope_map_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource ID of the scope map to which the token will be associated with.
        """
        return pulumi.get(self, "scope_map_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the token example enabled or disabled.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

