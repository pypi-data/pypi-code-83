"""
Type annotations for servicecatalog service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_servicecatalog import ServiceCatalogClient

    client: ServiceCatalogClient = boto3.client("servicecatalog")
    ```
"""
import sys
from typing import Any, Dict, List, Type, overload

from botocore.client import ClientMeta

from mypy_boto3_servicecatalog.literals import (
    DescribePortfolioShareType,
    OrganizationNodeType,
    PortfolioShareType,
    ProductType,
    ProductViewFilterBy,
    ProductViewSortBy,
    PropertyKey,
    ProvisioningArtifactGuidance,
    ServiceActionDefinitionKey,
    SortOrder,
)
from mypy_boto3_servicecatalog.paginator import (
    ListAcceptedPortfolioSharesPaginator,
    ListConstraintsForPortfolioPaginator,
    ListLaunchPathsPaginator,
    ListOrganizationPortfolioAccessPaginator,
    ListPortfoliosForProductPaginator,
    ListPortfoliosPaginator,
    ListPrincipalsForPortfolioPaginator,
    ListProvisionedProductPlansPaginator,
    ListProvisioningArtifactsForServiceActionPaginator,
    ListRecordHistoryPaginator,
    ListResourcesForTagOptionPaginator,
    ListServiceActionsForProvisioningArtifactPaginator,
    ListServiceActionsPaginator,
    ListTagOptionsPaginator,
    ScanProvisionedProductsPaginator,
    SearchProductsAsAdminPaginator,
)
from mypy_boto3_servicecatalog.type_defs import (
    AccessLevelFilterTypeDef,
    BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef,
    BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef,
    CopyProductOutputTypeDef,
    CreateConstraintOutputTypeDef,
    CreatePortfolioOutputTypeDef,
    CreatePortfolioShareOutputTypeDef,
    CreateProductOutputTypeDef,
    CreateProvisionedProductPlanOutputTypeDef,
    CreateProvisioningArtifactOutputTypeDef,
    CreateServiceActionOutputTypeDef,
    CreateTagOptionOutputTypeDef,
    DeletePortfolioShareOutputTypeDef,
    DescribeConstraintOutputTypeDef,
    DescribeCopyProductStatusOutputTypeDef,
    DescribePortfolioOutputTypeDef,
    DescribePortfolioSharesOutputTypeDef,
    DescribePortfolioShareStatusOutputTypeDef,
    DescribeProductAsAdminOutputTypeDef,
    DescribeProductOutputTypeDef,
    DescribeProductViewOutputTypeDef,
    DescribeProvisionedProductOutputTypeDef,
    DescribeProvisionedProductPlanOutputTypeDef,
    DescribeProvisioningArtifactOutputTypeDef,
    DescribeProvisioningParametersOutputTypeDef,
    DescribeRecordOutputTypeDef,
    DescribeServiceActionExecutionParametersOutputTypeDef,
    DescribeServiceActionOutputTypeDef,
    DescribeTagOptionOutputTypeDef,
    ExecuteProvisionedProductPlanOutputTypeDef,
    ExecuteProvisionedProductServiceActionOutputTypeDef,
    GetAWSOrganizationsAccessStatusOutputTypeDef,
    GetProvisionedProductOutputsOutputTypeDef,
    ImportAsProvisionedProductOutputTypeDef,
    ListAcceptedPortfolioSharesOutputTypeDef,
    ListBudgetsForResourceOutputTypeDef,
    ListConstraintsForPortfolioOutputTypeDef,
    ListLaunchPathsOutputTypeDef,
    ListOrganizationPortfolioAccessOutputTypeDef,
    ListPortfolioAccessOutputTypeDef,
    ListPortfoliosForProductOutputTypeDef,
    ListPortfoliosOutputTypeDef,
    ListPrincipalsForPortfolioOutputTypeDef,
    ListProvisionedProductPlansOutputTypeDef,
    ListProvisioningArtifactsForServiceActionOutputTypeDef,
    ListProvisioningArtifactsOutputTypeDef,
    ListRecordHistoryOutputTypeDef,
    ListRecordHistorySearchFilterTypeDef,
    ListResourcesForTagOptionOutputTypeDef,
    ListServiceActionsForProvisioningArtifactOutputTypeDef,
    ListServiceActionsOutputTypeDef,
    ListStackInstancesForProvisionedProductOutputTypeDef,
    ListTagOptionsFiltersTypeDef,
    ListTagOptionsOutputTypeDef,
    OrganizationNodeTypeDef,
    ProvisioningArtifactPropertiesTypeDef,
    ProvisioningParameterTypeDef,
    ProvisioningPreferencesTypeDef,
    ProvisionProductOutputTypeDef,
    ScanProvisionedProductsOutputTypeDef,
    SearchProductsAsAdminOutputTypeDef,
    SearchProductsOutputTypeDef,
    SearchProvisionedProductsOutputTypeDef,
    ServiceActionAssociationTypeDef,
    TagTypeDef,
    TerminateProvisionedProductOutputTypeDef,
    UpdateConstraintOutputTypeDef,
    UpdatePortfolioOutputTypeDef,
    UpdatePortfolioShareOutputTypeDef,
    UpdateProductOutputTypeDef,
    UpdateProvisionedProductOutputTypeDef,
    UpdateProvisionedProductPropertiesOutputTypeDef,
    UpdateProvisioningArtifactOutputTypeDef,
    UpdateProvisioningParameterTypeDef,
    UpdateProvisioningPreferencesTypeDef,
    UpdateServiceActionOutputTypeDef,
    UpdateTagOptionOutputTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("ServiceCatalogClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    DuplicateResourceException: Type[BotocoreClientError]
    InvalidParametersException: Type[BotocoreClientError]
    InvalidStateException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    OperationNotSupportedException: Type[BotocoreClientError]
    ResourceInUseException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    TagOptionNotMigratedException: Type[BotocoreClientError]


class ServiceCatalogClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def accept_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PortfolioShareType: PortfolioShareType = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.accept_portfolio_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#accept-portfolio-share)
        """

    def associate_budget_with_resource(self, BudgetName: str, ResourceId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_budget_with_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#associate-budget-with-resource)
        """

    def associate_principal_with_portfolio(
        self,
        PortfolioId: str,
        PrincipalARN: str,
        PrincipalType: Literal["IAM"],
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_principal_with_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#associate-principal-with-portfolio)
        """

    def associate_product_with_portfolio(
        self,
        ProductId: str,
        PortfolioId: str,
        AcceptLanguage: str = None,
        SourcePortfolioId: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_product_with_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#associate-product-with-portfolio)
        """

    def associate_service_action_with_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        ServiceActionId: str,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_service_action_with_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#associate-service-action-with-provisioning-artifact)
        """

    def associate_tag_option_with_resource(
        self, ResourceId: str, TagOptionId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.associate_tag_option_with_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#associate-tag-option-with-resource)
        """

    def batch_associate_service_action_with_provisioning_artifact(
        self,
        ServiceActionAssociations: List[ServiceActionAssociationTypeDef],
        AcceptLanguage: str = None,
    ) -> BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.batch_associate_service_action_with_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#batch-associate-service-action-with-provisioning-artifact)
        """

    def batch_disassociate_service_action_from_provisioning_artifact(
        self,
        ServiceActionAssociations: List[ServiceActionAssociationTypeDef],
        AcceptLanguage: str = None,
    ) -> BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.batch_disassociate_service_action_from_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#batch-disassociate-service-action-from-provisioning-artifact)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#can-paginate)
        """

    def copy_product(
        self,
        SourceProductArn: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        TargetProductId: str = None,
        TargetProductName: str = None,
        SourceProvisioningArtifactIdentifiers: List[Dict[Literal["Id"], str]] = None,
        CopyOptions: List[Literal["CopyTags"]] = None,
    ) -> CopyProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.copy_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#copy-product)
        """

    def create_constraint(
        self,
        PortfolioId: str,
        ProductId: str,
        Parameters: str,
        Type: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        Description: str = None,
    ) -> CreateConstraintOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.create_constraint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create-constraint)
        """

    def create_portfolio(
        self,
        DisplayName: str,
        ProviderName: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        Description: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreatePortfolioOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.create_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create-portfolio)
        """

    def create_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        AccountId: str = None,
        OrganizationNode: "OrganizationNodeTypeDef" = None,
        ShareTagOptions: bool = None,
    ) -> CreatePortfolioShareOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.create_portfolio_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create-portfolio-share)
        """

    def create_product(
        self,
        Name: str,
        Owner: str,
        ProductType: ProductType,
        ProvisioningArtifactParameters: ProvisioningArtifactPropertiesTypeDef,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        Description: str = None,
        Distributor: str = None,
        SupportDescription: str = None,
        SupportEmail: str = None,
        SupportUrl: str = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.create_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create-product)
        """

    def create_provisioned_product_plan(
        self,
        PlanName: str,
        PlanType: Literal["CLOUDFORMATION"],
        ProductId: str,
        ProvisionedProductName: str,
        ProvisioningArtifactId: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
        NotificationArns: List[str] = None,
        PathId: str = None,
        ProvisioningParameters: List["UpdateProvisioningParameterTypeDef"] = None,
        Tags: List["TagTypeDef"] = None,
    ) -> CreateProvisionedProductPlanOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.create_provisioned_product_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create-provisioned-product-plan)
        """

    def create_provisioning_artifact(
        self,
        ProductId: str,
        Parameters: ProvisioningArtifactPropertiesTypeDef,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
    ) -> CreateProvisioningArtifactOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.create_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create-provisioning-artifact)
        """

    def create_service_action(
        self,
        Name: str,
        DefinitionType: Literal["SSM_AUTOMATION"],
        Definition: Dict[ServiceActionDefinitionKey, str],
        IdempotencyToken: str,
        Description: str = None,
        AcceptLanguage: str = None,
    ) -> CreateServiceActionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.create_service_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create-service-action)
        """

    def create_tag_option(self, Key: str, Value: str) -> CreateTagOptionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.create_tag_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#create-tag-option)
        """

    def delete_constraint(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_constraint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete-constraint)
        """

    def delete_portfolio(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete-portfolio)
        """

    def delete_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        AccountId: str = None,
        OrganizationNode: "OrganizationNodeTypeDef" = None,
    ) -> DeletePortfolioShareOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_portfolio_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete-portfolio-share)
        """

    def delete_product(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete-product)
        """

    def delete_provisioned_product_plan(
        self, PlanId: str, AcceptLanguage: str = None, IgnoreErrors: bool = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_provisioned_product_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete-provisioned-product-plan)
        """

    def delete_provisioning_artifact(
        self, ProductId: str, ProvisioningArtifactId: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete-provisioning-artifact)
        """

    def delete_service_action(self, Id: str, AcceptLanguage: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_service_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete-service-action)
        """

    def delete_tag_option(self, Id: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.delete_tag_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#delete-tag-option)
        """

    def describe_constraint(
        self, Id: str, AcceptLanguage: str = None
    ) -> DescribeConstraintOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_constraint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-constraint)
        """

    def describe_copy_product_status(
        self, CopyProductToken: str, AcceptLanguage: str = None
    ) -> DescribeCopyProductStatusOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_copy_product_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-copy-product-status)
        """

    def describe_portfolio(
        self, Id: str, AcceptLanguage: str = None
    ) -> DescribePortfolioOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-portfolio)
        """

    def describe_portfolio_share_status(
        self, PortfolioShareToken: str
    ) -> DescribePortfolioShareStatusOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_portfolio_share_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-portfolio-share-status)
        """

    def describe_portfolio_shares(
        self,
        PortfolioId: str,
        Type: DescribePortfolioShareType,
        PageToken: str = None,
        PageSize: int = None,
    ) -> DescribePortfolioSharesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_portfolio_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-portfolio-shares)
        """

    def describe_product(
        self, AcceptLanguage: str = None, Id: str = None, Name: str = None
    ) -> DescribeProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-product)
        """

    def describe_product_as_admin(
        self,
        AcceptLanguage: str = None,
        Id: str = None,
        Name: str = None,
        SourcePortfolioId: str = None,
    ) -> DescribeProductAsAdminOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_product_as_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-product-as-admin)
        """

    def describe_product_view(
        self, Id: str, AcceptLanguage: str = None
    ) -> DescribeProductViewOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_product_view)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-product-view)
        """

    def describe_provisioned_product(
        self, AcceptLanguage: str = None, Id: str = None, Name: str = None
    ) -> DescribeProvisionedProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioned_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-provisioned-product)
        """

    def describe_provisioned_product_plan(
        self, PlanId: str, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None
    ) -> DescribeProvisionedProductPlanOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioned_product_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-provisioned-product-plan)
        """

    def describe_provisioning_artifact(
        self,
        AcceptLanguage: str = None,
        ProvisioningArtifactId: str = None,
        ProductId: str = None,
        ProvisioningArtifactName: str = None,
        ProductName: str = None,
        Verbose: bool = None,
    ) -> DescribeProvisioningArtifactOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-provisioning-artifact)
        """

    def describe_provisioning_parameters(
        self,
        AcceptLanguage: str = None,
        ProductId: str = None,
        ProductName: str = None,
        ProvisioningArtifactId: str = None,
        ProvisioningArtifactName: str = None,
        PathId: str = None,
        PathName: str = None,
    ) -> DescribeProvisioningParametersOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_provisioning_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-provisioning-parameters)
        """

    def describe_record(
        self, Id: str, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None
    ) -> DescribeRecordOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_record)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-record)
        """

    def describe_service_action(
        self, Id: str, AcceptLanguage: str = None
    ) -> DescribeServiceActionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_service_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-service-action)
        """

    def describe_service_action_execution_parameters(
        self, ProvisionedProductId: str, ServiceActionId: str, AcceptLanguage: str = None
    ) -> DescribeServiceActionExecutionParametersOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_service_action_execution_parameters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-service-action-execution-parameters)
        """

    def describe_tag_option(self, Id: str) -> DescribeTagOptionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.describe_tag_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#describe-tag-option)
        """

    def disable_aws_organizations_access(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.disable_aws_organizations_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#disable-aws-organizations-access)
        """

    def disassociate_budget_from_resource(self, BudgetName: str, ResourceId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_budget_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#disassociate-budget-from-resource)
        """

    def disassociate_principal_from_portfolio(
        self, PortfolioId: str, PrincipalARN: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_principal_from_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#disassociate-principal-from-portfolio)
        """

    def disassociate_product_from_portfolio(
        self, ProductId: str, PortfolioId: str, AcceptLanguage: str = None
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_product_from_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#disassociate-product-from-portfolio)
        """

    def disassociate_service_action_from_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        ServiceActionId: str,
        AcceptLanguage: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_service_action_from_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#disassociate-service-action-from-provisioning-artifact)
        """

    def disassociate_tag_option_from_resource(
        self, ResourceId: str, TagOptionId: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.disassociate_tag_option_from_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#disassociate-tag-option-from-resource)
        """

    def enable_aws_organizations_access(self) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.enable_aws_organizations_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#enable-aws-organizations-access)
        """

    def execute_provisioned_product_plan(
        self, PlanId: str, IdempotencyToken: str, AcceptLanguage: str = None
    ) -> ExecuteProvisionedProductPlanOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.execute_provisioned_product_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#execute-provisioned-product-plan)
        """

    def execute_provisioned_product_service_action(
        self,
        ProvisionedProductId: str,
        ServiceActionId: str,
        ExecuteToken: str,
        AcceptLanguage: str = None,
        Parameters: Dict[str, List[str]] = None,
    ) -> ExecuteProvisionedProductServiceActionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.execute_provisioned_product_service_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#execute-provisioned-product-service-action)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#generate-presigned-url)
        """

    def get_aws_organizations_access_status(self) -> GetAWSOrganizationsAccessStatusOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.get_aws_organizations_access_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#get-aws-organizations-access-status)
        """

    def get_provisioned_product_outputs(
        self,
        AcceptLanguage: str = None,
        ProvisionedProductId: str = None,
        ProvisionedProductName: str = None,
        OutputKeys: List[str] = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> GetProvisionedProductOutputsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.get_provisioned_product_outputs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#get-provisioned-product-outputs)
        """

    def import_as_provisioned_product(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        ProvisionedProductName: str,
        PhysicalId: str,
        IdempotencyToken: str,
        AcceptLanguage: str = None,
    ) -> ImportAsProvisionedProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.import_as_provisioned_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#import-as-provisioned-product)
        """

    def list_accepted_portfolio_shares(
        self,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
        PortfolioShareType: PortfolioShareType = None,
    ) -> ListAcceptedPortfolioSharesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_accepted_portfolio_shares)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-accepted-portfolio-shares)
        """

    def list_budgets_for_resource(
        self,
        ResourceId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ListBudgetsForResourceOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_budgets_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-budgets-for-resource)
        """

    def list_constraints_for_portfolio(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        ProductId: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ListConstraintsForPortfolioOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_constraints_for_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-constraints-for-portfolio)
        """

    def list_launch_paths(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ListLaunchPathsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_launch_paths)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-launch-paths)
        """

    def list_organization_portfolio_access(
        self,
        PortfolioId: str,
        OrganizationNodeType: OrganizationNodeType,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
    ) -> ListOrganizationPortfolioAccessOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_organization_portfolio_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-organization-portfolio-access)
        """

    def list_portfolio_access(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        OrganizationParentId: str = None,
        PageToken: str = None,
        PageSize: int = None,
    ) -> ListPortfolioAccessOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_portfolio_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-portfolio-access)
        """

    def list_portfolios(
        self, AcceptLanguage: str = None, PageToken: str = None, PageSize: int = None
    ) -> ListPortfoliosOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_portfolios)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-portfolios)
        """

    def list_portfolios_for_product(
        self,
        ProductId: str,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
    ) -> ListPortfoliosForProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_portfolios_for_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-portfolios-for-product)
        """

    def list_principals_for_portfolio(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ListPrincipalsForPortfolioOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_principals_for_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-principals-for-portfolio)
        """

    def list_provisioned_product_plans(
        self,
        AcceptLanguage: str = None,
        ProvisionProductId: str = None,
        PageSize: int = None,
        PageToken: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
    ) -> ListProvisionedProductPlansOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_provisioned_product_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-provisioned-product-plans)
        """

    def list_provisioning_artifacts(
        self, ProductId: str, AcceptLanguage: str = None
    ) -> ListProvisioningArtifactsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_provisioning_artifacts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-provisioning-artifacts)
        """

    def list_provisioning_artifacts_for_service_action(
        self,
        ServiceActionId: str,
        PageSize: int = None,
        PageToken: str = None,
        AcceptLanguage: str = None,
    ) -> ListProvisioningArtifactsForServiceActionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_provisioning_artifacts_for_service_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-provisioning-artifacts-for-service-action)
        """

    def list_record_history(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
        SearchFilter: ListRecordHistorySearchFilterTypeDef = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ListRecordHistoryOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_record_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-record-history)
        """

    def list_resources_for_tag_option(
        self,
        TagOptionId: str,
        ResourceType: str = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ListResourcesForTagOptionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_resources_for_tag_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-resources-for-tag-option)
        """

    def list_service_actions(
        self, AcceptLanguage: str = None, PageSize: int = None, PageToken: str = None
    ) -> ListServiceActionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_service_actions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-service-actions)
        """

    def list_service_actions_for_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        PageSize: int = None,
        PageToken: str = None,
        AcceptLanguage: str = None,
    ) -> ListServiceActionsForProvisioningArtifactOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_service_actions_for_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-service-actions-for-provisioning-artifact)
        """

    def list_stack_instances_for_provisioned_product(
        self,
        ProvisionedProductId: str,
        AcceptLanguage: str = None,
        PageToken: str = None,
        PageSize: int = None,
    ) -> ListStackInstancesForProvisionedProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_stack_instances_for_provisioned_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-stack-instances-for-provisioned-product)
        """

    def list_tag_options(
        self,
        Filters: ListTagOptionsFiltersTypeDef = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ListTagOptionsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.list_tag_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#list-tag-options)
        """

    def provision_product(
        self,
        ProvisionedProductName: str,
        ProvisionToken: str,
        AcceptLanguage: str = None,
        ProductId: str = None,
        ProductName: str = None,
        ProvisioningArtifactId: str = None,
        ProvisioningArtifactName: str = None,
        PathId: str = None,
        PathName: str = None,
        ProvisioningParameters: List[ProvisioningParameterTypeDef] = None,
        ProvisioningPreferences: ProvisioningPreferencesTypeDef = None,
        Tags: List["TagTypeDef"] = None,
        NotificationArns: List[str] = None,
    ) -> ProvisionProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.provision_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#provision-product)
        """

    def reject_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        PortfolioShareType: PortfolioShareType = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.reject_portfolio_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#reject-portfolio-share)
        """

    def scan_provisioned_products(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> ScanProvisionedProductsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.scan_provisioned_products)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#scan-provisioned-products)
        """

    def search_products(
        self,
        AcceptLanguage: str = None,
        Filters: Dict[ProductViewFilterBy, List[str]] = None,
        PageSize: int = None,
        SortBy: ProductViewSortBy = None,
        SortOrder: SortOrder = None,
        PageToken: str = None,
    ) -> SearchProductsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.search_products)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#search-products)
        """

    def search_products_as_admin(
        self,
        AcceptLanguage: str = None,
        PortfolioId: str = None,
        Filters: Dict[ProductViewFilterBy, List[str]] = None,
        SortBy: ProductViewSortBy = None,
        SortOrder: SortOrder = None,
        PageToken: str = None,
        PageSize: int = None,
        ProductSource: Literal["ACCOUNT"] = None,
    ) -> SearchProductsAsAdminOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.search_products_as_admin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#search-products-as-admin)
        """

    def search_provisioned_products(
        self,
        AcceptLanguage: str = None,
        AccessLevelFilter: AccessLevelFilterTypeDef = None,
        Filters: Dict[Literal["SearchQuery"], List[str]] = None,
        SortBy: str = None,
        SortOrder: SortOrder = None,
        PageSize: int = None,
        PageToken: str = None,
    ) -> SearchProvisionedProductsOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.search_provisioned_products)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#search-provisioned-products)
        """

    def terminate_provisioned_product(
        self,
        TerminateToken: str,
        ProvisionedProductName: str = None,
        ProvisionedProductId: str = None,
        IgnoreErrors: bool = None,
        AcceptLanguage: str = None,
        RetainPhysicalResources: bool = None,
    ) -> TerminateProvisionedProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.terminate_provisioned_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#terminate-provisioned-product)
        """

    def update_constraint(
        self, Id: str, AcceptLanguage: str = None, Description: str = None, Parameters: str = None
    ) -> UpdateConstraintOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.update_constraint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update-constraint)
        """

    def update_portfolio(
        self,
        Id: str,
        AcceptLanguage: str = None,
        DisplayName: str = None,
        Description: str = None,
        ProviderName: str = None,
        AddTags: List["TagTypeDef"] = None,
        RemoveTags: List[str] = None,
    ) -> UpdatePortfolioOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.update_portfolio)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update-portfolio)
        """

    def update_portfolio_share(
        self,
        PortfolioId: str,
        AcceptLanguage: str = None,
        AccountId: str = None,
        OrganizationNode: "OrganizationNodeTypeDef" = None,
        ShareTagOptions: bool = None,
    ) -> UpdatePortfolioShareOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.update_portfolio_share)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update-portfolio-share)
        """

    def update_product(
        self,
        Id: str,
        AcceptLanguage: str = None,
        Name: str = None,
        Owner: str = None,
        Description: str = None,
        Distributor: str = None,
        SupportDescription: str = None,
        SupportEmail: str = None,
        SupportUrl: str = None,
        AddTags: List["TagTypeDef"] = None,
        RemoveTags: List[str] = None,
    ) -> UpdateProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.update_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update-product)
        """

    def update_provisioned_product(
        self,
        UpdateToken: str,
        AcceptLanguage: str = None,
        ProvisionedProductName: str = None,
        ProvisionedProductId: str = None,
        ProductId: str = None,
        ProductName: str = None,
        ProvisioningArtifactId: str = None,
        ProvisioningArtifactName: str = None,
        PathId: str = None,
        PathName: str = None,
        ProvisioningParameters: List["UpdateProvisioningParameterTypeDef"] = None,
        ProvisioningPreferences: UpdateProvisioningPreferencesTypeDef = None,
        Tags: List["TagTypeDef"] = None,
    ) -> UpdateProvisionedProductOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.update_provisioned_product)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update-provisioned-product)
        """

    def update_provisioned_product_properties(
        self,
        ProvisionedProductId: str,
        ProvisionedProductProperties: Dict[PropertyKey, str],
        IdempotencyToken: str,
        AcceptLanguage: str = None,
    ) -> UpdateProvisionedProductPropertiesOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.update_provisioned_product_properties)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update-provisioned-product-properties)
        """

    def update_provisioning_artifact(
        self,
        ProductId: str,
        ProvisioningArtifactId: str,
        AcceptLanguage: str = None,
        Name: str = None,
        Description: str = None,
        Active: bool = None,
        Guidance: ProvisioningArtifactGuidance = None,
    ) -> UpdateProvisioningArtifactOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.update_provisioning_artifact)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update-provisioning-artifact)
        """

    def update_service_action(
        self,
        Id: str,
        Name: str = None,
        Definition: Dict[ServiceActionDefinitionKey, str] = None,
        Description: str = None,
        AcceptLanguage: str = None,
    ) -> UpdateServiceActionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.update_service_action)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update-service-action)
        """

    def update_tag_option(
        self, Id: str, Value: str = None, Active: bool = None
    ) -> UpdateTagOptionOutputTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Client.update_tag_option)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/client.html#update-tag-option)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_accepted_portfolio_shares"]
    ) -> ListAcceptedPortfolioSharesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListAcceptedPortfolioShares)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listacceptedportfoliosharespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_constraints_for_portfolio"]
    ) -> ListConstraintsForPortfolioPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListConstraintsForPortfolio)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listconstraintsforportfoliopaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_launch_paths"]
    ) -> ListLaunchPathsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListLaunchPaths)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listlaunchpathspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_organization_portfolio_access"]
    ) -> ListOrganizationPortfolioAccessPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListOrganizationPortfolioAccess)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listorganizationportfolioaccesspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_portfolios"]) -> ListPortfoliosPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfolios)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listportfoliospaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_portfolios_for_product"]
    ) -> ListPortfoliosForProductPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPortfoliosForProduct)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listportfoliosforproductpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_principals_for_portfolio"]
    ) -> ListPrincipalsForPortfolioPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListPrincipalsForPortfolio)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listprincipalsforportfoliopaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_provisioned_product_plans"]
    ) -> ListProvisionedProductPlansPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisionedProductPlans)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listprovisionedproductplanspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_provisioning_artifacts_for_service_action"]
    ) -> ListProvisioningArtifactsForServiceActionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListProvisioningArtifactsForServiceAction)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listprovisioningartifactsforserviceactionpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_record_history"]
    ) -> ListRecordHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListRecordHistory)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listrecordhistorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resources_for_tag_option"]
    ) -> ListResourcesForTagOptionPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListResourcesForTagOption)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listresourcesfortagoptionpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_actions"]
    ) -> ListServiceActionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listserviceactionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_service_actions_for_provisioning_artifact"]
    ) -> ListServiceActionsForProvisioningArtifactPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListServiceActionsForProvisioningArtifact)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listserviceactionsforprovisioningartifactpaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_tag_options"]) -> ListTagOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ListTagOptions)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#listtagoptionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["scan_provisioned_products"]
    ) -> ScanProvisionedProductsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.ScanProvisionedProducts)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#scanprovisionedproductspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_products_as_admin"]
    ) -> SearchProductsAsAdminPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.67/reference/services/servicecatalog.html#ServiceCatalog.Paginator.SearchProductsAsAdmin)[Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/paginators.html#searchproductsasadminpaginator)
        """
