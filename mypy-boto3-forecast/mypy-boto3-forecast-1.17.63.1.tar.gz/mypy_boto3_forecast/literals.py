"""
Type annotations for forecast service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_forecast/literals.html)

Usage::

    ```python
    from mypy_boto3_forecast.literals import AttributeType

    data: AttributeType = "float"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AttributeType",
    "DatasetType",
    "Domain",
    "EvaluationType",
    "FeaturizationMethodName",
    "FilterConditionString",
    "ListDatasetGroupsPaginatorName",
    "ListDatasetImportJobsPaginatorName",
    "ListDatasetsPaginatorName",
    "ListForecastExportJobsPaginatorName",
    "ListForecastsPaginatorName",
    "ListPredictorBacktestExportJobsPaginatorName",
    "ListPredictorsPaginatorName",
    "ScalingType",
)


AttributeType = Literal["float", "geolocation", "integer", "string", "timestamp"]
DatasetType = Literal["ITEM_METADATA", "RELATED_TIME_SERIES", "TARGET_TIME_SERIES"]
Domain = Literal[
    "CUSTOM", "EC2_CAPACITY", "INVENTORY_PLANNING", "METRICS", "RETAIL", "WEB_TRAFFIC", "WORK_FORCE"
]
EvaluationType = Literal["COMPUTED", "SUMMARY"]
FeaturizationMethodName = Literal["filling"]
FilterConditionString = Literal["IS", "IS_NOT"]
ListDatasetGroupsPaginatorName = Literal["list_dataset_groups"]
ListDatasetImportJobsPaginatorName = Literal["list_dataset_import_jobs"]
ListDatasetsPaginatorName = Literal["list_datasets"]
ListForecastExportJobsPaginatorName = Literal["list_forecast_export_jobs"]
ListForecastsPaginatorName = Literal["list_forecasts"]
ListPredictorBacktestExportJobsPaginatorName = Literal["list_predictor_backtest_export_jobs"]
ListPredictorsPaginatorName = Literal["list_predictors"]
ScalingType = Literal["Auto", "Linear", "Logarithmic", "ReverseLogarithmic"]
