"""
Type annotations for sagemaker-a2i-runtime service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_sagemaker_a2i_runtime/literals.html)

Usage::

    ```python
    from mypy_boto3_sagemaker_a2i_runtime.literals import ContentClassifier

    data: ContentClassifier = "FreeOfAdultContent"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ContentClassifier", "HumanLoopStatus", "ListHumanLoopsPaginatorName", "SortOrder")


ContentClassifier = Literal["FreeOfAdultContent", "FreeOfPersonallyIdentifiableInformation"]
HumanLoopStatus = Literal["Completed", "Failed", "InProgress", "Stopped", "Stopping"]
ListHumanLoopsPaginatorName = Literal["list_human_loops"]
SortOrder = Literal["Ascending", "Descending"]
