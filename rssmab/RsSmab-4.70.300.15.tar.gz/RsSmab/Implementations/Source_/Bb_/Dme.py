from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dme:
	"""Dme commands group definition. 6 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dme", core, parent)

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_setting'):
			from .Dme_.Setting import Setting
			self._setting = Setting(self._core, self._base)
		return self._setting

	@property
	def gaussian(self):
		"""gaussian commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gaussian'):
			from .Dme_.Gaussian import Gaussian
			self._gaussian = Gaussian(self._core, self._base)
		return self._gaussian

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:DME:PRESet \n
		Snippet: driver.source.bb.dme.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:DME:PRESet')

	def preset_with_opc(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:DME:PRESet \n
		Snippet: driver.source.bb.dme.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmab.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:DME:PRESet')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:DME:STATe \n
		Snippet: value: bool = driver.source.bb.dme.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DME:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:DME:STATe \n
		Snippet: driver.source.bb.dme.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:DME:STATe {param}')

	def clone(self) -> 'Dme':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dme(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
