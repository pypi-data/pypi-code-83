#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import requests
import argparse
import socket
import os
import subprocess
import time
try:
    import psutil
except:
    subprocess.Popen('python3 -m pip install psutil', shell=True).wait()
    import psutil

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = BASE_DIR.replace('\\', '/')

parser = argparse.ArgumentParser(
    description='EasyCompleteYou, Easily complete you.')
parser.add_argument('--stop', action='store_true', help='stop everything')

parser.add_argument('--is_use_cloudfare',
                    action='store_true',
                    help='stop everything')

parser.add_argument('--domain', help='domain for server')
g_args = parser.parse_args()


def IsProcessExist(name):
    pids = psutil.pids()
    for pid in pids:
        try:
            p = psutil.Process(pid)
            temp = p.name()
            if name == temp:
                return True
        except Exception as e:
            pass
    print(name, 'is not exist.')
    return False


SERVER_API_KEY = "123"


def MyRequest(url, dicts):
    try:
        global SERVER_API_KEY
        dicts['api_key'] = SERVER_API_KEY
        resp = requests.get(url, params=dicts, timeout=10)
        return resp.text
    except Exception as e:
        print(e)
    return ""


def GetCurrentOS():
    temp = sys.platform
    if temp == 'win32':
        return 'Windows'
    if temp == 'cygwin':
        return 'Cygwin'
    if temp == 'darwin':
        return 'Mac'
    return 'Linux'


if GetCurrentOS() == 'Linux':
    LINUX_CADDY_PATH = BASE_DIR + '/caddy/caddy_2.3.0_linux_amd64/caddy'
    LINUX_V2RAY_PATH = BASE_DIR + '/v2ray/linux/v2ray-linux-64/v2ray'
    LINUX_CONTR_PATH = BASE_DIR + '/controler/contro_linux'
else:
    LINUX_CADDY_PATH = BASE_DIR + '/caddy/caddy_2.3.0_windows_amd64/caddy.exe'
    LINUX_V2RAY_PATH = BASE_DIR + '/v2ray/windows/v2ray-windows-64/v2ray.exe'
    LINUX_CONTR_PATH = BASE_DIR + '/controler/contro_windows.exe'


def GetPermission():
    if GetCurrentOS() == 'Linux':
        cmd = "sudo chmod -R 750 " + BASE_DIR
        subprocess.Popen(cmd, shell=True).wait()


def RunV2ray(argv=""):
    cmd = LINUX_V2RAY_PATH + ' ' + argv
    if GetCurrentOS == 'Linux':
        cmd = 'sudo nohup %s' % (cmd)
    print(cmd)
    subprocess.Popen(cmd, shell=True)
    RunControler()
    print('v2ray is running.')


def Die():
    KillCaddy()
    KillV2ray()


def KillV2ray():
    cmd = LINUX_V2RAY_PATH + ' stop'
    subprocess.Popen(cmd, shell=True)
    print('v2ray dead')


def RunControler(argv=""):
    cmd = LINUX_CONTR_PATH + ' ' + argv
    if GetCurrentOS == 'Linux':
        cmd = 'sudo nohup %s' % (cmd)
    print(cmd)
    subprocess.Popen(cmd, shell=True)
    print('controler is running.')


def RunCaddy(argv=""):
    cmd = LINUX_CADDY_PATH + ' ' + argv
    if GetCurrentOS == 'Linux':
        cmd = 'sudo nohup %s' % (cmd)
    print(cmd)
    subprocess.Popen(cmd, shell=True)
    print('caddy is running.')


def KillCaddy():
    cmd = LINUX_CADDY_PATH + ' stop'
    subprocess.Popen(cmd, shell=True)
    print('caddy dead')


def GetMyIP(is_ipv6=False):
    if is_ipv6:
        return MyRequest('https://v6.ident.me/', {})
    return MyRequest('https://v4.ident.me/', {})


def CheckPort(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0


class V2ray_And_Caddy():
    def __init__(self, v2ray_config, caddy_config):
        self.v2ray_config = v2ray_config
        self.caddy_config = caddy_config
        self.caddy_test_address = 'http://127.0.0.1:3566'
        if CheckPort(80) or CheckPort(443):
            raise ValueError("port 80 or 443 is in use.")

        RunCaddy(argv='run -config "%s" -adapter caddyfile' %
                 (self.caddy_config))
        RunV2ray(argv='-config "%s"' % (self.v2ray_config))
        time.sleep(10)

    def Die(self):
        KillCaddy()
        KillV2ray()

    def TestCaddyOK(self):
        if GetCurrentOS() != 'Linux':
            return True
        if MyRequest(self.caddy_test_address, {}) != 'ok':
            return False
        return True


class Caddy_TLS_WS_VMESS:
    """ domain is needed
    """
    def __init__(self, domain=None, is_ipv6=True, use_cloudfare=False):
        self.is_init = False
        if CheckPort(80) or CheckPort(443):
            raise ValueError("port 80 or 443 is in use.")

        self._init_domain(domain, use_cloudfare)
        self.InitV2rayConfig(is_ipv6)

        self.InitCaddyConfig()

        # run
        self.instance = V2ray_And_Caddy(self.v2ray_config_file_path,
                                        self.caddy_config_file_path)
        self.is_init = True

    def InitV2rayConfig(self, is_ipv6):
        # v2ray
        if is_ipv6:
            self.v2ray_config_file_path = BASE_DIR + '/v2ray_server_configs/vmess_tls_ws_ipv6.json'
        else:
            self.v2ray_config_file_path = BASE_DIR + '/v2ray_server_configs/vmess_tls_ws.json'
        self.v2ray_config_file_path = BASE_DIR + '/v2ray_server_configs/vmess_tls_ws_free.json'

    def _init_domain(self, domain, is_use_cloudfare):
        self.is_use_cloudfare = is_use_cloudfare
        if domain is not None:
            self.domain = domain
            if not self.is_use_cloudfare:
                domain_ip = socket.gethostbyname(self.domain)
                my_ip = GetMyIP()
                if my_ip != domain_ip:
                    print(my_ip, domain_ip)
                    raise ValueError('wrong dns ip')
        else:
            self.domain = 'localhost'

    def Del(self):
        if self.is_init is False:
            return
        self.instance.Die()
        print('已关闭 %s' % (self.domain))

    def InitCaddyConfig(self):

        self.caddy_config_file_path = BASE_DIR + '/caddy_config/tls_ws.caddyfile'
        self.caddy_template_config_file_path = BASE_DIR + '/caddy_config/tls_ws.template'

        with open(self.v2ray_config_file_path, encoding='utf-8') as f:
            content = f.read()
        print('v2ray config', content)

        with open(self.caddy_template_config_file_path,
                  encoding='utf-8') as caddy:
            content = caddy.read()

        content = content.replace('{domain}', self.domain)
        print('caddy config', content)

        with open(self.caddy_config_file_path, 'w', encoding='utf-8') as caddy:
            caddy.write(content)


GetPermission()  # we need to

if __name__ == '__main__':
    if g_args.stop:
        Die()
    elif g_args.domain is None:
        temp = Caddy_TLS_WS_VMESS()
    else:
        temp = Caddy_TLS_WS_VMESS(g_args.domain,
                                  use_cloudfare=g_args.is_use_cloudfare)
