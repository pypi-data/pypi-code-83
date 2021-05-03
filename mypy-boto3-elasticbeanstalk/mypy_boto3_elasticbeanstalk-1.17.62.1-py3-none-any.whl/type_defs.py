"""
Type annotations for elasticbeanstalk service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_elasticbeanstalk/type_defs.html)

Usage::

    ```python
    from mypy_boto3_elasticbeanstalk.type_defs import ApplicationDescriptionMessageTypeDef

    data: ApplicationDescriptionMessageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_elasticbeanstalk.literals import (
    ActionHistoryStatus,
    ActionStatus,
    ActionType,
    ApplicationVersionStatus,
    ComputeType,
    ConfigurationDeploymentStatus,
    ConfigurationOptionValueType,
    EnvironmentHealth,
    EnvironmentHealthStatus,
    EnvironmentInfoType,
    EnvironmentStatus,
    EventSeverity,
    FailureType,
    PlatformStatus,
    SourceRepository,
    SourceType,
    ValidationSeverity,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationDescriptionMessageTypeDef",
    "ApplicationDescriptionTypeDef",
    "ApplicationDescriptionsMessageTypeDef",
    "ApplicationMetricsTypeDef",
    "ApplicationResourceLifecycleConfigTypeDef",
    "ApplicationResourceLifecycleDescriptionMessageTypeDef",
    "ApplicationVersionDescriptionMessageTypeDef",
    "ApplicationVersionDescriptionTypeDef",
    "ApplicationVersionDescriptionsMessageTypeDef",
    "ApplicationVersionLifecycleConfigTypeDef",
    "ApplyEnvironmentManagedActionResultTypeDef",
    "AutoScalingGroupTypeDef",
    "BuildConfigurationTypeDef",
    "BuilderTypeDef",
    "CPUUtilizationTypeDef",
    "CheckDNSAvailabilityResultMessageTypeDef",
    "ConfigurationOptionDescriptionTypeDef",
    "ConfigurationOptionSettingTypeDef",
    "ConfigurationOptionsDescriptionTypeDef",
    "ConfigurationSettingsDescriptionTypeDef",
    "ConfigurationSettingsDescriptionsTypeDef",
    "ConfigurationSettingsValidationMessagesTypeDef",
    "CreatePlatformVersionResultTypeDef",
    "CreateStorageLocationResultMessageTypeDef",
    "CustomAmiTypeDef",
    "DeletePlatformVersionResultTypeDef",
    "DeploymentTypeDef",
    "DescribeAccountAttributesResultTypeDef",
    "DescribeEnvironmentHealthResultTypeDef",
    "DescribeEnvironmentManagedActionHistoryResultTypeDef",
    "DescribeEnvironmentManagedActionsResultTypeDef",
    "DescribeInstancesHealthResultTypeDef",
    "DescribePlatformVersionResultTypeDef",
    "EnvironmentDescriptionTypeDef",
    "EnvironmentDescriptionsMessageTypeDef",
    "EnvironmentInfoDescriptionTypeDef",
    "EnvironmentLinkTypeDef",
    "EnvironmentResourceDescriptionTypeDef",
    "EnvironmentResourceDescriptionsMessageTypeDef",
    "EnvironmentResourcesDescriptionTypeDef",
    "EnvironmentTierTypeDef",
    "EventDescriptionTypeDef",
    "EventDescriptionsMessageTypeDef",
    "InstanceHealthSummaryTypeDef",
    "InstanceTypeDef",
    "LatencyTypeDef",
    "LaunchConfigurationTypeDef",
    "LaunchTemplateTypeDef",
    "ListAvailableSolutionStacksResultMessageTypeDef",
    "ListPlatformBranchesResultTypeDef",
    "ListPlatformVersionsResultTypeDef",
    "ListenerTypeDef",
    "LoadBalancerDescriptionTypeDef",
    "LoadBalancerTypeDef",
    "ManagedActionHistoryItemTypeDef",
    "ManagedActionTypeDef",
    "MaxAgeRuleTypeDef",
    "MaxCountRuleTypeDef",
    "OptionRestrictionRegexTypeDef",
    "OptionSpecificationTypeDef",
    "PaginatorConfigTypeDef",
    "PlatformBranchSummaryTypeDef",
    "PlatformDescriptionTypeDef",
    "PlatformFilterTypeDef",
    "PlatformFrameworkTypeDef",
    "PlatformProgrammingLanguageTypeDef",
    "PlatformSummaryTypeDef",
    "QueueTypeDef",
    "ResourceQuotaTypeDef",
    "ResourceQuotasTypeDef",
    "ResourceTagsDescriptionMessageTypeDef",
    "RetrieveEnvironmentInfoResultMessageTypeDef",
    "S3LocationTypeDef",
    "SearchFilterTypeDef",
    "SingleInstanceHealthTypeDef",
    "SolutionStackDescriptionTypeDef",
    "SourceBuildInformationTypeDef",
    "SourceConfigurationTypeDef",
    "StatusCodesTypeDef",
    "SystemStatusTypeDef",
    "TagTypeDef",
    "TriggerTypeDef",
    "ValidationMessageTypeDef",
    "WaiterConfigTypeDef",
)


class ApplicationDescriptionMessageTypeDef(TypedDict, total=False):
    Application: "ApplicationDescriptionTypeDef"


class ApplicationDescriptionTypeDef(TypedDict, total=False):
    ApplicationArn: str
    ApplicationName: str
    Description: str
    DateCreated: datetime
    DateUpdated: datetime
    Versions: List[str]
    ConfigurationTemplates: List[str]
    ResourceLifecycleConfig: "ApplicationResourceLifecycleConfigTypeDef"


class ApplicationDescriptionsMessageTypeDef(TypedDict, total=False):
    Applications: List["ApplicationDescriptionTypeDef"]


class ApplicationMetricsTypeDef(TypedDict, total=False):
    Duration: int
    RequestCount: int
    StatusCodes: "StatusCodesTypeDef"
    Latency: "LatencyTypeDef"


class ApplicationResourceLifecycleConfigTypeDef(TypedDict, total=False):
    ServiceRole: str
    VersionLifecycleConfig: "ApplicationVersionLifecycleConfigTypeDef"


class ApplicationResourceLifecycleDescriptionMessageTypeDef(TypedDict, total=False):
    ApplicationName: str
    ResourceLifecycleConfig: "ApplicationResourceLifecycleConfigTypeDef"


class ApplicationVersionDescriptionMessageTypeDef(TypedDict, total=False):
    ApplicationVersion: "ApplicationVersionDescriptionTypeDef"


class ApplicationVersionDescriptionTypeDef(TypedDict, total=False):
    ApplicationVersionArn: str
    ApplicationName: str
    Description: str
    VersionLabel: str
    SourceBuildInformation: "SourceBuildInformationTypeDef"
    BuildArn: str
    SourceBundle: "S3LocationTypeDef"
    DateCreated: datetime
    DateUpdated: datetime
    Status: ApplicationVersionStatus


class ApplicationVersionDescriptionsMessageTypeDef(TypedDict, total=False):
    ApplicationVersions: List["ApplicationVersionDescriptionTypeDef"]
    NextToken: str


class ApplicationVersionLifecycleConfigTypeDef(TypedDict, total=False):
    MaxCountRule: "MaxCountRuleTypeDef"
    MaxAgeRule: "MaxAgeRuleTypeDef"


class ApplyEnvironmentManagedActionResultTypeDef(TypedDict, total=False):
    ActionId: str
    ActionDescription: str
    ActionType: ActionType
    Status: str


class AutoScalingGroupTypeDef(TypedDict, total=False):
    Name: str


class _RequiredBuildConfigurationTypeDef(TypedDict):
    CodeBuildServiceRole: str
    Image: str


class BuildConfigurationTypeDef(_RequiredBuildConfigurationTypeDef, total=False):
    ArtifactName: str
    ComputeType: ComputeType
    TimeoutInMinutes: int


class BuilderTypeDef(TypedDict, total=False):
    ARN: str


class CPUUtilizationTypeDef(TypedDict, total=False):
    User: float
    Nice: float
    System: float
    Idle: float
    IOWait: float
    IRQ: float
    SoftIRQ: float
    Privileged: float


class CheckDNSAvailabilityResultMessageTypeDef(TypedDict, total=False):
    Available: bool
    FullyQualifiedCNAME: str


class ConfigurationOptionDescriptionTypeDef(TypedDict, total=False):
    Namespace: str
    Name: str
    DefaultValue: str
    ChangeSeverity: str
    UserDefined: bool
    ValueType: ConfigurationOptionValueType
    ValueOptions: List[str]
    MinValue: int
    MaxValue: int
    MaxLength: int
    Regex: "OptionRestrictionRegexTypeDef"


class ConfigurationOptionSettingTypeDef(TypedDict, total=False):
    ResourceName: str
    Namespace: str
    OptionName: str
    Value: str


class ConfigurationOptionsDescriptionTypeDef(TypedDict, total=False):
    SolutionStackName: str
    PlatformArn: str
    Options: List["ConfigurationOptionDescriptionTypeDef"]


class ConfigurationSettingsDescriptionTypeDef(TypedDict, total=False):
    SolutionStackName: str
    PlatformArn: str
    ApplicationName: str
    TemplateName: str
    Description: str
    EnvironmentName: str
    DeploymentStatus: ConfigurationDeploymentStatus
    DateCreated: datetime
    DateUpdated: datetime
    OptionSettings: List["ConfigurationOptionSettingTypeDef"]


class ConfigurationSettingsDescriptionsTypeDef(TypedDict, total=False):
    ConfigurationSettings: List["ConfigurationSettingsDescriptionTypeDef"]


class ConfigurationSettingsValidationMessagesTypeDef(TypedDict, total=False):
    Messages: List["ValidationMessageTypeDef"]


class CreatePlatformVersionResultTypeDef(TypedDict, total=False):
    PlatformSummary: "PlatformSummaryTypeDef"
    Builder: "BuilderTypeDef"


class CreateStorageLocationResultMessageTypeDef(TypedDict, total=False):
    S3Bucket: str


class CustomAmiTypeDef(TypedDict, total=False):
    VirtualizationType: str
    ImageId: str


class DeletePlatformVersionResultTypeDef(TypedDict, total=False):
    PlatformSummary: "PlatformSummaryTypeDef"


class DeploymentTypeDef(TypedDict, total=False):
    VersionLabel: str
    DeploymentId: int
    Status: str
    DeploymentTime: datetime


class DescribeAccountAttributesResultTypeDef(TypedDict, total=False):
    ResourceQuotas: "ResourceQuotasTypeDef"


class DescribeEnvironmentHealthResultTypeDef(TypedDict, total=False):
    EnvironmentName: str
    HealthStatus: str
    Status: EnvironmentHealth
    Color: str
    Causes: List[str]
    ApplicationMetrics: "ApplicationMetricsTypeDef"
    InstancesHealth: "InstanceHealthSummaryTypeDef"
    RefreshedAt: datetime


class DescribeEnvironmentManagedActionHistoryResultTypeDef(TypedDict, total=False):
    ManagedActionHistoryItems: List["ManagedActionHistoryItemTypeDef"]
    NextToken: str


class DescribeEnvironmentManagedActionsResultTypeDef(TypedDict, total=False):
    ManagedActions: List["ManagedActionTypeDef"]


class DescribeInstancesHealthResultTypeDef(TypedDict, total=False):
    InstanceHealthList: List["SingleInstanceHealthTypeDef"]
    RefreshedAt: datetime
    NextToken: str


class DescribePlatformVersionResultTypeDef(TypedDict, total=False):
    PlatformDescription: "PlatformDescriptionTypeDef"


class EnvironmentDescriptionTypeDef(TypedDict, total=False):
    EnvironmentName: str
    EnvironmentId: str
    ApplicationName: str
    VersionLabel: str
    SolutionStackName: str
    PlatformArn: str
    TemplateName: str
    Description: str
    EndpointURL: str
    CNAME: str
    DateCreated: datetime
    DateUpdated: datetime
    Status: EnvironmentStatus
    AbortableOperationInProgress: bool
    Health: EnvironmentHealth
    HealthStatus: EnvironmentHealthStatus
    Resources: "EnvironmentResourcesDescriptionTypeDef"
    Tier: "EnvironmentTierTypeDef"
    EnvironmentLinks: List["EnvironmentLinkTypeDef"]
    EnvironmentArn: str
    OperationsRole: str


class EnvironmentDescriptionsMessageTypeDef(TypedDict, total=False):
    Environments: List["EnvironmentDescriptionTypeDef"]
    NextToken: str


class EnvironmentInfoDescriptionTypeDef(TypedDict, total=False):
    InfoType: EnvironmentInfoType
    Ec2InstanceId: str
    SampleTimestamp: datetime
    Message: str


class EnvironmentLinkTypeDef(TypedDict, total=False):
    LinkName: str
    EnvironmentName: str


class EnvironmentResourceDescriptionTypeDef(TypedDict, total=False):
    EnvironmentName: str
    AutoScalingGroups: List["AutoScalingGroupTypeDef"]
    Instances: List["InstanceTypeDef"]
    LaunchConfigurations: List["LaunchConfigurationTypeDef"]
    LaunchTemplates: List["LaunchTemplateTypeDef"]
    LoadBalancers: List["LoadBalancerTypeDef"]
    Triggers: List["TriggerTypeDef"]
    Queues: List["QueueTypeDef"]


class EnvironmentResourceDescriptionsMessageTypeDef(TypedDict, total=False):
    EnvironmentResources: "EnvironmentResourceDescriptionTypeDef"


class EnvironmentResourcesDescriptionTypeDef(TypedDict, total=False):
    LoadBalancer: "LoadBalancerDescriptionTypeDef"


EnvironmentTierTypeDef = TypedDict(
    "EnvironmentTierTypeDef", {"Name": str, "Type": str, "Version": str}, total=False
)


class EventDescriptionTypeDef(TypedDict, total=False):
    EventDate: datetime
    Message: str
    ApplicationName: str
    VersionLabel: str
    TemplateName: str
    EnvironmentName: str
    PlatformArn: str
    RequestId: str
    Severity: EventSeverity


class EventDescriptionsMessageTypeDef(TypedDict, total=False):
    Events: List["EventDescriptionTypeDef"]
    NextToken: str


InstanceHealthSummaryTypeDef = TypedDict(
    "InstanceHealthSummaryTypeDef",
    {
        "NoData": int,
        "Unknown": int,
        "Pending": int,
        "Ok": int,
        "Info": int,
        "Warning": int,
        "Degraded": int,
        "Severe": int,
    },
    total=False,
)


class InstanceTypeDef(TypedDict, total=False):
    Id: str


class LatencyTypeDef(TypedDict, total=False):
    P999: float
    P99: float
    P95: float
    P90: float
    P85: float
    P75: float
    P50: float
    P10: float


class LaunchConfigurationTypeDef(TypedDict, total=False):
    Name: str


class LaunchTemplateTypeDef(TypedDict, total=False):
    Id: str


class ListAvailableSolutionStacksResultMessageTypeDef(TypedDict, total=False):
    SolutionStacks: List[str]
    SolutionStackDetails: List["SolutionStackDescriptionTypeDef"]


class ListPlatformBranchesResultTypeDef(TypedDict, total=False):
    PlatformBranchSummaryList: List["PlatformBranchSummaryTypeDef"]
    NextToken: str


class ListPlatformVersionsResultTypeDef(TypedDict, total=False):
    PlatformSummaryList: List["PlatformSummaryTypeDef"]
    NextToken: str


ListenerTypeDef = TypedDict("ListenerTypeDef", {"Protocol": str, "Port": int}, total=False)


class LoadBalancerDescriptionTypeDef(TypedDict, total=False):
    LoadBalancerName: str
    Domain: str
    Listeners: List["ListenerTypeDef"]


class LoadBalancerTypeDef(TypedDict, total=False):
    Name: str


class ManagedActionHistoryItemTypeDef(TypedDict, total=False):
    ActionId: str
    ActionType: ActionType
    ActionDescription: str
    FailureType: FailureType
    Status: ActionHistoryStatus
    FailureDescription: str
    ExecutedTime: datetime
    FinishedTime: datetime


class ManagedActionTypeDef(TypedDict, total=False):
    ActionId: str
    ActionDescription: str
    ActionType: ActionType
    Status: ActionStatus
    WindowStartTime: datetime


class _RequiredMaxAgeRuleTypeDef(TypedDict):
    Enabled: bool


class MaxAgeRuleTypeDef(_RequiredMaxAgeRuleTypeDef, total=False):
    MaxAgeInDays: int
    DeleteSourceFromS3: bool


class _RequiredMaxCountRuleTypeDef(TypedDict):
    Enabled: bool


class MaxCountRuleTypeDef(_RequiredMaxCountRuleTypeDef, total=False):
    MaxCount: int
    DeleteSourceFromS3: bool


OptionRestrictionRegexTypeDef = TypedDict(
    "OptionRestrictionRegexTypeDef", {"Pattern": str, "Label": str}, total=False
)


class OptionSpecificationTypeDef(TypedDict, total=False):
    ResourceName: str
    Namespace: str
    OptionName: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PlatformBranchSummaryTypeDef(TypedDict, total=False):
    PlatformName: str
    BranchName: str
    LifecycleState: str
    BranchOrder: int
    SupportedTierList: List[str]


class PlatformDescriptionTypeDef(TypedDict, total=False):
    PlatformArn: str
    PlatformOwner: str
    PlatformName: str
    PlatformVersion: str
    SolutionStackName: str
    PlatformStatus: PlatformStatus
    DateCreated: datetime
    DateUpdated: datetime
    PlatformCategory: str
    Description: str
    Maintainer: str
    OperatingSystemName: str
    OperatingSystemVersion: str
    ProgrammingLanguages: List["PlatformProgrammingLanguageTypeDef"]
    Frameworks: List["PlatformFrameworkTypeDef"]
    CustomAmiList: List["CustomAmiTypeDef"]
    SupportedTierList: List[str]
    SupportedAddonList: List[str]
    PlatformLifecycleState: str
    PlatformBranchName: str
    PlatformBranchLifecycleState: str


PlatformFilterTypeDef = TypedDict(
    "PlatformFilterTypeDef", {"Type": str, "Operator": str, "Values": List[str]}, total=False
)


class PlatformFrameworkTypeDef(TypedDict, total=False):
    Name: str
    Version: str


class PlatformProgrammingLanguageTypeDef(TypedDict, total=False):
    Name: str
    Version: str


class PlatformSummaryTypeDef(TypedDict, total=False):
    PlatformArn: str
    PlatformOwner: str
    PlatformStatus: PlatformStatus
    PlatformCategory: str
    OperatingSystemName: str
    OperatingSystemVersion: str
    SupportedTierList: List[str]
    SupportedAddonList: List[str]
    PlatformLifecycleState: str
    PlatformVersion: str
    PlatformBranchName: str
    PlatformBranchLifecycleState: str


class QueueTypeDef(TypedDict, total=False):
    Name: str
    URL: str


class ResourceQuotaTypeDef(TypedDict, total=False):
    Maximum: int


class ResourceQuotasTypeDef(TypedDict, total=False):
    ApplicationQuota: "ResourceQuotaTypeDef"
    ApplicationVersionQuota: "ResourceQuotaTypeDef"
    EnvironmentQuota: "ResourceQuotaTypeDef"
    ConfigurationTemplateQuota: "ResourceQuotaTypeDef"
    CustomPlatformQuota: "ResourceQuotaTypeDef"


class ResourceTagsDescriptionMessageTypeDef(TypedDict, total=False):
    ResourceArn: str
    ResourceTags: List["TagTypeDef"]


class RetrieveEnvironmentInfoResultMessageTypeDef(TypedDict, total=False):
    EnvironmentInfo: List["EnvironmentInfoDescriptionTypeDef"]


class S3LocationTypeDef(TypedDict, total=False):
    S3Bucket: str
    S3Key: str


class SearchFilterTypeDef(TypedDict, total=False):
    Attribute: str
    Operator: str
    Values: List[str]


class SingleInstanceHealthTypeDef(TypedDict, total=False):
    InstanceId: str
    HealthStatus: str
    Color: str
    Causes: List[str]
    LaunchedAt: datetime
    ApplicationMetrics: "ApplicationMetricsTypeDef"
    System: "SystemStatusTypeDef"
    Deployment: "DeploymentTypeDef"
    AvailabilityZone: str
    InstanceType: str


class SolutionStackDescriptionTypeDef(TypedDict, total=False):
    SolutionStackName: str
    PermittedFileTypes: List[str]


class SourceBuildInformationTypeDef(TypedDict):
    SourceType: SourceType
    SourceRepository: SourceRepository
    SourceLocation: str


class SourceConfigurationTypeDef(TypedDict, total=False):
    ApplicationName: str
    TemplateName: str


class StatusCodesTypeDef(TypedDict, total=False):
    Status2xx: int
    Status3xx: int
    Status4xx: int
    Status5xx: int


class SystemStatusTypeDef(TypedDict, total=False):
    CPUUtilization: "CPUUtilizationTypeDef"
    LoadAverage: List[float]


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class TriggerTypeDef(TypedDict, total=False):
    Name: str


class ValidationMessageTypeDef(TypedDict, total=False):
    Message: str
    Severity: ValidationSeverity
    Namespace: str
    OptionName: str


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
