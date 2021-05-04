"""
Type annotations for personalize service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/type_defs.html)

Usage::

    ```python
    from mypy_boto3_personalize.type_defs import AlgorithmImageTypeDef

    data: AlgorithmImageTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_personalize.literals import IngestionMode, TrainingMode

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AlgorithmImageTypeDef",
    "AlgorithmTypeDef",
    "AutoMLConfigTypeDef",
    "AutoMLResultTypeDef",
    "BatchInferenceJobConfigTypeDef",
    "BatchInferenceJobInputTypeDef",
    "BatchInferenceJobOutputTypeDef",
    "BatchInferenceJobSummaryTypeDef",
    "BatchInferenceJobTypeDef",
    "CampaignConfigTypeDef",
    "CampaignSummaryTypeDef",
    "CampaignTypeDef",
    "CampaignUpdateSummaryTypeDef",
    "CategoricalHyperParameterRangeTypeDef",
    "ContinuousHyperParameterRangeTypeDef",
    "CreateBatchInferenceJobResponseTypeDef",
    "CreateCampaignResponseTypeDef",
    "CreateDatasetExportJobResponseTypeDef",
    "CreateDatasetGroupResponseTypeDef",
    "CreateDatasetImportJobResponseTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateEventTrackerResponseTypeDef",
    "CreateFilterResponseTypeDef",
    "CreateSchemaResponseTypeDef",
    "CreateSolutionResponseTypeDef",
    "CreateSolutionVersionResponseTypeDef",
    "DataSourceTypeDef",
    "DatasetExportJobOutputTypeDef",
    "DatasetExportJobSummaryTypeDef",
    "DatasetExportJobTypeDef",
    "DatasetGroupSummaryTypeDef",
    "DatasetGroupTypeDef",
    "DatasetImportJobSummaryTypeDef",
    "DatasetImportJobTypeDef",
    "DatasetSchemaSummaryTypeDef",
    "DatasetSchemaTypeDef",
    "DatasetSummaryTypeDef",
    "DatasetTypeDef",
    "DefaultCategoricalHyperParameterRangeTypeDef",
    "DefaultContinuousHyperParameterRangeTypeDef",
    "DefaultHyperParameterRangesTypeDef",
    "DefaultIntegerHyperParameterRangeTypeDef",
    "DescribeAlgorithmResponseTypeDef",
    "DescribeBatchInferenceJobResponseTypeDef",
    "DescribeCampaignResponseTypeDef",
    "DescribeDatasetExportJobResponseTypeDef",
    "DescribeDatasetGroupResponseTypeDef",
    "DescribeDatasetImportJobResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "DescribeEventTrackerResponseTypeDef",
    "DescribeFeatureTransformationResponseTypeDef",
    "DescribeFilterResponseTypeDef",
    "DescribeRecipeResponseTypeDef",
    "DescribeSchemaResponseTypeDef",
    "DescribeSolutionResponseTypeDef",
    "DescribeSolutionVersionResponseTypeDef",
    "EventTrackerSummaryTypeDef",
    "EventTrackerTypeDef",
    "FeatureTransformationTypeDef",
    "FilterSummaryTypeDef",
    "FilterTypeDef",
    "GetSolutionMetricsResponseTypeDef",
    "HPOConfigTypeDef",
    "HPOObjectiveTypeDef",
    "HPOResourceConfigTypeDef",
    "HyperParameterRangesTypeDef",
    "IntegerHyperParameterRangeTypeDef",
    "ListBatchInferenceJobsResponseTypeDef",
    "ListCampaignsResponseTypeDef",
    "ListDatasetExportJobsResponseTypeDef",
    "ListDatasetGroupsResponseTypeDef",
    "ListDatasetImportJobsResponseTypeDef",
    "ListDatasetsResponseTypeDef",
    "ListEventTrackersResponseTypeDef",
    "ListFiltersResponseTypeDef",
    "ListRecipesResponseTypeDef",
    "ListSchemasResponseTypeDef",
    "ListSolutionVersionsResponseTypeDef",
    "ListSolutionsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "RecipeSummaryTypeDef",
    "RecipeTypeDef",
    "ResponseMetadata",
    "S3DataConfigTypeDef",
    "SolutionConfigTypeDef",
    "SolutionSummaryTypeDef",
    "SolutionTypeDef",
    "SolutionVersionSummaryTypeDef",
    "SolutionVersionTypeDef",
    "TunedHPOParamsTypeDef",
    "UpdateCampaignResponseTypeDef",
)


class _RequiredAlgorithmImageTypeDef(TypedDict):
    dockerURI: str


class AlgorithmImageTypeDef(_RequiredAlgorithmImageTypeDef, total=False):
    name: str


class AlgorithmTypeDef(TypedDict, total=False):
    name: str
    algorithmArn: str
    algorithmImage: "AlgorithmImageTypeDef"
    defaultHyperParameters: Dict[str, str]
    defaultHyperParameterRanges: "DefaultHyperParameterRangesTypeDef"
    defaultResourceConfig: Dict[str, str]
    trainingInputMode: str
    roleArn: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class AutoMLConfigTypeDef(TypedDict, total=False):
    metricName: str
    recipeList: List[str]


class AutoMLResultTypeDef(TypedDict, total=False):
    bestRecipeArn: str


class BatchInferenceJobConfigTypeDef(TypedDict, total=False):
    itemExplorationConfig: Dict[str, str]


class BatchInferenceJobInputTypeDef(TypedDict):
    s3DataSource: "S3DataConfigTypeDef"


class BatchInferenceJobOutputTypeDef(TypedDict):
    s3DataDestination: "S3DataConfigTypeDef"
    ResponseMetadata: "ResponseMetadata"


class BatchInferenceJobSummaryTypeDef(TypedDict, total=False):
    batchInferenceJobArn: str
    jobName: str
    status: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    failureReason: str
    solutionVersionArn: str


class BatchInferenceJobTypeDef(TypedDict, total=False):
    jobName: str
    batchInferenceJobArn: str
    filterArn: str
    failureReason: str
    solutionVersionArn: str
    numResults: int
    jobInput: "BatchInferenceJobInputTypeDef"
    jobOutput: "BatchInferenceJobOutputTypeDef"
    batchInferenceJobConfig: "BatchInferenceJobConfigTypeDef"
    roleArn: str
    status: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class CampaignConfigTypeDef(TypedDict, total=False):
    itemExplorationConfig: Dict[str, str]


class CampaignSummaryTypeDef(TypedDict, total=False):
    name: str
    campaignArn: str
    status: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    failureReason: str


class CampaignTypeDef(TypedDict, total=False):
    name: str
    campaignArn: str
    solutionVersionArn: str
    minProvisionedTPS: int
    campaignConfig: "CampaignConfigTypeDef"
    status: str
    failureReason: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    latestCampaignUpdate: "CampaignUpdateSummaryTypeDef"


class CampaignUpdateSummaryTypeDef(TypedDict, total=False):
    solutionVersionArn: str
    minProvisionedTPS: int
    campaignConfig: "CampaignConfigTypeDef"
    status: str
    failureReason: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class CategoricalHyperParameterRangeTypeDef(TypedDict, total=False):
    name: str
    values: List[str]


class ContinuousHyperParameterRangeTypeDef(TypedDict, total=False):
    name: str
    minValue: float
    maxValue: float


class CreateBatchInferenceJobResponseTypeDef(TypedDict, total=False):
    batchInferenceJobArn: str


class CreateCampaignResponseTypeDef(TypedDict, total=False):
    campaignArn: str


class CreateDatasetExportJobResponseTypeDef(TypedDict, total=False):
    datasetExportJobArn: str


class CreateDatasetGroupResponseTypeDef(TypedDict, total=False):
    datasetGroupArn: str


class CreateDatasetImportJobResponseTypeDef(TypedDict, total=False):
    datasetImportJobArn: str


class CreateDatasetResponseTypeDef(TypedDict, total=False):
    datasetArn: str


class CreateEventTrackerResponseTypeDef(TypedDict, total=False):
    eventTrackerArn: str
    trackingId: str


class CreateFilterResponseTypeDef(TypedDict, total=False):
    filterArn: str


class CreateSchemaResponseTypeDef(TypedDict, total=False):
    schemaArn: str


class CreateSolutionResponseTypeDef(TypedDict, total=False):
    solutionArn: str


class CreateSolutionVersionResponseTypeDef(TypedDict, total=False):
    solutionVersionArn: str


class DataSourceTypeDef(TypedDict, total=False):
    dataLocation: str


class DatasetExportJobOutputTypeDef(TypedDict):
    s3DataDestination: "S3DataConfigTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DatasetExportJobSummaryTypeDef(TypedDict, total=False):
    datasetExportJobArn: str
    jobName: str
    status: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    failureReason: str


class DatasetExportJobTypeDef(TypedDict, total=False):
    jobName: str
    datasetExportJobArn: str
    datasetArn: str
    ingestionMode: IngestionMode
    roleArn: str
    status: str
    jobOutput: "DatasetExportJobOutputTypeDef"
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    failureReason: str


class DatasetGroupSummaryTypeDef(TypedDict, total=False):
    name: str
    datasetGroupArn: str
    status: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    failureReason: str


class DatasetGroupTypeDef(TypedDict, total=False):
    name: str
    datasetGroupArn: str
    status: str
    roleArn: str
    kmsKeyArn: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    failureReason: str


class DatasetImportJobSummaryTypeDef(TypedDict, total=False):
    datasetImportJobArn: str
    jobName: str
    status: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    failureReason: str


class DatasetImportJobTypeDef(TypedDict, total=False):
    jobName: str
    datasetImportJobArn: str
    datasetArn: str
    dataSource: "DataSourceTypeDef"
    roleArn: str
    status: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    failureReason: str


class DatasetSchemaSummaryTypeDef(TypedDict, total=False):
    name: str
    schemaArn: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class DatasetSchemaTypeDef(TypedDict, total=False):
    name: str
    schemaArn: str
    schema: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class DatasetSummaryTypeDef(TypedDict, total=False):
    name: str
    datasetArn: str
    datasetType: str
    status: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class DatasetTypeDef(TypedDict, total=False):
    name: str
    datasetArn: str
    datasetGroupArn: str
    datasetType: str
    schemaArn: str
    status: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class DefaultCategoricalHyperParameterRangeTypeDef(TypedDict, total=False):
    name: str
    values: List[str]
    isTunable: bool


class DefaultContinuousHyperParameterRangeTypeDef(TypedDict, total=False):
    name: str
    minValue: float
    maxValue: float
    isTunable: bool


class DefaultHyperParameterRangesTypeDef(TypedDict, total=False):
    integerHyperParameterRanges: List["DefaultIntegerHyperParameterRangeTypeDef"]
    continuousHyperParameterRanges: List["DefaultContinuousHyperParameterRangeTypeDef"]
    categoricalHyperParameterRanges: List["DefaultCategoricalHyperParameterRangeTypeDef"]


class DefaultIntegerHyperParameterRangeTypeDef(TypedDict, total=False):
    name: str
    minValue: int
    maxValue: int
    isTunable: bool


class DescribeAlgorithmResponseTypeDef(TypedDict, total=False):
    algorithm: "AlgorithmTypeDef"


class DescribeBatchInferenceJobResponseTypeDef(TypedDict, total=False):
    batchInferenceJob: "BatchInferenceJobTypeDef"


class DescribeCampaignResponseTypeDef(TypedDict, total=False):
    campaign: "CampaignTypeDef"


class DescribeDatasetExportJobResponseTypeDef(TypedDict, total=False):
    datasetExportJob: "DatasetExportJobTypeDef"


class DescribeDatasetGroupResponseTypeDef(TypedDict, total=False):
    datasetGroup: "DatasetGroupTypeDef"


class DescribeDatasetImportJobResponseTypeDef(TypedDict, total=False):
    datasetImportJob: "DatasetImportJobTypeDef"


class DescribeDatasetResponseTypeDef(TypedDict, total=False):
    dataset: "DatasetTypeDef"


class DescribeEventTrackerResponseTypeDef(TypedDict, total=False):
    eventTracker: "EventTrackerTypeDef"


class DescribeFeatureTransformationResponseTypeDef(TypedDict, total=False):
    featureTransformation: "FeatureTransformationTypeDef"


DescribeFilterResponseTypeDef = TypedDict(
    "DescribeFilterResponseTypeDef", {"filter": "FilterTypeDef"}, total=False
)


class DescribeRecipeResponseTypeDef(TypedDict, total=False):
    recipe: "RecipeTypeDef"


class DescribeSchemaResponseTypeDef(TypedDict, total=False):
    schema: "DatasetSchemaTypeDef"


class DescribeSolutionResponseTypeDef(TypedDict, total=False):
    solution: "SolutionTypeDef"


class DescribeSolutionVersionResponseTypeDef(TypedDict, total=False):
    solutionVersion: "SolutionVersionTypeDef"


class EventTrackerSummaryTypeDef(TypedDict, total=False):
    name: str
    eventTrackerArn: str
    status: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class EventTrackerTypeDef(TypedDict, total=False):
    name: str
    eventTrackerArn: str
    accountId: str
    trackingId: str
    datasetGroupArn: str
    status: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class FeatureTransformationTypeDef(TypedDict, total=False):
    name: str
    featureTransformationArn: str
    defaultParameters: Dict[str, str]
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    status: str


class FilterSummaryTypeDef(TypedDict, total=False):
    name: str
    filterArn: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    datasetGroupArn: str
    failureReason: str
    status: str


class FilterTypeDef(TypedDict, total=False):
    name: str
    filterArn: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    datasetGroupArn: str
    failureReason: str
    filterExpression: str
    status: str


class GetSolutionMetricsResponseTypeDef(TypedDict, total=False):
    solutionVersionArn: str
    metrics: Dict[str, float]


class HPOConfigTypeDef(TypedDict, total=False):
    hpoObjective: "HPOObjectiveTypeDef"
    hpoResourceConfig: "HPOResourceConfigTypeDef"
    algorithmHyperParameterRanges: "HyperParameterRangesTypeDef"


HPOObjectiveTypeDef = TypedDict(
    "HPOObjectiveTypeDef", {"type": str, "metricName": str, "metricRegex": str}, total=False
)


class HPOResourceConfigTypeDef(TypedDict, total=False):
    maxNumberOfTrainingJobs: str
    maxParallelTrainingJobs: str


class HyperParameterRangesTypeDef(TypedDict, total=False):
    integerHyperParameterRanges: List["IntegerHyperParameterRangeTypeDef"]
    continuousHyperParameterRanges: List["ContinuousHyperParameterRangeTypeDef"]
    categoricalHyperParameterRanges: List["CategoricalHyperParameterRangeTypeDef"]


class IntegerHyperParameterRangeTypeDef(TypedDict, total=False):
    name: str
    minValue: int
    maxValue: int


class ListBatchInferenceJobsResponseTypeDef(TypedDict, total=False):
    batchInferenceJobs: List["BatchInferenceJobSummaryTypeDef"]
    nextToken: str


class ListCampaignsResponseTypeDef(TypedDict, total=False):
    campaigns: List["CampaignSummaryTypeDef"]
    nextToken: str


class ListDatasetExportJobsResponseTypeDef(TypedDict, total=False):
    datasetExportJobs: List["DatasetExportJobSummaryTypeDef"]
    nextToken: str


class ListDatasetGroupsResponseTypeDef(TypedDict, total=False):
    datasetGroups: List["DatasetGroupSummaryTypeDef"]
    nextToken: str


class ListDatasetImportJobsResponseTypeDef(TypedDict, total=False):
    datasetImportJobs: List["DatasetImportJobSummaryTypeDef"]
    nextToken: str


class ListDatasetsResponseTypeDef(TypedDict, total=False):
    datasets: List["DatasetSummaryTypeDef"]
    nextToken: str


class ListEventTrackersResponseTypeDef(TypedDict, total=False):
    eventTrackers: List["EventTrackerSummaryTypeDef"]
    nextToken: str


class ListFiltersResponseTypeDef(TypedDict, total=False):
    Filters: List["FilterSummaryTypeDef"]
    nextToken: str


class ListRecipesResponseTypeDef(TypedDict, total=False):
    recipes: List["RecipeSummaryTypeDef"]
    nextToken: str


class ListSchemasResponseTypeDef(TypedDict, total=False):
    schemas: List["DatasetSchemaSummaryTypeDef"]
    nextToken: str


class ListSolutionVersionsResponseTypeDef(TypedDict, total=False):
    solutionVersions: List["SolutionVersionSummaryTypeDef"]
    nextToken: str


class ListSolutionsResponseTypeDef(TypedDict, total=False):
    solutions: List["SolutionSummaryTypeDef"]
    nextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class RecipeSummaryTypeDef(TypedDict, total=False):
    name: str
    recipeArn: str
    status: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class RecipeTypeDef(TypedDict, total=False):
    name: str
    recipeArn: str
    algorithmArn: str
    featureTransformationArn: str
    status: str
    description: str
    creationDateTime: datetime
    recipeType: str
    lastUpdatedDateTime: datetime


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class _RequiredS3DataConfigTypeDef(TypedDict):
    path: str


class S3DataConfigTypeDef(_RequiredS3DataConfigTypeDef, total=False):
    kmsKeyArn: str


class SolutionConfigTypeDef(TypedDict, total=False):
    eventValueThreshold: str
    hpoConfig: "HPOConfigTypeDef"
    algorithmHyperParameters: Dict[str, str]
    featureTransformationParameters: Dict[str, str]
    autoMLConfig: "AutoMLConfigTypeDef"


class SolutionSummaryTypeDef(TypedDict, total=False):
    name: str
    solutionArn: str
    status: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class SolutionTypeDef(TypedDict, total=False):
    name: str
    solutionArn: str
    performHPO: bool
    performAutoML: bool
    recipeArn: str
    datasetGroupArn: str
    eventType: str
    solutionConfig: "SolutionConfigTypeDef"
    autoMLResult: "AutoMLResultTypeDef"
    status: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    latestSolutionVersion: "SolutionVersionSummaryTypeDef"


class SolutionVersionSummaryTypeDef(TypedDict, total=False):
    solutionVersionArn: str
    status: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime
    failureReason: str


class SolutionVersionTypeDef(TypedDict, total=False):
    solutionVersionArn: str
    solutionArn: str
    performHPO: bool
    performAutoML: bool
    recipeArn: str
    eventType: str
    datasetGroupArn: str
    solutionConfig: "SolutionConfigTypeDef"
    trainingHours: float
    trainingMode: TrainingMode
    tunedHPOParams: "TunedHPOParamsTypeDef"
    status: str
    failureReason: str
    creationDateTime: datetime
    lastUpdatedDateTime: datetime


class TunedHPOParamsTypeDef(TypedDict, total=False):
    algorithmHyperParameters: Dict[str, str]


class UpdateCampaignResponseTypeDef(TypedDict, total=False):
    campaignArn: str
