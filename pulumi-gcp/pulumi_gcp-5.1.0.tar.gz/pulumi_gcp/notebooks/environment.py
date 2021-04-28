# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['EnvironmentArgs', 'Environment']

@pulumi.input_type
class EnvironmentArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 container_image: Optional[pulumi.Input['EnvironmentContainerImageArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 post_startup_script: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 vm_image: Optional[pulumi.Input['EnvironmentVmImageArgs']] = None):
        """
        The set of arguments for constructing a Environment resource.
        :param pulumi.Input[str] location: A reference to the zone where the machine resides.
        :param pulumi.Input['EnvironmentContainerImageArgs'] container_image: Use a container image to start the notebook instance.
               Structure is documented below.
        :param pulumi.Input[str] description: A brief description of this environment.
        :param pulumi.Input[str] display_name: Display name of this environment for the UI.
        :param pulumi.Input[str] name: The name specified for the Environment instance.
               Format: projects/{project_id}/locations/{location}/environments/{environmentId}
        :param pulumi.Input[str] post_startup_script: Path to a Bash script that automatically runs after a notebook instance fully boots up.
               The path must be a URL or Cloud Storage path. Example: "gs://path-to-file/file-name"
        :param pulumi.Input[str] project: The name of the Google Cloud project that this VM image belongs to.
               Format: projects/{project_id}
        :param pulumi.Input['EnvironmentVmImageArgs'] vm_image: Use a Compute Engine VM image to start the notebook instance.
               Structure is documented below.
        """
        pulumi.set(__self__, "location", location)
        if container_image is not None:
            pulumi.set(__self__, "container_image", container_image)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if post_startup_script is not None:
            pulumi.set(__self__, "post_startup_script", post_startup_script)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if vm_image is not None:
            pulumi.set(__self__, "vm_image", vm_image)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        A reference to the zone where the machine resides.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> Optional[pulumi.Input['EnvironmentContainerImageArgs']]:
        """
        Use a container image to start the notebook instance.
        Structure is documented below.
        """
        return pulumi.get(self, "container_image")

    @container_image.setter
    def container_image(self, value: Optional[pulumi.Input['EnvironmentContainerImageArgs']]):
        pulumi.set(self, "container_image", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A brief description of this environment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of this environment for the UI.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name specified for the Environment instance.
        Format: projects/{project_id}/locations/{location}/environments/{environmentId}
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="postStartupScript")
    def post_startup_script(self) -> Optional[pulumi.Input[str]]:
        """
        Path to a Bash script that automatically runs after a notebook instance fully boots up.
        The path must be a URL or Cloud Storage path. Example: "gs://path-to-file/file-name"
        """
        return pulumi.get(self, "post_startup_script")

    @post_startup_script.setter
    def post_startup_script(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "post_startup_script", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Google Cloud project that this VM image belongs to.
        Format: projects/{project_id}
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="vmImage")
    def vm_image(self) -> Optional[pulumi.Input['EnvironmentVmImageArgs']]:
        """
        Use a Compute Engine VM image to start the notebook instance.
        Structure is documented below.
        """
        return pulumi.get(self, "vm_image")

    @vm_image.setter
    def vm_image(self, value: Optional[pulumi.Input['EnvironmentVmImageArgs']]):
        pulumi.set(self, "vm_image", value)


@pulumi.input_type
class _EnvironmentState:
    def __init__(__self__, *,
                 container_image: Optional[pulumi.Input['EnvironmentContainerImageArgs']] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 post_startup_script: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 vm_image: Optional[pulumi.Input['EnvironmentVmImageArgs']] = None):
        """
        Input properties used for looking up and filtering Environment resources.
        :param pulumi.Input['EnvironmentContainerImageArgs'] container_image: Use a container image to start the notebook instance.
               Structure is documented below.
        :param pulumi.Input[str] create_time: Instance creation time
        :param pulumi.Input[str] description: A brief description of this environment.
        :param pulumi.Input[str] display_name: Display name of this environment for the UI.
        :param pulumi.Input[str] location: A reference to the zone where the machine resides.
        :param pulumi.Input[str] name: The name specified for the Environment instance.
               Format: projects/{project_id}/locations/{location}/environments/{environmentId}
        :param pulumi.Input[str] post_startup_script: Path to a Bash script that automatically runs after a notebook instance fully boots up.
               The path must be a URL or Cloud Storage path. Example: "gs://path-to-file/file-name"
        :param pulumi.Input[str] project: The name of the Google Cloud project that this VM image belongs to.
               Format: projects/{project_id}
        :param pulumi.Input['EnvironmentVmImageArgs'] vm_image: Use a Compute Engine VM image to start the notebook instance.
               Structure is documented below.
        """
        if container_image is not None:
            pulumi.set(__self__, "container_image", container_image)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if post_startup_script is not None:
            pulumi.set(__self__, "post_startup_script", post_startup_script)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if vm_image is not None:
            pulumi.set(__self__, "vm_image", vm_image)

    @property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> Optional[pulumi.Input['EnvironmentContainerImageArgs']]:
        """
        Use a container image to start the notebook instance.
        Structure is documented below.
        """
        return pulumi.get(self, "container_image")

    @container_image.setter
    def container_image(self, value: Optional[pulumi.Input['EnvironmentContainerImageArgs']]):
        pulumi.set(self, "container_image", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        Instance creation time
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A brief description of this environment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of this environment for the UI.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        A reference to the zone where the machine resides.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name specified for the Environment instance.
        Format: projects/{project_id}/locations/{location}/environments/{environmentId}
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="postStartupScript")
    def post_startup_script(self) -> Optional[pulumi.Input[str]]:
        """
        Path to a Bash script that automatically runs after a notebook instance fully boots up.
        The path must be a URL or Cloud Storage path. Example: "gs://path-to-file/file-name"
        """
        return pulumi.get(self, "post_startup_script")

    @post_startup_script.setter
    def post_startup_script(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "post_startup_script", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Google Cloud project that this VM image belongs to.
        Format: projects/{project_id}
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="vmImage")
    def vm_image(self) -> Optional[pulumi.Input['EnvironmentVmImageArgs']]:
        """
        Use a Compute Engine VM image to start the notebook instance.
        Structure is documented below.
        """
        return pulumi.get(self, "vm_image")

    @vm_image.setter
    def vm_image(self, value: Optional[pulumi.Input['EnvironmentVmImageArgs']]):
        pulumi.set(self, "vm_image", value)


class Environment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_image: Optional[pulumi.Input[pulumi.InputType['EnvironmentContainerImageArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 post_startup_script: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 vm_image: Optional[pulumi.Input[pulumi.InputType['EnvironmentVmImageArgs']]] = None,
                 __props__=None):
        """
        A Cloud AI Platform Notebook environment.

        To get more information about Environment, see:

        * [API documentation](https://cloud.google.com/ai-platform/notebooks/docs/reference/rest)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/ai-platform-notebooks)

        ## Example Usage
        ### Notebook Environment Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        environment = gcp.notebooks.Environment("environment",
            container_image=gcp.notebooks.EnvironmentContainerImageArgs(
                repository="gcr.io/deeplearning-platform-release/base-cpu",
            ),
            location="us-west1-a")
        ```

        ## Import

        Environment can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:notebooks/environment:Environment default projects/{{project}}/locations/{{location}}/environments/{{name}}
        ```

        ```sh
         $ pulumi import gcp:notebooks/environment:Environment default {{project}}/{{location}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:notebooks/environment:Environment default {{location}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['EnvironmentContainerImageArgs']] container_image: Use a container image to start the notebook instance.
               Structure is documented below.
        :param pulumi.Input[str] description: A brief description of this environment.
        :param pulumi.Input[str] display_name: Display name of this environment for the UI.
        :param pulumi.Input[str] location: A reference to the zone where the machine resides.
        :param pulumi.Input[str] name: The name specified for the Environment instance.
               Format: projects/{project_id}/locations/{location}/environments/{environmentId}
        :param pulumi.Input[str] post_startup_script: Path to a Bash script that automatically runs after a notebook instance fully boots up.
               The path must be a URL or Cloud Storage path. Example: "gs://path-to-file/file-name"
        :param pulumi.Input[str] project: The name of the Google Cloud project that this VM image belongs to.
               Format: projects/{project_id}
        :param pulumi.Input[pulumi.InputType['EnvironmentVmImageArgs']] vm_image: Use a Compute Engine VM image to start the notebook instance.
               Structure is documented below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Cloud AI Platform Notebook environment.

        To get more information about Environment, see:

        * [API documentation](https://cloud.google.com/ai-platform/notebooks/docs/reference/rest)
        * How-to Guides
            * [Official Documentation](https://cloud.google.com/ai-platform-notebooks)

        ## Example Usage
        ### Notebook Environment Basic

        ```python
        import pulumi
        import pulumi_gcp as gcp

        environment = gcp.notebooks.Environment("environment",
            container_image=gcp.notebooks.EnvironmentContainerImageArgs(
                repository="gcr.io/deeplearning-platform-release/base-cpu",
            ),
            location="us-west1-a")
        ```

        ## Import

        Environment can be imported using any of these accepted formats

        ```sh
         $ pulumi import gcp:notebooks/environment:Environment default projects/{{project}}/locations/{{location}}/environments/{{name}}
        ```

        ```sh
         $ pulumi import gcp:notebooks/environment:Environment default {{project}}/{{location}}/{{name}}
        ```

        ```sh
         $ pulumi import gcp:notebooks/environment:Environment default {{location}}/{{name}}
        ```

        :param str resource_name: The name of the resource.
        :param EnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_image: Optional[pulumi.Input[pulumi.InputType['EnvironmentContainerImageArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 post_startup_script: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 vm_image: Optional[pulumi.Input[pulumi.InputType['EnvironmentVmImageArgs']]] = None,
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
            __props__ = EnvironmentArgs.__new__(EnvironmentArgs)

            __props__.__dict__["container_image"] = container_image
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["post_startup_script"] = post_startup_script
            __props__.__dict__["project"] = project
            __props__.__dict__["vm_image"] = vm_image
            __props__.__dict__["create_time"] = None
        super(Environment, __self__).__init__(
            'gcp:notebooks/environment:Environment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            container_image: Optional[pulumi.Input[pulumi.InputType['EnvironmentContainerImageArgs']]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            post_startup_script: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            vm_image: Optional[pulumi.Input[pulumi.InputType['EnvironmentVmImageArgs']]] = None) -> 'Environment':
        """
        Get an existing Environment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['EnvironmentContainerImageArgs']] container_image: Use a container image to start the notebook instance.
               Structure is documented below.
        :param pulumi.Input[str] create_time: Instance creation time
        :param pulumi.Input[str] description: A brief description of this environment.
        :param pulumi.Input[str] display_name: Display name of this environment for the UI.
        :param pulumi.Input[str] location: A reference to the zone where the machine resides.
        :param pulumi.Input[str] name: The name specified for the Environment instance.
               Format: projects/{project_id}/locations/{location}/environments/{environmentId}
        :param pulumi.Input[str] post_startup_script: Path to a Bash script that automatically runs after a notebook instance fully boots up.
               The path must be a URL or Cloud Storage path. Example: "gs://path-to-file/file-name"
        :param pulumi.Input[str] project: The name of the Google Cloud project that this VM image belongs to.
               Format: projects/{project_id}
        :param pulumi.Input[pulumi.InputType['EnvironmentVmImageArgs']] vm_image: Use a Compute Engine VM image to start the notebook instance.
               Structure is documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EnvironmentState.__new__(_EnvironmentState)

        __props__.__dict__["container_image"] = container_image
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["post_startup_script"] = post_startup_script
        __props__.__dict__["project"] = project
        __props__.__dict__["vm_image"] = vm_image
        return Environment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> pulumi.Output[Optional['outputs.EnvironmentContainerImage']]:
        """
        Use a container image to start the notebook instance.
        Structure is documented below.
        """
        return pulumi.get(self, "container_image")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Instance creation time
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A brief description of this environment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Display name of this environment for the UI.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        A reference to the zone where the machine resides.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name specified for the Environment instance.
        Format: projects/{project_id}/locations/{location}/environments/{environmentId}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="postStartupScript")
    def post_startup_script(self) -> pulumi.Output[Optional[str]]:
        """
        Path to a Bash script that automatically runs after a notebook instance fully boots up.
        The path must be a URL or Cloud Storage path. Example: "gs://path-to-file/file-name"
        """
        return pulumi.get(self, "post_startup_script")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The name of the Google Cloud project that this VM image belongs to.
        Format: projects/{project_id}
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="vmImage")
    def vm_image(self) -> pulumi.Output[Optional['outputs.EnvironmentVmImage']]:
        """
        Use a Compute Engine VM image to start the notebook instance.
        Structure is documented below.
        """
        return pulumi.get(self, "vm_image")

