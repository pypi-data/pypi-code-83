"""
Type annotations for codestar service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_codestar/type_defs.html)

Usage::

    ```python
    from mypy_boto3_codestar.type_defs import AssociateTeamMemberResultTypeDef

    data: AssociateTeamMemberResultTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AssociateTeamMemberResultTypeDef",
    "CodeCommitCodeDestinationTypeDef",
    "CodeDestinationTypeDef",
    "CodeSourceTypeDef",
    "CodeTypeDef",
    "CreateProjectResultTypeDef",
    "CreateUserProfileResultTypeDef",
    "DeleteProjectResultTypeDef",
    "DeleteUserProfileResultTypeDef",
    "DescribeProjectResultTypeDef",
    "DescribeUserProfileResultTypeDef",
    "GitHubCodeDestinationTypeDef",
    "ListProjectsResultTypeDef",
    "ListResourcesResultTypeDef",
    "ListTagsForProjectResultTypeDef",
    "ListTeamMembersResultTypeDef",
    "ListUserProfilesResultTypeDef",
    "PaginatorConfigTypeDef",
    "ProjectStatusTypeDef",
    "ProjectSummaryTypeDef",
    "ResourceTypeDef",
    "S3LocationTypeDef",
    "TagProjectResultTypeDef",
    "TeamMemberTypeDef",
    "ToolchainSourceTypeDef",
    "ToolchainTypeDef",
    "UpdateTeamMemberResultTypeDef",
    "UpdateUserProfileResultTypeDef",
    "UserProfileSummaryTypeDef",
)


class AssociateTeamMemberResultTypeDef(TypedDict, total=False):
    clientRequestToken: str


class CodeCommitCodeDestinationTypeDef(TypedDict):
    name: str


class CodeDestinationTypeDef(TypedDict, total=False):
    codeCommit: "CodeCommitCodeDestinationTypeDef"
    gitHub: "GitHubCodeDestinationTypeDef"


class CodeSourceTypeDef(TypedDict):
    s3: "S3LocationTypeDef"


class CodeTypeDef(TypedDict):
    source: "CodeSourceTypeDef"
    destination: "CodeDestinationTypeDef"


_RequiredCreateProjectResultTypeDef = TypedDict(
    "_RequiredCreateProjectResultTypeDef", {"id": str, "arn": str}
)
_OptionalCreateProjectResultTypeDef = TypedDict(
    "_OptionalCreateProjectResultTypeDef",
    {"clientRequestToken": str, "projectTemplateId": str},
    total=False,
)


class CreateProjectResultTypeDef(
    _RequiredCreateProjectResultTypeDef, _OptionalCreateProjectResultTypeDef
):
    pass


class _RequiredCreateUserProfileResultTypeDef(TypedDict):
    userArn: str


class CreateUserProfileResultTypeDef(_RequiredCreateUserProfileResultTypeDef, total=False):
    displayName: str
    emailAddress: str
    sshPublicKey: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime


class DeleteProjectResultTypeDef(TypedDict, total=False):
    stackId: str
    projectArn: str


class DeleteUserProfileResultTypeDef(TypedDict):
    userArn: str


DescribeProjectResultTypeDef = TypedDict(
    "DescribeProjectResultTypeDef",
    {
        "name": str,
        "id": str,
        "arn": str,
        "description": str,
        "clientRequestToken": str,
        "createdTimeStamp": datetime,
        "stackId": str,
        "projectTemplateId": str,
        "status": "ProjectStatusTypeDef",
    },
    total=False,
)


class _RequiredDescribeUserProfileResultTypeDef(TypedDict):
    userArn: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime


class DescribeUserProfileResultTypeDef(_RequiredDescribeUserProfileResultTypeDef, total=False):
    displayName: str
    emailAddress: str
    sshPublicKey: str


_RequiredGitHubCodeDestinationTypeDef = TypedDict(
    "_RequiredGitHubCodeDestinationTypeDef",
    {
        "name": str,
        "type": str,
        "owner": str,
        "privateRepository": bool,
        "issuesEnabled": bool,
        "token": str,
    },
)
_OptionalGitHubCodeDestinationTypeDef = TypedDict(
    "_OptionalGitHubCodeDestinationTypeDef", {"description": str}, total=False
)


class GitHubCodeDestinationTypeDef(
    _RequiredGitHubCodeDestinationTypeDef, _OptionalGitHubCodeDestinationTypeDef
):
    pass


class _RequiredListProjectsResultTypeDef(TypedDict):
    projects: List["ProjectSummaryTypeDef"]


class ListProjectsResultTypeDef(_RequiredListProjectsResultTypeDef, total=False):
    nextToken: str


class ListResourcesResultTypeDef(TypedDict, total=False):
    resources: List["ResourceTypeDef"]
    nextToken: str


class ListTagsForProjectResultTypeDef(TypedDict, total=False):
    tags: Dict[str, str]
    nextToken: str


class _RequiredListTeamMembersResultTypeDef(TypedDict):
    teamMembers: List["TeamMemberTypeDef"]


class ListTeamMembersResultTypeDef(_RequiredListTeamMembersResultTypeDef, total=False):
    nextToken: str


class _RequiredListUserProfilesResultTypeDef(TypedDict):
    userProfiles: List["UserProfileSummaryTypeDef"]


class ListUserProfilesResultTypeDef(_RequiredListUserProfilesResultTypeDef, total=False):
    nextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredProjectStatusTypeDef(TypedDict):
    state: str


class ProjectStatusTypeDef(_RequiredProjectStatusTypeDef, total=False):
    reason: str


class ProjectSummaryTypeDef(TypedDict, total=False):
    projectId: str
    projectArn: str


ResourceTypeDef = TypedDict("ResourceTypeDef", {"id": str})


class S3LocationTypeDef(TypedDict, total=False):
    bucketName: str
    bucketKey: str


class TagProjectResultTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class _RequiredTeamMemberTypeDef(TypedDict):
    userArn: str
    projectRole: str


class TeamMemberTypeDef(_RequiredTeamMemberTypeDef, total=False):
    remoteAccessAllowed: bool


class ToolchainSourceTypeDef(TypedDict):
    s3: "S3LocationTypeDef"


class _RequiredToolchainTypeDef(TypedDict):
    source: "ToolchainSourceTypeDef"


class ToolchainTypeDef(_RequiredToolchainTypeDef, total=False):
    roleArn: str
    stackParameters: Dict[str, str]


class UpdateTeamMemberResultTypeDef(TypedDict, total=False):
    userArn: str
    projectRole: str
    remoteAccessAllowed: bool


class _RequiredUpdateUserProfileResultTypeDef(TypedDict):
    userArn: str


class UpdateUserProfileResultTypeDef(_RequiredUpdateUserProfileResultTypeDef, total=False):
    displayName: str
    emailAddress: str
    sshPublicKey: str
    createdTimestamp: datetime
    lastModifiedTimestamp: datetime


class UserProfileSummaryTypeDef(TypedDict, total=False):
    userArn: str
    displayName: str
    emailAddress: str
    sshPublicKey: str
