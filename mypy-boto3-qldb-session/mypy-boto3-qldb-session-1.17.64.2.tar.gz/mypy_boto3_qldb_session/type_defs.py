"""
Type annotations for qldb-session service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_qldb_session/type_defs.html)

Usage::

    ```python
    from mypy_boto3_qldb_session.type_defs import AbortTransactionResultTypeDef

    data: AbortTransactionResultTypeDef = {...}
    ```
"""
import sys
from typing import IO, List, Union

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AbortTransactionResultTypeDef",
    "CommitTransactionRequestTypeDef",
    "CommitTransactionResultTypeDef",
    "EndSessionResultTypeDef",
    "ExecuteStatementRequestTypeDef",
    "ExecuteStatementResultTypeDef",
    "FetchPageRequestTypeDef",
    "FetchPageResultTypeDef",
    "IOUsageTypeDef",
    "PageTypeDef",
    "SendCommandResultTypeDef",
    "StartSessionRequestTypeDef",
    "StartSessionResultTypeDef",
    "StartTransactionResultTypeDef",
    "TimingInformationTypeDef",
    "ValueHolderTypeDef",
)


class AbortTransactionResultTypeDef(TypedDict, total=False):
    TimingInformation: "TimingInformationTypeDef"


class CommitTransactionRequestTypeDef(TypedDict):
    TransactionId: str
    CommitDigest: Union[bytes, IO[bytes]]


class CommitTransactionResultTypeDef(TypedDict, total=False):
    TransactionId: str
    CommitDigest: Union[bytes, IO[bytes]]
    TimingInformation: "TimingInformationTypeDef"
    ConsumedIOs: "IOUsageTypeDef"


class EndSessionResultTypeDef(TypedDict, total=False):
    TimingInformation: "TimingInformationTypeDef"


class _RequiredExecuteStatementRequestTypeDef(TypedDict):
    TransactionId: str
    Statement: str


class ExecuteStatementRequestTypeDef(_RequiredExecuteStatementRequestTypeDef, total=False):
    Parameters: List["ValueHolderTypeDef"]


class ExecuteStatementResultTypeDef(TypedDict, total=False):
    FirstPage: "PageTypeDef"
    TimingInformation: "TimingInformationTypeDef"
    ConsumedIOs: "IOUsageTypeDef"


class FetchPageRequestTypeDef(TypedDict):
    TransactionId: str
    NextPageToken: str


class FetchPageResultTypeDef(TypedDict, total=False):
    Page: "PageTypeDef"
    TimingInformation: "TimingInformationTypeDef"
    ConsumedIOs: "IOUsageTypeDef"


class IOUsageTypeDef(TypedDict, total=False):
    ReadIOs: int
    WriteIOs: int


class PageTypeDef(TypedDict, total=False):
    Values: List["ValueHolderTypeDef"]
    NextPageToken: str


class SendCommandResultTypeDef(TypedDict, total=False):
    StartSession: "StartSessionResultTypeDef"
    StartTransaction: "StartTransactionResultTypeDef"
    EndSession: "EndSessionResultTypeDef"
    CommitTransaction: "CommitTransactionResultTypeDef"
    AbortTransaction: "AbortTransactionResultTypeDef"
    ExecuteStatement: "ExecuteStatementResultTypeDef"
    FetchPage: "FetchPageResultTypeDef"


class StartSessionRequestTypeDef(TypedDict):
    LedgerName: str


class StartSessionResultTypeDef(TypedDict, total=False):
    SessionToken: str
    TimingInformation: "TimingInformationTypeDef"


class StartTransactionResultTypeDef(TypedDict, total=False):
    TransactionId: str
    TimingInformation: "TimingInformationTypeDef"


class TimingInformationTypeDef(TypedDict, total=False):
    ProcessingTimeMilliseconds: int


class ValueHolderTypeDef(TypedDict, total=False):
    IonBinary: Union[bytes, IO[bytes]]
    IonText: str
