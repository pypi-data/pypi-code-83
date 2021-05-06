from .slippitypes import FrameEntryType, FramesType, PostFrameUpdateType, Dict, List, Optional, number
from .common import Base, MoveLandedType, ConversionType, PlayerIndexedType, orderBy, groupBy, isDamaged, isGrabbed, calcDamageTaken, isInControl, didLoseStock, Timers
from .stats import StatComputer

#interface
class PlayerConversionState(Base):
    def __init__(
        self,
        conversion: Optional[ConversionType],
        move: Optional[MoveLandedType],
        resetCounter: number,
        lastHitAnimation: Optional[number],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.conversion = conversion
        self.move = move
        self.resetCounter = resetCounter
        self.lastHitAnimation = lastHitAnimation


#interface
class MetadataType(Base):
    def __init__(
        self,
        lastEndFrameByOppIdx: Dict[number, number], # oppIdx -> lastEndFrame
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.lastEndFrameByOppIdx = lastEndFrameByOppIdx


# extra
class ConversionsType(Base, list):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def _is_long(self) -> bool:
        return True

#export
#implements parents
class ConversionComputer(StatComputer):

    #public
    def __init__(
        self,
        playerPermutations: List[PlayerIndexedType] = [], # private
        conversions: ConversionsType = ConversionsType(), # private
        state: Dict[PlayerIndexedType, PlayerConversionState] = dict(), # private
        metadata: MetadataType = MetadataType(lastEndFrameByOppIdx={}), #private
        **kwargs
    ) -> None:
        super().__init__(**kwargs, type=self.__class__)
        self.playerPermutations = playerPermutations
        self.conversions = conversions
        self.state = state
        self.metadata = metadata
        self.setPlayerPermutations(playerPermutations)

    #public
    def setPlayerPermutations(self, playerPermutations: List[PlayerIndexedType]) -> None:
        self.playerPermutations = playerPermutations
        for indices in self.playerPermutations:
            playerState = PlayerConversionState( #const
                conversion=None,
                move=None,
                resetCounter=0,
                lastHitAnimation=None)
            self.state[indices] = playerState

    #public
    def processFrame(self, frame: FrameEntryType, allFrames: FramesType) -> None:
        for indices in self.playerPermutations:
            state = self.state.get(indices, None) #const
            if state:
                handleConversionCompute(allFrames, state, indices, frame, self.conversions)

    #public
    def fetch(self) -> ConversionsType:
        self._populateConversionTypes()
        return self.conversions

    def _populateConversionTypes(self) -> None: #private
        # Post-processing step: set the openingTypes
        conversionsToHandle = [conversion for conversion in self.conversions if conversion.openingType == "unknown"] # const

        # Group new conversions by startTime and sort
        sortedConversions: List[ConversionsType] = orderBy(groupBy(conversionsToHandle,'startFrame'), (lambda conversions: conversions[0].startFrame))

        # Set the opening types on the conversions we need to handle
        for conversions in sortedConversions:
            isTrade = len(conversions) >= 2 #const
            for conversion in conversions:
                # Set end frame for this conversion
                self.metadata.lastEndFrameByOppIdx[conversion.playerIndex] = conversion.endFrame

                if isTrade:
                    # If trade, just short-circuit
                    conversion.openingType = "trade"
                    return

                # If not trade, check the opponent endFrame
                oppEndFrame = self.metadata.lastEndFrameByOppIdx.get(conversion.opponentIndex, None) #const
                isCounterAttack = oppEndFrame and oppEndFrame > conversion.startFrame #const
                conversion.openingType = "counter-attack" if isCounterAttack else "neutral-win"


def handleConversionCompute(
    frames: FramesType,
    state: PlayerConversionState,
    indices: PlayerIndexedType,
    frame: FrameEntryType,
    conversions: ConversionsType,
) -> None :
    currentFrameNumber = frame.frame #const
    playerFrame: PostFrameUpdateType = frame.players[indices.playerIndex].post #const
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
    # start a conversion or
    if opntIsDamaged or opntIsGrabbed:
        if not state.conversion:
            state.conversion = ConversionType(
                playerIndex=indices.playerIndex,
                opponentIndex=indices.opponentIndex,
                startFrame=currentFrameNumber,
                endFrame=None,
                startPercent=(prevOpponentFrame.percent if prevOpponentFrame.percent else 0) if prevOpponentFrame else 0,
                currentPercent=(opponentFrame.percent if opponentFrame.percent else 0),
                endPercent=None,
                moves=[],
                didKill=False,
                openingType="unknown", # Will be updated later
            )

            conversions.append(state.conversion)

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

                state.conversion.moves.append(state.move)

            if state.move:
                state.move.hitCount += 1
                state.move.damage += opntDamageTaken

            # Store previous frame animation to consider the case of a trade, the previous
            # frame should always be the move that actually connected... I hope
            state.lastHitAnimation = prevPlayerFrame.actionStateId if prevPlayerFrame else None
    

    if not state.conversion:
        # The rest of the function handles conversion termination logic, so if we don't
        # have a conversion started, there is no need to continue
        return

    opntInControl = isInControl(oppActionStateId) #const
    opntDidLoseStock = prevOpponentFrame and didLoseStock(opponentFrame, prevOpponentFrame) #const

    # Update percent if opponent didn't lose stock
    if not opntDidLoseStock:
        state.conversion.currentPercent = (opponentFrame.percent if opponentFrame.percent else 0)

    if opntIsDamaged or opntIsGrabbed:
        # If opponent got grabbed or damaged, reset the reset counter
        state.resetCounter = 0

    shouldStartResetCounter = state.resetCounter == 0 and opntInControl #const
    shouldContinueResetCounter = state.resetCounter > 0 #const
    if shouldStartResetCounter or shouldContinueResetCounter:
        # This will increment the reset timer under the following conditions:
        # 1) if we were punishing opponent but they have now entered an actionable state
        # 2) if counter has already started counting meaning opponent has entered actionable state
        state.resetCounter += 1

    shouldTerminate = False #let

    # Termination condition 1 - player kills opponent
    if opntDidLoseStock:
        state.conversion.didKill = True
        shouldTerminate = True

    # Termination condition 2 - conversion resets on time
    if state.resetCounter > Timers.PUNISH_RESET_FRAMES.value:
        shouldTerminate = True

    # If conversion should terminate, mark the end states and add it to list
    if shouldTerminate:
        state.conversion.endFrame = playerFrame.frame
        state.conversion.endPercent = (prevOpponentFrame.percent if prevOpponentFrame.percent else 0) if prevOpponentFrame else 0

        state.conversion = None
        state.move = None
