import os, sys, random
CONFIGPATH = os.path.join(os.path.expanduser('~'), 'tradingalgorithm', 'code', 'lucen', 'code','')
sys.path.insert(0,CONFIGPATH)

from time import *
from config import *
from lib import *



#user defined [Lucen]
class PriceFeedPrint(object):
    """Price print from the simulated price feed. This is what is returned into the simulated feed 
    in the 'tick' function. This data is added to the connected market dataseries required for simulation
    or optimisation.
    
    Arguments:
        object {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    def __init__(self, bid, offer, time):
        """initialise the price print.
        
        Arguments:
            bid {[float/str]} -- the price print bid value
            offer {[float/str]} -- the price print off value
            time {[float/str]} -- the time of the price print
        """
        self.bid = float(bid)
        self.offer = float(offer)
        self.time = str(time)
        self.high = 0
        self.low = 0
        self.change = 0

    def __str__(self):
        """Returns the price print as a string for output.
        
        Returns:
            [string] -- [price print description]
        """
        return ("%f %f %s" % (self.bid, self.offer, self.time))

class SimulatedEpochFeed(object):
    """SimulatedDailyFeed stores the daily feed data for the market. Current resolution is one second.
    
    Arguments:
        object {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    def __init__(self, day):
        """Constructor. Set the day YY-MM-DD, bid offer and time vectors.
        
        Arguments:
            day {[type]} -- [description]
        """
        self.Day = day
        self.BidList = []
        self.OfferList = []
        self.TimeList =[]

    def AddPrint(self, bid, offer, time):
        """Add a print to the daily feed. This is called in the datastructure builder in SimulatedFeed.
        
        Arguments:
            bid {float} -- [bid]
            offer {float} -- [offer]
            time {string} -- [time]
        """
        self.BidList.append(bid)
        self.OfferList.append(offer)
        self.TimeList.append(time)

    def CloseDay(self):
        self.FirstPrint = self.TimeList[0]
        self.LastPrint = self.TimeList[len(self.TimeList)-1]

    def GetSimulatedPrint(self, indx):

        """Get the price print at the vector indx. Build and defines a PriceFeedPrint which 
        is returned. Checks to make sure that there is no segmentation fault
        Returns:
            [PriceFeedPrint] -- [Price feed]
            [int]            -- [Result]
        """
        if indx < len(self.BidList)-1:
            bid = float(self.BidList[indx])
            offer = float(self.OfferList[indx])
            time = str(self.TimeList[indx])
            pp = PriceFeedPrint(bid, offer, time)
            #print (pp.offer)
            return pp
        else:
            return -1

class SimulatedFeed(object):

    """Main holder for all days of data and their individual SimulatedDailyFeed objects.
    This dictionary is build in the 'buildsimulatedfeed' routine and requires the correct 
    folder and filename structire for the market in question.

    Returns:
        [type] -- [description]
    """

    def __init__(self, market = 'eurusd', numberOfDays = 3):
        self.Market = market
        self.numberOfDays = numberOfDays
        self.dataSeries = None
        #print (self.numberOfDays)
        self.FeedDays = []
        self.Feed = {}

    def SetDataSeries(self, dataSeries):
        """This set the dataSeries pointer/object from the simulation/optimisation.
        dataSeries.AddData is called in the 'Tick' routine if this field is set. Initially
        set as None
        
        Arguments:
            dataSeries {[DataSeries]} -- [DataSeries class for simualation/optimisation. See ref.]
        """
        

        self.dataSeries = dataSeries

    def BuildSimulatedFeed(self, startHour=0, endHour=24):

        """Builds the simulated feed for number of days required. Sets the time limits for the data. 
        Reads data files from MARKET_PLOT_DATA_FOLDER.
        
        Keyword Arguments:
            startHour {int} -- [description] (default: {0})
            endHour {int} -- [description] (default: {24})
        """

        print ("herererjekklk;ljerlk")
        fileList = os.listdir(MARKET_PLOT_DATA_FOLDER + "/" + self.Market)
        dayCnt = 0
        for fileName in fileList:
            print (fileName)
            if fileName.endswith(".txt"):
                fnArray = fileName.split('.')
                day = fnArray[0]
                DailyFeed = SimulatedDailyFeed(day)
                self.FeedDays.append(day)
                fullFileName = MARKET_PLOT_DATA_FOLDER + "/" + self.Market + "/" + fileName       
                try:    
                    fs = open(fullFileName, 'r')
                except Exception as e:
                    print("type error: " + str(e))
                    print(traceback.format_exc())

                for line in fs:
                    lineSpl = line.split(',')
                    
                    hr = GetHourFromPricePrint(lineSpl[0])
                    
                    #---sample data---
                    if hr> startHour:
                        if hr < endHour:
                            collectData = False
                            randNum = random.random()
                            #print (OptimsationParameters)
                            
                            if randNum < OptimsationParameters['feed_sample_rate']:
                                collectData = True


                            #-----------------
                            if collectData:
                                DailyFeed.AddPrint(lineSpl[1], lineSpl[2], lineSpl[0])
                                #print (lineSpl[1], lineSpl[2], lineSpl[0])

                fs.close()

                DailyFeed.CloseDay()
                self.Feed[day] = DailyFeed

                dayCnt +=1
                if dayCnt >= self.numberOfDays:
                    break

    def StartFeed(self):
        """Starts the feed for a particular day by setting the vector index pointer to 0.
        """
        print ("Starting feed")
        self.VIndex = 0
        return 1

 

    def Tick(self, day):
        """This simulates a market price tick, but limited to the time resolution saved in the datafiles.
        
        Arguments:
            day {[string]} -- The date of the data which is being read
            last_hr {[double/float]} -- last hour of feed
        
        Returns:
            [type] -- [description]
        """


        simulatedPricePrint = self.Feed[day].GetSimulatedPrint(self.VIndex)
        

        if self.dataSeries == None:

            if simulatedPricePrint is not -1:
                hr = GetHourFromPricePrint(simulatedPricePrint.time)
                if hr > last_hr:         
                
                    self.VIndex = 0
                    return -1
                
                print(simulatedPricePrint)
                self.VIndex += 1
                return 1

            return -1



        if self.dataSeries != None:
            
            if simulatedPricePrint is not -1:
            #add to dataseries
                #print (simulatedPricePrint, day)
                
                #hr = GetHourFromPricePrint(simulatedPricePrint.time)
                #if hr > last_hr:
                    #print ("End of day***")
                    #sleep(10000000)
                    #self.VIndex = 0
                    #self.dataSeries.DumpCandles(self.Market)
                    #print ("Reseting Market Data for new day")
                    #self.dataSeries.Reset(self.Market)

                    #return -1
                
                self.dataSeries.AddData(self.Market, simulatedPricePrint.bid, simulatedPricePrint.offer, simulatedPricePrint.time)
                
                self.VIndex += 1
                self.dataSeries.SetDay(self.Market, day)
                
                return 1
            else:
                #debug

                
                self.VIndex = 0
                #print ("Reseting Market Data for new day")
                self.dataSeries.Reset(self.Market)
                
                return -1



#debug  - build and output simulated feed

if __name__ == "__main__":
    pass
    '''
    simulatedMarket = SimulatedFeed('eurusd', 3)
    simulatedMarket.BuildSimulatedFeed(startHour=6,endHour=10)
    
    #Run without connecting to a dataseries. Simple outout to console.  
    for day in simulatedMarket.FeedDays:
        print (day)
        simulatedMarket.StartFeed()
        tickResult = 1
        while tickResult == 1:
            tickResult = simulatedMarket.Tick(day,10)
    '''

