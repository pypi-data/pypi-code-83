from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pulse:
	"""Pulse commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pulse", core, parent)

	@property
	def base(self):
		"""base commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_base'):
			from .Pulse_.Base import Base
			self._base = Base(self._core, self._base)
		return self._base

	@property
	def top(self):
		"""top commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_top'):
			from .Pulse_.Top import Top
			self._top = Top(self._core, self._base)
		return self._top

	def clone(self) -> 'Pulse':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pulse(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
