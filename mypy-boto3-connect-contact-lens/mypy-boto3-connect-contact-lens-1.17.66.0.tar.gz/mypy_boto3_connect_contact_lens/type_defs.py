"""
Type annotations for connect-contact-lens service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect_contact_lens/type_defs.html)

Usage::

    ```python
    from mypy_boto3_connect_contact_lens.type_defs import CategoriesTypeDef

    data: CategoriesTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_connect_contact_lens.literals import SentimentValue

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CategoriesTypeDef",
    "CategoryDetailsTypeDef",
    "CharacterOffsetsTypeDef",
    "IssueDetectedTypeDef",
    "ListRealtimeContactAnalysisSegmentsResponseTypeDef",
    "PointOfInterestTypeDef",
    "RealtimeContactAnalysisSegmentTypeDef",
    "TranscriptTypeDef",
)


class CategoriesTypeDef(TypedDict):
    MatchedCategories: List[str]
    MatchedDetails: Dict[str, "CategoryDetailsTypeDef"]


class CategoryDetailsTypeDef(TypedDict):
    PointsOfInterest: List["PointOfInterestTypeDef"]


class CharacterOffsetsTypeDef(TypedDict):
    BeginOffsetChar: int
    EndOffsetChar: int


class IssueDetectedTypeDef(TypedDict):
    CharacterOffsets: "CharacterOffsetsTypeDef"


class _RequiredListRealtimeContactAnalysisSegmentsResponseTypeDef(TypedDict):
    Segments: List["RealtimeContactAnalysisSegmentTypeDef"]


class ListRealtimeContactAnalysisSegmentsResponseTypeDef(
    _RequiredListRealtimeContactAnalysisSegmentsResponseTypeDef, total=False
):
    NextToken: str


class PointOfInterestTypeDef(TypedDict):
    BeginOffsetMillis: int
    EndOffsetMillis: int


class RealtimeContactAnalysisSegmentTypeDef(TypedDict, total=False):
    Transcript: "TranscriptTypeDef"
    Categories: "CategoriesTypeDef"


class _RequiredTranscriptTypeDef(TypedDict):
    Id: str
    ParticipantId: str
    ParticipantRole: str
    Content: str
    BeginOffsetMillis: int
    EndOffsetMillis: int
    Sentiment: SentimentValue


class TranscriptTypeDef(_RequiredTranscriptTypeDef, total=False):
    IssuesDetected: List["IssueDetectedTypeDef"]
