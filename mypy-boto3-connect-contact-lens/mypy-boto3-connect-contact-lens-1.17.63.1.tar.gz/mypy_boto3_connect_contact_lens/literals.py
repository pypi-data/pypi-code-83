"""
Type annotations for connect-contact-lens service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_connect_contact_lens/literals.html)

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
