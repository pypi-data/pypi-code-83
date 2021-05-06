#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
usbsecurity-server is the server program to control access to USB ports.
"""

#  This module belongs to the usbsecurity-server project.
#  Copyright (c) 2021 Alexis Torres Valdes
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Contact: alexis89.dev@gmail.com

import os
import sys
import socket
import argparse

import cherrypy

from django.core.wsgi import get_wsgi_application

from usbsecurity_server.usbsecurity_server.settings import STATIC_URL, STATIC_ROOT


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


about = {}
with open(os.path.join(BASE_DIR, '__version__.py')) as f:
    exec(f.read(), about)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'usbsecurity_server.usbsecurity_server.settings')
application = get_wsgi_application()


def mount_static(url, root):
    """
    :param url: Relative url
    :param root: Path to static files root
    """
    config = {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': root,
        'tools.expires.on': False,
        'tools.expires.secs': 86400
    }
    cherrypy.tree.mount(None, url, {'/': config})


class DjangoApplication(object):
    def __init__(self, host='127.0.0.1', port=8080):
        self.host = host
        self.port = port

    def is_running(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            result = sock.connect_ex((self.host, self.port))
            return result == 0

    def run(self):
        cherrypy.config.update({
            'server.socket_host': self.host,
            'server.socket_port': self.port,
            'engine.autoreload_on': True,
            'log.screen': True
        })
        mount_static(STATIC_URL, STATIC_ROOT)

        cherrypy.log('Loading and serving application')
        cherrypy.tree.graft(application)
        if self.is_running():
            msg = 'The application is already running'
            cherrypy.log(msg)
            sys.exit(msg)

        cherrypy.engine.start()
        cherrypy.engine.block()


def parse_args():
    __version__ = about['__version__']

    parser = argparse.ArgumentParser(prog=about['__title__'], description=about['__description__'])

    parser.add_argument('-v',
                        '--version',
                        action='version',
                        version=f'%(prog)s {__version__}')
    parser.add_argument('-a',
                        '--author',
                        action='version',
                        version='%(prog)s was created by software developer Alexis Torres Valdes <alexis89.dev@gmail.com>',
                        help="show program's author and exit")

    parser.add_argument('--host',
                        default='127.0.0.1',
                        help='Host server ip address. Default: 127.0.0.1')
    parser.add_argument('--port',
                        type=int,
                        default=8888,
                        help='Server port. Default: 8888')

    return parser.parse_args()


def main():
    args = parse_args()
    host = args.host
    port = args.port

    app = DjangoApplication(host=host, port=port)
    app.run()


if __name__ == '__main__':
    main()
