from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Log:
	"""Log commands group definition. 9 total commands, 7 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("log", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Log_.Mode import Mode
			self._mode = Mode(self._core, self._base)
		return self._mode

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Log_.Count import Count
			self._count = Count(self._core, self._base)
		return self._count

	@property
	def duration(self):
		"""duration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duration'):
			from .Log_.Duration import Duration
			self._duration = Duration(self._core, self._base)
		return self._duration

	@property
	def interval(self):
		"""interval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_interval'):
			from .Log_.Interval import Interval
			self._interval = Interval(self._core, self._base)
		return self._interval

	@property
	def fname(self):
		"""fname commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fname'):
			from .Log_.Fname import Fname
			self._fname = Fname(self._core, self._base)
		return self._fname

	@property
	def stime(self):
		"""stime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stime'):
			from .Log_.Stime import Stime
			self._stime = Stime(self._core, self._base)
		return self._stime

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Log_.Channel import Channel
			self._channel = Channel(self._core, self._base)
		return self._channel

	def get_state(self) -> bool:
		"""SCPI: LOG[:STATe] \n
		Snippet: value: bool = driver.log.get_state() \n
		Sets or queries the data logging state. \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('LOG:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, arg_0: bool) -> None:
		"""SCPI: LOG[:STATe] \n
		Snippet: driver.log.set_state(arg_0 = False) \n
		Sets or queries the data logging state. \n
			:param arg_0: 1 Data logging function is enabled. 0 Data logging function is disabled.
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'LOG:STATe {param}')

	def get_triggered(self) -> bool:
		"""SCPI: LOG:TRIGgered \n
		Snippet: value: bool = driver.log.get_triggered() \n
		Sets or queries the state for manual trigger logging function. \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('LOG:TRIGgered?')
		return Conversions.str_to_bool(response)

	def set_triggered(self, arg_0: bool) -> None:
		"""SCPI: LOG:TRIGgered \n
		Snippet: driver.log.set_triggered(arg_0 = False) \n
		Sets or queries the state for manual trigger logging function. \n
			:param arg_0: 0 Manual trigger function is disabled. 1 Manual trigger function is enabled.
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'LOG:TRIGgered {param}')
