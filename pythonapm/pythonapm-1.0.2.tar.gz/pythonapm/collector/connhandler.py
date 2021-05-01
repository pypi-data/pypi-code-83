import platform
import requests
import json
import time
from pythonapm import constants
from pythonapm.agentfactory import get_agent
from pythonapm.constants import api_connect, api_data
from pythonapm.logger import agentlogger
from pythonapm.collector.reqhandler import send_req
from pythonapm.collector.reshandler import handle_connect_response
from pythonapm.collector.datahandler import process_collected_data


task_spawned = False
conn_payload = None

def init_connection():
    global task_spawned
    try:
        if task_spawned is True:
            return
        
        import threading
        t = threading.Thread(target=background_task, args=(), kwargs={})
        t.setDaemon(True)
        t.start()
        task_spawned = True

    except Exception as exc:
        agentlogger.exception('Error while spawning thread')
        

def background_task():
    conn_success = False
    while(get_agent().insinfo.get_status() != constants.shutdown):
        try:
            if conn_success is False:
                conn_success = send_connect()
            else:
                process_collected_data()
        except Exception:
            agentlogger.exception('pythonapm task error')
        finally:
            get_agent().get_metric_store().cleanup()
            time.sleep(60)


def send_connect():
    payload = getconn_payload() if conn_payload is None else conn_payload
    res_data = send_req(api_connect, payload)
    return handle_connect_response(res_data)


def getconn_payload():
    global conn_payload
    config = get_agent().get_config()
    conn_payload = { 
            "agent_info" : { 
            "agent_version": '1.0',
            "host_type": platform.system(), 
            "hostname": platform.node()
        }, "environment" : { 
            "os_version": platform.release(), 
            "machine_name": platform.node(), 
            'AgentInstallPath': config.get_installed_dir(), 
            "python_version": platform.python_version(), 
            "osarch": platform.machine(), 
            "os": platform.system(),
        }
    }
    return conn_payload
