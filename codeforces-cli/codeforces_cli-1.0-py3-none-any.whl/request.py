import requests
import time
import random
import json

time_now = round(time.time() * 1000)
ran_num = random.randint(100000, 999999)

class codeforces_request:
    def __init__(self):
        self.url = "https://codeforces.com/api/"
        self.ran_num = ran_num
        self.secret = "dff892750fb999f23683265055512a9a32f93800"
        self.key = "0b970824b5d3892a23e590d2976679672c2c2a45"
        self.time_now = time_now

    def make_request(self, new_url, params):
        res = requests.get(new_url, params=params)
        json_data = json.loads(res.text)
        return json_data