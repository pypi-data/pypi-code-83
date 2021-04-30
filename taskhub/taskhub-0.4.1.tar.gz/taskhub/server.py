
from .hub import TaskHub,HubManager
from .connector import connect
from multiprocessing import Process
import time


def start_serve(port, passwd, back_end_url):
    hub = TaskHub(back_end_url)
    HubManager.register('get_hub', callable=lambda: hub)
    hubmanager = HubManager(address=("localhost", port),
                            authkey=passwd.encode("utf-8"))
    serve = hubmanager.get_server()
    serve.serve_forever()


def serve(port:int,passwd:str,back_end_url:str):
    p = Process(target=start_serve,args=(port,passwd,back_end_url,))
    p.start()
    time.sleep(3)
    hub = connect("localhost", port, passwd)
    hub.serve()
