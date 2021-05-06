"""
Type annotations for savingsplans service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/type_defs.html)

Usage::

    ```python
    from mypy_boto3_savingsplans.type_defs import CreateSavingsPlanResponseTypeDef

    data: CreateSavingsPlanResponseTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List

from mypy_boto3_savingsplans.literals import (
    CurrencyCode,
    SavingsPlanOfferingFilterAttribute,
    SavingsPlanOfferingPropertyKey,
    SavingsPlanPaymentOption,
    SavingsPlanProductType,
    SavingsPlanRateFilterAttribute,
    SavingsPlanRateFilterName,
    SavingsPlanRatePropertyKey,
    SavingsPlanRateServiceCode,
    SavingsPlanRateUnit,
    SavingsPlansFilterName,
    SavingsPlanState,
    SavingsPlanType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateSavingsPlanResponseTypeDef",
    "DescribeSavingsPlanRatesResponseTypeDef",
    "DescribeSavingsPlansOfferingRatesResponseTypeDef",
    "DescribeSavingsPlansOfferingsResponseTypeDef",
    "DescribeSavingsPlansResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ParentSavingsPlanOfferingTypeDef",
    "SavingsPlanFilterTypeDef",
    "SavingsPlanOfferingFilterElementTypeDef",
    "SavingsPlanOfferingPropertyTypeDef",
    "SavingsPlanOfferingRateFilterElementTypeDef",
    "SavingsPlanOfferingRatePropertyTypeDef",
    "SavingsPlanOfferingRateTypeDef",
    "SavingsPlanOfferingTypeDef",
    "SavingsPlanRateFilterTypeDef",
    "SavingsPlanRatePropertyTypeDef",
    "SavingsPlanRateTypeDef",
    "SavingsPlanTypeDef",
)


class CreateSavingsPlanResponseTypeDef(TypedDict, total=False):
    savingsPlanId: str


class DescribeSavingsPlanRatesResponseTypeDef(TypedDict, total=False):
    savingsPlanId: str
    searchResults: List["SavingsPlanRateTypeDef"]
    nextToken: str


class DescribeSavingsPlansOfferingRatesResponseTypeDef(TypedDict, total=False):
    searchResults: List["SavingsPlanOfferingRateTypeDef"]
    nextToken: str


class DescribeSavingsPlansOfferingsResponseTypeDef(TypedDict, total=False):
    searchResults: List["SavingsPlanOfferingTypeDef"]
    nextToken: str


class DescribeSavingsPlansResponseTypeDef(TypedDict, total=False):
    savingsPlans: List["SavingsPlanTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class ParentSavingsPlanOfferingTypeDef(TypedDict, total=False):
    offeringId: str
    paymentOption: SavingsPlanPaymentOption
    planType: SavingsPlanType
    durationSeconds: int
    currency: CurrencyCode
    planDescription: str


class SavingsPlanFilterTypeDef(TypedDict, total=False):
    name: SavingsPlansFilterName
    values: List[str]


class SavingsPlanOfferingFilterElementTypeDef(TypedDict, total=False):
    name: SavingsPlanOfferingFilterAttribute
    values: List[str]


class SavingsPlanOfferingPropertyTypeDef(TypedDict, total=False):
    name: SavingsPlanOfferingPropertyKey
    value: str


class SavingsPlanOfferingRateFilterElementTypeDef(TypedDict, total=False):
    name: SavingsPlanRateFilterAttribute
    values: List[str]


class SavingsPlanOfferingRatePropertyTypeDef(TypedDict, total=False):
    name: str
    value: str


class SavingsPlanOfferingRateTypeDef(TypedDict, total=False):
    savingsPlanOffering: "ParentSavingsPlanOfferingTypeDef"
    rate: str
    unit: SavingsPlanRateUnit
    productType: SavingsPlanProductType
    serviceCode: SavingsPlanRateServiceCode
    usageType: str
    operation: str
    properties: List["SavingsPlanOfferingRatePropertyTypeDef"]


class SavingsPlanOfferingTypeDef(TypedDict, total=False):
    offeringId: str
    productTypes: List[SavingsPlanProductType]
    planType: SavingsPlanType
    description: str
    paymentOption: SavingsPlanPaymentOption
    durationSeconds: int
    currency: CurrencyCode
    serviceCode: str
    usageType: str
    operation: str
    properties: List["SavingsPlanOfferingPropertyTypeDef"]


class SavingsPlanRateFilterTypeDef(TypedDict, total=False):
    name: SavingsPlanRateFilterName
    values: List[str]


class SavingsPlanRatePropertyTypeDef(TypedDict, total=False):
    name: SavingsPlanRatePropertyKey
    value: str


class SavingsPlanRateTypeDef(TypedDict, total=False):
    rate: str
    currency: CurrencyCode
    unit: SavingsPlanRateUnit
    productType: SavingsPlanProductType
    serviceCode: SavingsPlanRateServiceCode
    usageType: str
    operation: str
    properties: List["SavingsPlanRatePropertyTypeDef"]


class SavingsPlanTypeDef(TypedDict, total=False):
    offeringId: str
    savingsPlanId: str
    savingsPlanArn: str
    description: str
    start: str
    end: str
    state: SavingsPlanState
    region: str
    ec2InstanceFamily: str
    savingsPlanType: SavingsPlanType
    paymentOption: SavingsPlanPaymentOption
    productTypes: List[SavingsPlanProductType]
    currency: CurrencyCode
    commitment: str
    upfrontPaymentAmount: str
    recurringPaymentAmount: str
    termDurationInSeconds: int
    tags: Dict[str, str]
