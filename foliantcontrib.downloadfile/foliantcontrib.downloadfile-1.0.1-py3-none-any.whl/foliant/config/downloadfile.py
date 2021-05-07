import base64
import os
import ssl

from hashlib import md5
from pathlib import Path
from pathlib import PosixPath
from urllib.error import HTTPError
from urllib.parse import urlparse
from urllib.request import Request
from urllib.request import urlopen

from yaml import add_constructor

from foliant.config.base import BaseParser
from foliant.utils import output


class BadConfigException(Exception):
    pass


class DownloadError(Exception):
    pass


class Parser(BaseParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.downloadfile_cache_dir = self.project_path / '.downloadfilecache'

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

        return download_file(self.project_path, node.value, save_to=save_to)

    def parse(self, *args, **kwargs) -> dict:
        config = super().parse(*args, **kwargs)
        if 'downloadfile' in config:
            downloader = FileDownloader(
                config['downloadfile'],
                self.logger,
                project_path=self.project_path,
                quiet=self.quiet
            )
            downloader.download_all()
        return config


class FileDownloader:
    defaults = {
        'queue': [],
        'fail_fast': True,
    }

    def __init__(self,
                 config: dict,
                 logger,
                 project_path: PosixPath = Path(),
                 quiet: bool = False):
        self.config = {**self.defaults, **config}
        self.logger = logger.getChild('downloadfile')
        self.project_path = project_path
        self.quiet = quiet

    def download_file(self, file_info: dict):
        if 'url' not in file_info:
            raise BadConfigException('url must be specified for all queue elements.')
        download_file(self.project_path, **file_info)

    def download_all(self):
        for file_dict in self.config['queue']:
            try:
                self.download_file(file_dict)
            except (BadConfigException, DownloadError) as e:
                if self.config['fail_fast']:
                    raise
                else:
                    self.logger.warning(f'{e}. Skipping.')
                    output(f'{e}. Skipping.', self.quiet)


def download_file(
    root_dir: PosixPath,
    url: str,
    save_to: str or None = None,
    login: str or None = None,
    password: str or None = None,
    ignore_ssl_errors: bool = False,
) -> str:
    context = ssl._create_unverified_context() if ignore_ssl_errors else None
    request = Request(url)

    dest = root_dir / (save_to or get_file_name_from_url(url))
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
