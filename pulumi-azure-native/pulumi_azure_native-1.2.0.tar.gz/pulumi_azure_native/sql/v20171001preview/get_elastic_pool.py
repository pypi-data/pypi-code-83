# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetElasticPoolResult',
    'AwaitableGetElasticPoolResult',
    'get_elastic_pool',
]

@pulumi.output_type
class GetElasticPoolResult:
    """
    An elastic pool.
    """
    def __init__(__self__, creation_date=None, id=None, kind=None, license_type=None, location=None, max_size_bytes=None, name=None, per_database_settings=None, sku=None, state=None, tags=None, type=None, zone_redundant=None):
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if license_type and not isinstance(license_type, str):
            raise TypeError("Expected argument 'license_type' to be a str")
        pulumi.set(__self__, "license_type", license_type)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if max_size_bytes and not isinstance(max_size_bytes, float):
            raise TypeError("Expected argument 'max_size_bytes' to be a float")
        pulumi.set(__self__, "max_size_bytes", max_size_bytes)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if per_database_settings and not isinstance(per_database_settings, dict):
            raise TypeError("Expected argument 'per_database_settings' to be a dict")
        pulumi.set(__self__, "per_database_settings", per_database_settings)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if zone_redundant and not isinstance(zone_redundant, bool):
            raise TypeError("Expected argument 'zone_redundant' to be a bool")
        pulumi.set(__self__, "zone_redundant", zone_redundant)

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> str:
        """
        The creation date of the elastic pool (ISO8601 format).
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of elastic pool. This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="licenseType")
    def license_type(self) -> Optional[str]:
        """
        The license type to apply for this elastic pool.
        """
        return pulumi.get(self, "license_type")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxSizeBytes")
    def max_size_bytes(self) -> Optional[float]:
        """
        The storage limit for the database elastic pool in bytes.
        """
        return pulumi.get(self, "max_size_bytes")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="perDatabaseSettings")
    def per_database_settings(self) -> Optional['outputs.ElasticPoolPerDatabaseSettingsResponse']:
        """
        The per database settings for the elastic pool.
        """
        return pulumi.get(self, "per_database_settings")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The elastic pool SKU.
        
        The list of SKUs may vary by region and support offer. To determine the SKUs (including the SKU name, tier/edition, family, and capacity) that are available to your subscription in an Azure region, use the `Capabilities_ListByLocation` REST API or the following command:
        
        ```azurecli
        az sql elastic-pool list-editions -l <location> -o table
        ````
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the elastic pool.
        """
        return pulumi.get(self, "state")

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
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="zoneRedundant")
    def zone_redundant(self) -> Optional[bool]:
        """
        Whether or not this elastic pool is zone redundant, which means the replicas of this elastic pool will be spread across multiple availability zones.
        """
        return pulumi.get(self, "zone_redundant")


class AwaitableGetElasticPoolResult(GetElasticPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetElasticPoolResult(
            creation_date=self.creation_date,
            id=self.id,
            kind=self.kind,
            license_type=self.license_type,
            location=self.location,
            max_size_bytes=self.max_size_bytes,
            name=self.name,
            per_database_settings=self.per_database_settings,
            sku=self.sku,
            state=self.state,
            tags=self.tags,
            type=self.type,
            zone_redundant=self.zone_redundant)


def get_elastic_pool(elastic_pool_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     server_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetElasticPoolResult:
    """
    An elastic pool.


    :param str elastic_pool_name: The name of the elastic pool.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['elasticPoolName'] = elastic_pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20171001preview:getElasticPool', __args__, opts=opts, typ=GetElasticPoolResult).value

    return AwaitableGetElasticPoolResult(
        creation_date=__ret__.creation_date,
        id=__ret__.id,
        kind=__ret__.kind,
        license_type=__ret__.license_type,
        location=__ret__.location,
        max_size_bytes=__ret__.max_size_bytes,
        name=__ret__.name,
        per_database_settings=__ret__.per_database_settings,
        sku=__ret__.sku,
        state=__ret__.state,
        tags=__ret__.tags,
        type=__ret__.type,
        zone_redundant=__ret__.zone_redundant)
