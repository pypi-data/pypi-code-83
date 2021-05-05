"""
Type annotations for cloudsearch service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudsearch.type_defs import AccessPoliciesStatusTypeDef

    data: AccessPoliciesStatusTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_cloudsearch.literals import (
    AlgorithmicStemming,
    AnalysisSchemeLanguage,
    IndexFieldType,
    OptionState,
    PartitionInstanceType,
    SuggesterFuzzyMatching,
    TLSSecurityPolicy,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AccessPoliciesStatusTypeDef",
    "AnalysisOptionsTypeDef",
    "AnalysisSchemeStatusTypeDef",
    "AnalysisSchemeTypeDef",
    "AvailabilityOptionsStatusTypeDef",
    "BuildSuggestersResponseTypeDef",
    "CreateDomainResponseTypeDef",
    "DateArrayOptionsTypeDef",
    "DateOptionsTypeDef",
    "DefineAnalysisSchemeResponseTypeDef",
    "DefineExpressionResponseTypeDef",
    "DefineIndexFieldResponseTypeDef",
    "DefineSuggesterResponseTypeDef",
    "DeleteAnalysisSchemeResponseTypeDef",
    "DeleteDomainResponseTypeDef",
    "DeleteExpressionResponseTypeDef",
    "DeleteIndexFieldResponseTypeDef",
    "DeleteSuggesterResponseTypeDef",
    "DescribeAnalysisSchemesResponseTypeDef",
    "DescribeAvailabilityOptionsResponseTypeDef",
    "DescribeDomainEndpointOptionsResponseTypeDef",
    "DescribeDomainsResponseTypeDef",
    "DescribeExpressionsResponseTypeDef",
    "DescribeIndexFieldsResponseTypeDef",
    "DescribeScalingParametersResponseTypeDef",
    "DescribeServiceAccessPoliciesResponseTypeDef",
    "DescribeSuggestersResponseTypeDef",
    "DocumentSuggesterOptionsTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "DomainEndpointOptionsTypeDef",
    "DomainStatusTypeDef",
    "DoubleArrayOptionsTypeDef",
    "DoubleOptionsTypeDef",
    "ExpressionStatusTypeDef",
    "ExpressionTypeDef",
    "IndexDocumentsResponseTypeDef",
    "IndexFieldStatusTypeDef",
    "IndexFieldTypeDef",
    "IntArrayOptionsTypeDef",
    "IntOptionsTypeDef",
    "LatLonOptionsTypeDef",
    "LimitsTypeDef",
    "ListDomainNamesResponseTypeDef",
    "LiteralArrayOptionsTypeDef",
    "LiteralOptionsTypeDef",
    "OptionStatusTypeDef",
    "ScalingParametersStatusTypeDef",
    "ScalingParametersTypeDef",
    "ServiceEndpointTypeDef",
    "SuggesterStatusTypeDef",
    "SuggesterTypeDef",
    "TextArrayOptionsTypeDef",
    "TextOptionsTypeDef",
    "UpdateAvailabilityOptionsResponseTypeDef",
    "UpdateDomainEndpointOptionsResponseTypeDef",
    "UpdateScalingParametersResponseTypeDef",
    "UpdateServiceAccessPoliciesResponseTypeDef",
)


class AccessPoliciesStatusTypeDef(TypedDict):
    Options: str
    Status: "OptionStatusTypeDef"


class AnalysisOptionsTypeDef(TypedDict, total=False):
    Synonyms: str
    Stopwords: str
    StemmingDictionary: str
    JapaneseTokenizationDictionary: str
    AlgorithmicStemming: AlgorithmicStemming


class AnalysisSchemeStatusTypeDef(TypedDict):
    Options: "AnalysisSchemeTypeDef"
    Status: "OptionStatusTypeDef"


class _RequiredAnalysisSchemeTypeDef(TypedDict):
    AnalysisSchemeName: str
    AnalysisSchemeLanguage: AnalysisSchemeLanguage


class AnalysisSchemeTypeDef(_RequiredAnalysisSchemeTypeDef, total=False):
    AnalysisOptions: "AnalysisOptionsTypeDef"


class AvailabilityOptionsStatusTypeDef(TypedDict):
    Options: bool
    Status: "OptionStatusTypeDef"


class BuildSuggestersResponseTypeDef(TypedDict, total=False):
    FieldNames: List[str]


class CreateDomainResponseTypeDef(TypedDict, total=False):
    DomainStatus: "DomainStatusTypeDef"


class DateArrayOptionsTypeDef(TypedDict, total=False):
    DefaultValue: str
    SourceFields: str
    FacetEnabled: bool
    SearchEnabled: bool
    ReturnEnabled: bool


class DateOptionsTypeDef(TypedDict, total=False):
    DefaultValue: str
    SourceField: str
    FacetEnabled: bool
    SearchEnabled: bool
    ReturnEnabled: bool
    SortEnabled: bool


class DefineAnalysisSchemeResponseTypeDef(TypedDict):
    AnalysisScheme: "AnalysisSchemeStatusTypeDef"


class DefineExpressionResponseTypeDef(TypedDict):
    Expression: "ExpressionStatusTypeDef"


class DefineIndexFieldResponseTypeDef(TypedDict):
    IndexField: "IndexFieldStatusTypeDef"


class DefineSuggesterResponseTypeDef(TypedDict):
    Suggester: "SuggesterStatusTypeDef"


class DeleteAnalysisSchemeResponseTypeDef(TypedDict):
    AnalysisScheme: "AnalysisSchemeStatusTypeDef"


class DeleteDomainResponseTypeDef(TypedDict, total=False):
    DomainStatus: "DomainStatusTypeDef"


class DeleteExpressionResponseTypeDef(TypedDict):
    Expression: "ExpressionStatusTypeDef"


class DeleteIndexFieldResponseTypeDef(TypedDict):
    IndexField: "IndexFieldStatusTypeDef"


class DeleteSuggesterResponseTypeDef(TypedDict):
    Suggester: "SuggesterStatusTypeDef"


class DescribeAnalysisSchemesResponseTypeDef(TypedDict):
    AnalysisSchemes: List["AnalysisSchemeStatusTypeDef"]


class DescribeAvailabilityOptionsResponseTypeDef(TypedDict, total=False):
    AvailabilityOptions: "AvailabilityOptionsStatusTypeDef"


class DescribeDomainEndpointOptionsResponseTypeDef(TypedDict, total=False):
    DomainEndpointOptions: "DomainEndpointOptionsStatusTypeDef"


class DescribeDomainsResponseTypeDef(TypedDict):
    DomainStatusList: List["DomainStatusTypeDef"]


class DescribeExpressionsResponseTypeDef(TypedDict):
    Expressions: List["ExpressionStatusTypeDef"]


class DescribeIndexFieldsResponseTypeDef(TypedDict):
    IndexFields: List["IndexFieldStatusTypeDef"]


class DescribeScalingParametersResponseTypeDef(TypedDict):
    ScalingParameters: "ScalingParametersStatusTypeDef"


class DescribeServiceAccessPoliciesResponseTypeDef(TypedDict):
    AccessPolicies: "AccessPoliciesStatusTypeDef"


class DescribeSuggestersResponseTypeDef(TypedDict):
    Suggesters: List["SuggesterStatusTypeDef"]


class _RequiredDocumentSuggesterOptionsTypeDef(TypedDict):
    SourceField: str


class DocumentSuggesterOptionsTypeDef(_RequiredDocumentSuggesterOptionsTypeDef, total=False):
    FuzzyMatching: SuggesterFuzzyMatching
    SortExpression: str


class DomainEndpointOptionsStatusTypeDef(TypedDict):
    Options: "DomainEndpointOptionsTypeDef"
    Status: "OptionStatusTypeDef"


class DomainEndpointOptionsTypeDef(TypedDict, total=False):
    EnforceHTTPS: bool
    TLSSecurityPolicy: TLSSecurityPolicy


class _RequiredDomainStatusTypeDef(TypedDict):
    DomainId: str
    DomainName: str
    RequiresIndexDocuments: bool


class DomainStatusTypeDef(_RequiredDomainStatusTypeDef, total=False):
    ARN: str
    Created: bool
    Deleted: bool
    DocService: "ServiceEndpointTypeDef"
    SearchService: "ServiceEndpointTypeDef"
    Processing: bool
    SearchInstanceType: str
    SearchPartitionCount: int
    SearchInstanceCount: int
    Limits: "LimitsTypeDef"


class DoubleArrayOptionsTypeDef(TypedDict, total=False):
    DefaultValue: float
    SourceFields: str
    FacetEnabled: bool
    SearchEnabled: bool
    ReturnEnabled: bool


class DoubleOptionsTypeDef(TypedDict, total=False):
    DefaultValue: float
    SourceField: str
    FacetEnabled: bool
    SearchEnabled: bool
    ReturnEnabled: bool
    SortEnabled: bool


class ExpressionStatusTypeDef(TypedDict):
    Options: "ExpressionTypeDef"
    Status: "OptionStatusTypeDef"


class ExpressionTypeDef(TypedDict):
    ExpressionName: str
    ExpressionValue: str


class IndexDocumentsResponseTypeDef(TypedDict, total=False):
    FieldNames: List[str]


class IndexFieldStatusTypeDef(TypedDict):
    Options: "IndexFieldTypeDef"
    Status: "OptionStatusTypeDef"


class _RequiredIndexFieldTypeDef(TypedDict):
    IndexFieldName: str
    IndexFieldType: IndexFieldType


class IndexFieldTypeDef(_RequiredIndexFieldTypeDef, total=False):
    IntOptions: "IntOptionsTypeDef"
    DoubleOptions: "DoubleOptionsTypeDef"
    LiteralOptions: "LiteralOptionsTypeDef"
    TextOptions: "TextOptionsTypeDef"
    DateOptions: "DateOptionsTypeDef"
    LatLonOptions: "LatLonOptionsTypeDef"
    IntArrayOptions: "IntArrayOptionsTypeDef"
    DoubleArrayOptions: "DoubleArrayOptionsTypeDef"
    LiteralArrayOptions: "LiteralArrayOptionsTypeDef"
    TextArrayOptions: "TextArrayOptionsTypeDef"
    DateArrayOptions: "DateArrayOptionsTypeDef"


class IntArrayOptionsTypeDef(TypedDict, total=False):
    DefaultValue: int
    SourceFields: str
    FacetEnabled: bool
    SearchEnabled: bool
    ReturnEnabled: bool


class IntOptionsTypeDef(TypedDict, total=False):
    DefaultValue: int
    SourceField: str
    FacetEnabled: bool
    SearchEnabled: bool
    ReturnEnabled: bool
    SortEnabled: bool


class LatLonOptionsTypeDef(TypedDict, total=False):
    DefaultValue: str
    SourceField: str
    FacetEnabled: bool
    SearchEnabled: bool
    ReturnEnabled: bool
    SortEnabled: bool


class LimitsTypeDef(TypedDict):
    MaximumReplicationCount: int
    MaximumPartitionCount: int


class ListDomainNamesResponseTypeDef(TypedDict, total=False):
    DomainNames: Dict[str, str]


class LiteralArrayOptionsTypeDef(TypedDict, total=False):
    DefaultValue: str
    SourceFields: str
    FacetEnabled: bool
    SearchEnabled: bool
    ReturnEnabled: bool


class LiteralOptionsTypeDef(TypedDict, total=False):
    DefaultValue: str
    SourceField: str
    FacetEnabled: bool
    SearchEnabled: bool
    ReturnEnabled: bool
    SortEnabled: bool


class _RequiredOptionStatusTypeDef(TypedDict):
    CreationDate: datetime
    UpdateDate: datetime
    State: OptionState


class OptionStatusTypeDef(_RequiredOptionStatusTypeDef, total=False):
    UpdateVersion: int
    PendingDeletion: bool


class ScalingParametersStatusTypeDef(TypedDict):
    Options: "ScalingParametersTypeDef"
    Status: "OptionStatusTypeDef"


class ScalingParametersTypeDef(TypedDict, total=False):
    DesiredInstanceType: PartitionInstanceType
    DesiredReplicationCount: int
    DesiredPartitionCount: int


class ServiceEndpointTypeDef(TypedDict, total=False):
    Endpoint: str


class SuggesterStatusTypeDef(TypedDict):
    Options: "SuggesterTypeDef"
    Status: "OptionStatusTypeDef"


class SuggesterTypeDef(TypedDict):
    SuggesterName: str
    DocumentSuggesterOptions: "DocumentSuggesterOptionsTypeDef"


class TextArrayOptionsTypeDef(TypedDict, total=False):
    DefaultValue: str
    SourceFields: str
    ReturnEnabled: bool
    HighlightEnabled: bool
    AnalysisScheme: str


class TextOptionsTypeDef(TypedDict, total=False):
    DefaultValue: str
    SourceField: str
    ReturnEnabled: bool
    SortEnabled: bool
    HighlightEnabled: bool
    AnalysisScheme: str


class UpdateAvailabilityOptionsResponseTypeDef(TypedDict, total=False):
    AvailabilityOptions: "AvailabilityOptionsStatusTypeDef"


class UpdateDomainEndpointOptionsResponseTypeDef(TypedDict, total=False):
    DomainEndpointOptions: "DomainEndpointOptionsStatusTypeDef"


class UpdateScalingParametersResponseTypeDef(TypedDict):
    ScalingParameters: "ScalingParametersStatusTypeDef"


class UpdateServiceAccessPoliciesResponseTypeDef(TypedDict):
    AccessPolicies: "AccessPoliciesStatusTypeDef"
