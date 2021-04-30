import logging
from datetime import date
import os
from urllib.parse import urlencode
import requests

logger = logging.getLogger(__name__)

class Api:
    """
    A class that represents an API.
    """

    def __init__(self,hostname):
        self.host = hostname 
        self.memcache = dict()

    def fetch_json(self,*args,**kwargs):
        url = self._make_url(*args,**kwargs)
        logger.info("Fetching %s",url)
        response = requests.get(url)
        if response.status_code != 200:
            logger.critical("Request to %s returned %s",
                    response.url,response.status_code
                    )
                    
            raise requests.HTTPError(response=response)
        return response.json()

    def _rel_url(self,path):
        return os.path.join(self.host,path)

    def _make_url(self,*args,**kwargs):
        path = os.path.join(*[str(e) for e in args])
        url = self._rel_url(path)
        pstring = urlencode({str(k):str(v) for k,v in kwargs.items()})
        if pstring:
            url += "?"+pstring
        return url
