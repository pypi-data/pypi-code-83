"""
Type annotations for savingsplans service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_savingsplans/literals.html)

Usage::

    ```python
    from mypy_boto3_savingsplans.literals import CurrencyCode

    data: CurrencyCode = "CNY"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CurrencyCode",
    "SavingsPlanOfferingFilterAttribute",
    "SavingsPlanOfferingPropertyKey",
    "SavingsPlanPaymentOption",
    "SavingsPlanProductType",
    "SavingsPlanRateFilterAttribute",
    "SavingsPlanRateFilterName",
    "SavingsPlanRatePropertyKey",
    "SavingsPlanRateServiceCode",
    "SavingsPlanRateUnit",
    "SavingsPlanState",
    "SavingsPlanType",
    "SavingsPlansFilterName",
)


CurrencyCode = Literal["CNY", "USD"]
SavingsPlanOfferingFilterAttribute = Literal["instanceFamily", "region"]
SavingsPlanOfferingPropertyKey = Literal["instanceFamily", "region"]
SavingsPlanPaymentOption = Literal["All Upfront", "No Upfront", "Partial Upfront"]
SavingsPlanProductType = Literal["EC2", "Fargate", "Lambda", "SageMaker"]
SavingsPlanRateFilterAttribute = Literal[
    "instanceFamily", "instanceType", "productDescription", "productId", "region", "tenancy"
]
SavingsPlanRateFilterName = Literal[
    "instanceType",
    "operation",
    "productDescription",
    "productType",
    "region",
    "serviceCode",
    "tenancy",
    "usageType",
]
SavingsPlanRatePropertyKey = Literal[
    "instanceFamily", "instanceType", "productDescription", "region", "tenancy"
]
SavingsPlanRateServiceCode = Literal[
    "AWSLambda", "AmazonEC2", "AmazonECS", "AmazonEKS", "AmazonSageMaker"
]
SavingsPlanRateUnit = Literal["Hrs", "Lambda-GB-Second", "Request"]
SavingsPlanState = Literal[
    "active", "payment-failed", "payment-pending", "queued", "queued-deleted", "retired"
]
SavingsPlanType = Literal["Compute", "EC2Instance", "SageMaker"]
SavingsPlansFilterName = Literal[
    "commitment",
    "ec2-instance-family",
    "end",
    "payment-option",
    "region",
    "savings-plan-type",
    "start",
    "term",
    "upfront",
]
