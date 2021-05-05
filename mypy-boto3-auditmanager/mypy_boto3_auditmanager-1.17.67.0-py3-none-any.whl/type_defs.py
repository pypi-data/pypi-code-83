"""
Type annotations for auditmanager service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_auditmanager/type_defs.html)

Usage::

    ```python
    from mypy_boto3_auditmanager.type_defs import AWSAccountTypeDef

    data: AWSAccountTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_auditmanager.literals import (
    AccountStatus,
    ActionEnum,
    AssessmentReportStatus,
    AssessmentStatus,
    ControlResponse,
    ControlSetStatus,
    ControlStatus,
    ControlType,
    DelegationStatus,
    FrameworkType,
    ObjectTypeEnum,
    RoleType,
    SourceFrequency,
    SourceSetUpOption,
    SourceType,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AWSAccountTypeDef",
    "AWSServiceTypeDef",
    "AssessmentControlSetTypeDef",
    "AssessmentControlTypeDef",
    "AssessmentEvidenceFolderTypeDef",
    "AssessmentFrameworkMetadataTypeDef",
    "AssessmentFrameworkTypeDef",
    "AssessmentMetadataItemTypeDef",
    "AssessmentMetadataTypeDef",
    "AssessmentReportEvidenceErrorTypeDef",
    "AssessmentReportMetadataTypeDef",
    "AssessmentReportTypeDef",
    "AssessmentReportsDestinationTypeDef",
    "AssessmentTypeDef",
    "BatchAssociateAssessmentReportEvidenceResponseTypeDef",
    "BatchCreateDelegationByAssessmentErrorTypeDef",
    "BatchCreateDelegationByAssessmentResponseTypeDef",
    "BatchDeleteDelegationByAssessmentErrorTypeDef",
    "BatchDeleteDelegationByAssessmentResponseTypeDef",
    "BatchDisassociateAssessmentReportEvidenceResponseTypeDef",
    "BatchImportEvidenceToAssessmentControlErrorTypeDef",
    "BatchImportEvidenceToAssessmentControlResponseTypeDef",
    "ChangeLogTypeDef",
    "ControlCommentTypeDef",
    "ControlMappingSourceTypeDef",
    "ControlMetadataTypeDef",
    "ControlSetTypeDef",
    "ControlTypeDef",
    "CreateAssessmentFrameworkControlSetTypeDef",
    "CreateAssessmentFrameworkControlTypeDef",
    "CreateAssessmentFrameworkResponseTypeDef",
    "CreateAssessmentReportResponseTypeDef",
    "CreateAssessmentResponseTypeDef",
    "CreateControlMappingSourceTypeDef",
    "CreateControlResponseTypeDef",
    "CreateDelegationRequestTypeDef",
    "DelegationMetadataTypeDef",
    "DelegationTypeDef",
    "DeregisterAccountResponseTypeDef",
    "EvidenceTypeDef",
    "FrameworkMetadataTypeDef",
    "FrameworkTypeDef",
    "GetAccountStatusResponseTypeDef",
    "GetAssessmentFrameworkResponseTypeDef",
    "GetAssessmentReportUrlResponseTypeDef",
    "GetAssessmentResponseTypeDef",
    "GetChangeLogsResponseTypeDef",
    "GetControlResponseTypeDef",
    "GetDelegationsResponseTypeDef",
    "GetEvidenceByEvidenceFolderResponseTypeDef",
    "GetEvidenceFolderResponseTypeDef",
    "GetEvidenceFoldersByAssessmentControlResponseTypeDef",
    "GetEvidenceFoldersByAssessmentResponseTypeDef",
    "GetEvidenceResponseTypeDef",
    "GetOrganizationAdminAccountResponseTypeDef",
    "GetServicesInScopeResponseTypeDef",
    "GetSettingsResponseTypeDef",
    "ListAssessmentFrameworksResponseTypeDef",
    "ListAssessmentReportsResponseTypeDef",
    "ListAssessmentsResponseTypeDef",
    "ListControlsResponseTypeDef",
    "ListKeywordsForDataSourceResponseTypeDef",
    "ListNotificationsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ManualEvidenceTypeDef",
    "NotificationTypeDef",
    "RegisterAccountResponseTypeDef",
    "RegisterOrganizationAdminAccountResponseTypeDef",
    "ResourceTypeDef",
    "RoleTypeDef",
    "ScopeTypeDef",
    "ServiceMetadataTypeDef",
    "SettingsTypeDef",
    "SourceKeywordTypeDef",
    "URLTypeDef",
    "UpdateAssessmentControlResponseTypeDef",
    "UpdateAssessmentControlSetStatusResponseTypeDef",
    "UpdateAssessmentFrameworkControlSetTypeDef",
    "UpdateAssessmentFrameworkResponseTypeDef",
    "UpdateAssessmentResponseTypeDef",
    "UpdateAssessmentStatusResponseTypeDef",
    "UpdateControlResponseTypeDef",
    "UpdateSettingsResponseTypeDef",
    "ValidateAssessmentReportIntegrityResponseTypeDef",
)

AWSAccountTypeDef = TypedDict(
    "AWSAccountTypeDef", {"id": str, "emailAddress": str, "name": str}, total=False
)


class AWSServiceTypeDef(TypedDict, total=False):
    serviceName: str


AssessmentControlSetTypeDef = TypedDict(
    "AssessmentControlSetTypeDef",
    {
        "id": str,
        "description": str,
        "status": ControlSetStatus,
        "roles": List["RoleTypeDef"],
        "controls": List["AssessmentControlTypeDef"],
        "delegations": List["DelegationTypeDef"],
        "systemEvidenceCount": int,
        "manualEvidenceCount": int,
    },
    total=False,
)

AssessmentControlTypeDef = TypedDict(
    "AssessmentControlTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "status": ControlStatus,
        "response": ControlResponse,
        "comments": List["ControlCommentTypeDef"],
        "evidenceSources": List[str],
        "evidenceCount": int,
        "assessmentReportEvidenceCount": int,
    },
    total=False,
)

AssessmentEvidenceFolderTypeDef = TypedDict(
    "AssessmentEvidenceFolderTypeDef",
    {
        "name": str,
        "date": datetime,
        "assessmentId": str,
        "controlSetId": str,
        "controlId": str,
        "id": str,
        "dataSource": str,
        "author": str,
        "totalEvidence": int,
        "assessmentReportSelectionCount": int,
        "controlName": str,
        "evidenceResourcesIncludedCount": int,
        "evidenceByTypeConfigurationDataCount": int,
        "evidenceByTypeManualCount": int,
        "evidenceByTypeComplianceCheckCount": int,
        "evidenceByTypeComplianceCheckIssuesCount": int,
        "evidenceByTypeUserActivityCount": int,
        "evidenceAwsServiceSourceCount": int,
    },
    total=False,
)

AssessmentFrameworkMetadataTypeDef = TypedDict(
    "AssessmentFrameworkMetadataTypeDef",
    {
        "arn": str,
        "id": str,
        "type": FrameworkType,
        "name": str,
        "description": str,
        "logo": str,
        "complianceType": str,
        "controlsCount": int,
        "controlSetsCount": int,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

AssessmentFrameworkTypeDef = TypedDict(
    "AssessmentFrameworkTypeDef",
    {
        "id": str,
        "arn": str,
        "metadata": "FrameworkMetadataTypeDef",
        "controlSets": List["AssessmentControlSetTypeDef"],
    },
    total=False,
)

AssessmentMetadataItemTypeDef = TypedDict(
    "AssessmentMetadataItemTypeDef",
    {
        "name": str,
        "id": str,
        "complianceType": str,
        "status": AssessmentStatus,
        "roles": List["RoleTypeDef"],
        "delegations": List["DelegationTypeDef"],
        "creationTime": datetime,
        "lastUpdated": datetime,
    },
    total=False,
)

AssessmentMetadataTypeDef = TypedDict(
    "AssessmentMetadataTypeDef",
    {
        "name": str,
        "id": str,
        "description": str,
        "complianceType": str,
        "status": AssessmentStatus,
        "assessmentReportsDestination": "AssessmentReportsDestinationTypeDef",
        "scope": "ScopeTypeDef",
        "roles": List["RoleTypeDef"],
        "delegations": List["DelegationTypeDef"],
        "creationTime": datetime,
        "lastUpdated": datetime,
    },
    total=False,
)


class AssessmentReportEvidenceErrorTypeDef(TypedDict, total=False):
    evidenceId: str
    errorCode: str
    errorMessage: str


AssessmentReportMetadataTypeDef = TypedDict(
    "AssessmentReportMetadataTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "assessmentId": str,
        "assessmentName": str,
        "author": str,
        "status": AssessmentReportStatus,
        "creationTime": datetime,
    },
    total=False,
)

AssessmentReportTypeDef = TypedDict(
    "AssessmentReportTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "awsAccountId": str,
        "assessmentId": str,
        "assessmentName": str,
        "author": str,
        "status": AssessmentReportStatus,
        "creationTime": datetime,
    },
    total=False,
)


class AssessmentReportsDestinationTypeDef(TypedDict, total=False):
    destinationType: Literal["S3"]
    destination: str


class AssessmentTypeDef(TypedDict, total=False):
    arn: str
    awsAccount: "AWSAccountTypeDef"
    metadata: "AssessmentMetadataTypeDef"
    framework: "AssessmentFrameworkTypeDef"
    tags: Dict[str, str]


class BatchAssociateAssessmentReportEvidenceResponseTypeDef(TypedDict, total=False):
    evidenceIds: List[str]
    errors: List["AssessmentReportEvidenceErrorTypeDef"]


class BatchCreateDelegationByAssessmentErrorTypeDef(TypedDict, total=False):
    createDelegationRequest: "CreateDelegationRequestTypeDef"
    errorCode: str
    errorMessage: str


class BatchCreateDelegationByAssessmentResponseTypeDef(TypedDict, total=False):
    delegations: List["DelegationTypeDef"]
    errors: List["BatchCreateDelegationByAssessmentErrorTypeDef"]


class BatchDeleteDelegationByAssessmentErrorTypeDef(TypedDict, total=False):
    delegationId: str
    errorCode: str
    errorMessage: str


class BatchDeleteDelegationByAssessmentResponseTypeDef(TypedDict, total=False):
    errors: List["BatchDeleteDelegationByAssessmentErrorTypeDef"]


class BatchDisassociateAssessmentReportEvidenceResponseTypeDef(TypedDict, total=False):
    evidenceIds: List[str]
    errors: List["AssessmentReportEvidenceErrorTypeDef"]


class BatchImportEvidenceToAssessmentControlErrorTypeDef(TypedDict, total=False):
    manualEvidence: "ManualEvidenceTypeDef"
    errorCode: str
    errorMessage: str


class BatchImportEvidenceToAssessmentControlResponseTypeDef(TypedDict, total=False):
    errors: List["BatchImportEvidenceToAssessmentControlErrorTypeDef"]


class ChangeLogTypeDef(TypedDict, total=False):
    objectType: ObjectTypeEnum
    objectName: str
    action: ActionEnum
    createdAt: datetime
    createdBy: str


class ControlCommentTypeDef(TypedDict, total=False):
    authorName: str
    commentBody: str
    postedDate: datetime


class ControlMappingSourceTypeDef(TypedDict, total=False):
    sourceId: str
    sourceName: str
    sourceDescription: str
    sourceSetUpOption: SourceSetUpOption
    sourceType: SourceType
    sourceKeyword: "SourceKeywordTypeDef"
    sourceFrequency: SourceFrequency
    troubleshootingText: str


ControlMetadataTypeDef = TypedDict(
    "ControlMetadataTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "controlSources": str,
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
    },
    total=False,
)

ControlSetTypeDef = TypedDict(
    "ControlSetTypeDef", {"id": str, "name": str, "controls": List["ControlTypeDef"]}, total=False
)

ControlTypeDef = TypedDict(
    "ControlTypeDef",
    {
        "arn": str,
        "id": str,
        "type": ControlType,
        "name": str,
        "description": str,
        "testingInformation": str,
        "actionPlanTitle": str,
        "actionPlanInstructions": str,
        "controlSources": str,
        "controlMappingSources": List["ControlMappingSourceTypeDef"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "createdBy": str,
        "lastUpdatedBy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class _RequiredCreateAssessmentFrameworkControlSetTypeDef(TypedDict):
    name: str


class CreateAssessmentFrameworkControlSetTypeDef(
    _RequiredCreateAssessmentFrameworkControlSetTypeDef, total=False
):
    controls: List["CreateAssessmentFrameworkControlTypeDef"]


CreateAssessmentFrameworkControlTypeDef = TypedDict(
    "CreateAssessmentFrameworkControlTypeDef", {"id": str}, total=False
)


class CreateAssessmentFrameworkResponseTypeDef(TypedDict, total=False):
    framework: "FrameworkTypeDef"


class CreateAssessmentReportResponseTypeDef(TypedDict, total=False):
    assessmentReport: "AssessmentReportTypeDef"


class CreateAssessmentResponseTypeDef(TypedDict, total=False):
    assessment: "AssessmentTypeDef"


class CreateControlMappingSourceTypeDef(TypedDict, total=False):
    sourceName: str
    sourceDescription: str
    sourceSetUpOption: SourceSetUpOption
    sourceType: SourceType
    sourceKeyword: "SourceKeywordTypeDef"
    sourceFrequency: SourceFrequency
    troubleshootingText: str


class CreateControlResponseTypeDef(TypedDict, total=False):
    control: "ControlTypeDef"


class CreateDelegationRequestTypeDef(TypedDict, total=False):
    comment: str
    controlSetId: str
    roleArn: str
    roleType: RoleType


DelegationMetadataTypeDef = TypedDict(
    "DelegationMetadataTypeDef",
    {
        "id": str,
        "assessmentName": str,
        "assessmentId": str,
        "status": DelegationStatus,
        "roleArn": str,
        "creationTime": datetime,
        "controlSetName": str,
    },
    total=False,
)

DelegationTypeDef = TypedDict(
    "DelegationTypeDef",
    {
        "id": str,
        "assessmentName": str,
        "assessmentId": str,
        "status": DelegationStatus,
        "roleArn": str,
        "roleType": RoleType,
        "creationTime": datetime,
        "lastUpdated": datetime,
        "controlSetId": str,
        "comment": str,
        "createdBy": str,
    },
    total=False,
)


class DeregisterAccountResponseTypeDef(TypedDict, total=False):
    status: AccountStatus


EvidenceTypeDef = TypedDict(
    "EvidenceTypeDef",
    {
        "dataSource": str,
        "evidenceAwsAccountId": str,
        "time": datetime,
        "eventSource": str,
        "eventName": str,
        "evidenceByType": str,
        "resourcesIncluded": List["ResourceTypeDef"],
        "attributes": Dict[str, str],
        "iamId": str,
        "complianceCheck": str,
        "awsOrganization": str,
        "awsAccountId": str,
        "evidenceFolderId": str,
        "id": str,
        "assessmentReportSelection": str,
    },
    total=False,
)


class FrameworkMetadataTypeDef(TypedDict, total=False):
    name: str
    description: str
    logo: str
    complianceType: str


FrameworkTypeDef = TypedDict(
    "FrameworkTypeDef",
    {
        "arn": str,
        "id": str,
        "name": str,
        "type": FrameworkType,
        "complianceType": str,
        "description": str,
        "logo": str,
        "controlSources": str,
        "controlSets": List["ControlSetTypeDef"],
        "createdAt": datetime,
        "lastUpdatedAt": datetime,
        "createdBy": str,
        "lastUpdatedBy": str,
        "tags": Dict[str, str],
    },
    total=False,
)


class GetAccountStatusResponseTypeDef(TypedDict, total=False):
    status: AccountStatus


class GetAssessmentFrameworkResponseTypeDef(TypedDict, total=False):
    framework: "FrameworkTypeDef"


class GetAssessmentReportUrlResponseTypeDef(TypedDict, total=False):
    preSignedUrl: "URLTypeDef"


class GetAssessmentResponseTypeDef(TypedDict, total=False):
    assessment: "AssessmentTypeDef"
    userRole: "RoleTypeDef"


class GetChangeLogsResponseTypeDef(TypedDict, total=False):
    changeLogs: List["ChangeLogTypeDef"]
    nextToken: str


class GetControlResponseTypeDef(TypedDict, total=False):
    control: "ControlTypeDef"


class GetDelegationsResponseTypeDef(TypedDict, total=False):
    delegations: List["DelegationMetadataTypeDef"]
    nextToken: str


class GetEvidenceByEvidenceFolderResponseTypeDef(TypedDict, total=False):
    evidence: List["EvidenceTypeDef"]
    nextToken: str


class GetEvidenceFolderResponseTypeDef(TypedDict, total=False):
    evidenceFolder: "AssessmentEvidenceFolderTypeDef"


class GetEvidenceFoldersByAssessmentControlResponseTypeDef(TypedDict, total=False):
    evidenceFolders: List["AssessmentEvidenceFolderTypeDef"]
    nextToken: str


class GetEvidenceFoldersByAssessmentResponseTypeDef(TypedDict, total=False):
    evidenceFolders: List["AssessmentEvidenceFolderTypeDef"]
    nextToken: str


class GetEvidenceResponseTypeDef(TypedDict, total=False):
    evidence: "EvidenceTypeDef"


class GetOrganizationAdminAccountResponseTypeDef(TypedDict, total=False):
    adminAccountId: str
    organizationId: str


class GetServicesInScopeResponseTypeDef(TypedDict, total=False):
    serviceMetadata: List["ServiceMetadataTypeDef"]


class GetSettingsResponseTypeDef(TypedDict, total=False):
    settings: "SettingsTypeDef"


class ListAssessmentFrameworksResponseTypeDef(TypedDict, total=False):
    frameworkMetadataList: List["AssessmentFrameworkMetadataTypeDef"]
    nextToken: str


class ListAssessmentReportsResponseTypeDef(TypedDict, total=False):
    assessmentReports: List["AssessmentReportMetadataTypeDef"]
    nextToken: str


class ListAssessmentsResponseTypeDef(TypedDict, total=False):
    assessmentMetadata: List["AssessmentMetadataItemTypeDef"]
    nextToken: str


class ListControlsResponseTypeDef(TypedDict, total=False):
    controlMetadataList: List["ControlMetadataTypeDef"]
    nextToken: str


class ListKeywordsForDataSourceResponseTypeDef(TypedDict, total=False):
    keywords: List[str]
    nextToken: str


class ListNotificationsResponseTypeDef(TypedDict, total=False):
    notifications: List["NotificationTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class ManualEvidenceTypeDef(TypedDict, total=False):
    s3ResourcePath: str


NotificationTypeDef = TypedDict(
    "NotificationTypeDef",
    {
        "id": str,
        "assessmentId": str,
        "assessmentName": str,
        "controlSetId": str,
        "controlSetName": str,
        "description": str,
        "eventTime": datetime,
        "source": str,
    },
    total=False,
)


class RegisterAccountResponseTypeDef(TypedDict, total=False):
    status: AccountStatus


class RegisterOrganizationAdminAccountResponseTypeDef(TypedDict, total=False):
    adminAccountId: str
    organizationId: str


class ResourceTypeDef(TypedDict, total=False):
    arn: str
    value: str


class RoleTypeDef(TypedDict, total=False):
    roleType: RoleType
    roleArn: str


class ScopeTypeDef(TypedDict, total=False):
    awsAccounts: List["AWSAccountTypeDef"]
    awsServices: List["AWSServiceTypeDef"]


class ServiceMetadataTypeDef(TypedDict, total=False):
    name: str
    displayName: str
    description: str
    category: str


class SettingsTypeDef(TypedDict, total=False):
    isAwsOrgEnabled: bool
    snsTopic: str
    defaultAssessmentReportsDestination: "AssessmentReportsDestinationTypeDef"
    defaultProcessOwners: List["RoleTypeDef"]
    kmsKey: str


class SourceKeywordTypeDef(TypedDict, total=False):
    keywordInputType: Literal["SELECT_FROM_LIST"]
    keywordValue: str


class URLTypeDef(TypedDict, total=False):
    hyperlinkName: str
    link: str


class UpdateAssessmentControlResponseTypeDef(TypedDict, total=False):
    control: "AssessmentControlTypeDef"


class UpdateAssessmentControlSetStatusResponseTypeDef(TypedDict, total=False):
    controlSet: "AssessmentControlSetTypeDef"


_RequiredUpdateAssessmentFrameworkControlSetTypeDef = TypedDict(
    "_RequiredUpdateAssessmentFrameworkControlSetTypeDef", {"name": str}
)
_OptionalUpdateAssessmentFrameworkControlSetTypeDef = TypedDict(
    "_OptionalUpdateAssessmentFrameworkControlSetTypeDef",
    {"id": str, "controls": List["CreateAssessmentFrameworkControlTypeDef"]},
    total=False,
)


class UpdateAssessmentFrameworkControlSetTypeDef(
    _RequiredUpdateAssessmentFrameworkControlSetTypeDef,
    _OptionalUpdateAssessmentFrameworkControlSetTypeDef,
):
    pass


class UpdateAssessmentFrameworkResponseTypeDef(TypedDict, total=False):
    framework: "FrameworkTypeDef"


class UpdateAssessmentResponseTypeDef(TypedDict, total=False):
    assessment: "AssessmentTypeDef"


class UpdateAssessmentStatusResponseTypeDef(TypedDict, total=False):
    assessment: "AssessmentTypeDef"


class UpdateControlResponseTypeDef(TypedDict, total=False):
    control: "ControlTypeDef"


class UpdateSettingsResponseTypeDef(TypedDict, total=False):
    settings: "SettingsTypeDef"


class ValidateAssessmentReportIntegrityResponseTypeDef(TypedDict, total=False):
    signatureValid: bool
    signatureAlgorithm: str
    signatureDateTime: str
    signatureKeyId: str
    validationErrors: List[str]
