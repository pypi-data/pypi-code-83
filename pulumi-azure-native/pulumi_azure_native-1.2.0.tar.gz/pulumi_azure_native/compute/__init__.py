# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from ._enums import *
from .availability_set import *
from .cloud_service import *
from .dedicated_host import *
from .dedicated_host_group import *
from .disk import *
from .disk_access import *
from .disk_access_a_private_endpoint_connection import *
from .disk_encryption_set import *
from .gallery import *
from .gallery_application import *
from .gallery_application_version import *
from .gallery_image import *
from .gallery_image_version import *
from .get_availability_set import *
from .get_cloud_service import *
from .get_dedicated_host import *
from .get_dedicated_host_group import *
from .get_disk import *
from .get_disk_access import *
from .get_disk_access_a_private_endpoint_connection import *
from .get_disk_encryption_set import *
from .get_gallery import *
from .get_gallery_application import *
from .get_gallery_application_version import *
from .get_gallery_image import *
from .get_gallery_image_version import *
from .get_image import *
from .get_log_analytic_export_request_rate_by_interval import *
from .get_log_analytic_export_throttled_requests import *
from .get_proximity_placement_group import *
from .get_snapshot import *
from .get_ssh_public_key import *
from .get_virtual_machine import *
from .get_virtual_machine_extension import *
from .get_virtual_machine_run_command_by_virtual_machine import *
from .get_virtual_machine_scale_set import *
from .get_virtual_machine_scale_set_extension import *
from .get_virtual_machine_scale_set_vm import *
from .get_virtual_machine_scale_set_vm_extension import *
from .get_virtual_machine_scale_set_vm_run_command import *
from .image import *
from .proximity_placement_group import *
from .snapshot import *
from .ssh_public_key import *
from .virtual_machine import *
from .virtual_machine_extension import *
from .virtual_machine_run_command_by_virtual_machine import *
from .virtual_machine_scale_set import *
from .virtual_machine_scale_set_extension import *
from .virtual_machine_scale_set_vm import *
from .virtual_machine_scale_set_vm_extension import *
from .virtual_machine_scale_set_vm_run_command import *
from ._inputs import *
from . import outputs

# Make subpackages available:
from . import (
    v20150615,
    v20160330,
    v20160430preview,
    v20170330,
    v20171201,
    v20180401,
    v20180601,
    v20180930,
    v20181001,
    v20190301,
    v20190701,
    v20191101,
    v20191201,
    v20200501,
    v20200601,
    v20200630,
    v20200930,
    v20201001preview,
    v20201201,
    v20210301,
)

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "azure-native:compute:AvailabilitySet":
                return AvailabilitySet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:CloudService":
                return CloudService(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:DedicatedHost":
                return DedicatedHost(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:DedicatedHostGroup":
                return DedicatedHostGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:Disk":
                return Disk(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:DiskAccess":
                return DiskAccess(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:DiskAccessAPrivateEndpointConnection":
                return DiskAccessAPrivateEndpointConnection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:DiskEncryptionSet":
                return DiskEncryptionSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:Gallery":
                return Gallery(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:GalleryApplication":
                return GalleryApplication(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:GalleryApplicationVersion":
                return GalleryApplicationVersion(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:GalleryImage":
                return GalleryImage(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:GalleryImageVersion":
                return GalleryImageVersion(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:Image":
                return Image(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:ProximityPlacementGroup":
                return ProximityPlacementGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:Snapshot":
                return Snapshot(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:SshPublicKey":
                return SshPublicKey(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:VirtualMachine":
                return VirtualMachine(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:VirtualMachineExtension":
                return VirtualMachineExtension(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:VirtualMachineRunCommandByVirtualMachine":
                return VirtualMachineRunCommandByVirtualMachine(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:VirtualMachineScaleSet":
                return VirtualMachineScaleSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:VirtualMachineScaleSetExtension":
                return VirtualMachineScaleSetExtension(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:VirtualMachineScaleSetVM":
                return VirtualMachineScaleSetVM(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:VirtualMachineScaleSetVMExtension":
                return VirtualMachineScaleSetVMExtension(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "azure-native:compute:VirtualMachineScaleSetVMRunCommand":
                return VirtualMachineScaleSetVMRunCommand(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("azure-native", "compute", _module_instance)

_register_module()
