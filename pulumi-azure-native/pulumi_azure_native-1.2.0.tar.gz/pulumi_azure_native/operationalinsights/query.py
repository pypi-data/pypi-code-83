# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['QueryArgs', 'Query']

@pulumi.input_type
class QueryArgs:
    def __init__(__self__, *,
                 body: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 query_pack_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 properties: Optional[Any] = None,
                 related: Optional[pulumi.Input['LogAnalyticsQueryPackQueryPropertiesRelatedArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None):
        """
        The set of arguments for constructing a Query resource.
        :param pulumi.Input[str] body: Body of the query.
        :param pulumi.Input[str] display_name: Unique display name for your query within the Query Pack.
        :param pulumi.Input[str] query_pack_name: The name of the Log Analytics QueryPack resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] description: Description of the query.
        :param pulumi.Input[str] id: The id of a specific query defined in the Log Analytics QueryPack
        :param Any properties: Additional properties that can be set for the query.
        :param pulumi.Input['LogAnalyticsQueryPackQueryPropertiesRelatedArgs'] related: The related metadata items for the function.
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]] tags: Tags associated with the query.
        """
        pulumi.set(__self__, "body", body)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "query_pack_name", query_pack_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if related is not None:
            pulumi.set(__self__, "related", related)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Input[str]:
        """
        Body of the query.
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: pulumi.Input[str]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        Unique display name for your query within the Query Pack.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="queryPackName")
    def query_pack_name(self) -> pulumi.Input[str]:
        """
        The name of the Log Analytics QueryPack resource.
        """
        return pulumi.get(self, "query_pack_name")

    @query_pack_name.setter
    def query_pack_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "query_pack_name", value)

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
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the query.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of a specific query defined in the Log Analytics QueryPack
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[Any]:
        """
        Additional properties that can be set for the query.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[Any]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def related(self) -> Optional[pulumi.Input['LogAnalyticsQueryPackQueryPropertiesRelatedArgs']]:
        """
        The related metadata items for the function.
        """
        return pulumi.get(self, "related")

    @related.setter
    def related(self, value: Optional[pulumi.Input['LogAnalyticsQueryPackQueryPropertiesRelatedArgs']]):
        pulumi.set(self, "related", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]]:
        """
        Tags associated with the query.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]]):
        pulumi.set(self, "tags", value)


class Query(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 properties: Optional[Any] = None,
                 query_pack_name: Optional[pulumi.Input[str]] = None,
                 related: Optional[pulumi.Input[pulumi.InputType['LogAnalyticsQueryPackQueryPropertiesRelatedArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
                 __props__=None):
        """
        A Log Analytics QueryPack-Query definition.
        API Version: 2019-09-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: Body of the query.
        :param pulumi.Input[str] description: Description of the query.
        :param pulumi.Input[str] display_name: Unique display name for your query within the Query Pack.
        :param pulumi.Input[str] id: The id of a specific query defined in the Log Analytics QueryPack
        :param Any properties: Additional properties that can be set for the query.
        :param pulumi.Input[str] query_pack_name: The name of the Log Analytics QueryPack resource.
        :param pulumi.Input[pulumi.InputType['LogAnalyticsQueryPackQueryPropertiesRelatedArgs']] related: The related metadata items for the function.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]] tags: Tags associated with the query.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: QueryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Log Analytics QueryPack-Query definition.
        API Version: 2019-09-01-preview.

        :param str resource_name: The name of the resource.
        :param QueryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(QueryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 properties: Optional[Any] = None,
                 query_pack_name: Optional[pulumi.Input[str]] = None,
                 related: Optional[pulumi.Input[pulumi.InputType['LogAnalyticsQueryPackQueryPropertiesRelatedArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[Sequence[pulumi.Input[str]]]]]] = None,
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
            __props__ = QueryArgs.__new__(QueryArgs)

            if body is None and not opts.urn:
                raise TypeError("Missing required property 'body'")
            __props__.__dict__["body"] = body
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["id"] = id
            __props__.__dict__["properties"] = properties
            if query_pack_name is None and not opts.urn:
                raise TypeError("Missing required property 'query_pack_name'")
            __props__.__dict__["query_pack_name"] = query_pack_name
            __props__.__dict__["related"] = related
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["author"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["time_created"] = None
            __props__.__dict__["time_modified"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:operationalinsights:Query"), pulumi.Alias(type_="azure-native:operationalinsights/v20190901preview:Query"), pulumi.Alias(type_="azure-nextgen:operationalinsights/v20190901preview:Query")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Query, __self__).__init__(
            'azure-native:operationalinsights:Query',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Query':
        """
        Get an existing Query resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = QueryArgs.__new__(QueryArgs)

        __props__.__dict__["author"] = None
        __props__.__dict__["body"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["related"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["time_created"] = None
        __props__.__dict__["time_modified"] = None
        __props__.__dict__["type"] = None
        return Query(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def author(self) -> pulumi.Output[str]:
        """
        Object Id of user creating the query.
        """
        return pulumi.get(self, "author")

    @property
    @pulumi.getter
    def body(self) -> pulumi.Output[str]:
        """
        Body of the query.
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the query.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Unique display name for your query within the Query Pack.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        """
        Additional properties that can be set for the query.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def related(self) -> pulumi.Output[Optional['outputs.LogAnalyticsQueryPackQueryPropertiesResponseRelated']]:
        """
        The related metadata items for the function.
        """
        return pulumi.get(self, "related")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Sequence[str]]]]:
        """
        Tags associated with the query.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> pulumi.Output[str]:
        """
        Creation Date for the Log Analytics Query, in ISO 8601 format.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> pulumi.Output[str]:
        """
        Last modified date of the Log Analytics Query, in ISO 8601 format.
        """
        return pulumi.get(self, "time_modified")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

