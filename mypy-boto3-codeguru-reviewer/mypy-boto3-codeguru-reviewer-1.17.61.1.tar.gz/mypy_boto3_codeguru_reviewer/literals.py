"""
Type annotations for codeguru-reviewer service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codeguru_reviewer/literals.html)

Usage::

    ```python
    from mypy_boto3_codeguru_reviewer.literals import EncryptionOption

    data: EncryptionOption = "AWS_OWNED_CMK"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "EncryptionOption",
    "JobState",
    "ListRepositoryAssociationsPaginatorName",
    "ProviderType",
    "Reaction",
    "RepositoryAssociationState",
    "TypeType",
)


EncryptionOption = Literal["AWS_OWNED_CMK", "CUSTOMER_MANAGED_CMK"]
JobState = Literal["Completed", "Deleting", "Failed", "Pending"]
ListRepositoryAssociationsPaginatorName = Literal["list_repository_associations"]
ProviderType = Literal["Bitbucket", "CodeCommit", "GitHub", "GitHubEnterpriseServer"]
Reaction = Literal["ThumbsDown", "ThumbsUp"]
RepositoryAssociationState = Literal[
    "Associated", "Associating", "Disassociated", "Disassociating", "Failed"
]
TypeType = Literal["PullRequest", "RepositoryAnalysis"]
