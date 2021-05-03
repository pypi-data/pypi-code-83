import logging
import subprocess
import os

import requests
from urllib.parse import urlparse


logger = logging.getLogger(__file__)


def prepare_api_url(host: str, api_segment: str):
    return os.path.join(host, api_segment)


def prepare_headers(api_key: str):
    headers = {
        "Authorization": "Key " + api_key,
    }
    return headers


def run_command(cmd_list, capture=True, cwd="."):
    try:
        exec = subprocess.run(cmd_list, check=True, capture_output=capture, cwd=cwd)
        return exec.stdout.decode('UTF-8').strip()
    except subprocess.CalledProcessError as e:
        logger.error("The process failed")
        logger.error(e.stderr)
        logger.error(e.stdout)
        raise e


def post_data(url, data, headers, files=None):
    try:
        res = requests.post(url, files=files, data=data, headers=headers)
        check_requests_result(res)
    except requests.exceptions.ConnectionError as e:
        parsed_uri = urlparse(url)
        logger.error(f"The host {parsed_uri.netloc} could not be reached")
        raise e


def check_requests_result(res):
    res.raise_for_status()