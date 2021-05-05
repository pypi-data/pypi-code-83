"""
Type annotations for finspace-data service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_finspace_data/type_defs.html)

Usage::

    ```python
    from mypy_boto3_finspace_data.type_defs import ChangesetInfoTypeDef

    data: ChangesetInfoTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict

from mypy_boto3_finspace_data.literals import ChangesetStatus, ChangeType, ErrorCategory, FormatType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ChangesetInfoTypeDef",
    "CreateChangesetResponseTypeDef",
    "CredentialsTypeDef",
    "ErrorInfoTypeDef",
    "GetProgrammaticAccessCredentialsResponseTypeDef",
    "GetWorkingLocationResponseTypeDef",
)

ChangesetInfoTypeDef = TypedDict(
    "ChangesetInfoTypeDef",
    {
        "id": str,
        "changesetArn": str,
        "datasetId": str,
        "changeType": ChangeType,
        "sourceType": Literal["S3"],
        "sourceParams": Dict[str, str],
        "formatType": FormatType,
        "formatParams": Dict[str, str],
        "createTimestamp": datetime,
        "status": ChangesetStatus,
        "errorInfo": "ErrorInfoTypeDef",
        "changesetLabels": Dict[str, str],
        "updatesChangesetId": str,
        "updatedByChangesetId": str,
    },
    total=False,
)


class CreateChangesetResponseTypeDef(TypedDict, total=False):
    changeset: "ChangesetInfoTypeDef"


class CredentialsTypeDef(TypedDict, total=False):
    accessKeyId: str
    secretAccessKey: str
    sessionToken: str


class ErrorInfoTypeDef(TypedDict, total=False):
    errorMessage: str
    errorCategory: ErrorCategory


class GetProgrammaticAccessCredentialsResponseTypeDef(TypedDict, total=False):
    credentials: "CredentialsTypeDef"
    durationInMinutes: int


class GetWorkingLocationResponseTypeDef(TypedDict, total=False):
    s3Uri: str
    s3Path: str
    s3Bucket: str
