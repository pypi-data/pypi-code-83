"""
Type annotations for iotanalytics service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotanalytics/literals.html)

Usage::

    ```python
    from mypy_boto3_iotanalytics.literals import ChannelStatus

    data: ChannelStatus = "ACTIVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ChannelStatus",
    "ComputeType",
    "DatasetActionType",
    "DatasetContentState",
    "DatasetStatus",
    "DatastoreStatus",
    "FileFormatType",
    "ListChannelsPaginatorName",
    "ListDatasetContentsPaginatorName",
    "ListDatasetsPaginatorName",
    "ListDatastoresPaginatorName",
    "ListPipelinesPaginatorName",
    "LoggingLevel",
    "ReprocessingStatus",
)


ChannelStatus = Literal["ACTIVE", "CREATING", "DELETING"]
ComputeType = Literal["ACU_1", "ACU_2"]
DatasetActionType = Literal["CONTAINER", "QUERY"]
DatasetContentState = Literal["CREATING", "FAILED", "SUCCEEDED"]
DatasetStatus = Literal["ACTIVE", "CREATING", "DELETING"]
DatastoreStatus = Literal["ACTIVE", "CREATING", "DELETING"]
FileFormatType = Literal["JSON", "PARQUET"]
ListChannelsPaginatorName = Literal["list_channels"]
ListDatasetContentsPaginatorName = Literal["list_dataset_contents"]
ListDatasetsPaginatorName = Literal["list_datasets"]
ListDatastoresPaginatorName = Literal["list_datastores"]
ListPipelinesPaginatorName = Literal["list_pipelines"]
LoggingLevel = Literal["ERROR"]
ReprocessingStatus = Literal["CANCELLED", "FAILED", "RUNNING", "SUCCEEDED"]
