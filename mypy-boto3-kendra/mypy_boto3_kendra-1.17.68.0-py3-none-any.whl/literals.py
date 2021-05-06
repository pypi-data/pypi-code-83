"""
Type annotations for kendra service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_kendra/literals.html)

Usage::

    ```python
    from mypy_boto3_kendra.literals import AdditionalResultAttributeValueType

    data: AdditionalResultAttributeValueType = "TEXT_WITH_HIGHLIGHTS_VALUE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AdditionalResultAttributeValueType",
    "ConfluenceAttachmentFieldName",
    "ConfluenceBlogFieldName",
    "ConfluencePageFieldName",
    "ConfluenceSpaceFieldName",
    "ConfluenceVersion",
    "ContentType",
    "DataSourceStatus",
    "DataSourceSyncJobStatus",
    "DataSourceType",
    "DatabaseEngineType",
    "DocumentAttributeValueType",
    "ErrorCode",
    "FaqFileFormat",
    "FaqStatus",
    "HighlightType",
    "IndexEdition",
    "IndexStatus",
    "KeyLocation",
    "Order",
    "PrincipalType",
    "QueryIdentifiersEnclosingOption",
    "QueryResultType",
    "ReadAccessType",
    "RelevanceType",
    "SalesforceChatterFeedIncludeFilterType",
    "SalesforceKnowledgeArticleState",
    "SalesforceStandardObjectName",
    "ScoreConfidence",
    "ServiceNowAuthenticationType",
    "ServiceNowBuildVersionType",
    "SharePointVersion",
    "SortOrder",
    "ThesaurusStatus",
    "UserContextPolicy",
)


AdditionalResultAttributeValueType = Literal["TEXT_WITH_HIGHLIGHTS_VALUE"]
ConfluenceAttachmentFieldName = Literal[
    "AUTHOR",
    "CONTENT_TYPE",
    "CREATED_DATE",
    "DISPLAY_URL",
    "FILE_SIZE",
    "ITEM_TYPE",
    "PARENT_ID",
    "SPACE_KEY",
    "SPACE_NAME",
    "URL",
    "VERSION",
]
ConfluenceBlogFieldName = Literal[
    "AUTHOR",
    "DISPLAY_URL",
    "ITEM_TYPE",
    "LABELS",
    "PUBLISH_DATE",
    "SPACE_KEY",
    "SPACE_NAME",
    "URL",
    "VERSION",
]
ConfluencePageFieldName = Literal[
    "AUTHOR",
    "CONTENT_STATUS",
    "CREATED_DATE",
    "DISPLAY_URL",
    "ITEM_TYPE",
    "LABELS",
    "MODIFIED_DATE",
    "PARENT_ID",
    "SPACE_KEY",
    "SPACE_NAME",
    "URL",
    "VERSION",
]
ConfluenceSpaceFieldName = Literal["DISPLAY_URL", "ITEM_TYPE", "SPACE_KEY", "URL"]
ConfluenceVersion = Literal["CLOUD", "SERVER"]
ContentType = Literal["HTML", "MS_WORD", "PDF", "PLAIN_TEXT", "PPT"]
DataSourceStatus = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
DataSourceSyncJobStatus = Literal[
    "ABORTED", "FAILED", "INCOMPLETE", "STOPPING", "SUCCEEDED", "SYNCING", "SYNCING_INDEXING"
]
DataSourceType = Literal[
    "CONFLUENCE",
    "CUSTOM",
    "DATABASE",
    "GOOGLEDRIVE",
    "ONEDRIVE",
    "S3",
    "SALESFORCE",
    "SERVICENOW",
    "SHAREPOINT",
]
DatabaseEngineType = Literal[
    "RDS_AURORA_MYSQL", "RDS_AURORA_POSTGRESQL", "RDS_MYSQL", "RDS_POSTGRESQL"
]
DocumentAttributeValueType = Literal[
    "DATE_VALUE", "LONG_VALUE", "STRING_LIST_VALUE", "STRING_VALUE"
]
ErrorCode = Literal["InternalError", "InvalidRequest"]
FaqFileFormat = Literal["CSV", "CSV_WITH_HEADER", "JSON"]
FaqStatus = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "UPDATING"]
HighlightType = Literal["STANDARD", "THESAURUS_SYNONYM"]
IndexEdition = Literal["DEVELOPER_EDITION", "ENTERPRISE_EDITION"]
IndexStatus = Literal["ACTIVE", "CREATING", "DELETING", "FAILED", "SYSTEM_UPDATING", "UPDATING"]
KeyLocation = Literal["SECRET_MANAGER", "URL"]
Order = Literal["ASCENDING", "DESCENDING"]
PrincipalType = Literal["GROUP", "USER"]
QueryIdentifiersEnclosingOption = Literal["DOUBLE_QUOTES", "NONE"]
QueryResultType = Literal["ANSWER", "DOCUMENT", "QUESTION_ANSWER"]
ReadAccessType = Literal["ALLOW", "DENY"]
RelevanceType = Literal["NOT_RELEVANT", "RELEVANT"]
SalesforceChatterFeedIncludeFilterType = Literal["ACTIVE_USER", "STANDARD_USER"]
SalesforceKnowledgeArticleState = Literal["ARCHIVED", "DRAFT", "PUBLISHED"]
SalesforceStandardObjectName = Literal[
    "ACCOUNT",
    "CAMPAIGN",
    "CASE",
    "CONTACT",
    "CONTRACT",
    "DOCUMENT",
    "GROUP",
    "IDEA",
    "LEAD",
    "OPPORTUNITY",
    "PARTNER",
    "PRICEBOOK",
    "PRODUCT",
    "PROFILE",
    "SOLUTION",
    "TASK",
    "USER",
]
ScoreConfidence = Literal["HIGH", "LOW", "MEDIUM", "VERY_HIGH"]
ServiceNowAuthenticationType = Literal["HTTP_BASIC", "OAUTH2"]
ServiceNowBuildVersionType = Literal["LONDON", "OTHERS"]
SharePointVersion = Literal["SHAREPOINT_ONLINE"]
SortOrder = Literal["ASC", "DESC"]
ThesaurusStatus = Literal[
    "ACTIVE", "ACTIVE_BUT_UPDATE_FAILED", "CREATING", "DELETING", "FAILED", "UPDATING"
]
UserContextPolicy = Literal["ATTRIBUTE_FILTER", "USER_TOKEN"]
