"""
Type annotations for qldb service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb/type_defs.html)

Usage::

    ```python
    from mypy_boto3_qldb.type_defs import CancelJournalKinesisStreamResponseTypeDef

    data: CancelJournalKinesisStreamResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_qldb.literals import (
    ErrorCause,
    ExportStatus,
    LedgerState,
    S3ObjectEncryptionType,
    StreamStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelJournalKinesisStreamResponseTypeDef",
    "CreateLedgerResponseTypeDef",
    "DescribeJournalKinesisStreamResponseTypeDef",
    "DescribeJournalS3ExportResponseTypeDef",
    "DescribeLedgerResponseTypeDef",
    "ExportJournalToS3ResponseTypeDef",
    "GetBlockResponseTypeDef",
    "GetDigestResponseTypeDef",
    "GetRevisionResponseTypeDef",
    "JournalKinesisStreamDescriptionTypeDef",
    "JournalS3ExportDescriptionTypeDef",
    "KinesisConfigurationTypeDef",
    "LedgerSummaryTypeDef",
    "ListJournalKinesisStreamsForLedgerResponseTypeDef",
    "ListJournalS3ExportsForLedgerResponseTypeDef",
    "ListJournalS3ExportsResponseTypeDef",
    "ListLedgersResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "S3EncryptionConfigurationTypeDef",
    "S3ExportConfigurationTypeDef",
    "StreamJournalToKinesisResponseTypeDef",
    "UpdateLedgerResponseTypeDef",
    "ValueHolderTypeDef",
)


class CancelJournalKinesisStreamResponseTypeDef(TypedDict, total=False):
    StreamId: str


class CreateLedgerResponseTypeDef(TypedDict, total=False):
    Name: str
    Arn: str
    State: LedgerState
    CreationDateTime: datetime
    DeletionProtection: bool


class DescribeJournalKinesisStreamResponseTypeDef(TypedDict, total=False):
    Stream: "JournalKinesisStreamDescriptionTypeDef"


class DescribeJournalS3ExportResponseTypeDef(TypedDict):
    ExportDescription: "JournalS3ExportDescriptionTypeDef"


class DescribeLedgerResponseTypeDef(TypedDict, total=False):
    Name: str
    Arn: str
    State: LedgerState
    CreationDateTime: datetime
    DeletionProtection: bool


class ExportJournalToS3ResponseTypeDef(TypedDict):
    ExportId: str


class _RequiredGetBlockResponseTypeDef(TypedDict):
    Block: "ValueHolderTypeDef"


class GetBlockResponseTypeDef(_RequiredGetBlockResponseTypeDef, total=False):
    Proof: "ValueHolderTypeDef"


class GetDigestResponseTypeDef(TypedDict):
    Digest: Union[bytes, IO[bytes]]
    DigestTipAddress: "ValueHolderTypeDef"


class _RequiredGetRevisionResponseTypeDef(TypedDict):
    Revision: "ValueHolderTypeDef"


class GetRevisionResponseTypeDef(_RequiredGetRevisionResponseTypeDef, total=False):
    Proof: "ValueHolderTypeDef"


class _RequiredJournalKinesisStreamDescriptionTypeDef(TypedDict):
    LedgerName: str
    RoleArn: str
    StreamId: str
    Status: StreamStatus
    KinesisConfiguration: "KinesisConfigurationTypeDef"
    StreamName: str


class JournalKinesisStreamDescriptionTypeDef(
    _RequiredJournalKinesisStreamDescriptionTypeDef, total=False
):
    CreationTime: datetime
    InclusiveStartTime: datetime
    ExclusiveEndTime: datetime
    Arn: str
    ErrorCause: ErrorCause


class JournalS3ExportDescriptionTypeDef(TypedDict):
    LedgerName: str
    ExportId: str
    ExportCreationTime: datetime
    Status: ExportStatus
    InclusiveStartTime: datetime
    ExclusiveEndTime: datetime
    S3ExportConfiguration: "S3ExportConfigurationTypeDef"
    RoleArn: str


class _RequiredKinesisConfigurationTypeDef(TypedDict):
    StreamArn: str


class KinesisConfigurationTypeDef(_RequiredKinesisConfigurationTypeDef, total=False):
    AggregationEnabled: bool


class LedgerSummaryTypeDef(TypedDict, total=False):
    Name: str
    State: LedgerState
    CreationDateTime: datetime


class ListJournalKinesisStreamsForLedgerResponseTypeDef(TypedDict, total=False):
    Streams: List["JournalKinesisStreamDescriptionTypeDef"]
    NextToken: str


class ListJournalS3ExportsForLedgerResponseTypeDef(TypedDict, total=False):
    JournalS3Exports: List["JournalS3ExportDescriptionTypeDef"]
    NextToken: str


class ListJournalS3ExportsResponseTypeDef(TypedDict, total=False):
    JournalS3Exports: List["JournalS3ExportDescriptionTypeDef"]
    NextToken: str


class ListLedgersResponseTypeDef(TypedDict, total=False):
    Ledgers: List["LedgerSummaryTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class _RequiredS3EncryptionConfigurationTypeDef(TypedDict):
    ObjectEncryptionType: S3ObjectEncryptionType


class S3EncryptionConfigurationTypeDef(_RequiredS3EncryptionConfigurationTypeDef, total=False):
    KmsKeyArn: str


class S3ExportConfigurationTypeDef(TypedDict):
    Bucket: str
    Prefix: str
    EncryptionConfiguration: "S3EncryptionConfigurationTypeDef"


class StreamJournalToKinesisResponseTypeDef(TypedDict, total=False):
    StreamId: str


class UpdateLedgerResponseTypeDef(TypedDict, total=False):
    Name: str
    Arn: str
    State: LedgerState
    CreationDateTime: datetime
    DeletionProtection: bool


class ValueHolderTypeDef(TypedDict, total=False):
    IonText: str
