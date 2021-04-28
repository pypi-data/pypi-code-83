# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'FunctionEventTriggerArgs',
    'FunctionEventTriggerFailurePolicyArgs',
    'FunctionIamBindingConditionArgs',
    'FunctionIamMemberConditionArgs',
    'FunctionSourceRepositoryArgs',
]

@pulumi.input_type
class FunctionEventTriggerArgs:
    def __init__(__self__, *,
                 event_type: pulumi.Input[str],
                 resource: pulumi.Input[str],
                 failure_policy: Optional[pulumi.Input['FunctionEventTriggerFailurePolicyArgs']] = None):
        """
        :param pulumi.Input[str] event_type: The type of event to observe. For example: `"google.storage.object.finalize"`.
               See the documentation on [calling Cloud Functions](https://cloud.google.com/functions/docs/calling/) for a
               full reference of accepted triggers.
        :param pulumi.Input[str] resource: Required. The name or partial URI of the resource from
               which to observe events. For example, `"myBucket"` or `"projects/my-project/topics/my-topic"`
        :param pulumi.Input['FunctionEventTriggerFailurePolicyArgs'] failure_policy: Specifies policy for failed executions. Structure is documented below.
        """
        pulumi.set(__self__, "event_type", event_type)
        pulumi.set(__self__, "resource", resource)
        if failure_policy is not None:
            pulumi.set(__self__, "failure_policy", failure_policy)

    @property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input[str]:
        """
        The type of event to observe. For example: `"google.storage.object.finalize"`.
        See the documentation on [calling Cloud Functions](https://cloud.google.com/functions/docs/calling/) for a
        full reference of accepted triggers.
        """
        return pulumi.get(self, "event_type")

    @event_type.setter
    def event_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "event_type", value)

    @property
    @pulumi.getter
    def resource(self) -> pulumi.Input[str]:
        """
        Required. The name or partial URI of the resource from
        which to observe events. For example, `"myBucket"` or `"projects/my-project/topics/my-topic"`
        """
        return pulumi.get(self, "resource")

    @resource.setter
    def resource(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource", value)

    @property
    @pulumi.getter(name="failurePolicy")
    def failure_policy(self) -> Optional[pulumi.Input['FunctionEventTriggerFailurePolicyArgs']]:
        """
        Specifies policy for failed executions. Structure is documented below.
        """
        return pulumi.get(self, "failure_policy")

    @failure_policy.setter
    def failure_policy(self, value: Optional[pulumi.Input['FunctionEventTriggerFailurePolicyArgs']]):
        pulumi.set(self, "failure_policy", value)


@pulumi.input_type
class FunctionEventTriggerFailurePolicyArgs:
    def __init__(__self__, *,
                 retry: pulumi.Input[bool]):
        """
        :param pulumi.Input[bool] retry: Whether the function should be retried on failure. Defaults to `false`.
        """
        pulumi.set(__self__, "retry", retry)

    @property
    @pulumi.getter
    def retry(self) -> pulumi.Input[bool]:
        """
        Whether the function should be retried on failure. Defaults to `false`.
        """
        return pulumi.get(self, "retry")

    @retry.setter
    def retry(self, value: pulumi.Input[bool]):
        pulumi.set(self, "retry", value)


@pulumi.input_type
class FunctionIamBindingConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class FunctionIamMemberConditionArgs:
    def __init__(__self__, *,
                 expression: pulumi.Input[str],
                 title: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "expression", expression)
        pulumi.set(__self__, "title", title)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter
    def expression(self) -> pulumi.Input[str]:
        return pulumi.get(self, "expression")

    @expression.setter
    def expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "expression", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class FunctionSourceRepositoryArgs:
    def __init__(__self__, *,
                 url: pulumi.Input[str],
                 deployed_url: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] url: The URL pointing to the hosted repository where the function is defined. There are supported Cloud Source Repository URLs in the following formats:
        """
        pulumi.set(__self__, "url", url)
        if deployed_url is not None:
            pulumi.set(__self__, "deployed_url", deployed_url)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        The URL pointing to the hosted repository where the function is defined. There are supported Cloud Source Repository URLs in the following formats:
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="deployedUrl")
    def deployed_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "deployed_url")

    @deployed_url.setter
    def deployed_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployed_url", value)


