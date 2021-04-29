"""
Main interface for config service literal definitions.

Usage::

    ```python
    from mypy_boto3_config.literals import AggregateConformancePackComplianceSummaryGroupKey

    data: AggregateConformancePackComplianceSummaryGroupKey = "ACCOUNT_ID"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AggregateConformancePackComplianceSummaryGroupKey",
    "AggregatedSourceStatusType",
    "AggregatedSourceType",
    "ChronologicalOrder",
    "ComplianceType",
    "ConfigRuleComplianceSummaryGroupKey",
    "ConfigRuleState",
    "ConfigurationItemStatus",
    "ConformancePackComplianceType",
    "ConformancePackState",
    "DeliveryStatus",
    "DescribeAggregateComplianceByConfigRulesPaginatorName",
    "DescribeAggregationAuthorizationsPaginatorName",
    "DescribeComplianceByConfigRulePaginatorName",
    "DescribeComplianceByResourcePaginatorName",
    "DescribeConfigRuleEvaluationStatusPaginatorName",
    "DescribeConfigRulesPaginatorName",
    "DescribeConfigurationAggregatorSourcesStatusPaginatorName",
    "DescribeConfigurationAggregatorsPaginatorName",
    "DescribePendingAggregationRequestsPaginatorName",
    "DescribeRemediationExecutionStatusPaginatorName",
    "DescribeRetentionConfigurationsPaginatorName",
    "EventSource",
    "GetAggregateComplianceDetailsByConfigRulePaginatorName",
    "GetComplianceDetailsByConfigRulePaginatorName",
    "GetComplianceDetailsByResourcePaginatorName",
    "GetResourceConfigHistoryPaginatorName",
    "ListAggregateDiscoveredResourcesPaginatorName",
    "ListDiscoveredResourcesPaginatorName",
    "MaximumExecutionFrequency",
    "MemberAccountRuleStatus",
    "MessageType",
    "OrganizationConfigRuleTriggerType",
    "OrganizationResourceDetailedStatus",
    "OrganizationResourceStatus",
    "OrganizationRuleStatus",
    "Owner",
    "RecorderStatus",
    "RemediationExecutionState",
    "RemediationExecutionStepState",
    "RemediationTargetType",
    "ResourceCountGroupKey",
    "ResourceType",
    "ResourceValueType",
)


AggregateConformancePackComplianceSummaryGroupKey = Literal["ACCOUNT_ID", "AWS_REGION"]
AggregatedSourceStatusType = Literal["FAILED", "OUTDATED", "SUCCEEDED"]
AggregatedSourceType = Literal["ACCOUNT", "ORGANIZATION"]
ChronologicalOrder = Literal["Forward", "Reverse"]
ComplianceType = Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT", "NOT_APPLICABLE"]
ConfigRuleComplianceSummaryGroupKey = Literal["ACCOUNT_ID", "AWS_REGION"]
ConfigRuleState = Literal["ACTIVE", "DELETING", "DELETING_RESULTS", "EVALUATING"]
ConfigurationItemStatus = Literal[
    "OK",
    "ResourceDeleted",
    "ResourceDeletedNotRecorded",
    "ResourceDiscovered",
    "ResourceNotRecorded",
]
ConformancePackComplianceType = Literal["COMPLIANT", "INSUFFICIENT_DATA", "NON_COMPLIANT"]
ConformancePackState = Literal[
    "CREATE_COMPLETE", "CREATE_FAILED", "CREATE_IN_PROGRESS", "DELETE_FAILED", "DELETE_IN_PROGRESS"
]
DeliveryStatus = Literal["Failure", "Not_Applicable", "Success"]
DescribeAggregateComplianceByConfigRulesPaginatorName = Literal[
    "describe_aggregate_compliance_by_config_rules"
]
DescribeAggregationAuthorizationsPaginatorName = Literal["describe_aggregation_authorizations"]
DescribeComplianceByConfigRulePaginatorName = Literal["describe_compliance_by_config_rule"]
DescribeComplianceByResourcePaginatorName = Literal["describe_compliance_by_resource"]
DescribeConfigRuleEvaluationStatusPaginatorName = Literal["describe_config_rule_evaluation_status"]
DescribeConfigRulesPaginatorName = Literal["describe_config_rules"]
DescribeConfigurationAggregatorSourcesStatusPaginatorName = Literal[
    "describe_configuration_aggregator_sources_status"
]
DescribeConfigurationAggregatorsPaginatorName = Literal["describe_configuration_aggregators"]
DescribePendingAggregationRequestsPaginatorName = Literal["describe_pending_aggregation_requests"]
DescribeRemediationExecutionStatusPaginatorName = Literal["describe_remediation_execution_status"]
DescribeRetentionConfigurationsPaginatorName = Literal["describe_retention_configurations"]
EventSource = Literal["aws.config"]
GetAggregateComplianceDetailsByConfigRulePaginatorName = Literal[
    "get_aggregate_compliance_details_by_config_rule"
]
GetComplianceDetailsByConfigRulePaginatorName = Literal["get_compliance_details_by_config_rule"]
GetComplianceDetailsByResourcePaginatorName = Literal["get_compliance_details_by_resource"]
GetResourceConfigHistoryPaginatorName = Literal["get_resource_config_history"]
ListAggregateDiscoveredResourcesPaginatorName = Literal["list_aggregate_discovered_resources"]
ListDiscoveredResourcesPaginatorName = Literal["list_discovered_resources"]
MaximumExecutionFrequency = Literal[
    "One_Hour", "Six_Hours", "Three_Hours", "Twelve_Hours", "TwentyFour_Hours"
]
MemberAccountRuleStatus = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESSFUL",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_SUCCESSFUL",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
MessageType = Literal[
    "ConfigurationItemChangeNotification",
    "ConfigurationSnapshotDeliveryCompleted",
    "OversizedConfigurationItemChangeNotification",
    "ScheduledNotification",
]
OrganizationConfigRuleTriggerType = Literal[
    "ConfigurationItemChangeNotification",
    "OversizedConfigurationItemChangeNotification",
    "ScheduledNotification",
]
OrganizationResourceDetailedStatus = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESSFUL",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_SUCCESSFUL",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
OrganizationResourceStatus = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESSFUL",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_SUCCESSFUL",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
OrganizationRuleStatus = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESSFUL",
    "DELETE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_SUCCESSFUL",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
Owner = Literal["AWS", "CUSTOM_LAMBDA"]
RecorderStatus = Literal["Failure", "Pending", "Success"]
RemediationExecutionState = Literal["FAILED", "IN_PROGRESS", "QUEUED", "SUCCEEDED"]
RemediationExecutionStepState = Literal["FAILED", "PENDING", "SUCCEEDED"]
RemediationTargetType = Literal["SSM_DOCUMENT"]
ResourceCountGroupKey = Literal["ACCOUNT_ID", "AWS_REGION", "RESOURCE_TYPE"]
ResourceType = Literal[
    "AWS::ACM::Certificate",
    "AWS::ApiGateway::RestApi",
    "AWS::ApiGateway::Stage",
    "AWS::ApiGatewayV2::Api",
    "AWS::ApiGatewayV2::Stage",
    "AWS::AutoScaling::AutoScalingGroup",
    "AWS::AutoScaling::LaunchConfiguration",
    "AWS::AutoScaling::ScalingPolicy",
    "AWS::AutoScaling::ScheduledAction",
    "AWS::CloudFormation::Stack",
    "AWS::CloudFront::Distribution",
    "AWS::CloudFront::StreamingDistribution",
    "AWS::CloudTrail::Trail",
    "AWS::CloudWatch::Alarm",
    "AWS::CodeBuild::Project",
    "AWS::CodePipeline::Pipeline",
    "AWS::Config::ConformancePackCompliance",
    "AWS::Config::ResourceCompliance",
    "AWS::DynamoDB::Table",
    "AWS::EC2::CustomerGateway",
    "AWS::EC2::EIP",
    "AWS::EC2::EgressOnlyInternetGateway",
    "AWS::EC2::FlowLog",
    "AWS::EC2::Host",
    "AWS::EC2::Instance",
    "AWS::EC2::InternetGateway",
    "AWS::EC2::NatGateway",
    "AWS::EC2::NetworkAcl",
    "AWS::EC2::NetworkInterface",
    "AWS::EC2::RegisteredHAInstance",
    "AWS::EC2::RouteTable",
    "AWS::EC2::SecurityGroup",
    "AWS::EC2::Subnet",
    "AWS::EC2::VPC",
    "AWS::EC2::VPCEndpoint",
    "AWS::EC2::VPCEndpointService",
    "AWS::EC2::VPCPeeringConnection",
    "AWS::EC2::VPNConnection",
    "AWS::EC2::VPNGateway",
    "AWS::EC2::Volume",
    "AWS::ElasticBeanstalk::Application",
    "AWS::ElasticBeanstalk::ApplicationVersion",
    "AWS::ElasticBeanstalk::Environment",
    "AWS::ElasticLoadBalancing::LoadBalancer",
    "AWS::ElasticLoadBalancingV2::LoadBalancer",
    "AWS::Elasticsearch::Domain",
    "AWS::IAM::Group",
    "AWS::IAM::Policy",
    "AWS::IAM::Role",
    "AWS::IAM::User",
    "AWS::KMS::Key",
    "AWS::Lambda::Function",
    "AWS::NetworkFirewall::Firewall",
    "AWS::NetworkFirewall::FirewallPolicy",
    "AWS::NetworkFirewall::RuleGroup",
    "AWS::QLDB::Ledger",
    "AWS::RDS::DBCluster",
    "AWS::RDS::DBClusterSnapshot",
    "AWS::RDS::DBInstance",
    "AWS::RDS::DBSecurityGroup",
    "AWS::RDS::DBSnapshot",
    "AWS::RDS::DBSubnetGroup",
    "AWS::RDS::EventSubscription",
    "AWS::Redshift::Cluster",
    "AWS::Redshift::ClusterParameterGroup",
    "AWS::Redshift::ClusterSecurityGroup",
    "AWS::Redshift::ClusterSnapshot",
    "AWS::Redshift::ClusterSubnetGroup",
    "AWS::Redshift::EventSubscription",
    "AWS::S3::AccountPublicAccessBlock",
    "AWS::S3::Bucket",
    "AWS::SNS::Topic",
    "AWS::SQS::Queue",
    "AWS::SSM::AssociationCompliance",
    "AWS::SSM::FileData",
    "AWS::SSM::ManagedInstanceInventory",
    "AWS::SSM::PatchCompliance",
    "AWS::SecretsManager::Secret",
    "AWS::ServiceCatalog::CloudFormationProduct",
    "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
    "AWS::ServiceCatalog::Portfolio",
    "AWS::Shield::Protection",
    "AWS::ShieldRegional::Protection",
    "AWS::WAF::RateBasedRule",
    "AWS::WAF::Rule",
    "AWS::WAF::RuleGroup",
    "AWS::WAF::WebACL",
    "AWS::WAFRegional::RateBasedRule",
    "AWS::WAFRegional::Rule",
    "AWS::WAFRegional::RuleGroup",
    "AWS::WAFRegional::WebACL",
    "AWS::WAFv2::IPSet",
    "AWS::WAFv2::ManagedRuleSet",
    "AWS::WAFv2::RegexPatternSet",
    "AWS::WAFv2::RuleGroup",
    "AWS::WAFv2::WebACL",
    "AWS::XRay::EncryptionConfig",
]
ResourceValueType = Literal["RESOURCE_ID"]
