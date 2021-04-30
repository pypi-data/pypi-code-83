from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sensitivity:
	"""Sensitivity commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sensitivity", core, parent)

	@property
	def exponential(self):
		"""exponential commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_exponential'):
			from .Sensitivity_.Exponential import Exponential
			self._exponential = Exponential(self._core, self._base)
		return self._exponential

	@property
	def linear(self):
		"""linear commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_linear'):
			from .Sensitivity_.Linear import Linear
			self._linear = Linear(self._core, self._base)
		return self._linear

	def clone(self) -> 'Sensitivity':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sensitivity(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
