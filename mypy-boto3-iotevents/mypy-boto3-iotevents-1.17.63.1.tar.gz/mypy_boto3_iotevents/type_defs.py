"""
Type annotations for iotevents service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotevents/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotevents.type_defs import ActionTypeDef

    data: ActionTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import List

from mypy_boto3_iotevents.literals import (
    AnalysisResultLevel,
    AnalysisStatus,
    DetectorModelVersionStatus,
    EvaluationMethod,
    InputStatus,
    LoggingLevel,
    PayloadType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "ActionTypeDef",
    "AnalysisResultLocationTypeDef",
    "AnalysisResultTypeDef",
    "AssetPropertyTimestampTypeDef",
    "AssetPropertyValueTypeDef",
    "AssetPropertyVariantTypeDef",
    "AttributeTypeDef",
    "ClearTimerActionTypeDef",
    "CreateDetectorModelResponseTypeDef",
    "CreateInputResponseTypeDef",
    "DescribeDetectorModelAnalysisResponseTypeDef",
    "DescribeDetectorModelResponseTypeDef",
    "DescribeInputResponseTypeDef",
    "DescribeLoggingOptionsResponseTypeDef",
    "DetectorDebugOptionTypeDef",
    "DetectorModelConfigurationTypeDef",
    "DetectorModelDefinitionTypeDef",
    "DetectorModelSummaryTypeDef",
    "DetectorModelTypeDef",
    "DetectorModelVersionSummaryTypeDef",
    "DynamoDBActionTypeDef",
    "DynamoDBv2ActionTypeDef",
    "EventTypeDef",
    "FirehoseActionTypeDef",
    "GetDetectorModelAnalysisResultsResponseTypeDef",
    "InputConfigurationTypeDef",
    "InputDefinitionTypeDef",
    "InputSummaryTypeDef",
    "InputTypeDef",
    "IotEventsActionTypeDef",
    "IotSiteWiseActionTypeDef",
    "IotTopicPublishActionTypeDef",
    "LambdaActionTypeDef",
    "ListDetectorModelVersionsResponseTypeDef",
    "ListDetectorModelsResponseTypeDef",
    "ListInputsResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "LoggingOptionsTypeDef",
    "OnEnterLifecycleTypeDef",
    "OnExitLifecycleTypeDef",
    "OnInputLifecycleTypeDef",
    "PayloadTypeDef",
    "ResetTimerActionTypeDef",
    "SNSTopicPublishActionTypeDef",
    "SetTimerActionTypeDef",
    "SetVariableActionTypeDef",
    "SqsActionTypeDef",
    "StartDetectorModelAnalysisResponseTypeDef",
    "StateTypeDef",
    "TagTypeDef",
    "TransitionEventTypeDef",
    "UpdateDetectorModelResponseTypeDef",
    "UpdateInputResponseTypeDef",
)

ActionTypeDef = TypedDict(
    "ActionTypeDef",
    {
        "setVariable": "SetVariableActionTypeDef",
        "sns": "SNSTopicPublishActionTypeDef",
        "iotTopicPublish": "IotTopicPublishActionTypeDef",
        "setTimer": "SetTimerActionTypeDef",
        "clearTimer": "ClearTimerActionTypeDef",
        "resetTimer": "ResetTimerActionTypeDef",
        "lambda": "LambdaActionTypeDef",
        "iotEvents": "IotEventsActionTypeDef",
        "sqs": "SqsActionTypeDef",
        "firehose": "FirehoseActionTypeDef",
        "dynamoDB": "DynamoDBActionTypeDef",
        "dynamoDBv2": "DynamoDBv2ActionTypeDef",
        "iotSiteWise": "IotSiteWiseActionTypeDef",
    },
    total=False,
)


class AnalysisResultLocationTypeDef(TypedDict, total=False):
    path: str


AnalysisResultTypeDef = TypedDict(
    "AnalysisResultTypeDef",
    {
        "type": str,
        "level": AnalysisResultLevel,
        "message": str,
        "locations": List["AnalysisResultLocationTypeDef"],
    },
    total=False,
)


class _RequiredAssetPropertyTimestampTypeDef(TypedDict):
    timeInSeconds: str


class AssetPropertyTimestampTypeDef(_RequiredAssetPropertyTimestampTypeDef, total=False):
    offsetInNanos: str


class _RequiredAssetPropertyValueTypeDef(TypedDict):
    value: "AssetPropertyVariantTypeDef"


class AssetPropertyValueTypeDef(_RequiredAssetPropertyValueTypeDef, total=False):
    timestamp: "AssetPropertyTimestampTypeDef"
    quality: str


class AssetPropertyVariantTypeDef(TypedDict, total=False):
    stringValue: str
    integerValue: str
    doubleValue: str
    booleanValue: str


class AttributeTypeDef(TypedDict):
    jsonPath: str


class ClearTimerActionTypeDef(TypedDict):
    timerName: str


class CreateDetectorModelResponseTypeDef(TypedDict, total=False):
    detectorModelConfiguration: "DetectorModelConfigurationTypeDef"


class CreateInputResponseTypeDef(TypedDict, total=False):
    inputConfiguration: "InputConfigurationTypeDef"


class DescribeDetectorModelAnalysisResponseTypeDef(TypedDict, total=False):
    status: AnalysisStatus


class DescribeDetectorModelResponseTypeDef(TypedDict, total=False):
    detectorModel: "DetectorModelTypeDef"


DescribeInputResponseTypeDef = TypedDict(
    "DescribeInputResponseTypeDef", {"input": "InputTypeDef"}, total=False
)


class DescribeLoggingOptionsResponseTypeDef(TypedDict, total=False):
    loggingOptions: "LoggingOptionsTypeDef"


class _RequiredDetectorDebugOptionTypeDef(TypedDict):
    detectorModelName: str


class DetectorDebugOptionTypeDef(_RequiredDetectorDebugOptionTypeDef, total=False):
    keyValue: str


class DetectorModelConfigurationTypeDef(TypedDict, total=False):
    detectorModelName: str
    detectorModelVersion: str
    detectorModelDescription: str
    detectorModelArn: str
    roleArn: str
    creationTime: datetime
    lastUpdateTime: datetime
    status: DetectorModelVersionStatus
    key: str
    evaluationMethod: EvaluationMethod


class DetectorModelDefinitionTypeDef(TypedDict):
    states: List["StateTypeDef"]
    initialStateName: str


class DetectorModelSummaryTypeDef(TypedDict, total=False):
    detectorModelName: str
    detectorModelDescription: str
    creationTime: datetime


class DetectorModelTypeDef(TypedDict, total=False):
    detectorModelDefinition: "DetectorModelDefinitionTypeDef"
    detectorModelConfiguration: "DetectorModelConfigurationTypeDef"


class DetectorModelVersionSummaryTypeDef(TypedDict, total=False):
    detectorModelName: str
    detectorModelVersion: str
    detectorModelArn: str
    roleArn: str
    creationTime: datetime
    lastUpdateTime: datetime
    status: DetectorModelVersionStatus
    evaluationMethod: EvaluationMethod


class _RequiredDynamoDBActionTypeDef(TypedDict):
    hashKeyField: str
    hashKeyValue: str
    tableName: str


class DynamoDBActionTypeDef(_RequiredDynamoDBActionTypeDef, total=False):
    hashKeyType: str
    rangeKeyType: str
    rangeKeyField: str
    rangeKeyValue: str
    operation: str
    payloadField: str
    payload: "PayloadTypeDef"


class _RequiredDynamoDBv2ActionTypeDef(TypedDict):
    tableName: str


class DynamoDBv2ActionTypeDef(_RequiredDynamoDBv2ActionTypeDef, total=False):
    payload: "PayloadTypeDef"


class _RequiredEventTypeDef(TypedDict):
    eventName: str


class EventTypeDef(_RequiredEventTypeDef, total=False):
    condition: str
    actions: List["ActionTypeDef"]


class _RequiredFirehoseActionTypeDef(TypedDict):
    deliveryStreamName: str


class FirehoseActionTypeDef(_RequiredFirehoseActionTypeDef, total=False):
    separator: str
    payload: "PayloadTypeDef"


class GetDetectorModelAnalysisResultsResponseTypeDef(TypedDict, total=False):
    analysisResults: List["AnalysisResultTypeDef"]
    nextToken: str


class _RequiredInputConfigurationTypeDef(TypedDict):
    inputName: str
    inputArn: str
    creationTime: datetime
    lastUpdateTime: datetime
    status: InputStatus


class InputConfigurationTypeDef(_RequiredInputConfigurationTypeDef, total=False):
    inputDescription: str


class InputDefinitionTypeDef(TypedDict):
    attributes: List["AttributeTypeDef"]


class InputSummaryTypeDef(TypedDict, total=False):
    inputName: str
    inputDescription: str
    inputArn: str
    creationTime: datetime
    lastUpdateTime: datetime
    status: InputStatus


class InputTypeDef(TypedDict, total=False):
    inputConfiguration: "InputConfigurationTypeDef"
    inputDefinition: "InputDefinitionTypeDef"


class _RequiredIotEventsActionTypeDef(TypedDict):
    inputName: str


class IotEventsActionTypeDef(_RequiredIotEventsActionTypeDef, total=False):
    payload: "PayloadTypeDef"


class _RequiredIotSiteWiseActionTypeDef(TypedDict):
    propertyValue: "AssetPropertyValueTypeDef"


class IotSiteWiseActionTypeDef(_RequiredIotSiteWiseActionTypeDef, total=False):
    entryId: str
    assetId: str
    propertyId: str
    propertyAlias: str


class _RequiredIotTopicPublishActionTypeDef(TypedDict):
    mqttTopic: str


class IotTopicPublishActionTypeDef(_RequiredIotTopicPublishActionTypeDef, total=False):
    payload: "PayloadTypeDef"


class _RequiredLambdaActionTypeDef(TypedDict):
    functionArn: str


class LambdaActionTypeDef(_RequiredLambdaActionTypeDef, total=False):
    payload: "PayloadTypeDef"


class ListDetectorModelVersionsResponseTypeDef(TypedDict, total=False):
    detectorModelVersionSummaries: List["DetectorModelVersionSummaryTypeDef"]
    nextToken: str


class ListDetectorModelsResponseTypeDef(TypedDict, total=False):
    detectorModelSummaries: List["DetectorModelSummaryTypeDef"]
    nextToken: str


class ListInputsResponseTypeDef(TypedDict, total=False):
    inputSummaries: List["InputSummaryTypeDef"]
    nextToken: str


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: List["TagTypeDef"]


class _RequiredLoggingOptionsTypeDef(TypedDict):
    roleArn: str
    level: LoggingLevel
    enabled: bool


class LoggingOptionsTypeDef(_RequiredLoggingOptionsTypeDef, total=False):
    detectorDebugOptions: List["DetectorDebugOptionTypeDef"]


class OnEnterLifecycleTypeDef(TypedDict, total=False):
    events: List["EventTypeDef"]


class OnExitLifecycleTypeDef(TypedDict, total=False):
    events: List["EventTypeDef"]


class OnInputLifecycleTypeDef(TypedDict, total=False):
    events: List["EventTypeDef"]
    transitionEvents: List["TransitionEventTypeDef"]


PayloadTypeDef = TypedDict("PayloadTypeDef", {"contentExpression": str, "type": PayloadType})


class ResetTimerActionTypeDef(TypedDict):
    timerName: str


class _RequiredSNSTopicPublishActionTypeDef(TypedDict):
    targetArn: str


class SNSTopicPublishActionTypeDef(_RequiredSNSTopicPublishActionTypeDef, total=False):
    payload: "PayloadTypeDef"


class _RequiredSetTimerActionTypeDef(TypedDict):
    timerName: str


class SetTimerActionTypeDef(_RequiredSetTimerActionTypeDef, total=False):
    seconds: int
    durationExpression: str


class SetVariableActionTypeDef(TypedDict):
    variableName: str
    value: str


class _RequiredSqsActionTypeDef(TypedDict):
    queueUrl: str


class SqsActionTypeDef(_RequiredSqsActionTypeDef, total=False):
    useBase64: bool
    payload: "PayloadTypeDef"


class StartDetectorModelAnalysisResponseTypeDef(TypedDict, total=False):
    analysisId: str


class _RequiredStateTypeDef(TypedDict):
    stateName: str


class StateTypeDef(_RequiredStateTypeDef, total=False):
    onInput: "OnInputLifecycleTypeDef"
    onEnter: "OnEnterLifecycleTypeDef"
    onExit: "OnExitLifecycleTypeDef"


class TagTypeDef(TypedDict):
    key: str
    value: str


class _RequiredTransitionEventTypeDef(TypedDict):
    eventName: str
    condition: str
    nextState: str


class TransitionEventTypeDef(_RequiredTransitionEventTypeDef, total=False):
    actions: List["ActionTypeDef"]


class UpdateDetectorModelResponseTypeDef(TypedDict, total=False):
    detectorModelConfiguration: "DetectorModelConfigurationTypeDef"


class UpdateInputResponseTypeDef(TypedDict, total=False):
    inputConfiguration: "InputConfigurationTypeDef"
