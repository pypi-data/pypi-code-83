import logging
import unittest
import requests
import httpretty
from snec import Api

class TestSnec(unittest.TestCase):
    @httpretty.activate
    def test_api(self):
        httpretty.register_uri(
                httpretty.GET,
                "http://my_api.org/",
                body='{"status":"success"}'
                )
        httpretty.register_uri(
                httpretty.GET,
                "http://my_api.org/resource/",
                body='{"status":"its there"}'
                )

        api = Api("http://my_api.org")
        resp = api.fetch_json("")
        self.assertEqual(resp["status"],"success")
        resp = api.fetch_json("resource/")
        self.assertEqual(resp["status"],"its there")


