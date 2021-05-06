"""
Type annotations for cloudtrail service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cloudtrail/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cloudtrail.type_defs import AdvancedEventSelectorTypeDef

    data: AdvancedEventSelectorTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, List, Union

from mypy_boto3_cloudtrail.literals import LookupAttributeKey, ReadWriteType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AdvancedEventSelectorTypeDef",
    "AdvancedFieldSelectorTypeDef",
    "CreateTrailResponseTypeDef",
    "DataResourceTypeDef",
    "DescribeTrailsResponseTypeDef",
    "EventSelectorTypeDef",
    "EventTypeDef",
    "GetEventSelectorsResponseTypeDef",
    "GetInsightSelectorsResponseTypeDef",
    "GetTrailResponseTypeDef",
    "GetTrailStatusResponseTypeDef",
    "InsightSelectorTypeDef",
    "ListPublicKeysResponseTypeDef",
    "ListTagsResponseTypeDef",
    "ListTrailsResponseTypeDef",
    "LookupAttributeTypeDef",
    "LookupEventsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PublicKeyTypeDef",
    "PutEventSelectorsResponseTypeDef",
    "PutInsightSelectorsResponseTypeDef",
    "ResourceTagTypeDef",
    "ResourceTypeDef",
    "TagTypeDef",
    "TrailInfoTypeDef",
    "TrailTypeDef",
    "UpdateTrailResponseTypeDef",
)


class _RequiredAdvancedEventSelectorTypeDef(TypedDict):
    FieldSelectors: List["AdvancedFieldSelectorTypeDef"]


class AdvancedEventSelectorTypeDef(_RequiredAdvancedEventSelectorTypeDef, total=False):
    Name: str


class _RequiredAdvancedFieldSelectorTypeDef(TypedDict):
    Field: str


class AdvancedFieldSelectorTypeDef(_RequiredAdvancedFieldSelectorTypeDef, total=False):
    Equals: List[str]
    StartsWith: List[str]
    EndsWith: List[str]
    NotEquals: List[str]
    NotStartsWith: List[str]
    NotEndsWith: List[str]


class CreateTrailResponseTypeDef(TypedDict, total=False):
    Name: str
    S3BucketName: str
    S3KeyPrefix: str
    SnsTopicName: str
    SnsTopicARN: str
    IncludeGlobalServiceEvents: bool
    IsMultiRegionTrail: bool
    TrailARN: str
    LogFileValidationEnabled: bool
    CloudWatchLogsLogGroupArn: str
    CloudWatchLogsRoleArn: str
    KmsKeyId: str
    IsOrganizationTrail: bool


DataResourceTypeDef = TypedDict(
    "DataResourceTypeDef", {"Type": str, "Values": List[str]}, total=False
)


class DescribeTrailsResponseTypeDef(TypedDict, total=False):
    trailList: List["TrailTypeDef"]


class EventSelectorTypeDef(TypedDict, total=False):
    ReadWriteType: ReadWriteType
    IncludeManagementEvents: bool
    DataResources: List["DataResourceTypeDef"]
    ExcludeManagementEventSources: List[str]


class EventTypeDef(TypedDict, total=False):
    EventId: str
    EventName: str
    ReadOnly: str
    AccessKeyId: str
    EventTime: datetime
    EventSource: str
    Username: str
    Resources: List["ResourceTypeDef"]
    CloudTrailEvent: str


class GetEventSelectorsResponseTypeDef(TypedDict, total=False):
    TrailARN: str
    EventSelectors: List["EventSelectorTypeDef"]
    AdvancedEventSelectors: List["AdvancedEventSelectorTypeDef"]


class GetInsightSelectorsResponseTypeDef(TypedDict, total=False):
    TrailARN: str
    InsightSelectors: List["InsightSelectorTypeDef"]


class GetTrailResponseTypeDef(TypedDict, total=False):
    Trail: "TrailTypeDef"


class GetTrailStatusResponseTypeDef(TypedDict, total=False):
    IsLogging: bool
    LatestDeliveryError: str
    LatestNotificationError: str
    LatestDeliveryTime: datetime
    LatestNotificationTime: datetime
    StartLoggingTime: datetime
    StopLoggingTime: datetime
    LatestCloudWatchLogsDeliveryError: str
    LatestCloudWatchLogsDeliveryTime: datetime
    LatestDigestDeliveryTime: datetime
    LatestDigestDeliveryError: str
    LatestDeliveryAttemptTime: str
    LatestNotificationAttemptTime: str
    LatestNotificationAttemptSucceeded: str
    LatestDeliveryAttemptSucceeded: str
    TimeLoggingStarted: str
    TimeLoggingStopped: str


class InsightSelectorTypeDef(TypedDict, total=False):
    InsightType: Literal["ApiCallRateInsight"]


class ListPublicKeysResponseTypeDef(TypedDict, total=False):
    PublicKeyList: List["PublicKeyTypeDef"]
    NextToken: str


class ListTagsResponseTypeDef(TypedDict, total=False):
    ResourceTagList: List["ResourceTagTypeDef"]
    NextToken: str


class ListTrailsResponseTypeDef(TypedDict, total=False):
    Trails: List["TrailInfoTypeDef"]
    NextToken: str


class LookupAttributeTypeDef(TypedDict):
    AttributeKey: LookupAttributeKey
    AttributeValue: str


class LookupEventsResponseTypeDef(TypedDict, total=False):
    Events: List["EventTypeDef"]
    NextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PublicKeyTypeDef(TypedDict, total=False):
    Value: Union[bytes, IO[bytes]]
    ValidityStartTime: datetime
    ValidityEndTime: datetime
    Fingerprint: str


class PutEventSelectorsResponseTypeDef(TypedDict, total=False):
    TrailARN: str
    EventSelectors: List["EventSelectorTypeDef"]
    AdvancedEventSelectors: List["AdvancedEventSelectorTypeDef"]


class PutInsightSelectorsResponseTypeDef(TypedDict, total=False):
    TrailARN: str
    InsightSelectors: List["InsightSelectorTypeDef"]


class ResourceTagTypeDef(TypedDict, total=False):
    ResourceId: str
    TagsList: List["TagTypeDef"]


class ResourceTypeDef(TypedDict, total=False):
    ResourceType: str
    ResourceName: str


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    Value: str


class TrailInfoTypeDef(TypedDict, total=False):
    TrailARN: str
    Name: str
    HomeRegion: str


class TrailTypeDef(TypedDict, total=False):
    Name: str
    S3BucketName: str
    S3KeyPrefix: str
    SnsTopicName: str
    SnsTopicARN: str
    IncludeGlobalServiceEvents: bool
    IsMultiRegionTrail: bool
    HomeRegion: str
    TrailARN: str
    LogFileValidationEnabled: bool
    CloudWatchLogsLogGroupArn: str
    CloudWatchLogsRoleArn: str
    KmsKeyId: str
    HasCustomEventSelectors: bool
    HasInsightSelectors: bool
    IsOrganizationTrail: bool


class UpdateTrailResponseTypeDef(TypedDict, total=False):
    Name: str
    S3BucketName: str
    S3KeyPrefix: str
    SnsTopicName: str
    SnsTopicARN: str
    IncludeGlobalServiceEvents: bool
    IsMultiRegionTrail: bool
    TrailARN: str
    LogFileValidationEnabled: bool
    CloudWatchLogsLogGroupArn: str
    CloudWatchLogsRoleArn: str
    KmsKeyId: str
    IsOrganizationTrail: bool
