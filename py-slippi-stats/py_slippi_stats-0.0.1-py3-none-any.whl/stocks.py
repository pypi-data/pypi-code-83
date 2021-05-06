from .common import Base, isDead, didLoseStock, PlayerIndexedType, StockType
from .slippitypes import FrameEntryType, FramesType, Dict, List, Optional
from .stats import StatComputer

#interface
class StockState(Base):
    def __init__(
        self,
        stock: Optional[StockType],
        **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.stock = stock


#export
#implements parents
class StockComputer(StatComputer):
    def __init__(
        self,
        state: Dict[PlayerIndexedType, StockState] = dict(), # private
        playerPermutations: List[PlayerIndexedType] = [], # private
        stocks: List[StockType] = [], # private
        **kwargs
    ) -> None:
        super().__init__(**kwargs, type=self.__class__)
        self.state = state
        self.playerPermutations = playerPermutations
        self.stocks = stocks
        self.setPlayerPermutations(playerPermutations)

    #public
    def setPlayerPermutations(self, playerPermutations: List[PlayerIndexedType]) -> None:
        self.playerPermutations = playerPermutations
        for indices in self.playerPermutations:
            playerState = StockState( #const
                stock=None)
            self.state[indices] = playerState

    #public
    def processFrame(self, frame: FrameEntryType, allFrames: FramesType) -> None:
        for indices in self.playerPermutations:
            state = self.state.get(indices, None) #const
            if state:
                handleStockCompute(allFrames, state, indices, frame, self.stocks)

    #public
    def fetch(self) -> List[StockType]:
        return self.stocks


def handleStockCompute(
    frames: FramesType,
    state: StockState,
    indices: PlayerIndexedType,
    frame: FrameEntryType,
    stocks: List[StockType],
) -> None:
    playerFrame = frame.players[indices.playerIndex].post #const
    currentFrameNumber = playerFrame.frame #const
    prevFrameNumber = currentFrameNumber - 1 #const
    prevPlayerFrame = frames[prevFrameNumber].players[indices.playerIndex].post if (prevFrameNumber in frames and frames[prevFrameNumber]) else None #const

    # If there is currently no active stock, wait until the player is no longer spawning.
    # Once the player is no longer spawning, start the stock
    if not state.stock:
        isPlayerDead = isDead(playerFrame.actionStateId) #const
        if isPlayerDead:
            return

        state.stock = StockType(
            playerIndex=indices.playerIndex,
            opponentIndex=indices.opponentIndex,
            startFrame=currentFrameNumber,
            endFrame=None,
            startPercent=0,
            endPercent=None,
            currentPercent=0,
            count=playerFrame.stocksRemaining,
            deathAnimation=None,
        )

        stocks.append(state.stock)
    elif prevPlayerFrame and didLoseStock(playerFrame, prevPlayerFrame):
        state.stock.endFrame = playerFrame.frame
        state.stock.endPercent = (prevPlayerFrame.percent if prevPlayerFrame.percent else 0)
        state.stock.deathAnimation = playerFrame.actionStateId
        state.stock = None
    else:
        state.stock.currentPercent = (playerFrame.percent if playerFrame.percent else 0)

