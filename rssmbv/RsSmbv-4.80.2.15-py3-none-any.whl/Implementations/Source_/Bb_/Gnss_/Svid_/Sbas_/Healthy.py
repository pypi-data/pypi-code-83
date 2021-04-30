from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Healthy:
	"""Healthy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("healthy", core, parent)

	def set(self, healthy_state: bool, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:SBAS:HEALthy \n
		Snippet: driver.source.bb.gnss.svid.sbas.healthy.set(healthy_state = False, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Indicates if the selected SV ID is healthy or not. \n
			:param healthy_state: 0| 1| OFF| ON 1 = healthy satellite The healthy state reflects the value of the corresponding healthy flag in the navigation message: method RsSmbv.Source.Bb.Gnss.Svid.Gps.Nmessage.Lnav.Ephemeris.Health.set method RsSmbv.Source.Bb.Gnss.Svid.Gps.Nmessage.Cnav.Ephemeris.L1Health.set method RsSmbv.Source.Bb.Gnss.Svid.Gps.Nmessage.Cnav.Ephemeris.L2Health.set method RsSmbv.Source.Bb.Gnss.Svid.Gps.Nmessage.Cnav.Ephemeris.L5Health.set method RsSmbv.Source.Bb.Gnss.Svid.Galileo.Nmessage.Inav.E1Bdvs.set method RsSmbv.Source.Bb.Gnss.Svid.Galileo.Nmessage.Inav.E1Bhs.set method RsSmbv.Source.Bb.Gnss.Svid.Galileo.Nmessage.Inav.E5Bhs.set method RsSmbv.Source.Bb.Gnss.Svid.Beidou.Nmessage.Dnav.Ephemeris.Health.set method RsSmbv.Source.Bb.Gnss.Svid.Glonass.Nmessage.Nav.Ephemeris.Health.set method RsSmbv.Source.Bb.Gnss.Svid.Qzss.Nmessage.Nav.Ephemeris.Health.set The values are interdependent; changing one of them changes the other.
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')"""
		param = Conversions.bool_to_str(healthy_state)
		satelliteSvid_cmd_val = self._base.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:SBAS:HEALthy {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:SBAS:HEALthy \n
		Snippet: value: bool = driver.source.bb.gnss.svid.sbas.healthy.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Indicates if the selected SV ID is healthy or not. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: healthy_state: 0| 1| OFF| ON 1 = healthy satellite The healthy state reflects the value of the corresponding healthy flag in the navigation message: method RsSmbv.Source.Bb.Gnss.Svid.Gps.Nmessage.Lnav.Ephemeris.Health.set method RsSmbv.Source.Bb.Gnss.Svid.Gps.Nmessage.Cnav.Ephemeris.L1Health.set method RsSmbv.Source.Bb.Gnss.Svid.Gps.Nmessage.Cnav.Ephemeris.L2Health.set method RsSmbv.Source.Bb.Gnss.Svid.Gps.Nmessage.Cnav.Ephemeris.L5Health.set method RsSmbv.Source.Bb.Gnss.Svid.Galileo.Nmessage.Inav.E1Bdvs.set method RsSmbv.Source.Bb.Gnss.Svid.Galileo.Nmessage.Inav.E1Bhs.set method RsSmbv.Source.Bb.Gnss.Svid.Galileo.Nmessage.Inav.E5Bhs.set method RsSmbv.Source.Bb.Gnss.Svid.Beidou.Nmessage.Dnav.Ephemeris.Health.set method RsSmbv.Source.Bb.Gnss.Svid.Glonass.Nmessage.Nav.Ephemeris.Health.set method RsSmbv.Source.Bb.Gnss.Svid.Qzss.Nmessage.Nav.Ephemeris.Health.set The values are interdependent; changing one of them changes the other."""
		satelliteSvid_cmd_val = self._base.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:SBAS:HEALthy?')
		return Conversions.str_to_bool(response)
