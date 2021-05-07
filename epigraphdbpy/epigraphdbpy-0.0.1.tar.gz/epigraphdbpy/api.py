"""API management
"""
import webbrowser, os, json, requests
import epigraphdbpy.constants as cons
from retry import retry
from urllib.parse import urljoin

MAX_TRIES = 10
TRIES_DELAY = 5  # seconds
TRIES_BACKOFF = 2


@retry(tries=MAX_TRIES, delay=TRIES_DELAY, backoff=TRIES_BACKOFF)
def ping_api():
    """This is a simple function to ping the API.  
    Returns:
        boolean: true if API is responsive
    """
    path = "/ping"
    url = urljoin(cons.url, path)
    response = requests.get(url)
    return response.json()
