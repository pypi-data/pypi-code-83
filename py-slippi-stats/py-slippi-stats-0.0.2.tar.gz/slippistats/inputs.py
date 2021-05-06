from .common import Base, PlayerIndexedType
from .slippitypes import FramesType, FrameEntryType, Frames, Dict, List, number

from .stats import StatComputer

from enum import Enum

#enum
class JoystickRegion(Enum):
    DZ = 0
    NE = 1
    SE = 2
    SW = 3
    NW = 4
    N = 5
    E = 6
    S = 7
    W = 8


#export
#interface
class PlayerInput(Base):
    def __init__(
        self,
        playerIndex: number,
        opponentIndex: number,
        inputCount: number,
        joystickInputCount: number,
        cstickInputCount: number,
        buttonInputCount: number,
        triggerInputCount: number,
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.playerIndex = playerIndex
        self.opponentIndex = opponentIndex
        self.inputCount = inputCount
        self.joystickInputCount = joystickInputCount
        self.cstickInputCount = cstickInputCount
        self.buttonInputCount = buttonInputCount
        self.triggerInputCount = triggerInputCount


#export
#implements parents
class InputComputer(StatComputer):
    def __init__(
        self,
        playerPermutations: List[PlayerIndexedType] = [], # private
        state: Dict[PlayerIndexedType, PlayerInput] = dict(), # private
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
            playerState = PlayerInput( #const
                playerIndex=indices.playerIndex,
                opponentIndex=indices.opponentIndex,
                inputCount=0,
                joystickInputCount=0,
                cstickInputCount=0,
                buttonInputCount=0,
                triggerInputCount=0)
            self.state[indices] = playerState

    #public
    def processFrame(self, frame: FrameEntryType, allFrames: FramesType) -> None:
        for indices in self.playerPermutations:
            state = self.state.get(indices, None) #const
            if state:
                handleInputCompute(allFrames, state, indices, frame)

    #public
    def fetch(self) -> List[PlayerInput]:
        return self.state.values()


def handleInputCompute(
    frames: FramesType,
    state: PlayerInput,
    indices: PlayerIndexedType,
    frame: FrameEntryType,
) -> None:
    playerFrame = frame.players[indices.playerIndex].pre #const
    currentFrameNumber = playerFrame.frame #const
    prevFrameNumber = currentFrameNumber - 1 #const
    prevPlayerFrame = frames[prevFrameNumber].players[indices.playerIndex].pre if (prevFrameNumber in frames and frames[prevFrameNumber]) else None #const

    if currentFrameNumber < Frames.FIRST_PLAYABLE.value or not prevPlayerFrame:
        # Don't count inputs until the game actually starts
        return

    # First count the number of buttons that go from 0 to 1
    # Increment action count by amount of button presses
    invertedPreviousButtons = ~prevPlayerFrame.physicalButtons #const
    currentButtons = playerFrame.physicalButtons #const
    buttonChanges = invertedPreviousButtons & currentButtons & 0xfff #const
    newInputsPressed = countSetBits(buttonChanges) #const
    state.inputCount += newInputsPressed
    state.buttonInputCount += newInputsPressed

    # Increment action count when sticks change from one region to another.
    # Don't increment when stick returns to deadzone
    prevAnalogRegion = getJoystickRegion(prevPlayerFrame.joystickX, prevPlayerFrame.joystickY) #const
    currentAnalogRegion = getJoystickRegion(playerFrame.joystickX, playerFrame.joystickY) #const
    if prevAnalogRegion != currentAnalogRegion and currentAnalogRegion != JoystickRegion.DZ.value:
        state.inputCount += 1
        state.joystickInputCount += 1

    # Do the same for c-stick
    prevCstickRegion = getJoystickRegion(prevPlayerFrame.cStickX, prevPlayerFrame.cStickY) #const
    currentCstickRegion = getJoystickRegion(playerFrame.cStickX, playerFrame.cStickY) #const
    if prevCstickRegion != currentCstickRegion and currentCstickRegion != JoystickRegion.DZ.value:
        state.inputCount += 1
        state.cstickInputCount += 1

    # Increment action on analog trigger... I'm not sure when. This needs revision
    # Currently will update input count when the button gets pressed past 0.3
    # Changes from hard shield to light shield should probably count as inputs but
    # are not counted here
    if prevPlayerFrame.physicalLTrigger < 0.3 and playerFrame.physicalLTrigger >= 0.3:
        state.inputCount += 1
        state.triggerInputCount += 1
    if prevPlayerFrame.physicalRTrigger < 0.3 and playerFrame.physicalRTrigger >= 0.3:
        state.inputCount += 1
        state.triggerInputCount += 1


def countSetBits(x: number) -> number:
    # This function solves the Hamming Weight problem. Effectively it counts the number of
    # bits in the input that are set to 1
    # This implementation is supposedly very efficient when most bits are zero.
    # Found: https://en.wikipedia.org/wiki/Hamming_weight#Efficient_implementation
    bits = x #let

    count = 0 #let
    while bits:
        bits &= bits - 1
        count += 1
    return count


def getJoystickRegion(x: number, y: number) -> JoystickRegion:
    region = JoystickRegion.DZ.value #let

    if x >= 0.2875 and y >= 0.2875:
        region = JoystickRegion.NE.value
    elif x >= 0.2875 and y <= -0.2875:
        region = JoystickRegion.SE.value
    elif x <= -0.2875 and y <= -0.2875:
        region = JoystickRegion.SW.value
    elif x <= -0.2875 and y >= 0.2875:
        region = JoystickRegion.NW.value
    elif y >= 0.2875:
        region = JoystickRegion.N.value
    elif x >= 0.2875:
        region = JoystickRegion.E.value
    elif y <= -0.2875:
        region = JoystickRegion.S.value
    elif x <= -0.2875:
        region = JoystickRegion.W.value

    return region

