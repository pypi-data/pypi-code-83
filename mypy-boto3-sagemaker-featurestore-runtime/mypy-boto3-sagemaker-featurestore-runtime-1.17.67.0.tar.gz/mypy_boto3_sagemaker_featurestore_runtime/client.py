"""
Type annotations for sagemaker-featurestore-runtime service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_sagemaker_featurestore_runtime import SagemakerFeatureStoreRuntimeClient

    client: SagemakerFeatureStoreRuntimeClient = boto3.client("sagemaker-featurestore-runtime")
    ```
"""
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_sagemaker_featurestore_runtime.type_defs import (
    FeatureValueTypeDef,
    GetRecordResponseTypeDef,
)

__all__ = ("SagemakerFeatureStoreRuntimeClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AccessForbidden: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalFailure: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]
    ServiceUnavailable: Type[BotocoreClientError]
    ValidationError: Type[BotocoreClientError]


class SagemakerFeatureStoreRuntimeClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker-featurestore-runtime.html#SagemakerFeatureStoreRuntime.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker-featurestore-runtime.html#SagemakerFeatureStoreRuntime.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client.html#can-paginate)
        """

    def delete_record(
        self, FeatureGroupName: str, RecordIdentifierValueAsString: str, EventTime: str
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker-featurestore-runtime.html#SagemakerFeatureStoreRuntime.Client.delete_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client.html#delete-record)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker-featurestore-runtime.html#SagemakerFeatureStoreRuntime.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client.html#generate-presigned-url)
        """

    def get_record(
        self,
        FeatureGroupName: str,
        RecordIdentifierValueAsString: str,
        FeatureNames: List[str] = None,
    ) -> GetRecordResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker-featurestore-runtime.html#SagemakerFeatureStoreRuntime.Client.get_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client.html#get-record)
        """

    def put_record(self, FeatureGroupName: str, Record: List["FeatureValueTypeDef"]) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/sagemaker-featurestore-runtime.html#SagemakerFeatureStoreRuntime.Client.put_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_featurestore_runtime/client.html#put-record)
        """
