# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .address import *
from .attached_disk import *
from .autoscalar import *
from .autoscaler import *
from .backend_bucket import *
from .backend_bucket_signed_url_key import *
from .backend_service import *
from .backend_service_signed_url_key import *
from .disk import *
from .disk_iam_binding import *
from .disk_iam_member import *
from .disk_iam_policy import *
from .disk_resource_policy_attachment import *
from .external_vpn_gateway import *
from .firewall import *
from .forwarding_rule import *
from .get_address import *
from .get_backend_bucket import *
from .get_backend_service import *
from .get_certificate import *
from .get_default_service_account import *
from .get_forwarding_rule import *
from .get_global_address import *
from .get_global_forwarding_rule import *
from .get_health_check import *
from .get_image import *
from .get_instance import *
from .get_instance_group import *
from .get_instance_serial_port import *
from .get_instance_template import *
from .get_lbip_ranges import *
from .get_netblock_ip_ranges import *
from .get_network import *
from .get_network_endpoint_group import *
from .get_node_types import *
from .get_region_instance_group import *
from .get_region_ssl_certificate import *
from .get_regions import *
from .get_resource_policy import *
from .get_router import *
from .get_ssl_policy import *
from .get_subnetwork import *
from .get_vpn_gateway import *
from .get_zones import *
from .global_address import *
from .global_forwarding_rule import *
from .global_network_endpoint import *
from .global_network_endpoint_group import *
from .ha_vpn_gateway import *
from .health_check import *
from .http_health_check import *
from .https_health_check import *
from .image import *
from .image_iam_binding import *
from .image_iam_member import *
from .image_iam_policy import *
from .instance import *
from .instance_from_machine_image import *
from .instance_from_template import *
from .instance_group import *
from .instance_group_manager import *
from .instance_group_named_port import *
from .instance_iam_binding import *
from .instance_iam_member import *
from .instance_iam_policy import *
from .instance_template import *
from .interconnect_attachment import *
from .machine_image import *
from .machine_image_iam_binding import *
from .machine_image_iam_member import *
from .machine_image_iam_policy import *
from .managed_ssl_certificate import *
from .manged_ssl_certificate import *
from .network import *
from .network_endpoint import *
from .network_endpoint_group import *
from .network_peering import *
from .network_peering_routes_config import *
from .node_group import *
from .node_template import *
from .organization_security_policy import *
from .organization_security_policy_association import *
from .organization_security_policy_rule import *
from .packet_mirroring import *
from .per_instance_config import *
from .project_default_network_tier import *
from .project_metadata import *
from .project_metadata_item import *
from .region_autoscaler import *
from .region_backend_service import *
from .region_disk import *
from .region_disk_iam_binding import *
from .region_disk_iam_member import *
from .region_disk_iam_policy import *
from .region_disk_resource_policy_attachment import *
from .region_health_check import *
from .region_instance_group_manager import *
from .region_network_endpoint_group import *
from .region_per_instance_config import *
from .region_ssl_certificate import *
from .region_target_http_proxy import *
from .region_target_https_proxy import *
from .region_url_map import *
from .reservation import *
from .resource_policy import *
from .route import *
from .router import *
from .router_interface import *
from .router_nat import *
from .router_peer import *
from .security_policy import *
from .security_scan_config import *
from .shared_vpc_host_project import *
from .shared_vpc_service_project import *
from .snapshot import *
from .ssl_certificate import *
from .ssl_policy import *
from .subnetwork import *
from .subnetwork_iam_binding import *
from .subnetwork_iam_member import *
from .subnetwork_iam_policy import *
from .target_grpc_proxy import *
from .target_http_proxy import *
from .target_https_proxy import *
from .target_instance import *
from .target_pool import *
from .target_ssl_proxy import *
from .target_tcp_proxy import *
from .url_map import *
from .vpn_gateway import *
from .vpn_tunnel import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "gcp:compute/address:Address":
                return Address(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/attachedDisk:AttachedDisk":
                return AttachedDisk(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/autoscalar:Autoscalar":
                return Autoscalar(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/autoscaler:Autoscaler":
                return Autoscaler(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/backendBucket:BackendBucket":
                return BackendBucket(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/backendBucketSignedUrlKey:BackendBucketSignedUrlKey":
                return BackendBucketSignedUrlKey(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/backendService:BackendService":
                return BackendService(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/backendServiceSignedUrlKey:BackendServiceSignedUrlKey":
                return BackendServiceSignedUrlKey(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/disk:Disk":
                return Disk(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/diskIamBinding:DiskIamBinding":
                return DiskIamBinding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/diskIamMember:DiskIamMember":
                return DiskIamMember(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/diskIamPolicy:DiskIamPolicy":
                return DiskIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/diskResourcePolicyAttachment:DiskResourcePolicyAttachment":
                return DiskResourcePolicyAttachment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/externalVpnGateway:ExternalVpnGateway":
                return ExternalVpnGateway(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/firewall:Firewall":
                return Firewall(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/forwardingRule:ForwardingRule":
                return ForwardingRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/globalAddress:GlobalAddress":
                return GlobalAddress(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/globalForwardingRule:GlobalForwardingRule":
                return GlobalForwardingRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/globalNetworkEndpoint:GlobalNetworkEndpoint":
                return GlobalNetworkEndpoint(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/globalNetworkEndpointGroup:GlobalNetworkEndpointGroup":
                return GlobalNetworkEndpointGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/haVpnGateway:HaVpnGateway":
                return HaVpnGateway(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/healthCheck:HealthCheck":
                return HealthCheck(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/httpHealthCheck:HttpHealthCheck":
                return HttpHealthCheck(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/httpsHealthCheck:HttpsHealthCheck":
                return HttpsHealthCheck(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/image:Image":
                return Image(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/imageIamBinding:ImageIamBinding":
                return ImageIamBinding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/imageIamMember:ImageIamMember":
                return ImageIamMember(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/imageIamPolicy:ImageIamPolicy":
                return ImageIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/instance:Instance":
                return Instance(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/instanceFromMachineImage:InstanceFromMachineImage":
                return InstanceFromMachineImage(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/instanceFromTemplate:InstanceFromTemplate":
                return InstanceFromTemplate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/instanceGroup:InstanceGroup":
                return InstanceGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/instanceGroupManager:InstanceGroupManager":
                return InstanceGroupManager(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/instanceGroupNamedPort:InstanceGroupNamedPort":
                return InstanceGroupNamedPort(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/instanceIAMBinding:InstanceIAMBinding":
                return InstanceIAMBinding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/instanceIAMMember:InstanceIAMMember":
                return InstanceIAMMember(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/instanceIAMPolicy:InstanceIAMPolicy":
                return InstanceIAMPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/instanceTemplate:InstanceTemplate":
                return InstanceTemplate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/interconnectAttachment:InterconnectAttachment":
                return InterconnectAttachment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/machineImage:MachineImage":
                return MachineImage(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/machineImageIamBinding:MachineImageIamBinding":
                return MachineImageIamBinding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/machineImageIamMember:MachineImageIamMember":
                return MachineImageIamMember(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/machineImageIamPolicy:MachineImageIamPolicy":
                return MachineImageIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/managedSslCertificate:ManagedSslCertificate":
                return ManagedSslCertificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/mangedSslCertificate:MangedSslCertificate":
                return MangedSslCertificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/network:Network":
                return Network(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/networkEndpoint:NetworkEndpoint":
                return NetworkEndpoint(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/networkEndpointGroup:NetworkEndpointGroup":
                return NetworkEndpointGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/networkPeering:NetworkPeering":
                return NetworkPeering(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/networkPeeringRoutesConfig:NetworkPeeringRoutesConfig":
                return NetworkPeeringRoutesConfig(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/nodeGroup:NodeGroup":
                return NodeGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/nodeTemplate:NodeTemplate":
                return NodeTemplate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/organizationSecurityPolicy:OrganizationSecurityPolicy":
                return OrganizationSecurityPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/organizationSecurityPolicyAssociation:OrganizationSecurityPolicyAssociation":
                return OrganizationSecurityPolicyAssociation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/organizationSecurityPolicyRule:OrganizationSecurityPolicyRule":
                return OrganizationSecurityPolicyRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/packetMirroring:PacketMirroring":
                return PacketMirroring(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/perInstanceConfig:PerInstanceConfig":
                return PerInstanceConfig(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/projectDefaultNetworkTier:ProjectDefaultNetworkTier":
                return ProjectDefaultNetworkTier(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/projectMetadata:ProjectMetadata":
                return ProjectMetadata(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/projectMetadataItem:ProjectMetadataItem":
                return ProjectMetadataItem(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/regionAutoscaler:RegionAutoscaler":
                return RegionAutoscaler(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/regionBackendService:RegionBackendService":
                return RegionBackendService(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/regionDisk:RegionDisk":
                return RegionDisk(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/regionDiskIamBinding:RegionDiskIamBinding":
                return RegionDiskIamBinding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/regionDiskIamMember:RegionDiskIamMember":
                return RegionDiskIamMember(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/regionDiskIamPolicy:RegionDiskIamPolicy":
                return RegionDiskIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/regionDiskResourcePolicyAttachment:RegionDiskResourcePolicyAttachment":
                return RegionDiskResourcePolicyAttachment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/regionHealthCheck:RegionHealthCheck":
                return RegionHealthCheck(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/regionInstanceGroupManager:RegionInstanceGroupManager":
                return RegionInstanceGroupManager(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/regionNetworkEndpointGroup:RegionNetworkEndpointGroup":
                return RegionNetworkEndpointGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/regionPerInstanceConfig:RegionPerInstanceConfig":
                return RegionPerInstanceConfig(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/regionSslCertificate:RegionSslCertificate":
                return RegionSslCertificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/regionTargetHttpProxy:RegionTargetHttpProxy":
                return RegionTargetHttpProxy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/regionTargetHttpsProxy:RegionTargetHttpsProxy":
                return RegionTargetHttpsProxy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/regionUrlMap:RegionUrlMap":
                return RegionUrlMap(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/reservation:Reservation":
                return Reservation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/resourcePolicy:ResourcePolicy":
                return ResourcePolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/route:Route":
                return Route(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/router:Router":
                return Router(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/routerInterface:RouterInterface":
                return RouterInterface(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/routerNat:RouterNat":
                return RouterNat(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/routerPeer:RouterPeer":
                return RouterPeer(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/sSLCertificate:SSLCertificate":
                return SSLCertificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/sSLPolicy:SSLPolicy":
                return SSLPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/securityPolicy:SecurityPolicy":
                return SecurityPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/securityScanConfig:SecurityScanConfig":
                return SecurityScanConfig(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/sharedVPCHostProject:SharedVPCHostProject":
                return SharedVPCHostProject(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/sharedVPCServiceProject:SharedVPCServiceProject":
                return SharedVPCServiceProject(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/snapshot:Snapshot":
                return Snapshot(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/subnetwork:Subnetwork":
                return Subnetwork(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/subnetworkIAMBinding:SubnetworkIAMBinding":
                return SubnetworkIAMBinding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/subnetworkIAMMember:SubnetworkIAMMember":
                return SubnetworkIAMMember(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/subnetworkIAMPolicy:SubnetworkIAMPolicy":
                return SubnetworkIAMPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/targetGrpcProxy:TargetGrpcProxy":
                return TargetGrpcProxy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/targetHttpProxy:TargetHttpProxy":
                return TargetHttpProxy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/targetHttpsProxy:TargetHttpsProxy":
                return TargetHttpsProxy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/targetInstance:TargetInstance":
                return TargetInstance(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/targetPool:TargetPool":
                return TargetPool(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/targetSSLProxy:TargetSSLProxy":
                return TargetSSLProxy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/targetTCPProxy:TargetTCPProxy":
                return TargetTCPProxy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/uRLMap:URLMap":
                return URLMap(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/vPNGateway:VPNGateway":
                return VPNGateway(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:compute/vPNTunnel:VPNTunnel":
                return VPNTunnel(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("gcp", "compute/address", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/attachedDisk", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/autoscalar", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/autoscaler", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/backendBucket", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/backendBucketSignedUrlKey", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/backendService", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/backendServiceSignedUrlKey", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/disk", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/diskIamBinding", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/diskIamMember", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/diskIamPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/diskResourcePolicyAttachment", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/externalVpnGateway", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/firewall", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/forwardingRule", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/globalAddress", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/globalForwardingRule", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/globalNetworkEndpoint", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/globalNetworkEndpointGroup", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/haVpnGateway", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/healthCheck", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/httpHealthCheck", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/httpsHealthCheck", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/image", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/imageIamBinding", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/imageIamMember", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/imageIamPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/instance", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/instanceFromMachineImage", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/instanceFromTemplate", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/instanceGroup", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/instanceGroupManager", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/instanceGroupNamedPort", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/instanceIAMBinding", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/instanceIAMMember", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/instanceIAMPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/instanceTemplate", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/interconnectAttachment", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/machineImage", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/machineImageIamBinding", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/machineImageIamMember", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/machineImageIamPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/managedSslCertificate", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/mangedSslCertificate", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/network", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/networkEndpoint", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/networkEndpointGroup", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/networkPeering", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/networkPeeringRoutesConfig", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/nodeGroup", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/nodeTemplate", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/organizationSecurityPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/organizationSecurityPolicyAssociation", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/organizationSecurityPolicyRule", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/packetMirroring", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/perInstanceConfig", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/projectDefaultNetworkTier", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/projectMetadata", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/projectMetadataItem", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/regionAutoscaler", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/regionBackendService", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/regionDisk", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/regionDiskIamBinding", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/regionDiskIamMember", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/regionDiskIamPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/regionDiskResourcePolicyAttachment", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/regionHealthCheck", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/regionInstanceGroupManager", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/regionNetworkEndpointGroup", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/regionPerInstanceConfig", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/regionSslCertificate", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/regionTargetHttpProxy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/regionTargetHttpsProxy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/regionUrlMap", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/reservation", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/resourcePolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/route", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/router", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/routerInterface", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/routerNat", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/routerPeer", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/sSLCertificate", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/sSLPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/securityPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/securityScanConfig", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/sharedVPCHostProject", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/sharedVPCServiceProject", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/snapshot", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/subnetwork", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/subnetworkIAMBinding", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/subnetworkIAMMember", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/subnetworkIAMPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/targetGrpcProxy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/targetHttpProxy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/targetHttpsProxy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/targetInstance", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/targetPool", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/targetSSLProxy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/targetTCPProxy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/uRLMap", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/vPNGateway", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "compute/vPNTunnel", _module_instance)

_register_module()
