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

__all__ = ['StorageAccountArgs', 'StorageAccount']

@pulumi.input_type
class StorageAccountArgs:
    def __init__(__self__, *,
                 data_policy: pulumi.Input[Union[str, 'DataPolicy']],
                 device_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 storage_account_credential_id: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 storage_account_status: Optional[pulumi.Input[Union[str, 'StorageAccountStatus']]] = None):
        """
        The set of arguments for constructing a StorageAccount resource.
        :param pulumi.Input[Union[str, 'DataPolicy']] data_policy: Data policy of the storage Account.
        :param pulumi.Input[str] device_name: The device name.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] description: Description for the storage Account.
        :param pulumi.Input[str] storage_account_credential_id: Storage Account Credential Id
        :param pulumi.Input[str] storage_account_name: The StorageAccount name.
        :param pulumi.Input[Union[str, 'StorageAccountStatus']] storage_account_status: Current status of the storage account
        """
        pulumi.set(__self__, "data_policy", data_policy)
        pulumi.set(__self__, "device_name", device_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if storage_account_credential_id is not None:
            pulumi.set(__self__, "storage_account_credential_id", storage_account_credential_id)
        if storage_account_name is not None:
            pulumi.set(__self__, "storage_account_name", storage_account_name)
        if storage_account_status is not None:
            pulumi.set(__self__, "storage_account_status", storage_account_status)

    @property
    @pulumi.getter(name="dataPolicy")
    def data_policy(self) -> pulumi.Input[Union[str, 'DataPolicy']]:
        """
        Data policy of the storage Account.
        """
        return pulumi.get(self, "data_policy")

    @data_policy.setter
    def data_policy(self, value: pulumi.Input[Union[str, 'DataPolicy']]):
        pulumi.set(self, "data_policy", value)

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[str]:
        """
        The device name.
        """
        return pulumi.get(self, "device_name")

    @device_name.setter
    def device_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "device_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description for the storage Account.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="storageAccountCredentialId")
    def storage_account_credential_id(self) -> Optional[pulumi.Input[str]]:
        """
        Storage Account Credential Id
        """
        return pulumi.get(self, "storage_account_credential_id")

    @storage_account_credential_id.setter
    def storage_account_credential_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_credential_id", value)

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The StorageAccount name.
        """
        return pulumi.get(self, "storage_account_name")

    @storage_account_name.setter
    def storage_account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_name", value)

    @property
    @pulumi.getter(name="storageAccountStatus")
    def storage_account_status(self) -> Optional[pulumi.Input[Union[str, 'StorageAccountStatus']]]:
        """
        Current status of the storage account
        """
        return pulumi.get(self, "storage_account_status")

    @storage_account_status.setter
    def storage_account_status(self, value: Optional[pulumi.Input[Union[str, 'StorageAccountStatus']]]):
        pulumi.set(self, "storage_account_status", value)


class StorageAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_policy: Optional[pulumi.Input[Union[str, 'DataPolicy']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_credential_id: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 storage_account_status: Optional[pulumi.Input[Union[str, 'StorageAccountStatus']]] = None,
                 __props__=None):
        """
        Represents a Storage Account on the  Data Box Edge/Gateway device.
        API Version: 2020-12-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'DataPolicy']] data_policy: Data policy of the storage Account.
        :param pulumi.Input[str] description: Description for the storage Account.
        :param pulumi.Input[str] device_name: The device name.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] storage_account_credential_id: Storage Account Credential Id
        :param pulumi.Input[str] storage_account_name: The StorageAccount name.
        :param pulumi.Input[Union[str, 'StorageAccountStatus']] storage_account_status: Current status of the storage account
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StorageAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a Storage Account on the  Data Box Edge/Gateway device.
        API Version: 2020-12-01.

        :param str resource_name: The name of the resource.
        :param StorageAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StorageAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_policy: Optional[pulumi.Input[Union[str, 'DataPolicy']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_credential_id: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 storage_account_status: Optional[pulumi.Input[Union[str, 'StorageAccountStatus']]] = None,
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
            __props__ = StorageAccountArgs.__new__(StorageAccountArgs)

            if data_policy is None and not opts.urn:
                raise TypeError("Missing required property 'data_policy'")
            __props__.__dict__["data_policy"] = data_policy
            __props__.__dict__["description"] = description
            if device_name is None and not opts.urn:
                raise TypeError("Missing required property 'device_name'")
            __props__.__dict__["device_name"] = device_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["storage_account_credential_id"] = storage_account_credential_id
            __props__.__dict__["storage_account_name"] = storage_account_name
            __props__.__dict__["storage_account_status"] = storage_account_status
            __props__.__dict__["blob_endpoint"] = None
            __props__.__dict__["container_count"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:databoxedge:StorageAccount"), pulumi.Alias(type_="azure-native:databoxedge/v20190801:StorageAccount"), pulumi.Alias(type_="azure-nextgen:databoxedge/v20190801:StorageAccount"), pulumi.Alias(type_="azure-native:databoxedge/v20200501preview:StorageAccount"), pulumi.Alias(type_="azure-nextgen:databoxedge/v20200501preview:StorageAccount"), pulumi.Alias(type_="azure-native:databoxedge/v20200901:StorageAccount"), pulumi.Alias(type_="azure-nextgen:databoxedge/v20200901:StorageAccount"), pulumi.Alias(type_="azure-native:databoxedge/v20200901preview:StorageAccount"), pulumi.Alias(type_="azure-nextgen:databoxedge/v20200901preview:StorageAccount"), pulumi.Alias(type_="azure-native:databoxedge/v20201201:StorageAccount"), pulumi.Alias(type_="azure-nextgen:databoxedge/v20201201:StorageAccount"), pulumi.Alias(type_="azure-native:databoxedge/v20210201preview:StorageAccount"), pulumi.Alias(type_="azure-nextgen:databoxedge/v20210201preview:StorageAccount")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StorageAccount, __self__).__init__(
            'azure-native:databoxedge:StorageAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StorageAccount':
        """
        Get an existing StorageAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StorageAccountArgs.__new__(StorageAccountArgs)

        __props__.__dict__["blob_endpoint"] = None
        __props__.__dict__["container_count"] = None
        __props__.__dict__["data_policy"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["storage_account_credential_id"] = None
        __props__.__dict__["storage_account_status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return StorageAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="blobEndpoint")
    def blob_endpoint(self) -> pulumi.Output[str]:
        """
        BlobEndpoint of Storage Account
        """
        return pulumi.get(self, "blob_endpoint")

    @property
    @pulumi.getter(name="containerCount")
    def container_count(self) -> pulumi.Output[int]:
        """
        The Container Count. Present only for Storage Accounts with DataPolicy set to Cloud.
        """
        return pulumi.get(self, "container_count")

    @property
    @pulumi.getter(name="dataPolicy")
    def data_policy(self) -> pulumi.Output[str]:
        """
        Data policy of the storage Account.
        """
        return pulumi.get(self, "data_policy")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description for the storage Account.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageAccountCredentialId")
    def storage_account_credential_id(self) -> pulumi.Output[Optional[str]]:
        """
        Storage Account Credential Id
        """
        return pulumi.get(self, "storage_account_credential_id")

    @property
    @pulumi.getter(name="storageAccountStatus")
    def storage_account_status(self) -> pulumi.Output[Optional[str]]:
        """
        Current status of the storage account
        """
        return pulumi.get(self, "storage_account_status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        StorageAccount object on ASE device
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

