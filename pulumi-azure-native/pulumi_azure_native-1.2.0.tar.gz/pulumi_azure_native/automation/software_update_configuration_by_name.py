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

__all__ = ['SoftwareUpdateConfigurationByNameArgs', 'SoftwareUpdateConfigurationByName']

@pulumi.input_type
class SoftwareUpdateConfigurationByNameArgs:
    def __init__(__self__, *,
                 automation_account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 schedule_info: pulumi.Input['SUCSchedulePropertiesArgs'],
                 update_configuration: pulumi.Input['UpdateConfigurationArgs'],
                 error: Optional[pulumi.Input['ErrorResponseArgs']] = None,
                 software_update_configuration_name: Optional[pulumi.Input[str]] = None,
                 tasks: Optional[pulumi.Input['SoftwareUpdateConfigurationTasksArgs']] = None):
        """
        The set of arguments for constructing a SoftwareUpdateConfigurationByName resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input['SUCSchedulePropertiesArgs'] schedule_info: Schedule information for the Software update configuration
        :param pulumi.Input['UpdateConfigurationArgs'] update_configuration: update specific properties for the Software update configuration
        :param pulumi.Input['ErrorResponseArgs'] error: Details of provisioning error
        :param pulumi.Input[str] software_update_configuration_name: The name of the software update configuration to be created.
        :param pulumi.Input['SoftwareUpdateConfigurationTasksArgs'] tasks: Tasks information for the Software update configuration.
        """
        pulumi.set(__self__, "automation_account_name", automation_account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "schedule_info", schedule_info)
        pulumi.set(__self__, "update_configuration", update_configuration)
        if error is not None:
            pulumi.set(__self__, "error", error)
        if software_update_configuration_name is not None:
            pulumi.set(__self__, "software_update_configuration_name", software_update_configuration_name)
        if tasks is not None:
            pulumi.set(__self__, "tasks", tasks)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[str]:
        """
        The name of the automation account.
        """
        return pulumi.get(self, "automation_account_name")

    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "automation_account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of an Azure Resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="scheduleInfo")
    def schedule_info(self) -> pulumi.Input['SUCSchedulePropertiesArgs']:
        """
        Schedule information for the Software update configuration
        """
        return pulumi.get(self, "schedule_info")

    @schedule_info.setter
    def schedule_info(self, value: pulumi.Input['SUCSchedulePropertiesArgs']):
        pulumi.set(self, "schedule_info", value)

    @property
    @pulumi.getter(name="updateConfiguration")
    def update_configuration(self) -> pulumi.Input['UpdateConfigurationArgs']:
        """
        update specific properties for the Software update configuration
        """
        return pulumi.get(self, "update_configuration")

    @update_configuration.setter
    def update_configuration(self, value: pulumi.Input['UpdateConfigurationArgs']):
        pulumi.set(self, "update_configuration", value)

    @property
    @pulumi.getter
    def error(self) -> Optional[pulumi.Input['ErrorResponseArgs']]:
        """
        Details of provisioning error
        """
        return pulumi.get(self, "error")

    @error.setter
    def error(self, value: Optional[pulumi.Input['ErrorResponseArgs']]):
        pulumi.set(self, "error", value)

    @property
    @pulumi.getter(name="softwareUpdateConfigurationName")
    def software_update_configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the software update configuration to be created.
        """
        return pulumi.get(self, "software_update_configuration_name")

    @software_update_configuration_name.setter
    def software_update_configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "software_update_configuration_name", value)

    @property
    @pulumi.getter
    def tasks(self) -> Optional[pulumi.Input['SoftwareUpdateConfigurationTasksArgs']]:
        """
        Tasks information for the Software update configuration.
        """
        return pulumi.get(self, "tasks")

    @tasks.setter
    def tasks(self, value: Optional[pulumi.Input['SoftwareUpdateConfigurationTasksArgs']]):
        pulumi.set(self, "tasks", value)


class SoftwareUpdateConfigurationByName(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 error: Optional[pulumi.Input[pulumi.InputType['ErrorResponseArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schedule_info: Optional[pulumi.Input[pulumi.InputType['SUCSchedulePropertiesArgs']]] = None,
                 software_update_configuration_name: Optional[pulumi.Input[str]] = None,
                 tasks: Optional[pulumi.Input[pulumi.InputType['SoftwareUpdateConfigurationTasksArgs']]] = None,
                 update_configuration: Optional[pulumi.Input[pulumi.InputType['UpdateConfigurationArgs']]] = None,
                 __props__=None):
        """
        Software update configuration properties.
        API Version: 2019-06-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[pulumi.InputType['ErrorResponseArgs']] error: Details of provisioning error
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[pulumi.InputType['SUCSchedulePropertiesArgs']] schedule_info: Schedule information for the Software update configuration
        :param pulumi.Input[str] software_update_configuration_name: The name of the software update configuration to be created.
        :param pulumi.Input[pulumi.InputType['SoftwareUpdateConfigurationTasksArgs']] tasks: Tasks information for the Software update configuration.
        :param pulumi.Input[pulumi.InputType['UpdateConfigurationArgs']] update_configuration: update specific properties for the Software update configuration
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SoftwareUpdateConfigurationByNameArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Software update configuration properties.
        API Version: 2019-06-01.

        :param str resource_name: The name of the resource.
        :param SoftwareUpdateConfigurationByNameArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SoftwareUpdateConfigurationByNameArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 error: Optional[pulumi.Input[pulumi.InputType['ErrorResponseArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schedule_info: Optional[pulumi.Input[pulumi.InputType['SUCSchedulePropertiesArgs']]] = None,
                 software_update_configuration_name: Optional[pulumi.Input[str]] = None,
                 tasks: Optional[pulumi.Input[pulumi.InputType['SoftwareUpdateConfigurationTasksArgs']]] = None,
                 update_configuration: Optional[pulumi.Input[pulumi.InputType['UpdateConfigurationArgs']]] = None,
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
            __props__ = SoftwareUpdateConfigurationByNameArgs.__new__(SoftwareUpdateConfigurationByNameArgs)

            if automation_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__.__dict__["automation_account_name"] = automation_account_name
            __props__.__dict__["error"] = error
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if schedule_info is None and not opts.urn:
                raise TypeError("Missing required property 'schedule_info'")
            __props__.__dict__["schedule_info"] = schedule_info
            __props__.__dict__["software_update_configuration_name"] = software_update_configuration_name
            __props__.__dict__["tasks"] = tasks
            if update_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'update_configuration'")
            __props__.__dict__["update_configuration"] = update_configuration
            __props__.__dict__["created_by"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["last_modified_by"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:automation:SoftwareUpdateConfigurationByName"), pulumi.Alias(type_="azure-native:automation/v20170515preview:SoftwareUpdateConfigurationByName"), pulumi.Alias(type_="azure-nextgen:automation/v20170515preview:SoftwareUpdateConfigurationByName"), pulumi.Alias(type_="azure-native:automation/v20190601:SoftwareUpdateConfigurationByName"), pulumi.Alias(type_="azure-nextgen:automation/v20190601:SoftwareUpdateConfigurationByName")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SoftwareUpdateConfigurationByName, __self__).__init__(
            'azure-native:automation:SoftwareUpdateConfigurationByName',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SoftwareUpdateConfigurationByName':
        """
        Get an existing SoftwareUpdateConfigurationByName resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SoftwareUpdateConfigurationByNameArgs.__new__(SoftwareUpdateConfigurationByNameArgs)

        __props__.__dict__["created_by"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["error"] = None
        __props__.__dict__["last_modified_by"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["schedule_info"] = None
        __props__.__dict__["tasks"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["update_configuration"] = None
        return SoftwareUpdateConfigurationByName(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        """
        CreatedBy property, which only appears in the response.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        Creation time of the resource, which only appears in the response.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def error(self) -> pulumi.Output[Optional['outputs.ErrorResponseResponse']]:
        """
        Details of provisioning error
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> pulumi.Output[str]:
        """
        LastModifiedBy property, which only appears in the response.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[str]:
        """
        Last time resource was modified, which only appears in the response.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state for the software update configuration, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="scheduleInfo")
    def schedule_info(self) -> pulumi.Output['outputs.SUCSchedulePropertiesResponse']:
        """
        Schedule information for the Software update configuration
        """
        return pulumi.get(self, "schedule_info")

    @property
    @pulumi.getter
    def tasks(self) -> pulumi.Output[Optional['outputs.SoftwareUpdateConfigurationTasksResponse']]:
        """
        Tasks information for the Software update configuration.
        """
        return pulumi.get(self, "tasks")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updateConfiguration")
    def update_configuration(self) -> pulumi.Output['outputs.UpdateConfigurationResponse']:
        """
        update specific properties for the Software update configuration
        """
        return pulumi.get(self, "update_configuration")

