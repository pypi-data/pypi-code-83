"""
Type annotations for inspector service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_inspector/type_defs.html)

Usage::

    ```python
    from mypy_boto3_inspector.type_defs import AddAttributesToFindingsResponseTypeDef

    data: AddAttributesToFindingsResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_inspector.literals import (
    AgentHealth,
    AgentHealthCode,
    AssessmentRunNotificationSnsStatusCode,
    AssessmentRunState,
    FailedItemErrorCode,
    InspectorEvent,
    PreviewStatus,
    ReportStatus,
    ScopeType,
    Severity,
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
    "AddAttributesToFindingsResponseTypeDef",
    "AgentFilterTypeDef",
    "AgentPreviewTypeDef",
    "AssessmentRunAgentTypeDef",
    "AssessmentRunFilterTypeDef",
    "AssessmentRunNotificationTypeDef",
    "AssessmentRunStateChangeTypeDef",
    "AssessmentRunTypeDef",
    "AssessmentTargetFilterTypeDef",
    "AssessmentTargetTypeDef",
    "AssessmentTemplateFilterTypeDef",
    "AssessmentTemplateTypeDef",
    "AssetAttributesTypeDef",
    "AttributeTypeDef",
    "CreateAssessmentTargetResponseTypeDef",
    "CreateAssessmentTemplateResponseTypeDef",
    "CreateExclusionsPreviewResponseTypeDef",
    "CreateResourceGroupResponseTypeDef",
    "DescribeAssessmentRunsResponseTypeDef",
    "DescribeAssessmentTargetsResponseTypeDef",
    "DescribeAssessmentTemplatesResponseTypeDef",
    "DescribeCrossAccountAccessRoleResponseTypeDef",
    "DescribeExclusionsResponseTypeDef",
    "DescribeFindingsResponseTypeDef",
    "DescribeResourceGroupsResponseTypeDef",
    "DescribeRulesPackagesResponseTypeDef",
    "DurationRangeTypeDef",
    "EventSubscriptionTypeDef",
    "ExclusionPreviewTypeDef",
    "ExclusionTypeDef",
    "FailedItemDetailsTypeDef",
    "FindingFilterTypeDef",
    "FindingTypeDef",
    "GetAssessmentReportResponseTypeDef",
    "GetExclusionsPreviewResponseTypeDef",
    "GetTelemetryMetadataResponseTypeDef",
    "InspectorServiceAttributesTypeDef",
    "ListAssessmentRunAgentsResponseTypeDef",
    "ListAssessmentRunsResponseTypeDef",
    "ListAssessmentTargetsResponseTypeDef",
    "ListAssessmentTemplatesResponseTypeDef",
    "ListEventSubscriptionsResponseTypeDef",
    "ListExclusionsResponseTypeDef",
    "ListFindingsResponseTypeDef",
    "ListRulesPackagesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "NetworkInterfaceTypeDef",
    "PaginatorConfigTypeDef",
    "PreviewAgentsResponseTypeDef",
    "PrivateIpTypeDef",
    "RemoveAttributesFromFindingsResponseTypeDef",
    "ResourceGroupTagTypeDef",
    "ResourceGroupTypeDef",
    "RulesPackageTypeDef",
    "ScopeTypeDef",
    "SecurityGroupTypeDef",
    "StartAssessmentRunResponseTypeDef",
    "SubscriptionTypeDef",
    "TagTypeDef",
    "TelemetryMetadataTypeDef",
    "TimestampRangeTypeDef",
)


class AddAttributesToFindingsResponseTypeDef(TypedDict):
    failedItems: Dict[str, "FailedItemDetailsTypeDef"]


class AgentFilterTypeDef(TypedDict):
    agentHealths: List[AgentHealth]
    agentHealthCodes: List[AgentHealthCode]


class _RequiredAgentPreviewTypeDef(TypedDict):
    agentId: str


class AgentPreviewTypeDef(_RequiredAgentPreviewTypeDef, total=False):
    hostname: str
    autoScalingGroup: str
    agentHealth: AgentHealth
    agentVersion: str
    operatingSystem: str
    kernelVersion: str
    ipv4Address: str


class _RequiredAssessmentRunAgentTypeDef(TypedDict):
    agentId: str
    assessmentRunArn: str
    agentHealth: AgentHealth
    agentHealthCode: AgentHealthCode
    telemetryMetadata: List["TelemetryMetadataTypeDef"]


class AssessmentRunAgentTypeDef(_RequiredAssessmentRunAgentTypeDef, total=False):
    agentHealthDetails: str
    autoScalingGroup: str


class AssessmentRunFilterTypeDef(TypedDict, total=False):
    namePattern: str
    states: List[AssessmentRunState]
    durationRange: "DurationRangeTypeDef"
    rulesPackageArns: List[str]
    startTimeRange: "TimestampRangeTypeDef"
    completionTimeRange: "TimestampRangeTypeDef"
    stateChangeTimeRange: "TimestampRangeTypeDef"


class _RequiredAssessmentRunNotificationTypeDef(TypedDict):
    date: datetime
    event: InspectorEvent
    error: bool


class AssessmentRunNotificationTypeDef(_RequiredAssessmentRunNotificationTypeDef, total=False):
    message: str
    snsTopicArn: str
    snsPublishStatusCode: AssessmentRunNotificationSnsStatusCode


class AssessmentRunStateChangeTypeDef(TypedDict):
    stateChangedAt: datetime
    state: AssessmentRunState


class _RequiredAssessmentRunTypeDef(TypedDict):
    arn: str
    name: str
    assessmentTemplateArn: str
    state: AssessmentRunState
    durationInSeconds: int
    rulesPackageArns: List[str]
    userAttributesForFindings: List["AttributeTypeDef"]
    createdAt: datetime
    stateChangedAt: datetime
    dataCollected: bool
    stateChanges: List["AssessmentRunStateChangeTypeDef"]
    notifications: List["AssessmentRunNotificationTypeDef"]
    findingCounts: Dict[Severity, int]


class AssessmentRunTypeDef(_RequiredAssessmentRunTypeDef, total=False):
    startedAt: datetime
    completedAt: datetime


class AssessmentTargetFilterTypeDef(TypedDict, total=False):
    assessmentTargetNamePattern: str


class _RequiredAssessmentTargetTypeDef(TypedDict):
    arn: str
    name: str
    createdAt: datetime
    updatedAt: datetime


class AssessmentTargetTypeDef(_RequiredAssessmentTargetTypeDef, total=False):
    resourceGroupArn: str


class AssessmentTemplateFilterTypeDef(TypedDict, total=False):
    namePattern: str
    durationRange: "DurationRangeTypeDef"
    rulesPackageArns: List[str]


class _RequiredAssessmentTemplateTypeDef(TypedDict):
    arn: str
    name: str
    assessmentTargetArn: str
    durationInSeconds: int
    rulesPackageArns: List[str]
    userAttributesForFindings: List["AttributeTypeDef"]
    assessmentRunCount: int
    createdAt: datetime


class AssessmentTemplateTypeDef(_RequiredAssessmentTemplateTypeDef, total=False):
    lastAssessmentRunArn: str


class _RequiredAssetAttributesTypeDef(TypedDict):
    schemaVersion: int


class AssetAttributesTypeDef(_RequiredAssetAttributesTypeDef, total=False):
    agentId: str
    autoScalingGroup: str
    amiId: str
    hostname: str
    ipv4Addresses: List[str]
    tags: List["TagTypeDef"]
    networkInterfaces: List["NetworkInterfaceTypeDef"]


class _RequiredAttributeTypeDef(TypedDict):
    key: str


class AttributeTypeDef(_RequiredAttributeTypeDef, total=False):
    value: str


class CreateAssessmentTargetResponseTypeDef(TypedDict):
    assessmentTargetArn: str


class CreateAssessmentTemplateResponseTypeDef(TypedDict):
    assessmentTemplateArn: str


class CreateExclusionsPreviewResponseTypeDef(TypedDict):
    previewToken: str


class CreateResourceGroupResponseTypeDef(TypedDict):
    resourceGroupArn: str


class DescribeAssessmentRunsResponseTypeDef(TypedDict):
    assessmentRuns: List["AssessmentRunTypeDef"]
    failedItems: Dict[str, "FailedItemDetailsTypeDef"]


class DescribeAssessmentTargetsResponseTypeDef(TypedDict):
    assessmentTargets: List["AssessmentTargetTypeDef"]
    failedItems: Dict[str, "FailedItemDetailsTypeDef"]


class DescribeAssessmentTemplatesResponseTypeDef(TypedDict):
    assessmentTemplates: List["AssessmentTemplateTypeDef"]
    failedItems: Dict[str, "FailedItemDetailsTypeDef"]


class DescribeCrossAccountAccessRoleResponseTypeDef(TypedDict):
    roleArn: str
    valid: bool
    registeredAt: datetime


class DescribeExclusionsResponseTypeDef(TypedDict):
    exclusions: Dict[str, "ExclusionTypeDef"]
    failedItems: Dict[str, "FailedItemDetailsTypeDef"]


class DescribeFindingsResponseTypeDef(TypedDict):
    findings: List["FindingTypeDef"]
    failedItems: Dict[str, "FailedItemDetailsTypeDef"]


class DescribeResourceGroupsResponseTypeDef(TypedDict):
    resourceGroups: List["ResourceGroupTypeDef"]
    failedItems: Dict[str, "FailedItemDetailsTypeDef"]


class DescribeRulesPackagesResponseTypeDef(TypedDict):
    rulesPackages: List["RulesPackageTypeDef"]
    failedItems: Dict[str, "FailedItemDetailsTypeDef"]


class DurationRangeTypeDef(TypedDict, total=False):
    minSeconds: int
    maxSeconds: int


class EventSubscriptionTypeDef(TypedDict):
    event: InspectorEvent
    subscribedAt: datetime


class _RequiredExclusionPreviewTypeDef(TypedDict):
    title: str
    description: str
    recommendation: str
    scopes: List["ScopeTypeDef"]


class ExclusionPreviewTypeDef(_RequiredExclusionPreviewTypeDef, total=False):
    attributes: List["AttributeTypeDef"]


class _RequiredExclusionTypeDef(TypedDict):
    arn: str
    title: str
    description: str
    recommendation: str
    scopes: List["ScopeTypeDef"]


class ExclusionTypeDef(_RequiredExclusionTypeDef, total=False):
    attributes: List["AttributeTypeDef"]


class FailedItemDetailsTypeDef(TypedDict):
    failureCode: FailedItemErrorCode
    retryable: bool


class FindingFilterTypeDef(TypedDict, total=False):
    agentIds: List[str]
    autoScalingGroups: List[str]
    ruleNames: List[str]
    severities: List[Severity]
    rulesPackageArns: List[str]
    attributes: List["AttributeTypeDef"]
    userAttributes: List["AttributeTypeDef"]
    creationTimeRange: "TimestampRangeTypeDef"


_RequiredFindingTypeDef = TypedDict(
    "_RequiredFindingTypeDef",
    {
        "arn": str,
        "attributes": List["AttributeTypeDef"],
        "userAttributes": List["AttributeTypeDef"],
        "createdAt": datetime,
        "updatedAt": datetime,
    },
)
_OptionalFindingTypeDef = TypedDict(
    "_OptionalFindingTypeDef",
    {
        "schemaVersion": int,
        "service": str,
        "serviceAttributes": "InspectorServiceAttributesTypeDef",
        "assetType": Literal["ec2-instance"],
        "assetAttributes": "AssetAttributesTypeDef",
        "id": str,
        "title": str,
        "description": str,
        "recommendation": str,
        "severity": Severity,
        "numericSeverity": float,
        "confidence": int,
        "indicatorOfCompromise": bool,
    },
    total=False,
)


class FindingTypeDef(_RequiredFindingTypeDef, _OptionalFindingTypeDef):
    pass


class _RequiredGetAssessmentReportResponseTypeDef(TypedDict):
    status: ReportStatus


class GetAssessmentReportResponseTypeDef(_RequiredGetAssessmentReportResponseTypeDef, total=False):
    url: str


class _RequiredGetExclusionsPreviewResponseTypeDef(TypedDict):
    previewStatus: PreviewStatus


class GetExclusionsPreviewResponseTypeDef(
    _RequiredGetExclusionsPreviewResponseTypeDef, total=False
):
    exclusionPreviews: List["ExclusionPreviewTypeDef"]
    nextToken: str


class GetTelemetryMetadataResponseTypeDef(TypedDict):
    telemetryMetadata: List["TelemetryMetadataTypeDef"]


class _RequiredInspectorServiceAttributesTypeDef(TypedDict):
    schemaVersion: int


class InspectorServiceAttributesTypeDef(_RequiredInspectorServiceAttributesTypeDef, total=False):
    assessmentRunArn: str
    rulesPackageArn: str


class _RequiredListAssessmentRunAgentsResponseTypeDef(TypedDict):
    assessmentRunAgents: List["AssessmentRunAgentTypeDef"]


class ListAssessmentRunAgentsResponseTypeDef(
    _RequiredListAssessmentRunAgentsResponseTypeDef, total=False
):
    nextToken: str


class _RequiredListAssessmentRunsResponseTypeDef(TypedDict):
    assessmentRunArns: List[str]


class ListAssessmentRunsResponseTypeDef(_RequiredListAssessmentRunsResponseTypeDef, total=False):
    nextToken: str


class _RequiredListAssessmentTargetsResponseTypeDef(TypedDict):
    assessmentTargetArns: List[str]


class ListAssessmentTargetsResponseTypeDef(
    _RequiredListAssessmentTargetsResponseTypeDef, total=False
):
    nextToken: str


class _RequiredListAssessmentTemplatesResponseTypeDef(TypedDict):
    assessmentTemplateArns: List[str]


class ListAssessmentTemplatesResponseTypeDef(
    _RequiredListAssessmentTemplatesResponseTypeDef, total=False
):
    nextToken: str


class _RequiredListEventSubscriptionsResponseTypeDef(TypedDict):
    subscriptions: List["SubscriptionTypeDef"]


class ListEventSubscriptionsResponseTypeDef(
    _RequiredListEventSubscriptionsResponseTypeDef, total=False
):
    nextToken: str


class _RequiredListExclusionsResponseTypeDef(TypedDict):
    exclusionArns: List[str]


class ListExclusionsResponseTypeDef(_RequiredListExclusionsResponseTypeDef, total=False):
    nextToken: str


class _RequiredListFindingsResponseTypeDef(TypedDict):
    findingArns: List[str]


class ListFindingsResponseTypeDef(_RequiredListFindingsResponseTypeDef, total=False):
    nextToken: str


class _RequiredListRulesPackagesResponseTypeDef(TypedDict):
    rulesPackageArns: List[str]


class ListRulesPackagesResponseTypeDef(_RequiredListRulesPackagesResponseTypeDef, total=False):
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: List["TagTypeDef"]


class NetworkInterfaceTypeDef(TypedDict, total=False):
    networkInterfaceId: str
    subnetId: str
    vpcId: str
    privateDnsName: str
    privateIpAddress: str
    privateIpAddresses: List["PrivateIpTypeDef"]
    publicDnsName: str
    publicIp: str
    ipv6Addresses: List[str]
    securityGroups: List["SecurityGroupTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredPreviewAgentsResponseTypeDef(TypedDict):
    agentPreviews: List["AgentPreviewTypeDef"]


class PreviewAgentsResponseTypeDef(_RequiredPreviewAgentsResponseTypeDef, total=False):
    nextToken: str


class PrivateIpTypeDef(TypedDict, total=False):
    privateDnsName: str
    privateIpAddress: str


class RemoveAttributesFromFindingsResponseTypeDef(TypedDict):
    failedItems: Dict[str, "FailedItemDetailsTypeDef"]


class _RequiredResourceGroupTagTypeDef(TypedDict):
    key: str


class ResourceGroupTagTypeDef(_RequiredResourceGroupTagTypeDef, total=False):
    value: str


class ResourceGroupTypeDef(TypedDict):
    arn: str
    tags: List["ResourceGroupTagTypeDef"]
    createdAt: datetime


class _RequiredRulesPackageTypeDef(TypedDict):
    arn: str
    name: str
    version: str
    provider: str


class RulesPackageTypeDef(_RequiredRulesPackageTypeDef, total=False):
    description: str


class ScopeTypeDef(TypedDict, total=False):
    key: ScopeType
    value: str


class SecurityGroupTypeDef(TypedDict, total=False):
    groupName: str
    groupId: str


class StartAssessmentRunResponseTypeDef(TypedDict):
    assessmentRunArn: str


class SubscriptionTypeDef(TypedDict):
    resourceArn: str
    topicArn: str
    eventSubscriptions: List["EventSubscriptionTypeDef"]


class _RequiredTagTypeDef(TypedDict):
    key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    value: str


class _RequiredTelemetryMetadataTypeDef(TypedDict):
    messageType: str
    count: int


class TelemetryMetadataTypeDef(_RequiredTelemetryMetadataTypeDef, total=False):
    dataSize: int


class TimestampRangeTypeDef(TypedDict, total=False):
    beginDate: datetime
    endDate: datetime
