import os
import hashlib
import math
import json
import pycurl

from urllib.parse import urlparse
from sys import stderr as STREAM
from tqdm import tqdm
from io import BytesIO

class FshareUtils:

    @classmethod
    def is_valid_fshare_url(cls, furl):
        url = urlparse(furl)
        return (
            url.scheme in ['http', 'https']
            and url.netloc in ['fshare.vn', 'www.fshare.vn']
            and len(url.path.split('/')) >= 3
            and url.path.split('/')[1] in ['file', 'folder']
        )

    @classmethod
    def is_valid_password(cls, plain_pass, hashed_pass):
        if hashed_pass:
            if plain_pass:
                return hashlib.sha1(plain_pass.encode('utf-8')).hexdigest() == hashed_pass
            else:
                return False
        else:
            return True

    @classmethod
    def convert_bytes(cls, bytes, unit=None):
        if bytes == 0:
            return (0, 'B')
        size_name = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
        i = size_name.index(unit) if unit else int(math.floor(math.log(bytes, 1024)))
        p = math.pow(1024, i)
        s = round(bytes / p, 1)
        return (s, size_name[i])

    @classmethod
    def upload(cls, url, file, size, desc):
        with tqdm(total=size, unit='iB', unit_scale=True) as pbar:
            pbar.set_description(desc)
            total_ul_d = [0]
            output = BytesIO()
            def status(download_t, download_d, upload_t, upload_d, total=total_ul_d):
                pbar.update(upload_d - total[0])
                total[0] = upload_d

            response = False
            c = pycurl.Curl()
            c.setopt(pycurl.URL, url)
            c.setopt(pycurl.VERBOSE, False)
            c.setopt(pycurl.NOPROGRESS, False)
            c.setopt(pycurl.PROGRESSFUNCTION, status)
            # upload
            c.setopt(pycurl.UPLOAD, 1)
            c.setopt(pycurl.READFUNCTION, open(file, 'rb').read)
            c.setopt(pycurl.INFILESIZE, size)
            c.setopt(pycurl.WRITEFUNCTION, output.write)
            # upload
            c.perform()
            c.close()

            return json.loads(output.getvalue().decode('iso-8859-1'))

    @classmethod
    def download(cls, url, file, size, desc):
        with tqdm(total=size, unit='iB', unit_scale=True) as pbar:
            pbar.set_description(desc)
            total_dl_d = [0]
            def status(download_t, download_d, upload_t, upload_d, total=total_dl_d):
                pbar.update(download_d - total[0])
                total[0] = download_d

            with open(file, 'wb') as f:
                c = pycurl.Curl()
                c.setopt(pycurl.URL, url)
                c.setopt(pycurl.VERBOSE, False)
                c.setopt(pycurl.NOPROGRESS, False)
                c.setopt(pycurl.PROGRESSFUNCTION, status)
                # download
                c.setopt(pycurl.WRITEDATA, f)
                # download
                c.perform()
                c.close()
