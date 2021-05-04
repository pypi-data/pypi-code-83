"""
Type annotations for groundstation service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_groundstation/type_defs.html)

Usage::

    ```python
    from mypy_boto3_groundstation.type_defs import AntennaDemodDecodeDetailsTypeDef

    data: AntennaDemodDecodeDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List

from mypy_boto3_groundstation.literals import (
    AngleUnits,
    BandwidthUnits,
    ConfigCapabilityType,
    ContactStatus,
    Criticality,
    EndpointStatus,
    FrequencyUnits,
    Polarization,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AntennaDemodDecodeDetailsTypeDef",
    "AntennaDownlinkConfigTypeDef",
    "AntennaDownlinkDemodDecodeConfigTypeDef",
    "AntennaUplinkConfigTypeDef",
    "ConfigDetailsTypeDef",
    "ConfigIdResponseTypeDef",
    "ConfigListItemTypeDef",
    "ConfigTypeDataTypeDef",
    "ContactDataTypeDef",
    "ContactIdResponseTypeDef",
    "DataflowDetailTypeDef",
    "DataflowEndpointConfigTypeDef",
    "DataflowEndpointGroupIdResponseTypeDef",
    "DataflowEndpointListItemTypeDef",
    "DataflowEndpointTypeDef",
    "DecodeConfigTypeDef",
    "DemodulationConfigTypeDef",
    "DescribeContactResponseTypeDef",
    "DestinationTypeDef",
    "EirpTypeDef",
    "ElevationTypeDef",
    "EndpointDetailsTypeDef",
    "FrequencyBandwidthTypeDef",
    "FrequencyTypeDef",
    "GetConfigResponseTypeDef",
    "GetDataflowEndpointGroupResponseTypeDef",
    "GetMinuteUsageResponseTypeDef",
    "GetMissionProfileResponseTypeDef",
    "GetSatelliteResponseTypeDef",
    "GroundStationDataTypeDef",
    "ListConfigsResponseTypeDef",
    "ListContactsResponseTypeDef",
    "ListDataflowEndpointGroupsResponseTypeDef",
    "ListGroundStationsResponseTypeDef",
    "ListMissionProfilesResponseTypeDef",
    "ListSatellitesResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MissionProfileIdResponseTypeDef",
    "MissionProfileListItemTypeDef",
    "PaginatorConfigTypeDef",
    "S3RecordingConfigTypeDef",
    "S3RecordingDetailsTypeDef",
    "SatelliteListItemTypeDef",
    "SecurityDetailsTypeDef",
    "SocketAddressTypeDef",
    "SourceTypeDef",
    "SpectrumConfigTypeDef",
    "TrackingConfigTypeDef",
    "UplinkEchoConfigTypeDef",
    "UplinkSpectrumConfigTypeDef",
)


class AntennaDemodDecodeDetailsTypeDef(TypedDict, total=False):
    outputNode: str


class AntennaDownlinkConfigTypeDef(TypedDict):
    spectrumConfig: "SpectrumConfigTypeDef"


class AntennaDownlinkDemodDecodeConfigTypeDef(TypedDict):
    decodeConfig: "DecodeConfigTypeDef"
    demodulationConfig: "DemodulationConfigTypeDef"
    spectrumConfig: "SpectrumConfigTypeDef"


class _RequiredAntennaUplinkConfigTypeDef(TypedDict):
    spectrumConfig: "UplinkSpectrumConfigTypeDef"
    targetEirp: "EirpTypeDef"


class AntennaUplinkConfigTypeDef(_RequiredAntennaUplinkConfigTypeDef, total=False):
    transmitDisabled: bool


class ConfigDetailsTypeDef(TypedDict, total=False):
    antennaDemodDecodeDetails: "AntennaDemodDecodeDetailsTypeDef"
    endpointDetails: "EndpointDetailsTypeDef"
    s3RecordingDetails: "S3RecordingDetailsTypeDef"


class ConfigIdResponseTypeDef(TypedDict, total=False):
    configArn: str
    configId: str
    configType: ConfigCapabilityType


class ConfigListItemTypeDef(TypedDict, total=False):
    configArn: str
    configId: str
    configType: ConfigCapabilityType
    name: str


class ConfigTypeDataTypeDef(TypedDict, total=False):
    antennaDownlinkConfig: "AntennaDownlinkConfigTypeDef"
    antennaDownlinkDemodDecodeConfig: "AntennaDownlinkDemodDecodeConfigTypeDef"
    antennaUplinkConfig: "AntennaUplinkConfigTypeDef"
    dataflowEndpointConfig: "DataflowEndpointConfigTypeDef"
    s3RecordingConfig: "S3RecordingConfigTypeDef"
    trackingConfig: "TrackingConfigTypeDef"
    uplinkEchoConfig: "UplinkEchoConfigTypeDef"


class ContactDataTypeDef(TypedDict, total=False):
    contactId: str
    contactStatus: ContactStatus
    endTime: datetime
    errorMessage: str
    groundStation: str
    maximumElevation: "ElevationTypeDef"
    missionProfileArn: str
    postPassEndTime: datetime
    prePassStartTime: datetime
    region: str
    satelliteArn: str
    startTime: datetime
    tags: Dict[str, str]


class ContactIdResponseTypeDef(TypedDict, total=False):
    contactId: str


class DataflowDetailTypeDef(TypedDict, total=False):
    destination: "DestinationTypeDef"
    errorMessage: str
    source: "SourceTypeDef"


class _RequiredDataflowEndpointConfigTypeDef(TypedDict):
    dataflowEndpointName: str


class DataflowEndpointConfigTypeDef(_RequiredDataflowEndpointConfigTypeDef, total=False):
    dataflowEndpointRegion: str


class DataflowEndpointGroupIdResponseTypeDef(TypedDict, total=False):
    dataflowEndpointGroupId: str


class DataflowEndpointListItemTypeDef(TypedDict, total=False):
    dataflowEndpointGroupArn: str
    dataflowEndpointGroupId: str


class DataflowEndpointTypeDef(TypedDict, total=False):
    address: "SocketAddressTypeDef"
    mtu: int
    name: str
    status: EndpointStatus


class DecodeConfigTypeDef(TypedDict):
    unvalidatedJSON: str


class DemodulationConfigTypeDef(TypedDict):
    unvalidatedJSON: str


class DescribeContactResponseTypeDef(TypedDict, total=False):
    contactId: str
    contactStatus: ContactStatus
    dataflowList: List["DataflowDetailTypeDef"]
    endTime: datetime
    errorMessage: str
    groundStation: str
    maximumElevation: "ElevationTypeDef"
    missionProfileArn: str
    postPassEndTime: datetime
    prePassStartTime: datetime
    region: str
    satelliteArn: str
    startTime: datetime
    tags: Dict[str, str]


class DestinationTypeDef(TypedDict, total=False):
    configDetails: "ConfigDetailsTypeDef"
    configId: str
    configType: ConfigCapabilityType
    dataflowDestinationRegion: str


class EirpTypeDef(TypedDict):
    units: Literal["dBW"]
    value: float


class ElevationTypeDef(TypedDict):
    unit: AngleUnits
    value: float


class EndpointDetailsTypeDef(TypedDict, total=False):
    endpoint: "DataflowEndpointTypeDef"
    securityDetails: "SecurityDetailsTypeDef"


class FrequencyBandwidthTypeDef(TypedDict):
    units: BandwidthUnits
    value: float


class FrequencyTypeDef(TypedDict):
    units: FrequencyUnits
    value: float


class _RequiredGetConfigResponseTypeDef(TypedDict):
    configArn: str
    configData: "ConfigTypeDataTypeDef"
    configId: str
    name: str


class GetConfigResponseTypeDef(_RequiredGetConfigResponseTypeDef, total=False):
    configType: ConfigCapabilityType
    tags: Dict[str, str]


class GetDataflowEndpointGroupResponseTypeDef(TypedDict, total=False):
    dataflowEndpointGroupArn: str
    dataflowEndpointGroupId: str
    endpointsDetails: List["EndpointDetailsTypeDef"]
    tags: Dict[str, str]


class GetMinuteUsageResponseTypeDef(TypedDict, total=False):
    estimatedMinutesRemaining: int
    isReservedMinutesCustomer: bool
    totalReservedMinuteAllocation: int
    totalScheduledMinutes: int
    upcomingMinutesScheduled: int


class GetMissionProfileResponseTypeDef(TypedDict, total=False):
    contactPostPassDurationSeconds: int
    contactPrePassDurationSeconds: int
    dataflowEdges: List[List[str]]
    minimumViableContactDurationSeconds: int
    missionProfileArn: str
    missionProfileId: str
    name: str
    region: str
    tags: Dict[str, str]
    trackingConfigArn: str


class GetSatelliteResponseTypeDef(TypedDict, total=False):
    groundStations: List[str]
    noradSatelliteID: int
    satelliteArn: str
    satelliteId: str


class GroundStationDataTypeDef(TypedDict, total=False):
    groundStationId: str
    groundStationName: str
    region: str


class ListConfigsResponseTypeDef(TypedDict, total=False):
    configList: List["ConfigListItemTypeDef"]
    nextToken: str


class ListContactsResponseTypeDef(TypedDict, total=False):
    contactList: List["ContactDataTypeDef"]
    nextToken: str


class ListDataflowEndpointGroupsResponseTypeDef(TypedDict, total=False):
    dataflowEndpointGroupList: List["DataflowEndpointListItemTypeDef"]
    nextToken: str


class ListGroundStationsResponseTypeDef(TypedDict, total=False):
    groundStationList: List["GroundStationDataTypeDef"]
    nextToken: str


class ListMissionProfilesResponseTypeDef(TypedDict, total=False):
    missionProfileList: List["MissionProfileListItemTypeDef"]
    nextToken: str


class ListSatellitesResponseTypeDef(TypedDict, total=False):
    nextToken: str
    satellites: List["SatelliteListItemTypeDef"]


class ListTagsForResourceResponseTypeDef(TypedDict, total=False):
    tags: Dict[str, str]


class MissionProfileIdResponseTypeDef(TypedDict, total=False):
    missionProfileId: str


class MissionProfileListItemTypeDef(TypedDict, total=False):
    missionProfileArn: str
    missionProfileId: str
    name: str
    region: str


class PaginatorConfigTypeDef(TypedDict, total=False):
    MaxItems: int
    PageSize: int
    StartingToken: str


class _RequiredS3RecordingConfigTypeDef(TypedDict):
    bucketArn: str
    roleArn: str


class S3RecordingConfigTypeDef(_RequiredS3RecordingConfigTypeDef, total=False):
    prefix: str


class S3RecordingDetailsTypeDef(TypedDict, total=False):
    bucketArn: str
    keyTemplate: str


class SatelliteListItemTypeDef(TypedDict, total=False):
    groundStations: List[str]
    noradSatelliteID: int
    satelliteArn: str
    satelliteId: str


class SecurityDetailsTypeDef(TypedDict):
    roleArn: str
    securityGroupIds: List[str]
    subnetIds: List[str]


class SocketAddressTypeDef(TypedDict):
    name: str
    port: int


class SourceTypeDef(TypedDict, total=False):
    configDetails: "ConfigDetailsTypeDef"
    configId: str
    configType: ConfigCapabilityType
    dataflowSourceRegion: str


class _RequiredSpectrumConfigTypeDef(TypedDict):
    bandwidth: "FrequencyBandwidthTypeDef"
    centerFrequency: "FrequencyTypeDef"


class SpectrumConfigTypeDef(_RequiredSpectrumConfigTypeDef, total=False):
    polarization: Polarization


class TrackingConfigTypeDef(TypedDict):
    autotrack: Criticality


class UplinkEchoConfigTypeDef(TypedDict):
    antennaUplinkConfigArn: str
    enabled: bool


class _RequiredUplinkSpectrumConfigTypeDef(TypedDict):
    centerFrequency: "FrequencyTypeDef"


class UplinkSpectrumConfigTypeDef(_RequiredUplinkSpectrumConfigTypeDef, total=False):
    polarization: Polarization
