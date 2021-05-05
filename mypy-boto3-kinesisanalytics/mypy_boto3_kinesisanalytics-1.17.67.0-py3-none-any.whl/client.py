"""
Type annotations for kinesisanalytics service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_kinesisanalytics import KinesisAnalyticsClient

    client: KinesisAnalyticsClient = boto3.client("kinesisanalytics")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_kinesisanalytics.type_defs import (
    ApplicationUpdateTypeDef,
    CloudWatchLoggingOptionTypeDef,
    CreateApplicationResponseTypeDef,
    DescribeApplicationResponseTypeDef,
    DiscoverInputSchemaResponseTypeDef,
    InputConfigurationTypeDef,
    InputProcessingConfigurationTypeDef,
    InputStartingPositionConfigurationTypeDef,
    InputTypeDef,
    ListApplicationsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    OutputTypeDef,
    ReferenceDataSourceTypeDef,
    S3ConfigurationTypeDef,
    TagTypeDef,
)

__all__ = ("KinesisAnalyticsClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    CodeValidationException: Type[BotocoreClientError]
    ConcurrentModificationException: Type[BotocoreClientError]
    InvalidApplicationConfigurationException: Type[BotocoreClientError]
    InvalidArgumentException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ResourceProvisionedThroughputExceededException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]
    UnableToDetectSchemaException: Type[BotocoreClientError]
    UnsupportedOperationException: Type[BotocoreClientError]


class KinesisAnalyticsClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def add_application_cloud_watch_logging_option(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        CloudWatchLoggingOption: CloudWatchLoggingOptionTypeDef,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_cloud_watch_logging_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#add-application-cloud-watch-logging-option)
        """

    def add_application_input(
        self, ApplicationName: str, CurrentApplicationVersionId: int, Input: InputTypeDef
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_input)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#add-application-input)
        """

    def add_application_input_processing_configuration(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        InputId: str,
        InputProcessingConfiguration: "InputProcessingConfigurationTypeDef",
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_input_processing_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#add-application-input-processing-configuration)
        """

    def add_application_output(
        self, ApplicationName: str, CurrentApplicationVersionId: int, Output: OutputTypeDef
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#add-application-output)
        """

    def add_application_reference_data_source(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ReferenceDataSource: ReferenceDataSourceTypeDef,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.add_application_reference_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#add-application-reference-data-source)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#can-paginate)
        """

    def create_application(
        self,
        ApplicationName: str,
        ApplicationDescription: str = None,
        Inputs: List[InputTypeDef] = None,
        Outputs: List[OutputTypeDef] = None,
        CloudWatchLoggingOptions: List[CloudWatchLoggingOptionTypeDef] = None,
        ApplicationCode: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.create_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#create-application)
        """

    def delete_application(self, ApplicationName: str, CreateTimestamp: datetime) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#delete-application)
        """

    def delete_application_cloud_watch_logging_option(
        self, ApplicationName: str, CurrentApplicationVersionId: int, CloudWatchLoggingOptionId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_cloud_watch_logging_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#delete-application-cloud-watch-logging-option)
        """

    def delete_application_input_processing_configuration(
        self, ApplicationName: str, CurrentApplicationVersionId: int, InputId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_input_processing_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#delete-application-input-processing-configuration)
        """

    def delete_application_output(
        self, ApplicationName: str, CurrentApplicationVersionId: int, OutputId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#delete-application-output)
        """

    def delete_application_reference_data_source(
        self, ApplicationName: str, CurrentApplicationVersionId: int, ReferenceId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.delete_application_reference_data_source)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#delete-application-reference-data-source)
        """

    def describe_application(self, ApplicationName: str) -> DescribeApplicationResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.describe_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#describe-application)
        """

    def discover_input_schema(
        self,
        ResourceARN: str = None,
        RoleARN: str = None,
        InputStartingPositionConfiguration: "InputStartingPositionConfigurationTypeDef" = None,
        S3Configuration: S3ConfigurationTypeDef = None,
        InputProcessingConfiguration: "InputProcessingConfigurationTypeDef" = None,
    ) -> DiscoverInputSchemaResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.discover_input_schema)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#discover-input-schema)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#generate-presigned-url)
        """

    def list_applications(
        self, Limit: int = None, ExclusiveStartApplicationName: str = None
    ) -> ListApplicationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.list_applications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#list-applications)
        """

    def list_tags_for_resource(self, ResourceARN: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#list-tags-for-resource)
        """

    def start_application(
        self, ApplicationName: str, InputConfigurations: List[InputConfigurationTypeDef]
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.start_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#start-application)
        """

    def stop_application(self, ApplicationName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.stop_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#stop-application)
        """

    def tag_resource(self, ResourceARN: str, Tags: List["TagTypeDef"]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#tag-resource)
        """

    def untag_resource(self, ResourceARN: str, TagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#untag-resource)
        """

    def update_application(
        self,
        ApplicationName: str,
        CurrentApplicationVersionId: int,
        ApplicationUpdate: ApplicationUpdateTypeDef,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/kinesisanalytics.html#KinesisAnalytics.Client.update_application)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kinesisanalytics/client.html#update-application)
        """
