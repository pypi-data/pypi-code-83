import base64
import os
import ssl

from hashlib import md5
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlparse
from urllib.request import Request
from urllib.request import urlopen

from yaml import add_constructor

from foliant.config.base import BaseParser


class BadConfigException(Exception):
    pass


class DownloadError(Exception):
    pass


class Parser(BaseParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.downloadfile_cache_dir = '.downloadfilecache'

        add_constructor('!download', self._resolve_download_tag)

    def _resolve_download_tag(self, _, node) -> str:
        '''
        Download file from link after ``!download``, save it into
        cachedir and replace tag with absolute path to this file.
        '''

        url = node.value
        file_ext = get_file_ext_from_url(url)
        url_hash = md5(url.encode()).hexdigest()
        save_to = os.path.join(self.downloadfile_cache_dir, url_hash + file_ext)

        return download_file(node.value, save_to=save_to)

    def parse(self, *args, **kwargs) -> dict:
        config = super().parse(*args, **kwargs)
        if 'downloadfile' in config:
            downloader = FileDownloader(config['downloadfile'], self.logger)
            downloader.download_all()
        return config


class FileDownloader:
    defaults = {
        'queue': []
    }

    def __init__(self, config: dict, logger):
        self.config = {**self.defaults, **config}
        self.logger = logger.getChild('downloadfile')

    def download_file(self, file_info: dict):
        if 'url' not in file_info:
            raise BadConfigException('url must be specified for all queue elements.')
        download_file(**file_info)

    def download_all(self):
        for file_dict in self.config['queue']:
            self.download_file(file_dict)


def download_file(
    url: str,
    save_to: str or None = None,
    login: str or None = None,
    password: str or None = None,
    ignore_ssl_errors=False,
) -> str:
    context = ssl._create_unverified_context() if ignore_ssl_errors else None
    request = Request(url)

    dest = save_to if save_to else get_file_name_from_url(url)
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)

    if login and password:
        b64_creds = base64.b64encode(bytes(f'{login}:{password}', 'ascii')).decode('utf-8')
        request.add_header('Authorization', f'Basic {b64_creds}')
    try:
        response = urlopen(request, context=context)
    except HTTPError as e:
        raise DownloadError(f'Cannot open URL {url}: {e}')
    with open(dest, 'wb') as f:
        f.write(response.read())
    return str(dest.resolve())


def get_file_name_from_url(url: str) -> str:
    parsed = urlparse(url)
    return os.path.basename(parsed.path)


def get_file_ext_from_url(url: str) -> str:
    filename = get_file_name_from_url(url)
    return os.path.splitext(filename)[1]
