import requests
import json

AUTH_TOKEN_URL = 'https://api.orange.com/oauth/v3/token'


class SMS:
    def __init__(self, AUTH_TOKEN):
        self.AUTH_TOKEN = AUTH_TOKEN

    def login(self):
        headers = {
            "Authorization": self.AUTH_TOKEN,
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json" 
        }
        data = {"grant_type":"client_credentials"}
        r = requests.post(AUTH_TOKEN_URL, headers=headers, data=data)
        return  json.loads(r.text)

    def send(self, from_, to, message):
        from_in_url = from_.split('+')[1]
        url = f"https://api.orange.com/smsmessaging/v1/outbound/tel%3A%2B{from_in_url}/requests"
        data = self.login()
        access_token = data['access_token']
        headers = {
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json",
        }
        params = {}
        data = {
            "outboundSMSMessageRequest":{
                "address": "tel:" + to,
                "senderAddress": "tel:" + from_,
                "senderName": "Moke",
                "outboundSMSTextMessage":{ "message": message } 
            } 
        }
        data = json.dumps(data)
        r = requests.post(url, headers=headers, data=data)
        return  r