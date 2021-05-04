import os
import logging
import colorlog

import requests
import json
import hashlib
import math

from easysettings import EasySettings
import getpass
from urllib.parse import urlparse

class FshareAPI:

    def __init__(self, logging_level=logging.INFO):

        colorlog.basicConfig(format = '%(log_color)s%(asctime)s %(levelname)s %(module)s.%(funcName)s:%(lineno)s %(message)s')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging_level)

        self.headers = {}

        self.mappings = {
            '/api/user/login': self.login,
            '/api/user/logout': self.logout,
            '/api/user/refreshToken': self.refresh_token,
            '/api/user/get': self.me,

            '/api/session/upload': self.upload,
            '/api/session/download': self.download,

            '/api/fileops/get': self.info,
            '/api/fileops/list': self.list,
            '/api/fileops/getTotalFileInFolder': self.get_total_file_in_folder,
            '/api/fileops/createFolder': self.create_folder,
            '/api/fileops/rename': self.rename,
            '/api/fileops/move': self.move,
            '/api/fileops/delete': self.delete,
            '/api/fileops/createFilePass': self.create_file_pass,
            '/api/fileops/changeSecure': self.change_secure,
            '/api/fileops/duplicate': self.duplicate,
            '/api/fileops/getFolderList': self.get_folder_list,
            '/api/fileops/getTopFollowMovie': self.get_top_follow_movie,
            '/api/fileops/getListFollow': self.get_list_follow,
            '/api/fileops/followFolder': self.follow_folder,
            '/api/fileops/unFollowFolder': self.unfollow_folder,
            '/api/fileops/listFavorite': self.list_favorite,
            '/api/fileops/ChangeFavorite': self.change_favorite,

            '/api/share/SetDirectLink': self.set_direct_link,
        }

    def auto_configure(self, location='.fshare', forced_user_pass=False, forced_app_key=False, forced_app_name=False):
        os.makedirs(os.path.expanduser('~/%s' % (location)), exist_ok=True)
        self.settings = EasySettings(os.path.expanduser('~/%s/fshare-cli.conf' % (location)))

        # credential
        username = self.settings.get('username', None)
        password = self.settings.get('password', None)
        app_key  = self.settings.get('app_key', None)
        app_name = self.settings.get('app_name', None)

        while not username or not password or forced_user_pass:
            username = input('Your username [Current: %s]: ' % username) or username
            password = getpass.getpass('Your password [Current: %s]: ' % ("***" if password else "None")) or password
            self.settings.set('username', username)
            self.settings.set('password', password)
            self.settings.save()
            forced_user_pass = False # avoid infinitive loop

        while not app_key or forced_app_key:
            app_key  = input('Your app key  [Current: %s]: ' % (app_key)) or app_key
            self.settings.set('app_key', app_key)
            self.settings.save()
            forced_app_key = False # avoid infinitive loop

        while not app_name or forced_app_name:
            app_name = input('Your app name [Current: %s]: ' % (app_name)) or app_name
            self.settings.set('app_name', app_name)
            self.settings.save()
            forced_app_name = False # avoid infinitive loop

        self.headers['User-Agent'] = self.settings.get('app_name')

        # session
        session_id = self.settings.get('session_id', None)
        token      = self.settings.get('token', None)

        if session_id and token and not (forced_user_pass or forced_app_name or forced_app_key):
            self.headers['Cookie'] = 'session_id=%s' % (self.settings.get('session_id'))

            try:
                self.info('https://www.fshare.vn/file/WIJUHJ16K28R')
                self.logger.info('Re-logged in successfully')
            except Exception as e:
                self.logger.warning('Session expired, re-logging in...')
                self.settings.remove('session_id')
                self.settings.remove('token')
                self.settings.save()
                self.auto_configure(location)
        else:
            auth = self.login()

            self.settings.set('session_id', auth['session_id'])
            self.settings.set('token', auth['token'])
            self.settings.save()

            self.headers['Cookie'] = 'session_id=%s' % (self.settings.get("session_id"))

            self.logger.debug(auth)
            self.logger.info('Logged in successfully')

    # +--------------------------------------+ #
    # | Login - Logout - User info           | #
    # +--------------------------------------+ #
    def login(self):
        return self.post('/api/user/login', {
            'user_email': self.settings.get('username'),
            'password': self.settings.get('password'),
            'app_key': self.settings.get('app_key'),
        })

    def logout(self):
        return self.get('/api/user/logout')

    def refresh_token(self):
        return self.post('/api/user/refreshToken', {
            'token': self.settings.get('token'),
            'app_key': self.settings.get('app_name'),
        })

    def me(self):
        return self.get('/api/user/get')

    # +--------------------------------------+ #
    # | File manager                         | #
    # +--------------------------------------+ #
    def upload(self, name, size, path, secured=1):
        return self.post('/api/session/upload', {
            'name': name,
            'size': size,
            'path': path,
            'secured': secured,
            'token': self.settings.get('token'),
        })

    def download(self, furl, password='', zipflag=0):
        return self.post('/api/session/download', {
            'url': furl,
            'password': password,
            'zipflag': zipflag,
            'token': self.settings.get('token'),
        })

    # TODO: undocumented
    def info(self, furl):
        return self.post('/api/fileops/get', {
            'url': furl,
            'token': self.settings.get('token'),
        })

    def list(self, path='', pageIndex=0, dirOnly=0, limit=100, ext=''):
        return self.get('/api/fileops/list?path=%s&pageIndex=%s&dirOnly=%s&limit=%s&ext=%s' % (path, pageIndex, dirOnly, limit, ext))

    def get_total_file_in_folder(self, furl, have_file=False):
        return self.post('/api/fileops/getTotalFileInFolder', {
            'url': furl,
            'have_file': have_file,
            'token': self.settings.get('token'),
        })

    def create_folder(self, name, in_dir="0"):
        return self.post('/api/fileops/createFolder', {
            'name': name,
            'in_dir': in_dir,
            'token': self.settings.get('token'),
        })

    def rename(self, new_name, linkcode):
        return self.post('/api/fileops/rename', {
            'new_name': new_name,
            'file': linkcode,
            'token': self.settings.get('token'),
        })

    def move(self, items, to):
        return self.post('/api/fileops/move', {
            'items': items,
            'to': to,
            'token': self.settings.get('token'),
        })

    def delete(self, items):
        return self.post('/api/fileops/delete', {
            'items': items,
            'token': self.settings.get('token'),
        })

    def create_file_pass(self, items, password):
        return self.post('/api/fileops/createFilePass', {
            'items': items,
            'pass': password,
            'token': self.settings.get('token'),
        })

    def change_secure(self, items, status=1):
        return self.post('/api/fileops/changeSecure', {
            'items': items,
            'status': status,
            'token': self.settings.get('token'),
        })

    def set_direct_link(self, items, status=1):
        return self.post('/api/share/SetDirectLink', {
            'items': items,
            'status': status,
            'token': self.settings.get('token'),
        })

    def duplicate(self, linkcode, path='', confirm=True):
        return self.post('/api/fileops/duplicate', {
            'linkcode': linkcode,
            'path': path,
            'confirm': confirm,
            'token': self.settings.get('token'),
        })

    # +--------------------------------------+ #
    # | Follow - Public Folder - User Action | #
    # +--------------------------------------+ #
    def get_folder_list(self, furl, pageIndex=0, dirOnly=0, limit=100):
        return self.post('/api/fileops/getFolderList', {
            'url': furl,
            'pageIndex': pageIndex,
            'dirOnly': dirOnly,
            'limit': limit,
            'token': self.settings.get('token'),
        })

    def get_top_follow_movie(self):
        return self.get('/api/fileops/getTopFollowMovie')

    def get_list_follow(self):
        return self.get('/api/fileops/getListFollow')

    def follow_folder(self, furl):
        return self.post('/api/fileops/followFolder', {
            'link': furl,
            'token': self.settings.get('token'),
        })

    def unfollow_folder(self, furl):
        return self.post('/api/fileops/unFollowFolder', {
            'link': furl,
            'token': self.settings.get('token'),
        })

    # +--------------------------------------+ #
    # | Favorite                             | #
    # +--------------------------------------+ #
    def list_favorite(self):
        return self.get('/api/fileops/listFavorite')

    def change_favorite(self, furls, status=0):
        return self.post('/api/fileops/ChangeFavorite', {
            'items': furls,
            'status': status,
            'token': self.settings.get('token'),
        })

    # +--------------------------------------+ #
    # | Utilities                            | #
    # +--------------------------------------+ #
    def get(self, endpoint):
        return self.request('get', endpoint)

    def post(self, endpoint, payload):
        return self.request('post', endpoint, payload)

    def request(self, method, endpoint, payload=None):
        self.logger.debug('%s %s headers=%s payload=%s' % (method, endpoint, self.headers, payload))
        response = requests.request(
            method = method,
            url = 'https://api.fshare.vn%s' % (endpoint),
            headers = self.headers,
            json = payload,
        )

        if response.headers['Content-Type'].find('application/json') >= 0:
            response_json = response.json()

            self.logger.debug(response_json)

            if response.status_code == 200:
                return response_json
            else:
                raise Exception(response.status_code, response_json['msg'])
        elif response.headers['Content-Type'].find('text/html') >= 0:
            # lengthly html page so no debug logging here
            raise Exception(response.status_code, response.text)
        else:
            self.logger.debug(response.text)
            raise Exception(response.status_code, response.text)
