from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IodNav:
	"""IodNav commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iodNav", core, parent)

	def set(self, io_dnav: int, satelliteSvid=repcap.SatelliteSvid.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:NMESsage:FNAV:EPHemeris:IODNav \n
		Snippet: driver.source.bb.gnss.svid.galileo.nmessage.fnav.ephemeris.iodNav.set(io_dnav = 1, satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the IODnav parameter. \n
			:param io_dnav: integer Range: 0 to 1023
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')"""
		param = Conversions.decimal_value_to_str(io_dnav)
		satelliteSvid_cmd_val = self._base.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		self._core.io.write(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:NMESsage:FNAV:EPHemeris:IODNav {param}')

	def get(self, satelliteSvid=repcap.SatelliteSvid.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:GNSS:SVID<CH>:GALileo:NMESsage:FNAV:EPHemeris:IODNav \n
		Snippet: value: int = driver.source.bb.gnss.svid.galileo.nmessage.fnav.ephemeris.iodNav.get(satelliteSvid = repcap.SatelliteSvid.Default) \n
		Sets the IODnav parameter. \n
			:param satelliteSvid: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Svid')
			:return: io_dnav: integer Range: 0 to 1023"""
		satelliteSvid_cmd_val = self._base.get_repcap_cmd_value(satelliteSvid, repcap.SatelliteSvid)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:GNSS:SVID{satelliteSvid_cmd_val}:GALileo:NMESsage:FNAV:EPHemeris:IODNav?')
		return Conversions.str_to_int(response)
