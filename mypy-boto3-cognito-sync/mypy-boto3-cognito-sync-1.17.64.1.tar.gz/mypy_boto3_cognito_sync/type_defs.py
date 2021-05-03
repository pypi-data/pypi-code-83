"""
Type annotations for cognito-sync service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_cognito_sync/type_defs.html)

Usage::

    ```python
    from mypy_boto3_cognito_sync.type_defs import BulkPublishResponseTypeDef

    data: BulkPublishResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_cognito_sync.literals import BulkPublishStatus, Operation, StreamingStatus

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BulkPublishResponseTypeDef",
    "CognitoStreamsTypeDef",
    "DatasetTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeIdentityPoolUsageResponseTypeDef",
    "DescribeIdentityUsageResponseTypeDef",
    "GetBulkPublishDetailsResponseTypeDef",
    "GetCognitoEventsResponseTypeDef",
    "GetIdentityPoolConfigurationResponseTypeDef",
    "IdentityPoolUsageTypeDef",
    "IdentityUsageTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListIdentityPoolUsageResponseTypeDef",
    "ListRecordsResponseTypeDef",
    "PushSyncTypeDef",
    "RecordPatchTypeDef",
    "RecordTypeDef",
    "RegisterDeviceResponseTypeDef",
    "SetIdentityPoolConfigurationResponseTypeDef",
    "UpdateRecordsResponseTypeDef",
)


class BulkPublishResponseTypeDef(TypedDict, total=False):
    IdentityPoolId: str


class CognitoStreamsTypeDef(TypedDict, total=False):
    StreamName: str
    RoleArn: str
    StreamingStatus: StreamingStatus


class DatasetTypeDef(TypedDict, total=False):
    IdentityId: str
    DatasetName: str
    CreationDate: datetime
    LastModifiedDate: datetime
    LastModifiedBy: str
    DataStorage: int
    NumRecords: int


class DeleteDatasetResponseTypeDef(TypedDict, total=False):
    Dataset: "DatasetTypeDef"


class DescribeDatasetResponseTypeDef(TypedDict, total=False):
    Dataset: "DatasetTypeDef"


class DescribeIdentityPoolUsageResponseTypeDef(TypedDict, total=False):
    IdentityPoolUsage: "IdentityPoolUsageTypeDef"


class DescribeIdentityUsageResponseTypeDef(TypedDict, total=False):
    IdentityUsage: "IdentityUsageTypeDef"


class GetBulkPublishDetailsResponseTypeDef(TypedDict, total=False):
    IdentityPoolId: str
    BulkPublishStartTime: datetime
    BulkPublishCompleteTime: datetime
    BulkPublishStatus: BulkPublishStatus
    FailureMessage: str


class GetCognitoEventsResponseTypeDef(TypedDict, total=False):
    Events: Dict[str, str]


class GetIdentityPoolConfigurationResponseTypeDef(TypedDict, total=False):
    IdentityPoolId: str
    PushSync: "PushSyncTypeDef"
    CognitoStreams: "CognitoStreamsTypeDef"


class IdentityPoolUsageTypeDef(TypedDict, total=False):
    IdentityPoolId: str
    SyncSessionsCount: int
    DataStorage: int
    LastModifiedDate: datetime


class IdentityUsageTypeDef(TypedDict, total=False):
    IdentityId: str
    IdentityPoolId: str
    LastModifiedDate: datetime
    DatasetCount: int
    DataStorage: int


class ListDatasetsResponseTypeDef(TypedDict, total=False):
    Datasets: List["DatasetTypeDef"]
    Count: int
    NextToken: str


class ListIdentityPoolUsageResponseTypeDef(TypedDict, total=False):
    IdentityPoolUsages: List["IdentityPoolUsageTypeDef"]
    MaxResults: int
    Count: int
    NextToken: str


class ListRecordsResponseTypeDef(TypedDict, total=False):
    Records: List["RecordTypeDef"]
    NextToken: str
    Count: int
    DatasetSyncCount: int
    LastModifiedBy: str
    MergedDatasetNames: List[str]
    DatasetExists: bool
    DatasetDeletedAfterRequestedSyncCount: bool
    SyncSessionToken: str


class PushSyncTypeDef(TypedDict, total=False):
    ApplicationArns: List[str]
    RoleArn: str


class _RequiredRecordPatchTypeDef(TypedDict):
    Op: Operation
    Key: str
    SyncCount: int


class RecordPatchTypeDef(_RequiredRecordPatchTypeDef, total=False):
    Value: str
    DeviceLastModifiedDate: datetime


class RecordTypeDef(TypedDict, total=False):
    Key: str
    Value: str
    SyncCount: int
    LastModifiedDate: datetime
    LastModifiedBy: str
    DeviceLastModifiedDate: datetime


class RegisterDeviceResponseTypeDef(TypedDict, total=False):
    DeviceId: str


class SetIdentityPoolConfigurationResponseTypeDef(TypedDict, total=False):
    IdentityPoolId: str
    PushSync: "PushSyncTypeDef"
    CognitoStreams: "CognitoStreamsTypeDef"


class UpdateRecordsResponseTypeDef(TypedDict, total=False):
    Records: List["RecordTypeDef"]
