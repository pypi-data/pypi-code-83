from ejtraderIQ import IQOption


api = IQOption('emerson@ejtrader.com','Olatikas@123','DEMO')

def sendorder():
    for _ in range(1000):
        id = api.buy(1,'EURUSD','M1')
   

