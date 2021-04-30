from .req_handler import *

class plucker:
    def __init__(self,urls):
        self.urls = urls
        self.requests = 16
        self.timeout = 5
    
    def get(self,tag):
        return req(tag,self)
        
