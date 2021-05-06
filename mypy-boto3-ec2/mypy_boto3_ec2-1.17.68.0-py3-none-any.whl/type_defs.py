"""
Type annotations for ec2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ec2.type_defs import AcceptReservedInstancesExchangeQuoteResultTypeDef

    data: AcceptReservedInstancesExchangeQuoteResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, List, Union

from mypy_boto3_ec2.literals import (
    ActivityStatus,
    AllocationState,
    AllocationStrategy,
    AllowsMultipleInstanceTypes,
    AnalysisStatus,
    ApplianceModeSupportValue,
    ArchitectureType,
    ArchitectureValues,
    AssociationStatusCode,
    AttachmentStatus,
    AutoAcceptSharedAssociationsValue,
    AutoAcceptSharedAttachmentsValue,
    AutoPlacement,
    AvailabilityZoneOptInStatus,
    AvailabilityZoneState,
    BatchState,
    BgpStatus,
    BootModeType,
    BootModeValues,
    BundleTaskState,
    ByoipCidrState,
    CancelBatchErrorCode,
    CancelSpotInstanceRequestState,
    CapacityReservationInstancePlatform,
    CapacityReservationPreference,
    CapacityReservationState,
    CapacityReservationTenancy,
    CarrierGatewayState,
    ClientCertificateRevocationListStatusCode,
    ClientVpnAuthenticationType,
    ClientVpnAuthorizationRuleStatusCode,
    ClientVpnConnectionStatusCode,
    ClientVpnEndpointAttributeStatusCode,
    ClientVpnEndpointStatusCode,
    ClientVpnRouteStatusCode,
    ConnectionNotificationState,
    ConversionTaskState,
    DatafeedSubscriptionState,
    DefaultRouteTableAssociationValue,
    DefaultRouteTablePropagationValue,
    DefaultTargetCapacityType,
    DeleteFleetErrorCode,
    DeleteQueuedReservedInstancesErrorCode,
    DeviceType,
    DiskImageFormat,
    DiskType,
    DnsNameState,
    DnsSupportValue,
    DomainType,
    EbsEncryptionSupport,
    EbsNvmeSupport,
    EbsOptimizedSupport,
    ElasticGpuStatus,
    EnaSupport,
    EndDateType,
    EphemeralNvmeSupport,
    EventCode,
    EventType,
    ExcessCapacityTerminationPolicy,
    ExportEnvironment,
    ExportTaskState,
    FastSnapshotRestoreStateCode,
    FleetActivityStatus,
    FleetEventType,
    FleetExcessCapacityTerminationPolicy,
    FleetOnDemandAllocationStrategy,
    FleetStateCode,
    FleetType,
    FpgaImageStateCode,
    HostRecovery,
    HttpTokensState,
    HypervisorType,
    IamInstanceProfileAssociationState,
    Igmpv2SupportValue,
    ImageState,
    ImageTypeValues,
    InstanceHealthStatus,
    InstanceInterruptionBehavior,
    InstanceLifecycle,
    InstanceLifecycleType,
    InstanceMatchCriteria,
    InstanceMetadataEndpointState,
    InstanceMetadataOptionsState,
    InstanceStateName,
    InstanceType,
    InstanceTypeHypervisor,
    InterfacePermissionType,
    Ipv6SupportValue,
    LaunchTemplateErrorCode,
    LaunchTemplateHttpTokensState,
    LaunchTemplateInstanceMetadataEndpointState,
    LaunchTemplateInstanceMetadataOptionsState,
    ListingState,
    ListingStatus,
    LocalGatewayRouteState,
    LocalGatewayRouteType,
    LocationType,
    LogDestinationType,
    MembershipType,
    MonitoringState,
    MoveStatus,
    MulticastSupportValue,
    NatGatewayState,
    NetworkInterfacePermissionStateCode,
    NetworkInterfaceStatus,
    NetworkInterfaceType,
    OfferingClassType,
    OfferingTypeValues,
    OnDemandAllocationStrategy,
    PartitionLoadFrequency,
    PaymentOption,
    PlacementGroupState,
    PlacementGroupStrategy,
    PlacementStrategy,
    PrefixListState,
    PrincipalType,
    ProductCodeValues,
    ProtocolType,
    ReplaceRootVolumeTaskState,
    ReservationState,
    ReservedInstanceState,
    ResourceType,
    RIProductDescription,
    RootDeviceType,
    RouteOrigin,
    RouteState,
    RouteTableAssociationStateCode,
    RuleAction,
    ServiceState,
    ServiceType,
    ShutdownBehavior,
    SnapshotState,
    SpotAllocationStrategy,
    SpotInstanceInterruptionBehavior,
    SpotInstanceState,
    SpotInstanceType,
    State,
    StaticSourcesSupportValue,
    Status,
    StatusType,
    SubnetCidrBlockStateCode,
    SubnetState,
    SummaryStatus,
    TelemetryStatus,
    Tenancy,
    TrafficDirection,
    TrafficMirrorRuleAction,
    TrafficMirrorTargetType,
    TrafficType,
    TransitGatewayAssociationState,
    TransitGatewayAttachmentResourceType,
    TransitGatewayAttachmentState,
    TransitGatewayConnectPeerState,
    TransitGatewayMulitcastDomainAssociationState,
    TransitGatewayMulticastDomainState,
    TransitGatewayPrefixListReferenceState,
    TransitGatewayPropagationState,
    TransitGatewayRouteState,
    TransitGatewayRouteTableState,
    TransitGatewayRouteType,
    TransitGatewayState,
    TransportProtocol,
    TunnelInsideIpVersion,
    UnlimitedSupportedInstanceFamily,
    UnsuccessfulInstanceCreditSpecificationErrorCode,
    UsageClassType,
    VirtualizationType,
    VolumeAttachmentState,
    VolumeModificationState,
    VolumeState,
    VolumeStatusInfoStatus,
    VolumeStatusName,
    VolumeType,
    VpcCidrBlockStateCode,
    VpcEndpointType,
    VpcPeeringConnectionStateReasonCode,
    VpcState,
    VpnEcmpSupportValue,
    VpnState,
    scope,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AcceptReservedInstancesExchangeQuoteResultTypeDef",
    "AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef",
    "AcceptTransitGatewayPeeringAttachmentResultTypeDef",
    "AcceptTransitGatewayVpcAttachmentResultTypeDef",
    "AcceptVpcEndpointConnectionsResultTypeDef",
    "AcceptVpcPeeringConnectionResultTypeDef",
    "AccountAttributeTypeDef",
    "AccountAttributeValueTypeDef",
    "ActiveInstanceTypeDef",
    "AddPrefixListEntryTypeDef",
    "AddressAttributeTypeDef",
    "AddressTypeDef",
    "AdvertiseByoipCidrResultTypeDef",
    "AllocateAddressResultTypeDef",
    "AllocateHostsResultTypeDef",
    "AllowedPrincipalTypeDef",
    "AlternatePathHintTypeDef",
    "AnalysisAclRuleTypeDef",
    "AnalysisComponentTypeDef",
    "AnalysisLoadBalancerListenerTypeDef",
    "AnalysisLoadBalancerTargetTypeDef",
    "AnalysisPacketHeaderTypeDef",
    "AnalysisRouteTableRouteTypeDef",
    "AnalysisSecurityGroupRuleTypeDef",
    "ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef",
    "AssignIpv6AddressesResultTypeDef",
    "AssignPrivateIpAddressesResultTypeDef",
    "AssignedPrivateIpAddressTypeDef",
    "AssociateAddressResultTypeDef",
    "AssociateClientVpnTargetNetworkResultTypeDef",
    "AssociateEnclaveCertificateIamRoleResultTypeDef",
    "AssociateIamInstanceProfileResultTypeDef",
    "AssociateRouteTableResultTypeDef",
    "AssociateSubnetCidrBlockResultTypeDef",
    "AssociateTransitGatewayMulticastDomainResultTypeDef",
    "AssociateTransitGatewayRouteTableResultTypeDef",
    "AssociateVpcCidrBlockResultTypeDef",
    "AssociatedRoleTypeDef",
    "AssociatedTargetNetworkTypeDef",
    "AssociationStatusTypeDef",
    "AthenaIntegrationTypeDef",
    "AttachClassicLinkVpcResultTypeDef",
    "AttachNetworkInterfaceResultTypeDef",
    "AttachVpnGatewayResultTypeDef",
    "AttributeBooleanValueTypeDef",
    "AttributeValueTypeDef",
    "AuthorizationRuleTypeDef",
    "AuthorizeClientVpnIngressResultTypeDef",
    "AvailabilityZoneMessageTypeDef",
    "AvailabilityZoneTypeDef",
    "AvailableCapacityTypeDef",
    "BlobAttributeValueTypeDef",
    "BlockDeviceMappingTypeDef",
    "BundleInstanceResultTypeDef",
    "BundleTaskErrorTypeDef",
    "BundleTaskTypeDef",
    "ByoipCidrTypeDef",
    "CancelBundleTaskResultTypeDef",
    "CancelCapacityReservationResultTypeDef",
    "CancelImportTaskResultTypeDef",
    "CancelReservedInstancesListingResultTypeDef",
    "CancelSpotFleetRequestsErrorItemTypeDef",
    "CancelSpotFleetRequestsErrorTypeDef",
    "CancelSpotFleetRequestsResponseTypeDef",
    "CancelSpotFleetRequestsSuccessItemTypeDef",
    "CancelSpotInstanceRequestsResultTypeDef",
    "CancelledSpotInstanceRequestTypeDef",
    "CapacityReservationGroupTypeDef",
    "CapacityReservationOptionsRequestTypeDef",
    "CapacityReservationOptionsTypeDef",
    "CapacityReservationSpecificationResponseTypeDef",
    "CapacityReservationSpecificationTypeDef",
    "CapacityReservationTargetResponseTypeDef",
    "CapacityReservationTargetTypeDef",
    "CapacityReservationTypeDef",
    "CarrierGatewayTypeDef",
    "CertificateAuthenticationRequestTypeDef",
    "CertificateAuthenticationTypeDef",
    "CidrAuthorizationContextTypeDef",
    "CidrBlockTypeDef",
    "ClassicLinkDnsSupportTypeDef",
    "ClassicLinkInstanceTypeDef",
    "ClassicLoadBalancerTypeDef",
    "ClassicLoadBalancersConfigTypeDef",
    "ClientCertificateRevocationListStatusTypeDef",
    "ClientConnectOptionsTypeDef",
    "ClientConnectResponseOptionsTypeDef",
    "ClientDataTypeDef",
    "ClientVpnAuthenticationRequestTypeDef",
    "ClientVpnAuthenticationTypeDef",
    "ClientVpnAuthorizationRuleStatusTypeDef",
    "ClientVpnConnectionStatusTypeDef",
    "ClientVpnConnectionTypeDef",
    "ClientVpnEndpointAttributeStatusTypeDef",
    "ClientVpnEndpointStatusTypeDef",
    "ClientVpnEndpointTypeDef",
    "ClientVpnRouteStatusTypeDef",
    "ClientVpnRouteTypeDef",
    "CoipAddressUsageTypeDef",
    "CoipPoolTypeDef",
    "ConfirmProductInstanceResultTypeDef",
    "ConnectionLogOptionsTypeDef",
    "ConnectionLogResponseOptionsTypeDef",
    "ConnectionNotificationTypeDef",
    "ConversionTaskTypeDef",
    "CopyFpgaImageResultTypeDef",
    "CopyImageResultTypeDef",
    "CopySnapshotResultTypeDef",
    "CpuOptionsRequestTypeDef",
    "CpuOptionsTypeDef",
    "CreateCapacityReservationResultTypeDef",
    "CreateCarrierGatewayResultTypeDef",
    "CreateClientVpnEndpointResultTypeDef",
    "CreateClientVpnRouteResultTypeDef",
    "CreateCustomerGatewayResultTypeDef",
    "CreateDefaultSubnetResultTypeDef",
    "CreateDefaultVpcResultTypeDef",
    "CreateDhcpOptionsResultTypeDef",
    "CreateEgressOnlyInternetGatewayResultTypeDef",
    "CreateFleetErrorTypeDef",
    "CreateFleetInstanceTypeDef",
    "CreateFleetResultTypeDef",
    "CreateFlowLogsResultTypeDef",
    "CreateFpgaImageResultTypeDef",
    "CreateImageResultTypeDef",
    "CreateInstanceExportTaskResultTypeDef",
    "CreateInternetGatewayResultTypeDef",
    "CreateLaunchTemplateResultTypeDef",
    "CreateLaunchTemplateVersionResultTypeDef",
    "CreateLocalGatewayRouteResultTypeDef",
    "CreateLocalGatewayRouteTableVpcAssociationResultTypeDef",
    "CreateManagedPrefixListResultTypeDef",
    "CreateNatGatewayResultTypeDef",
    "CreateNetworkAclResultTypeDef",
    "CreateNetworkInsightsPathResultTypeDef",
    "CreateNetworkInterfacePermissionResultTypeDef",
    "CreateNetworkInterfaceResultTypeDef",
    "CreatePlacementGroupResultTypeDef",
    "CreateReplaceRootVolumeTaskResultTypeDef",
    "CreateReservedInstancesListingResultTypeDef",
    "CreateRestoreImageTaskResultTypeDef",
    "CreateRouteResultTypeDef",
    "CreateRouteTableResultTypeDef",
    "CreateSecurityGroupResultTypeDef",
    "CreateSnapshotsResultTypeDef",
    "CreateSpotDatafeedSubscriptionResultTypeDef",
    "CreateStoreImageTaskResultTypeDef",
    "CreateSubnetResultTypeDef",
    "CreateTrafficMirrorFilterResultTypeDef",
    "CreateTrafficMirrorFilterRuleResultTypeDef",
    "CreateTrafficMirrorSessionResultTypeDef",
    "CreateTrafficMirrorTargetResultTypeDef",
    "CreateTransitGatewayConnectPeerResultTypeDef",
    "CreateTransitGatewayConnectRequestOptionsTypeDef",
    "CreateTransitGatewayConnectResultTypeDef",
    "CreateTransitGatewayMulticastDomainRequestOptionsTypeDef",
    "CreateTransitGatewayMulticastDomainResultTypeDef",
    "CreateTransitGatewayPeeringAttachmentResultTypeDef",
    "CreateTransitGatewayPrefixListReferenceResultTypeDef",
    "CreateTransitGatewayResultTypeDef",
    "CreateTransitGatewayRouteResultTypeDef",
    "CreateTransitGatewayRouteTableResultTypeDef",
    "CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    "CreateTransitGatewayVpcAttachmentResultTypeDef",
    "CreateVolumePermissionModificationsTypeDef",
    "CreateVolumePermissionTypeDef",
    "CreateVpcEndpointConnectionNotificationResultTypeDef",
    "CreateVpcEndpointResultTypeDef",
    "CreateVpcEndpointServiceConfigurationResultTypeDef",
    "CreateVpcPeeringConnectionResultTypeDef",
    "CreateVpcResultTypeDef",
    "CreateVpnConnectionResultTypeDef",
    "CreateVpnGatewayResultTypeDef",
    "CreditSpecificationRequestTypeDef",
    "CreditSpecificationTypeDef",
    "CustomerGatewayTypeDef",
    "DeleteCarrierGatewayResultTypeDef",
    "DeleteClientVpnEndpointResultTypeDef",
    "DeleteClientVpnRouteResultTypeDef",
    "DeleteEgressOnlyInternetGatewayResultTypeDef",
    "DeleteFleetErrorItemTypeDef",
    "DeleteFleetErrorTypeDef",
    "DeleteFleetSuccessItemTypeDef",
    "DeleteFleetsResultTypeDef",
    "DeleteFlowLogsResultTypeDef",
    "DeleteFpgaImageResultTypeDef",
    "DeleteLaunchTemplateResultTypeDef",
    "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef",
    "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef",
    "DeleteLaunchTemplateVersionsResultTypeDef",
    "DeleteLocalGatewayRouteResultTypeDef",
    "DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef",
    "DeleteManagedPrefixListResultTypeDef",
    "DeleteNatGatewayResultTypeDef",
    "DeleteNetworkInsightsAnalysisResultTypeDef",
    "DeleteNetworkInsightsPathResultTypeDef",
    "DeleteNetworkInterfacePermissionResultTypeDef",
    "DeleteQueuedReservedInstancesErrorTypeDef",
    "DeleteQueuedReservedInstancesResultTypeDef",
    "DeleteTrafficMirrorFilterResultTypeDef",
    "DeleteTrafficMirrorFilterRuleResultTypeDef",
    "DeleteTrafficMirrorSessionResultTypeDef",
    "DeleteTrafficMirrorTargetResultTypeDef",
    "DeleteTransitGatewayConnectPeerResultTypeDef",
    "DeleteTransitGatewayConnectResultTypeDef",
    "DeleteTransitGatewayMulticastDomainResultTypeDef",
    "DeleteTransitGatewayPeeringAttachmentResultTypeDef",
    "DeleteTransitGatewayPrefixListReferenceResultTypeDef",
    "DeleteTransitGatewayResultTypeDef",
    "DeleteTransitGatewayRouteResultTypeDef",
    "DeleteTransitGatewayRouteTableResultTypeDef",
    "DeleteTransitGatewayVpcAttachmentResultTypeDef",
    "DeleteVpcEndpointConnectionNotificationsResultTypeDef",
    "DeleteVpcEndpointServiceConfigurationsResultTypeDef",
    "DeleteVpcEndpointsResultTypeDef",
    "DeleteVpcPeeringConnectionResultTypeDef",
    "DeprovisionByoipCidrResultTypeDef",
    "DeregisterInstanceEventNotificationAttributesResultTypeDef",
    "DeregisterInstanceTagAttributeRequestTypeDef",
    "DeregisterTransitGatewayMulticastGroupMembersResultTypeDef",
    "DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    "DescribeAccountAttributesResultTypeDef",
    "DescribeAddressesAttributeResultTypeDef",
    "DescribeAddressesResultTypeDef",
    "DescribeAggregateIdFormatResultTypeDef",
    "DescribeAvailabilityZonesResultTypeDef",
    "DescribeBundleTasksResultTypeDef",
    "DescribeByoipCidrsResultTypeDef",
    "DescribeCapacityReservationsResultTypeDef",
    "DescribeCarrierGatewaysResultTypeDef",
    "DescribeClassicLinkInstancesResultTypeDef",
    "DescribeClientVpnAuthorizationRulesResultTypeDef",
    "DescribeClientVpnConnectionsResultTypeDef",
    "DescribeClientVpnEndpointsResultTypeDef",
    "DescribeClientVpnRoutesResultTypeDef",
    "DescribeClientVpnTargetNetworksResultTypeDef",
    "DescribeCoipPoolsResultTypeDef",
    "DescribeConversionTasksResultTypeDef",
    "DescribeCustomerGatewaysResultTypeDef",
    "DescribeDhcpOptionsResultTypeDef",
    "DescribeEgressOnlyInternetGatewaysResultTypeDef",
    "DescribeElasticGpusResultTypeDef",
    "DescribeExportImageTasksResultTypeDef",
    "DescribeExportTasksResultTypeDef",
    "DescribeFastSnapshotRestoreSuccessItemTypeDef",
    "DescribeFastSnapshotRestoresResultTypeDef",
    "DescribeFleetErrorTypeDef",
    "DescribeFleetHistoryResultTypeDef",
    "DescribeFleetInstancesResultTypeDef",
    "DescribeFleetsInstancesTypeDef",
    "DescribeFleetsResultTypeDef",
    "DescribeFlowLogsResultTypeDef",
    "DescribeFpgaImageAttributeResultTypeDef",
    "DescribeFpgaImagesResultTypeDef",
    "DescribeHostReservationOfferingsResultTypeDef",
    "DescribeHostReservationsResultTypeDef",
    "DescribeHostsResultTypeDef",
    "DescribeIamInstanceProfileAssociationsResultTypeDef",
    "DescribeIdFormatResultTypeDef",
    "DescribeIdentityIdFormatResultTypeDef",
    "DescribeImagesResultTypeDef",
    "DescribeImportImageTasksResultTypeDef",
    "DescribeImportSnapshotTasksResultTypeDef",
    "DescribeInstanceCreditSpecificationsResultTypeDef",
    "DescribeInstanceEventNotificationAttributesResultTypeDef",
    "DescribeInstanceStatusResultTypeDef",
    "DescribeInstanceTypeOfferingsResultTypeDef",
    "DescribeInstanceTypesResultTypeDef",
    "DescribeInstancesResultTypeDef",
    "DescribeInternetGatewaysResultTypeDef",
    "DescribeIpv6PoolsResultTypeDef",
    "DescribeKeyPairsResultTypeDef",
    "DescribeLaunchTemplateVersionsResultTypeDef",
    "DescribeLaunchTemplatesResultTypeDef",
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef",
    "DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef",
    "DescribeLocalGatewayRouteTablesResultTypeDef",
    "DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef",
    "DescribeLocalGatewayVirtualInterfacesResultTypeDef",
    "DescribeLocalGatewaysResultTypeDef",
    "DescribeManagedPrefixListsResultTypeDef",
    "DescribeMovingAddressesResultTypeDef",
    "DescribeNatGatewaysResultTypeDef",
    "DescribeNetworkAclsResultTypeDef",
    "DescribeNetworkInsightsAnalysesResultTypeDef",
    "DescribeNetworkInsightsPathsResultTypeDef",
    "DescribeNetworkInterfaceAttributeResultTypeDef",
    "DescribeNetworkInterfacePermissionsResultTypeDef",
    "DescribeNetworkInterfacesResultTypeDef",
    "DescribePlacementGroupsResultTypeDef",
    "DescribePrefixListsResultTypeDef",
    "DescribePrincipalIdFormatResultTypeDef",
    "DescribePublicIpv4PoolsResultTypeDef",
    "DescribeRegionsResultTypeDef",
    "DescribeReplaceRootVolumeTasksResultTypeDef",
    "DescribeReservedInstancesListingsResultTypeDef",
    "DescribeReservedInstancesModificationsResultTypeDef",
    "DescribeReservedInstancesOfferingsResultTypeDef",
    "DescribeReservedInstancesResultTypeDef",
    "DescribeRouteTablesResultTypeDef",
    "DescribeScheduledInstanceAvailabilityResultTypeDef",
    "DescribeScheduledInstancesResultTypeDef",
    "DescribeSecurityGroupReferencesResultTypeDef",
    "DescribeSecurityGroupsResultTypeDef",
    "DescribeSnapshotAttributeResultTypeDef",
    "DescribeSnapshotsResultTypeDef",
    "DescribeSpotDatafeedSubscriptionResultTypeDef",
    "DescribeSpotFleetInstancesResponseTypeDef",
    "DescribeSpotFleetRequestHistoryResponseTypeDef",
    "DescribeSpotFleetRequestsResponseTypeDef",
    "DescribeSpotInstanceRequestsResultTypeDef",
    "DescribeSpotPriceHistoryResultTypeDef",
    "DescribeStaleSecurityGroupsResultTypeDef",
    "DescribeStoreImageTasksResultTypeDef",
    "DescribeSubnetsResultTypeDef",
    "DescribeTagsResultTypeDef",
    "DescribeTrafficMirrorFiltersResultTypeDef",
    "DescribeTrafficMirrorSessionsResultTypeDef",
    "DescribeTrafficMirrorTargetsResultTypeDef",
    "DescribeTransitGatewayAttachmentsResultTypeDef",
    "DescribeTransitGatewayConnectPeersResultTypeDef",
    "DescribeTransitGatewayConnectsResultTypeDef",
    "DescribeTransitGatewayMulticastDomainsResultTypeDef",
    "DescribeTransitGatewayPeeringAttachmentsResultTypeDef",
    "DescribeTransitGatewayRouteTablesResultTypeDef",
    "DescribeTransitGatewayVpcAttachmentsResultTypeDef",
    "DescribeTransitGatewaysResultTypeDef",
    "DescribeVolumeAttributeResultTypeDef",
    "DescribeVolumeStatusResultTypeDef",
    "DescribeVolumesModificationsResultTypeDef",
    "DescribeVolumesResultTypeDef",
    "DescribeVpcAttributeResultTypeDef",
    "DescribeVpcClassicLinkDnsSupportResultTypeDef",
    "DescribeVpcClassicLinkResultTypeDef",
    "DescribeVpcEndpointConnectionNotificationsResultTypeDef",
    "DescribeVpcEndpointConnectionsResultTypeDef",
    "DescribeVpcEndpointServiceConfigurationsResultTypeDef",
    "DescribeVpcEndpointServicePermissionsResultTypeDef",
    "DescribeVpcEndpointServicesResultTypeDef",
    "DescribeVpcEndpointsResultTypeDef",
    "DescribeVpcPeeringConnectionsResultTypeDef",
    "DescribeVpcsResultTypeDef",
    "DescribeVpnConnectionsResultTypeDef",
    "DescribeVpnGatewaysResultTypeDef",
    "DetachClassicLinkVpcResultTypeDef",
    "DhcpConfigurationTypeDef",
    "DhcpOptionsTypeDef",
    "DirectoryServiceAuthenticationRequestTypeDef",
    "DirectoryServiceAuthenticationTypeDef",
    "DisableEbsEncryptionByDefaultResultTypeDef",
    "DisableFastSnapshotRestoreErrorItemTypeDef",
    "DisableFastSnapshotRestoreStateErrorItemTypeDef",
    "DisableFastSnapshotRestoreStateErrorTypeDef",
    "DisableFastSnapshotRestoreSuccessItemTypeDef",
    "DisableFastSnapshotRestoresResultTypeDef",
    "DisableSerialConsoleAccessResultTypeDef",
    "DisableTransitGatewayRouteTablePropagationResultTypeDef",
    "DisableVpcClassicLinkDnsSupportResultTypeDef",
    "DisableVpcClassicLinkResultTypeDef",
    "DisassociateClientVpnTargetNetworkResultTypeDef",
    "DisassociateEnclaveCertificateIamRoleResultTypeDef",
    "DisassociateIamInstanceProfileResultTypeDef",
    "DisassociateSubnetCidrBlockResultTypeDef",
    "DisassociateTransitGatewayMulticastDomainResultTypeDef",
    "DisassociateTransitGatewayRouteTableResultTypeDef",
    "DisassociateVpcCidrBlockResultTypeDef",
    "DiskImageDescriptionTypeDef",
    "DiskImageDetailTypeDef",
    "DiskImageTypeDef",
    "DiskImageVolumeDescriptionTypeDef",
    "DiskInfoTypeDef",
    "DnsEntryTypeDef",
    "DnsServersOptionsModifyStructureTypeDef",
    "EbsBlockDeviceTypeDef",
    "EbsInfoTypeDef",
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    "EbsInstanceBlockDeviceTypeDef",
    "EbsOptimizedInfoTypeDef",
    "EfaInfoTypeDef",
    "EgressOnlyInternetGatewayTypeDef",
    "ElasticGpuAssociationTypeDef",
    "ElasticGpuHealthTypeDef",
    "ElasticGpuSpecificationResponseTypeDef",
    "ElasticGpuSpecificationTypeDef",
    "ElasticGpusTypeDef",
    "ElasticInferenceAcceleratorAssociationTypeDef",
    "ElasticInferenceAcceleratorTypeDef",
    "EnableEbsEncryptionByDefaultResultTypeDef",
    "EnableFastSnapshotRestoreErrorItemTypeDef",
    "EnableFastSnapshotRestoreStateErrorItemTypeDef",
    "EnableFastSnapshotRestoreStateErrorTypeDef",
    "EnableFastSnapshotRestoreSuccessItemTypeDef",
    "EnableFastSnapshotRestoresResultTypeDef",
    "EnableSerialConsoleAccessResultTypeDef",
    "EnableTransitGatewayRouteTablePropagationResultTypeDef",
    "EnableVpcClassicLinkDnsSupportResultTypeDef",
    "EnableVpcClassicLinkResultTypeDef",
    "EnclaveOptionsRequestTypeDef",
    "EnclaveOptionsTypeDef",
    "EventInformationTypeDef",
    "ExplanationTypeDef",
    "ExportClientVpnClientCertificateRevocationListResultTypeDef",
    "ExportClientVpnClientConfigurationResultTypeDef",
    "ExportImageResultTypeDef",
    "ExportImageTaskTypeDef",
    "ExportTaskS3LocationRequestTypeDef",
    "ExportTaskS3LocationTypeDef",
    "ExportTaskTypeDef",
    "ExportToS3TaskSpecificationTypeDef",
    "ExportToS3TaskTypeDef",
    "ExportTransitGatewayRoutesResultTypeDef",
    "FailedQueuedPurchaseDeletionTypeDef",
    "FederatedAuthenticationRequestTypeDef",
    "FederatedAuthenticationTypeDef",
    "FilterTypeDef",
    "FleetDataTypeDef",
    "FleetLaunchTemplateConfigRequestTypeDef",
    "FleetLaunchTemplateConfigTypeDef",
    "FleetLaunchTemplateOverridesRequestTypeDef",
    "FleetLaunchTemplateOverridesTypeDef",
    "FleetLaunchTemplateSpecificationRequestTypeDef",
    "FleetLaunchTemplateSpecificationTypeDef",
    "FleetSpotCapacityRebalanceRequestTypeDef",
    "FleetSpotCapacityRebalanceTypeDef",
    "FleetSpotMaintenanceStrategiesRequestTypeDef",
    "FleetSpotMaintenanceStrategiesTypeDef",
    "FlowLogTypeDef",
    "FpgaDeviceInfoTypeDef",
    "FpgaDeviceMemoryInfoTypeDef",
    "FpgaImageAttributeTypeDef",
    "FpgaImageStateTypeDef",
    "FpgaImageTypeDef",
    "FpgaInfoTypeDef",
    "GetAssociatedEnclaveCertificateIamRolesResultTypeDef",
    "GetAssociatedIpv6PoolCidrsResultTypeDef",
    "GetCapacityReservationUsageResultTypeDef",
    "GetCoipPoolUsageResultTypeDef",
    "GetConsoleOutputResultTypeDef",
    "GetConsoleScreenshotResultTypeDef",
    "GetDefaultCreditSpecificationResultTypeDef",
    "GetEbsDefaultKmsKeyIdResultTypeDef",
    "GetEbsEncryptionByDefaultResultTypeDef",
    "GetFlowLogsIntegrationTemplateResultTypeDef",
    "GetGroupsForCapacityReservationResultTypeDef",
    "GetHostReservationPurchasePreviewResultTypeDef",
    "GetLaunchTemplateDataResultTypeDef",
    "GetManagedPrefixListAssociationsResultTypeDef",
    "GetManagedPrefixListEntriesResultTypeDef",
    "GetPasswordDataResultTypeDef",
    "GetReservedInstancesExchangeQuoteResultTypeDef",
    "GetSerialConsoleAccessStatusResultTypeDef",
    "GetTransitGatewayAttachmentPropagationsResultTypeDef",
    "GetTransitGatewayMulticastDomainAssociationsResultTypeDef",
    "GetTransitGatewayPrefixListReferencesResultTypeDef",
    "GetTransitGatewayRouteTableAssociationsResultTypeDef",
    "GetTransitGatewayRouteTablePropagationsResultTypeDef",
    "GpuDeviceInfoTypeDef",
    "GpuDeviceMemoryInfoTypeDef",
    "GpuInfoTypeDef",
    "GroupIdentifierTypeDef",
    "HibernationOptionsRequestTypeDef",
    "HibernationOptionsTypeDef",
    "HistoryRecordEntryTypeDef",
    "HistoryRecordTypeDef",
    "HostInstanceTypeDef",
    "HostOfferingTypeDef",
    "HostPropertiesTypeDef",
    "HostReservationTypeDef",
    "HostTypeDef",
    "IKEVersionsListValueTypeDef",
    "IKEVersionsRequestListValueTypeDef",
    "IamInstanceProfileAssociationTypeDef",
    "IamInstanceProfileSpecificationTypeDef",
    "IamInstanceProfileTypeDef",
    "IcmpTypeCodeTypeDef",
    "IdFormatTypeDef",
    "ImageAttributeTypeDef",
    "ImageDiskContainerTypeDef",
    "ImageTypeDef",
    "ImportClientVpnClientCertificateRevocationListResultTypeDef",
    "ImportImageLicenseConfigurationRequestTypeDef",
    "ImportImageLicenseConfigurationResponseTypeDef",
    "ImportImageResultTypeDef",
    "ImportImageTaskTypeDef",
    "ImportInstanceLaunchSpecificationTypeDef",
    "ImportInstanceResultTypeDef",
    "ImportInstanceTaskDetailsTypeDef",
    "ImportInstanceVolumeDetailItemTypeDef",
    "ImportKeyPairResultTypeDef",
    "ImportSnapshotResultTypeDef",
    "ImportSnapshotTaskTypeDef",
    "ImportVolumeResultTypeDef",
    "ImportVolumeTaskDetailsTypeDef",
    "InferenceAcceleratorInfoTypeDef",
    "InferenceDeviceInfoTypeDef",
    "InstanceAttributeTypeDef",
    "InstanceBlockDeviceMappingSpecificationTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "InstanceCapacityTypeDef",
    "InstanceCountTypeDef",
    "InstanceCreditSpecificationRequestTypeDef",
    "InstanceCreditSpecificationTypeDef",
    "InstanceExportDetailsTypeDef",
    "InstanceFamilyCreditSpecificationTypeDef",
    "InstanceIpv6AddressRequestTypeDef",
    "InstanceIpv6AddressTypeDef",
    "InstanceMarketOptionsRequestTypeDef",
    "InstanceMetadataOptionsRequestTypeDef",
    "InstanceMetadataOptionsResponseTypeDef",
    "InstanceMonitoringTypeDef",
    "InstanceNetworkInterfaceAssociationTypeDef",
    "InstanceNetworkInterfaceAttachmentTypeDef",
    "InstanceNetworkInterfaceSpecificationTypeDef",
    "InstanceNetworkInterfaceTypeDef",
    "InstancePrivateIpAddressTypeDef",
    "InstanceSpecificationTypeDef",
    "InstanceStateChangeTypeDef",
    "InstanceStateTypeDef",
    "InstanceStatusDetailsTypeDef",
    "InstanceStatusEventTypeDef",
    "InstanceStatusSummaryTypeDef",
    "InstanceStatusTypeDef",
    "InstanceStorageInfoTypeDef",
    "InstanceTagNotificationAttributeTypeDef",
    "InstanceTypeDef",
    "InstanceTypeInfoTypeDef",
    "InstanceTypeOfferingTypeDef",
    "InstanceUsageTypeDef",
    "IntegrateServicesTypeDef",
    "InternetGatewayAttachmentTypeDef",
    "InternetGatewayTypeDef",
    "IpPermissionTypeDef",
    "IpRangeTypeDef",
    "Ipv6CidrAssociationTypeDef",
    "Ipv6CidrBlockTypeDef",
    "Ipv6PoolTypeDef",
    "Ipv6RangeTypeDef",
    "KeyPairInfoTypeDef",
    "KeyPairTypeDef",
    "LastErrorTypeDef",
    "LaunchPermissionModificationsTypeDef",
    "LaunchPermissionTypeDef",
    "LaunchSpecificationTypeDef",
    "LaunchTemplateAndOverridesResponseTypeDef",
    "LaunchTemplateBlockDeviceMappingRequestTypeDef",
    "LaunchTemplateBlockDeviceMappingTypeDef",
    "LaunchTemplateCapacityReservationSpecificationRequestTypeDef",
    "LaunchTemplateCapacityReservationSpecificationResponseTypeDef",
    "LaunchTemplateConfigTypeDef",
    "LaunchTemplateCpuOptionsRequestTypeDef",
    "LaunchTemplateCpuOptionsTypeDef",
    "LaunchTemplateEbsBlockDeviceRequestTypeDef",
    "LaunchTemplateEbsBlockDeviceTypeDef",
    "LaunchTemplateElasticInferenceAcceleratorResponseTypeDef",
    "LaunchTemplateElasticInferenceAcceleratorTypeDef",
    "LaunchTemplateEnclaveOptionsRequestTypeDef",
    "LaunchTemplateEnclaveOptionsTypeDef",
    "LaunchTemplateHibernationOptionsRequestTypeDef",
    "LaunchTemplateHibernationOptionsTypeDef",
    "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef",
    "LaunchTemplateIamInstanceProfileSpecificationTypeDef",
    "LaunchTemplateInstanceMarketOptionsRequestTypeDef",
    "LaunchTemplateInstanceMarketOptionsTypeDef",
    "LaunchTemplateInstanceMetadataOptionsRequestTypeDef",
    "LaunchTemplateInstanceMetadataOptionsTypeDef",
    "LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef",
    "LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef",
    "LaunchTemplateLicenseConfigurationRequestTypeDef",
    "LaunchTemplateLicenseConfigurationTypeDef",
    "LaunchTemplateOverridesTypeDef",
    "LaunchTemplatePlacementRequestTypeDef",
    "LaunchTemplatePlacementTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LaunchTemplateSpotMarketOptionsRequestTypeDef",
    "LaunchTemplateSpotMarketOptionsTypeDef",
    "LaunchTemplateTagSpecificationRequestTypeDef",
    "LaunchTemplateTagSpecificationTypeDef",
    "LaunchTemplateTypeDef",
    "LaunchTemplateVersionTypeDef",
    "LaunchTemplatesMonitoringRequestTypeDef",
    "LaunchTemplatesMonitoringTypeDef",
    "LicenseConfigurationRequestTypeDef",
    "LicenseConfigurationTypeDef",
    "LoadBalancersConfigTypeDef",
    "LoadPermissionModificationsTypeDef",
    "LoadPermissionRequestTypeDef",
    "LoadPermissionTypeDef",
    "LocalGatewayRouteTableTypeDef",
    "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef",
    "LocalGatewayRouteTableVpcAssociationTypeDef",
    "LocalGatewayRouteTypeDef",
    "LocalGatewayTypeDef",
    "LocalGatewayVirtualInterfaceGroupTypeDef",
    "LocalGatewayVirtualInterfaceTypeDef",
    "ManagedPrefixListTypeDef",
    "MemoryInfoTypeDef",
    "ModifyAddressAttributeResultTypeDef",
    "ModifyAvailabilityZoneGroupResultTypeDef",
    "ModifyCapacityReservationResultTypeDef",
    "ModifyClientVpnEndpointResultTypeDef",
    "ModifyDefaultCreditSpecificationResultTypeDef",
    "ModifyEbsDefaultKmsKeyIdResultTypeDef",
    "ModifyFleetResultTypeDef",
    "ModifyFpgaImageAttributeResultTypeDef",
    "ModifyHostsResultTypeDef",
    "ModifyInstanceCapacityReservationAttributesResultTypeDef",
    "ModifyInstanceCreditSpecificationResultTypeDef",
    "ModifyInstanceEventStartTimeResultTypeDef",
    "ModifyInstanceMetadataOptionsResultTypeDef",
    "ModifyInstancePlacementResultTypeDef",
    "ModifyLaunchTemplateResultTypeDef",
    "ModifyManagedPrefixListResultTypeDef",
    "ModifyReservedInstancesResultTypeDef",
    "ModifySpotFleetRequestResponseTypeDef",
    "ModifyTrafficMirrorFilterNetworkServicesResultTypeDef",
    "ModifyTrafficMirrorFilterRuleResultTypeDef",
    "ModifyTrafficMirrorSessionResultTypeDef",
    "ModifyTransitGatewayOptionsTypeDef",
    "ModifyTransitGatewayPrefixListReferenceResultTypeDef",
    "ModifyTransitGatewayResultTypeDef",
    "ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    "ModifyTransitGatewayVpcAttachmentResultTypeDef",
    "ModifyVolumeResultTypeDef",
    "ModifyVpcEndpointConnectionNotificationResultTypeDef",
    "ModifyVpcEndpointResultTypeDef",
    "ModifyVpcEndpointServiceConfigurationResultTypeDef",
    "ModifyVpcEndpointServicePermissionsResultTypeDef",
    "ModifyVpcPeeringConnectionOptionsResultTypeDef",
    "ModifyVpcTenancyResultTypeDef",
    "ModifyVpnConnectionOptionsResultTypeDef",
    "ModifyVpnConnectionResultTypeDef",
    "ModifyVpnTunnelCertificateResultTypeDef",
    "ModifyVpnTunnelOptionsResultTypeDef",
    "ModifyVpnTunnelOptionsSpecificationTypeDef",
    "MonitorInstancesResultTypeDef",
    "MonitoringTypeDef",
    "MoveAddressToVpcResultTypeDef",
    "MovingAddressStatusTypeDef",
    "NatGatewayAddressTypeDef",
    "NatGatewayTypeDef",
    "NetworkAclAssociationTypeDef",
    "NetworkAclEntryTypeDef",
    "NetworkAclTypeDef",
    "NetworkCardInfoTypeDef",
    "NetworkInfoTypeDef",
    "NetworkInsightsAnalysisTypeDef",
    "NetworkInsightsPathTypeDef",
    "NetworkInterfaceAssociationTypeDef",
    "NetworkInterfaceAttachmentChangesTypeDef",
    "NetworkInterfaceAttachmentTypeDef",
    "NetworkInterfaceIpv6AddressTypeDef",
    "NetworkInterfacePermissionStateTypeDef",
    "NetworkInterfacePermissionTypeDef",
    "NetworkInterfacePrivateIpAddressTypeDef",
    "NetworkInterfaceTypeDef",
    "NewDhcpConfigurationTypeDef",
    "OnDemandOptionsRequestTypeDef",
    "OnDemandOptionsTypeDef",
    "PaginatorConfigTypeDef",
    "PathComponentTypeDef",
    "PciIdTypeDef",
    "PeeringAttachmentStatusTypeDef",
    "PeeringConnectionOptionsRequestTypeDef",
    "PeeringConnectionOptionsTypeDef",
    "PeeringTgwInfoTypeDef",
    "Phase1DHGroupNumbersListValueTypeDef",
    "Phase1DHGroupNumbersRequestListValueTypeDef",
    "Phase1EncryptionAlgorithmsListValueTypeDef",
    "Phase1EncryptionAlgorithmsRequestListValueTypeDef",
    "Phase1IntegrityAlgorithmsListValueTypeDef",
    "Phase1IntegrityAlgorithmsRequestListValueTypeDef",
    "Phase2DHGroupNumbersListValueTypeDef",
    "Phase2DHGroupNumbersRequestListValueTypeDef",
    "Phase2EncryptionAlgorithmsListValueTypeDef",
    "Phase2EncryptionAlgorithmsRequestListValueTypeDef",
    "Phase2IntegrityAlgorithmsListValueTypeDef",
    "Phase2IntegrityAlgorithmsRequestListValueTypeDef",
    "PlacementGroupInfoTypeDef",
    "PlacementGroupTypeDef",
    "PlacementResponseTypeDef",
    "PlacementTypeDef",
    "PoolCidrBlockTypeDef",
    "PortRangeTypeDef",
    "PrefixListAssociationTypeDef",
    "PrefixListEntryTypeDef",
    "PrefixListIdTypeDef",
    "PrefixListTypeDef",
    "PriceScheduleSpecificationTypeDef",
    "PriceScheduleTypeDef",
    "PricingDetailTypeDef",
    "PrincipalIdFormatTypeDef",
    "PrivateDnsDetailsTypeDef",
    "PrivateDnsNameConfigurationTypeDef",
    "PrivateIpAddressSpecificationTypeDef",
    "ProcessorInfoTypeDef",
    "ProductCodeTypeDef",
    "PropagatingVgwTypeDef",
    "ProvisionByoipCidrResultTypeDef",
    "ProvisionedBandwidthTypeDef",
    "PtrUpdateStatusTypeDef",
    "PublicIpv4PoolRangeTypeDef",
    "PublicIpv4PoolTypeDef",
    "PurchaseHostReservationResultTypeDef",
    "PurchaseRequestTypeDef",
    "PurchaseReservedInstancesOfferingResultTypeDef",
    "PurchaseScheduledInstancesResultTypeDef",
    "PurchaseTypeDef",
    "RecurringChargeTypeDef",
    "RegionTypeDef",
    "RegisterImageResultTypeDef",
    "RegisterInstanceEventNotificationAttributesResultTypeDef",
    "RegisterInstanceTagAttributeRequestTypeDef",
    "RegisterTransitGatewayMulticastGroupMembersResultTypeDef",
    "RegisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    "RejectTransitGatewayMulticastDomainAssociationsResultTypeDef",
    "RejectTransitGatewayPeeringAttachmentResultTypeDef",
    "RejectTransitGatewayVpcAttachmentResultTypeDef",
    "RejectVpcEndpointConnectionsResultTypeDef",
    "RejectVpcPeeringConnectionResultTypeDef",
    "ReleaseHostsResultTypeDef",
    "RemovePrefixListEntryTypeDef",
    "ReplaceIamInstanceProfileAssociationResultTypeDef",
    "ReplaceNetworkAclAssociationResultTypeDef",
    "ReplaceRootVolumeTaskTypeDef",
    "ReplaceRouteTableAssociationResultTypeDef",
    "ReplaceTransitGatewayRouteResultTypeDef",
    "RequestLaunchTemplateDataTypeDef",
    "RequestSpotFleetResponseTypeDef",
    "RequestSpotInstancesResultTypeDef",
    "RequestSpotLaunchSpecificationTypeDef",
    "ReservationTypeDef",
    "ReservationValueTypeDef",
    "ReservedInstanceLimitPriceTypeDef",
    "ReservedInstanceReservationValueTypeDef",
    "ReservedInstancesConfigurationTypeDef",
    "ReservedInstancesIdTypeDef",
    "ReservedInstancesListingTypeDef",
    "ReservedInstancesModificationResultTypeDef",
    "ReservedInstancesModificationTypeDef",
    "ReservedInstancesOfferingTypeDef",
    "ReservedInstancesTypeDef",
    "ResetAddressAttributeResultTypeDef",
    "ResetEbsDefaultKmsKeyIdResultTypeDef",
    "ResetFpgaImageAttributeResultTypeDef",
    "ResponseErrorTypeDef",
    "ResponseLaunchTemplateDataTypeDef",
    "RestoreAddressToClassicResultTypeDef",
    "RestoreManagedPrefixListVersionResultTypeDef",
    "RevokeClientVpnIngressResultTypeDef",
    "RevokeSecurityGroupEgressResultTypeDef",
    "RevokeSecurityGroupIngressResultTypeDef",
    "RouteTableAssociationStateTypeDef",
    "RouteTableAssociationTypeDef",
    "RouteTableTypeDef",
    "RouteTypeDef",
    "RunInstancesMonitoringEnabledTypeDef",
    "RunScheduledInstancesResultTypeDef",
    "S3ObjectTagTypeDef",
    "S3StorageTypeDef",
    "ScheduledInstanceAvailabilityTypeDef",
    "ScheduledInstanceRecurrenceRequestTypeDef",
    "ScheduledInstanceRecurrenceTypeDef",
    "ScheduledInstanceTypeDef",
    "ScheduledInstancesBlockDeviceMappingTypeDef",
    "ScheduledInstancesEbsTypeDef",
    "ScheduledInstancesIamInstanceProfileTypeDef",
    "ScheduledInstancesIpv6AddressTypeDef",
    "ScheduledInstancesLaunchSpecificationTypeDef",
    "ScheduledInstancesMonitoringTypeDef",
    "ScheduledInstancesNetworkInterfaceTypeDef",
    "ScheduledInstancesPlacementTypeDef",
    "ScheduledInstancesPrivateIpAddressConfigTypeDef",
    "SearchLocalGatewayRoutesResultTypeDef",
    "SearchTransitGatewayMulticastGroupsResultTypeDef",
    "SearchTransitGatewayRoutesResultTypeDef",
    "SecurityGroupIdentifierTypeDef",
    "SecurityGroupReferenceTypeDef",
    "SecurityGroupTypeDef",
    "ServiceConfigurationTypeDef",
    "ServiceDetailTypeDef",
    "ServiceTypeDetailTypeDef",
    "SlotDateTimeRangeRequestTypeDef",
    "SlotStartTimeRangeRequestTypeDef",
    "SnapshotDetailTypeDef",
    "SnapshotDiskContainerTypeDef",
    "SnapshotInfoTypeDef",
    "SnapshotTaskDetailTypeDef",
    "SnapshotTypeDef",
    "SpotCapacityRebalanceTypeDef",
    "SpotDatafeedSubscriptionTypeDef",
    "SpotFleetLaunchSpecificationTypeDef",
    "SpotFleetMonitoringTypeDef",
    "SpotFleetRequestConfigDataTypeDef",
    "SpotFleetRequestConfigTypeDef",
    "SpotFleetTagSpecificationTypeDef",
    "SpotInstanceRequestTypeDef",
    "SpotInstanceStateFaultTypeDef",
    "SpotInstanceStatusTypeDef",
    "SpotMaintenanceStrategiesTypeDef",
    "SpotMarketOptionsTypeDef",
    "SpotOptionsRequestTypeDef",
    "SpotOptionsTypeDef",
    "SpotPlacementTypeDef",
    "SpotPriceTypeDef",
    "StaleIpPermissionTypeDef",
    "StaleSecurityGroupTypeDef",
    "StartInstancesResultTypeDef",
    "StartNetworkInsightsAnalysisResultTypeDef",
    "StartVpcEndpointServicePrivateDnsVerificationResultTypeDef",
    "StateReasonTypeDef",
    "StopInstancesResultTypeDef",
    "StorageLocationTypeDef",
    "StorageTypeDef",
    "StoreImageTaskResultTypeDef",
    "SubnetAssociationTypeDef",
    "SubnetCidrBlockStateTypeDef",
    "SubnetIpv6CidrBlockAssociationTypeDef",
    "SubnetTypeDef",
    "SuccessfulInstanceCreditSpecificationItemTypeDef",
    "SuccessfulQueuedPurchaseDeletionTypeDef",
    "TagDescriptionTypeDef",
    "TagSpecificationTypeDef",
    "TagTypeDef",
    "TargetCapacitySpecificationRequestTypeDef",
    "TargetCapacitySpecificationTypeDef",
    "TargetConfigurationRequestTypeDef",
    "TargetConfigurationTypeDef",
    "TargetGroupTypeDef",
    "TargetGroupsConfigTypeDef",
    "TargetNetworkTypeDef",
    "TargetReservationValueTypeDef",
    "TerminateClientVpnConnectionsResultTypeDef",
    "TerminateConnectionStatusTypeDef",
    "TerminateInstancesResultTypeDef",
    "TrafficMirrorFilterRuleTypeDef",
    "TrafficMirrorFilterTypeDef",
    "TrafficMirrorPortRangeRequestTypeDef",
    "TrafficMirrorPortRangeTypeDef",
    "TrafficMirrorSessionTypeDef",
    "TrafficMirrorTargetTypeDef",
    "TransitGatewayAssociationTypeDef",
    "TransitGatewayAttachmentAssociationTypeDef",
    "TransitGatewayAttachmentBgpConfigurationTypeDef",
    "TransitGatewayAttachmentPropagationTypeDef",
    "TransitGatewayAttachmentTypeDef",
    "TransitGatewayConnectOptionsTypeDef",
    "TransitGatewayConnectPeerConfigurationTypeDef",
    "TransitGatewayConnectPeerTypeDef",
    "TransitGatewayConnectRequestBgpOptionsTypeDef",
    "TransitGatewayConnectTypeDef",
    "TransitGatewayMulticastDeregisteredGroupMembersTypeDef",
    "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef",
    "TransitGatewayMulticastDomainAssociationTypeDef",
    "TransitGatewayMulticastDomainAssociationsTypeDef",
    "TransitGatewayMulticastDomainOptionsTypeDef",
    "TransitGatewayMulticastDomainTypeDef",
    "TransitGatewayMulticastGroupTypeDef",
    "TransitGatewayMulticastRegisteredGroupMembersTypeDef",
    "TransitGatewayMulticastRegisteredGroupSourcesTypeDef",
    "TransitGatewayOptionsTypeDef",
    "TransitGatewayPeeringAttachmentTypeDef",
    "TransitGatewayPrefixListAttachmentTypeDef",
    "TransitGatewayPrefixListReferenceTypeDef",
    "TransitGatewayPropagationTypeDef",
    "TransitGatewayRequestOptionsTypeDef",
    "TransitGatewayRouteAttachmentTypeDef",
    "TransitGatewayRouteTableAssociationTypeDef",
    "TransitGatewayRouteTablePropagationTypeDef",
    "TransitGatewayRouteTableTypeDef",
    "TransitGatewayRouteTypeDef",
    "TransitGatewayTypeDef",
    "TransitGatewayVpcAttachmentOptionsTypeDef",
    "TransitGatewayVpcAttachmentTypeDef",
    "TunnelOptionTypeDef",
    "UnassignIpv6AddressesResultTypeDef",
    "UnmonitorInstancesResultTypeDef",
    "UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef",
    "UnsuccessfulInstanceCreditSpecificationItemTypeDef",
    "UnsuccessfulItemErrorTypeDef",
    "UnsuccessfulItemTypeDef",
    "UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef",
    "UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef",
    "UserBucketDetailsTypeDef",
    "UserBucketTypeDef",
    "UserDataTypeDef",
    "UserIdGroupPairTypeDef",
    "VCpuInfoTypeDef",
    "ValidationErrorTypeDef",
    "ValidationWarningTypeDef",
    "VgwTelemetryTypeDef",
    "VolumeAttachmentTypeDef",
    "VolumeDetailTypeDef",
    "VolumeModificationTypeDef",
    "VolumeStatusActionTypeDef",
    "VolumeStatusAttachmentStatusTypeDef",
    "VolumeStatusDetailsTypeDef",
    "VolumeStatusEventTypeDef",
    "VolumeStatusInfoTypeDef",
    "VolumeStatusItemTypeDef",
    "VolumeTypeDef",
    "VpcAttachmentTypeDef",
    "VpcCidrBlockAssociationTypeDef",
    "VpcCidrBlockStateTypeDef",
    "VpcClassicLinkTypeDef",
    "VpcEndpointConnectionTypeDef",
    "VpcEndpointTypeDef",
    "VpcIpv6CidrBlockAssociationTypeDef",
    "VpcPeeringConnectionOptionsDescriptionTypeDef",
    "VpcPeeringConnectionStateReasonTypeDef",
    "VpcPeeringConnectionTypeDef",
    "VpcPeeringConnectionVpcInfoTypeDef",
    "VpcTypeDef",
    "VpnConnectionOptionsSpecificationTypeDef",
    "VpnConnectionOptionsTypeDef",
    "VpnConnectionTypeDef",
    "VpnGatewayTypeDef",
    "VpnStaticRouteTypeDef",
    "VpnTunnelOptionsSpecificationTypeDef",
    "WaiterConfigTypeDef",
    "WithdrawByoipCidrResultTypeDef",
)


class AcceptReservedInstancesExchangeQuoteResultTypeDef(TypedDict, total=False):
    ExchangeId: str


class AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef(TypedDict, total=False):
    Associations: "TransitGatewayMulticastDomainAssociationsTypeDef"


class AcceptTransitGatewayPeeringAttachmentResultTypeDef(TypedDict, total=False):
    TransitGatewayPeeringAttachment: "TransitGatewayPeeringAttachmentTypeDef"


class AcceptTransitGatewayVpcAttachmentResultTypeDef(TypedDict, total=False):
    TransitGatewayVpcAttachment: "TransitGatewayVpcAttachmentTypeDef"


class AcceptVpcEndpointConnectionsResultTypeDef(TypedDict, total=False):
    Unsuccessful: List["UnsuccessfulItemTypeDef"]


class AcceptVpcPeeringConnectionResultTypeDef(TypedDict, total=False):
    VpcPeeringConnection: "VpcPeeringConnectionTypeDef"


class AccountAttributeTypeDef(TypedDict, total=False):
    AttributeName: str
    AttributeValues: List["AccountAttributeValueTypeDef"]


class AccountAttributeValueTypeDef(TypedDict, total=False):
    AttributeValue: str


class ActiveInstanceTypeDef(TypedDict, total=False):
    InstanceId: str
    InstanceType: str
    SpotInstanceRequestId: str
    InstanceHealth: InstanceHealthStatus


class _RequiredAddPrefixListEntryTypeDef(TypedDict):
    Cidr: str


class AddPrefixListEntryTypeDef(_RequiredAddPrefixListEntryTypeDef, total=False):
    Description: str


class AddressAttributeTypeDef(TypedDict, total=False):
    PublicIp: str
    AllocationId: str
    PtrRecord: str
    PtrRecordUpdate: "PtrUpdateStatusTypeDef"


class AddressTypeDef(TypedDict, total=False):
    InstanceId: str
    PublicIp: str
    AllocationId: str
    AssociationId: str
    Domain: DomainType
    NetworkInterfaceId: str
    NetworkInterfaceOwnerId: str
    PrivateIpAddress: str
    Tags: List["TagTypeDef"]
    PublicIpv4Pool: str
    NetworkBorderGroup: str
    CustomerOwnedIp: str
    CustomerOwnedIpv4Pool: str
    CarrierIp: str


class AdvertiseByoipCidrResultTypeDef(TypedDict, total=False):
    ByoipCidr: "ByoipCidrTypeDef"


class AllocateAddressResultTypeDef(TypedDict, total=False):
    PublicIp: str
    AllocationId: str
    PublicIpv4Pool: str
    NetworkBorderGroup: str
    Domain: DomainType
    CustomerOwnedIp: str
    CustomerOwnedIpv4Pool: str
    CarrierIp: str


class AllocateHostsResultTypeDef(TypedDict, total=False):
    HostIds: List[str]


class AllowedPrincipalTypeDef(TypedDict, total=False):
    PrincipalType: PrincipalType
    Principal: str


class AlternatePathHintTypeDef(TypedDict, total=False):
    ComponentId: str
    ComponentArn: str


AnalysisAclRuleTypeDef = TypedDict(
    "AnalysisAclRuleTypeDef",
    {
        "Cidr": str,
        "Egress": bool,
        "PortRange": "PortRangeTypeDef",
        "Protocol": str,
        "RuleAction": str,
        "RuleNumber": int,
    },
    total=False,
)


class AnalysisComponentTypeDef(TypedDict, total=False):
    Id: str
    Arn: str


class AnalysisLoadBalancerListenerTypeDef(TypedDict, total=False):
    LoadBalancerPort: int
    InstancePort: int


class AnalysisLoadBalancerTargetTypeDef(TypedDict, total=False):
    Address: str
    AvailabilityZone: str
    Instance: "AnalysisComponentTypeDef"
    Port: int


AnalysisPacketHeaderTypeDef = TypedDict(
    "AnalysisPacketHeaderTypeDef",
    {
        "DestinationAddresses": List[str],
        "DestinationPortRanges": List["PortRangeTypeDef"],
        "Protocol": str,
        "SourceAddresses": List[str],
        "SourcePortRanges": List["PortRangeTypeDef"],
    },
    total=False,
)


class AnalysisRouteTableRouteTypeDef(TypedDict, total=False):
    DestinationCidr: str
    DestinationPrefixListId: str
    EgressOnlyInternetGatewayId: str
    GatewayId: str
    InstanceId: str
    NatGatewayId: str
    NetworkInterfaceId: str
    Origin: str
    TransitGatewayId: str
    VpcPeeringConnectionId: str


AnalysisSecurityGroupRuleTypeDef = TypedDict(
    "AnalysisSecurityGroupRuleTypeDef",
    {
        "Cidr": str,
        "Direction": str,
        "SecurityGroupId": str,
        "PortRange": "PortRangeTypeDef",
        "PrefixListId": str,
        "Protocol": str,
    },
    total=False,
)


class ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef(TypedDict, total=False):
    SecurityGroupIds: List[str]


class AssignIpv6AddressesResultTypeDef(TypedDict, total=False):
    AssignedIpv6Addresses: List[str]
    NetworkInterfaceId: str


class AssignPrivateIpAddressesResultTypeDef(TypedDict, total=False):
    NetworkInterfaceId: str
    AssignedPrivateIpAddresses: List["AssignedPrivateIpAddressTypeDef"]


class AssignedPrivateIpAddressTypeDef(TypedDict, total=False):
    PrivateIpAddress: str


class AssociateAddressResultTypeDef(TypedDict, total=False):
    AssociationId: str


class AssociateClientVpnTargetNetworkResultTypeDef(TypedDict, total=False):
    AssociationId: str
    Status: "AssociationStatusTypeDef"


class AssociateEnclaveCertificateIamRoleResultTypeDef(TypedDict, total=False):
    CertificateS3BucketName: str
    CertificateS3ObjectKey: str
    EncryptionKmsKeyId: str


class AssociateIamInstanceProfileResultTypeDef(TypedDict, total=False):
    IamInstanceProfileAssociation: "IamInstanceProfileAssociationTypeDef"


class AssociateRouteTableResultTypeDef(TypedDict, total=False):
    AssociationId: str
    AssociationState: "RouteTableAssociationStateTypeDef"


class AssociateSubnetCidrBlockResultTypeDef(TypedDict, total=False):
    Ipv6CidrBlockAssociation: "SubnetIpv6CidrBlockAssociationTypeDef"
    SubnetId: str


class AssociateTransitGatewayMulticastDomainResultTypeDef(TypedDict, total=False):
    Associations: "TransitGatewayMulticastDomainAssociationsTypeDef"


class AssociateTransitGatewayRouteTableResultTypeDef(TypedDict, total=False):
    Association: "TransitGatewayAssociationTypeDef"


class AssociateVpcCidrBlockResultTypeDef(TypedDict, total=False):
    Ipv6CidrBlockAssociation: "VpcIpv6CidrBlockAssociationTypeDef"
    CidrBlockAssociation: "VpcCidrBlockAssociationTypeDef"
    VpcId: str


class AssociatedRoleTypeDef(TypedDict, total=False):
    AssociatedRoleArn: str
    CertificateS3BucketName: str
    CertificateS3ObjectKey: str
    EncryptionKmsKeyId: str


class AssociatedTargetNetworkTypeDef(TypedDict, total=False):
    NetworkId: str
    NetworkType: Literal["vpc"]


class AssociationStatusTypeDef(TypedDict, total=False):
    Code: AssociationStatusCode
    Message: str


class _RequiredAthenaIntegrationTypeDef(TypedDict):
    IntegrationResultS3DestinationArn: str
    PartitionLoadFrequency: PartitionLoadFrequency


class AthenaIntegrationTypeDef(_RequiredAthenaIntegrationTypeDef, total=False):
    PartitionStartDate: datetime
    PartitionEndDate: datetime


class AttachClassicLinkVpcResultTypeDef(TypedDict, total=False):
    Return: bool


class AttachNetworkInterfaceResultTypeDef(TypedDict, total=False):
    AttachmentId: str
    NetworkCardIndex: int


class AttachVpnGatewayResultTypeDef(TypedDict, total=False):
    VpcAttachment: "VpcAttachmentTypeDef"


class AttributeBooleanValueTypeDef(TypedDict, total=False):
    Value: bool


class AttributeValueTypeDef(TypedDict, total=False):
    Value: str


class AuthorizationRuleTypeDef(TypedDict, total=False):
    ClientVpnEndpointId: str
    Description: str
    GroupId: str
    AccessAll: bool
    DestinationCidr: str
    Status: "ClientVpnAuthorizationRuleStatusTypeDef"


class AuthorizeClientVpnIngressResultTypeDef(TypedDict, total=False):
    Status: "ClientVpnAuthorizationRuleStatusTypeDef"


class AvailabilityZoneMessageTypeDef(TypedDict, total=False):
    Message: str


class AvailabilityZoneTypeDef(TypedDict, total=False):
    State: AvailabilityZoneState
    OptInStatus: AvailabilityZoneOptInStatus
    Messages: List["AvailabilityZoneMessageTypeDef"]
    RegionName: str
    ZoneName: str
    ZoneId: str
    GroupName: str
    NetworkBorderGroup: str
    ZoneType: str
    ParentZoneName: str
    ParentZoneId: str


class AvailableCapacityTypeDef(TypedDict, total=False):
    AvailableInstanceCapacity: List["InstanceCapacityTypeDef"]
    AvailableVCpus: int


class BlobAttributeValueTypeDef(TypedDict, total=False):
    Value: Union[bytes, IO[bytes]]


class BlockDeviceMappingTypeDef(TypedDict, total=False):
    DeviceName: str
    VirtualName: str
    Ebs: "EbsBlockDeviceTypeDef"
    NoDevice: str


class BundleInstanceResultTypeDef(TypedDict, total=False):
    BundleTask: "BundleTaskTypeDef"


class BundleTaskErrorTypeDef(TypedDict, total=False):
    Code: str
    Message: str


class BundleTaskTypeDef(TypedDict, total=False):
    BundleId: str
    BundleTaskError: "BundleTaskErrorTypeDef"
    InstanceId: str
    Progress: str
    StartTime: datetime
    State: BundleTaskState
    Storage: "StorageTypeDef"
    UpdateTime: datetime


class ByoipCidrTypeDef(TypedDict, total=False):
    Cidr: str
    Description: str
    StatusMessage: str
    State: ByoipCidrState


class CancelBundleTaskResultTypeDef(TypedDict, total=False):
    BundleTask: "BundleTaskTypeDef"


class CancelCapacityReservationResultTypeDef(TypedDict, total=False):
    Return: bool


class CancelImportTaskResultTypeDef(TypedDict, total=False):
    ImportTaskId: str
    PreviousState: str
    State: str


class CancelReservedInstancesListingResultTypeDef(TypedDict, total=False):
    ReservedInstancesListings: List["ReservedInstancesListingTypeDef"]


class CancelSpotFleetRequestsErrorItemTypeDef(TypedDict, total=False):
    Error: "CancelSpotFleetRequestsErrorTypeDef"
    SpotFleetRequestId: str


class CancelSpotFleetRequestsErrorTypeDef(TypedDict, total=False):
    Code: CancelBatchErrorCode
    Message: str


class CancelSpotFleetRequestsResponseTypeDef(TypedDict, total=False):
    SuccessfulFleetRequests: List["CancelSpotFleetRequestsSuccessItemTypeDef"]
    UnsuccessfulFleetRequests: List["CancelSpotFleetRequestsErrorItemTypeDef"]


class CancelSpotFleetRequestsSuccessItemTypeDef(TypedDict, total=False):
    CurrentSpotFleetRequestState: BatchState
    PreviousSpotFleetRequestState: BatchState
    SpotFleetRequestId: str


class CancelSpotInstanceRequestsResultTypeDef(TypedDict, total=False):
    CancelledSpotInstanceRequests: List["CancelledSpotInstanceRequestTypeDef"]


class CancelledSpotInstanceRequestTypeDef(TypedDict, total=False):
    SpotInstanceRequestId: str
    State: CancelSpotInstanceRequestState


class CapacityReservationGroupTypeDef(TypedDict, total=False):
    GroupArn: str
    OwnerId: str


class CapacityReservationOptionsRequestTypeDef(TypedDict, total=False):
    UsageStrategy: Literal["use-capacity-reservations-first"]


class CapacityReservationOptionsTypeDef(TypedDict, total=False):
    UsageStrategy: Literal["use-capacity-reservations-first"]


class CapacityReservationSpecificationResponseTypeDef(TypedDict, total=False):
    CapacityReservationPreference: CapacityReservationPreference
    CapacityReservationTarget: "CapacityReservationTargetResponseTypeDef"


class CapacityReservationSpecificationTypeDef(TypedDict, total=False):
    CapacityReservationPreference: CapacityReservationPreference
    CapacityReservationTarget: "CapacityReservationTargetTypeDef"


class CapacityReservationTargetResponseTypeDef(TypedDict, total=False):
    CapacityReservationId: str
    CapacityReservationResourceGroupArn: str


class CapacityReservationTargetTypeDef(TypedDict, total=False):
    CapacityReservationId: str
    CapacityReservationResourceGroupArn: str


class CapacityReservationTypeDef(TypedDict, total=False):
    CapacityReservationId: str
    OwnerId: str
    CapacityReservationArn: str
    AvailabilityZoneId: str
    InstanceType: str
    InstancePlatform: CapacityReservationInstancePlatform
    AvailabilityZone: str
    Tenancy: CapacityReservationTenancy
    TotalInstanceCount: int
    AvailableInstanceCount: int
    EbsOptimized: bool
    EphemeralStorage: bool
    State: CapacityReservationState
    StartDate: datetime
    EndDate: datetime
    EndDateType: EndDateType
    InstanceMatchCriteria: InstanceMatchCriteria
    CreateDate: datetime
    Tags: List["TagTypeDef"]


class CarrierGatewayTypeDef(TypedDict, total=False):
    CarrierGatewayId: str
    VpcId: str
    State: CarrierGatewayState
    OwnerId: str
    Tags: List["TagTypeDef"]


class CertificateAuthenticationRequestTypeDef(TypedDict, total=False):
    ClientRootCertificateChainArn: str


class CertificateAuthenticationTypeDef(TypedDict, total=False):
    ClientRootCertificateChain: str


class CidrAuthorizationContextTypeDef(TypedDict):
    Message: str
    Signature: str


class CidrBlockTypeDef(TypedDict, total=False):
    CidrBlock: str


class ClassicLinkDnsSupportTypeDef(TypedDict, total=False):
    ClassicLinkDnsSupported: bool
    VpcId: str


class ClassicLinkInstanceTypeDef(TypedDict, total=False):
    Groups: List["GroupIdentifierTypeDef"]
    InstanceId: str
    Tags: List["TagTypeDef"]
    VpcId: str


class ClassicLoadBalancerTypeDef(TypedDict, total=False):
    Name: str


class ClassicLoadBalancersConfigTypeDef(TypedDict, total=False):
    ClassicLoadBalancers: List["ClassicLoadBalancerTypeDef"]


class ClientCertificateRevocationListStatusTypeDef(TypedDict, total=False):
    Code: ClientCertificateRevocationListStatusCode
    Message: str


class ClientConnectOptionsTypeDef(TypedDict, total=False):
    Enabled: bool
    LambdaFunctionArn: str


class ClientConnectResponseOptionsTypeDef(TypedDict, total=False):
    Enabled: bool
    LambdaFunctionArn: str
    Status: "ClientVpnEndpointAttributeStatusTypeDef"


class ClientDataTypeDef(TypedDict, total=False):
    Comment: str
    UploadEnd: datetime
    UploadSize: float
    UploadStart: datetime


ClientVpnAuthenticationRequestTypeDef = TypedDict(
    "ClientVpnAuthenticationRequestTypeDef",
    {
        "Type": ClientVpnAuthenticationType,
        "ActiveDirectory": "DirectoryServiceAuthenticationRequestTypeDef",
        "MutualAuthentication": "CertificateAuthenticationRequestTypeDef",
        "FederatedAuthentication": "FederatedAuthenticationRequestTypeDef",
    },
    total=False,
)

ClientVpnAuthenticationTypeDef = TypedDict(
    "ClientVpnAuthenticationTypeDef",
    {
        "Type": ClientVpnAuthenticationType,
        "ActiveDirectory": "DirectoryServiceAuthenticationTypeDef",
        "MutualAuthentication": "CertificateAuthenticationTypeDef",
        "FederatedAuthentication": "FederatedAuthenticationTypeDef",
    },
    total=False,
)


class ClientVpnAuthorizationRuleStatusTypeDef(TypedDict, total=False):
    Code: ClientVpnAuthorizationRuleStatusCode
    Message: str


class ClientVpnConnectionStatusTypeDef(TypedDict, total=False):
    Code: ClientVpnConnectionStatusCode
    Message: str


class ClientVpnConnectionTypeDef(TypedDict, total=False):
    ClientVpnEndpointId: str
    Timestamp: str
    ConnectionId: str
    Username: str
    ConnectionEstablishedTime: str
    IngressBytes: str
    EgressBytes: str
    IngressPackets: str
    EgressPackets: str
    ClientIp: str
    CommonName: str
    Status: "ClientVpnConnectionStatusTypeDef"
    ConnectionEndTime: str
    PostureComplianceStatuses: List[str]


class ClientVpnEndpointAttributeStatusTypeDef(TypedDict, total=False):
    Code: ClientVpnEndpointAttributeStatusCode
    Message: str


class ClientVpnEndpointStatusTypeDef(TypedDict, total=False):
    Code: ClientVpnEndpointStatusCode
    Message: str


class ClientVpnEndpointTypeDef(TypedDict, total=False):
    ClientVpnEndpointId: str
    Description: str
    Status: "ClientVpnEndpointStatusTypeDef"
    CreationTime: str
    DeletionTime: str
    DnsName: str
    ClientCidrBlock: str
    DnsServers: List[str]
    SplitTunnel: bool
    VpnProtocol: Literal["openvpn"]
    TransportProtocol: TransportProtocol
    VpnPort: int
    AssociatedTargetNetworks: List["AssociatedTargetNetworkTypeDef"]
    ServerCertificateArn: str
    AuthenticationOptions: List["ClientVpnAuthenticationTypeDef"]
    ConnectionLogOptions: "ConnectionLogResponseOptionsTypeDef"
    Tags: List["TagTypeDef"]
    SecurityGroupIds: List[str]
    VpcId: str
    SelfServicePortalUrl: str
    ClientConnectOptions: "ClientConnectResponseOptionsTypeDef"


class ClientVpnRouteStatusTypeDef(TypedDict, total=False):
    Code: ClientVpnRouteStatusCode
    Message: str


ClientVpnRouteTypeDef = TypedDict(
    "ClientVpnRouteTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DestinationCidr": str,
        "TargetSubnet": str,
        "Type": str,
        "Origin": str,
        "Status": "ClientVpnRouteStatusTypeDef",
        "Description": str,
    },
    total=False,
)


class CoipAddressUsageTypeDef(TypedDict, total=False):
    AllocationId: str
    AwsAccountId: str
    AwsService: str
    CoIp: str


class CoipPoolTypeDef(TypedDict, total=False):
    PoolId: str
    PoolCidrs: List[str]
    LocalGatewayRouteTableId: str
    Tags: List["TagTypeDef"]
    PoolArn: str


class ConfirmProductInstanceResultTypeDef(TypedDict, total=False):
    OwnerId: str
    Return: bool


class ConnectionLogOptionsTypeDef(TypedDict, total=False):
    Enabled: bool
    CloudwatchLogGroup: str
    CloudwatchLogStream: str


class ConnectionLogResponseOptionsTypeDef(TypedDict, total=False):
    Enabled: bool
    CloudwatchLogGroup: str
    CloudwatchLogStream: str


class ConnectionNotificationTypeDef(TypedDict, total=False):
    ConnectionNotificationId: str
    ServiceId: str
    VpcEndpointId: str
    ConnectionNotificationType: Literal["Topic"]
    ConnectionNotificationArn: str
    ConnectionEvents: List[str]
    ConnectionNotificationState: ConnectionNotificationState


class ConversionTaskTypeDef(TypedDict, total=False):
    ConversionTaskId: str
    ExpirationTime: str
    ImportInstance: "ImportInstanceTaskDetailsTypeDef"
    ImportVolume: "ImportVolumeTaskDetailsTypeDef"
    State: ConversionTaskState
    StatusMessage: str
    Tags: List["TagTypeDef"]


class CopyFpgaImageResultTypeDef(TypedDict, total=False):
    FpgaImageId: str


class CopyImageResultTypeDef(TypedDict, total=False):
    ImageId: str


class CopySnapshotResultTypeDef(TypedDict, total=False):
    SnapshotId: str
    Tags: List["TagTypeDef"]


class CpuOptionsRequestTypeDef(TypedDict, total=False):
    CoreCount: int
    ThreadsPerCore: int


class CpuOptionsTypeDef(TypedDict, total=False):
    CoreCount: int
    ThreadsPerCore: int


class CreateCapacityReservationResultTypeDef(TypedDict, total=False):
    CapacityReservation: "CapacityReservationTypeDef"


class CreateCarrierGatewayResultTypeDef(TypedDict, total=False):
    CarrierGateway: "CarrierGatewayTypeDef"


class CreateClientVpnEndpointResultTypeDef(TypedDict, total=False):
    ClientVpnEndpointId: str
    Status: "ClientVpnEndpointStatusTypeDef"
    DnsName: str


class CreateClientVpnRouteResultTypeDef(TypedDict, total=False):
    Status: "ClientVpnRouteStatusTypeDef"


class CreateCustomerGatewayResultTypeDef(TypedDict, total=False):
    CustomerGateway: "CustomerGatewayTypeDef"


class CreateDefaultSubnetResultTypeDef(TypedDict, total=False):
    Subnet: "SubnetTypeDef"


class CreateDefaultVpcResultTypeDef(TypedDict, total=False):
    Vpc: "VpcTypeDef"


class CreateDhcpOptionsResultTypeDef(TypedDict, total=False):
    DhcpOptions: "DhcpOptionsTypeDef"


class CreateEgressOnlyInternetGatewayResultTypeDef(TypedDict, total=False):
    ClientToken: str
    EgressOnlyInternetGateway: "EgressOnlyInternetGatewayTypeDef"


class CreateFleetErrorTypeDef(TypedDict, total=False):
    LaunchTemplateAndOverrides: "LaunchTemplateAndOverridesResponseTypeDef"
    Lifecycle: InstanceLifecycle
    ErrorCode: str
    ErrorMessage: str


class CreateFleetInstanceTypeDef(TypedDict, total=False):
    LaunchTemplateAndOverrides: "LaunchTemplateAndOverridesResponseTypeDef"
    Lifecycle: InstanceLifecycle
    InstanceIds: List[str]
    InstanceType: InstanceType
    Platform: Literal["Windows"]


class CreateFleetResultTypeDef(TypedDict, total=False):
    FleetId: str
    Errors: List["CreateFleetErrorTypeDef"]
    Instances: List["CreateFleetInstanceTypeDef"]


class CreateFlowLogsResultTypeDef(TypedDict, total=False):
    ClientToken: str
    FlowLogIds: List[str]
    Unsuccessful: List["UnsuccessfulItemTypeDef"]


class CreateFpgaImageResultTypeDef(TypedDict, total=False):
    FpgaImageId: str
    FpgaImageGlobalId: str


class CreateImageResultTypeDef(TypedDict, total=False):
    ImageId: str


class CreateInstanceExportTaskResultTypeDef(TypedDict, total=False):
    ExportTask: "ExportTaskTypeDef"


class CreateInternetGatewayResultTypeDef(TypedDict, total=False):
    InternetGateway: "InternetGatewayTypeDef"


CreateLaunchTemplateResultTypeDef = TypedDict(
    "CreateLaunchTemplateResultTypeDef",
    {"LaunchTemplate": "LaunchTemplateTypeDef", "Warning": "ValidationWarningTypeDef"},
    total=False,
)

CreateLaunchTemplateVersionResultTypeDef = TypedDict(
    "CreateLaunchTemplateVersionResultTypeDef",
    {
        "LaunchTemplateVersion": "LaunchTemplateVersionTypeDef",
        "Warning": "ValidationWarningTypeDef",
    },
    total=False,
)


class CreateLocalGatewayRouteResultTypeDef(TypedDict, total=False):
    Route: "LocalGatewayRouteTypeDef"


class CreateLocalGatewayRouteTableVpcAssociationResultTypeDef(TypedDict, total=False):
    LocalGatewayRouteTableVpcAssociation: "LocalGatewayRouteTableVpcAssociationTypeDef"


class CreateManagedPrefixListResultTypeDef(TypedDict, total=False):
    PrefixList: "ManagedPrefixListTypeDef"


class CreateNatGatewayResultTypeDef(TypedDict, total=False):
    ClientToken: str
    NatGateway: "NatGatewayTypeDef"


class CreateNetworkAclResultTypeDef(TypedDict, total=False):
    NetworkAcl: "NetworkAclTypeDef"


class CreateNetworkInsightsPathResultTypeDef(TypedDict, total=False):
    NetworkInsightsPath: "NetworkInsightsPathTypeDef"


class CreateNetworkInterfacePermissionResultTypeDef(TypedDict, total=False):
    InterfacePermission: "NetworkInterfacePermissionTypeDef"


class CreateNetworkInterfaceResultTypeDef(TypedDict, total=False):
    NetworkInterface: "NetworkInterfaceTypeDef"


class CreatePlacementGroupResultTypeDef(TypedDict, total=False):
    PlacementGroup: "PlacementGroupTypeDef"


class CreateReplaceRootVolumeTaskResultTypeDef(TypedDict, total=False):
    ReplaceRootVolumeTask: "ReplaceRootVolumeTaskTypeDef"


class CreateReservedInstancesListingResultTypeDef(TypedDict, total=False):
    ReservedInstancesListings: List["ReservedInstancesListingTypeDef"]


class CreateRestoreImageTaskResultTypeDef(TypedDict, total=False):
    ImageId: str


class CreateRouteResultTypeDef(TypedDict, total=False):
    Return: bool


class CreateRouteTableResultTypeDef(TypedDict, total=False):
    RouteTable: "RouteTableTypeDef"


class CreateSecurityGroupResultTypeDef(TypedDict, total=False):
    GroupId: str
    Tags: List["TagTypeDef"]


class CreateSnapshotsResultTypeDef(TypedDict, total=False):
    Snapshots: List["SnapshotInfoTypeDef"]


class CreateSpotDatafeedSubscriptionResultTypeDef(TypedDict, total=False):
    SpotDatafeedSubscription: "SpotDatafeedSubscriptionTypeDef"


class CreateStoreImageTaskResultTypeDef(TypedDict, total=False):
    ObjectKey: str


class CreateSubnetResultTypeDef(TypedDict, total=False):
    Subnet: "SubnetTypeDef"


class CreateTrafficMirrorFilterResultTypeDef(TypedDict, total=False):
    TrafficMirrorFilter: "TrafficMirrorFilterTypeDef"
    ClientToken: str


class CreateTrafficMirrorFilterRuleResultTypeDef(TypedDict, total=False):
    TrafficMirrorFilterRule: "TrafficMirrorFilterRuleTypeDef"
    ClientToken: str


class CreateTrafficMirrorSessionResultTypeDef(TypedDict, total=False):
    TrafficMirrorSession: "TrafficMirrorSessionTypeDef"
    ClientToken: str


class CreateTrafficMirrorTargetResultTypeDef(TypedDict, total=False):
    TrafficMirrorTarget: "TrafficMirrorTargetTypeDef"
    ClientToken: str


class CreateTransitGatewayConnectPeerResultTypeDef(TypedDict, total=False):
    TransitGatewayConnectPeer: "TransitGatewayConnectPeerTypeDef"


CreateTransitGatewayConnectRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayConnectRequestOptionsTypeDef", {"Protocol": Literal["gre"]}
)


class CreateTransitGatewayConnectResultTypeDef(TypedDict, total=False):
    TransitGatewayConnect: "TransitGatewayConnectTypeDef"


class CreateTransitGatewayMulticastDomainRequestOptionsTypeDef(TypedDict, total=False):
    Igmpv2Support: Igmpv2SupportValue
    StaticSourcesSupport: StaticSourcesSupportValue
    AutoAcceptSharedAssociations: AutoAcceptSharedAssociationsValue


class CreateTransitGatewayMulticastDomainResultTypeDef(TypedDict, total=False):
    TransitGatewayMulticastDomain: "TransitGatewayMulticastDomainTypeDef"


class CreateTransitGatewayPeeringAttachmentResultTypeDef(TypedDict, total=False):
    TransitGatewayPeeringAttachment: "TransitGatewayPeeringAttachmentTypeDef"


class CreateTransitGatewayPrefixListReferenceResultTypeDef(TypedDict, total=False):
    TransitGatewayPrefixListReference: "TransitGatewayPrefixListReferenceTypeDef"


class CreateTransitGatewayResultTypeDef(TypedDict, total=False):
    TransitGateway: "TransitGatewayTypeDef"


class CreateTransitGatewayRouteResultTypeDef(TypedDict, total=False):
    Route: "TransitGatewayRouteTypeDef"


class CreateTransitGatewayRouteTableResultTypeDef(TypedDict, total=False):
    TransitGatewayRouteTable: "TransitGatewayRouteTableTypeDef"


class CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef(TypedDict, total=False):
    DnsSupport: DnsSupportValue
    Ipv6Support: Ipv6SupportValue
    ApplianceModeSupport: ApplianceModeSupportValue


class CreateTransitGatewayVpcAttachmentResultTypeDef(TypedDict, total=False):
    TransitGatewayVpcAttachment: "TransitGatewayVpcAttachmentTypeDef"


class CreateVolumePermissionModificationsTypeDef(TypedDict, total=False):
    Add: List["CreateVolumePermissionTypeDef"]
    Remove: List["CreateVolumePermissionTypeDef"]


class CreateVolumePermissionTypeDef(TypedDict, total=False):
    Group: Literal["all"]
    UserId: str


class CreateVpcEndpointConnectionNotificationResultTypeDef(TypedDict, total=False):
    ConnectionNotification: "ConnectionNotificationTypeDef"
    ClientToken: str


class CreateVpcEndpointResultTypeDef(TypedDict, total=False):
    VpcEndpoint: "VpcEndpointTypeDef"
    ClientToken: str


class CreateVpcEndpointServiceConfigurationResultTypeDef(TypedDict, total=False):
    ServiceConfiguration: "ServiceConfigurationTypeDef"
    ClientToken: str


class CreateVpcPeeringConnectionResultTypeDef(TypedDict, total=False):
    VpcPeeringConnection: "VpcPeeringConnectionTypeDef"


class CreateVpcResultTypeDef(TypedDict, total=False):
    Vpc: "VpcTypeDef"


class CreateVpnConnectionResultTypeDef(TypedDict, total=False):
    VpnConnection: "VpnConnectionTypeDef"


class CreateVpnGatewayResultTypeDef(TypedDict, total=False):
    VpnGateway: "VpnGatewayTypeDef"


class CreditSpecificationRequestTypeDef(TypedDict):
    CpuCredits: str


class CreditSpecificationTypeDef(TypedDict, total=False):
    CpuCredits: str


CustomerGatewayTypeDef = TypedDict(
    "CustomerGatewayTypeDef",
    {
        "BgpAsn": str,
        "CustomerGatewayId": str,
        "IpAddress": str,
        "CertificateArn": str,
        "State": str,
        "Type": str,
        "DeviceName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class DeleteCarrierGatewayResultTypeDef(TypedDict, total=False):
    CarrierGateway: "CarrierGatewayTypeDef"


class DeleteClientVpnEndpointResultTypeDef(TypedDict, total=False):
    Status: "ClientVpnEndpointStatusTypeDef"


class DeleteClientVpnRouteResultTypeDef(TypedDict, total=False):
    Status: "ClientVpnRouteStatusTypeDef"


class DeleteEgressOnlyInternetGatewayResultTypeDef(TypedDict, total=False):
    ReturnCode: bool


class DeleteFleetErrorItemTypeDef(TypedDict, total=False):
    Error: "DeleteFleetErrorTypeDef"
    FleetId: str


class DeleteFleetErrorTypeDef(TypedDict, total=False):
    Code: DeleteFleetErrorCode
    Message: str


class DeleteFleetSuccessItemTypeDef(TypedDict, total=False):
    CurrentFleetState: FleetStateCode
    PreviousFleetState: FleetStateCode
    FleetId: str


class DeleteFleetsResultTypeDef(TypedDict, total=False):
    SuccessfulFleetDeletions: List["DeleteFleetSuccessItemTypeDef"]
    UnsuccessfulFleetDeletions: List["DeleteFleetErrorItemTypeDef"]


class DeleteFlowLogsResultTypeDef(TypedDict, total=False):
    Unsuccessful: List["UnsuccessfulItemTypeDef"]


class DeleteFpgaImageResultTypeDef(TypedDict, total=False):
    Return: bool


class DeleteLaunchTemplateResultTypeDef(TypedDict, total=False):
    LaunchTemplate: "LaunchTemplateTypeDef"


class DeleteLaunchTemplateVersionsResponseErrorItemTypeDef(TypedDict, total=False):
    LaunchTemplateId: str
    LaunchTemplateName: str
    VersionNumber: int
    ResponseError: "ResponseErrorTypeDef"


class DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef(TypedDict, total=False):
    LaunchTemplateId: str
    LaunchTemplateName: str
    VersionNumber: int


class DeleteLaunchTemplateVersionsResultTypeDef(TypedDict, total=False):
    SuccessfullyDeletedLaunchTemplateVersions: List[
        "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef"
    ]
    UnsuccessfullyDeletedLaunchTemplateVersions: List[
        "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef"
    ]


class DeleteLocalGatewayRouteResultTypeDef(TypedDict, total=False):
    Route: "LocalGatewayRouteTypeDef"


class DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef(TypedDict, total=False):
    LocalGatewayRouteTableVpcAssociation: "LocalGatewayRouteTableVpcAssociationTypeDef"


class DeleteManagedPrefixListResultTypeDef(TypedDict, total=False):
    PrefixList: "ManagedPrefixListTypeDef"


class DeleteNatGatewayResultTypeDef(TypedDict, total=False):
    NatGatewayId: str


class DeleteNetworkInsightsAnalysisResultTypeDef(TypedDict, total=False):
    NetworkInsightsAnalysisId: str


class DeleteNetworkInsightsPathResultTypeDef(TypedDict, total=False):
    NetworkInsightsPathId: str


class DeleteNetworkInterfacePermissionResultTypeDef(TypedDict, total=False):
    Return: bool


class DeleteQueuedReservedInstancesErrorTypeDef(TypedDict, total=False):
    Code: DeleteQueuedReservedInstancesErrorCode
    Message: str


class DeleteQueuedReservedInstancesResultTypeDef(TypedDict, total=False):
    SuccessfulQueuedPurchaseDeletions: List["SuccessfulQueuedPurchaseDeletionTypeDef"]
    FailedQueuedPurchaseDeletions: List["FailedQueuedPurchaseDeletionTypeDef"]


class DeleteTrafficMirrorFilterResultTypeDef(TypedDict, total=False):
    TrafficMirrorFilterId: str


class DeleteTrafficMirrorFilterRuleResultTypeDef(TypedDict, total=False):
    TrafficMirrorFilterRuleId: str


class DeleteTrafficMirrorSessionResultTypeDef(TypedDict, total=False):
    TrafficMirrorSessionId: str


class DeleteTrafficMirrorTargetResultTypeDef(TypedDict, total=False):
    TrafficMirrorTargetId: str


class DeleteTransitGatewayConnectPeerResultTypeDef(TypedDict, total=False):
    TransitGatewayConnectPeer: "TransitGatewayConnectPeerTypeDef"


class DeleteTransitGatewayConnectResultTypeDef(TypedDict, total=False):
    TransitGatewayConnect: "TransitGatewayConnectTypeDef"


class DeleteTransitGatewayMulticastDomainResultTypeDef(TypedDict, total=False):
    TransitGatewayMulticastDomain: "TransitGatewayMulticastDomainTypeDef"


class DeleteTransitGatewayPeeringAttachmentResultTypeDef(TypedDict, total=False):
    TransitGatewayPeeringAttachment: "TransitGatewayPeeringAttachmentTypeDef"


class DeleteTransitGatewayPrefixListReferenceResultTypeDef(TypedDict, total=False):
    TransitGatewayPrefixListReference: "TransitGatewayPrefixListReferenceTypeDef"


class DeleteTransitGatewayResultTypeDef(TypedDict, total=False):
    TransitGateway: "TransitGatewayTypeDef"


class DeleteTransitGatewayRouteResultTypeDef(TypedDict, total=False):
    Route: "TransitGatewayRouteTypeDef"


class DeleteTransitGatewayRouteTableResultTypeDef(TypedDict, total=False):
    TransitGatewayRouteTable: "TransitGatewayRouteTableTypeDef"


class DeleteTransitGatewayVpcAttachmentResultTypeDef(TypedDict, total=False):
    TransitGatewayVpcAttachment: "TransitGatewayVpcAttachmentTypeDef"


class DeleteVpcEndpointConnectionNotificationsResultTypeDef(TypedDict, total=False):
    Unsuccessful: List["UnsuccessfulItemTypeDef"]


class DeleteVpcEndpointServiceConfigurationsResultTypeDef(TypedDict, total=False):
    Unsuccessful: List["UnsuccessfulItemTypeDef"]


class DeleteVpcEndpointsResultTypeDef(TypedDict, total=False):
    Unsuccessful: List["UnsuccessfulItemTypeDef"]


class DeleteVpcPeeringConnectionResultTypeDef(TypedDict, total=False):
    Return: bool


class DeprovisionByoipCidrResultTypeDef(TypedDict, total=False):
    ByoipCidr: "ByoipCidrTypeDef"


class DeregisterInstanceEventNotificationAttributesResultTypeDef(TypedDict, total=False):
    InstanceTagAttribute: "InstanceTagNotificationAttributeTypeDef"


class DeregisterInstanceTagAttributeRequestTypeDef(TypedDict, total=False):
    IncludeAllTagsOfInstance: bool
    InstanceTagKeys: List[str]


class DeregisterTransitGatewayMulticastGroupMembersResultTypeDef(TypedDict, total=False):
    DeregisteredMulticastGroupMembers: "TransitGatewayMulticastDeregisteredGroupMembersTypeDef"


class DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef(TypedDict, total=False):
    DeregisteredMulticastGroupSources: "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef"


class DescribeAccountAttributesResultTypeDef(TypedDict, total=False):
    AccountAttributes: List["AccountAttributeTypeDef"]


class DescribeAddressesAttributeResultTypeDef(TypedDict, total=False):
    Addresses: List["AddressAttributeTypeDef"]
    NextToken: str


class DescribeAddressesResultTypeDef(TypedDict, total=False):
    Addresses: List["AddressTypeDef"]


class DescribeAggregateIdFormatResultTypeDef(TypedDict, total=False):
    UseLongIdsAggregated: bool
    Statuses: List["IdFormatTypeDef"]


class DescribeAvailabilityZonesResultTypeDef(TypedDict, total=False):
    AvailabilityZones: List["AvailabilityZoneTypeDef"]


class DescribeBundleTasksResultTypeDef(TypedDict, total=False):
    BundleTasks: List["BundleTaskTypeDef"]


class DescribeByoipCidrsResultTypeDef(TypedDict, total=False):
    ByoipCidrs: List["ByoipCidrTypeDef"]
    NextToken: str


class DescribeCapacityReservationsResultTypeDef(TypedDict, total=False):
    NextToken: str
    CapacityReservations: List["CapacityReservationTypeDef"]


class DescribeCarrierGatewaysResultTypeDef(TypedDict, total=False):
    CarrierGateways: List["CarrierGatewayTypeDef"]
    NextToken: str


class DescribeClassicLinkInstancesResultTypeDef(TypedDict, total=False):
    Instances: List["ClassicLinkInstanceTypeDef"]
    NextToken: str


class DescribeClientVpnAuthorizationRulesResultTypeDef(TypedDict, total=False):
    AuthorizationRules: List["AuthorizationRuleTypeDef"]
    NextToken: str


class DescribeClientVpnConnectionsResultTypeDef(TypedDict, total=False):
    Connections: List["ClientVpnConnectionTypeDef"]
    NextToken: str


class DescribeClientVpnEndpointsResultTypeDef(TypedDict, total=False):
    ClientVpnEndpoints: List["ClientVpnEndpointTypeDef"]
    NextToken: str


class DescribeClientVpnRoutesResultTypeDef(TypedDict, total=False):
    Routes: List["ClientVpnRouteTypeDef"]
    NextToken: str


class DescribeClientVpnTargetNetworksResultTypeDef(TypedDict, total=False):
    ClientVpnTargetNetworks: List["TargetNetworkTypeDef"]
    NextToken: str


class DescribeCoipPoolsResultTypeDef(TypedDict, total=False):
    CoipPools: List["CoipPoolTypeDef"]
    NextToken: str


class DescribeConversionTasksResultTypeDef(TypedDict, total=False):
    ConversionTasks: List["ConversionTaskTypeDef"]


class DescribeCustomerGatewaysResultTypeDef(TypedDict, total=False):
    CustomerGateways: List["CustomerGatewayTypeDef"]


class DescribeDhcpOptionsResultTypeDef(TypedDict, total=False):
    DhcpOptions: List["DhcpOptionsTypeDef"]
    NextToken: str


class DescribeEgressOnlyInternetGatewaysResultTypeDef(TypedDict, total=False):
    EgressOnlyInternetGateways: List["EgressOnlyInternetGatewayTypeDef"]
    NextToken: str


class DescribeElasticGpusResultTypeDef(TypedDict, total=False):
    ElasticGpuSet: List["ElasticGpusTypeDef"]
    MaxResults: int
    NextToken: str


class DescribeExportImageTasksResultTypeDef(TypedDict, total=False):
    ExportImageTasks: List["ExportImageTaskTypeDef"]
    NextToken: str


class DescribeExportTasksResultTypeDef(TypedDict, total=False):
    ExportTasks: List["ExportTaskTypeDef"]


class DescribeFastSnapshotRestoreSuccessItemTypeDef(TypedDict, total=False):
    SnapshotId: str
    AvailabilityZone: str
    State: FastSnapshotRestoreStateCode
    StateTransitionReason: str
    OwnerId: str
    OwnerAlias: str
    EnablingTime: datetime
    OptimizingTime: datetime
    EnabledTime: datetime
    DisablingTime: datetime
    DisabledTime: datetime


class DescribeFastSnapshotRestoresResultTypeDef(TypedDict, total=False):
    FastSnapshotRestores: List["DescribeFastSnapshotRestoreSuccessItemTypeDef"]
    NextToken: str


class DescribeFleetErrorTypeDef(TypedDict, total=False):
    LaunchTemplateAndOverrides: "LaunchTemplateAndOverridesResponseTypeDef"
    Lifecycle: InstanceLifecycle
    ErrorCode: str
    ErrorMessage: str


class DescribeFleetHistoryResultTypeDef(TypedDict, total=False):
    HistoryRecords: List["HistoryRecordEntryTypeDef"]
    LastEvaluatedTime: datetime
    NextToken: str
    FleetId: str
    StartTime: datetime


class DescribeFleetInstancesResultTypeDef(TypedDict, total=False):
    ActiveInstances: List["ActiveInstanceTypeDef"]
    NextToken: str
    FleetId: str


class DescribeFleetsInstancesTypeDef(TypedDict, total=False):
    LaunchTemplateAndOverrides: "LaunchTemplateAndOverridesResponseTypeDef"
    Lifecycle: InstanceLifecycle
    InstanceIds: List[str]
    InstanceType: InstanceType
    Platform: Literal["Windows"]


class DescribeFleetsResultTypeDef(TypedDict, total=False):
    NextToken: str
    Fleets: List["FleetDataTypeDef"]


class DescribeFlowLogsResultTypeDef(TypedDict, total=False):
    FlowLogs: List["FlowLogTypeDef"]
    NextToken: str


class DescribeFpgaImageAttributeResultTypeDef(TypedDict, total=False):
    FpgaImageAttribute: "FpgaImageAttributeTypeDef"


class DescribeFpgaImagesResultTypeDef(TypedDict, total=False):
    FpgaImages: List["FpgaImageTypeDef"]
    NextToken: str


class DescribeHostReservationOfferingsResultTypeDef(TypedDict, total=False):
    NextToken: str
    OfferingSet: List["HostOfferingTypeDef"]


class DescribeHostReservationsResultTypeDef(TypedDict, total=False):
    HostReservationSet: List["HostReservationTypeDef"]
    NextToken: str


class DescribeHostsResultTypeDef(TypedDict, total=False):
    Hosts: List["HostTypeDef"]
    NextToken: str


class DescribeIamInstanceProfileAssociationsResultTypeDef(TypedDict, total=False):
    IamInstanceProfileAssociations: List["IamInstanceProfileAssociationTypeDef"]
    NextToken: str


class DescribeIdFormatResultTypeDef(TypedDict, total=False):
    Statuses: List["IdFormatTypeDef"]


class DescribeIdentityIdFormatResultTypeDef(TypedDict, total=False):
    Statuses: List["IdFormatTypeDef"]


class DescribeImagesResultTypeDef(TypedDict, total=False):
    Images: List["ImageTypeDef"]


class DescribeImportImageTasksResultTypeDef(TypedDict, total=False):
    ImportImageTasks: List["ImportImageTaskTypeDef"]
    NextToken: str


class DescribeImportSnapshotTasksResultTypeDef(TypedDict, total=False):
    ImportSnapshotTasks: List["ImportSnapshotTaskTypeDef"]
    NextToken: str


class DescribeInstanceCreditSpecificationsResultTypeDef(TypedDict, total=False):
    InstanceCreditSpecifications: List["InstanceCreditSpecificationTypeDef"]
    NextToken: str


class DescribeInstanceEventNotificationAttributesResultTypeDef(TypedDict, total=False):
    InstanceTagAttribute: "InstanceTagNotificationAttributeTypeDef"


class DescribeInstanceStatusResultTypeDef(TypedDict, total=False):
    InstanceStatuses: List["InstanceStatusTypeDef"]
    NextToken: str


class DescribeInstanceTypeOfferingsResultTypeDef(TypedDict, total=False):
    InstanceTypeOfferings: List["InstanceTypeOfferingTypeDef"]
    NextToken: str


class DescribeInstanceTypesResultTypeDef(TypedDict, total=False):
    InstanceTypes: List["InstanceTypeInfoTypeDef"]
    NextToken: str


class DescribeInstancesResultTypeDef(TypedDict, total=False):
    Reservations: List["ReservationTypeDef"]
    NextToken: str


class DescribeInternetGatewaysResultTypeDef(TypedDict, total=False):
    InternetGateways: List["InternetGatewayTypeDef"]
    NextToken: str


class DescribeIpv6PoolsResultTypeDef(TypedDict, total=False):
    Ipv6Pools: List["Ipv6PoolTypeDef"]
    NextToken: str


class DescribeKeyPairsResultTypeDef(TypedDict, total=False):
    KeyPairs: List["KeyPairInfoTypeDef"]


class DescribeLaunchTemplateVersionsResultTypeDef(TypedDict, total=False):
    LaunchTemplateVersions: List["LaunchTemplateVersionTypeDef"]
    NextToken: str


class DescribeLaunchTemplatesResultTypeDef(TypedDict, total=False):
    LaunchTemplates: List["LaunchTemplateTypeDef"]
    NextToken: str


class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef(
    TypedDict, total=False
):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociations: List[
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef"
    ]
    NextToken: str


class DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef(TypedDict, total=False):
    LocalGatewayRouteTableVpcAssociations: List["LocalGatewayRouteTableVpcAssociationTypeDef"]
    NextToken: str


class DescribeLocalGatewayRouteTablesResultTypeDef(TypedDict, total=False):
    LocalGatewayRouteTables: List["LocalGatewayRouteTableTypeDef"]
    NextToken: str


class DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef(TypedDict, total=False):
    LocalGatewayVirtualInterfaceGroups: List["LocalGatewayVirtualInterfaceGroupTypeDef"]
    NextToken: str


class DescribeLocalGatewayVirtualInterfacesResultTypeDef(TypedDict, total=False):
    LocalGatewayVirtualInterfaces: List["LocalGatewayVirtualInterfaceTypeDef"]
    NextToken: str


class DescribeLocalGatewaysResultTypeDef(TypedDict, total=False):
    LocalGateways: List["LocalGatewayTypeDef"]
    NextToken: str


class DescribeManagedPrefixListsResultTypeDef(TypedDict, total=False):
    NextToken: str
    PrefixLists: List["ManagedPrefixListTypeDef"]


class DescribeMovingAddressesResultTypeDef(TypedDict, total=False):
    MovingAddressStatuses: List["MovingAddressStatusTypeDef"]
    NextToken: str


class DescribeNatGatewaysResultTypeDef(TypedDict, total=False):
    NatGateways: List["NatGatewayTypeDef"]
    NextToken: str


class DescribeNetworkAclsResultTypeDef(TypedDict, total=False):
    NetworkAcls: List["NetworkAclTypeDef"]
    NextToken: str


class DescribeNetworkInsightsAnalysesResultTypeDef(TypedDict, total=False):
    NetworkInsightsAnalyses: List["NetworkInsightsAnalysisTypeDef"]
    NextToken: str


class DescribeNetworkInsightsPathsResultTypeDef(TypedDict, total=False):
    NetworkInsightsPaths: List["NetworkInsightsPathTypeDef"]
    NextToken: str


class DescribeNetworkInterfaceAttributeResultTypeDef(TypedDict, total=False):
    Attachment: "NetworkInterfaceAttachmentTypeDef"
    Description: "AttributeValueTypeDef"
    Groups: List["GroupIdentifierTypeDef"]
    NetworkInterfaceId: str
    SourceDestCheck: "AttributeBooleanValueTypeDef"


class DescribeNetworkInterfacePermissionsResultTypeDef(TypedDict, total=False):
    NetworkInterfacePermissions: List["NetworkInterfacePermissionTypeDef"]
    NextToken: str


class DescribeNetworkInterfacesResultTypeDef(TypedDict, total=False):
    NetworkInterfaces: List["NetworkInterfaceTypeDef"]
    NextToken: str


class DescribePlacementGroupsResultTypeDef(TypedDict, total=False):
    PlacementGroups: List["PlacementGroupTypeDef"]


class DescribePrefixListsResultTypeDef(TypedDict, total=False):
    NextToken: str
    PrefixLists: List["PrefixListTypeDef"]


class DescribePrincipalIdFormatResultTypeDef(TypedDict, total=False):
    Principals: List["PrincipalIdFormatTypeDef"]
    NextToken: str


class DescribePublicIpv4PoolsResultTypeDef(TypedDict, total=False):
    PublicIpv4Pools: List["PublicIpv4PoolTypeDef"]
    NextToken: str


class DescribeRegionsResultTypeDef(TypedDict, total=False):
    Regions: List["RegionTypeDef"]


class DescribeReplaceRootVolumeTasksResultTypeDef(TypedDict, total=False):
    ReplaceRootVolumeTasks: List["ReplaceRootVolumeTaskTypeDef"]
    NextToken: str


class DescribeReservedInstancesListingsResultTypeDef(TypedDict, total=False):
    ReservedInstancesListings: List["ReservedInstancesListingTypeDef"]


class DescribeReservedInstancesModificationsResultTypeDef(TypedDict, total=False):
    NextToken: str
    ReservedInstancesModifications: List["ReservedInstancesModificationTypeDef"]


class DescribeReservedInstancesOfferingsResultTypeDef(TypedDict, total=False):
    ReservedInstancesOfferings: List["ReservedInstancesOfferingTypeDef"]
    NextToken: str


class DescribeReservedInstancesResultTypeDef(TypedDict, total=False):
    ReservedInstances: List["ReservedInstancesTypeDef"]


class DescribeRouteTablesResultTypeDef(TypedDict, total=False):
    RouteTables: List["RouteTableTypeDef"]
    NextToken: str


class DescribeScheduledInstanceAvailabilityResultTypeDef(TypedDict, total=False):
    NextToken: str
    ScheduledInstanceAvailabilitySet: List["ScheduledInstanceAvailabilityTypeDef"]


class DescribeScheduledInstancesResultTypeDef(TypedDict, total=False):
    NextToken: str
    ScheduledInstanceSet: List["ScheduledInstanceTypeDef"]


class DescribeSecurityGroupReferencesResultTypeDef(TypedDict, total=False):
    SecurityGroupReferenceSet: List["SecurityGroupReferenceTypeDef"]


class DescribeSecurityGroupsResultTypeDef(TypedDict, total=False):
    SecurityGroups: List["SecurityGroupTypeDef"]
    NextToken: str


class DescribeSnapshotAttributeResultTypeDef(TypedDict, total=False):
    CreateVolumePermissions: List["CreateVolumePermissionTypeDef"]
    ProductCodes: List["ProductCodeTypeDef"]
    SnapshotId: str


class DescribeSnapshotsResultTypeDef(TypedDict, total=False):
    Snapshots: List["SnapshotTypeDef"]
    NextToken: str


class DescribeSpotDatafeedSubscriptionResultTypeDef(TypedDict, total=False):
    SpotDatafeedSubscription: "SpotDatafeedSubscriptionTypeDef"


class DescribeSpotFleetInstancesResponseTypeDef(TypedDict, total=False):
    ActiveInstances: List["ActiveInstanceTypeDef"]
    NextToken: str
    SpotFleetRequestId: str


class DescribeSpotFleetRequestHistoryResponseTypeDef(TypedDict, total=False):
    HistoryRecords: List["HistoryRecordTypeDef"]
    LastEvaluatedTime: datetime
    NextToken: str
    SpotFleetRequestId: str
    StartTime: datetime


class DescribeSpotFleetRequestsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    SpotFleetRequestConfigs: List["SpotFleetRequestConfigTypeDef"]


class DescribeSpotInstanceRequestsResultTypeDef(TypedDict, total=False):
    SpotInstanceRequests: List["SpotInstanceRequestTypeDef"]
    NextToken: str


class DescribeSpotPriceHistoryResultTypeDef(TypedDict, total=False):
    NextToken: str
    SpotPriceHistory: List["SpotPriceTypeDef"]


class DescribeStaleSecurityGroupsResultTypeDef(TypedDict, total=False):
    NextToken: str
    StaleSecurityGroupSet: List["StaleSecurityGroupTypeDef"]


class DescribeStoreImageTasksResultTypeDef(TypedDict, total=False):
    StoreImageTaskResults: List["StoreImageTaskResultTypeDef"]
    NextToken: str


class DescribeSubnetsResultTypeDef(TypedDict, total=False):
    Subnets: List["SubnetTypeDef"]
    NextToken: str


class DescribeTagsResultTypeDef(TypedDict, total=False):
    NextToken: str
    Tags: List["TagDescriptionTypeDef"]


class DescribeTrafficMirrorFiltersResultTypeDef(TypedDict, total=False):
    TrafficMirrorFilters: List["TrafficMirrorFilterTypeDef"]
    NextToken: str


class DescribeTrafficMirrorSessionsResultTypeDef(TypedDict, total=False):
    TrafficMirrorSessions: List["TrafficMirrorSessionTypeDef"]
    NextToken: str


class DescribeTrafficMirrorTargetsResultTypeDef(TypedDict, total=False):
    TrafficMirrorTargets: List["TrafficMirrorTargetTypeDef"]
    NextToken: str


class DescribeTransitGatewayAttachmentsResultTypeDef(TypedDict, total=False):
    TransitGatewayAttachments: List["TransitGatewayAttachmentTypeDef"]
    NextToken: str


class DescribeTransitGatewayConnectPeersResultTypeDef(TypedDict, total=False):
    TransitGatewayConnectPeers: List["TransitGatewayConnectPeerTypeDef"]
    NextToken: str


class DescribeTransitGatewayConnectsResultTypeDef(TypedDict, total=False):
    TransitGatewayConnects: List["TransitGatewayConnectTypeDef"]
    NextToken: str


class DescribeTransitGatewayMulticastDomainsResultTypeDef(TypedDict, total=False):
    TransitGatewayMulticastDomains: List["TransitGatewayMulticastDomainTypeDef"]
    NextToken: str


class DescribeTransitGatewayPeeringAttachmentsResultTypeDef(TypedDict, total=False):
    TransitGatewayPeeringAttachments: List["TransitGatewayPeeringAttachmentTypeDef"]
    NextToken: str


class DescribeTransitGatewayRouteTablesResultTypeDef(TypedDict, total=False):
    TransitGatewayRouteTables: List["TransitGatewayRouteTableTypeDef"]
    NextToken: str


class DescribeTransitGatewayVpcAttachmentsResultTypeDef(TypedDict, total=False):
    TransitGatewayVpcAttachments: List["TransitGatewayVpcAttachmentTypeDef"]
    NextToken: str


class DescribeTransitGatewaysResultTypeDef(TypedDict, total=False):
    TransitGateways: List["TransitGatewayTypeDef"]
    NextToken: str


class DescribeVolumeAttributeResultTypeDef(TypedDict, total=False):
    AutoEnableIO: "AttributeBooleanValueTypeDef"
    ProductCodes: List["ProductCodeTypeDef"]
    VolumeId: str


class DescribeVolumeStatusResultTypeDef(TypedDict, total=False):
    NextToken: str
    VolumeStatuses: List["VolumeStatusItemTypeDef"]


class DescribeVolumesModificationsResultTypeDef(TypedDict, total=False):
    VolumesModifications: List["VolumeModificationTypeDef"]
    NextToken: str


class DescribeVolumesResultTypeDef(TypedDict, total=False):
    Volumes: List["VolumeTypeDef"]
    NextToken: str


class DescribeVpcAttributeResultTypeDef(TypedDict, total=False):
    VpcId: str
    EnableDnsHostnames: "AttributeBooleanValueTypeDef"
    EnableDnsSupport: "AttributeBooleanValueTypeDef"


class DescribeVpcClassicLinkDnsSupportResultTypeDef(TypedDict, total=False):
    NextToken: str
    Vpcs: List["ClassicLinkDnsSupportTypeDef"]


class DescribeVpcClassicLinkResultTypeDef(TypedDict, total=False):
    Vpcs: List["VpcClassicLinkTypeDef"]


class DescribeVpcEndpointConnectionNotificationsResultTypeDef(TypedDict, total=False):
    ConnectionNotificationSet: List["ConnectionNotificationTypeDef"]
    NextToken: str


class DescribeVpcEndpointConnectionsResultTypeDef(TypedDict, total=False):
    VpcEndpointConnections: List["VpcEndpointConnectionTypeDef"]
    NextToken: str


class DescribeVpcEndpointServiceConfigurationsResultTypeDef(TypedDict, total=False):
    ServiceConfigurations: List["ServiceConfigurationTypeDef"]
    NextToken: str


class DescribeVpcEndpointServicePermissionsResultTypeDef(TypedDict, total=False):
    AllowedPrincipals: List["AllowedPrincipalTypeDef"]
    NextToken: str


class DescribeVpcEndpointServicesResultTypeDef(TypedDict, total=False):
    ServiceNames: List[str]
    ServiceDetails: List["ServiceDetailTypeDef"]
    NextToken: str


class DescribeVpcEndpointsResultTypeDef(TypedDict, total=False):
    VpcEndpoints: List["VpcEndpointTypeDef"]
    NextToken: str


class DescribeVpcPeeringConnectionsResultTypeDef(TypedDict, total=False):
    VpcPeeringConnections: List["VpcPeeringConnectionTypeDef"]
    NextToken: str


class DescribeVpcsResultTypeDef(TypedDict, total=False):
    Vpcs: List["VpcTypeDef"]
    NextToken: str


class DescribeVpnConnectionsResultTypeDef(TypedDict, total=False):
    VpnConnections: List["VpnConnectionTypeDef"]


class DescribeVpnGatewaysResultTypeDef(TypedDict, total=False):
    VpnGateways: List["VpnGatewayTypeDef"]


class DetachClassicLinkVpcResultTypeDef(TypedDict, total=False):
    Return: bool


class DhcpConfigurationTypeDef(TypedDict, total=False):
    Key: str
    Values: List["AttributeValueTypeDef"]


class DhcpOptionsTypeDef(TypedDict, total=False):
    DhcpConfigurations: List["DhcpConfigurationTypeDef"]
    DhcpOptionsId: str
    OwnerId: str
    Tags: List["TagTypeDef"]


class DirectoryServiceAuthenticationRequestTypeDef(TypedDict, total=False):
    DirectoryId: str


class DirectoryServiceAuthenticationTypeDef(TypedDict, total=False):
    DirectoryId: str


class DisableEbsEncryptionByDefaultResultTypeDef(TypedDict, total=False):
    EbsEncryptionByDefault: bool


class DisableFastSnapshotRestoreErrorItemTypeDef(TypedDict, total=False):
    SnapshotId: str
    FastSnapshotRestoreStateErrors: List["DisableFastSnapshotRestoreStateErrorItemTypeDef"]


class DisableFastSnapshotRestoreStateErrorItemTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    Error: "DisableFastSnapshotRestoreStateErrorTypeDef"


class DisableFastSnapshotRestoreStateErrorTypeDef(TypedDict, total=False):
    Code: str
    Message: str


class DisableFastSnapshotRestoreSuccessItemTypeDef(TypedDict, total=False):
    SnapshotId: str
    AvailabilityZone: str
    State: FastSnapshotRestoreStateCode
    StateTransitionReason: str
    OwnerId: str
    OwnerAlias: str
    EnablingTime: datetime
    OptimizingTime: datetime
    EnabledTime: datetime
    DisablingTime: datetime
    DisabledTime: datetime


class DisableFastSnapshotRestoresResultTypeDef(TypedDict, total=False):
    Successful: List["DisableFastSnapshotRestoreSuccessItemTypeDef"]
    Unsuccessful: List["DisableFastSnapshotRestoreErrorItemTypeDef"]


class DisableSerialConsoleAccessResultTypeDef(TypedDict, total=False):
    SerialConsoleAccessEnabled: bool


class DisableTransitGatewayRouteTablePropagationResultTypeDef(TypedDict, total=False):
    Propagation: "TransitGatewayPropagationTypeDef"


class DisableVpcClassicLinkDnsSupportResultTypeDef(TypedDict, total=False):
    Return: bool


class DisableVpcClassicLinkResultTypeDef(TypedDict, total=False):
    Return: bool


class DisassociateClientVpnTargetNetworkResultTypeDef(TypedDict, total=False):
    AssociationId: str
    Status: "AssociationStatusTypeDef"


class DisassociateEnclaveCertificateIamRoleResultTypeDef(TypedDict, total=False):
    Return: bool


class DisassociateIamInstanceProfileResultTypeDef(TypedDict, total=False):
    IamInstanceProfileAssociation: "IamInstanceProfileAssociationTypeDef"


class DisassociateSubnetCidrBlockResultTypeDef(TypedDict, total=False):
    Ipv6CidrBlockAssociation: "SubnetIpv6CidrBlockAssociationTypeDef"
    SubnetId: str


class DisassociateTransitGatewayMulticastDomainResultTypeDef(TypedDict, total=False):
    Associations: "TransitGatewayMulticastDomainAssociationsTypeDef"


class DisassociateTransitGatewayRouteTableResultTypeDef(TypedDict, total=False):
    Association: "TransitGatewayAssociationTypeDef"


class DisassociateVpcCidrBlockResultTypeDef(TypedDict, total=False):
    Ipv6CidrBlockAssociation: "VpcIpv6CidrBlockAssociationTypeDef"
    CidrBlockAssociation: "VpcCidrBlockAssociationTypeDef"
    VpcId: str


class DiskImageDescriptionTypeDef(TypedDict, total=False):
    Checksum: str
    Format: DiskImageFormat
    ImportManifestUrl: str
    Size: int


class DiskImageDetailTypeDef(TypedDict):
    Bytes: int
    Format: DiskImageFormat
    ImportManifestUrl: str


class DiskImageTypeDef(TypedDict, total=False):
    Description: str
    Image: "DiskImageDetailTypeDef"
    Volume: "VolumeDetailTypeDef"


class DiskImageVolumeDescriptionTypeDef(TypedDict, total=False):
    Id: str
    Size: int


DiskInfoTypeDef = TypedDict(
    "DiskInfoTypeDef", {"SizeInGB": int, "Count": int, "Type": DiskType}, total=False
)


class DnsEntryTypeDef(TypedDict, total=False):
    DnsName: str
    HostedZoneId: str


class DnsServersOptionsModifyStructureTypeDef(TypedDict, total=False):
    CustomDnsServers: List[str]
    Enabled: bool


class EbsBlockDeviceTypeDef(TypedDict, total=False):
    DeleteOnTermination: bool
    Iops: int
    SnapshotId: str
    VolumeSize: int
    VolumeType: VolumeType
    KmsKeyId: str
    Throughput: int
    OutpostArn: str
    Encrypted: bool


class EbsInfoTypeDef(TypedDict, total=False):
    EbsOptimizedSupport: EbsOptimizedSupport
    EncryptionSupport: EbsEncryptionSupport
    EbsOptimizedInfo: "EbsOptimizedInfoTypeDef"
    NvmeSupport: EbsNvmeSupport


class EbsInstanceBlockDeviceSpecificationTypeDef(TypedDict, total=False):
    DeleteOnTermination: bool
    VolumeId: str


class EbsInstanceBlockDeviceTypeDef(TypedDict, total=False):
    AttachTime: datetime
    DeleteOnTermination: bool
    Status: AttachmentStatus
    VolumeId: str


class EbsOptimizedInfoTypeDef(TypedDict, total=False):
    BaselineBandwidthInMbps: int
    BaselineThroughputInMBps: float
    BaselineIops: int
    MaximumBandwidthInMbps: int
    MaximumThroughputInMBps: float
    MaximumIops: int


class EfaInfoTypeDef(TypedDict, total=False):
    MaximumEfaInterfaces: int


class EgressOnlyInternetGatewayTypeDef(TypedDict, total=False):
    Attachments: List["InternetGatewayAttachmentTypeDef"]
    EgressOnlyInternetGatewayId: str
    Tags: List["TagTypeDef"]


class ElasticGpuAssociationTypeDef(TypedDict, total=False):
    ElasticGpuId: str
    ElasticGpuAssociationId: str
    ElasticGpuAssociationState: str
    ElasticGpuAssociationTime: str


class ElasticGpuHealthTypeDef(TypedDict, total=False):
    Status: ElasticGpuStatus


ElasticGpuSpecificationResponseTypeDef = TypedDict(
    "ElasticGpuSpecificationResponseTypeDef", {"Type": str}, total=False
)

ElasticGpuSpecificationTypeDef = TypedDict("ElasticGpuSpecificationTypeDef", {"Type": str})


class ElasticGpusTypeDef(TypedDict, total=False):
    ElasticGpuId: str
    AvailabilityZone: str
    ElasticGpuType: str
    ElasticGpuHealth: "ElasticGpuHealthTypeDef"
    ElasticGpuState: Literal["ATTACHED"]
    InstanceId: str
    Tags: List["TagTypeDef"]


class ElasticInferenceAcceleratorAssociationTypeDef(TypedDict, total=False):
    ElasticInferenceAcceleratorArn: str
    ElasticInferenceAcceleratorAssociationId: str
    ElasticInferenceAcceleratorAssociationState: str
    ElasticInferenceAcceleratorAssociationTime: datetime


_RequiredElasticInferenceAcceleratorTypeDef = TypedDict(
    "_RequiredElasticInferenceAcceleratorTypeDef", {"Type": str}
)
_OptionalElasticInferenceAcceleratorTypeDef = TypedDict(
    "_OptionalElasticInferenceAcceleratorTypeDef", {"Count": int}, total=False
)


class ElasticInferenceAcceleratorTypeDef(
    _RequiredElasticInferenceAcceleratorTypeDef, _OptionalElasticInferenceAcceleratorTypeDef
):
    pass


class EnableEbsEncryptionByDefaultResultTypeDef(TypedDict, total=False):
    EbsEncryptionByDefault: bool


class EnableFastSnapshotRestoreErrorItemTypeDef(TypedDict, total=False):
    SnapshotId: str
    FastSnapshotRestoreStateErrors: List["EnableFastSnapshotRestoreStateErrorItemTypeDef"]


class EnableFastSnapshotRestoreStateErrorItemTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    Error: "EnableFastSnapshotRestoreStateErrorTypeDef"


class EnableFastSnapshotRestoreStateErrorTypeDef(TypedDict, total=False):
    Code: str
    Message: str


class EnableFastSnapshotRestoreSuccessItemTypeDef(TypedDict, total=False):
    SnapshotId: str
    AvailabilityZone: str
    State: FastSnapshotRestoreStateCode
    StateTransitionReason: str
    OwnerId: str
    OwnerAlias: str
    EnablingTime: datetime
    OptimizingTime: datetime
    EnabledTime: datetime
    DisablingTime: datetime
    DisabledTime: datetime


class EnableFastSnapshotRestoresResultTypeDef(TypedDict, total=False):
    Successful: List["EnableFastSnapshotRestoreSuccessItemTypeDef"]
    Unsuccessful: List["EnableFastSnapshotRestoreErrorItemTypeDef"]


class EnableSerialConsoleAccessResultTypeDef(TypedDict, total=False):
    SerialConsoleAccessEnabled: bool


class EnableTransitGatewayRouteTablePropagationResultTypeDef(TypedDict, total=False):
    Propagation: "TransitGatewayPropagationTypeDef"


class EnableVpcClassicLinkDnsSupportResultTypeDef(TypedDict, total=False):
    Return: bool


class EnableVpcClassicLinkResultTypeDef(TypedDict, total=False):
    Return: bool


class EnclaveOptionsRequestTypeDef(TypedDict, total=False):
    Enabled: bool


class EnclaveOptionsTypeDef(TypedDict, total=False):
    Enabled: bool


class EventInformationTypeDef(TypedDict, total=False):
    EventDescription: str
    EventSubType: str
    InstanceId: str


class ExplanationTypeDef(TypedDict, total=False):
    Acl: "AnalysisComponentTypeDef"
    AclRule: "AnalysisAclRuleTypeDef"
    Address: str
    Addresses: List[str]
    AttachedTo: "AnalysisComponentTypeDef"
    AvailabilityZones: List[str]
    Cidrs: List[str]
    Component: "AnalysisComponentTypeDef"
    CustomerGateway: "AnalysisComponentTypeDef"
    Destination: "AnalysisComponentTypeDef"
    DestinationVpc: "AnalysisComponentTypeDef"
    Direction: str
    ExplanationCode: str
    IngressRouteTable: "AnalysisComponentTypeDef"
    InternetGateway: "AnalysisComponentTypeDef"
    LoadBalancerArn: str
    ClassicLoadBalancerListener: "AnalysisLoadBalancerListenerTypeDef"
    LoadBalancerListenerPort: int
    LoadBalancerTarget: "AnalysisLoadBalancerTargetTypeDef"
    LoadBalancerTargetGroup: "AnalysisComponentTypeDef"
    LoadBalancerTargetGroups: List["AnalysisComponentTypeDef"]
    LoadBalancerTargetPort: int
    ElasticLoadBalancerListener: "AnalysisComponentTypeDef"
    MissingComponent: str
    NatGateway: "AnalysisComponentTypeDef"
    NetworkInterface: "AnalysisComponentTypeDef"
    PacketField: str
    VpcPeeringConnection: "AnalysisComponentTypeDef"
    Port: int
    PortRanges: List["PortRangeTypeDef"]
    PrefixList: "AnalysisComponentTypeDef"
    Protocols: List[str]
    RouteTableRoute: "AnalysisRouteTableRouteTypeDef"
    RouteTable: "AnalysisComponentTypeDef"
    SecurityGroup: "AnalysisComponentTypeDef"
    SecurityGroupRule: "AnalysisSecurityGroupRuleTypeDef"
    SecurityGroups: List["AnalysisComponentTypeDef"]
    SourceVpc: "AnalysisComponentTypeDef"
    State: str
    Subnet: "AnalysisComponentTypeDef"
    SubnetRouteTable: "AnalysisComponentTypeDef"
    Vpc: "AnalysisComponentTypeDef"
    VpcEndpoint: "AnalysisComponentTypeDef"
    VpnConnection: "AnalysisComponentTypeDef"
    VpnGateway: "AnalysisComponentTypeDef"


class ExportClientVpnClientCertificateRevocationListResultTypeDef(TypedDict, total=False):
    CertificateRevocationList: str
    Status: "ClientCertificateRevocationListStatusTypeDef"


class ExportClientVpnClientConfigurationResultTypeDef(TypedDict, total=False):
    ClientConfiguration: str


class ExportImageResultTypeDef(TypedDict, total=False):
    Description: str
    DiskImageFormat: DiskImageFormat
    ExportImageTaskId: str
    ImageId: str
    RoleName: str
    Progress: str
    S3ExportLocation: "ExportTaskS3LocationTypeDef"
    Status: str
    StatusMessage: str
    Tags: List["TagTypeDef"]


class ExportImageTaskTypeDef(TypedDict, total=False):
    Description: str
    ExportImageTaskId: str
    ImageId: str
    Progress: str
    S3ExportLocation: "ExportTaskS3LocationTypeDef"
    Status: str
    StatusMessage: str
    Tags: List["TagTypeDef"]


class _RequiredExportTaskS3LocationRequestTypeDef(TypedDict):
    S3Bucket: str


class ExportTaskS3LocationRequestTypeDef(_RequiredExportTaskS3LocationRequestTypeDef, total=False):
    S3Prefix: str


class ExportTaskS3LocationTypeDef(TypedDict, total=False):
    S3Bucket: str
    S3Prefix: str


class ExportTaskTypeDef(TypedDict, total=False):
    Description: str
    ExportTaskId: str
    ExportToS3Task: "ExportToS3TaskTypeDef"
    InstanceExportDetails: "InstanceExportDetailsTypeDef"
    State: ExportTaskState
    StatusMessage: str
    Tags: List["TagTypeDef"]


class ExportToS3TaskSpecificationTypeDef(TypedDict, total=False):
    ContainerFormat: Literal["ova"]
    DiskImageFormat: DiskImageFormat
    S3Bucket: str
    S3Prefix: str


class ExportToS3TaskTypeDef(TypedDict, total=False):
    ContainerFormat: Literal["ova"]
    DiskImageFormat: DiskImageFormat
    S3Bucket: str
    S3Key: str


class ExportTransitGatewayRoutesResultTypeDef(TypedDict, total=False):
    S3Location: str


class FailedQueuedPurchaseDeletionTypeDef(TypedDict, total=False):
    Error: "DeleteQueuedReservedInstancesErrorTypeDef"
    ReservedInstancesId: str


class FederatedAuthenticationRequestTypeDef(TypedDict, total=False):
    SAMLProviderArn: str
    SelfServiceSAMLProviderArn: str


class FederatedAuthenticationTypeDef(TypedDict, total=False):
    SamlProviderArn: str
    SelfServiceSamlProviderArn: str


class FilterTypeDef(TypedDict, total=False):
    Name: str
    Values: List[str]


FleetDataTypeDef = TypedDict(
    "FleetDataTypeDef",
    {
        "ActivityStatus": FleetActivityStatus,
        "CreateTime": datetime,
        "FleetId": str,
        "FleetState": FleetStateCode,
        "ClientToken": str,
        "ExcessCapacityTerminationPolicy": FleetExcessCapacityTerminationPolicy,
        "FulfilledCapacity": float,
        "FulfilledOnDemandCapacity": float,
        "LaunchTemplateConfigs": List["FleetLaunchTemplateConfigTypeDef"],
        "TargetCapacitySpecification": "TargetCapacitySpecificationTypeDef",
        "TerminateInstancesWithExpiration": bool,
        "Type": FleetType,
        "ValidFrom": datetime,
        "ValidUntil": datetime,
        "ReplaceUnhealthyInstances": bool,
        "SpotOptions": "SpotOptionsTypeDef",
        "OnDemandOptions": "OnDemandOptionsTypeDef",
        "Tags": List["TagTypeDef"],
        "Errors": List["DescribeFleetErrorTypeDef"],
        "Instances": List["DescribeFleetsInstancesTypeDef"],
    },
    total=False,
)


class FleetLaunchTemplateConfigRequestTypeDef(TypedDict, total=False):
    LaunchTemplateSpecification: "FleetLaunchTemplateSpecificationRequestTypeDef"
    Overrides: List["FleetLaunchTemplateOverridesRequestTypeDef"]


class FleetLaunchTemplateConfigTypeDef(TypedDict, total=False):
    LaunchTemplateSpecification: "FleetLaunchTemplateSpecificationTypeDef"
    Overrides: List["FleetLaunchTemplateOverridesTypeDef"]


class FleetLaunchTemplateOverridesRequestTypeDef(TypedDict, total=False):
    InstanceType: InstanceType
    MaxPrice: str
    SubnetId: str
    AvailabilityZone: str
    WeightedCapacity: float
    Priority: float
    Placement: "PlacementTypeDef"


class FleetLaunchTemplateOverridesTypeDef(TypedDict, total=False):
    InstanceType: InstanceType
    MaxPrice: str
    SubnetId: str
    AvailabilityZone: str
    WeightedCapacity: float
    Priority: float
    Placement: "PlacementResponseTypeDef"


class FleetLaunchTemplateSpecificationRequestTypeDef(TypedDict, total=False):
    LaunchTemplateId: str
    LaunchTemplateName: str
    Version: str


class FleetLaunchTemplateSpecificationTypeDef(TypedDict, total=False):
    LaunchTemplateId: str
    LaunchTemplateName: str
    Version: str


class FleetSpotCapacityRebalanceRequestTypeDef(TypedDict, total=False):
    ReplacementStrategy: Literal["launch"]


class FleetSpotCapacityRebalanceTypeDef(TypedDict, total=False):
    ReplacementStrategy: Literal["launch"]


class FleetSpotMaintenanceStrategiesRequestTypeDef(TypedDict, total=False):
    CapacityRebalance: "FleetSpotCapacityRebalanceRequestTypeDef"


class FleetSpotMaintenanceStrategiesTypeDef(TypedDict, total=False):
    CapacityRebalance: "FleetSpotCapacityRebalanceTypeDef"


class FlowLogTypeDef(TypedDict, total=False):
    CreationTime: datetime
    DeliverLogsErrorMessage: str
    DeliverLogsPermissionArn: str
    DeliverLogsStatus: str
    FlowLogId: str
    FlowLogStatus: str
    LogGroupName: str
    ResourceId: str
    TrafficType: TrafficType
    LogDestinationType: LogDestinationType
    LogDestination: str
    LogFormat: str
    Tags: List["TagTypeDef"]
    MaxAggregationInterval: int


class FpgaDeviceInfoTypeDef(TypedDict, total=False):
    Name: str
    Manufacturer: str
    Count: int
    MemoryInfo: "FpgaDeviceMemoryInfoTypeDef"


class FpgaDeviceMemoryInfoTypeDef(TypedDict, total=False):
    SizeInMiB: int


class FpgaImageAttributeTypeDef(TypedDict, total=False):
    FpgaImageId: str
    Name: str
    Description: str
    LoadPermissions: List["LoadPermissionTypeDef"]
    ProductCodes: List["ProductCodeTypeDef"]


class FpgaImageStateTypeDef(TypedDict, total=False):
    Code: FpgaImageStateCode
    Message: str


class FpgaImageTypeDef(TypedDict, total=False):
    FpgaImageId: str
    FpgaImageGlobalId: str
    Name: str
    Description: str
    ShellVersion: str
    PciId: "PciIdTypeDef"
    State: "FpgaImageStateTypeDef"
    CreateTime: datetime
    UpdateTime: datetime
    OwnerId: str
    OwnerAlias: str
    ProductCodes: List["ProductCodeTypeDef"]
    Tags: List["TagTypeDef"]
    Public: bool
    DataRetentionSupport: bool


class FpgaInfoTypeDef(TypedDict, total=False):
    Fpgas: List["FpgaDeviceInfoTypeDef"]
    TotalFpgaMemoryInMiB: int


class GetAssociatedEnclaveCertificateIamRolesResultTypeDef(TypedDict, total=False):
    AssociatedRoles: List["AssociatedRoleTypeDef"]


class GetAssociatedIpv6PoolCidrsResultTypeDef(TypedDict, total=False):
    Ipv6CidrAssociations: List["Ipv6CidrAssociationTypeDef"]
    NextToken: str


class GetCapacityReservationUsageResultTypeDef(TypedDict, total=False):
    NextToken: str
    CapacityReservationId: str
    InstanceType: str
    TotalInstanceCount: int
    AvailableInstanceCount: int
    State: CapacityReservationState
    InstanceUsages: List["InstanceUsageTypeDef"]


class GetCoipPoolUsageResultTypeDef(TypedDict, total=False):
    CoipPoolId: str
    CoipAddressUsages: List["CoipAddressUsageTypeDef"]
    LocalGatewayRouteTableId: str


class GetConsoleOutputResultTypeDef(TypedDict, total=False):
    InstanceId: str
    Output: str
    Timestamp: datetime


class GetConsoleScreenshotResultTypeDef(TypedDict, total=False):
    ImageData: str
    InstanceId: str


class GetDefaultCreditSpecificationResultTypeDef(TypedDict, total=False):
    InstanceFamilyCreditSpecification: "InstanceFamilyCreditSpecificationTypeDef"


class GetEbsDefaultKmsKeyIdResultTypeDef(TypedDict, total=False):
    KmsKeyId: str


class GetEbsEncryptionByDefaultResultTypeDef(TypedDict, total=False):
    EbsEncryptionByDefault: bool


class GetFlowLogsIntegrationTemplateResultTypeDef(TypedDict, total=False):
    Result: str


class GetGroupsForCapacityReservationResultTypeDef(TypedDict, total=False):
    NextToken: str
    CapacityReservationGroups: List["CapacityReservationGroupTypeDef"]


class GetHostReservationPurchasePreviewResultTypeDef(TypedDict, total=False):
    CurrencyCode: Literal["USD"]
    Purchase: List["PurchaseTypeDef"]
    TotalHourlyPrice: str
    TotalUpfrontPrice: str


class GetLaunchTemplateDataResultTypeDef(TypedDict, total=False):
    LaunchTemplateData: "ResponseLaunchTemplateDataTypeDef"


class GetManagedPrefixListAssociationsResultTypeDef(TypedDict, total=False):
    PrefixListAssociations: List["PrefixListAssociationTypeDef"]
    NextToken: str


class GetManagedPrefixListEntriesResultTypeDef(TypedDict, total=False):
    Entries: List["PrefixListEntryTypeDef"]
    NextToken: str


class GetPasswordDataResultTypeDef(TypedDict, total=False):
    InstanceId: str
    PasswordData: str
    Timestamp: datetime


class GetReservedInstancesExchangeQuoteResultTypeDef(TypedDict, total=False):
    CurrencyCode: str
    IsValidExchange: bool
    OutputReservedInstancesWillExpireAt: datetime
    PaymentDue: str
    ReservedInstanceValueRollup: "ReservationValueTypeDef"
    ReservedInstanceValueSet: List["ReservedInstanceReservationValueTypeDef"]
    TargetConfigurationValueRollup: "ReservationValueTypeDef"
    TargetConfigurationValueSet: List["TargetReservationValueTypeDef"]
    ValidationFailureReason: str


class GetSerialConsoleAccessStatusResultTypeDef(TypedDict, total=False):
    SerialConsoleAccessEnabled: bool


class GetTransitGatewayAttachmentPropagationsResultTypeDef(TypedDict, total=False):
    TransitGatewayAttachmentPropagations: List["TransitGatewayAttachmentPropagationTypeDef"]
    NextToken: str


class GetTransitGatewayMulticastDomainAssociationsResultTypeDef(TypedDict, total=False):
    MulticastDomainAssociations: List["TransitGatewayMulticastDomainAssociationTypeDef"]
    NextToken: str


class GetTransitGatewayPrefixListReferencesResultTypeDef(TypedDict, total=False):
    TransitGatewayPrefixListReferences: List["TransitGatewayPrefixListReferenceTypeDef"]
    NextToken: str


class GetTransitGatewayRouteTableAssociationsResultTypeDef(TypedDict, total=False):
    Associations: List["TransitGatewayRouteTableAssociationTypeDef"]
    NextToken: str


class GetTransitGatewayRouteTablePropagationsResultTypeDef(TypedDict, total=False):
    TransitGatewayRouteTablePropagations: List["TransitGatewayRouteTablePropagationTypeDef"]
    NextToken: str


class GpuDeviceInfoTypeDef(TypedDict, total=False):
    Name: str
    Manufacturer: str
    Count: int
    MemoryInfo: "GpuDeviceMemoryInfoTypeDef"


class GpuDeviceMemoryInfoTypeDef(TypedDict, total=False):
    SizeInMiB: int


class GpuInfoTypeDef(TypedDict, total=False):
    Gpus: List["GpuDeviceInfoTypeDef"]
    TotalGpuMemoryInMiB: int


class GroupIdentifierTypeDef(TypedDict, total=False):
    GroupName: str
    GroupId: str


class HibernationOptionsRequestTypeDef(TypedDict, total=False):
    Configured: bool


class HibernationOptionsTypeDef(TypedDict, total=False):
    Configured: bool


class HistoryRecordEntryTypeDef(TypedDict, total=False):
    EventInformation: "EventInformationTypeDef"
    EventType: FleetEventType
    Timestamp: datetime


class HistoryRecordTypeDef(TypedDict, total=False):
    EventInformation: "EventInformationTypeDef"
    EventType: EventType
    Timestamp: datetime


class HostInstanceTypeDef(TypedDict, total=False):
    InstanceId: str
    InstanceType: str
    OwnerId: str


class HostOfferingTypeDef(TypedDict, total=False):
    CurrencyCode: Literal["USD"]
    Duration: int
    HourlyPrice: str
    InstanceFamily: str
    OfferingId: str
    PaymentOption: PaymentOption
    UpfrontPrice: str


class HostPropertiesTypeDef(TypedDict, total=False):
    Cores: int
    InstanceType: str
    InstanceFamily: str
    Sockets: int
    TotalVCpus: int


class HostReservationTypeDef(TypedDict, total=False):
    Count: int
    CurrencyCode: Literal["USD"]
    Duration: int
    End: datetime
    HostIdSet: List[str]
    HostReservationId: str
    HourlyPrice: str
    InstanceFamily: str
    OfferingId: str
    PaymentOption: PaymentOption
    Start: datetime
    State: ReservationState
    UpfrontPrice: str
    Tags: List["TagTypeDef"]


class HostTypeDef(TypedDict, total=False):
    AutoPlacement: AutoPlacement
    AvailabilityZone: str
    AvailableCapacity: "AvailableCapacityTypeDef"
    ClientToken: str
    HostId: str
    HostProperties: "HostPropertiesTypeDef"
    HostReservationId: str
    Instances: List["HostInstanceTypeDef"]
    State: AllocationState
    AllocationTime: datetime
    ReleaseTime: datetime
    Tags: List["TagTypeDef"]
    HostRecovery: HostRecovery
    AllowsMultipleInstanceTypes: AllowsMultipleInstanceTypes
    OwnerId: str
    AvailabilityZoneId: str
    MemberOfServiceLinkedResourceGroup: bool


class IKEVersionsListValueTypeDef(TypedDict, total=False):
    Value: str


class IKEVersionsRequestListValueTypeDef(TypedDict, total=False):
    Value: str


class IamInstanceProfileAssociationTypeDef(TypedDict, total=False):
    AssociationId: str
    InstanceId: str
    IamInstanceProfile: "IamInstanceProfileTypeDef"
    State: IamInstanceProfileAssociationState
    Timestamp: datetime


class IamInstanceProfileSpecificationTypeDef(TypedDict, total=False):
    Arn: str
    Name: str


class IamInstanceProfileTypeDef(TypedDict, total=False):
    Arn: str
    Id: str


IcmpTypeCodeTypeDef = TypedDict("IcmpTypeCodeTypeDef", {"Code": int, "Type": int}, total=False)


class IdFormatTypeDef(TypedDict, total=False):
    Deadline: datetime
    Resource: str
    UseLongIds: bool


class ImageAttributeTypeDef(TypedDict, total=False):
    BlockDeviceMappings: List["BlockDeviceMappingTypeDef"]
    ImageId: str
    LaunchPermissions: List["LaunchPermissionTypeDef"]
    ProductCodes: List["ProductCodeTypeDef"]
    Description: "AttributeValueTypeDef"
    KernelId: "AttributeValueTypeDef"
    RamdiskId: "AttributeValueTypeDef"
    SriovNetSupport: "AttributeValueTypeDef"
    BootMode: "AttributeValueTypeDef"


class ImageDiskContainerTypeDef(TypedDict, total=False):
    Description: str
    DeviceName: str
    Format: str
    SnapshotId: str
    Url: str
    UserBucket: "UserBucketTypeDef"


class ImageTypeDef(TypedDict, total=False):
    Architecture: ArchitectureValues
    CreationDate: str
    ImageId: str
    ImageLocation: str
    ImageType: ImageTypeValues
    Public: bool
    KernelId: str
    OwnerId: str
    Platform: Literal["Windows"]
    PlatformDetails: str
    UsageOperation: str
    ProductCodes: List["ProductCodeTypeDef"]
    RamdiskId: str
    State: ImageState
    BlockDeviceMappings: List["BlockDeviceMappingTypeDef"]
    Description: str
    EnaSupport: bool
    Hypervisor: HypervisorType
    ImageOwnerAlias: str
    Name: str
    RootDeviceName: str
    RootDeviceType: DeviceType
    SriovNetSupport: str
    StateReason: "StateReasonTypeDef"
    Tags: List["TagTypeDef"]
    VirtualizationType: VirtualizationType
    BootMode: BootModeValues


class ImportClientVpnClientCertificateRevocationListResultTypeDef(TypedDict, total=False):
    Return: bool


class ImportImageLicenseConfigurationRequestTypeDef(TypedDict, total=False):
    LicenseConfigurationArn: str


class ImportImageLicenseConfigurationResponseTypeDef(TypedDict, total=False):
    LicenseConfigurationArn: str


class ImportImageResultTypeDef(TypedDict, total=False):
    Architecture: str
    Description: str
    Encrypted: bool
    Hypervisor: str
    ImageId: str
    ImportTaskId: str
    KmsKeyId: str
    LicenseType: str
    Platform: str
    Progress: str
    SnapshotDetails: List["SnapshotDetailTypeDef"]
    Status: str
    StatusMessage: str
    LicenseSpecifications: List["ImportImageLicenseConfigurationResponseTypeDef"]
    Tags: List["TagTypeDef"]


class ImportImageTaskTypeDef(TypedDict, total=False):
    Architecture: str
    Description: str
    Encrypted: bool
    Hypervisor: str
    ImageId: str
    ImportTaskId: str
    KmsKeyId: str
    LicenseType: str
    Platform: str
    Progress: str
    SnapshotDetails: List["SnapshotDetailTypeDef"]
    Status: str
    StatusMessage: str
    Tags: List["TagTypeDef"]
    LicenseSpecifications: List["ImportImageLicenseConfigurationResponseTypeDef"]


class ImportInstanceLaunchSpecificationTypeDef(TypedDict, total=False):
    AdditionalInfo: str
    Architecture: ArchitectureValues
    GroupIds: List[str]
    GroupNames: List[str]
    InstanceInitiatedShutdownBehavior: ShutdownBehavior
    InstanceType: InstanceType
    Monitoring: bool
    Placement: "PlacementTypeDef"
    PrivateIpAddress: str
    SubnetId: str
    UserData: "UserDataTypeDef"


class ImportInstanceResultTypeDef(TypedDict, total=False):
    ConversionTask: "ConversionTaskTypeDef"


class ImportInstanceTaskDetailsTypeDef(TypedDict, total=False):
    Description: str
    InstanceId: str
    Platform: Literal["Windows"]
    Volumes: List["ImportInstanceVolumeDetailItemTypeDef"]


class ImportInstanceVolumeDetailItemTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    BytesConverted: int
    Description: str
    Image: "DiskImageDescriptionTypeDef"
    Status: str
    StatusMessage: str
    Volume: "DiskImageVolumeDescriptionTypeDef"


class ImportKeyPairResultTypeDef(TypedDict, total=False):
    KeyFingerprint: str
    KeyName: str
    KeyPairId: str
    Tags: List["TagTypeDef"]


class ImportSnapshotResultTypeDef(TypedDict, total=False):
    Description: str
    ImportTaskId: str
    SnapshotTaskDetail: "SnapshotTaskDetailTypeDef"
    Tags: List["TagTypeDef"]


class ImportSnapshotTaskTypeDef(TypedDict, total=False):
    Description: str
    ImportTaskId: str
    SnapshotTaskDetail: "SnapshotTaskDetailTypeDef"
    Tags: List["TagTypeDef"]


class ImportVolumeResultTypeDef(TypedDict, total=False):
    ConversionTask: "ConversionTaskTypeDef"


class ImportVolumeTaskDetailsTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    BytesConverted: int
    Description: str
    Image: "DiskImageDescriptionTypeDef"
    Volume: "DiskImageVolumeDescriptionTypeDef"


class InferenceAcceleratorInfoTypeDef(TypedDict, total=False):
    Accelerators: List["InferenceDeviceInfoTypeDef"]


class InferenceDeviceInfoTypeDef(TypedDict, total=False):
    Count: int
    Name: str
    Manufacturer: str


class InstanceAttributeTypeDef(TypedDict, total=False):
    Groups: List["GroupIdentifierTypeDef"]
    BlockDeviceMappings: List["InstanceBlockDeviceMappingTypeDef"]
    DisableApiTermination: "AttributeBooleanValueTypeDef"
    EnaSupport: "AttributeBooleanValueTypeDef"
    EnclaveOptions: "EnclaveOptionsTypeDef"
    EbsOptimized: "AttributeBooleanValueTypeDef"
    InstanceId: str
    InstanceInitiatedShutdownBehavior: "AttributeValueTypeDef"
    InstanceType: "AttributeValueTypeDef"
    KernelId: "AttributeValueTypeDef"
    ProductCodes: List["ProductCodeTypeDef"]
    RamdiskId: "AttributeValueTypeDef"
    RootDeviceName: "AttributeValueTypeDef"
    SourceDestCheck: "AttributeBooleanValueTypeDef"
    SriovNetSupport: "AttributeValueTypeDef"
    UserData: "AttributeValueTypeDef"


class InstanceBlockDeviceMappingSpecificationTypeDef(TypedDict, total=False):
    DeviceName: str
    Ebs: "EbsInstanceBlockDeviceSpecificationTypeDef"
    NoDevice: str
    VirtualName: str


class InstanceBlockDeviceMappingTypeDef(TypedDict, total=False):
    DeviceName: str
    Ebs: "EbsInstanceBlockDeviceTypeDef"


class InstanceCapacityTypeDef(TypedDict, total=False):
    AvailableCapacity: int
    InstanceType: str
    TotalCapacity: int


class InstanceCountTypeDef(TypedDict, total=False):
    InstanceCount: int
    State: ListingState


class InstanceCreditSpecificationRequestTypeDef(TypedDict, total=False):
    InstanceId: str
    CpuCredits: str


class InstanceCreditSpecificationTypeDef(TypedDict, total=False):
    InstanceId: str
    CpuCredits: str


class InstanceExportDetailsTypeDef(TypedDict, total=False):
    InstanceId: str
    TargetEnvironment: ExportEnvironment


class InstanceFamilyCreditSpecificationTypeDef(TypedDict, total=False):
    InstanceFamily: UnlimitedSupportedInstanceFamily
    CpuCredits: str


class InstanceIpv6AddressRequestTypeDef(TypedDict, total=False):
    Ipv6Address: str


class InstanceIpv6AddressTypeDef(TypedDict, total=False):
    Ipv6Address: str


class InstanceMarketOptionsRequestTypeDef(TypedDict, total=False):
    MarketType: Literal["spot"]
    SpotOptions: "SpotMarketOptionsTypeDef"


class InstanceMetadataOptionsRequestTypeDef(TypedDict, total=False):
    HttpTokens: HttpTokensState
    HttpPutResponseHopLimit: int
    HttpEndpoint: InstanceMetadataEndpointState


class InstanceMetadataOptionsResponseTypeDef(TypedDict, total=False):
    State: InstanceMetadataOptionsState
    HttpTokens: HttpTokensState
    HttpPutResponseHopLimit: int
    HttpEndpoint: InstanceMetadataEndpointState


class InstanceMonitoringTypeDef(TypedDict, total=False):
    InstanceId: str
    Monitoring: "MonitoringTypeDef"


class InstanceNetworkInterfaceAssociationTypeDef(TypedDict, total=False):
    CarrierIp: str
    IpOwnerId: str
    PublicDnsName: str
    PublicIp: str


class InstanceNetworkInterfaceAttachmentTypeDef(TypedDict, total=False):
    AttachTime: datetime
    AttachmentId: str
    DeleteOnTermination: bool
    DeviceIndex: int
    Status: AttachmentStatus
    NetworkCardIndex: int


class InstanceNetworkInterfaceSpecificationTypeDef(TypedDict, total=False):
    AssociatePublicIpAddress: bool
    DeleteOnTermination: bool
    Description: str
    DeviceIndex: int
    Groups: List[str]
    Ipv6AddressCount: int
    Ipv6Addresses: List["InstanceIpv6AddressTypeDef"]
    NetworkInterfaceId: str
    PrivateIpAddress: str
    PrivateIpAddresses: List["PrivateIpAddressSpecificationTypeDef"]
    SecondaryPrivateIpAddressCount: int
    SubnetId: str
    AssociateCarrierIpAddress: bool
    InterfaceType: str
    NetworkCardIndex: int


class InstanceNetworkInterfaceTypeDef(TypedDict, total=False):
    Association: "InstanceNetworkInterfaceAssociationTypeDef"
    Attachment: "InstanceNetworkInterfaceAttachmentTypeDef"
    Description: str
    Groups: List["GroupIdentifierTypeDef"]
    Ipv6Addresses: List["InstanceIpv6AddressTypeDef"]
    MacAddress: str
    NetworkInterfaceId: str
    OwnerId: str
    PrivateDnsName: str
    PrivateIpAddress: str
    PrivateIpAddresses: List["InstancePrivateIpAddressTypeDef"]
    SourceDestCheck: bool
    Status: NetworkInterfaceStatus
    SubnetId: str
    VpcId: str
    InterfaceType: str


class InstancePrivateIpAddressTypeDef(TypedDict, total=False):
    Association: "InstanceNetworkInterfaceAssociationTypeDef"
    Primary: bool
    PrivateDnsName: str
    PrivateIpAddress: str


class InstanceSpecificationTypeDef(TypedDict, total=False):
    InstanceId: str
    ExcludeBootVolume: bool


class InstanceStateChangeTypeDef(TypedDict, total=False):
    CurrentState: "InstanceStateTypeDef"
    InstanceId: str
    PreviousState: "InstanceStateTypeDef"


class InstanceStateTypeDef(TypedDict, total=False):
    Code: int
    Name: InstanceStateName


class InstanceStatusDetailsTypeDef(TypedDict, total=False):
    ImpairedSince: datetime
    Name: Literal["reachability"]
    Status: StatusType


class InstanceStatusEventTypeDef(TypedDict, total=False):
    InstanceEventId: str
    Code: EventCode
    Description: str
    NotAfter: datetime
    NotBefore: datetime
    NotBeforeDeadline: datetime


class InstanceStatusSummaryTypeDef(TypedDict, total=False):
    Details: List["InstanceStatusDetailsTypeDef"]
    Status: SummaryStatus


class InstanceStatusTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    OutpostArn: str
    Events: List["InstanceStatusEventTypeDef"]
    InstanceId: str
    InstanceState: "InstanceStateTypeDef"
    InstanceStatus: "InstanceStatusSummaryTypeDef"
    SystemStatus: "InstanceStatusSummaryTypeDef"


class InstanceStorageInfoTypeDef(TypedDict, total=False):
    TotalSizeInGB: int
    Disks: List["DiskInfoTypeDef"]
    NvmeSupport: EphemeralNvmeSupport


class InstanceTagNotificationAttributeTypeDef(TypedDict, total=False):
    InstanceTagKeys: List[str]
    IncludeAllTagsOfInstance: bool


class InstanceTypeDef(TypedDict, total=False):
    AmiLaunchIndex: int
    ImageId: str
    InstanceId: str
    InstanceType: InstanceType
    KernelId: str
    KeyName: str
    LaunchTime: datetime
    Monitoring: "MonitoringTypeDef"
    Placement: "PlacementTypeDef"
    Platform: Literal["Windows"]
    PrivateDnsName: str
    PrivateIpAddress: str
    ProductCodes: List["ProductCodeTypeDef"]
    PublicDnsName: str
    PublicIpAddress: str
    RamdiskId: str
    State: "InstanceStateTypeDef"
    StateTransitionReason: str
    SubnetId: str
    VpcId: str
    Architecture: ArchitectureValues
    BlockDeviceMappings: List["InstanceBlockDeviceMappingTypeDef"]
    ClientToken: str
    EbsOptimized: bool
    EnaSupport: bool
    Hypervisor: HypervisorType
    IamInstanceProfile: "IamInstanceProfileTypeDef"
    InstanceLifecycle: InstanceLifecycleType
    ElasticGpuAssociations: List["ElasticGpuAssociationTypeDef"]
    ElasticInferenceAcceleratorAssociations: List["ElasticInferenceAcceleratorAssociationTypeDef"]
    NetworkInterfaces: List["InstanceNetworkInterfaceTypeDef"]
    OutpostArn: str
    RootDeviceName: str
    RootDeviceType: DeviceType
    SecurityGroups: List["GroupIdentifierTypeDef"]
    SourceDestCheck: bool
    SpotInstanceRequestId: str
    SriovNetSupport: str
    StateReason: "StateReasonTypeDef"
    Tags: List["TagTypeDef"]
    VirtualizationType: VirtualizationType
    CpuOptions: "CpuOptionsTypeDef"
    CapacityReservationId: str
    CapacityReservationSpecification: "CapacityReservationSpecificationResponseTypeDef"
    HibernationOptions: "HibernationOptionsTypeDef"
    Licenses: List["LicenseConfigurationTypeDef"]
    MetadataOptions: "InstanceMetadataOptionsResponseTypeDef"
    EnclaveOptions: "EnclaveOptionsTypeDef"
    BootMode: BootModeValues


class InstanceTypeInfoTypeDef(TypedDict, total=False):
    InstanceType: InstanceType
    CurrentGeneration: bool
    FreeTierEligible: bool
    SupportedUsageClasses: List[UsageClassType]
    SupportedRootDeviceTypes: List[RootDeviceType]
    SupportedVirtualizationTypes: List[VirtualizationType]
    BareMetal: bool
    Hypervisor: InstanceTypeHypervisor
    ProcessorInfo: "ProcessorInfoTypeDef"
    VCpuInfo: "VCpuInfoTypeDef"
    MemoryInfo: "MemoryInfoTypeDef"
    InstanceStorageSupported: bool
    InstanceStorageInfo: "InstanceStorageInfoTypeDef"
    EbsInfo: "EbsInfoTypeDef"
    NetworkInfo: "NetworkInfoTypeDef"
    GpuInfo: "GpuInfoTypeDef"
    FpgaInfo: "FpgaInfoTypeDef"
    PlacementGroupInfo: "PlacementGroupInfoTypeDef"
    InferenceAcceleratorInfo: "InferenceAcceleratorInfoTypeDef"
    HibernationSupported: bool
    BurstablePerformanceSupported: bool
    DedicatedHostsSupported: bool
    AutoRecoverySupported: bool
    SupportedBootModes: List[BootModeType]


class InstanceTypeOfferingTypeDef(TypedDict, total=False):
    InstanceType: InstanceType
    LocationType: LocationType
    Location: str


class InstanceUsageTypeDef(TypedDict, total=False):
    AccountId: str
    UsedInstanceCount: int


class IntegrateServicesTypeDef(TypedDict, total=False):
    AthenaIntegrations: List["AthenaIntegrationTypeDef"]


class InternetGatewayAttachmentTypeDef(TypedDict, total=False):
    State: AttachmentStatus
    VpcId: str


class InternetGatewayTypeDef(TypedDict, total=False):
    Attachments: List["InternetGatewayAttachmentTypeDef"]
    InternetGatewayId: str
    OwnerId: str
    Tags: List["TagTypeDef"]


class IpPermissionTypeDef(TypedDict, total=False):
    FromPort: int
    IpProtocol: str
    IpRanges: List["IpRangeTypeDef"]
    Ipv6Ranges: List["Ipv6RangeTypeDef"]
    PrefixListIds: List["PrefixListIdTypeDef"]
    ToPort: int
    UserIdGroupPairs: List["UserIdGroupPairTypeDef"]


class IpRangeTypeDef(TypedDict, total=False):
    CidrIp: str
    Description: str


class Ipv6CidrAssociationTypeDef(TypedDict, total=False):
    Ipv6Cidr: str
    AssociatedResource: str


class Ipv6CidrBlockTypeDef(TypedDict, total=False):
    Ipv6CidrBlock: str


class Ipv6PoolTypeDef(TypedDict, total=False):
    PoolId: str
    Description: str
    PoolCidrBlocks: List["PoolCidrBlockTypeDef"]
    Tags: List["TagTypeDef"]


class Ipv6RangeTypeDef(TypedDict, total=False):
    CidrIpv6: str
    Description: str


class KeyPairInfoTypeDef(TypedDict, total=False):
    KeyPairId: str
    KeyFingerprint: str
    KeyName: str
    Tags: List["TagTypeDef"]


class KeyPairTypeDef(TypedDict, total=False):
    KeyFingerprint: str
    KeyMaterial: str
    KeyName: str
    KeyPairId: str
    Tags: List["TagTypeDef"]


class LastErrorTypeDef(TypedDict, total=False):
    Message: str
    Code: str


class LaunchPermissionModificationsTypeDef(TypedDict, total=False):
    Add: List["LaunchPermissionTypeDef"]
    Remove: List["LaunchPermissionTypeDef"]


class LaunchPermissionTypeDef(TypedDict, total=False):
    Group: Literal["all"]
    UserId: str


class LaunchSpecificationTypeDef(TypedDict, total=False):
    UserData: str
    SecurityGroups: List["GroupIdentifierTypeDef"]
    AddressingType: str
    BlockDeviceMappings: List["BlockDeviceMappingTypeDef"]
    EbsOptimized: bool
    IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef"
    ImageId: str
    InstanceType: InstanceType
    KernelId: str
    KeyName: str
    NetworkInterfaces: List["InstanceNetworkInterfaceSpecificationTypeDef"]
    Placement: "SpotPlacementTypeDef"
    RamdiskId: str
    SubnetId: str
    Monitoring: "RunInstancesMonitoringEnabledTypeDef"


class LaunchTemplateAndOverridesResponseTypeDef(TypedDict, total=False):
    LaunchTemplateSpecification: "FleetLaunchTemplateSpecificationTypeDef"
    Overrides: "FleetLaunchTemplateOverridesTypeDef"


class LaunchTemplateBlockDeviceMappingRequestTypeDef(TypedDict, total=False):
    DeviceName: str
    VirtualName: str
    Ebs: "LaunchTemplateEbsBlockDeviceRequestTypeDef"
    NoDevice: str


class LaunchTemplateBlockDeviceMappingTypeDef(TypedDict, total=False):
    DeviceName: str
    VirtualName: str
    Ebs: "LaunchTemplateEbsBlockDeviceTypeDef"
    NoDevice: str


class LaunchTemplateCapacityReservationSpecificationRequestTypeDef(TypedDict, total=False):
    CapacityReservationPreference: CapacityReservationPreference
    CapacityReservationTarget: "CapacityReservationTargetTypeDef"


class LaunchTemplateCapacityReservationSpecificationResponseTypeDef(TypedDict, total=False):
    CapacityReservationPreference: CapacityReservationPreference
    CapacityReservationTarget: "CapacityReservationTargetResponseTypeDef"


class LaunchTemplateConfigTypeDef(TypedDict, total=False):
    LaunchTemplateSpecification: "FleetLaunchTemplateSpecificationTypeDef"
    Overrides: List["LaunchTemplateOverridesTypeDef"]


class LaunchTemplateCpuOptionsRequestTypeDef(TypedDict, total=False):
    CoreCount: int
    ThreadsPerCore: int


class LaunchTemplateCpuOptionsTypeDef(TypedDict, total=False):
    CoreCount: int
    ThreadsPerCore: int


class LaunchTemplateEbsBlockDeviceRequestTypeDef(TypedDict, total=False):
    Encrypted: bool
    DeleteOnTermination: bool
    Iops: int
    KmsKeyId: str
    SnapshotId: str
    VolumeSize: int
    VolumeType: VolumeType
    Throughput: int


class LaunchTemplateEbsBlockDeviceTypeDef(TypedDict, total=False):
    Encrypted: bool
    DeleteOnTermination: bool
    Iops: int
    KmsKeyId: str
    SnapshotId: str
    VolumeSize: int
    VolumeType: VolumeType
    Throughput: int


LaunchTemplateElasticInferenceAcceleratorResponseTypeDef = TypedDict(
    "LaunchTemplateElasticInferenceAcceleratorResponseTypeDef",
    {"Type": str, "Count": int},
    total=False,
)

_RequiredLaunchTemplateElasticInferenceAcceleratorTypeDef = TypedDict(
    "_RequiredLaunchTemplateElasticInferenceAcceleratorTypeDef", {"Type": str}
)
_OptionalLaunchTemplateElasticInferenceAcceleratorTypeDef = TypedDict(
    "_OptionalLaunchTemplateElasticInferenceAcceleratorTypeDef", {"Count": int}, total=False
)


class LaunchTemplateElasticInferenceAcceleratorTypeDef(
    _RequiredLaunchTemplateElasticInferenceAcceleratorTypeDef,
    _OptionalLaunchTemplateElasticInferenceAcceleratorTypeDef,
):
    pass


class LaunchTemplateEnclaveOptionsRequestTypeDef(TypedDict, total=False):
    Enabled: bool


class LaunchTemplateEnclaveOptionsTypeDef(TypedDict, total=False):
    Enabled: bool


class LaunchTemplateHibernationOptionsRequestTypeDef(TypedDict, total=False):
    Configured: bool


class LaunchTemplateHibernationOptionsTypeDef(TypedDict, total=False):
    Configured: bool


class LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef(TypedDict, total=False):
    Arn: str
    Name: str


class LaunchTemplateIamInstanceProfileSpecificationTypeDef(TypedDict, total=False):
    Arn: str
    Name: str


class LaunchTemplateInstanceMarketOptionsRequestTypeDef(TypedDict, total=False):
    MarketType: Literal["spot"]
    SpotOptions: "LaunchTemplateSpotMarketOptionsRequestTypeDef"


class LaunchTemplateInstanceMarketOptionsTypeDef(TypedDict, total=False):
    MarketType: Literal["spot"]
    SpotOptions: "LaunchTemplateSpotMarketOptionsTypeDef"


class LaunchTemplateInstanceMetadataOptionsRequestTypeDef(TypedDict, total=False):
    HttpTokens: LaunchTemplateHttpTokensState
    HttpPutResponseHopLimit: int
    HttpEndpoint: LaunchTemplateInstanceMetadataEndpointState


class LaunchTemplateInstanceMetadataOptionsTypeDef(TypedDict, total=False):
    State: LaunchTemplateInstanceMetadataOptionsState
    HttpTokens: LaunchTemplateHttpTokensState
    HttpPutResponseHopLimit: int
    HttpEndpoint: LaunchTemplateInstanceMetadataEndpointState


class LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef(TypedDict, total=False):
    AssociateCarrierIpAddress: bool
    AssociatePublicIpAddress: bool
    DeleteOnTermination: bool
    Description: str
    DeviceIndex: int
    Groups: List[str]
    InterfaceType: str
    Ipv6AddressCount: int
    Ipv6Addresses: List["InstanceIpv6AddressRequestTypeDef"]
    NetworkInterfaceId: str
    PrivateIpAddress: str
    PrivateIpAddresses: List["PrivateIpAddressSpecificationTypeDef"]
    SecondaryPrivateIpAddressCount: int
    SubnetId: str
    NetworkCardIndex: int


class LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef(TypedDict, total=False):
    AssociateCarrierIpAddress: bool
    AssociatePublicIpAddress: bool
    DeleteOnTermination: bool
    Description: str
    DeviceIndex: int
    Groups: List[str]
    InterfaceType: str
    Ipv6AddressCount: int
    Ipv6Addresses: List["InstanceIpv6AddressTypeDef"]
    NetworkInterfaceId: str
    PrivateIpAddress: str
    PrivateIpAddresses: List["PrivateIpAddressSpecificationTypeDef"]
    SecondaryPrivateIpAddressCount: int
    SubnetId: str
    NetworkCardIndex: int


class LaunchTemplateLicenseConfigurationRequestTypeDef(TypedDict, total=False):
    LicenseConfigurationArn: str


class LaunchTemplateLicenseConfigurationTypeDef(TypedDict, total=False):
    LicenseConfigurationArn: str


class LaunchTemplateOverridesTypeDef(TypedDict, total=False):
    InstanceType: InstanceType
    SpotPrice: str
    SubnetId: str
    AvailabilityZone: str
    WeightedCapacity: float
    Priority: float


class LaunchTemplatePlacementRequestTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    Affinity: str
    GroupName: str
    HostId: str
    Tenancy: Tenancy
    SpreadDomain: str
    HostResourceGroupArn: str
    PartitionNumber: int


class LaunchTemplatePlacementTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    Affinity: str
    GroupName: str
    HostId: str
    Tenancy: Tenancy
    SpreadDomain: str
    HostResourceGroupArn: str
    PartitionNumber: int


class LaunchTemplateSpecificationTypeDef(TypedDict, total=False):
    LaunchTemplateId: str
    LaunchTemplateName: str
    Version: str


class LaunchTemplateSpotMarketOptionsRequestTypeDef(TypedDict, total=False):
    MaxPrice: str
    SpotInstanceType: SpotInstanceType
    BlockDurationMinutes: int
    ValidUntil: datetime
    InstanceInterruptionBehavior: InstanceInterruptionBehavior


class LaunchTemplateSpotMarketOptionsTypeDef(TypedDict, total=False):
    MaxPrice: str
    SpotInstanceType: SpotInstanceType
    BlockDurationMinutes: int
    ValidUntil: datetime
    InstanceInterruptionBehavior: InstanceInterruptionBehavior


class LaunchTemplateTagSpecificationRequestTypeDef(TypedDict, total=False):
    ResourceType: ResourceType
    Tags: List["TagTypeDef"]


class LaunchTemplateTagSpecificationTypeDef(TypedDict, total=False):
    ResourceType: ResourceType
    Tags: List["TagTypeDef"]


class LaunchTemplateTypeDef(TypedDict, total=False):
    LaunchTemplateId: str
    LaunchTemplateName: str
    CreateTime: datetime
    CreatedBy: str
    DefaultVersionNumber: int
    LatestVersionNumber: int
    Tags: List["TagTypeDef"]


class LaunchTemplateVersionTypeDef(TypedDict, total=False):
    LaunchTemplateId: str
    LaunchTemplateName: str
    VersionNumber: int
    VersionDescription: str
    CreateTime: datetime
    CreatedBy: str
    DefaultVersion: bool
    LaunchTemplateData: "ResponseLaunchTemplateDataTypeDef"


class LaunchTemplatesMonitoringRequestTypeDef(TypedDict, total=False):
    Enabled: bool


class LaunchTemplatesMonitoringTypeDef(TypedDict, total=False):
    Enabled: bool


class LicenseConfigurationRequestTypeDef(TypedDict, total=False):
    LicenseConfigurationArn: str


class LicenseConfigurationTypeDef(TypedDict, total=False):
    LicenseConfigurationArn: str


class LoadBalancersConfigTypeDef(TypedDict, total=False):
    ClassicLoadBalancersConfig: "ClassicLoadBalancersConfigTypeDef"
    TargetGroupsConfig: "TargetGroupsConfigTypeDef"


class LoadPermissionModificationsTypeDef(TypedDict, total=False):
    Add: List["LoadPermissionRequestTypeDef"]
    Remove: List["LoadPermissionRequestTypeDef"]


class LoadPermissionRequestTypeDef(TypedDict, total=False):
    Group: Literal["all"]
    UserId: str


class LoadPermissionTypeDef(TypedDict, total=False):
    UserId: str
    Group: Literal["all"]


class LocalGatewayRouteTableTypeDef(TypedDict, total=False):
    LocalGatewayRouteTableId: str
    LocalGatewayRouteTableArn: str
    LocalGatewayId: str
    OutpostArn: str
    OwnerId: str
    State: str
    Tags: List["TagTypeDef"]


class LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef(TypedDict, total=False):
    LocalGatewayRouteTableVirtualInterfaceGroupAssociationId: str
    LocalGatewayVirtualInterfaceGroupId: str
    LocalGatewayId: str
    LocalGatewayRouteTableId: str
    LocalGatewayRouteTableArn: str
    OwnerId: str
    State: str
    Tags: List["TagTypeDef"]


class LocalGatewayRouteTableVpcAssociationTypeDef(TypedDict, total=False):
    LocalGatewayRouteTableVpcAssociationId: str
    LocalGatewayRouteTableId: str
    LocalGatewayRouteTableArn: str
    LocalGatewayId: str
    VpcId: str
    OwnerId: str
    State: str
    Tags: List["TagTypeDef"]


LocalGatewayRouteTypeDef = TypedDict(
    "LocalGatewayRouteTypeDef",
    {
        "DestinationCidrBlock": str,
        "LocalGatewayVirtualInterfaceGroupId": str,
        "Type": LocalGatewayRouteType,
        "State": LocalGatewayRouteState,
        "LocalGatewayRouteTableId": str,
        "LocalGatewayRouteTableArn": str,
        "OwnerId": str,
    },
    total=False,
)


class LocalGatewayTypeDef(TypedDict, total=False):
    LocalGatewayId: str
    OutpostArn: str
    OwnerId: str
    State: str
    Tags: List["TagTypeDef"]


class LocalGatewayVirtualInterfaceGroupTypeDef(TypedDict, total=False):
    LocalGatewayVirtualInterfaceGroupId: str
    LocalGatewayVirtualInterfaceIds: List[str]
    LocalGatewayId: str
    OwnerId: str
    Tags: List["TagTypeDef"]


class LocalGatewayVirtualInterfaceTypeDef(TypedDict, total=False):
    LocalGatewayVirtualInterfaceId: str
    LocalGatewayId: str
    Vlan: int
    LocalAddress: str
    PeerAddress: str
    LocalBgpAsn: int
    PeerBgpAsn: int
    OwnerId: str
    Tags: List["TagTypeDef"]


class ManagedPrefixListTypeDef(TypedDict, total=False):
    PrefixListId: str
    AddressFamily: str
    State: PrefixListState
    StateMessage: str
    PrefixListArn: str
    PrefixListName: str
    MaxEntries: int
    Version: int
    Tags: List["TagTypeDef"]
    OwnerId: str


class MemoryInfoTypeDef(TypedDict, total=False):
    SizeInMiB: int


class ModifyAddressAttributeResultTypeDef(TypedDict, total=False):
    Address: "AddressAttributeTypeDef"


class ModifyAvailabilityZoneGroupResultTypeDef(TypedDict, total=False):
    Return: bool


class ModifyCapacityReservationResultTypeDef(TypedDict, total=False):
    Return: bool


class ModifyClientVpnEndpointResultTypeDef(TypedDict, total=False):
    Return: bool


class ModifyDefaultCreditSpecificationResultTypeDef(TypedDict, total=False):
    InstanceFamilyCreditSpecification: "InstanceFamilyCreditSpecificationTypeDef"


class ModifyEbsDefaultKmsKeyIdResultTypeDef(TypedDict, total=False):
    KmsKeyId: str


class ModifyFleetResultTypeDef(TypedDict, total=False):
    Return: bool


class ModifyFpgaImageAttributeResultTypeDef(TypedDict, total=False):
    FpgaImageAttribute: "FpgaImageAttributeTypeDef"


class ModifyHostsResultTypeDef(TypedDict, total=False):
    Successful: List[str]
    Unsuccessful: List["UnsuccessfulItemTypeDef"]


class ModifyInstanceCapacityReservationAttributesResultTypeDef(TypedDict, total=False):
    Return: bool


class ModifyInstanceCreditSpecificationResultTypeDef(TypedDict, total=False):
    SuccessfulInstanceCreditSpecifications: List["SuccessfulInstanceCreditSpecificationItemTypeDef"]
    UnsuccessfulInstanceCreditSpecifications: List[
        "UnsuccessfulInstanceCreditSpecificationItemTypeDef"
    ]


class ModifyInstanceEventStartTimeResultTypeDef(TypedDict, total=False):
    Event: "InstanceStatusEventTypeDef"


class ModifyInstanceMetadataOptionsResultTypeDef(TypedDict, total=False):
    InstanceId: str
    InstanceMetadataOptions: "InstanceMetadataOptionsResponseTypeDef"


class ModifyInstancePlacementResultTypeDef(TypedDict, total=False):
    Return: bool


class ModifyLaunchTemplateResultTypeDef(TypedDict, total=False):
    LaunchTemplate: "LaunchTemplateTypeDef"


class ModifyManagedPrefixListResultTypeDef(TypedDict, total=False):
    PrefixList: "ManagedPrefixListTypeDef"


class ModifyReservedInstancesResultTypeDef(TypedDict, total=False):
    ReservedInstancesModificationId: str


class ModifySpotFleetRequestResponseTypeDef(TypedDict, total=False):
    Return: bool


class ModifyTrafficMirrorFilterNetworkServicesResultTypeDef(TypedDict, total=False):
    TrafficMirrorFilter: "TrafficMirrorFilterTypeDef"


class ModifyTrafficMirrorFilterRuleResultTypeDef(TypedDict, total=False):
    TrafficMirrorFilterRule: "TrafficMirrorFilterRuleTypeDef"


class ModifyTrafficMirrorSessionResultTypeDef(TypedDict, total=False):
    TrafficMirrorSession: "TrafficMirrorSessionTypeDef"


class ModifyTransitGatewayOptionsTypeDef(TypedDict, total=False):
    AddTransitGatewayCidrBlocks: List[str]
    RemoveTransitGatewayCidrBlocks: List[str]
    VpnEcmpSupport: VpnEcmpSupportValue
    DnsSupport: DnsSupportValue
    AutoAcceptSharedAttachments: AutoAcceptSharedAttachmentsValue
    DefaultRouteTableAssociation: DefaultRouteTableAssociationValue
    AssociationDefaultRouteTableId: str
    DefaultRouteTablePropagation: DefaultRouteTablePropagationValue
    PropagationDefaultRouteTableId: str


class ModifyTransitGatewayPrefixListReferenceResultTypeDef(TypedDict, total=False):
    TransitGatewayPrefixListReference: "TransitGatewayPrefixListReferenceTypeDef"


class ModifyTransitGatewayResultTypeDef(TypedDict, total=False):
    TransitGateway: "TransitGatewayTypeDef"


class ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef(TypedDict, total=False):
    DnsSupport: DnsSupportValue
    Ipv6Support: Ipv6SupportValue
    ApplianceModeSupport: ApplianceModeSupportValue


class ModifyTransitGatewayVpcAttachmentResultTypeDef(TypedDict, total=False):
    TransitGatewayVpcAttachment: "TransitGatewayVpcAttachmentTypeDef"


class ModifyVolumeResultTypeDef(TypedDict, total=False):
    VolumeModification: "VolumeModificationTypeDef"


class ModifyVpcEndpointConnectionNotificationResultTypeDef(TypedDict, total=False):
    ReturnValue: bool


class ModifyVpcEndpointResultTypeDef(TypedDict, total=False):
    Return: bool


class ModifyVpcEndpointServiceConfigurationResultTypeDef(TypedDict, total=False):
    Return: bool


class ModifyVpcEndpointServicePermissionsResultTypeDef(TypedDict, total=False):
    ReturnValue: bool


class ModifyVpcPeeringConnectionOptionsResultTypeDef(TypedDict, total=False):
    AccepterPeeringConnectionOptions: "PeeringConnectionOptionsTypeDef"
    RequesterPeeringConnectionOptions: "PeeringConnectionOptionsTypeDef"


class ModifyVpcTenancyResultTypeDef(TypedDict, total=False):
    ReturnValue: bool


class ModifyVpnConnectionOptionsResultTypeDef(TypedDict, total=False):
    VpnConnection: "VpnConnectionTypeDef"


class ModifyVpnConnectionResultTypeDef(TypedDict, total=False):
    VpnConnection: "VpnConnectionTypeDef"


class ModifyVpnTunnelCertificateResultTypeDef(TypedDict, total=False):
    VpnConnection: "VpnConnectionTypeDef"


class ModifyVpnTunnelOptionsResultTypeDef(TypedDict, total=False):
    VpnConnection: "VpnConnectionTypeDef"


class ModifyVpnTunnelOptionsSpecificationTypeDef(TypedDict, total=False):
    TunnelInsideCidr: str
    TunnelInsideIpv6Cidr: str
    PreSharedKey: str
    Phase1LifetimeSeconds: int
    Phase2LifetimeSeconds: int
    RekeyMarginTimeSeconds: int
    RekeyFuzzPercentage: int
    ReplayWindowSize: int
    DPDTimeoutSeconds: int
    DPDTimeoutAction: str
    Phase1EncryptionAlgorithms: List["Phase1EncryptionAlgorithmsRequestListValueTypeDef"]
    Phase2EncryptionAlgorithms: List["Phase2EncryptionAlgorithmsRequestListValueTypeDef"]
    Phase1IntegrityAlgorithms: List["Phase1IntegrityAlgorithmsRequestListValueTypeDef"]
    Phase2IntegrityAlgorithms: List["Phase2IntegrityAlgorithmsRequestListValueTypeDef"]
    Phase1DHGroupNumbers: List["Phase1DHGroupNumbersRequestListValueTypeDef"]
    Phase2DHGroupNumbers: List["Phase2DHGroupNumbersRequestListValueTypeDef"]
    IKEVersions: List["IKEVersionsRequestListValueTypeDef"]
    StartupAction: str


class MonitorInstancesResultTypeDef(TypedDict, total=False):
    InstanceMonitorings: List["InstanceMonitoringTypeDef"]


class MonitoringTypeDef(TypedDict, total=False):
    State: MonitoringState


class MoveAddressToVpcResultTypeDef(TypedDict, total=False):
    AllocationId: str
    Status: Status


class MovingAddressStatusTypeDef(TypedDict, total=False):
    MoveStatus: MoveStatus
    PublicIp: str


class NatGatewayAddressTypeDef(TypedDict, total=False):
    AllocationId: str
    NetworkInterfaceId: str
    PrivateIp: str
    PublicIp: str


class NatGatewayTypeDef(TypedDict, total=False):
    CreateTime: datetime
    DeleteTime: datetime
    FailureCode: str
    FailureMessage: str
    NatGatewayAddresses: List["NatGatewayAddressTypeDef"]
    NatGatewayId: str
    ProvisionedBandwidth: "ProvisionedBandwidthTypeDef"
    State: NatGatewayState
    SubnetId: str
    VpcId: str
    Tags: List["TagTypeDef"]


class NetworkAclAssociationTypeDef(TypedDict, total=False):
    NetworkAclAssociationId: str
    NetworkAclId: str
    SubnetId: str


NetworkAclEntryTypeDef = TypedDict(
    "NetworkAclEntryTypeDef",
    {
        "CidrBlock": str,
        "Egress": bool,
        "IcmpTypeCode": "IcmpTypeCodeTypeDef",
        "Ipv6CidrBlock": str,
        "PortRange": "PortRangeTypeDef",
        "Protocol": str,
        "RuleAction": RuleAction,
        "RuleNumber": int,
    },
    total=False,
)


class NetworkAclTypeDef(TypedDict, total=False):
    Associations: List["NetworkAclAssociationTypeDef"]
    Entries: List["NetworkAclEntryTypeDef"]
    IsDefault: bool
    NetworkAclId: str
    Tags: List["TagTypeDef"]
    VpcId: str
    OwnerId: str


class NetworkCardInfoTypeDef(TypedDict, total=False):
    NetworkCardIndex: int
    NetworkPerformance: str
    MaximumNetworkInterfaces: int


class NetworkInfoTypeDef(TypedDict, total=False):
    NetworkPerformance: str
    MaximumNetworkInterfaces: int
    MaximumNetworkCards: int
    DefaultNetworkCardIndex: int
    NetworkCards: List["NetworkCardInfoTypeDef"]
    Ipv4AddressesPerInterface: int
    Ipv6AddressesPerInterface: int
    Ipv6Supported: bool
    EnaSupport: EnaSupport
    EfaSupported: bool
    EfaInfo: "EfaInfoTypeDef"


class NetworkInsightsAnalysisTypeDef(TypedDict, total=False):
    NetworkInsightsAnalysisId: str
    NetworkInsightsAnalysisArn: str
    NetworkInsightsPathId: str
    FilterInArns: List[str]
    StartDate: datetime
    Status: AnalysisStatus
    StatusMessage: str
    NetworkPathFound: bool
    ForwardPathComponents: List["PathComponentTypeDef"]
    ReturnPathComponents: List["PathComponentTypeDef"]
    Explanations: List["ExplanationTypeDef"]
    AlternatePathHints: List["AlternatePathHintTypeDef"]
    Tags: List["TagTypeDef"]


NetworkInsightsPathTypeDef = TypedDict(
    "NetworkInsightsPathTypeDef",
    {
        "NetworkInsightsPathId": str,
        "NetworkInsightsPathArn": str,
        "CreatedDate": datetime,
        "Source": str,
        "Destination": str,
        "SourceIp": str,
        "DestinationIp": str,
        "Protocol": ProtocolType,
        "DestinationPort": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class NetworkInterfaceAssociationTypeDef(TypedDict, total=False):
    AllocationId: str
    AssociationId: str
    IpOwnerId: str
    PublicDnsName: str
    PublicIp: str
    CustomerOwnedIp: str
    CarrierIp: str


class NetworkInterfaceAttachmentChangesTypeDef(TypedDict, total=False):
    AttachmentId: str
    DeleteOnTermination: bool


class NetworkInterfaceAttachmentTypeDef(TypedDict, total=False):
    AttachTime: datetime
    AttachmentId: str
    DeleteOnTermination: bool
    DeviceIndex: int
    NetworkCardIndex: int
    InstanceId: str
    InstanceOwnerId: str
    Status: AttachmentStatus


class NetworkInterfaceIpv6AddressTypeDef(TypedDict, total=False):
    Ipv6Address: str


class NetworkInterfacePermissionStateTypeDef(TypedDict, total=False):
    State: NetworkInterfacePermissionStateCode
    StatusMessage: str


class NetworkInterfacePermissionTypeDef(TypedDict, total=False):
    NetworkInterfacePermissionId: str
    NetworkInterfaceId: str
    AwsAccountId: str
    AwsService: str
    Permission: InterfacePermissionType
    PermissionState: "NetworkInterfacePermissionStateTypeDef"


class NetworkInterfacePrivateIpAddressTypeDef(TypedDict, total=False):
    Association: "NetworkInterfaceAssociationTypeDef"
    Primary: bool
    PrivateDnsName: str
    PrivateIpAddress: str


class NetworkInterfaceTypeDef(TypedDict, total=False):
    Association: "NetworkInterfaceAssociationTypeDef"
    Attachment: "NetworkInterfaceAttachmentTypeDef"
    AvailabilityZone: str
    Description: str
    Groups: List["GroupIdentifierTypeDef"]
    InterfaceType: NetworkInterfaceType
    Ipv6Addresses: List["NetworkInterfaceIpv6AddressTypeDef"]
    MacAddress: str
    NetworkInterfaceId: str
    OutpostArn: str
    OwnerId: str
    PrivateDnsName: str
    PrivateIpAddress: str
    PrivateIpAddresses: List["NetworkInterfacePrivateIpAddressTypeDef"]
    RequesterId: str
    RequesterManaged: bool
    SourceDestCheck: bool
    Status: NetworkInterfaceStatus
    SubnetId: str
    TagSet: List["TagTypeDef"]
    VpcId: str


class NewDhcpConfigurationTypeDef(TypedDict, total=False):
    Key: str
    Values: List[str]


class OnDemandOptionsRequestTypeDef(TypedDict, total=False):
    AllocationStrategy: FleetOnDemandAllocationStrategy
    CapacityReservationOptions: "CapacityReservationOptionsRequestTypeDef"
    SingleInstanceType: bool
    SingleAvailabilityZone: bool
    MinTargetCapacity: int
    MaxTotalPrice: str


class OnDemandOptionsTypeDef(TypedDict, total=False):
    AllocationStrategy: FleetOnDemandAllocationStrategy
    CapacityReservationOptions: "CapacityReservationOptionsTypeDef"
    SingleInstanceType: bool
    SingleAvailabilityZone: bool
    MinTargetCapacity: int
    MaxTotalPrice: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PathComponentTypeDef(TypedDict, total=False):
    SequenceNumber: int
    AclRule: "AnalysisAclRuleTypeDef"
    Component: "AnalysisComponentTypeDef"
    DestinationVpc: "AnalysisComponentTypeDef"
    OutboundHeader: "AnalysisPacketHeaderTypeDef"
    InboundHeader: "AnalysisPacketHeaderTypeDef"
    RouteTableRoute: "AnalysisRouteTableRouteTypeDef"
    SecurityGroupRule: "AnalysisSecurityGroupRuleTypeDef"
    SourceVpc: "AnalysisComponentTypeDef"
    Subnet: "AnalysisComponentTypeDef"
    Vpc: "AnalysisComponentTypeDef"


class PciIdTypeDef(TypedDict, total=False):
    DeviceId: str
    VendorId: str
    SubsystemId: str
    SubsystemVendorId: str


class PeeringAttachmentStatusTypeDef(TypedDict, total=False):
    Code: str
    Message: str


class PeeringConnectionOptionsRequestTypeDef(TypedDict, total=False):
    AllowDnsResolutionFromRemoteVpc: bool
    AllowEgressFromLocalClassicLinkToRemoteVpc: bool
    AllowEgressFromLocalVpcToRemoteClassicLink: bool


class PeeringConnectionOptionsTypeDef(TypedDict, total=False):
    AllowDnsResolutionFromRemoteVpc: bool
    AllowEgressFromLocalClassicLinkToRemoteVpc: bool
    AllowEgressFromLocalVpcToRemoteClassicLink: bool


class PeeringTgwInfoTypeDef(TypedDict, total=False):
    TransitGatewayId: str
    OwnerId: str
    Region: str


class Phase1DHGroupNumbersListValueTypeDef(TypedDict, total=False):
    Value: int


class Phase1DHGroupNumbersRequestListValueTypeDef(TypedDict, total=False):
    Value: int


class Phase1EncryptionAlgorithmsListValueTypeDef(TypedDict, total=False):
    Value: str


class Phase1EncryptionAlgorithmsRequestListValueTypeDef(TypedDict, total=False):
    Value: str


class Phase1IntegrityAlgorithmsListValueTypeDef(TypedDict, total=False):
    Value: str


class Phase1IntegrityAlgorithmsRequestListValueTypeDef(TypedDict, total=False):
    Value: str


class Phase2DHGroupNumbersListValueTypeDef(TypedDict, total=False):
    Value: int


class Phase2DHGroupNumbersRequestListValueTypeDef(TypedDict, total=False):
    Value: int


class Phase2EncryptionAlgorithmsListValueTypeDef(TypedDict, total=False):
    Value: str


class Phase2EncryptionAlgorithmsRequestListValueTypeDef(TypedDict, total=False):
    Value: str


class Phase2IntegrityAlgorithmsListValueTypeDef(TypedDict, total=False):
    Value: str


class Phase2IntegrityAlgorithmsRequestListValueTypeDef(TypedDict, total=False):
    Value: str


class PlacementGroupInfoTypeDef(TypedDict, total=False):
    SupportedStrategies: List[PlacementGroupStrategy]


class PlacementGroupTypeDef(TypedDict, total=False):
    GroupName: str
    State: PlacementGroupState
    Strategy: PlacementStrategy
    PartitionCount: int
    GroupId: str
    Tags: List["TagTypeDef"]


class PlacementResponseTypeDef(TypedDict, total=False):
    GroupName: str


class PlacementTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    Affinity: str
    GroupName: str
    PartitionNumber: int
    HostId: str
    Tenancy: Tenancy
    SpreadDomain: str
    HostResourceGroupArn: str


class PoolCidrBlockTypeDef(TypedDict, total=False):
    Cidr: str


class PortRangeTypeDef(TypedDict, total=False):
    From: int
    To: int


class PrefixListAssociationTypeDef(TypedDict, total=False):
    ResourceId: str
    ResourceOwner: str


class PrefixListEntryTypeDef(TypedDict, total=False):
    Cidr: str
    Description: str


class PrefixListIdTypeDef(TypedDict, total=False):
    Description: str
    PrefixListId: str


class PrefixListTypeDef(TypedDict, total=False):
    Cidrs: List[str]
    PrefixListId: str
    PrefixListName: str


class PriceScheduleSpecificationTypeDef(TypedDict, total=False):
    CurrencyCode: Literal["USD"]
    Price: float
    Term: int


class PriceScheduleTypeDef(TypedDict, total=False):
    Active: bool
    CurrencyCode: Literal["USD"]
    Price: float
    Term: int


class PricingDetailTypeDef(TypedDict, total=False):
    Count: int
    Price: float


class PrincipalIdFormatTypeDef(TypedDict, total=False):
    Arn: str
    Statuses: List["IdFormatTypeDef"]


class PrivateDnsDetailsTypeDef(TypedDict, total=False):
    PrivateDnsName: str


PrivateDnsNameConfigurationTypeDef = TypedDict(
    "PrivateDnsNameConfigurationTypeDef",
    {"State": DnsNameState, "Type": str, "Value": str, "Name": str},
    total=False,
)


class PrivateIpAddressSpecificationTypeDef(TypedDict, total=False):
    Primary: bool
    PrivateIpAddress: str


class ProcessorInfoTypeDef(TypedDict, total=False):
    SupportedArchitectures: List[ArchitectureType]
    SustainedClockSpeedInGhz: float


class ProductCodeTypeDef(TypedDict, total=False):
    ProductCodeId: str
    ProductCodeType: ProductCodeValues


class PropagatingVgwTypeDef(TypedDict, total=False):
    GatewayId: str


class ProvisionByoipCidrResultTypeDef(TypedDict, total=False):
    ByoipCidr: "ByoipCidrTypeDef"


class ProvisionedBandwidthTypeDef(TypedDict, total=False):
    ProvisionTime: datetime
    Provisioned: str
    RequestTime: datetime
    Requested: str
    Status: str


class PtrUpdateStatusTypeDef(TypedDict, total=False):
    Value: str
    Status: str
    Reason: str


class PublicIpv4PoolRangeTypeDef(TypedDict, total=False):
    FirstAddress: str
    LastAddress: str
    AddressCount: int
    AvailableAddressCount: int


class PublicIpv4PoolTypeDef(TypedDict, total=False):
    PoolId: str
    Description: str
    PoolAddressRanges: List["PublicIpv4PoolRangeTypeDef"]
    TotalAddressCount: int
    TotalAvailableAddressCount: int
    NetworkBorderGroup: str
    Tags: List["TagTypeDef"]


class PurchaseHostReservationResultTypeDef(TypedDict, total=False):
    ClientToken: str
    CurrencyCode: Literal["USD"]
    Purchase: List["PurchaseTypeDef"]
    TotalHourlyPrice: str
    TotalUpfrontPrice: str


class PurchaseRequestTypeDef(TypedDict):
    InstanceCount: int
    PurchaseToken: str


class PurchaseReservedInstancesOfferingResultTypeDef(TypedDict, total=False):
    ReservedInstancesId: str


class PurchaseScheduledInstancesResultTypeDef(TypedDict, total=False):
    ScheduledInstanceSet: List["ScheduledInstanceTypeDef"]


class PurchaseTypeDef(TypedDict, total=False):
    CurrencyCode: Literal["USD"]
    Duration: int
    HostIdSet: List[str]
    HostReservationId: str
    HourlyPrice: str
    InstanceFamily: str
    PaymentOption: PaymentOption
    UpfrontPrice: str


class RecurringChargeTypeDef(TypedDict, total=False):
    Amount: float
    Frequency: Literal["Hourly"]


class RegionTypeDef(TypedDict, total=False):
    Endpoint: str
    RegionName: str
    OptInStatus: str


class RegisterImageResultTypeDef(TypedDict, total=False):
    ImageId: str


class RegisterInstanceEventNotificationAttributesResultTypeDef(TypedDict, total=False):
    InstanceTagAttribute: "InstanceTagNotificationAttributeTypeDef"


class RegisterInstanceTagAttributeRequestTypeDef(TypedDict, total=False):
    IncludeAllTagsOfInstance: bool
    InstanceTagKeys: List[str]


class RegisterTransitGatewayMulticastGroupMembersResultTypeDef(TypedDict, total=False):
    RegisteredMulticastGroupMembers: "TransitGatewayMulticastRegisteredGroupMembersTypeDef"


class RegisterTransitGatewayMulticastGroupSourcesResultTypeDef(TypedDict, total=False):
    RegisteredMulticastGroupSources: "TransitGatewayMulticastRegisteredGroupSourcesTypeDef"


class RejectTransitGatewayMulticastDomainAssociationsResultTypeDef(TypedDict, total=False):
    Associations: "TransitGatewayMulticastDomainAssociationsTypeDef"


class RejectTransitGatewayPeeringAttachmentResultTypeDef(TypedDict, total=False):
    TransitGatewayPeeringAttachment: "TransitGatewayPeeringAttachmentTypeDef"


class RejectTransitGatewayVpcAttachmentResultTypeDef(TypedDict, total=False):
    TransitGatewayVpcAttachment: "TransitGatewayVpcAttachmentTypeDef"


class RejectVpcEndpointConnectionsResultTypeDef(TypedDict, total=False):
    Unsuccessful: List["UnsuccessfulItemTypeDef"]


class RejectVpcPeeringConnectionResultTypeDef(TypedDict, total=False):
    Return: bool


class ReleaseHostsResultTypeDef(TypedDict, total=False):
    Successful: List[str]
    Unsuccessful: List["UnsuccessfulItemTypeDef"]


class RemovePrefixListEntryTypeDef(TypedDict):
    Cidr: str


class ReplaceIamInstanceProfileAssociationResultTypeDef(TypedDict, total=False):
    IamInstanceProfileAssociation: "IamInstanceProfileAssociationTypeDef"


class ReplaceNetworkAclAssociationResultTypeDef(TypedDict, total=False):
    NewAssociationId: str


class ReplaceRootVolumeTaskTypeDef(TypedDict, total=False):
    ReplaceRootVolumeTaskId: str
    InstanceId: str
    TaskState: ReplaceRootVolumeTaskState
    StartTime: str
    CompleteTime: str
    Tags: List["TagTypeDef"]


class ReplaceRouteTableAssociationResultTypeDef(TypedDict, total=False):
    NewAssociationId: str
    AssociationState: "RouteTableAssociationStateTypeDef"


class ReplaceTransitGatewayRouteResultTypeDef(TypedDict, total=False):
    Route: "TransitGatewayRouteTypeDef"


class RequestLaunchTemplateDataTypeDef(TypedDict, total=False):
    KernelId: str
    EbsOptimized: bool
    IamInstanceProfile: "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef"
    BlockDeviceMappings: List["LaunchTemplateBlockDeviceMappingRequestTypeDef"]
    NetworkInterfaces: List["LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef"]
    ImageId: str
    InstanceType: InstanceType
    KeyName: str
    Monitoring: "LaunchTemplatesMonitoringRequestTypeDef"
    Placement: "LaunchTemplatePlacementRequestTypeDef"
    RamDiskId: str
    DisableApiTermination: bool
    InstanceInitiatedShutdownBehavior: ShutdownBehavior
    UserData: str
    TagSpecifications: List["LaunchTemplateTagSpecificationRequestTypeDef"]
    ElasticGpuSpecifications: List["ElasticGpuSpecificationTypeDef"]
    ElasticInferenceAccelerators: List["LaunchTemplateElasticInferenceAcceleratorTypeDef"]
    SecurityGroupIds: List[str]
    SecurityGroups: List[str]
    InstanceMarketOptions: "LaunchTemplateInstanceMarketOptionsRequestTypeDef"
    CreditSpecification: "CreditSpecificationRequestTypeDef"
    CpuOptions: "LaunchTemplateCpuOptionsRequestTypeDef"
    CapacityReservationSpecification: "LaunchTemplateCapacityReservationSpecificationRequestTypeDef"
    LicenseSpecifications: List["LaunchTemplateLicenseConfigurationRequestTypeDef"]
    HibernationOptions: "LaunchTemplateHibernationOptionsRequestTypeDef"
    MetadataOptions: "LaunchTemplateInstanceMetadataOptionsRequestTypeDef"
    EnclaveOptions: "LaunchTemplateEnclaveOptionsRequestTypeDef"


class RequestSpotFleetResponseTypeDef(TypedDict, total=False):
    SpotFleetRequestId: str


class RequestSpotInstancesResultTypeDef(TypedDict, total=False):
    SpotInstanceRequests: List["SpotInstanceRequestTypeDef"]


class RequestSpotLaunchSpecificationTypeDef(TypedDict, total=False):
    SecurityGroupIds: List[str]
    SecurityGroups: List[str]
    AddressingType: str
    BlockDeviceMappings: List["BlockDeviceMappingTypeDef"]
    EbsOptimized: bool
    IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef"
    ImageId: str
    InstanceType: InstanceType
    KernelId: str
    KeyName: str
    Monitoring: "RunInstancesMonitoringEnabledTypeDef"
    NetworkInterfaces: List["InstanceNetworkInterfaceSpecificationTypeDef"]
    Placement: "SpotPlacementTypeDef"
    RamdiskId: str
    SubnetId: str
    UserData: str


class ReservationTypeDef(TypedDict, total=False):
    Groups: List["GroupIdentifierTypeDef"]
    Instances: List["InstanceTypeDef"]
    OwnerId: str
    RequesterId: str
    ReservationId: str


class ReservationValueTypeDef(TypedDict, total=False):
    HourlyPrice: str
    RemainingTotalValue: str
    RemainingUpfrontValue: str


class ReservedInstanceLimitPriceTypeDef(TypedDict, total=False):
    Amount: float
    CurrencyCode: Literal["USD"]


class ReservedInstanceReservationValueTypeDef(TypedDict, total=False):
    ReservationValue: "ReservationValueTypeDef"
    ReservedInstanceId: str


class ReservedInstancesConfigurationTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    InstanceCount: int
    InstanceType: InstanceType
    Platform: str
    Scope: scope


class ReservedInstancesIdTypeDef(TypedDict, total=False):
    ReservedInstancesId: str


class ReservedInstancesListingTypeDef(TypedDict, total=False):
    ClientToken: str
    CreateDate: datetime
    InstanceCounts: List["InstanceCountTypeDef"]
    PriceSchedules: List["PriceScheduleTypeDef"]
    ReservedInstancesId: str
    ReservedInstancesListingId: str
    Status: ListingStatus
    StatusMessage: str
    Tags: List["TagTypeDef"]
    UpdateDate: datetime


class ReservedInstancesModificationResultTypeDef(TypedDict, total=False):
    ReservedInstancesId: str
    TargetConfiguration: "ReservedInstancesConfigurationTypeDef"


class ReservedInstancesModificationTypeDef(TypedDict, total=False):
    ClientToken: str
    CreateDate: datetime
    EffectiveDate: datetime
    ModificationResults: List["ReservedInstancesModificationResultTypeDef"]
    ReservedInstancesIds: List["ReservedInstancesIdTypeDef"]
    ReservedInstancesModificationId: str
    Status: str
    StatusMessage: str
    UpdateDate: datetime


class ReservedInstancesOfferingTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    Duration: int
    FixedPrice: float
    InstanceType: InstanceType
    ProductDescription: RIProductDescription
    ReservedInstancesOfferingId: str
    UsagePrice: float
    CurrencyCode: Literal["USD"]
    InstanceTenancy: Tenancy
    Marketplace: bool
    OfferingClass: OfferingClassType
    OfferingType: OfferingTypeValues
    PricingDetails: List["PricingDetailTypeDef"]
    RecurringCharges: List["RecurringChargeTypeDef"]
    Scope: scope


class ReservedInstancesTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    Duration: int
    End: datetime
    FixedPrice: float
    InstanceCount: int
    InstanceType: InstanceType
    ProductDescription: RIProductDescription
    ReservedInstancesId: str
    Start: datetime
    State: ReservedInstanceState
    UsagePrice: float
    CurrencyCode: Literal["USD"]
    InstanceTenancy: Tenancy
    OfferingClass: OfferingClassType
    OfferingType: OfferingTypeValues
    RecurringCharges: List["RecurringChargeTypeDef"]
    Scope: scope
    Tags: List["TagTypeDef"]


class ResetAddressAttributeResultTypeDef(TypedDict, total=False):
    Address: "AddressAttributeTypeDef"


class ResetEbsDefaultKmsKeyIdResultTypeDef(TypedDict, total=False):
    KmsKeyId: str


class ResetFpgaImageAttributeResultTypeDef(TypedDict, total=False):
    Return: bool


class ResponseErrorTypeDef(TypedDict, total=False):
    Code: LaunchTemplateErrorCode
    Message: str


class ResponseLaunchTemplateDataTypeDef(TypedDict, total=False):
    KernelId: str
    EbsOptimized: bool
    IamInstanceProfile: "LaunchTemplateIamInstanceProfileSpecificationTypeDef"
    BlockDeviceMappings: List["LaunchTemplateBlockDeviceMappingTypeDef"]
    NetworkInterfaces: List["LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef"]
    ImageId: str
    InstanceType: InstanceType
    KeyName: str
    Monitoring: "LaunchTemplatesMonitoringTypeDef"
    Placement: "LaunchTemplatePlacementTypeDef"
    RamDiskId: str
    DisableApiTermination: bool
    InstanceInitiatedShutdownBehavior: ShutdownBehavior
    UserData: str
    TagSpecifications: List["LaunchTemplateTagSpecificationTypeDef"]
    ElasticGpuSpecifications: List["ElasticGpuSpecificationResponseTypeDef"]
    ElasticInferenceAccelerators: List["LaunchTemplateElasticInferenceAcceleratorResponseTypeDef"]
    SecurityGroupIds: List[str]
    SecurityGroups: List[str]
    InstanceMarketOptions: "LaunchTemplateInstanceMarketOptionsTypeDef"
    CreditSpecification: "CreditSpecificationTypeDef"
    CpuOptions: "LaunchTemplateCpuOptionsTypeDef"
    CapacityReservationSpecification: "LaunchTemplateCapacityReservationSpecificationResponseTypeDef"
    LicenseSpecifications: List["LaunchTemplateLicenseConfigurationTypeDef"]
    HibernationOptions: "LaunchTemplateHibernationOptionsTypeDef"
    MetadataOptions: "LaunchTemplateInstanceMetadataOptionsTypeDef"
    EnclaveOptions: "LaunchTemplateEnclaveOptionsTypeDef"


class RestoreAddressToClassicResultTypeDef(TypedDict, total=False):
    PublicIp: str
    Status: Status


class RestoreManagedPrefixListVersionResultTypeDef(TypedDict, total=False):
    PrefixList: "ManagedPrefixListTypeDef"


class RevokeClientVpnIngressResultTypeDef(TypedDict, total=False):
    Status: "ClientVpnAuthorizationRuleStatusTypeDef"


class RevokeSecurityGroupEgressResultTypeDef(TypedDict, total=False):
    Return: bool
    UnknownIpPermissions: List["IpPermissionTypeDef"]


class RevokeSecurityGroupIngressResultTypeDef(TypedDict, total=False):
    Return: bool
    UnknownIpPermissions: List["IpPermissionTypeDef"]


class RouteTableAssociationStateTypeDef(TypedDict, total=False):
    State: RouteTableAssociationStateCode
    StatusMessage: str


class RouteTableAssociationTypeDef(TypedDict, total=False):
    Main: bool
    RouteTableAssociationId: str
    RouteTableId: str
    SubnetId: str
    GatewayId: str
    AssociationState: "RouteTableAssociationStateTypeDef"


class RouteTableTypeDef(TypedDict, total=False):
    Associations: List["RouteTableAssociationTypeDef"]
    PropagatingVgws: List["PropagatingVgwTypeDef"]
    RouteTableId: str
    Routes: List["RouteTypeDef"]
    Tags: List["TagTypeDef"]
    VpcId: str
    OwnerId: str


class RouteTypeDef(TypedDict, total=False):
    DestinationCidrBlock: str
    DestinationIpv6CidrBlock: str
    DestinationPrefixListId: str
    EgressOnlyInternetGatewayId: str
    GatewayId: str
    InstanceId: str
    InstanceOwnerId: str
    NatGatewayId: str
    TransitGatewayId: str
    LocalGatewayId: str
    CarrierGatewayId: str
    NetworkInterfaceId: str
    Origin: RouteOrigin
    State: RouteState
    VpcPeeringConnectionId: str


class RunInstancesMonitoringEnabledTypeDef(TypedDict):
    Enabled: bool


class RunScheduledInstancesResultTypeDef(TypedDict, total=False):
    InstanceIdSet: List[str]


class S3ObjectTagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class S3StorageTypeDef(TypedDict, total=False):
    AWSAccessKeyId: str
    Bucket: str
    Prefix: str
    UploadPolicy: Union[bytes, IO[bytes]]
    UploadPolicySignature: str


class ScheduledInstanceAvailabilityTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    AvailableInstanceCount: int
    FirstSlotStartTime: datetime
    HourlyPrice: str
    InstanceType: str
    MaxTermDurationInDays: int
    MinTermDurationInDays: int
    NetworkPlatform: str
    Platform: str
    PurchaseToken: str
    Recurrence: "ScheduledInstanceRecurrenceTypeDef"
    SlotDurationInHours: int
    TotalScheduledInstanceHours: int


class ScheduledInstanceRecurrenceRequestTypeDef(TypedDict, total=False):
    Frequency: str
    Interval: int
    OccurrenceDays: List[int]
    OccurrenceRelativeToEnd: bool
    OccurrenceUnit: str


class ScheduledInstanceRecurrenceTypeDef(TypedDict, total=False):
    Frequency: str
    Interval: int
    OccurrenceDaySet: List[int]
    OccurrenceRelativeToEnd: bool
    OccurrenceUnit: str


class ScheduledInstanceTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    CreateDate: datetime
    HourlyPrice: str
    InstanceCount: int
    InstanceType: str
    NetworkPlatform: str
    NextSlotStartTime: datetime
    Platform: str
    PreviousSlotEndTime: datetime
    Recurrence: "ScheduledInstanceRecurrenceTypeDef"
    ScheduledInstanceId: str
    SlotDurationInHours: int
    TermEndDate: datetime
    TermStartDate: datetime
    TotalScheduledInstanceHours: int


class ScheduledInstancesBlockDeviceMappingTypeDef(TypedDict, total=False):
    DeviceName: str
    Ebs: "ScheduledInstancesEbsTypeDef"
    NoDevice: str
    VirtualName: str


class ScheduledInstancesEbsTypeDef(TypedDict, total=False):
    DeleteOnTermination: bool
    Encrypted: bool
    Iops: int
    SnapshotId: str
    VolumeSize: int
    VolumeType: str


class ScheduledInstancesIamInstanceProfileTypeDef(TypedDict, total=False):
    Arn: str
    Name: str


class ScheduledInstancesIpv6AddressTypeDef(TypedDict, total=False):
    Ipv6Address: str


class _RequiredScheduledInstancesLaunchSpecificationTypeDef(TypedDict):
    ImageId: str


class ScheduledInstancesLaunchSpecificationTypeDef(
    _RequiredScheduledInstancesLaunchSpecificationTypeDef, total=False
):
    BlockDeviceMappings: List["ScheduledInstancesBlockDeviceMappingTypeDef"]
    EbsOptimized: bool
    IamInstanceProfile: "ScheduledInstancesIamInstanceProfileTypeDef"
    InstanceType: str
    KernelId: str
    KeyName: str
    Monitoring: "ScheduledInstancesMonitoringTypeDef"
    NetworkInterfaces: List["ScheduledInstancesNetworkInterfaceTypeDef"]
    Placement: "ScheduledInstancesPlacementTypeDef"
    RamdiskId: str
    SecurityGroupIds: List[str]
    SubnetId: str
    UserData: str


class ScheduledInstancesMonitoringTypeDef(TypedDict, total=False):
    Enabled: bool


class ScheduledInstancesNetworkInterfaceTypeDef(TypedDict, total=False):
    AssociatePublicIpAddress: bool
    DeleteOnTermination: bool
    Description: str
    DeviceIndex: int
    Groups: List[str]
    Ipv6AddressCount: int
    Ipv6Addresses: List["ScheduledInstancesIpv6AddressTypeDef"]
    NetworkInterfaceId: str
    PrivateIpAddress: str
    PrivateIpAddressConfigs: List["ScheduledInstancesPrivateIpAddressConfigTypeDef"]
    SecondaryPrivateIpAddressCount: int
    SubnetId: str


class ScheduledInstancesPlacementTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    GroupName: str


class ScheduledInstancesPrivateIpAddressConfigTypeDef(TypedDict, total=False):
    Primary: bool
    PrivateIpAddress: str


class SearchLocalGatewayRoutesResultTypeDef(TypedDict, total=False):
    Routes: List["LocalGatewayRouteTypeDef"]
    NextToken: str


class SearchTransitGatewayMulticastGroupsResultTypeDef(TypedDict, total=False):
    MulticastGroups: List["TransitGatewayMulticastGroupTypeDef"]
    NextToken: str


class SearchTransitGatewayRoutesResultTypeDef(TypedDict, total=False):
    Routes: List["TransitGatewayRouteTypeDef"]
    AdditionalRoutesAvailable: bool


class SecurityGroupIdentifierTypeDef(TypedDict, total=False):
    GroupId: str
    GroupName: str


class SecurityGroupReferenceTypeDef(TypedDict, total=False):
    GroupId: str
    ReferencingVpcId: str
    VpcPeeringConnectionId: str


class SecurityGroupTypeDef(TypedDict, total=False):
    Description: str
    GroupName: str
    IpPermissions: List["IpPermissionTypeDef"]
    OwnerId: str
    GroupId: str
    IpPermissionsEgress: List["IpPermissionTypeDef"]
    Tags: List["TagTypeDef"]
    VpcId: str


class ServiceConfigurationTypeDef(TypedDict, total=False):
    ServiceType: List["ServiceTypeDetailTypeDef"]
    ServiceId: str
    ServiceName: str
    ServiceState: ServiceState
    AvailabilityZones: List[str]
    AcceptanceRequired: bool
    ManagesVpcEndpoints: bool
    NetworkLoadBalancerArns: List[str]
    GatewayLoadBalancerArns: List[str]
    BaseEndpointDnsNames: List[str]
    PrivateDnsName: str
    PrivateDnsNameConfiguration: "PrivateDnsNameConfigurationTypeDef"
    Tags: List["TagTypeDef"]


class ServiceDetailTypeDef(TypedDict, total=False):
    ServiceName: str
    ServiceId: str
    ServiceType: List["ServiceTypeDetailTypeDef"]
    AvailabilityZones: List[str]
    Owner: str
    BaseEndpointDnsNames: List[str]
    PrivateDnsName: str
    PrivateDnsNames: List["PrivateDnsDetailsTypeDef"]
    VpcEndpointPolicySupported: bool
    AcceptanceRequired: bool
    ManagesVpcEndpoints: bool
    Tags: List["TagTypeDef"]
    PrivateDnsNameVerificationState: DnsNameState


class ServiceTypeDetailTypeDef(TypedDict, total=False):
    ServiceType: ServiceType


class SlotDateTimeRangeRequestTypeDef(TypedDict):
    EarliestTime: datetime
    LatestTime: datetime


class SlotStartTimeRangeRequestTypeDef(TypedDict, total=False):
    EarliestTime: datetime
    LatestTime: datetime


class SnapshotDetailTypeDef(TypedDict, total=False):
    Description: str
    DeviceName: str
    DiskImageSize: float
    Format: str
    Progress: str
    SnapshotId: str
    Status: str
    StatusMessage: str
    Url: str
    UserBucket: "UserBucketDetailsTypeDef"


class SnapshotDiskContainerTypeDef(TypedDict, total=False):
    Description: str
    Format: str
    Url: str
    UserBucket: "UserBucketTypeDef"


class SnapshotInfoTypeDef(TypedDict, total=False):
    Description: str
    Tags: List["TagTypeDef"]
    Encrypted: bool
    VolumeId: str
    State: SnapshotState
    VolumeSize: int
    StartTime: datetime
    Progress: str
    OwnerId: str
    SnapshotId: str
    OutpostArn: str


class SnapshotTaskDetailTypeDef(TypedDict, total=False):
    Description: str
    DiskImageSize: float
    Encrypted: bool
    Format: str
    KmsKeyId: str
    Progress: str
    SnapshotId: str
    Status: str
    StatusMessage: str
    Url: str
    UserBucket: "UserBucketDetailsTypeDef"


class SnapshotTypeDef(TypedDict, total=False):
    DataEncryptionKeyId: str
    Description: str
    Encrypted: bool
    KmsKeyId: str
    OwnerId: str
    Progress: str
    SnapshotId: str
    StartTime: datetime
    State: SnapshotState
    StateMessage: str
    VolumeId: str
    VolumeSize: int
    OwnerAlias: str
    OutpostArn: str
    Tags: List["TagTypeDef"]


class SpotCapacityRebalanceTypeDef(TypedDict, total=False):
    ReplacementStrategy: Literal["launch"]


class SpotDatafeedSubscriptionTypeDef(TypedDict, total=False):
    Bucket: str
    Fault: "SpotInstanceStateFaultTypeDef"
    OwnerId: str
    Prefix: str
    State: DatafeedSubscriptionState


class SpotFleetLaunchSpecificationTypeDef(TypedDict, total=False):
    SecurityGroups: List["GroupIdentifierTypeDef"]
    AddressingType: str
    BlockDeviceMappings: List["BlockDeviceMappingTypeDef"]
    EbsOptimized: bool
    IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef"
    ImageId: str
    InstanceType: InstanceType
    KernelId: str
    KeyName: str
    Monitoring: "SpotFleetMonitoringTypeDef"
    NetworkInterfaces: List["InstanceNetworkInterfaceSpecificationTypeDef"]
    Placement: "SpotPlacementTypeDef"
    RamdiskId: str
    SpotPrice: str
    SubnetId: str
    UserData: str
    WeightedCapacity: float
    TagSpecifications: List["SpotFleetTagSpecificationTypeDef"]


class SpotFleetMonitoringTypeDef(TypedDict, total=False):
    Enabled: bool


_RequiredSpotFleetRequestConfigDataTypeDef = TypedDict(
    "_RequiredSpotFleetRequestConfigDataTypeDef", {"IamFleetRole": str, "TargetCapacity": int}
)
_OptionalSpotFleetRequestConfigDataTypeDef = TypedDict(
    "_OptionalSpotFleetRequestConfigDataTypeDef",
    {
        "AllocationStrategy": AllocationStrategy,
        "OnDemandAllocationStrategy": OnDemandAllocationStrategy,
        "SpotMaintenanceStrategies": "SpotMaintenanceStrategiesTypeDef",
        "ClientToken": str,
        "ExcessCapacityTerminationPolicy": ExcessCapacityTerminationPolicy,
        "FulfilledCapacity": float,
        "OnDemandFulfilledCapacity": float,
        "LaunchSpecifications": List["SpotFleetLaunchSpecificationTypeDef"],
        "LaunchTemplateConfigs": List["LaunchTemplateConfigTypeDef"],
        "SpotPrice": str,
        "OnDemandTargetCapacity": int,
        "OnDemandMaxTotalPrice": str,
        "SpotMaxTotalPrice": str,
        "TerminateInstancesWithExpiration": bool,
        "Type": FleetType,
        "ValidFrom": datetime,
        "ValidUntil": datetime,
        "ReplaceUnhealthyInstances": bool,
        "InstanceInterruptionBehavior": InstanceInterruptionBehavior,
        "LoadBalancersConfig": "LoadBalancersConfigTypeDef",
        "InstancePoolsToUseCount": int,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)


class SpotFleetRequestConfigDataTypeDef(
    _RequiredSpotFleetRequestConfigDataTypeDef, _OptionalSpotFleetRequestConfigDataTypeDef
):
    pass


class SpotFleetRequestConfigTypeDef(TypedDict, total=False):
    ActivityStatus: ActivityStatus
    CreateTime: datetime
    SpotFleetRequestConfig: "SpotFleetRequestConfigDataTypeDef"
    SpotFleetRequestId: str
    SpotFleetRequestState: BatchState
    Tags: List["TagTypeDef"]


class SpotFleetTagSpecificationTypeDef(TypedDict, total=False):
    ResourceType: ResourceType
    Tags: List["TagTypeDef"]


SpotInstanceRequestTypeDef = TypedDict(
    "SpotInstanceRequestTypeDef",
    {
        "ActualBlockHourlyPrice": str,
        "AvailabilityZoneGroup": str,
        "BlockDurationMinutes": int,
        "CreateTime": datetime,
        "Fault": "SpotInstanceStateFaultTypeDef",
        "InstanceId": str,
        "LaunchGroup": str,
        "LaunchSpecification": "LaunchSpecificationTypeDef",
        "LaunchedAvailabilityZone": str,
        "ProductDescription": RIProductDescription,
        "SpotInstanceRequestId": str,
        "SpotPrice": str,
        "State": SpotInstanceState,
        "Status": "SpotInstanceStatusTypeDef",
        "Tags": List["TagTypeDef"],
        "Type": SpotInstanceType,
        "ValidFrom": datetime,
        "ValidUntil": datetime,
        "InstanceInterruptionBehavior": InstanceInterruptionBehavior,
    },
    total=False,
)


class SpotInstanceStateFaultTypeDef(TypedDict, total=False):
    Code: str
    Message: str


class SpotInstanceStatusTypeDef(TypedDict, total=False):
    Code: str
    Message: str
    UpdateTime: datetime


class SpotMaintenanceStrategiesTypeDef(TypedDict, total=False):
    CapacityRebalance: "SpotCapacityRebalanceTypeDef"


class SpotMarketOptionsTypeDef(TypedDict, total=False):
    MaxPrice: str
    SpotInstanceType: SpotInstanceType
    BlockDurationMinutes: int
    ValidUntil: datetime
    InstanceInterruptionBehavior: InstanceInterruptionBehavior


class SpotOptionsRequestTypeDef(TypedDict, total=False):
    AllocationStrategy: SpotAllocationStrategy
    MaintenanceStrategies: "FleetSpotMaintenanceStrategiesRequestTypeDef"
    InstanceInterruptionBehavior: SpotInstanceInterruptionBehavior
    InstancePoolsToUseCount: int
    SingleInstanceType: bool
    SingleAvailabilityZone: bool
    MinTargetCapacity: int
    MaxTotalPrice: str


class SpotOptionsTypeDef(TypedDict, total=False):
    AllocationStrategy: SpotAllocationStrategy
    MaintenanceStrategies: "FleetSpotMaintenanceStrategiesTypeDef"
    InstanceInterruptionBehavior: SpotInstanceInterruptionBehavior
    InstancePoolsToUseCount: int
    SingleInstanceType: bool
    SingleAvailabilityZone: bool
    MinTargetCapacity: int
    MaxTotalPrice: str


class SpotPlacementTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    GroupName: str
    Tenancy: Tenancy


class SpotPriceTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    InstanceType: InstanceType
    ProductDescription: RIProductDescription
    SpotPrice: str
    Timestamp: datetime


class StaleIpPermissionTypeDef(TypedDict, total=False):
    FromPort: int
    IpProtocol: str
    IpRanges: List[str]
    PrefixListIds: List[str]
    ToPort: int
    UserIdGroupPairs: List["UserIdGroupPairTypeDef"]


class StaleSecurityGroupTypeDef(TypedDict, total=False):
    Description: str
    GroupId: str
    GroupName: str
    StaleIpPermissions: List["StaleIpPermissionTypeDef"]
    StaleIpPermissionsEgress: List["StaleIpPermissionTypeDef"]
    VpcId: str


class StartInstancesResultTypeDef(TypedDict, total=False):
    StartingInstances: List["InstanceStateChangeTypeDef"]


class StartNetworkInsightsAnalysisResultTypeDef(TypedDict, total=False):
    NetworkInsightsAnalysis: "NetworkInsightsAnalysisTypeDef"


class StartVpcEndpointServicePrivateDnsVerificationResultTypeDef(TypedDict, total=False):
    ReturnValue: bool


class StateReasonTypeDef(TypedDict, total=False):
    Code: str
    Message: str


class StopInstancesResultTypeDef(TypedDict, total=False):
    StoppingInstances: List["InstanceStateChangeTypeDef"]


class StorageLocationTypeDef(TypedDict, total=False):
    Bucket: str
    Key: str


class StorageTypeDef(TypedDict, total=False):
    S3: "S3StorageTypeDef"


class StoreImageTaskResultTypeDef(TypedDict, total=False):
    AmiId: str
    TaskStartTime: datetime
    Bucket: str
    S3objectKey: str
    ProgressPercentage: int
    StoreTaskState: str
    StoreTaskFailureReason: str


class SubnetAssociationTypeDef(TypedDict, total=False):
    SubnetId: str
    State: TransitGatewayMulitcastDomainAssociationState


class SubnetCidrBlockStateTypeDef(TypedDict, total=False):
    State: SubnetCidrBlockStateCode
    StatusMessage: str


class SubnetIpv6CidrBlockAssociationTypeDef(TypedDict, total=False):
    AssociationId: str
    Ipv6CidrBlock: str
    Ipv6CidrBlockState: "SubnetCidrBlockStateTypeDef"


class SubnetTypeDef(TypedDict, total=False):
    AvailabilityZone: str
    AvailabilityZoneId: str
    AvailableIpAddressCount: int
    CidrBlock: str
    DefaultForAz: bool
    MapPublicIpOnLaunch: bool
    MapCustomerOwnedIpOnLaunch: bool
    CustomerOwnedIpv4Pool: str
    State: SubnetState
    SubnetId: str
    VpcId: str
    OwnerId: str
    AssignIpv6AddressOnCreation: bool
    Ipv6CidrBlockAssociationSet: List["SubnetIpv6CidrBlockAssociationTypeDef"]
    Tags: List["TagTypeDef"]
    SubnetArn: str
    OutpostArn: str


class SuccessfulInstanceCreditSpecificationItemTypeDef(TypedDict, total=False):
    InstanceId: str


class SuccessfulQueuedPurchaseDeletionTypeDef(TypedDict, total=False):
    ReservedInstancesId: str


class TagDescriptionTypeDef(TypedDict, total=False):
    Key: str
    ResourceId: str
    ResourceType: ResourceType
    Value: str


class TagSpecificationTypeDef(TypedDict, total=False):
    ResourceType: ResourceType
    Tags: List["TagTypeDef"]


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    Value: str


class _RequiredTargetCapacitySpecificationRequestTypeDef(TypedDict):
    TotalTargetCapacity: int


class TargetCapacitySpecificationRequestTypeDef(
    _RequiredTargetCapacitySpecificationRequestTypeDef, total=False
):
    OnDemandTargetCapacity: int
    SpotTargetCapacity: int
    DefaultTargetCapacityType: DefaultTargetCapacityType


class TargetCapacitySpecificationTypeDef(TypedDict, total=False):
    TotalTargetCapacity: int
    OnDemandTargetCapacity: int
    SpotTargetCapacity: int
    DefaultTargetCapacityType: DefaultTargetCapacityType


class _RequiredTargetConfigurationRequestTypeDef(TypedDict):
    OfferingId: str


class TargetConfigurationRequestTypeDef(_RequiredTargetConfigurationRequestTypeDef, total=False):
    InstanceCount: int


class TargetConfigurationTypeDef(TypedDict, total=False):
    InstanceCount: int
    OfferingId: str


class TargetGroupTypeDef(TypedDict, total=False):
    Arn: str


class TargetGroupsConfigTypeDef(TypedDict, total=False):
    TargetGroups: List["TargetGroupTypeDef"]


class TargetNetworkTypeDef(TypedDict, total=False):
    AssociationId: str
    VpcId: str
    TargetNetworkId: str
    ClientVpnEndpointId: str
    Status: "AssociationStatusTypeDef"
    SecurityGroups: List[str]


class TargetReservationValueTypeDef(TypedDict, total=False):
    ReservationValue: "ReservationValueTypeDef"
    TargetConfiguration: "TargetConfigurationTypeDef"


class TerminateClientVpnConnectionsResultTypeDef(TypedDict, total=False):
    ClientVpnEndpointId: str
    Username: str
    ConnectionStatuses: List["TerminateConnectionStatusTypeDef"]


class TerminateConnectionStatusTypeDef(TypedDict, total=False):
    ConnectionId: str
    PreviousStatus: "ClientVpnConnectionStatusTypeDef"
    CurrentStatus: "ClientVpnConnectionStatusTypeDef"


class TerminateInstancesResultTypeDef(TypedDict, total=False):
    TerminatingInstances: List["InstanceStateChangeTypeDef"]


TrafficMirrorFilterRuleTypeDef = TypedDict(
    "TrafficMirrorFilterRuleTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
        "TrafficMirrorFilterId": str,
        "TrafficDirection": TrafficDirection,
        "RuleNumber": int,
        "RuleAction": TrafficMirrorRuleAction,
        "Protocol": int,
        "DestinationPortRange": "TrafficMirrorPortRangeTypeDef",
        "SourcePortRange": "TrafficMirrorPortRangeTypeDef",
        "DestinationCidrBlock": str,
        "SourceCidrBlock": str,
        "Description": str,
    },
    total=False,
)


class TrafficMirrorFilterTypeDef(TypedDict, total=False):
    TrafficMirrorFilterId: str
    IngressFilterRules: List["TrafficMirrorFilterRuleTypeDef"]
    EgressFilterRules: List["TrafficMirrorFilterRuleTypeDef"]
    NetworkServices: List[Literal["amazon-dns"]]
    Description: str
    Tags: List["TagTypeDef"]


class TrafficMirrorPortRangeRequestTypeDef(TypedDict, total=False):
    FromPort: int
    ToPort: int


class TrafficMirrorPortRangeTypeDef(TypedDict, total=False):
    FromPort: int
    ToPort: int


class TrafficMirrorSessionTypeDef(TypedDict, total=False):
    TrafficMirrorSessionId: str
    TrafficMirrorTargetId: str
    TrafficMirrorFilterId: str
    NetworkInterfaceId: str
    OwnerId: str
    PacketLength: int
    SessionNumber: int
    VirtualNetworkId: int
    Description: str
    Tags: List["TagTypeDef"]


TrafficMirrorTargetTypeDef = TypedDict(
    "TrafficMirrorTargetTypeDef",
    {
        "TrafficMirrorTargetId": str,
        "NetworkInterfaceId": str,
        "NetworkLoadBalancerArn": str,
        "Type": TrafficMirrorTargetType,
        "Description": str,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class TransitGatewayAssociationTypeDef(TypedDict, total=False):
    TransitGatewayRouteTableId: str
    TransitGatewayAttachmentId: str
    ResourceId: str
    ResourceType: TransitGatewayAttachmentResourceType
    State: TransitGatewayAssociationState


class TransitGatewayAttachmentAssociationTypeDef(TypedDict, total=False):
    TransitGatewayRouteTableId: str
    State: TransitGatewayAssociationState


class TransitGatewayAttachmentBgpConfigurationTypeDef(TypedDict, total=False):
    TransitGatewayAsn: int
    PeerAsn: int
    TransitGatewayAddress: str
    PeerAddress: str
    BgpStatus: BgpStatus


class TransitGatewayAttachmentPropagationTypeDef(TypedDict, total=False):
    TransitGatewayRouteTableId: str
    State: TransitGatewayPropagationState


class TransitGatewayAttachmentTypeDef(TypedDict, total=False):
    TransitGatewayAttachmentId: str
    TransitGatewayId: str
    TransitGatewayOwnerId: str
    ResourceOwnerId: str
    ResourceType: TransitGatewayAttachmentResourceType
    ResourceId: str
    State: TransitGatewayAttachmentState
    Association: "TransitGatewayAttachmentAssociationTypeDef"
    CreationTime: datetime
    Tags: List["TagTypeDef"]


TransitGatewayConnectOptionsTypeDef = TypedDict(
    "TransitGatewayConnectOptionsTypeDef", {"Protocol": Literal["gre"]}, total=False
)

TransitGatewayConnectPeerConfigurationTypeDef = TypedDict(
    "TransitGatewayConnectPeerConfigurationTypeDef",
    {
        "TransitGatewayAddress": str,
        "PeerAddress": str,
        "InsideCidrBlocks": List[str],
        "Protocol": Literal["gre"],
        "BgpConfigurations": List["TransitGatewayAttachmentBgpConfigurationTypeDef"],
    },
    total=False,
)


class TransitGatewayConnectPeerTypeDef(TypedDict, total=False):
    TransitGatewayAttachmentId: str
    TransitGatewayConnectPeerId: str
    State: TransitGatewayConnectPeerState
    CreationTime: datetime
    ConnectPeerConfiguration: "TransitGatewayConnectPeerConfigurationTypeDef"
    Tags: List["TagTypeDef"]


class TransitGatewayConnectRequestBgpOptionsTypeDef(TypedDict, total=False):
    PeerAsn: int


class TransitGatewayConnectTypeDef(TypedDict, total=False):
    TransitGatewayAttachmentId: str
    TransportTransitGatewayAttachmentId: str
    TransitGatewayId: str
    State: TransitGatewayAttachmentState
    CreationTime: datetime
    Options: "TransitGatewayConnectOptionsTypeDef"
    Tags: List["TagTypeDef"]


class TransitGatewayMulticastDeregisteredGroupMembersTypeDef(TypedDict, total=False):
    TransitGatewayMulticastDomainId: str
    DeregisteredNetworkInterfaceIds: List[str]
    GroupIpAddress: str


class TransitGatewayMulticastDeregisteredGroupSourcesTypeDef(TypedDict, total=False):
    TransitGatewayMulticastDomainId: str
    DeregisteredNetworkInterfaceIds: List[str]
    GroupIpAddress: str


class TransitGatewayMulticastDomainAssociationTypeDef(TypedDict, total=False):
    TransitGatewayAttachmentId: str
    ResourceId: str
    ResourceType: TransitGatewayAttachmentResourceType
    ResourceOwnerId: str
    Subnet: "SubnetAssociationTypeDef"


class TransitGatewayMulticastDomainAssociationsTypeDef(TypedDict, total=False):
    TransitGatewayMulticastDomainId: str
    TransitGatewayAttachmentId: str
    ResourceId: str
    ResourceType: TransitGatewayAttachmentResourceType
    ResourceOwnerId: str
    Subnets: List["SubnetAssociationTypeDef"]


class TransitGatewayMulticastDomainOptionsTypeDef(TypedDict, total=False):
    Igmpv2Support: Igmpv2SupportValue
    StaticSourcesSupport: StaticSourcesSupportValue
    AutoAcceptSharedAssociations: AutoAcceptSharedAssociationsValue


class TransitGatewayMulticastDomainTypeDef(TypedDict, total=False):
    TransitGatewayMulticastDomainId: str
    TransitGatewayId: str
    TransitGatewayMulticastDomainArn: str
    OwnerId: str
    Options: "TransitGatewayMulticastDomainOptionsTypeDef"
    State: TransitGatewayMulticastDomainState
    CreationTime: datetime
    Tags: List["TagTypeDef"]


class TransitGatewayMulticastGroupTypeDef(TypedDict, total=False):
    GroupIpAddress: str
    TransitGatewayAttachmentId: str
    SubnetId: str
    ResourceId: str
    ResourceType: TransitGatewayAttachmentResourceType
    ResourceOwnerId: str
    NetworkInterfaceId: str
    GroupMember: bool
    GroupSource: bool
    MemberType: MembershipType
    SourceType: MembershipType


class TransitGatewayMulticastRegisteredGroupMembersTypeDef(TypedDict, total=False):
    TransitGatewayMulticastDomainId: str
    RegisteredNetworkInterfaceIds: List[str]
    GroupIpAddress: str


class TransitGatewayMulticastRegisteredGroupSourcesTypeDef(TypedDict, total=False):
    TransitGatewayMulticastDomainId: str
    RegisteredNetworkInterfaceIds: List[str]
    GroupIpAddress: str


class TransitGatewayOptionsTypeDef(TypedDict, total=False):
    AmazonSideAsn: int
    TransitGatewayCidrBlocks: List[str]
    AutoAcceptSharedAttachments: AutoAcceptSharedAttachmentsValue
    DefaultRouteTableAssociation: DefaultRouteTableAssociationValue
    AssociationDefaultRouteTableId: str
    DefaultRouteTablePropagation: DefaultRouteTablePropagationValue
    PropagationDefaultRouteTableId: str
    VpnEcmpSupport: VpnEcmpSupportValue
    DnsSupport: DnsSupportValue
    MulticastSupport: MulticastSupportValue


class TransitGatewayPeeringAttachmentTypeDef(TypedDict, total=False):
    TransitGatewayAttachmentId: str
    RequesterTgwInfo: "PeeringTgwInfoTypeDef"
    AccepterTgwInfo: "PeeringTgwInfoTypeDef"
    Status: "PeeringAttachmentStatusTypeDef"
    State: TransitGatewayAttachmentState
    CreationTime: datetime
    Tags: List["TagTypeDef"]


class TransitGatewayPrefixListAttachmentTypeDef(TypedDict, total=False):
    TransitGatewayAttachmentId: str
    ResourceType: TransitGatewayAttachmentResourceType
    ResourceId: str


class TransitGatewayPrefixListReferenceTypeDef(TypedDict, total=False):
    TransitGatewayRouteTableId: str
    PrefixListId: str
    PrefixListOwnerId: str
    State: TransitGatewayPrefixListReferenceState
    Blackhole: bool
    TransitGatewayAttachment: "TransitGatewayPrefixListAttachmentTypeDef"


class TransitGatewayPropagationTypeDef(TypedDict, total=False):
    TransitGatewayAttachmentId: str
    ResourceId: str
    ResourceType: TransitGatewayAttachmentResourceType
    TransitGatewayRouteTableId: str
    State: TransitGatewayPropagationState


class TransitGatewayRequestOptionsTypeDef(TypedDict, total=False):
    AmazonSideAsn: int
    AutoAcceptSharedAttachments: AutoAcceptSharedAttachmentsValue
    DefaultRouteTableAssociation: DefaultRouteTableAssociationValue
    DefaultRouteTablePropagation: DefaultRouteTablePropagationValue
    VpnEcmpSupport: VpnEcmpSupportValue
    DnsSupport: DnsSupportValue
    MulticastSupport: MulticastSupportValue
    TransitGatewayCidrBlocks: List[str]


class TransitGatewayRouteAttachmentTypeDef(TypedDict, total=False):
    ResourceId: str
    TransitGatewayAttachmentId: str
    ResourceType: TransitGatewayAttachmentResourceType


class TransitGatewayRouteTableAssociationTypeDef(TypedDict, total=False):
    TransitGatewayAttachmentId: str
    ResourceId: str
    ResourceType: TransitGatewayAttachmentResourceType
    State: TransitGatewayAssociationState


class TransitGatewayRouteTablePropagationTypeDef(TypedDict, total=False):
    TransitGatewayAttachmentId: str
    ResourceId: str
    ResourceType: TransitGatewayAttachmentResourceType
    State: TransitGatewayPropagationState


class TransitGatewayRouteTableTypeDef(TypedDict, total=False):
    TransitGatewayRouteTableId: str
    TransitGatewayId: str
    State: TransitGatewayRouteTableState
    DefaultAssociationRouteTable: bool
    DefaultPropagationRouteTable: bool
    CreationTime: datetime
    Tags: List["TagTypeDef"]


TransitGatewayRouteTypeDef = TypedDict(
    "TransitGatewayRouteTypeDef",
    {
        "DestinationCidrBlock": str,
        "PrefixListId": str,
        "TransitGatewayAttachments": List["TransitGatewayRouteAttachmentTypeDef"],
        "Type": TransitGatewayRouteType,
        "State": TransitGatewayRouteState,
    },
    total=False,
)


class TransitGatewayTypeDef(TypedDict, total=False):
    TransitGatewayId: str
    TransitGatewayArn: str
    State: TransitGatewayState
    OwnerId: str
    Description: str
    CreationTime: datetime
    Options: "TransitGatewayOptionsTypeDef"
    Tags: List["TagTypeDef"]


class TransitGatewayVpcAttachmentOptionsTypeDef(TypedDict, total=False):
    DnsSupport: DnsSupportValue
    Ipv6Support: Ipv6SupportValue
    ApplianceModeSupport: ApplianceModeSupportValue


class TransitGatewayVpcAttachmentTypeDef(TypedDict, total=False):
    TransitGatewayAttachmentId: str
    TransitGatewayId: str
    VpcId: str
    VpcOwnerId: str
    State: TransitGatewayAttachmentState
    SubnetIds: List[str]
    CreationTime: datetime
    Options: "TransitGatewayVpcAttachmentOptionsTypeDef"
    Tags: List["TagTypeDef"]


class TunnelOptionTypeDef(TypedDict, total=False):
    OutsideIpAddress: str
    TunnelInsideCidr: str
    TunnelInsideIpv6Cidr: str
    PreSharedKey: str
    Phase1LifetimeSeconds: int
    Phase2LifetimeSeconds: int
    RekeyMarginTimeSeconds: int
    RekeyFuzzPercentage: int
    ReplayWindowSize: int
    DpdTimeoutSeconds: int
    DpdTimeoutAction: str
    Phase1EncryptionAlgorithms: List["Phase1EncryptionAlgorithmsListValueTypeDef"]
    Phase2EncryptionAlgorithms: List["Phase2EncryptionAlgorithmsListValueTypeDef"]
    Phase1IntegrityAlgorithms: List["Phase1IntegrityAlgorithmsListValueTypeDef"]
    Phase2IntegrityAlgorithms: List["Phase2IntegrityAlgorithmsListValueTypeDef"]
    Phase1DHGroupNumbers: List["Phase1DHGroupNumbersListValueTypeDef"]
    Phase2DHGroupNumbers: List["Phase2DHGroupNumbersListValueTypeDef"]
    IkeVersions: List["IKEVersionsListValueTypeDef"]
    StartupAction: str


class UnassignIpv6AddressesResultTypeDef(TypedDict, total=False):
    NetworkInterfaceId: str
    UnassignedIpv6Addresses: List[str]


class UnmonitorInstancesResultTypeDef(TypedDict, total=False):
    InstanceMonitorings: List["InstanceMonitoringTypeDef"]


class UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef(TypedDict, total=False):
    Code: UnsuccessfulInstanceCreditSpecificationErrorCode
    Message: str


class UnsuccessfulInstanceCreditSpecificationItemTypeDef(TypedDict, total=False):
    InstanceId: str
    Error: "UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef"


class UnsuccessfulItemErrorTypeDef(TypedDict, total=False):
    Code: str
    Message: str


class UnsuccessfulItemTypeDef(TypedDict, total=False):
    Error: "UnsuccessfulItemErrorTypeDef"
    ResourceId: str


class UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef(TypedDict, total=False):
    Return: bool


class UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef(TypedDict, total=False):
    Return: bool


class UserBucketDetailsTypeDef(TypedDict, total=False):
    S3Bucket: str
    S3Key: str


class UserBucketTypeDef(TypedDict, total=False):
    S3Bucket: str
    S3Key: str


class UserDataTypeDef(TypedDict, total=False):
    Data: str


class UserIdGroupPairTypeDef(TypedDict, total=False):
    Description: str
    GroupId: str
    GroupName: str
    PeeringStatus: str
    UserId: str
    VpcId: str
    VpcPeeringConnectionId: str


class VCpuInfoTypeDef(TypedDict, total=False):
    DefaultVCpus: int
    DefaultCores: int
    DefaultThreadsPerCore: int
    ValidCores: List[int]
    ValidThreadsPerCore: List[int]


class ValidationErrorTypeDef(TypedDict, total=False):
    Code: str
    Message: str


class ValidationWarningTypeDef(TypedDict, total=False):
    Errors: List["ValidationErrorTypeDef"]


class VgwTelemetryTypeDef(TypedDict, total=False):
    AcceptedRouteCount: int
    LastStatusChange: datetime
    OutsideIpAddress: str
    Status: TelemetryStatus
    StatusMessage: str
    CertificateArn: str


class VolumeAttachmentTypeDef(TypedDict, total=False):
    AttachTime: datetime
    Device: str
    InstanceId: str
    State: VolumeAttachmentState
    VolumeId: str
    DeleteOnTermination: bool


class VolumeDetailTypeDef(TypedDict):
    Size: int


class VolumeModificationTypeDef(TypedDict, total=False):
    VolumeId: str
    ModificationState: VolumeModificationState
    StatusMessage: str
    TargetSize: int
    TargetIops: int
    TargetVolumeType: VolumeType
    TargetThroughput: int
    TargetMultiAttachEnabled: bool
    OriginalSize: int
    OriginalIops: int
    OriginalVolumeType: VolumeType
    OriginalThroughput: int
    OriginalMultiAttachEnabled: bool
    Progress: int
    StartTime: datetime
    EndTime: datetime


class VolumeStatusActionTypeDef(TypedDict, total=False):
    Code: str
    Description: str
    EventId: str
    EventType: str


class VolumeStatusAttachmentStatusTypeDef(TypedDict, total=False):
    IoPerformance: str
    InstanceId: str


class VolumeStatusDetailsTypeDef(TypedDict, total=False):
    Name: VolumeStatusName
    Status: str


class VolumeStatusEventTypeDef(TypedDict, total=False):
    Description: str
    EventId: str
    EventType: str
    NotAfter: datetime
    NotBefore: datetime
    InstanceId: str


class VolumeStatusInfoTypeDef(TypedDict, total=False):
    Details: List["VolumeStatusDetailsTypeDef"]
    Status: VolumeStatusInfoStatus


class VolumeStatusItemTypeDef(TypedDict, total=False):
    Actions: List["VolumeStatusActionTypeDef"]
    AvailabilityZone: str
    OutpostArn: str
    Events: List["VolumeStatusEventTypeDef"]
    VolumeId: str
    VolumeStatus: "VolumeStatusInfoTypeDef"
    AttachmentStatuses: List["VolumeStatusAttachmentStatusTypeDef"]


class VolumeTypeDef(TypedDict, total=False):
    Attachments: List["VolumeAttachmentTypeDef"]
    AvailabilityZone: str
    CreateTime: datetime
    Encrypted: bool
    KmsKeyId: str
    OutpostArn: str
    Size: int
    SnapshotId: str
    State: VolumeState
    VolumeId: str
    Iops: int
    Tags: List["TagTypeDef"]
    VolumeType: VolumeType
    FastRestored: bool
    MultiAttachEnabled: bool
    Throughput: int


class VpcAttachmentTypeDef(TypedDict, total=False):
    State: AttachmentStatus
    VpcId: str


class VpcCidrBlockAssociationTypeDef(TypedDict, total=False):
    AssociationId: str
    CidrBlock: str
    CidrBlockState: "VpcCidrBlockStateTypeDef"


class VpcCidrBlockStateTypeDef(TypedDict, total=False):
    State: VpcCidrBlockStateCode
    StatusMessage: str


class VpcClassicLinkTypeDef(TypedDict, total=False):
    ClassicLinkEnabled: bool
    Tags: List["TagTypeDef"]
    VpcId: str


class VpcEndpointConnectionTypeDef(TypedDict, total=False):
    ServiceId: str
    VpcEndpointId: str
    VpcEndpointOwner: str
    VpcEndpointState: State
    CreationTimestamp: datetime
    DnsEntries: List["DnsEntryTypeDef"]
    NetworkLoadBalancerArns: List[str]
    GatewayLoadBalancerArns: List[str]


class VpcEndpointTypeDef(TypedDict, total=False):
    VpcEndpointId: str
    VpcEndpointType: VpcEndpointType
    VpcId: str
    ServiceName: str
    State: State
    PolicyDocument: str
    RouteTableIds: List[str]
    SubnetIds: List[str]
    Groups: List["SecurityGroupIdentifierTypeDef"]
    PrivateDnsEnabled: bool
    RequesterManaged: bool
    NetworkInterfaceIds: List[str]
    DnsEntries: List["DnsEntryTypeDef"]
    CreationTimestamp: datetime
    Tags: List["TagTypeDef"]
    OwnerId: str
    LastError: "LastErrorTypeDef"


class VpcIpv6CidrBlockAssociationTypeDef(TypedDict, total=False):
    AssociationId: str
    Ipv6CidrBlock: str
    Ipv6CidrBlockState: "VpcCidrBlockStateTypeDef"
    NetworkBorderGroup: str
    Ipv6Pool: str


class VpcPeeringConnectionOptionsDescriptionTypeDef(TypedDict, total=False):
    AllowDnsResolutionFromRemoteVpc: bool
    AllowEgressFromLocalClassicLinkToRemoteVpc: bool
    AllowEgressFromLocalVpcToRemoteClassicLink: bool


class VpcPeeringConnectionStateReasonTypeDef(TypedDict, total=False):
    Code: VpcPeeringConnectionStateReasonCode
    Message: str


class VpcPeeringConnectionTypeDef(TypedDict, total=False):
    AccepterVpcInfo: "VpcPeeringConnectionVpcInfoTypeDef"
    ExpirationTime: datetime
    RequesterVpcInfo: "VpcPeeringConnectionVpcInfoTypeDef"
    Status: "VpcPeeringConnectionStateReasonTypeDef"
    Tags: List["TagTypeDef"]
    VpcPeeringConnectionId: str


class VpcPeeringConnectionVpcInfoTypeDef(TypedDict, total=False):
    CidrBlock: str
    Ipv6CidrBlockSet: List["Ipv6CidrBlockTypeDef"]
    CidrBlockSet: List["CidrBlockTypeDef"]
    OwnerId: str
    PeeringOptions: "VpcPeeringConnectionOptionsDescriptionTypeDef"
    VpcId: str
    Region: str


class VpcTypeDef(TypedDict, total=False):
    CidrBlock: str
    DhcpOptionsId: str
    State: VpcState
    VpcId: str
    OwnerId: str
    InstanceTenancy: Tenancy
    Ipv6CidrBlockAssociationSet: List["VpcIpv6CidrBlockAssociationTypeDef"]
    CidrBlockAssociationSet: List["VpcCidrBlockAssociationTypeDef"]
    IsDefault: bool
    Tags: List["TagTypeDef"]


class VpnConnectionOptionsSpecificationTypeDef(TypedDict, total=False):
    EnableAcceleration: bool
    StaticRoutesOnly: bool
    TunnelInsideIpVersion: TunnelInsideIpVersion
    TunnelOptions: List["VpnTunnelOptionsSpecificationTypeDef"]
    LocalIpv4NetworkCidr: str
    RemoteIpv4NetworkCidr: str
    LocalIpv6NetworkCidr: str
    RemoteIpv6NetworkCidr: str


class VpnConnectionOptionsTypeDef(TypedDict, total=False):
    EnableAcceleration: bool
    StaticRoutesOnly: bool
    LocalIpv4NetworkCidr: str
    RemoteIpv4NetworkCidr: str
    LocalIpv6NetworkCidr: str
    RemoteIpv6NetworkCidr: str
    TunnelInsideIpVersion: TunnelInsideIpVersion
    TunnelOptions: List["TunnelOptionTypeDef"]


VpnConnectionTypeDef = TypedDict(
    "VpnConnectionTypeDef",
    {
        "CustomerGatewayConfiguration": str,
        "CustomerGatewayId": str,
        "Category": str,
        "State": VpnState,
        "Type": Literal["ipsec.1"],
        "VpnConnectionId": str,
        "VpnGatewayId": str,
        "TransitGatewayId": str,
        "Options": "VpnConnectionOptionsTypeDef",
        "Routes": List["VpnStaticRouteTypeDef"],
        "Tags": List["TagTypeDef"],
        "VgwTelemetry": List["VgwTelemetryTypeDef"],
    },
    total=False,
)

VpnGatewayTypeDef = TypedDict(
    "VpnGatewayTypeDef",
    {
        "AvailabilityZone": str,
        "State": VpnState,
        "Type": Literal["ipsec.1"],
        "VpcAttachments": List["VpcAttachmentTypeDef"],
        "VpnGatewayId": str,
        "AmazonSideAsn": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)


class VpnStaticRouteTypeDef(TypedDict, total=False):
    DestinationCidrBlock: str
    Source: Literal["Static"]
    State: VpnState


class VpnTunnelOptionsSpecificationTypeDef(TypedDict, total=False):
    TunnelInsideCidr: str
    TunnelInsideIpv6Cidr: str
    PreSharedKey: str
    Phase1LifetimeSeconds: int
    Phase2LifetimeSeconds: int
    RekeyMarginTimeSeconds: int
    RekeyFuzzPercentage: int
    ReplayWindowSize: int
    DPDTimeoutSeconds: int
    DPDTimeoutAction: str
    Phase1EncryptionAlgorithms: List["Phase1EncryptionAlgorithmsRequestListValueTypeDef"]
    Phase2EncryptionAlgorithms: List["Phase2EncryptionAlgorithmsRequestListValueTypeDef"]
    Phase1IntegrityAlgorithms: List["Phase1IntegrityAlgorithmsRequestListValueTypeDef"]
    Phase2IntegrityAlgorithms: List["Phase2IntegrityAlgorithmsRequestListValueTypeDef"]
    Phase1DHGroupNumbers: List["Phase1DHGroupNumbersRequestListValueTypeDef"]
    Phase2DHGroupNumbers: List["Phase2DHGroupNumbersRequestListValueTypeDef"]
    IKEVersions: List["IKEVersionsRequestListValueTypeDef"]
    StartupAction: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int


class WithdrawByoipCidrResultTypeDef(TypedDict, total=False):
    ByoipCidr: "ByoipCidrTypeDef"
