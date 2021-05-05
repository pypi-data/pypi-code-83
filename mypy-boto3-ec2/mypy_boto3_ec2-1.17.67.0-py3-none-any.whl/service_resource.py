"""
Type annotations for ec2 service ServiceResource

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_ec2 import EC2ServiceResource
    import mypy_boto3_ec2.service_resource as ec2_resources

    resource: EC2ServiceResource = boto3.resource("ec2")

    my_classic_address: ec2_resources.ClassicAddress = resource.ClassicAddress(...)
    my_dhcp_options: ec2_resources.DhcpOptions = resource.DhcpOptions(...)
    my_image: ec2_resources.Image = resource.Image(...)
    my_instance: ec2_resources.Instance = resource.Instance(...)
    my_internet_gateway: ec2_resources.InternetGateway = resource.InternetGateway(...)
    my_key_pair: ec2_resources.KeyPair = resource.KeyPair(...)
    my_key_pair_info: ec2_resources.KeyPairInfo = resource.KeyPairInfo(...)
    my_network_acl: ec2_resources.NetworkAcl = resource.NetworkAcl(...)
    my_network_interface: ec2_resources.NetworkInterface = resource.NetworkInterface(...)
    my_network_interface_association: ec2_resources.NetworkInterfaceAssociation = resource.NetworkInterfaceAssociation(...)
    my_placement_group: ec2_resources.PlacementGroup = resource.PlacementGroup(...)
    my_route: ec2_resources.Route = resource.Route(...)
    my_route_table: ec2_resources.RouteTable = resource.RouteTable(...)
    my_route_table_association: ec2_resources.RouteTableAssociation = resource.RouteTableAssociation(...)
    my_security_group: ec2_resources.SecurityGroup = resource.SecurityGroup(...)
    my_snapshot: ec2_resources.Snapshot = resource.Snapshot(...)
    my_subnet: ec2_resources.Subnet = resource.Subnet(...)
    my_tag: ec2_resources.Tag = resource.Tag(...)
    my_volume: ec2_resources.Volume = resource.Volume(...)
    my_vpc: ec2_resources.Vpc = resource.Vpc(...)
    my_vpc_peering_connection: ec2_resources.VpcPeeringConnection = resource.VpcPeeringConnection(...)
    my_vpc_address: ec2_resources.VpcAddress = resource.VpcAddress(...)
```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, Iterator, List, Optional, Union

from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection

from mypy_boto3_ec2.literals import (
    ArchitectureValues,
    BootModeValues,
    ImageAttributeName,
    InstanceAttributeName,
    InstanceType,
    NetworkInterfaceAttribute,
    OperationType,
    PlacementStrategy,
    ReportInstanceReasonCodes,
    ReportStatusType,
    RuleAction,
    ShutdownBehavior,
    SnapshotAttributeName,
    Tenancy,
    VolumeAttributeName,
    VolumeType,
    VpcAttributeName,
)
from mypy_boto3_ec2.type_defs import (
    AcceptVpcPeeringConnectionResultTypeDef,
    AssignPrivateIpAddressesResultTypeDef,
    AssociateAddressResultTypeDef,
    AttachClassicLinkVpcResultTypeDef,
    AttachNetworkInterfaceResultTypeDef,
    AttributeBooleanValueTypeDef,
    AttributeValueTypeDef,
    BlobAttributeValueTypeDef,
    BlockDeviceMappingTypeDef,
    CapacityReservationSpecificationTypeDef,
    CopySnapshotResultTypeDef,
    CpuOptionsRequestTypeDef,
    CreateVolumePermissionModificationsTypeDef,
    CreditSpecificationRequestTypeDef,
    DeleteVpcPeeringConnectionResultTypeDef,
    DescribeNetworkInterfaceAttributeResultTypeDef,
    DescribeSnapshotAttributeResultTypeDef,
    DescribeVolumeAttributeResultTypeDef,
    DescribeVolumeStatusResultTypeDef,
    DescribeVpcAttributeResultTypeDef,
    DetachClassicLinkVpcResultTypeDef,
    DisableVpcClassicLinkResultTypeDef,
    ElasticGpuSpecificationTypeDef,
    ElasticInferenceAcceleratorTypeDef,
    EnableVpcClassicLinkResultTypeDef,
    EnclaveOptionsRequestTypeDef,
    FilterTypeDef,
    GetConsoleOutputResultTypeDef,
    GetPasswordDataResultTypeDef,
    HibernationOptionsRequestTypeDef,
    IamInstanceProfileSpecificationTypeDef,
    IcmpTypeCodeTypeDef,
    ImageAttributeTypeDef,
    InstanceAttributeTypeDef,
    InstanceBlockDeviceMappingSpecificationTypeDef,
    InstanceIpv6AddressTypeDef,
    InstanceMarketOptionsRequestTypeDef,
    InstanceMetadataOptionsRequestTypeDef,
    InstanceNetworkInterfaceSpecificationTypeDef,
    IpPermissionTypeDef,
    LaunchPermissionModificationsTypeDef,
    LaunchTemplateSpecificationTypeDef,
    LicenseConfigurationRequestTypeDef,
    MonitorInstancesResultTypeDef,
    NetworkInterfaceAttachmentChangesTypeDef,
    NewDhcpConfigurationTypeDef,
    PlacementTypeDef,
    PortRangeTypeDef,
    PrivateIpAddressSpecificationTypeDef,
    RejectVpcPeeringConnectionResultTypeDef,
    ReplaceNetworkAclAssociationResultTypeDef,
    RevokeSecurityGroupEgressResultTypeDef,
    RevokeSecurityGroupIngressResultTypeDef,
    RunInstancesMonitoringEnabledTypeDef,
    StartInstancesResultTypeDef,
    StopInstancesResultTypeDef,
    TagSpecificationTypeDef,
    TagTypeDef,
    TerminateInstancesResultTypeDef,
    UnmonitorInstancesResultTypeDef,
    VolumeAttachmentTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "EC2ServiceResource",
    "ClassicAddress",
    "DhcpOptions",
    "Image",
    "Instance",
    "InternetGateway",
    "KeyPair",
    "KeyPairInfo",
    "NetworkAcl",
    "NetworkInterface",
    "NetworkInterfaceAssociation",
    "PlacementGroup",
    "Route",
    "RouteTable",
    "RouteTableAssociation",
    "SecurityGroup",
    "Snapshot",
    "Subnet",
    "Tag",
    "Volume",
    "Vpc",
    "VpcPeeringConnection",
    "VpcAddress",
    "ServiceResourceClassicAddressesCollection",
    "ServiceResourceDhcpOptionsSetsCollection",
    "ServiceResourceImagesCollection",
    "ServiceResourceInstancesCollection",
    "ServiceResourceInternetGatewaysCollection",
    "ServiceResourceKeyPairsCollection",
    "ServiceResourceNetworkAclsCollection",
    "ServiceResourceNetworkInterfacesCollection",
    "ServiceResourcePlacementGroupsCollection",
    "ServiceResourceRouteTablesCollection",
    "ServiceResourceSecurityGroupsCollection",
    "ServiceResourceSnapshotsCollection",
    "ServiceResourceSubnetsCollection",
    "ServiceResourceVolumesCollection",
    "ServiceResourceVpcAddressesCollection",
    "ServiceResourceVpcPeeringConnectionsCollection",
    "ServiceResourceVpcsCollection",
    "InstanceVolumesCollection",
    "InstanceVpcAddressesCollection",
    "PlacementGroupInstancesCollection",
    "SubnetInstancesCollection",
    "SubnetNetworkInterfacesCollection",
    "VolumeSnapshotsCollection",
    "VpcAcceptedVpcPeeringConnectionsCollection",
    "VpcInstancesCollection",
    "VpcInternetGatewaysCollection",
    "VpcNetworkAclsCollection",
    "VpcNetworkInterfacesCollection",
    "VpcRequestedVpcPeeringConnectionsCollection",
    "VpcRouteTablesCollection",
    "VpcSecurityGroupsCollection",
    "VpcSubnetsCollection",
)


class ServiceResourceClassicAddressesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.classic_addresses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourceclassicaddressescollection)
    """

    def all(self) -> "ServiceResourceClassicAddressesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        PublicIps: List[str] = None,
        AllocationIds: List[str] = None,
        DryRun: bool = None,
    ) -> "ServiceResourceClassicAddressesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceClassicAddressesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceClassicAddressesCollection":
        pass

    def pages(self) -> Iterator[List["ClassicAddress"]]:
        pass

    def __iter__(self) -> Iterator["ClassicAddress"]:
        pass


class ServiceResourceDhcpOptionsSetsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.dhcp_options_sets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcedhcpoptionssetscollection)
    """

    def all(self) -> "ServiceResourceDhcpOptionsSetsCollection":
        pass

    def filter(  # type: ignore
        self,
        DhcpOptionsIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "ServiceResourceDhcpOptionsSetsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceDhcpOptionsSetsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceDhcpOptionsSetsCollection":
        pass

    def pages(self) -> Iterator[List["DhcpOptions"]]:
        pass

    def __iter__(self) -> Iterator["DhcpOptions"]:
        pass


class ServiceResourceImagesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.images)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourceimagescollection)
    """

    def all(self) -> "ServiceResourceImagesCollection":
        pass

    def filter(  # type: ignore
        self,
        ExecutableUsers: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        ImageIds: List[str] = None,
        Owners: List[str] = None,
        DryRun: bool = None,
    ) -> "ServiceResourceImagesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceImagesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceImagesCollection":
        pass

    def pages(self) -> Iterator[List["Image"]]:
        pass

    def __iter__(self) -> Iterator["Image"]:
        pass


class ServiceResourceInstancesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.instances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourceinstancescollection)
    """

    def all(self) -> "ServiceResourceInstancesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> "ServiceResourceInstancesCollection":
        pass

    def create_tags(self, DryRun: bool = None) -> None:
        pass

    def monitor(self, DryRun: bool = None) -> MonitorInstancesResultTypeDef:
        pass

    def reboot(self, DryRun: bool = None) -> None:
        pass

    def start(self, AdditionalInfo: str = None, DryRun: bool = None) -> StartInstancesResultTypeDef:
        pass

    def stop(
        self, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> StopInstancesResultTypeDef:
        pass

    def terminate(self, DryRun: bool = None) -> TerminateInstancesResultTypeDef:
        pass

    def unmonitor(self, DryRun: bool = None) -> UnmonitorInstancesResultTypeDef:
        pass

    def limit(self, count: int) -> "ServiceResourceInstancesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceInstancesCollection":
        pass

    def pages(self) -> Iterator[List["Instance"]]:
        pass

    def __iter__(self) -> Iterator["Instance"]:
        pass


class ServiceResourceInternetGatewaysCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.internet_gateways)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourceinternetgatewayscollection)
    """

    def all(self) -> "ServiceResourceInternetGatewaysCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "ServiceResourceInternetGatewaysCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceInternetGatewaysCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceInternetGatewaysCollection":
        pass

    def pages(self) -> Iterator[List["InternetGateway"]]:
        pass

    def __iter__(self) -> Iterator["InternetGateway"]:
        pass


class ServiceResourceKeyPairsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.key_pairs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcekeypairscollection)
    """

    def all(self) -> "ServiceResourceKeyPairsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        KeyNames: List[str] = None,
        KeyPairIds: List[str] = None,
        DryRun: bool = None,
    ) -> "ServiceResourceKeyPairsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceKeyPairsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceKeyPairsCollection":
        pass

    def pages(self) -> Iterator[List["KeyPairInfo"]]:
        pass

    def __iter__(self) -> Iterator["KeyPairInfo"]:
        pass


class ServiceResourceNetworkAclsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.network_acls)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcenetworkaclscollection)
    """

    def all(self) -> "ServiceResourceNetworkAclsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "ServiceResourceNetworkAclsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceNetworkAclsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceNetworkAclsCollection":
        pass

    def pages(self) -> Iterator[List["NetworkAcl"]]:
        pass

    def __iter__(self) -> Iterator["NetworkAcl"]:
        pass


class ServiceResourceNetworkInterfacesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.network_interfaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcenetworkinterfacescollection)
    """

    def all(self) -> "ServiceResourceNetworkInterfacesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "ServiceResourceNetworkInterfacesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceNetworkInterfacesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceNetworkInterfacesCollection":
        pass

    def pages(self) -> Iterator[List["NetworkInterface"]]:
        pass

    def __iter__(self) -> Iterator["NetworkInterface"]:
        pass


class ServiceResourcePlacementGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.placement_groups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourceplacementgroupscollection)
    """

    def all(self) -> "ServiceResourcePlacementGroupsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        GroupNames: List[str] = None,
        GroupIds: List[str] = None,
    ) -> "ServiceResourcePlacementGroupsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourcePlacementGroupsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourcePlacementGroupsCollection":
        pass

    def pages(self) -> Iterator[List["PlacementGroup"]]:
        pass

    def __iter__(self) -> Iterator["PlacementGroup"]:
        pass


class ServiceResourceRouteTablesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.route_tables)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourceroutetablescollection)
    """

    def all(self) -> "ServiceResourceRouteTablesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "ServiceResourceRouteTablesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceRouteTablesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceRouteTablesCollection":
        pass

    def pages(self) -> Iterator[List["RouteTable"]]:
        pass

    def __iter__(self) -> Iterator["RouteTable"]:
        pass


class ServiceResourceSecurityGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.security_groups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcesecuritygroupscollection)
    """

    def all(self) -> "ServiceResourceSecurityGroupsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "ServiceResourceSecurityGroupsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceSecurityGroupsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceSecurityGroupsCollection":
        pass

    def pages(self) -> Iterator[List["SecurityGroup"]]:
        pass

    def __iter__(self) -> Iterator["SecurityGroup"]:
        pass


class ServiceResourceSnapshotsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.snapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcesnapshotscollection)
    """

    def all(self) -> "ServiceResourceSnapshotsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
    ) -> "ServiceResourceSnapshotsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceSnapshotsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceSnapshotsCollection":
        pass

    def pages(self) -> Iterator[List["Snapshot"]]:
        pass

    def __iter__(self) -> Iterator["Snapshot"]:
        pass


class ServiceResourceSubnetsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.subnets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcesubnetscollection)
    """

    def all(self) -> "ServiceResourceSubnetsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "ServiceResourceSubnetsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceSubnetsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceSubnetsCollection":
        pass

    def pages(self) -> Iterator[List["Subnet"]]:
        pass

    def __iter__(self) -> Iterator["Subnet"]:
        pass


class ServiceResourceVolumesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.volumes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcevolumescollection)
    """

    def all(self) -> "ServiceResourceVolumesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> "ServiceResourceVolumesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceVolumesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceVolumesCollection":
        pass

    def pages(self) -> Iterator[List["Volume"]]:
        pass

    def __iter__(self) -> Iterator["Volume"]:
        pass


class ServiceResourceVpcAddressesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.vpc_addresses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcevpcaddressescollection)
    """

    def all(self) -> "ServiceResourceVpcAddressesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        PublicIps: List[str] = None,
        AllocationIds: List[str] = None,
        DryRun: bool = None,
    ) -> "ServiceResourceVpcAddressesCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceVpcAddressesCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceVpcAddressesCollection":
        pass

    def pages(self) -> Iterator[List["VpcAddress"]]:
        pass

    def __iter__(self) -> Iterator["VpcAddress"]:
        pass


class ServiceResourceVpcPeeringConnectionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.vpc_peering_connections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcevpcpeeringconnectionscollection)
    """

    def all(self) -> "ServiceResourceVpcPeeringConnectionsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "ServiceResourceVpcPeeringConnectionsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceVpcPeeringConnectionsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceVpcPeeringConnectionsCollection":
        pass

    def pages(self) -> Iterator[List["VpcPeeringConnection"]]:
        pass

    def __iter__(self) -> Iterator["VpcPeeringConnection"]:
        pass


class ServiceResourceVpcsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.vpcs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#serviceresourcevpcscollection)
    """

    def all(self) -> "ServiceResourceVpcsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "ServiceResourceVpcsCollection":
        pass

    def limit(self, count: int) -> "ServiceResourceVpcsCollection":
        pass

    def page_size(self, count: int) -> "ServiceResourceVpcsCollection":
        pass

    def pages(self) -> Iterator[List["Vpc"]]:
        pass

    def __iter__(self) -> Iterator["Vpc"]:
        pass


class InstanceVolumesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.volumes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancevolumescollection)
    """

    def all(self) -> "InstanceVolumesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> "InstanceVolumesCollection":
        pass

    def limit(self, count: int) -> "InstanceVolumesCollection":
        pass

    def page_size(self, count: int) -> "InstanceVolumesCollection":
        pass

    def pages(self) -> Iterator[List["Volume"]]:
        pass

    def __iter__(self) -> Iterator["Volume"]:
        pass


class InstanceVpcAddressesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.vpc_addresses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancevpcaddressescollection)
    """

    def all(self) -> "InstanceVpcAddressesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        PublicIps: List[str] = None,
        AllocationIds: List[str] = None,
        DryRun: bool = None,
    ) -> "InstanceVpcAddressesCollection":
        pass

    def limit(self, count: int) -> "InstanceVpcAddressesCollection":
        pass

    def page_size(self, count: int) -> "InstanceVpcAddressesCollection":
        pass

    def pages(self) -> Iterator[List["VpcAddress"]]:
        pass

    def __iter__(self) -> Iterator["VpcAddress"]:
        pass


class PlacementGroupInstancesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.PlacementGroup.instances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#placementgroupinstancescollection)
    """

    def all(self) -> "PlacementGroupInstancesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> "PlacementGroupInstancesCollection":
        pass

    def create_tags(self, DryRun: bool = None) -> None:
        pass

    def monitor(self, DryRun: bool = None) -> MonitorInstancesResultTypeDef:
        pass

    def reboot(self, DryRun: bool = None) -> None:
        pass

    def start(self, AdditionalInfo: str = None, DryRun: bool = None) -> StartInstancesResultTypeDef:
        pass

    def stop(
        self, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> StopInstancesResultTypeDef:
        pass

    def terminate(self, DryRun: bool = None) -> TerminateInstancesResultTypeDef:
        pass

    def unmonitor(self, DryRun: bool = None) -> UnmonitorInstancesResultTypeDef:
        pass

    def limit(self, count: int) -> "PlacementGroupInstancesCollection":
        pass

    def page_size(self, count: int) -> "PlacementGroupInstancesCollection":
        pass

    def pages(self) -> Iterator[List["Instance"]]:
        pass

    def __iter__(self) -> Iterator["Instance"]:
        pass


class SubnetInstancesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Subnet.instances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetinstancescollection)
    """

    def all(self) -> "SubnetInstancesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> "SubnetInstancesCollection":
        pass

    def create_tags(self, DryRun: bool = None) -> None:
        pass

    def monitor(self, DryRun: bool = None) -> MonitorInstancesResultTypeDef:
        pass

    def reboot(self, DryRun: bool = None) -> None:
        pass

    def start(self, AdditionalInfo: str = None, DryRun: bool = None) -> StartInstancesResultTypeDef:
        pass

    def stop(
        self, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> StopInstancesResultTypeDef:
        pass

    def terminate(self, DryRun: bool = None) -> TerminateInstancesResultTypeDef:
        pass

    def unmonitor(self, DryRun: bool = None) -> UnmonitorInstancesResultTypeDef:
        pass

    def limit(self, count: int) -> "SubnetInstancesCollection":
        pass

    def page_size(self, count: int) -> "SubnetInstancesCollection":
        pass

    def pages(self) -> Iterator[List["Instance"]]:
        pass

    def __iter__(self) -> Iterator["Instance"]:
        pass


class SubnetNetworkInterfacesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Subnet.network_interfaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetnetworkinterfacescollection)
    """

    def all(self) -> "SubnetNetworkInterfacesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "SubnetNetworkInterfacesCollection":
        pass

    def limit(self, count: int) -> "SubnetNetworkInterfacesCollection":
        pass

    def page_size(self, count: int) -> "SubnetNetworkInterfacesCollection":
        pass

    def pages(self) -> Iterator[List["NetworkInterface"]]:
        pass

    def __iter__(self) -> Iterator["NetworkInterface"]:
        pass


class VolumeSnapshotsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Volume.snapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumesnapshotscollection)
    """

    def all(self) -> "VolumeSnapshotsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
    ) -> "VolumeSnapshotsCollection":
        pass

    def limit(self, count: int) -> "VolumeSnapshotsCollection":
        pass

    def page_size(self, count: int) -> "VolumeSnapshotsCollection":
        pass

    def pages(self) -> Iterator[List["Snapshot"]]:
        pass

    def __iter__(self) -> Iterator["Snapshot"]:
        pass


class VpcAcceptedVpcPeeringConnectionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.accepted_vpc_peering_connections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcacceptedvpcpeeringconnectionscollection)
    """

    def all(self) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        pass

    def limit(self, count: int) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        pass

    def page_size(self, count: int) -> "VpcAcceptedVpcPeeringConnectionsCollection":
        pass

    def pages(self) -> Iterator[List["VpcPeeringConnection"]]:
        pass

    def __iter__(self) -> Iterator["VpcPeeringConnection"]:
        pass


class VpcInstancesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.instances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcinstancescollection)
    """

    def all(self) -> "VpcInstancesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> "VpcInstancesCollection":
        pass

    def create_tags(self, DryRun: bool = None) -> None:
        pass

    def monitor(self, DryRun: bool = None) -> MonitorInstancesResultTypeDef:
        pass

    def reboot(self, DryRun: bool = None) -> None:
        pass

    def start(self, AdditionalInfo: str = None, DryRun: bool = None) -> StartInstancesResultTypeDef:
        pass

    def stop(
        self, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> StopInstancesResultTypeDef:
        pass

    def terminate(self, DryRun: bool = None) -> TerminateInstancesResultTypeDef:
        pass

    def unmonitor(self, DryRun: bool = None) -> UnmonitorInstancesResultTypeDef:
        pass

    def limit(self, count: int) -> "VpcInstancesCollection":
        pass

    def page_size(self, count: int) -> "VpcInstancesCollection":
        pass

    def pages(self) -> Iterator[List["Instance"]]:
        pass

    def __iter__(self) -> Iterator["Instance"]:
        pass


class VpcInternetGatewaysCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.internet_gateways)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcinternetgatewayscollection)
    """

    def all(self) -> "VpcInternetGatewaysCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "VpcInternetGatewaysCollection":
        pass

    def limit(self, count: int) -> "VpcInternetGatewaysCollection":
        pass

    def page_size(self, count: int) -> "VpcInternetGatewaysCollection":
        pass

    def pages(self) -> Iterator[List["InternetGateway"]]:
        pass

    def __iter__(self) -> Iterator["InternetGateway"]:
        pass


class VpcNetworkAclsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.network_acls)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcnetworkaclscollection)
    """

    def all(self) -> "VpcNetworkAclsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "VpcNetworkAclsCollection":
        pass

    def limit(self, count: int) -> "VpcNetworkAclsCollection":
        pass

    def page_size(self, count: int) -> "VpcNetworkAclsCollection":
        pass

    def pages(self) -> Iterator[List["NetworkAcl"]]:
        pass

    def __iter__(self) -> Iterator["NetworkAcl"]:
        pass


class VpcNetworkInterfacesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.network_interfaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcnetworkinterfacescollection)
    """

    def all(self) -> "VpcNetworkInterfacesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "VpcNetworkInterfacesCollection":
        pass

    def limit(self, count: int) -> "VpcNetworkInterfacesCollection":
        pass

    def page_size(self, count: int) -> "VpcNetworkInterfacesCollection":
        pass

    def pages(self) -> Iterator[List["NetworkInterface"]]:
        pass

    def __iter__(self) -> Iterator["NetworkInterface"]:
        pass


class VpcRequestedVpcPeeringConnectionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.requested_vpc_peering_connections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcrequestedvpcpeeringconnectionscollection)
    """

    def all(self) -> "VpcRequestedVpcPeeringConnectionsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "VpcRequestedVpcPeeringConnectionsCollection":
        pass

    def limit(self, count: int) -> "VpcRequestedVpcPeeringConnectionsCollection":
        pass

    def page_size(self, count: int) -> "VpcRequestedVpcPeeringConnectionsCollection":
        pass

    def pages(self) -> Iterator[List["VpcPeeringConnection"]]:
        pass

    def __iter__(self) -> Iterator["VpcPeeringConnection"]:
        pass


class VpcRouteTablesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.route_tables)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcroutetablescollection)
    """

    def all(self) -> "VpcRouteTablesCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "VpcRouteTablesCollection":
        pass

    def limit(self, count: int) -> "VpcRouteTablesCollection":
        pass

    def page_size(self, count: int) -> "VpcRouteTablesCollection":
        pass

    def pages(self) -> Iterator[List["RouteTable"]]:
        pass

    def __iter__(self) -> Iterator["RouteTable"]:
        pass


class VpcSecurityGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.security_groups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcsecuritygroupscollection)
    """

    def all(self) -> "VpcSecurityGroupsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "VpcSecurityGroupsCollection":
        pass

    def limit(self, count: int) -> "VpcSecurityGroupsCollection":
        pass

    def page_size(self, count: int) -> "VpcSecurityGroupsCollection":
        pass

    def pages(self) -> Iterator[List["SecurityGroup"]]:
        pass

    def __iter__(self) -> Iterator["SecurityGroup"]:
        pass


class VpcSubnetsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.subnets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcsubnetscollection)
    """

    def all(self) -> "VpcSubnetsCollection":
        pass

    def filter(  # type: ignore
        self,
        Filters: List[FilterTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> "VpcSubnetsCollection":
        pass

    def limit(self, count: int) -> "VpcSubnetsCollection":
        pass

    def page_size(self, count: int) -> "VpcSubnetsCollection":
        pass

    def pages(self) -> Iterator[List["Subnet"]]:
        pass

    def __iter__(self) -> Iterator["Subnet"]:
        pass


class ClassicAddress(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.ClassicAddress)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#classicaddress)
    """

    instance_id: str
    allocation_id: str
    association_id: str
    domain: str
    network_interface_id: str
    network_interface_owner_id: str
    private_ip_address: str
    tags: List[Any]
    public_ipv4_pool: str
    network_border_group: str
    customer_owned_ip: str
    customer_owned_ipv4_pool: str
    carrier_ip: str
    public_ip: str

    def associate(
        self,
        AllocationId: str = None,
        InstanceId: str = None,
        AllowReassociation: bool = None,
        DryRun: bool = None,
        NetworkInterfaceId: str = None,
        PrivateIpAddress: str = None,
    ) -> AssociateAddressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ClassicAddress.associate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#classicaddressassociatemethod)
        """

    def disassociate(
        self, AssociationId: str = None, PublicIp: str = None, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ClassicAddress.disassociate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#classicaddressdisassociatemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ClassicAddress.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#classicaddressget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ClassicAddress.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#classicaddressloadmethod)
        """

    def release(
        self,
        AllocationId: str = None,
        PublicIp: str = None,
        NetworkBorderGroup: str = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ClassicAddress.release)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#classicaddressreleasemethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ClassicAddress.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#classicaddressreloadmethod)
        """


_ClassicAddress = ClassicAddress


class KeyPair(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.KeyPair)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypair)
    """

    key_fingerprint: str
    key_material: str
    key_name: str
    key_pair_id: str
    tags: List[Any]
    name: str

    def delete(self, KeyPairId: str = None, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.KeyPair.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypairdeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.KeyPair.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypairget-available-subresourcesmethod)
        """


_KeyPair = KeyPair


class KeyPairInfo(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.KeyPairInfo)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypairinfo)
    """

    key_pair_id: str
    key_fingerprint: str
    key_name: str
    tags: List[Any]
    name: str

    def delete(self, KeyPairId: str = None, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.KeyPairInfo.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypairinfodeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.KeyPairInfo.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypairinfoget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.KeyPairInfo.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypairinfoloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.KeyPairInfo.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#keypairinforeloadmethod)
        """


_KeyPairInfo = KeyPairInfo


class NetworkInterfaceAssociation(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.NetworkInterfaceAssociation)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceassociation)
    """

    carrier_ip: str
    ip_owner_id: str
    public_dns_name: str
    public_ip: str
    id: str
    address: "VpcAddress"

    def delete(self, PublicIp: str = None, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceassociationdeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceassociationget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceassociationloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterfaceAssociation.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceassociationreloadmethod)
        """


_NetworkInterfaceAssociation = NetworkInterfaceAssociation


class PlacementGroup(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.PlacementGroup)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#placementgroup)
    """

    group_name: str
    state: str
    strategy: str
    partition_count: int
    group_id: str
    tags: List[Any]
    name: str
    instances: PlacementGroupInstancesCollection

    def delete(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.PlacementGroup.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#placementgroupdeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.PlacementGroup.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#placementgroupget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.PlacementGroup.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#placementgrouploadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.PlacementGroup.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#placementgroupreloadmethod)
        """


_PlacementGroup = PlacementGroup


class Tag(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Tag)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#tag)
    """

    resource_type: str
    resource_id: str
    key: str
    value: str

    def delete(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Tag.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#tagdeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Tag.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#tagget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Tag.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#tagloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Tag.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#tagreloadmethod)
        """


_Tag = Tag


class VpcPeeringConnection(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.VpcPeeringConnection)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnection)
    """

    accepter_vpc_info: Dict[str, Any]
    expiration_time: datetime
    requester_vpc_info: Dict[str, Any]
    status: Dict[str, Any]
    tags: List[Any]
    vpc_peering_connection_id: str
    id: str
    accepter_vpc: "Vpc"
    requester_vpc: "Vpc"

    def accept(self, DryRun: bool = None) -> AcceptVpcPeeringConnectionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.VpcPeeringConnection.accept)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnectionacceptmethod)
        """

    def delete(self, DryRun: bool = None) -> DeleteVpcPeeringConnectionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.VpcPeeringConnection.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnectiondeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.VpcPeeringConnection.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnectionget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.VpcPeeringConnection.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnectionloadmethod)
        """

    def reject(self, DryRun: bool = None) -> RejectVpcPeeringConnectionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.VpcPeeringConnection.reject)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnectionrejectmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.VpcPeeringConnection.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnectionreloadmethod)
        """

    def wait_until_exists(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.VpcPeeringConnection.wait_until_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcpeeringconnectionwait-until-existsmethod)
        """


_VpcPeeringConnection = VpcPeeringConnection


class VpcAddress(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.VpcAddress)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcaddress)
    """

    instance_id: str
    public_ip: str
    association_id: str
    domain: str
    network_interface_id: str
    network_interface_owner_id: str
    private_ip_address: str
    tags: List[Any]
    public_ipv4_pool: str
    network_border_group: str
    customer_owned_ip: str
    customer_owned_ipv4_pool: str
    carrier_ip: str
    allocation_id: str
    association: "NetworkInterfaceAssociation"

    def associate(
        self,
        InstanceId: str = None,
        PublicIp: str = None,
        AllowReassociation: bool = None,
        DryRun: bool = None,
        NetworkInterfaceId: str = None,
        PrivateIpAddress: str = None,
    ) -> AssociateAddressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.VpcAddress.associate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcaddressassociatemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.VpcAddress.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcaddressget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.VpcAddress.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcaddressloadmethod)
        """

    def release(
        self,
        AllocationId: str = None,
        PublicIp: str = None,
        NetworkBorderGroup: str = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.VpcAddress.release)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcaddressreleasemethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.VpcAddress.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcaddressreloadmethod)
        """


_VpcAddress = VpcAddress


class DhcpOptions(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.DhcpOptions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#dhcpoptions)
    """

    dhcp_configurations: List[Any]
    dhcp_options_id: str
    owner_id: str
    tags: List[Any]
    id: str

    def associate_with_vpc(self, VpcId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.DhcpOptions.associate_with_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#dhcpoptionsassociate-with-vpcmethod)
        """

    def create_tags(self, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.DhcpOptions.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#dhcpoptionscreate-tagsmethod)
        """

    def delete(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.DhcpOptions.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#dhcpoptionsdeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.DhcpOptions.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#dhcpoptionsget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.DhcpOptions.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#dhcpoptionsloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.DhcpOptions.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#dhcpoptionsreloadmethod)
        """


_DhcpOptions = DhcpOptions


class Image(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Image)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#image)
    """

    architecture: str
    creation_date: str
    image_id: str
    image_location: str
    image_type: str
    public: bool
    kernel_id: str
    owner_id: str
    platform: str
    platform_details: str
    usage_operation: str
    product_codes: List[Any]
    ramdisk_id: str
    state: str
    block_device_mappings: List[Any]
    description: str
    ena_support: bool
    hypervisor: str
    image_owner_alias: str
    name: str
    root_device_name: str
    root_device_type: str
    sriov_net_support: str
    state_reason: Dict[str, Any]
    tags: List[Any]
    virtualization_type: str
    boot_mode: str
    id: str

    def create_tags(self, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Image.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imagecreate-tagsmethod)
        """

    def deregister(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Image.deregister)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imagederegistermethod)
        """

    def describe_attribute(
        self, Attribute: ImageAttributeName, DryRun: bool = None
    ) -> ImageAttributeTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Image.describe_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imagedescribe-attributemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Image.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imageget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Image.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imageloadmethod)
        """

    def modify_attribute(
        self,
        Attribute: str = None,
        Description: "AttributeValueTypeDef" = None,
        LaunchPermission: LaunchPermissionModificationsTypeDef = None,
        OperationType: OperationType = None,
        ProductCodes: List[str] = None,
        UserGroups: List[str] = None,
        UserIds: List[str] = None,
        Value: str = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Image.modify_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imagemodify-attributemethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Image.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imagereloadmethod)
        """

    def reset_attribute(self, Attribute: Literal["launchPermission"], DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Image.reset_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imagereset-attributemethod)
        """

    def wait_until_exists(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Image.wait_until_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#imagewait-until-existsmethod)
        """


_Image = Image


class InternetGateway(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.InternetGateway)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgateway)
    """

    attachments: List[Any]
    internet_gateway_id: str
    owner_id: str
    tags: List[Any]
    id: str

    def attach_to_vpc(self, VpcId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.InternetGateway.attach_to_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgatewayattach-to-vpcmethod)
        """

    def create_tags(self, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.InternetGateway.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgatewaycreate-tagsmethod)
        """

    def delete(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.InternetGateway.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgatewaydeletemethod)
        """

    def detach_from_vpc(self, VpcId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.InternetGateway.detach_from_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgatewaydetach-from-vpcmethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.InternetGateway.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgatewayget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.InternetGateway.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgatewayloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.InternetGateway.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#internetgatewayreloadmethod)
        """


_InternetGateway = InternetGateway


class NetworkAcl(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.NetworkAcl)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkacl)
    """

    associations: List[Any]
    entries: List[Any]
    is_default: bool
    network_acl_id: str
    tags: List[Any]
    vpc_id: str
    owner_id: str
    id: str
    vpc: "Vpc"

    def create_entry(
        self,
        Egress: bool,
        Protocol: str,
        RuleAction: RuleAction,
        RuleNumber: int,
        CidrBlock: str = None,
        DryRun: bool = None,
        IcmpTypeCode: "IcmpTypeCodeTypeDef" = None,
        Ipv6CidrBlock: str = None,
        PortRange: "PortRangeTypeDef" = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkAcl.create_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkaclcreate-entrymethod)
        """

    def create_tags(self, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkAcl.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkaclcreate-tagsmethod)
        """

    def delete(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkAcl.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkacldeletemethod)
        """

    def delete_entry(self, Egress: bool, RuleNumber: int, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkAcl.delete_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkacldelete-entrymethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkAcl.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkaclget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkAcl.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkaclloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkAcl.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkaclreloadmethod)
        """

    def replace_association(
        self, AssociationId: str, DryRun: bool = None
    ) -> ReplaceNetworkAclAssociationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkAcl.replace_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkaclreplace-associationmethod)
        """

    def replace_entry(
        self,
        Egress: bool,
        Protocol: str,
        RuleAction: RuleAction,
        RuleNumber: int,
        CidrBlock: str = None,
        DryRun: bool = None,
        IcmpTypeCode: "IcmpTypeCodeTypeDef" = None,
        Ipv6CidrBlock: str = None,
        PortRange: "PortRangeTypeDef" = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkAcl.replace_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkaclreplace-entrymethod)
        """


_NetworkAcl = NetworkAcl


class NetworkInterface(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.NetworkInterface)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterface)
    """

    association_attribute: Dict[str, Any]
    attachment: Dict[str, Any]
    availability_zone: str
    description: str
    groups: List[Any]
    interface_type: str
    ipv6_addresses: List[Any]
    mac_address: str
    network_interface_id: str
    outpost_arn: str
    owner_id: str
    private_dns_name: str
    private_ip_address: str
    private_ip_addresses: List[Any]
    requester_id: str
    requester_managed: bool
    source_dest_check: bool
    status: str
    subnet_id: str
    tag_set: List[Any]
    vpc_id: str
    id: str
    association: "NetworkInterfaceAssociation"
    subnet: "Subnet"
    vpc: "Vpc"

    def assign_private_ip_addresses(
        self,
        AllowReassignment: bool = None,
        PrivateIpAddresses: List[str] = None,
        SecondaryPrivateIpAddressCount: int = None,
    ) -> AssignPrivateIpAddressesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterface.assign_private_ip_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceassign-private-ip-addressesmethod)
        """

    def attach(
        self, DeviceIndex: int, InstanceId: str, DryRun: bool = None, NetworkCardIndex: int = None
    ) -> AttachNetworkInterfaceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterface.attach)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceattachmethod)
        """

    def create_tags(self, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterface.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfacecreate-tagsmethod)
        """

    def delete(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterface.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfacedeletemethod)
        """

    def describe_attribute(
        self, Attribute: NetworkInterfaceAttribute = None, DryRun: bool = None
    ) -> DescribeNetworkInterfaceAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterface.describe_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfacedescribe-attributemethod)
        """

    def detach(self, AttachmentId: str, DryRun: bool = None, Force: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterface.detach)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfacedetachmethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterface.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterface.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceloadmethod)
        """

    def modify_attribute(
        self,
        Attachment: NetworkInterfaceAttachmentChangesTypeDef = None,
        Description: "AttributeValueTypeDef" = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        SourceDestCheck: "AttributeBooleanValueTypeDef" = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterface.modify_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfacemodify-attributemethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterface.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfacereloadmethod)
        """

    def reset_attribute(self, DryRun: bool = None, SourceDestCheck: str = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterface.reset_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfacereset-attributemethod)
        """

    def unassign_private_ip_addresses(self, PrivateIpAddresses: List[str]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.NetworkInterface.unassign_private_ip_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#networkinterfaceunassign-private-ip-addressesmethod)
        """


_NetworkInterface = NetworkInterface


class Route(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Route)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#route)
    """

    destination_ipv6_cidr_block: str
    destination_prefix_list_id: str
    egress_only_internet_gateway_id: str
    gateway_id: str
    instance_id: str
    instance_owner_id: str
    nat_gateway_id: str
    transit_gateway_id: str
    local_gateway_id: str
    carrier_gateway_id: str
    network_interface_id: str
    origin: str
    state: str
    vpc_peering_connection_id: str
    route_table_id: str
    destination_cidr_block: str

    def RouteTable(self) -> "_RouteTable":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Route.RouteTable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routeroutetablemethod)
        """

    def delete(
        self,
        DestinationIpv6CidrBlock: str = None,
        DestinationPrefixListId: str = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Route.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routedeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Route.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routeget-available-subresourcesmethod)
        """

    def replace(
        self,
        DestinationIpv6CidrBlock: str = None,
        DestinationPrefixListId: str = None,
        DryRun: bool = None,
        VpcEndpointId: str = None,
        EgressOnlyInternetGatewayId: str = None,
        GatewayId: str = None,
        InstanceId: str = None,
        LocalTarget: bool = None,
        NatGatewayId: str = None,
        TransitGatewayId: str = None,
        LocalGatewayId: str = None,
        CarrierGatewayId: str = None,
        NetworkInterfaceId: str = None,
        VpcPeeringConnectionId: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Route.replace)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routereplacemethod)
        """


_Route = Route


class RouteTableAssociation(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.RouteTableAssociation)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetableassociation)
    """

    main: bool
    route_table_association_id: str
    route_table_id: str
    subnet_id: str
    gateway_id: str
    association_state: Dict[str, Any]
    id: str
    route_table: "RouteTable"
    subnet: "Subnet"

    def delete(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.RouteTableAssociation.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetableassociationdeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.RouteTableAssociation.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetableassociationget-available-subresourcesmethod)
        """

    def replace_subnet(self, RouteTableId: str, DryRun: bool = None) -> "_RouteTableAssociation":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.RouteTableAssociation.replace_subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetableassociationreplace-subnetmethod)
        """


_RouteTableAssociation = RouteTableAssociation


class SecurityGroup(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.SecurityGroup)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygroup)
    """

    description: str
    group_name: str
    ip_permissions: List[Any]
    owner_id: str
    group_id: str
    ip_permissions_egress: List[Any]
    tags: List[Any]
    vpc_id: str
    id: str

    def authorize_egress(
        self,
        DryRun: bool = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        CidrIp: str = None,
        FromPort: int = None,
        IpProtocol: str = None,
        ToPort: int = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.SecurityGroup.authorize_egress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygroupauthorize-egressmethod)
        """

    def authorize_ingress(
        self,
        CidrIp: str = None,
        FromPort: int = None,
        GroupName: str = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.SecurityGroup.authorize_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygroupauthorize-ingressmethod)
        """

    def create_tags(self, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.SecurityGroup.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygroupcreate-tagsmethod)
        """

    def delete(self, GroupName: str = None, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.SecurityGroup.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygroupdeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.SecurityGroup.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygroupget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.SecurityGroup.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygrouploadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.SecurityGroup.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygroupreloadmethod)
        """

    def revoke_egress(
        self,
        DryRun: bool = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        CidrIp: str = None,
        FromPort: int = None,
        IpProtocol: str = None,
        ToPort: int = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
    ) -> RevokeSecurityGroupEgressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.SecurityGroup.revoke_egress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygrouprevoke-egressmethod)
        """

    def revoke_ingress(
        self,
        CidrIp: str = None,
        FromPort: int = None,
        GroupName: str = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None,
    ) -> RevokeSecurityGroupIngressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.SecurityGroup.revoke_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#securitygrouprevoke-ingressmethod)
        """


_SecurityGroup = SecurityGroup


class Snapshot(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Snapshot)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshot)
    """

    data_encryption_key_id: str
    description: str
    encrypted: bool
    kms_key_id: str
    owner_id: str
    progress: str
    snapshot_id: str
    start_time: datetime
    state: str
    state_message: str
    volume_id: str
    volume_size: int
    owner_alias: str
    outpost_arn: str
    tags: List[Any]
    id: str
    volume: "Volume"

    def copy(
        self,
        SourceRegion: str,
        Description: str = None,
        DestinationOutpostArn: str = None,
        DestinationRegion: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        PresignedUrl: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> CopySnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Snapshot.copy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotcopymethod)
        """

    def create_tags(self, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Snapshot.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotcreate-tagsmethod)
        """

    def delete(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Snapshot.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotdeletemethod)
        """

    def describe_attribute(
        self, Attribute: SnapshotAttributeName, DryRun: bool = None
    ) -> DescribeSnapshotAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Snapshot.describe_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotdescribe-attributemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Snapshot.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Snapshot.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotloadmethod)
        """

    def modify_attribute(
        self,
        Attribute: SnapshotAttributeName = None,
        CreateVolumePermission: CreateVolumePermissionModificationsTypeDef = None,
        GroupNames: List[str] = None,
        OperationType: OperationType = None,
        UserIds: List[str] = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Snapshot.modify_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotmodify-attributemethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Snapshot.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotreloadmethod)
        """

    def reset_attribute(self, Attribute: SnapshotAttributeName, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Snapshot.reset_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotreset-attributemethod)
        """

    def wait_until_completed(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Snapshot.wait_until_completed)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#snapshotwait-until-completedmethod)
        """


_Snapshot = Snapshot


class Instance(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Instance)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instance)
    """

    ami_launch_index: int
    image_id: str
    instance_id: str
    instance_type: str
    kernel_id: str
    key_name: str
    launch_time: datetime
    monitoring: Dict[str, Any]
    placement: Dict[str, Any]
    platform: str
    private_dns_name: str
    private_ip_address: str
    product_codes: List[Any]
    public_dns_name: str
    public_ip_address: str
    ramdisk_id: str
    state: Dict[str, Any]
    state_transition_reason: str
    subnet_id: str
    vpc_id: str
    architecture: str
    block_device_mappings: List[Any]
    client_token: str
    ebs_optimized: bool
    ena_support: bool
    hypervisor: str
    iam_instance_profile: Dict[str, Any]
    instance_lifecycle: str
    elastic_gpu_associations: List[Any]
    elastic_inference_accelerator_associations: List[Any]
    network_interfaces_attribute: List[Any]
    outpost_arn: str
    root_device_name: str
    root_device_type: str
    security_groups: List[Any]
    source_dest_check: bool
    spot_instance_request_id: str
    sriov_net_support: str
    state_reason: Dict[str, Any]
    tags: List[Any]
    virtualization_type: str
    cpu_options: Dict[str, Any]
    capacity_reservation_id: str
    capacity_reservation_specification: Dict[str, Any]
    hibernation_options: Dict[str, Any]
    licenses: List[Any]
    metadata_options: Dict[str, Any]
    enclave_options: Dict[str, Any]
    boot_mode: str
    id: str
    classic_address: "ClassicAddress"
    image: "Image"
    key_pair: "KeyPairInfo"
    network_interfaces: "NetworkInterface"
    placement_group: "PlacementGroup"
    subnet: "Subnet"
    vpc: "Vpc"
    volumes: InstanceVolumesCollection
    vpc_addresses: InstanceVpcAddressesCollection

    def attach_classic_link_vpc(
        self, Groups: List[str], VpcId: str, DryRun: bool = None
    ) -> AttachClassicLinkVpcResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.attach_classic_link_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instanceattach-classic-link-vpcmethod)
        """

    def attach_volume(
        self, Device: str, VolumeId: str, DryRun: bool = None
    ) -> "VolumeAttachmentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.attach_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instanceattach-volumemethod)
        """

    def console_output(
        self, DryRun: bool = None, Latest: bool = None
    ) -> GetConsoleOutputResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.console_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instanceconsole-outputmethod)
        """

    def create_image(
        self,
        Name: str,
        BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
        Description: str = None,
        DryRun: bool = None,
        NoReboot: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> _Image:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.create_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancecreate-imagemethod)
        """

    def create_tags(self, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancecreate-tagsmethod)
        """

    def delete_tags(self, Tags: List[TagTypeDef] = None, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancedelete-tagsmethod)
        """

    def describe_attribute(
        self, Attribute: InstanceAttributeName, DryRun: bool = None
    ) -> InstanceAttributeTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.describe_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancedescribe-attributemethod)
        """

    def detach_classic_link_vpc(
        self, VpcId: str, DryRun: bool = None
    ) -> DetachClassicLinkVpcResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.detach_classic_link_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancedetach-classic-link-vpcmethod)
        """

    def detach_volume(
        self, VolumeId: str, Device: str = None, Force: bool = None, DryRun: bool = None
    ) -> "VolumeAttachmentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.detach_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancedetach-volumemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instanceget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instanceloadmethod)
        """

    def modify_attribute(
        self,
        SourceDestCheck: "AttributeBooleanValueTypeDef" = None,
        Attribute: InstanceAttributeName = None,
        BlockDeviceMappings: List[InstanceBlockDeviceMappingSpecificationTypeDef] = None,
        DisableApiTermination: "AttributeBooleanValueTypeDef" = None,
        DryRun: bool = None,
        EbsOptimized: "AttributeBooleanValueTypeDef" = None,
        EnaSupport: "AttributeBooleanValueTypeDef" = None,
        Groups: List[str] = None,
        InstanceInitiatedShutdownBehavior: "AttributeValueTypeDef" = None,
        InstanceType: "AttributeValueTypeDef" = None,
        Kernel: "AttributeValueTypeDef" = None,
        Ramdisk: "AttributeValueTypeDef" = None,
        SriovNetSupport: "AttributeValueTypeDef" = None,
        UserData: BlobAttributeValueTypeDef = None,
        Value: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.modify_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancemodify-attributemethod)
        """

    def monitor(self, DryRun: bool = None) -> MonitorInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.monitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancemonitormethod)
        """

    def password_data(self, DryRun: bool = None) -> GetPasswordDataResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.password_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancepassword-datamethod)
        """

    def reboot(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.reboot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancerebootmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancereloadmethod)
        """

    def report_status(
        self,
        ReasonCodes: List[ReportInstanceReasonCodes],
        Status: ReportStatusType,
        Description: str = None,
        DryRun: bool = None,
        EndTime: datetime = None,
        StartTime: datetime = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.report_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancereport-statusmethod)
        """

    def reset_attribute(self, Attribute: InstanceAttributeName, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.reset_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancereset-attributemethod)
        """

    def reset_kernel(self, Attribute: InstanceAttributeName, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.reset_kernel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancereset-kernelmethod)
        """

    def reset_ramdisk(self, Attribute: InstanceAttributeName, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.reset_ramdisk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancereset-ramdiskmethod)
        """

    def reset_source_dest_check(
        self, Attribute: InstanceAttributeName, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.reset_source_dest_check)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancereset-source-dest-checkmethod)
        """

    def start(self, AdditionalInfo: str = None, DryRun: bool = None) -> StartInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.start)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancestartmethod)
        """

    def stop(
        self, Hibernate: bool = None, DryRun: bool = None, Force: bool = None
    ) -> StopInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.stop)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancestopmethod)
        """

    def terminate(self, DryRun: bool = None) -> TerminateInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.terminate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instanceterminatemethod)
        """

    def unmonitor(self, DryRun: bool = None) -> UnmonitorInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.unmonitor)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instanceunmonitormethod)
        """

    def wait_until_exists(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.wait_until_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancewait-until-existsmethod)
        """

    def wait_until_running(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.wait_until_running)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancewait-until-runningmethod)
        """

    def wait_until_stopped(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.wait_until_stopped)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancewait-until-stoppedmethod)
        """

    def wait_until_terminated(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Instance.wait_until_terminated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#instancewait-until-terminatedmethod)
        """


_Instance = Instance


class Volume(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Volume)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volume)
    """

    attachments: List[Any]
    availability_zone: str
    create_time: datetime
    encrypted: bool
    kms_key_id: str
    outpost_arn: str
    size: int
    snapshot_id: str
    state: str
    volume_id: str
    iops: int
    tags: List[Any]
    volume_type: str
    fast_restored: bool
    multi_attach_enabled: bool
    throughput: int
    id: str
    snapshots: VolumeSnapshotsCollection

    def attach_to_instance(
        self, Device: str, InstanceId: str, DryRun: bool = None
    ) -> "VolumeAttachmentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Volume.attach_to_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumeattach-to-instancemethod)
        """

    def create_snapshot(
        self,
        Description: str = None,
        OutpostArn: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> _Snapshot:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Volume.create_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumecreate-snapshotmethod)
        """

    def create_tags(self, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Volume.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumecreate-tagsmethod)
        """

    def delete(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Volume.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumedeletemethod)
        """

    def describe_attribute(
        self, Attribute: VolumeAttributeName, DryRun: bool = None
    ) -> DescribeVolumeAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Volume.describe_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumedescribe-attributemethod)
        """

    def describe_status(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeVolumeStatusResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Volume.describe_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumedescribe-statusmethod)
        """

    def detach_from_instance(
        self, Device: str = None, Force: bool = None, InstanceId: str = None, DryRun: bool = None
    ) -> "VolumeAttachmentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Volume.detach_from_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumedetach-from-instancemethod)
        """

    def enable_io(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Volume.enable_io)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumeenable-iomethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Volume.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumeget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Volume.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumeloadmethod)
        """

    def modify_attribute(
        self, AutoEnableIO: "AttributeBooleanValueTypeDef" = None, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Volume.modify_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumemodify-attributemethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Volume.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#volumereloadmethod)
        """


_Volume = Volume


class RouteTable(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.RouteTable)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetable)
    """

    associations_attribute: List[Any]
    propagating_vgws: List[Any]
    route_table_id: str
    routes_attribute: List[Any]
    tags: List[Any]
    vpc_id: str
    owner_id: str
    id: str
    associations: "RouteTableAssociation"
    routes: "Route"
    vpc: "Vpc"

    def associate_with_subnet(
        self, DryRun: bool = None, SubnetId: str = None, GatewayId: str = None
    ) -> _RouteTableAssociation:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.RouteTable.associate_with_subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetableassociate-with-subnetmethod)
        """

    def create_route(
        self,
        DestinationCidrBlock: str = None,
        DestinationIpv6CidrBlock: str = None,
        DestinationPrefixListId: str = None,
        DryRun: bool = None,
        VpcEndpointId: str = None,
        EgressOnlyInternetGatewayId: str = None,
        GatewayId: str = None,
        InstanceId: str = None,
        NatGatewayId: str = None,
        TransitGatewayId: str = None,
        LocalGatewayId: str = None,
        CarrierGatewayId: str = None,
        NetworkInterfaceId: str = None,
        VpcPeeringConnectionId: str = None,
    ) -> _Route:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.RouteTable.create_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetablecreate-routemethod)
        """

    def create_tags(self, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.RouteTable.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetablecreate-tagsmethod)
        """

    def delete(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.RouteTable.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetabledeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.RouteTable.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetableget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.RouteTable.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetableloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.RouteTable.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#routetablereloadmethod)
        """


_RouteTable = RouteTable


class Subnet(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Subnet)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnet)
    """

    availability_zone: str
    availability_zone_id: str
    available_ip_address_count: int
    cidr_block: str
    default_for_az: bool
    map_public_ip_on_launch: bool
    map_customer_owned_ip_on_launch: bool
    customer_owned_ipv4_pool: str
    state: str
    subnet_id: str
    vpc_id: str
    owner_id: str
    assign_ipv6_address_on_creation: bool
    ipv6_cidr_block_association_set: List[Any]
    tags: List[Any]
    subnet_arn: str
    outpost_arn: str
    id: str
    vpc: "Vpc"
    instances: SubnetInstancesCollection
    network_interfaces: SubnetNetworkInterfacesCollection

    def create_instances(
        self,
        MaxCount: int,
        MinCount: int,
        BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
        ImageId: str = None,
        InstanceType: InstanceType = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List["InstanceIpv6AddressTypeDef"] = None,
        KernelId: str = None,
        KeyName: str = None,
        Monitoring: "RunInstancesMonitoringEnabledTypeDef" = None,
        Placement: "PlacementTypeDef" = None,
        RamdiskId: str = None,
        SecurityGroupIds: List[str] = None,
        SecurityGroups: List[str] = None,
        UserData: str = None,
        AdditionalInfo: str = None,
        ClientToken: str = None,
        DisableApiTermination: bool = None,
        DryRun: bool = None,
        EbsOptimized: bool = None,
        IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef" = None,
        InstanceInitiatedShutdownBehavior: ShutdownBehavior = None,
        NetworkInterfaces: List["InstanceNetworkInterfaceSpecificationTypeDef"] = None,
        PrivateIpAddress: str = None,
        ElasticGpuSpecification: List["ElasticGpuSpecificationTypeDef"] = None,
        ElasticInferenceAccelerators: List[ElasticInferenceAcceleratorTypeDef] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        LaunchTemplate: LaunchTemplateSpecificationTypeDef = None,
        InstanceMarketOptions: InstanceMarketOptionsRequestTypeDef = None,
        CreditSpecification: "CreditSpecificationRequestTypeDef" = None,
        CpuOptions: CpuOptionsRequestTypeDef = None,
        CapacityReservationSpecification: CapacityReservationSpecificationTypeDef = None,
        HibernationOptions: HibernationOptionsRequestTypeDef = None,
        LicenseSpecifications: List[LicenseConfigurationRequestTypeDef] = None,
        MetadataOptions: InstanceMetadataOptionsRequestTypeDef = None,
        EnclaveOptions: EnclaveOptionsRequestTypeDef = None,
    ) -> List[_Instance]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Subnet.create_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetcreate-instancesmethod)
        """

    def create_network_interface(
        self,
        Description: str = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List["InstanceIpv6AddressTypeDef"] = None,
        PrivateIpAddress: str = None,
        PrivateIpAddresses: List["PrivateIpAddressSpecificationTypeDef"] = None,
        SecondaryPrivateIpAddressCount: int = None,
        InterfaceType: Literal["efa"] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> _NetworkInterface:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Subnet.create_network_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetcreate-network-interfacemethod)
        """

    def create_tags(self, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Subnet.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetcreate-tagsmethod)
        """

    def delete(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Subnet.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetdeletemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Subnet.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Subnet.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetloadmethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Subnet.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#subnetreloadmethod)
        """


_Subnet = Subnet


class Vpc(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Vpc)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpc)
    """

    cidr_block: str
    dhcp_options_id: str
    state: str
    vpc_id: str
    owner_id: str
    instance_tenancy: str
    ipv6_cidr_block_association_set: List[Any]
    cidr_block_association_set: List[Any]
    is_default: bool
    tags: List[Any]
    id: str
    dhcp_options: "DhcpOptions"
    accepted_vpc_peering_connections: VpcAcceptedVpcPeeringConnectionsCollection
    instances: VpcInstancesCollection
    internet_gateways: VpcInternetGatewaysCollection
    network_acls: VpcNetworkAclsCollection
    network_interfaces: VpcNetworkInterfacesCollection
    requested_vpc_peering_connections: VpcRequestedVpcPeeringConnectionsCollection
    route_tables: VpcRouteTablesCollection
    security_groups: VpcSecurityGroupsCollection
    subnets: VpcSubnetsCollection

    def associate_dhcp_options(self, DhcpOptionsId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.associate_dhcp_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcassociate-dhcp-optionsmethod)
        """

    def attach_classic_link_instance(
        self, Groups: List[str], InstanceId: str, DryRun: bool = None
    ) -> AttachClassicLinkVpcResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.attach_classic_link_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcattach-classic-link-instancemethod)
        """

    def attach_internet_gateway(self, InternetGatewayId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.attach_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcattach-internet-gatewaymethod)
        """

    def create_network_acl(
        self, DryRun: bool = None, TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> _NetworkAcl:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.create_network_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpccreate-network-aclmethod)
        """

    def create_route_table(
        self, DryRun: bool = None, TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> _RouteTable:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.create_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpccreate-route-tablemethod)
        """

    def create_security_group(
        self,
        Description: str,
        GroupName: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> _SecurityGroup:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.create_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpccreate-security-groupmethod)
        """

    def create_subnet(
        self,
        CidrBlock: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Ipv6CidrBlock: str = None,
        OutpostArn: str = None,
        DryRun: bool = None,
    ) -> _Subnet:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.create_subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpccreate-subnetmethod)
        """

    def create_tags(self, Tags: Optional[List[TagTypeDef]], DryRun: bool = None) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpccreate-tagsmethod)
        """

    def delete(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.delete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcdeletemethod)
        """

    def describe_attribute(
        self, Attribute: VpcAttributeName, DryRun: bool = None
    ) -> DescribeVpcAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.describe_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcdescribe-attributemethod)
        """

    def detach_classic_link_instance(
        self, InstanceId: str, DryRun: bool = None
    ) -> DetachClassicLinkVpcResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.detach_classic_link_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcdetach-classic-link-instancemethod)
        """

    def detach_internet_gateway(self, InternetGatewayId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.detach_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcdetach-internet-gatewaymethod)
        """

    def disable_classic_link(self, DryRun: bool = None) -> DisableVpcClassicLinkResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.disable_classic_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcdisable-classic-linkmethod)
        """

    def enable_classic_link(self, DryRun: bool = None) -> EnableVpcClassicLinkResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.enable_classic_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcenable-classic-linkmethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcget-available-subresourcesmethod)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.load)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcloadmethod)
        """

    def modify_attribute(
        self,
        EnableDnsHostnames: "AttributeBooleanValueTypeDef" = None,
        EnableDnsSupport: "AttributeBooleanValueTypeDef" = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.modify_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcmodify-attributemethod)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.reload)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcreloadmethod)
        """

    def request_vpc_peering_connection(
        self,
        DryRun: bool = None,
        PeerOwnerId: str = None,
        PeerVpcId: str = None,
        PeerRegion: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> _VpcPeeringConnection:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.request_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcrequest-vpc-peering-connectionmethod)
        """

    def wait_until_available(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.wait_until_available)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcwait-until-availablemethod)
        """

    def wait_until_exists(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Vpc.wait_until_exists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#vpcwait-until-existsmethod)
        """


_Vpc = Vpc


class EC2ServiceResource(Boto3ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html)
    """

    classic_addresses: ServiceResourceClassicAddressesCollection
    dhcp_options_sets: ServiceResourceDhcpOptionsSetsCollection
    images: ServiceResourceImagesCollection
    instances: ServiceResourceInstancesCollection
    internet_gateways: ServiceResourceInternetGatewaysCollection
    key_pairs: ServiceResourceKeyPairsCollection
    network_acls: ServiceResourceNetworkAclsCollection
    network_interfaces: ServiceResourceNetworkInterfacesCollection
    placement_groups: ServiceResourcePlacementGroupsCollection
    route_tables: ServiceResourceRouteTablesCollection
    security_groups: ServiceResourceSecurityGroupsCollection
    snapshots: ServiceResourceSnapshotsCollection
    subnets: ServiceResourceSubnetsCollection
    volumes: ServiceResourceVolumesCollection
    vpc_addresses: ServiceResourceVpcAddressesCollection
    vpc_peering_connections: ServiceResourceVpcPeeringConnectionsCollection
    vpcs: ServiceResourceVpcsCollection

    def ClassicAddress(self, public_ip: str) -> _ClassicAddress:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.ClassicAddress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceclassicaddressmethod)
        """

    def DhcpOptions(self, id: str) -> _DhcpOptions:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.DhcpOptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcedhcpoptionsmethod)
        """

    def Image(self, id: str) -> _Image:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceimagemethod)
        """

    def Instance(self, id: str) -> _Instance:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceinstancemethod)
        """

    def InternetGateway(self, id: str) -> _InternetGateway:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.InternetGateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceinternetgatewaymethod)
        """

    def KeyPair(self, name: str) -> _KeyPairInfo:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.KeyPair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcekeypairmethod)
        """

    def NetworkAcl(self, id: str) -> _NetworkAcl:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.NetworkAcl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcenetworkaclmethod)
        """

    def NetworkInterface(self, id: str) -> _NetworkInterface:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.NetworkInterface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcenetworkinterfacemethod)
        """

    def NetworkInterfaceAssociation(self, id: str) -> _NetworkInterfaceAssociation:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.NetworkInterfaceAssociation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcenetworkinterfaceassociationmethod)
        """

    def PlacementGroup(self, name: str) -> _PlacementGroup:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.PlacementGroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceplacementgroupmethod)
        """

    def Route(self, route_table_id: str, destination_cidr_block: str) -> _Route:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceroutemethod)
        """

    def RouteTable(self, id: str) -> _RouteTable:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.RouteTable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceroutetablemethod)
        """

    def RouteTableAssociation(self, id: str) -> _RouteTableAssociation:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.RouteTableAssociation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceroutetableassociationmethod)
        """

    def SecurityGroup(self, id: str) -> _SecurityGroup:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.SecurityGroup)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcesecuritygroupmethod)
        """

    def Snapshot(self, id: str) -> _Snapshot:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcesnapshotmethod)
        """

    def Subnet(self, id: str) -> _Subnet:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcesubnetmethod)
        """

    def Tag(self, resource_id: str, key: str, value: str) -> _Tag:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Tag)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcetagmethod)
        """

    def Volume(self, id: str) -> _Volume:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcevolumemethod)
        """

    def Vpc(self, id: str) -> _Vpc:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.Vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcevpcmethod)
        """

    def VpcAddress(self, allocation_id: str) -> _VpcAddress:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.VpcAddress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcevpcaddressmethod)
        """

    def VpcPeeringConnection(self, id: str) -> _VpcPeeringConnection:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.VpcPeeringConnection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcevpcpeeringconnectionmethod)
        """

    def create_dhcp_options(
        self,
        DhcpConfigurations: List[NewDhcpConfigurationTypeDef],
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> _DhcpOptions:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.create_dhcp_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate-dhcp-optionsmethod)
        """

    def create_instances(
        self,
        MaxCount: int,
        MinCount: int,
        BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
        ImageId: str = None,
        InstanceType: InstanceType = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List["InstanceIpv6AddressTypeDef"] = None,
        KernelId: str = None,
        KeyName: str = None,
        Monitoring: "RunInstancesMonitoringEnabledTypeDef" = None,
        Placement: "PlacementTypeDef" = None,
        RamdiskId: str = None,
        SecurityGroupIds: List[str] = None,
        SecurityGroups: List[str] = None,
        SubnetId: str = None,
        UserData: str = None,
        AdditionalInfo: str = None,
        ClientToken: str = None,
        DisableApiTermination: bool = None,
        DryRun: bool = None,
        EbsOptimized: bool = None,
        IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef" = None,
        InstanceInitiatedShutdownBehavior: ShutdownBehavior = None,
        NetworkInterfaces: List["InstanceNetworkInterfaceSpecificationTypeDef"] = None,
        PrivateIpAddress: str = None,
        ElasticGpuSpecification: List["ElasticGpuSpecificationTypeDef"] = None,
        ElasticInferenceAccelerators: List[ElasticInferenceAcceleratorTypeDef] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        LaunchTemplate: LaunchTemplateSpecificationTypeDef = None,
        InstanceMarketOptions: InstanceMarketOptionsRequestTypeDef = None,
        CreditSpecification: "CreditSpecificationRequestTypeDef" = None,
        CpuOptions: CpuOptionsRequestTypeDef = None,
        CapacityReservationSpecification: CapacityReservationSpecificationTypeDef = None,
        HibernationOptions: HibernationOptionsRequestTypeDef = None,
        LicenseSpecifications: List[LicenseConfigurationRequestTypeDef] = None,
        MetadataOptions: InstanceMetadataOptionsRequestTypeDef = None,
        EnclaveOptions: EnclaveOptionsRequestTypeDef = None,
    ) -> List[_Instance]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.create_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate-instancesmethod)
        """

    def create_internet_gateway(
        self, TagSpecifications: List["TagSpecificationTypeDef"] = None, DryRun: bool = None
    ) -> _InternetGateway:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.create_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate-internet-gatewaymethod)
        """

    def create_key_pair(
        self,
        KeyName: str,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> _KeyPair:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.create_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate-key-pairmethod)
        """

    def create_network_acl(
        self,
        VpcId: str,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> _NetworkAcl:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.create_network_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate-network-aclmethod)
        """

    def create_network_interface(
        self,
        SubnetId: str,
        Description: str = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List["InstanceIpv6AddressTypeDef"] = None,
        PrivateIpAddress: str = None,
        PrivateIpAddresses: List["PrivateIpAddressSpecificationTypeDef"] = None,
        SecondaryPrivateIpAddressCount: int = None,
        InterfaceType: Literal["efa"] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> _NetworkInterface:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.create_network_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate-network-interfacemethod)
        """

    def create_placement_group(
        self,
        DryRun: bool = None,
        GroupName: str = None,
        Strategy: PlacementStrategy = None,
        PartitionCount: int = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> _PlacementGroup:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.create_placement_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate-placement-groupmethod)
        """

    def create_route_table(
        self,
        VpcId: str,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> _RouteTable:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.create_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate-route-tablemethod)
        """

    def create_security_group(
        self,
        Description: str,
        GroupName: str,
        VpcId: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> _SecurityGroup:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.create_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate-security-groupmethod)
        """

    def create_snapshot(
        self,
        VolumeId: str,
        Description: str = None,
        OutpostArn: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> _Snapshot:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.create_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate-snapshotmethod)
        """

    def create_subnet(
        self,
        VpcId: str,
        CidrBlock: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Ipv6CidrBlock: str = None,
        OutpostArn: str = None,
        DryRun: bool = None,
    ) -> _Subnet:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.create_subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate-subnetmethod)
        """

    def create_tags(
        self, Resources: List[str], Tags: List["TagTypeDef"], DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate-tagsmethod)
        """

    def create_volume(
        self,
        AvailabilityZone: str,
        Encrypted: bool = None,
        Iops: int = None,
        KmsKeyId: str = None,
        OutpostArn: str = None,
        Size: int = None,
        SnapshotId: str = None,
        VolumeType: VolumeType = None,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        MultiAttachEnabled: bool = None,
        Throughput: int = None,
    ) -> _Volume:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.create_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate-volumemethod)
        """

    def create_vpc(
        self,
        CidrBlock: str,
        AmazonProvidedIpv6CidrBlock: bool = None,
        Ipv6Pool: str = None,
        Ipv6CidrBlock: str = None,
        DryRun: bool = None,
        InstanceTenancy: Tenancy = None,
        Ipv6CidrBlockNetworkBorderGroup: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> _Vpc:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.create_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate-vpcmethod)
        """

    def create_vpc_peering_connection(
        self,
        DryRun: bool = None,
        PeerOwnerId: str = None,
        PeerVpcId: str = None,
        VpcId: str = None,
        PeerRegion: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> _VpcPeeringConnection:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.create_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcecreate-vpc-peering-connectionmethod)
        """

    def disassociate_route_table(self, AssociationId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.disassociate_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourcedisassociate-route-tablemethod)
        """

    def get_available_subresources(self) -> List[str]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.get_available_subresources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceget-available-subresourcesmethod)
        """

    def import_key_pair(
        self,
        KeyName: str,
        PublicKeyMaterial: Union[bytes, IO[bytes]],
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> _KeyPairInfo:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.import_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceimport-key-pairmethod)
        """

    def register_image(
        self,
        Name: str,
        ImageLocation: str = None,
        Architecture: ArchitectureValues = None,
        BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
        Description: str = None,
        DryRun: bool = None,
        EnaSupport: bool = None,
        KernelId: str = None,
        BillingProducts: List[str] = None,
        RamdiskId: str = None,
        RootDeviceName: str = None,
        SriovNetSupport: str = None,
        VirtualizationType: str = None,
        BootMode: BootModeValues = None,
    ) -> _Image:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.ServiceResource.register_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource.html#ec2serviceresourceregister-imagemethod)
        """
