from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reference:
	"""Reference commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("reference", core, parent)

	def set(self) -> None:
		"""SCPI: CSYNthesis:PHASe:REFerence \n
		Snippet: driver.csynthesis.phase.reference.set() \n
		Resets the delta phase value. \n
		"""
		self._core.io.write(f'CSYNthesis:PHASe:REFerence')

	def set_with_opc(self) -> None:
		"""SCPI: CSYNthesis:PHASe:REFerence \n
		Snippet: driver.csynthesis.phase.reference.set_with_opc() \n
		Resets the delta phase value. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsSmab.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CSYNthesis:PHASe:REFerence')
