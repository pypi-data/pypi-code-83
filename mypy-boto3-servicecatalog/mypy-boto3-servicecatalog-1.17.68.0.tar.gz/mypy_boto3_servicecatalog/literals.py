"""
Type annotations for servicecatalog service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/literals.html)

Usage::

    ```python
    from mypy_boto3_servicecatalog.literals import AccessLevelFilterKey

    data: AccessLevelFilterKey = "Account"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AccessLevelFilterKey",
    "AccessStatus",
    "ChangeAction",
    "CopyOption",
    "CopyProductStatus",
    "DescribePortfolioShareType",
    "EvaluationType",
    "ListAcceptedPortfolioSharesPaginatorName",
    "ListConstraintsForPortfolioPaginatorName",
    "ListLaunchPathsPaginatorName",
    "ListOrganizationPortfolioAccessPaginatorName",
    "ListPortfoliosForProductPaginatorName",
    "ListPortfoliosPaginatorName",
    "ListPrincipalsForPortfolioPaginatorName",
    "ListProvisionedProductPlansPaginatorName",
    "ListProvisioningArtifactsForServiceActionPaginatorName",
    "ListRecordHistoryPaginatorName",
    "ListResourcesForTagOptionPaginatorName",
    "ListServiceActionsForProvisioningArtifactPaginatorName",
    "ListServiceActionsPaginatorName",
    "ListTagOptionsPaginatorName",
    "OrganizationNodeType",
    "PortfolioShareType",
    "PrincipalType",
    "ProductSource",
    "ProductType",
    "ProductViewFilterBy",
    "ProductViewSortBy",
    "PropertyKey",
    "ProvisionedProductPlanStatus",
    "ProvisionedProductPlanType",
    "ProvisionedProductStatus",
    "ProvisionedProductViewFilterBy",
    "ProvisioningArtifactGuidance",
    "ProvisioningArtifactPropertyName",
    "ProvisioningArtifactType",
    "RecordStatus",
    "Replacement",
    "RequiresRecreation",
    "ResourceAttribute",
    "ScanProvisionedProductsPaginatorName",
    "SearchProductsAsAdminPaginatorName",
    "ServiceActionAssociationErrorCode",
    "ServiceActionDefinitionKey",
    "ServiceActionDefinitionType",
    "ShareStatus",
    "SortOrder",
    "StackInstanceStatus",
    "StackSetOperationType",
    "Status",
)


AccessLevelFilterKey = Literal["Account", "Role", "User"]
AccessStatus = Literal["DISABLED", "ENABLED", "UNDER_CHANGE"]
ChangeAction = Literal["ADD", "MODIFY", "REMOVE"]
CopyOption = Literal["CopyTags"]
CopyProductStatus = Literal["FAILED", "IN_PROGRESS", "SUCCEEDED"]
DescribePortfolioShareType = Literal[
    "ACCOUNT", "ORGANIZATION", "ORGANIZATIONAL_UNIT", "ORGANIZATION_MEMBER_ACCOUNT"
]
EvaluationType = Literal["DYNAMIC", "STATIC"]
ListAcceptedPortfolioSharesPaginatorName = Literal["list_accepted_portfolio_shares"]
ListConstraintsForPortfolioPaginatorName = Literal["list_constraints_for_portfolio"]
ListLaunchPathsPaginatorName = Literal["list_launch_paths"]
ListOrganizationPortfolioAccessPaginatorName = Literal["list_organization_portfolio_access"]
ListPortfoliosForProductPaginatorName = Literal["list_portfolios_for_product"]
ListPortfoliosPaginatorName = Literal["list_portfolios"]
ListPrincipalsForPortfolioPaginatorName = Literal["list_principals_for_portfolio"]
ListProvisionedProductPlansPaginatorName = Literal["list_provisioned_product_plans"]
ListProvisioningArtifactsForServiceActionPaginatorName = Literal[
    "list_provisioning_artifacts_for_service_action"
]
ListRecordHistoryPaginatorName = Literal["list_record_history"]
ListResourcesForTagOptionPaginatorName = Literal["list_resources_for_tag_option"]
ListServiceActionsForProvisioningArtifactPaginatorName = Literal[
    "list_service_actions_for_provisioning_artifact"
]
ListServiceActionsPaginatorName = Literal["list_service_actions"]
ListTagOptionsPaginatorName = Literal["list_tag_options"]
OrganizationNodeType = Literal["ACCOUNT", "ORGANIZATION", "ORGANIZATIONAL_UNIT"]
PortfolioShareType = Literal["AWS_ORGANIZATIONS", "AWS_SERVICECATALOG", "IMPORTED"]
PrincipalType = Literal["IAM"]
ProductSource = Literal["ACCOUNT"]
ProductType = Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE"]
ProductViewFilterBy = Literal["FullTextSearch", "Owner", "ProductType", "SourceProductId"]
ProductViewSortBy = Literal["CreationDate", "Title", "VersionCount"]
PropertyKey = Literal["LAUNCH_ROLE", "OWNER"]
ProvisionedProductPlanStatus = Literal[
    "CREATE_FAILED",
    "CREATE_IN_PROGRESS",
    "CREATE_SUCCESS",
    "EXECUTE_FAILED",
    "EXECUTE_IN_PROGRESS",
    "EXECUTE_SUCCESS",
]
ProvisionedProductPlanType = Literal["CLOUDFORMATION"]
ProvisionedProductStatus = Literal[
    "AVAILABLE", "ERROR", "PLAN_IN_PROGRESS", "TAINTED", "UNDER_CHANGE"
]
ProvisionedProductViewFilterBy = Literal["SearchQuery"]
ProvisioningArtifactGuidance = Literal["DEFAULT", "DEPRECATED"]
ProvisioningArtifactPropertyName = Literal["Id"]
ProvisioningArtifactType = Literal["CLOUD_FORMATION_TEMPLATE", "MARKETPLACE_AMI", "MARKETPLACE_CAR"]
RecordStatus = Literal["CREATED", "FAILED", "IN_PROGRESS", "IN_PROGRESS_IN_ERROR", "SUCCEEDED"]
Replacement = Literal["CONDITIONAL", "FALSE", "TRUE"]
RequiresRecreation = Literal["ALWAYS", "CONDITIONALLY", "NEVER"]
ResourceAttribute = Literal[
    "CREATIONPOLICY", "DELETIONPOLICY", "METADATA", "PROPERTIES", "TAGS", "UPDATEPOLICY"
]
ScanProvisionedProductsPaginatorName = Literal["scan_provisioned_products"]
SearchProductsAsAdminPaginatorName = Literal["search_products_as_admin"]
ServiceActionAssociationErrorCode = Literal[
    "DUPLICATE_RESOURCE", "INTERNAL_FAILURE", "LIMIT_EXCEEDED", "RESOURCE_NOT_FOUND", "THROTTLING"
]
ServiceActionDefinitionKey = Literal["AssumeRole", "Name", "Parameters", "Version"]
ServiceActionDefinitionType = Literal["SSM_AUTOMATION"]
ShareStatus = Literal["COMPLETED", "COMPLETED_WITH_ERRORS", "ERROR", "IN_PROGRESS", "NOT_STARTED"]
SortOrder = Literal["ASCENDING", "DESCENDING"]
StackInstanceStatus = Literal["CURRENT", "INOPERABLE", "OUTDATED"]
StackSetOperationType = Literal["CREATE", "DELETE", "UPDATE"]
Status = Literal["AVAILABLE", "CREATING", "FAILED"]
