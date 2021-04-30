from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mbeacon:
	"""Mbeacon commands group definition. 17 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("mbeacon", core, parent)

	@property
	def comid(self):
		"""comid commands group. 1 Sub-classes, 9 commands."""
		if not hasattr(self, '_comid'):
			from .Mbeacon_.Comid import Comid
			self._comid = Comid(self._core, self._base)
		return self._comid

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Mbeacon_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	@property
	def marker(self):
		"""marker commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_marker'):
			from .Mbeacon_.Marker import Marker
			self._marker = Marker(self._core, self._base)
		return self._marker

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:[ILS]:MBEacon:PRESet \n
		Snippet: driver.source.ils.mbeacon.preset() \n
		Sets the parameters of the ILS marker beacons component to their default values (*RST values specified for the commands) .
		For other ILS preset commands, see method RsSmab.Source.Ils.preset. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:ILS:MBEacon:PRESet')

	def preset_with_opc(self) -> None:
		"""SCPI: [SOURce<HW>]:[ILS]:MBEacon:PRESet \n
		Snippet: driver.source.ils.mbeacon.preset_with_opc() \n
		Sets the parameters of the ILS marker beacons component to their default values (*RST values specified for the commands) .
		For other ILS preset commands, see method RsSmab.Source.Ils.preset. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmab.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:ILS:MBEacon:PRESet')

	def clone(self) -> 'Mbeacon':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mbeacon(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
