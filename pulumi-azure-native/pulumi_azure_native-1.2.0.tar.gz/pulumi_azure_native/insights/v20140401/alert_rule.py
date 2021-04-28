# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['AlertRuleArgs', 'AlertRule']

@pulumi.input_type
class AlertRuleArgs:
    def __init__(__self__, *,
                 condition: pulumi.Input[Union['LocationThresholdRuleConditionArgs', 'ManagementEventRuleConditionArgs', 'ThresholdRuleConditionArgs']],
                 is_enabled: pulumi.Input[bool],
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 action: Optional[pulumi.Input[Union['RuleEmailActionArgs', 'RuleWebhookActionArgs']]] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['RuleEmailActionArgs', 'RuleWebhookActionArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AlertRule resource.
        :param pulumi.Input[Union['LocationThresholdRuleConditionArgs', 'ManagementEventRuleConditionArgs', 'ThresholdRuleConditionArgs']] condition: the condition that results in the alert rule being activated.
        :param pulumi.Input[bool] is_enabled: the flag that indicates whether the alert rule is enabled.
        :param pulumi.Input[str] name: the name of the alert rule.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Union['RuleEmailActionArgs', 'RuleWebhookActionArgs']] action: action that is performed when the alert rule becomes active, and when an alert condition is resolved.
        :param pulumi.Input[Sequence[pulumi.Input[Union['RuleEmailActionArgs', 'RuleWebhookActionArgs']]]] actions: the array of actions that are performed when the alert rule becomes active, and when an alert condition is resolved.
        :param pulumi.Input[str] description: the description of the alert rule that will be included in the alert email.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] provisioning_state: the provisioning state.
        :param pulumi.Input[str] rule_name: The name of the rule.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "condition", condition)
        pulumi.set(__self__, "is_enabled", is_enabled)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if action is not None:
            pulumi.set(__self__, "action", action)
        if actions is not None:
            pulumi.set(__self__, "actions", actions)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if rule_name is not None:
            pulumi.set(__self__, "rule_name", rule_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def condition(self) -> pulumi.Input[Union['LocationThresholdRuleConditionArgs', 'ManagementEventRuleConditionArgs', 'ThresholdRuleConditionArgs']]:
        """
        the condition that results in the alert rule being activated.
        """
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: pulumi.Input[Union['LocationThresholdRuleConditionArgs', 'ManagementEventRuleConditionArgs', 'ThresholdRuleConditionArgs']]):
        pulumi.set(self, "condition", value)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[bool]:
        """
        the flag that indicates whether the alert rule is enabled.
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        the name of the alert rule.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Union['RuleEmailActionArgs', 'RuleWebhookActionArgs']]]:
        """
        action that is performed when the alert rule becomes active, and when an alert condition is resolved.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[Union['RuleEmailActionArgs', 'RuleWebhookActionArgs']]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union['RuleEmailActionArgs', 'RuleWebhookActionArgs']]]]]:
        """
        the array of actions that are performed when the alert rule becomes active, and when an alert condition is resolved.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union['RuleEmailActionArgs', 'RuleWebhookActionArgs']]]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        the description of the alert rule that will be included in the alert email.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the rule.
        """
        return pulumi.get(self, "rule_name")

    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class AlertRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[Union[pulumi.InputType['RuleEmailActionArgs'], pulumi.InputType['RuleWebhookActionArgs']]]] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['RuleEmailActionArgs'], pulumi.InputType['RuleWebhookActionArgs']]]]]] = None,
                 condition: Optional[pulumi.Input[Union[pulumi.InputType['LocationThresholdRuleConditionArgs'], pulumi.InputType['ManagementEventRuleConditionArgs'], pulumi.InputType['ThresholdRuleConditionArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The alert rule resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[pulumi.InputType['RuleEmailActionArgs'], pulumi.InputType['RuleWebhookActionArgs']]] action: action that is performed when the alert rule becomes active, and when an alert condition is resolved.
        :param pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['RuleEmailActionArgs'], pulumi.InputType['RuleWebhookActionArgs']]]]] actions: the array of actions that are performed when the alert rule becomes active, and when an alert condition is resolved.
        :param pulumi.Input[Union[pulumi.InputType['LocationThresholdRuleConditionArgs'], pulumi.InputType['ManagementEventRuleConditionArgs'], pulumi.InputType['ThresholdRuleConditionArgs']]] condition: the condition that results in the alert rule being activated.
        :param pulumi.Input[str] description: the description of the alert rule that will be included in the alert email.
        :param pulumi.Input[bool] is_enabled: the flag that indicates whether the alert rule is enabled.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] name: the name of the alert rule.
        :param pulumi.Input[str] provisioning_state: the provisioning state.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] rule_name: The name of the rule.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AlertRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The alert rule resource.

        :param str resource_name: The name of the resource.
        :param AlertRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AlertRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[Union[pulumi.InputType['RuleEmailActionArgs'], pulumi.InputType['RuleWebhookActionArgs']]]] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['RuleEmailActionArgs'], pulumi.InputType['RuleWebhookActionArgs']]]]]] = None,
                 condition: Optional[pulumi.Input[Union[pulumi.InputType['LocationThresholdRuleConditionArgs'], pulumi.InputType['ManagementEventRuleConditionArgs'], pulumi.InputType['ThresholdRuleConditionArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 is_enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = AlertRuleArgs.__new__(AlertRuleArgs)

            __props__.__dict__["action"] = action
            __props__.__dict__["actions"] = actions
            if condition is None and not opts.urn:
                raise TypeError("Missing required property 'condition'")
            __props__.__dict__["condition"] = condition
            __props__.__dict__["description"] = description
            if is_enabled is None and not opts.urn:
                raise TypeError("Missing required property 'is_enabled'")
            __props__.__dict__["is_enabled"] = is_enabled
            __props__.__dict__["location"] = location
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["rule_name"] = rule_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["last_updated_time"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:insights/v20140401:AlertRule"), pulumi.Alias(type_="azure-native:insights:AlertRule"), pulumi.Alias(type_="azure-nextgen:insights:AlertRule"), pulumi.Alias(type_="azure-native:insights/v20160301:AlertRule"), pulumi.Alias(type_="azure-nextgen:insights/v20160301:AlertRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AlertRule, __self__).__init__(
            'azure-native:insights/v20140401:AlertRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AlertRule':
        """
        Get an existing AlertRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AlertRuleArgs.__new__(AlertRuleArgs)

        __props__.__dict__["action"] = None
        __props__.__dict__["actions"] = None
        __props__.__dict__["condition"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["is_enabled"] = None
        __props__.__dict__["last_updated_time"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return AlertRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[Optional[Any]]:
        """
        action that is performed when the alert rule becomes active, and when an alert condition is resolved.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        """
        the array of actions that are performed when the alert rule becomes active, and when an alert condition is resolved.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def condition(self) -> pulumi.Output[Any]:
        """
        the condition that results in the alert rule being activated.
        """
        return pulumi.get(self, "condition")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        the description of the alert rule that will be included in the alert email.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Output[bool]:
        """
        the flag that indicates whether the alert rule is enabled.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[str]:
        """
        Last time the rule was updated in ISO8601 format.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

