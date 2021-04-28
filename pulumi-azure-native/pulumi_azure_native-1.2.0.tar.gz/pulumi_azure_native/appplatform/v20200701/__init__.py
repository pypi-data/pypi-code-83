# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .app import *
from .binding import *
from .certificate import *
from .custom_domain import *
from .deployment import *
from .get_app import *
from .get_app_resource_upload_url import *
from .get_binding import *
from .get_certificate import *
from .get_custom_domain import *
from .get_deployment import *
from .get_deployment_log_file_url import *
from .get_service import *
from .list_service_test_keys import *
from .service import *
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
            if typ == "azure-native:appplatform/v20200701:App":
                return App(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:appplatform/v20200701:Binding":
                return Binding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:appplatform/v20200701:Certificate":
                return Certificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:appplatform/v20200701:CustomDomain":
                return CustomDomain(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:appplatform/v20200701:Deployment":
                return Deployment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:appplatform/v20200701:Service":
                return Service(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "appplatform/v20200701", _module_instance)

_register_module()
