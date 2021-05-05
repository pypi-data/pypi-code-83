"""
Type annotations for comprehend service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_comprehend/literals.html)

Usage::

    ```python
    from mypy_boto3_comprehend.literals import DocumentClassifierDataFormat

    data: DocumentClassifierDataFormat = "AUGMENTED_MANIFEST"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DocumentClassifierDataFormat",
    "DocumentClassifierMode",
    "EndpointStatus",
    "EntityRecognizerDataFormat",
    "EntityType",
    "InputFormat",
    "JobStatus",
    "LanguageCode",
    "ListDocumentClassificationJobsPaginatorName",
    "ListDocumentClassifiersPaginatorName",
    "ListDominantLanguageDetectionJobsPaginatorName",
    "ListEntitiesDetectionJobsPaginatorName",
    "ListEntityRecognizersPaginatorName",
    "ListKeyPhrasesDetectionJobsPaginatorName",
    "ListSentimentDetectionJobsPaginatorName",
    "ListTopicsDetectionJobsPaginatorName",
    "ModelStatus",
    "PartOfSpeechTagType",
    "PiiEntitiesDetectionMaskMode",
    "PiiEntitiesDetectionMode",
    "PiiEntityType",
    "SentimentType",
    "SyntaxLanguageCode",
)


DocumentClassifierDataFormat = Literal["AUGMENTED_MANIFEST", "COMPREHEND_CSV"]
DocumentClassifierMode = Literal["MULTI_CLASS", "MULTI_LABEL"]
EndpointStatus = Literal["CREATING", "DELETING", "FAILED", "IN_SERVICE", "UPDATING"]
EntityRecognizerDataFormat = Literal["AUGMENTED_MANIFEST", "COMPREHEND_CSV"]
EntityType = Literal[
    "COMMERCIAL_ITEM",
    "DATE",
    "EVENT",
    "LOCATION",
    "ORGANIZATION",
    "OTHER",
    "PERSON",
    "QUANTITY",
    "TITLE",
]
InputFormat = Literal["ONE_DOC_PER_FILE", "ONE_DOC_PER_LINE"]
JobStatus = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "STOPPED", "STOP_REQUESTED", "SUBMITTED"]
LanguageCode = Literal["ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "pt", "zh", "zh-TW"]
ListDocumentClassificationJobsPaginatorName = Literal["list_document_classification_jobs"]
ListDocumentClassifiersPaginatorName = Literal["list_document_classifiers"]
ListDominantLanguageDetectionJobsPaginatorName = Literal["list_dominant_language_detection_jobs"]
ListEntitiesDetectionJobsPaginatorName = Literal["list_entities_detection_jobs"]
ListEntityRecognizersPaginatorName = Literal["list_entity_recognizers"]
ListKeyPhrasesDetectionJobsPaginatorName = Literal["list_key_phrases_detection_jobs"]
ListSentimentDetectionJobsPaginatorName = Literal["list_sentiment_detection_jobs"]
ListTopicsDetectionJobsPaginatorName = Literal["list_topics_detection_jobs"]
ModelStatus = Literal[
    "DELETING", "IN_ERROR", "STOPPED", "STOP_REQUESTED", "SUBMITTED", "TRAINED", "TRAINING"
]
PartOfSpeechTagType = Literal[
    "ADJ",
    "ADP",
    "ADV",
    "AUX",
    "CCONJ",
    "CONJ",
    "DET",
    "INTJ",
    "NOUN",
    "NUM",
    "O",
    "PART",
    "PRON",
    "PROPN",
    "PUNCT",
    "SCONJ",
    "SYM",
    "VERB",
]
PiiEntitiesDetectionMaskMode = Literal["MASK", "REPLACE_WITH_PII_ENTITY_TYPE"]
PiiEntitiesDetectionMode = Literal["ONLY_OFFSETS", "ONLY_REDACTION"]
PiiEntityType = Literal[
    "ADDRESS",
    "AGE",
    "ALL",
    "AWS_ACCESS_KEY",
    "AWS_SECRET_KEY",
    "BANK_ACCOUNT_NUMBER",
    "BANK_ROUTING",
    "CREDIT_DEBIT_CVV",
    "CREDIT_DEBIT_EXPIRY",
    "CREDIT_DEBIT_NUMBER",
    "DATE_TIME",
    "DRIVER_ID",
    "EMAIL",
    "IP_ADDRESS",
    "MAC_ADDRESS",
    "NAME",
    "PASSPORT_NUMBER",
    "PASSWORD",
    "PHONE",
    "PIN",
    "SSN",
    "URL",
    "USERNAME",
]
SentimentType = Literal["MIXED", "NEGATIVE", "NEUTRAL", "POSITIVE"]
SyntaxLanguageCode = Literal["de", "en", "es", "fr", "it", "pt"]
