# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BackendServiceSignedUrlKeyArgs', 'BackendServiceSignedUrlKey']

@pulumi.input_type
class BackendServiceSignedUrlKeyArgs:
    def __init__(__self__, *,
                 backend_service: pulumi.Input[str],
                 key_value: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BackendServiceSignedUrlKey resource.
        :param pulumi.Input[str] backend_service: The backend service this signed URL key belongs.
        :param pulumi.Input[str] key_value: 128-bit key value used for signing the URL. The key value must be a
               valid RFC 4648 Section 5 base64url encoded string.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] name: Name of the signed URL key.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        pulumi.set(__self__, "backend_service", backend_service)
        pulumi.set(__self__, "key_value", key_value)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="backendService")
    def backend_service(self) -> pulumi.Input[str]:
        """
        The backend service this signed URL key belongs.
        """
        return pulumi.get(self, "backend_service")

    @backend_service.setter
    def backend_service(self, value: pulumi.Input[str]):
        pulumi.set(self, "backend_service", value)

    @property
    @pulumi.getter(name="keyValue")
    def key_value(self) -> pulumi.Input[str]:
        """
        128-bit key value used for signing the URL. The key value must be a
        valid RFC 4648 Section 5 base64url encoded string.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "key_value")

    @key_value.setter
    def key_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the signed URL key.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _BackendServiceSignedUrlKeyState:
    def __init__(__self__, *,
                 backend_service: Optional[pulumi.Input[str]] = None,
                 key_value: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BackendServiceSignedUrlKey resources.
        :param pulumi.Input[str] backend_service: The backend service this signed URL key belongs.
        :param pulumi.Input[str] key_value: 128-bit key value used for signing the URL. The key value must be a
               valid RFC 4648 Section 5 base64url encoded string.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] name: Name of the signed URL key.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        if backend_service is not None:
            pulumi.set(__self__, "backend_service", backend_service)
        if key_value is not None:
            pulumi.set(__self__, "key_value", key_value)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="backendService")
    def backend_service(self) -> Optional[pulumi.Input[str]]:
        """
        The backend service this signed URL key belongs.
        """
        return pulumi.get(self, "backend_service")

    @backend_service.setter
    def backend_service(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backend_service", value)

    @property
    @pulumi.getter(name="keyValue")
    def key_value(self) -> Optional[pulumi.Input[str]]:
        """
        128-bit key value used for signing the URL. The key value must be a
        valid RFC 4648 Section 5 base64url encoded string.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "key_value")

    @key_value.setter
    def key_value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the signed URL key.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class BackendServiceSignedUrlKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_service: Optional[pulumi.Input[str]] = None,
                 key_value: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A key for signing Cloud CDN signed URLs for Backend Services.

        To get more information about BackendServiceSignedUrlKey, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/backendServices)
        * How-to Guides
            * [Using Signed URLs](https://cloud.google.com/cdn/docs/using-signed-urls/)

        > **Warning:** All arguments including `key_value` will be stored in the raw
        state as plain-text.

        ## Example Usage
        ### Backend Service Signed Url Key

        ```python
        import pulumi
        import pulumi_gcp as gcp
        import pulumi_random as random

        url_signature = random.RandomId("urlSignature", byte_length=16)
        webserver = gcp.compute.InstanceTemplate("webserver",
            machine_type="e2-medium",
            network_interfaces=[gcp.compute.InstanceTemplateNetworkInterfaceArgs(
                network="default",
            )],
            disks=[gcp.compute.InstanceTemplateDiskArgs(
                source_image="debian-cloud/debian-9",
                auto_delete=True,
                boot=True,
            )])
        webservers = gcp.compute.InstanceGroupManager("webservers",
            versions=[gcp.compute.InstanceGroupManagerVersionArgs(
                instance_template=webserver.id,
                name="primary",
            )],
            base_instance_name="webserver",
            zone="us-central1-f",
            target_size=1)
        default = gcp.compute.HttpHealthCheck("default",
            request_path="/",
            check_interval_sec=1,
            timeout_sec=1)
        example_backend = gcp.compute.BackendService("exampleBackend",
            description="Our company website",
            port_name="http",
            protocol="HTTP",
            timeout_sec=10,
            enable_cdn=True,
            backends=[gcp.compute.BackendServiceBackendArgs(
                group=webservers.instance_group,
            )],
            health_checks=[default.id])
        backend_key = gcp.compute.BackendServiceSignedUrlKey("backendKey",
            key_value=url_signature.b64_url,
            backend_service=example_backend.name)
        ```

        ## Import

        This resource does not support import.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backend_service: The backend service this signed URL key belongs.
        :param pulumi.Input[str] key_value: 128-bit key value used for signing the URL. The key value must be a
               valid RFC 4648 Section 5 base64url encoded string.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] name: Name of the signed URL key.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BackendServiceSignedUrlKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A key for signing Cloud CDN signed URLs for Backend Services.

        To get more information about BackendServiceSignedUrlKey, see:

        * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/backendServices)
        * How-to Guides
            * [Using Signed URLs](https://cloud.google.com/cdn/docs/using-signed-urls/)

        > **Warning:** All arguments including `key_value` will be stored in the raw
        state as plain-text.

        ## Example Usage
        ### Backend Service Signed Url Key

        ```python
        import pulumi
        import pulumi_gcp as gcp
        import pulumi_random as random

        url_signature = random.RandomId("urlSignature", byte_length=16)
        webserver = gcp.compute.InstanceTemplate("webserver",
            machine_type="e2-medium",
            network_interfaces=[gcp.compute.InstanceTemplateNetworkInterfaceArgs(
                network="default",
            )],
            disks=[gcp.compute.InstanceTemplateDiskArgs(
                source_image="debian-cloud/debian-9",
                auto_delete=True,
                boot=True,
            )])
        webservers = gcp.compute.InstanceGroupManager("webservers",
            versions=[gcp.compute.InstanceGroupManagerVersionArgs(
                instance_template=webserver.id,
                name="primary",
            )],
            base_instance_name="webserver",
            zone="us-central1-f",
            target_size=1)
        default = gcp.compute.HttpHealthCheck("default",
            request_path="/",
            check_interval_sec=1,
            timeout_sec=1)
        example_backend = gcp.compute.BackendService("exampleBackend",
            description="Our company website",
            port_name="http",
            protocol="HTTP",
            timeout_sec=10,
            enable_cdn=True,
            backends=[gcp.compute.BackendServiceBackendArgs(
                group=webservers.instance_group,
            )],
            health_checks=[default.id])
        backend_key = gcp.compute.BackendServiceSignedUrlKey("backendKey",
            key_value=url_signature.b64_url,
            backend_service=example_backend.name)
        ```

        ## Import

        This resource does not support import.

        :param str resource_name: The name of the resource.
        :param BackendServiceSignedUrlKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BackendServiceSignedUrlKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_service: Optional[pulumi.Input[str]] = None,
                 key_value: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
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
            __props__ = BackendServiceSignedUrlKeyArgs.__new__(BackendServiceSignedUrlKeyArgs)

            if backend_service is None and not opts.urn:
                raise TypeError("Missing required property 'backend_service'")
            __props__.__dict__["backend_service"] = backend_service
            if key_value is None and not opts.urn:
                raise TypeError("Missing required property 'key_value'")
            __props__.__dict__["key_value"] = key_value
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
        super(BackendServiceSignedUrlKey, __self__).__init__(
            'gcp:compute/backendServiceSignedUrlKey:BackendServiceSignedUrlKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            backend_service: Optional[pulumi.Input[str]] = None,
            key_value: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'BackendServiceSignedUrlKey':
        """
        Get an existing BackendServiceSignedUrlKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backend_service: The backend service this signed URL key belongs.
        :param pulumi.Input[str] key_value: 128-bit key value used for signing the URL. The key value must be a
               valid RFC 4648 Section 5 base64url encoded string.
               **Note**: This property is sensitive and will not be displayed in the plan.
        :param pulumi.Input[str] name: Name of the signed URL key.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs.
               If it is not provided, the provider project is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BackendServiceSignedUrlKeyState.__new__(_BackendServiceSignedUrlKeyState)

        __props__.__dict__["backend_service"] = backend_service
        __props__.__dict__["key_value"] = key_value
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        return BackendServiceSignedUrlKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backendService")
    def backend_service(self) -> pulumi.Output[str]:
        """
        The backend service this signed URL key belongs.
        """
        return pulumi.get(self, "backend_service")

    @property
    @pulumi.getter(name="keyValue")
    def key_value(self) -> pulumi.Output[str]:
        """
        128-bit key value used for signing the URL. The key value must be a
        valid RFC 4648 Section 5 base64url encoded string.
        **Note**: This property is sensitive and will not be displayed in the plan.
        """
        return pulumi.get(self, "key_value")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the signed URL key.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        return pulumi.get(self, "project")

