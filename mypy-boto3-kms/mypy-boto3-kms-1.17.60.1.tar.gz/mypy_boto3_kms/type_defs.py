"""
Main interface for kms service type definitions.

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
    "CustomKeyStoresListEntryTypeDef",
    "GrantConstraintsTypeDef",
    "GrantListEntryTypeDef",
    "KeyListEntryTypeDef",
    "KeyMetadataTypeDef",
    "TagTypeDef",
    "CancelKeyDeletionResponseTypeDef",
    "CreateCustomKeyStoreResponseTypeDef",
    "CreateGrantResponseTypeDef",
    "CreateKeyResponseTypeDef",
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
    "ListAliasesResponseTypeDef",
    "ListGrantsResponseTypeDef",
    "ListKeyPoliciesResponseTypeDef",
    "ListKeysResponseTypeDef",
    "ListResourceTagsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ReEncryptResponseTypeDef",
    "ScheduleKeyDeletionResponseTypeDef",
    "SignResponseTypeDef",
    "VerifyResponseTypeDef",
)

AliasListEntryTypeDef = TypedDict(
    "AliasListEntryTypeDef",
    {
        "AliasName": str,
        "AliasArn": str,
        "TargetKeyId": str,
        "CreationDate": datetime,
        "LastUpdatedDate": datetime,
    },
    total=False,
)

CustomKeyStoresListEntryTypeDef = TypedDict(
    "CustomKeyStoresListEntryTypeDef",
    {
        "CustomKeyStoreId": str,
        "CustomKeyStoreName": str,
        "CloudHsmClusterId": str,
        "TrustAnchorCertificate": str,
        "ConnectionState": ConnectionStateType,
        "ConnectionErrorCode": ConnectionErrorCodeType,
        "CreationDate": datetime,
    },
    total=False,
)

GrantConstraintsTypeDef = TypedDict(
    "GrantConstraintsTypeDef",
    {"EncryptionContextSubset": Dict[str, str], "EncryptionContextEquals": Dict[str, str]},
    total=False,
)

GrantListEntryTypeDef = TypedDict(
    "GrantListEntryTypeDef",
    {
        "KeyId": str,
        "GrantId": str,
        "Name": str,
        "CreationDate": datetime,
        "GranteePrincipal": str,
        "RetiringPrincipal": str,
        "IssuingAccount": str,
        "Operations": List[GrantOperation],
        "Constraints": "GrantConstraintsTypeDef",
    },
    total=False,
)

KeyListEntryTypeDef = TypedDict("KeyListEntryTypeDef", {"KeyId": str, "KeyArn": str}, total=False)

_RequiredKeyMetadataTypeDef = TypedDict("_RequiredKeyMetadataTypeDef", {"KeyId": str})
_OptionalKeyMetadataTypeDef = TypedDict(
    "_OptionalKeyMetadataTypeDef",
    {
        "AWSAccountId": str,
        "Arn": str,
        "CreationDate": datetime,
        "Enabled": bool,
        "Description": str,
        "KeyUsage": KeyUsageType,
        "KeyState": KeyState,
        "DeletionDate": datetime,
        "ValidTo": datetime,
        "Origin": OriginType,
        "CustomKeyStoreId": str,
        "CloudHsmClusterId": str,
        "ExpirationModel": ExpirationModelType,
        "KeyManager": KeyManagerType,
        "CustomerMasterKeySpec": CustomerMasterKeySpec,
        "EncryptionAlgorithms": List[EncryptionAlgorithmSpec],
        "SigningAlgorithms": List[SigningAlgorithmSpec],
    },
    total=False,
)


class KeyMetadataTypeDef(_RequiredKeyMetadataTypeDef, _OptionalKeyMetadataTypeDef):
    pass


TagTypeDef = TypedDict("TagTypeDef", {"TagKey": str, "TagValue": str})

CancelKeyDeletionResponseTypeDef = TypedDict(
    "CancelKeyDeletionResponseTypeDef", {"KeyId": str}, total=False
)

CreateCustomKeyStoreResponseTypeDef = TypedDict(
    "CreateCustomKeyStoreResponseTypeDef", {"CustomKeyStoreId": str}, total=False
)

CreateGrantResponseTypeDef = TypedDict(
    "CreateGrantResponseTypeDef", {"GrantToken": str, "GrantId": str}, total=False
)

CreateKeyResponseTypeDef = TypedDict(
    "CreateKeyResponseTypeDef", {"KeyMetadata": "KeyMetadataTypeDef"}, total=False
)

DecryptResponseTypeDef = TypedDict(
    "DecryptResponseTypeDef",
    {
        "KeyId": str,
        "Plaintext": Union[bytes, IO[bytes]],
        "EncryptionAlgorithm": EncryptionAlgorithmSpec,
    },
    total=False,
)

DescribeCustomKeyStoresResponseTypeDef = TypedDict(
    "DescribeCustomKeyStoresResponseTypeDef",
    {
        "CustomKeyStores": List["CustomKeyStoresListEntryTypeDef"],
        "NextMarker": str,
        "Truncated": bool,
    },
    total=False,
)

DescribeKeyResponseTypeDef = TypedDict(
    "DescribeKeyResponseTypeDef", {"KeyMetadata": "KeyMetadataTypeDef"}, total=False
)

EncryptResponseTypeDef = TypedDict(
    "EncryptResponseTypeDef",
    {
        "CiphertextBlob": Union[bytes, IO[bytes]],
        "KeyId": str,
        "EncryptionAlgorithm": EncryptionAlgorithmSpec,
    },
    total=False,
)

GenerateDataKeyPairResponseTypeDef = TypedDict(
    "GenerateDataKeyPairResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": Union[bytes, IO[bytes]],
        "PrivateKeyPlaintext": Union[bytes, IO[bytes]],
        "PublicKey": Union[bytes, IO[bytes]],
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpec,
    },
    total=False,
)

GenerateDataKeyPairWithoutPlaintextResponseTypeDef = TypedDict(
    "GenerateDataKeyPairWithoutPlaintextResponseTypeDef",
    {
        "PrivateKeyCiphertextBlob": Union[bytes, IO[bytes]],
        "PublicKey": Union[bytes, IO[bytes]],
        "KeyId": str,
        "KeyPairSpec": DataKeyPairSpec,
    },
    total=False,
)

GenerateDataKeyResponseTypeDef = TypedDict(
    "GenerateDataKeyResponseTypeDef",
    {"CiphertextBlob": Union[bytes, IO[bytes]], "Plaintext": Union[bytes, IO[bytes]], "KeyId": str},
    total=False,
)

GenerateDataKeyWithoutPlaintextResponseTypeDef = TypedDict(
    "GenerateDataKeyWithoutPlaintextResponseTypeDef",
    {"CiphertextBlob": Union[bytes, IO[bytes]], "KeyId": str},
    total=False,
)

GenerateRandomResponseTypeDef = TypedDict(
    "GenerateRandomResponseTypeDef", {"Plaintext": Union[bytes, IO[bytes]]}, total=False
)

GetKeyPolicyResponseTypeDef = TypedDict("GetKeyPolicyResponseTypeDef", {"Policy": str}, total=False)

GetKeyRotationStatusResponseTypeDef = TypedDict(
    "GetKeyRotationStatusResponseTypeDef", {"KeyRotationEnabled": bool}, total=False
)

GetParametersForImportResponseTypeDef = TypedDict(
    "GetParametersForImportResponseTypeDef",
    {
        "KeyId": str,
        "ImportToken": Union[bytes, IO[bytes]],
        "PublicKey": Union[bytes, IO[bytes]],
        "ParametersValidTo": datetime,
    },
    total=False,
)

GetPublicKeyResponseTypeDef = TypedDict(
    "GetPublicKeyResponseTypeDef",
    {
        "KeyId": str,
        "PublicKey": Union[bytes, IO[bytes]],
        "CustomerMasterKeySpec": CustomerMasterKeySpec,
        "KeyUsage": KeyUsageType,
        "EncryptionAlgorithms": List[EncryptionAlgorithmSpec],
        "SigningAlgorithms": List[SigningAlgorithmSpec],
    },
    total=False,
)

ListAliasesResponseTypeDef = TypedDict(
    "ListAliasesResponseTypeDef",
    {"Aliases": List["AliasListEntryTypeDef"], "NextMarker": str, "Truncated": bool},
    total=False,
)

ListGrantsResponseTypeDef = TypedDict(
    "ListGrantsResponseTypeDef",
    {"Grants": List["GrantListEntryTypeDef"], "NextMarker": str, "Truncated": bool},
    total=False,
)

ListKeyPoliciesResponseTypeDef = TypedDict(
    "ListKeyPoliciesResponseTypeDef",
    {"PolicyNames": List[str], "NextMarker": str, "Truncated": bool},
    total=False,
)

ListKeysResponseTypeDef = TypedDict(
    "ListKeysResponseTypeDef",
    {"Keys": List["KeyListEntryTypeDef"], "NextMarker": str, "Truncated": bool},
    total=False,
)

ListResourceTagsResponseTypeDef = TypedDict(
    "ListResourceTagsResponseTypeDef",
    {"Tags": List["TagTypeDef"], "NextMarker": str, "Truncated": bool},
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

ReEncryptResponseTypeDef = TypedDict(
    "ReEncryptResponseTypeDef",
    {
        "CiphertextBlob": Union[bytes, IO[bytes]],
        "SourceKeyId": str,
        "KeyId": str,
        "SourceEncryptionAlgorithm": EncryptionAlgorithmSpec,
        "DestinationEncryptionAlgorithm": EncryptionAlgorithmSpec,
    },
    total=False,
)

ScheduleKeyDeletionResponseTypeDef = TypedDict(
    "ScheduleKeyDeletionResponseTypeDef", {"KeyId": str, "DeletionDate": datetime}, total=False
)

SignResponseTypeDef = TypedDict(
    "SignResponseTypeDef",
    {"KeyId": str, "Signature": Union[bytes, IO[bytes]], "SigningAlgorithm": SigningAlgorithmSpec},
    total=False,
)

VerifyResponseTypeDef = TypedDict(
    "VerifyResponseTypeDef",
    {"KeyId": str, "SignatureValid": bool, "SigningAlgorithm": SigningAlgorithmSpec},
    total=False,
)
