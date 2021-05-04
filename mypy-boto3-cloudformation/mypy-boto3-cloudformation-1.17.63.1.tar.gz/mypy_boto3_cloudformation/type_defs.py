"""
Type annotations for cloudformation service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudformation.type_defs import AccountGateResultTypeDef

    data: AccountGateResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_cloudformation.literals import (
    AccountGateStatus,
    Capability,
    ChangeAction,
    ChangeSetStatus,
    ChangeSource,
    DeprecatedStatus,
    DifferenceType,
    EvaluationType,
    ExecutionStatus,
    PermissionModels,
    ProvisioningType,
    RegionConcurrencyType,
    RegistrationStatus,
    RegistryType,
    Replacement,
    RequiresRecreation,
    ResourceAttribute,
    ResourceStatus,
    StackDriftDetectionStatus,
    StackDriftStatus,
    StackInstanceDetailedStatus,
    StackInstanceStatus,
    StackResourceDriftStatus,
    StackSetDriftDetectionStatus,
    StackSetDriftStatus,
    StackSetOperationAction,
    StackSetOperationResultStatus,
    StackSetOperationStatus,
    StackSetStatus,
    StackStatus,
    TemplateStage,
    Visibility,
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
    "AccountGateResultTypeDef",
    "AccountLimitTypeDef",
    "AutoDeploymentTypeDef",
    "ChangeSetSummaryTypeDef",
    "ChangeTypeDef",
    "CreateChangeSetOutputTypeDef",
    "CreateStackInstancesOutputTypeDef",
    "CreateStackOutputTypeDef",
    "CreateStackSetOutputTypeDef",
    "DeleteStackInstancesOutputTypeDef",
    "DeploymentTargetsTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeChangeSetOutputTypeDef",
    "DescribeStackDriftDetectionStatusOutputTypeDef",
    "DescribeStackEventsOutputTypeDef",
    "DescribeStackInstanceOutputTypeDef",
    "DescribeStackResourceDriftsOutputTypeDef",
    "DescribeStackResourceOutputTypeDef",
    "DescribeStackResourcesOutputTypeDef",
    "DescribeStackSetOperationOutputTypeDef",
    "DescribeStackSetOutputTypeDef",
    "DescribeStacksOutputTypeDef",
    "DescribeTypeOutputTypeDef",
    "DescribeTypeRegistrationOutputTypeDef",
    "DetectStackDriftOutputTypeDef",
    "DetectStackResourceDriftOutputTypeDef",
    "DetectStackSetDriftOutputTypeDef",
    "EstimateTemplateCostOutputTypeDef",
    "ExportTypeDef",
    "GetStackPolicyOutputTypeDef",
    "GetTemplateOutputTypeDef",
    "GetTemplateSummaryOutputTypeDef",
    "ListChangeSetsOutputTypeDef",
    "ListExportsOutputTypeDef",
    "ListImportsOutputTypeDef",
    "ListStackInstancesOutputTypeDef",
    "ListStackResourcesOutputTypeDef",
    "ListStackSetOperationResultsOutputTypeDef",
    "ListStackSetOperationsOutputTypeDef",
    "ListStackSetsOutputTypeDef",
    "ListStacksOutputTypeDef",
    "ListTypeRegistrationsOutputTypeDef",
    "ListTypeVersionsOutputTypeDef",
    "ListTypesOutputTypeDef",
    "LoggingConfigTypeDef",
    "ModuleInfoTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterConstraintsTypeDef",
    "ParameterDeclarationTypeDef",
    "ParameterTypeDef",
    "PhysicalResourceIdContextKeyValuePairTypeDef",
    "PropertyDifferenceTypeDef",
    "RegisterTypeOutputTypeDef",
    "ResourceChangeDetailTypeDef",
    "ResourceChangeTypeDef",
    "ResourceIdentifierSummaryTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "ResourceToImportTypeDef",
    "ResponseMetadata",
    "RollbackConfigurationTypeDef",
    "RollbackTriggerTypeDef",
    "StackDriftInformationSummaryTypeDef",
    "StackDriftInformationTypeDef",
    "StackEventTypeDef",
    "StackInstanceComprehensiveStatusTypeDef",
    "StackInstanceFilterTypeDef",
    "StackInstanceSummaryTypeDef",
    "StackInstanceTypeDef",
    "StackResourceDetailTypeDef",
    "StackResourceDriftInformationSummaryTypeDef",
    "StackResourceDriftInformationTypeDef",
    "StackResourceDriftTypeDef",
    "StackResourceSummaryTypeDef",
    "StackResourceTypeDef",
    "StackSetDriftDetectionDetailsTypeDef",
    "StackSetOperationPreferencesTypeDef",
    "StackSetOperationResultSummaryTypeDef",
    "StackSetOperationSummaryTypeDef",
    "StackSetOperationTypeDef",
    "StackSetSummaryTypeDef",
    "StackSetTypeDef",
    "StackSummaryTypeDef",
    "StackTypeDef",
    "TagTypeDef",
    "TemplateParameterTypeDef",
    "TypeSummaryTypeDef",
    "TypeVersionSummaryTypeDef",
    "UpdateStackInstancesOutputTypeDef",
    "UpdateStackOutputTypeDef",
    "UpdateStackSetOutputTypeDef",
    "UpdateTerminationProtectionOutputTypeDef",
    "ValidateTemplateOutputTypeDef",
    "WaiterConfigTypeDef",
)


class AccountGateResultTypeDef(TypedDict, total=False):
    Status: AccountGateStatus
    StatusReason: str


class AccountLimitTypeDef(TypedDict, total=False):
    Name: str
    Value: int


class AutoDeploymentTypeDef(TypedDict, total=False):
    Enabled: bool
    RetainStacksOnAccountRemoval: bool


class ChangeSetSummaryTypeDef(TypedDict, total=False):
    StackId: str
    StackName: str
    ChangeSetId: str
    ChangeSetName: str
    ExecutionStatus: ExecutionStatus
    Status: ChangeSetStatus
    StatusReason: str
    CreationTime: datetime
    Description: str
    IncludeNestedStacks: bool
    ParentChangeSetId: str
    RootChangeSetId: str


ChangeTypeDef = TypedDict(
    "ChangeTypeDef",
    {"Type": Literal["Resource"], "ResourceChange": "ResourceChangeTypeDef"},
    total=False,
)


class CreateChangeSetOutputTypeDef(TypedDict):
    Id: str
    StackId: str
    ResponseMetadata: "ResponseMetadata"


class CreateStackInstancesOutputTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: "ResponseMetadata"


class CreateStackOutputTypeDef(TypedDict):
    StackId: str
    ResponseMetadata: "ResponseMetadata"


class CreateStackSetOutputTypeDef(TypedDict):
    StackSetId: str
    ResponseMetadata: "ResponseMetadata"


class DeleteStackInstancesOutputTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: "ResponseMetadata"


class DeploymentTargetsTypeDef(TypedDict, total=False):
    Accounts: List[str]
    AccountsUrl: str
    OrganizationalUnitIds: List[str]


class DescribeAccountLimitsOutputTypeDef(TypedDict):
    AccountLimits: List["AccountLimitTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeChangeSetOutputTypeDef(TypedDict):
    ChangeSetName: str
    ChangeSetId: str
    StackId: str
    StackName: str
    Description: str
    Parameters: List["ParameterTypeDef"]
    CreationTime: datetime
    ExecutionStatus: ExecutionStatus
    Status: ChangeSetStatus
    StatusReason: str
    NotificationARNs: List[str]
    RollbackConfiguration: "RollbackConfigurationTypeDef"
    Capabilities: List[Capability]
    Tags: List["TagTypeDef"]
    Changes: List["ChangeTypeDef"]
    NextToken: str
    IncludeNestedStacks: bool
    ParentChangeSetId: str
    RootChangeSetId: str
    ResponseMetadata: "ResponseMetadata"


class DescribeStackDriftDetectionStatusOutputTypeDef(TypedDict):
    StackId: str
    StackDriftDetectionId: str
    StackDriftStatus: StackDriftStatus
    DetectionStatus: StackDriftDetectionStatus
    DetectionStatusReason: str
    DriftedStackResourceCount: int
    Timestamp: datetime
    ResponseMetadata: "ResponseMetadata"


class DescribeStackEventsOutputTypeDef(TypedDict):
    StackEvents: List["StackEventTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeStackInstanceOutputTypeDef(TypedDict):
    StackInstance: "StackInstanceTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeStackResourceDriftsOutputTypeDef(TypedDict):
    StackResourceDrifts: List["StackResourceDriftTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeStackResourceOutputTypeDef(TypedDict):
    StackResourceDetail: "StackResourceDetailTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeStackResourcesOutputTypeDef(TypedDict):
    StackResources: List["StackResourceTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeStackSetOperationOutputTypeDef(TypedDict):
    StackSetOperation: "StackSetOperationTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeStackSetOutputTypeDef(TypedDict):
    StackSet: "StackSetTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeStacksOutputTypeDef(TypedDict):
    Stacks: List["StackTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


DescribeTypeOutputTypeDef = TypedDict(
    "DescribeTypeOutputTypeDef",
    {
        "Arn": str,
        "Type": RegistryType,
        "TypeName": str,
        "DefaultVersionId": str,
        "IsDefaultVersion": bool,
        "Description": str,
        "Schema": str,
        "ProvisioningType": ProvisioningType,
        "DeprecatedStatus": DeprecatedStatus,
        "LoggingConfig": "LoggingConfigTypeDef",
        "ExecutionRoleArn": str,
        "Visibility": Visibility,
        "SourceUrl": str,
        "DocumentationUrl": str,
        "LastUpdated": datetime,
        "TimeCreated": datetime,
        "ResponseMetadata": "ResponseMetadata",
    },
)


class DescribeTypeRegistrationOutputTypeDef(TypedDict):
    ProgressStatus: RegistrationStatus
    Description: str
    TypeArn: str
    TypeVersionArn: str
    ResponseMetadata: "ResponseMetadata"


class DetectStackDriftOutputTypeDef(TypedDict):
    StackDriftDetectionId: str
    ResponseMetadata: "ResponseMetadata"


class DetectStackResourceDriftOutputTypeDef(TypedDict):
    StackResourceDrift: "StackResourceDriftTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DetectStackSetDriftOutputTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: "ResponseMetadata"


class EstimateTemplateCostOutputTypeDef(TypedDict):
    Url: str
    ResponseMetadata: "ResponseMetadata"


class ExportTypeDef(TypedDict, total=False):
    ExportingStackId: str
    Name: str
    Value: str


class GetStackPolicyOutputTypeDef(TypedDict):
    StackPolicyBody: str
    ResponseMetadata: "ResponseMetadata"


class GetTemplateOutputTypeDef(TypedDict):
    TemplateBody: str
    StagesAvailable: List[TemplateStage]
    ResponseMetadata: "ResponseMetadata"


class GetTemplateSummaryOutputTypeDef(TypedDict):
    Parameters: List["ParameterDeclarationTypeDef"]
    Description: str
    Capabilities: List[Capability]
    CapabilitiesReason: str
    ResourceTypes: List[str]
    Version: str
    Metadata: str
    DeclaredTransforms: List[str]
    ResourceIdentifierSummaries: List["ResourceIdentifierSummaryTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class ListChangeSetsOutputTypeDef(TypedDict):
    Summaries: List["ChangeSetSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListExportsOutputTypeDef(TypedDict):
    Exports: List["ExportTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListImportsOutputTypeDef(TypedDict):
    Imports: List[str]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListStackInstancesOutputTypeDef(TypedDict):
    Summaries: List["StackInstanceSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListStackResourcesOutputTypeDef(TypedDict):
    StackResourceSummaries: List["StackResourceSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListStackSetOperationResultsOutputTypeDef(TypedDict):
    Summaries: List["StackSetOperationResultSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListStackSetOperationsOutputTypeDef(TypedDict):
    Summaries: List["StackSetOperationSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListStackSetsOutputTypeDef(TypedDict):
    Summaries: List["StackSetSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListStacksOutputTypeDef(TypedDict):
    StackSummaries: List["StackSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTypeRegistrationsOutputTypeDef(TypedDict):
    RegistrationTokenList: List[str]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTypeVersionsOutputTypeDef(TypedDict):
    TypeVersionSummaries: List["TypeVersionSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTypesOutputTypeDef(TypedDict):
    TypeSummaries: List["TypeSummaryTypeDef"]
    NextToken: str
    ResponseMetadata: "ResponseMetadata"


class LoggingConfigTypeDef(TypedDict):
    LogRoleArn: str
    LogGroupName: str


class ModuleInfoTypeDef(TypedDict, total=False):
    TypeHierarchy: str
    LogicalIdHierarchy: str


class OutputTypeDef(TypedDict):
    OutputKey: str
    OutputValue: str
    Description: str
    ExportName: str
    ResponseMetadata: "ResponseMetadata"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParameterConstraintsTypeDef(TypedDict, total=False):
    AllowedValues: List[str]


class ParameterDeclarationTypeDef(TypedDict, total=False):
    ParameterKey: str
    DefaultValue: str
    ParameterType: str
    NoEcho: bool
    Description: str
    ParameterConstraints: "ParameterConstraintsTypeDef"


class ParameterTypeDef(TypedDict, total=False):
    ParameterKey: str
    ParameterValue: str
    UsePreviousValue: bool
    ResolvedValue: str


class PhysicalResourceIdContextKeyValuePairTypeDef(TypedDict):
    Key: str
    Value: str


class PropertyDifferenceTypeDef(TypedDict):
    PropertyPath: str
    ExpectedValue: str
    ActualValue: str
    DifferenceType: DifferenceType


class RegisterTypeOutputTypeDef(TypedDict):
    RegistrationToken: str
    ResponseMetadata: "ResponseMetadata"


class ResourceChangeDetailTypeDef(TypedDict, total=False):
    Target: "ResourceTargetDefinitionTypeDef"
    Evaluation: EvaluationType
    ChangeSource: ChangeSource
    CausingEntity: str


class ResourceChangeTypeDef(TypedDict, total=False):
    Action: ChangeAction
    LogicalResourceId: str
    PhysicalResourceId: str
    ResourceType: str
    Replacement: Replacement
    Scope: List[ResourceAttribute]
    Details: List["ResourceChangeDetailTypeDef"]
    ChangeSetId: str
    ModuleInfo: "ModuleInfoTypeDef"


class ResourceIdentifierSummaryTypeDef(TypedDict, total=False):
    ResourceType: str
    LogicalResourceIds: List[str]
    ResourceIdentifiers: List[str]


class ResourceTargetDefinitionTypeDef(TypedDict, total=False):
    Attribute: ResourceAttribute
    Name: str
    RequiresRecreation: RequiresRecreation


class ResourceToImportTypeDef(TypedDict):
    ResourceType: str
    LogicalResourceId: str
    ResourceIdentifier: Dict[str, str]


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class RollbackConfigurationTypeDef(TypedDict, total=False):
    RollbackTriggers: List["RollbackTriggerTypeDef"]
    MonitoringTimeInMinutes: int


RollbackTriggerTypeDef = TypedDict("RollbackTriggerTypeDef", {"Arn": str, "Type": str})


class _RequiredStackDriftInformationSummaryTypeDef(TypedDict):
    StackDriftStatus: StackDriftStatus


class StackDriftInformationSummaryTypeDef(
    _RequiredStackDriftInformationSummaryTypeDef, total=False
):
    LastCheckTimestamp: datetime


class _RequiredStackDriftInformationTypeDef(TypedDict):
    StackDriftStatus: StackDriftStatus


class StackDriftInformationTypeDef(_RequiredStackDriftInformationTypeDef, total=False):
    LastCheckTimestamp: datetime


class _RequiredStackEventTypeDef(TypedDict):
    StackId: str
    EventId: str
    StackName: str
    Timestamp: datetime


class StackEventTypeDef(_RequiredStackEventTypeDef, total=False):
    LogicalResourceId: str
    PhysicalResourceId: str
    ResourceType: str
    ResourceStatus: ResourceStatus
    ResourceStatusReason: str
    ResourceProperties: str
    ClientRequestToken: str


class StackInstanceComprehensiveStatusTypeDef(TypedDict, total=False):
    DetailedStatus: StackInstanceDetailedStatus


class StackInstanceFilterTypeDef(TypedDict, total=False):
    Name: Literal["DETAILED_STATUS"]
    Values: str


class StackInstanceSummaryTypeDef(TypedDict, total=False):
    StackSetId: str
    Region: str
    Account: str
    StackId: str
    Status: StackInstanceStatus
    StatusReason: str
    StackInstanceStatus: "StackInstanceComprehensiveStatusTypeDef"
    OrganizationalUnitId: str
    DriftStatus: StackDriftStatus
    LastDriftCheckTimestamp: datetime


class StackInstanceTypeDef(TypedDict, total=False):
    StackSetId: str
    Region: str
    Account: str
    StackId: str
    ParameterOverrides: List["ParameterTypeDef"]
    Status: StackInstanceStatus
    StackInstanceStatus: "StackInstanceComprehensiveStatusTypeDef"
    StatusReason: str
    OrganizationalUnitId: str
    DriftStatus: StackDriftStatus
    LastDriftCheckTimestamp: datetime


class _RequiredStackResourceDetailTypeDef(TypedDict):
    LogicalResourceId: str
    ResourceType: str
    LastUpdatedTimestamp: datetime
    ResourceStatus: ResourceStatus


class StackResourceDetailTypeDef(_RequiredStackResourceDetailTypeDef, total=False):
    StackName: str
    StackId: str
    PhysicalResourceId: str
    ResourceStatusReason: str
    Description: str
    Metadata: str
    DriftInformation: "StackResourceDriftInformationTypeDef"
    ModuleInfo: "ModuleInfoTypeDef"


class _RequiredStackResourceDriftInformationSummaryTypeDef(TypedDict):
    StackResourceDriftStatus: StackResourceDriftStatus


class StackResourceDriftInformationSummaryTypeDef(
    _RequiredStackResourceDriftInformationSummaryTypeDef, total=False
):
    LastCheckTimestamp: datetime


class _RequiredStackResourceDriftInformationTypeDef(TypedDict):
    StackResourceDriftStatus: StackResourceDriftStatus


class StackResourceDriftInformationTypeDef(
    _RequiredStackResourceDriftInformationTypeDef, total=False
):
    LastCheckTimestamp: datetime


class _RequiredStackResourceDriftTypeDef(TypedDict):
    StackId: str
    LogicalResourceId: str
    ResourceType: str
    StackResourceDriftStatus: StackResourceDriftStatus
    Timestamp: datetime


class StackResourceDriftTypeDef(_RequiredStackResourceDriftTypeDef, total=False):
    PhysicalResourceId: str
    PhysicalResourceIdContext: List["PhysicalResourceIdContextKeyValuePairTypeDef"]
    ExpectedProperties: str
    ActualProperties: str
    PropertyDifferences: List["PropertyDifferenceTypeDef"]
    ModuleInfo: "ModuleInfoTypeDef"


class _RequiredStackResourceSummaryTypeDef(TypedDict):
    LogicalResourceId: str
    ResourceType: str
    LastUpdatedTimestamp: datetime
    ResourceStatus: ResourceStatus


class StackResourceSummaryTypeDef(_RequiredStackResourceSummaryTypeDef, total=False):
    PhysicalResourceId: str
    ResourceStatusReason: str
    DriftInformation: "StackResourceDriftInformationSummaryTypeDef"
    ModuleInfo: "ModuleInfoTypeDef"


class _RequiredStackResourceTypeDef(TypedDict):
    LogicalResourceId: str
    ResourceType: str
    Timestamp: datetime
    ResourceStatus: ResourceStatus


class StackResourceTypeDef(_RequiredStackResourceTypeDef, total=False):
    StackName: str
    StackId: str
    PhysicalResourceId: str
    ResourceStatusReason: str
    Description: str
    DriftInformation: "StackResourceDriftInformationTypeDef"
    ModuleInfo: "ModuleInfoTypeDef"


class StackSetDriftDetectionDetailsTypeDef(TypedDict, total=False):
    DriftStatus: StackSetDriftStatus
    DriftDetectionStatus: StackSetDriftDetectionStatus
    LastDriftCheckTimestamp: datetime
    TotalStackInstancesCount: int
    DriftedStackInstancesCount: int
    InSyncStackInstancesCount: int
    InProgressStackInstancesCount: int
    FailedStackInstancesCount: int


class StackSetOperationPreferencesTypeDef(TypedDict, total=False):
    RegionConcurrencyType: RegionConcurrencyType
    RegionOrder: List[str]
    FailureToleranceCount: int
    FailureTolerancePercentage: int
    MaxConcurrentCount: int
    MaxConcurrentPercentage: int


class StackSetOperationResultSummaryTypeDef(TypedDict, total=False):
    Account: str
    Region: str
    Status: StackSetOperationResultStatus
    StatusReason: str
    AccountGateResult: "AccountGateResultTypeDef"
    OrganizationalUnitId: str


class StackSetOperationSummaryTypeDef(TypedDict, total=False):
    OperationId: str
    Action: StackSetOperationAction
    Status: StackSetOperationStatus
    CreationTimestamp: datetime
    EndTimestamp: datetime


class StackSetOperationTypeDef(TypedDict, total=False):
    OperationId: str
    StackSetId: str
    Action: StackSetOperationAction
    Status: StackSetOperationStatus
    OperationPreferences: "StackSetOperationPreferencesTypeDef"
    RetainStacks: bool
    AdministrationRoleARN: str
    ExecutionRoleName: str
    CreationTimestamp: datetime
    EndTimestamp: datetime
    DeploymentTargets: "DeploymentTargetsTypeDef"
    StackSetDriftDetectionDetails: "StackSetDriftDetectionDetailsTypeDef"


class StackSetSummaryTypeDef(TypedDict, total=False):
    StackSetName: str
    StackSetId: str
    Description: str
    Status: StackSetStatus
    AutoDeployment: "AutoDeploymentTypeDef"
    PermissionModel: PermissionModels
    DriftStatus: StackDriftStatus
    LastDriftCheckTimestamp: datetime


class StackSetTypeDef(TypedDict, total=False):
    StackSetName: str
    StackSetId: str
    Description: str
    Status: StackSetStatus
    TemplateBody: str
    Parameters: List["ParameterTypeDef"]
    Capabilities: List[Capability]
    Tags: List["TagTypeDef"]
    StackSetARN: str
    AdministrationRoleARN: str
    ExecutionRoleName: str
    StackSetDriftDetectionDetails: "StackSetDriftDetectionDetailsTypeDef"
    AutoDeployment: "AutoDeploymentTypeDef"
    PermissionModel: PermissionModels
    OrganizationalUnitIds: List[str]


class _RequiredStackSummaryTypeDef(TypedDict):
    StackName: str
    CreationTime: datetime
    StackStatus: StackStatus


class StackSummaryTypeDef(_RequiredStackSummaryTypeDef, total=False):
    StackId: str
    TemplateDescription: str
    LastUpdatedTime: datetime
    DeletionTime: datetime
    StackStatusReason: str
    ParentId: str
    RootId: str
    DriftInformation: "StackDriftInformationSummaryTypeDef"


class _RequiredStackTypeDef(TypedDict):
    StackName: str
    CreationTime: datetime
    StackStatus: StackStatus


class StackTypeDef(_RequiredStackTypeDef, total=False):
    StackId: str
    ChangeSetId: str
    Description: str
    Parameters: List["ParameterTypeDef"]
    DeletionTime: datetime
    LastUpdatedTime: datetime
    RollbackConfiguration: "RollbackConfigurationTypeDef"
    StackStatusReason: str
    DisableRollback: bool
    NotificationARNs: List[str]
    TimeoutInMinutes: int
    Capabilities: List[Capability]
    Outputs: List["OutputTypeDef"]
    RoleARN: str
    Tags: List["TagTypeDef"]
    EnableTerminationProtection: bool
    ParentId: str
    RootId: str
    DriftInformation: "StackDriftInformationTypeDef"


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TemplateParameterTypeDef(TypedDict, total=False):
    ParameterKey: str
    DefaultValue: str
    NoEcho: bool
    Description: str


TypeSummaryTypeDef = TypedDict(
    "TypeSummaryTypeDef",
    {
        "Type": RegistryType,
        "TypeName": str,
        "DefaultVersionId": str,
        "TypeArn": str,
        "LastUpdated": datetime,
        "Description": str,
    },
    total=False,
)

TypeVersionSummaryTypeDef = TypedDict(
    "TypeVersionSummaryTypeDef",
    {
        "Type": RegistryType,
        "TypeName": str,
        "VersionId": str,
        "IsDefaultVersion": bool,
        "Arn": str,
        "TimeCreated": datetime,
        "Description": str,
    },
    total=False,
)


class UpdateStackInstancesOutputTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: "ResponseMetadata"


class UpdateStackOutputTypeDef(TypedDict):
    StackId: str
    ResponseMetadata: "ResponseMetadata"


class UpdateStackSetOutputTypeDef(TypedDict):
    OperationId: str
    ResponseMetadata: "ResponseMetadata"


class UpdateTerminationProtectionOutputTypeDef(TypedDict):
    StackId: str
    ResponseMetadata: "ResponseMetadata"


class ValidateTemplateOutputTypeDef(TypedDict):
    Parameters: List["TemplateParameterTypeDef"]
    Description: str
    Capabilities: List[Capability]
    CapabilitiesReason: str
    DeclaredTransforms: List[str]
    ResponseMetadata: "ResponseMetadata"


class WaiterConfigTypeDef(TypedDict, total=False):
    Delay: int
    MaxAttempts: int
