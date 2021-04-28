# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['WorkspaceSqlAadAdminArgs', 'WorkspaceSqlAadAdmin']

@pulumi.input_type
class WorkspaceSqlAadAdminArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 administrator_type: Optional[pulumi.Input[str]] = None,
                 login: Optional[pulumi.Input[str]] = None,
                 sid: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WorkspaceSqlAadAdmin resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace
        :param pulumi.Input[str] administrator_type: Workspace active directory administrator type
        :param pulumi.Input[str] login: Login of the workspace active directory administrator
        :param pulumi.Input[str] sid: Object ID of the workspace active directory administrator
        :param pulumi.Input[str] tenant_id: Tenant ID of the workspace active directory administrator
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if administrator_type is not None:
            pulumi.set(__self__, "administrator_type", administrator_type)
        if login is not None:
            pulumi.set(__self__, "login", login)
        if sid is not None:
            pulumi.set(__self__, "sid", sid)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

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
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="administratorType")
    def administrator_type(self) -> Optional[pulumi.Input[str]]:
        """
        Workspace active directory administrator type
        """
        return pulumi.get(self, "administrator_type")

    @administrator_type.setter
    def administrator_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "administrator_type", value)

    @property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input[str]]:
        """
        Login of the workspace active directory administrator
        """
        return pulumi.get(self, "login")

    @login.setter
    def login(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "login", value)

    @property
    @pulumi.getter
    def sid(self) -> Optional[pulumi.Input[str]]:
        """
        Object ID of the workspace active directory administrator
        """
        return pulumi.get(self, "sid")

    @sid.setter
    def sid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sid", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        Tenant ID of the workspace active directory administrator
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


class WorkspaceSqlAadAdmin(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_type: Optional[pulumi.Input[str]] = None,
                 login: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sid: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Workspace active directory administrator

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] administrator_type: Workspace active directory administrator type
        :param pulumi.Input[str] login: Login of the workspace active directory administrator
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sid: Object ID of the workspace active directory administrator
        :param pulumi.Input[str] tenant_id: Tenant ID of the workspace active directory administrator
        :param pulumi.Input[str] workspace_name: The name of the workspace
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceSqlAadAdminArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Workspace active directory administrator

        :param str resource_name: The name of the resource.
        :param WorkspaceSqlAadAdminArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceSqlAadAdminArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_type: Optional[pulumi.Input[str]] = None,
                 login: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sid: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = WorkspaceSqlAadAdminArgs.__new__(WorkspaceSqlAadAdminArgs)

            __props__.__dict__["administrator_type"] = administrator_type
            __props__.__dict__["login"] = login
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sid"] = sid
            __props__.__dict__["tenant_id"] = tenant_id
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:synapse/v20190601preview:WorkspaceSqlAadAdmin"), pulumi.Alias(type_="azure-native:synapse:WorkspaceSqlAadAdmin"), pulumi.Alias(type_="azure-nextgen:synapse:WorkspaceSqlAadAdmin"), pulumi.Alias(type_="azure-native:synapse/v20201201:WorkspaceSqlAadAdmin"), pulumi.Alias(type_="azure-nextgen:synapse/v20201201:WorkspaceSqlAadAdmin"), pulumi.Alias(type_="azure-native:synapse/v20210301:WorkspaceSqlAadAdmin"), pulumi.Alias(type_="azure-nextgen:synapse/v20210301:WorkspaceSqlAadAdmin"), pulumi.Alias(type_="azure-native:synapse/v20210401preview:WorkspaceSqlAadAdmin"), pulumi.Alias(type_="azure-nextgen:synapse/v20210401preview:WorkspaceSqlAadAdmin")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkspaceSqlAadAdmin, __self__).__init__(
            'azure-native:synapse/v20190601preview:WorkspaceSqlAadAdmin',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkspaceSqlAadAdmin':
        """
        Get an existing WorkspaceSqlAadAdmin resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceSqlAadAdminArgs.__new__(WorkspaceSqlAadAdminArgs)

        __props__.__dict__["administrator_type"] = None
        __props__.__dict__["login"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["sid"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        return WorkspaceSqlAadAdmin(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administratorType")
    def administrator_type(self) -> pulumi.Output[Optional[str]]:
        """
        Workspace active directory administrator type
        """
        return pulumi.get(self, "administrator_type")

    @property
    @pulumi.getter
    def login(self) -> pulumi.Output[Optional[str]]:
        """
        Login of the workspace active directory administrator
        """
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sid(self) -> pulumi.Output[Optional[str]]:
        """
        Object ID of the workspace active directory administrator
        """
        return pulumi.get(self, "sid")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[str]]:
        """
        Tenant ID of the workspace active directory administrator
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

