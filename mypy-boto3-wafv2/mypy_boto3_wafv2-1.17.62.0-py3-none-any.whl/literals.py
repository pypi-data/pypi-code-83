"""
Main interface for wafv2 service literal definitions.

Usage::

    ```python
    from mypy_boto3_wafv2.literals import ActionValue

    data: ActionValue = "ALLOW"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "ActionValue",
    "BodyParsingFallbackBehavior",
    "FilterBehavior",
    "FilterRequirement",
    "IPAddressVersion",
    "JsonMatchScope",
    "ResourceType",
    "ResponseContentType",
    "Scope",
)


ActionValue = Literal["ALLOW", "BLOCK", "COUNT"]
BodyParsingFallbackBehavior = Literal["EVALUATE_AS_STRING", "MATCH", "NO_MATCH"]
FilterBehavior = Literal["DROP", "KEEP"]
FilterRequirement = Literal["MEETS_ALL", "MEETS_ANY"]
IPAddressVersion = Literal["IPV4", "IPV6"]
JsonMatchScope = Literal["ALL", "KEY", "VALUE"]
ResourceType = Literal["API_GATEWAY", "APPLICATION_LOAD_BALANCER", "APPSYNC"]
ResponseContentType = Literal["APPLICATION_JSON", "TEXT_HTML", "TEXT_PLAIN"]
Scope = Literal["CLOUDFRONT", "REGIONAL"]
