# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['EmailTemplateArgs', 'EmailTemplate']

@pulumi.input_type
class EmailTemplateArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 body: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input['EmailTemplateParametersContractPropertiesArgs']]]] = None,
                 subject: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EmailTemplate resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] body: Email Template Body. This should be a valid XDocument
        :param pulumi.Input[str] description: Description of the Email Template.
        :param pulumi.Input[Sequence[pulumi.Input['EmailTemplateParametersContractPropertiesArgs']]] parameters: Email Template Parameter values.
        :param pulumi.Input[str] subject: Subject of the Template.
        :param pulumi.Input[str] template_name: Email Template Name Identifier.
        :param pulumi.Input[str] title: Title of the Template.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if body is not None:
            pulumi.set(__self__, "body", body)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if subject is not None:
            pulumi.set(__self__, "subject", subject)
        if template_name is not None:
            pulumi.set(__self__, "template_name", template_name)
        if title is not None:
            pulumi.set(__self__, "title", title)

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
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[str]]:
        """
        Email Template Body. This should be a valid XDocument
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the Email Template.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EmailTemplateParametersContractPropertiesArgs']]]]:
        """
        Email Template Parameter values.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EmailTemplateParametersContractPropertiesArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def subject(self) -> Optional[pulumi.Input[str]]:
        """
        Subject of the Template.
        """
        return pulumi.get(self, "subject")

    @subject.setter
    def subject(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subject", value)

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[pulumi.Input[str]]:
        """
        Email Template Name Identifier.
        """
        return pulumi.get(self, "template_name")

    @template_name.setter
    def template_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_name", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        Title of the Template.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)


class EmailTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EmailTemplateParametersContractPropertiesArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 subject: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Email Template details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: Email Template Body. This should be a valid XDocument
        :param pulumi.Input[str] description: Description of the Email Template.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EmailTemplateParametersContractPropertiesArgs']]]] parameters: Email Template Parameter values.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] subject: Subject of the Template.
        :param pulumi.Input[str] template_name: Email Template Name Identifier.
        :param pulumi.Input[str] title: Title of the Template.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EmailTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Email Template details.

        :param str resource_name: The name of the resource.
        :param EmailTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EmailTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EmailTemplateParametersContractPropertiesArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 subject: Optional[pulumi.Input[str]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
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
            __props__ = EmailTemplateArgs.__new__(EmailTemplateArgs)

            __props__.__dict__["body"] = body
            __props__.__dict__["description"] = description
            __props__.__dict__["parameters"] = parameters
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["subject"] = subject
            __props__.__dict__["template_name"] = template_name
            __props__.__dict__["title"] = title
            __props__.__dict__["is_default"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-nextgen:apimanagement/v20180101:EmailTemplate"), pulumi.Alias(type_="azure-native:apimanagement:EmailTemplate"), pulumi.Alias(type_="azure-nextgen:apimanagement:EmailTemplate"), pulumi.Alias(type_="azure-native:apimanagement/v20170301:EmailTemplate"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20170301:EmailTemplate"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:EmailTemplate"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20180601preview:EmailTemplate"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:EmailTemplate"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20190101:EmailTemplate"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:EmailTemplate"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201:EmailTemplate"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:EmailTemplate"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20191201preview:EmailTemplate"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:EmailTemplate"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20200601preview:EmailTemplate"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:EmailTemplate"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20201201:EmailTemplate"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:EmailTemplate"), pulumi.Alias(type_="azure-nextgen:apimanagement/v20210101preview:EmailTemplate")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(EmailTemplate, __self__).__init__(
            'azure-native:apimanagement/v20180101:EmailTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EmailTemplate':
        """
        Get an existing EmailTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EmailTemplateArgs.__new__(EmailTemplateArgs)

        __props__.__dict__["body"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["is_default"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["subject"] = None
        __props__.__dict__["title"] = None
        __props__.__dict__["type"] = None
        return EmailTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Output[str]:
        """
        Email Template Body. This should be a valid XDocument
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the Email Template.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> pulumi.Output[bool]:
        """
        Whether the template is the default template provided by Api Management or has been edited.
        """
        return pulumi.get(self, "is_default")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Sequence['outputs.EmailTemplateParametersContractPropertiesResponse']]]:
        """
        Email Template Parameter values.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def subject(self) -> pulumi.Output[str]:
        """
        Subject of the Template.
        """
        return pulumi.get(self, "subject")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[str]]:
        """
        Title of the Template.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

