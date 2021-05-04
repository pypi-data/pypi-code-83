"""
Type annotations for sns service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sns/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sns.type_defs import CheckIfPhoneNumberIsOptedOutResponseTypeDef

    data: CheckIfPhoneNumberIsOptedOutResponseTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, List, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CheckIfPhoneNumberIsOptedOutResponseTypeDef",
    "ConfirmSubscriptionResponseTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreatePlatformApplicationResponseTypeDef",
    "CreateTopicResponseTypeDef",
    "EndpointTypeDef",
    "GetEndpointAttributesResponseTypeDef",
    "GetPlatformApplicationAttributesResponseTypeDef",
    "GetSMSAttributesResponseTypeDef",
    "GetSubscriptionAttributesResponseTypeDef",
    "GetTopicAttributesResponseTypeDef",
    "ListEndpointsByPlatformApplicationResponseTypeDef",
    "ListPhoneNumbersOptedOutResponseTypeDef",
    "ListPlatformApplicationsResponseTypeDef",
    "ListSubscriptionsByTopicResponseTypeDef",
    "ListSubscriptionsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTopicsResponseTypeDef",
    "MessageAttributeValueTypeDef",
    "PaginatorConfigTypeDef",
    "PlatformApplicationTypeDef",
    "PublishResponseTypeDef",
    "SubscribeResponseTypeDef",
    "SubscriptionTypeDef",
    "TagTypeDef",
    "TopicTypeDef",
)


class CheckIfPhoneNumberIsOptedOutResponseTypeDef(TypedDict, total=False):
    isOptedOut: bool


class ConfirmSubscriptionResponseTypeDef(TypedDict, total=False):
    SubscriptionArn: str


class CreateEndpointResponseTypeDef(TypedDict, total=False):
    EndpointArn: str


class CreatePlatformApplicationResponseTypeDef(TypedDict, total=False):
    PlatformApplicationArn: str


class CreateTopicResponseTypeDef(TypedDict, total=False):
    TopicArn: str


class EndpointTypeDef(TypedDict, total=False):
    EndpointArn: str
    Attributes: Dict[str, str]


class GetEndpointAttributesResponseTypeDef(TypedDict, total=False):
    Attributes: Dict[str, str]


class GetPlatformApplicationAttributesResponseTypeDef(TypedDict, total=False):
    Attributes: Dict[str, str]


class GetSMSAttributesResponseTypeDef(TypedDict, total=False):
    attributes: Dict[str, str]


class GetSubscriptionAttributesResponseTypeDef(TypedDict, total=False):
    Attributes: Dict[str, str]


class GetTopicAttributesResponseTypeDef(TypedDict, total=False):
    Attributes: Dict[str, str]


class ListEndpointsByPlatformApplicationResponseTypeDef(TypedDict, total=False):
    Endpoints: List["EndpointTypeDef"]
    NextToken: str


class ListPhoneNumbersOptedOutResponseTypeDef(TypedDict, total=False):
    phoneNumbers: List[str]
    nextToken: str


class ListPlatformApplicationsResponseTypeDef(TypedDict, total=False):
    PlatformApplications: List["PlatformApplicationTypeDef"]
    NextToken: str


class ListSubscriptionsByTopicResponseTypeDef(TypedDict, total=False):
    Subscriptions: List["SubscriptionTypeDef"]
    NextToken: str


class ListSubscriptionsResponseTypeDef(TypedDict, total=False):
    Subscriptions: List["SubscriptionTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class ListTopicsResponseTypeDef(TypedDict, total=False):
    Topics: List["TopicTypeDef"]
    NextToken: str


class _RequiredMessageAttributeValueTypeDef(TypedDict):
    DataType: str


class MessageAttributeValueTypeDef(_RequiredMessageAttributeValueTypeDef, total=False):
    StringValue: str
    BinaryValue: Union[bytes, IO[bytes]]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PlatformApplicationTypeDef(TypedDict, total=False):
    PlatformApplicationArn: str
    Attributes: Dict[str, str]


class PublishResponseTypeDef(TypedDict, total=False):
    MessageId: str
    SequenceNumber: str


class SubscribeResponseTypeDef(TypedDict, total=False):
    SubscriptionArn: str


SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {"SubscriptionArn": str, "Owner": str, "Protocol": str, "Endpoint": str, "TopicArn": str},
    total=False,
)


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TopicTypeDef(TypedDict, total=False):
    TopicArn: str
