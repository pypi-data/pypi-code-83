import logging
import requests


logger = logging.getLogger(__name__)


def make_get_request(url):
    logger.debug(f'Sending GET request to {url}')
    response = requests.get(url)
    logger.debug(f'Got response:\n{response.text}')
    response.raise_for_status()
    return response


def make_post_request(url, headers):
    logger.debug(
        f'Sending POST request to {url} with headers {headers}')
    response = requests.post(url,
                             data=None,
                             headers=headers)
    logger.debug(f'Got response:\n{response.text}')
    response.raise_for_status()
    return response
