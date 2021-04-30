"""
Main interface for qldb service type definitions.

Usage::

    ```python
    from mypy_boto3_qldb.type_defs import JournalKinesisStreamDescriptionTypeDef

    data: JournalKinesisStreamDescriptionTypeDef = {...}
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
    "JournalKinesisStreamDescriptionTypeDef",
    "JournalS3ExportDescriptionTypeDef",
    "KinesisConfigurationTypeDef",
    "LedgerSummaryTypeDef",
    "S3EncryptionConfigurationTypeDef",
    "S3ExportConfigurationTypeDef",
    "ValueHolderTypeDef",
    "CancelJournalKinesisStreamResponseTypeDef",
    "CreateLedgerResponseTypeDef",
    "DescribeJournalKinesisStreamResponseTypeDef",
    "DescribeJournalS3ExportResponseTypeDef",
    "DescribeLedgerResponseTypeDef",
    "ExportJournalToS3ResponseTypeDef",
    "GetBlockResponseTypeDef",
    "GetDigestResponseTypeDef",
    "GetRevisionResponseTypeDef",
    "ListJournalKinesisStreamsForLedgerResponseTypeDef",
    "ListJournalS3ExportsForLedgerResponseTypeDef",
    "ListJournalS3ExportsResponseTypeDef",
    "ListLedgersResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StreamJournalToKinesisResponseTypeDef",
    "UpdateLedgerResponseTypeDef",
)

_RequiredJournalKinesisStreamDescriptionTypeDef = TypedDict(
    "_RequiredJournalKinesisStreamDescriptionTypeDef",
    {
        "LedgerName": str,
        "RoleArn": str,
        "StreamId": str,
        "Status": StreamStatus,
        "KinesisConfiguration": "KinesisConfigurationTypeDef",
        "StreamName": str,
    },
)
_OptionalJournalKinesisStreamDescriptionTypeDef = TypedDict(
    "_OptionalJournalKinesisStreamDescriptionTypeDef",
    {
        "CreationTime": datetime,
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "Arn": str,
        "ErrorCause": ErrorCause,
    },
    total=False,
)


class JournalKinesisStreamDescriptionTypeDef(
    _RequiredJournalKinesisStreamDescriptionTypeDef, _OptionalJournalKinesisStreamDescriptionTypeDef
):
    pass


JournalS3ExportDescriptionTypeDef = TypedDict(
    "JournalS3ExportDescriptionTypeDef",
    {
        "LedgerName": str,
        "ExportId": str,
        "ExportCreationTime": datetime,
        "Status": ExportStatus,
        "InclusiveStartTime": datetime,
        "ExclusiveEndTime": datetime,
        "S3ExportConfiguration": "S3ExportConfigurationTypeDef",
        "RoleArn": str,
    },
)

_RequiredKinesisConfigurationTypeDef = TypedDict(
    "_RequiredKinesisConfigurationTypeDef", {"StreamArn": str}
)
_OptionalKinesisConfigurationTypeDef = TypedDict(
    "_OptionalKinesisConfigurationTypeDef", {"AggregationEnabled": bool}, total=False
)


class KinesisConfigurationTypeDef(
    _RequiredKinesisConfigurationTypeDef, _OptionalKinesisConfigurationTypeDef
):
    pass


LedgerSummaryTypeDef = TypedDict(
    "LedgerSummaryTypeDef",
    {"Name": str, "State": LedgerState, "CreationDateTime": datetime},
    total=False,
)

_RequiredS3EncryptionConfigurationTypeDef = TypedDict(
    "_RequiredS3EncryptionConfigurationTypeDef", {"ObjectEncryptionType": S3ObjectEncryptionType}
)
_OptionalS3EncryptionConfigurationTypeDef = TypedDict(
    "_OptionalS3EncryptionConfigurationTypeDef", {"KmsKeyArn": str}, total=False
)


class S3EncryptionConfigurationTypeDef(
    _RequiredS3EncryptionConfigurationTypeDef, _OptionalS3EncryptionConfigurationTypeDef
):
    pass


S3ExportConfigurationTypeDef = TypedDict(
    "S3ExportConfigurationTypeDef",
    {"Bucket": str, "Prefix": str, "EncryptionConfiguration": "S3EncryptionConfigurationTypeDef"},
)

ValueHolderTypeDef = TypedDict("ValueHolderTypeDef", {"IonText": str}, total=False)

CancelJournalKinesisStreamResponseTypeDef = TypedDict(
    "CancelJournalKinesisStreamResponseTypeDef", {"StreamId": str}, total=False
)

CreateLedgerResponseTypeDef = TypedDict(
    "CreateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerState,
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
    },
    total=False,
)

DescribeJournalKinesisStreamResponseTypeDef = TypedDict(
    "DescribeJournalKinesisStreamResponseTypeDef",
    {"Stream": "JournalKinesisStreamDescriptionTypeDef"},
    total=False,
)

DescribeJournalS3ExportResponseTypeDef = TypedDict(
    "DescribeJournalS3ExportResponseTypeDef",
    {"ExportDescription": "JournalS3ExportDescriptionTypeDef"},
)

DescribeLedgerResponseTypeDef = TypedDict(
    "DescribeLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerState,
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
    },
    total=False,
)

ExportJournalToS3ResponseTypeDef = TypedDict("ExportJournalToS3ResponseTypeDef", {"ExportId": str})

_RequiredGetBlockResponseTypeDef = TypedDict(
    "_RequiredGetBlockResponseTypeDef", {"Block": "ValueHolderTypeDef"}
)
_OptionalGetBlockResponseTypeDef = TypedDict(
    "_OptionalGetBlockResponseTypeDef", {"Proof": "ValueHolderTypeDef"}, total=False
)


class GetBlockResponseTypeDef(_RequiredGetBlockResponseTypeDef, _OptionalGetBlockResponseTypeDef):
    pass


GetDigestResponseTypeDef = TypedDict(
    "GetDigestResponseTypeDef",
    {"Digest": Union[bytes, IO[bytes]], "DigestTipAddress": "ValueHolderTypeDef"},
)

_RequiredGetRevisionResponseTypeDef = TypedDict(
    "_RequiredGetRevisionResponseTypeDef", {"Revision": "ValueHolderTypeDef"}
)
_OptionalGetRevisionResponseTypeDef = TypedDict(
    "_OptionalGetRevisionResponseTypeDef", {"Proof": "ValueHolderTypeDef"}, total=False
)


class GetRevisionResponseTypeDef(
    _RequiredGetRevisionResponseTypeDef, _OptionalGetRevisionResponseTypeDef
):
    pass


ListJournalKinesisStreamsForLedgerResponseTypeDef = TypedDict(
    "ListJournalKinesisStreamsForLedgerResponseTypeDef",
    {"Streams": List["JournalKinesisStreamDescriptionTypeDef"], "NextToken": str},
    total=False,
)

ListJournalS3ExportsForLedgerResponseTypeDef = TypedDict(
    "ListJournalS3ExportsForLedgerResponseTypeDef",
    {"JournalS3Exports": List["JournalS3ExportDescriptionTypeDef"], "NextToken": str},
    total=False,
)

ListJournalS3ExportsResponseTypeDef = TypedDict(
    "ListJournalS3ExportsResponseTypeDef",
    {"JournalS3Exports": List["JournalS3ExportDescriptionTypeDef"], "NextToken": str},
    total=False,
)

ListLedgersResponseTypeDef = TypedDict(
    "ListLedgersResponseTypeDef",
    {"Ledgers": List["LedgerSummaryTypeDef"], "NextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"Tags": Dict[str, str]}, total=False
)

StreamJournalToKinesisResponseTypeDef = TypedDict(
    "StreamJournalToKinesisResponseTypeDef", {"StreamId": str}, total=False
)

UpdateLedgerResponseTypeDef = TypedDict(
    "UpdateLedgerResponseTypeDef",
    {
        "Name": str,
        "Arn": str,
        "State": LedgerState,
        "CreationDateTime": datetime,
        "DeletionProtection": bool,
    },
    total=False,
)
