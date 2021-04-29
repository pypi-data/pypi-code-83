"""
Main interface for savingsplans service type definitions.

Usage::

    ```python
    from mypy_boto3_savingsplans.type_defs import ParentSavingsPlanOfferingTypeDef

    data: ParentSavingsPlanOfferingTypeDef = {...}
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
    "ParentSavingsPlanOfferingTypeDef",
    "SavingsPlanOfferingPropertyTypeDef",
    "SavingsPlanOfferingRatePropertyTypeDef",
    "SavingsPlanOfferingRateTypeDef",
    "SavingsPlanOfferingTypeDef",
    "SavingsPlanRatePropertyTypeDef",
    "SavingsPlanRateTypeDef",
    "SavingsPlanTypeDef",
    "CreateSavingsPlanResponseTypeDef",
    "DescribeSavingsPlanRatesResponseTypeDef",
    "DescribeSavingsPlansOfferingRatesResponseTypeDef",
    "DescribeSavingsPlansOfferingsResponseTypeDef",
    "DescribeSavingsPlansResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "SavingsPlanFilterTypeDef",
    "SavingsPlanOfferingFilterElementTypeDef",
    "SavingsPlanOfferingRateFilterElementTypeDef",
    "SavingsPlanRateFilterTypeDef",
)

ParentSavingsPlanOfferingTypeDef = TypedDict(
    "ParentSavingsPlanOfferingTypeDef",
    {
        "offeringId": str,
        "paymentOption": SavingsPlanPaymentOption,
        "planType": SavingsPlanType,
        "durationSeconds": int,
        "currency": CurrencyCode,
        "planDescription": str,
    },
    total=False,
)

SavingsPlanOfferingPropertyTypeDef = TypedDict(
    "SavingsPlanOfferingPropertyTypeDef",
    {"name": SavingsPlanOfferingPropertyKey, "value": str},
    total=False,
)

SavingsPlanOfferingRatePropertyTypeDef = TypedDict(
    "SavingsPlanOfferingRatePropertyTypeDef", {"name": str, "value": str}, total=False
)

SavingsPlanOfferingRateTypeDef = TypedDict(
    "SavingsPlanOfferingRateTypeDef",
    {
        "savingsPlanOffering": "ParentSavingsPlanOfferingTypeDef",
        "rate": str,
        "unit": SavingsPlanRateUnit,
        "productType": SavingsPlanProductType,
        "serviceCode": SavingsPlanRateServiceCode,
        "usageType": str,
        "operation": str,
        "properties": List["SavingsPlanOfferingRatePropertyTypeDef"],
    },
    total=False,
)

SavingsPlanOfferingTypeDef = TypedDict(
    "SavingsPlanOfferingTypeDef",
    {
        "offeringId": str,
        "productTypes": List[SavingsPlanProductType],
        "planType": SavingsPlanType,
        "description": str,
        "paymentOption": SavingsPlanPaymentOption,
        "durationSeconds": int,
        "currency": CurrencyCode,
        "serviceCode": str,
        "usageType": str,
        "operation": str,
        "properties": List["SavingsPlanOfferingPropertyTypeDef"],
    },
    total=False,
)

SavingsPlanRatePropertyTypeDef = TypedDict(
    "SavingsPlanRatePropertyTypeDef",
    {"name": SavingsPlanRatePropertyKey, "value": str},
    total=False,
)

SavingsPlanRateTypeDef = TypedDict(
    "SavingsPlanRateTypeDef",
    {
        "rate": str,
        "currency": CurrencyCode,
        "unit": SavingsPlanRateUnit,
        "productType": SavingsPlanProductType,
        "serviceCode": SavingsPlanRateServiceCode,
        "usageType": str,
        "operation": str,
        "properties": List["SavingsPlanRatePropertyTypeDef"],
    },
    total=False,
)

SavingsPlanTypeDef = TypedDict(
    "SavingsPlanTypeDef",
    {
        "offeringId": str,
        "savingsPlanId": str,
        "savingsPlanArn": str,
        "description": str,
        "start": str,
        "end": str,
        "state": SavingsPlanState,
        "region": str,
        "ec2InstanceFamily": str,
        "savingsPlanType": SavingsPlanType,
        "paymentOption": SavingsPlanPaymentOption,
        "productTypes": List[SavingsPlanProductType],
        "currency": CurrencyCode,
        "commitment": str,
        "upfrontPaymentAmount": str,
        "recurringPaymentAmount": str,
        "termDurationInSeconds": int,
        "tags": Dict[str, str],
    },
    total=False,
)

CreateSavingsPlanResponseTypeDef = TypedDict(
    "CreateSavingsPlanResponseTypeDef", {"savingsPlanId": str}, total=False
)

DescribeSavingsPlanRatesResponseTypeDef = TypedDict(
    "DescribeSavingsPlanRatesResponseTypeDef",
    {"savingsPlanId": str, "searchResults": List["SavingsPlanRateTypeDef"], "nextToken": str},
    total=False,
)

DescribeSavingsPlansOfferingRatesResponseTypeDef = TypedDict(
    "DescribeSavingsPlansOfferingRatesResponseTypeDef",
    {"searchResults": List["SavingsPlanOfferingRateTypeDef"], "nextToken": str},
    total=False,
)

DescribeSavingsPlansOfferingsResponseTypeDef = TypedDict(
    "DescribeSavingsPlansOfferingsResponseTypeDef",
    {"searchResults": List["SavingsPlanOfferingTypeDef"], "nextToken": str},
    total=False,
)

DescribeSavingsPlansResponseTypeDef = TypedDict(
    "DescribeSavingsPlansResponseTypeDef",
    {"savingsPlans": List["SavingsPlanTypeDef"], "nextToken": str},
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef", {"tags": Dict[str, str]}, total=False
)

SavingsPlanFilterTypeDef = TypedDict(
    "SavingsPlanFilterTypeDef", {"name": SavingsPlansFilterName, "values": List[str]}, total=False
)

SavingsPlanOfferingFilterElementTypeDef = TypedDict(
    "SavingsPlanOfferingFilterElementTypeDef",
    {"name": SavingsPlanOfferingFilterAttribute, "values": List[str]},
    total=False,
)

SavingsPlanOfferingRateFilterElementTypeDef = TypedDict(
    "SavingsPlanOfferingRateFilterElementTypeDef",
    {"name": SavingsPlanRateFilterAttribute, "values": List[str]},
    total=False,
)

SavingsPlanRateFilterTypeDef = TypedDict(
    "SavingsPlanRateFilterTypeDef",
    {"name": SavingsPlanRateFilterName, "values": List[str]},
    total=False,
)
