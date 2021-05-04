"""
Type annotations for iotdeviceadvisor service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotdeviceadvisor/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotdeviceadvisor.type_defs import CreateSuiteDefinitionResponseTypeDef

    data: CreateSuiteDefinitionResponseTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_iotdeviceadvisor.literals import Status, SuiteRunStatus

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateSuiteDefinitionResponseTypeDef",
    "DeviceUnderTestTypeDef",
    "GetSuiteDefinitionResponseTypeDef",
    "GetSuiteRunReportResponseTypeDef",
    "GetSuiteRunResponseTypeDef",
    "GroupResultTypeDef",
    "ListSuiteDefinitionsResponseTypeDef",
    "ListSuiteRunsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTestCasesResponseTypeDef",
    "StartSuiteRunResponseTypeDef",
    "SuiteDefinitionConfigurationTypeDef",
    "SuiteDefinitionInformationTypeDef",
    "SuiteRunConfigurationTypeDef",
    "SuiteRunInformationTypeDef",
    "TestCaseCategoryTypeDef",
    "TestCaseDefinitionTypeDef",
    "TestCaseRunTypeDef",
    "TestCaseTypeDef",
    "TestResultTypeDef",
    "UpdateSuiteDefinitionResponseTypeDef",
)


class CreateSuiteDefinitionResponseTypeDef(TypedDict, total=False):
    suiteDefinitionId: str
    suiteDefinitionArn: str
    suiteDefinitionName: str
    createdAt: datetime


class DeviceUnderTestTypeDef(TypedDict, total=False):
    thingArn: str
    certificateArn: str


class GetSuiteDefinitionResponseTypeDef(TypedDict, total=False):
    suiteDefinitionId: str
    suiteDefinitionArn: str
    suiteDefinitionVersion: str
    latestVersion: str
    suiteDefinitionConfiguration: "SuiteDefinitionConfigurationTypeDef"
    createdAt: datetime
    lastModifiedAt: datetime
    tags: Dict[str, str]


class GetSuiteRunReportResponseTypeDef(TypedDict, total=False):
    qualificationReportDownloadUrl: str


class GetSuiteRunResponseTypeDef(TypedDict, total=False):
    suiteDefinitionId: str
    suiteDefinitionVersion: str
    suiteRunId: str
    suiteRunArn: str
    suiteRunConfiguration: "SuiteRunConfigurationTypeDef"
    testResult: "TestResultTypeDef"
    startTime: datetime
    endTime: datetime
    status: SuiteRunStatus
    errorReason: str
    tags: Dict[str, str]


class GroupResultTypeDef(TypedDict, total=False):
    groupId: str
    groupName: str
    tests: List["TestCaseRunTypeDef"]


class ListSuiteDefinitionsResponseTypeDef(TypedDict, total=False):
    suiteDefinitionInformationList: List["SuiteDefinitionInformationTypeDef"]
    nextToken: str


class ListSuiteRunsResponseTypeDef(TypedDict, total=False):
    suiteRunsList: List["SuiteRunInformationTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class ListTestCasesResponseTypeDef(TypedDict, total=False):
    categories: List["TestCaseCategoryTypeDef"]
    rootGroupConfiguration: Dict[str, str]
    groupConfiguration: Dict[str, str]
    nextToken: str


class StartSuiteRunResponseTypeDef(TypedDict, total=False):
    suiteRunId: str
    suiteRunArn: str
    createdAt: datetime


class SuiteDefinitionConfigurationTypeDef(TypedDict, total=False):
    suiteDefinitionName: str
    devices: List["DeviceUnderTestTypeDef"]
    intendedForQualification: bool
    rootGroup: str
    devicePermissionRoleArn: str


class SuiteDefinitionInformationTypeDef(TypedDict, total=False):
    suiteDefinitionId: str
    suiteDefinitionName: str
    defaultDevices: List["DeviceUnderTestTypeDef"]
    intendedForQualification: bool
    createdAt: datetime


class SuiteRunConfigurationTypeDef(TypedDict, total=False):
    primaryDevice: "DeviceUnderTestTypeDef"
    secondaryDevice: "DeviceUnderTestTypeDef"
    selectedTestList: List[str]


class SuiteRunInformationTypeDef(TypedDict, total=False):
    suiteDefinitionId: str
    suiteDefinitionVersion: str
    suiteDefinitionName: str
    suiteRunId: str
    createdAt: datetime
    startedAt: datetime
    endAt: datetime
    status: SuiteRunStatus
    passed: int
    failed: int


class TestCaseCategoryTypeDef(TypedDict, total=False):
    name: str
    tests: List["TestCaseTypeDef"]


TestCaseDefinitionTypeDef = TypedDict(
    "TestCaseDefinitionTypeDef", {"id": str, "testCaseVersion": str}, total=False
)


class TestCaseRunTypeDef(TypedDict, total=False):
    testCaseRunId: str
    testCaseDefinitionId: str
    testCaseDefinitionName: str
    status: Status
    startTime: datetime
    endTime: datetime
    logUrl: str
    warnings: str
    failure: str


class TestCaseTypeDef(TypedDict, total=False):
    name: str
    configuration: Dict[str, str]
    test: "TestCaseDefinitionTypeDef"


class TestResultTypeDef(TypedDict, total=False):
    groups: List["GroupResultTypeDef"]


class UpdateSuiteDefinitionResponseTypeDef(TypedDict, total=False):
    suiteDefinitionId: str
    suiteDefinitionArn: str
    suiteDefinitionName: str
    suiteDefinitionVersion: str
    createdAt: datetime
    lastUpdatedAt: datetime
