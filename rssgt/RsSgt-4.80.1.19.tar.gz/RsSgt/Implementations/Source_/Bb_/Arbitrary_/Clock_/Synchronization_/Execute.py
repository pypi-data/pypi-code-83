from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Execute:
	"""Execute commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("execute", core, parent)

	def set(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CLOCk:SYNChronization:EXECute \n
		Snippet: driver.source.bb.arbitrary.clock.synchronization.execute.set() \n
		Performs automatically adjustment of the instrument's settings required for the synchronization mode, set with the
		command method RsSgt.Source.Bb.Arbitrary.Clock.Synchronization.mode. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CLOCk:SYNChronization:EXECute')

	def set_with_opc(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CLOCk:SYNChronization:EXECute \n
		Snippet: driver.source.bb.arbitrary.clock.synchronization.execute.set_with_opc() \n
		Performs automatically adjustment of the instrument's settings required for the synchronization mode, set with the
		command method RsSgt.Source.Bb.Arbitrary.Clock.Synchronization.mode. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSgt.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:ARBitrary:CLOCk:SYNChronization:EXECute')
