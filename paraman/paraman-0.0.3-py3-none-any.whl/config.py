from datetime import date, datetime
import json
import os

import click


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def is_docker():
    path = '/proc/self/cgroup'
    return (
        os.path.exists('/.dockerenv') or
        os.path.isfile(path) and any('docker' in line for line in open(path))
    )


def print_msg(msg_content, data=None, msg_type='l', terminate=False):
    if msg_type == "data" or msg_type == "d":
        msg = f">> {msg_content}\nData:\n"
    elif msg_type == "error" or msg_type == "e":
        msg = f">> [ERROR] {msg_content}"
        terminate = True
    elif msg_type == "warning" or msg_type == "w":
        msg = f">> [WARNING] {msg_content}"
    elif msg_type == "log" or msg_type == "l":
        msg = f">> [LOG] {msg_content}"

    if data:
        if isinstance(data, dict) or isinstance(data, list):
            print(
                f"{msg}\n{json.dumps(data,indent=2,sort_keys=True,default=json_serial)}"  # noqa: 501
            )
        else:
            print(f"{msg} {data}")
    else:
        print(msg)

    if terminate:
        raise Exception(msg)


def print_json(obj):
    print(json.dumps(obj, indent=2, sort_keys=True, default=json_serial))


class Config(object):
    def __init__(self, raise_error=True):
        self.verbose = False
        self.errors = 0
        self.errors_msg = ""
        self.ci = False
        self.local_dev = False
        self.endpoint_url = ""


pass_config = click.make_pass_decorator(Config, ensure=True)
