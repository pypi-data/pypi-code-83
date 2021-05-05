#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import requests
import argparse
import time
import socket
import threading
import json
import subprocess

try:
    from aiohttp import web
except:
    cmd = "pip3 install aiohttp"
    subprocess.Popen(cmd, shell=True).wait()
    from aiohttp import web

import install

parser = argparse.ArgumentParser(
    description='EasyCompleteYou, Easily complete you.')
parser.add_argument('--stop', action='store_true', help='stop everything')

parser.add_argument('--is_use_cloudfare',
                    action='store_true',
                    help='stop everything')

parser.add_argument('--domain', help='domain for server')
g_args = parser.parse_args()


def Get(dicts, key, default_value=""):
    if key in dicts:
        return dicts[key]
    return default_value


def GetCurrentOS():
    temp = sys.platform
    if temp == 'win32':
        return 'Windows'
    if temp == 'cygwin':
        return 'Cygwin'
    if temp == 'darwin':
        return 'Mac'
    return 'Linux'


def AllowPort(port):
    if GetCurrentOS() == 'Linux':
        subprocess.Popen('ufw allow %s' % (port), shell=True).wait()


def DeletePort(port):
    if GetCurrentOS() == 'Linux':
        subprocess.Popen('ufw delete allow %s' % (port), shell=True).wait()


SERVER_API_KEY = "123"


def MyRequest(url, dicts, is_return=True):
    try:
        global SERVER_API_KEY
        dicts['api_key'] = SERVER_API_KEY
        resp = requests.get(url, params=dicts, timeout=10)
        return resp.text
    except Exception as e:
        print(e)
    return ""


class ClassName(object):
    def __init__(self, CLIENT_API_PORT="8082"):
        self.SERVER_API_UIL = "http://uifv2ray.xyz:8081/api"
        self.SERVER_API_UIL = "http://127.0.0.1:8081/api"  # for test

        self.CLIENT_API_PORT = CLIENT_API_PORT
        self.GO_REMOVE_USER_URL = "http://127.0.0.1:9090/removeUser"
        self.GO_ADD_USER_URL = "http://127.0.0.1:9090/addUser"
        self.GO_CLOSE_URL = "http://127.0.0.1:9090/quit"

        self.g_current_ip = ''
        self.ClientInfo()

        DeletePort(9090)  # my v2ray grpc port
        DeletePort(10085)  # v2ray grpc original prot

        AllowPort(self.CLIENT_API_PORT)  # client
        AllowPort(80)
        AllowPort(443)
        global SERVER_API_KEY
        self.SERVER_API_KEY = SERVER_API_KEY

        self.g_user_list = {}

    def CloseClient(self):
        MyRequest(self.ClientInfo(), {'type': 'Quit'})
        quit()

    def Start(self):
        global g_args
        self.bg = install.Caddy_TLS_WS_VMESS(
            g_args.domain, use_cloudfare=g_args.is_use_cloudfare)

        app = web.Application()
        threading.Thread(target=self._heart_beat).start()
        app.add_routes([web.get('/', self.Dispash)])
        web.run_app(app,
                    host=self.g_current_ip,
                    port=int(self.CLIENT_API_PORT))  # block here

    def Die(self):
        install.Die()
        self.CloseControler()
        quit()

    async def Dispash(self, req):  # Request from user
        params = req.rel_url.query
        user_key = Get(params, 'user_key')
        api_key = Get(params, 'api_key')
        if user_key == '':
            return web.Response(text="fuck")
        types = Get(params, 'type')
        text = "wrong type"
        if types == 'UserLogin':
            text = self.UserLogin(params, user_key)
        elif types == 'DisConnect' and api_key == self.SERVER_API_KEY:
            text = self.DisConnect(user_key)
        elif types == 'Quit' and api_key == self.SERVER_API_KEY:
            self.Die()
        return web.Response(text=text)

    def ClientInfo(self):  # myself info
        if self.g_current_ip == '':
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(('8.8.8.8', 80))
                self.g_current_ip = s.getsockname()[0]
            except Exception as e:
                s.close()
                print(e)
                raise ValueError('failed to get VPS IPv4')
        return "http://%s:%s/api" % (self.g_current_ip, self.CLIENT_API_PORT)

    def _heart_beat(self):
        while True:
            time.sleep(20 * 60)  # 20 minutes
            for item in self.g_user_list:
                MyRequest(
                    self.SERVER_API_UIL, {
                        'user_key': item,
                        'type': 'Update',
                        'used_flow': self.ReadUserFlow(item)
                    })

    def ReadUserFlow(self, user_key):
        try:
            return "1"
        except Exception as e:
            print(e)
            return ""

    def DisConnect(self, user_key):  # remove user
        if user_key not in self.g_user_list:
            return
        del self.g_user_list[user_key]
        res = MyRequest(self.GO_REMOVE_USER_URL, {'user_key': user_key})
        return res

    def _add_user(self, user_key):  # can only call by center's server
        t = time.time()
        t = int(t)
        if user_key not in self.g_user_list:
            self.g_user_list[user_key] = {}
        self.g_user_list[user_key]['last_time'] = t
        print(MyRequest(self.GO_ADD_USER_URL, {'user_key': user_key}))

    def CloseControler(self):
        print(MyRequest(self.GO_CLOSE_URL, {}))

    def UserLogin(self, params, user_key):
        payload = {
            'type': 'UserLogin',
            'user_key': user_key,
            'client_address': self.ClientInfo()
        }
        res = ""
        try:
            res = MyRequest(self.SERVER_API_UIL, payload)
            temp = json.loads(res)
            if temp['status'] == 0:  # check by server
                self._add_user(user_key)
            else:
                self.DisConnect(user_key)

            # for safety reason
            # try:
            #     del temp['params']['using']
            # except:
            #     pass
            # res = json.dumps(temp)
        except Exception as e:
            print(e)
        return res


if __name__ == '__main__':
    temp = ClassName()
    if g_args.stop:
        temp.CloseClient()  # die here
    temp.Start()
    temp.CloseClient()  # die here
