# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .app_service_certificate_order import *
from .app_service_certificate_order_certificate import *
from .get_app_service_certificate_order import *
from .get_app_service_certificate_order_certificate import *
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
            if typ == "azure-native:certificateregistration/v20201001:AppServiceCertificateOrder":
                return AppServiceCertificateOrder(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:certificateregistration/v20201001:AppServiceCertificateOrderCertificate":
                return AppServiceCertificateOrderCertificate(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "certificateregistration/v20201001", _module_instance)

_register_module()
