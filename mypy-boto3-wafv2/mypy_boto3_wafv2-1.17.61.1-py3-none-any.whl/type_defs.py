"""
Type annotations for wafv2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_wafv2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_wafv2.type_defs import ActionConditionTypeDef

    data: ActionConditionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Union

from mypy_boto3_wafv2.literals import (
    ActionValue,
    BodyParsingFallbackBehavior,
    ComparisonOperator,
    CountryCode,
    FallbackBehavior,
    FilterBehavior,
    FilterRequirement,
    ForwardedIPPosition,
    IPAddressVersion,
    JsonMatchScope,
    LabelMatchScope,
    PositionalConstraint,
    RateBasedStatementAggregateKeyType,
    ResponseContentType,
    TextTransformationType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionConditionTypeDef",
    "AllowActionTypeDef",
    "AndStatementTypeDef",
    "BlockActionTypeDef",
    "ByteMatchStatementTypeDef",
    "CheckCapacityResponseTypeDef",
    "ConditionTypeDef",
    "CountActionTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateRegexPatternSetResponseTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "CreateWebACLResponseTypeDef",
    "CustomHTTPHeaderTypeDef",
    "CustomRequestHandlingTypeDef",
    "CustomResponseBodyTypeDef",
    "CustomResponseTypeDef",
    "DefaultActionTypeDef",
    "DeleteFirewallManagerRuleGroupsResponseTypeDef",
    "DescribeManagedRuleGroupResponseTypeDef",
    "ExcludedRuleTypeDef",
    "FieldToMatchTypeDef",
    "FilterTypeDef",
    "FirewallManagerRuleGroupTypeDef",
    "FirewallManagerStatementTypeDef",
    "ForwardedIPConfigTypeDef",
    "GeoMatchStatementTypeDef",
    "GetIPSetResponseTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "GetPermissionPolicyResponseTypeDef",
    "GetRateBasedStatementManagedKeysResponseTypeDef",
    "GetRegexPatternSetResponseTypeDef",
    "GetRuleGroupResponseTypeDef",
    "GetSampledRequestsResponseTypeDef",
    "GetWebACLForResourceResponseTypeDef",
    "GetWebACLResponseTypeDef",
    "HTTPHeaderTypeDef",
    "HTTPRequestTypeDef",
    "IPSetForwardedIPConfigTypeDef",
    "IPSetReferenceStatementTypeDef",
    "IPSetSummaryTypeDef",
    "IPSetTypeDef",
    "JsonBodyTypeDef",
    "JsonMatchPatternTypeDef",
    "LabelMatchStatementTypeDef",
    "LabelNameConditionTypeDef",
    "LabelSummaryTypeDef",
    "LabelTypeDef",
    "ListAvailableManagedRuleGroupsResponseTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "ListRegexPatternSetsResponseTypeDef",
    "ListResourcesForWebACLResponseTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebACLsResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "LoggingFilterTypeDef",
    "ManagedRuleGroupStatementTypeDef",
    "ManagedRuleGroupSummaryTypeDef",
    "NotStatementTypeDef",
    "OrStatementTypeDef",
    "OverrideActionTypeDef",
    "PutLoggingConfigurationResponseTypeDef",
    "RateBasedStatementManagedKeysIPSetTypeDef",
    "RateBasedStatementTypeDef",
    "RegexPatternSetReferenceStatementTypeDef",
    "RegexPatternSetSummaryTypeDef",
    "RegexPatternSetTypeDef",
    "RegexTypeDef",
    "RuleActionTypeDef",
    "RuleGroupReferenceStatementTypeDef",
    "RuleGroupSummaryTypeDef",
    "RuleGroupTypeDef",
    "RuleSummaryTypeDef",
    "RuleTypeDef",
    "SampledHTTPRequestTypeDef",
    "SingleHeaderTypeDef",
    "SingleQueryArgumentTypeDef",
    "SizeConstraintStatementTypeDef",
    "SqliMatchStatementTypeDef",
    "StatementTypeDef",
    "TagInfoForResourceTypeDef",
    "TagTypeDef",
    "TextTransformationTypeDef",
    "TimeWindowTypeDef",
    "UpdateIPSetResponseTypeDef",
    "UpdateRegexPatternSetResponseTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateWebACLResponseTypeDef",
    "VisibilityConfigTypeDef",
    "WebACLSummaryTypeDef",
    "WebACLTypeDef",
    "XssMatchStatementTypeDef",
)


class ActionConditionTypeDef(TypedDict):
    Action: ActionValue


class AllowActionTypeDef(TypedDict, total=False):
    CustomRequestHandling: "CustomRequestHandlingTypeDef"


class AndStatementTypeDef(TypedDict):
    Statements: List["StatementTypeDef"]


class BlockActionTypeDef(TypedDict, total=False):
    CustomResponse: "CustomResponseTypeDef"


class ByteMatchStatementTypeDef(TypedDict):
    SearchString: Union[bytes, IO[bytes]]
    FieldToMatch: "FieldToMatchTypeDef"
    TextTransformations: List["TextTransformationTypeDef"]
    PositionalConstraint: PositionalConstraint


class CheckCapacityResponseTypeDef(TypedDict, total=False):
    Capacity: int


class ConditionTypeDef(TypedDict, total=False):
    ActionCondition: "ActionConditionTypeDef"
    LabelNameCondition: "LabelNameConditionTypeDef"


class CountActionTypeDef(TypedDict, total=False):
    CustomRequestHandling: "CustomRequestHandlingTypeDef"


class CreateIPSetResponseTypeDef(TypedDict, total=False):
    Summary: "IPSetSummaryTypeDef"


class CreateRegexPatternSetResponseTypeDef(TypedDict, total=False):
    Summary: "RegexPatternSetSummaryTypeDef"


class CreateRuleGroupResponseTypeDef(TypedDict, total=False):
    Summary: "RuleGroupSummaryTypeDef"


class CreateWebACLResponseTypeDef(TypedDict, total=False):
    Summary: "WebACLSummaryTypeDef"


class CustomHTTPHeaderTypeDef(TypedDict):
    Name: str
    Value: str


class CustomRequestHandlingTypeDef(TypedDict):
    InsertHeaders: List["CustomHTTPHeaderTypeDef"]


class CustomResponseBodyTypeDef(TypedDict):
    ContentType: ResponseContentType
    Content: str


class _RequiredCustomResponseTypeDef(TypedDict):
    ResponseCode: int


class CustomResponseTypeDef(_RequiredCustomResponseTypeDef, total=False):
    CustomResponseBodyKey: str
    ResponseHeaders: List["CustomHTTPHeaderTypeDef"]


class DefaultActionTypeDef(TypedDict, total=False):
    Block: "BlockActionTypeDef"
    Allow: "AllowActionTypeDef"


class DeleteFirewallManagerRuleGroupsResponseTypeDef(TypedDict, total=False):
    NextWebACLLockToken: str


class DescribeManagedRuleGroupResponseTypeDef(TypedDict, total=False):
    Capacity: int
    Rules: List["RuleSummaryTypeDef"]
    LabelNamespace: str
    AvailableLabels: List["LabelSummaryTypeDef"]
    ConsumedLabels: List["LabelSummaryTypeDef"]


class ExcludedRuleTypeDef(TypedDict):
    Name: str


class FieldToMatchTypeDef(TypedDict, total=False):
    SingleHeader: "SingleHeaderTypeDef"
    SingleQueryArgument: "SingleQueryArgumentTypeDef"
    AllQueryArguments: Dict[str, Any]
    UriPath: Dict[str, Any]
    QueryString: Dict[str, Any]
    Body: Dict[str, Any]
    Method: Dict[str, Any]
    JsonBody: "JsonBodyTypeDef"


class FilterTypeDef(TypedDict):
    Behavior: FilterBehavior
    Requirement: FilterRequirement
    Conditions: List["ConditionTypeDef"]


class FirewallManagerRuleGroupTypeDef(TypedDict):
    Name: str
    Priority: int
    FirewallManagerStatement: "FirewallManagerStatementTypeDef"
    OverrideAction: "OverrideActionTypeDef"
    VisibilityConfig: "VisibilityConfigTypeDef"


class FirewallManagerStatementTypeDef(TypedDict, total=False):
    ManagedRuleGroupStatement: "ManagedRuleGroupStatementTypeDef"
    RuleGroupReferenceStatement: "RuleGroupReferenceStatementTypeDef"


class ForwardedIPConfigTypeDef(TypedDict):
    HeaderName: str
    FallbackBehavior: FallbackBehavior


class GeoMatchStatementTypeDef(TypedDict, total=False):
    CountryCodes: List[CountryCode]
    ForwardedIPConfig: "ForwardedIPConfigTypeDef"


class GetIPSetResponseTypeDef(TypedDict, total=False):
    IPSet: "IPSetTypeDef"
    LockToken: str


class GetLoggingConfigurationResponseTypeDef(TypedDict, total=False):
    LoggingConfiguration: "LoggingConfigurationTypeDef"


class GetPermissionPolicyResponseTypeDef(TypedDict, total=False):
    Policy: str


class GetRateBasedStatementManagedKeysResponseTypeDef(TypedDict, total=False):
    ManagedKeysIPV4: "RateBasedStatementManagedKeysIPSetTypeDef"
    ManagedKeysIPV6: "RateBasedStatementManagedKeysIPSetTypeDef"


class GetRegexPatternSetResponseTypeDef(TypedDict, total=False):
    RegexPatternSet: "RegexPatternSetTypeDef"
    LockToken: str


class GetRuleGroupResponseTypeDef(TypedDict, total=False):
    RuleGroup: "RuleGroupTypeDef"
    LockToken: str


class GetSampledRequestsResponseTypeDef(TypedDict, total=False):
    SampledRequests: List["SampledHTTPRequestTypeDef"]
    PopulationSize: int
    TimeWindow: "TimeWindowTypeDef"


class GetWebACLForResourceResponseTypeDef(TypedDict, total=False):
    WebACL: "WebACLTypeDef"


class GetWebACLResponseTypeDef(TypedDict, total=False):
    WebACL: "WebACLTypeDef"
    LockToken: str


class HTTPHeaderTypeDef(TypedDict, total=False):
    Name: str
    Value: str


class HTTPRequestTypeDef(TypedDict, total=False):
    ClientIP: str
    Country: str
    URI: str
    Method: str
    HTTPVersion: str
    Headers: List["HTTPHeaderTypeDef"]


class IPSetForwardedIPConfigTypeDef(TypedDict):
    HeaderName: str
    FallbackBehavior: FallbackBehavior
    Position: ForwardedIPPosition


class _RequiredIPSetReferenceStatementTypeDef(TypedDict):
    ARN: str


class IPSetReferenceStatementTypeDef(_RequiredIPSetReferenceStatementTypeDef, total=False):
    IPSetForwardedIPConfig: "IPSetForwardedIPConfigTypeDef"


class IPSetSummaryTypeDef(TypedDict, total=False):
    Name: str
    Id: str
    Description: str
    LockToken: str
    ARN: str


class _RequiredIPSetTypeDef(TypedDict):
    Name: str
    Id: str
    ARN: str
    IPAddressVersion: IPAddressVersion
    Addresses: List[str]


class IPSetTypeDef(_RequiredIPSetTypeDef, total=False):
    Description: str


class _RequiredJsonBodyTypeDef(TypedDict):
    MatchPattern: "JsonMatchPatternTypeDef"
    MatchScope: JsonMatchScope


class JsonBodyTypeDef(_RequiredJsonBodyTypeDef, total=False):
    InvalidFallbackBehavior: BodyParsingFallbackBehavior


class JsonMatchPatternTypeDef(TypedDict, total=False):
    All: Dict[str, Any]
    IncludedPaths: List[str]


class LabelMatchStatementTypeDef(TypedDict):
    Scope: LabelMatchScope
    Key: str


class LabelNameConditionTypeDef(TypedDict):
    LabelName: str


class LabelSummaryTypeDef(TypedDict, total=False):
    Name: str


class LabelTypeDef(TypedDict):
    Name: str


class ListAvailableManagedRuleGroupsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    ManagedRuleGroups: List["ManagedRuleGroupSummaryTypeDef"]


class ListIPSetsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    IPSets: List["IPSetSummaryTypeDef"]


class ListLoggingConfigurationsResponseTypeDef(TypedDict, total=False):
    LoggingConfigurations: List["LoggingConfigurationTypeDef"]
    NextMarker: str


class ListRegexPatternSetsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    RegexPatternSets: List["RegexPatternSetSummaryTypeDef"]


class ListResourcesForWebACLResponseTypeDef(TypedDict, total=False):
    ResourceArns: List[str]


class ListRuleGroupsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    RuleGroups: List["RuleGroupSummaryTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    TagInfoForResource: "TagInfoForResourceTypeDef"


class ListWebACLsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    WebACLs: List["WebACLSummaryTypeDef"]


class _RequiredLoggingConfigurationTypeDef(TypedDict):
    ResourceArn: str
    LogDestinationConfigs: List[str]


class LoggingConfigurationTypeDef(_RequiredLoggingConfigurationTypeDef, total=False):
    RedactedFields: List["FieldToMatchTypeDef"]
    ManagedByFirewallManager: bool
    LoggingFilter: "LoggingFilterTypeDef"


class LoggingFilterTypeDef(TypedDict):
    Filters: List["FilterTypeDef"]
    DefaultBehavior: FilterBehavior


class _RequiredManagedRuleGroupStatementTypeDef(TypedDict):
    VendorName: str
    Name: str


class ManagedRuleGroupStatementTypeDef(_RequiredManagedRuleGroupStatementTypeDef, total=False):
    ExcludedRules: List["ExcludedRuleTypeDef"]
    ScopeDownStatement: "StatementTypeDef"


class ManagedRuleGroupSummaryTypeDef(TypedDict, total=False):
    VendorName: str
    Name: str
    Description: str


class NotStatementTypeDef(TypedDict):
    Statement: Dict[str, Any]


class OrStatementTypeDef(TypedDict):
    Statements: List["StatementTypeDef"]


OverrideActionTypeDef = TypedDict(
    "OverrideActionTypeDef", {"Count": "CountActionTypeDef", "None": Dict[str, Any]}, total=False
)


class PutLoggingConfigurationResponseTypeDef(TypedDict, total=False):
    LoggingConfiguration: "LoggingConfigurationTypeDef"


class RateBasedStatementManagedKeysIPSetTypeDef(TypedDict, total=False):
    IPAddressVersion: IPAddressVersion
    Addresses: List[str]


class _RequiredRateBasedStatementTypeDef(TypedDict):
    Limit: int
    AggregateKeyType: RateBasedStatementAggregateKeyType


class RateBasedStatementTypeDef(_RequiredRateBasedStatementTypeDef, total=False):
    ScopeDownStatement: "StatementTypeDef"
    ForwardedIPConfig: "ForwardedIPConfigTypeDef"


class RegexPatternSetReferenceStatementTypeDef(TypedDict):
    ARN: str
    FieldToMatch: "FieldToMatchTypeDef"
    TextTransformations: List["TextTransformationTypeDef"]


class RegexPatternSetSummaryTypeDef(TypedDict, total=False):
    Name: str
    Id: str
    Description: str
    LockToken: str
    ARN: str


class RegexPatternSetTypeDef(TypedDict, total=False):
    Name: str
    Id: str
    ARN: str
    Description: str
    RegularExpressionList: List["RegexTypeDef"]


class RegexTypeDef(TypedDict, total=False):
    RegexString: str


class RuleActionTypeDef(TypedDict, total=False):
    Block: "BlockActionTypeDef"
    Allow: "AllowActionTypeDef"
    Count: "CountActionTypeDef"


class _RequiredRuleGroupReferenceStatementTypeDef(TypedDict):
    ARN: str


class RuleGroupReferenceStatementTypeDef(_RequiredRuleGroupReferenceStatementTypeDef, total=False):
    ExcludedRules: List["ExcludedRuleTypeDef"]


class RuleGroupSummaryTypeDef(TypedDict, total=False):
    Name: str
    Id: str
    Description: str
    LockToken: str
    ARN: str


class _RequiredRuleGroupTypeDef(TypedDict):
    Name: str
    Id: str
    Capacity: int
    ARN: str
    VisibilityConfig: "VisibilityConfigTypeDef"


class RuleGroupTypeDef(_RequiredRuleGroupTypeDef, total=False):
    Description: str
    Rules: List["RuleTypeDef"]
    LabelNamespace: str
    CustomResponseBodies: Dict[str, "CustomResponseBodyTypeDef"]
    AvailableLabels: List["LabelSummaryTypeDef"]
    ConsumedLabels: List["LabelSummaryTypeDef"]


class RuleSummaryTypeDef(TypedDict, total=False):
    Name: str
    Action: "RuleActionTypeDef"


class _RequiredRuleTypeDef(TypedDict):
    Name: str
    Priority: int
    Statement: "StatementTypeDef"
    VisibilityConfig: "VisibilityConfigTypeDef"


class RuleTypeDef(_RequiredRuleTypeDef, total=False):
    Action: "RuleActionTypeDef"
    OverrideAction: "OverrideActionTypeDef"
    RuleLabels: List["LabelTypeDef"]


class _RequiredSampledHTTPRequestTypeDef(TypedDict):
    Request: "HTTPRequestTypeDef"
    Weight: int


class SampledHTTPRequestTypeDef(_RequiredSampledHTTPRequestTypeDef, total=False):
    Timestamp: datetime
    Action: str
    RuleNameWithinRuleGroup: str
    RequestHeadersInserted: List["HTTPHeaderTypeDef"]
    ResponseCodeSent: int
    Labels: List["LabelTypeDef"]


class SingleHeaderTypeDef(TypedDict):
    Name: str


class SingleQueryArgumentTypeDef(TypedDict):
    Name: str


class SizeConstraintStatementTypeDef(TypedDict):
    FieldToMatch: "FieldToMatchTypeDef"
    ComparisonOperator: ComparisonOperator
    Size: int
    TextTransformations: List["TextTransformationTypeDef"]


class SqliMatchStatementTypeDef(TypedDict):
    FieldToMatch: "FieldToMatchTypeDef"
    TextTransformations: List["TextTransformationTypeDef"]


class StatementTypeDef(TypedDict, total=False):
    ByteMatchStatement: "ByteMatchStatementTypeDef"
    SqliMatchStatement: "SqliMatchStatementTypeDef"
    XssMatchStatement: "XssMatchStatementTypeDef"
    SizeConstraintStatement: "SizeConstraintStatementTypeDef"
    GeoMatchStatement: "GeoMatchStatementTypeDef"
    RuleGroupReferenceStatement: "RuleGroupReferenceStatementTypeDef"
    IPSetReferenceStatement: "IPSetReferenceStatementTypeDef"
    RegexPatternSetReferenceStatement: "RegexPatternSetReferenceStatementTypeDef"
    RateBasedStatement: Dict[str, Any]
    AndStatement: Dict[str, Any]
    OrStatement: Dict[str, Any]
    NotStatement: Dict[str, Any]
    ManagedRuleGroupStatement: Dict[str, Any]
    LabelMatchStatement: "LabelMatchStatementTypeDef"


class TagInfoForResourceTypeDef(TypedDict, total=False):
    ResourceARN: str
    TagList: List["TagTypeDef"]


class TagTypeDef(TypedDict):
    Key: str
    Value: str


TextTransformationTypeDef = TypedDict(
    "TextTransformationTypeDef", {"Priority": int, "Type": TextTransformationType}
)


class TimeWindowTypeDef(TypedDict):
    StartTime: datetime
    EndTime: datetime


class UpdateIPSetResponseTypeDef(TypedDict, total=False):
    NextLockToken: str


class UpdateRegexPatternSetResponseTypeDef(TypedDict, total=False):
    NextLockToken: str


class UpdateRuleGroupResponseTypeDef(TypedDict, total=False):
    NextLockToken: str


class UpdateWebACLResponseTypeDef(TypedDict, total=False):
    NextLockToken: str


class VisibilityConfigTypeDef(TypedDict):
    SampledRequestsEnabled: bool
    CloudWatchMetricsEnabled: bool
    MetricName: str


class WebACLSummaryTypeDef(TypedDict, total=False):
    Name: str
    Id: str
    Description: str
    LockToken: str
    ARN: str


class _RequiredWebACLTypeDef(TypedDict):
    Name: str
    Id: str
    ARN: str
    DefaultAction: "DefaultActionTypeDef"
    VisibilityConfig: "VisibilityConfigTypeDef"


class WebACLTypeDef(_RequiredWebACLTypeDef, total=False):
    Description: str
    Rules: List["RuleTypeDef"]
    Capacity: int
    PreProcessFirewallManagerRuleGroups: List["FirewallManagerRuleGroupTypeDef"]
    PostProcessFirewallManagerRuleGroups: List["FirewallManagerRuleGroupTypeDef"]
    ManagedByFirewallManager: bool
    LabelNamespace: str
    CustomResponseBodies: Dict[str, "CustomResponseBodyTypeDef"]


class XssMatchStatementTypeDef(TypedDict):
    FieldToMatch: "FieldToMatchTypeDef"
    TextTransformations: List["TextTransformationTypeDef"]
