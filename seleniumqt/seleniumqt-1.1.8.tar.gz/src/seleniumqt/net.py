# -*- coding: utf-8 -*-
import json
import os
import requests
import traceback
from random import Random


def random_str(ran_len=8):
    ran_str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(ran_len):
        ran_str += chars[random.randint(0, length)]
    return ran_str


def android_page_img(root_path, upload_file):
    file_path = os.path.join(root_path, upload_file.name)
    f = open(file_path, 'wb')
    for chunk in upload_file.chunks():
        print('开始上传文件', upload_file)
        f.write(chunk)
    f.close()
    return file_path


def server_get(url, path):
    try:
        url_path = '%s/%s/' % (url, path)
        res = requests.get(url=url_path)
        return json.loads(res.text)
    except:
        traceback.print_exc()


def server_post(url, path, data):
    try:
        url_path = '%s/%s/' % (url, path)
        res = requests.post(url=url_path, data=data)
        return json.loads(res.text)
    except:
        traceback.print_exc()
