from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Transition:
	"""Transition commands group definition. 12 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("transition", core, parent)

	@property
	def negative(self):
		"""negative commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_negative'):
			from .Transition_.Negative import Negative
			self._negative = Negative(self._core, self._base)
		return self._negative

	@property
	def positive(self):
		"""positive commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_positive'):
			from .Transition_.Positive import Positive
			self._positive = Positive(self._core, self._base)
		return self._positive

	def clone(self) -> 'Transition':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Transition(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
