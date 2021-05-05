"""
Type annotations for kinesis service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesis/literals.html)

Usage::

    ```python
    from mypy_boto3_kinesis.literals import ConsumerStatus

    data: ConsumerStatus = "ACTIVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ConsumerStatus",
    "DescribeStreamPaginatorName",
    "EncryptionType",
    "ListShardsPaginatorName",
    "ListStreamConsumersPaginatorName",
    "ListStreamsPaginatorName",
    "MetricsName",
    "ScalingType",
    "ShardFilterType",
    "ShardIteratorType",
    "StreamExistsWaiterName",
    "StreamNotExistsWaiterName",
    "StreamStatus",
)


ConsumerStatus = Literal["ACTIVE", "CREATING", "DELETING"]
DescribeStreamPaginatorName = Literal["describe_stream"]
EncryptionType = Literal["KMS", "NONE"]
ListShardsPaginatorName = Literal["list_shards"]
ListStreamConsumersPaginatorName = Literal["list_stream_consumers"]
ListStreamsPaginatorName = Literal["list_streams"]
MetricsName = Literal[
    "ALL",
    "IncomingBytes",
    "IncomingRecords",
    "IteratorAgeMilliseconds",
    "OutgoingBytes",
    "OutgoingRecords",
    "ReadProvisionedThroughputExceeded",
    "WriteProvisionedThroughputExceeded",
]
ScalingType = Literal["UNIFORM_SCALING"]
ShardFilterType = Literal[
    "AFTER_SHARD_ID",
    "AT_LATEST",
    "AT_TIMESTAMP",
    "AT_TRIM_HORIZON",
    "FROM_TIMESTAMP",
    "FROM_TRIM_HORIZON",
]
ShardIteratorType = Literal[
    "AFTER_SEQUENCE_NUMBER", "AT_SEQUENCE_NUMBER", "AT_TIMESTAMP", "LATEST", "TRIM_HORIZON"
]
StreamExistsWaiterName = Literal["stream_exists"]
StreamNotExistsWaiterName = Literal["stream_not_exists"]
StreamStatus = Literal["ACTIVE", "CREATING", "DELETING", "UPDATING"]
