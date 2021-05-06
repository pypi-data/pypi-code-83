"""
Type annotations for databrew service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_databrew/type_defs.html)

Usage::

    ```python
    from mypy_boto3_databrew.type_defs import BatchDeleteRecipeVersionResponseTypeDef

    data: BatchDeleteRecipeVersionResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_databrew.literals import (
    CompressionFormat,
    EncryptionMode,
    InputFormat,
    JobRunState,
    JobType,
    LogSubscription,
    Order,
    OutputFormat,
    ParameterType,
    SampleMode,
    SampleType,
    SessionStatus,
    Source,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "BatchDeleteRecipeVersionResponseTypeDef",
    "ConditionExpressionTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateProfileJobResponseTypeDef",
    "CreateProjectResponseTypeDef",
    "CreateRecipeJobResponseTypeDef",
    "CreateRecipeResponseTypeDef",
    "CreateScheduleResponseTypeDef",
    "CsvOptionsTypeDef",
    "CsvOutputOptionsTypeDef",
    "DataCatalogInputDefinitionTypeDef",
    "DatabaseInputDefinitionTypeDef",
    "DatasetParameterTypeDef",
    "DatasetTypeDef",
    "DatetimeOptionsTypeDef",
    "DeleteDatasetResponseTypeDef",
    "DeleteJobResponseTypeDef",
    "DeleteProjectResponseTypeDef",
    "DeleteRecipeVersionResponseTypeDef",
    "DeleteScheduleResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeJobResponseTypeDef",
    "DescribeJobRunResponseTypeDef",
    "DescribeProjectResponseTypeDef",
    "DescribeRecipeResponseTypeDef",
    "DescribeScheduleResponseTypeDef",
    "ExcelOptionsTypeDef",
    "FilesLimitTypeDef",
    "FilterExpressionTypeDef",
    "FormatOptionsTypeDef",
    "InputTypeDef",
    "JobRunTypeDef",
    "JobSampleTypeDef",
    "JobTypeDef",
    "JsonOptionsTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListJobRunsResponseTypeDef",
    "ListJobsResponseTypeDef",
    "ListProjectsResponseTypeDef",
    "ListRecipeVersionsResponseTypeDef",
    "ListRecipesResponseTypeDef",
    "ListSchedulesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "OutputFormatOptionsTypeDef",
    "OutputTypeDef",
    "PaginatorConfigTypeDef",
    "PathOptionsTypeDef",
    "ProjectTypeDef",
    "PublishRecipeResponseTypeDef",
    "RecipeActionTypeDef",
    "RecipeReferenceTypeDef",
    "RecipeStepTypeDef",
    "RecipeTypeDef",
    "RecipeVersionErrorDetailTypeDef",
    "ResponseMetadata",
    "S3LocationTypeDef",
    "SampleTypeDef",
    "ScheduleTypeDef",
    "SendProjectSessionActionResponseTypeDef",
    "StartJobRunResponseTypeDef",
    "StartProjectSessionResponseTypeDef",
    "StopJobRunResponseTypeDef",
    "UpdateDatasetResponseTypeDef",
    "UpdateProfileJobResponseTypeDef",
    "UpdateProjectResponseTypeDef",
    "UpdateRecipeJobResponseTypeDef",
    "UpdateRecipeResponseTypeDef",
    "UpdateScheduleResponseTypeDef",
    "ViewFrameTypeDef",
)


class _RequiredBatchDeleteRecipeVersionResponseTypeDef(TypedDict):
    Name: str


class BatchDeleteRecipeVersionResponseTypeDef(
    _RequiredBatchDeleteRecipeVersionResponseTypeDef, total=False
):
    Errors: List["RecipeVersionErrorDetailTypeDef"]


class _RequiredConditionExpressionTypeDef(TypedDict):
    Condition: str
    TargetColumn: str


class ConditionExpressionTypeDef(_RequiredConditionExpressionTypeDef, total=False):
    Value: str


class CreateDatasetResponseTypeDef(TypedDict):
    Name: str


class CreateProfileJobResponseTypeDef(TypedDict):
    Name: str


class CreateProjectResponseTypeDef(TypedDict):
    Name: str


class CreateRecipeJobResponseTypeDef(TypedDict):
    Name: str


class CreateRecipeResponseTypeDef(TypedDict):
    Name: str


class CreateScheduleResponseTypeDef(TypedDict):
    Name: str


class CsvOptionsTypeDef(TypedDict, total=False):
    Delimiter: str
    HeaderRow: bool


class CsvOutputOptionsTypeDef(TypedDict, total=False):
    Delimiter: str


class _RequiredDataCatalogInputDefinitionTypeDef(TypedDict):
    DatabaseName: str
    TableName: str


class DataCatalogInputDefinitionTypeDef(_RequiredDataCatalogInputDefinitionTypeDef, total=False):
    CatalogId: str
    TempDirectory: "S3LocationTypeDef"


class _RequiredDatabaseInputDefinitionTypeDef(TypedDict):
    GlueConnectionName: str
    DatabaseTableName: str


class DatabaseInputDefinitionTypeDef(_RequiredDatabaseInputDefinitionTypeDef, total=False):
    TempDirectory: "S3LocationTypeDef"


_RequiredDatasetParameterTypeDef = TypedDict(
    "_RequiredDatasetParameterTypeDef", {"Name": str, "Type": ParameterType}
)
_OptionalDatasetParameterTypeDef = TypedDict(
    "_OptionalDatasetParameterTypeDef",
    {
        "DatetimeOptions": "DatetimeOptionsTypeDef",
        "CreateColumn": bool,
        "Filter": "FilterExpressionTypeDef",
    },
    total=False,
)


class DatasetParameterTypeDef(_RequiredDatasetParameterTypeDef, _OptionalDatasetParameterTypeDef):
    pass


class _RequiredDatasetTypeDef(TypedDict):
    Name: str
    Input: "InputTypeDef"


class DatasetTypeDef(_RequiredDatasetTypeDef, total=False):
    AccountId: str
    CreatedBy: str
    CreateDate: datetime
    Format: InputFormat
    FormatOptions: "FormatOptionsTypeDef"
    LastModifiedDate: datetime
    LastModifiedBy: str
    Source: Source
    PathOptions: "PathOptionsTypeDef"
    Tags: Dict[str, str]
    ResourceArn: str


class _RequiredDatetimeOptionsTypeDef(TypedDict):
    Format: str


class DatetimeOptionsTypeDef(_RequiredDatetimeOptionsTypeDef, total=False):
    TimezoneOffset: str
    LocaleCode: str


class DeleteDatasetResponseTypeDef(TypedDict):
    Name: str


class DeleteJobResponseTypeDef(TypedDict):
    Name: str


class DeleteProjectResponseTypeDef(TypedDict):
    Name: str


class DeleteRecipeVersionResponseTypeDef(TypedDict):
    Name: str
    RecipeVersion: str


class DeleteScheduleResponseTypeDef(TypedDict):
    Name: str


class _RequiredDescribeDatasetResponseTypeDef(TypedDict):
    Name: str
    Input: "InputTypeDef"


class DescribeDatasetResponseTypeDef(_RequiredDescribeDatasetResponseTypeDef, total=False):
    CreatedBy: str
    CreateDate: datetime
    Format: InputFormat
    FormatOptions: "FormatOptionsTypeDef"
    LastModifiedDate: datetime
    LastModifiedBy: str
    Source: Source
    PathOptions: "PathOptionsTypeDef"
    Tags: Dict[str, str]
    ResourceArn: str


_RequiredDescribeJobResponseTypeDef = TypedDict(
    "_RequiredDescribeJobResponseTypeDef", {"Name": str}
)
_OptionalDescribeJobResponseTypeDef = TypedDict(
    "_OptionalDescribeJobResponseTypeDef",
    {
        "CreateDate": datetime,
        "CreatedBy": str,
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionMode,
        "Type": JobType,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "LogSubscription": LogSubscription,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": List["OutputTypeDef"],
        "ProjectName": str,
        "RecipeReference": "RecipeReferenceTypeDef",
        "ResourceArn": str,
        "RoleArn": str,
        "Tags": Dict[str, str],
        "Timeout": int,
        "JobSample": "JobSampleTypeDef",
    },
    total=False,
)


class DescribeJobResponseTypeDef(
    _RequiredDescribeJobResponseTypeDef, _OptionalDescribeJobResponseTypeDef
):
    pass


class _RequiredDescribeJobRunResponseTypeDef(TypedDict):
    JobName: str


class DescribeJobRunResponseTypeDef(_RequiredDescribeJobRunResponseTypeDef, total=False):
    Attempt: int
    CompletedOn: datetime
    DatasetName: str
    ErrorMessage: str
    ExecutionTime: int
    RunId: str
    State: JobRunState
    LogSubscription: LogSubscription
    LogGroupName: str
    Outputs: List["OutputTypeDef"]
    RecipeReference: "RecipeReferenceTypeDef"
    StartedBy: str
    StartedOn: datetime
    JobSample: "JobSampleTypeDef"


class _RequiredDescribeProjectResponseTypeDef(TypedDict):
    Name: str


class DescribeProjectResponseTypeDef(_RequiredDescribeProjectResponseTypeDef, total=False):
    CreateDate: datetime
    CreatedBy: str
    DatasetName: str
    LastModifiedDate: datetime
    LastModifiedBy: str
    RecipeName: str
    ResourceArn: str
    Sample: "SampleTypeDef"
    RoleArn: str
    Tags: Dict[str, str]
    SessionStatus: SessionStatus
    OpenedBy: str
    OpenDate: datetime


class _RequiredDescribeRecipeResponseTypeDef(TypedDict):
    Name: str


class DescribeRecipeResponseTypeDef(_RequiredDescribeRecipeResponseTypeDef, total=False):
    CreatedBy: str
    CreateDate: datetime
    LastModifiedBy: str
    LastModifiedDate: datetime
    ProjectName: str
    PublishedBy: str
    PublishedDate: datetime
    Description: str
    Steps: List["RecipeStepTypeDef"]
    Tags: Dict[str, str]
    ResourceArn: str
    RecipeVersion: str


class _RequiredDescribeScheduleResponseTypeDef(TypedDict):
    Name: str


class DescribeScheduleResponseTypeDef(_RequiredDescribeScheduleResponseTypeDef, total=False):
    CreateDate: datetime
    CreatedBy: str
    JobNames: List[str]
    LastModifiedBy: str
    LastModifiedDate: datetime
    ResourceArn: str
    CronExpression: str
    Tags: Dict[str, str]


class ExcelOptionsTypeDef(TypedDict, total=False):
    SheetNames: List[str]
    SheetIndexes: List[int]
    HeaderRow: bool


class _RequiredFilesLimitTypeDef(TypedDict):
    MaxFiles: int


class FilesLimitTypeDef(_RequiredFilesLimitTypeDef, total=False):
    OrderedBy: Literal["LAST_MODIFIED_DATE"]
    Order: Order


class FilterExpressionTypeDef(TypedDict):
    Expression: str
    ValuesMap: Dict[str, str]


class FormatOptionsTypeDef(TypedDict, total=False):
    Json: "JsonOptionsTypeDef"
    Excel: "ExcelOptionsTypeDef"
    Csv: "CsvOptionsTypeDef"


class InputTypeDef(TypedDict, total=False):
    S3InputDefinition: "S3LocationTypeDef"
    DataCatalogInputDefinition: "DataCatalogInputDefinitionTypeDef"
    DatabaseInputDefinition: "DatabaseInputDefinitionTypeDef"


class JobRunTypeDef(TypedDict, total=False):
    Attempt: int
    CompletedOn: datetime
    DatasetName: str
    ErrorMessage: str
    ExecutionTime: int
    JobName: str
    RunId: str
    State: JobRunState
    LogSubscription: LogSubscription
    LogGroupName: str
    Outputs: List["OutputTypeDef"]
    RecipeReference: "RecipeReferenceTypeDef"
    StartedBy: str
    StartedOn: datetime
    JobSample: "JobSampleTypeDef"


class JobSampleTypeDef(TypedDict, total=False):
    Mode: SampleMode
    Size: int


_RequiredJobTypeDef = TypedDict("_RequiredJobTypeDef", {"Name": str})
_OptionalJobTypeDef = TypedDict(
    "_OptionalJobTypeDef",
    {
        "AccountId": str,
        "CreatedBy": str,
        "CreateDate": datetime,
        "DatasetName": str,
        "EncryptionKeyArn": str,
        "EncryptionMode": EncryptionMode,
        "Type": JobType,
        "LastModifiedBy": str,
        "LastModifiedDate": datetime,
        "LogSubscription": LogSubscription,
        "MaxCapacity": int,
        "MaxRetries": int,
        "Outputs": List["OutputTypeDef"],
        "ProjectName": str,
        "RecipeReference": "RecipeReferenceTypeDef",
        "ResourceArn": str,
        "RoleArn": str,
        "Timeout": int,
        "Tags": Dict[str, str],
        "JobSample": "JobSampleTypeDef",
    },
    total=False,
)


class JobTypeDef(_RequiredJobTypeDef, _OptionalJobTypeDef):
    pass


class JsonOptionsTypeDef(TypedDict, total=False):
    MultiLine: bool


class _RequiredListDatasetsResponseTypeDef(TypedDict):
    Datasets: List["DatasetTypeDef"]


class ListDatasetsResponseTypeDef(_RequiredListDatasetsResponseTypeDef, total=False):
    NextToken: str


class _RequiredListJobRunsResponseTypeDef(TypedDict):
    JobRuns: List["JobRunTypeDef"]


class ListJobRunsResponseTypeDef(_RequiredListJobRunsResponseTypeDef, total=False):
    NextToken: str


class _RequiredListJobsResponseTypeDef(TypedDict):
    Jobs: List["JobTypeDef"]


class ListJobsResponseTypeDef(_RequiredListJobsResponseTypeDef, total=False):
    NextToken: str


class _RequiredListProjectsResponseTypeDef(TypedDict):
    Projects: List["ProjectTypeDef"]


class ListProjectsResponseTypeDef(_RequiredListProjectsResponseTypeDef, total=False):
    NextToken: str


class _RequiredListRecipeVersionsResponseTypeDef(TypedDict):
    Recipes: List["RecipeTypeDef"]


class ListRecipeVersionsResponseTypeDef(_RequiredListRecipeVersionsResponseTypeDef, total=False):
    NextToken: str


class _RequiredListRecipesResponseTypeDef(TypedDict):
    Recipes: List["RecipeTypeDef"]


class ListRecipesResponseTypeDef(_RequiredListRecipesResponseTypeDef, total=False):
    NextToken: str


class _RequiredListSchedulesResponseTypeDef(TypedDict):
    Schedules: List["ScheduleTypeDef"]


class ListSchedulesResponseTypeDef(_RequiredListSchedulesResponseTypeDef, total=False):
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: Dict[str, str]


class OutputFormatOptionsTypeDef(TypedDict, total=False):
    Csv: "CsvOutputOptionsTypeDef"


class OutputTypeDef(TypedDict):
    CompressionFormat: CompressionFormat
    Format: OutputFormat
    PartitionColumns: List[str]
    Location: "S3LocationTypeDef"
    Overwrite: bool
    FormatOptions: "OutputFormatOptionsTypeDef"
    ResponseMetadata: "ResponseMetadata"


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PathOptionsTypeDef(TypedDict, total=False):
    LastModifiedDateCondition: "FilterExpressionTypeDef"
    FilesLimit: "FilesLimitTypeDef"
    Parameters: Dict[str, "DatasetParameterTypeDef"]


class _RequiredProjectTypeDef(TypedDict):
    Name: str
    RecipeName: str


class ProjectTypeDef(_RequiredProjectTypeDef, total=False):
    AccountId: str
    CreateDate: datetime
    CreatedBy: str
    DatasetName: str
    LastModifiedDate: datetime
    LastModifiedBy: str
    ResourceArn: str
    Sample: "SampleTypeDef"
    Tags: Dict[str, str]
    RoleArn: str
    OpenedBy: str
    OpenDate: datetime


class PublishRecipeResponseTypeDef(TypedDict):
    Name: str


class _RequiredRecipeActionTypeDef(TypedDict):
    Operation: str


class RecipeActionTypeDef(_RequiredRecipeActionTypeDef, total=False):
    Parameters: Dict[str, str]


class _RequiredRecipeReferenceTypeDef(TypedDict):
    Name: str


class RecipeReferenceTypeDef(_RequiredRecipeReferenceTypeDef, total=False):
    RecipeVersion: str


class _RequiredRecipeStepTypeDef(TypedDict):
    Action: "RecipeActionTypeDef"


class RecipeStepTypeDef(_RequiredRecipeStepTypeDef, total=False):
    ConditionExpressions: List["ConditionExpressionTypeDef"]


class _RequiredRecipeTypeDef(TypedDict):
    Name: str


class RecipeTypeDef(_RequiredRecipeTypeDef, total=False):
    CreatedBy: str
    CreateDate: datetime
    LastModifiedBy: str
    LastModifiedDate: datetime
    ProjectName: str
    PublishedBy: str
    PublishedDate: datetime
    Description: str
    ResourceArn: str
    Steps: List["RecipeStepTypeDef"]
    Tags: Dict[str, str]
    RecipeVersion: str


class RecipeVersionErrorDetailTypeDef(TypedDict, total=False):
    ErrorCode: str
    ErrorMessage: str
    RecipeVersion: str


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class _RequiredS3LocationTypeDef(TypedDict):
    Bucket: str


class S3LocationTypeDef(_RequiredS3LocationTypeDef, total=False):
    Key: str


_RequiredSampleTypeDef = TypedDict("_RequiredSampleTypeDef", {"Type": SampleType})
_OptionalSampleTypeDef = TypedDict("_OptionalSampleTypeDef", {"Size": int}, total=False)


class SampleTypeDef(_RequiredSampleTypeDef, _OptionalSampleTypeDef):
    pass


class _RequiredScheduleTypeDef(TypedDict):
    Name: str


class ScheduleTypeDef(_RequiredScheduleTypeDef, total=False):
    AccountId: str
    CreatedBy: str
    CreateDate: datetime
    JobNames: List[str]
    LastModifiedBy: str
    LastModifiedDate: datetime
    ResourceArn: str
    CronExpression: str
    Tags: Dict[str, str]


class _RequiredSendProjectSessionActionResponseTypeDef(TypedDict):
    Name: str


class SendProjectSessionActionResponseTypeDef(
    _RequiredSendProjectSessionActionResponseTypeDef, total=False
):
    Result: str
    ActionId: int


class StartJobRunResponseTypeDef(TypedDict):
    RunId: str


class _RequiredStartProjectSessionResponseTypeDef(TypedDict):
    Name: str


class StartProjectSessionResponseTypeDef(_RequiredStartProjectSessionResponseTypeDef, total=False):
    ClientSessionId: str


class StopJobRunResponseTypeDef(TypedDict):
    RunId: str


class UpdateDatasetResponseTypeDef(TypedDict):
    Name: str


class UpdateProfileJobResponseTypeDef(TypedDict):
    Name: str


class _RequiredUpdateProjectResponseTypeDef(TypedDict):
    Name: str


class UpdateProjectResponseTypeDef(_RequiredUpdateProjectResponseTypeDef, total=False):
    LastModifiedDate: datetime


class UpdateRecipeJobResponseTypeDef(TypedDict):
    Name: str


class UpdateRecipeResponseTypeDef(TypedDict):
    Name: str


class UpdateScheduleResponseTypeDef(TypedDict):
    Name: str


class _RequiredViewFrameTypeDef(TypedDict):
    StartColumnIndex: int


class ViewFrameTypeDef(_RequiredViewFrameTypeDef, total=False):
    ColumnRange: int
    HiddenColumns: List[str]
