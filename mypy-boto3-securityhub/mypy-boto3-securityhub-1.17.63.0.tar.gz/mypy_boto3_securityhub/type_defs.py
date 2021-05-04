"""
Type annotations for securityhub service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_securityhub/type_defs.html)

Usage::

    ```python
    from mypy_boto3_securityhub.type_defs import AccountDetailsTypeDef

    data: AccountDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_securityhub.literals import (
    AdminStatus,
    AwsIamAccessKeyStatus,
    ComplianceStatus,
    ControlStatus,
    IntegrationType,
    MalwareState,
    MalwareType,
    MapFilterComparison,
    NetworkDirection,
    Partition,
    RecordState,
    SeverityLabel,
    SeverityRating,
    SortOrder,
    StandardsStatus,
    StringFilterComparison,
    ThreatIntelIndicatorCategory,
    ThreatIntelIndicatorType,
    VerificationState,
    WorkflowState,
    WorkflowStatus,
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
    "AccountDetailsTypeDef",
    "ActionLocalIpDetailsTypeDef",
    "ActionLocalPortDetailsTypeDef",
    "ActionRemoteIpDetailsTypeDef",
    "ActionRemotePortDetailsTypeDef",
    "ActionTargetTypeDef",
    "ActionTypeDef",
    "AdminAccountTypeDef",
    "AvailabilityZoneTypeDef",
    "AwsApiCallActionDomainDetailsTypeDef",
    "AwsApiCallActionTypeDef",
    "AwsApiGatewayAccessLogSettingsTypeDef",
    "AwsApiGatewayCanarySettingsTypeDef",
    "AwsApiGatewayEndpointConfigurationTypeDef",
    "AwsApiGatewayMethodSettingsTypeDef",
    "AwsApiGatewayRestApiDetailsTypeDef",
    "AwsApiGatewayStageDetailsTypeDef",
    "AwsApiGatewayV2ApiDetailsTypeDef",
    "AwsApiGatewayV2RouteSettingsTypeDef",
    "AwsApiGatewayV2StageDetailsTypeDef",
    "AwsAutoScalingAutoScalingGroupDetailsTypeDef",
    "AwsCertificateManagerCertificateDetailsTypeDef",
    "AwsCertificateManagerCertificateDomainValidationOptionTypeDef",
    "AwsCertificateManagerCertificateExtendedKeyUsageTypeDef",
    "AwsCertificateManagerCertificateKeyUsageTypeDef",
    "AwsCertificateManagerCertificateOptionsTypeDef",
    "AwsCertificateManagerCertificateRenewalSummaryTypeDef",
    "AwsCertificateManagerCertificateResourceRecordTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorTypeDef",
    "AwsCloudFrontDistributionCacheBehaviorsTypeDef",
    "AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef",
    "AwsCloudFrontDistributionDetailsTypeDef",
    "AwsCloudFrontDistributionLoggingTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef",
    "AwsCloudFrontDistributionOriginGroupFailoverTypeDef",
    "AwsCloudFrontDistributionOriginGroupTypeDef",
    "AwsCloudFrontDistributionOriginGroupsTypeDef",
    "AwsCloudFrontDistributionOriginItemTypeDef",
    "AwsCloudFrontDistributionOriginS3OriginConfigTypeDef",
    "AwsCloudFrontDistributionOriginsTypeDef",
    "AwsCloudTrailTrailDetailsTypeDef",
    "AwsCodeBuildProjectDetailsTypeDef",
    "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
    "AwsCodeBuildProjectEnvironmentTypeDef",
    "AwsCodeBuildProjectSourceTypeDef",
    "AwsCodeBuildProjectVpcConfigTypeDef",
    "AwsCorsConfigurationTypeDef",
    "AwsDynamoDbTableAttributeDefinitionTypeDef",
    "AwsDynamoDbTableBillingModeSummaryTypeDef",
    "AwsDynamoDbTableDetailsTypeDef",
    "AwsDynamoDbTableGlobalSecondaryIndexTypeDef",
    "AwsDynamoDbTableKeySchemaTypeDef",
    "AwsDynamoDbTableLocalSecondaryIndexTypeDef",
    "AwsDynamoDbTableProjectionTypeDef",
    "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef",
    "AwsDynamoDbTableProvisionedThroughputTypeDef",
    "AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef",
    "AwsDynamoDbTableReplicaTypeDef",
    "AwsDynamoDbTableRestoreSummaryTypeDef",
    "AwsDynamoDbTableSseDescriptionTypeDef",
    "AwsDynamoDbTableStreamSpecificationTypeDef",
    "AwsEc2EipDetailsTypeDef",
    "AwsEc2InstanceDetailsTypeDef",
    "AwsEc2NetworkAclAssociationTypeDef",
    "AwsEc2NetworkAclDetailsTypeDef",
    "AwsEc2NetworkAclEntryTypeDef",
    "AwsEc2NetworkInterfaceAttachmentTypeDef",
    "AwsEc2NetworkInterfaceDetailsTypeDef",
    "AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef",
    "AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef",
    "AwsEc2NetworkInterfaceSecurityGroupTypeDef",
    "AwsEc2SecurityGroupDetailsTypeDef",
    "AwsEc2SecurityGroupIpPermissionTypeDef",
    "AwsEc2SecurityGroupIpRangeTypeDef",
    "AwsEc2SecurityGroupIpv6RangeTypeDef",
    "AwsEc2SecurityGroupPrefixListIdTypeDef",
    "AwsEc2SecurityGroupUserIdGroupPairTypeDef",
    "AwsEc2SubnetDetailsTypeDef",
    "AwsEc2VolumeAttachmentTypeDef",
    "AwsEc2VolumeDetailsTypeDef",
    "AwsEc2VpcDetailsTypeDef",
    "AwsElasticBeanstalkEnvironmentDetailsTypeDef",
    "AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef",
    "AwsElasticBeanstalkEnvironmentOptionSettingTypeDef",
    "AwsElasticBeanstalkEnvironmentTierTypeDef",
    "AwsElasticsearchDomainDetailsTypeDef",
    "AwsElasticsearchDomainDomainEndpointOptionsTypeDef",
    "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef",
    "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef",
    "AwsElasticsearchDomainVPCOptionsTypeDef",
    "AwsElbAppCookieStickinessPolicyTypeDef",
    "AwsElbLbCookieStickinessPolicyTypeDef",
    "AwsElbLoadBalancerAccessLogTypeDef",
    "AwsElbLoadBalancerAttributesTypeDef",
    "AwsElbLoadBalancerBackendServerDescriptionTypeDef",
    "AwsElbLoadBalancerConnectionDrainingTypeDef",
    "AwsElbLoadBalancerConnectionSettingsTypeDef",
    "AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef",
    "AwsElbLoadBalancerDetailsTypeDef",
    "AwsElbLoadBalancerHealthCheckTypeDef",
    "AwsElbLoadBalancerInstanceTypeDef",
    "AwsElbLoadBalancerListenerDescriptionTypeDef",
    "AwsElbLoadBalancerListenerTypeDef",
    "AwsElbLoadBalancerPoliciesTypeDef",
    "AwsElbLoadBalancerSourceSecurityGroupTypeDef",
    "AwsElbv2LoadBalancerDetailsTypeDef",
    "AwsIamAccessKeyDetailsTypeDef",
    "AwsIamAccessKeySessionContextAttributesTypeDef",
    "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    "AwsIamAccessKeySessionContextTypeDef",
    "AwsIamAttachedManagedPolicyTypeDef",
    "AwsIamGroupDetailsTypeDef",
    "AwsIamGroupPolicyTypeDef",
    "AwsIamInstanceProfileRoleTypeDef",
    "AwsIamInstanceProfileTypeDef",
    "AwsIamPermissionsBoundaryTypeDef",
    "AwsIamPolicyDetailsTypeDef",
    "AwsIamPolicyVersionTypeDef",
    "AwsIamRoleDetailsTypeDef",
    "AwsIamRolePolicyTypeDef",
    "AwsIamUserDetailsTypeDef",
    "AwsIamUserPolicyTypeDef",
    "AwsKmsKeyDetailsTypeDef",
    "AwsLambdaFunctionCodeTypeDef",
    "AwsLambdaFunctionDeadLetterConfigTypeDef",
    "AwsLambdaFunctionDetailsTypeDef",
    "AwsLambdaFunctionEnvironmentErrorTypeDef",
    "AwsLambdaFunctionEnvironmentTypeDef",
    "AwsLambdaFunctionLayerTypeDef",
    "AwsLambdaFunctionTracingConfigTypeDef",
    "AwsLambdaFunctionVpcConfigTypeDef",
    "AwsLambdaLayerVersionDetailsTypeDef",
    "AwsRdsDbClusterAssociatedRoleTypeDef",
    "AwsRdsDbClusterDetailsTypeDef",
    "AwsRdsDbClusterMemberTypeDef",
    "AwsRdsDbClusterOptionGroupMembershipTypeDef",
    "AwsRdsDbClusterSnapshotDetailsTypeDef",
    "AwsRdsDbDomainMembershipTypeDef",
    "AwsRdsDbInstanceAssociatedRoleTypeDef",
    "AwsRdsDbInstanceDetailsTypeDef",
    "AwsRdsDbInstanceEndpointTypeDef",
    "AwsRdsDbInstanceVpcSecurityGroupTypeDef",
    "AwsRdsDbOptionGroupMembershipTypeDef",
    "AwsRdsDbParameterGroupTypeDef",
    "AwsRdsDbPendingModifiedValuesTypeDef",
    "AwsRdsDbProcessorFeatureTypeDef",
    "AwsRdsDbSnapshotDetailsTypeDef",
    "AwsRdsDbStatusInfoTypeDef",
    "AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef",
    "AwsRdsDbSubnetGroupSubnetTypeDef",
    "AwsRdsDbSubnetGroupTypeDef",
    "AwsRdsPendingCloudWatchLogsExportsTypeDef",
    "AwsRedshiftClusterClusterNodeTypeDef",
    "AwsRedshiftClusterClusterParameterGroupTypeDef",
    "AwsRedshiftClusterClusterParameterStatusTypeDef",
    "AwsRedshiftClusterClusterSecurityGroupTypeDef",
    "AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef",
    "AwsRedshiftClusterDeferredMaintenanceWindowTypeDef",
    "AwsRedshiftClusterDetailsTypeDef",
    "AwsRedshiftClusterElasticIpStatusTypeDef",
    "AwsRedshiftClusterEndpointTypeDef",
    "AwsRedshiftClusterHsmStatusTypeDef",
    "AwsRedshiftClusterIamRoleTypeDef",
    "AwsRedshiftClusterPendingModifiedValuesTypeDef",
    "AwsRedshiftClusterResizeInfoTypeDef",
    "AwsRedshiftClusterRestoreStatusTypeDef",
    "AwsRedshiftClusterVpcSecurityGroupTypeDef",
    "AwsS3AccountPublicAccessBlockDetailsTypeDef",
    "AwsS3BucketDetailsTypeDef",
    "AwsS3BucketServerSideEncryptionByDefaultTypeDef",
    "AwsS3BucketServerSideEncryptionConfigurationTypeDef",
    "AwsS3BucketServerSideEncryptionRuleTypeDef",
    "AwsS3ObjectDetailsTypeDef",
    "AwsSecretsManagerSecretDetailsTypeDef",
    "AwsSecretsManagerSecretRotationRulesTypeDef",
    "AwsSecurityFindingFiltersTypeDef",
    "AwsSecurityFindingIdentifierTypeDef",
    "AwsSecurityFindingTypeDef",
    "AwsSnsTopicDetailsTypeDef",
    "AwsSnsTopicSubscriptionTypeDef",
    "AwsSqsQueueDetailsTypeDef",
    "AwsSsmComplianceSummaryTypeDef",
    "AwsSsmPatchComplianceDetailsTypeDef",
    "AwsSsmPatchTypeDef",
    "AwsWafWebAclDetailsTypeDef",
    "AwsWafWebAclRuleTypeDef",
    "BatchDisableStandardsResponseTypeDef",
    "BatchEnableStandardsResponseTypeDef",
    "BatchImportFindingsResponseTypeDef",
    "BatchUpdateFindingsResponseTypeDef",
    "BatchUpdateFindingsUnprocessedFindingTypeDef",
    "CellTypeDef",
    "CidrBlockAssociationTypeDef",
    "CityTypeDef",
    "ClassificationResultTypeDef",
    "ClassificationStatusTypeDef",
    "ComplianceTypeDef",
    "ContainerDetailsTypeDef",
    "CountryTypeDef",
    "CreateActionTargetResponseTypeDef",
    "CreateInsightResponseTypeDef",
    "CreateMembersResponseTypeDef",
    "CustomDataIdentifiersDetectionsTypeDef",
    "CustomDataIdentifiersResultTypeDef",
    "CvssTypeDef",
    "DataClassificationDetailsTypeDef",
    "DateFilterTypeDef",
    "DateRangeTypeDef",
    "DeclineInvitationsResponseTypeDef",
    "DeleteActionTargetResponseTypeDef",
    "DeleteInsightResponseTypeDef",
    "DeleteInvitationsResponseTypeDef",
    "DeleteMembersResponseTypeDef",
    "DescribeActionTargetsResponseTypeDef",
    "DescribeHubResponseTypeDef",
    "DescribeOrganizationConfigurationResponseTypeDef",
    "DescribeProductsResponseTypeDef",
    "DescribeStandardsControlsResponseTypeDef",
    "DescribeStandardsResponseTypeDef",
    "DnsRequestActionTypeDef",
    "EnableImportFindingsForProductResponseTypeDef",
    "FindingProviderFieldsTypeDef",
    "FindingProviderSeverityTypeDef",
    "GeoLocationTypeDef",
    "GetAdministratorAccountResponseTypeDef",
    "GetEnabledStandardsResponseTypeDef",
    "GetFindingsResponseTypeDef",
    "GetInsightResultsResponseTypeDef",
    "GetInsightsResponseTypeDef",
    "GetInvitationsCountResponseTypeDef",
    "GetMasterAccountResponseTypeDef",
    "GetMembersResponseTypeDef",
    "IcmpTypeCodeTypeDef",
    "ImportFindingsErrorTypeDef",
    "InsightResultValueTypeDef",
    "InsightResultsTypeDef",
    "InsightTypeDef",
    "InvitationTypeDef",
    "InviteMembersResponseTypeDef",
    "IpFilterTypeDef",
    "IpOrganizationDetailsTypeDef",
    "Ipv6CidrBlockAssociationTypeDef",
    "KeywordFilterTypeDef",
    "ListEnabledProductsForImportResponseTypeDef",
    "ListInvitationsResponseTypeDef",
    "ListMembersResponseTypeDef",
    "ListOrganizationAdminAccountsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoadBalancerStateTypeDef",
    "MalwareTypeDef",
    "MapFilterTypeDef",
    "MemberTypeDef",
    "NetworkConnectionActionTypeDef",
    "NetworkHeaderTypeDef",
    "NetworkPathComponentDetailsTypeDef",
    "NetworkPathComponentTypeDef",
    "NetworkTypeDef",
    "NoteTypeDef",
    "NoteUpdateTypeDef",
    "NumberFilterTypeDef",
    "OccurrencesTypeDef",
    "PageTypeDef",
    "PaginatorConfigTypeDef",
    "PatchSummaryTypeDef",
    "PortProbeActionTypeDef",
    "PortProbeDetailTypeDef",
    "PortRangeFromToTypeDef",
    "PortRangeTypeDef",
    "ProcessDetailsTypeDef",
    "ProductTypeDef",
    "RangeTypeDef",
    "RecommendationTypeDef",
    "RecordTypeDef",
    "RelatedFindingTypeDef",
    "RemediationTypeDef",
    "ResourceDetailsTypeDef",
    "ResourceTypeDef",
    "ResultTypeDef",
    "SensitiveDataDetectionsTypeDef",
    "SensitiveDataResultTypeDef",
    "SeverityTypeDef",
    "SeverityUpdateTypeDef",
    "SoftwarePackageTypeDef",
    "SortCriterionTypeDef",
    "StandardTypeDef",
    "StandardsControlTypeDef",
    "StandardsSubscriptionRequestTypeDef",
    "StandardsSubscriptionTypeDef",
    "StatusReasonTypeDef",
    "StringFilterTypeDef",
    "ThreatIntelIndicatorTypeDef",
    "VulnerabilityTypeDef",
    "VulnerabilityVendorTypeDef",
    "WafActionTypeDef",
    "WafExcludedRuleTypeDef",
    "WafOverrideActionTypeDef",
    "WorkflowTypeDef",
    "WorkflowUpdateTypeDef",
)


class _RequiredAccountDetailsTypeDef(TypedDict):
    AccountId: str


class AccountDetailsTypeDef(_RequiredAccountDetailsTypeDef, total=False):
    Email: str


class ActionLocalIpDetailsTypeDef(TypedDict, total=False):
    IpAddressV4: str


class ActionLocalPortDetailsTypeDef(TypedDict, total=False):
    Port: int
    PortName: str


class ActionRemoteIpDetailsTypeDef(TypedDict, total=False):
    IpAddressV4: str
    Organization: "IpOrganizationDetailsTypeDef"
    Country: "CountryTypeDef"
    City: "CityTypeDef"
    GeoLocation: "GeoLocationTypeDef"


class ActionRemotePortDetailsTypeDef(TypedDict, total=False):
    Port: int
    PortName: str


class ActionTargetTypeDef(TypedDict):
    ActionTargetArn: str
    Name: str
    Description: str


class ActionTypeDef(TypedDict, total=False):
    ActionType: str
    NetworkConnectionAction: "NetworkConnectionActionTypeDef"
    AwsApiCallAction: "AwsApiCallActionTypeDef"
    DnsRequestAction: "DnsRequestActionTypeDef"
    PortProbeAction: "PortProbeActionTypeDef"


class AdminAccountTypeDef(TypedDict, total=False):
    AccountId: str
    Status: AdminStatus


class AvailabilityZoneTypeDef(TypedDict, total=False):
    ZoneName: str
    SubnetId: str


class AwsApiCallActionDomainDetailsTypeDef(TypedDict, total=False):
    Domain: str


class AwsApiCallActionTypeDef(TypedDict, total=False):
    Api: str
    ServiceName: str
    CallerType: str
    RemoteIpDetails: "ActionRemoteIpDetailsTypeDef"
    DomainDetails: "AwsApiCallActionDomainDetailsTypeDef"
    AffectedResources: Dict[str, str]
    FirstSeen: str
    LastSeen: str


class AwsApiGatewayAccessLogSettingsTypeDef(TypedDict, total=False):
    Format: str
    DestinationArn: str


class AwsApiGatewayCanarySettingsTypeDef(TypedDict, total=False):
    PercentTraffic: float
    DeploymentId: str
    StageVariableOverrides: Dict[str, str]
    UseStageCache: bool


class AwsApiGatewayEndpointConfigurationTypeDef(TypedDict, total=False):
    Types: List[str]


class AwsApiGatewayMethodSettingsTypeDef(TypedDict, total=False):
    MetricsEnabled: bool
    LoggingLevel: str
    DataTraceEnabled: bool
    ThrottlingBurstLimit: int
    ThrottlingRateLimit: float
    CachingEnabled: bool
    CacheTtlInSeconds: int
    CacheDataEncrypted: bool
    RequireAuthorizationForCacheControl: bool
    UnauthorizedCacheControlHeaderStrategy: str
    HttpMethod: str
    ResourcePath: str


class AwsApiGatewayRestApiDetailsTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Description: str
    CreatedDate: str
    Version: str
    BinaryMediaTypes: List[str]
    MinimumCompressionSize: int
    ApiKeySource: str
    EndpointConfiguration: "AwsApiGatewayEndpointConfigurationTypeDef"


class AwsApiGatewayStageDetailsTypeDef(TypedDict, total=False):
    DeploymentId: str
    ClientCertificateId: str
    StageName: str
    Description: str
    CacheClusterEnabled: bool
    CacheClusterSize: str
    CacheClusterStatus: str
    MethodSettings: List["AwsApiGatewayMethodSettingsTypeDef"]
    Variables: Dict[str, str]
    DocumentationVersion: str
    AccessLogSettings: "AwsApiGatewayAccessLogSettingsTypeDef"
    CanarySettings: "AwsApiGatewayCanarySettingsTypeDef"
    TracingEnabled: bool
    CreatedDate: str
    LastUpdatedDate: str
    WebAclArn: str


class AwsApiGatewayV2ApiDetailsTypeDef(TypedDict, total=False):
    ApiEndpoint: str
    ApiId: str
    ApiKeySelectionExpression: str
    CreatedDate: str
    Description: str
    Version: str
    Name: str
    ProtocolType: str
    RouteSelectionExpression: str
    CorsConfiguration: "AwsCorsConfigurationTypeDef"


class AwsApiGatewayV2RouteSettingsTypeDef(TypedDict, total=False):
    DetailedMetricsEnabled: bool
    LoggingLevel: str
    DataTraceEnabled: bool
    ThrottlingBurstLimit: int
    ThrottlingRateLimit: float


class AwsApiGatewayV2StageDetailsTypeDef(TypedDict, total=False):
    CreatedDate: str
    Description: str
    DefaultRouteSettings: "AwsApiGatewayV2RouteSettingsTypeDef"
    DeploymentId: str
    LastUpdatedDate: str
    RouteSettings: "AwsApiGatewayV2RouteSettingsTypeDef"
    StageName: str
    StageVariables: Dict[str, str]
    AccessLogSettings: "AwsApiGatewayAccessLogSettingsTypeDef"
    AutoDeploy: bool
    LastDeploymentStatusMessage: str
    ApiGatewayManaged: bool


class AwsAutoScalingAutoScalingGroupDetailsTypeDef(TypedDict, total=False):
    LaunchConfigurationName: str
    LoadBalancerNames: List[str]
    HealthCheckType: str
    HealthCheckGracePeriod: int
    CreatedTime: str


AwsCertificateManagerCertificateDetailsTypeDef = TypedDict(
    "AwsCertificateManagerCertificateDetailsTypeDef",
    {
        "CertificateAuthorityArn": str,
        "CreatedAt": str,
        "DomainName": str,
        "DomainValidationOptions": List[
            "AwsCertificateManagerCertificateDomainValidationOptionTypeDef"
        ],
        "ExtendedKeyUsages": List["AwsCertificateManagerCertificateExtendedKeyUsageTypeDef"],
        "FailureReason": str,
        "ImportedAt": str,
        "InUseBy": List[str],
        "IssuedAt": str,
        "Issuer": str,
        "KeyAlgorithm": str,
        "KeyUsages": List["AwsCertificateManagerCertificateKeyUsageTypeDef"],
        "NotAfter": str,
        "NotBefore": str,
        "Options": "AwsCertificateManagerCertificateOptionsTypeDef",
        "RenewalEligibility": str,
        "RenewalSummary": "AwsCertificateManagerCertificateRenewalSummaryTypeDef",
        "Serial": str,
        "SignatureAlgorithm": str,
        "Status": str,
        "Subject": str,
        "SubjectAlternativeNames": List[str],
        "Type": str,
    },
    total=False,
)


class AwsCertificateManagerCertificateDomainValidationOptionTypeDef(TypedDict, total=False):
    DomainName: str
    ResourceRecord: "AwsCertificateManagerCertificateResourceRecordTypeDef"
    ValidationDomain: str
    ValidationEmails: List[str]
    ValidationMethod: str
    ValidationStatus: str


class AwsCertificateManagerCertificateExtendedKeyUsageTypeDef(TypedDict, total=False):
    Name: str
    OId: str


class AwsCertificateManagerCertificateKeyUsageTypeDef(TypedDict, total=False):
    Name: str


class AwsCertificateManagerCertificateOptionsTypeDef(TypedDict, total=False):
    CertificateTransparencyLoggingPreference: str


class AwsCertificateManagerCertificateRenewalSummaryTypeDef(TypedDict, total=False):
    DomainValidationOptions: List["AwsCertificateManagerCertificateDomainValidationOptionTypeDef"]
    RenewalStatus: str
    RenewalStatusReason: str
    UpdatedAt: str


AwsCertificateManagerCertificateResourceRecordTypeDef = TypedDict(
    "AwsCertificateManagerCertificateResourceRecordTypeDef",
    {"Name": str, "Type": str, "Value": str},
    total=False,
)


class AwsCloudFrontDistributionCacheBehaviorTypeDef(TypedDict, total=False):
    ViewerProtocolPolicy: str


class AwsCloudFrontDistributionCacheBehaviorsTypeDef(TypedDict, total=False):
    Items: List["AwsCloudFrontDistributionCacheBehaviorTypeDef"]


class AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef(TypedDict, total=False):
    ViewerProtocolPolicy: str


class AwsCloudFrontDistributionDetailsTypeDef(TypedDict, total=False):
    CacheBehaviors: "AwsCloudFrontDistributionCacheBehaviorsTypeDef"
    DefaultCacheBehavior: "AwsCloudFrontDistributionDefaultCacheBehaviorTypeDef"
    DefaultRootObject: str
    DomainName: str
    ETag: str
    LastModifiedTime: str
    Logging: "AwsCloudFrontDistributionLoggingTypeDef"
    Origins: "AwsCloudFrontDistributionOriginsTypeDef"
    OriginGroups: "AwsCloudFrontDistributionOriginGroupsTypeDef"
    Status: str
    WebAclId: str


class AwsCloudFrontDistributionLoggingTypeDef(TypedDict, total=False):
    Bucket: str
    Enabled: bool
    IncludeCookies: bool
    Prefix: str


class AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef(TypedDict, total=False):
    Items: List[int]
    Quantity: int


class AwsCloudFrontDistributionOriginGroupFailoverTypeDef(TypedDict, total=False):
    StatusCodes: "AwsCloudFrontDistributionOriginGroupFailoverStatusCodesTypeDef"


class AwsCloudFrontDistributionOriginGroupTypeDef(TypedDict, total=False):
    FailoverCriteria: "AwsCloudFrontDistributionOriginGroupFailoverTypeDef"


class AwsCloudFrontDistributionOriginGroupsTypeDef(TypedDict, total=False):
    Items: List["AwsCloudFrontDistributionOriginGroupTypeDef"]


class AwsCloudFrontDistributionOriginItemTypeDef(TypedDict, total=False):
    DomainName: str
    Id: str
    OriginPath: str
    S3OriginConfig: "AwsCloudFrontDistributionOriginS3OriginConfigTypeDef"


class AwsCloudFrontDistributionOriginS3OriginConfigTypeDef(TypedDict, total=False):
    OriginAccessIdentity: str


class AwsCloudFrontDistributionOriginsTypeDef(TypedDict, total=False):
    Items: List["AwsCloudFrontDistributionOriginItemTypeDef"]


class AwsCloudTrailTrailDetailsTypeDef(TypedDict, total=False):
    CloudWatchLogsLogGroupArn: str
    CloudWatchLogsRoleArn: str
    HasCustomEventSelectors: bool
    HomeRegion: str
    IncludeGlobalServiceEvents: bool
    IsMultiRegionTrail: bool
    IsOrganizationTrail: bool
    KmsKeyId: str
    LogFileValidationEnabled: bool
    Name: str
    S3BucketName: str
    S3KeyPrefix: str
    SnsTopicArn: str
    SnsTopicName: str
    TrailArn: str


class AwsCodeBuildProjectDetailsTypeDef(TypedDict, total=False):
    EncryptionKey: str
    Environment: "AwsCodeBuildProjectEnvironmentTypeDef"
    Name: str
    Source: "AwsCodeBuildProjectSourceTypeDef"
    ServiceRole: str
    VpcConfig: "AwsCodeBuildProjectVpcConfigTypeDef"


class AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef(TypedDict, total=False):
    Credential: str
    CredentialProvider: str


AwsCodeBuildProjectEnvironmentTypeDef = TypedDict(
    "AwsCodeBuildProjectEnvironmentTypeDef",
    {
        "Certificate": str,
        "ImagePullCredentialsType": str,
        "RegistryCredential": "AwsCodeBuildProjectEnvironmentRegistryCredentialTypeDef",
        "Type": str,
    },
    total=False,
)

AwsCodeBuildProjectSourceTypeDef = TypedDict(
    "AwsCodeBuildProjectSourceTypeDef",
    {"Type": str, "Location": str, "GitCloneDepth": int, "InsecureSsl": bool},
    total=False,
)


class AwsCodeBuildProjectVpcConfigTypeDef(TypedDict, total=False):
    VpcId: str
    Subnets: List[str]
    SecurityGroupIds: List[str]


class AwsCorsConfigurationTypeDef(TypedDict, total=False):
    AllowOrigins: List[str]
    AllowCredentials: bool
    ExposeHeaders: List[str]
    MaxAge: int
    AllowMethods: List[str]
    AllowHeaders: List[str]


class AwsDynamoDbTableAttributeDefinitionTypeDef(TypedDict, total=False):
    AttributeName: str
    AttributeType: str


class AwsDynamoDbTableBillingModeSummaryTypeDef(TypedDict, total=False):
    BillingMode: str
    LastUpdateToPayPerRequestDateTime: str


class AwsDynamoDbTableDetailsTypeDef(TypedDict, total=False):
    AttributeDefinitions: List["AwsDynamoDbTableAttributeDefinitionTypeDef"]
    BillingModeSummary: "AwsDynamoDbTableBillingModeSummaryTypeDef"
    CreationDateTime: str
    GlobalSecondaryIndexes: List["AwsDynamoDbTableGlobalSecondaryIndexTypeDef"]
    GlobalTableVersion: str
    ItemCount: int
    KeySchema: List["AwsDynamoDbTableKeySchemaTypeDef"]
    LatestStreamArn: str
    LatestStreamLabel: str
    LocalSecondaryIndexes: List["AwsDynamoDbTableLocalSecondaryIndexTypeDef"]
    ProvisionedThroughput: "AwsDynamoDbTableProvisionedThroughputTypeDef"
    Replicas: List["AwsDynamoDbTableReplicaTypeDef"]
    RestoreSummary: "AwsDynamoDbTableRestoreSummaryTypeDef"
    SseDescription: "AwsDynamoDbTableSseDescriptionTypeDef"
    StreamSpecification: "AwsDynamoDbTableStreamSpecificationTypeDef"
    TableId: str
    TableName: str
    TableSizeBytes: int
    TableStatus: str


class AwsDynamoDbTableGlobalSecondaryIndexTypeDef(TypedDict, total=False):
    Backfilling: bool
    IndexArn: str
    IndexName: str
    IndexSizeBytes: int
    IndexStatus: str
    ItemCount: int
    KeySchema: List["AwsDynamoDbTableKeySchemaTypeDef"]
    Projection: "AwsDynamoDbTableProjectionTypeDef"
    ProvisionedThroughput: "AwsDynamoDbTableProvisionedThroughputTypeDef"


class AwsDynamoDbTableKeySchemaTypeDef(TypedDict, total=False):
    AttributeName: str
    KeyType: str


class AwsDynamoDbTableLocalSecondaryIndexTypeDef(TypedDict, total=False):
    IndexArn: str
    IndexName: str
    KeySchema: List["AwsDynamoDbTableKeySchemaTypeDef"]
    Projection: "AwsDynamoDbTableProjectionTypeDef"


class AwsDynamoDbTableProjectionTypeDef(TypedDict, total=False):
    NonKeyAttributes: List[str]
    ProjectionType: str


class AwsDynamoDbTableProvisionedThroughputOverrideTypeDef(TypedDict, total=False):
    ReadCapacityUnits: int


class AwsDynamoDbTableProvisionedThroughputTypeDef(TypedDict, total=False):
    LastDecreaseDateTime: str
    LastIncreaseDateTime: str
    NumberOfDecreasesToday: int
    ReadCapacityUnits: int
    WriteCapacityUnits: int


class AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef(TypedDict, total=False):
    IndexName: str
    ProvisionedThroughputOverride: "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef"


class AwsDynamoDbTableReplicaTypeDef(TypedDict, total=False):
    GlobalSecondaryIndexes: List["AwsDynamoDbTableReplicaGlobalSecondaryIndexTypeDef"]
    KmsMasterKeyId: str
    ProvisionedThroughputOverride: "AwsDynamoDbTableProvisionedThroughputOverrideTypeDef"
    RegionName: str
    ReplicaStatus: str
    ReplicaStatusDescription: str


class AwsDynamoDbTableRestoreSummaryTypeDef(TypedDict, total=False):
    SourceBackupArn: str
    SourceTableArn: str
    RestoreDateTime: str
    RestoreInProgress: bool


class AwsDynamoDbTableSseDescriptionTypeDef(TypedDict, total=False):
    InaccessibleEncryptionDateTime: str
    Status: str
    SseType: str
    KmsMasterKeyArn: str


class AwsDynamoDbTableStreamSpecificationTypeDef(TypedDict, total=False):
    StreamEnabled: bool
    StreamViewType: str


class AwsEc2EipDetailsTypeDef(TypedDict, total=False):
    InstanceId: str
    PublicIp: str
    AllocationId: str
    AssociationId: str
    Domain: str
    PublicIpv4Pool: str
    NetworkBorderGroup: str
    NetworkInterfaceId: str
    NetworkInterfaceOwnerId: str
    PrivateIpAddress: str


AwsEc2InstanceDetailsTypeDef = TypedDict(
    "AwsEc2InstanceDetailsTypeDef",
    {
        "Type": str,
        "ImageId": str,
        "IpV4Addresses": List[str],
        "IpV6Addresses": List[str],
        "KeyName": str,
        "IamInstanceProfileArn": str,
        "VpcId": str,
        "SubnetId": str,
        "LaunchedAt": str,
    },
    total=False,
)


class AwsEc2NetworkAclAssociationTypeDef(TypedDict, total=False):
    NetworkAclAssociationId: str
    NetworkAclId: str
    SubnetId: str


class AwsEc2NetworkAclDetailsTypeDef(TypedDict, total=False):
    IsDefault: bool
    NetworkAclId: str
    OwnerId: str
    VpcId: str
    Associations: List["AwsEc2NetworkAclAssociationTypeDef"]
    Entries: List["AwsEc2NetworkAclEntryTypeDef"]


AwsEc2NetworkAclEntryTypeDef = TypedDict(
    "AwsEc2NetworkAclEntryTypeDef",
    {
        "CidrBlock": str,
        "Egress": bool,
        "IcmpTypeCode": "IcmpTypeCodeTypeDef",
        "Ipv6CidrBlock": str,
        "PortRange": "PortRangeFromToTypeDef",
        "Protocol": str,
        "RuleAction": str,
        "RuleNumber": int,
    },
    total=False,
)


class AwsEc2NetworkInterfaceAttachmentTypeDef(TypedDict, total=False):
    AttachTime: str
    AttachmentId: str
    DeleteOnTermination: bool
    DeviceIndex: int
    InstanceId: str
    InstanceOwnerId: str
    Status: str


class AwsEc2NetworkInterfaceDetailsTypeDef(TypedDict, total=False):
    Attachment: "AwsEc2NetworkInterfaceAttachmentTypeDef"
    NetworkInterfaceId: str
    SecurityGroups: List["AwsEc2NetworkInterfaceSecurityGroupTypeDef"]
    SourceDestCheck: bool
    IpV6Addresses: List["AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef"]
    PrivateIpAddresses: List["AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef"]
    PublicDnsName: str
    PublicIp: str


class AwsEc2NetworkInterfaceIpV6AddressDetailTypeDef(TypedDict, total=False):
    IpV6Address: str


class AwsEc2NetworkInterfacePrivateIpAddressDetailTypeDef(TypedDict, total=False):
    PrivateIpAddress: str
    PrivateDnsName: str


class AwsEc2NetworkInterfaceSecurityGroupTypeDef(TypedDict, total=False):
    GroupName: str
    GroupId: str


class AwsEc2SecurityGroupDetailsTypeDef(TypedDict, total=False):
    GroupName: str
    GroupId: str
    OwnerId: str
    VpcId: str
    IpPermissions: List["AwsEc2SecurityGroupIpPermissionTypeDef"]
    IpPermissionsEgress: List["AwsEc2SecurityGroupIpPermissionTypeDef"]


class AwsEc2SecurityGroupIpPermissionTypeDef(TypedDict, total=False):
    IpProtocol: str
    FromPort: int
    ToPort: int
    UserIdGroupPairs: List["AwsEc2SecurityGroupUserIdGroupPairTypeDef"]
    IpRanges: List["AwsEc2SecurityGroupIpRangeTypeDef"]
    Ipv6Ranges: List["AwsEc2SecurityGroupIpv6RangeTypeDef"]
    PrefixListIds: List["AwsEc2SecurityGroupPrefixListIdTypeDef"]


class AwsEc2SecurityGroupIpRangeTypeDef(TypedDict, total=False):
    CidrIp: str


class AwsEc2SecurityGroupIpv6RangeTypeDef(TypedDict, total=False):
    CidrIpv6: str


class AwsEc2SecurityGroupPrefixListIdTypeDef(TypedDict, total=False):
    PrefixListId: str


class AwsEc2SecurityGroupUserIdGroupPairTypeDef(TypedDict, total=False):
    GroupId: str
    GroupName: str
    PeeringStatus: str
    UserId: str
    VpcId: str
    VpcPeeringConnectionId: str


class AwsEc2SubnetDetailsTypeDef(TypedDict, total=False):
    AssignIpv6AddressOnCreation: bool
    AvailabilityZone: str
    AvailabilityZoneId: str
    AvailableIpAddressCount: int
    CidrBlock: str
    DefaultForAz: bool
    MapPublicIpOnLaunch: bool
    OwnerId: str
    State: str
    SubnetArn: str
    SubnetId: str
    VpcId: str
    Ipv6CidrBlockAssociationSet: List["Ipv6CidrBlockAssociationTypeDef"]


class AwsEc2VolumeAttachmentTypeDef(TypedDict, total=False):
    AttachTime: str
    DeleteOnTermination: bool
    InstanceId: str
    Status: str


class AwsEc2VolumeDetailsTypeDef(TypedDict, total=False):
    CreateTime: str
    Encrypted: bool
    Size: int
    SnapshotId: str
    Status: str
    KmsKeyId: str
    Attachments: List["AwsEc2VolumeAttachmentTypeDef"]


class AwsEc2VpcDetailsTypeDef(TypedDict, total=False):
    CidrBlockAssociationSet: List["CidrBlockAssociationTypeDef"]
    Ipv6CidrBlockAssociationSet: List["Ipv6CidrBlockAssociationTypeDef"]
    DhcpOptionsId: str
    State: str


class AwsElasticBeanstalkEnvironmentDetailsTypeDef(TypedDict, total=False):
    ApplicationName: str
    Cname: str
    DateCreated: str
    DateUpdated: str
    Description: str
    EndpointUrl: str
    EnvironmentArn: str
    EnvironmentId: str
    EnvironmentLinks: List["AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef"]
    EnvironmentName: str
    OptionSettings: List["AwsElasticBeanstalkEnvironmentOptionSettingTypeDef"]
    PlatformArn: str
    SolutionStackName: str
    Status: str
    Tier: "AwsElasticBeanstalkEnvironmentTierTypeDef"
    VersionLabel: str


class AwsElasticBeanstalkEnvironmentEnvironmentLinkTypeDef(TypedDict, total=False):
    EnvironmentName: str
    LinkName: str


class AwsElasticBeanstalkEnvironmentOptionSettingTypeDef(TypedDict, total=False):
    Namespace: str
    OptionName: str
    ResourceName: str
    Value: str


AwsElasticBeanstalkEnvironmentTierTypeDef = TypedDict(
    "AwsElasticBeanstalkEnvironmentTierTypeDef",
    {"Name": str, "Type": str, "Version": str},
    total=False,
)


class AwsElasticsearchDomainDetailsTypeDef(TypedDict, total=False):
    AccessPolicies: str
    DomainEndpointOptions: "AwsElasticsearchDomainDomainEndpointOptionsTypeDef"
    DomainId: str
    DomainName: str
    Endpoint: str
    Endpoints: Dict[str, str]
    ElasticsearchVersion: str
    EncryptionAtRestOptions: "AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef"
    NodeToNodeEncryptionOptions: "AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef"
    VPCOptions: "AwsElasticsearchDomainVPCOptionsTypeDef"


class AwsElasticsearchDomainDomainEndpointOptionsTypeDef(TypedDict, total=False):
    EnforceHTTPS: bool
    TLSSecurityPolicy: str


class AwsElasticsearchDomainEncryptionAtRestOptionsTypeDef(TypedDict, total=False):
    Enabled: bool
    KmsKeyId: str


class AwsElasticsearchDomainNodeToNodeEncryptionOptionsTypeDef(TypedDict, total=False):
    Enabled: bool


class AwsElasticsearchDomainVPCOptionsTypeDef(TypedDict, total=False):
    AvailabilityZones: List[str]
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    VPCId: str


class AwsElbAppCookieStickinessPolicyTypeDef(TypedDict, total=False):
    CookieName: str
    PolicyName: str


class AwsElbLbCookieStickinessPolicyTypeDef(TypedDict, total=False):
    CookieExpirationPeriod: int
    PolicyName: str


class AwsElbLoadBalancerAccessLogTypeDef(TypedDict, total=False):
    EmitInterval: int
    Enabled: bool
    S3BucketName: str
    S3BucketPrefix: str


class AwsElbLoadBalancerAttributesTypeDef(TypedDict, total=False):
    AccessLog: "AwsElbLoadBalancerAccessLogTypeDef"
    ConnectionDraining: "AwsElbLoadBalancerConnectionDrainingTypeDef"
    ConnectionSettings: "AwsElbLoadBalancerConnectionSettingsTypeDef"
    CrossZoneLoadBalancing: "AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef"


class AwsElbLoadBalancerBackendServerDescriptionTypeDef(TypedDict, total=False):
    InstancePort: int
    PolicyNames: List[str]


class AwsElbLoadBalancerConnectionDrainingTypeDef(TypedDict, total=False):
    Enabled: bool
    Timeout: int


class AwsElbLoadBalancerConnectionSettingsTypeDef(TypedDict, total=False):
    IdleTimeout: int


class AwsElbLoadBalancerCrossZoneLoadBalancingTypeDef(TypedDict, total=False):
    Enabled: bool


class AwsElbLoadBalancerDetailsTypeDef(TypedDict, total=False):
    AvailabilityZones: List[str]
    BackendServerDescriptions: List["AwsElbLoadBalancerBackendServerDescriptionTypeDef"]
    CanonicalHostedZoneName: str
    CanonicalHostedZoneNameID: str
    CreatedTime: str
    DnsName: str
    HealthCheck: "AwsElbLoadBalancerHealthCheckTypeDef"
    Instances: List["AwsElbLoadBalancerInstanceTypeDef"]
    ListenerDescriptions: List["AwsElbLoadBalancerListenerDescriptionTypeDef"]
    LoadBalancerAttributes: "AwsElbLoadBalancerAttributesTypeDef"
    LoadBalancerName: str
    Policies: "AwsElbLoadBalancerPoliciesTypeDef"
    Scheme: str
    SecurityGroups: List[str]
    SourceSecurityGroup: "AwsElbLoadBalancerSourceSecurityGroupTypeDef"
    Subnets: List[str]
    VpcId: str


class AwsElbLoadBalancerHealthCheckTypeDef(TypedDict, total=False):
    HealthyThreshold: int
    Interval: int
    Target: str
    Timeout: int
    UnhealthyThreshold: int


class AwsElbLoadBalancerInstanceTypeDef(TypedDict, total=False):
    InstanceId: str


class AwsElbLoadBalancerListenerDescriptionTypeDef(TypedDict, total=False):
    Listener: "AwsElbLoadBalancerListenerTypeDef"
    PolicyNames: List[str]


AwsElbLoadBalancerListenerTypeDef = TypedDict(
    "AwsElbLoadBalancerListenerTypeDef",
    {
        "InstancePort": int,
        "InstanceProtocol": str,
        "LoadBalancerPort": int,
        "Protocol": str,
        "SslCertificateId": str,
    },
    total=False,
)


class AwsElbLoadBalancerPoliciesTypeDef(TypedDict, total=False):
    AppCookieStickinessPolicies: List["AwsElbAppCookieStickinessPolicyTypeDef"]
    LbCookieStickinessPolicies: List["AwsElbLbCookieStickinessPolicyTypeDef"]
    OtherPolicies: List[str]


class AwsElbLoadBalancerSourceSecurityGroupTypeDef(TypedDict, total=False):
    GroupName: str
    OwnerAlias: str


AwsElbv2LoadBalancerDetailsTypeDef = TypedDict(
    "AwsElbv2LoadBalancerDetailsTypeDef",
    {
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "CanonicalHostedZoneId": str,
        "CreatedTime": str,
        "DNSName": str,
        "IpAddressType": str,
        "Scheme": str,
        "SecurityGroups": List[str],
        "State": "LoadBalancerStateTypeDef",
        "Type": str,
        "VpcId": str,
    },
    total=False,
)


class AwsIamAccessKeyDetailsTypeDef(TypedDict, total=False):
    UserName: str
    Status: AwsIamAccessKeyStatus
    CreatedAt: str
    PrincipalId: str
    PrincipalType: str
    PrincipalName: str
    AccountId: str
    AccessKeyId: str
    SessionContext: "AwsIamAccessKeySessionContextTypeDef"


class AwsIamAccessKeySessionContextAttributesTypeDef(TypedDict, total=False):
    MfaAuthenticated: bool
    CreationDate: str


AwsIamAccessKeySessionContextSessionIssuerTypeDef = TypedDict(
    "AwsIamAccessKeySessionContextSessionIssuerTypeDef",
    {"Type": str, "PrincipalId": str, "Arn": str, "AccountId": str, "UserName": str},
    total=False,
)


class AwsIamAccessKeySessionContextTypeDef(TypedDict, total=False):
    Attributes: "AwsIamAccessKeySessionContextAttributesTypeDef"
    SessionIssuer: "AwsIamAccessKeySessionContextSessionIssuerTypeDef"


class AwsIamAttachedManagedPolicyTypeDef(TypedDict, total=False):
    PolicyName: str
    PolicyArn: str


class AwsIamGroupDetailsTypeDef(TypedDict, total=False):
    AttachedManagedPolicies: List["AwsIamAttachedManagedPolicyTypeDef"]
    CreateDate: str
    GroupId: str
    GroupName: str
    GroupPolicyList: List["AwsIamGroupPolicyTypeDef"]
    Path: str


class AwsIamGroupPolicyTypeDef(TypedDict, total=False):
    PolicyName: str


class AwsIamInstanceProfileRoleTypeDef(TypedDict, total=False):
    Arn: str
    AssumeRolePolicyDocument: str
    CreateDate: str
    Path: str
    RoleId: str
    RoleName: str


class AwsIamInstanceProfileTypeDef(TypedDict, total=False):
    Arn: str
    CreateDate: str
    InstanceProfileId: str
    InstanceProfileName: str
    Path: str
    Roles: List["AwsIamInstanceProfileRoleTypeDef"]


class AwsIamPermissionsBoundaryTypeDef(TypedDict, total=False):
    PermissionsBoundaryArn: str
    PermissionsBoundaryType: str


class AwsIamPolicyDetailsTypeDef(TypedDict, total=False):
    AttachmentCount: int
    CreateDate: str
    DefaultVersionId: str
    Description: str
    IsAttachable: bool
    Path: str
    PermissionsBoundaryUsageCount: int
    PolicyId: str
    PolicyName: str
    PolicyVersionList: List["AwsIamPolicyVersionTypeDef"]
    UpdateDate: str


class AwsIamPolicyVersionTypeDef(TypedDict, total=False):
    VersionId: str
    IsDefaultVersion: bool
    CreateDate: str


class AwsIamRoleDetailsTypeDef(TypedDict, total=False):
    AssumeRolePolicyDocument: str
    AttachedManagedPolicies: List["AwsIamAttachedManagedPolicyTypeDef"]
    CreateDate: str
    InstanceProfileList: List["AwsIamInstanceProfileTypeDef"]
    PermissionsBoundary: "AwsIamPermissionsBoundaryTypeDef"
    RoleId: str
    RoleName: str
    RolePolicyList: List["AwsIamRolePolicyTypeDef"]
    MaxSessionDuration: int
    Path: str


class AwsIamRolePolicyTypeDef(TypedDict, total=False):
    PolicyName: str


class AwsIamUserDetailsTypeDef(TypedDict, total=False):
    AttachedManagedPolicies: List["AwsIamAttachedManagedPolicyTypeDef"]
    CreateDate: str
    GroupList: List[str]
    Path: str
    PermissionsBoundary: "AwsIamPermissionsBoundaryTypeDef"
    UserId: str
    UserName: str
    UserPolicyList: List["AwsIamUserPolicyTypeDef"]


class AwsIamUserPolicyTypeDef(TypedDict, total=False):
    PolicyName: str


class AwsKmsKeyDetailsTypeDef(TypedDict, total=False):
    AWSAccountId: str
    CreationDate: float
    KeyId: str
    KeyManager: str
    KeyState: str
    Origin: str
    Description: str


class AwsLambdaFunctionCodeTypeDef(TypedDict, total=False):
    S3Bucket: str
    S3Key: str
    S3ObjectVersion: str
    ZipFile: str


class AwsLambdaFunctionDeadLetterConfigTypeDef(TypedDict, total=False):
    TargetArn: str


class AwsLambdaFunctionDetailsTypeDef(TypedDict, total=False):
    Code: "AwsLambdaFunctionCodeTypeDef"
    CodeSha256: str
    DeadLetterConfig: "AwsLambdaFunctionDeadLetterConfigTypeDef"
    Environment: "AwsLambdaFunctionEnvironmentTypeDef"
    FunctionName: str
    Handler: str
    KmsKeyArn: str
    LastModified: str
    Layers: List["AwsLambdaFunctionLayerTypeDef"]
    MasterArn: str
    MemorySize: int
    RevisionId: str
    Role: str
    Runtime: str
    Timeout: int
    TracingConfig: "AwsLambdaFunctionTracingConfigTypeDef"
    VpcConfig: "AwsLambdaFunctionVpcConfigTypeDef"
    Version: str


class AwsLambdaFunctionEnvironmentErrorTypeDef(TypedDict, total=False):
    ErrorCode: str
    Message: str


class AwsLambdaFunctionEnvironmentTypeDef(TypedDict, total=False):
    Variables: Dict[str, str]
    Error: "AwsLambdaFunctionEnvironmentErrorTypeDef"


class AwsLambdaFunctionLayerTypeDef(TypedDict, total=False):
    Arn: str
    CodeSize: int


class AwsLambdaFunctionTracingConfigTypeDef(TypedDict, total=False):
    Mode: str


class AwsLambdaFunctionVpcConfigTypeDef(TypedDict, total=False):
    SecurityGroupIds: List[str]
    SubnetIds: List[str]
    VpcId: str


class AwsLambdaLayerVersionDetailsTypeDef(TypedDict, total=False):
    Version: int
    CompatibleRuntimes: List[str]
    CreatedDate: str


class AwsRdsDbClusterAssociatedRoleTypeDef(TypedDict, total=False):
    RoleArn: str
    Status: str


class AwsRdsDbClusterDetailsTypeDef(TypedDict, total=False):
    AllocatedStorage: int
    AvailabilityZones: List[str]
    BackupRetentionPeriod: int
    DatabaseName: str
    Status: str
    Endpoint: str
    ReaderEndpoint: str
    CustomEndpoints: List[str]
    MultiAz: bool
    Engine: str
    EngineVersion: str
    Port: int
    MasterUsername: str
    PreferredBackupWindow: str
    PreferredMaintenanceWindow: str
    ReadReplicaIdentifiers: List[str]
    VpcSecurityGroups: List["AwsRdsDbInstanceVpcSecurityGroupTypeDef"]
    HostedZoneId: str
    StorageEncrypted: bool
    KmsKeyId: str
    DbClusterResourceId: str
    AssociatedRoles: List["AwsRdsDbClusterAssociatedRoleTypeDef"]
    ClusterCreateTime: str
    EnabledCloudWatchLogsExports: List[str]
    EngineMode: str
    DeletionProtection: bool
    HttpEndpointEnabled: bool
    ActivityStreamStatus: str
    CopyTagsToSnapshot: bool
    CrossAccountClone: bool
    DomainMemberships: List["AwsRdsDbDomainMembershipTypeDef"]
    DbClusterParameterGroup: str
    DbSubnetGroup: str
    DbClusterOptionGroupMemberships: List["AwsRdsDbClusterOptionGroupMembershipTypeDef"]
    DbClusterIdentifier: str
    DbClusterMembers: List["AwsRdsDbClusterMemberTypeDef"]
    IamDatabaseAuthenticationEnabled: bool


class AwsRdsDbClusterMemberTypeDef(TypedDict, total=False):
    IsClusterWriter: bool
    PromotionTier: int
    DbInstanceIdentifier: str
    DbClusterParameterGroupStatus: str


class AwsRdsDbClusterOptionGroupMembershipTypeDef(TypedDict, total=False):
    DbClusterOptionGroupName: str
    Status: str


class AwsRdsDbClusterSnapshotDetailsTypeDef(TypedDict, total=False):
    AvailabilityZones: List[str]
    SnapshotCreateTime: str
    Engine: str
    AllocatedStorage: int
    Status: str
    Port: int
    VpcId: str
    ClusterCreateTime: str
    MasterUsername: str
    EngineVersion: str
    LicenseModel: str
    SnapshotType: str
    PercentProgress: int
    StorageEncrypted: bool
    KmsKeyId: str
    DbClusterIdentifier: str
    DbClusterSnapshotIdentifier: str
    IamDatabaseAuthenticationEnabled: bool


class AwsRdsDbDomainMembershipTypeDef(TypedDict, total=False):
    Domain: str
    Status: str
    Fqdn: str
    IamRoleName: str


class AwsRdsDbInstanceAssociatedRoleTypeDef(TypedDict, total=False):
    RoleArn: str
    FeatureName: str
    Status: str


class AwsRdsDbInstanceDetailsTypeDef(TypedDict, total=False):
    AssociatedRoles: List["AwsRdsDbInstanceAssociatedRoleTypeDef"]
    CACertificateIdentifier: str
    DBClusterIdentifier: str
    DBInstanceIdentifier: str
    DBInstanceClass: str
    DbInstancePort: int
    DbiResourceId: str
    DBName: str
    DeletionProtection: bool
    Endpoint: "AwsRdsDbInstanceEndpointTypeDef"
    Engine: str
    EngineVersion: str
    IAMDatabaseAuthenticationEnabled: bool
    InstanceCreateTime: str
    KmsKeyId: str
    PubliclyAccessible: bool
    StorageEncrypted: bool
    TdeCredentialArn: str
    VpcSecurityGroups: List["AwsRdsDbInstanceVpcSecurityGroupTypeDef"]
    MultiAz: bool
    EnhancedMonitoringResourceArn: str
    DbInstanceStatus: str
    MasterUsername: str
    AllocatedStorage: int
    PreferredBackupWindow: str
    BackupRetentionPeriod: int
    DbSecurityGroups: List[str]
    DbParameterGroups: List["AwsRdsDbParameterGroupTypeDef"]
    AvailabilityZone: str
    DbSubnetGroup: "AwsRdsDbSubnetGroupTypeDef"
    PreferredMaintenanceWindow: str
    PendingModifiedValues: "AwsRdsDbPendingModifiedValuesTypeDef"
    LatestRestorableTime: str
    AutoMinorVersionUpgrade: bool
    ReadReplicaSourceDBInstanceIdentifier: str
    ReadReplicaDBInstanceIdentifiers: List[str]
    ReadReplicaDBClusterIdentifiers: List[str]
    LicenseModel: str
    Iops: int
    OptionGroupMemberships: List["AwsRdsDbOptionGroupMembershipTypeDef"]
    CharacterSetName: str
    SecondaryAvailabilityZone: str
    StatusInfos: List["AwsRdsDbStatusInfoTypeDef"]
    StorageType: str
    DomainMemberships: List["AwsRdsDbDomainMembershipTypeDef"]
    CopyTagsToSnapshot: bool
    MonitoringInterval: int
    MonitoringRoleArn: str
    PromotionTier: int
    Timezone: str
    PerformanceInsightsEnabled: bool
    PerformanceInsightsKmsKeyId: str
    PerformanceInsightsRetentionPeriod: int
    EnabledCloudWatchLogsExports: List[str]
    ProcessorFeatures: List["AwsRdsDbProcessorFeatureTypeDef"]
    ListenerEndpoint: "AwsRdsDbInstanceEndpointTypeDef"
    MaxAllocatedStorage: int


class AwsRdsDbInstanceEndpointTypeDef(TypedDict, total=False):
    Address: str
    Port: int
    HostedZoneId: str


class AwsRdsDbInstanceVpcSecurityGroupTypeDef(TypedDict, total=False):
    VpcSecurityGroupId: str
    Status: str


class AwsRdsDbOptionGroupMembershipTypeDef(TypedDict, total=False):
    OptionGroupName: str
    Status: str


class AwsRdsDbParameterGroupTypeDef(TypedDict, total=False):
    DbParameterGroupName: str
    ParameterApplyStatus: str


class AwsRdsDbPendingModifiedValuesTypeDef(TypedDict, total=False):
    DbInstanceClass: str
    AllocatedStorage: int
    MasterUserPassword: str
    Port: int
    BackupRetentionPeriod: int
    MultiAZ: bool
    EngineVersion: str
    LicenseModel: str
    Iops: int
    DbInstanceIdentifier: str
    StorageType: str
    CaCertificateIdentifier: str
    DbSubnetGroupName: str
    PendingCloudWatchLogsExports: "AwsRdsPendingCloudWatchLogsExportsTypeDef"
    ProcessorFeatures: List["AwsRdsDbProcessorFeatureTypeDef"]


class AwsRdsDbProcessorFeatureTypeDef(TypedDict, total=False):
    Name: str
    Value: str


class AwsRdsDbSnapshotDetailsTypeDef(TypedDict, total=False):
    DbSnapshotIdentifier: str
    DbInstanceIdentifier: str
    SnapshotCreateTime: str
    Engine: str
    AllocatedStorage: int
    Status: str
    Port: int
    AvailabilityZone: str
    VpcId: str
    InstanceCreateTime: str
    MasterUsername: str
    EngineVersion: str
    LicenseModel: str
    SnapshotType: str
    Iops: int
    OptionGroupName: str
    PercentProgress: int
    SourceRegion: str
    SourceDbSnapshotIdentifier: str
    StorageType: str
    TdeCredentialArn: str
    Encrypted: bool
    KmsKeyId: str
    Timezone: str
    IamDatabaseAuthenticationEnabled: bool
    ProcessorFeatures: List["AwsRdsDbProcessorFeatureTypeDef"]
    DbiResourceId: str


class AwsRdsDbStatusInfoTypeDef(TypedDict, total=False):
    StatusType: str
    Normal: bool
    Status: str
    Message: str


class AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef(TypedDict, total=False):
    Name: str


class AwsRdsDbSubnetGroupSubnetTypeDef(TypedDict, total=False):
    SubnetIdentifier: str
    SubnetAvailabilityZone: "AwsRdsDbSubnetGroupSubnetAvailabilityZoneTypeDef"
    SubnetStatus: str


class AwsRdsDbSubnetGroupTypeDef(TypedDict, total=False):
    DbSubnetGroupName: str
    DbSubnetGroupDescription: str
    VpcId: str
    SubnetGroupStatus: str
    Subnets: List["AwsRdsDbSubnetGroupSubnetTypeDef"]
    DbSubnetGroupArn: str


class AwsRdsPendingCloudWatchLogsExportsTypeDef(TypedDict, total=False):
    LogTypesToEnable: List[str]
    LogTypesToDisable: List[str]


class AwsRedshiftClusterClusterNodeTypeDef(TypedDict, total=False):
    NodeRole: str
    PrivateIpAddress: str
    PublicIpAddress: str


class AwsRedshiftClusterClusterParameterGroupTypeDef(TypedDict, total=False):
    ClusterParameterStatusList: List["AwsRedshiftClusterClusterParameterStatusTypeDef"]
    ParameterApplyStatus: str
    ParameterGroupName: str


class AwsRedshiftClusterClusterParameterStatusTypeDef(TypedDict, total=False):
    ParameterName: str
    ParameterApplyStatus: str
    ParameterApplyErrorDescription: str


class AwsRedshiftClusterClusterSecurityGroupTypeDef(TypedDict, total=False):
    ClusterSecurityGroupName: str
    Status: str


class AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef(TypedDict, total=False):
    DestinationRegion: str
    ManualSnapshotRetentionPeriod: int
    RetentionPeriod: int
    SnapshotCopyGrantName: str


class AwsRedshiftClusterDeferredMaintenanceWindowTypeDef(TypedDict, total=False):
    DeferMaintenanceEndTime: str
    DeferMaintenanceIdentifier: str
    DeferMaintenanceStartTime: str


class AwsRedshiftClusterDetailsTypeDef(TypedDict, total=False):
    AllowVersionUpgrade: bool
    AutomatedSnapshotRetentionPeriod: int
    AvailabilityZone: str
    ClusterAvailabilityStatus: str
    ClusterCreateTime: str
    ClusterIdentifier: str
    ClusterNodes: List["AwsRedshiftClusterClusterNodeTypeDef"]
    ClusterParameterGroups: List["AwsRedshiftClusterClusterParameterGroupTypeDef"]
    ClusterPublicKey: str
    ClusterRevisionNumber: str
    ClusterSecurityGroups: List["AwsRedshiftClusterClusterSecurityGroupTypeDef"]
    ClusterSnapshotCopyStatus: "AwsRedshiftClusterClusterSnapshotCopyStatusTypeDef"
    ClusterStatus: str
    ClusterSubnetGroupName: str
    ClusterVersion: str
    DBName: str
    DeferredMaintenanceWindows: List["AwsRedshiftClusterDeferredMaintenanceWindowTypeDef"]
    ElasticIpStatus: "AwsRedshiftClusterElasticIpStatusTypeDef"
    ElasticResizeNumberOfNodeOptions: str
    Encrypted: bool
    Endpoint: "AwsRedshiftClusterEndpointTypeDef"
    EnhancedVpcRouting: bool
    ExpectedNextSnapshotScheduleTime: str
    ExpectedNextSnapshotScheduleTimeStatus: str
    HsmStatus: "AwsRedshiftClusterHsmStatusTypeDef"
    IamRoles: List["AwsRedshiftClusterIamRoleTypeDef"]
    KmsKeyId: str
    MaintenanceTrackName: str
    ManualSnapshotRetentionPeriod: int
    MasterUsername: str
    NextMaintenanceWindowStartTime: str
    NodeType: str
    NumberOfNodes: int
    PendingActions: List[str]
    PendingModifiedValues: "AwsRedshiftClusterPendingModifiedValuesTypeDef"
    PreferredMaintenanceWindow: str
    PubliclyAccessible: bool
    ResizeInfo: "AwsRedshiftClusterResizeInfoTypeDef"
    RestoreStatus: "AwsRedshiftClusterRestoreStatusTypeDef"
    SnapshotScheduleIdentifier: str
    SnapshotScheduleState: str
    VpcId: str
    VpcSecurityGroups: List["AwsRedshiftClusterVpcSecurityGroupTypeDef"]


class AwsRedshiftClusterElasticIpStatusTypeDef(TypedDict, total=False):
    ElasticIp: str
    Status: str


class AwsRedshiftClusterEndpointTypeDef(TypedDict, total=False):
    Address: str
    Port: int


class AwsRedshiftClusterHsmStatusTypeDef(TypedDict, total=False):
    HsmClientCertificateIdentifier: str
    HsmConfigurationIdentifier: str
    Status: str


class AwsRedshiftClusterIamRoleTypeDef(TypedDict, total=False):
    ApplyStatus: str
    IamRoleArn: str


class AwsRedshiftClusterPendingModifiedValuesTypeDef(TypedDict, total=False):
    AutomatedSnapshotRetentionPeriod: int
    ClusterIdentifier: str
    ClusterType: str
    ClusterVersion: str
    EncryptionType: str
    EnhancedVpcRouting: bool
    MaintenanceTrackName: str
    MasterUserPassword: str
    NodeType: str
    NumberOfNodes: int
    PubliclyAccessible: bool


class AwsRedshiftClusterResizeInfoTypeDef(TypedDict, total=False):
    AllowCancelResize: bool
    ResizeType: str


class AwsRedshiftClusterRestoreStatusTypeDef(TypedDict, total=False):
    CurrentRestoreRateInMegaBytesPerSecond: float
    ElapsedTimeInSeconds: int
    EstimatedTimeToCompletionInSeconds: int
    ProgressInMegaBytes: int
    SnapshotSizeInMegaBytes: int
    Status: str


class AwsRedshiftClusterVpcSecurityGroupTypeDef(TypedDict, total=False):
    Status: str
    VpcSecurityGroupId: str


class AwsS3AccountPublicAccessBlockDetailsTypeDef(TypedDict, total=False):
    BlockPublicAcls: bool
    BlockPublicPolicy: bool
    IgnorePublicAcls: bool
    RestrictPublicBuckets: bool


class AwsS3BucketDetailsTypeDef(TypedDict, total=False):
    OwnerId: str
    OwnerName: str
    CreatedAt: str
    ServerSideEncryptionConfiguration: "AwsS3BucketServerSideEncryptionConfigurationTypeDef"
    PublicAccessBlockConfiguration: "AwsS3AccountPublicAccessBlockDetailsTypeDef"


class AwsS3BucketServerSideEncryptionByDefaultTypeDef(TypedDict, total=False):
    SSEAlgorithm: str
    KMSMasterKeyID: str


class AwsS3BucketServerSideEncryptionConfigurationTypeDef(TypedDict, total=False):
    Rules: List["AwsS3BucketServerSideEncryptionRuleTypeDef"]


class AwsS3BucketServerSideEncryptionRuleTypeDef(TypedDict, total=False):
    ApplyServerSideEncryptionByDefault: "AwsS3BucketServerSideEncryptionByDefaultTypeDef"


class AwsS3ObjectDetailsTypeDef(TypedDict, total=False):
    LastModified: str
    ETag: str
    VersionId: str
    ContentType: str
    ServerSideEncryption: str
    SSEKMSKeyId: str


class AwsSecretsManagerSecretDetailsTypeDef(TypedDict, total=False):
    RotationRules: "AwsSecretsManagerSecretRotationRulesTypeDef"
    RotationOccurredWithinFrequency: bool
    KmsKeyId: str
    RotationEnabled: bool
    RotationLambdaArn: str
    Deleted: bool
    Name: str
    Description: str


class AwsSecretsManagerSecretRotationRulesTypeDef(TypedDict, total=False):
    AutomaticallyAfterDays: int


AwsSecurityFindingFiltersTypeDef = TypedDict(
    "AwsSecurityFindingFiltersTypeDef",
    {
        "ProductArn": List["StringFilterTypeDef"],
        "AwsAccountId": List["StringFilterTypeDef"],
        "Id": List["StringFilterTypeDef"],
        "GeneratorId": List["StringFilterTypeDef"],
        "Type": List["StringFilterTypeDef"],
        "FirstObservedAt": List["DateFilterTypeDef"],
        "LastObservedAt": List["DateFilterTypeDef"],
        "CreatedAt": List["DateFilterTypeDef"],
        "UpdatedAt": List["DateFilterTypeDef"],
        "SeverityProduct": List["NumberFilterTypeDef"],
        "SeverityNormalized": List["NumberFilterTypeDef"],
        "SeverityLabel": List["StringFilterTypeDef"],
        "Confidence": List["NumberFilterTypeDef"],
        "Criticality": List["NumberFilterTypeDef"],
        "Title": List["StringFilterTypeDef"],
        "Description": List["StringFilterTypeDef"],
        "RecommendationText": List["StringFilterTypeDef"],
        "SourceUrl": List["StringFilterTypeDef"],
        "ProductFields": List["MapFilterTypeDef"],
        "ProductName": List["StringFilterTypeDef"],
        "CompanyName": List["StringFilterTypeDef"],
        "UserDefinedFields": List["MapFilterTypeDef"],
        "MalwareName": List["StringFilterTypeDef"],
        "MalwareType": List["StringFilterTypeDef"],
        "MalwarePath": List["StringFilterTypeDef"],
        "MalwareState": List["StringFilterTypeDef"],
        "NetworkDirection": List["StringFilterTypeDef"],
        "NetworkProtocol": List["StringFilterTypeDef"],
        "NetworkSourceIpV4": List["IpFilterTypeDef"],
        "NetworkSourceIpV6": List["IpFilterTypeDef"],
        "NetworkSourcePort": List["NumberFilterTypeDef"],
        "NetworkSourceDomain": List["StringFilterTypeDef"],
        "NetworkSourceMac": List["StringFilterTypeDef"],
        "NetworkDestinationIpV4": List["IpFilterTypeDef"],
        "NetworkDestinationIpV6": List["IpFilterTypeDef"],
        "NetworkDestinationPort": List["NumberFilterTypeDef"],
        "NetworkDestinationDomain": List["StringFilterTypeDef"],
        "ProcessName": List["StringFilterTypeDef"],
        "ProcessPath": List["StringFilterTypeDef"],
        "ProcessPid": List["NumberFilterTypeDef"],
        "ProcessParentPid": List["NumberFilterTypeDef"],
        "ProcessLaunchedAt": List["DateFilterTypeDef"],
        "ProcessTerminatedAt": List["DateFilterTypeDef"],
        "ThreatIntelIndicatorType": List["StringFilterTypeDef"],
        "ThreatIntelIndicatorValue": List["StringFilterTypeDef"],
        "ThreatIntelIndicatorCategory": List["StringFilterTypeDef"],
        "ThreatIntelIndicatorLastObservedAt": List["DateFilterTypeDef"],
        "ThreatIntelIndicatorSource": List["StringFilterTypeDef"],
        "ThreatIntelIndicatorSourceUrl": List["StringFilterTypeDef"],
        "ResourceType": List["StringFilterTypeDef"],
        "ResourceId": List["StringFilterTypeDef"],
        "ResourcePartition": List["StringFilterTypeDef"],
        "ResourceRegion": List["StringFilterTypeDef"],
        "ResourceTags": List["MapFilterTypeDef"],
        "ResourceAwsEc2InstanceType": List["StringFilterTypeDef"],
        "ResourceAwsEc2InstanceImageId": List["StringFilterTypeDef"],
        "ResourceAwsEc2InstanceIpV4Addresses": List["IpFilterTypeDef"],
        "ResourceAwsEc2InstanceIpV6Addresses": List["IpFilterTypeDef"],
        "ResourceAwsEc2InstanceKeyName": List["StringFilterTypeDef"],
        "ResourceAwsEc2InstanceIamInstanceProfileArn": List["StringFilterTypeDef"],
        "ResourceAwsEc2InstanceVpcId": List["StringFilterTypeDef"],
        "ResourceAwsEc2InstanceSubnetId": List["StringFilterTypeDef"],
        "ResourceAwsEc2InstanceLaunchedAt": List["DateFilterTypeDef"],
        "ResourceAwsS3BucketOwnerId": List["StringFilterTypeDef"],
        "ResourceAwsS3BucketOwnerName": List["StringFilterTypeDef"],
        "ResourceAwsIamAccessKeyUserName": List["StringFilterTypeDef"],
        "ResourceAwsIamAccessKeyStatus": List["StringFilterTypeDef"],
        "ResourceAwsIamAccessKeyCreatedAt": List["DateFilterTypeDef"],
        "ResourceContainerName": List["StringFilterTypeDef"],
        "ResourceContainerImageId": List["StringFilterTypeDef"],
        "ResourceContainerImageName": List["StringFilterTypeDef"],
        "ResourceContainerLaunchedAt": List["DateFilterTypeDef"],
        "ResourceDetailsOther": List["MapFilterTypeDef"],
        "ComplianceStatus": List["StringFilterTypeDef"],
        "VerificationState": List["StringFilterTypeDef"],
        "WorkflowState": List["StringFilterTypeDef"],
        "WorkflowStatus": List["StringFilterTypeDef"],
        "RecordState": List["StringFilterTypeDef"],
        "RelatedFindingsProductArn": List["StringFilterTypeDef"],
        "RelatedFindingsId": List["StringFilterTypeDef"],
        "NoteText": List["StringFilterTypeDef"],
        "NoteUpdatedAt": List["DateFilterTypeDef"],
        "NoteUpdatedBy": List["StringFilterTypeDef"],
        "Keyword": List["KeywordFilterTypeDef"],
        "FindingProviderFieldsConfidence": List["NumberFilterTypeDef"],
        "FindingProviderFieldsCriticality": List["NumberFilterTypeDef"],
        "FindingProviderFieldsRelatedFindingsId": List["StringFilterTypeDef"],
        "FindingProviderFieldsRelatedFindingsProductArn": List["StringFilterTypeDef"],
        "FindingProviderFieldsSeverityLabel": List["StringFilterTypeDef"],
        "FindingProviderFieldsSeverityOriginal": List["StringFilterTypeDef"],
        "FindingProviderFieldsTypes": List["StringFilterTypeDef"],
    },
    total=False,
)


class AwsSecurityFindingIdentifierTypeDef(TypedDict):
    Id: str
    ProductArn: str


class _RequiredAwsSecurityFindingTypeDef(TypedDict):
    SchemaVersion: str
    Id: str
    ProductArn: str
    GeneratorId: str
    AwsAccountId: str
    CreatedAt: str
    UpdatedAt: str
    Title: str
    Description: str
    Resources: List["ResourceTypeDef"]


class AwsSecurityFindingTypeDef(_RequiredAwsSecurityFindingTypeDef, total=False):
    Types: List[str]
    FirstObservedAt: str
    LastObservedAt: str
    Severity: "SeverityTypeDef"
    Confidence: int
    Criticality: int
    Remediation: "RemediationTypeDef"
    SourceUrl: str
    ProductFields: Dict[str, str]
    UserDefinedFields: Dict[str, str]
    Malware: List["MalwareTypeDef"]
    Network: "NetworkTypeDef"
    NetworkPath: List["NetworkPathComponentTypeDef"]
    Process: "ProcessDetailsTypeDef"
    ThreatIntelIndicators: List["ThreatIntelIndicatorTypeDef"]
    Compliance: "ComplianceTypeDef"
    VerificationState: VerificationState
    WorkflowState: WorkflowState
    Workflow: "WorkflowTypeDef"
    RecordState: RecordState
    RelatedFindings: List["RelatedFindingTypeDef"]
    Note: "NoteTypeDef"
    Vulnerabilities: List["VulnerabilityTypeDef"]
    PatchSummary: "PatchSummaryTypeDef"
    Action: "ActionTypeDef"
    FindingProviderFields: "FindingProviderFieldsTypeDef"


class AwsSnsTopicDetailsTypeDef(TypedDict, total=False):
    KmsMasterKeyId: str
    Subscription: List["AwsSnsTopicSubscriptionTypeDef"]
    TopicName: str
    Owner: str


AwsSnsTopicSubscriptionTypeDef = TypedDict(
    "AwsSnsTopicSubscriptionTypeDef", {"Endpoint": str, "Protocol": str}, total=False
)


class AwsSqsQueueDetailsTypeDef(TypedDict, total=False):
    KmsDataKeyReusePeriodSeconds: int
    KmsMasterKeyId: str
    QueueName: str
    DeadLetterTargetArn: str


class AwsSsmComplianceSummaryTypeDef(TypedDict, total=False):
    Status: str
    CompliantCriticalCount: int
    CompliantHighCount: int
    CompliantMediumCount: int
    ExecutionType: str
    NonCompliantCriticalCount: int
    CompliantInformationalCount: int
    NonCompliantInformationalCount: int
    CompliantUnspecifiedCount: int
    NonCompliantLowCount: int
    NonCompliantHighCount: int
    CompliantLowCount: int
    ComplianceType: str
    PatchBaselineId: str
    OverallSeverity: str
    NonCompliantMediumCount: int
    NonCompliantUnspecifiedCount: int
    PatchGroup: str


class AwsSsmPatchComplianceDetailsTypeDef(TypedDict, total=False):
    Patch: "AwsSsmPatchTypeDef"


class AwsSsmPatchTypeDef(TypedDict, total=False):
    ComplianceSummary: "AwsSsmComplianceSummaryTypeDef"


class AwsWafWebAclDetailsTypeDef(TypedDict, total=False):
    Name: str
    DefaultAction: str
    Rules: List["AwsWafWebAclRuleTypeDef"]
    WebAclId: str


AwsWafWebAclRuleTypeDef = TypedDict(
    "AwsWafWebAclRuleTypeDef",
    {
        "Action": "WafActionTypeDef",
        "ExcludedRules": List["WafExcludedRuleTypeDef"],
        "OverrideAction": "WafOverrideActionTypeDef",
        "Priority": int,
        "RuleId": str,
        "Type": str,
    },
    total=False,
)


class BatchDisableStandardsResponseTypeDef(TypedDict, total=False):
    StandardsSubscriptions: List["StandardsSubscriptionTypeDef"]


class BatchEnableStandardsResponseTypeDef(TypedDict, total=False):
    StandardsSubscriptions: List["StandardsSubscriptionTypeDef"]


class _RequiredBatchImportFindingsResponseTypeDef(TypedDict):
    FailedCount: int
    SuccessCount: int


class BatchImportFindingsResponseTypeDef(_RequiredBatchImportFindingsResponseTypeDef, total=False):
    FailedFindings: List["ImportFindingsErrorTypeDef"]


class BatchUpdateFindingsResponseTypeDef(TypedDict):
    ProcessedFindings: List["AwsSecurityFindingIdentifierTypeDef"]
    UnprocessedFindings: List["BatchUpdateFindingsUnprocessedFindingTypeDef"]


class BatchUpdateFindingsUnprocessedFindingTypeDef(TypedDict):
    FindingIdentifier: "AwsSecurityFindingIdentifierTypeDef"
    ErrorCode: str
    ErrorMessage: str


class CellTypeDef(TypedDict, total=False):
    Column: int
    Row: int
    ColumnName: str
    CellReference: str


class CidrBlockAssociationTypeDef(TypedDict, total=False):
    AssociationId: str
    CidrBlock: str
    CidrBlockState: str


class CityTypeDef(TypedDict, total=False):
    CityName: str


class ClassificationResultTypeDef(TypedDict, total=False):
    MimeType: str
    SizeClassified: int
    AdditionalOccurrences: bool
    Status: "ClassificationStatusTypeDef"
    SensitiveData: List["SensitiveDataResultTypeDef"]
    CustomDataIdentifiers: "CustomDataIdentifiersResultTypeDef"


class ClassificationStatusTypeDef(TypedDict, total=False):
    Code: str
    Reason: str


class ComplianceTypeDef(TypedDict, total=False):
    Status: ComplianceStatus
    RelatedRequirements: List[str]
    StatusReasons: List["StatusReasonTypeDef"]


class ContainerDetailsTypeDef(TypedDict, total=False):
    Name: str
    ImageId: str
    ImageName: str
    LaunchedAt: str


class CountryTypeDef(TypedDict, total=False):
    CountryCode: str
    CountryName: str


class CreateActionTargetResponseTypeDef(TypedDict):
    ActionTargetArn: str


class CreateInsightResponseTypeDef(TypedDict):
    InsightArn: str


class CreateMembersResponseTypeDef(TypedDict, total=False):
    UnprocessedAccounts: List["ResultTypeDef"]


class CustomDataIdentifiersDetectionsTypeDef(TypedDict, total=False):
    Count: int
    Arn: str
    Name: str
    Occurrences: "OccurrencesTypeDef"


class CustomDataIdentifiersResultTypeDef(TypedDict, total=False):
    Detections: List["CustomDataIdentifiersDetectionsTypeDef"]
    TotalCount: int


class CvssTypeDef(TypedDict, total=False):
    Version: str
    BaseScore: float
    BaseVector: str


class DataClassificationDetailsTypeDef(TypedDict, total=False):
    DetailedResultsLocation: str
    Result: "ClassificationResultTypeDef"


class DateFilterTypeDef(TypedDict, total=False):
    Start: str
    End: str
    DateRange: "DateRangeTypeDef"


class DateRangeTypeDef(TypedDict, total=False):
    Value: int
    Unit: Literal["DAYS"]


class DeclineInvitationsResponseTypeDef(TypedDict, total=False):
    UnprocessedAccounts: List["ResultTypeDef"]


class DeleteActionTargetResponseTypeDef(TypedDict):
    ActionTargetArn: str


class DeleteInsightResponseTypeDef(TypedDict):
    InsightArn: str


class DeleteInvitationsResponseTypeDef(TypedDict, total=False):
    UnprocessedAccounts: List["ResultTypeDef"]


class DeleteMembersResponseTypeDef(TypedDict, total=False):
    UnprocessedAccounts: List["ResultTypeDef"]


class _RequiredDescribeActionTargetsResponseTypeDef(TypedDict):
    ActionTargets: List["ActionTargetTypeDef"]


class DescribeActionTargetsResponseTypeDef(
    _RequiredDescribeActionTargetsResponseTypeDef, total=False
):
    NextToken: str


class DescribeHubResponseTypeDef(TypedDict, total=False):
    HubArn: str
    SubscribedAt: str
    AutoEnableControls: bool


class DescribeOrganizationConfigurationResponseTypeDef(TypedDict, total=False):
    AutoEnable: bool
    MemberAccountLimitReached: bool


class _RequiredDescribeProductsResponseTypeDef(TypedDict):
    Products: List["ProductTypeDef"]


class DescribeProductsResponseTypeDef(_RequiredDescribeProductsResponseTypeDef, total=False):
    NextToken: str


class DescribeStandardsControlsResponseTypeDef(TypedDict, total=False):
    Controls: List["StandardsControlTypeDef"]
    NextToken: str


class DescribeStandardsResponseTypeDef(TypedDict, total=False):
    Standards: List["StandardTypeDef"]
    NextToken: str


DnsRequestActionTypeDef = TypedDict(
    "DnsRequestActionTypeDef", {"Domain": str, "Protocol": str, "Blocked": bool}, total=False
)


class EnableImportFindingsForProductResponseTypeDef(TypedDict, total=False):
    ProductSubscriptionArn: str


class FindingProviderFieldsTypeDef(TypedDict, total=False):
    Confidence: int
    Criticality: int
    RelatedFindings: List["RelatedFindingTypeDef"]
    Severity: "FindingProviderSeverityTypeDef"
    Types: List[str]


class FindingProviderSeverityTypeDef(TypedDict, total=False):
    Label: SeverityLabel
    Original: str


class GeoLocationTypeDef(TypedDict, total=False):
    Lon: float
    Lat: float


class GetAdministratorAccountResponseTypeDef(TypedDict, total=False):
    Administrator: "InvitationTypeDef"


class GetEnabledStandardsResponseTypeDef(TypedDict, total=False):
    StandardsSubscriptions: List["StandardsSubscriptionTypeDef"]
    NextToken: str


class _RequiredGetFindingsResponseTypeDef(TypedDict):
    Findings: List["AwsSecurityFindingTypeDef"]


class GetFindingsResponseTypeDef(_RequiredGetFindingsResponseTypeDef, total=False):
    NextToken: str


class GetInsightResultsResponseTypeDef(TypedDict):
    InsightResults: "InsightResultsTypeDef"


class _RequiredGetInsightsResponseTypeDef(TypedDict):
    Insights: List["InsightTypeDef"]


class GetInsightsResponseTypeDef(_RequiredGetInsightsResponseTypeDef, total=False):
    NextToken: str


class GetInvitationsCountResponseTypeDef(TypedDict, total=False):
    InvitationsCount: int


class GetMasterAccountResponseTypeDef(TypedDict, total=False):
    Master: "InvitationTypeDef"


class GetMembersResponseTypeDef(TypedDict, total=False):
    Members: List["MemberTypeDef"]
    UnprocessedAccounts: List["ResultTypeDef"]


IcmpTypeCodeTypeDef = TypedDict("IcmpTypeCodeTypeDef", {"Code": int, "Type": int}, total=False)


class ImportFindingsErrorTypeDef(TypedDict):
    Id: str
    ErrorCode: str
    ErrorMessage: str


class InsightResultValueTypeDef(TypedDict):
    GroupByAttributeValue: str
    Count: int


class InsightResultsTypeDef(TypedDict):
    InsightArn: str
    GroupByAttribute: str
    ResultValues: List["InsightResultValueTypeDef"]


class InsightTypeDef(TypedDict):
    InsightArn: str
    Name: str
    Filters: "AwsSecurityFindingFiltersTypeDef"
    GroupByAttribute: str


class InvitationTypeDef(TypedDict, total=False):
    AccountId: str
    InvitationId: str
    InvitedAt: datetime
    MemberStatus: str


class InviteMembersResponseTypeDef(TypedDict, total=False):
    UnprocessedAccounts: List["ResultTypeDef"]


class IpFilterTypeDef(TypedDict, total=False):
    Cidr: str


class IpOrganizationDetailsTypeDef(TypedDict, total=False):
    Asn: int
    AsnOrg: str
    Isp: str
    Org: str


class Ipv6CidrBlockAssociationTypeDef(TypedDict, total=False):
    AssociationId: str
    Ipv6CidrBlock: str
    CidrBlockState: str


class KeywordFilterTypeDef(TypedDict, total=False):
    Value: str


class ListEnabledProductsForImportResponseTypeDef(TypedDict, total=False):
    ProductSubscriptions: List[str]
    NextToken: str


class ListInvitationsResponseTypeDef(TypedDict, total=False):
    Invitations: List["InvitationTypeDef"]
    NextToken: str


class ListMembersResponseTypeDef(TypedDict, total=False):
    Members: List["MemberTypeDef"]
    NextToken: str


class ListOrganizationAdminAccountsResponseTypeDef(TypedDict, total=False):
    AdminAccounts: List["AdminAccountTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class LoadBalancerStateTypeDef(TypedDict, total=False):
    Code: str
    Reason: str


_RequiredMalwareTypeDef = TypedDict("_RequiredMalwareTypeDef", {"Name": str})
_OptionalMalwareTypeDef = TypedDict(
    "_OptionalMalwareTypeDef",
    {"Type": MalwareType, "Path": str, "State": MalwareState},
    total=False,
)


class MalwareTypeDef(_RequiredMalwareTypeDef, _OptionalMalwareTypeDef):
    pass


class MapFilterTypeDef(TypedDict, total=False):
    Key: str
    Value: str
    Comparison: MapFilterComparison


class MemberTypeDef(TypedDict, total=False):
    AccountId: str
    Email: str
    MasterId: str
    AdministratorId: str
    MemberStatus: str
    InvitedAt: datetime
    UpdatedAt: datetime


NetworkConnectionActionTypeDef = TypedDict(
    "NetworkConnectionActionTypeDef",
    {
        "ConnectionDirection": str,
        "RemoteIpDetails": "ActionRemoteIpDetailsTypeDef",
        "RemotePortDetails": "ActionRemotePortDetailsTypeDef",
        "LocalPortDetails": "ActionLocalPortDetailsTypeDef",
        "Protocol": str,
        "Blocked": bool,
    },
    total=False,
)

NetworkHeaderTypeDef = TypedDict(
    "NetworkHeaderTypeDef",
    {
        "Protocol": str,
        "Destination": "NetworkPathComponentDetailsTypeDef",
        "Source": "NetworkPathComponentDetailsTypeDef",
    },
    total=False,
)


class NetworkPathComponentDetailsTypeDef(TypedDict, total=False):
    Address: List[str]
    PortRanges: List["PortRangeTypeDef"]


class NetworkPathComponentTypeDef(TypedDict, total=False):
    ComponentId: str
    ComponentType: str
    Egress: "NetworkHeaderTypeDef"
    Ingress: "NetworkHeaderTypeDef"


NetworkTypeDef = TypedDict(
    "NetworkTypeDef",
    {
        "Direction": NetworkDirection,
        "Protocol": str,
        "OpenPortRange": "PortRangeTypeDef",
        "SourceIpV4": str,
        "SourceIpV6": str,
        "SourcePort": int,
        "SourceDomain": str,
        "SourceMac": str,
        "DestinationIpV4": str,
        "DestinationIpV6": str,
        "DestinationPort": int,
        "DestinationDomain": str,
    },
    total=False,
)

NoteTypeDef = TypedDict("NoteTypeDef", {"Text": str, "UpdatedBy": str, "UpdatedAt": str})

NoteUpdateTypeDef = TypedDict("NoteUpdateTypeDef", {"Text": str, "UpdatedBy": str})


class NumberFilterTypeDef(TypedDict, total=False):
    Gte: float
    Lte: float
    Eq: float


class OccurrencesTypeDef(TypedDict, total=False):
    LineRanges: List["RangeTypeDef"]
    OffsetRanges: List["RangeTypeDef"]
    Pages: List["PageTypeDef"]
    Records: List["RecordTypeDef"]
    Cells: List["CellTypeDef"]


class PageTypeDef(TypedDict, total=False):
    PageNumber: int
    LineRange: "RangeTypeDef"
    OffsetRange: "RangeTypeDef"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredPatchSummaryTypeDef(TypedDict):
    Id: str


class PatchSummaryTypeDef(_RequiredPatchSummaryTypeDef, total=False):
    InstalledCount: int
    MissingCount: int
    FailedCount: int
    InstalledOtherCount: int
    InstalledRejectedCount: int
    InstalledPendingReboot: int
    OperationStartTime: str
    OperationEndTime: str
    RebootOption: str
    Operation: str


class PortProbeActionTypeDef(TypedDict, total=False):
    PortProbeDetails: List["PortProbeDetailTypeDef"]
    Blocked: bool


class PortProbeDetailTypeDef(TypedDict, total=False):
    LocalPortDetails: "ActionLocalPortDetailsTypeDef"
    LocalIpDetails: "ActionLocalIpDetailsTypeDef"
    RemoteIpDetails: "ActionRemoteIpDetailsTypeDef"


class PortRangeFromToTypeDef(TypedDict, total=False):
    From: int
    To: int


class PortRangeTypeDef(TypedDict, total=False):
    Begin: int
    End: int


class ProcessDetailsTypeDef(TypedDict, total=False):
    Name: str
    Path: str
    Pid: int
    ParentPid: int
    LaunchedAt: str
    TerminatedAt: str


class _RequiredProductTypeDef(TypedDict):
    ProductArn: str


class ProductTypeDef(_RequiredProductTypeDef, total=False):
    ProductName: str
    CompanyName: str
    Description: str
    Categories: List[str]
    IntegrationTypes: List[IntegrationType]
    MarketplaceUrl: str
    ActivationUrl: str
    ProductSubscriptionResourcePolicy: str


class RangeTypeDef(TypedDict, total=False):
    Start: int
    End: int
    StartColumn: int


RecommendationTypeDef = TypedDict("RecommendationTypeDef", {"Text": str, "Url": str}, total=False)


class RecordTypeDef(TypedDict, total=False):
    JsonPath: str
    RecordIndex: int


class RelatedFindingTypeDef(TypedDict):
    ProductArn: str
    Id: str


class RemediationTypeDef(TypedDict, total=False):
    Recommendation: "RecommendationTypeDef"


ResourceDetailsTypeDef = TypedDict(
    "ResourceDetailsTypeDef",
    {
        "AwsAutoScalingAutoScalingGroup": "AwsAutoScalingAutoScalingGroupDetailsTypeDef",
        "AwsCodeBuildProject": "AwsCodeBuildProjectDetailsTypeDef",
        "AwsCloudFrontDistribution": "AwsCloudFrontDistributionDetailsTypeDef",
        "AwsEc2Instance": "AwsEc2InstanceDetailsTypeDef",
        "AwsEc2NetworkInterface": "AwsEc2NetworkInterfaceDetailsTypeDef",
        "AwsEc2SecurityGroup": "AwsEc2SecurityGroupDetailsTypeDef",
        "AwsEc2Volume": "AwsEc2VolumeDetailsTypeDef",
        "AwsEc2Vpc": "AwsEc2VpcDetailsTypeDef",
        "AwsEc2Eip": "AwsEc2EipDetailsTypeDef",
        "AwsEc2Subnet": "AwsEc2SubnetDetailsTypeDef",
        "AwsEc2NetworkAcl": "AwsEc2NetworkAclDetailsTypeDef",
        "AwsElbv2LoadBalancer": "AwsElbv2LoadBalancerDetailsTypeDef",
        "AwsElasticBeanstalkEnvironment": "AwsElasticBeanstalkEnvironmentDetailsTypeDef",
        "AwsElasticsearchDomain": "AwsElasticsearchDomainDetailsTypeDef",
        "AwsS3Bucket": "AwsS3BucketDetailsTypeDef",
        "AwsS3AccountPublicAccessBlock": "AwsS3AccountPublicAccessBlockDetailsTypeDef",
        "AwsS3Object": "AwsS3ObjectDetailsTypeDef",
        "AwsSecretsManagerSecret": "AwsSecretsManagerSecretDetailsTypeDef",
        "AwsIamAccessKey": "AwsIamAccessKeyDetailsTypeDef",
        "AwsIamUser": "AwsIamUserDetailsTypeDef",
        "AwsIamPolicy": "AwsIamPolicyDetailsTypeDef",
        "AwsApiGatewayV2Stage": "AwsApiGatewayV2StageDetailsTypeDef",
        "AwsApiGatewayV2Api": "AwsApiGatewayV2ApiDetailsTypeDef",
        "AwsDynamoDbTable": "AwsDynamoDbTableDetailsTypeDef",
        "AwsApiGatewayStage": "AwsApiGatewayStageDetailsTypeDef",
        "AwsApiGatewayRestApi": "AwsApiGatewayRestApiDetailsTypeDef",
        "AwsCloudTrailTrail": "AwsCloudTrailTrailDetailsTypeDef",
        "AwsSsmPatchCompliance": "AwsSsmPatchComplianceDetailsTypeDef",
        "AwsCertificateManagerCertificate": "AwsCertificateManagerCertificateDetailsTypeDef",
        "AwsRedshiftCluster": "AwsRedshiftClusterDetailsTypeDef",
        "AwsElbLoadBalancer": "AwsElbLoadBalancerDetailsTypeDef",
        "AwsIamGroup": "AwsIamGroupDetailsTypeDef",
        "AwsIamRole": "AwsIamRoleDetailsTypeDef",
        "AwsKmsKey": "AwsKmsKeyDetailsTypeDef",
        "AwsLambdaFunction": "AwsLambdaFunctionDetailsTypeDef",
        "AwsLambdaLayerVersion": "AwsLambdaLayerVersionDetailsTypeDef",
        "AwsRdsDbInstance": "AwsRdsDbInstanceDetailsTypeDef",
        "AwsSnsTopic": "AwsSnsTopicDetailsTypeDef",
        "AwsSqsQueue": "AwsSqsQueueDetailsTypeDef",
        "AwsWafWebAcl": "AwsWafWebAclDetailsTypeDef",
        "AwsRdsDbSnapshot": "AwsRdsDbSnapshotDetailsTypeDef",
        "AwsRdsDbClusterSnapshot": "AwsRdsDbClusterSnapshotDetailsTypeDef",
        "AwsRdsDbCluster": "AwsRdsDbClusterDetailsTypeDef",
        "Container": "ContainerDetailsTypeDef",
        "Other": Dict[str, str],
    },
    total=False,
)

_RequiredResourceTypeDef = TypedDict("_RequiredResourceTypeDef", {"Type": str, "Id": str})
_OptionalResourceTypeDef = TypedDict(
    "_OptionalResourceTypeDef",
    {
        "Partition": Partition,
        "Region": str,
        "ResourceRole": str,
        "Tags": Dict[str, str],
        "DataClassification": "DataClassificationDetailsTypeDef",
        "Details": "ResourceDetailsTypeDef",
    },
    total=False,
)


class ResourceTypeDef(_RequiredResourceTypeDef, _OptionalResourceTypeDef):
    pass


class ResultTypeDef(TypedDict, total=False):
    AccountId: str
    ProcessingResult: str


SensitiveDataDetectionsTypeDef = TypedDict(
    "SensitiveDataDetectionsTypeDef",
    {"Count": int, "Type": str, "Occurrences": "OccurrencesTypeDef"},
    total=False,
)


class SensitiveDataResultTypeDef(TypedDict, total=False):
    Category: str
    Detections: List["SensitiveDataDetectionsTypeDef"]
    TotalCount: int


class SeverityTypeDef(TypedDict, total=False):
    Product: float
    Label: SeverityLabel
    Normalized: int
    Original: str


class SeverityUpdateTypeDef(TypedDict, total=False):
    Normalized: int
    Product: float
    Label: SeverityLabel


class SoftwarePackageTypeDef(TypedDict, total=False):
    Name: str
    Version: str
    Epoch: str
    Release: str
    Architecture: str


class SortCriterionTypeDef(TypedDict, total=False):
    Field: str
    SortOrder: SortOrder


class StandardTypeDef(TypedDict, total=False):
    StandardsArn: str
    Name: str
    Description: str
    EnabledByDefault: bool


class StandardsControlTypeDef(TypedDict, total=False):
    StandardsControlArn: str
    ControlStatus: ControlStatus
    DisabledReason: str
    ControlStatusUpdatedAt: datetime
    ControlId: str
    Title: str
    Description: str
    RemediationUrl: str
    SeverityRating: SeverityRating
    RelatedRequirements: List[str]


class _RequiredStandardsSubscriptionRequestTypeDef(TypedDict):
    StandardsArn: str


class StandardsSubscriptionRequestTypeDef(
    _RequiredStandardsSubscriptionRequestTypeDef, total=False
):
    StandardsInput: Dict[str, str]


class StandardsSubscriptionTypeDef(TypedDict):
    StandardsSubscriptionArn: str
    StandardsArn: str
    StandardsInput: Dict[str, str]
    StandardsStatus: StandardsStatus


class _RequiredStatusReasonTypeDef(TypedDict):
    ReasonCode: str


class StatusReasonTypeDef(_RequiredStatusReasonTypeDef, total=False):
    Description: str


class StringFilterTypeDef(TypedDict, total=False):
    Value: str
    Comparison: StringFilterComparison


ThreatIntelIndicatorTypeDef = TypedDict(
    "ThreatIntelIndicatorTypeDef",
    {
        "Type": ThreatIntelIndicatorType,
        "Value": str,
        "Category": ThreatIntelIndicatorCategory,
        "LastObservedAt": str,
        "Source": str,
        "SourceUrl": str,
    },
    total=False,
)


class _RequiredVulnerabilityTypeDef(TypedDict):
    Id: str


class VulnerabilityTypeDef(_RequiredVulnerabilityTypeDef, total=False):
    VulnerablePackages: List["SoftwarePackageTypeDef"]
    Cvss: List["CvssTypeDef"]
    RelatedVulnerabilities: List[str]
    Vendor: "VulnerabilityVendorTypeDef"
    ReferenceUrls: List[str]


class _RequiredVulnerabilityVendorTypeDef(TypedDict):
    Name: str


class VulnerabilityVendorTypeDef(_RequiredVulnerabilityVendorTypeDef, total=False):
    Url: str
    VendorSeverity: str
    VendorCreatedAt: str
    VendorUpdatedAt: str


WafActionTypeDef = TypedDict("WafActionTypeDef", {"Type": str}, total=False)


class WafExcludedRuleTypeDef(TypedDict, total=False):
    RuleId: str


WafOverrideActionTypeDef = TypedDict("WafOverrideActionTypeDef", {"Type": str}, total=False)


class WorkflowTypeDef(TypedDict, total=False):
    Status: WorkflowStatus


class WorkflowUpdateTypeDef(TypedDict, total=False):
    Status: WorkflowStatus
