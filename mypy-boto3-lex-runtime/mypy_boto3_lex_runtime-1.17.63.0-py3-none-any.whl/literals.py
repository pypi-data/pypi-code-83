"""
Type annotations for lex-runtime service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_lex_runtime/literals.html)

Usage::

    ```python
    from mypy_boto3_lex_runtime.literals import ConfirmationStatus

    data: ConfirmationStatus = "Confirmed"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ConfirmationStatus",
    "ContentType",
    "DialogActionType",
    "DialogState",
    "FulfillmentState",
    "MessageFormatType",
)


ConfirmationStatus = Literal["Confirmed", "Denied", "None"]
ContentType = Literal["application/vnd.amazonaws.card.generic"]
DialogActionType = Literal["Close", "ConfirmIntent", "Delegate", "ElicitIntent", "ElicitSlot"]
DialogState = Literal[
    "ConfirmIntent", "ElicitIntent", "ElicitSlot", "Failed", "Fulfilled", "ReadyForFulfillment"
]
FulfillmentState = Literal["Failed", "Fulfilled", "ReadyForFulfillment"]
MessageFormatType = Literal["Composite", "CustomPayload", "PlainText", "SSML"]
