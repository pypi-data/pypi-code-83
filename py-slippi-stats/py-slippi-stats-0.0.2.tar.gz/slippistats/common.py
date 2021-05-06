import re

from enum import Enum
from typing import List, Tuple, Union, Optional, Callable, Iterable

number = Union[int, float]

# lodash simulated functions

def identity(x):
    return x

def tofunc(iteratee: Union[int, str, Callable]) -> Callable:
    if callable(iteratee):
        return iteratee
    def ev(x):
        try:
            return x[iteratee]
        except:
            return getattr(x, iteratee)
    return ev

def groupBy(collection: Iterable, iteratee: Union[int, str, Callable] = identity) -> dict:
    func = tofunc(iteratee)
    output = dict()
    if isinstance(collection, (list, tuple)):
        for element in collection:
            key = func(element)
            output[key] = output.get(key, []) + [element]
    else:
        for _, value in collection.items():
            key = func(value)
            output[key] = output.get(key, []) + [value]
    return output

def keyBy(collection: Iterable, iteratee: Union[int, str, Callable] = identity) -> dict:
    func = tofunc(iteratee)
    output = dict()
    for element in collection:
        output[func(element)] = element
    return output

def orderBy(collection: Iterable, iteratee: Union[int, str, Callable] = identity, reverse: bool = False) -> list:
    func = tofunc(iteratee)
    collection = collection.values() if isinstance(collection, dict) else collection
    return sorted(collection, key=func, reverse=reverse)

def mapValues(object: Iterable, iteratee: Union[int, str, Callable] = identity) -> dict:
    func = tofunc(iteratee)
    output = dict()
    for key, value in object.items():
        output[key] = func(value)
    return output


# extra
def _indent(s):
    return re.sub(r'^', '    ', s, flags=re.MULTILINE)


def _format_collection(coll, delim_open, delim_close):
    elements = [_format(x) for x in coll]
    if elements and '\n' in elements[0]:
        return delim_open + '\n' + ',\n'.join(_indent(e) for e in elements) + delim_close
    else:
        return delim_open + ', '.join(elements) + delim_close


def _format(obj):
    if isinstance(obj, float):
        return '%.02f' % obj
    elif isinstance(obj, tuple):
        return _format_collection(obj, '(', ')')
    elif obj.__class__ == list:
        return _format_collection(obj, '[', ']')
    elif isinstance(obj, Enum):
        return repr(obj)
    else:
        return str(obj)


class Base:

    def _is_long(self) -> bool:
        return False

    def _attr_repr(self, attr):
        return attr + '=' + _format(getattr(self, attr))

    def _attr_repr(self, attr):
        self_attr = getattr(self, attr)
        if isinstance(self_attr, list) and hasattr(self_attr, '_is_long') and self_attr._is_long():
            return '%s=[...](%d)' % (attr, len(self_attr))
        elif isinstance(self_attr, dict) and hasattr(self_attr, '_is_long') and self_attr._is_long():
            return '%s={...}(%d)' % (attr, len(self_attr))
        elif attr == 'metadata_raw':
            return None
        else:
            return attr + '=' + _format(self_attr)

    def __repr__(self):
        attrs = []
        for attr in dir(self):
            # uppercase names are nested classes
            if not (attr.startswith('_') or attr[0].isupper() or callable(getattr(self, attr))):
                s = self._attr_repr(attr)
                if s:
                    attrs.append(_indent(s))

        return '%s(\n%s)' % (self.__class__.__name__, ',\n'.join(attrs))


#export
#interface
class PlayerIndexedType(Base, list):

    def __init__(
        self,
        playerIndex: number,
        opponentIndex: number,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.playerIndex = playerIndex
        self.opponentIndex = opponentIndex
        self.append(playerIndex)
        self.append(opponentIndex)

    def __hash__(self):
        return hash((self.playerIndex, self.opponentIndex))

    def __eq__(self, other):
        return (self.playerIndex == other.playerIndex) and (self.opponentIndex == other.opponentIndex)


#export
#interface
class DurationType(Base):
    def __init__(
        self,
        startFrame: number,
        endFrame: Optional[number],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.startFrame = startFrame
        self.endFrame = endFrame

#export
#interface
class DamageType(Base):
    def __init__(
        self,
        startPercent: number,
        currentPercent: number,
        endPercent: Optional[number],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.startPercent = startPercent
        self.currentPercent = currentPercent
        self.endPercent = endPercent

#export
#interface
#extends parents
class StockType(PlayerIndexedType, DurationType, DamageType):
    def __init__(
        self,
        count: number,
        deathAnimation: Optional[number],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.count = count
        self.deathAnimation = deathAnimation

#export
#interface
class MoveLandedType(Base):
    def __init__(
        self,
        frame: number,
        moveId: number,
        hitCount: number,
        damage: number,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.frame = frame
        self.moveId = moveId
        self.hitCount = hitCount
        self.damage = damage

#export
#interface
class RatioType(Base):
    def __init__(
        self,
        count: number,
        total: number,
        ratio: Optional[number],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.count = count
        self.total = total
        self.ratio = ratio

#export
#interface
class InputCountsType(Base):
    def __init__(
        self,
        buttons: number,
        triggers: number,
        joystick: number,
        cstick: number,
        total: number,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.buttons = buttons
        self.triggers = triggers
        self.joystick = joystick
        self.cstick = cstick
        self.total = total

#export
#interface
#extends parents
class ConversionType(PlayerIndexedType, DurationType, DamageType):
    def __init__(
        self,
        moves: List[MoveLandedType],
        openingType: str,
        didKill: bool,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.moves = moves
        self.openingType = openingType
        self.didKill = didKill

#export
#interface
#extends parents
class ComboType(PlayerIndexedType, DurationType, DamageType):
    def __init__(
        self,
        moves: List[MoveLandedType],
        didKill: bool,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.moves = moves
        self.didKill = didKill

#export
#interface
#extends parents
class ActionCountsType(PlayerIndexedType):
    def __init__(
        self,
        wavedashCount: number,
        wavelandCount: number,
        airDodgeCount: number,
        dashDanceCount: number,
        spotDodgeCount: number,
        ledgegrabCount: number,
        rollCount: number,
        lCancelSuccessCount: number,
        lCancelFailCount: number,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.wavedashCount = wavedashCount
        self.wavelandCount = wavelandCount
        self.airDodgeCount = airDodgeCount
        self.dashDanceCount = dashDanceCount
        self.spotDodgeCount = spotDodgeCount
        self.ledgegrabCount = ledgegrabCount
        self.rollCount = rollCount
        self.lCancelSuccessCount = lCancelSuccessCount
        self.lCancelFailCount = lCancelFailCount

#export
#interface
#extends parents
class OverallType(PlayerIndexedType):
    def __init__(
        self,
        inputCounts: InputCountsType,
        conversionCount: number,
        totalDamage: number,
        killCount: number,
        successfulConversions: RatioType,
        inputsPerMinute: RatioType,
        digitalInputsPerMinute: RatioType,
        openingsPerKill: RatioType,
        damagePerOpening: RatioType,
        neutralWinRatio: RatioType,
        counterHitRatio: RatioType,
        beneficialTradeRatio: RatioType,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.inputCounts = inputCounts
        self.conversionCount = conversionCount
        self.totalDamage = totalDamage
        self.killCount = killCount
        self.successfulConversions = successfulConversions
        self.inputsPerMinute = inputsPerMinute
        self.digitalInputsPerMinute = digitalInputsPerMinute
        self.openingsPerKill = openingsPerKill
        self.damagePerOpening = damagePerOpening
        self.neutralWinRatio = neutralWinRatio
        self.counterHitRatio = counterHitRatio
        self.beneficialTradeRatio = beneficialTradeRatio

#export
#interface
class StatsType(Base):
    def __init__(
        self,
        gameComplete: bool,
        lastFrame: number,
        playableFrameCount: number,
        stocks: List[StockType],
        conversions: List[ConversionType],
        combos: List[ComboType],
        actionCounts: List[ActionCountsType],
        overall: List[OverallType],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.gameComplete = gameComplete
        self.lastFrame = lastFrame
        self.playableFrameCount = playableFrameCount
        self.stocks = stocks
        self.conversions = conversions
        self.combos = combos
        self.actionCounts = actionCounts
        self.overall = overall

#export
#enum
class State(Enum):
    # Animation ID ranges
    DAMAGE_START = 0x4b
    DAMAGE_END = 0x5b
    CAPTURE_START = 0xdf
    CAPTURE_END = 0xe8
    GUARD_START = 0xb2
    GUARD_END = 0xb6
    GROUNDED_CONTROL_START = 0xe
    GROUNDED_CONTROL_END = 0x18
    SQUAT_START = 0x27
    SQUAT_END = 0x29
    DOWN_START = 0xb7
    DOWN_END = 0xc6
    TECH_START = 0xc7
    TECH_END = 0xcc
    DYING_START = 0x0
    DYING_END = 0xa
    CONTROLLED_JUMP_START = 0x18
    CONTROLLED_JUMP_END = 0x22
    GROUND_ATTACK_START = 0x2c
    GROUND_ATTACK_END = 0x40
    AERIAL_ATTACK_START = 0x41
    AERIAL_ATTACK_END = 0x4a

    # Animation ID specific
    ROLL_FORWARD = 0xe9
    ROLL_BACKWARD = 0xea
    SPOT_DODGE = 0xeb
    AIR_DODGE = 0xec
    ACTION_WAIT = 0xe
    ACTION_DASH = 0x14
    ACTION_KNEE_BEND = 0x18
    GUARD_ON = 0xb2
    TECH_MISS_UP = 0xb7
    TECH_MISS_DOWN = 0xbf
    DASH = 0x14
    TURN = 0x12
    LANDING_FALL_SPECIAL = 0x2b
    JUMP_FORWARD = 0x19
    JUMP_BACKWARD = 0x1a
    FALL_FORWARD = 0x1e
    FALL_BACKWARD = 0x1f
    GRAB = 0xd4
    CLIFF_CATCH = 0xfc


#export
class Timers(Enum): #const
    PUNISH_RESET_FRAMES = 45
    RECOVERY_RESET_FRAMES = 45
    COMBO_STRING_RESET_FRAMES = 45

#export
def getSinglesPlayerPermutationsFromSettings(settings: 'GameStartType') -> List[PlayerIndexedType]:
    if not settings or len(settings.players) != 2:
        # Only return opponent indices for singles
        return []

    return [
        PlayerIndexedType(
            playerIndex=settings.players[0].playerIndex,
            opponentIndex=settings.players[1].playerIndex,
        ),
        PlayerIndexedType(
            playerIndex=settings.players[1].playerIndex,
            opponentIndex=settings.players[0].playerIndex,
        ),
    ]


#export
def didLoseStock(frame: 'PostFrameUpdateType', prevFrame: 'PostFrameUpdateType') -> bool:
    if not frame or not prevFrame:
        return False

    return prevFrame.stocksRemaining - frame.stocksRemaining > 0


#export
def isInControl(state: number) -> bool:
    ground = state >= State.GROUNDED_CONTROL_START.value and state <= State.GROUNDED_CONTROL_END.value #const
    squat = state >= State.SQUAT_START.value and state <= State.SQUAT_END.value #const
    groundAttack = state > State.GROUND_ATTACK_START.value and state <= State.GROUND_ATTACK_END.value #const
    isGrab = state == State.GRAB.value #const
    # TODO: Add grounded b moves
    return ground or squat or groundAttack or isGrab


#export
def isTeching(state: number) -> bool:
    return state >= State.TECH_START.value and state <= State.TECH_END.value


#export
def isDown(state: number) -> bool:
    return state >= State.DOWN_START.value and state <= State.DOWN_END.value


#export
def isDamaged(state: number) -> bool:
    return state >= State.DAMAGE_START.value and state <= State.DAMAGE_END.value


#export
def isGrabbed(state: number) -> bool:
    return state >= State.CAPTURE_START.value and state <= State.CAPTURE_END.value


#export
def isDead(state: number) -> bool:
    return state >= State.DYING_START.value and state <= State.DYING_END.value


#export
def calcDamageTaken(frame: 'PostFrameUpdateType', prevFrame: 'PostFrameUpdateType') -> number:
    percent = frame.percent if frame and frame.percent else 0 #const
    prevPercent = prevFrame.percent if prevFrame and prevFrame.percent else 0 #const
    return percent - prevPercent

