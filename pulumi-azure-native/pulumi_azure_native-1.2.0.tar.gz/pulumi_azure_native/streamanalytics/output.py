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

__all__ = ['OutputArgs', 'Output']

@pulumi.input_type
class OutputArgs:
    def __init__(__self__, *,
                 job_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 datasource: Optional[pulumi.Input[Union['AzureDataLakeStoreOutputDataSourceArgs', 'AzureSqlDatabaseOutputDataSourceArgs', 'AzureTableOutputDataSourceArgs', 'BlobOutputDataSourceArgs', 'DocumentDbOutputDataSourceArgs', 'EventHubOutputDataSourceArgs', 'PowerBIOutputDataSourceArgs', 'ServiceBusQueueOutputDataSourceArgs', 'ServiceBusTopicOutputDataSourceArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 output_name: Optional[pulumi.Input[str]] = None,
                 serialization: Optional[pulumi.Input[Union['AvroSerializationArgs', 'CsvSerializationArgs', 'JsonSerializationArgs']]] = None):
        """
        The set of arguments for constructing a Output resource.
        :param pulumi.Input[str] job_name: The name of the streaming job.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[Union['AzureDataLakeStoreOutputDataSourceArgs', 'AzureSqlDatabaseOutputDataSourceArgs', 'AzureTableOutputDataSourceArgs', 'BlobOutputDataSourceArgs', 'DocumentDbOutputDataSourceArgs', 'EventHubOutputDataSourceArgs', 'PowerBIOutputDataSourceArgs', 'ServiceBusQueueOutputDataSourceArgs', 'ServiceBusTopicOutputDataSourceArgs']] datasource: Describes the data source that output will be written to. Required on PUT (CreateOrReplace) requests.
        :param pulumi.Input[str] name: Resource name
        :param pulumi.Input[str] output_name: The name of the output.
        :param pulumi.Input[Union['AvroSerializationArgs', 'CsvSerializationArgs', 'JsonSerializationArgs']] serialization: Describes how data from an input is serialized or how data is serialized when written to an output. Required on PUT (CreateOrReplace) requests.
        """
        pulumi.set(__self__, "job_name", job_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if datasource is not None:
            pulumi.set(__self__, "datasource", datasource)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if output_name is not None:
            pulumi.set(__self__, "output_name", output_name)
        if serialization is not None:
            pulumi.set(__self__, "serialization", serialization)

    @property
    @pulumi.getter(name="jobName")
    def job_name(self) -> pulumi.Input[str]:
        """
        The name of the streaming job.
        """
        return pulumi.get(self, "job_name")

    @job_name.setter
    def job_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "job_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def datasource(self) -> Optional[pulumi.Input[Union['AzureDataLakeStoreOutputDataSourceArgs', 'AzureSqlDatabaseOutputDataSourceArgs', 'AzureTableOutputDataSourceArgs', 'BlobOutputDataSourceArgs', 'DocumentDbOutputDataSourceArgs', 'EventHubOutputDataSourceArgs', 'PowerBIOutputDataSourceArgs', 'ServiceBusQueueOutputDataSourceArgs', 'ServiceBusTopicOutputDataSourceArgs']]]:
        """
        Describes the data source that output will be written to. Required on PUT (CreateOrReplace) requests.
        """
        return pulumi.get(self, "datasource")

    @datasource.setter
    def datasource(self, value: Optional[pulumi.Input[Union['AzureDataLakeStoreOutputDataSourceArgs', 'AzureSqlDatabaseOutputDataSourceArgs', 'AzureTableOutputDataSourceArgs', 'BlobOutputDataSourceArgs', 'DocumentDbOutputDataSourceArgs', 'EventHubOutputDataSourceArgs', 'PowerBIOutputDataSourceArgs', 'ServiceBusQueueOutputDataSourceArgs', 'ServiceBusTopicOutputDataSourceArgs']]]):
        pulumi.set(self, "datasource", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="outputName")
    def output_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the output.
        """
        return pulumi.get(self, "output_name")

    @output_name.setter
    def output_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "output_name", value)

    @property
    @pulumi.getter
    def serialization(self) -> Optional[pulumi.Input[Union['AvroSerializationArgs', 'CsvSerializationArgs', 'JsonSerializationArgs']]]:
        """
        Describes how data from an input is serialized or how data is serialized when written to an output. Required on PUT (CreateOrReplace) requests.
        """
        return pulumi.get(self, "serialization")

    @serialization.setter
    def serialization(self, value: Optional[pulumi.Input[Union['AvroSerializationArgs', 'CsvSerializationArgs', 'JsonSerializationArgs']]]):
        pulumi.set(self, "serialization", value)


class Output(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datasource: Optional[pulumi.Input[Union[pulumi.InputType['AzureDataLakeStoreOutputDataSourceArgs'], pulumi.InputType['AzureSqlDatabaseOutputDataSourceArgs'], pulumi.InputType['AzureTableOutputDataSourceArgs'], pulumi.InputType['BlobOutputDataSourceArgs'], pulumi.InputType['DocumentDbOutputDataSourceArgs'], pulumi.InputType['EventHubOutputDataSourceArgs'], pulumi.InputType['PowerBIOutputDataSourceArgs'], pulumi.InputType['ServiceBusQueueOutputDataSourceArgs'], pulumi.InputType['ServiceBusTopicOutputDataSourceArgs']]]] = None,
                 job_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 output_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 serialization: Optional[pulumi.Input[Union[pulumi.InputType['AvroSerializationArgs'], pulumi.InputType['CsvSerializationArgs'], pulumi.InputType['JsonSerializationArgs']]]] = None,
                 __props__=None):
        """
        An output object, containing all information associated with the named output. All outputs are contained under a streaming job.
        API Version: 2016-03-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[pulumi.InputType['AzureDataLakeStoreOutputDataSourceArgs'], pulumi.InputType['AzureSqlDatabaseOutputDataSourceArgs'], pulumi.InputType['AzureTableOutputDataSourceArgs'], pulumi.InputType['BlobOutputDataSourceArgs'], pulumi.InputType['DocumentDbOutputDataSourceArgs'], pulumi.InputType['EventHubOutputDataSourceArgs'], pulumi.InputType['PowerBIOutputDataSourceArgs'], pulumi.InputType['ServiceBusQueueOutputDataSourceArgs'], pulumi.InputType['ServiceBusTopicOutputDataSourceArgs']]] datasource: Describes the data source that output will be written to. Required on PUT (CreateOrReplace) requests.
        :param pulumi.Input[str] job_name: The name of the streaming job.
        :param pulumi.Input[str] name: Resource name
        :param pulumi.Input[str] output_name: The name of the output.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[Union[pulumi.InputType['AvroSerializationArgs'], pulumi.InputType['CsvSerializationArgs'], pulumi.InputType['JsonSerializationArgs']]] serialization: Describes how data from an input is serialized or how data is serialized when written to an output. Required on PUT (CreateOrReplace) requests.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OutputArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An output object, containing all information associated with the named output. All outputs are contained under a streaming job.
        API Version: 2016-03-01.

        :param str resource_name: The name of the resource.
        :param OutputArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OutputArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datasource: Optional[pulumi.Input[Union[pulumi.InputType['AzureDataLakeStoreOutputDataSourceArgs'], pulumi.InputType['AzureSqlDatabaseOutputDataSourceArgs'], pulumi.InputType['AzureTableOutputDataSourceArgs'], pulumi.InputType['BlobOutputDataSourceArgs'], pulumi.InputType['DocumentDbOutputDataSourceArgs'], pulumi.InputType['EventHubOutputDataSourceArgs'], pulumi.InputType['PowerBIOutputDataSourceArgs'], pulumi.InputType['ServiceBusQueueOutputDataSourceArgs'], pulumi.InputType['ServiceBusTopicOutputDataSourceArgs']]]] = None,
                 job_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 output_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 serialization: Optional[pulumi.Input[Union[pulumi.InputType['AvroSerializationArgs'], pulumi.InputType['CsvSerializationArgs'], pulumi.InputType['JsonSerializationArgs']]]] = None,
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
            __props__ = OutputArgs.__new__(OutputArgs)

            __props__.__dict__["datasource"] = datasource
            if job_name is None and not opts.urn:
                raise TypeError("Missing required property 'job_name'")
            __props__.__dict__["job_name"] = job_name
            __props__.__dict__["name"] = name
            __props__.__dict__["output_name"] = output_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["serialization"] = serialization
            __props__.__dict__["diagnostics"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:streamanalytics:Output"), pulumi.Alias(type_="azure-native:streamanalytics/v20160301:Output"), pulumi.Alias(type_="azure-nextgen:streamanalytics/v20160301:Output"), pulumi.Alias(type_="azure-native:streamanalytics/v20170401preview:Output"), pulumi.Alias(type_="azure-nextgen:streamanalytics/v20170401preview:Output")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Output, __self__).__init__(
            'azure-native:streamanalytics:Output',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Output':
        """
        Get an existing Output resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OutputArgs.__new__(OutputArgs)

        __props__.__dict__["datasource"] = None
        __props__.__dict__["diagnostics"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["serialization"] = None
        __props__.__dict__["type"] = None
        return Output(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def datasource(self) -> pulumi.Output[Optional[Any]]:
        """
        Describes the data source that output will be written to. Required on PUT (CreateOrReplace) requests.
        """
        return pulumi.get(self, "datasource")

    @property
    @pulumi.getter
    def diagnostics(self) -> pulumi.Output['outputs.DiagnosticsResponse']:
        """
        Describes conditions applicable to the Input, Output, or the job overall, that warrant customer attention.
        """
        return pulumi.get(self, "diagnostics")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        The current entity tag for the output. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def serialization(self) -> pulumi.Output[Optional[Any]]:
        """
        Describes how data from an input is serialized or how data is serialized when written to an output. Required on PUT (CreateOrReplace) requests.
        """
        return pulumi.get(self, "serialization")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

