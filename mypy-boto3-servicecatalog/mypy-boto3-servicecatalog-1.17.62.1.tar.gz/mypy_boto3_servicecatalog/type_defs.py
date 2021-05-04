"""
Type annotations for servicecatalog service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_servicecatalog/type_defs.html)

Usage::

    ```python
    from mypy_boto3_servicecatalog.type_defs import AccessLevelFilterTypeDef

    data: AccessLevelFilterTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from mypy_boto3_servicecatalog.literals import (
    AccessLevelFilterKey,
    AccessStatus,
    ChangeAction,
    CopyProductStatus,
    DescribePortfolioShareType,
    EvaluationType,
    OrganizationNodeType,
    ProductType,
    PropertyKey,
    ProvisionedProductPlanStatus,
    ProvisionedProductStatus,
    ProvisioningArtifactGuidance,
    ProvisioningArtifactType,
    RecordStatus,
    Replacement,
    RequiresRecreation,
    ResourceAttribute,
    ServiceActionAssociationErrorCode,
    ServiceActionDefinitionKey,
    ShareStatus,
    StackInstanceStatus,
    StackSetOperationType,
    Status,
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
    "AccessLevelFilterTypeDef",
    "BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef",
    "BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef",
    "BudgetDetailTypeDef",
    "CloudWatchDashboardTypeDef",
    "ConstraintDetailTypeDef",
    "ConstraintSummaryTypeDef",
    "CopyProductOutputTypeDef",
    "CreateConstraintOutputTypeDef",
    "CreatePortfolioOutputTypeDef",
    "CreatePortfolioShareOutputTypeDef",
    "CreateProductOutputTypeDef",
    "CreateProvisionedProductPlanOutputTypeDef",
    "CreateProvisioningArtifactOutputTypeDef",
    "CreateServiceActionOutputTypeDef",
    "CreateTagOptionOutputTypeDef",
    "DeletePortfolioShareOutputTypeDef",
    "DescribeConstraintOutputTypeDef",
    "DescribeCopyProductStatusOutputTypeDef",
    "DescribePortfolioOutputTypeDef",
    "DescribePortfolioShareStatusOutputTypeDef",
    "DescribePortfolioSharesOutputTypeDef",
    "DescribeProductAsAdminOutputTypeDef",
    "DescribeProductOutputTypeDef",
    "DescribeProductViewOutputTypeDef",
    "DescribeProvisionedProductOutputTypeDef",
    "DescribeProvisionedProductPlanOutputTypeDef",
    "DescribeProvisioningArtifactOutputTypeDef",
    "DescribeProvisioningParametersOutputTypeDef",
    "DescribeRecordOutputTypeDef",
    "DescribeServiceActionExecutionParametersOutputTypeDef",
    "DescribeServiceActionOutputTypeDef",
    "DescribeTagOptionOutputTypeDef",
    "ExecuteProvisionedProductPlanOutputTypeDef",
    "ExecuteProvisionedProductServiceActionOutputTypeDef",
    "ExecutionParameterTypeDef",
    "FailedServiceActionAssociationTypeDef",
    "GetAWSOrganizationsAccessStatusOutputTypeDef",
    "GetProvisionedProductOutputsOutputTypeDef",
    "ImportAsProvisionedProductOutputTypeDef",
    "LaunchPathSummaryTypeDef",
    "LaunchPathTypeDef",
    "ListAcceptedPortfolioSharesOutputTypeDef",
    "ListBudgetsForResourceOutputTypeDef",
    "ListConstraintsForPortfolioOutputTypeDef",
    "ListLaunchPathsOutputTypeDef",
    "ListOrganizationPortfolioAccessOutputTypeDef",
    "ListPortfolioAccessOutputTypeDef",
    "ListPortfoliosForProductOutputTypeDef",
    "ListPortfoliosOutputTypeDef",
    "ListPrincipalsForPortfolioOutputTypeDef",
    "ListProvisionedProductPlansOutputTypeDef",
    "ListProvisioningArtifactsForServiceActionOutputTypeDef",
    "ListProvisioningArtifactsOutputTypeDef",
    "ListRecordHistoryOutputTypeDef",
    "ListRecordHistorySearchFilterTypeDef",
    "ListResourcesForTagOptionOutputTypeDef",
    "ListServiceActionsForProvisioningArtifactOutputTypeDef",
    "ListServiceActionsOutputTypeDef",
    "ListStackInstancesForProvisionedProductOutputTypeDef",
    "ListTagOptionsFiltersTypeDef",
    "ListTagOptionsOutputTypeDef",
    "OrganizationNodeTypeDef",
    "PaginatorConfigTypeDef",
    "ParameterConstraintsTypeDef",
    "PortfolioDetailTypeDef",
    "PortfolioShareDetailTypeDef",
    "PrincipalTypeDef",
    "ProductViewAggregationValueTypeDef",
    "ProductViewDetailTypeDef",
    "ProductViewSummaryTypeDef",
    "ProvisionProductOutputTypeDef",
    "ProvisionedProductAttributeTypeDef",
    "ProvisionedProductDetailTypeDef",
    "ProvisionedProductPlanDetailsTypeDef",
    "ProvisionedProductPlanSummaryTypeDef",
    "ProvisioningArtifactDetailTypeDef",
    "ProvisioningArtifactOutputTypeDef",
    "ProvisioningArtifactParameterTypeDef",
    "ProvisioningArtifactPreferencesTypeDef",
    "ProvisioningArtifactPropertiesTypeDef",
    "ProvisioningArtifactSummaryTypeDef",
    "ProvisioningArtifactTypeDef",
    "ProvisioningArtifactViewTypeDef",
    "ProvisioningParameterTypeDef",
    "ProvisioningPreferencesTypeDef",
    "RecordDetailTypeDef",
    "RecordErrorTypeDef",
    "RecordOutputTypeDef",
    "RecordTagTypeDef",
    "ResourceChangeDetailTypeDef",
    "ResourceChangeTypeDef",
    "ResourceDetailTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "ResponseMetadata",
    "ScanProvisionedProductsOutputTypeDef",
    "SearchProductsAsAdminOutputTypeDef",
    "SearchProductsOutputTypeDef",
    "SearchProvisionedProductsOutputTypeDef",
    "ServiceActionAssociationTypeDef",
    "ServiceActionDetailTypeDef",
    "ServiceActionSummaryTypeDef",
    "ShareDetailsTypeDef",
    "ShareErrorTypeDef",
    "StackInstanceTypeDef",
    "TagOptionDetailTypeDef",
    "TagOptionSummaryTypeDef",
    "TagTypeDef",
    "TerminateProvisionedProductOutputTypeDef",
    "UpdateConstraintOutputTypeDef",
    "UpdatePortfolioOutputTypeDef",
    "UpdatePortfolioShareOutputTypeDef",
    "UpdateProductOutputTypeDef",
    "UpdateProvisionedProductOutputTypeDef",
    "UpdateProvisionedProductPropertiesOutputTypeDef",
    "UpdateProvisioningArtifactOutputTypeDef",
    "UpdateProvisioningParameterTypeDef",
    "UpdateProvisioningPreferencesTypeDef",
    "UpdateServiceActionOutputTypeDef",
    "UpdateTagOptionOutputTypeDef",
    "UsageInstructionTypeDef",
)


class AccessLevelFilterTypeDef(TypedDict, total=False):
    Key: AccessLevelFilterKey
    Value: str


class BatchAssociateServiceActionWithProvisioningArtifactOutputTypeDef(TypedDict):
    FailedServiceActionAssociations: List["FailedServiceActionAssociationTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class BatchDisassociateServiceActionFromProvisioningArtifactOutputTypeDef(TypedDict):
    FailedServiceActionAssociations: List["FailedServiceActionAssociationTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class BudgetDetailTypeDef(TypedDict, total=False):
    BudgetName: str


class CloudWatchDashboardTypeDef(TypedDict, total=False):
    Name: str


ConstraintDetailTypeDef = TypedDict(
    "ConstraintDetailTypeDef",
    {
        "ConstraintId": str,
        "Type": str,
        "Description": str,
        "Owner": str,
        "ProductId": str,
        "PortfolioId": str,
    },
    total=False,
)

ConstraintSummaryTypeDef = TypedDict(
    "ConstraintSummaryTypeDef", {"Type": str, "Description": str}, total=False
)


class CopyProductOutputTypeDef(TypedDict):
    CopyProductToken: str
    ResponseMetadata: "ResponseMetadata"


class CreateConstraintOutputTypeDef(TypedDict):
    ConstraintDetail: "ConstraintDetailTypeDef"
    ConstraintParameters: str
    Status: Status
    ResponseMetadata: "ResponseMetadata"


class CreatePortfolioOutputTypeDef(TypedDict):
    PortfolioDetail: "PortfolioDetailTypeDef"
    Tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class CreatePortfolioShareOutputTypeDef(TypedDict):
    PortfolioShareToken: str
    ResponseMetadata: "ResponseMetadata"


class CreateProductOutputTypeDef(TypedDict):
    ProductViewDetail: "ProductViewDetailTypeDef"
    ProvisioningArtifactDetail: "ProvisioningArtifactDetailTypeDef"
    Tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class CreateProvisionedProductPlanOutputTypeDef(TypedDict):
    PlanName: str
    PlanId: str
    ProvisionProductId: str
    ProvisionedProductName: str
    ProvisioningArtifactId: str
    ResponseMetadata: "ResponseMetadata"


class CreateProvisioningArtifactOutputTypeDef(TypedDict):
    ProvisioningArtifactDetail: "ProvisioningArtifactDetailTypeDef"
    Info: Dict[str, str]
    Status: Status
    ResponseMetadata: "ResponseMetadata"


class CreateServiceActionOutputTypeDef(TypedDict):
    ServiceActionDetail: "ServiceActionDetailTypeDef"
    ResponseMetadata: "ResponseMetadata"


class CreateTagOptionOutputTypeDef(TypedDict):
    TagOptionDetail: "TagOptionDetailTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DeletePortfolioShareOutputTypeDef(TypedDict):
    PortfolioShareToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeConstraintOutputTypeDef(TypedDict):
    ConstraintDetail: "ConstraintDetailTypeDef"
    ConstraintParameters: str
    Status: Status
    ResponseMetadata: "ResponseMetadata"


class DescribeCopyProductStatusOutputTypeDef(TypedDict):
    CopyProductStatus: CopyProductStatus
    TargetProductId: str
    StatusDetail: str
    ResponseMetadata: "ResponseMetadata"


class DescribePortfolioOutputTypeDef(TypedDict):
    PortfolioDetail: "PortfolioDetailTypeDef"
    Tags: List["TagTypeDef"]
    TagOptions: List["TagOptionDetailTypeDef"]
    Budgets: List["BudgetDetailTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribePortfolioShareStatusOutputTypeDef(TypedDict):
    PortfolioShareToken: str
    PortfolioId: str
    OrganizationNodeValue: str
    Status: ShareStatus
    ShareDetails: "ShareDetailsTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribePortfolioSharesOutputTypeDef(TypedDict):
    NextPageToken: str
    PortfolioShareDetails: List["PortfolioShareDetailTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeProductAsAdminOutputTypeDef(TypedDict):
    ProductViewDetail: "ProductViewDetailTypeDef"
    ProvisioningArtifactSummaries: List["ProvisioningArtifactSummaryTypeDef"]
    Tags: List["TagTypeDef"]
    TagOptions: List["TagOptionDetailTypeDef"]
    Budgets: List["BudgetDetailTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeProductOutputTypeDef(TypedDict):
    ProductViewSummary: "ProductViewSummaryTypeDef"
    ProvisioningArtifacts: List["ProvisioningArtifactTypeDef"]
    Budgets: List["BudgetDetailTypeDef"]
    LaunchPaths: List["LaunchPathTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeProductViewOutputTypeDef(TypedDict):
    ProductViewSummary: "ProductViewSummaryTypeDef"
    ProvisioningArtifacts: List["ProvisioningArtifactTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeProvisionedProductOutputTypeDef(TypedDict):
    ProvisionedProductDetail: "ProvisionedProductDetailTypeDef"
    CloudWatchDashboards: List["CloudWatchDashboardTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeProvisionedProductPlanOutputTypeDef(TypedDict):
    ProvisionedProductPlanDetails: "ProvisionedProductPlanDetailsTypeDef"
    ResourceChanges: List["ResourceChangeTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeProvisioningArtifactOutputTypeDef(TypedDict):
    ProvisioningArtifactDetail: "ProvisioningArtifactDetailTypeDef"
    Info: Dict[str, str]
    Status: Status
    ResponseMetadata: "ResponseMetadata"


class DescribeProvisioningParametersOutputTypeDef(TypedDict):
    ProvisioningArtifactParameters: List["ProvisioningArtifactParameterTypeDef"]
    ConstraintSummaries: List["ConstraintSummaryTypeDef"]
    UsageInstructions: List["UsageInstructionTypeDef"]
    TagOptions: List["TagOptionSummaryTypeDef"]
    ProvisioningArtifactPreferences: "ProvisioningArtifactPreferencesTypeDef"
    ProvisioningArtifactOutputs: List["ProvisioningArtifactOutputTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeRecordOutputTypeDef(TypedDict):
    RecordDetail: "RecordDetailTypeDef"
    RecordOutputs: List["RecordOutputTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class DescribeServiceActionExecutionParametersOutputTypeDef(TypedDict):
    ServiceActionParameters: List["ExecutionParameterTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class DescribeServiceActionOutputTypeDef(TypedDict):
    ServiceActionDetail: "ServiceActionDetailTypeDef"
    ResponseMetadata: "ResponseMetadata"


class DescribeTagOptionOutputTypeDef(TypedDict):
    TagOptionDetail: "TagOptionDetailTypeDef"
    ResponseMetadata: "ResponseMetadata"


class ExecuteProvisionedProductPlanOutputTypeDef(TypedDict):
    RecordDetail: "RecordDetailTypeDef"
    ResponseMetadata: "ResponseMetadata"


class ExecuteProvisionedProductServiceActionOutputTypeDef(TypedDict):
    RecordDetail: "RecordDetailTypeDef"
    ResponseMetadata: "ResponseMetadata"


ExecutionParameterTypeDef = TypedDict(
    "ExecutionParameterTypeDef", {"Name": str, "Type": str, "DefaultValues": List[str]}, total=False
)


class FailedServiceActionAssociationTypeDef(TypedDict, total=False):
    ServiceActionId: str
    ProductId: str
    ProvisioningArtifactId: str
    ErrorCode: ServiceActionAssociationErrorCode
    ErrorMessage: str


class GetAWSOrganizationsAccessStatusOutputTypeDef(TypedDict):
    AccessStatus: AccessStatus
    ResponseMetadata: "ResponseMetadata"


class GetProvisionedProductOutputsOutputTypeDef(TypedDict):
    Outputs: List["RecordOutputTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ImportAsProvisionedProductOutputTypeDef(TypedDict):
    RecordDetail: "RecordDetailTypeDef"
    ResponseMetadata: "ResponseMetadata"


class LaunchPathSummaryTypeDef(TypedDict, total=False):
    Id: str
    ConstraintSummaries: List["ConstraintSummaryTypeDef"]
    Tags: List["TagTypeDef"]
    Name: str


class LaunchPathTypeDef(TypedDict, total=False):
    Id: str
    Name: str


class ListAcceptedPortfolioSharesOutputTypeDef(TypedDict):
    PortfolioDetails: List["PortfolioDetailTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListBudgetsForResourceOutputTypeDef(TypedDict):
    Budgets: List["BudgetDetailTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListConstraintsForPortfolioOutputTypeDef(TypedDict):
    ConstraintDetails: List["ConstraintDetailTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListLaunchPathsOutputTypeDef(TypedDict):
    LaunchPathSummaries: List["LaunchPathSummaryTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListOrganizationPortfolioAccessOutputTypeDef(TypedDict):
    OrganizationNodes: List["OrganizationNodeTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListPortfolioAccessOutputTypeDef(TypedDict):
    AccountIds: List[str]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListPortfoliosForProductOutputTypeDef(TypedDict):
    PortfolioDetails: List["PortfolioDetailTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListPortfoliosOutputTypeDef(TypedDict):
    PortfolioDetails: List["PortfolioDetailTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListPrincipalsForPortfolioOutputTypeDef(TypedDict):
    Principals: List["PrincipalTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListProvisionedProductPlansOutputTypeDef(TypedDict):
    ProvisionedProductPlans: List["ProvisionedProductPlanSummaryTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListProvisioningArtifactsForServiceActionOutputTypeDef(TypedDict):
    ProvisioningArtifactViews: List["ProvisioningArtifactViewTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListProvisioningArtifactsOutputTypeDef(TypedDict):
    ProvisioningArtifactDetails: List["ProvisioningArtifactDetailTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListRecordHistoryOutputTypeDef(TypedDict):
    RecordDetails: List["RecordDetailTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListRecordHistorySearchFilterTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class ListResourcesForTagOptionOutputTypeDef(TypedDict):
    ResourceDetails: List["ResourceDetailTypeDef"]
    PageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListServiceActionsForProvisioningArtifactOutputTypeDef(TypedDict):
    ServiceActionSummaries: List["ServiceActionSummaryTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListServiceActionsOutputTypeDef(TypedDict):
    ServiceActionSummaries: List["ServiceActionSummaryTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListStackInstancesForProvisionedProductOutputTypeDef(TypedDict):
    StackInstances: List["StackInstanceTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ListTagOptionsFiltersTypeDef(TypedDict, total=False):
    Key: str
    Value: str
    Active: bool


class ListTagOptionsOutputTypeDef(TypedDict):
    TagOptionDetails: List["TagOptionDetailTypeDef"]
    PageToken: str
    ResponseMetadata: "ResponseMetadata"


OrganizationNodeTypeDef = TypedDict(
    "OrganizationNodeTypeDef", {"Type": OrganizationNodeType, "Value": str}, total=False
)


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class ParameterConstraintsTypeDef(TypedDict, total=False):
    AllowedValues: List[str]
    AllowedPattern: str
    ConstraintDescription: str
    MaxLength: str
    MinLength: str
    MaxValue: str
    MinValue: str


class PortfolioDetailTypeDef(TypedDict, total=False):
    Id: str
    ARN: str
    DisplayName: str
    Description: str
    CreatedTime: datetime
    ProviderName: str


PortfolioShareDetailTypeDef = TypedDict(
    "PortfolioShareDetailTypeDef",
    {
        "PrincipalId": str,
        "Type": DescribePortfolioShareType,
        "Accepted": bool,
        "ShareTagOptions": bool,
    },
    total=False,
)


class PrincipalTypeDef(TypedDict, total=False):
    PrincipalARN: str
    PrincipalType: Literal["IAM"]


class ProductViewAggregationValueTypeDef(TypedDict, total=False):
    Value: str
    ApproximateCount: int


class ProductViewDetailTypeDef(TypedDict, total=False):
    ProductViewSummary: "ProductViewSummaryTypeDef"
    Status: Status
    ProductARN: str
    CreatedTime: datetime


ProductViewSummaryTypeDef = TypedDict(
    "ProductViewSummaryTypeDef",
    {
        "Id": str,
        "ProductId": str,
        "Name": str,
        "Owner": str,
        "ShortDescription": str,
        "Type": ProductType,
        "Distributor": str,
        "HasDefaultPath": bool,
        "SupportEmail": str,
        "SupportDescription": str,
        "SupportUrl": str,
    },
    total=False,
)


class ProvisionProductOutputTypeDef(TypedDict):
    RecordDetail: "RecordDetailTypeDef"
    ResponseMetadata: "ResponseMetadata"


ProvisionedProductAttributeTypeDef = TypedDict(
    "ProvisionedProductAttributeTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": ProvisionedProductStatus,
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "LastProvisioningRecordId": str,
        "LastSuccessfulProvisioningRecordId": str,
        "Tags": List["TagTypeDef"],
        "PhysicalId": str,
        "ProductId": str,
        "ProductName": str,
        "ProvisioningArtifactId": str,
        "ProvisioningArtifactName": str,
        "UserArn": str,
        "UserArnSession": str,
    },
    total=False,
)

ProvisionedProductDetailTypeDef = TypedDict(
    "ProvisionedProductDetailTypeDef",
    {
        "Name": str,
        "Arn": str,
        "Type": str,
        "Id": str,
        "Status": ProvisionedProductStatus,
        "StatusMessage": str,
        "CreatedTime": datetime,
        "IdempotencyToken": str,
        "LastRecordId": str,
        "LastProvisioningRecordId": str,
        "LastSuccessfulProvisioningRecordId": str,
        "ProductId": str,
        "ProvisioningArtifactId": str,
        "LaunchRoleArn": str,
    },
    total=False,
)


class ProvisionedProductPlanDetailsTypeDef(TypedDict, total=False):
    CreatedTime: datetime
    PathId: str
    ProductId: str
    PlanName: str
    PlanId: str
    ProvisionProductId: str
    ProvisionProductName: str
    PlanType: Literal["CLOUDFORMATION"]
    ProvisioningArtifactId: str
    Status: ProvisionedProductPlanStatus
    UpdatedTime: datetime
    NotificationArns: List[str]
    ProvisioningParameters: List["UpdateProvisioningParameterTypeDef"]
    Tags: List["TagTypeDef"]
    StatusMessage: str


class ProvisionedProductPlanSummaryTypeDef(TypedDict, total=False):
    PlanName: str
    PlanId: str
    ProvisionProductId: str
    ProvisionProductName: str
    PlanType: Literal["CLOUDFORMATION"]
    ProvisioningArtifactId: str


ProvisioningArtifactDetailTypeDef = TypedDict(
    "ProvisioningArtifactDetailTypeDef",
    {
        "Id": str,
        "Name": str,
        "Description": str,
        "Type": ProvisioningArtifactType,
        "CreatedTime": datetime,
        "Active": bool,
        "Guidance": ProvisioningArtifactGuidance,
    },
    total=False,
)


class ProvisioningArtifactOutputTypeDef(TypedDict):
    Key: str
    Description: str
    ResponseMetadata: "ResponseMetadata"


class ProvisioningArtifactParameterTypeDef(TypedDict, total=False):
    ParameterKey: str
    DefaultValue: str
    ParameterType: str
    IsNoEcho: bool
    Description: str
    ParameterConstraints: "ParameterConstraintsTypeDef"


class ProvisioningArtifactPreferencesTypeDef(TypedDict, total=False):
    StackSetAccounts: List[str]
    StackSetRegions: List[str]


_RequiredProvisioningArtifactPropertiesTypeDef = TypedDict(
    "_RequiredProvisioningArtifactPropertiesTypeDef", {"Info": Dict[str, str]}
)
_OptionalProvisioningArtifactPropertiesTypeDef = TypedDict(
    "_OptionalProvisioningArtifactPropertiesTypeDef",
    {
        "Name": str,
        "Description": str,
        "Type": ProvisioningArtifactType,
        "DisableTemplateValidation": bool,
    },
    total=False,
)


class ProvisioningArtifactPropertiesTypeDef(
    _RequiredProvisioningArtifactPropertiesTypeDef, _OptionalProvisioningArtifactPropertiesTypeDef
):
    pass


class ProvisioningArtifactSummaryTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Description: str
    CreatedTime: datetime
    ProvisioningArtifactMetadata: Dict[str, str]


class ProvisioningArtifactTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Description: str
    CreatedTime: datetime
    Guidance: ProvisioningArtifactGuidance


class ProvisioningArtifactViewTypeDef(TypedDict, total=False):
    ProductViewSummary: "ProductViewSummaryTypeDef"
    ProvisioningArtifact: "ProvisioningArtifactTypeDef"


class ProvisioningParameterTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class ProvisioningPreferencesTypeDef(TypedDict, total=False):
    StackSetAccounts: List[str]
    StackSetRegions: List[str]
    StackSetFailureToleranceCount: int
    StackSetFailureTolerancePercentage: int
    StackSetMaxConcurrencyCount: int
    StackSetMaxConcurrencyPercentage: int


class RecordDetailTypeDef(TypedDict, total=False):
    RecordId: str
    ProvisionedProductName: str
    Status: RecordStatus
    CreatedTime: datetime
    UpdatedTime: datetime
    ProvisionedProductType: str
    RecordType: str
    ProvisionedProductId: str
    ProductId: str
    ProvisioningArtifactId: str
    PathId: str
    RecordErrors: List["RecordErrorTypeDef"]
    RecordTags: List["RecordTagTypeDef"]
    LaunchRoleArn: str


class RecordErrorTypeDef(TypedDict, total=False):
    Code: str
    Description: str


class RecordOutputTypeDef(TypedDict):
    OutputKey: str
    OutputValue: str
    Description: str
    ResponseMetadata: "ResponseMetadata"


class RecordTagTypeDef(TypedDict, total=False):
    Key: str
    Value: str


class ResourceChangeDetailTypeDef(TypedDict, total=False):
    Target: "ResourceTargetDefinitionTypeDef"
    Evaluation: EvaluationType
    CausingEntity: str


class ResourceChangeTypeDef(TypedDict, total=False):
    Action: ChangeAction
    LogicalResourceId: str
    PhysicalResourceId: str
    ResourceType: str
    Replacement: Replacement
    Scope: List[ResourceAttribute]
    Details: List["ResourceChangeDetailTypeDef"]


class ResourceDetailTypeDef(TypedDict, total=False):
    Id: str
    ARN: str
    Name: str
    Description: str
    CreatedTime: datetime


class ResourceTargetDefinitionTypeDef(TypedDict, total=False):
    Attribute: ResourceAttribute
    Name: str
    RequiresRecreation: RequiresRecreation


class ResponseMetadata(TypedDict):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, Any]
    RetryAttempts: int


class ScanProvisionedProductsOutputTypeDef(TypedDict):
    ProvisionedProducts: List["ProvisionedProductDetailTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class SearchProductsAsAdminOutputTypeDef(TypedDict):
    ProductViewDetails: List["ProductViewDetailTypeDef"]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class SearchProductsOutputTypeDef(TypedDict):
    ProductViewSummaries: List["ProductViewSummaryTypeDef"]
    ProductViewAggregations: Dict[str, List["ProductViewAggregationValueTypeDef"]]
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class SearchProvisionedProductsOutputTypeDef(TypedDict):
    ProvisionedProducts: List["ProvisionedProductAttributeTypeDef"]
    TotalResultsCount: int
    NextPageToken: str
    ResponseMetadata: "ResponseMetadata"


class ServiceActionAssociationTypeDef(TypedDict):
    ServiceActionId: str
    ProductId: str
    ProvisioningArtifactId: str


class ServiceActionDetailTypeDef(TypedDict, total=False):
    ServiceActionSummary: "ServiceActionSummaryTypeDef"
    Definition: Dict[ServiceActionDefinitionKey, str]


class ServiceActionSummaryTypeDef(TypedDict, total=False):
    Id: str
    Name: str
    Description: str
    DefinitionType: Literal["SSM_AUTOMATION"]


class ShareDetailsTypeDef(TypedDict, total=False):
    SuccessfulShares: List[str]
    ShareErrors: List["ShareErrorTypeDef"]


class ShareErrorTypeDef(TypedDict, total=False):
    Accounts: List[str]
    Message: str
    Error: str


class StackInstanceTypeDef(TypedDict, total=False):
    Account: str
    Region: str
    StackInstanceStatus: StackInstanceStatus


class TagOptionDetailTypeDef(TypedDict, total=False):
    Key: str
    Value: str
    Active: bool
    Id: str
    Owner: str


class TagOptionSummaryTypeDef(TypedDict, total=False):
    Key: str
    Values: List[str]


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TerminateProvisionedProductOutputTypeDef(TypedDict):
    RecordDetail: "RecordDetailTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateConstraintOutputTypeDef(TypedDict):
    ConstraintDetail: "ConstraintDetailTypeDef"
    ConstraintParameters: str
    Status: Status
    ResponseMetadata: "ResponseMetadata"


class UpdatePortfolioOutputTypeDef(TypedDict):
    PortfolioDetail: "PortfolioDetailTypeDef"
    Tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class UpdatePortfolioShareOutputTypeDef(TypedDict):
    PortfolioShareToken: str
    Status: ShareStatus
    ResponseMetadata: "ResponseMetadata"


class UpdateProductOutputTypeDef(TypedDict):
    ProductViewDetail: "ProductViewDetailTypeDef"
    Tags: List["TagTypeDef"]
    ResponseMetadata: "ResponseMetadata"


class UpdateProvisionedProductOutputTypeDef(TypedDict):
    RecordDetail: "RecordDetailTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateProvisionedProductPropertiesOutputTypeDef(TypedDict):
    ProvisionedProductId: str
    ProvisionedProductProperties: Dict[PropertyKey, str]
    RecordId: str
    Status: RecordStatus
    ResponseMetadata: "ResponseMetadata"


class UpdateProvisioningArtifactOutputTypeDef(TypedDict):
    ProvisioningArtifactDetail: "ProvisioningArtifactDetailTypeDef"
    Info: Dict[str, str]
    Status: Status
    ResponseMetadata: "ResponseMetadata"


class UpdateProvisioningParameterTypeDef(TypedDict, total=False):
    Key: str
    Value: str
    UsePreviousValue: bool


class UpdateProvisioningPreferencesTypeDef(TypedDict, total=False):
    StackSetAccounts: List[str]
    StackSetRegions: List[str]
    StackSetFailureToleranceCount: int
    StackSetFailureTolerancePercentage: int
    StackSetMaxConcurrencyCount: int
    StackSetMaxConcurrencyPercentage: int
    StackSetOperationType: StackSetOperationType


class UpdateServiceActionOutputTypeDef(TypedDict):
    ServiceActionDetail: "ServiceActionDetailTypeDef"
    ResponseMetadata: "ResponseMetadata"


class UpdateTagOptionOutputTypeDef(TypedDict):
    TagOptionDetail: "TagOptionDetailTypeDef"
    ResponseMetadata: "ResponseMetadata"


UsageInstructionTypeDef = TypedDict(
    "UsageInstructionTypeDef", {"Type": str, "Value": str}, total=False
)
