"""
Type annotations for personalize service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_personalize/literals.html)

Usage::

    ```python
    from mypy_boto3_personalize.literals import IngestionMode

    data: IngestionMode = "ALL"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "IngestionMode",
    "ListBatchInferenceJobsPaginatorName",
    "ListCampaignsPaginatorName",
    "ListDatasetExportJobsPaginatorName",
    "ListDatasetGroupsPaginatorName",
    "ListDatasetImportJobsPaginatorName",
    "ListDatasetsPaginatorName",
    "ListEventTrackersPaginatorName",
    "ListFiltersPaginatorName",
    "ListRecipesPaginatorName",
    "ListSchemasPaginatorName",
    "ListSolutionVersionsPaginatorName",
    "ListSolutionsPaginatorName",
    "RecipeProvider",
    "TrainingMode",
)


IngestionMode = Literal["ALL", "BULK", "PUT"]
ListBatchInferenceJobsPaginatorName = Literal["list_batch_inference_jobs"]
ListCampaignsPaginatorName = Literal["list_campaigns"]
ListDatasetExportJobsPaginatorName = Literal["list_dataset_export_jobs"]
ListDatasetGroupsPaginatorName = Literal["list_dataset_groups"]
ListDatasetImportJobsPaginatorName = Literal["list_dataset_import_jobs"]
ListDatasetsPaginatorName = Literal["list_datasets"]
ListEventTrackersPaginatorName = Literal["list_event_trackers"]
ListFiltersPaginatorName = Literal["list_filters"]
ListRecipesPaginatorName = Literal["list_recipes"]
ListSchemasPaginatorName = Literal["list_schemas"]
ListSolutionVersionsPaginatorName = Literal["list_solution_versions"]
ListSolutionsPaginatorName = Literal["list_solutions"]
RecipeProvider = Literal["SERVICE"]
TrainingMode = Literal["FULL", "UPDATE"]
