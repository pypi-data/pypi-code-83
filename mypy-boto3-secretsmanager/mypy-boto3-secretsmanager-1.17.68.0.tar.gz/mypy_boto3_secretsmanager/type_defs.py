"""
Type annotations for secretsmanager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_secretsmanager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_secretsmanager.type_defs import CancelRotateSecretResponseTypeDef

    data: CancelRotateSecretResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_secretsmanager.literals import FilterNameStringType, StatusType

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CancelRotateSecretResponseTypeDef",
    "CreateSecretResponseTypeDef",
    "DeleteResourcePolicyResponseTypeDef",
    "DeleteSecretResponseTypeDef",
    "DescribeSecretResponseTypeDef",
    "FilterTypeDef",
    "GetRandomPasswordResponseTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "GetSecretValueResponseTypeDef",
    "ListSecretVersionIdsResponseTypeDef",
    "ListSecretsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "PutSecretValueResponseTypeDef",
    "RemoveRegionsFromReplicationResponseTypeDef",
    "ReplicaRegionTypeTypeDef",
    "ReplicateSecretToRegionsResponseTypeDef",
    "ReplicationStatusTypeTypeDef",
    "RestoreSecretResponseTypeDef",
    "RotateSecretResponseTypeDef",
    "RotationRulesTypeTypeDef",
    "SecretListEntryTypeDef",
    "SecretVersionsListEntryTypeDef",
    "StopReplicationToReplicaResponseTypeDef",
    "TagTypeDef",
    "UpdateSecretResponseTypeDef",
    "UpdateSecretVersionStageResponseTypeDef",
    "ValidateResourcePolicyResponseTypeDef",
    "ValidationErrorsEntryTypeDef",
)


class CancelRotateSecretResponseTypeDef(TypedDict, total=False):
    ARN: str
    Name: str
    VersionId: str


class CreateSecretResponseTypeDef(TypedDict, total=False):
    ARN: str
    Name: str
    VersionId: str
    ReplicationStatus: List["ReplicationStatusTypeTypeDef"]


class DeleteResourcePolicyResponseTypeDef(TypedDict, total=False):
    ARN: str
    Name: str


class DeleteSecretResponseTypeDef(TypedDict, total=False):
    ARN: str
    Name: str
    DeletionDate: datetime


class DescribeSecretResponseTypeDef(TypedDict, total=False):
    ARN: str
    Name: str
    Description: str
    KmsKeyId: str
    RotationEnabled: bool
    RotationLambdaARN: str
    RotationRules: "RotationRulesTypeTypeDef"
    LastRotatedDate: datetime
    LastChangedDate: datetime
    LastAccessedDate: datetime
    DeletedDate: datetime
    Tags: List["TagTypeDef"]
    VersionIdsToStages: Dict[str, List[str]]
    OwningService: str
    CreatedDate: datetime
    PrimaryRegion: str
    ReplicationStatus: List["ReplicationStatusTypeTypeDef"]


class FilterTypeDef(TypedDict, total=False):
    Key: FilterNameStringType
    Values: List[str]


class GetRandomPasswordResponseTypeDef(TypedDict, total=False):
    RandomPassword: str


class GetResourcePolicyResponseTypeDef(TypedDict, total=False):
    ARN: str
    Name: str
    ResourcePolicy: str


class GetSecretValueResponseTypeDef(TypedDict, total=False):
    ARN: str
    Name: str
    VersionId: str
    SecretBinary: Union[bytes, IO[bytes]]
    SecretString: str
    VersionStages: List[str]
    CreatedDate: datetime


class ListSecretVersionIdsResponseTypeDef(TypedDict, total=False):
    Versions: List["SecretVersionsListEntryTypeDef"]
    NextToken: str
    ARN: str
    Name: str


class ListSecretsResponseTypeDef(TypedDict, total=False):
    SecretList: List["SecretListEntryTypeDef"]
    NextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PutResourcePolicyResponseTypeDef(TypedDict, total=False):
    ARN: str
    Name: str


class PutSecretValueResponseTypeDef(TypedDict, total=False):
    ARN: str
    Name: str
    VersionId: str
    VersionStages: List[str]


class RemoveRegionsFromReplicationResponseTypeDef(TypedDict, total=False):
    ARN: str
    ReplicationStatus: List["ReplicationStatusTypeTypeDef"]


class ReplicaRegionTypeTypeDef(TypedDict, total=False):
    Region: str
    KmsKeyId: str


class ReplicateSecretToRegionsResponseTypeDef(TypedDict, total=False):
    ARN: str
    ReplicationStatus: List["ReplicationStatusTypeTypeDef"]


class ReplicationStatusTypeTypeDef(TypedDict, total=False):
    Region: str
    KmsKeyId: str
    Status: StatusType
    StatusMessage: str
    LastAccessedDate: datetime


class RestoreSecretResponseTypeDef(TypedDict, total=False):
    ARN: str
    Name: str


class RotateSecretResponseTypeDef(TypedDict, total=False):
    ARN: str
    Name: str
    VersionId: str


class RotationRulesTypeTypeDef(TypedDict, total=False):
    AutomaticallyAfterDays: int


class SecretListEntryTypeDef(TypedDict, total=False):
    ARN: str
    Name: str
    Description: str
    KmsKeyId: str
    RotationEnabled: bool
    RotationLambdaARN: str
    RotationRules: "RotationRulesTypeTypeDef"
    LastRotatedDate: datetime
    LastChangedDate: datetime
    LastAccessedDate: datetime
    DeletedDate: datetime
    Tags: List["TagTypeDef"]
    SecretVersionsToStages: Dict[str, List[str]]
    OwningService: str
    CreatedDate: datetime
    PrimaryRegion: str


class SecretVersionsListEntryTypeDef(TypedDict, total=False):
    VersionId: str
    VersionStages: List[str]
    LastAccessedDate: datetime
    CreatedDate: datetime


class StopReplicationToReplicaResponseTypeDef(TypedDict, total=False):
    ARN: str


class TagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class UpdateSecretResponseTypeDef(TypedDict, total=False):
    ARN: str
    Name: str
    VersionId: str


class UpdateSecretVersionStageResponseTypeDef(TypedDict, total=False):
    ARN: str
    Name: str


class ValidateResourcePolicyResponseTypeDef(TypedDict, total=False):
    PolicyValidationPassed: bool
    ValidationErrors: List["ValidationErrorsEntryTypeDef"]


class ValidationErrorsEntryTypeDef(TypedDict, total=False):
    CheckName: str
    ErrorMessage: str
