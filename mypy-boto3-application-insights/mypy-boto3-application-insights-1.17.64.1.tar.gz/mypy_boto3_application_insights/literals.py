"""
Type annotations for application-insights service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_application_insights/literals.html)

Usage::

    ```python
    from mypy_boto3_application_insights.literals import CloudWatchEventSource

    data: CloudWatchEventSource = "CODE_DEPLOY"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "CloudWatchEventSource",
    "ConfigurationEventResourceType",
    "ConfigurationEventStatus",
    "FeedbackKey",
    "FeedbackValue",
    "LogFilter",
    "OsType",
    "SeverityLevel",
    "Status",
    "Tier",
)


CloudWatchEventSource = Literal["CODE_DEPLOY", "EC2", "HEALTH", "RDS"]
ConfigurationEventResourceType = Literal[
    "CLOUDFORMATION", "CLOUDWATCH_ALARM", "CLOUDWATCH_LOG", "SSM_ASSOCIATION"
]
ConfigurationEventStatus = Literal["ERROR", "INFO", "WARN"]
FeedbackKey = Literal["INSIGHTS_FEEDBACK"]
FeedbackValue = Literal["NOT_SPECIFIED", "NOT_USEFUL", "USEFUL"]
LogFilter = Literal["ERROR", "INFO", "WARN"]
OsType = Literal["LINUX", "WINDOWS"]
SeverityLevel = Literal["High", "Low", "Medium"]
Status = Literal["IGNORE", "PENDING", "RESOLVED"]
Tier = Literal[
    "CUSTOM",
    "DEFAULT",
    "DOT_NET_CORE",
    "DOT_NET_WEB",
    "DOT_NET_WEB_TIER",
    "DOT_NET_WORKER",
    "JAVA_JMX",
    "MYSQL",
    "ORACLE",
    "POSTGRESQL",
    "SQL_SERVER",
    "SQL_SERVER_ALWAYSON_AVAILABILITY_GROUP",
]
