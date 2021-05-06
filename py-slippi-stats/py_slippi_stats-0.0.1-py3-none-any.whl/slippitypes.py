
from .common import Base

from enum import Enum
from typing import Dict, List, Optional, Union

number = Union[int, float]

#export
#enum
class Command(Enum):
    MESSAGE_SIZES = 0x35
    GAME_START = 0x36
    PRE_FRAME_UPDATE = 0x37
    POST_FRAME_UPDATE = 0x38
    GAME_END = 0x39
    ITEM_UPDATE = 0x3b
    FRAME_BOOKEND = 0x3c


#export
#interface
class PlayerType(Base):

    def __init__(
        self,
        playerIndex: number,
        port: number,
        characterId: Optional[number],
        characterColor: Optional[number],
        startStocks: Optional[number],
        type: Optional[number],
        teamId: Optional[number],
        controllerFix: Optional[str],
        nametag: Optional[str],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.playerIndex = playerIndex
        self.port = port
        self.characterId = characterId
        self.characterColor = characterColor
        self.startStocks = startStocks
        self.type = type
        self.teamId = teamId
        self.controllerFix = controllerFix
        self.nametag = nametag


#export
#enum
class GameMode(Enum):
    VS = 0x02,
    ONLINE = 0x08,


#export
#interface
class GameStartType(Base):
    def __init__(
        self,
        slpVersion: Optional[str],
        isTeams: Optional[bool],
        isPAL: Optional[bool],
        stageId: Optional[number],
        players: List[PlayerType],
        scene: Optional[number],
        gameMode: Optional[GameMode],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.slpVersion = slpVersion
        self.isTeams = isTeams
        self.isPAL = isPAL
        self.stageId = stageId
        self.players = players
        self.scene = scene
        self.gameMode = gameMode


#export
#interface
class PreFrameUpdateType(Base):
    def __init__(
        self,
        frame: Optional[number],
        playerIndex: Optional[number],
        isFollower: Optional[bool],
        seed: Optional[number],
        actionStateId: Optional[number],
        positionX: Optional[number],
        positionY: Optional[number],
        facingDirection: Optional[number],
        joystickX: Optional[number],
        joystickY: Optional[number],
        cStickX: Optional[number],
        cStickY: Optional[number],
        trigger: Optional[number],
        buttons: Optional[number],
        physicalButtons: Optional[number],
        physicalLTrigger: Optional[number],
        physicalRTrigger: Optional[number],
        percent: Optional[number],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.frame = frame
        self.playerIndex = playerIndex
        self.isFollower = isFollower
        self.seed = seed
        self.actionStateId = actionStateId
        self.positionX = positionX
        self.positionY = positionY
        self.facingDirection = facingDirection
        self.joystickX = joystickX
        self.joystickY = joystickY
        self.cStickX = cStickX
        self.cStickY = cStickY
        self.trigger = trigger
        self.buttons = buttons
        self.physicalButtons = physicalButtons
        self.physicalLTrigger = physicalLTrigger
        self.physicalRTrigger = physicalRTrigger
        self.percent = percent


#export
#interface
class SelfInducedSpeedsType(Base):
    def __init__(
        self,
        airX: Optional[number],
        y: Optional[number],
        attackX: Optional[number],
        attackY: Optional[number],
        groundX: Optional[number],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.airX = airX
        self.y = y
        self.attackX = attackX
        self.attackY = attackY
        self.groundX = groundX


#export
#interface
class PostFrameUpdateType(Base):
    def __init__(
        self,
        frame: Optional[number],
        playerIndex: Optional[number],
        isFollower: Optional[bool],
        internalCharacterId: Optional[number],
        actionStateId: Optional[number],
        positionX: Optional[number],
        positionY: Optional[number],
        facingDirection: Optional[number],
        percent: Optional[number],
        shieldSize: Optional[number],
        lastAttackLanded: Optional[number],
        currentComboCount: Optional[number],
        lastHitBy: Optional[number],
        stocksRemaining: Optional[number],
        actionStateCounter: Optional[number],
        miscActionState: Optional[number],
        isAirborne: Optional[bool],
        lastGroundId: Optional[number],
        jumpsRemaining: Optional[number],
        lCancelStatus: Optional[number],
        hurtboxCollisionState: Optional[number],
        selfInducedSpeeds: Optional[SelfInducedSpeedsType],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.frame = frame
        self.playerIndex = playerIndex
        self.isFollower = isFollower
        self.internalCharacterId = internalCharacterId
        self.actionStateId = actionStateId
        self.positionX = positionX
        self.positionY = positionY
        self.facingDirection = facingDirection
        self.percent = percent
        self.shieldSize = shieldSize
        self.lastAttackLanded = lastAttackLanded
        self.currentComboCount = currentComboCount
        self.lastHitBy = lastHitBy
        self.stocksRemaining = stocksRemaining
        self.actionStateCounter = actionStateCounter
        self.miscActionState = miscActionState
        self.isAirborne = isAirborne
        self.lastGroundId = lastGroundId
        self.jumpsRemaining = jumpsRemaining
        self.lCancelStatus = lCancelStatus
        self.hurtboxCollisionState = hurtboxCollisionState
        self.selfInducedSpeeds = selfInducedSpeeds


#export
#interface
class ItemUpdateType(Base):
    def __init__(
        self,
        frame: Optional[number],
        typeId: Optional[number],
        state: Optional[number],
        facingDirection: Optional[number],
        velocityX: Optional[number],
        velocityY: Optional[number],
        positionX: Optional[number],
        positionY: Optional[number],
        damageTaken: Optional[number],
        expirationTimer: Optional[number],
        spawnId: Optional[number],
        missileType: Optional[number],
        turnipFace: Optional[number],
        chargeShotLaunched: Optional[number],
        chargePower: Optional[number],
        owner: Optional[number],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.frame = frame
        self.typeId = typeId
        self.state = state
        self.facingDirection = facingDirection
        self.velocityX = velocityX
        self.velocityY = velocityY
        self.positionX = positionX
        self.positionY = positionY
        self.damageTaken = damageTaken
        self.expirationTimer = expirationTimer
        self.spawnId = spawnId
        self.missileType = missileType
        self.turnipFace = turnipFace
        self.chargeShotLaunched = chargeShotLaunched
        self.chargePower = chargePower
        self.owner = owner


#export
#interface
class FrameBookendType(Base):
    def __init__(
        self,
        frame: Optional[number],
        latestFinalizedFrame: Optional[number],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.frame = frame
        self.latestFinalizedFrame = latestFinalizedFrame


#export
#interface
class GameEndType(Base):
    def __init__(
        self,
        gameEndMethod: Optional[number],
        lrasInitiatorIndex: Optional[number],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.gameEndMethod = gameEndMethod
        self.lrasInitiatorIndex = lrasInitiatorIndex


# extra
class MetadataCharactersType(dict):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        for characterId, metadataCharacterId in self.items():
            if not isinstance(characterId, int):
                raise ValueError('characterId is not int in MetadataCharactersType construct')
            if not isinstance(metadataCharacterId, int):
                raise ValueError('metadataCharacterId is not int in MetadataCharactersType construct')

    def __setitem__(self, key, val):
        if not isinstance(key, int):
            raise ValueError('characterId is not int in MetadataCharactersType construct')
        if not isinstance(val, int):
            raise ValueError('metadataCharacterId is not int in MetadataCharactersType construct')
        dict.__setitem__(self, key, val)


# extra
class MetadataNamesType(Base):
    def __init__(self, netplay: str, code: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.netplay = netplay
        self.code = code


# extra
class MetadataPlayerType(Base):
    def __init__(
        self,
        characters: MetadataCharactersType,
        names: MetadataNamesType,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.characters = characters
        self.names = names


#export
#interface
class MetadataType(Base):
    def __init__(
        self,
        startAt: Optional[str],
        playedOn: Optional[str],
        lastFrame: Optional[number],
        players: Dict[
            int, # playerIndex
            MetadataPlayerType],
        consoleNick: Optional[str],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.startAt = startAt
        self.playedOn = playedOn
        self.lastFrame = lastFrame
        self.players = players
        self.consoleNick = consoleNick


#export
EventPayloadTypes = Union[
    GameStartType,
    PreFrameUpdateType,
    PostFrameUpdateType,
    ItemUpdateType,
    FrameBookendType,
    GameEndType
]

#export
# type EventCallbackFunc = (command: Command, payload: Optional[EventPayloadTypes]) => bool


# extra
class FrameUpdateType(Base):
    def __init__(self, pre: PreFrameUpdateType, post: PostFrameUpdateType, **kwargs):
        super().__init__(**kwargs)
        self.pre = pre
        self.post = post


#export
#interface
class FrameEntryType(Base):
    def __init__(
        self,
        frame: number,
        players: Dict[
            number, # playerIndex
            FrameUpdateType
        ],
        followers: Dict[
            number, # playerIndex
            FrameUpdateType
        ],
        items: List[ItemUpdateType],
        **kwargs
    ) -> None:
        self.frame = frame
        self.players = players
        self.followers = followers
        self.items = items


#export
#enum
class Frames(Enum):
    FIRST = -123
    FIRST_PLAYABLE = -39


#export
#interface
class FramesType(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for frameIndex, frameEntryType in self.items():
            if not isinstance(frameIndex, int):
                raise ValueError('frameIndex is not int in FramesType construct')
            if not isinstance(frameEntryType, FrameEntryType):
                raise ValueError('frameEntryType is not int in FrameEntryType construct')

    def __setitem__(self, key, val):
        if not isinstance(key, int):
            raise ValueError('frameIndex is not int in FramesType construct')
        if not isinstance(val, FrameEntryType):
            raise ValueError('frameEntryType is not int in FrameEntryType construct')
        dict.__setitem__(self, key, val)

    def _is_long(self) -> bool:
        return True