from .hub import TaskHub, HubManager

def connect(ip:str,port:int,passwd:str):
    HubManager.register('get_hub')
    m = HubManager(address=(ip,port), authkey=passwd.encode("utf-8"))
    m.connect()
    return m.get_hub()
