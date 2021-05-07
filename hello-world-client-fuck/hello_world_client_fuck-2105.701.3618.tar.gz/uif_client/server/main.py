import requests
import json
import time
import subprocess
from aiohttp import web

SERVER_API_KEY = "123"
MAX_ALLOW_USING = 4

g_user_list = {}


def MyRequest(url, dicts, is_return=True):
    try:
        resp = requests.get(url, params=dicts, timeout=10)
        return resp.text
    except Exception as e:
        print(e)
    return ""


def Get(dicts, key, default_value=""):
    if key in dicts:
        return dicts[key]
    return default_value


def DisConnect(user_key, client_address):
    if user_key == "" or client_address == "":
        return
    payload = {
        'type': 'DisConnect',
        'user_key': user_key,
        'api_key': SERVER_API_KEY
    }
    MyRequest(client_address, payload)


def CountUsedFlow(user_dict):
    for item in user_dict['used']:
        pass
    return


def CheckOutDate(user_dict):
    t = time.time()
    t = int(t)
    user_dict['last_time'] = t

    if 'pass_time' not in user_dict:
        user_dict['is_out_date'] = True
        return True

    if user_dict > t:
        user_dict['is_out_date'] = True
        return True
    user_dict['is_out_date'] = False
    return False


def AddUser(user_key, client_address):
    if client_address in g_user_list[user_key]['using']:
        return
    g_user_list[user_key]['using'].append(client_address)
    if len(g_user_list[user_key]['using']) > MAX_ALLOW_USING:
        DisConnect(user_key, g_user_list[user_key]['using'].pop())


def UserLogin(params, user_key):
    if user_key not in g_user_list:
        g_user_list[user_key] = {}
        g_user_list[user_key]['using'] = []
    client_address = Get(params, 'client_address')
    if client_address == '':  # should not happen
        status = 2
    else:
        AddUser(user_key, client_address)
        status = 0
        if CheckOutDate(g_user_list[user_key]):
            status = 1
            for item in g_user_list[user_key]['using']:  # DisConnect all
                if item == client_address:  # avoid dead lock # avoid dead lock # avoid dead lock
                    continue
                DisConnect(user_key, item)

    return json.dumps({'params': g_user_list[user_key], 'status': status})


async def API(req):
    params = req.rel_url.query
    user_key = Get(params, 'user_key')
    api_key = Get(params, 'api_key')
    client_address = Get(params, 'client_address')
    if api_key != SERVER_API_KEY or user_key == '':
        return web.Response(text="fuck")
    types = Get(params, 'type')
    text = ""
    if types == 'UserLogin':
        text = UserLogin(params, user_key)
    elif types == "DisConnect":
        text = DisConnect(user_key, client_address)
    return web.Response(text=text)


app = web.Application()
app.add_routes([web.get('/api', API)])

if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1", port="8081")
