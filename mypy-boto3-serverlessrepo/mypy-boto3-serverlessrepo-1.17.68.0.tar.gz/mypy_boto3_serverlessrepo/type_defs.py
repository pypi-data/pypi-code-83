"""
Type annotations for serverlessrepo service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_serverlessrepo/type_defs.html)

Usage::

    ```python
    from mypy_boto3_serverlessrepo.type_defs import ApplicationDependencySummaryTypeDef

    data: ApplicationDependencySummaryTypeDef = {...}
    ```
"""
import sys
from typing import List

from mypy_boto3_serverlessrepo.literals import Capability, Status

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ApplicationDependencySummaryTypeDef",
    "ApplicationPolicyStatementTypeDef",
    "ApplicationSummaryTypeDef",
    "CreateApplicationResponseTypeDef",
    "CreateApplicationVersionResponseTypeDef",
    "CreateCloudFormationChangeSetResponseTypeDef",
    "CreateCloudFormationTemplateResponseTypeDef",
    "GetApplicationPolicyResponseTypeDef",
    "GetApplicationResponseTypeDef",
    "GetCloudFormationTemplateResponseTypeDef",
    "ListApplicationDependenciesResponseTypeDef",
    "ListApplicationVersionsResponseTypeDef",
    "ListApplicationsResponseTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterDefinitionTypeDef",
    "ParameterValueTypeDef",
    "PutApplicationPolicyResponseTypeDef",
    "RollbackConfigurationTypeDef",
    "RollbackTriggerTypeDef",
    "TagTypeDef",
    "UpdateApplicationResponseTypeDef",
    "VersionSummaryTypeDef",
    "VersionTypeDef",
)


class ApplicationDependencySummaryTypeDef(TypedDict):
    ApplicationId: str
    SemanticVersion: str


class _RequiredApplicationPolicyStatementTypeDef(TypedDict):
    Actions: List[str]
    Principals: List[str]


class ApplicationPolicyStatementTypeDef(_RequiredApplicationPolicyStatementTypeDef, total=False):
    PrincipalOrgIDs: List[str]
    StatementId: str


class _RequiredApplicationSummaryTypeDef(TypedDict):
    ApplicationId: str
    Author: str
    Description: str
    Name: str


class ApplicationSummaryTypeDef(_RequiredApplicationSummaryTypeDef, total=False):
    CreationTime: str
    HomePageUrl: str
    Labels: List[str]
    SpdxLicenseId: str


class CreateApplicationResponseTypeDef(TypedDict, total=False):
    ApplicationId: str
    Author: str
    CreationTime: str
    Description: str
    HomePageUrl: str
    IsVerifiedAuthor: bool
    Labels: List[str]
    LicenseUrl: str
    Name: str
    ReadmeUrl: str
    SpdxLicenseId: str
    VerifiedAuthorUrl: str
    Version: "VersionTypeDef"


class CreateApplicationVersionResponseTypeDef(TypedDict, total=False):
    ApplicationId: str
    CreationTime: str
    ParameterDefinitions: List["ParameterDefinitionTypeDef"]
    RequiredCapabilities: List[Capability]
    ResourcesSupported: bool
    SemanticVersion: str
    SourceCodeArchiveUrl: str
    SourceCodeUrl: str
    TemplateUrl: str


class CreateCloudFormationChangeSetResponseTypeDef(TypedDict, total=False):
    ApplicationId: str
    ChangeSetId: str
    SemanticVersion: str
    StackId: str


class CreateCloudFormationTemplateResponseTypeDef(TypedDict, total=False):
    ApplicationId: str
    CreationTime: str
    ExpirationTime: str
    SemanticVersion: str
    Status: Status
    TemplateId: str
    TemplateUrl: str


class GetApplicationPolicyResponseTypeDef(TypedDict, total=False):
    Statements: List["ApplicationPolicyStatementTypeDef"]


class GetApplicationResponseTypeDef(TypedDict, total=False):
    ApplicationId: str
    Author: str
    CreationTime: str
    Description: str
    HomePageUrl: str
    IsVerifiedAuthor: bool
    Labels: List[str]
    LicenseUrl: str
    Name: str
    ReadmeUrl: str
    SpdxLicenseId: str
    VerifiedAuthorUrl: str
    Version: "VersionTypeDef"


class GetCloudFormationTemplateResponseTypeDef(TypedDict, total=False):
    ApplicationId: str
    CreationTime: str
    ExpirationTime: str
    SemanticVersion: str
    Status: Status
    TemplateId: str
    TemplateUrl: str


class ListApplicationDependenciesResponseTypeDef(TypedDict, total=False):
    Dependencies: List["ApplicationDependencySummaryTypeDef"]
    NextToken: str


class ListApplicationVersionsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Versions: List["VersionSummaryTypeDef"]


class ListApplicationsResponseTypeDef(TypedDict, total=False):
    Applications: List["ApplicationSummaryTypeDef"]
    NextToken: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


_RequiredParameterDefinitionTypeDef = TypedDict(
    "_RequiredParameterDefinitionTypeDef", {"Name": str, "ReferencedByResources": List[str]}
)
_OptionalParameterDefinitionTypeDef = TypedDict(
    "_OptionalParameterDefinitionTypeDef",
    {
        "AllowedPattern": str,
        "AllowedValues": List[str],
        "ConstraintDescription": str,
        "DefaultValue": str,
        "Description": str,
        "MaxLength": int,
        "MaxValue": int,
        "MinLength": int,
        "MinValue": int,
        "NoEcho": bool,
        "Type": str,
    },
    total=False,
)


class ParameterDefinitionTypeDef(
    _RequiredParameterDefinitionTypeDef, _OptionalParameterDefinitionTypeDef
):
    pass


class ParameterValueTypeDef(TypedDict):
    Name: str
    Value: str


class PutApplicationPolicyResponseTypeDef(TypedDict, total=False):
    Statements: List["ApplicationPolicyStatementTypeDef"]


class RollbackConfigurationTypeDef(TypedDict, total=False):
    MonitoringTimeInMinutes: int
    RollbackTriggers: List["RollbackTriggerTypeDef"]


RollbackTriggerTypeDef = TypedDict("RollbackTriggerTypeDef", {"Arn": str, "Type": str})


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class UpdateApplicationResponseTypeDef(TypedDict, total=False):
    ApplicationId: str
    Author: str
    CreationTime: str
    Description: str
    HomePageUrl: str
    IsVerifiedAuthor: bool
    Labels: List[str]
    LicenseUrl: str
    Name: str
    ReadmeUrl: str
    SpdxLicenseId: str
    VerifiedAuthorUrl: str
    Version: "VersionTypeDef"


class _RequiredVersionSummaryTypeDef(TypedDict):
    ApplicationId: str
    CreationTime: str
    SemanticVersion: str


class VersionSummaryTypeDef(_RequiredVersionSummaryTypeDef, total=False):
    SourceCodeUrl: str


class _RequiredVersionTypeDef(TypedDict):
    ApplicationId: str
    CreationTime: str
    ParameterDefinitions: List["ParameterDefinitionTypeDef"]
    RequiredCapabilities: List[Capability]
    ResourcesSupported: bool
    SemanticVersion: str
    TemplateUrl: str


class VersionTypeDef(_RequiredVersionTypeDef, total=False):
    SourceCodeArchiveUrl: str
    SourceCodeUrl: str
