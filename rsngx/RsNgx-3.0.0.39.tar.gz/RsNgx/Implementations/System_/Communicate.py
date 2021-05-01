from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Communicate:
	"""Communicate commands group definition. 10 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("communicate", core, parent)

	@property
	def lan(self):
		"""lan commands group. 2 Sub-classes, 8 commands."""
		if not hasattr(self, '_lan'):
			from .Communicate_.Lan import Lan
			self._lan = Lan(self._core, self._base)
		return self._lan
