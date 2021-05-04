"""
Type annotations for cloudsearchdomain service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudsearchdomain/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudsearchdomain.type_defs import BucketInfoTypeDef

    data: BucketInfoTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BucketInfoTypeDef",
    "BucketTypeDef",
    "DocumentServiceWarningTypeDef",
    "FieldStatsTypeDef",
    "HitTypeDef",
    "HitsTypeDef",
    "SearchResponseTypeDef",
    "SearchStatusTypeDef",
    "SuggestModelTypeDef",
    "SuggestResponseTypeDef",
    "SuggestStatusTypeDef",
    "SuggestionMatchTypeDef",
    "UploadDocumentsResponseTypeDef",
)


class BucketInfoTypeDef(TypedDict, total=False):
    buckets: List["BucketTypeDef"]


class BucketTypeDef(TypedDict, total=False):
    value: str
    count: int


class DocumentServiceWarningTypeDef(TypedDict, total=False):
    message: str


FieldStatsTypeDef = TypedDict(
    "FieldStatsTypeDef",
    {
        "min": str,
        "max": str,
        "count": int,
        "missing": int,
        "sum": float,
        "sumOfSquares": float,
        "mean": str,
        "stddev": float,
    },
    total=False,
)

HitTypeDef = TypedDict(
    "HitTypeDef",
    {
        "id": str,
        "fields": Dict[str, List[str]],
        "exprs": Dict[str, str],
        "highlights": Dict[str, str],
    },
    total=False,
)


class HitsTypeDef(TypedDict, total=False):
    found: int
    start: int
    cursor: str
    hit: List["HitTypeDef"]


class SearchResponseTypeDef(TypedDict, total=False):
    status: "SearchStatusTypeDef"
    hits: "HitsTypeDef"
    facets: Dict[str, "BucketInfoTypeDef"]
    stats: Dict[str, "FieldStatsTypeDef"]


class SearchStatusTypeDef(TypedDict, total=False):
    timems: int
    rid: str


class SuggestModelTypeDef(TypedDict, total=False):
    query: str
    found: int
    suggestions: List["SuggestionMatchTypeDef"]


class SuggestResponseTypeDef(TypedDict, total=False):
    status: "SuggestStatusTypeDef"
    suggest: "SuggestModelTypeDef"


class SuggestStatusTypeDef(TypedDict, total=False):
    timems: int
    rid: str


SuggestionMatchTypeDef = TypedDict(
    "SuggestionMatchTypeDef", {"suggestion": str, "score": int, "id": str}, total=False
)


class UploadDocumentsResponseTypeDef(TypedDict, total=False):
    status: str
    adds: int
    deletes: int
    warnings: List["DocumentServiceWarningTypeDef"]
