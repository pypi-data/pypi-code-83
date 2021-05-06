"""
Type annotations for healthlake service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_healthlake/type_defs.html)

Usage::

    ```python
    from mypy_boto3_healthlake.type_defs import CreateFHIRDatastoreResponseTypeDef

    data: CreateFHIRDatastoreResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_healthlake.literals import DatastoreStatus, JobStatus

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateFHIRDatastoreResponseTypeDef",
    "DatastoreFilterTypeDef",
    "DatastorePropertiesTypeDef",
    "DeleteFHIRDatastoreResponseTypeDef",
    "DescribeFHIRDatastoreResponseTypeDef",
    "DescribeFHIRExportJobResponseTypeDef",
    "DescribeFHIRImportJobResponseTypeDef",
    "ExportJobPropertiesTypeDef",
    "ImportJobPropertiesTypeDef",
    "InputDataConfigTypeDef",
    "ListFHIRDatastoresResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PreloadDataConfigTypeDef",
    "StartFHIRExportJobResponseTypeDef",
    "StartFHIRImportJobResponseTypeDef",
)


class CreateFHIRDatastoreResponseTypeDef(TypedDict):
    DatastoreId: str
    DatastoreArn: str
    DatastoreStatus: DatastoreStatus
    DatastoreEndpoint: str


class DatastoreFilterTypeDef(TypedDict, total=False):
    DatastoreName: str
    DatastoreStatus: DatastoreStatus
    CreatedBefore: datetime
    CreatedAfter: datetime


class _RequiredDatastorePropertiesTypeDef(TypedDict):
    DatastoreId: str
    DatastoreArn: str
    DatastoreStatus: DatastoreStatus
    DatastoreTypeVersion: Literal["R4"]
    DatastoreEndpoint: str


class DatastorePropertiesTypeDef(_RequiredDatastorePropertiesTypeDef, total=False):
    DatastoreName: str
    CreatedAt: datetime
    PreloadDataConfig: "PreloadDataConfigTypeDef"


class DeleteFHIRDatastoreResponseTypeDef(TypedDict):
    DatastoreId: str
    DatastoreArn: str
    DatastoreStatus: DatastoreStatus
    DatastoreEndpoint: str


class DescribeFHIRDatastoreResponseTypeDef(TypedDict):
    DatastoreProperties: "DatastorePropertiesTypeDef"


class DescribeFHIRExportJobResponseTypeDef(TypedDict):
    ExportJobProperties: "ExportJobPropertiesTypeDef"


class DescribeFHIRImportJobResponseTypeDef(TypedDict):
    ImportJobProperties: "ImportJobPropertiesTypeDef"


class _RequiredExportJobPropertiesTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatus
    SubmitTime: datetime
    DatastoreId: str
    OutputDataConfig: "OutputDataConfigTypeDef"


class ExportJobPropertiesTypeDef(_RequiredExportJobPropertiesTypeDef, total=False):
    JobName: str
    EndTime: datetime
    DataAccessRoleArn: str
    Message: str


class _RequiredImportJobPropertiesTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatus
    SubmitTime: datetime
    DatastoreId: str
    InputDataConfig: "InputDataConfigTypeDef"


class ImportJobPropertiesTypeDef(_RequiredImportJobPropertiesTypeDef, total=False):
    JobName: str
    EndTime: datetime
    DataAccessRoleArn: str
    Message: str


class InputDataConfigTypeDef(TypedDict, total=False):
    S3Uri: str


class _RequiredListFHIRDatastoresResponseTypeDef(TypedDict):
    DatastorePropertiesList: List["DatastorePropertiesTypeDef"]


class ListFHIRDatastoresResponseTypeDef(_RequiredListFHIRDatastoresResponseTypeDef, total=False):
    NextToken: str


class OutputDataConfigTypeDef(TypedDict, total=False):
    S3Uri: str


class PreloadDataConfigTypeDef(TypedDict):
    PreloadDataType: Literal["SYNTHEA"]


class _RequiredStartFHIRExportJobResponseTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatus


class StartFHIRExportJobResponseTypeDef(_RequiredStartFHIRExportJobResponseTypeDef, total=False):
    DatastoreId: str


class _RequiredStartFHIRImportJobResponseTypeDef(TypedDict):
    JobId: str
    JobStatus: JobStatus


class StartFHIRImportJobResponseTypeDef(_RequiredStartFHIRImportJobResponseTypeDef, total=False):
    DatastoreId: str
