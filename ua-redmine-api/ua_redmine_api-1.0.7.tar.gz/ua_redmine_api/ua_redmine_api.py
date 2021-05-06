import requests
from requests.auth import HTTPBasicAuth
import json


class RedmineApi():
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def get(self, endpoint, **kwargs):
        response = requests.get(
            f"{self.host}/{endpoint}.json",
            auth=HTTPBasicAuth(self.username, self.password),
            **kwargs,
        )
        response.raise_for_status()
        if response.content:
            return json.loads(response.content)

    def put(self, endpoint, data, **kwargs):
        response = requests.put(
            f"{self.host}/{endpoint}.json",
            auth=HTTPBasicAuth(self.username, self.password),
            json=data,
            **kwargs,
        )
        response.raise_for_status()
        if response.content:
            return json.loads(response.content)

    def post(self, endpoint, data, **kwargs):
        response = requests.post(
            f"{self.host}/{endpoint}.json",
            auth=HTTPBasicAuth(self.username, self.password),
            json=data,
            **kwargs,
        )
        response.raise_for_status()
        if response.content:
            return json.loads(response.content)

    def delete(self, endpoint, **kwargs):
        response = requests.delete(
            f"{self.host}/{endpoint}.json",
            auth=HTTPBasicAuth(self.username, self.password),
            **kwargs,
        )
        response.raise_for_status()
        if response.content:
            return json.loads(response.content)
