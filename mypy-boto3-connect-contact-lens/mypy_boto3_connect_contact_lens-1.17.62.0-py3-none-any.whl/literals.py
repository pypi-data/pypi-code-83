"""
Main interface for connect-contact-lens service literal definitions.

Usage::

    ```python
    from mypy_boto3_connect_contact_lens.literals import SentimentValue

    data: SentimentValue = "NEGATIVE"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SentimentValue",)


SentimentValue = Literal["NEGATIVE", "NEUTRAL", "POSITIVE"]
