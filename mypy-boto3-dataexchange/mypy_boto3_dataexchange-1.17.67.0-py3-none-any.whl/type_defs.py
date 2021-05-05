"""
Type annotations for dataexchange service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_dataexchange/type_defs.html)

Usage::

    ```python
    from mypy_boto3_dataexchange.type_defs import AssetDestinationEntryTypeDef

    data: AssetDestinationEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_dataexchange.literals import (
    Code,
    JobErrorLimitName,
    JobErrorResourceTypes,
    Origin,
    ServerSideEncryptionTypes,
    State,
    TypeType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssetDestinationEntryTypeDef",
    "AssetDetailsTypeDef",
    "AssetEntryTypeDef",
    "AssetSourceEntryTypeDef",
    "CreateDataSetResponseTypeDef",
    "CreateJobResponseTypeDef",
    "CreateRevisionResponseTypeDef",
    "DataSetEntryTypeDef",
    "DetailsTypeDef",
    "ExportAssetToSignedUrlRequestDetailsTypeDef",
    "ExportAssetToSignedUrlResponseDetailsTypeDef",
    "ExportAssetsToS3RequestDetailsTypeDef",
    "ExportAssetsToS3ResponseDetailsTypeDef",
    "ExportRevisionsToS3RequestDetailsTypeDef",
    "ExportRevisionsToS3ResponseDetailsTypeDef",
    "ExportServerSideEncryptionTypeDef",
    "GetAssetResponseTypeDef",
    "GetDataSetResponseTypeDef",
    "GetJobResponseTypeDef",
    "GetRevisionResponseTypeDef",
    "ImportAssetFromSignedUrlJobErrorDetailsTypeDef",
    "ImportAssetFromSignedUrlRequestDetailsTypeDef",
    "ImportAssetFromSignedUrlResponseDetailsTypeDef",
    "ImportAssetsFromS3RequestDetailsTypeDef",
    "ImportAssetsFromS3ResponseDetailsTypeDef",
    "JobEntryTypeDef",
    "JobErrorTypeDef",
    "ListDataSetRevisionsResponseTypeDef",
    "ListDataSetsResponseTypeDef",
    "ListJobsResponseTypeDef",
    "ListRevisionAssetsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OriginDetailsTypeDef",
    "PaginatorConfigTypeDef",
    "RequestDetailsTypeDef",
    "ResponseDetailsTypeDef",
    "RevisionDestinationEntryTypeDef",
    "RevisionEntryTypeDef",
    "S3SnapshotAssetTypeDef",
    "UpdateAssetResponseTypeDef",
    "UpdateDataSetResponseTypeDef",
    "UpdateRevisionResponseTypeDef",
)


class _RequiredAssetDestinationEntryTypeDef(TypedDict):
    AssetId: str
    Bucket: str


class AssetDestinationEntryTypeDef(_RequiredAssetDestinationEntryTypeDef, total=False):
    Key: str


class AssetDetailsTypeDef(TypedDict, total=False):
    S3SnapshotAsset: "S3SnapshotAssetTypeDef"


class _RequiredAssetEntryTypeDef(TypedDict):
    Arn: str
    AssetDetails: "AssetDetailsTypeDef"
    AssetType: Literal["S3_SNAPSHOT"]
    CreatedAt: datetime
    DataSetId: str
    Id: str
    Name: str
    RevisionId: str
    UpdatedAt: datetime


class AssetEntryTypeDef(_RequiredAssetEntryTypeDef, total=False):
    SourceId: str


class AssetSourceEntryTypeDef(TypedDict):
    Bucket: str
    Key: str


class CreateDataSetResponseTypeDef(TypedDict, total=False):
    Arn: str
    AssetType: Literal["S3_SNAPSHOT"]
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: Origin
    OriginDetails: "OriginDetailsTypeDef"
    SourceId: str
    Tags: Dict[str, str]
    UpdatedAt: datetime


CreateJobResponseTypeDef = TypedDict(
    "CreateJobResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": "ResponseDetailsTypeDef",
        "Errors": List["JobErrorTypeDef"],
        "Id": str,
        "State": State,
        "Type": TypeType,
        "UpdatedAt": datetime,
    },
    total=False,
)


class CreateRevisionResponseTypeDef(TypedDict, total=False):
    Arn: str
    Comment: str
    CreatedAt: datetime
    DataSetId: str
    Finalized: bool
    Id: str
    SourceId: str
    Tags: Dict[str, str]
    UpdatedAt: datetime


class _RequiredDataSetEntryTypeDef(TypedDict):
    Arn: str
    AssetType: Literal["S3_SNAPSHOT"]
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: Origin
    UpdatedAt: datetime


class DataSetEntryTypeDef(_RequiredDataSetEntryTypeDef, total=False):
    OriginDetails: "OriginDetailsTypeDef"
    SourceId: str


class DetailsTypeDef(TypedDict, total=False):
    ImportAssetFromSignedUrlJobErrorDetails: "ImportAssetFromSignedUrlJobErrorDetailsTypeDef"
    ImportAssetsFromS3JobErrorDetails: List["AssetSourceEntryTypeDef"]


class ExportAssetToSignedUrlRequestDetailsTypeDef(TypedDict):
    AssetId: str
    DataSetId: str
    RevisionId: str


class _RequiredExportAssetToSignedUrlResponseDetailsTypeDef(TypedDict):
    AssetId: str
    DataSetId: str
    RevisionId: str


class ExportAssetToSignedUrlResponseDetailsTypeDef(
    _RequiredExportAssetToSignedUrlResponseDetailsTypeDef, total=False
):
    SignedUrl: str
    SignedUrlExpiresAt: datetime


class _RequiredExportAssetsToS3RequestDetailsTypeDef(TypedDict):
    AssetDestinations: List["AssetDestinationEntryTypeDef"]
    DataSetId: str
    RevisionId: str


class ExportAssetsToS3RequestDetailsTypeDef(
    _RequiredExportAssetsToS3RequestDetailsTypeDef, total=False
):
    Encryption: "ExportServerSideEncryptionTypeDef"


class _RequiredExportAssetsToS3ResponseDetailsTypeDef(TypedDict):
    AssetDestinations: List["AssetDestinationEntryTypeDef"]
    DataSetId: str
    RevisionId: str


class ExportAssetsToS3ResponseDetailsTypeDef(
    _RequiredExportAssetsToS3ResponseDetailsTypeDef, total=False
):
    Encryption: "ExportServerSideEncryptionTypeDef"


class _RequiredExportRevisionsToS3RequestDetailsTypeDef(TypedDict):
    DataSetId: str
    RevisionDestinations: List["RevisionDestinationEntryTypeDef"]


class ExportRevisionsToS3RequestDetailsTypeDef(
    _RequiredExportRevisionsToS3RequestDetailsTypeDef, total=False
):
    Encryption: "ExportServerSideEncryptionTypeDef"


class _RequiredExportRevisionsToS3ResponseDetailsTypeDef(TypedDict):
    DataSetId: str
    RevisionDestinations: List["RevisionDestinationEntryTypeDef"]


class ExportRevisionsToS3ResponseDetailsTypeDef(
    _RequiredExportRevisionsToS3ResponseDetailsTypeDef, total=False
):
    Encryption: "ExportServerSideEncryptionTypeDef"


_RequiredExportServerSideEncryptionTypeDef = TypedDict(
    "_RequiredExportServerSideEncryptionTypeDef", {"Type": ServerSideEncryptionTypes}
)
_OptionalExportServerSideEncryptionTypeDef = TypedDict(
    "_OptionalExportServerSideEncryptionTypeDef", {"KmsKeyArn": str}, total=False
)


class ExportServerSideEncryptionTypeDef(
    _RequiredExportServerSideEncryptionTypeDef, _OptionalExportServerSideEncryptionTypeDef
):
    pass


class GetAssetResponseTypeDef(TypedDict, total=False):
    Arn: str
    AssetDetails: "AssetDetailsTypeDef"
    AssetType: Literal["S3_SNAPSHOT"]
    CreatedAt: datetime
    DataSetId: str
    Id: str
    Name: str
    RevisionId: str
    SourceId: str
    UpdatedAt: datetime


class GetDataSetResponseTypeDef(TypedDict, total=False):
    Arn: str
    AssetType: Literal["S3_SNAPSHOT"]
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: Origin
    OriginDetails: "OriginDetailsTypeDef"
    SourceId: str
    Tags: Dict[str, str]
    UpdatedAt: datetime


GetJobResponseTypeDef = TypedDict(
    "GetJobResponseTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": "ResponseDetailsTypeDef",
        "Errors": List["JobErrorTypeDef"],
        "Id": str,
        "State": State,
        "Type": TypeType,
        "UpdatedAt": datetime,
    },
    total=False,
)


class GetRevisionResponseTypeDef(TypedDict, total=False):
    Arn: str
    Comment: str
    CreatedAt: datetime
    DataSetId: str
    Finalized: bool
    Id: str
    SourceId: str
    Tags: Dict[str, str]
    UpdatedAt: datetime


class ImportAssetFromSignedUrlJobErrorDetailsTypeDef(TypedDict):
    AssetName: str


class ImportAssetFromSignedUrlRequestDetailsTypeDef(TypedDict):
    AssetName: str
    DataSetId: str
    Md5Hash: str
    RevisionId: str


class _RequiredImportAssetFromSignedUrlResponseDetailsTypeDef(TypedDict):
    AssetName: str
    DataSetId: str
    RevisionId: str


class ImportAssetFromSignedUrlResponseDetailsTypeDef(
    _RequiredImportAssetFromSignedUrlResponseDetailsTypeDef, total=False
):
    Md5Hash: str
    SignedUrl: str
    SignedUrlExpiresAt: datetime


class ImportAssetsFromS3RequestDetailsTypeDef(TypedDict):
    AssetSources: List["AssetSourceEntryTypeDef"]
    DataSetId: str
    RevisionId: str


class ImportAssetsFromS3ResponseDetailsTypeDef(TypedDict):
    AssetSources: List["AssetSourceEntryTypeDef"]
    DataSetId: str
    RevisionId: str


_RequiredJobEntryTypeDef = TypedDict(
    "_RequiredJobEntryTypeDef",
    {
        "Arn": str,
        "CreatedAt": datetime,
        "Details": "ResponseDetailsTypeDef",
        "Id": str,
        "State": State,
        "Type": TypeType,
        "UpdatedAt": datetime,
    },
)
_OptionalJobEntryTypeDef = TypedDict(
    "_OptionalJobEntryTypeDef", {"Errors": List["JobErrorTypeDef"]}, total=False
)


class JobEntryTypeDef(_RequiredJobEntryTypeDef, _OptionalJobEntryTypeDef):
    pass


class _RequiredJobErrorTypeDef(TypedDict):
    Code: Code
    Message: str


class JobErrorTypeDef(_RequiredJobErrorTypeDef, total=False):
    Details: "DetailsTypeDef"
    LimitName: JobErrorLimitName
    LimitValue: float
    ResourceId: str
    ResourceType: JobErrorResourceTypes


class ListDataSetRevisionsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Revisions: List["RevisionEntryTypeDef"]


class ListDataSetsResponseTypeDef(TypedDict, total=False):
    DataSets: List["DataSetEntryTypeDef"]
    NextToken: str


class ListJobsResponseTypeDef(TypedDict, total=False):
    Jobs: List["JobEntryTypeDef"]
    NextToken: str


class ListRevisionAssetsResponseTypeDef(TypedDict, total=False):
    Assets: List["AssetEntryTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class OriginDetailsTypeDef(TypedDict):
    ProductId: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RequestDetailsTypeDef(TypedDict, total=False):
    ExportAssetToSignedUrl: "ExportAssetToSignedUrlRequestDetailsTypeDef"
    ExportAssetsToS3: "ExportAssetsToS3RequestDetailsTypeDef"
    ExportRevisionsToS3: "ExportRevisionsToS3RequestDetailsTypeDef"
    ImportAssetFromSignedUrl: "ImportAssetFromSignedUrlRequestDetailsTypeDef"
    ImportAssetsFromS3: "ImportAssetsFromS3RequestDetailsTypeDef"


class ResponseDetailsTypeDef(TypedDict, total=False):
    ExportAssetToSignedUrl: "ExportAssetToSignedUrlResponseDetailsTypeDef"
    ExportAssetsToS3: "ExportAssetsToS3ResponseDetailsTypeDef"
    ExportRevisionsToS3: "ExportRevisionsToS3ResponseDetailsTypeDef"
    ImportAssetFromSignedUrl: "ImportAssetFromSignedUrlResponseDetailsTypeDef"
    ImportAssetsFromS3: "ImportAssetsFromS3ResponseDetailsTypeDef"


class _RequiredRevisionDestinationEntryTypeDef(TypedDict):
    Bucket: str
    RevisionId: str


class RevisionDestinationEntryTypeDef(_RequiredRevisionDestinationEntryTypeDef, total=False):
    KeyPattern: str


class _RequiredRevisionEntryTypeDef(TypedDict):
    Arn: str
    CreatedAt: datetime
    DataSetId: str
    Id: str
    UpdatedAt: datetime


class RevisionEntryTypeDef(_RequiredRevisionEntryTypeDef, total=False):
    Comment: str
    Finalized: bool
    SourceId: str


class S3SnapshotAssetTypeDef(TypedDict):
    Size: float


class UpdateAssetResponseTypeDef(TypedDict, total=False):
    Arn: str
    AssetDetails: "AssetDetailsTypeDef"
    AssetType: Literal["S3_SNAPSHOT"]
    CreatedAt: datetime
    DataSetId: str
    Id: str
    Name: str
    RevisionId: str
    SourceId: str
    UpdatedAt: datetime


class UpdateDataSetResponseTypeDef(TypedDict, total=False):
    Arn: str
    AssetType: Literal["S3_SNAPSHOT"]
    CreatedAt: datetime
    Description: str
    Id: str
    Name: str
    Origin: Origin
    OriginDetails: "OriginDetailsTypeDef"
    SourceId: str
    UpdatedAt: datetime


class UpdateRevisionResponseTypeDef(TypedDict, total=False):
    Arn: str
    Comment: str
    CreatedAt: datetime
    DataSetId: str
    Finalized: bool
    Id: str
    SourceId: str
    UpdatedAt: datetime
