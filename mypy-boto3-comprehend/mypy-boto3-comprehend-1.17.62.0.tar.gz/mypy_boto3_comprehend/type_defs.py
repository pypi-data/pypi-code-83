"""
Main interface for comprehend service type definitions.

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
    "BatchDetectEntitiesItemResultTypeDef",
    "BatchDetectKeyPhrasesItemResultTypeDef",
    "BatchDetectSentimentItemResultTypeDef",
    "BatchDetectSyntaxItemResultTypeDef",
    "BatchItemErrorTypeDef",
    "ClassifierEvaluationMetricsTypeDef",
    "ClassifierMetadataTypeDef",
    "DocumentClassTypeDef",
    "DocumentClassificationJobPropertiesTypeDef",
    "DocumentClassifierInputDataConfigTypeDef",
    "DocumentClassifierOutputDataConfigTypeDef",
    "DocumentClassifierPropertiesTypeDef",
    "DocumentLabelTypeDef",
    "DominantLanguageDetectionJobPropertiesTypeDef",
    "DominantLanguageTypeDef",
    "EndpointPropertiesTypeDef",
    "EntitiesDetectionJobPropertiesTypeDef",
    "EntityLabelTypeDef",
    "EntityRecognizerAnnotationsTypeDef",
    "EntityRecognizerDocumentsTypeDef",
    "EntityRecognizerEntityListTypeDef",
    "EntityRecognizerEvaluationMetricsTypeDef",
    "EntityRecognizerInputDataConfigTypeDef",
    "EntityRecognizerMetadataEntityTypesListItemTypeDef",
    "EntityRecognizerMetadataTypeDef",
    "EntityRecognizerPropertiesTypeDef",
    "EntityTypeDef",
    "EntityTypesEvaluationMetricsTypeDef",
    "EntityTypesListItemTypeDef",
    "EventsDetectionJobPropertiesTypeDef",
    "InputDataConfigTypeDef",
    "KeyPhraseTypeDef",
    "KeyPhrasesDetectionJobPropertiesTypeDef",
    "OutputDataConfigTypeDef",
    "PartOfSpeechTagTypeDef",
    "PiiEntitiesDetectionJobPropertiesTypeDef",
    "PiiEntityTypeDef",
    "PiiOutputDataConfigTypeDef",
    "RedactionConfigTypeDef",
    "SentimentDetectionJobPropertiesTypeDef",
    "SentimentScoreTypeDef",
    "SyntaxTokenTypeDef",
    "TagTypeDef",
    "TopicsDetectionJobPropertiesTypeDef",
    "VpcConfigTypeDef",
    "BatchDetectDominantLanguageResponseTypeDef",
    "BatchDetectEntitiesResponseTypeDef",
    "BatchDetectKeyPhrasesResponseTypeDef",
    "BatchDetectSentimentResponseTypeDef",
    "BatchDetectSyntaxResponseTypeDef",
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
    "DocumentClassificationJobFilterTypeDef",
    "DocumentClassifierFilterTypeDef",
    "DominantLanguageDetectionJobFilterTypeDef",
    "EndpointFilterTypeDef",
    "EntitiesDetectionJobFilterTypeDef",
    "EntityRecognizerFilterTypeDef",
    "EventsDetectionJobFilterTypeDef",
    "KeyPhrasesDetectionJobFilterTypeDef",
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
    "PaginatorConfigTypeDef",
    "PiiEntitiesDetectionJobFilterTypeDef",
    "SentimentDetectionJobFilterTypeDef",
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
    "TopicsDetectionJobFilterTypeDef",
)

AugmentedManifestsListItemTypeDef = TypedDict(
    "AugmentedManifestsListItemTypeDef", {"S3Uri": str, "AttributeNames": List[str]}
)

BatchDetectDominantLanguageItemResultTypeDef = TypedDict(
    "BatchDetectDominantLanguageItemResultTypeDef",
    {"Index": int, "Languages": List["DominantLanguageTypeDef"]},
    total=False,
)

BatchDetectEntitiesItemResultTypeDef = TypedDict(
    "BatchDetectEntitiesItemResultTypeDef",
    {"Index": int, "Entities": List["EntityTypeDef"]},
    total=False,
)

BatchDetectKeyPhrasesItemResultTypeDef = TypedDict(
    "BatchDetectKeyPhrasesItemResultTypeDef",
    {"Index": int, "KeyPhrases": List["KeyPhraseTypeDef"]},
    total=False,
)

BatchDetectSentimentItemResultTypeDef = TypedDict(
    "BatchDetectSentimentItemResultTypeDef",
    {"Index": int, "Sentiment": SentimentType, "SentimentScore": "SentimentScoreTypeDef"},
    total=False,
)

BatchDetectSyntaxItemResultTypeDef = TypedDict(
    "BatchDetectSyntaxItemResultTypeDef",
    {"Index": int, "SyntaxTokens": List["SyntaxTokenTypeDef"]},
    total=False,
)

BatchItemErrorTypeDef = TypedDict(
    "BatchItemErrorTypeDef", {"Index": int, "ErrorCode": str, "ErrorMessage": str}, total=False
)

ClassifierEvaluationMetricsTypeDef = TypedDict(
    "ClassifierEvaluationMetricsTypeDef",
    {
        "Accuracy": float,
        "Precision": float,
        "Recall": float,
        "F1Score": float,
        "MicroPrecision": float,
        "MicroRecall": float,
        "MicroF1Score": float,
        "HammingLoss": float,
    },
    total=False,
)

ClassifierMetadataTypeDef = TypedDict(
    "ClassifierMetadataTypeDef",
    {
        "NumberOfLabels": int,
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": "ClassifierEvaluationMetricsTypeDef",
    },
    total=False,
)

DocumentClassTypeDef = TypedDict("DocumentClassTypeDef", {"Name": str, "Score": float}, total=False)

DocumentClassificationJobPropertiesTypeDef = TypedDict(
    "DocumentClassificationJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatus,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "DocumentClassifierArn": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

DocumentClassifierInputDataConfigTypeDef = TypedDict(
    "DocumentClassifierInputDataConfigTypeDef",
    {
        "DataFormat": DocumentClassifierDataFormat,
        "S3Uri": str,
        "LabelDelimiter": str,
        "AugmentedManifests": List["AugmentedManifestsListItemTypeDef"],
    },
    total=False,
)

DocumentClassifierOutputDataConfigTypeDef = TypedDict(
    "DocumentClassifierOutputDataConfigTypeDef", {"S3Uri": str, "KmsKeyId": str}, total=False
)

DocumentClassifierPropertiesTypeDef = TypedDict(
    "DocumentClassifierPropertiesTypeDef",
    {
        "DocumentClassifierArn": str,
        "LanguageCode": LanguageCode,
        "Status": ModelStatus,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": "DocumentClassifierInputDataConfigTypeDef",
        "OutputDataConfig": "DocumentClassifierOutputDataConfigTypeDef",
        "ClassifierMetadata": "ClassifierMetadataTypeDef",
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "Mode": DocumentClassifierMode,
        "ModelKmsKeyId": str,
    },
    total=False,
)

DocumentLabelTypeDef = TypedDict("DocumentLabelTypeDef", {"Name": str, "Score": float}, total=False)

DominantLanguageDetectionJobPropertiesTypeDef = TypedDict(
    "DominantLanguageDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatus,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

DominantLanguageTypeDef = TypedDict(
    "DominantLanguageTypeDef", {"LanguageCode": str, "Score": float}, total=False
)

EndpointPropertiesTypeDef = TypedDict(
    "EndpointPropertiesTypeDef",
    {
        "EndpointArn": str,
        "Status": EndpointStatus,
        "Message": str,
        "ModelArn": str,
        "DesiredInferenceUnits": int,
        "CurrentInferenceUnits": int,
        "CreationTime": datetime,
        "LastModifiedTime": datetime,
        "DataAccessRoleArn": str,
    },
    total=False,
)

EntitiesDetectionJobPropertiesTypeDef = TypedDict(
    "EntitiesDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatus,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "EntityRecognizerArn": str,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "LanguageCode": LanguageCode,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

EntityLabelTypeDef = TypedDict(
    "EntityLabelTypeDef", {"Name": PiiEntityType, "Score": float}, total=False
)

EntityRecognizerAnnotationsTypeDef = TypedDict("EntityRecognizerAnnotationsTypeDef", {"S3Uri": str})

EntityRecognizerDocumentsTypeDef = TypedDict("EntityRecognizerDocumentsTypeDef", {"S3Uri": str})

EntityRecognizerEntityListTypeDef = TypedDict("EntityRecognizerEntityListTypeDef", {"S3Uri": str})

EntityRecognizerEvaluationMetricsTypeDef = TypedDict(
    "EntityRecognizerEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)

_RequiredEntityRecognizerInputDataConfigTypeDef = TypedDict(
    "_RequiredEntityRecognizerInputDataConfigTypeDef",
    {"EntityTypes": List["EntityTypesListItemTypeDef"]},
)
_OptionalEntityRecognizerInputDataConfigTypeDef = TypedDict(
    "_OptionalEntityRecognizerInputDataConfigTypeDef",
    {
        "DataFormat": EntityRecognizerDataFormat,
        "Documents": "EntityRecognizerDocumentsTypeDef",
        "Annotations": "EntityRecognizerAnnotationsTypeDef",
        "EntityList": "EntityRecognizerEntityListTypeDef",
        "AugmentedManifests": List["AugmentedManifestsListItemTypeDef"],
    },
    total=False,
)


class EntityRecognizerInputDataConfigTypeDef(
    _RequiredEntityRecognizerInputDataConfigTypeDef, _OptionalEntityRecognizerInputDataConfigTypeDef
):
    pass


EntityRecognizerMetadataEntityTypesListItemTypeDef = TypedDict(
    "EntityRecognizerMetadataEntityTypesListItemTypeDef",
    {
        "Type": str,
        "EvaluationMetrics": "EntityTypesEvaluationMetricsTypeDef",
        "NumberOfTrainMentions": int,
    },
    total=False,
)

EntityRecognizerMetadataTypeDef = TypedDict(
    "EntityRecognizerMetadataTypeDef",
    {
        "NumberOfTrainedDocuments": int,
        "NumberOfTestDocuments": int,
        "EvaluationMetrics": "EntityRecognizerEvaluationMetricsTypeDef",
        "EntityTypes": List["EntityRecognizerMetadataEntityTypesListItemTypeDef"],
    },
    total=False,
)

EntityRecognizerPropertiesTypeDef = TypedDict(
    "EntityRecognizerPropertiesTypeDef",
    {
        "EntityRecognizerArn": str,
        "LanguageCode": LanguageCode,
        "Status": ModelStatus,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "TrainingStartTime": datetime,
        "TrainingEndTime": datetime,
        "InputDataConfig": "EntityRecognizerInputDataConfigTypeDef",
        "RecognizerMetadata": "EntityRecognizerMetadataTypeDef",
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
        "ModelKmsKeyId": str,
    },
    total=False,
)

EntityTypeDef = TypedDict(
    "EntityTypeDef",
    {"Score": float, "Type": EntityType, "Text": str, "BeginOffset": int, "EndOffset": int},
    total=False,
)

EntityTypesEvaluationMetricsTypeDef = TypedDict(
    "EntityTypesEvaluationMetricsTypeDef",
    {"Precision": float, "Recall": float, "F1Score": float},
    total=False,
)

EntityTypesListItemTypeDef = TypedDict("EntityTypesListItemTypeDef", {"Type": str})

EventsDetectionJobPropertiesTypeDef = TypedDict(
    "EventsDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatus,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "LanguageCode": LanguageCode,
        "DataAccessRoleArn": str,
        "TargetEventTypes": List[str],
    },
    total=False,
)

_RequiredInputDataConfigTypeDef = TypedDict("_RequiredInputDataConfigTypeDef", {"S3Uri": str})
_OptionalInputDataConfigTypeDef = TypedDict(
    "_OptionalInputDataConfigTypeDef", {"InputFormat": InputFormat}, total=False
)


class InputDataConfigTypeDef(_RequiredInputDataConfigTypeDef, _OptionalInputDataConfigTypeDef):
    pass


KeyPhraseTypeDef = TypedDict(
    "KeyPhraseTypeDef",
    {"Score": float, "Text": str, "BeginOffset": int, "EndOffset": int},
    total=False,
)

KeyPhrasesDetectionJobPropertiesTypeDef = TypedDict(
    "KeyPhrasesDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatus,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "LanguageCode": LanguageCode,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

_RequiredOutputDataConfigTypeDef = TypedDict("_RequiredOutputDataConfigTypeDef", {"S3Uri": str})
_OptionalOutputDataConfigTypeDef = TypedDict(
    "_OptionalOutputDataConfigTypeDef", {"KmsKeyId": str}, total=False
)


class OutputDataConfigTypeDef(_RequiredOutputDataConfigTypeDef, _OptionalOutputDataConfigTypeDef):
    pass


PartOfSpeechTagTypeDef = TypedDict(
    "PartOfSpeechTagTypeDef", {"Tag": PartOfSpeechTagType, "Score": float}, total=False
)

PiiEntitiesDetectionJobPropertiesTypeDef = TypedDict(
    "PiiEntitiesDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatus,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "PiiOutputDataConfigTypeDef",
        "RedactionConfig": "RedactionConfigTypeDef",
        "LanguageCode": LanguageCode,
        "DataAccessRoleArn": str,
        "Mode": PiiEntitiesDetectionMode,
    },
    total=False,
)

PiiEntityTypeDef = TypedDict(
    "PiiEntityTypeDef",
    {"Score": float, "Type": PiiEntityType, "BeginOffset": int, "EndOffset": int},
    total=False,
)

_RequiredPiiOutputDataConfigTypeDef = TypedDict(
    "_RequiredPiiOutputDataConfigTypeDef", {"S3Uri": str}
)
_OptionalPiiOutputDataConfigTypeDef = TypedDict(
    "_OptionalPiiOutputDataConfigTypeDef", {"KmsKeyId": str}, total=False
)


class PiiOutputDataConfigTypeDef(
    _RequiredPiiOutputDataConfigTypeDef, _OptionalPiiOutputDataConfigTypeDef
):
    pass


RedactionConfigTypeDef = TypedDict(
    "RedactionConfigTypeDef",
    {
        "PiiEntityTypes": List[PiiEntityType],
        "MaskMode": PiiEntitiesDetectionMaskMode,
        "MaskCharacter": str,
    },
    total=False,
)

SentimentDetectionJobPropertiesTypeDef = TypedDict(
    "SentimentDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatus,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "LanguageCode": LanguageCode,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

SentimentScoreTypeDef = TypedDict(
    "SentimentScoreTypeDef",
    {"Positive": float, "Negative": float, "Neutral": float, "Mixed": float},
    total=False,
)

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

_RequiredTagTypeDef = TypedDict("_RequiredTagTypeDef", {"Key": str})
_OptionalTagTypeDef = TypedDict("_OptionalTagTypeDef", {"Value": str}, total=False)


class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass


TopicsDetectionJobPropertiesTypeDef = TypedDict(
    "TopicsDetectionJobPropertiesTypeDef",
    {
        "JobId": str,
        "JobName": str,
        "JobStatus": JobStatus,
        "Message": str,
        "SubmitTime": datetime,
        "EndTime": datetime,
        "InputDataConfig": "InputDataConfigTypeDef",
        "OutputDataConfig": "OutputDataConfigTypeDef",
        "NumberOfTopics": int,
        "DataAccessRoleArn": str,
        "VolumeKmsKeyId": str,
        "VpcConfig": "VpcConfigTypeDef",
    },
    total=False,
)

VpcConfigTypeDef = TypedDict(
    "VpcConfigTypeDef", {"SecurityGroupIds": List[str], "Subnets": List[str]}
)

BatchDetectDominantLanguageResponseTypeDef = TypedDict(
    "BatchDetectDominantLanguageResponseTypeDef",
    {
        "ResultList": List["BatchDetectDominantLanguageItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
    },
)

BatchDetectEntitiesResponseTypeDef = TypedDict(
    "BatchDetectEntitiesResponseTypeDef",
    {
        "ResultList": List["BatchDetectEntitiesItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
    },
)

BatchDetectKeyPhrasesResponseTypeDef = TypedDict(
    "BatchDetectKeyPhrasesResponseTypeDef",
    {
        "ResultList": List["BatchDetectKeyPhrasesItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
    },
)

BatchDetectSentimentResponseTypeDef = TypedDict(
    "BatchDetectSentimentResponseTypeDef",
    {
        "ResultList": List["BatchDetectSentimentItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
    },
)

BatchDetectSyntaxResponseTypeDef = TypedDict(
    "BatchDetectSyntaxResponseTypeDef",
    {
        "ResultList": List["BatchDetectSyntaxItemResultTypeDef"],
        "ErrorList": List["BatchItemErrorTypeDef"],
    },
)

ClassifyDocumentResponseTypeDef = TypedDict(
    "ClassifyDocumentResponseTypeDef",
    {"Classes": List["DocumentClassTypeDef"], "Labels": List["DocumentLabelTypeDef"]},
    total=False,
)

ContainsPiiEntitiesResponseTypeDef = TypedDict(
    "ContainsPiiEntitiesResponseTypeDef", {"Labels": List["EntityLabelTypeDef"]}, total=False
)

CreateDocumentClassifierResponseTypeDef = TypedDict(
    "CreateDocumentClassifierResponseTypeDef", {"DocumentClassifierArn": str}, total=False
)

CreateEndpointResponseTypeDef = TypedDict(
    "CreateEndpointResponseTypeDef", {"EndpointArn": str}, total=False
)

CreateEntityRecognizerResponseTypeDef = TypedDict(
    "CreateEntityRecognizerResponseTypeDef", {"EntityRecognizerArn": str}, total=False
)

DescribeDocumentClassificationJobResponseTypeDef = TypedDict(
    "DescribeDocumentClassificationJobResponseTypeDef",
    {"DocumentClassificationJobProperties": "DocumentClassificationJobPropertiesTypeDef"},
    total=False,
)

DescribeDocumentClassifierResponseTypeDef = TypedDict(
    "DescribeDocumentClassifierResponseTypeDef",
    {"DocumentClassifierProperties": "DocumentClassifierPropertiesTypeDef"},
    total=False,
)

DescribeDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "DescribeDominantLanguageDetectionJobResponseTypeDef",
    {"DominantLanguageDetectionJobProperties": "DominantLanguageDetectionJobPropertiesTypeDef"},
    total=False,
)

DescribeEndpointResponseTypeDef = TypedDict(
    "DescribeEndpointResponseTypeDef",
    {"EndpointProperties": "EndpointPropertiesTypeDef"},
    total=False,
)

DescribeEntitiesDetectionJobResponseTypeDef = TypedDict(
    "DescribeEntitiesDetectionJobResponseTypeDef",
    {"EntitiesDetectionJobProperties": "EntitiesDetectionJobPropertiesTypeDef"},
    total=False,
)

DescribeEntityRecognizerResponseTypeDef = TypedDict(
    "DescribeEntityRecognizerResponseTypeDef",
    {"EntityRecognizerProperties": "EntityRecognizerPropertiesTypeDef"},
    total=False,
)

DescribeEventsDetectionJobResponseTypeDef = TypedDict(
    "DescribeEventsDetectionJobResponseTypeDef",
    {"EventsDetectionJobProperties": "EventsDetectionJobPropertiesTypeDef"},
    total=False,
)

DescribeKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "DescribeKeyPhrasesDetectionJobResponseTypeDef",
    {"KeyPhrasesDetectionJobProperties": "KeyPhrasesDetectionJobPropertiesTypeDef"},
    total=False,
)

DescribePiiEntitiesDetectionJobResponseTypeDef = TypedDict(
    "DescribePiiEntitiesDetectionJobResponseTypeDef",
    {"PiiEntitiesDetectionJobProperties": "PiiEntitiesDetectionJobPropertiesTypeDef"},
    total=False,
)

DescribeSentimentDetectionJobResponseTypeDef = TypedDict(
    "DescribeSentimentDetectionJobResponseTypeDef",
    {"SentimentDetectionJobProperties": "SentimentDetectionJobPropertiesTypeDef"},
    total=False,
)

DescribeTopicsDetectionJobResponseTypeDef = TypedDict(
    "DescribeTopicsDetectionJobResponseTypeDef",
    {"TopicsDetectionJobProperties": "TopicsDetectionJobPropertiesTypeDef"},
    total=False,
)

DetectDominantLanguageResponseTypeDef = TypedDict(
    "DetectDominantLanguageResponseTypeDef",
    {"Languages": List["DominantLanguageTypeDef"]},
    total=False,
)

DetectEntitiesResponseTypeDef = TypedDict(
    "DetectEntitiesResponseTypeDef", {"Entities": List["EntityTypeDef"]}, total=False
)

DetectKeyPhrasesResponseTypeDef = TypedDict(
    "DetectKeyPhrasesResponseTypeDef", {"KeyPhrases": List["KeyPhraseTypeDef"]}, total=False
)

DetectPiiEntitiesResponseTypeDef = TypedDict(
    "DetectPiiEntitiesResponseTypeDef", {"Entities": List["PiiEntityTypeDef"]}, total=False
)

DetectSentimentResponseTypeDef = TypedDict(
    "DetectSentimentResponseTypeDef",
    {"Sentiment": SentimentType, "SentimentScore": "SentimentScoreTypeDef"},
    total=False,
)

DetectSyntaxResponseTypeDef = TypedDict(
    "DetectSyntaxResponseTypeDef", {"SyntaxTokens": List["SyntaxTokenTypeDef"]}, total=False
)

DocumentClassificationJobFilterTypeDef = TypedDict(
    "DocumentClassificationJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatus,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)

DocumentClassifierFilterTypeDef = TypedDict(
    "DocumentClassifierFilterTypeDef",
    {"Status": ModelStatus, "SubmitTimeBefore": datetime, "SubmitTimeAfter": datetime},
    total=False,
)

DominantLanguageDetectionJobFilterTypeDef = TypedDict(
    "DominantLanguageDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatus,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)

EndpointFilterTypeDef = TypedDict(
    "EndpointFilterTypeDef",
    {
        "ModelArn": str,
        "Status": EndpointStatus,
        "CreationTimeBefore": datetime,
        "CreationTimeAfter": datetime,
    },
    total=False,
)

EntitiesDetectionJobFilterTypeDef = TypedDict(
    "EntitiesDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatus,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)

EntityRecognizerFilterTypeDef = TypedDict(
    "EntityRecognizerFilterTypeDef",
    {"Status": ModelStatus, "SubmitTimeBefore": datetime, "SubmitTimeAfter": datetime},
    total=False,
)

EventsDetectionJobFilterTypeDef = TypedDict(
    "EventsDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatus,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)

KeyPhrasesDetectionJobFilterTypeDef = TypedDict(
    "KeyPhrasesDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatus,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)

ListDocumentClassificationJobsResponseTypeDef = TypedDict(
    "ListDocumentClassificationJobsResponseTypeDef",
    {
        "DocumentClassificationJobPropertiesList": List[
            "DocumentClassificationJobPropertiesTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

ListDocumentClassifiersResponseTypeDef = TypedDict(
    "ListDocumentClassifiersResponseTypeDef",
    {
        "DocumentClassifierPropertiesList": List["DocumentClassifierPropertiesTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListDominantLanguageDetectionJobsResponseTypeDef = TypedDict(
    "ListDominantLanguageDetectionJobsResponseTypeDef",
    {
        "DominantLanguageDetectionJobPropertiesList": List[
            "DominantLanguageDetectionJobPropertiesTypeDef"
        ],
        "NextToken": str,
    },
    total=False,
)

ListEndpointsResponseTypeDef = TypedDict(
    "ListEndpointsResponseTypeDef",
    {"EndpointPropertiesList": List["EndpointPropertiesTypeDef"], "NextToken": str},
    total=False,
)

ListEntitiesDetectionJobsResponseTypeDef = TypedDict(
    "ListEntitiesDetectionJobsResponseTypeDef",
    {
        "EntitiesDetectionJobPropertiesList": List["EntitiesDetectionJobPropertiesTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListEntityRecognizersResponseTypeDef = TypedDict(
    "ListEntityRecognizersResponseTypeDef",
    {"EntityRecognizerPropertiesList": List["EntityRecognizerPropertiesTypeDef"], "NextToken": str},
    total=False,
)

ListEventsDetectionJobsResponseTypeDef = TypedDict(
    "ListEventsDetectionJobsResponseTypeDef",
    {
        "EventsDetectionJobPropertiesList": List["EventsDetectionJobPropertiesTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListKeyPhrasesDetectionJobsResponseTypeDef = TypedDict(
    "ListKeyPhrasesDetectionJobsResponseTypeDef",
    {
        "KeyPhrasesDetectionJobPropertiesList": List["KeyPhrasesDetectionJobPropertiesTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListPiiEntitiesDetectionJobsResponseTypeDef = TypedDict(
    "ListPiiEntitiesDetectionJobsResponseTypeDef",
    {
        "PiiEntitiesDetectionJobPropertiesList": List["PiiEntitiesDetectionJobPropertiesTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListSentimentDetectionJobsResponseTypeDef = TypedDict(
    "ListSentimentDetectionJobsResponseTypeDef",
    {
        "SentimentDetectionJobPropertiesList": List["SentimentDetectionJobPropertiesTypeDef"],
        "NextToken": str,
    },
    total=False,
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {"ResourceArn": str, "Tags": List["TagTypeDef"]},
    total=False,
)

ListTopicsDetectionJobsResponseTypeDef = TypedDict(
    "ListTopicsDetectionJobsResponseTypeDef",
    {
        "TopicsDetectionJobPropertiesList": List["TopicsDetectionJobPropertiesTypeDef"],
        "NextToken": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef", {"MaxItems": int, "PageSize": int, "StartingToken": str}, total=False
)

PiiEntitiesDetectionJobFilterTypeDef = TypedDict(
    "PiiEntitiesDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatus,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)

SentimentDetectionJobFilterTypeDef = TypedDict(
    "SentimentDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatus,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)

StartDocumentClassificationJobResponseTypeDef = TypedDict(
    "StartDocumentClassificationJobResponseTypeDef",
    {"JobId": str, "JobStatus": JobStatus},
    total=False,
)

StartDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "StartDominantLanguageDetectionJobResponseTypeDef",
    {"JobId": str, "JobStatus": JobStatus},
    total=False,
)

StartEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StartEntitiesDetectionJobResponseTypeDef", {"JobId": str, "JobStatus": JobStatus}, total=False
)

StartEventsDetectionJobResponseTypeDef = TypedDict(
    "StartEventsDetectionJobResponseTypeDef", {"JobId": str, "JobStatus": JobStatus}, total=False
)

StartKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "StartKeyPhrasesDetectionJobResponseTypeDef",
    {"JobId": str, "JobStatus": JobStatus},
    total=False,
)

StartPiiEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StartPiiEntitiesDetectionJobResponseTypeDef",
    {"JobId": str, "JobStatus": JobStatus},
    total=False,
)

StartSentimentDetectionJobResponseTypeDef = TypedDict(
    "StartSentimentDetectionJobResponseTypeDef", {"JobId": str, "JobStatus": JobStatus}, total=False
)

StartTopicsDetectionJobResponseTypeDef = TypedDict(
    "StartTopicsDetectionJobResponseTypeDef", {"JobId": str, "JobStatus": JobStatus}, total=False
)

StopDominantLanguageDetectionJobResponseTypeDef = TypedDict(
    "StopDominantLanguageDetectionJobResponseTypeDef",
    {"JobId": str, "JobStatus": JobStatus},
    total=False,
)

StopEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StopEntitiesDetectionJobResponseTypeDef", {"JobId": str, "JobStatus": JobStatus}, total=False
)

StopEventsDetectionJobResponseTypeDef = TypedDict(
    "StopEventsDetectionJobResponseTypeDef", {"JobId": str, "JobStatus": JobStatus}, total=False
)

StopKeyPhrasesDetectionJobResponseTypeDef = TypedDict(
    "StopKeyPhrasesDetectionJobResponseTypeDef", {"JobId": str, "JobStatus": JobStatus}, total=False
)

StopPiiEntitiesDetectionJobResponseTypeDef = TypedDict(
    "StopPiiEntitiesDetectionJobResponseTypeDef",
    {"JobId": str, "JobStatus": JobStatus},
    total=False,
)

StopSentimentDetectionJobResponseTypeDef = TypedDict(
    "StopSentimentDetectionJobResponseTypeDef", {"JobId": str, "JobStatus": JobStatus}, total=False
)

TopicsDetectionJobFilterTypeDef = TypedDict(
    "TopicsDetectionJobFilterTypeDef",
    {
        "JobName": str,
        "JobStatus": JobStatus,
        "SubmitTimeBefore": datetime,
        "SubmitTimeAfter": datetime,
    },
    total=False,
)
