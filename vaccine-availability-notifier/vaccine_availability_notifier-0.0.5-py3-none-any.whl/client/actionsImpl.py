import requests

from vaccineAvailabilityNotifier.client.actions import Actions


def build_url(PINCODE, DATE):
    # /v2/appointment/sessions/public/calendarByPin
    return 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=' + PINCODE + '&date=' + DATE


def get_headers(params=None):
    # 'accept': 'application/json',
    # 'Accept-Language': 'hi_IN'
    return {'accept': 'application/json', 'Accept-Language': 'hi_IN'}


class ActionsImpl(Actions):

    def get(self, params={}):
        r = None
        try:
            url = build_url(PINCODE=params["pincode"], DATE=params["date"])
            r = requests.get(url, {}, headers=get_headers())
        except requests.exceptions.RequestException as e:
            exit()
        return r

    def create(self, uri, payload):
        r = None
        try:
            url = build_url()
            r = requests.post(url, data=payload, headers=get_headers())
        except requests.exceptions.RequestException as e:
            exit()
        return r

    def delete(self, uri, payload=None):
        return self.create(uri, payload)
