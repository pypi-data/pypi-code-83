"""
Type annotations for ec2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ec2 import EC2Client

    client: EC2Client = boto3.client("ec2")
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Optional, Type, Union, overload

from botocore.client import ClientMeta

from mypy_boto3_ec2.literals import (
    AccountAttributeName,
    Affinity,
    ArchitectureValues,
    AutoPlacement,
    BootModeValues,
    CapacityReservationInstancePlatform,
    CapacityReservationTenancy,
    DiskImageFormat,
    DomainType,
    EndDateType,
    EventType,
    ExcessCapacityTerminationPolicy,
    ExportEnvironment,
    FleetEventType,
    FleetExcessCapacityTerminationPolicy,
    FleetType,
    FlowLogsResourceType,
    FpgaImageAttributeName,
    HostRecovery,
    HostTenancy,
    HttpTokensState,
    ImageAttributeName,
    InstanceAttributeName,
    InstanceInterruptionBehavior,
    InstanceMatchCriteria,
    InstanceMetadataEndpointState,
    InstanceType,
    InterfacePermissionType,
    LocationType,
    LogDestinationType,
    ModifyAvailabilityZoneOptInStatus,
    NetworkInterfaceAttribute,
    OfferingClassType,
    OfferingTypeValues,
    OperationType,
    PlacementStrategy,
    ProtocolType,
    ReportInstanceReasonCodes,
    ReportStatusType,
    RIProductDescription,
    RuleAction,
    SelfServicePortal,
    ShutdownBehavior,
    SnapshotAttributeName,
    SpotInstanceType,
    Tenancy,
    TrafficDirection,
    TrafficMirrorFilterRuleField,
    TrafficMirrorRuleAction,
    TrafficMirrorSessionField,
    TrafficType,
    TransportProtocol,
    UnlimitedSupportedInstanceFamily,
    VolumeAttributeName,
    VolumeType,
    VpcAttributeName,
    VpcEndpointType,
)
from mypy_boto3_ec2.paginator import (
    DescribeAddressesAttributePaginator,
    DescribeByoipCidrsPaginator,
    DescribeCapacityReservationsPaginator,
    DescribeCarrierGatewaysPaginator,
    DescribeClassicLinkInstancesPaginator,
    DescribeClientVpnAuthorizationRulesPaginator,
    DescribeClientVpnConnectionsPaginator,
    DescribeClientVpnEndpointsPaginator,
    DescribeClientVpnRoutesPaginator,
    DescribeClientVpnTargetNetworksPaginator,
    DescribeCoipPoolsPaginator,
    DescribeDhcpOptionsPaginator,
    DescribeEgressOnlyInternetGatewaysPaginator,
    DescribeExportImageTasksPaginator,
    DescribeFastSnapshotRestoresPaginator,
    DescribeFleetsPaginator,
    DescribeFlowLogsPaginator,
    DescribeFpgaImagesPaginator,
    DescribeHostReservationOfferingsPaginator,
    DescribeHostReservationsPaginator,
    DescribeHostsPaginator,
    DescribeIamInstanceProfileAssociationsPaginator,
    DescribeImportImageTasksPaginator,
    DescribeImportSnapshotTasksPaginator,
    DescribeInstanceCreditSpecificationsPaginator,
    DescribeInstancesPaginator,
    DescribeInstanceStatusPaginator,
    DescribeInstanceTypeOfferingsPaginator,
    DescribeInstanceTypesPaginator,
    DescribeInternetGatewaysPaginator,
    DescribeIpv6PoolsPaginator,
    DescribeLaunchTemplatesPaginator,
    DescribeLaunchTemplateVersionsPaginator,
    DescribeLocalGatewayRouteTablesPaginator,
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator,
    DescribeLocalGatewayRouteTableVpcAssociationsPaginator,
    DescribeLocalGatewaysPaginator,
    DescribeLocalGatewayVirtualInterfaceGroupsPaginator,
    DescribeLocalGatewayVirtualInterfacesPaginator,
    DescribeManagedPrefixListsPaginator,
    DescribeMovingAddressesPaginator,
    DescribeNatGatewaysPaginator,
    DescribeNetworkAclsPaginator,
    DescribeNetworkInsightsAnalysesPaginator,
    DescribeNetworkInsightsPathsPaginator,
    DescribeNetworkInterfacePermissionsPaginator,
    DescribeNetworkInterfacesPaginator,
    DescribePrefixListsPaginator,
    DescribePrincipalIdFormatPaginator,
    DescribePublicIpv4PoolsPaginator,
    DescribeReplaceRootVolumeTasksPaginator,
    DescribeReservedInstancesModificationsPaginator,
    DescribeReservedInstancesOfferingsPaginator,
    DescribeRouteTablesPaginator,
    DescribeScheduledInstanceAvailabilityPaginator,
    DescribeScheduledInstancesPaginator,
    DescribeSecurityGroupsPaginator,
    DescribeSnapshotsPaginator,
    DescribeSpotFleetInstancesPaginator,
    DescribeSpotFleetRequestsPaginator,
    DescribeSpotInstanceRequestsPaginator,
    DescribeSpotPriceHistoryPaginator,
    DescribeStaleSecurityGroupsPaginator,
    DescribeStoreImageTasksPaginator,
    DescribeSubnetsPaginator,
    DescribeTagsPaginator,
    DescribeTrafficMirrorFiltersPaginator,
    DescribeTrafficMirrorSessionsPaginator,
    DescribeTrafficMirrorTargetsPaginator,
    DescribeTransitGatewayAttachmentsPaginator,
    DescribeTransitGatewayConnectPeersPaginator,
    DescribeTransitGatewayConnectsPaginator,
    DescribeTransitGatewayMulticastDomainsPaginator,
    DescribeTransitGatewayPeeringAttachmentsPaginator,
    DescribeTransitGatewayRouteTablesPaginator,
    DescribeTransitGatewaysPaginator,
    DescribeTransitGatewayVpcAttachmentsPaginator,
    DescribeVolumesModificationsPaginator,
    DescribeVolumesPaginator,
    DescribeVolumeStatusPaginator,
    DescribeVpcClassicLinkDnsSupportPaginator,
    DescribeVpcEndpointConnectionNotificationsPaginator,
    DescribeVpcEndpointConnectionsPaginator,
    DescribeVpcEndpointServiceConfigurationsPaginator,
    DescribeVpcEndpointServicePermissionsPaginator,
    DescribeVpcEndpointServicesPaginator,
    DescribeVpcEndpointsPaginator,
    DescribeVpcPeeringConnectionsPaginator,
    DescribeVpcsPaginator,
    GetAssociatedIpv6PoolCidrsPaginator,
    GetGroupsForCapacityReservationPaginator,
    GetManagedPrefixListAssociationsPaginator,
    GetManagedPrefixListEntriesPaginator,
    GetTransitGatewayAttachmentPropagationsPaginator,
    GetTransitGatewayMulticastDomainAssociationsPaginator,
    GetTransitGatewayPrefixListReferencesPaginator,
    GetTransitGatewayRouteTableAssociationsPaginator,
    GetTransitGatewayRouteTablePropagationsPaginator,
    SearchLocalGatewayRoutesPaginator,
    SearchTransitGatewayMulticastGroupsPaginator,
)
from mypy_boto3_ec2.type_defs import (
    AcceptReservedInstancesExchangeQuoteResultTypeDef,
    AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef,
    AcceptTransitGatewayPeeringAttachmentResultTypeDef,
    AcceptTransitGatewayVpcAttachmentResultTypeDef,
    AcceptVpcEndpointConnectionsResultTypeDef,
    AcceptVpcPeeringConnectionResultTypeDef,
    AddPrefixListEntryTypeDef,
    AdvertiseByoipCidrResultTypeDef,
    AllocateAddressResultTypeDef,
    AllocateHostsResultTypeDef,
    ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef,
    AssignIpv6AddressesResultTypeDef,
    AssignPrivateIpAddressesResultTypeDef,
    AssociateAddressResultTypeDef,
    AssociateClientVpnTargetNetworkResultTypeDef,
    AssociateEnclaveCertificateIamRoleResultTypeDef,
    AssociateIamInstanceProfileResultTypeDef,
    AssociateRouteTableResultTypeDef,
    AssociateSubnetCidrBlockResultTypeDef,
    AssociateTransitGatewayMulticastDomainResultTypeDef,
    AssociateTransitGatewayRouteTableResultTypeDef,
    AssociateVpcCidrBlockResultTypeDef,
    AttachClassicLinkVpcResultTypeDef,
    AttachNetworkInterfaceResultTypeDef,
    AttachVpnGatewayResultTypeDef,
    AttributeBooleanValueTypeDef,
    AttributeValueTypeDef,
    AuthorizeClientVpnIngressResultTypeDef,
    BlobAttributeValueTypeDef,
    BlockDeviceMappingTypeDef,
    BundleInstanceResultTypeDef,
    CancelBundleTaskResultTypeDef,
    CancelCapacityReservationResultTypeDef,
    CancelImportTaskResultTypeDef,
    CancelReservedInstancesListingResultTypeDef,
    CancelSpotFleetRequestsResponseTypeDef,
    CancelSpotInstanceRequestsResultTypeDef,
    CapacityReservationSpecificationTypeDef,
    CidrAuthorizationContextTypeDef,
    ClientConnectOptionsTypeDef,
    ClientDataTypeDef,
    ClientVpnAuthenticationRequestTypeDef,
    ConfirmProductInstanceResultTypeDef,
    ConnectionLogOptionsTypeDef,
    CopyFpgaImageResultTypeDef,
    CopyImageResultTypeDef,
    CopySnapshotResultTypeDef,
    CpuOptionsRequestTypeDef,
    CreateCapacityReservationResultTypeDef,
    CreateCarrierGatewayResultTypeDef,
    CreateClientVpnEndpointResultTypeDef,
    CreateClientVpnRouteResultTypeDef,
    CreateCustomerGatewayResultTypeDef,
    CreateDefaultSubnetResultTypeDef,
    CreateDefaultVpcResultTypeDef,
    CreateDhcpOptionsResultTypeDef,
    CreateEgressOnlyInternetGatewayResultTypeDef,
    CreateFleetResultTypeDef,
    CreateFlowLogsResultTypeDef,
    CreateFpgaImageResultTypeDef,
    CreateImageResultTypeDef,
    CreateInstanceExportTaskResultTypeDef,
    CreateInternetGatewayResultTypeDef,
    CreateLaunchTemplateResultTypeDef,
    CreateLaunchTemplateVersionResultTypeDef,
    CreateLocalGatewayRouteResultTypeDef,
    CreateLocalGatewayRouteTableVpcAssociationResultTypeDef,
    CreateManagedPrefixListResultTypeDef,
    CreateNatGatewayResultTypeDef,
    CreateNetworkAclResultTypeDef,
    CreateNetworkInsightsPathResultTypeDef,
    CreateNetworkInterfacePermissionResultTypeDef,
    CreateNetworkInterfaceResultTypeDef,
    CreatePlacementGroupResultTypeDef,
    CreateReplaceRootVolumeTaskResultTypeDef,
    CreateReservedInstancesListingResultTypeDef,
    CreateRestoreImageTaskResultTypeDef,
    CreateRouteResultTypeDef,
    CreateRouteTableResultTypeDef,
    CreateSecurityGroupResultTypeDef,
    CreateSnapshotsResultTypeDef,
    CreateSpotDatafeedSubscriptionResultTypeDef,
    CreateStoreImageTaskResultTypeDef,
    CreateSubnetResultTypeDef,
    CreateTrafficMirrorFilterResultTypeDef,
    CreateTrafficMirrorFilterRuleResultTypeDef,
    CreateTrafficMirrorSessionResultTypeDef,
    CreateTrafficMirrorTargetResultTypeDef,
    CreateTransitGatewayConnectPeerResultTypeDef,
    CreateTransitGatewayConnectRequestOptionsTypeDef,
    CreateTransitGatewayConnectResultTypeDef,
    CreateTransitGatewayMulticastDomainRequestOptionsTypeDef,
    CreateTransitGatewayMulticastDomainResultTypeDef,
    CreateTransitGatewayPeeringAttachmentResultTypeDef,
    CreateTransitGatewayPrefixListReferenceResultTypeDef,
    CreateTransitGatewayResultTypeDef,
    CreateTransitGatewayRouteResultTypeDef,
    CreateTransitGatewayRouteTableResultTypeDef,
    CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef,
    CreateTransitGatewayVpcAttachmentResultTypeDef,
    CreateVolumePermissionModificationsTypeDef,
    CreateVpcEndpointConnectionNotificationResultTypeDef,
    CreateVpcEndpointResultTypeDef,
    CreateVpcEndpointServiceConfigurationResultTypeDef,
    CreateVpcPeeringConnectionResultTypeDef,
    CreateVpcResultTypeDef,
    CreateVpnConnectionResultTypeDef,
    CreateVpnGatewayResultTypeDef,
    CreditSpecificationRequestTypeDef,
    DeleteCarrierGatewayResultTypeDef,
    DeleteClientVpnEndpointResultTypeDef,
    DeleteClientVpnRouteResultTypeDef,
    DeleteEgressOnlyInternetGatewayResultTypeDef,
    DeleteFleetsResultTypeDef,
    DeleteFlowLogsResultTypeDef,
    DeleteFpgaImageResultTypeDef,
    DeleteLaunchTemplateResultTypeDef,
    DeleteLaunchTemplateVersionsResultTypeDef,
    DeleteLocalGatewayRouteResultTypeDef,
    DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef,
    DeleteManagedPrefixListResultTypeDef,
    DeleteNatGatewayResultTypeDef,
    DeleteNetworkInsightsAnalysisResultTypeDef,
    DeleteNetworkInsightsPathResultTypeDef,
    DeleteNetworkInterfacePermissionResultTypeDef,
    DeleteQueuedReservedInstancesResultTypeDef,
    DeleteTrafficMirrorFilterResultTypeDef,
    DeleteTrafficMirrorFilterRuleResultTypeDef,
    DeleteTrafficMirrorSessionResultTypeDef,
    DeleteTrafficMirrorTargetResultTypeDef,
    DeleteTransitGatewayConnectPeerResultTypeDef,
    DeleteTransitGatewayConnectResultTypeDef,
    DeleteTransitGatewayMulticastDomainResultTypeDef,
    DeleteTransitGatewayPeeringAttachmentResultTypeDef,
    DeleteTransitGatewayPrefixListReferenceResultTypeDef,
    DeleteTransitGatewayResultTypeDef,
    DeleteTransitGatewayRouteResultTypeDef,
    DeleteTransitGatewayRouteTableResultTypeDef,
    DeleteTransitGatewayVpcAttachmentResultTypeDef,
    DeleteVpcEndpointConnectionNotificationsResultTypeDef,
    DeleteVpcEndpointServiceConfigurationsResultTypeDef,
    DeleteVpcEndpointsResultTypeDef,
    DeleteVpcPeeringConnectionResultTypeDef,
    DeprovisionByoipCidrResultTypeDef,
    DeregisterInstanceEventNotificationAttributesResultTypeDef,
    DeregisterInstanceTagAttributeRequestTypeDef,
    DeregisterTransitGatewayMulticastGroupMembersResultTypeDef,
    DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef,
    DescribeAccountAttributesResultTypeDef,
    DescribeAddressesAttributeResultTypeDef,
    DescribeAddressesResultTypeDef,
    DescribeAggregateIdFormatResultTypeDef,
    DescribeAvailabilityZonesResultTypeDef,
    DescribeBundleTasksResultTypeDef,
    DescribeByoipCidrsResultTypeDef,
    DescribeCapacityReservationsResultTypeDef,
    DescribeCarrierGatewaysResultTypeDef,
    DescribeClassicLinkInstancesResultTypeDef,
    DescribeClientVpnAuthorizationRulesResultTypeDef,
    DescribeClientVpnConnectionsResultTypeDef,
    DescribeClientVpnEndpointsResultTypeDef,
    DescribeClientVpnRoutesResultTypeDef,
    DescribeClientVpnTargetNetworksResultTypeDef,
    DescribeCoipPoolsResultTypeDef,
    DescribeConversionTasksResultTypeDef,
    DescribeCustomerGatewaysResultTypeDef,
    DescribeDhcpOptionsResultTypeDef,
    DescribeEgressOnlyInternetGatewaysResultTypeDef,
    DescribeElasticGpusResultTypeDef,
    DescribeExportImageTasksResultTypeDef,
    DescribeExportTasksResultTypeDef,
    DescribeFastSnapshotRestoresResultTypeDef,
    DescribeFleetHistoryResultTypeDef,
    DescribeFleetInstancesResultTypeDef,
    DescribeFleetsResultTypeDef,
    DescribeFlowLogsResultTypeDef,
    DescribeFpgaImageAttributeResultTypeDef,
    DescribeFpgaImagesResultTypeDef,
    DescribeHostReservationOfferingsResultTypeDef,
    DescribeHostReservationsResultTypeDef,
    DescribeHostsResultTypeDef,
    DescribeIamInstanceProfileAssociationsResultTypeDef,
    DescribeIdentityIdFormatResultTypeDef,
    DescribeIdFormatResultTypeDef,
    DescribeImagesResultTypeDef,
    DescribeImportImageTasksResultTypeDef,
    DescribeImportSnapshotTasksResultTypeDef,
    DescribeInstanceCreditSpecificationsResultTypeDef,
    DescribeInstanceEventNotificationAttributesResultTypeDef,
    DescribeInstancesResultTypeDef,
    DescribeInstanceStatusResultTypeDef,
    DescribeInstanceTypeOfferingsResultTypeDef,
    DescribeInstanceTypesResultTypeDef,
    DescribeInternetGatewaysResultTypeDef,
    DescribeIpv6PoolsResultTypeDef,
    DescribeKeyPairsResultTypeDef,
    DescribeLaunchTemplatesResultTypeDef,
    DescribeLaunchTemplateVersionsResultTypeDef,
    DescribeLocalGatewayRouteTablesResultTypeDef,
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef,
    DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef,
    DescribeLocalGatewaysResultTypeDef,
    DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef,
    DescribeLocalGatewayVirtualInterfacesResultTypeDef,
    DescribeManagedPrefixListsResultTypeDef,
    DescribeMovingAddressesResultTypeDef,
    DescribeNatGatewaysResultTypeDef,
    DescribeNetworkAclsResultTypeDef,
    DescribeNetworkInsightsAnalysesResultTypeDef,
    DescribeNetworkInsightsPathsResultTypeDef,
    DescribeNetworkInterfaceAttributeResultTypeDef,
    DescribeNetworkInterfacePermissionsResultTypeDef,
    DescribeNetworkInterfacesResultTypeDef,
    DescribePlacementGroupsResultTypeDef,
    DescribePrefixListsResultTypeDef,
    DescribePrincipalIdFormatResultTypeDef,
    DescribePublicIpv4PoolsResultTypeDef,
    DescribeRegionsResultTypeDef,
    DescribeReplaceRootVolumeTasksResultTypeDef,
    DescribeReservedInstancesListingsResultTypeDef,
    DescribeReservedInstancesModificationsResultTypeDef,
    DescribeReservedInstancesOfferingsResultTypeDef,
    DescribeReservedInstancesResultTypeDef,
    DescribeRouteTablesResultTypeDef,
    DescribeScheduledInstanceAvailabilityResultTypeDef,
    DescribeScheduledInstancesResultTypeDef,
    DescribeSecurityGroupReferencesResultTypeDef,
    DescribeSecurityGroupsResultTypeDef,
    DescribeSnapshotAttributeResultTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeSpotDatafeedSubscriptionResultTypeDef,
    DescribeSpotFleetInstancesResponseTypeDef,
    DescribeSpotFleetRequestHistoryResponseTypeDef,
    DescribeSpotFleetRequestsResponseTypeDef,
    DescribeSpotInstanceRequestsResultTypeDef,
    DescribeSpotPriceHistoryResultTypeDef,
    DescribeStaleSecurityGroupsResultTypeDef,
    DescribeStoreImageTasksResultTypeDef,
    DescribeSubnetsResultTypeDef,
    DescribeTagsResultTypeDef,
    DescribeTrafficMirrorFiltersResultTypeDef,
    DescribeTrafficMirrorSessionsResultTypeDef,
    DescribeTrafficMirrorTargetsResultTypeDef,
    DescribeTransitGatewayAttachmentsResultTypeDef,
    DescribeTransitGatewayConnectPeersResultTypeDef,
    DescribeTransitGatewayConnectsResultTypeDef,
    DescribeTransitGatewayMulticastDomainsResultTypeDef,
    DescribeTransitGatewayPeeringAttachmentsResultTypeDef,
    DescribeTransitGatewayRouteTablesResultTypeDef,
    DescribeTransitGatewaysResultTypeDef,
    DescribeTransitGatewayVpcAttachmentsResultTypeDef,
    DescribeVolumeAttributeResultTypeDef,
    DescribeVolumesModificationsResultTypeDef,
    DescribeVolumesResultTypeDef,
    DescribeVolumeStatusResultTypeDef,
    DescribeVpcAttributeResultTypeDef,
    DescribeVpcClassicLinkDnsSupportResultTypeDef,
    DescribeVpcClassicLinkResultTypeDef,
    DescribeVpcEndpointConnectionNotificationsResultTypeDef,
    DescribeVpcEndpointConnectionsResultTypeDef,
    DescribeVpcEndpointServiceConfigurationsResultTypeDef,
    DescribeVpcEndpointServicePermissionsResultTypeDef,
    DescribeVpcEndpointServicesResultTypeDef,
    DescribeVpcEndpointsResultTypeDef,
    DescribeVpcPeeringConnectionsResultTypeDef,
    DescribeVpcsResultTypeDef,
    DescribeVpnConnectionsResultTypeDef,
    DescribeVpnGatewaysResultTypeDef,
    DetachClassicLinkVpcResultTypeDef,
    DisableEbsEncryptionByDefaultResultTypeDef,
    DisableFastSnapshotRestoresResultTypeDef,
    DisableSerialConsoleAccessResultTypeDef,
    DisableTransitGatewayRouteTablePropagationResultTypeDef,
    DisableVpcClassicLinkDnsSupportResultTypeDef,
    DisableVpcClassicLinkResultTypeDef,
    DisassociateClientVpnTargetNetworkResultTypeDef,
    DisassociateEnclaveCertificateIamRoleResultTypeDef,
    DisassociateIamInstanceProfileResultTypeDef,
    DisassociateSubnetCidrBlockResultTypeDef,
    DisassociateTransitGatewayMulticastDomainResultTypeDef,
    DisassociateTransitGatewayRouteTableResultTypeDef,
    DisassociateVpcCidrBlockResultTypeDef,
    DiskImageDetailTypeDef,
    DiskImageTypeDef,
    DnsServersOptionsModifyStructureTypeDef,
    ElasticGpuSpecificationTypeDef,
    ElasticInferenceAcceleratorTypeDef,
    EnableEbsEncryptionByDefaultResultTypeDef,
    EnableFastSnapshotRestoresResultTypeDef,
    EnableSerialConsoleAccessResultTypeDef,
    EnableTransitGatewayRouteTablePropagationResultTypeDef,
    EnableVpcClassicLinkDnsSupportResultTypeDef,
    EnableVpcClassicLinkResultTypeDef,
    EnclaveOptionsRequestTypeDef,
    ExportClientVpnClientCertificateRevocationListResultTypeDef,
    ExportClientVpnClientConfigurationResultTypeDef,
    ExportImageResultTypeDef,
    ExportTaskS3LocationRequestTypeDef,
    ExportToS3TaskSpecificationTypeDef,
    ExportTransitGatewayRoutesResultTypeDef,
    FilterTypeDef,
    FleetLaunchTemplateConfigRequestTypeDef,
    GetAssociatedEnclaveCertificateIamRolesResultTypeDef,
    GetAssociatedIpv6PoolCidrsResultTypeDef,
    GetCapacityReservationUsageResultTypeDef,
    GetCoipPoolUsageResultTypeDef,
    GetConsoleOutputResultTypeDef,
    GetConsoleScreenshotResultTypeDef,
    GetDefaultCreditSpecificationResultTypeDef,
    GetEbsDefaultKmsKeyIdResultTypeDef,
    GetEbsEncryptionByDefaultResultTypeDef,
    GetFlowLogsIntegrationTemplateResultTypeDef,
    GetGroupsForCapacityReservationResultTypeDef,
    GetHostReservationPurchasePreviewResultTypeDef,
    GetLaunchTemplateDataResultTypeDef,
    GetManagedPrefixListAssociationsResultTypeDef,
    GetManagedPrefixListEntriesResultTypeDef,
    GetPasswordDataResultTypeDef,
    GetReservedInstancesExchangeQuoteResultTypeDef,
    GetSerialConsoleAccessStatusResultTypeDef,
    GetTransitGatewayAttachmentPropagationsResultTypeDef,
    GetTransitGatewayMulticastDomainAssociationsResultTypeDef,
    GetTransitGatewayPrefixListReferencesResultTypeDef,
    GetTransitGatewayRouteTableAssociationsResultTypeDef,
    GetTransitGatewayRouteTablePropagationsResultTypeDef,
    HibernationOptionsRequestTypeDef,
    IamInstanceProfileSpecificationTypeDef,
    IcmpTypeCodeTypeDef,
    ImageAttributeTypeDef,
    ImageDiskContainerTypeDef,
    ImportClientVpnClientCertificateRevocationListResultTypeDef,
    ImportImageLicenseConfigurationRequestTypeDef,
    ImportImageResultTypeDef,
    ImportInstanceLaunchSpecificationTypeDef,
    ImportInstanceResultTypeDef,
    ImportKeyPairResultTypeDef,
    ImportSnapshotResultTypeDef,
    ImportVolumeResultTypeDef,
    InstanceAttributeTypeDef,
    InstanceBlockDeviceMappingSpecificationTypeDef,
    InstanceCreditSpecificationRequestTypeDef,
    InstanceIpv6AddressTypeDef,
    InstanceMarketOptionsRequestTypeDef,
    InstanceMetadataOptionsRequestTypeDef,
    InstanceNetworkInterfaceSpecificationTypeDef,
    InstanceSpecificationTypeDef,
    IntegrateServicesTypeDef,
    IpPermissionTypeDef,
    KeyPairTypeDef,
    LaunchPermissionModificationsTypeDef,
    LaunchTemplateConfigTypeDef,
    LaunchTemplateSpecificationTypeDef,
    LicenseConfigurationRequestTypeDef,
    LoadPermissionModificationsTypeDef,
    ModifyAddressAttributeResultTypeDef,
    ModifyAvailabilityZoneGroupResultTypeDef,
    ModifyCapacityReservationResultTypeDef,
    ModifyClientVpnEndpointResultTypeDef,
    ModifyDefaultCreditSpecificationResultTypeDef,
    ModifyEbsDefaultKmsKeyIdResultTypeDef,
    ModifyFleetResultTypeDef,
    ModifyFpgaImageAttributeResultTypeDef,
    ModifyHostsResultTypeDef,
    ModifyInstanceCapacityReservationAttributesResultTypeDef,
    ModifyInstanceCreditSpecificationResultTypeDef,
    ModifyInstanceEventStartTimeResultTypeDef,
    ModifyInstanceMetadataOptionsResultTypeDef,
    ModifyInstancePlacementResultTypeDef,
    ModifyLaunchTemplateResultTypeDef,
    ModifyManagedPrefixListResultTypeDef,
    ModifyReservedInstancesResultTypeDef,
    ModifySpotFleetRequestResponseTypeDef,
    ModifyTrafficMirrorFilterNetworkServicesResultTypeDef,
    ModifyTrafficMirrorFilterRuleResultTypeDef,
    ModifyTrafficMirrorSessionResultTypeDef,
    ModifyTransitGatewayOptionsTypeDef,
    ModifyTransitGatewayPrefixListReferenceResultTypeDef,
    ModifyTransitGatewayResultTypeDef,
    ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef,
    ModifyTransitGatewayVpcAttachmentResultTypeDef,
    ModifyVolumeResultTypeDef,
    ModifyVpcEndpointConnectionNotificationResultTypeDef,
    ModifyVpcEndpointResultTypeDef,
    ModifyVpcEndpointServiceConfigurationResultTypeDef,
    ModifyVpcEndpointServicePermissionsResultTypeDef,
    ModifyVpcPeeringConnectionOptionsResultTypeDef,
    ModifyVpcTenancyResultTypeDef,
    ModifyVpnConnectionOptionsResultTypeDef,
    ModifyVpnConnectionResultTypeDef,
    ModifyVpnTunnelCertificateResultTypeDef,
    ModifyVpnTunnelOptionsResultTypeDef,
    ModifyVpnTunnelOptionsSpecificationTypeDef,
    MonitorInstancesResultTypeDef,
    MoveAddressToVpcResultTypeDef,
    NetworkInterfaceAttachmentChangesTypeDef,
    NewDhcpConfigurationTypeDef,
    OnDemandOptionsRequestTypeDef,
    PeeringConnectionOptionsRequestTypeDef,
    PlacementTypeDef,
    PortRangeTypeDef,
    PriceScheduleSpecificationTypeDef,
    PrivateIpAddressSpecificationTypeDef,
    ProvisionByoipCidrResultTypeDef,
    PurchaseHostReservationResultTypeDef,
    PurchaseRequestTypeDef,
    PurchaseReservedInstancesOfferingResultTypeDef,
    PurchaseScheduledInstancesResultTypeDef,
    RegisterImageResultTypeDef,
    RegisterInstanceEventNotificationAttributesResultTypeDef,
    RegisterInstanceTagAttributeRequestTypeDef,
    RegisterTransitGatewayMulticastGroupMembersResultTypeDef,
    RegisterTransitGatewayMulticastGroupSourcesResultTypeDef,
    RejectTransitGatewayMulticastDomainAssociationsResultTypeDef,
    RejectTransitGatewayPeeringAttachmentResultTypeDef,
    RejectTransitGatewayVpcAttachmentResultTypeDef,
    RejectVpcEndpointConnectionsResultTypeDef,
    RejectVpcPeeringConnectionResultTypeDef,
    ReleaseHostsResultTypeDef,
    RemovePrefixListEntryTypeDef,
    ReplaceIamInstanceProfileAssociationResultTypeDef,
    ReplaceNetworkAclAssociationResultTypeDef,
    ReplaceRouteTableAssociationResultTypeDef,
    ReplaceTransitGatewayRouteResultTypeDef,
    RequestLaunchTemplateDataTypeDef,
    RequestSpotFleetResponseTypeDef,
    RequestSpotInstancesResultTypeDef,
    RequestSpotLaunchSpecificationTypeDef,
    ReservationTypeDef,
    ReservedInstanceLimitPriceTypeDef,
    ReservedInstancesConfigurationTypeDef,
    ResetAddressAttributeResultTypeDef,
    ResetEbsDefaultKmsKeyIdResultTypeDef,
    ResetFpgaImageAttributeResultTypeDef,
    RestoreAddressToClassicResultTypeDef,
    RestoreManagedPrefixListVersionResultTypeDef,
    RevokeClientVpnIngressResultTypeDef,
    RevokeSecurityGroupEgressResultTypeDef,
    RevokeSecurityGroupIngressResultTypeDef,
    RunInstancesMonitoringEnabledTypeDef,
    RunScheduledInstancesResultTypeDef,
    S3ObjectTagTypeDef,
    ScheduledInstanceRecurrenceRequestTypeDef,
    ScheduledInstancesLaunchSpecificationTypeDef,
    SearchLocalGatewayRoutesResultTypeDef,
    SearchTransitGatewayMulticastGroupsResultTypeDef,
    SearchTransitGatewayRoutesResultTypeDef,
    SlotDateTimeRangeRequestTypeDef,
    SlotStartTimeRangeRequestTypeDef,
    SnapshotDiskContainerTypeDef,
    SnapshotTypeDef,
    SpotFleetRequestConfigDataTypeDef,
    SpotOptionsRequestTypeDef,
    StartInstancesResultTypeDef,
    StartNetworkInsightsAnalysisResultTypeDef,
    StartVpcEndpointServicePrivateDnsVerificationResultTypeDef,
    StopInstancesResultTypeDef,
    StorageLocationTypeDef,
    StorageTypeDef,
    TagSpecificationTypeDef,
    TagTypeDef,
    TargetCapacitySpecificationRequestTypeDef,
    TargetConfigurationRequestTypeDef,
    TerminateClientVpnConnectionsResultTypeDef,
    TerminateInstancesResultTypeDef,
    TrafficMirrorPortRangeRequestTypeDef,
    TransitGatewayConnectRequestBgpOptionsTypeDef,
    TransitGatewayRequestOptionsTypeDef,
    UnassignIpv6AddressesResultTypeDef,
    UnmonitorInstancesResultTypeDef,
    UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef,
    UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef,
    VolumeAttachmentTypeDef,
    VolumeDetailTypeDef,
    VolumeTypeDef,
    VpnConnectionOptionsSpecificationTypeDef,
    WithdrawByoipCidrResultTypeDef,
)
from mypy_boto3_ec2.waiter import (
    BundleTaskCompleteWaiter,
    ConversionTaskCancelledWaiter,
    ConversionTaskCompletedWaiter,
    ConversionTaskDeletedWaiter,
    CustomerGatewayAvailableWaiter,
    ExportTaskCancelledWaiter,
    ExportTaskCompletedWaiter,
    ImageAvailableWaiter,
    ImageExistsWaiter,
    InstanceExistsWaiter,
    InstanceRunningWaiter,
    InstanceStatusOkWaiter,
    InstanceStoppedWaiter,
    InstanceTerminatedWaiter,
    KeyPairExistsWaiter,
    NatGatewayAvailableWaiter,
    NetworkInterfaceAvailableWaiter,
    PasswordDataAvailableWaiter,
    SecurityGroupExistsWaiter,
    SnapshotCompletedWaiter,
    SpotInstanceRequestFulfilledWaiter,
    SubnetAvailableWaiter,
    SystemStatusOkWaiter,
    VolumeAvailableWaiter,
    VolumeDeletedWaiter,
    VolumeInUseWaiter,
    VpcAvailableWaiter,
    VpcExistsWaiter,
    VpcPeeringConnectionDeletedWaiter,
    VpcPeeringConnectionExistsWaiter,
    VpnConnectionAvailableWaiter,
    VpnConnectionDeletedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("EC2Client",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]


class EC2Client:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_reserved_instances_exchange_quote(
        self,
        ReservedInstanceIds: List[str],
        DryRun: bool = None,
        TargetConfigurations: List[TargetConfigurationRequestTypeDef] = None,
    ) -> AcceptReservedInstancesExchangeQuoteResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.accept_reserved_instances_exchange_quote)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#accept-reserved-instances-exchange-quote)
        """

    def accept_transit_gateway_multicast_domain_associations(
        self,
        TransitGatewayMulticastDomainId: str = None,
        TransitGatewayAttachmentId: str = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
    ) -> AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.accept_transit_gateway_multicast_domain_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#accept-transit-gateway-multicast-domain-associations)
        """

    def accept_transit_gateway_peering_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> AcceptTransitGatewayPeeringAttachmentResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.accept_transit_gateway_peering_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#accept-transit-gateway-peering-attachment)
        """

    def accept_transit_gateway_vpc_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> AcceptTransitGatewayVpcAttachmentResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.accept_transit_gateway_vpc_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#accept-transit-gateway-vpc-attachment)
        """

    def accept_vpc_endpoint_connections(
        self, ServiceId: str, VpcEndpointIds: List[str], DryRun: bool = None
    ) -> AcceptVpcEndpointConnectionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.accept_vpc_endpoint_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#accept-vpc-endpoint-connections)
        """

    def accept_vpc_peering_connection(
        self, DryRun: bool = None, VpcPeeringConnectionId: str = None
    ) -> AcceptVpcPeeringConnectionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.accept_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#accept-vpc-peering-connection)
        """

    def advertise_byoip_cidr(
        self, Cidr: str, DryRun: bool = None
    ) -> AdvertiseByoipCidrResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.advertise_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#advertise-byoip-cidr)
        """

    def allocate_address(
        self,
        Domain: DomainType = None,
        Address: str = None,
        PublicIpv4Pool: str = None,
        NetworkBorderGroup: str = None,
        CustomerOwnedIpv4Pool: str = None,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> AllocateAddressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.allocate_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#allocate-address)
        """

    def allocate_hosts(
        self,
        AvailabilityZone: str,
        Quantity: int,
        AutoPlacement: AutoPlacement = None,
        ClientToken: str = None,
        InstanceType: str = None,
        InstanceFamily: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        HostRecovery: HostRecovery = None,
    ) -> AllocateHostsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.allocate_hosts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#allocate-hosts)
        """

    def apply_security_groups_to_client_vpn_target_network(
        self, ClientVpnEndpointId: str, VpcId: str, SecurityGroupIds: List[str], DryRun: bool = None
    ) -> ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.apply_security_groups_to_client_vpn_target_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#apply-security-groups-to-client-vpn-target-network)
        """

    def assign_ipv6_addresses(
        self, NetworkInterfaceId: str, Ipv6AddressCount: int = None, Ipv6Addresses: List[str] = None
    ) -> AssignIpv6AddressesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.assign_ipv6_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#assign-ipv6-addresses)
        """

    def assign_private_ip_addresses(
        self,
        NetworkInterfaceId: str,
        AllowReassignment: bool = None,
        PrivateIpAddresses: List[str] = None,
        SecondaryPrivateIpAddressCount: int = None,
    ) -> AssignPrivateIpAddressesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.assign_private_ip_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#assign-private-ip-addresses)
        """

    def associate_address(
        self,
        AllocationId: str = None,
        InstanceId: str = None,
        PublicIp: str = None,
        AllowReassociation: bool = None,
        DryRun: bool = None,
        NetworkInterfaceId: str = None,
        PrivateIpAddress: str = None,
    ) -> AssociateAddressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.associate_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate-address)
        """

    def associate_client_vpn_target_network(
        self, ClientVpnEndpointId: str, SubnetId: str, ClientToken: str = None, DryRun: bool = None
    ) -> AssociateClientVpnTargetNetworkResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.associate_client_vpn_target_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate-client-vpn-target-network)
        """

    def associate_dhcp_options(self, DhcpOptionsId: str, VpcId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.associate_dhcp_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate-dhcp-options)
        """

    def associate_enclave_certificate_iam_role(
        self, CertificateArn: str = None, RoleArn: str = None, DryRun: bool = None
    ) -> AssociateEnclaveCertificateIamRoleResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.associate_enclave_certificate_iam_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate-enclave-certificate-iam-role)
        """

    def associate_iam_instance_profile(
        self, IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef", InstanceId: str
    ) -> AssociateIamInstanceProfileResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.associate_iam_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate-iam-instance-profile)
        """

    def associate_route_table(
        self, RouteTableId: str, DryRun: bool = None, SubnetId: str = None, GatewayId: str = None
    ) -> AssociateRouteTableResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.associate_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate-route-table)
        """

    def associate_subnet_cidr_block(
        self, SubnetId: str, Ipv6CidrBlock: str
    ) -> AssociateSubnetCidrBlockResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.associate_subnet_cidr_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate-subnet-cidr-block)
        """

    def associate_transit_gateway_multicast_domain(
        self,
        TransitGatewayMulticastDomainId: str = None,
        TransitGatewayAttachmentId: str = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
    ) -> AssociateTransitGatewayMulticastDomainResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.associate_transit_gateway_multicast_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate-transit-gateway-multicast-domain)
        """

    def associate_transit_gateway_route_table(
        self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> AssociateTransitGatewayRouteTableResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.associate_transit_gateway_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate-transit-gateway-route-table)
        """

    def associate_vpc_cidr_block(
        self,
        VpcId: str,
        AmazonProvidedIpv6CidrBlock: bool = None,
        CidrBlock: str = None,
        Ipv6CidrBlockNetworkBorderGroup: str = None,
        Ipv6Pool: str = None,
        Ipv6CidrBlock: str = None,
    ) -> AssociateVpcCidrBlockResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.associate_vpc_cidr_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate-vpc-cidr-block)
        """

    def attach_classic_link_vpc(
        self, Groups: List[str], InstanceId: str, VpcId: str, DryRun: bool = None
    ) -> AttachClassicLinkVpcResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.attach_classic_link_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#attach-classic-link-vpc)
        """

    def attach_internet_gateway(
        self, InternetGatewayId: str, VpcId: str, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.attach_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#attach-internet-gateway)
        """

    def attach_network_interface(
        self,
        DeviceIndex: int,
        InstanceId: str,
        NetworkInterfaceId: str,
        DryRun: bool = None,
        NetworkCardIndex: int = None,
    ) -> AttachNetworkInterfaceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.attach_network_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#attach-network-interface)
        """

    def attach_volume(
        self, Device: str, InstanceId: str, VolumeId: str, DryRun: bool = None
    ) -> "VolumeAttachmentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.attach_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#attach-volume)
        """

    def attach_vpn_gateway(
        self, VpcId: str, VpnGatewayId: str, DryRun: bool = None
    ) -> AttachVpnGatewayResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.attach_vpn_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#attach-vpn-gateway)
        """

    def authorize_client_vpn_ingress(
        self,
        ClientVpnEndpointId: str,
        TargetNetworkCidr: str,
        AccessGroupId: str = None,
        AuthorizeAllGroups: bool = None,
        Description: str = None,
        ClientToken: str = None,
        DryRun: bool = None,
    ) -> AuthorizeClientVpnIngressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.authorize_client_vpn_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#authorize-client-vpn-ingress)
        """

    def authorize_security_group_egress(
        self,
        GroupId: str,
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.authorize_security_group_egress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#authorize-security-group-egress)
        """

    def authorize_security_group_ingress(
        self,
        CidrIp: str = None,
        FromPort: int = None,
        GroupId: str = None,
        GroupName: str = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.authorize_security_group_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#authorize-security-group-ingress)
        """

    def bundle_instance(
        self, InstanceId: str, Storage: "StorageTypeDef", DryRun: bool = None
    ) -> BundleInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.bundle_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#bundle-instance)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#can-paginate)
        """

    def cancel_bundle_task(
        self, BundleId: str, DryRun: bool = None
    ) -> CancelBundleTaskResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.cancel_bundle_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel-bundle-task)
        """

    def cancel_capacity_reservation(
        self, CapacityReservationId: str, DryRun: bool = None
    ) -> CancelCapacityReservationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.cancel_capacity_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel-capacity-reservation)
        """

    def cancel_conversion_task(
        self, ConversionTaskId: str, DryRun: bool = None, ReasonMessage: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.cancel_conversion_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel-conversion-task)
        """

    def cancel_export_task(self, ExportTaskId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.cancel_export_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel-export-task)
        """

    def cancel_import_task(
        self, CancelReason: str = None, DryRun: bool = None, ImportTaskId: str = None
    ) -> CancelImportTaskResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.cancel_import_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel-import-task)
        """

    def cancel_reserved_instances_listing(
        self, ReservedInstancesListingId: str
    ) -> CancelReservedInstancesListingResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.cancel_reserved_instances_listing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel-reserved-instances-listing)
        """

    def cancel_spot_fleet_requests(
        self, SpotFleetRequestIds: List[str], TerminateInstances: bool, DryRun: bool = None
    ) -> CancelSpotFleetRequestsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.cancel_spot_fleet_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel-spot-fleet-requests)
        """

    def cancel_spot_instance_requests(
        self, SpotInstanceRequestIds: List[str], DryRun: bool = None
    ) -> CancelSpotInstanceRequestsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.cancel_spot_instance_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel-spot-instance-requests)
        """

    def confirm_product_instance(
        self, InstanceId: str, ProductCode: str, DryRun: bool = None
    ) -> ConfirmProductInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.confirm_product_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#confirm-product-instance)
        """

    def copy_fpga_image(
        self,
        SourceFpgaImageId: str,
        SourceRegion: str,
        DryRun: bool = None,
        Description: str = None,
        Name: str = None,
        ClientToken: str = None,
    ) -> CopyFpgaImageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.copy_fpga_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#copy-fpga-image)
        """

    def copy_image(
        self,
        Name: str,
        SourceImageId: str,
        SourceRegion: str,
        ClientToken: str = None,
        Description: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        DestinationOutpostArn: str = None,
        DryRun: bool = None,
    ) -> CopyImageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.copy_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#copy-image)
        """

    def copy_snapshot(
        self,
        SourceRegion: str,
        SourceSnapshotId: str,
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.copy_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#copy-snapshot)
        """

    def create_capacity_reservation(
        self,
        InstanceType: str,
        InstancePlatform: CapacityReservationInstancePlatform,
        InstanceCount: int,
        ClientToken: str = None,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Tenancy: CapacityReservationTenancy = None,
        EbsOptimized: bool = None,
        EphemeralStorage: bool = None,
        EndDate: datetime = None,
        EndDateType: EndDateType = None,
        InstanceMatchCriteria: InstanceMatchCriteria = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> CreateCapacityReservationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_capacity_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-capacity-reservation)
        """

    def create_carrier_gateway(
        self,
        VpcId: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> CreateCarrierGatewayResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_carrier_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-carrier-gateway)
        """

    def create_client_vpn_endpoint(
        self,
        ClientCidrBlock: str,
        ServerCertificateArn: str,
        AuthenticationOptions: List[ClientVpnAuthenticationRequestTypeDef],
        ConnectionLogOptions: ConnectionLogOptionsTypeDef,
        DnsServers: List[str] = None,
        TransportProtocol: TransportProtocol = None,
        VpnPort: int = None,
        Description: str = None,
        SplitTunnel: bool = None,
        DryRun: bool = None,
        ClientToken: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        SecurityGroupIds: List[str] = None,
        VpcId: str = None,
        SelfServicePortal: SelfServicePortal = None,
        ClientConnectOptions: ClientConnectOptionsTypeDef = None,
    ) -> CreateClientVpnEndpointResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_client_vpn_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-client-vpn-endpoint)
        """

    def create_client_vpn_route(
        self,
        ClientVpnEndpointId: str,
        DestinationCidrBlock: str,
        TargetVpcSubnetId: str,
        Description: str = None,
        ClientToken: str = None,
        DryRun: bool = None,
    ) -> CreateClientVpnRouteResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_client_vpn_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-client-vpn-route)
        """

    def create_customer_gateway(
        self,
        BgpAsn: int,
        Type: Literal["ipsec.1"],
        PublicIp: str = None,
        CertificateArn: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DeviceName: str = None,
        DryRun: bool = None,
    ) -> CreateCustomerGatewayResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_customer_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-customer-gateway)
        """

    def create_default_subnet(
        self, AvailabilityZone: str, DryRun: bool = None
    ) -> CreateDefaultSubnetResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_default_subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-default-subnet)
        """

    def create_default_vpc(self, DryRun: bool = None) -> CreateDefaultVpcResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_default_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-default-vpc)
        """

    def create_dhcp_options(
        self,
        DhcpConfigurations: List[NewDhcpConfigurationTypeDef],
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> CreateDhcpOptionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_dhcp_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-dhcp-options)
        """

    def create_egress_only_internet_gateway(
        self,
        VpcId: str,
        ClientToken: str = None,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> CreateEgressOnlyInternetGatewayResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_egress_only_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-egress-only-internet-gateway)
        """

    def create_fleet(
        self,
        LaunchTemplateConfigs: List[FleetLaunchTemplateConfigRequestTypeDef],
        TargetCapacitySpecification: TargetCapacitySpecificationRequestTypeDef,
        DryRun: bool = None,
        ClientToken: str = None,
        SpotOptions: SpotOptionsRequestTypeDef = None,
        OnDemandOptions: OnDemandOptionsRequestTypeDef = None,
        ExcessCapacityTerminationPolicy: FleetExcessCapacityTerminationPolicy = None,
        TerminateInstancesWithExpiration: bool = None,
        Type: FleetType = None,
        ValidFrom: datetime = None,
        ValidUntil: datetime = None,
        ReplaceUnhealthyInstances: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> CreateFleetResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-fleet)
        """

    def create_flow_logs(
        self,
        ResourceIds: List[str],
        ResourceType: FlowLogsResourceType,
        TrafficType: TrafficType,
        DryRun: bool = None,
        ClientToken: str = None,
        DeliverLogsPermissionArn: str = None,
        LogGroupName: str = None,
        LogDestinationType: LogDestinationType = None,
        LogDestination: str = None,
        LogFormat: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        MaxAggregationInterval: int = None,
    ) -> CreateFlowLogsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_flow_logs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-flow-logs)
        """

    def create_fpga_image(
        self,
        InputStorageLocation: StorageLocationTypeDef,
        DryRun: bool = None,
        LogsStorageLocation: StorageLocationTypeDef = None,
        Description: str = None,
        Name: str = None,
        ClientToken: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> CreateFpgaImageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_fpga_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-fpga-image)
        """

    def create_image(
        self,
        InstanceId: str,
        Name: str,
        BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
        Description: str = None,
        DryRun: bool = None,
        NoReboot: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> CreateImageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-image)
        """

    def create_instance_export_task(
        self,
        ExportToS3Task: ExportToS3TaskSpecificationTypeDef,
        InstanceId: str,
        TargetEnvironment: ExportEnvironment,
        Description: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> CreateInstanceExportTaskResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_instance_export_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-instance-export-task)
        """

    def create_internet_gateway(
        self, TagSpecifications: List["TagSpecificationTypeDef"] = None, DryRun: bool = None
    ) -> CreateInternetGatewayResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-internet-gateway)
        """

    def create_key_pair(
        self,
        KeyName: str,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> KeyPairTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-key-pair)
        """

    def create_launch_template(
        self,
        LaunchTemplateName: str,
        LaunchTemplateData: RequestLaunchTemplateDataTypeDef,
        DryRun: bool = None,
        ClientToken: str = None,
        VersionDescription: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> CreateLaunchTemplateResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_launch_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-launch-template)
        """

    def create_launch_template_version(
        self,
        LaunchTemplateData: RequestLaunchTemplateDataTypeDef,
        DryRun: bool = None,
        ClientToken: str = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        SourceVersion: str = None,
        VersionDescription: str = None,
    ) -> CreateLaunchTemplateVersionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_launch_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-launch-template-version)
        """

    def create_local_gateway_route(
        self,
        DestinationCidrBlock: str,
        LocalGatewayRouteTableId: str,
        LocalGatewayVirtualInterfaceGroupId: str,
        DryRun: bool = None,
    ) -> CreateLocalGatewayRouteResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_local_gateway_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-local-gateway-route)
        """

    def create_local_gateway_route_table_vpc_association(
        self,
        LocalGatewayRouteTableId: str,
        VpcId: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> CreateLocalGatewayRouteTableVpcAssociationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_local_gateway_route_table_vpc_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-local-gateway-route-table-vpc-association)
        """

    def create_managed_prefix_list(
        self,
        PrefixListName: str,
        MaxEntries: int,
        AddressFamily: str,
        DryRun: bool = None,
        Entries: List[AddPrefixListEntryTypeDef] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None,
    ) -> CreateManagedPrefixListResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_managed_prefix_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-managed-prefix-list)
        """

    def create_nat_gateway(
        self,
        SubnetId: str,
        AllocationId: str,
        ClientToken: str = None,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> CreateNatGatewayResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_nat_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-nat-gateway)
        """

    def create_network_acl(
        self,
        VpcId: str,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> CreateNetworkAclResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_network_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-network-acl)
        """

    def create_network_acl_entry(
        self,
        Egress: bool,
        NetworkAclId: str,
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_network_acl_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-network-acl-entry)
        """

    def create_network_insights_path(
        self,
        Source: str,
        Destination: str,
        Protocol: ProtocolType,
        ClientToken: str,
        SourceIp: str = None,
        DestinationIp: str = None,
        DestinationPort: int = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> CreateNetworkInsightsPathResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_network_insights_path)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-network-insights-path)
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
    ) -> CreateNetworkInterfaceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_network_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-network-interface)
        """

    def create_network_interface_permission(
        self,
        NetworkInterfaceId: str,
        Permission: InterfacePermissionType,
        AwsAccountId: str = None,
        AwsService: str = None,
        DryRun: bool = None,
    ) -> CreateNetworkInterfacePermissionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_network_interface_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-network-interface-permission)
        """

    def create_placement_group(
        self,
        DryRun: bool = None,
        GroupName: str = None,
        Strategy: PlacementStrategy = None,
        PartitionCount: int = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> CreatePlacementGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_placement_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-placement-group)
        """

    def create_replace_root_volume_task(
        self,
        InstanceId: str,
        SnapshotId: str = None,
        ClientToken: str = None,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> CreateReplaceRootVolumeTaskResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_replace_root_volume_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-replace-root-volume-task)
        """

    def create_reserved_instances_listing(
        self,
        ClientToken: str,
        InstanceCount: int,
        PriceSchedules: List[PriceScheduleSpecificationTypeDef],
        ReservedInstancesId: str,
    ) -> CreateReservedInstancesListingResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_reserved_instances_listing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-reserved-instances-listing)
        """

    def create_restore_image_task(
        self,
        Bucket: str,
        ObjectKey: str,
        Name: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> CreateRestoreImageTaskResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_restore_image_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-restore-image-task)
        """

    def create_route(
        self,
        RouteTableId: str,
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
    ) -> CreateRouteResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-route)
        """

    def create_route_table(
        self,
        VpcId: str,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> CreateRouteTableResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-route-table)
        """

    def create_security_group(
        self,
        Description: str,
        GroupName: str,
        VpcId: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> CreateSecurityGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-security-group)
        """

    def create_snapshot(
        self,
        VolumeId: str,
        Description: str = None,
        OutpostArn: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> "SnapshotTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-snapshot)
        """

    def create_snapshots(
        self,
        InstanceSpecification: InstanceSpecificationTypeDef,
        Description: str = None,
        OutpostArn: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
        CopyTagsFromSource: Literal["volume"] = None,
    ) -> CreateSnapshotsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-snapshots)
        """

    def create_spot_datafeed_subscription(
        self, Bucket: str, DryRun: bool = None, Prefix: str = None
    ) -> CreateSpotDatafeedSubscriptionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_spot_datafeed_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-spot-datafeed-subscription)
        """

    def create_store_image_task(
        self,
        ImageId: str,
        Bucket: str,
        S3ObjectTags: List[S3ObjectTagTypeDef] = None,
        DryRun: bool = None,
    ) -> CreateStoreImageTaskResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_store_image_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-store-image-task)
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
    ) -> CreateSubnetResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-subnet)
        """

    def create_tags(
        self, Resources: List[Any], Tags: Optional[List[TagTypeDef]], DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-tags)
        """

    def create_traffic_mirror_filter(
        self,
        Description: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> CreateTrafficMirrorFilterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_traffic_mirror_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-traffic-mirror-filter)
        """

    def create_traffic_mirror_filter_rule(
        self,
        TrafficMirrorFilterId: str,
        TrafficDirection: TrafficDirection,
        RuleNumber: int,
        RuleAction: TrafficMirrorRuleAction,
        DestinationCidrBlock: str,
        SourceCidrBlock: str,
        DestinationPortRange: TrafficMirrorPortRangeRequestTypeDef = None,
        SourcePortRange: TrafficMirrorPortRangeRequestTypeDef = None,
        Protocol: int = None,
        Description: str = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> CreateTrafficMirrorFilterRuleResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_traffic_mirror_filter_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-traffic-mirror-filter-rule)
        """

    def create_traffic_mirror_session(
        self,
        NetworkInterfaceId: str,
        TrafficMirrorTargetId: str,
        TrafficMirrorFilterId: str,
        SessionNumber: int,
        PacketLength: int = None,
        VirtualNetworkId: int = None,
        Description: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> CreateTrafficMirrorSessionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_traffic_mirror_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-traffic-mirror-session)
        """

    def create_traffic_mirror_target(
        self,
        NetworkInterfaceId: str = None,
        NetworkLoadBalancerArn: str = None,
        Description: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> CreateTrafficMirrorTargetResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_traffic_mirror_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-traffic-mirror-target)
        """

    def create_transit_gateway(
        self,
        Description: str = None,
        Options: TransitGatewayRequestOptionsTypeDef = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> CreateTransitGatewayResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_transit_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-transit-gateway)
        """

    def create_transit_gateway_connect(
        self,
        TransportTransitGatewayAttachmentId: str,
        Options: CreateTransitGatewayConnectRequestOptionsTypeDef,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> CreateTransitGatewayConnectResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_transit_gateway_connect)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-transit-gateway-connect)
        """

    def create_transit_gateway_connect_peer(
        self,
        TransitGatewayAttachmentId: str,
        PeerAddress: str,
        InsideCidrBlocks: List[str],
        TransitGatewayAddress: str = None,
        BgpOptions: TransitGatewayConnectRequestBgpOptionsTypeDef = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> CreateTransitGatewayConnectPeerResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_transit_gateway_connect_peer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-transit-gateway-connect-peer)
        """

    def create_transit_gateway_multicast_domain(
        self,
        TransitGatewayId: str,
        Options: CreateTransitGatewayMulticastDomainRequestOptionsTypeDef = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> CreateTransitGatewayMulticastDomainResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_transit_gateway_multicast_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-transit-gateway-multicast-domain)
        """

    def create_transit_gateway_peering_attachment(
        self,
        TransitGatewayId: str,
        PeerTransitGatewayId: str,
        PeerAccountId: str,
        PeerRegion: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> CreateTransitGatewayPeeringAttachmentResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_transit_gateway_peering_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-transit-gateway-peering-attachment)
        """

    def create_transit_gateway_prefix_list_reference(
        self,
        TransitGatewayRouteTableId: str,
        PrefixListId: str,
        TransitGatewayAttachmentId: str = None,
        Blackhole: bool = None,
        DryRun: bool = None,
    ) -> CreateTransitGatewayPrefixListReferenceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_transit_gateway_prefix_list_reference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-transit-gateway-prefix-list-reference)
        """

    def create_transit_gateway_route(
        self,
        DestinationCidrBlock: str,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str = None,
        Blackhole: bool = None,
        DryRun: bool = None,
    ) -> CreateTransitGatewayRouteResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_transit_gateway_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-transit-gateway-route)
        """

    def create_transit_gateway_route_table(
        self,
        TransitGatewayId: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> CreateTransitGatewayRouteTableResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_transit_gateway_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-transit-gateway-route-table)
        """

    def create_transit_gateway_vpc_attachment(
        self,
        TransitGatewayId: str,
        VpcId: str,
        SubnetIds: List[str],
        Options: CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
    ) -> CreateTransitGatewayVpcAttachmentResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_transit_gateway_vpc_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-transit-gateway-vpc-attachment)
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
    ) -> "VolumeTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-volume)
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
    ) -> CreateVpcResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-vpc)
        """

    def create_vpc_endpoint(
        self,
        VpcId: str,
        ServiceName: str,
        DryRun: bool = None,
        VpcEndpointType: VpcEndpointType = None,
        PolicyDocument: str = None,
        RouteTableIds: List[str] = None,
        SubnetIds: List[str] = None,
        SecurityGroupIds: List[str] = None,
        ClientToken: str = None,
        PrivateDnsEnabled: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> CreateVpcEndpointResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_vpc_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-vpc-endpoint)
        """

    def create_vpc_endpoint_connection_notification(
        self,
        ConnectionNotificationArn: str,
        ConnectionEvents: List[str],
        DryRun: bool = None,
        ServiceId: str = None,
        VpcEndpointId: str = None,
        ClientToken: str = None,
    ) -> CreateVpcEndpointConnectionNotificationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_vpc_endpoint_connection_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-vpc-endpoint-connection-notification)
        """

    def create_vpc_endpoint_service_configuration(
        self,
        DryRun: bool = None,
        AcceptanceRequired: bool = None,
        PrivateDnsName: str = None,
        NetworkLoadBalancerArns: List[str] = None,
        GatewayLoadBalancerArns: List[str] = None,
        ClientToken: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> CreateVpcEndpointServiceConfigurationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_vpc_endpoint_service_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-vpc-endpoint-service-configuration)
        """

    def create_vpc_peering_connection(
        self,
        DryRun: bool = None,
        PeerOwnerId: str = None,
        PeerVpcId: str = None,
        VpcId: str = None,
        PeerRegion: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> CreateVpcPeeringConnectionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-vpc-peering-connection)
        """

    def create_vpn_connection(
        self,
        CustomerGatewayId: str,
        Type: str,
        VpnGatewayId: str = None,
        TransitGatewayId: str = None,
        DryRun: bool = None,
        Options: VpnConnectionOptionsSpecificationTypeDef = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> CreateVpnConnectionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_vpn_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-vpn-connection)
        """

    def create_vpn_connection_route(self, DestinationCidrBlock: str, VpnConnectionId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_vpn_connection_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-vpn-connection-route)
        """

    def create_vpn_gateway(
        self,
        Type: Literal["ipsec.1"],
        AvailabilityZone: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        AmazonSideAsn: int = None,
        DryRun: bool = None,
    ) -> CreateVpnGatewayResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.create_vpn_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create-vpn-gateway)
        """

    def delete_carrier_gateway(
        self, CarrierGatewayId: str, DryRun: bool = None
    ) -> DeleteCarrierGatewayResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_carrier_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-carrier-gateway)
        """

    def delete_client_vpn_endpoint(
        self, ClientVpnEndpointId: str, DryRun: bool = None
    ) -> DeleteClientVpnEndpointResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_client_vpn_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-client-vpn-endpoint)
        """

    def delete_client_vpn_route(
        self,
        ClientVpnEndpointId: str,
        DestinationCidrBlock: str,
        TargetVpcSubnetId: str = None,
        DryRun: bool = None,
    ) -> DeleteClientVpnRouteResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_client_vpn_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-client-vpn-route)
        """

    def delete_customer_gateway(self, CustomerGatewayId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_customer_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-customer-gateway)
        """

    def delete_dhcp_options(self, DhcpOptionsId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_dhcp_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-dhcp-options)
        """

    def delete_egress_only_internet_gateway(
        self, EgressOnlyInternetGatewayId: str, DryRun: bool = None
    ) -> DeleteEgressOnlyInternetGatewayResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_egress_only_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-egress-only-internet-gateway)
        """

    def delete_fleets(
        self, FleetIds: List[str], TerminateInstances: bool, DryRun: bool = None
    ) -> DeleteFleetsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-fleets)
        """

    def delete_flow_logs(
        self, FlowLogIds: List[str], DryRun: bool = None
    ) -> DeleteFlowLogsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_flow_logs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-flow-logs)
        """

    def delete_fpga_image(
        self, FpgaImageId: str, DryRun: bool = None
    ) -> DeleteFpgaImageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_fpga_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-fpga-image)
        """

    def delete_internet_gateway(self, InternetGatewayId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-internet-gateway)
        """

    def delete_key_pair(
        self, KeyName: str = None, KeyPairId: str = None, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-key-pair)
        """

    def delete_launch_template(
        self, DryRun: bool = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None
    ) -> DeleteLaunchTemplateResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_launch_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-launch-template)
        """

    def delete_launch_template_versions(
        self,
        Versions: List[str],
        DryRun: bool = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
    ) -> DeleteLaunchTemplateVersionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_launch_template_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-launch-template-versions)
        """

    def delete_local_gateway_route(
        self, DestinationCidrBlock: str, LocalGatewayRouteTableId: str, DryRun: bool = None
    ) -> DeleteLocalGatewayRouteResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_local_gateway_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-local-gateway-route)
        """

    def delete_local_gateway_route_table_vpc_association(
        self, LocalGatewayRouteTableVpcAssociationId: str, DryRun: bool = None
    ) -> DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_local_gateway_route_table_vpc_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-local-gateway-route-table-vpc-association)
        """

    def delete_managed_prefix_list(
        self, PrefixListId: str, DryRun: bool = None
    ) -> DeleteManagedPrefixListResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_managed_prefix_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-managed-prefix-list)
        """

    def delete_nat_gateway(
        self, NatGatewayId: str, DryRun: bool = None
    ) -> DeleteNatGatewayResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_nat_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-nat-gateway)
        """

    def delete_network_acl(self, NetworkAclId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_network_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-network-acl)
        """

    def delete_network_acl_entry(
        self, Egress: bool, NetworkAclId: str, RuleNumber: int, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_network_acl_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-network-acl-entry)
        """

    def delete_network_insights_analysis(
        self, NetworkInsightsAnalysisId: str, DryRun: bool = None
    ) -> DeleteNetworkInsightsAnalysisResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_network_insights_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-network-insights-analysis)
        """

    def delete_network_insights_path(
        self, NetworkInsightsPathId: str, DryRun: bool = None
    ) -> DeleteNetworkInsightsPathResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_network_insights_path)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-network-insights-path)
        """

    def delete_network_interface(self, NetworkInterfaceId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_network_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-network-interface)
        """

    def delete_network_interface_permission(
        self, NetworkInterfacePermissionId: str, Force: bool = None, DryRun: bool = None
    ) -> DeleteNetworkInterfacePermissionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_network_interface_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-network-interface-permission)
        """

    def delete_placement_group(self, GroupName: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_placement_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-placement-group)
        """

    def delete_queued_reserved_instances(
        self, ReservedInstancesIds: List[str], DryRun: bool = None
    ) -> DeleteQueuedReservedInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_queued_reserved_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-queued-reserved-instances)
        """

    def delete_route(
        self,
        RouteTableId: str,
        DestinationCidrBlock: str = None,
        DestinationIpv6CidrBlock: str = None,
        DestinationPrefixListId: str = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-route)
        """

    def delete_route_table(self, RouteTableId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-route-table)
        """

    def delete_security_group(
        self, GroupId: str = None, GroupName: str = None, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-security-group)
        """

    def delete_snapshot(self, SnapshotId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-snapshot)
        """

    def delete_spot_datafeed_subscription(self, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_spot_datafeed_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-spot-datafeed-subscription)
        """

    def delete_subnet(self, SubnetId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-subnet)
        """

    def delete_tags(
        self, Resources: List[Any], DryRun: bool = None, Tags: Optional[List[TagTypeDef]] = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-tags)
        """

    def delete_traffic_mirror_filter(
        self, TrafficMirrorFilterId: str, DryRun: bool = None
    ) -> DeleteTrafficMirrorFilterResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-traffic-mirror-filter)
        """

    def delete_traffic_mirror_filter_rule(
        self, TrafficMirrorFilterRuleId: str, DryRun: bool = None
    ) -> DeleteTrafficMirrorFilterRuleResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_filter_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-traffic-mirror-filter-rule)
        """

    def delete_traffic_mirror_session(
        self, TrafficMirrorSessionId: str, DryRun: bool = None
    ) -> DeleteTrafficMirrorSessionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-traffic-mirror-session)
        """

    def delete_traffic_mirror_target(
        self, TrafficMirrorTargetId: str, DryRun: bool = None
    ) -> DeleteTrafficMirrorTargetResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-traffic-mirror-target)
        """

    def delete_transit_gateway(
        self, TransitGatewayId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_transit_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-transit-gateway)
        """

    def delete_transit_gateway_connect(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayConnectResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_transit_gateway_connect)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-transit-gateway-connect)
        """

    def delete_transit_gateway_connect_peer(
        self, TransitGatewayConnectPeerId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayConnectPeerResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_transit_gateway_connect_peer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-transit-gateway-connect-peer)
        """

    def delete_transit_gateway_multicast_domain(
        self, TransitGatewayMulticastDomainId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayMulticastDomainResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_transit_gateway_multicast_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-transit-gateway-multicast-domain)
        """

    def delete_transit_gateway_peering_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayPeeringAttachmentResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_transit_gateway_peering_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-transit-gateway-peering-attachment)
        """

    def delete_transit_gateway_prefix_list_reference(
        self, TransitGatewayRouteTableId: str, PrefixListId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayPrefixListReferenceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_transit_gateway_prefix_list_reference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-transit-gateway-prefix-list-reference)
        """

    def delete_transit_gateway_route(
        self, TransitGatewayRouteTableId: str, DestinationCidrBlock: str, DryRun: bool = None
    ) -> DeleteTransitGatewayRouteResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_transit_gateway_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-transit-gateway-route)
        """

    def delete_transit_gateway_route_table(
        self, TransitGatewayRouteTableId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayRouteTableResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_transit_gateway_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-transit-gateway-route-table)
        """

    def delete_transit_gateway_vpc_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayVpcAttachmentResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_transit_gateway_vpc_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-transit-gateway-vpc-attachment)
        """

    def delete_volume(self, VolumeId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-volume)
        """

    def delete_vpc(self, VpcId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-vpc)
        """

    def delete_vpc_endpoint_connection_notifications(
        self, ConnectionNotificationIds: List[str], DryRun: bool = None
    ) -> DeleteVpcEndpointConnectionNotificationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_vpc_endpoint_connection_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-vpc-endpoint-connection-notifications)
        """

    def delete_vpc_endpoint_service_configurations(
        self, ServiceIds: List[str], DryRun: bool = None
    ) -> DeleteVpcEndpointServiceConfigurationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_vpc_endpoint_service_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-vpc-endpoint-service-configurations)
        """

    def delete_vpc_endpoints(
        self, VpcEndpointIds: List[str], DryRun: bool = None
    ) -> DeleteVpcEndpointsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_vpc_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-vpc-endpoints)
        """

    def delete_vpc_peering_connection(
        self, VpcPeeringConnectionId: str, DryRun: bool = None
    ) -> DeleteVpcPeeringConnectionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-vpc-peering-connection)
        """

    def delete_vpn_connection(self, VpnConnectionId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_vpn_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-vpn-connection)
        """

    def delete_vpn_connection_route(self, DestinationCidrBlock: str, VpnConnectionId: str) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_vpn_connection_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-vpn-connection-route)
        """

    def delete_vpn_gateway(self, VpnGatewayId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.delete_vpn_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete-vpn-gateway)
        """

    def deprovision_byoip_cidr(
        self, Cidr: str, DryRun: bool = None
    ) -> DeprovisionByoipCidrResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.deprovision_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#deprovision-byoip-cidr)
        """

    def deregister_image(self, ImageId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.deregister_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#deregister-image)
        """

    def deregister_instance_event_notification_attributes(
        self,
        DryRun: bool = None,
        InstanceTagAttribute: DeregisterInstanceTagAttributeRequestTypeDef = None,
    ) -> DeregisterInstanceEventNotificationAttributesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.deregister_instance_event_notification_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#deregister-instance-event-notification-attributes)
        """

    def deregister_transit_gateway_multicast_group_members(
        self,
        TransitGatewayMulticastDomainId: str = None,
        GroupIpAddress: str = None,
        NetworkInterfaceIds: List[str] = None,
        DryRun: bool = None,
    ) -> DeregisterTransitGatewayMulticastGroupMembersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.deregister_transit_gateway_multicast_group_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#deregister-transit-gateway-multicast-group-members)
        """

    def deregister_transit_gateway_multicast_group_sources(
        self,
        TransitGatewayMulticastDomainId: str = None,
        GroupIpAddress: str = None,
        NetworkInterfaceIds: List[str] = None,
        DryRun: bool = None,
    ) -> DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.deregister_transit_gateway_multicast_group_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#deregister-transit-gateway-multicast-group-sources)
        """

    def describe_account_attributes(
        self, AttributeNames: List[AccountAttributeName] = None, DryRun: bool = None
    ) -> DescribeAccountAttributesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_account_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-account-attributes)
        """

    def describe_addresses(
        self,
        Filters: List[FilterTypeDef] = None,
        PublicIps: List[str] = None,
        AllocationIds: List[str] = None,
        DryRun: bool = None,
    ) -> DescribeAddressesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-addresses)
        """

    def describe_addresses_attribute(
        self,
        AllocationIds: List[str] = None,
        Attribute: Literal["domain-name"] = None,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None,
    ) -> DescribeAddressesAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_addresses_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-addresses-attribute)
        """

    def describe_aggregate_id_format(
        self, DryRun: bool = None
    ) -> DescribeAggregateIdFormatResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_aggregate_id_format)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-aggregate-id-format)
        """

    def describe_availability_zones(
        self,
        Filters: List[FilterTypeDef] = None,
        ZoneNames: List[str] = None,
        ZoneIds: List[str] = None,
        AllAvailabilityZones: bool = None,
        DryRun: bool = None,
    ) -> DescribeAvailabilityZonesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_availability_zones)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-availability-zones)
        """

    def describe_bundle_tasks(
        self, BundleIds: List[str] = None, Filters: List[FilterTypeDef] = None, DryRun: bool = None
    ) -> DescribeBundleTasksResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_bundle_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-bundle-tasks)
        """

    def describe_byoip_cidrs(
        self, MaxResults: int, DryRun: bool = None, NextToken: str = None
    ) -> DescribeByoipCidrsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_byoip_cidrs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-byoip-cidrs)
        """

    def describe_capacity_reservations(
        self,
        CapacityReservationIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
    ) -> DescribeCapacityReservationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_capacity_reservations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-capacity-reservations)
        """

    def describe_carrier_gateways(
        self,
        CarrierGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeCarrierGatewaysResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_carrier_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-carrier-gateways)
        """

    def describe_classic_link_instances(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeClassicLinkInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_classic_link_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-classic-link-instances)
        """

    def describe_client_vpn_authorization_rules(
        self,
        ClientVpnEndpointId: str,
        DryRun: bool = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
    ) -> DescribeClientVpnAuthorizationRulesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_client_vpn_authorization_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-client-vpn-authorization-rules)
        """

    def describe_client_vpn_connections(
        self,
        ClientVpnEndpointId: str,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None,
    ) -> DescribeClientVpnConnectionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_client_vpn_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-client-vpn-connections)
        """

    def describe_client_vpn_endpoints(
        self,
        ClientVpnEndpointIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
    ) -> DescribeClientVpnEndpointsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_client_vpn_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-client-vpn-endpoints)
        """

    def describe_client_vpn_routes(
        self,
        ClientVpnEndpointId: str,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeClientVpnRoutesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_client_vpn_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-client-vpn-routes)
        """

    def describe_client_vpn_target_networks(
        self,
        ClientVpnEndpointId: str,
        AssociationIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
    ) -> DescribeClientVpnTargetNetworksResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_client_vpn_target_networks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-client-vpn-target-networks)
        """

    def describe_coip_pools(
        self,
        PoolIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeCoipPoolsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_coip_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-coip-pools)
        """

    def describe_conversion_tasks(
        self, ConversionTaskIds: List[str] = None, DryRun: bool = None
    ) -> DescribeConversionTasksResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_conversion_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-conversion-tasks)
        """

    def describe_customer_gateways(
        self,
        CustomerGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
    ) -> DescribeCustomerGatewaysResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_customer_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-customer-gateways)
        """

    def describe_dhcp_options(
        self,
        DhcpOptionsIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeDhcpOptionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_dhcp_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-dhcp-options)
        """

    def describe_egress_only_internet_gateways(
        self,
        DryRun: bool = None,
        EgressOnlyInternetGatewayIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> DescribeEgressOnlyInternetGatewaysResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_egress_only_internet_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-egress-only-internet-gateways)
        """

    def describe_elastic_gpus(
        self,
        ElasticGpuIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeElasticGpusResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_elastic_gpus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-elastic-gpus)
        """

    def describe_export_image_tasks(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ExportImageTaskIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeExportImageTasksResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_export_image_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-export-image-tasks)
        """

    def describe_export_tasks(
        self, ExportTaskIds: List[str] = None, Filters: List[FilterTypeDef] = None
    ) -> DescribeExportTasksResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_export_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-export-tasks)
        """

    def describe_fast_snapshot_restores(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeFastSnapshotRestoresResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_fast_snapshot_restores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-fast-snapshot-restores)
        """

    def describe_fleet_history(
        self,
        FleetId: str,
        StartTime: datetime,
        DryRun: bool = None,
        EventType: FleetEventType = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeFleetHistoryResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_fleet_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-fleet-history)
        """

    def describe_fleet_instances(
        self,
        FleetId: str,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List[FilterTypeDef] = None,
    ) -> DescribeFleetInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_fleet_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-fleet-instances)
        """

    def describe_fleets(
        self,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        FleetIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
    ) -> DescribeFleetsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-fleets)
        """

    def describe_flow_logs(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        FlowLogIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeFlowLogsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_flow_logs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-flow-logs)
        """

    def describe_fpga_image_attribute(
        self, FpgaImageId: str, Attribute: FpgaImageAttributeName, DryRun: bool = None
    ) -> DescribeFpgaImageAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_fpga_image_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-fpga-image-attribute)
        """

    def describe_fpga_images(
        self,
        DryRun: bool = None,
        FpgaImageIds: List[str] = None,
        Owners: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeFpgaImagesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_fpga_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-fpga-images)
        """

    def describe_host_reservation_offerings(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxDuration: int = None,
        MaxResults: int = None,
        MinDuration: int = None,
        NextToken: str = None,
        OfferingId: str = None,
    ) -> DescribeHostReservationOfferingsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_host_reservation_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-host-reservation-offerings)
        """

    def describe_host_reservations(
        self,
        Filters: List[FilterTypeDef] = None,
        HostReservationIdSet: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeHostReservationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_host_reservations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-host-reservations)
        """

    def describe_hosts(
        self,
        Filters: List[FilterTypeDef] = None,
        HostIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeHostsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_hosts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-hosts)
        """

    def describe_iam_instance_profile_associations(
        self,
        AssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeIamInstanceProfileAssociationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_iam_instance_profile_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-iam-instance-profile-associations)
        """

    def describe_id_format(self, Resource: str = None) -> DescribeIdFormatResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_id_format)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-id-format)
        """

    def describe_identity_id_format(
        self, PrincipalArn: str, Resource: str = None
    ) -> DescribeIdentityIdFormatResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_identity_id_format)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-identity-id-format)
        """

    def describe_image_attribute(
        self, Attribute: ImageAttributeName, ImageId: str, DryRun: bool = None
    ) -> ImageAttributeTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_image_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-image-attribute)
        """

    def describe_images(
        self,
        ExecutableUsers: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        ImageIds: List[str] = None,
        Owners: List[str] = None,
        DryRun: bool = None,
    ) -> DescribeImagesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-images)
        """

    def describe_import_image_tasks(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ImportTaskIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeImportImageTasksResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_import_image_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-import-image-tasks)
        """

    def describe_import_snapshot_tasks(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        ImportTaskIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeImportSnapshotTasksResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_import_snapshot_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-import-snapshot-tasks)
        """

    def describe_instance_attribute(
        self, Attribute: InstanceAttributeName, InstanceId: str, DryRun: bool = None
    ) -> InstanceAttributeTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_instance_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-instance-attribute)
        """

    def describe_instance_credit_specifications(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeInstanceCreditSpecificationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_instance_credit_specifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-instance-credit-specifications)
        """

    def describe_instance_event_notification_attributes(
        self, DryRun: bool = None
    ) -> DescribeInstanceEventNotificationAttributesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_instance_event_notification_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-instance-event-notification-attributes)
        """

    def describe_instance_status(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
    ) -> DescribeInstanceStatusResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_instance_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-instance-status)
        """

    def describe_instance_type_offerings(
        self,
        DryRun: bool = None,
        LocationType: LocationType = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeInstanceTypeOfferingsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_instance_type_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-instance-type-offerings)
        """

    def describe_instance_types(
        self,
        DryRun: bool = None,
        InstanceTypes: List[InstanceType] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeInstanceTypesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_instance_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-instance-types)
        """

    def describe_instances(
        self,
        Filters: List[FilterTypeDef] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-instances)
        """

    def describe_internet_gateways(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeInternetGatewaysResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_internet_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-internet-gateways)
        """

    def describe_ipv6_pools(
        self,
        PoolIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
    ) -> DescribeIpv6PoolsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_ipv6_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-ipv6-pools)
        """

    def describe_key_pairs(
        self,
        Filters: List[FilterTypeDef] = None,
        KeyNames: List[str] = None,
        KeyPairIds: List[str] = None,
        DryRun: bool = None,
    ) -> DescribeKeyPairsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_key_pairs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-key-pairs)
        """

    def describe_launch_template_versions(
        self,
        DryRun: bool = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        Versions: List[str] = None,
        MinVersion: str = None,
        MaxVersion: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[FilterTypeDef] = None,
    ) -> DescribeLaunchTemplateVersionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_launch_template_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-launch-template-versions)
        """

    def describe_launch_templates(
        self,
        DryRun: bool = None,
        LaunchTemplateIds: List[str] = None,
        LaunchTemplateNames: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeLaunchTemplatesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_launch_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-launch-templates)
        """

    def describe_local_gateway_route_table_virtual_interface_group_associations(
        self,
        LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_table_virtual_interface_group_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-local-gateway-route-table-virtual-interface-group-associations)
        """

    def describe_local_gateway_route_table_vpc_associations(
        self,
        LocalGatewayRouteTableVpcAssociationIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_table_vpc_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-local-gateway-route-table-vpc-associations)
        """

    def describe_local_gateway_route_tables(
        self,
        LocalGatewayRouteTableIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeLocalGatewayRouteTablesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-local-gateway-route-tables)
        """

    def describe_local_gateway_virtual_interface_groups(
        self,
        LocalGatewayVirtualInterfaceGroupIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_local_gateway_virtual_interface_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-local-gateway-virtual-interface-groups)
        """

    def describe_local_gateway_virtual_interfaces(
        self,
        LocalGatewayVirtualInterfaceIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeLocalGatewayVirtualInterfacesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_local_gateway_virtual_interfaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-local-gateway-virtual-interfaces)
        """

    def describe_local_gateways(
        self,
        LocalGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeLocalGatewaysResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_local_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-local-gateways)
        """

    def describe_managed_prefix_lists(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        PrefixListIds: List[str] = None,
    ) -> DescribeManagedPrefixListsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_managed_prefix_lists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-managed-prefix-lists)
        """

    def describe_moving_addresses(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        PublicIps: List[str] = None,
    ) -> DescribeMovingAddressesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_moving_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-moving-addresses)
        """

    def describe_nat_gateways(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NatGatewayIds: List[str] = None,
        NextToken: str = None,
    ) -> DescribeNatGatewaysResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_nat_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-nat-gateways)
        """

    def describe_network_acls(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeNetworkAclsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_network_acls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-network-acls)
        """

    def describe_network_insights_analyses(
        self,
        NetworkInsightsAnalysisIds: List[str] = None,
        NetworkInsightsPathId: str = None,
        AnalysisStartTime: datetime = None,
        AnalysisEndTime: datetime = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        DryRun: bool = None,
        NextToken: str = None,
    ) -> DescribeNetworkInsightsAnalysesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_network_insights_analyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-network-insights-analyses)
        """

    def describe_network_insights_paths(
        self,
        NetworkInsightsPathIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        DryRun: bool = None,
        NextToken: str = None,
    ) -> DescribeNetworkInsightsPathsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_network_insights_paths)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-network-insights-paths)
        """

    def describe_network_interface_attribute(
        self,
        NetworkInterfaceId: str,
        Attribute: NetworkInterfaceAttribute = None,
        DryRun: bool = None,
    ) -> DescribeNetworkInterfaceAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_network_interface_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-network-interface-attribute)
        """

    def describe_network_interface_permissions(
        self,
        NetworkInterfacePermissionIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeNetworkInterfacePermissionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_network_interface_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-network-interface-permissions)
        """

    def describe_network_interfaces(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeNetworkInterfacesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_network_interfaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-network-interfaces)
        """

    def describe_placement_groups(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        GroupNames: List[str] = None,
        GroupIds: List[str] = None,
    ) -> DescribePlacementGroupsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_placement_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-placement-groups)
        """

    def describe_prefix_lists(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        PrefixListIds: List[str] = None,
    ) -> DescribePrefixListsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_prefix_lists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-prefix-lists)
        """

    def describe_principal_id_format(
        self,
        DryRun: bool = None,
        Resources: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribePrincipalIdFormatResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_principal_id_format)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-principal-id-format)
        """

    def describe_public_ipv4_pools(
        self,
        PoolIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List[FilterTypeDef] = None,
    ) -> DescribePublicIpv4PoolsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_public_ipv4_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-public-ipv4-pools)
        """

    def describe_regions(
        self,
        Filters: List[FilterTypeDef] = None,
        RegionNames: List[str] = None,
        DryRun: bool = None,
        AllRegions: bool = None,
    ) -> DescribeRegionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_regions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-regions)
        """

    def describe_replace_root_volume_tasks(
        self,
        ReplaceRootVolumeTaskIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeReplaceRootVolumeTasksResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_replace_root_volume_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-replace-root-volume-tasks)
        """

    def describe_reserved_instances(
        self,
        Filters: List[FilterTypeDef] = None,
        OfferingClass: OfferingClassType = None,
        ReservedInstancesIds: List[str] = None,
        DryRun: bool = None,
        OfferingType: OfferingTypeValues = None,
    ) -> DescribeReservedInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_reserved_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-reserved-instances)
        """

    def describe_reserved_instances_listings(
        self,
        Filters: List[FilterTypeDef] = None,
        ReservedInstancesId: str = None,
        ReservedInstancesListingId: str = None,
    ) -> DescribeReservedInstancesListingsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_reserved_instances_listings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-reserved-instances-listings)
        """

    def describe_reserved_instances_modifications(
        self,
        Filters: List[FilterTypeDef] = None,
        ReservedInstancesModificationIds: List[str] = None,
        NextToken: str = None,
    ) -> DescribeReservedInstancesModificationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_reserved_instances_modifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-reserved-instances-modifications)
        """

    def describe_reserved_instances_offerings(
        self,
        AvailabilityZone: str = None,
        Filters: List[FilterTypeDef] = None,
        IncludeMarketplace: bool = None,
        InstanceType: InstanceType = None,
        MaxDuration: int = None,
        MaxInstanceCount: int = None,
        MinDuration: int = None,
        OfferingClass: OfferingClassType = None,
        ProductDescription: RIProductDescription = None,
        ReservedInstancesOfferingIds: List[str] = None,
        DryRun: bool = None,
        InstanceTenancy: Tenancy = None,
        MaxResults: int = None,
        NextToken: str = None,
        OfferingType: OfferingTypeValues = None,
    ) -> DescribeReservedInstancesOfferingsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_reserved_instances_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-reserved-instances-offerings)
        """

    def describe_route_tables(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeRouteTablesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_route_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-route-tables)
        """

    def describe_scheduled_instance_availability(
        self,
        FirstSlotStartTimeRange: SlotDateTimeRangeRequestTypeDef,
        Recurrence: ScheduledInstanceRecurrenceRequestTypeDef,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        MaxSlotDurationInHours: int = None,
        MinSlotDurationInHours: int = None,
        NextToken: str = None,
    ) -> DescribeScheduledInstanceAvailabilityResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_scheduled_instance_availability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-scheduled-instance-availability)
        """

    def describe_scheduled_instances(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        ScheduledInstanceIds: List[str] = None,
        SlotStartTimeRange: SlotStartTimeRangeRequestTypeDef = None,
    ) -> DescribeScheduledInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_scheduled_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-scheduled-instances)
        """

    def describe_security_group_references(
        self, GroupId: List[str], DryRun: bool = None
    ) -> DescribeSecurityGroupReferencesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_security_group_references)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-security-group-references)
        """

    def describe_security_groups(
        self,
        Filters: List[FilterTypeDef] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeSecurityGroupsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_security_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-security-groups)
        """

    def describe_snapshot_attribute(
        self, Attribute: SnapshotAttributeName, SnapshotId: str, DryRun: bool = None
    ) -> DescribeSnapshotAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_snapshot_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-snapshot-attribute)
        """

    def describe_snapshots(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
    ) -> DescribeSnapshotsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-snapshots)
        """

    def describe_spot_datafeed_subscription(
        self, DryRun: bool = None
    ) -> DescribeSpotDatafeedSubscriptionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_spot_datafeed_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-spot-datafeed-subscription)
        """

    def describe_spot_fleet_instances(
        self,
        SpotFleetRequestId: str,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeSpotFleetInstancesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_spot_fleet_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-spot-fleet-instances)
        """

    def describe_spot_fleet_request_history(
        self,
        SpotFleetRequestId: str,
        StartTime: datetime,
        DryRun: bool = None,
        EventType: EventType = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeSpotFleetRequestHistoryResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_spot_fleet_request_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-spot-fleet-request-history)
        """

    def describe_spot_fleet_requests(
        self,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        SpotFleetRequestIds: List[str] = None,
    ) -> DescribeSpotFleetRequestsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_spot_fleet_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-spot-fleet-requests)
        """

    def describe_spot_instance_requests(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        SpotInstanceRequestIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeSpotInstanceRequestsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_spot_instance_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-spot-instance-requests)
        """

    def describe_spot_price_history(
        self,
        Filters: List[FilterTypeDef] = None,
        AvailabilityZone: str = None,
        DryRun: bool = None,
        EndTime: datetime = None,
        InstanceTypes: List[InstanceType] = None,
        MaxResults: int = None,
        NextToken: str = None,
        ProductDescriptions: List[str] = None,
        StartTime: datetime = None,
    ) -> DescribeSpotPriceHistoryResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_spot_price_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-spot-price-history)
        """

    def describe_stale_security_groups(
        self, VpcId: str, DryRun: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeStaleSecurityGroupsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_stale_security_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-stale-security-groups)
        """

    def describe_store_image_tasks(
        self,
        ImageIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeStoreImageTasksResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_store_image_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-store-image-tasks)
        """

    def describe_subnets(
        self,
        Filters: List[FilterTypeDef] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeSubnetsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_subnets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-subnets)
        """

    def describe_tags(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeTagsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-tags)
        """

    def describe_traffic_mirror_filters(
        self,
        TrafficMirrorFilterIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeTrafficMirrorFiltersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-traffic-mirror-filters)
        """

    def describe_traffic_mirror_sessions(
        self,
        TrafficMirrorSessionIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeTrafficMirrorSessionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-traffic-mirror-sessions)
        """

    def describe_traffic_mirror_targets(
        self,
        TrafficMirrorTargetIds: List[str] = None,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeTrafficMirrorTargetsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-traffic-mirror-targets)
        """

    def describe_transit_gateway_attachments(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeTransitGatewayAttachmentsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_transit_gateway_attachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-transit-gateway-attachments)
        """

    def describe_transit_gateway_connect_peers(
        self,
        TransitGatewayConnectPeerIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeTransitGatewayConnectPeersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_transit_gateway_connect_peers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-transit-gateway-connect-peers)
        """

    def describe_transit_gateway_connects(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeTransitGatewayConnectsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_transit_gateway_connects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-transit-gateway-connects)
        """

    def describe_transit_gateway_multicast_domains(
        self,
        TransitGatewayMulticastDomainIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeTransitGatewayMulticastDomainsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_transit_gateway_multicast_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-transit-gateway-multicast-domains)
        """

    def describe_transit_gateway_peering_attachments(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeTransitGatewayPeeringAttachmentsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_transit_gateway_peering_attachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-transit-gateway-peering-attachments)
        """

    def describe_transit_gateway_route_tables(
        self,
        TransitGatewayRouteTableIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeTransitGatewayRouteTablesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_transit_gateway_route_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-transit-gateway-route-tables)
        """

    def describe_transit_gateway_vpc_attachments(
        self,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeTransitGatewayVpcAttachmentsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_transit_gateway_vpc_attachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-transit-gateway-vpc-attachments)
        """

    def describe_transit_gateways(
        self,
        TransitGatewayIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> DescribeTransitGatewaysResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_transit_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-transit-gateways)
        """

    def describe_volume_attribute(
        self, Attribute: VolumeAttributeName, VolumeId: str, DryRun: bool = None
    ) -> DescribeVolumeAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_volume_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-volume-attribute)
        """

    def describe_volume_status(
        self,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
    ) -> DescribeVolumeStatusResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_volume_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-volume-status)
        """

    def describe_volumes(
        self,
        Filters: List[FilterTypeDef] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeVolumesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_volumes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-volumes)
        """

    def describe_volumes_modifications(
        self,
        DryRun: bool = None,
        VolumeIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeVolumesModificationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_volumes_modifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-volumes-modifications)
        """

    def describe_vpc_attribute(
        self, Attribute: VpcAttributeName, VpcId: str, DryRun: bool = None
    ) -> DescribeVpcAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_vpc_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-vpc-attribute)
        """

    def describe_vpc_classic_link(
        self, Filters: List[FilterTypeDef] = None, DryRun: bool = None, VpcIds: List[str] = None
    ) -> DescribeVpcClassicLinkResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_vpc_classic_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-vpc-classic-link)
        """

    def describe_vpc_classic_link_dns_support(
        self, MaxResults: int = None, NextToken: str = None, VpcIds: List[str] = None
    ) -> DescribeVpcClassicLinkDnsSupportResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_vpc_classic_link_dns_support)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-vpc-classic-link-dns-support)
        """

    def describe_vpc_endpoint_connection_notifications(
        self,
        DryRun: bool = None,
        ConnectionNotificationId: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeVpcEndpointConnectionNotificationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_connection_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-vpc-endpoint-connection-notifications)
        """

    def describe_vpc_endpoint_connections(
        self,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeVpcEndpointConnectionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-vpc-endpoint-connections)
        """

    def describe_vpc_endpoint_service_configurations(
        self,
        DryRun: bool = None,
        ServiceIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeVpcEndpointServiceConfigurationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_service_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-vpc-endpoint-service-configurations)
        """

    def describe_vpc_endpoint_service_permissions(
        self,
        ServiceId: str,
        DryRun: bool = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeVpcEndpointServicePermissionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_service_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-vpc-endpoint-service-permissions)
        """

    def describe_vpc_endpoint_services(
        self,
        DryRun: bool = None,
        ServiceNames: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeVpcEndpointServicesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-vpc-endpoint-services)
        """

    def describe_vpc_endpoints(
        self,
        DryRun: bool = None,
        VpcEndpointIds: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> DescribeVpcEndpointsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_vpc_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-vpc-endpoints)
        """

    def describe_vpc_peering_connections(
        self,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeVpcPeeringConnectionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_vpc_peering_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-vpc-peering-connections)
        """

    def describe_vpcs(
        self,
        Filters: List[FilterTypeDef] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
    ) -> DescribeVpcsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_vpcs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-vpcs)
        """

    def describe_vpn_connections(
        self,
        Filters: List[FilterTypeDef] = None,
        VpnConnectionIds: List[str] = None,
        DryRun: bool = None,
    ) -> DescribeVpnConnectionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_vpn_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-vpn-connections)
        """

    def describe_vpn_gateways(
        self,
        Filters: List[FilterTypeDef] = None,
        VpnGatewayIds: List[str] = None,
        DryRun: bool = None,
    ) -> DescribeVpnGatewaysResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.describe_vpn_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe-vpn-gateways)
        """

    def detach_classic_link_vpc(
        self, InstanceId: str, VpcId: str, DryRun: bool = None
    ) -> DetachClassicLinkVpcResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.detach_classic_link_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#detach-classic-link-vpc)
        """

    def detach_internet_gateway(
        self, InternetGatewayId: str, VpcId: str, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.detach_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#detach-internet-gateway)
        """

    def detach_network_interface(
        self, AttachmentId: str, DryRun: bool = None, Force: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.detach_network_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#detach-network-interface)
        """

    def detach_volume(
        self,
        VolumeId: str,
        Device: str = None,
        Force: bool = None,
        InstanceId: str = None,
        DryRun: bool = None,
    ) -> "VolumeAttachmentTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.detach_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#detach-volume)
        """

    def detach_vpn_gateway(self, VpcId: str, VpnGatewayId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.detach_vpn_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#detach-vpn-gateway)
        """

    def disable_ebs_encryption_by_default(
        self, DryRun: bool = None
    ) -> DisableEbsEncryptionByDefaultResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disable_ebs_encryption_by_default)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable-ebs-encryption-by-default)
        """

    def disable_fast_snapshot_restores(
        self, AvailabilityZones: List[str], SourceSnapshotIds: List[str], DryRun: bool = None
    ) -> DisableFastSnapshotRestoresResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disable_fast_snapshot_restores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable-fast-snapshot-restores)
        """

    def disable_serial_console_access(
        self, DryRun: bool = None
    ) -> DisableSerialConsoleAccessResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disable_serial_console_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable-serial-console-access)
        """

    def disable_transit_gateway_route_table_propagation(
        self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> DisableTransitGatewayRouteTablePropagationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disable_transit_gateway_route_table_propagation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable-transit-gateway-route-table-propagation)
        """

    def disable_vgw_route_propagation(
        self, GatewayId: str, RouteTableId: str, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disable_vgw_route_propagation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable-vgw-route-propagation)
        """

    def disable_vpc_classic_link(
        self, VpcId: str, DryRun: bool = None
    ) -> DisableVpcClassicLinkResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disable_vpc_classic_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable-vpc-classic-link)
        """

    def disable_vpc_classic_link_dns_support(
        self, VpcId: str = None
    ) -> DisableVpcClassicLinkDnsSupportResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disable_vpc_classic_link_dns_support)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable-vpc-classic-link-dns-support)
        """

    def disassociate_address(
        self, AssociationId: str = None, PublicIp: str = None, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disassociate_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate-address)
        """

    def disassociate_client_vpn_target_network(
        self, ClientVpnEndpointId: str, AssociationId: str, DryRun: bool = None
    ) -> DisassociateClientVpnTargetNetworkResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disassociate_client_vpn_target_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate-client-vpn-target-network)
        """

    def disassociate_enclave_certificate_iam_role(
        self, CertificateArn: str = None, RoleArn: str = None, DryRun: bool = None
    ) -> DisassociateEnclaveCertificateIamRoleResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disassociate_enclave_certificate_iam_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate-enclave-certificate-iam-role)
        """

    def disassociate_iam_instance_profile(
        self, AssociationId: str
    ) -> DisassociateIamInstanceProfileResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disassociate_iam_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate-iam-instance-profile)
        """

    def disassociate_route_table(self, AssociationId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disassociate_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate-route-table)
        """

    def disassociate_subnet_cidr_block(
        self, AssociationId: str
    ) -> DisassociateSubnetCidrBlockResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disassociate_subnet_cidr_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate-subnet-cidr-block)
        """

    def disassociate_transit_gateway_multicast_domain(
        self,
        TransitGatewayMulticastDomainId: str = None,
        TransitGatewayAttachmentId: str = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
    ) -> DisassociateTransitGatewayMulticastDomainResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disassociate_transit_gateway_multicast_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate-transit-gateway-multicast-domain)
        """

    def disassociate_transit_gateway_route_table(
        self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> DisassociateTransitGatewayRouteTableResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disassociate_transit_gateway_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate-transit-gateway-route-table)
        """

    def disassociate_vpc_cidr_block(
        self, AssociationId: str
    ) -> DisassociateVpcCidrBlockResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.disassociate_vpc_cidr_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate-vpc-cidr-block)
        """

    def enable_ebs_encryption_by_default(
        self, DryRun: bool = None
    ) -> EnableEbsEncryptionByDefaultResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.enable_ebs_encryption_by_default)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable-ebs-encryption-by-default)
        """

    def enable_fast_snapshot_restores(
        self, AvailabilityZones: List[str], SourceSnapshotIds: List[str], DryRun: bool = None
    ) -> EnableFastSnapshotRestoresResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.enable_fast_snapshot_restores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable-fast-snapshot-restores)
        """

    def enable_serial_console_access(
        self, DryRun: bool = None
    ) -> EnableSerialConsoleAccessResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.enable_serial_console_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable-serial-console-access)
        """

    def enable_transit_gateway_route_table_propagation(
        self, TransitGatewayRouteTableId: str, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> EnableTransitGatewayRouteTablePropagationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.enable_transit_gateway_route_table_propagation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable-transit-gateway-route-table-propagation)
        """

    def enable_vgw_route_propagation(
        self, GatewayId: str, RouteTableId: str, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.enable_vgw_route_propagation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable-vgw-route-propagation)
        """

    def enable_volume_io(self, VolumeId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.enable_volume_io)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable-volume-io)
        """

    def enable_vpc_classic_link(
        self, VpcId: str, DryRun: bool = None
    ) -> EnableVpcClassicLinkResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.enable_vpc_classic_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable-vpc-classic-link)
        """

    def enable_vpc_classic_link_dns_support(
        self, VpcId: str = None
    ) -> EnableVpcClassicLinkDnsSupportResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.enable_vpc_classic_link_dns_support)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable-vpc-classic-link-dns-support)
        """

    def export_client_vpn_client_certificate_revocation_list(
        self, ClientVpnEndpointId: str, DryRun: bool = None
    ) -> ExportClientVpnClientCertificateRevocationListResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.export_client_vpn_client_certificate_revocation_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#export-client-vpn-client-certificate-revocation-list)
        """

    def export_client_vpn_client_configuration(
        self, ClientVpnEndpointId: str, DryRun: bool = None
    ) -> ExportClientVpnClientConfigurationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.export_client_vpn_client_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#export-client-vpn-client-configuration)
        """

    def export_image(
        self,
        DiskImageFormat: DiskImageFormat,
        ImageId: str,
        S3ExportLocation: ExportTaskS3LocationRequestTypeDef,
        ClientToken: str = None,
        Description: str = None,
        DryRun: bool = None,
        RoleName: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> ExportImageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.export_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#export-image)
        """

    def export_transit_gateway_routes(
        self,
        TransitGatewayRouteTableId: str,
        S3Bucket: str,
        Filters: List[FilterTypeDef] = None,
        DryRun: bool = None,
    ) -> ExportTransitGatewayRoutesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.export_transit_gateway_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#export-transit-gateway-routes)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#generate-presigned-url)
        """

    def get_associated_enclave_certificate_iam_roles(
        self, CertificateArn: str = None, DryRun: bool = None
    ) -> GetAssociatedEnclaveCertificateIamRolesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_associated_enclave_certificate_iam_roles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-associated-enclave-certificate-iam-roles)
        """

    def get_associated_ipv6_pool_cidrs(
        self, PoolId: str, NextToken: str = None, MaxResults: int = None, DryRun: bool = None
    ) -> GetAssociatedIpv6PoolCidrsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_associated_ipv6_pool_cidrs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-associated-ipv6-pool-cidrs)
        """

    def get_capacity_reservation_usage(
        self,
        CapacityReservationId: str,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None,
    ) -> GetCapacityReservationUsageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_capacity_reservation_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-capacity-reservation-usage)
        """

    def get_coip_pool_usage(
        self,
        PoolId: str,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> GetCoipPoolUsageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_coip_pool_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-coip-pool-usage)
        """

    def get_console_output(
        self, InstanceId: str, DryRun: bool = None, Latest: bool = None
    ) -> GetConsoleOutputResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_console_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-console-output)
        """

    def get_console_screenshot(
        self, InstanceId: str, DryRun: bool = None, WakeUp: bool = None
    ) -> GetConsoleScreenshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_console_screenshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-console-screenshot)
        """

    def get_default_credit_specification(
        self, InstanceFamily: UnlimitedSupportedInstanceFamily, DryRun: bool = None
    ) -> GetDefaultCreditSpecificationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_default_credit_specification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-default-credit-specification)
        """

    def get_ebs_default_kms_key_id(self, DryRun: bool = None) -> GetEbsDefaultKmsKeyIdResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_ebs_default_kms_key_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-ebs-default-kms-key-id)
        """

    def get_ebs_encryption_by_default(
        self, DryRun: bool = None
    ) -> GetEbsEncryptionByDefaultResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_ebs_encryption_by_default)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-ebs-encryption-by-default)
        """

    def get_flow_logs_integration_template(
        self,
        FlowLogId: str,
        ConfigDeliveryS3DestinationArn: str,
        IntegrateServices: IntegrateServicesTypeDef,
        DryRun: bool = None,
    ) -> GetFlowLogsIntegrationTemplateResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_flow_logs_integration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-flow-logs-integration-template)
        """

    def get_groups_for_capacity_reservation(
        self,
        CapacityReservationId: str,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None,
    ) -> GetGroupsForCapacityReservationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_groups_for_capacity_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-groups-for-capacity-reservation)
        """

    def get_host_reservation_purchase_preview(
        self, HostIdSet: List[str], OfferingId: str
    ) -> GetHostReservationPurchasePreviewResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_host_reservation_purchase_preview)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-host-reservation-purchase-preview)
        """

    def get_launch_template_data(
        self, InstanceId: str, DryRun: bool = None
    ) -> GetLaunchTemplateDataResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_launch_template_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-launch-template-data)
        """

    def get_managed_prefix_list_associations(
        self, PrefixListId: str, DryRun: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> GetManagedPrefixListAssociationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_managed_prefix_list_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-managed-prefix-list-associations)
        """

    def get_managed_prefix_list_entries(
        self,
        PrefixListId: str,
        DryRun: bool = None,
        TargetVersion: int = None,
        MaxResults: int = None,
        NextToken: str = None,
    ) -> GetManagedPrefixListEntriesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_managed_prefix_list_entries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-managed-prefix-list-entries)
        """

    def get_password_data(
        self, InstanceId: str, DryRun: bool = None
    ) -> GetPasswordDataResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_password_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-password-data)
        """

    def get_reserved_instances_exchange_quote(
        self,
        ReservedInstanceIds: List[str],
        DryRun: bool = None,
        TargetConfigurations: List[TargetConfigurationRequestTypeDef] = None,
    ) -> GetReservedInstancesExchangeQuoteResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_reserved_instances_exchange_quote)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-reserved-instances-exchange-quote)
        """

    def get_serial_console_access_status(
        self, DryRun: bool = None
    ) -> GetSerialConsoleAccessStatusResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_serial_console_access_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-serial-console-access-status)
        """

    def get_transit_gateway_attachment_propagations(
        self,
        TransitGatewayAttachmentId: str,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> GetTransitGatewayAttachmentPropagationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_transit_gateway_attachment_propagations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-transit-gateway-attachment-propagations)
        """

    def get_transit_gateway_multicast_domain_associations(
        self,
        TransitGatewayMulticastDomainId: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> GetTransitGatewayMulticastDomainAssociationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_transit_gateway_multicast_domain_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-transit-gateway-multicast-domain-associations)
        """

    def get_transit_gateway_prefix_list_references(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> GetTransitGatewayPrefixListReferencesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_transit_gateway_prefix_list_references)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-transit-gateway-prefix-list-references)
        """

    def get_transit_gateway_route_table_associations(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> GetTransitGatewayRouteTableAssociationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_transit_gateway_route_table_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-transit-gateway-route-table-associations)
        """

    def get_transit_gateway_route_table_propagations(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> GetTransitGatewayRouteTablePropagationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.get_transit_gateway_route_table_propagations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get-transit-gateway-route-table-propagations)
        """

    def import_client_vpn_client_certificate_revocation_list(
        self, ClientVpnEndpointId: str, CertificateRevocationList: str, DryRun: bool = None
    ) -> ImportClientVpnClientCertificateRevocationListResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.import_client_vpn_client_certificate_revocation_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#import-client-vpn-client-certificate-revocation-list)
        """

    def import_image(
        self,
        Architecture: str = None,
        ClientData: ClientDataTypeDef = None,
        ClientToken: str = None,
        Description: str = None,
        DiskContainers: List[ImageDiskContainerTypeDef] = None,
        DryRun: bool = None,
        Encrypted: bool = None,
        Hypervisor: str = None,
        KmsKeyId: str = None,
        LicenseType: str = None,
        Platform: str = None,
        RoleName: str = None,
        LicenseSpecifications: List[ImportImageLicenseConfigurationRequestTypeDef] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> ImportImageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.import_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#import-image)
        """

    def import_instance(
        self,
        Platform: Literal["Windows"],
        Description: str = None,
        DiskImages: List[DiskImageTypeDef] = None,
        DryRun: bool = None,
        LaunchSpecification: ImportInstanceLaunchSpecificationTypeDef = None,
    ) -> ImportInstanceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.import_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#import-instance)
        """

    def import_key_pair(
        self,
        KeyName: str,
        PublicKeyMaterial: Union[bytes, IO[bytes]],
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> ImportKeyPairResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.import_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#import-key-pair)
        """

    def import_snapshot(
        self,
        ClientData: ClientDataTypeDef = None,
        ClientToken: str = None,
        Description: str = None,
        DiskContainer: SnapshotDiskContainerTypeDef = None,
        DryRun: bool = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        RoleName: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> ImportSnapshotResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.import_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#import-snapshot)
        """

    def import_volume(
        self,
        AvailabilityZone: str,
        Image: "DiskImageDetailTypeDef",
        Volume: "VolumeDetailTypeDef",
        Description: str = None,
        DryRun: bool = None,
    ) -> ImportVolumeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.import_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#import-volume)
        """

    def modify_address_attribute(
        self, AllocationId: str, DomainName: str = None, DryRun: bool = None
    ) -> ModifyAddressAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_address_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-address-attribute)
        """

    def modify_availability_zone_group(
        self, GroupName: str, OptInStatus: ModifyAvailabilityZoneOptInStatus, DryRun: bool = None
    ) -> ModifyAvailabilityZoneGroupResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_availability_zone_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-availability-zone-group)
        """

    def modify_capacity_reservation(
        self,
        CapacityReservationId: str,
        InstanceCount: int = None,
        EndDate: datetime = None,
        EndDateType: EndDateType = None,
        Accept: bool = None,
        DryRun: bool = None,
    ) -> ModifyCapacityReservationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_capacity_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-capacity-reservation)
        """

    def modify_client_vpn_endpoint(
        self,
        ClientVpnEndpointId: str,
        ServerCertificateArn: str = None,
        ConnectionLogOptions: ConnectionLogOptionsTypeDef = None,
        DnsServers: DnsServersOptionsModifyStructureTypeDef = None,
        VpnPort: int = None,
        Description: str = None,
        SplitTunnel: bool = None,
        DryRun: bool = None,
        SecurityGroupIds: List[str] = None,
        VpcId: str = None,
        SelfServicePortal: SelfServicePortal = None,
        ClientConnectOptions: ClientConnectOptionsTypeDef = None,
    ) -> ModifyClientVpnEndpointResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_client_vpn_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-client-vpn-endpoint)
        """

    def modify_default_credit_specification(
        self, InstanceFamily: UnlimitedSupportedInstanceFamily, CpuCredits: str, DryRun: bool = None
    ) -> ModifyDefaultCreditSpecificationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_default_credit_specification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-default-credit-specification)
        """

    def modify_ebs_default_kms_key_id(
        self, KmsKeyId: str, DryRun: bool = None
    ) -> ModifyEbsDefaultKmsKeyIdResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_ebs_default_kms_key_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-ebs-default-kms-key-id)
        """

    def modify_fleet(
        self,
        FleetId: str,
        DryRun: bool = None,
        ExcessCapacityTerminationPolicy: FleetExcessCapacityTerminationPolicy = None,
        LaunchTemplateConfigs: List[FleetLaunchTemplateConfigRequestTypeDef] = None,
        TargetCapacitySpecification: TargetCapacitySpecificationRequestTypeDef = None,
    ) -> ModifyFleetResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-fleet)
        """

    def modify_fpga_image_attribute(
        self,
        FpgaImageId: str,
        DryRun: bool = None,
        Attribute: FpgaImageAttributeName = None,
        OperationType: OperationType = None,
        UserIds: List[str] = None,
        UserGroups: List[str] = None,
        ProductCodes: List[str] = None,
        LoadPermission: LoadPermissionModificationsTypeDef = None,
        Description: str = None,
        Name: str = None,
    ) -> ModifyFpgaImageAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_fpga_image_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-fpga-image-attribute)
        """

    def modify_hosts(
        self,
        HostIds: List[str],
        AutoPlacement: AutoPlacement = None,
        HostRecovery: HostRecovery = None,
        InstanceType: str = None,
        InstanceFamily: str = None,
    ) -> ModifyHostsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_hosts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-hosts)
        """

    def modify_id_format(self, Resource: str, UseLongIds: bool) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_id_format)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-id-format)
        """

    def modify_identity_id_format(self, PrincipalArn: str, Resource: str, UseLongIds: bool) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_identity_id_format)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-identity-id-format)
        """

    def modify_image_attribute(
        self,
        ImageId: str,
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_image_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-image-attribute)
        """

    def modify_instance_attribute(
        self,
        InstanceId: str,
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_instance_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-instance-attribute)
        """

    def modify_instance_capacity_reservation_attributes(
        self,
        InstanceId: str,
        CapacityReservationSpecification: CapacityReservationSpecificationTypeDef,
        DryRun: bool = None,
    ) -> ModifyInstanceCapacityReservationAttributesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_instance_capacity_reservation_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-instance-capacity-reservation-attributes)
        """

    def modify_instance_credit_specification(
        self,
        InstanceCreditSpecifications: List[InstanceCreditSpecificationRequestTypeDef],
        DryRun: bool = None,
        ClientToken: str = None,
    ) -> ModifyInstanceCreditSpecificationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_instance_credit_specification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-instance-credit-specification)
        """

    def modify_instance_event_start_time(
        self, InstanceId: str, InstanceEventId: str, NotBefore: datetime, DryRun: bool = None
    ) -> ModifyInstanceEventStartTimeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_instance_event_start_time)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-instance-event-start-time)
        """

    def modify_instance_metadata_options(
        self,
        InstanceId: str,
        HttpTokens: HttpTokensState = None,
        HttpPutResponseHopLimit: int = None,
        HttpEndpoint: InstanceMetadataEndpointState = None,
        DryRun: bool = None,
    ) -> ModifyInstanceMetadataOptionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_instance_metadata_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-instance-metadata-options)
        """

    def modify_instance_placement(
        self,
        InstanceId: str,
        Affinity: Affinity = None,
        GroupName: str = None,
        HostId: str = None,
        Tenancy: HostTenancy = None,
        PartitionNumber: int = None,
        HostResourceGroupArn: str = None,
    ) -> ModifyInstancePlacementResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_instance_placement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-instance-placement)
        """

    def modify_launch_template(
        self,
        DryRun: bool = None,
        ClientToken: str = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        DefaultVersion: str = None,
    ) -> ModifyLaunchTemplateResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_launch_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-launch-template)
        """

    def modify_managed_prefix_list(
        self,
        PrefixListId: str,
        DryRun: bool = None,
        CurrentVersion: int = None,
        PrefixListName: str = None,
        AddEntries: List[AddPrefixListEntryTypeDef] = None,
        RemoveEntries: List[RemovePrefixListEntryTypeDef] = None,
    ) -> ModifyManagedPrefixListResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_managed_prefix_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-managed-prefix-list)
        """

    def modify_network_interface_attribute(
        self,
        NetworkInterfaceId: str,
        Attachment: NetworkInterfaceAttachmentChangesTypeDef = None,
        Description: "AttributeValueTypeDef" = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        SourceDestCheck: "AttributeBooleanValueTypeDef" = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_network_interface_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-network-interface-attribute)
        """

    def modify_reserved_instances(
        self,
        ReservedInstancesIds: List[str],
        TargetConfigurations: List["ReservedInstancesConfigurationTypeDef"],
        ClientToken: str = None,
    ) -> ModifyReservedInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_reserved_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-reserved-instances)
        """

    def modify_snapshot_attribute(
        self,
        SnapshotId: str,
        Attribute: SnapshotAttributeName = None,
        CreateVolumePermission: CreateVolumePermissionModificationsTypeDef = None,
        GroupNames: List[str] = None,
        OperationType: OperationType = None,
        UserIds: List[str] = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_snapshot_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-snapshot-attribute)
        """

    def modify_spot_fleet_request(
        self,
        SpotFleetRequestId: str,
        ExcessCapacityTerminationPolicy: ExcessCapacityTerminationPolicy = None,
        LaunchTemplateConfigs: List["LaunchTemplateConfigTypeDef"] = None,
        TargetCapacity: int = None,
        OnDemandTargetCapacity: int = None,
    ) -> ModifySpotFleetRequestResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_spot_fleet_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-spot-fleet-request)
        """

    def modify_subnet_attribute(
        self,
        SubnetId: str,
        AssignIpv6AddressOnCreation: "AttributeBooleanValueTypeDef" = None,
        MapPublicIpOnLaunch: "AttributeBooleanValueTypeDef" = None,
        MapCustomerOwnedIpOnLaunch: "AttributeBooleanValueTypeDef" = None,
        CustomerOwnedIpv4Pool: str = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_subnet_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-subnet-attribute)
        """

    def modify_traffic_mirror_filter_network_services(
        self,
        TrafficMirrorFilterId: str,
        AddNetworkServices: List[Literal["amazon-dns"]] = None,
        RemoveNetworkServices: List[Literal["amazon-dns"]] = None,
        DryRun: bool = None,
    ) -> ModifyTrafficMirrorFilterNetworkServicesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_filter_network_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-traffic-mirror-filter-network-services)
        """

    def modify_traffic_mirror_filter_rule(
        self,
        TrafficMirrorFilterRuleId: str,
        TrafficDirection: TrafficDirection = None,
        RuleNumber: int = None,
        RuleAction: TrafficMirrorRuleAction = None,
        DestinationPortRange: TrafficMirrorPortRangeRequestTypeDef = None,
        SourcePortRange: TrafficMirrorPortRangeRequestTypeDef = None,
        Protocol: int = None,
        DestinationCidrBlock: str = None,
        SourceCidrBlock: str = None,
        Description: str = None,
        RemoveFields: List[TrafficMirrorFilterRuleField] = None,
        DryRun: bool = None,
    ) -> ModifyTrafficMirrorFilterRuleResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_filter_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-traffic-mirror-filter-rule)
        """

    def modify_traffic_mirror_session(
        self,
        TrafficMirrorSessionId: str,
        TrafficMirrorTargetId: str = None,
        TrafficMirrorFilterId: str = None,
        PacketLength: int = None,
        SessionNumber: int = None,
        VirtualNetworkId: int = None,
        Description: str = None,
        RemoveFields: List[TrafficMirrorSessionField] = None,
        DryRun: bool = None,
    ) -> ModifyTrafficMirrorSessionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-traffic-mirror-session)
        """

    def modify_transit_gateway(
        self,
        TransitGatewayId: str,
        Description: str = None,
        Options: ModifyTransitGatewayOptionsTypeDef = None,
        DryRun: bool = None,
    ) -> ModifyTransitGatewayResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_transit_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-transit-gateway)
        """

    def modify_transit_gateway_prefix_list_reference(
        self,
        TransitGatewayRouteTableId: str,
        PrefixListId: str,
        TransitGatewayAttachmentId: str = None,
        Blackhole: bool = None,
        DryRun: bool = None,
    ) -> ModifyTransitGatewayPrefixListReferenceResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_transit_gateway_prefix_list_reference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-transit-gateway-prefix-list-reference)
        """

    def modify_transit_gateway_vpc_attachment(
        self,
        TransitGatewayAttachmentId: str,
        AddSubnetIds: List[str] = None,
        RemoveSubnetIds: List[str] = None,
        Options: ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef = None,
        DryRun: bool = None,
    ) -> ModifyTransitGatewayVpcAttachmentResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_transit_gateway_vpc_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-transit-gateway-vpc-attachment)
        """

    def modify_volume(
        self,
        VolumeId: str,
        DryRun: bool = None,
        Size: int = None,
        VolumeType: VolumeType = None,
        Iops: int = None,
        Throughput: int = None,
        MultiAttachEnabled: bool = None,
    ) -> ModifyVolumeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-volume)
        """

    def modify_volume_attribute(
        self,
        VolumeId: str,
        AutoEnableIO: "AttributeBooleanValueTypeDef" = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_volume_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-volume-attribute)
        """

    def modify_vpc_attribute(
        self,
        VpcId: str,
        EnableDnsHostnames: "AttributeBooleanValueTypeDef" = None,
        EnableDnsSupport: "AttributeBooleanValueTypeDef" = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_vpc_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-vpc-attribute)
        """

    def modify_vpc_endpoint(
        self,
        VpcEndpointId: str,
        DryRun: bool = None,
        ResetPolicy: bool = None,
        PolicyDocument: str = None,
        AddRouteTableIds: List[str] = None,
        RemoveRouteTableIds: List[str] = None,
        AddSubnetIds: List[str] = None,
        RemoveSubnetIds: List[str] = None,
        AddSecurityGroupIds: List[str] = None,
        RemoveSecurityGroupIds: List[str] = None,
        PrivateDnsEnabled: bool = None,
    ) -> ModifyVpcEndpointResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-vpc-endpoint)
        """

    def modify_vpc_endpoint_connection_notification(
        self,
        ConnectionNotificationId: str,
        DryRun: bool = None,
        ConnectionNotificationArn: str = None,
        ConnectionEvents: List[str] = None,
    ) -> ModifyVpcEndpointConnectionNotificationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_connection_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-vpc-endpoint-connection-notification)
        """

    def modify_vpc_endpoint_service_configuration(
        self,
        ServiceId: str,
        DryRun: bool = None,
        PrivateDnsName: str = None,
        RemovePrivateDnsName: bool = None,
        AcceptanceRequired: bool = None,
        AddNetworkLoadBalancerArns: List[str] = None,
        RemoveNetworkLoadBalancerArns: List[str] = None,
        AddGatewayLoadBalancerArns: List[str] = None,
        RemoveGatewayLoadBalancerArns: List[str] = None,
    ) -> ModifyVpcEndpointServiceConfigurationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_service_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-vpc-endpoint-service-configuration)
        """

    def modify_vpc_endpoint_service_permissions(
        self,
        ServiceId: str,
        DryRun: bool = None,
        AddAllowedPrincipals: List[str] = None,
        RemoveAllowedPrincipals: List[str] = None,
    ) -> ModifyVpcEndpointServicePermissionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_service_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-vpc-endpoint-service-permissions)
        """

    def modify_vpc_peering_connection_options(
        self,
        VpcPeeringConnectionId: str,
        AccepterPeeringConnectionOptions: PeeringConnectionOptionsRequestTypeDef = None,
        DryRun: bool = None,
        RequesterPeeringConnectionOptions: PeeringConnectionOptionsRequestTypeDef = None,
    ) -> ModifyVpcPeeringConnectionOptionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_vpc_peering_connection_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-vpc-peering-connection-options)
        """

    def modify_vpc_tenancy(
        self, VpcId: str, InstanceTenancy: Literal["default"], DryRun: bool = None
    ) -> ModifyVpcTenancyResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_vpc_tenancy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-vpc-tenancy)
        """

    def modify_vpn_connection(
        self,
        VpnConnectionId: str,
        TransitGatewayId: str = None,
        CustomerGatewayId: str = None,
        VpnGatewayId: str = None,
        DryRun: bool = None,
    ) -> ModifyVpnConnectionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_vpn_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-vpn-connection)
        """

    def modify_vpn_connection_options(
        self,
        VpnConnectionId: str,
        LocalIpv4NetworkCidr: str = None,
        RemoteIpv4NetworkCidr: str = None,
        LocalIpv6NetworkCidr: str = None,
        RemoteIpv6NetworkCidr: str = None,
        DryRun: bool = None,
    ) -> ModifyVpnConnectionOptionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_vpn_connection_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-vpn-connection-options)
        """

    def modify_vpn_tunnel_certificate(
        self, VpnConnectionId: str, VpnTunnelOutsideIpAddress: str, DryRun: bool = None
    ) -> ModifyVpnTunnelCertificateResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_vpn_tunnel_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-vpn-tunnel-certificate)
        """

    def modify_vpn_tunnel_options(
        self,
        VpnConnectionId: str,
        VpnTunnelOutsideIpAddress: str,
        TunnelOptions: ModifyVpnTunnelOptionsSpecificationTypeDef,
        DryRun: bool = None,
    ) -> ModifyVpnTunnelOptionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.modify_vpn_tunnel_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify-vpn-tunnel-options)
        """

    def monitor_instances(
        self, InstanceIds: List[str], DryRun: bool = None
    ) -> MonitorInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.monitor_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#monitor-instances)
        """

    def move_address_to_vpc(
        self, PublicIp: str, DryRun: bool = None
    ) -> MoveAddressToVpcResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.move_address_to_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#move-address-to-vpc)
        """

    def provision_byoip_cidr(
        self,
        Cidr: str,
        CidrAuthorizationContext: CidrAuthorizationContextTypeDef = None,
        PubliclyAdvertisable: bool = None,
        Description: str = None,
        DryRun: bool = None,
        PoolTagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> ProvisionByoipCidrResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.provision_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#provision-byoip-cidr)
        """

    def purchase_host_reservation(
        self,
        HostIdSet: List[str],
        OfferingId: str,
        ClientToken: str = None,
        CurrencyCode: Literal["USD"] = None,
        LimitPrice: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> PurchaseHostReservationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.purchase_host_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#purchase-host-reservation)
        """

    def purchase_reserved_instances_offering(
        self,
        InstanceCount: int,
        ReservedInstancesOfferingId: str,
        DryRun: bool = None,
        LimitPrice: ReservedInstanceLimitPriceTypeDef = None,
        PurchaseTime: datetime = None,
    ) -> PurchaseReservedInstancesOfferingResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.purchase_reserved_instances_offering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#purchase-reserved-instances-offering)
        """

    def purchase_scheduled_instances(
        self,
        PurchaseRequests: List[PurchaseRequestTypeDef],
        ClientToken: str = None,
        DryRun: bool = None,
    ) -> PurchaseScheduledInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.purchase_scheduled_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#purchase-scheduled-instances)
        """

    def reboot_instances(self, InstanceIds: List[str], DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.reboot_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reboot-instances)
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
    ) -> RegisterImageResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.register_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#register-image)
        """

    def register_instance_event_notification_attributes(
        self,
        DryRun: bool = None,
        InstanceTagAttribute: RegisterInstanceTagAttributeRequestTypeDef = None,
    ) -> RegisterInstanceEventNotificationAttributesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.register_instance_event_notification_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#register-instance-event-notification-attributes)
        """

    def register_transit_gateway_multicast_group_members(
        self,
        TransitGatewayMulticastDomainId: str = None,
        GroupIpAddress: str = None,
        NetworkInterfaceIds: List[str] = None,
        DryRun: bool = None,
    ) -> RegisterTransitGatewayMulticastGroupMembersResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.register_transit_gateway_multicast_group_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#register-transit-gateway-multicast-group-members)
        """

    def register_transit_gateway_multicast_group_sources(
        self,
        TransitGatewayMulticastDomainId: str = None,
        GroupIpAddress: str = None,
        NetworkInterfaceIds: List[str] = None,
        DryRun: bool = None,
    ) -> RegisterTransitGatewayMulticastGroupSourcesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.register_transit_gateway_multicast_group_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#register-transit-gateway-multicast-group-sources)
        """

    def reject_transit_gateway_multicast_domain_associations(
        self,
        TransitGatewayMulticastDomainId: str = None,
        TransitGatewayAttachmentId: str = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
    ) -> RejectTransitGatewayMulticastDomainAssociationsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.reject_transit_gateway_multicast_domain_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reject-transit-gateway-multicast-domain-associations)
        """

    def reject_transit_gateway_peering_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> RejectTransitGatewayPeeringAttachmentResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.reject_transit_gateway_peering_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reject-transit-gateway-peering-attachment)
        """

    def reject_transit_gateway_vpc_attachment(
        self, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> RejectTransitGatewayVpcAttachmentResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.reject_transit_gateway_vpc_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reject-transit-gateway-vpc-attachment)
        """

    def reject_vpc_endpoint_connections(
        self, ServiceId: str, VpcEndpointIds: List[str], DryRun: bool = None
    ) -> RejectVpcEndpointConnectionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.reject_vpc_endpoint_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reject-vpc-endpoint-connections)
        """

    def reject_vpc_peering_connection(
        self, VpcPeeringConnectionId: str, DryRun: bool = None
    ) -> RejectVpcPeeringConnectionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.reject_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reject-vpc-peering-connection)
        """

    def release_address(
        self,
        AllocationId: str = None,
        PublicIp: str = None,
        NetworkBorderGroup: str = None,
        DryRun: bool = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.release_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#release-address)
        """

    def release_hosts(self, HostIds: List[str]) -> ReleaseHostsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.release_hosts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#release-hosts)
        """

    def replace_iam_instance_profile_association(
        self, IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef", AssociationId: str
    ) -> ReplaceIamInstanceProfileAssociationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.replace_iam_instance_profile_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#replace-iam-instance-profile-association)
        """

    def replace_network_acl_association(
        self, AssociationId: str, NetworkAclId: str, DryRun: bool = None
    ) -> ReplaceNetworkAclAssociationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.replace_network_acl_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#replace-network-acl-association)
        """

    def replace_network_acl_entry(
        self,
        Egress: bool,
        NetworkAclId: str,
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.replace_network_acl_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#replace-network-acl-entry)
        """

    def replace_route(
        self,
        RouteTableId: str,
        DestinationCidrBlock: str = None,
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.replace_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#replace-route)
        """

    def replace_route_table_association(
        self, AssociationId: str, RouteTableId: str, DryRun: bool = None
    ) -> ReplaceRouteTableAssociationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.replace_route_table_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#replace-route-table-association)
        """

    def replace_transit_gateway_route(
        self,
        DestinationCidrBlock: str,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str = None,
        Blackhole: bool = None,
        DryRun: bool = None,
    ) -> ReplaceTransitGatewayRouteResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.replace_transit_gateway_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#replace-transit-gateway-route)
        """

    def report_instance_status(
        self,
        Instances: List[str],
        ReasonCodes: List[ReportInstanceReasonCodes],
        Status: ReportStatusType,
        Description: str = None,
        DryRun: bool = None,
        EndTime: datetime = None,
        StartTime: datetime = None,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.report_instance_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#report-instance-status)
        """

    def request_spot_fleet(
        self, SpotFleetRequestConfig: "SpotFleetRequestConfigDataTypeDef", DryRun: bool = None
    ) -> RequestSpotFleetResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.request_spot_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#request-spot-fleet)
        """

    def request_spot_instances(
        self,
        AvailabilityZoneGroup: str = None,
        BlockDurationMinutes: int = None,
        ClientToken: str = None,
        DryRun: bool = None,
        InstanceCount: int = None,
        LaunchGroup: str = None,
        LaunchSpecification: RequestSpotLaunchSpecificationTypeDef = None,
        SpotPrice: str = None,
        Type: SpotInstanceType = None,
        ValidFrom: datetime = None,
        ValidUntil: datetime = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        InstanceInterruptionBehavior: InstanceInterruptionBehavior = None,
    ) -> RequestSpotInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.request_spot_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#request-spot-instances)
        """

    def reset_address_attribute(
        self, AllocationId: str, Attribute: Literal["domain-name"], DryRun: bool = None
    ) -> ResetAddressAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.reset_address_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reset-address-attribute)
        """

    def reset_ebs_default_kms_key_id(
        self, DryRun: bool = None
    ) -> ResetEbsDefaultKmsKeyIdResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.reset_ebs_default_kms_key_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reset-ebs-default-kms-key-id)
        """

    def reset_fpga_image_attribute(
        self, FpgaImageId: str, DryRun: bool = None, Attribute: Literal["loadPermission"] = None
    ) -> ResetFpgaImageAttributeResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.reset_fpga_image_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reset-fpga-image-attribute)
        """

    def reset_image_attribute(
        self, Attribute: Literal["launchPermission"], ImageId: str, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.reset_image_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reset-image-attribute)
        """

    def reset_instance_attribute(
        self, Attribute: InstanceAttributeName, InstanceId: str, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.reset_instance_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reset-instance-attribute)
        """

    def reset_network_interface_attribute(
        self, NetworkInterfaceId: str, DryRun: bool = None, SourceDestCheck: str = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.reset_network_interface_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reset-network-interface-attribute)
        """

    def reset_snapshot_attribute(
        self, Attribute: SnapshotAttributeName, SnapshotId: str, DryRun: bool = None
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.reset_snapshot_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reset-snapshot-attribute)
        """

    def restore_address_to_classic(
        self, PublicIp: str, DryRun: bool = None
    ) -> RestoreAddressToClassicResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.restore_address_to_classic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#restore-address-to-classic)
        """

    def restore_managed_prefix_list_version(
        self, PrefixListId: str, PreviousVersion: int, CurrentVersion: int, DryRun: bool = None
    ) -> RestoreManagedPrefixListVersionResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.restore_managed_prefix_list_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#restore-managed-prefix-list-version)
        """

    def revoke_client_vpn_ingress(
        self,
        ClientVpnEndpointId: str,
        TargetNetworkCidr: str,
        AccessGroupId: str = None,
        RevokeAllGroups: bool = None,
        DryRun: bool = None,
    ) -> RevokeClientVpnIngressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.revoke_client_vpn_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#revoke-client-vpn-ingress)
        """

    def revoke_security_group_egress(
        self,
        GroupId: str,
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
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.revoke_security_group_egress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#revoke-security-group-egress)
        """

    def revoke_security_group_ingress(
        self,
        CidrIp: str = None,
        FromPort: int = None,
        GroupId: str = None,
        GroupName: str = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None,
    ) -> RevokeSecurityGroupIngressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.revoke_security_group_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#revoke-security-group-ingress)
        """

    def run_instances(
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
    ) -> "ReservationTypeDef":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.run_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#run-instances)
        """

    def run_scheduled_instances(
        self,
        LaunchSpecification: ScheduledInstancesLaunchSpecificationTypeDef,
        ScheduledInstanceId: str,
        ClientToken: str = None,
        DryRun: bool = None,
        InstanceCount: int = None,
    ) -> RunScheduledInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.run_scheduled_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#run-scheduled-instances)
        """

    def search_local_gateway_routes(
        self,
        LocalGatewayRouteTableId: str,
        Filters: List[FilterTypeDef],
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> SearchLocalGatewayRoutesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.search_local_gateway_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#search-local-gateway-routes)
        """

    def search_transit_gateway_multicast_groups(
        self,
        TransitGatewayMulticastDomainId: str = None,
        Filters: List[FilterTypeDef] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
    ) -> SearchTransitGatewayMulticastGroupsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.search_transit_gateway_multicast_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#search-transit-gateway-multicast-groups)
        """

    def search_transit_gateway_routes(
        self,
        TransitGatewayRouteTableId: str,
        Filters: List[FilterTypeDef],
        MaxResults: int = None,
        DryRun: bool = None,
    ) -> SearchTransitGatewayRoutesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.search_transit_gateway_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#search-transit-gateway-routes)
        """

    def send_diagnostic_interrupt(self, InstanceId: str, DryRun: bool = None) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.send_diagnostic_interrupt)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#send-diagnostic-interrupt)
        """

    def start_instances(
        self, InstanceIds: List[str], AdditionalInfo: str = None, DryRun: bool = None
    ) -> StartInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.start_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#start-instances)
        """

    def start_network_insights_analysis(
        self,
        NetworkInsightsPathId: str,
        ClientToken: str,
        FilterInArns: List[str] = None,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
    ) -> StartNetworkInsightsAnalysisResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.start_network_insights_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#start-network-insights-analysis)
        """

    def start_vpc_endpoint_service_private_dns_verification(
        self, ServiceId: str, DryRun: bool = None
    ) -> StartVpcEndpointServicePrivateDnsVerificationResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.start_vpc_endpoint_service_private_dns_verification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#start-vpc-endpoint-service-private-dns-verification)
        """

    def stop_instances(
        self,
        InstanceIds: List[str],
        Hibernate: bool = None,
        DryRun: bool = None,
        Force: bool = None,
    ) -> StopInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.stop_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#stop-instances)
        """

    def terminate_client_vpn_connections(
        self,
        ClientVpnEndpointId: str,
        ConnectionId: str = None,
        Username: str = None,
        DryRun: bool = None,
    ) -> TerminateClientVpnConnectionsResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.terminate_client_vpn_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#terminate-client-vpn-connections)
        """

    def terminate_instances(
        self, InstanceIds: List[str], DryRun: bool = None
    ) -> TerminateInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.terminate_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#terminate-instances)
        """

    def unassign_ipv6_addresses(
        self, NetworkInterfaceId: str, Ipv6Addresses: List[str]
    ) -> UnassignIpv6AddressesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.unassign_ipv6_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#unassign-ipv6-addresses)
        """

    def unassign_private_ip_addresses(
        self, NetworkInterfaceId: str, PrivateIpAddresses: List[str]
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.unassign_private_ip_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#unassign-private-ip-addresses)
        """

    def unmonitor_instances(
        self, InstanceIds: List[str], DryRun: bool = None
    ) -> UnmonitorInstancesResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.unmonitor_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#unmonitor-instances)
        """

    def update_security_group_rule_descriptions_egress(
        self,
        IpPermissions: List["IpPermissionTypeDef"],
        DryRun: bool = None,
        GroupId: str = None,
        GroupName: str = None,
    ) -> UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.update_security_group_rule_descriptions_egress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#update-security-group-rule-descriptions-egress)
        """

    def update_security_group_rule_descriptions_ingress(
        self,
        IpPermissions: List["IpPermissionTypeDef"],
        DryRun: bool = None,
        GroupId: str = None,
        GroupName: str = None,
    ) -> UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.update_security_group_rule_descriptions_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#update-security-group-rule-descriptions-ingress)
        """

    def withdraw_byoip_cidr(self, Cidr: str, DryRun: bool = None) -> WithdrawByoipCidrResultTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Client.withdraw_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#withdraw-byoip-cidr)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_addresses_attribute"]
    ) -> DescribeAddressesAttributePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeAddressesAttribute)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeaddressesattributepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_byoip_cidrs"]
    ) -> DescribeByoipCidrsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeByoipCidrs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describebyoipcidrspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_capacity_reservations"]
    ) -> DescribeCapacityReservationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeCapacityReservations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecapacityreservationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_carrier_gateways"]
    ) -> DescribeCarrierGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeCarrierGateways)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecarriergatewayspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_classic_link_instances"]
    ) -> DescribeClassicLinkInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeClassicLinkInstances)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclassiclinkinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_authorization_rules"]
    ) -> DescribeClientVpnAuthorizationRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnAuthorizationRules)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnauthorizationrulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_connections"]
    ) -> DescribeClientVpnConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnConnections)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnconnectionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_endpoints"]
    ) -> DescribeClientVpnEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnEndpoints)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnendpointspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_routes"]
    ) -> DescribeClientVpnRoutesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnRoutes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnroutespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_target_networks"]
    ) -> DescribeClientVpnTargetNetworksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnTargetNetworks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpntargetnetworkspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_coip_pools"]
    ) -> DescribeCoipPoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeCoipPools)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecoippoolspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_dhcp_options"]
    ) -> DescribeDhcpOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeDhcpOptions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describedhcpoptionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_egress_only_internet_gateways"]
    ) -> DescribeEgressOnlyInternetGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeEgressOnlyInternetGateways)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeegressonlyinternetgatewayspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_image_tasks"]
    ) -> DescribeExportImageTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeExportImageTasks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeexportimagetaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fast_snapshot_restores"]
    ) -> DescribeFastSnapshotRestoresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeFastSnapshotRestores)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describefastsnapshotrestorespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_fleets"]) -> DescribeFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeFleets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describefleetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_flow_logs"]
    ) -> DescribeFlowLogsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeFlowLogs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeflowlogspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fpga_images"]
    ) -> DescribeFpgaImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeFpgaImages)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describefpgaimagespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_host_reservation_offerings"]
    ) -> DescribeHostReservationOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeHostReservationOfferings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describehostreservationofferingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_host_reservations"]
    ) -> DescribeHostReservationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeHostReservations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describehostreservationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_hosts"]) -> DescribeHostsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeHosts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describehostspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_iam_instance_profile_associations"]
    ) -> DescribeIamInstanceProfileAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeIamInstanceProfileAssociations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeiaminstanceprofileassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_import_image_tasks"]
    ) -> DescribeImportImageTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeImportImageTasks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeimportimagetaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_import_snapshot_tasks"]
    ) -> DescribeImportSnapshotTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeImportSnapshotTasks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeimportsnapshottaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_credit_specifications"]
    ) -> DescribeInstanceCreditSpecificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeInstanceCreditSpecifications)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancecreditspecificationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_status"]
    ) -> DescribeInstanceStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeInstanceStatus)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancestatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_type_offerings"]
    ) -> DescribeInstanceTypeOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTypeOfferings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancetypeofferingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_types"]
    ) -> DescribeInstanceTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTypes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancetypespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instances"]
    ) -> DescribeInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeInstances)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_internet_gateways"]
    ) -> DescribeInternetGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeInternetGateways)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinternetgatewayspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ipv6_pools"]
    ) -> DescribeIpv6PoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeIpv6Pools)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipv6poolspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_launch_template_versions"]
    ) -> DescribeLaunchTemplateVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplateVersions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelaunchtemplateversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_launch_templates"]
    ) -> DescribeLaunchTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplates)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelaunchtemplatespaginator)
        """

    @overload
    def get_paginator(
        self,
        operation_name: Literal[
            "describe_local_gateway_route_table_virtual_interface_group_associations"
        ],
    ) -> DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayroutetablevirtualinterfacegroupassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_local_gateway_route_table_vpc_associations"]
    ) -> DescribeLocalGatewayRouteTableVpcAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTableVpcAssociations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayroutetablevpcassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_local_gateway_route_tables"]
    ) -> DescribeLocalGatewayRouteTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTables)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayroutetablespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_local_gateway_virtual_interface_groups"]
    ) -> DescribeLocalGatewayVirtualInterfaceGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaceGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayvirtualinterfacegroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_local_gateway_virtual_interfaces"]
    ) -> DescribeLocalGatewayVirtualInterfacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaces)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayvirtualinterfacespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_local_gateways"]
    ) -> DescribeLocalGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeLocalGateways)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_managed_prefix_lists"]
    ) -> DescribeManagedPrefixListsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeManagedPrefixLists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describemanagedprefixlistspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_moving_addresses"]
    ) -> DescribeMovingAddressesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeMovingAddresses)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describemovingaddressespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_nat_gateways"]
    ) -> DescribeNatGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeNatGateways)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenatgatewayspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_acls"]
    ) -> DescribeNetworkAclsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeNetworkAcls)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkaclspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_insights_analyses"]
    ) -> DescribeNetworkInsightsAnalysesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsAnalyses)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinsightsanalysespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_insights_paths"]
    ) -> DescribeNetworkInsightsPathsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsPaths)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinsightspathspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_interface_permissions"]
    ) -> DescribeNetworkInterfacePermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfacePermissions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinterfacepermissionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_interfaces"]
    ) -> DescribeNetworkInterfacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfaces)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinterfacespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_prefix_lists"]
    ) -> DescribePrefixListsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribePrefixLists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeprefixlistspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_principal_id_format"]
    ) -> DescribePrincipalIdFormatPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribePrincipalIdFormat)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeprincipalidformatpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_public_ipv4_pools"]
    ) -> DescribePublicIpv4PoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribePublicIpv4Pools)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describepublicipv4poolspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replace_root_volume_tasks"]
    ) -> DescribeReplaceRootVolumeTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeReplaceRootVolumeTasks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describereplacerootvolumetaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_instances_modifications"]
    ) -> DescribeReservedInstancesModificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesModifications)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describereservedinstancesmodificationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_instances_offerings"]
    ) -> DescribeReservedInstancesOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesOfferings)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describereservedinstancesofferingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_route_tables"]
    ) -> DescribeRouteTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeRouteTables)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeroutetablespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_instance_availability"]
    ) -> DescribeScheduledInstanceAvailabilityPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstanceAvailability)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describescheduledinstanceavailabilitypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_instances"]
    ) -> DescribeScheduledInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstances)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describescheduledinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_security_groups"]
    ) -> DescribeSecurityGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeSecurityGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesecuritygroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshots"]
    ) -> DescribeSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeSnapshots)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesnapshotspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_fleet_instances"]
    ) -> DescribeSpotFleetInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetInstances)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotfleetinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_fleet_requests"]
    ) -> DescribeSpotFleetRequestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetRequests)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotfleetrequestspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_instance_requests"]
    ) -> DescribeSpotInstanceRequestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeSpotInstanceRequests)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotinstancerequestspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_price_history"]
    ) -> DescribeSpotPriceHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeSpotPriceHistory)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotpricehistorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_stale_security_groups"]
    ) -> DescribeStaleSecurityGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeStaleSecurityGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describestalesecuritygroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_store_image_tasks"]
    ) -> DescribeStoreImageTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeStoreImageTasks)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describestoreimagetaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subnets"]
    ) -> DescribeSubnetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeSubnets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesubnetspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_tags"]) -> DescribeTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeTags)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetagspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_traffic_mirror_filters"]
    ) -> DescribeTrafficMirrorFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorFilters)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetrafficmirrorfilterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_traffic_mirror_sessions"]
    ) -> DescribeTrafficMirrorSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorSessions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetrafficmirrorsessionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_traffic_mirror_targets"]
    ) -> DescribeTrafficMirrorTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorTargets)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetrafficmirrortargetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_attachments"]
    ) -> DescribeTransitGatewayAttachmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayAttachments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayattachmentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_connect_peers"]
    ) -> DescribeTransitGatewayConnectPeersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayConnectPeers)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayconnectpeerspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_connects"]
    ) -> DescribeTransitGatewayConnectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayConnects)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayconnectspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_multicast_domains"]
    ) -> DescribeTransitGatewayMulticastDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayMulticastDomains)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewaymulticastdomainspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_peering_attachments"]
    ) -> DescribeTransitGatewayPeeringAttachmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayPeeringAttachments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewaypeeringattachmentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_route_tables"]
    ) -> DescribeTransitGatewayRouteTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayRouteTables)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayroutetablespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_vpc_attachments"]
    ) -> DescribeTransitGatewayVpcAttachmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayVpcAttachments)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayvpcattachmentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateways"]
    ) -> DescribeTransitGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeTransitGateways)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_volume_status"]
    ) -> DescribeVolumeStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeVolumeStatus)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevolumestatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_volumes"]
    ) -> DescribeVolumesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeVolumes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevolumespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_volumes_modifications"]
    ) -> DescribeVolumesModificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeVolumesModifications)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevolumesmodificationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_classic_link_dns_support"]
    ) -> DescribeVpcClassicLinkDnsSupportPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeVpcClassicLinkDnsSupport)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcclassiclinkdnssupportpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_connection_notifications"]
    ) -> DescribeVpcEndpointConnectionNotificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnectionNotifications)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointconnectionnotificationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_connections"]
    ) -> DescribeVpcEndpointConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnections)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointconnectionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_service_configurations"]
    ) -> DescribeVpcEndpointServiceConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServiceConfigurations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointserviceconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_service_permissions"]
    ) -> DescribeVpcEndpointServicePermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServicePermissions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointservicepermissionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_services"]
    ) -> DescribeVpcEndpointServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServices)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointservicespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoints"]
    ) -> DescribeVpcEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpoints)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_peering_connections"]
    ) -> DescribeVpcPeeringConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeVpcPeeringConnections)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcpeeringconnectionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_vpcs"]) -> DescribeVpcsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.DescribeVpcs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_associated_ipv6_pool_cidrs"]
    ) -> GetAssociatedIpv6PoolCidrsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.GetAssociatedIpv6PoolCidrs)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getassociatedipv6poolcidrspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_groups_for_capacity_reservation"]
    ) -> GetGroupsForCapacityReservationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.GetGroupsForCapacityReservation)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getgroupsforcapacityreservationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_managed_prefix_list_associations"]
    ) -> GetManagedPrefixListAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.GetManagedPrefixListAssociations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getmanagedprefixlistassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_managed_prefix_list_entries"]
    ) -> GetManagedPrefixListEntriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.GetManagedPrefixListEntries)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getmanagedprefixlistentriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_attachment_propagations"]
    ) -> GetTransitGatewayAttachmentPropagationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayAttachmentPropagations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayattachmentpropagationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_multicast_domain_associations"]
    ) -> GetTransitGatewayMulticastDomainAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayMulticastDomainAssociations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewaymulticastdomainassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_prefix_list_references"]
    ) -> GetTransitGatewayPrefixListReferencesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayPrefixListReferences)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayprefixlistreferencespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_route_table_associations"]
    ) -> GetTransitGatewayRouteTableAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTableAssociations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayroutetableassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_route_table_propagations"]
    ) -> GetTransitGatewayRouteTablePropagationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTablePropagations)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayroutetablepropagationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_local_gateway_routes"]
    ) -> SearchLocalGatewayRoutesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.SearchLocalGatewayRoutes)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#searchlocalgatewayroutespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_transit_gateway_multicast_groups"]
    ) -> SearchTransitGatewayMulticastGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Paginator.SearchTransitGatewayMulticastGroups)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#searchtransitgatewaymulticastgroupspaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bundle_task_complete"]) -> BundleTaskCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.bundle_task_complete)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#bundletaskcompletewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["conversion_task_cancelled"]
    ) -> ConversionTaskCancelledWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.conversion_task_cancelled)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#conversiontaskcancelledwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["conversion_task_completed"]
    ) -> ConversionTaskCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.conversion_task_completed)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#conversiontaskcompletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["conversion_task_deleted"]
    ) -> ConversionTaskDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.conversion_task_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#conversiontaskdeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["customer_gateway_available"]
    ) -> CustomerGatewayAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.customer_gateway_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#customergatewayavailablewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["export_task_cancelled"]
    ) -> ExportTaskCancelledWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.export_task_cancelled)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#exporttaskcancelledwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["export_task_completed"]
    ) -> ExportTaskCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.export_task_completed)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#exporttaskcompletedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["image_available"]) -> ImageAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.image_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#imageavailablewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["image_exists"]) -> ImageExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.image_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#imageexistswaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_exists"]) -> InstanceExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.instance_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#instanceexistswaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_running"]) -> InstanceRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.instance_running)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#instancerunningwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_status_ok"]) -> InstanceStatusOkWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.instance_status_ok)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#instancestatusokwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_stopped"]) -> InstanceStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.instance_stopped)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#instancestoppedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_terminated"]) -> InstanceTerminatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.instance_terminated)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#instanceterminatedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["key_pair_exists"]) -> KeyPairExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.key_pair_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#keypairexistswaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["nat_gateway_available"]
    ) -> NatGatewayAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.nat_gateway_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#natgatewayavailablewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["network_interface_available"]
    ) -> NetworkInterfaceAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.network_interface_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#networkinterfaceavailablewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["password_data_available"]
    ) -> PasswordDataAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.password_data_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#passworddataavailablewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["security_group_exists"]
    ) -> SecurityGroupExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.security_group_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#securitygroupexistswaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["snapshot_completed"]) -> SnapshotCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.snapshot_completed)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#snapshotcompletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["spot_instance_request_fulfilled"]
    ) -> SpotInstanceRequestFulfilledWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.spot_instance_request_fulfilled)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#spotinstancerequestfulfilledwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["subnet_available"]) -> SubnetAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.subnet_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#subnetavailablewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["system_status_ok"]) -> SystemStatusOkWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.system_status_ok)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#systemstatusokwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["volume_available"]) -> VolumeAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.volume_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#volumeavailablewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["volume_deleted"]) -> VolumeDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.volume_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#volumedeletedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["volume_in_use"]) -> VolumeInUseWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.volume_in_use)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#volumeinusewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["vpc_available"]) -> VpcAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.vpc_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#vpcavailablewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["vpc_exists"]) -> VpcExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.vpc_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#vpcexistswaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpc_peering_connection_deleted"]
    ) -> VpcPeeringConnectionDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.vpc_peering_connection_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#vpcpeeringconnectiondeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpc_peering_connection_exists"]
    ) -> VpcPeeringConnectionExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.vpc_peering_connection_exists)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#vpcpeeringconnectionexistswaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpn_connection_available"]
    ) -> VpnConnectionAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.vpn_connection_available)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#vpnconnectionavailablewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpn_connection_deleted"]
    ) -> VpnConnectionDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/ec2.html#EC2.Waiter.vpn_connection_deleted)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#vpnconnectiondeletedwaiter)
        """
