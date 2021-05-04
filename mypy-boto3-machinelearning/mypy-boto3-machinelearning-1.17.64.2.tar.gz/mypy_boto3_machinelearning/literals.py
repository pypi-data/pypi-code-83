"""
Type annotations for machinelearning service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_machinelearning/literals.html)

Usage::

    ```python
    from mypy_boto3_machinelearning.literals import Algorithm

    data: Algorithm = "sgd"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "Algorithm",
    "BatchPredictionAvailableWaiterName",
    "BatchPredictionFilterVariable",
    "DataSourceAvailableWaiterName",
    "DataSourceFilterVariable",
    "DescribeBatchPredictionsPaginatorName",
    "DescribeDataSourcesPaginatorName",
    "DescribeEvaluationsPaginatorName",
    "DescribeMLModelsPaginatorName",
    "DetailsAttributes",
    "EntityStatus",
    "EvaluationAvailableWaiterName",
    "EvaluationFilterVariable",
    "MLModelAvailableWaiterName",
    "MLModelFilterVariable",
    "MLModelType",
    "RealtimeEndpointStatus",
    "SortOrder",
    "TaggableResourceType",
)


Algorithm = Literal["sgd"]
BatchPredictionAvailableWaiterName = Literal["batch_prediction_available"]
BatchPredictionFilterVariable = Literal[
    "CreatedAt",
    "DataSourceId",
    "DataURI",
    "IAMUser",
    "LastUpdatedAt",
    "MLModelId",
    "Name",
    "Status",
]
DataSourceAvailableWaiterName = Literal["data_source_available"]
DataSourceFilterVariable = Literal[
    "CreatedAt", "DataLocationS3", "IAMUser", "LastUpdatedAt", "Name", "Status"
]
DescribeBatchPredictionsPaginatorName = Literal["describe_batch_predictions"]
DescribeDataSourcesPaginatorName = Literal["describe_data_sources"]
DescribeEvaluationsPaginatorName = Literal["describe_evaluations"]
DescribeMLModelsPaginatorName = Literal["describe_ml_models"]
DetailsAttributes = Literal["Algorithm", "PredictiveModelType"]
EntityStatus = Literal["COMPLETED", "DELETED", "FAILED", "INPROGRESS", "PENDING"]
EvaluationAvailableWaiterName = Literal["evaluation_available"]
EvaluationFilterVariable = Literal[
    "CreatedAt",
    "DataSourceId",
    "DataURI",
    "IAMUser",
    "LastUpdatedAt",
    "MLModelId",
    "Name",
    "Status",
]
MLModelAvailableWaiterName = Literal["ml_model_available"]
MLModelFilterVariable = Literal[
    "Algorithm",
    "CreatedAt",
    "IAMUser",
    "LastUpdatedAt",
    "MLModelType",
    "Name",
    "RealtimeEndpointStatus",
    "Status",
    "TrainingDataSourceId",
    "TrainingDataURI",
]
MLModelType = Literal["BINARY", "MULTICLASS", "REGRESSION"]
RealtimeEndpointStatus = Literal["FAILED", "NONE", "READY", "UPDATING"]
SortOrder = Literal["asc", "dsc"]
TaggableResourceType = Literal["BatchPrediction", "DataSource", "Evaluation", "MLModel"]
