"""
Type annotations for quicksight service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_quicksight/literals.html)

Usage::

    ```python
    from mypy_boto3_quicksight.literals import AnalysisErrorType

    data: AnalysisErrorType = "ACCESS_DENIED"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AnalysisErrorType",
    "AnalysisFilterAttribute",
    "AssignmentStatus",
    "ColumnDataType",
    "DashboardBehavior",
    "DashboardErrorType",
    "DashboardFilterAttribute",
    "DashboardUIState",
    "DataSetImportMode",
    "DataSourceErrorInfoType",
    "DataSourceType",
    "Edition",
    "EmbeddingIdentityType",
    "FileFormat",
    "FilterOperator",
    "GeoSpatialCountryCode",
    "GeoSpatialDataRole",
    "IdentityStore",
    "IdentityType",
    "IngestionErrorType",
    "IngestionRequestSource",
    "IngestionRequestType",
    "IngestionStatus",
    "InputColumnDataType",
    "JoinType",
    "ListAnalysesPaginatorName",
    "ListDashboardVersionsPaginatorName",
    "ListDashboardsPaginatorName",
    "ListDataSetsPaginatorName",
    "ListDataSourcesPaginatorName",
    "ListIngestionsPaginatorName",
    "ListNamespacesPaginatorName",
    "ListTemplateAliasesPaginatorName",
    "ListTemplateVersionsPaginatorName",
    "ListTemplatesPaginatorName",
    "ListThemeVersionsPaginatorName",
    "ListThemesPaginatorName",
    "NamespaceErrorType",
    "NamespaceStatus",
    "ResourceStatus",
    "RowLevelPermissionPolicy",
    "SearchAnalysesPaginatorName",
    "SearchDashboardsPaginatorName",
    "TemplateErrorType",
    "TextQualifier",
    "ThemeErrorType",
    "ThemeType",
    "UserRole",
)


AnalysisErrorType = Literal[
    "ACCESS_DENIED",
    "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
    "COLUMN_REPLACEMENT_MISSING",
    "COLUMN_TYPE_MISMATCH",
    "DATA_SET_NOT_FOUND",
    "INTERNAL_FAILURE",
    "PARAMETER_NOT_FOUND",
    "PARAMETER_TYPE_INVALID",
    "PARAMETER_VALUE_INCOMPATIBLE",
    "SOURCE_NOT_FOUND",
]
AnalysisFilterAttribute = Literal["QUICKSIGHT_USER"]
AssignmentStatus = Literal["DISABLED", "DRAFT", "ENABLED"]
ColumnDataType = Literal["DATETIME", "DECIMAL", "INTEGER", "STRING"]
DashboardBehavior = Literal["DISABLED", "ENABLED"]
DashboardErrorType = Literal[
    "ACCESS_DENIED",
    "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
    "COLUMN_REPLACEMENT_MISSING",
    "COLUMN_TYPE_MISMATCH",
    "DATA_SET_NOT_FOUND",
    "INTERNAL_FAILURE",
    "PARAMETER_NOT_FOUND",
    "PARAMETER_TYPE_INVALID",
    "PARAMETER_VALUE_INCOMPATIBLE",
    "SOURCE_NOT_FOUND",
]
DashboardFilterAttribute = Literal["QUICKSIGHT_USER"]
DashboardUIState = Literal["COLLAPSED", "EXPANDED"]
DataSetImportMode = Literal["DIRECT_QUERY", "SPICE"]
DataSourceErrorInfoType = Literal[
    "ACCESS_DENIED",
    "CONFLICT",
    "COPY_SOURCE_NOT_FOUND",
    "ENGINE_VERSION_NOT_SUPPORTED",
    "GENERIC_SQL_FAILURE",
    "TIMEOUT",
    "UNKNOWN",
    "UNKNOWN_HOST",
]
DataSourceType = Literal[
    "ADOBE_ANALYTICS",
    "AMAZON_ELASTICSEARCH",
    "ATHENA",
    "AURORA",
    "AURORA_POSTGRESQL",
    "AWS_IOT_ANALYTICS",
    "GITHUB",
    "JIRA",
    "MARIADB",
    "MYSQL",
    "ORACLE",
    "POSTGRESQL",
    "PRESTO",
    "REDSHIFT",
    "S3",
    "SALESFORCE",
    "SERVICENOW",
    "SNOWFLAKE",
    "SPARK",
    "SQLSERVER",
    "TERADATA",
    "TIMESTREAM",
    "TWITTER",
]
Edition = Literal["ENTERPRISE", "STANDARD"]
EmbeddingIdentityType = Literal["ANONYMOUS", "IAM", "QUICKSIGHT"]
FileFormat = Literal["CLF", "CSV", "ELF", "JSON", "TSV", "XLSX"]
FilterOperator = Literal["StringEquals"]
GeoSpatialCountryCode = Literal["US"]
GeoSpatialDataRole = Literal[
    "CITY", "COUNTRY", "COUNTY", "LATITUDE", "LONGITUDE", "POSTCODE", "STATE"
]
IdentityStore = Literal["QUICKSIGHT"]
IdentityType = Literal["IAM", "QUICKSIGHT"]
IngestionErrorType = Literal[
    "ACCOUNT_CAPACITY_LIMIT_EXCEEDED",
    "CONNECTION_FAILURE",
    "CUSTOMER_ERROR",
    "DATA_SET_DELETED",
    "DATA_SET_NOT_SPICE",
    "DATA_SET_SIZE_LIMIT_EXCEEDED",
    "DATA_SOURCE_AUTH_FAILED",
    "DATA_SOURCE_CONNECTION_FAILED",
    "DATA_SOURCE_NOT_FOUND",
    "DATA_TOLERANCE_EXCEPTION",
    "FAILURE_TO_ASSUME_ROLE",
    "FAILURE_TO_PROCESS_JSON_FILE",
    "IAM_ROLE_NOT_AVAILABLE",
    "INGESTION_CANCELED",
    "INGESTION_SUPERSEDED",
    "INTERNAL_SERVICE_ERROR",
    "INVALID_DATAPREP_SYNTAX",
    "INVALID_DATA_SOURCE_CONFIG",
    "INVALID_DATE_FORMAT",
    "IOT_DATA_SET_FILE_EMPTY",
    "IOT_FILE_NOT_FOUND",
    "OAUTH_TOKEN_FAILURE",
    "PASSWORD_AUTHENTICATION_FAILURE",
    "PERMISSION_DENIED",
    "QUERY_TIMEOUT",
    "ROW_SIZE_LIMIT_EXCEEDED",
    "S3_FILE_INACCESSIBLE",
    "S3_MANIFEST_ERROR",
    "S3_UPLOADED_FILE_DELETED",
    "SOURCE_API_LIMIT_EXCEEDED_FAILURE",
    "SOURCE_RESOURCE_LIMIT_EXCEEDED",
    "SPICE_TABLE_NOT_FOUND",
    "SQL_EXCEPTION",
    "SQL_INVALID_PARAMETER_VALUE",
    "SQL_NUMERIC_OVERFLOW",
    "SQL_SCHEMA_MISMATCH_ERROR",
    "SQL_TABLE_NOT_FOUND",
    "SSL_CERTIFICATE_VALIDATION_FAILURE",
    "UNRESOLVABLE_HOST",
    "UNROUTABLE_HOST",
]
IngestionRequestSource = Literal["MANUAL", "SCHEDULED"]
IngestionRequestType = Literal["EDIT", "FULL_REFRESH", "INCREMENTAL_REFRESH", "INITIAL_INGESTION"]
IngestionStatus = Literal["CANCELLED", "COMPLETED", "FAILED", "INITIALIZED", "QUEUED", "RUNNING"]
InputColumnDataType = Literal["BIT", "BOOLEAN", "DATETIME", "DECIMAL", "INTEGER", "JSON", "STRING"]
JoinType = Literal["INNER", "LEFT", "OUTER", "RIGHT"]
ListAnalysesPaginatorName = Literal["list_analyses"]
ListDashboardVersionsPaginatorName = Literal["list_dashboard_versions"]
ListDashboardsPaginatorName = Literal["list_dashboards"]
ListDataSetsPaginatorName = Literal["list_data_sets"]
ListDataSourcesPaginatorName = Literal["list_data_sources"]
ListIngestionsPaginatorName = Literal["list_ingestions"]
ListNamespacesPaginatorName = Literal["list_namespaces"]
ListTemplateAliasesPaginatorName = Literal["list_template_aliases"]
ListTemplateVersionsPaginatorName = Literal["list_template_versions"]
ListTemplatesPaginatorName = Literal["list_templates"]
ListThemeVersionsPaginatorName = Literal["list_theme_versions"]
ListThemesPaginatorName = Literal["list_themes"]
NamespaceErrorType = Literal["INTERNAL_SERVICE_ERROR", "PERMISSION_DENIED"]
NamespaceStatus = Literal[
    "CREATED", "CREATING", "DELETING", "NON_RETRYABLE_FAILURE", "RETRYABLE_FAILURE"
]
ResourceStatus = Literal[
    "CREATION_FAILED",
    "CREATION_IN_PROGRESS",
    "CREATION_SUCCESSFUL",
    "DELETED",
    "UPDATE_FAILED",
    "UPDATE_IN_PROGRESS",
    "UPDATE_SUCCESSFUL",
]
RowLevelPermissionPolicy = Literal["DENY_ACCESS", "GRANT_ACCESS"]
SearchAnalysesPaginatorName = Literal["search_analyses"]
SearchDashboardsPaginatorName = Literal["search_dashboards"]
TemplateErrorType = Literal[
    "ACCESS_DENIED", "DATA_SET_NOT_FOUND", "INTERNAL_FAILURE", "SOURCE_NOT_FOUND"
]
TextQualifier = Literal["DOUBLE_QUOTE", "SINGLE_QUOTE"]
ThemeErrorType = Literal["INTERNAL_FAILURE"]
ThemeType = Literal["ALL", "CUSTOM", "QUICKSIGHT"]
UserRole = Literal["ADMIN", "AUTHOR", "READER", "RESTRICTED_AUTHOR", "RESTRICTED_READER"]
