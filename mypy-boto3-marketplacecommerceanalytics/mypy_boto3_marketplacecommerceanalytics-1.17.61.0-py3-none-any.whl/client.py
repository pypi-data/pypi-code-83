"""
Main interface for marketplacecommerceanalytics service client

Usage::

    ```python
    import boto3
    from mypy_boto3_marketplacecommerceanalytics import MarketplaceCommerceAnalyticsClient

    client: MarketplaceCommerceAnalyticsClient = boto3.client("marketplacecommerceanalytics")
    ```
"""
from datetime import datetime
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from mypy_boto3_marketplacecommerceanalytics.literals import DataSetType, SupportDataSetType
from mypy_boto3_marketplacecommerceanalytics.type_defs import (
    GenerateDataSetResultTypeDef,
    StartSupportDataExportResultTypeDef,
)

__all__ = ("MarketplaceCommerceAnalyticsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    MarketplaceCommerceAnalyticsException: Type[BotocoreClientError]


class MarketplaceCommerceAnalyticsClient:
    """
    [MarketplaceCommerceAnalytics.Client documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Client.can_paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.can_paginate)
        """

    def generate_data_set(
        self,
        dataSetType: DataSetType,
        dataSetPublicationDate: datetime,
        roleNameArn: str,
        destinationS3BucketName: str,
        snsTopicArn: str,
        destinationS3Prefix: str = None,
        customerDefinedValues: Dict[str, str] = None,
    ) -> GenerateDataSetResultTypeDef:
        """
        [Client.generate_data_set documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.generate_data_set)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Client.generate_presigned_url documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.generate_presigned_url)
        """

    def start_support_data_export(
        self,
        dataSetType: SupportDataSetType,
        fromDate: datetime,
        roleNameArn: str,
        destinationS3BucketName: str,
        snsTopicArn: str,
        destinationS3Prefix: str = None,
        customerDefinedValues: Dict[str, str] = None,
    ) -> StartSupportDataExportResultTypeDef:
        """
        [Client.start_support_data_export documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/marketplacecommerceanalytics.html#MarketplaceCommerceAnalytics.Client.start_support_data_export)
        """
