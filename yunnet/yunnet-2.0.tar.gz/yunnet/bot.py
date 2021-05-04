import httpx as requests
import json


class Bot:

    __unt = None
    __polling_url = None
    __last_event_id = 0

    def __init__(self, untSession):
        self.__unt = untSession

        pollingData = untSession.execute("realtime.connect", {"mode": "polling"})[
            "response"
        ]

        self.__polling_url = pollingData["url"]
        self.__last_event_id = pollingData["last_event_id"]

    def __iter__(self):
        return self

    def __next__(self):
        return self.getEvent()

    def listen(self):
        return self

    def getEvent(self):
        res = json.loads(
            requests.get(
                self.__polling_url + str("&last_event_id=") + str(self.__last_event_id)
            ).text
        )

        if "error" in res:
            raise ValueError("Polling stopped by server")

        if "last_event_id" in res:
            self.__last_event_id = int(res["last_event_id"]) + 1

        return res
