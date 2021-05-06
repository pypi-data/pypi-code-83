"""
Type annotations for accessanalyzer service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_accessanalyzer/literals.html)

Usage::

    ```python
    from mypy_boto3_accessanalyzer.literals import AccessPreviewStatus

    data: AccessPreviewStatus = "COMPLETED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccessPreviewStatus",
    "AccessPreviewStatusReasonCode",
    "AclPermission",
    "AnalyzerStatus",
    "FindingChangeType",
    "FindingSourceType",
    "FindingStatus",
    "FindingStatusUpdate",
    "JobErrorCode",
    "JobStatus",
    "KmsGrantOperation",
    "ListAccessPreviewFindingsPaginatorName",
    "ListAccessPreviewsPaginatorName",
    "ListAnalyzedResourcesPaginatorName",
    "ListAnalyzersPaginatorName",
    "ListArchiveRulesPaginatorName",
    "ListFindingsPaginatorName",
    "ListPolicyGenerationsPaginatorName",
    "Locale",
    "OrderBy",
    "PolicyType",
    "ReasonCode",
    "ResourceType",
    "TypeType",
    "ValidatePolicyFindingType",
    "ValidatePolicyPaginatorName",
)


AccessPreviewStatus = Literal["COMPLETED", "CREATING", "FAILED"]
AccessPreviewStatusReasonCode = Literal["INTERNAL_ERROR", "INVALID_CONFIGURATION"]
AclPermission = Literal["FULL_CONTROL", "READ", "READ_ACP", "WRITE", "WRITE_ACP"]
AnalyzerStatus = Literal["ACTIVE", "CREATING", "DISABLED", "FAILED"]
FindingChangeType = Literal["CHANGED", "NEW", "UNCHANGED"]
FindingSourceType = Literal["BUCKET_ACL", "POLICY", "S3_ACCESS_POINT"]
FindingStatus = Literal["ACTIVE", "ARCHIVED", "RESOLVED"]
FindingStatusUpdate = Literal["ACTIVE", "ARCHIVED"]
JobErrorCode = Literal[
    "AUTHORIZATION_ERROR",
    "RESOURCE_NOT_FOUND_ERROR",
    "SERVICE_ERROR",
    "SERVICE_QUOTA_EXCEEDED_ERROR",
]
JobStatus = Literal["CANCELED", "FAILED", "IN_PROGRESS", "SUCCEEDED"]
KmsGrantOperation = Literal[
    "CreateGrant",
    "Decrypt",
    "DescribeKey",
    "Encrypt",
    "GenerateDataKey",
    "GenerateDataKeyPair",
    "GenerateDataKeyPairWithoutPlaintext",
    "GenerateDataKeyWithoutPlaintext",
    "GetPublicKey",
    "ReEncryptFrom",
    "ReEncryptTo",
    "RetireGrant",
    "Sign",
    "Verify",
]
ListAccessPreviewFindingsPaginatorName = Literal["list_access_preview_findings"]
ListAccessPreviewsPaginatorName = Literal["list_access_previews"]
ListAnalyzedResourcesPaginatorName = Literal["list_analyzed_resources"]
ListAnalyzersPaginatorName = Literal["list_analyzers"]
ListArchiveRulesPaginatorName = Literal["list_archive_rules"]
ListFindingsPaginatorName = Literal["list_findings"]
ListPolicyGenerationsPaginatorName = Literal["list_policy_generations"]
Locale = Literal["DE", "EN", "ES", "FR", "IT", "JA", "KO", "PT_BR", "ZH_CN", "ZH_TW"]
OrderBy = Literal["ASC", "DESC"]
PolicyType = Literal["IDENTITY_POLICY", "RESOURCE_POLICY", "SERVICE_CONTROL_POLICY"]
ReasonCode = Literal[
    "AWS_SERVICE_ACCESS_DISABLED",
    "DELEGATED_ADMINISTRATOR_DEREGISTERED",
    "ORGANIZATION_DELETED",
    "SERVICE_LINKED_ROLE_CREATION_FAILED",
]
ResourceType = Literal[
    "AWS::IAM::Role",
    "AWS::KMS::Key",
    "AWS::Lambda::Function",
    "AWS::Lambda::LayerVersion",
    "AWS::S3::Bucket",
    "AWS::SQS::Queue",
    "AWS::SecretsManager::Secret",
]
TypeType = Literal["ACCOUNT", "ORGANIZATION"]
ValidatePolicyFindingType = Literal["ERROR", "SECURITY_WARNING", "SUGGESTION", "WARNING"]
ValidatePolicyPaginatorName = Literal["validate_policy"]
