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
    'GetProfileResult',
    'AwaitableGetProfileResult',
    'get_profile',
]

@pulumi.output_type
class GetProfileResult:
    """
    The profile resource format.
    """
    def __init__(__self__, api_entity_set_name=None, attributes=None, description=None, display_name=None, entity_type=None, fields=None, id=None, instances_count=None, large_image=None, last_changed_utc=None, localized_attributes=None, medium_image=None, name=None, provisioning_state=None, schema_item_type_link=None, small_image=None, strong_ids=None, tenant_id=None, timestamp_field_name=None, type=None, type_name=None):
        if api_entity_set_name and not isinstance(api_entity_set_name, str):
            raise TypeError("Expected argument 'api_entity_set_name' to be a str")
        pulumi.set(__self__, "api_entity_set_name", api_entity_set_name)
        if attributes and not isinstance(attributes, dict):
            raise TypeError("Expected argument 'attributes' to be a dict")
        pulumi.set(__self__, "attributes", attributes)
        if description and not isinstance(description, dict):
            raise TypeError("Expected argument 'description' to be a dict")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, dict):
            raise TypeError("Expected argument 'display_name' to be a dict")
        pulumi.set(__self__, "display_name", display_name)
        if entity_type and not isinstance(entity_type, str):
            raise TypeError("Expected argument 'entity_type' to be a str")
        pulumi.set(__self__, "entity_type", entity_type)
        if fields and not isinstance(fields, list):
            raise TypeError("Expected argument 'fields' to be a list")
        pulumi.set(__self__, "fields", fields)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instances_count and not isinstance(instances_count, int):
            raise TypeError("Expected argument 'instances_count' to be a int")
        pulumi.set(__self__, "instances_count", instances_count)
        if large_image and not isinstance(large_image, str):
            raise TypeError("Expected argument 'large_image' to be a str")
        pulumi.set(__self__, "large_image", large_image)
        if last_changed_utc and not isinstance(last_changed_utc, str):
            raise TypeError("Expected argument 'last_changed_utc' to be a str")
        pulumi.set(__self__, "last_changed_utc", last_changed_utc)
        if localized_attributes and not isinstance(localized_attributes, dict):
            raise TypeError("Expected argument 'localized_attributes' to be a dict")
        pulumi.set(__self__, "localized_attributes", localized_attributes)
        if medium_image and not isinstance(medium_image, str):
            raise TypeError("Expected argument 'medium_image' to be a str")
        pulumi.set(__self__, "medium_image", medium_image)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if schema_item_type_link and not isinstance(schema_item_type_link, str):
            raise TypeError("Expected argument 'schema_item_type_link' to be a str")
        pulumi.set(__self__, "schema_item_type_link", schema_item_type_link)
        if small_image and not isinstance(small_image, str):
            raise TypeError("Expected argument 'small_image' to be a str")
        pulumi.set(__self__, "small_image", small_image)
        if strong_ids and not isinstance(strong_ids, list):
            raise TypeError("Expected argument 'strong_ids' to be a list")
        pulumi.set(__self__, "strong_ids", strong_ids)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if timestamp_field_name and not isinstance(timestamp_field_name, str):
            raise TypeError("Expected argument 'timestamp_field_name' to be a str")
        pulumi.set(__self__, "timestamp_field_name", timestamp_field_name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if type_name and not isinstance(type_name, str):
            raise TypeError("Expected argument 'type_name' to be a str")
        pulumi.set(__self__, "type_name", type_name)

    @property
    @pulumi.getter(name="apiEntitySetName")
    def api_entity_set_name(self) -> Optional[str]:
        """
        The api entity set name. This becomes the odata entity set name for the entity Type being referred in this object.
        """
        return pulumi.get(self, "api_entity_set_name")

    @property
    @pulumi.getter
    def attributes(self) -> Optional[Mapping[str, Sequence[str]]]:
        """
        The attributes for the Type.
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter
    def description(self) -> Optional[Mapping[str, str]]:
        """
        Localized descriptions for the property.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[Mapping[str, str]]:
        """
        Localized display names for the property.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> Optional[str]:
        """
        Type of entity.
        """
        return pulumi.get(self, "entity_type")

    @property
    @pulumi.getter
    def fields(self) -> Optional[Sequence['outputs.PropertyDefinitionResponse']]:
        """
        The properties of the Profile.
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instancesCount")
    def instances_count(self) -> Optional[int]:
        """
        The instance count.
        """
        return pulumi.get(self, "instances_count")

    @property
    @pulumi.getter(name="largeImage")
    def large_image(self) -> Optional[str]:
        """
        Large Image associated with the Property or EntityType.
        """
        return pulumi.get(self, "large_image")

    @property
    @pulumi.getter(name="lastChangedUtc")
    def last_changed_utc(self) -> str:
        """
        The last changed time for the type definition.
        """
        return pulumi.get(self, "last_changed_utc")

    @property
    @pulumi.getter(name="localizedAttributes")
    def localized_attributes(self) -> Optional[Mapping[str, Mapping[str, str]]]:
        """
        Any custom localized attributes for the Type.
        """
        return pulumi.get(self, "localized_attributes")

    @property
    @pulumi.getter(name="mediumImage")
    def medium_image(self) -> Optional[str]:
        """
        Medium Image associated with the Property or EntityType.
        """
        return pulumi.get(self, "medium_image")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="schemaItemTypeLink")
    def schema_item_type_link(self) -> Optional[str]:
        """
        The schema org link. This helps ACI identify and suggest semantic models.
        """
        return pulumi.get(self, "schema_item_type_link")

    @property
    @pulumi.getter(name="smallImage")
    def small_image(self) -> Optional[str]:
        """
        Small Image associated with the Property or EntityType.
        """
        return pulumi.get(self, "small_image")

    @property
    @pulumi.getter(name="strongIds")
    def strong_ids(self) -> Optional[Sequence['outputs.StrongIdResponse']]:
        """
        The strong IDs.
        """
        return pulumi.get(self, "strong_ids")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The hub name.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="timestampFieldName")
    def timestamp_field_name(self) -> Optional[str]:
        """
        The timestamp property name. Represents the time when the interaction or profile update happened.
        """
        return pulumi.get(self, "timestamp_field_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="typeName")
    def type_name(self) -> Optional[str]:
        """
        The name of the entity.
        """
        return pulumi.get(self, "type_name")


class AwaitableGetProfileResult(GetProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProfileResult(
            api_entity_set_name=self.api_entity_set_name,
            attributes=self.attributes,
            description=self.description,
            display_name=self.display_name,
            entity_type=self.entity_type,
            fields=self.fields,
            id=self.id,
            instances_count=self.instances_count,
            large_image=self.large_image,
            last_changed_utc=self.last_changed_utc,
            localized_attributes=self.localized_attributes,
            medium_image=self.medium_image,
            name=self.name,
            provisioning_state=self.provisioning_state,
            schema_item_type_link=self.schema_item_type_link,
            small_image=self.small_image,
            strong_ids=self.strong_ids,
            tenant_id=self.tenant_id,
            timestamp_field_name=self.timestamp_field_name,
            type=self.type,
            type_name=self.type_name)


def get_profile(hub_name: Optional[str] = None,
                locale_code: Optional[str] = None,
                profile_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProfileResult:
    """
    The profile resource format.


    :param str hub_name: The name of the hub.
    :param str locale_code: Locale of profile to retrieve, default is en-us.
    :param str profile_name: The name of the profile.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['hubName'] = hub_name
    __args__['localeCode'] = locale_code
    __args__['profileName'] = profile_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:customerinsights/v20170101:getProfile', __args__, opts=opts, typ=GetProfileResult).value

    return AwaitableGetProfileResult(
        api_entity_set_name=__ret__.api_entity_set_name,
        attributes=__ret__.attributes,
        description=__ret__.description,
        display_name=__ret__.display_name,
        entity_type=__ret__.entity_type,
        fields=__ret__.fields,
        id=__ret__.id,
        instances_count=__ret__.instances_count,
        large_image=__ret__.large_image,
        last_changed_utc=__ret__.last_changed_utc,
        localized_attributes=__ret__.localized_attributes,
        medium_image=__ret__.medium_image,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        schema_item_type_link=__ret__.schema_item_type_link,
        small_image=__ret__.small_image,
        strong_ids=__ret__.strong_ids,
        tenant_id=__ret__.tenant_id,
        timestamp_field_name=__ret__.timestamp_field_name,
        type=__ret__.type,
        type_name=__ret__.type_name)
