from .common import Base, State, PlayerIndexedType, ActionCountsType
from .slippitypes import FramesType, FrameEntryType, Dict, List, number
from .stats import StatComputer

# Frame pattern that indicates a dash dance turn was executed
dashDanceAnimations = [State.DASH.value, State.TURN.value, State.DASH.value] #const


# extra
class AnimationsType(Base, list):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def _is_long(self) -> bool:
        return True

#interface
class PlayerActionState(Base):

    def __init__(
        self,
        playerCounts: ActionCountsType,
        animations: AnimationsType,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.playerCounts = playerCounts
        self.animations = animations


#export
#implements parents
class ActionsComputer(StatComputer):

    def __init__(
        self,
        playerPermutations: List[PlayerIndexedType] = [], # private
        state: Dict[PlayerIndexedType, PlayerActionState] = dict(), # private
        **kwargs
    ) -> None:
        super().__init__(**kwargs, type=self.__class__)
        self.playerPermutations = playerPermutations
        self.state = state
        self.setPlayerPermutations(playerPermutations)

    #public
    def setPlayerPermutations(self, playerPermutations: List[PlayerIndexedType]) -> None:
        self.playerPermutations = playerPermutations
        for indices in self.playerPermutations:
            playerCounts = ActionCountsType( #const
                playerIndex=indices.playerIndex,
                opponentIndex=indices.opponentIndex,
                wavedashCount=0,
                wavelandCount=0,
                airDodgeCount=0,
                dashDanceCount=0,
                spotDodgeCount=0,
                ledgegrabCount=0,
                rollCount=0,
                lCancelSuccessCount=0,
                lCancelFailCount=0)
            playerState = PlayerActionState( #const
                playerCounts=playerCounts,
                animations=AnimationsType())
            self.state[indices] = playerState

    #public
    def processFrame(self, frame: FrameEntryType, allFrames: FramesType = None) -> None:
        for indices in self.playerPermutations:
            state = self.state.get(indices, None) #const
            if state:
                handleActionCompute(state, indices, frame)

    #public
    def fetch(self) -> List[ActionCountsType]:
        return [val.playerCounts for val in self.state.values()]


def isRolling(animation: State) -> bool:
    return animation == State.ROLL_BACKWARD.value or animation == State.ROLL_FORWARD.value


def didStartRoll(currentAnimation: number, previousAnimation: number) -> bool:
    isCurrentlyRolling = isRolling(currentAnimation) #const
    wasPreviouslyRolling = isRolling(previousAnimation) #const
    return isCurrentlyRolling and not wasPreviouslyRolling


def isSpotDodging(animation: State) -> bool:
    return animation == State.SPOT_DODGE.value


def didStartSpotDodge(currentAnimation: State, previousAnimation: State) -> bool:
    isCurrentlyDodging = isSpotDodging(currentAnimation) #const
    wasPreviouslyDodging = isSpotDodging(previousAnimation) #const
    return isCurrentlyDodging and not wasPreviouslyDodging


def isAirDodging(animation: State) -> bool:
    return animation == State.AIR_DODGE.value


def didStartAirDodge(currentAnimation: State, previousAnimation: State) -> bool:
    isCurrentlyDodging = isAirDodging(currentAnimation) #const
    wasPreviouslyDodging = isAirDodging(previousAnimation) #const
    return isCurrentlyDodging and not wasPreviouslyDodging


def isGrabbingLedge(animation: State) -> bool:
    return animation == State.CLIFF_CATCH.value


def isAerialAttack(animation: State) -> bool:
    return animation >= State.AERIAL_ATTACK_START.value and animation <= State.AERIAL_ATTACK_END.value


def didStartLedgegrab(currentAnimation: State, previousAnimation: State) -> bool:
    isCurrentlyGrabbingLedge = isGrabbingLedge(currentAnimation) #const
    wasPreviouslyGrabbingLedge = isGrabbingLedge(previousAnimation) #const
    return isCurrentlyGrabbingLedge and not wasPreviouslyGrabbingLedge


def handleActionCompute(state: PlayerActionState, indices: PlayerIndexedType, frame: FrameEntryType) -> None:
    playerFrame = frame.players[indices.playerIndex].post #const
    def incrementCount(field: str, condition: bool) -> None: #const
        if not condition:
            return None
        # FIXME: ActionsCountsType should be a map of actions -> number, instead of accessing the field via str
        setattr(state.playerCounts, field, getattr(state.playerCounts, field) + 1)

    # Manage animation state
    currentAnimation = playerFrame.actionStateId #const
    state.animations.append(currentAnimation)

    # Grab last 3 frames
    last3Frames = state.animations[-3:] #const
    prevAnimation = last3Frames[len(last3Frames) - 2] #const

    # Increment counts based on conditions
    didDashDance = (last3Frames == dashDanceAnimations) #const
    incrementCount("dashDanceCount", didDashDance)

    didRoll = didStartRoll(currentAnimation, prevAnimation) #const
    incrementCount("rollCount", didRoll)

    didSpotDodge = didStartSpotDodge(currentAnimation, prevAnimation) #const
    incrementCount("spotDodgeCount", didSpotDodge)

    didAirDodge = didStartAirDodge(currentAnimation, prevAnimation) #const
    incrementCount("airDodgeCount", didAirDodge)

    didGrabLedge = didStartLedgegrab(currentAnimation, prevAnimation) #const
    incrementCount("ledgegrabCount", didGrabLedge)

    if isAerialAttack(currentAnimation):
        incrementCount("lCancelSuccessCount", playerFrame.lCancelStatus == 1)
        incrementCount("lCancelFailCount", playerFrame.lCancelStatus == 2)

    # Handles wavedash detection (and waveland)
    handleActionWavedash(state.playerCounts, state.animations)


def handleActionWavedash(counts: ActionCountsType, animations: List[State]) -> None:
    currentAnimation = animations[-1] #const
    prevAnimation = animations[len(animations) - 2] #const

    isSpecialLanding = currentAnimation == State.LANDING_FALL_SPECIAL.value #const
    isAcceptablePrevious = isWavedashInitiationAnimation(prevAnimation) #const
    isPossibleWavedash = isSpecialLanding and isAcceptablePrevious #const

    if not isPossibleWavedash:
        return None

    # Here we special landed, it might be a wavedash, let's check
    # We grab the last 8 frames here because that should be enough time to execute a
    # wavedash. This number could be tweaked if we find False negatives
    recentFrames = animations[-8:] #const
    recentAnimations = {}
    for animation in recentFrames: #keyBy
        recentAnimations[animation] = animation

    if len(recentAnimations) == 2 and (State.AIR_DODGE.value in recentAnimations) and recentAnimations[State.AIR_DODGE.value]:
        # If the only other animation is air dodge, this might be really late to the point
        # where it was actually an air dodge. Air dodge animation is really long
        return None

    if (State.AIR_DODGE.value in recentAnimations) and recentAnimations[State.AIR_DODGE.value]:
        # If one of the recent animations was an air dodge, let's remove that from the
        # air dodge counter, we don't want to count air dodges used to wavedash/land
        counts.airDodgeCount -= 1

    if (State.ACTION_KNEE_BEND.value in recentAnimations) and recentAnimations[State.ACTION_KNEE_BEND.value]:
        # If a jump was started recently, we will consider this a wavedash
        counts.wavedashCount += 1
    else:
        # If there was no jump recently, this is a waveland
        counts.wavelandCount += 1


def isWavedashInitiationAnimation(animation: State) -> bool:
    if animation == State.AIR_DODGE.value:
        return True

    isAboveMin = animation >= State.CONTROLLED_JUMP_START.value #const
    isBelowMax = animation <= State.CONTROLLED_JUMP_END.value #const
    return isAboveMin and isBelowMax

