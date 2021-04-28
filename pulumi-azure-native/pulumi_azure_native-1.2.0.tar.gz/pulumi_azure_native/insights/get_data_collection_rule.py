# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetDataCollectionRuleResult',
    'AwaitableGetDataCollectionRuleResult',
    'get_data_collection_rule',
]

@pulumi.output_type
class GetDataCollectionRuleResult:
    """
    Definition of ARM tracked top level resource.
    """
    def __init__(__self__, data_flows=None, data_sources=None, description=None, destinations=None, etag=None, id=None, immutable_id=None, kind=None, location=None, name=None, provisioning_state=None, tags=None, type=None):
        if data_flows and not isinstance(data_flows, list):
            raise TypeError("Expected argument 'data_flows' to be a list")
        pulumi.set(__self__, "data_flows", data_flows)
        if data_sources and not isinstance(data_sources, dict):
            raise TypeError("Expected argument 'data_sources' to be a dict")
        pulumi.set(__self__, "data_sources", data_sources)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if destinations and not isinstance(destinations, dict):
            raise TypeError("Expected argument 'destinations' to be a dict")
        pulumi.set(__self__, "destinations", destinations)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if immutable_id and not isinstance(immutable_id, str):
            raise TypeError("Expected argument 'immutable_id' to be a str")
        pulumi.set(__self__, "immutable_id", immutable_id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="dataFlows")
    def data_flows(self) -> Optional[Sequence['outputs.DataFlowResponse']]:
        """
        The specification of data flows.
        """
        return pulumi.get(self, "data_flows")

    @property
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> Optional['outputs.DataCollectionRuleResponseDataSources']:
        """
        The specification of data sources. 
        This property is optional and can be omitted if the rule is meant to be used via direct calls to the provisioned endpoint.
        """
        return pulumi.get(self, "data_sources")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the data collection rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def destinations(self) -> Optional['outputs.DataCollectionRuleResponseDestinations']:
        """
        The specification of destinations.
        """
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Resource entity tag (ETag).
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified ID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="immutableId")
    def immutable_id(self) -> str:
        """
        The immutable ID of this data collection rule. This property is READ-ONLY.
        """
        return pulumi.get(self, "immutable_id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        The kind of the resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The resource provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetDataCollectionRuleResult(GetDataCollectionRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDataCollectionRuleResult(
            data_flows=self.data_flows,
            data_sources=self.data_sources,
            description=self.description,
            destinations=self.destinations,
            etag=self.etag,
            id=self.id,
            immutable_id=self.immutable_id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            tags=self.tags,
            type=self.type)


def get_data_collection_rule(data_collection_rule_name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDataCollectionRuleResult:
    """
    Definition of ARM tracked top level resource.
    API Version: 2019-11-01-preview.


    :param str data_collection_rule_name: The name of the data collection rule. The name is case insensitive.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['dataCollectionRuleName'] = data_collection_rule_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:insights:getDataCollectionRule', __args__, opts=opts, typ=GetDataCollectionRuleResult).value

    return AwaitableGetDataCollectionRuleResult(
        data_flows=__ret__.data_flows,
        data_sources=__ret__.data_sources,
        description=__ret__.description,
        destinations=__ret__.destinations,
        etag=__ret__.etag,
        id=__ret__.id,
        immutable_id=__ret__.immutable_id,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        tags=__ret__.tags,
        type=__ret__.type)
