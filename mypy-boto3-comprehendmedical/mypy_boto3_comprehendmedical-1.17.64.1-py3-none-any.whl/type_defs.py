"""
Type annotations for comprehendmedical service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehendmedical/type_defs.html)

Usage::

    ```python
    from mypy_boto3_comprehendmedical.type_defs import AttributeTypeDef

    data: AttributeTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_comprehendmedical.literals import (
    AttributeName,
    EntitySubType,
    EntityType,
    ICD10CMAttributeType,
    ICD10CMEntityType,
    ICD10CMRelationshipType,
    ICD10CMTraitName,
    JobStatus,
    RelationshipType,
    RxNormAttributeType,
    RxNormEntityType,
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
    "AttributeTypeDef",
    "ComprehendMedicalAsyncJobFilterTypeDef",
    "ComprehendMedicalAsyncJobPropertiesTypeDef",
    "DescribeEntitiesDetectionV2JobResponseTypeDef",
    "DescribeICD10CMInferenceJobResponseTypeDef",
    "DescribePHIDetectionJobResponseTypeDef",
    "DescribeRxNormInferenceJobResponseTypeDef",
    "DetectEntitiesResponseTypeDef",
    "DetectEntitiesV2ResponseTypeDef",
    "DetectPHIResponseTypeDef",
    "EntityTypeDef",
    "ICD10CMAttributeTypeDef",
    "ICD10CMConceptTypeDef",
    "ICD10CMEntityTypeDef",
    "ICD10CMTraitTypeDef",
    "InferICD10CMResponseTypeDef",
    "InferRxNormResponseTypeDef",
    "InputDataConfigTypeDef",
    "ListEntitiesDetectionV2JobsResponseTypeDef",
    "ListICD10CMInferenceJobsResponseTypeDef",
    "ListPHIDetectionJobsResponseTypeDef",
    "ListRxNormInferenceJobsResponseTypeDef",
    "OutputDataConfigTypeDef",
    "RxNormAttributeTypeDef",
    "RxNormConceptTypeDef",
    "RxNormEntityTypeDef",
    "RxNormTraitTypeDef",
    "StartEntitiesDetectionV2JobResponseTypeDef",
    "StartICD10CMInferenceJobResponseTypeDef",
    "StartPHIDetectionJobResponseTypeDef",
    "StartRxNormInferenceJobResponseTypeDef",
    "StopEntitiesDetectionV2JobResponseTypeDef",
    "StopICD10CMInferenceJobResponseTypeDef",
    "StopPHIDetectionJobResponseTypeDef",
    "StopRxNormInferenceJobResponseTypeDef",
    "TraitTypeDef",
    "UnmappedAttributeTypeDef",
)

AttributeTypeDef = TypedDict(
    "AttributeTypeDef",
    {
        "Type": EntitySubType,
        "Score": float,
        "RelationshipScore": float,
        "RelationshipType": RelationshipType,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Category": EntityType,
        "Traits": List["TraitTypeDef"],
    },
    total=False,
)


class ComprehendMedicalAsyncJobFilterTypeDef(TypedDict, total=False):
    JobName: str
    JobStatus: JobStatus
    SubmitTimeBefore: datetime
    SubmitTimeAfter: datetime


class ComprehendMedicalAsyncJobPropertiesTypeDef(TypedDict, total=False):
    JobId: str
    JobName: str
    JobStatus: JobStatus
    Message: str
    SubmitTime: datetime
    EndTime: datetime
    ExpirationTime: datetime
    InputDataConfig: "InputDataConfigTypeDef"
    OutputDataConfig: "OutputDataConfigTypeDef"
    LanguageCode: Literal["en"]
    DataAccessRoleArn: str
    ManifestFilePath: str
    KMSKey: str
    ModelVersion: str


class DescribeEntitiesDetectionV2JobResponseTypeDef(TypedDict, total=False):
    ComprehendMedicalAsyncJobProperties: "ComprehendMedicalAsyncJobPropertiesTypeDef"


class DescribeICD10CMInferenceJobResponseTypeDef(TypedDict, total=False):
    ComprehendMedicalAsyncJobProperties: "ComprehendMedicalAsyncJobPropertiesTypeDef"


class DescribePHIDetectionJobResponseTypeDef(TypedDict, total=False):
    ComprehendMedicalAsyncJobProperties: "ComprehendMedicalAsyncJobPropertiesTypeDef"


class DescribeRxNormInferenceJobResponseTypeDef(TypedDict, total=False):
    ComprehendMedicalAsyncJobProperties: "ComprehendMedicalAsyncJobPropertiesTypeDef"


class _RequiredDetectEntitiesResponseTypeDef(TypedDict):
    Entities: List["EntityTypeDef"]
    ModelVersion: str


class DetectEntitiesResponseTypeDef(_RequiredDetectEntitiesResponseTypeDef, total=False):
    UnmappedAttributes: List["UnmappedAttributeTypeDef"]
    PaginationToken: str


class _RequiredDetectEntitiesV2ResponseTypeDef(TypedDict):
    Entities: List["EntityTypeDef"]
    ModelVersion: str


class DetectEntitiesV2ResponseTypeDef(_RequiredDetectEntitiesV2ResponseTypeDef, total=False):
    UnmappedAttributes: List["UnmappedAttributeTypeDef"]
    PaginationToken: str


class _RequiredDetectPHIResponseTypeDef(TypedDict):
    Entities: List["EntityTypeDef"]
    ModelVersion: str


class DetectPHIResponseTypeDef(_RequiredDetectPHIResponseTypeDef, total=False):
    PaginationToken: str


EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Score": float,
        "Text": str,
        "Category": EntityType,
        "Type": EntitySubType,
        "Traits": List["TraitTypeDef"],
        "Attributes": List["AttributeTypeDef"],
    },
    total=False,
)

ICD10CMAttributeTypeDef = TypedDict(
    "ICD10CMAttributeTypeDef",
    {
        "Type": ICD10CMAttributeType,
        "Score": float,
        "RelationshipScore": float,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List["ICD10CMTraitTypeDef"],
        "Category": ICD10CMEntityType,
        "RelationshipType": ICD10CMRelationshipType,
    },
    total=False,
)


class ICD10CMConceptTypeDef(TypedDict, total=False):
    Description: str
    Code: str
    Score: float


ICD10CMEntityTypeDef = TypedDict(
    "ICD10CMEntityTypeDef",
    {
        "Id": int,
        "Text": str,
        "Category": Literal["MEDICAL_CONDITION"],
        "Type": ICD10CMEntityType,
        "Score": float,
        "BeginOffset": int,
        "EndOffset": int,
        "Attributes": List["ICD10CMAttributeTypeDef"],
        "Traits": List["ICD10CMTraitTypeDef"],
        "ICD10CMConcepts": List["ICD10CMConceptTypeDef"],
    },
    total=False,
)


class ICD10CMTraitTypeDef(TypedDict, total=False):
    Name: ICD10CMTraitName
    Score: float


class _RequiredInferICD10CMResponseTypeDef(TypedDict):
    Entities: List["ICD10CMEntityTypeDef"]


class InferICD10CMResponseTypeDef(_RequiredInferICD10CMResponseTypeDef, total=False):
    PaginationToken: str
    ModelVersion: str


class _RequiredInferRxNormResponseTypeDef(TypedDict):
    Entities: List["RxNormEntityTypeDef"]


class InferRxNormResponseTypeDef(_RequiredInferRxNormResponseTypeDef, total=False):
    PaginationToken: str
    ModelVersion: str


class _RequiredInputDataConfigTypeDef(TypedDict):
    S3Bucket: str


class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, total=False):
    S3Key: str


class ListEntitiesDetectionV2JobsResponseTypeDef(TypedDict, total=False):
    ComprehendMedicalAsyncJobPropertiesList: List["ComprehendMedicalAsyncJobPropertiesTypeDef"]
    NextToken: str


class ListICD10CMInferenceJobsResponseTypeDef(TypedDict, total=False):
    ComprehendMedicalAsyncJobPropertiesList: List["ComprehendMedicalAsyncJobPropertiesTypeDef"]
    NextToken: str


class ListPHIDetectionJobsResponseTypeDef(TypedDict, total=False):
    ComprehendMedicalAsyncJobPropertiesList: List["ComprehendMedicalAsyncJobPropertiesTypeDef"]
    NextToken: str


class ListRxNormInferenceJobsResponseTypeDef(TypedDict, total=False):
    ComprehendMedicalAsyncJobPropertiesList: List["ComprehendMedicalAsyncJobPropertiesTypeDef"]
    NextToken: str


class _RequiredOutputDataConfigTypeDef(TypedDict):
    S3Bucket: str


class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, total=False):
    S3Key: str


RxNormAttributeTypeDef = TypedDict(
    "RxNormAttributeTypeDef",
    {
        "Type": RxNormAttributeType,
        "Score": float,
        "RelationshipScore": float,
        "Id": int,
        "BeginOffset": int,
        "EndOffset": int,
        "Text": str,
        "Traits": List["RxNormTraitTypeDef"],
    },
    total=False,
)


class RxNormConceptTypeDef(TypedDict, total=False):
    Description: str
    Code: str
    Score: float


RxNormEntityTypeDef = TypedDict(
    "RxNormEntityTypeDef",
    {
        "Id": int,
        "Text": str,
        "Category": Literal["MEDICATION"],
        "Type": RxNormEntityType,
        "Score": float,
        "BeginOffset": int,
        "EndOffset": int,
        "Attributes": List["RxNormAttributeTypeDef"],
        "Traits": List["RxNormTraitTypeDef"],
        "RxNormConcepts": List["RxNormConceptTypeDef"],
    },
    total=False,
)


class RxNormTraitTypeDef(TypedDict, total=False):
    Name: Literal["NEGATION"]
    Score: float


class StartEntitiesDetectionV2JobResponseTypeDef(TypedDict, total=False):
    JobId: str


class StartICD10CMInferenceJobResponseTypeDef(TypedDict, total=False):
    JobId: str


class StartPHIDetectionJobResponseTypeDef(TypedDict, total=False):
    JobId: str


class StartRxNormInferenceJobResponseTypeDef(TypedDict, total=False):
    JobId: str


class StopEntitiesDetectionV2JobResponseTypeDef(TypedDict, total=False):
    JobId: str


class StopICD10CMInferenceJobResponseTypeDef(TypedDict, total=False):
    JobId: str


class StopPHIDetectionJobResponseTypeDef(TypedDict, total=False):
    JobId: str


class StopRxNormInferenceJobResponseTypeDef(TypedDict, total=False):
    JobId: str


class TraitTypeDef(TypedDict, total=False):
    Name: AttributeName
    Score: float


UnmappedAttributeTypeDef = TypedDict(
    "UnmappedAttributeTypeDef", {"Type": EntityType, "Attribute": "AttributeTypeDef"}, total=False
)
