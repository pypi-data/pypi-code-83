"""
Type annotations for serverlessrepo service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/literals.html)

Usage::

    ```python
    from mypy_boto3_serverlessrepo.literals import Capability

    data: Capability = "CAPABILITY_AUTO_EXPAND"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "Capability",
    "ListApplicationDependenciesPaginatorName",
    "ListApplicationVersionsPaginatorName",
    "ListApplicationsPaginatorName",
    "Status",
)


Capability = Literal[
    "CAPABILITY_AUTO_EXPAND", "CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_RESOURCE_POLICY"
]
ListApplicationDependenciesPaginatorName = Literal["list_application_dependencies"]
ListApplicationVersionsPaginatorName = Literal["list_application_versions"]
ListApplicationsPaginatorName = Literal["list_applications"]
Status = Literal["ACTIVE", "EXPIRED", "PREPARING"]
