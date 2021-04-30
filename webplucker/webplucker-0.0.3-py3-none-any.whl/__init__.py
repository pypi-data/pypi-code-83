from .req_handler import *

class plucker:
    def __init__(self,urls):
        self.urls = urls
        self.requests = 10
        self.timeout = 5
        self.verbose = True
        self.organised = False
    
    def cssselect(self,tag):
        return req(tag,self,'css')
    
    def xpath(self,tag):
        return req(tag,self,'xpath')
