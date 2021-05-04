
import os, sys, time

CONFIGPATH = os.path.join(os.path.expanduser('~'), 'tradingalgorithm', 'code', 'lucen', 'code', '')
#---add config folder to project
sys.path.insert(0,CONFIGPATH)


#---import custom config
from config import *

#---required libs
from lib import *


class Candle(object):

    def __init__(self, priceType="BID"):
        self.high = 0
        self.low = 10000000
        self.open = 0
        self.close = 0
        self.ticks = 0
        self.time = 0
        self.priceType = priceType
        self.minuteCounter = -1
        self.complete = False
        self.direction = 0


    def AddPriceTick(self, bid, offer, time):

        if bid>self.high:
            self.high = bid

        if bid<self.low:
            self.low = bid

        if self.ticks is 0:
            self.open = bid
            #print ("OpEN BID: %f" % (bid))

        self.close = bid
        self.ticks += 1
        self.time = time

        if self.open > self.close:
            self.direction = -1

        if self.open < self.close:
            self.direction = 1



    def __str__(self):
        return ("O: %f C: %f H: %f L: %f M:%s C: %s" % (self.open, self.close, self.high, self.low, self.minuteCounter, self.complete))





class CandleHolder(object):

    def __init__(self, deltaT = 1): #made into integer
        self.deltaT = deltaT
        self.candles = None
        self.fresh = True

        self.deltaTFloat = float(deltaT)
        

        #if deltaT is '1M':
        #    self.deltaTFloat = 1.0
        #if deltaT is '5M':
        #    self.deltaTFloat = 5.0

    def __str__(self):
        return ("%s : %f " % (self.deltaT, self.deltaTFloat))


    def Output(self):
        if self.candles is not None:
            for candle in self.candles:
                print(candle)

    def AddPrice(self, bid, offer, time):
        #print ("[cs] bid: %f offer: %f time: %s " % (bid, offer, time))
        #make sure we have a candle
        if self.candles is None:
            self.candles = []
            candle = Candle(priceType= "BID")
            self.candles.append(candle)

        minute = GetMinute(time)
        ActiveCandle = self.candles[len(self.candles)-1]
        if self.fresh is True:
            self.candles[0].minuteCounter = minute




        #add price to candle

        #add to existing candle

        #sort out new candle or not depending on delta T*************



        if self.deltaT == 1:
            if ActiveCandle.minuteCounter == minute:
                #add to candle
                ActiveCandle.AddPriceTick(bid, offer, time)
                self.fresh = False
                return 0

            else:
                #new candle
                #print completed cs
                #print (ActiveCandle)
                ActiveCandle.complete = True
                #print (self.candles[len(self.candles)-1])
                candle = Candle(priceType= "BID")
                candle.minuteCounter = minute
                self.candles.append(candle)
                ActiveCandle = self.candles[len(self.candles)-1]
                ActiveCandle.AddPriceTick(bid, offer, time)
                self.fresh = False
                return 0

        newCandle = False
        if self.deltaT != 1:
            mod_val = float(minute) % float(self.deltaTFloat)
            if int(mod_val) is 0:
                newCandle = True
                #print ("FSA")
                #exit()
                #print (("%f %f %f") % (mod_val, float(minute), float(self.deltaTFloat)))
        '''
        if ActiveCandle.minuteCounter == minute:
            #add to candle
            ActiveCandle.AddPriceTick(bid, offer, time)

        else:
            #new candle
            #print completed cs
            #print (ActiveCandle)
            ActiveCandle.complete = True
            #print (self.candles[len(self.candles)-1])
            candle = Candle(priceType= "BID")
            candle.minuteCounter = minute
            self.candles.append(candle)
            ActiveCandle = self.candles[len(self.candles)-1]
            ActiveCandle.AddPriceTick(bid, offer, time)
        '''



        if newCandle is True:
            if int(ActiveCandle.minuteCounter) != int(minute):
                #print ("%d %d" % (int(ActiveCandle.minuteCounter), int(minute)))
                #new candle
                #print completed cs
                #print (ActiveCandle)
                ActiveCandle.complete = True
                #print (self.candles[len(self.candles)-1])
                candle = Candle(priceType= "BID")
                candle.minuteCounter = minute
                self.candles.append(candle)
                ActiveCandle = self.candles[len(self.candles)-1]
                ActiveCandle.AddPriceTick(bid, offer, time)
                self.fresh = False
                #print ("add to new")

        if newCandle is False:
            ActiveCandle.AddPriceTick(bid, offer, time)
            self.fresh = False
            #print ("add to exist: %s" % minute)
