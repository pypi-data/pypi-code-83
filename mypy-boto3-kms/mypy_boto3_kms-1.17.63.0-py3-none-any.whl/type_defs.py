"""
Type annotations for kms service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/type_defs.html)

Usage::

    ```python
    from mypy_boto3_kms.type_defs import AliasListEntryTypeDef

    data: AliasListEntryTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Dict, List, Union

from mypy_boto3_kms.literals import (
    ConnectionErrorCodeType,
    ConnectionStateType,
    CustomerMasterKeySpec,
    DataKeyPairSpec,
    EncryptionAlgorithmSpec,
    ExpirationModelType,
    GrantOperation,
    KeyManagerType,
    KeyState,
    KeyUsageType,
    OriginType,
    SigningAlgorithmSpec,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AliasListEntryTypeDef",
    "CancelKeyDeletionResponseTypeDef",
    "CreateCustomKeyStoreResponseTypeDef",
    "CreateGrantResponseTypeDef",
    "CreateKeyResponseTypeDef",
    "CustomKeyStoresListEntryTypeDef",
    "DecryptResponseTypeDef",
    "DescribeCustomKeyStoresResponseTypeDef",
    "DescribeKeyResponseTypeDef",
    "EncryptResponseTypeDef",
    "GenerateDataKeyPairResponseTypeDef",
    "GenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    "GenerateDataKeyResponseTypeDef",
    "GenerateDataKeyWithoutPlaintextResponseTypeDef",
    "GenerateRandomResponseTypeDef",
    "GetKeyPolicyResponseTypeDef",
    "GetKeyRotationStatusResponseTypeDef",
    "GetParametersForImportResponseTypeDef",
    "GetPublicKeyResponseTypeDef",
    "GrantConstraintsTypeDef",
    "GrantListEntryTypeDef",
    "KeyListEntryTypeDef",
    "KeyMetadataTypeDef",
    "ListAliasesResponseTypeDef",
    "ListGrantsResponseTypeDef",
    "ListKeyPoliciesResponseTypeDef",
    "ListKeysResponseTypeDef",
    "ListResourceTagsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ReEncryptResponseTypeDef",
    "ScheduleKeyDeletionResponseTypeDef",
    "SignResponseTypeDef",
    "TagTypeDef",
    "VerifyResponseTypeDef",
)


class AliasListEntryTypeDef(TypedDict, total=False):
    AliasName: str
    AliasArn: str
    TargetKeyId: str
    CreationDate: datetime
    LastUpdatedDate: datetime


class CancelKeyDeletionResponseTypeDef(TypedDict, total=False):
    KeyId: str


class CreateCustomKeyStoreResponseTypeDef(TypedDict, total=False):
    CustomKeyStoreId: str


class CreateGrantResponseTypeDef(TypedDict, total=False):
    GrantToken: str
    GrantId: str


class CreateKeyResponseTypeDef(TypedDict, total=False):
    KeyMetadata: "KeyMetadataTypeDef"


class CustomKeyStoresListEntryTypeDef(TypedDict, total=False):
    CustomKeyStoreId: str
    CustomKeyStoreName: str
    CloudHsmClusterId: str
    TrustAnchorCertificate: str
    ConnectionState: ConnectionStateType
    ConnectionErrorCode: ConnectionErrorCodeType
    CreationDate: datetime


class DecryptResponseTypeDef(TypedDict, total=False):
    KeyId: str
    Plaintext: Union[bytes, IO[bytes]]
    EncryptionAlgorithm: EncryptionAlgorithmSpec


class DescribeCustomKeyStoresResponseTypeDef(TypedDict, total=False):
    CustomKeyStores: List["CustomKeyStoresListEntryTypeDef"]
    NextMarker: str
    Truncated: bool


class DescribeKeyResponseTypeDef(TypedDict, total=False):
    KeyMetadata: "KeyMetadataTypeDef"


class EncryptResponseTypeDef(TypedDict, total=False):
    CiphertextBlob: Union[bytes, IO[bytes]]
    KeyId: str
    EncryptionAlgorithm: EncryptionAlgorithmSpec


class GenerateDataKeyPairResponseTypeDef(TypedDict, total=False):
    PrivateKeyCiphertextBlob: Union[bytes, IO[bytes]]
    PrivateKeyPlaintext: Union[bytes, IO[bytes]]
    PublicKey: Union[bytes, IO[bytes]]
    KeyId: str
    KeyPairSpec: DataKeyPairSpec


class GenerateDataKeyPairWithoutPlaintextResponseTypeDef(TypedDict, total=False):
    PrivateKeyCiphertextBlob: Union[bytes, IO[bytes]]
    PublicKey: Union[bytes, IO[bytes]]
    KeyId: str
    KeyPairSpec: DataKeyPairSpec


class GenerateDataKeyResponseTypeDef(TypedDict, total=False):
    CiphertextBlob: Union[bytes, IO[bytes]]
    Plaintext: Union[bytes, IO[bytes]]
    KeyId: str


class GenerateDataKeyWithoutPlaintextResponseTypeDef(TypedDict, total=False):
    CiphertextBlob: Union[bytes, IO[bytes]]
    KeyId: str


class GenerateRandomResponseTypeDef(TypedDict, total=False):
    Plaintext: Union[bytes, IO[bytes]]


class GetKeyPolicyResponseTypeDef(TypedDict, total=False):
    Policy: str


class GetKeyRotationStatusResponseTypeDef(TypedDict, total=False):
    KeyRotationEnabled: bool


class GetParametersForImportResponseTypeDef(TypedDict, total=False):
    KeyId: str
    ImportToken: Union[bytes, IO[bytes]]
    PublicKey: Union[bytes, IO[bytes]]
    ParametersValidTo: datetime


class GetPublicKeyResponseTypeDef(TypedDict, total=False):
    KeyId: str
    PublicKey: Union[bytes, IO[bytes]]
    CustomerMasterKeySpec: CustomerMasterKeySpec
    KeyUsage: KeyUsageType
    EncryptionAlgorithms: List[EncryptionAlgorithmSpec]
    SigningAlgorithms: List[SigningAlgorithmSpec]


class GrantConstraintsTypeDef(TypedDict, total=False):
    EncryptionContextSubset: Dict[str, str]
    EncryptionContextEquals: Dict[str, str]


class GrantListEntryTypeDef(TypedDict, total=False):
    KeyId: str
    GrantId: str
    Name: str
    CreationDate: datetime
    GranteePrincipal: str
    RetiringPrincipal: str
    IssuingAccount: str
    Operations: List[GrantOperation]
    Constraints: "GrantConstraintsTypeDef"


class KeyListEntryTypeDef(TypedDict, total=False):
    KeyId: str
    KeyArn: str


class _RequiredKeyMetadataTypeDef(TypedDict):
    KeyId: str


class KeyMetadataTypeDef(_RequiredKeyMetadataTypeDef, total=False):
    AWSAccountId: str
    Arn: str
    CreationDate: datetime
    Enabled: bool
    Description: str
    KeyUsage: KeyUsageType
    KeyState: KeyState
    DeletionDate: datetime
    ValidTo: datetime
    Origin: OriginType
    CustomKeyStoreId: str
    CloudHsmClusterId: str
    ExpirationModel: ExpirationModelType
    KeyManager: KeyManagerType
    CustomerMasterKeySpec: CustomerMasterKeySpec
    EncryptionAlgorithms: List[EncryptionAlgorithmSpec]
    SigningAlgorithms: List[SigningAlgorithmSpec]


class ListAliasesResponseTypeDef(TypedDict, total=False):
    Aliases: List["AliasListEntryTypeDef"]
    NextMarker: str
    Truncated: bool


class ListGrantsResponseTypeDef(TypedDict, total=False):
    Grants: List["GrantListEntryTypeDef"]
    NextMarker: str
    Truncated: bool


class ListKeyPoliciesResponseTypeDef(TypedDict, total=False):
    PolicyNames: List[str]
    NextMarker: str
    Truncated: bool


class ListKeysResponseTypeDef(TypedDict, total=False):
    Keys: List["KeyListEntryTypeDef"]
    NextMarker: str
    Truncated: bool


class ListResourceTagsResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]
    NextMarker: str
    Truncated: bool


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ReEncryptResponseTypeDef(TypedDict, total=False):
    CiphertextBlob: Union[bytes, IO[bytes]]
    SourceKeyId: str
    KeyId: str
    SourceEncryptionAlgorithm: EncryptionAlgorithmSpec
    DestinationEncryptionAlgorithm: EncryptionAlgorithmSpec


class ScheduleKeyDeletionResponseTypeDef(TypedDict, total=False):
    KeyId: str
    DeletionDate: datetime


class SignResponseTypeDef(TypedDict, total=False):
    KeyId: str
    Signature: Union[bytes, IO[bytes]]
    SigningAlgorithm: SigningAlgorithmSpec


class TagTypeDef(TypedDict):
    TagKey: str
    TagValue: str


class VerifyResponseTypeDef(TypedDict, total=False):
    KeyId: str
    SignatureValid: bool
    SigningAlgorithm: SigningAlgorithmSpec
