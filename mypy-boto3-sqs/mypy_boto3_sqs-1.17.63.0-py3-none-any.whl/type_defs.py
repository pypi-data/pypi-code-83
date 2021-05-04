"""
Type annotations for sqs service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sqs/type_defs.html)

Usage::

    ```python
    from mypy_boto3_sqs.type_defs import BatchResultErrorEntryTypeDef

    data: BatchResultErrorEntryTypeDef = {...}
    ```
"""
import sys
from typing import IO, Dict, List, Union

from mypy_boto3_sqs.literals import MessageSystemAttributeName, QueueAttributeName

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchResultErrorEntryTypeDef",
    "ChangeMessageVisibilityBatchRequestEntryTypeDef",
    "ChangeMessageVisibilityBatchResultEntryTypeDef",
    "ChangeMessageVisibilityBatchResultTypeDef",
    "CreateQueueResultTypeDef",
    "DeleteMessageBatchRequestEntryTypeDef",
    "DeleteMessageBatchResultEntryTypeDef",
    "DeleteMessageBatchResultTypeDef",
    "GetQueueAttributesResultTypeDef",
    "GetQueueUrlResultTypeDef",
    "ListDeadLetterSourceQueuesResultTypeDef",
    "ListQueueTagsResultTypeDef",
    "ListQueuesResultTypeDef",
    "MessageAttributeValueTypeDef",
    "MessageSystemAttributeValueTypeDef",
    "MessageTypeDef",
    "PaginatorConfigTypeDef",
    "ReceiveMessageResultTypeDef",
    "SendMessageBatchRequestEntryTypeDef",
    "SendMessageBatchResultEntryTypeDef",
    "SendMessageBatchResultTypeDef",
    "SendMessageResultTypeDef",
)


class _RequiredBatchResultErrorEntryTypeDef(TypedDict):
    Id: str
    SenderFault: bool
    Code: str


class BatchResultErrorEntryTypeDef(_RequiredBatchResultErrorEntryTypeDef, total=False):
    Message: str


class _RequiredChangeMessageVisibilityBatchRequestEntryTypeDef(TypedDict):
    Id: str
    ReceiptHandle: str


class ChangeMessageVisibilityBatchRequestEntryTypeDef(
    _RequiredChangeMessageVisibilityBatchRequestEntryTypeDef, total=False
):
    VisibilityTimeout: int


class ChangeMessageVisibilityBatchResultEntryTypeDef(TypedDict):
    Id: str


class ChangeMessageVisibilityBatchResultTypeDef(TypedDict):
    Successful: List["ChangeMessageVisibilityBatchResultEntryTypeDef"]
    Failed: List["BatchResultErrorEntryTypeDef"]


class CreateQueueResultTypeDef(TypedDict, total=False):
    QueueUrl: str


class DeleteMessageBatchRequestEntryTypeDef(TypedDict):
    Id: str
    ReceiptHandle: str


class DeleteMessageBatchResultEntryTypeDef(TypedDict):
    Id: str


class DeleteMessageBatchResultTypeDef(TypedDict):
    Successful: List["DeleteMessageBatchResultEntryTypeDef"]
    Failed: List["BatchResultErrorEntryTypeDef"]


class GetQueueAttributesResultTypeDef(TypedDict, total=False):
    Attributes: Dict[QueueAttributeName, str]


class GetQueueUrlResultTypeDef(TypedDict, total=False):
    QueueUrl: str


class _RequiredListDeadLetterSourceQueuesResultTypeDef(TypedDict):
    queueUrls: List[str]


class ListDeadLetterSourceQueuesResultTypeDef(
    _RequiredListDeadLetterSourceQueuesResultTypeDef, total=False
):
    NextToken: str


class ListQueueTagsResultTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class ListQueuesResultTypeDef(TypedDict, total=False):
    QueueUrls: List[str]
    NextToken: str


class _RequiredMessageAttributeValueTypeDef(TypedDict):
    DataType: str


class MessageAttributeValueTypeDef(_RequiredMessageAttributeValueTypeDef, total=False):
    StringValue: str
    BinaryValue: Union[bytes, IO[bytes]]
    StringListValues: List[str]
    BinaryListValues: List[Union[bytes, IO[bytes]]]


class _RequiredMessageSystemAttributeValueTypeDef(TypedDict):
    DataType: str


class MessageSystemAttributeValueTypeDef(_RequiredMessageSystemAttributeValueTypeDef, total=False):
    StringValue: str
    BinaryValue: Union[bytes, IO[bytes]]
    StringListValues: List[str]
    BinaryListValues: List[Union[bytes, IO[bytes]]]


class MessageTypeDef(TypedDict, total=False):
    MessageId: str
    ReceiptHandle: str
    MD5OfBody: str
    Body: str
    Attributes: Dict[MessageSystemAttributeName, str]
    MD5OfMessageAttributes: str
    MessageAttributes: Dict[str, "MessageAttributeValueTypeDef"]


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ReceiveMessageResultTypeDef(TypedDict, total=False):
    Messages: List["MessageTypeDef"]


class _RequiredSendMessageBatchRequestEntryTypeDef(TypedDict):
    Id: str
    MessageBody: str


class SendMessageBatchRequestEntryTypeDef(
    _RequiredSendMessageBatchRequestEntryTypeDef, total=False
):
    DelaySeconds: int
    MessageAttributes: Dict[str, "MessageAttributeValueTypeDef"]
    MessageSystemAttributes: Dict[Literal["AWSTraceHeader"], "MessageSystemAttributeValueTypeDef"]
    MessageDeduplicationId: str
    MessageGroupId: str


class _RequiredSendMessageBatchResultEntryTypeDef(TypedDict):
    Id: str
    MessageId: str
    MD5OfMessageBody: str


class SendMessageBatchResultEntryTypeDef(_RequiredSendMessageBatchResultEntryTypeDef, total=False):
    MD5OfMessageAttributes: str
    MD5OfMessageSystemAttributes: str
    SequenceNumber: str


class SendMessageBatchResultTypeDef(TypedDict):
    Successful: List["SendMessageBatchResultEntryTypeDef"]
    Failed: List["BatchResultErrorEntryTypeDef"]


class SendMessageResultTypeDef(TypedDict, total=False):
    MD5OfMessageBody: str
    MD5OfMessageAttributes: str
    MD5OfMessageSystemAttributes: str
    MessageId: str
    SequenceNumber: str
