#!/usr/bin/python3
import os
from os import environ
import sys
from time import sleep
from datetime import datetime
import pytz
# import json
import random
import numpy as np

################################# BASIC TIME FUNCTIONS #################################
def minToSec(mins=1):
    return mins*60

def hoursToMins(hrs=1):
    return hrs*60

def hoursToSec(hrs=1):
    return hrs * 60 * 60

def getHour(tz='America/Los_Angeles'):
    tzwc=pytz.timezone(tz)
    return int(datetime.now(tzwc).hour)

def randomize_interval(ti=10,randomization=50):
    spread = ti*randomization/100
    # t = abs(round(random.uniform(ti-spread,ti+spread)))
    # return t
    rng = np.random.default_rng(); 
    # print('ti:',ti)
    # print('spread:',spread)
    n = rng.normal(ti,spread,1000)
    rand_unit = abs(round(random.choice(n))) #use randomized increment as unit
    #For Poisson distribution
    # p = rng.poisson(1, 100) #poisson dist with lambda 1 -- select random value & multiply it
    # multiplier = random.choice(p)+1
    # ri = multiplier*rand_unit
    return rand_unit

########################################## Woke Class ##########################################
class Joe:
    def __init__(self, timezone = 'America/Los_Angeles', waketime=5,bedtime=22, time_interval=30,randomzn=50):
        self.awake = True
        self.was_wake = True
        self.timezone = timezone
        self.waketime = waketime 
        self.bedtime = bedtime
        self.time_interval = time_interval
        self.randomzn = randomzn 
        self.randomize_daily_interval()

    def is_awake(self):
        hour = getHour()
        if hour >= self.waketime and hour < self.bedtime:
            self.awake = True
            if(self.was_wake == False): 
                self.wakeup()
            self.was_wake=self.awake
            return True
        else:
            print("Am asleep. Zzzz...")
            self.awake = False
            self.was_wake=self.awake
            return False

    def wakeup(self):
        print('I just woke up.')
        self.randomize_daily_interval()

    def randomize_daily_interval(self):
        spread = self.time_interval*10/100
        rng = np.random.default_rng(); 
        n = rng.normal(self.time_interval,spread,1000)
        self.daily_time_interval = abs(round(random.choice(n)))
        print("Daily time interval %s has been randomized to: %s minutes"%(self.time_interval, self.daily_time_interval))

    def get_next_interval(self):
        curr_hour = getHour()
        if(self.is_awake()):
            return randomize_interval(self.time_interval,self.randomzn)
        else: #return sleep interval to next waketime
            rand_60m = randomize_interval(60, 50)
            if(curr_hour <= self.waketime):  #if before waketime, subtract current hour i.e., 5AM - 3AM = 2 hrs & also randomize wake time by 10%
                return hoursToMins(self.waketime - curr_hour - 1) + rand_60m
            elif(curr_hour > self.bedtime): #if after waketime then must be evening
                return hoursToMins(24 - self.bedtime + self.waketime - 1) + rand_60m
            else:
                return randomize_interval(self.time_interval,self.randomzn)

