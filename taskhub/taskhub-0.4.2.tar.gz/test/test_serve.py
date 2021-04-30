import requests

from taskhub.server import serve
from retry import retry
from loger import makelog

address = "127.0.0.1"


def sync(task):
    back_end_url = ""
    @retry(tries=5, delay=1, backoff=1)
    def req(self, task: Task):
        r = requests.post(back_end_url, json=task.get_dict())
        r.raise_for_status
        return r.json()

    makelog("syncing...")
    try:
        r_data = req(task)
    except:
        makelog("sync: req 时发生异常：{}".format(traceback.format_exc()), 1)
        return False
    else:
        if r_data.get("suc"):
            makelog("synced!", 4)
            return True
        else:
            makelog("sync: 返回状态异常：{}".format(r_data))
            return False



if __name__ == "__main__":
    serve(
        port=2333, 
        passwd="1qaz2wsx", 
      sync=sync)
