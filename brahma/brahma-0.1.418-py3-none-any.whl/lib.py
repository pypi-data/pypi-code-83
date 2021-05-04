import os, sys

#command line input

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

#raw data file manipulation

def parsePriceDataLine(line):
    parsedArray = []
    parsedArray = line.split(',')
    #print (parsedArray[1])
    return (parsedArray)

def GetDateStr(dt):
    year = str(dt.year)
    month = str(dt.month)
    if int(month) < 10:
        month = '0' + str(month)
    day = str(dt.day)
    if int(day) < 10:
        day = '0' + str(day)
    return (year+month+day)

def GetDayTime(dt):
    print (dt)
    hour = str(dt.hour)
    if int(hour) < 10:
        hour = '0' + str(hour)
    minute = str(dt.minute)
    if int(minute) < 10:
        minute = '0' + str(minute)
    return (hour+minute)

def parseHighLow(data):
    print ("waiting...")

def testlib():
    print ('connected to lib module')

def GetConvertVal(market):
    if market in marketConvertVals:
        return marketConvertVals[market]

def GetPipVal(market):
    if market in marketPipVals:
        return marketPipVals[market]

def GetTimeVecIndex(time, timeVec):
    return timeVec.index(time)

def GetPipDifference(startPrice, endPrice, market):
    deltaPrice = float(startPrice) - float(endPrice)
    pipVal = GetPipVal(market)
    deltaPips = deltaPrice/pipVal
    return round(deltaPips,2)

def GetPipValFromMarketPrice(deltaPrice, market):
    pipVal = GetPipVal(market)
    deltaPips = deltaPrice/pipVal
    return round(deltaPips,2)

def GetMinute(time):
    parsedArray = []
    parsedArray = time.split('-')
    return (parsedArray[len(parsedArray)-1])

def GetDateFromPricePrint(pricePrintTime):
    parsedArray = []

    time = str(pricePrintTime)
    parsedArray = time.split('-')
    #print (parsedArray)
    #print (parsedArray)
    #print(time)
    #print (parsedArray)
    date = parsedArray[0]+parsedArray[1]+parsedArray[2]
    return date

def getDate():
    import datetime
    now = datetime.datetime.now()

    #print (str(now))
    date = now.strftime("%Y-%m-%d")
    return date

def GetHourFromPricePrint(pricePrintTime):
    parsedArray = []

    time = str(pricePrintTime)
    parsedArray = time.split('-')
    #print (parsedArray)
    #print(time)
    
    hour = float(parsedArray[3])
    return hour
    #exit()

def GetMinuteFromPricePrint(pricePrintTime):
    parsedArray = []

    time = str(pricePrintTime)
    parsedArray = time.split('-')
    #print (parsedArray)
    #print(time)
    #print (parsedArray)
    minute = float(parsedArray[4])
    return minute
    #exit()

def GetPriceDeduction(price_one,  pips,market):
    pipVal = GetPipVal(market)
    diff = pips * pipVal
    return round(price_one - diff,5)


def GetPriceSum(price_one, pips, market):
    pipVal = GetPipVal(market)
    diff = pips * pipVal
    return round(price_one + diff, 5)


def GenerateTradeID():
    import random
    _id = str(random.randint(0,10000)) + str(random.randint(0,100000)) + "trade"
    return _id


#---------------------FTP DATA TO VX.COM SERVER---------------------------------------


def FTPFile(file='none'):
    from ftplib import FTP

    ftp = FTP('ftp.vixencapital.com')
    ftp.login(user='vixencapital.com', passwd='Edinburgh69!')

    UPLOADDIR = '/htdocs/plotter/data/'
    #filename = '../../results/dirbots/botsData.json'
    filename = "test.txt"
    #file = open(filename, 'rb')
    #ftp.cwd(UPLOADDIR)
    #ftp.storbinary('STOR'+filename, file)

    with open(filename, 'rb') as contents:
        ftp.storbinary('STOR %s' % filename, contents)

    ftp.quit()
    ftp.close()
