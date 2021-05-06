from .common import Base, PlayerIndexedType, _indent
from .slippitypes import FrameEntryType, Frames, FramesType, List, Optional, Union, number

#export
#interface
class StatComputer(Base):

    def __init__(self, type: type, **kwargs) -> None:
        self.type = type
        super().__init__(**kwargs)

    def setPlayerPermutations(self, indices: List[PlayerIndexedType]) -> None:
        raise NotImplementedError('setPlayerPermutations not implemented')

    def processFrame(self, newFrame: FrameEntryType, allFrames: FramesType) -> None:
        raise NotImplementedError('processFrame not implemented')

    def fetch(self):
        raise NotImplementedError('fetch not implemented')

#export
#interface
class StatOptions(Base):

    def __init__(self, processOnTheFly: bool):
        self.processOnTheFly = processOnTheFly


defaultOptions = StatOptions(processOnTheFly=False)

#export
class Stats(Base):

    #public
    def __init__(
        self,
        options: Optional[StatOptions] = None, #private
        lastProcessedFrame: Optional[number] = None, #private
        frames: FramesType = FramesType(), #private
        playerPermutations: List[PlayerIndexedType] = [], # private
        allComputers: List[StatComputer] = [], # private
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.options = options if options else defaultOptions
        self.lastProcessedFrame = lastProcessedFrame
        self.frames = frames
        self.playerPermutations = playerPermutations
        self.allComputers: List[StatComputer] = []
        self.register(allComputers)
        self.setPlayerPermutations(playerPermutations)

    #public
    def setPlayerPermutations(self, indices: List[PlayerIndexedType]) -> None:
        self.playerPermutations = indices
        for comp in self.allComputers:
            comp.setPlayerPermutations(indices)

    #public
    def register(self, computers: List[StatComputer]) -> None:
        for computer in computers:
            self.allComputers.append(computer(
                playerPermutations=self.playerPermutations))

    #public
    def process(self) -> None:
        if len(self.playerPermutations) == 0:
            return
        i = self.lastProcessedFrame + 1 if self.lastProcessedFrame is not None else Frames.FIRST.value #let
        for i in self.frames:
            frame = self.frames[i] #const
            # Don't attempt to compute stats on frames that have not been fully received
            if not isCompletedFrame(self.playerPermutations, frame):
                return
            for comp in self.allComputers:
                comp.processFrame(frame, self.frames)
            self.lastProcessedFrame = i

    #public
    def addFrame(self, frame: FrameEntryType) -> None:
        self.frames[frame.frame] = frame

        if self.options.processOnTheFly:
            self.process()


def isCompletedFrame(playerPermutations: List[PlayerIndexedType], frame: FrameEntryType) -> bool:
    # This function checks whether we have successfully received an entire frame.
    # It is not perfect because it does not wait for follower frames. Fortunately,
    # follower frames are not used for any stat calculations so this doesn't matter
    # for our purposes.
    playerIndex, opponentIndex = playerPermutations[0][:] #const
    playerPostFrame = frame.players[playerIndex].post #const
    oppPostFrame = frame.players[opponentIndex].post #const
    return playerPostFrame and oppPostFrame
