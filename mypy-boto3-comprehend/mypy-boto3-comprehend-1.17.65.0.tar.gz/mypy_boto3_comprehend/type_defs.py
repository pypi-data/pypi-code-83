"""
Type annotations for comprehend service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/type_defs.html)

Usage::

    ```python
    from mypy_boto3_comprehend.type_defs import AugmentedManifestsListItemTypeDef

    data: AugmentedManifestsListItemTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_comprehend.literals import (
    DocumentClassifierDataFormat,
    DocumentClassifierMode,
    EndpointStatus,
    EntityRecognizerDataFormat,
    EntityType,
    InputFormat,
    JobStatus,
    LanguageCode,
    ModelStatus,
    PartOfSpeechTagType,
    PiiEntitiesDetectionMaskMode,
    PiiEntitiesDetectionMode,
    PiiEntityType,
    SentimentType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AugmentedManifestsListItemTypeDef",
    "BatchDetectDominantLanguageItemResultTypeDef",
    "BatchDetectDominantLanguageResponseTypeDef",
    "BatchDetectEntitiesItemResultTypeDef",
    "BatchDetectEntitiesResponseTypeDef",
    "BatchDetectKeyPhrasesItemResultTypeDef",
    "BatchDetectKeyPhrasesResponseTypeDef",
    "BatchDetectSentimentItemResultTypeDef",
    "BatchDetectSentimentResponseTypeDef",
    "BatchDetectSyntaxItemResultTypeDef",
    "BatchDetectSyntaxResponseTypeDef",
    "BatchItemErrorTypeDef",
    "ClassifierEvaluationMetricsTypeDef",
    "ClassifierMetadataTypeDef",
    "ClassifyDocumentResponseTypeDef",
    "ContainsPiiEntitiesResponseTypeDef",
    "CreateDocumentClassifierResponseTypeDef",
    "CreateEndpointResponseTypeDef",
    "CreateEntityRecognizerResponseTypeDef",
    "DescribeDocumentClassificationJobResponseTypeDef",
    "DescribeDocumentClassifierResponseTypeDef",
    "DescribeDominantLanguageDetectionJobResponseTypeDef",
    "DescribeEndpointResponseTypeDef",
    "DescribeEntitiesDetectionJobResponseTypeDef",
    "DescribeEntityRecognizerResponseTypeDef",
    "DescribeEventsDetectionJobResponseTypeDef",
    "DescribeKeyPhrasesDetectionJobResponseTypeDef",
    "DescribePiiEntitiesDetectionJobResponseTypeDef",
    "DescribeSentimentDetectionJobResponseTypeDef",
    "DescribeTopicsDetectionJobResponseTypeDef",
    "DetectDominantLanguageResponseTypeDef",
    "DetectEntitiesResponseTypeDef",
    "DetectKeyPhrasesResponseTypeDef",
    "DetectPiiEntitiesResponseTypeDef",
    "DetectSentimentResponseTypeDef",
    "DetectSyntaxResponseTypeDef",
    "DocumentClassTypeDef",
    "DocumentClassificationJobFilterTypeDef",
    "DocumentClassificationJobPropertiesTypeDef",
    "DocumentClassifierFilterTypeDef",
    "DocumentClassifierInputDataConfigTypeDef",
    "DocumentClassifierOutputDataConfigTypeDef",
    "DocumentClassifierPropertiesTypeDef",
    "DocumentLabelTypeDef",
    "DominantLanguageDetectionJobFilterTypeDef",
    "DominantLanguageDetectionJobPropertiesTypeDef",
    "DominantLanguageTypeDef",
    "EndpointFilterTypeDef",
    "EndpointPropertiesTypeDef",
    "EntitiesDetectionJobFilterTypeDef",
    "EntitiesDetectionJobPropertiesTypeDef",
    "EntityLabelTypeDef",
    "EntityRecognizerAnnotationsTypeDef",
    "EntityRecognizerDocumentsTypeDef",
    "EntityRecognizerEntityListTypeDef",
    "EntityRecognizerEvaluationMetricsTypeDef",
    "EntityRecognizerFilterTypeDef",
    "EntityRecognizerInputDataConfigTypeDef",
    "EntityRecognizerMetadataEntityTypesListItemTypeDef",
    "EntityRecognizerMetadataTypeDef",
    "EntityRecognizerPropertiesTypeDef",
    "EntityTypeDef",
    "EntityTypesEvaluationMetricsTypeDef",
    "EntityTypesListItemTypeDef",
    "EventsDetectionJobFilterTypeDef",
    "EventsDetectionJobPropertiesTypeDef",
    "InputDataConfigTypeDef",
    "KeyPhraseTypeDef",
    "KeyPhrasesDetectionJobFilterTypeDef",
    "KeyPhrasesDetectionJobPropertiesTypeDef",
    "ListDocumentClassificationJobsResponseTypeDef",
    "ListDocumentClassifiersResponseTypeDef",
    "ListDominantLanguageDetectionJobsResponseTypeDef",
    "ListEndpointsResponseTypeDef",
    "ListEntitiesDetectionJobsResponseTypeDef",
    "ListEntityRecognizersResponseTypeDef",
    "ListEventsDetectionJobsResponseTypeDef",
    "ListKeyPhrasesDetectionJobsResponseTypeDef",
    "ListPiiEntitiesDetectionJobsResponseTypeDef",
    "ListSentimentDetectionJobsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListTopicsDetectionJobsResponseTypeDef",
    "OutputDataConfigTypeDef",
    "PaginatorConfigTypeDef",
    "PartOfSpeechTagTypeDef",
    "PiiEntitiesDetectionJobFilterTypeDef",
    "PiiEntitiesDetectionJobPropertiesTypeDef",
    "PiiEntityTypeDef",
    "PiiOutputDataConfigTypeDef",
    "RedactionConfigTypeDef",
    "SentimentDetectionJobFilterTypeDef",
    "SentimentDetectionJobPropertiesTypeDef",
    "SentimentScoreTypeDef",
    "StartDocumentClassificationJobResponseTypeDef",
    "StartDominantLanguageDetectionJobResponseTypeDef",
    "StartEntitiesDetectionJobResponseTypeDef",
    "StartEventsDetectionJobResponseTypeDef",
    "StartKeyPhrasesDetectionJobResponseTypeDef",
    "StartPiiEntitiesDetectionJobResponseTypeDef",
    "StartSentimentDetectionJobResponseTypeDef",
    "StartTopicsDetectionJobResponseTypeDef",
    "StopDominantLanguageDetectionJobResponseTypeDef",
    "StopEntitiesDetectionJobResponseTypeDef",
    "StopEventsDetectionJobResponseTypeDef",
    "StopKeyPhrasesDetectionJobResponseTypeDef",
    "StopPiiEntitiesDetectionJobResponseTypeDef",
    "StopSentimentDetectionJobResponseTypeDef",
    "SyntaxTokenTypeDef",
    "TagTypeDef",
    "TopicsDetectionJobFilterTypeDef",
    "TopicsDetectionJobPropertiesTypeDef",
    "VpcConfigTypeDef",
)


class AugmentedManifestsListItemTypeDef(TypedDict):
    S3Uri: str
    AttributeNames: List[str]


class BatchDetectDominantLanguageItemResultTypeDef(TypedDict, total=False):
    Index: int
    Languages: List["DominantLanguageTypeDef"]


class BatchDetectDominantLanguageResponseTypeDef(TypedDict):
    ResultList: List["BatchDetectDominantLanguageItemResultTypeDef"]
    ErrorList: List["BatchItemErrorTypeDef"]


class BatchDetectEntitiesItemResultTypeDef(TypedDict, total=False):
    Index: int
    Entities: List["EntityTypeDef"]


class BatchDetectEntitiesResponseTypeDef(TypedDict):
    ResultList: List["BatchDetectEntitiesItemResultTypeDef"]
    ErrorList: List["BatchItemErrorTypeDef"]


class BatchDetectKeyPhrasesItemResultTypeDef(TypedDict, total=False):
    Index: int
    KeyPhrases: List["KeyPhraseTypeDef"]


class BatchDetectKeyPhrasesResponseTypeDef(TypedDict):
    ResultList: List["BatchDetectKeyPhrasesItemResultTypeDef"]
    ErrorList: List["BatchItemErrorTypeDef"]


class BatchDetectSentimentItemResultTypeDef(TypedDict, total=False):
    Index: int
    Sentiment: SentimentType
    SentimentScore: "SentimentScoreTypeDef"


class BatchDetectSentimentResponseTypeDef(TypedDict):
    ResultList: List["BatchDetectSentimentItemResultTypeDef"]
    ErrorList: List["BatchItemErrorTypeDef"]


class BatchDetectSyntaxItemResultTypeDef(TypedDict, total=False):
    Index: int
    SyntaxTokens: List["SyntaxTokenTypeDef"]


class BatchDetectSyntaxResponseTypeDef(TypedDict):
    ResultList: List["BatchDetectSyntaxItemResultTypeDef"]
    ErrorList: List["BatchItemErrorTypeDef"]


class BatchItemErrorTypeDef(TypedDict, total=False):
    Index: int
    ErrorCode: str
    ErrorMessage: str


class ClassifierEvaluationMetricsTypeDef(TypedDict, total=False):
    Accuracy: float
    Precision: float
    Recall: float
    F1Score: float
    MicroPrecision: float
    MicroRecall: float
    MicroF1Score: float
    HammingLoss: float


class ClassifierMetadataTypeDef(TypedDict, total=False):
    NumberOfLabels: int
    NumberOfTrainedDocuments: int
    NumberOfTestDocuments: int
    EvaluationMetrics: "ClassifierEvaluationMetricsTypeDef"


class ClassifyDocumentResponseTypeDef(TypedDict, total=False):
    Classes: List["DocumentClassTypeDef"]
    Labels: List["DocumentLabelTypeDef"]


class ContainsPiiEntitiesResponseTypeDef(TypedDict, total=False):
    Labels: List["EntityLabelTypeDef"]


class CreateDocumentClassifierResponseTypeDef(TypedDict, total=False):
    DocumentClassifierArn: str


class CreateEndpointResponseTypeDef(TypedDict, total=False):
    EndpointArn: str


class CreateEntityRecognizerResponseTypeDef(TypedDict, total=False):
    EntityRecognizerArn: str


class DescribeDocumentClassificationJobResponseTypeDef(TypedDict, total=False):
    DocumentClassificationJobProperties: "DocumentClassificationJobPropertiesTypeDef"


class DescribeDocumentClassifierResponseTypeDef(TypedDict, total=False):
    DocumentClassifierProperties: "DocumentClassifierPropertiesTypeDef"


class DescribeDominantLanguageDetectionJobResponseTypeDef(TypedDict, total=False):
    DominantLanguageDetectionJobProperties: "DominantLanguageDetectionJobPropertiesTypeDef"


class DescribeEndpointResponseTypeDef(TypedDict, total=False):
    EndpointProperties: "EndpointPropertiesTypeDef"


class DescribeEntitiesDetectionJobResponseTypeDef(TypedDict, total=False):
    EntitiesDetectionJobProperties: "EntitiesDetectionJobPropertiesTypeDef"


class DescribeEntityRecognizerResponseTypeDef(TypedDict, total=False):
    EntityRecognizerProperties: "EntityRecognizerPropertiesTypeDef"


class DescribeEventsDetectionJobResponseTypeDef(TypedDict, total=False):
    EventsDetectionJobProperties: "EventsDetectionJobPropertiesTypeDef"


class DescribeKeyPhrasesDetectionJobResponseTypeDef(TypedDict, total=False):
    KeyPhrasesDetectionJobProperties: "KeyPhrasesDetectionJobPropertiesTypeDef"


class DescribePiiEntitiesDetectionJobResponseTypeDef(TypedDict, total=False):
    PiiEntitiesDetectionJobProperties: "PiiEntitiesDetectionJobPropertiesTypeDef"


class DescribeSentimentDetectionJobResponseTypeDef(TypedDict, total=False):
    SentimentDetectionJobProperties: "SentimentDetectionJobPropertiesTypeDef"


class DescribeTopicsDetectionJobResponseTypeDef(TypedDict, total=False):
    TopicsDetectionJobProperties: "TopicsDetectionJobPropertiesTypeDef"


class DetectDominantLanguageResponseTypeDef(TypedDict, total=False):
    Languages: List["DominantLanguageTypeDef"]


class DetectEntitiesResponseTypeDef(TypedDict, total=False):
    Entities: List["EntityTypeDef"]


class DetectKeyPhrasesResponseTypeDef(TypedDict, total=False):
    KeyPhrases: List["KeyPhraseTypeDef"]


class DetectPiiEntitiesResponseTypeDef(TypedDict, total=False):
    Entities: List["PiiEntityTypeDef"]


class DetectSentimentResponseTypeDef(TypedDict, total=False):
    Sentiment: SentimentType
    SentimentScore: "SentimentScoreTypeDef"


class DetectSyntaxResponseTypeDef(TypedDict, total=False):
    SyntaxTokens: List["SyntaxTokenTypeDef"]


class DocumentClassTypeDef(TypedDict, total=False):
    Name: str
    Score: float


class DocumentClassificationJobFilterTypeDef(TypedDict, total=False):
    JobName: str
    JobStatus: JobStatus
    SubmitTimeBefore: datetime
    SubmitTimeAfter: datetime


class DocumentClassificationJobPropertiesTypeDef(TypedDict, total=False):
    JobId: str
    JobName: str
    JobStatus: JobStatus
    Message: str
    SubmitTime: datetime
    EndTime: datetime
    DocumentClassifierArn: str
    InputDataConfig: "InputDataConfigTypeDef"
    OutputDataConfig: "OutputDataConfigTypeDef"
    DataAccessRoleArn: str
    VolumeKmsKeyId: str
    VpcConfig: "VpcConfigTypeDef"


class DocumentClassifierFilterTypeDef(TypedDict, total=False):
    Status: ModelStatus
    SubmitTimeBefore: datetime
    SubmitTimeAfter: datetime


class DocumentClassifierInputDataConfigTypeDef(TypedDict, total=False):
    DataFormat: DocumentClassifierDataFormat
    S3Uri: str
    LabelDelimiter: str
    AugmentedManifests: List["AugmentedManifestsListItemTypeDef"]


class DocumentClassifierOutputDataConfigTypeDef(TypedDict, total=False):
    S3Uri: str
    KmsKeyId: str


class DocumentClassifierPropertiesTypeDef(TypedDict, total=False):
    DocumentClassifierArn: str
    LanguageCode: LanguageCode
    Status: ModelStatus
    Message: str
    SubmitTime: datetime
    EndTime: datetime
    TrainingStartTime: datetime
    TrainingEndTime: datetime
    InputDataConfig: "DocumentClassifierInputDataConfigTypeDef"
    OutputDataConfig: "DocumentClassifierOutputDataConfigTypeDef"
    ClassifierMetadata: "ClassifierMetadataTypeDef"
    DataAccessRoleArn: str
    VolumeKmsKeyId: str
    VpcConfig: "VpcConfigTypeDef"
    Mode: DocumentClassifierMode
    ModelKmsKeyId: str


class DocumentLabelTypeDef(TypedDict, total=False):
    Name: str
    Score: float


class DominantLanguageDetectionJobFilterTypeDef(TypedDict, total=False):
    JobName: str
    JobStatus: JobStatus
    SubmitTimeBefore: datetime
    SubmitTimeAfter: datetime


class DominantLanguageDetectionJobPropertiesTypeDef(TypedDict, total=False):
    JobId: str
    JobName: str
    JobStatus: JobStatus
    Message: str
    SubmitTime: datetime
    EndTime: datetime
    InputDataConfig: "InputDataConfigTypeDef"
    OutputDataConfig: "OutputDataConfigTypeDef"
    DataAccessRoleArn: str
    VolumeKmsKeyId: str
    VpcConfig: "VpcConfigTypeDef"


class DominantLanguageTypeDef(TypedDict, total=False):
    LanguageCode: str
    Score: float


class EndpointFilterTypeDef(TypedDict, total=False):
    ModelArn: str
    Status: EndpointStatus
    CreationTimeBefore: datetime
    CreationTimeAfter: datetime


class EndpointPropertiesTypeDef(TypedDict, total=False):
    EndpointArn: str
    Status: EndpointStatus
    Message: str
    ModelArn: str
    DesiredInferenceUnits: int
    CurrentInferenceUnits: int
    CreationTime: datetime
    LastModifiedTime: datetime
    DataAccessRoleArn: str


class EntitiesDetectionJobFilterTypeDef(TypedDict, total=False):
    JobName: str
    JobStatus: JobStatus
    SubmitTimeBefore: datetime
    SubmitTimeAfter: datetime


class EntitiesDetectionJobPropertiesTypeDef(TypedDict, total=False):
    JobId: str
    JobName: str
    JobStatus: JobStatus
    Message: str
    SubmitTime: datetime
    EndTime: datetime
    EntityRecognizerArn: str
    InputDataConfig: "InputDataConfigTypeDef"
    OutputDataConfig: "OutputDataConfigTypeDef"
    LanguageCode: LanguageCode
    DataAccessRoleArn: str
    VolumeKmsKeyId: str
    VpcConfig: "VpcConfigTypeDef"


class EntityLabelTypeDef(TypedDict, total=False):
    Name: PiiEntityType
    Score: float


class EntityRecognizerAnnotationsTypeDef(TypedDict):
    S3Uri: str


class EntityRecognizerDocumentsTypeDef(TypedDict):
    S3Uri: str


class EntityRecognizerEntityListTypeDef(TypedDict):
    S3Uri: str


class EntityRecognizerEvaluationMetricsTypeDef(TypedDict, total=False):
    Precision: float
    Recall: float
    F1Score: float


class EntityRecognizerFilterTypeDef(TypedDict, total=False):
    Status: ModelStatus
    SubmitTimeBefore: datetime
    SubmitTimeAfter: datetime


class _RequiredEntityRecognizerInputDataConfigTypeDef(TypedDict):
    EntityTypes: List["EntityTypesListItemTypeDef"]


class EntityRecognizerInputDataConfigTypeDef(
    _RequiredEntityRecognizerInputDataConfigTypeDef, total=False
):
    DataFormat: EntityRecognizerDataFormat
    Documents: "EntityRecognizerDocumentsTypeDef"
    Annotations: "EntityRecognizerAnnotationsTypeDef"
    EntityList: "EntityRecognizerEntityListTypeDef"
    AugmentedManifests: List["AugmentedManifestsListItemTypeDef"]


EntityRecognizerMetadataEntityTypesListItemTypeDef = TypedDict(
    "EntityRecognizerMetadataEntityTypesListItemTypeDef",
    {
        "Type": str,
        "EvaluationMetrics": "EntityTypesEvaluationMetricsTypeDef",
        "NumberOfTrainMentions": int,
    },
    total=False,
)


class EntityRecognizerMetadataTypeDef(TypedDict, total=False):
    NumberOfTrainedDocuments: int
    NumberOfTestDocuments: int
    EvaluationMetrics: "EntityRecognizerEvaluationMetricsTypeDef"
    EntityTypes: List["EntityRecognizerMetadataEntityTypesListItemTypeDef"]


class EntityRecognizerPropertiesTypeDef(TypedDict, total=False):
    EntityRecognizerArn: str
    LanguageCode: LanguageCode
    Status: ModelStatus
    Message: str
    SubmitTime: datetime
    EndTime: datetime
    TrainingStartTime: datetime
    TrainingEndTime: datetime
    InputDataConfig: "EntityRecognizerInputDataConfigTypeDef"
    RecognizerMetadata: "EntityRecognizerMetadataTypeDef"
    DataAccessRoleArn: str
    VolumeKmsKeyId: str
    VpcConfig: "VpcConfigTypeDef"
    ModelKmsKeyId: str


EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {"Score": float, "Type": EntityType, "Text": str, "BeginOffset": int, "EndOffset": int},
    total=False,
)


class EntityTypesEvaluationMetricsTypeDef(TypedDict, total=False):
    Precision: float
    Recall: float
    F1Score: float


EntityTypesListItemTypeDef = TypedDict("EntityTypesListItemTypeDef", {"Type": str})


class EventsDetectionJobFilterTypeDef(TypedDict, total=False):
    JobName: str
    JobStatus: JobStatus
    SubmitTimeBefore: datetime
    SubmitTimeAfter: datetime


class EventsDetectionJobPropertiesTypeDef(TypedDict, total=False):
    JobId: str
    JobName: str
    JobStatus: JobStatus
    Message: str
    SubmitTime: datetime
    EndTime: datetime
    InputDataConfig: "InputDataConfigTypeDef"
    OutputDataConfig: "OutputDataConfigTypeDef"
    LanguageCode: LanguageCode
    DataAccessRoleArn: str
    TargetEventTypes: List[str]


class _RequiredInputDataConfigTypeDef(TypedDict):
    S3Uri: str


class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, total=False):
    InputFormat: InputFormat


KeyPhraseTypeDef = TypedDict(
    "KeyPhraseTypeDef",
    {"Score": float, "Text": str, "BeginOffset": int, "EndOffset": int},
    total=False,
)


class KeyPhrasesDetectionJobFilterTypeDef(TypedDict, total=False):
    JobName: str
    JobStatus: JobStatus
    SubmitTimeBefore: datetime
    SubmitTimeAfter: datetime


class KeyPhrasesDetectionJobPropertiesTypeDef(TypedDict, total=False):
    JobId: str
    JobName: str
    JobStatus: JobStatus
    Message: str
    SubmitTime: datetime
    EndTime: datetime
    InputDataConfig: "InputDataConfigTypeDef"
    OutputDataConfig: "OutputDataConfigTypeDef"
    LanguageCode: LanguageCode
    DataAccessRoleArn: str
    VolumeKmsKeyId: str
    VpcConfig: "VpcConfigTypeDef"


class ListDocumentClassificationJobsResponseTypeDef(TypedDict, total=False):
    DocumentClassificationJobPropertiesList: List["DocumentClassificationJobPropertiesTypeDef"]
    NextToken: str


class ListDocumentClassifiersResponseTypeDef(TypedDict, total=False):
    DocumentClassifierPropertiesList: List["DocumentClassifierPropertiesTypeDef"]
    NextToken: str


class ListDominantLanguageDetectionJobsResponseTypeDef(TypedDict, total=False):
    DominantLanguageDetectionJobPropertiesList: List[
        "DominantLanguageDetectionJobPropertiesTypeDef"
    ]
    NextToken: str


class ListEndpointsResponseTypeDef(TypedDict, total=False):
    EndpointPropertiesList: List["EndpointPropertiesTypeDef"]
    NextToken: str


class ListEntitiesDetectionJobsResponseTypeDef(TypedDict, total=False):
    EntitiesDetectionJobPropertiesList: List["EntitiesDetectionJobPropertiesTypeDef"]
    NextToken: str


class ListEntityRecognizersResponseTypeDef(TypedDict, total=False):
    EntityRecognizerPropertiesList: List["EntityRecognizerPropertiesTypeDef"]
    NextToken: str


class ListEventsDetectionJobsResponseTypeDef(TypedDict, total=False):
    EventsDetectionJobPropertiesList: List["EventsDetectionJobPropertiesTypeDef"]
    NextToken: str


class ListKeyPhrasesDetectionJobsResponseTypeDef(TypedDict, total=False):
    KeyPhrasesDetectionJobPropertiesList: List["KeyPhrasesDetectionJobPropertiesTypeDef"]
    NextToken: str


class ListPiiEntitiesDetectionJobsResponseTypeDef(TypedDict, total=False):
    PiiEntitiesDetectionJobPropertiesList: List["PiiEntitiesDetectionJobPropertiesTypeDef"]
    NextToken: str


class ListSentimentDetectionJobsResponseTypeDef(TypedDict, total=False):
    SentimentDetectionJobPropertiesList: List["SentimentDetectionJobPropertiesTypeDef"]
    NextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    ResourceArn: str
    Tags: List["TagTypeDef"]


class ListTopicsDetectionJobsResponseTypeDef(TypedDict, total=False):
    TopicsDetectionJobPropertiesList: List["TopicsDetectionJobPropertiesTypeDef"]
    NextToken: str


class _RequiredOutputDataConfigTypeDef(TypedDict):
    S3Uri: str


class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, total=False):
    KmsKeyId: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class PartOfSpeechTagTypeDef(TypedDict, total=False):
    Tag: PartOfSpeechTagType
    Score: float


class PiiEntitiesDetectionJobFilterTypeDef(TypedDict, total=False):
    JobName: str
    JobStatus: JobStatus
    SubmitTimeBefore: datetime
    SubmitTimeAfter: datetime


class PiiEntitiesDetectionJobPropertiesTypeDef(TypedDict, total=False):
    JobId: str
    JobName: str
    JobStatus: JobStatus
    Message: str
    SubmitTime: datetime
    EndTime: datetime
    InputDataConfig: "InputDataConfigTypeDef"
    OutputDataConfig: "PiiOutputDataConfigTypeDef"
    RedactionConfig: "RedactionConfigTypeDef"
    LanguageCode: LanguageCode
    DataAccessRoleArn: str
    Mode: PiiEntitiesDetectionMode


PiiEntityTypeDef = TypedDict(
    "PiiEntityTypeDef",
    {"Score": float, "Type": PiiEntityType, "BeginOffset": int, "EndOffset": int},
    total=False,
)


class _RequiredPiiOutputDataConfigTypeDef(TypedDict):
    S3Uri: str


class PiiOutputDataConfigTypeDef(_RequiredPiiOutputDataConfigTypeDef, total=False):
    KmsKeyId: str


class RedactionConfigTypeDef(TypedDict, total=False):
    PiiEntityTypes: List[PiiEntityType]
    MaskMode: PiiEntitiesDetectionMaskMode
    MaskCharacter: str


class SentimentDetectionJobFilterTypeDef(TypedDict, total=False):
    JobName: str
    JobStatus: JobStatus
    SubmitTimeBefore: datetime
    SubmitTimeAfter: datetime


class SentimentDetectionJobPropertiesTypeDef(TypedDict, total=False):
    JobId: str
    JobName: str
    JobStatus: JobStatus
    Message: str
    SubmitTime: datetime
    EndTime: datetime
    InputDataConfig: "InputDataConfigTypeDef"
    OutputDataConfig: "OutputDataConfigTypeDef"
    LanguageCode: LanguageCode
    DataAccessRoleArn: str
    VolumeKmsKeyId: str
    VpcConfig: "VpcConfigTypeDef"


class SentimentScoreTypeDef(TypedDict, total=False):
    Positive: float
    Negative: float
    Neutral: float
    Mixed: float


class StartDocumentClassificationJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


class StartDominantLanguageDetectionJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


class StartEntitiesDetectionJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


class StartEventsDetectionJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


class StartKeyPhrasesDetectionJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


class StartPiiEntitiesDetectionJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


class StartSentimentDetectionJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


class StartTopicsDetectionJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


class StopDominantLanguageDetectionJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


class StopEntitiesDetectionJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


class StopEventsDetectionJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


class StopKeyPhrasesDetectionJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


class StopPiiEntitiesDetectionJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


class StopSentimentDetectionJobResponseTypeDef(TypedDict, total=False):
    JobId: str
    JobStatus: JobStatus


SyntaxTokenTypeDef = TypedDict(
    "SyntaxTokenTypeDef",
    {
        "TokenId": int,
        "Text": str,
        "BeginOffset": int,
        "EndOffset": int,
        "PartOfSpeech": "PartOfSpeechTagTypeDef",
    },
    total=False,
)


class _RequiredTagTypeDef(TypedDict):
    Key: str


class TagTypeDef(_RequiredTagTypeDef, total=False):
    Value: str


class TopicsDetectionJobFilterTypeDef(TypedDict, total=False):
    JobName: str
    JobStatus: JobStatus
    SubmitTimeBefore: datetime
    SubmitTimeAfter: datetime


class TopicsDetectionJobPropertiesTypeDef(TypedDict, total=False):
    JobId: str
    JobName: str
    JobStatus: JobStatus
    Message: str
    SubmitTime: datetime
    EndTime: datetime
    InputDataConfig: "InputDataConfigTypeDef"
    OutputDataConfig: "OutputDataConfigTypeDef"
    NumberOfTopics: int
    DataAccessRoleArn: str
    VolumeKmsKeyId: str
    VpcConfig: "VpcConfigTypeDef"


class VpcConfigTypeDef(TypedDict):
    SecurityGroupIds: List[str]
    Subnets: List[str]
