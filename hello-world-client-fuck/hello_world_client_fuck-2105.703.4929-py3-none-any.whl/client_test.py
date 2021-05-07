import uuid
import socket
import time
import requests
import subprocess

import install

SERVER_API_KEY = '123'

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    g_current_ip = s.getsockname()[0]
    print(g_current_ip)
except Exception as e:
    s.close()
    print(e)
    raise ValueError('failed to get VPS IPv4')


def MyRequest(url, dicts):
    try:
        global SERVER_API_KEY
        dicts['api_key'] = SERVER_API_KEY
        resp = requests.get(url, params=dicts, timeout=10)
        return resp.text
    except Exception as e:
        print(e)
    return ""


#install deps
subprocess.Popen('python3 -m pip install psutil', shell=True).wait()
subprocess.Popen('python3 -m pip install aiohttp', shell=True).wait()

subprocess.Popen('python3 ./uif_client --domain abc.com', shell=True)

subprocess.Popen('python3 ./uif_client/server/main.py', shell=True)

time.sleep(20)

# check if it's running
if not install.IsProcessExist('contro_linux') or not install.IsProcessExist(
        'v2ray'):
    raise ValueError('no runing')

# check UserLogin function
my_uuid = uuid.uuid1()
url = 'http://%s:8082' % (g_current_ip)

print('UserLogin ', MyRequest(url, {'type': 'UserLogin', 'user_key': my_uuid}))

# check DisConnect function
print('DisConnect ', MyRequest(url, {
    'type': 'DisConnect',
    'user_key': my_uuid
}))

# check Quit function
print('Close ', MyRequest(url, {'type': 'Quit'}))

# check if Quit ok
if install.IsProcessExist('contro_linux') or install.IsProcessExist('v2ray'):
    raise ValueError('failed to close')
