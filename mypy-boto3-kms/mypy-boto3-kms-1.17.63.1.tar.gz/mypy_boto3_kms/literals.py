"""
Type annotations for kms service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kms/literals.html)

Usage::

    ```python
    from mypy_boto3_kms.literals import AlgorithmSpec

    data: AlgorithmSpec = "RSAES_OAEP_SHA_1"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AlgorithmSpec",
    "ConnectionErrorCodeType",
    "ConnectionStateType",
    "CustomerMasterKeySpec",
    "DataKeyPairSpec",
    "DataKeySpec",
    "EncryptionAlgorithmSpec",
    "ExpirationModelType",
    "GrantOperation",
    "KeyManagerType",
    "KeyState",
    "KeyUsageType",
    "ListAliasesPaginatorName",
    "ListGrantsPaginatorName",
    "ListKeyPoliciesPaginatorName",
    "ListKeysPaginatorName",
    "MessageType",
    "OriginType",
    "SigningAlgorithmSpec",
    "WrappingKeySpec",
)


AlgorithmSpec = Literal["RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256", "RSAES_PKCS1_V1_5"]
ConnectionErrorCodeType = Literal[
    "CLUSTER_NOT_FOUND",
    "INSUFFICIENT_CLOUDHSM_HSMS",
    "INTERNAL_ERROR",
    "INVALID_CREDENTIALS",
    "NETWORK_ERRORS",
    "SUBNET_NOT_FOUND",
    "USER_LOCKED_OUT",
    "USER_LOGGED_IN",
    "USER_NOT_FOUND",
]
ConnectionStateType = Literal["CONNECTED", "CONNECTING", "DISCONNECTED", "DISCONNECTING", "FAILED"]
CustomerMasterKeySpec = Literal[
    "ECC_NIST_P256",
    "ECC_NIST_P384",
    "ECC_NIST_P521",
    "ECC_SECG_P256K1",
    "RSA_2048",
    "RSA_3072",
    "RSA_4096",
    "SYMMETRIC_DEFAULT",
]
DataKeyPairSpec = Literal[
    "ECC_NIST_P256",
    "ECC_NIST_P384",
    "ECC_NIST_P521",
    "ECC_SECG_P256K1",
    "RSA_2048",
    "RSA_3072",
    "RSA_4096",
]
DataKeySpec = Literal["AES_128", "AES_256"]
EncryptionAlgorithmSpec = Literal["RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256", "SYMMETRIC_DEFAULT"]
ExpirationModelType = Literal["KEY_MATERIAL_DOES_NOT_EXPIRE", "KEY_MATERIAL_EXPIRES"]
GrantOperation = Literal[
    "CreateGrant",
    "Decrypt",
    "DescribeKey",
    "Encrypt",
    "GenerateDataKey",
    "GenerateDataKeyPair",
    "GenerateDataKeyPairWithoutPlaintext",
    "GenerateDataKeyWithoutPlaintext",
    "GetPublicKey",
    "ReEncryptFrom",
    "ReEncryptTo",
    "RetireGrant",
    "Sign",
    "Verify",
]
KeyManagerType = Literal["AWS", "CUSTOMER"]
KeyState = Literal["Disabled", "Enabled", "PendingDeletion", "PendingImport", "Unavailable"]
KeyUsageType = Literal["ENCRYPT_DECRYPT", "SIGN_VERIFY"]
ListAliasesPaginatorName = Literal["list_aliases"]
ListGrantsPaginatorName = Literal["list_grants"]
ListKeyPoliciesPaginatorName = Literal["list_key_policies"]
ListKeysPaginatorName = Literal["list_keys"]
MessageType = Literal["DIGEST", "RAW"]
OriginType = Literal["AWS_CLOUDHSM", "AWS_KMS", "EXTERNAL"]
SigningAlgorithmSpec = Literal[
    "ECDSA_SHA_256",
    "ECDSA_SHA_384",
    "ECDSA_SHA_512",
    "RSASSA_PKCS1_V1_5_SHA_256",
    "RSASSA_PKCS1_V1_5_SHA_384",
    "RSASSA_PKCS1_V1_5_SHA_512",
    "RSASSA_PSS_SHA_256",
    "RSASSA_PSS_SHA_384",
    "RSASSA_PSS_SHA_512",
]
WrappingKeySpec = Literal["RSA_2048"]
