from enum import Enum


# noinspection SpellCheckingInspection
class ArbEndBehavior(Enum):
	"""2 Members, HOLD ... OFF"""
	HOLD = 0
	OFF = 1


# noinspection SpellCheckingInspection
class ArbTrigMode(Enum):
	"""2 Members, RUN ... SINGle"""
	RUN = 0
	SINGle = 1


# noinspection SpellCheckingInspection
class DioFaultSource(Enum):
	"""6 Members, CC ... SINK"""
	CC = 0
	CR = 1
	CV = 2
	OUTPut = 3
	PROTection = 4
	SINK = 5


# noinspection SpellCheckingInspection
class DioOutSource(Enum):
	"""3 Members, FORCed ... TRIGger"""
	FORCed = 0
	OUTPut = 1
	TRIGger = 2


# noinspection SpellCheckingInspection
class DioSignal(Enum):
	"""2 Members, CONStant ... PULSe"""
	CONStant = 0
	PULSe = 1


# noinspection SpellCheckingInspection
class FastLogSampleRate(Enum):
	"""6 Members, S001k ... S500k"""
	S001k = 0
	S010k = 1
	S050k = 2
	S100 = 3
	S250k = 4
	S500k = 5


# noinspection SpellCheckingInspection
class FastLogTarget(Enum):
	"""2 Members, SCPI ... USB"""
	SCPI = 0
	USB = 1


# noinspection SpellCheckingInspection
class FileName(Enum):
	"""3 Members, DEF ... INT"""
	DEF = 0
	EXT = 1
	INT = 2


# noinspection SpellCheckingInspection
class HcpyFormat(Enum):
	"""2 Members, BMP ... PNG"""
	BMP = 0
	PNG = 1


# noinspection SpellCheckingInspection
class LogMode(Enum):
	"""4 Members, COUNt ... UNLimited"""
	COUNt = 0
	DURation = 1
	SPAN = 2
	UNLimited = 3


# noinspection SpellCheckingInspection
class MinOrMax(Enum):
	"""4 Members, MAX ... MINimum"""
	MAX = 0
	MAXimum = 1
	MIN = 2
	MINimum = 3


# noinspection SpellCheckingInspection
class OptDfltStep(Enum):
	"""1 Members, DEFault ... DEFault"""
	DEFault = 0


# noinspection SpellCheckingInspection
class PrioMode(Enum):
	"""2 Members, CPM ... VPM"""
	CPM = 0
	VPM = 1


# noinspection SpellCheckingInspection
class TriggerDioSource(Enum):
	"""2 Members, EXT ... IN"""
	EXT = 0
	IN = 1


# noinspection SpellCheckingInspection
class TriggerOperMode(Enum):
	"""5 Members, CC ... SINK"""
	CC = 0
	CR = 1
	CV = 2
	PROTection = 3
	SINK = 4


# noinspection SpellCheckingInspection
class TriggerSource(Enum):
	"""3 Members, DIO ... OUTPut"""
	DIO = 0
	OMODe = 1
	OUTPut = 2


# noinspection SpellCheckingInspection
class UsbClass(Enum):
	"""2 Members, CDC ... TMC"""
	CDC = 0
	TMC = 1
