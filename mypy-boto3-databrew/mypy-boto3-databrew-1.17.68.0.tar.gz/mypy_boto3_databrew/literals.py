"""
Type annotations for databrew service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/literals.html)

Usage::

    ```python
    from mypy_boto3_databrew.literals import CompressionFormat

    data: CompressionFormat = "BROTLI"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CompressionFormat",
    "EncryptionMode",
    "InputFormat",
    "JobRunState",
    "JobType",
    "ListDatasetsPaginatorName",
    "ListJobRunsPaginatorName",
    "ListJobsPaginatorName",
    "ListProjectsPaginatorName",
    "ListRecipeVersionsPaginatorName",
    "ListRecipesPaginatorName",
    "ListSchedulesPaginatorName",
    "LogSubscription",
    "Order",
    "OrderedBy",
    "OutputFormat",
    "ParameterType",
    "SampleMode",
    "SampleType",
    "SessionStatus",
    "Source",
)


CompressionFormat = Literal[
    "BROTLI", "BZIP2", "DEFLATE", "GZIP", "LZ4", "LZO", "SNAPPY", "ZLIB", "ZSTD"
]
EncryptionMode = Literal["SSE-KMS", "SSE-S3"]
InputFormat = Literal["CSV", "EXCEL", "JSON", "PARQUET"]
JobRunState = Literal[
    "FAILED", "RUNNING", "STARTING", "STOPPED", "STOPPING", "SUCCEEDED", "TIMEOUT"
]
JobType = Literal["PROFILE", "RECIPE"]
ListDatasetsPaginatorName = Literal["list_datasets"]
ListJobRunsPaginatorName = Literal["list_job_runs"]
ListJobsPaginatorName = Literal["list_jobs"]
ListProjectsPaginatorName = Literal["list_projects"]
ListRecipeVersionsPaginatorName = Literal["list_recipe_versions"]
ListRecipesPaginatorName = Literal["list_recipes"]
ListSchedulesPaginatorName = Literal["list_schedules"]
LogSubscription = Literal["DISABLE", "ENABLE"]
Order = Literal["ASCENDING", "DESCENDING"]
OrderedBy = Literal["LAST_MODIFIED_DATE"]
OutputFormat = Literal["AVRO", "CSV", "GLUEPARQUET", "JSON", "ORC", "PARQUET", "XML"]
ParameterType = Literal["Datetime", "Number", "String"]
SampleMode = Literal["CUSTOM_ROWS", "FULL_DATASET"]
SampleType = Literal["FIRST_N", "LAST_N", "RANDOM"]
SessionStatus = Literal[
    "ASSIGNED",
    "FAILED",
    "INITIALIZING",
    "PROVISIONING",
    "READY",
    "RECYCLING",
    "ROTATING",
    "TERMINATED",
    "TERMINATING",
    "UPDATING",
]
Source = Literal["DATA-CATALOG", "DATABASE", "S3"]
