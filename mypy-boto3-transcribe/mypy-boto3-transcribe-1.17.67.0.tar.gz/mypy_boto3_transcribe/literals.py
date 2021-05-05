"""
Type annotations for transcribe service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_transcribe/literals.html)

Usage::

    ```python
    from mypy_boto3_transcribe.literals import BaseModelName

    data: BaseModelName = "NarrowBand"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "BaseModelName",
    "CLMLanguageCode",
    "LanguageCode",
    "MediaFormat",
    "ModelStatus",
    "OutputLocationType",
    "RedactionOutput",
    "RedactionType",
    "Specialty",
    "TranscriptionJobStatus",
    "TypeType",
    "VocabularyFilterMethod",
    "VocabularyState",
)


BaseModelName = Literal["NarrowBand", "WideBand"]
CLMLanguageCode = Literal["en-AU", "en-GB", "en-US", "es-US", "hi-IN"]
LanguageCode = Literal[
    "af-ZA",
    "ar-AE",
    "ar-SA",
    "cy-GB",
    "da-DK",
    "de-CH",
    "de-DE",
    "en-AB",
    "en-AU",
    "en-GB",
    "en-IE",
    "en-IN",
    "en-US",
    "en-WL",
    "es-ES",
    "es-US",
    "fa-IR",
    "fr-CA",
    "fr-FR",
    "ga-IE",
    "gd-GB",
    "he-IL",
    "hi-IN",
    "id-ID",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "ms-MY",
    "nl-NL",
    "pt-BR",
    "pt-PT",
    "ru-RU",
    "ta-IN",
    "te-IN",
    "tr-TR",
    "zh-CN",
]
MediaFormat = Literal["amr", "flac", "mp3", "mp4", "ogg", "wav", "webm"]
ModelStatus = Literal["COMPLETED", "FAILED", "IN_PROGRESS"]
OutputLocationType = Literal["CUSTOMER_BUCKET", "SERVICE_BUCKET"]
RedactionOutput = Literal["redacted", "redacted_and_unredacted"]
RedactionType = Literal["PII"]
Specialty = Literal["PRIMARYCARE"]
TranscriptionJobStatus = Literal["COMPLETED", "FAILED", "IN_PROGRESS", "QUEUED"]
TypeType = Literal["CONVERSATION", "DICTATION"]
VocabularyFilterMethod = Literal["mask", "remove", "tag"]
VocabularyState = Literal["FAILED", "PENDING", "READY"]
