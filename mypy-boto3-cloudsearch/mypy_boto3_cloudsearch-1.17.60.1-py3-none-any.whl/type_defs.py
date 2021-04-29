"""
Main interface for cloudsearch service type definitions.

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
    "DateArrayOptionsTypeDef",
    "DateOptionsTypeDef",
    "DocumentSuggesterOptionsTypeDef",
    "DomainEndpointOptionsStatusTypeDef",
    "DomainEndpointOptionsTypeDef",
    "DomainStatusTypeDef",
    "DoubleArrayOptionsTypeDef",
    "DoubleOptionsTypeDef",
    "ExpressionStatusTypeDef",
    "ExpressionTypeDef",
    "IndexFieldStatusTypeDef",
    "IndexFieldTypeDef",
    "IntArrayOptionsTypeDef",
    "IntOptionsTypeDef",
    "LatLonOptionsTypeDef",
    "LimitsTypeDef",
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
    "BuildSuggestersResponseTypeDef",
    "CreateDomainResponseTypeDef",
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
    "IndexDocumentsResponseTypeDef",
    "ListDomainNamesResponseTypeDef",
    "UpdateAvailabilityOptionsResponseTypeDef",
    "UpdateDomainEndpointOptionsResponseTypeDef",
    "UpdateScalingParametersResponseTypeDef",
    "UpdateServiceAccessPoliciesResponseTypeDef",
)

AccessPoliciesStatusTypeDef = TypedDict(
    "AccessPoliciesStatusTypeDef", {"Options": str, "Status": "OptionStatusTypeDef"}
)

AnalysisOptionsTypeDef = TypedDict(
    "AnalysisOptionsTypeDef",
    {
        "Synonyms": str,
        "Stopwords": str,
        "StemmingDictionary": str,
        "JapaneseTokenizationDictionary": str,
        "AlgorithmicStemming": AlgorithmicStemming,
    },
    total=False,
)

AnalysisSchemeStatusTypeDef = TypedDict(
    "AnalysisSchemeStatusTypeDef",
    {"Options": "AnalysisSchemeTypeDef", "Status": "OptionStatusTypeDef"},
)

_RequiredAnalysisSchemeTypeDef = TypedDict(
    "_RequiredAnalysisSchemeTypeDef",
    {"AnalysisSchemeName": str, "AnalysisSchemeLanguage": AnalysisSchemeLanguage},
)
_OptionalAnalysisSchemeTypeDef = TypedDict(
    "_OptionalAnalysisSchemeTypeDef", {"AnalysisOptions": "AnalysisOptionsTypeDef"}, total=False
)


class AnalysisSchemeTypeDef(_RequiredAnalysisSchemeTypeDef, _OptionalAnalysisSchemeTypeDef):
    pass


AvailabilityOptionsStatusTypeDef = TypedDict(
    "AvailabilityOptionsStatusTypeDef", {"Options": bool, "Status": "OptionStatusTypeDef"}
)

DateArrayOptionsTypeDef = TypedDict(
    "DateArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

DateOptionsTypeDef = TypedDict(
    "DateOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

_RequiredDocumentSuggesterOptionsTypeDef = TypedDict(
    "_RequiredDocumentSuggesterOptionsTypeDef", {"SourceField": str}
)
_OptionalDocumentSuggesterOptionsTypeDef = TypedDict(
    "_OptionalDocumentSuggesterOptionsTypeDef",
    {"FuzzyMatching": SuggesterFuzzyMatching, "SortExpression": str},
    total=False,
)


class DocumentSuggesterOptionsTypeDef(
    _RequiredDocumentSuggesterOptionsTypeDef, _OptionalDocumentSuggesterOptionsTypeDef
):
    pass


DomainEndpointOptionsStatusTypeDef = TypedDict(
    "DomainEndpointOptionsStatusTypeDef",
    {"Options": "DomainEndpointOptionsTypeDef", "Status": "OptionStatusTypeDef"},
)

DomainEndpointOptionsTypeDef = TypedDict(
    "DomainEndpointOptionsTypeDef",
    {"EnforceHTTPS": bool, "TLSSecurityPolicy": TLSSecurityPolicy},
    total=False,
)

_RequiredDomainStatusTypeDef = TypedDict(
    "_RequiredDomainStatusTypeDef",
    {"DomainId": str, "DomainName": str, "RequiresIndexDocuments": bool},
)
_OptionalDomainStatusTypeDef = TypedDict(
    "_OptionalDomainStatusTypeDef",
    {
        "ARN": str,
        "Created": bool,
        "Deleted": bool,
        "DocService": "ServiceEndpointTypeDef",
        "SearchService": "ServiceEndpointTypeDef",
        "Processing": bool,
        "SearchInstanceType": str,
        "SearchPartitionCount": int,
        "SearchInstanceCount": int,
        "Limits": "LimitsTypeDef",
    },
    total=False,
)


class DomainStatusTypeDef(_RequiredDomainStatusTypeDef, _OptionalDomainStatusTypeDef):
    pass


DoubleArrayOptionsTypeDef = TypedDict(
    "DoubleArrayOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

DoubleOptionsTypeDef = TypedDict(
    "DoubleOptionsTypeDef",
    {
        "DefaultValue": float,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

ExpressionStatusTypeDef = TypedDict(
    "ExpressionStatusTypeDef", {"Options": "ExpressionTypeDef", "Status": "OptionStatusTypeDef"}
)

ExpressionTypeDef = TypedDict("ExpressionTypeDef", {"ExpressionName": str, "ExpressionValue": str})

IndexFieldStatusTypeDef = TypedDict(
    "IndexFieldStatusTypeDef", {"Options": "IndexFieldTypeDef", "Status": "OptionStatusTypeDef"}
)

_RequiredIndexFieldTypeDef = TypedDict(
    "_RequiredIndexFieldTypeDef", {"IndexFieldName": str, "IndexFieldType": IndexFieldType}
)
_OptionalIndexFieldTypeDef = TypedDict(
    "_OptionalIndexFieldTypeDef",
    {
        "IntOptions": "IntOptionsTypeDef",
        "DoubleOptions": "DoubleOptionsTypeDef",
        "LiteralOptions": "LiteralOptionsTypeDef",
        "TextOptions": "TextOptionsTypeDef",
        "DateOptions": "DateOptionsTypeDef",
        "LatLonOptions": "LatLonOptionsTypeDef",
        "IntArrayOptions": "IntArrayOptionsTypeDef",
        "DoubleArrayOptions": "DoubleArrayOptionsTypeDef",
        "LiteralArrayOptions": "LiteralArrayOptionsTypeDef",
        "TextArrayOptions": "TextArrayOptionsTypeDef",
        "DateArrayOptions": "DateArrayOptionsTypeDef",
    },
    total=False,
)


class IndexFieldTypeDef(_RequiredIndexFieldTypeDef, _OptionalIndexFieldTypeDef):
    pass


IntArrayOptionsTypeDef = TypedDict(
    "IntArrayOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

IntOptionsTypeDef = TypedDict(
    "IntOptionsTypeDef",
    {
        "DefaultValue": int,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

LatLonOptionsTypeDef = TypedDict(
    "LatLonOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

LimitsTypeDef = TypedDict(
    "LimitsTypeDef", {"MaximumReplicationCount": int, "MaximumPartitionCount": int}
)

LiteralArrayOptionsTypeDef = TypedDict(
    "LiteralArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
    },
    total=False,
)

LiteralOptionsTypeDef = TypedDict(
    "LiteralOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "FacetEnabled": bool,
        "SearchEnabled": bool,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
    },
    total=False,
)

_RequiredOptionStatusTypeDef = TypedDict(
    "_RequiredOptionStatusTypeDef",
    {"CreationDate": datetime, "UpdateDate": datetime, "State": OptionState},
)
_OptionalOptionStatusTypeDef = TypedDict(
    "_OptionalOptionStatusTypeDef", {"UpdateVersion": int, "PendingDeletion": bool}, total=False
)


class OptionStatusTypeDef(_RequiredOptionStatusTypeDef, _OptionalOptionStatusTypeDef):
    pass


ScalingParametersStatusTypeDef = TypedDict(
    "ScalingParametersStatusTypeDef",
    {"Options": "ScalingParametersTypeDef", "Status": "OptionStatusTypeDef"},
)

ScalingParametersTypeDef = TypedDict(
    "ScalingParametersTypeDef",
    {
        "DesiredInstanceType": PartitionInstanceType,
        "DesiredReplicationCount": int,
        "DesiredPartitionCount": int,
    },
    total=False,
)

ServiceEndpointTypeDef = TypedDict("ServiceEndpointTypeDef", {"Endpoint": str}, total=False)

SuggesterStatusTypeDef = TypedDict(
    "SuggesterStatusTypeDef", {"Options": "SuggesterTypeDef", "Status": "OptionStatusTypeDef"}
)

SuggesterTypeDef = TypedDict(
    "SuggesterTypeDef",
    {"SuggesterName": str, "DocumentSuggesterOptions": "DocumentSuggesterOptionsTypeDef"},
)

TextArrayOptionsTypeDef = TypedDict(
    "TextArrayOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceFields": str,
        "ReturnEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

TextOptionsTypeDef = TypedDict(
    "TextOptionsTypeDef",
    {
        "DefaultValue": str,
        "SourceField": str,
        "ReturnEnabled": bool,
        "SortEnabled": bool,
        "HighlightEnabled": bool,
        "AnalysisScheme": str,
    },
    total=False,
)

BuildSuggestersResponseTypeDef = TypedDict(
    "BuildSuggestersResponseTypeDef", {"FieldNames": List[str]}, total=False
)

CreateDomainResponseTypeDef = TypedDict(
    "CreateDomainResponseTypeDef", {"DomainStatus": "DomainStatusTypeDef"}, total=False
)

DefineAnalysisSchemeResponseTypeDef = TypedDict(
    "DefineAnalysisSchemeResponseTypeDef", {"AnalysisScheme": "AnalysisSchemeStatusTypeDef"}
)

DefineExpressionResponseTypeDef = TypedDict(
    "DefineExpressionResponseTypeDef", {"Expression": "ExpressionStatusTypeDef"}
)

DefineIndexFieldResponseTypeDef = TypedDict(
    "DefineIndexFieldResponseTypeDef", {"IndexField": "IndexFieldStatusTypeDef"}
)

DefineSuggesterResponseTypeDef = TypedDict(
    "DefineSuggesterResponseTypeDef", {"Suggester": "SuggesterStatusTypeDef"}
)

DeleteAnalysisSchemeResponseTypeDef = TypedDict(
    "DeleteAnalysisSchemeResponseTypeDef", {"AnalysisScheme": "AnalysisSchemeStatusTypeDef"}
)

DeleteDomainResponseTypeDef = TypedDict(
    "DeleteDomainResponseTypeDef", {"DomainStatus": "DomainStatusTypeDef"}, total=False
)

DeleteExpressionResponseTypeDef = TypedDict(
    "DeleteExpressionResponseTypeDef", {"Expression": "ExpressionStatusTypeDef"}
)

DeleteIndexFieldResponseTypeDef = TypedDict(
    "DeleteIndexFieldResponseTypeDef", {"IndexField": "IndexFieldStatusTypeDef"}
)

DeleteSuggesterResponseTypeDef = TypedDict(
    "DeleteSuggesterResponseTypeDef", {"Suggester": "SuggesterStatusTypeDef"}
)

DescribeAnalysisSchemesResponseTypeDef = TypedDict(
    "DescribeAnalysisSchemesResponseTypeDef",
    {"AnalysisSchemes": List["AnalysisSchemeStatusTypeDef"]},
)

DescribeAvailabilityOptionsResponseTypeDef = TypedDict(
    "DescribeAvailabilityOptionsResponseTypeDef",
    {"AvailabilityOptions": "AvailabilityOptionsStatusTypeDef"},
    total=False,
)

DescribeDomainEndpointOptionsResponseTypeDef = TypedDict(
    "DescribeDomainEndpointOptionsResponseTypeDef",
    {"DomainEndpointOptions": "DomainEndpointOptionsStatusTypeDef"},
    total=False,
)

DescribeDomainsResponseTypeDef = TypedDict(
    "DescribeDomainsResponseTypeDef", {"DomainStatusList": List["DomainStatusTypeDef"]}
)

DescribeExpressionsResponseTypeDef = TypedDict(
    "DescribeExpressionsResponseTypeDef", {"Expressions": List["ExpressionStatusTypeDef"]}
)

DescribeIndexFieldsResponseTypeDef = TypedDict(
    "DescribeIndexFieldsResponseTypeDef", {"IndexFields": List["IndexFieldStatusTypeDef"]}
)

DescribeScalingParametersResponseTypeDef = TypedDict(
    "DescribeScalingParametersResponseTypeDef",
    {"ScalingParameters": "ScalingParametersStatusTypeDef"},
)

DescribeServiceAccessPoliciesResponseTypeDef = TypedDict(
    "DescribeServiceAccessPoliciesResponseTypeDef",
    {"AccessPolicies": "AccessPoliciesStatusTypeDef"},
)

DescribeSuggestersResponseTypeDef = TypedDict(
    "DescribeSuggestersResponseTypeDef", {"Suggesters": List["SuggesterStatusTypeDef"]}
)

IndexDocumentsResponseTypeDef = TypedDict(
    "IndexDocumentsResponseTypeDef", {"FieldNames": List[str]}, total=False
)

ListDomainNamesResponseTypeDef = TypedDict(
    "ListDomainNamesResponseTypeDef", {"DomainNames": Dict[str, str]}, total=False
)

UpdateAvailabilityOptionsResponseTypeDef = TypedDict(
    "UpdateAvailabilityOptionsResponseTypeDef",
    {"AvailabilityOptions": "AvailabilityOptionsStatusTypeDef"},
    total=False,
)

UpdateDomainEndpointOptionsResponseTypeDef = TypedDict(
    "UpdateDomainEndpointOptionsResponseTypeDef",
    {"DomainEndpointOptions": "DomainEndpointOptionsStatusTypeDef"},
    total=False,
)

UpdateScalingParametersResponseTypeDef = TypedDict(
    "UpdateScalingParametersResponseTypeDef",
    {"ScalingParameters": "ScalingParametersStatusTypeDef"},
)

UpdateServiceAccessPoliciesResponseTypeDef = TypedDict(
    "UpdateServiceAccessPoliciesResponseTypeDef", {"AccessPolicies": "AccessPoliciesStatusTypeDef"}
)
