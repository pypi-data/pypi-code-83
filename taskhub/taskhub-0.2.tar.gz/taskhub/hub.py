import random
import time
import json
import requests 
import traceback
from multiprocessing.managers import BaseManager


from retry import retry
from loger import makelog

class HubManager(BaseManager):
    pass


class Task():
    key = ""
    priority = 1
    data = dict()
    status = "wait"
    start_time = 0
    nodeId = 0

    def __init__(self,key:str,priority:int,data:dict):
        if isinstance(key, str) and isinstance(priority, int) and isinstance(data, dict) and 0 < priority < 1000000:
            self.key = key
            self.priority = priority if priority < 1000000 else 1000000
            self.data = data
        else:
            raise TaskInitError()
    def get_dict(self):
        return {
            "key": self.key,
            "priority": self.priority,
            "status": self.status,
            "data": self.data,
            "start_time": self.start_time,
            "nodeId": 0
        }
    def __str__(self): 
        return json.dumps(self.get_dict())


class TaskHub():
    name = "taskhub"
    tasks = dict()
    lock = False
    back_end_url = ""
    timeout = 600
    check_gap = 20

    def __init__(self,back_end_url):
        self.back_end_url = back_end_url

        pass
    def add(self,task:Task):
        # 加锁
        self.get_lock()
        # 检查是否存在
        if not self.tasks.get( task.key):
            # 不存在则设置
            self.tasks[task.key] =task
            makelog("task added!",4)
            # 释放锁并返回
            self.release_lock()
            return True
        else:
            # 存在则释放锁并抛出异常
            self.release_lock()
            raise TaskAlreadyExist()

    def get(self,nodeId:int):
        # 加锁
        self.get_lock()
        # 根据优先级排序 然后便利
        for key, task in sorted(self.tasks.items(),reverse=True,key=lambda item:item[1].priority):
            # 获取第一个是wait的 设置数据并返回
            if task.status == "wait":
                task.node_id = nodeId
                task.status = "running"
                self.release_lock()
                return  task
        else:
            # 全部遍历后均没有wait则释放锁返回None
            self.release_lock()
    
    def upload(self,task:Task):
                # 加锁
                self.get_lock()
                # 检查任务是否存在
                target_task = self.tasks.get(task.key)
                if target_task:
                    # 检查任务状态是否正确
                    if target_task.status == "running":
                        # 检查nodeid是否正确
                        if target_task.nodeId == task.nodeId:
                            target_task.data = task.data
                            target_task.status = "done"
                            self.release_lock()
                            return True
                        else:
                            self.release_lock()
                            raise NodeIdNotMatch()
                    else:
                        self.release_lock()
                        raise TaskNotRunning()
                else:
                    self.release_lock()
                    raise TaskNotExist()

    def serve(self):
        t = 0
        while True:
            if time.time() - t > self.check_gap:
                # 加锁
                self.get_lock()

                # 输出状态
                status_str = "tasks: "
                for key, task in self.tasks.items():
                    status_str += "{}：{}\t".format(key, task.status)
                makelog(status_str)

                # 检查需要同步的数据
                for key,task in self.tasks.items():
                    if task.status == "done":
                        # 将数据同步到后端
                        if self.sync(task):
                            del self.tasks[key]

                # 释放锁
                self.release_lock() 
                t = time.time()
                time.sleep(1)
 
    def sync(self,task):
        makelog("syncing...")
        try:
            r_data = self.req(task)
        except :
            makelog("sync: req 时发生异常：{}".format(traceback.format_exc()),1)
            return False
        else:
            if r_data.get("suc"):
                makelog("synced!", 4)
                return True
            else:
                makelog("sync: 返回状态异常：{}".format(r_data))
                return False

    
    @retry(tries=5,delay=1,backoff=1)
    def req(self,task:Task):
        r = requests.post(self.back_end_url,json=task.get_dict())
        r.raise_for_status
        return r.json()

    def get_lock(self):
        # makelog("getting lock ....")
        while self.lock:
            time.sleep(random.random())
        self.lock = True
        # makelog("lock got!")

    def release_lock(self):
        self.lock=False
        # makelog("lock released!")


class TaskIdExitRequired(Exception):
    def __str__(task):
        return "id is required for a task dict!{}".format(task)


class TaskAlreadyExist(Exception):
    def __str__(task_id):
        return "task {} already exist! ".format(task_id)


class TaskNotExist(Exception):
    def __str__():
        return "task not exist! "


class TaskInitError(Exception):
    def __str__(task_id):
        return "task pramar invalid! key:str priority:0<int<1000000 data:dict"


class TaskNotRunning(Exception):
    def __str__(self,task):
        return "task should be running but it in {} now".format(task.status)


class NodeIdTypeError(Exception):
    def __str__(nodeId):
        return "nodeId must be int!"


class NodeIdNotMatch(Exception):
    def __str__(self, task_nodeId, nodeId):
        return "nodeId doesn`t match! task nodeid = {} your node id = {}".format(task_nodeId,nodeId)
