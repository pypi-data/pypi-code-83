import time
import os
from client_base import kill_proc_tree
print("Please open: http://zuizhongkeji.com:8090")
try:
    while True:
        time.sleep(1)
except:
    kill_proc_tree(os.getpid())
