from slippi import Game

from .common import Base, ConversionType, PlayerIndexedType, StockType, OverallType, RatioType, InputCountsType, keyBy, groupBy, mapValues, getSinglesPlayerPermutationsFromSettings
from .conversions import ConversionsType, ConversionComputer
from .inputs import PlayerInput, InputComputer
from .factory import FramesTypeFactory, GameStartTypeFactory
from .slippitypes import List, number
from .stats import Stats
from .stocks import StockComputer

#interface
class ConversionsByPlayerByOpening(Base, dict): # Dict[str, Dict[str, ConversionsType]] (opening -> type -> conversion)
    def __init__(self , **kwargs) -> None:
        super().__init__(**kwargs)
        for playerIndex, openings in self.items():
            if not isinstance(playerIndex, str):
                raise ValueError('playerIndex in ConversionsByPlayerByOpening not initialized as str')
            if not isinstance(openings, dict):
                raise ValueError('openings in ConversionsByPlayerByOpening not initialized as dict')
            for openingType, conversionList in openings.items():
                if not isinstance(openingType, str):
                    raise ValueError('openingType in openings not initialized as str')
                if not isinstance(conversionList, list):
                    raise ValueError('conversionList in openings not initialized as list')
                for conversion in conversionList:
                    if not isinstance(conversion, ConversionType):
                        raise ValueError('conversion in conversionList not initialized as ConversionType')

    def __setitem__(self, key, val):
        if not isinstance(key, str):
            raise ValueError('playerIndex in ConversionsByPlayerByOpening not initialized as str')
        if not isinstance(val, dict):
            raise ValueError('openings in ConversionsByPlayerByOpening not initialized as dict')
        for openingType, conversionList in val.items():
            if not isinstance(openingType, str):
                raise ValueError('openingType in openings not initialized as str')
            if not isinstance(conversionList, list):
                raise ValueError('conversionList in openings not initialized as list')
            for conversion in conversionList:
                if not isinstance(conversion, ConversionType):
                    raise ValueError('conversion in conversionList not initialized as ConversionType')
        dict.__setitem__(self, key, val)


#export
def generateOverallStats(
    playerIndices: List[PlayerIndexedType],
    inputs: List[PlayerInput],
    stocks: List[StockType],
    conversions: ConversionsType,
    playableFrameCount: number,
) -> List[OverallType]:
    inputsByPlayer = keyBy(inputs, "playerIndex") #const
    stocksByPlayer = groupBy(stocks, "playerIndex") #const
    conversionsByPlayer = groupBy(conversions, "playerIndex") #const
    conversionsByPlayerByOpening: ConversionsByPlayerByOpening = mapValues(
        conversionsByPlayer,
        lambda conversions : groupBy(conversions, "openingType")
    )

    gameMinutes = playableFrameCount / 3600 #const

    overall = []
    for indices in playerIndices:
        playerIndex = indices.playerIndex #const
        opponentIndex = indices.opponentIndex #const
        playerInputs = inputsByPlayer.get(playerIndex, {}) #const
        inputCounts = InputCountsType( #const
            buttons=playerInputs.buttonInputCount,
            triggers=playerInputs.triggerInputCount,
            cstick=playerInputs.cstickInputCount,
            joystick=playerInputs.joystickInputCount,
            total=playerInputs.inputCount)
        conversions = conversionsByPlayer.get(playerIndex, []) #const
        successfulConversions = [conversion for conversion in conversions if len(conversion.moves) > 1] #const
        opponentStocks = stocksByPlayer.get(opponentIndex, []) #const
        opponentEndedStocks = [oppstock for oppstock in opponentStocks if oppstock.endFrame] #const

        conversionCount = len(conversions) #const
        successfulConversionCount = len(successfulConversions) #const
        totalDamage = sum([oppstock.currentPercent for oppstock in opponentStocks]) #const
        killCount = len(opponentEndedStocks) #const

        overall.append(OverallType(
            playerIndex=playerIndex,
            opponentIndex=opponentIndex,
            inputCounts=inputCounts,
            conversionCount=conversionCount,
            totalDamage=totalDamage,
            killCount=killCount,
            successfulConversions=getRatio(successfulConversionCount, conversionCount),
            inputsPerMinute=getRatio(inputCounts.total, gameMinutes),
            digitalInputsPerMinute=getRatio(inputCounts.buttons, gameMinutes),
            openingsPerKill=getRatio(conversionCount, killCount),
            damagePerOpening=getRatio(totalDamage, conversionCount),
            neutralWinRatio=getOpeningRatio(conversionsByPlayerByOpening, playerIndex, opponentIndex, "neutral-win"),
            counterHitRatio=getOpeningRatio(conversionsByPlayerByOpening, playerIndex, opponentIndex, "counter-attack"),
            beneficialTradeRatio=getBeneficialTradeRatio(conversionsByPlayerByOpening, playerIndex, opponentIndex),
        ))

    return overall

def getRatio(count: number, total: number) -> RatioType:
    return RatioType(
        count=count,
        total=total,
        ratio=count / total if total else None,
    )


def getOpeningRatio(
    conversionsByPlayerByOpening: ConversionsByPlayerByOpening,
    playerIndex: number,
    opponentIndex: number,
    type: str,
) -> RatioType:
    openings = conversionsByPlayerByOpening[playerIndex].get(type, []) if (playerIndex in conversionsByPlayerByOpening) else [] #const
    opponentOpenings = conversionsByPlayerByOpening[opponentIndex].get(type, []) if (opponentIndex in conversionsByPlayerByOpening) else [] #const
    return getRatio(len(openings), len(openings) + len(opponentOpenings))


def getBeneficialTradeRatio(
    conversionsByPlayerByOpening: ConversionsByPlayerByOpening,
    playerIndex: number,
    opponentIndex: number,
) -> RatioType:
    playerTrades = conversionsByPlayerByOpening[playerIndex].get('trade', []) if (playerIndex in conversionsByPlayerByOpening) else [] #const
    opponentTrades = conversionsByPlayerByOpening[opponentIndex].get('trade', []) if (opponentIndex in conversionsByPlayerByOpening) else [] #const

    benefitsPlayer = [] #const

    # Figure out which punishes benefited this player
    zippedTrades = zip(playerTrades, opponentTrades) #const
    for conversionPair in zippedTrades:
        playerConversion = conversionPair[0] #const
        opponentConversion = conversionPair[-1] #const
        playerDamage = playerConversion.currentPercent - playerConversion.startPercent #const
        opponentDamage = opponentConversion.currentPercent - opponentConversion.startPercent #const

        if playerConversion.didKill and not opponentConversion.didKill:
            benefitsPlayer.append(playerConversion)
        elif playerDamage > opponentDamage:
            benefitsPlayer.append(playerConversion)

    return getRatio(len(benefitsPlayer), len(playerTrades))


def getGameStats(game: Game) -> OverallType:

    frames = FramesTypeFactory(game.frames).generate_object()
    start = GameStartTypeFactory(game.start).generate_object()
    permutations = getSinglesPlayerPermutationsFromSettings(start)

    stats = Stats(
        frames=frames,
        playerPermutations=permutations,
        allComputers=[
            ConversionComputer,
            InputComputer,
            StockComputer])
    stats.process()

    return generateOverallStats(
        playerIndices=permutations,
        conversions=stats.allComputers[0].fetch(),
        inputs=stats.allComputers[1].fetch(),
        stocks=stats.allComputers[2].fetch(),
        playableFrameCount=max(frames))
