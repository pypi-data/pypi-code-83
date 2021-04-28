# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .deployment import *
from .deployment_at_management_group_scope import *
from .deployment_at_scope import *
from .deployment_at_subscription_scope import *
from .deployment_at_tenant_scope import *
from .get_deployment import *
from .get_deployment_at_management_group_scope import *
from .get_deployment_at_scope import *
from .get_deployment_at_subscription_scope import *
from .get_deployment_at_tenant_scope import *
from .get_resource import *
from .get_resource_group import *
from .get_tag_at_scope import *
from .resource import *
from .resource_group import *
from .tag_at_scope import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from ... import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "azure-native:resources/v20210101:Deployment":
                return Deployment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:resources/v20210101:DeploymentAtManagementGroupScope":
                return DeploymentAtManagementGroupScope(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:resources/v20210101:DeploymentAtScope":
                return DeploymentAtScope(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:resources/v20210101:DeploymentAtSubscriptionScope":
                return DeploymentAtSubscriptionScope(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:resources/v20210101:DeploymentAtTenantScope":
                return DeploymentAtTenantScope(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:resources/v20210101:Resource":
                return Resource(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:resources/v20210101:ResourceGroup":
                return ResourceGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:resources/v20210101:TagAtScope":
                return TagAtScope(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "resources/v20210101", _module_instance)

_register_module()
