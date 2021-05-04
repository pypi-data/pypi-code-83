"""
Type annotations for waf service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_waf/type_defs.html)

Usage::

    ```python
    from mypy_boto3_waf.type_defs import ActivatedRuleTypeDef

    data: ActivatedRuleTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, List, Union

from mypy_boto3_waf.literals import (
    ChangeAction,
    ChangeTokenStatus,
    ComparisonOperator,
    GeoMatchConstraintValue,
    IPSetDescriptorType,
    MatchFieldType,
    PositionalConstraint,
    PredicateType,
    TextTransformation,
    WafActionType,
    WafOverrideActionType,
    WafRuleType,
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
    "ActivatedRuleTypeDef",
    "ByteMatchSetSummaryTypeDef",
    "ByteMatchSetTypeDef",
    "ByteMatchSetUpdateTypeDef",
    "ByteMatchTupleTypeDef",
    "CreateByteMatchSetResponseTypeDef",
    "CreateGeoMatchSetResponseTypeDef",
    "CreateIPSetResponseTypeDef",
    "CreateRateBasedRuleResponseTypeDef",
    "CreateRegexMatchSetResponseTypeDef",
    "CreateRegexPatternSetResponseTypeDef",
    "CreateRuleGroupResponseTypeDef",
    "CreateRuleResponseTypeDef",
    "CreateSizeConstraintSetResponseTypeDef",
    "CreateSqlInjectionMatchSetResponseTypeDef",
    "CreateWebACLMigrationStackResponseTypeDef",
    "CreateWebACLResponseTypeDef",
    "CreateXssMatchSetResponseTypeDef",
    "DeleteByteMatchSetResponseTypeDef",
    "DeleteGeoMatchSetResponseTypeDef",
    "DeleteIPSetResponseTypeDef",
    "DeleteRateBasedRuleResponseTypeDef",
    "DeleteRegexMatchSetResponseTypeDef",
    "DeleteRegexPatternSetResponseTypeDef",
    "DeleteRuleGroupResponseTypeDef",
    "DeleteRuleResponseTypeDef",
    "DeleteSizeConstraintSetResponseTypeDef",
    "DeleteSqlInjectionMatchSetResponseTypeDef",
    "DeleteWebACLResponseTypeDef",
    "DeleteXssMatchSetResponseTypeDef",
    "ExcludedRuleTypeDef",
    "FieldToMatchTypeDef",
    "GeoMatchConstraintTypeDef",
    "GeoMatchSetSummaryTypeDef",
    "GeoMatchSetTypeDef",
    "GeoMatchSetUpdateTypeDef",
    "GetByteMatchSetResponseTypeDef",
    "GetChangeTokenResponseTypeDef",
    "GetChangeTokenStatusResponseTypeDef",
    "GetGeoMatchSetResponseTypeDef",
    "GetIPSetResponseTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "GetPermissionPolicyResponseTypeDef",
    "GetRateBasedRuleManagedKeysResponseTypeDef",
    "GetRateBasedRuleResponseTypeDef",
    "GetRegexMatchSetResponseTypeDef",
    "GetRegexPatternSetResponseTypeDef",
    "GetRuleGroupResponseTypeDef",
    "GetRuleResponseTypeDef",
    "GetSampledRequestsResponseTypeDef",
    "GetSizeConstraintSetResponseTypeDef",
    "GetSqlInjectionMatchSetResponseTypeDef",
    "GetWebACLResponseTypeDef",
    "GetXssMatchSetResponseTypeDef",
    "HTTPHeaderTypeDef",
    "HTTPRequestTypeDef",
    "IPSetDescriptorTypeDef",
    "IPSetSummaryTypeDef",
    "IPSetTypeDef",
    "IPSetUpdateTypeDef",
    "ListActivatedRulesInRuleGroupResponseTypeDef",
    "ListByteMatchSetsResponseTypeDef",
    "ListGeoMatchSetsResponseTypeDef",
    "ListIPSetsResponseTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
    "ListRateBasedRulesResponseTypeDef",
    "ListRegexMatchSetsResponseTypeDef",
    "ListRegexPatternSetsResponseTypeDef",
    "ListRuleGroupsResponseTypeDef",
    "ListRulesResponseTypeDef",
    "ListSizeConstraintSetsResponseTypeDef",
    "ListSqlInjectionMatchSetsResponseTypeDef",
    "ListSubscribedRuleGroupsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWebACLsResponseTypeDef",
    "ListXssMatchSetsResponseTypeDef",
    "LoggingConfigurationTypeDef",
    "PaginatorConfigTypeDef",
    "PredicateTypeDef",
    "PutLoggingConfigurationResponseTypeDef",
    "RateBasedRuleTypeDef",
    "RegexMatchSetSummaryTypeDef",
    "RegexMatchSetTypeDef",
    "RegexMatchSetUpdateTypeDef",
    "RegexMatchTupleTypeDef",
    "RegexPatternSetSummaryTypeDef",
    "RegexPatternSetTypeDef",
    "RegexPatternSetUpdateTypeDef",
    "RuleGroupSummaryTypeDef",
    "RuleGroupTypeDef",
    "RuleGroupUpdateTypeDef",
    "RuleSummaryTypeDef",
    "RuleTypeDef",
    "RuleUpdateTypeDef",
    "SampledHTTPRequestTypeDef",
    "SizeConstraintSetSummaryTypeDef",
    "SizeConstraintSetTypeDef",
    "SizeConstraintSetUpdateTypeDef",
    "SizeConstraintTypeDef",
    "SqlInjectionMatchSetSummaryTypeDef",
    "SqlInjectionMatchSetTypeDef",
    "SqlInjectionMatchSetUpdateTypeDef",
    "SqlInjectionMatchTupleTypeDef",
    "SubscribedRuleGroupSummaryTypeDef",
    "TagInfoForResourceTypeDef",
    "TagTypeDef",
    "TimeWindowTypeDef",
    "UpdateByteMatchSetResponseTypeDef",
    "UpdateGeoMatchSetResponseTypeDef",
    "UpdateIPSetResponseTypeDef",
    "UpdateRateBasedRuleResponseTypeDef",
    "UpdateRegexMatchSetResponseTypeDef",
    "UpdateRegexPatternSetResponseTypeDef",
    "UpdateRuleGroupResponseTypeDef",
    "UpdateRuleResponseTypeDef",
    "UpdateSizeConstraintSetResponseTypeDef",
    "UpdateSqlInjectionMatchSetResponseTypeDef",
    "UpdateWebACLResponseTypeDef",
    "UpdateXssMatchSetResponseTypeDef",
    "WafActionTypeDef",
    "WafOverrideActionTypeDef",
    "WebACLSummaryTypeDef",
    "WebACLTypeDef",
    "WebACLUpdateTypeDef",
    "XssMatchSetSummaryTypeDef",
    "XssMatchSetTypeDef",
    "XssMatchSetUpdateTypeDef",
    "XssMatchTupleTypeDef",
)

_RequiredActivatedRuleTypeDef = TypedDict(
    "_RequiredActivatedRuleTypeDef", {"Priority": int, "RuleId": str}
)
_OptionalActivatedRuleTypeDef = TypedDict(
    "_OptionalActivatedRuleTypeDef",
    {
        "Action": "WafActionTypeDef",
        "OverrideAction": "WafOverrideActionTypeDef",
        "Type": WafRuleType,
        "ExcludedRules": List["ExcludedRuleTypeDef"],
    },
    total=False,
)


class ActivatedRuleTypeDef(_RequiredActivatedRuleTypeDef, _OptionalActivatedRuleTypeDef):
    pass


class ByteMatchSetSummaryTypeDef(TypedDict):
    ByteMatchSetId: str
    Name: str


class _RequiredByteMatchSetTypeDef(TypedDict):
    ByteMatchSetId: str
    ByteMatchTuples: List["ByteMatchTupleTypeDef"]


class ByteMatchSetTypeDef(_RequiredByteMatchSetTypeDef, total=False):
    Name: str


class ByteMatchSetUpdateTypeDef(TypedDict):
    Action: ChangeAction
    ByteMatchTuple: "ByteMatchTupleTypeDef"


class ByteMatchTupleTypeDef(TypedDict):
    FieldToMatch: "FieldToMatchTypeDef"
    TargetString: Union[bytes, IO[bytes]]
    TextTransformation: TextTransformation
    PositionalConstraint: PositionalConstraint


class CreateByteMatchSetResponseTypeDef(TypedDict, total=False):
    ByteMatchSet: "ByteMatchSetTypeDef"
    ChangeToken: str


class CreateGeoMatchSetResponseTypeDef(TypedDict, total=False):
    GeoMatchSet: "GeoMatchSetTypeDef"
    ChangeToken: str


class CreateIPSetResponseTypeDef(TypedDict, total=False):
    IPSet: "IPSetTypeDef"
    ChangeToken: str


class CreateRateBasedRuleResponseTypeDef(TypedDict, total=False):
    Rule: "RateBasedRuleTypeDef"
    ChangeToken: str


class CreateRegexMatchSetResponseTypeDef(TypedDict, total=False):
    RegexMatchSet: "RegexMatchSetTypeDef"
    ChangeToken: str


class CreateRegexPatternSetResponseTypeDef(TypedDict, total=False):
    RegexPatternSet: "RegexPatternSetTypeDef"
    ChangeToken: str


class CreateRuleGroupResponseTypeDef(TypedDict, total=False):
    RuleGroup: "RuleGroupTypeDef"
    ChangeToken: str


class CreateRuleResponseTypeDef(TypedDict, total=False):
    Rule: "RuleTypeDef"
    ChangeToken: str


class CreateSizeConstraintSetResponseTypeDef(TypedDict, total=False):
    SizeConstraintSet: "SizeConstraintSetTypeDef"
    ChangeToken: str


class CreateSqlInjectionMatchSetResponseTypeDef(TypedDict, total=False):
    SqlInjectionMatchSet: "SqlInjectionMatchSetTypeDef"
    ChangeToken: str


class CreateWebACLMigrationStackResponseTypeDef(TypedDict):
    S3ObjectUrl: str


class CreateWebACLResponseTypeDef(TypedDict, total=False):
    WebACL: "WebACLTypeDef"
    ChangeToken: str


class CreateXssMatchSetResponseTypeDef(TypedDict, total=False):
    XssMatchSet: "XssMatchSetTypeDef"
    ChangeToken: str


class DeleteByteMatchSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class DeleteGeoMatchSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class DeleteIPSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class DeleteRateBasedRuleResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class DeleteRegexMatchSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class DeleteRegexPatternSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class DeleteRuleGroupResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class DeleteRuleResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class DeleteSizeConstraintSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class DeleteSqlInjectionMatchSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class DeleteWebACLResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class DeleteXssMatchSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class ExcludedRuleTypeDef(TypedDict):
    RuleId: str


_RequiredFieldToMatchTypeDef = TypedDict("_RequiredFieldToMatchTypeDef", {"Type": MatchFieldType})
_OptionalFieldToMatchTypeDef = TypedDict("_OptionalFieldToMatchTypeDef", {"Data": str}, total=False)


class FieldToMatchTypeDef(_RequiredFieldToMatchTypeDef, _OptionalFieldToMatchTypeDef):
    pass


GeoMatchConstraintTypeDef = TypedDict(
    "GeoMatchConstraintTypeDef", {"Type": Literal["Country"], "Value": GeoMatchConstraintValue}
)


class GeoMatchSetSummaryTypeDef(TypedDict):
    GeoMatchSetId: str
    Name: str


class _RequiredGeoMatchSetTypeDef(TypedDict):
    GeoMatchSetId: str
    GeoMatchConstraints: List["GeoMatchConstraintTypeDef"]


class GeoMatchSetTypeDef(_RequiredGeoMatchSetTypeDef, total=False):
    Name: str


class GeoMatchSetUpdateTypeDef(TypedDict):
    Action: ChangeAction
    GeoMatchConstraint: "GeoMatchConstraintTypeDef"


class GetByteMatchSetResponseTypeDef(TypedDict, total=False):
    ByteMatchSet: "ByteMatchSetTypeDef"


class GetChangeTokenResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class GetChangeTokenStatusResponseTypeDef(TypedDict, total=False):
    ChangeTokenStatus: ChangeTokenStatus


class GetGeoMatchSetResponseTypeDef(TypedDict, total=False):
    GeoMatchSet: "GeoMatchSetTypeDef"


class GetIPSetResponseTypeDef(TypedDict, total=False):
    IPSet: "IPSetTypeDef"


class GetLoggingConfigurationResponseTypeDef(TypedDict, total=False):
    LoggingConfiguration: "LoggingConfigurationTypeDef"


class GetPermissionPolicyResponseTypeDef(TypedDict, total=False):
    Policy: str


class GetRateBasedRuleManagedKeysResponseTypeDef(TypedDict, total=False):
    ManagedKeys: List[str]
    NextMarker: str


class GetRateBasedRuleResponseTypeDef(TypedDict, total=False):
    Rule: "RateBasedRuleTypeDef"


class GetRegexMatchSetResponseTypeDef(TypedDict, total=False):
    RegexMatchSet: "RegexMatchSetTypeDef"


class GetRegexPatternSetResponseTypeDef(TypedDict, total=False):
    RegexPatternSet: "RegexPatternSetTypeDef"


class GetRuleGroupResponseTypeDef(TypedDict, total=False):
    RuleGroup: "RuleGroupTypeDef"


class GetRuleResponseTypeDef(TypedDict, total=False):
    Rule: "RuleTypeDef"


class GetSampledRequestsResponseTypeDef(TypedDict, total=False):
    SampledRequests: List["SampledHTTPRequestTypeDef"]
    PopulationSize: int
    TimeWindow: "TimeWindowTypeDef"


class GetSizeConstraintSetResponseTypeDef(TypedDict, total=False):
    SizeConstraintSet: "SizeConstraintSetTypeDef"


class GetSqlInjectionMatchSetResponseTypeDef(TypedDict, total=False):
    SqlInjectionMatchSet: "SqlInjectionMatchSetTypeDef"


class GetWebACLResponseTypeDef(TypedDict, total=False):
    WebACL: "WebACLTypeDef"


class GetXssMatchSetResponseTypeDef(TypedDict, total=False):
    XssMatchSet: "XssMatchSetTypeDef"


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


IPSetDescriptorTypeDef = TypedDict(
    "IPSetDescriptorTypeDef", {"Type": IPSetDescriptorType, "Value": str}
)


class IPSetSummaryTypeDef(TypedDict):
    IPSetId: str
    Name: str


class _RequiredIPSetTypeDef(TypedDict):
    IPSetId: str
    IPSetDescriptors: List["IPSetDescriptorTypeDef"]


class IPSetTypeDef(_RequiredIPSetTypeDef, total=False):
    Name: str


class IPSetUpdateTypeDef(TypedDict):
    Action: ChangeAction
    IPSetDescriptor: "IPSetDescriptorTypeDef"


class ListActivatedRulesInRuleGroupResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    ActivatedRules: List["ActivatedRuleTypeDef"]


class ListByteMatchSetsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    ByteMatchSets: List["ByteMatchSetSummaryTypeDef"]


class ListGeoMatchSetsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    GeoMatchSets: List["GeoMatchSetSummaryTypeDef"]


class ListIPSetsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    IPSets: List["IPSetSummaryTypeDef"]


class ListLoggingConfigurationsResponseTypeDef(TypedDict, total=False):
    LoggingConfigurations: List["LoggingConfigurationTypeDef"]
    NextMarker: str


class ListRateBasedRulesResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    Rules: List["RuleSummaryTypeDef"]


class ListRegexMatchSetsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    RegexMatchSets: List["RegexMatchSetSummaryTypeDef"]


class ListRegexPatternSetsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    RegexPatternSets: List["RegexPatternSetSummaryTypeDef"]


class ListRuleGroupsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    RuleGroups: List["RuleGroupSummaryTypeDef"]


class ListRulesResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    Rules: List["RuleSummaryTypeDef"]


class ListSizeConstraintSetsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    SizeConstraintSets: List["SizeConstraintSetSummaryTypeDef"]


class ListSqlInjectionMatchSetsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    SqlInjectionMatchSets: List["SqlInjectionMatchSetSummaryTypeDef"]


class ListSubscribedRuleGroupsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    RuleGroups: List["SubscribedRuleGroupSummaryTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    TagInfoForResource: "TagInfoForResourceTypeDef"


class ListWebACLsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    WebACLs: List["WebACLSummaryTypeDef"]


class ListXssMatchSetsResponseTypeDef(TypedDict, total=False):
    NextMarker: str
    XssMatchSets: List["XssMatchSetSummaryTypeDef"]


class _RequiredLoggingConfigurationTypeDef(TypedDict):
    ResourceArn: str
    LogDestinationConfigs: List[str]


class LoggingConfigurationTypeDef(_RequiredLoggingConfigurationTypeDef, total=False):
    RedactedFields: List["FieldToMatchTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


PredicateTypeDef = TypedDict(
    "PredicateTypeDef", {"Negated": bool, "Type": PredicateType, "DataId": str}
)


class PutLoggingConfigurationResponseTypeDef(TypedDict, total=False):
    LoggingConfiguration: "LoggingConfigurationTypeDef"


class _RequiredRateBasedRuleTypeDef(TypedDict):
    RuleId: str
    MatchPredicates: List["PredicateTypeDef"]
    RateKey: Literal["IP"]
    RateLimit: int


class RateBasedRuleTypeDef(_RequiredRateBasedRuleTypeDef, total=False):
    Name: str
    MetricName: str


class RegexMatchSetSummaryTypeDef(TypedDict):
    RegexMatchSetId: str
    Name: str


class RegexMatchSetTypeDef(TypedDict, total=False):
    RegexMatchSetId: str
    Name: str
    RegexMatchTuples: List["RegexMatchTupleTypeDef"]


class RegexMatchSetUpdateTypeDef(TypedDict):
    Action: ChangeAction
    RegexMatchTuple: "RegexMatchTupleTypeDef"


class RegexMatchTupleTypeDef(TypedDict):
    FieldToMatch: "FieldToMatchTypeDef"
    TextTransformation: TextTransformation
    RegexPatternSetId: str


class RegexPatternSetSummaryTypeDef(TypedDict):
    RegexPatternSetId: str
    Name: str


class _RequiredRegexPatternSetTypeDef(TypedDict):
    RegexPatternSetId: str
    RegexPatternStrings: List[str]


class RegexPatternSetTypeDef(_RequiredRegexPatternSetTypeDef, total=False):
    Name: str


class RegexPatternSetUpdateTypeDef(TypedDict):
    Action: ChangeAction
    RegexPatternString: str


class RuleGroupSummaryTypeDef(TypedDict):
    RuleGroupId: str
    Name: str


class _RequiredRuleGroupTypeDef(TypedDict):
    RuleGroupId: str


class RuleGroupTypeDef(_RequiredRuleGroupTypeDef, total=False):
    Name: str
    MetricName: str


class RuleGroupUpdateTypeDef(TypedDict):
    Action: ChangeAction
    ActivatedRule: "ActivatedRuleTypeDef"


class RuleSummaryTypeDef(TypedDict):
    RuleId: str
    Name: str


class _RequiredRuleTypeDef(TypedDict):
    RuleId: str
    Predicates: List["PredicateTypeDef"]


class RuleTypeDef(_RequiredRuleTypeDef, total=False):
    Name: str
    MetricName: str


class RuleUpdateTypeDef(TypedDict):
    Action: ChangeAction
    Predicate: "PredicateTypeDef"


class _RequiredSampledHTTPRequestTypeDef(TypedDict):
    Request: "HTTPRequestTypeDef"
    Weight: int


class SampledHTTPRequestTypeDef(_RequiredSampledHTTPRequestTypeDef, total=False):
    Timestamp: datetime
    Action: str
    RuleWithinRuleGroup: str


class SizeConstraintSetSummaryTypeDef(TypedDict):
    SizeConstraintSetId: str
    Name: str


class _RequiredSizeConstraintSetTypeDef(TypedDict):
    SizeConstraintSetId: str
    SizeConstraints: List["SizeConstraintTypeDef"]


class SizeConstraintSetTypeDef(_RequiredSizeConstraintSetTypeDef, total=False):
    Name: str


class SizeConstraintSetUpdateTypeDef(TypedDict):
    Action: ChangeAction
    SizeConstraint: "SizeConstraintTypeDef"


class SizeConstraintTypeDef(TypedDict):
    FieldToMatch: "FieldToMatchTypeDef"
    TextTransformation: TextTransformation
    ComparisonOperator: ComparisonOperator
    Size: int


class SqlInjectionMatchSetSummaryTypeDef(TypedDict):
    SqlInjectionMatchSetId: str
    Name: str


class _RequiredSqlInjectionMatchSetTypeDef(TypedDict):
    SqlInjectionMatchSetId: str
    SqlInjectionMatchTuples: List["SqlInjectionMatchTupleTypeDef"]


class SqlInjectionMatchSetTypeDef(_RequiredSqlInjectionMatchSetTypeDef, total=False):
    Name: str


class SqlInjectionMatchSetUpdateTypeDef(TypedDict):
    Action: ChangeAction
    SqlInjectionMatchTuple: "SqlInjectionMatchTupleTypeDef"


class SqlInjectionMatchTupleTypeDef(TypedDict):
    FieldToMatch: "FieldToMatchTypeDef"
    TextTransformation: TextTransformation


class SubscribedRuleGroupSummaryTypeDef(TypedDict):
    RuleGroupId: str
    Name: str
    MetricName: str


class TagInfoForResourceTypeDef(TypedDict, total=False):
    ResourceARN: str
    TagList: List["TagTypeDef"]


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TimeWindowTypeDef(TypedDict):
    StartTime: datetime
    EndTime: datetime


class UpdateByteMatchSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class UpdateGeoMatchSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class UpdateIPSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class UpdateRateBasedRuleResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class UpdateRegexMatchSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class UpdateRegexPatternSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class UpdateRuleGroupResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class UpdateRuleResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class UpdateSizeConstraintSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class UpdateSqlInjectionMatchSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class UpdateWebACLResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


class UpdateXssMatchSetResponseTypeDef(TypedDict, total=False):
    ChangeToken: str


WafActionTypeDef = TypedDict("WafActionTypeDef", {"Type": WafActionType})

WafOverrideActionTypeDef = TypedDict("WafOverrideActionTypeDef", {"Type": WafOverrideActionType})


class WebACLSummaryTypeDef(TypedDict):
    WebACLId: str
    Name: str


class _RequiredWebACLTypeDef(TypedDict):
    WebACLId: str
    DefaultAction: "WafActionTypeDef"
    Rules: List["ActivatedRuleTypeDef"]


class WebACLTypeDef(_RequiredWebACLTypeDef, total=False):
    Name: str
    MetricName: str
    WebACLArn: str


class WebACLUpdateTypeDef(TypedDict):
    Action: ChangeAction
    ActivatedRule: "ActivatedRuleTypeDef"


class XssMatchSetSummaryTypeDef(TypedDict):
    XssMatchSetId: str
    Name: str


class _RequiredXssMatchSetTypeDef(TypedDict):
    XssMatchSetId: str
    XssMatchTuples: List["XssMatchTupleTypeDef"]


class XssMatchSetTypeDef(_RequiredXssMatchSetTypeDef, total=False):
    Name: str


class XssMatchSetUpdateTypeDef(TypedDict):
    Action: ChangeAction
    XssMatchTuple: "XssMatchTupleTypeDef"


class XssMatchTupleTypeDef(TypedDict):
    FieldToMatch: "FieldToMatchTypeDef"
    TextTransformation: TextTransformation
