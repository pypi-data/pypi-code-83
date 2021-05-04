import datetime
import json
import random
import requests
import threading

from django.utils import timezone

import callcounter

class Capturer:
    def __init__(self, get_response):
        self.get_response = get_response
        self.debug = False
        self.project_token = callcounter.project_token
        self.buffer = []
        self.buffer_start = datetime.datetime.now()

    def __call__(self, request):
        start = datetime.datetime.now()
        response = self.get_response(request)
        finish = datetime.datetime.now()

        if self.project_token and callcounter.track(request):
            t = threading.Thread(target=self.background_work, args=(start, finish, request, response))
            t.start()

        return response

    def send_buffer(self):
        try:
            requests.post(url='https://api.callcounter.eu/api/v1/events/batch.json',
                    headers={ 'Content-Type': 'application/json',
                            'User-Agent': 'callcounter-pip ({})'.format(callcounter.__version__) },
                    data=json.dumps({ 'batch': { 'project_token': self.project_token, 'events': self.buffer }}))
        finally:
            self.buffer_start = datetime.datetime.now()
            self.buffer = []

    def should_send_buffer(self):
        return self.buffer_start < datetime.datetime.now() - datetime.timedelta(0, random.randint(300, 359)) \
                or len(self.buffer) > 25

    def background_work(self, start, finish, request, response):
        self.buffer.append({
                'created_at': str(timezone.localtime()),
                'elapsed_time': (finish - start).total_seconds() * 1000,
                'method': request.method,
                'path': request.path,
                'user_agent': request.META['HTTP_USER_AGENT'],
                'status': response.status_code,
            })

        if self.should_send_buffer():
            self.send_buffer()
