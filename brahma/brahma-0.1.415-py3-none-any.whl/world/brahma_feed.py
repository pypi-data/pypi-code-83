"""
Module holding root data feed for the brahma world environment.
Brahma allows for both static and data feeds to the virtual world 
with both 'sets' of data provided by a data feed. We define the root data
feed class here.

The data heirarchy in the Brahma world is divided into 4 main categories, each which must
be customised by the user for their bots/indis.

1 ->  Data Source. e.g. market prices. static or live.
!!!!!!!!!!!!!!!!!!!!!!!!
2 ->  NO!!!!Buckets: Data Source is then bundled into groups or "buckets" of data!!! This
      comes after and is handles by a bucket class for DNA to get correct data vector...
!!!!!!!!!!!!!!!!!!!!!!!!
3 ->  Epochs:  Data sources in static feeds are allowed to be divided into epochs of data.
      e.g. days of market data. At least one epoch of data is required.
3 ->  Data prints for feeding into the world. This is the stage at which data is presented into the world 
      for the bots/indis to interact with. Data must be declared and presented as a "print" which
      is read by an indi/bot for genetic evaluation.

Ignore "3" for live data feeds into the Brahma World.
"""

#------------------DERIVATION REQUIRED-----------
import time, sys

# #config core
# sys.path.append('../')
# from configCore import *

class BrahmaData(object):
  def __init__(self, type='static'):
    self.epochs = None     #list of epochs. Each  epoch has its own feed to the world

  def AddEpochs(self, epochs  = None):
    self.epochs = epochs

class DataPrint(object):
  """
  Root data print  class
  :param object: [description]
  :type object: [type]
  """

  def __init__(self, value=0, high=0, low=0):
    self.value =  value
    self.high = 0
    self.low  = 0

  def __exit__(self):
    pass

class BrahmaLiveData(object):
  def __init__(self, data_type = 'dynamic', source_file = "live.data"):
    self.dataType = data_type
    self.epoch = None
    self.sourceDataFile = source_file
    self.dataSource = LiveDataSource(source_file=source_file)
    self.running = False


  def Start(self):
    self.epoch = BrahmaEpoch(self.dataSource.dataSource)
    self.running = True

  def Tick(self):
    
    #get new values from file 
    new_data = self.dataSource.Tick()
    
    #create print which is read by bots/indis
    dp = testPricePrint(new_data[0])
    #update epoch and price feed to iter over
    self.epoch.Update(data=dp)

  def Stop(self):
    self.running = False

class LiveDataSource(object):
  def __init__(self, data = [], source_file = ""):
    self.dataSource =  data #list of data prints
    self.data_source_file = source_file

  def Tick(self):
    #update data source - grab new data and updata data. This is done from file here.
    data = self.GrabData()
    
    return data

  def GrabData(self):
    return_data = []
    with open (self.data_source_file, 'r') as f:
      lines = f.read().splitlines()
      last_line = lines[-1]
      #print (last_line)
      data = last_line.split(',')
      #print (data[0])
      return_data.append(data)
    
    #print("d {0}".format(return_data))
    
      
    return return_data
    
#-------------------NO DERIVATION-----------------


class DataSource(object):
  def __init__(self, data = []):
    self.dataSource =  data #list of data prints

class BrahmaEpoch(object):

  def __init__(self, data = None, epochTag = "root", start_idx = 0, end_idx = 0):
    self.source = data
    self.epochTag = epochTag
    self.feed = BrahmaDataFeed(self.source, self.epochTag, start_index = start_idx, end_index= end_idx)

  def Update(self, data = None):
    """
    For live data - update the feed object.

    :param data: [description], defaults to []
    :type data: list, optional
    """
    #print (data)
    self.source.append(data)
    
    

  def __str__(self):
    return ("Ind epoch Tag: {0} ".format(self.epochTag))

class Epochs(object):
  def __init__(self):
    self.epochs = []
    self.startIndex = 0
    self.index = self.startIndex

  def AddEpoch(self, newEpoch = None):
    self.epochs.append(newEpoch)

  def __iter__(self):
    return self

  def __next__(self):
    
    
    if self.index >= len(self.epochs):
      self.index = self.startIndex
      raise StopIteration
    returnFeed = self.epochs[self.index].feed
    self.index+=1
    return returnFeed


  def __str__(self):
    return ("Number of Epochs: {0}".format(len(self.epochs)))

class BrahmaDataFeed(object):
  """
  Class responsible for connecting the Brahma World to the 'environmental' data source
  for the virtual world. Environmental pressure is provided via this data and in order to allow
  fully customizable data sets and environments, this class provides the conduit of any data
  source to its corresponding. This data feed class is responsible for introducing data prints 
  into the brahma world.

  :param object: root class
  :type object: object
  """

  def __init__(self, source = None, epoch_tag = "unique", start_index = 0, end_index = 0):
    
    self.start_index = start_index
    self.end_index = end_index
    self.source = source
    self.epoch_tag = epoch_tag
    self.index  = self.start_index


  def __exit__(self):
    pass

  def __iter__(self):
    return self
    
  def __next__(self):
    #print (self.source)
    if self.index >= len(self.source):
      #print ("No values available. Data exhausted.")
      self.index = self.start_index
      raise StopIteration
    print_value = self.source[self.index]
    self.index += 1
    return print_value
  '''
  def Tick(self, data = None):
    if data != None:
      print (data)
      print (self.source)
      print (len(self.source))
      self.source.append(data)
      print (self.source)
      print (len(self.source))
      exit()
  '''

  def __str__(self):
    return ("source len: {0} epoch tag: {1}".format(len(self.source), self.epoch_tag))

  """
  Root data  source for Brahma World.

  :param object: [description]
  :type object: [type]
  """

class testPricePrint(object):
  def __init__(self, data):
   
    
    self.one =data[0]
    self.two = data[1]
    self.three = data[2]

  def __str__(self):
    return "pp: {0} {1} {2}".format(self.one, self.two, self.three)



if __name__ == "__main__":

  '''  static data example'''
  # source1 = [0,3,5,2,5,6]
  # source2 = [4,23,35,52,35,36]
  # source3 = [50,33,35,52,55,26]
  # source4 = [0,3,5,2,5,6]

  # epoch_1 = BrahmaEpoch(source1, "1")
  # epoch_2 = BrahmaEpoch(source2, "2")
  # epoch_3 = BrahmaEpoch(source3, "3")
  # epoch_4 = BrahmaEpoch(source4, "4")


  # my_epochs = Epochs()
  # my_epochs.AddEpoch(epoch_1)
  # my_epochs.AddEpoch(epoch_2)
  # my_epochs.AddEpoch(epoch_3)
  # my_epochs.AddEpoch(epoch_4)


  '''static data example'''
  #1.  define data print you will be using
  #we will  use the root one here

  #2. Build data prints - this is the main  data source
  p1 = DataPrint(15,73,2)
  p2 = DataPrint(37,36,2)
  p3 = DataPrint(14,33,42)
  p4 = DataPrint(12,53,23)
  p5 = DataPrint(13,34,32)
  p6 = DataPrint(13,33,2)
  p7 = DataPrint(1,33,2)
  p8 = DataPrint(15,33,2)
  p9 = DataPrint(16,43,2)
  p10 = DataPrint(13,3,2)
  p11 = DataPrint(12,23,2)
  p12 = DataPrint(11,34,32)


  #3. Add data to data source
  dataSource1 = DataSource(data=[p1,p3,p2])
  # print(len(dataSource1.dataSource))
  dataSource2 = DataSource(data=[p4,p5,p6])
  dataSource3 = DataSource(data=[p7,p8,p9])

  #4. place into indvidual epochs
  e1 = BrahmaEpoch(data=dataSource1.dataSource,epochTag="1")

  e2 = BrahmaEpoch(data=dataSource2.dataSource,epochTag="2")
  e3 = BrahmaEpoch(data=dataSource3.dataSource,epochTag="3")

  #5. group epochs together for the world data
  world_data_epochs = Epochs()
  world_data_epochs.AddEpoch(e1)
  world_data_epochs.AddEpoch(e2)
  world_data_epochs.AddEpoch(e3)

  #6. create world data structure which will feed the virtual world  via epochs and data feeds
  world_data = BrahmaData(type='static')
  world_data.AddEpochs(world_data_epochs)

  #7.  feed the world
  # print (world_data.epochs.epochs[0].feed)
  print (world_data.epochs)
  for epoch in world_data.epochs:
    for dp in  epoch:
      pass

  '''
  #---LIVE DATA FEED---
  print ("live feed test")

  #1. build live data
  liveData = BrahmaLiveData(source_file='live.data')

  #2. start the feed
  liveData.Start()

  # tick through data
  #liveData.Tick()

  liveData.Tick()
  
  for dp in liveData.epoch.feed:
    liveData.Tick()
    time.sleep(1)
    print (dp)

'''





  



  
  




  

