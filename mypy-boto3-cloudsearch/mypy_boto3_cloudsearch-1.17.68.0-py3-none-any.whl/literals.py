"""
Type annotations for cloudsearch service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearch/literals.html)

Usage::

    ```python
    from mypy_boto3_cloudsearch.literals import AlgorithmicStemming

    data: AlgorithmicStemming = "full"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AlgorithmicStemming",
    "AnalysisSchemeLanguage",
    "IndexFieldType",
    "OptionState",
    "PartitionInstanceType",
    "SuggesterFuzzyMatching",
    "TLSSecurityPolicy",
)


AlgorithmicStemming = Literal["full", "light", "minimal", "none"]
AnalysisSchemeLanguage = Literal[
    "ar",
    "bg",
    "ca",
    "cs",
    "da",
    "de",
    "el",
    "en",
    "es",
    "eu",
    "fa",
    "fi",
    "fr",
    "ga",
    "gl",
    "he",
    "hi",
    "hu",
    "hy",
    "id",
    "it",
    "ja",
    "ko",
    "lv",
    "mul",
    "nl",
    "no",
    "pt",
    "ro",
    "ru",
    "sv",
    "th",
    "tr",
    "zh-Hans",
    "zh-Hant",
]
IndexFieldType = Literal[
    "date",
    "date-array",
    "double",
    "double-array",
    "int",
    "int-array",
    "latlon",
    "literal",
    "literal-array",
    "text",
    "text-array",
]
OptionState = Literal["Active", "FailedToValidate", "Processing", "RequiresIndexDocuments"]
PartitionInstanceType = Literal[
    "search.2xlarge",
    "search.large",
    "search.m1.large",
    "search.m1.small",
    "search.m2.2xlarge",
    "search.m2.xlarge",
    "search.m3.2xlarge",
    "search.m3.large",
    "search.m3.medium",
    "search.m3.xlarge",
    "search.medium",
    "search.small",
    "search.xlarge",
]
SuggesterFuzzyMatching = Literal["high", "low", "none"]
TLSSecurityPolicy = Literal["Policy-Min-TLS-1-0-2019-07", "Policy-Min-TLS-1-2-2019-07"]
