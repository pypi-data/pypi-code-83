from .slippitypes import FrameEntryType, FramesType, PostFrameUpdateType, List, Dict, Optional, number
from .common import Base, MoveLandedType, ComboType, PlayerIndexedType, isDamaged, isGrabbed, calcDamageTaken, isTeching, didLoseStock, Timers, isDown, isDead
from .stats import StatComputer

#interface
class ComboState(Base):

    def __init__(
        self,
        combo: Optional[ComboType],
        move: Optional[MoveLandedType],
        resetCounter: number,
        lastHitAnimation: Optional[number],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.combo = combo
        self.move = move
        self.resetCounter = resetCounter
        self.lastHitAnimation = lastHitAnimation


# extra
class CombosType(Base, list):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def _is_long(self) -> bool:
        return True


#export
#implements parents
class ComboComputer(StatComputer):

    def __init__(
        self,
        playerPermutations: List[PlayerIndexedType] = [], # private
        state: Dict[PlayerIndexedType, ComboState] = dict(), # private
        combos: CombosType = CombosType(), # private
        **kwargs
    ) -> None:
        super().__init__(**kwargs, type=self.__class__)
        self.playerPermutations = playerPermutations
        self.state = state
        self.combos = combos
        self.setPlayerPermutations(playerPermutations)

    #public
    def setPlayerPermutations(self, playerPermutations: List[PlayerIndexedType]) -> None:
        self.playerPermutations = playerPermutations
        for indices in self.playerPermutations:
            playerState = ComboState( #const
                combo=None,
                move=None,
                resetCounter=0,
                lastHitAnimation=None)
            self.state[indices] = playerState

    #public
    def processFrame(self, frame: FrameEntryType, allFrames: FramesType) -> None:
        for indices in self.playerPermutations:
            state = self.state.get(indices, None) #const
            if state:
                handleComboCompute(allFrames, state, indices, frame, self.combos)

    #public
    def fetch(self) -> List[ComboType]:
        return self.combos


def handleComboCompute(
    frames: FramesType,
    state: ComboState,
    indices: PlayerIndexedType,
    frame: FrameEntryType,
    combos: CombosType,
) -> None:
    currentFrameNumber = frame.frame #const
    playerFrame = frame.players[indices.playerIndex].post #const
    opponentFrame = frame.players[indices.opponentIndex].post #const

    prevFrameNumber = currentFrameNumber - 1 #const
    prevPlayerFrame: Optional[PostFrameUpdateType] = None #let
    prevOpponentFrame: Optional[PostFrameUpdateType] = None #let

    if (prevFrameNumber in frames) and frames[prevFrameNumber]:
        prevPlayerFrame = frames[prevFrameNumber].players[indices.playerIndex].post
        prevOpponentFrame = frames[prevFrameNumber].players[indices.opponentIndex].post

    oppActionStateId = opponentFrame.actionStateId #const
    opntIsDamaged = isDamaged(oppActionStateId) #const
    opntIsGrabbed = isGrabbed(oppActionStateId) #const
    opntDamageTaken = calcDamageTaken(opponentFrame, prevOpponentFrame) if prevOpponentFrame else 0 #const

    # Keep track of whether actionState changes after a hit. Used to compute move count
    # When purely using action state there was a bug where if you did two of the same
    # move really fast (such as ganon's jab), it would count as one move. Added
    # the actionStateCounter at this point which counts the number of frames since
    # an animation started. Should be more robust, for old files it should always be
    # None and None < None = False
    actionChangedSinceHit = playerFrame.actionStateId != state.lastHitAnimation #const
    actionCounter = playerFrame.actionStateCounter #const
    prevActionCounter = prevPlayerFrame.actionStateCounter if prevPlayerFrame else 0 #const
    actionFrameCounterReset = actionCounter < prevActionCounter #const
    if actionChangedSinceHit or actionFrameCounterReset:
        state.lastHitAnimation = None

    # If opponent took damage and was put in some kind of stun this frame, either
    # start a combo or count the moves for the existing combo
    if opntIsDamaged or opntIsGrabbed:
        if not state.combo:
            state.combo = ComboType(
                playerIndex=indices.playerIndex,
                opponentIndex=indices.opponentIndex,
                startFrame=currentFrameNumber,
                endFrame=None,
                startPercent=(prevOpponentFrame.percent if prevOpponentFrame.percent else 0) if prevOpponentFrame else 0,
                currentPercent=(opponentFrame.percent if opponentFrame.percent else 0),
                endPercent=None,
                moves=[],
                didKill=False,
            )

            combos.append(state.combo)

        if opntDamageTaken:
            # If animation of last hit has been cleared that means this is a new move. This
            # prevents counting multiple hits from the same move such as fox's drill
            if state.lastHitAnimation == None:
                state.move = MoveLandedType(
                    frame=currentFrameNumber,
                    moveId=playerFrame.lastAttackLanded,
                    hitCount=0,
                    damage=0,
                )

                state.combo.moves.append(state.move)

            if state.move:
                state.move.hitCount += 1
                state.move.damage += opntDamageTaken

            # Store previous frame animation to consider the case of a trade, the previous
            # frame should always be the move that actually connected... I hope
            state.lastHitAnimation = prevPlayerFrame.actionStateId if prevPlayerFrame else None
    

    if not state.combo:
        # The rest of the function handles combo termination logic, so if we don't
        # have a combo started, there is no need to continue
        return

    opntIsTeching = isTeching(oppActionStateId) #const
    opntIsDowned = isDown(oppActionStateId) #const
    opntDidLoseStock = prevOpponentFrame and didLoseStock(opponentFrame, prevOpponentFrame) #const
    opntIsDying = isDead(oppActionStateId) #const

    # Update percent if opponent didn't lose stock
    if not opntDidLoseStock:
        state.combo.currentPercent = (opponentFrame.percent if opponentFrame.percent else 0)

    if opntIsDamaged or opntIsGrabbed or opntIsTeching or opntIsDowned or opntIsDying:
        # If opponent got grabbed or damaged, reset the reset counter
        state.resetCounter = 0
    else:
        state.resetCounter += 1

    shouldTerminate = False #let

    # Termination condition 1 - player kills opponent
    if opntDidLoseStock:
        state.combo.didKill = True
        shouldTerminate = True

    # Termination condition 2 - combo resets on time
    if state.resetCounter > Timers.COMBO_STRING_RESET_FRAMES.value:
        shouldTerminate = True

    # If combo should terminate, mark the end states and add it to list
    if shouldTerminate:
        state.combo.endFrame = playerFrame.frame
        state.combo.endPercent = (prevOpponentFrame.percent if prevOpponentFrame.percent else 0) if prevOpponentFrame else 0

        state.combo = None
        state.move = None

