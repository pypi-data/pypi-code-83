"""
Main interface for marketplace-entitlement service client paginators.

Usage::

    ```python
    import boto3

    from mypy_boto3_marketplace_entitlement import MarketplaceEntitlementServiceClient
    from mypy_boto3_marketplace_entitlement.paginator import (
        GetEntitlementsPaginator,
    )

    client: MarketplaceEntitlementServiceClient = boto3.client("marketplace-entitlement")

    get_entitlements_paginator: GetEntitlementsPaginator = client.get_paginator("get_entitlements")
    ```
"""
from typing import Dict, Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from mypy_boto3_marketplace_entitlement.literals import GetEntitlementFilterName
from mypy_boto3_marketplace_entitlement.type_defs import (
    GetEntitlementsResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = ("GetEntitlementsPaginator",)


class GetEntitlementsPaginator(Boto3Paginator):
    """
    [Paginator.GetEntitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Paginator.GetEntitlements)
    """

    def paginate(
        self,
        ProductCode: str,
        Filter: Dict[GetEntitlementFilterName, List[str]] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[GetEntitlementsResultTypeDef]:
        """
        [GetEntitlements.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.61/reference/services/marketplace-entitlement.html#MarketplaceEntitlementService.Paginator.GetEntitlements.paginate)
        """
