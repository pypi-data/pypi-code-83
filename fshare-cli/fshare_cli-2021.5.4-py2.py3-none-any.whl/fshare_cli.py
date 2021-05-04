import sys
import os
import logging
import colorlog

from .fshare_api import FshareAPI
from .fshare_utils import FshareUtils
from pprint import pprint

class FshareCLI:

    def __init__(self, params=None):

        if params.quiet:
            logging_level = logging.CRITICAL
        elif params.verbose:
            logging_level = logging.DEBUG
        else:
            logging_level = logging.INFO

        colorlog.basicConfig(format = '%(log_color)s%(asctime)s %(levelname)s %(module)s.%(funcName)s:%(lineno)s %(message)s')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging_level)

        if params.cmd in ['configure', 'download', 'upload', 'api']:
            self.fshare_api = FshareAPI(logging_level=logging_level)

            try:
                if params.cmd == 'configure':
                    self.fshare_api.auto_configure(forced_user_pass=True, forced_app_key=True, forced_app_name=True)
                else:
                    self.fshare_api.auto_configure()
            except Exception as e:
                self.logger.error('Invalid configs, run `fshare configure` to (re)config your Fshare credentials %s' % (e))
                sys.exit(1)

            if params.cmd == 'download':
                self.download(params.url, params.password, params.destination)
            elif params.cmd == 'upload':
                self.upload(params.file, params.password, params.destination)
            elif params.cmd == 'api':
                self.api(params.path, params.args.split())
        else:
            self.logger.error('Invalid command %s' % (params.cmd))
            sys.exit(1)

    def download(self, furl, password, destination):
        # validate url
        if not FshareUtils.is_valid_fshare_url(furl):
            self.logger.error('Invalid Fshare URL %s' % (furl))
            sys.exit(1)

        # fetch file/folder information
        try:
            info = self.fshare_api.info(furl)
            info['furl'] = furl
            self.logger.debug(info)
        except Exception as e:
            code, message = e.args
            if code == 404:
                self.logger.error('Cannot find this URL %s' % (furl))
                sys.exit(1)
            else:
                self.logger.error('Cannot fetch this URL %s: %s' % (furl, message))
                sys.exit(1)

        # download depends on file type
        if int(info['file_type']) == 0:
            self.download_folder(info, password, destination)
        elif int(info['file_type']) == 1:
            self.download_file(info, password, destination)
        else:
            self.logger.error('File type %s is not supported' % (info['file_type']))
            sys.exit(1)

    def upload(self, file, password, destination):
        try:
            size = os.path.getsize(file)
            name = os.path.basename(file)
            link = self.fshare_api.upload(name, str(size), destination)
            file = FshareUtils.upload(link['location'], file, size, 'Uploading %s' % (name))
            if password:
                self.fshare_api.create_file_pass([file['url'].split('/')[-1]], password)
        except Exception as e:
            self.logger.error(e)
            sys.exit(1)

    def api(self, path, args):
        func = self.fshare_api.mappings.get(path)
        if func:
            try:
                pprint(func(*args) if args else func())
            except TypeError as e:
                self.logger.error('Incorrect arguments %s' % (e))
            except Exception as e:
                self.logger.error(e)
        else:
            self.logger.error('Incorrect API path `%s`' % (path))
            sys.exit(1)

    def download_folder(self, info, password, destination):
        self.logger.debug(info)

        files = self.fshare_api.get_folder_list(info['furl'])
        files = filter(lambda info: info['file_type'] == 1, files)

        for i, file in enumerate(files):
            self.download_file(file, password, destination, '[%s/%s]' % (i + 1, len(files)))

    def download_file(self, info, password, destination, progress='[1/1]'):
        self.logger.debug(info)

        file = (info.get('ftitle') or info.get('name'))
        if destination:
            os.makedirs(destination, exist_ok=True)
            path = '%s/%s' % (destination, file)
        else:
            path = file

        if os.path.exists(path) and os.path.getsize(path) == int(info['size']):
            self.logger.warning('%s File %s existed at %s' % (progress, file, path))
        else:
            if FshareUtils.is_valid_password(password, info['pwd']):
                link = self.fshare_api.download(info['furl'], password)
                FshareUtils.download(link['location'], path, int(info['size']), '%s Downloading %s' % (progress, file))
            else:
                self.logger.error('%s Invalid password for Fshare URL %s' % (progress, info['furl']))
