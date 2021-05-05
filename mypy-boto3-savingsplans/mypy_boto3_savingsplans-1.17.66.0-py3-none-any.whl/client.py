"""
Type annotations for savingsplans service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_savingsplans import SavingsPlansClient

    client: SavingsPlansClient = boto3.client("savingsplans")
    ```
"""
from datetime import datetime
from typing import Any, Dict, List, Type

from botocore.client import ClientMeta

from mypy_boto3_savingsplans.literals import (
    CurrencyCode,
    SavingsPlanPaymentOption,
    SavingsPlanProductType,
    SavingsPlanRateServiceCode,
    SavingsPlanState,
    SavingsPlanType,
)
from mypy_boto3_savingsplans.type_defs import (
    CreateSavingsPlanResponseTypeDef,
    DescribeSavingsPlanRatesResponseTypeDef,
    DescribeSavingsPlansOfferingRatesResponseTypeDef,
    DescribeSavingsPlansOfferingsResponseTypeDef,
    DescribeSavingsPlansResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    SavingsPlanFilterTypeDef,
    SavingsPlanOfferingFilterElementTypeDef,
    SavingsPlanOfferingRateFilterElementTypeDef,
    SavingsPlanRateFilterTypeDef,
)

__all__ = ("SavingsPlansClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InternalServerException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class SavingsPlansClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/savingsplans.html#SavingsPlans.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client.html)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/savingsplans.html#SavingsPlans.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client.html#can-paginate)
        """

    def create_savings_plan(
        self,
        savingsPlanOfferingId: str,
        commitment: str,
        upfrontPaymentAmount: str = None,
        purchaseTime: datetime = None,
        clientToken: str = None,
        tags: Dict[str, str] = None,
    ) -> CreateSavingsPlanResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/savingsplans.html#SavingsPlans.Client.create_savings_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client.html#create-savings-plan)
        """

    def delete_queued_savings_plan(self, savingsPlanId: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/savingsplans.html#SavingsPlans.Client.delete_queued_savings_plan)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client.html#delete-queued-savings-plan)
        """

    def describe_savings_plan_rates(
        self,
        savingsPlanId: str,
        filters: List[SavingsPlanRateFilterTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeSavingsPlanRatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plan_rates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client.html#describe-savings-plan-rates)
        """

    def describe_savings_plans(
        self,
        savingsPlanArns: List[str] = None,
        savingsPlanIds: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
        states: List[SavingsPlanState] = None,
        filters: List[SavingsPlanFilterTypeDef] = None,
    ) -> DescribeSavingsPlansResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plans)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client.html#describe-savings-plans)
        """

    def describe_savings_plans_offering_rates(
        self,
        savingsPlanOfferingIds: List[str] = None,
        savingsPlanPaymentOptions: List[SavingsPlanPaymentOption] = None,
        savingsPlanTypes: List[SavingsPlanType] = None,
        products: List[SavingsPlanProductType] = None,
        serviceCodes: List[SavingsPlanRateServiceCode] = None,
        usageTypes: List[str] = None,
        operations: List[str] = None,
        filters: List[SavingsPlanOfferingRateFilterElementTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeSavingsPlansOfferingRatesResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plans_offering_rates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client.html#describe-savings-plans-offering-rates)
        """

    def describe_savings_plans_offerings(
        self,
        offeringIds: List[str] = None,
        paymentOptions: List[SavingsPlanPaymentOption] = None,
        productType: SavingsPlanProductType = None,
        planTypes: List[SavingsPlanType] = None,
        durations: List[int] = None,
        currencies: List[CurrencyCode] = None,
        descriptions: List[str] = None,
        serviceCodes: List[str] = None,
        usageTypes: List[str] = None,
        operations: List[str] = None,
        filters: List[SavingsPlanOfferingFilterElementTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> DescribeSavingsPlansOfferingsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/savingsplans.html#SavingsPlans.Client.describe_savings_plans_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client.html#describe-savings-plans-offerings)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/savingsplans.html#SavingsPlans.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client.html#generate-presigned-url)
        """

    def list_tags_for_resource(self, resourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/savingsplans.html#SavingsPlans.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client.html#list-tags-for-resource)
        """

    def tag_resource(self, resourceArn: str, tags: Dict[str, str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/savingsplans.html#SavingsPlans.Client.tag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client.html#tag-resource)
        """

    def untag_resource(self, resourceArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.66/reference/services/savingsplans.html#SavingsPlans.Client.untag_resource)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/client.html#untag-resource)
        """
