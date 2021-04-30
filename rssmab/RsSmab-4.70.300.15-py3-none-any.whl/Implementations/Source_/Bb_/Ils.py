from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ils:
	"""Ils commands group definition. 5 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ils", core, parent)

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_setting'):
			from .Ils_.Setting import Setting
			self._setting = Setting(self._core, self._base)
		return self._setting

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:[BB]:ILS:PRESet \n
		Snippet: driver.source.bb.ils.preset() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command method RsSmab.Source.Vor.state. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:ILS:PRESet')

	def preset_with_opc(self) -> None:
		"""SCPI: [SOURce<HW>]:[BB]:ILS:PRESet \n
		Snippet: driver.source.bb.ils.preset_with_opc() \n
		Sets the parameters of the digital standard to their default values (*RST values specified for the commands) .
		Not affected is the state set with the command method RsSmab.Source.Vor.state. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmab.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:ILS:PRESet')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:[BB]:ILS:STATe \n
		Snippet: value: bool = driver.source.bb.ils.get_state() \n
		Activates/deactivates the VOR modulation. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ILS:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:[BB]:ILS:STATe \n
		Snippet: driver.source.bb.ils.set_state(state = False) \n
		Activates/deactivates the VOR modulation. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ILS:STATe {param}')

	def clone(self) -> 'Ils':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ils(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
