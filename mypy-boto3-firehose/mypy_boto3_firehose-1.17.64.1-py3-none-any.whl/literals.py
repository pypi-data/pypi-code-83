"""
Type annotations for firehose service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_firehose/literals.html)

Usage::

    ```python
    from mypy_boto3_firehose.literals import CompressionFormat

    data: CompressionFormat = "GZIP"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CompressionFormat",
    "ContentEncoding",
    "DeliveryStreamEncryptionStatus",
    "DeliveryStreamFailureType",
    "DeliveryStreamStatus",
    "DeliveryStreamType",
    "ElasticsearchIndexRotationPeriod",
    "ElasticsearchS3BackupMode",
    "HECEndpointType",
    "HttpEndpointS3BackupMode",
    "KeyType",
    "NoEncryptionConfig",
    "OrcCompression",
    "OrcFormatVersion",
    "ParquetCompression",
    "ParquetWriterVersion",
    "ProcessorParameterName",
    "ProcessorType",
    "RedshiftS3BackupMode",
    "S3BackupMode",
    "SplunkS3BackupMode",
)


CompressionFormat = Literal["GZIP", "HADOOP_SNAPPY", "Snappy", "UNCOMPRESSED", "ZIP"]
ContentEncoding = Literal["GZIP", "NONE"]
DeliveryStreamEncryptionStatus = Literal[
    "DISABLED", "DISABLING", "DISABLING_FAILED", "ENABLED", "ENABLING", "ENABLING_FAILED"
]
DeliveryStreamFailureType = Literal[
    "CREATE_ENI_FAILED",
    "CREATE_KMS_GRANT_FAILED",
    "DELETE_ENI_FAILED",
    "DISABLED_KMS_KEY",
    "ENI_ACCESS_DENIED",
    "INVALID_KMS_KEY",
    "KMS_ACCESS_DENIED",
    "KMS_KEY_NOT_FOUND",
    "KMS_OPT_IN_REQUIRED",
    "RETIRE_KMS_GRANT_FAILED",
    "SECURITY_GROUP_ACCESS_DENIED",
    "SECURITY_GROUP_NOT_FOUND",
    "SUBNET_ACCESS_DENIED",
    "SUBNET_NOT_FOUND",
    "UNKNOWN_ERROR",
]
DeliveryStreamStatus = Literal[
    "ACTIVE", "CREATING", "CREATING_FAILED", "DELETING", "DELETING_FAILED"
]
DeliveryStreamType = Literal["DirectPut", "KinesisStreamAsSource"]
ElasticsearchIndexRotationPeriod = Literal["NoRotation", "OneDay", "OneHour", "OneMonth", "OneWeek"]
ElasticsearchS3BackupMode = Literal["AllDocuments", "FailedDocumentsOnly"]
HECEndpointType = Literal["Event", "Raw"]
HttpEndpointS3BackupMode = Literal["AllData", "FailedDataOnly"]
KeyType = Literal["AWS_OWNED_CMK", "CUSTOMER_MANAGED_CMK"]
NoEncryptionConfig = Literal["NoEncryption"]
OrcCompression = Literal["NONE", "SNAPPY", "ZLIB"]
OrcFormatVersion = Literal["V0_11", "V0_12"]
ParquetCompression = Literal["GZIP", "SNAPPY", "UNCOMPRESSED"]
ParquetWriterVersion = Literal["V1", "V2"]
ProcessorParameterName = Literal[
    "BufferIntervalInSeconds", "BufferSizeInMBs", "LambdaArn", "NumberOfRetries", "RoleArn"
]
ProcessorType = Literal["Lambda"]
RedshiftS3BackupMode = Literal["Disabled", "Enabled"]
S3BackupMode = Literal["Disabled", "Enabled"]
SplunkS3BackupMode = Literal["AllEvents", "FailedEventsOnly"]
