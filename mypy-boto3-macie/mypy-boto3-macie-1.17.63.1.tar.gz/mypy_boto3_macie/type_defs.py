"""
Type annotations for macie service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_macie/type_defs.html)

Usage::

    ```python
    from mypy_boto3_macie.type_defs import AssociateS3ResourcesResultTypeDef

    data: AssociateS3ResourcesResultTypeDef = {...}
    ```
"""
import sys
from typing import List

from mypy_boto3_macie.literals import S3OneTimeClassificationType

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateS3ResourcesResultTypeDef",
    "ClassificationTypeTypeDef",
    "ClassificationTypeUpdateTypeDef",
    "DisassociateS3ResourcesResultTypeDef",
    "FailedS3ResourceTypeDef",
    "ListMemberAccountsResultTypeDef",
    "ListS3ResourcesResultTypeDef",
    "MemberAccountTypeDef",
    "PaginatorConfigTypeDef",
    "S3ResourceClassificationTypeDef",
    "S3ResourceClassificationUpdateTypeDef",
    "S3ResourceTypeDef",
    "UpdateS3ResourcesResultTypeDef",
)


class AssociateS3ResourcesResultTypeDef(TypedDict, total=False):
    failedS3Resources: List["FailedS3ResourceTypeDef"]


class ClassificationTypeTypeDef(TypedDict):
    oneTime: S3OneTimeClassificationType
    continuous: Literal["FULL"]


class ClassificationTypeUpdateTypeDef(TypedDict, total=False):
    oneTime: S3OneTimeClassificationType
    continuous: Literal["FULL"]


class DisassociateS3ResourcesResultTypeDef(TypedDict, total=False):
    failedS3Resources: List["FailedS3ResourceTypeDef"]


class FailedS3ResourceTypeDef(TypedDict, total=False):
    failedItem: "S3ResourceTypeDef"
    errorCode: str
    errorMessage: str


class ListMemberAccountsResultTypeDef(TypedDict, total=False):
    memberAccounts: List["MemberAccountTypeDef"]
    nextToken: str


class ListS3ResourcesResultTypeDef(TypedDict, total=False):
    s3Resources: List["S3ResourceClassificationTypeDef"]
    nextToken: str


class MemberAccountTypeDef(TypedDict, total=False):
    accountId: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredS3ResourceClassificationTypeDef(TypedDict):
    bucketName: str
    classificationType: "ClassificationTypeTypeDef"


class S3ResourceClassificationTypeDef(_RequiredS3ResourceClassificationTypeDef, total=False):
    prefix: str


class _RequiredS3ResourceClassificationUpdateTypeDef(TypedDict):
    bucketName: str
    classificationTypeUpdate: "ClassificationTypeUpdateTypeDef"


class S3ResourceClassificationUpdateTypeDef(
    _RequiredS3ResourceClassificationUpdateTypeDef, total=False
):
    prefix: str


class _RequiredS3ResourceTypeDef(TypedDict):
    bucketName: str


class S3ResourceTypeDef(_RequiredS3ResourceTypeDef, total=False):
    prefix: str


class UpdateS3ResourcesResultTypeDef(TypedDict, total=False):
    failedS3Resources: List["FailedS3ResourceTypeDef"]
