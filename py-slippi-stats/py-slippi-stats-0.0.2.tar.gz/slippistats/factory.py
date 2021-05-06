from .slippitypes import GameEndType, PreFrameUpdateType, PostFrameUpdateType, FrameUpdateType, ItemUpdateType, FrameEntryType, FramesType, MetadataCharactersType, MetadataNamesType, MetadataPlayerType, MetadataType, GameStartType, PlayerType

from typing import List


class GameEndTypeFactory:

    def __init__(self, game_end: 'End') -> None:
        self.gameEndMethod = game_end.method.value
        self.lrasInitiatorIndex = game_end.lras_initiator

    def generate_object(self) -> GameEndType:
        return GameEndType(
            gameEndMethod=self.gameEndMethod,
            lrasInitiatorIndex=self.lrasInitiatorIndex)


class PreFrameUpdateTypeFactory:

    def __init__(self, frame: 'Frame', port_id: int, isFollower: bool = False) -> None:
        port = frame.ports[port_id]
        entity = port.follower.pre if isFollower else port.leader.pre
        self.frame = frame.index
        self.playerIndex = port_id
        self.isFollower = isFollower
        self.seed = entity.random_seed
        self.actionStateId = entity.state
        self.positionX = entity.position.x
        self.positionY = entity.position.y
        self.facingDirection = entity.direction.value
        self.joystickX = entity.joystick.x
        self.joystickY = entity.joystick.y
        self.cStickX = entity.cstick.x
        self.cStickY = entity.cstick.y
        self.trigger = entity.triggers.logical
        self.buttons = entity.buttons.logical
        self.physicalButtons = entity.buttons.physical
        self.physicalLTrigger = entity.triggers.physical.l
        self.physicalRTrigger = entity.triggers.physical.r
        self.percent = float(entity.damage[0] if isinstance(entity.damage, (list, tuple)) else entity.damage)

    def generate_object(self) -> PreFrameUpdateType:
        return PreFrameUpdateType(
            frame = self.frame,
            playerIndex = self.playerIndex,
            isFollower = self.isFollower,
            seed = self.seed,
            actionStateId = self.actionStateId,
            positionX = self.positionX,
            positionY = self.positionY,
            facingDirection = self.facingDirection,
            joystickX = self.joystickX,
            joystickY = self.joystickY,
            cStickX = self.cStickX,
            cStickY = self.cStickY,
            trigger = self.trigger,
            buttons = self.buttons,
            physicalButtons = self.physicalButtons,
            physicalLTrigger = self.physicalLTrigger,
            physicalRTrigger = self.physicalRTrigger,
            percent = self.percent)


class PostFrameUpdateTypeFactory:

    def __init__(self, frame: 'Frame', port_id: int, isFollower: bool = False) -> None:
        port = frame.ports[port_id]
        entity = port.follower.post if isFollower else port.leader.post
        self.frame = frame.index
        self.playerIndex = port_id
        self.isFollower = isFollower
        self.internalCharacterId = entity.character.value
        self.actionStateId = int(entity.state if isinstance(entity.state, int) else entity.state.value)
        self.positionX = entity.position.x
        self.positionY = entity.position.y
        self.facingDirection = entity.direction.value
        self.percent = float(entity.damage[0] if isinstance(entity.damage, (list, tuple)) else entity.damage)
        self.shieldSize = entity.shield
        self.lastAttackLanded = int(entity.last_attack_landed if isinstance(entity.last_attack_landed, int) else entity.last_attack_landed.value) if entity.last_attack_landed else None
        self.currentComboCount = entity.combo_count
        self.lastHitBy = entity.last_hit_by
        self.stocksRemaining = entity.stocks
        self.actionStateCounter = entity.state_age
        self.miscActionState = None #TODO look for correspondence
        self.isAirborne = entity.airborne
        self.lastGroundId = entity.ground #TODO find out if this needs to be corrected
        self.jumpsRemaining = entity.jumps
        self.lCancelStatus = entity.l_cancel
        self.hurtboxCollisionState = None #TODO look for correspondence
        self.selfInducedSpeeds = None #TODO look for correspondence

    def generate_object(self) -> PostFrameUpdateType:
        return PostFrameUpdateType(
            frame = self.frame,
            playerIndex = self.playerIndex,
            isFollower = self.isFollower,
            internalCharacterId = self.internalCharacterId,
            actionStateId = self.actionStateId,
            positionX = self.positionX,
            positionY = self.positionY,
            facingDirection = self.facingDirection,
            percent = self.percent,
            shieldSize = self.shieldSize,
            lastAttackLanded = self.lastAttackLanded,
            currentComboCount = self.currentComboCount,
            lastHitBy = self.lastHitBy,
            stocksRemaining = self.stocksRemaining,
            actionStateCounter = self.actionStateCounter,
            miscActionState = self.miscActionState,
            isAirborne = self.isAirborne,
            lastGroundId = self.lastGroundId,
            jumpsRemaining = self.jumpsRemaining,
            lCancelStatus = self.lCancelStatus,
            hurtboxCollisionState = self.hurtboxCollisionState,
            selfInducedSpeeds = self.selfInducedSpeeds)


class FrameUpdateTypeFactory:

    def __init__(self, frame: 'Frame', port_id: int, isFollower: bool = False) -> None:
        self.pre = PreFrameUpdateTypeFactory(
            frame=frame,
            port_id=port_id,
            isFollower=isFollower)
        self.post = PostFrameUpdateTypeFactory(
            frame=frame,
            port_id=port_id,
            isFollower=isFollower)

    def generate_object(self) -> FrameUpdateType:
        return FrameUpdateType(
            pre = self.pre.generate_object(),
            post = self.post.generate_object()
        )


class FrameEntryTypeFactory:

    def __init__(self, frame: 'Frame'):
        self.frame = frame.index
        self.players = {}
        self.followers = {}
        self.items = []
        for i, port in enumerate(frame.ports):
            if not port:
                continue
            self.players[i] = FrameUpdateTypeFactory(
                frame = frame,
                port_id = i,
                isFollower = False).generate_object()
            if not port.follower:
                self.followers[i] = None
                continue
            self.followers[i] = FrameUpdateTypeFactory(
                frame = frame,
                port_id = i,
                isFollower = True).generate_object()
        for item in frame.items:
            self.items.append(ItemUpdateType(
                frame = frame.index,
                typeId = item.type.value,
                state = item.state,
                facingDirection = item.direction.value,
                velocityX = item.velocity.x,
                velocityY = item.velocity.y,
                positionX = item.position.x,
                positionY = item.position.y,
                damageTaken = item.damage,
                expirationTimer = item.timer,
                spawnId = item.spawn_id,
                missileType = None, #TODO find correspondence
                turnipFace = None, #TODO find correspondence
                chargeShotLaunched = None, #TODO find correspondence
                chargePower = None, #TODO find correspondence
                owner = None, #TODO find correspondence
            ))

    def generate_object(self) -> FrameEntryType:
        return FrameEntryType(
            frame = self.frame,
            players = self.players,
            followers = self.followers,
            items = self.items)


class FramesTypeFactory:

    def __init__(self, frames: List['Frame']) -> None:
        self.frames = {}
        for frame in frames:
            self.frames[frame.index] = FrameEntryTypeFactory(frame)

    def generate_object(self) -> FramesType:
        frames = FramesType()
        for index, factory in self.frames.items():
            frames[index] = factory.generate_object()
        return frames


class MetadataTypeFactory:

    def __init__(self, game_metadata: 'Metadata') -> None:
        self.startAt = game_metadata.date.strftime('%Y-%m-%d %H:%M:%S.%f %Z')
        self.playedOn = game_metadata.platform.value
        self.lastFrame = None #TODO find correspondence
        self.players = {}
        for i, player in enumerate(game_metadata.players):
            if not player:
                continue
            characters = MetadataCharactersType()
            if player.characters:
                for characterkey, charactervalue in player.characters.items():
                    characters[characterkey.value] = charactervalue
            self.players[i] = MetadataPlayerType(
                characters = characters,
                names = MetadataNamesType(
                    netplay = player.netplay.name if player.netplay and player.netplay.name else None,
                    code = player.netplay.code if player.netplay and player.netplay.code else None
                ))
        self.consoleNick = game_metadata.console_name

    def generate_object(self) -> MetadataType:
        return MetadataType(
            startAt = self.startAt,
            playedOn = self.playedOn,
            lastFrame = self.lastFrame,
            players = self.players,
            consoleNick = self.consoleNick)


class GameStartTypeFactory:

    def __init__(self, game_start) -> None:
        self.slpVersion = game_start.slippi.version
        self.isTeams = game_start.is_teams
        self.isPAL = game_start.is_pal
        self.stageId = game_start.stage.value
        self.players = {}
        for i, player in enumerate(game_start.players):
            if not player:
                continue
            self.players[i] = PlayerType(
                playerIndex = i,
                port = i,
                characterId = player.character.value,
                characterColor = player.costume,
                startStocks = player.stocks,
                type = player.type.value,
                teamId = player.team.value if player.team else player.team,
                controllerFix = player.ucf,
                nametag = player.tag)
        self.scene = None #TODO find correspondence
        self.gameMode = None #TODO find correspondence

    def generate_object(self) -> GameStartType:
        return GameStartType(
            slpVersion = self.slpVersion,
            isTeams = self.isTeams,
            isPAL = self.isPAL,
            stageId = self.stageId,
            players = self.players,
            scene = self.scene,
            gameMode = self.gameMode
        )