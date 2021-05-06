"""
Type annotations for comprehendmedical service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/literals.html)

Usage::

    ```python
    from mypy_boto3_comprehendmedical.literals import AttributeName

    data: AttributeName = "DIAGNOSIS"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "AttributeName",
    "EntitySubType",
    "EntityType",
    "ICD10CMAttributeType",
    "ICD10CMEntityCategory",
    "ICD10CMEntityType",
    "ICD10CMRelationshipType",
    "ICD10CMTraitName",
    "JobStatus",
    "LanguageCode",
    "RelationshipType",
    "RxNormAttributeType",
    "RxNormEntityCategory",
    "RxNormEntityType",
    "RxNormTraitName",
)


AttributeName = Literal["DIAGNOSIS", "NEGATION", "SIGN", "SYMPTOM"]
EntitySubType = Literal[
    "ACUITY",
    "ADDRESS",
    "AGE",
    "BRAND_NAME",
    "CONTACT_POINT",
    "DATE",
    "DIRECTION",
    "DOSAGE",
    "DURATION",
    "EMAIL",
    "FORM",
    "FREQUENCY",
    "GENERIC_NAME",
    "IDENTIFIER",
    "NAME",
    "PROCEDURE_NAME",
    "PROFESSION",
    "QUALITY",
    "QUANTITY",
    "RATE",
    "ROUTE_OR_MODE",
    "STRENGTH",
    "SYSTEM_ORGAN_SITE",
    "TEST_NAME",
    "TEST_UNITS",
    "TEST_VALUE",
    "TIME_EXPRESSION",
    "TIME_TO_DX_NAME",
    "TIME_TO_MEDICATION_NAME",
    "TIME_TO_PROCEDURE_NAME",
    "TIME_TO_TEST_NAME",
    "TIME_TO_TREATMENT_NAME",
    "TREATMENT_NAME",
    "URL",
]
EntityType = Literal[
    "ANATOMY",
    "MEDICAL_CONDITION",
    "MEDICATION",
    "PROTECTED_HEALTH_INFORMATION",
    "TEST_TREATMENT_PROCEDURE",
    "TIME_EXPRESSION",
]
ICD10CMAttributeType = Literal[
    "ACUITY",
    "DIRECTION",
    "QUALITY",
    "QUANTITY",
    "SYSTEM_ORGAN_SITE",
    "TIME_EXPRESSION",
    "TIME_TO_DX_NAME",
]
ICD10CMEntityCategory = Literal["MEDICAL_CONDITION"]
ICD10CMEntityType = Literal["DX_NAME", "TIME_EXPRESSION"]
ICD10CMRelationshipType = Literal["OVERLAP", "SYSTEM_ORGAN_SITE"]
ICD10CMTraitName = Literal["DIAGNOSIS", "NEGATION", "SIGN", "SYMPTOM"]
JobStatus = Literal[
    "COMPLETED",
    "FAILED",
    "IN_PROGRESS",
    "PARTIAL_SUCCESS",
    "STOPPED",
    "STOP_REQUESTED",
    "SUBMITTED",
]
LanguageCode = Literal["en"]
RelationshipType = Literal[
    "ACUITY",
    "ADMINISTERED_VIA",
    "DIRECTION",
    "DOSAGE",
    "DURATION",
    "EVERY",
    "FOR",
    "FORM",
    "FREQUENCY",
    "NEGATIVE",
    "OVERLAP",
    "RATE",
    "ROUTE_OR_MODE",
    "STRENGTH",
    "SYSTEM_ORGAN_SITE",
    "TEST_UNITS",
    "TEST_VALUE",
    "WITH_DOSAGE",
]
RxNormAttributeType = Literal[
    "DOSAGE", "DURATION", "FORM", "FREQUENCY", "RATE", "ROUTE_OR_MODE", "STRENGTH"
]
RxNormEntityCategory = Literal["MEDICATION"]
RxNormEntityType = Literal["BRAND_NAME", "GENERIC_NAME"]
RxNormTraitName = Literal["NEGATION"]
