"""
Type annotations for iotwireless service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_iotwireless/type_defs.html)

Usage::

    ```python
    from mypy_boto3_iotwireless.type_defs import AbpV1_0_xTypeDef

    data: AbpV1_0_xTypeDef = {...}
    ```
"""
import sys
from typing import List

from mypy_boto3_iotwireless.literals import (
    BatteryLevel,
    ConnectionStatus,
    DeviceState,
    Event,
    ExpressionType,
    MessageType,
    SigningAlg,
    WirelessDeviceType,
    WirelessGatewayServiceType,
    WirelessGatewayTaskStatus,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AbpV1_0_xTypeDef",
    "AbpV1_1TypeDef",
    "AssociateAwsAccountWithPartnerAccountResponseTypeDef",
    "AssociateWirelessGatewayWithCertificateResponseTypeDef",
    "CertificateListTypeDef",
    "CreateDestinationResponseTypeDef",
    "CreateDeviceProfileResponseTypeDef",
    "CreateServiceProfileResponseTypeDef",
    "CreateWirelessDeviceResponseTypeDef",
    "CreateWirelessGatewayResponseTypeDef",
    "CreateWirelessGatewayTaskDefinitionResponseTypeDef",
    "CreateWirelessGatewayTaskResponseTypeDef",
    "DestinationsTypeDef",
    "DeviceProfileTypeDef",
    "GetDestinationResponseTypeDef",
    "GetDeviceProfileResponseTypeDef",
    "GetPartnerAccountResponseTypeDef",
    "GetServiceEndpointResponseTypeDef",
    "GetServiceProfileResponseTypeDef",
    "GetWirelessDeviceResponseTypeDef",
    "GetWirelessDeviceStatisticsResponseTypeDef",
    "GetWirelessGatewayCertificateResponseTypeDef",
    "GetWirelessGatewayFirmwareInformationResponseTypeDef",
    "GetWirelessGatewayResponseTypeDef",
    "GetWirelessGatewayStatisticsResponseTypeDef",
    "GetWirelessGatewayTaskDefinitionResponseTypeDef",
    "GetWirelessGatewayTaskResponseTypeDef",
    "ListDestinationsResponseTypeDef",
    "ListDeviceProfilesResponseTypeDef",
    "ListPartnerAccountsResponseTypeDef",
    "ListServiceProfilesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWirelessDevicesResponseTypeDef",
    "ListWirelessGatewayTaskDefinitionsResponseTypeDef",
    "ListWirelessGatewaysResponseTypeDef",
    "LoRaWANDeviceMetadataTypeDef",
    "LoRaWANDeviceProfileTypeDef",
    "LoRaWANDeviceTypeDef",
    "LoRaWANGatewayCurrentVersionTypeDef",
    "LoRaWANGatewayMetadataTypeDef",
    "LoRaWANGatewayTypeDef",
    "LoRaWANGatewayVersionTypeDef",
    "LoRaWANGetServiceProfileInfoTypeDef",
    "LoRaWANListDeviceTypeDef",
    "LoRaWANSendDataToDeviceTypeDef",
    "LoRaWANServiceProfileTypeDef",
    "LoRaWANUpdateDeviceTypeDef",
    "LoRaWANUpdateGatewayTaskCreateTypeDef",
    "LoRaWANUpdateGatewayTaskEntryTypeDef",
    "OtaaV1_0_xTypeDef",
    "OtaaV1_1TypeDef",
    "SendDataToWirelessDeviceResponseTypeDef",
    "ServiceProfileTypeDef",
    "SessionKeysAbpV1_0_xTypeDef",
    "SessionKeysAbpV1_1TypeDef",
    "SidewalkAccountInfoTypeDef",
    "SidewalkAccountInfoWithFingerprintTypeDef",
    "SidewalkDeviceMetadataTypeDef",
    "SidewalkDeviceTypeDef",
    "SidewalkListDeviceTypeDef",
    "SidewalkSendDataToDeviceTypeDef",
    "SidewalkUpdateAccountTypeDef",
    "TagTypeDef",
    "TestWirelessDeviceResponseTypeDef",
    "UpdateWirelessGatewayTaskCreateTypeDef",
    "UpdateWirelessGatewayTaskEntryTypeDef",
    "WirelessDeviceStatisticsTypeDef",
    "WirelessGatewayStatisticsTypeDef",
    "WirelessMetadataTypeDef",
)


class AbpV1_0_xTypeDef(TypedDict, total=False):
    DevAddr: str
    SessionKeys: "SessionKeysAbpV1_0_xTypeDef"


class AbpV1_1TypeDef(TypedDict, total=False):
    DevAddr: str
    SessionKeys: "SessionKeysAbpV1_1TypeDef"


class AssociateAwsAccountWithPartnerAccountResponseTypeDef(TypedDict, total=False):
    Sidewalk: "SidewalkAccountInfoTypeDef"
    Arn: str


class AssociateWirelessGatewayWithCertificateResponseTypeDef(TypedDict, total=False):
    IotCertificateId: str


class CertificateListTypeDef(TypedDict):
    SigningAlg: SigningAlg
    Value: str


class CreateDestinationResponseTypeDef(TypedDict, total=False):
    Arn: str
    Name: str


class CreateDeviceProfileResponseTypeDef(TypedDict, total=False):
    Arn: str
    Id: str


class CreateServiceProfileResponseTypeDef(TypedDict, total=False):
    Arn: str
    Id: str


class CreateWirelessDeviceResponseTypeDef(TypedDict, total=False):
    Arn: str
    Id: str


class CreateWirelessGatewayResponseTypeDef(TypedDict, total=False):
    Arn: str
    Id: str


class CreateWirelessGatewayTaskDefinitionResponseTypeDef(TypedDict, total=False):
    Id: str
    Arn: str


class CreateWirelessGatewayTaskResponseTypeDef(TypedDict, total=False):
    WirelessGatewayTaskDefinitionId: str
    Status: WirelessGatewayTaskStatus


class DestinationsTypeDef(TypedDict, total=False):
    Arn: str
    Name: str
    ExpressionType: ExpressionType
    Expression: str
    Description: str
    RoleArn: str


class DeviceProfileTypeDef(TypedDict, total=False):
    Arn: str
    Name: str
    Id: str


class GetDestinationResponseTypeDef(TypedDict, total=False):
    Arn: str
    Name: str
    Expression: str
    ExpressionType: ExpressionType
    Description: str
    RoleArn: str


class GetDeviceProfileResponseTypeDef(TypedDict, total=False):
    Arn: str
    Name: str
    Id: str
    LoRaWAN: "LoRaWANDeviceProfileTypeDef"


class GetPartnerAccountResponseTypeDef(TypedDict, total=False):
    Sidewalk: "SidewalkAccountInfoWithFingerprintTypeDef"
    AccountLinked: bool


class GetServiceEndpointResponseTypeDef(TypedDict, total=False):
    ServiceType: WirelessGatewayServiceType
    ServiceEndpoint: str
    ServerTrust: str


class GetServiceProfileResponseTypeDef(TypedDict, total=False):
    Arn: str
    Name: str
    Id: str
    LoRaWAN: "LoRaWANGetServiceProfileInfoTypeDef"


GetWirelessDeviceResponseTypeDef = TypedDict(
    "GetWirelessDeviceResponseTypeDef",
    {
        "Type": WirelessDeviceType,
        "Name": str,
        "Description": str,
        "DestinationName": str,
        "Id": str,
        "Arn": str,
        "ThingName": str,
        "ThingArn": str,
        "LoRaWAN": "LoRaWANDeviceTypeDef",
        "Sidewalk": "SidewalkDeviceTypeDef",
    },
    total=False,
)


class GetWirelessDeviceStatisticsResponseTypeDef(TypedDict, total=False):
    WirelessDeviceId: str
    LastUplinkReceivedAt: str
    LoRaWAN: "LoRaWANDeviceMetadataTypeDef"
    Sidewalk: "SidewalkDeviceMetadataTypeDef"


class GetWirelessGatewayCertificateResponseTypeDef(TypedDict, total=False):
    IotCertificateId: str
    LoRaWANNetworkServerCertificateId: str


class GetWirelessGatewayFirmwareInformationResponseTypeDef(TypedDict, total=False):
    LoRaWAN: "LoRaWANGatewayCurrentVersionTypeDef"


class GetWirelessGatewayResponseTypeDef(TypedDict, total=False):
    Name: str
    Id: str
    Description: str
    LoRaWAN: "LoRaWANGatewayTypeDef"
    Arn: str
    ThingName: str
    ThingArn: str


class GetWirelessGatewayStatisticsResponseTypeDef(TypedDict, total=False):
    WirelessGatewayId: str
    LastUplinkReceivedAt: str
    ConnectionStatus: ConnectionStatus


class GetWirelessGatewayTaskDefinitionResponseTypeDef(TypedDict, total=False):
    AutoCreateTasks: bool
    Name: str
    Update: "UpdateWirelessGatewayTaskCreateTypeDef"
    Arn: str


class GetWirelessGatewayTaskResponseTypeDef(TypedDict, total=False):
    WirelessGatewayId: str
    WirelessGatewayTaskDefinitionId: str
    LastUplinkReceivedAt: str
    TaskCreatedAt: str
    Status: WirelessGatewayTaskStatus


class ListDestinationsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    DestinationList: List["DestinationsTypeDef"]


class ListDeviceProfilesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    DeviceProfileList: List["DeviceProfileTypeDef"]


class ListPartnerAccountsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    Sidewalk: List["SidewalkAccountInfoWithFingerprintTypeDef"]


class ListServiceProfilesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    ServiceProfileList: List["ServiceProfileTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    Tags: List["TagTypeDef"]


class ListWirelessDevicesResponseTypeDef(TypedDict, total=False):
    NextToken: str
    WirelessDeviceList: List["WirelessDeviceStatisticsTypeDef"]


class ListWirelessGatewayTaskDefinitionsResponseTypeDef(TypedDict, total=False):
    NextToken: str
    TaskDefinitions: List["UpdateWirelessGatewayTaskEntryTypeDef"]


class ListWirelessGatewaysResponseTypeDef(TypedDict, total=False):
    NextToken: str
    WirelessGatewayList: List["WirelessGatewayStatisticsTypeDef"]


class LoRaWANDeviceMetadataTypeDef(TypedDict, total=False):
    DevEui: str
    FPort: int
    DataRate: int
    Frequency: int
    Timestamp: str
    Gateways: List["LoRaWANGatewayMetadataTypeDef"]


class LoRaWANDeviceProfileTypeDef(TypedDict, total=False):
    SupportsClassB: bool
    ClassBTimeout: int
    PingSlotPeriod: int
    PingSlotDr: int
    PingSlotFreq: int
    SupportsClassC: bool
    ClassCTimeout: int
    MacVersion: str
    RegParamsRevision: str
    RxDelay1: int
    RxDrOffset1: int
    RxDataRate2: int
    RxFreq2: int
    FactoryPresetFreqsList: List[int]
    MaxEirp: int
    MaxDutyCycle: int
    RfRegion: str
    SupportsJoin: bool
    Supports32BitFCnt: bool


class LoRaWANDeviceTypeDef(TypedDict, total=False):
    DevEui: str
    DeviceProfileId: str
    ServiceProfileId: str
    OtaaV1_1: "OtaaV1_1TypeDef"
    OtaaV1_0_x: "OtaaV1_0_xTypeDef"
    AbpV1_1: "AbpV1_1TypeDef"
    AbpV1_0_x: "AbpV1_0_xTypeDef"


class LoRaWANGatewayCurrentVersionTypeDef(TypedDict, total=False):
    CurrentVersion: "LoRaWANGatewayVersionTypeDef"


class LoRaWANGatewayMetadataTypeDef(TypedDict, total=False):
    GatewayEui: str
    Snr: float
    Rssi: float


class LoRaWANGatewayTypeDef(TypedDict, total=False):
    GatewayEui: str
    RfRegion: str


class LoRaWANGatewayVersionTypeDef(TypedDict, total=False):
    PackageVersion: str
    Model: str
    Station: str


class LoRaWANGetServiceProfileInfoTypeDef(TypedDict, total=False):
    UlRate: int
    UlBucketSize: int
    UlRatePolicy: str
    DlRate: int
    DlBucketSize: int
    DlRatePolicy: str
    AddGwMetadata: bool
    DevStatusReqFreq: int
    ReportDevStatusBattery: bool
    ReportDevStatusMargin: bool
    DrMin: int
    DrMax: int
    ChannelMask: str
    PrAllowed: bool
    HrAllowed: bool
    RaAllowed: bool
    NwkGeoLoc: bool
    TargetPer: int
    MinGwDiversity: int


class LoRaWANListDeviceTypeDef(TypedDict, total=False):
    DevEui: str


class LoRaWANSendDataToDeviceTypeDef(TypedDict, total=False):
    FPort: int


class LoRaWANServiceProfileTypeDef(TypedDict, total=False):
    AddGwMetadata: bool


class LoRaWANUpdateDeviceTypeDef(TypedDict, total=False):
    DeviceProfileId: str
    ServiceProfileId: str


class LoRaWANUpdateGatewayTaskCreateTypeDef(TypedDict, total=False):
    UpdateSignature: str
    SigKeyCrc: int
    CurrentVersion: "LoRaWANGatewayVersionTypeDef"
    UpdateVersion: "LoRaWANGatewayVersionTypeDef"


class LoRaWANUpdateGatewayTaskEntryTypeDef(TypedDict, total=False):
    CurrentVersion: "LoRaWANGatewayVersionTypeDef"
    UpdateVersion: "LoRaWANGatewayVersionTypeDef"


class OtaaV1_0_xTypeDef(TypedDict, total=False):
    AppKey: str
    AppEui: str


class OtaaV1_1TypeDef(TypedDict, total=False):
    AppKey: str
    NwkKey: str
    JoinEui: str


class SendDataToWirelessDeviceResponseTypeDef(TypedDict, total=False):
    MessageId: str


class ServiceProfileTypeDef(TypedDict, total=False):
    Arn: str
    Name: str
    Id: str


class SessionKeysAbpV1_0_xTypeDef(TypedDict, total=False):
    NwkSKey: str
    AppSKey: str


class SessionKeysAbpV1_1TypeDef(TypedDict, total=False):
    FNwkSIntKey: str
    SNwkSIntKey: str
    NwkSEncKey: str
    AppSKey: str


class SidewalkAccountInfoTypeDef(TypedDict, total=False):
    AmazonId: str
    AppServerPrivateKey: str


class SidewalkAccountInfoWithFingerprintTypeDef(TypedDict, total=False):
    AmazonId: str
    Fingerprint: str
    Arn: str


class SidewalkDeviceMetadataTypeDef(TypedDict, total=False):
    Rssi: int
    BatteryLevel: BatteryLevel
    Event: Event
    DeviceState: DeviceState


class SidewalkDeviceTypeDef(TypedDict, total=False):
    SidewalkId: str
    SidewalkManufacturingSn: str
    DeviceCertificates: List["CertificateListTypeDef"]


class SidewalkListDeviceTypeDef(TypedDict, total=False):
    AmazonId: str
    SidewalkId: str
    SidewalkManufacturingSn: str
    DeviceCertificates: List["CertificateListTypeDef"]


class SidewalkSendDataToDeviceTypeDef(TypedDict, total=False):
    Seq: int
    MessageType: MessageType


class SidewalkUpdateAccountTypeDef(TypedDict, total=False):
    AppServerPrivateKey: str


class TagTypeDef(TypedDict):
    Key: str
    Value: str


class TestWirelessDeviceResponseTypeDef(TypedDict, total=False):
    Result: str


class UpdateWirelessGatewayTaskCreateTypeDef(TypedDict, total=False):
    UpdateDataSource: str
    UpdateDataRole: str
    LoRaWAN: "LoRaWANUpdateGatewayTaskCreateTypeDef"


class UpdateWirelessGatewayTaskEntryTypeDef(TypedDict, total=False):
    Id: str
    LoRaWAN: "LoRaWANUpdateGatewayTaskEntryTypeDef"
    Arn: str


WirelessDeviceStatisticsTypeDef = TypedDict(
    "WirelessDeviceStatisticsTypeDef",
    {
        "Arn": str,
        "Id": str,
        "Type": WirelessDeviceType,
        "Name": str,
        "DestinationName": str,
        "LastUplinkReceivedAt": str,
        "LoRaWAN": "LoRaWANListDeviceTypeDef",
        "Sidewalk": "SidewalkListDeviceTypeDef",
    },
    total=False,
)


class WirelessGatewayStatisticsTypeDef(TypedDict, total=False):
    Arn: str
    Id: str
    Name: str
    Description: str
    LoRaWAN: "LoRaWANGatewayTypeDef"
    LastUplinkReceivedAt: str


class WirelessMetadataTypeDef(TypedDict, total=False):
    LoRaWAN: "LoRaWANSendDataToDeviceTypeDef"
    Sidewalk: "SidewalkSendDataToDeviceTypeDef"
